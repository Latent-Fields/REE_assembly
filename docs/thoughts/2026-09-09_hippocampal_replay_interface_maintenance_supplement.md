# Replay-Dependent Maintenance of Cross-System Access

**Status:** adversarial literature supplement; no scientific claim registration, promotion, experiment implementation, or queue action.

**Parent:** [Hippocampal campaign adjudication](2026-09-09_hippocampal_campaign_adjudication.md)

**Existing tranches read:** [biology campaign map](../../evidence/planning/hippocampal_translation_maps_biology_campaign_20260909.md), [literature tranche 1](../../evidence/planning/hippocampal_translation_maps_literature_tranche_1.md), and [CA1 transformation tranche](../../evidence/planning/hippocampal_translation_maps_literature_tranche_2_ca1_transformation.md).

## Bottom line

No located biological study establishes the complete causal chain in the target question:

> after a sender and/or receiver representation changes while each system retains its own information and competence, correctly paired replay repairs the correspondence and thereby restores the receiver's causal use of sender information.

The literature contains strong pieces of this chain, but they do not close it in one experiment. Multi-area studies establish coordinated replay or low-dimensional communication structure without controlled drift and replay perturbation. Replay interventions establish content or timing dependence, but their outcomes are memory formation, local map stability, or recognition itself; local memory quality is therefore not held intact. Drift studies establish stable geometry or successful readout despite unstable units, but do not manipulate replay. Káli and Dayan explicitly model correspondence refresh, yet their ordinary cortical-learning-on-replay mechanism also rescues recall, and the model supplies the hippocampal reinstatement operation rather than deriving it biologically.[^1]

The strongest present conclusion is therefore **design-generative, not evidential**: interface repair is a live mechanism that deserves a discriminating assay, not a completed biological claim. No study located genuinely discriminates interface repair from consolidation under matched local-memory quality.

## What would count as a completed chain

The chain is considered complete only if one experiment or tightly integrated experimental series satisfies all six gates:

1. **Measured change:** the sender code, receiver code, or their effective mapping changes longitudinally; apparent change is not only neuron turnover, registration noise, behavior, or a coordinate rotation that preserves the receiver-potent subspace.
2. **Local preservation:** sender information and sender-local use remain intact; receiver-local memory/competence also remains intact before the cross-system test.
3. **Access loss:** the representation change specifically reduces receiver use of sender information. A stale cross-system readout, not poor memory, must be the limiting variable.
4. **Pair-specific maintenance:** replay presents the correct sender–receiver episode correspondence. A within-context permutation preserves event count, state occupancy, marginal content, firing, and plasticity opportunity but breaks only pairing.
5. **Causal restoration:** correct pairing restores a receiver-dependent behavior or computation on held-out episodes; decoding, correlation, or receiver activation alone is insufficient.
6. **Rival exclusion:** the rescue exceeds local Hebbian/homeostatic readout adaptation, ordinary rehearsal/cortical completion, stable-subspace alignment, and nonspecific timing/plasticity effects at matched budgets.

This criterion intentionally rejects an additive proof assembled from unrelated preparations. Adjacent findings can justify an assay component; they cannot be called a completed biological chain.

## Model-assumption audit

### Káli–Dayan: correspondence maintenance is explicit, but not uniquely necessary

Káli and Dayan's neocortical model contains three 100-unit binary feature areas connected through a 100-unit medial-temporal neocortical (MTNC) layer. Local cleanup memories in the feature areas are hard-coded; cortex is a probabilistic generative network trained with contrastive-divergence-like learning. The hippocampus is not implemented as a neural network. It is an assumed store that recognizes a sufficiently similar MTNC pattern and reinstates an exact stored MTNC pattern; the relevant hippocampal traces are nondecaying in the maintenance simulations.[^1]

Continued semantic learning changes the MTNC representation of old cortical content. The old episode can therefore remain perfectly present in the assumed hippocampal store while the route from current cortical cues to that trace, and from the trace back to current cortical codes, degrades. The model tests recall by clamping two feature-area patterns and asking whether the third is completed. This is a real functional-readout criterion inside the model, but it is not a separately measured biological receiver behavior.

Two distinct maintenance operations rescue recall:

- **Ordinary cortical learning on replay:** replayed episodes continue to train the cortical generative model, tending to hold their MTNC representations fixed. This is rehearsal/consolidation.
- **Hippocampus–MTNC correspondence refresh:** the stored trace reconstructs lower cortical content; the current feed-forward cortical mapping generates an updated MTNC pattern; that new pattern is associated with the same hippocampal episode. This is the closest formal precursor of interface/index repair.

Either operation can maintain episodic recall in the reported simulations, and combining them produces no clear extra benefit. For semantic memory, cortical learning on replay is more important. The work does not include marginal-matched wrong pairings, replay-timing perturbations, a receiver-local adaptation competitor, or a local-memory-equalized biological transfer task. Frequent refresh is assumed; elsewhere in the same paper, transfer required replay to greatly outnumber new experience. Thus the paper verifies that correspondence refresh is computationally coherent, but it does not show that replay-dependent interface repair is biologically used or distinguish it from rehearsal.[^1]

### Rule–O'Leary: a serious local rival, under restrictive conditions

Rule and O'Leary model a redundant population encoding a low-dimensional continuous variable with overlapping tuning functions that continue to tile the variable as individual tuning drifts. Drift is gradual and generated through changing encoder parameters while average population geometry and information remain usable. A downstream linear–nonlinear unit is initialized on the original code.[^2]

The local repair rule has no episode labels and no external teaching signal. It combines a fixed homeostatic target for the readout's initial output mean/variance with Hebbian weight change driven by presynaptic activity and the postsynaptic output; weight decay is gated by homeostatic error. The authors explicitly describe this coupling as an ansatz requiring physiological confirmation. Updates are much faster than drift: simulations repeatedly sample the encoded variable and apply many repair iterations between small drift increments. When maintenance is too infrequent, the rule fails.

Hebbian homeostasis alone extends readout life but can eventually corrupt tuning or permit preference swaps. The more durable variants add response normalization and/or a stable recurrent predictive model that supplies covariance structure. Those variants assume that recurrent structure is fixed or changes much more slowly than the feed-forward representation, and that it can be reactivated by rehearsal or replay. The origin and long-term updating of that internal model are left open.[^2]

Rule–O'Leary is therefore not a demonstration that generic local plasticity solves arbitrary cross-system drift. It assumes a stable task variable, redundancy, smooth incremental drift, a stable receiver, frequent sampling, and a suitable homeostatic or predictive target. It does, however, define the strongest executable rival to assay B: a receiver can self-repair its readout from local activity statistics without seeing paired sender–receiver episode identities. Micou and O'Leary strengthen this rival normatively by showing that heavy-tailed, sparse tuning jumps can make unsupervised readout correction easier, while also emphasizing the fundamental ambiguity between a changing code and a changing world.[^3]

## Focused evidence matrix

**Access key:** FT = full primary text inspected in this pass; AM = author manuscript; ABS = primary abstract/metadata only in this pass; PRE = non-peer-reviewed preprint. “Local control” means direct evidence that information or competence inside the putative sender and receiver remained intact, not merely matched stimulation or baseline behavior.

| Study | Perturbation | Sender → receiver | Representational change | Replay content, pairing, or timing | Local-memory controls | Functional transfer / actual receiver use | Strongest live alternative | Access / chain verdict |
|---|---|---|---|---|---|---|---|---|
| Káli & Dayan 2004[^1] | In-silico continued semantic learning; replay mechanisms toggled | Assumed hippocampal index ↔ MTNC ↔ cortical feature areas | Yes: cortical learning shifts MTNC codes while hippocampal trace is retained | Correct stored episodes replayed; mapping refresh and cortical learning separable; no wrong-pair or timing control | Feature patterns and hippocampal traces stipulated intact | Pattern completion of a missing cortical feature area | Ordinary cortical learning on replay rescues too | FT/AM. **Mechanistic model only; partial chain, no biological discrimination.** |
| Rule & O'Leary 2022[^2] | Simulated gradual encoder drift; local plasticity rules toggled | Drifting encoding population → stable readout | Yes, with preserved low-dimensional variable and redundant coverage | No cross-system episode pairing; local rehearsal/reactivation may drive adaptation | Local information preserved by construction | Readout tuning stability in simulation | Homeostatic/Hebbian self-repair, normalization, stable recurrent predictor | FT. **Executable rival, not replay-interface evidence.** |
| Micou & O'Leary 2026[^3] | Normative adaptive decoder across Gaussian vs heavy-tailed drift; reanalysis of PPC/V1 data | Drifting population → ideal adaptive decoder | Yes in model and existing single-area data | No replay manipulation | Stimulus statistics and decoder assumptions, not two-system local competence | Decoder accuracy only | Drift statistics themselves permit unsupervised repair | FT. **Upper-bound rival; authors do not claim physiological algorithm.** |
| Gonzalez et al. 2026[^4] | Observational simultaneous recording and subspace analysis across behavior/sleep | DG/CA3/CA2/CA1 → RSC, with partialled multi-area relationships | Task/state recombination; not chronic controlled drift | Natural replay covaries with reactivation of some task-defined hippocampal subspaces; CA1–RSC relation is not uniformly positive | No induced access loss; task performance is not a matched local-memory control | Communication-subspace information/correlation, not causal receiver use | Stable, reusable low-dimensional subspaces; plasticity–stability balance | FT. **Strong multi-area adjacency; missing longitudinal drift and replay perturbation.** |
| Ji & Wilson 2007[^5] | None | Hippocampus ↔ visual cortex | Pre/post experience correlations, not drift | Coordinated same-experience replay in slow-wave sleep | No | No behavior or receiver perturbation | Common-state coordination; consolidation | ABS in this pass. **Pairing observation only.** |
| Ólafsdóttir et al. 2016[^6] | None | CA1 → deep MEC | No longitudinal drift | Spatially coherent replay; MEC lagged CA1 by about 11 ms, strongest in forward/direction-modulated events | No | No | Common input or state-dependent coupling | AM. **Direction/timing observation only.** |
| Berners-Lee, Wu & Foster 2021[^7] | None; shuffle analyses preserve event statistics | Hippocampus → PFC | No longitudinal drift | PFC units are selective for replayed arms; arm-label shuffles test content specificity | No separate local-memory preservation test | PFC activity predicts later choice, but PFC replay response is not causally shown to drive it | Replay reports past state or common task variable; PFC correlation without use | FT. **Best content-to-receiver-to-behavior adjacency; no causal replay/drift test.** |
| Rothschild et al. 2017[^8] | Sound presentations bias cortical activity; natural sleep events analyzed | Auditory cortex → hippocampus → auditory cortex | No controlled drift | Sensory cortical activation precedes and follows hippocampal SWRs; cues alter loop content | No | No | Sensory reactivation and consolidation loop | ABS plus prior-tranche extraction. **Closed-loop anatomy/content, not repair.** |
| Maingret et al. 2016[^9] | Closed-loop cortical stimulation immediately after hippocampal SWR vs 160–240 ms delayed stimulation | Hippocampus → neocortical delta/spindle network, including mPFC | No drift | Timing manipulated with the same number of stimulations; content/pair identity not manipulated | Sleep architecture and stimulation efficacy matched; memory strength is the outcome, not held intact | Next-day object-location memory and mPFC reorganization | Ordinary consolidation through plasticity-window alignment | FT/AM. **Strong timing causality; does not distinguish interface repair.** |
| Geva-Sagiv et al. 2023[^10] | Human closed-loop prefrontal stimulation phase-locked vs not phase-locked to MTL slow-wave upstates | MTL/thalamocortical network → prefrontal stimulation site | No drift | Timing/phase locked; no episode-pair manipulation | Same stimulation without precise phase locking; local memory not held | Recognition accuracy improves with correct locking | Systems consolidation and global excitability/coordination | FT institutional record. **Human timing causality; no interface-specific test.** |
| Gridchyn et al. 2020[^11] | Online disruption of sleep reactivation decoded as one of two learned environments | Hippocampal assemblies; no independently assayed receiver | Place-map destabilization follows manipulation, rather than being controlled away | Strong environment-specific content selection; not sender–receiver pair permutation | Other environment is within-animal control; targeted local hippocampal map/memory is altered | Environment-specific later memory deficit | Content-specific consolidation/local map stabilization | ABS in this pass. **Strong content causality, but violates local-preservation gate.** |
| Clawson et al. 2021[^12] | Sleep-wide optogenetic inhibition or activation of learning-recruited V1 neurons | Local V1 ensemble; cross-system sender not identified | Orientation tuning can be shifted; no natural longitudinal drift test | Reactivation is cell-ensemble-specific, not paired interareal replay | Generalized freezing/gist can remain while cue discrimination changes | Cue-specific fear discrimination and induced perceptual behavior | Local cortical rehearsal/completion | FT. **Powerful local-rehearsal rival; not cross-system interface repair.** |
| Deceuninck & Kloosterman 2024[^13] | Closed-loop awake-SWR disruption vs delayed stimulation/no stimulation in three repeated-acquisition tasks | Hippocampal SWR-associated activity; receiver not recorded | No drift | Ripple timing disrupted; replay content is not directly decoded or selectively mismatched | Detection efficacy, behavior, ripple rate/location controlled; tasks remain hippocampus-dependent by prior evidence | No effect on immediate or within-session spatial-memory behavior | Ordinary online/theta processing; long-term rather than immediate replay function | FT. **Causal null; also shows SWR intervention is not content-specific replay intervention.** |
| Kovács et al. 2016[^14] | Optogenetic inhibition of CA1 pyramidal cells during sleep/rest SWRs vs equal non-coincident light | CA1; cortical receiver not recorded | New CA1 map tested before/after rest | Ripple-locked timing disrupted; no decoded content pairing | Same light dose; local CA1 spatial representation directly measured | No behavioral receiver test; CA1 stability unchanged | Waking SWRs or offline molecular stabilization | FT. **Local-map null; no cross-system result.** |
| Widloski & Foster 2025[^15] | Replay detector independent of ripples/bursts; barrier/reward contingencies changed | CA1 replay; downstream receiver not recorded | Within-task unstable place fields and context remapping | About one quarter of detected replays lacked ripples/bursts; ripple timing depends on decoded replayed location | Spike rate/active-cell matching equalizes replay decoding quality across event classes | No causal transfer test | Replay and ripple are separable; ripple may tag salient content rather than generate replay | FT. **Measurement warning: ripple-triggered perturbation can miss replay and confound event with content.** |
| Keinath et al. 2022[^16] | Longitudinal CA1 imaging across repeated contexts | CA1 population → experimenter decoder | Neuron-level drift with preserved relative context geometry | No replay manipulation | Context information and behavior remain stable | Consistent context readout from geometry; no biological receiver manipulation | Invariant relational geometry makes repair unnecessary | FT. **Strong stable-geometry rival; single-area.** |
| Gallego et al. 2020[^17] | Longitudinal recordings in motor-related cortical areas over months/years | Premotor/M1/somatosensory population → behavior/decoder | Neuron-level turnover and drift | No replay manipulation | Stable reaching behavior and latent dynamics | Stable behavioral decoding from latent dynamics, despite raw-unit decoder decay | Stable latent manifold / changing embedding | FT. **Strong non-hippocampal invariant-subspace precedent.** |
| Rule et al. 2020[^18] | Longitudinal PPC data plus subspace analyses and simulations | PPC population → task-variable readout | Drift in coding and noncoding dimensions | No replay manipulation | Expert behavior and task information stable | Stable task information in an approximately stable subspace | Drift structured around a stable readout-relevant subspace | FT/AM. **Direct stable-readout rival; no replay or second biological receiver.** |
| Peters et al. 2026[^19] | Chronic simultaneous calcium imaging across four dorsal cortical regions | RSP/VIS/SSp/MO network | Yes: 47-day single-neuron drift across regions | No sleep/replay measurement or perturbation | Behavioral signals regressed; early-learning sessions excluded | Stable task behavior and preserved population geometry; no causal interareal receiver-use test | Coordinated orthogonal drift preserves cross-area geometry | FT/PRE. **Closest simultaneous multi-area drift observation; no hippocampus/replay.** |

## Why the biological chain remains open

Three near-bridges fail for different reasons:

- **Interareal replay studies** show that content can propagate or covary across hippocampus, entorhinal, sensory, prefrontal, and retrosplenial networks. They do not establish a previously broken correspondence, because the relevant sender and receiver codes are not tracked through access loss and recovery.
- **Causal replay studies** show that content identity or millisecond timing can matter for later memory. But the later memory, local hippocampal code, or recognition score is the dependent variable. A deficit can therefore be ordinary consolidation, local stabilization, or plasticity gating.
- **Drift/stable-subspace studies** show why an interface-repair mechanism may be unnecessary. Information can remain in an invariant geometry, drift can be coordinated across areas, or a local adaptive readout can track a changing encoder. None tests whether paired replay contributes incremental rescue beyond these mechanisms.

The one paper that explicitly separates correspondence refresh from rehearsal is computational. In Káli–Dayan, both mechanisms rescue, so even the model does not award a unique necessity claim to interface repair.[^1] Maingret and Geva-Sagiv demonstrate timing dependence but do not manipulate pairing; Gridchyn demonstrates content specificity but changes local memory/map quality; Berners-Lee connects replay content to PFC and later behavior without perturbing replay or drift. These studies motivate orthogonal assay factors, not a composite proof.

## Assay B revision: make interface repair earn its name

### Operational variables

Let sender state `x_t` encode item `z`, receiver state `r_t` retain its own task competence, and `A_t` be the cross-system mapping used by the receiver. Drift changes the embedding to `x'_t = D_s x_t`, the receiver's coordinates, or both, while oracle decoding of `z` within each local system remains at criterion.

Define receiver use as a causal contrast on a held-out task:

\[
U = \text{performance(message available)} - \text{performance(message ablated or counterfactually replaced)}.
\]

The primary endpoint is recovery of `U`, not representation similarity, adapter loss, mutual information, or local recall. Pair-specific repair requires the recovery under correctly paired replay to exceed both a marginal-matched pair permutation and the best local self-repair rival.

### Gate 0: prove that the imposed drift creates an interface lesion

Before evaluating maintenance, assay B must reject two benign cases:

1. **Invariant-subspace drift:** a fixed receiver readout still works because drift is confined to a null direction or preserves a stable latent geometry.
2. **Global task loss:** sender information or receiver competence has degraded, so there is no isolated interface problem to repair.

Use three drift probes before the maintenance phase:

- no drift;
- task-relevant, known invertible drift that breaks a frozen cross-system readout;
- magnitude-matched drift restricted to an empirically identified receiver-null subspace.

For the task-relevant drift, require: degraded `U`; intact sender-local decoding/action; intact receiver-local memory/action; and restoration by an oracle inverse adapter. If the oracle cannot restore use, the lesion is not an interface lesion. If null-space drift degrades use, the subspace identification is invalid. If task-relevant drift does not degrade use, stable invariants or endogenous adaptation already win and the replay-repair test should stop.

Sender-only drift should be the first identification case. Receiver-only and joint drift are generalization tests, because joint drift otherwise leaves the locus of repair underdetermined.

### Minimal decisive contrasts

After Gate 0 passes, the smallest interpretable primary set is:

| Arm | Drift | Maintenance information | Purpose |
|---|---|---|---|
| A | none | none | stable ceiling |
| B | relevant drift | none | access-lesion floor |
| C | relevant drift | oracle inverse | verifies recoverability and maximum repair |
| D | relevant drift | correctly paired sender–receiver replay | target mechanism |
| E | relevant drift | within-context permuted pairs, identical marginals/timing | isolates correspondence information |
| F | relevant drift | Rule–O'Leary-faithful receiver-local self-repair | strongest executable rival |
| G | relevant drift | receiver-local ordinary rehearsal/completion | consolidation/completion rival |

The primary attribution contrast is `D > max(E, F, G)` on held-out `U`, with A–C validating the lesion and dynamic range. Do not interpret `D > B` alone: it is compatible with generic replay, more plasticity opportunities, rehearsal, and homeostatic adaptation.

Timing is a second-stage test, run only if correct content pairing first beats the permuted-pair arm. Then compare identical correct pairs delivered inside the receiver's plasticity window versus a temporally shifted window, with total events, inter-event intervals, state occupancy, and stimulation energy matched. A timing effect without pair specificity supports plasticity gating or consolidation, not interface repair.

### Strong executable rival: self-healing receiver

Implement the rival at the same representational interface and give it the same update count and local samples as the paired-replay adapter, but no cross-system episode identity:

1. Initialize the receiver readout on the pre-drift code.
2. Store fixed targets for its pre-drift output mean and variance.
3. During each maintenance opportunity, update receiver weights using only current presynaptic sender activity, the receiver's own output, homeostatic variance error, and error-gated decay, following Rule–O'Leary's local rule.[^2]
4. Add population response normalization as a preregistered stronger version.
5. Add a separate ceiling rival with a fixed recurrent predictive/covariance model learned before drift and reactivated on the same schedule. Label it as an extra stability assumption, not as free local plasticity.
6. Sweep maintenance interval relative to drift rate. Rule–O'Leary's success depends on many small corrections before mismatch becomes large; one abrupt rotation followed by one repair block is not a faithful test.

For joint sender/receiver drift, provide symmetric local adaptation at each endpoint or explicitly declare the receiver fixed. Otherwise a paired adapter receives a structural advantage unrelated to pairing.

### Local-memory controls must be constraints, not explanatory covariates

Before every cross-system evaluation block, require criterion performance on:

- decoding `z` from the sender using a freshly fit local oracle and a sender-local behavioral/readout task;
- receiver-only completion or task execution without the sender message;
- episode/item identity and difficulty distributions matched across maintenance arms;
- equivalent maintenance event count, plastic updates, activation magnitude, and elapsed time.

Titrate or exclude blocks until local measures are equated prospectively. Regressing out unequal local recall after the fact is insufficient because consolidation may already have altered which items remain available.

Receiver use must also be causally localized: ablate or replace the incoming message at test, intervene on the learned adapter, and verify item-specific errors predicted by the induced mapping. A decoder that reads sender content from receiver activity is not enough.

### Strongest falsifier

The strongest falsifier is not “replay disruption has no effect.” It is:

> after a verified interface lesion with intact local information and recoverability, a faithful local self-healing/readout-adaptation arm or ordinary local rehearsal restores held-out receiver use as well as correctly paired replay, within a prespecified equivalence margin and matched update budget.

That result would remove the claimed need for pairwise cross-system correspondence repair even if replay remains helpful for consolidation. A more upstream falsifier is also decisive: if the relevant biological or synthetic drift preserves receiver use through an invariant subspace or coordinated transformation, there is no broken interface for replay to repair.

## Search streams and stopping result

| Stream | Primary-source query families and venues | What was recovered | Stopping result |
|---|---|---|---|
| Explicit correspondence maintenance | “hippocampal replay correspondence maintenance,” “index update cortical representation change,” Káli/Dayan cited work | Káli–Dayan's mapping-refresh mechanism; no biological implementation with matched wrong pairs | Saturated around the named model and its assumptions; biological bridge absent |
| Local readout repair | “representational drift homeostatic Hebbian readout,” “adaptive decoder drift,” PNAS/PLOS/eLife | Rule–O'Leary, Micou–O'Leary, Rule et al. | Strong computational rivals found; physiological tests absent |
| Simultaneous interareal replay | hippocampus–PFC, hippocampus–visual cortex, hippocampus–MEC, hippocampus–RSC; Nature/Neuron/JNeurosci/PMC | Ji–Wilson, Ólafsdóttir, Berners-Lee, Rothschild, Gonzalez | Content/coordination found; no chronic drift × intervention × use study |
| Replay content perturbation | “decoded replay content disruption environment,” Cell/Neuron/PubMed | Gridchyn environment-selective disruption | Content causality found, but local hippocampal map/memory changes |
| Replay timing perturbation | SWR-triggered cortical stimulation, phase-locked human stimulation, delayed controls | Maingret; Geva-Sagiv | Timing causality found; pair identity and local-memory preservation absent |
| Null/negative replay intervention | “SWR disruption no effect,” eLife/PLOS/PMC | Deceuninck–Kloosterman behavioral null; Kovács CA1-map null | Nulls are task/state dependent and generally target SWRs, not decoded replay content |
| Replay measurement boundary | “replay without ripple,” Nature Communications/PMC | Widloski–Foster | Ripple-triggered designs can miss a substantial replay class; intervention target must be decoded content |
| Stable invariant subspaces | longitudinal drift stable geometry/readout; Nature Communications/eLife/Nature Neuroscience/PMC | Keinath, Gallego, Rule et al., Gonzalez | Strong rival class; no replay manipulation |
| Simultaneous multi-area drift | “coordinated representational drift across areas,” bioRxiv/PMC/PubMed | Peters et al. cortex-wide preprint | Chronic multi-area drift found, but no hippocampus, sleep/replay, or causal receiver-use test |
| Cortical completion / rehearsal | learning-activated V1 ensembles, retrosplenial engrams, Science/Neuron/Nature Communications | Clawson and adjacent cortical-engram work | Local reactivation can drive or preserve content; no pairwise cross-system repair isolation |

The search was stopped when additional queries repeatedly returned the same three disconnected families—interareal replay without drift, replay intervention with memory as outcome, and drift stability without replay—rather than a study crossing the gates. This is a negative search conclusion, not proof that no such paper exists.

## Unresolved debts

1. **Exact biological bridge:** locate or run a longitudinal sender–receiver recording that tracks both representational changes, directly measures preserved local competence, perturbs decoded pair identity, and tests receiver-dependent behavior.
2. **Replay target validity:** determine whether closed-loop SWR interventions actually capture the relevant replay class. Ripple-less replay makes SWR onset an incomplete proxy.[^15]
3. **Receiver locus:** establish whether observed cortical activation during hippocampal replay changes a readout used later, rather than merely co-reactivating a memory or reflecting common input.
4. **Pair identity:** develop a within-context permutation that preserves replay marginals and physiological timing while selectively breaking which sender event is paired with which receiver state.
5. **Local-memory equivalence:** validate independent sender-local and receiver-local tasks at the exact post-maintenance time point, prospectively equated across arms.
6. **Natural drift geometry:** measure whether the biological drift actually enters the receiver-potent subspace. Unit instability alone is inadequate.
7. **Adaptation timescale:** map drift rate against replay/update interval; local adaptation models are favored by incremental drift and frequent rehearsal.
8. **World-change ambiguity:** separate code drift from real changes in latent cause. A local adaptive decoder can otherwise “repair” a truthful update away.[^3]
9. **Joint drift:** test sender-only first, then receiver-only and joint changes with symmetric local rivals; otherwise correspondence repair and endpoint stabilization remain confounded.
10. **Negative-result scope:** replay interventions need positive controls for disruption efficacy and an explicit statement of which replay classes, states, and timescales remain untouched.

## Sources

[^1]: Káli, S., & Dayan, P. (2004). “Off-line replay maintains declarative memories in a model of hippocampal-neocortical interactions.” *Nature Neuroscience*. [Author-hosted paper and abstract](https://www.gatsby.ucl.ac.uk/~dayan/papers/kd04.html). [DOI](https://doi.org/10.1038/nn1202).
[^2]: Rule, M. E., & O'Leary, T. (2022). “Self-healing codes: How stable neural populations can track continually reconfiguring neural representations.” *PNAS*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8851551/). [DOI](https://doi.org/10.1073/pnas.2106692119).
[^3]: Micou, C., & O'Leary, T. (2026). “Statistics of cortical representational drift can enable robust readout.” *PLOS Computational Biology*. [Full text](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014297). [DOI](https://doi.org/10.1371/journal.pcbi.1014297).
[^4]: Gonzalez, J., et al. (2026). “Subspace communication in the hippocampal–retrosplenial axis.” *Nature*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13317024/). [DOI](https://doi.org/10.1038/s41586-026-10481-z).
[^5]: Ji, D., & Wilson, M. A. (2007). “Coordinated memory replay in the visual cortex and hippocampus during sleep.” *Nature Neuroscience*. [Publisher page](https://www.nature.com/articles/nn1825). [DOI](https://doi.org/10.1038/nn1825).
[^6]: Ólafsdóttir, H. F., Carpenter, F., & Barry, C. (2016). “Coordinated grid and place cell replay during rest.” *Nature Neuroscience*. [Accepted manuscript](https://discovery.ucl.ac.uk/1478267/3/Olafsdottir_et_al_2016%20Co-ordinated%20grid.pdf). [DOI](https://doi.org/10.1038/nn.4291).
[^7]: Berners-Lee, A., Wu, X., & Foster, D. J. (2021). “Prefrontal cortical neurons are selective for non-local hippocampal representations during replay and behavior.” *Journal of Neuroscience*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8265798/). [DOI](https://doi.org/10.1523/JNEUROSCI.1158-20.2021).
[^8]: Rothschild, G., Eban, E., & Frank, L. M. (2017). “A cortical–hippocampal–cortical loop of information processing during memory consolidation.” *Nature Neuroscience*. [DOI](https://doi.org/10.1038/nn.4457).
[^9]: Maingret, N., Girardeau, G., Todorova, R., Goutierre, M., & Zugaro, M. (2016). “Hippocampo-cortical coupling mediates memory consolidation during sleep.” *Nature Neuroscience*. [Author manuscript](https://girardeaulab.org/wp-content/uploads/2018/08/Maingret2016.pdf). [DOI](https://doi.org/10.1038/nn.4304).
[^10]: Geva-Sagiv, M., et al. (2023). “Augmenting hippocampal–prefrontal neuronal synchrony during sleep enhances memory consolidation in humans.” *Nature Neuroscience*. [Institutional record](https://escholarship.org/uc/item/1hm3t82s). [DOI](https://doi.org/10.1038/s41593-023-01324-5).
[^11]: Gridchyn, I., Schoenenberger, P., O'Neill, J., & Csicsvari, J. (2020). “Assembly-specific disruption of hippocampal replay leads to selective memory deficit.” *Neuron*. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/32070475/). [DOI](https://doi.org/10.1016/j.neuron.2020.01.021).
[^12]: Clawson, B. C., et al. (2021). “Causal role for sleep-dependent reactivation of learning-activated sensory ensembles for fear memory consolidation.” *Nature Communications*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7900186/). [DOI](https://doi.org/10.1038/s41467-021-21471-2).
[^13]: Deceuninck, L., & Kloosterman, F. (2024). “Disruption of awake sharp-wave ripples does not affect memorization of locations in repeated-acquisition spatial memory tasks.” *eLife*. [Full text](https://elifesciences.org/articles/84004). [DOI](https://doi.org/10.7554/eLife.84004).
[^14]: Kovács, K. A., et al. (2016). “Optogenetically blocking sharp wave ripple events in sleep does not interfere with the formation of stable spatial representation in the CA1 area of the hippocampus.” *PLOS ONE*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5070819/). [DOI](https://doi.org/10.1371/journal.pone.0164675).
[^15]: Widloski, J., & Foster, D. J. (2025). “Replay without sharp wave ripples in a spatial memory task.” *Nature Communications*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12639102/). [DOI](https://doi.org/10.1038/s41467-025-65181-5).
[^16]: Keinath, A. T., Mosser, C.-A., & Brandon, M. P. (2022). “The representation of context in mouse hippocampus is preserved despite neural drift.” *Nature Communications*. [Full text](https://www.nature.com/articles/s41467-022-30198-7). [DOI](https://doi.org/10.1038/s41467-022-30198-7).
[^17]: Gallego, J. A., et al. (2020). “Long-term stability of cortical population dynamics underlying consistent behavior.” *Nature Neuroscience*. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7007364/). [DOI](https://doi.org/10.1038/s41593-019-0555-4).
[^18]: Rule, M. E., et al. (2020). “Stable task information from an unstable neural population.” *eLife*. [Full text](https://elifesciences.org/articles/51121). [DOI](https://doi.org/10.7554/eLife.51121).
[^19]: Peters, R., et al. (2026). “Coordinated Representational Drift Across the Mouse Cortex.” *bioRxiv* preprint. [Full text](https://www.biorxiv.org/content/10.64898/2026.05.05.723038v1). [DOI](https://doi.org/10.64898/2026.05.05.723038).
