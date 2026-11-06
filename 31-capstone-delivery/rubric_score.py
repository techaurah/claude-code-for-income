#!/usr/bin/env python3
"""Score a capstone delivery pack against the Lesson 31 rubric.

Takes a JSON object mapping each rubric criterion to a score
from 0 to 3, applies the rubric weights, and returns a weighted
percentage with a verdict band: ship it, fix and reship, or redo.
Scores outside 0 to 3 are refused, because a rubric you can
overflow is a mood, not a measure.

Standard library only, offline, no credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

WEIGHTS = {
    "scope_fidelity": 0.20,
    "price_integrity": 0.15,
    "qa_evidence": 0.20,
    "handover_completeness": 0.15,
    "honesty_of_numbers": 0.20,
    "support_readiness": 0.10,
}


def verdict(percent):
    if percent >= 85:
        return "ship it"
    if percent >= 60:
        return "fix and reship"
    return "redo"


def score_grades(grades):
    """Return (weighted percent, verdict). Refuse out of range scores."""
    missing = [key for key in WEIGHTS if key not in grades]
    if missing:
        raise ValueError(f"missing criteria: {missing}")
    weighted = 0.0
    for key, weight in WEIGHTS.items():
        value = grades[key]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError(f"{key} must be a number from 0 to 3")
        if value < 0 or value > 3:
            raise ValueError(f"{key} score {value} is outside 0 to 3")
        weighted += (value / 3.0) * weight
    percent = round(weighted * 100, 1)
    return percent, verdict(percent)


def main(argv):
    if argv:
        with open(argv[0], encoding="utf-8") as f:
            grades = json.load(f)
    else:
        grades = {key: 3 for key in WEIGHTS}
        print("No grades file given, showing a perfect-score example:")
    percent, band = score_grades(grades)
    for key in WEIGHTS:
        print(f"  {key}: {grades[key]} of 3 (weight {WEIGHTS[key]})")
    print(f"Weighted total: {percent}%")
    print(f"Verdict: {band}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
