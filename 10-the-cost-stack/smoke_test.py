#!/usr/bin/env python3
"""Smoke test for Lesson 10: API math, plan credit, recommendation."""
import cost_stack as cs


def main():
    assert cs.api_cost("sonnet", 10_000_000, 2_000_000) == 40.0
    assert cs.api_cost("sonnet", 10_000_000, 2_000_000, batch=True) == 20.0
    assert cs.api_cost("haiku", 1_000_000, 1_000_000) == 0.6
    assert cs.api_cost("opus", 1_000_000, 1_000_000) == 24.0
    assert cs.api_cost("fable", 1_000_000, 1_000_000) == 60.0
    assert cs.break_even_hours(100, 50) == 2.0
    assert cs.break_even_hours(20, 50) == 0.4
    plan = cs.plan_route_cost("max-5x", api_jobs_cost_usd=30)
    assert plan["total_cash_usd"] == 100
    assert plan["credit_used_usd"] == 30
    plan2 = cs.plan_route_cost("max-5x", api_jobs_cost_usd=150)
    assert plan2["total_cash_usd"] == 150
    profile = {"interactive_hours": 5, "rate_usd": 50, "client_work": True,
               "jobs": [{"model": "haiku", "input_tokens": 100_000, "output_tokens": 20_000}]}
    result = cs.recommend(profile)
    assert result["recommendation"] == "api-only"
    assert result["free_route"]["defensible_for_client_work"] is False
    heavy = {"interactive_hours": 60, "rate_usd": 75, "client_work": True,
             "jobs": [{"model": "sonnet", "input_tokens": 20_000_000, "output_tokens": 5_000_000}]}
    result2 = cs.recommend(heavy)
    assert result2["api_route"]["total_usd"] == 90.0
    print("lesson 10 smoke test passed")


if __name__ == "__main__":
    main()
