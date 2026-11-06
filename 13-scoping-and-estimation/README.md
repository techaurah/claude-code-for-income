# Lesson 13: Scoping and estimation when an agent does the typing

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 12 · **You need:** Python 3.11 or newer and notes from one real or realistic discovery conversation.

An agent makes the typing fast. It does not make the
work simple, and it does not make estimation optional.
Most freelance losses are not coding losses. They are
scope losses: work that was never named, never priced,
and never excluded, delivered anyway because saying no
mid project feels harder than absorbing it.

This lesson builds the estimate the rest of Module 4
runs on: a work breakdown that splits agent time from
human time, buffers by uncertainty, and draws scope
boundaries a client can read before anyone signs.

## Discovery questions that scope the work

Estimation starts in discovery, and discovery is a set
of questions with a purpose. Ask these, and write the
answers down where the estimator can use them.

What happens today when this problem occurs, step by
step? What systems must the build touch, and who owns
access to each? What does a correct result look like,
and who decides it is correct? What is explicitly not
wanted? What happens if this is not built at all, and
what does that cost, in the client's own words?

That last answer becomes the value anchor in Lesson 14.
The access answer decides half your risk before you
write a line. A build that depends on a system nobody
can give you access to is not a build. It is a delay
with a price attached.

## Split agent time from human time

The central discipline of this lesson is the split.
Every task carries two numbers, not one.

Agent hours are machine time: drafting, generating,
first pass implementation, bulk changes. They matter
for scheduling and for token cost. They are not what
the client is mainly paying for, and they compress as
your workflows improve.

Human hours are your time: discovery, design decisions,
review, judgement calls, testing against reality, client
handling, and handover. They do not compress at the same
rate, because review and accountability do not speed up
just because generation did. Price and promise on the
human number. Report the agent number for planning.

An estimate that merges the two lies in both directions.
It overstates the human effort the client should fund,
and understates the review load that will actually land
on your week.

## Risk buffers by uncertainty class

Not all human time is equally predictable. The estimator
in this lesson classes each task and buffers the human
time only, because that is where variance lives.

Low uncertainty adds 10 percent: the work is known, the
system is accessible, the result is easy to check. Med
adds 25 percent: a real unknown exists but it is bounded.
High adds 50 percent: an external system, a vague
requirement, or a decision maker who has not yet decided.

Buffers are not padding to be negotiated away in the
room. If a client wants a lower price, the honest lever
is lower scope or lower uncertainty: give access earlier,
decide the open question, cut a task. A buffer removed
by pressure returns as unpaid overtime with good
attendance.

## Scope boundaries and exclusions

Every scope names its edges in writing. Included tasks,
by name. Excluded work, by name: new channels, new
locations, data migration, content writing, anything the
buyer mentioned once and you are not delivering.

Exclusions feel awkward for about one minute in a sales
conversation. Their absence feels worse for weeks during
delivery. Lesson 15's QA gate checks the delivered scope,
and Lesson 16's handover restates the boundary as support
terms. Both are easier when this lesson did its job.

Revision rounds belong here too, as a counted thing.
Two rounds of revisions on the delivered scope is a
scope statement. Unlimited revisions is not generosity.
It is an unpriced second project hiding inside the first.

## WORKED EXAMPLE: the Lumen build

Assumptions box. Fictional client: Lumen Med Spa, a
three location med spa group. Target rate $75 an hour.
This is a worked example, not platform data.

The shipped fixture, `lumen_scope.json`, breaks the
enquiry response build into four tasks. Discovery and
enquiry mapping: 1 agent hour, 2 human hours, low.
Enquiry handler build: 6 agent hours, 3 human hours,
med. Booking integration: 4 agent hours, 2 human hours,
high, because an external calendar decides its shape.
QA, docs, and handover prep: 2 agent hours, 2 human
hours, low.

Totals: 13 agent hours and 9 human hours. Buffers add
2.15 human hours, giving 11.15 human hours with buffer
and a total range of 22.0 to 24.15 hours. Lesson 14
prices the 9 human hours, not the range, and keeps the
buffer as your protection rather than the client's bill.
Human time 9 hours at $75 is $675. Remember that figure.
It is the first line of the cost floor next lesson.

## Run it

Run `python3 scope_estimator.py` on the shipped fixture
and check the totals against this lesson. Then write a
scope JSON for a job of your own, with the split and a
class per task. Then run `python3 smoke_test.py`.

## Common failures

- **Estimating one merged number per task.** A merged number hides the review load, and the review load is the part that lands on you. Split every task, every time.
- **Buffering agent time instead of human time.** Agent variance is mostly token cost, which Lesson 11 measures in dollars. Human variance is your week, and that is what the buffer protects.
- **Leaving exclusions for the contract stage.** By then the buyer has already imagined the excluded work as included. Name exclusions in the scope itself, while expectations are still cheap to set.

## Recap checklist

- [ ] My scopes split agent hours from human hours on every task.
- [ ] Every task carries an uncertainty class, and buffers follow the 10, 25, 50 rule on human time.
- [ ] My scope documents name exclusions and a counted number of revision rounds.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Upwork freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
- [Fiverr payment terms](https://www.fiverr.com/legal/payments-terms)
