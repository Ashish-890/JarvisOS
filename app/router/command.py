from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from app.router.intent import Intent


@dataclass(slots=True)
class Command:
    """
    A structured representation of a user's request.

    Every input source (voice, GUI, keyboard, API, etc.)
    should eventually produce one of these objects.
    """

    # --------------------------------------------------
    # Required
    # --------------------------------------------------

    intent: Intent

    raw_text: str

    # --------------------------------------------------
    # Optional extracted information
    # --------------------------------------------------

    target: str | None = None

    query: str | None = None

    content: str | None = None

    parameters: dict[str, Any] = field(default_factory=dict)

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    confidence: float = 1.0

    source: str = "voice"

    timestamp: datetime = field(default_factory=datetime.now)

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    def has_target(self) -> bool:
        return self.target is not None

    def has_query(self) -> bool:
        return self.query is not None

    def has_content(self) -> bool:
        return self.content is not None

    def add_parameter(self, key: str, value: Any) -> None:
        self.parameters[key] = value

    def get_parameter(self, key: str, default=None):
        return self.parameters.get(key, default)

    # --------------------------------------------------
    # Pretty Print
    # --------------------------------------------------

    def __str__(self):

        parts = [
            f"intent={self.intent.value}",
            f"confidence={self.confidence:.2f}",
        ]

        if self.target:
            parts.append(f"target='{self.target}'")

        if self.query:
            parts.append(f"query='{self.query}'")

        if self.content:
            parts.append(f"content='{self.content}'")

        if self.parameters:
            parts.append(f"parameters={self.parameters}")

        return "Command(" + ", ".join(parts) + ")"