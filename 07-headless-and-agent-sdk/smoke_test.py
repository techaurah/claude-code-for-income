#!/usr/bin/env python3
"""Smoke test for Lesson 07: command construction and cost parsing, offline."""
import json
import os

import cost_report as cr
import headless_driver as hd

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    cmd = hd.build_command(hd.DEMO_SPEC)
    assert cmd[0] == "claude" and cmd[1] == "-p"
    assert "--allowedTools" in cmd and "Read,Bash" in cmd
    assert "--max-turns" in cmd and cmd[cmd.index("--max-turns") + 1] == "10"
    assert "--max-budget-usd" in cmd
    assert "--output-format" in cmd and cmd[-1] == "json"
    for bad in ({"prompt": "", "allowed_tools": ["Read"]},
                {"prompt": "x", "allowed_tools": []},
                {"prompt": "x", "allowed_tools": ["Read"], "max_turns": 0},
                {"prompt": "x", "allowed_tools": ["Read"],
                 "max_budget_usd": 0}):
        try:
            hd.build_command(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"bad spec accepted: {bad}")
    with open(os.path.join(HERE, "sample_output.json"),
              encoding="utf-8") as f:
        data = json.load(f)
    record = cr.parse_output(data)
    assert abs(record["cost_usd"] - 0.42) < 1e-9, record
    assert record["turns"] == 6 and record["duration_ms"] == 45210
    assert record["is_error"] is False
    line = cr.summarize_file(os.path.join(HERE, "sample_output.json"))
    assert "cost_usd=0.4200" in line and "turns=6" in line, line
    print("lesson 07 smoke test passed")


if __name__ == "__main__":
    main()
