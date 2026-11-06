#!/usr/bin/env python3
"""Smoke test for Lesson 11: per job and total pricing."""
import os

import job_cost as jc

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    jobs = jc.load_jobs(os.path.join(HERE, "jobs.csv"))
    assert len(jobs) == 4
    by_name = {job["name"]: jc.price_job(job) for job in jobs}
    assert by_name["intake-router"] == 0.2
    assert by_name["summarize-notes"] == 7.2
    assert by_name["batch-reports"] == 9.0
    assert by_name["retry-storm-booking"] == 54.0
    result = jc.summarise(jobs)
    assert result["total_usd"] == 70.4
    assert result["most_expensive"]["name"] == "retry-storm-booking"
    cached_job = {"model": "sonnet", "input_tokens": 1_000_000, "output_tokens": 0, "cached_input_tokens": 1_000_000, "batch": "false"}
    assert jc.price_job(cached_job) == 0.2
    print("lesson 11 smoke test passed")


if __name__ == "__main__":
    main()
