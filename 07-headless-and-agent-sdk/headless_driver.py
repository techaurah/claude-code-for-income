#!/usr/bin/env python3
"""Build a safe headless claude -p command from a job spec.

This file drives a live Claude Code session when run for real.
Offline behaviour: if the claude CLI is absent, it prints the
command it would run and exits cleanly with code 0. Standard
library only. All caps come from the job spec and are validated.
"""
import json
import os
import shutil
import subprocess
import sys

DEMO_SPEC = {
    "prompt": "Run the test suite and summarise failures in three lines.",
    "allowed_tools": ["Read", "Bash"],
    "permission_mode": "default",
    "max_turns": 10,
    "max_budget_usd": 2.00,
}


def build_command(spec):
    """Return the claude -p argument list for a validated job spec."""
    prompt = spec.get("prompt", "").strip()
    if not prompt:
        raise ValueError("job spec needs a prompt")
    tools = spec.get("allowed_tools") or []
    if not tools:
        raise ValueError("job spec needs at least one allowed tool")
    max_turns = int(spec.get("max_turns", 10))
    if max_turns <= 0:
        raise ValueError("max_turns must be positive")
    budget = float(spec.get("max_budget_usd", 1.0))
    if budget <= 0:
        raise ValueError("max_budget_usd must be positive")
    return [
        "claude", "-p", prompt,
        "--allowedTools", ",".join(tools),
        "--permission-mode", str(spec.get("permission_mode", "default")),
        "--max-turns", str(max_turns),
        "--max-budget-usd", f"{budget:.2f}",
        "--output-format", "json",
    ]


def load_spec(argv):
    if argv:
        with open(argv[0], encoding="utf-8") as f:
            return json.load(f)
    return DEMO_SPEC


def main(argv):
    spec = load_spec(argv)
    command = build_command(spec)
    print("Command:", " ".join(command))
    if not shutil.which("claude"):
        print("claude CLI not found: nothing run. "
              "This is the offline path; review the command above.")
        return 0
    if "--run" not in argv:
        print("claude found, but --run was not given: nothing run.")
        return 0
    proc = subprocess.run(command, capture_output=True, text=True,
                          check=False)
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
