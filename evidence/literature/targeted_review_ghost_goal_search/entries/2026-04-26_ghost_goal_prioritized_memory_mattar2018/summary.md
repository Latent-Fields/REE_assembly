# Mattar & Daw 2018 -- unresolved traces should be ranked by utility, not revisited randomly

## What the paper did

Mattar and Daw developed a normative theory of replay priority. The question was
not whether replay exists, but which memories should be accessed if the system is
trying to improve future decisions efficiently.

## Key findings relevant to ghost-goal search

Their answer is utility-like prioritization. Memory access should concentrate on
states whose update would most improve future behavior. This is neither pure
recency nor pure surprise and is much closer to a weighted prioritization rule.

For ghost-goal search, that is exactly the ranking problem. Not every blocked or
stale trace deserves re-probing. Some unresolved goals are recoverable and
decision-relevant; others are dead ends. A good bank therefore needs a priority
rule, not just a broad pool.

## Translation to REE

MECH-292's ranking rule is the direct translation: wanting, goal match,
staleness, and recoverability together approximate a utility-style priority over
unresolved traces. The paper also argues against flat random probing as a default
search policy.

## Limitations and caveats

The paper is a computational model and uses reward-oriented utility rather than a
full REE-style separation of harm and wanting. It is normative support, not a
direct neural demonstration of ghost goals.

## Confidence reasoning

Confidence 0.79. Strong normative support for ranked unresolved-goal access, with
the main gap being that the paper is not about explicit blocked-goal traces.
