# SD-033e Prong D — Frontopolar analog literature synthesis

**Status:** Initial synthesis, 2026-04-27.
**Scope:** Five-paper biological grounding for the SD-033e frontopolar analog, addressing MECH-264 (counterfactual-value tracking), MECH-265 (relative-importance monitoring across competing goals), the gateway / disengagement function, and the rostral-pole position in the executive-control hierarchy.

This synthesis is the prerequisite for the SD-033e design doc (Phase 1.1 of the SD-033e preparation plan in `evidence/planning/sd033_governance_plan.md`). The five entries below establish the architectural commitment that SD-033e will need to make, and the open questions that the design doc must address.

## The five entries

1. **Boorman, Behrens, Woolrich & Rushworth 2009** (Neuron, [DOI 10.1016/j.neuron.2009.05.014](https://doi.org/10.1016/j.neuron.2009.05.014)) -- fMRI demonstration that frontopolar cortex tracks the relative advantage in favor of switching to a foregone alternative, with vmPFC encoding current-decision value. Foundational paper for FPC counterfactual tracking. Direct support for **MECH-264** (pairwise counterfactual evaluation), partial support for **MECH-265** (the design is pairwise chosen-vs-alternative, not K>=2-way).

2. **Burgess, Dumontheil & Gilbert 2007** (TiCS, [DOI 10.1016/j.tics.2007.05.004](https://doi.org/10.1016/j.tics.2007.05.004)) -- Theoretical synthesis of the gateway hypothesis: rostral PFC (BA 10) supports switching between external (environmental) and internal (self-generated) representations, with medial vs lateral BA 10 dissociation. Architectural anchor for the SD-033e commitment that the FPC analog supports both external-engagement and internal-cognition modes.

3. **Mansouri, Buckley, Mahboubi & Tanaka 2015** (PNAS, [DOI 10.1073/pnas.1422629112](https://doi.org/10.1073/pnas.1422629112)) -- Macaque bilateral selective FPC lesion. Causal phenotype: lesioned animals show *better* current-task focus, *augmented* post-conflict cognitive control adjustment, and *better* memory for relevant rule across distractions. The disengagement interpretation (FPC normally pulls cognitive resources toward novel / counterfactual goals at some cost to current-task focus) is the most coherent reading. Direct causal support for the architectural role MECH-264/265 specify.

4. **Mansouri, Koechlin, Rosa & Buckley 2017** (Nat Rev Neurosci, [DOI 10.1038/nrn.2017.111](https://doi.org/10.1038/nrn.2017.111)) -- Major integrative review on FPC managing competing goals. Central thesis: primate FPC monitors current vs alternative goals (basic role); humans further specialise in parallel monitoring of multiple goals. Direct theoretical support for **MECH-265** (K>=2-way set monitoring), with the human-specific elaboration creating a transfer-risk question for non-biological agents.

5. **Koechlin & Summerfield 2007** (TiCS, [DOI 10.1016/j.tics.2007.04.005](https://doi.org/10.1016/j.tics.2007.04.005)) -- Information-theoretical account of executive control via hierarchical control signals along the anterior-posterior axis of lateral PFC. Architectural framing: the FPC analog sits at the rostral end of the executive-control gradient, at the most abstract / branching / counterfactual level. Provides the hierarchical-position commitment SD-033e inherits.

## Synthesis: answers to the four lit-pull synthesis questions

The SD-033 governance plan posed four synthesis questions for Prong D. The answers are:

### (a) Pairwise (MECH-264) vs K>=2-way (MECH-265) counterfactual evaluation?

**Both, with separate supporting evidence.** Boorman 2009 establishes pairwise counterfactual tracking (MECH-264) as the basic, well-evidenced FPC function — fMRI signal scales with the chosen-vs-alternative-advantage, and FPC-vmPFC functional connectivity changes at switch decisions. The pairwise structure is empirically clean and architecturally simple.

K>=2-way set monitoring (MECH-265) is supported by the Mansouri 2017 review as the natural extension of the basic role, with the parallel-monitoring component argued to be a human-specific elaboration of primate FPC function. The empirical evidence for K-way monitoring is more theoretical / inferential than direct: the WCST lesion phenotype (Mansouri 2015) is consistent with K>=2-way monitoring but does not strictly demonstrate it because the WCST has 4 simultaneously-available cards (the lesion affects performance regardless of whether monitoring is pairwise or K-way).

**Recommendation for SD-033e design doc:** Commit to MECH-264 pairwise counterfactual evaluation as the core mechanism (empirically clean). Treat MECH-265 K-way monitoring as a *generalisation* of the same machinery, implementable as parallel pairwise comparisons against a value-of-current-decision reference. This is computationally simpler than a true K-way set-monitoring computation and is consistent with the available evidence.

### (b) Continuous-modulatory vs discrete-switching gateway function?

**Continuous-modulatory at the biological level; SD-033e inherits this with a discrete-mode wrapper.** Burgess 2007 frames the gateway function as a continuous modulation between external and internal attention. Boorman 2009's FPC counterfactual signal is also continuous (scales with chosen-vs-alternative advantage). Mansouri 2015's lesion phenotype is consistent with a graded disengagement pressure rather than discrete mode-state transitions.

**Recommendation for SD-033e design doc:** The FPC analog's score_bias output should be *graded* (not discrete admit/reject), modulated by the continuous counterfactual-value signal. The discrete operating-mode commitment in MECH-261 is at a higher level of abstraction than the FPC analog's output and does not need to be mirrored in the FPC analog itself. The FPC analog modulates rule_state weights graded over time; mode-state-transitions happen elsewhere (SalienceCoordinator).

### (c) Lesion specificity: is FPC ablation a generic executive deficit?

**No -- the lesion phenotype is specific and dissociable.** Mansouri 2015 shows that FPC lesion produces a paradoxical *improvement* on distractor-resistance and *augmented* post-conflict adjustment, rather than a generic executive deficit. PCC-lesioned controls do not show this pattern. The FPC-specific phenotype is therefore not a non-specific frontal-damage syndrome.

**Recommendation for SD-033e design doc:** The FPC analog should function as a *disengage-and-redistribute* module, not as a current-task focus module. Implementation: the FPC analog's score_bias should *reduce* current-candidate weight in proportion to counterfactual evidence, not increase it. This is the opposite of what a naive design might assume (FPC supports executive control -> FPC augments current-task focus). The lesion phenotype directly contradicts that naive reading.

### (d) Training signal for counterfactual-value heads?

**Not strictly determined by the available evidence, but the most architecturally coherent option is reward PE on unchosen options through counterfactual rollouts.** Boorman 2009's Bayesian RL model uses counterfactual reward-PE updates (the value of the unchosen option is updated based on a model-based prediction of what reward it would have produced). Mansouri 2017 review notes the training-dependent emergence of FPC counterfactual signals during human cognitive development.

The SD-033a A2 lit-pull (Buckley 2009, Mansouri 2020, Badre & Nee 2018, Johnson 2016 -- already indexed) recommended corticostriatal-RPE phased training for the rule-bias projection. The natural composition for SD-033e is that the FPC analog inherits the same training signal architecture: phased training with a corticostriatal-RPE-style signal over counterfactual rollouts.

**Recommendation for SD-033e design doc:** For V3, implement the FPC analog as a frozen-random head (analogous to SD-033a A2 frozen-random landing) with phased training deferred. For V4 reconsideration, the candidate training signal is reward-PE on counterfactual rollouts via the existing E2 model -- this would integrate cleanly with the V3 hippocampal-CEM machinery and the SD-039 / MECH-292 / MECH-293 ghost-goal substrate.

## Open questions for the SD-033e design doc

The synthesis above resolves the four lit-pull questions but leaves three open architectural questions for the SD-033e design doc itself:

1. **Hierarchical wiring vs parallel wiring with SD-033a.** Koechlin & Summerfield 2007's A-P-gradient framework supports hierarchical: FPC analog modulates SD-033a's rule_state. But the strict cascade has been challenged (Badre & Nee 2018), and a parallel-with-bidirectional-modulation wiring is also consistent with the evidence. The design doc must commit to one.

2. **Substrate-localisation: medial / lateral BA 10 split, or unified?** Burgess 2007 dissociates medial (external) from lateral (internal) BA 10. Mansouri 2017 emphasises a more integrated functional organisation. SD-033e should not lock to the strict medial/lateral split as if it were decided.

3. **Computational granularity of K-way monitoring.** If MECH-265 is implemented as parallel pairwise comparisons against a value-of-current-decision reference (recommendation a above), the FPC analog needs a list of currently-tracked alternative goals. How does this list get populated and pruned? Candidates: (i) MECH-292 ghost-goal bank (already implemented for blocked goals); (ii) hippocampal trajectory proposals filtered for counterfactual-relevance; (iii) explicit alternative-goal register populated by SD-032a operating-mode shifts. The design doc should resolve this.

## Falsifiable signature for SD-033e

When the design doc is written and an experiment queued, the falsifiable signature should follow from the disengagement interpretation: an FPC-analog-ablation should produce *better* current-task focus and *worse* exploration of counterfactually-valuable alternatives, mirroring the Mansouri 2015 lesion phenotype. This is the cleanest empirical handle and the test that would distinguish SD-033e from a generic executive-control augmentation.

## Process notes

- Five entries written to `evidence/literature/targeted_review_frontopolar_analog_prong_d/entries/`.
- Synthesis written to this file (the design doc, when written, should link to this synthesis).
- The Christoff et al (FPC internally-directed cognition) and Badre & Nee 2018 (rostral pole gradient) papers from the secondary candidates list were not pulled in this round -- the five-paper Prong D survey is sufficient to establish the architectural commitment, and Badre & Nee 2018 is already indexed under the SD-033a A2 lit-pull (the same paper supports both the rule-learning and the rostral-gradient questions). Christoff's internally-directed-cognition work (PNAS 2009, NeuroImage 2009) is a candidate follow-up if the design-doc work surfaces specific gaps that those papers address.
- The Mansouri 2020 paper (already in SD-033a A2 review) addresses dynamic emergence of abstract rules; that finding is also relevant to SD-033e but is not a Prong-D-specific contribution beyond what is captured here.
