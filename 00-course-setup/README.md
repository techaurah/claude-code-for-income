# Lesson 00: Course setup: environment, accounts, and your cost baseline

**Time:** about 45 minutes · **Difficulty:** Advanced (the course's floor) · **Prerequisites:** Professional development experience and at least one real project built with Claude Code · **You need:** Python 3.11 or newer. A Claude account is optional for this lesson; the checker reports what it finds either way.

Every course in this programme starts by verifying the environment, and this one adds a second verification the income lessons depend on: your cost baseline. The workstation modules assume tools that exist. The money modules assume numbers that are yours. This lesson produces both, in one sitting, and it states the course's honesty contract in working form rather than as a slogan.

## What this course assumes you already have

This is an advanced course, and Lesson 00 is where that stops being a label. You should already be able to: ship and maintain real software, review a diff and say what is wrong with it, work in a terminal, and drive Claude Code on a real project without a tutorial open. If any of that is shaky, the free official courses in [resources](../../resources/README.md) will close the gap faster than struggling here, and this course will wait.

What this course teaches is the layer those courses do not: the workstation as an asset, the cost stack as a ledger, and delivery, packaging, products, and consulting as systems.

## The environment check

Run the checker in this folder:

```
python3 check_environment.py
```

It verifies four things and prints a plain report: Python 3.11 or newer (every artifact in this repo needs it), git (the worktree and CI lessons assume it), the `claude` CLI if present (the live lessons use it; its absence blocks nothing offline), and the lesson folder layout (so a partial clone is caught now, not in Lesson 18). Nothing is installed, nothing is sent anywhere, and no credential is read.

With `--write` it also writes `baseline.json` next to itself: the file the rest of the course calls your cost baseline.

## Your cost baseline: four numbers

The baseline is a small JSON record of the four numbers every money lesson in this course uses:

- **Your plan and its monthly price.** Pro at $20 a month, Max 5x at $100, Max 20x at $200, or an API account billed per token (US list prices checked October 2026; they move, and Lesson 10 teaches the re-check).
- **Your target billable rate.** What an hour of your delivered work should earn, before platform fees. If you do not have one yet, Lesson 01 and Lesson 14 build it from the work itself; for now, write the number you would charge a stranger for a day, divided by the hours you would actually bill.
- **Your platform fee, if any.** Upwork's freelancer service fee is variable (0% to 15%, shown before you send a proposal). Fiverr keeps 20%. Direct clients: zero. The fee belongs in the baseline because margin is what is left after it.
- **Your current client count and monthly hours available.** The capacity inputs the productized and retainer maths divide by.

None of these numbers leaves your machine. The baseline is a local file, and the course's calculators read yours instead of assuming a stranger's.

## The honesty contract, in working form

The research behind this course ([RESEARCH.md](../../RESEARCH.md)) found the income genre's standard move: an unsourced monthly figure, presented as typical. This course's counter-move is mechanical, and you will see it in every lesson:

1. Platform data is cited with its source and its limits, in the same paragraph.
2. Prices carry the month they were checked.
3. Everything else is a **worked example**, introduced as one, with an assumptions box you can edit. The capstone's $1,850 price is one. It is a teaching instrument, not a data point.

If you finish this course and catch yourself quoting a number, the habit to keep is asking which of the three it is.

## Run it

Run the checker, then run it again with `--write` and open `baseline.json`. Then run this lesson's smoke test (`python3 smoke_test.py`), which is the same loop CI runs across the whole repo: every lesson's artifacts, verified offline, on every push.

## Common failures

- **Skipping the baseline because the numbers feel made up.** They are estimates, and that is fine; an estimate you wrote down can be corrected, while the vague sense that a plan "pays for itself" cannot. Lesson 11 replaces estimates with measured cost per job.
- **Treating the environment check as ceremony.** The two failures it catches most, an old Python and a partial clone, otherwise surface mid-capstone wearing better costumes.
- **Reading ahead to the income tracks first.** The tracks divide by the workstation and cost modules. A price built before Lesson 10 is a guess wearing a suit.

## Recap checklist

- [ ] The checker passes, or I know exactly which item is missing and which lessons it affects.
- [ ] My `baseline.json` exists with four honest numbers in it.
- [ ] I can state the three kinds of money figures this course uses, and which kind the capstone price is.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Python downloads and documentation](https://www.python.org)
- [Anthropic Academy](https://anthropic.skilljar.com), if the prerequisites need closing first
