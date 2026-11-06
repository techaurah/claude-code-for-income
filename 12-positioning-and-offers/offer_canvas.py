#!/usr/bin/env python3
"""Render a one page offer from a JSON canvas, or refuse clearly.

Canvas fields: buyer, pain, outcome, system, proof, boundary.
Buyer and outcome carry the offer. If either is vague, the tool
refuses instead of polishing vagueness into copy.

Vague means empty, or under the word minimum:
  buyer: at least 3 words
  outcome: at least 5 words

Standard library only. Offline. No credentials.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

MIN_BUYER_WORDS = 3
MIN_OUTCOME_WORDS = 5
REQUIRED = ("buyer", "pain", "outcome", "system", "proof", "boundary")


def word_count(text):
    return len(str(text or "").split())


def validate(canvas):
    """Return a list of problems. Empty list means the canvas passes."""
    problems = []
    for field in REQUIRED:
        if not str(canvas.get(field, "")).strip():
            problems.append(f"missing or empty field: {field}")
    if word_count(canvas.get("buyer")) < MIN_BUYER_WORDS:
        problems.append(f"buyer is too vague: needs at least {MIN_BUYER_WORDS} words naming who buys")
    if word_count(canvas.get("outcome")) < MIN_OUTCOME_WORDS:
        problems.append(f"outcome is too vague: needs at least {MIN_OUTCOME_WORDS} words naming the result")
    return problems


def outcome_sentence(canvas):
    return (f"For {canvas['buyer']}, {canvas['outcome']} "
            f"by {canvas['system']}, without {canvas['boundary']}.")


def render(canvas):
    problems = validate(canvas)
    if problems:
        raise ValueError("Offer refused: " + "; ".join(problems))
    lines = []
    lines.append("# Offer")
    lines.append("")
    lines.append(f"**For:** {canvas['buyer']}")
    lines.append("")
    lines.append(f"**The pain:** {canvas['pain']}")
    lines.append("")
    lines.append(f"**The outcome:** {canvas['outcome']}")
    lines.append("")
    lines.append(f"**How it works:** {canvas['system']}")
    lines.append("")
    lines.append(f"**Proof:** {canvas['proof']}")
    lines.append("")
    lines.append(f"**Boundary:** {canvas['boundary']}")
    lines.append("")
    lines.append("## The outcome sentence")
    lines.append("")
    lines.append(outcome_sentence(canvas))
    lines.append("")
    return "\n".join(lines)


def load_canvas(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, "lumen_offer.json")
    canvas = load_canvas(path)
    try:
        print(render(canvas))
    except ValueError as exc:
        print(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
