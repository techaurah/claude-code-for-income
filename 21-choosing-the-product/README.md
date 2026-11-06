# Lesson 21: Micro-SaaS: choosing a problem worth a product

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Module 5 (productized thinking) and Lesson 01 (the honesty contract) · **You need:** Just the lesson files. The scorer runs offline and rejects scores without evidence.

Module 6 stops selling your time entirely, which is the appeal
of a micro-SaaS product and also its trap. A service business
with a bad month loses a month. A product built on a weak problem
loses the build weeks, then charges you a maintenance tail for
years to remind you. So this module starts where the leverage
is: choosing the problem, with a scorer strict enough to kill
ideas you like, on evidence you have to write down.

## The five selection criteria

- **Pain severity.** How much does the problem hurt when it
  happens? Empty appointment slots hurt in revenue a clinic owner
  can count. Mild inconvenience does not survive a paywall.
- **Frequency.** How often does it happen? Daily pain supports a
  subscription. Annual pain supports, at best, an annual purchase
  made in a panic and resented by spring.
- **Ability to pay.** Does this buyer already spend money on
  adjacent tools? A buyer with a software budget is a different
  prospect from one who must be convinced software costs money.
- **Distribution reach.** Can you reach these buyers through a
  channel you actually have: an audience, a partner, a community
  you belong to? A great problem you cannot announce is a diary.
- **Maintenance lightness.** Scored 5 for a light tail. Every
  product drags a tail of updates, support, and dependency churn
  behind it, Lesson 23 prices it, and this criterion makes you
  look at the tail before you own it.

## Evidence, or the score does not count

`problem_score.py` refuses any criterion score that arrives
without a non-empty evidence note. That refusal is the lesson.
A severity of 5 because the idea feels important is a horoscope.
A severity of 5 because three clinic owners named the problem
unprompted in discovery calls is evidence, and the note forces
you to write which one you have. Scores without notes are how
builders talk themselves into quarters of work on a guess.

## The kill line

Totals rank the living. The kill line buries the dead: any
criterion at 1 kills the idea outright, whatever the total. The
fixture proves why. Fully autonomous tax filing totals 15 of 25,
a respectable middle score, on severe pain and strong ability to
pay. Its maintenance lightness is 1, because tax rules change
every year in every jurisdiction and an error is not a bug, it
is a liability. The total says maybe. The kill line says no, and
the kill line is right, because a single fatal criterion does
not average out. It compounds, monthly, for as long as the
product lives.

Killing cheaply is a skill, not a loss. Each fixture problem you
kill on paper costs a reading. Each one you build first costs a
quarter and a tail. Keep a written list of killed ideas with the
criterion that killed them. It is the cheapest research archive
you will ever own, and it stops the same idea returning in six
months wearing a new name. A killed idea can also return
honestly, later, when the killing criterion changes: a partner
gives you distribution, a platform absorbs the maintenance, a
regulation settles. The list records the condition, so the idea
waits for its condition instead of for your weakest moment.

## Run it

Run `python3 problem_score.py` and read the ranking: the clinic
reminder problem first at 22, the invoice helper alive at 18,
the tax idea last and marked killed. Then score a problem of
your own and try, deliberately, to submit a score without an
evidence note and watch it refuse. Then run
`python3 smoke_test.py`, which asserts the ranking, the evidence
rejection, and the kill.

## Common failures

- **Scoring the solution instead of the problem.** Shiny buildability is not a criterion here. Agents make many things buildable now, which is exactly why problem choice carries the return.
- **Averaging away a fatal flaw.** If distribution is 1, a total of 20 is a well built product nobody hears about. The kill line exists because multiplication, not addition, runs a product's life.
- **Evidence notes that quote yourself.** "I believe clinics hate no-shows" is a belief with formatting. Evidence names a source outside your head: a call, a bill, a forum thread, a tool they already pay for.

## Recap checklist

- [ ] I can state the five criteria and which one most builders forget.
- [ ] Every score I assign carries an evidence note that names a source outside my own opinion.
- [ ] I have a written kill list, and I can name the criterion that killed each entry.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Upwork In-Demand Skills 2026](https://www.upwork.com/resources/in-demand-jobs-and-skills)
- [Stripe pricing](https://stripe.com/pricing)
