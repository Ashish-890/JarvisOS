from app.voice.wakeword import WakeWordDetector

detector = WakeWordDetector()

detector.wait_for_wake_word()

print("Wake word detected!")