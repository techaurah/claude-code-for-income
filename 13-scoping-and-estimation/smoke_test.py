#!/usr/bin/env python3
"""Smoke test for Lesson 13: fixture totals and buffer math."""
import os

import scope_estimator as se

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    tasks = se.load_tasks(os.path.join(HERE, "lumen_scope.json"))
    result = se.estimate(tasks)
    assert result["human_hours"] == 9.0
    assert result["agent_hours"] == 13.0
    assert result["buffer_hours"] == 2.15
    assert result["human_with_buffer"] == 11.15
    assert result["range_low_hours"] == 22.0
    assert result["range_high_hours"] == 24.15
    single = se.estimate([{"name": "x", "agent_hours": 0, "human_hours": 10, "uncertainty": "high"}])
    assert single["buffer_hours"] == 5.0
    single_low = se.estimate([{"name": "x", "agent_hours": 0, "human_hours": 10, "uncertainty": "low"}])
    assert single_low["buffer_hours"] == 1.0
    print("lesson 13 smoke test passed")


if __name__ == "__main__":
    main()
