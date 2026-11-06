# Solution for Lesson 30: Capstone run: build, QA gate, and the honest numbers

On the shipped record the simulator reports 11 of 11 checks effectively passing and marks delivery READY. The honest detail is inside that sentence: 10 checks passed as run, and Q07, the opt-out check, failed as run, was fixed with a send-time stop-condition check, and passed its retest. The ledger it prints is read from Lesson 29 and matches the spec exactly: fixed price $1,850, cost floor $720 (9 hours at $75 is $675, plus $25 plan share, plus $20 measured API), gross margin $1,130 before any platform fee.

Remove the retest from Q07 in a copy and the same simulator refuses the delivery state and names Q07 as the blocker. That pair of behaviours is the whole lesson: the gate is a mechanism, not a mood, and it treats a fixed and retested failure as evidence while treating an open failure as a stop.
