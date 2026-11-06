# Lesson 22: Build and ship: a real product cadence with agents

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 21 (a problem that survived), Lessons 04 and 09 (subagents and worktrees) · **You need:** Just the lesson files. The plan generator runs offline on a JSON feature list.

A solo builder with agents does not need more hours. They need a
cadence that survives contact with reality: a frozen scope, a
thin slice running end to end before anything is polished, gates
at the end of each week that mean something, and a written answer
to what gets cut when a week slips. This lesson builds that
cadence as a four week plan shape you can generate, inspect, and
argue with before a single feature is written.

## Week zero is a decision: the scope freeze

Before week 1, the feature list stops moving. New ideas go on a
later list, in writing, where they can be good without being
urgent. A freeze is not a lack of ambition. It is the only way
the words "week 3" mean anything, and it is the solo builder's
substitute for the roadmap meeting a team would hold. Lesson 21
killed problems cheaply. The freeze kills features cheaply, for
the same reason: after the build starts, every change costs ten
times the argument it would have cost on paper.

## The thin slice first, riskiest first

Week 1 builds the thin end to end slice: the smallest path that
takes a real user from sign-in to the product's core outcome,
rough edges visible and allowed. Inside the slice, and inside
every week, work is ordered risk first. `ship_plan.py` sorts
slice features ahead of the rest and highest risk ahead inside
each group, so the fixture puts the core booking flow and the
reminder sender at the top of week 1, where a nasty surprise
still leaves three weeks to answer it. Risk discovered in week 4
is not a discovery. It is a delay announcement.

In the fixture, the slice fills week 1 exactly at capacity, the
remaining features settle into weeks 2 and 3, and week 4 carries
no new features at all. That empty week is the plan working:
hardening, the ship checklist, and a rehearsed rollback live
there, and they need the room the greedy schedule did not eat.

## The human and agent split, per week

The generator labels each feature agent work or human work, and
the split follows accountability, not typing speed. Agents take
bounded implementation, tests, migrations, and drafts inside the
frozen scope, in worktrees, with the Lesson 05 guardrails on.
Humans keep integration judgement, anything touching billing
correctness, the final review of risk-first features, and every
gate decision. If a feature marked human work is quietly handed
to an agent to catch up, the plan has not sped up. Its risk has
moved somewhere unrecorded.

## Weekly gates and the cut rule

Each week ends at a gate: slice runs end to end, riskiest
remaining feature works on real data, billing and edge cases
pass with a support path, ship checklist green with rollback
rehearsed. A failed gate does not move the deadline by hope. It
fires the cut rule: the lowest risk, non-slice feature in the
overloaded week is named by the generator and leaves the release,
joining the later list from the freeze. Cutting the riskiest
work feels brave and ships a hollow product. Cutting the
polish is how the core survives its own schedule.

## Run it

Run `python3 ship_plan.py` and check week 1 by hand: slice only,
riskiest first, at capacity. Then add a large feature to a copy
of `features.json` until a week overloads, and read the cut
suggestion the generator prints. Then run
`python3 smoke_test.py`, which asserts the ordering, the gates,
and the overload flag with its cut.

## Common failures

- **Polishing week 1.** A beautiful slice that only runs on your machine has proven the least risky thing available. Rough and end to end beats polished and partial, every single week.
- **Letting the freeze thaw quietly.** Each silent addition feels small. Together they are the reason week 4 has no room for the rollback rehearsal, discovered during the rollback.
- **Cutting risk to save the date.** Removing the hard core to ship on time gives you a punctual launch of a product that does not do the thing. Cut polish, protect the slice.

## Recap checklist

- [ ] My feature list is frozen in writing, with a later list beside it.
- [ ] Week 1 is a thin end to end slice, riskiest feature first, at or under capacity.
- [ ] I know which feature gets cut first when a gate fails, before any gate has failed.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [GitHub documentation](https://docs.github.com)
- [Anthropic Academy](https://anthropic.skilljar.com)
