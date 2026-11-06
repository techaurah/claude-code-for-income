#!/usr/bin/env python3
"""Smoke test for Lesson 20."""
import queue_sim as qs


def main():
    fx = qs.load_fixtures()
    over = qs.simulate(fx["overloaded_arrivals"], fx["minutes_per_order"], fx["weekly_capacity_minutes"], fx["sla_weeks"])
    assert over["total_breaches"] > 0, over
    assert over["final_backlog"] > 0
    assert over["first_unrecoverable_week"] is not None
    calm = qs.simulate(fx["calm_arrivals"], fx["minutes_per_order"], fx["weekly_capacity_minutes"], fx["sla_weeks"])
    assert calm["total_breaches"] == 0, calm
    assert calm["final_backlog"] == 0
    assert calm["first_unrecoverable_week"] is None
    print("lesson 20 smoke test passed")


if __name__ == "__main__":
    main()
