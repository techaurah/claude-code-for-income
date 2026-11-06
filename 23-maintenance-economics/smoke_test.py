#!/usr/bin/env python3
"""Smoke test for Lesson 23."""
import math
import maintenance_ledger as ml


def main():
    profile = ml.load_profile()
    result = ml.compute(profile)
    # Independent recomputation of the break even math.
    tickets = 120 * 8 / 100.0
    support_cost = tickets * 18 / 60.0 * 40
    assert abs(result["support_cost"] - round(support_cost, 2)) < 0.01
    agent_per_run = 400000 * 2 / 1_000_000 + 80000 * 10 / 1_000_000
    assert abs(agent_per_run - 1.6) < 1e-9
    fixed = 45 + agent_per_run * 12
    contribution = 15 - support_cost / 120
    expected_be = math.ceil(fixed / contribution)
    assert result["break_even_users"] == expected_be, result
    assert expected_be == 5
    assert result["margin_per_user"] > 0
    print("lesson 23 smoke test passed")


if __name__ == "__main__":
    main()
