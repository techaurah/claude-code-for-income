# Lesson 27: Selling to teams: security, IP, and contracts

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 14 and 16 (pricing and handover) · **You need:** Python 3.11 or newer. The readiness checker in this folder runs fully offline.

A solo buyer asks what it costs.
A team asks what could go wrong.
The first time a larger organisation considers your work, the questions arrive before the price discussion, and they are not obstacles.
They are the buying process, working as designed.
This lesson teaches the four areas teams ask about, and how to be ready before they ask.
A note on limits first: this lesson is orientation, not legal advice. Contract decisions with real money attached deserve a real lawyer in your jurisdiction.

## Why teams buy differently

An individual buys an outcome.
A team buys an outcome plus protection for everyone whose name touches the decision.
The manager who champions you needs answers they can forward to people you will never meet: a finance lead, an IT reviewer, sometimes a lawyer.
If your answers live only in calls, the deal stalls in rooms you are not in.
Written, checkable answers are a sales asset, not bureaucracy.

## Area one: IP and ownership

The questions, in the order teams ask them:

- Who owns the code you deliver?
- Who owns the prompts, workflows, and configuration?
- Can we maintain this without you?
- Did anything you used carry a licence that limits us?

Answer them in your agreement before they are asked.
A common shape is: the client owns the delivered system and its configuration, you keep ownership of your pre-existing tools and libraries, and each side can use what it owns without asking again.
Whatever shape you choose, write it down.
Verbal IP arrangements survive exactly until the first disagreement.

## Area two: data handling

An enquiry system touches personal data by design: names, contact details, what someone asked about.
Teams will ask:

- What data does the agent read, store, or send anywhere?
- Where does it live, and for how long?
- Which other services process it (your subprocessors, defined below)?

A subprocessor is any third party that processes client data inside your system: the model provider, the messaging platform, the diary tool.
List yours by name, with what each one receives.
If you cannot list them, you do not yet know your own system well enough to sell it to a team.

## Area three: security practice

Nobody expects a small practice to hold enterprise certifications.
Teams expect basic practice, stated in writing:

- Access is per person, with the least privilege each task needs.
- Credentials live in a secrets store, never in code, documents, or chat.
- You can say what happens when something leaks, and who gets told.
- Logs exist, are kept for a stated period, and can be produced on request.

Prepare a one page security note before the first team conversation.
Short, factual, dated. Update it when your practice changes, not when a prospect catches a gap.

## Area four: contract readiness

Team work runs on paper, and the standard shapes are worth knowing by name:

- An MSA, a master services agreement, sets the standing terms once: IP, liability, confidentiality, payment terms.
- A statement of work, often shortened to SOW, sits under the MSA and scopes one engagement: deliverables, dates, price.
- A data processing addendum may join them when personal data is involved.

You do not need all three for a small client.
You need to recognise them, know which parts you can sign as written, and know which parts you will ask a lawyer about.
Never sign liability or data terms you have not read because the start date felt urgent.

## Never start paid work on a verbal yes

This rule has its own section because it ends more small practices than bad pricing does.
A verbal yes followed by changed scope, a departed champion, or a finance team that never heard of you leaves you with work done and no agreement to point at.
The minimum safe start is a written scope with a price, accepted in writing, with a deposit or payment terms stated.
That can be a one page SOW or a signed proposal. It cannot be a call recording and optimism.

## The readiness checker

`readiness_check.py` scores four areas from a JSON of answers.
Each question is answered yes, partial, or no.
Yes scores 1, partial scores 0.5, no scores 0.
An area at 80 percent or above reads as ready, 50 to 79 as gaps to close, and below 50 as not ready.
The checker prints the gaps by name, because a score without its gaps is a poster, not a tool.
Run it on `readiness_example.json`, the worked state of a practitioner who is close but not ready, and read the gap list as a to do list.

## Walk in with the file already built

The strongest move in a team sale is boring: prepare the pack before the meeting.
One page on ownership. One page on data and subprocessors. One page on security practice. Your standard terms.
When the questions come, you send documents the same day.
Speed here is not pressure. It is evidence that the delivery will feel like this too.

## Run it

Run `python3 readiness_check.py` to score the example answers and print the gaps.
Then copy the file, answer it honestly for your own practice, and run it again.
Finish with `python3 smoke_test.py`.

## Common failures

- **Treating written answers as friction.** Every unanswered security question is a week added to the sales cycle, usually spent by your champion guessing on your behalf.
- **Starting on a verbal yes to look easy to work with.** Easy to start and impossible to invoice is the worst combination in contracting.
- **Promising certifications or controls you do not have.** A false answer found in diligence ends the deal and the referral chain behind it.

## Recap checklist

- [ ] I can state who owns the code, the prompts, and the configuration in my standard engagement.
- [ ] I have a written subprocessor list for a typical system I sell.
- [ ] My start rule is written down: no paid work without an accepted written scope and price.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Anthropic privacy policy and data handling](https://www.anthropic.com/legal/privacy)
- [OWASP top ten for LLM applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [SPDX licence list](https://spdx.org/licenses/)
- [GitHub documentation](https://docs.github.com)
