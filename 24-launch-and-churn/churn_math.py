#!/usr/bin/env python3
"""Simulate subscriber and MRR growth under churn, as a model.

Assumptions, stated up front: adds are constant each month, churn
applies to the subscribers present at the start of the month, and
price never changes. Real launches break all three assumptions.
Lifetime in months is 1 divided by the churn rate. LTV here is
price times lifetime, gross before costs, so it overstates what
a subscriber is worth until Lesson 23 costs are subtracted.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def simulate(starting, monthly_adds, churn_rate, price, months=12):
    if not 0 < churn_rate < 1:
        raise ValueError("churn rate must be between 0 and 1, exclusive")
    subscribers = float(starting)
    rows = []
    for month in range(1, months + 1):
        churned = subscribers * churn_rate
        subscribers = subscribers - churned + monthly_adds
        rows.append({"month": month, "subscribers": round(subscribers, 2), "mrr": round(subscribers * price, 2)})
    lifetime = 1.0 / churn_rate
    ltv = price * lifetime
    return {"rows": rows, "lifetime_months": lifetime, "ltv_gross": ltv, "final_subscribers": rows[-1]["subscribers"], "final_mrr": rows[-1]["mrr"]}


def load_scenario(path=None):
    path = path or os.path.join(HERE, "scenario.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    sc = load_scenario()
    churn_rate = sc["churn_percent"] / 100.0
    result = simulate(sc["starting_subscribers"], sc["monthly_adds"], churn_rate, sc["price_usd_per_month"], sc["months"])
    print("MODEL, not a forecast. Assumptions: constant adds, constant churn, constant price.")
    print(f"  Start: {sc['starting_subscribers']} subscribers, adds {sc['monthly_adds']} per month, churn {sc['churn_percent']} percent, price ${sc['price_usd_per_month']}")
    for row in result["rows"]:
        print(f"  Month {row['month']}: {row['subscribers']:.2f} subscribers, MRR ${row['mrr']:.2f}")
    print(f"  Expected lifetime: {result['lifetime_months']:.2f} months (1 / churn)")
    print(f"  LTV, gross before costs: ${result['ltv_gross']:.2f} (price times lifetime)")
    print("Gross means before hosting, support, and agent costs. Lesson 23 is where those come off.")


if __name__ == "__main__":
    main()
