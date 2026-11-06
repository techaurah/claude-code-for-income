---
name: qa-checklist
description: Use when you need to check a delivery before handover. Review the diff, verify the tests pass, audit links and secrets, and run through the scope item by item before anything reaches the client.
---

# QA checklist: delivery check before handover

Use this skill on any delivery, before the client sees it.

## Steps

1. Check the scope first. List every promised item and mark where it is delivered.
2. Review the diff. Read every changed file, not only the summary.
3. Verify the tests. Run the project test command and record the result.
4. Audit links, secrets, and personal data. None may ship by accident.
5. Check the handover note. It must state what changed, how to run it, and what is out of scope.
6. Report back: pass or fail per item, with the failing item named plainly.

## Pass and fail

A pass means every scope item is present and every check above ran.
A fail means any scope item is missing, any test fails, or any secret,
broken link, or personal data appears in the delivery.
On a fail, fix and run this checklist again from step 1.
