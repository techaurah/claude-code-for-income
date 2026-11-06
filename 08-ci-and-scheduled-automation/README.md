# Lesson 08: CI and scheduled automation: work that runs while you sleep

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 05 and 07 · **You need:** Python 3.11 or newer. A GitHub account is optional; the shipped workflow is a file to read and adapt, and the planner runs offline.

Unattended work is where agent time stops competing with your day.
A review runs when a pull request opens.
A check runs at night.
A report is waiting in the morning.
This lesson teaches the four unattended modes, the official GitHub Action, and the discipline that stops unattended from becoming unnoticed.

## The four unattended modes

Each mode fits a different shape of work.

- **Background agents.** You start a session, step away, and check back. The session stays visible and resumable. Best for long jobs you still want to steer.
- **Headless mode.** A script runs `claude -p` with caps, as in Lesson 07. Best for one bounded job inside a pipeline you control.
- **In-session loop.** A running session repeats a prompt on an interval, keeping its context. Best for watching a changing situation during a working session.
- **Cloud scheduled tasks.** A saved configuration runs on Anthropic's cloud on a schedule, an API call, or a GitHub event. Best when your machine is off or the trigger lives in the cloud.

There is a fifth, plain option this course uses often: your own cron or scheduler running a headless command on a machine you control.
`schedule_plan.py` covers all five and gives reasons, because choosing the mode is the design decision.

## Choosing by constraints, not habit

Ask three questions in order.

- **What triggers the job?** A repository event, a clock, a human, or a loop inside a session.
- **Where must it run?** Your machine, CI, or the cloud, and is that place awake at trigger time.
- **What does it need?** Local files, repository events, live context, or a human checkpoint partway through.

The planner in this lesson encodes those questions.
If its recommendation surprises you, check your answers before you argue with the mode.
Most surprises are a constraint you stated loosely, such as a scheduled job on a laptop that sleeps.

## The official GitHub Action

For repository work, the official action is `anthropics/claude-code-action@v1`.
The shipped `claude-review.yml` uses it to review pull requests.
Read the workflow before you copy it.

- It triggers on pull request events, not on every push.
- It runs with the permissions the job states, and no more.
- The prompt tells the agent to review, not to rewrite the branch.
- Any API key belongs in repository secrets, never in the workflow file.

Pin actions, review their updates, and treat a workflow that can comment or edit as production code.
It is production code, with your repository's keys in its pockets.

## Scheduling discipline

Unattended work fails quietly by default.
Discipline is how you hear about it.

- Every scheduled job has an owner and a stated purpose.
- Every job logs its runs, its cost record where it has one, and its result.
- Failures go somewhere a human looks, the same day.
- A job that has not been useful in a month is deleted, not kept out of habit.
- Caps from Lesson 07 apply to every run, every time.

A useful test: if a job ran wrong last night, how would you know, and when?
If the answer is "when the client notices", the job is not ready to be unattended.

## What belongs on a schedule, and what does not

Good candidates share a shape.

- The job is bounded and its output is checkable.
- A wrong run is cheap to spot and cheap to undo.
- The value is in regularity, not in judgement calls.

Bad candidates are the mirror image.
Client visible judgement, irreversible actions, and anything Lesson 05 would block do not become acceptable because a clock started them.
Scheduling changes when work runs. It does not change what work is allowed.

## A worked example

Worked example: assume three recurring jobs for a practice serving Lumen Med Spa, the fictional client in this course.
A pull request review is triggered by repository events, so it belongs in CI with the official action.
A nightly test summary runs on a machine that is always on and already has a scheduler, so own cron running a capped headless command fits.
A weekly status check must run while your laptop is closed, so a cloud scheduled task fits.
Same agent, three modes, chosen by trigger and machine, not by preference.

## Run it

Run the planner, then create cases of your own:

```
python3 schedule_plan.py
```

The demo prints one case per mode, with reasons.
Adapt `claude-review.yml` on paper for a repository you own: change the trigger wording and the review prompt, and note where the secret would live.
Then run `python3 smoke_test.py`.

## Common failures

- **Scheduling a job on a machine that sleeps.** The job does not fail loudly; it simply never runs, which looks like success until it matters.
- **No failure route.** Unattended jobs need a named place where failures land and a human habit of reading it.
- **Review automation that can edit.** A review workflow with write power it does not need turns a comment bot into a supply chain risk.

## Recap checklist

- [ ] I can name the four unattended modes and the constraint that picks each one.
- [ ] Every scheduled job I run has caps, logs, and a failure route a human reads.
- [ ] My GitHub Action workflows use least permissions and secrets held outside the file.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)
- [Claude Code Action on GitHub](https://github.com/anthropics/claude-code-action)
- [Claude Code scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks)
- [Claude pricing](https://claude.com/pricing)
