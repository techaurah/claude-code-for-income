#!/usr/bin/env python3
"""Score an automation audit intake into a lead-flow style report.

Reads a JSON intake (channels, weekly volume band, after-hours
share, response time band, follow-up practice, booking method)
and scores six dimensions from 0 to 100. The report names the
weakest dimension first, so the worst leak gets read first.

Standard library only, offline, no credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

RESPONSE_SPEED = {
    "under_5_min": 95,
    "under_1_hour": 70,
    "hours": 35,
    "next_day": 10,
    "no_reply_often": 0,
}

FOLLOW_UP = {
    "systematic": 90,
    "automated_sequence": 85,
    "ad_hoc": 45,
    "none": 10,
}

BOOKING = {
    "online_self_serve": 90,
    "online_request": 65,
    "message_only": 40,
    "phone_only": 30,
}

CAPACITY = {
    "under_10": 85,
    "10-30": 65,
    "30-60": 50,
    "60-120": 35,
    "over_120": 20,
}

KNOWN_CHANNELS = ("instagram", "whatsapp", "website", "phone")

DIMENSION_LABELS = {
    "response_speed": "Response speed",
    "after_hours_coverage": "After-hours coverage",
    "follow_up_discipline": "Follow-up discipline",
    "booking_ease": "Booking ease",
    "channel_coverage": "Channel coverage",
    "capacity_headroom": "Capacity headroom",
}


def _band_score(table, value, field):
    if value not in table:
        raise ValueError(f"unknown {field}: {value!r} "
                         f"(expected one of {sorted(table)})")
    return table[value]


def score_intake(intake):
    """Return {dimension: score} with every score in 0..100."""
    channels = intake.get("channels", [])
    share = intake.get("after_hours_share_percent", 0)
    if not 0 <= share <= 100:
        raise ValueError("after_hours_share_percent must be 0 to 100")
    handled = len([c for c in channels if c in KNOWN_CHANNELS])
    scores = {
        "response_speed": _band_score(
            RESPONSE_SPEED, intake.get("current_response_time_band"),
            "current_response_time_band"),
        "after_hours_coverage": max(0, round(100 - share * 1.2)),
        "follow_up_discipline": _band_score(
            FOLLOW_UP, intake.get("follow_up_practice"),
            "follow_up_practice"),
        "booking_ease": _band_score(
            BOOKING, intake.get("booking_method"), "booking_method"),
        "channel_coverage": min(100, handled * 25),
        "capacity_headroom": _band_score(
            CAPACITY, intake.get("weekly_enquiry_volume_band"),
            "weekly_enquiry_volume_band"),
    }
    for key, value in scores.items():
        assert 0 <= value <= 100, f"{key} out of bounds: {value}"
    return scores


def overall(scores):
    return round(sum(scores.values()) / len(scores))


def weakest_first(scores):
    """(dimension, score) pairs sorted weakest first."""
    return sorted(scores.items(), key=lambda kv: (kv[1], kv[0]))


def build_report(intake):
    scores = score_intake(intake)
    ordered = weakest_first(scores)
    lines = []
    lines.append(f"Audit findings: {intake.get('business', 'unnamed business')}")
    lines.append(f"Overall lead-flow score: {overall(scores)} of 100")
    lines.append("")
    lines.append("Dimensions, weakest first:")
    for key, value in ordered:
        lines.append(f"  {DIMENSION_LABELS[key]}: {value}")
    lines.append("")
    worst_key, worst_value = ordered[0]
    lines.append(f"Weakest dimension: {DIMENSION_LABELS[worst_key]} "
                 f"at {worst_value}. Start the conversation here.")
    return "\n".join(lines)


def load_intake(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "intake_dental.json")
    print(build_report(load_intake(path)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
