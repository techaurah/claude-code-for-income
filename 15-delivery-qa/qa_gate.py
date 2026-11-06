#!/usr/bin/env python3
"""Run a small delivery QA gate over a folder and report as JSON.

Checks:
1. Required files are present, including a README.
2. Every Python file compiles.
3. No simple secret pattern appears in a text file.

Secret patterns are a first pass, not a guarantee. They catch
the common shapes: provider key prefixes, assigned api key
lines, and private key headers.

Standard library only. Offline. No credentials.
"""
import json
import os
import py_compile
import re
import sys
import tempfile

REQUIRED_FILES = ["README.md", "runbook.md", "handover.md"]
TEXT_SUFFIXES = (".py", ".md", ".txt", ".json", ".cfg", ".toml", ".yaml", ".yml")
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{16,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|secret|password)\s*=\s*[\"'][^\"'\s]{8,}[\"']"),
]
FAKE_MARKERS = ("example", "placeholder", "your-key", "xxxx", "redacted", "fake-key-for-test")


def find_secret_hits(root):
    hits = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            if not name.lower().endswith(TEXT_SUFFIXES):
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8", errors="ignore") as f:
                    text = f.read()
            except OSError:
                continue
            for lineno, line in enumerate(text.splitlines(), start=1):
                lowered = line.lower()
                if any(marker in lowered for marker in FAKE_MARKERS):
                    continue
                for pattern in SECRET_PATTERNS:
                    if pattern.search(line):
                        hits.append({"file": os.path.relpath(path, root), "line": lineno, "pattern": pattern.pattern})
                        break
    return hits


def check_compiles(root):
    failures = []
    checked = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            if not name.endswith(".py"):
                continue
            checked += 1
            path = os.path.join(dirpath, name)
            try:
                with tempfile.TemporaryDirectory() as tmp:
                    py_compile.compile(path, cfile=os.path.join(tmp, "out.pyc"), doraise=True)
            except py_compile.PyCompileError as exc:
                failures.append({"file": os.path.relpath(path, root), "error": str(exc)})
    return checked, failures


def run_gate(root):
    root = os.path.abspath(root)
    missing = [name for name in REQUIRED_FILES if not os.path.isfile(os.path.join(root, name))]
    checked, compile_failures = check_compiles(root)
    secret_hits = find_secret_hits(root)
    checks = [
        {"name": "required_files", "passed": not missing, "missing": missing},
        {"name": "readme_present", "passed": os.path.isfile(os.path.join(root, "README.md"))},
        {"name": "python_compiles", "passed": not compile_failures, "files_checked": checked, "failures": compile_failures},
        {"name": "secret_scan", "passed": not secret_hits, "hits": secret_hits},
    ]
    return {"folder": root, "passed": all(item["passed"] for item in checks), "checks": checks}


def main(argv):
    root = argv[0] if argv else os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixture")
    result = run_gate(root)
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
