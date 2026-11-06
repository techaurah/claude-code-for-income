# Lesson 06: MCP servers: connecting the agent to the client's world

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 02 to 05 · **You need:** Python 3.11 or newer. The budget tool runs offline on tool definitions you supply.

MCP is the Model Context Protocol, an open protocol that lets agents use external tools and data through servers with defined schemas.
A server exposes tools.
The agent calls those tools like any other tool.
For client work, that means the agent can work inside the client's world instead of beside it: their files, their database in read only form, their issue tracker, their calendar.
This lesson teaches selection judgement and the cost nobody budgets.

## What MCP adds to client work

Without MCP, the agent sees the repo and the terminal.
Useful, but limited to what you paste or clone.
With the right server, the same agent can do connected work.

- Look up a real record instead of guessing from a screenshot.
- Create an issue in the tracker the team actually uses.
- Read a document from the store the client already pays for.
- Check a calendar before proposing a time.

Each connection removes a manual step where you were the courier between systems.
That courier work is real time on real jobs, and removing it is the honest value here.

## What MCP does not add

A server does not make a bad scope good.
It does not grant permission you do not have.
It does not make a tool's output true.
Connecting more systems also widens what can go wrong.
A read only server misread is an annoyance.
A write capable server, pointed at production, is Lesson 05's problem all over again, with a new surface.
Connect the few servers the job needs, with the narrowest access that works.

## Server selection judgement

Choose servers the way you choose dependencies.

- Prefer official or well maintained servers, with a public repo you can read.
- Check what credentials it wants and where they are stored.
- Check whether it can run in read only mode, and start there.
- Check its tool list. A server with forty tools for a two tool job is a cost, not a bonus.
- Test it on harmless data before it touches a client system.

The programme's Build MCP Servers course teaches building servers in depth.
This lesson teaches choosing and budgeting them for paid work, and points you there for the build side.

## The tool definition overhead nobody budgets

Every connected tool carries a definition: a name, a description, and a schema for its inputs.
Those definitions sit in the agent's context.
They are paid for in context space on every session that loads them, whether the tool is called or not.
Connect three large servers and you can spend a visible share of context on tools the job never uses.

This is an estimate problem, not a mystery.
`tool_budget.py` in this lesson estimates each tool's cost with a simple heuristic: serialised characters divided by four, a rough tokens per character rule.
It is labelled a heuristic because it is one.
It is close enough to compare servers and to enforce a budget, which is the decision you actually face.
Set a budget for tool definitions per engagement, and make a new server argue its way in.

## Budgeting in practice

Use a simple discipline.

- List the tools a job truly needs before connecting anything.
- Estimate the full server set, not only the tools you like.
- If the total is over budget, drop a server, or pick a narrower one.
- Re check the budget when a server updates and its schemas grow.

Worked example: assume an engagement budget of 800 estimated tokens for tool definitions.
A small file server and a small issue tracker server fit, as the shipped example shows in the exercise data.
A third, broad server pushes the set over budget.
The right move is usually to connect the third server only for the sessions that need it, not to raise the budget by default.

## Configuration shape

Claude Code MCP configuration names each server and how to start it.
`mcp_config.example.json` in this lesson shows two servers in that shape, with placeholder values only.
Real credentials belong in the client's approved secret store or your local environment, never in a config file you commit.
Lesson 05's secret rule applies here with extra force, because MCP configs get copied between projects.

## Safety checks before a client connection

Run this list before any server touches client data.

- The client knows which systems the agent can reach, in writing.
- Access is read only until write access is separately agreed.
- The server's tools are inside the token budget.
- The guardrails from Lesson 05 still apply to local tool calls.
- You can disconnect the server in one step and say how.

If any item fails, the connection waits.
A delayed connection is a scheduling note. A bad connection is an incident.

## Run it

Run the budget tool on its demo set, then on a JSON file of your own:

```
python3 tool_budget.py
python3 tool_budget.py my_tools.json 800
```

The demo should report a total and state whether it is over budget.
Then run `python3 smoke_test.py`, and read the Build MCP Servers course in this programme when you need to build a server rather than choose one.

## Common failures

- **Connecting every server you own to every job.** Context fills with definitions for tools the job never calls, and the code that matters gets squeezed.
- **Committing real credentials in an MCP config.** Config files travel; secrets must live outside them.
- **Write access on day one.** Starting read only costs little and proves the value before the risk grows.

## Recap checklist

- [ ] I can name the servers a current job needs, and the ones it does not.
- [ ] I have an estimated token total for my tool set, against a stated budget.
- [ ] My MCP configs contain placeholders only, with secrets held elsewhere.

## Resources

- [Model Context Protocol](https://modelcontextprotocol.io)
- [Claude Code documentation](https://code.claude.com/docs)
- [Claude Code MCP guide](https://code.claude.com/docs/en/mcp)
- [MCP servers on GitHub](https://github.com/modelcontextprotocol/servers)
- [Anthropic on GitHub](https://github.com/anthropics)
