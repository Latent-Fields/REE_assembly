Status: processed
Intake: evidence/planning/thought_intake_2026-08-27_developmental_integration_and_readiness_programme.md
Claims registered: GOV-CAPCONTRACT-1, ARC-135

<!--
STAGE 1 RAW CAPTURE. Imported verbatim 2026-08-27T19:25Z from
~/Dropbox/.../Downloads/REE_developmental_integration_program_2026-08-27_revised.md
(session thought-ingest-devintegration-20260827). Nothing below this comment was
edited on import. This document is a SYNTHESIS/PROGRAMME capture rather than a
short raw thought; it is non-authoritative per its own section 20 and registers
nothing by itself.
-->

# REE Developmental Integration and Readiness Programme

**Status:** repo-aligned project-development synthesis / candidate integration programme  
**Date:** 2026-08-27  
**Scope:** full Reflective–Ethical Engine (REE) lineage, with REE-v3 as the current experimental organism/substrate  
**Purpose:** consolidate the developmental threads exposed by the August 2026 review **without duplicating developmental architecture, claims, metrics or control machinery already present in the repositories**.

**Repository alignment checkpoint:** reviewed against the live `Latent-Fields/REE_assembly` and `Latent-Fields/ree-v3` repositories on 2026-08-27. At the final audit pass, the observed heads were `REE_assembly@59cfa1b8` and `ree-v3@8bfcf198f`. Treat later repository state as authoritative if it conflicts with this snapshot.

**Import semantics:** this is a synthesis and programme document. It does **not** by itself register claims, change version routing, authorise substrate builds, promote/demote evidence, or supersede canonical architecture documents. New work should enter REE through the existing thought/claim/governance/experiment machinery.

---

## 0. Repository-audit correction to the originating discussion

The discussion that produced the first version of this document reached a useful conclusion but initially understated how much of the proposed programme already exists in REE.

The repository already contains, among other things:

- a canonical **developmental curriculum** (`docs/architecture/developmental_curriculum.md`, ARC-019 and related claims), including infant, childhood/play and later-stage sequencing;
- a canonical **Developmental Needs Register** (`docs/architecture/developmental_needs_register.md`) and quantitative companion (`developmental_metrics.md`), with explicit gate criteria, failure modes, stage coverage and backward traceability;
- an eight-criterion **infant -> childhood competence gate**, including `z_goal`, spatial coverage, residue coverage, action entropy/context sensitivity, harm/benefit balance, post-sleep retention, trajectory diversity and competence progress, plus a perseveration false-pass check;
- the principle that **competence should precede authority**, already represented by ARC-120 and concretely by developmental gates such as ARC-042 / DEV-NEED-008;
- a **developmental-readiness audit framework** (`developmental_readiness_investigation_2026-08-12.md`) that scores mechanisms from Level 0 source-existence through Level 7 longitudinal developmental necessity;
- a refined **causal-reach / installability framework** (ARC-130, ARC-131) distinguishing representation, endogenous recruitment, local operation, competitive authority, committed throughput, ecological consequence and retention/generalisation;
- a live-wired **metacognitive coalition/topology controller** (SD-091 / MECH-481), not merely a forgotten idea: its substrate and eight consumer sites are implemented in REE-v3, while its falsifier is blocked by the lack of a suitable competent, online-adapting organism/harness;
- structured curiosity and learning-progress machinery (MECH-314 family) plus a registered competence-based intrinsic-motivation candidate (MECH-455);
- explicit **non-oracular intervention** concepts already registered in two distinct domains: GOV-INTERVENE-1 for experimental diagnosis and INV-103 for runtime evidence ingestion;
- an existing **event-sourced status/history plane**, where append-only evidence/decision events are authoritative and current state is a regenerable projection;
- substantial sleep, ContextMemory, long-life and organism-level behavioural instrumentation already in flight;
- a **canonical-profile mechanism and admission doctrine** created specifically because “REE-v3” otherwise denotes several non-equivalent instantiated organisms (bare defaults, script-specific flag bundles, historical architecture epochs, and curated profiles). The currently frozen `ree_v3_baseline@v0` remains a placeholder with zero overrides, so the mechanism exists but a genuinely populated canonical V3 organism has not yet been admitted.

Therefore this programme should **not** be interpreted as a request to create a new developmental architecture beside the existing one.

Its role is narrower and, arguably, more useful:

> **Turn REE's existing developmental commitments, readiness concepts and control mechanisms into a coherent organism-level integration programme that can explain and unblock the live V3 competence/causal-reach failures.**

The key question is no longer "should REE have development?" It already does architecturally. The question is:

> **Can the currently implemented organism actually traverse those developmental obligations, and can we measure where the traversal stops?**

### 0.1 Novelty disposition of the discussion threads

This is the quickest guard against accidentally re-registering ideas that are already present.

| Discussion thread | Repo-aligned disposition | What remains genuinely useful/new |
|---|---|---|
| Developmental competence scoreboard | **Already substantially present** through the curriculum, DEV-NEED register/metrics, Level 0–7 readiness and ARC-130 causal reach. | A **derived Developmental Integration View** joining those projections around organism-level capabilities. |
| Developmental / metacognitive controller | **Partly already built.** ARC-005 control, mode/write gates and SD-091/MECH-481 coalition control already provide substantial machinery. | Test a **competence-to-authority bridge** first; add a persistent developmental governor only if existing control cannot express the required hysteresis/scheduling. |
| Policy–representation co-development | **Already represented in components** (SD-056, MECH-457, MECH-314*, MECH-455 and developmental repertoire gates). | Longitudinal **joint assays in the same developing organism** rather than another representation or motivation module. |
| Function-shaped perceptual categories / object boundaries | **Partly represented** in developmental grounding, context, categorisation/granularity and newer compression work. | Test whether functional consequence changes reorganise distinctions **without labels/oracles**; avoid minting a new claim until overlap is re-audited. |
| Heterogeneous/interdependent memory | **Architecturally present as multiple systems.** | Cross-memory **functional competence assays** and dependency mapping; do not collapse to one memory score. |
| Agentic memory writing | **Broad generic write eligibility already exists** (MECH-094/261); V4 allocation-policy work also exists. | In V3, validate ContextMemory **content-sensitive address → retrieval → behavioural use**, then ask whether additional selection policy is truly missing. |
| Non-oracular injections | **Already formalised** in GOV-INTERVENE-1; runtime non-oracular evidence has separate INV-103 scope. | Apply the taxonomy systematically to developmental assays and production-path diagnostics. |
| Sleep as deeper schema reorganisation | **Sleep substrate and developmental/offline commitments already exist.** | Move the success criterion from liveness/reward to **transformational competence** and empirically partition waking vs offline update permissions. |
| Epistemic orienting / “reflect harder” | **Mechanisms exist but recruitment/functional benefit are incomplete.** | Endogenous demand classification, information-seeking and matched typed-coalition benefit. |
| Persistent long-life development | **Partial continuity already exists.** | Make cognitive/body/ecology/plasticity continuity explicit and build a persistent-ecology assay family. |
| “Make sure the right things are turned on” / full-stack organism | **A canonical-profile mechanism already exists**, but `ree_v3_baseline@v0` is still an empty placeholder and experiments commonly assemble their own flag bundles. | Populate/qualify a canonical integrated V3 profile, then add an **experiment capability contract** that records profile + deviations + required mechanisms + actual activation/authority/plasticity. Use an “all-on”/whole-organism run as an integration assay, not as the sole canonical solution. |
| Event-sourced scientific state / state transitions | **Already implemented conceptually and substantially operationally** in the status/history plane. | Reuse that contract for derived developmental state; do not create a rival ledger. |
| Development Atlas | **Not needed as another source of truth.** | Useful if implemented as a generated/derived view over canonical developmental + causal-reach evidence. |

---

## 1. Programme-level diagnosis

REE-v3 increasingly appears **development- and integration-limited rather than simply module-limited**.

This does not mean every apparent failure should be excused as immaturity. The repository's own readiness work explicitly warns against both lazy explanations: do not call REE "a baby" when a mechanism is actually broken, and do not call it "broken" when the system simply cannot yet reach the states required to express a mechanism.

A same-day inter-governance workset regeneration reported **242 work items, only 22 ready and 0 in flight**. That number is not itself a scientific result, but it is consistent with the architectural reading here: much of the frontier is now governed by prerequisites, readiness and integration dependencies rather than by an absence of named mechanisms.

The recurring live pattern is more precise:

1. a mechanism may exist in code;
2. it may be instantiated and locally callable;
3. its inputs may nevertheless be undifferentiated or absent;
4. the organism may not recruit it endogenously;
5. it may operate locally but lack competitive authority;
6. it may alter an internal decision yet fail to reach committed behaviour;
7. changed behaviour may occur in an ecology that cannot reveal the claimed competence;
8. a competence may work in isolation and disappear when installed in the whole organism;
9. an acquired competence may fail to persist through subsequent learning or offline integration.

This is already close to ARC-120 plus ARC-130/131. The proposed programme makes that **the main experimental spine** for the next phase of organism-level work.

### Working programme hypothesis

> **Many recurrent REE-v3 ceiling effects are different failures along a developmental causal-reach chain. They should become more tractable if experiments first establish the prerequisite organismal competencies, then test whether those competencies acquire authority, throughput, ecological consequence and retention.**

This hypothesis is falsifiable. If the prerequisites are demonstrably mature and the target mechanism still fails, the explanation must move downstream or elsewhere.

---

## 2. Do not build a second scoreboard: unify the existing developmental projections

The first draft proposed a new "developmental competence scoreboard". The repository audit changes that recommendation.

REE already has **three complementary maturity representations**:

1. **Developmental stage gates** in `developmental_curriculum.md` and `developmental_metrics.md`;
2. **DEV-NEED traceability** in `developmental_needs_register.md`;
3. **Levels 0-7 developmental readiness / ARC-130 causal reach**, which ask how far a mechanism has actually become part of the organism.

The useful new artifact is therefore not another canonical registry. It is a **derived Developmental Integration View** over those existing sources.

### 2.1 Proposed derived view

For each organism-level capability, display:

| Dimension | Question |
|---|---|
| Canonical stage / DEV-NEED | Where does REE already say this belongs developmentally? |
| Substrates / claims | Which existing mechanisms are expected to support it? |
| Readiness / causal reach | What is the furthest demonstrated level: source, reachable, non-degenerate, recruited, authoritative, behavioural, ecological, retained? |
| Behavioural assay | What whole-organism behaviour would demonstrate the capability? |
| Internal diagnostics | What telemetry can localise failure without becoming the success criterion itself? |
| Developmental dependency | Which capacities must already be good enough? |
| Current evidence | Which experiments/autopsies actually establish each link? |
| Live blocker | What prevents the next level from being tested? |
| V3/V4 scope | Is this executable in V3 or deliberately parked for later generations? |

This should be **derived**, not hand-maintained as a rival source of truth.

### 2.2 Why this is different from the existing register

The Developmental Needs Register answers: **what developmental conditions does the architecture require?**

The readiness/causal-reach frameworks answer: **how far has a particular mechanism been demonstrated to work?**

The proposed view answers a third question:

> **Which combination of existing developmental needs and mechanisms currently yields an organism-level competence, and where does that competence fail to become behaviourally real?**

That is the missing integration projection.

---

## 3. Organism-level capabilities remain the correct primary experimental unit

The repo audit strengthens rather than weakens the original shift from module-centric to organism-centric assays.

Internal mechanisms are indispensable for diagnosis, but the primary success criterion should often be a **stable functional capacity of the organism**.

A useful general assay structure is:

1. define a functional capability;
2. map it to existing DEV-NEEDs / claims rather than inventing new prerequisites casually;
3. establish readiness of the relevant production pathway;
4. provide a fair, preferably non-oracular developmental opportunity;
5. measure the behavioural capability;
6. use lesions, oracle controls, non-oracle perturbations and internal telemetry to locate the causal-reach boundary;
7. test whether the competence survives installation, later learning and held-out conditions.

This naturally reuses ARC-130/131 and GOV-PATHVALID-1 rather than creating a new experimental philosophy.

### 3.1 Experimental organism identity and capability contract

The discussion after this document was first drafted exposed a more operational version of the same problem:

> **Before interpreting an experiment, establish that the organism instantiated for that run was actually capable of expressing the faculty being tested.**

This is not merely a documentation preference. REE-v3 currently has many default-off or context-dependent mechanisms, a placeholder canonical profile with no admitted overrides, experiment-specific configuration bundles, and long-life drivers in which some forms of learning are deliberately disabled. A scientifically negative-looking result can therefore arise because the target mechanism was absent, unreachable, competitively powerless, or non-plastic rather than because the proposed faculty failed.

The repository already contains the right base mechanism: `canonical_profile.py`, canonical-profile fingerprints, cross-epoch aggregation guards, and `canonical_profile_admission_criteria.md`. The missing layer is to bind **experiment meaning** to **instantiated organism capability**.

Each organism-level experiment should therefore emit or derive an **Experiment Capability Contract** containing at least:

| Field | Question |
|---|---|
| Canonical profile | Which named/frozen organism profile did the run instantiate? |
| Explicit deviations | Which flags/parameters differ from that profile, and why? |
| Required capabilities | Which developmental/functional capabilities must already exist for the target hypothesis to be testable? |
| Required mechanisms | Which concrete substrates/claims are expected to carry those capabilities? |
| Activation/reachability | Were those mechanisms constructed, enabled and reached on the production path? |
| Engagement | Did they actually fire/use their decisive readouts often enough for the test to be non-vacuous? |
| Competitive authority | Could their output influence the relevant arbitration surface at the scale present in this run? |
| Plasticity mode | What was allowed to change: policy/value parameters, E1/E2 representations, memory state, residue/EMA state, sleep updates? |
| Gradient capability | If online learning is required, were gradients enabled, were the relevant parameters in an optimizer, and did parameter deltas confirm an actual update path? |
| Commitment/behaviour throughput | Could any local change reach fresh committed action rather than a stale or downstream-blocked choice? |
| Ecological opportunity | Did the environment provide the events/opportunities needed to express the capability? |
| Interpretation result | `interpretable`, `capability_precondition_unmet`, `mechanism_unreached`, `nonplastic_misfire`, `authority_floor_unmet`, or another explicit route. |

The critical rule is:

> **A run should not count as negative evidence for a learning- or development-dependent claim if the required learning pathway was not plastic during that run. “It did not learn” and “it could not have learned” are different scientific outcomes.**

This generalises beyond gradients. A required mechanism that was default-off, never recruited, or many orders of magnitude below the competitive authority floor likewise makes the run a capability/precondition diagnostic rather than a clean falsifier.

#### Canonical integrated organism versus literal “all-on”

There is real value in periodically running a whole-organism profile in which every **admitted, mutually compatible mechanism appropriate to the developmental stage** is active. This is the closest rigorous analogue of “run it with everything turned on” and is useful for:

- discovering config drift and default-off omissions;
- testing installability and mechanism interactions;
- checking whether isolated competencies survive full-stack composition;
- providing an observational Fishtank organism whose configuration has a stable identity across time.

But literal indiscriminate `all flags = True` should not become the definition of REE. Some flags are diagnostic-only, mutually interacting, superseded, V4-deferred, or developmentally inappropriate. The canonical-profile admission doctrine already recognises this. The right target is therefore:

> **a curated, versioned integrated-organism profile, plus experiment-specific justified deviations, with automatic preflight verification of the capabilities each experiment assumes.**

This turns “which REE did this experiment actually test?” into a machine-answerable provenance question.

---

## 4. Capability lanes: orthogonal to the existing stage model, not a replacement for it

The first draft proposed a ten-step capability sequence. That risks becoming a second developmental ladder beside ARC-019.

A better representation is **capability lanes that mature across the existing developmental stages**.

### 4.1 World/perceptual differentiation

Functional question:

> Does the organism distinguish states, objects or contexts when the distinction changes prediction, affordance, harm, benefit or control?

This aligns with existing sensorimotor grounding, object persistence/binding, ARC-042 E1/E2 readiness and newer compression/granularity work.

Candidate organism-level signatures:

- behaviour changes between superficially similar states with different consequences;
- generalisation occurs across superficially different states with equivalent consequences;
- context changes alter prediction and action before explicit reward labels are supplied;
- representational distinctions become more useful, not merely more numerous.

### 4.2 Controllability / affordance competence

Functional question:

> Has the organism learned which aspects of the world its actions can change and which actions realise useful affordances?

This should connect action-conditional prediction, actor-critic/action learning, wanting/goal systems and developmental exploration.

### 4.3 Predictive representation competence

Functional question:

> Does E1/E2/`z_world` contain differentiated, action-relevant structure that downstream systems can actually use?

This must distinguish:

- non-collapsed latent numbers;
- prediction competence;
- action-adequate representation;
- downstream-effective representation.

The MECH-457 / SD-056 lineage already demonstrates why these are not equivalent.

### 4.4 Policy repertoire competence

Functional question:

> Can the organism acquire multiple useful strategies and deploy them conditionally rather than converging on a narrow behavioural loop?

Relevant readouts already exist or are adjacent to existing developmental metrics: action entropy, context-sensitive entropy, perseveration, trajectory diversity, strategy switching and competence retention.

### 4.5 Functional memory competence

Functional question:

> Can the organism preserve, retrieve, reorganise and use past information in a way that changes future prediction or action?

This must remain plural: ContextMemory, hippocampal trajectories, residue, E1 persistent state, policy and representational categories are not one memory system.

### 4.6 Epistemic / orienting competence

Functional question:

> When an important uncertainty is resolvable, does the organism recruit the appropriate processing and obtain information that reduces the uncertainty?

The current orienting and coalition-control lineages make this directly testable once a competent, adapting harness exists.

### 4.7 Counterfactual competence

Functional question:

> Can internally generated alternatives change future behaviour without direct repetition of the original experience?

This should map onto the existing hippocampal/counterfactual/play architecture rather than becoming a new generic counterfactual module.

### 4.8 Offline integration competence

Functional question:

> Does offline processing transform relations among memories/representations in ways that later alter waking cognition?

The success criterion should distinguish structural reorganisation from mere replay liveness or performance improvement.

### 4.9 Metacognitive / coalition-regulation competence

Functional question:

> Can the organism recognise a processing demand and recruit an appropriate cognitive coalition or alter its processing policy accordingly?

Importantly, **the coalition controller already exists**. The live gap is endogenous recruitment plus a competent online-adapting organism on which type-specific recruitment can improve behaviour.

### 4.10 Long-horizon organismal coherence

Functional question:

> Do the above capabilities form a persistent but revisable developmental history rather than a series of unrelated experimental episodes?

This requires resolving what "continuous life" means in V3 and distinguishing within-life state change from between-run training.

---

## 5. The controller question changes: first test whether existing control machinery is enough

The first draft described a possible new developmental controller. The repository audit makes "build a new controller" premature.

REE already has:

- control-plane parametric modulation;
- mode-dependent write/gain machinery;
- commitment/readiness gates;
- structured curiosity;
- sleep-state control;
- SD-091 / MECH-481 coalition/topology control, which can selectively recruit/suppress existing subsystems;
- developmental stage/gate concepts;
- competence-before-authority commitments.

The more precise missing object is a **competence-to-authority bridge**.

### 5.1 Question to test before adding a module

Can existing mechanisms jointly implement the desired developmental physiology if they receive a derived competence/readiness signal?

For example, can demonstrated competence alter:

- whether a coalition can be recruited;
- which downstream mechanisms receive authority;
- exploration/exploitation balance;
- plasticity / learning-rate regime;
- commitment thresholds;
- sleep/offline restructuring eligibility;
- reopening/deferment after uncertainty;
- retention/protection of a newly acquired competence?

If this can be expressed by ARC-005 + SD-091/MECH-481 + existing gates, **do not add another central controller**.

Only if the mapping itself requires persistent state, hysteresis, cross-capability arbitration or developmental scheduling that the existing control plane cannot express should a distinct controller be proposed.

### 5.2 Existing SD-091 result is especially informative

The MECH-481 four-arm falsifier scaffold already demonstrates:

- the coalition substrate is live and ablatable;
- typed templates are distinct;
- the coalition can alter the action stream/cost footprint;
- the current naive harness cannot test type-specific performance recovery because the agent lacks appropriate goal-directed, online-adapting competence.

That is almost a worked example of this programme's thesis. The next move is not a more elaborate coalition controller. It is a developmental/adaptation harness in which recruitment can solve something the organism is capable of learning online.

---

## 6. Policy, perception and representation should be studied as a coupled developmental loop

This remains one of the strongest synthesis points.

A collapsed policy creates an impoverished developmental dataset. An impoverished representation constrains policy learning. Perceptual/category boundaries determine what the organism treats as equivalent; policy determines which consequences reveal whether those equivalence classes are useful.

The loop is therefore:

**experienced structure -> representation/perception -> policy -> visited transitions -> learning signal -> revised representation/perception**.

### 6.1 This is already partly represented in REE

Relevant existing lines include:

- developmental sensorimotor grounding and behavioural-repertoire gates;
- ARC-042's requirement that E1/E2 become differentiated before E3 receives meaningful authority;
- SD-056 action-conditional representation;
- MECH-457 actor-critic/action-learning and co-shaping work;
- MECH-314 structured curiosity and MECH-455 competence-based intrinsic motivation;
- MECH-496/INV-101 representational categorisation/granularity work;
- recent compression/decompression and attractor claims (MECH-507 onward, V4-scoped).

The gap is not recognition of the loop. It is a **joint longitudinal assay** that measures both sides while the same organism develops.

### 6.2 Functional perception rather than similarity clustering

A perceptual grouping should earn persistence partly because it supports useful prediction, action, harm avoidance, benefit pursuit, controllability or generalisation.

This does **not** mean current goals directly dictate perception. The important distinction is between:

- an externally supplied label saying "these are the same object"; and
- long-run functional pressure making one partition of experience more predictive/useful than another.

A good developmental assay would change the functional consequences of a distinction without telling the organism what the new category boundary is, then test whether perception/representation and policy co-adapt.

### 6.3 Learning progress is already an architectural thread

Do not register "learning progress" as a new idea. REE already has MECH-314c and MECH-455-related work.

The useful question is whether the learning-progress / competence-progress signals:

- are genuinely per-context or per-candidate rather than broadcast/inert;
- influence what the organism samples;
- prevent polished monostrategy collapse;
- generate an emergent curriculum;
- remain useful when installed alongside the rest of the motivational/control stack.

---

## 7. Heterogeneous memory: study interdependence and functional use, not a universal memory score

The discussion correctly identified that "memory" in REE spans several different substrates:

- ContextMemory / cue-addressed contextual storage;
- hippocampal path/trajectory memory and replay;
- E1 persistent predictive state;
- E2 learned action-conditional predictive structure;
- residue / affective history;
- policy weights and value structure;
- learned perceptual categories / attractor structure;
- environmental persistence that stores consequences outside the agent.

They should not be forced into one success metric or assumed to be cleanly separable.

### 7.1 ContextMemory: revise the live question

The live ContextMemory problem is **not simply "we need a learned write address"** anymore.

As of 2026-08-27:

- bias and refractory mechanisms exist but mainly solve occupancy;
- `gumbel_learned` now introduces a dedicated trainable write-address policy with a verified gradient path;
- content discrimination remains unvalidated;
- functional downstream benefit remains unresolved;
- sleep-dependent claims remain blocked until the corrupting write-path issue is genuinely validated.

So the next competence sequence should be:

1. content-sensitive addressing;
2. stable/useful retrieval;
3. downstream behavioural use;
4. only then causal sleep/consolidation claims that depend on it.

### 7.2 Do not duplicate existing write-gating architecture

REE already owns substantial **whether-writing-is-allowed** machinery through MECH-094 / MECH-261 and related mode-conditioned gates. A separate V4 memory-allocation line explicitly asks how to regulate integrate/separate/partial-overlap topology.

Therefore the V3 programme should not casually add another generic "write/no-write" mechanism to ContextMemory.

Instead ask:

- Is the existing write eligibility reaching ContextMemory appropriately?
- What selects **content and address** within an eligible write?
- Is the resulting trace retrievable and behaviourally useful?
- How do ContextMemory, hippocampal memory, residue and E1/E2 representations constrain each other's updates?

### 7.3 Cross-memory competence assays

A useful memory assay should often require more than one system, for example:

- an experience is encoded contextually;
- a later hippocampal/counterfactual process uses it;
- offline integration changes its relation to other experiences;
- subsequent perception or policy changes in the appropriate context.

The point is not to prove that one memory module is "pure." It is to identify which memory interactions are necessary for a stable organism-level capability.

---

## 8. Non-oracular intervention: preserve the distinction between runtime evidence and experimental diagnosis

The originating conversation used "non-oracular injections" as a developmental-testing idea. The repo now has a more precise taxonomy.

### 8.1 Experimental domain: GOV-INTERVENE-1

A non-oracle diagnostic changes a suspected variable without supplying the answer the organism is meant to discover.

It should be classified independently by construction:

- **oracle vs non-oracle**: whether privileged target-correct information is imported;
- **silky vs oddly composed**: whether the intervention minimally perturbs a natural state or deliberately creates a rare composition to stress-test causal structure.

This is ideal for developmental assays because it can separate:

- missing representation;
- bad threshold/scale;
- timing failure;
- absent downstream sensitivity;
- production-path failure;
- shortcut dependence.

### 8.2 Runtime domain: INV-103

A separate V4 invariant now says external evidence should not directly set E1's truth-state; it must pass through ordinary provenance, precision and learning-eligibility machinery.

Do **not** conflate that runtime invariant with GOV-INTERVENE-1's experimental-method taxonomy.

### 8.3 Programme use

For each organism-level assay, explicitly state:

- what the organism receives naturally;
- which positive control is oracle-assisted;
- which perturbations are non-oracular;
- whether each intervention is on-manifold, silky or deliberately oddly composed;
- what causal edge it is meant to diagnose.

---

## 9. Sleep/offline integration: the programme should move from liveness to transformational competence

The first draft's conceptual direction remains useful, but the live substrate has moved.

### 9.1 Do not repeat the old "sleep cannot occur in a continuous life" diagnosis as current truth

That was a real August 12 finding, but it has since been addressed by **SD-SLEEP-ENTRY-PRESSURE**:

- a time-integrating entry-pressure accumulator now exists;
- a refractory floor bounds repeated firing;
- V3-EXQ-933a validated sustained sub-threshold accumulation and bounded supra-threshold firing in a true continuous-life driver.

So within-life sleep entry is now mechanically possible.

### 9.2 The major causal sleep experiment is still legitimately blocked elsewhere

The matched-arm sleep/deprivation design remains valuable, but ContextMemory write addressing is on its causal path. Until the write-path policy is validated, a null could still be manufactured by defective memory storage.

That block is scientifically appropriate.

### 9.3 Transformational sleep competence

Once the storage path is valid, sleep should be tested for transformations such as:

- context/schema reorganisation;
- cross-episode integration;
- changed retrieval relationships;
- altered generalisation;
- recalibrated confidence/precision;
- revised perceptual equivalence classes;
- counterfactual transfer;
- weakening/pruning of misleading structure.

The key contrast is not simply "sleep ON performs better." It is:

> **Did offline processing change the structure through which later waking experience is interpreted or acted upon?**

### 9.4 Waking versus offline plasticity should remain an empirical partition

The useful hypothesis from the discussion is that some large-scale schema revisions may be safer/effective offline because waking cognition depends on a coherent currently active model.

But do not hard-code every deep update as sleep-exclusive. The correct programme is to classify update types by:

- whether they can complete during waking;
- whether they can begin during waking but require offline completion;
- whether offline conditions make them more effective;
- whether some disruptive transformations should be prohibited during active control.

This can connect to MECH-511/deep-update eligibility and the existing sleep-mode/control architecture rather than spawning an isolated sleep-plasticity subsystem.

---

## 10. Metacognition and epistemic orienting: recruitment is the live edge

The discussion's "rudimentary metacognitive controller" is not missing in the simple sense.

REE already contains distributed confidence/precision/control mechanisms and the explicit SD-091/MECH-481 coalition controller.

The important missing edges are:

1. **monitor/classify**: detect what kind of processing problem is occurring;
2. **endogenous recruitment**: request the appropriate coalition without the experiment driver telling it which coalition to open;
3. **adaptive operation**: recruited systems must be capable of changing their state/model/policy online;
4. **behavioural recovery**: the recruitment should resolve uncertainty or improve action in a type-specific way;
5. **cost/selectivity**: typed recruitment should outperform undifferentiated "reflect harder" activation.

### 10.1 Orienting assay

A strong future organism-level assay would present a consequential ambiguity where the organism can perform an information-gathering action.

Success requires more than an orienting spike:

- uncertainty/problem type becomes discriminable;
- the appropriate coalition/control policy is recruited;
- the organism samples informative evidence;
- uncertainty or model conflict falls;
- subsequent action changes appropriately;
- a mismatched coalition or generic gain increase performs worse or costs more.

That directly links orienting, SD-091/MECH-481, policy competence, representation updating and causal reach.

---

## 11. Long-life development: distinguish persistence of mind, body, ecology and plasticity

The Fishtank work already created a useful form of continuity, but the semantics are unusual.

In the 906 lineage, cognitive/affective/mnemonic state persists across segment boundaries while the environment resets local layout/body health. A `health_depleted` boundary therefore regenerates the body/environment around a persisting cognitive system rather than constituting organismal death.

This matters because "long life" contains at least four separable continuities:

1. **cognitive state continuity**;
2. **parameter/plasticity continuity**;
3. **body/homeostatic continuity**;
4. **ecological/world continuity**.

V3 currently provides some but not all.

### 11.1 Within-life plasticity is a separate blocker

The August developmental-readiness investigation found that standard observational-life drivers run under `torch.no_grad()`. Therefore more observed ticks do not equal more gradient-based learning.

A long-life developmental programme must explicitly choose which forms of adaptation are meant to occur:

- residue/EMA/buffer/non-parametric state change;
- online policy/value learning;
- representation learning;
- memory consolidation;
- offline updates.

Otherwise an experiment can watch a frozen policy for a long time and mistake duration for developmental opportunity.

This should be made a **preflight invariant**, not left to post-hoc interpretation. If an experiment's claimed outcome depends on within-life gradient learning, its capability contract should fail closed unless the relevant learning path is actually enabled. At minimum that means checking `torch.is_grad_enabled()` at the relevant phase, optimizer membership for the intended trainable parameters, and a small parameter-delta/gradient-flow witness. Conversely, a deliberately `no_grad` Fishtank run should label itself explicitly as an **observation of a fixed parametric organism with non-parametric state adaptation only**, not as a general developmental-learning assay.

### 11.2 Persistent ecology successor

A useful successor should preserve one world/organism relationship long enough to separate:

- age from layout luck;
- learning from reset effects;
- injury/recovery from death;
- memory accumulation from environmental regeneration.

This does not require abolishing segmented experiments. It requires a distinct **persistent-ecology assay family** whose semantics are explicit.

---

## 12. Governance/provenance: reuse the existing event-sourced architecture

The first draft proposed making state transitions "first-class events." That is already substantially implemented for scientific/governance state.

`status_history_plane_separation_design.md` explicitly establishes:

- append-only autopsies, manifests and decisions as authoritative events;
- a pure projector that derives current `live` status from an event slice;
- `status_snapshot/v1` projections appended back into history;
- generated human-readable history sidecars;
- non-destructive migration and drift checks.

Therefore **do not create another generic transition ledger**.

### 12.1 What remains useful

Apply the same principle consistently where it is not yet authoritative:

- task/claim/chip coordinator state changes;
- materialisation to Git/GitHub;
- cutover/fallback provenance;
- any future developmental-integration view.

The default design rule should be:

> **events/history are authoritative where the fact cannot be re-derived; live dashboards/registries are projections where they can.**

### 12.2 Current TASK_CLAIMS/TASK_CHIPS migration status

The migration plan has advanced since the first draft:

- Phase 1 shadow mirroring is deployed and soaking with drift instrumentation;
- Phase 2 build has **started in parallel** behind a default-OFF flag;
- actual claim-authority cutover still waits on the soak evidence plus a separate go-live decision;
- the previously proposed Mac-tunnel trailing-rate criterion is **no longer a pre-cutover gate**; it was explicitly moved to post-cutover monitoring because the first-class Git fallback degrades a tunnel outage to the current behaviour rather than a hard/data-safety failure;
- Git/GitHub remain materialisation/fallback rather than disappearing;
- this migration is specifically about `TASK_CLAIMS.json` / `TASK_CHIPS.json`, not a blanket claim that every repository write has already moved behind one universal committer.

The developmental programme should not entangle itself with this migration beyond using the eventual coordinator as a reliable source for task/claim/chip state.

### 12.3 Science-throughput governance remains important

The recent housekeeping-treadmill episode shows that even a safe governance machine can allocate effort poorly.

Continue measuring:

- experiment supply/queue depth;
- scientific vs housekeeping work creation;
- time spent resolving repeated infrastructure state;
- blocker centrality removed per unit work;
- whether new governance machinery actually reduces research friction.

---

## 13. Proposed integration workstreams

These workstreams are **not new architecture modules by default**. They are integration/research programmes that should reuse existing claims and mechanisms wherever possible.

### Workstream A — Developmental Integration View

Build a derived capability -> DEV-NEED -> substrate -> readiness/causal-reach -> assay -> blocker projection.

**Do not:** create a second canonical developmental registry.

### Workstream B — Competence-to-authority experiments

Test whether existing developmental gates and SD-091/control-plane machinery can make authority contingent on demonstrated competence.

**Decision gate:** only propose a new developmental controller if existing machinery cannot express the required mapping.

### Workstream C — Policy/representation co-development

Run longitudinal assays in which policy diversity, predictive discrimination and action-relevance are measured together in the same organism.

Use existing SD-056, MECH-457, MECH-314*, MECH-455 and developmental metrics rather than a parallel intrinsic-motivation stack.

### Workstream D — Heterogeneous functional memory

Validate ContextMemory content/addressing and retrieval, then test cross-memory organism-level capabilities.

Keep V4 overlap-topology allocation policy separate from V3 critical-path repair unless V3 evidence creates a direct need.

### Workstream E — Offline transformational competence

After memory-path validation, test whether sleep changes representational relations, not merely cycle liveness or reward.

### Workstream F — Epistemic recruitment/metacognition

Use the existing coalition controller. Build the missing endogenous monitor/classifier and a competent adapting assay only when the causal prerequisites are explicit.

### Workstream G — Persistent developmental ecology

Create a long-life assay family with explicit cognitive, body, ecological and plasticity continuity semantics.

### Workstream H — Governance/provenance integration

Reuse status/history event sourcing and complete the coordinator migration; ensure developmental views are projections over existing authoritative records rather than new manual state.

### Workstream I — Experimental organism configuration and plasticity integrity

Use the existing canonical-profile machinery to define the organism being tested, then add a preflight capability contract to every developmental/organism-level experiment.

Near-term tasks:

1. run the canonical-profile admission process and populate a first **integrated V3 profile** rather than leaving `ree_v3_baseline@v0` as an empty overlay;
2. make experiment manifests record canonical profile hash plus explicit deviations;
3. allow experiments to declare `requires_mechanisms`, `requires_capabilities`, and `requires_plasticity`;
4. automatically compare those requirements with actual construction/flags, decisive-readout engagement, optimizer membership/gradient mode, and authority/readiness diagnostics;
5. self-route unmet requirements to a non-falsifying status before scientific interpretation;
6. maintain at least one periodic **whole-organism integration/Fishtank run** under the populated canonical profile to detect config drift, composition failure and competence loss.

This is not a new cognitive module. It is an experimental-integrity layer ensuring each experiment actually tests the organism it claims to test.

---

## 13.1 Live integration matrix: what to do with the main threads now

| Thread | Already established | Live gap | Recommended next move | Avoid |
|---|---|---|---|---|
| Developmental maturity | Curriculum, DEV-NEEDs, quantitative gates, readiness and causal-reach frameworks | No single view joins capability, prerequisite, reach and live blocker | Generate a small derived integration view for 3–5 live capabilities | New hand-maintained scoreboard |
| Coalition/metacognitive control | SD-091/MECH-481 substrate, live wiring, distinct typed templates | Endogenous recruitment + suitable online-adapting competence/harness | Build/identify a fair adapting task and typed-demand producer; then reuse the existing falsifier scaffold | More coalition complexity before a fair test |
| Policy/representation | SD-056, MECH-457, curiosity/competence progress lines | Longitudinal co-development not demonstrated as an organismal capability | Same-organism joint training/measurement with held-out transfer and anti-monostrategy checks | Treating latent variance or action entropy alone as competence |
| ContextMemory | Three write-address mechanisms; learned tagger has real gradient path | Learned **content discrimination** and functional read/use not demonstrated | Validate content-conditioned address; then retrieval/bank-content ablation; then behavioural utility | Occupancy as proof of addressing; causal sleep test before memory path clears |
| Sleep | Rich sleep substrate; within-life entry-pressure fix validated | Structural transformation after sleep not cleanly demonstrated; memory dependency still open | After memory clearance, matched-arm structural-reorganisation assay | “Sleep fired” or reward delta as sufficient evidence |
| Orienting/information seeking | Defensive orienting and coalition machinery do something measurably | Trigger/valence alignment and information-gathering competence weak/unclear | Consequential ambiguity task where information can be actively acquired and used | Scripted correct coalition as evidence of endogenous metacognition |
| Long life | Persistent cognitive state across segmented runs; survival instrumentation | Ecology/body reset semantics and online plasticity confound development | Explicit persistent-ecology + plasticity-profile successor | Calling more frozen/no-grad observation “development” |
| Experimental organism identity / configuration | Canonical-profile mechanism, profile fingerprinting, admission doctrine and cross-epoch guard exist; `ree_v3_baseline@v0` is frozen | Baseline profile still has zero overrides; script-specific flag bundles can instantiate different “REE-v3” organisms; no universal capability/plasticity preflight | Admit a populated integrated V3 profile; bind each experiment to profile + deviations + capability/plasticity contract; periodically run whole-organism integration assay | Treating bare defaults or arbitrary “all flags on” as canonical; interpreting a run before checking it could express/learn the target faculty |
| Governance | Event-sourced status/history; coordinator migration underway | Remaining contention/materialisation cutover and state-view integration | Complete claim/chip coordinator cutover; keep developmental views derived | Parallel state ledgers or manually duplicated status |

---

## 14. Concrete first deliverables after this repo audit

### Deliverable 1 — Developmental Integration View v0

**Inputs:**

- `developmental_curriculum.md`;
- `developmental_needs_register.md`;
- `developmental_metrics.md`;
- developmental-readiness Levels 0-7;
- ARC-120 / ARC-130 / ARC-131;
- current claims/substrate status and experiment/autopsy evidence.

**Output:** one derived table/view for a small number of live V3 capabilities.

Do not attempt the whole architecture initially.

### Deliverable 2 — Pick three live "blocked by competence" mechanisms and trace them end-to-end

Good candidates:

1. **SD-091 / MECH-481 coalition control** — operator works; competent online-adapting harness/endogenous recruitment absent.
2. **MECH-465 commitment-gate grading** — downstream gate question remains confounded by weak/degenerate upstream representation-policy regimes.
3. **ContextMemory -> sleep** — learned addressing now exists; content discrimination/functional use must clear before causal sleep interpretation.

For each, record the furthest ARC-130 stage actually demonstrated and the next discriminating experiment.

### Deliverable 3 — One organism-level developmental assay

Prefer an assay that requires several existing systems but little new substrate.

**Strong candidate:** consequential ambiguity with optional information acquisition.

It can test:

- environmental differentiation;
- uncertainty/problem detection;
- coalition/orienting recruitment;
- information-seeking;
- online representation/policy update;
- subsequent decision improvement;
- matched vs mismatched/generic control.

However, only choose it if the adaptation machinery needed to benefit from new evidence is actually live. Otherwise begin earlier with a policy-representation co-development assay.

### Deliverable 4 — Canonical integrated V3 profile + Experiment Capability Contract

Use the existing canonical-profile admission doctrine rather than inventing another config standard.

**Part A — populate an integrated profile.** Re-run the admission criteria against the live corpus and curate the mechanisms that are sufficiently implemented, exercised, non-degenerate and mutually compatible to define a named V3 organism. Freeze the resulting profile and constitution through the existing machinery. Do not silently edit the placeholder `ree_v3_baseline@v0`; create/update a profile version through the canonical admission process.

**Part B — preflight every developmental experiment.** Add a small manifest/preflight layer that compares what the experiment **requires** with what the instantiated organism **actually provides**. It should cover:

- profile name/hash and explicit deviations;
- required mechanisms/capabilities;
- enabled/constructed/reached state;
- decisive-readout engagement/non-degeneracy;
- competitive-authority/readiness floors where applicable;
- learning mode (`train`/`eval`, `torch.no_grad`/grad enabled);
- intended trainable parameter groups and optimizer membership;
- gradient/parameter-delta witness when online learning is part of the hypothesis;
- relevant memory/sleep/non-parametric update permissions;
- ecological opportunity and commitment-throughput checks.

A failed preflight should self-route the run as a **mis-instantiated or capability-precondition diagnostic**, not as negative claim evidence.

**Part C — whole-organism integration assay.** Maintain a periodic long-life/Fishtank run of the populated canonical integrated profile. Its purpose is not to prove that “everything works”; it is to detect:

- default-off/config drift;
- installability failures;
- interactions among individually validated mechanisms;
- unexpected competence loss over time;
- whether capabilities demonstrated in isolated assays remain present in the integrated organism.

### Deliverable 5 — Within-life plasticity inventory

For each long-life driver/profile, document which state can change during the life:

- parameters;
- policy/value;
- E1/E2 representations;
- ContextMemory;
- hippocampal buffers;
- residue;
- EMAs/control state;
- sleep-dependent updates.

This prevents "longer observation" from being mistaken for "more development."

### Deliverable 6 — Update-transform taxonomy

Map important update types to waking/offline eligibility:

- safe/local waking update;
- waking-start/offline-complete;
- offline-favoured;
- offline-only candidate;
- unknown/test required.

Tie this to existing sleep/control/MECH-511 machinery instead of inventing a standalone rule system.

### Deliverable 7 — Governance reuse check

Before adding any developmental state artifact, verify whether it should be:

- an event in the existing history plane;
- a derived status projection;
- a view over DEV-NEED/readiness data;
- a task/chip coordinator record.

Avoid another manually maintained source of truth.

---

## 15. Explicit V3/V4 boundary

This programme is intended to **unblock V3 organism development and measurement**, not pull every long-term developmental concept into V3.

Keep existing later-generation routing intact unless governance explicitly changes it.

In particular:

- social/caregiver/play/language developmental architecture remains where the canonical claims place it;
- INV-103 runtime non-oracular E1 evidence ingestion is currently V4-scoped;
- contextual memory overlap-topology allocation is V4/V5 groundwork;
- recent compression/decompression/attractor mechanisms are mostly V4-scoped;
- this programme may use their conceptual distinctions when designing V3 measurements, but should not silently authorise their implementation in V3.

The V3 question is narrower:

> **Does the current organism possess the reachable, plastic, behaviourally effective developmental pathway required to test the mechanisms already assigned to V3?**

---

## 16. Open questions after repo alignment

1. Can the existing control plane + SD-091 coalition controller implement competence-contingent authority, or is a persistent developmental governor genuinely missing?
2. Which existing DEV-NEED metrics are ready to become cross-capability organismal measures, and which are still calibration proposals?
3. Which currently implemented mechanisms should be admitted into the first populated canonical integrated V3 profile, and which must remain context-dependent/diagnostic/deferred?
4. Which experiments currently assume capabilities that their own config or learning mode makes impossible to express?
5. What is the earliest V3 capability that can be tested longitudinally under **real online plasticity**, not just frozen observation?
6. How should policy competence and representational competence be co-measured so improvement in one cannot hide collapse in the other?
7. Which ContextMemory competence must clear before causal sleep experiments become interpretable: content discrimination, retrieval, behavioural use, or all three?
8. Which memory interactions are functionally necessary versus merely correlated?
9. Can an endogenous monitor/classifier recruit SD-091 coalitions without becoming an oracle about the correct response?
10. What should “death,” “recovery,” “body reset” and “world reset” mean in persistent-organism experiments?
11. Which V3 null/FAIL results should be revisited first once a populated canonical profile and capability preflight exist?

---

## 17. Near-term programme hypothesis and falsifiers

### Hypothesis

> **A significant subset of current REE-v3 ceiling effects arise because mechanisms are being tested before the production organism has achieved the representation, endogenous recruitment, competitive authority, committed throughput or plasticity required to express them. A developmental-integration programme using existing REE gates and control machinery will convert some of these ceilings into interpretable mechanism tests.**

### What would weaken this hypothesis

- upstream competence/readiness clears robustly but downstream mechanisms remain equally degenerate;
- competence-contingent gating does not change interpretability or developmental trajectory;
- joint policy/representation training improves internal metrics without improving organism-level capability;
- mechanisms that appear blocked by recruitment remain non-functional even under endogenous correct recruitment;
- persistent, plastic long-life assays show no developmental differences beyond environment variance;
- runs that pass the full capability/configuration/plasticity preflight still show the same apparent failures at the same rate, indicating mis-instantiation was not an important source of prior nulls;
- sleep-path validation clears but offline processing produces no structural transformation under well-powered causal tests.

### What would strongly support it

- an existing mechanism such as SD-091 becomes behaviourally useful once a competent/adapting prerequisite harness exists without changing the mechanism itself;
- ContextMemory/sleep effects become detectable only after write-address/content competence clears;
- policy diversity and representational differentiation improve together under a competence-progress curriculum and unlock previously unreachable downstream gates;
- a mechanism's furthest ARC-130 stage advances predictably after its identified prerequisite matures.

---


## 18. Scientific position, external legibility and evidence milestones

The originating conversation was not only about developmental integration. It also stepped back and asked what REE **is**, what V3 already amounts to, where later versions might sit scientifically, and what would have to happen before the work becomes intelligible and interesting to researchers outside the project.

These points matter because the internal programme can become so absorbed in developmental blockers that it loses sight of the larger scientific object.

### 18.1 REE should be treated as an independent research programme, not as a conventional AI product

The public repository already states the relevant position: REE is an **independent research programme** and a **claim-governed experimental system**, not a normal feature-shipping codebase. The important comparison is therefore not “is REE-v3 competitive with a frontier language model?” It is closer to:

- cognitive architecture;
- developmental/embodied artificial intelligence;
- computational neuroscience-inspired agent design;
- artificial-organism research;
- mechanistic alignment / architectures of constrained agency;
- computational psychiatry as a source of falsifiable failure-mode hypotheses.

REE's distinctive scientific question is not primarily “how capable can this model become?” but something closer to:

> **What internal organisation allows an artificial organism to acquire, regulate, remember and take responsibility for action in a world where its own continued existence and the existence of others matter?**

This does not make REE exempt from ordinary AI benchmarks or controls. Quite the opposite: the more unusual the question, the more important matched baselines, behavioural demonstrations, reproducibility and explicit failure records become.

### 18.2 V3 and later REE have different scientific jobs

**REE-v3 should be understood primarily as the current experimental organism and mechanistic proving ground.**

Its scientific value does not depend on being a finished general agent. V3 is where REE can establish whether the proposed pieces actually become:

- differentiated representations;
- useful policies;
- memory-guided behaviour;
- commitment-sensitive action;
- affective/control modulation;
- offline transformation;
- developmental competence;
- integrated organism-level behaviour.

A V3 mechanism can therefore be scientifically valuable even if the whole organism remains poor at a broad task, provided the experiment cleanly demonstrates a causal capability and its limits.

Later versions have a different burden. V4/V5 should increasingly test whether the pieces demonstrated in V3 can become a **co-developing, persistent, socially situated artificial organism** rather than a collection of individually defensible mechanisms. The newer compression/decompression, context-allocation, non-oracular evidence, social/other modelling and deeper developmental threads belong naturally to that larger synthesis.

The development path is therefore not:

`V3 failed -> replace it with V4`

but closer to:

`V3 localises and proves/weakens mechanisms -> later versions inherit only what survives and test stronger organism-level integration claims`.

### 18.3 Do not erase the behavioural wins while diagnosing the competence floor

The present developmental/integration diagnosis should not be allowed to rewrite the project history as “REE has never done anything.”

The evidence corpus contains real PASSes and non-trivial behavioural effects: mechanisms have altered behaviour, real foraging/contact has been achieved in targeted lineages, memory/control pathways have produced measurable causal effects, and multiple internal mechanisms have passed appropriately scoped falsifiers. At the same time, the current broad **whole-stack competence** picture is uneven: the AI-design critique's capability yardstick records at least one trained all-ON condition as surviving while remaining at-or-below the random floor for foraging/goal-reach/planning.

Both statements can be true:

> **REE already exhibits genuine behaviour and causal mechanism effects; REE has not yet demonstrated robust, accumulating, general organism-level competence.**

That distinction is important externally and internally. Small genuine wins should be retained as part of the evidence trajectory rather than hidden because a later integrated benchmark exposes a deeper ceiling.

### 18.4 Build a curated behavioural evidence ladder

The project needs a compact outward-facing answer to “what has REE actually done?”

This should be derived from existing reviewed evidence, not written from memory. A **Behavioural Evidence Ladder** should select a small number of demonstrations at increasing levels:

1. **Mechanism bites** — a targeted manipulation changes the predicted internal/behavioural variable.
2. **Behavioural competence** — the agent performs a meaningful task above an appropriate matched baseline.
3. **Flexible competence** — behaviour changes appropriately after a rule/context/goal change.
4. **Developmental acquisition** — a capability appears through experience and was absent earlier.
5. **Retention/generalisation** — the acquired capability survives time/offline integration and transfers.
6. **Integrated organism competence** — several faculties remain functional together in a canonical long-life organism.
7. **Independent reproduction** — another person/environment reproduces the effect from the public instructions.

Every rung should include:

- the exact run(s);
- the matched control/baseline;
- effect size / uncertainty where available;
- what the result establishes;
- what it explicitly does **not** establish;
- reproduction instructions;
- canonical-profile / substrate identity.

The purpose is not marketing. It is to make the project's actual evidential footprint legible in minutes.

### 18.5 External engagement can start before REE is “finished”

There are at least three useful thresholds for talking to other researchers:

**Now — exploratory contact.**  
REE is already legible enough to ask adjacent researchers for criticism or comparison. The request should be small: inspect one architecture claim, one experiment, or one overlap with their work. The goal is not endorsement.

**After one or two especially crisp organism-level demonstrations — evidence-led contact.**  
A result becomes useful socially when it is easier to inspect than to dismiss: a pre-registered contrast, matched controls, reproducible script, visible effect, and a narrow interpretation. One or two such demonstrations are enough to anchor a substantive conversation even if most of REE remains unresolved.

**After independent reproduction — community-level credibility.**  
Once another person can reproduce or extend a result without the project author steering the run, the conversation changes from “interesting private programme” toward a shared research object.

This suggests a practical external-legibility packet:

- a one-page “What REE is / is not” orientation;
- the public `START_HERE` route;
- one or two best behavioural experiments;
- a minimal reproduction command/notebook;
- a short limitations/known-failures page;
- links to claims/evidence provenance;
- a “questions I would value criticism on” section.

The existing public front matter and Explorer are a strong starting point; the missing part is **curation around a few externally inspectable scientific results**, not more total documentation.

### 18.6 The philosophy made explicit in the discussion

Several principles that have guided the project implicitly were articulated more clearly in the conversation. They should be preserved as **research-method/architectural orientation**, not automatically minted as claims:

> **Cognition should be developed, not merely installed.**

A mechanism existing in source is not the same as an organism possessing the faculty. Development is the process by which representations, skills, memory, regulation and authority become mutually usable.

> **Behaviour is the final arbiter; internal measures are diagnostic instruments.**

Internal telemetry is essential for localisation, but an elegant latent, gate or memory statistic is not organismal competence unless it can eventually alter appropriate behaviour.

> **Structure should follow function.**

Representations and categories should be shaped by what distinctions help the organism predict, control, pursue, avoid, care and learn — not merely by statistical similarity. This is compatible with REE's historical tendency to discover interfaces and differentiate overloaded functions.

> **Competence should precede authority.**

This is already canonical in ARC-120. The conversation extends its practical consequence: experiments should not grant interpretive authority to a mechanism that the organism could not recruit or use.

> **Explicitness beats assumption.**

Mechanism enabled? Gradient flowing? Memory writable? Commitment reachable? Ecology informative? These should become recorded facts, not assumptions inferred after a null result.

> **History and continuity matter.**

The organism carries history through residue, memory, learned representations and developmental state; the research programme likewise treats its own archaeology as evidence. Resetting away history can destroy the phenomenon being studied.

> **The goal is a coherent organism–world relationship, not cleverness in isolation.**

REE's architecture is organised around prediction, action, vulnerability, consequence, other agents and responsibility. Capability is necessary, but capability alone is not the target scientific object.

These principles connect the developmental programme back to the broader REE thesis rather than allowing “developmental readiness” to become a narrow engineering exercise.

### 18.7 Concrete actions from this broader view

Add the following to the project programme alongside the developmental work:

1. **Behavioural Evidence Ladder v0** — mine reviewed experiments for 5–10 strongest behavioural/causal demonstrations and rank them by what they establish.
2. **Canonical integrated V3 demonstration** — once the profile/capability-contract work lands, run a stable whole-organism showcase whose exact organism identity is reproducible.
3. **One developmental flagship experiment** — seek a crisp transition where a capability genuinely appears through experience and survives a held-out test.
4. **External legibility packet** — one-page orientation + best experiment(s) + reproduction path + known limitations.
5. **Reproduction target** — identify at least one experiment simple enough that an outside researcher could reproduce it without understanding the whole architecture.
6. **Adjacent-research map** — maintain a short list of research communities/individual papers whose work genuinely overlaps particular REE mechanisms, so contact can be specific rather than a general “please look at my project.”
7. **Do not wait for completion to seek criticism** — exploratory outreach can begin with narrow questions while stronger public claims remain gated on evidence.

The aim is to let small wins **stack into legibility and reproducibility**, rather than waiting for a single dramatic proof of REE as a whole.

---

## 19. Short handover

The repository audit changes the interpretation of the August discussion in an important way.

REE does **not** need a new developmental philosophy. It already has one. It does **not** need a new generic developmental scoreboard. It already has stage gates, a developmental-needs register, metrics, a Level 0-7 readiness framework and a causal-reach/installability ladder. It does **not** simply lack metacognitive control: SD-091/MECH-481 already provides a live-wired coalition-control substrate. It does **not** lack learning-progress ideas, non-oracular diagnostic concepts, or event-sourced governance. It also already has the beginnings of a solution to configuration identity: a versioned canonical-profile mechanism and admission doctrine. What it does **not yet have is a populated canonical V3 organism plus a universal experiment-level contract proving that the organism instantiated for a run could actually express and learn the faculty under test.**

What REE appears to need now is **integration across those existing pieces**.

The central programme is to determine, for a small set of organism-level capabilities, whether the production organism actually traverses:

**developmental prerequisite -> representation -> endogenous recruitment -> local operation -> competitive authority -> committed behaviour -> ecological consequence -> retention/generalisation.**

That projection should be built from existing canonical developmental/evidence records, not from a parallel architecture.

The most promising immediate leverage is that several stubborn live blockers already sit exactly on this boundary. The coalition controller has a validated operator but no fair competent/adapting organism in which to test type-specific benefit. Commitment-gate work repeatedly discovers that the upstream state/policy distribution is too impoverished to grade the mechanism fairly. ContextMemory now has a learned addressing path but still owes content discrimination and functional use before causal sleep findings can be trusted. Long-life observation exists, but plasticity and ecological continuity need to be made explicit before duration can become development. And at the experimental layer, REE must stop allowing the question “was the required faculty even enabled and plastic in this run?” to remain implicit: canonical profile identity, required mechanism activation, engagement, authority and learning capability should become preflight facts.

The next phase should therefore be framed as:

> **not building development into REE from scratch, but making REE's existing developmental architecture executable, observable and causally connected in the organism that actually runs.**

---

## 20. Completion criterion for this programme document

For project-import purposes this synthesis is now **complete enough to act as a routing document**. Completeness here does not mean that every claim or experiment in REE has been exhaustively enumerated. It means the document now:

- distinguishes existing canonical machinery from genuinely new synthesis;
- avoids proposing duplicate developmental, metacognitive, memory-gating or event-sourcing architecture;
- incorporates the important live corrections through the 2026-08-27 repository audit;
- names concrete organism-level workstreams and first deliverables;
- explicitly turns instantiated-organism identity, mechanism activation and plasticity into experimental preconditions rather than post-hoc caveats;
- preserves the broader scientific framing of V3 as an experimental organism and later REE as an integration programme rather than reducing the handover to developmental debugging;
- records the need to curate existing behavioural evidence, build reproducible flagship demonstrations and lower the barrier for external scientific inspection;
- captures the research philosophy articulated in the discussion without promoting it automatically into claims;
- preserves V3/V4 scope boundaries;
- makes its own non-authoritative status explicit.

The preferred maintenance model is **not** to keep expanding this prose whenever REE changes. Once the Developmental Integration View exists, live status should be generated there from canonical records, while this document remains the programme rationale and initial handover.

---

## Appendix A — Canonical repository anchors

### Core developmental specification

- `REE_assembly/docs/architecture/developmental_curriculum.md`
- `REE_assembly/docs/architecture/developmental_needs_register.md`
- `REE_assembly/docs/architecture/developmental_metrics.md`
- `REE_assembly/evidence/planning/developmental_readiness_investigation_2026-08-12.md`
- ARC-120 competence-before-authority lineage
- `REE_assembly/docs/architecture/causal_reach_and_installability.md` (ARC-130 / ARC-131)

### Metacognitive / coalition control

- `REE_assembly/docs/architecture/sd_091_coalition_topology_control.md`
- raw source: `REE_assembly/docs/thoughts/2026-08-01_metacognitive_control_selective_cognitive_coalition_instantiation.md`
- `ree-v3/experiments/v3_exq_886_mech481_coalition_4arm_falsifier.py`

### Policy / representation / competence

- `REE_assembly/docs/architecture/sd_actor_critic_action_learning.md` (MECH-457)
- SD-056 action-conditional E2 lineage
- MECH-314a/b/c structured-curiosity lineage
- MECH-455 competence-based intrinsic motivation
- `REE_assembly/evidence/planning/competence_floor_reposing_2026-07-20.md`
- `REE_assembly/evidence/planning/competence_floor_reposing_2026-07-25.md`
- `REE_assembly/evidence/planning/mech465_stage2_conditional_gate_probe_2026-07-21.md`
- `REE_assembly/evidence/planning/mech465_boundary_regime_reachability_probe_20260827.md`

### Memory

- `REE_assembly/docs/architecture/contextmemory_write_address_selection.md`
- `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-943_2026-08-21.md`
- `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-946_2026-08-25.md`
- `REE_assembly/evidence/planning/memory_allocation_gate_candidate_claim_disposition_2026-06-06.md`
- `REE_assembly/evidence/literature/targeted_review_contextual_memory_allocation_gate/VERDICT.md`

### Intervention / causal reach

- `REE_assembly/docs/thoughts/2026-08-24_causal_reach_installability_and_when_a_mechanism_becomes_part_of_the_organism.md`
- `REE_assembly/docs/architecture/causal_reach_and_installability.md`
- `REE_assembly/evidence/planning/thought_intake_2026-08-24_compression-decompression-prospective-attractors-barrett-miller-convergence.md` (INV-103 distinction)

### Sleep / offline integration

- `REE_assembly/evidence/planning/sleep_substrate_plan.md`
- SD-SLEEP-ENTRY-PRESSURE / V3-EXQ-933a
- `REE_assembly/evidence/planning/causal_sleep_deprivation_matched_arm_design_2026-08-14.md`
- `REE_assembly/evidence/planning/causal_sleep_matched_arm_queue_blocked_2026-08-18.md`

### Long-life organism

- `REE_assembly/evidence/planning/organism_lifespan_development_review_906_lineage_2026-08-10.md`
- `REE_assembly/evidence/planning/observational_review_V3-EXQ-906b_2026-08-09.md`

### Canonical organism / experiment configuration integrity

- `REE_assembly/docs/architecture/canonical_profile_admission_criteria.md`
- `REE_assembly/docs/architecture/canonical_profiles/ree_v3_baseline.json`
- `REE_assembly/docs/architecture/canonical_profiles/CONSTITUTION_TEMPLATE.md`
- `REE_assembly/evidence/planning/architecture_epoch_investigation.md`
- `ree-v3/ree_core/utils/canonical_profile.py`
- `ree-v3/experiments/_lib/canonical_profile_fingerprint.py`

### Scientific programme / public orientation

- `REE_assembly/README.md`
- `REE_assembly/docs/START_HERE_HOW_REE_DEVELOPS.md`
- `REE_assembly/docs/thoughts/2026-08-06_scientific_evolution_of_ree.md`
- `REE_assembly/evidence/planning/ree_ai_design_critique_plan.md`
- `REE_assembly/evidence/planning/goal_pipeline_plan.md`

### Governance / provenance

- `REE_assembly/evidence/planning/status_history_plane_separation_design.md`
- `REE_assembly/evidence/planning/status_history/README.md`
- `REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md`
- `REE_assembly/evidence/planning/treadmill_fix_effect_measurement_20260826.md`
- umbrella coordination state: `REE_Working/TASK_CLAIMS.json`, `REE_Working/TASK_CHIPS.json`

---

## Appendix B — Superseded recommendations from the first draft

These are retained here so future archaeology can see what changed after checking the repositories.

| First-draft recommendation | Repo-aligned disposition |
|---|---|
| Build a new developmental competence scoreboard | **Superseded.** Derive an integration view from existing curriculum, DEV-NEEDs, metrics and readiness/causal-reach frameworks. |
| Recover/possibly build a metacognitive developmental controller | **Mostly superseded.** SD-091/MECH-481 already exists and is live-wired. First test a competence-to-authority bridge using existing control machinery. |
| Make learning progress a new developmental objective | **Superseded as novelty claim.** Existing MECH-314c/MECH-455 lineage; focus on causal influence, context specificity and installability. |
| Make memory writing agentic | **Narrowed.** Existing write gates and V4 allocation-policy line already cover much of "whether/how to write". V3 live need is ContextMemory content/address/retrieval/behavioural competence and cross-memory integration. |
| Define non-oracular injections | **Superseded as new concept.** Already represented by GOV-INTERVENE-1; distinguish from runtime INV-103. |
| Build a new governance state-transition ledger | **Superseded.** Existing status/history plane is already event-sourced. Reuse/extend its contract. |
| Continuous-life sleep cannot fire | **Stale finding.** SD-SLEEP-ENTRY-PRESSURE + V3-EXQ-933a now provide validated within-life entry mechanics. |
| Phase 2 claim/chip migration has not started | **Stale.** Phase 2 build has started default-OFF in parallel with Phase 1 soak; actual go-live remains gated. |

