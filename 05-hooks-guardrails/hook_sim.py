#!/usr/bin/env python3
"""Feed sample hook events through guard.py and report decisions.

Uses a subprocess per event, exactly as a hook runner would, so
the exit code path is exercised too. Offline, no live session.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GUARD = os.path.join(HERE, "guard.py")

SAMPLE_EVENTS = [
    {"tool_name": "Bash", "tool_input": {"command": "python3 -m pytest -q"}},
    {"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}},
    {"tool_name": "Read", "tool_input": {"file_path": ".env"}},
    {"tool_name": "Bash", "tool_input": {"command": "cat config/.env.local"}},
    {"tool_name": "Bash", "tool_input": {"command": "git push origin main --force"}},
    {"tool_name": "Bash", "tool_input": {"command": "git status --short"}},
    {"tool_name": "Read", "tool_input": {"file_path": "src/app.py"}},
]


def run_event(event):
    proc = subprocess.run(
        [sys.executable, GUARD], input=json.dumps(event),
        capture_output=True, text=True, check=False)
    data = json.loads(proc.stdout.strip() or "{}")
    return {"event": event, "decision": data.get("decision"),
            "reason": data.get("reason"), "exit_code": proc.returncode}


def run_samples():
    return [run_event(event) for event in SAMPLE_EVENTS]


def main():
    for result in run_samples():
        import guard
        text = guard.extract_command(result["event"])
        print(f"{result['decision']}: {text} ({result['reason']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
