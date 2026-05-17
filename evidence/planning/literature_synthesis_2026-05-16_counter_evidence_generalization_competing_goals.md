# Literature synthesis — counter-evidence, generalization tolerance, goal competition (GAP-3 env-extension sub-questions)

- Date: 2026-05-16
- Scope: biology-before-formal-definition grounding for three open sub-questions in
  [causalgridworldv2_env_extensions_spec.md](./causalgridworldv2_env_extensions_spec.md)
  (`commitment_closure:GAP-3` Phase 3 env infrastructure).
- Sources: PubMed (attributed inline); WebSearch fallback for the
  behavioural-economics sub-question per the empty-PubMed rule.
- Claim-tagged entries written: MECH-268 x2 (see
  `evidence/literature/targeted_review_connectome_mech_268/`). Q-1b and
  Q-3b sources are methodological grounding for an env primitive, not
  evidence for a specific REE claim, so they are recorded here only
  (honest per the lit-pull claim-tagging rule).

---

## Q-2a (PRIMARY) — operationalising "counter-evidence against a persistent rule_state"

**Question.** For EXP-0164 (SD-034 closure operator vs MECH-268 dACC
pe-saturation under sustained contradiction), should the env inject
counter-evidence as (i) a signed reward/harm perturbation at the
committed target, (ii) a contingency reversal / identity flip, or
(iii) contingency degradation (the committed action loses validity as a
predictor of the committed outcome)?

**Evidence.** According to PubMed:

- Piquet, Faugère & Parkes (2023), *Current Biology*
  ([DOI](https://doi.org/10.1016/j.cub.2023.11.036)): adapting to
  instrumental contingency degradation requires a vHPC->mPFC pathway and
  is, psychologically, an inability to discern *the relative predictive
  validity of the action versus the context*. Degradation depends on
  intact context-outcome learning. (i)/(ii)/(iii) are dissociable
  manipulations recruiting partly different circuitry.
- Dutech, Coutureau & Marchand (2011), *J Physiol Paris*
  ([DOI](https://doi.org/10.1016/j.jphysparis.2011.07.017)): a low-gain
  TD model reproduces normal vs medial-PFC-lesioned degradation; the
  lesion deficit is specifically the *inability to detect weak
  contingency changes*. The measured quantity is the weak/strong
  boundary, not the response to one contradicting event.

**Env-design recommendation.** Operationalise counter-evidence as
**(iii) graded contingency degradation** against the persistent
rule_state — the committed action progressively loses validity as a
predictor of the committed outcome while the surrounding context is held
constant — **not** as a one-shot signed perturbation (i) and **not** as
an identity flip / reversal (ii). Two corollaries for the spec:
1. Counter-evidence **dose and duration must be first-class, sweepable
   parameters**, because EXP-0164's discriminating regime is *sustained*
   contradiction (where a saturation-cap and a low-gain integrator make
   opposite predictions); a fixed single injection cannot resolve the
   MECH-268-vs-SD-034 dissociation.
2. The contradiction must be *relative to an unchanged context* (the env
   must not co-vary the background when it degrades the action), or the
   readout confounds contingency degradation with context change.

This revises the spec's prior default (Q-2a took the simpler signed
perturbation): the perturbation form is **rejected on biological
grounds**; degradation with tunable dose/duration is adopted.

---

## Q-1b — tolerance-band metric: isotropic vs city-block, hard vs graded

**Question.** Should the "completion within tolerance T of the goal"
region be isotropic (Chebyshev/Euclidean) or city-block (Manhattan), and
hard-threshold or graded?

**Evidence.** According to PubMed:

- Shepard (1987), *Science*, "Toward a universal law of generalization"
  ([DOI](https://doi.org/10.1126/science.3629243)): generalization
  probability decays **exponentially (concavely) with distance** in
  psychological space, under **one of two metrics depending on the
  relation between the stimulus dimensions** — Euclidean (isotropic)
  when the dimensions are *integral*, city-block (Manhattan) when they
  are *separable*.
- Marjieh, Jacoby, Peterson & Griffiths (2024), *J Exp Psychol Gen*
  ([DOI](https://doi.org/10.1037/xge0001533)): the universal law (concave
  exponential decay) holds in a high-dimensional naturalistic regime
  (>600k judgments), i.e. graded-concave generalization is not an
  artefact of toy low-dimensional stimuli.

**Env-design recommendation.** Spatial (x, y) location is a single
*integral* percept, not two separable feature dimensions — Shepard's law
prescribes the **Euclidean / isotropic** metric, not Manhattan. On an
8-neighbour grid the **Chebyshev** metric is the discrete isotropic
approximation, so the spec's Chebyshev default is correct and Q-1b is
resolved in its favour (Manhattan rejected on grounds of dimensional
integrality). Second, the universal law says generalization is **graded
and concave, not a hard threshold**. The spec should therefore expose an
optional **graded (exponential-decay) tolerance kernel** — completion
probability / credit decaying as `exp(-d / lambda)` inside the band —
with the hard-threshold band as the default and the graded kernel a
config option for behavioural arms that need a biologically faithful
generalization gradient. A hard band remains acceptable as the
*default* (it is the conservative, deterministic, contract-testable
choice), but the graded kernel should exist because EXP-0156/0162-class
arms that probe generalization shape will need it.

---

## Q-3b — competing-goals primitive: replace-on-early-consume vs invalidate-episode

**Question.** If one of the two simultaneously-active competing cues is
consumed before the minimum both-active window, is re-placing it (to
honour the window) a valid operationalisation, or a confound for the
MECH-266 competing-goals / mode-stickiness measurement?

**Evidence.** PubMed is sparse here (this is a
behavioural-economics/conflict-paradigm methodology question, not a
biomedical-indexed one); WebSearch returned only generic
approach-approach-conflict material. No canonical empirical paper
adjudicates mid-conflict replenishment. This sub-question is therefore
resolved on **measurement-validity reasoning**, not literature:

- The dependent measure for EXP-0160/0163 is *behaviour under sustained
  simultaneous competition* (which cue wins, and how sticky the mode is
  once committed). Re-placing a consumed cue mid-episode makes the
  choice set **non-stationary and contingent on the agent's own prior
  choice** — the replacement only happens *because* the agent took the
  other (or the same) option. That is a classic reactive-measurement
  confound: the manipulation becomes a function of the behaviour it is
  meant to measure, and "mode stickiness" can no longer be cleanly
  attributed to the agent vs the env-induced re-presentation.

**Env-design recommendation.** Prefer **invalidate-episode** over
replace-on-early-consume: if a cue is consumed before
`dual_cue_min_active_ticks`, mark the episode as not meeting the
competing-goals precondition and exclude it from the EXP-0160/0163
analysis cohort, rather than re-placing the cue. Keep
`dual_cue_replace_on_early_consume` as a config flag but **flip its
default to False** (invalidate) and document that the True path is a
diagnostic/relaxation mode only, not for the MECH-266 measurement. This
trades sample efficiency for measurement validity — the right trade for
a load-bearing behavioural arm. (If early-consume invalidation discards
too many episodes in practice, the correct fix is to make the two cues
harder to reach within `dual_cue_min_active_ticks`, not to re-place
them.)

---

## Net effect on the spec

| Sub-Q | Prior spec default | Resolved | Basis |
|---|---|---|---|
| Q-2a | signed perturbation at target | **contingency degradation, dose+duration sweepable, context held constant** | Piquet 2023 + Dutech 2011 (MECH-268 entries) |
| Q-1b | Chebyshev, hard band | **Chebyshev confirmed (integral dims); add optional graded exp-decay kernel** | Shepard 1987 + Marjieh 2024 |
| Q-3b | replace-on-early-consume=True | **invalidate-episode (default flip to False)** | measurement-validity reasoning (no canonical lit) |

These resolutions are propagated into
`causalgridworldv2_env_extensions_spec.md` (sections 3, 2, 4 and the
open-questions section) and noted in the `commitment_closure_plan.md`
decision log.
