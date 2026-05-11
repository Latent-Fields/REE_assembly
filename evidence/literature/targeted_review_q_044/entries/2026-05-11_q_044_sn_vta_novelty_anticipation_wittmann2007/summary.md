# Wittmann et al. 2007 — Anticipation of novelty recruits reward system and hippocampus

**Citation.** Wittmann BC, Bunzeck N, Dolan RJ, Düzel E. (2007). Anticipation of novelty recruits reward system and hippocampus while promoting recollection. *NeuroImage* 38(1):194-202. [DOI](https://doi.org/10.1016/j.neuroimage.2007.06.038). PMID 17764976.

## What the paper did

Wittmann and colleagues tested whether the dopaminergic midbrain (substantia nigra / ventral tegmental area, SN/VTA) signals anticipated novelty in the same way it signals anticipated reward. Sixteen healthy adults underwent fMRI while viewing symbolic cues that predicted either novel or familiar images of scenes, with 75% validity. They examined four conditions: cue-predicting-novelty, cue-predicting-familiarity, anticipated novel image (matching the cue), and unexpected novel image (after a familiarity cue).

SN/VTA was activated by cues predicting novel images and by unexpected novel images themselves. The activation profile parallelled the canonical reward-prediction signal: the system responds to anticipation and to unexpected occurrence. The hippocampus also showed anticipatory novelty responses but with a different profile — it activated at outcome for expected and unexpected novelty alike. In a behavioural follow-up the same subjects showed enhanced recollection memory for anticipated novel events.

The take-home is that novelty has its own dopaminergic anticipation signal, distinct from reward anticipation in stimulus content but using the same dopaminergic-midbrain circuitry, and that the hippocampus participates in encoding novel events with a primed-by-anticipation signature.

## Relevance to Q-044

Q-044 asks whether MECH-314a (striatal novelty), MECH-314b (frontopolar uncertainty-driven curiosity), and MECH-314c (learning-progress curiosity) are three distinct substrates or three readings of one mechanism. Wittmann 2007 is the canonical anchor for MECH-314a's substrate identity: the striatal/SN-VTA novelty signal is dopaminergic, anatomically distinct from the frontopolar locus of uncertainty-driven exploration (Daw 2006), and operates via a specific computation (novelty-anticipation) that differs from the value-of-information computation underlying directed exploration. This is positive evidence for the slot-level distinction Q-044 asks about — at least for the MECH-314a vs MECH-314b boundary.

It does not, by itself, dissociate MECH-314a from MECH-314c (learning-progress). Both could plausibly involve dopaminergic signalling, and Kaplan & Oudeyer 2007 (sibling entry) explicitly proposes tonic dopamine as a learning-progress signal. The two are observationally similar in that both produce "reward-like" responses to information-related events. The substrate-level distinction MECH-314a vs MECH-314c is harder to make from human fMRI alone.

## Caveats

The dopaminergic-midbrain novelty signal in Wittmann 2007 could in principle be accounted for by a single prediction-error variable that updates on both novelty and reward outcomes (Kakade & Dayan 2002). That is, the fact that SN/VTA responds to novelty does NOT prove that the novelty signal is mechanistically distinct from the reward signal at the circuit level — they could share a common prediction-error machinery. For Q-044 this is the most important caveat: a single-mechanism account where 314a/b/c are three task-conditional readings of one underlying TD-error or free-energy signal cannot be ruled out from Wittmann alone.

fMRI cannot resolve phasic vs tonic dopaminergic activity. The papers that argue for distinct phasic-novelty and tonic-learning-progress signals (Kaplan & Oudeyer 2007) rely on electrophysiology and computational modelling, not BOLD.

For REE, the implementation-level translation is approximate. MECH-314a computes a state-novelty bonus over the encoder z-space; Wittmann's "novelty" is stimulus-novelty (images the subject has not seen). The algorithmic role (novel-state-driving-exploration) transfers; the specific computation may not.

## Confidence reasoning

I assign 0.80. Source quality (0.80) is good (NeuroImage, methodologically clean). Mapping fidelity (0.78) is moderate-high — the substrate locus aligns with REE's MECH-314a commitment, but the within-DA-system disambiguation against MECH-314c is left for other anchors. Transfer risk (0.30) is modest. The 0.80 reflects strong primary evidence for the SN/VTA novelty signal as a distinct circuit-level computation alongside reward, while acknowledging that the most-on-topic dissociation question (314a vs 314c) is partially unresolved.
