#!/usr/bin/env python3
"""Build a monthly retainer report in markdown from an activity log.

The log is JSON: the agreed scope list, incidents, changes shipped,
agent-run maintenance with costs, enquiries handled, and a response
time summary. Any delivered item whose scope tag is outside the
agreed scope list is flagged in the report by name.

Standard library only, offline, no credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def find_out_of_scope(log):
    """Delivered items whose scope tag is not in the agreed list."""
    agreed = set(log.get("agreed_scope", []))
    flagged = []
    for section in ("incidents", "changes", "maintenance"):
        for item in log.get(section, []):
            if item.get("scope") not in agreed:
                flagged.append({
                    "section": section,
                    "title": item.get("title", "untitled item"),
                    "scope": item.get("scope"),
                })
    return flagged


def maintenance_total(log):
    return round(sum(item.get("cost_usd", 0)
                     for item in log.get("maintenance", [])), 2)


def build_report(log):
    flagged = find_out_of_scope(log)
    rt = log.get("response_time_summary", {})
    lines = []
    lines.append(f"# Retainer report: {log.get('client', 'unnamed client')}")
    lines.append(f"Month: {log.get('month', 'unspecified')}")
    lines.append("")
    lines.append("## Outcomes")
    lines.append(f"Enquiries handled: {log.get('enquiries_handled', 0)}")
    lines.append(f"Median first response: {rt.get('median_first_response', 'n/a')}")
    lines.append(f"Share answered within 5 minutes: "
                 f"{rt.get('within_5_min_percent', 'n/a')}%")
    lines.append("")
    lines.append("## Incidents")
    if log.get("incidents"):
        for item in log["incidents"]:
            lines.append(f"- {item.get('title')}: {item.get('resolution', '')}")
    else:
        lines.append("- None this month.")
    lines.append("")
    lines.append("## Changes shipped")
    if log.get("changes"):
        for item in log["changes"]:
            lines.append(f"- {item.get('title')} (scope: {item.get('scope')})")
    else:
        lines.append("- None this month.")
    lines.append("")
    lines.append("## Agent-run maintenance")
    for item in log.get("maintenance", []):
        lines.append(f"- {item.get('title')}: ${item.get('cost_usd', 0):.2f} "
                     f"(scope: {item.get('scope')})")
    lines.append(f"Total measured maintenance cost: "
                 f"${maintenance_total(log):.2f}")
    lines.append("")
    lines.append("## Scope check")
    if flagged:
        lines.append("OUT OF SCOPE items delivered this month:")
        for item in flagged:
            lines.append(f"- {item['title']} (in {item['section']}, "
                         f"tagged {item['scope']})")
        lines.append("These need a conversation: bill them, swap them, "
                     "or agree in writing that the scope has changed.")
    else:
        lines.append("All delivered items fall inside the agreed scope.")
    return "\n".join(lines) + "\n"


def load_log(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "lumen_month_one.json")
    print(build_report(load_log(path)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
