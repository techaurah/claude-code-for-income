#!/usr/bin/env python3
"""Smoke test for Lesson 00: the checker logic, offline."""
import check_environment as env


def main():
    assert env.python_ok((3, 11, 0))
    assert env.python_ok((3, 12, 1))
    assert not env.python_ok((3, 10, 9))
    assert env.lesson_count() == env.EXPECTED_LESSONS
    ok, lines = env.report()
    assert ok, lines
    assert env.BASELINE_TEMPLATE["plan_price_usd_per_month"] == 100
    print("lesson 00 smoke test passed")


if __name__ == "__main__":
    main()
