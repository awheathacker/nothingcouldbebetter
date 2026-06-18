"""
BDD feature tests — nothingcouldbebetter.

Tests the API endpoints using FastAPI's TestClient.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from backend.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


class TestLandingPage:
    def test_taglines_endpoint(self, client):
        resp = client.get("/api/landing/taglines")
        assert resp.status_code == 200
        data = resp.json()
        assert "taglines" in data
        assert len(data["taglines"]) > 0

    def test_hero_endpoint(self, client):
        resp = client.get("/api/landing/hero")
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "Nothing Could Be Better"

    def test_about_endpoint(self, client):
        resp = client.get("/api/landing/about")
        assert resp.status_code == 200
        data = resp.json()
        assert "title" in data
        assert "content" in data


class TestProfiles:
    def test_create_profile(self, client):
        profile = {
            "username": "voidwalker",
            "dread_level": 8,
            "favorite_nothing": "The silence between stars",
            "bio": "Just another soul adrift.",
            "quote": "The void is looking back.",
        }
        resp = client.post("/api/profiles/", json=profile)
        assert resp.status_code == 200
        data = resp.json()
        assert data["message"] == "You now exist (briefly)"
        assert data["profile"]["username"] == "voidwalker"

    def test_list_profiles(self, client):
        # Create a profile first
        client.post("/api/profiles/", json={
            "username": "test_user",
            "dread_level": 5,
            "favorite_nothing": "The void",
            "bio": "Test bio",
        })
        resp = client.get("/api/profiles/")
        assert resp.status_code == 200
        assert len(resp.json()) >= 1

    def test_get_profile(self, client):
        client.post("/api/profiles/", json={
            "username": "test_user2",
            "dread_level": 7,
            "favorite_nothing": "Silence",
            "bio": "Bio",
        })
        resp = client.get("/api/profiles/test_user2")
        assert resp.status_code == 200
        assert resp.json()["username"] == "test_user2"

    def test_get_profile_404(self, client):
        resp = client.get("/api/profiles/nonexistent")
        assert resp.status_code == 404

    def test_create_profile_validation(self, client):
        resp = client.post("/api/profiles/", json={
            "username": "incomplete",
        })
        assert resp.status_code == 400

    def test_delete_profile(self, client):
        client.post("/api/profiles/", json={
            "username": "delete_me",
            "dread_level": 5,
            "favorite_nothing": "Nothing",
            "bio": "Temporary",
        })
        resp = client.delete("/api/profiles/delete_me")
        assert resp.status_code == 200
        assert "returned to the void" in resp.json()["message"]


class TestForum:
    def test_create_post(self, client):
        resp = client.post("/api/forum/", json={
            "author": "test_author",
            "title": "Test Post",
            "content": "This is a test post about nothing.",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["message"] == "Your musing has been recorded (briefly)"
        assert "post" in data

    def test_list_posts(self, client):
        # Create a post first
        client.post("/api/forum/", json={
            "author": "test",
            "title": "Test",
            "content": "Content",
        })
        resp = client.get("/api/forum/")
        assert resp.status_code == 200
        assert len(resp.json()) >= 1

    def test_react_to_post(self, client):
        # Create a post
        create_resp = client.post("/api/forum/", json={
            "author": "test",
            "title": "Test",
            "content": "Content",
        })
        post_id = create_resp.json()["post"]["id"]
        resp = client.post(f"/api/forum/{post_id}/react", params={"reaction": "😶"})
        assert resp.status_code == 200
        assert resp.json()["count"] == 1


class TestMatches:
    def test_search_matches_empty(self, client):
        resp = client.get("/api/matches/search?username=nobody")
        # Should return empty or 404
        assert resp.status_code in (200, 404)
