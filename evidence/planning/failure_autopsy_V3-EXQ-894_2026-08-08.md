# Failure Autopsy: V3-EXQ-894 (MECH-074d BLA remap attribution selectivity)

Generated: `2026-08-08T06:33:36Z`
Scope: single
Status: confirmed

## Facts

- **Run**: `v3_exq_894_mech074d_bla_remap_attribution_selectivity_20260808T005219Z_v3`, queue_id `V3-EXQ-894`. First-ever autopsy for MECH-074d (freshly built GOV-CONFIRM-1 confirmer, routed from IGW-20260807-235; lit_conf 0.809, prior `genuine_exp_count 0`).
- **Purpose**: evidence. Claim: MECH-074d only.
- **Dry-run check**: `check_dry_run_citations.py` -> 0 dry, clean. `dry_run` not set / falsy on manifest.
- **Recording core**: `substrate_hash` present (`dd04a2959...`), `substrate_commit` (`b575405e95`, clean, branch main), `machine_class`, `elapsed_seconds`, full `config`, explicit `seeds: [42, 43, 45]`. No recording gap.
- **Design**: 2 arms x 3 seeds, matched-baseline repeated-measures. `ARM_REMAP_ON` (`bla_remap_pe_sigma_threshold=1.0`, the SD-035 default) vs `ARM_REMAP_OFF` (threshold `1e9`, gate never opens). Both arms leave P0 from an identical differentiated `ContextMemory` snapshot restored at the start of every measurement episode, specifically to prevent the remap from destroying its own measurement substrate before the DV is read (verified in a same-day smoke: unrestored, the gate drove slot differentiation from 0.089 to 2.7e-6 -- total homogenisation -- within one episode). Substrate wiring pre-verified by probe (`use_e2_harm_a=True` confirmed load-bearing: without it `bla._n_remap == 0` over 296 ticks; with it, 72 fires / 137 ticks).
- **Readiness gate**: green on all 18 preconditions across both arms and all three seeds (slot differentiation, PE spread, remap-events-sufficient, both-contexts-fired). `non_degenerate: true`.
- **Criteria and combination rule**: PASS iff C1 (attribution_selectivity, load-bearing) AND C2 (context_differentiated_addressing, load-bearing) AND C3 (partial_not_wholesale, load-bearing) AND C4 (pe_spike_sparsity, supporting) hold on >= 2 of 3 seeds (`SEEDS_PASS_MIN=2`).
- **Per-seed result**:
  | Seed | attr_mass_excess (C1, margin>0.05) | jaccard_gap (C2, margin>0.05) | fire_fraction (C4, ceil 0.25) | C1 | C2 | C3 | C4 |
  |---|---|---|---|---|---|---|---|
  | 42 | 0.0026 | -0.0043 | 0.591 | FAIL (near chance) | FAIL (negative) | FAIL | FAIL |
  | 43 | 0.0383 | 0.0000 | 0.907 | FAIL (below margin) | FAIL (exactly zero -- same 5 slots every fire) | PASS | FAIL |
  | 45 | 0.2131 | 0.0790 | 0.411 | PASS (wide margin) | PASS | PASS | FAIL |
- **Seeds-ok tally**: C1=1/3 (not met, needs >=2), C2=1/3 (not met), C3=2/3 (met), C4=0/3 (not met). Attribution-gate half (C1+C2, the Moita 2004 dissociation) fails structurally; partiality half (C3) passes.
- **Notable pattern**: fire_fraction is inversely correlated with attribution signal across the three seeds -- the seed with the lowest fire fraction (45, 0.411) is the only one showing real C1/C2 signal; the two highest-fire-fraction seeds (42 at 0.591, 43 at 0.907) are the two that read near chance. All three seeds blow the C4 sparsity ceiling (0.25) regardless. The driver's own pilot-probe docstring (one seed, 12 warmup episodes) had already recorded fire fraction ~0.5 and near-chance attribution entropy (0.9999) before the full run -- this risk was visible pre-registration, not discovered only after the fact.

## Claim-layer mapping

**MECH-074d** (mechanism_hypothesis, status: provisional, `depends_on: [MECH-074, SD-011, ARC-033, ARC-007, MECH-073, SD-035]`). Registered 2026-04-21 as split child of MECH-074. Load-bearing literature: Nader/Schafe/LeDoux 2000 (reconsolidation necessity, conf 0.80), Moita et al 2004 (contextual-vs-auditory dissociation mandating attribution gating, conf 0.78). This is the claim's first-ever experimental evidence of any kind (previously 0 experimental entries; latest prior touchpoint was a 2026-04-25 lit citation, and the one prior run tagging MECH-074d, V3-EXQ-474, was a synthetic-PE module-boundary diagnostic that never exercised a live agent).

## Biological-reference triage

- **Closest mechanism**: Moita et al 2004 contextual-vs-auditory fear conditioning dissociation -- BLA-driven attribution gating that selectively targets context-predictive representations rather than broadcasting to all stored codes.
- **Is formal import**: no -- direct architectural translation (a PE-gated, attribution-weighted partial remap of a slot-based context store).
- **Divergence**: none newly identified in source; the substrate wiring was pre-verified correct by probe before the run (candidate computation, remap gate, write path all confirmed at the cited line numbers).
- **Lit status**: present, load-bearing (Nader 2000, Moita 2004; part of the 9-entry `targeted_review_connectome_mech_074`).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | first fair test; substrate wiring pre-verified by probe, matched-baseline design specifically engineered to avoid self-inflicted degeneracy |
| Biological reference | clear | Moita 2004 dissociation; the claim's own falsifier is stated at exactly the representation level this design tests |
| Prerequisites | present | SD-035 BLAAnalog built and confirmed exercised (candidates, remap gate, write path all fire) |
| Implementation | complete, but calibration in question | the attribution mechanism computes and writes correctly (verified by probe and by seed 45's clean positive result); whether the DEFAULT PE-sigma threshold (1.0) is well-calibrated for this environment is the open question -- normal-theory expectation for a >1-SD PE excursion is ~0.16 fire rate, measured fire rates are 0.41-0.91 |
| Environment | adequate | threat/neutral alternation, scheduled limb-damage injection all functioning per readiness gates |
| Measurement | adequate | matched-baseline repeated-measures design is unusually careful (restore-to-snapshot per episode specifically to prevent the remap from destroying its own measurement substrate) |
| Integration | coupled correctly | wiring pre-verified by targeted probe before the run, not inferred after the fact |
| Scale | 3 seeds, bimodal not uniform | 2/3 near-chance, 1/3 clearly positive -- a real qualitative split, not simple underpowering |

## Confound noted (user-instructed: flag explicitly, do not treat as settled)

Fire-fraction and attribution-selectivity are inversely related across the three seeds. This is consistent with the remap gate's PE-sigma threshold being calibrated too permissively for this environment, so that frequent, low-selectivity fires dilute/destroy a genuine underlying attribution signal in the higher-fire-fraction seeds, while the lower-fire-fraction seed (45) preserves enough signal to show real selectivity. This is a plausible alternative to "the attribution mechanism is fundamentally absent" and is NOT verified here -- 3 seeds is not enough to establish the correlation is causal rather than coincidental. It is recorded as a hypothesis for a follow-up probe, not as the confirmed explanation for the FAIL.

## Learning extracted

- MECH-074d's substrate is built and functioning (candidates compute, remap gate fires under the confirmed-necessary `use_e2_harm_a=True` flag, writes land) -- this is not an implementation-absence FAIL.
- The attribution-gate half of the claim (C1+C2, the Moita dissociation) fails on 2/3 seeds under a green, well-instrumented, non-degenerate gate -- a genuine weakens as measured.
- The partiality half (C3, "not wholesale replacement") holds on 2/3 seeds -- the remap is not blowing away the whole store, even when attribution selectivity is weak.
- All three seeds blow the C4 sparsity ceiling, and the driver's own pre-registered pilot probe already anticipated this -- the SD-035 default sigma threshold (1.0) may simply be too permissive for this environment's PE distribution.
- The fire-fraction / selectivity anti-correlation across seeds is a concrete, testable hypothesis for why the gate reads as vacuous in 2/3 seeds without requiring the attribution mechanism itself to be absent.

## Routing (user-confirmed)

**Flag the sigma-threshold over-firing confound explicitly; route to a recalibration retest.** Record as `weakens` per the pre-registered combination rule, with the confound noted above as an alternative explanation warranting follow-up before this is read as strong evidence against the attribution-gating mechanism itself. Route to `/queue-experiment` for **894a**: same instrument, `bla_remap_pe_sigma_threshold` raised to bring the fire fraction toward the driver's own pre-registered ~0.25 expectation, to test directly whether attribution selectivity becomes reliably detectable once firing frequency is controlled.

Draft `evidence_quality_note` for governance:

> V3-EXQ-894 (2026-08-08, FAIL, mech074d_attribution_gate_vacuous_and_remap_wholesale): first genuine experimental evidence for MECH-074d. Readiness gate green (18/18 preconditions), substrate wiring pre-verified by probe, non-degenerate, matched-baseline design. Attribution-gate half (C1 attribution_selectivity, C2 context_differentiated_addressing -- the Moita 2004 dissociation) fails on 2/3 seeds; partiality half (C3) holds on 2/3. Confound flagged, not resolved: fire_fraction is inversely correlated with attribution signal across the 3 seeds (the one seed with real signal has the lowest fire fraction; the two near-chance seeds have the two highest), consistent with the SD-035 default PE-sigma threshold (1.0) over-firing and diluting a genuine signal rather than the attribution mechanism being architecturally absent. All three seeds also blow the C4 sparsity ceiling, which the driver's own pre-registered pilot probe already anticipated. Routed to /queue-experiment (894a) with a recalibrated sigma threshold to test the over-firing hypothesis directly before this FAIL is weighted as strong evidence against the attribution-gating mechanism.

## Substrate queue entry

`action: none` -- no new build required; 894a is a driver-level threshold override testing whether the existing SD-035 default needs recalibrating, not a new substrate component. If 894a confirms the over-firing hypothesis, THAT would be the point to consider amending the SD-035 default via `/implement-substrate`.

## Re-derive brake

`fired: false` -- 0 prior `substrate_ceiling` (or any) autopsy targets tag MECH-074d; this is its first.
