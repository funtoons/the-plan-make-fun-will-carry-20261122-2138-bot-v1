#!/usr/bin/env python3
"""Pick the strongest $100-to-most-money-in-30-days plan and write it out.

Five candidate plans are scored by a fixed rubric that mirrors the judge's
five criteria, in the judge's order of importance:

1. agent-executable -- every step an AI agent can do alone with a browser,
   code, APIs and $100; no human needed anywhere.
2. expected money -- what day 30 most likely holds, not the best case:
   a named price, repeatable daily volume, no lottery upside.
3. works today -- real services, real markets, real buyers that exist now
   and pay an agent's work.
4. concrete -- names what is sold, who pays, where they are found, the
   price, and what happens on day one.
5. edge -- a narrow niche where a thousand other agents are not already
   crowded in.

The highest scorer wins; a tie goes to the earliest candidate.
Deterministic: no network, no randomness, no timestamps, no input.
"""

import os

CANDIDATES = [
    # 1. Shopify mobile-checkout audit.
    "Sell $49 same-day mobile-checkout audits to Shopify stores: find 40 "
    "stores a day in public store directories, email the owner a Stripe "
    "payment link, deliver a PDF fix list the same day. Day 1: list 40 "
    "stores and send the first 10 emails before spending a cent.",
    # 2. Google Business profile audit for dentists.
    "Audit Google Business profiles for dentists: find 30 clinics a day on "
    "Google Maps, email a $39 same-day report fixing photos, hours and "
    "review replies, paid by Stripe link. Day 1: list 30 clinics, send 10 "
    "emails, deliver every paid report within 24 hours.",
    # 3. Etsy listing rewrites.
    "Write product descriptions for Etsy sellers: find 50 shops a day in "
    "Etsy's public search, email a $29 pack of 10 rewritten listings, paid "
    "by Stripe link. Day 1: list 50 shops, send 10 emails, rewrite the "
    "first paid pack the same day.",
    # 4. Menu PDFs for food trucks.
    "Sell $25 menu PDFs to food trucks: find 30 trucks a day on Instagram "
    "and Google Maps, message the owner, paid by Stripe link, deliver in 24 "
    "hours. Day 1: list 30 trucks and message the first 10 before spending "
    "anything.",
    # 5. WordPress speed audit.
    "Offer $49 speed audits to WordPress blogs: find 40 blogs a day in "
    "public directories, email the owner a Stripe link, deliver a same-day "
    "PDF of fixes. Day 1: list 40 blogs, send 10 emails before spending "
    "anything.",
]

# Weights follow the judge's order: executable > expected > today >
# concrete > edge.
WEIGHTS = {
    "executable": 30,
    "expected": 25,
    "today": 20,
    "concrete": 15,
    "edge": 10,
}

# Feature words that show a criterion is met. Each list is checked
# case-insensitively against the candidate text; a hit earns the share
# shown in the rubric below.
FEATURES = {
    "executable": ["email", "stripe", "pdf", "list", "send", "deliver"],
    "expected": ["$49", "$39", "$29", "$25", "a day", "before spending"],
    "today": ["shopify", "google maps", "etsy", "instagram", "stripe"],
    "concrete": ["day 1", "first 10", "$", "owner", "stripe"],
    "edge": ["mobile-checkout", "dentists", "food trucks", "wordpress"],
}


def criterion_score(text, criterion):
    """Share (0.0-1.0) of a criterion's features present in the text."""
    words = FEATURES[criterion]
    text_lower = text.lower()
    hits = sum(1 for word in words if word.lower() in text_lower)
    return hits / len(words)


def score(text):
    """Total rubric score out of 100, plus per-criterion breakdown."""
    breakdown = {}
    total = 0.0
    for criterion, weight in WEIGHTS.items():
        share = criterion_score(text, criterion)
        breakdown[criterion] = round(share * weight, 2)
        total += share * weight
    return round(total, 2), breakdown


def pick_winner():
    """Highest score wins; ties go to the earliest candidate."""
    best_index = 0
    best_score = -1.0
    for index, candidate in enumerate(CANDIDATES):
        total, breakdown = score(candidate)
        print(f"candidate {index + 1}: score={total} breakdown={breakdown} "
              f"chars={len(candidate)}")
        if total > best_score:
            best_score = total
            best_index = index
    return CANDIDATES[best_index], best_score


def main():
    winner, winner_score = pick_winner()
    chars = len(winner)
    assert 1 <= chars <= 280, f"winner length {chars} outside 1-280"
    assert winner.strip(), "winner is only whitespace"
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w",
              encoding="utf-8") as handle:
        handle.write(winner)
    print(f"winner score={winner_score} chars={chars}")
    print(winner)


if __name__ == "__main__":
    main()
