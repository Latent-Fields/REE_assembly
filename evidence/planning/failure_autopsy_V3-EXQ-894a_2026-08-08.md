# Failure Autopsy: V3-EXQ-894a (MECH-074d, BLA remap attribution selectivity)

**Generated:** 2026-08-08T16:39:36Z
**Scope:** single
**Status:** confirmed (Step 8 interactive gate: user confirmed `implement-substrate`)

## 1. Facts

Run: `v3_exq_894a_mech074d_bla_remap_attribution_selectivity_20260808T101157Z_v3` (queue V3-EXQ-894a, machine `ree-cloud-2`, elapsed 1850.3s). `dry_run` confirmed false. `validate_recording.py`: OK, full always-core present (`substrate_hash`, `config`, `seeds: [42,43,45]`, `machine_class`).

This is a same-claim, same-design **retest** superseding `V3-EXQ-894` (also FAIL, `standard`, autopsied same-day, `confirmed`). 894a is that autopsy's own routed follow-on: identical instrument, one design change — the fixed PE-sigma threshold (1.0) becomes a 4-point sweep `[1.0, 1.5, 2.0, 2.5]`, targeting 894's own flagged confound ("fire-fraction inversely correlated with attribution signal across seeds — consistent with an over-permissive gate diluting a genuine signal").

Design: 5 arms x 3 seeds `[42,43,45]` (44 excluded, standing early-episode-death instability). `ARM_REMAP_OFF` (drift control) + 4 ON arms at increasing sigma. Matched-baseline repeated-measures (ContextMemory restored to end-of-P0 snapshot each measurement episode). `use_e2_harm_a=True` held identical across arms (confirmed load-bearing by 894's probe).

`non_degenerate: true`. `ARM_SIGMA_25` correctly scored out (readiness gate fails: `remap_events_sufficient`, `both_contexts_fired` — seed 45 fire rate collapses to zero at sigma 2.5), per the V3-EXQ-785 scored-out convention. Three arms actually scored: SIGMA_10/15/20.

`outcome: FAIL`, `evidence_direction: weakens`, `interpretation.label: mech074d_attribution_gate_vacuous_across_sigma_sweep`, `passing_arm_ids: []`.

| Arm (sigma) | C1 seeds-ok/3 | C2 seeds-ok/3 | mean attr_mass_excess | mean fire_frac | mean jaccard_gap |
|---|---|---|---|---|---|
| 1.0 | 1 | 1 | 0.0847 | 0.637 | +0.0249 |
| 1.5 | 1 | 0 | 0.0773 | 0.402 | +0.0046 |
| 2.0 | 1 | 0 | 0.0573 | 0.243 | -0.0106 |
| (2.5, red/unscored) | 0 | 0 | 0.0074 | 0.086 | -0.0189 |

`SEEDS_PASS_MIN=2` — no arm ever reaches 2/3 on load-bearing C1 or C2. **Decisive number: `dose_response.spearman_mass_excess_vs_sigma = -1.0`**, paired with `spearman_fire_fraction_vs_sigma = -1.0` — perfectly monotone, moving *together*. This directly refutes the over-firing/dilution hypothesis 894 raised: dilution predicts attribution excess should *rise* as fire fraction falls (restricting to rarer, larger PE excursions purifies the signal); instead both fall in lock-step. Per-seed data confirm this isn't one outlier seed: seed 45 decays 0.213 -> 0.192 -> 0.135 -> 0.000; seed 42 stays near-chance/negative throughout; seed 43 holds an exactly-zero jaccard_gap at every threshold (same ~5 slots selected regardless of context — context-blind, deterministic, not noisy). The seed ranking (45 best, 43 context-blind, 42 null) is stable across all four thresholds.

## 2. Claim-layer mapping

MECH-074d (`mechanism_hypothesis`, `status: provisional`, `implementation_phase: v3`, `v3_pending: false`). `depends_on: [MECH-074, SD-011, ARC-033, ARC-007, MECH-073, SD-035]`. Registered 2026-04-21 as a split child of MECH-074, with its own text already stating: *"For the initial non-trainable pass this is approximated by selecting codes whose contribution to the harm-PE exceeds a threshold; a learnable attribution head is deferred."* Falsifier: *"if remap fires on sub-threshold PE or perturbs untagged codes uniformly, the attribution gate is broken."*

`claim_ids` accurate on both manifests — tests exactly the attribution gate at the representation level the claim's own falsifier specifies.

Tested fairly, with a caveat: the instrument is unusually careful (readiness gate, matched-baseline restore, DV-symmetry declaration, pre-verified wiring). But the claim as registered names two components — the PE-threshold gate (a), and a "predictor-attribution head" which the claim text itself pre-announces as a non-trainable placeholder with a learnable version deliberately deferred (b). 894a tested whether recalibrating (a) recovers selectivity from (b); it does not. That rules out (a) as sole cause but does not distinguish "the biological mechanism is wrong" from "the deferred, known-incomplete stand-in for (b) cannot express selective attribution regardless of (a)."

## 3. Biological-reference triage

Closest mammalian reference: **Moita et al. 2004** (context-vs-tone fear conditioning place-cell/BLA remapping dissociation, Z=-1.36 vs -0.34, p=0.02) — already cited, load-bearing, in `evidence/literature/targeted_review_connectome_mech_074/`. This is the correct anchor: real amygdala-driven consolidation-time remapping is selective for context-predictive representations, not a broadcast update — exactly what C1/C2 operationalize. **Nader, Schafe & LeDoux 2000** (reconsolidation necessity) supports the PE-triggered-update half. `lit_status: present` — no `/lit-pull` commission indicated.

Faithful translation of the mechanism *class* (PE-gated, attribution-weighted partial remap), not a formal-definition import. The specific attribution computation, however, is explicitly a placeholder: a fixed, non-trainable contribution-threshold rule standing in for the claim's own promised "learnable attribution head." Real BLA attribution is a *learned* cue-outcome association built up over experience (Moita 2004's own dissociation develops over training) — a fixed, context-agnostic threshold rule has no mechanism by which it could become more selective with more experience. The observed signature (one genuinely selective seed, one context-blind-but-deterministic seed, one null seed, invariant to threshold recalibration) is consistent with a computation that has no learned component to differentiate cases.

This matches the skill's "missing prerequisite" default reading, and unusually strongly: the claim's own registration text named the missing dependency in advance, rather than this autopsy discovering it after the fact.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | Fair test; the specific alternative (over-firing dilution) is now cleanly refuted (Spearman -1.0 on both axes, moving together not inversely). |
| Biological reference | clear | Moita 2004 dissociation is the correct, present, load-bearing anchor; claim's own falsifier tested at the right representation level. |
| Prerequisites | present | SD-011, ARC-033, SD-035 all built and confirmed exercised by probe pre-run. |
| Implementation completeness | **partial/stub — dominant layer** | Gate mechanics (fire, write, partial-not-wholesale) work; attribution component is an explicitly-declared non-trainable placeholder. Stable across 4 thresholds and 2 experiments — not a tuning artifact. |
| Environment | adequate | PE genuinely varies, slots genuinely differentiated at window start. |
| Measurement | adequate, unusually careful | Matched-baseline restore-per-episode; pre-registered DV-symmetry and combination rule. |
| Integration | coupled correctly | Wiring pre-verified by probe before either run. |
| Scale/capacity | seed-heterogeneous, not ordinary underpowering | Same 3-way seed pattern recurs identically across both experiments and all 4 thresholds — reads as a structural property of the non-trainable rule, not sampling noise. |

## 5. Recommended epistemic_category / evidence_direction / evidence_quality_note

`epistemic_category: competence_implementation_gap` (a specifically-named, not-yet-built component, not a broader information-carrying ceiling; `substrate_ceiling` was flagged as a defensible alternative reading but routes to the same place — governance may relabel without re-opening the diagnosis). `evidence_direction: weakens` (matches manifest).

> V3-EXQ-894a (2026-08-08, FAIL, mech074d_attribution_gate_vacuous_across_sigma_sweep): recalibrated-threshold retest of V3-EXQ-894, sweeping `bla_remap_pe_sigma_threshold` over [1.0,1.5,2.0,2.5] to test 894's over-firing/dilution hypothesis. Refuted: mean attribution-mass-excess falls monotonically with sigma (Spearman -1.0), tracking the fall in fire-fraction rather than diverging as dilution would predict; per-seed ranking (one selective, one context-blind-deterministic, one null) stable across all four thresholds. C1/C2 (Moita 2004 dissociation) never reach 2/3 seeds at any scored threshold; C3 (partiality) holds throughout. Readiness/recording clean. Diagnosis: recalibration confound closed; MECH-074d's attribution computation is, by the claim's own 2026-04-21 text, a non-trainable threshold placeholder with a learnable head explicitly deferred as "a deliberate second pass" — substrate has the symbol of attribution gating but not the learned functional component to discriminate context-predictive from incidental codes. Routed `/implement-substrate` (build the deferred learnable attribution head); MECH-074d stays `provisional`/`pending_retest_after_substrate`, not demoted.

## 6. Recommended routing — CONFIRMED implement-substrate

User-confirmed at Step 8 (2026-08-08). `complicated (buildable)`, not `complex (probe-gated)`: the claim's own registration text already named the missing component as a planned second pass; the sweep closed off the one live alternative-hypothesis question. No further diagnostic probe indicated.

Not routing to `/queue-experiment` for a 894b same-claim retest — the two live parameters in the non-trainable design (threshold, attribution rule) have both now been exercised and both point at the same wall.

**Re-derive brake: does NOT fire.** Under R1-R3 (unit=run, latest-adjudication-wins, substrate_ceiling-only), 894 was categorized `standard` (0 ceiling hits). This would be the first ceiling-adjacent (`competence_implementation_gap`) reading for MECH-074d — well below threshold=2.

**Substrate queue entry:**

```json
{
  "action": "amend",
  "target_sd_id": "SD-035",
  "title_addendum": "BLAAnalog attribution head: promote non-trainable threshold heuristic to a learnable/trainable head",
  "implementation_hint": "SD-035's BLAAnalog currently approximates predictor-attribution by a fixed, non-trainable contribution-threshold rule over candidate latent codes (ree_core/amygdala/bla.py:472-531 remap gate; ree_core/agent.py:4450-4453 candidate computation via slot-attention softmax over ContextMemory; ree_core/agent.py:4488-4493 fire dispatch; ree_core/agent.py:3889-3913 the write). Two independent experiments (V3-EXQ-894, V3-EXQ-894a) show context-selectivity does not respond to PE-threshold recalibration across a 4-point sweep -- per-seed outcome stable regardless of threshold, consistent with a rule with no learned component to differentiate genuinely context-predictive codes from incidentally-high-contribution ones. Build: replace/augment the fixed-threshold candidate selection with a trainable attribution/gating head, validated against the same C1/C2 instrument already proven informative by 894/894a.",
  "unblocks_claims": ["MECH-074d"],
  "depends_on_unresolved": [],
  "priority_suggested": 2,
  "severity": "degrading",
  "substrate_paths": ["ree_core/amygdala/bla.py", "ree_core/agent.py"],
  "failure_record_entry": {
    "run_id": "v3_exq_894a_mech074d_bla_remap_attribution_selectivity_20260808T101157Z_v3",
    "experiment_type": "v3_exq_894a_mech074d_bla_remap_attribution_selectivity",
    "metric": "C1 attribution_mass_excess / C2 context_jaccard_gap never reach 2/3-seed pass at any of 4 swept PE-sigma thresholds; mass-excess and fire-fraction both fall monotonically with sigma (Spearman -1.0 both), refuting the over-firing/dilution alternative from V3-EXQ-894",
    "target": "attribution_mass_excess > 0.05 AND context_jaccard_gap > 0.05 on >=2/3 seeds, at some operating point, under a trainable attribution head",
    "resolved": "open"
  }
}
```

Drafted as `amend` to SD-035 (a targeted capability addition to an already-implemented module) rather than `create` of a new SD-XXX; governance may instead prefer spinning off a dedicated SD-035b — flagged, not presumed.

## 7. Learning extracted

- BLAAnalog's mechanical gate (candidates compute, gate fires under confirmed-necessary `use_e2_harm_a=True`, writes land, partiality holds) is correctly implemented — this is not an implementation-absence FAIL.
- The over-firing/dilution alternative is now closed off by direct test.
- The 3-seed pattern (selective / context-blind-deterministic / null) is stable across two independent experiments and four threshold settings — a structural property of the current non-trainable rule, not sampling noise.
- Dominant explanation: implementation completeness, not biology or claim falsification — the claim's own text pre-announced the attribution head as a placeholder pending "a deliberate second pass."
- Recording/instrumentation practice on this pair is a positive example: full recording core, pre-registered thresholds, explicit DV-symmetry, matched-baseline restore, correct scored-vs-red arm handling (V3-EXQ-785 pattern applied correctly).

## 8. Re-derive brake / granularity-debt recurrence

Re-derive brake does not fire (see above). Granularity-debt recurrence does not fire either: `granularity_debt_cluster.py MECH-074d` shows 1 prior target (894, `intact`/`standard`), and 894/894a are not structurally different failure shapes — they are the same instrument testing the same single confound at four points along one dimension, a converging investigation reaching a clean answer, not a claim circled by qualitatively different failure modes. No `/claim-synthesis` recommendation.

Note for governance: worth separately checking whether MECH-074b's retrieval_bias head shares the same non-trainable-placeholder pattern before finalizing SD-035's scope — not verified in this autopsy.
