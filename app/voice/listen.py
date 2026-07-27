from app.voice.recorder import Recorder
from app.voice.transcriber import Transcriber

recorder = Recorder()
transcriber = Transcriber()

IGNORE_WORDS = {
    "you",
    "yeah",
    "okay",
    "ok",
    "thanks",
    "thank you",
    "hmm",
    "um",
    "uh",
}


def listen():

    audio = recorder.record()

    # Nobody spoke
    if audio is None:
        return ""

    text = transcriber.transcribe(audio).strip()

    if not text:
        return ""

    if text.lower() in IGNORE_WORDS:
        return ""

    return text