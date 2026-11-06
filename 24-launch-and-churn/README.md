# Lesson 24: Launch, pricing, and the churn math

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 23 (your ledger and price floor) · **You need:** Just the lesson files. The churn simulator runs offline and labels itself a model on every run.

Module 6 closes with the launch, and this lesson's first claim
is unfashionable: a launch is a sequence, not an event. The
second claim is arithmetic: at small scale, retention beats
acquisition so reliably that the churn rate, a number most solo
builders never compute, decides whether the product compounds
or leaks. Both claims are testable with the tools in this folder.

## Launch as a sequence

Start with the audience you already have. For this course's
reader, that is the Module 5 client list, the people who watched
the productized work land, and any community where you have
genuinely contributed. They go first, in small numbers, because
their feedback is kind enough to be honest and their churn in
month one teaches more than a stranger's silence.

Then widen one channel at a time: a partner whose audience
matches the Lesson 21 buyer, a directory or marketplace listing,
content that names the problem the way buyers name it. One
channel at a time is not caution. It is measurement. Launch
everywhere at once and a good month tells you nothing you can
repeat, while a bad month tells you nothing you can fix.

Public launch, the announcement day people imagine, comes last,
when onboarding survives strangers, support has a path, and the
Lesson 20 pause discipline exists for signups too. An audience
arriving before the product can hold them is not a launch. It
is a churn donation.

## Pricing from the ledger up

Price from Lesson 23, never from nerves. The floor is the
contribution math: price must clear support cost per user with
fixed costs covered at a user count you can plausibly reach.
Above the floor, price against the buyer's existing spend, the
adjacent tools from Lesson 21's ability to pay evidence. Below
the floor, no launch sequence saves you, because every retained
user extends a loss. If the market will not bear a price above
your floor, the honest conclusions are to cut the maintenance
tail, narrow the buyer, or kill the product, in that order.

## The churn mathematics

Four terms, each defined by its formula:

- **Monthly recurring revenue (MRR):** subscribers times price.
- **Churn rate:** the share of subscribers who cancel in a
  month, as a fraction. 8 percent churn is 0.08.
- **Expected lifetime:** 1 divided by the churn rate. At 0.08, a
  subscriber stays 12.5 months on average.
- **Lifetime value (LTV), gross:** price times lifetime. At $15
  and 12.5 months, $187.50, gross before costs, which means
  before Lesson 23 takes its lines off. Net LTV uses margin per
  user instead of price, and the gap between the two is why this
  course prints the word gross every time.

**MODEL, with stated assumptions.** `churn_math.py` runs the
fixture: 40 starting subscribers, 12 adds a month, 8 percent
churn, $15 price, constant everything. Month 12 lands at about
109.6 subscribers and about $1,643 in MRR. Those figures are the
output of the assumptions, not a forecast. Real adds arrive in
lumps, real churn moves with quality and season, and the tool
prints the assumptions first so the numbers never travel alone.

## Why retention beats acquisition here

Run the model twice in your head. Doubling adds from 12 to 24
roughly doubles the workload of acquisition forever. Halving
churn from 8 to 4 percent doubles lifetime from 12.5 to 25
months and doubles LTV with it, and the subscribers you already
have start compounding instead of leaking. At small scale the
cheapest growth is a cancellation prevented: an onboarding fix,
a reminder before a silent user drifts, a support answer that
arrives inside the window. Acquisition fills the bucket.
Retention is the bucket.

## Run it

Run `python3 churn_math.py` and verify the month 12 line against
the formula by hand for month 1: 40 minus 8 percent, plus 12,
times the price. Then edit the scenario to 4 percent churn and
watch lifetime and month 12 move. Then run
`python3 smoke_test.py`, which asserts the lifetime formula, the
gross LTV, and the month 12 figure for the shipped fixture.

## Common failures

- **Launching to everyone on day one.** Strangers churn silently and teach nothing, while the audience you have would have told you exactly what was broken. Sequence is free research, spent in the right order.
- **Quoting LTV without the word gross.** Gross LTV at $187.50 sounds like permission to spend on acquisition. Net of the Lesson 23 ledger it is a smaller, honest number, and spending against the gross one is how small products die well marketed.
- **Watching MRR and never computing churn.** MRR can rise while churn worsens, as long as adds outrun it, until the month adds pause. Churn is the early warning. Compute it monthly, from the first subscriber.

## Recap checklist

- [ ] My launch is a written sequence, audience I have first, one new channel at a time.
- [ ] My price clears the Lesson 23 floor, and I can show the contribution math.
- [ ] I can compute lifetime and gross LTV from my churn rate, and I state gross every time.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Stripe pricing](https://stripe.com/pricing)
- [Upwork In-Demand Skills 2026](https://www.upwork.com/resources/in-demand-jobs-and-skills)
