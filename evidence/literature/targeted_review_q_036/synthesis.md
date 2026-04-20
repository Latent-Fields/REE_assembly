# Synthesis: Q-036 — Affective Harm Load State Variables

**Pull date:** 2026-04-20
**Question (Q-036):** What additional variables, beyond temporal integration, are required for affective harm to become a genuinely distinct load state: persistence, recovery failure, uncontrollability, inescapability, or prediction error?

---

## Converging answer: temporal integration is necessary but not sufficient

Three papers converge on the same functional conclusion: affective harm load (suffering) has determinants that are orthogonal to or exceed what a temporal integrator over sensory magnitude captures.

**Salomons et al. 2004** (JNeurosci, n=16, fMRI): Identical noxious stimuli produce different ACC/insula activation depending solely on perceived controllability. Controllability modulates the affective pain circuit without changing stimulus intensity -- direct evidence that controllability is a load-determining variable beyond sensory input.

**Loffler et al. 2018** (Pain Reports, behavioural): Controllability selectively reduces suffering without affecting pain intensity or unpleasantness. This three-way dissociation (intensity / unpleasantness / suffering) establishes suffering as a construct with its own determinants, and controllability as one of them. Chance-attributional locus of control predicts suffering; catastrophising does not.

**De Ridder et al. 2021** (Neurosci Biobehav Rev, synthesis): Medial pain pathway (ACC/insula, overlapping with salience network) processes suffering; lateral pathway processes painfulness. The medial pathway's output is determined by "salience and context" -- behavioural meaning -- not sensory magnitude. Suffering is highest when harm is unresolvable and persistent: the acute-to-chronic transition is precisely where temporal accumulation becomes insufficient and additional variables (inescapability, loss of warning function) become necessary.

---

## Variable-by-variable summary

| Variable | Evidence status |
|----------|----------------|
| **Controllability / escapability** | Strong: two independent studies show specific effects on affective circuit and suffering dimension |
| **Persistence / duration** | Suggestive: De Ridder acute-to-chronic transition; not cleanly dissociated from controllability |
| **Recovery failure** | Indirect: chronic pain literature implies accumulation without recovery; not directly isolated |
| **Inescapability** | Theoretical: subsumed under uncontrollability in the experimental literature; the learned-helplessness literature provides supporting evidence but was not pulled in this session |
| **Prediction error** | Open: Fazeli & Buchel 2018 (not in this pull) shows anterior insula PE signals are modality-specific and not pure aversiveness; PE contributes but is not sufficient alone |

---

## Implication for MECH-219 and z_harm_a design

MECH-219 (temporal hysteresis integrator) captures duration and intensity-weighted accumulation. The literature here argues for at least one additional input: an estimate of controllability or escapability that gates the accumulator's effective magnitude. The biological locus is the dorsal ACC (Salomons et al.: integrates both stimulus and controllability context).

The connection to SD-032 (salience-network coordinator) is pointed out by De Ridder: the medial suffering pathway overlaps with the salience network. This means z_harm_a's computation is not isolatable from the salience coordinator -- the same system that triggers mode-switches (MECH-259) also modulates affective load.

---

## Confidence summary

| Entry | Confidence | Direction |
|-------|-----------|-----------|
| Salomons et al. 2004 | 0.75 | supports |
| Loffler et al. 2018 | 0.72 | supports |
| De Ridder et al. 2021 | 0.70 | supports |
| **Mean** | **0.72** | **supports** |

---

## Suggested follow-up

A second pull targeting inescapability specifically (learned helplessness; Maier & Watkins; Amat et al.) would fill the inescapability slot. A pull on pain prediction error (Fazeli & Buchel 2018; Büchel et al. 2014) would address the PE variable more directly.
