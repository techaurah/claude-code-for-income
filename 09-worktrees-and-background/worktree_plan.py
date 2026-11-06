#!/usr/bin/env python3
"""Build a worktree plan from a task list with file ownership.

Offline, standard library only, deterministic. Each task gets a
worktree directory, a branch, an owner agent, and a merge order
position that respects dependencies. Files claimed by more than
one task are flagged as collisions.
"""
import json
import sys

DEMO_TASKS = [
    {"id": "api-handler", "agent": "builder",
     "files": ["src/api.py"], "depends_on": []},
    {"id": "booking-form", "agent": "builder",
     "files": ["src/form.py"], "depends_on": ["api-handler"]},
    {"id": "docs", "agent": "docs-writer",
     "files": ["docs/usage.md"], "depends_on": ["booking-form"]},
]


def merge_order(tasks):
    """Task ids in dependency order, stable for equal depth."""
    by_id = {t["id"]: t for t in tasks}
    for t in tasks:
        for dep in t.get("depends_on", []):
            if dep not in by_id:
                raise ValueError(f"task {t['id']} depends on unknown {dep}")
    ordered, done, remaining = [], set(), list(tasks)
    while remaining:
        ready = [t for t in remaining
                 if all(d in done for d in t.get("depends_on", []))]
        if not ready:
            raise ValueError("dependency cycle in task list")
        for t in ready:
            ordered.append(t["id"])
            done.add(t["id"])
            remaining.remove(t)
    return ordered


def find_collisions(tasks):
    owners = {}
    for t in tasks:
        for path in t.get("files", []):
            owners.setdefault(path, []).append(t["id"])
    return [{"file": path, "tasks": ids}
            for path, ids in sorted(owners.items()) if len(ids) > 1]


def build_plan(tasks, base_dir="../wt"):
    order = merge_order(tasks)
    by_id = {t["id"]: t for t in tasks}
    entries = []
    for position, task_id in enumerate(order, start=1):
        t = by_id[task_id]
        entries.append({
            "task": task_id,
            "directory": f"{base_dir}-{task_id}",
            "branch": f"agent/{task_id}",
            "owner_agent": t.get("agent", "builder"),
            "files": list(t.get("files", [])),
            "merge_order": position,
        })
    collisions = find_collisions(tasks)
    return {"entries": entries, "collisions": collisions,
            "has_collisions": bool(collisions)}


def main(argv):
    tasks = DEMO_TASKS
    if argv:
        with open(argv[0], encoding="utf-8") as f:
            data = json.load(f)
        tasks = data["tasks"] if isinstance(data, dict) else data
    plan = build_plan(tasks)
    for e in plan["entries"]:
        print(f"merge {e['merge_order']}: {e['task']} "
              f"dir={e['directory']} branch={e['branch']} "
              f"owner={e['owner_agent']} files={', '.join(e['files'])}")
    if plan["has_collisions"]:
        for c in plan["collisions"]:
            print(f"COLLISION: {c['file']} claimed by "
                  f"{', '.join(c['tasks'])}")
    else:
        print("no ownership collisions")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
