"""
Matching routes — find compatible nihilists.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/matches")


def _build_user_obj(profile_dict: dict) -> object:
    """Build a UserProfile-like dict for matching."""
    from backend.models import UserProfile
    return UserProfile(
        username=profile_dict["username"],
        dread_level=profile_dict["dread_level"],
        favorite_nothing=profile_dict["favorite_nothing"],
        bio=profile_dict["bio"],
        quote=profile_dict.get("quote", ""),
    )


@router.get("/search")
def search_matches(username: str) -> list[dict]:
    """Find matches for a given user."""
    from backend.store import store
    from backend import services

    user_profile = store.get_profile(username)
    if not user_profile:
        raise HTTPException(status_code=404, detail=f"{username} hasn't materialized yet")

    user_obj = _build_user_obj(user_profile)

    candidates = []
    for p in store.list_profiles():
        if p["username"] != username:
            candidates.append(_build_user_obj(p))

    matches = services.find_matches(user_obj, candidates)
    return [
        {
            "match_user": m.user_b,
            "score": m.score,
            "reason": m.reason,
            "compatible": m.is_compatible,
        }
        for m in matches
    ]


@router.get("/top")
def top_matches(username: str, n: int = 3) -> list[dict]:
    """Find the top N matches for a user."""
    from backend.store import store
    from backend import services

    user_profile = store.get_profile(username)
    if not user_profile:
        raise HTTPException(status_code=404, detail=f"{username} hasn't materialized yet")

    user_obj = _build_user_obj(user_profile)

    candidates = []
    for p in store.list_profiles():
        if p["username"] != username:
            candidates.append(_build_user_obj(p))

    matches = services.find_top_matches(user_obj, candidates, n)
    return [
        {
            "match_user": m.user_b,
            "score": m.score,
            "reason": m.reason,
            "compatible": m.is_compatible,
        }
        for m in matches
    ]
