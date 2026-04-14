---
title: Roadmap
nav_order: 6
---

# Roadmap

**Claim Type:** implementation_note
**Scope:** Program phases, repository roles, and phase-gate criteria
**Depends On:** IMPL-020, IMPL-021, IMPL-022, MECH-057, MECH-058, MECH-059, MECH-060
**Status:** candidate
**Claim ID:** IMPL-008
<a id="impl-008"></a>

---

## Status Snapshot (2026-04-14)

- **Key governance outcome: SD-013 promoted candidate->provisional (2026-04-13b governance).** conf=0.788, 5 supports/1 weakens. SD-013 (interventional training bias) now provisional. 7 experiments reclassified non_contributory.
- **New claim class registered: EXT-001 through EXT-007.** External AI/LLM failure mode catalogue with REE mechanism mappings (sycophancy, hallucination, reward hacking, goal misgeneralization, causal attribution gap, other-model collapse, context amnesia). claims.yaml: 454 claims total.
- **MECH-231 registered** (E2 short-horizon discriminative pair, cowork-2026-04-13-e). EXQ-407 queued.
- **EXQ-406 queued** (INV-053 depression attractor replication, 5-seed LONG_HORIZON characterisation, ~240 min).
- **~481 experiments completed.** 96 PASS, 235 FAIL, 51 ERROR, 99 UNKNOWN.
- **2 pending review** (as of 2026-04-14T04:18:29Z): v3_exq_326_wanting_gradient_nav_fix FAIL (MECH-216/SD-012/SD-015); V3-EXQ-326 UNKNOWN.
- **Current bottleneck: first-paper gate.** Active queue (17 items): EXQ-326, EXQ-332, EXQ-330a, EXQ-353, EXQ-322a, EXQ-328a, EXQ-321a, EXQ-325a, EXQ-365, EXQ-355, EXQ-395, EXQ-375, EXQ-385, EXQ-328b, EXQ-326a, EXQ-406 (INV-053 depression attractor), EXQ-407 (MECH-231 E2 short-horizon).

---

## Status Snapshot (2026-04-13)

- **Key governance outcome: EXQ-354 PASS (2026-04-13).** MECH-112 behavioral wanting/liking
  dissociation confirmed with SD-015 wiring (3/3 seeds). MECH-112 split into MECH-229
  (behavioral wanting/liking dissociation, active) and MECH-230 (latent z_goal structure,
  candidate). 7 dry-run FAILs from earlier sessions reclassified as non_contributory. SD-012
  design doc updated to IMPLEMENTED.
- **Five new experiments queued (2026-04-13):** V3-EXQ-355 (ARC-038 schema assimilation),
  V3-EXQ-365 (MECH-104 surprise gate, 5-seed), V3-EXQ-375 (MECH-073 valence geometry),
  V3-EXQ-385 (INV-049 offline consolidation necessity / sleep ablation), V3-EXQ-395
  (MECH-220 harm hub behavioral probe). Plus EXQ-328b (MECH-230 full run) and EXQ-326a
  (SD-015 + MECH-229 nav fix).
- **SDs moved pending->implemented since last snapshot:** SD-013 (interventional training),
  SD-015 (ResourceEncoder), SD-017 (minimal sleep infrastructure), SD-018 (resource proximity
  supervision), SD-019 (affective nonredundancy constraint), SD-020 (affective harm surprise PE),
  SD-021 (descending pain modulation), SD-022 (directional limb damage), SD-023 (environmental
  gradient texture). Also: ARC-033, MECH-090 bistable gate, MECH-120 SHY wiring, MECH-203/204
  serotonin substrate, MECH-205 surprise-gated replay fix, MECH-216 E1 predictive wanting.
- **481 experiments completed.** 96 PASS, 235 FAIL, 51 ERROR, 99 UNKNOWN.
- **0 pending review** (as of 2026-04-13T07:19:18Z).
- **Current bottleneck: first-paper gate.** Active queue (16 items): EXQ-327 (MECH-163
  goal-conditioned nav paper gate), EXQ-326a (SD-015 + MECH-229 nav fix), EXQ-353 (ARC-033/
  SD-003/SD-013 interventional vs observational counterfactual), EXQ-321a (MECH-090 bistable
  gate retest), EXQ-325a (SD-021 descending modulation retest), EXQ-365 (MECH-104 surprise
  gate), EXQ-355 (ARC-038), EXQ-395 (MECH-220), EXQ-375 (MECH-073), EXQ-385 (INV-049 sleep
  ablation), and fix iterations EXQ-322a/328a/330a/332/328b/326a.

---

## Status Snapshot (2026-04-06)

- **SD-011/SD-012 Full E3 Integration (2026-04-05).** z_harm_a now flows through the complete
  agent loop: agent.sense() -> LatentStack.encode() -> E3.select(). New E3Config parameters:
  urgency_weight (z_harm_a.norm() lowers commit threshold, D2 avoidance escape, capped by
  urgency_max=0.5) and affective_harm_scale (amplifies lambda_ethical by accumulated threat).
  E3.compute_harm_forward_cost() replaces deprecated HarmBridge path, rolling z_harm_s step-by-step
  through trajectory actions via ResidualHarmForward. Agent.compute_drive_level(obs_body) added
  as canonical SD-012 static method. All new parameters default to 0.0/None for full backward
  compatibility.
- **EXQ-247 queued:** 4-arm ablation validating full SD-011/SD-012 E3 integration. Tests
  urgency_weight and affective_harm_scale jointly with drive_weight across ablation conditions
  (FULL vs NO_URGENCY vs NO_AFFECT vs BASELINE). 3 seeds x 200 train + 50 eval x 200 steps.
- **New claims registered (2026-04-06 thought-intake sessions):** INV-049 (Offline Update
  Necessity Principle -- offline phases are a mathematical necessity for model-building agents),
  INV-050 (three-drive sleep regulation), INV-051 (optimal novelty range), MECH-178
  (noradrenergic REM suppression pathway), MECH-179 (MEL type-specificity), MECH-180
  (novelty-driven adaptive sleep), MECH-181 (cognitive reserve as update-loop maintenance),
  Q-033 (actigraphy MEL forecasting).
- **~198 experiments run.** 51 PASS, 123 FAIL, 22 ERROR, 2 UNKNOWN. 22 experiments
  currently queued (EXQ-223 through EXQ-247 series plus EWIN-PC onboarding smoke).
- **0 pending review** (as of 2026-04-04T18:45:00Z).
- **Current bottleneck: first-paper gate.** Active queue: EXQ-074e/234 (wanting/liking),
  EXQ-076e/235 (goal conditioning), EXQ-195 (SD-003 z_harm_s counterfactual), EXQ-247
  (SD-011/012 full integration), and sleep-architecture experiments (EXQ-242--246).

---

## Status Snapshot (2026-04-04)

- **SD-014 implemented (2026-04-04): hippocampal valence vector node recording.** 4-component
  valence vector V=[wanting, liking, harm_discriminative, surprise] added to RBFLayer and
  ResidueField (ree_core/residue/field.py). Each RBF center stores a valence_vecs buffer
  [num_centers, 4] updated incrementally per visit. MECH-094 gate applies: hypothesis_tag=True
  blocks valence updates. Prerequisite for ARC-036 and replay prioritisation via drive state.
- **ARC-028 + MECH-105 implemented (2026-04-04): hippocampal-BetaGate completion coupling.**
  HippocampalModule.compute_completion_signal() maps best trajectory score to a sigmoid
  dopamine-analog value. BetaGate.receive_hippocampal_completion() releases beta when signal
  >= threshold (0.75). Implements the Lisman & Grace 2005 subiculum->NAc->VP->VTA loop.
- **~292 experiment scripts authored.** EXQ-001 through EXQ-223 series. 0 pending review
  as of 2026-04-03 (all discussed). EXQ-125 currently running on DLAPTOP-4.local (ARC-029).
- **Governance clean.** 0 pending review items (generated 2026-04-03T21:39:23Z).
  Last governance cycle: 2026-04-03 (cowork-2026-04-03-b, 14 experiments reviewed;
  ARC-022 promoted to provisional).
- **Current bottleneck: first-paper gate experiments.** EXQ-223 PASS confirmed the minimal
  E1+E2+hippocampus core loop. Active queue: EXQ-074e (MECH-112/117 wanting/liking),
  EXQ-076e (MECH-116 E1 goal conditioning), EXQ-195 (SD-003 z_harm_s counterfactual),
  EXQ-125 (ARC-029 committed mode, running). SD-015 resource indicator in progress.

---

## Status Snapshot (2026-04-03)

- **EXQ-223 PASS: Minimal mind confirmed (2026-04-03).** The REE core loop —
  E1 (associative world model) + E2 (fast transition model) + HippocampalModule
  (trajectory proposal) + multinomial go/no-go + raw harm/reward signals — is sufficient
  for stable navigation, harm avoidance, and resource acquisition. 3/3 criteria met across
  all 3 seeds (harm_ratio 0.29–0.39; REE takes ~4.5× as much reward as random). The
  ablation strips the deliberative architecture entirely: commitment_threshold=−1.0 (always
  uncommitted), z_goal disabled, benefit_eval disabled. What remains is the predictive
  associative core alone — and it works. This is the first experimental confirmation that
  the E1+E2+hippocampus triad constitutes a minimal functional mind. **The circuit topology
  is a named-structure match to the zebrafish larva (5–7 dpf)**: dorsal pallium (E1) →
  cerebellum (E2) → lateral pallium (hippocampal module) → optic tectum + reticulospinal
  neurons (go/no-go) → lateral habenula (harm signal). The larva has no mature prefrontal
  cortex — no commitment architecture — matching the ablation exactly. It is the only
  vertebrate whose entire ~100,000-neuron CNS has been functionally imaged during free
  behaviour (Ahrens et al., 2013, *Nature Methods*; Portugues et al., 2014, *Neuron*).
  This match was derived from functional-architecture arguments, not from biology.
  Episode visualiser (`episode_viewer.html`) added to the explorer for trajectory playback.
  Full circuit table and references: see changelog 2026-04-03.
- **SD-011 and SD-012 both implemented.** SD-011 (dual nociceptive streams: z_harm_s +
  z_harm_a) validated at EXQ-178b PASS (2026-03-30). SD-012 (homeostatic drive modulation)
  implemented 2026-04-02: drive_weight default raised from 0.0 to 2.0, enabling
  effective_benefit = benefit_exposure * (1.0 + drive_weight * drive_level). Step 3.1
  substrate debt now substantially resolved (SD-008/009/010/011/012 all done).
- **~198 experiments run.** EXQ-001 through EXQ-212+ series. 51 PASS, 123 FAIL, 22 ERROR
  as of 2026-04-03. Breadth of FAIL reflects aggressive experimentation on a developing
  substrate -- each FAIL cluster was analyzed and resolved before the next iteration.
- **Breath oscillator and z_beta pathway wired (2026-04-02).** BreathOscillator integrated
  into core commitment decision (MECH-108). rv -> z_beta volatility pathway wired for Q-007.
  14 substrate-limited experiments marked scoring_excluded. EXQ-199--203 queued to re-run
  MECH-025/Q-007/MECH-029/MECH-026/MECH-057a on corrected substrate.
- **ARC-033 ResidualHarmForward promoted to ree_core (2026-04-02).** E2_harm_s forward model
  now in `ree_core/latent/stack.py`, enabling EXQ-195 (SD-003 z_harm_s counterfactual).
  EXQ-195 queued; this is the critical SD-003 re-validation step on the new harm pipeline.
- **Governance cycle active.** 36 experiments pending review (2026-04-03). PASS cluster
  includes SD-011 validation (EXQ-178b), terrain work (SD-015), and several MECH-1xx claims;
  FAIL cluster being classified (evidence vs diagnostic). Governance session in progress.
- **Current bottleneck: first-paper gate experiments.** SD-011/012 substrates cleared; next
  priority is EXQ-074e (MECH-112/117 wanting/liking), EXQ-076e (MECH-116 E1 goal
  conditioning), EXQ-195 (SD-003 z_harm_s counterfactual), and EXQ-182a (oracle ceiling
  for habit-system goal lift).

---

## Status Snapshot (2026-03-31)

- **V3 first-paper gate clarified.** `ree-v3` completion for the first paper is now
  explicitly scoped to the **waking, single-agent substrate**. Sleep, social extension,
  language/communication, nth-order ethics, and full psychiatric modelling are **not**
  blockers for V3 completion.
- **Immediate focus is the approach/goal side.** Harm/attribution substrate has advanced
  materially (SD-003 architecture, SD-005, SD-010, SD-011, ARC-033), but the main remaining
  V3 risk is still positive attractor behavior rather than harm avoidance.
- **Hard V3 completion gates for paper 1:** (1) post-SD-011 SD-003 works on `z_harm_s`,
  not only the legacy `z_world` form; (2) harm/attribution substrate is stable enough to
  treat as platform rather than ongoing rescue work; (3) SD-012 + MECH-112 yield genuine
  behavioral goal lift, not only `z_goal` activation; (4) ARC-030 is demonstrated as
  dual evaluation of the same trajectories by harm and goal channels inside one selector;
  (5) matched-seed reruns and at least one task variant confirm robustness; (6) governance
  state remains clean enough that review/index/claim status are aligned.
- **First-paper claim remains narrow.** Target claim is: REE architectural separation yields
  attributable, harm-avoiding, goal-directed agency in a waking single-agent substrate.
- **Deferred to V4/V5:** consolidation/sleep mechanisms, integrated self/other modelling,
  structured communication, and emergent ethical behavior in multi-agent settings.
  *(Note 2026-04-02:* The V4 deferral of social work reflects a precise architectural
  constraint: INV-043 establishes that testing whether ethical capacity is
  *developmentally activated* — not merely architecturally present — requires a
  multi-agent substrate with modelled caregiving. V3 tests the machinery (ARC-043
  Layer 6); INV-043 testing requires Layers 2-4 to be exercised socially.
  See `docs/architecture/developmental_curriculum.md#inv-043`.*)*

---

## Status Snapshot (2026-03-26)

- **V2 complete.** Series closed after EXQ-028 (2026-03-19). Governance cycle applied 7
  decisions, V3-pending gate lifted.
- **V3 active.** ~96 experiments run (through EXQ-096a). SDs 004–010 implemented.
  SD-010 (harm stream separation) unblocked the prior FAIL cluster: EXQ-056c/058b/059c all PASS.
- **SD-011 is the current bottleneck.** Dual nociceptive streams (z_harm_s + z_harm_a) are
  required for the SD-003 counterfactual redesign. EXQ-093/094 confirmed that
  `HarmBridge(z_world → z_harm)` has bridge_r2=0 (architectural impossibility by SD-010 design).
  ~10 experiments are blocked pending SD-011. Design doc: `sd_011_dual_nociceptive_streams.md`.
- **SD-012 registered.** Homeostatic drive modulation for z_goal seeding — required for
  EXQ-085+ (wanting/liking experiments) and for any goal-directed behavior validation.
  Design doc: `sd_012_homeostatic_drive.md`.
- **New claims registered (2026-03-24/25):** INV-032–038 (approach/avoidance symmetry,
  epistemic self-monitoring, goal maintenance, state definition, stored/active distinction,
  EVR pattern). ARC-030–035. SD-011/012. MECH-112–134.
- **Currently queued:** EXQ-074b (MECH-112/117 wanting/liking, supersedes EXQ-074) and
  EXQ-076b (MECH-116/ARC-032 goal conditioning, supersedes EXQ-076).
- **MECH-124 diagnostic:** When reviewing EXQ-074b/076b results, check whether z_goal
  salience is competitive with harm salience — if not, this is a V4 early risk indicator
  (consolidation-mediated option-space contraction).
- **0 pending review** as of 2026-03-25 (all experiments discussed and marked in
  review_tracker.json).
- **Phase gate:** SD-011 implementation → re-run blocked experiments → governance cycle.
- **Step 3.1 (Substrate Debt Resolution)** is the current active step; SD-008/009/010 are
  done; SD-011/012 remain.

---

## Status Snapshot (2026-03-20) — archived

- **V2 complete.** All three hard-stop criteria triggered after EXQ-028. Governance cycle
  run 2026-03-19: 7 decisions applied, V3-pending gate lifted, ARC-024 and SD-010
  registered.
- **V3 active.** 73 experiments run (through EXQ-059). Substrate SDs 004/005/006/007
  implemented. EXQ-030b PASS validated V3-form SD-003 attribution pipeline
  (attribution_gap=0.035, world_forward_r2=0.947). Current focus: SD-010 implementation
  (harm stream separation) to unblock ~10 pending FAILs.
- **Q-020 adjudicated:** ARC-007 strict (2026-03-16). HippocampalModule generates
  value-flat proposals; terrain sensitivity is a consequence of navigating
  residue-shaped z_world, not a separate hippocampal value signal.
- **17 pending FAILs** awaiting review (generated 2026-03-20). Root cause cluster:
  fused z_world containing harm signal → SD-010 substrate debt.
- `REE_assembly` is the canonical governance + specification repo. Current V3 roadmap
  is in §REE-v3 below; `v2_v3_transition_roadmap.md` is now historical.

---

## Status Snapshot (2026-02-28) — archived

- `REE_assembly` is the canonical governance + specification repo.
- `ree-v1-minimal` has served as the qualification harness: 8 genuine experiments
  completed (EXQ-000 through EXQ-007), 4 PASS, 4 informative FAIL (substrate-limited).
- Substrate debt items SD-001, SD-002, SD-003 registered. V1 has reached saturation
  for the claims it was designed to test. Further V1 runs (EXQ-008/009) complete the
  current evidence cycle; extended-seed reruns (EXQ-010–013) are low-priority confidence
  accumulation.
- V2 cutover gates passed 2026-02-18 but cutover was deferred. Correct decision: V2
  specification needs redesigning (Step 2.0, below) before implementation begins.
- JEPA integration guidance remains convergence-first: source-method details live in
  `REE_convergence`; `REE_assembly` keeps REE-first canonical contracts and adjudication
  outputs.

---

## Roadmap Discipline

**Each step must be completed in sequence. Before starting the next step:**

1. Record what was learned (update GOVERNANCE_STATE.md, substrate debt register, any
   affected claims).
2. Update this roadmap to reflect that learning — revise subsequent steps if the
   evidence changes what they should be.
3. Make the update-roadmap action explicit in the exit criteria of every step.

The roadmap is not a fixed plan; it is a living document that is deliberately updated at
each step boundary. Steps may be added, split, or reordered as understanding grows.

## V3 Completion Gate For First Paper (2026-03-31 clarification)

This section records the current planning boundary for when `ree-v3` should be considered
"complete enough" for the first real paper.

**Paper-1 target claim**

REE should support a narrow, defensible claim:

- A waking, single-agent REE substrate can learn stable self/world attribution, harm avoidance,
  and genuine goal-directed behavior from architectural separation rather than a monolithic
  reward objective.

**Must-pass gates**

- **Post-SD-011 SD-003 works in the current architecture.** Counterfactual attribution must
  succeed on the sensory-discriminative harm stream (`z_harm_s`), not only on the older
  `z_world` formulation.
- **Harm/attribution substrate is stable.** SD-005, SD-010, SD-011, and ARC-033 must be
  reliable enough to function as substrate rather than as active rescue work.
- **Goal-directed behavior is behaviorally real.** SD-012 and MECH-112 must produce a genuine
  GOAL_PRESENT vs GOAL_ABSENT behavioral lift, not just `z_goal` seeding.
- **Approach and avoidance compete in one selector.** ARC-030 must be demonstrated as dual
  evaluation of the same candidate trajectories by harm and goal channels inside a shared
  commitment process.
- **Results survive reruns.** Matched-seed reruns and at least one task variant must confirm
  the core behavior is not a one-task artifact.
- **Governance state is clean.** Review tracking, claim status, and experiment indexing must
  remain aligned enough for the evidence story to be legible to an external reader.

**Two-tier V3 completion (2026-04-02 clarification)**

V3 completion has two levels with distinct gates:

*V3 first-paper gate* (sufficient for Paper 1 claim):
- Habit-system goal-directed behavior demonstrated: SD-012 activates approach drive;
  EXQ-182a oracle confirms the environment is near-optimal for habit-level policy;
  goal-lift experiment (EXQ-074e successor) shows GOAL_PRESENT > GOAL_ABSENT behavioral
  lift with ARC-030 harm/goal competition in one selector.

*V3 full completion gate* (required before V4 entry):
- **HippocampalModule multi-step trajectory planning validated.** This is a V4
  prerequisite, not merely a V4 feature. V4's social extension ("sharing joys and
  sorrows", INV-029 benefit gradient) requires planning trajectories that affect
  another agent's z_harm_a accumulation and benefit_exposure over time. One-step
  greedy cannot reach this: it can approach its own resources but cannot plan paths
  that sustain another's joy or reduce another's sorrow over multi-step trajectories.
  The VTA/hippocampal system (MECH-163) must be validated in V3 to provide the
  planning substrate that V4 social cognition will depend on.
- All V3 first-paper gates passed.

See MECH-163 (dual goal-directed systems: habit vs hippocampally-planned).

**Explicit non-blockers for V3 *first-paper* completion**

- Sleep/offline consolidation mechanisms.
- Integrated self/other social modelling.
- Full language integration; simple future communication primitives are enough.
- nth-order multi-agent ethics tests.
- Full computational-psychiatry coverage.

**Deferred to V4/V5 / later papers** *(requires V3 full completion gates first)*

- Sleep-like consolidation as a load-bearing mechanism.
- Social coupling and other-modelling inside core substrate — **specifically requires
  hippocampal multi-step planning (MECH-163 VTA/planned system) from V3 full gate**.
- Structured communication between agents.
- Emergent ethical behavior in multi-agent settings.
- Stronger psychiatric modelling beyond single-agent perturbation analogs.
- **INV-043 (caregiver requirement)** — requires multi-agent substrate with modelled
  caregiving. V3 cannot test whether ethical capacity is *motivationally activated*
  (vs merely architecturally present). This is a first-class V4 research question.
- **MECH-158 (love-exclusion failure mode)** — requires developmental multi-agent
  substrate to test whether absence of love-experience collapses ethical motivation.
- **MECH-159 (intergenerational moral progress)** — requires multi-generation agent
  infrastructure. V5 scope or later.

*The distinction between V3 and V4 is not only scope but epistemological level:
V3 tests whether the machinery works. V4 tests whether the machinery develops correctly.
The ARC-043 stack makes this precise: V3 exercises Layers 6-9; V4 must exercise Layers
2-5 dynamically, with caregiving, developmental phases, and social residue.*

---

## Phase Definitions

### REE-v1 ✓ (completed purpose: qualification baseline)

**Primary role:** validate whether proposed mechanisms produce expected directional
effects under controlled conditions.

**Outcome:** useful for signal discovery and contract hardening. Not sufficient as final
architecture target due to stress-lane conflicts, limited environment breadth, and
accumulated substrate debt (SD-001, SD-002, SD-003). Four genuine PASSes confirm core
signal structure; four informative FAILs confirm substrate resolution limits, not
architecture failures.

**Post-V1 learning incorporated into roadmap:**
- E2/hippocampus conflation (SD-001) prevents clean mechanistic isolation
- E1/E2 mutual constitution (SD-002) reframes timescale-separation interpretation
- E2 self-attribution substrate (SD-003) is an unmet V2 design requirement
- V1 stateless grid cannot surface persistent agent causal footprint
- MECH-057 (control completion) requires multi-step environment with genuine commitment
  pressure; needs richer substrate before further testing

---

### REE-v2 ✓ (completed purpose: V2 qualification)

**V2 series closed after EXQ-028 (2026-03-19).** All three hard-stop criteria met.
Governance cycle completed 2026-03-19.

#### Step 2.0 — V2 Redesign ✓

**Primary role:** Produce an updated V2 specification that incorporates V1 learning.
The original V2 spec (representation-interface contract) remains in scope, but the
design must now account for SD-001/002/003 and explicitly address what V2 must deliver
to make future self-attribution and self-modelling experiments possible.

**In-scope:**
- Redesign V2 architecture to resolve SD-001: E2 separated as pure transition MLP,
  HippocampalModule created as distinct component of E3 complex
- Revise V2 entry criteria to include SD-003 requirements (see below)
- Produce first-pass V2 implementation spec: subsystem boundaries, required metrics,
  failure gates
- Define the persistent-causal-footprint environment requirement (SD-003)
- Capture mutual constitution (SD-002) in architecture documents

**Out-of-scope:**
- Implementation (code changes happen in Step 2.1 onward)
- New V1 experiments beyond EXQ-008/009

**Exit criteria:**
- Updated V2 implementation spec document exists with SD-001/002/003 addressed
- V2 entry criteria revised (see below)
- This roadmap updated with Step 2.1–2.5 refined based on redesign output
- GOVERNANCE_STATE.md SD-003 entry complete ✓ (done 2026-02-28)

**Outcome:** ✓ Complete. V2 spec produced (`docs/architecture/ree_v2_spec.md`). SD-001/002/003
addressed in design. Steps 2.1–2.5 scoped.

---

#### Step 2.1 — E2 Separation (SD-001 resolution) ✓

**Primary role:** Refactor E2 into a pure fast transition model. Create HippocampalModule
as a distinct component of the E3 complex. Close SD-001.

**In-scope:**
- `E2FastPredictor` → pure forward predictor: `forward(z, a) → z_next` (cerebellum-like)
- `HippocampalModule` (new) → trajectory proposal by navigating affective terrain; not
  by running transition predictions
- Counterfactual E2 querying made architecturally possible: `e2.forward(z, a_cf)`
- SD-001 closed in GOVERNANCE_STATE.md

**Out-of-scope:**
- Full E3 complex redesign (Step 2.2+)
- Self-attribution experiments (Step 2.4)

**Exit criteria:**
- E2 callable independently with arbitrary action input
- HippocampalModule exists as separate class
- Existing EXQ PASS results replicated on refactored substrate (parity check)
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. E2 is a pure fast transition MLP on z_self. HippocampalModule
created as distinct E3 component. SD-001 closed.

---

#### Step 2.2 — Representation Interface Contract ✓

**Primary role:** Lock stable representation-interface contract for sensing adapters
and E1/E2 latent prediction. This is the original primary V2 role, now sequenced after
E2 separation.

**In-scope:**
- Sensor adapters mapped to JEPA-like context/target latent interfaces
- E1/E2 representation-reference integration contract (`IMPL-022`)
- Stable output streams for latent prediction error and uncertainty
- Run-pack/adapter-signal compliance and calibration metrics

**Out-of-scope:**
- Full control-plane completion
- Hippocampal/E3 commitment architecture
- Full ethical arbitration dynamics

**Exit criteria:**
- Representation-interface contract stable across qualification and stress lanes
- Uncertainty/error streams calibrated and non-gamed across distribution shifts
- No unresolved adapter contract drift
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. MECH-059 PASS confirmed E1 precision and E3 confidence are
structurally independent. Representation interface stable.

---

#### Step 2.3 — Persistent Causal Environment ✓

**Primary role:** Upgrade the environment substrate so that persistent agent causal
footprint is present — actions at step N affect the landscape at step N+k in ways
that require disambiguation from independent environment change. This is the
prerequisite for SD-003 experiments.

**In-scope:**
- Environment design where agent-caused and environment-caused transitions are
  structurally distinct and must be separated for correct attribution
- Validation that E2 (now pure transition model from Step 2.1) can be queried
  counterfactually against this environment

**Out-of-scope:**
- Full self-attribution claim testing (Step 2.4)

**Exit criteria:**
- Environment exists with persistent agent causal footprint
- Baseline experiments confirm agent-caused / environment-caused distinguishability
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. CausalGridWorld implemented with persistent agent causal
footprint. EXQ-018 PASS confirmed agent-caused/environment-caused distinguishability.

---

#### Step 2.4 — Self-Attribution Substrate ✓ (V2 partial; V3 form validated)

**Primary role:** Implement and test counterfactual E2 querying for self-modelling.
First genuine experiments on self-attribution claims. Close SD-003.

**In-scope:**
- Counterfactual E2 queries integrated into agent decision loop
- First genuine experiments isolating agent-caused vs environment-caused harm
- Self-attribution claim coverage (claims to be identified during Step 2.0 redesign)
- SD-003 closed in GOVERNANCE_STATE.md

**Exit criteria:**
- At least one genuine PASS on a self-attribution claim
- E2 counterfactual querying demonstrated experimentally
- Roadmap updated with any discoveries

**Outcome:** ✓ Partial / hard stop. EXQ-027 FAIL triggered V2 hard stop: E2 cannot
discriminate agent-caused harm in z_gamma; SD-005 substrate required. V2
self-attribution experiments concluded. V3-form SD-003 validated at EXQ-030b PASS
(2026-03-18): attribution_gap=0.035, world_forward_r2=0.947. Full SD-003 achieved on
V3 substrate with z_world separation.

---

#### Step 2.5 — V2 Qualification ✓

**Primary role:** Genuine experiment coverage across core V2 claims. Sufficient evidence
to make V3 entry decision.

**Exit criteria:**
- Representation interface stable across qualification and stress lanes (from Step 2.2)
- Self-attribution substrate tested (from Step 2.4)
- Governance confidence above provisional thresholds for core V2 claims
- **Roadmap updated with V1+V2 learnings before V3 begins**
- V3 entry decision made explicitly

**Outcome:** ✓ Complete. V2 series closed after EXQ-028. 15 genuine V2 experiments
(EXQ-014–028): 5 structural-separation PASSes, 9 FAILs (all substrate-limited by
z_gamma conflation or SD-004 absence). Governance cycle 2026-03-19: 7 decisions
applied. V3 entry formally made.

---

### REE-v3 ← **current phase** (control completion + full attribution)

**Primary role:** Implement full attribution pipeline, control-plane heartbeat architecture,
and E3 commitment/accountability on the z_self/z_world split substrate (SD-004/005).

#### Step 3.0 — V3 Substrate Implementation ✓

SD-004 (E2 action objects; HippocampalModule navigates action-object space O), SD-005
(z_gamma → z_self + z_world split), SD-006 (asynchronous multi-rate heartbeat,
time-multiplexed phase 1), SD-007 (ReafferencePredictor for perspective-corrected
z_world). Q-020 adjudicated: ARC-007 strict (2026-03-16). CausalGridWorld extended
to V3 environment. EXQ-030b PASS: SD-003 attribution pipeline validated.

#### Step 3.1 — Substrate Debt Resolution ← **current step**

**In-scope:**
- SD-008: alpha_world ≥ 0.9 in LatentStackConfig ✓ (validated EXQ-040)
- SD-009: event-contrastive CE auxiliary loss for z_world encoder ✓ (EXQ-020 PASS)
- SD-010: harm stream separation ✓ (EXQ-056c/058b/059c PASS)
- SD-011: dual nociceptive streams (z_harm_s + z_harm_a) ← **current focus**
- SD-012: homeostatic drive modulation for z_goal seeding ← **next**

**Exit criteria:**
- SD-011 implemented and EXQ-093/094 successors run on dual-stream substrate
- SD-003 counterfactual redesigned for z_harm_s pipeline and validated
- SD-012 implemented; EXQ-085 successors (wanting/liking) runnable with functional z_goal
- Pending FAIL cluster (~10 experiments) reviewed after SD-011 implementation

#### Step 3.2 — V3 Claim Qualification

**In-scope:**
- ARC-016: E3-derived dynamic precision + end-to-end commitment→behavior behavioral distinction
- MECH-025: action-doing mode probe on V3 substrate
- MECH-057b: completion gate retest
- Q-007: valence-precision interaction
- SD-006: multi-rate loop validation at scale (ARC-023, MECH-089–093)
- MECH-090: beta-gated policy propagation
- ARC-024: harm attribution with SD-010 substrate
- Full V3-EXQ series (V3-EXQ-001 through V3-EXQ-010 as designed in transition roadmap)

**Exit criteria:**
- Governance confidence above provisional thresholds for core V3 control claims
- V3-pending claims adjudicated (ARC-007, ARC-016, ARC-018, MECH-025, MECH-033, Q-007)
- **Roadmap updated with V1+V2+V3 learnings before V4 begins**

#### Step 3.3 — V3 Governance Cycle and V4 Entry Decision

**Exit criteria to start V4:**
- Robust separation of exploratory simulation vs committed learning
- Stable behaviour under adversarial trajectory pressure
- Governance confidence above provisional thresholds for core control claims
- V4 entry decision made explicitly

---

### REE-v4 (later: social and institutional complexity)

**Primary role:** Scale to richer multi-agent coupling, language-mediated coordination,
and institutional constraints.

**Exit criteria:** To be defined during V3, informed by what V3 delivers.

---

## V2 Entry Criteria (revised 2026-02-28)

Original criteria (all still required):
- Representation-interface contract stable across qualification and stress lanes
- Uncertainty/error streams calibrated and non-gamed across distribution shifts
- No unresolved adapter contract drift

Added from V1 learning:
- **SD-001 resolved**: E2 implemented as pure isolatable transition model; HippocampalModule
  exists as separate component of E3 complex
- **SD-003 requirement**: Counterfactual E2 querying architecturally possible
  (`e2.forward(z, a_counterfactual)` callable independently)
- **Persistent causal environment**: environment substrate provides persistent agent
  causal footprint, enabling agent-caused vs environment-caused transition disambiguation

---

## Repository Roles

- `REE_assembly`: canonical claims, architecture docs, evidence matrix, governance outputs.
- `ree-v3`: **primary qualification lane** for V3 experiments and claim coverage. Default
  branch: `main`. Results go to `REE_assembly/evidence/experiments/`.
- `ree-v2`: transitional reference. V2 series complete (EXQ-014–028). No new experiments.
- `ree-v1-minimal`: legacy baseline/reference harness. No new mechanism development.
- `ree-experiments-lab`: **ARCHIVED** 2026-02-26. Synthetic scaffolding only; do not use.

---

## Immediate Work Queue (This Cycle)

**Current step: First-Paper Gate Experiments (as of 2026-04-14)**

SD-004 through SD-023 all implemented. ARC-033, MECH-090, MECH-120, MECH-203/204, MECH-205,
MECH-216 implemented. EXQ-354 PASS: MECH-229 behavioral wanting/liking dissociation confirmed.
MECH-112 split into MECH-229 (active) + MECH-230 (candidate). SD-013 promoted to provisional
(governance-2026-04-13-b, conf=0.788). MECH-231 registered + EXQ-407 queued. 2 pending review.

1. **EXQ-326a** (SD-015 nav integration fix + MECH-229 behavioral dissociation in nav context).
2. **EXQ-353** (ARC-033/SD-003/SD-013 interventional vs observational counterfactual):
   critical re-validation of SD-003 interventional pipeline.
3. **EXQ-321a** (MECH-090 bistable gate retest; E2 world-forward training added to fix EXQ-321).
4. **EXQ-325a** (SD-021 descending pain modulation retest; E2 world-forward training fix).
5. **EXQ-365** (MECH-104 surprise gate 5-seed replication).
6. **EXQ-385** (INV-049 offline consolidation necessity / sleep ablation pair).
7. **EXQ-406** (INV-053 depression attractor replication; 5-seed LONG_HORIZON characterisation).
8. **EXQ-407** (MECH-231 E2 short-horizon efference-copy discriminative pair).

---

## ARC-057 Environment-Complexity Gate (2026-04-14)

**Status: PARKED.** ARC-057 (curiosity-approach emergence) cannot be faithfully tested
in the current CausalGridWorld. The mechanism requires an environment where
representational expansion at a location captures genuinely additional information --
near-fractal complexity where zooming in reveals more structure. Grid cells are
informationally flat: a cell is a cell. See `docs/architecture/hippocampal_valence_asymmetry.md`.

**What this blocks:** Faithful testing of approach-via-representational-expansion (MECH-232),
the valence encoding asymmetry (MECH-233), and the curiosity-approach emergence (ARC-057).

**What this does NOT block:** The threat/avoidance side (harm residue field, BLA-pathway
logic) remains fully testable. All existing V3 architecture work continues. The claims
are registered and constrain future design even without experiments.

### Proxy mechanism policy

Any experiment testing approach behavior in the grid world will necessarily use a **proxy
mechanism** for the approach signal (e.g., explicit wanting gradient, DA-modulated place
priority, or direct goal-location bias). This is acceptable for testing downstream
architecture (commitment gating, trajectory selection, E3 evaluation) but carries a
contamination risk:

**Results obtained with a proxy approach mechanism may not generalize to an ARC-057-enabled
agent.** The proxy is a commanded gradient; ARC-057 is emergent from representational
expansion + curiosity. The downstream architecture may develop implicit dependencies on
proxy properties (e.g., gradient smoothness, signal strength, spatial extent) that the
real mechanism would not provide.

### Tagging requirements

1. **Any experiment that tests approach behavior** must declare in its docstring and
   manifest notes which proxy mechanism it uses for the approach signal.
2. **Tag**: experiments using a proxy approach mechanism should include `approach_proxy`
   in their tags. This enables future filtering when ARC-057 becomes testable.
3. **Evidence interpretation**: PASS results for claims that depend on approach behavior
   should carry an `evidence_quality_note` stating the proxy was used and results may not
   transfer to ARC-057-enabled substrate.
4. **Re-validation queue**: when a richer environment becomes available, all `approach_proxy`
   tagged experiments form the re-validation backlog.

### What "richer environment" requires

- More sensory input channels (visual texture, object features, spatial micro-structure)
- Larger latent spaces to encode location-dependent detail
- Significantly more compute for training
- Location-dependent information density (some areas genuinely have more to discover)

This is a V5+ concern. V3 and V4 proceed with proxy mechanisms and honest tagging.

---

## Open Questions

- **SD-010 HarmEncoder architecture**: should z_harm be a separate stream alongside
  z_world and z_self, or should it route through z_world after SD-010? The `l_space.md`
  architecture suggests a four-stream model (z_self, z_world, z_beta, z_harm).
- **ARC-016 E3-derived precision**: EXQ-038 FAIL — root cause (precision invariance)
  needs analysis before designing the next precision-regime experiment.
- **SD-006 phase 2**: time-multiplexed multi-rate is phase 1; true asynchronous
  execution (thread-based or event-loop) is still open. HTA (hierarchical temporal
  abstraction) is the recommended direction but not yet designed.
- **ARC-057 environment substrate**: what is the minimum environment complexity that
  would enable faithful testing of curiosity-approach emergence? Is a continuous 2D
  world with procedural texture sufficient, or does it require full 3D/visual input?
  See ARC-057 gate section above.

---

## Related Claims

- IMPL-008, IMPL-020, IMPL-021, IMPL-022
- MECH-057, MECH-058, MECH-059, MECH-060, MECH-063
- ARC-024, MECH-069, MECH-070, MECH-089, MECH-090, MECH-100, MECH-101, MECH-102
- SD-010 (harm stream separation)

## References

- `docs/architecture/jepa_ree_hybrid_diagram_spec.md`
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `evidence/GOVERNANCE_STATE.md` (substrate debt register: SD-001, SD-002, SD-003)
- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/promotion_demotion_recommendations.md`
- `evidence/planning/CUTOVER_REE_V2_READINESS.md`
