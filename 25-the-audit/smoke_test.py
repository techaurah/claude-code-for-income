#!/usr/bin/env python3
"""Smoke test for Lesson 25: scoring bounds and weakest-first order."""
import json
import os

import audit_score as audit

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "intake_dental.json"),
              encoding="utf-8") as f:
        intake = json.load(f)
    scores = audit.score_intake(intake)
    assert len(scores) == 6
    for key, value in scores.items():
        assert 0 <= value <= 100, f"{key} out of bounds: {value}"
    assert scores["follow_up_discipline"] == 10
    assert scores["response_speed"] == 35
    ordered = audit.weakest_first(scores)
    values = [v for _k, v in ordered]
    assert values == sorted(values), "report must be weakest first"
    assert ordered[0][0] == "follow_up_discipline"
    assert audit.overall(scores) == 39
    report = audit.build_report(intake)
    assert "Weakest dimension: Follow-up discipline" in report
    best = dict(intake, current_response_time_band="under_5_min",
                after_hours_share_percent=5, follow_up_practice="systematic",
                booking_method="online_self_serve",
                weekly_enquiry_volume_band="under_10",
                channels=["instagram", "whatsapp", "website", "phone"])
    top = audit.score_intake(best)
    assert all(v >= 80 for v in top.values())
    print("lesson 25 smoke test passed")


if __name__ == "__main__":
    main()
