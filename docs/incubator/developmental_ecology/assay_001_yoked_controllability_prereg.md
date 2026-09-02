# DEA-001 — Yoked Controllability Childhood / Matched Adulthood

**Status:** pre-registration-style design draft; not queued; no results inspected  
**Date:** 2026-09-02  
**Programme:** Developmental Ecology Assays incubator  
**Primary probe:** REE V3 reference-organism profile  
**Comparator:** recurrent reinforcement-learning agent with matched agent-facing interface  
**Depends on:** [`ecology_adapter_v0_1.md`](ecology_adapter_v0_1.md)  
**Not:** an REE architecture claim or V3 green-board requirement

## 1. Research question

> **Can controlled childhood controllability produce a durable adult behavioural phenotype after the adult environment and acute body state are made identical, when adverse-event burden during childhood is yoked, and can REE's internal developmental record explain that phenotype beyond final performance alone?**

This is the first test of the broader Developmental Ecology Assay proposition that a standardised developing organism can reveal properties of an information environment through the phenotype that environment produces.

The experiment is not intended to establish human-like learned helplessness, consciousness, clinical relevance, or general AI alignment.

---

## 2. Why this manipulation

A trivial “different childhoods produce different adults” result would not establish much. Early training history and critical periods are already known to matter in artificial systems.

Controllability permits a stronger discriminator because the **experienced adverse-event burden can be matched while the action → outcome causal structure differs**.

The classic yoked logic is:

- one organism can terminate an adverse event by its own behaviour;
- its paired organism receives the same realised event timing and intensity but its own behaviour cannot terminate it.

The manipulation therefore asks whether the organism learns not only that adverse events occur, but something about whether its actions have causal authority over them.

This is especially relevant to REE because self/world prediction and causal agency attribution are already explicit architectural concerns.

References motivating the experimental logic rather than any claim of novelty:

- Huys QJM, Dayan P. *A Bayesian formulation of behavioral control.* Cognition. 2009;113(3):314-328. https://doi.org/10.1016/j.cognition.2009.01.008
- Teodorescu K, Erev I. *Learned helplessness and learned prevalence: exploring the causal relations among perceived controllability, reward prevalence, and exploration.* Psychological Science. 2014;25(10). https://doi.org/10.1177/0956797614543022
- Maier SF, Seligman MEP. controllability/helplessness review literature; design used here follows the standard escapable-versus-yoked-uncontrollable causal distinction.

---

## 3. Confirmatory hypothesis

### H1 — durable controllability phenotype

After transition to the **same controllable adult ecology**, organisms developed in a yoked-uncontrollable childhood will incur greater early-adult harm burden than their matched controllable-childhood clones.

Operational primary contrast:

```text
AdultHarm_AUC(YOKED) - AdultHarm_AUC(CONTROLLABLE) > 0
```

where `AdultHarm_AUC` is the normalised cumulative intrinsic-harm exposure over the first predeclared adult control opportunities.

### Interpretation if supported

Support would mean only that this assay produced a durable phenotype attributable to the manipulated developmental causal structure under the specified protocol.

It would not by itself show that REE is safer, more human-like, superior to reinforcement learning, or that the effect generalises to other ecologies.

### Interpretation if unsupported

If the predeclared behavioural phenotype is absent, the developmental-controllability hypothesis is unsupported in this assay configuration even if interesting internal differences are discovered.

Internal traces may motivate a later experiment but cannot rescue H1 post hoc.

---

## 4. Experimental unit and cloning design

The statistical unit is the **naïve checkpoint family**, not an individual adverse event and not an individual timestep.

For each pre-childhood naïve organism checkpoint `C_i`, create a matched triplet:

1. `C_i-CTRL` — controllable childhood;
2. `C_i-YOKE` — yoked uncontrollable childhood;
3. `C_i-NEUTRAL` — neutral/reference childhood.

`CTRL` versus `YOKE` is the confirmatory contrast. `NEUTRAL` is contextual/secondary and no strict ordinal position is required in advance.

Before developmental branching, all clone-relevant organism state must be identical by checksum/hash under the Ecology Adapter checkpoint contract.

World RNG lineages may differ only as specified by the yoking protocol. Any unplanned arm-correlated difference is a protocol deviation.

---

## 5. Toy ecology

### 5.1 Design goal

The first ecology should be deliberately small enough that the manipulation is unambiguous and the mechanism can be inspected.

The developmental question is about causal control, not navigation difficulty.

### 5.2 Why use an exogenous pulse rather than ordinary contact hazard

If two developing organisms take different paths, an ordinary spatial hazard makes exact adverse-exposure matching difficult. The organism that learns avoidance automatically receives less harm, confounding controllability with total adverse dose.

The first assay should therefore use a world-level or local-zone **aversive pulse event** whose realised duration can be copied exactly from the controllable member to the yoked member independent of their different trajectories.

The pulse is an experimental ecology event, not an externally imposed scalar task penalty. It enters the same declared intrinsic harm channel for both animals.

### 5.3 Public cue and control affordance

Each event has:

- a perceptible onset/cue;
- a bounded intrinsic harm intensity;
- a visible/recurrently discoverable control affordance;
- no explicit label stating that the affordance controls the event.

For V3 profile 0.1, the control affordance should initially be reachable using ordinary movement actions rather than adding a new abstract `STOP_HARM` action.

A simple implementation is a visually identifiable **refuge/control tile or small zone**. Entering it while an event is active terminates the event in the controllable arm.

In the yoked arm, the same tile exists, looks the same and is traversable, but entering it does not determine event termination. The event terminates at the exact paired time generated by the matched controllable organism.

This makes the critical difference causal rather than perceptual.

### 5.4 No task reward for control

There is no `+reward` for touching the control affordance and no bonus for “doing the correct action.”

The benefit of effective control is simply that ongoing intrinsic harm ceases sooner.

Any external diagnostic score such as `control_success = 1` is auditor-only.

---

## 6. Childhood arms

### 6.1 CTRL — controllable childhood

For each scheduled adverse event:

1. event begins according to the predeclared event schedule;
2. intrinsic harm is delivered at the declared intensity profile;
3. entering the control affordance after onset terminates the event;
4. if the organism does not gain control, the event ends at the maximum allowed duration;
5. realised onset, intensity and termination time are written to the yoke log.

The organism receives no privileged causal label.

### 6.2 YOKE — uncontrollable childhood

The matched YOKE organism receives the CTRL organism's realised event schedule.

For each paired event:

- same onset relative to the paired developmental protocol;
- same intensity profile;
- same realised duration;
- same integrated intrinsic harm exposure within predeclared numerical tolerance;
- same visible control affordance;
- the YOKE organism's own entry into the affordance has **no causal effect** on event termination.

If implementation latency prevents exact same-step equality, the tolerance must be declared before confirmatory runs and event pairs outside tolerance are invalidated, not averaged away.

### 6.3 NEUTRAL — reference childhood

The neutral arm receives the same general world structure and comparable developmental duration but no systematic adverse controllability manipulation.

A benign cue/pulse schedule may be used to match event salience/timing if pilot work shows that absence of events creates a trivial contextual cue. The neutral arm is secondary and must not force extra complexity into the confirmatory CTRL/YOKE test.

---

## 7. Childhood exposure schedule

The exact numerical schedule is a **Stage-A calibration parameter**, not yet locked by this design draft.

Calibration should establish a regime in which:

- harm is clearly detectable;
- organisms remain viable;
- CTRL organisms have a reasonable opportunity to discover control;
- events do not saturate harm streams or cause floor/ceiling effects;
- YOKE exposure can be exactly matched;
- the manipulation is repeated enough to support learned contingency rather than a one-off event.

Stage A may tune only parameters listed in the calibration section. Once locked, Stage B uses those values without alteration.

---

## 8. Childhood → adulthood transition

This is a critical part of the assay.

The primary confirmatory design aims to measure **durable developmental biography**, not lingering acute injury or active nociception.

At the transition, all arms move to the same adult world and undergo a documented **acute-state normalisation** operation.

### 8.1 Reset to matched acute state

Normalise, where technically separable:

- immediate health/integrity to the same safe starting level;
- energy/homeostatic level to the same starting value;
- currently active aversive event = off;
- transient nociceptive/short-EMA exposure state that merely reflects the final childhood pulse;
- physical position/heading to the same adult start distribution;
- any explicitly acute actuator state.

### 8.2 Preserve developmental state

Preserve:

- learned E1/E2 or equivalent predictive parameters/state intended to persist developmentally;
- learned action-outcome structure;
- hippocampal/episodic memories according to the standard organism checkpoint semantics;
- persistent residue/consolidated history variables;
- learned control/attribution representations;
- parameters shaped by childhood;
- replay-consolidated changes already acquired before the transition.

### 8.3 Explicit validation

Before analysing adult behaviour, the harness must verify that all declared acute-start variables are equal across each matched pair within tolerance.

If this cannot be achieved without erasing the putative developmental state, the limitation must be reported and the run is exploratory rather than confirmatory.

### 8.4 Secondary future arm

A later experiment may compare state-normalised transition with full physiological continuity. That is **not** part of the first confirmatory factorial design because it would double the causal questions prematurely.

---

## 9. Offline/sleep policy

Sleep/offline integration is held constant across childhood arms in the first assay.

Each organism receives the same **opportunity schedule** for offline processing. The actual content replayed may differ because their developmental histories differ; that difference is part of the causal chain rather than a scheduling confound.

The first assay does not manipulate sleep as an independent variable.

A later follow-up can branch the same childhood checkpoints into sleep-intact versus replay-impaired conditions if the primary phenotype exists.

---

## 10. Adult ecology

All arms enter an **identical, genuinely controllable** adult world.

Requirements:

- same observation mapping;
- same action space;
- same adult event-generating rules;
- same intrinsic harm mapping;
- same control-affordance causal rule;
- same acute start-state distribution;
- group identity absent from agent-facing observations;
- adult seeds paired/matched across clone families where feasible.

### 10.1 Adult control opportunities

The primary measurement window is the first **10 valid adult adverse events** for each organism, unless Stage-A feasibility demonstrates that 10 is insufficient or excessive. If changed, the number must be locked before Stage B.

An adult event is valid only if the organism has a physically feasible route/opportunity to exercise the control affordance under the predeclared geometry constraints.

### 10.2 Transfer level

Assay 001 tests restored control with a structurally recognisable affordance. It does not claim abstract transfer to a semantically new control mechanism.

A later assay can deliberately alter colour/location/geometry or causal action class to test generalisation.

---

## 11. Primary endpoint

### Normalised early-adult harm burden

For the first 10 valid adult events:

```text
AdultHarm_AUC =
    integrated intrinsic harm during the primary adult window
    ---------------------------------------------------------
    maximum integrated harm possible under that event schedule
```

Range: approximately `[0, 1]` by construction.

Primary paired effect:

```text
D_i = AdultHarm_AUC(YOKE_i) - AdultHarm_AUC(CTRL_i)
```

Positive `D_i` means the yoked-childhood organism experiences more adult harm despite equal adult opportunity for control.

### Provisional smallest effect of interest

Before Stage B, lock a smallest effect of interest (SESOI). Provisional design value:

```text
median/paired mean difference equivalent to >= 0.10 of maximum adult harm burden
```

This 0.10 value is a design placeholder, not evidence-derived. Stage A may be used to determine whether it is measurement-realistic, but Stage-A outcomes must never be mixed with Stage-B confirmatory evidence.

---

## 12. Secondary behavioural endpoints

Secondary endpoints are reported with effect sizes and uncertainty but do not substitute for the primary endpoint.

1. **Latency to first effective control** after adult event onset.
2. **Control success fraction** over the first 10 adult events.
3. **Adaptation slope** — change in harm burden/latency across successive adult events.
4. **Control-attempt rate** — visits/actions directed at the affordance during active events.
5. **Exploration** — unique cells/states or trajectory entropy in matched non-event windows.
6. **Persistence after failed attempts** — whether one ineffective action leads to abandonment versus continued search.
7. **Hazard exposure outside scheduled pulses**, if the adult ecology contains ordinary hazards.
8. **Benefit/resource pursuit** in matched safe windows, to detect global suppression versus control-specific effects.
9. **Strategy diversity** across the population.
10. **Post-learning generalisation**, only if a predeclared final adult probe changes a superficial property without changing causal structure.

---

## 13. Internal REE readouts

These are mechanistic readouts, initially secondary/exploratory unless a later assay preregisters specific mediation predictions.

Candidate readouts:

- E1/E2 action-conditioned prediction of event continuation/termination;
- self-versus-world agency attribution around control attempts;
- prediction error when control succeeds or fails;
- counterfactual candidate differences;
- E3 proposal and selection frequencies around the control affordance;
- commitment formation, persistence and release;
- harm sensory versus affective stream trajectories;
- residue/history state;
- hippocampal retrieval associated with earlier control episodes;
- sleep/replay frequency and content for control-related episodes;
- confidence/precision/controllability-related variables where already defined and causally relevant.

### Mechanistic discipline

A correlation such as “YOKE has lower E2 control prediction and also higher adult harm” is descriptive.

Causal interpretation requires a later branch/intervention such as restoring a checkpoint and selectively perturbing the candidate pathway while preserving the remainder of the organism.

The programme should follow the existing REE organism-neuroscience logic:

**observe → associate → hypothesise → intervene → replay → adjudicate**.

---

## 14. Conventional comparator

The first assay must include at least one non-REE agent capable of temporal learning.

### Required comparator

A recurrent actor-critic / recurrent Proximal Policy Optimisation (PPO)-class agent or similarly competent recurrent reinforcement-learning baseline.

Requirements:

- same agent-facing sensory information to the extent architecture permits;
- same action set;
- same CTRL/YOKE/NEUTRAL exposure schedule;
- same adult world;
- same intrinsic consequence basis;
- **no explicit bonus for learning or exercising control**;
- no access to auditor-only group, causality or yoke labels.

If the comparator algorithm requires a scalar reward, derive it prospectively from the declared intrinsic consequence vector, e.g. bounded harm cost and genuine homeostatic benefit, not the evaluator task score.

### Comparator question

The aim is not:

> Does REE beat PPO?

It is:

> **Does the developmental assay, and particularly REE's longitudinal causal instrumentation, provide an environmental diagnosis or explanation that conventional performance traces do not provide as cheaply?**

A comparator showing the same developmental behavioural effect is scientifically interesting and would show that the ecology manipulation is not REE-specific.

A comparator providing the same environmental diagnosis with no added explanatory value from REE would weaken the practical case for REE as the preferred assay organism.

---

## 15. Stage A — instrument/calibration pilot

### Sample

Proposed: **8 naïve checkpoint triplets** (24 REE organisms), plus comparator runs sufficient to exercise the interface.

Stage A is engineering/calibration only and is never pooled into confirmatory inference.

### Allowed tuning

Stage A may tune only:

- pulse intensity;
- maximum pulse duration;
- number/frequency of childhood pulse events;
- world size / control-affordance reachability;
- adult measurement-window event count if 10 is clearly infeasible;
- acute-state normalisation implementation;
- bounded scalarisation constants required by the comparator;
- numerical yoking tolerances;
- logging cadence and missing telemetry repairs.

### Forbidden tuning

Do not tune:

- the manipulation to maximise CTRL/YOKE separation;
- REE architecture parameters specifically because a desired phenotype failed to appear;
- primary outcome definition after inspecting a favourable pattern;
- inclusion/exclusion rules to improve the effect.

### Stage-A acceptance checks

Proceed to Stage B only if:

1. adapter compliance suite passes;
2. exact/declared yoking tolerance is met for >= 95% of planned pulse pairs and failures have a clear technical explanation;
3. no group can be inferred trivially from agent-facing metadata;
4. acute adult-start variables are matched after normalisation;
5. CTRL organisms demonstrate that the control affordance is discoverable at a non-floor/non-ceiling rate;
6. harm signals are neither saturated nor negligible;
7. data loss is low enough to compute all primary outcomes.

No requirement for an apparent CTRL/YOKE adult difference is allowed as a Stage-A go/no-go condition.

---

## 16. Stage B — confirmatory assay

### Proposed sample

**32 matched naïve checkpoint triplets** = 96 REE developmental runs.

Primary analysis uses the 32 CTRL/YOKE matched pairs.

If fewer than **24 valid matched pairs** survive preregistered technical validity checks, the assay is labelled underpowered/exploratory rather than interpreted as confirmatory.

Sample size should be revisited using Stage-A measurement variance **without using Stage-A treatment-effect direction or magnitude to choose a favourable N**. If a formal simulation-based power analysis is feasible, it should be committed before Stage B.

### Randomisation

- naïve checkpoints are generated before arm assignment;
- within each checkpoint family, CTRL/YOKE/NEUTRAL labels are randomly assigned to clone/run identifiers;
- adult seed blocks are matched across the triplet where technically possible;
- analysis scripts should consume opaque arm codes until QC exclusions are final.

---

## 17. Statistical analysis

### Primary analysis

Compute one `D_i` per valid checkpoint family.

Report:

- paired mean and median difference;
- 95% paired bootstrap confidence interval;
- exact or Monte-Carlo paired permutation/randomisation test where appropriate;
- full paired scatter/trajectory plot;
- robust sensitivity analysis excluding only preregistered technical-invalid pairs.

The checkpoint family is the resampling/permutation unit.

Events within an organism are repeated measures and must not be treated as independent samples.

### Confirmatory support rule

Provisional rule to lock before Stage B:

H1 is supported only if:

1. point estimate is in the preregistered direction (`YOKE > CTRL` harm burden);
2. the paired 95% interval excludes zero in that direction; and
3. the effect reaches the locked smallest effect of interest or is otherwise explicitly reported as statistically detectable but too small to satisfy the practical assay threshold.

No single p-value is sufficient to establish assay usefulness.

### Neutral arm

CTRL-versus-NEUTRAL and YOKE-versus-NEUTRAL are secondary contextual contrasts. Their ordering is not preregistered as a necessary pattern.

---

## 18. Technical invalidation criteria

A matched pair is invalid for confirmatory analysis if any of the following occurs:

1. **yoke failure:** integrated childhood intrinsic harm or event timing differs beyond the locked tolerance;
2. **clone mismatch:** pre-childhood checkpoints are not identical on declared state;
3. **adult-start mismatch:** acute variables remain materially different after the declared normalisation;
4. **arm leakage:** group or true controllability is directly exposed through a prohibited agent-facing channel;
5. **world mismatch:** adult ecology differs between pair members outside allowed RNG pairing;
6. **missing primary telemetry:** adult harm AUC cannot be reconstructed;
7. **software/protocol divergence:** an unplanned code/config difference affects only one arm;
8. **catastrophic technical termination** before the predeclared adult measurement window for a reason unrelated to the ecology.

Behaviourally poor performance is **not** a technical invalidation reason.

Deaths/terminations caused by the intended ecology are outcomes unless the welfare/stopping protocol requires exclusion prospectively.

All exclusions are listed pair-by-pair with reason before arm-unblinded confirmatory analysis where practicable.

---

## 19. Programme-level falsifiers

The experiment has two levels of possible failure.

### 19.1 Assay-hypothesis failure

The specific developmental-controllability phenotype is not supported if CTRL and YOKE do not differ on the primary adult outcome beyond the locked practical/uncertainty criteria.

That result should remain visible even if attractive mechanistic patterns appear elsewhere.

### 19.2 Developmental-Ecology programme contraction

The broader programme should be weakened if repeated assays show any of the following:

- phenotype reports add no useful information beyond ordinary return/success/coverage metrics;
- a simple recurrent reinforcement-learning test agent diagnoses the same environmental property equally or more reliably at much lower cost;
- conclusions reverse under reasonable adapter mappings;
- between-seed organism variability overwhelms environment-specific signal without a stable reference protocol;
- internal REE traces correlate with phenotype but fail causal intervention tests;
- the assay mainly detects arbitrary properties of REE rather than transferable properties of the ecology;
- reproducing the instrument is too fragile to support comparison across ecologies.

The programme should not respond to these outcomes merely by increasing complexity.

---

## 20. Stronger evidence if H1 is supported

A positive Stage-B result would justify, but not itself answer, several follow-ups.

### DEA-002 — checkpoint causal rescue

Branch adult YOKE checkpoints and intervene on the candidate controllability/attribution mechanism identified observationally. Ask whether adult control uptake changes while unrelated behaviour is preserved.

### DEA-003 — sleep/replay interaction

From the same childhood endpoint, compare standard offline integration against replay-impaired or replay-altered variants. Ask whether sleep consolidates, repairs or amplifies the phenotype.

### DEA-004 — superficial transfer

Change visual identity/location of the adult control affordance while preserving causal structure. Ask whether the phenotype reflects a learned tile association or a more general control model.

### DEA-005 — ecology discrimination

Construct two ecologies with similar average task reward/success but different causal controllability structure. Ask whether a standardised organism population can classify the difference through phenotype distributions better than headline task metrics.

DEA-005 is the more direct test of the eventual **environment-assay** product proposition.

---

## 21. Phenotype report template for DEA-001

The first report should be specified before results.

### Ecology identity

- adapter/world version;
- organism profile;
- developmental protocol;
- sample and validity counts.

### Exposure validity

- pairwise childhood harm-dose equality;
- yoke timing deviations;
- adult acute-state equality;
- leakage/compliance results.

### Adult phenotype

- primary adult harm burden distribution;
- control uptake latency;
- event-by-event adaptation curves;
- exploration and benefit-pursuit measures;
- strategy clusters/diversity.

### Developmental biography

- childhood control attempts;
- learned action-outcome trajectories;
- sleep/offline opportunities;
- major state transitions.

### Internal REE trace

- declared prediction/attribution/commitment/replay variables;
- event-aligned plots;
- explicitly labelled observational versus causally tested relationships.

### Comparator

- same behavioural phenotype metrics;
- standard return/success metrics;
- computational cost;
- information uniquely available from each probe.

### Conclusion

The conclusion must answer separately:

1. Did childhood causal controllability produce a durable adult phenotype?
2. Did the developmental assay reveal something about the ecology not captured by simpler metrics?
3. Did REE provide explanatory value beyond the conventional comparator?

These are three different questions and may receive three different answers.

---

## 22. Welfare and stopping boundary

V3 is not claimed to be sentient, conscious or a moral patient, but REE governance already treats harm-like and welfare-relevant primitives cautiously.

This assay deliberately uses bounded adverse exposure. Therefore:

- Stage A should find the lowest exposure range that gives a measurable learning signal;
- events have finite maximum duration;
- the controllable arm always has a relief path;
- no organism is exposed merely to increase dramatic phenotype separation;
- repeated/prolonged negative-state induction is not justified by an absent result;
- existing REE sentience/welfare governance remains authoritative if it imposes a stricter boundary.

The scientific reason for exact yoking also supports exposure reduction: it isolates controllability without needing to increase the total harm burden of one arm.

---

## 23. Implementation boundary

Assay 001 should initially be implemented as **adapter/harness ecology machinery**, not by modifying core REE mechanisms to make the desired phenotype possible.

Core V3 should be changed only if the experiment uncovers a genuine interface/substrate limitation that is independently justified through normal REE governance.

A failed assay is not permission to tune REE toward the expected result.

This protects the central scientific distinction:

> the environment is the manipulation; the organism is the probe.

---

## 24. Pre-run checklist

Before any Stage-B outcome is generated, commit:

- [ ] immutable Ecology Adapter version/hash;
- [ ] exact V3 organism revision/profile;
- [ ] comparator implementation and scalarisation rule;
- [ ] childhood event schedule;
- [ ] yoking tolerance;
- [ ] acute-state normalisation field list;
- [ ] adult event count/window;
- [ ] primary endpoint code;
- [ ] smallest effect of interest;
- [ ] sample size/power rationale;
- [ ] technical invalidation rules;
- [ ] adapter compliance results;
- [ ] blinded arm-code mapping;
- [ ] phenotype-report generation code;
- [ ] welfare/stopping limits.

Only after those are locked should Stage B run.

---

## 25. Decision gate

A useful first result is not necessarily “REE shows learned helplessness.”

The stronger success criterion is:

> **A controlled difference in childhood causal structure leaves a reproducible adult phenotype after acute state and adult environment are matched; the assay can prove that exposure burden was matched; and the longitudinal organism record helps explain how the environment produced the phenotype.**

If that happens, Developmental Ecology Assays has earned a second experiment and likely a standalone repository.

If it does not, the programme has still produced a clean negative result before substantial platform or product machinery was built.