#!/usr/bin/env python3
"""Compare the three routes for paying for Claude Code work.

Routes covered:
1. Subscription plans, priced per month, checked October 2026.
2. API billing per million tokens, by model class.
3. Free third-party tiers reached through a gateway.

The free route is reported as zero cash cost with its caveats
attached. It is never recommended for client work in this tool,
because the terms and capacity limits make it indefensible there.

Standard library only. Offline. No credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

PLANS = {
    "pro": {"label": "Pro", "monthly_usd": 20, "annual_monthly_usd": 17, "api_credit_usd": 0},
    "max-5x": {"label": "Max 5x", "monthly_usd": 100, "annual_monthly_usd": None, "api_credit_usd": 100},
    "max-20x": {"label": "Max 20x", "monthly_usd": 200, "annual_monthly_usd": None, "api_credit_usd": 200},
}

API_PRICES = {
    "sonnet": {"input_per_million": 2.0, "output_per_million": 10.0},
    "opus": {"input_per_million": 4.0, "output_per_million": 20.0},
    "haiku": {"input_per_million": 0.10, "output_per_million": 0.50},
    "fable": {"input_per_million": 10.0, "output_per_million": 50.0},
}


def api_cost(model_class, input_tokens, output_tokens, batch=False):
    """Cost in USD for one headless job at API list prices.

    Prices checked October 2026. Batch API is half price.
    """
    key = model_class.lower()
    if key not in API_PRICES:
        raise ValueError(f"unknown model class: {model_class}")
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("token counts must not be negative")
    prices = API_PRICES[key]
    cost = (input_tokens / 1_000_000 * prices["input_per_million"]
            + output_tokens / 1_000_000 * prices["output_per_million"])
    if batch:
        cost *= 0.5
    return round(cost, 4)


def api_route_cost(jobs):
    """Total API cost for a list of job dicts."""
    total = 0.0
    per_class = {}
    for job in jobs:
        cost = api_cost(job["model"], job.get("input_tokens", 0),
                        job.get("output_tokens", 0), job.get("batch", False))
        total += cost
        per_class[job["model"].lower()] = round(per_class.get(job["model"].lower(), 0.0) + cost, 4)
    return {"total_usd": round(total, 4), "per_model_class": per_class}


def break_even_hours(plan_price_usd, billable_rate_usd):
    """Hours a plan must save per month to pay for itself."""
    if billable_rate_usd <= 0:
        raise ValueError("billable rate must be positive")
    return round(plan_price_usd / billable_rate_usd, 4)


def plan_route_cost(plan_key, api_jobs_cost_usd=0.0):
    """Plan price minus any API credit the plan returns.

    Max plans return their price as monthly API credit, with no
    rollover. Credit can offset headless API spend up to its value.
    It does not reduce cash cost below zero.
    """
    if plan_key not in PLANS:
        raise ValueError(f"unknown plan: {plan_key}")
    plan = PLANS[plan_key]
    credit_used = min(plan["api_credit_usd"], api_jobs_cost_usd)
    return {
        "plan": plan["label"],
        "plan_price_usd": plan["monthly_usd"],
        "api_credit_usd": plan["api_credit_usd"],
        "credit_used_usd": round(credit_used, 4),
        "remaining_api_usd": round(max(0.0, api_jobs_cost_usd - credit_used), 4),
        "total_cash_usd": round(plan["monthly_usd"] + max(0.0, api_jobs_cost_usd - credit_used), 4),
    }


def recommend(profile):
    """Recommend the cheapest defensible route for a usage profile.

    Profile keys:
      interactive_hours: estimated interactive hours per month.
      rate_usd: target billable rate per hour.
      jobs: list of headless job dicts for api_cost.
      client_work: bool. If True, the free route is excluded.
    """
    jobs = profile.get("jobs", [])
    rate = profile.get("rate_usd", 50)
    api = api_route_cost(jobs)
    api_total = api["total_usd"]
    plans = {key: plan_route_cost(key, api_total) for key in PLANS}
    pure_api_total = api_total
    options = []
    for key, result in plans.items():
        options.append({"route": f"plan:{key}", "cash_usd": result["total_cash_usd"]})
    options.append({"route": "api-only", "cash_usd": round(pure_api_total, 4)})
    options.sort(key=lambda item: item["cash_usd"])
    cheapest = options[0]
    if profile.get("client_work", True):
        recommendation = cheapest["route"]
        reason = "Free tiers are excluded for client work: terms, training, and capacity risks."
    else:
        recommendation = cheapest["route"]
        reason = "Cheapest cash route among plan and API options. Free tiers suit only throwaway experiments."
    return {
        "api_route": api,
        "plans": plans,
        "break_even_hours": {key: break_even_hours(item["monthly_usd"], rate) for key, item in PLANS.items()},
        "options_ranked": options,
        "recommendation": recommendation,
        "reason": reason,
        "free_route": {
            "cash_usd": 0,
            "defensible_for_client_work": False,
            "caveats": [
                "Routing Claude Code to other providers free models is off-label use.",
                "Free tiers may train on prompts, so client data must not go there.",
                "Capacity is small and can be withdrawn without notice.",
            ],
        },
    }


def default_profile():
    return {
        "interactive_hours": 30,
        "rate_usd": 75,
        "client_work": True,
        "jobs": [
            {"name": "nightly-summary", "model": "sonnet", "input_tokens": 2_000_000, "output_tokens": 500_000},
            {"name": "triage", "model": "haiku", "input_tokens": 5_000_000, "output_tokens": 1_000_000},
        ],
    }


def main(argv):
    if argv:
        with open(argv[0], encoding="utf-8") as f:
            profile = json.load(f)
    else:
        profile = default_profile()
    result = recommend(profile)
    print(json.dumps(result, indent=2))
    print()
    print("Worked example note: figures above use October 2026 list prices and the profile shown.")
    print(f"Profile: {json.dumps(profile)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
