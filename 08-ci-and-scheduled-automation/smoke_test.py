#!/usr/bin/env python3
"""Smoke test for Lesson 08: every planner branch, plus the workflow file."""
import os

import schedule_plan as sp

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    cases = [
        ({"trigger": "github_event", "needs_repo_events": True},
         "cloud_scheduled_task"),
        ({"trigger": "loop", "keep_context": True}, "in_session_loop"),
        ({"trigger": "supervised", "wants_checkpoint": True},
         "background_agent"),
        ({"trigger": "cron", "own_scheduler": True,
          "machine_always_on": True}, "own_cron_headless"),
        ({"trigger": "schedule", "machine_always_on": False},
         "cloud_scheduled_task"),
        ({"trigger": "manual"}, "headless"),
        ({"trigger": "one_off"}, "headless"),
    ]
    seen = set()
    for job, expected in cases:
        result = sp.recommend(job)
        assert result["mode"] == expected, (job, result)
        assert result["reasons"], result
        seen.add(result["mode"])
    assert seen == set(sp.MODES), seen
    with open(os.path.join(HERE, "claude-review.yml"),
              encoding="utf-8") as f:
        workflow = f.read()
    assert "anthropics/claude-code-action@v1" in workflow
    assert "pull_request" in workflow
    assert "secrets.ANTHROPIC_API_KEY" in workflow
    print("lesson 08 smoke test passed")


if __name__ == "__main__":
    main()
