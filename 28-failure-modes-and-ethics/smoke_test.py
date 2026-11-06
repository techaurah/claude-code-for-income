#!/usr/bin/env python3
"""Smoke test for Lesson 28: register seeding matches project shape."""
import json
import os

import pre_mortem as pm

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "project_example.json"),
              encoding="utf-8") as f:
        project = json.load(f)
    register = pm.build_register(project)
    assert "Undisclosed agent work" in register
    assert "IP contamination in shipped code" in register
    assert "Licence violation" in register
    assert "Platform terms breach" in register
    assert "Owner:" in register
    ids = {entry["id"] for entry in pm.seed_risks(project)}
    assert ids == {entry["id"] for entry in pm.CATALOGUE}
    minimal = {"project": "Advice only memo", "client_type": "solo buyer",
               "channels": [], "data_touched": [],
               "deliverables": ["written memo"]}
    small = pm.build_register(minimal)
    assert "Undisclosed agent work" in small
    assert "IP contamination" not in small
    assert "Platform terms" not in small
    print("lesson 28 smoke test passed")


if __name__ == "__main__":
    main()
