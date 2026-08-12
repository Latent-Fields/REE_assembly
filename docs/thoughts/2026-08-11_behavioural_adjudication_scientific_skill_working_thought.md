# Working Thought: Behavioural Adjudication as a Scientific Skill for REE Assembly

Status: processed
Intake: evidence/planning/thought_intake_2026-08-11_behavioural_adjudication_scientific_skill.md
Processed in:
- docs/claims/claims.yaml#GOV-BEHADJ-1

**Editorial status of the thought itself (unchanged by intake):** provisional working thought; intended for literature mining, criticism, revision, and eventual skill development rather than immediate hardening into methodology. Registered as a candidate governance_rule (GOV-BEHADJ-1) so the proposal is tracked -- registration does not mean it has been hardened into a skill.

The recent organism-level Fishtank work suggests that REE Assembly may need a dedicated scientific skill for behavioural experiment design and adjudication.

This thought is intentionally provisional. It should not be treated as a finished methodology. Its purpose is to identify a methodological gap, preserve the reasoning that exposed it, and provide a scaffold for deeper literature searches, cross-disciplinary comparison, criticism, revision, and eventual implementation.

The central problem is that increasingly rich REE behaviour may not be well captured by a fixed set of scalar metrics chosen in advance. Recent Fishtank observations have made this particularly clear.

Some trajectories appeared, visually, to show coherent use of environmental structure: remaining within a relatively safe reef region, making excursions outward for exploration or food, returning, avoiding hazards, and sometimes appearing more purposeful later in a run. Separately, behaviour observed after sleep appeared potentially “smoother” than before sleep: not smooth in a literal geometric sense, since movement occurs on a grid, but perhaps involving fewer reversals, less local dithering, longer coherent runs, more direct approaches, or improved reuse of previously successful trajectory fragments.

These impressions may be genuine behavioural signals. They may equally be perceptual artefacts, consequences of environmental geometry, changes in general activity, stochastic variation, or effects that disappear with another sample.

The scientific challenge is therefore not to find a number that confirms what the observer believes they saw.

The challenge is to construct an umpire.

A useful guiding phrase is:

> **We never needed a ruler; we needed an umpire.**

The distinction matters. A ruler measures one selected property. An umpire adjudicates among competing explanations using multiple observations, perturbations, controls, and predictions.

A behavioural methodology for REE should therefore resist the temptation to define an interesting phenomenon through whichever measurement first appears convenient. If “smoothness” becomes “number of turns,” for example, the experiment may quietly cease to ask whether behaviour became more coherent and instead become an experiment about turn count. Similarly, if behavioural diversity becomes occupancy entropy, repeated strategic use of a refuge could mistakenly look behaviourally impoverished even if the organism is displaying a rich, context-sensitive strategy.

The proposed skill should preserve a separation between at least three levels of description:

**Observation:** what was actually seen or measured.

**Interpretation:** the behavioural organisation that might explain the observation.

**Mechanism:** the internal process proposed to produce that organisation.

For example, “Post-sleep trajectories contained fewer local reversals and longer directed runs” is an observational claim. “Post-sleep behaviour was more strategically organised” is an interpretive claim. “Sleep consolidated useful trajectory structure or altered policy selection” is a mechanistic claim.

Each level may be wrong independently of the others. This separation should be treated as a scientific safeguard.

## Behaviour should be treated as structured process, not merely as aggregate output

A substantial body of modern computational ethology and behavioural neuroscience argues that behaviour is organised across time into motifs, bouts, states, transitions, sequences, and sometimes hierarchical structures. Behavioural phenotypes can therefore disappear when reduced to marginal quantities such as total distance travelled, average speed, occupancy, or reward count.

This suggests that REE behavioural experiments should often examine not only how much of something occurred, but how behavioural states were organised and how the organism moved between them.

Two agents could, for example, spend identical proportions of time in refuge, exploration, feeding, and transit while displaying very different behavioural organisation.

One might alternate:

`refuge → explore → refuge → explore → refuge`

while another produces:

`refuge → exploration → food approach → acquisition → directed return to refuge`.

The aggregate behavioural totals could be identical while the behavioural strategy is substantially different.

Transition structure, temporal sequencing, behavioural persistence, and context-dependent switching may therefore be as important as state occupancy itself.

## Use both hypothesis-directed and discovery-oriented behavioural analysis

The skill should probably require two complementary analytical channels whenever practical.

The first is **hypothesis-directed**.

If a behavioural observation suggests smoother or more strategic navigation, relevant pre-specified measurements might include reversal frequency, path efficiency, approach abandonment, excursion duration, return-path efficiency, route reuse, hazard proximity, persistence of directed movement, goal latency, local oscillation, and transitions among refuge, exploration, food-seeking, acquisition, and return states.

The second is **discovery-oriented**.

It should ask:

> **What behavioural structure is present that we did not think to measure?**

Unsupervised behavioural methods in other fields attempt to discover recurring behavioural motifs, states, temporal clusters, or transition structures without assuming beforehand which dimensions are scientifically important.

The appropriate lesson for REE is not that unsupervised behavioural discovery should replace investigator-defined measurements. It is that the two approaches protect against different errors.

Top-down analysis tests predictions. Bottom-up analysis protects against blindness to unexpected organisation. Both may be needed.

## Variability must not automatically be classified as noise

REE contains genuine stochastic processes and exploratory behaviour. Accordingly, apparent randomness should not simply be treated as behavioural failure or measurement contamination.

Biological organisms sometimes use behavioural variability adaptively. Exploration, stochastic sampling, uncertainty management, predator avoidance, search behaviour, and mixed strategies can all involve variability that is functional rather than erroneous.

The important question may therefore not be:

> **Did behaviour become less random?**

but:

> **Did randomness become differently organised?**

A potentially important pattern would be one in which pre-sleep behaviour mixes random movement into goal pursuit, whereas post-sleep behaviour preserves stochastic exploration but exhibits more coherent movement once a goal-directed sequence begins.

A global entropy or tortuosity measure could miss this entirely.

The methodology should therefore ask whether variability is context-dependent, temporally structured, state-specific, adaptive, preserved where exploration is appropriate, and suppressed where previously learned action is useful.

## Behavioural observations should generate competing explanations

The Assembly agent should not move directly from observation to favoured mechanism. Instead, behavioural hypotheses should generate explicit rivals.

For an apparent post-sleep improvement, possible explanations might include genuine consolidation, state-dependent policy change, altered general activity, chance differences between seeds, environmental starting-position effects, food distribution effects, reduced exploratory drive, trajectory reuse, changes in action persistence, altered hazard sensitivity, or visual overinterpretation by the observer.

These rivals should not merely be listed. The experiment should attempt to make them disagree.

## Discriminating perturbations may be more informative than additional metrics

One of the strongest principles to incorporate is that a good behavioural experiment changes the world in a way that causes competing explanations to make different predictions.

Rather than asking only whether a behavioural score increases, ask:

- **If explanation A is true, what environmental change should preserve the behaviour?**
- **What change should break it?**
- **What change should be irrelevant and therefore leave it intact?**

This creates positive perturbations, destructive perturbations, and orthogonal negative controls.

Examples might include moving food while preserving refuge structure; altering refuge geometry while preserving food distribution; changing hazard locations; rotating or reflecting environmental layouts; introducing novel but functionally equivalent environments; changing irrelevant visual or spatial features; modifying starting locations; disrupting access to particular memory sources; comparing sleep against matched no-sleep intervals; and testing generalisation to environments where the same strategy requires a visibly different trajectory.

Such perturbations are particularly valuable because they adjudicate between mechanisms rather than merely increasing confidence in one descriptive statistic.

## Discovery and confirmation must remain distinct

The current behavioural observations are exploratory because they were noticed after viewing the trajectories. That is not a defect. It simply means the next stage must be clearly labelled.

The scientific sequence should be:

**Exploratory observation → formalised hypothesis → pre-specified predictions → unseen runs → adjudication.**

The original observation should remain part of the historical record as discovery evidence. It should not be retroactively treated as confirmatory evidence.

Once candidate behavioural signatures are defined, future runs can be sealed until the predictions and analysis plan are committed.

REE provides an unusually favourable environment for this because computational experiments can often be blinded cheaply. Runs could be anonymised so that a human or automated behavioural adjudicator does not know which condition produced each trajectory. The experiment designer might know the conditions while the scorer sees only Run A, Run B, Run C, Run D. Condition labels would be revealed only after scoring or classification is complete.

This should reduce expectancy effects and post-hoc narrative fitting.

## Visual observation should remain legitimate evidence

The answer is not to discard human observation. Human observers may detect structure before suitable metrics exist. Indeed, many behavioural sciences began through careful naturalistic observation before later formalisation.

The safeguard should instead be:

> **An observation may generate a hypothesis, but it does not confirm itself.**

When a visual pattern is noticed, the immediate scientific question becomes:

> **What else would have to be true if this pattern is real?**

Those additional consequences can then be tested.

Visualisation may therefore remain an important discovery instrument and potentially part of later blinded adjudication, especially when paired with quantitative analyses.

## Behavioural properties should be tested for invariance at the correct level

A particularly important extension concerns behavioural generalisation.

If a proposed strategy is genuine, its superficial appearance may change when the environment changes. The strongest evidence for a latent behavioural organisation may therefore be that a visible trajectory changes while a deeper functional relationship is preserved.

For example, “return rapidly to refuge after acquisition” should not imply reuse of the same geometric route when the environment is rearranged. A changed trajectory that preserves the functional organisation may provide stronger evidence for strategy than literal repetition of an old route.

The skill should therefore distinguish between invariance of surface behaviour, invariance of functional organisation, and invariance of mechanism. These are not the same thing.

Generalisation experiments should deliberately seek environments in which a true strategy must manifest differently.

## A tentative behavioural-adjudication workflow

A future skill might eventually formalise something like:

**Observe → Preserve → Compete → Predict → Perturb → Blind → Measure → Discover → Adjudicate → Replicate → Generalise.**

### Observe
Identify an interesting behavioural pattern.

### Preserve
Record the observation as closely as possible without embedding an explanation into its description.

### Compete
Generate credible alternative explanations, including trivial ones.

### Predict
Derive multiple behavioural consequences expected under each explanation.

### Perturb
Construct manipulations that make competing explanations diverge.

### Blind
Where practical, hide condition labels during behavioural scoring or interpretation.

### Measure
Use pre-specified hypothesis-directed metrics.

### Discover
Also inspect behavioural structure not captured by the predefined measurements.

### Adjudicate
Judge the pattern of evidence across measures and perturbations rather than allowing one metric to define the phenomenon.

### Replicate
Repeat across seeds, episodes, and relevant controls.

### Generalise
Test whether the inferred behavioural organisation survives environmental changes requiring a new surface expression.

This sequence is currently only a candidate structure and should itself be criticised.

## The skill should explicitly avoid behavioural Goodharting

A recurring danger is that once a useful behavioural indicator becomes measurable, experiments begin to optimise or interpret the indicator rather than the underlying phenomenon.

A behavioural metric should therefore generally remain an indicator, not an ontology.

The skill might include questions such as:

- What phenomenon is this metric intended to index?
- What alternative processes could change the metric?
- Could the metric improve while the behaviour of interest worsens?
- Could the behaviour of interest improve without changing this metric?
- What second and third measures would be expected to co-vary if the interpretation were correct?
- What perturbation would distinguish the intended interpretation from metric gaming?

This seems particularly important in REE because the experimental system itself may eventually adapt to repeatedly used metrics.

## Possible scientific domains to mine

This thought should trigger deeper investigation rather than immediately hardening into an implementation.

Relevant literatures may include, but should not be limited to:

- **Ethology and computational ethology:** ethograms, behavioural motifs, action sequencing, state transitions, hierarchical behaviour, unsupervised phenotyping.
- **Movement ecology:** path tortuosity, correlated random walks, Lévy-like search, home-range behaviour, first-passage analysis, resource selection, state-switching movement models.
- **Behavioural neuroscience:** learning, memory consolidation, replay, navigation, exploration/exploitation, latent behavioural states, behavioural variability.
- **Motor control:** movement chunking, trajectory smoothness, action primitives, corrective submovements, motor variability, skill consolidation.
- **Animal cognition and comparative psychology:** flexible strategy use, detour tasks, reversal learning, transfer, latent learning, cognitive maps, behavioural flexibility.
- **Reinforcement learning and artificial intelligence:** policy evaluation, exploration/exploitation, hierarchical reinforcement learning, options, successor representations, representation learning, generalisation, behavioural cloning, inverse reinforcement learning.
- **Dynamical systems:** attractors, metastability, switching dynamics, recurrence, phase-space analysis, state transitions, behavioural manifolds.
- **Causal inference and experimental design:** interventions, negative controls, mediation, counterfactual reasoning, discriminating experiments.
- **Open science and metascience:** preregistration, registered reports, blinded analysis, multiverse analysis, exploratory versus confirmatory inference.
- **Psychometrics and latent-variable modelling:** construct validity, convergent evidence, discriminant evidence, measurement invariance, multi-indicator constructs.
- **Ecology and evolutionary biology:** behavioural strategies, adaptive variability, niche-dependent behaviour, behavioural syndromes, functional equivalence across environments.
- **Robotics and embodied artificial intelligence:** navigation strategies, behavioural evaluation, sim-to-sim generalisation, embodiment-dependent policy structure, emergent behavioural repertoires.

There are likely other relevant traditions that should be discovered rather than assumed in advance.

## Literature mining should seek methods, not merely citations

Future literature review should not simply accumulate references supporting this thought.

It should actively search for:

- established methods that contradict parts of the proposed workflow;
- experimental designs more rigorous than those suggested here;
- known failure modes in behavioural classification;
- validated measures of sequence structure;
- techniques for discovering latent behavioural states;
- methods for comparing behavioural repertoires across different environments;
- approaches to separating stochastic exploration from behavioural disorganisation;
- procedures for blinded behavioural analysis;
- statistical methods for multi-metric adjudication;
- methods for testing behavioural generalisation;
- historical examples where apparently meaningful behaviour vanished under better controls;
- cases where coarse metrics missed an important phenotype;
- cases where human observers perceived structure that quantitative analysis failed to confirm;
- cases where quantitative discovery revealed structure human observers had missed.

The eventual REE skill should emerge from that comparative work rather than merely formalising the present intuition.

## Possible deeper principle

The scientific object of interest may increasingly cease to be individual actions.

It may instead be **organisation across actions, time, context, memory, and environmental change**.

If so, the appropriate unit of behavioural evidence will sometimes be neither the action nor the trajectory nor a scalar summary, but a pattern of relationships that persists across carefully chosen transformations.

That possibility deserves much more thought.

For now, the safest methodological stance may be:

> **Do not ask one ruler whether behaviour changed. Construct an umpire capable of deciding among explanations.**

This thought should remain open for revision, expansion, partial rejection, and replacement as broader scientific methods are examined.
