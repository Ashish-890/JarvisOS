import re

from app.registry.registry import registry
from app.router.command import Command
from app.router.intent import Intent
from app.router.normalizer import CommandNormalizer
from app.router.patterns import PatternRouter


class IntentClassifier:
    """
    JarvisOS Natural Language Understanding Engine

    Pipeline

    Speech
        ↓
    Pattern Router
        ↓
    Normalizer
        ↓
    Explicit Commands
        ↓
    Implicit Apps/Websites
        ↓
    Search Intent
        ↓
    AI Chat
    """

    def __init__(self):

        self.normalizer = CommandNormalizer()
        self.patterns = PatternRouter()

        self.OPEN_WORDS = (
            "open",
            "launch",
            "start",
            "run",
        )

        self.SEARCH_WORDS = (
            "search",
            "find",
            "lookup",
            "look up",
            "google",
        )

        self.YOUTUBE_WORDS = (
            "youtube",
            "watch",
            "play on youtube",
        )

        self.GITHUB_WORDS = (
            "github",
            "search github",
            "find on github",
        )

    # =====================================================

    def classify(self, text: str) -> Command:

        raw = text

        text = self.patterns.normalize(text)

        text = self.normalizer.normalize(text)

        # =====================================================
        # OPEN
        # =====================================================

        match = re.match(
            r"^(open|launch|start|run)\s+(.+)$",
            text,
        )

        if match:

            target = registry.resolve_alias(
                self.normalizer.normalize_app(
                    match.group(2)
                )
            )

            if registry.website_exists(target):

                return Command(
                    intent=Intent.OPEN_WEBSITE,
                    raw_text=raw,
                    target=target,
                    confidence=0.99,
                )

            if registry.app_exists(target):

                return Command(
                    intent=Intent.OPEN_APP,
                    raw_text=raw,
                    target=target,
                    confidence=0.99,
                )

            if registry.is_url(target):

                return Command(
                    intent=Intent.OPEN_WEBSITE,
                    raw_text=raw,
                    target=target,
                    confidence=0.98,
                )

            return Command(
                intent=Intent.OPEN_APP,
                raw_text=raw,
                target=target,
                confidence=0.70,
            )

        # =====================================================
        # GOOGLE SEARCH
        # =====================================================

        google_patterns = [

            r"^search (.+)$",

            r"^find (.+)$",

            r"^look up (.+)$",

            r"^lookup (.+)$",

            r"^google (.+)$",

            r"^search google for (.+)$",
        ]

        for pattern in google_patterns:

            match = re.match(pattern, text)

            if match:

                query = match.group(1).strip()

                return Command(
                    intent=Intent.GOOGLE_SEARCH,
                    raw_text=raw,
                    target=query,
                    query=query,
                    confidence=0.98,
                )

        # =====================================================
        # YOUTUBE SEARCH
        # =====================================================

        youtube_patterns = [

            r"^youtube (.+)$",

            r"^watch (.+)$",

            r"^search youtube for (.+)$",

            r"^find on youtube (.+)$",
        ]

        for pattern in youtube_patterns:

            match = re.match(pattern, text)

            if match:

                query = match.group(1).strip()

                return Command(
                    intent=Intent.YOUTUBE_SEARCH,
                    raw_text=raw,
                    target=query,
                    query=query,
                    confidence=0.99,
                )

        # =====================================================
        # GITHUB SEARCH
        # =====================================================

        github_patterns = [

            r"^github (.+)$",

            r"^search github for (.+)$",

            r"^find on github (.+)$",
        ]

        for pattern in github_patterns:

            match = re.match(pattern, text)

            if match:

                query = match.group(1).strip()

                return Command(
                    intent=Intent.GITHUB_SEARCH,
                    raw_text=raw,
                    target=query,
                    query=query,
                    confidence=0.99,
                )

        # =====================================================
        # SAVE MEMORY
        # =====================================================

        match = re.match(
            r"^remember (.+)$",
            text,
        )

        if match:

            return Command(
                intent=Intent.SAVE_MEMORY,
                raw_text=raw,
                content=match.group(1),
                confidence=0.99,
            )

        # =====================================================
        # RECALL MEMORY
        # =====================================================

        if text in {

            "what do you remember",

            "what do you know about me",

            "tell me what you remember",

            "recall memory",

        }:

            return Command(
                intent=Intent.RECALL_MEMORY,
                raw_text=raw,
                confidence=0.99,
            )

        # =====================================================
        # IMPLICIT APPS
        # =====================================================

        target = registry.resolve_alias(text)

        if registry.app_exists(target):

            return Command(
                intent=Intent.OPEN_APP,
                raw_text=raw,
                target=target,
                confidence=0.95,
            )

        # =====================================================
        # IMPLICIT WEBSITES
        # =====================================================

        if registry.website_exists(target):

            return Command(
                intent=Intent.OPEN_WEBSITE,
                raw_text=raw,
                target=target,
                confidence=0.95,
            )

        # =====================================================
        # DIRECT URL
        # =====================================================

        if registry.is_url(text):

            return Command(
                intent=Intent.OPEN_WEBSITE,
                raw_text=raw,
                target=text,
                confidence=0.95,
            )

        # =====================================================
        # CHAT
        # =====================================================

        return Command(
            intent=Intent.CHAT,
            raw_text=raw,
            confidence=0.90,
        )