---
nav_exclude: true
---

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

## Route-range amend: route upstream-channel range into the bias the authority rescales (569f/661/654a, 2026-06-10)

The 2026-06-03 / 643a authority rescales `_modulatory_accum` (the composed `score_bias`
chain + MECH-341 bonus). The **569f / 661 / 654a** cluster (failure_autopsy_569f-661-654a_2026-06-10,
user-adjudicated) exposed the next link: a channel whose **representation** carries
genuine cross-candidate range still does **not** move committed action.

| Run | Channel | Range present in representation | Committed-action readout |
|-----|---------|--------------------------------|--------------------------|
| 569f (ARC-065) | world-summary | consumed spread **0.196** (> floor); C1 e2.world_forward divergent PASS | selected-action entropy **bit-identical 0.549141** across e2wf / proposer / matched-noise |
| 661 (MECH-294) | theta co-binding coherence | coherence **JOINT 1.0 / ALT 0.25 / SHUF 0.0** (mode-distinct) | committed-dist TV **~0** (max 0.0097); C3 gate-ON == gate-OFF |
| 654a (ARC-062/MECH-309) | candidate rule field | rules minted **268/549/220** | within-arm rule_state counterfactual **0/3**; committed-class entropy lift OFF 0.9375 -> ON 0.9377 |

**One structural property, not three bugs:** the range exists in the representation but
is **flattened by the consuming bias head** before it reaches `_modulatory_accum`, so the
authority has nothing to amplify. V3-EXQ-643 established *no range -> no authority*; this
cluster extends it one link: **the channel range must be ROUTED into the per-candidate
modulatory bias the authority rescales, not merely exist in the representation.**

### The fix (parameter-free, no-op default, bit-identical OFF)

1. **`project_channel_range(features)`** (`e3_selector.py`): a deterministic,
   range-preserving projection of a channel's per-candidate representation into a
   per-candidate scalar bias `[K]`. `[K, D]` (e.g. `cand_world_summaries`): center across
   the K candidates, project onto the leading right-singular vector of the centered
   matrix (SVD on a detached copy; numerical fallback to the mean-deviation axis). `[K]`:
   identity. K<2 / flat input: zeroed (below-floor). The singular-vector sign is
   arbitrary -- routing makes the channel range **reach and move** the committed argmax
   (the readiness property), **not** necessarily move it *beneficially* (that is the
   channel's own trained head, the separate per-claim evidence retest).
2. **`E3TrajectorySelector.select(channel_route_bias=...)`**: when
   `use_modulatory_channel_routing` is on, the `[K]` routed bias is normalised to unit
   zero-mean range (bounded even with the authority OFF; the authority re-normalises the
   combined accumulator to `gain * raw_score_range` regardless), scaled by
   `modulatory_channel_route_weight`, and folded into **both** `scores` and
   `_modulatory_accum` **before** the authority's range computation. New P0 diagnostics:
   `modulatory_channel_route_range` (the **raw** cross-candidate range, pre-normalise /
   pre-rescale -- the gate signal) + `modulatory_channel_route_active`.
3. **`REEAgent.select_action`** builds `channel_route_bias` from the channel-under-test's
   per-candidate representation and passes it. `modulatory_channel_route_source`:
   `cand_world_summary` (the [K, world_dim] world-summary channel -- 569f cluster lead,
   the genuine projection case) / `curiosity` / `gated_policy` / `mech295` / `coherence`
   (each an already-computed `[K]` bias, identity-routed). Default `none` -> bit-identical.

**P0 readiness gate (the autopsy's explicit requirement):**
`modulatory_channel_route_range` lets a retest assert the modulatory bias **itself**
carries cross-candidate range derived from the channel under test **before** any
behavioural falsifier is scored -- so an unrouted channel cannot self-route a false
negative.

**Config** (E3Config + REEConfig mirror + `from_dims`; all no-op default):
`use_modulatory_channel_routing` (False), `modulatory_channel_route_min_range_floor`
(1e-6), `modulatory_channel_route_weight` (1.0), `modulatory_channel_route_source`
("none").

**Honest scope.** For **coherence** (661): `currency_coherence` is a *scalar* (uniform
across candidates) -- a scalar gate is **rescale-invisible** by construction. Routing the
compose `[K]` bias gives it the cosine's range, but joint-vs-alternation
**mode-discrimination** (a different per-candidate *pattern*, not just magnitude) is a
MECH-294-side concern, out of scope here. The P0 gate correctly flags a channel carrying
no cross-candidate range as `substrate_not_ready`.

**Validation:** V3-EXQ-663 substrate-readiness diagnostic (`claim_ids=[]`; ARM_0 routing
OFF vs ARM_1 routing ON, both authority ON + e2_world_forward + SD-056 online). PASS
(`route_range_substrate_ready`) confirms the P0 gate and unblocks the **separate**
per-claim behavioural retests of ARC-065 / MECH-294 / ARC-062 / MECH-309 / MECH-341.
Those claims stay candidate / v3_pending / pending_retest_after_substrate; not weakened.

## CONVERSION amend (gain/contrast + shortlist-then-modulate, 569g/682, 2026-06-15)

The route-range amend (above) solved **reach**: V3-EXQ-682 (`no_collapse_reproduced`,
2026-06-15) confirmed ARM_1 applies in-arm `route_range ~0.20` at the live select tick
with **all four collapse causes ruled out** (live summary re-collapse / project_channel_range
/ wiring / applied-zero), including on seed 43 (the seed where 569g's *conversion* failed).
So the residual gap is **conversion**, exactly as `failure_autopsy_V3-EXQ-569g_2026-06-14`
isolated: the gap-relative **additive** authority at gain 0.5 (`modrange = 0.5*raw_score_range`)
is subdominant to the **F-dominated primary** (88-89% of E3 variance, V3-EXQ-571), so the
routed range flips only near-tie **outliers**, not near-decisive winners (569g 1/3 seeds
strict-above a temperature-matched control; 662 `TV>0` but no entropy lift). Upstream-magnitude
sweeps (667/640a byte-identical) cannot fix this -- the authority **range-renormalizes its
input** -- so only authority **gain** and arbitration **structure** are live levers.

Two no-op-default conversion levers (`e3_selector.py` authority block + selection site):

**(a) gain/contrast normalization** -- `E3Config.modulatory_authority_normalize_basis`:
- `"range"` (default, bit-identical legacy): `target = gain * raw_score_range`, scaled by the
  modulatory **range** -- outlier-sensitive, near-tie-only.
- `"std"`: `target = gain * raw_score_std`, scaled by the modulatory **std** -- robust to
  outliers, anchoring authority to the *typical* primary spread so the structured channel
  competes against **near-decisive** candidates. `modulatory_authority_gain` stays sweepable.
  *Safety:* additive gain `>= 1.0` breaks the safety bound (modulatory can override a
  clearly-harmful rejection); keep gain `< 1.0` on the additive path for the shipped config,
  or use lever (b).

**(b) shortlist-then-modulate** -- `use_modulatory_shortlist_then_modulate` +
`modulatory_shortlist_margin` (0.25): F (raw primary scores) filters to a near-tie set
(candidates within `margin * raw_score_range` of the best raw score), then the modulatory
channel (`_modulatory_accum`) **arbitrates the winner within that set** (argmin when committed,
softmax-sampled when uncommitted). The structured channel is load-bearing **without
out-magnitude-ing F**, and **safety is preserved at any internal strength** (clearly-harmful
candidates outside the shortlist are never selectable). Takes precedence over the
additive-authority rescale + argmin/stratified selection when enabled.

**Diagnostics** on `last_score_diagnostics`: `modulatory_authority_normalize_basis`,
`modulatory_shortlist_active`, `modulatory_shortlist_size`.

**Contracts** (`tests/contracts/test_e3_score_bias_candidate_support.py`): conversion-amend
OFF bit-identical; std-basis distinct scale_factor; shortlist restricts to the F near-tie set
and preserves safety (worst-primary never selected even with overwhelming pull); shortlist
arbitrates by the modulatory channel within the set. Full suite 1036 contracts + 7 preflight
PASS with both levers OFF.

**Validation:** V3-EXQ-684 claim-free readiness sweep (gain x {range,std} x shortlist vs a
**verified-lifting** matched-noise control; committed-action entropy must MOVE with channel
range AND beat the control, not merely reach the accumulator). On PASS, **V3-EXQ-569h**
(the GAP-A falsifier with an in-arm applied-route-range non-vacuity gate) is queued with the
winning conversion config. ARC-065 stays provisional / non_contributory /
pending_retest_after_substrate; not weakened.

## See also

- `ree-v3/ree_core/predictors/e3_selector.py` (additive authority + V3-EXQ-643a explicit
  accumulator + route-range `project_channel_range` + conversion gain/contrast + shortlist),
  `e3_score_diversity.py` (stratified normalization), `ree_core/utils/config.py` (flags).
- 569g autopsy (the corrected conversion-ceiling diagnosis routing this amend):
  `evidence/planning/failure_autopsy_V3-EXQ-569g_2026-06-14.{md,json}`.
- Cluster autopsy: `evidence/planning/failure_autopsy_604a-624a-630_2026-06-03.{md,json}`.
- 643 autopsy (root cause corrected by the 643a fix above):
  `evidence/planning/failure_autopsy_V3-EXQ-643_2026-06-06.{md,json}`.
- MECH-343 working hypothesis: `docs/thoughts/2026-06-03_difficulty_gated_proposal_entropy.md`.
