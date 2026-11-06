# Lesson 17: Productized services: choosing an offer that repeats

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 12 to 16 (positioning, scoping, pricing, delivery QA, handover) · **You need:** Just the lesson files. The scorer runs offline on the standard library.

Module 5 changes the unit of work. In Module 4 you sold your
judgement one engagement at a time. A productized service sells
one named outcome, at one fixed price, through one pipeline that
runs the same way every time. The margin does not come from
working faster. It comes from not redesigning the work on every
order. This lesson is the filter before any of that: choosing
which service deserves to become a product, and refusing the rest
early, while refusal is still cheap.

## What productized means, precisely

A productized service is a service sold as a fixed package: named
outcome, fixed scope, fixed price, repeatable fulfilment pipeline.
The client buys the outcome on a page, not your hours in a call.
Four conditions have to hold at once, and Lesson 17 tests each one
before you build anything:

- The same buyer, with the same role and the same budget line.
- The same pain, stated in the buyer's own words, not yours.
- A bounded scope you can write as inclusions and exclusions.
- A delivery you can repeat without inventing steps per order.

If one condition fails, you do not have a weak product. You have
bespoke work wearing a fixed price, which is the worst contract
shape in this course: the client holds the price, you hold the
unbounded risk.

## Why judgement-heavy work resists productizing

Some work is valuable precisely because it does not repeat. A
bespoke data migration depends on the source system, the data
quality no one has measured yet, and decisions the client has not
made. An incident investigation, a rescue project, a strategy
call: the judgement is the product. Try to fix the scope and the
price in advance and one of two things happens. You pad the price
until nobody buys, or you absorb every surprise until the margin
is gone.

That is not a failure of the work. Migrations and investigations
are good Module 4 work, priced from discovery, Lesson 13 style.
The failure is forcing them into a shape they do not fit. The
scorer in this lesson gives that work a low total on purpose, so
you practise seeing the shape before you practise selling it.

## The five scoring criteria

`offer_score.py` scores each candidate from 1 to 5 on five
criteria, and the fixture in `offers.json` ships three candidates
chosen to teach the spread:

- **Buyer clarity.** Can you name the buyer in one phrase? Med
  spa owners with three locations is a buyer. Anyone who needs a
  chatbot is not.
- **Pain urgency.** Does the pain cost money this week? Missed
  enquiries at 10pm do. A nicer dashboard does not.
- **Scope boundedness.** Can you list what is out, in Lesson 19
  language, without arguing with yourself?
- **Delivery repeatability.** Would order ten follow the same
  steps as order one, with the same checks?
- **Support load, inverted.** A load of 5 contributes 1 point.
  Heavy support is the silent tax on productized work, so the
  score charges for it up front instead of in month two.

Watch the generic offer in the fixture. Its delivery is not even
hard. It scores last and gets flagged because buyer clarity and
scope are both at 1, and no pipeline fixes a buyer you cannot
name. The med spa enquiry package scores first for the opposite
reason: one buyer, one painful leak, one bounded system, and a
support load the intake form keeps small by design.

## A note on the money in this module

This module talks about prices, margins, and capacity, so the
Lesson 01 discipline applies with no exceptions. Platform figures
keep their source and limits. Claude plan and API prices are the
public list prices checked October 2026, and they move. Everything
else, including any price you put on your own package in Lesson
19, is a worked example: your inputs, printed next to the result,
never a typical outcome and never a forecast for the next reader.

## Run it

Run `python3 offer_score.py` and read the ranking with the verdict
line under each offer. Then edit `offers.json`: add one service
you actually sell, score it honestly, and note which criterion
you scored from evidence and which you scored from hope. Then run
`python3 smoke_test.py`, which asserts the fixture ranking, the
flag on the generic offer, and the range checks on every score.

## Common failures

- **Productizing the work you enjoy instead of the work that repeats.** Enjoyment does not lower support load or bound the scope. Score the candidate in front of you, not the one you wish you had.
- **Scoring from hope.** A 5 for buyer clarity means you can name buyers you have already spoken to. If the evidence is a feeling, the honest score is 2, and the fix is conversations, not optimism.
- **Treating a low score as a verdict on the work.** The migration scores low as a product and stays valuable as bespoke work. The scorer sorts shapes, not worth.

## Recap checklist

- [ ] I can state the four conditions a service needs before it can be productized.
- [ ] I have scored one real service of mine and can defend each score with evidence.
- [ ] I can explain why support load is inverted, in one sentence.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Upwork In-Demand Skills 2026](https://www.upwork.com/resources/in-demand-jobs-and-skills)
- [Upwork's freelancer fee schedule](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
