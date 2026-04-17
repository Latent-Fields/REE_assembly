# Invariant Classification Audit

**Session:** Session B of invariant-types governance cycle
**Date:** 2026-04-17
**Auditor session:** session-b-2026-04-17-invariant-audit
**Total invariants audited:** 72

Schema reference: `docs/architecture/invariant_types.md`
Planning doc: `docs/thoughts/2026-04-17_invariant_types_governance.md`

---

## CHECKPOINT REACHED

Per Q4 of the planning doc (§7 `pending_substrate_reconfirmation` threshold rule), the
retroactive-flag pass exceeds both thresholds:

- Total emergent: 22
- Total flagged `pending_substrate_reconfirmation: true`: 19
- Fraction flagged: 86% (threshold: >20%)
- Absolute flag count: 19 (threshold: >10)

**Substrates driving the flags** (multi-flag substrates first):

- **SD-017** (sleep infrastructure, provisional): 3 flags — INV-045, INV-046, INV-050
- **SD-012** (homeostatic drive, candidate): 3 flags — INV-041, INV-052, INV-053
- **SD-014** (hippocampal 4-component valence, candidate): 3 flags — INV-054, INV-056, INV-065
- **ARC-019** (staged developmental curriculum, provisional): 3 flags — INV-043, INV-055, INV-056
- **ARC-035** (vmPFC stored->active compiler, candidate): 2 flags — INV-037, INV-038
- **ARC-041** (E1 cue-indexed retrieval, candidate): 2 flags — INV-040, INV-041
- Single-flag substrates: SD-011, SD-015, SD-026, ARC-016, ARC-030, ARC-038, ARC-039, ARC-040,
  ARC-042, ARC-046, ARC-049 (one flag each).

**Auditor recommendation: proceed.** The flag rate is high because most substrates that carry
emergent invariants are still `candidate` or `provisional` — the substrate layer is under
active construction (SD-011 through SD-028 registered in the last six weeks, ARC-030 through
ARC-057 predominantly candidate). The flag is doing its job: it marks that the invariants'
subjects rest on machinery whose design is not yet governance-frozen. Reading 86% flagged as
"rule misfire" would require a substrate layer that is already mostly active, which it is not.

If the rule did misfire, the fix would not be to relax the threshold — it would be to promote
substrates. That is out of scope for Session B.

Session B stops before committing `claims.yaml` pending user confirmation. The registry
(`docs/governance/invariant_classification_audit.md`) and the applied-but-unstaged edits to
`claims.yaml` are ready for review.

---

## Summary

- Clear universal: 36
- Clear emergent: 22
- Grey zone: 14
- Sum: 72

Retroactive flag count (`pending_substrate_reconfirmation: true`): 19
Checkpoint threshold triggered: **yes**

---

## Clear Universal

These invariants can be stated and defended using information-theoretic,
thermodynamic, decision-theoretic, or purely philosophical/logical
vocabulary. They would survive a substantially different E1/E2/E3 substrate.

### INV-001
- **Title:** No explicit ethics module or moral scoring layer.
- **Rationale:** Decision-theoretic design stance (ethics-from-constraint rather than
  optimisation of a scalar moral objective); holds across any architecture that respects
  the constraint, not a claim about specific REE structures.

### INV-002
- **Title:** Coherence includes temporal/phase binding, not just static metrics.
- **Rationale:** Definitional / dynamical-systems claim about what coherence must include;
  independent of substrate choice.

### INV-003
- **Title:** Language emerges as functional self-representation, not a bolt-on.
- **Rationale:** Functional-role claim about language stateable in any cognitive architecture
  with representations and agents.

### INV-007
- **Title:** Language cannot override embodied harm sensing.
- **Rationale:** Safety-ordering claim: symbolic/deliberate channels must not override
  aversive affective signal. Holds in any architecture with those channel types, regardless
  of how harm sensing is physically realised.

### INV-008
- **Title:** Precision is routed and depth-specific, not global.
- **Rationale:** Generic predictive-processing / attention-as-precision claim; substrate-agnostic.

### INV-009
- **Title:** Attention is precision modulation, not symbolic control.
- **Rationale:** Predictive-processing / information-theoretic claim about what attention is;
  substrate-independent.

### INV-010
- **Title:** Offline integration exists and is required.
- **Rationale:** General computational-necessity claim (further generalised by INV-049);
  independent of how offline phases are physically realised.

### INV-011
- **Title:** Imagination must be possible without belief update.
- **Rationale:** Decision-theoretic separability of counterfactual simulation from posterior
  update; holds in any agent that both simulates and updates.

### INV-013
- **Title:** Cognition is predictive, iterative, and multi-timescale.
- **Rationale:** General dynamical/predictive-processing claim about cognition; does not pick
  out any REE-specific structure.

### INV-014
- **Title:** Representation and regulation are strictly separated.
- **Rationale:** Architectural-category claim (representation vs regulation channels); would
  hold under any substrate that distinguishes those channels.

### INV-015
- **Title:** Ethics emerges from constraint, not optimisation.
- **Rationale:** Decision-theoretic stance about the origin of ethical behaviour;
  substrate-agnostic.

### INV-016
- **Title:** Stability is prioritized over maximal performance.
- **Rationale:** Engineering/design priority claim; stateable for any optimising agent.

### INV-017
- **Title:** Runaway behavior is a control failure, not representational.
- **Rationale:** Classification of failure-mode in dynamical/control-theoretic terms;
  substrate-independent.

### INV-018
- **Title:** Agency is required; passive predictors are not REE.
- **Rationale:** Definitional boundary claim about what counts as agentive; holds across
  substrates.

### INV-022
- **Title:** Trust/precision allocation must remain heterogeneous, not a single scalar.
- **Rationale:** Information-theoretic / predictive-processing claim; applies to any
  hierarchical precision-weighted architecture.

### INV-023
- **Title:** Protected offline recalibration/integration regimes are structurally required.
- **Rationale:** Subsumed by INV-049's general computational-necessity argument for offline
  phases; substrate-independent.

### INV-025
- **Title:** Irreducible uncertainty is an epistemological constraint that cannot be
  engineered away.
- **Rationale:** Information-theoretic / epistemological claim; stateable without any
  substrate commitment.

### INV-026
- **Title:** A self is an operational prerequisite for responsible agency.
- **Rationale:** Philosophical/decision-theoretic claim; the "self" here is an operational
  role, not a specific REE representation.

### INV-027
- **Title:** An external world is a structural prerequisite for grounded representation.
- **Rationale:** Grounded-cognition claim; substrate-independent.

### INV-028
- **Title:** Shared-world ethics requires modelling others as co-inhabitants of the same
  consequence space.
- **Rationale:** Ethical/decision-theoretic claim about what shared-world ethics requires;
  holds for any agent architecture capable of modelling others.

### INV-029
- **Title:** Love as long-horizon care-investment is a structurally coherent agent disposition.
- **Rationale:** Decision-theoretic/philosophical claim about the coherence of the disposition
  under any sufficiently expressive agent architecture.

### INV-030
- **Title:** Viability is defined relative to the agent's continuity in a shared world, not
  as a scalar reward.
- **Rationale:** Decision-theoretic design stance on what viability means; rejects the
  scalar-reward formulation independent of substrate.

### INV-031
- **Title:** Functional persistence in a shared world is the operational goal of cognition.
- **Rationale:** Decision-theoretic goal-formulation claim; independent of substrate.

### INV-032
- **Title:** Moral agency requires both approach and avoidance drives.
- **Rationale:** Decision-theoretic/ethical claim about necessary-condition structure of
  moral agency; universal even though REE instantiates it via ARC-030.

### INV-042
- **Title:** The five axioms jointly derive ethical objectives.
- **Rationale:** Axiomatic/logical derivation claim from philosophical axioms; no substrate
  required to state.

### INV-044
- **Title:** Approximate Bayesian contextual inference is architecturally impossible to
  co-compute with online encoding.
- **Rationale:** Information-theoretic impossibility argument; substrate-independent.

### INV-049
- **Title:** Any agent that builds a model of the world and acts in it requires periodic
  offline phases.
- **Rationale:** Explicit universal: the claim asserts "this is not a biological contingency
  but a general computational necessity for model-building agents."

### INV-057
- **Title:** Cross-species signal legibility evidences functional specificity.
- **Rationale:** Evolutionary/communication-theoretic claim about signal structure; does not
  depend on REE substrate.

### INV-058
- **Title:** Play is a structurally necessary behavioral mode.
- **Rationale:** Decision-theoretic / learning-theoretic claim about the role of bounded
  low-stakes contexts in skill acquisition.

### INV-059
- **Title:** Mutual frame-maintenance signaling is necessary for play.
- **Rationale:** Game-theoretic claim about frame negotiation; does not require REE-specific
  machinery to state.

### INV-067
- **Title:** Verisimilitude definition.
- **Rationale:** Definitional claim in predictive-processing vocabulary.

### INV-068
- **Title:** Temporal depth D_V(t).
- **Rationale:** Definitional extension of INV-067; substrate-independent.

### INV-069
- **Title:** Self as dynamically sustained verisimilitude-maintaining process.
- **Rationale:** Process-philosophical definition of self in terms of INV-067/068; general.

### INV-070
- **Title:** Epistemic responsibility.
- **Rationale:** Ethical/decision-theoretic claim; substrate-independent.

### INV-071
- **Title:** Language as similarity repair.
- **Rationale:** Functional-role claim about language in inter-agent coordination;
  substrate-agnostic.

### INV-072
- **Title:** Violence conditions corollary.
- **Rationale:** Ethical/logical claim derived from INV-028/029/070/071; no substrate
  required.

---

## Clear Emergent

Each entry's subject matter becomes ill-defined if the listed substrate is retracted. Every
`emergent_from` entry is already present in the invariant's `depends_on`.

### INV-012
- **Title:** Responsibility arises through commitment, not prediction alone.
- **emergent_from:** [SD-026]
- **Rationale:** "Commitment" as load-bearing ethical concept requires a mechanism by which
  endogenous goal-derived templates can write precision biases before a decision (SD-026);
  without that, commitment collapses into "whatever was already conditioned." (Already
  classified in Session A — unchanged.)
- **Substrate status at audit:** candidate
- **pending_substrate_reconfirmation applied:** yes (already set in Session A)

### INV-033
- **Title:** REE agents require second-order epistemic access to their own model confidence,
  wired into commit gating.
- **emergent_from:** [ARC-016]
- **Rationale:** "Wired into commit gating" and "structurally represented model confidence"
  are concepts that only have well-formed referents under ARC-016 (modes as control-plane
  regimes with routed precision). Without a mode/precision regime substrate, there is no
  commit-gating locus for second-order access to plug into.
- **Substrate status at audit:** provisional
- **pending_substrate_reconfirmation applied:** yes

### INV-034
- **Title:** Goal maintenance is a necessary co-condition for ethical agency.
- **emergent_from:** [ARC-030]
- **Rationale:** Pairs with INV-032 but asserts the need for a prospective goal-maintenance
  drive that is symmetrically Go-side (not merely NoGo/harm-avoidance). The subject —
  "prospective goal-directed motivation" as distinct from harm-avoidance — requires the
  symmetric Go/NoGo substrate (ARC-030). In a pure-avoidance architecture the invariant is
  un-stateable, not merely unevidenced.
- **Substrate status at audit:** candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-035
- **Title:** A REE state must not be defined purely by sensory appearance.
- **emergent_from:** [ARC-003, ARC-004, ARC-007]
- **Rationale:** "REE state" is explicit in the title — the claim is definitional for state
  representation given commitment (ARC-003), multi-timescale latent stack (ARC-004), and
  hippocampal paths through residue-field terrain (ARC-007). Retract any of these and the
  distinguishing dimensions named (temporal position, active commitment, goal/antigoal,
  operative constraints) have no structural home.
- **Substrate status at audit:** all three active
- **pending_substrate_reconfirmation applied:** no

### INV-036
- **Title:** A REE state is valid only if it supports transition prediction, valence/antigoal
  tagging, and uncertainty representation.
- **emergent_from:** [ARC-003, ARC-007, ARC-018]
- **Rationale:** Three validity-conditions on REE state objects; the state object itself is
  the ARC-003/007 construct, and "transition prediction supports trajectory evaluation"
  presumes ARC-018 (explicit rollouts and post-commitment viability mapping).
- **Substrate status at audit:** all three active
- **pending_substrate_reconfirmation applied:** no

### INV-037
- **Title:** Stored-vs-active distinction requires a preparation substrate (vmPFC-analog).
- **emergent_from:** [ARC-035]
- **Rationale:** The stored/active distinction as an architectural claim is defined by the
  existence of a compiler (ARC-035 vmPFC) that converts stored content into live state
  components. Remove ARC-035 and the claim has no referent.
- **Substrate status at audit:** candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-038
- **Title:** EVR pattern: post-hoc ethical scoring without active constraint preparation
  produces unconstrained trajectory generation.
- **emergent_from:** [ARC-035]
- **Rationale:** The EVR pattern is defined as the failure mode of a system with post-hoc
  scoring but no ARC-035 preparation substrate. Without ARC-035 in the architectural
  vocabulary, "absence-of-active-constraint-preparation" is not a specifiable condition.
- **Substrate status at audit:** candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-039
- **Title:** Schema-primed rapid consolidation.
- **emergent_from:** [ARC-007, ARC-038]
- **Rationale:** "Stable prior map" and "mature coherent residue field" are ARC-007
  constructs, and the map-stability-gated consolidation rate is a claim about ARC-038's
  replay-switching regime. Without hippocampal terrain maps and switchable replay, neither
  side of the conditional is well-formed.
- **Substrate status at audit:** ARC-007 active; ARC-038 candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-040
- **Title:** A minimal z_world cue pattern is sufficient to activate the appropriate
  harm/goal terrain precision configuration.
- **emergent_from:** [SD-005, ARC-041]
- **Rationale:** Title explicitly names z_world (SD-005 self/world split) and the E1
  cue-indexed retrieval circuit (ARC-041). Retract either and the claim's subject ("minimal
  z_world cue pattern triggers terrain preparation") has no object.
- **Substrate status at audit:** SD-005 implemented; ARC-041 candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-041
- **Title:** Childhood phase is architecturally prerequisite for E3 ethical selection.
- **emergent_from:** [ARC-042, SD-012, SD-016]
- **Rationale:** The claim is that a specific developmental regime populates ARC-041's
  ContextMemory (SD-016) and exercises the homeostatic drive (SD-012) so that ARC-042's
  pre-initialised ethical selection machinery operates on real signal. Without these
  substrates the notion of "architectural prerequisite" is un-stateable.
- **Substrate status at audit:** ARC-042 candidate; SD-012 candidate; SD-016 implemented
- **pending_substrate_reconfirmation applied:** yes

### INV-043
- **Title:** REE architecture enables but does not guarantee ethical development; caregiver
  love is required.
- **emergent_from:** [ARC-019, ARC-040]
- **Rationale:** The claim picks out "developmental phase in which the agent experiences love
  from caregivers" — which presumes ARC-040 (caregiver substrate) and ARC-019 (staged
  developmental curriculum). Without a developmental-phase architecture, the conditional
  has no antecedent.
- **Substrate status at audit:** ARC-019 provisional; ARC-040 candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-045
- **Title:** NREM-then-REM sleep phase sequence is the correct computational order.
- **emergent_from:** [SD-017]
- **Rationale:** The claim is specifically about the ordering within the SD-017 sleep-phase
  infrastructure. Without SD-017 the NREM/REM labels and the phase-dependency chain have
  no substrate referent. (INV-049 states the universal version; INV-045 is the
  substrate-specific ordering claim.)
- **Substrate status at audit:** provisional
- **pending_substrate_reconfirmation applied:** yes

### INV-046
- **Title:** Dementia is computationally a failure of the contextual attribution pipeline.
- **emergent_from:** [SD-017]
- **Rationale:** "Contextual attribution pipeline" in this invariant means the pipeline
  maintained by SD-017's sleep phases. Without SD-017 the attribution-pipeline-failure
  reframing is not stateable in those specific terms.
- **Substrate status at audit:** provisional
- **pending_substrate_reconfirmation applied:** yes

### INV-050
- **Title:** Sleep phase architecture is regulated by three drives (circadian, homeostatic,
  MEL).
- **emergent_from:** [SD-017]
- **Rationale:** The three-drive claim is a claim about the regulation of SD-017's sleep
  phase architecture. The drives exist abstractly, but the invariant's subject (sleep phase
  architecture regulation) is SD-017-resident.
- **Substrate status at audit:** provisional
- **pending_substrate_reconfirmation applied:** yes

### INV-052
- **Title:** Goal-directed behaviour in adversive environments requires a tonic regulatory
  system.
- **emergent_from:** [SD-012]
- **Rationale:** "Tonic regulatory system maintaining benefit orientation" is an SD-012
  concept (homeostatic drive modulation for z_goal seeding). Without SD-012 the claim's
  subject is un-stateable.
- **Substrate status at audit:** candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-053
- **Title:** Chronic harm-dominated environments produce a self-maintaining depressive
  attractor.
- **emergent_from:** [SD-011, SD-012]
- **Rationale:** "z_goal seeding failure", "terrain collapse", "HABIT/PLANNED behavioural
  equivalence" are all SD-012/SD-011-resident concepts. Remove either substrate and the
  attractor description has no object.
- **Substrate status at audit:** both candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-054
- **Title:** Benefit terrain collapse creates a closed negative feedback loop predicting
  chronicity.
- **emergent_from:** [SD-014]
- **Rationale:** "Benefit terrain" names the hippocampal 4-component valence vector (SD-014).
  The collapse-and-feedback-loop claim is a claim about that specific terrain representation.
- **Substrate status at audit:** candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-055
- **Title:** A pre-childhood infant stage is developmentally necessary.
- **emergent_from:** [ARC-019, ARC-046]
- **Rationale:** "Infant stage" in the ARC-019 curriculum sense, requiring ARC-046's hazard
  protection for sensorially broad exploration. Without those substrates the phase the
  invariant picks out does not exist architecturally.
- **Substrate status at audit:** ARC-019 provisional; ARC-046 candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-056
- **Title:** Developmental hardening should be substrate-specific: selective neoteny.
- **emergent_from:** [ARC-010, ARC-019, SD-014]
- **Rationale:** Names specific subsystems (social cognition = ARC-010; developmental staging
  = ARC-019; valence/goal = SD-014) that retain elevated plasticity. The substrate-specific
  hardening claim has no partition to refer to without these.
- **Substrate status at audit:** ARC-010 active; ARC-019 provisional; SD-014 candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-060
- **Title:** Play dominates child developmental phase; play type progresses as subsystem
  competence develops.
- **emergent_from:** [ARC-049]
- **Rationale:** "Play" in the ARC-049 sense (co-maintained context tag held by agent and
  environment). The progression-with-competence claim is about play episodes as defined by
  that substrate.
- **Substrate status at audit:** candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-065
- **Title:** Proxy goal necessity for multi-step planning.
- **emergent_from:** [SD-014, SD-015]
- **Rationale:** "Proxy goal" presumes a goal/resource representation (SD-015 z_resource
  encoder) and a valence vector (SD-014). Without these the proxy-goal construct is
  un-stateable.
- **Substrate status at audit:** both candidate
- **pending_substrate_reconfirmation applied:** yes

### INV-066
- **Title:** z_self subtraction must precede coherency-based control plane signals.
- **emergent_from:** [SD-005]
- **Rationale:** z_self as a separable quantity exists only under SD-005's self/world split.
  Without SD-005 the subtraction operation is un-stateable (no z_self to subtract).
- **Substrate status at audit:** implemented (treated as active-equivalent)
- **pending_substrate_reconfirmation applied:** no

---

## Grey Zone

These entries could plausibly resolve as universal (by re-statement) or as emergent on a
specific substrate, but the audit is not confident enough to force a verdict in one session.
Each entry carries a self-contained follow-up prompt for a Session C_n auditor.

### INV-004
- **Title:** Post-commit consequence traces are persistent, not resettable.
- **Why ambiguous:** "Post-commit" and "consequence traces" are REE-specific terms
  (commitment boundary + residue field), but the underlying principle — irreversibility of
  committed action effects — is stateable in pure decision-theoretic vocabulary. As written
  the invariant has empty `depends_on`, so there is no explicit substrate anchor to treat
  as emergent-of.
- **Candidate classifications:**
  - universal (re-stated as: "actions, once committed, leave persistent state changes that
    cannot be erased by subsequent decisions")
  - emergent on: [ARC-003, ARC-013] (commitment + residue field) — would require adding
    these to `depends_on`
- **Follow-up prompt for Session C_n:**
  > INV-004 ("Post-commit consequence traces are persistent, not resettable.") has empty
  > `depends_on` and references the REE-specific "post-commit" / "consequence traces"
  > terminology. Decide: (a) restate the invariant in substrate-neutral decision-theoretic
  > terms and classify as universal (preferred if possible — this is essentially a
  > restatement of action-irreversibility), or (b) keep the wording and classify as emergent
  > on ARC-003 (commitment) and ARC-013 (residue field as persistent latent-space curvature),
  > adding these to `depends_on`. If restated, update the title, subject, and notes so the
  > registry reflects the universal framing. Read the invariant, `docs/invariants.md#inv-004`,
  > and ARC-003/ARC-013 entries before deciding. Update the audit registry's grey-zone entry
  > with the decision and rationale.

### INV-005
- **Title:** Harm to others contributes via mirror modelling, not symbolic rules.
- **Why ambiguous:** Empty `depends_on`, but the invariant explicitly names "mirror
  modelling" — which is ARC-010's substrate. The principle "harm-to-others grounded in
  simulation, not symbolic rules" is decision-theoretic, but "mirror modelling" is a
  specific architectural choice. Auditor uncertain whether the claim intends the general
  principle or the specific mechanism.
- **Candidate classifications:**
  - universal (re-stated as: "harm-to-others must be grounded in simulative/empathic
    mechanisms, not symbolic rule evaluation")
  - emergent on: [ARC-010] (mirror modelling and coupling) — requires adding ARC-010 to
    `depends_on`.
- **Follow-up prompt for Session C_n:**
  > INV-005 ("Harm to others contributes via mirror modelling, not symbolic rules.")
  > literally names mirror modelling (ARC-010) in the title. Decide whether the load-bearing
  > claim is (a) the general principle that other-harm is grounded in simulation rather than
  > symbolic rules (universal — rewrite title to remove "mirror modelling" specifically),
  > or (b) the specific architectural commitment that ARC-010's mirror modelling substrate
  > is the implementation locus (emergent on ARC-010, add to `depends_on`). Read ARC-010 and
  > the sources in INV-005 before deciding.

### INV-006
- **Title:** Post-commit consequence traces cannot be erased, only integrated.
- **Why ambiguous:** Same class as INV-004 — "post-commit consequence traces" phrasing is
  REE-specific but the irreversibility principle is general. Adds an integration claim
  (only-integrated, not erased) which overlaps with sleep/consolidation (ARC-011/SD-017).
- **Candidate classifications:**
  - universal (re-stated as: action effects are integrated into subsequent world state,
    never reverted)
  - emergent on: [ARC-003, ARC-013, ARC-011] (commitment + residue + offline consolidation)
- **Follow-up prompt for Session C_n:**
  > INV-006 ("Post-commit consequence traces cannot be erased, only integrated.") pairs with
  > INV-004 but adds an integration claim that may require offline-consolidation substrate
  > (ARC-011 or SD-017). Decide the classification jointly with INV-004. If INV-004 is
  > re-stated as universal, consider whether INV-006 can follow, or whether the integration
  > claim is substrate-dependent in a way that INV-004 is not. Options: (a) universal with
  > restatement, (b) emergent on ARC-003+ARC-013+ARC-011, (c) split the invariant into a
  > universal irreversibility claim and an emergent integration claim.

### INV-019
- **Title:** Rehearsal traversal and irreversible durable write must remain separated.
- **Why ambiguous:** The separation principle is decision-theoretic (simulation vs
  commitment — see INV-011), but "rehearsal traversal" and "durable write" are REE-specific
  vocabulary tied to DMN rollouts (ARC-014) and memory-write loci (MECH-060, listed in deps).
- **Candidate classifications:**
  - universal (extension of INV-011 — "any agent capable of simulation must separate the
    simulation path from the path that commits to memory")
  - emergent on: [ARC-014] (Default Mode enables safe imagination without commitment) —
    would need ARC-014 added to depends_on.
- **Follow-up prompt for Session C_n:**
  > INV-019 ("Rehearsal traversal and irreversible durable write must remain separated.")
  > appears to be a substrate-flavoured restatement of INV-011's universal "imagination
  > without belief update" principle. Decide: (a) universal, justified as a direct
  > consequence of INV-011 under any architecture with durable memory (preferred if
  > possible — restate to remove "rehearsal traversal / durable write" phrasing), or (b)
  > emergent on ARC-014 (Default Mode) because the particular separation regime this
  > invariant asserts is ARC-014-resident. Check whether MECH-060 already names the
  > load-bearing substrate.

### INV-020
- **Title:** Constraint stores are authority-stratified from direct observational/symbolic
  writes.
- **Why ambiguous:** "Constraint stores" and "authority stratification" are REE-specific
  architectural terms (see MECH-064, MECH-065 in deps), but the principle (write-channel
  stratification by type) can be stated architecturally-neutrally.
- **Candidate classifications:**
  - universal (re-stated as: "any architecture with multiple write channels requires typed
    authority separation between them")
  - emergent on: [ARC-020] (offline consolidation protected by typed authority/write
    boundaries) — ARC-020 would need to be added to depends_on.
- **Follow-up prompt for Session C_n:**
  > INV-020 ("Constraint stores are authority-stratified from direct observational/symbolic
  > writes.") depends on MECH-064/065 but no SD/ARC substrate. Check whether ARC-020
  > (typed authority/write boundaries in offline consolidation) is the load-bearing
  > substrate for this invariant's subject. If yes, classify emergent on ARC-020 (and add
  > to depends_on). If the claim is fundamentally about any multi-channel architecture,
  > restate universally.

### INV-021
- **Title:** Responsibility-bearing durable updates occur only at typed commit boundaries.
- **Why ambiguous:** Structurally parallel to INV-012 (both centre on commitment), but
  `depends_on` is [INV-012, MECH-061, Q-015] — no SD/ARC IDs. The "commit boundary" is
  REE's architectural commitment (ARC-003 / SD-026), but the invariant does not declare
  that dependency.
- **Candidate classifications:**
  - emergent on: [SD-026] (via INV-012 — the commitment-as-load-bearing substrate). Adding
    SD-026 to `depends_on` is defensible because INV-021 is in practice a generalisation of
    INV-012.
  - emergent on: [ARC-003, SD-026] (E3's commit action + the prospective-precision
    substrate that gives commitment its ethical content)
- **Follow-up prompt for Session C_n:**
  > INV-021 ("Responsibility-bearing durable updates occur only at typed commit boundaries.")
  > is a structural parallel to INV-012 (Session A's worked emergent example). Decide
  > whether to classify emergent on SD-026 only (treating INV-021 as a generalisation of
  > INV-012), or on ARC-003 + SD-026 (E3's commit action + SD-026's commitment content),
  > and add the chosen substrate to depends_on. Refer to INV-012's emergent-on-SD-026
  > rationale in the audit registry and the architecture doc for the load-bearing argument.

### INV-024
- **Title:** Offline consolidation and online commitment must remain isolated at
  responsibility-bearing write loci.
- **Why ambiguous:** Crosses both the commitment substrate (INV-021 / INV-012) and the
  offline substrate (ARC-020 / SD-017). The claim is a conjunctive emergence: it relies on
  both substrate clusters simultaneously.
- **Candidate classifications:**
  - emergent on: [ARC-020] (offline write-boundary typing) — already in depends_on.
  - emergent on: [ARC-020, SD-026] (offline substrate + commitment substrate) — needs
    SD-026 added to depends_on.
- **Follow-up prompt for Session C_n:**
  > INV-024 ("Offline consolidation and online commitment must remain isolated at
  > responsibility-bearing write loci.") depends on INV-021/INV-023/ARC-020. Decide whether
  > to classify emergent on ARC-020 alone (the typed write boundary in offline consolidation)
  > or on ARC-020 plus SD-026 (because "responsibility-bearing" imports INV-012's
  > substrate dependency). Note that Session C's decisions on INV-021/INV-024 should be
  > made jointly with INV-004/INV-006 since they all centre on the commitment/post-commit
  > cluster.

### INV-047
- **Title:** Alzheimer's staged cognitive decline follows reverse of sleep phase dependency
  ordering.
- **Why ambiguous:** Logically depends on SD-017 via INV-045/INV-046 (both in its
  depends_on), but does not name SD-017 in its own `depends_on`. The specific staged profile
  claim may be a universal consequence of INV-045's ordering plus general lesion reasoning,
  or it may be substrate-bound via SD-017.
- **Candidate classifications:**
  - universal (derived from INV-045 by reversed-dependency lesion logic)
  - emergent on: [SD-017] (transitive through INV-045; would need SD-017 added to deps)
- **Follow-up prompt for Session C_n:**
  > INV-047 ("Alzheimer's staged cognitive decline follows reverse of sleep phase dependency
  > ordering.") logically rests on SD-017 via INV-045/INV-046 but does not itself list
  > SD-017 in depends_on. Decide: (a) classify as universal deriving purely from INV-045's
  > ordering plus generic lesion-reversal reasoning (so the AD-specific staged prediction
  > is a consequence of the ordering, not of SD-017 directly), or (b) classify as emergent
  > on SD-017 and add SD-017 to depends_on. Consider whether MECH-168 (listed in deps) is
  > the load-bearing substrate link.

### INV-048
- **Title:** Pharmacological sleep disruption is equivalent to behavioral disruption in
  attribution pipeline degradation.
- **Why ambiguous:** Same class as INV-047 — logically depends on SD-017 via INV-045/46
  but does not list SD-017 in its own depends_on. The equivalence claim is stateable
  universally as "any disruption mechanism with equivalent phase-fidelity impact produces
  equivalent degradation" or emergent on SD-017 ("the pipeline is SD-017's, and mechanism
  is immaterial once phase fidelity matches").
- **Candidate classifications:**
  - universal (phase-fidelity equivalence principle)
  - emergent on: [SD-017]
- **Follow-up prompt for Session C_n:**
  > INV-048 ("Pharmacological sleep disruption produces equivalent attribution pipeline
  > degradation to behavioral.") is a parallel to INV-047 — decide jointly. The universal
  > reading is that phase-fidelity mediates the disruption regardless of mechanism; the
  > emergent reading is that "the pipeline" just is SD-017's. Choose per joint decision on
  > INV-045 through INV-048 to keep the sleep-cluster classifications coherent.

### INV-051
- **Title:** There exists an optimal range of daily Model Error Load (MEL).
- **Why ambiguous:** Extends INV-050 (emergent on SD-017 per this audit), but its own
  depends_on is [INV-050, INV-049, MECH-181] with no SD/ARC. The MEL-range claim is a
  general learning-theoretic proposition that could stand independently, or a substrate-
  specific claim about SD-017's throughput.
- **Candidate classifications:**
  - universal (under-/over-stimulation of any model-update drive produces degenerate
    outcomes — derivable from learning-theory without SD-017)
  - emergent on: [SD-017] (MEL is an SD-017-resident drive)
- **Follow-up prompt for Session C_n:**
  > INV-051 ("Optimal range of daily Model Error Load MEL.") extends INV-050. Decide
  > classification jointly. If INV-050 is emergent on SD-017 (as this audit set it), INV-051
  > most likely is too — but verify whether "MEL" is a concept that requires SD-017 to be
  > stateable or whether it generalises to any model-building agent's error throughput.
  > Check MECH-181 and SD-017 design doc.

### INV-061
- **Title:** Psychiatric frame confusion (derealization, delusion, PTSD, anxiety, mania,
  impulsivity, commitment paralysis) share a common architectural substrate: undertrained
  real/synthetic frame distinction from insufficient pretend play.
- **Why ambiguous:** Depends purely on MECHs (MECH-094 hypothesis tag + MECH-198/200/201/202)
  with no SD/ARC ID. The hypothesis-tag mechanism is the load-bearing substrate, but MECH
  entries are not allowed in `emergent_from`. The claim's subject ("frame confusion") is
  MECH-094-resident.
- **Candidate classifications:**
  - emergent on: [ARC-014] (Default Mode — where pretend/real frame distinction lives) —
    not currently in depends_on; would need adding.
  - emergent on: [ARC-049] (play mode boundary) — not in depends_on; would need adding.
  - universal: unlikely; the frame distinction is an architectural feature.
- **Follow-up prompt for Session C_n:**
  > INV-061 ("Psychiatric frame confusion shares a common architectural substrate.") depends
  > only on MECHs — no SD/ARC is listed. MECH-094 (hypothesis tag) is the obvious load-
  > bearing mechanism, but MECH entries cannot populate `emergent_from`. Decide which SD/ARC
  > owns MECH-094 — candidates are ARC-014 (Default Mode) and ARC-049 (play mode boundary).
  > Add the chosen substrate to depends_on and classify emergent on it.

### INV-062
- **Title:** Dream phenomenology maps onto four computationally distinct sleep functions.
- **Why ambiguous:** Same class as INV-061 — depends_on is all MECHs and INV-049/MECH-121/123.
  The claim requires SD-017 to name "sleep functions", but SD-017 is not in depends_on. The
  four-dream-type taxonomy is SD-017-resident.
- **Candidate classifications:**
  - emergent on: [SD-017] — add to depends_on.
- **Follow-up prompt for Session C_n:**
  > INV-062 ("Dream phenomenology maps onto four sleep functions.") is an SD-017-resident
  > claim by content but does not list SD-017 in depends_on. Add SD-017 and classify
  > emergent. Verify that the four dream types (harm-contrastive replay, goal-contrastive
  > replay, NREM semantic consolidation, REM free-running) each map to an SD-017 phase.

### INV-063
- **Title:** Minimum entropy intake sleep dependency.
- **Why ambiguous:** Depends on INV-049/MECH-121/205/209/210/211 — MECH-only, no SD/ARC.
  Load-bearing substrate is likely SD-017 (the MEL/throughput argument is sleep-phase-
  resident) but the invariant does not declare it.
- **Candidate classifications:**
  - emergent on: [SD-017] — add to depends_on.
  - universal: unlikely without significant restatement, as the "entropy intake" concept
    is defined relative to sleep functions.
- **Follow-up prompt for Session C_n:**
  > INV-063 ("Minimum entropy intake sleep dependency.") depends only on MECHs. Add SD-017
  > to depends_on and classify emergent, paralleling the sleep-cluster decisions on
  > INV-045/INV-046/INV-050/INV-062.

### INV-064
- **Title:** E1/E2/E3 maturational sequence necessity.
- **Why ambiguous:** The title explicitly names E1/E2/E3 — clearly emergent on ARC-001/002/003
  — but `depends_on` is [INV-055, INV-056, MECH-212, MECH-213] with no ARC. Adding
  ARC-001/002/003 is defensible because the subject is literally those substrates' maturation.
- **Candidate classifications:**
  - emergent on: [ARC-001, ARC-002, ARC-003] — add to depends_on.
  - emergent on: [ARC-019] (staged developmental curriculum, which defines the maturational
    sequence) — add to depends_on. Possibly plus the three engine ARCs.
- **Follow-up prompt for Session C_n:**
  > INV-064 ("E1/E2/E3 maturational sequence necessity.") names the three engines explicitly
  > but has no ARC in depends_on. Choose emergent_from: [ARC-001, ARC-002, ARC-003] (the
  > engines whose maturation is being ordered) or [ARC-019] (the developmental-curriculum
  > substrate that specifies the ordering) or both. Add to depends_on accordingly.
