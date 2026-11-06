#!/usr/bin/env python3
"""Tiny demo app for the fixture delivery."""


def reply(enquiry):
    if not enquiry.strip():
        return "Please tell us what you would like to book."
    return "Thanks for your enquiry. We can help with that."


if __name__ == "__main__":
    print(reply("Hello"))
