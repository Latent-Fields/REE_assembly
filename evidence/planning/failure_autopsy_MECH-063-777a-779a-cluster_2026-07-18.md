# Failure autopsy — MECH-063 cluster: V3-EXQ-777a + V3-EXQ-779a

- **Generated:** 2026-07-18T18:09:53Z
- **Session:** `fervent-tereshkova-2f1c69` ("MECH-063 777a/779a cluster autopsy")
- **Scope:** cluster (2 targets)
- **Status:** confirmed (interactive gate completed 2026-07-18)
- **Predecessor:** [`failure_autopsy_MECH-063-777-779-cluster_2026-07-18`](failure_autopsy_MECH-063-777-779-cluster_2026-07-18.md)
- **Provenance:** Deferred by the 2026-07-18 `/governance` cycle (session `governance-c4a10d`, route B). Governance applied no `evidence_direction` and marked neither run reviewed. Both runs are the routed fixes of the predecessor autopsy.

---

## Executive summary

Both targets superseded runs the predecessor autopsy adjudicated as artifacts. Its four fixes all landed. **The instrument repair genuinely worked — and that is what makes this cycle diagnostic**: with sampling fixed, the two sub-claims separated for the first time in this chain and now require different responses.

| | V3-EXQ-777a — sub-claim (i) | V3-EXQ-779a — sub-claim (ii) |
|---|---|---|
| Self-route | `control_axes_collinear_toward_one_scalar` | `sample_starvation_requeue` |
| Manifest direction | `weakens` | `non_contributory` |
| **Adjudicated direction** | **`non_contributory`** (corrected) | **`non_contributory`** (unchanged) |
| **Category** | **`substrate_ceiling`** | **`measurement_test_design_defect`** |
| Load-bearing criterion | FAILED — but not on collinearity | **PASSED** — withheld on a precondition |
| Re-derive brake | **FIRED** — re-queue refused | Exempt |
| Routing | `/implement-substrate` (SD-PROBE-WARMUP) | `/queue-experiment` (V3-EXQ-779b) |

Neither self-route label survived contact with the run's own numbers in the way the label implied — but for opposite reasons. 777a's label is **wrong** (the orthogonality statistic clears its margin). 779a's label is **right**, and the capability worry it might have masked is definitively ruled out.

**Answering the standing question — (a) refutation, (b) substrate ceiling, or (c) granularity debt:** **(b)**, for sub-claim (i). Not (a): the evidence points *toward* orthogonality. Not (c): all four failures reduce to one signature.

---

## Target 1 — V3-EXQ-777a (sub-claim (i), orthogonal control axes)

`v3_exq_777a_mech063_orthogonal_control_axes_dissociation_20260718T101635Z_v3`
FAIL · `weakens` · `non_degenerate: true` · `substrate_hash 8348f89d…` · ree-cloud-4 · 2.4 h · 14 seeds

### The predecessor's fixes, verified

| Fix | Verdict |
|---|---|
| **F1** sample-driven stopping | **Worked.** All 56 cells reached 250 fresh E3 selections, every cell `stopped_on: floors_met`, `starved_cells` **empty**. The 40x yield spread of 777 is gone. |
| **F2** D-saturation guard | **Applied, does not repair.** It *excludes* saturated seeds rather than reducing saturation. 777: ~4 of 5 saturated (80%). 777a: 9 of 14 (64%). Rate essentially unchanged — a false signal became a small sample. |
| **F3** per-seed R5 authority gating | **Worked.** 9 of 14 seeds correctly reported `authority_met: false`. |
| **F4** pool 5→14 + seed bar | **Partly a threshold re-expression.** Pool growth is real; `C1_SEED_FRAC = 0.75` lowered the effective bar from 4-of-5 to 3-of-4. |

All six preconditions met, as the tasking noted. The instrument *is* repaired. The reading still does not say what the label says.

### C1 did not fail on collinearity

| | 777 | 777a |
|---|---|---|
| `mean_sin_angle` | 0.530 | **0.5454** |
| `SIN_MARGIN` | 0.500 | 0.500 |
| `c1_seed_count` | FAIL (3 < 4) | **PASS (3 of 4, req 3)** |
| `c1_robust` | FAIL (0.177) | **FAIL (0.2226)** |

The mean **exceeds** the orthogonality margin and 3 of 4 informative seeds clear it. The sole failing bar is `c1_robust`. This is the **second consecutive run** whose headline orthogonality number exceeds its own margin while the self-route asserts collinearity.

And the tell that this is not a refutation: seed 17 — the one genuinely mid-range seed (`D_seed_mean` 0.497) with the strongest score-axis authority (`norm_v_score` 0.213) — gives **`sin_angle` 0.9883**, near-perfect orthogonality. Where the instrument can see, it sees the claim.

### `c1_robust` cannot be met at any sample size

Script line 697:

```python
c1_robust = (mean_sin - sd_sin) > SIN_MARGIN   # effect exceeds its own noise
```

`_pooled_std` (line 541) returns `statistics.pstdev` — the **population** SD across seeds, not a standard error. Population dispersion does not shrink with *n*, so the bar is unreachable regardless of sample size. The comment's intent ("effect exceeds its own noise") is sound; the denominator conflates seed-to-seed initialisation variability with measurement noise.

Repairing it to standard-error form is **necessary but not sufficient**:

| n informative | SE | mean − SE | passes |
|---|---|---|---|
| 4 (actual) | 0.161 | 0.384 | no |
| 14 | 0.086 | 0.459 | no |
| 25 | 0.065 | 0.481 | no |
| **51** | 0.045 | 0.500 | **yes** |

At the observed mean (0.545) and dispersion (0.323) the design needs **~51 informative seeds**. Observed informative yield is **4 of 14 = 28.6%** → **~177 raw seeds → ~31 h**. Infeasible.

### The yield is substrate-gated, not sampling-gated

**`corr(distance of D_action_mass_mean from saturation, norm_v_score) = 0.884`** across all 14 seeds.

The score axis's measurable authority is very largely *determined* by how far the action-value mass sits from its 0/1 bounds. Where `D` is pinned, the score-bias lever has nothing to act on, its effect vector collapses toward zero, and the angle against a large temperature vector becomes numerically ill-conditioned.

Supporting numbers:

- regimes: **7 ceiling, 5 headroom, 2 floor**; `authority_met` true on only 5 of 14
- median magnitude asymmetry `v_temp / v_score` = **8.1x**
- `corr(v_score, sin)` = **0.315 over all 14** but **0.028 within the informative pool**

That last contrast is decisive: within the surviving pool the angle does *not* track score-axis magnitude, so no weak-axis-implies-collinear artifact contaminates the informative seeds. The 0.315 is carried entirely by the saturated seeds — which is precisely why F2 excluding them was correct.

**Why this is substrate and not sampling.** `D_action_mass` saturation is a property of an *untrained* agent's degenerate E3 action-value distribution: either one action dominates (D→1) or values are flat (D→0). It is invariant to how long a cell is sampled. 777a gave every cell 250 clean selections and the saturation rate barely moved from 777's starved run. **Sampling was the binding constraint in 777; it demonstrably is not in 777a.**

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | not expressible on 9 of 14 seeds; on the 4 where it was, 3 cleared the margin |
| Biological reference | clear | LC-NE tonic/phasic adaptive gain; failure matches a dynamic-range floor, not a missing dependency |
| Prerequisites | present | MECH-320 and MECH-313 live, confirmed by all six preconditions |
| Implementation | complete | both regulators on the real production E3 `select()` path |
| Environment | wrong pressures | untrained agent in hazard-terminating 8x8 → degenerate action-values on ~64% of seeds |
| Measurement | under-instrumented | `c1_robust` uses population SD where a standard error is intended |
| Integration | coupled | both axes route to the same E3 softmax by design |
| Scale | likely insufficient | 28.6% informative yield caps power; ~51 needed, 4 obtained |

**Biological dependency discovered.** A gain/bias regulator is only observable when the distribution it modulates has dynamic range. In brains that range comes from a trained, non-degenerate action-value landscape. Its absence here is a genuine prerequisite surfaced by the FAIL — not a falsification, and arguably positive evidence for the dependency.

### Re-derive brake — **FIRED**

Prior `substrate_ceiling`/`non_contributory` autopsies tagging MECH-063: **1** (the predecessor). This makes **2**, meeting `RE_DERIVE_BRAKE_THRESHOLD`.

> **A further lettered iteration of the orthogonal-control-axes probe against an untrained agent (a hypothetical V3-EXQ-777b) is REFUSED.**

The predecessor warned that 777a must fix the sampling model rather than nudge a threshold. F1 and F3 *were* genuine fixes and did work — but the run still landed a third consecutive instrument-defect reading, and the power analysis shows no instrument repair alone reaches the bar. Build `SD-PROBE-WARMUP` first. A redesign testing a *different* mechanism under a new EXQ number remains permitted.

**Routing:** `/implement-substrate` → `SD-PROBE-WARMUP` (substrate_queue `action: create`, priority 1).

---

## Target 2 — V3-EXQ-779a (sub-claim (ii), tonic/phasic dissociation)

`v3_exq_779a_mech063_tonic_phasic_dissociation_20260718T121351Z_v3`
FAIL · `non_contributory` · `non_degenerate: false` · `substrate_hash 765ce9d2…` · ree-cloud-4 · 2.0 h · 5 seeds

### The load-bearing criterion PASSED

`double_dissociation_C1_and_C2`: **`passed: true`**, `criteria_non_degenerate: true`, `robust: true`, `diss_seed_count: 4` = `min_seeds: 4`.

| Metric | Value | Margin |
|---|---|---|
| `mean_dS_tonic` | +0.2654 (sd 0.0722) | `SUSTAINED_MARGIN` 0.05 |
| `mean_dR_phasic` | −0.0484 (sd 0.0373) | `TRANSIENT_MARGIN` 0.02 |

It was withheld solely because `phasic_fires_real_events` measured **6** against threshold **10**, aggregated as a MIN across cells and sourced entirely from **seed 23 / T1P1**.

### The self-route mismatch, adjudicated

**Question:** is `sample_starvation_requeue` right, or is SD-069 genuinely not firing (a capability question)?

**Verdict: SAMPLING. The capability reading is ruled out.** The manifest's own classification (`kind: "sample"`, `readiness_unmet_capability_kind: []`) is correct.

Evidence:

1. **`burst_level_max = 1.00` in every PHASIC-ON cell**, including *both* seed-23 cells. SD-069 fires at full amplitude on the offending seed.
2. **Firing rate on seed 23 is normal.** Event ticks per 1000 env steps: seed 23 → 7.19 (T1P1) and 11.86 (T0P1). Seed 29 → 8.75 and 9.58, i.e. *lower* than seed 23's T0P1. No rate anomaly.
3. **The shortfall is fully explained by exposure.** Seed 23 received 835/843 env steps against 2400 for every other cell. Scaling seed 29's rate to 835 steps predicts ~7.7 ticks; 6 observed.

**Root cause: the 120-EPISODE cap, not the 2400-step cap.** Seed 23 dies in ~7 steps per episode, so 120 episodes exhausted at 835 steps — **35% of the exposure every other cell received**. It is the *only* cell reporting `stop_reason: episode_cap`; all 15 other starved cells report `step_cap`.

**Structural reading:** F1 fixed the stopping *rule* but left the *cap* episode-denominated. The original 777/779 defect — an episode-denominated budget silently truncating fast-dying seeds — **reappeared one layer down on the same seed**. The fix moved the bottleneck rather than removing it.

### The withholding is nonetheless correct

The gate is **not** mis-scoped. Seed 23 is one of the four dissociating seeds (11, 23, 29, 37 dissociate; 17 fails C2) and carries the **largest phasic effect of any seed** — `dR_phasic = −0.108` — estimated on just **6 event ticks**. Excluding seed 23 leaves 3 dissociating seeds against `min_seeds` 4, so the run would fail on seed count. **The PASS genuinely depends on the under-exposed cell**, and the precondition correctly refused to bank it.

Contrast with the predecessor: in 779 the min-across-cells gate was criticised for letting a *non-contributing* dead cell veto a working run. Here the vetoing cell **is** a contributor, and the strongest one. Same rule, legitimate work. **Do not "fix" the min-aggregation — fix the exposure.**

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact, **nearly demonstrated** | dissociation held robustly on 4 seeds |
| Biological reference | clear | SD-069 is the phasic complement to MECH-313 tonic on one readout |
| Prerequisites | present | SD-069 implemented, wired, firing at normal rate everywhere |
| Implementation | complete | — |
| Environment | adequate for mechanism, adverse for exposure | ~7-step episodes on seed 23 |
| Measurement | adequate | the gate correctly caught that the strongest contributor rests on 6 ticks |
| Integration | coupled | tonic and phasic share the temperature readout by design |
| Scale | insufficient on one cell only | 6 ticks vs 30 target, from a cap binding at 835 of 2400 steps |

**Brake:** exempt. This lineage is not circling a substrate ceiling — its criterion passed non-degenerately and it is one parameter from adjudication. Refusing V3-EXQ-779b would discard a nearly-complete result rather than prevent a re-derive loop.

**Routing:** `/queue-experiment` → V3-EXQ-779b, **not blocked on SD-PROBE-WARMUP**.

---

## Cluster pattern

**Shape.** Both runs inherit one root — per-seed heterogeneity in an untrained agent inside a hazard-terminating environment — but it now expresses through two **different channels**, and the predecessor's fixes cleanly separated them:

- **777a → dynamic range.** The score axis's DV is saturated on 64% of seeds, capping informative yield at 28.6%.
- **779a → exposure.** One fast-dying seed is truncated by an episode-denominated cap at 35% of the steps other cells received.

**Independent bugs?** No. Seed-level heterogeneity is the single upstream property. The predecessor diagnosed it as a *sampling* defect and fixed sampling; sampling is now demonstrably repaired in 777a and the saturation rate barely moved — proving sampling was never the binding constraint for sub-claim (i). What the repair achieved was to **separate the two channels** so each could be diagnosed on its own terms.

**The divergent routing is itself the finding.** This is the first iteration in the chain where the two sub-claims do *not* share a diagnosis. Treating them as one undifferentiated cluster from here would hold a nearly-complete result hostage to a substrate build it does not need.

### Seed 23 — the recurring pathological seed

| Run | Seed 23 |
|---|---|
| 777 | 21 of 900 steps; D at floor (0.002–0.013) |
| 779 | 21 steps; 19-step cell vetoed readiness |
| 777a | 250 selects obtained (sampling fixed); `D_seed_mean` 0.0099, floor, `authority_met: false` — excluded |
| 779a | 835 of 2400 steps via `episode_cap`; 6 event ticks; vetoed readiness **and** carried the largest phasic effect |

### Reading adjudication

- **substrate_enrichment** — **ACCEPTED for sub-claim (i)**, as *training-regime* substrate (a non-degenerate action-value landscape for the regulator to act on), **not** a `ree_core` mechanism gap. Both regulators under test are present and live.
- **test_design_ceiling** — **ACCEPTED as secondary** for sub-claim (i) (`c1_robust`'s population-SD denominator), **rejected as dominant** because repairing it still leaves ~51 informative seeds needed at a 28.6% yield. **ACCEPTED as the sole reading** for sub-claim (ii), where it is a one-parameter cap denomination.

---

## Granularity debt — GOV-GRAN-1 P1, adjudicated

The audit fired a P1 `unflagged_recurrence` on MECH-063 (2 hits, 2 distinct signatures, chain 777 → 779), now a 4-run chain.

**VERDICT: NOT granularity debt → coherent substrate-build campaign circling one buildable gap**, matching the 460e..i lineage the `/failure-autopsy` docstring cites and the MECH-180 worked example.

All four failures share a **single upstream signature** — per-seed heterogeneity in an untrained agent in a hazard-terminating environment — recurring in **successively narrower locations** rather than as structurally distinct mechanisms:

> episode-denominated **budget** (777, 779) → dependent-variable **saturation** capping informative yield (777a) → episode-denominated **cap** truncating one contributor (779a)

Each iteration eliminated the previous location and exposed the next. That is progressive localization, not bundled mechanisms.

Two further facts weigh against the coarse-claim reading:

1. The two sub-claims are cleanly **separable and are visibly separating** — in this cycle they took different epistemic categories, different routings, and different brake dispositions for the first time.
2. **Neither sub-claim produced a falsification a finer child claim would have caught.** Sub-claim (ii) in fact *passed* its load-bearing criterion.

No `/claim-synthesis` handoff. Re-evaluate if a future iteration produces a failure signature that does **not** reduce to per-seed heterogeneity.

---

## Claim disposition — MECH-063

**Status: provisional → provisional. Do not demote.**

The demotion threshold (tested fairly + biology supports + still fails) is not met for either sub-claim. Sub-claim (i) was not tested — 9 of 14 seeds could not express it, and on the 4 that could, 3 cleared the margin with the best-conditioned seed at 0.988. Sub-claim (ii) *passed* robustly and was withheld only on one contributor's estimate reliability.

**Post-adjudication evidence state:** ZERO experimental entries; 2 literature supports (0.79, 0.81) from one 2005-era LC-NE / neuromodulator pull. The predecessor withdrew 777's artifact `weakens`; this withdraws 777a's.

**Narrow-supports check:** no illusory support is manufactured. The claim's own flags (`lit_only_above_cap`, `low_exp_conf`, `synthetic_signals_only`) already assert this posture. **MECH-063 is UNTESTED — not supported, not weakened.**

Retain flags: `lit_only_above_cap`, `low_exp_conf`, `synthetic_signals_only`.

---

## Learning extracted

**From 777a**

1. A robustness bar written as `mean − pstdev > margin` is **not sample-size-improvable**. Where the intent is "effect exceeds its own noise", the standard error is the correct denominator; conflating seed variability with measurement noise makes a load-bearing criterion structurally unreachable.
2. **Excluding a degenerate sample is not repairing it.** F2 correctly stopped saturated seeds contributing a false angle but left the *rate* untouched, converting a false signal into an underpowered one. The honest next question is why the rate is 64%, not how to filter it.
3. A gain/bias regulator is only measurable when the distribution it modulates has dynamic range. `corr = 0.884` is the quantitative form of that prerequisite — a genuine biological dependency discovered by the FAIL.
4. **Quantify the power ceiling before authorising another iteration.** Computing "seeds required at observed effect and dispersion" is cheap and is what converts "the bar is too strict" into a decidable substrate-vs-instrument verdict.
5. An auto-derived `evidence_direction` produced a **second consecutive artifact `weakens`** on MECH-063 from a criterion that never tested collinearity. A self-route label contradicting its own headline statistic twice is a signal about the labelling logic.
6. Distinguishing **within-pool from across-pool correlation** was decisive (0.028 vs 0.315) — it ruled out artifact contamination of the surviving seeds.

**From 779a**

7. **Fixing a stopping RULE does not fix an episode-denominated CAP.** The identical starvation mechanism reappeared one layer down on the identical seed. When retiring a denomination bug, audit *every* budget in the file.
8. **`stop_reason` is the discriminating diagnostic** — 15 cells `step_cap` vs the one decisive `episode_cap`. Recording it per-cell made this a one-command diagnosis.
9. **A rate check separates capability from exposure cheaply.** Normalising to ticks per 1000 steps showed seed 23 firing *inside* the range other seeds span. Raw counts alone would have supported the opposite conclusion.
10. The **sample-vs-capability precondition `kind`** introduced by this iteration worked as designed and is why the 779 mislabelling did not recur. Keep it in the template.
11. **A min-across-cells gate is legitimate when the offending cell contributes** and pathological when it does not. The same rule was wrong in 779 and right in 779a — the discriminating question is participation, not aggregation.

---

## Recommended follow-ups

| # | Type | Skill | Detail |
|---|---|---|---|
| 1 | Substrate build | `/implement-substrate` | **`SD-PROBE-WARMUP`** priority 1 — trained-enough agent substrate for the read-only telemetry-probe family. Target: majority of seeds with `D_action_mass_mean` strictly inside (0.05, 0.95). Record realised per-seed saturation so yield is auditable. **Brake-enforced gate for sub-claim (i).** |
| 2 | Same-question re-queue | `/queue-experiment` | **V3-EXQ-779b** — step-denominate the per-cell cap so `max_env_steps_per_cell` binds for every cell. Keep the min-across-cells aggregation and the sample/capability `kind`. **Not blocked on #1.** |
| 3 | Shared lib | `/queue-experiment` | `experiments/_lib/` rollout helper (carried forward, now extended): budgets **and caps** denominated in the same unit as the gates that consume them; emit per-cell `stop_reason` and realised counts. |
| 4 | Probe template fix | `/queue-experiment` | Retire the mean-minus-population-SD robustness idiom. Use the standard error for "exceeds its own noise"; state "holds on essentially every seed" as a seed-fraction bar. |

### Follow-up 4 — carrier survey and resolution (2026-07-18, session `intelligent-poincare-f59a5a`)

**No experiment script was edited. Every carrier of the idiom is already-run or frozen**, so the retirement had to be prospective. Full survey of `ree-v3/experiments/` for `_pooled_std` / `pstdev`:

| Script | Bar | MARGIN | Status | Disposition |
|---|---|---|---|---|
| `v3_exq_777a_..._orthogonal_control_axes_dissociation.py:697` | `mean_sin - sd_sin > SIN_MARGIN` | **0.500** | RAN (manifest `20260718T101635Z`) | **The confirmed defect.** Autopsy matter — not retro-edited. |
| `v3_exq_777_..._orthogonal_control_axes_dissociation.py:416` | same idiom | — | RAN (`20260717T155914Z`) | Predecessor. Not retro-edited. |
| `v3_exq_779a_..._tonic_phasic_dissociation.py:676` | `abs(mean) - _pooled_std > 0.0` | **0.0** | RAN (`20260718T121351Z`) | Conservative form — see below. Criterion **PASSED**. |
| `v3_exq_779_..._tonic_phasic_dissociation.py:469` | same, margin 0.0 | 0.0 | RAN (`20260717T191826Z`) | Conservative form. |
| `v3_exq_779b_..._tonic_phasic_dissociation.py:751` | same, margin 0.0 | 0.0 | **QUEUED**, pending `ree-cloud-4` | **Deliberately untouched** — supersession contract. |
| `v3_exq_760_mech303_contextual_safety_terrain_discrimination.py:423` | `mean_margin - sd_margin > 0.0` | 0.0 | RAN (`20260714T202728Z`), **PASS/supports**, claim **MECH-303** | Conservative form. Carrier **outside** the MECH-063 family — not previously identified. |

**The key distinction, which makes a blanket rewrite wrong.** The consequence of the idiom depends entirely on `MARGIN`:

- **`MARGIN > 0` compounds into unreachability.** A non-shrinking dispersion is subtracted *and* a positive bar must still be cleared. This is 777a alone, and it is the confirmed defect.
- **`MARGIN == 0` reduces to `mean > dispersion`, which is a *conservative* bar** — strictly *harder* than the SEM form it was mistaken for, since `pstdev >= pstdev/sqrt(n)` for all `n >= 1`. The five margin-0.0 carriers therefore cleared (or failed) a **stricter** test than intended. **779a's and 760's PASSes are not undermined by this defect** and must not be "corrected" as though they were — re-denominating a bar a run already cleared would loosen it retroactively. In particular **MECH-303 needs no `evidence_quality_note`**: 760 passed a harder bar than the one it meant to set.

That distinction is also the independent, mechanism-level reason the brief's instruction to leave **779b** alone is correct, not merely procedural.

**What landed instead:** `ree-v3/experiments/_lib/robustness_bars.py` (new), so the successor author (777b / 779c) has a correct bar to import rather than another copy to make:

- `robust_by_sem(vals, margin, k, min_n)` — `mean - k*SEM > margin`, the replacement where the intent is "exceeds its own measurement noise". Tightens with `n`; `k` is pre-registered and emitted.
- `exceeds_cross_seed_dispersion(vals, margin, min_n)` — the dispersion bar kept but **named**, returning `sample_size_improvable: False` for the manifest, and flagging `margin_compounds_unreachability` when `margin > 0`.
- `seeds_required_for_sem_bar(...)` — the design-time cost check. Validated against this autopsy's own recorded figures: reproduces `SE` at n=4/14/51 (0.1614 / 0.0863 / 0.0452) and `n_informative_required = 51` exactly. (`raw_seeds_implied` 179 vs the autopsy's 177 — the helper ceils informative-`n` before dividing by yield, the more conservative order.)

The module's docstring carries the autopsy's sharpest finding up front: **repairing the denominator is necessary but not sufficient** — 777a's numbers still fail the corrected bar at n=4 and n=14, needing ~51 informative seeds (~177 raw, ~31 h) at the observed 28.6% yield. The binding constraint was the **yield**, which is follow-up #1's `SD-PROBE-WARMUP`, not this criterion.

**Seed-fraction bar (second half of follow-up 4): already present, no action.** 777a's `c1_seed_count` is exactly that bar, and it **PASSED** at 3 of 4 informative seeds. The defect was never the absence of a seed-fraction criterion.

`pytest tests/` — **1628 passed**, 39 subtests passed.

---

## Hypothesis-space ledger (Step 9b)

Question **`control_plane_rank`** — Mode B resolve only. **No growth**; 777a and 779a were already pre-registered as `adjudicating_runs` by the predecessor autopsy. Axes (`representation`, `drive`) are already in `axis_families.map`.

| Hypothesis | State | Update |
|---|---|---|
| `H-rank2-score-temp` | **alive** | `control_passed` **true** and `non_degenerate` **true** for the first time (all six preconditions met), but a `non_contributory` substrate-ceiling reading discriminates nothing. Bar not met. |
| `H-rank2-tonic-phasic` | **alive** | Significant update: its criterion **PASSED** robustly and is withheld only on one contributor's exposure. `non_degenerate` false → bar not met. |
| `H-collapse-one-scalar` | **alive** | Both runs produced evidence pointing **away** from it, but neither cleared the elimination bar, so **no bits may be claimed**. |

**Reduction this cycle: 0 of 3 eliminated. Four runs now spent on this question across two cycles, zero bits removed.** That is the honest headline, and it is the reason the brake firing is appropriate: the question is not being narrowed by more iterations of the same instrument against the same substrate.

**Observation bottleneck** — sub-claim (i): informative-seed yield capped at 28.6% by action-value saturation in an untrained agent. Sub-claim (ii): one contributing cell truncated to 35% exposure by an episode-denominated cap.

---

## Handoff to `/governance`

Governance applies; this autopsy does not write claims, manifests, `review_tracker`, or `substrate_queue`.

1. **V3-EXQ-777a** — set `evidence_direction: non_contributory` (**overwriting the auto-derived `weakens`**), `epistemic_category: substrate_ceiling`, write the `evidence_quality_note` from the JSON target, set `pending_retest_after_substrate: true`.
2. **V3-EXQ-779a** — keep `evidence_direction: non_contributory`, set `epistemic_category: measurement_test_design_defect`, write its `evidence_quality_note`.
3. **MECH-063** — no status change. Update `notes` with `claim_disposition.suggested_claim_note`; add `granularity_debt_recurrence_note`; retain the three flags.
4. **substrate_queue.json** — create `SD-PROBE-WARMUP` from `targets[0].recommended_substrate_queue_entry` (`action: create`, priority 1, with the failure record).
5. **Ledger** — Mode B resolve applied to `control_plane_rank`; all three legs remain alive; no growth event.
6. **review_tracker** — this skill does not mark either run reviewed; both remain pending for the next governance walk.
