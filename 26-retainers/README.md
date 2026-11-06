# Lesson 26: Retainers: structure, reporting, and renewal

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 25 (the audit) and Lesson 23 (maintenance economics) · **You need:** Python 3.11 or newer. The report builder in this folder runs fully offline.

A project ends. A retainer is the agreement that the system keeps working after it ends.
Clients buy retainers for one reason: someone accountable is watching.
That sentence has to stay true every month, in writing, or the retainer is just a subscription to hope.
This lesson teaches retainer structure, the monthly report as the renewal instrument, and pricing from measured load.

## What a retainer actually sells

A retainer sells vigilance and small, steady improvement.
It does not sell unlimited changes, and it does not sell your evenings.
The client is paying so that drift, breakage, and small opportunities get caught by you before their customers catch them.
Name that plainly in the agreement.
Clients who understand what they bought renew. Clients who bought a vague feeling churn at the first quiet month.

## The defined monthly scope

Write the scope as a list a stranger could check:

- The systems watched, named one by one: the enquiry responder, the qualification flow, the booking hand-off, the follow-up sequence.
- The checks that run, and how often: daily run health, weekly output sampling, monthly prompt and price list review.
- The changes included: small fixes, wording updates, and configuration changes within an agreed monthly allowance.
- The response times you commit to, by severity: what counts as urgent, and how fast you reply in working hours.

Every item on this list should be observable in the monthly report.
If you cannot report it, do not promise it.

## What is explicitly out of scope

The out of scope list is not legal decoration. It is the boundary that keeps the retainer profitable:

- New channels or new systems: those are projects, scoped and priced separately.
- Rebuilds after a client changes their own tooling without notice.
- Content writing, advertising, and anything that was never in the system.
- Emergency cover outside the agreed hours, unless a separate term says otherwise.

`retainer_report.py` enforces this boundary mechanically.
Every delivered item in the activity log carries a scope tag, and the report flags any item whose tag is outside the agreed scope list.
The flag is not an accusation. It is the prompt for a conversation held monthly, in small amounts, instead of yearly, in large ones.

## The monthly report is the renewal instrument

Renewals are rarely decided at the renewal meeting.
They are decided by the pile of monthly reports the client has already read.
A good report is short, factual, and built from the activity log, not from memory:

- Enquiries handled and the response time summary, from the system itself.
- Incidents, what caused them, and what changed so they do not recur.
- Changes shipped, each tied to a client request or a finding of yours.
- Agent run maintenance, with its measured cost, in plain figures.
- Anything delivered outside the agreed scope, flagged by name.
- Next month's watch items, in two or three lines.

Never pad a quiet month.
A month where nothing broke and the numbers held is a good month, and the report should say exactly that.
Padding teaches the client to discount every report, including the important ones.

## Pricing from measured maintenance load

Do not price a retainer from hope, and do not copy a number from another practice.
Price it from the load you measured during the build and the support window:

- Your human hours per month on checks, fixes, and client questions, logged, not remembered.
- The measured API and tool cost of the maintenance runs, from the run output itself.
- A margin for the incidents you cannot schedule, sized from the first months of real data.

**WORKED EXAMPLE, with assumptions printed.** Assumptions: the support window showed 2 hours of human maintenance a month, a target rate of $75 an hour (the capstone rate from Lesson 29, used here for consistency), and $20 a month of measured API cost for maintenance runs. The floor is 2 times 75 plus 20, which is $170 a month. A retainer priced below that floor loses money slowly and politely. What you charge above the floor is a positioning decision, and Lesson 14's value anchor logic applies. This example teaches the method. It is not a market rate and not a promise.

Revisit the price when the measured load changes.
A client whose enquiry volume doubles has doubled part of your load, and the report is where that conversation starts, with numbers both sides can see.

## The Lumen month-one fixture

`lumen_month_one.json` is the activity log for the first retainer month of the capstone client from Lesson 29, Lumen Med Spa.
It is fictional, like the client, and it is deliberately ordinary: two minor incidents, a price list update, steady enquiry volume, and maintenance runs with their costs recorded.
Run the report builder on it and read the output as a client would.
Then ask the only question that matters: would this page make you pay for month two?

## Renewal, handled before it is urgent

Send the report a few days before the renewal date, every month, without exception.
Once a quarter, add three lines: what the system handled in total, what you improved without being asked, and what you recommend next, priced separately if it is project sized.
Clients renew systems that visibly work and visibly improve.
They cancel systems that only become visible when an invoice arrives.

## Run it

Run `python3 retainer_report.py` to build the Lumen month-one report in markdown.
Then edit a copy of the log, tag one change with a scope the agreement never included, and run it again to see the flag.
Finish with `python3 smoke_test.py`.

## Common failures

- **Selling unlimited changes inside a fixed fee.** The first heavy month converts your retainer into the worst paid work you do.
- **Reporting activity instead of outcomes.** Hours and effort are your ledger; enquiries handled, incidents closed, and response times are the client's.
- **Letting out of scope work slide silently.** Unflagged extras become the expected scope, and the next in scope month looks thin by comparison.

## Recap checklist

- [ ] My retainer scope is a checkable list, and every item on it appears in my monthly report.
- [ ] I can build my retainer price from a measured load, with the arithmetic shown.
- [ ] My report flags out of scope delivery by name, monthly, while the amounts are still small.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Anthropic API pricing](https://www.anthropic.com/pricing)
- [Upwork In-Demand Skills 2026](https://www.upwork.com/resources/in-demand-jobs-and-skills)
