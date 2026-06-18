"""
Tests for nothingcouldbebetter — functional and BDD-style tests.

Uses pytest (functional test-first approach per TDD).
"""

import sys
import os

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.models import dread_category, get_default_taglines, UserProfile
from backend.services import compute_match_score, generate_match_reason, find_matches, find_top_matches


class TestDreadCategory:
    """Test dread level categorization."""

    def test_mild(self):
        assert dread_category(1) == "mild"
        assert dread_category(3) == "mild"

    def test_moderate(self):
        assert dread_category(4) == "moderate"
        assert dread_category(6) == "moderate"

    def test_severe(self):
        assert dread_category(7) == "severe"
        assert dread_category(9) == "severe"

    def test_transcendent(self):
        assert dread_category(10) == "transcendent"

    def test_boundary_low(self):
        assert dread_category(0) == "mild"

    def test_boundary_high(self):
        assert dread_category(10) == "transcendent"


class TestMatching:
    """Test matching algorithm."""

    def _user(self, name, dread=5, nothing="The Void"):
        return UserProfile(username=name, dread_level=dread, favorite_nothing=nothing, bio="")

    def test_identical_profiles_match_well(self):
        a = self._user("Alice", 7, "The Void")
        b = self._user("Bob", 7, "The Void")
        score = compute_match_score(a, b)
        assert score >= 0.6

    def test_opposite_dread_scores_lower(self):
        a = self._user("Alice", 1, "Silence")
        b = self._user("Bob", 10, "Chaos")
        score = compute_match_score(a, b)
        assert score < 0.5

    def test_same_nothing_boosts_score(self):
        a = self._user("Alice", 5, "The Void")
        b = self._user("Bob", 5, "The Void")
        score_same = compute_match_score(a, b)

        c = self._user("Charlie", 5, "Silence")
        score_diff = compute_match_score(a, c)
        assert score_same > score_diff

    def test_find_matches_returns_matches(self):
        a = self._user("Alice", 7, "The Void")
        b = self._user("Bob", 8, "The Void")
        matches = find_matches(a, [b])
        assert len(matches) == 1
        assert matches[0].user_b == "Bob"

    def test_find_top_matches_limits_results(self):
        a = self._user("Alice", 5)
        c = [self._user("User" + str(i), 5) for i in range(5)]
        top = find_top_matches(a, c, n=3)
        assert len(top) == 3

    def test_generate_match_reason_is_not_empty(self):
        a = self._user("A", 5, "The Void")
        b = self._user("B", 5, "The Void")
        score = compute_match_score(a, b)
        reason = generate_match_reason(a, b, score)
        assert reason
        assert "Because" in reason

    def test_score_is_bounded_0_to_1(self):
        a = self._user("Alice", 5)
        b = self._user("Bob", 8)
        score = compute_match_score(a, b)
        assert 0.0 <= score <= 1.0


class TestTaglines:
    """Test default taglines."""

    def test_taglines_not_empty(self):
        taglines = get_default_taglines()
        assert len(taglines) > 0

    def test_taglines_have_text(self):
        taglines = get_default_taglines()
        assert all(t.text for t in taglines)
