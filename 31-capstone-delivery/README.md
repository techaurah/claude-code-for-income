# Lesson 31: Capstone delivery: the pack and the self-grading rubric

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 29 and 30, plus Lesson 16 (handover) and Lesson 26 (retainers) · **You need:** Python 3.11 or newer. Everything in this folder runs offline.

The engagement is built and the gate has spoken.
What the client keeps is not the build session. It is the pack.
This final lesson assembles the delivery pack for the Lumen Med Spa engagement, then grades it against a rubric, in the open, before you read the worked solution.
Grade your own work first. That order is the course's last honesty habit, and it is deliberate.

## What a delivery pack is

A delivery pack is the set of documents that lets the client own what they bought:

- The brief, unchanged, so delivery can be checked against the client's own words.
- The discovery record and the agreed scope.
- The system itself, with its handover notes and runbook.
- The QA record, failures and fixes included.
- The cost ledger, with assumptions printed.
- The support terms, and what happens when the window ends.

If a stranger at the client's business opened the pack in six months, they should be able to run the system, explain its limits, and find who to call.
Anything less is a handover that depends on your memory, and your memory is not a deliverable.

## Assembling the pack from the spec

`delivery_pack.py` generates the pack checklist from Lesson 29's engagement.json.
Every element of the price build-up becomes a deliverable line, with its evidence file and its pack status.
Generating the checklist from the spec matters: a typed checklist can quietly drop the element that ran late.
A generated one lists what was priced, and the pack must answer for each line or visibly fail to.

The five lines, matching the build-up you already know: discovery and scope at $250, build at $950, QA and hardening at $300, handover and training at $200, and the 30 day support window at $150, inside the $1,850 fixed price from the worked example.
Nothing new is priced here. Delivery accounts for the price; it never revises it.

## Handover is a transfer, not a send

Lesson 16 taught the shape and the capstone follows it: a walked session with the client's team, the limits stated out loud (clinical questions go to humans, opted out leads are never messaged, prices come only from their list), and the take-over path practised while you are still in the room.
The pack records that the session happened.
A runbook nobody has opened during training is a file, not a handover.

## The rubric: six criteria, graded on evidence

`rubric.md` in this folder is the grading instrument. Six criteria:

- Scope fidelity: did the pack deliver the brief, line by line?
- Price integrity: can the price be rebuilt, with assumptions attached?
- QA evidence: does the record show checks, failures, fixes, and retests?
- Handover completeness: can the client run this without you?
- Honesty of numbers: is every figure sourced, dated, or labelled a worked example?
- Support readiness: does the client know what happens when something breaks?

Each criterion scores 0 to 3 against written descriptors.
Grade the evidence in the pack, not the effort and not the intention. A criterion with no evidence in the pack scores 0, however good the work behind it was.
`rubric_score.py` applies the weights and returns a verdict band: ship it at 85 percent or above, fix and reship from 60 to 84, redo below 60. It refuses scores outside 0 to 3, because a rubric you can overflow is a mood.

## Self-grading, honestly

Grade before you open the solution. Write the scores down. Then read the worked grading and argue with it where your evidence reading differs.
Two habits are being trained here.
The first is grading down: the capstone pack has real weaknesses, and a self-grade of straight 3s says more about the grader than the pack.
The second is naming the fix that follows from the grade. A fix and reship verdict is not a failure state. It is the normal end of a first pack, and the rubric tells you which criteria to fix instead of inviting a general redo of everything.

## What happens after delivery

The support window runs for 30 days on the terms in the pack.
Then the Lesson 26 retainer conversation begins, with the month-one report as its instrument, the way the fixture in that lesson models for this same client.
The course ends where a practice continues: a system in a client's hands, a record both sides trust, and a monthly report that will either renew the relationship or honestly end it.

## Run it

Run `python3 delivery_pack.py` and check every priced element appears in the checklist.
Write your grades into a JSON file, one score per criterion, and run `python3 rubric_score.py your_grades.json` before opening the solution.
Finish with `python3 smoke_test.py`.

## Common failures

- **Grading the work instead of the pack.** The client, the showcase reviewer, and future you all meet the pack, not the build session.
- **Writing handover notes for yourself.** Notes in your shorthand fail the six month stranger test; write for the client's team, in their words where the brief gave them.
- **Treating the rubric as a ceremony after shipping.** The pack ships after the grade. A redo verdict discovered post-delivery is a client conversation, not a rubric entry.

## Recap checklist

- [ ] My pack checklist is generated from the spec and accounts for every priced element.
- [ ] I graded all six criteria from evidence, in writing, before reading the solution.
- [ ] My verdict names the specific criteria to fix, or honestly says ship it.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [GitHub documentation](https://docs.github.com)
- [Anthropic Academy](https://anthropic.skilljar.com)
