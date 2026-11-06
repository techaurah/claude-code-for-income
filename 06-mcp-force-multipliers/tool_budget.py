#!/usr/bin/env python3
"""Estimate the context cost of MCP tool definitions against a budget.

Offline, standard library only. Heuristic, labelled as such: the
estimated tokens for a tool are the characters of its JSON form
divided by four, rounded up. Good enough to compare server sets
and enforce a budget, not a billing figure.
"""
import json
import math
import os
import sys

DEFAULT_BUDGET_TOKENS = 800

DEMO_TOOLS = [
    {"name": "read_file", "description": "Read a file by path",
     "inputSchema": {"type": "object",
                     "properties": {"path": {"type": "string"}}}},
    {"name": "create_issue", "description": "Create an issue with a title",
     "inputSchema": {"type": "object",
                     "properties": {"title": {"type": "string"}}}},
]


def estimate_tokens(tool):
    """Estimated tokens for one tool definition: chars / 4, rounded up."""
    return math.ceil(len(json.dumps(tool, sort_keys=True)) / 4)


def evaluate(tools, budget=DEFAULT_BUDGET_TOKENS):
    per_tool = {t.get("name", "?"): estimate_tokens(t) for t in tools}
    total = sum(per_tool.values())
    return {
        "per_tool": per_tool,
        "total": total,
        "budget": budget,
        "over_budget": total > budget,
        "heuristic": "chars/4",
    }


def load_tools(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        return data.get("tools", [])
    return data


def main(argv):
    tools = DEMO_TOOLS
    budget = DEFAULT_BUDGET_TOKENS
    if argv:
        tools = load_tools(argv[0])
    if len(argv) > 1:
        budget = int(argv[1])
    result = evaluate(tools, budget=budget)
    for name, cost in result["per_tool"].items():
        print(f"  {name}: about {cost} tokens (chars/4 heuristic)")
    print(f"total: about {result['total']} tokens, "
          f"budget {result['budget']}, "
          f"{'OVER BUDGET' if result['over_budget'] else 'within budget'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
