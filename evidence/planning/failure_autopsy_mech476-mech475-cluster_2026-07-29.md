# Failure Autopsy — cluster: V3-EXQ-836, V3-EXQ-836c (MECH-476), V3-EXQ-837 (MECH-475)

Generated: `2026-07-29T20:23:19Z`
Scope: cluster (shared substrate/lineage: MECH-457 competence-bootstrap decomposition,
`experiments/_lib/baselines/mech457_retention.py` lineage)
Session: `silly-mayer-a60957` (worktree)

Dry-run check (Step 2a): `scripts/check_dry_run_citations.py` on all three run_ids —
**0 dry cited, 0 in named families, 0 ambiguous, 3 clean.** All three carry `dry_run: false`
verified directly on the manifest. None are smokes.

Recording provenance (Step 2b): `ree-v3/validate_recording.py --paths` on all three manifests —
**3 complete, 0 always-core gaps, 0 thin-pack drops, 0 schema warnings.** `substrate_hash`,
`config`, `seeds`, `machine`/`machine_class`, `elapsed_seconds` all present on all three. No
recording-debt.

---

## 1. Facts reconstruction

### 1a. V3-EXQ-836 — MECH-476 DOSE arm

**Manifest**: `v3_exq_836_mech476_dose_dependent_consolidation_20260729T092449Z_v3`. `outcome:
FAIL`, `evidence_direction: mixed`, `non_degenerate: true`. `interpretation.label:
non_monotone_dose_response`. Load-bearing criterion `resistance_grows_with_dose`: `passed: false`.

Three dose arms (BC-install episodes 300/600/900), n=6 seeds each (42-47), all three arms
`gate_green: true` (install_took_strict_majority precondition measured 1.0 vs 0.5 threshold on
every arm — no readiness problem).

`dose_response`: `retained_fraction_mean_axis = [0.5877 (300), 0.2867 (600), 0.4226 (900)]`,
`spread = 0.3010`, `monotone_non_decreasing: false`, `resistance_dose_margin: 0.15` (a **fixed**
absolute floor, not scaled to observed noise), `non_monotone: true`.

**Per-seed spread is large relative to the between-arm signal the verdict rests on.** Recomputed
directly from `per_arm[*].retained_fraction_per_seed`:

| Arm | mean | SD | SEM (n=6) |
|---|---|---|---|
| dose_bc300 | 0.5877 | 0.3679 | **0.1502** |
| dose_bc600 | 0.2867 | 0.1358 | 0.0555 |
| dose_bc900 | 0.4226 | 0.1451 | 0.0592 |

dose_bc300's own SEM (0.150) is comparable in magnitude to the between-arm deltas the
non-monotone verdict is read from (300-600 delta 0.301, 600-900 delta 0.136, 300-900 delta 0.165).
The dose_bc300 arm's high mean is driven substantially by one seed at `retained_fraction=1.274419`
(post_bc=10.75 -> terminal ~13.7, i.e. RL refinement *improved* on the BC install for that one
seed) against five siblings in the 0.259-0.637 range. `RESISTANCE_DOSE_MARGIN = 0.15` is a fixed
literal in the script (`v3_exq_836_...py:134`), not derived from `sd_delta` — this is a direct
instance of the project's own documented effect-size-gate convention violation (scale noise on the
SD of the delta between arms plus an absolute floor; never a bare fixed number).

### 1b. V3-EXQ-836c — MECH-476 NOVELTY-TAGGING arm

**Manifest**: `v3_exq_836c_mech476_novelty_tagging_consolidation_20260729T181956Z_v3`. `outcome:
FAIL`, `evidence_direction: mixed`, `non_degenerate: true`. `interpretation.label:
reversed_novelty_effect`. Load-bearing criterion `paired_retains_more_than_unpaired`: `passed:
false`.

Two arms (`novelty_paired`, `novelty_unpaired`), fixed weak BC dose = 150 episodes (deliberately
sub-threshold per the Moncada & Viola 1997/2007 behavioural-tagging paradigm the arm is modelled
on), n=6 seeds each, both `gate_green: true`. `novelty_contrast`: `paired_retained_fraction_mean =
0.8441`, `unpaired_retained_fraction_mean = 1.1327`, `delta = -0.2886`, `margin = 0.15`,
`reversed: true`.

**The entire reversal is attributable to one outlier seed.** `novelty_unpaired`'s per-seed
`retained_fraction`: `[1.1667, 0.6293, 0.1826, 2.7671, 1.3582, 0.6923]`. The fourth value
(post_bc=3.65 -> terminal ~10.10) is 2-15x every sibling in the same arm (SD of the full arm =
0.9026, vs 0.3347 for the paired arm — 2.7x). Removing it: `unpaired mean(n=5) = 0.8058`, so
`paired - unpaired = 0.8441 - 0.8058 = +0.0383` — the *direction reverses back* to (weakly) SUPPORT
the paired-retains-more prediction, and the magnitude sits well inside the 0.15 margin either way.
The reversal is not robust to a single seed; it does not survive a leave-one-out check.

### 1c. V3-EXQ-837 — MECH-475 distributional-critic iatrogenic-reversal falsifier

**Manifest**: `v3_exq_837_mech475_distributional_critic_iatrogenic_falsifier_20260729T141738Z_v3`.
`outcome: FAIL`, `evidence_direction: weakens`, `non_degenerate: true`.
`interpretation.label: iatrogenesis_persists_under_informative_baseline`.

Three families (capacity=769 capacity/budget, approach=781 approach-drive, metabolic=771
metabolic-coupling), each with a scalar-critic control/treatment pair and a distributional-critic
control/treatment pair, n=3 seeds per family. Readiness gates, per family: `env_local_view_clears_
floor` (positive control the env is solvable), `scalar_control_competent` (**the load-bearing
non-degeneracy guard** — a control at floor cannot exhibit a treatment-below-control inversion),
`scalar_inversion_reproduces` (the original destructive phenomenon must reproduce on this build),
`trajectory_readings` (>=2 probe readings).

`capacity` and `approach` clear every gate (`scalar_control_competent` measured 4.64 vs floor 1.0;
`scalar_inversion_reproduces` measured 4.45/4.44 vs margin 1.0). `metabolic` **fails**
`scalar_control_competent` (measured 0.9056 vs floor 1.0) and is correctly excluded —
`n_scorable_families: 2`, not 3.

`discrimination_verdict.per_family_reverses_or_flattens`: `capacity: false, approach: false,
metabolic: false`. `per_family_scalar_inversion_mean`: capacity 4.45, approach 4.44.
`per_family_dist_inversion_mean`: capacity **15.13**, approach **14.90** — the distributional
critic's inversion is *3.4x larger* than the scalar critic's in both scorable families, i.e. the
"informative baseline" treatment made the destructive competence-below-control effect **worse**,
not reversed or flattened, on every seed of both scorable families (`per_seed.reverses_or_
flattens: false` x6).

**Script**: `ree-v3/experiments/v3_exq_837_mech475_distributional_critic_iatrogenic_falsifier.py`.
Modelled on the same three destructive instances (769/781/771) that motivated MECH-475's
registration, now re-run with V3-EXQ-788's distributional critic substituted for the scalar one,
holding everything else byte-identical to the destructive-treatment build.

**Queue entry**: `V3-EXQ-837`, `experiment_purpose: evidence`. No `supersedes` — first real test of
MECH-475's own decisive REVERSAL prediction.

**Expected vs observed**: MECH-475's `what_would_answer` (a) states explicitly: *"SUPPORTED if the
treatment-below-control inversion REVERSES OR FLATTENS in at least 2 of 3. WEAKENED if treatments
still land below their own controls with an informative baseline — the destructiveness is then not
the baseline's doing and this claim is WITHDRAWN (it does not degrade into a weaker version; the
whole content is the causal attribution)."* Observed: 0 of 2 scorable families reverse or flatten;
both get *worse*. **Failed criterion: discrimination** (the reversal test), on a fair,
non-degenerate, readiness-gated design.

---

## 2. Claim-layer map

### MECH-476 (`competence_retention_dissociable_from_acquisition`)

`claim_type: mechanism_hypothesis`, `status: candidate`, `v3_pending: true`,
`implementation_phase: v3`, `epistemic_category: standard`, `split_from: MECH-457`,
`depends_on: [MECH-457, MECH-459, MECH-460, MECH-475]`. Registered 2026-07-22 by
`/claim-synthesis`. `what_would_answer` names three arms: DOSE (836, this run), INTERVAL (836b,
still running on ree-cloud-3 as of this autopsy), NOVELTY (836c, this run). SUPPORTED requires
monotone growth with dose/interval; WEAKENED requires invariance to both; **the script itself
pre-registers a third bucket, NON-MONOTONE, for "a real but uninterpretable dose effect... routes
to `/failure-autopsy` rather than a clean verdict"** — this autopsy is exactly that routing, named
in the driver's own docstring before the run.

**Did the experiment test the claim under conditions where it could express itself?** The DOSE and
NOVELTY *designs* are sound instantiations of the claim's own falsifier spec (Krakauer 2005
over-training paradigm; Moncada & Viola weak-install-plus-novelty paradigm) with every readiness
gate green — the install took, in every arm, on every seed. What failed to let the claim express
itself is **statistical power at n=6 seeds combined with a fixed (non-noise-scaled) discrimination
margin**: retained_fraction is a ratio statistic with high per-seed variance (single-seed values
range 3-15x from their arm-mates in both runs), and the margin used to call SUPPORTED/WEAKENED/
NON-MONOTONE does not account for that variance. This is a measurement/test-design gap in the
*discrimination rule*, not evidence that the underlying dose/novelty relationship is genuinely
non-monotone or reversed.

### MECH-475 (`uninformative_value_baseline_makes_optimisation_iatrogenic`)

`claim_type: mechanism_hypothesis`, `status: candidate`, `v3_pending: true`,
`implementation_phase: v3`, `epistemic_category: standard`, `split_from: MECH-457`,
`depends_on: [MECH-457, MECH-459]`. Registered 2026-07-22. Motivating evidence: five independent
destructive instances (769/781/771/780/789) plus the measured mechanism (V3-EXQ-782 R-(b), an
uninformative critic: `std(V)/std(G) = 0.041` vs 0.25 collapse threshold) and the positive control
(V3-EXQ-788: a distributional critic *retains* competence where a scalar one does not — proving the
baseline swap changes the sign of the outcome on at least one instance).

**Did the experiment test the claim under conditions where it could express itself?** Yes,
cleanly. This is the single decisive test the claim itself names as its highest-value readout,
run on 2 of the 3 named destructive instances (the third, metabolic, correctly self-excluded on
its own non-degeneracy guard rather than being forced into a false reading), with every
readiness/positive-control gate green and the destructive phenomenon confirmed to reproduce on
this build before testing whether the informative baseline fixes it. There is no test-design gap
here to hide behind.

---

## 3. Biological-reference triage

**MECH-476** — closest mechanism: post-training memory consolidation as resistance to retrograde
interference (Krakauer, Ghez & Ghilardi 2005), dose/time-dependent strengthening (over-training,
elapsed offline interval), and behavioural tagging (Moncada & Viola 2007: a sub-threshold install
consolidates when paired with a temporally-close novelty exposure). This is a faithful biological
translation attempt, not a formal-definition import — the falsifier design (dose x interval x
novelty-pairing) is lifted near-verbatim from the cited paradigms. `targeted_review_mech_457_
consolidation` lit-pull is **commissioned but not yet delivered** (claims.yaml notes); the citations
present (Krakauer, Walker 2003, Moncada & Viola, Bin Ibrahim 2024) are strong anchors already on
file, and the claim's own notes record a load-bearing divergence (REE's protection pathways are
awake/online/undifferentiated vs the biology's sleep/replay-dependent, trace-selective mechanisms)
that this run's design is explicitly agnostic to and does not resolve either way.

**MECH-475** — closest mechanism: dopaminergic/striatal value-signal grounding of instrumental
learning. Partially a formal-definition import (the policy-gradient variance-reduction argument,
Sutton et al. 2000, is the theoretical anchor) but grounded in real lesion/depletion literature:
Rothenhoefer et al. 2017 (ventral-striatum-lesioned macaques degrade with an unbaselined-error
signature, not a plateau — the predicted *shape*) and Salamone/Szczypka (dopamine-deficient mice
with intact perception/motor/hedonics starve in front of food — the predicted *floor* phenotype).
The claim's own notes flag an unresolved divergence: the biological lesion effect is specific to
STIMULUS-value learning and spares ACTION-value learning, whereas REE's deficit is on actions. This
autopsy does not resolve that divergence; it tests a narrower, REE-internal causal claim (does
substituting the value estimator reverse the effect) that is orthogonal to it.

---

## 4. Four-layer diagnosis

### V3-EXQ-836 / V3-EXQ-836c (MECH-476)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Design is a fair instantiation of the claim's own falsifier spec; the discrimination rule, not the design, is what fails to resolve it. |
| Biological reference | clear | Krakauer/Moncada/Walker paradigms faithfully instantiated. |
| Developmental / dependency prerequisites | present | MECH-457/459/460/475 all registered; SD-083 offline consolidation substrate landed 2026-07-29, unblocking 836b/836c. |
| Implementation completeness | complete | All install/readiness gates green on every arm, every seed. |
| Environment adequacy | adequate | Not implicated. |
| Measurement adequacy | **misleading** | Fixed 0.15 discrimination margin not scaled to observed per-arm noise (SEM up to 0.150); ratio DV highly sensitive to individual-seed RL trajectory variance at n=6. |
| Integration adequacy | isolated | Not implicated — each arm's install/refinement pipeline is self-contained. |
| Scale / capacity | **likely insufficient (n)** | n=6 seeds per arm; both non-monotone/reversed verdicts fail a leave-one-out robustness check. |

Dominant diagnosis: **measurement/test-design gap** — the discrimination rule, not the underlying
phenomenon, is what produced an uninterpretable reading. `epistemic_category:
measurement_test_design_defect`.

### V3-EXQ-837 (MECH-475)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened** | The claim's own pre-registered criterion is met for withdrawal; the test let the claim express itself fully. |
| Biological reference | partial | Real lesion literature grounds the destructiveness phenotype; the informative-baseline-reverses-it mechanism is more formal-theoretic (variance reduction) than directly biologically evidenced, and a known stimulus/action-value divergence is unresolved but orthogonal to this specific test. |
| Developmental / dependency prerequisites | present | MECH-457, MECH-459 both registered; V3-EXQ-788 (the positive control) and V3-EXQ-782 (the measured mechanism) both already landed. |
| Implementation completeness | complete | Distributional critic substitution is byte-identical elsewhere to the destructive build; `scalar_inversion_reproduces` confirms no substrate drift. |
| Environment adequacy | adequate | Same env family as the original destructive instances (769/781); not implicated. |
| Measurement adequacy | adequate | `late_competence` trajectory DV, `>=2` probe readings enforced, non-degeneracy guard on the control level — no gap found. |
| Integration adequacy | isolated | Not implicated. |
| Scale / capacity | adequate | n=3 seeds x 2 families x 2 critics x 2 arms, all readiness-gated; metabolic correctly excluded rather than forced. |

Dominant diagnosis: **claim falsified on its own decisive prediction, tested fairly.**
`epistemic_category: standard`.

---

## 5. Cluster pattern

**These are not one convergent structural shape — two distinct diagnoses sharing only a lineage
(the MECH-457 `mech457_retention` baseline substrate) and a family resemblance (both are children
of the same 2026-07-22 `/claim-synthesis` decomposition).** Reported together because they were
adjudicated in the same sweep and because the MECH-476 finding is directly relevant to *how* the
MECH-475 finding should be read (both use the same ratio-DV-at-n=6 measurement pattern; 837 avoided
the trap 836/836c fell into by having a much larger, gate-confirmed effect size — dist_inversion
~15 against a floor of 1.0 — well outside plausible n=3 noise, whereas 836/836c's effects sit
inside their own per-arm SEM).

| Experiment | Claim | Negative-control / absolute criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-836 | MECH-476 | install_took (all arms) PASS | resistance_grows_with_dose FAIL | non-monotone, not robust to 1 outlier seed |
| V3-EXQ-836c | MECH-476 | install_took (both arms) PASS | paired_retains_more_than_unpaired FAIL | reversed, not robust to 1 outlier seed |
| V3-EXQ-837 | MECH-475 | scalar_control_competent, scalar_inversion_reproduces (2/2 scorable) PASS | reverses_or_flattens FAIL (0/2 families, effect 3.4x worse not better) | robust, gate-confirmed falsification |

---

## 6. Learning extracted

- **Measurement gap, propagation risk to V3-EXQ-836b.** The still-running INTERVAL arm
  (`v3_exq_836b_mech476_interval_dependent_consolidation.py`) is very likely to share the same
  fixed-margin discrimination rule (same script family, same `mech457_retention` DV). Flagging now
  so its own eventual autopsy checks this before trusting a SUPPORTED/WEAKENED verdict from it.
- **Existing dependency strengthened, not weakened, for MECH-476**: nothing here bears on whether
  consolidation is dose/interval-dependent. The finding is entirely about discrimination-rule
  validity at this sample size.
- **MECH-475 falsified on its most decisive, self-nominated prediction**, under a fair and
  well-powered test — the claim's own text pre-commits to withdrawal on exactly this outcome
  shape, which is what makes this the highest-confidence finding of the three.
- **Effect-size-gate convention violation, systemic**: both `v3_exq_836` and `v3_exq_836c` use a
  bare literal (`RESISTANCE_DOSE_MARGIN` / `novelty_retention_margin = 0.15`) rather than scaling
  to `sd_delta` as the project's documented convention requires. This is a pattern to check for in
  any sibling script drawing on the same `mech457_retention` DV convention.

---

## 7. Repair pathway

### V3-EXQ-836 / V3-EXQ-836c — node: `complex (probe-gated) / mystery (known data)`

We already have the data; the discrimination *rule* is what's wrong, not the design. Re-gathering
more of the same ratio statistic at the same margin would not resolve it — the frame needs
correcting first.

**Routing: `/queue-experiment`, same-question redesign** (alphabetic suffix — 836a for the dose
arm re-analysis/re-run, and a 836c redo; the scientific question is unchanged). Scope:

1. Replace the fixed `RESISTANCE_DOSE_MARGIN` / `novelty_retention_margin = 0.15` with a
   noise-scaled floor per the project convention (`max(K * sd_delta, absolute_floor)`, mirroring
   the `EFFECT_SIZE_K` / `EFFECT_SIZE_ABS_FLOOR` pattern already used elsewhere in the same
   experiment family — see `v3_exq_824...py:EFFECT_SIZE_K/EFFECT_SIZE_ABS_FLOOR`).
2. Increase seed count (n=6 -> n>=10 per arm) and/or report a robust statistic (trimmed mean or
   median of `retained_fraction`) alongside the mean, so a single-seed RL-trajectory outlier
   cannot flip the verdict.
3. Re-run V3-EXQ-836's three dose arms and 836c's two novelty arms under the corrected rule before
   836's dose-response or 836c's novelty-tagging question is treated as resolved either way.
4. Check `v3_exq_836b_mech476_interval_dependent_consolidation.py` (still running) for the same
   fixed-margin pattern before trusting its own eventual verdict.

**Recommended `evidence_quality_note` for MECH-476** (governance to write, not this skill):

> V3-EXQ-836 (2026-07-29, DOSE arm) self-routed `non_monotone_dose_response` and V3-EXQ-836c
> (2026-07-29, NOVELTY arm) self-routed `reversed_novelty_effect`, but both are
> `non_contributory`, not `mixed`: both verdicts rest on a fixed 0.15 effect-size margin not scaled
> to observed per-arm noise, and neither survives a leave-one-out check on the single most extreme
> seed (`failure_autopsy_mech476-mech475-cluster_2026-07-29`). Superseded pending 836a/836c-redo
> under a noise-scaled discrimination rule.

### V3-EXQ-837 — node: `puzzle` resolved, not `mystery`

The frame was well-posed and the fact was obtained cleanly: **`tested fairly + biology supports the
mechanism (partially) + still fails`.**

**Routing: governance demotion recommendation** for MECH-475, per its own pre-registered
withdrawal criterion.

**Recommended `evidence_quality_note` for MECH-475** (governance to write, not this skill):

> V3-EXQ-837 (2026-07-29) is MECH-475's own decisive REVERSAL test (`what_would_answer` (a)):
> substituting a distributional critic for the scalar one on 2 of the 3 named destructive
> instances (capacity/769, approach/781; metabolic/771 correctly self-excluded, its own control
> never cleared the competence floor). Result: the destructive treatment-below-control inversion
> did **not** reverse or flatten in either scorable family — it got 3.4x *worse* under the
> informative baseline (dist_inversion 15.1/14.9 vs scalar_inversion 4.5/4.4, both families,
> `reverses_or_flattens: false` on all 6 scorable seeds). Per the claim's own text, this outcome
> means the destructiveness is not the baseline's doing and MECH-475 is WITHDRAWN rather than
> narrowed (`failure_autopsy_mech476-mech475-cluster_2026-07-29`). Note MECH-476/460 (which cite
> MECH-475 in `depends_on`) should be re-read for whether they lean on MECH-475's specific causal
> attribution or only on the independently-established destructiveness phenomenon (they use the
> latter — the five-instance table and V3-EXQ-782 R-(b) stand unaffected).

**Granularity-debt recurrence trigger**: `granularity_debt_cluster.py MECH-476` and `MECH-475` both
report **0 target(s) across 0 file(s)** — these are each claim's first autopsy. Trigger does NOT
fire (nothing to recur against yet).

**Re-derive brake**: does not fire for either claim (0 prior `substrate_ceiling` hits under the
R1-R3 convention; neither target's `recommended_epistemic_category` is `substrate_ceiling`).

**Step 9b (hypothesis ledger)**: both targets carry a `recommended_evidence_direction`, so this
runs. Neither V3-EXQ-836/836c/837 was previously an `adjudicating_runs` entry on any existing
`competence_floor` hypothesis (checked directly against the registry). See Step 9b write-up below.

---

## 8. Interactive gate

User confirmed via AskUserQuestion (2026-07-29):

- **MECH-475 (V3-EXQ-837)**: "Recommend demotion/withdrawal" — routed to `/governance` as a fair,
  well-powered test that falsifies MECH-475's causal claim per its own pre-registered criteria.
- **MECH-476 (V3-EXQ-836 + 836c)**: "Redesign re-run (noise-scaled margin + more seeds)" — routed
  to `/queue-experiment`, same-question redesign, new letters.

---

## 9. Routing summary

| Target | evidence_direction (recommended) | epistemic_category (recommended) | Routing |
|---|---|---|---|
| V3-EXQ-836 | non_contributory | measurement_test_design_defect | `/queue-experiment` (836a redesign) |
| V3-EXQ-836c | non_contributory | measurement_test_design_defect | `/queue-experiment` (836c redo) |
| V3-EXQ-837 | weakens | standard | `/governance` demotion recommendation (MECH-475 withdraw) |

`recommended_substrate_queue_entry.action: none` for all three — no substrate build needed; the
gap is in discrimination-rule design (836/836c) or is a clean claim falsification (837).
