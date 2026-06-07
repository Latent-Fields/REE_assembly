# Targeted review: hazard / aversion avoidance LEARNING

**Commissioned:** 2026-06-07, by the cluster failure-autopsy of V3-EXQ-603g / 624c / 651a
(`evidence/planning/failure_autopsy_V3-EXQ-603g-624c-651a_2026-06-07.md`).
**Purpose:** inform a *substrate mechanism* for the survival/hazard-avoidance learning leg that
the `scaffolded_sd054_onboarding` / goal-pipeline GAP-2 gate requires -- explicitly BEFORE any
further curriculum-budget iteration (avoiding the SD-003-style "philosophy-right /
mechanism-wrong, iterate the caveat" trap).

## The question

603g showed goal FORMATION works (G0 3/3, z_goal lights on forced feed) but the survival /
hazard-avoidance LEARNING leg does not train even when isolated as a dedicated Stage-H
(G1 0/3, G_H 0/3 at budget). The user adjudicated this as a **deeper survival/aversion-learning
substrate gap, not a budget tweak**. This review asks the biology: how is avoidance learning
actually acquired, and what does REE's substrate lack?

## Entries

| Entry | Claim | Direction | Conf | Contribution |
|---|---|---|---|---|
| Debiec & Sullivan 2017 (Neurobiol Learn Mem) | SD-035 | supports | 0.74 | Avoidance learning is developmentally/gradually acquired, gated by amygdala maturation (~PN10) + parental HPA/CORT buffering during acquisition. Avoidance is NOT an init-time capacity. |
| Thompson, Sullivan & Wilson 2008 (Brain Res) | SD-035 | supports | 0.70 | Substrate correlate: inducible BLA plasticity (gated by GABAergic-inhibition maturation) appears exactly when avoidance learning becomes possible. Substrate-readiness, not budget. |
| Tovote et al. 2016 (Nature) | MECH-279 | supports | 0.80 | CeA->vlPAG disinhibition produces freezing; freeze and flight are distinct competing outputs. Confirms MECH-279 freeze gate -- but it is RESPONSE EXECUTION, not avoidance learning. |
| Moscarello & LeDoux 2013 (J Neurosci) | SD-035 | **mixed** | 0.78 | **Load-bearing.** Active avoidance = resolving a Pavlovian-instrumental conflict; learning REQUIRES ilPFC to suppress CeA-driven freezing. ilPFC lesion -> more freezing, less avoidance. |
| Turchetta et al. 2020 (NeurIPS) | SD-054 | supports | 0.62 | ML mirror: hazardous tasks become learnable under an external instructor/reset curriculum that protects during acquisition and is withdrawn -- the maternal-buffering analogue. Methods-only. |

## Convergent verdict

Three independent lines converge on one diagnosis, and it is **not** "train longer":

1. **Avoidance learning is a developmentally-acquired, scaffold-dependent competency**, gated by
   a substrate-maturation step (Debiec & Sullivan; Thompson et al.). The 603g "isolated stage
   won't train at budget" shape is the *expected* signature of treating it as an init-time
   capacity. This supports treating `scaffolded_sd054_onboarding` as a genuine staged
   curriculum with protection-during-acquisition (corroborated on the ML side by Turchetta et al.).

2. **REE already has the Pavlovian/defensive side but not the instrumental-acquisition side.**
   SD-035 (amygdala salience) + MECH-279 (CeA->PAG freeze gate) give REE the *reaction*
   (Tovote). What is missing is the step from reaction to learned avoidance: Moscarello & LeDoux
   show that active-avoidance learning is the *resolution of a Pavlovian-instrumental conflict*,
   won by a top-down (ilPFC) inhibitory gate over the freeze output plus an instrumental-action
   pathway. A freeze-and-salience substrate with no reaction-suppression / instrumental layer is
   the ilPFC-lesion animal: it freezes instead of learning to avoid -- the 603g G_H 0/3 prediction.

3. **The fix is therefore structural, not budgetary.** Per the biology-before-formal-definitions
   principle, the mechanism question is carried by the biology entries; the ML curriculum entry
   only confirms the staged-scaffold *shape* is feasible.

## Recommended substrate direction (for implement-substrate / governance, NOT applied here)

The verdict that feeds `scaffolded_sd054_onboarding`:

- **Primary (mechanism):** wire SD-035 / MECH-279 as an avoidance-**learning** driver, and add the
  currently-missing piece they imply -- an **instrumental-avoidance action pathway plus an
  ilPFC-analog suppression gate over the freeze output** (a candidate new SD/MECH: "prefrontal
  suppression of the defensive reaction enabling instrumental avoidance acquisition"). This is the
  precise gap Moscarello & LeDoux identifies; a freeze-only substrate cannot learn to avoid.
- **Secondary (curriculum):** stage the onboarding so avoidance is acquired under an external
  protective scaffold that is annealed as competence grows (developmental maternal-buffering /
  Turchetta reset-curriculum analogue), rather than a single unscaffolded survival stage with a
  larger episode budget.
- **Do NOT** iterate `scaffolded_sd054_onboarding` curriculum budget as the primary fix; `ready`
  stays false until the structural avoidance-acquisition mechanism is addressed.

This gates ARC-060, MECH-320, ARC-068, and SD-054-readiness retests (all
`pending_retest_after_substrate`).
