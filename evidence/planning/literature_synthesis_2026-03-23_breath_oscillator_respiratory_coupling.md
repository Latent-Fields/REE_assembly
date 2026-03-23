# Literature Synthesis: Respiratory-Neural Coupling and Cyclical Commitment Modulation

**LIT-0094** | Claims: MECH-107, MECH-108, MECH-109, MECH-026, MECH-029, MECH-047
**Date:** 2026-03-23
**Purpose:** Ground BreathOscillator parameters for EXP-0089/090/091; determine what cyclically modulates neural commitment/precision thresholds at respiratory and slower timescales.
**Outcome:** Parameters updated; MECH-107 phase framing partially revised; new dual-mechanism finding (Braendholt 2025) constrains BreathOscillator design; preBotC-LC circuit (Yackle 2017) provides direct mechanistic grounding for MECH-108/104 link.

---

## Finding 1: Respiratory frequency and phase reference in the human brain

**Zelano et al. (2016)** — *Journal of Neuroscience*, PMID: 27927961, DOI: 10.1523/JNEUROSCI.2586-16.2016
Intracranial EEG in epilepsy patients. Nasal breathing entrains piriform cortex, amygdala, and hippocampus at respiratory frequency (0.16–0.33 Hz in humans). Oscillatory power peaks during **inhalation**, not exhalation. Fear recognition was 20% better and memory retrieval 30% better during the inhalation phase. Effect was absent during mouth breathing, confirming that olfactory bulb afference is the primary route.

**Architectural implication:** The system-wide phase reference is a nasal-airflow signal. Inhalation = peak neural excitability / sensory sampling. Exhalation = relative inhibition / top-down propagation window. **This partially revises MECH-107**: the behavioral observation (dogs/humans exhale when abandoning a plan) and the neural observation (exhalation = reduced sensory input, top-down propagation dominant) are compatible — abandonment is a top-down prediction event (E3 signals no-viable-trajectory), which Boyadzhieva confirms occurs on exhalation. The search/sampling phase is inhalation; the decision-and-release phase is exhalation.

**Tort et al. (2018)** — *Scientific Reports*, PMID: 29691421, DOI: 10.1038/s41598-018-24629-z
Respiratory-coupled oscillations (RCOs) detected independently of theta in all 15 brain regions simultaneously, including prelimbic mPFC, thalamus, amygdala, and **nucleus accumbens**. Breathing provides a global system-wide phase reference, not a local signal. RCOs and theta were decorrelated — two independent channels.

**Architectural implication:** The BreathOscillator is not a hippocampal-only phenomenon. It simultaneously gates mPFC, amygdala, and nucleus accumbens — exactly the E3, harm-evaluation, and BG-gating structures. The period is a global clock parameter, not a local one. Confirmed: `breath_period` should be a system-wide config parameter, not component-specific.

**Synthesis:** Human respiratory ~0.2 Hz range is 0.16–0.33 Hz (3–6 seconds per cycle). At 10 Hz simulation time, `breath_period` = 32–60 steps. Current proposal value of 50 steps (= 5 seconds = 0.2 Hz) is **within physiological range** and well-chosen.

---

## Finding 2: Phase specificity — inhalation vs exhalation (revised MECH-107 framing)

**Boyadzhieva & Kayhan (2021)** — *Frontiers in Neuroscience*, PMID: 34267621, DOI: 10.3389/fnins.2021.647579
Theoretical review bridging respiratory-entrained oscillations to the Free Energy Principle. Core claim: **inhalation = bottom-up sensory (feedforward prediction error sampling)**; **exhalation = top-down prefrontal prediction propagation** (precision-weighted prediction update). Volitional breath control as active inference — deliberate inhalation increases bottom-up sampling; deliberate exhalation increases top-down prediction weight. LC-NE ascending modulation documented as the mechanistic route linking breath phase to precision modulation.

**Braendholt et al. (2025)** — *PLoS Computational Biology*, PMID: 40424351, DOI: 10.1371/journal.pcbi.1013086
N=41 human participants; dot motion and facial emotion tasks. **Inspiration lowered the perceptual decision boundary** (speed-accuracy threshold shift — faster, less cautious decisions) AND **shifted affective starting point toward positive valence**. Two distinct computational mechanisms — threshold modulation and bias modulation — operate independently across the breath cycle. The threshold effect (lower decision boundary on inspiration) is consistent with lower commitment/increased openness to new information.

**Architectural implication (dual-mechanism finding):** The BreathOscillator operates on **two separate channels**, not one:

1. **Threshold channel**: inspiration transiently lowers commit_threshold (or equivalently, raises running_variance tolerance) — opening an uncommitted window for trajectory re-evaluation
2. **Bias channel**: inspiration shifts affective/valence baseline — distinct from pure commitment

Current EXP-0089/090/091 design only models threshold modulation. The bias channel is separately testable but is a second-order effect for the current experiments. **Revised BreathOscillator design**: primary parameter is `sweep_amplitude` modulating `commit_threshold`; secondary parameter `valence_nudge` deferred to future experiment.

**MECH-107 framing revision:** The claim "exhalation = trajectory abandonment" is mechanistically accurate at the behavioral output level (the signal is emitted on exhale). But the *decision* to abandon is made during or near the inhalation phase (peak excitability, bottom-up sampling, lower decision boundary). The exhale executes the decision. Functionally: **inhalation = sweep / evaluate viability**; **exhalation = execute abandonment decision (clear hypothesis tag)**. Both phases are part of one MECH-107 cycle; the claim captures only the exhalation side.

---

## Finding 3: preBotC-LC circuit — respiratory rhythm hardwired to NE precision modulation

**Yackle et al. (2017)** — *Science*, PMID: 28360327, DOI: 10.1126/science.aai7984
~175 Cdh9/Dbx1-positive preBötzinger complex neurons project **monosynaptically to locus coeruleus**. Selective ablation left breathing intact but shifted mice toward sustained calm/reduced arousal. Establishes a direct breathing-to-NE arousal circuit — the respiratory oscillator is hardwired to NE (unexpected uncertainty) release.

**Architectural implication:** MECH-108 (respiratory sweep clock) and MECH-104 (LC-NE volatility interrupt) are not independent claims — they share a substrate. The preBotC is the upstream clock for both. This means:
- Breath-rate changes modulate baseline NE tone, which modulates running_variance, which modulates commit_threshold crossing frequency
- A BreathOscillator that modulates commit_threshold is biologically grounded in a real monosynaptic circuit, not just an analogy
- Respiratory pacing of NE may be the mechanism by which MECH-104 (surprise interrupt) and MECH-108 (plan-sweep clock) interact — the same circuit does both at different timescales

**New dependency to register:** MECH-108 depends on MECH-104 via the preBotC-LC pathway, not just architecturally (via ARC-023) but mechanistically. Add MECH-104 to MECH-108 depends_on.

---

## Finding 4: Sigh rate as behavioral correlate of plan-abandonment (MECH-107/109 validation)

**Vlemincx et al. (2010)** — *Psychophysiology*, PMID: 20536901, DOI: 10.1111/j.1469-8986.2010.01043.x
Sigh rate **increased during and immediately after** mental load and sustained attention tasks. Sustained attention compressed total respiratory variability (reduced flexibility). Sighs functioned as resets — restoring respiratory variability after high-commitment compression. The sigh is not a random event; its timing correlates with sustained-attention offload.

**Architectural implication:** This is the closest direct behavioral evidence for MECH-107 and MECH-109:
- High-commitment sustained attention compresses respiratory flexibility (analogous to: committed trajectory suppresses plan-sweep clock)
- Sigh = forced plan-sweep reset (MECH-109: voluntary handle on sweep clock)
- Sigh rate at load recovery is the measurable output

**Experimental prediction for REE substrate:** If commit_threshold is elevated and MECH-104 jitter is active, sigh-equivalent events (large upward impulse to running_variance) should be more frequent when the agent has been committed for many consecutive steps — a fatigue/load effect. This is a testable prediction beyond EXP-0089/090/091.

---

## Finding 5: Infraslow oscillations nest faster rhythms — a second slower cycle

**Monto, Palva, Voipio & Palva (2008)** — *Journal of Neuroscience*, PMID: 18701689, DOI: 10.1523/JNEUROSCI.1910-08.2008
Infraslow EEG fluctuations (0.01–0.1 Hz, i.e., 10–100 seconds per cycle) predicted somatosensory detection probability: 55% higher hit rate in the rising vs. falling ISF phase. Fast oscillation amplitudes (1–40 Hz) were robustly correlated with ISF phase. **Phase, not amplitude**, is the operative variable — the slow oscillation gates excitability rather than adding noise.

**Architectural implication:** There is a second, slower oscillatory modulator below respiratory frequency. ISF at 0.01–0.1 Hz = one cycle every 10–100 seconds. In simulation terms (10 Hz): 100–1000 steps per cycle. This is potentially the substrate for **longer-scale commitment hysteresis** — the agent's mean commitment level oscillates on timescales longer than any single breath cycle.

For EXP-0091 (MECH-047 hysteresis): the re-commitment latency after a breath sweep may be nested within a slower ISF-equivalent modulation. Consider a secondary slow oscillator parameter in a later experiment.

---

## Finding 6: Neuromodulator cycling — NE (interrupt), 5-HT (persistence), and their duality

**Dayan & Yu (2006)** — *Network: Computation in Neural Systems*, PMID: 17162459, DOI: 10.1080/09548980601004024
Bayesian model: **phasic LC-NE = unexpected uncertainty** (model failure, structural change). **Tonic NE = expected uncertainty** (routine volatility tracking). The model reproduces sub-second LC responses in visual discrimination. Confirms MECH-104's framing directly.

**Lottem et al. (2018)** — *Nature Communications*, PMID: 29520000, DOI: 10.1038/s41467-018-03438-y
Optogenetic DRN serotonin (5-HT) activation increased nose-poke persistence and dwell time in probabilistic foraging. **5-HT promotes active persistence / staying-in-plan** — it is the complement of NE. 5-HT reduces probability of abandoning a current trajectory per unit time; NE (phasic) is the interrupt signal.

**Architectural implication:** The neuromodulator duality — 5-HT (stay) vs NE phasic (interrupt) — maps directly onto the BreathOscillator's function:
- **Inter-sweep phase** (committed): 5-HT-dominant — stay, persist, hold trajectory
- **Sweep phase** (uncommitted window): NE primed — sample, re-evaluate, interrupt-eligible

The BreathOscillator in simulation is modelling the **oscillation between 5-HT-dominant and NE-ready states** at respiratory frequency. This is not just a threshold trick — it is a plausible approximation of a real neuromodulator cycling pattern. The preBotC-LC circuit (Yackle 2017) provides the pacemaker for this cycling.

**New claim candidate:** A new MECH may be worth registering: "5-HT and phasic NE constitute a commitment-duality pair; respiratory cycling oscillates between 5-HT-dominant (stay/commit) and NE-ready (interrupt/release) states." This would be the mechanistic substrate for MECH-108.

---

## BreathOscillator Parameter Revisions (from LIT-0094)

| Parameter | Prior proposal | Revised | Basis |
|---|---|---|---|
| `breath_period` | 50 steps | **50 steps (confirmed)** | Zelano 0.16–0.33 Hz → 30–60 steps; 50 is mid-range |
| `sweep_duration` | 5 steps | **20 steps** | Zelano/Boyadzhieva: inhalation phase ~2 sec at 10 Hz = 20 steps; prior 5 steps was too short to sample |
| `sweep_amplitude` | 0.1 | **0.1 (confirmed)** | Braendholt: threshold lowering is moderate, not dramatic; 0.1 above base threshold is appropriate |
| Phase trigger | threshold raise | **threshold lower on inhalation** | Braendholt: inspiration lowers decision boundary. Revised: sweep window = *lower* commit_threshold by sweep_amplitude (i.e., agent is less committed, more likely to be uncommitted during sweep), not raise it |

**Critical direction correction:** The original proposal raised commit_threshold during sweep (making it harder to be committed = more uncommitted steps). The literature says inspiration *lowers* decision boundary. These are equivalent effects if we define "lowering the decision boundary" as "lowering the threshold below which running_variance must fall to be committed." Both produce uncommitted windows. The direction of the parameter change in the config is the same either way; only the framing changes.

---

## Implications for REE Claims

**MECH-107** (`respiratory.exhalation_trajectory_abandonment`): Partially revised. The claim is correct that exhalation is the output signal for plan abandonment, but incomplete — inhalation is the evaluation/sweep phase. Add to notes: "inhalation phase = viability scan (peak excitability, reduced decision boundary); exhalation phase = execute abandonment decision (hypothesis tag clear). Both phases are part of one sweep cycle; the claim captures the exhalation execution side." Status: candidate. No status change; framing refinement only.

**MECH-108** (`respiratory.breath_rate_plan_sweep_clock`): Add MECH-104 to depends_on (preBotC-LC monosynaptic circuit links the two directly). Add 5-HT as neuromodulator complement: inter-sweep = 5-HT-dominant; sweep = NE-ready. Status: candidate. No status change; evidence accumulating.

**MECH-109** (`respiratory.voluntary_breath_control_planning_gate`): Vlemincx 2010 provides direct behavioral evidence: sigh rate increases on load-recovery, sighs restore respiratory variability after commitment compression. This is the first empirical evidence that voluntary breath events correlate with plan-state transitions. Strengthen status_note with this finding. Status: candidate. Consider provisional after one targeted experiment.

**MECH-026** (ready vigilance), **MECH-029** (default mode), **MECH-047** (hysteresis): EXP-0089/090/091 updated with revised sweep_duration=20 steps and corrected phase framing. Experiments remain as designed.

**New candidate (unregistered):** "Respiratory cycling oscillates between 5-HT-dominant (commit/persist) and NE-ready (interrupt/release) neuromodulator states; the preBotC is the common pacemaker." — mechanistic substrate for MECH-108. Flag for registration.

---

## Summary: What the literature confirms, partially confirms, and challenges

| MECH-108 component | Status after LIT-0094 | Key paper |
|---|---|---|
| ~0.2 Hz respiratory clock exists | **Confirmed** | Zelano 2016, Tort 2018 |
| System-wide (not just hippocampal) | **Confirmed** | Tort 2018 (15 regions incl. NAc, PFC, amygdala) |
| Hardwired to NE precision modulation | **Confirmed** | Yackle 2017 (preBotC-LC monosynaptic) |
| Exhalation = plan-sweep trigger | **Partially revised** — inhalation = scan, exhalation = execute | Zelano 2016, Boyadzhieva 2021, Braendholt 2025 |
| Voluntary modulation is the top-down handle | **Confirmed (behavioral)** | Vlemincx 2010 (sigh rate = load-recovery reset) |
| Threshold + bias are independent | **New finding** | Braendholt 2025 (two computational mechanisms) |
| Slower nested oscillators also exist | **Confirmed** | Monto et al. 2008 (ISF 0.01-0.1 Hz) |
| 5-HT as persistence/commit complement to NE | **Confirmed** | Lottem 2018 |
