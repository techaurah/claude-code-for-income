# Project memory: booking integration (worked example)

This is a project level CLAUDE.md for a fictional project for
Lumen Med Spa. It is a worked example, not a real client file.

## Commands

- Install: `python3 -m pip install -r requirements.txt`
- Run tests: `python3 -m pytest -q`
- Lint: `python3 -m compileall src`
- Run locally: `python3 -m src.app`

## Conventions

- Python 3.11 or newer, standard library first.
- Short functions with names that state the action.
- Tests sit next to the module they cover.
- Commit messages are one line, in the imperative mood.

## Boundaries

- Never read or print files matching `.env` or `secrets`.
- Never edit generated files under `src/generated/` by hand.
- Payment webhooks are tested with fixtures only, never live calls.
- Ask for review before changing booking or payment logic.

## Architecture in brief

The web app takes enquiries, the API qualifies and books them,
and a worker sends follow ups. Data flows one way: web, API, worker.
