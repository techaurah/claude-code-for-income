# Glossary

Every term this course uses, in plain language. Lessons define
terms on first use too; this page is the shelf to check when one
slips past.

- **Agent SDK**: Anthropic's library for embedding the Claude Code agent in your own programs, so a product or pipeline can run the agent without a human at a terminal. Lesson 07.
- **Break-even hours**: a plan's monthly price divided by your billable rate. The hours the tool must save each month before the plan costs you money instead of making room. Lesson 01.
- **CLAUDE.md**: the instruction file Claude Code reads at the start of a session. Layered from user level down to directory level, it is the agent's standing memory for how you work. Lesson 02.
- **Capstone**: the course's closing project, Lessons 29 to 31: one simulated client engagement run end to end.
- **Churn**: the share of subscribers who cancel in a period. The quiet variable that decides whether a micro-SaaS lives. Lesson 24.
- **Cost floor**: the lowest price at which a job still covers your time at your target rate plus its measured costs. Pricing below it is a donation. Lesson 14.
- **Cost per job**: what one engagement or order actually cost in model usage, measured from run output rather than guessed. Lesson 11.
- **Discovery**: the structured conversation and inspection before a scope exists, where the client's real problem and real numbers come from. Lesson 13.
- **Fixed price**: a single price for a defined scope, agreed before work starts. The risk moves to whoever scoped it, which is why Lesson 13 exists.
- **Headless mode**: running Claude Code non-interactively (`claude -p`) from a script, cron job, or CI pipeline, with explicit tools, caps, and machine-readable output. Lesson 07.
- **Hook**: a command Claude Code runs automatically at a lifecycle point (before a tool call, after an edit, at session end). The course uses hooks as guardrails and gates. Lesson 05.
- **Lifetime value (LTV)**: the gross margin one customer produces over the whole relationship. Compared against acquisition and maintenance cost in Lesson 24.
- **MCP (Model Context Protocol)**: the open protocol that lets agents use external tools and data through servers with defined schemas. Lesson 06, and Course 3 of this programme in depth.
- **Productized service**: a service sold as a fixed package: named outcome, fixed scope, fixed price, repeatable fulfilment pipeline. Module 5.
- **QA gate**: a defined set of checks that must pass before work reaches a client. Automated where possible, human where it matters. Lessons 05, 15, and 18.
- **Retainer**: a recurring fee for ongoing availability and a defined monthly scope of work, with reporting the client can verify. Lesson 26.
- **Routine / scheduled task**: a saved Claude Code configuration that runs on a schedule, an API call, or a GitHub event, on Anthropic's cloud or your own machine. Lesson 08.
- **Scope**: the written boundary of what a price buys: deliverables, exclusions, revision rounds, and what happens when the boundary moves. Lesson 13.
- **Skill**: a packaged folder of instructions and resources (a SKILL.md at its heart) that Claude Code loads when a task matches its description. Treated in this course as reusable capital. Lesson 03.
- **Subagent**: a specialist agent definition with its own context, tools, and instructions, dispatched by the main agent for a bounded piece of work. Lesson 04.
- **Value anchor**: the client's own number for what the problem costs them, established in discovery, against which a price is judged. Lesson 14.
- **Worked example**: an illustrative calculation in this course whose inputs are invented for teaching and printed next to the result, so you can change them. Never data, never a promise.
- **Worktree**: a separate working directory sharing one git repository, so parallel agents edit in isolation and merge deliberately. Lesson 09.
