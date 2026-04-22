---
nav_exclude: true
---

# Event-Segment Detection Substrate (MECH-288)

**Claim:** MECH-288 (event-segmentation substrate; hippocampal.event_segmenter)
**Status:** candidate, v3_pending
**Registered:** 2026-04-22
**Origin:** Phase 2 substrate planning for V_s invalidation runtime cluster (MECH-269 anchor sets,
MECH-284 staleness accumulator, MECH-287 dual-component trigger) needs region IDs; ree-v3 has no
event-boundary detector at the substrate level. This claim fills the gap.
**Lit-pulls:**
- `evidence/literature/targeted_review_v_s_foundation/` (verdict 1: schema/event-segment as default
  V_s region granularity per Eichenbaum 2017 + Sols-DuBrow-Davachi 2017)
- `evidence/literature/targeted_review_event_segmentation/` (commissioned in parallel, IN PROGRESS;
  spec at `docs/session_prompts/event_segmentation_litpull.md`; will answer the four remaining
  architectural questions and populate the verdict integration section below)
**Depends on:** MECH-269, MECH-284, MECH-287

---

## Problem

The V_s invalidation runtime cluster (MECH-269 anchor sets keyed on `region_id`, MECH-284 staleness
accumulator indexed on `region_id`, MECH-287 dual-component trigger carrying `current_anchor_set`)
all assume the substrate produces a region partition. The foundation lit-pull verdict 1 establishes
that the partition is at schema/event-segment scale, NOT place-cell-field, NOT individual-step
latent-delta. ree-v3 currently has no event-boundary detector — the only "boundary" code is
episode-level (env reset) and the self/other TPJ comparator. Without a substrate-side event-segment
detector, Phase 2 (ii) anchor-set tracking has no native source for the region key.

MECH-288 fills this gap with a per-tick boundary detector that emits monotonic segment IDs.

---

## Mechanism

### 1. Per-tick boundary detection

```
For each tick t:
    boundary(t) = boundary_criterion(z_obs(t), z_pred(t-1), task_markers(t))
    if boundary(t):
        segment_id += 1
        emit_boundary_event(segment_id, t)
```

Consumers read `current_segment_id()` to key region-aware substrates.

### 2. Boundary criterion

**Default first pass** (subject to lit-pull verdict 4):

```
boundary_criterion(z_obs, z_pred, task_markers):
    return norm(z_pred - z_obs) > theta_boundary
```

This is the threshold-on-prediction-error variant matching Zacks 2007's prediction-error account
of event segmentation. It is the cheapest substrate option and aligns with the existing
prediction-error machinery in `ree_core` (E1 deep predictor, ReafferencePredictor, HarmForwardModel).

**Optional alternatives behind config flags** (verdict-dependent — to be confirmed by lit-pull):

- `latent_change_point`: Bayesian online change-point detection (Adams & MacKay 2007 BOCPD-style)
  on the latent stream. Richer; more substrate cost; matches Baldassano 2017 latent-state
  segmentation framing.
- `task_marker`: External sensory cue or action-completion event. Useful for ground-truth-aligned
  segments in supervised regimes.
- `hybrid`: OR over the three signals.

### 3. Hierarchical / multi-scale support

Per foundation verdict 1 + Baldassano 2017 nested timescales (fast-segmenter regions report short
events; slow-segmenter regions report long events), `segment_id` may be hierarchical:
`"segment.outer.inner"`.

**Default first pass:** flat `segment_id` (single integer counter). Hierarchical added as Phase 2
refinement IF event-segmentation lit-pull verdict 2 supports it as architecturally necessary
rather than optional.

### 4. Coupling to MECH-287 broadcast trigger

This is the load-bearing open question for the lit-pull (verdict 3). Three possibilities:

(a) **Independent.** MECH-288 boundaries and MECH-287 broadcast trigger are independent signals
    that happen to correlate (Clewett 2020 LC-at-boundaries is a correlation report, not a wiring
    claim). Architectural implication: MECH-287 keeps its own ComparatorStage; MECH-288 just
    provides region IDs.

(b) **Coupled stages of one comparator.** Boundary detection IS the upstream anchor-side stage
    of MECH-287's dual-component architecture. Architectural implication: MECH-287's ComparatorStage
    code can read MECH-288 boundaries directly; MECH-287's comparator collapses into MECH-288's
    detector.

(c) **Trigger downstream of boundary.** MECH-287 fires when MECH-288 emits a boundary.
    Architectural implication: MECH-287 has no independent threshold; its trigger criterion is
    "MECH-288 emitted a boundary this tick".

**Default first pass: (a) independent.** Refactor path to (b) or (c) reserved pending lit-pull
verdict 3.

---

## Verdict integration (PLACEHOLDER -- to be filled when targeted_review_event_segmentation/ lands)

**Verdict 1 (trigger criteria for boundary detection):** _PENDING_ — will name the canonical
default among prediction-error spike, latent change-point, and task marker, with optional
alternatives behind config flags.

**Verdict 2 (hierarchical vs flat segmentation):** _PENDING_ — will recommend whether the
substrate's first pass is flat segment_id or hierarchical, with rationale from Baldassano 2017
nested timescales.

**Verdict 3 (coupling to MECH-287 broadcast trigger):** _PENDING_ — will discriminate options
(a)/(b)/(c) above; bears directly on whether MECH-287's Phase 2 (iv) implementation needs its
own ComparatorStage or can read MECH-288 boundaries.

**Verdict 4 (substrate algorithm guidance):** _PENDING_ — will recommend default algorithm
(BOCPD vs HSMM vs threshold-on-PE vs latent change-point) with notes on biological mapping.

**Verdict 5 (place-cell-field option):** _PENDING_ — will confirm whether place-cell-field
resolution is a parametric refinement of the same substrate or a fundamentally different one.

This section will be revised in-place when SYNTHESIS.md lands. The MECH-288 entry in claims.yaml
will be revised to match.

---

## Predicted observables (V3 scope)

A V3 experiment validating MECH-288 would measure:

1. **Boundary precision/recall against task-natural events.** With MECH-288 enabled, boundary
   events should fire at task-natural transitions (arrival at goal cell, harm onset, mode switch,
   episode end) at higher rate than at intra-event timesteps. Precision/recall against a
   ground-truth event-boundary set computable from env state.

2. **Downstream usefulness — anchor-set partition quality.** Per-region V_s readouts keyed on
   MECH-288 segment_ids should produce more informative anchor-set partitions than uniform
   place-binning, as measured by anchor-reset latency on V3-EXQ-471 conditions (re-running
   EXQ-475 with MECH-288 + MECH-269 anchor sets enabled).

3. **MECH-287 coupling test (verdict 3 dependent).** If verdict 3 favours option (b),
   lesioning MECH-288 should silently lesion the upstream comparator stage of MECH-287
   (comparator-loss phenotype: silent trigger; broadcast never fires from boundary signals).
   If verdict 3 favours option (a), MECH-287 broadcast should fire normally on threshold
   crossings even with MECH-288 lesioned.

Candidate experiment names (not yet queued):
- `v3_exq_NNN_mech288_boundary_precision_recall.py`
- `v3_exq_NNN_mech288_anchor_partition_quality.py` (downstream usefulness)
- `v3_exq_NNN_mech288_mech287_coupling_factorial.py` (verdict 3 dependent)

---

## Substrate hooks required

- `ree_core/hippocampal/event_segmenter.py` — new module hosting MECH-288. Emits boundary events
  on a queue consumed by HippocampalModule (anchor set keying) and staleness accumulator (region
  indexing). Optionally consumed by `ree_core/regulators/invalidation_trigger.py` ComparatorStage
  if verdict 3 supports option (b) or (c).
- `ree_core/hippocampal/module.py` — extend HippocampalModule to subscribe to the boundary queue;
  uses `current_segment_id()` as `region_id` for anchor-set entries (Phase 2 (ii)).
- `ree_core/utils/config.py` — add `EventSegmenterConfig` with `boundary_criterion`,
  `theta_boundary`, optional `hierarchical_segments` flag.
- `HippocampalConfig.use_event_segmenter` — master switch (default False).

---

## Open design questions

1. **Verdict integration.** All five verdicts above are pending. The substrate first-pass
   defaults are educated guesses; verdicts may revise them.

2. **Event-segmenter run order in agent.tick().** Should the segmenter run before sense() (so
   the segment_id is fresh when V_s readouts compute) or after (so it has the latest latent
   stream)? Current proposal: run inside sense() immediately after latent encoding, before
   per-stream V_s update. Consistent with Phase 1 wiring choice.

3. **Reset semantics on episode boundary.** Does segment_id reset to 0 on env reset, or
   continue monotonically across episodes? Recommendation: continue monotonically (the substrate
   sees one continuous experience stream; episode boundaries are an env artefact, not a
   substrate event). Episode boundaries DO trigger a boundary event with appropriate
   high-magnitude marker.

4. **Stream-mixture default for stream-conditioned anchors.** Phase 2 (ii) plan flags this as
   simple stand-in (`stream_mixture = current_active_streams_at_creation_time`). NOT to be
   confused with MECH-288's segment_id criterion. The learned-attribution-head version is a
   future open question separate from this claim.

5. **False-positive rate calibration.** If `theta_boundary` is set too low, every small
   prediction-error fires a boundary and `segment_id` increments every tick — substrate
   becomes useless region-keying. Surface as diagnostic counter (mean boundary fire rate;
   mean inter-boundary interval) rather than relying on parameter sweep alone.

---

## Status log

- **2026-04-22** — Design doc skeleton written. MECH-288 registered candidate v3_pending in
  claims.yaml. Lit-pull `targeted_review_event_segmentation/` commissioned in parallel (spec
  at `docs/session_prompts/event_segmentation_litpull.md`). Phase 2 (ii)+(iii) substrate
  blocks on verdict integration. Phase 2 (iv) MECH-287 trigger does NOT block on this and
  may proceed in parallel (subject to verdict 3 — if option (b) or (c) holds, the
  ComparatorStage code in invalidation_trigger.py will be refactored to read MECH-288
  boundaries instead of computing its own threshold).
- Verdict integration follows when lit-pull lands.
