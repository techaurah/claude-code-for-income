#!/usr/bin/env python3
"""Replay the capstone engagement and apply its QA gate.

Walks the five build stages deterministically, reads the QA
record in this folder, and refuses to mark delivery ready while
any gate check effectively fails. A check whose failure carries
a recorded fix and a passing retest counts as passed. The final
cost ledger is read from Lesson 29's engagement.json, never
restated here, so the two lessons cannot quietly disagree.

Standard library only, offline, no credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGAGEMENT_PATH = os.path.join(
    HERE, "..", "29-capstone-spec", "capstone", "engagement.json")
QA_PATH = os.path.join(HERE, "qa_record.json")

STAGES = [
    "Stage 1: workstation setup for the engagement",
    "Stage 2: build across Instagram, WhatsApp, and the website",
    "Stage 3: hardening against the discovery edge cases",
    "Stage 4: QA gate",
    "Stage 5: handover preparation",
]


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def effective_result(check):
    """A fixed failure with a passing retest counts as passed."""
    if check.get("result") == "fail" and check.get("retest") == "pass":
        return "pass (after fix and retest)"
    return check.get("result", "missing")


def failing_checks(record):
    return [check for check in record.get("checks", [])
            if effective_result(check) != "pass"
            and not effective_result(check).startswith("pass")]


def gate_status(record):
    failing = failing_checks(record)
    return (not failing, failing)


def cost_ledger(engagement):
    floor = engagement["cost_floor"]
    return [
        f"Fixed price: ${engagement['fixed_price_usd']}",
        f"Human time: {floor['human_hours']} hours at "
        f"${floor['target_rate_usd_per_hour']}/h = "
        f"${floor['human_hours'] * floor['target_rate_usd_per_hour']}",
        f"Plan share: ${floor['plan_share_usd']}",
        f"Measured API: ${floor['measured_api_usd']}",
        f"Cost floor total: ${floor['total_usd']}",
        f"Gross margin before any platform fee: "
        f"${engagement['gross_margin_usd']}",
    ]


def replay(record, engagement):
    lines = []
    for stage in STAGES:
        lines.append(stage)
    lines.append("")
    ready, failing = gate_status(record)
    total = len(record.get("checks", []))
    passed = total - len(failing_checks(record))
    lines.append(f"QA gate: {passed} of {total} checks effectively passing")
    for check in record.get("checks", []):
        lines.append(f"  {check['id']} {check['name']}: "
                     f"{effective_result(check)}")
    lines.append("")
    if ready:
        lines.append("Delivery state: READY")
    else:
        lines.append("Delivery state: REFUSED, gate checks still failing:")
        for check in failing:
            lines.append(f"  {check['id']} {check['name']}")
    lines.append("")
    lines.append("Final cost ledger (read from Lesson 29 engagement.json):")
    lines.extend(cost_ledger(engagement))
    return "\n".join(lines)


def main(argv):
    qa_path = argv[0] if argv else QA_PATH
    record = load_json(qa_path)
    engagement = load_json(ENGAGEMENT_PATH)
    print(replay(record, engagement))
    ready, _failing = gate_status(record)
    return 0 if ready else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
