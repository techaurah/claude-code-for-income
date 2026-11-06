#!/usr/bin/env python3
"""Smoke test for Lesson 26: the report renders, the flag fires."""
import copy
import json
import os

import retainer_report as rr

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "lumen_month_one.json"),
              encoding="utf-8") as f:
        log = json.load(f)
    report = rr.build_report(log)
    assert "Lumen Med Spa (fictional)" in report
    assert "Enquiries handled: 212" in report
    assert "All delivered items fall inside the agreed scope." in report
    assert rr.find_out_of_scope(log) == []
    assert rr.maintenance_total(log) == 13.5
    doctored = copy.deepcopy(log)
    doctored["changes"].append(
        {"title": "Ad campaign copy drafted", "scope": "advertising"})
    flagged = rr.find_out_of_scope(doctored)
    assert len(flagged) == 1
    assert flagged[0]["title"] == "Ad campaign copy drafted"
    assert "OUT OF SCOPE" in rr.build_report(doctored)
    print("lesson 26 smoke test passed")


if __name__ == "__main__":
    main()
