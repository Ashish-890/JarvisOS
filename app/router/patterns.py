"""
Natural language patterns used by Jarvis.

Everything here is converted into a simple command
before the classifier runs.
"""

import re


class PatternRouter:

    def __init__(self):

        self.patterns = [

            # -----------------------------------------
            # OPEN
            # -----------------------------------------

            (
                r"^(please )?(could you )?(can you )?"
                r"(open|launch|start|run) (.+)$",

                lambda m: f"open {m.group(5)}",
            ),

            # -----------------------------------------
            # GO TO WEBSITE
            # -----------------------------------------

            (
                r"^(go to|take me to|show me) (.+)$",

                lambda m: f"open {m.group(2)}",
            ),

            # -----------------------------------------
            # GOOGLE SEARCH
            # -----------------------------------------

            (
                r"^(search google for|google) (.+)$",

                lambda m: f"search google for {m.group(2)}",
            ),

            # -----------------------------------------
            # YOUTUBE SEARCH
            # -----------------------------------------

            (
                r"^(search youtube for|youtube) (.+)$",

                lambda m: f"search youtube for {m.group(2)}",
            ),

            # -----------------------------------------
            # PLAY MUSIC
            # -----------------------------------------

            (
                r"^play (.+)$",

                lambda m: f"play {m.group(1)}",
            ),

        ]

    # ==================================================

    def normalize(self, text):

        text = text.lower().strip()

        for pattern, action in self.patterns:

            match = re.match(pattern, text)

            if match:

                return action(match)

        return text