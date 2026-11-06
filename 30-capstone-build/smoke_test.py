#!/usr/bin/env python3
"""Smoke test for Lesson 30: the gate refuses failure, accepts the fix."""
import copy

import engagement_sim as sim


def main():
    record = sim.load_json(sim.QA_PATH)
    engagement = sim.load_json(sim.ENGAGEMENT_PATH)
    assert len(record["checks"]) == 11
    raw_fails = [c for c in record["checks"] if c["result"] == "fail"]
    assert len(raw_fails) == 1
    assert raw_fails[0]["id"] == "Q07"
    assert "opt" in raw_fails[0]["name"].lower()
    assert raw_fails[0]["retest"] == "pass"
    ready, failing = sim.gate_status(record)
    assert ready and failing == []
    doctored = copy.deepcopy(record)
    for check in doctored["checks"]:
        if check["id"] == "Q07":
            del check["retest"]
    ready2, failing2 = sim.gate_status(doctored)
    assert not ready2
    assert [c["id"] for c in failing2] == ["Q07"]
    assert "REFUSED" in sim.replay(doctored, engagement)
    ledger = "\n".join(sim.cost_ledger(engagement))
    assert "$1850" in ledger and "$720" in ledger and "$1130" in ledger
    assert "$675" in ledger
    print("lesson 30 smoke test passed")


if __name__ == "__main__":
    main()
