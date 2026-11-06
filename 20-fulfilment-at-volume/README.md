# Lesson 20: Fulfilment at volume: queues, failures, and refunds

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 18 and 19 (pipeline minutes and the packaged promise) · **You need:** Just the lesson files. The queue simulator runs offline with a fixed arrival pattern.

Module 5 ends where productized services actually fail: not at
the sale, but three weeks after a launch works. Orders arrive
faster than human minutes clear them, the queue looks manageable
in week one, and by the time the delay is visible to buyers the
backlog needs more than good intentions to clear. This lesson
teaches capacity as arithmetic, queue behaviour as a system, and
the pause button as a designed part of the offer.

## Capacity math, in human minutes

Your capacity is not orders per week. It is human minutes per
week, divided by human minutes per order. Lesson 18 gave a clean
order at 90 human minutes and a bounced order at 135. A solo
operator with 600 honest fulfilment minutes in a week, ten hours
after the rest of the business takes its share, clears six clean
orders in that week, fewer when QA bounces land. That number,
not your ambition, is the sales ceiling. Sell past it and you
have not grown. You have borrowed delivery time from next week
at an interest rate set by angry buyers.

## What a queue does when arrivals beat service

`queue_sim.py` runs two deterministic patterns against that
capacity. In the calm pattern, two or three orders a week, the
queue empties every week and nothing breaches. In the overloaded
pattern, eight to twelve orders a week against six served, the
backlog grows every single week while each individual week still
feels survivable. That gap, between the weekly feeling and the
cumulative fact, is why queues surprise people.

The simulator counts SLA breaches: orders still waiting past the
stated limit, here two weeks. Breaches appear late, in weeks
seven and eight of the fixture, long after the decision that
caused them. A queue punishes you on a delay, which is exactly
why the decision to pause cannot wait for the punishment.

## Unrecoverable means pause, not push

The simulator marks the first week where the backlog alone needs
more than two weeks of capacity while arrivals still exceed one
week of service. In the overloaded fixture that is week five.
Past that point, working weekends does not clear the queue,
because new arrivals refill it faster than heroic effort drains
it. The queue is unrecoverable without pausing intake. That word
matters: unrecoverable describes the maths, not your character.

Pausing sales is therefore a designed move, written before the
launch: the backlog number that triggers it, the page change
that closes intake, the message waiting buyers receive, and the
condition for reopening. A seller who designed the pause keeps
the buyers a seller who hides from the queue loses.

## Failure and refund policy, designed in advance

Failures at volume are statistical, not personal. Some orders
will bounce twice. Some intakes will be unusable. Some buyers
will ask for a refund on day thirteen. Each case gets a policy
before it gets a case: the fix first, inside the support window,
per Lesson 19's guarantee, and a refund of the package fee when
the fix fails, processed fast and without a debate the buyer has
to win. Refund handling is part of fulfilment, budgeted like QA,
because the alternative, arguing each case from scratch, costs
more human minutes than the refund and all of your reputation
with it.

## Run it

Run `python3 queue_sim.py` and compare the two patterns week by
week. Find the week the overloaded backlog first exceeds one
week of capacity, then the later week the simulator calls
unrecoverable, and sit with the distance between them: that gap
is your decision window. Then run `python3 smoke_test.py`, which
asserts breaches and an unrecoverable week on the overloaded
fixture, and a clean run with neither on the calm one.

## Common failures

- **Counting capacity in orders instead of minutes.** Orders differ by exactly the QA bounce you averaged away. Minutes do not care about your averages, and neither does the queue.
- **Pausing after the first breach.** A breach is the queue reporting damage already done. The trigger belongs on backlog size, which moves weeks earlier.
- **Treating refunds as admissions to avoid.** A slow, contested refund costs the fee anyway in time and reputation. A fast, policy based refund is a fulfilment cost you already priced.

## Recap checklist

- [ ] I know my weekly human minutes, my minutes per order, and the sales ceiling they imply.
- [ ] My pause trigger is a backlog number, written down, with the buyer message drafted.
- [ ] My refund path follows the Lesson 19 guarantee and needs no fresh decision per case.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Upwork In-Demand Skills 2026](https://www.upwork.com/resources/in-demand-jobs-and-skills)
- [Fiverr's payment terms](https://www.fiverr.com/legal/payments-terms)
