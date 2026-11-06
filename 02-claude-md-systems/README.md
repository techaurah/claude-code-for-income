# Lesson 02: CLAUDE.md systems: memory that compounds

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 00 and 01, plus one real project where you already use a CLAUDE.md · **You need:** Python 3.11 or newer. No Claude session is required; the linter runs offline.

A CLAUDE.md file is the instruction file Claude Code reads at the start of a session.
Think of it as standing memory.
Without it, every session starts from zero and you repeat the same corrections.
With it, a correction you make once stays made.
That is why this lesson calls memory an asset that compounds.
Each good entry saves a little time on every future job.
Each bad entry costs a little time on every future job too.

## The three layers

Claude Code reads memory in layers, from broad to specific.

- **User layer.** Your personal CLAUDE.md, shared across projects.
- **Project layer.** A CLAUDE.md at the repository root, shared with the team.
- **Directory layer.** A CLAUDE.md inside a folder, for rules that only apply there.

More specific layers add detail for their scope.
They do not need to repeat the broad layers.
Repetition is a cost, because the agent reads it all, every session.

## What belongs in the user layer

Keep this layer about you, not about any one codebase.

- Your default tone for commit messages and comments.
- Tools you prefer, and tools you avoid.
- Checks you want run before any delivery.
- Hard personal boundaries, such as never force pushing.

Keep it short.
If a rule only makes sense in one repository, it does not belong here.

## What belongs in the project layer

Keep this layer about the shared project.

- How to install, run, test, and lint the project.
- The architecture in a few lines, not a design document.
- Conventions the codebase actually follows.
- Boundaries: files not to edit, secrets never to read, areas that need review.

This is the file a new contributor, human or agent, should read first.
The shipped example under `examples/` follows this shape.

## What belongs in the directory layer

Keep this layer narrow.

- Rules for one package, one service, or one risky folder.
- Local commands that differ from the project defaults.
- Local hazards, such as generated files that look hand written.

The shipped example under `examples/api/` covers an API folder.
It says nothing about the rest of the project.
That narrow scope is the point.

## What does not belong anywhere

Some content hurts wherever you put it.

- Secrets, tokens, passwords, or client data. Never.
- Long tutorials the agent does not need at task time.
- History: why a decision was made three months ago, in essay form.
- Vague advice such as "write good code" or "be careful".
- Instructions you no longer follow yourself.

If an entry would not change an action, delete it.

## Size discipline

Context is not free.
Every word in memory is read before real work starts.
Long files crowd out the code that matters.
They also hide the few rules that matter most.

Use these working rules:

- Keep the project file under the linter budget in this lesson.
- Prefer one precise line over one vague paragraph.
- Move reference detail into docs, and link to it instead.
- Prune monthly. Stale rules are worse than missing rules.

The linter in this lesson reports word count and warns over budget.
It is a prompt to edit, not a law of nature.

## Writing entries that change behaviour

Good entries share a shape.

- They name a command, a path, or a check.
- They can be obeyed or disobeyed, clearly.
- They fit on one or two lines.

Compare two entries.
"Be careful with the database" changes nothing.
"Never edit files under `migrations/` by hand; add a new migration instead" changes the next action.
Write the second kind.

## A worked example: Lumen Med Spa

Worked example: Lumen Med Spa is the fictional client used across this course.
Assume a small booking integration with a web app and an API folder.
The project file states the test command and the booking rules once.
The API folder file adds one local rule: payment webhooks are tested with fixtures, never with live calls.
Neither file repeats the other.
A session in the API folder gets both layers, in the right order.
A session elsewhere gets only what it needs.

## Updating memory during a job

Treat corrections as deposits.

- When the agent makes the same mistake twice, add a rule.
- When you override the agent, ask whether a rule would prevent a repeat.
- When a rule causes a mistake, fix or remove that rule at once.
- Review the diff to CLAUDE.md like any other code change.

Do not add a rule after a single odd case.
One case is noise. Two cases are a pattern worth encoding.

## Run it

Run the linter on both shipped examples:

```
python3 claude_md_lint.py examples/CLAUDE.md
python3 claude_md_lint.py examples/api/CLAUDE.md
```

The project example should report no missing sections.
The directory example should report missing sections, on purpose.
A narrow file does not need every section, and the linter output shows the trade off.
Then run `python3 smoke_test.py`.

## Common failures

- **One giant file for everything.** User, project, and directory rules mixed together means no layer can be reused and every session pays for rules it does not need.
- **Memory as a diary.** Decision history and long explanations bury the commands and boundaries the agent needs in the first minute.
- **Never pruning.** Rules for a stack you left last year still steer the agent today, and they steer it wrong.

## Recap checklist

- [ ] I can place any rule in the user, project, or directory layer and say why.
- [ ] My project CLAUDE.md has commands, conventions, and boundaries, and fits the budget.
- [ ] I have removed at least one entry that would not change an action.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code memory and CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Claude pricing](https://claude.com/pricing)
- [Anthropic on GitHub](https://github.com/anthropics)
