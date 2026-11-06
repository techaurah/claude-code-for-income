# Course design: Claude Code for Income

The design this repository was built to. Research behind it:
[RESEARCH.md](RESEARCH.md). House standard inherited from the
TechAurah free courses programme: numbered lesson folders, every
lesson a complete unit (written lesson, runnable artifact,
exercise, worked solution), an offline path in every lesson, no
em dashes, no invented statistics, no certificates. This course
adds one rule of its own, from the order that created it: no
income promises, anywhere, ever. Every money figure is either
sourced platform data with its limits stated, public list pricing
checked at writing time, or a worked example with its assumptions
printed next to it.

## Title and promise

**Claude Code for Income** is a free, advanced course that teaches
experienced developers to run Claude Code like a business asset:
the power workflows (CLAUDE.md systems, skills, subagents, hooks,
MCP, headless and scheduled automation, cost engineering) and the
four income tracks built on them (freelance and agency delivery,
productized services, indie products and micro-SaaS, automation
consulting), with real cost math and the failure modes taught as
plainly as the wins.

The promise is a system, not a number. The course never states or
implies what a student will earn.

## Audience

- Developers who already use Claude Code (or a comparable agent)
  on real work and can read and review production code unaided.
- Freelancers, agency operators, and indie builders who want the
  delivery, pricing, and packaging system around the tool.
- Consultants selling automation to small and mid-sized
  businesses.

Not for: beginners (the prerequisites are real and Lesson 00
checks them), anyone looking for a certificate, or anyone looking
for a promise. The README says all three plainly.

## Prerequisites

- Working developer skill: you ship and maintain real software,
  read diffs critically, and run a terminal without fear.
- Claude Code installed and used on at least one real project,
  on any paid plan or API account. Several lessons also run fully
  offline on the standard library, and say so at the top.
- Python 3.11 or newer for the course's own calculators and
  simulators. No other dependency exists anywhere in the repo.
- Optional: a GitHub account for the CI lesson, a marketplace
  account (Upwork or Fiverr) for the track lessons' exercises.

## How the course is built

Each lesson is a folder: a written lesson (README.md), one or
more runnable artifacts, one exercise (exercise.md), and a worked
solution (solution/SOLUTION.md). Because the subject is a
commercial tool students may not have open while studying, every
lesson carries an offline artifact that computes or simulates the
lesson system on the standard library alone: cost calculators,
scope estimators, a CLAUDE.md linter, a hook simulator, a
pipeline simulator, pricing worksheets. Where a lesson teaches a
real Claude Code artifact (a CLAUDE.md, a SKILL.md, a settings
hook, a GitHub Action), that file ships in the lesson ready to
copy, and the offline artifact validates or rehearses it.

Money lessons follow a fixed discipline: source it, price it, or
label it. Platform data is cited with its limits. List prices are
dated. Everything else is a worked example, introduced as one,
with an assumptions box the student can change.

## Modules and lessons (32)

0. **Foundations** (00-01): setup and the honesty contract; the
   economics of agent-assisted work, from platform data.
1. **The professional workstation** (02-05): CLAUDE.md systems,
   skills as reusable capital, subagents and parallel
   delegation, hooks as guardrails.
2. **Production workflows** (06-09): MCP as a force multiplier,
   headless mode and the Agent SDK, CI and scheduled automation,
   worktrees and background agents.
3. **Cost engineering** (10-11): plans versus API versus free
   routes, with the break-even math; token economics per job.
4. **Freelance and agency delivery** (12-16): positioning,
   scoping and estimation, pricing, delivery QA, handover and
   rehire.
5. **Productized services** (17-20): choosing the offer, building
   the pipeline, packaging and pricing the page, fulfilment and
   failure modes.
6. **Indie products and micro-SaaS** (21-24): choosing the
   problem, building and shipping, maintenance economics, launch
   and churn math.
7. **Automation consulting** (25-27): the audit as entry product,
   retainer structure and reporting, selling to teams (security,
   IP, contracts).
8. **Risk and durability** (28): failure modes, disclosure, IP
   and platform terms, when not to automate.
9. **Capstone** (29-31): one simulated client engagement end to
   end: spec and brief, the run, the delivery pack with a
   self-grading rubric.

## Capstone

A fictional client, Lumen Med Spa (three locations), needs the
thing TechAura actually sells: enquiries answered in minutes at
all hours, qualified, and booked, with a follow-up sequence for
the ones that go quiet. The engagement is simulated end to end
and every number in it is a worked example: the discovery notes,
the scope priced from the course's own estimator ($1,850 fixed,
assumptions printed), the build plan executed with the course's
workflow stack, a QA gate with recorded results, a delivery pack
(handover notes, runbook, support terms), and a grading rubric
students score themselves against before reading the worked
solution. The client, the business, and the numbers are invented
for teaching and labelled as such wherever they appear.

## Visuals

Branded SVGs generated by assets/visuals/generate_visuals.py in
the programme's house style (navy primary, light blue supporting,
cyan arrows, amber for human and safety gates), indexed in
assets/visuals/VISUALS.md, embedded in the root README and the
lessons they belong to, each with alt text. The set: course map,
the workstation stack, the four unattended modes, the cost stack
with break-even, the four income tracks, the delivery pipeline,
the capstone engagement flow. Diagrams carry structures and
labelled worked examples only; no chart in this repo plots an
income outcome as if it were data.

## Verification standard

Same gate as the sibling courses, run before this design is
called built: full recursive inventory reconciled against this
design, every lesson folder complete (README, exercise, solution,
artifact), the link checker at zero broken, every smoke test
passing under the same loop CI runs, and a repo-wide em dash scan
at zero.
