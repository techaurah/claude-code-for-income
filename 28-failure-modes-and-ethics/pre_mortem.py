#!/usr/bin/env python3
"""Generate a pre-mortem risk register in markdown from a project JSON.

Seeds the risks from the Lesson 28 catalogue that match the
project shape: client work always seeds the disclosure risk,
shipping code seeds the IP and licence risks, named channels seed
the platform terms risk, and so on. Owner and control fields are
left blank for the practitioner to complete before work starts.

Standard library only, offline, no credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

CATALOGUE = [
    {
        "id": "disclosure",
        "title": "Undisclosed agent work",
        "when": "always",
        "detail": "Client believed the work was manual and learns "
                  "otherwise from a third party.",
        "seed_control": "Disclose the method in the proposal, in one "
                        "plain sentence, before money moves.",
    },
    {
        "id": "ip_contamination",
        "title": "IP contamination in shipped code",
        "when": "ships_code",
        "detail": "Agent output or pasted code carries third party "
                  "work into the client's codebase.",
        "seed_control": "Review output as untrusted code and check "
                        "shipped code for suspicious matches.",
    },
    {
        "id": "licence_violation",
        "title": "Licence violation in a shipped dependency",
        "when": "ships_code",
        "detail": "A dependency added for fit carries licence terms "
                  "the client cannot accept.",
        "seed_control": "Keep a dependency list and check each "
                        "licence before delivery.",
    },
    {
        "id": "platform_terms",
        "title": "Platform terms breach",
        "when": "uses_platforms",
        "detail": "A workflow depends on breaching a marketplace or "
                  "model provider term, risking the account.",
        "seed_control": "Read the terms of each platform relied on "
                        "and refuse work that needs a breach.",
    },
    {
        "id": "sensitive_data",
        "title": "Sensitive data handled without a practice",
        "when": "sensitive_data",
        "detail": "The agent touches personal or health related data "
                  "with no handling, retention, or access practice.",
        "seed_control": "Write the data inventory and retention "
                        "rules before the first live record.",
    },
    {
        "id": "scope_creep",
        "title": "Scope creep disguised as revisions",
        "when": "always",
        "detail": "New work arrives labelled as fixes and silently "
                  "reprices the engagement downward.",
        "seed_control": "Flag out of scope items by name on arrival "
                        "and price them as separate choices.",
    },
    {
        "id": "single_client",
        "title": "Single-client dependence",
        "when": "always",
        "detail": "One client grows past a safe share of income and "
                  "their pause becomes your emergency.",
        "seed_control": "Track client share monthly and treat the "
                        "next client as the main project past a third.",
    },
    {
        "id": "commodity_trap",
        "title": "The commodity trap",
        "when": "always",
        "detail": "The offer drifts toward simple work the market "
                  "is pricing down, per the Lesson 01 data.",
        "seed_control": "Keep the offer at the complex end: "
                        "integration, accountability, evidence.",
    },
]


def _matches(entry, project):
    rule = entry["when"]
    if rule == "always":
        return True
    if rule == "ships_code":
        return any("code" in d or "system" in d or "software" in d
                   for d in project.get("deliverables", []))
    if rule == "uses_platforms":
        return bool(project.get("channels")) or bool(
            project.get("platforms"))
    if rule == "sensitive_data":
        joined = " ".join(project.get("data_touched", [])).lower()
        return any(word in joined for word in
                   ("personal", "health", "contact", "medical", "payment"))
    return False


def seed_risks(project):
    return [entry for entry in CATALOGUE if _matches(entry, project)]


def build_register(project):
    risks = seed_risks(project)
    lines = []
    lines.append(f"# Pre-mortem risk register: "
                 f"{project.get('project', 'unnamed project')}")
    lines.append(f"Client type: {project.get('client_type', 'unspecified')}")
    lines.append(f"Risks seeded: {len(risks)} of {len(CATALOGUE)} "
                 f"in the Lesson 28 catalogue")
    lines.append("")
    for entry in risks:
        lines.append(f"## {entry['title']}")
        lines.append(f"Failure shape: {entry['detail']}")
        lines.append(f"Seed control: {entry['seed_control']}")
        lines.append("Owner: (complete before work starts)")
        lines.append("Control in place: (complete before work starts)")
        lines.append("")
    return "\n".join(lines)


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "project_example.json")
    with open(path, encoding="utf-8") as f:
        project = json.load(f)
    print(build_register(project))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
