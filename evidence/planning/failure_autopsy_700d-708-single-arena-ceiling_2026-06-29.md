# Failure Autopsy — V3-EXQ-700d + V3-EXQ-708 (single-arena conversion ceiling, convergent cluster)

- **Generated (UTC):** 2026-06-29T05:56:09Z
- **Scope:** cluster (2 targets, structurally-different claims, one structural property)
- **Status:** confirmed (interactive gate cleared 2026-06-29; route confirmed + claim-synthesis flag added on MECH-439)
- **Invoked inline** under the `/governance` session claim `governance-cycle-20260629T0533Z` (covers `evidence/planning/`).

---

## 1. Scope

Two pending FAILs, both `outcome=FAIL` / `evidence_direction=non_contributory` / self-routed
`interpretation.label=substrate_not_ready_requeue`, sharing one failure shape:

| Target | run_id | claims | purpose | supersedes |
|---|---|---|---|---|
| V3-EXQ-700d | `v3_exq_700d_arc108_sec7_learned_gating_settling_samelayer_null_retune_20260627T221359Z_v3` | MECH-439, ARC-108, MECH-450 | evidence | V3-EXQ-700c |
| V3-EXQ-708 | `v3_exq_708_mech440_noisy_selection_head_propagation_falsifier_20260628T220908Z_v3` | MECH-440 | diagnostic | — |

Both ran to completion (no crash). 708 carries the indexer `precondition_unmet` adjudication
flag; 700d (purpose=evidence) is unflagged but un-autopsied. Cluster justified: convergent
failure across **structurally different** claims (a same-layer-null validity test vs a
noise-injection-site falsifier) on the **same underlying substrate property**.

## 2. Facts reconstruction

### V3-EXQ-700d — magnitude-matched same-layer null still inert/destructive
The validity re-tune of the 700-lineage same-layer null. The single change from 700c was to
auto-compute the frozen-random W_lat null scale at run time to 1.0x the in-run median LEARNED
W_lat range of the A2/A3 signed settling arms. **The fix worked** —
`field_noise_magnitude_matched` = 1.0 (band [0.25, 4.0]), correcting 700c's 41.42x miss.
But the correctly-sized null **still** failed the two discrimination preconditions:

- `matched_noise_control_verified_lifting`: measured **0.0**, threshold 2.0 → **FAIL** (the
  magnitude-matched null did not verify-lift committed-class entropy on the divergent seeds).
- `same_layer_null_not_destructive`: measured **1.0**, threshold 2.0 → **FAIL** (the null
  drove committed-class entropy below A0).

All absolute / non-vacuity preconditions PASSED: `enough_divergent_seeds` 4/3,
`learned_settling_range_non_vacuous` 0.0316 > 0.005, `delta_t_carries_variance_on_learning_arms`,
`learned_weights_moved_from_init_on_armed_arms`, `candidate_pool_divergent_focus_arms`.

The pre-registered terminal ("a magnitude-matched null that VERIFY-LIFTS while learned settling
still does NOT lift → escalate ARC-110, trip the brake-LOCK") **did not fire** — because the null
could not be made valid. This is the **3rd consecutive failed construction** of a valid
committed-class same-layer null in the V3 single arena: 700b (decoupled) → 700c (41.42x) →
700d (matched-but-inert).

### V3-EXQ-708 — injected weight noise washes at the F-dominated argmax
4-arm noise-injection-site falsifier (A0_OFF / ARM_TEMP / ARM_NOISE_SINGLE / ARM_NOISE_LOOPSEG)
on the 569i top-k + MECH-448 demotion SOTA conversion stack; the only swept factor is the
exploration-injection site. Failed discrimination preconditions:

- `temperature_control_raises_precommit_entropy`: measured **0.0**, threshold 2.0 → **FAIL**.
- `weight_noise_raises_precommit_entropy`: measured **0.0**, threshold 2.0 → **FAIL**.

Critically, the noise was genuinely injected — `noise_bias_range_supra_floor_vs_raw` = 0.2216
(supra-floor), `dacc_suppression_live` ✓, `loopseg_arm_carries_live_cross_loop_variance` 6.0 ✓,
`learning_engaged_finer_channels_dissociable` ✓. So this is **not** a sigma=0 config degeneracy:
the weight noise was present at supra-floor magnitude but **raised pre-commit class entropy by
exactly 0.0** — it washed out at the F-dominated argmax. Both ARM_TEMP and ARM_NOISE_SINGLE
failed to raise pre-commit entropy, so the falsifier's non-vacuity gate self-routed
`substrate_not_ready_requeue` rather than producing a (false) weakens. This is **708's own
pre-registered `could_be_wrong_if #4`**: the single-arena collapse subsumes the injection locus.

## 3. Claim-layer mapping

| Claim | type | status | epistemic_category | gate | could the test let it express? |
|---|---|---|---|---|---|
| MECH-439 | mechanism | candidate | substrate_ceiling | impl_phase v3, pending_retest | No — the single arena denied a valid null. F-dominance is the ceiling *being measured*, not falsified. |
| ARC-108 | architecture | candidate | substrate_conditional | impl_phase v3 | No — depends on a valid same-layer null the single arena cannot furnish. |
| MECH-450 | mechanism | candidate | substrate_conditional | impl_phase v3 | No — same dependency. |
| MECH-440 | mechanism | candidate | substrate_ceiling | v3_pending, impl_phase v3 | No — the injection washed at the argmax; could not express under single-arena F-dominance. |

`claim_ids` accuracy: verified, not inherited — 700d's tags match the settling/null mechanism it
measures; 708 tags only MECH-440 (the injection mechanism), correctly excluding MECH-441
(curiosity channel, separate lineage).

## 4. Biological-reference triage

Closest reference: **parallel segregated cortico-basal-ganglia-thalamic loops** (Alexander &
DeLong; Haber's ascending spiral) with **per-loop normalization**. In real brains, motor,
associative, and limbic loops compete *within loop* and arbitrate *across loops* — no single
shared arena lets one channel's raw magnitude monopolize selection. The REE single-arena E3
selector is a faithful translation of *a* BG arena but at the **wrong abstraction level** (one
arena vs N segregated loops). The failure signature — one channel (motor/F) monopolizing the
shared selector so non-motor signals (settling content, exploration noise) cannot express — is
exactly what biology predicts in the *absence* of per-loop normalization. **This is a missing-
dependency signature, not a claim falsification.** The dependency (segregated loops + per-loop
zscore = v4_loop_segregation / ARC-110) was BUILT 2026-06-27 and is live-validating via 707b.

Not a formal-definition import; no `/lit-pull` commission needed (the loop-segregation biology is
already anchored by the ARC-110 build's grounding ledger).

## 5. Four-layer diagnosis (cluster)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Neither weakens; both non_contributory. The substrate precondition (valid null / non-washed injection) was structurally unavailable. |
| Biological reference | clear | Segregated loops + per-loop normalization; single-arena collapse = missing-dependency signature. |
| Prerequisites | missing → present | v4_loop_segregation built 2026-06-27 (was the missing dependency). |
| Implementation | wrong abstraction level → fixed | one shared arena vs N segregated loops; loop-seg now present (no-op-default, byte-identical OFF). |
| Environment | adequate | reef-bipartite, GAP-A divergent pool ✓. |
| Measurement | adequate | committed-class / pre-commit entropy DVs correct; preconditions correctly self-routed instead of false-weakening. |
| Integration | single-arena binding constraint | modules work; the shared-selector integration is the ceiling. |
| Scale | adequate | — |

Dominant diagnosis → `epistemic_category: substrate_ceiling` (V3 single arena too coarse;
enrichment = loop segregation, already built and validating).

## 6. Cluster pattern

| Experiment | Claim | Negative-control / absolute criterion | Discrimination criteria (failed) | Read |
|---|---|---|---|---|
| 700d | MECH-439/ARC-108/MECH-450 | pool divergent ✓, learned range non-vacuous ✓, Δt variance ✓, weights moved ✓ | matched-null verify-lift 0/2 ✗ + null-not-destructive ✗ | magnitude-matched same-layer null still inert/destructive |
| 708 | MECH-440 | noise bias supra-floor 0.22 ✓, dACC live ✓, loop-seg variance ✓, learning ✓ | temp raises precommit 0.0 ✗ + noise raises precommit 0.0 ✗ | injected noise washes at the F-dominated argmax |

**Shape:** NOT N independent bugs — **one structural property**: the V3 single F-dominated E3
arena both (a) cannot furnish a valid committed-class same-layer null and (b) dissolves any
pre-commit exploration injection at the argmax, because F's raw-magnitude monopoly (88-89% of E3
selection variance) swamps every non-motor signal at the single shared selector. Two
structurally-different mechanisms (null construction, noise injection) converge on the same
ceiling — corroborating the 700b/700c + 704b-706b cluster autopsies. **Readings:** the
substrate-enrichment reading (loop segregation strips F's raw-magnitude advantage via per-loop
zscore) is the live one and is already built; the test-design-ceiling reading is closed (the
preconditions are correctly specified — they self-route rather than false-weaken).

## 7. Learning extracted + repair pathway

- The V3 same-layer-null validity question is **EXHAUSTED** across three constructions
  (decoupled / 41x / matched-but-inert). The single arena cannot furnish a valid committed-class
  null at *any* magnitude — too big is destructive, matched is inert.
- The exploration-injection locus (708) is subsumed by the same single-arena ceiling — even a
  supra-floor weight-noise injection raises pre-commit entropy by 0.0.
- Both map to the **already-built** v4_loop_segregation (ARC-110) substrate, live-validating via
  **707b**. No new substrate design is needed (the design exists and is implemented).

**Re-derive brake (700d cluster):** FIRED. Prior substrate_ceiling/non_contributory autopsies —
MECH-439: 6 (689, 689a, 700-cluster, 700b, 700c, f-dominance-conversion-cluster) + this = **7th**;
ARC-108: 4 + this = **5th**; MECH-450: 3 + this = **4th**. All ≫ threshold 2. → **REFUSE a 700e
single-arena re-test.** Route = `implement-substrate` on v4_loop_segregation (already built;
validating via 707b). A different-mechanism redesign (new EXQ, different claim_ids) remains
allowed; another single-arena letter does not.

**MECH-440 (708):** brake NOT fired (1st substrate_ceiling/non_contributory autopsy). But the
informative next test is 708's own pre-registered ARM_NOISE_LOOPSEG arm on the ARC-110 substrate
(the 707b lineage), not a single-arena 708 letter.

**Granularity-debt flag (MECH-439 — user-requested at the Step 8 gate):** MECH-439 has now
accumulated **7** substrate_ceiling/non_contributory autopsies, reached from structurally
different angles (conflict-grade falsifiers 689/689a, learned-gating + settling + same-layer null
700-lineage, the f-dominance-conversion cluster). That recurrence is a **granularity-debt
signal**: "F-dominance" may be several finer mechanisms (raw-magnitude monopoly vs absence of
per-loop normalization vs eligibility-arbitration coarseness), not one claim. **Recommend a
`/claim-synthesis` pass on MECH-439** as a parallel track — proposal-first, lit-grounded
decomposition into testable children — to run **if the loop-segregation substrate (707b) also
fails to convert** (which would confirm the claim is genuinely coarse rather than only
substrate-bound). This does not change the primary routing (implement-substrate / the live 707b
validation); it is a flagged contingency so the decomposition option is on the record now.

## 8. Routing summary

| Target | evidence_direction | epistemic_category | routing | substrate action | brake |
|---|---|---|---|---|---|
| 700d (MECH-439/ARC-108/MECH-450) | non_contributory | substrate_ceiling | implement-substrate | amend v4_loop_segregation (append 700d failure record) | FIRED — refuse 700e |
| 708 (MECH-440) | non_contributory | substrate_ceiling | implement-substrate | amend v4_loop_segregation (add MECH-440 to unblocks_claims + failure record) | not fired (1st) |

All four claims UNWEAKENED; `pending_retest_after_substrate` on each. Plus: `/claim-synthesis`
contingency flagged on MECH-439.

## 9. Draft `evidence_quality_note` text (governance applies)

**MECH-439 / ARC-108 / MECH-450 (700d):**
> V3-EXQ-700d (same-layer-null VALIDITY RE-TUNE; supersedes 700c) FAIL/non_contributory. The
> null-magnitude fix succeeded (field_noise_magnitude_matched 1.0x, correcting 700c's 41.42x) but
> the correctly-sized magnitude-matched same-layer null STILL failed to verify-lift committed-class
> entropy (matched_noise_control_verified_lifting 0/2) and remained destructive
> (same_layer_null_not_destructive false) -- the 3rd consecutive failed construction of a VALID
> committed-class same-layer null in the V3 single E3 arena (700b decoupled / 700c 41.42x / 700d
> matched-but-inert). The pre-registered terminal did not fire because the null could not be made
> valid; this CONFIRMS the single-arena substrate ceiling diagnosed by the 700c + 704b-706b cluster
> autopsies. Claim UNWEAKENED. RE-DERIVE BRAKE FIRED (7th MECH-439 / 5th ARC-108 / 4th MECH-450
> substrate_ceiling/non_contributory autopsy): a same-claim single-arena re-test (700e) is REFUSED;
> the V3 same-layer-null validity question is EXHAUSTED. Route = the already-built v4_loop_segregation
> (ARC-110) substrate, validating via V3-EXQ-707b. pending_retest_after_substrate. (MECH-439 also
> flagged for a /claim-synthesis granularity-debt review if 707b also fails to convert -- 7 autopsies
> from structurally different angles suggest "F-dominance" may decompose into finer mechanisms.)

**MECH-440 (708):**
> V3-EXQ-708 (MECH-440 NoisyNet propagation falsifier) FAIL/non_contributory / substrate_not_ready_
> requeue. The selection-head weight noise WAS injected supra-floor (noise_bias_range 0.22) but BOTH
> the temperature control and the weight noise raised pre-commit class entropy by 0.0 -- the
> injection washes out at the F-dominated argmax. This is 708's own pre-registered could_be_wrong_if
> #4 (the single-arena collapse subsumes the injection locus), the same single-arena F-dominance
> ceiling that bounds the 700-lineage. MECH-440 UNWEAKENED (the falsifier's non-vacuity gate
> correctly self-routed rather than producing a false weakens). Route = the already-built
> v4_loop_segregation (ARC-110) substrate (708's pre-registered ARM_NOISE_LOOPSEG escalation),
> validating via V3-EXQ-707b; a single-arena 708 re-test is not informative. pending_retest_after_substrate.
