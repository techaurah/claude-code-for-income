# Lesson 04: Subagents and delegation: a team in a folder

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 02 and 03 · **You need:** Python 3.11 or newer. The dispatch simulator runs offline and needs no live agents.

A subagent is a specialist agent definition with its own context, tools, and instructions.
The main agent dispatches a bounded job to it.
The subagent works in isolation and returns a result.
A folder of these definitions starts to behave like a small team.
This lesson teaches how to define that team, how to dispatch to it with discipline, and where to put review gates so speed does not outrun judgement.

## Agent definition files

In Claude Code, a custom subagent is a Markdown file with frontmatter.
The frontmatter carries the fields the dispatcher needs.

- **name.** A short, stable identifier, lower case and hyphenated.
- **description.** When this agent should be used, in trigger language.
- **tools.** The tools this agent may use. Leave it out only when inheritance is intended.
- **model.** The model this agent should run on, when the job needs a specific tier.

The body is the agent's system prompt: its job, its method, and what it must return.
This lesson ships two examples under `agents/`: a code reviewer and a test writer.
Read their tool lists carefully.
The reviewer can read and search, but not edit.
The test writer can edit test files and run tests.
That difference is not decoration. It is the safety design.

## Why context isolation matters

Each subagent starts with a fresh context.
That has three practical effects.

- The main conversation stays clean. Exploration noise stays in the subagent.
- The subagent cannot be distracted by the main thread's history.
- The result comes back as a summary, not as a transcript.

Isolation also has a cost.
The subagent knows only what you send it and what its definition says.
A vague dispatch gives an isolated agent nothing to work with.
Delegation therefore rewards precise briefs, which is a theme this course returns to often.

## Dispatch discipline

One bounded job per agent.
That sentence is the whole discipline, and the rest is detail.

- Name the output. "Return a list of findings with file and line" beats "look at the code".
- Name the boundary. State what is out of scope as plainly as what is in scope.
- Name the done condition. Say what a finished job looks like.
- Dispatch independent jobs together. Wait for dependent jobs in order.

If a job cannot be stated in a short brief, it is not ready to delegate.
Do the splitting yourself first.
Splitting is the human work. Typing was never the bottleneck at this level.

## Parallel waves

When tasks have dependencies, they form waves.
Wave one holds every task with no unmet dependency.
Wave two holds the tasks that wave one unlocks, and so on.
Independent tasks in the same wave can run at the same time.
Dependent tasks must never share a wave with the task they depend on.

`dispatch_sim.py` in this lesson computes exactly this.
Feed it a task list with dependencies and named agents.
It prints the waves in order, with the agent assigned to each task.
If your mental schedule and the simulator disagree, trust the dependency list and fix the brief.

## Review gates between agents

Agents should not grade their own homework, and downstream agents should not build on unreviewed work.
Put a gate between production and use.

- A reviewer checks a builder's output before anything merges.
- A test run checks a writer's output before a reviewer spends time on it.
- A human checks anything a client will see, at least at first.

A gate can bounce work.
In the simulator, a task named in the bounce set fails its first review and runs once more in the next wave, then passes.
That one bounce is deliberate teaching.
In real work, set a bounce limit in advance.
A task that bounces twice needs a human and a better brief, not a third try.

## Choosing tools and models per agent

Give each agent the smallest tool set that can do its job.
A reviewer that cannot edit cannot break the code it reviews.
A researcher that cannot write files cannot leave stray notes in the repo.
Small tool sets also make review easier: you know what the agent could have touched.

Match the model to the job, using the same rule as the cost lessons.
Mechanical work can run on a smaller, cheaper tier.
Judgement heavy work earns the stronger tier.
Lesson 11 turns that rule into measured cost per job.
For now, state the choice in the definition file so it is visible and changeable.

## A worked example

Worked example: a delivery for Lumen Med Spa, the fictional client in this course, needs a booking form change.
Assume three tasks: write the form change, write tests for it, and review both.
The test task depends on the form task, because tests target real behaviour.
The review task depends on both.
The simulator places the form task in wave one, the tests in wave two, and the review in wave three.
If the review bounces the form task, the form runs once more before the review can pass.
That schedule is the exercise pattern, at delivery scale.

## Run it

Run the simulator on its built in demo, then on your own JSON task list:

```
python3 dispatch_sim.py
python3 dispatch_sim.py my_tasks.json
```

Check that dependent tasks land in later waves than their dependencies.
Then run `python3 smoke_test.py`, which asserts the wave ordering and the bounce.

## Common failures

- **Delegating a whole project in one brief.** Unbounded jobs return unbounded results, and the review cost lands back on you with interest.
- **Giving every agent every tool.** Broad tool access removes the safety that specialist definitions were meant to create.
- **No gate before merge.** Two agents agreeing with each other is not verification; an independent check is.

## Recap checklist

- [ ] Each of my agent definitions has a name, a triggering description, a deliberate tool list, and a stated return shape.
- [ ] I can split a real job into bounded tasks with explicit dependencies.
- [ ] Every agent output that other work builds on passes a review gate first.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Anthropic agents on GitHub](https://github.com/anthropics)
- [Claude pricing](https://claude.com/pricing)
