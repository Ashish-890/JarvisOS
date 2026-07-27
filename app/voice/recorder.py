import time

import numpy as np
import sounddevice as sd


class Recorder:

    def __init__(self):

        # Audio settings
        self.sample_rate = 16000
        self.channels = 1
        self.chunk_size = 1024

        # Voice detection
        self.threshold = 700          # Increase if room is noisy
        self.wait_timeout = 8         # Seconds to wait for speech
        self.max_silence = 1.2        # Seconds of silence before stopping
        self.min_speech = 0.4         # Ignore accidental bumps/noise

    def record(self):

        print("🎤 Waiting for speech...")

        recording = []

        speech_started = False

        speech_start_time = None
        waiting_start = time.time()

        silence_start = None

        stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16",
            blocksize=self.chunk_size,
        )

        stream.start()

        try:

            while True:

                audio, _ = stream.read(self.chunk_size)

                volume = np.abs(audio).mean()

                # -----------------------------------
                # WAITING FOR USER TO SPEAK
                # -----------------------------------
                if not speech_started:

                    if time.time() - waiting_start > self.wait_timeout:

                        print("⏰ No speech detected.")

                        return None

                    if volume > self.threshold:

                        speech_started = True
                        speech_start_time = time.time()

                        print("🟢 Speech detected.")

                        recording.append(audio.copy())

                    continue

                # -----------------------------------
                # RECORDING
                # -----------------------------------
                recording.append(audio.copy())

                if volume > self.threshold:

                    silence_start = None

                else:

                    if silence_start is None:
                        silence_start = time.time()

                    elif time.time() - silence_start >= self.max_silence:
                        break

            # Ignore accidental clicks/coughs
            speech_duration = time.time() - speech_start_time

            if speech_duration < self.min_speech:

                print("⚠️ Speech too short.")

                return None

            print("✅ Recording finished.")

            return np.concatenate(recording, axis=0)

        finally:

            stream.stop()
            stream.close()

            # Give Windows a moment to release the microphone
            time.sleep(0.2)