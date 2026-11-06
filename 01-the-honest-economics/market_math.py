#!/usr/bin/env python3
"""The three calculations Lesson 01 runs on the sourced platform data.

1. Break-even hours: what a plan must save monthly to pay for itself.
2. Net rate after a platform fee: the rate that actually reaches you.
3. The complexity contrast: why this course teaches the complex end.

All inputs are either the reader's own numbers or the sourced
figures in platform_numbers.json, printed with their limits by the
report at the bottom. Nothing here predicts an individual's income.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def break_even_hours(plan_price_usd, billable_rate_usd):
    """Hours a tool must save per month for its price to pay for itself."""
    if billable_rate_usd <= 0:
        raise ValueError("billable rate must be positive")
    return plan_price_usd / billable_rate_usd


def net_rate(gross_rate_usd, fee_percent):
    """The rate that reaches you after a marketplace takes its cut."""
    return gross_rate_usd * (1 - fee_percent / 100.0)


def load_numbers():
    with open(os.path.join(HERE, "platform_numbers.json"),
              encoding="utf-8") as f:
        return {k: v for k, v in json.load(f).items()
                if not k.startswith("_")}


def report():
    print("Break-even worked examples (change the inputs, keep the method):")
    for plan, price in (("Pro", 20), ("Max 5x", 100), ("Max 20x", 200)):
        for rate in (35, 50, 75):
            hours = break_even_hours(price, rate)
            print(f"  {plan} at ${price}/mo, rate ${rate}/h: "
                  f"{hours:.2f} saved hours/month to break even")
    print()
    print("Net rate worked example: $60/h gross on a 10% fee channel "
          f"nets ${net_rate(60, 10):.0f}/h; on a 20% channel, "
          f"${net_rate(60, 20):.0f}/h.")
    print()
    print("The sourced demand picture (each figure with its limits):")
    for key, entry in load_numbers().items():
        print(f"  {key}: {entry['figure']}")
        print(f"    source: {entry['source']}")
        print(f"    limits: {entry['limits']}")


if __name__ == "__main__":
    report()
