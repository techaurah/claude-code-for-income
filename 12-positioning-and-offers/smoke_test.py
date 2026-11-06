#!/usr/bin/env python3
"""Smoke test for Lesson 12: rendering and the refusal."""
import os

import offer_canvas as oc

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    canvas = oc.load_canvas(os.path.join(HERE, "lumen_offer.json"))
    text = oc.render(canvas)
    assert "owners of multi location med spas" in text
    assert "every enquiry answered within one minute" in text
    assert "## The outcome sentence" in text
    vague = dict(canvas)
    vague["buyer"] = "businesses"
    try:
        oc.render(vague)
    except ValueError as exc:
        assert "buyer is too vague" in str(exc)
    else:
        raise AssertionError("vague buyer must be refused")
    empty = dict(canvas)
    empty["outcome"] = ""
    try:
        oc.render(empty)
    except ValueError as exc:
        assert "outcome" in str(exc)
    else:
        raise AssertionError("empty outcome must be refused")
    print("lesson 12 smoke test passed")


if __name__ == "__main__":
    main()
