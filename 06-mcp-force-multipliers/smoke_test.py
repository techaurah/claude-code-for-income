#!/usr/bin/env python3
"""Smoke test for Lesson 06: token estimates, totals, over budget flag."""
import json
import math
import os

import tool_budget as tb

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    tool = {"name": "x", "description": "y"}
    expected = math.ceil(len(json.dumps(tool, sort_keys=True)) / 4)
    assert tb.estimate_tokens(tool) == expected
    result = tb.evaluate(tb.DEMO_TOOLS)
    assert result["total"] == sum(result["per_tool"].values())
    assert result["total"] > 0
    assert not result["over_budget"], result
    assert result["heuristic"] == "chars/4"
    tight = tb.evaluate(tb.DEMO_TOOLS, budget=1)
    assert tight["over_budget"]
    with open(os.path.join(HERE, "mcp_config.example.json"),
              encoding="utf-8") as f:
        config = json.load(f)
    servers = config["mcpServers"]
    assert len(servers) == 2, servers
    assert all("command" in s for s in servers.values())
    print("lesson 06 smoke test passed")


if __name__ == "__main__":
    main()
