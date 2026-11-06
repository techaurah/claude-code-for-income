#!/usr/bin/env python3
"""Smoke test for Lesson 29: the whole spec pack passes its checks."""
import capstone_check as cc


def main():
    checks = cc.run_checks()
    failed = [name for name, ok, _d in checks if not ok]
    assert not failed, f"spec pack checks failed: {failed}"
    eng = cc.load_engagement()
    assert eng["client"] == "Lumen Med Spa (fictional)"
    assert eng["fixed_price_usd"] == 1850
    assert sum(eng["price_build_up"].values()) == 1850
    floor = eng["cost_floor"]
    assert floor["human_hours"] == 9
    assert floor["target_rate_usd_per_hour"] == 75
    assert floor["total_usd"] == 720
    assert eng["gross_margin_usd"] == 1130
    assert len(checks) >= 10
    print("lesson 29 smoke test passed")


if __name__ == "__main__":
    main()
