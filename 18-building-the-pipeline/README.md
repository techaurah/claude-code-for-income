# Lesson 18: Building the fulfilment pipeline

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 17 (a scored offer worth productizing), Lesson 07 (headless mode), Lesson 15 (delivery QA) · **You need:** Just the lesson files. The pipeline here is a deterministic simulation, offline, on the standard library.

An offer is a promise. A pipeline is how the promise gets kept
when you are busy, ill, or on the tenth order instead of the
first. This lesson builds the fulfilment pipeline for the offer
you chose in Lesson 17 as a system with named stages, caps, and
gates, and it is precise about the part sellers blur: where the
human stays in the loop, and what that human time costs.

## The six stages

Every order moves through the same six stages, in this order:

1. **Intake.** A form, not a chat thread. It collects the inputs
   the build needs and refuses the order politely when a required
   input is missing. A form that accepts anything has automated
   the collection of future support tickets.
2. **Scope check.** A human reads the intake against the package
   exclusions from Lesson 19. This is the cheapest place to catch
   an out of scope order, and the most expensive place to skip.
3. **Build.** A headless run with caps: an allowlist of tools, a
   turn limit, and a budget limit, the Lesson 07 discipline. Caps
   are what make an unattended build safe to repeat.
4. **QA gate.** Defined checks that must pass before delivery.
   Automated where the check is mechanical, human where the check
   is judgement. A failed gate sends the order back to build,
   once by design, and the loop is logged, not hidden.
5. **Delivery.** A fixed pack: what was built, how to use it,
   what is excluded, and when the support window ends.
6. **Support window.** A bounded period for defects in the
   delivered scope. Bounded is the operative word, in writing.

## Where humans stay, and why

The simulation in this lesson counts human minutes per stage, and
the split is deliberate. Intake and build are mostly machine time
with small human touches. Scope check, QA, and support are human
heavy, because each one is a judgement the client is actually
paying for: is this in scope, is this good enough to ship under
my name, is this failure mine to fix.

Automating those three away does not create a scalable business.
It creates an unreviewed one, and Lesson 01's data is the warning:
simple, unaccountable work is the end of the market being priced
down. The pipeline automates the repeatable middle so the human
minutes concentrate exactly where accountability lives.

## The QA bounce is a feature

`pipeline_sim.py` runs three orders through the six stages. One
order, ORD-2, fails QA on its first attempt, returns to build,
and passes on the second. Read the log and the minute totals:
ORD-2 costs 135 human minutes against 90 for a clean order. That
difference is not an embarrassment to average away. It is a real
input to Lesson 20, where capacity math decides how many orders
a week you can honestly sell. A pipeline whose plan assumes zero
bounces has planned to be surprised every week.

Design the bounce in: one return to build inside the quoted
delivery time, a second failure escalates to a human decision,
and the client hears about a delay from you before they discover
it themselves. The gate that never fails is not a gate. It is a
stamp.

## Run it

Run `python3 pipeline_sim.py` and trace ORD-2 through the stage
log by hand. Check that its human minutes equal the clean order
plus one extra build and one extra QA pass. Then run
`python3 smoke_test.py`, which asserts the stage order for every
order, the single QA bounce, and the totals. If you change a
stage minute value, the smoke test totals should move with it.

## Common failures

- **Starting the build before the scope check.** The headless run is fast, which makes it tempting. Fast work on an out of scope order is just a quicker loss, plus a harder refund conversation.
- **A QA gate with no recorded result.** If the gate cannot show what it checked and what failed, Lesson 15's handover has nothing to stand on and the client grades your work alone.
- **Support with no end date.** An open ended window turns every productized order into a small retainer you never priced. State the window at delivery, in the pack, every time.

## Recap checklist

- [ ] I can name the six stages in order and say what each one refuses.
- [ ] I can point to the three stages where human judgement stays, and say why.
- [ ] I have costed one QA bounce into my delivery time and capacity, not just the clean run.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code headless mode and Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [Claude pricing](https://claude.com/pricing)
- [Anthropic Academy](https://anthropic.skilljar.com)
