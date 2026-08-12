# GOV-BEHADJ-1 Behavioural-Adjudication Methodology -- Synthesis

> Created: 2026-08-12
> Scope: 9 entries across computational ethology, movement ecology, behavioral
> neuroscience, metascience/open science, reinforcement learning, and
> psychometrics, targeting the source thought's own instruction (docs/thoughts/
> 2026-08-11_behavioural_adjudication_scientific_skill_working_thought.md,
> "Literature mining should seek methods, not merely citations") to search
> actively for CONTRADICTING methods, known failure modes, and historical cases
> where apparently meaningful behaviour did not survive better controls -- not
> merely to accumulate supporting citations.
> This pull is chipped follow-on from the 2026-08-12 thought-intake session that
> registered GOV-BEHADJ-1 (status `candidate`, explicitly provisional). It does
> NOT change GOV-BEHADJ-1's status or epistemic_category -- that is governance's
> call, per this claim's own `what_would_answer` field and GOV-HELDOUT-1's
> discipline (do not treat literature support, or even eventual skill drafting,
> as evidence the methodology "works"; only real use on a real claim can answer
> that).

## Headline verdict

The core reframing -- "we never needed a ruler, we needed an umpire" -- is
methodologically sound and has real precedent across every field it names.
But the literature does NOT simply validate the source thought's specific
11-step workflow as written. It surfaces three substantive complications that
should be preserved for eventual skill drafting, not smoothed over:

1. **Rigor exists, and it is more formal than the thought's own language.**
   Where the source thought describes states/transitions/discovery informally,
   established literatures (movement-ecology HMMs, MoSeq-style generative
   segmentation, survival/hazard models for sequence structure) already have
   mature, validated machinery for exactly these questions. A REE skill built
   from GOV-BEHADJ-1 should point to this machinery rather than reinvent
   informal versions of it.
2. **Blinding, replication, and perturbation are each individually necessary
   but NONE of them is sufficient on its own** -- and the literature documents
   concrete cases where each safeguard, applied carefully, still let a false
   effect through. This is the most important corrective to the thought's own
   framing, which risks reading as "do all eleven steps and you're safe."
3. **The risk the thought is most worried about (Goodharting a hand-picked
   metric) reappears, in a different form, inside every one of the more
   rigorous alternatives too** -- state-count selection in HMMs, model-order
   selection in unsupervised discovery, and the combinatorial choice space of
   multiverse analysis are all NEW places researcher degrees of freedom can
   hide, not places where they disappear.

## Findings organized by workflow step

### Observe / Preserve -- the risk of contamination before formal blinding

**Lit et al. (2011)** is the strongest complicating finding in this pull. It is
a rigorous, modern, peer-reviewed replication of the Clever Hans effect in a
working-animal paradigm: detection-dog handlers falsely told a scent target
was present at certain locations produced 225 false alert reports across 164
trials with NO target scent present anywhere, and human belief outweighed the
dog's own independently-manipulated cues in predicting where alerts occurred.
The complication for GOV-BEHADJ-1 is structural: the contamination in this
paper entered during the human's REAL-TIME interpretation of the animal's
behavior, not during a later, separate scoring step -- which means the source
thought's "Blind" step (hide condition labels during scoring) protects against
a narrower slice of the risk than it may appear to. The REE-relevant analogue
is not Fishtank trajectory generation (no human is present during a run) but
the researcher's own FIRST VISUAL IMPRESSION of a trajectory, which is exactly
where "post-sleep behaviour looked smoother" originated. **This directly
supports the source thought's own line -- "an observation may generate a
hypothesis, but it does not confirm itself" -- while showing that line needs
teeth: the observation that seeded the hypothesis should be logged verbatim,
before any belief-driven re-reading, and the formal blinded re-analysis should
be treated as the actual evidence, not a confirmatory formality.**

### Measure / Discover -- established machinery exists, and it relocates the Goodharting risk rather than solving it

**McClintock et al. (2020)**, the field-standard review of hidden Markov
models in movement ecology, and **Wiltschko et al. (2015)**, the founding
MoSeq paper for unsupervised behavioral-syllable discovery, both confirm that
rigorous, validated alternatives to the source thought's informal
state/transition language already exist -- and both are explicit, in their
own words, that these methods carry a version of the SAME risk the thought
raises for hand-picked metrics. McClintock et al.: choosing the number of
hidden states has "no foolproof or automatic way," and a fully free-
parameterized model's "states" can be "fully data driven" with no
correspondence to real behavioral categories. Wiltschko et al.'s own method
requires an analogous model-order hyperparameter with no single correct value.
**This is the pull's clearest instance of "established methods that
contradict parts of the proposed workflow": the thought implies that moving
from a hand-picked scalar metric to formal discovery-oriented analysis is a
safeguard against Goodharting. The literature says the safeguard is real but
incomplete -- the same failure mode recurs one level up, at the level of model
selection, and any REE skill needs its own explicit checklist item for THAT,
not just for metric choice.** Gygax et al. (2022) adds a related caution at
the sequence-structure level specifically: naive Markov-chain transition
counting -- the natural first-pass implementation of the thought's own
refuge/explore/food-seeking transition language -- assumes memorylessness,
an assumption the tutorial's own framing treats as frequently unrealistic for
real behavioral sequences; survival/hazard models are proposed as a more
flexible, validated alternative (entry not independently verified past
abstract-level; see its own confidence_rationale).

### Perturb / Generalise -- a worked positive template, and a direct caution about the motivating observation

**Belkaid et al. (2020)** is the pull's strongest positive supporting entry
and a genuine worked template: mice in a fully deterministic task actively
generated increasing choice variability rather than converging on the
theoretically optimal fixed sequence, and a discriminating switch-test
perturbation (introduce probabilistic rewards, check whether behavior changes)
cleanly distinguished "learned a specific sequence" from "learned a randomness
strategy." This is close to a real-organism demonstration of the source
thought's own "variability must not automatically be classified as noise"
section, done with exactly the kind of discriminating-perturbation design the
thought's own "Perturb" step calls for.

**Cobbe et al. (2019)**, by contrast, is this pull's most direct caution
about the SPECIFIC Fishtank observations that motivated GOV-BEHADJ-1. It is
also the highest-fidelity mapping in the whole pull, since both source and
target are deep RL agents. The paper shows that RL agents evaluated only
within their training distribution can appear highly competent while badly
failing to generalize to held-out, procedurally varied environments -- and
that standard within-distribution evaluation cannot distinguish a genuinely
general policy from memorization of training-distribution specifics. The
source thought's own motivating observations (coherent reef use, post-sleep
trajectories "looking smoother") were, by its own description, noticed within
a limited set of runs, not systematically checked against procedurally varied
held-out environments. **Until that check is run, this literature says the
observations that motivated GOV-BEHADJ-1 in the first place cannot yet be
distinguished from training-distribution memorization -- which is precisely
the class of risk the thought's own "Generalise" step exists to catch, now
with a concrete, quantitative RL precedent for how large such gaps can be and
how invisible they are without a dedicated test.**

### Adjudicate -- a formal statistical answer to a currently-qualitative step

**Steegen et al. (2016)**'s multiverse analysis and, with lower confidence,
**Flake & Fried (2020)**'s construct-validity/measurement-transparency
framework both give the source thought's "Adjudicate" step -- currently stated
only as "judge the pattern of evidence across measures and perturbations" --
concrete, established, citable statistical procedures rather than a purely
qualitative aspiration. Multiverse analysis in particular is a close, formal
match for the thought's own anti-Goodharting question ("could the metric
improve while the behaviour of interest worsens?"): rerun the same hypothesis
test across the full reasonable space of metric-definition choices (window
sizes, thresholds) and report whether the conclusion is robust to that choice
or an artifact of one arbitrary parameterization.

### Replicate -- a historical case exactly matching the thought's own request

**Crabbe, Wahlsten & Dudek (1999)** is the pull's most direct answer to the
source thought's explicit request for "historical examples where apparently
meaningful behaviour vanished under better controls." Three laboratories,
testing the same mouse strains with apparatus, protocol, and environment
rigorously standardized, still found systematic lab-by-strain interactions --
a real genotype effect that was nonetheless partly idiosyncratic to
unmeasured context, despite the experimenters' best efforts to eliminate
exactly that source of variation. **This is a direct caution against reading
GOV-BEHADJ-1's proposed workflow as a guarantee: standardized, rigorous,
multi-condition protocols reduce but do not eliminate the risk that an
observed effect is idiosyncratic to unmeasured context.** The REE-specific
translation is closer to home than a 1999 mouse-genetics paper might suggest:
REE Assembly already has its own confirmed instance of structurally the same
failure mode -- `torch.multinomial` returning different sampled actions from
bit-identical probability tensors across machine classes (memory
`reference-cross-machine-class-contract-divergence`). Any REE behavioural-
adjudication skill built from GOV-BEHADJ-1 should treat machine class and
substrate version as candidate confounds worth deliberately varying in its
"Replicate" step, not just seeds and environment layouts.

## What this pull does NOT establish

- No paper here directly evaluates GOV-BEHADJ-1's SPECIFIC 11-step workflow
  as a unit -- every entry speaks to one or more individual steps or to the
  general methodological posture, not to the sequence as an integrated whole.
  No literature currently exists (nor could it, since the workflow is novel
  to this thought) that validates the full pipeline.
- No paper directly tests any of the specific Fishtank observations (reef-use
  coherence, post-sleep smoothness) against a real held-out generalization
  test -- Cobbe et al. establishes the RISK and the RL precedent for how to
  test it, not a REE-specific result.
- The Gygax et al. and Flake & Fried entries could not be verified past
  abstract-level and secondary-source description (publisher paywalls); both
  are flagged accordingly in their own confidence_rationale and should be
  read as directionally reliable, not exhaustively checked.
- This pull is a literature-methods survey, not a skill draft. Per
  GOV-BEHADJ-1's own `notes` and `what_would_answer` fields, formalizing any
  of this into `.claude/skills/` remains explicitly out of scope for this
  pass and should not be treated as validated until applied to a real
  organism-level behavioural claim and shown to change (or not change) the
  adjudication outcome, per GOV-HELDOUT-1's discipline.

## Papers pulled in this review

| # | First author | Year | Venue | Direction | Contribution |
|---|--------------|------|-------|-----------|---------------|
| 1 | Crabbe, Wahlsten & Dudek | 1999 | Science | mixed | Historical case: standardized multi-lab replication still found context-idiosyncratic effects |
| 2 | Lit, Schweitzer & Oberbauer | 2011 | Animal Cognition | mixed | Modern Clever Hans replication; complicates "Blind" step's scope |
| 3 | Wiltschko et al. | 2015 | Neuron | supports | Rigorous unsupervised discovery precedent (MoSeq); relocates Goodharting risk to model order |
| 4 | McClintock et al. | 2020 | Ecology Letters | mixed | HMM state-inference machinery + documented state-count/data-driven-state pitfalls |
| 5 | Steegen et al. | 2016 | Perspectives on Psych Sci | supports | Formal statistical method for the "Adjudicate" step (multiverse analysis) |
| 6 | Cobbe et al. | 2019 | ICML | mixed | Highest-fidelity mapping; direct caution re: motivating Fishtank observations |
| 7 | Gygax, van Zeeland & Rufener | 2022 | Ethology | mixed | More rigorous sequence-structure method; complicates naive Markov-transition language |
| 8 | Belkaid et al. | 2020 | Communications Biology | supports | Worked positive template for "variability is not noise" + discriminating perturbation |
| 9 | Flake & Fried | 2020 | AMPPS | supports | Formal construct-validity framework for the anti-Goodharting checklist |

## Papers/leads considered and not pulled (scope note, not exhaustive)

Given the 12 named domains and the effort budget for this pass, several
named literatures (motor control/movement chunking specifically, animal
cognition/comparative-psychology detour and reversal-learning tasks,
robotics/embodied-AI sim-to-sim generalization beyond the RL entry already
pulled, dynamical-systems attractor/metastability formalisms) were not
independently searched in this pass and remain open for a follow-on pull if
GOV-BEHADJ-1 progresses toward skill drafting. This is a scope limitation to
flag explicitly, not a claim that those literatures are unimportant or
contradict anything found here.
