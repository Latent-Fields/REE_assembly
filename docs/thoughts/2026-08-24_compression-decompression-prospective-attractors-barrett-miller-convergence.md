# Compression, decompression and prospective attractors: Barrett–Miller convergence with REE

Status: processed
Intake: evidence/planning/thought_intake_2026-08-24_compression-decompression-prospective-attractors-barrett-miller-convergence.md
Claims registered: MECH-507, MECH-508, MECH-509, MECH-510, MECH-511, MECH-512, INV-103

Date: 2026-08-24

Source: discussion prompted by Conor Feehly, “A New Framework for How the Brain Compresses Our Noisy World,” *Quanta Magazine*, 24 August 2026, and the underlying Perspective by Lisa Feldman Barrett and Earl K. Miller, “Categorization is ‘baked’ into the brain,” *Nature Reviews Neuroscience* 27, 435–456 (2026), DOI: 10.1038/s41583-026-01036-2.

This is a raw/refined thought intake for the full Reflective–Ethical Engine (REE) lineage. It is not a registered mechanism or claim. It should be compared against current REE claims and implementation before promotion.

## Originating observation

> “Wow. This is describing REE like processes very closely if not exactly how I imagine them”

and, after a detailed comparison:

> “These might be people I could ask questions of REE. The convergence is quite extraordinary”

The important point is not that Barrett and Miller use the language of predictive processing. That overlap alone would be unsurprising. The striking convergence is narrower and more structural: **compression into low-dimensional multimodal state; prospective generation of possible sensorimotor futures; internal-state-conditioned interpretation; precision-weighted reconciliation with incoming evidence; and selective learning from mismatch, in approximately that causal order.**

REE then continues through mechanisms that Barrett and Miller are not attempting to specify: extended counterfactual evaluation, a hard simulation-to-action commitment boundary, ownership, responsibility-bearing residue, self–other ethical coupling, and constrained offline authority.

This document therefore treats the paper as a potentially important biological and computational cross-check on REE’s *pre-commitment cognition*, while preserving the places where the two frameworks diverge.

## Barrett–Miller mechanism, in REE-relevant terms

Barrett and Miller argue against a filing-cabinet model in which perception is first assembled from sensory features and only then matched to a stored category. In their account, categorisation is present throughout processing. Predictive feedback provides a context that shapes the meaning of feedforward signals from the outset.

Several pieces are especially relevant to REE.

### 1. Compression is an active organising operation

High-dimensional sensory and bodily signals are progressively compressed into lower-dimensional summaries. These summaries preserve what is useful for current control while discarding detail. Different high-dimensional situations can therefore become functionally equivalent if they imply sufficiently similar action-relevant consequences.

This is stronger than saying that the nervous system merely has a latent representation. It suggests an explicit reciprocal operation:

**high-dimensional experience → compression → lower-dimensional organising state**

followed by:

**lower-dimensional organising state → decompression → higher-dimensional predictions and possible actions**

REE already contains latent representations, persistent context and multi-timescale predictive state. What appears newly useful is making **compression/decompression itself an explicit bridge abstraction** rather than leaving compression implicit in representation learning.

### 2. Low-dimensional state is prospective, not merely descriptive

The compressed state does not merely summarise “what is there.” Barrett and Miller describe low-dimensional multimodal summaries as sources of predictions about possible future bodily regulation, motor activity and resulting sensations.

In REE language, the latent state is therefore not best understood as a static label or memory key. It can be a **generative disposition over possible trajectories**.

This substantially sharpens the current attractor idea.

### 3. Categories are dynamic events rather than stored objects

A category in this account is constructed in the moment from history, context, bodily state and current purpose. It is not necessarily a permanent symbolic item stored intact in memory. Its useful equivalence class can change according to what the organism is trying to do.

This suggests that an REE attractor should not be represented as a proposition such as “this is threat” or as a fixed memory object. A better candidate formulation is:

> **An attractor is a compressed, history-conditioned generative disposition defining a family and probability distribution of possible sensorimotor trajectories. Its precision controls how strongly that family constrains interpretation and future generation; incoming precision-weighted discrepancies may select within it, modify it, or — if sufficiently consequential — remodel or displace it.**

The attractor is therefore partly a *way of generating the next hypothesis space*.

### 4. Decompression may precede expensive explicit rollout

A single compressed multimodal summary can generate a grouping of possible future movements and sensations. This raises a useful architectural possibility for REE:

**compressed context/attractor → decompressed possibility field → sampled candidate trajectories → extended E2/hippocampal rollout**

The “possibility field” is not yet a claim that Barrett and Miller have identified an REE-style rollout mechanism. Their prospective alternatives need not be explicit long-horizon sequences. The useful inference is computational: a cheap generative field of plausible/functional futures could exist *before* expensive trajectory simulation.

This may help both conceptual clarity and compute efficiency. Instead of asking hippocampal rollout to invent trajectories from an unconstrained space, a lower-cost decompression stage could first define a structured distribution from which a smaller number of trajectories are sampled for extended simulation.

### 5. Incoming evidence constrains rather than dictates

In the Barrett–Miller account, predictive feedback and feedforward signals interact. Incoming evidence can confirm, constrain or contradict the generated possibilities. Prediction error is therefore not an oracle that directly replaces the current model.

This is highly consonant with the recent REE requirement for **non-oracular injections**.

A useful REE rule is:

> **No injection may directly set the truth-state of E1. It may supply evidence capable of modifying E1 only through ordinary precision-, provenance-, and learning-eligibility machinery.**

REE should extend the biological formulation with explicit provenance. A statement from another agent, direct sensory evidence, an internally generated counterfactual and an externally injected datum may share representational format without becoming epistemically identical.

### 6. Precision has more than one target

Barrett and Miller distinguish the strength/reliability of predictions from the weighting of prediction errors. REE already treats precision as heterogeneous rather than scalar, but this suggests a useful implementation refinement:

- **prediction precision**: how strongly a generative attractor constrains interpretation and proposal generation;
- **prediction-error precision / salience**: how much a discrepancy is trusted and how strongly it is allowed to drive correction or learning.

These quantities need not move together.

An overprecise prediction with underweighted error produces capture. Noisy but highly salient errors can produce instability. A mature control plane may need to route them separately.

### 7. Not every error deserves deep learning

A particularly useful part of the paper is its proposal that the value of a prediction error depends on its anticipated relevance to future allostatic control. Error magnitude alone is insufficient.

REE should not import metabolism as its complete objective. REE’s relevant future consequences include bodily viability but also self-continuity, other agents, harm, commitments, social consequences and responsibility.

The transferable idea is **learning eligibility**:

`deep-update eligibility = f(error, error precision, future relevance, organism/other consequence, provenance, current mode)`

Possible routing might be:

- low-consequence mismatch → local correction;
- significant mismatch → retain as pending integration material;
- high-confidence/high-consequence mismatch → waking adaptation and active information seeking;
- contradiction of a deep attractor → preserve and contest rather than immediately rewrite;
- accumulated or structurally important contradiction → counterfactual reprocessing and possible offline revision.

These routes are REE synthesis, not claims made by Barrett and Miller.

### 8. Representational granularity is itself a control problem

Barrett and Miller discuss failure at both extremes of abstraction. Too much compression can overgeneralise; too little compression can prevent useful generalisation and leave the system overly concrete or uncertain.

This is especially important in light of `2026-08-23_memory-dimensionality-crystallisation.md`. REE already has a live question about whether representational bucket number and dimensionality should be learned and environment-dependent. Barrett and Miller add a complementary point: **the level of abstraction selected at a moment may itself be functionally consequential.**

This may be distinct from both memory capacity and confidence.

A candidate control variable is therefore **representational granularity / compression depth**.

## Two independent attractor failure axes

Recent REE discussion focused on an attractor becoming too “sure” and consequently becoming the perceptual lens through which ambiguous evidence is interpreted.

The Barrett–Miller framework exposes a second, separable failure axis.

### Excessive precision

The agent effectively says:

> this generative hypothesis is extremely certain.

The attractor strongly constrains interpretation, retrieval and future generation.

### Excessive compression / generalisation

The agent effectively says:

> too many different situations belong to this equivalence class.

Distinct contexts are collapsed into the same action-relevant representation.

These can interact but should not be conflated.

A threat attractor can therefore become pathological because it is **too confident**, because it is **too broad**, or both.

This gives a cleaner computational-psychiatry coordinate system than precision alone. It also generates obvious experimental dissociations: hold confidence constant while changing the breadth of the equivalence class, and vice versa.

## Threat attractor example

A threat attractor need not contain a proposition like “this is dangerous.”

Instead it may decompress into a family containing:

- vigilance;
- withdrawal;
- attack;
- freezing;
- expected bodily changes;
- selective attention to ambiguous cues;
- threat-consistent memory retrieval;
- expectations about what the environment will do next;
- downstream action consequences.

If the attractor becomes overprecise, it generates a threat-shaped hypothesis space *before* ambiguous evidence arrives.

Incoming evidence can then do at least two importantly different things:

1. **select within the generated family** — determining which threat exemplar best fits; or
2. **remain as residual mismatch capable of revising the generative source**.

A failure occurs when the system treats every mismatch only as information for selecting within the existing family. The attractor then becomes difficult to falsify because its own hypothesis space defines what counts as an explanation.

This is the computational form of the recent “perceptual lens” thought.

## Mapping to current REE architecture

The present REE README describes:

- **E1** as a persistent, slow predictive substrate maintaining coherent self/world/value state;
- **E2** as a fast action-conditioned forward predictor over motor-sensory state;
- a **hippocampal module** that proposes imagined trajectories without commitment;
- a heterogeneous **control plane** routing precision and mode;
- a **multi-rate clock**;
- **offline integration** that consolidates and contextualises experience;
- **E3** as trajectory selection and commitment machinery;
- a hard **commitment boundary** separating hypothetical simulation from owned action;
- **residue** as persistent consequence trace after commitment.

Against that architecture, the Barrett–Miller convergence is strongest *before commitment*.

A useful combined sketch is:

**experience + autobiographical history + internal/body state**

→ **compression**

→ low-dimensional context-sensitive generative state `z_t`

→ **decompression**

→ `P(possible sensorimotor futures | z_t, current context)`

→ cheap possibility field

→ hippocampal sampling / counterfactual extension + E2 action-conditioned rollout

→ candidate trajectories `{τ1 ... τn}`

→ precision-weighted incoming evidence + affect + organism/other-agent state

→ candidate refinement / E3 evaluation

→ **COMMITMENT BOUNDARY**

→ owned action

→ real consequence + responsibility-bearing residue

→ prediction error / learning eligibility

→ local waking update and/or bounded pending material

→ offline integration / possible deep attractor revision

→ changed future compression/decompression landscape.

The last line may be particularly important:

> **Experience is not simply stored. It changes what the organism subsequently compresses together as equivalent, which changes what futures it can subsequently imagine.**

## Relation to existing REE thoughts rather than duplication

This thought should not replace several closely related documents already in the repository.

### `2026-08-24_offline-representational-reindexing-counterfactual-model-comparison.md`

That document addresses what happens when representational primitives change: preserving evidence, reindexing memory, matched replay under competing models, provenance, waking validation and rollback.

The present thought adds a potential *upstream reason* such reindexing becomes necessary: the compression/decompression structure itself may change, altering equivalence classes and the futures generated from them.

### `2026-08-23_memory-dimensionality-crystallisation.md`

That document asks whether the number/granularity of representational buckets should be environment-conditioned and developmentally plastic rather than fixed.

The present thought adds **momentary functional granularity** and a biological/computational account of why abstraction depth matters for prediction and action.

### `2026-08-19_context-inference-active-persistent-control.md`

That document treats active context as a persistent inference process with uncertainty, orienting, hysteresis, context creation and exploitation windows.

The present thought provides a possible internal form for the active context: a compressed generative disposition whose decompression shapes which candidate futures are available.

### Earlier multi-timescale / precision / hippocampal work

REE already contains heterogeneous precision, multi-rate processing, hippocampal proposal generation, contextual memory and prospective trajectory machinery. The Barrett–Miller paper is therefore not being treated as the origin of those ideas in REE. Its value is the way these elements are arranged together and the additional abstractions it suggests.

## Waking versus offline revision

The Barrett–Miller Perspective does **not** establish REE’s waking/offline authority distinction. It should not be cited as evidence that deep updates must occur in sleep.

However, its mechanism combines naturally with the separate REE sleep/offline thought.

During waking, REE may need to:

- maintain viable control;
- update probabilities locally;
- reduce authority of a suspect attractor;
- seek discriminating evidence;
- preserve high-value unresolved mismatch;
- perform bounded counterfactual tests;
- avoid destabilising the whole representational basis while action is ongoing.

During protected offline processing, REE may be able to:

- gather several high-value unresolved errors together;
- temporarily relax the precision of a dominant attractor;
- re-decompress affected representations under alternative models;
- replay preserved evidence while retaining provenance;
- reconsider older autobiographical episodes whose interpretation depended on the old compression scheme;
- split, merge or alter equivalence classes;
- compare candidate revisions before restoring waking action authority.

This remains an REE-specific architectural proposal.

## Developmental staging

Barrett and Miller’s framework is compatible with the idea that useful abstraction is learned from experience and that representational competence changes with development. It does **not** establish REE’s particular developmental stages or delayed E3 coupling.

A useful REE hypothesis is nevertheless visible:

> development may partly consist of learning what to compress together, how far to compress it, and how to decompress abstract state into useful prospective possibilities without losing access to corrective detail.

A young system may therefore require higher plasticity not only in weights/policies but in the *equivalence structure of its world*.

Crystallisation should not mean immobility. It may mean progressively stronger priors over useful abstraction structure combined with preserved capacity for revision when persistent high-value error shows the environment has been mis-partitioned.

## Biological timing and oscillatory inspiration

Barrett and Miller also discuss spatial and temporal gradients in neural processing and different frequency regimes associated with feedforward and feedback signalling.

This may be relevant to REE’s multi-rate clock:

- faster, higher-dimensional error-rich signals could correspond conceptually to rapid evidence streams;
- slower, lower-dimensional feedback/context signals could correspond conceptually to persistent organising state;
- interaction across these rates may implement repeated compression–prediction–correction cycles.

This is **inspiration only**. REE should not literalise cortical gamma or alpha/beta rhythms in software simply because the analogy is attractive. The useful claim, if any, is about heterogeneous timescales and information dimensionality, not frequency matching.

## Critical distinctions that must not collapse

### Barrett–Miller selection is not REE commitment

Their account describes how one of many possible futures can become the present through predictive constraint and incoming evidence.

REE’s commitment boundary carries an additional architectural role: the action becomes **owned**, responsibility becomes attributable, and real consequences become eligible for responsibility-bearing residue.

Perceptual/action selection upstream of commitment is therefore not enough to identify E3’s commitment operation.

### Prediction error is not residue

Prediction error is mismatch used for inference and learning.

REE residue is a persistent trace associated with owned real-world consequence. A simulated future can generate prediction differences without generating responsibility-bearing residue.

### The limbic core is not an REE module

The biological “narrow waist” is an appealing analogy for a region where compressed internal, external and remembered information interact. It should not be mapped one-to-one onto E1, E3, the control plane or any other single REE component.

If useful, the analogy is to an **integrative compressed interface spanning several REE functions**.

### Allostasis is not REE ethics

Barrett and Miller ground meaning heavily in predicted bodily/energetic consequence.

REE includes bodily viability, but its value structure also includes other agents, harm, responsibility, commitments and autobiographical continuity. Helping another agent may be energetically costly and still be required by REE’s architecture.

Metabolic/allostatic control can therefore inform REE’s viability machinery without replacing its ethical structure.

### Prospective categorisation is not proof of explicit counterfactual rollout

A distribution of possible futures is not the same thing as an extended hippocampal simulation of several temporally structured trajectories.

The useful mapping is hierarchical rather than identificatory:

**compressed state → possibility field → sampled trajectory → extended rollout**.

### Psychiatric examples should remain hypothesis-level

Barrett and Miller discuss abstraction-related failure modes and neuropsychiatric implications, but their paper should not be treated as proof of REE’s existing psychosis, depression or autism formulations. REE can use the framework to derive experiments and failure axes without claiming disease validation.

## Candidate mechanisms / claims to consider later

These are candidates for structured intake and claim harvesting, not registrations made by this raw thought.

1. **Reciprocal compression/decompression bridge** — E1-like persistent context should be capable of generating structured higher-dimensional sensorimotor possibility distributions rather than serving only as stored context.

2. **Prospective attractor definition** — an attractor is a compressed generative disposition over a family of trajectories, not merely a stored representation or confidence-bearing proposition.

3. **Pre-rollout possibility field** — cheap decompression should be tested as a proposal distribution from which expensive hippocampal/E2 rollouts are sampled.

4. **Dual precision routing** — prediction precision and prediction-error precision/salience should be experimentally separable.

5. **Deep-update eligibility** — durable revision of E1 or deep attractors should depend on precision, provenance and predicted future consequence/control relevance, not raw error magnitude alone.

6. **Adaptive representational granularity** — compression depth/generalisation should be treated as a variable separable from confidence/precision and from total representational capacity.

7. **Non-oracular evidence ingestion** — external injections may constrain internal state only through ordinary evidence, provenance, precision and learning-eligibility routes.

8. **Compression-history dependence** — deep learning should be evaluated not only by whether remembered content changes but by whether the equivalence classes used to generate future possibilities change.

## Candidate experiments

### Precision versus compression dissociation

Create two agents with equal nominal confidence but different breadth of context generalisation, and two with equal generalisation but different precision. Test whether threat-like capture, switching, false positives and recovery differ independently.

### Possibility-field efficiency

Compare:

- unconstrained hippocampal candidate generation;
- candidate generation sampled from a decompressed low-dimensional possibility field.

Measure compute cost, candidate diversity, coverage of viable trajectories and behavioural performance.

### Deep-update eligibility

Present prediction errors matched in magnitude but differing in future consequence. Test whether only consequential/high-value errors gain access to deep E1 revision while low-consequence errors remain local.

### Non-oracular injection

Inject externally supplied information that conflicts with a high-precision attractor. Verify that the information does not directly overwrite E1, retains provenance, and can alter the attractor only when evidence weighting and learning eligibility support it.

### Overcompression failure

Train a context system that collapses too many situations into one equivalence class while keeping confidence calibrated. Test for inappropriate transfer of action policies despite absence of overprecision.

### Offline restructuring

Accumulate persistent high-value contradictions while waking. Compare immediate structural revision with deferred offline reprocessing. Measure stability, catastrophic remapping, preservation of source evidence and subsequent generalisation.

### Behaviour-linked substrate analysis

Use the existing REE proposal for longitudinal substrate imaging to ask whether transitions in behaviour are preceded by identifiable changes in compression structure, attractor precision, possibility-field entropy or candidate-trajectory diversity.

## Questions worth asking Barrett and Miller

The degree of overlap makes direct scientific questions potentially useful. The best questions are not “does REE sound right?” but questions at the boundary where their framework exposes unresolved REE mechanisms.

### Revision versus exemplar selection

What determines when discrepant evidence merely selects a different exemplar within the current compressed category versus forcing revision of the compressed summary itself?

This is almost exactly REE’s deep-update problem.

### Precision versus abstraction

Do they regard the precision/confidence of a generative category and its degree of abstraction/generalisation as biologically separable variables?

This tests the proposed distinction between an overconfident attractor and an overbroad attractor.

### Decompression before sequence simulation

Do they envisage low-dimensional summaries decompressing into a probabilistic field of possible futures before anything like explicit hippocampal sequential simulation occurs?

This could support, reject or refine the proposed REE possibility-field layer.

### Contradictory evidence and established summaries

How does evidence revise a deeply established compressed summary when that same summary is already shaping how the contradictory evidence is interpreted?

This is the attractor-as-perceptual-lens problem.

### Error classes

Are there computationally distinct prediction errors used primarily for online selection versus errors that trigger durable representational learning?

This maps directly onto local correction versus deep-update eligibility.

### Offline structural change

Do they expect offline or sleep states to permit changes in compression structure that are difficult, destabilising or computationally expensive during active behaviour?

A negative answer would still be informative for REE.

### Agency discontinuity

If an organism must distinguish an action it simulated from an action it actually caused, where would they expect that causal/agency discontinuity to appear within their predictive architecture?

This introduces REE’s commitment-boundary problem without requiring them to accept REE’s solution in advance.

## Possible concise description of REE for correspondence

A useful introduction would focus only on the overlapping machinery:

> I have been developing an artificial-agent architecture in which a slow persistent predictive state generates candidate sensorimotor futures, precision-weighted evidence constrains them, and a separate commitment mechanism determines when a simulated trajectory becomes an owned action. Your compression/decompression framework appears to converge closely with much of the upstream machinery and has made me reconsider our representation of attractors and prediction-error learning.

Then ask one or two specific questions rather than presenting the whole REE programme.

## Why this convergence matters

The significance is not that a neuroscience Perspective has “validated REE.” It has not.

The significance is that a framework developed to explain biological categorisation independently places several operations that REE has been assembling for artificial cognition into an unusually similar causal arrangement:

**compressed multimodal state → prospective action-conditioned possibilities → internal-state-dependent meaning → precision-weighted evidence → selective updating.**

That is a much narrower conjunction than generic predictive processing.

It provides three kinds of value to REE:

1. **confirmation of plausibility at the level of organisation** — several REE intuitions correspond to a serious contemporary account of biological cognition;
2. **new abstractions** — especially explicit compression/decompression, possibility fields and adaptive representational granularity;
3. **new falsifiable questions** — especially the distinction between overprecision and overcompression, and between ordinary prediction error and deep-update-eligible error.

The most productive response is therefore neither to claim equivalence nor to treat the resemblance as cosmetic. It is to use the convergence to sharpen REE’s mechanisms, design discriminating experiments, and ask the authors questions at the places where REE and their framework nearly meet but do not yet coincide.

## Sources

- Barrett LF, Miller EK. “Categorization is ‘baked’ into the brain.” *Nature Reviews Neuroscience*. 2026;27:435–456. DOI: https://doi.org/10.1038/s41583-026-01036-2
- Feehly C. “A New Framework for How the Brain Compresses Our Noisy World.” *Quanta Magazine*. 24 August 2026. https://www.quantamagazine.org/a-new-framework-for-how-the-brain-compresses-our-noisy-world-20260824/

## Possible affected components

- E1 persistent predictive substrate / ContextMemory
- E2 fast action-conditioned prediction
- hippocampal proposal generation and counterfactual rollout
- attractor representation
- latent stack / representational granularity
- control plane precision and salience routing
- orienting and active evidence acquisition
- learning/plasticity gating
- non-oracular injection/provenance machinery
- multi-rate clock
- waking versus offline integration
- developmental plasticity/crystallisation
- E3 interface and commitment boundary, principally to preserve the distinction from upstream selection
- behavioural/substrate imaging experiments
- computational-psychiatry failure models
