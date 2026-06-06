# modulatory-bias-selection-authority

**Status:** IMPLEMENTED 2026-06-03 (substrate-readiness validation pending V3-EXQ).
**Subject:** `ethics_engine_3.modulatory_bias_selection_authority`
**Unblocks:** MECH-314 / MECH-314a/b/c, Q-044, MECH-320, ARC-068, MECH-341 (and downstream MECH-343 difficulty-gated proposal entropy).
**Substrate_queue:** `modulatory-bias-selection-authority` (created from the 604a/624a cluster autopsy 2026-06-03).

## Problem

The modulatory / diversity score-bias channels at E3 committed selection fire but have
**zero authority over the committed argmin**. Three convergent failure records, one root
cause:

| Run | Lever | Signature |
|-----|-------|-----------|
| V3-EXQ-604a | MECH-314 curiosity | `curiosity_bias_abs_mean = 0.0` every arm; `selected_entropy` identical across 5 arms |
| V3-EXQ-624a | MECH-320 vigor | vigor fires (`v_t=0.05`) but `action_density` byte-identical vigor-ON vs OFF (0.865) |
| V3-EXQ-614d | MECH-341 within-class temperature | within-class branch fires 3/3 seeds, but committed-class entropy **byte-identical** (1.056572) across T=0.5/1.0/2.0 |

Root cause (confirmed at `ree-v3/ree_core/predictors/e3_selector.py` `select()`): the
modulatory contributions are **fixed small magnitudes** (curiosity/vigor `bias_scale ~0.1`,
entropy `0.05-2.0`) **added to primary `scores` whose `raw_score_range` is much larger**, so
they never move the argmin. The MECH-341 across-class `stratified_select` softmax has the
same problem: the absolute class-representative score gap dominates `stratified_temperature`,
collapsing committed-class selection onto one class.

## Solution (approach (b): gap-relative scaling)

Give the modulatory layer **genuine but bounded** authority by scaling it relative to the
local primary-score scale — **without modifying the primary scores** (so commit-threshold /
`running_variance` / softmax-temperature / urgency-interrupt / MECH-090 admission semantics
are untouched, and a clearly-harmful candidate with a large primary gap stays rejected).

Three application sites, all gated on one master flag (default OFF, bit-identical):

1. **Additive bias chain + MECH-341 entropy bonus** (`e3_selector.select()`): after the
   composed `score_bias` (dACC + lateral_pfc + ofc + mech295 + curiosity + vigor) and the
   MECH-341 entropy bonus are added, compute the combined modulatory delta
   `mod = scores - raw_scores` and rescale it so `range(mod) == gain × raw_score_range`,
   then `scores = raw_scores + rescaled_mod`. Takes precedence over the legacy
   `normalize_score_bias_to_e3_range` (the blunt `gain=1.0` blob version), which is skipped
   when this flag is on.
2. **Stratified across-class softmax** (`e3_score_diversity.stratified_select()`): normalize
   the class-representative scores to **unit range** before the `stratified_temperature`
   softmax, so the diversity temperature acts on a fixed scale (the 614d C2 fix).

**Safety property.** With `gain < 1.0`, the modulatory layer is competitive in near-tie
regimes (top-2 primary gap `< gain × range`) but subdominant when the primary harm/goal gap
exceeds `gain × range`. Primary scores are never mutated.

## Config (`REEConfig` / `from_dims` / `E3Config`)

| Param | Default | Site |
|-------|---------|------|
| `use_modulatory_selection_authority` | `False` | master (E3Config + REEConfig top-level mirror) |
| `modulatory_authority_gain` | `0.5` | additive-bias rescale target as fraction of `raw_score_range` |
| `modulatory_authority_min_range_floor` | `1e-6` | degenerate-range guard |

The top-level REEConfig mirror lets `build_from_ree_config` arm the stratified across-class
normalization (`E3ScoreDiversityConfig.use_selection_authority`).

## Backward compatibility

Default OFF → bit-identical to pre-substrate. 734/734 contracts + 7/7 preflight PASS with
the flag off, verified under two pytest-randomly orderings. Existing
`normalize_score_bias_to_e3_range` is unchanged and independent.

## Necessary-but-not-sufficient caveat (validation-shaping)

624a (vigor) and 614d (within-class temperature) are **pure drowning** — this substrate fixes
them directly. **604a had `curiosity_bias_abs_mean = 0.0`** — the curiosity bias was genuinely
~zero (MECH-314a found no active residue centers; MECH-314b/c are broadcast-by-design), not
just drowned. Scaling zero is still zero. The validation EXQ **must guard
`curiosity_bias_abs_mean > 0`** before testing curiosity's authority; otherwise a curiosity
arm tests a degenerate upstream signal, not this substrate.

## MECH-094 / phased training

Pure arithmetic on the waking committed-selection path; `stratified_select` already carries
`simulation_mode`. No replay write surface — N/A / preserved. No learned parameters — no
phased training.

## Validation

Substrate-readiness diagnostic EXQ (via `/queue-experiment`): re-run the vigor (624a-style),
curiosity (604a-style, with the non-degeneracy guard) and within-class (614d-style) arms,
master OFF vs ON, measuring whether the previously-inert lever now changes committed
selection (`action_density` lift for vigor; committed-class entropy lift for diversity)
**without** a harm increase. `claim_ids=[]` (substrate-readiness). PASS unblocks the
per-claim evidence retests of MECH-314/320/341 and the MECH-343 hypothesis.

## V3-EXQ-643a fix: float32 catastrophic cancellation (2026-06-06)

The 2026-06-03 Solution (b) computed the combined modulatory delta as
`mod = scores - raw_scores` — reconstructing it by **subtracting two primary-magnitude
score tensors**. This is numerically fragile, and V3-EXQ-643 (the substrate-readiness
validation) hit the fragility: `modulatory_authority_active_frac = 0.0` and
`scale_factor_mean = 0.0` on **both** authority-ON arms, 0/3 seeds.

**Code-confirmed root cause (corrects `failure_autopsy_V3-EXQ-643_2026-06-06`).** The
autopsy concluded "the modulatory bias is uniform across the K candidates … range < 1e-6
… scaling a zero range is still zero." That is **numerically wrong**. The MECH-341 entropy
bonus keys on per-candidate **first-action class** (not z_world), so it carries a genuine
~0.17 cross-candidate range — it is *not* uniform. What actually happened:

- The 643 harness trains SD-056 (`e2_action_contrastive`) **online**, which drove the
  primary E3 scores to ~**1e32** (z_world instability; the SD-056 multistep rollout-norm
  clamp is OFF in 643).
- The float32 ULP at 1e32 is ~1e25, far above 0.17. So `scores - raw_scores` collapses to
  **exactly 0.0** → `modulatory_range < floor` → the gate never fires.

Diagnostic probe (643 config + harness): SD-056-training-**OFF** → `raw_score_range ~4.5`,
gate fires (`modulatory_range ~0.25`, `active=True`); SD-056-training-**ON** →
`raw_score_range ~1e32`, `modulatory_range = 0.0`, never fires. **The substrate is
functionally correct at normal score magnitude**; 643 failed from a harness-induced
numerical degeneracy, not from absent per-candidate signal.

**Fix.** Track the combined modulatory contribution **explicitly** as a small accumulated
tensor `_modulatory_accum = (score_bias added) + (MECH-341 entropy bonus added)`, captured
at the two add sites. The authority block measures `modulatory_total = _modulatory_accum`
(range from the small ~0.17 bias tensor, independent of primary-score magnitude) instead of
reconstructing it by subtraction. Mathematically identical to `scores - raw_scores` in exact
arithmetic; immune to large-score cancellation. `scores = raw_scores + scale_factor × mod`
is unchanged. New diagnostic `modulatory_authority_range` exposes the true range (0.17, not 0).

Bit-identical OFF (flag default); bit-identical when scores are small (differs only in
low-order float bits, argmin unchanged). Regression contract
`test_modulatory_authority_survives_large_primary_scores` (large per-candidate world states →
`raw_score_range > 1e10`; a 0.5-range bias is annihilated by the pre-fix subtraction but the
post-fix gate reports `modulatory_authority_range == 0.5`, `active = True`).

**Validation-shaping (vacuity guard).** With the fix, the gate fires correctly even at 1e32
scores — but `scale_factor` is then ~1e27, a **vacuous** fire on degenerate scores. A
meaningful V3-EXQ-643a therefore REQUIRES the harness to keep primary scores bounded: enable
the SD-056 rollout-norm clamp (`e2_rollout_output_norm_clamp_enabled`) and add a
`raw_score_range` non-vacuity precondition (below-bound → `substrate_not_ready_requeue`, not
an authority verdict). The 604a curiosity non-degeneracy guard is retained.

## See also

- `ree-v3/ree_core/predictors/e3_selector.py` (additive authority + V3-EXQ-643a explicit
  accumulator), `e3_score_diversity.py` (stratified normalization), `ree_core/utils/config.py`
  (flags).
- Cluster autopsy: `evidence/planning/failure_autopsy_604a-624a-630_2026-06-03.{md,json}`.
- 643 autopsy (root cause corrected by the 643a fix above):
  `evidence/planning/failure_autopsy_V3-EXQ-643_2026-06-06.{md,json}`.
- MECH-343 working hypothesis: `docs/thoughts/2026-06-03_difficulty_gated_proposal_entropy.md`.
