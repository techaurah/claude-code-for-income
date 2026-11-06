#!/usr/bin/env python3
"""Generate a handover document from a JSON project record.

Record fields: project, client, deliverables, run_instructions,
change_guide, support_terms, next_problem.

The completeness check lists every required section that is
missing or empty, so a thin pack fails loudly before it ships.

Standard library only. Offline. No credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

REQUIRED_SECTIONS = ["deliverables", "run_instructions", "change_guide", "support_terms", "next_problem"]


def missing_sections(record):
    missing = []
    for section in REQUIRED_SECTIONS:
        value = record.get(section)
        if value is None:
            missing.append(section)
        elif isinstance(value, list) and len(value) == 0:
            missing.append(section)
        elif isinstance(value, str) and not value.strip():
            missing.append(section)
    if not str(record.get("project", "")).strip():
        missing.append("project")
    if not str(record.get("client", "")).strip():
        missing.append("client")
    return missing


def is_complete(record):
    return not missing_sections(record)


def generate(record):
    missing = missing_sections(record)
    lines = []
    lines.append(f"# Handover: {record.get('project', 'Untitled project')}")
    lines.append("")
    lines.append(f"**Client:** {record.get('client', '')}")
    lines.append("")
    lines.append("## What was built")
    lines.append("")
    deliverables = record.get("deliverables") or []
    if deliverables:
        for item in deliverables:
            lines.append(f"- {item}")
    else:
        lines.append("Missing: deliverables")
    lines.append("")
    lines.append("## How to run it")
    lines.append("")
    lines.append(str(record.get("run_instructions") or "Missing: run instructions"))
    lines.append("")
    lines.append("## How to change it")
    lines.append("")
    lines.append(str(record.get("change_guide") or "Missing: change guide"))
    lines.append("")
    lines.append("## Support terms")
    lines.append("")
    lines.append(str(record.get("support_terms") or "Missing: support terms"))
    lines.append("")
    lines.append("## The next problem")
    lines.append("")
    lines.append(str(record.get("next_problem") or "Missing: next problem"))
    lines.append("")
    lines.append("## Completeness check")
    lines.append("")
    if missing:
        lines.append(f"Incomplete. Missing sections: {', '.join(missing)}")
    else:
        lines.append("Complete. All required sections are present.")
    lines.append("")
    return "\n".join(lines), missing


def load_record(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "lumen_record.json")
    record = load_record(path)
    text, missing = generate(record)
    print(text)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
