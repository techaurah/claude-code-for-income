#!/usr/bin/env python3
"""Smoke test for Lesson 05: guard deny and allow cases, plus settings."""
import json
import os

import guard
import hook_sim

HERE = os.path.dirname(os.path.abspath(__file__))


def ev(command=None, path=None):
    tool_input = {}
    if command is not None:
        tool_input["command"] = command
    if path is not None:
        tool_input["file_path"] = path
    return {"tool_name": "Bash", "tool_input": tool_input}


def main():
    assert guard.evaluate(ev(command="rm -rf build"))["decision"] == "deny"
    assert guard.evaluate(ev(command="rm -fr /tmp/x"))["decision"] == "deny"
    assert guard.evaluate(ev(path=".env"))["decision"] == "deny"
    assert guard.evaluate(ev(command="cat .env"))["decision"] == "deny"
    assert guard.evaluate(ev(command="git push origin main --force"))["decision"] == "deny"
    assert guard.evaluate(ev(command="python3 -m pytest -q"))["decision"] == "allow"
    assert guard.evaluate(ev(path="src/app.py"))["decision"] == "allow"
    assert guard.evaluate(ev(command="git status --short"))["decision"] == "allow"
    results = hook_sim.run_samples()
    decisions = [r["decision"] for r in results]
    assert decisions.count("deny") == 4, decisions
    assert decisions.count("allow") == 3, decisions
    assert all(r["exit_code"] == (2 if r["decision"] == "deny" else 0)
               for r in results)
    with open(os.path.join(HERE, "hooks", "settings.example.json"),
              encoding="utf-8") as f:
        settings = json.load(f)
    hooks = settings["hooks"]
    assert set(hooks) == {"PreToolUse", "PostToolUse", "Stop"}, hooks
    print("lesson 05 smoke test passed")


if __name__ == "__main__":
    main()
