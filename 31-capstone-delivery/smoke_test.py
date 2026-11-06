#!/usr/bin/env python3
"""Smoke test for Lesson 31: verdict bands and checklist contents."""
import delivery_pack as dp
import rubric_score as rs


def main():
    perfect = {key: 3 for key in rs.WEIGHTS}
    percent, band = rs.score_grades(perfect)
    assert percent == 100.0 and band == "ship it"
    zero = {key: 0 for key in rs.WEIGHTS}
    percent0, band0 = rs.score_grades(zero)
    assert percent0 == 0.0 and band0 == "redo"
    worked = {"scope_fidelity": 3, "price_integrity": 3,
              "qa_evidence": 3, "handover_completeness": 2,
              "honesty_of_numbers": 3, "support_readiness": 2}
    percent_w, band_w = rs.score_grades(worked)
    assert percent_w == 91.7 and band_w == "ship it"
    middle = {key: 2 for key in rs.WEIGHTS}
    percent_m, band_m = rs.score_grades(middle)
    assert abs(percent_m - 66.7) < 0.1 and band_m == "fix and reship"
    for bad in (4, -1):
        broken = dict(perfect, scope_fidelity=bad)
        try:
            rs.score_grades(broken)
        except ValueError:
            pass
        else:
            raise AssertionError(f"score {bad} must be refused")
    checklist = dp.build_checklist(dp.load_engagement())
    for key in ("discovery_and_scope", "build", "qa_and_hardening",
                "handover_and_training", "support_window_30d"):
        assert key in checklist, key
    assert "$1850" in checklist
    print("lesson 31 smoke test passed")


if __name__ == "__main__":
    main()
