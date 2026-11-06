#!/usr/bin/env python3
"""Smoke test for Lesson 17."""
import offer_score as oscore


def main():
    offers = oscore.load_offers()
    assert len(offers) == 3
    ranked = oscore.rank_offers(offers)
    assert ranked[0]["name"] == "Enquiry response package for med spas", ranked
    assert ranked[-1]["name"] == "Generic AI chatbot for anyone", ranked
    assert "flagged" in ranked[-1]["verdict"]
    assert ranked[0]["total"] == 24
    assert ranked[-1]["total"] == 8
    try:
        oscore.score_offer({"name": "bad", "buyer_clarity": 9, "pain_urgency": 3, "scope_boundedness": 3, "delivery_repeatability": 3, "support_load": 3})
    except ValueError:
        pass
    else:
        raise AssertionError("out of range score must raise")
    print("lesson 17 smoke test passed")


if __name__ == "__main__":
    main()
