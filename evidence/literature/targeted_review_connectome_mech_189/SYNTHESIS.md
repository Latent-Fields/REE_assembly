# MECH-189 literature synthesis — DEV-NEED-024 write-gate threshold pass

**Claim:** MECH-189 (write-gate angle) — specifically **DEV-NEED-024**: *"What contextual-complexity threshold triggers a super-ordinal write?"*
**Substrate parameter under adjudication:** `super_ordinal_complexity_mode` / `super_ordinal_complexity_threshold` in `SuperOrdinalGoalMemory` (ree-v3 `goal.py`).
**Pull date:** 2026-06-09. **Entries:** 5. **Companion review:** [`targeted_review_mech_189`](../targeted_review_mech_189/SYNTHESIS.md) (super-ordinal goal *formation* mechanism class). **Combined view:** [`mech_189_evidence_overview.md`](../mech_189_evidence_overview.md).

This pull is the "follow-on lit-pull" the MECH-189 design doc deferred DEV-NEED-024 to: the substrate's WRITE gate (b) defaults to `complexity_mode='novelty'` (`complexity = 1 - max cosine(z_world, occupied anchor keys)`), explicitly flagged as "the DEV-NEED-024 adjudication target — to be settled by the validation EXQ and a follow-on lit-pull, not hard-coded." It asks the connectome/electrophysiology literature what the biological "contextual complexity" signal that gates a durable, value-laden memory write actually *is*.

## Entry-by-entry

| Source | Direction (conf) | Contribution |
|---|---|---|
| Lima et al. 2023 — *Novelty facilitates the persistence of aversive memory extinction* | supports (0.60) | Cellular justification for having a gate at all: a salient contact that does **not** co-occur with a novelty event may fail to persist; novelty co-occurrence captures it into durable storage (behavioural tagging). |
| Lisman & Grace 2005 — *The hippocampal-VTA loop* | mixed (0.72) | The biological template for the write gate: a novelty/complexity signal licenses a dopamine-mediated write into durable hippocampal memory. **But** the loop computes novelty as comparator-mismatch against the *entire stored model*, not distance to goal-anchor keys. |
| Elliott et al. 2022 — *Midbrain-Hippocampus structural connectivity predicts motivated memory* | supports (0.74) | MECH-189 writes a **value/goal** anchor, not a neutral trace; the relevant gate is the dopaminergic, value-PE-linked motivated-memory pathway — argues for an `external` mode driven by a value/prediction-error signal. |
| Aberg et al. 2017 — *Trial-by-trial modulation of associative memory by reward prediction error* | supports (0.63) | Strongest direct support for `complexity_mode='external'`: quantitative trial-by-trial **PE magnitude** is a genuine encoding-strength determinant for value-associated memory. |
| Quent et al. 2022 — *Shape of U: nonmonotonic object-location memory* | mixed (0.70) | The complexity term should **not** be a monotonic novelty/dissimilarity measure: memory is U-shaped in expectedness (both schema-congruent and schema-incongruent encode well). Favours a **signed/nonmonotonic PE-magnitude** term. |

## Verdict on DEV-NEED-024

**Having the gate is biologically supported; the substrate's default *form* of the gate is questionable on two specific counts.**

The evidence is unanimous that a durable, value-laden memory write is licensed by a novelty/surprise signal routed through a dopaminergic VTA–hippocampus pathway (Lima; Lisman & Grace; Elliott). MECH-189 is right to gate the write on a "contextual complexity" term. But the **monotonic `1 − cosine(z_world, anchor keys)` novelty default** is challenged:

1. **Wrong reference set.** Biological novelty is comparator-mismatch against the *whole world model* (Lisman & Grace), not distance to the small set of goal-anchor keys. The substrate's measure asks "is this context far from contexts I already made anchors for?" when the biology asks "is this context surprising given everything I know?" These diverge sharply once a few anchors exist.

2. **Wrong functional form.** The signal should be **prediction-error magnitude** (Aberg) and likely **nonmonotonic / signed** (Quent's U-shape: both the highly expected and the highly unexpected encode strongly), not a monotonic dissimilarity. A simple "far-from-anchors → write" rule misses the schema-congruent write regime.

**Recommendation (directional, to be confirmed by the validation EXQ, not a settle):** prefer `super_ordinal_complexity_mode='external'` fed by an E1/E2 prediction-error / surprise signal over the monotonic `'novelty'` default; if `'novelty'` is retained, compute it against the world model rather than anchor keys, and consider a signed/nonmonotonic form.

**Transfer caveat that bounds the verdict:** several of these papers use a *value/RL* prediction error, whereas REE's E1/E2 PE is a *forward-model (perceptual)* error. The recommendation assumes these surprise signals are functionally analogous as encoding-strength gates — a real assumption the validation EXQ should not take for granted.

## Governance note

Lit signal only. All 5 entries tag `MECH-189` (`claim_ids_tested`), so they already blend into MECH-189's `literature_confidence` via the tag-based indexer — there is no separate DEV-NEED-024 confidence channel. This synthesis exists to make the DEV-NEED-024 *design verdict* consumable; it does not change MECH-189's `experimental_confidence` (0.0) or `status` (candidate / v3_pending). The verdict is fed into the DEV-NEED-024 open-question rows in [`mech_189_super_ordinal_goal_anchors.md`](../../../docs/architecture/mech_189_super_ordinal_goal_anchors.md) and [`developmental_needs_register.md`](../../../docs/architecture/developmental_needs_register.md#dev-need-024).
