"""
Matching service — compatibility through shared nothingness.

Pure functional approach: inputs are UserProfile objects, outputs are scores/matches.
"""

from backend.models import UserProfile, Match


def compute_match_score(profile_a: UserProfile, profile_b: UserProfile) -> float:
    """Compute compatibility score (0.0 to 1.0).

    Scoring breakdown:
    - Dread level proximity: up to 0.4
    - Favorite nothing match: up to 0.3
    - Quote/philosopher overlap: up to 0.3
    """
    score = 0.0

    # Dread level proximity (closer = more compatible)
    dread_diff = abs(profile_a.dread_level - profile_b.dread_level)
    score += 0.4 * max(0.0, 1.0 - (dread_diff / 10.0))

    # Shared favorite nothing
    if profile_a.favorite_nothing.lower() == profile_b.favorite_nothing.lower():
        score += 0.3
    elif profile_a.favorite_nothing and profile_b.favorite_nothing:
        shared = set(profile_a.favorite_nothing.lower().split()) & \
                 set(profile_b.favorite_nothing.lower().split())
        score += 0.15 if shared else 0.0

    # Quote similarity — shared philosopher reference
    philosophers = {"sartre", "nietzsche", "camus", "wilde", "cioran", "feynman", "shakespeare"}
    authors_a = set(w.lower() for w in profile_a.quote.split()) & philosophers
    authors_b = set(w.lower() for w in profile_b.quote.split()) & philosophers
    if authors_a & authors_b:
        score += 0.25
    else:
        # Fallback: general word overlap
        words_a = set(profile_a.quote.lower().split())
        words_b = set(profile_b.quote.lower().split())
        if words_a and words_b:
            overlap = len(words_a & words_b) / max(len(words_a | words_b), 1)
            score += 0.15 * overlap

    return min(1.0, max(0.0, score))


def generate_match_reason(profile_a: UserProfile, profile_b: UserProfile, score: float) -> str:
    """Generate a human-readable match reason."""
    reasons = []

    if abs(profile_a.dread_level - profile_b.dread_level) <= 2:
        reasons.append("You share a similar level of existential dread")

    if profile_a.favorite_nothing.lower() == profile_b.favorite_nothing.lower():
        reasons.append(f"You both cherish the same nothing: {profile_a.favorite_nothing}")

    if score > 0.8:
        reasons.append("The universe has aligned your nothingness")
    elif score > 0.6:
        reasons.append("Your voids complement each other")
    else:
        reasons.append("At least you both agree that none of this matters")

    return " Because " + reasons[0].lower() if reasons else " Because the void connects you"


def find_matches(user: UserProfile, candidates: list) -> list[Match]:
    """Find all matches for a user from a candidate pool."""
    matches = []
    for candidate in candidates:
        if candidate.username == user.username:
            continue
        score = compute_match_score(user, candidate)
        reason = generate_match_reason(user, candidate, score)
        matches.append(Match(
            user_a=user.username,
            user_b=candidate.username,
            score=score,
            reason=reason,
        ))
    matches.sort(key=lambda m: m.score, reverse=True)
    return matches


def find_top_matches(user: UserProfile, candidates: list, n: int = 3) -> list[Match]:
    """Find the top N compatible matches for a user."""
    return find_matches(user, candidates)[:n]
