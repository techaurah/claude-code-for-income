#!/usr/bin/env python3
"""Smoke test for Lesson 18."""
import pipeline_sim as ps


def main():
    result = ps.simulate()
    for oid in ("ORD-1", "ORD-2", "ORD-3"):
        assert ps.stage_sequence(result["log"], oid) == list(ps.STAGES), oid
    assert result["orders"]["ORD-2"]["qa_attempts"] == 2
    assert result["orders"]["ORD-1"]["qa_attempts"] == 1
    fails = [e for e in result["log"] if e[1] == "qa_failed"]
    assert len(fails) == 1 and fails[0][0] == "ORD-2"
    base = sum(ps.HUMAN_MINUTES[s] for s in ps.STAGES)
    assert result["orders"]["ORD-1"]["human_minutes"] == base
    assert result["orders"]["ORD-2"]["human_minutes"] == base + ps.HUMAN_MINUTES["build"] + ps.HUMAN_MINUTES["qa"]
    assert result["total_human_minutes"] == sum(o["human_minutes"] for o in result["orders"].values())
    print("lesson 18 smoke test passed")


if __name__ == "__main__":
    main()
