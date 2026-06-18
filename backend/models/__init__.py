"""
Nothing Could Be Better — Data Models

Immutable dataclasses for the core domain objects.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class UserProfile:
    """A nihilist seeking connection in the void."""
    username: str
    dread_level: int  # 1-10 scale of existential dread
    favorite_nothing: str
    bio: str
    quote: str = "We are all here on earth to do nothing."
    joined: str = field(default_factory=lambda: datetime.now().isoformat())

    @property
    def dread_category(self) -> str:
        return dread_category(self.dread_level)


@dataclass(frozen=True)
class Match:
    """A compatibility match between two profiles."""
    user_a: str  # username
    user_b: str  # username
    score: float  # 0.0 to 1.0
    reason: str

    @property
    def is_compatible(self) -> bool:
        return self.score >= 0.6


@dataclass(frozen=True)
class ForumPost:
    """An existential musing on the void board."""
    author: str
    title: str
    body: str
    created: str = field(default_factory=lambda: datetime.now().isoformat())
    reactions: list = field(default_factory=lambda: ["☁️"])


@dataclass(frozen=True)
class Tagline:
    """An existential tagline for the landing page."""
    text: str
    author: str


def dread_category(level: int) -> str:
    """Map dread level (1-10) to a category string."""
    if level <= 3:
        return "mild"
    elif level <= 6:
        return "moderate"
    elif level <= 9:
        return "severe"
    else:
        return "transcendent"


DEFAULT_TAGLINES = [
    Tagline("You won't find what you're looking for.", "Sartre"),
    Tagline("The void is looking back.", "Nietzsche"),
    Tagline("Everything matters. Nothing means anything.", "Cioran"),
    Tagline("Life is a temporary condition, usually fatal.", "Wilde"),
    Tagline("We are all in the gutter, but some of us are looking at the stars.", "Wilde"),
    Tagline("The meaning of life is that it stops meaning.", "Camus"),
    Tagline("To be or not to be — either way, same difference.", "Shakespeare"),
    Tagline("The universe is under no obligation to make sense to you.", "Feynman"),
]


def get_default_taglines() -> list[Tagline]:
    """Return the default set of existential taglines."""
    return DEFAULT_TAGLINES
