# Failure Autopsy (cluster): V3-EXQ-704b + V3-EXQ-706b — the conversion ceiling is the single-arena collapse

- **Generated**: 2026-06-27T10:04:21Z
- **Scope**: cluster (convergent endpoint across two structurally-different claims)
- **Status**: confirmed
- **Surfaced by**: `/governance` cycle 2026-06-27 (route A — clear inline)
- **Targets**:
  - `v3_exq_704b_mech451_finer_channel_granularity_falsifier_20260626T180938Z_v3` (V3-EXQ-704b, MECH-451) — supersedes V3-EXQ-704
  - `v3_exq_706b_mech314_curiosity_conversion_double_gated_validity_20260626T073417Z_v3` (V3-EXQ-706b, MECH-314) — supersedes V3-EXQ-706

## Bottom line

Both validity re-tests **fixed their predecessors' measurement defects and then hit the same wall.** Neither claim is weakened; both are diagnosed `substrate_ceiling`, both fire the re-derive brake, and both route to `/implement-substrate` on `v4_loop_segregation` (ARC-110). The convergence is the load-bearing signal: the V3 single shared E3 foraging arena structurally denies committed-action-class conversion **and** a valid same-layer null — exactly the two conditions the 700b/700c learned-gating-settling autopsies already named. This is now corroborated from two further independent mechanisms (finer-channel compression; structured curiosity).

---

## Facts (no interpretation)

### V3-EXQ-704b — MECH-451 finer-channel-granularity falsifier
- Outcome **FAIL**, `evidence_direction: non_contributory`, **non_degenerate=False** (self-route `substrate_not_ready_requeue`, scoring-excluded).
- Readiness legs:
  - `enough_divergent_seeds` 4 ≥ 3 — **MET**
  - `finer_channels_dissociable` 0.00148 ≥ 1e-4 — **MET**
  - `finer_channels_dissociation_substantive` 0.0087 ≥ 0.005 — **MET** (704's near-vacuity guard cleared)
  - `delta_t_carries_variance_on_armed_arms` 0.0005 ≥ 1e-4 — **MET**
  - `learned_weights_moved_from_init_on_armed_arms` 0.00135 ≥ 1e-4 — **MET**
  - `fcg_noise_magnitude_matched` **1.0** ∈ [0.25, 4.0] — **MET** (704 was **176.9×**; the fix worked)
  - `matched_noise_control_verified_lifting` **0.0** vs threshold 2 — **FAILED** ← the blocker
  - `candidate_pool_divergent_focus_arms` 0.036 < 0.05 — borderline
- The decisive A2-vs-A1 conversion comparison was **never reached**: the null-validity readiness leg failed first.

### V3-EXQ-706b — MECH-314 curiosity-conversion double-gated (validity-fixed)
- Outcome **FAIL**, `evidence_direction: non_contributory`, **non_degenerate=True** (a *valid* test).
- Interpretation label: `conversion_ceiling_persists_despite_double_gating_valid_null` (pre-registered TERMINAL).
- All **6 readiness legs MET**: GAP-A pool 0.072 ≥ 0.02; curiosity bias range 0.00197 ≥ 1e-4; demotion excluded 23.4 > 0; z_world bounded; Go/No-Go suppressed 7.9 > 0; per-seed committed-tick budget balanced.
- Committed-class entropy: **ARM_CURIOSITY 0.967** < ARM_FONLY (double-gated F-only) **1.029** and < ARM_NOISE (valid null) **1.019**. No lift on any seed.
- Null validity: ARM_NOISE injected range 0.00197 = curiosity range 0.00197 (ratio 1.0, magnitude-matched by construction); ARM_NOISE 1.019 ≠ ARM_FONLY 1.029 → **non-degenerate** (the 706 byte-identical-null defect fixed).

---

## Claim-layer mapping

| Claim | Status / category | Tested fairly? | Read |
|---|---|---|---|
| **MECH-451** | candidate / substrate_conditional → **substrate_ceiling** | No — control unconstructable | UNWEAKENED, untested either direction; the null cannot verify-lift in V3 |
| **MECH-314** | candidate_substrate_landed / substrate_ceiling | **Yes** — first fully-valid double-gated test | UNWEAKENED; ceiling is architectural (single-arena), not the channel |

Neither FAIL falsifies its claim. 704b is a control-construction impossibility; 706b is a fair test whose no-lift localises the constraint to architecture, not to MECH-314.

## Biological-reference triage

Both mechanisms are faithful functional translations (OFC/dACC/lPFC finer channels; frontopolar+striatal curiosity). The divergence from biology is the **single-arena collapse**: real cortico-BG-thalamic channels compete *within segregated loops* (Alexander/DeLong/Strick) before cross-loop arbitration. The V3 single E3 arena collapses motor / associative / limbic competition into one F-dominated arena, which (a) lets F drown non-motor conversion and (b) makes any same-layer null inert on the committed-class DV. Lit present for both; no lit-pull owed.

## Four-layer diagnosis (dominant)

| Layer | 704b | 706b |
|---|---|---|
| Claim alignment | intact (untested) | intact (fairly tested, no-lift) |
| Biological reference | clear; single-arena divergence | clear; single-arena divergence |
| Prerequisites | **ARC-110 missing** | **ARC-110 missing** |
| Implementation | complete (channels learn) | complete (gates fire, valid null) |
| Environment | **single-arena, too sparse** | **single-arena, too sparse** |
| Measurement | DV decoupled from same-layer null | adequate (706 defects fixed) |
| Integration | isolated (channel can't reach selection) | coupled but F-drowned |
| Scale | adequate | adequate (budget balanced) |

Dominant diagnosis (both): **`substrate_ceiling`** — the single E3 arena is too coarse to carry conversion or a valid null.

## Cluster pattern

| Run | Claim | Negative-control / readiness | Discrimination | Read |
|---|---|---|---|---|
| 704b | MECH-451 | magnitude-match MET (1.0) | matched-null inert on DV (0/2 verify-lift) | control unconstructable in V3 |
| 706b | MECH-314 | all 6 legs MET, valid null | curiosity 0.967 < F-only 1.029 < null 1.019 | no conversion at eligibility face |

**Not independent bugs — one structural property.** The single F-dominated E3 selection arena cannot carry committed-action-class conversion from non-motor channels, nor furnish a valid same-layer null to test it. Both require **ARC-110 parallel segregated loops (+ in-layer null)** to lift. Live reading: **substrate enrichment** (the 704 "test-design ceiling" reading is now retired — 704b fixed the test design and still cannot construct a valid null, proving it is the substrate, not the test). This corroborates the 700b/700c learned-gating-settling reading from two further independent angles, strengthening ARC-110 as the binding constraint on the F-dominance conversion ceiling (MECH-439).

## Re-derive brake

- **MECH-451**: 1 prior non_contributory autopsy (704) + this = **2 = threshold → FIRES.** Refuse a further V3 finer-channel-vs-same-layer-null letter; route `/implement-substrate` v4_loop_segregation.
- **MECH-314**: 7 prior + this = **8 → FIRES (brake-LOCK).** The 706 autopsy pre-recorded the lock naming 706b as the one permitted validity letter. Refuse all further V3 letters on the conversion lineage; route `/implement-substrate` v4_loop_segregation.

## Learning extracted

1. Fixing a null's *scale* (704) only exposed the deeper wall: a correctly-sized same-layer null is *inert* on committed-class entropy in the single arena.
2. MECH-451's finer channels build, dissociate, and learn — the representation works; only the *conversion test's control* is unconstructable in V3.
3. 706b is the first fully-valid double-gated MECH-314 test; both eligibility gates fire and curiosity still cannot convert → the binding constraint is *after* eligibility construction, at the single-arena selection collapse.
4. The convergence of two independent mechanisms onto the same wall is positive evidence for ARC-110 as the binding constraint.

## Routing (proposed — governance applies)

Both targets → **`/implement-substrate` on `v4_loop_segregation` (ARC-110)**; `recommended_substrate_queue_entry.action: amend` (add MECH-451 and MECH-314 to `unblocks_claims`, append both failure records). Both `pending_retest_after_substrate: true`. Both `evidence_direction: non_contributory` (no claim weakened). MECH-451 `epistemic_category` → `substrate_ceiling`; MECH-314 stays `substrate_ceiling`.

## Draft `evidence_quality_note`s

See the `recommended_evidence_quality_note` fields in the JSON sibling — verbatim text for governance to write to MECH-451 and MECH-314.
