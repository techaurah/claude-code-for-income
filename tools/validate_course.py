#!/usr/bin/env python3
"""Validate this course's structure, JSON data, and capstone math.

Checks:
- Every .json file in the repository parses.
- Every lesson folder 00 to 31 exists and is a complete unit:
  README.md, exercise.md, and solution/SOLUTION.md.
- The capstone engagement file (29-capstone-spec/capstone/
  engagement.json) is internally consistent: the fixed price
  equals its printed build-up, the cost floor equals its printed
  parts, and the margin is the difference. A capstone that cannot
  add up cannot teach pricing.
- The platform numbers file (01-the-honest-economics/
  platform_numbers.json) carries a source and a limits note for
  every figure, because unsourced numbers are this course's
  definition of a bug.
Exits nonzero on any failure, so CI can gate on it.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LESSONS = [
    "00-course-setup", "01-the-honest-economics", "02-claude-md-systems",
    "03-skills-as-capital", "04-subagents-and-delegation",
    "05-hooks-guardrails", "06-mcp-force-multipliers",
    "07-headless-and-agent-sdk", "08-ci-and-scheduled-automation",
    "09-worktrees-and-background", "10-the-cost-stack",
    "11-token-economics", "12-positioning-and-offers",
    "13-scoping-and-estimation", "14-pricing", "15-delivery-qa",
    "16-handover-and-rehire", "17-choosing-a-productized-offer",
    "18-building-the-pipeline", "19-packaging-and-pricing-page",
    "20-fulfilment-at-volume", "21-choosing-the-product",
    "22-build-and-ship", "23-maintenance-economics",
    "24-launch-and-churn", "25-the-audit", "26-retainers",
    "27-selling-to-teams", "28-failure-modes-and-ethics",
    "29-capstone-spec", "30-capstone-build", "31-capstone-delivery",
]


def iter_json():
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath or "__pycache__" in dirpath:
            continue
        for name in sorted(files):
            if name.endswith(".json"):
                yield os.path.join(dirpath, name)


def main():
    errors = []
    data = {}
    total = 0
    for path in iter_json():
        total += 1
        rel = os.path.relpath(path, ROOT)
        try:
            with open(path, encoding="utf-8") as f:
                data[rel] = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"FAIL {rel}: does not parse: {exc}")
    print(f"{total} JSON file(s) checked")

    for folder in LESSONS:
        for needed in ("README.md", "exercise.md",
                       os.path.join("solution", "SOLUTION.md")):
            if not os.path.isfile(os.path.join(ROOT, folder, needed)):
                errors.append(f"INCOMPLETE {folder}: missing {needed}")
    print(f"{len(LESSONS)} lesson folder(s) checked")

    eng = data.get(os.path.join(
        "29-capstone-spec", "capstone", "engagement.json"))
    if eng is None:
        errors.append("capstone engagement.json missing or unparsed")
    else:
        parts = eng["price_build_up"]
        built = sum(parts.values())
        if built != eng["fixed_price_usd"]:
            errors.append(
                f"capstone price build-up sums to {built}, "
                f"not the fixed price {eng['fixed_price_usd']}")
        costs = eng["cost_floor"]
        floor = costs["human_hours"] * costs["target_rate_usd_per_hour"] \
            + costs["plan_share_usd"] + costs["measured_api_usd"]
        if floor != costs["total_usd"]:
            errors.append(
                f"capstone cost floor parts give {floor}, "
                f"file claims {costs['total_usd']}")
        if eng["fixed_price_usd"] - costs["total_usd"] != eng["gross_margin_usd"]:
            errors.append("capstone gross margin is not price minus floor")

    nums = data.get(os.path.join(
        "01-the-honest-economics", "platform_numbers.json"))
    if nums is None:
        errors.append("platform_numbers.json missing or unparsed")
    else:
        for key, entry in nums.items():
            if key.startswith("_"):
                continue
            for field in ("figure", "source", "limits"):
                if field not in entry:
                    errors.append(
                        f"platform number {key} missing {field}")

    for e in errors:
        print(e)
    print(f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
