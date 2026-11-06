# Lesson 09: Parallel worktrees and background agents

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 04, 07, and 08, plus working knowledge of git branches · **You need:** Python 3.11 or newer and git for the live path. The planner runs offline on a task list.

One agent in one checkout can only move at one speed.
Parallel agents in one checkout move at the speed of their conflicts.
A worktree solves that shape of problem.
A worktree is a separate working directory that shares one git repository.
Each agent stream gets its own directory and its own branch.
Streams edit in isolation and merge deliberately, in an order you chose in advance.
This lesson teaches that discipline: naming, merge order, and file ownership.

## Why parallel work fails without isolation

Agents are fast editors.
Two fast editors in one folder overwrite each other's context, and sometimes each other's files.
Even when the files differ, a half finished change in the shared folder breaks the other stream's tests.
The failure looks like agent error.
It is usually workspace design error.
Isolation is cheaper than debugging interference you created yourself.

## The worktree pattern

For each parallel stream, create one worktree and one branch.

- One directory per stream, outside or beside the main checkout.
- One branch per stream, named for the task, not for the agent.
- One owner agent per stream, named in the plan.
- One merge order, decided before work starts.

`worktree_plan.py` in this lesson turns a task list with file ownership into exactly that plan.
It also flags the problem isolation cannot solve: two streams that claim the same file.

## Branch naming that survives review

A branch name should tell a reviewer what is inside without opening it.

- Use a short prefix for the kind of work, such as `agent/`.
- Follow it with the task id or a few words of the task slug.
- Keep it lower case and hyphenated.
- Never name a branch after the day or the agent alone.

`agent/fix-booking-form` ages well.
`agent/work-2` tells the future nothing, and the future is where merges happen.

## File ownership: the real contract

Parallel safety comes from ownership, not from directories alone.
Before dispatch, assign every task the files it may change.
Then check the assignments for overlap.

- If two tasks claim the same file, they are not parallel tasks. Sequence them, or split the file work.
- Shared files such as lock files, schemas, and top level configs get one owner, or a merge step of their own.
- A task that discovers it needs a file outside its list stops and reports. It does not quietly expand its territory.

The planner flags collisions by exact file path.
That catches the common case.
It does not catch two files that secretly depend on each other, which is why dependencies from Lesson 04 still belong in the plan.

## Merge order

Isolation defers integration. It does not remove it.
Decide the order before the branches exist.

- Merge foundations first: schemas, interfaces, shared types.
- Merge dependents after the things they depend on.
- Run the full test set after each merge, not only at the end.
- If a merge conflicts, the owner of the later branch resolves it, with the earlier owner reviewing.

A merge order written in advance turns integration into a checklist.
A merge order invented at the end turns it into an argument between tired people and fast agents.

## Background agents in worktrees

Background agents pair well with worktrees.
Start a stream, let it run in its own directory, and check back through its branch and its test results.
Keep the same discipline as Lesson 08: caps, logs, and a failure route.
A background agent in a shared checkout is a hazard.
A background agent in its own worktree, on its own branch, with owned files, is a colleague with a desk.

## A worked example

Worked example: assume a delivery for Lumen Med Spa, the fictional client in this course, splits into three streams.
One stream changes the booking form, one updates the API handler, and one writes documentation.
Their file lists do not overlap, so the plan is clean and the merge order follows the dependencies: API first, form second, docs last.
Now add a fourth stream that also edits the API handler file.
The planner flags a collision on that file.
The fix is not hope. Either sequence the two API streams, or give the file to one owner and let the other stream work through it.

## Run it

Run the planner on its demo tasks, then on your own JSON list:

```
python3 worktree_plan.py
python3 worktree_plan.py my_tasks.json
```

A clean plan prints a directory, a branch, an owner, and a merge position per task, with no collisions.
Then run `python3 smoke_test.py`.

## Common failures

- **Parallel tasks, shared files.** Two streams editing one file is serial work wearing a parallel costume, plus merge conflicts.
- **Branches named by agent or date.** Reviewers cannot tell what a branch holds, so integration slows exactly where it should speed up.
- **Merging everything at the end.** Late integration concentrates every conflict into the worst hour of the job; merge in the planned order, testing as you go.

## Recap checklist

- [ ] Every parallel stream in my plan has its own directory, branch, and owner agent.
- [ ] File ownership lists are checked for collisions before any agent starts.
- [ ] The merge order is written down, follows dependencies, and includes a test run after each merge.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code worktrees and parallel sessions](https://code.claude.com/docs/en/worktrees)
- [git worktree documentation](https://git-scm.com/docs/git-worktree)
- [Anthropic on GitHub](https://github.com/anthropics)
- [Claude pricing](https://claude.com/pricing)
