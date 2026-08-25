# Thought: Causal Reach, Installability, and When a Mechanism Becomes Part of the Organism

Status: processed
Intake: evidence/planning/thought_intake_2026-08-24_causal_reach_installability_and_when_a_mechanism_becomes_part_of_the_organism.md
Claims registered: ARC-130, ARC-131, GOV-PATHVALID-1, GOV-INTERVENE-1

**Date:** 2026\-08\-24
**Status (descriptive):** Raw thought intake for `docs/thoughts`; no claim or implementation change follows automatically. Processed 2026-08-25 -- see Intake link above.
**Origin:** Structured mining of Antonio Gullì’s *Agentic Design Patterns*, its companion code, and the current `REE_assembly` / `ree-v3` repositories

## Originating observation

> “Mechanisms etc that are represented in both this literature and REE which REE is struggling to implement in a way that is working could also be looked at in more detail.”

The immediate observation was methodological: discovering that an external source overlaps an existing REE claim should not end the mining process\. It should change the question\.

If the mechanism is already represented in REE but REE has repeatedly struggled to make it work, the source may still be valuable\. It may contain a better decomposition, a simpler positive control, an explicit routing boundary, a stopping condition, a reference operator, or a diagnostic capable of showing exactly where the REE mechanism loses causal reach\.

This led to a deeper architectural thought\.

> **A mechanism is not fully part of the organism merely because its code, representation, or local operator exists. It becomes part of the organism only when the organism can recruit it under the appropriate conditions, its operation can acquire the intended authority, that authority can reach committed behaviour, and the resulting competence survives installation into the whole cognifold.**

This is partly an extension of the existing REE principle that competence should precede authority\. It adds two further problems:

1. **causal reach:** even authority at one selection boundary may fail to propagate to action or consequence;
2. **installability:** a mechanism that works alone may cease to work when composed with the rest of the organism\.

A further implication follows from the observation that not every useful injection is an oracle\. An **oracle intervention** supplies privileged information, a target-correct value, or competence that the organism does not yet possess\. A **non-oracle injection** changes a suspected causal variable without supplying the answer the mechanism is meant to discover\. The former asks whether the rest of the pathway could succeed if one stage were competent; the latter asks how the pathway responds when a particular state, relation, magnitude, or timing is changed\.

Within either epistemic condition, **silky injections**—carefully shaped interventions that preserve the surrounding state distribution while altering one suspected causal variable—and **oddly composed injections**—interventions that deliberately combine states or signals that would rarely arise naturally—may be diagnostically useful\. They can reveal whether a mechanism is sensitive to the right structure, whether it depends on accidental correlations, and whether a downstream pathway can use a signal that the production organism does not yet generate\. A silky injection may be oracle-directed or non-oracular; an oddly composed injection may likewise contain an oracle-selected value or merely a controlled counterfactual composition\.

These may be among the most important general lessons of current REE implementation\.

---

## A repository can contain a mechanism that the organism does not possess

There are several importantly different meanings of “implemented”:

- a class, tensor, state field, controller, or operator exists in source code;
- the component is constructed under some configuration;
- a test can call it directly;
- its intended input can be supplied artificially;
- it changes its immediate local target;
- the integrated agent can generate the input endogenously;
- the component can compete successfully with other influences;
- its output changes fresh committed action;
- the changed action produces an ecologically meaningful consequence;
- the competence persists through later learning, composition, and developmental change\.

These are not interchangeable\.

An optional controller that is default\-off is not present in a particular running organism\. A controller that is instantiated but never called is anatomically present but functionally silent\. A mechanism that changes a local score but never changes the selected action has local causal efficacy without behavioural authority\. A mechanism that changes an internal argmin but not the action the body executes has selection authority at one layer without behavioural throughput\. A mechanism that works only when a test injects a hidden internal state may be mechanically sound but unavailable to the organism\. A mechanism that passes in isolation and disappears in the all\-on agent may be locally competent but not installable\.

The meaningful scientific object is therefore not simply the component\. It is the **reachable pathway through the whole instantiated organism**\.

This also sharpens the idea of REE as one cognifold\. The actual organism is not the union of everything the repository could instantiate\. It is the configured, trained, dynamically reachable system that exists during a run\. A mechanism outside the reachable dynamics is closer to latent architectural possibility than an acquired faculty\.

---

## A causal\-reach ladder

The existing Architectural Commitment `ARC-120` describes a developmental sequence:

`existence → representation → competence → authority → behavioural influence`\.

Current implementation experience suggests a more resolved audit projection:

1. **Existence**
   The architecture names the problem and a candidate mechanism exists in design or code\.
2. **Representation**
   The mechanism receives or constructs the differentiated state it requires\. A scalar that is identical across candidates cannot support candidate selection merely because it has magnitude\.
3. **Endogenous recruitment**
   The organism can recognise the conditions in which the mechanism is needed and invoke it without an experimenter directly calling the operator or injecting its internal state\.
4. **Local operation**
   Once recruited, the mechanism measurably transforms its direct target\. Its trigger fires, its gate changes, its candidate field differentiates, or its update occurs\.
5. **Competitive authority**
   The transformed signal is strong, timely, and correctly placed enough to influence the arbitration surface against competing terms\. Non\-zero influence is not necessarily competitive influence\.
6. **Committed throughput**
   The changed arbitration result survives any later selector, latch, commitment boundary, action remapping, hold state, or stale\-selection path and alters what the organism actually does\.
7. **Ecological consequence**
   The changed behaviour matters in an environment that gives the organism a valid opportunity to express the capability\. The consequence might be progress, information gain, harm avoided, successful closure, flexible rule use, or another claim\-aligned outcome\.
8. **Retention and generalisation**
   The capability persists through subsequent learning and composition, and generalises to held\-out conditions at the level claimed\. Acquisition without retention, or a local effect that disappears outside its training ecology, is not the same competence\.

This is not necessarily the literal computational topology\. REE is recurrent, distributed, multi\-rate, and increasingly compositional\. Several stages may form loops or operate in parallel\. The ladder is an **audit projection**: a way to ask what obligation has and has not been demonstrated\.

It may often be useful to record the furthest stage reached\. For example:

- `represented / not endogenously recruited`;
- `operator engaged / no competitive authority`;
- `selection changed / no committed throughput`;
- `behaviour changed / ecological competence unresolved`;
- `isolated competence / full-stack installation failed`\.

It may also be useful to record the intervention along several independent dimensions rather than force it into one flat type:

| Dimension | Examples |
| --- | --- |
| Epistemic content | `natural` / `oracle` / `non-oracle` |
| Intervention form | `replacement` / `nudge` / `recombination` / `substitution` |
| Distribution relation | `on-manifold` / `near-manifold` / `deliberately off-manifold` |
| Causal locus | `upstream source` / `edge` / `downstream consumer` |
| Diagnostic purpose | `ceiling` / `local sensitivity` / `threshold` / `timing` / `compositional structure` / `shortcut detection` |

This matters because oracle status concerns the information supplied, not whether the intervention is small, smooth, abrupt, or unusual\. A silky nudge can still use oracle knowledge of the correct direction; an oddly composed state can be wholly non-oracular\.

This would be more informative than the undifferentiated statement that a mechanism is implemented or not implemented\.

---

## Causal reach is distinct from competence\-before\-authority

The competence\-before\-authority principle remains important: a mechanism should not gain behavioural or write authority simply because it exists\. It should earn that authority through demonstrated competence\.

The current thought adds that **authority is not the end of the chain**\.

A mechanism may acquire authority over one internal decision while still failing to control the organism\. There may be another selector downstream\. The selected candidate may not be fresh\. A commitment latch may preserve a previous policy\. A motor mapping may ignore the changed variable\. The body may be unable to enact the selection\. The environment may not expose a consequence\. A later learning phase may erase the competence\.

Therefore:

> **Competence should precede authority, but authority must also demonstrate throughput.**

Conversely, behavioural correlation does not establish authority\. A state can predict behaviour because both are driven by the same situation\. A live motivational or affective signal may covary with movement while contributing nothing to selection\. Correlation, competitive authority, and committed throughput require different experiments\.

This may be particularly important for REE because its architecture deliberately contains several levels of control: proposal, scoring, eligibility, selection, commitment, execution, learning, and governance\. Each boundary is useful, but each is also a place where an apparently working signal can disappear\.

---

## Diagnostics should include oracle and non-oracle interventions

A simple diagnostic strategy places an oracle immediately before or after a suspected causal edge\. This is often useful, but it is not sufficient\.

A pre\-edge oracle can test whether a downstream consumer can use a correct signal\. A post\-edge oracle can test whether an upstream mechanism can produce a signal that contains the required information\. Yet both may miss failures caused by the **shape**, **timing**, **distribution**, or **composition** of the intervention itself\.

### Oracle versus non-oracle

An oracle intervention imports some of the competence under investigation\. It may select the correct route, supply a correctly differentiated candidate field, identify a failure type, or declare whether a goal is genuinely complete\. Its primary use is as a positive control and ceiling test: if the downstream organism still cannot use the correct signal, improving the endogenous producer cannot solve the observed failure\.

A non-oracle injection need not know which state is correct\. It may perturb signal strength, cross a threshold, shift timing, decorrelate two variables, or recombine otherwise plausible states\. Its primary use is causal identification: it estimates sensitivity to a variable or relation without pretending to solve the task on the organism's behalf\.

The evidence produced is therefore different:

- **oracles establish achievable ceilings and downstream usability;**
- **silky injections map local causal sensitivity, thresholds, timing dependence, and hysteresis;**
- **oddly composed injections test factorisation, invariants, compositionality, and shortcut dependence\.**

The last two descriptions are not alternatives to oracle status\. They describe how the injected state is constructed and how it relates to the production distribution\. Either can be oracle-informed or non-oracular\.

### Silky injections

A silky injection is a minimally disruptive intervention designed to alter the suspected causal variable while preserving as much of the surrounding state as possible\. It should be smooth in magnitude, timing, and representational form rather than an abrupt replacement with an idealised value\.

Examples might include:

- slightly increasing the candidate spread of an otherwise naturally generated field;
- nudging a deficit signal across a recruitment threshold without replacing the entire state;
- inserting a graded confidence change while preserving the original uncertainty structure;
- perturbing one coalition demand while retaining the current mode and resource context;
- adding a small, temporally aligned closure cue rather than directly inserting a committed trajectory\.

Silky injections can help distinguish:

- threshold failure from representation failure;
- scale failure from semantic failure;
- timing failure from pathway absence;
- competitive weakness from complete downstream insensitivity;
- a mechanism that requires a natural manifold from one that merely responds to arbitrary values\.

They should not be assumed to be neutral\. Even a smooth perturbation can alter learning, attention, or mode occupancy\. Their value lies in making the intervention more local and interpretable, not in making it causally innocent\.

### Oddly composed injections

An oddly composed injection deliberately combines components that are individually plausible but rarely or never co\-occur in the natural production distribution\. The purpose is diagnostic rather than ecological\.

Examples might include:

- a high epistemic deficit paired with low novelty and high confidence;
- a closure cue combined with a trajectory that was not generated by the commitment pathway;
- a coalition demand whose members are individually valid but whose joint timing is developmentally unusual;
- a candidate field with natural local structure but an atypical global ranking;
- a wanting signal that is semantically aligned with one candidate but temporally aligned with another\.

Such interventions can reveal whether a mechanism depends on:

- the intended factorisation;
- a hidden shortcut;
- a particular conjunction of upstream states;
- a downstream invariant that has not been documented;
- accidental training correlations;
- a production distribution that is narrower than the claim implies\.

Oddly composed injections should be treated as **stress tests of causal structure**, not as evidence of ordinary competence\. A mechanism that responds correctly to an unusual composition may possess useful compositionality, but the intervention itself does not establish that the organism can naturally generate or encounter that state\.

Together, silky and oddly composed injections extend the diagnostic space between ordinary production and blunt oracle replacement\. They may be especially valuable when a mechanism appears to work under direct injection but fails under natural operation, because they can show whether the failure lies in the exact state manifold, the transition into that manifold, or the downstream use of the state\.

---

## Installability is a separate competence

REE has repeatedly exposed another problem: a mechanism can work in isolation and still fail as part of the whole organism\.

The rest of the organism changes the mechanism’s operating conditions\. It changes:

- the state distribution it receives;
- the scale and variance of competing signals;
- the timing and frequency of relevant events;
- the availability of competent upstream representations;
- the downstream action space and commitment dynamics;
- the learning gradients applied after installation;
- resource use, interference, and mode occupancy;
- the ecology in which the mechanism must demonstrate value\.

This makes **installability** more than an engineering convenience\. It is a property of the mechanism\-organism relationship\.

A component\-level passing result &#40;PASS&#41; can establish that an operation is possible\. It does not establish that the whole agent can enter the states in which it operates, that it remains competitive when other mechanisms are enabled, or that later learning will preserve it\.

The difference resembles, but is not reducible to, competence retention\. A competence can be acquired and then erased by subsequent learning\. Installability also includes simultaneous composition: the competence may never appear in the full\-stack agent because its signal is drowned, its preconditions vanish, its timing conflicts with other loops, or the combined organism is no longer competent enough to expose the relevant behaviour\.

This suggests a second general formulation:

> **A mechanism that cannot be installed without losing its function is not yet a solved organism-level mechanism, even if its isolated implementation is correct.**

This does not mean every mechanism must work in every configuration\. Some mechanisms should be conditionally recruited, developmentally staged, or mutually inhibitory\. The requirement is that the architecture can compose or recruit the mechanism in the situations for which the claim assigns it a role\.

---

## Why current REE makes this visible

Several live lineages illustrate different broken edges\. These examples motivate the thought; they should not be mistaken for new adjudications of the claims involved\.

### Coalition control: operator present, endogenous recruitment absent

Reflective–Ethical Engine version 3 &#40;REE\-v3&#41; contains typed control demands, coalition templates, a coalition controller, dissolution conditions, and multiple consumer gates\. When a coalition is requested manually, tests show that it can alter the action stream\. Yet the enabled controller is deliberately inert until something calls `request_coalition()`, and the current live agent has no endogenous monitor/classifier doing so\. Only two coalition templates are implemented\.

This is not a missing controller\. It is a broken representation/recruitment edge\.

### Decomposition: recruitment demonstrated, quality obligation unresolved

The prediction\-failure decomposition mechanism can fire, and the latest re\-posed experiment corrected a long chain of trigger\-occupancy defects\. Yet a mechanism firing in the right experimental arm does not by itself establish that it produced better re\-tilings or harm\-aware selection among them\. Trigger selectivity, decomposition occurrence, candidate quality, ranking quality, and final outcome are distinct stages\.

This is a reminder that operator engagement can be genuine while the claim\-aligned competence remains unmeasured\.

### Wanting and selection: correlation, authority, and throughput separate

Recent wanting experiments provide an unusually clean demonstration\. A wanting state can be live and predict locomotion while having no causal authority over the selection pathway being tested\. Even when a very large experimental weight forces changes in the hippocampal Cross\-Entropy Method &#40;CEM&#41; argmin, executed behaviour can remain unchanged\. Buying authority at one internal boundary does not necessarily buy throughput\.

This is perhaps the clearest evidence that the causal\-reach ladder needs a stage after authority\.

### Closure and decommitment: a green test can certify an injected state

At one point, a closure\-exclusive decommitment test appeared activated because its contract harness directly inserted a committed trajectory\. The production organism could not create that supposedly closure\-exclusive state independently of the natural commitment path\. The test showed that the downstream machinery worked if its precondition was injected; it did not show that the organism possessed the full pathway\.

This is a general warning: **a contract test that mocks the source of the load\-bearing state cannot certify production\-path reachability**\.

### Epistemic orienting: a named route can still be absent

The configuration surface reserves an `epistemic_deficit` source, but the accumulator itself remains unbuilt and the route currently falls back to a generic broadcast source\. A vocabulary entry and a fallback\-compatible interface preserve future architecture; they do not mean the epistemic\-deficit mechanism exists in the organism\.

### Rule apprehension: fallback can quietly erase the manipulation

A selector may be configured to demote candidates, yet an envelope that admits every candidate falls back to all\-admit and makes the enabled arm &#40;ON&#41; equivalent to the disabled arm &#40;OFF&#41;\. The surrounding experiment may execute successfully while the intended causal contrast never occurs\. Here the non\-degeneracy gate becomes part of the mechanism’s evidential boundary\.

Together these cases span representation, recruitment, engagement, authority, throughput, measurement, and installation\. Their recurrence suggests a general architectural/scientific principle rather than unrelated local bugs\.

---

## What external agentic patterns can contribute without becoming REE mechanisms

Many agentic software patterns appear cognitively impressive because a pretrained large language model &#40;LLM&#41;, developer, evaluator, or framework supplies the difficult competence\. A router asks an LLM to emit a branch name\. A reflection loop asks the same model to critique itself\. A goal loop stops when a model returns `True`\. A recovery system switches tools when a Boolean flag is present\. A planning agent writes a textual plan\. These are not evidence that the corresponding endogenous REE mechanisms have been constructed\.

However, their explicit interfaces can be scientifically useful\.

They often expose a boundary that is implicit or broken in REE:

- classifier → route;
- failure type → admissible recovery;
- discrepancy → revision;
- progress evidence → continuation or stop;
- complexity estimate → cognitive resource allocation;
- hypothesis → external evaluation → update\.

This suggests using such patterns and injections as **temporary scientific prostheses or causal probes**:

1. Replace one missing stage with an oracle or externally supplied decision\.
2. Determine whether the downstream REE pathway can use a correct signal\.
3. Replace the downstream stage with an oracle to determine whether the upstream representation contains useful information\.
4. Use non-oracle injections to measure whether changing the suspected variable matters without supplying the task solution\.
5. Use silky injections to test whether a small, production\-like perturbation is sufficient to cross the suspected boundary\.
6. Use oddly composed injections to test whether the pathway depends on intended structure or accidental state conjunctions\.
7. Cross oracle status, intervention form, distribution relation, and causal locus in a factorial design where necessary\.
8. Remove the prosthesis or probe and test whether REE can acquire and recruit the same function endogenously\.

For example, if an oracle selects the correct route and behaviour still does not change, further work on the endogenous classifier is premature\. If oracle\-diverse candidates plus the current selector fail, selection or throughput is the bottleneck\. If current candidates plus an oracle selector succeed, generation may be adequate\. If a silky nudge to the candidate field changes behaviour while a blunt replacement does not, the mechanism may depend on continuity or timing\. If an oddly composed state produces a response that natural states do not, the pathway may be responding to a shortcut rather than the intended construct\. If neither oracle condition can produce behaviour, the competence or environmental substrate lies elsewhere\.

The important safeguards are:

- oracle competence must be labelled and excluded from organism\-level claims;
- provenance must state which stage, variable, relation, or information source was externally altered;
- non-oracle does not mean natural: silky and oddly composed injections must still be identified as diagnostic interventions rather than production-path evidence;
- effects demonstrated only under external intervention must be attributed to that intervention condition rather than silently treated as endogenous REE competence;
- the oracle should be a bounded experimental instrument, not a hidden permanent homunculus;
- matched\-cost and no\-oracle baselines should be preserved;
- the eventual endogenous mechanism must be tested separately\.

The source’s weakness as a cognitive architecture can therefore become its strength as a stage\-isolating control\.

---

## A mechanism passport or causal\-reach trace

It may be useful for important REE mechanisms to carry an inspectable evidential record—not necessarily as one monolithic runtime object, but as a shared experimental schema\.

```text
MechanismReachTrace:
    mechanism_or_claim_id
    configured_and_instantiated
    required_representation_present
    endogenous_trigger_present
    trigger_occasion_count
    operator_engagement_count
    direct_target_effect
    competitive_authority_ratio
    selected_state_changed
    fresh_commit_changed
    executed_action_changed
    ecological_opportunity_present
    task_consequence_changed
    retained_after_learning
    held_out_generalisation
    intervention_used
    epistemic_content_natural_oracle_nonoracle
    intervention_form
    distribution_relation
    causal_locus
    diagnostic_purpose
    privileged_information_supplied
    silky_injection_parameters
    oddly_composed_state_description
    production_path_verified
    first_broken_edge
    uncertainty_and_provenance
```

Not every field applies to every mechanism\. Some mechanisms act on memory writes, perceptual inference, or internal resource allocation rather than immediate action\. Their later stages should be expressed in the correct currency: write admission, belief revision, recall, future policy, welfare consequence, or another claim\-aligned effect\.

The general rule is that the trace should follow the mechanism to the level at which its claim says it matters\.

This could improve several parts of the scientific process:

- readiness gates could target the exact upstream requirement;
- a non\-contributory result could identify the first broken edge;
- repeated experiments would be less likely to retest a downstream dependent variable while the same upstream edge remained broken;
- contract tests could distinguish direct\-call functionality from production\-path reachability;
- apparently contradictory experiments could be reconciled as measurements of different stages;
- installability could be compared across progressively composed configurations;
- intervention provenance could prevent a silky or oddly composed diagnostic from being mistaken for natural operation\.

---

## Composition experiments should treat installation as the independent variable

The full\-stack problem suggests a family of experiments in which the main manipulation is not simply mechanism ON versus OFF, but **where and how the mechanism is installed**\.

Possible designs include:

### Layer\-by\-layer installation

Begin with a competence\-qualified base agent\. Add one mechanism or face at a time\. At each step, re\-measure:

- upstream representation quality;
- source\-signal range;
- authority at the relevant selector;
- committed throughput;
- task competence;
- retained prior competences;
- resource and mode occupancy\.

The first layer at which competence disappears is more informative than a null from the final all\-on agent\.

### Order\-of\-installation tests

Some mechanisms may need developmental ordering\. A competence installed before another learning phase may be overwritten, while the reverse order may permit coexistence\. Order should therefore sometimes be treated as a causal variable rather than incidental training detail\.

### Oracle boundary crossing

Place an oracle immediately before and after the suspected broken edge\. If the downstream oracle rescues behaviour but the upstream oracle does not, the boundary has been localised\.

### Silky perturbation sweeps

Apply graded, temporally aligned perturbations around the suspected threshold\. Measure whether the response is smooth, discontinuous, hysteretic, or absent\. This can distinguish a missing route from a route that exists but requires an unrealistically large intervention\.

### Odd composition matrices

Construct controlled combinations of otherwise valid states that vary one structural relation at a time\. Test whether the mechanism follows the intended relation or merely responds to familiar conjunctions\. These matrices should be interpreted as structural diagnostics, not ordinary ecological trials\.

### Competitive\-scale testing

Measure not only whether a signal varies, but its cross\-candidate spread relative to the dominant competing term\. A signal with a real range may still be several orders of magnitude below the authority threshold\.

### Fresh\-commit verification

Distinguish a changed internal selection from a changed fresh commitment\. Hold\-dominated &#40;`HOLD`\-weighted&#41; or stale\-trajectory behaviour can make an internal selector appear behaviourally irrelevant even when it works as designed\.

### Retention after installation

After adding the mechanism, continue learning and re\-test both the new competence and protected old competences\. This joins installability to the existing acquisition\-versus\-retention distinction without collapsing them\.

---

## The full versioned lineage

Although current V3 failures make this thought visible, it concerns the full REE lineage\.

### REE\-v3

The immediate problem is making single\-goal organism mechanisms causally reachable and behaviourally meaningful: proposal, selection, commitment, harm/goal control, closure, curiosity, replay, orienting, and rule use\. V3 is where the basic distinction between local function and organism\-level reach must become experimentally explicit\.

### REE\-v4

Multi\-goal deliberation, richer memory lifecycle, inference, object/action affordances, and cognitive\-operation allocation multiply the number of boundaries\. A cognitive operation may be correctly selected yet fail to change a goal decision; a memory may be retrieved yet lack action authority; a parked goal may be represented yet never become resumable\. Causal\-reach traces may therefore become even more important\.

### REE\-v5

Social cognition introduces capability claims about other minds, shared attention, communication, repair, trust, and responsibility\. Protocol\-level communication or self\-declared capability cannot establish grounded social competence\. Reach must extend through self/other attribution, shared reference, coordinated behaviour, and consequences for another agent\.

### REE\-v6

Language creates a particularly strong risk of confusing report with mechanism\. A fluent verbal explanation, self\-critique, declared intention, or completion statement may correlate with internal processing without controlling it\. Linguistic output should be tested for causal relationship to grounded cognition rather than treated as transparent access to it\.

### REE Assembly

Assembly needs the complementary external view: it should know which stages were endogenous, externally scaffolded, injected, inferred, or unmeasured\. Governance should avoid both errors—crediting REE with oracle competence and blaming REE for a failure that occurred in the mechanism, measure, or environment\.

---

## Relationship to existing REE thoughts and claims

This thought does not begin from an empty space\.

- `ARC-120` already states that competence should precede authority and gives the sequence `existence → representation → competence → authority → behavioural influence`\.
- Governance rule `GOV-FAILLOC-1` already separates REE failure, mechanism failure, measurement failure, and environment failure\.
- The behavioural\-adjudication thought already distinguishes observation, interpretation, and mechanism, and argues for an umpire rather than one convenient ruler\.
- The single\-cognifold thought already distinguishes repository possibility from the configured, instantiated organism\.
- `MECH-476` already separates acquiring competence from retaining it\.
- The persistence/earned\-continuation thought already rejects continuation merely because a process began\.
- The strategy\-authority thought already separates authority, policy persistence, and execution gain\.

The distinct synthesis here is:

1. **authority may fail to propagate into committed throughput;**
2. **production\-path reachability must be demonstrated rather than injected;**
3. **whole\-organism installability is a separate competence;**
4. **external agentic patterns can be mined as bounded oracle controls at a broken causal edge;**
5. **non-oracle injections can establish causal sensitivity without supplying the competence being tested;**
6. **silky and oddly composed injections can diagnose sensitivity to scale, timing, structure, and distribution, independently of whether they are oracle-informed;**
7. **mechanism status should be qualified by the furthest causal stage actually demonstrated\.**

This may ultimately refine `ARC-120`, add an experiment/governance doctrine, or remain a cross\-cutting methodology\. It does not presently justify a new cognitive module\.

---

## Candidate harvests for later structured intake

These are candidate formulations only\. They should be checked against the current claims registry before any registration or amendment\.

### Candidate architectural refinement

> **Organism-level mechanism status is stage-qualified:** existence and local competence do not establish behavioural membership. The mechanism must be endogenously recruitable, competitively authoritative at the relevant boundary, and capable of claim-aligned throughput in the integrated organism.

This may be an amendment or elaboration of `ARC-120`, not a new claim\.

### Candidate installability principle

> **Installability is dissociable from isolated competence:** a mechanism can pass component-level validation yet lose its competence, upstream preconditions, competitive scale, or downstream throughput when composed into the full agent.

This appears related to, but not identical with, competence retention\. It would need a duplication and literature audit\.

### Candidate experimental\-governance rule

> **A load-bearing positive control must traverse the production path it claims to validate.** Directly injecting the state immediately downstream of the suspected failure can validate the consumer but cannot certify reachability of the complete pathway.

This may belong under the experimental\-recording, non\-degeneracy, or failure\-autopsy governance family\.

### Candidate intervention\-diagnostic doctrine

> **Diagnostics should distinguish whether an intervention supplies privileged competence from how it changes the state.** Oracle interventions test achievable ceilings and downstream usability; non-oracle injections test causal sensitivity without supplying the task answer; silky and oddly composed constructions test local response and structural dependence along an independent axis.

This should not be interpreted as evidence of natural competence unless the organism can generate the relevant state through the production path\.

### Candidate instrumentation doctrine

> Experiments should identify the first broken causal edge and report the furthest stage demonstrated, rather than labelling the whole mechanism implemented, failed, or non-contributory without qualification.

This may refine `GOV-FAILLOC-1` rather than requiring a separate rule\.

---

## Important cautions

### Do not force a software pipeline ontology onto distributed cognition

The causal\-reach ladder is an audit device\. A biological or learned distributed mechanism may not expose neat modules, route labels, or single call sites\. The methodology should permit causal mediation across distributed states and recurrent dynamics rather than requiring literal software boundaries\.

### Do not demand immediate action effects from every mechanism

Some mechanisms alter future learning, memory consolidation, belief precision, or developmental readiness\. Their correct downstream consequence may appear much later\. The trace must follow the claim’s timescale rather than privilege one\-step motor behaviour\.

### Do not turn the ladder into infinite validation debt

Not every low\-risk implementation needs eight separate experiments\. Evidence requirements should scale with the claim, the mechanism’s authority, and the consequences of error\. Several stages can be tested together if the design remains discriminative\.

### Oracle interventions can change the system they diagnose

An oracle may supply an unrealistically clean state, alter timing, or move the agent into a distribution it would never reach endogenously\. Oracle results establish ceilings and localise boundaries; they do not automatically predict learnability or natural operation\.

### Silky injections are not automatically naturalistic

A smooth or small intervention may still create a state that the organism cannot naturally produce\. Its diagnostic value comes from controlled locality, not from presumed ecological validity\.

### Oddly composed injections are stress tests, not ordinary trials

A response to an unusual composition may reveal useful structural sensitivity, but it does not establish that the organism encounters or generates that composition in normal operation\.

### Non-oracle injections are still external interventions

An injection does not become production-path evidence merely because it supplies no correct answer\. It may still create a magnitude, timing, transition, or composition the organism cannot generate\. Its result supports a causal statement about the manipulated pathway; endogenous competence requires a separate production-path demonstration\.

### Intervention dimensions should not be collapsed

`Oracle`, `silky`, and `oddly composed` do not name mutually exclusive classes\. Oracle status concerns privileged information or competence; silky and oddly composed concern construction and distribution\. Flattening them into one enum would obscure potentially decisive combinations\.

### A failed ecological consequence does not always mean no causal reach

The changed behaviour may be real but irrelevant to the selected task, or the ecology may lack headroom\. Behaviour, claim alignment, and environmental adequacy remain separate\.

### Integration losses may be appropriate inhibition

A mechanism being suppressed in the full organism may be correct if another mechanism has higher justified authority in that state\. Installability does not mean every mechanism must express simultaneously; it means the architecture can recruit it when its role should be load\-bearing\.

---

## Literature and technical domains worth mining

The next literature search should seek methods capable of refining or challenging this thought, not citations that merely agree with it\.

Relevant domains may include:

- causal mediation and intervention analysis;
- systems neuroscience using lesions, stimulation, disconnection, and pathway\-specific manipulation;
- control theory and controllability/observability;
- hierarchical reinforcement learning and option initiation/termination;
- modular and compositional reinforcement learning;
- mixture\-of\-experts routing and router collapse;
- multi\-agent and distributed\-system integration testing;
- software integration, contract testing, dependency injection, and end\-to\-end testing;
- developmental scaffolding and fading of external support;
- curriculum learning and teacher\-student systems;
- competence acquisition, consolidation, catastrophic interference, and continual learning;
- causal representation learning;
- behavioural throughput and embodied affordance testing;
- measurement invariance and construct validation;
- metareasoning and expected value of computation;
- ecological validity and positive\-control design;
- causal probing with minimal and distribution\-preserving interventions;
- compositional generalisation and systematicity testing;
- manifold\-preserving perturbation methods;
- adversarial and counterfactual stress testing of recurrent agents\.

Particular questions include:

1. How do other fields distinguish component efficacy from system\-level causal contribution?
2. What methods best locate the first failed edge in a recurrent distributed system?
3. How can an oracle intervention be designed without moving the system into a meaningless state distribution?
4. When do smooth, local interventions provide more information than direct state replacement?
5. How can oddly composed interventions reveal shortcut dependence without being mistaken for ecological evidence?
6. How is competence retention measured when a new component is composed with older competences?
7. When should authority be measured through mediation rather than direct behavioural ablation?
8. How can production\-path reachability be tested without requiring every experiment to be fully ecological?
9. What formal measures exist for competitive influence relative to dominant signals?
10. How should causal reach be represented when the mechanism’s effect is delayed, distributed, or probabilistic?
11. What intervention designs preserve the relevant state manifold while still crossing a suspected threshold?
12. How can one distinguish a mechanism that is absent from one that is present but only responsive to unnatural compositions?

---

## Provisional final formulation

> **A REE mechanism is not merely a computation that exists or can be invoked. It is a causally reachable transformation within the instantiated organism. The organism must be able to generate its inputs, recruit it under the appropriate conditions, grant it justified competitive authority, carry its result through commitment or the relevant write boundary, and preserve its competence when composed with the rest of the cognifold. External scaffolds, oracle stages, non-oracle injections, silky perturbations, and oddly composed states can help locate a broken edge, but any effect demonstrated only under external intervention must be attributed to that condition rather than silently treated as endogenous REE competence.**

A shorter form is:

> **The mechanism is not the component. The mechanism is the reachable pathway through the organism.**

And the implementation corollary is:

> **Installability is not an afterthought. It is one of the competences the architecture must demonstrate.**

---

## Possible affected components and processes

- `ARC-120` competence\-before\-authority framing
- Governance rule `GOV-FAILLOC-1` failure\-location triage
- experimental non\-degeneracy and positive\-control standards
- failure\-autopsy and experiment\-design skills
- mechanism and claim status language
- causal\-reach trace and intervention provenance
- oracle versus non\-oracle intervention status
- silky\-injection and oddly composed\-injection diagnostics
- trajectory\-selection and commitment engine &#40;E3&#41; scoring, eligibility, selection, commitment, and fresh\-action telemetry
- hippocampal candidate generation and Cross\-Entropy Method selection
- control\-plane routing and typed coalition recruitment
- closure, decommitment, interruption, and recovery
- goal/wanting propagation and behavioural authority
- orienting and epistemic\-deficit accumulation
- rule apprehension, discovery, and write gating
- sleep, consolidation, competence retention, and interference resistance
- V4 cognitive\-operation allocation and multi\-goal deliberation
- V5 social coordination and capability verification
- V6 language/report versus grounded causal mechanism
- REE Assembly provenance, governance, and causal\-attribution standards
