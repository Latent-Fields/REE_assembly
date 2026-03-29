# Targeted Literature Review: ARC-018

**Claim ID:** ARC-018
**Claim title:** hippocampus.rollout_viability_mapping
**Claim text:** "Hippocampus generates explicit rollouts and post-commitment viability mapping, indexed by E2 action-object coordinates and updated by E3 harm/goal error."
**Status at time of review:** active, adjudicated (retain_ree)

**Date created:** 2026-03-29
**Number of entries:** 5

---

## Rationale for source selection

ARC-018's corrected V3 framing breaks into two separable claims: (1) hippocampus generates prospective rollouts anchored to goal/harm coordinates; and (2) those rollouts are indexed by E2 action-object coordinates (not spatial position) and updated by E3 harm/goal error. The literature strongly supports (1) and is largely agnostic about (2) -- which is exactly the gap V3 experiments are designed to close.

Sources were selected to triangulate the claim from multiple angles:

- **Pfeiffer & Foster (2013)** -- gold-standard electrophysiology for the forward-sweep mechanism itself. Rats, CA1, open arena, pre-movement sequences to known goals. Best evidence for prospective rollout generation.
- **Mattar & Daw (2018)** -- normative computational theory for why replay should be error-driven and utility-prioritised. Closest theoretical framework to ARC-018's E3-error-driven update mechanism.
- **Olafsdottir, Carpenter & Barry (2017)** -- dynamic switch between planning-mode and consolidation-mode replay. Best evidence for the dual-mode operation (rollout before, update after) ARC-018 requires.
- **Momennejad, Otto, Daw & Norman (2018)** -- human fMRI showing offline replay predicts replanning in abstract sequential decisions. Extends the mechanism beyond spatial coordinates toward action-sequence representations.
- **Dolan & Dayan (2013)** -- theoretical review establishing hippocampus as the substrate for model-based planning and flexible value updating. Conceptual scaffolding for the viability-map claim.

---

## Entries

| entry_id | Paper | Direction | Confidence |
|----------|-------|-----------|-----------|
| 2026-03-29_arc_018_forward_sweeps_pfeiffer2013 | Pfeiffer & Foster 2013, Nature | supports | 0.85 |
| 2026-03-29_arc_018_prioritized_replay_mattar2018 | Mattar & Daw 2018, Nat Neurosci | supports | 0.80 |
| 2026-03-29_arc_018_awake_replay_switch_olafsdottir2017 | Olafsdottir et al. 2017, Neuron | supports | 0.78 |
| 2026-03-29_arc_018_offline_replay_planning_momennejad2018 | Momennejad et al. 2018, eLife | supports | 0.72 |
| 2026-03-29_arc_018_goals_habits_dolan2013 | Dolan & Dayan 2013, Neuron | supports | 0.68 |

---

## Overall assessment

The biological literature clearly and consistently supports the rollout-generation component of ARC-018. The prospective forward-sweep mechanism (Pfeiffer & Foster), the utility-prioritised update logic (Mattar & Daw), the dual planning/consolidation mode (Olafsdottir et al.), and the human replanning evidence (Momennejad et al.) all converge on the same conclusion: hippocampus generates goal-directed prospective sequences that are updated by value/error signals and that causally support planning.

The specific V3 claims -- E2 action-object indexing and E3 harm/goal error as the update signal -- are not directly tested by any of these papers. The Momennejad et al. human data (abstract sequential task) and the Mattar & Daw utility framework are the closest analogues. The critical gap is the harm-signal component: all studies reviewed here use reward-based or uncertainty-based (unsigned PE) signals, not explicit harm signals. Whether hippocampal viability mapping operates equivalently for harm-loaded action sequences is supported by the framework (Dolan & Dayan) but not directly demonstrated.

This is not a weakness of ARC-018 -- it is a precise statement of what V3 experiments need to test.
