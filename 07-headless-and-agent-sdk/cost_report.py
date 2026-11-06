#!/usr/bin/env python3
"""Parse a headless JSON output file into a one line cost record.

Offline, standard library only. The total_cost_usd field in a
headless run's JSON output is a client side estimate, as the
official docs note. This record is for a cost ledger and for
comparing runs, not a billing invoice.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def parse_output(data):
    """Return a dict of the ledger fields from headless JSON output."""
    return {
        "cost_usd": float(data.get("total_cost_usd", 0.0)),
        "turns": int(data.get("num_turns", 0)),
        "duration_ms": int(data.get("duration_ms", 0)),
        "is_error": bool(data.get("is_error", False)),
        "session_id": str(data.get("session_id", "")),
    }


def format_record(record):
    return (f"cost_usd={record['cost_usd']:.4f} "
            f"turns={record['turns']} "
            f"duration_ms={record['duration_ms']} "
            f"is_error={record['is_error']} "
            f"session={record['session_id']}")


def summarize_file(path):
    with open(path, encoding="utf-8") as f:
        return format_record(parse_output(json.load(f)))


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "sample_output.json")
    print(summarize_file(path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
