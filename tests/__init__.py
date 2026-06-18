"""
BDD feature tests — nothingcouldbebetter.
"""

import pytest

# --- Dread Category Tests ---

from backend.models import dread_category

def test_dread_category_mild():
    assert dread_category(1) == "mild"
    assert dread_category(3) == "mild"

def test_dread_category_moderate():
    assert dread_category(4) == "moderate"
    assert dread_category(6) == "moderate"

def test_dread_category_severe():
    assert dread_category(7) == "severe"
    assert dread_category(9) == "severe"

def test_dread_category_transcendent():
    assert dread_category(10) == "transcendent"

# --- Matching Score Tests ---

from backend.models import UserProfile
from backend.services import compute_match_score, find_matches, find_top_matches, generate_match_reason

def test_identical_profiles_match_perfectly():
    a = UserProfile(username="Alice", dread_level=7, favorite_nothing="The Void", bio="")
    b = UserProfile(username="Bob", dread_level=7, favorite_nothing="The Void", bio="")
    score = compute_match_score(a, b)
    assert score >= 0.6

def test_opposite_dread_levels_score_lower():
    a = UserProfile(username="Alice", dread_level=1, favorite_nothing="Silence", bio="")
    b = UserProfile(username="Bob", dread_level=10, favorite_nothing="Chaos", bio="")
    score = compute_match_score(a, b)
    assert score < 0.5

def test_find_matches_returns_compatible_pairs():
    a = UserProfile(username="Alice", dread_level=7, favorite_nothing="The Void", bio="")
    b = UserProfile(username="Bob", dread_level=8, favorite_nothing="The Void", bio="")
    matches = find_matches(a, [b])
    assert len(matches) == 1
    assert matches[0].user_b == "Bob"

def test_find_top_matches_limits_results():
    a = UserProfile(username="Alice", dread_level=5, favorite_nothing="Nothing", bio="")
    c = [
        UserProfile(username=f"User{i}", dread_level=5, favorite_nothing="Nothing", bio="")
        for i in range(5)
    ]
    top = find_top_matches(a, c, n=3)
    assert len(top) == 3

def test_match_reason_is_not_empty():
    a = UserProfile(username="A", dread_level=5, favorite_nothing="The Void", bio="")
    b = UserProfile(username="B", dread_level=5, favorite_nothing="The Void", bio="")
    score = compute_match_score(a, b)
    reason = generate_match_reason(a, b, score)
    assert reason
    assert "Because" in reason

def test_default_taglines_not_empty():
    from backend.models import get_default_taglines
    taglines = get_default_taglines()
    assert len(taglines) > 0
    assert all(t.text for t in taglines)
