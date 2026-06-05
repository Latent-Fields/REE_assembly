# Thought intake: orienting/surveying drive as pre-approach active sensing

**Date:** 2026-06-04 (raw); intake written 2026-06-05
**Status:** intake / routing hypothesis. NOT an active work item; NOT a change to V3 acceptance
criteria. Becomes actionable only if the 638a/640 result pattern below appears.
**Raw thought file:** `docs/thoughts/2026-06-04_Orienting_surveying_drive.md`
**Origin:** user -- REE-v3 may be missing a primitive orienting/surveying drive: a brief
active-sensing phase between "something matters" (cue recall fires) and "move effectively toward
it" (approach). The organism may "smell something" but not yet turn/scan/sample/localise before
attempting approach.
**Anchors:** SD-057 / MECH-347 (cue recall), MECH-295 (drive->liking->approach), MECH-111
(curiosity/novelty), the live cue-recall thread (V3-EXQ-638a cue-fires-no-contact, 640 post-cue
action diagnostic), cue-ecology intake `thought_intake_2026-06-04_cue_ecology_weaning_nursery_to_forager.md`.

---

## 1. Core idea

A candidate missing control state inserted into the weaning sequence:
`token formation -> cue recall -> wanting -> **orient/survey/sample -> directional gradient
improves** -> approach -> contact`. **Orienting/surveying is distinct from curiosity, cue recall,
and approach** -- it is a pre-approach active-sensing mode entered when a cue/token/need is present
but directional/affordance confidence is too low for reliable approach. Its function: improve
action-relevant information by active sampling (turn/scan, sample gradients, small exploratory arcs,
delay commitment until directional confidence rises).

## 2. Why this matters now (live thread)

638a moved the cue-recall failure downstream: cue fires but contact does not lift. The thought
warns against collapsing that immediately into "cue lacks motivational authority" -- it may instead
mean **cue made the resource meaningful, but the agent lacks an orienting behaviour that converts
meaning into spatial/action information.** This is the V3-conservative reading the 640 diagnostic
(post-cue action/gradient instrumentation) is positioned to discriminate.

## 3. What is new vs what REE already has

| Existing mechanism | Difference from orienting/surveying | Verdict |
|---|---|---|
| MECH-111 curiosity/novelty | Broad info-seeking on moderate surprise; not cue-triggered local sampling | distinct |
| SD-057/MECH-347 cue recall | Retrieves wanting/incentive salience; not active sensing | distinct |
| MECH-295 drive->liking->approach | Converts drive+liking into approach tendency; assumes a vector exists | distinct -- orienting is what FINDS the vector |
| attention/precision selection | Weights content for processing; not motor active-sensing | distinct |

**Verdict: a genuinely distinct candidate mechanism** -- a *cue-triggered, need-gated, pre-approach
active-sensing mode* -- not captured by any existing claim. Currently a routing hypothesis, not yet
a candidate claim, because 640 must first show whether the missing middle is orienting vs raw
cue-to-action authority.

## 4. Candidate claim (gated behind the result pattern)

- **Candidate MECH (pre-approach-orienting-mode)** -- a control state entered when (cue fires AND
  need-relevant AND no high-confidence approach vector AND hazard not vetoing AND need unresolved),
  exited when (gradient confidence rises / vector stabilises / hazard high / cue decays / survey
  budget expires / contact). Metrics: orient_mode_entries_after_cue, survey_steps, heading_entropy,
  gradient_information_gain, cue_fire_to_first_directional_approach, hazard_exposure_during_survey.
  **Register only if 640+ shows: cue fires, no contact, AND no orienting/surveying occurs** (the
  routing table's discriminating row).

## 5. Routing table (from the thought -- the management logic)

| Result pattern | Interpretation | Route |
|---|---|---|
| Cue does not fire | Token/perception/wiring | Re-audit cue formation |
| Cue fires, no contact, no orient/survey | Missing pre-approach active sensing | **This MECH -> orient/survey diagnostic** |
| Cue fires, surveying occurs, no contact | Survey doesn't translate to approach | Diagnose cue-to-action translation |
| Cue fires, contact improves, survival worsens | Cue works but unsafe | Safe-weaning scaffold (cue-ecology intake S8) |
| Cue fires, surveying improves gradients, contact lifts | Orienting was the missing bridge | Promote pre-approach control mode |

## 6. Relation to siblings

Does NOT replace the 638b interoceptive-cue design -- it is a parallel/after branch to the Layer-2
cue-authority question (cue-ecology intake S5-6). Listed in the `non_terminal_need` launch-kit
("orient/survey primitive when action is under-specified"). One member of the live cue-recall
diagnostic family alongside 640 (cue-to-action authority) and the safe-weaning layer.

## 7. Next steps (gated)

1. **Containment** -- do not expand the V3 green-board path; this is a captured hypothesis for
   routing the 638a/640 result. Gate = 640 shows cue-fires-no-contact-no-orienting.
2. If routed in: design an orient/survey diagnostic (measure the section-4 metrics) BEFORE building
   any orienting substrate -- per the snail-race method.
3. Keep distinct from 640's cue-to-action-authority question; do not conflate.

## 8. Cross-references

- Raw: `docs/thoughts/2026-06-04_Orienting_surveying_drive.md`.
- Live thread: `evidence/planning/failure_autopsy_V3-EXQ-638a_2026-06-05.md`,
  `thought_intake_2026-06-04_cue_ecology_weaning_nursery_to_forager.md` (S5-8),
  `thought_intake_2026-06-04_non_terminal_need_launch.md` (launch kit).
- Claims: SD-057, MECH-347, MECH-295, MECH-111.
