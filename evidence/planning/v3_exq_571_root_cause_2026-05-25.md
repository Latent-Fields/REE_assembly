# V3-EXQ-571 bias-channel propagation: root cause 2026-05-25

## Status

**ROOT-CAUSED.** The V3-EXQ-571 observation `bias_fraction_curiosity = 0.0`
(and zero for every other diversity-stack bias channel: dacc, lateral_pfc,
ofc, gated_policy, mech295_liking, tonic_vigor) is a real propagation failure
to E3 selection, but the failure site is **upstream of every bias channel**,
not in score_bias plumbing. Same root cause as the 2026-05-17 ARC-062 GAP-B
autopsy; the GAP-B fix was scoped only to `GatedPolicy`.

This note does not modify `claims.yaml`, `substrate_queue.json`, or
`review_tracker.json`. Governance dispositions are proposed at the bottom for
a separate session to land.

## Verified facts

### F1. MECH-111 broadcast novelty branch is dead-by-construction

[`ree-v3/ree_core/predictors/e3_selector.py`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py) lines 606-613 subtract a single scalar `self._novelty_ema`
uniformly from every candidate's score. Uniform shift is argmin-invariant,
so the branch has no behavioural effect under any
`config.novelty_bonus_weight`. V3-EXQ-590a's bit-identical per-seed metrics
across `novelty_bonus_weight ∈ {0.1, 0.3, 0.5, 0.7, 1.0}` is a direct
consequence. Deleted in the same session as this note; pure cleanup, no
behaviour change.

### F2. score_bias plumbing into E3 selection is correct

End-to-end trace verified:

- `REEAgent.select_action()` composes per-channel biases into
  `dacc_score_bias` ([`ree_core/agent.py:3275-3322`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/agent.py)
  for MECH-314a curiosity; sibling blocks for dacc, lateral_pfc, ofc,
  gated_policy, mech295, tonic_vigor) and passes it as
  `score_bias=dacc_score_bias` to `e3.select()` ([`ree_core/agent.py:3455`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/agent.py)).
- `e3.select()` adds the bias to per-candidate scores
  ([`ree_core/predictors/e3_selector.py:737`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py) `scores = scores + bias_tensor`).
- Selection is `argmin(scores)` (committed) or `multinomial(softmax(-scores/T))`
  (uncommitted), both on the biased scores ([`ree_core/predictors/e3_selector.py:807-810`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py)).

If `score_bias[i]` varies across `i ∈ [K]`, argmin shifts. There is no
plumbing-side bug.

### F3. EXQ-571's `bias_fraction_curiosity` is a mean-collapsed scalar

The diagnostic at [`ree_core/agent.py:3437-3448`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/agent.py) records
`_last_score_bias_decomp["curiosity"] = _bdc_mean(_bdc_curiosity)`, i.e. the
mean of the `[K]` bias vector across candidates. For a per-candidate signal
whose mean-across-K is roughly stationary in time, the temporal variance of
the mean-across-K is ~0 even when per-candidate spread within each step is
non-zero (which is what actually shifts argmin). The diagnostic was unsuited
to detect a per-candidate signal that nevertheless **fails for an upstream
reason**, and so it reads zero for both the right and the wrong reason in
the current substrate state.

### F4. The real per-candidate signal is structurally zero

Empirical drivers (`/tmp/verify_mech314a_propagation.py`,
`/tmp/verify_mech314a_with_residue.py`):

- Default untrained agent, `use_structured_curiosity=True`,
  `curiosity_novelty_weight=0.5`, `curiosity_bias_scale=1.0`, 30 waking
  ticks: `_bdc_curiosity` is identically `[0, 0, ..., 0]`. Cause:
  `residue_field.rbf_field.active_mask.sum() == 0` for every tick, because
  `residue_field.accumulate()` only fires on `harm_occurred=True` AND a
  committed trajectory ([`ree_core/predictors/e3_selector.py:894`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py)). Untrained
  random-policy runs satisfy neither. MECH-314a's
  `_compute_novelty` returns `None` (line 414 of `structured_curiosity.py`)
  and contributes zero.

- Same agent with `residue_field` manually seeded with 8 RBF centers (so
  `cur_n_active=8`, `last_novelty_norm=14.72`): bias magnitude saturates the
  ±1.0 clamp at `mean_bias=-1.0`, but `std_bias=0.0000` across K=32.
  Inspection of candidate first-step `z_world` summaries:
  `cand_world_pairwise_dist = 0.0000` across K=32, even though
  `cand_action_std=0.034-0.044` and 2-3 unique argmax action classes
  exist. **All K candidates produce the same z_world after one E2
  world-forward step, despite differing in their first action.**

### F5. F4 is the same root cause as 2026-05-17 ARC-062 GAP-B autopsy

`ree-v3/CLAUDE.md` "ARC-062 GatedPolicy GAP-B" entry, verbatim:

> SP-CEM delivers ~5 distinct first-action classes but E2 world-forward
> compresses them to 0.22% of z_world magnitude before reaching the
> z_world-only GatedPolicy heads -- the heads are under-fed. Fix: bypass
> E2 compression by concatenating the first-action one-hot directly onto
> the head's candidate_features input.

The GAP-B fix `gated_policy_use_first_action_onehot` was scoped only to
GatedPolicy. **Every other bias channel that reads `cand_world_summaries`
(MECH-314a curiosity novelty, MECH-320 tonic_vigor, MECH-295 liking,
SD-033a lateral_pfc, SD-033b ofc) consumes the same compressed
first-step `z_world` and is doomed by the same upstream collapse.**

## Diagnosis

- The MECH-111 broadcast branch is dead and contributes nothing in any
  configuration.
- MECH-314a's `_compute_novelty` is correctly wired to ResidueField and
  produces per-candidate output when fed diverse `cand_world_summaries`
  against active centers — but its inputs collapse for two independent
  reasons:
  1. **ResidueField is empty in untrained runs.** It only accumulates on
     harm-occurred + committed-trajectory events; untrained agents
     experience neither during EXQ-571-style probes.
  2. **Even with active centers, K candidates share identical first-step
     z_world.** E2's world-forward predictor compresses the K diverse
     first-action one-hots to a single z_world, the same bottleneck the
     2026-05-17 GAP-B autopsy identified and patched only for GatedPolicy.
- EXQ-571's `bias_fraction_*` mean-collapsed scalar is a methodology
  weakness — it cannot distinguish "channel emits zero" from "channel
  emits a non-zero per-candidate vector with stationary mean" — but in
  the current substrate state the channel does literally emit zero, so
  the conclusion is right for the wrong reason.

## Acted on this session

- Deleted dead MECH-111 broadcast branch ([`ree-v3/ree_core/predictors/e3_selector.py`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py) lines 606-613). `_novelty_ema` instance state,
  `update_novelty_ema()` method, and `novelty_bonus_weight` config field are
  intentionally retained so the ~30 existing call sites that pass
  `novelty_bonus_weight=0.0` are bit-identical. `score_components.novelty_weighted` in `last_score_decomp` stays at 0.0 (was already 0.0 because
  the branch was a no-op).
- Wrote this finding doc.

## NOT acted on this session (proposed governance follow-ons)

The following are governance acts that change cross-session reasoning and
should be landed by separate sessions with explicit user assent:

1. **substrate_queue.json ARC-065 `failure_record`** currently reads "Bias
   channel present in substrate but not propagating to E3 selection." The
   wording implies a plumbing bug. Replace with: "Bias channels (MECH-314a,
   MECH-320, MECH-295, SD-033a, SD-033b) are correctly composed into the
   `score_bias` kwarg of `e3.select()` and added to per-candidate scores at
   `e3_selector.py:737`. Per-candidate spread is structurally zero because
   E2 world-forward compresses K diverse first-action candidates to
   identical first-step z_world (same root cause as 2026-05-17 ARC-062
   GAP-B autopsy; GAP-B fix `use_first_action_onehot` scoped only to
   GatedPolicy). Gate (a) per-candidate propagation cannot be cleared by a
   score_bias wiring change; requires either (i) extending GAP-B
   first-action one-hot bypass to all bias-channel consumers of
   first-step z_world, or (ii) fixing the E2 world-forward predictor to
   preserve per-action z_world divergence, or (iii) sourcing per-candidate
   novelty from non-z_world signals (raw action one-hots, candidate-pool
   relative-rank, hippocampal anchor identity)."

2. **MECH-314 pending_retests block on substrate_queue.json**: the
   V3-EXQ-590b `note` currently gates the retest on "MECH-314a per-candidate
   RBF novelty Goldilocks calibration ... gated on ARC-065 behavioural-
   diversity-generation landing in addition to MECH-314a propagation
   validation". Per F4/F5, the gate (a) "per-candidate propagation
   validated" is structurally unmeetable in the current substrate state.
   Either move EXQ-590b into a "blocked_until" state with the explicit
   blocker named, or supersede the goldilocks-calibration framing entirely
   (the calibration is meaningless until the per-candidate signal is
   non-zero).

3. **EXQ-571 diagnostic methodology**: surface per-candidate spread
   (`std_across_K`) AND per-candidate range
   (`bias_range_mean = max - min`) in `agent._last_score_bias_decomp`
   alongside the existing `mean_across_K`. Without this, future EXQ-571-style
   probes will continue to produce the same false-positive "bias channel
   not propagating" headline even after the actual upstream fix lands. The
   raw values are already captured on `agent.e3.last_score_diagnostics`
   ([`ree_core/predictors/e3_selector.py:744-764`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py)
   `score_bias_range_mean`, `score_bias_to_raw_range_ratio`) — they just
   are not exposed per-channel in the decomp record.

4. **Q-044 three-arm sub-flavour ablation** (MECH-314a/b/c isolation): the
   314a per-candidate arm is structurally indistinguishable from the 314b/c
   broadcast-scalar arms while the upstream collapse persists, since 314a's
   per-candidate output is itself broadcast-equivalent. Q-044 should be
   marked blocked-by E2-world-forward-fix in `claims.yaml`.

5. **Forward-looking architectural question (not blocking)**: should
   MECH-314a source novelty from a richer signal — a rolling buffer of
   recently-visited z_world prototypes that ALWAYS populates on waking
   ticks (independent of harm + commitment), or from first-step action
   one-hots, or from candidate-pool relative rank — so it can produce a
   non-zero contribution even before the E2 world-forward bottleneck is
   addressed and even on first-encounter / harm-free episodes? This was
   hinted at in the original task brief ("distance to a buffer of
   recently-visited z_world points under an RBF kernel"). Worth queuing as
   an MECH-314a-Phase-2 design question alongside the E2 fix.

## Evidence

- Empirical drivers (one-off; not committed):
  `/tmp/verify_mech314a_propagation.py`,
  `/tmp/verify_mech314a_with_residue.py`.
- V3-EXQ-571 manifest: [`evidence/experiments/v3_exq_571_e3_score_variance_decomp_20260516T004017Z_v3.json`](../experiments/v3_exq_571_e3_score_variance_decomp_20260516T004017Z_v3.json).
- V3-EXQ-590a manifest: [`evidence/experiments/v3_exq_590_isef004_novelty_bonus_goldilocks/v3_exq_590_isef004_novelty_bonus_goldilocks_20260525T084057Z_v3.json`](../experiments/v3_exq_590_isef004_novelty_bonus_goldilocks/v3_exq_590_isef004_novelty_bonus_goldilocks_20260525T084057Z_v3.json).
- 2026-05-17 ARC-062 GAP-B autopsy: see `ree-v3/CLAUDE.md` "ARC-062
  GatedPolicy GAP-B head-input first-action one-hot augmentation" block.
