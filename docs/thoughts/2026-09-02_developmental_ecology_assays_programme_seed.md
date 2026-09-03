Status: processed
Intake: docs/incubator/developmental_ecology/README.md
Processing note (2026-09-03): processed directly into the Developmental Ecology incubator (README + ecology_adapter_v0_1.md + assay_001_yoked_controllability_prereg.md, REE_assembly 74312b8b7d/5295c87ed1/51072112ab, 2026-09-02) rather than a claims intake -- an adjacent programme, not an REE architecture claim, per the document's own status line. No claims registered.

Programme Seed: Developmental Ecology Assays — Measuring Environments by the Organisms They Produce

Original status line: incubator seed — do not ingest as an REE architecture claim

Date: 2026-09-02
Source: voice discussion on practical applications of retained REE versions
Purpose: Record a research programme that sits conceptually beside REE. REE supplies candidate developing organisms; this programme asks what standardised developing organisms can reveal about designed environments.

---

## Programme boundary

This document is not a proposal to change the REE architecture.

It records a separate scientific/application programme discovered while considering useful niches for completed lower-version REE organisms. The programme may initially use REE V3 as its best-understood probe organism, but its concepts should be defined so that other developmental architectures could eventually be compared.

Commercial/domain-specific implementations are intentionally not specified here. The scientific interface and assay concepts can remain open even if later domain adapters, validation services or applied products are developed separately.

---

## Core inversion

Most agent evaluation asks:

> How well does this agent perform in this environment?

A developmental ecology assay asks:

> **What kinds of agents does this environment produce?**

The environment therefore becomes the object being measured, while a standardised population of developing agents becomes part of the measuring instrument.

The primary deliverable is not a leaderboard score. It is an **ecological phenotype report** describing the behavioural and internal-state distributions that emerge after development in a specified world.

---

## Why this may matter

Designed worlds contain more than explicit task objectives.

They may implicitly teach that:

* actions are effective or ineffective;
* exploration is profitable or dangerous;
* harms are predictable or arbitrary;
* benefits are stable or transient;
* shortcuts dominate long-horizon strategies;
* uncertainty should trigger curiosity or withdrawal;
* persistence pays or becomes trapping;
* adverse outcomes are controllable or inescapable;
* apparent success generalises or collapses after environmental change.

These properties are often difficult to characterise by inspecting a reward function or specification alone.

A developing organism integrates repeated interaction over time. Its resulting phenotype may therefore expose structural properties of the world that are not obvious from static analysis.

---

## Assay, not benchmark

A benchmark ranks agents against a task.

An assay holds the probe organism and protocol sufficiently stable that differences in the response can reveal differences in what was presented to it.

The analogy is closer to biological or toxicological bioassays than to an agent leaderboard:

* standardised probe;
* defined exposure;
* controlled developmental period;
* matched reference condition;
* multiple readouts;
* population distributions rather than one success score;
* mechanism-oriented follow-up after an abnormal phenotype appears.

The goal is not to anthropomorphise the artificial organism. It is to use developmental response as an instrument for measuring an information world.

---

## Intrinsic values are not task goals

A key conceptual distinction from the voice discussion is:

> **What is intrinsically beneficial or harmful to an organism need not be the same thing as the goal it eventually pursues.**

A developmental agent may begin with bounded intrinsic sensitivities such as:

* integrity/harm;
* resources or homeostatic viability;
* prediction and surprise;
* controllability;
* curiosity or information gain;
* persistence/completion signals.

A particular environment can then support the emergence of provisional goals, strategies and habits that manage those values.

This differs from simply declaring a task reward such as `+10 for reaching the target` and treating the reward function as the goal itself.

The distinction is not unique to REE: developmental robotics, intrinsic-motivation research and autotelic reinforcement learning already investigate innate/acquired value and self-generated goals. The opportunity here is to combine that distinction with controlled developmental histories and use the resulting organism as an environmental assay.

---

## The Ecology Adapter

A practical programme needs a stable boundary between an external simulation and the developing organism.

Provisional interface:

`external world → ecology adapter → organism`  
`organism actions → ecology adapter → external world`

The adapter should map a domain onto organism-relevant channels without leaking privileged task solutions.

### Observation contract

Specify what the organism can sense, including:

* local/world observations;
* temporal change;
* proprioceptive/self state where relevant;
* resource/homeostatic state;
* harm/integrity state;
* action consequences;
* uncertainty-relevant sensory structure.

### Action contract

Specify:

* available actions;
* action timing/duration;
* action costs;
* failed/blocked action semantics;
* whether actions alter the organism, environment, or both.

### Consequence contract

Keep separate:

1. **observable outcomes** — what happened in the world;
2. **intrinsic consequence channels** — what changed in organism-relevant harm, benefit or viability variables;
3. **evaluation labels** — metrics used by investigators after the fact.

The adapter should not silently convert investigator knowledge into an oracle available to the organism.

### Development contract

Define:

* developmental duration;
* episode/reset semantics;
* waking versus offline/sleep opportunities;
* checkpoint schedule;
* randomisation policy;
* population size;
* stopping/welfare rules where relevant.

The adapter itself should be versioned and auditable because it is part of the scientific instrument.

---

## Candidate assay outputs

A useful ecology report could include:

### Behaviour

* explored state-space fraction;
* strategy families;
* route/trajectory diversity;
* persistence and abandonment;
* risk/hazard exposure;
* recovery after setbacks;
* generalisation after environmental change;
* brittle versus resilient success.

### Development

* timing of stable strategy formation;
* sensitivity to early exposures;
* between-organism divergence;
* convergence across different developmental histories;
* critical/sensitive periods;
* effect of replay or sleep on persistence and adaptation.

### Agency and causality

* learned controllability;
* action-outcome attribution;
* response to restored control after uncontrollable exposure;
* counterfactual sensitivity;
* distinguishability of own-action versus external-event consequences.

### Internal mechanism, where the probe allows it

* E1/E2 predictive-state changes;
* commitment formation/release;
* hippocampal/replay statistics;
* affective/harm pathway state;
* attractor/confidence changes;
* counterfactual candidates considered but not selected.

A major possible advantage of REE as a probe is not simply behaviour but unusually rich causal instrumentation across development.

---

## Reference organisms and population organisms

The programme should distinguish two experimental modes.

### Reference-organism mode

Use tightly specified architecture, seed, childhood and checkpoints to ask:

> What changed when one property of the ecology changed?

This maximises reproducibility and causal isolation.

### Population mode

Run many independently developing organisms to ask:

> What distribution of phenotypes can this ecology produce?

This measures:

* variance;
* behavioural attractor frequencies;
* developmental bifurcations;
* stable temperament-like differences;
* rare pathological trajectories;
* multiple viable strategies.

The two modes answer different scientific questions and should not be collapsed into one score.

---

## First concrete scientific demonstration

The clearest initial demonstration should be understandable without knowing the full REE architecture:

> **Same adult world, different childhoods.**

Two or more cohorts receive systematically different early environments. They are then moved into an identical adult environment. The question is whether their adult behaviour remains detectably different and whether those differences can be causally traced to the developmental exposure.

A stronger version should avoid the trivial result that more early reward simply produces more approach behaviour.

One candidate manipulation is **controllability with matched outcome burden**:

* **Controllable childhood:** harmful events are predictable and can be reduced/avoided by appropriate action.
* **Uncontrollable/yoked childhood:** an organism receives a matched distribution of harmful events, but its actions do not control them.
* **Adult phase:** all cohorts enter the same environment in which hazards are genuinely controllable.

Questions:

* Does early controllability change later exploration?
* Does the organism exploit restored control?
* Does it attribute adult outcomes differently?
* Does commitment become overly cautious or appropriately adaptive?
* Does replay preserve, worsen or repair the developmental effect?
* Are internal mechanisms different even when adult task performance converges?

This experiment has close neighbours in learned-helplessness and reinforcement-learning research, so novelty would not lie in the concept of controllability itself. The contribution would be the developmental-assay framing, mechanistic accessibility, and use of a standardised artificial organism to characterise what a world teaches.

---

## First toy application

A deliberately modest application could be a simulated game or designed micro-world.

Question to a designer:

> Does this world reliably teach the affordance/strategy you intended, or does it produce avoidance, shortcut capture, unexplored regions or brittle strategies instead?

A small cohort of standardised developing organisms is exposed to alternative versions of the world. The report compares the distributions of developmental outcomes.

Existing automated game-playtesting systems already use reinforcement-learning agents for coverage, exploits and difficulty. The developmental ecology assay should therefore not claim novelty merely from using agents to test games. Its distinct question is whether **developmental phenotype** provides useful information beyond coverage, score and task success.

That is an empirical discriminator for the programme.

---

## Relationship to environment design and curriculum learning

Unsupervised Environment Design and curriculum-learning research typically modifies environments to train more robust or generally capable agents.

Developmental ecology assays invert the optimisation target:

* environment-design work: **change the world to improve the agent**;
* developmental ecology assay: **hold the probe protocol stable to measure what the world does to the agent**.

The methods can still cross-fertilise. Environment-generation tools may create controlled assay conditions; assay results may later inform curriculum design. But the scientific object is different.

---

## Relationship to REE versions

REE V3 is a plausible first probe because it is intended to expose self/world prediction, harm, agency, commitment, residue and offline integration in a bounded organism.

Later REE versions could produce a family of assays at different cognitive levels:

* V3 assay — causal/solitary ecology;
* V4 assay — long-horizon individual ecology;
* V5 assay — social ecology;
* later language-capable assay — communicative/cultural ecology.

Higher-level assays should be used only when the property under investigation requires the added ontology. Otherwise lower preparations retain greater causal clarity and potentially lower welfare ambiguity.

---

## Scientific discriminators

The programme becomes worthwhile only if developmental assays provide information that simpler approaches do not.

Early discriminators should include:

1. Can the assay distinguish environments with identical headline reward/task structure but different causal organisation?
2. Does developmental history explain adult behaviour after the adult environment is matched?
3. Do population phenotypes reveal rare or stable failure modes missed by mean reward/success metrics?
4. Can internal developmental traces explain why two apparently similar adult policies differ in brittleness or generalisation?
5. Do assay conclusions transfer across probe architectures, or are they merely peculiarities of REE?
6. Does the added developmental machinery justify its computational cost over conventional reinforcement-learning test agents?

A negative answer to these questions should shrink or terminate the programme rather than being explained away.

---

## Provisional programme architecture

If the idea survives initial experiments, a standalone repository could eventually contain:

```text
developmental-ecology/
  README.md
  docs/
    programme.md
    theory/
    literature/
    assays/
    governance/
  ecology_adapter/
  reference_ecologies/
  organism_interfaces/
  experiments/
  reports/
```

`organism_interfaces/` should point to REE and other probes rather than copying their implementations.

This seed remains in REE_assembly only to preserve provenance until the programme has earned a separate home.

---

## Immediate research programme

1. Complete a focused novelty review across developmental robotics, critical learning periods, artificial life, environment design, automated playtesting, AI-safety model organisms and biological bioassays.
2. Formalise the Ecology Adapter contract.
3. Pre-register a matched-adulthood / different-childhood experiment.
4. Include conventional reinforcement-learning comparators.
5. Define an ecology phenotype report before seeing results.
6. Determine whether V3 currently exposes the necessary intrinsic consequence and causal-attribution channels without adding programme-specific machinery to REE.
7. Only after a useful discriminator is demonstrated, decide whether to create the standalone repository and applied/product layer.

---

## Reflection

The potentially distinctive idea is not merely a new kind of agent.

It is a new use for a developing agent:

> **the organism becomes an instrument for measuring the causal-developmental properties of an information world.**

If that inversion proves useful, the same research programme can remain scientifically meaningful even as the specific probe organisms evolve.