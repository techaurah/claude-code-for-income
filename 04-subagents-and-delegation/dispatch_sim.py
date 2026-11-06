#!/usr/bin/env python3
"""Simulate dispatching tasks to named subagents in parallel waves.

Offline, standard library only, fully deterministic. Tasks carry
dependencies. Tasks whose dependencies are done form a wave and
can run in parallel. A task in the bounce set fails its first
review gate and runs once more in the following wave, then passes.
"""
import json
import os
import sys

DEMO_TASKS = [
    {"id": "form", "agent": "builder", "depends_on": []},
    {"id": "tests", "agent": "test-writer", "depends_on": ["form"]},
    {"id": "review", "agent": "code-reviewer", "depends_on": ["form", "tests"]},
]


def build_waves(tasks):
    """Group task ids into waves by dependency depth."""
    by_id = {t["id"]: t for t in tasks}
    for t in tasks:
        for dep in t.get("depends_on", []):
            if dep not in by_id:
                raise ValueError(f"task {t['id']} depends on unknown {dep}")
    depth = {}

    def depth_of(task_id, seen):
        if task_id in depth:
            return depth[task_id]
        if task_id in seen:
            raise ValueError(f"dependency cycle at {task_id}")
        deps = by_id[task_id].get("depends_on", [])
        value = 0 if not deps else 1 + max(
            depth_of(d, seen | {task_id}) for d in deps)
        depth[task_id] = value
        return value

    for t in tasks:
        depth_of(t["id"], set())
    waves = []
    for t in tasks:
        d = depth[t["id"]]
        while len(waves) <= d:
            waves.append([])
        waves[d].append(t["id"])
    return waves


def simulate(tasks, bounce_ids=()):
    """Return a schedule: ordered events with wave, task, agent, attempt."""
    bounce = set(bounce_ids)
    by_id = {t["id"]: t for t in tasks}
    waves = build_waves(tasks)
    schedule = []
    wave_no = 0
    pending_bounces = []
    for wave in waves:
        wave_no += 1
        for task_id in wave:
            schedule.append({
                "wave": wave_no, "task": task_id,
                "agent": by_id[task_id]["agent"], "attempt": 1,
                "review": "bounced" if task_id in bounce else "passed",
            })
            if task_id in bounce:
                pending_bounces.append(task_id)
        if pending_bounces:
            wave_no += 1
            for task_id in pending_bounces:
                schedule.append({
                    "wave": wave_no, "task": task_id,
                    "agent": by_id[task_id]["agent"], "attempt": 2,
                    "review": "passed",
                })
            pending_bounces = []
    return schedule


def print_schedule(schedule):
    for event in schedule:
        print(f"wave {event['wave']}: {event['task']} "
              f"-> {event['agent']} (attempt {event['attempt']}, "
              f"review {event['review']})")


def main(argv):
    tasks = DEMO_TASKS
    bounce = {"form"}
    if argv:
        with open(argv[0], encoding="utf-8") as f:
            data = json.load(f)
        tasks = data["tasks"] if isinstance(data, dict) else data
        bounce = set(data.get("bounce", [])) if isinstance(data, dict) else set()
    schedule = simulate(tasks, bounce_ids=bounce)
    print_schedule(schedule)
    print(f"{len(schedule)} event(s) for {len(tasks)} task(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
