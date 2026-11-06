#!/usr/bin/env python3
"""Smoke test for Lesson 02: lint findings on the shipped examples."""
import os

import claude_md_lint as lint

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    assert lint.word_count("one two  three") == 3
    assert lint.missing_sections("# Commands\n# Conventions\n# Boundaries") == []
    project = lint.lint_file(os.path.join(HERE, "examples", "CLAUDE.md"))
    assert project["missing"] == [], project
    assert not project["over_budget"], project
    assert project["words"] > 50, project
    directory = lint.lint_file(os.path.join(HERE, "examples", "api", "CLAUDE.md"))
    assert "commands" in directory["missing"] or directory["missing"], directory
    over = lint.lint_text("word " * 500)
    assert over["over_budget"] and over["words"] == 500
    print("lesson 02 smoke test passed")


if __name__ == "__main__":
    main()
