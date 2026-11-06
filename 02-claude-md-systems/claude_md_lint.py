#!/usr/bin/env python3
"""Lint a CLAUDE.md file for size and missing recommended sections.

Offline, standard library only. Reports word count, warns when the
file is over a word budget, and flags missing sections among the
recommended set: commands, conventions, boundaries.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_BUDGET_WORDS = 400
RECOMMENDED_SECTIONS = ("commands", "conventions", "boundaries")


def word_count(text):
    return len(text.split())


def missing_sections(text):
    low = text.lower()
    return [name for name in RECOMMENDED_SECTIONS if name not in low]


def lint_text(text, budget=DEFAULT_BUDGET_WORDS):
    words = word_count(text)
    return {
        "words": words,
        "budget": budget,
        "over_budget": words > budget,
        "missing": missing_sections(text),
    }


def lint_file(path, budget=DEFAULT_BUDGET_WORDS):
    with open(path, encoding="utf-8") as f:
        return lint_text(f.read(), budget=budget)


def report(path, budget=DEFAULT_BUDGET_WORDS):
    result = lint_file(path, budget=budget)
    print(f"{path}: {result['words']} words (budget {result['budget']})")
    if result["over_budget"]:
        print("  WARN over budget: prune or move detail to docs")
    else:
        print("  size ok")
    if result["missing"]:
        print(f"  missing recommended sections: {', '.join(result['missing'])}")
    else:
        print("  all recommended sections present")
    return result


def main(argv):
    paths = argv or [
        os.path.join(HERE, "examples", "CLAUDE.md"),
        os.path.join(HERE, "examples", "api", "CLAUDE.md"),
    ]
    for path in paths:
        report(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
