# SYNTHESIS — Event Segmentation Literature Pull (MECH-288)

**Date:** 2026-04-22
**Claim under test:** MECH-288 (`hippocampal.event_segmenter`, candidate, v3_pending)
**Entries:** 11 papers (this directory) + re-cites from `targeted_review_v_s_foundation/` (Sols/DuBrow/Davachi 2017, Eichenbaum 2017)
**Author:** lit-pull session "litpull-event-segmentation-2026-04-22T19"

This synthesis is intended to be **actionable enough that the next session can write `event_segmenter.py` without re-reading any of the papers**. Each verdict states the answer, the evidence, and the default substrate config implied.

---

## Q1 — Trigger criteria: PE-spike vs latent change-point vs task marker

**Verdict:** Hybrid, with PE-spike as primary trigger and latent change-point as secondary. Task markers are optional (keep API surface but do not require for the default substrate).

**Evidence:**
- Zacks 2007 (EST, conf 0.88) — PE-spike account is the dominant theory; behavioural and fMRI evidence robust.
- Speer 2007 (conf 0.78) — narrative event boundaries align with cortical PE transients.
- Heilbron 2018 (conf 0.65, mixed) — PE-spike has biological grounding for hierarchical PE responses; but biology has NOT validated separate "error neuron / prediction neuron" architecture, so do not over-architect.
- Baldassano 2017 (conf 0.90) — HMM-recovered latent state changes capture the hierarchical/slow-scale boundaries that pure PE on raw stream tends to miss.
- DuBrow 2014/2016 (conf 0.78/0.75) — task-marker boundaries (context shifts) produce the same memory signatures as perceptual ones; argues for keeping task markers as an injectable trigger but not the primary mechanism.

**Substrate decision:**
- Fast scale (z_world, z_self): **PE-threshold only** (algorithm (c) in Q4). Cheap, biologically warranted, gives a graded signal already.
- Slow scale (z_goal, narrative scale): **PE-threshold OR BOCPD run-length posterior** (algorithm (a) in Q4) — BOCPD because schema-scale boundaries are weakly visible in instantaneous PE.
- Task markers: expose `force_boundary(reason)` API hook; do not wire to default trigger logic.

---

## Q2 — Hierarchical vs flat segmentation (Baldassano nested timescales)

**Verdict:** **Hierarchical, with two levels in the v3 substrate. Defer three+ levels to a later phase.**

**Evidence:**
- Baldassano 2017 (conf 0.90) — direct fMRI demonstration of nested timescales: posterior sensory cortex segments at seconds, mid-level cortex at tens of seconds, mPFC/AG at minutes. The same data-generating process (HMM event detection) recovers all levels with only a timescale parameter swap.
- Brunec 2018 (conf 0.74) — anteroposterior hippocampal gradient mirrors the same multi-scale story inside HC; not separate substrates, just different time constants along a gradient.
- Eichenbaum 2017 (re-cited from v_s_foundation) — single hippocampal substrate spans event-segment scale and place-cell-field scale via parametric refinement.

**Substrate decision:**
- Two scales by default: **fast** (≈1–5 step / fine perceptual / place-cell-field-equivalent) and **slow** (≈20–100 step / event-segment / schema-scale).
- Segment IDs encoded as `outer.inner` strings (e.g. `"goal_segment_42.action_subsegment_7"`). Outer increments only when the slow-scale detector fires; inner resets on outer-fire and on its own fast-scale fires.
- Same boundary-detection algorithm at both levels with different `tau` and `min_segment_length` parameters. Do NOT instantiate separate detector classes.
- Three+ levels deferred (Phase 3); the API should accept a list of scale-configs so adding levels later is a config change, not a rewrite.

---

## Q3 — Coupling to MECH-287 broadcast trigger

**Verdict:** **MECH-287 broadcast is downstream of MECH-288 boundary detection** (option (c) in the spec). MECH-287 should NOT implement its own independent comparator. Add a phasic/tonic guardrail.

**Evidence (this is the strongest single result of the pull):**
- Clewett 2025 (conf 0.92) — multi-modal (fMRI + neuromelanin + pupillometry) demonstration that event boundaries trigger pupil-linked LC activation, which in turn predicts hippocampal pattern separation in DG. This directly evidences MECH-287/288 coupling at the BOLD timescale.
- Cohn-Sheehy 2021 (conf 0.82) — boundary HC activity is integrative as well as separative; confirms the boundary event is the moment downstream broadcast/integration occurs.
- Clewett 2025 (failure signature 2) — hyperaroused tonic LC activity DISRUPTS phasic boundary-locked LC. The substrate must keep MECH-287's broadcast distinct from background tonic noise.

**Substrate decision:**
- MECH-288 emits `BoundaryEvent(segment_id_old, segment_id_new, scale, posterior, sources)`.
- MECH-287 subscribes to MECH-288 BoundaryEvents and triggers broadcast at the moment of fire — no second comparator code.
- Broadcast strength = scaled function of MECH-288 posterior (graded, not binary). Calibrated against Aston-Jones-Cohen 2005 phasic/tonic distinction (already captured in v_s_invalidation pull).
- If MECH-287's tonic-noise level exceeds threshold, the substrate suppresses the next phasic broadcast (guardrail; see Clewett 2025 failure signature).

---

## Q4 — Substrate algorithm (BOCPD vs HSMM vs threshold-on-PE vs latent change-point)

**Verdict:** **Default = threshold-on-PE (c) for fast scale. BOCPD-Gaussian (a) for slow scale. Defer HSMM (b) and full HMM (d) to Phase 3.**

**Evidence:**
- Adams & MacKay 2007 (conf 0.80) — BOCPD is the canonical online change-point algorithm; gives a calibrated run-length posterior usable directly as a graded boundary signal. Pruned-run-length variant scales O(1) per step in practice.
- Baldassano 2017 (conf 0.90) — HMM-event-segmentation is the right model for hierarchical/narrative scale, but full HMM is offline-EM in their pipeline; an online approximation is the practical Phase 2 option.
- Heilbron 2018 — supports threshold-on-PE as biologically tractable; warns against over-architecting separate prediction/error modules.
- Heusser 2018 (conf 0.72) — perceptual boundaries align with multivariate pattern transitions, supporting both PE-threshold (low-level) and latent change-point (mid-level).

**Substrate decision (canonical config to ship):**
```
EventSegmenter(
  scales=[
    Scale(name="fast", streams=["z_world","z_self"],
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
- BOCPD is implemented with Gaussian per-segment likelihood and Hazard=1/expected_segment_length. Run-length posterior pruned to top-k=20.
- PE-threshold uses normalised PE z-scored over a sliding window (length=200 steps).
- Both algorithms emit a `BoundaryEvent` with `posterior` field; downstream uses posterior as graded broadcast strength.

**Decisive advantage of this default**: matches biological evidence (PE-threshold for sensory; latent change-point for schema), is online-tractable, and exposes the posterior as a graded signal so MECH-287 doesn't need binary thresholding.

---

## Q5 — Place-cell-field as parametric refinement vs separate substrate

**Verdict:** **CONFIRMED — place-cell-field-scale boundaries and event-segment-scale boundaries are parametric variants of one substrate, NOT separate substrates.**

**Evidence:**
- Eichenbaum 2017 (re-cited from v_s_foundation; verdict 1 of that pull already established this) — single hippocampal substrate handles both granularities.
- Brunec 2018 (conf 0.74) — anteroposterior hippocampal gradient gives the natural anatomical multi-scale support: posterior HC fast (place-cell-field), anterior HC slow (schema/event). Same circuitry, different time constants along the axis.
- Baldassano 2017 — same HMM model recovers all scales with timescale parameter swap.

**Substrate decision:**
- Scales differ ONLY in `(tau, min_segment_length, algorithm_choice)` parameters within `Scale(...)` configs. No separate detector class for place-cell-field-scale.
- MECH-269 anchor-set keys are scale-tagged (e.g. `anchor[scale=fast][segment_id="3.7"]`) so the same anchor mechanism handles both granularities without code duplication.
- Per-stream tau values (V_s lit-pull verdict 1) flow naturally into this design as the per-Scale `tau` parameter.

---

## Confidence summary

| Question | Verdict confidence | Strongest evidence |
|----------|-------------------|---------------------|
| Q1 trigger | 0.85 | Zacks 2007, Heilbron 2018, Baldassano 2017 |
| Q2 hierarchy | 0.88 | Baldassano 2017, Brunec 2018 |
| Q3 coupling | 0.92 | Clewett 2025 (decisive) |
| Q4 algorithm | 0.80 | Adams 2007, Baldassano 2017, Heilbron 2018 |
| Q5 parametric refinement | 0.90 | Eichenbaum 2017, Brunec 2018, Baldassano 2017 |

**Aggregate MECH-288 lit_confidence (recommended):** 0.85 (supports → upgrade candidate to active-pending-V3-experiment).

The single decisive paper is **Clewett 2025** for Q3. The single most generative paper for substrate design is **Baldassano 2017** (covers Q2, Q4, Q5 simultaneously).

---

## Pseudocode API for `event_segmenter.py`

```
class BoundaryEvent:
    segment_id_old: str   # "outer.inner"
    segment_id_new: str
    scale: str            # "fast" | "slow"
    posterior: float      # graded boundary strength in [0,1]
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
    def step(self, latent_dict: dict[str, Tensor], pe_dict: dict[str, float], t: int) -> list[BoundaryEvent]: ...
    def force_boundary(self, scale: str, reason: str) -> BoundaryEvent: ...
    def current_segment_id(self) -> str: ...   # returns "outer.inner"
```

---

## Caveats and known unknowns

- **Three-level hierarchy** is plausible (Baldassano 2017 found 3 levels in fMRI) but adding it now risks over-engineering. Defer to Phase 3 with a config-only path.
- **Full BOCPD biological plausibility** is weak (it is engineering; MECH-288 commits only to the *computational role*, not the implementation). Heilbron 2018 cautions against architecting biology that hasn't been tested.
- **HSMM** (Hidden Semi-Markov) was a candidate for slow-scale; rejected for Phase 2 because BOCPD subsumes its essential property (explicit segment-length distribution via the hazard function) at lower complexity.
- **Cross-scale interaction**: when slow-scale boundary fires, must fast-scale boundary also fire? Default: yes (slow boundary forces an inner reset). This is the parsimonious choice; revisit if EXQ evidence contradicts.

---

## Cross-references

- Companion lit-pulls in the same literature root:
  - `targeted_review_v_s_foundation/` (Sols 2017, Eichenbaum 2017, DuBrow/Davachi 2017) — sets the per-stream tau / staleness substrate that MECH-288 reads.
  - `targeted_review_waking_v_s_invalidation/` — tonic/phasic LC distinction (Aston-Jones-Cohen 2005); directly informs Q3 guardrail.
  - `targeted_review_connectome_mech_269/` — anchor-set substrate that MECH-288 BoundaryEvents drive.

- Architectural docs to update next session:
  - `docs/architecture/hippocampal_systems.md` — add MECH-288 substrate config from Q4 verdict.
  - `docs/claims/claims.yaml` — set MECH-288 `lit_confidence: 0.85`, `evidence_direction: supports`, retain `v3_pending: true`.
