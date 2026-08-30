# Failure autopsy -- V3-EXQ-936a (MECH-439)

- **Generated (UTC):** 2026-08-30T08:42:14Z
- **Scope:** single
- **Status:** confirmed (Step 8 gate cleared 2026-08-30 -- user selected "Non-contributory +
  monopoly audit", the recommended option; outcome logged via `record_recommendation_outcome.py`)
- **Session:** fable-autopsy-936a-20260830
- **Target:** `v3_exq_936a_mech439_f_variance_share_rollout_clamp_fix_20260829T071510Z_v3` (V3-EXQ-936a, MECH-439)
- **Supersedes (run-level):** `v3_exq_936_...20260817T062038Z_v3` (adjudicated non_contributory by `failure_autopsy_V3-EXQ-936_2026-08-18`, read in full for this autopsy)

## Headline

**The manifest's `weakens` against MECH-439 is vacuous -- C2 fired by construction, in the
MIRROR direction of its predecessor's defect.** 936 could not evaluate C2 because F's share was
pinned at ~1.0 (unclamped rollout divergence); 936a, with the prescribed clamp armed, cannot
evaluate C2 because F's share is ~6.33e-06 -- the maximum attainable paired reduction is ~7,900x
below the pre-registered 0.05 bar, so `n_reducing = 0` is guaranteed for ANY behaviour and the
falsifier branch fires regardless. The claim's monopoly premise is simply ABSENT in this regime,
so the run bears on MECH-439 in neither direction.

Three genuine findings survive the vacuous criterion:

1. **The variance monopoly persists with a different occupant.** `residue_weighted` carries
   ~99.9998% of committed-selection variance in all 8 cells, both arms. The structural property
   (one channel monopolises the un-normalised E3 score sum) is conserved; WHICH channel is
   config-/scale-dependent. Corroborates H5 (`score-scale-uncontrolled`, confirmed) on
   `e3_fdominance_causal_discrimination`.
2. **The paired deltas actually REDUCE F's share on 3/4 seeds** -- directionally as MECH-439
   predicts -- at 1e-06 scale, five orders below the bar.
3. **MECH-439's quantitative basis has never been measured under the fixed instrument.** The
   0.886 monopoly figure comes from V3-EXQ-571, a DIAGNOSTIC (scoring-excluded) run whose driver
   sets no clamp flag (config default False -- unclamped regime), in a different config
   (CausalGridWorld 8x8, diversity stack) from this GAP-A/689i stack. Whether an F-monopoly
   regime exists at all under clamped rollouts is now the open question.

## 1. Dry-run gate (Step 2a)

`check_dry_run_citations.py` over v3_exq_936a + v3_exq_936: **0 dry cited, 2 clean.** Real-run
denominator: 4 seeds x 2 arms = 8 cells.

## 2. Recording provenance

`validate_recording.py`: **OK -- 1 complete, 0 always-core gaps.** `substrate_hash`
2151a1142cd96346, machine ree-cloud-2, elapsed 8062s, seeds [42,43,45,46].

**Prescription compliance from the 2026-08-18 autopsy -- PARTIAL, and the gap matters:**
- (a) clamp parity: DONE (`mech439_f_variance_share.py:191-192`,
  `e2_rollout_output_norm_clamp_enabled=True, ratio=2.0`).
- (b) scale anchors: NOT DONE. No `||z_world||` step-norm, no raw E3 score range, no
  clamp-hit-rate readout in `arm_results`. Absolute variances (`f_variance_abs` 1.7e-4..1.6e-2,
  `nonf_variance_abs` ~1e3) partially substitute -- they show magnitudes are sane -- but the
  manifest cannot distinguish naturally sub-ceiling rollouts from clamp-PINNED rollouts (a
  norm-pinned rollout population would crush var(F) by construction).
- (c) relative readiness floor: NOT AS PRESCRIBED. The prescription was
  `var_nonF / var_F >= epsilon` (relative); the driver implemented absolute floors on both
  (`f_variance_nondegenerate` >= 1e-9, `nonf_variance_nondegenerate` >= 1e-9). In the event the
  old failure mode did not recur -- but the missing SYMMETRIC guard (monopoly presence: OFF-arm
  share large enough for a 0.05 reduction to be attainable) is exactly the tail that bit.

## 3. Facts

`outcome: PASS`, `evidence_direction: weakens`, `experiment_purpose: evidence`,
`claim_ids: [MECH-439]`, label `conversion_without_f_share_reduction_falsifies_monopoly`.

- **C1** (a treatment arm converts): **passed 4/4 seeds** (entropy deltas +0.232, +0.054, +0.487,
  +0.252 vs ARM_OFF -- stronger than 936's 3/4).
- **C2** (converting arm reduces F share by >= 0.05 on >= 3 paired seeds): **failed,
  n_reducing = 0.** Per-seed paired reductions: -2.0e-08, +6.8e-06, +6.5e-06, +1.4e-06
  (positive = reduction; 3/4 seeds reduce, at 1e-06 scale).
- Combination rule: C1 true + C2 false -> weakens ("a lever that converts WITHOUT reducing F's
  variance share").
- All four readiness preconditions met (decomp samples 201 >= 60; f variance 1.7e-4 >= 1e-9;
  non-F variance 914 >= 1e-9; demotion lever engaged 1.0).

### The arithmetic that voids C2

`off_arm_mean_f_variance_share = 6.328e-06`. A paired reduction cannot exceed the OFF-arm share
itself, so the maximum attainable reduction is 6.33e-06 -- **7,900x below MIN_F_SHARE_REDUCTION
(0.05)**. `reduced_f_share` is false by arithmetic; the falsifier branch fires by construction.

The driver's own constants block (lines 279-302) anticipated the absolute-level mismatch with 571
("immune to the absolute level differing from 571's 0.886 because 571 ran a different config")
-- but only for the CONTRAST. The bar's magnitude (0.05 = "6x 571's null-level movement") is
still denominated in 571's absolute scale. And the driver computes the discriminating quantity
(`mean_share_above_monopoly_bar` = false, `F_MONOPOLY_THRESHOLD` = 0.85) yet routes on it only in
the C1-FALSE supports branch -- the C1-true falsifier branch never checks that the monopoly it is
falsifying exists.

### Per-cell decomposition (committed-method fractions)

| cell | residue_weighted | harm_weighted | f | f_share (571-method) | ent | classes |
|---|---|---|---|---|---|---|
| OFF/42 | 0.999998 | 1.8e-06 | 7.5e-10 | 2.37e-06 | 1.189 | 5 |
| OFF/43 | 0.999993 | 6.8e-06 | 6.0e-09 | 6.94e-06 | 0.639 | 2 |
| OFF/45 | 0.999988 | 1.2e-05 | 3.2e-09 | 1.24e-05 | 0.479 | 3 |
| OFF/46 | 0.999996 | 4.0e-06 | 8.1e-09 | 3.64e-06 | 0.958 | 5 |
| DEM/42 | 0.999997 | 3.1e-06 | 2.4e-10 | 2.39e-06 | 1.420 | 5 |
| DEM/43 | 1.000000 | 2.2e-07 | 3.9e-09 | 1.27e-07 | 0.693 | 2 |
| DEM/45 | 0.999994 | 6.0e-06 | 2.9e-09 | 5.89e-06 | 0.966 | 4 |
| DEM/46 | 0.999998 | 2.3e-06 | 1.1e-09 | 2.20e-06 | 1.210 | 5 |

`benefit_weighted` / `novelty_weighted` / `goal_weighted` are exactly 0.0 in every cell (inactive
in this config). Float32 annihilation (936's Section 3d pathology) is GONE: std(f)/std(residue)
~1.5e-3, far above float32 eps.

## 4. Claim layer

MECH-439 (`mechanism_hypothesis`, `candidate`, `epistemic_category: standard`,
`ceiling_decision: exhausted` -- demoted to contested candidate 2026-07-09, inert/no-op null
carried co-equally; 9 counted ceiling hits after the 2026-08-10 correction;
`pending_retest_after_substrate: true`, awaiting ARC-107). Its text is F-SPECIFIC: "the primary
harm/goal score (F) monopolises ~88-89% of E3 committed-selection variance (V3-EXQ-571)". The
claim also pre-empts the eligibility-lever objection: "a shortlist-then-modulate lever
circumvents F locally but may cap committed entropy below the proposer ceiling" -- so C1
conversion via the MECH-448 demotion (eligibility) lever is compatible with the claim's own
caveat and is NOT a falsification in spirit either.

**Did the experiment test the claim under conditions where it could express itself? No.** The
monopoly premise (F share >= ~0.85) does not obtain in this regime (6.33e-06). A falsifier of
"conversion without reducing F's share" is meaningful only where F HAS a share to reduce.

## 5. Biological triage

Same load-bearing divergence the 936 autopsy recorded, now visible from the other side: the E3
score sum has **no normalisation across channels** (divisive normalisation / gain control is the
ubiquitous biological counterpart -- Carandini-Heeger; partial lit coverage exists at
`targeted_review_striatal_gain_control_bounding`). Unclamped, F's quadratic scaling made it the
monopolist; clamped, residue_weighted's scale makes IT the monopolist (~99.9998% everywhere).
The monopoly is a property of the un-normalised sum, not of F. This is a formal-import divergence
and remains load-bearing.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | Monopoly premise absent; claim could not express itself. Not weakened, not supported. |
| Biological reference | **partial** | No-normalisation divergence, load-bearing (Section 5); partial lit coverage. |
| Prerequisites | **present** | The named prerequisite (SD-056 clamp) restored per prescription. |
| Implementation | **partial** | Instrument prescriptions half-implemented: clamp yes; relative floor and scale anchors no (Section 2). Substrate itself complete. |
| Environment | **adequate** | Validated 689i GAP-A reef stack. |
| Measurement | **misleading** | C2 unreachable by construction in this regime; monopoly-presence precondition missing; guard existed as a readout, not a gate. |
| Integration | **adequate** | Dual-method share readouts, fresh-select gating, decomposition all functioned. |
| Scale / capacity | **adequate** | Magnitudes sane; annihilation gone. |

**Failure-location (GOV-FAILLOC-1): MEASURES FAILED -- not chargeable to REE.** Mechanism
established (clamp worked, lever engaged), environment established, measurement not_established.

## 7. Learning extracted

1. **Both tails of a ratio DV need floors.** 936 guarded share~1.0 starvation; nobody guarded
   share~0 starvation; it bit on the very next run. A paired-reduction bar needs a
   premise-presence precondition: OFF-arm share >= bar + margin.
2. **An instrument-fix successor must re-derive criterion reachability from the fixed regime**,
   not carry the broken regime's bar (0.05 was calibrated to 571's 0.886 world).
3. **A guard that exists as a readout is not a gate.** `mean_share_above_monopoly_bar` was
   computed and never consulted on the falsifier branch.
4. **Half-implemented prescriptions recur.** Clamp: done; relative floor + scale anchors: not
   done -- and the missing anchor is what leaves the clamp-pinning question open (Section 2b).
5. **MECH-439's quantitative premise rests on an unclamped diagnostic** (571). The claim has
   never had its monopoly measured by the fixed instrument.

## 8. Routing (DRAFT -- Step 8 gate pending)

- **`recommended_evidence_direction`: `non_contributory`** for MECH-439 (manifest `weakens` is
  vacuous; governance should set non_contributory + note).
- **`recommended_epistemic_category`: `standard`** (unchanged; no ceiling hit added -- an
  instrument defect is not ceiling evidence; same reasoning as the 936 autopsy).
- **Status stays `candidate`;** `pending_retest_after_substrate` stays true.
- **Routing: `queue-experiment` -- a DIAGNOSTIC monopoly-presence audit, not another 936-family
  falsifier.** Re-run the 571 decomposition in 571's own config with the clamp armed
  (`v3_exq_571b`-shape), recording per-cell scale anchors (mean/max ||z_world|| step norm, raw
  score range, clamp-hit fraction) and 936a's dual-method share readouts. It discriminates:
  (Ha) 571's 0.886 was divergence-inflated -> no F-monopoly regime exists under the fixed
  instrument; MECH-439's premise collapses (governance re-words/narrows). (Hb) 571's config
  genuinely exhibits F-monopoly clamped -> MECH-439 is regime-scoped; the 936-family falsifier is
  re-posed THERE, with a monopoly-presence precondition and a relative bar.
- **A further 936-family falsifier in the GAP-A stack is REFUSED** until the audit establishes a
  monopoly-present regime (re-derive-brake spirit; the brake itself does not fire -- this autopsy
  adds no ceiling hit, and the successor is on the measurement axis, not another letter of the
  braked design).
- **Ledger (Step 9b):** append 936a to H5-score-scale-uncontrolled's `resolving_runs` on
  `e3_fdominance_causal_discrimination` with extended basis; NO state change, NO denominator
  change; H1-H4 stay alive (936a does not discriminate them).
- **Granularity-debt trigger: does NOT fire.** 17 targets on MECH-439, zero read `weakened`
  (this one reads `unclear`) -- measurement/implementation debt, not granularity debt. The
  standing observation stands: MECH-439 has been autopsied 17 times and never once fairly tested.

## 9. Checks

- Step 7b pre-routing checks: **0 fires** (C5 inapplicable).
- Step 7c red-team pass: **CONFIRMED** (same-model, Fable -- the drafting session is itself
  Fable, so a cross-model pass was not available; stated per Step 7c). All six load-bearing
  assertions survived independent recomputation from the manifest's own cells: off-arm mean F
  share recomputes to exactly 6.328e-06; per-seed best-case attainable reduction is 1.236e-05,
  still **~4,044x** below the bar (the 7,900x headline figure is the mean-based form); the
  sign convention (`red = off - dem`, positive = reduction) confirms 3/4 seeds reduce; the
  residue monopoly holds on BOTH share methods (the >1.0 wrinkle is confined to the
  covariance-retained method). One assertion was STRENGTHENED: v3_exq_571 ran 2026-05-15/16,
  predating the clamp's landing (ree-v3 d327b89, 2026-05-31) entirely. The recommended
  571-family re-measure is not redundant (no 571b driver, no queue entry, no clamp-enabled
  variance-share manifest anywhere). Hygiene note for governance: this artifact counts 9
  ceiling hits (R1-R3, matching claims.yaml's 2026-08-10 correction) while the 936a driver's
  inherited custom_information says 12/13 -- reconcile at GOV-APPLY-1; the discrepancy does not
  affect this reading (no ceiling hit added either way).

## 10. Ledger (Step 9b) -- APPLIED

Appended `v3_exq_936a_...` to `H5-score-scale-uncontrolled.resolution.resolving_runs` on
`e3_fdominance_causal_discrimination` with an extended basis (residue monopoly under the clamp);
NO state change, NO denominator change; H1-H4 left alive. Derive rollups rebuilt
(`build_hypothesis_space.py`); integrity audit **flags a=0 b=0 c=0 d=0**.
