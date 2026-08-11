# Failure Autopsy: V3-EXQ-894c (MECH-074d BLA entropy-weight/MSE balance retune)

**Generated:** 2026-08-11T06:01:31Z
**Status:** confirmed
**Scope:** single
**Session:** diagnose-errors-8cdcaf

- **run_id:** `v3_exq_894c_mech074d_bla_entropy_weight_sweep_20260810T212602Z_v3`
- **queue_id:** V3-EXQ-894c
- **Outcome:** FAIL, `evidence_direction: mixed`
- **claim_ids:** `["MECH-074d"]`
- **experiment_purpose:** evidence
- **Dry-run check:** clean

## Facts

Fourth run in a sequential-narrowing lineage on MECH-074d's C2 (context-differentiated
addressing -- the Moita et al. 2004 threat/neutral dissociation this claim's own
falsifiability clause is built on):

| Run | Result | Hypothesis tested | Verdict |
|---|---|---|---|
| V3-EXQ-894 | FAIL/weakens | fixed non-trainable rule; over-firing/dilution suspected | C1/C2 fail 2/3 seeds |
| V3-EXQ-894a | FAIL/weakens | dilution (PE-sigma sweep [1.0,1.5,2.0,2.5]) | **REFUTED** -- Spearman -1.0 monotonic, structural not sampling noise |
| V3-EXQ-894b | FAIL/weakens | trainability alone (learnable head, single vs. doubled budget) | **REFUTED** -- C1 recovers fully (0/3->3/3) but C2 stays 0/3; doubling budget doesn't help |
| **V3-EXQ-894c (this run)** | FAIL, mixed | loss-term balance (entropy_weight retune [0.02,0.01,0.005,0.001], sigma held at 1.0) | **REFUTED** -- see below |

This run held sigma fixed at 1.0 (894a-closed), used a single P0-only training budget
(894b's own `training_budget_helps=False` finding licenses this), and swept ONLY
`entropy_weight` across 4 values plus a fixed-rule replication arm (`ARM_HEAD_FIXED`) and a
gate-shut drift control (`ARM_REMAP_OFF`). Pre-registered: PASS iff an entropy-weight arm
meets C1 AND C2 AND C3 AND C4 on >=2/3 of 3 seeds.

**Aggregate result:** `passing_arm_ids=[]`. Any-arm aggregate: C1=True, C2=**False**,
C3=True, C4=False. `attribution_recovers=True` (best_arm=ARM_EW_0p001) but
`dose_response_matches_docstring=False`.

### The raw per-cell data reveals a collapse mode the aggregate statistics obscure

Reading past the `jaccard_context_gap` (C2 statistic) into its two components
(`jaccard_within_on`, `jaccard_cross_on`) across all 15 scored (seed, arm) cells:

| seed | arm | ew | mass_excess | jac_gap | within | cross | C1 | C2 | C3 |
|---|---|---|---|---|---|---|---|---|---|
| 42 | HEAD_FIXED | 0.02 | 0.003 | -0.004 | 0.236 | 0.240 | F | F | F |
| 43 | HEAD_FIXED | 0.02 | 0.039 | 0.000 | **1.000** | **1.000** | F | F | T |
| 45 | HEAD_FIXED | 0.02 | 0.213 | 0.079 | 0.866 | 0.787 | T | **T** | T |
| 42 | EW_0.02 | 0.02 | 0.653 | 0.036 | 0.895 | 0.858 | T | F | T |
| 43 | EW_0.02 | 0.02 | 0.434 | 0.000 | **1.000** | **1.000** | T | F | T |
| 45 | EW_0.02 | 0.02 | 0.624 | -0.043 | 0.789 | 0.831 | T | F | T |
| 42 | EW_0.01 | 0.01 | 0.652 | 0.000 | **1.000** | **1.000** | T | F | T |
| 43 | EW_0.01 | 0.01 | 0.434 | 0.000 | **1.000** | **1.000** | T | F | T |
| 45 | EW_0.01 | 0.01 | 0.638 | 0.000 | **1.000** | **1.000** | T | F | T |
| 42 | EW_0.005 | 0.005 | 0.652 | 0.000 | **1.000** | **1.000** | T | F | T |
| 43 | EW_0.005 | 0.005 | 0.434 | 0.000 | **1.000** | **1.000** | T | F | T |
| 45 | EW_0.005 | 0.005 | 0.644 | 0.000 | **1.000** | **1.000** | T | F | T |
| 42 | EW_0.001 | 0.001 | 0.652 | 0.198 | 0.875 | 0.677 | T | **T** | T |
| 43 | EW_0.001 | 0.001 | 0.434 | 0.000 | **1.000** | **1.000** | T | F | T |
| 45 | EW_0.001 | 0.001 | 0.648 | 0.000 | **1.000** | **1.000** | T | F | T |

**10 of 15 cells (67%) show `within=cross=1.0000` exactly** -- not "low" context-sensitivity,
but complete saturation: the attribution head selects the IDENTICAL target set of codes on
every single measurement episode, both threat and neutral, with `n_jaccard_within_pairs=8000`
/ `n_jaccard_cross_pairs=4000` real pairs behind each figure (not a sample-size floor --
`ARM_REMAP_OFF`'s 0/0 pairs, correctly excluded from scoring, is the only genuine
floor-related zero in the table). This is a **deterministic collapse to a context-invariant
answer**, not a smoothly-graded loss of context sensitivity.

C2 clears the 0.05 margin in exactly 2 of 15 cells: seed45/ARM_HEAD_FIXED (the LEGACY
non-trainable rule -- not a trainable-head result at all) and seed42/ARM_EW_0p001 (the
smallest swept value, for one seed only). The collapse is concentrated at the middle two
swept values (0.01, 0.005), where ALL THREE seeds saturate; only the extremes (module
default 0.02, and 0.001) show any seed escaping it, and never more than one seed at a time.

**The docstring's own tradeoff theory is also undermined, not merely unconfirmed.**
`ree_core/amygdala/attribution_head.py` design decision (3) predicted mass_excess (C1
statistic) should RISE with entropy_weight (larger EW buys more peakedness) and
jaccard_gap (C2) should FALL with entropy_weight (larger EW costs context sensitivity) -- a
genuine tension/tradeoff. Observed: `spearman_mass_excess_vs_entropy_weight=-1.0` (mass_excess
FALLS as entropy_weight falls to 0.001 -- C1 gets BETTER as EW shrinks, the opposite of the
predicted direction) while `spearman_jaccard_gap_vs_entropy_weight=-0.949` (numerically
negative, nominally matching predicted direction, but this correlation is dominated by the
mid-range saturation floor rather than a smooth trend -- see table). There is no clean
tradeoff visible in the raw data: smaller entropy_weight is directionally somewhat better for
BOTH statistics at the extremes, with a collapse-prone plateau in between. `H0` (the
docstring's own falsification condition: "no swept value does better than the fixed rule on
C1 AND C2 -- the defect is deeper than the loss balance") is **confirmed**.

`fixed_unexpectedly_passed=false` at the aggregate level, but seed45's `ARM_HEAD_FIXED` cell
individually clears C1+C2+C3 (fails only the non-load-bearing C4) -- worth naming precisely:
the fixed, non-trainable legacy rule achieves genuine context-differentiation for ONE seed,
while the trainable head (built specifically to fix C2) achieves it for a DIFFERENT single
seed only at its smallest tested weight. Neither mechanism reliably clears C2.

## Claim-layer mapping

**MECH-074d** (`docs/claims/claims.yaml:9372`): "BLA analogue emits a remap_signal on harm-PE
spike when predictor-attribution flags specific latent codes -- partial (~one-third) remap,
NOT wholesale replacement." `status: provisional`, `epistemic_category: substrate_conditional`,
`pending_retest_after_substrate: true`. Depends on: MECH-074 (parent), SD-011 (z_harm_a),
ARC-033 (E2_harm_s forward model), ARC-007 (hippocampal map), MECH-073 (valenced hippocampal
map), SD-035 (amygdala substrate) -- all IMPLEMENTED. The claim's own falsifiability clause:
"if remap fires on sub-threshold PE or perturbs untagged codes uniformly, the attribution
gate is broken" -- this run's near-universal within=cross=1.0 saturation is directly on point
for that clause (perturbing an effectively context-untagged, invariant code set).

**Did the experiment test the claim under conditions where it could express itself?** Yes --
readiness gate green on every arm (no `structurally_vacuous_arms`), substrate wiring
pre-verified, matched-baseline design (per-episode ContextMemory restore prevents the
known slot-homogenization confound), single training budget licensed by 894b's own null
result. This is a fair test.

## Biological reference

Nader, Schafe & LeDoux 2000 (reconsolidation necessity) and Moita et al. 2004
(contextual-vs-auditory dissociation, Z=-1.36 vs -0.34, p=0.02) are both directly cited in
the claim's literature basis -- a real, well-grounded connectome mechanism, not a
formal-definition import. C1 (attribution selectivity/peakedness) is now robustly supported
across every trainable-head arm and seed (0/3 -> 3/3 since 894b) -- the "WHAT to attend to"
half of the mechanism is functioning. C2 (context-conditional addressing) is the harder,
repeatedly-refuted half. The collapse-to-deterministic-answer failure mode observed here
biologically resembles a system that has learned salience (which features/codes matter) but
not context-gating (conditioning that salience on which context it is in) -- a specific,
falsifiable framing distinct from "needs more training" (894b) or "needs different loss
weighting" (this run). This maps onto the claim's own dependency list: if the representation
the attribution head reads from (fed via SD-011 z_harm_a / ARC-033 E2_harm_s) does not itself
carry a reliable context-discriminating signal, no amount of downstream retuning -- of
either the gate threshold or the loss weighting -- can produce genuine context-conditional
attribution.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | H0 confirmed; C2 fails under a 4th structurally distinct manipulation |
| Biological reference | clear | Nader 2000 + Moita 2004 directly cited; collapse-to-invariant-answer maps onto "learned salience without context-gating" |
| Prerequisites | present | SD-011, ARC-033, ARC-007, MECH-073, SD-035 all implemented |
| Implementation completeness | complete for C1 mechanism; **likely architecturally underspecified for C2** | the attribution head has no explicit mechanism forcing context-conditional output -- its loss (peakedness + accuracy) does not penalize context-invariance directly, so gradient descent can (and mostly does) settle on a fixed-answer local optimum that still minimizes both loss terms |
| Environment adequacy | adequate | alternating threat/neutral episodes, matched-baseline restore, sufficient window sizes (MIN_WINDOWS_PER_CONTEXT=4, cleared every green cell) |
| Measurement adequacy | adequate, with a real caveat | the bare `jaccard_context_gap` (arm-level mean) hides the within=cross=1.0 saturation that dominates 10/15 cells; reading the raw within/cross components was necessary to see the collapse mode at all |
| Integration adequacy | adequate | measurement wraps the single entry point (`_get_context_memory_code_contributions`) both fixed and trainable implementations dispatch through |
| Scale/capacity | adequate | 3 seeds x 6 arms, single training budget per 894b's own budget-null finding |

**Failure-location (GOV-FAILLOC-1):** Implementation is the dominant bucket -- the C2
mechanism appears absent/underspecified (no explicit context-conditioning term), not merely
mistuned. Measurement is adequate but required raw-component inspection to reveal the true
shape of the failure (aggregate statistics alone were misleading). Environment is adequate.
Net: **MECHANISM implicated** (a real implementation/architecture gap in context-conditioning),
not a broad "REE FAILED" read, and not chargeable to environment or measurement design.

## Repair pathway

`complex (probe-gated) / mystery (known data)` -- extensive data already exists (4 independent
experiments, 6 arms, 3 seeds, full within/cross-context breakdown); the frame needs
reworking, not more sweep data at the same granularity. **Refusing a 5th same-question
lettered hyperparameter sweep (894d)** -- H0 already establishes that no tested entropy_weight
value, and by extension no simple scalar retune of THIS loss formulation, recovers C2.

**Routing: `/implement-substrate`, amend SD-035.** User-confirmed at the Step 8 gate (plain
routing, not the broader GOV-FANOUT-1 portfolio option). Supersede the 894b failure_record
target ("retuned entropy_weight/MSE balance", currently `resolved: open`) with a narrower one:
investigate whether the attribution head's input representation carries a
context-discriminating signal at all, and/or add an explicit context-conditioning mechanism
to the head (rather than relying on the entropy/MSE loss balance alone to induce one).
`severity=degrading` (the built mechanism computes/fires/writes correctly and produces
genuine, reproducible data -- the gap is in what it has learned to represent, not a
corrupting defect).

**Granularity-debt check (fires):** C1 (attribution selectivity) is now robustly supported
(0/3 -> 3/3 seeds across every trainable-head arm, every entropy_weight). C2
(context-differentiated addressing -- the actual Moita 2004 dissociation MECH-074d's
falsifiability clause is built on) has failed under 4 structurally distinct manipulations:
dilution/threshold (894a), trainability-alone (894b), training budget (894b), loss-term
balance (894c, this run). `granularity_debt_cluster.py MECH-074d` confirms `weakened=2,
intact=1` across the 3 prior confirmed autopsies (894c's own read makes it `weakened=3` of
4). **Recommend `/claim-synthesis`**, user-confirmed at the Step 8 gate: split MECH-074d into
a selectivity child (well-supported, candidate for promotion) and a context-addressing child
(the harder, repeatedly-refuted Moita dissociation specifically), so each gets its own
re-derive-brake count and governance treatment rather than one coarse claim absorbing both a
success and a persistent, structurally-narrowing failure.

**Re-derive brake:** does NOT fire mechanically. Counted via the R1-R3 convention
(`REE_Working/scripts` recipe) against the 3 prior confirmed autopsies: 0 `substrate_ceiling`
hits for MECH-074d (894 -> `standard`, 894a -> `competence_implementation_gap` [note: this is
an out-of-enum stamp on that prior artifact, not addressed here -- outside this autopsy's
scope; not propagated into this artifact's own `recommended_epistemic_category`], 894b ->
`standard`). The brake's R3 restriction (only `substrate_ceiling` counts) is a deliberate,
narrower net than "any repeated FAIL" -- this lineage's repeated FAILs are a genuine
implementation/architecture gap, correctly routed to `/implement-substrate` on the merits
(the four-layer diagnosis above), not because a mechanical brake threshold fired.

## Draft `evidence_quality_note` (not written -- for governance)

> [/failure-autopsy 2026-08-11, V3-EXQ-894c, confirmed failure_autopsy_V3-EXQ-894c_2026-08-11,
> entropy_weight/MSE balance retune]: H0 confirmed -- no swept entropy_weight value
> ([0.02,0.01,0.005,0.001], sigma fixed at 1.0) recovers C1 AND C2 on >=2/3 seeds for any arm
> (passing_arm_ids=[]). Reading past the aggregate jaccard_context_gap statistic into its raw
> within/cross-context components reveals the attribution head collapses to a fully
> deterministic, context-invariant target-set selection (within=cross=1.0000 exactly) in 10 of
> 15 scored cells -- concentrated at the middle two swept values, with only the extremes
> (module default 0.02, and the smallest 0.001) showing partial, single-seed escape. The
> module's own predicted C1-vs-C2 tradeoff is also NOT supported by the data (C1's mass_excess
> statistic improves, not degrades, as entropy_weight falls -- opposite the predicted
> direction). Diagnosis: the defect looks like an architecture/optimization gap (the head has
> no explicit mechanism forcing context-conditional output) rather than a loss-weighting
> tuning problem. Three iterations (894a/894b/894c) have now progressively eliminated
> dilution, trainability-alone, and loss-balance-alone -- C1 (selectivity) is robustly
> resolved (0/3->3/3); C2 (context-addressing, the actual Moita 2004 dissociation) remains
> unresolved across all four manipulations. routing=implement-substrate: substrate_queue.json
> SD-035 entry to be amended with this failure_record, superseding the 894b
> "retuned entropy_weight/MSE balance" target with a narrower one (investigate the head's
> context-representation input / add explicit context-conditioning). Granularity-debt trigger
> FIRES: recommend /claim-synthesis split MECH-074d into a selectivity child and a
> context-addressing child. Stays provisional / pending_retest_after_substrate.
