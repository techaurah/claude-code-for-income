#!/usr/bin/env python3
"""Score product problems, require evidence, and apply a kill line.

Five criteria, each 1 to 5: pain severity, frequency, ability to
pay, distribution reach, and maintenance lightness (5 means a
light maintenance tail). Every score must carry a non-empty
evidence note or the problem is rejected. Any criterion scored
at 1 kills the idea, whatever the total says.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA = ("pain_severity", "frequency", "ability_to_pay", "distribution_reach", "maintenance_lightness")


def validate_problem(problem):
    scores = problem.get("scores", {})
    evidence = problem.get("evidence", {})
    for key in CRITERIA:
        value = scores.get(key)
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError(f"{problem.get('name', '?')}: {key} must be an int from 1 to 5")
        note = evidence.get(key)
        if not isinstance(note, str) or not note.strip():
            raise ValueError(f"{problem.get('name', '?')}: {key} needs an evidence note")


def score_problem(problem):
    validate_problem(problem)
    total = sum(problem["scores"][k] for k in CRITERIA)
    killed_by = [k for k in CRITERIA if problem["scores"][k] == 1]
    return {"name": problem["name"], "total": total, "killed": bool(killed_by), "killed_by": killed_by}


def rank_problems(problems):
    scored = [score_problem(p) for p in problems]
    alive = sorted([s for s in scored if not s["killed"]], key=lambda r: (-r["total"], r["name"]))
    dead = [s for s in scored if s["killed"]]
    return alive + dead


def load_problems(path=None):
    path = path or os.path.join(HERE, "problems.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)["problems"]


def main():
    for row in rank_problems(load_problems()):
        status = f"KILLED by {', '.join(row['killed_by'])}" if row["killed"] else "alive"
        print(f"{row['name']}: {row['total']}/25, {status}")


if __name__ == "__main__":
    main()
