# Lesson 15: Delivery QA: the review discipline that protects your rate

**Time:** about 55 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 13 and Lesson 14 · **You need:** Python 3.11 or newer. The fixture delivery folder in this lesson passes the gate as shipped.

A client cannot read your intentions. They can read what
you ship. Delivery QA is the discipline that makes what
you ship match what you promised in Lesson 12, scoped in
Lesson 13, and priced in Lesson 14.

Treat the QA gate as a product feature, not a private
chore. Clients at the complex end of the market pay for
accountability. A recorded gate they can inspect is
accountability with a file name.

## Definition of done, written before the build ends

Done is a list, written when scope is agreed, not a
feeling at midnight before delivery. A useful definition
of done for agent built work names five things.

The delivered scope matches the scope document, task by
task. The main flows work on the client's kind of data,
not only on your happy path examples. Tests exist for
the behaviour the client depends on, and they pass. No
secret, key, or client data sits in the delivery. The
docs a non developer needs are present and current.

If an item cannot be checked, it is not part of done.
Rewrite it until it can be, or move it out of scope.

## Diff review discipline

The agent writes fast. Your review is the rate limiting
step, and it is supposed to be. Review the diff, not the
agent's summary of the diff. Summaries describe intent.
Diffs describe reality, including the file the agent
touched for reasons it did not mention.

Read in this order. Behaviour changes first, in the code
paths the client will actually exercise. Then new
dependencies and configuration, where supply chain and
secrets risk live. Then tests, checking that they test
behaviour and would fail if the behaviour broke. Then
docs, last, because docs written before review tend to
document the plan instead of the result.

Anything you do not understand does not ship. Ask the
agent to explain it, shrink it, or remove it. Code you
cannot explain to the client is code you cannot support
in Lesson 16's window.

## Test evidence, not test theatre

Evidence is output a third party can re-run: the test
command, the result, the date, the environment in one
line. Theatre is a sentence saying tests pass.

Record the gate result per delivery and keep it with the
client pack. When a client asks, six weeks later, whether
a behaviour was covered, the record answers in seconds.
When a dispute starts, and one eventually does, the record
is the difference between a conversation and an argument.

The artifact in this lesson produces a small version of
that record: JSON, pass or fail per check, ready to file
with the pack from Lesson 16.

## Secret scanning

Agent assisted work raises a specific leak risk. Keys get
pasted into examples. Config files get copied into docs.
A test fixture quietly contains a real credential.

Scan every delivery folder for common secret shapes
before it leaves your machine: provider key prefixes,
cloud access key shapes, private key headers, and lines
that assign a value to a key, secret, or password field.
The scanner in `qa_gate.py` is a first pass, not proof of
safety. It catches the common shapes cheaply, and a clean
scan plus your own read of config files is a defensible
habit. A hit stops delivery. No deadline argument outranks
a leaked client key.

## Docs check and the gate record

Docs fail in a predictable way: they describe an earlier
version. The gate therefore checks presence mechanically,
required files present, a README present, code compiling,
and you check currency by reading the runbook against the
final build once, as the last review step.

Run the gate. Save the JSON record with the delivery.
If the gate fails, fix the delivery, not the gate. A gate
that gets edited until it passes has recorded one thing
accurately: that it is no longer a gate.

## The fixture, and breaking it on purpose

The `fixture/` folder in this lesson is a small delivery
that passes: required files present, one Python file that
compiles, no secret patterns. The exercise copies it and
breaks it deliberately, so you can watch the record change
from pass to fail and learn what a failing record looks
like before a real client delivery depends on it.

That rehearsal matters. The first failing gate of your
practice should happen in a lesson, not in a delivery
thread at the end of a paid week.

## Run it

Run `python3 qa_gate.py` and read the JSON record for the
fixture. It should pass every check. Then run
`python3 smoke_test.py`, which also verifies that a copy
with a fake key fails the secret scan.

## Common failures

- **Reviewing the summary instead of the diff.** The summary is the agent's account of itself. The diff is the delivery. Only one of them reaches the client.
- **Recording that tests pass without the evidence.** A claim ages badly and cannot be re-run. File the command and its output, or the gate has no memory.
- **Weakening the gate under deadline pressure.** The gate exists for exactly the days when pressure argues against it. Fix the delivery, extend the deadline, or narrow the scope.

## Recap checklist

- [ ] My definition of done is written, checkable, and agreed before delivery pressure arrives.
- [ ] I review diffs in order: behaviour, dependencies and config, tests, then docs.
- [ ] Every delivery leaves with a saved gate record, including its secret scan result.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Python py_compile documentation](https://docs.python.org/3/library/py_compile.html)
- [Upwork freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
