# Lesson 28: Failure modes and ethics: staying in business

**Time:** about 70 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 15 and 27 (the QA gate and team readiness) · **You need:** Python 3.11 or newer. The pre-mortem generator in this folder runs fully offline.

Most agent practices do not die from bad code.
They die from a trust failure, a terms breach, or a slow leak nobody priced.
This lesson is the failure catalogue, taught as plainly as the wins elsewhere in the course.
Each failure comes with the control that prevents it.
The controls are cheaper than the failures. That is the entire argument.

## How to use this catalogue

Read it as a pre-mortem: before a project starts, assume it failed, and ask which of these did it.
`pre_mortem.py` in this folder generates that register from a project description, seeding the risks that match the project's shape.
Owner and control fields are left for you to complete, because a risk register nobody owns is a diary.

## Failure one: undisclosed agent work

The client believed the work was manual. It was not, and they found out from someone else.
The damage is not the method. Plenty of clients happily buy agent-assisted delivery.
The damage is the discovery, which rewrites every past deliverable as a possible deception.
Control: disclose the method in the proposal, in one plain sentence, before money moves.
Price and QA carry the value story. Secrecy carries nothing worth keeping.

## Failure two: IP contamination

Agent output can resemble its training data, and pasted code can carry someone else's work into a client's codebase.
The risk shows up as near-duplicate snippets, copied comments, or a function that matches a known project closely enough to matter.
Control: review agent output as untrusted code, check shipped code for suspicious matches, and keep the licence question from Lesson 27 in every review.
You are accountable for what you ship, whatever typed it.

## Failure three: licence violations in shipped dependencies

An agent adds a library because it fits. Its licence may not.
Copyleft terms, non-commercial weights, and attribution duties have all ended up inside client systems this way.
Control: keep a dependency list per project, check each licence before delivery, and pin what you ship.
The check takes minutes. The remediation conversation takes weeks.

## Failure four: platform terms breaches

Marketplaces have terms about how work is sourced, communicated, and paid for.
Model providers have terms about acceptable use and about routing their service through other tools.
Breaking either can cost the account, and the account is the business.
Control: read the terms of every platform you depend on, re-read them when they change, and never build a workflow whose survival requires a breach.
If a client's request needs one, the request is the failure, and you decline it in writing.

## Failure five: scope creep disguised as revisions

Revision rounds are for fixing what the scope promised.
Creep arrives wearing the same clothes: a new channel described as a tweak, a new report described as a correction.
Each silent yes reprices your work downward and retrains the client's expectations.
Control: the Lesson 26 habit, applied during projects. Flag out of scope items by name when they arrive, price them kindly, and let the client choose.
Most clients choose fine. What they resent is the surprise invoice, not the boundary.

## Failure six: single-client dependence

One client at most of your income feels like success until they pause, churn, or get acquired.
Then their budget meeting becomes your emergency.
Control: watch the share. When one client passes a third of your income, treat winning the next client as your main project.
Diversification is slow, which is why it starts before it is urgent.

## Failure seven: the commodity trap

Lesson 01's data, returning as a failure mode: simple generative work saw contract starts rise about 90 percent while earnings per contract fell about 13 percent (Upwork Future Workforce Index, as reported; the limits from Lesson 01 travel with the figures).
Selling what everyone can now supply is a race you win by getting cheaper.
Control: keep moving your offer toward the complex end: integration, accountability, reporting, and the QA evidence a commodity seller cannot show.

## The failure underneath the others

Every failure above has the same root: a gap between what the client believes and what is true.
Undisclosed methods, unowned code, unflagged scope, an income story resting on one client.
The controls share a shape too: write the true thing down, early, where the client can read it.
Ethics in this course is not a mood. It is that paperwork habit, kept when it costs you something.

## When not to automate: the standing answer

Some requests should be refused even when they are legal and profitable:

- Automating deception: fake reviews, undisclosed synthetic outreach presented as human, engagement that imitates people.
- Automating contact with people who opted out, under any framing.
- Building a system whose logs the client intends to hide from their own customers or staff.

Refusing in writing, with a reason, protects you twice.
It ends the request, and it creates the record that you ended it.

## Run it

Run `python3 pre_mortem.py` to generate the risk register for the example project in this folder.
Read which risks were seeded and which were not, and check the seeding against the project's channels, data, and deliverables.
Finish with `python3 smoke_test.py`.

## Common failures

- **Treating disclosure as a pricing risk.** The disclosed practitioner keeps the client who finds out. The undisclosed one keeps nothing.
- **Checking licences at the end.** Licence problems found at delivery have no cheap fixes left; the check belongs at the moment a dependency is added.
- **Writing a risk register once and framing it.** Risks change when the project does. Regenerate the register at every scope change.

## Recap checklist

- [ ] My proposals disclose agent-assisted delivery in one plain sentence.
- [ ] I can produce a dependency and licence list for my current project.
- [ ] I have a written line I will not cross, and a refusal I could send today.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Anthropic acceptable use policy](https://www.anthropic.com/legal/aup)
- [SPDX licence list](https://spdx.org/licenses/)
- [Upwork terms of service](https://www.upwork.com/legal)
- [Fiverr terms of service](https://www.fiverr.com/legal/terms_of_service)
- [OWASP top ten for LLM applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
