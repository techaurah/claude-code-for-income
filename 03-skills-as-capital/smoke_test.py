#!/usr/bin/env python3
"""Smoke test for Lesson 03: audit passes the shipped skill, catches a broken one."""
import os
import tempfile

import skill_audit as audit

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    shipped = audit.audit_file(
        os.path.join(HERE, "skills", "qa-checklist", "SKILL.md"))
    assert shipped["ok"], shipped
    assert shipped["fields"]["name"] == "qa-checklist"
    inv = audit.inventory(os.path.join(HERE, "skills"))
    assert len(inv) == 1 and inv[0]["ok"], inv
    broken = "---\nname: broken-one\n---\n\n# Broken\n\nNo description.\n"
    result = audit.audit_text(broken)
    assert not result["ok"]
    assert "missing description" in result["problems"], result
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "SKILL.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(broken)
        assert not audit.audit_file(path)["ok"]
    short = "---\nname: x\ndescription: QA helper\n---\n"
    assert not audit.audit_text(short)["ok"]
    print("lesson 03 smoke test passed")


if __name__ == "__main__":
    main()
