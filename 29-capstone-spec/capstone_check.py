#!/usr/bin/env python3
"""Validate the capstone spec pack for the Lumen Med Spa engagement.

Checks that the brief, the discovery notes, and engagement.json
exist, that the price build-up sums to the fixed price, that the
cost floor parts sum to the stated total, that the margin is the
difference, and that every price element has a matching scope
line in the client brief.

Standard library only, offline, no credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CAPSTONE = os.path.join(HERE, "capstone")

SCOPE_PHRASES = {
    "discovery_and_scope": "Discovery and scope",
    "build": "Build",
    "qa_and_hardening": "QA and hardening",
    "handover_and_training": "Handover and training",
    "support_window_30d": "Support window",
}


def load_engagement(path=None):
    path = path or os.path.join(CAPSTONE, "engagement.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def run_checks():
    """Return a list of (name, passed, detail) for every check."""
    checks = []
    brief_path = os.path.join(CAPSTONE, "client_brief.md")
    notes_path = os.path.join(CAPSTONE, "discovery_notes.md")
    eng_path = os.path.join(CAPSTONE, "engagement.json")
    for name, path in (("client_brief.md exists", brief_path),
                       ("discovery_notes.md exists", notes_path),
                       ("engagement.json exists", eng_path)):
        checks.append((name, os.path.isfile(path), path))
    if not all(ok for _n, ok, _d in checks):
        return checks
    eng = load_engagement(eng_path)
    built = sum(eng["price_build_up"].values())
    checks.append(("price build-up sums to fixed price",
                   built == eng["fixed_price_usd"],
                   f"build-up {built} vs fixed {eng['fixed_price_usd']}"))
    floor = eng["cost_floor"]
    parts = (floor["human_hours"] * floor["target_rate_usd_per_hour"]
             + floor["plan_share_usd"] + floor["measured_api_usd"])
    checks.append(("cost floor parts sum to total",
                   parts == floor["total_usd"],
                   f"parts {parts} vs total {floor['total_usd']}"))
    margin = eng["fixed_price_usd"] - floor["total_usd"]
    checks.append(("gross margin is price minus floor",
                   margin == eng["gross_margin_usd"],
                   f"computed {margin} vs stated {eng['gross_margin_usd']}"))
    with open(brief_path, encoding="utf-8") as f:
        brief = f.read().lower()
    for key, phrase in SCOPE_PHRASES.items():
        present = key in eng["price_build_up"] and phrase.lower() in brief
        checks.append((f"scope line in brief for {key}", present,
                       f"looking for {phrase!r} in client_brief.md"))
    checks.append(("assumptions are printed",
                   bool(eng.get("assumptions")),
                   f"{len(eng.get('assumptions', []))} assumption(s) listed"))
    return checks


def main():
    checks = run_checks()
    failed = 0
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {name}  ({detail})")
        failed += 0 if ok else 1
    print(f"{len(checks) - failed} of {len(checks)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
