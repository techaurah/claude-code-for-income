# Lesson 07: Headless mode and the Agent SDK: the agent as a program

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 02 to 06, especially the guardrails in Lesson 05 · **You need:** Python 3.11 or newer. A `claude` CLI is optional; every artifact works or exits cleanly without it.

So far, a human has started every session.
Headless mode removes the human from the start line.
You run `claude -p` with a prompt, from a script, a cron job, or a pipeline.
The agent runs non interactively, does the job inside the limits you set, and prints a result your program can read.
The Agent SDK goes one step further: it embeds the same agent inside your own application.
This lesson teaches the controls that keep a programmatic agent bounded.

## The headless command shape

A safe headless call names five things.

- **The prompt.** With `-p`, the full instruction for this one run.
- **The allowed tools.** With `--allowedTools`, the smallest set the job needs.
- **The permission mode.** How tool approvals are handled when no human is watching.
- **The caps.** `--max-turns` limits steps, and `--max-budget-usd` limits spend for the run.
- **The output format.** JSON, so a program can parse the result and its cost.

`headless_driver.py` in this lesson builds exactly this command from a job spec.
If the `claude` CLI is absent, it prints the command and exits cleanly.
That is the offline path, and it is also how you review a command before any real run.

## Permission modes, in plain terms

When no human is present, permission choices cannot be improvised.
Read the official docs for the current mode names and defaults before a live run, because this area changes.
The principle is stable even when names shift.
Grant the narrowest mode that lets the job finish, pair it with an explicit tool allowlist, and keep Lesson 05's guardrails in place for the commands that do run.
An allowlist plus caps plus guards is a system.
Any one of them alone is a hope.

## Caps are the contract

A headless run without caps is an open ended commitment.
Set them every time.

- Max turns stops a loop that keeps trying.
- A budget cap stops a run that keeps spending.
- A short, specific prompt stops a run that keeps wandering.

Worked example: assume a nightly check for Lumen Med Spa, the fictional client in this course.
Assumptions stated: one repository, read and test tools only, a budget cap set at the level of a small API job, and a turn cap low enough that a stuck run ends in minutes.
The point is not the exact numbers.
The point is that the numbers exist before the run starts, and the run's own output is checked against them after.

## JSON output and the cost field

With JSON output, a headless run reports its own result in a structured record.
It includes a `total_cost_usd` field.
Anthropic notes that this figure is a client side estimate.
Treat it as one: close enough to run a cost ledger, not a billing invoice.
Lesson 11 builds cost per job from exactly this field.
`sample_output.json` in this lesson shows the documented shape, with invented values for teaching.
`cost_report.py` parses such a file into a one line cost record you can append to a ledger: cost, turns, duration, and whether the run reported an error.

## The Agent SDK shape

The Agent SDK is Anthropic's library for embedding the agent in your own programs.
Conceptually, you stop shelling out to a command and start calling the agent from code: you supply the prompt, the tool configuration, and the limits, and you handle the streamed or final result in your application.
Use it when the agent is part of a product or a pipeline you ship, rather than a script you run.
Use headless mode when a script, a schedule, or CI is the host.
The caps and allowlists matter in both shapes, for the same reason: a program cannot raise an eyebrow at a strange run the way a human can.

## Safety before scale

Programmatic runs multiply whatever you configure, including mistakes.

- Start with read only tools on a copy of the work.
- Log the command, the caps, and the JSON output for every run.
- Alert on error results and on cost far above the run's usual record.
- Keep a human review step before any client visible output ships.

Lessons 08 and 09 put these runs on schedules and in parallel.
None of that is safe until a single capped run is boringly predictable.

## Run it

Build a command from the demo job spec, and parse the sample output:

```
python3 headless_driver.py
python3 cost_report.py sample_output.json
```

If `claude` is absent on your machine, the driver should print the command it would run and exit cleanly.
Then run `python3 smoke_test.py`.

## Common failures

- **No budget or turn cap.** One stuck loop can spend the margin of the whole engagement before anyone notices.
- **A broad tool allowlist for convenience.** Headless runs have no human to catch an odd tool call; the allowlist is the supervision.
- **Treating the cost field as an invoice.** It is a client side estimate, useful for ledgers and comparisons, and the docs say so.

## Recap checklist

- [ ] Every headless command I build names allowed tools, a permission mode, a turn cap, and a budget cap.
- [ ] I can parse a run's JSON output into a one line cost record.
- [ ] I can say when a job belongs in headless mode and when it belongs in the Agent SDK.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code headless mode](https://code.claude.com/docs/en/headless)
- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [Claude pricing](https://claude.com/pricing)
- [Anthropic on GitHub](https://github.com/anthropics)
