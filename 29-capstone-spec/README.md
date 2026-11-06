# Lesson 29: Capstone spec: the Lumen Med Spa engagement

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** All of Modules 4 to 8, in particular Lessons 13, 14, 25, and 28 · **You need:** Python 3.11 or newer, and the `capstone/` folder in this lesson. Everything is fictional and runs offline.

The capstone is one complete engagement, simulated end to end.
The client is Lumen Med Spa, a fictional three-location med spa group.
The numbers are a worked example, labelled as one everywhere they appear.
Your job in this lesson is not to build anything.
It is to read the engagement the way a careful practitioner reads it before signing: brief first, discovery second, numbers last, each checked against the others.

## What Lumen is buying

In the client's own framing, kept in `capstone/client_brief.md`: enquiries arrive from Instagram, WhatsApp, and the website, many of them in the evenings and at weekends.
The front desk is stretched across three locations.
The owner wants replies in minutes at all hours, qualification against the real services and price list, bookings written into the diary, and a follow-up sequence for enquiries that go quiet.
That is the system TechAura actually sells, which is why the course uses it as the capstone.
Read the brief in full before continuing. It is short, and every later document answers to it.

## The discovery record

`capstone/discovery_notes.md` records what discovery established, in the client's own statements: channels and volumes as stated, the current response pattern, the value anchor in the client's own framing, and the boundaries and exclusions agreed before pricing.
Discovery notes are not colour. They are the evidence the price stands on.
When a scope line in the brief and a fact in the notes disagree, the engagement is not ready to price, and the disagreement gets resolved in writing, not averaged away.

## The estimator inputs

Before the price, the inputs, because Lesson 13 taught that an estimate is its inputs or it is nothing:

- Human time: 9 hours of your time across discovery, build supervision, QA, and handover. Agents type; these hours are the judgement, review, and client contact an agent does not replace.
- Target rate: $75 an hour, the rate this worked example assumes. Yours comes from your Lesson 00 baseline.
- Plan share: $25, the slice of a monthly plan this engagement is charged with.
- Measured API cost: $20, the figure the headless runs report for work of this shape in this example. Lesson 11 taught the measuring habit; Lesson 30 shows the ledger it lands in.

Those inputs produce the cost floor: 9 times 75 is $675, plus $25, plus $20, for a total of $720.
The floor is what the engagement costs you before any platform fee.
A price below it is a donation, whatever the client calls it.

## The price build-up

The fixed price is built from scope elements, each priced separately, the way Lesson 14 builds:

- Discovery and scope: $250
- Build: $950
- QA and hardening: $300
- Handover and training: $200
- Support window, 30 days: $150

The build-up sums to the fixed price of $1,850.
Gross margin is the fixed price minus the cost floor: $1,850 minus $720 is $1,130, before any platform fee.
On a fee-taking channel that margin is computed again after the fee, using the rates Lesson 01 sourced: Upwork's freelancer fee runs 0% to 15%, and Fiverr keeps 20%.
This engagement is modelled as a direct client, so no fee is applied. State that assumption whenever you quote the margin, exactly as `capstone/engagement.json` does in its assumptions list.

## The spec pack and the checker

The engagement lives in three files under `capstone/`: the brief, the discovery notes, and `engagement.json`, the machine readable spec.
`capstone_check.py` validates the pack the way CI validates this course:

- All three files exist.
- The price build-up sums to the fixed price.
- The cost floor parts sum to the stated total, and the margin is price minus floor.
- Every price element has a matching scope line in the brief, so nothing is priced that the client never agreed to read about.

Run the checker before you open Lesson 30.
A spec that fails its own checker does not get built, in this course or in practice.

## What this lesson is really testing

Not arithmetic. Consistency under reading.
The brief promises, the notes evidence, the JSON computes, and the checker proves the three agree.
Clients rarely test your consistency on purpose. Time, staff changes, and memory do it for them, usually at invoice stage.
The pack is how the engagement survives its own retelling.

## Run it

Read `capstone/client_brief.md` and `capstone/discovery_notes.md` in full.
Then run `python3 capstone_check.py` and read every line of its output.
Finish with `python3 smoke_test.py`, which asserts the whole pack passes.

## Common failures

- **Pricing from the build-up alone.** A build-up without discovery evidence is a list of prices in search of a client; the notes are what make each line defensible.
- **Quoting the margin without its assumptions.** $1,130 before fees, on stated hours and a stated rate, is an honest figure. The same number quoted bare is the genre this course exists to refuse.
- **Letting scope live in the call.** Anything agreed verbally and absent from the brief will be remembered differently by each side. The checker can only protect what is written.

## Recap checklist

- [ ] I have read the brief and the discovery notes, and I can state the value anchor in the client's own framing.
- [ ] I can rebuild the cost floor and the price build-up from memory, with assumptions attached.
- [ ] The checker passes on the shipped pack, and I know which check protects which failure.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Upwork freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
- [Fiverr payment terms](https://www.fiverr.com/legal/payments-terms)
