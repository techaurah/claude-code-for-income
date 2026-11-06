#!/usr/bin/env python3
"""Smoke test for Lesson 27: scoring, bands, and the all-no case."""
import copy
import json
import os

import readiness_check as rc

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "readiness_example.json"),
              encoding="utf-8") as f:
        data = {k: v for k, v in json.load(f).items()
                if not k.startswith("_")}
    results = rc.score_readiness(data)
    assert results["IP and ownership"]["percent"] == 88
    assert results["IP and ownership"]["band"] == "ready"
    assert results["Data handling"]["percent"] == 50
    assert results["Data handling"]["band"] == "gaps to close"
    assert "retention_period_stated" in results["Data handling"]["gaps"]
    all_no = {area: {q: "no" for q in answers}
              for area, answers in data.items()}
    flat = rc.score_readiness(all_no)
    for label, result in flat.items():
        assert result["percent"] == 0, label
        assert result["band"] == "not ready", label
        assert result["gaps"], label
    all_yes = copy.deepcopy(data)
    for answers in all_yes.values():
        for q in answers:
            answers[q] = "yes"
    assert all(r["band"] == "ready"
               for r in rc.score_readiness(all_yes).values())
    print("lesson 27 smoke test passed")


if __name__ == "__main__":
    main()
