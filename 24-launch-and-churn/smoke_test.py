#!/usr/bin/env python3
"""Smoke test for Lesson 24."""
import churn_math as cm


def main():
    sc = cm.load_scenario()
    result = cm.simulate(sc["starting_subscribers"], sc["monthly_adds"], sc["churn_percent"] / 100.0, sc["price_usd_per_month"], sc["months"])
    assert len(result["rows"]) == 12
    assert abs(result["lifetime_months"] - 12.5) < 1e-9
    assert abs(result["ltv_gross"] - 187.5) < 1e-9
    # Month 12 figure for the shipped fixture, recomputed by hand loop.
    subs = 40.0
    for _ in range(12):
        subs = subs - subs * 0.08 + 12
    assert abs(result["final_subscribers"] - round(subs, 2)) < 0.01
    assert abs(result["final_mrr"] - round(subs * 15, 2)) < 0.01
    assert abs(result["final_mrr"] - 1643.35) < 1.0, result["final_mrr"]
    print("lesson 24 smoke test passed")


if __name__ == "__main__":
    main()
