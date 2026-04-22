# Lit-pull spec: Event Segmentation (MECH-288 prerequisite)

**Target claim:** MECH-288 (event-segmentation substrate; candidate v3_pending, registered 2026-04-22 alongside this spec).

**Output directory:** `REE_assembly/evidence/literature/targeted_review_event_segmentation/`

**Why this pull:** Phase 2 of the V_s invalidation runtime work (MECH-269 anchor sets + MECH-284 staleness accumulator + MECH-287 dual-component trigger) needs a substrate-side event-segment detector that emits monotonic segment IDs on detected boundaries. These IDs key the per-region V_s readout and the anchor-set's `region_id` field. The `targeted_review_v_s_foundation/` SYNTHESIS verdict 1 already established that the V_s region unit should be schema/event-segment scale (NOT place-cell-field) per Eichenbaum 2017 and Sols/DuBrow/Davachi 2017. This pull translates that "default schema/event-segment granularity" verdict into a concrete substrate algorithm by surveying the event-segmentation literature directly.

**Architectural questions to answer:**

1. **Trigger criteria for boundary detection.** What does biology actually use to demarcate event boundaries? Three candidate signals:
   (a) Prediction-error spike in a forward model (Zacks 2007 prediction-error account)
   (b) Latent-state change-point (Baldassano 2017 hierarchical-timescale segmentation)
   (c) Task-supplied marker (sensory cue, action completion)
   Recommend one canonical default for the substrate, with optional alternatives behind config flags.

2. **Hierarchical vs flat segmentation.** Baldassano 2017 reports nested timescales — fast-segmenter regions (early visual) report short events; slow-segmenter regions (mPFC, posterior cingulate) report long events. Should the substrate's event-segmenter emit a single segment_id stream or a hierarchical segment_id (`segment.outer.inner`)? Recommend a default architecture with explicit deferrals for what is over-engineering.

3. **Coupling to MECH-287 broadcast trigger.** Clewett et al 2020 reports LC activity at event boundaries. If event boundaries co-fire with LC bursts, then MECH-288 boundary detection and MECH-287 broadcast trigger may share substrate (or one drives the other). Identify whether the literature supports treating them as: (a) independent signals that happen to correlate, (b) coupled stages of the same comparator (boundary detection IS the upstream comparator stage of MECH-287), or (c) MECH-287 broadcast is downstream of MECH-288 boundary. This bears directly on whether MECH-287 needs its own comparator code or can read MECH-288 boundaries.

4. **Substrate algorithm guidance.** What computational method best mirrors the biology? Candidates:
   (a) Bayesian online change-point detection (Adams & MacKay 2007 BOCPD)
   (b) Hidden semi-Markov segmenters
   (c) Threshold-on-prediction-error (cheapest, matches Zacks 2007 directly)
   (d) Latent change-point under variational inference (matches Baldassano 2017 framing)
   Recommend a default for Phase 2 substrate implementation with notes on which biological literature each choice maps onto.

5. **Place-cell-field option.** Verdict 1 of the foundation pull says default to schema/event-segment but support multi-scale with finer place-cell-field-scale resolution where the task demands it. Confirm or revise: does the event-segmentation literature support the finer-scale being a parametric refinement of the same algorithm, or is it a fundamentally different substrate?

**Target papers (~8-12; precision over breadth):**

Core (must include):
- Zacks et al 2007 (Event perception: a mind-brain perspective; prediction-error account of segmentation)
- Baldassano et al 2017 (Discovering event structure in continuous narrative; hierarchical timescale segmentation)
- DuBrow & Davachi 2014 or 2016 (event segmentation and hippocampal contributions to memory)
- Reagh & Ranganath 2018 (event boundaries and hippocampal pattern separation)
- Clewett et al 2020 (LC and event boundaries — couples to MECH-287 broadcast stage)
- Brunec et al 2018 (multivoxel event boundaries) OR Speer et al 2007 (cortical activity at event boundaries)
- Ezzyat & Davachi 2011 (temporal binding within events; the within-event side of the boundary signal)

Algorithm guidance (1-2):
- Adams & MacKay 2007 (Bayesian online change-point detection — substrate algorithm candidate)
- One of: Fox et al 2008 (HDP-HMM segmenters) or Heilbron & Chait 2018 (predictive coding and segmentation)

Already-pulled (re-cite, do NOT re-pull):
- Sols/DuBrow/Davachi 2017 — already in `targeted_review_v_s_foundation/`
- Eichenbaum 2017 — already in `targeted_review_v_s_foundation/`

**Synthesis goal:** Produce `SYNTHESIS.md` with five verdicts answering questions 1-5 above. Each verdict must:
- Give a concrete substrate recommendation (default + any deferred alternatives behind config flags)
- Cite the specific papers that support the recommendation
- Flag failure modes if the substrate commits to the wrong choice
- Note dependencies on other claims (especially MECH-287 coupling per question 3)

The synthesis should be actionable enough that the next session can write `event_segmenter.py` directly from it without re-reading every paper.

**Cross-references in INDEX.md:**
- Link from `targeted_review_v_s_foundation/` (verdict 1 motivates this pull)
- Link to `targeted_review_waking_v_s_invalidation/` (MECH-287 coupling)
- Link to `targeted_review_connectome_mech_269/` (anchor selection downstream)

**MECH-288 claim record:** Already registered as candidate v3_pending in `claims.yaml` at `2026-04-22` registered_utc by the parallel claim-registration stream. The lit-pull updates `lit_confidence` on MECH-288 via the indexer rerun in step 7.
