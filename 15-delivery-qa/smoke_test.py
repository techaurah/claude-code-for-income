#!/usr/bin/env python3
"""Smoke test for Lesson 15: fixture passes, leaked key fails."""
import os
import shutil
import tempfile

import qa_gate as qa

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "fixture")


def main():
    result = qa.run_gate(FIXTURE)
    assert result["passed"], result
    with tempfile.TemporaryDirectory() as tmp:
        copy_root = os.path.join(tmp, "delivery")
        shutil.copytree(FIXTURE, copy_root)
        with open(os.path.join(copy_root, "notes.txt"), "w", encoding="utf-8") as f:
            f.write('api_key = "sk-1234567890abcdefghij"\n')
        bad = qa.run_gate(copy_root)
        assert not bad["passed"], bad
        secret_check = [c for c in bad["checks"] if c["name"] == "secret_scan"][0]
        assert secret_check["passed"] is False
    print("lesson 15 smoke test passed")


if __name__ == "__main__":
    main()
