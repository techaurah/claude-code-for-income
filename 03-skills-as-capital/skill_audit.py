#!/usr/bin/env python3
"""Audit SKILL.md files: frontmatter health and library inventory.

Offline, standard library only. A skill passes when its frontmatter
has a name and a description, the description is a usable length,
and it contains at least one trigger verb.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TRIGGER_VERBS = ("use when", "use", "check", "review", "verify",
                 "audit", "run", "create", "generate")
MIN_DESCRIPTION = 40
MAX_DESCRIPTION = 400


def parse_frontmatter(text):
    """Return the frontmatter dict, or an empty dict if absent."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fields = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def audit_text(text):
    fields = parse_frontmatter(text)
    problems = []
    if not fields:
        problems.append("missing frontmatter")
        return {"ok": False, "problems": problems, "fields": fields}
    if not fields.get("name"):
        problems.append("missing name")
    desc = fields.get("description", "")
    if not desc:
        problems.append("missing description")
    else:
        if len(desc) < MIN_DESCRIPTION:
            problems.append("description too short")
        if len(desc) > MAX_DESCRIPTION:
            problems.append("description too long")
        low = desc.lower()
        if not any(verb in low for verb in TRIGGER_VERBS):
            problems.append("description has no trigger verb")
    return {"ok": not problems, "problems": problems, "fields": fields}


def audit_file(path):
    with open(path, encoding="utf-8") as f:
        result = audit_text(f.read())
    result["path"] = path
    return result


def inventory(folder):
    """List every SKILL.md under folder, with its audit result."""
    found = []
    for dirpath, _dirs, files in os.walk(folder):
        if "SKILL.md" in files:
            found.append(audit_file(os.path.join(dirpath, "SKILL.md")))
    return sorted(found, key=lambda r: r["path"])


def main(argv):
    target = argv[0] if argv else os.path.join(HERE, "skills")
    if os.path.isdir(target):
        results = inventory(target)
    else:
        results = [audit_file(target)]
    for r in results:
        status = "ok" if r["ok"] else "FAIL: " + "; ".join(r["problems"])
        name = r["fields"].get("name", "?")
        print(f"{name}: {status} ({r['path']})")
    print(f"{len(results)} skill(s) audited")
    return 0 if all(r["ok"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
