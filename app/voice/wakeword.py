import time

import numpy as np
import openwakeword
import sounddevice as sd
from openwakeword.model import Model


class WakeWordDetector:

    def __init__(self):

        # Download OpenWakeWord models (only downloads once)
        openwakeword.utils.download_models()

        # Initialize model once
        self.model = Model()

        # Audio settings
        self.sample_rate = 16000
        self.chunk_size = 1280

        # Detection settings
        self.threshold = 0.80          # Increase if false triggers occur
        self.required_hits = 3         # Consecutive detections needed
        self.cooldown = 1.5            # Seconds before listening again

        # Debug mode
        self.debug = False

    def wait_for_wake_word(self):

        print("🟢 Waiting for wake word...")

        consecutive_hits = 0

        try:

            with sd.InputStream(
                samplerate=self.sample_rate,
                channels=1,
                dtype="int16",
                blocksize=self.chunk_size,
            ) as stream:

                while True:

                    audio, overflowed = stream.read(self.chunk_size)

                    if overflowed:
                        continue

                    audio = audio.flatten().astype(np.int16)

                    predictions = self.model.predict(audio)

                    best_word = None
                    best_score = 0.0

                    for wakeword, score in predictions.items():

                        if score > best_score:
                            best_word = wakeword
                            best_score = score

                    if self.debug:
                        print(f"{best_word}: {best_score:.2f}")

                    if best_score >= self.threshold:

                        consecutive_hits += 1

                    else:

                        consecutive_hits = 0

                    if consecutive_hits >= self.required_hits:

                        print(
                            f"✅ Wake word detected: "
                            f"{best_word} ({best_score:.2f})"
                        )

                        # Reset internal OpenWakeWord buffers
                        self.model.reset()

                        # Prevent immediate retrigger
                        time.sleep(self.cooldown)

                        return

        except Exception as e:

            print(f"Wake word error: {e}")

            time.sleep(1)