# Intrinsic-Motivation Mechanisms for Earning Competence — WS-9 Distillation

**Created:** 2026-07-09
**Owner thread:** WS-9 of [`ree_ai_design_critique_plan.md`](ree_ai_design_critique_plan.md) (Tier 2, theory grounding)
**Feeds:** WS-1 (capability floor before structure) and [`goal_pipeline_plan.md`](goal_pipeline_plan.md) (wanting / liking / goal-seeding)
**Status:** lit-pull complete (4 canonical sources); mechanisms ranked; one candidate-claim registration flagged for governance. **PROMOTES NOTHING.**

Literature entries backing this doc live in
[`evidence/literature/targeted_review_intrinsic_motivation_exploration/`](../literature/targeted_review_intrinsic_motivation_exploration/)
(added to the existing directory, not a new one).

---

## Headline finding (the one line for WS-1)

> **REE's entire registered intrinsic-motivation stack is *knowledge-based*. It has *no
> competence-based* intrinsic motivation. WS-1's competence floor — the all-ON agent that
> cannot forage — is the exact symptom Baldassarre & Mirolli predict when you try to earn
> skills with a knowledge-based drive alone.**

Mirolli & Baldassarre (2013) draw the field's load-bearing distinction:

- **Knowledge-based IM** — novelty, surprise, prediction error, learning progress. Rewards
  improving the agent's **world model**. Drives exploration/attention. *REE has all of this*:
  MECH-314 (info-gain), MECH-314a (novelty), MECH-314c (learning progress).
- **Competence-based IM** — reward = **progress in achieving a self-generated goal**. Rewards
  improving the agent's **skills**. Drives autonomous cumulative skill acquisition. *REE has
  none of this registered.* The goal pipeline supplies goal representations but sources
  *wanting* from homeostatic/hedonic value (SD-012, MECH-229), never from competence progress.

Schmidhuber (2010) makes the same concession from the other side: in the compression-progress
theory, skills are acquired only as a *by-product* of seeking compressible data. Curiosity
substrate wired + foraging competence zero is the predicted outcome, not an anomaly.

---

## Source → REE-claim map

| Source | Core mechanism | Nearest REE claim | Direction | Entry |
|---|---|---|---|---|
| Oudeyer & Kaplan 2007 (typology; IAC/R-IAC learning progress) | Reward the **derivative** of predictive error (learning progress); avoids both noisy-TV and blank-wall traps; self-organises a developmental curriculum | **MECH-314c** (namesake) + MECH-314 typology | supports (0.82) | `..._oudeyer2007` |
| Schmidhuber 2010 (formal theory of creativity; compression progress) | Intrinsic reward = bits saved before/after learning; single-scalar objective on one model+controller | MECH-314c (info-theoretic form) | **mixed** (0.70) — single-scalar framing is the design REE's ARC-021/MECH-069 rejects | `..._schmidhuber2010` |
| Mirolli & Baldassarre 2013 (knowledge- vs competence-based IM) | Competence-based IM: reward = **goal-achievement progress**; the mechanism that actually earns skills | **UNREGISTERED** (goal pipeline / drive plane is the host; MECH-307 goal reps) | **mixed** (0.74) — documents an *absence* | `..._baldassarre2013` |
| Bellemare et al. 2016 (count-based / pseudocounts) | **Pseudocount** from a density model generalises count-based novelty to non-tabular states | **MECH-314a** (RL instantiation + estimator) | supports (0.76) | `..._bellemare2016` |

---

## Ranked candidate mechanisms (by fit to current V3 substrate)

Fit = closeness to what REE has already built × leverage on the WS-1 competence floor.
"Plane" tags: **E1** slow/deep world model (`e1_deep.py`), **E2** fast world model
(`e2_fast.py`), **E3** score/action selection, **drive plane** (SD-012 `goal_state.py`),
**goal pipeline** (MECH-307 / SD-049 / MECH-229 wanting-liking).

### 1. Competence-based IM — goal-achievement-progress wanting  ★ highest WS-1 leverage
- **What:** For each active goal in the pipeline, maintain an EMA of the *improvement* in the
  agent's success at reaching it (success rate, or 1 − proximity-at-termination). Inject that
  derivative as an intrinsic **wanting** bonus that biases the agent toward goals it is
  *currently getting better at achieving*. Same derivative discipline as MECH-314c, but the
  operand is **behavioural competence**, not predictive error.
- **Plane / claim:** **goal pipeline + drive plane.** Hosts on MECH-307 goal reps + SD-012
  drive; wanting injection alongside MECH-229 VALENCE_WANTING. **No existing claim** — this is
  the WS-9 → governance registration flag (candidate: *competence-based intrinsic motivation /
  goal-achievement-progress wanting*).
- **Fit:** medium build. Goal representations exist; the missing piece is a per-goal
  competence-progress estimator + its injection point. Directly targets the WS-1 diagnosis
  (missing *drive type*, not just a training bug).
- **Source:** Baldassarre & Mirolli 2013.

### 2. Per-candidate learning-progress bonus — upgrade MECH-314c off the broadcast scalar
- **What:** Replace the current global broadcast scalar (`e3._running_variance` derivative
  applied identically to all K candidates) with a **per-candidate / per-region** learning-
  progress estimate, so exploration concentrates where the model is *currently improving fastest*
  (Oudeyer's zone-of-proximal-development curriculum). This is the upgrade path the MECH-314c
  claim text already anticipates.
- **Plane / claim:** **E2 → E3** (world-model error derivative routed into action selection).
  Claim **MECH-314c** (registered; provisional-adjacent).
- **Fit:** medium build; claim already exists, substrate is Phase-1 present but scalar. Best
  *knowledge-based* driver for competence (learning progress ≈ a proxy for "am I mastering
  this?"), but still knowledge-side — pairs with #1, does not replace it.
- **Source:** Oudeyer & Kaplan 2007; Schmidhuber 2010 (signal grounding).

### 3. Latent-space pseudocount novelty — give MECH-314a a real estimator
- **What:** Fit a sequential **density model** over `z_world` / `z_resource` and derive a
  **pseudocount** novelty bonus, so MECH-314a's rarity signal is computable in the continuous
  latent space instead of a tabular grid. Good for breaking a cold-start exploration deadlock.
- **Plane / claim:** **E1/E2 latent → E3 selection.** Claim **MECH-314a** (provisional).
- **Fit:** low-medium build, but it is a genuine substrate *add* (a latent density model REE
  hasn't built). **Coverage, not competence** — weakest lever for the WS-1 floor; use to
  unstick exploration, not to earn skill. Inherits the noisy-TV trap (level signal, not
  derivative).
- **Source:** Bellemare et al. 2016.

### 4. Compression-progress / info-gain epistemic bonus — MECH-314, epistemic channel only
- **What:** Reward expected reduction in coding cost / uncertainty on the world model. Adopt
  the *signal* for REE's **epistemic channel only** — never as the whole objective (the
  single-scalar framing contradicts ARC-021/MECH-069's three-incommensurable-channels design).
- **Plane / claim:** **E1/E2 + epistemic channel.** Claim **MECH-314** (candidate).
- **Fit:** medium; overlaps #2 conceptually. Lower marginal value than #1–#3 given the
  single-scalar caveat and the existing MECH-314c learning-progress path.
- **Source:** Schmidhuber 2010.

### 5. Intrinsically-motivated goal generation (automatic curriculum / IMGEP)  — V4-leaning
- **What:** A policy that *samples its own goals* and allocates practice by competence progress
  (Oudeyer's IMGEP / automatic curriculum learning). The full developmental-curriculum engine
  #1 and #2 are components of.
- **Plane / claim:** **goal pipeline + hippocampal proposer** (MECH-269 anchor/probe family).
  No single claim; spans the pipeline.
- **Fit:** high build cost; needs a goal-sampling policy and a curriculum allocator. **Defer to
  V4** — right end-state, wrong sequencing for the immediate WS-1 floor.
- **Source:** Oudeyer & Kaplan 2007 (developmental staging); Baldassarre & Mirolli 2013.

---

## Substrate precondition — the wired-but-inert routing (blocks #2–#4)

Any world-model-side IM bonus is **inert until the EMA → E3-selection routing is repaired**.
claims.yaml records this directly: V3-EXQ-590a Goldilocks calibration was *degenerate* — across
novelty_bonus_weight ∈ {0.1…1.0} all arms produced byte-identical coverage/entropy/novelty_ema,
"MECH-111 broadcast novelty does not propagate downstream to alter selection … corroborates the
EXQ-141b finding that the EMA → E3-selection routing is broken." So mechanisms #2, #3, #4 cannot
be *validated* on the current substrate no matter how well specified — the bonus reaches the EMA
but not the committed action. This is the same downstream-of-selection bottleneck the conversion-
ceiling campaign keeps hitting (MECH-439 F-dominance / E3 commit-selection-authority coupling).

**Consequence for sequencing:** the competence-based mechanism (#1) is partly *exempt* from this
trap because it injects into the **wanting/goal** path, not the broadcast-novelty → E3 path — a
further reason it is ranked first for WS-1. But a clean demonstration of *any* of these still
wants the routing fix that the conversion-ceiling line (V3-EXQ-700b and successors) is chasing.

---

## Recommendation to WS-1

1. **Consume V3-EXQ-724** (competence-localization diagnostic, already in flight) before
   building. If 724 localizes the floor to a training-regime / capability gap, that *confirms*
   the Baldassarre & Mirolli reading: the substrate lacks a competence-earning drive.
2. **Register a candidate claim** for competence-based IM (goal-achievement-progress wanting) —
   governance-only edit under an active claim, per WS-2/skill path. This is the single novel
   registration this lit-pull warrants; everything else maps to existing MECH-314 family claims.
3. **Design the WS-1 competence experiment** (via `/queue-experiment`, never hand-edit the queue)
   as a **delta measurement**: a competence-based IM bonus ON vs OFF on the goal pipeline, DV =
   foraging competence crossing the 1.0/ep floor. This is the "can the substrate *earn* the
   capability floor" test, distinct from "does gating help."
4. **Do NOT** lead with pseudocount novelty (#3) or a fresh compression-progress bonus (#4) for
   the competence floor — both are knowledge-based (coverage, not competence) and both are
   blocked by the EMA → E3 routing until that is fixed.

---

## Cross-references

- WS-1 / WS-6 (Bitter Lesson): the learning-progress + competence-based-IM answer is the
  developmental-robotics reply to "structure was specified faster than capability was earned."
- [`goal_pipeline_plan.md`](goal_pipeline_plan.md): mechanism #1 attaches at the MECH-307 /
  SD-012 / MECH-229 wanting site; competence-progress wanting is a *new* wanting operand
  alongside the homeostatic/hedonic ones.
- Existing lit in the same directory: Pathak 2017 (forward-model PE), Burda 2018 (large-scale
  curiosity / noisy-TV), Monosov 2024 (primate curiosity circuits), Oudeyer 2016 (curiosity as
  developmental process) — this pull adds the four canonical *foundations* (Oudeyer & Kaplan
  typology, Schmidhuber compression progress, Baldassarre & Mirolli competence-based IM,
  Bellemare pseudocounts) those entries assumed.
- ARC-021 / MECH-069 (three incommensurable channels): the guardrail that keeps REE from
  adopting Schmidhuber's single-scalar objective wholesale.
