# Failure autopsy -- SD-068 REM leg, GOV-FANOUT-1 3-leg discrimination cluster

- **Generated:** 2026-07-18T18:06:48Z
- **Scope:** cluster (3 legs, read jointly)
- **Status:** confirmed (interactive gate answered 2026-07-18)
- **Question:** `consolidation_readout_validity` (frozen ledger, pre-registered 2026-07-18T08:41:15Z)
- **Governing rule:** GOV-FANOUT-1 (portfolio must be read jointly) + GOV-FROZEN-1 (this artifact is the single producer of the Step 9b resolutions)
- **Claims tagged:** SD-068, MECH-168, INV-047, MECH-169
- **Routed by:** `failure_autopsy_V3-EXQ-778c_2026-07-18.json` -> `targets[0].fanout_recommendation`

| Leg | queue_id | axis | hypothesis | outcome | self-route |
|---|---|---|---|---|---|
| 1 | V3-EXQ-778d | measurement | `H-rem-clamp-artifact` | FAIL | `substrate_not_ready_requeue` |
| 2 | V3-EXQ-778e | representation | `H-rem-genuinely-content-free` | FAIL | `measurement_still_degenerate_requeue` |
| 3 | V3-EXQ-778f | observation | `H-gen-gain-content-free` | PASS | `gen_gain_content_free_intact_seed_gloss_unsupported` |

**All three legs are present.** V3-EXQ-778e completed at 2026-07-18T16:33:18Z, eighteen minutes after the `/governance` cycle ran at 16:15Z; it was therefore absent from that cycle's `pending_review.md` but is fully available here. No leg was dropped or failed to report. **No subset adjudication occurred.**

---

## 1. Facts reconstruction

### Recording provenance

All three manifests carry the always-record core: `recording_schema: rec/v1`, top-level `substrate_hash`, `machine_class`, `elapsed_seconds`, full `config`, explicit `seeds` (`[42, 7, 123, 2024, 99, 7777, 314, 1000]`, n=8 throughout). No recording debt. Substrate hashes differ per leg (`3ede592a...` / `95ec67cb...` / `9fb95d10...`) because each leg ships its own driver; all are `linux-x86_64-py3.10`.

### Leg 1 -- V3-EXQ-778d (measurement axis)

Probe was **amended before queuing**. The original step-ladder probe was proven inert at pre-queue design audit: `recalibrate_precision_to` computes `rv_after = (1-step)*rv_before + step*(1/(target+1e-6))`, so the `1e-3` positivity clamp is applied upstream of `step` (clamp fraction exactly step-invariant) and `step` cancels in the reported ratio. Verified over `step in {0.1, 0.25, 0.5, 1.0}`: ratio identical to 12 significant figures. The amendment (unpaired-target null, the Bar et al. 2020 "same odour, no prior pairing" analog) is recorded at `probe_amendments[0]` and landed at REE_assembly master `2970e2112c`; witness commit ree-v3 `18c4687`. **The amendment retired a probe that would have returned its own declared null by construction** -- it prevented a false elimination, and is a model instance of pre-queue design audit.

Preconditions:

| precondition | measured | threshold | met |
|---|---|---|---|
| `injected_arm_sigma_slope_supra_floor` | 0.06648 | 1e-06 | **true** |
| `null_zero_anchor_reproduces_778c_railed_signature` | 0.625 | 0.75 | **false** |

Criteria: `C1_unpaired_null_derails` (LOAD-BEARING) **passed**, 7/8 seeds de-railed. `C2_unpaired_ratio_content_contingent` failed, 1/8. `C3_anchor_reproduces_778c` failed (inherits the anchor).

`ARM_NULL_UNPAIRED` per-seed clamp fractions `[0.0, 0.0, 0.0, 0.2, 0.0, 0.6, 0.2, 0.2]`; unclamped null_slope_ratios `[0.995, 0.901, 0.877, 0.0011, 0.577, 85.18, 0.574, 3.295]`.

### Leg 2 -- V3-EXQ-778e (representation axis)

Preconditions: `declamped_injected_arm_sigma_slope_supra_floor` 0.0771 vs 1e-06 **met**; `declamped_null_series_non_degenerate` 0.0 vs 1e-09 **not met**.

`C1_declamped_ratio_above_ceiling` (LOAD-BEARING) failed. Per-seed de-clamped ratios `[0.999, 0.0, 0.998, 0.0, 0.326, 0.0, 0.0, 0.0]`; per-seed null-series SD `[0.154, 0.0, 0.061, 0.0, 0.586, 0.0, 0.0, 0.0]`; `n_distinct` `[5, 1, 5, 1, 5, 1, 1, 1]`.

The run carries a **within-run legacy replication anchor**: `calibration_error` scored on the identical cells, per-seed ratios `[4348.47, 0.0, 9142.77, 0.0, 1801.65, 0.0, 0.0, 0.0]`.

### Leg 3 -- V3-EXQ-778f (observation axis)

Precondition `control_input_corruption_range_supra_floor` 1.5646 vs 0.05 **met**. `non_degenerate: true`, all three `criteria_non_degenerate` true, all three criteria passed.

`C1_gain_flat_in_content_scale` (LOAD-BEARING) **passed**: `mean_gain_delta_1_minus_0 = -0.009662`, separation bar `max(0.05, 2 x SEM=0.0117) = 0.05`, `separated: false`. Mean gain by content scale: 0.1589 (0.0) / 0.1520 (0.5) / 0.1493 (1.0). `n_seeds_attenuating = 8` at **every** scale.

---

## 2. The load-bearing finding: 778d's failing precondition is a specification bug

`ARM_NULL_ZERO` **is** the V3-EXQ-778c rem condition on the same seeds and the same RNG stream. It reproduced 778c exactly:

| source | per-seed `null_slope_ratio` |
|---|---|
| V3-EXQ-778c (registry basis) | `0.0` on 5/8, `1801-9143` on 3/8 |
| V3-EXQ-778d `ARM_NULL_ZERO` | `[4348.47, 0, 9142.77, 0, 1801.65, 0, 0, 0]` |
| V3-EXQ-778e legacy anchor | `[4348.47, 0, 9142.77, 0, 1801.65, 0, 0, 0]` |

Bit-identical floats across three independent runs. The replication is not in doubt.

The precondition nevertheless reported FALSE, because of its predicate at
`ree-v3/experiments/v3_exq_sd068_rem_unpaired_null_diagnostic.py:288`:

```python
derailed = bool(
    clamp_frac <= DERAIL_CLAMP_CEILING      # 0.2
    and n_distinct >= DERAIL_MIN_DISTINCT   # 3
    and len(clean_sigmas) >= MIN_UNCLAMPED_SIGMAS  # 3
)
...
"railed": bool(not derailed),
```

V3-EXQ-778c's degeneracy was documented **at BOTH rails**:

- the **saturation** rail -- `calibration_error` pinned at the constant 998.5009992509989, `target_clamped 1.0`, giving an identically zero slope (5/8 seeds);
- the **positivity-floor** rail -- the null precision reference collapsed onto the `1e-3` floor so `1/1e-3` dominates, giving off-scale ratios 1801-9143 (3/8 seeds).

This predicate detects only the **saturation** rail. The three floor-collapsed seeds (indices 0, 2, 4 -- exactly the 4348 / 9143 / 1802 seeds) have `clamp_frac = 0.2`, `n_distinct = 5`, `n_unclamped = 4`, so they satisfy `derailed` and are scored as **healthy**. Verified on seed 42: `clamp_frac 0.2`, `n_distinct 5.0`, `railed: false`, `derailed: true` -- while its `null_slope_ratio_full` is 4348.47, which is the off-scale rail.

**Consequence: the maximum anchor fraction achievable by a bit-perfect replication of 778c is exactly 5/8 = 0.625, and the gate demands >= 0.75. The precondition is unmeetable by construction.** It cannot ever report "met," no matter how faithfully the anchor reproduces.

And because

```python
"criteria_non_degenerate": {
    "C1_unpaired_null_derails": bool(readiness_ok and anchor_ok),
```

with `readiness_ok` true on 8/8, **the entire degeneracy flag on the load-bearing criterion traces to this one mis-specified statistic.**

This is the canonical V3-EXQ-642 shape the skill warns about: the precondition test itself is wrong, so the self-route `substrate_not_ready_requeue` **mislabels the cause**. Nothing about the substrate was unready. The correct classification is `instrument_specification_gap` -- a readiness predicate narrower than the degeneracy it anchors to.

**Adjudicated at the interactive gate:** correct the anchor to the both-rails predicate, treat `control_passed` as true (the underlying evidence is identical floats, not a judgement call), and record the correction and its witness in the resolution basis. This is a post-hoc rehabilitation of the control and is labelled as such.

---

## 3. Cluster pattern -- one structural property, not three bugs

| Leg | Axis | Family | Negative-control / readiness | Discrimination result | Read |
|---|---|---|---|---|---|
| 778d | measurement | instrumentation | injected slope 0.0665 >> 1e-06, 8/8 (**passed**); anchor mis-specified (rehabilitated) | C1 de-rail **passed** 7/8; C2 content-contingent **1/8**, ratios 0.577-0.995 | degeneracy WAS an operationalisation artifact; once de-railed the null STILL tracks the injected slope -> readout content-**free** |
| 778e | representation | representation | injected slope 0.0771 >> 1e-06 (**passed**) | on the 3 non-degenerate seeds: 0.999 / 0.998 / 0.326, all above the 0.25 ceiling | independent route, same answer -> content-**free** |
| 778f | observation | representation | corruption range 1.5646 >> 0.05 (**passed**) | Δgain -0.0097 vs bar 0.05; 8/8 attenuating at every scale | gain is content-**free** |

**These are not three independent bugs. They are one structural property: the SD-068 REM calibration readout does not track content fidelity.** The finding is robust across three distinct design axes spanning two axis-families (instrumentation, representation), each with its own declared null, each with a passing positive control.

Two corroborating details:

- **De-clamping changed the scale but not the pattern.** 778e's de-clamped readout moved the ratios from 1801-9143 down to ~0.33-1.0, but the *same five seeds* still saturate (`n_distinct = 1`). The degeneracy is not a units artifact.
- **778f's residual trend points the wrong way for the gloss.** There is a consistent monotone ordering (7/8 seeds), but it is an order of magnitude below the pre-registered separation bar -- exactly the "consistent-but-tiny" case the bar was built to reject -- and its **sign is inverted**: gain is *lower* with intact content (0.1493) than with none (0.1589). The "correction needs an intact seed" gloss predicts the opposite.

**Why joint reading was load-bearing.** No single leg cleared its own load-bearing criterion in isolation. Read alone, 778d routes to `substrate_not_ready_requeue` and 778e to `measurement_still_degenerate_requeue` -- two requeues and no finding. Read jointly, with the anchor bug diagnosed, they are unambiguous and mutually corroborating. This cluster is a direct validating instance of GOV-FANOUT-1's premise: **subset adjudication here would have produced two spurious requeues and left a real result unrecorded.**

**Axis-family note (anti-circling check).** `H-rem-clamp-artifact` sits in the `instrumentation` family, which already contains an eliminated leg (`H-sws-content-contingent`). This is **not** the dead leg wearing a new name: `H-sws` concerned the SWS phase's `denoising_snr` log-ratio, whose content term differentiates out algebraically; `H-rem-clamp-artifact` concerns a different phase, a different readout (`calibration_error`), and a different failure mode (clamp saturation, not algebraic cancellation). The family co-occurrence is genuine convergence on "the instruments are the problem," not re-entry.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened (SD-068 only)** | The claims could express themselves; the *instrument* could not. SD-068's staged-failure contract loses its REM instrument and its generative-gain pillar. MECH-168 / INV-047 / MECH-169 are context tags -- the cluster audits the instrument, not those claims. |
| Biological reference | **clear** | Bar et al. 2020 unpaired-target control ("same odour, no prior pairing") is the correct biological analog and was faithfully implemented in the amended 778d probe. Not a formal-definition import. |
| Prerequisites | **present** | No missing `depends_on`. Both readiness controls cleared on 8/8 seeds. |
| Implementation | **complete** | The consolidation pipeline ran as designed; `e3_selector.recalibrate_precision_to` behaves exactly as its algebra predicts. |
| Environment | **adequate** | Sigma sweep spans the full grid; corruption range 1.56 >> floor. |
| Measurement | **misleading (the finding)** | Two distinct instrument defects: (a) the REM readout is content-free -- it responds to noise magnitude, not content fidelity; (b) 778d's readiness anchor predicate is narrower than the degeneracy it anchors to. |
| Integration | **coupled, stable** | Consistent across seeds, axes, and three runs. |
| Scale / capacity | **adequate** | n=8 seeds; the joint signal is not power-limited. Ratio *spread* is wide, but every per-seed value except one falls on the content-free side of the ceiling. |

**Recommended `epistemic_category`: `measurement_gap`** (consistent with 778c's reading of the same question).

**Residual honestly stated:** one dissenting seed. 778d seed index 3 shows an unclamped ratio of 0.0011 -- strongly content-contingent -- on a legitimately de-railed arm (`clamp_frac 0.2`, 4 unclamped sigmas). The unpaired-arm ratio estimate is also unstable (sd 29.8, 95% CI [-9.08, 32.18], `ceiling_inside_ci95: true`), but the instability runs *toward* larger ratios, i.e. toward more content-freeness. The direction is not in doubt; the magnitude is not estimable.

---

## 5. Learning extracted

1. **A readiness anchor must be scored with the same predicate as the degeneracy it anchors to.** 778d's anchor asserted "reproduces 778c's railed signature" but implemented a one-rail `railed` predicate against a documented two-rail degeneracy, capping the achievable score at 0.625 under a 0.75 gate. A precondition that a perfect replication cannot pass is not a control -- it is a guaranteed false negative. **Generalisable check for any future readiness anchor: compute the value the reference run itself would score under the shipped predicate, and assert the threshold is below it.** Had that check been run at design-audit time it would have caught this exactly as the step-ladder inertness was caught.
2. **The SD-068 REM calibration readout is content-free**, robust across measurement / representation / observation axes. It measures noise sensitivity, not content fidelity.
3. **`rem_generative_gain` is a content-free transfer-function property.** The attenuation is real (0.149, 8/8 seeds, at every content scale) but occurs with no seed content at all, so it cannot evidence that correction needs an intact seed.
4. **GOV-FANOUT-1 validated on a live case.** Two of three legs self-routed to requeue; the portfolio read jointly yields a clean structural finding. Subset adjudication would have produced exactly the confident-but-wrong outcome the rule exists to prevent -- here, ironically, in the *conservative* direction (two spurious requeues, one real finding lost).
5. **Pre-queue design audit paid for itself twice on this question** -- once catching the provably-inert step ladder before compute was spent, and once (retrospectively, here) failing to catch the anchor predicate. The asymmetry is instructive: the inert-probe check was algebraic and got run; the anchor-threshold check was arithmetic and did not exist. Learning 1 proposes it.

---

## 6. Routing

**Primary routing: `queue-experiment`** -- a same-question re-run of the 778d measurement leg (alphabetic suffix, `V3-EXQ-778h`) whose **only** change is to fix the anchor predicate to count both rails, plus the generalisable threshold-vs-reference assertion from Learning 1.

This is an **instrument-specification fix, not a blind re-run and not a substrate build.** The scientific content of 778d is already adjudicated here; the re-run exists to make the ledger's control provenance clean-as-shipped rather than clean-as-rehabilitated. It is therefore **low priority** -- explicitly *not* a blocker on the resolutions below, which stand on the joint evidence.

**Re-derive brake: NOT fired.** Zero prior `substrate_ceiling` / `non_contributory` autopsies on SD-068, MECH-168, INV-047, MECH-169. No same-claim re-queue is being refused.

**Granularity-debt recurrence trigger: FIRES (N=2).** This is the second autopsy on the `consolidation_readout_validity` / SD-068 target (prior: `failure_autopsy_V3-EXQ-778c_2026-07-18`), with a *different* failure signature each time (778c: algebraic content-cancellation in a log-ratio; this cluster: clamp saturation + a mis-specified readiness predicate). Per the skill's proactive hook this is surfaced as a **`/claim-synthesis` recommendation** on SD-068: the recurring pattern is that SD-068 asserts a *staged* three-phase damage-tolerance contract while its three per-phase instruments have turned out to be three structurally different measurement problems. That is granularity debt -- SD-068 is plausibly several claims (one per phase, plus the staging-order claim) -- not a falsification. Recorded as a recommendation only; this autopsy does not route it.

**No substrate_queue entry.** `recommended_substrate_queue_entry.action: none`. The existing SD-068 readout-rebuild routing (from 778c, now partly discharged by the 778g SWS rebuild) already covers the substrate plane; this cluster adds no new substrate gap.

### Draft `evidence_quality_note` for governance (SD-068)

> The SD-068 REM per-phase readout is content-free. Three GOV-FANOUT-1 discrimination legs on distinct design axes converge (V3-EXQ-778d measurement / 778e representation / 778f observation, n=8 seeds each, all positive controls passing): once the zero-content null's clamp degeneracy is removed by an unpaired-target null, the null arm still tracks the injected arm's sigma-slope (content-contingent on 1/8 seeds only; unclamped ratios 0.577-0.995), and an independently de-clamped readout agrees on every non-degenerate seed (0.999 / 0.998 / 0.326, all above the 0.25 ceiling). Separately, `rem_generative_gain` is flat in content scale (delta -0.0097 against a pre-registered bar of 0.05, with the residual trend inverted in sign), so the interpretive gloss that "correction needs an intact seed" is RETRACTED from `docs/architecture/sd_068_consolidation_lesion_harness.md`. The attenuation finding itself (`rem_generative_gain` 0.149, attenuating 8/8 seeds) is NOT overturned and STANDS -- it is recorded at every content scale (0.1589 / 0.1520 / 0.1493, 8/8 attenuating throughout) precisely so it stays visible. Net effect on SD-068: the staged-failure contract is carried by `nrem` plus the rebuilt `sws` (V3-EXQ-778g) only; the REM leg is not a functional-damage instrument and the generative-gain pillar does not evidence content-dependent correction. The staging order remains unsupported. NOTE a specification defect found in the course of this adjudication: V3-EXQ-778d's readiness anchor scored `railed` on the saturation rail only, against a two-rail degeneracy, capping a bit-perfect replication at 0.625 under a 0.75 gate; the anchor's underlying data reproduced V3-EXQ-778c to identical floats across three runs, so `control_passed` is asserted here on the corrected both-rails predicate. Fix routed as V3-EXQ-778h (low priority, ledger-hygiene only).

MECH-168 / INV-047 / MECH-169: `evidence_direction: unknown` (context tags; the cluster audits the instrument, not the claims -- consistent with the V3-EXQ-778c precedent).

### Documentation change required (governance, not this skill)

`REE_assembly/docs/architecture/sd_068_consolidation_lesion_harness.md` lines ~292-302: the OPEN QUESTION box on the "intact seed" gloss is **resolved** -- the gloss is retracted. The 778g re-widening note at ~361-369 explicitly lists "the generative-gain pillar's content-dependence is still open (`H-gen-gain-content-free`)" as an outstanding caution; that item is now closed, and closed in the **narrowing** direction. Neither edit widens SD-068.

---

## 7. Frozen-ledger resolutions (Step 9b, Mode B)

Question `consolidation_readout_validity`. All four legs were already pre-registered (2026-07-18T07:23:18Z / 08:41:15Z), all with `pre_registered_utc <= resolved_utc`. **No fan-out growth; `initial_frozen_count` stays 6; no `fanout_growth_events` entry and no `axis_families.map` extension are required** (all four axes -- measurement, representation, observation, readout -- are already mapped).

| hid | axis | before | after | direction | bar |
|---|---|---|---|---|---|
| `H-rem-content-contingent` | measurement | alive | **eliminated** | weakens | met (all three true) |
| `H-rem-clamp-artifact` | measurement | alive | **confirmed** | supports | control rehabilitated; `met_elimination_bar` true |
| `H-rem-genuinely-content-free` | representation | alive | **confirmed** | supports | joint 778d+778e |
| `H-gen-gain-content-free` | observation | alive | **confirmed** | supports | clean, non-degenerate as shipped |

`H-rem-content-contingent` is eliminated as the direct complement of `H-rem-genuinely-content-free` being confirmed -- the two are mutually exclusive readings of the same readout, and the joint evidence discriminates between them.

The question moves from **2/6 to 6/6 resolved**; 4 of 6 hypotheses survive as confirmed, 2 eliminated. `decision.decidable` -> **true**: the decision question ("can the staging order be read as functional damage tolerance at all, or only as noise sensitivity?") is now answerable -- **only two of three phases carry content-contingent instruments, so the staging order cannot be read as functional damage tolerance.** `decision_log_ref` stays null (human-owned).
