#!/usr/bin/env python3
"""Compute the monthly maintenance ledger for a small product.

Costs: hosting (fixed), agent run maintenance (fixed at a stated
run count), and support time (variable with users). The tool
prints its assumptions, monthly cost, gross margin per user, and
the break even user count: fixed costs divided by the contribution
per user (price minus variable support cost per user).
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def compute(profile):
    users = profile["users"]
    price = profile["price_usd_per_user_per_month"]
    tickets = users * profile["tickets_per_100_users_per_month"] / 100.0
    support_minutes = tickets * profile["minutes_per_ticket"]
    support_cost = support_minutes / 60.0 * profile["support_hourly_rate_usd"]
    agent_cost_per_run = (profile["input_tokens_per_run"] * profile["input_price_per_million_usd"] / 1_000_000 + profile["output_tokens_per_run"] * profile["output_price_per_million_usd"] / 1_000_000)
    agent_cost = agent_cost_per_run * profile["agent_runs_per_month"]
    hosting = profile["hosting_usd_per_month"]
    total_cost = hosting + agent_cost + support_cost
    revenue = users * price
    margin_per_user = (revenue - total_cost) / users if users else 0.0
    support_cost_per_user = support_cost / users if users else 0.0
    fixed_cost = hosting + agent_cost
    contribution = price - support_cost_per_user
    if contribution <= 0:
        break_even = None
    else:
        break_even = math.ceil(fixed_cost / contribution)
    return {"tickets_per_month": tickets, "support_minutes": support_minutes, "support_cost": round(support_cost, 2), "agent_cost_per_run": round(agent_cost_per_run, 2), "agent_cost": round(agent_cost, 2), "hosting": hosting, "total_cost": round(total_cost, 2), "revenue": round(revenue, 2), "margin_per_user": round(margin_per_user, 2), "support_cost_per_user": round(support_cost_per_user, 2), "fixed_cost": round(fixed_cost, 2), "contribution_per_user": round(contribution, 2), "break_even_users": break_even}


def load_profile(path=None):
    path = path or os.path.join(HERE, "product_profile.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    profile = load_profile()
    result = compute(profile)
    print("WORKED EXAMPLE: maintenance ledger. Assumptions you can change:")
    print(f"  Product: {profile['product']}")
    print(f"  Users: {profile['users']} at ${profile['price_usd_per_user_per_month']} per user per month")
    print(f"  Support: {profile['tickets_per_100_users_per_month']} tickets per 100 users, {profile['minutes_per_ticket']} minutes each, at ${profile['support_hourly_rate_usd']} per hour")
    print(f"  Hosting: ${profile['hosting_usd_per_month']} per month")
    print(f"  Agent maintenance: {profile['agent_runs_per_month']} runs, {profile['input_tokens_per_run']} input and {profile['output_tokens_per_run']} output tokens per run")
    print(f"  Token prices checked October 2026: ${profile['input_price_per_million_usd']} per million in, ${profile['output_price_per_million_usd']} per million out")
    print()
    print(f"  Tickets per month: {result['tickets_per_month']:.1f}")
    print(f"  Support cost: ${result['support_cost']:.2f}")
    print(f"  Agent maintenance cost: ${result['agent_cost']:.2f}")
    print(f"  Total monthly cost: ${result['total_cost']:.2f}")
    print(f"  Revenue: ${result['revenue']:.2f}")
    print(f"  Gross margin per user: ${result['margin_per_user']:.2f}")
    print(f"  Break even users: {result['break_even_users']}")
    print()
    print("This is a model of one invented product. It is not a forecast for yours.")


if __name__ == "__main__":
    main()
