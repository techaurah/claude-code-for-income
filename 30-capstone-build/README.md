# Lesson 30: Capstone run: build, QA gate, and the honest numbers

**Time:** about 90 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 29 (the checked spec pack) and Lessons 04, 05, 07, and 15 · **You need:** Python 3.11 or newer. The simulation in this folder replays the engagement offline and deterministically.

Lesson 29 ended with a spec that passed its checker.
This lesson runs the engagement against it: the build plan stage by stage, the workflow stack doing the typing, your hours spent where judgement lives, and a QA gate that is allowed to say no.
It ends with the honest numbers, because a build report that hides its ledger is marketing, not delivery.

## The build plan, stage by stage

Five stages, in order, each with a gate before the next begins:

- Stage one, workstation setup for the engagement: a project folder with the brief, the discovery notes, and engagement.json as its memory, plus a CLAUDE.md written for this client and no other.
- Stage two, the build: the response system across the three channels, qualification against the supplied price list, the diary booking step, and the follow-up sequence.
- Stage three, hardening: the edge cases from the discovery notes, out of hours arrivals, opt-outs, clinical questions routed to a human, prices never invented.
- Stage four, the QA gate: the Lesson 15 gate, run in full, recorded in `qa_record.json`.
- Stage five, handover preparation: the pack Lesson 31 assembles and grades.

A stage that fails its gate does not get described as nearly done.
It gets fixed or the engagement stops and the client hears why, in writing, that day.

## Skills used, and why they exist

The build reuses the course's own capital, which is the point of Module 1.
The enquiry handling skill carries the qualification logic.
The scope skill keeps every build decision traceable to a brief line.
The QA skill runs the gate the same way on this engagement as on the last one.
Skills are why the second engagement is cheaper to run than the first, and Lesson 03 priced that effect honestly: cheaper to run, not free, and never a reason to cut the QA stage.

## The subagent split

The build splits the way Lesson 04 teaches: one subagent per channel, working in parallel against the same qualification core, and one reviewer subagent that reads diffs without having written them.
Your hours go to the split itself, to reviewing what returns, and to the decisions the agents are not allowed to make: anything touching price wording, opt-out behaviour, or the human hand-off boundary.
Nine hours of human time was the Lesson 29 estimate for the whole engagement.
The simulation keeps that figure because the run matched it closely enough that changing it would be decoration. Lesson 31's rubric grades that claim.

## Headless runs, with caps

Repetitive build and test work runs headless, the Lesson 07 way: print mode, an allowlist of tools, a turn cap, and a budget cap per run.
Every run reports its own cost in its JSON output, and those reported figures are what the cost ledger records.
Measured, not estimated: the engagement's measured API cost in the ledger is the $20 from the Lesson 29 floor, because the run totals landed on the estimate.
When yours do not land on the estimate, the ledger prints the measured figure and the estimate gets corrected in the open. That correction is the habit Lesson 11 exists to build.

## The QA gate, reported honestly

The gate ran 11 checks. Ten passed.
One failed, and it was the failure this engagement could least afford: the follow-up sequence messaged a test lead who had opted out.
Opt-outs were checked when a lead entered the sequence, not when each message was sent, so a lead who opted out mid-sequence still received the next step.
The fix is a stop-condition check at send time: before any sequence message leaves, the system re-reads the opt-out flag, and a set flag ends the sequence for that lead permanently.
The fix was retested against the same case and the neighbouring cases, and the retest passed.
All of this is recorded in `qa_record.json`, including the failure, because the record is the deliverable's evidence.

Read that paragraph again if it felt uncomfortable.
A gate that has never failed anything is a gate nobody trusts, including you.
The shipped system is safer for having failed in test, on the record, than a fictional clean run would be.

## The simulation

`engagement_sim.py` replays the engagement deterministically.
It walks the five stages, applies the QA record, and refuses to mark delivery ready while any gate check effectively fails.
A check with a recorded fix and a passing retest counts as passed. A check still failing blocks the delivery state, and the simulator says which one and why.
It then prints the final cost ledger, reading the figures from Lesson 29's engagement.json rather than restating them, so the two lessons can never quietly disagree.

## The honest numbers

The ledger, from the engagement file: fixed price $1,850.
Cost floor $720: 9 human hours at $75 is $675, plan share $25, measured API $20.
Gross margin $1,130 before any platform fee, on a direct client, per the printed assumptions.
Nothing in the run changed these figures, and the lesson says so plainly rather than manufacturing a variance to look rigorous.
Your real engagements will vary. The discipline is that the variance gets printed, not absorbed.

## Run it

Run `python3 engagement_sim.py` and read the stage replay, the gate outcome, and the ledger.
Then copy `qa_record.json`, remove the retest from the opt-out check, and run the simulator again: it must refuse the delivery ready state.
Finish with `python3 smoke_test.py`.

## Common failures

- **Treating the gate as a ceremony at the end.** Checks written after the build test what the build happens to do. The gate list comes from the brief and the discovery notes, written before the build starts.
- **Fixing a failure without recording it.** An unrecorded fix leaves no evidence, and the next engagement inherits the bug class with no warning.
- **Restating numbers instead of reading them.** Every copied figure is a future disagreement. The simulator reads Lesson 29's file for exactly that reason.

## Recap checklist

- [ ] I can walk the five stages and name the gate at the end of each.
- [ ] I can explain the opt-out failure, its root cause, and the stop-condition fix, from the record.
- [ ] My simulator run ends delivery ready on the shipped record and refuses a doctored one.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code headless mode and SDK](https://code.claude.com/docs/en/headless)
- [Claude pricing](https://claude.com/pricing)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
