# Roadmap

**Claim Type:** implementation_note
**Scope:** Program phases, repository roles, and phase-gate criteria
**Depends On:** IMPL-020, IMPL-021, IMPL-022, MECH-057, MECH-058, MECH-059, MECH-060
**Status:** candidate
**Claim ID:** IMPL-008
<a id="impl-008"></a>

---

## Status Snapshot (2026-02-28)

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

### REE-v2 (current phase)

#### Step 2.0 — V2 Redesign ← **current step**

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

**Post-step action:** Revise Steps 2.1–2.5 scope based on what the redesign reveals.

---

#### Step 2.1 — E2 Separation (SD-001 resolution)

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

---

#### Step 2.2 — Representation Interface Contract

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

---

#### Step 2.3 — Persistent Causal Environment

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

---

#### Step 2.4 — Self-Attribution Substrate

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

---

#### Step 2.5 — V2 Qualification

**Primary role:** Genuine experiment coverage across core V2 claims. Sufficient evidence
to make V3 entry decision.

**Exit criteria:**
- Representation interface stable across qualification and stress lanes (from Step 2.2)
- Self-attribution substrate tested (from Step 2.4)
- Governance confidence above provisional thresholds for core V2 claims
- **Roadmap updated with V1+V2 learnings before V3 begins**
- V3 entry decision made explicitly

---

### REE-v3 (next phase after V2: control completion)

**Primary role:** Add and iterate control-plane, hippocampal functions, and E3
commitment/accountability on top of the V2 representation interface and self-attribution
substrate.

**In-scope:**
- Control-plane arbitration and precision routing
- Hippocampal rollout generation + post-commit map/model updates
- Pre-commit vs post-commit error-channel separation and accountability hooks
- Commitment gating and conflict-resolution policies
- MECH-057 (control completion) retested on richer substrate with genuine commitment pressure

**Exit criteria to start V4:**
- Robust separation of exploratory simulation vs committed learning
- Stable behaviour under adversarial trajectory pressure
- Governance confidence above provisional thresholds for core control claims
- **Roadmap updated with V1+V2+V3 learnings before V4 begins**

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
- `ree-v2`: primary qualification lane for V2 representation-interface profiles and
  acceptance gates.
- `ree-experiments-lab`: stress/adversarial/replication experiments and falsification
  pressure.
- `ree-v1-minimal`: legacy baseline/reference harness. Transitional parity checks until
  V2 coverage is complete. No new mechanism development.

---

## Immediate Work Queue (This Cycle)

**Current step: 2.0 — V2 Redesign**

1. Complete EXQ-008 (candidate count ablation) and EXQ-009 (residue routing weight) to
   close out V1 evidence on MECH-063 and MECH-062. Results inform V2 redesign.
2. Produce V2 implementation spec document: subsystem boundaries, SD-001/002/003
   addressed in design, required metrics, failure gates.
3. Revise V2 entry criteria in this roadmap once implementation spec is complete (above
   revision is preliminary; spec may refine further).
4. Run targeted literature program for V3-critical systems:
   - hippocampal replay/planning/map-update mechanisms,
   - prefrontal control/arbitration/commitment mechanisms,
   - JEPA-like latent-to-hippocampal mapping constraints.
5. Route resulting evidence into backlog/proposals and governance decisions.

**Deferred pending Step 2.0 completion:**
- EXQ-010 through EXQ-013 (extended-seed reruns of PASS claims): low-priority
  confidence accumulation; do not block V2 redesign work.

---

## Open Questions

- Should the persistent-causal-footprint environment (Step 2.3) be built in-repo or
  sourced from an existing environment library?
- What minimum genuine-run threshold triggers promotion from provisional to active for
  V2 claims? (V1 threshold was informally 2 genuine runs; V2 should define this
  explicitly in the Step 2.0 spec.)

---

## Related Claims

- IMPL-008, IMPL-020, IMPL-021, IMPL-022
- MECH-057, MECH-058, MECH-059, MECH-060, MECH-063

## References

- `docs/architecture/jepa_ree_hybrid_diagram_spec.md`
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `evidence/GOVERNANCE_STATE.md` (substrate debt register: SD-001, SD-002, SD-003)
- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/promotion_demotion_recommendations.md`
- `evidence/planning/CUTOVER_REE_V2_READINESS.md`
