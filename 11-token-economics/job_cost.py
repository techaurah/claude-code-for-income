#!/usr/bin/env python3
"""Price a ledger of jobs from a CSV file.

Columns: name, model, input_tokens, output_tokens,
cached_input_tokens, batch

Pricing uses October 2026 list prices per million tokens.
Cache reads are priced at one tenth of the input price. That
is labelled here as the current Sonnet class behaviour and is
applied as the course model for this calculator. Batch jobs
are half price after caching is applied.

Standard library only. Offline. No credentials.
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

API_PRICES = {
    "sonnet": {"input_per_million": 2.0, "output_per_million": 10.0},
    "opus": {"input_per_million": 4.0, "output_per_million": 20.0},
    "haiku": {"input_per_million": 0.10, "output_per_million": 0.50},
    "fable": {"input_per_million": 10.0, "output_per_million": 50.0},
}

CACHE_FACTOR = 0.1
BATCH_FACTOR = 0.5


def price_job(job):
    """Return the cost in USD for one job dict."""
    model = job["model"].lower()
    if model not in API_PRICES:
        raise ValueError(f"unknown model class: {job['model']}")
    input_tokens = int(job.get("input_tokens", 0))
    output_tokens = int(job.get("output_tokens", 0))
    cached = int(job.get("cached_input_tokens", 0))
    if cached > input_tokens:
        raise ValueError("cached input tokens cannot exceed input tokens")
    prices = API_PRICES[model]
    in_price = prices["input_per_million"]
    out_price = prices["output_per_million"]
    uncached = input_tokens - cached
    cost = (uncached / 1_000_000 * in_price
            + cached / 1_000_000 * in_price * CACHE_FACTOR
            + output_tokens / 1_000_000 * out_price)
    batch = str(job.get("batch", "false")).lower() in ("true", "1", "yes")
    if batch:
        cost *= BATCH_FACTOR
    return round(cost, 4)


def load_jobs(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        jobs = []
        for row in reader:
            jobs.append({
                "name": row["name"],
                "model": row["model"],
                "input_tokens": int(row["input_tokens"]),
                "output_tokens": int(row["output_tokens"]),
                "cached_input_tokens": int(row.get("cached_input_tokens") or 0),
                "batch": row.get("batch", "false"),
            })
        return jobs


def summarise(jobs):
    priced = []
    total = 0.0
    for job in jobs:
        cost = price_job(job)
        total += cost
        priced.append({**job, "cost_usd": cost})
    priced_sorted = sorted(priced, key=lambda item: item["cost_usd"], reverse=True)
    return {
        "jobs": priced,
        "total_usd": round(total, 4),
        "job_count": len(priced),
        "most_expensive": priced_sorted[0] if priced_sorted else None,
        "average_usd": round(total / len(priced), 4) if priced else 0.0,
    }


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "jobs.csv")
    result = summarise(load_jobs(path))
    for job in result["jobs"]:
        print(f"{job['name']}: ${job['cost_usd']:.2f} ({job['model']})")
    print(f"Total for {result['job_count']} jobs: ${result['total_usd']:.2f}")
    if result["most_expensive"]:
        print(f"Most expensive job: {result['most_expensive']['name']} at ${result['most_expensive']['cost_usd']:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
