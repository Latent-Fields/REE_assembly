# Targeted Review: ARC-067 — Idle Aversion / Boredom (Sustained-Low-Engagement Aversive Valence Accumulator)

**Claim:** ARC-067 — Architectural commitment that prolonged low-engagement is itself negatively valenced; the agent acts to escape boredom even in the absence of specific targets, threats, or novelty pressure. Aversive-side accumulator companion to ARC-066 (vigor) and ARC-068 (opportunity cost) in the non_deficit_action_drives family. Distinct from policy-side ARC-066: ARC-067 instantiates an aversive-side accumulator that recruits the same downstream as actual harm (z_harm-like channel), so engagement-poverty competes for action-selection priority on the same axis as discomfort.

**Session:** lit-pull-arc-067-boredom-2026-05-10T1620Z
**Date:** 2026-05-10
**Pull 2 of 3** in the non_deficit_action_drives family (ARC-066 / ARC-067 / ARC-068).

## Research Question

Five verdicts to deliver before child MECH/SD design can proceed:

1. **R1** — Functional account arbitration: Eastwood/van Tilburg engagement-search trigger vs Westgate & Wilson MAC attentional-failure vs ARC-068 opportunity-cost overlap.
2. **R2** — Timescale split: acute restlessness (~minutes / tens of episodes) vs chronic anhedonic flatness (~episodes / sessions). Confirm or refute biological support for separate substrates. **Flag** the split as a governance call if supported; do not execute.
3. **R3** — Routing channel: z_harm_a (affective stream / AIC analog per Critchley) vs separate engagement-rate scalar converging on a downstream consumer of z_harm_a. Pick biologically clean option.
4. **R4** — Engagement-rate estimator inputs: which of (commit transitions, novel-observation count, E3 deliberation depth, residue-write rate) are biologically grounded and which are not.
5. **R5** — Anhedonia / abulia / catatonic flatness anchor for future psychiatric_failure_modes.md cross-reference. Anchor only — no pathology mapping registered yet.

## Critical Disambiguations

The pull addresses four substrate boundaries to existing claims:

- **vs SD-010 / SD-011 z_harm streams** — boredom-aversive routing through z_harm_a (affective stream) confirmed via Danckert 2018 AIC-deactivation under boredom and Wilson 2014 self-shock exchangeability of boredom-aversive with physical pain.
- **vs MECH-216 predictive_wanting** — boredom is target-absent; MECH-216 is target-conditioned. van Tilburg 2017 confirms via meaning-seeking-not-stimulation-seeking action tendency.
- **vs MECH-314a striatal novelty** — novelty != engagement. van Tilburg + Westgate confirm: novel territory without engagement opportunity does not discharge boredom on either functional or attentional account.
- **vs MECH-302 suffering_derivative_comparator** — ARC-067 is structurally inverse: positive aversive accumulation rather than relief on valence drop. Cross-link maintained.

## Entries

| Entry ID | Authors | Year | Evidence Direction | Confidence | Verdicts Informed |
|----------|---------|------|--------------------|------------|-------------------|
| 2026-05-10_arc_067_unengaged_mind_eastwood2012 | Eastwood, Frischen, Fenske, Smilek | 2012 | supports | 0.78 | R1 (definitional anchor) |
| 2026-05-10_arc_067_mac_model_westgate_wilson2018 | Westgate, Wilson | 2018 | supports | 0.82 | R1, R2 (attentional vs meaning components) |
| 2026-05-10_arc_067_boredom_differentiation_vantilburg_igou2017 | van Tilburg, Igou | 2017 | supports | 0.74 | R1, R5 (functional emotion differentiation) |
| 2026-05-10_arc_067_function_of_boredom_bench_lench2013 | Bench, Lench | 2013 | supports | 0.66 | R1, R4 (goal-shift discharge condition) |
| 2026-05-10_arc_067_just_think_wilson2014 | Wilson, Reinhard, Westgate, Gilbert et al. | 2014 | supports | 0.78 | R3 (routing-channel exchangeability), R2 acute |
| 2026-05-10_arc_067_dmn_insula_danckert_merrifield2018 | Danckert, Merrifield | 2018 | supports | 0.72 | R3 (AIC routing), R4 (executive engagement) |
| 2026-05-10_arc_067_hpa_axis_ulrich_lai_herman2009 | Ulrich-Lai, Herman | 2009 | mixed | 0.55 | R2 chronic, R5 substrate context |
| 2026-05-10_arc_067_apathy_anhedonia_husain_roiser2018 | Husain, Roiser | 2018 | supports | 0.78 | R5 (apathy vs anhedonia distinction) |

## Summary Assessment

7 of 8 entries support ARC-067; 1 mixed (Ulrich-Lai is substrate-context only, intentional honesty about indirect mapping). Coverage spans:

- **Definitional / functional theory:** Eastwood 2012, Bench & Lench 2013, van Tilburg & Igou 2017
- **Attentional / cognitive-engagement theory:** Westgate & Wilson 2018
- **Behavioural-aversive empirical evidence:** Wilson 2014 (Science 11-study self-shock paradigm)
- **Neural-correlates / routing-channel evidence:** Danckert 2018 (AIC deactivation under boredom)
- **Chronic-timescale substrate context:** Ulrich-Lai 2009 (HPA-axis chronic stress)
- **R5 anhedonia/abulia anchor:** Husain & Roiser 2018 (transdiagnostic frontostriatal)

## Verdicts (full reasoning in synthesis.md)

- **R1:** primary mechanism is the **engagement-rate aversive accumulator** (Eastwood / van Tilburg / Bench-Lench). Westgate & Wilson MAC adds a meaning-misfit channel as a secondary parallel pathway. ARC-068 opportunity-cost overlap is real but on a different layer (E3 score axis vs z_harm_a valence axis). Confidence 0.80.
- **R2:** **biology supports the timescale split** (acute restlessness vs chronic anhedonic flatness on distinct substrates). **FLAG** to governance — do not execute. Acute and chronic should be separate child claims (proposed: MECH-Xa acute / MECH-Xb chronic). Confidence 0.72.
- **R3:** **route through z_harm_a / SD-011 affective stream** (AIC analog), driven by Danckert 2018 AIC-deactivation finding and Wilson 2014 self-shock exchangeability. Engagement-rate estimator produces positive-engagement signals that, when below threshold, allow slow accumulator to fire on the same channel as actual harm. Confidence 0.82.
- **R4:** biologically-grounded engagement-rate inputs are **commit transitions per episode, E3 deliberation depth, residue-write rate** (executive / effort-allocation proxies). **Drop novel-observation count** as primary input — it conflates with MECH-314a striatal novelty and is ruled out by van Tilburg's meaning-seeking-not-stimulation-seeking signature. Novelty may contribute as secondary positive engagement signal but not as primary boredom estimator. Confidence 0.74.
- **R5:** ARC-067 ablation maps onto **apathy** (Husain-Roiser frontostriatal effort-allocation failure), specifically **NOT anhedonia** (reward-experience failure / MECH-295 liking-channel). Anchor only — register pathology mapping in future psychiatric_failure_modes.md governance pass, not here. Confidence 0.78.

## Aggregate ARC-067 lit_conf

Expected post-indexer: **0.74** (supports-direction, 8-entry cohort with one intentionally-low-confidence substrate-context entry; weighted aggregate of seven supports + one mixed).
