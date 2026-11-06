#!/usr/bin/env python3
"""Smoke test for Lesson 22."""
import ship_plan as sp


def main():
    features, capacity = sp.load_features()
    ordered = sp.sort_features(features)
    assert ordered[0]["name"] == "Core booking flow end to end", ordered
    assert all(f.get("slice") for f in ordered[:3])
    risks = [sp.RISK_ORDER[f["risk"]] for f in ordered[:3]]
    assert risks == sorted(risks, reverse=True)
    result = sp.build_plan(features, capacity)
    md = sp.render_markdown(result, capacity)
    assert "Week 1" in md and "Week 4" in md
    heavy = [{"name": "Big risky core", "size": 8, "risk": "high", "slice": True, "work": "human"}, {"name": "Extra A", "size": 8, "risk": "low", "slice": False, "work": "agent"}, {"name": "Extra B", "size": 8, "risk": "low", "slice": False, "work": "agent"}, {"name": "Extra C", "size": 8, "risk": "low", "slice": False, "work": "agent"}, {"name": "Extra D", "size": 8, "risk": "low", "slice": False, "work": "agent"}]
    over = sp.build_plan(heavy, weekly_capacity=10)
    assert over["overloads"], over
    assert over["overloads"][0]["cut_suggestion"] is not None
    assert "OVERLOAD" in sp.render_markdown(over, 10)
    print("lesson 22 smoke test passed")


if __name__ == "__main__":
    main()
