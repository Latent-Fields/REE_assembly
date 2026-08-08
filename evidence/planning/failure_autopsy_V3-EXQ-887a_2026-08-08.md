# Failure Autopsy: V3-EXQ-887a (SD-014 node-valence sensitization retest)

Generated: `2026-08-08T06:33:36Z`
Scope: single
Status: confirmed

## Facts

- **Run**: `v3_exq_887a_sd014_node_valence_repfunc_sensitized_20260807T214013Z_v3`, queue_id `V3-EXQ-887a`, supersedes `v3_exq_887_sd014_node_valence_representational_functional_20260804T022547Z_v3`.
- **Purpose**: evidence. Claim: SD-014 only.
- **Dry-run check**: `check_dry_run_citations.py` on this run and its 887 predecessor -> 0 dry, clean. `dry_run: false` on the manifest.
- **Recording core**: `substrate_hash` present (`3a0409dd...`), `substrate_commit` (`7c41bbc8c2`, clean, branch main), `machine_class`, `elapsed_seconds`, full `config`, explicit `seeds: [42, 137, 2026]` all present. No recording gap.
- **Outcome**: FAIL. `evidence_direction: weakens` (as computed by the driver's combination rule).
- **Design**: byte-for-byte the V3-EXQ-887 instrument (P0 synthetic-control gate, R1-R4 readiness floors, C1/C2/C3 definitions) with exactly two substrate changes: (1) `incentive_sensitization_enabled=True` routing the WANTING write through a per-node, drive-coupled, saturating gain (`sensitization_rate=0.05`, `sensitization_max=4.0`, `sensitization_coupling=1.0`); (2) the rollout threads a live `drive_level = agent.compute_drive_level(body_obs)` into `agent.update_benefit_salience(benefit_exposure, drive_level)` every step (confirmed at driver line 532/541) -- without a real drive_level the sensitization gain is inert, so this is load-bearing.
- **Readiness gate**: green on all four preconditions (R1-R4), including the positive-control instrument check (synthetic orthogonal-peak control tau=0.197 vs ceiling 0.5). `non_degenerate: true`.
- **Criteria and combination rule**: PASS iff C1 (functional drive-gating, tau <= 0.85) AND C2 (representational separability, max|Spearman| <= 0.90) AND C3 (replay-set selectivity, Jaccard <= 0.80) hold on EVERY seed.
- **Per-seed result** (tau / max|Spearman| / Jaccard, thresholds 0.85 / 0.90 / 0.80):
  | Seed | tau (C1) | max\|Spearman\| (C2) | Jaccard (C3) | C1 | C2 | C3 |
  |---|---|---|---|---|---|---|
  | 42   | 0.8625 | 0.9248 | 0.619 | FAIL (+0.0125 over) | FAIL (+0.025 over) | PASS |
  | 137  | 0.8524 | 0.9193 | 0.639 | FAIL (+0.0024 over) | FAIL (+0.019 over) | PASS |
  | 2026 | 0.8352 | 0.8960 | 0.619 | PASS (-0.015 margin) | PASS (-0.004 margin) | PASS |
- **Compare to 887 (pre-fix)**: all three seeds failed C2 with max|Spearman| = 0.93-0.97 (0.03-0.07 over the 0.90 ceiling) -- a wide, uniform miss. Here the miss is narrow (0.019-0.025 over) on 2/3 seeds and one seed fully clears. This is a genuine, biologically-directed shift, not noise: seed 2026, the seed that clears, is also the seed with the *lowest* raw exposure (`n_resource_contacts=15`, `max_benefit_exposure=0.039` vs 24/0.070 and 29/0.095 for the failing seeds) -- i.e. dissociation tracked with something other than raw contact volume, consistent with a drive-level-gated (not exposure-count-gated) mechanism as designed.

## Claim-layer mapping

**SD-014** (design_decision, status: candidate, `depends_on: [ARC-036, SD-011, SD-012, MECH-030]`). Prior state: HOLD AT CANDIDATE, lit_conf=0.813, zero contributory experimental evidence until 887 (first genuine weakens). This is SD-014's second genuine experimental touchpoint and the direct retest of 887's own recommended fix.

## Biological-reference triage

- **Closest mechanism**: Smith/Berridge/Aldridge 2011 incentive-sensitization -- dopamine sensitization raises wanting without raising liking, the mechanistic basis for wanting/liking divergence over repeated exposure.
- **Is formal import**: no -- direct biological translation (per-node gain term keyed to homeostatic drive state), not a Pearl/Shannon/Bayesian formalism substituted for the mechanism.
- **Divergence**: none newly found. 887's autopsy already found and fixed the load-bearing divergence (wanting and liking both derived from one shared `benefit_exposure` signal via different monotone transforms). That fix is what this run retests.
- **Lit status**: present, `targeted_review_sd_014` (4 entries, lit_conf 0.813).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | fair, byte-identical-instrument retest of the exact fix 887's autopsy recommended |
| Biological reference | clear | Smith/Berridge/Aldridge 2011; direction of movement matches prediction |
| Prerequisites | present | SD-070/MECH-307 width fix + sensitization decouple both landed on `main` before this run |
| Implementation | partial | mechanism exists and is genuinely exercised (drive_level threaded live per step, confirmed in source), but default gain parameterization (rate 0.05, max 4.0, coupling 1.0) produces only marginal separation clustering at the threshold |
| Environment | adequate | unchanged from 887, itself judged a fair test |
| Measurement | adequate | instrument-verified via orthogonal synthetic control, unchanged from 887 |
| Integration | coupled correctly | decoupled write-path confirmed functioning (wanting genuinely diverges from liking, just not far enough on 2/3 seeds) |
| Scale | 3 seeds, all near threshold | not a clean uniform failure; small N amplifies borderline variance around a real but marginal effect |

## Learning extracted

- The incentive-sensitization decouple fix (887's routing) is a real, working, biologically-directed mechanism -- it moved the metric from a wide, uniform pre-fix miss (887: 0.93-0.97 vs ceiling 0.90) to a narrow, seed-dependent one (887a: 0.896-0.925), and produced one seed that fully clears both load-bearing criteria.
- The seed that clears is not the one with the most raw exposure -- consistent with the mechanism being genuinely drive-level-gated (as designed) rather than exposure-count-gated, which argues against "just run more episodes" as the fix and for "increase the gain magnitude" instead.
- This is the second consecutive genuine (non-artifactual) experimental touchpoint for SD-014, and both are now informative rather than non-contributory.

## Routing (user-confirmed)

**Same-claim retest with a stronger sensitization gain.** Record as a marginal/partial `weakens` -- real improvement, underpowered fix, explicitly distinguished from 887's clean full-collapse weakens. Route to `/queue-experiment` for **887b**: same instrument, `sensitization_rate` and/or `sensitization_coupling` raised from the current defaults, to test whether a stronger dose reliably clears the C1/C2 thresholds across seeds. Not a re-derive-brake case (0 prior `substrate_ceiling` hits on SD-014; the prior category was `standard`).

Draft `evidence_quality_note` for governance:

> V3-EXQ-887a (2026-08-07, FAIL, node_valence_collapsible_to_composite [retest]): retest of 887's autopsy-recommended incentive-sensitization decouple fix (ree-v3 `d8a94bd`), byte-identical instrument. Readiness gate green, instrument-verified, non-degenerate. Result is a genuine partial improvement, not a repeat of 887's uniform collapse: seed 2026 clears both load-bearing criteria (tau=0.835<=0.85, |Spearman|=0.896<=0.90); seeds 42/137 miss narrowly (tau 0.852-0.863, |Spearman| 0.919-0.925, vs 887's pre-fix range of 0.93-0.97). The clearing seed has the LOWEST raw resource exposure of the three, consistent with a genuinely drive-level-gated (not exposure-count-gated) mechanism. Routed to /queue-experiment (887b) with a stronger sensitization gain, not to substrate rebuild or claim demotion -- the mechanism is real and directionally correct, current default parameterization is underpowered.

## Substrate queue entry

`action: none` -- the substrate (SD-014 sensitized write-path) already exists and is functioning; 887b is a driver-level parameter override, not a new build.

## Re-derive brake

`fired: false` -- 0 prior `substrate_ceiling` hits for SD-014 (threshold 2). Prior category on 887 was `standard`.
