---
title: State-conditioned exploration (MECH-440 / MECH-441)
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 19
---

# State-conditioned exploration (MECH-440 / MECH-441)

Status: candidate / substrate_ceiling / v3_pending. Registered 2026-06-18 from Convergence
Demand Pipeline row **CDQ-002** (NoisyNet primary + RND/Plan2Explore secondary intakes). Off the V3
critical path -- these block no V3 closure node.

**SUBSTRATE IMPLEMENTED 2026-06-27** (BUILD APPROVED, decision-of-record
`evidence/decisions/cpkt_tonic_exploration_noise_build_decision_2026-06-27.md`; user verdict BUILD
BOTH). Both no-op default / bit-identical OFF, built on top of the same-day landed ARC-110 multi-arena
substrate. **PROMOTES NOTHING** -- MECH-440 / MECH-441 stay `candidate / substrate_ceiling /
v3_pending` until the falsifiers return contributory.
- MECH-440: `ree-v3/ree_core/policy/noisy_selection_head.py` (NoisySelectionHead). Injected in
  `e3_selector.select()` into `_modulatory_accum` (+ the ARC-110 segregated `final`) before the
  committed argmin. Config E3Config.`use_noisy_selection_head` (default False),
  `noisy_selection_sigma_init` (default 0.0 -> exactly-zero output -> bit-identical even ON).
  Falsifier QUEUED on the 569i top-k + MECH-448 demotion stack (loop-seg OFF vs ON arms).
- MECH-441: `ree-v3/ree_core/policy/model_disagreement.py` (ModelDisagreementEnsemble, K-head). Built
  at the agent level; per-candidate cross-head variance -> propagating curiosity bonus via the
  version-layering-guarded `model_disagreement_per_candidate` kwarg. Config E3Config.
  `use_model_disagreement_curiosity` + LatentStackConfig.`n_disagreement_heads` (default 0 -> not
  built). Falsifier **HELD** (blocked_substrate) gated on ARC-110 validation V3-EXQ-707 -- 706b proved
  the curiosity channel works; the single-arena collapse, not the channel, is the binding constraint
  (failure_autopsy_704b-706b-conversion-ceiling_2026-06-27), so a run before ARC-110 is validated would
  re-derive the arena ceiling.
- ARC-106 divergences logged: (1) per-parameter sigma is one level below biology's systems-level
  tonic/phasic LC-NE mode gate; (2) sigma self-anneals via REE's LOCAL confidence EMA, not NoisyNet's
  RL gradient (REE does not backprop through E3 selection).
- Implementation record: `ree-v3/CLAUDE.md` "MECH-440 / MECH-441: state-conditioned exploration".

## The gap

`behavioral_diversity_isolation:GAP-C` and `arc_062_rule_apprehension:GAP-H` both name a missing
mechanism: a **tonic, state-conditioned exploration noise floor (MECH-313 LC-NE analog) -- distinct
from a fixed epsilon schedule**. The necessity is established by ARC-065 (the
behavioural-diversity-generation pathway). The mechanism is not: MECH-313 as registered is
explicitly a **state-INDEPENDENT** post-softmax max-entropy/temperature floor, and the GAP-C
falsifier **V3-EXQ-687** self-routed `substrate_not_ready_requeue` because that floor was
**non-propagating** -- the temperature was invisible to the argmax/committed action
(`selected_action_entropy = 0.0`, the `r1a_entropy_only_artefact`;
`failure_autopsy_V3-EXQ-687_2026-06-18`).

## MECH-440 -- state-conditioned, self-annealing, propagating noise floor (NoisyNet analog)

The LC-NE tonic floor should be injected as **learned per-parameter (factorised-Gaussian) weight
noise** in the E3 selection pathway (`w = mu + sigma (x) epsilon`, `sigma` gradient-trained), so it:

1. **propagates** into the committed action -- it changes which action is argmax, not a discarded
   pre-commit temperature (fixes the V3-EXQ-687 non-propagation);
2. is **state-conditioned** by construction -- weight noise x state-dependent activations;
3. **self-anneals** -- learned per-parameter `sigma` falls where the policy is confident, stays up
   where exploration pays, so the floor does not wash out committed-action diversity uniformly.

**Biology (lit-pull before registration).** The LC-NE tonic exploration signal is itself
state/uncertainty-conditioned and annealed by controllability: Aston-Jones & Cohen 2005 adaptive-gain
theory ([DOI](https://doi.org/10.1146/annurev.neuro.28.061604.135709)) and Tervo et al. 2014 Cell
([DOI](https://doi.org/10.1016/j.cell.2014.08.037), LC->ACC gating of stochastic choice under
uncertainty). So MECH-313's state-independent framing is biologically under-specified; the NoisyNet
refinement is the biologically-correct shape.

**Locus / adapter.** The MECH-313 `use_noise_floor` / `noise_floor` lever in `e3_selector` /
`select_action`; replace/augment the post-softmax temperature with selection-head parametric weight
noise. No-op default (`sigma_init=0` / flag OFF = bit-identical), per the V3-primacy version-layering
doctrine.

**Falsifier.** Selection-head weight noise yields committed (argmax) `selected_action_entropy`
strictly above a matched-pre-commit-variance temperature control (the 687 non-propagating arm) on
>= 2/3 seeds, non-degenerate. Refuted if it washes out at argmax (reproduces the
`r1a_entropy_only_artefact`) or raises pre-commit entropy without raising committed diversity
(thrash, not carve).

## MECH-441 -- model-disagreement directed curiosity (RND / Plan2Explore analog)

The complementary directed-curiosity leg (ARC-065 substrate (b)): a **per-candidate, self-annealing**
intrinsic signal from **E2 forward-model disagreement** (ensemble / dropout-variance proxy), fed into
E3 selection so it propagates per-candidate -- unlike the broadcast-novelty EMA channel found
non-propagating (V3-EXQ-590a / 141b). Maps to MECH-314c learning-progress / MECH-314b uncertainty-driven
curiosity. The Q-044/MECH-314 leg of GAP-H is already satisfied (V3-EXQ-604c); MECH-441 refines the
curiosity *mechanism*, it does not reopen that leg.

**Biology.** Daw et al. 2006 Nature ([DOI](https://doi.org/10.1038/nature04766)) -- frontopolar
cortex preferentially active during exploratory decisions, a dedicated directed-exploration substrate.

**Falsifier.** A per-candidate self-annealing disagreement bonus raises committed-action diversity
above a matched-magnitude constant-bonus control on >= 2/3 seeds with supra-floor cross-candidate
range. Refuted if cross-candidate flat (degenerate) or non-propagating.

## Relationship to the existing cluster

- Extends MECH-313 (440) and MECH-314 (441) via `depends_on`; both also `depends_on` ARC-065.
- Distinct from the conversion-ceiling F-dominance claim (MECH-439): F-dominance is a
  selection-VARIANCE problem at the primary score; MECH-440/441 are about the diversity-GENERATION
  channels (tonic floor + curiosity) reaching the committed action at all. A propagating floor that
  still loses to F-share would point back at MECH-439's rebalance lever.
- Convergence intake: `REE_convergence/sources/noisynet/`, `REE_convergence/sources/rnd-plan2explore/`,
  `reports/2026-06-18_tonic_exploration_noise_synthesis.md`; packet
  `CPKT-TONIC-EXPLORATION-NOISE-20260618`.
