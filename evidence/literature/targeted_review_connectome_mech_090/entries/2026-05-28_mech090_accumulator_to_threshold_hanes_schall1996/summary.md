# Hanes & Schall 1996 — the commit gate is on a readiness accumulator, not on precision

**Citation.** Hanes, D. P., & Schall, J. D. (1996). Neural control of voluntary movement initiation. *Science*, 274(5286), 427–430. https://doi.org/10.1126/science.274.5286.427

## What the paper does

Hanes and Schall recorded single-unit activity from movement-related neurons in the frontal eye field (FEF) of two rhesus macaques performing a saccade countermanding (stop-signal) task. They asked a sharp mechanistic question: do voluntary saccades fire when a neural readiness signal reaches a specific threshold, or are they triggered by some other process (a deadline, a stochastic event)? They tested race / accumulator models against deadline-based and stochastic-decision alternatives.

The data favoured the accumulator model unambiguously. Movement-related FEF cells showed a stereotyped pre-saccadic rise; the rate of that rise was variable across trials, accounting for the distribution of reaction times; and crucially, movements were initiated *if and only if* firing rate reached a specific, approximately constant threshold activation level. Trials in which the readiness signal did not reach threshold (because the stop signal arrived in time to interrupt its rise) produced cancelled saccades. The threshold was a feature of the system, not of the trial.

This was the original direct neural evidence for the proposition — now central to a whole class of models — that commitment to a discrete motor act fires when motor-program readiness crosses a criterion.

## What it says about the REE commit predicate

This is the cleanest possible literature counterpoint to the current MECH-090 substrate. The REE-V3 BetaGate elevates into committed mode on `running_variance < commitment_threshold` — a predicate on precision of prediction (the world has stopped surprising the agent). Hanes-Schall is the canonical empirical finding that the biological commit gate is on the opposite kind of signal: an accumulator over a *readiness* representation, the firing-rate proxy for "the motor program I'm about to enact is prepared."

The V3-EXQ-592 seed 42 trajectory could not happen under a Hanes-Schall-style gate. An agent whose motor competence is 0.0 has no readiness signal to cross threshold. The rate of rise in the readiness accumulator would simply not occur, and the gate would not fire. The fact that REE's gate did fire — because the alternative, precision-based predicate happens to be satisfiable by degenerate trivial-predictability — is a direct architectural mismatch with the empirical commit-entry biology this paper anchors.

## How this translates to a substrate-design recommendation

There are two clean ways to bring REE into rough alignment with the Hanes-Schall posture:

1. **Replace the precision predicate with a readiness predicate.** Compute a readiness accumulator over the leading E3 candidate (or the top-k candidates' margin), and gate BetaGate entry on that accumulator crossing a criterion. Precision becomes either a biasing input to the accumulator (faster rise when prediction is tight) or a parallel constraint (the gate fires when *both* conditions hold). The latter is the conjunction architecture the GAP-4 question is weighing.

2. **Keep the precision predicate but add a readiness conjunction.** Less invasive: keep rv as one gate, AND it with a readiness threshold from the E3 scoring stage or from a nav_competence-style accumulator. This is the more conservative substrate change but preserves the spirit of the Hanes-Schall finding: commitment cannot fire on precision alone if there is no readiness signal also crossing.

Pass-2's Cisek-Kalaska entry argues for the more architecturally honest version (readiness-primary, precision-biasing); this Hanes-Schall entry supplies the empirical operationalisation (an accumulator-to-threshold, with the threshold being on a readiness representation).

## Limitations and caveats

The Hanes-Schall task is a discrete saccade in macaque FEF, not a sustained committed motor sequence in BG circuits. The transfer is at the level of architectural posture — the *form* of the predicate (readiness crossing a criterion) generalises across motor systems (saccadic, reaching, locomotor) and across structures (FEF, M1, SC, BG, premotor); the specific neural implementation differs. The strict constant-threshold claim from 1996 has also been refined by subsequent work (Boucher et al. 2007 interactive race / inhibition models, Reddi & Carpenter 2000 urgency signals, Pouget's normative accumulator framework). Modern accumulator models allow threshold modulation by urgency and value, but the architectural commitment to a readiness-crossing gate is preserved across the lineage.

The translation from a saccade-onset commit to a sustained committed-mode entry in REE is an inference. Saccades are discrete events; committed-mode entry is a state transition that opens a window. But the gating logic — "fire on a readiness-signal threshold crossing" — is what transfers, and the V3-EXQ-592 finding is exactly the failure the readiness-gating discipline prevents.

## Confidence reasoning

Source quality is very high: *Science* 1996, ~2000+ citations, dispositive for an entire modelling lineage. Mapping fidelity is moderate-to-high — architectural posture transfers cleanly even where neural implementation differs. Transfer risk is modest because the readiness-accumulator framework has been validated across multiple species, circuits, and motor domains. The `weakens` direction targets the rv-only predicate specifically; sub-claims about beta as a status-quo signal during sustained commitment are untouched (those are about what beta *does* once elevated; this paper is about what gates the elevation).
