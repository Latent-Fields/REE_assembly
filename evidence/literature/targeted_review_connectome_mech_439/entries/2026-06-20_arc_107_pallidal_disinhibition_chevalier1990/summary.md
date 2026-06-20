# Chevalier & Deniau 1990 — disinhibition: the BG grant commitment by releasing a default brake, not by argmax

**Claim grounding:** ARC-107 (BG selector constitution), MECH-448 (F→eligibility demotion / permission-to-commit) · ARC-106 component 3 (pallidal output gate as permission-to-commit)
**Source:** Chevalier G, Deniau JM. *Trends in Neurosciences* 13(7):277–280 (1990). [DOI](https://doi.org/10.1016/0166-2236(90)90109-n) · PMID 1695403.
*According to PubMed.*

## What the paper argues

This short, foundational review crystallised what is now the textbook account of basal-ganglia output: **disinhibition**. The output nuclei (substantia nigra pars reticulata, internal globus pallidus) are *tonically active* GABAergic neurons that hold their downstream motor targets — superior colliculus, thalamus, brainstem motor centres — under sustained inhibition. Movement is initiated not by the basal ganglia *driving* a target but by a phasic striatal input that transiently **pauses** that tonic inhibition, *releasing* the selected target to act. Chevalier and Deniau frame the BG output as a "movement template" that specifies which motor elements are engaged. The resting state of the system is therefore "everything inhibited; nothing acts," and action is a local, selective lifting of the brake.

## Why it matters for the ARC-107 constitution

ARC-107 calls explicitly for "a pallidal-like permission-to-commit gate (rather than bare argmax)." Disinhibition is the precise biological grounding for that phrase. In REE's current selector the committed action is simply `argmin J(ζ)` — whatever minimises the cost, granted unconditionally, with no gate to pass. In Chevalier & Deniau's substrate, commitment is granted by **removing a default inhibitory brake** from the selected action. Two design consequences for ARC-107/MECH-448 follow directly:

1. **Default-deny.** The biological gate is tonically closed; nothing commits until permission (disinhibition) is granted. That is the structural *opposite* of unconditional argmin, and it is the addition ARC-107 must make. A selector that keeps unconditional argmin cannot express "permission-to-commit," however its scores are weighted — this is a structural change, not a reweighting.
2. **No-op default, granted not assumed.** MECH-448 is designed to be bit-identical OFF (no-op default). That mirrors the tonically-inhibited resting state: eligibility/permission is something that gets *granted*, never assumed. The biology endorses the conservative default the build already chose.

The "output as movement template" framing also supports the **eligibility-envelope** idea at the core of MECH-448: BG output specifies *which* elements are engaged — an eligible set — within which the movement is shaped, rather than emitting a single scalar winner. That is exactly "F sets eligibility, a modulatory channel arbitrates within it."

## The failure mode it makes the default

Disinhibition is valuable for the psychiatric column precisely because of its resting state. Because the default is *full inhibition*, the **default failure of a mis-set permission gate is global akinesia** — nothing converts, the bradykinetic/avolitional pole. MECH-448's psychiatric column names "envelope too tight → bradykinesia/avolition (the current failure: nothing but F converts)"; disinhibition is the grounding that makes that pole the *default* failure, not an edge case. This sharpens a real risk for the falsifier: a too-tight permission gate that lets nothing through will look, in the aggregate metric, exactly like a genuine upstream conversion ceiling. The REE falsifier's non-degeneracy and safety checks (design note §4: channels actually reach the selector; the envelope actually excludes non-eligible candidates rather than being all-deny) are what must distinguish "the gate is strangling conversion" from "there is nothing upstream to convert." And, as with every entry here, the gate only buys flexibility if the striatal pattern selecting *which* target to disinhibit is richer than the single dominant scalar — if F decides who gets disinhibited, the permission gate is argmin with extra steps.

## Limitations

The load-bearing divergence is mechanism-level: Chevalier-Deniau disinhibition is *literal tonic GABAergic inhibition phasically paused*, and REE has no tonic-brake substrate at all. REE will implement "permission" as an algorithmic commit-entry predicate over an eligible set, not as a released inhibition. I import the functional logic — default-deny, grant-by-release, eligibility-as-template — and explicitly not the GABAergic mechanism, per ARC-106's function-not-homology guardrail. It is also a short conceptual TINS review, so I cap source quality below the empirical entries even though it is canonical and heavily cited.

## Confidence

**0.71 (supports).** A clean functional grounding for the permission-to-commit gate and the default-deny / no-op-default design of MECH-448, discounted for being a conceptual review and for the literal-GABAergic → algorithmic-predicate translation.
