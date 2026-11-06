#!/usr/bin/env python3
"""Smoke test for Lesson 09: clean plan, merge order, collision flag."""
import worktree_plan as wp


def main():
    plan = wp.build_plan(wp.DEMO_TASKS)
    assert not plan["has_collisions"], plan
    assert plan["collisions"] == []
    entries = plan["entries"]
    assert [e["task"] for e in entries] == [
        "api-handler", "booking-form", "docs"], entries
    assert [e["merge_order"] for e in entries] == [1, 2, 3]
    first = entries[0]
    assert first["directory"] == "../wt-api-handler"
    assert first["branch"] == "agent/api-handler"
    assert first["owner_agent"] == "builder"
    overlapping = wp.DEMO_TASKS + [
        {"id": "api-docs", "agent": "docs-writer",
         "files": ["src/api.py"], "depends_on": []},
    ]
    bad = wp.build_plan(overlapping)
    assert bad["has_collisions"], bad
    assert bad["collisions"][0]["file"] == "src/api.py"
    assert set(bad["collisions"][0]["tasks"]) == {"api-handler", "api-docs"}
    print("lesson 09 smoke test passed")


if __name__ == "__main__":
    main()
