# Lesson 25: Automation consulting: the audit as the entry product

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 01, 13, and 14 (the economics, scoping, and pricing habits) · **You need:** Python 3.11 or newer. The scorer in this folder runs fully offline.

Most consulting work dies in the first conversation.
The client describes a vague problem.
You describe a vague system.
Nobody can price a vague thing, so the call ends with goodwill and no work.
The audit fixes that shape.
It is a small, fixed, paid product that turns a vague problem into evidence.
This lesson teaches the audit as the entry product for automation consulting.

## What an audit is, and what it is not

An audit is a bounded diagnostic.
You examine one flow, usually how enquiries arrive, get answered, and become bookings.
You measure what is actually happening.
You report findings with scores, and you recommend next steps with separate prices.
The audit is not a free discovery call stretched over two weeks.
It is not a proposal in disguise.
And it is not a sales document that always recommends buying from you.
A paid audit the client keeps either way is what makes the findings believable.

## Why the audit is paid

Free audits attract the wrong sample.
People accept them because they cost nothing, then read them the same way.
A paid audit filters for a client with a real problem and a real budget.
It also changes your incentives.
When the audit itself is the product, a finding of "do not automate this" is a success, not a lost sale.
That single property is why clients trust the recommendation that follows.

State the price, the scope, and the delivery date before work starts.
One flow. One report. One findings call.
Anything beyond that is a second engagement, priced separately.

## Fixed scope: the shape that protects you

A workable audit scope has five parts, written down before you start:

- The flow under review, named in one sentence.
- The evidence you will gather, and where it comes from.
- The scoring model you will apply, shared with the client in advance.
- The deliverable: one written report plus one walkthrough call.
- The exclusions, stated plainly: no building, no fixing, no tool setup.

If a client asks you to "just fix that one thing while you look", decline inside the audit.
Fixing during diagnosis destroys the evidence and blurs the price boundary.
Note the request. Price it in the recommendations.

## Intake: questions that produce evidence

Intake is six questions, and each one feeds a score:

- Which channels do enquiries arrive on?
- How many enquiries arrive in a typical week, in a band, not a guess at an exact count?
- What share arrives after hours or at weekends?
- How fast is the first human reply today, in a band?
- What happens to an enquiry that goes quiet?
- How does a booking actually get made?

Bands are deliberate.
A client who cannot tell you an exact number can still place the business in a band honestly.
Exact numbers invented to end an awkward pause are worse than an honest band.
`intake_dental.json` in this folder is a completed intake for a fictional dental practice.
Read it before you run the scorer, so you can judge whether the scores match the answers.

## Evidence gathering: sampled, not vibes

Scores built on feelings are decoration.
Where you can, sample the real thing:

- Take the last twenty enquiries on the main channel and time the first replies.
- Count how many received any follow-up after going quiet.
- Walk the booking path yourself, as a stranger would, and count the steps.
- Note which enquiries arrived outside working hours, from timestamps, not memory.

You will not always get full access.
Say so in the report, name which scores rest on client statements alone, and lower your confidence in writing.
A report that marks its own weak evidence is worth more than one that hides it.

## The scored findings report

`audit_score.py` scores six dimensions from 0 to 100:

- Response speed, from the current response time band.
- After-hours coverage, from the share of enquiries arriving when nobody is on duty.
- Follow-up discipline, from what happens when an enquiry goes quiet.
- Booking ease, from how a booking gets made.
- Channel coverage, from how many arrival channels are actually handled.
- Capacity headroom, from weekly volume against a manual process.

The report lists the weakest dimension first.
That ordering is the lesson in miniature: the client reads the worst leak first, while attention is fresh.
The overall score is the mean of the six, nothing fancier.
A single composite number is a summary, never the finding.

## Recommendations priced separately

The report ends with recommendations, and each one carries its own price logic.
Keep three kinds distinct:

- Fix by hand first: a process change that needs no software at all.
- Automate: the system you would build, scoped the way Lesson 13 scopes.
- Do not automate: see below.

The audit fee never silently includes the fix.
If you built the audit price into the build price, say so in writing, or do not do it.
Clients who later discover quiet bundling read every earlier number again, with suspicion.

## When the honest recommendation is "do not automate this"

Some flows should stay manual, and naming them is billable judgement:

- Volume is so low that no system pays for its own maintenance.
- The process changes weekly, so automation would freeze a moving target.
- The real problem is pricing, staffing, or a broken offer, and software would hide it for a month.
- The data the agent would touch is sensitive and the client has no handling practice yet.

Write the reasoning into the report with the same care as a build recommendation.
Clients remember who talked them out of a bad purchase.
That memory is a referral asset no advertisement buys.

## A note on audit pricing

This course does not hand you an audit price, because Lesson 14 already taught you to build one.
Price the audit from your floor: the hours the evidence work honestly takes, at your target rate, plus your measured tool costs.
Then test the figure against the value anchor the client named in intake, in their own framing.
If the two disagree wildly, the scope is wrong, not the arithmetic.

## Run it

Run `python3 audit_score.py` to score the shipped dental intake and print the report.
Then copy the intake, change one answer at a time, and watch which dimension moves.
Finish with `python3 smoke_test.py`, which asserts the scoring bounds and the weakest first ordering.

## Common failures

- **Selling the build inside the audit.** The moment the report reads as a pitch, every score in it is discounted by the reader.
- **Scoring from the sales call alone.** Unsampled impressions produce confident numbers with nothing under them; sample the timestamps or mark the confidence down.
- **Letting the audit absorb free fixes.** Small fixes during diagnosis feel generous and teach the client that scope boundaries are negotiable.

## Recap checklist

- [ ] I can state an audit scope with its exclusions in under a minute.
- [ ] I have run the scorer on the dental intake and can explain each dimension in plain words.
- [ ] I can name two situations where my honest recommendation would be not to automate.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Upwork In-Demand Skills 2026](https://www.upwork.com/resources/in-demand-jobs-and-skills)
- [Upwork freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
