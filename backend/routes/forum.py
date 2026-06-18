"""
Nothing Could Be Better — Forum Routes

Forum/message board routes — existential musings on the void board.
"""

from datetime import datetime
from fastapi import APIRouter, HTTPException
import uuid

router = APIRouter(prefix="/api/forum")


@router.get("/")
def list_posts() -> list[dict]:
    """Return all forum posts sorted by date."""
    from backend.store import store
    return store.list_posts()


@router.get("/{post_id}")
def get_post(post_id: str) -> dict:
    """Get a specific forum post."""
    from backend.store import store
    post = store.get_post(post_id)
    if post:
        return post
    raise HTTPException(status_code=404, detail=f"Post {post_id} has faded into nothingness")


@router.post("/")
def create_post(post_data: dict) -> dict:
    """Create a new forum post."""
    required = ["author", "title", "content"]
    missing = [f for f in required if f not in post_data]
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required fields: {', '.join(missing)}"
        )

    post = {
        "id": str(uuid.uuid4())[:8],
        "author": post_data["author"],
        "title": post_data["title"],
        "content": post_data["content"],
        "tags": post_data.get("tags", ["existentialism"]),
        "created_at": datetime.now().isoformat(),
        "reactions": {},
    }
    store.add_post(post)
    return {"message": "Your musing has been recorded (briefly)", "post": post}


@router.post("/{post_id}/react")
def react_to_post(post_id: str, reaction: str = "😶") -> dict:
    """React to a forum post with an emotion."""
    from backend.store import store
    count = store.react_to_post(post_id, reaction)
    if count is not None:
        return {"post_id": post_id, "reaction": reaction, "count": count}
    raise HTTPException(status_code=404, detail=f"Post {post_id} has faded")


@router.delete("/{post_id}")
def delete_post(post_id: str) -> dict:
    """Delete a post — it dissolves back into the void."""
    from backend.store import store
    removed = store.delete_post(post_id)
    if removed:
        return {"message": f"Post {post_id} has dissolved into the void"}
    raise HTTPException(status_code=404, detail=f"Post {post_id} was already nothing")
