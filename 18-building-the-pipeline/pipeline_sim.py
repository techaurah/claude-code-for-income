#!/usr/bin/env python3
"""Simulate a productized fulfilment pipeline, deterministically.

Stages in order: intake, scope_check, build, qa, delivery, support.
One order fails the QA gate once, returns to build, and passes on
the second attempt. Human minutes are counted per stage so the
lesson can price the human part honestly. Offline only.
"""
STAGES = ("intake", "scope_check", "build", "qa", "delivery", "support")
HUMAN_MINUTES = {"intake": 5, "scope_check": 15, "build": 20, "qa": 25, "delivery": 10, "support": 15}
QA_FAIL_ORDERS = {"ORD-2"}


def simulate(order_ids=("ORD-1", "ORD-2", "ORD-3")):
    log = []
    orders = {}
    for oid in order_ids:
        minutes = 0
        qa_attempts = 0
        for stage in STAGES:
            if stage == "qa":
                qa_attempts += 1
                log.append((oid, "qa", qa_attempts))
                minutes += HUMAN_MINUTES["qa"]
                if oid in QA_FAIL_ORDERS and qa_attempts == 1:
                    log.append((oid, "qa_failed", qa_attempts))
                    log.append((oid, "build", 2))
                    minutes += HUMAN_MINUTES["build"]
                    qa_attempts += 1
                    log.append((oid, "qa", qa_attempts))
                    minutes += HUMAN_MINUTES["qa"]
                    log.append((oid, "qa_passed", qa_attempts))
                else:
                    log.append((oid, "qa_passed", qa_attempts))
            else:
                log.append((oid, stage, 1))
                minutes += HUMAN_MINUTES[stage]
        orders[oid] = {"human_minutes": minutes, "qa_attempts": qa_attempts}
    total = sum(o["human_minutes"] for o in orders.values())
    return {"log": log, "orders": orders, "total_human_minutes": total}


def stage_sequence(log, order_id):
    seen = []
    for oid, stage, _attempt in log:
        if oid == order_id and stage in STAGES and stage not in seen:
            seen.append(stage)
    return seen


def main():
    result = simulate()
    for oid, info in result["orders"].items():
        print(f"{oid}: {info['human_minutes']} human minutes, QA attempts: {info['qa_attempts']}")
    print(f"Total human minutes for {len(result['orders'])} orders: {result['total_human_minutes']}")
    print("ORD-2 bounced at QA once, returned to build, then passed.")
    print("That bounce is planned capacity, not a surprise, once you log it.")


if __name__ == "__main__":
    main()
