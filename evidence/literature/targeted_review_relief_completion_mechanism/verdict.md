# Relief / Suffering-Reduction Completion: Pre-Registration Lit-Pull Verdict

**Date:** 2026-05-03
**Question:** Does relief / suffering-reduction in the brain use the same goal-achievement / reward completion circuitry, or a distinct mechanism?
**Failure mode being guarded:** SD-011 / SD-003 pattern — philosophy-right, mechanism-wrong. No MECH/SD registered yet; this verdict feeds the design decision.

## Recommendation

**Hybrid, leaning Model 1.** Confidence 0.80.

The relief-completion *event itself* uses goal-achievement / reward-circuit machinery and should reuse the existing release pipeline (MECH-057a, MECH-091, MECH-094). The *predictive encoding of safety cues* uses a parallel prefrontal-hippocampal substrate and should be modelled as a separate mechanism. These two are coordinated but architecturally distinct, and collapsing them into one mechanism is the most likely failure mode for an REE substrate.

## Strongest findings per branch

### Model 1 wins for the completion event

- **[Andreatta et al. 2012](https://doi.org/10.1101/lm.026864.112)** — cross-species double dissociation: relief activates and requires ventral striatum (reward circuit), fear activates and requires amygdala. This is the load-bearing structural anchor. Confidence 0.86.
- **[Navratilova et al. 2012](https://doi.org/10.1073/pnas.1214605109)** — pain relief activates VTA dopamine neurons, drives NAc dopamine release, and the place preference is dopamine-antagonist-blockable. Pins the cellular mechanism. Confidence 0.84.
- **[Ramirez et al. 2015](https://doi.org/10.1523/JNEUROSCI.1331-14.2015)** — active avoidance behaviour requires the basal-amygdala-to-NAc-shell circuit, dissociable from NAc core and from CeA-PAG fear circuitry. The action-policy node for suffering-reducing behaviour overlaps with the reward-system node. Confidence 0.78.

These three converge on: relief-completion sits on reward-system substrate at the structural, cellular, and behavioural-control levels.

### Model 2 wins for safety-cue prediction (parallel substrate)

- **[Kreutzmann et al. 2020](https://doi.org/10.1007/s00213-020-05527-7)** — the infralimbic cortex is required for *expression* (not acquisition) of conditioned safety; PL inactivation has no effect. Confidence 0.74.
- **[Meyer et al. 2019](https://doi.org/10.1073/pnas.1910481116)** — cross-species (mouse + human): conditioned inhibition of threat via safety routes through a vHipp-to-PL pathway specifically, dissociable from amygdalar and IL pathways. Confidence 0.78.

These converge on: predictive encoding of "this cue predicts safety / threat-absence" has its own prefrontal-hippocampal substrate, separate from both the threat circuit and the relief-completion circuit.

### Qualifiers / cautions on Model 1

- **[Brischoux et al. 2009](https://doi.org/10.1073/pnas.0811507106)** — ventral-VTA dopamine neurons are *excited* by aversive footshock onset (juxtacellularly confirmed). Confidence 0.80.
- **[Bromberg-Martin, Matsumoto & Hikosaka 2010](https://doi.org/10.1016/j.neuron.2010.11.022)** — review framework: at least two functionally distinct DA populations, value-coding vs salience-coding. Confidence 0.79.

Together these say the REE substrate cannot model "phasic dopamine = good thing" as a unitary signal. The relief-relevant DA channel is the value-coding one (which is the same one reward-onset uses). The salience-coding DA channel fires for both reward and aversive events and serves orienting / arousal functions; it is upstream of MECH-091 (phase-reset) but should not feed MECH-094 (categorical write gate).

### Behavioural foundation

- **[Tanimoto, Heisenberg & Gerber 2004](https://doi.org/10.1038/430983a)** — Drosophila opponent-timing demonstration: the same shock acts as either an aversive or appetitive reinforcer depending on cue timing. Cross-species behavioural anchor for the principle that relief is a positive reinforcer, not just a return to baseline. Confidence 0.78.

## Architectural implications for REE

Two mechanisms, coordinated:

**MECH-X (relief-completion event, M1).** Fires when a derived suffering-state comparator crosses a downward threshold. Reuses MECH-057a (commitment-release / beta-gate-drop), MECH-091 (salient-event phase reset), and MECH-094 (categorical hypothesis-tag write gate). The polarity of the reinforcement is set at the input — what counts as the completion is the suffering-derivative crossing the threshold, not a reward-onset event. The downstream tag-and-store machinery is shared with goal-achievement. "Things that just reduced suffering" are tagged in the same approach-attractor structure as "things liked."

**MECH-Y (safety-cue prediction, parallel).** A learned predictive structure analogous to but separate from "things liked." Encodes "this stimulus / context predicts that suffering will not happen / will be reduced." Anatomically maps to IL-equivalent and vHipp-PL-equivalent substrate. Behaviourally gates: (a) commitment-release thresholds — is this context safe enough to drop the avoidance commitment? (b) approach toward safety-associated stimuli, including the clinical patterns of attachment to relief-providers, comfort objects, and trusted others.

The teaching signal that updates MECH-Y is the same MECH-X completion event, but the *store* is parallel. This matters because:
- It predicts that relief-cue learning can proceed even when the immediate completion event is not occurring (extinction-style safety learning).
- It predicts that loss of safety-cue learning produces a clinical pattern distinct from loss of goal-cue learning — chronic anxiety / persistent avoidance commitments that cannot find a safe context to release.
- It predicts that if MECH-X never fires cleanly (relief-completion event missing or noisy), avoidance commitments accumulate without ever being tagged-and-released, which is a candidate substrate for chronic anxiety / PTSD-style persistence beyond the MECH-094 tag-loss story.

## What this lit-pull does *not* settle

- The exact temporal profile of relief-DA versus reward-DA. The convergent literature implicates the same value-coding population, but does not directly compare offset-DA timing to onset-DA timing. An REE implementation should treat 'same machinery' as 'same downstream pipeline', not as 'identical phasic profile'.
- Whether the threat-absence (cue predicts no shock) and threat-termination (cue follows shock cessation) signals dissociate in REE-relevant ways. The Andreatta 2017 entry (not in this slate; flagged for follow-up if needed) suggests they do behaviourally; the architectural consequence in REE is unsettled.
- The role of opioid signalling in the ACC at relief, which the Navratilova-Atcherley-Porreca 2015 review flags as a third pillar of the relief circuit. If REE wants a deeper substrate-level model, an ACC-opioid follow-up lit-pull would be useful.

## Mapping to existing REE claims

- **MECH-057a** (commitment release / beta-gate drop at goal completion): the lit-pull supports extending the trigger condition to include suffering-derivative-crossing-threshold, not only goal attainment.
- **MECH-091** (salient-event phase reset): supported as the mechanism for marking the completion moment; both reward onset and aversive offset count as salient events that should phase-reset.
- **MECH-094** (categorical hypothesis tag / write gate): supported as the mechanism for tagging "this just worked" at completion. The polarity of the polarity of the value-coding DA pulse handles the sign; the tag itself is categorical.
- **SD-011** (dual nociceptive streams, sensory pain vs suffering): the relief-completion mechanism would naturally operate on the suffering-stream derivative rather than on the sensory-pain derivative, which is consistent with SD-011's separation.

## Recommended next steps (not done in this session)

1. Draft a candidate MECH for relief-completion (M1-with-DA-heterogeneity-caveat) and a candidate MECH for safety-cue prediction (M2/parallel), as separate registry entries, with this verdict as the lit-anchor.
2. Optional follow-up lit-pull on ACC-opioid signalling at relief (Navratilova-Atcherley-Porreca 2015 + Bushnell line) if REE wants a third-pillar substrate model.
3. Optional follow-up on threat-absence vs threat-termination dissociation (Andreatta 2017 + extension) if the architectural decision needs to differentiate these in REE.

## Confidence components

- **Cross-species convergence**: high (Drosophila, rodent, human all in slate; double dissociations in two of the entries).
- **Cellular mechanism specificity**: high (Navratilova electrophysiology + microdialysis + pharmacology in one paper; Brischoux juxtacellular labelling).
- **Architectural mapping fidelity**: moderate-high (Andreatta directly tests M1 vs M2 at the structural level; Kreutzmann/Meyer add the parallel-safety qualifier).
- **Transfer to REE goal-pursuit substrate**: moderate. The substrate REE wants to model is more elaborate than any of these paradigms. The convergent finding gives reasonable transfer confidence; the precise substrate mapping for the SD-011 suffering stream would benefit from a follow-up implementation experiment.

Net: 0.80 confidence in the hybrid recommendation, with the M1 component (completion event reuses goal-achievement machinery) being the more strongly supported half and the M2 component (parallel safety-cue substrate) being the qualifier that prevents a clean single-mechanism design.
