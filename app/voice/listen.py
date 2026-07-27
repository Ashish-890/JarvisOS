import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import tempfile
import os

# Use CPU for now
model = WhisperModel("base", device="cpu", compute_type="int8")


def listen(seconds=5):
    print("🎤 Listening...")

    fs = 16000

    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    # Create temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        temp_path = temp.name

    # Save recording
    write(temp_path, fs, recording)

    # Transcribe
    segments, info = model.transcribe(
    temp_path,
    language="en",
    beam_size=5
    )

    text = ""

    for segment in segments:
        text += segment.text

    # Clean up safely
    try:
        os.remove(temp_path)
    except PermissionError:
        pass

    return text.strip()