#!/usr/bin/env python3
"""Generate the Claude Code for Income diagram set as clean, branded SVGs.

Style: white canvas, navy (#0B1F4A) primary boxes with white text,
light blue (#E0F2FE) secondary boxes with navy text, cyan (#0891B2)
arrows, amber (#F59E0B) accent for warnings and human gates. Every
number on a chart is a public list price checked October 2026 or a
worked example labelled as one, per the course's honesty rules.
Run: python3 generate_visuals.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
NAVY = "#0B1F4A"
LIGHT = "#E0F2FE"
CYAN = "#0891B2"
AMBER = "#F59E0B"
GREY = "#475569"
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class SVG:
    def __init__(self, w, h, title, subtitle):
        self.w, self.h = w, h
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
            f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>',
            f'<text x="40" y="52" font-family="{FONT}" font-size="30" font-weight="700" fill="{NAVY}">{esc(title)}</text>',
            f'<text x="40" y="82" font-family="{FONT}" font-size="17" fill="{GREY}">{esc(subtitle)}</text>',
            f'<rect x="40" y="98" width="90" height="5" fill="{CYAN}"/>',
        ]

    def box(self, x, y, w, h, text, fill=NAVY, color="#FFFFFF", size=16, bold=False):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"/>')
        weight = "700" if bold else "400"
        lines = text.split("\n")
        for i, line in enumerate(lines):
            ly = y + h / 2 + (i - (len(lines) - 1) / 2) * (size + 4) + size * 0.35
            self.parts.append(f'<text x="{x + w / 2}" y="{ly:.0f}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="middle">{esc(line)}</text>')

    def arrow(self, x1, y1, x2, y2, color=CYAN):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3"/>')
        self.parts.append(f'<polygon points="{x2},{y2} {x2 - 10},{y2 - 6} {x2 - 10},{y2 + 6}" fill="{color}"/>')

    def arrow_down(self, x, y1, y2, color=CYAN):
        self.parts.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="3"/>')
        self.parts.append(f'<polygon points="{x},{y2} {x - 6},{y2 - 10} {x + 6},{y2 - 10}" fill="{color}"/>')

    def label(self, x, y, text, size=15, color=GREY, anchor="start"):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{esc(text)}</text>')

    def bar(self, x, y, w, h, frac, color=CYAN):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#E2E8F0"/>')
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w * frac:.0f}" height="{h}" fill="{color}"/>')

    def save(self, name):
        self.parts.append("</svg>")
        with open(os.path.join(OUT, name), "w") as f:
            f.write("\n".join(self.parts))
        print("wrote", name)


def course_map():
    s = SVG(1180, 560, "Claude Code for Income: the course map",
            "Ten modules: the workstation, the workflows, the cost stack, four income tracks, and one full engagement.")
    mods = [("0 Foundations", "00-01"), ("1 Workstation", "02-05"),
            ("2 Production", "06-09"), ("3 Cost", "10-11"),
            ("4 Freelance", "12-16"), ("5 Productized", "17-20"),
            ("6 Micro-SaaS", "21-24"), ("7 Consulting", "25-27"),
            ("8 Risk", "28"), ("9 Capstone", "29-31")]
    for i, (name, rng) in enumerate(mods):
        x = 40 + (i % 5) * 224
        y = 150 + (i // 5) * 170
        s.box(x, y, 190, 110, f"{name}\nLessons {rng}", fill=NAVY if i in (0, 9) else LIGHT,
              color="#FFFFFF" if i in (0, 9) else NAVY, bold=True)
        if i % 5 != 4:
            s.arrow(x + 192, y + 55, x + 220, y + 55)
    s.label(40, 520, "Modules 1 to 3 make the work fast and cheap to run. Modules 4 to 7 make it sellable. Nothing here promises an income.", size=16)
    s.save("course-map.svg")


def workstation_stack():
    s = SVG(1180, 700, "The professional workstation: five layers",
            "Each layer is an asset you build once and reuse on every engagement (Lessons 02 to 06).")
    layers = [
        ("YOU: judgement, review, client trust", AMBER, NAVY),
        ("CLAUDE.md: layered memory, project to directory", NAVY, "#FFFFFF"),
        ("Skills: packaged expertise, invoked on demand", LIGHT, NAVY),
        ("Subagents: specialists with their own context", LIGHT, NAVY),
        ("Hooks: guardrails on every tool call", AMBER, NAVY),
        ("MCP servers: the client's systems, as tools", NAVY, "#FFFFFF"),
    ]
    y = 140
    for text, fill, color in layers:
        s.box(240, y, 700, 62, text, fill=fill, color=color, bold=True, size=17)
        if y > 140:
            s.arrow_down(590, y - 18, y - 2)
        y += 86
    s.label(240, 672, "Amber layers are where the human stays in charge: your judgement on top, hook gates underneath.", size=16)
    s.save("workstation-stack.svg")


def unattended_modes():
    s = SVG(1180, 480, "Four ways to run Claude Code unattended",
            "Pick by trigger and supervision, not by fashion (Lesson 08). All four bill against the same plan or API account.")
    modes = [
        ("Background agents", "Agent View\nYou start it, it works\nwhile you do other work"),
        ("Headless mode", "claude -p\nScripts, cron, CI\nCaps: turns and budget"),
        ("In-session loop", "/loop\nRepeats a prompt\ninside an open session"),
        ("Cloud scheduled", "Scheduled tasks\nFire on time, API call,\nor GitHub event"),
    ]
    for i, (name, body) in enumerate(modes):
        x = 40 + i * 282
        s.box(x, 150, 250, 64, name, fill=NAVY, bold=True, size=17)
        s.box(x, 226, 250, 120, body, fill=LIGHT, color=NAVY, size=16)
    s.label(40, 400, "The GitHub Action is headless mode with a repository trigger: same discipline, different door.", size=16)
    s.label(40, 432, "Every unattended run needs the Lesson 05 gates first: allowlists, budgets, and a human review point.", size=16)
    s.save("unattended-modes.svg")


def cost_stack():
    s = SVG(1180, 520, "The cost stack: three ways to pay for the same agent",
            "US list prices checked October 2026. Break-even hours = monthly price divided by your billable rate.")
    rows = [
        ("Pro, $20/mo", 0.10, "Side projects, first clients"),
        ("Max 5x, $100/mo", 0.50, "Daily client work, one practice"),
        ("Max 20x, $200/mo", 1.00, "Heavy parallel and headless volume"),
    ]
    y = 160
    for name, frac, note in rows:
        s.label(40, y + 22, name, size=17, color=NAVY)
        s.bar(330, y, 420, 26, frac)
        s.label(770, y + 22, note, size=16)
        y += 64
    s.label(40, y + 10, "API route, per million tokens in/out: Sonnet class $2/$10, Opus class $4/$20, Haiku class $0.10/$0.50. Batch work: half price.", size=16)
    s.label(40, y + 42, "Worked example: a $100 plan at a $50 rate breaks even at 2 saved hours a month. Below that, the plan is a hobby cost.", size=16)
    s.label(40, y + 74, "Max plans also return their price as monthly API credit. Free third-party tiers exist, with terms caveats (Lesson 10).", size=16)
    s.save("cost-stack.svg")


def income_tracks():
    s = SVG(1180, 520, "The four income tracks",
            "Same workstation, four ways to package it (Modules 4 to 7). Cycle = typical time from first contact to paid work starting.")
    tracks = [
        ("Freelance and\nagency delivery", "Sell: scoped projects\nBuyer: one client\nCycle: days to weeks"),
        ("Productized\nservices", "Sell: a fixed package\nBuyer: many, same offer\nCycle: days"),
        ("Indie products\nand micro-SaaS", "Sell: subscriptions\nBuyer: a market\nCycle: weeks to months"),
        ("Automation\nconsulting", "Sell: audits, retainers\nBuyer: a business\nCycle: weeks"),
    ]
    for i, (name, body) in enumerate(tracks):
        x = 40 + i * 282
        s.box(x, 150, 250, 84, name, fill=NAVY if i in (0, 3) else LIGHT,
              color="#FFFFFF" if i in (0, 3) else NAVY, bold=True, size=17)
        s.box(x, 246, 250, 120, body, fill="#FFFFFF", color=NAVY, size=15)
    s.label(40, 420, "Most durable practices stack two: delivery income funds the product, the audit feeds the retainer.", size=16)
    s.label(40, 452, "Demand context with sources and limits: Lesson 01. Nothing in this diagram is an earnings figure.", size=16)
    s.save("income-tracks.svg")


def delivery_pipeline():
    s = SVG(1180, 420, "The delivery pipeline: how paid work flows",
            "Module 4's spine. The amber step is the one that protects your rate: nothing reaches the client ungated.")
    steps = [("Discovery", NAVY), ("Scope and\nestimate", LIGHT), ("Fixed price", LIGHT),
             ("Build with\nthe stack", LIGHT), ("QA GATE", AMBER), ("Handover", NAVY)]
    for i, (name, fill) in enumerate(steps):
        x = 40 + i * 188
        color = "#FFFFFF" if fill == NAVY else NAVY
        s.box(x, 160, 160, 96, name, fill=fill, color=color, bold=True, size=16)
        if i < len(steps) - 1:
            s.arrow(x + 162, 208, x + 184, 208)
    s.label(40, 320, "Support and rehire (Lesson 16) loop back from Handover: the cheapest client is the one who already trusts you.", size=16)
    s.label(40, 352, "Every stage has an artifact in this course: notes, estimate, price model, QA record, delivery pack.", size=16)
    s.save("delivery-pipeline.svg")


def capstone_flow():
    s = SVG(1180, 560, "The capstone: one engagement, end to end",
            "Lumen Med Spa (fictional): an enquiry-response system, priced at $1,850 fixed in a worked example.")
    steps = [
        ("Brief and discovery", "The client's words, their numbers"),
        ("Scope and estimate", "Estimator output, assumptions printed"),
        ("Build with the stack", "Skills, subagents, hooks, headless runs"),
        ("QA gate", "Recorded checks, failures included"),
        ("Delivery pack", "Handover, runbook, support terms"),
        ("Self-grading rubric", "Score yourself before the solution"),
    ]
    y = 140
    for i, (name, note) in enumerate(steps):
        fill = AMBER if i in (3, 5) else (NAVY if i in (0, 4) else LIGHT)
        color = "#FFFFFF" if fill == NAVY else NAVY
        s.box(240, y, 340, 52, name, fill=fill, color=color, bold=True, size=16)
        s.label(610, y + 32, note, size=16)
        if i < len(steps) - 1:
            s.arrow_down(410, y + 54, y + 66)
        y += 68
    s.save("capstone-flow.svg")


if __name__ == "__main__":
    course_map()
    workstation_stack()
    unattended_modes()
    cost_stack()
    income_tracks()
    delivery_pipeline()
    capstone_flow()
