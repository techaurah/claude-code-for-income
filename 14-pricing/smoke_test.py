#!/usr/bin/env python3
"""Smoke test for Lesson 14: floor, fee math, and margin."""
import price_model as pm


def main():
    assert pm.cost_floor(9, 75, 25, 20) == 720.0
    assert pm.effective_received(1850, 10) == 1665.0
    assert pm.effective_received(1850, 20) == 1480.0
    assert pm.effective_received(1850, 0) == 1850.0
    assert pm.fee_adjusted_floor(720, 10) == 800.0
    margin = pm.margin_at_price(1850, 720)
    assert margin["gross_margin_usd"] == 1130.0
    margin_fee = pm.margin_at_price(1850, 720, fee_percent=10)
    assert margin_fee["margin_after_fee_usd"] == 945.0
    example = pm.worked_example()
    assert example["floor_usd"] == 720.0
    assert example["price_usd"] == 1850
    assert example["gross_margin_usd"] == 1130.0
    rows = pm.compare_candidates([1850], 720, 2400)
    assert rows[0]["covers_floor_after_fee"] is True
    print("lesson 14 smoke test passed")


if __name__ == "__main__":
    main()
