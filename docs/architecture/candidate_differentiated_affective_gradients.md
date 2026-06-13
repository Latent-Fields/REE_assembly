---
title: Candidate-Differentiated Affective Gradients (V4/V5 cluster)
parent: "Affect, Harm & Nociception"
grandparent: Architecture
nav_order: 5
---

# Candidate-Differentiated Affective Gradients (V4/V5 cluster)

**Status:** candidate / substrate_conditional / implementation_phase v4 — **DO NOT build in V3.**
**Registered:** 2026-06-09
**Claims:** MECH-359 (candidate affect vector), MECH-360 (expression as action geometry), MECH-361 (candidate-gradient episode schema)
**Source thought:** [docs/thoughts/2026-06-06_Candidate-differentiated_affective_gradients.md](../thoughts/2026-06-06_Candidate-differentiated_affective_gradients.md)
**Intake:** [evidence/planning/thought_intake_2026-06-06_Candidate-differentiated_affective_gradients.md](../../evidence/planning/thought_intake_2026-06-06_Candidate-differentiated_affective_gradients.md)

This is a **stub** capturing why the cluster exists and the V3/V4 boundary. It is not a build spec — these claims must not be implemented in V3 until routed by experiment.

---

## 1. The seed (V3-EXQ-643 autopsy)

V3-EXQ-643 (modulatory-authority validation) FAILed at the authority-active precondition: in both authority-ON arms `modulatory_authority_active_frac = 0.0` and `scale_factor = 0.0`. The modulatory/curiosity contribution had **magnitude** (~0.024 mean-abs) but **zero cross-candidate range** — a per-tick scalar added equally to all K candidates. A scalar added equally to every candidate cannot change an argmax, so E3 had nothing to rescale into action-selection authority. *"Rescaling a zero range is still zero."*

The autopsy's first root cause ("modulatory bias uniform across candidates") was later corrected: the binding cause was **float32 catastrophic cancellation** — the 643 harness trained SD-056 online, exploding primary E3 scores to ~1e32, so the gate's `modulatory_total = scores - scores_raw` subtracted two ~1e32 floats and the genuine ~0.17 range collapsed below the float32 ULP. **V3-EXQ-643a** fixed this and added a **range/non-vacuity readiness gate** (require measurable per-candidate range before testing authority).

The generalisable insight the thought extracts:

> **For affect to carve behaviour, the affective contribution must be candidate-differentiated (carry cross-candidate range), not merely per-tick magnitude.**

---

## 2. What is V3 (already owned) vs what is this cluster (V4/V5)

**V3-narrow — already operationalised, NOT in this cluster:**

| Concern | Owner |
|---|---|
| range-not-magnitude readiness gate | V3-EXQ-643a (range/non-vacuity gate, same-statistic rule) |
| per-candidate signal collapse (`cand_world_pairwise_dist=0.0`) | `behavioral_diversity_isolation:GAP-A` + SD-056 |
| committed-class diversity preservation at E3 scoring | MECH-341, `behavioral_diversity_isolation:GAP-B` |
| per-candidate world-forward divergence preservation | SD-056 |

Registering a V3 claim for the range-not-magnitude principle would duplicate these and corrupt their evidence records (per the `claim_ids` accuracy discipline). It is therefore **not** registered — captured as a lesson-note on the above instead.

**V4/V5-rich — this cluster (MECH-359/360/361):** the *unification* — one candidate-differentiated affective-gradient structure serving selection authority **and** expression **and** hippocampal indexing — is genuinely new and is what these three claims record.

---

## 3. The three claims

- **MECH-359 — candidate affect vector.** Each E3 candidate trajectory carries a multi-channel affect vector (curiosity / safety / harm-sensory / harm-affective / effort / relief / blocked-agency). The bridge primitive; MECH-360 and MECH-361 depend on it. `depends_on: MECH-055, SD-011, MECH-341, SD-056`.
- **MECH-360 — expression as emergent action geometry.** Because candidate-differentiated affect selects trajectories, it shapes the visible *style* of behaviour (hesitation, latency, approach angle, oscillation, decommitment). Expression is the emergent geometric residue of per-candidate arbitration — complementary to MECH-041's broadcast framing, not a replacement. `depends_on: MECH-359, MECH-041`.
- **MECH-361 — candidate-gradient episode schema.** Enrich the trace to `state -> candidates -> affective gradients -> selected -> outcome -> residue`; use the affective gradient as a write-weight and retrieval-query variable. Amends MECH-261's content schema (not the gate) and sharpens MECH-074's BLA arousal-write-gain. `depends_on: MECH-359, MECH-261, MECH-074, MECH-094`.

```text
proto-affect
-> E3 action selection            (MECH-359 candidate affect vector)
-> behavioural expression         (MECH-360 action geometry)
-> hippocampal event indexing     (MECH-361 episode schema)
-> future retrieval / replay
-> V4 other-attribution
-> V5 communication and grammar
```

---

## 4. V3/V4 boundary and the do-not-build rule

`substrate_conditional`: these claims depend on a V4 per-candidate multi-channel affect substrate that is not yet built. Promote/demote is suppressed; the correct response is to **wait for the upstream substrate**, not to run more experiments on the current single-channel modulatory path.

**Revisit trigger:** re-open after a downstream per-candidate-affective-variance readiness result on the GAP-A-ready substrate (the MECH-341 within-class-representative-diversity retest + GAP-A bias channels demonstrating per-candidate range bites at behavioural runtime). Only then consider a V4 build of MECH-359, with MECH-360/361 strictly after it.

**IGW visibility (verified 2026-06-09):** `epistemic_category: substrate_conditional` keeps these claims **out of** the inter-governance workset and the promotion/demotion queue while V3 work is in flight. It is in the IGW generator's `_EPI_SUPPRESS_PROPOSAL` set (`generate_inter_governance_workset.py`, with the proposal lane skipping such claims) and the indexer suppresses promote/demote for the category. Empirically the precedent `substrate_conditional` cluster (play-mode MECH-194..199) has 0 hits in the current workset and 0 rows in `promotion_demotion_recommendations.md`. The suppression lever is the epistemic category, not `implementation_phase: v4` (which is the scheduling/prediction label). So MECH-359/360/361 stay invisible to IGW during the V3 phase by construction; do not queue probes against them until the V4 substrate exists. They remain discoverable for the V4 phase via `implementation_phase: v4` in `claims.yaml` + this doc.

---

## 5. Literature anchors (for a later targeted review — none load-bearing for registration)

McGaugh 2004 (Annu Rev Neurosci); Cahill & McGaugh 1998 (TINS); Dolcos, LaBar & Cabeza 2004 (Neuron); Girardeau, Inema & Buzsáki 2017 (Nat Neurosci 20:1634 — verified); Ballarini et al. 2009 (PNAS 106:14599, behavioural tagging — verified); Bechara et al. 1994 (Cognition) + Damasio 1994 (somatic markers); Ólafsdóttir, Bush & Barry 2018 (Curr Biol) + Joo & Frank 2018 (Nat Rev Neurosci — replay).
