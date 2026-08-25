# Diagnostic: why does MECH-314b's per-candidate path move ZERO argmins? (chip-20260823-exq947-dose-axis-vs-queue-as-briefed, Option C)

**Date:** 2026-08-25T13:22:30Z
**Chip:** chip-20260823-exq947-dose-axis-vs-queue-as-briefed (Option C: measure why, before deciding on a dose axis)
**Type:** `complex (probe-gated)` diagnostic, not a build. Read-only against production code.

**Verdict up front: the null is not a weight-magnitude problem, it is the
already-documented 604a/624a/614d/640a modulatory-bias-selection-authority
failure class recurring at 314b. `structured_curiosity`'s per-candidate
contribution (`last_uncertainty_dev_range`) is ~1.5-2e-05 in this environment
while the base E3 `raw_score_range` the argmin actually operates over is
~270-290 -- a ratio of ~1.4-1.8e7x. Critically, this is NOT closeable by
raising `curiosity_uncertainty_weight`: the contribution is hard-clamped to
`curiosity_bias_scale` (0.1 default) before it ever reaches the argmin, and
0.1 is itself ~2700-2900x too small relative to `raw_score_range`. The
existing (already-built, off-by-default) fix is `use_modulatory_selection_authority`,
which rescales the combined modulatory bias to `modulatory_authority_gain *
raw_score_range` -- confirmed empirically below to change `post_score_range`
materially, unlike a weight sweep.**

---

## 1. Motivation

`mech314b_percandidate_2x2_design_and_null_authority_2026-08-23.md` found
MECH-314b's live per-candidate path changes the committed action on 0/320
paired ticks at both diversity floors, with every ARC-065 section-5 readiness
precondition green, and flagged an unconfirmed hypothesis: `last_uncertainty_dev_range`
measured ~1.5e-05 "may be orders of magnitude below the other E3 score
channels' spread." Decision chip `chip-20260823-exq947-dose-axis-vs-queue-as-briefed`
put three options to the user (queue V3-EXQ-947 as briefed / add a
`curiosity_uncertainty_weight` dose axis / measure why first), recommending
"Option C then B." User selected Option C (`AskUserQuestion`, matched
recommendation).

## 2. Method

Read-only diagnostic against production `ree_core` code -- no source edited.
One throwaway script (`ree-v3/_score_bias_magnitude_scratch.py`), written and
deleted in-session, not committed, reusing the exact `_Runner`/`build_config`
pattern from `experiments/v3_exq_947_mech314b_percandidate_2x2_diversity_validation.py`
(same seed 71, `CausalGridWorldV2`, 4 episodes x 80 steps = 320 ticks, floor 5
= `action_dim`, `warmup_steps=100`, 314b ON). Per tick, alongside
`agent.curiosity.get_state()`'s existing `last_uncertainty_dev_range` /
`last_novelty_dev_range` / `last_bias_range` / `last_clamp_saturated_frac`,
additionally read `agent.e3.last_raw_scores` and `agent.e3.last_scores`
(both already stored, undocumented-but-public attributes -- no new
instrumentation needed) and computed their range (`max - min`), i.e. the
actual score magnitude the argmin operates over, before and after the
combined modulatory bias is applied.

## 3. Results

### 3a. Baseline (`use_modulatory_selection_authority` OFF, matching the 947 driver's `build_config`)

| floor | n | `unc_dev_range` (mean) | `nov_dev_range` | `bias_range` | `raw_score_range` (mean) | `post_score_range` | ratio raw/unc |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 320 | 1.52e-05 -- 1.67e-05 (2 runs) | **0** (every tick) | == unc_dev_range (ratio 1.00x) | 271 -- 285 | == raw_score_range exactly | **1.4-1.8e7x** |
| 2 | 320 | 4.08e-06 | 0 | == unc_dev_range | 96.2 | == raw_score_range exactly | 2.4e7x |

`nov_dev_range == 0` on every one of 320 ticks at both floors: `use_curiosity_novelty`
is not firing in this `REEConfig.from_dims`-bare build (no active residue
centers, same condition the modulatory-bias-selection-authority claims.yaml
entry independently notes for 604a: "curiosity bias was genuinely zero (314a
no active residue centers"). Consequence: in this build `structured_curiosity`'s
entire combined bias is attributable to 314b alone (`bias_range == unc_dev_range`
to 5 significant figures), so this diagnostic cleanly isolates 314b's own
authority rather than a novelty/uncertainty mixture.

`post_score_range == raw_score_range` to displayed precision at every tick --
the applied bias never moves the score span at all, mechanically confirming
the 2x2's 0/320 divergence rather than merely correlating with it.

### 3b. `use_modulatory_selection_authority=True`, `modulatory_authority_gain=0.5` (floor 5, otherwise identical)

| metric | baseline | authority ON |
|---|---:|---:|
| `unc_dev_range` (curiosity's own diagnostic, pre-rescale) | 1.52e-05 | 2.05e-05 (unchanged in kind -- still tiny) |
| `raw_score_range` (mean) | 271.4 | 283.5 |
| `post_score_range` (mean) | 271.4 (== raw) | **243.8** (diverges from raw) |
| `post_score_range` (last tick) | 284.9 (== raw) | **178.4** vs raw 296.6 |

`curiosity.get_state()`'s `last_bias_range` stays tiny under authority-ON,
because it is computed *inside* `compute_score_bias()`, before the
`e3_selector.select()`-level rescale -- it is not the wrong statistic, it is
answering a different question (curiosity's own internal composition, not
the force actually applied at commit). What changes is `post_score_range`,
which now diverges materially from `raw_score_range` -- direct evidence the
combined modulatory bias (100% curiosity/314b in this build, per 3a) is being
rescaled to a magnitude genuinely competitive with the base score span,
exactly as `use_modulatory_selection_authority`'s design intends.

## 4. Why this is the 604a/624a/614d/640a class, not a new failure

`REE_assembly/docs/claims/claims.yaml` already carries, on multiple claims
(MECH-314b's own siblings among them, `claims.yaml:50609` / `:54843` /
`:61524`), a **2026-06-03 substrate landing** entry for exactly this
mechanism: *"Root cause (604a/624a/614d cluster autopsy): fixed small bias
magnitudes (~0.05-0.1) added to primary scores whose raw_score_range is much
larger never change the argmin."* `use_modulatory_selection_authority`
rescales the combined modulatory contribution to
`modulatory_authority_gain * raw_score_range`. Status: `implemented_pending_validation`
in `substrate_queue.json`, default OFF/bit-identical, cited from 111
existing experiment driver call sites. **This diagnostic establishes that
MECH-314b's V3-EXQ-947 null is a new instance of that same cluster, measured
directly (magnitude ratio) rather than inferred from a null result alone.**

The 2x2 driver's `build_config()` does not set `use_modulatory_selection_authority`
or `normalize_score_bias_to_e3_range` -- both default False, so V3-EXQ-947 as
designed was, mechanically, guaranteed to return zero regardless of seed
count. Extra seeds would not have changed this: the gap (~1.4-1.8e7x at
current weights, ~2700-2900x even if `curiosity_uncertainty_weight` were
raised until the deviation fully saturates `curiosity_bias_scale`) is not a
sampling-noise-sized gap.

## 5. Consequence for the two open options

**Option A (queue V3-EXQ-947 as briefed) is no longer recommended.** The
"determinate weakens" framing in the 2x2 doc understated the case -- this is
not merely determinate at n=1 seed, it is *mechanistically* determinate: the
gap is architectural (bias-scale-vs-raw-score-range), not statistical, so 5
seeds x 4 arms (~2-3h cloud) would spend real compute reconfirming an
already-proven-null rather than adding information.

**Option B as originally scoped (sweep `curiosity_uncertainty_weight`) is
also not recommended, and for a specific reason worth stating plainly: it
cannot work.** `curiosity_uncertainty_weight` only scales the pre-clamp
deviation up to `curiosity_bias_scale` (0.1); increasing it further does
nothing once clamped (`last_clamp_saturated_frac` was 0 throughout this
diagnostic, meaning even at the CURRENT tiny weight the deviation is nowhere
near the rail -- so headroom exists up to 0.1, but 0.1 itself is ~2700-2900x
too small). No weight value can close a gap whose ceiling is fixed by
`curiosity_bias_scale`, not by the weight.

**The corrected dose axis is `use_modulatory_selection_authority` /
`modulatory_authority_gain`, not `curiosity_uncertainty_weight`.** Section 3b
confirms this axis actually moves the applied score magnitude, which neither
the baseline nor a weight sweep could do. This also has real governance
value beyond MECH-314b: `use_modulatory_selection_authority` itself is
`implemented_pending_validation` and explicitly awaiting "a per-claim
EVIDENCE retest on the authority-ON substrate" as its own governance-weighting
signal (`claims.yaml`) -- a MECH-314b authority-ON retest would serve both
claims at once.

## 6. Scope held

This session did not: touch `ree_core/policy/structured_curiosity.py`,
`ree_core/predictors/e3_selector.py`, or `ree_core/utils/config.py`
(read-only diagnostic); modify or queue any experiment (the diagnostic script
was throwaway, not the 947 driver); close or modify the orphaned TASK_CLAIMS
entry `worktree-agent-a53b125a2ecbdbfa7` (not this session's call; confirmed
via `task_claim.py check` that it no longer blocks arbitration, being >48h
stale and therefore excluded automatically); change any `claims.yaml` field.

## 7. Follow-on

1. **Design + queue an amended MECH-314b validation experiment** (new EXQ or
   an amended V3-EXQ-947) crossing 314b ON/OFF x `use_modulatory_selection_authority`
   ON/OFF (at the existing default `modulatory_authority_gain=0.5`, or a small
   sweep of it), with the same yoked-pair + private-RNG-stream + in-run
   pairing-control design the 2x2 driver already validated. This both
   answers "does 314b carry real argmin authority once the known scale
   mismatch is corrected" and supplies the substrate-readiness retest
   `use_modulatory_selection_authority` itself is gated on. Via
   `/queue-experiment`, chipped rather than built here (scope + review
   process).
2. V3-EXQ-947 as originally briefed is NOT recommended for queuing (section
   5) -- superseded by follow-on 1, which subsumes its 314b ON/OFF factor and
   adds the one that matters.
