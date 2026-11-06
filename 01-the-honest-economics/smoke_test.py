#!/usr/bin/env python3
"""Smoke test for Lesson 01: the market math and the data's integrity."""
import market_math as mm


def main():
    assert mm.break_even_hours(100, 50) == 2.0
    assert abs(mm.break_even_hours(20, 35) - 0.5714) < 0.001
    assert mm.net_rate(60, 20) == 48.0
    assert mm.net_rate(60, 0) == 60.0
    numbers = mm.load_numbers()
    assert len(numbers) >= 8
    for key, entry in numbers.items():
        for field in ("figure", "source", "limits"):
            assert entry.get(field), f"{key} missing {field}"
    try:
        mm.break_even_hours(100, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("zero rate must raise")
    print("lesson 01 smoke test passed")


if __name__ == "__main__":
    main()
