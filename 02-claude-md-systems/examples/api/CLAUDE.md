# Directory memory: API folder (worked example)

This file applies only inside the API folder of the fictional
Lumen Med Spa booking integration.

## Local rules

- Run API tests with `python3 -m pytest tests/api -q`.
- Payment webhooks are tested with fixtures only, never live calls.
- Response shapes are versioned. Do not change a v1 field in place.
- Log request ids, never log request bodies with personal data.

This narrow file deliberately has no project wide
command list, no shared rule set, and no architecture summary.
Those live in the project file, one layer up.
