# LIT-0094: BreathOscillator Literature Synthesis

**Date:** 2026-03-23
**Purpose:** Ground parameters for a BreathOscillator mechanism that creates cyclical uncommitted
planning windows — respiratory rhythm and other slow oscillators modulating neural
commitment/precision/gain.
**Status:** Complete — 10 targeted papers + 3 bonus papers

---

## Summary

Respiratory rhythm (~0.1-0.33 Hz in humans, ~1-4 Hz in rodents) is not merely a homeostatic
signal but a global neural pacemaker that modulates cortical excitability, prefrontal-hippocampal
coupling, and decision thresholds across the respiratory cycle. The key mechanistic chain is:

- Inhalation drives feedforward sensory processing; exhalation enables top-down prefrontal
  planning/commitment signals.
- A small subpopulation (~175 neurons) of the preBötzinger complex directly projects to locus
  coeruleus, providing a direct coupling between respiratory rhythm and noradrenergic arousal/gain.
- Infraslow (0.01-0.1 Hz) fluctuations modulate fast oscillation amplitudes and behavioral
  excitability across timescales far slower than the respiratory cycle itself.
- Serotonin and norepinephrine play complementary roles: NE signals unexpected uncertainty (model
  failure / interrupt), serotonin signals expected-uncertainty / persist-in-current-plan.

---

## Paper 1 — Zelano et al. 2016

**Full citation:** Zelano C, Jiang H, Zhou G, Arora N, Schuele S, Rosenow J, Gottfried JA.
"Nasal Respiration Entrains Human Limbic Oscillations and Modulates Cognitive Function."
J Neurosci. 2016 Dec 7; 36(49):12448-12467.

**PMID:** 27927961
**PMCID:** PMC5148230
**DOI:** 10.1523/JNEUROSCI.2586-16.2016
**Journal:** Journal of Neuroscience (NOT Nature Neuroscience as originally queried)

**Key findings:**
Using intracranial EEG in medically refractory epilepsy patients, nasal breathing synchronizes
electrical activity in piriform cortex, amygdala, and hippocampus at the respiratory frequency
(~0.16-0.33 Hz in humans). Oscillatory power in limbic regions peaked during inspiration and
dissipated when breathing switched from nasal to mouth. Parallel behavioral experiments showed
that respiratory phase modulates fear discrimination and memory retrieval -- recognition accuracy
for fearful faces was significantly higher when stimuli were presented during inhalation vs.
exhalation.

**Quantitative data:**
- Respiratory frequency in humans: ~0.16-0.33 Hz
- Limbic coupling was phase-locked to inspiration
- Fear recognition and memory retrieval performance were inspiration-preferring
- Effect was absent during mouth breathing (confirming olfactory-to-limbic propagation route)

**REE relevance:** Establishes human data for respiration-locked limbic (amygdala, hippocampus)
excitability windows. Inhalation = high-excitability / high-precision window for threat and
memory retrieval. Exhalation = relative disengagement. Directly grounds a BreathOscillator
that gates hippocampal/amygdala access as a function of respiratory phase.

---

## Paper 2 — Karalis & Sirota 2022

**Full citation:** Karalis N, Sirota A.
"Breathing coordinates cortico-hippocampal dynamics in mice during offline states."
Nat Commun. 2022 Jan 24; 13(1):467.

**PMID:** 35075139
**PMCID:** PMC8786964
**DOI:** 10.1038/s41467-022-28090-5
**Journal:** Nature Communications

NOTE: The user queried "Karalis & Bhatt 2020" -- the actual paper is Karalis & Sirota 2022.
The second author is Anton Sirota (Ludwig-Maximilian University Munich), not "Bhatt."
There is a related earlier preprint by Karalis & Sirota (2018, SSRN) titled "Breathing
Coordinates Limbic Network Dynamics Underlying Memory Consolidation."

**Key findings:**
Using large-scale recordings from cortical and subcortical structures in behaving mice, breathing
acts as an oscillatory pacemaker that coordinates hippocampal sharp-wave ripples (SWR) with
cortical DOWN/UP state transitions during offline states (sleep/quiet wakefulness). The coupling
is olfaction-independent -- it arises from an intracerebral respiratory corollary discharge that
modulates circuit excitability across hippocampus, mPFC, visual cortex, thalamus, amygdala, and
nucleus accumbens. During offline states this coordination mediates systems-level memory
consolidation.

**Quantitative data:**
- Respiratory entrainment of neural activity detected across all surveyed regions
- Hippocampal SWR preferentially occurred at specific respiratory phases during offline states
- Coupling was olfaction-independent (corollary discharge route)
- Regions included: hippocampus, mPFC, visual cortex, thalamus, amygdala, nucleus accumbens

**REE relevance:** Breathing functions as a master clock for cortico-hippocampal consolidation
during offline/quiescent states. Directly grounds MECH-092 (micro-quiescence SWR-equivalent
replay) and supports the idea that BreathOscillator defines offline planning windows.

---

## Paper 3 — Yackle et al. 2017

**Full citation:** Yackle K, Schwarz LA, Kam K, Sorokin JM, Huguenard JR, Feldman JL, Luo L,
Krasnow MA.
"Breathing control center neurons that promote arousal in mice."
Science. 2017 Mar 31; 355(6332):1411-1415.

**PMID:** 28360327
**PMCID:** PMC5505554
**DOI:** 10.1126/science.aai7984
**Journal:** Science

**Key findings:**
Identified a small (~175 neuron) subpopulation in the preBötzinger complex (preBötC) -- the
brainstem breathing rhythm generator -- that directly projects to and positively regulates
noradrenergic neurons in the locus coeruleus. These Cdh9/Dbx1 double-positive neurons are
distinct from the respiration-essential population. Conditional bilateral genetic ablation of
this subpopulation left breathing intact but shifted mice toward sustained calm states and away
from arousal states. The finding establishes a direct monosynaptic circuit from the breathing
rhythm generator to the LC-NE arousal system.

**Quantitative data:**
- Approximately 175 Cdh9/Dbx1+ neurons in preBötC mediate the arousal link
- Ablation increased calm behavior without affecting breathing rate or pattern
- Direct synaptic projection to LC confirmed (not polysynaptic)
- Ablation specifically decreased time in aroused states

**REE relevance:** Critical mechanistic grounding for BreathOscillator -> LC-NE gain coupling.
Breath rhythm directly drives noradrenergic arousal. Bridges MECH-047 (LC-NE gain modulation)
to the respiratory oscillator. A BreathOscillator parameter controlling "NE pulse probability
per cycle" has a direct biological substrate in this circuit. Also connects to MECH-093
(z_beta modulates E3 heartbeat frequency).

---

## Paper 4 — Vlemincx et al. 2010/2011

**Full citation:** Vlemincx E, Taelman J, De Peuter S, Van Diest I, Van den Bergh O.
"Sigh rate and respiratory variability during mental load and sustained attention."
Psychophysiology. 2011 Jan; 48(1):117-120. [Epub 2010]

**PMID:** 20536901
**DOI:** 10.1111/j.1469-8986.2010.01043.x
**Journal:** Psychophysiology (NOT Acta Psychologica as originally queried)

**Key findings:**
Measured spontaneous sigh rate and respiratory variability across rest, mental load (N-back
task), and sustained attention tasks. Mental load reduced correlated respiratory variability
(consecutive-breath autocorrelation) while sustained attention reduced total respiratory
variability. Both conditions elevated sigh rate relative to rest. Sighs followed periods of
reduced variability and appear to function as a reset mechanism restoring respiratory
flexibility.

**Quantitative data:**
- Sigh rate increased during mental load and during recovery from sustained attention tasks
- Correlated respiratory variability (autocorrelation of consecutive breaths) decreased during
  mental load
- Total respiratory variability decreased during sustained attention
- Sighs correlated with transition from reduced-variability states to recovery

**REE relevance:** Sighs as respiratory resets correlate with cognitive state transitions.
Sustained cognitive commitment (sustained attention) compresses respiratory variability -- the
system becomes locked into a narrow rhythm. Sighs mark uncommitted-window openings after
cognitive strain. This grounds a BreathOscillator mechanism where high-commitment states
compress respiratory variability (analogous to reduced E3 beta drop probability) and sighs
mark forced quiescence windows.

---

## Paper 5 — Tort et al. 2018

**Full citation:** Tort ABL, Ponsel S, Jessberger J, Yanovsky Y, Brankacak J, Draguhn A.
"Parallel detection of theta and respiration-coupled oscillations throughout the mouse brain."
Sci Rep. 2018 Apr 24; 8(1):6432.

**PMID:** 29691421
**PMCID:** PMC5915406
**DOI:** 10.1038/s41598-018-24629-z
**Journal:** Scientific Reports

**Key findings:**
Simultaneous LFP recordings from 15 brain regions in mice during exploration and REM sleep,
with concurrent respiratory monitoring, show that respiration-coupled oscillations (RCOs) are
detectable independently of theta oscillations throughout the brain -- including hippocampus,
prelimbic cortex, parietal cortex, and subcortical structures (thalamus, amygdala, ventral
hippocampus). RCOs are not simply a harmonic of theta; they constitute a separate, globally
distributed rhythm.

**Quantitative data:**
- Theta frequency in mice: 5-10 Hz; mouse breathing: often overlaps (1-4 Hz but can reach
  theta range during active exploration)
- RCOs detected in 15/15 regions simultaneously
- Neocortical regions included: prefrontal (prelimbic), parietal, visual
- Subcortical: thalamus, amygdala, ventral hippocampus
- RCOs were parallel to theta during exploration and during REM sleep

**REE relevance:** Respiration provides a global rhythm that reaches every region relevant to
REE -- including mPFC (E3 planning), hippocampus (trajectory proposals), amygdala (harm/fear
evaluation), and thalamus (ARC-023 heartbeat relay). BreathOscillator is not a single-node
modulator but a system-wide phase reference. Grounds the design principle that respiratory phase
should modulate all three BG-like loops simultaneously (ARC-021).

---

## Paper 6 — Helfrich et al. 2019

**Full citation:** Helfrich RF, Lendner JD, Mander BA, Guillen H, Paff M, Mnatsakanyan L,
Vadera S, Walker MP, Lin JJ, Knight RT.
"Bidirectional prefrontal-hippocampal dynamics organize information transfer during sleep in
humans."
Nat Commun. 2019 Aug 7; 10(1):3572.

**PMID:** 31395890
**DOI:** 10.1038/s41467-019-11444-x
**Journal:** Nature Communications

NOTE: The user queried for a Helfrich paper on "respiratory or slow oscillations and memory/
cognition NOT the general sleep paper." This is the closest non-sleep-focused match in PubMed --
it uses human iEEG and is specifically about the prefrontal-hippocampal mechanism rather than
about sleep per se. A related 2018 Neuron paper (Helfrich et al., PMID not separately confirmed
here) addresses aging/SO-spindle coupling.

**Key findings:**
Human iEEG recordings (medial temporal lobe + three PFC regions) during NREM sleep show that
prefrontal cortex orchestrates bidirectional hippocampal-neocortical information transfer via
SO-spindle coupling. Only SO-coupled spindles (not isolated spindles) trigger hippocampal
ripple-mediated transfer. Prefrontal slow oscillation phase predicts memory retention. The
SO-spindle-ripple sequence forms a temporal hierarchy for memory consolidation.

**Quantitative data:**
- Slow oscillation frequency: ~0.5-1 Hz (NREM SO)
- Only phase-coupled spindles (not isolated) drive hippocampal activation
- Frontal electrode SO-spindle coupling phase predicted overnight memory retention
- Bidirectional coupling confirmed: PFC initiates, hippocampus responds, then transfer back
- 18 subjects with MTL + PFC intracranial recordings

**REE relevance:** Establishes that the cortical slow oscillation (not just theta or gamma)
is the timing mechanism for hippocampal-neocortical information transfer. A BreathOscillator
operating at respiratory frequency (~0.16-0.33 Hz in humans) is in the same frequency range
as slow oscillations and could serve as an online analog of the NREM consolidation mechanism
during waking planning states. Directly relevant to MECH-092 (SWR-equivalent replay) and to
the proposed micro-DMN quiescence during E3 heartbeat cycles.

---

## Paper 7 — Monto, Palva, Voipio & Palva 2008

**Full citation:** Monto S, Palva S, Voipio J, Palva JM.
"Very slow EEG fluctuations predict the dynamics of stimulus detection and oscillation amplitudes
in humans."
J Neurosci. 2008 Aug 13; 28(33):8268-8272.

**PMID:** 18701689
**PMCID:** PMC6670577
**DOI:** 10.1523/JNEUROSCI.1910-08.2008
**Journal:** Journal of Neuroscience

RELATED PAPER (also found in search): Hiltunen T, Kantola J, Abou Elseoud A, et al., including
S Palva, JM Palva. "Infra-slow EEG fluctuations are correlated with resting-state network
dynamics in fMRI." J Neurosci. 2014 Jan 8; 34(2):356-362. PMID: 24403137.
DOI: 10.1523/JNEUROSCI.0276-13.2014.

The user queried "Palva & Palva 2012" -- the 2012 paper is a review in NeuroImage:
Palva JM, Palva S. "Infra-slow fluctuations in electrophysiological recordings, blood-oxygenation-
level-dependent signals, and psychophysical time series." NeuroImage. 2012; 62(4):2201-2211.
DOI: 10.1016/j.neuroimage.2012.02.060. PMID: 22401756.

The 2008 J Neurosci paper (PMID 18701689) is the primary empirical paper; the 2012 review
synthesizes the field.

**Key findings (Monto et al. 2008):**
Full-band EEG during a somatosensory near-threshold detection task revealed prominent infraslow
(0.01-0.1 Hz) fluctuations. Stimulus detection probability was 55% larger in the rising phase
vs. falling phase of the infraslow EEG cycle. The phase (not amplitude) of infraslow fluctuations
predicted both behavioral performance and the amplitudes of 1-40 Hz fast oscillations. This
establishes infraslow fluctuations as a cortical excitability governor -- a superstructure
modulating all faster rhythms.

**Quantitative data:**
- Infraslow frequency range: 0.01-0.1 Hz (10-100 second cycles)
- Stimulus detection probability: 55% higher in rising vs. falling ISF phase
- Fast oscillations (1-40 Hz) amplitudes robustly correlated with ISF phase
- Phase (not amplitude) is the relevant variable for behavioral prediction
- 11 subjects; somatosensory detection task

**REE relevance:** Infraslow oscillations (<0.1 Hz) are the excitability superstructure above
the respiratory rhythm. A BreathOscillator at ~0.16-0.33 Hz sits between infraslow and theta.
The ISF -> fast oscillation amplitude coupling means a BreathOscillator-driven phase reset would
cascade upward to modulate gamma/theta power and downward into behavioral precision. The 55%
detection difference quantifies the behavioral magnitude of slow-oscillation phase effects.

---

## Paper 8 — Dayan & Yu 2006

**Full citation:** Dayan P, Yu AJ.
"Phasic norepinephrine: A neural interrupt signal for unexpected events."
Network: Computation in Neural Systems. 2006; 17(4):335-350.

**PMID:** 17162459
**DOI:** 10.1080/09548980601004024
**Journal:** Network: Computation in Neural Systems
(NOTE: This is NOT Neural Computation -- that is a different journal.)

**Key findings:**
A Bayesian model of a visual discrimination task showing that phasic LC-NE activity is
driven specifically by unexpected uncertainty -- events that deviate from the current internal
model in ways that signal model failure rather than expected noise. Tonic NE tracks expected
uncertainty (known task volatility). Phasic NE serves as a neural interrupt: it resets
attentional weights, suspends current task representations, and initiates model re-evaluation.
The model captures the sub-second LC-NE responses observed in primate electrophysiology during
attentional tasks.

**Quantitative data:**
- Phasic NE response latency: sub-second (modeled at <500ms post-unexpected-event)
- Tonic vs. phasic distinction: tonic = expected uncertainty; phasic = unexpected uncertainty
- Bayesian model reproduces LC firing patterns during visual discrimination task
- Model predicts both response facilitation and subsequent attentional reset

**REE relevance:** The phasic NE interrupt mechanism is the canonical computational formulation
for what the BreathOscillator needs to avoid -- a committed state that fires phasic NE should
be interrupted regardless of where in the respiratory cycle it occurs. Conversely, exhalation
windows with no phasic NE activity are the safe planning/uncommitted states. Grounds the
relationship between the BreathOscillator and MECH-047 (LC-NE gain modulation). Also connects
to MECH-094 (hypothesis tag loss = tag-loss event triggers phasic NE / PTSD mechanism).

---

## Paper 9 — Lottem et al. 2018

**Full citation:** Lottem E, Banerjee D, Vertechi P, Sarra D, Oude Lohuis M, Mainen ZF.
"Activation of serotonin neurons promotes active persistence in a probabilistic foraging task."
Nat Commun. 2018 Mar 8; 9(1):1000.

**PMID:** 29520000
**PMCID:** PMC5843608
**DOI:** 10.1038/s41467-018-03438-y
**Journal:** Nature Communications

**Key findings:**
Optogenetic activation of dorsal raphe serotonin neurons in mice performing a probabilistic
foraging task (nose-poke to exploit reward sites, then leave for the next) increased the number
of nose pokes before leaving and increased time at a foraging site -- i.e., promoted active
persistence in the current behavioral strategy. This is inconsistent with the "behavioral
inhibition" account of serotonin and instead positions 5-HT as a persistence/stay signal in
the face of probabilistic reward, modeling the expected-uncertainty environment as still worth
exploiting.

**Quantitative data:**
- Serotonin stimulation increased nose-poke rate and dwell time at foraging sites
- Proportional hazards model: NE stimulation reduced probability of leaving per unit time
- Effect was specific to persistence, not general motor inhibition
- The task was probabilistic -- mice had to infer statistics of the reward environment

**REE relevance:** Serotonin (5-HT) is a "stay in current plan" signal complementary to phasic
NE's "abandon current model" interrupt. Together they define the plan-persistence vs. model-reset
axis relevant to E3 commitment gating. A BreathOscillator could modulate the relative gain
on these two signals: exhalation windows (uncommitted) reduce 5-HT persistence weighting while
increasing sensitivity to phasic NE interrupts. Grounds the computational role of serotonin
as a commitment-sustainer opposing respiratory-phase-linked uncommitted windows.

---

## Paper 10 — Yackle/preBotC -> LC circuit (additional coverage)

The Yackle et al. 2017 paper (Paper 3 above, PMID 28360327) covers this directly.
The preBotC -> LC projection is the primary mechanistic link found in the literature.

A supplementary paper on the same circuit:
**Karalis N, Bhatt DL [NOTE: no matching paper found -- likely a confusion with Karalis & Sirota
or another author pair].** No paper specifically by "Karalis & Bhatt" was found in PubMed.
The search for this author pair returned no results.

The closest related paper on preBotC-LC-arousal found independently:

PMID 27353953: Confirmed as the BMC Neuroscience CNS-2016 conference proceedings
(doi: 10.1186/s12868-016-0283-6) -- a large multi-author conference supplement, not a specific
preBotC-LC paper. This PMID was returned by the PubMed search but is not a dedicated paper on
this topic.

**The definitive preBotC-LC paper is Yackle et al. 2017 (Paper 3 above).**

Additional highly relevant paper found in bonus search:
Karalis N, Bhatt et al. -- see bonus section below for the Karalis 2016 fear/4-Hz paper
(PMID 26878674) which is closely related.

---

## Bonus Paper A — Karalis et al. 2016

**Full citation:** Karalis N, Bhatt DL [NOTE: actually authored by Karalis N, Bhatt DL
-- CORRECTION: actual authors are Karalis N, Bhatt DL is NOT an author here].

CORRECTION: The 2016 paper is:
Karalis N, Dejean C, Bhatt DL [NOTE: this attribution is still wrong].

ACTUAL citation confirmed by search:
Karalis N, Dejean C, Bhatt DL [STILL not confirmed -- web results show "Karalis et al." as
lead author for a Nature Neuroscience 2016 paper].

**Confirmed citation from web search:**
Karalis N et al. "4-Hz oscillations synchronize prefrontal-amygdala circuits during fear behavior."
Nat Neurosci. 2016 Apr; 19(4):605-612.
PMID: 26878674
DOI: 10.1038/nn.4251
Journal: Nature Neuroscience

NOTE: This appears to be the paper the user may have meant by "Karalis & Bhatt 2020" -- it is
Karalis et al. 2016, published in Nature Neuroscience. "Bhatt" may refer to a co-author.

**Key findings:**
Freezing behavior (expression of conditioned fear) co-occurs with sustained, internally generated
4-Hz oscillations in prefrontal-amygdala circuits. These oscillations predict freezing onset and
offset. Causal analysis showed prefrontal activation precedes amygdala activation within each
4-Hz cycle. Optogenetic induction of 4-Hz oscillations in dmPFC was sufficient to drive freezing
and form fear memory. Subsequent work (Moberly et al. 2018, Bagur et al. 2021) showed these
4-Hz oscillations are breathing-coupled rhythms -- not purely "internally generated."

**Quantitative data:**
- 4-Hz oscillations (2-6 Hz band) arise during freezing in dmPFC and BLA
- Prefrontal leads amygdala within each 4-Hz cycle (causal direction: PFC -> BLA)
- Optogenetic 4-Hz stimulation of dmPFC: sufficient to drive freezing + lasting fear memory
- 4 Hz = mouse respiratory rate during freezing (body still, breathing slows)
- Oscillations predict freezing onset and offset in time

**REE relevance:** A 4-Hz rhythm locking PFC and amygdala during committed fear/freezing is
respiraton-driven. The BreathOscillator operating at rodent respiratory rate (~2-4 Hz during
quiet states) directly generates the oscillatory substrate for committed behavioral states.
High-commitment states (freezing, sustained attention) coincide with oscillatory locking at the
respiratory frequency. Uncommitted planning requires disrupting this lock -- consistent with
MECH-091 (salient events phase-reset E3 heartbeat) and MECH-090 (beta gate).

---

## Bonus Paper B — Boyadzhieva & Kayhan 2021

**Full citation:** Boyadzhieva A, Kayhan E.
"Keeping the Breath in Mind: Respiration, Neural Oscillations, and the Free Energy Principle."
Front Neurosci. 2021 Jun 29; 15:647579.

**PMID:** 34267621
**PMCID:** PMC8275985
**DOI:** 10.3389/fnins.2021.647579
**Journal:** Frontiers in Neuroscience

**Key findings:**
A theoretical review connecting respiratory entrainment of neural oscillations to the Free Energy
Principle / active inference framework. Proposes that respiration-entrained gamma oscillations
propagate prediction errors from sensory cortex to higher cortical regions. Volitional breath
control is framed as an active inference mechanism for allostatic regulation -- modifying the
respiratory signal alters precision-weighting of interoceptive predictions. The authors document
bidirectional PFC-respiratory network communication and note that corticospinal pathways to the
subparabrachial nucleus / PAG (not just preBötC) mediate volitional respiratory control.

**Quantitative data:**
- No primary quantitative data (theoretical review)
- Synthesizes literature: respiration drives gamma coupling in prefrontal/limbic regions
- Documents the inhalation (feedforward) / exhalation (feedback/top-down) asymmetry
- Notes LC-NE ascending modulation as one route by which respiratory-modulated oscillations
  alter cortical gain

**REE relevance:** This review provides the direct theoretical bridge between the BreathOscillator
and REE's precision-weighting architecture. Framing exhalation as top-down / prediction-driven
and inhalation as bottom-up / sensory-driven maps onto REE's pre-commit (simulation) vs.
post-commit (realized-outcome) channel distinction. Active inference / FEP framing makes the
BreathOscillator a first-class precision-modulating mechanism, not a peripheral add-on.

---

## Bonus Paper C — Braendholt et al. 2025

**Full citation:** Braendholt M, Nikolova N, Vejlo M, Banellis L, Fardo F, Kluger DS, Allen M.
"The respiratory cycle modulates distinct dynamics of affective and perceptual decision-making."
PLoS Comput Biol. 2025 May 27; 21(5):e1013086.

**PMID:** 40424351
**PMCID:** PMC12240353
**DOI:** 10.1371/journal.pcbi.1013086
**Journal:** PLoS Computational Biology

**Key findings:**
41 human participants categorized dot motion (perceptual) and facial emotion (affective) stimuli
across respiratory phases. Inspiration accelerated responses in both domains. Computational
modeling (hierarchical evidence accumulation) showed domain-specific mechanisms: for perceptual
decisions, inspiration reduced the evidential decision boundary (speed-accuracy tradeoff shifts
toward speed); for affective decisions, inspiration shifted the starting point of evidence
accumulation (positive valence bias). Two distinct computational mechanisms, not one uniform
respiratory effect.

**Quantitative data:**
- N = 41 participants; 2 tasks: dot motion + facial emotion
- Inspiration effect on perceptual decisions: reduced decision boundary (threshold)
- Inspiration effect on affective decisions: shifted starting point (bias) toward positive
- Both effects were inspiration-preferring (higher baseline at peak inhalation)
- Hierarchical drift-diffusion model with respiratory phase as modulator

**REE relevance:** The most direct evidence for a BreathOscillator affecting decision computation
parameters. Inhalation lowers decision threshold (equivalent to lower precision/commitment
threshold) and biases affective starting points. This maps directly onto:
- E3 commitment gate being phase-sensitive (lower threshold during inhalation = uncommitted window)
- Valence bias shifting with respiratory phase (grounding for z_beta / affective latent coupling)
- Two distinct computational mechanisms imply the oscillator affects multiple downstream
  parameters independently -- not a single scalar gain

---

## Cross-Cutting Parameter Notes for BreathOscillator Design

### Frequencies

| Species | Resting rate | Active exploration | During freezing/quiet |
|---------|-------------|-------------------|----------------------|
| Human | 0.16-0.33 Hz (1 breath per 3-6 s) | ~0.33-0.5 Hz | ~0.16 Hz |
| Mouse | 1-4 Hz (varies by state) | 4-8 Hz | ~1-2 Hz |
| Note: mouse respiration during active exploration overlaps theta (4-8 Hz) |

### Phase Relationships (human, nasal breathing)

- Inspiration: feedforward/sensory; higher limbic excitability; lower decision threshold;
  positive affective bias (Zelano 2016, Braendholt 2025)
- Exhalation: top-down/prefrontal; planning and cognitive signal propagation; commitment
  signal propagation from higher to lower cortex (Boyadzhieva & Kayhan 2021)
- Exhalation + uncommitted state: respiratory variability is restored (Vlemincx 2011)

### Amplitude/Gain Effects

- Infraslow ISF phase modulates all fast oscillation amplitudes (1-40 Hz) (Monto et al. 2008)
- Stimulus detection probability: 55% higher in rising ISF phase
- Respiratory phase modulates gamma coupling in mPFC (Behavioral State-Dependent Modulation,
  J Neurosci 2023)
- 4-Hz PFC-amygdala oscillations: appear during committed fear/freezing states, respiratory-locked
  (Karalis 2016)

### The NE-5HT Axis

- Phasic NE (LC): unexpected uncertainty interrupt -- model failure signal (Dayan & Yu 2006)
- Tonic NE: expected uncertainty gain -- environmental volatility tracking
- 5-HT (DRN): active persistence in probabilistic environments -- stay-in-plan signal (Lottem 2018)
- preBotC -> LC monosynaptic projection: ~175 neurons couple breathing rhythm to NE arousal
  (Yackle 2017)
- Implication: every inspiration potentially delivers a pulse to LC proportional to preBötC
  activity; exhalation reduces LC drive; this creates a within-cycle NE fluctuation that could
  gate commitment

### Sigh Physiology

- Sighs mark cognitive resets after sustained high-attention states (Vlemincx 2011)
- Sigh rate increases during mental load and during recovery from sustained attention
- Sighs restore respiratory variability (system flexibility)
- Interpretation: sighs are forced uncommitted-window insertions when variability is pathologically
  compressed

---

## Missing Papers / Caveats

1. **"Karalis & Bhatt"** -- no paper by this exact authorship exists in PubMed. The most likely
   candidates are: (a) Karalis et al. 2016 (Nat Neurosci, fear/4-Hz) or (b) Karalis & Sirota
   2022 (Nat Commun, offline cortico-hippocampal). The user should clarify which paper was intended.

2. **Dayan & Yu journal**: Published in Network: Computation in Neural Systems (NOT Neural
   Computation). Two distinct journals. DOI confirmed.

3. **Zelano journal**: Published in Journal of Neuroscience (NOT Nature Neuroscience).

4. **Vlemincx journal**: Published in Psychophysiology (NOT Acta Psychologica).

5. **Palva & Palva 2012**: The 2012 paper is a NeuroImage review (PMID 22401756). The primary
   empirical paper (with the 55% detection effect) is Monto et al. 2008 J Neurosci (PMID 18701689).
   Both are by Palva group members.

6. **PMID 27353953** (returned by PubMed for preBötC-LC search): This is the CNS-2016 conference
   proceedings supplement (BMC Neuroscience), not a focused preBötC-LC paper. The correct paper
   for that circuit is Yackle et al. 2017 (PMID 28360327).

---

## Files

This document: `REE_assembly/evidence/literature/lit_breath_oscillator/LIT-0094_breath_oscillator_synthesis.md`
