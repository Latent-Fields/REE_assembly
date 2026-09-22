# Thought Intake: Behavioural Precision Provenance and Sleep Plasticity Gain

**Date:** 2026-09-22  
**Raw thought file:** `docs/thoughts/2026-09-22_behavioral_precision_provenance_and_sleep_plasticity_gain.md`  
**Status:** structured intake; hypothesis-generating; literature-scouted; no claim registration or build authorisation  
**Primary scope:** hippocampal episodic/index memory, precision/confidence, E1/E2 predictive learning, replay priority, sleep consolidation, plasticity/write authority  
**Immediate trigger:** MECH-572 / INV-063 leg B — fixed-size consolidation displacement on converged versus fresh readouts.

## Verbatim prompt

> “And it may need stored precision values from the relevant behavioural ‘test’.”

Follow-up instruction:

> “Let’s make this a thought intake and do some literature searching to elucidate the mechanism further including with anatomical landmarking.”

## Core proposal

The current MECH-572 result suggests that REE's sleep consolidator can impose almost the same parameter displacement on a nearly converged representation as on a poorly fitted one. The resulting sign reversal is plausibly a **gain-control failure** rather than evidence that consolidation is intrinsically harmful.

The present thought sharpens that observation:

> **A replayed episode may need to carry forward the epistemic conditions under which it was behaviorally tested, so that later consolidation can decide both whether the episode deserves replay and how strongly it is allowed to alter a persistent model.**

The relevant memory object may therefore be richer than an episode tuple. It may need an **epistemic / precision provenance packet**.

A minimal candidate packet is:

```
episode_id / hippocampal index
context / latent state
prediction_at_test
prediction_precision_at_test
action_that_exposed_prediction
observed_outcome
outcome_or_observation_precision
signed/unsigned prediction error or mismatch
novelty / salience / value relevance
real-vs-reconstructed-vs-simulated provenance
behavioural consequence
timestamp / developmental state
```

The most important distinction is:

- **historical model precision**: how strongly the organism believed the prediction before the behavioural test;
- **evidence precision**: how reliable or diagnostic the observed consequence was;
- **current model precision**: how strongly the model now holds the relevant belief when the episode is replayed.

Historical confidence must **not** become a permanent protection term. Otherwise an early confidently-wrong attractor becomes self-sealing. Historical precision is provenance: it tells sleep how surprising and diagnostically important the later outcome was. Current precision must still be recomputed against the accumulated evidence.

A Bayesian-style abstraction is useful without committing REE to a literal Bayesian implementation:

```
replay_priority_i = f(stored prediction error,
                      stored evidence precision,
                      novelty/salience,
                      unresolved contradiction,
                      behavioural relevance,
                      age/staleness)

plasticity_gain_i = g(stored evidence precision,
                      current model precision,
                      stored miscalibration,
                      later corroboration/contradiction,
                      provenance,
                      current operating mode)
```

This is potentially a stronger and more general interpretation of MECH-572 than “use a smaller learning rate.”

## Current REE coverage: what is already present

This is not a blank-slate proposal. Several existing families already own pieces of it:

| Existing REE item | Already owns | Relation to this thought |
|---|---|---|
| **MECH-572** | consolidation sign depends on step-to-residual ratio; fresh Adam makes displacement nearly independent of residual | immediate trigger; supplies the fixed-gain failure |
| **MECH-573** | readability must beat a trivial predictor, not merely random initialization | prevents low residual from being mistaken for high epistemic precision |
| **MECH-574** | productive replay may need regenerated / improved targets rather than re-presented observations | says content quality and gain are separable |
| **MECH-016** | sleep precision recalibration; neuromodulatory/gain/plasticity evidence | existing sleep-side precision family |
| **ARC-055** | confidence/reliability signal should be available to learning updates | existing learning-side confidence family |
| **MECH-043** | precision-weighted unsigned prediction error / dopamine-like modulation | existing precision-weighted error family |
| **MECH-368 / MECH-431** | event-level write authority and tag-and-capture eligibility | candidate admission/write gate into which precision provenance could feed |
| **MECH-284 / MECH-285** | staleness accumulation and sleep replay prioritization | current replay-selection substrate |
| **MECH-269 / AnchorSet** | scale-tagged hippocampal anchors with dual-trace preservation | likely current storage locus to inspect/extend |
| **ARC-137** | typed offline transformations and distal readouts | governance boundary: replay/plasticity gain is not itself behavioural authority |

The genuinely new synthesis is not “precision exists” or “sleep recalibrates.” It is the proposed **binding of behavioural test reliability to episodic provenance, and its later use as an input to sleep-time plasticity gain**.

## Current V3 implementation check

A targeted inspection was performed on the live `ree-v3` paths most directly implicated:

- `ree_core/hippocampal/anchor_set.py`
- `ree_core/hippocampal/module.py`
- `ree_core/hippocampal/staleness_accumulator.py`
- `ree_core/sleep/replay_sampler.py`
- `ree_core/sleep/cross_module_consolidation.py`

### What the inspected hippocampal payload already stores

`AnchorGoalPayload` currently preserves:

- `z_goal_snapshot`
- `wanting_strength`
- `arousal_tag`
- `last_vs`
- `staleness_at_write`
- `payload_written_step`

This is important: REE already has the architectural precedent that a hippocampal anchor can preserve **state-at-write metadata** in addition to content.

### What is not present in that inspected payload/path

In these specific files, no per-anchor/per-episode fields were found for:

- prediction precision/confidence at behavioural test;
- outcome/observation precision;
- prediction error tied to the episode;
- behavioural success/failure of the tested prediction.

Likewise, `SleepReplaySampler` currently samples from a frozen **staleness** snapshot, not a precision-provenance vector, and `CrossModuleConsolidator` has no precision/confidence input to its learning rate or step schedule.

This is a **path-local finding**, not a claim that no other REE subsystem stores any precision or outcome signal. It is enough to identify a plausible information-loss boundary in the currently inspected hippocampal-anchor -> replay-sampler -> consolidator path.

## Focused literature scan

### 1. Confidence can be maintained per learned relation and used to set learning gain

Meyniel & Dehaene (2017, PNAS; doi: 10.1073/pnas.1615773114) provide a particularly direct computational analogue. Human subjects maintained distinct confidence estimates for learned transition probabilities. Surprise and confidence were represented separately and combined in the **right inferior frontal gyrus (rIFG)** into a confidence-weighted update signal. The **intraparietal sulcus (IPS)** carried confidence-like signals; sensory/frontal regions carried surprise-like signals.

This supports the architectural proposition that confidence is not merely a report variable. It can be a **stored/maintained statistic that changes how much new evidence updates an existing model**.

Meyniel (2020) further reported that confidence dampens surprise responses and alters beta-band activity and pupil-linked arousal, suggesting that confidence weighting may operate partly by changing the **state/gain of the learning system**, not solely by algebraically scaling a loss.

**Limit:** these studies concern probabilistic sequence learning, not episodic sleep replay. They support the gain principle, not the hippocampal storage mechanism.

### 2. Memory confidence is represented within medial temporal lobe circuitry

Rutishauser et al. (2015, Nature Neuroscience; doi: 10.1038/nn.4041) recorded 1,065 single neurons in human hippocampus and amygdala during memory decisions. A population of memory-selective neurons carried trial-by-trial familiarity and subjective retrieval confidence.

This is important anatomical permission for the present idea: a confidence/strength-like variable is available **inside medial temporal lobe (MTL) memory circuitry**, rather than existing only as a late frontal metacognitive report.

**Limit:** retrieval confidence is not the same quantity as precision-at-encoding or precision-at-behavioural-test. The result supports local availability, not durable binding of precision to an episodic trace.

### 3. CA1 is well positioned to bind prediction strength to mismatch

Human high-resolution functional magnetic resonance imaging studies support a comparator role for hippocampal **CA1**. Chen et al. (2015, Journal of Neurophysiology; doi: 10.1152/jn.00149.2015) found that CA1 responses to sequence violations increased when the violated prediction had been stronger. Earlier work similarly found CA1 to be especially sensitive to match/mismatch.

This is striking for REE because the desired stored quantity is not simply “error occurred.” A mismatch is more diagnostic when it violates a **strong prediction**. CA1 sits at a circuit junction where retrieved/predicted information from CA3 can be compared against entorhinal sensory input.

Bein et al. (2020, Nature Communications; doi: 10.1038/s41467-020-17287-1) further showed that mnemonic prediction errors shift hippocampal network state toward encoding rather than retrieval. Thus prediction error can change not only content but **which memory-processing regime becomes active**.

### 4. The hippocampal–entorhinal circuit provides a plausible anatomical write path

High-resolution work on hippocampal-entorhinal layers supports a directional distinction:

- superficial entorhinal cortex (EC) strongly feeds dentate gyrus (DG), CA3 and apical CA1;
- CA1/subiculum provide major hippocampal output to deep EC;
- novelty is especially associated with input-side structures, while later memory fate depends strongly on hippocampal output pathways.

A plausible biological analogy is therefore not “store precision in CA1” as a single scalar register. Rather, the **episode/index may be formed across DG/CA3/CA1-entorhinal circuitry while precision/mismatch signals influence the tag and the later output state**.

### 5. Behavioural tagging supplies a mechanism for preserving “this event matters later”

Synaptic tagging and capture / behavioural tagging literature provides a mechanistic precedent for a transient learning event setting a local tag whose persistence is later stabilized by neuromodulatory resources. Novelty-driven dopamine, including dopamine released from **locus coeruleus (LC)** projections to hippocampus, can enhance persistence through hippocampal D1/D5 receptors.

Takeuchi et al. (2016, Nature; doi: 10.1038/nature19325) showed that LC tyrosine-hydroxylase-positive neurons strongly innervate hippocampus, respond to novelty, and can enhance memory persistence in a D1/D5-dependent manner.

This does **not** show a numeric precision value being stored. It provides a biologically credible substrate for a weaker statement: waking events can acquire a **durable eligibility/priority mark** based on behavioural significance.

### 6. Replay is already selective according to learning need and experience

Schapiro et al. (2018, Nature Communications; doi: 10.1038/s41467-018-06213-1) found that individual items remembered less well were preferentially replayed in human hippocampus during subsequent rest, and replay predicted later memory improvement.

Huelin Gorriz et al. (2023, Nature Communications; doi: 10.1038/s41467-023-43939-z) found in rats that sleep replay priority increased with amount of experience and decreased with familiarity; cumulative **awake replay** predicted later sleep replay priority.

The 2025 review by van der Meer & Bendor (Trends in Neurosciences; doi: 10.1016/j.tins.2025.02.006) develops an explicit candidate mechanism: salient experiences generate more awake sharp-wave-ripple replay, producing a **latent excitable state in hippocampal–cortical circuits** that biases which memories are replayed in sleep.

This is close to a biological answer to “how can information available during the behavioural test still matter during sleep?” The answer may not be a literal scalar copied into a memory record. It may be a **distributed persistent tag/excitability state**.

### 7. Sleep supplies a separate gain/plasticity regime

Swift et al. (2018, Current Biology; PMID 30393040) showed that abnormally activating LC during sleep disrupts spindles, ripple-spindle coupling, hippocampal place-cell stability and spatial memory. LC silence therefore appears permissive for the normal sleep consolidation regime.

Fehér et al. (2026, NeuroImage; doi: 10.1016/j.neuroimage.2026.121723) provide complementary human evidence: a daytime nap reduced indices of net cortical synaptic strength while **increasing inducibility of long-term-potentiation-like associative plasticity**. Sleep can therefore change the gain landscape itself, not just provide replay time.

These findings fit MECH-016 particularly well: sleep may regulate **how writable the system is**.

## Anatomical landmarking

This should be treated as a candidate circuit map, not a one-region/one-function assignment.

| Stage | Anatomical landmarks | Candidate computation relevant to REE |
|---|---|---|
| **Prediction formation / retrieval** | CA3, hippocampal recurrent circuitry; medial temporal cortical inputs | retrieve/complete expected episode or state against which current input can be tested |
| **Comparator / behavioural test** | **CA1**, direct entorhinal input + CA3 input | compare expectation with actual input; mismatch magnitude depends on prediction strength |
| **Episode/index formation** | DG/CA3, CA1, superficial/deep entorhinal cortex, subiculum | bind event/context and route a durable index/output |
| **Confidence / reliability estimation** | hippocampus + amygdala memory-selective neurons; **IPS**; **rIFG**; orbitofrontal/prefrontal networks | maintain confidence; combine confidence with surprise; represent top-down expectation |
| **Salience/tagging neuromodulation** | **LC**, ventral tegmental area (VTA), hippocampal D1/D5 receptors; amygdala for arousal relevance | decide which waking events receive persistence/replay eligibility |
| **Awake replay / pre-sleep tagging** | hippocampal sharp-wave ripples with hippocampal-cortical ensembles | reinforce a latent excitability/tag that can survive the disappearance of the original behavioural cue |
| **NREM replay orchestration** | frontal / orbitofrontal cortex slow oscillations, thalamus / thalamic reticular circuitry spindles, hippocampal ripples | open temporally precise windows for replay and plasticity |
| **Hippocampal-prefrontal dialogue** | medial/orbitofrontal PFC, hippocampus; nucleus reuniens and entorhinal/perirhinal routes as candidate intermediaries | bidirectional constraint and transfer between episodic index and cortical model |
| **Plasticity-state control** | LC/noradrenergic system, cholinergic state, dopamine-related tagging systems | regulate whether replay causes strong learning, weak refinement, protection, or no write |
| **Cortical incorporation** | prefrontal/orbitofrontal, retrosplenial and distributed task-relevant neocortex | integrate replayed structure into persistent cortical/world-model representations |

### Particularly important 2026 anatomical evidence

Wodeyar et al. (2026, PNAS; doi: 10.1073/pnas.2517454123) simultaneously recorded **orbitofrontal cortex (OFC), thalamus and hippocampus** in 19 humans with epilepsy during sleep. Orbitofrontal slow oscillations modulated thalamic spindles and hippocampal ripples; hippocampal ripple rate and coupled hippocampal–orbitofrontal ripples were the strongest positive predictors of overnight memory improvement.

This supplies an unusually concrete landmark for a REE analogue:

```
frontal slow state
    -> thalamic timing / spindle gate
    <-> hippocampal replay
    <-> frontal/cortical incorporation
```

It is compatible with earlier human intracranial work showing rapid bidirectional prefrontal–hippocampal dynamics during NREM sleep (Helfrich et al., 2019) and with closed-loop human stimulation showing that prefrontal stimulation precisely synchronized to medial-temporal slow waves enhances spindle/ripple coupling and recognition memory (Geva-Sagiv et al., 2023).

The **nucleus reuniens** is a plausible anatomical coordinator rather than a demonstrated precision store: it projects to both medial PFC and hippocampus and is positioned to modulate their synchrony. Entorhinal/perirhinal pathways provide additional bidirectional routes.

## Candidate mechanism for REE

### Wake: create a behavioural evidence packet

When REE makes a prediction and then acts in a way that exposes it to the environment:

1. snapshot the relevant prediction/model state;
2. snapshot **prediction precision**;
3. record the realised outcome and **outcome reliability**;
4. calculate mismatch/prediction error;
5. attach context, provenance, salience and behavioural consequence;
6. bind this metadata to the relevant hippocampal/episodic index or to a linked evidence record.

This is closer to a **behavioural test record** than an ordinary memory.

### Awake rest: tag/select without yet rewriting the world model

Awake replay can then increase the future replay eligibility of episodes with combinations such as:

- high diagnostic prediction error;
- low-confidence knowledge in a behaviourally important domain;
- high-confidence prediction that was contradicted by reliable evidence;
- novel/high-value outcomes;
- unresolved conflict with other episodes.

This stage should mainly answer **what deserves offline work?**

### Sleep: recompute gain, do not replay the old gain

At sleep time, retrieve the evidence packet and compare it with the **current** model.

A useful distinction is:

```
stored prediction precision     = what I believed then
stored evidence precision       = how trustworthy that test was
current model precision         = what I believe now
current contradiction structure = what later evidence has accumulated
```

Then derive a plasticity gain.

A high-confidence old prediction that was reliably falsified should *increase* the diagnostic importance of the trace, not protect the old attractor. Conversely, a low-confidence old prediction followed by a noisy outcome should have little authority.

This is why “store precision” should become **store precision provenance**, not “freeze confidence with the memory.”

### Write boundary

Replay priority and plasticity gain remain separate decisions:

1. **replay selection** — should this trace be reconsidered?
2. **plasticity gain** — how strongly may it change the target model?
3. **write authority** — is this kind of change permitted in this sleep phase?
4. **waking validation** — does the resulting representation actually improve endogenous behaviour?

This preserves ARC-137 / ARC-130 style organism-level validation and avoids granting offline coherence direct behavioural authority.

## Relationship to MECH-572

MECH-572 currently states that the across-sleep readout sign depends on the ratio between consolidation displacement and the remaining residual.

This thought suggests two levels:

**Level 1 — immediate engineering correction**
- stop using an update schedule whose displacement is almost independent of residual/convergence;
- test persistent optimiser state, lower learning rate, fewer steps, or an explicit displacement cap.

**Level 2 — architectural hypothesis**
- residual size is only a crude local proxy for “how much should this representation change”;
- a mature consolidator may need **precision- and provenance-conditioned plasticity**, potentially drawing on behaviourally grounded metadata stored with the replayed episode.

Level 2 must not be used to skip the simple Level-1 test. If MECH-572 is falsified by reducing the displacement-to-residual ratio, that is useful evidence; a precision architecture should then be motivated independently by better behavioural calibration, not retrofitted to rescue a failed result.

## Falsifiers / discriminating tests

### F1 — stored precision adds no information beyond current residual
Hold episode content, outcome, current model, and replay dose fixed. Vary only the historical confidence/precision under which the episode was behaviourally tested.

If replay priority, consolidation gain and later behaviour are unchanged once current residual/error is controlled, the stored-precision component is not load-bearing.

### F2 — evidence precision is irrelevant
Create matched episodes with the same prediction error but different reliability of the outcome/observation. If the system should learn equally from both, the proposed evidence-precision field is unnecessary.

### F3 — precision becomes self-sealing
If high historical prediction precision suppresses revision even when reliable contradictory evidence is replayed, the mechanism is wrong. High-confidence falsification should be diagnostically important, not protected.

### F4 — no durable behavioural-test tag
Manipulate confidence/salience during waking, then remove the original cue before sleep. If later replay priority cannot retain any dependence on the waking manipulation, there is no evidence for a stored/distributed tag bridging wake to sleep.

### F5 — replay priority and gain do not dissociate
If every factor that increases replay frequency proportionally increases parameter update magnitude, REE has collapsed two different control problems. A mature mechanism should allow “replay often, update gently” for uncertain or repeatedly checked traces and “replay selectively, update strongly” for reliable diagnostic evidence when appropriate.

### F6 — only a scalar is sufficient
Compare a single stored confidence scalar with a provenance packet containing historical model precision + outcome precision + prediction error. If the richer packet gives no improvement in calibration, stability, or adaptation across contradictory/noisy environments, do not add the extra dimensions.

## High-value REE experiments suggested by the thought

1. **Current-precision x stored-evidence-precision 2x2.** Same content and current residual; vary how reliable the original outcome was and how confident the current model is. Test update magnitude and direction.
2. **Confidently-wrong challenge.** Create an episode where a high-confidence prediction is reliably falsified. Correct architecture should reopen the model rather than protect it.
3. **Weak-memory replay challenge.** Match Schapiro-like conditions: lower-strength traces should be replay-prioritized without necessarily receiving a large write.
4. **Wake-tag lesion.** Preserve episodic content but remove only the precision/salience tag before sleep. Test whether prioritisation collapses.
5. **Gain lesion.** Preserve replay ordering but replace precision-conditioned update gain with fixed steps. Test whether the MECH-572-like overwrite phenotype returns.
6. **Post-sleep organism assay.** Require the changed model to alter native E1/E2 prediction and downstream E3 behaviour; internal loss movement alone is insufficient.

## What is new versus already owned

**Already owned**
- precision-weighted learning;
- sleep precision recalibration;
- event-level write gating;
- replay prioritisation by staleness;
- hippocampal anchor metadata;
- fixed-step consolidation pathology;
- organism-level behavioural validation doctrine.

**Potentially new**
- a **behavioural-test precision provenance packet** linked to hippocampal/episodic traces;
- use of that packet, alongside current model precision, to derive **sleep-time plasticity gain**;
- an explicit separation between **replay priority** and **write magnitude** based on different combinations of the same provenance signals.

No new claim ID is registered by this intake. The idea should first be checked against the complete current claims graph and, ideally, tested as a minimal metadata/gain intervention rather than expanded into a new module.

## Candidate claim formulations — NOT REGISTERED

1. **Behavioural precision provenance.** A memory trace that may later drive offline model revision must preserve enough information about the reliability of the original prediction and the reliability of the observed outcome to reconstruct the epistemic force of that behavioural test.
2. **Precision-conditioned consolidation gain.** Offline plasticity magnitude should depend on the relationship between replayed evidence precision and current model precision, rather than only on a fixed optimiser schedule or raw residual.
3. **Replay/write dissociation.** The signal deciding which memory is replayed need not be the signal deciding how strongly replay modifies a target model.

These are candidate formulations only; they may ultimately refine MECH-572/MECH-016/ARC-055/MECH-431/MECH-285 rather than deserving new IDs.

## Literature references used in this intake

- Meyniel F, Dehaene S. *Brain networks for confidence weighting and hierarchical inference during probabilistic learning.* PNAS. 2017. doi:10.1073/pnas.1615773114. PMID 28439014.
- Rutishauser U et al. *Representation of retrieval confidence by single neurons in the human medial temporal lobe.* Nature Neuroscience. 2015. doi:10.1038/nn.4041. PMID 26053402.
- Chen J, Cook PA, Wagner AD. *Prediction strength modulates responses in human area CA1 to sequence violations.* Journal of Neurophysiology. 2015. doi:10.1152/jn.00149.2015. PMID 26063773.
- Bein O et al. *Mnemonic prediction errors bias hippocampal states.* Nature Communications. 2020. doi:10.1038/s41467-020-17287-1. PMID 32651370.
- Takeuchi T et al. *Locus coeruleus and dopaminergic consolidation of everyday memory.* Nature. 2016. doi:10.1038/nature19325.
- Schapiro AC et al. *Human hippocampal replay during rest prioritizes weakly learned information and predicts memory performance.* Nature Communications. 2018. doi:10.1038/s41467-018-06213-1. PMID 30254219.
- Huelin Gorriz M, Takigawa M, Bendor D. *The role of experience in prioritizing hippocampal replay.* Nature Communications. 2023. doi:10.1038/s41467-023-43939-z. PMID 38071221.
- van der Meer MAA, Bendor D. *Awake replay: off the clock but on the job.* Trends in Neurosciences. 2025. doi:10.1016/j.tins.2025.02.006. PMID 40121166.
- Swift KM et al. *Abnormal locus coeruleus activity during sleep alters sleep signatures of memory consolidation and impairs place cell stability and spatial memory.* Current Biology. 2018. PMID 30393040.
- Helfrich RF et al. *Bidirectional prefrontal-hippocampal dynamics organize information transfer during sleep in humans.* Nature Communications. 2019. PMID 31395890.
- Ngo HVV et al. *Sleep spindles mediate hippocampal-neocortical coupling during long-duration ripples.* eLife. 2020. doi:10.7554/eLife.57011. PMID 32657268.
- Geva-Sagiv M et al. *Augmenting hippocampal-prefrontal neuronal synchrony during sleep enhances memory consolidation in humans.* Nature Neuroscience. 2023. PMID 37264156.
- Wodeyar A et al. *A hierarchical cascade of sleep rhythms supports motor memory and is hijacked by epileptic spikes in human epilepsy.* PNAS. 2026. doi:10.1073/pnas.2517454123. PMID 42378289.
- Fehér KD et al. *A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex.* NeuroImage. 2026. doi:10.1016/j.neuroimage.2026.121723. PMID 41544905.
- Vertes RP et al. *Anatomical substrates for direct interactions between hippocampus, medial prefrontal cortex, and the thalamic nucleus reuniens.* Brain Structure and Function. 2015. doi:10.1007/s00429-013-0543-5. PMID 23571778.

## Recommended routing

1. Keep this intake as an **integration hypothesis**, not a build instruction.
2. Cross-check whether any current claim already binds per-episode precision to hippocampal memory more specifically than the inspected AnchorSet path.
3. Feed the literature links into the existing MECH-016 / ARC-055 / MECH-043 / MECH-572 evidence map rather than duplicating them where already present.
4. The cheapest implementation probe is metadata-only: preserve a historical precision/evidence-precision field on selected waking traces, leave replay content and objective unchanged, and test whether a precision-conditioned gain removes overwrite without creating self-sealing high-confidence errors.
5. Only after that should governance decide whether this is a refinement of existing precision/write-gating claims or deserves a new registered mechanism.

## Routing update 2026-09-22 (session `compassionate-pike-fe9174`, user-commissioned)

**Status change:** the intake's "cheapest implementation probe is metadata-only" recommendation was
audited against live code and found to require new substrate on both precision legs (Result 6 of
the user brief): no evidence-precision producer existed anywhere in `ree_core`, and no producer of
the world-forward head's own precision. USER DECISION (recommendation ledger 520): build the
producers first, then run. Delivered the same day:

- **Spec:** `docs/architecture/precision_provenance_substrate_spec.md` (SD-PP-1..4).
- **Substrate (ree-v3 `9a3907d93c` + `074b6a795c`):** `precision.observation_reliability` (SD-PP-1),
  `precision.world_forward_epistemic_precision` (SD-PP-2), `hippocampal.replay_provenance_packet`
  (SD-PP-3), `sleep.provenance_conditioned_consolidation_gain` (SD-PP-4). Default OFF, bit-identical.
- **Necessities register:** `evidence/planning/precision_provenance_substrate_necessities_20260922.md`
  and `substrate_queue.json` rows SD-PP-1..4 (implemented_pending_validation) and SD-PP-B1..B8
  (registration only). Correction to this intake: the AnchorSet / StalenessAccumulator /
  SleepReplaySampler path inspected above is NOT on the weight-consolidation path that produces the
  MECH-572 phenotype; that pass draws `randperm` batches from the raw experience buffers (B2). The
  packet therefore rides the buffer index.
- **Preregistration + freeze record:** `evidence/planning/precision_provenance_consolidation_gain_design_20260922.md`.
- **Experiment:** V3-EXQ-1073 queued (diagnostic; evidence ceiling mechanistic/local because no
  default-on behavioural consumer of `e2.world_forward` exists, B1).
- **Pre-freeze finding, already measured:** the confidently-wrong condition (intake experiment 2 /
  falsifier F3) is UNPOSEABLE on the current world-forward head: it sits at copy-the-input (skill
  -0.071, MECH-573) and barely reads the action, so an action-map inversion is not a contradiction
  (B5). The hardest test in the intake cannot be run until the head reads its action.
- **Governance:** GFLAG-0413 (MECH-572) records the refusal-and-build decision and the owed
  adjudications. No claim registered from this intake; candidate formulations 1-3 above remain
  NOT REGISTERED pending the run's autopsy.
