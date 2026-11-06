#!/usr/bin/env python3
"""Smoke test for Lesson 19."""
import package_page as pp


def main():
    packages = pp.load_packages()
    assert len(packages) == 2
    page = pp.render_page(packages)
    assert "Enquiry Response System for Lumen Med Spa" in page
    assert "Not included:" in page
    assert "Support window:" in page
    assert "We do not guarantee bookings" in page
    bad = [{"name": "Vague Package", "outcome": "Better enquiries", "inclusions": ["A chatbot"], "revision_rounds": 1, "delivery_days": 5, "support_window": "7 days"}]
    reasons = pp.validate_packages(bad)
    assert any("exclusion" in r for r in reasons), reasons
    try:
        pp.render_page(bad)
    except ValueError as exc:
        assert "exclusion" in str(exc)
    else:
        raise AssertionError("render must refuse a package missing exclusions")
    print("lesson 19 smoke test passed")


if __name__ == "__main__":
    main()
