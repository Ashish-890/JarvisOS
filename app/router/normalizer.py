import re


class CommandNormalizer:
    """
    Cleans and standardizes user commands before
    the classifier processes them.
    """

    # --------------------------------------------
    # Words that don't affect meaning
    # --------------------------------------------

    FILLER_WORDS = [

        "hey jarvis",
        "jarvis",

        "please",

        "could you",

        "can you",

        "would you",

        "will you",

        "for me",

        "kindly",

        "just",

    ]

    # --------------------------------------------
    # App aliases
    # --------------------------------------------

    APP_ALIASES = {

        "google chrome": "chrome",
        "chrome browser": "chrome",

        "visual studio code": "vscode",
        "vs code": "vscode",
        "vs-code": "vscode",
        "code": "vscode",

        "calculator": "calculator",
        "calc": "calculator",

        "notepad": "notepad",

        "paint": "paint",

    }

    # --------------------------------------------
    # Command aliases
    # --------------------------------------------

    COMMAND_ALIASES = {

        "launch": "open",

        "start": "open",

        "run": "open",

    }

    # ==========================================================
    # Normalize Entire Sentence
    # ==========================================================

    def normalize(self, text: str) -> str:

        text = text.lower()

        # Remove punctuation
        text = re.sub(r"[^\w\s']", " ", text)

        # Remove filler words
        for filler in self.FILLER_WORDS:

            text = text.replace(filler, " ")

        # Remove duplicate spaces
        text = re.sub(r"\s+", " ", text).strip()

        # Normalize command verbs
        words = text.split()

        if words:

            first = words[0]

            if first in self.COMMAND_ALIASES:

                words[0] = self.COMMAND_ALIASES[first]

        text = " ".join(words)

        return text

    # ==========================================================
    # Normalize Application Names
    # ==========================================================

    def normalize_app(self, app: str) -> str:

        app = self.normalize(app)

        return self.APP_ALIASES.get(app, app)