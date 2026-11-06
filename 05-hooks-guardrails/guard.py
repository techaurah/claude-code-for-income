#!/usr/bin/env python3
"""PreToolUse guard: deny destructive commands and secret reads.

Offline, standard library only. Reads a JSON event on stdin when
run as a script, prints a JSON decision, and exits 2 on a deny so
a hook runner can block the call. The decision logic is in
evaluate(), so tests and the simulator can call it directly.
"""
import json
import re
import sys

DENY_PATTERNS = [
    (r"\brm\s+-[a-z]*r[a-z]*f\b", "recursive forced delete (rm -rf)"),
    (r"\brm\s+-[a-z]*f[a-z]*r\b", "recursive forced delete (rm -fr)"),
    (r"\bgit\s+push\b.*--force", "force push"),
    (r"\bgit\s+push\b.*\s-f(\s|$)", "force push"),
    (r"\bdrop\s+table\b", "drop table"),
    (r"\bdrop\s+database\b", "drop database"),
    (r"(?:^|[\s'\"/])\.env(\b|\.)", "secret file read (.env)"),
    (r"id_rsa|id_ed25519|\.pem\b|credentials\.json", "key or credential file"),
]


def extract_command(event):
    """Pull a command or file path string out of a hook event."""
    if not isinstance(event, dict):
        return ""
    tool_input = event.get("tool_input") or event.get("input") or {}
    if isinstance(tool_input, dict):
        for key in ("command", "file_path", "path"):
            if tool_input.get(key):
                return str(tool_input[key])
    for key in ("command", "file_path", "path"):
        if event.get(key):
            return str(event[key])
    return ""


def evaluate(event):
    """Return {'decision': 'allow'|'deny', 'reason': str} for an event."""
    text = extract_command(event)
    low = text.lower()
    for pattern, label in DENY_PATTERNS:
        if re.search(pattern, low):
            return {"decision": "deny",
                    "reason": f"blocked by guardrail: {label}"}
    return {"decision": "allow", "reason": "no guardrail matched"}


def main():
    raw = sys.stdin.read().strip()
    if not raw:
        print(json.dumps({"decision": "allow",
                          "reason": "empty event, nothing to check"}))
        return 0
    try:
        event = json.loads(raw)
    except json.JSONDecodeError:
        print(json.dumps({"decision": "deny",
                          "reason": "event was not valid JSON"}))
        return 2
    result = evaluate(event)
    output = {
        "decision": result["decision"],
        "reason": result["reason"],
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": result["decision"],
            "permissionDecisionReason": result["reason"],
        },
    }
    print(json.dumps(output))
    return 2 if result["decision"] == "deny" else 0


if __name__ == "__main__":
    sys.exit(main())
