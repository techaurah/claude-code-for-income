#!/usr/bin/env python3
"""Generate a four week ship plan from a feature list.

Ordering rule: slice features first, highest risk first inside
each group. That puts the riskiest part of the thin end to end
slice in week 1, where there is still time to react. Weeks have
a point capacity. A week over capacity is flagged, and the cut
suggestion names the lowest risk, non-slice feature in that week.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RISK_ORDER = {"high": 3, "medium": 2, "low": 1}


def sort_features(features):
    return sorted(features, key=lambda f: (0 if f.get("slice") else 1, -RISK_ORDER[f["risk"]], f["name"]))


def build_plan(features, weekly_capacity=10, weeks=4):
    ordered = sort_features(features)
    plan = [[] for _ in range(weeks)]
    loads = [0] * weeks
    for feat in ordered:
        placed = False
        for i in range(weeks):
            if loads[i] + feat["size"] <= weekly_capacity:
                plan[i].append(feat)
                loads[i] += feat["size"]
                placed = True
                break
        if not placed:
            idx = min(range(weeks), key=lambda i: loads[i])
            plan[idx].append(feat)
            loads[idx] += feat["size"]
    overloads = []
    for i, week in enumerate(plan):
        if loads[i] > weekly_capacity:
            candidates = [f for f in week if not f.get("slice")]
            cut = min(candidates, key=lambda f: (RISK_ORDER[f["risk"]], -f["size"])) if candidates else None
            overloads.append({"week": i + 1, "load": loads[i], "capacity": weekly_capacity, "cut_suggestion": cut["name"] if cut else None})
    return {"weeks": plan, "loads": loads, "overloads": overloads, "ordered": ordered}


def render_markdown(result, weekly_capacity=10):
    lines = ["# Four week ship plan", "", f"Weekly capacity: {weekly_capacity} points. Slice first, highest risk first.", ""]
    for i, week in enumerate(result["weeks"]):
        lines.append(f"## Week {i + 1} ({result['loads'][i]} points)")
        lines.append("")
        if i == 0:
            lines.append("Gate: the thin slice runs end to end, even if rough.")
        elif i == 1:
            lines.append("Gate: the riskiest remaining feature works against real data.")
        elif i == 2:
            lines.append("Gate: billing and edge cases pass, support path exists.")
        else:
            lines.append("Gate: ship checklist passes, rollback is rehearsed.")
        lines.append("")
        for feat in week:
            lines.append(f"- {feat['name']} ({feat['size']} pts, {feat['risk']} risk, {feat['work']} work)")
        lines.append("")
    for flag in result["overloads"]:
        lines.append(f"OVERLOAD: Week {flag['week']} carries {flag['load']} points against a capacity of {flag['capacity']}. Cut suggestion: {flag['cut_suggestion']}.")
        lines.append("")
    if not result["overloads"]:
        lines.append("No week is overloaded at this capacity.")
        lines.append("")
    lines.append("Human and agent split: human work is judgement, integration, and final review. Agent work is bounded implementation, tests, and drafts inside the frozen scope.")
    return "\n".join(lines)


def load_features(path=None):
    path = path or os.path.join(HERE, "features.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["features"], data.get("weekly_capacity_points", 10)


def main():
    features, capacity = load_features()
    print(render_markdown(build_plan(features, capacity), capacity))


if __name__ == "__main__":
    main()
