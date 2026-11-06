# Lesson 19: Packaging: the pricing page and the promise you can keep

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 18 (the pipeline the page must describe honestly) and Lesson 14 (your cost floor) · **You need:** Just the lesson files. The page renderer and validator run offline.

A pricing page for a productized service is not marketing copy
with numbers attached. It is the contract's front door: the
named outcome, what is included, what is excluded, how many
revision rounds, how long delivery takes, and how long support
lasts. A buyer who can answer all six from the page alone will
argue with you less, refund less, and refer better, because the
disappointments were priced and printed before money moved.

## The six parts of a package

- **Named outcome.** One sentence, in the buyer's language.
  Every new enquiry answered within minutes is an outcome. AI
  chatbot installation is a task, and tasks invite comparison
  with everyone else's tasks.
- **Inclusions.** The short list the pipeline in Lesson 18
  actually delivers. If a line is not in the pipeline, it does
  not go on the page, however well it would sell.
- **Exclusions.** At least one, explicit, and in this course the
  renderer enforces it. Exclusions are not legal small print.
  They are the scope boundary the buyer deserves to see before
  paying, and the line your scope check enforces later.
- **Revision rounds.** A number. Two is a design decision, not
  stinginess: it forces feedback to arrive gathered instead of
  dripping, and it tells the buyer their review time is part of
  the system.
- **Delivery time.** Stated in days, and built from the pipeline
  including one QA bounce, not from the clean run.
- **Support window.** A bounded period for defects in scope.
  Unbounded support is a retainer you forgot to price.

## Tiering without fake tiers

The fixture ships one package and one optional add-on, and that
shape is the lesson. The classic three tier ladder, where the
middle tier exists to make the top tier look reasonable and the
bottom tier exists to be ignored, is pricing theatre. It works
on buyers once and teaches them to distrust the page.

Tier when the work genuinely differs: a second location is a
real add-on for Lumen Med Spa because the pipeline repeats with
different settings. Do not tier by loosening adjectives. If you
cannot describe the difference as different pipeline work, you
do not have two packages. You have one package and a markup.

## Guarantee language you can honour

A guarantee is a promise about your behaviour, never about the
client's results. The renderer prints the course's pattern:
miss the stated delivery time or ship an item that fails its
agreed check, and you fix it inside the support window at no
extra charge. Cannot fix it, and you refund the fee for that
package. Bookings, revenue, and growth are never guaranteed,
because they depend on the client's offer, prices, and market,
none of which your pipeline controls.

Notice what this language costs you. Very little, if the QA gate
is real, and it buys the one thing vague pages cannot: a buyer
who knows exactly what happens when something goes wrong, which
is the moment trust is actually decided.

A note on price itself: any figure you place on your page comes
from your Lesson 00 baseline and your Lesson 14 cost floor, after
platform fees where a channel takes one (Upwork 0% to 15%,
Fiverr keeps 20%, checked October 2026). The fixture carries no
market price, on purpose. It carries a note telling you to set
yours, because a copied price is a worked example you forgot to
label.

## Run it

Run `python3 package_page.py` and read the rendered page as a
buyer would: can you find the outcome, the exclusions, and the
end of support in one pass? Then delete the exclusions from one
package in a copy of `packages.json` and watch the render refuse,
with reasons. Then run `python3 smoke_test.py`.

## Common failures

- **Exclusions written as apologies.** "We sadly cannot offer phone cover" invites negotiation. "No out of hours human phone cover" is a boundary. Same fact, different contract.
- **A support window that starts at purchase.** The window covers defects after delivery. Starting it at purchase lets a slow intake quietly burn the help the buyer paid for.
- **Guaranteeing an outcome the client controls.** The first refund demand written in your own guarantee's language ends the debate about whether results language was worth it.

## Recap checklist

- [ ] My package page states outcome, inclusions, exclusions, revisions, delivery time, and support window, all findable in one read.
- [ ] Every tier or add-on I offer maps to genuinely different pipeline work.
- [ ] My guarantee promises my fix or refund behaviour, and no business result.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude pricing](https://claude.com/pricing)
- [Fiverr's payment terms](https://www.fiverr.com/legal/payments-terms)
- [Upwork's freelancer fee schedule](https://support.upwork.com/hc/en-us/articles/211062538-Freelancer-Service-Fees)
