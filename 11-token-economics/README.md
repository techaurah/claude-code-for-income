# Lesson 11: Token economics: knowing your cost per job

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 10 · **You need:** Python 3.11 or newer. Optional: one real headless run whose JSON output you can inspect.

Lesson 10 priced the routes. This lesson prices the
unit that actually earns money: one job. A month is
just jobs added up, and a practice that cannot say
what a job cost cannot say whether the job was worth
doing at that model class, with that much context, and
that many retries.

Cost per job is a measurement habit, not a prediction.
Headless runs report their own usage. Your job is to
read it, record it, and route the next job better.

## Where tokens actually go

Beginners blame the answer for the bill. The answer is
often the smallest part. In a typical coding job, tokens
go to five places, in roughly this order of surprise.

The system prompt and tool definitions ride on every
call. They are fixed rent. File reads are usually the
largest variable cost: one broad search that returns
whole files can cost more than the fix it informed.
Conversation history grows turn by turn, so a long,
drifting session re-pays for its own past. Retries are
the ugly line: a failed approach does not refund its
tokens when you start again. Output, the code itself,
is often last.

That ordering gives you the levers in the right order
too. Narrow the reads. Keep sessions on task or start
fresh. Fix the cause of retries. Then worry about how
verbose the answer is.

## Prompt caching: paying rent once

When the same context is sent repeatedly, prompt caching
lets the repeated part be read back cheaply instead of
priced as fresh input each time. In this course's
calculator, cache reads are priced at one tenth of the
input price, labelled as the current Sonnet class
behaviour. Treat the factor as dated, like any price,
and re-check it when you re-check Lesson 10.

Caching rewards stable context. A project brief, a style
guide, and a large reference file that stay fixed across
jobs are good cache citizens. Context that changes every
run caches badly, and no setting fixes that. Structure
work so the stable material is stable.

In `jobs.csv`, the summarize-notes job sends two million
input tokens, half of them cached. Its input cost is
$2.20 instead of $4.00: one million fresh tokens at $2,
plus one million cached tokens at $0.20. Small numbers,
same shape at any scale.

## Batch: half price for work that can wait

The Batch API is half price in both directions. It fits
work with no human waiting on the other end: overnight
reports, bulk tagging, first pass reviews of a backlog.

It does not fit interactive delivery, and it does not
fit anything on a client deadline measured in hours.
The discipline is classification. Before a job runs, ask
whether anyone is waiting. If not, batch is the default
and full price needs a reason.

In the fixture, batch-reports would cost $18 at full
price. Batched, it costs $9. The work is identical. Only
the waiting changed.

## Model routing by task class

Routing is where token economics becomes judgement.

Route mechanical work to Haiku class: routing enquiries,
extracting fields, renaming, format conversion, short
classification. Route default delivery work to Sonnet
class: features, fixes, integrations, tests. Route the
hard core to Opus class: the design decision, the subtle
bug, the migration with consequences. Reserve Fable class
for work whose failure cost dwarfs the token bill.

The fixture's last job shows the opposite discipline.
retry-storm-booking ran on Opus class, burned six million
input tokens through retries, and cost $54: more than
the other three jobs combined. The lesson is not that
Opus is expensive. It is that retries on a premium class
are expensive, and the fix was upstream: a clearer task,
a smaller context, and a stop rule, not a cheaper model
applied after the storm.

## Reading cost from headless output

A headless run with JSON output includes a total cost
field, reported by the tool itself as a client side
estimate. Record it per job, with the job name, the model
class, and whether the result passed review. Three fields
in a CSV will, within a month, tell you which jobs to
reroute, which to batch, and which prompts keep paying
retry tax.

`job_cost.py` reads exactly that shape of ledger. It
prices each job, applies caching and batch rules, names
the most expensive job, and totals the month. Run it on
the fixture, then replace the fixture rows with a week
of your own jobs and read your own storm line.

## Run it

Run `python3 job_cost.py` and check the four fixture
jobs against the figures in this lesson: $0.20, $7.20,
$9.00, and $54.00, totalling $70.40. Then run
`python3 smoke_test.py`.

## Common failures

- **Optimising output length while file reads run wild.** The answer is rarely the bill. Measure per job first, then cut the largest line, which is usually context.
- **Running every job on one premium class by habit.** Habit is not routing. Classify the task first, and let the class follow the classification.
- **Treating retries as free learning.** A retry spends real tokens and often signals a vague task. Log retry heavy jobs by name and fix the task, not just the bill.

## Recap checklist

- [ ] I can name the five places tokens go and which one usually costs most.
- [ ] I can price a cached job and a batch job by hand and match the calculator.
- [ ] I keep, or will start, a per job ledger with model class and review outcome.

## Resources

- [Claude pricing](https://claude.com/pricing)
- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code documentation on headless mode](https://code.claude.com/docs/en/headless)
- [Fiverr payment terms](https://www.fiverr.com/legal/payments-terms)
