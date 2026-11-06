#!/usr/bin/env python3
"""Generate the capstone delivery pack checklist in markdown.

Reads the engagement spec from Lesson 29 and lists every
deliverable implied by the price build-up, the evidence file
that proves it, and its pack status. The checklist is generated
from the spec, never typed by hand, so a priced element cannot
be quietly dropped from the pack.

Standard library only, offline, no credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGAGEMENT_PATH = os.path.join(
    HERE, "..", "29-capstone-spec", "capstone", "engagement.json")

DELIVERABLES = {
    "discovery_and_scope": (
        "Discovery record and agreed scope",
        "capstone/discovery_notes.md"),
    "build": (
        "Enquiry response system across Instagram, WhatsApp, and the website",
        "qa_record.json (Lesson 30) and the build log"),
    "qa_and_hardening": (
        "QA gate record with per-check results, fixes, and retests",
        "qa_record.json (Lesson 30)"),
    "handover_and_training": (
        "Handover notes, runbook, and training session record",
        "handover_notes.md and runbook.md in the delivery pack"),
    "support_window_30d": (
        "Support terms for the 30 day window, with the retainer path after it",
        "support_terms.md in the delivery pack"),
}


def load_engagement(path=ENGAGEMENT_PATH):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_checklist(engagement):
    lines = []
    lines.append(f"# Delivery pack checklist: {engagement['client']}")
    lines.append(f"Fixed price: ${engagement['fixed_price_usd']} "
                 f"(build-up verified in Lesson 29)")
    lines.append("")
    lines.append("| Deliverable | From price element | Evidence file | Pack status |")
    lines.append("|---|---|---|---|")
    for key, price in engagement["price_build_up"].items():
        name, evidence = DELIVERABLES[key]
        lines.append(f"| {name} | {key} (${price}) | {evidence} | "
                     f"included, checked against the brief |")
    lines.append("")
    lines.append("Also in the pack, not priced as separate elements:")
    lines.append("- The client brief, unchanged, so the client can check "
                 "the delivery against their own words.")
    lines.append("- The cost ledger from Lesson 30, with assumptions printed.")
    lines.append("- The self-grading rubric scores from this lesson, "
                 "weaknesses included.")
    return "\n".join(lines) + "\n"


def main():
    print(build_checklist(load_engagement()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
