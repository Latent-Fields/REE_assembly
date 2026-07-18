# Failure Autopsy — MECH-063 cluster: V3-EXQ-777 + V3-EXQ-779

- **Generated (UTC):** 2026-07-18T06:58:49Z
- **Scope:** cluster (2 targets, both `claim_ids: [MECH-063]`, both `experiment_purpose: evidence`)
- **Status:** confirmed (interactive gate answered 2026-07-18)
- **Session:** festive-goldstine-5eda5a
- **Provenance:** deferred by the 2026-07-18 `/governance` cycle (Step 1.5 route B = defer). Governance
  deliberately did NOT demote MECH-063 on 777's un-adjudicated `weakens` self-route.

---

## 0. Headline

**Neither run tested MECH-063.** Both were starved by the same structural property of the shared
telemetry-probe template, and the load-bearing criterion in each was decided by sampling noise rather
than by the mechanism under test.

- **V3-EXQ-777**'s self-route `control_axes_collinear_toward_one_scalar` and its
  `evidence_direction: weakens` are an **artifact**. Recommended: `non_contributory`.
- **V3-EXQ-779**'s `evidence_direction: non_contributory` is **correct**, but its self-route
  `substrate_not_ready_requeue` **mislabels the cause**. SD-069 is ready and firing; the probe was
  sample-starved.
- **MECH-063 stays `provisional`, with zero experimental evidence.** No demotion. The biological
  existence proof (LC-NE tonic/phasic adaptive gain) is strong and the claim was never placed in
  conditions where it could express itself.

---

## 1. Facts reconstruction

### Recording provenance (always-core)

Both manifests carry the full Experimental Recording Standard always-core: `recording_schema: rec/v1`,
top-level `substrate_hash`, `machine` / `machine_class`, `elapsed_seconds`, full `config`, explicit
`seeds`. **No recording gap.** In particular `n_env_steps` was recorded per cell — that field is what
made this diagnosis possible at all, and it is the reason no blind re-run is needed. Good recording
practice paid for itself here.

| | V3-EXQ-777 | V3-EXQ-779 |
|---|---|---|
| run_id | `v3_exq_777_..._20260717T155914Z_v3` | `v3_exq_779_..._20260717T191826Z_v3` |
| substrate_hash | `f56e1a7e…2bbbde` | `a549ae6a…9ba5f4` |
| machine_class | linux-x86_64-py3.10 | linux-x86_64-py3.10 |
| elapsed | 939.5 s | 1051.8 s |
| seeds | 11, 17, 23, 29, 37 | 11, 17, 23, 29, 37 |
| outcome | FAIL | FAIL |
| non_degenerate | true | **false** (readiness unmet) |
| self-route | `control_axes_collinear_toward_one_scalar` | `substrate_not_ready_requeue` |
| manifest direction | `weakens` | `non_contributory` |

### The binding constraint: episode survival

Both are **untrained** 2×2 factorial telemetry probes (no gradient training; regulators act on the live
E3 `select()` path) in a hazard-terminating 8×8 CausalGridWorldV2, budget 3 episodes × 300 steps = 900,
with `if r.done: break` and **no continuation to meet a sample budget**. Survival is violently
seed-dependent — and **near-identically so across both experiments**, despite different env configs
(777 no background drift; 779 `background_drift_enabled: true`, 3 random-walk sources) and different
regulators under test:

| seed | 777 `n_env_steps` (of 900) | 779 `n_env_steps` (of 900) |
|---|---|---|
| 11 | 281 / 149 / 220 / 321 (~25%) | 262 / 286 / 208 / 284 (~28%) |
| 17 | 98 / 162 / 141 / 208 (~17%) | 239 / 113 / 105 / 130 (~21%) |
| 23 | **21 / 20 / 21 / 21 (2%)** | **21 / 21 / 21 / 19 (2%)** |
| 29 | 900 / 900 / 900 / 900 (100%) | 900 ×4 (100%) |
| 37 | 900 / 900 / 900 / 900 (100%) | 900 ×4 (100%) |

A 40x spread in sample yield across the seed set, reproducing across two structurally different
experiments. This is a property of the **environment under those seeds with an untrained agent**, not of
either probe and not of MECH-063.

Consequence: both runs scored **exactly 3/5 seeds against a `min_seeds: 4` bar**. With 3 of 5 seeds at
2–30% yield, that bar was arithmetically out of reach independent of the hypothesis's truth.

### V3-EXQ-777 — the criterion did not fail on collinearity

```
acceptance: C1_rank2_non_collinearity = false
            c1_seed_count = 3   (min_seeds 4)
            mean_sin_angle = 0.5303   <-- EXCEEDS SIN_MARGIN 0.5
            sd_sin_angle   = 0.3529
```

C1 = `c1_seed_count AND c1_robust`, where `c1_robust = (mean_sin - sd_sin) > 0.5` → 0.177, fails. So the
criterion fell to **seed-count and dispersion**, while the central estimate was on the passing side of
the margin. The manifest's "axes collapse to one scalar" label is not what the numbers say.

Per-seed, and the reason for the dispersion:

| seed | sin_angle | `D_action_mass_mean` (score axis DV) | regime | `dD_score` | `norm_v_score` |
|---|---|---|---|---|---|
| 11 | **0.019** | 0.9969–0.9997 | **ceiling** | 0.0011 | 0.1866 |
| 17 | 0.741 | 0.4483–0.5288 | **headroom** | 0.0538 | 0.1828 |
| 23 | **0.231** | 0.0024–0.0131 | **floor** | 0.0034 | 0.0423 (< 0.05 floor) |
| 29 | 0.984 | 0.9370–0.9839 | near ceiling | 0.0130 | 0.0346 (< 0.05 floor) |
| 37 | 0.677 | 0.8152–0.9456 | near ceiling | 0.0256 | 0.0764 |

`dD_score` tracks D-headroom. Seed 17 — the only mid-range seed — yields the largest score-axis effect.
On the saturated seeds the score axis moves entropy but not action mass, i.e. it degenerates into a
weaker copy of the temperature axis, which is exactly what a low `sin_angle` reports. **The observed
"collinearity" is a ceiling/floor effect on the dependent variable, not a property of the control plane.**

Two design defects produce this:

1. **No saturation guard on the score axis's DV.** P0 guards headroom on the *temperature* axis's
   readout (`baseline_entropy_headroom`, `E_SAT_CEIL = 0.98`, measured 0.3496 → met). R4 checks
   `D_action_mass_std > 0.0`, a trivially-satisfied non-degeneracy test, **not** a saturation test.
   There is no `D_SAT_CEIL` / `D_SAT_FLOOR` analog. The design carefully protected one axis's headroom
   and forgot the same protection for the other.
2. **R5 `axis_authority` aggregates by mean across seeds.**
   `fmean([norm_v_score]) = 0.1046 > EFFECT_FLOOR 0.05` → met. But seeds 23 (0.0423) and 29 (0.0346) are
   individually *below* the floor. The mean masked per-seed axis death, so the gate that exists
   specifically to "guard the false-collapse trap" (queue-entry note) waved through exactly the runs it
   was built to catch.

Note also `sample_sufficiency: measured 20, threshold 20` — the worst cell sat **exactly** on the bar.

### Resolving the seed-11 inline-vs-cloud tension

The queue entry records: *"full-scale seed-11 inline PASS (readiness met, sin_angle=0.93>0.5, entropy
lift +0.30 temp-axis, noop-mass suppression score-axis)."* Cloud seed 11: `sin_angle = 0.019`.

Ruled out — this is **not** a code, scale, or substrate divergence:

- **Script:** exactly one commit (`3b270a1`, 2026-07-17T15:42:33Z), never modified. Inline and cloud ran
  identical code.
- **Scale:** `N_EPISODES=3 / STEPS_PER_EPISODE=300` are the module-level full-scale defaults; only
  `--dry-run` reduces them (to 1/40). The cloud run used full scale (`config` confirms).
- **Substrate:** no `ree_core/` commit landed between `61c0fd9` (2026-07-16T18:08) and the run start
  (≈15:43:35Z = 15:59:14Z − 939.5 s elapsed). The SD-069 commits (`ab6ff33`, `f386179`) landed ~18:04Z,
  *after* 777 finished. Same substrate.

What the divergence actually is: **the temperature axis reproduced; the score axis did not.** Inline
entropy lift +0.30 vs cloud `dE_temp = 0.3229` — a match. Inline reported no-op-mass suppression; cloud
`dD_score = 0.0011` — no suppression, because on cloud seed 11 `D` was pinned at 0.997 and there was
nothing left to suppress. The Mac (`darwin-arm64`) inline run put seed 11 into a different
survival/saturation regime than the cloud worker (`linux-x86_64`).

**Read:** the result is knife-edge on which saturation regime a seed happens to land in, and that regime
is float/platform-sensitive. The single-seed inline PASS was luck, not a contradicted finding — and the
5-seed cloud run is the better-powered observation of a metric that is, in both cases, not measuring
what it was designed to measure. This also means an inline single-seed check is **not** a valid
pre-queue validation for this probe family.

### V3-EXQ-779 — the substrate is ready; the label is wrong

Two preconditions failed:

```
phasic_fires_real_events : measured 5   threshold 10   NOT met
sample_sufficiency       : measured 19  threshold 20   NOT met
```

**The arms did set the new signal source.** Manifest `config.phasic_burst.signal_source =
"instantaneous_pe"`; script sets `cfg.phasic_burst_signal_source = PHASIC_SOURCE` (line 205) and passes
it again at line 236. The user's first hypothesis (mis-wired arms) is ruled out.

**Bursts fire.** Every PHASIC-ON arm shows `burst_level_max = 1.0` with `n_event_ticks` of 19, 15, 18,
12, 6, 5, 19, 17, 22, 22 across the ten P1 cells. SD-069 works as validated.

`phasic_fires_real_events: measured 5` is a **min across cells**, and the 5 comes from exactly one cell:
seed 23 / T1P1, the cell that ran 19 env steps. One dead seed vetoed the entire run's readiness.

So `substrate_not_ready_requeue` is a **mislabel**: it reports a substrate-capability failure where the
actual failure is sample starvation. The direction (`non_contributory`) is nonetheless correct — the run
genuinely discriminated nothing. 779 got the right answer for the wrong reason.

(`mean_dR_phasic = -0.083`, robust, is computed over ~5 event ticks and carries no weight.)

---

## 2. Claim-layer mapping

**MECH-063** — `control_plane.orthogonal_axes_tonic_phasic`
"Control plane retains orthogonal tonic/phasic axes rather than collapsing into one scalar."

- `claim_type: mechanism_hypothesis`; `status: provisional` (as_of 2026-07-11)
- `depends_on: ARC-005, MECH-039, MECH-040, MECH-055`
- Sub-claim (i) orthogonal axes → V3-EXQ-777; sub-claim (ii) tonic/phasic split → V3-EXQ-779 on SD-069.

Index state before adjudication (`claim_evidence.v1.json`):

```
experimental_confidence = 0.324      literature_confidence = 0.758
direction_counts: supports 2, weakens 1
genuine_exp_direction_counts: supports 0, weakens 1
fail_runs 1, pass_runs 0
latest_run_id = v3_exq_777_...
```

**Both "supports" are literature.** 777's `weakens` is the *only* experimental entry MECH-063 has, and
it alone produces `exp_conf = 0.324`. 779 is correctly absent (non_contributory is excluded).

**Were the claim tags accurate?** Yes — both experiments were purpose-built for MECH-063 sub-claims (i)
and (ii) respectively; tags were not inherited from a predecessor. The FAILs are weighing against the
right claim. They simply do not weigh.

**Did the experiment let the claim express itself?** No, in both cases. 777 could not: on 4 of 5 seeds
the score axis's dependent variable was saturated, so orthogonality had no room to appear. 779 could
not: it never accumulated enough event-locked ticks to compute a transient.

**Illusory-conflict check (mandatory for any non_contributory recommendation).** Reclassifying 777
removes MECH-063's only experimental entry and returns the claim to **lit-only** — 2 literature supports
(0.79, 0.81), zero experimental. This does **not** manufacture illusory support: it restores exactly the
posture the claim's own flags already assert (`lit_only_above_cap`, `low_exp_conf`,
`synthetic_signals_only`). The remaining supports are narrow and single-pathway — both are 2005-era
LC-NE / neuromodulator theory reviews from one lit pull — and that narrowness should be stated plainly
rather than papered over. MECH-063 after this adjudication is an **untested** claim with good biological
warrant, not a supported one.

---

## 3. Biological-reference triage

- **Closest reference mechanism:** locus coeruleus–noradrenaline tonic vs phasic modes (Aston-Jones &
  Cohen adaptive gain theory), with DA tonic/phasic (Grace) as a second instance of the same class.
  Tonic baseline arousal/exploration and event-locked phasic gain bursts are genuinely dissociable
  degrees of freedom in primate recordings.
- **Dependencies in real brains:** an arousal/uncertainty baseline signal, a salience/event detector, and
  a shared downstream gain target on which both act.
- **Is MECH-063 a formal-definition import?** **No.** It derives from basal-ganglia and neuromodulator
  biology (`docs/thoughts/2026-02-15_basal_ganglia*.md`), not from a Pearl/Shannon/optimal-control
  formalism. This is a biological translation, so the SD-003 failure mode does not apply.
- **Literature status: present.** `evidence/literature/targeted_review_mech_063/` holds two entries —
  `2026-02-15_mech063_lcne_adaptive_gain_annurev2005` (0.81) and
  `2026-02-15_mech063_uncertainty_neuromod_attention_neuron2005` (0.79). **No `/lit-pull` commission is
  owed.**
- **Does the failure resemble a missing biological dependency?** **No.** It resembles a measurement
  instrument run against a saturated dependent variable on a starved sample. Both regulators were
  confirmed live by P0 (`score_axis_live` 0.5 > 0; `temperature_axis_live` 1.0 > 0.5; `tonic_axis_live`
  1.0 > 0.5), and SD-069 demonstrably fired. The mechanism was present; the readout could not see it.

**Verdict: the biology supports the mechanism class strongly, and the experiments did not place the
claim in conditions where it could express itself. Demotion threshold is not remotely met.**

---

## 4. Four-layer diagnosis

| Layer | V3-EXQ-777 | V3-EXQ-779 |
|---|---|---|
| Claim alignment | **intact (untested)** — saturated DV prevented expression | **intact (untested)** — insufficient event ticks |
| Biological reference | **clear** — LC-NE tonic/phasic; failure does NOT match a missing-dependency signature | **clear** — same; SD-069 is the phasic complement to MECH-313 tonic |
| Prerequisites | **present** — MECH-320 tonic_vigor + MECH-313 noise_floor both implemented, both confirmed live by P0 | **present** — SD-069 IMPLEMENTED, correctly wired (`instantaneous_pe`), bursts fire (`burst_level_max 1.0`) |
| Implementation | **complete** — both regulators exercised on the real production E3 path | **complete** — self-route label wrongly implies otherwise |
| Environment | **wrong pressures** — untrained agent, hazard-terminating env; `D_action_mass` saturates at ceiling/floor on 4/5 seeds | **wrong pressures** — same starvation; drift raises the surprise baseline against a ratio trigger |
| Measurement | **under-instrumented / misleading** — no saturation guard on the score axis's DV; R5 mean-across-seeds masks per-seed axis death | **under-instrumented** — min-across-cells readiness lets one dead cell veto the run; label conflates sampling with substrate |
| Integration | **coupled** — both axes route to the same softmax by design | **coupled** — tonic + phasic share the temperature readout by design |
| Scale / capacity | **insufficient** — 20–21 selections on starved seeds, exactly at `MIN_SELECTS` | **insufficient** — 19 selections, below `MIN_SELECTS` 20 |

**Recommended `epistemic_category` (both): `measurement_test_design_defect`.**
Not `substrate_ceiling` — the substrate is present, wired, and demonstrably active in both runs. The
defect is in the probe template's sampling model and readiness gating.

---

## 5. Cluster pattern

| Experiment | Claim | Negative-control / absolute criteria | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-777 | MECH-063 (i) | ALL 5 P0 preconditions **met** (score axis live, temp axis live, samples ≥20, entropy headroom, axis authority) | `C1_rank2_non_collinearity` **failed** on 3/5 seeds + dispersion, with `mean_sin 0.530 > margin 0.500` | discrimination failed on sampling noise while controls passed |
| V3-EXQ-779 | MECH-063 (ii) | tonic axis live **met**, both partitions populated **met**, entropy headroom **met** | `double_dissociation_C1_and_C2` **failed** on 3/5 seeds; 2 sample-count preconditions unmet | same shape; readiness vetoed by one starved cell |

**These are NOT two independent bugs. They are one structural property.**

> The shared 2×2 read-only telemetry-probe template fixes its sampling budget in **episodes**, while its
> readiness gates and criterion bars are denominated in **selections / event ticks / per-seed counts**.
> Because these probes run an **untrained** agent in a **hazard-terminating** environment, episodes
> terminate early and seed-dependently — a 40x spread in yield across one seed set. The budget therefore
> does not determine the sample, and the criterion bar (`min_seeds = 4 of 5`) becomes unreachable
> whenever 3 of 5 seeds run short, regardless of the hypothesis's truth value.

The two gates then failed in **opposite directions from the same blind spot**:

- **777's P0 was too permissive** — aggregating axis authority by *mean across seeds* let a run through
  in which the score axis was individually dead on 2 seeds and saturated on 2 more.
- **779's P0 was too restrictive on the wrong axis** — aggregating by *min across cells* let a single
  19-step cell veto a run in which the substrate was working everywhere else.

Neither gate guarded the actual binding constraint: **sample yield per cell**.

Both readings named and adjudicated:
- *substrate enrichment* — **rejected.** Both substrates (MECH-320/MECH-313; SD-069) were present, live
  and firing. Nothing about ree_core needs to be built for these questions.
- *test-design ceiling* — **accepted.** The defect lives entirely in the probe template's sampling model
  and readiness aggregation.

**Planning consequence:** the fix belongs to the *telemetry-probe family*, not to MECH-063. Any future
2×2 read-only probe built from this template inherits the same defect until the shared rollout helper
exists. That is why the routing below includes a `_lib` build alongside the two re-queues.

---

## 6. Learning extracted

1. **Episode-denominated budgets do not control sample size for untrained agents in terminating
   environments.** Yield varied 40x across one seed set and reproduced across two different experiments
   — a property of env × seed, not of either probe. Telemetry probes must use **sample-driven stopping**
   (run until each cell reaches N fresh selections), not a fixed episode count.
2. **Guard saturation on *every* axis's dependent variable, not just the first.** 777 protected entropy
   headroom (`E_SAT_CEIL`) and left action-mass unguarded; action-mass then sat at ceiling or floor on
   4/5 seeds and produced a false collinearity signature. A `>0.0` standard-deviation check is a
   non-degeneracy test, not a saturation test.
3. **Never aggregate a per-seed readiness gate by the mean.** R5's `fmean(norm_v_score) = 0.1046 > 0.05`
   passed while two seeds sat below the floor individually. A gate built to catch the false-collapse
   trap was defeated by its own aggregator. Per-seed gating, reported per seed.
4. **Distinguish "substrate cannot" from "we did not sample enough" in self-route vocabulary.**
   `substrate_not_ready_requeue` sent a reader looking for a missing SD-069 capability that was in fact
   present and firing. A distinct `sample_starvation_requeue` label would have routed this correctly on
   sight. Min-across-cells readiness needs to report *which* cell and *why*.
5. **A single-seed inline pre-queue check is not valid validation for a metric with seed-dependent
   saturation.** The seed-11 inline PASS (`sin_angle 0.93`) and the seed-11 cloud FAIL (`0.019`) came
   from identical code and substrate; they differ only in which saturation regime that seed landed in on
   that machine class. Pre-queue validation for this family must run the full seed set, and should
   report the DV's saturation state per seed.
6. **Cross-machine-class reproducibility is readout-specific.** The temperature axis reproduced across
   `darwin-arm64` → `linux-x86_64` (+0.30 vs +0.323); the score axis did not. A probe whose verdict
   flips with machine class is reporting its own instability, and that instability is diagnostic
   information worth recording.
7. **Recording discipline paid off.** `n_env_steps` per cell is what made this whole diagnosis possible
   without a re-run. This is **not** a recording gap (Experimental Recording Standard §3b always-core is
   complete in both manifests) — it is a design gap, diagnosable precisely because recording was good.
8. **An auto-derived `evidence_direction` can move a claim's confidence before a human adjudicates the
   self-route.** 777's `weakens` propagated into `exp_conf = 0.324` while the run was still sitting
   un-adjudicated in `pending_review.md`. The 2026-07-18 governance cycle's decision to defer rather
   than demote was correct and is what preserved the claim.

---

## 7. Repair pathway

**Work-graph classification: `complicated (buildable)`.** The fix is a named build with no open
question — no spike is needed to learn anything first. Do not queue a diagnostic to re-confirm what the
data already shows.

**Re-derive brake: does NOT fire.** Prior `substrate_ceiling` / `non_contributory` autopsies tagging
MECH-063 = **0**; this autopsy makes it 1, below the `RE_DERIVE_BRAKE_THRESHOLD` of 2. A same-question
re-queue is therefore permitted. **Flag for the next cycle:** a further `non_contributory` autopsy on
MECH-063 *will* fire the brake and force `/implement-substrate` routing — so 777a/779a must actually fix
the sampling model, not re-run the same design with a nudged threshold.

**GOV-FANOUT-1: not applicable.** This bottleneck routes to a single unambiguous build, not to a
discrimination among ≥2 live hypotheses. No `fanout_recommendation` is emitted.

### Routing (user-confirmed)

**(a) `/queue-experiment` — V3-EXQ-777a** (alphabetic suffix: same scientific question, implementation
fix). Required changes:
- **Sample-driven stopping**: run until every cell reaches ≥ `MIN_SELECTS` fresh E3 selections
  (auto-reset and continue across episodes), replacing the fixed 3×300 budget. Cap total env steps to
  bound runtime and **record the realised step count and episode count per cell**.
- **Add a saturation guard on the score axis's DV**: `D_SAT_LOW` / `D_SAT_HIGH` on `D_action_mass_mean`,
  mirroring the existing `E_SAT_CEIL` on entropy. A seed whose D is pinned at ceiling or floor must be
  reported as non-informative for the score axis rather than contributing an angle.
- **Per-seed R5 authority gating**: replace `fmean([norm_v_score]) > EFFECT_FLOOR` with a per-seed test;
  report which seeds pass. Do not let a mean mask per-seed axis death.
- Re-examine whether `min_seeds = 4 of 5` is the right bar once yield is equalised, and record the
  per-seed saturation state alongside `sin_angle`.

**(b) `/queue-experiment` — V3-EXQ-779a** (alphabetic suffix). Required changes:
- Same sample-driven stopping; guarantee `MIN_EVENT_TICKS` per PHASIC-ON cell before scoring.
- **Rename / re-route the self-route label**: emit `sample_starvation_requeue` (not
  `substrate_not_ready_requeue`) when the unmet precondition is a sample count rather than a capability
  check, and **report the offending cell** (seed + arm) in the precondition record.
- Consider whether the ratio-based burst trigger (`trigger_ratio 1.2` against a surprise EMA) needs an
  absolute-level companion under `background_drift_enabled`, where chronic drift elevates the EMA
  baseline and desensitises a purely relative trigger. Record `burst_level_mean` against the EMA so this
  is checkable.

**(c) Shared `_lib` build (prevents recurrence across the family).** Add a rollout helper under
`ree-v3/experiments/_lib/` providing sample-driven cell rollout — "run until this cell has N fresh E3
selections (or a step cap), auto-resetting across episodes, returning realised counts". Every 2×2
read-only telemetry probe built from this template inherits the starvation defect until this exists.
This is an experiment-harness build, not a `ree_core` substrate change — hence
`recommended_substrate_queue_entry.action = "none"`.

**Nothing is currently in flight** for either question (`ree-v3/experiment_queue.json` holds 2 items,
neither MECH-063; `substrate_queue.json` holds 6 items, none covering this gap).

### Granularity-debt recurrence check

Grep of `evidence/planning/failure_autopsy_*.json` for MECH-063 returns **no prior autopsy**. This is the
first. The recurrence trigger does **not** fire and no `/claim-synthesis` handoff is recommended.
`granularity_debt_trigger.fires = false`.

---

## 8. Recommended governance writes (this skill does NOT apply them)

### V3-EXQ-777

- `evidence_direction`: `weakens` → **`non_contributory`**
- `epistemic_category`: **`measurement_test_design_defect`**
- `pending_retest_after_substrate`: **true** (retest = V3-EXQ-777a)

**Draft `evidence_quality_note`:**

> Adjudicated by failure_autopsy_MECH-063-777-779-cluster_2026-07-18. The self-route
> `control_axes_collinear_toward_one_scalar` is an artifact and does not weaken MECH-063. C1 failed on
> seed-count (3/5 vs min 4) and dispersion, NOT on collinearity: mean_sin_angle 0.530 exceeds the 0.500
> margin. The score axis's dependent variable (D_action_mass) was saturated at ceiling on seeds 11/29/37
> (0.94-0.9997) and at floor on seed 23 (0.002-0.013), leaving no headroom for the axis to express
> itself; dD_score tracks D-headroom (largest, 0.054, on seed 17, the only mid-range seed). The P0
> readiness gate passed because R5 axis_authority aggregates norm_v_score by MEAN across seeds (0.1046 >
> 0.05 floor) while seeds 23 (0.0423) and 29 (0.0346) were individually below floor, and because the
> design guards saturation on the temperature axis's readout (E_SAT_CEIL) with no equivalent guard on
> the score axis's. Compounding this, 3 of 5 seeds ran at 2-30% of the 900-step budget (untrained agent,
> hazard-terminating env), putting the worst cell exactly at MIN_SELECTS=20. The queueing session's
> seed-11 inline PASS (sin_angle 0.93) is not contradicted: identical script (single commit 3b270a1) and
> identical substrate (no ree_core commit in the window), with the temperature axis reproducing (+0.30
> inline vs dE_temp 0.323 cloud) and only the score axis diverging, because cloud seed 11 was saturated
> at D=0.997. The verdict is knife-edge on per-seed saturation regime, which is machine-class sensitive.
> MECH-063 was not tested. Retest V3-EXQ-777a with sample-driven stopping, a D-saturation guard, and
> per-seed authority gating.

### V3-EXQ-779

- `evidence_direction`: **`non_contributory` (unchanged — already correct)**
- `epistemic_category`: **`measurement_test_design_defect`**
- `pending_retest_after_substrate`: **true** (retest = V3-EXQ-779a)

**Draft `evidence_quality_note`:**

> Adjudicated by failure_autopsy_MECH-063-777-779-cluster_2026-07-18. Direction non_contributory is
> correct, but the self-route `substrate_not_ready_requeue` mislabels the cause: SD-069 is ready and
> working, and the failure is sample starvation. The arms DID set the sharp source
> (config.phasic_burst.signal_source = "instantaneous_pe"; script line 205), and bursts fired in every
> PHASIC-ON cell (burst_level_max 1.0; n_event_ticks 5-22). The failed precondition
> phasic_fires_real_events (measured 5, threshold 10) is a MIN across cells sourced entirely from seed
> 23 / T1P1, the cell that ran 19 env steps of a 900-step budget; sample_sufficiency (19 vs 20) has the
> same origin. Seeds 11/17/23 ran at 2-28% of budget while 29/37 ran at 100% - a seed-dependent
> early-termination pattern reproduced almost exactly in V3-EXQ-777, i.e. a property of the untrained
> agent in a hazard-terminating env rather than of this probe. mean_dR_phasic (-0.083) is computed over
> ~5 event ticks and carries no weight. MECH-063 sub-claim (ii) was not tested. Retest V3-EXQ-779a with
> sample-driven stopping guaranteeing MIN_EVENT_TICKS per PHASIC-ON cell, and a
> `sample_starvation_requeue` label distinct from substrate-capability failure.

### MECH-063 claim disposition

**Stays `provisional`. No demotion.** After adjudication the claim holds **zero** experimental evidence
and two literature supports (0.79, 0.81, both from one 2005-era LC-NE / neuromodulator pull). Its
existing flags (`lit_only_above_cap`, `low_exp_conf`, `synthetic_signals_only`) already describe this
posture accurately and should be retained. Both sub-claims remain open pending V3-EXQ-777a / 779a.

**Suggested claim-level note:**

> Sub-claims (i) and (ii) both remain experimentally untested as of 2026-07-18. V3-EXQ-777 and
> V3-EXQ-779 were adjudicated non_contributory (measurement_test_design_defect) by
> failure_autopsy_MECH-063-777-779-cluster_2026-07-18: a shared telemetry-probe template denominates its
> budget in episodes while its gates are denominated in selections, and untrained agents in a
> hazard-terminating env yield 2-100% of budget depending on seed. Retests V3-EXQ-777a / 779a pending.
> Biological warrant remains strong (LC-NE tonic/phasic adaptive gain); the claim is untested, not
> unsupported.

---

## 9. Hypothesis-space ledger (Step 9b)

New question registered: **`control_plane_rank`** — "Does the control plane carry two independent
degrees of freedom, or collapse to one scalar?" (claims: MECH-063, SD-069).

Three hypotheses pre-registered, **all left `alive`**: the rank-2 score/temperature reading (777), the
tonic/phasic dissociation reading (779), and the rival one-scalar-collapse reading. Both runs are
recorded as `resolving_runs` with a `basis`, but **neither met the elimination bar** — controls were not
cleanly passed (777's P0 passed only via a mean that masked per-seed axis death; 779's readiness was
unmet and `non_degenerate` is false), and neither run discriminated.

**Reduction ratio for this cycle: 0 of 3 eliminated. Two runs spent, zero bits removed.** The
`decision.observation_bottleneck` records the cause: sample starvation from episode-denominated budgets
in a terminating environment. This is the honest Dimension-3/4 signal and is exactly the anti-Goodhart
record the frozen ledger exists to keep.
