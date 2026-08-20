# Rapid Spatial Learning Controls Instinctive Defensive Behavior in Mice

Vale, Evans & Branco (2017), *Current Biology* 27(9):1342-1349. DOI 10.1016/j.cub.2017.03.031. PMID 28416117. PMC5434248.

## What the paper did

This is a Branco-lab paper about how "instinctive" defensive behavior in mice is not actually rigid -- it is gated by rapidly-acquired spatial memory of where the shelter is. The design manipulates shelter availability directly: when the shelter route is experimentally closed at the moment a looming threat appears, the mouse cannot escape and instead freezes, and the authors measured how that freezing scales with threat urgency. A fast, near-maximal looming disc produced a freezing bout of 629.9 +/- 100.0 ms; a slow-expanding, less urgent looming spot produced a much longer freezing bout of 7.9 +/- 2.7 s. Separately, when the arena was unexpectedly rotated so the shelter's remembered relative position was briefly wrong, mice lingered near the now-incorrect pre-rotation location for 4.6 +/- 0.2 s before updating. And when a closed shelter route was reopened, defensive strategy flipped straight back to flight on the very next encounter five minutes later -- full reversal within a single trial, not a gradual re-acquisition.

## Why this bears on SD-099's persistence-window question

Two separate contributions, and they pull in different directions, which is why I have coded this `mixed` rather than `supports`.

First, on the pure MAGNITUDE question this pull was commissioned to settle: this is a second, fully independent triangulation point, from a different lab and a different manipulation than the Shang 2018 entry in this directory, and it lands in the same place. Even the FASTEST defensive-state duration measured anywhere in this paper -- 630ms, under the most time-pressured condition the authors tested -- sits almost exactly at Option A's own lower bound (625ms), not inside Option C's 60-125ms range. The slower, arguably more typical condition (7.9s) is closer to the Shang 2018 seconds-scale finding. Two independent paradigms, two different labs, converging on "post-orienting defensive state persists for hundreds of milliseconds to tens of seconds" and neither ever landing inside a sub-100ms window, is a stronger form of evidence than either alone.

Second, and this is the more consequential finding for SD-099's actual design: the paper's central point is that defensive-strategy commitment is not well described as running on a fixed schedule at all. It flips completely -- freeze back to flee -- within a single subsequent encounter once the state that produced it (shelter blocked vs. open) changes. That is direct evidence bearing on Q2, not just Q1. If the biological system this claim is modeled on resolves its post-encounter bias by re-evaluating against current state rather than by counting down a fixed duration, then the deeper design question is not "how many ticks" but "should this be a tick-count at all, or a condition-gated clear." I want to flag this without overstating it: SD-099 as documented already gates its ARREST phase on an identification-confidence accumulator rather than a fixed timer (per its own design doc), so the tick-count under discussion here is specifically the POST-decision bias window, a narrower and different component. Whether that narrower component should also be state-gated rather than duration-gated is a real question this paper raises but does not itself answer for that specific sub-mechanism.

## Limitations

The freezing-duration numbers are from a shelter-availability manipulation, not from SD-099's approach/withdraw/resume valence decision -- a structurally different choice. The urgency-scaling result (630ms vs. 7.9s) itself shows biological duration is not a fixed constant; it tracks stimulus and state parameters SD-099's current tick-count design does not read, which limits how directly any single number here can be imported. Some conditions have small sample sizes (arena-rotation, n=8 animals). Mouse throughout, single lab/paradigm family shared with much of the surrounding looming-defense literature.

## Confidence

0.60. Source quality 0.82 -- Current Biology, precise SEM-quantified numbers, a genuinely causal shelter-manipulation design. Mapping fidelity 0.55 -- strong as a second magnitude anchor, real but non-decisive on the duration-vs-state-gating question. Transfer risk 0.45, the same class of rodent-innate-defense-to-abstract-agent gap as the sibling entry in this directory.
