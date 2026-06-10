# MECH-189 — combined literature evidence overview

**Claim:** MECH-189 — *"During the child phase, high-salience benefit contacts under high contextual complexity are written to persistent ContextMemory as super-ordinal goal anchors that bias adult z_goal seeding across novel episodes."*
**Status:** candidate / v3_pending / `experimental_confidence` 0.0; substrate implemented 2026-06-09 (`SuperOrdinalGoalMemory`); validation EXQ pending (infant_substrate:GAP-11 → V3-EXQ-588c).
**Compiled:** 2026-06-10. **Purpose:** reconcile the two MECH-189 literature reviews — pulled independently and in parallel on 2026-06-09 — into one governance view.

## Why there are two directories

Two lit-pull sessions started within 2 seconds of each other on 2026-06-09, attacking MECH-189 from different angles. Per operator decision (2026-06-10), both directories are kept; the evidence is **already unified at the claim level** because the indexer aggregates literature by `claim_ids_tested`, not by directory — every entry in both folders tags `MECH-189`, so they all feed the single `literature_confidence`. The directory split is organizational, not an evidence fork.

| Directory | Question | Lens | Verdict |
|---|---|---|---|
| [`targeted_review_mech_189`](targeted_review_mech_189/SYNTHESIS.md) | Does the **formation mechanism class** hold? | Developmental (incentive salience, infant operant memory, schema consolidation, explore-window) | **Class supported** — clears the biology-before-mechanism gate. |
| [`targeted_review_connectome_mech_189`](targeted_review_connectome_mech_189/SYNTHESIS.md) | What should the **write-gate threshold** be (DEV-NEED-024)? | Connectome / electrophysiology (hippocampal–VTA loop, prediction-error, U-shape expectedness) | **Gate justified; the substrate's default *form* is questionable** — prefer a PE/surprise gate over monotonic novelty. |

Aggregate at compile time: `literature_confidence ≈ 0.83`, `experimental_confidence` 0.0, quadrant **plausible_unproven** (lit support present; experiment still owed).

## The two reviews operate at different levels — and do not conflict

The natural worry is that one review "supports" and the other "questions" the same claim. They do not contradict, because they answer different questions:

- The **formation** review asks whether the *architecture* (salient contact → cue-indexed durable anchor, formed preferentially in childhood) corresponds to real biology. It does: the four pillars chain end-to-end (incentive-salience write trigger → labile cue-indexed infant trace → schema-consolidated cortical anchor → during the childhood explore window).
- The **write-gate** review asks how the *"high contextual complexity" term* should be computed. It finds the substrate's specific default (`complexity_mode='novelty'`, monotonic `1 − cosine` to anchor keys) biologically suspect, and points toward a prediction-error / surprise signal.

So: **the mechanism class is endorsed; one parameter inside it is flagged for redesign.** A reader should not take the formation review's Gopnik-based "childhood novelty/exploration is justified" as an endorsement of the *monotonic anchor-distance* implementation — Gopnik justifies novelty at the life-history/window level (why childhood writes), not the functional form of the gate signal (which signal triggers a write). The write-gate review is the authority on the latter.

## Two convergences worth flagging (the reviews reinforce each other)

1. **Persistence requires a co-occurring novelty/surprise event.** The formation review's main caveat (Rovee-Collier: infant operant memory decays without reactivation) and the write-gate review's Lima-2023 entry (novelty co-occurrence is what captures a labile trace into durable storage) are the *same finding from two sides*. Biologically, the durable super-ordinal anchor is not a one-shot write — it is a labile trace **stabilised by a novelty/surprise-tagged consolidation event**. This strengthens the recommendation that the validation EXQ build in repeated, surprise-accompanied child-phase re-encounters rather than single writes.

2. **The "complexity" and "salience" gates are not independent.** Formation grounds gate (a) on incentive salience (a value/wanting signal); the write-gate review grounds the durable write on a *value*-modulated, dopaminergic motivated-memory pathway (Elliott; Aberg). Both point at the same VTA–dopamine substrate, suggesting gates (a) salience and (b) complexity may be facets of one value-prediction-error signal rather than two orthogonal thresholds — a substrate simplification worth testing.

## Net governance verdict

**Biology supports the MECH-189 mechanism class and clears the biology-before-formal-definitions gate.** Promotion past v3_pending still requires experimental evidence (the gate is necessary, not sufficient). Three items carry forward to the validation work, none of which change confidence or status:

1. **DEV-NEED-024 (write-gate form):** prefer `complexity_mode='external'` fed by an E1/E2 prediction-error/surprise signal over the monotonic `'novelty'` default; if novelty is kept, reference the world model not the anchor keys, and consider a signed/nonmonotonic form. Fed into the design doc + dev-needs register. Transfer caveat: REE forward-model PE vs the literature's value/RL PE.
2. **Persistence is reactivation-conditional:** the validation EXQ should include repeated, surprise-accompanied child-phase re-encounters; the substrate models no decay/reactivation (fidelity gap, noted not fixed — substrate code out of scope).
3. **MECH-329 developmental ordering** (wanting-before-liking) is the thinnest link — separability is grounded, the *temporal* ordering is not, and its cited anchor "Keren-Portnoy & Tomasello 2021" could not be independently verified. Recommend a dedicated MECH-329 ontogeny lit-pull + anchor correction in claims.yaml.

*Lit signal only — `experimental_confidence` and `status` untouched throughout, per the lit/exp decoupling rule.*
