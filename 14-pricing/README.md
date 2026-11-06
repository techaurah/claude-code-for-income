# Lesson 14: Pricing the work: fixed, anchored, and defensible

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 10, 11, and 13 · **You need:** Python 3.11 or newer and a scope with human hours from Lesson 13.

Pricing is where the course's ledgers meet a real buyer.
Done badly, it is a number defended with hope. Done the
way this lesson teaches, it is three numbers in a known
relationship: a floor you will not cross, an anchor the
client supplied, and a price that sits between them for
reasons you can say out loud.

No figure in this lesson is a promise about your income.
The client figures are a worked example, labelled as one,
with its assumptions printed.

## The cost floor

The floor is what the work costs you before profit, built
from parts you have already measured in this course.

Human time at your target rate, from Lesson 13. Plus a
share of your plan cost for the month. Plus measured API
cost per job, from Lesson 11. That sum is the floor.
Below it, you are not discounting. You are paying the
client for the privilege of doing their work.

Floors are private. A client never needs your floor, and
showing it invites negotiation against your costs instead
of discussion of their outcome. What the client sees is
the price and what it buys, from Lesson 12.

## WORKED EXAMPLE: the floor for the Lumen build

Assumptions box. Fictional client: Lumen Med Spa, a
three location med spa group. Human time 9 hours at a
$75 target rate is $675. Plan share $25. Measured API
cost $20. This is a worked example.

Floor: $675 plus $25 plus $20 equals $720. Hold that
number. Every price judgement below is made against it.

The fixed price for this build, built up fully in Lesson
29, is $1,850. Gross margin at that price is $1,850 minus
$720, which is $1,130 before platform fee. That margin is
not greed and not luck. It is what covers discovery that
did not convert, revision risk, support, and the weeks
with no client work at all.

## Fees change the floor you must charge

Platform fees apply to the price, not to your costs, so
the floor you must charge on a fee taking channel rises.

Upwork's freelancer fee is variable, 0% to 15%, shown
before a proposal is sent. Fiverr keeps 20%, so the
seller receives 80%. Public fee facts, checked with the
platform terms linked below.

The arithmetic is simple and often skipped. At a 10%
channel fee, a $1,850 price delivers $1,665 to you. The
margin after fee is $1,665 minus the $720 floor, which
is $945. To merely cover a $720 floor at a 10% fee, you
must charge $800: the fee adjusted floor, which is the
floor divided by one minus the fee rate.

`price_model.py` computes all three: the floor, the fee
adjusted floor, and the margin at any candidate price.
Run your channel's real fee through it, not the fee you
wish the channel charged.

## The value anchor: the client's own number

In discovery, Lesson 13 told you to ask what the problem
costs when it stays unsolved, in the client's own words.
That answer is the anchor, and it is the only honest
ceiling reference you have.

In the worked example, the client framed the cost of
slow replies at $2,400 a month as their stated figure in
discovery: enquiries going cold overnight, across three
locations. Their number, from the worked example's
assumptions box, not a statistic. Against it, a $1,850
one off build that removes the problem is easy to reason
about together, because the comparison sits inside one
month of the problem's own cost.

Anchors do not set the price by themselves. A price above
the anchor needs a reason the client accepts. A price
far below it usually means you misread the problem, or
you are leaving margin that funds your support window
sitting on the table.

## Fixed, hourly, or package

Fixed price fits a scoped outcome with named boundaries,
which is why the capstone uses it. It rewards your
efficiency and puts estimation risk on you, which
Lessons 13 and 15 exist to control.

Hourly fits genuinely exploratory work where scope cannot
be named yet, billed with a cap and a review point. It
caps agent leverage, as Lesson 12 showed, so use it as a
discovery phase with an exit into fixed, not as the whole
engagement by default.

A package fits a repeating outcome for a repeating buyer
type: same system, bounded variations, a price the buyer
can read on a page. Module 5 builds packages properly.
The pricing rule does not change: floor first, anchor in
view, fee applied.

## Revision rounds and payment terms

Revision rounds are priced scope, stated in Lesson 13
and enforced here. Two rounds inside the delivered scope
are included. Further rounds are quoted as new work, at
the same rate logic, before they start. Free unlimited
revision is not a policy. It is a slow discount to zero.

Payment terms protect the floor in time. A deposit before
work starts, commonly a third to a half on fixed builds.
Milestone payments on longer work, tied to deliverables
the client can inspect, not to dates alone. Final payment
against the delivery pack from Lesson 16. State terms in
the proposal, not after the first invoice surprises
someone.

## Run it

Run `python3 price_model.py` and check the worked example:
floor $720, price $1,850, gross margin $1,130, effective
received at a 10% fee $1,665. Then model one real job with
your own scope, rate, and channel fee. Then run
`python3 smoke_test.py`.

## Common failures

- **Pricing from the anchor alone.** A rich client's big problem does not repeal your costs. If delivery expands to fill the anchor, the floor rises to meet it and the margin vanishes.
- **Forgetting the fee until payout.** A price that clears the floor before fees can sit under it after fees. Run every channel price through the fee adjustment first.
- **Discounting below the floor to win a first client.** A loss making first client teaches the market your work is worth a loss. Narrow the scope instead, and keep the price honest for the smaller build.

## Recap checklist

- [ ] I can build a cost floor from human time, plan share, and measured API cost without notes.
- [ ] I compute fee adjusted floors and margins after fees for the channel I actually use.
- [ ] My proposals state revision rounds and payment terms before work starts.

## Resources

- [Claude pricing](https://claude.com/pricing)
- [Claude Code documentation](https://code.claude.com/docs)
- [Upwork freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
- [Fiverr payment terms](https://www.fiverr.com/legal/payments-terms)
- [Upwork In-Demand Skills 2026](https://www.upwork.com/resources/in-demand-jobs-and-skills)
