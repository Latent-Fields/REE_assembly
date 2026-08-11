---
nav_exclude: true
---

# Thought Intake: Behavioural Diversity -- We Never Needed a Ruler, We Needed an Umpire

**Raw thought file:** `docs/thoughts/2026-08-11_behavioural_diversity_umpire.md`
**Session:** jovial-shannon-35d300, 2026-08-11
**Status:** processed, candidate claim DRAFTED not yet registered (claims.yaml contended --
see "Candidate claims" below)

---

## Verbatim prompt

See `docs/thoughts/2026-08-11_behavioural_diversity_umpire.md` for the full text (reproduced
there verbatim). Core reframing, condensed: replace the question "how much behavioural
diversity does REE exhibit" (a scalar) with "can we reliably distinguish different forms of
organised behaviour emerging in response to different ecological problems" (a discriminability
test -- an "umpire," not a "ruler"). Proposes: environment-conditioned behavioural signatures
built from trajectory-derived features without pre-specifying which feature constitutes
"strategy"; a held-out classifier ("umpire") testing whether Environment A and Environment B
produce distinguishable signatures; an orthogonal-perturbation selectivity check; and a strict
separation between demonstrating that organisations differ (measurement) and interpreting that
difference as strategy (later, human judgement).

---

## What's New vs. Existing REE Docs (novelty table)

| Existing doc/claim | What it already covers | What this thought adds |
|---|---|---|
| `behavioral_diversity_acceptance_criteria.md` (Rungs 0-4, `ARC-065`/`ARC-062`/`MECH-313`/`MECH-314`/`MECH-269`) -- the plan-of-record for diversity governance | A rigorous, FP-taxonomy-guarded (FP-1..FP-5) **ladder of pre-specified scalar/bivariate metrics**: action entropy (Rung 0), trajectory-class count (Rung 1), total-variation distance between two hand-picked probe states within ONE environment (Rung 2), persistence after training/sleep (Rung 3), harm/goal separation reaching the ethics layer (Rung 4). Rung 2's TV-distance-plus-ablation test is the closest existing analog to the thought's core idea -- but the compared "conditions" are two probe STATES inside the same SD-054 map, the feature is fixed in advance (action distribution), and necessity is tested by ablating the AGENT'S substrate (MECH-313/314/260), not by perturbing the ENVIRONMENT. | **(a)** A single, general, feature-agnostic discriminability test over a MULTIVARIATE trajectory-segment signature (refuge occupancy, excursion structure, hazard relationships, transitions, spatial distribution, etc. jointly) rather than one pre-chosen scalar/bivariate metric per Rung. **(b)** Comparison is CROSS-ENVIRONMENT (two genuinely different ecological problems), not within-environment probe-state comparison -- closer to a generalisation/transfer test than Rung 2's context-switching test. **(c)** Explicit held-out generalisation discipline (train/test split on unseen episodes/seeds) -- the Rung framework's thresholds are evaluated on the same data that motivated them, with no stated train/held-out split. **(d)** An orthogonal-perturbation SELECTIVITY check on the ENVIRONMENT side (does the signature move only along the perturbed axis) -- the Rung framework's only analogous check is agent-SUBSTRATE ablation (necessity), never an environment-side specificity probe. **(e)** Strategy interpretation explicitly deferred to a second, separate step post-discrimination -- the Rung framework does not separate these two steps as sharply (Rung labels like "state-contingent strategy switching" name the interpretation inside the metric definition itself). |
| `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` -- the retrospective analysis of the **same reef visualisation** the thought is responding to | Ad hoc, hand-designed statistical tests applied to the 906 lineage: ground-truth `in_reef` excursion inventory, harm-rate-in-vs-out-of-reef ratio, distance-controlled threat-triggered-return correlation, opportunity-triggered-exit correlation. **Conclusion reached the same day:** the phenotype the human observer found visually organised is "closer to passive exploitation of a genuinely protective zone without demonstrated contingent control" than genuine discriminative strategy, and is attributed to the *already-diagnosed* `MECH-309` (monomodal collapse without a rule-apprehender) landing on the safety pole of the two designed attractors -- not treated as a fresh finding. | **This is, in substance, a hand-run, low-powered, univariate/bivariate precursor of exactly the "umpire" the thought proposes** -- run on the identical data the thought's visual impression came from. Its own correlational sub-tests (1b-C depth/harm correlation, 1b-D opportunity-exit, 1b-E threat-return) are individually weak/inconsistent, which is precisely the failure mode a joint multivariate classifier is designed to be more sensitive to (many correlated weak signals can jointly discriminate even when no single one clears a threshold). **The thought's proposal is therefore best read as "run the properly-powered version of the test this review already attempted by hand and found inconclusive," not as an unrelated new direction.** It does not, by itself, contradict the review's negative-leaning verdict -- it raises the evidential bar on both sides (a positive umpire result would need to survive the same FP taxonomy the review already applied by hand; a negative umpire result would strengthen `MECH-309` well beyond what six univariate correlational sub-tests can). |
| `ARC-062` (context-discriminator gated-policy architecture) | A "learned context discriminator emitting a soft gate" -- but this is a **component of the agent's own policy**, trained end-to-end jointly with behaviour, whose job is to CAUSE mode-switching, not to MEASURE whether switching occurred. | The thought's "umpire" is architecturally the opposite kind of object: an **external, offline, held-out evaluator with no causal role in behaviour generation** -- a measurement instrument, not a generative mechanism. Confirmed via code survey: nothing in `ree_core/` implements this external-evaluator pattern for trajectories; `ARC-062`'s discriminator and the thought's umpire share a name-adjacent concept (discrimination) but sit on opposite sides of the generate/measure boundary. Worth stating explicitly so the two are never conflated when this claim is discussed. |
| `MECH-191` (`v3_exq_686_mech191_signal_state_discriminability.py`) | A held-out **logistic classifier**, PASS = accuracy >=70%/class above chance, predicting which internal functional state (WANTING/NOCICEPTION/FRUSTRATION) produced a signal vector. | This is the closest existing REUSABLE PATTERN for the umpire's statistical machinery (classifier-based discriminability with a chance-level bound) -- but it classifies **internal signal vectors**, not **behavioural trajectory segments across environments**. Its code is the natural starting point for the umpire's classifier harness (see "Next steps"). Confirms the classifier-as-discriminator pattern is not foreign to this codebase's experiment style; it has simply never been pointed at cross-environment trajectory data. |
| `MECH-439` (F-dominance conversion ceiling) / `MECH-442` (behavioural-descriptor committed-selection archive, Quality-Diversity/MAP-Elites) | The primary harm/goal score F monopolises ~88-89% of E3 committed-selection variance; per-candidate diversity generated upstream (`ARC-065`, `MECH-341`) collapses at the committed argmax. `MECH-442` is the parked candidate fix (a MAP-Elites-style behavioural-descriptor archive upstream of the commit). | Not new, but load-bearing context: **even a well-built umpire may currently return a weak or null result for reasons that have nothing to do with whether the umpire methodology itself is sound.** If committed-action diversity is architecturally capped before it ever reaches the trajectory level, a null cross-environment discriminability result should be read as corroborating `MECH-439`, not as refuting the "umpire, not ruler" reframing. This caveat should travel with any experiment run against the new candidate claim (see below). |
| `ree_core/environment/causal_grid_world.py` reef mode (`SD-054`) -- code-level, not doc-level | The reef substrate's own docstring literally names it a "Behavioral diversity substrate," built specifically so reef-approach vs forage-approach trajectories diverge for CEM-candidate distinguishability (`V3-EXQ-543b`). Existing tunable knobs: `reef_enabled`, `n_reef_patches`, `reef_patch_radius`, `hazard_food_attraction`, `reef_scent_sigma`. | Confirms the two-condition contrast the thought asks for (a "substantially different environment") and a usable orthogonal-perturbation knob (`hazard_food_attraction`, or `reef_patch_radius`) already exist as config flags on the SAME validated substrate -- no new environment needs to be built for a first pass (see "Next steps"). |

**Net assessment:** the reframing itself ("distinguishability, not magnitude" / "umpire, not
ruler") is genuinely new **terminology and emphasis**, not previously named anywhere in the
repo (`grep` across `claims.yaml`, `docs/architecture/`, `docs/thoughts/`, `evidence/planning/`
and `ree_core/` found zero occurrences of "umpire"). But the underlying methodological
instinct -- that context-conditioned discriminability matters more than scalar magnitude -- is
**already partially present** in Rung 2 (TV-distance + ablation) and already **hand-attempted,
the same week, on the exact data that motivated this thought** (the 2026-08-10 reef review).
What is genuinely new relative to both: (1) a feature-agnostic multivariate signature instead
of one pre-chosen scalar per Rung; (2) cross-environment rather than within-environment
comparison; (3) explicit held-out generalisation discipline; (4) an environment-side
orthogonal-perturbation specificity check, which the existing framework has no analog of at
all (its only specificity-adjacent check is agent-substrate ablation); (5) a sharp two-stage
separation of measurement from interpretation. This is a **methodological refinement and
generalisation of Rung 2**, not an unrelated new direction, and not merely a renaming of
existing work.

---

## Key formulations

1. **Reframe the target metric.** Not `H(behaviour)` (a scalar) but
   `Discriminable(Env_A, Env_B)` (a held-out classifier verdict) -- distinguishability above
   chance is the object of interest, not magnitude of variability.
2. **Signature, not score.** A trajectory-segment feature vector (refuge occupancy, excursion
   structure, food-directed movement, hazard relationships, return behaviour, spatial
   distribution, transition probabilities...) constructed WITHOUT committing in advance to
   which combination constitutes "strategy" -- let the discriminator find the combination, if
   any.
3. **Two-part conservative test, refined from the thought during this intake to close a gap
   the raw thought did not itself name:**
   - **(a) Above-chance:** held-out classifier accuracy vs. a label-permutation null (not a
     bare >50% threshold -- accuracy alone is not a conservative statistic at unconstrained
     sample size).
   - **(b) Above-matched-control:** the SAME classifier pipeline run on trajectories from an
     UNTRAINED / random / fixed-heuristic policy sampled from the SAME two environments.
     **This second control is necessary and was implicit but not stated in the raw thought**:
     two different environments differ in raw geometry/terrain regardless of what any policy
     does inside them (a spatial-occupancy histogram alone would trivially discriminate reef-ON
     from reef-OFF for a RANDOM policy, since the reef literally removes certain cells from the
     hazard/food spawn pool). Requiring the TRAINED policy's discriminability to exceed the
     control policy's discriminability is the direct cross-environment analog of Rung 1's
     matched-entropy-random-walk control and Rung 2's ARC-065-ablation control -- without it,
     "the umpire says A and B differ" could just be re-discovering that A and B are different
     ENVIRONMENTS, which is not a claim about REE at all.
4. **Orthogonal-perturbation selectivity.** Perturb something that does NOT change the
   qualitative ecological problem (a nuisance axis) and confirm the discriminator's verdict is
   comparatively stable to it, while remaining sensitive to the real ecological-problem axis.
   This is the one check with no existing analog anywhere in the current framework.
5. **Strict two-stage separation, made explicit during this intake:**
   - **Stage 1 (measurement, agnostic):** does discriminability clear both (3a) and (3b), and
     survive (4)? This alone establishes "context-sensitive behavioural differentiation
     exists" as a bare statistical fact -- no claim about goals, adaptiveness, or "strategy" is
     made or needed at this stage.
   - **Stage 2 (interpretation, human-in-the-loop, only after Stage 1 passes):** inspect which
     features the classifier weighted most heavily (coefficients / permutation importance /
     partial dependence) to produce a human-readable gloss of what the signature consists of.
     Only at this stage does a team choose whether "strategy" is an apt word -- and even then,
     per the existing FP taxonomy, a passing Stage-1 result plus a plausible-looking Stage-2
     gloss is still not itself proof of goal-directed adaptive control (that requires
     substrate-ablation-style causal tests, exactly as Rungs 2/4 already require for their own
     claims).

---

## Affected existing claims

- **`ARC-065`** (behavioural-diversity generation pathway) -- unaffected in status; the umpire
  is a candidate NEW evaluation instrument that could eventually feed evidence toward `ARC-065`
  promotion criteria (Rung 1/2), not a replacement for them.
- **`ARC-062`** (context-discriminator gated policy) -- unaffected in status; clarified above
  that its "discriminator" and the thought's "umpire" are different kinds of object
  (generative mechanism vs. external measurement) and should not be conflated in future
  writeups.
- **`MECH-309`** (monomodal collapse without rule-apprehender) -- unaffected in status; the
  2026-08-10 reef review's verdict (current phenotype consistent with `MECH-309`, not with
  genuine contingent strategy) stands. This intake does not overturn that verdict; it proposes
  a higher-powered test of the same question the review already asked by hand.
- **`MECH-439`/`MECH-442`** (F-dominance ceiling / QD archive) -- unaffected in status; flagged
  as the interpretive caveat a null/weak umpire result should be read against before being
  taken as evidence against the reframing itself.
- **`MECH-191`** (internal-state discriminability classifier) -- unaffected in status; cited as
  the reusable code pattern for the umpire's classifier harness.
- **`SD-054`** (reef substrate) -- unaffected in status; identified as already carrying both the
  two-condition contrast and an orthogonal-perturbation knob needed for a first-pass experiment,
  with no new environment engineering required.

No existing claim's evidence, status, or confidence was altered by this intake -- purely
additive, same as prior intakes of this shape.

---

## Candidate claims

**DRAFTED, NOT YET REGISTERED.** `claims.yaml` is under an active contended claim
(`fishtank-affect-telemetry-1aba08`, opened 2026-08-11T17:02:47Z, task: "Clamp/decay
`RBFLayer.update_valence()` unbounded accumulator") for the duration of this session's work;
`task_claim.py open` arbitration confirmed that session as owner and this session as NOT
owner when both named `claims.yaml` (checked 2026-08-11T17:46Z). Per the thought-intake
discipline this is a genuine resource-contention deferral, not a "future registration" prose
punt -- the exact YAML block below is ready to paste as soon as the contention clears; it is
recorded here specifically so registration is a five-minute mechanical follow-up, not a
research task, for whichever session does it next (this session, if it clears before close;
otherwise the next `/governance` or thought-digestion pass).

```yaml
id: Q-092   # VERIFY max Q-id at registration time; do not trust this number if time has passed
title: "Does a held-out, permutation-tested classifier ('umpire') over a multivariate
  trajectory-segment feature signature (refuge occupancy, excursion structure, hazard
  relationships, transitions, spatial distribution) detect context-sensitive behavioural
  differentiation between SD-054 reef-ON and reef-OFF conditions -- above BOTH a permutation
  null AND a matched untrained/random-policy control -- and does that differentiation show
  selective sensitivity to the reef-presence axis specifically, as distinct from an orthogonal
  nuisance perturbation (e.g. hazard_food_attraction magnitude)?"
claim_type: open_question
subject: measurement.behavioural_diversity.cross_environment_discriminability_umpire
polarity: open
status: open
epistemic_category: standard
implementation_phase: v3
claim_level: mechanistic
registered_utc: "2026-08-11"
depends_on:
  - ARC-065     # diversity-generation pathway the umpire would be evaluating evidence about
  - ARC-062     # context-discriminator architecture -- distinguished, not conflated, in notes
  - MECH-309    # current best diagnosis of the reef phenotype the raw thought responded to
  - MECH-439    # F-dominance ceiling -- interpretive caveat for a null/weak umpire result
  - MECH-191    # reusable classifier-discriminability code pattern
  - SD-054      # substrate supplying both the two-condition contrast and the perturbation knob
notes: >
  Raw thought: docs/thoughts/2026-08-11_behavioural_diversity_umpire.md.
  Structured intake: evidence/planning/thought_intake_2026-08-11_behavioural_diversity_umpire.md
  (full novelty comparison, methodology refinement, and minimal-experiment design).

  This is a MEASUREMENT-layer claim, not an architecture claim: it asks whether a specific
  evaluation methodology (cross-environment classifier discriminability, held-out, permutation-
  tested, matched-control-guarded, orthogonal-perturbation-checked) detects structure that the
  existing behavioral_diversity_acceptance_criteria.md Rung-2 test (within-environment TV
  distance at two hand-picked probe states) does not test for. A PASS would strengthen the
  evidential case that reaches ARC-065/ARC-062 Rung 1/2, not substitute for their own
  acceptance criteria. A null/weak result should be interpreted jointly with MECH-439
  (F-dominance ceiling) before being read as evidence against the reframing itself -- see
  thought_intake_2026-08-11_behavioural_diversity_umpire.md "Affected existing claims."

  DO NOT treat a positive result alone as evidence of "strategy" -- Stage 1 (discriminability)
  and Stage 2 (feature-importance interpretation) are deliberately kept separate per the
  intake's "Key formulations" #5; a Stage-2 gloss still requires the existing FP taxonomy
  (behavioral_diversity_acceptance_criteria.md) before any adaptive-control claim is made.
evidence_quality_note: >
  Proposed 2026-08-11 from user thought intake. No experimental evidence yet. Minimal
  experiment design in thought_intake_2026-08-11_behavioural_diversity_umpire.md "Next steps."
location: evidence/planning/thought_intake_2026-08-11_behavioural_diversity_umpire.md
```

No other genuinely-new candidate claims were identified; the rest of the thought's content
(the two-stage measurement/interpretation separation, the matched-control refinement) is
methodology supporting this one open question, not a separate claim.

---

## Next steps

1. **Register Q-092 (verify id) into `claims.yaml`** once the current contention on that file
   clears -- mechanical, the YAML block above is ready. `build_claims_json.py` after.
2. **Minimal experiment, smallest version that tests the idea convincingly** -- deliberately
   reuses existing validated substrate and code rather than building anything new:
   - **Conditions.** Env-A = `SD-054` reef `reef_enabled=True` (current default config).
     Env-B = the SAME substrate with `reef_enabled=False` (already-supported flag; zero new
     environment code). This is a genuinely different ecological problem (no shelter,
     continuous exposure) rather than a cosmetic variant.
   - **Policies.** Train (or reuse existing trained checkpoints if available for both
     conditions) the same architecture/hyperparameters separately in each condition, >=3 seeds
     each (matching the existing Rung-2 seed-count convention).
   - **Held-out split.** Fit any feature normalisation / classifier only on a subset of
     episodes per seed; evaluate on a disjoint, never-touched set of episodes (or, if seeds
     permit, hold out an entire seed per condition) -- this is the discipline the existing
     Rung framework does not state explicitly and this thought's proposal specifically adds.
   - **Features.** Reuse, do not reinvent: the 2026-08-10 reef review already computes most of
     the needed statistics (per-episode `in_reef` fraction, excursion count/duration/depth,
     harm-rate in/out of reef, zone-transition rate, spatial-occupancy histogram). Build the
     trajectory-segment feature vector from that existing instrumentation.
   - **Classifier.** A simple, interpretable model (logistic regression or a shallow
     gradient-boosted-tree ensemble) -- reuse the harness pattern from
     `experiments/v3_exq_686_mech191_signal_state_discriminability.py` (the codebase's one
     existing classifier-as-discriminator experiment) rather than writing a new one from
     scratch.
   - **Test (3a).** Held-out accuracy vs. a label-permutation null (shuffle env-A/env-B labels
     across episodes, refit+reevaluate N times, compare observed accuracy to that null
     distribution).
   - **Control (3b).** Same pipeline, same two environments, but trajectories from an
     untrained / random-action policy (or the existing hand-coded reef-aware heuristic
     mentioned in `V3-EXQ-522`'s own design note) instead of the trained agent. Trained-policy
     discriminability must exceed this control's by a pre-registered margin.
   - **Selectivity (4).** Re-run held-out evaluation on episodes from a mildly perturbed
     Env-A (`hazard_food_attraction` shifted by a modest amount, or `reef_patch_radius` +/-1 --
     both already-existing config knobs on the same substrate, no new environment needed) and
     confirm the discriminator trained on the ORIGINAL Env-A/Env-B contrast still classifies
     these as "A" at a comparably high rate (the signature is robust to a nuisance
     perturbation, not merely fit to one specific instantiation).
   - **PASS bar.** (3a) exceeds permutation null AND (3b) trained policy exceeds matched
     control AND (4) selectivity holds. Any one failing should be reported as which stage
     failed (this generalises the existing Rung framework's own "classify which Rung/FP
     failed" discipline, per `behavioral_diversity_acceptance_criteria.md`).
   - **Interpretation, only after PASS.** Feature-importance / coefficient inspection to name
     which components of the signature the classifier relied on -- reported as a descriptive
     gloss, explicitly not yet a claim of adaptive strategic control.
3. **Do not queue this experiment via `/queue-experiment` yet.** Per the non-degeneracy
   discipline this codebase applies to every other diversity claim, first confirm SD-054
   reef-ON/reef-OFF trained-agent runs with sufficient episode counts for the held-out split
   already exist or are cheap to produce, and check whether `MECH-439`'s F-dominance ceiling
   is expected to leave enough committed-action diversity at the trajectory level for the
   umpire to have anything to detect in the FIRST place -- a run attempted before that
   precondition is understood risks reproducing the same
   `substrate_not_ready_requeue`/non-informative-null pattern already seen elsewhere in this
   claim cluster (see `MECH-488`'s and `Q-046`'s own precondition language for the house style
   on this).
4. **Do not amend `behavioral_diversity_acceptance_criteria.md` in this pass.** That file is
   the plan-of-record and a natural home for a new "Rung 2b" / companion section describing
   this methodology once Q-092 is registered and a first PASS/FAIL result exists -- but editing
   it now would be a second, unclaimed `evidence/planning/` resource touched outside this
   session's opened claim scope. Flagged as a follow-on, not performed here (Scope Discipline).
5. No lit-pull performed for this intake -- the methodology (classifier two-sample test with a
   permutation null) is standard statistics/ML practice, not a REE-specific biological claim
   requiring citation-backed grounding the way `INV-074` did.
