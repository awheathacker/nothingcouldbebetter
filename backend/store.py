"""
In-memory data store for nothingcouldbebetter.

Central store to avoid circular imports between route modules.
"""

from datetime import datetime
import uuid


class InMemoryStore:
    """Simple in-memory store for profiles and forum posts."""

    def __init__(self):
        self.profiles: list[dict] = []
        self.posts: list[dict] = []

    def get_profile(self, username: str) -> dict | None:
        for p in self.profiles:
            if p["username"] == username:
                return p
        return None

    def add_profile(self, profile: dict) -> None:
        self.profiles.append(profile)

    def remove_profile(self, username: str) -> bool:
        before = len(self.profiles)
        self.profiles = [p for p in self.profiles if p["username"] != username]
        return len(self.profiles) < before

    def list_profiles(self) -> list[dict]:
        return list(self.profiles)

    def add_post(self, post: dict) -> None:
        self.posts.append(post)

    def get_post(self, post_id: str) -> dict | None:
        for p in self.posts:
            if p["id"] == post_id:
                return p
        return None

    def delete_post(self, post_id: str) -> bool:
        before = len(self.posts)
        self.posts = [p for p in self.posts if p["id"] != post_id]
        return len(self.posts) < before

    def list_posts(self, sort_by: str = "date") -> list[dict]:
        if sort_by == "date":
            return sorted(self.posts, key=lambda p: p["created_at"], reverse=True)
        return list(self.posts)

    def react_to_post(self, post_id: str, reaction: str) -> int | None:
        for p in self.posts:
            if p["id"] == post_id:
                if "reactions" not in p:
                    p["reactions"] = {}
                p["reactions"][reaction] = p["reactions"].get(reaction, 0) + 1
                return p["reactions"][reaction]
        return None


# Singleton store instance
store = InMemoryStore()
