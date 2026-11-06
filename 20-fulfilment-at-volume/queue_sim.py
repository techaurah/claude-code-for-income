#!/usr/bin/env python3
"""Simulate a fulfilment queue week by week.

Orders arrive in a fixed pattern. Each order needs a fixed number
of human minutes. Each week has a fixed capacity. Orders are
served first in, first out. An order that waits longer than the
SLA limit counts as a breach. The queue is called unrecoverable
in the first week where the backlog alone needs more than two
weeks of capacity and arrivals still exceed what one week can
serve. At that point, working harder does not clear it. Pausing
intake does. Offline, deterministic, no credentials.
"""
import json
import os
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load_fixtures(path=None):
    path = path or os.path.join(HERE, "fixtures.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def simulate(weekly_arrivals, minutes_per_order, weekly_capacity_minutes, sla_weeks=2):
    queue = deque()
    next_id = 1
    weeks = []
    total_breaches = 0
    first_unrecoverable = None
    for week_idx, arrivals in enumerate(weekly_arrivals, 1):
        for _ in range(arrivals):
            queue.append({"id": next_id, "arrived_week": week_idx})
            next_id += 1
        capacity = weekly_capacity_minutes
        served = 0
        while queue and capacity >= minutes_per_order:
            queue.popleft()
            capacity -= minutes_per_order
            served += 1
        breaches = sum(1 for o in queue if week_idx - o["arrived_week"] >= sla_weeks)
        total_breaches += breaches
        backlog = len(queue)
        backlog_minutes = backlog * minutes_per_order
        arrivals_minutes = arrivals * minutes_per_order
        unrecoverable = backlog_minutes > 2 * weekly_capacity_minutes and arrivals_minutes > weekly_capacity_minutes
        if unrecoverable and first_unrecoverable is None:
            first_unrecoverable = week_idx
        weeks.append({"week": week_idx, "arrivals": arrivals, "served": served, "backlog": backlog, "breaches_this_week": breaches, "unrecoverable": unrecoverable})
    return {"weeks": weeks, "total_breaches": total_breaches, "final_backlog": len(queue), "first_unrecoverable_week": first_unrecoverable}


def main():
    fx = load_fixtures()
    for label, arrivals in (("Overloaded", fx["overloaded_arrivals"]), ("Within capacity", fx["calm_arrivals"])):
        result = simulate(arrivals, fx["minutes_per_order"], fx["weekly_capacity_minutes"], fx["sla_weeks"])
        print(f"{label}: final backlog {result['final_backlog']}, total breach-weeks {result['total_breaches']}, first unrecoverable week: {result['first_unrecoverable_week']}")
        for row in result["weeks"]:
            print(f"  week {row['week']}: arrivals {row['arrivals']}, served {row['served']}, backlog {row['backlog']}, breaches {row['breaches_this_week']}")


if __name__ == "__main__":
    main()
