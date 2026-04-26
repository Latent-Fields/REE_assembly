# Ghost Goal Search Lit-Pull -- Synthesis

> Created: 2026-04-26
> Scope: literature grounding for explicit unresolved-goal traces, ghost-goal
> ranking, and awake hippocampal probe search.
> New claims anchored here: SD-039, MECH-292, MECH-293, ARC-060.
> Existing claims anchored here: MECH-230, ARC-051, MECH-269, MECH-285, MECH-291.

This pull asks a narrow design question:

> Does a good agent need an explicit bank of still-wanted but not currently
> executable goals, and should waking hippocampal search spend proposal budget
> on those traces rather than probing randomly?

The answer from the current literature is **yes, with three constraints**:

1. the unresolved trace must preserve motivational identity, not just location
2. replay/search priority must be utility-like, not pure recency or pure noise
3. inactive traces should remain queryable across waking and offline modes

## Verdict 1. Wanting is a distinct persistent motivational signal, not just contact pleasure

Berridge & Robinson 1998 and Barch & Dowd 2010 jointly ground the first half of
the argument.

- Berridge & Robinson show that wanting and liking are dissociable.
- Barch & Dowd show that losing sustained goal representations collapses agency
  even when liking remains intact.

The architectural implication is direct: a stale region is not enough. If the
system is going to preserve a blocked or deferred goal, it must preserve
something about the motivational content that made the goal live in the first
place. In REE terms, this means preserving a goal-linked payload, not just an
inactive anchor plus staleness scalar.

**Design implication:** supports SD-039 and ARC-060.

## Verdict 2. Blocked goals remain affectively active rather than disappearing cleanly

Berkowitz 1989 is not a hippocampal paper, but it is useful here because it
captures the phenomenology of unresolved goals: goal blockage does not merely
erase motivation; it often preserves an aversive, still-live pull around the
failed goal path.

REE should not translate this literally into aggression. The useful architectural
piece is simpler:

- blocked goals remain computationally active
- unresolved path closure carries affective weight
- search pressure is therefore biased, not neutral, after blockage

**Design implication:** supports the need for a ghost-goal bank rather than
assuming inactive anchors can stay anonymous.

## Verdict 3. Hippocampal search is already goal-biased and future-directed

Pfeiffer & Foster 2013 show that hippocampal sequences can depict future paths
toward remembered goals before action. This matters because it rejects the idea
that hippocampal search is only a generic planner over current terrain. The
sequence generator is explicitly capable of being goal-directed.

That does not yet prove ghost-goal search. But it does support the next step:
if the hippocampus can generate goal-directed future paths, then feeding it a
ranked bank of unresolved goal traces is biologically plausible.

**Design implication:** supports MECH-293.

## Verdict 4. Search/replay priority should be utility-like, not random

Mattar & Daw 2018 give the normative backbone. Memory access should be
prioritized by decision utility, not random choice or naive recency. This fits
the ghost-goal problem exactly:

- some blocked goals are still worth probing
- others are dead ends
- a useful system needs a ranking rule

The ghost-goal bank therefore should not simply replay or probe the stalest
trace. It should rank unresolved traces by a utility-like mixture of wanting,
goal match, staleness, and recoverability.

**Design implication:** supports MECH-292 and MECH-293.

## Verdict 5. Broad replay pools include non-current and not-recent traces

Gillespie et al. 2021 is the strongest direct support for the "ghost" part of
the idea. Replay is enriched for previously rewarded and not-recently-visited
locations, not just the imminent choice path.

That means:

- the seed pool is broad
- inactive or non-current traces remain replay-eligible
- a time-since-visited or staleness-like variable contributes to priority

This is close to a direct argument against current-only active-anchor search.

**Design implication:** supports MECH-292 and argues that the waking probe
policy should not be pure random noise around the current anchor.

## Verdict 6. Online and offline search are two modes of one sequence generator

Muessig et al. 2019 supports the architectural unity of waking and offline
hippocampal sequence generation. This matters because ghost goals should not be
implemented as a sleep-only repair trick. If the same generator runs in two
modes, the unresolved-goal substrate should be shared:

- sleep can replay it
- waking can probe it

The weighting and timing may differ by mode, but the preserved trace should not
live in one mode only.

**Design implication:** supports MECH-293 and ARC-060.

## Main architectural conclusion

The literature does **not** support a full "goal stack" in the software-engineering
sense. What it supports is:

- a continuous wanting field for smooth local guidance
- plus a discrete bank of unresolved goal traces when local guidance collapses

That is the right translation of the user's "ghosts of goals" idea.

## Strongest required addition to V3

The most important missing substrate in `ree-v3` is not another planner. It is
the preservation of goal identity on dual-trace anchors.

Right now the system can say:

- this region is stale
- this anchor is inactive

but not:

- this inactive stale anchor still corresponds to the current goal

That missing sentence is exactly SD-039.

## Recommended implementation order

1. Preserve `z_goal_snapshot` plus wanting/arousal payload on anchors.
2. Build a ranked ghost-goal bank from inactive/high-staleness anchors.
3. Allocate a minority waking probe budget to top ghost-goal entries.
4. Add between-ticks micro-refresh only after full-tick ghost probing works.

## Papers pulled in this review

| # | First author | Year | Why it matters here |
|---|--------------|------|---------------------|
| 1 | Berridge | 1998 | wanting is distinct from liking |
| 2 | Barch | 2010 | goal maintenance failure collapses agency |
| 3 | Berkowitz | 1989 | blocked goals remain affectively live |
| 4 | Pfeiffer | 2013 | hippocampus generates future paths to remembered goals |
| 5 | Mattar | 2018 | priority should be utility-like, not random |
| 6 | Gillespie | 2021 | replay enriched for non-current, not-recent traces |
| 7 | Muessig | 2019 | online/offline sequence generation is one substrate, two modes |
