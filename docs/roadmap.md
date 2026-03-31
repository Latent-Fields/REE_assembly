# Roadmap

**Claim Type:** implementation_note
**Scope:** Program phases, repository roles, and phase-gate criteria
**Depends On:** IMPL-020, IMPL-021, IMPL-022, MECH-057, MECH-058, MECH-059, MECH-060
**Status:** candidate
**Claim ID:** IMPL-008
<a id="impl-008"></a>

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

**Explicit non-blockers for V3 completion**

- Sleep/offline consolidation mechanisms.
- Integrated self/other social modelling.
- Full language integration; simple future communication primitives are enough.
- nth-order multi-agent ethics tests.
- Full computational-psychiatry coverage.

**Deferred to V4/V5 / later papers**

- Sleep-like consolidation as a load-bearing mechanism.
- Social coupling and other-modelling inside core substrate.
- Structured communication between agents.
- Emergent ethical behavior in multi-agent settings.
- Stronger psychiatric modelling beyond single-agent perturbation analogs.

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

**Current step: 3.1 — Substrate Debt Resolution (SD-011/012 phase)**

1. **Implement SD-011** (dual nociceptive streams): split z_harm into z_harm_s + z_harm_a;
   add HarmEncoderA, E2_harm_s forward model; update LatentState and E3Selector.
   Design doc: `docs/architecture/sd_011_dual_nociceptive_streams.md`.
2. **Redesign SD-003 counterfactual** for z_harm_s pipeline (post SD-011):
   `causal_sig = E3.harm_eval(z_harm_s_actual) - E3.harm_eval(E2_harm_s(z_harm_s, a_cf))`.
   Do NOT use HarmBridge — bridge_r2=0 is architectural.
3. **Implement SD-012** (homeostatic drive): wire drive_level into GoalState.update() with
   drive-scaled benefit amplitude. Design doc: `docs/architecture/sd_012_homeostatic_drive.md`.
4. **Re-run blocked experiments** (EXQ-093/094 successors + EXQ-085 successors) after
   SD-011/012 implementation.
5. **Await EXQ-074b and EXQ-076b results** (currently queued); review MECH-124 diagnostic
   (z_goal salience vs harm salience as V4 risk indicator).

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
