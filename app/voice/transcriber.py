import tempfile
import os

from scipy.io.wavfile import write
from faster_whisper import WhisperModel


class Transcriber:

    def __init__(self):

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8",
        )

    def transcribe(self, audio):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav",
        ) as temp:

            path = temp.name

        write(path, 16000, audio)

        segments, info = self.model.transcribe(
            path,
            language="en",
            beam_size=5,
        )

        text = ""

        for segment in segments:
            text += segment.text

        try:
            os.remove(path)
        except PermissionError:
            pass

        return text.strip()