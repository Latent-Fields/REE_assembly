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
- `evidence/literature/targeted_review_event_segmentation/` (COMPLETE 2026-04-22; 11 papers +
  SYNTHESIS.md; aggregate lit_confidence 0.85; decisive paper Clewett 2025 Neuron for verdict 3;
  most generative paper Baldassano 2017 covering verdicts 2/4/5)
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

### 2. Boundary criterion (per scale; verdicts 1 + 4 integrated)

Two algorithms run in parallel, one per scale:

**Fast scale** -- threshold on normalised prediction error:
```
pe_z = (norm(z_pred(t-1) - z_obs(t)) - mu_window) / sigma_window
boundary_fast(t) = pe_z > pe_threshold      # default 0.65
```
PE normalised over a sliding window of length 200. Streams: `z_world`, `z_self`. tau=2.
min_segment_length=2.

**Slow scale** -- BOCPD-Gaussian (Adams & MacKay 2007) on the latent stream:
```
run_length_posterior = bocpd_step(latent, hazard=1/40)
boundary_slow(t) = posterior(run_length=0) > posterior_threshold   # default 0.5
```
Per-segment Gaussian likelihood. Run-length posterior pruned to top-k=20 (O(1) per step in
practice). Streams: `z_goal`. min_segment_length=15.

Both algorithms emit a `posterior` field in [0, 1] consumed downstream by MECH-287 as graded
broadcast strength (no binary thresholding).

**Optional injection (config-only):**
- `task_marker`: external cue. Exposed via `force_boundary(scale, reason)` API hook. NOT wired
  to default trigger logic; available for supervised / scripted regimes.

### 3. Hierarchical / multi-scale support (verdicts 2 + 5 integrated)

**Two scales by default (defer 3+ to Phase 3).** Same detection algorithm at both levels,
parametrically distinguished by `(tau, min_segment_length, algorithm_choice)` -- no separate
detector classes. The API accepts a list of `Scale(...)` configs so a third level is a
config-only addition.

Segment IDs are nested `outer.inner` strings:
- `outer` increments only when the slow detector fires.
- `inner` resets on outer-fire and on its own fast-fires.
- Cross-scale interaction: when slow fires, fast also fires (slow forces inner reset).
  Parsimonious default; revisit if EXQ evidence contradicts.

**Place-cell-field as parametric refinement (verdict 5 CONFIRMED).** Place-cell-field-scale and
event-segment-scale boundaries are parametric variants of one substrate, NOT separate substrates
(Eichenbaum 2017 mixed-selectivity; Brunec 2018 anteroposterior HC gradient; Baldassano 2017
single-HMM recovers all scales with timescale parameter swap). MECH-269 anchor-set keys are
scale-tagged (`anchor[scale=fast][segment_id="3.7"]`) so the same anchor mechanism handles both
granularities without code duplication.

### 4. Coupling to MECH-287 broadcast trigger (verdict 3 DECISIVE)

**MECH-287 broadcast is downstream of MECH-288 boundary detection (option (c)).**

Decisive evidence: **Clewett 2025 Neuron (conf 0.92)** -- multi-modal fMRI + neuromelanin +
pupillometry demonstration that event boundaries trigger pupil-linked LC activation, which in
turn predicts hippocampal pattern separation in DG. This directly evidences MECH-287/288
coupling at the BOLD timescale. Cohn-Sheehy 2021 (conf 0.82) confirms the boundary moment is
when downstream broadcast/integration occurs.

**Implementation:**
- MECH-288 emits `BoundaryEvent(segment_id_old, segment_id_new, scale, posterior, sources, t)`.
- MECH-287 subscribes to MECH-288 BoundaryEvents and triggers broadcast at the moment of fire.
  No second comparator code; the original "ComparatorStage" sub-component collapses to a
  subscriber.
- Broadcast strength = scaled function of MECH-288 posterior (graded, not binary). Calibrated
  against Aston-Jones-Cohen 2005 phasic/tonic distinction (already captured in
  `targeted_review_waking_v_s_invalidation/`).

**Phasic/tonic guardrail (Clewett 2025 failure signature 2):** if MECH-287's tonic-noise level
exceeds threshold, the substrate suppresses the next phasic broadcast. Hyperaroused tonic LC
disrupts phasic boundary-locked LC; the substrate must keep these distinct.

**Architectural reconciliation with MECH-287's "upstream comparator stage" (per V_s foundation
pull verdict 5):** the Vinogradova 2001 CA1/CA3 mismatch + O'Mara 2009 subicular routing +
Lisman & Grace 2005 HC-VTA loop substrate registered for MECH-287 is best read as the
BIOLOGICAL substrate that MECH-288 instantiates computationally. The two entries point at the
same biological circuit from different angles. MECH-287's biological-substrate text remains
accurate; the IMPLEMENTATION-side ComparatorStage sub-component should not duplicate the
detector. Whether to refactor MECH-287's claim text to make this explicit is a downstream
governance decision (tracked in the MECH-287 status log; not contradictory with current
entries).

---

## Verdict integration (COMPLETE -- targeted_review_event_segmentation/ landed 2026-04-22)

| Verdict | Outcome | Strongest evidence | Confidence |
|---------|---------|--------------------|------------|
| Q1 trigger | PE-spike primary + BOCPD secondary; task-markers via API hook only | Zacks 2007, Heilbron 2018, Baldassano 2017 | 0.85 |
| Q2 hierarchy | Two-level nested with `outer.inner` segment IDs; defer 3+ to Phase 3 | Baldassano 2017, Brunec 2018 | 0.88 |
| Q3 coupling | MECH-287 broadcast is downstream of MECH-288 (option c); add phasic/tonic guardrail | **Clewett 2025 (decisive)** | 0.92 |
| Q4 algorithm | PE-threshold on fast scale, BOCPD-Gaussian on slow scale; defer HSMM/full-HMM | Adams 2007, Baldassano 2017, Heilbron 2018 | 0.80 |
| Q5 parametric refinement | CONFIRMED -- place-cell-field is parametric refinement of same substrate | Eichenbaum 2017, Brunec 2018, Baldassano 2017 | 0.90 |

**Aggregate MECH-288 lit_confidence:** 0.85 (supports → recommend upgrade candidate to
active-pending-V3-experiment once substrate code lands).

---

## Pseudocode API (canonical -- to ship in `event_segmenter.py`)

```python
class BoundaryEvent:
    segment_id_old: str   # "outer.inner"
    segment_id_new: str
    scale: str            # "fast" | "slow"
    posterior: float      # graded boundary strength in [0, 1]
    sources: list[str]    # which streams fired
    t: int                # tick when boundary detected

class Scale:
    name: str
    streams: list[str]
    algorithm: str        # "pe_threshold" | "bocpd_gaussian"
    tau: int
    min_segment_length: int
    # algorithm-specific
    pe_threshold: float | None
    hazard: float | None
    posterior_threshold: float | None

class EventSegmenter:
    def __init__(self, scales: list[Scale], emit_to: list[str],
                 scale_id_format: str = "{outer}.{inner}"): ...
    def step(self, latent_dict: dict, pe_dict: dict, t: int) -> list[BoundaryEvent]: ...
    def force_boundary(self, scale: str, reason: str) -> BoundaryEvent: ...
    def current_segment_id(self) -> str: ...   # returns "outer.inner"
```

## Canonical default config (to ship)

```python
EventSegmenter(
  scales=[
    Scale(name="fast", streams=["z_world", "z_self"],
          algorithm="pe_threshold", tau=2, min_segment_length=2,
          pe_threshold=0.65),
    Scale(name="slow", streams=["z_goal"],
          algorithm="bocpd_gaussian", hazard=1/40,
          posterior_threshold=0.5, min_segment_length=15),
  ],
  emit_to=["mech_287_broadcast", "mech_269_anchor_set"],
  scale_id_format="{outer}.{inner}",
)
```

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

1. **Verdict integration.** ~~PENDING~~ COMPLETE 2026-04-22 (see Verdict integration table
   above). Substrate first-pass defaults pinned to canonical config.

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

- **2026-04-22 (am)** — Design doc skeleton written. MECH-288 registered candidate v3_pending
  in claims.yaml. Lit-pull `targeted_review_event_segmentation/` commissioned in parallel
  (spec at `docs/session_prompts/event_segmentation_litpull.md`). Phase 2 (ii)+(iii)
  substrate blocks on verdict integration. Phase 2 (iv) MECH-287 trigger initially planned
  as parallelisable (pending verdict 3).

- **2026-04-22 (pm)** — Lit-pull complete: 11 papers + SYNTHESIS.md, aggregate lit_conf 0.85.
  All five verdicts integrated in-place above. Key results:
  - Verdict 3 = option (c) DECISIVE (Clewett 2025 Neuron). MECH-287 trigger reads MECH-288
    BoundaryEvents; no independent comparator. **Sequencing implication: MECH-288 substrate
    code must land BEFORE MECH-287 Phase 2 (iv) trigger code, not in parallel.** Phase 2
    sequencing revised: (288) → (iv MECH-287) → (ii MECH-269 anchors + iii per-region V_s),
    OR (288) → (ii + iii) → (iv) -- both routes land 288 first; (iv) before (ii+iii) is
    the cleaner test order because it isolates whether the trigger fires correctly before
    we wire the consumers.
  - Verdict 4 pinned canonical config (PE-threshold fast on z_world+z_self; BOCPD-Gaussian
    slow on z_goal). Ready for implementation as-is.
  - Verdict 2 pinned two-level nested `outer.inner` segment IDs. Defer 3+ levels to Phase 3
    (config-only addition).
  - Verdict 5 confirmed place-cell-field as parametric refinement (no separate substrate).
  - Architectural reconciliation flagged with MECH-287's "upstream comparator stage" framing
    (per V_s foundation pull verdict 5): MECH-287's biological-substrate text remains
    accurate; the IMPLEMENTATION-side ComparatorStage sub-component collapses to a
    BoundaryEvent subscriber in the MECH-288 era. Whether to refactor MECH-287 claim text
    to make this explicit is a downstream governance decision (not contradictory with
    current entries; tracked in MECH-287 status log).
