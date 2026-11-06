#!/usr/bin/env python3
"""Score candidate productized offers and rank them.

Each offer is scored 1 to 5 on buyer clarity, pain urgency, scope
boundedness, and delivery repeatability. Support load is also 1 to
5, but it is inverted: a load of 5 contributes 1 point, because
heavy support eats the margin a productized offer exists to protect.
Total is out of 25. No network, no credentials.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA = ("buyer_clarity", "pain_urgency", "scope_boundedness", "delivery_repeatability")


def score_offer(offer):
    for key in CRITERIA + ("support_load",):
        value = offer.get(key)
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError(f"{offer.get('name', '?')}: {key} must be an int from 1 to 5")
    inverted_support = 6 - offer["support_load"]
    total = sum(offer[k] for k in CRITERIA) + inverted_support
    return total


def verdict(total, offer):
    if offer["buyer_clarity"] <= 1 or offer["scope_boundedness"] <= 1:
        return "flagged: buyer or scope is too vague to productize yet"
    if total >= 20:
        return "productize: strong candidate, build the pipeline next"
    if total >= 15:
        return "refine: tighten scope or buyer before productizing"
    return "do not productize: keep as bespoke work or drop it"


def rank_offers(offers):
    scored = []
    for offer in offers:
        total = score_offer(offer)
        scored.append({"name": offer["name"], "total": total, "verdict": verdict(total, offer), "offer": offer})
    return sorted(scored, key=lambda row: (-row["total"], row["name"]))


def load_offers(path=None):
    path = path or os.path.join(HERE, "offers.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["offers"]


def main():
    ranked = rank_offers(load_offers())
    print("Ranked candidate offers (total out of 25, support load inverted):")
    for i, row in enumerate(ranked, 1):
        print(f"  {i}. {row['name']}: {row['total']}/25. {row['verdict']}")
    print()
    print("Reading the ranking: the top offer names one buyer, one pain,")
    print("and one bounded outcome. The bottom offer names none of them.")


if __name__ == "__main__":
    main()
