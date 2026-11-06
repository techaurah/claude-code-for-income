# AGENTS.md

Conventions for AI assistants working in this repository. Human contributors should read CONTRIBUTING.md; this file states the same rules in machine-checkable form.

## Repository shape

- Lessons live in root folders named `NN-kebab-lesson-name`, numbered 00 to 31, matching the lessons table in README.md exactly. Never rename a lesson folder without updating README.md, llms.txt, and PROGRESS.md in the same change.
- Each lesson folder contains: `README.md` (the lesson), runnable artifacts (Python calculators, simulators, checkers, and copy-ready Claude Code config files), `exercise.md`, and `solution/` with the worked solution.
- Root files: README.md (landing page), llms.txt (course index for AI assistants), PROGRESS.md (learner checklist), DESIGN.md (the design this repo was built to), RESEARCH.md (the competitor scan and the publish verdict), resources/, showcase/, translations/, assets/, tools/.

## Writing rules

- Plain language, short sentences. Define every technical term on first use or ensure it exists in resources/glossary.md.
- No em dashes anywhere, in prose or code comments. Use commas, colons, or full stops instead.
- Question-shaped headings are welcome in lessons where natural.
- **Honesty rules, the point of this course.** No invented statistics, learner counts, earnings figures, or results. No sentence that promises or implies a student will earn a specific amount. Platform data (Upwork, Fiverr) is cited with source and limits. Plan and API prices carry the month checked (October 2026 at first publication) and a note that prices move. Everything else financial is a worked example, introduced as one, with assumptions printed next to the numbers.
- Do not promise certificates. The course's completion artifact is the public capstone showcase.

## Code rules

- Python artifacts, checkers, and smoke tests run on the standard library (Python 3.11 or newer) with a zero-credential path. Any file that drives a live Claude Code session must say so at the top, must work or exit cleanly with a clear message when `claude` is absent, and must keep its logic testable offline.
- Every JSON example must parse and pass tools/validate_course.py. CI runs it.
- A lesson may ship a `smoke_test.py`; CI runs every file with that name, so keep smoke tests fast, offline, and credential-free.
- Never print a real API key, token, or client name in an example. Worked examples use the fictional client named in the capstone spec (Lumen Med Spa) or clearly generic placeholders.

## Change rules

- Small fixes may go straight to a pull request. New lessons, rewritten lessons, and new translation languages start with an issue (the two-tier rule in CONTRIBUTING.md).
- If lesson titles change, update README.md, llms.txt, and PROGRESS.md together; the three must never disagree.
- Showcase rows are added by learners via PR, one row per learner, format in showcase/README.md.
