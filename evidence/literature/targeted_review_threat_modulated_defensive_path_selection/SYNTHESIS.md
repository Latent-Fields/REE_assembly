# Targeted lit-pull synthesis: threat-modulated defensive path-selection (SD-hazard-aware-policy-decomposition / MECH-321)

**Pulled** 2026-08-01 (9 entries).
**Target claim** MECH-321 (`policy_decomposition_via_event_segmenter`). **Commissioning artifact**: `evidence/planning/failure_autopsy_V3-EXQ-844_2026-08-01.md`, which found that MECH-321's mid-execution redecomposition step (`_apply_policy_decomposition`, `ree_core/hippocampal/module.py:896-983`; `PolicyDecomposition.evaluate()`/`decompose_sequence()`, `ree_core/policy/policy_decomposition.py:471-747`) reads no harm-valence signal and performs no ranked selection among candidate re-tilings at all (binary decompose/keep test per candidate; all survivors additively recombined).
**substrate_queue.json entry**: `SD-hazard-aware-policy-decomposition`, prerequisite for `implementation_hint` per its `/lit-pull` commission.
**Author**: lit-pull session (worktree `frosty-satoshi-2e7cbc`), 2026-08-01.
**Starting point**: Fanselow's Predatory Imminence Continuum (PIC), per the commissioning autopsy's explicit suggestion; followed outward via PubMed `find_related_articles` and targeted searches into human neuroimaging (Mobbs), a computational MF/MB reframing (Mobbs/Dayan), a causally-validated circuit mechanism (Branco lab), classical economic escape theory (Cooper), and classical ethoexperimental taxonomy (Blanchard).

---

## The two design questions this pull was commissioned to ground

1. **Threshold/switch vs. smooth/graded selection rule** — does the biology suggest a categorical shift in defensive-behavior selection as imminence crosses a boundary, or a continuous, harm-valence-proportional biasing of which option is favored?
2. **Which threat features modulate the selection rule** — beyond raw magnitude, what should a REE-side harm-valence signal (`z_harm_a`/BLA `threat_scale`) plausibly need to carry or be paired with?

## Verdict on Q1 — **both, at different levels: graded input, thresholded regime, graded output within the chosen regime**

The literature does not support either a pure single-fixed-threshold design or a pure smooth-linear-weighting design in isolation. Five entries converge on a specific dual-coding structure:

| Source | What it shows |
|---|---|
| Fanselow & Hoffman 2024 ([10.1037/amp0001354](https://doi.org/10.1037/amp0001354)); Hoffman et al. 2022 ([10.3758/s13420-021-00509-x](https://doi.org/10.3758/s13420-021-00509-x)) | Defense is organized into a small number of qualitatively distinct, empirically dissociable MODES (pre-encounter/anxiety, post-encounter/fear, circa-strike/panic) keyed to imminence — not a single continuous response curve. |
| Mobbs et al. 2007 *Science* ([10.1126/science.1144298](https://doi.org/10.1126/science.1144298)) | Human fMRI: which brain system CONTROLS defensive behavior literally switches (vmPFC → PAG) as imminence crosses a boundary, steepest under high anticipated harm — a genuine regime change, not a smooth blend. |
| Evans et al. 2018 *Nature* ([10.1038/s41586-018-0244-6](https://doi.org/10.1038/s41586-018-0244-6)) | Causally-validated circuit mechanism: a GRADED upstream signal (mSC saliency) drives a THRESHOLD-CROSSING categorical decision (dPAG escape choice) via a drift-diffusion process, while the SAME graded signal separately and continuously scales the chosen response's VIGOUR. Removing the threshold node doesn't produce no-response, it produces a different discrete DEFAULT (freezing). |
| Mobbs, Headley, Ding & Dayan 2020 ([10.1016/j.tics.2019.12.016](https://doi.org/10.1016/j.tics.2019.12.016)) | Recasts the above in REE's own computational vocabulary: proximal threat narrows the decision/state space toward fast, reduced-repertoire, model-free-like selection; distal threat affords full model-based deliberation over a larger space. |
| Fanselow, Hoffman & Zhuravka 2019 ([10.1016/j.beproc.2019.103890](https://doi.org/10.1016/j.beproc.2019.103890)) | What most reliably triggers an immediate mode TRANSITION is a sudden CHANGE in threat state on top of an ongoing one, not absolute magnitude alone — and the defensive system resists moving toward its most extreme mode (asymmetric with appetitive systems), so "more harm signal → ever more drastic response" is not a safe default assumption. |

**Read together**: the biological target is not "pick a threshold" XOR "pick a smooth weight." It is (a) a continuously graded harm signal, (b) feeding a threshold-crossing (or small-number-of-discrete-regime) categorical decision about HOW to select, which (c) also continuously scales the MAGNITUDE/vigour/urgency of whatever gets selected, and (d) is more reliably triggered by a CHANGE/surprise in the harm signal than by its absolute level alone.

## Verdict on Q2 — three threat features beyond magnitude, each requiring a distinct additional input

| Feature | Evidence | REE mapping |
|---|---|---|
| **Imminence / proximity** (spatial+temporal) | Master axis of PIC (Fanselow entries) and Mobbs 2007's categorical shift; interacts multiplicatively with magnitude (shift steepest under high anticipated pain) | Already the natural reading of `z_harm_a` itself, if it is scaled by distance/time-to-contact rather than a pure static magnitude. Should NOT be treated as additively separable from magnitude — the entries show an interaction, not two independent terms. |
| **Escapability** (can this option actually reach safety) | Cooper 2016 ([10.1016/j.jtbi.2016.06.023](https://doi.org/10.1016/j.jtbi.2016.06.023)): FID is jointly, sigmoidally determined by distance-to-refuge, relative speed, and path angle — not by danger magnitude alone | A concrete GAP: REE currently has no candidate input analogous to "how likely is THIS tile to reach a safe/low-harm completion." This is structurally separate from `z_harm_a` and would need to be derived from something like the tile's own predicted z_world trajectory / reachability, not sourced from the amygdala pathway at all. |
| **Predictability / certainty** of the harm-predicting cue | Fanselow 2022 (BST, [10.1042/ETLS20220003](https://doi.org/10.1042/ETLS20220003)) and Blanchard & Blanchard 1989 ([10.1016/0278-5846(89)90105-x](https://doi.org/10.1016/0278-5846(89)90105-x)), independently converging | A second candidate companion signal to raw `z_harm_a` magnitude — governs whether the system should widen (diffuse/ambiguous threat → broader, more exploratory candidate consideration, closer to current harm-blind behavior) or narrow (discrete/confirmed threat → committed selection toward one low-harm tile) its selection behavior. Also the feature most associated with a documented PATHOLOGICAL failure mode (below). |

## A concrete functional-form recommendation for `/implement-substrate`

This pull's deliverable is not a bibliography — it is a small number of candidate functional forms, ranked by convergent biological support, for a future implementation session to choose between.

**Recommended default (Form B — two-stage, regime-sensitive)**, in the order `_apply_policy_decomposition` would apply it to each surviving candidate tile:

1. **Graded bias term** (always active): `score_total(tile) = score_structural(tile) - w(h) * harm_penalty(tile)`, where `h` is a function of `z_harm_a`/BLA `threat_scale` and `w(h)` is monotonically increasing in `h` (Cooper 2016's sigmoidal-not-linear finding argues for a saturating/sigmoidal `w`, not a linear one). This is the smooth-weighting component supported by the economic-escape and vigour-scaling entries (Cooper 2016; Evans 2018's vigour half).
2. **Threshold-gated categorical override** (activates only above a high-imminence/high-`h` boundary): when `h` (or, per Fanselow 2019, a rate-of-CHANGE in `h`) crosses a threshold, restrict the candidate set to the single lowest-harm-penalty tile (or a small set within an acceptable-harm bound), overriding ordinary structural-cost scoring — mirroring the PIC's circa-strike mode and Mobbs 2007/Evans 2018's categorical decision-node behavior. Below threshold, all surviving tiles remain eligible under the graded bias alone.
3. **Preserve the existing harm-blind additive recombination as the below-threshold default**, per Evans 2018's freeze-as-fallback finding — do not replace `_apply_policy_decomposition`'s current behavior wholesale; add the override on top of it.

**Rejected alternative (Form A — pure graded weighting, no regime change)**: supported only by the economic-escape entries (Cooper) in isolation; contradicted by the categorical-shift evidence from Mobbs 2007, the mode-dissociation evidence from Hoffman et al. 2022, and the mechanistic threshold evidence from Evans 2018. Not recommended as the sole mechanism, though its bias-term math is a legitimate SUBCOMPONENT of Form B.

**Deferred refinement, not blocking a first buildable version**: an escapability-like second input (structurally separate from `z_harm_a`, per Cooper 2016) and a predictability/certainty companion signal modulating the threshold's persistence (per Fanselow 2022, Blanchard 1989) are both real gaps this pull surfaced but are of secondary priority — `implementation_hint`'s existing scope (extend `AnchorGoalPayload` with a signed harm-valence field, build a ranked-selection step) is buildable and testable with Form B's magnitude-and-imminence-only version alone. Flagging both explicitly so a later iteration is not mistaken for scope creep on the first one.

**A documented failure mode to test for once built** (Fanselow 2022's "sustained threat"): a selection step that, once triggered, never disengages — keeps biasing every subsequent redecomposition toward maximally-defensive tiles even after the harm-predicting condition resolves — is the architectural analog of a real, named pathology in this literature (defensive behavior intruding into contexts where other adaptive behavior should occur). This should be an explicit negative-control acceptance criterion for the eventual Phase-2 falsifier, not just a magnitude/direction check.

---

## Entries summary

| entry_id | source | direction | confidence | primary contribution |
|---|---|---|---|---|
| `..._predatory_imminence_continuum_negative_valence_fanselow2024` | Fanselow & Hoffman 2024 *Am Psychol* | supports | 0.85 | PIC/RDoC framework — categorical-mode scaffold |
| `..._pic_empirical_mode_assessment_hoffman2022` | Hoffman et al. 2022 *Learn Behav* | supports | 0.78 | Empirical dissociation of the three PIC modes (mouse) |
| `..._pic_mode_transition_timing_fanselow2019` | Fanselow, Hoffman & Zhuravka 2019 *Behav Processes* | mixed | 0.68 | What triggers a mode TRANSITION (change > absolute level; asymmetric vs. appetitive systems) |
| `..._sustained_threat_predictability_fanselow2022` | Fanselow 2022 *Emerg Top Life Sci* | supports | 0.72 | Predictability as a distinct threat feature (BST); sustained-threat failure mode |
| `..._prefrontal_pag_imminence_shift_mobbs2007` | Mobbs et al. 2007 *Science* | supports | 0.88 | Strongest evidence for a genuine categorical regime shift with imminence (human fMRI) |
| `..._modelfree_modelbased_defensive_circuits_mobbs2020` | Mobbs, Headley, Ding & Dayan 2020 *TICS* | supports | 0.83 | Highest-fidelity REE-native (MF/MB) computational reframing |
| `..._synaptic_threshold_escape_decision_evans2018` | Evans et al. 2018 *Nature* | supports | 0.87 | Causally-validated dual-coding mechanism: graded in, thresholded choice + graded vigour out |
| `..._escapability_refuge_race_economic_model_cooper2016` | Cooper 2016 *J Theor Biol* | supports | 0.74 | Escapability as a distinct, non-linearly-related feature (economic model) |
| `..._defense_predictability_risk_assessment_blanchard1989` | Blanchard & Blanchard 1989 *Prog Neuropsychopharmacol Biol Psychiatry* | supports | 0.68 | Independent classical anchor for discreteness/predictability |

## Next steps post-pull

1. Rebuild the evidence index (`build_experiment_indexes.py`) so these 9 entries appear in `evidence/literature/INDEX.md`.
2. Update the `SD-hazard-aware-policy-decomposition` entry in `substrate_queue.json` to note the `/lit-pull` prerequisite is satisfied, pointing at this directory (done as part of this same session, narrow structural append).
3. Do NOT touch `claims.yaml` — this pull grounds a future implementation design; it is not evidence for or against MECH-321 itself (per the commissioning instructions).
4. When `/implement-substrate` picks this up: build Form B (graded bias + threshold-gated override + preserved default), with the escapability and predictability refinements explicitly deferred rather than silently dropped.
