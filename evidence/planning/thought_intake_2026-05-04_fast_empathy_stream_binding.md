# Thought intake: fast empathy as developmental stream-binding (not an empathy module)

**Date:** 2026-05-04 (raw); intake written 2026-06-05
**Status:** intake / candidate cluster (NOT yet registered). V4-leaning with one V3-proxy experiment.
**Raw thought file:** `docs/thoughts/2026-05-04_Empathy_development.md`
**Origin:** Wu et al. 2026 (eLife) adolescent repeated-Prisoner's-Dilemma -- adolescents
estimate partner cooperation as well as adults but show weaker *intrinsic reward for
reciprocity*. User reframes: fast empathy is NOT a distinct empathy module / scalar; it is a
social binding + relevance-routing pattern over basic motivational-affective streams that
already exist for the agent's own modelling.
**Anchors:** ARC-010 (fast empathy), MECH-112 (wanting/liking dissociation), SD-011 (dual
nociceptive / suffering stream), MECH-183 / MECH-191 (z_beta leakage + signal legibility for
fast empathy), the affect-primitive register `docs/architecture/affect_primitives.md`, and the
sibling thoughts `2026-04-16_language_lateralisation` / `2026-05-04_Theory_of_mind_v_language`.

---

## 1. Core idea

Fast empathy = ordinary motivational-affective streams (liking, wanting, suffering, threat,
relief, frustration, curiosity, attachment/proximity, fatigue/cost, agency/control, prediction
error) routed across **self -> object -> other** models with relevance to commitment. The
load-bearing dissociation from Wu et al.: **other-model prediction != reciprocity valuation
!= residue-aware social commitment.** Prediction alone is not ethics; the predicted other-state
must become motivationally/ethically relevant to the commitment gate.

## 2. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| Fast empathy exists as a capacity | **Yes** -- ARC-010, MECH-183/191 (legibility prerequisite) | Confirms |
| Wanting/liking are separable affect primitives | **Yes** -- MECH-112, affect_primitives.md three-primitive register | Confirms; this thought extends the register to ~11 streams |
| Suffering as a stream that can be other-bound | **Partial** -- SD-011 dual nociceptive (self harm_a/harm_s); "other-bound suffering = suffering stream + other-model binding" is new framing | **Extension** |
| **Fast empathy = stream-binding, NOT a module/scalar** (architectural prohibition on `empathy_enabled`/`empathy_score`) | **Implied** but never stated as a claim | **NOVEL** -- the central contribution |
| **other-prediction separable from reciprocity-reward** (developmental dissociation) | **No** | **NOVEL** -- and the most testable |
| Developmental ordering: other-bound suffering/threat online BEFORE other-bound liking/wanting (early positive other-reward is destabilising/exploitable) | **No** | **NOVEL** -- safety-relevant ordering claim |
| Open, provisional stream taxonomy (handles not final ontology) | **Partial** -- affect_primitives.md is already a register; this argues it must stay extensible | Sharpening |

**Verdict: genuinely novel decomposition** that extends the affect-primitive register into the
social domain and supplies a falsifiable dissociation. Connects to the object-representation
thread (self/object/other binding) and to the two sibling social/language thoughts.

## 3. Concrete experiment (the reason this is more than theory)

The thought specifies a repeated-cooperation grid-world with four agent variants:
- **A** self-streams only (no stable other-model)
- **B** other-prediction only (predicts partner cooperation; does NOT bind it into affect)
- **C** reciprocity-reward (binds partner cooperation into liking/wanting/trust/shared-goal)
- **D** residue-aware reciprocity (C + residue from exploiting cooperators + repair-goal generation)

Predicted dissociation: B detects but under-reciprocates; C reciprocates more after repeated
cooperation; D additionally shows repair / regret-residue after exploitation. This directly
tests `other_model_prediction != reciprocity_reward != residue_aware_social_commitment`.
**This is a candidate chip/EXQ** (V4-social, or a single-agent-with-scripted-partner V3 proxy)
-- but it needs the social substrate (stable other-model), so gate it behind that.

## 4. Candidate claims

- **ARC (fast-empathy-as-stream-binding)** -- fast empathy emerges from binding/routing basic
  motivational-affective streams across self/object/other; do NOT implement as a module or
  scalar. *[novel; extends ARC-010]*
- **ARC (affect-stream-taxonomy-open)** -- the stream taxonomy is provisional; permit later
  split/merge/rename. *[sharpens affect_primitives.md]*
- **MECH (other-prediction-separable-from-reciprocity-valuation)** -- an agent can predict
  cooperative intent without binding it into commitment-altering value. *[novel; testable via the
  A/B/C/D experiment]*
- **MECH (developmental-reciprocity-gap)** -- the adolescent pattern = dissociation between
  other-cooperation detection and adult-like reciprocity reward. *[lit-anchored: Wu et al. 2026]*
- **Q (delay-positive-other-reward)** -- why might other-bound suffering/threat come online
  before other-bound liking/wanting? (protection vs exploitation-vulnerability). *[open]*

## 5. Affected existing claims / docs

- ARC-010, MECH-112, MECH-183/191, SD-011; `docs/architecture/affect_primitives.md` (the
  register this extends); fast-empathy / social architecture docs.
- Object-representation thread (self/object/other binding) -- the binding layers this needs.
- Cluster siblings: `2026-04-16_language_lateralisation`, `2026-05-04_Theory_of_mind_v_language`.

## 6. Next steps (gated)

1. **Process as a cluster** with the two sibling social/language thoughts (one governance pass).
2. The A/B/C/D cooperation experiment is the standout deliverable -- but it requires a stable
   other-model substrate (V4-social) or a scripted-partner V3 proxy. Do NOT queue until that
   substrate exists; flag as a candidate chip when social work is scheduled.
3. Per memory `feedback_biology_before_formal_definitions`, the suffering/empathy mapping needs
   the social-development lit-pull before registering the developmental-ordering claim.

## 7. Cross-references

- Raw: `docs/thoughts/2026-05-04_Empathy_development.md` (Wu et al. 2026, eLife).
- Claims: ARC-010, MECH-112, SD-011, MECH-183, MECH-191; doc `affect_primitives.md`.
- Memory: `project_object_representation_thread`, `feedback_biology_before_formal_definitions`.
