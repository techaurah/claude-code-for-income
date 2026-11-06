# Lesson 03: Skills as capital: a library that sells twice

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 02 and at least one workflow you have repeated on three real jobs · **You need:** Python 3.11 or newer. The audit tool runs offline on any folder of skills.

A skill is a packaged folder of instructions that Claude Code loads when a task matches its description.
At its heart sits a SKILL.md file.
Around it can sit scripts, checklists, and reference files.
Lesson 02 built memory.
This lesson builds reusable procedure.
Memory says how you work in a project.
A skill says how a whole job gets done, in any project.

## Why call it capital

Capital is something you build once and use many times.
A good skill fits that shape exactly.

- You write the procedure once, while it is fresh.
- You reuse it on the next job at almost no extra effort.
- You improve it after each use, so the next use is better.
- You can deliver with it, and later you can sell the library itself.

That last point is the "sells twice" idea in the title.
First the skill makes client delivery faster and more consistent.
Then, packaged with care, the same library can become a product for other practitioners.
Neither step is a promise.
Both steps depend on the skill being genuinely useful, job after job.

## The anatomy of a SKILL.md

A SKILL.md has two parts.

- **Frontmatter.** Machine read fields at the top, including `name` and `description`.
- **Body.** The procedure itself, written for an agent to follow.

The `name` should be short, lower case, and hyphenated.
The `description` is the most important line in the file.
It is the trigger.
Claude Code decides whether to load the skill by reading it.
A vague description means a skill that never fires, or fires at the wrong time.

## Writing a description that triggers well

A good description does three things.

- It names the job, in words a user would actually say.
- It includes trigger verbs such as use, check, review, verify, or run.
- It states when to use the skill, not only what the skill is.

Compare two descriptions.
"QA helper" tells the loader almost nothing.
"Use when you need to check a delivery before handover: review the diff, verify tests, and audit the pack against the scope" names the moment and the actions.
Write the second kind.
Keep it long enough to be specific and short enough to scan.
The audit tool in this lesson checks length and trigger verbs.

## When a workflow deserves to become a skill

Not every repeated task earns a skill.
Use this test.

- You have done it at least three times.
- The steps are stable, even if the inputs change.
- A missed step has a real cost.
- A checklist or script can carry part of the work.

If the steps still change every time, keep learning in the open.
Turn it into a skill when the shape settles.
A skill built too early freezes a bad process and lends it authority.

## The body: procedure, not essay

Write the body as steps an agent can follow and check.

- Number the steps in the order they must run.
- Name the exact checks, files, or commands involved.
- State what a pass looks like and what a fail looks like.
- End with what to report back to the human.

Leave out background theory.
Put depth in a reference file inside the skill folder if it is needed.
The skill body should stay short enough to load without regret.

## Versioning a personal library

Treat your library like software you depend on.

- Keep it in one folder, under version control.
- Change one skill at a time, and note why in the commit message.
- Bump behaviour, not cosmetics: if the steps change, the version note changes.
- Remove skills you no longer trust. A stale skill is a liability.

An inventory matters as the library grows.
`skill_audit.py` in this lesson lists every skill in a folder and reports its health.
Run it before a client job, not after a skill misfires during one.

## Delivering with skills, then selling the library

Delivery comes first.
Use the library on real work, under real deadlines, until the weak skills have failed in private and been fixed.
Only then consider packaging it for sale.
A library sold before it is proven sells your untested drafts.
A library proven in delivery can be described honestly: what each skill does, when it helps, and where it stops.
That honest description is also better marketing, because buyers can test the claims.

There is no price in this lesson on purpose.
Pricing a library follows the same rules as Lesson 01 and Lesson 14: source it, price it from your costs, or label any figure a worked example.

## A worked example

Worked example: assume you run a delivery QA pass before every handover for Lumen Med Spa, the fictional client in this course.
The first time, it took an afternoon and you still missed a broken link.
The third time, the steps were stable: check the scope, review the diff, verify the tests, audit links and secrets, write the handover note.
That is the moment to write the skill shipped in this lesson, at `skills/qa-checklist/SKILL.md`.
From then on, the QA pass starts from the checklist instead of from memory.

## Run it

Run the audit on the shipped skill, then on the whole folder:

```
python3 skill_audit.py skills/qa-checklist/SKILL.md
python3 skill_audit.py skills
```

The shipped skill should pass with no problems.
Then run `python3 smoke_test.py`.
The smoke test also builds a broken fixture and checks that the audit catches it.

## Common failures

- **A description that describes, but never triggers.** No trigger verbs and no "use when" moment means the loader cannot match real requests to the skill.
- **Skills for one off tasks.** A skill used once is documentation with extra ceremony; wait until the third repeat.
- **Selling an untested library.** Buyers find the same bugs your clients would have found, except they paid for the privilege and they say so in public.

## Recap checklist

- [ ] I can explain why the description, not the body, decides whether a skill fires.
- [ ] I have one workflow that passes the four part test for becoming a skill.
- [ ] My library has an inventory I can audit in one command.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Anthropic skills repository](https://github.com/anthropics/skills)
- [Claude pricing](https://claude.com/pricing)
