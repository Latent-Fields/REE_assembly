# Experimental learning beyond the literature: a frontier-evidence doctrine for REE

**Date:** 2026-09-24  
**Status:** raw thought / methodology proposal; not yet claim-ingested  
**Scope:** REE-wide, with immediate relevance to V3 interface learning and later V5 ethical-development mechanisms  
**Related internal material:** `docs/architecture/developmental_curriculum.md`, `docs/architecture/social.md`, `docs/architecture/agency_responsibility_flow.md`, `docs/thoughts/2026-09-02_sleep_as_deferred_reorganisation_and_behavioural_access_repair.md`, `evidence/planning/latent_interface_translation_campaign_20260907.md`, `evidence/planning/loveability_ethical_agency_v5_plan.md`

## Core proposition

REE should not treat the absence of direct backing literature as a reason to avoid implementing or testing a mechanism that is required by the ethical experiment.

Literature is evidence, prior constraint, analogy, warning, and source of candidate mechanisms. It is **not permission**.

Some REE requirements may be unusual precisely because REE is asking questions that existing machine-learning, developmental-robotics, cognitive-science, and social-learning literatures have not yet posed in the same computational form. In those cases, a failed literature pull can establish that REE is near a research frontier; it must not silently turn into a veto on the mechanism.

The appropriate response to weak or absent direct literature is therefore not:

> no literature -> do not build

but:

> no direct literature -> mark the mechanism as frontier/conjectural, identify the closest precedents and what they fail to solve, then make the mechanism earn standing experimentally.

This matters especially because REE's primary purpose is to create a testbed in which the ethical axioms can be made causally operative and falsifiable. If the testbed refuses to instantiate a necessary consequence of the theory merely because nobody has already published the required learning rule, REE would become unable to test the very parts of the theory that are most original.

## Why this issue has become visible now

A growing class of REE requirements has good **adjacent** literature but no obvious ready-made algorithm.

Examples include:

1. **Loveability internalisation (LOVE-2):** experienced caregiver care becomes applicable-to-self and alters durable self-valence, rather than merely teaching caregiver reliability or approach behaviour.
2. **Correction without annihilation (LOVE-4):** the agent learns "I caused harm / this action or model should change" without collapsing the error into "I am globally bad, unsafe, unloveable, or should appease".
3. **Love-mediated repair (LOVE-5):** attributed harm plus preserved relationship and residue produces relationship-restoring behaviour that can be distinguished from punishment avoidance, distress-signal suppression, metric gaming, or self-erasure.
4. **Self-to-other valuation transfer (A5-A7):** the self-model is reused not only to predict another agent but to make the other's predicted degradation or benefit causally relevant to the focal agent's own trajectory selection without installing an explicit moral reward.
5. **Responsibility-weighted learning:** commitment, causal attribution, uncertainty/precision, available alternatives, realised consequence, and residue jointly determine how an experience changes future action.
6. **Autonomous internal interface repair:** separately learned REE representations become mutually usable through development, replay, or sleep, judged by downstream causal use rather than probe decodability alone.
7. **Language as ethical-model repair (A8):** communication revises similarity, responsibility, harm, trust, or relationship models and thereby changes later action, while remaining evidentially calibrated rather than treating statements as privileged truth.

The neighbouring literatures are valuable. Attachment theory, shame-versus-guilt research, rupture-and-repair, artificial empathy, Self-Other Modeling, causal responsibility, multi-agent reinforcement learning, model stitching, latent alignment, theory of mind, dialogue repair, and continual learning all supply parts of the terrain.

But a literature analogue is not the same thing as the learning problem REE actually needs to solve.

## Three evidence classes

REE should explicitly distinguish three classes of mechanism.

### Class L — literature-specified

A sufficiently close mechanism already exists in the literature and can be adapted with modest translation.

Examples might include ordinary world-model learning, episodic replay, standard causal estimators, or a well-characterised representation-alignment method.

The default burden is replication/adaptation: show that the imported mechanism reaches the intended REE consumer and survives REE-specific controls.

### Class S — synthesis-required

Relevant components exist, but REE's requirement combines them in a way that is not directly supplied by any one source.

Examples include precision-weighted responsibility attribution, sleep-mediated interface repair, or a self/other model coupled to REE's commitment/residue architecture.

The burden is stronger: separate which parts are literature-backed from which coupling assumptions are REE conjectures, then test the couplings directly.

### Class F — frontier / experimentally discovered

No sufficiently close mechanism can be found after a scoped, good-faith literature search. The requirement nevertheless follows from a REE architectural or ethical question that must be instantiated if the theory is to be tested.

Examples may include LOVE-2, LOVE-4, LOVE-5, some forms of A5-A7 valuation transfer, and A8 ethical-model repair.

Class F is **not a lower-status scientific category**. It is a different provenance category.

Its evidence may begin at zero literature confidence and still eventually become strong if REE experiments repeatedly support it.

## Absence of literature is not evidence of absence

A failed literature search can mean several different things:

- the mechanism is impossible or incoherent;
- the mechanism is possible but has not been studied;
- the mechanism exists under a different vocabulary;
- relevant fields study its components separately but not the coupling;
- the mechanism only becomes meaningful in an architecture with REE-like commitments;
- the question is genuinely new.

These possibilities must not be collapsed.

In particular, "no paper found" should not be entered into governance as if it were evidence against a mechanism unless there is a defensible reason to believe that the relevant literature **should already contain the mechanism if it were viable**.

For many V5 ethical-development questions, that expectation would be unreasonable. Mainstream machine learning usually optimises task performance, reward, preference, imitation, or externally specified social objectives. It does not generally ask how an artificial agent should learn loveability, metabolise correction without self-devaluation, carry responsibility residue, or repair relationships without being rewarded for repair.

The absence of those algorithms may therefore reflect a missing research question rather than a negative result.

## Experimental evidence must be allowed to promote a frontier mechanism

REE already separates literature confidence from experimental confidence in parts of its governance. That separation should be taken seriously.

A Class F mechanism should be promotable on REE experimental evidence alone if the evidence is sufficiently strong.

Promotion should not require retrospective discovery of a citation merely to legitimise the result.

A plausible frontier-evidence pathway is:

1. **Scoped literature search.** Search broadly enough to identify direct precedents, neighbouring mechanisms, known failure modes, and alternative vocabulary.
2. **Frontier declaration.** If no direct precedent is found, record that explicitly. State what was searched and what the nearest analogues do not solve.
3. **Mechanistic specification.** State the proposed learning rule or developmental process at a causal level, including writable targets and prohibited shortcuts.
4. **Competing hypotheses.** Implement or specify credible alternatives rather than testing one favoured mechanism against nothing.
5. **Pre-registration.** Define positive predictions, nulls, non-degeneracy conditions, and what would count as evidence against the mechanism before observing the decisive result.
6. **Causal reach.** Prove that the manipulated signal can reach the claimed consumer and dependent variable.
7. **Negative controls.** Include controls for channel presence, proxy rewards, punishment avoidance, metric optimisation, random/mismatched information, and architectural incapacity where relevant.
8. **Ablation/intervention.** Remove or perturb the proposed mechanism and require the predicted behavioural/internal consequence to change.
9. **Replication.** Reproduce across seeds and, where the claim is intended to be general, across ecologies or developmental histories.
10. **Alternative-mechanism competition.** Prefer the mechanism that explains the intervention pattern, not simply the one that produces a desirable phenotype.
11. **Promotion by evidence.** Permit experimental confidence to carry the claim even when literature confidence remains low, while preserving the provenance label "REE-derived / frontier empirical mechanism."

The absence of literature should therefore increase the **experimental burden**, not prohibit the experiment.

## A crucial distinction: implementing a conjecture is not endorsing it

REE needs to be able to instantiate mechanisms that may be wrong.

Building a candidate learning rule is not promotion.
Running it is not promotion.
Obtaining prosocial-looking behaviour is not promotion.

The purpose of implementation is to make the conjecture vulnerable.

For frontier mechanisms, it may be especially useful to maintain several small, mutually exclusive implementations behind default-OFF flags and let experiments discriminate among them.

For example, correction after harm could update primarily:

- action-value / policy structure;
- causal world models;
- other-harm prediction;
- residue and replay priority;
- self-valence;
- relationship models;
- or some gated combination.

Rather than deciding philosophically which update is "correct", REE can ask which assignments generate the predicted combination of accountability, stable selfhood, repair, generalisation, and resistance to appeasement.

The learning rule itself becomes an experimental object.

## Candidate discovery problems

### 1. Loveability internalisation

The open question is not merely whether a caregiver is predictable or rewarding.

The learning problem is:

> Through what update process does repeated evidence that another self-like agent values my continuation become a durable, behaviourally accessible belief/valuation that my own existence is worth preserving?

Competing implementations might place the update in self-valence, relational prediction, expected support, precision, attachment representation, or combinations thereof.

The empirical target is not attachment behaviour alone. The learned representation must later affect self-preservation, correction tolerance, social exploration, and ethical choice in the predicted directions.

### 2. Error localisation: action versus global self

LOVE-4 implies a hierarchical credit-assignment problem.

After a harmful outcome, which representation should be revised?

A useful agent must sometimes learn:

> this action/model/rule was wrong

without necessarily learning:

> the self as a whole is bad or unsafe.

The literature describes human shame/guilt distinctions and secure-base effects, but REE may need to discover the actual computational gating that produces the separation.

A candidate experiment could orthogonally manipulate:

- causal responsibility;
- caregiver relationship continuity;
- severity of correction;
- reversibility/repair opportunity;
- self-valence stability.

The winning mechanism would update action/causal models when responsibility is high while preserving global self-value when relationship evidence remains intact.

### 3. Repair as a learned consequence of responsibility

A repair mechanism should survive controls that defeat simpler explanations.

A successful agent should not merely:

- stop a visible distress signal;
- minimise an experimenter's harm metric;
- act only under threat of punishment;
- erase or avoid the other;
- collapse itself;
- learn a hard-coded "repair action".

The stronger target is that harm attributed to self creates persistent pressure to restore the other's trajectory or relationship, with appropriate sensitivity to what the other actually needs.

This may require a learning rule that does not currently exist in standard reinforcement-learning form.

### 4. From simulation of another to care about another

Self-Other Modeling and artificial-empathy work show routes to prediction.

REE requires a further transformation:

> predicted state of other -> homologous value relevance -> altered candidate trajectory ranking.

That motivational bridge must be discovered or validated rather than assumed.

An especially important falsifier is the possibility that accurate self-like simulation remains merely informational. If so, A7's implementation requires an additional mechanism or the axiom-to-mechanism derivation must be revised.

### 5. Responsibility-sensitive residue

Today's MECH-025b refusal illustrates the general point. REE wanted precision/responsibility to influence residue, but the dependent variable had no precision input in its causal chain.

The missing substrate should not be inserted merely because the claim expects it. Several candidate update laws can be tested:

- residue proportional to realised harm only;
- harm × causal ownership;
- harm × ownership × commitment strength;
- harm × ownership × epistemic foreseeability/precision;
- nonlinear thresholds for catastrophic or irreversible harm.

The correct REE mechanism, if any, should be discovered by the behaviour and causal properties it produces, not by selecting the most philosophically attractive formula.

### 6. Endogenous internal-interface learning

V3 may encounter this frontier before V5.

REE repeatedly finds that information is:

- encoded,
- externally decodable,
- but not natively usable by the intended consumer.

A normal engineering response is to train an adapter externally. A persistent organism ultimately needs a mechanism for detecting and repairing such failures itself.

A candidate developmental process is:

> repeated prediction/action mismatch -> identify interface-level information loss or incompatibility -> replay paired internal states -> adjust the minimal bridge/readout -> waking test of causal use -> retain only repairs that improve downstream ecological outcomes.

The closest literatures cover representation alignment, model stitching, hyperalignment, continual latent alignment, complementary learning systems, and sleep transformation. The REE-specific open question is whether an artificial organism can perform this process **endogenously**.

If it can, "training REE" begins to become "REE learns how to keep its own cognitive systems mutually legible."

### 7. Language-mediated ethical repair

A8 eventually requires more than communication competence.

A statement from another agent may supply evidence about intent, perception, causal history, similarity, or relationship state. REE must decide how strongly to update those models.

The learning problem is therefore:

> linguistic evidence + prior causal model + source reliability + observed consequences -> revised ethical/social model -> changed future action.

The important failure modes are gullibility, strategic manipulation, language overriding embodied evidence, and inability to repair a false attribution even when counterevidence is strong.

Again, there may be no ready-made algorithm that matches the complete requirement.

## Implication for REE governance

REE should consider adding an explicit **frontier-mechanism route** to its scientific governance.

Suggested semantics:

- `literature_status: direct | adjacent | frontier`
- `literature_confidence` remains independent of `experimental_confidence`
- no minimum literature-confidence threshold for experimental promotion when `literature_status: frontier`
- frontier status requires a documented scoped search and nearest-precedent analysis
- promotion requires stronger causal and replication evidence than would normally be demanded of a directly replicated mechanism
- later literature convergence should update literature confidence but should not rewrite the historical provenance of the REE discovery

This avoids two opposite errors:

1. **citation conservatism:** refusing to investigate a necessary mechanism because nobody has already named it;
2. **novelty exceptionalism:** treating lack of literature as evidence that an attractive idea is profound or likely true.

Frontier status means only: **the answer must come primarily from experiment.**

## Relationship to the existing biology-before-formalisation rule

REE's preference for biological or cognitive grounding before formal definitions remains valuable. It prevents arbitrary mechanism invention and often reveals constraints that a software-first design would miss.

But it needs a stopping condition.

A literature pull should be able to return:

> No direct mechanism found. Adjacent biology constrains A, B, and C. The remaining mapping is an open REE hypothesis and should proceed to competing implementations and experiment.

Otherwise "ground in biology first" can inadvertently become "only implement things biology has already explained", which would make genuinely novel mechanistic questions impossible to study.

The rule should therefore constrain the search space where evidence exists, not prohibit exploration where it does not.

## Scientific value if REE succeeds here

A frontier mechanism discovered in REE would initially be evidence about **REE**, not automatically about human cognition, moral psychology, or universal ethics.

That distinction matters.

But such a mechanism could still be a genuine contribution:

- a computational model of loveability internalisation;
- a learning rule that separates responsibility from global self-devaluation;
- an endogenous repair drive arising from causal attribution and relational residue;
- a method for social valuation transfer without an explicit altruism reward;
- a developmental algorithm for autonomous internal-interface repair;
- or a language-mediated ethical belief-revision mechanism.

Those would be independently interesting even if the broader REE ethical theory later failed.

Conversely, failure to discover a viable learning rule is also evidence. If repeated implementations cannot make one of the axiom-derived transitions work without inserting the desired conclusion as a reward or rule, that counts against the claimed derivation.


## Methodological backing: discovering mechanisms rather than merely retrieving them

The frontier route does not need to rely on an improvised REE methodology. A growing automated-science and cognitive-model-discovery literature already supports a closely related workflow: specify a phenomenon or evaluation criterion, generate executable competing mechanisms, design experiments that make those mechanisms disagree, diagnose failures, and synthesize successor mechanisms.

This literature does **not** validate any particular REE ethical mechanism. Its relevance is methodological: it shows that novel computational mechanisms can be treated as a search-and-adjudication problem rather than requiring the human investigator to know the correct algorithm in advance.

### AutoCog: theory -> discriminating experiment -> failure diagnosis -> successor theory

Jagadish et al. (2026), *Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist* (AutoCog), explicitly treats cognitive theory-building as a closed-loop search problem. Large-language-model agents advocate competing theories expressed as executable cognitive models, design experiments that best discriminate them, collect data, score the models, diagnose why they fail, and synthesize a better successor. Repeating the cycle searches jointly over theories, executable models, and experiments.

Source: https://arxiv.org/abs/2606.26448

For REE, the transferable pattern is:

> phenomenon/constraint specification -> competing executable mechanisms -> maximally discriminating experiment -> failure diagnosis -> revised candidate mechanism.

This is particularly relevant to LOVE-2/4/5 and A5-A8, where the desired functional property can be specified more clearly than the learning rule that produces it.

### Automated adversarial collaboration: candidate models and experiments may both be unknown

Chandramouli, Kachergis & Jagadish (2026), *Automated Adversarial Collaboration for Advancing Theory Building in the Cognitive Sciences*, combines LLM-based theory agents, program synthesis, and information-theoretic experimental design in a closed loop. Importantly, the framework addresses cases where **both the candidate models and the experiments needed to discriminate them must be discovered during adjudication**.

Source: https://arxiv.org/abs/2604.25521

This strengthens the frontier doctrine. REE does not need a complete menu of candidate mechanisms before experimentation begins. A failed candidate can itself generate the information needed to propose the next one.

### ATLAS: actively construct experiments that make mechanisms disagree

Éltető et al. (2026), *ATLAS: Active Theory Learning for Automated Science*, alternates between generating diverse mechanistic hypotheses and designing experiments that optimally distinguish among them. In in-silico reinforcement-learning recovery tasks, ATLAS reports substantially greater sample efficiency than random experimentation and compares its generated experiments with expert-designed experiments from the literature.

Source: https://arxiv.org/abs/2606.12386

The immediate REE implication is that frontier mechanism discovery should not merely run candidate mechanisms on a fixed ecology. The experiment generator should search for **ecologies, developmental histories, interventions, or conflict cases in which plausible mechanisms make divergent predictions**.

For example, two LOVE-4 implementations that both behave well under ordinary caregiver correction may diverge when causal responsibility is low, relationship continuity is high, or repair is possible but costly. Those boundary cases are more informative than aggregate "prosociality" scores.

### Symbolic cognitive-model discovery

Castro et al. (ICML 2025), *Discovering Symbolic Cognitive Models from Human and Animal Behavior*, adapted FunSearch to automatically discover interpretable symbolic learning and decision-making models from behavioural data. The discovered programs outperformed established cognitive models in the studied reward-learning datasets and could be read as explicit hypotheses about cognitive mechanisms.

Source: https://proceedings.mlr.press/v267/castro25a.html

This is unusually close to the REE need. It demonstrates that the **learning rule itself** can be the object of program search rather than something selected entirely from prior literature.

For REE this suggests a hierarchy:

1. begin with simple hand-specified candidate update laws;
2. test and eliminate obvious variants;
3. if the residual phenomenon remains unexplained, allow constrained symbolic/program search over the unresolved update rule;
4. retain interpretability, causal instrumentation, and explicit write permissions so the resulting mechanism remains scientifically inspectable.

### FunSearch: the human can specify the evaluator rather than the solution

Romera-Paredes et al. (Nature 2024), *Mathematical discoveries from program search with large language models*, introduced FunSearch. Its crucial methodological structure is that the user supplies an evaluation function and optionally a program skeleton, while the search system evolves the difficult program logic. FunSearch discovered new mathematical constructions and algorithms beyond previous best-known solutions.

DOI: https://doi.org/10.1038/s41586-023-06924-6  
Source: https://www.nature.com/articles/s41586-023-06924-6

This suggests a productive division of labour for frontier REE work:

> Daniel/the project specifies what a valid mechanism must accomplish, what it may read/write, what shortcuts are forbidden, and what would falsify it. Automated implementation/search machinery proposes and mutates the mechanism.

The investigator therefore does not have to know the missing algorithm in advance.

### Optimal experimental design for model discrimination

Myung & Pitt (2009), *Optimal experimental design for model discrimination*, established a statistical framework for selecting experimental conditions that are maximally informative for distinguishing competing cognitive models rather than merely collecting more data under convenient conditions.

DOI: https://doi.org/10.1037/a0016104  
PubMed: https://pubmed.ncbi.nlm.nih.gov/19618983/

This provides an older methodological foundation beneath the newer agentic systems. REE's frontier process should explicitly optimise experiments for **mechanism discrimination**, not only for competence measurement.

### Robin: iterative hypothesis generation can be closed around real experiments

Hinks et al. (Nature 2026), *A multi-agent system for automating scientific discovery*, describes Robin, which integrates literature search, hypothesis generation, experiment proposal, data analysis, and updated hypothesis generation in an iterative lab-in-the-loop process.

Source: https://www.nature.com/articles/s41586-026-10652-y

Robin is not a cognitive-mechanism-discovery system and its domain is experimental biology, but it is relevant as evidence that agentic hypothesis/data loops can remain scientifically productive when the human investigator controls the experimental substrate and validation.

## The REE frontier mechanism discovery loop

Taken together, the literature supports a more concrete protocol for Class F mechanisms.

### Step 1 — Specify the phenomenon, not the answer

Write a behavioural/causal contract:

- what the mechanism must achieve;
- inputs it is allowed to read;
- states it is allowed to modify;
- states it must not directly modify;
- expected internal and behavioural signatures;
- forbidden shortcuts;
- known alternative explanations;
- decisive falsifiers.

For LOVE-4, for example, the contract might require attributable harm to update the implicated action/causal model while preserving global self-valence when relationship continuity remains evidenced, and require repair/generalisation without punishment-only appeasement.

### Step 2 — Generate deliberately simple competing mechanisms

Prefer small, interpretable rules before learned black boxes.

Examples:

- policy-only update;
- policy + causal-model update;
- policy + causal ownership + residue;
- the above with relationship-continuity gating of self-valence;
- an adaptive/learned gate only after fixed alternatives fail.

Every candidate should be default-OFF and independently instrumentable.

### Step 3 — Prove substrate and causal reach before behavioural interpretation

For each candidate, verify:

- the intended input exists and varies;
- the mechanism actually consumes it;
- its output reaches the claimed downstream consumer;
- the dependent variable can change because of that output;
- OFF controls are bit-identical where appropriate.

This prevents frontier search from rediscovering the current class of "mechanism could not possibly affect the DV" refusals.

### Step 4 — Search for discriminating experiments

Do not ask only whether each candidate "works."

Search for the environmental condition in which their predictions differ most.

Candidate discriminators include:

- high versus low causal responsibility;
- foreseeable versus unforeseeable harm;
- relationship continuity versus rupture;
- repair available versus impossible;
- self-cost of repair;
- same surface outcome generated by different causal histories;
- novel agents/ecologies after identical developmental histories.

### Step 5 — Adversarially test shortcuts

The evaluator must include tests for:

- explicit or hidden proxy reward;
- punishment avoidance;
- distress-signal suppression;
- removing the unethical affordance;
- self-erasure;
- relationship avoidance;
- metric gaming;
- hard-coded action lookup;
- channel-presence effects without content dependence;
- train/test ecological memorisation.

### Step 6 — Diagnose failures and synthesize successors

A candidate that fails is not merely discarded. Record **how** it failed:

- correct representation but no behavioural authority;
- behavioural success through the wrong causal route;
- excessive self-valence update;
- no generalisation;
- unstable residue;
- repair only under punishment;
- collapse under novel other-agents.

Use those failure signatures to constrain the next search generation.

### Step 7 — Escalate search complexity only as needed

The sequence should be:

> simple fixed rule -> parameterised rule -> sparse symbolic/program search -> small learned mapping -> higher-capacity learner only if the simpler hypothesis class is demonstrably inadequate.

This keeps frontier science interpretable and makes it possible to identify what new computational complexity was actually necessary.

### Step 8 — Promote by causal evidence, not by desirable phenotype

A frontier mechanism earns standing only when the **predicted causal pattern** survives:

- ablation;
- intervention;
- mismatched/random controls;
- multiple seeds;
- altered ecology;
- developmental variation;
- comparison with plausible rival mechanisms.

A mechanism is not promoted merely because it produces kindness, cooperation, or low harm.

## The evaluator is the dangerous part

The automated-discovery literature also sharpens a major risk.

Program search is only as scientifically meaningful as its evaluator.

If REE asks a search process to "maximise kindness", "minimise harm", or optimise a single prosocial score, the search can discover:

- deletion of harmful affordances;
- avoidance of other agents;
- metric suppression;
- appeasement;
- proxy gaming;
- hard constraints that mimic ethics without agency.

That would collapse REE back into reward engineering.

Therefore the REE evaluator should be a **multi-test causal adjudication battery**, not a scalar moral fitness function.

Where an aggregate score is needed for search mechanics, it should be downstream of hard validity gates and should not permit compensation: e.g. excellent repair behaviour must not compensate for failure of the live-unethical-affordance requirement.

The evaluator should ask whether the mechanism instantiates the claimed causal structure, not whether the resulting phenotype looks morally attractive.

This is likely the central human scientific role in frontier REE development: defining the meaningful discriminations, prohibited shortcuts, and falsifiers that keep automated mechanism search attached to the axioms rather than to superficial output.

## Revised interpretation of the investigator's role

For frontier mechanisms, the human role need not be:

> invent the correct learning algorithm and then code it.

A literature-backed alternative is:

> define the phenomenon precisely enough that competing mechanisms can be generated, made executable, and killed by discriminating experiments.

The implementation/search system can propose code.
The forge can execute experiments.
The governance layer can prevent invalid promotion.
The investigator remains responsible for whether the experiment actually bears on the intended ethical proposition.

This is not a retreat from scientific authorship. It is a redistribution of scientific work around specification, falsification, and experimental adjudication.


## Central methodological commitment

The project should preserve the following rule:

> **REE must be allowed to discover mechanisms that the literature does not yet contain, and must be allowed to reject mechanisms that its own philosophy predicts.**

Literature constrains priors.
Architecture makes hypotheses executable.
Experiment decides what survives.

For the parts of REE that are genuinely new, that may be the only scientifically honest route.
