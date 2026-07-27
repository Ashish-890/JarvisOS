import pyttsx3
import re


def clean_text(text):
    text = re.sub(r"\\\[|\\\]", "", text)
    text = re.sub(r"[*#`]", "", text)
    return text.strip()


def speak(text):
    text = clean_text(text)

    engine = pyttsx3.init()      # Create a new engine every time
    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

    # Clean up the engine object
    del engine