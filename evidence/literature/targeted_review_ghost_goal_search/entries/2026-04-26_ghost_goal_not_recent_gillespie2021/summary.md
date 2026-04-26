# Gillespie et al. 2021 -- replay already reaches non-current, not-recent traces

## What the paper did

Gillespie and colleagues decoded awake hippocampal replay in a dynamic spatial
memory task where rewarded locations changed over time. They asked whether replay
primarily previewed the upcoming choice or whether it was biased toward different
content.

## Key findings relevant to ghost-goal search

Replay was not tightly tied to the imminent choice. Instead it was enriched for
previously rewarded and not-recently-visited locations. This is the strongest
local literature support that the replay/search substrate already admits traces
that are:

- non-current
- non-recent
- still behaviorally relevant

That is extremely close to the operational meaning of a ghost-goal bank.

## Translation to REE

The paper strongly supports broad coverage plus weighted prioritization. It argues
against a waking policy that only searches around the current anchor, and it also
argues against pure random probing because the enrichment is structured rather than
flat. This is direct support for MECH-292 and good support for the waking-probe
half of MECH-293.

## Limitations and caveats

Visit-recency is only a proxy for REE-style staleness, and the study is about
awake replay rather than explicit blocked-goal retention. Still, it is the best
available bridge from stale, non-current traces to replay priority.

## Confidence reasoning

Confidence 0.84. This is the clearest existing neural match for a broad,
structured, non-current access policy.
