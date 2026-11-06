#!/usr/bin/env python3
"""Verify the course environment and (with --write) record a cost baseline.

Checks Python, git, the optional claude CLI, and the lesson layout.
Prints a plain report and exits nonzero only on a hard failure
(Python too old, or lesson folders missing). No network, no
credentials, nothing installed.
"""
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

EXPECTED_LESSONS = 32

BASELINE_TEMPLATE = {
    "_about": "Your cost baseline. Local only; the course calculators "
              "read this file. Prices checked October 2026; update "
              "them when yours change.",
    "plan": "max-5x",
    "plan_price_usd_per_month": 100,
    "target_rate_usd_per_hour": 50,
    "platform_fee_percent": 0,
    "clients_now": 0,
    "billable_hours_available_per_month": 40,
}


def python_ok(version=None):
    v = version or sys.version_info
    return (v[0], v[1]) >= (3, 11)


def lesson_count(root=ROOT):
    return sum(
        1 for name in os.listdir(root)
        if len(name) > 3 and name[:2].isdigit() and name[2] == "-"
        and os.path.isdir(os.path.join(root, name)))


def report():
    lines = []
    ok = True
    lines.append(f"Python: {sys.version.split()[0]} "
                 f"({'ok' if python_ok() else 'TOO OLD, need 3.11+'})")
    ok = ok and python_ok()
    git = shutil.which("git")
    lines.append(f"git: {'found at ' + git if git else 'not found (Lessons 08 and 09 assume it)'}")
    claude = shutil.which("claude")
    lines.append(f"claude CLI: {'found at ' + claude if claude else 'not found (fine: every lesson has an offline path)'}")
    count = lesson_count()
    lines.append(f"Lesson folders: {count} of {EXPECTED_LESSONS} "
                 f"({'ok' if count == EXPECTED_LESSONS else 'PARTIAL CLONE'})")
    ok = ok and count == EXPECTED_LESSONS
    return ok, lines


def main(argv):
    ok, lines = report()
    for line in lines:
        print(line)
    if "--write" in argv:
        path = os.path.join(HERE, "baseline.json")
        if os.path.exists(path):
            print(f"baseline.json already exists at {path}; left untouched")
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(BASELINE_TEMPLATE, f, indent=2)
            print(f"Wrote {path}; edit the four numbers to yours")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
