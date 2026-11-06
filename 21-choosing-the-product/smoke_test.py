#!/usr/bin/env python3
"""Smoke test for Lesson 21."""
import problem_score as ps


def main():
    problems = ps.load_problems()
    ranked = ps.rank_problems(problems)
    assert ranked[0]["name"] == "No-show reminders and rebooking for clinics", ranked
    killed = [r for r in ranked if r["killed"]]
    assert len(killed) == 1 and killed[0]["name"] == "Fully autonomous tax filing for freelancers"
    assert "maintenance_lightness" in killed[0]["killed_by"]
    assert ranked[-1]["killed"] is True
    bad = {"name": "No evidence", "scores": {k: 3 for k in ps.CRITERIA}, "evidence": {k: "noted" for k in ps.CRITERIA}}
    bad["evidence"]["frequency"] = "  "
    try:
        ps.score_problem(bad)
    except ValueError as exc:
        assert "evidence" in str(exc)
    else:
        raise AssertionError("missing evidence must be rejected")
    print("lesson 21 smoke test passed")


if __name__ == "__main__":
    main()
