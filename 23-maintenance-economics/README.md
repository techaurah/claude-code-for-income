# Lesson 23: Maintenance economics: keeping a product alive cheaply

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 22 (a shipped product), Lesson 11 (measured cost per job) · **You need:** Just the lesson files. The ledger runs offline on the shipped profile.

Shipping a product creates a monthly bill that arrives whether
or not anyone pays you that month. This lesson writes that bill
down as a ledger with four lines, adds a fifth line most builders
forget, their own agent-run maintenance, and derives the only
price question that matters at small scale: the floor below
which each new user makes you poorer.

## The four lines of the ledger

- **Hosting.** The fixed cost of keeping the lights on: compute,
  database, storage, the domain. Boring, knowable, and the line
  builders estimate most accurately because a provider invoices it.
- **Support time.** Tickets per hundred users, times minutes per
  ticket, times your hourly rate. It grows with users, which
  makes it a variable cost, and it is the line builders estimate
  worst because nobody logs the small answers.
- **Dependency churn.** Libraries update, APIs deprecate, a
  provider changes a limit. Churn arrives as small urgent work
  on someone else's schedule, and it is why maintenance lightness
  was a selection criterion back in Lesson 21.
- **Model costs for maintenance itself.** The next section.

## Agent-run maintenance, and its own cost line

Agents change the maintenance shape. A scheduled routine can run
the dependency updates, execute the test suite, draft the
changelog, triage the support inbox into answered, escalated,
and ignored, and open a tidy summary for your morning review.
That labour is real and it is not free. Each run spends tokens,
and the ledger must carry the line or the automation is a cost
hiding inside a saving.

The fixture prices it honestly at list rates checked October
2026: Sonnet class at $2 per million input tokens and $10 per
million output, so a run of 400,000 input and 80,000 output
tokens costs $1.60, and twelve runs a month cost $19.20. Small
money, and that is the point of writing it down: small lines are
the ones that quietly double when a routine starts running daily
instead of weekly, and nobody notices until the bill does.

## The price floor and break-even

From the ledger, two numbers fall out. The contribution per user
is the price minus the variable support cost per user. The break
even user count is the fixed costs, hosting plus agent runs,
divided by that contribution, rounded up. Below break-even, the
product is a subsidised hobby with users. Above it, each user
adds contribution, and Lesson 24 can talk about growth with a
straight face.

**WORKED EXAMPLE, with its assumptions printed.** The fixture is
a fictional reminder tool for a solo practice: 120 users at $15
a month, 8 tickets per 100 users at 18 minutes each and $40 an
hour, hosting at $45, and the agent line above. The ledger in
`maintenance_ledger.py` computes support at $115.20 a month,
total cost at $179.40 against $1,800 of revenue, a gross margin
of $13.50 per user, and break-even at 5 users. Change any input
and the outputs move. None of these numbers describes your
product, and the tool prints the assumptions every run so nobody
quotes the result without them.

The discipline generalises: if your contribution per user is
negative, growth is a faster way to lose money, and the fix is
price or support cost, never volume.

## Run it

Run `python3 maintenance_ledger.py` and recompute the break-even
by hand from the printed assumptions: fixed costs divided by
price minus support cost per user. Then halve the price in a
copy of the profile and watch break-even move. Then run
`python3 smoke_test.py`, which asserts the support cost, the
agent cost per run, and the break-even count independently.

## Common failures

- **Pricing from competitors instead of the ledger.** A rival's price reflects their costs, their churn, and possibly their investor subsidy. Your floor comes from your four lines or it comes from nowhere.
- **Support time valued at zero because it is yours.** Unpriced owner time is how products look profitable until the owner needs a holiday. Value it at your Lesson 00 rate, always.
- **Agent routines with no cost ceiling.** An uncapped nightly routine that retries is a meter running in an empty room. Give every routine a run budget and read its line monthly.

## Recap checklist

- [ ] My ledger has hosting, support, churn allowance, and the agent maintenance line, each with a number.
- [ ] I can state my contribution per user and my break-even user count from memory.
- [ ] My price sits above the floor the ledger implies, or I have a written reason and a date to revisit it.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Anthropic API pricing](https://claude.com/pricing)
- [Stripe pricing](https://stripe.com/pricing)
