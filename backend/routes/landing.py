"""
Landing page routes — existential taglines and hero section.
"""

from fastapi import APIRouter
from backend.models import get_default_taglines

router = APIRouter(prefix="/api/landing")


@router.get("/taglines")
def list_taglines() -> dict:
    """Return the current set of existential taglines."""
    taglines = get_default_taglines()
    return {
        "taglines": [
            {"text": t.text, "author": t.author}
            for t in taglines
        ]
    }


@router.get("/hero")
def hero_section() -> dict:
    """Return hero section data for the landing page."""
    return {
        "title": "Nothing Could Be Better",
        "subtitle": "A dating site for nihilists",
        "body": "Find someone to stare into the void with. No algorithms, no ads, no meaning — just you and the abyss.",
        "cta": "Enter the Void",
        "cta_href": "/profiles",
    }


@router.get("/about")
def about() -> dict:
    """Return the about page content."""
    return {
        "title": "About Nothing",
        "content": "Nothing Could Be Better is a gathering place for people who believe life has no objective meaning, purpose, or intrinsic value. We don't make money on this site. We don't want to change the world. We just want to find someone who gets it.",
        "philosophy": "Everything matters so little that we might as well enjoy it.",
    }
