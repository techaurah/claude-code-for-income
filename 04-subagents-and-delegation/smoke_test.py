#!/usr/bin/env python3
"""Smoke test for Lesson 04: wave ordering and the review bounce."""
import dispatch_sim as sim


def main():
    waves = sim.build_waves(sim.DEMO_TASKS)
    assert waves == [["form"], ["tests"], ["review"]], waves
    flat = [task for wave in waves for task in wave]
    assert flat.index("form") < flat.index("tests") < flat.index("review")
    parallel = [
        {"id": "a", "agent": "builder", "depends_on": []},
        {"id": "b", "agent": "builder", "depends_on": []},
        {"id": "c", "agent": "code-reviewer", "depends_on": ["a", "b"]},
    ]
    assert sim.build_waves(parallel) == [["a", "b"], ["c"]]
    schedule = sim.simulate(sim.DEMO_TASKS, bounce_ids={"form"})
    form_events = [e for e in schedule if e["task"] == "form"]
    assert len(form_events) == 2, form_events
    assert form_events[0]["review"] == "bounced"
    assert form_events[1]["attempt"] == 2 and form_events[1]["review"] == "passed"
    assert form_events[1]["wave"] > form_events[0]["wave"]
    clean = sim.simulate(sim.DEMO_TASKS)
    assert len(clean) == 3 and all(e["attempt"] == 1 for e in clean)
    print("lesson 04 smoke test passed")


if __name__ == "__main__":
    main()
