# Acetylcholine, encoding, and consolidation (Hasselmo 1999) — MECH-207

**Claim:** MECH-207 — acetylcholine acts as a permissive write-gate on the surprise buffer: prediction errors trigger hippocampal destabilisation and offline memory updating only when basal-forebrain cholinergic activation co-occurs.

## What the paper did

Hasselmo's influential *Trends in Cognitive Sciences* review integrates rodent cholinergic physiology with computational models of memory. The central proposal: acetylcholine sets the hippocampus into one of two operating regimes depending on its level. During active waking, **high** acetylcholine partially suppresses excitatory feedback connections within the hippocampus — this favours *encoding*, because new input can be laid down without interference from previously stored patterns. During quiet waking and slow-wave sleep, **low** acetylcholine releases that suppression, allowing activity to spread within the hippocampus and outward to entorhinal/association cortex — this favours *consolidation*, the formation of additional cortical traces. Acetylcholine, in short, is the switch between "take in new information" and "replay and stabilise old information."

## Why it matters for REE — and the honest tension

This is the foundational source for the *idea* MECH-207 rests on: that a single cholinergic signal gates **which memory operation the hippocampus is performing** — a state-conditional plasticity switch. REE owns the *closure* side of plasticity gating (EWC, MECH-333/334) but lacks the *opening* side, and a cholinergic encode-versus-consolidate switch is exactly that missing primitive. To that extent the paper supports the claim's premise.

But I have marked this **mixed**, not supports, and the reason is a directionality mismatch worth being explicit about — this is precisely the "philosophy-right / mechanism-wrong" trap the biology-before-formal-definitions rule exists to catch. Hasselmo's classic model places *consolidation* at **low** acetylcholine. MECH-207 (which the node attributes to Sinclair 2021) frames acetylcholine as the **permissive** write-gate — PE-tagged episodes become *eligible* for offline updating *with* cholinergic co-activation. The two are reconcilable: Hasselmo is describing ACh suppressing interference during online encoding, while MECH-207 is describing ACh gating which specific episodes earn eligibility for later updating — different operations, on plausibly different timescales and circuits. But they are not the same *sign*, and it would be wrong to cite Hasselmo as clean support for MECH-207's permissive-write-gate directionality.

## Caveats and confidence

The mapping-fidelity axis is the weak one here (0.58): the paper grounds the *frame* (ACh gates an encode/consolidate switch) but not MECH-207's *specific directionality*. The source itself is canonical and high-quality. The actionable consequence: HPL-9 should not be marked fully grounded on the strength of this entry — the Sinclair (2021) primary the node names must be pulled to settle whether the write-gate is permissive-at-high-ACh (as MECH-207 states) or whether MECH-207 needs reformulating toward the classic low-ACh-consolidation account. Confidence 0.62 (mixed), with that follow-up flagged as the load-bearing next step for this claim.

*According to PubMed.* Source: Hasselmo ME (1999), *Trends in Cognitive Sciences* 3(9):351–359. [DOI](https://doi.org/10.1016/s1364-6613(99)01365-0)
