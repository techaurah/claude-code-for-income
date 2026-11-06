#!/usr/bin/env python3
"""Price work from a floor, a fee, and a value anchor.

Floor: human time at your target rate, plus plan share, plus
measured API cost. Nothing below the floor is a discount. It
is a loss with better marketing.

Fee adjusted floor: the price you must charge on a fee taking
channel so that, after the fee, you still cover the floor.

Value anchor: the cost the client named in discovery for the
problem staying unsolved. It is their number, not yours.

Standard library only. Offline. No credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def cost_floor(human_hours, rate_usd, plan_share_usd, api_cost_usd):
    return round(human_hours * rate_usd + plan_share_usd + api_cost_usd, 2)


def effective_received(price_usd, fee_percent):
    return round(price_usd * (1 - fee_percent / 100.0), 2)


def fee_adjusted_floor(floor_usd, fee_percent):
    if fee_percent >= 100:
        raise ValueError("fee percent must be under 100")
    return round(floor_usd / (1 - fee_percent / 100.0), 2)


def margin_at_price(price_usd, floor_usd, fee_percent=0):
    received = effective_received(price_usd, fee_percent)
    return {
        "price_usd": round(price_usd, 2),
        "fee_percent": fee_percent,
        "effective_received_usd": received,
        "gross_margin_usd": round(price_usd - floor_usd, 2),
        "margin_after_fee_usd": round(received - floor_usd, 2),
    }


def compare_candidates(candidates, floor_usd, anchor_usd, fee_percent=0):
    rows = []
    for price in candidates:
        row = margin_at_price(price, floor_usd, fee_percent)
        row["price_as_share_of_anchor"] = round(price / anchor_usd, 4) if anchor_usd else None
        row["covers_floor_after_fee"] = row["margin_after_fee_usd"] >= 0
        rows.append(row)
    return rows


def worked_example():
    """The shared worked example from Lessons 13 and 14."""
    floor = cost_floor(human_hours=9, rate_usd=75, plan_share_usd=25, api_cost_usd=20)
    return {
        "label": "WORKED EXAMPLE: Lumen Med Spa enquiry response build, fictional client",
        "assumptions": {
            "human_hours": 9,
            "rate_usd": 75,
            "plan_share_usd": 25,
            "api_cost_usd": 20,
            "anchor_usd_per_month": 2400,
            "anchor_source": "Client stated cost of slow replies in discovery, their number, as framed in the worked example",
        },
        "floor_usd": floor,
        "price_usd": 1850,
        "gross_margin_usd": round(1850 - floor, 2),
        "at_10_percent_fee": margin_at_price(1850, floor, 10),
        "fee_adjusted_floor_at_10_percent": fee_adjusted_floor(floor, 10),
        "candidates": compare_candidates([1200, 1850, 2400], floor, 2400, fee_percent=0),
    }


def main(argv):
    if argv:
        with open(argv[0], encoding="utf-8") as f:
            data = json.load(f)
        floor = cost_floor(data["human_hours"], data["rate_usd"], data["plan_share_usd"], data["api_cost_usd"])
        result = {
            "floor_usd": floor,
            "margin": margin_at_price(data["price_usd"], floor, data.get("fee_percent", 0)),
            "fee_adjusted_floor_usd": fee_adjusted_floor(floor, data.get("fee_percent", 0)),
        }
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(worked_example(), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
