# Thought intake: failure-directed comparative biology — let REE's causal failures generate neuroscience questions

**Date:** 2026-09-26  
**Status:** intake / candidate methodology — do not register a new claim automatically  
**Origin:** discussion following the dynamic-control governance/autopsy pass: literature searches are becoming more useful when REE's own failures specify the biological question, rather than when biology is searched broadly for components to copy.

**Primary REE anchors:**
- `docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md`
- `evidence/planning/dynamic_control_audit_20260926.md`
- `evidence/planning/dynamic_control_audit_inventory_20260926.md`
- `evidence/planning/dynamic_control_audit_biology_20260926.md`
- latest commit-gate read on absorbing commitment / GFLAG-0486
- `evidence/planning/thought_intake_2026-09-26_nicotinic_habit_routing_gate.md`
- `evidence/planning/thought_intake_2026-08-11_behavioural_adjudication_scientific_skill.md`

---

## 1. Seed idea

REE may have reached a stage where its most informative use of biological literature is no longer:

> **What mechanism does the brain have that REE should copy?**

but instead:

> **REE has failed in this specific causal way. What class of problem is this, does biology face an analogous problem, and what families of mechanisms allow biological systems to solve it?**

The distinction is important.

The first question encourages architecture-by-analogy. It begins with an attractive biological mechanism and risks importing it because it sounds plausible.

The second begins with an observed failure in an artificial organism. The failure defines the computational problem before biology is consulted. Biology can then constrain the candidate solution space, suggest hidden variables, reveal distinctions REE has collapsed, and provide intervention ideas. Those candidates must still survive causal tests inside REE.

This creates a possible reciprocal research loop:

**REE causal failure**
→ **mechanistic problem statement**
→ **targeted comparative-biological search**
→ **candidate solution families / hidden variables / timescales**
→ **minimal competing REE implementations or interventions**
→ **causal discrimination / falsification**
→ **updated architecture or rejected hypothesis**
→ **next organism-level failure**.

The literature is therefore not an oracle and the brain is not a blueprint.

Biology becomes a **comparative experimental resource**.

REE becomes not merely a neuroscience-inspired architecture, but an artificial system capable of generating increasingly precise questions for neuroscience as its own internal machinery begins to interact in non-trivial ways.

---

## 2. Why this becomes possible only now

Earlier in REE development, many failures were too coarse to generate useful biological questions.

Examples included:
- a representation was absent;
- a consumer was unwired;
- a signal was not trained;
- a harness did not induce the intended state;
- an experiment lacked a discriminating positive control;
- a subsystem simply did not yet exist.

At that stage a query such as “how does the brain coordinate cognitive regimes?” would have been premature and underconstrained. Almost any cognitive-control paper could have been made to sound relevant.

The recent autopsies are different.

REE increasingly contains locally functioning prediction, valuation, action selection, commitment, threat, veto, exploration, plasticity, memory and route-selection machinery. Failures can therefore arise **between mechanisms that each work locally**.

That produces sharper problem statements:

- a learned control quantity changes scale while its threshold remains fixed;
- a strong regime suppresses the observations needed to decide whether that regime should end;
- a controller reaches action selection but another controller has already removed the action-space degrees of freedom over which it could exert causal influence;
- a commitment variable becomes almost immediately absorbing because its update rule and initialization dominate the information it was meant to represent;
- a surprise signal cannot distinguish “large but expected noise” from “the world has changed” because the organism lacks a model of its own recent error distribution;
- deliberative actions can be executed and reinforced, but the rule by which repeated successful constructions become eligible for cheap habitual proposal remains incomplete.

These are no longer generic “intelligence” problems.

They are identifiable control, inference, learning and state-transition problems.

That makes a targeted biological comparison scientifically meaningful.

---

## 3. The key methodological inversion

### Old direction

**Biology → mechanism → REE implementation → test**

This remains useful when there is a well-defined missing competence, but it has several hazards:

1. **Prestige bias:** a biologically fashionable mechanism is implemented because it is interesting rather than because REE needs it.
2. **Anatomical literalism:** a biological structure is copied when only its computational property matters.
3. **Single-paper overfitting:** one explanatory framework is treated as more settled than the field warrants.
4. **Mechanism inflation:** each new paper adds another subsystem rather than constraining existing machinery.
5. **Oracle leakage:** an experimenter supplies the very regime classification or target state the organism was supposed to infer endogenously.

### Proposed direction

**REE failure → causal localization → biological question → candidate mechanism classes → discriminating REE intervention**

This reverses the epistemic priority.

The artificial organism supplies the problem.

Biology supplies candidate ways evolved systems may have encountered related constraints.

REE then determines whether those candidate principles are sufficient, necessary, redundant, harmful or irrelevant in this artificial setting.

That result does **not** prove that the brain uses the winning REE mechanism. It can, however, sharpen the biological question and identify which computational properties deserve direct biological testing.

---

## 4. Worked examples from the present frontier

### 4.1 Absorbing commitment

**REE observation:** the current commitment gate rapidly becomes effectively permanent across distinct arms. The observed crossing is strongly shaped by the initialization / exponential-moving-average / fixed-threshold geometry, while the underlying “prediction error” has timing semantics that mix predicted displacement, realised one-step error and increasingly stale error.

**Bad literature query:**
> What brain area controls commitment?

**Failure-directed query:**
> How do biological decision systems maintain stable commitment while preserving evidence-sensitive reversibility when confidence statistics, prediction-error scale and environmental contingencies change?

Useful literatures may include:
- hysteresis and decision commitment;
- metastable neural dynamics;
- change-point detection;
- evidence accumulation with reversal;
- adaptive confidence thresholds;
- locus-coeruleus reset / unexpected uncertainty;
- basal-ganglia hold/update gating;
- homeostatic reference tracking.

The goal would not be to import one of these wholesale. It would be to identify candidate *computational invariants*: relative rather than absolute thresholds, slow/fast opponent variables, context-dependent reset, explicit change-point evidence, bounded persistence, or parallel escape channels.

### 4.2 Freeze suppressing its own release evidence

**REE observation:** a strong defensive regime can suppress the interaction required to generate the evidence its own release pathway expects.

This is stronger than “the freeze threshold is too low.” It is a closed-loop informational failure:

**state → behaviour suppression → evidence suppression → inability to infer that the state should end**.

**Bad literature query:**
> What neurotransmitter ends freezing?

**Failure-directed query:**
> When biological systems enter defensive states that reduce exploration and action, which information channels remain capable of detecting changed conditions and causing an adaptive transition out of the state?

Candidate solution classes to look for:
- parallel sensory monitoring that survives motor suppression;
- opponent-process decay;
- spontaneous low-cost probing;
- internal time/state uncertainty accumulation;
- neuromodulatory reset signals;
- escape thresholds driven by evidence unavailable to the suppressed policy;
- multiple defensive substates rather than binary freeze/unfreeze.

REE could then test these as competing architectural properties rather than implementing a named biological pathway.

### 4.3 Expected noise versus world change

**REE observation:** a candidate shift detector can react to surprising events yet fail to distinguish a true action-map change from large surprise in an unchanged environment.

The biological comparison has already been useful here. Acetylcholine / norepinephrine theories distinguish uncertainty expected under the current model from unexpected uncertainty suggesting the regime itself changed.

That suggests a concrete hidden variable REE may lack:

> **a model of its own recent error statistics under the current inferred regime**.

The important advance is not “add norepinephrine.”

It is:

> instantaneous error magnitude and evidence for model/regime change are different computations.

That distinction can be implemented abstractly and tested without pretending the artificial variable is literally norepinephrine.

### 4.4 Safety veto without behavioural authority

**REE observation:** a veto can be locally functional and causally connected yet behaviourally irrelevant if another controller has already collapsed the executable action repertoire.

**Failure-directed query:**
> How do biological control systems preserve enough behavioural degrees of freedom for multiple constraints to matter without requiring a single central arbitrator?

This points toward literatures on:
- basal-ganglia pathway competition;
- thalamocortical gating;
- distributed inhibition/disinhibition;
- salience and gain competition;
- reciprocal inhibition;
- hierarchical versus parallel action selection;
- state-dependent routing;
- oscillatory/synchrony-mediated coordination.

The crucial test in REE is controller composition: after correcting each controller individually, do they coexist appropriately? If yes, a new arbitration mechanism is unnecessary. If not, the interaction itself becomes the target.

### 4.5 Deliberative-to-habit migration

**REE observation:** deliberative and habitual proposal routes can be conceptually separated, and repeated successful action should eventually permit cheap direct proposal, but the write rule deciding which practised actions earn that privilege is incomplete.

The nicotinic/cholinergic search produced a valuable refinement: nicotinic signalling is more plausibly interpreted as part of a temporally structured **credit/write filter** than a simple “habit switch.”

That changes the REE question from:

> what turns habit on?

to:

> what evidence allows an executed deliberative construction to be selectively consolidated into a directly routable habitual proposal without simply rewarding repetition?

Again the literature has exposed a missing distinction rather than supplied a module.

---

## 5. Search discipline: query the failure, not the architecture

For a major REE failure, the literature pull should begin only after a compact causal failure statement exists.

A useful template:

### A. Observed failure
What changed in behaviour or internal state?

### B. Earliest demonstrated causal break
Where in the chain did the intended information or control cease to matter?

### C. Closed-loop consequence
Did the failure itself change what evidence became available next?

### D. Missing computational property
Phrase this without biological nouns if possible.

Examples:
- stable but reversible commitment;
- scale-invariant thresholding;
- distinction between expected variance and regime change;
- escape evidence that survives the regime;
- preservation of action-space degrees of freedom under multiple constraints;
- temporally selective credit assignment;
- state-dependent controller authority.

### E. Comparative biological question
Ask how nervous systems solve **that property**, not which brain structure “does” the REE function.

### F. Candidate solution families
Extract several competing mechanisms, including contradictory or negative evidence.

### G. Translation layer
For each mechanism identify:
- information required;
- timescale;
- local versus broadcast character;
- update rule;
- controlled variable;
- failure mode;
- what would be observable if it were causally active.

### H. Minimal REE discrimination
Design the cheapest intervention capable of separating the candidate properties.

Only after this should implementation be considered.

---

## 6. A hierarchy of biological transfer

Not all biological resemblance deserves equal weight. A useful hierarchy may be:

### Level 0 — metaphor
“REE has something a bit like dopamine.”

Useful for intuition only.

### Level 1 — functional analogy
Both systems require, for example, credit assignment or adaptive thresholding.

Potentially useful, but still weak.

### Level 2 — computational property
A biological mechanism demonstrates that the problem can be solved by, for example, comparing current error against a learned error distribution rather than raw magnitude.

Strong enough to motivate an abstract REE candidate.

### Level 3 — discriminating prediction
The biological account implies that manipulating variable X while holding Y fixed should change transition behaviour but not local prediction accuracy, or vice versa.

This can directly structure a REE experiment.

### Level 4 — convergent causal structure
Multiple biological literatures and REE interventions independently favour the same abstract causal organization.

This is the strongest useful transfer, while still stopping short of claiming biological identity.

The aim of literature work should increasingly be to move from Levels 0–1 toward Levels 2–4.

---

## 7. Non-oracular constraint

This methodology only works if biology does not silently provide information that the organism itself should have to infer.

A literature-derived mechanism is invalid as an REE solution if its implementation requires the experimenter to provide labels such as:

- “the environment just changed”;
- “this is noise”;
- “you should explore now”;
- “the threat is over”;
- “this action is now a habit”;
- “the current controller is wrong.”

The question must always be:

> What endogenous measurements could allow the organism to infer this distinction for itself?

The biological literature is most valuable when it points to such measurements:
- recent prediction-error distributions;
- relative signal scale;
- temporal coincidence;
- running utility;
- rate of environmental change;
- reliability history;
- competing-pathway balance;
- internally generated probes;
- state duration;
- mismatch across timescales.

A biological mechanism that only works because the experimental description already knows the answer is not a solution to REE's problem.

---

## 8. Why negative biological evidence is unusually valuable

This method should actively seek biology that contradicts an attractive REE mapping.

Examples:
- acetylcholine is not simply “pro-habit”;
- serotonin is not simply “inhibition”;
- dopamine is not a universal reward/choice scalar;
- norepinephrine is not merely “arousal”;
- basal ganglia are not a single action switch;
- oscillatory coordination is not evidence for a master clock.

Contradictory findings help identify when REE has compressed several biological functions into one artificial variable or assigned one variable too many jobs.

A search that only returns support for the proposed implementation should therefore be treated as incomplete.

The preferred output is not “biology agrees.”

It is:

> these are the competing biological solution families, these are the distinctions the current REE implementation collapses, these are the observations that would separate them.

---

## 9. REE can return questions to biology

The loop may eventually become genuinely bidirectional.

Suppose several abstract solutions are instantiated in REE and only one family supports:
- stable commitment without lock-in;
- recovery after contingency change;
- preservation of local controller function;
- development across changing signal scales;
- appropriate novel-context behaviour.

That does not prove biology uses the same solution.

But it may generate a sharper biological question than existed beforehand:

> In animals, is regime exit driven primarily by decay within the active state, by a parallel change detector, by internally generated probing, or by opponent circuitry carrying evidence unavailable to the active policy?

REE can therefore act as a **hypothesis refinery**.

It can take broad biological theories that are difficult to distinguish in vivo, instantiate their abstract causal commitments in a small artificial organism, and identify where their predictions actually diverge.

Those divergences can then suggest better biological experiments.

This is especially promising at the current REE frontier because the problems involve interacting systems and closed loops, where verbal theories can easily appear compatible until forced to control the same behaving organism.

---

## 10. Relationship to REE's primary scientific purpose

This methodology remains subordinate to REE's central purpose: building an artificial testbed in which the ethical axioms and derivations can become causally operative, stressed, falsified and refined.

Failure-directed comparative biology is valuable because a meaningful ethical agent requires non-trivial:
- uncertainty;
- vulnerability;
- prediction;
- learning;
- commitment;
- self/other modelling;
- action;
- consequences;
- memory;
- behavioural flexibility.

If the cognitive machinery coordinating those capacities is brittle, permanently locked, externally labelled or dependent on arbitrary scale constants, then later ethical-looking behaviour will be difficult to interpret causally.

Thus this method is not a diversion into neuroscience mimicry.

It is a way to improve the experimental apparatus so that ethical hypotheses can eventually be tested in an agent whose behaviour genuinely depends on its own uncertain models and endogenous control processes.

The ethical claims must still be allowed to fail.

Likewise, the biological analogies must be allowed to fail.

---

## 11. Candidate methodological principle

**Candidate principle — failure-directed comparative biology**

> Once a REE failure has been causally localized, biological literature should be searched for organisms' solutions to the same abstract control/inference/learning problem. The resulting mechanisms should be translated into competing computational properties and tested by minimal causal interventions in REE. Biological resemblance alone is not evidence; value comes from constraining hypotheses and generating discriminating experiments.

This may be better treated as a **scientific-method rule** than as an architectural claim.

Possible governance homes could include:
- behavioural/scientific adjudication procedure;
- literature-pull discipline;
- metaworker/orchestrator experiment-planning guidance;
- failure-autopsy follow-up procedure.

Do not force it into `claims.yaml` if the claims system is intended only for empirical/architectural propositions.

---

## 12. Candidate research questions for governance consideration

Do **not** register automatically; reconcile with existing methodology and dynamic-control claims first.

### Q-A — Does failure-directed literature search outperform architecture-first literature search?
When REE has a localized causal failure, does searching the biological literature using the failure-defined computational property produce more discriminating experiments and fewer unnecessary mechanisms than searching from a named cognitive architecture or brain structure?

### Q-B — Are there recurring cross-domain solution motifs?
Across commitment, threat, habit, exploration, plasticity and attention, do biological solutions repeatedly use a small family of motifs — e.g. relative normalization, opponent processes, parallel change detection, multi-timescale state variables, preserved escape evidence, local receiver-specific gain — or are the mechanisms domain-specific?

### Q-C — Can REE expose biological theory degeneracy?
When two biological theories make similar verbal predictions, can instantiating their abstract causal commitments in REE reveal behavioural or internal-state interventions that distinguish them?

### Q-D — Does the organism itself become the literature-search curriculum?
As REE matures, do its successive organism-level failures naturally generate a progressively more specific sequence of neuroscience questions, reducing dependence on manually chosen architecture topics?

---

## 13. Immediate operational proposal

For the current dynamic-control frontier, literature work should no longer be a broad “cognitive control” sweep.

Each major autopsy should optionally emit a **comparative-biology query packet** containing:

1. causal failure statement;
2. earliest broken edge;
3. closed-loop consequence;
4. abstract missing property;
5. 3–6 targeted search questions across different biological literatures;
6. explicit request for conflicting/negative evidence;
7. extracted candidate solution families;
8. endogenous measurements each solution would require;
9. minimal REE interventions capable of separating them;
10. what result would make the biological analogy irrelevant.

The current highest-value query packets appear to be:

- **stable-but-reversible commitment / absorbing commitment escape**;
- **defensive freeze with regime-surviving release evidence**;
- **expected uncertainty versus true regime change**;
- **composition of multiple locally valid controllers without action-space collapse**;
- **adaptive operating-point control under learned scale drift**;
- **selective migration from deliberative construction to habitual proposal**.

These should be ranked by information gain about the organism bottleneck, not by literature volume.

---

## 14. Strong falsifiers / failure modes of this methodology

This proposal should itself be allowed to fail.

It is weakened if:

- failure-directed searches repeatedly recover only generic analogies and do not improve experiment design;
- biology systematically adds complexity without narrowing hypotheses;
- abstract mechanisms that work in REE bear no useful relation to biological evidence;
- REE failures are mostly implementation-specific artefacts with no meaningful organism-level analogue;
- architecture-first engineering solves the problems more simply and with equal causal clarity;
- the methodology creates confirmation bias by finding a biological story for every failure;
- literature-driven candidates converge only because the same small set of fashionable neuroscience frameworks is repeatedly reused.

Guard against these by keeping a control condition where appropriate:

> **What is the simplest non-biological engineering explanation and intervention for this failure?**

If that explanation is sufficient and more discriminating, prefer it.

Biology earns influence only when it adds explanatory or experimental leverage.

---

## 15. Central thought

The most important shift may be this:

> **REE does not need to ask neuroscience what a mind should contain. It can increasingly ask neuroscience what kinds of solutions exist for the exact problems its own emerging mind encounters.**

That is a much stronger relationship between the project and cognitive science.

REE becomes neither a copy of the brain nor an isolated engineering exercise.

It becomes an artificial organism whose failures generate mechanistic questions, whose design allows those questions to be causally tested, and whose results can in turn sharpen the questions asked of biological cognition.

The organism can become part of the research method.
