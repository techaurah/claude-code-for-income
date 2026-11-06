#!/usr/bin/env python3
"""Estimate a scope by splitting agent time from human time.

Input is a JSON file with a tasks list. Each task has name,
agent_hours, human_hours, and uncertainty (low, med, high).

Buffers apply to human time only, because review, judgement,
and client handling are where variance lives:
  low 10 percent, med 25 percent, high 50 percent.

Standard library only. Offline. No credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

BUFFERS = {"low": 0.10, "med": 0.25, "high": 0.50}


def estimate(tasks):
    if not tasks:
        raise ValueError("task list must not be empty")
    agent_total = 0.0
    human_total = 0.0
    buffer_total = 0.0
    rows = []
    for task in tasks:
        level = str(task["uncertainty"]).lower()
        if level not in BUFFERS:
            raise ValueError(f"unknown uncertainty: {task['uncertainty']}")
        agent = float(task["agent_hours"])
        human = float(task["human_hours"])
        buffer = round(human * BUFFERS[level], 4)
        agent_total += agent
        human_total += human
        buffer_total += buffer
        rows.append({**task, "buffer_hours": buffer})
    human_with_buffer = round(human_total + buffer_total, 4)
    return {
        "tasks": rows,
        "agent_hours": round(agent_total, 4),
        "human_hours": round(human_total, 4),
        "buffer_hours": round(buffer_total, 4),
        "human_with_buffer": human_with_buffer,
        "total_hours": round(agent_total + human_with_buffer, 4),
        "range_low_hours": round(agent_total + human_total, 4),
        "range_high_hours": round(agent_total + human_with_buffer, 4),
    }


def load_tasks(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        return data["tasks"]
    return data


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "lumen_scope.json")
    result = estimate(load_tasks(path))
    print(json.dumps(result, indent=2))
    print()
    print(f"Human time: {result['human_hours']} hours, plus {result['buffer_hours']} buffer = {result['human_with_buffer']}")
    print(f"Agent time: {result['agent_hours']} hours")
    print(f"Range: {result['range_low_hours']} to {result['range_high_hours']} total hours")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
