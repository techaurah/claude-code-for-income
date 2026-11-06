# Lesson 10: The cost stack: plans, API, and free routes

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 00 (your cost baseline) and Lesson 01 · **You need:** Python 3.11 or newer and your own rough usage estimate for one month.

Every income lesson after this one divides by a cost.
If the cost is a guess, the price built on it is a guess.
This lesson builds the cost stack properly: three routes
for paying for the work, the break-even for each, and the
caveats that stop a cheap route becoming an expensive
mistake.

Prices in this lesson are public list prices checked
October 2026. They move. Re-check them before you quote
a client, and treat the method as the durable part.

## The three routes

There are three ways to pay for Claude Code work.

First, a subscription plan. You pay per month and you
work interactively inside usage limits. Pro is $20 a
month, or $17 a month billed annually. Max 5x is $100
a month. Max 20x is $200 a month. Max plans are monthly
only.

Second, the API. You pay per million tokens, input and
output priced separately. There is no plan discount
hidden in it. You pay for exactly what a job uses, and
headless work reports its own cost as it runs.

Third, free third-party tiers reached through a gateway
tool that points Claude Code at another provider. The
cash price is zero. The other costs are real, and this
lesson gives them a full section below.

Most working practices use route one, route two, or a
mix. Route three has a narrow, honest use, and client
work is not it.

## API prices, dated

Per million tokens, input and output, October 2026:

- Sonnet class: $2 in, $10 out. The default for most
  client work: strong, fast enough, and priced so a
  normal job costs single dollars, not tens.
- Opus class: $4 in, $20 out. For the hard core of a
  problem, not for moving files around.
- Haiku class: $0.10 in, $0.50 out. For mechanical work:
  routing, tagging, short summaries, format fixes.
- Fable class: $10 in, $50 out. The premium tier. Use
  it only when the task earns that price.

The Batch API is half price in both directions, for
work that can wait. Lesson 11 uses these same prices
to cost individual jobs, so learn the shape now: output
costs more than input in every class, and class choice
moves a bill by multiples, not by percent.

Check the maths once by hand. Ten million input tokens
and two million output tokens on Sonnet class cost
10 times $2 plus 2 times $10, which is $40. The smoke
test for this lesson asserts exactly that figure.

## The Max credit detail most people miss

Max plans now return their price as monthly API credit.
Max 5x returns $100 of credit. Max 20x returns $200.
The credit offsets API spend in that month. It does not
roll over, and it does not pay out as cash.

That changes the comparison. A practitioner on Max 5x
who also runs $30 of headless API jobs in a month does
not pay $130. The credit absorbs the $30, and the cash
total stays $100. The same practitioner running $150
of API work pays $150 in total: the plan price, plus
the $50 the credit could not cover.

`cost_stack.py` models this directly, so you do not
have to hold it in your head while comparing routes.

## Break-even, route by route

The break-even test from Lesson 01 applies per plan:

**Break-even hours = monthly plan price / your rate.**

At a $75 rate, Pro needs about 0.27 saved hours a month,
Max 5x needs about 1.33, and Max 20x needs about 2.67.
At a $35 rate the same plans need about 0.57, 2.86, and
5.71 hours. The plan does not change. Your rate decides
whether it is cheap.

The API route has no fixed break-even. It has a per job
cost, which is why Lesson 11 exists. Its break-even
question is different: does this job, at this model
class, cost less than the human time it replaces, after
you add your review time back in?

## The free route, with its caveats printed

Routing Claude Code to another provider's free models
is off-label use of those tiers. Say that plainly in
your own notes, because three risks follow from it.

Free tiers may train on prompts. Client code, client
data, and client names must never travel that route.
Capacity is small. A free tier that works for a demo
can stall in the middle of a delivery deadline. Terms
can change or the tier can close, with no contract to
point at when it does.

The defensible use is narrow: your own throwaway
experiments, public code, nothing confidential, nothing
a client is waiting for. If a route cannot be defended
to the client in one honest sentence, it is not cheap.
It is borrowed risk.

## Choosing a route you can defend

Start on the smallest plan that fits real interactive
work. Add API billing when headless jobs become regular,
and let the Max credit absorb them if you are already
on Max. Move model classes down before you move plans
up: a lot of expensive months are Haiku work run on a
premium class by habit.

The tool in this lesson ranks plan and API options by
cash cost for a profile you supply. It excludes the
free route for client work on purpose. Cost is a reason.
Defensibility is the filter before it.

## Run it

Run `python3 cost_stack.py` for the default profile,
then run it with your own profile JSON: interactive
hours, your rate, and your headless jobs with token
counts. Then run `python3 smoke_test.py`.

## Common failures

- **Comparing a plan price to an API bill without the credit.** On Max, the first dollars of API spend are already paid for. Double counting them makes the API route look worse than it is.
- **Buying Max 20x ahead of the workload.** A bigger plan is not ambition. If break-even needs more saved hours than you bill, drop a tier and let measured job costs argue for the upgrade.
- **Sending client work through a free tier to save a few dollars.** The saving is small, the terms and confidentiality risks are not, and one incident costs more than years of plan fees.

## Recap checklist

- [ ] I can state all three routes, the October 2026 price of each plan, and the per million token price of each model class.
- [ ] I have run my own monthly profile through the calculator and can name my cheapest defensible route.
- [ ] I can explain, in one sentence, why free tiers are excluded from client work.

## Resources

- [Claude pricing](https://claude.com/pricing)
- [Claude Code documentation](https://code.claude.com/docs)
- [Upwork freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
- [Fiverr payment terms](https://www.fiverr.com/legal/payments-terms)
