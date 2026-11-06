#!/usr/bin/env python3
"""Recommend an unattended mode for a job, with reasons.

Offline, standard library only, deterministic. Inputs describe
the job constraints: trigger type, machine availability, whether
repo events are needed, whether session context must be kept,
whether a human checkpoint is wanted, and whether the machine
already has a scheduler such as cron.
"""
import sys

MODES = ("background_agent", "headless", "in_session_loop",
         "cloud_scheduled_task", "own_cron_headless")


def recommend(job):
    """Return {'mode': str, 'reasons': [str, ...]} for a job dict."""
    trigger = job.get("trigger", "manual")
    if job.get("needs_repo_events") or trigger == "github_event":
        return {"mode": "cloud_scheduled_task", "reasons": [
            "the trigger is a repository event, so the run must "
            "live where repository events arrive",
            "no local machine needs to be awake when the event fires",
        ]}
    if job.get("keep_context") or trigger == "loop":
        return {"mode": "in_session_loop", "reasons": [
            "the job needs the context of a live session between runs",
            "a loop inside the session repeats without losing state",
        ]}
    if job.get("wants_checkpoint") or trigger == "supervised":
        return {"mode": "background_agent", "reasons": [
            "a human checkpoint is wanted partway through",
            "a background session stays visible and resumable",
        ]}
    if trigger == "cron" and job.get("own_scheduler"):
        return {"mode": "own_cron_headless", "reasons": [
            "the machine is available and already runs a scheduler",
            "own cron running a capped headless command keeps "
            "logs and control local",
        ]}
    if trigger == "schedule" and not job.get("machine_always_on", True):
        return {"mode": "cloud_scheduled_task", "reasons": [
            "the job runs on a clock but the local machine is "
            "not always on",
            "a cloud scheduled task does not depend on a laptop "
            "being awake",
        ]}
    return {"mode": "headless", "reasons": [
        "the job is one bounded run with no live context need",
        "a capped claude -p call inside your own pipeline is "
        "the simplest fit",
    ]}


DEMO_JOBS = [
    ("PR review", {"trigger": "github_event", "needs_repo_events": True}),
    ("Watch a deploy in session", {"trigger": "loop", "keep_context": True}),
    ("Long refactor with a checkpoint", {"trigger": "supervised",
                                          "wants_checkpoint": True}),
    ("Nightly tests on an always on box",
     {"trigger": "cron", "own_scheduler": True, "machine_always_on": True}),
    ("Weekly report while travelling",
     {"trigger": "schedule", "machine_always_on": False}),
    ("One off audit from a script", {"trigger": "manual"}),
]


def main():
    for name, job in DEMO_JOBS:
        result = recommend(job)
        print(f"{name}: {result['mode']}")
        for reason in result["reasons"]:
            print(f"  - {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
