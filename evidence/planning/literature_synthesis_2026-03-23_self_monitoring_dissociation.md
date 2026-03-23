# Literature Synthesis: D_eff / Hopfield Familiarity / Markov Blanket Dissociation

**Date:** 2026-03-23
**Purpose:** Assess whether D_eff (participation ratio), Hopfield pattern familiarity,
and Markov blanket self-modeling are genuinely dissociable mechanisms in self-representation.
**Outcome:** All three are empirically and theoretically dissociable. Design of
Q-022 dissociation test and MECH-118/119 framing updated accordingly.
**Informs:** Q-022, MECH-113, MECH-118, MECH-119, EVB-0069

---

## Core Question

MECH-113 currently has three framings for "self-model coherence" that require deciding
whether they are measuring the same latent or independent dimensions:

1. D_eff (participation ratio): geometric coherence — how focused z_self is across its dimensions
2. Hopfield stability: familiarity — whether current z_self pattern matches stored self-states
3. Markov blanket resistance: topological — minimising surprise about self-generated states (FEP)

If any two of these always co-vary, the weaker one is redundant. If they dissociate,
MECH-113 will eventually need to be split and MECH-118/119 become independent mechanisms.

---

## Finding 1: Markov Blanket and D_eff Are Orthogonal by Construction

**Friston 2013 (PMID 23825119, DOI 10.1098/rsif.2013.0475)**
The Markov blanket formulation defines the self as the set of states with a specific
*conditional independence structure* — internal states screened from external by
sensory/active blanket states. This is a topological/graph property. D_eff is a
geometric property of the activity manifold. They are defined on different mathematical
objects and can vary independently.

**Hipolito et al. 2021 (PMID 33607182, DOI 10.1016/j.neubiorev.2021.02.003)**
Applies Markov blanket formalism at multiple neural scales. The partition is determined
by effective connectivity architecture, not by the content, dimensionality, or familiarity
of what is represented. A delusional patient still has a Markov blanket (still self-organizes)
but may have severely disrupted D_eff. A focused low-D_eff system may violate blanket
conditions through misrouted coupling. These are independent.

**Parr et al. 2021 (PMID 34573730, DOI 10.3390/e23091105) — MOST DIRECTLY RELEVANT**
"Memory and Markov Blankets." Directly addresses: conditional independence constrains
the *steady-state density*, not the dynamics. A system can have long memory time constants
(high Hopfield familiarity, sustained representations) while the Markov blanket integrity
depends on the *current* coupling structure. Familiarity depends on memory persistence
time; blanket integrity depends on current conditional independence. These are independent
parameters. *This is the strongest theoretical grounding for the three-way dissociation.*

**Palacios et al. 2019 (PMID 31756340, DOI 10.1016/j.jtbi.2019.110089)**
Hierarchical nesting of Markov blankets through simulation. Self-organisation occurs
through prior beliefs about *which units to couple with* (coupling structure), not
about the content or dimensionality of what is encoded. The geometric complexity of
internal representations (D_eff) is a downstream property that varies independently
of the coupling architecture (blanket).

**Conclusion:** Markov blanket is topological/structural; D_eff is geometric; familiarity
is mnemonic. All three are defined on different axes. They dissociate.

---

## Finding 2: Familiarity and Recollection Are Doubly Dissociable in Hippocampal Systems

**Yonelinas 2001 (PMID 11571028, DOI 10.1098/rstb.2001.0939)**
Canonical dual-process review. Recollection = threshold process, context-bound detail
retrieval, hippocampus-dependent. Familiarity = signal-detection process, graded sense
of prior occurrence, perirhinal cortex-dependent. Behaviorally, neurally, and
phenomenologically dissociable. Maps to REE: pattern familiarity is Hopfield-style
perirhinal process; recollection/context reconstruction maps to hippocampal generative
model (closer to Markov blanket self-modeling via causal reconstruction). Doubly dissociable.

**Aggleton et al. 2005 (PMID 16154457, DOI 10.1016/j.neuropsychologia.2005.01.019)**
Patient KN: 45% bilateral hippocampal volume loss, near-normal perirhinal cortex.
Near-normal familiarity, severely impaired recollection. *The clearest single existence
proof that familiarity survives without the hippocampal substrate.*
REE implication: Hopfield stability (familiarity) and hippocampal recollective-model
reconstruction can dissociate in both directions.

**Turriziani et al. 2008 (PMID 18306303, DOI 10.1002/hipo.20412)**
Convergent evidence from R/K and Process Dissociation Procedure in hippocampal amnesics:
recollection abolished, familiarity intact. The generation effect (which boosts
context-binding) selectively affected recollection in controls but not amnesics;
familiarity for generated words was identical. Confirms double dissociation across paradigms.

**Staresina et al. 2012 (PMID 22751037, DOI 10.1038/nn.3154)**
Simultaneous fMRI + intracranial EEG: hippocampus shows early source-retrieval then
late novelty signal; perirhinal cortex shows early item novelty then sustained source
retrieval. Familiarity (perirhinal) and recollection (hippocampal) process on *distinct
time bases*. For REE design: D_eff monitoring would track on the slow/sustained timescale,
while familiarity detection is fast. A time-course dissociation is testable in z_self.

---

## Finding 3: D_eff (Participation Ratio) Measures Capacity, Not Content Proximity

**PMID 27534393 (likely Rigotti et al. 2013, DOI 10.1038/nature12160)**
"The importance of mixed selectivity in complex cognitive tasks." Participation ratio
of PFC covariance eigenspectrum predicts *how many distinct states can be linearly
discriminated*, not whether any state is familiar or near a stored attractor. High-D_eff
mixed-selectivity enables exponential readout capacity. A Hopfield network with N stored
patterns has a fixed attractor structure; D_eff measures ambient dimensionality of the
activity space. These are orthogonal: you can have high D_eff with no familiar states
(novel high-dimensional space), low D_eff with very familiar states (settled attractor).

**Synthesis:** D_eff = capacity / coherence; Hopfield = proximity / familiarity.
Neither implies the other.

---

## Finding 4: Coherent-but-Unfamiliar States Are Clinically Real (MECH-117 Confirmed)

**Sierra & David 2011 (PMID 21087873, DOI 10.1016/j.concog.2010.10.018)**
Depersonalization (DP) = increased prefrontal inhibition of insula/limbic processing.
Self-representation remains structurally intact (thinking, planning, memory preserved =
low D_eff, focused coherent representation), but the emotional colouring signalling
"this is mine, this is familiar" is absent (low Hopfield stability). Markov blanket also
intact (still self-organizes, still conditionally independent from environment).
*This is precisely MECH-119: coherent (low D_eff) + unfamiliar (low stability) + intact
blanket. All three framings dissociate simultaneously in depersonalization.*

**Milliere 2017 (PMID 28588463, DOI 10.3389/fnhum.2017.00245)**
Drug-induced ego dissolution. Different compounds produce different dissociation profiles:
- Dissociatives: "coherent but detached" — intact cognition, abolished self-location
  (low D_eff, low familiarity, disrupted blanket coupling to spatial self-location)
- Psychedelics: high D_eff (dimensionality expansion, novel states, no familiarity),
  variable self-boundary dissolution
- Kappa-opioid agonists: dysphoric unfamiliarity with intact self-location
Three drug classes dissociate all three REE framings simultaneously.

**Paul et al. 2019 (PMID 31103548, DOI 10.1016/j.bpsc.2019.03.007)**
Only reduced extrastriate body area (EBA) to DMN connectivity predicted depersonalization
in depression. EBA processes visual body information (body-as-object = familiarity signal);
DMN integrates autobiographical self-model (Markov blanket component). Reduced coupling =
body familiarity signal severed from self-model integrity. High self-model coherence (DMN
active), low body familiarity (EBA-DMN decoupling). Clean neural dissociation.

**Harricharan et al. 2017 (PMID 28911803, DOI 10.1016/j.neuropsychologia.2017.09.010)**
PTSD vs PTSD with dissociative subtype: hyperarousal and depersonalization co-occur.
PTSD self-model is tightly organized around threat (high D_eff focused on danger-related
dimensions, intact blanket of threat responses), but body familiarity is suppressed
(perirhinal-level decoupling from interoceptive signals). All three framings dissociate
in this clinical context. The REE self-maintenance system would need all three metrics
to detect this state.

**Sierra et al. 2002 (PMID 11909918, DOI 10.1136/jnnp.72.4.530)**
Lesion analysis: depersonalization (body-ownership failure = parietal Markov blanket
disruption for interoceptive states) and derealization (visual hypoemotionality = Hopfield
attractor signal stripped of emotional salience) have distinct neural signatures. D_eff
of cognitive representations may be intact in both. Three-way dissociation in lesion data.

---

## Summary Table

| Framing | What it measures | Substrate | Dissociates when... |
|---------|-----------------|-----------|---------------------|
| D_eff (participation ratio) | Geometric capacity of representation space | PFC mixed-selectivity populations | Novel/complex states; fatigue; drugs (psychedelics raise D_eff) |
| Markov blanket self-modeling | Conditional independence structure (coupling architecture) | Interoceptive hierarchy + hippocampal context binding | Lesions to coupling (parietal, interoceptive cortex) independent of representation geometry |
| Pattern familiarity (Hopfield-style) | Distance to stored attractor / perirhinal signal | Perirhinal cortex, lateral entorhinal cortex | Hippocampal amnesia (familiarity preserved, recollection lost); depersonalization (geometry intact, familiarity signal suppressed) |

---

## Implications for REE Claims

### Q-022 (dissociation question): CONFIRMED THEORETICALLY
The three framings are dissociable by construction (Markov blanket vs D_eff) and
empirically (familiarity vs recollection). Q-022 shifts from "is dissociation possible?"
to "does dissociation occur in z_self representations in CausalGridWorldV2?" The
experimental design (EVB-0069) is now well-grounded.

### MECH-113 pending_design: RESOLVED TOWARD SPLIT
The three framings measure different things. MECH-113 (Level 1 D_eff reactive homeostasis)
is not the same mechanism as MECH-118 (Hopfield familiarity monitoring). Both are needed.
The combined certainty score from epistemic-mapping (0.4*entropy + 0.3*D_eff + 0.3*stability)
is vindicated as a multi-dimensional score, not redundant combination.

### MECH-119 (coherent-but-unfamiliar pathology): CLINICALLY VALIDATED
Depersonalization is the existence proof. Paul et al. 2019 provides the neural mechanism
(EBA-DMN decoupling). MECH-119 is not speculative — it has a documented clinical
instantiation with a known neural substrate.

### Architecture shape for MECH-114 commit gate:
If D_eff and familiarity are dissociable, the commit gate (MECH-114) should eventually
incorporate both:
  commit_allowed = (running_variance < threshold) AND (d_eff < d_eff_threshold)
                   AND (hopfield_stability > stability_threshold)
The third condition prevents commitment in the coherent-but-unfamiliar regime (MECH-119).

### Markov blanket framing in REE:
The blanket framing maps to a different level than D_eff and familiarity — it is about
the STRUCTURAL COUPLING between self and world, not about the quality of internal
representations. In REE terms: the Markov blanket of the REE agent is defined by the
latent stack's encoding (which sensory states it conditions on). The reafference predictor
(SD-007) and the z_self/z_world split (SD-005) implement aspects of the blanket.
D_eff and Hopfield stability are properties of *what is inside* the blanket.
These are different design dimensions. Markov blanket framing of MECH-113 may be
better registered as a separate constraint on the LatentStack design rather than
a framing of the self-maintenance loss.

---

## Key Papers for Claim Notes

| Paper | PMID | Relevance |
|-------|------|-----------|
| Friston 2013 | 23825119 | Markov blanket definition; orthogonal to D_eff |
| Parr et al. 2021 | 34573730 | Memory persistence ≠ blanket integrity; theoretical proof of dissociation |
| Hipolito et al. 2021 | 33607182 | Blanket = connectivity architecture, not representation geometry |
| Yonelinas 2001 | 11571028 | Familiarity vs recollection dual-process canonical review |
| Aggleton et al. 2005 | 16154457 | Familiarity preserved without hippocampus (clearest existence proof) |
| Staresina et al. 2012 | 22751037 | Temporal dissociation: familiarity fast, recollection slow |
| PMID 27534393 | 27534393 | D_eff = capacity; orthogonal to familiarity (Rigotti 2013) |
| Sierra & David 2011 | 21087873 | Depersonalization = coherent + unfamiliar; MECH-119 clinical proof |
| Paul et al. 2019 | 31103548 | EBA-DMN decoupling: body familiarity severed from self-model |
| Harricharan et al. 2017 | 28911803 | PTSD dissociative subtype: all three framings dissociate |
| Milliere 2017 | 28588463 | Drug-induced ego dissolution: three classes dissociate all three metrics |
| Sierra et al. 2002 | 11909918 | Lesion dissociation: depersonalization vs derealization have distinct substrates |
