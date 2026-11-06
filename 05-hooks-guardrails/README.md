# Lesson 05: Hooks: guardrails that make autonomy safe to sell

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 02 to 04 · **You need:** Python 3.11 or newer. The guard and simulator run offline; no live session is started.

A hook is a command Claude Code runs automatically at a point in the session lifecycle.
You configure hooks in settings.
Claude Code passes the event to your script as JSON.
Your script allows the action, blocks it, or adds checks after it.
Hooks turn rules you hope the agent follows into rules the system enforces.
That difference is what makes autonomy safe enough to sell to a client.

## The lifecycle points that matter first

Three hook events cover most client work.

- **PreToolUse.** Runs before a tool call. It can block the call.
- **PostToolUse.** Runs after a tool call. It can check, format, or report the result.
- **Stop.** Runs when the agent is about to finish. It can require more work or a final check.

Other events exist, and the official docs list them all.
Learn these three first.
They map to the three questions of any engagement: is this action allowed, did it work, and are we really done.

## The block and allow contract

A PreToolUse guard has a simple contract.

- Read the event JSON from standard input.
- Decide allow or deny, with a reason a human can read.
- Communicate the decision in the format Claude Code expects, and with the exit behaviour the docs describe.

Keep the contract boring.
A guard that tries to be clever will fail in clever ways.
`guard.py` in this lesson follows the simple shape: it reads a JSON event, extracts the command when there is one, checks it against deny patterns, and returns a decision with a reason.
`hook_sim.py` feeds sample events through it so you can see decisions without a live session.

## Guardrail one: no destructive commands

Some commands should never run unattended on a client system.

- Recursive forced deletion, such as `rm -rf` on a path.
- Force pushing to a shared branch.
- Dropping tables, or the database equivalent in your stack.
- Overwriting a disk, a production config, or a live data file.

Deny these by pattern in the guard.
Do not rely on the agent remembering a line in CLAUDE.md.
Memory persuades. A hook decides.

## Guardrail two: no secret reads

Client systems hold secrets: API keys, customer data, credentials.
An agent rarely needs to read them to do its job.
Deny reads of the usual homes for secrets.

- Environment files such as `.env`.
- Private keys and credential files.
- Home directory config for cloud tools, unless the job is about them.

If a job genuinely needs a secret, a human supplies it through the approved channel for that engagement.
The agent does not go looking.
This rule also protects you: work you never saw cannot leak through your work.

## Guardrail three: format and test on edit

PostToolUse hooks are where quality becomes automatic.

- After an edit, run the formatter for that file type.
- After a code change, run the fast test set, or at least the affected tests.
- If formatting or tests fail, surface it at once, not at delivery time.

Lesson 03's QA skill checks delivery at the end.
Hooks check each step as it lands.
Use both. End checks catch what step checks missed, and step checks keep end checks short.

## The Stop hook as a delivery gate

A Stop hook can ask one final question before a session ends.
Did the run update what it promised to update?
Did the tests pass after the last edit?
Is there a note for the human about what changed?
Configured well, it stops the quiet failure mode of agent work: a session that ends politely with the job half done and no signal.
Configured badly, it nags.
Keep the Stop check short and mechanical, like the other guards.

## Selling guardrails honestly

Clients do not buy hooks. They buy the risk the hooks remove.
In a proposal, describe guardrails in client language: no destructive commands run without approval, secrets are never read by the agent, every change is formatted and tested as it lands.
Those are verifiable claims, because the settings file and the guard script are artefacts you can show.
Do not claim a guard makes a system safe in general.
Claim what the patterns actually block, and keep the list current as you learn.

## A worked example

Worked example: for Lumen Med Spa, the fictional client in this course, assume the booking code lives in a repo the agent may edit.
The example settings in `hooks/settings.example.json` wire three hooks: the guard before tool use, a format and test check after edits, and a short final check at Stop.
The guard denies a recursive delete, denies a read of `.env`, and denies a force push, while allowing a normal test command.
Run the simulator and watch those exact decisions print.

## Run it

Run the simulator, then feed the guard a sample event yourself:

```
python3 hook_sim.py
echo '{"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}}' | python3 guard.py
```

The second command should report a deny decision with a reason.
Then run `python3 smoke_test.py`.

## Common failures

- **Guardrails only in prose.** A rule in CLAUDE.md that no hook enforces will eventually be skipped by a busy agent on a long session.
- **A guard with no reasons.** A deny with no explanation trains the human to bypass the guard, which is worse than no guard.
- **Blocking so much that work stops.** If normal commands bounce daily, tune the patterns. A guard people route around protects nothing.

## Recap checklist

- [ ] My PreToolUse guard denies destructive commands and secret reads, with reasons.
- [ ] My PostToolUse hook formats or tests after edits, automatically.
- [ ] I can state, in client language, exactly which risks my hooks do and do not cover.

## Resources

- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Anthropic on GitHub](https://github.com/anthropics)
