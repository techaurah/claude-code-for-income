# Lesson 16: Handover: documentation, training, and the rehire

**Time:** about 50 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 15 · **You need:** Python 3.11 or newer and the QA record from a real or fixture delivery.

Most projects end with a zip file and a thank you. Well
run projects end with a pack: documents that let the
client operate what they bought, train their people, and
understand exactly what support they have. The pack is
also, not by accident, the most reliable source of the
next engagement.

Handover is not admin after the real work. For the buyer,
handover is the moment the work becomes theirs. Treat it
with the same discipline as the build.

## The handover pack: five sections

A complete pack answers five questions, in this order.

What was built: the deliverables, named as the client
names them, mapped to the scope from Lesson 13. How to
run it: start, stop, check health, read the logs, the
daily operations a non developer can own. How to change
it: the safe changes, where they live, what to test after
each, and which changes are not safe to attempt without
you. Support terms: the window, what counts as a defect,
what counts as new scope, and how to reach you. The next
problem: named in the final section, in the client's own
terms where you have them.

`handover_pack.py` generates that document from a JSON
project record and runs a completeness check over it. A
pack missing a section says so, by name, before it ships.
Ship the completeness result with the pack, next to the
QA record from Lesson 15. Together they are the delivery
evidence a serious buyer keeps.

## Documentation a client can actually use

Write for the person on duty, not for yourself. Short
steps. Exact commands and file names. What good looks
like after each step, so the reader can tell success from
failure without asking anyone.

Keep two layers apart. The runbook is operations: run,
check, restart, escalate. The change guide is judgement:
what may change, what must not, and what a change can
break. Merging them produces a document that is too
dangerous for operations staff and too shallow for
anyone making changes.

The shipped fixture is the Lumen Med Spa record: a three
location med spa group, fictional, taking delivery of the
enquiry response system built across this module. Read
its change guide closely. It names the safe edits, config
for hours and prices, the handoff list, and it names the
test step that must follow. That specificity is the
standard.

## The training session

Documents alone do not transfer confidence. Run one live
session, about an hour, with the people who will operate
the system, and structure it tightly.

Walk the main flow end to end on their data. Hand over
the controls early and let them run the second pass while
you watch. Break something small on purpose, in a test
setting, and let them recover it from the runbook. Close
with the boundaries: what support covers, how to ask,
and what response time to expect.

Record the session if the client agrees, and file it with
the pack. Questions asked in training are a free audit of
your docs: every repeated question marks a paragraph that
needs rewriting before the next delivery.

## The 30 day support window

Offer a defined window, 30 days in this course's standard
pack, for defects in the delivered scope. A defect is the
system failing to do what the scope and QA record say it
does. A new channel, a new location, and a new feature are
not defects. They are the next scope, priced by Lesson 14.

Boundaries stated kindly at handover save hard
conversations later. Log support requests against the
scope, reply within the time you promised, one business
day in the fixture terms, and close the window with a
short written summary: what was asked, what was fixed,
what remains open by agreement.

A support window run this way builds the reference and
the review. Run loosely, it becomes unpaid maintenance
with no end date, which is how good delivery practices
quietly lose their margin.

## Engineering the rehire

The next problem section is not a pitch. It is an honest
observation, earned during delivery, about the problem
this build exposed or left adjacent.

In the Lumen record, the next problem is no shows after
booking, named by the follow up data from this very build,
with a reminder sequence as the natural next engagement.
That is the shape to copy: observed, specific, and left
for the client to raise. Name it once, in the pack, and
once more when the support window closes. Then stop.

Rehire engineering fails when it becomes pressure. A
client who feels sold at handover discounts the pack, the
training, and you. A client who feels understood calls
when the named problem starts costing money, and by then
your pack has already written the first paragraph of the
next scope.

## Run it

Run `python3 handover_pack.py` to generate the Lumen
handover from its record and check its completeness.
Then run it on a record with sections removed and read
the missing section report. Then run
`python3 smoke_test.py`.

## Common failures

- **Handing over a zip file with no runbook.** The client now owns a system they cannot operate, and every question returns to you unpaid. The pack is the product at this stage.
- **Support terms with no boundary between defect and new scope.** Without that line, the window absorbs a second project. State it at handover, while goodwill is highest.
- **Turning the next problem into a pitch deck.** One observed problem, named plainly, outperforms a sales section. Pressure at handover taxes every future conversation.

## Recap checklist

- [ ] My handover packs contain all five sections, with a completeness check saved beside the QA record.
- [ ] I run a live training session that includes a guided recovery from the runbook.
- [ ] My support terms define the window, the defect boundary, and the response time in writing.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Upwork freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
- [Fiverr payment terms](https://www.fiverr.com/legal/payments-terms)
