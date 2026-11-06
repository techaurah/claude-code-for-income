#!/usr/bin/env python3
"""Smoke test for Lesson 16: generation and missing sections."""
import os

import handover_pack as hp

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    record = hp.load_record(os.path.join(HERE, "lumen_record.json"))
    text, missing = hp.generate(record)
    assert missing == []
    assert hp.is_complete(record)
    assert "## How to run it" in text
    assert "## The next problem" in text
    assert "Lumen Med Spa" in text
    incomplete = {"project": "Small build", "client": "Example client", "deliverables": ["One script"]}
    text2, missing2 = hp.generate(incomplete)
    assert "run_instructions" in missing2
    assert "support_terms" in missing2
    assert "next_problem" in missing2
    assert "Incomplete" in text2
    print("lesson 16 smoke test passed")


if __name__ == "__main__":
    main()
