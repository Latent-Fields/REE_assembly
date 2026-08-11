---
status: implemented
status_asof: 2026-08-11
status_claim: SD-RESIDUE-VALENCE-BOUND
---

# SD-RESIDUE-VALENCE-BOUND: residue.field.RBFLayer.update_valence.accumulator_bound

**Claim ID:** SD-RESIDUE-VALENCE-BOUND
**Subject:** residue.field.RBFLayer.update_valence.accumulator_bound
**Status:** IMPLEMENTED
**Registered:** 2026-08-09 (as a `substrate_queue.json` entry, from
  `failure_autopsy_V3-EXQ-906a_894b_2026-08-09.md`; scope widened 2026-08-10 by
  `failure_autopsy_906b-906c-911-cluster_2026-08-10.md`)
**Implemented:** 2026-08-11
**Depends on:** none (`substrate_queue.json` `depends_on_unresolved: []`)
**Blocks:** none directly (`unblocks_claims: []`) -- all three motivating runs (906a, 906c, and
  the 906b/906c/911 cluster) are diagnostic showcases with `claim_ids: []`. The fix restores
  trustworthiness to the `excite`/`dread`/`liking` readouts those showcases (and any future
  long-continuity showcase) surface, which several of them explicitly flag as contaminated
  pending this landing (e.g. 906c's `excite_channel_contaminated` precondition).

## Problem

`RBFLayer.update_valence()` (`ree_core/residue/field.py`) is the single write path behind all
six SD-014 / ARC-036 valence components (`wanting`/`liking`/`harm_discriminative`/`surprise`/
`positive_surprise`/`negative_surprise`, MECH-307 Gap-1 Option-b) -- it was a raw

```python
self.valence_vecs[center_idx, valence_component] += value
```

with no decay and no clamp. Only 32 RBF centers exist by default, so a long-lived agent
revisiting the same regions drives the same centers' components unboundedly. Confirmed
end-to-end at three independent points:

- `failure_autopsy_V3-EXQ-906a_894b_2026-08-09.md`: `z_world_norm` ~150-320 and excite/dread "in
  the hundreds" under sustained continuous exposure (203 realized steps, 1 seed), vs ~0.5-0.7 at
  smoke scale.
- `observational_review_V3-EXQ-906b_2026-08-09.md` Section 3d: `excite` mean=14.0, max=42.7 vs
  `dread` mean=1.0, max=2.8 in the same run -- a scale asymmetry the autopsy attributes to the
  same unbounded write, not a real appetitive/aversive difference.
- `failure_autopsy_906b-906c-911-cluster_2026-08-10.md` Finding 2: `liking` mean=19.88 (~50x a
  smoke-observed 0.39 per-step ceiling); `dread` rises 40-110x across 8 episodes in both 906b and
  906c -- independently confirming `liking` and `dread` share the identical write path already
  flagged for `excite`, not three separate bugs.

`ResidueField.update_wanting_sensitized()` (the SD-014 incentive-sensitization WANTING write,
V3-EXQ-887 decouple fix) calls the same `RBFLayer.update_valence()` primitive directly, so
`wanting` shares the identical exposure even though no failure record yet measured it in
isolation.

This is a `complicated (buildable)` node (work-graph debt vocabulary): the mechanism, the bug,
and the fix shape (clamp/decay the accumulator) were fully specified by `substrate_queue.json`'s
`implementation_hint` and the three autopsies above.

## Solution

### Leaky-integrator decay + hard clamp, gated behind a new master switch

```python
# RBFLayer.update_valence(center_idx, component, value, decay_rate=0.0, clamp_abs=None)
current = self.valence_vecs[center_idx, component]
if decay_rate:
    current = current * (1.0 - decay_rate)
updated = current + value
if clamp_abs is not None:
    updated = torch.clamp(updated, -clamp_abs, clamp_abs)
self.valence_vecs[center_idx, component] = updated
```

`decay_rate=0.0, clamp_abs=None` (the defaults) reduce this to exactly the pre-fix `+=` --
bit-identical. `ResidueField.update_valence()` and `ResidueField.update_wanting_sensitized()`
(the two callers, covering all 13 `agent.py` call sites plus the sensitized-wanting path) resolve
both parameters from config through a single shared helper, `_valence_bound_params()`, so the
fix is applied from one point rather than duplicated per call site.

### Why a new master-switch flag, not an unconditional fix

The same-day precedent `SD-ORIENTING-DECISION-SCALE` changed its buggy math's default behaviour
directly, because that code path lived behind an off-by-default master switch
(`use_defensive_orienting=False`) that only one experiment (V3-EXQ-910) had ever exercised --
no historical evidence depended on the old (broken) semantics.

`update_valence()` is the opposite: `ResidueConfig.valence_enabled` defaults `True`, and the
write path is exercised by dozens of historical experiments (V3-EXQ-255/259/263/263a/263b/
332/332a/432/843/887/887a/887b, among others) carrying real `claims.yaml` evidence. Silently
changing its output would be a mechanism change requiring the `/implement-substrate` Step-8.5
evidence-staleness audit across all of them -- disproportionate to a plumbing bound-fix. A new
no-op-default flag avoids that: existing evidence stays bit-identical; new experiments (and the
validation run below) opt in explicitly.

### Config (`ResidueConfig`; all three new fields live together, `ree_core/utils/config.py`)

| Param | Default | Purpose |
|-------|---------|---------|
| `valence_bounding_enabled` | `False` | master switch. `False` -> `update_valence()` is the exact pre-fix `+=`, regardless of the two knobs below. |
| `valence_decay_rate` | `0.02` | leaky-integrator decay applied to the existing value before adding the increment. Mirrors this same config class's existing `integration_rate` (`0.01`) timescale convention, doubled because valence writes fire per-threshold-crossing (sparser) rather than per-step. |
| `valence_clamp_abs` | `5.0` | hard symmetric bound applied after the decayed add. Headroom above the smoke-scale ceiling (~0.39-0.7) while staying far below the observed unbounded contamination (150-320 / 19.88) -- bounded and interpretable, not tuned to any one claim's acceptance threshold. |

Unlike `REEConfig`-level knobs, `ResidueConfig` fields are not threaded through
`REEConfig.from_dims()` as named kwargs (`valence_enabled`/`safety_terrain_enabled` are not
either) -- they are set by direct post-construction assignment
(`cfg.residue.valence_bounding_enabled = True`), matching the existing sibling-flag convention on
this class. No `from_dims()` signature change was needed or made.

### Data flow

```
[agent.py: ~13 update_valence() call sites, incl. MECH-307 split-surprise excite/dread write]  -\
[field.py: update_wanting_sensitized() SD-014 incentive-sensitized WANTING write]                 +-> ResidueField._valence_bound_params()
                                                                                                    |    reads config.valence_bounding_enabled /
                                                                                                    |    valence_decay_rate / valence_clamp_abs
                                                                                                    v
                                                                              RBFLayer.update_valence(decay_rate, clamp_abs)
                                                                                    |
                                                                                    v
                                                                    valence_vecs[center, component]  (bounded when enabled)
```

### Backward compatibility

Confirmed by direct unit test: 200 successive `+1.0` writes to the same component/center produce
exactly `200.0` under default config (bit-identical to the pre-fix `+=`), and a bounded value
(clamped at `valence_clamp_abs`) under `valence_bounding_enabled=True`. `update_wanting_sensitized`
tested identically (unbounded OFF, bounded ON). A full `--dry-run` of
`v3_exq_887_sd014_node_valence_representational_functional.py` (an existing experiment exercising
this exact write path at default config) ran end-to-end with no error.

### Phased training / MECH-094

Not applicable -- `valence_vecs` is a `register_buffer`, not an `nn.Parameter`; every write
already executes under `torch.no_grad()`. No gradient flow, no trainable parameters. MECH-094
gating is unchanged: `ResidueField.update_valence()`'s existing `hypothesis_tag` check is
upstream of the new decay/clamp logic and untouched.

## What This SD Enables

Removes the contamination caveat several diagnostic showcases (906a, 906c) explicitly carry
against `excite`/`liking`/`dread` coupling metrics, for any future run that opts in via
`valence_bounding_enabled=True`. No `claims.yaml` claim currently reads these metrics directly
(all three motivating runs are `claim_ids: []`), so no `v3_pending` flip is made by this landing.

## Descoped: `residue_wanting` orphaned writer

The same failure-autopsy cluster also flagged `update_benefit_salience()`/`update_schema_wanting()`
(the `residue_wanting`/`VALENCE_WANTING` writer methods) as "never called from the 906-family
agent step loop." Traced directly against source: `REEAgent` has no internal step loop at all --
every experiment driver script calls `sense()`/`select_action()`/the `update_*` methods
explicitly itself (confirmed via `experiments/_harness.py`'s `StepHarness` and ~20 other scripts
that already call `update_benefit_salience`/`update_schema_wanting` correctly). The 906-family
driver simply omits these calls. That is an experiment-script gap, not a `ree_core/` substrate
gap -- `ree-v3/CLAUDE.md`'s mandatory skill-path rule restricts `experiments/` edits to
`/queue-experiment` or `/diagnose-errors`, not `/implement-substrate`. Left as a reported
follow-on rather than folded into this change.

## Related Claims

No direct `claims.yaml` claim gates on this SD (`unblocks_claims: []`). Bears on **MECH-307**
(the split-surprise mechanism whose excite/dread writes are the most-affected components) and
**SD-014** / **ARC-036** (the valence-vector mechanism this accumulator belongs to) by
corroboration/repair, not by a status change. See `failure_autopsy_V3-EXQ-906a_894b_2026-08-09.md`
and `failure_autopsy_906b-906c-911-cluster_2026-08-10.md` for the original findings and routing.
