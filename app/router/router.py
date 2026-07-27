from app.router.classifier import IntentClassifier


class Router:

    def __init__(self):

        self.classifier = IntentClassifier()

    def route(self, text):

        return self.classifier.classify(text)