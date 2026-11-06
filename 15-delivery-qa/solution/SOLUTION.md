# Solution for Lesson 15: Delivery QA: the review discipline that protects your rate

The shipped fixture passes all four checks: required files present including the README, one Python file checked and compiling, and a clean secret scan. The smoke test performs the breaking half automatically: it copies the fixture, adds a notes file containing a fake key line, and the gate flips to fail with the secret scan check naming the file and line.

Deleting `runbook.md` from a copy fails a different check, required files, with the missing name listed. Two failures, two different repairs, neither of them editing the gate. That separation is the worked point: the record tells you which discipline slipped, presence, compilation, or secrets, and the delivery, not the checker, is where the fix belongs.
