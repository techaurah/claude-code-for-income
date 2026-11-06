#!/usr/bin/env python3
"""Render a pricing page from a package definition, with validation.

A package may not render unless it names at least one explicit
exclusion and a support window. Those two fields are what keep a
promise honest: what is not included, and how long help lasts.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def validate_package(pkg):
    reasons = []
    if not pkg.get("name"):
        reasons.append("package has no name")
    if not pkg.get("outcome"):
        reasons.append(f"{pkg.get('name', 'unnamed')}: missing named outcome")
    if not pkg.get("exclusions"):
        reasons.append(f"{pkg.get('name', 'unnamed')}: needs at least one explicit exclusion")
    if not pkg.get("support_window"):
        reasons.append(f"{pkg.get('name', 'unnamed')}: missing support window")
    if not pkg.get("inclusions"):
        reasons.append(f"{pkg.get('name', 'unnamed')}: missing inclusions")
    return reasons


def validate_packages(packages):
    reasons = []
    for pkg in packages:
        reasons.extend(validate_package(pkg))
    return reasons


def render_page(packages):
    reasons = validate_packages(packages)
    if reasons:
        raise ValueError("Refusing to render pricing page: " + "; ".join(reasons))
    lines = ["# Pricing", ""]
    for pkg in packages:
        lines.append(f"## {pkg['name']}")
        lines.append("")
        lines.append(f"Outcome: {pkg['outcome']}")
        lines.append("")
        lines.append(f"Price note: {pkg['price_note']}")
        lines.append("")
        lines.append("Included:")
        for item in pkg["inclusions"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append("Not included:")
        for item in pkg["exclusions"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append(f"Revision rounds: {pkg['revision_rounds']}")
        lines.append(f"Delivery time: {pkg['delivery_days']} days")
        lines.append(f"Support window: {pkg['support_window']}")
        lines.append("")
        lines.append("Guarantee: if we miss the stated delivery time or a delivered item fails its agreed check, we fix it inside the support window at no extra charge. If we cannot fix it, we refund the fee for that package. We do not guarantee bookings, revenue, or any business result, because those depend on factors outside the delivered system.")
        lines.append("")
    return "\n".join(lines)


def load_packages(path=None):
    path = path or os.path.join(HERE, "packages.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)["packages"]


def main():
    print(render_page(load_packages()))


if __name__ == "__main__":
    main()
