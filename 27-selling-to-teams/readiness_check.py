#!/usr/bin/env python3
"""Score team-sale readiness across four areas from yes/no answers.

Reads a JSON file where each of the four areas maps question keys
to "yes", "partial", or "no". Reports a per-area percentage, a
readiness band, and the named gaps (anything not answered yes).

Standard library only, offline, no credentials. This tool is
orientation for preparing a sale, not legal advice.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

POINTS = {"yes": 1.0, "partial": 0.5, "no": 0.0}

AREAS = {
    "ip_and_ownership": "IP and ownership",
    "data_handling": "Data handling",
    "security_practice": "Security practice",
    "contract_readiness": "Contract readiness",
}


def band(percent):
    if percent >= 80:
        return "ready"
    if percent >= 50:
        return "gaps to close"
    return "not ready"


def score_area(answers):
    if not answers:
        raise ValueError("an area needs at least one answer")
    total = 0.0
    gaps = []
    for question, answer in answers.items():
        if answer not in POINTS:
            raise ValueError(f"answer for {question!r} must be one of "
                             f"{sorted(POINTS)}, got {answer!r}")
        total += POINTS[answer]
        if answer != "yes":
            gaps.append(question)
    percent = round(100 * total / len(answers))
    return {"percent": percent, "band": band(percent), "gaps": gaps}


def score_readiness(data):
    results = {}
    for area, label in AREAS.items():
        if area not in data:
            raise ValueError(f"missing area: {area}")
        results[label] = score_area(data[area])
    return results


def build_report(data):
    results = score_readiness(data)
    lines = []
    for label, result in results.items():
        lines.append(f"{label}: {result['percent']}% ({result['band']})")
        for gap in result["gaps"]:
            lines.append(f"  gap to close: {gap}")
    ready = all(r["band"] == "ready" for r in results.values())
    lines.append("")
    lines.append("Overall: ready for a team sale" if ready
                 else "Overall: close the named gaps before a team sale")
    return "\n".join(lines)


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "readiness_example.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    print(build_report(data))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
