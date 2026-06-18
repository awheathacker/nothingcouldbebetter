"""
Profile routes — CRUD for nihilist profiles.
"""

from fastapi import APIRouter, HTTPException
from backend.models import UserProfile

router = APIRouter(prefix="/api/profiles")


@router.get("/")
def list_profiles() -> list[dict]:
    """Return all registered profiles."""
    from backend.store import store
    return store.list_profiles()


@router.get("/{username}")
def get_profile(username: str) -> dict:
    """Get a specific user profile."""
    from backend.store import store
    profile = store.get_profile(username)
    if profile:
        return profile
    raise HTTPException(status_code=404, detail=f"{username} has vanished into the void")


@router.post("/")
def create_profile(profile_data: dict) -> dict:
    """Create a new user profile."""
    from backend.store import store
    required = ["username", "dread_level", "favorite_nothing", "bio"]
    missing = [f for f in required if f not in profile_data]
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required fields: {', '.join(missing)}"
        )

    profile = UserProfile(
        username=profile_data["username"],
        dread_level=profile_data["dread_level"],
        favorite_nothing=profile_data["favorite_nothing"],
        bio=profile_data["bio"],
        quote=profile_data.get("quote", "We are all here on earth to do nothing."),
    )

    profile_dict = {
        "username": profile.username,
        "dread_level": profile.dread_level,
        "favorite_nothing": profile.favorite_nothing,
        "bio": profile.bio,
        "quote": profile.quote,
        "joined": profile.joined,
        "dread_category": profile.dread_category,
    }

    store.add_profile(profile_dict)
    return {"message": "You now exist (briefly)", "profile": profile_dict}


@router.delete("/{username}")
def delete_profile(username: str) -> dict:
    """Delete a user profile — back to nothing."""
    from backend.store import store
    removed = store.remove_profile(username)
    if removed:
        return {"message": f"{username} has returned to the void", "username": username}
    raise HTTPException(status_code=404, detail=f"{username} was already nothing")
