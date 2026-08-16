# Failure Autopsy -- V3-EXQ-922a (SD-016 / MECH-152 soft-selection ablation)

**Status: `awaiting_human_confirmation` (STAGING MODE -- headless, no user present).**
Steps 1-7 and 9 were run in full; Step 8 (the interactive scientific-judgment gate) was
skipped and the routing below is a **draft**, not a confirmed disposition. Step 9b was
drafted only -- nothing was written to `hypothesis_space_registry.v1.json`; the intended
pre-registration/resolution is carried in the companion JSON under
`hypothesis_space_ledger_pending`.

- **Generated:** 2026-08-16T18:26:47Z
- **Target:** `v3_exq_922a_sd016_mech152_softsel_ablation_20260814T183708Z_v3` (`V3-EXQ-922a`)
- **Outcome as recorded:** PASS | `experiment_purpose: diagnostic` | `evidence_direction: mixed`
- **Self-routed label:** `selection_hardness_partial_recovery`
- **Claims tagged:** MECH-152 (single)
- **Scope:** single (not a cluster -- see Section 1d)

**Why this autopsy exists.** `experiment_purpose: "diagnostic"` -- ALL diagnostics require
this skill, PASS or FAIL, flagged or not (2026-08-07 user-instructed correction). The run
carries no `adjudication` flag; "cleared its own preconditions" is exactly what a vacuous or
confounded pass would also show. It also discharges the specific adjudication the 2026-08-16
`/governance` cycle deferred to (Section 8).

---

## 1. Facts -- reconstruction before interpretation

### 1a. Dry-run gate (Step 2a) -- CLEAN

```
scripts/check_dry_run_citations.py v3_exq_922a_sd016_mech152_softsel_ablation_20260814T183708Z_v3
-- 0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown   (exit 0)
```

| run_id cited | `dry_run` | role |
|---|---|---|
| `v3_exq_922a_sd016_mech152_softsel_ablation_20260814T183708Z_v3` | `false` | target |
| `v3_exq_922_sd016_mech151_152_arc041_production_combo_20260812T035119Z_v3` | `false` | prior autopsy context only, not a population member |

`excluded_dry_run_ids: []`. No smoke is admitted anywhere in this diagnosis, and no
population statistic is quoted over a mixed real/dry denominator.

**Criterion-reachability lint** (`validate_experiments.py --checks dry_run_unreachable_criterion`)
fires on 11 drivers, all in the `v3_exq_543` lineage (b through l). It is **silent on
`v3_exq_922a_...`**. Per the skill this is a net, not a substitute -- but with no dry manifest
in scope at all, the driver-side truncation trap cannot apply here, and the manual read of the
dry-run reduction block is moot for adjudication purposes.

### 1b. Recording provenance -- COMPLETE

`ree-v3/validate_recording.py --paths <manifest>` -> **OK, 1 complete, 0 always-core gaps,
0 thin-pack provenance drops, 0 schema warnings.** `recording_schema: rec/v1`,
`substrate_hash: de92958c...cece88`, `substrate_stable_across_run: true`,
`machine: ree-worker-3`, `machine_class: linux-x86_64-py3.10-torch2.12.0+cpu`,
`elapsed_seconds: 79.50`, full `config`, explicit `seeds: [42,43,44]`.

**This is not a footnote and it deserves saying plainly: the recording quality of this run is
what made this autopsy possible.** The driver recorded `w_harm_std`, `w_goal_std`,
`hazard_std`, `n_collection_steps` and `final_terrain_loss` per arm per seed, none of which
any scored criterion consumes. Those five optional fields are the entire basis of Sections 2
and 3 below. There is **no recording debt here** -- the opposite.

### 1c. Design (from the driver and the queue entry)

3 arms x 3 seeds [42,43,44], 9 cells, all 9 ready (`n_seeds_ready: 3`). MECH-152 terrain
machinery identical to V3-EXQ-922. Phased P0a=60 / P1=40 episodes, 150 steps/episode,
`context_switch_every: 5`, `collection_episodes: 20`, `lambda_terrain: 0.1`, `lr: 1e-4`.

| arm | `cue_slot_tagger` | `selection` | `ctxdiv_weight` | declared role |
|---|---|---|---|---|
| `A0_OFF` | False | soft | 0.0 | MECH-150 C2 saddle **control**; reproduces 922's closest-to-threshold arm |
| `A1_PRODUCTION` | True | gumbel | 0.5 | reproduces 922's collapse in-run |
| `A2_SOFTSEL` | True | **soft** | 0.5 | **THE ABLATION** -- differs from A1 in the selection operator ONLY |

Primary contrast A2 vs A1 is a genuine clean 1-knob ablation. That design intent is sound and
is executed exactly as specified; nothing below is a complaint about the ablation logic.

Thresholds inherited from V3-EXQ-194a: `r_w_harm > 0.5` (C1), `r_w_goal < -0.3` (C2).
`RECOVERY_MARGIN = 0.15`, stated as "grounded in 922's ~0.35 A0-vs-A1 gap".

### 1d. Single, not a cluster

The only other autopsy tagging MECH-152 is `failure_autopsy_V3-EXQ-922_2026-08-13` (confirmed),
which this run is the designated follow-on to and which it explicitly does **not** supersede.
There is no third run sharing the shape, and the sibling SD-016 work (V3-EXQ-898, V3-EXQ-908,
`sd016_selection_fanout_portfolio_scope_staged_20260809.md`) is about **retrieval selectivity**,
a different DV. Cluster scope would be manufactured; Step 6 does not apply.

### 1e. What was actually scored, and what was not

```
interpretation.criteria = [
  {"name": "a2_retrieval_selective_premise",      "load_bearing": true, "passed": true},
  {"name": "a2_terrain_nondegenerate_premise",    "load_bearing": true, "passed": true}
]
```

**Both load-bearing criteria are premises. There is no scored mechanism criterion in this
run at all.** The MECH-152 thresholds (C1/C2) are evaluated in `acceptance_checks` and drive
the *label*, but they are not `criteria[]` entries and therefore do not gate the PASS/FAIL
outcome. The driver states this deliberately:

> "outcome PASS = a real discrimination was produced ... A diagnostic PASS/FAIL is about
> whether the probe RAN meaningfully; the scientific reading lives in the label."

That is an honest and defensible convention -- **but it means the PASS certifies readiness,
not a finding.** Section 4 takes up whether the label it delegates to is trustworthy.

### 1f. Preconditions as recorded

| precondition | measured | threshold | direction | met |
|---|---|---|---|---|
| `seed_readiness_majority` | 3.0 | 2.0 | lower | true |
| `a2_softsel_retrieval_entropy_selective` | 2.457597 | 2.5 | **upper** | true |
| `a2_softsel_retrieval_ctxdiv_selective` | 0.654469 | 0.1 | lower | true |
| `a2_softsel_terrain_series_nondegenerate` | 3.0 | 2.0 | lower | true |

`criteria_non_degenerate`: `a2_retrieval_selective` true, `a2_terrain_series_nondegenerate`
true, `a1_terrain_series_nondegenerate` true.

### 1g. Measurements

Per-arm means over 3 ready seeds:

| arm | `sel_entropy` | `sel_ctx_div` | **`r_w_harm`** | **`r_w_goal`** | **`w_harm_std`** (per seed) | `final_terrain_loss` (per seed) |
|---|---|---|---|---|---|---|
| `A0_OFF` | **2.772586** | 0.000117 | **0.35590** | **-0.35480** | 3.75e-07, 1.39e-06, 6.80e-07 | 8.09e-04, 7.21e-03, 7.10e-04 |
| `A1_PRODUCTION` | 1.10e-08 | 1.0625 | 0.00131 | -0.00768 | 2.47e-03, 1.94e-03, 7.08e-03 | 1.03e-05, 4.31e-03, 7.55e-05 |
| `A2_SOFTSEL` | 2.457084 | 0.565516 | 0.18525 | -0.18119 | 1.53e-03, 1.72e-04, 1.03e-02 | 1.30e-05, 4.30e-03, 1.07e-04 |

Per-seed (seed 42 / 43 / 44):

| arm | `sel_entropy` | `r_w_harm` | `r_w_goal` |
|---|---|---|---|
| `A0_OFF` | 2.7726 / 2.7726 / 2.7726 | 0.4646 / 0.2963 / 0.3069 | -0.4578 / -0.2924 / -0.3142 |
| `A1_PRODUCTION` | 0.0 / 0.0 / 0.0 | 0.0922 / -0.0475 / -0.0408 | -0.0983 / 0.0371 / 0.0381 |
| `A2_SOFTSEL` | **2.3474 / 2.5662 / 2.4576** | 0.3824 / 0.1771 / -0.0037 | -0.3820 / -0.1653 / 0.0037 |

Seed-majority scoring against the 194a thresholds (majority = 2 of 3):

| arm | C1 `r_w_harm > 0.5` | C2 `r_w_goal < -0.3` | scored `pass` |
|---|---|---|---|
| `A1_PRODUCTION` | 0/3 | 0/3 | **false** |
| `A2_SOFTSEL` | 0/3 | 1/3 | **false** |
| `A0_OFF` (control -- **not scored for MECH-152**) | 0/3 | **2/3 -- would PASS on majority** | (n/a) |

`recovery`: `harm_recovery_A2_minus_A1 = 0.18395`, `goal_recovery_A1_minus_A2 = 0.17351`,
`recovery_margin = 0.15`, `substantial_recovery: true`.

`hazard_std` 0.19-0.25 on every cell -- the hazard field genuinely varies. That side of the
correlation is fine. `uniform_reference = 2.772589 = ln(16)`.

---

## 2. The four sharp edges, tested rather than assumed

### 2a. The thin margin on `a2_softsel_retrieval_entropy_selective` -- direction is DECLARED, and it is a CEILING

**The precondition declares `"direction": "upper"` explicitly.** So the indexer's
`_precondition_direction` default-to-floor path is never taken, and measured (2.4576) below
threshold (2.5) is correctly MET. The run did **not** escape a `precondition_unmet` flag by
omission or by an indexer default -- the driver states the bound direction, and the direction
it states is the right one (low entropy = selective retrieval). **This sharp edge is clean.**

**But the margin does not survive the seed scatter, and one seed openly violates it.**

- A2 per-seed `sel_entropy`: 2.3474, 2.5662, 2.4576. Sample SD = **0.1094**.
- Margin to the ceiling: 2.5 - 2.4576 = **0.0424 = 0.39 SD**.
- `c1_seeds_pass: 2` of 3 -- **seed 43 measures 2.5662, above the ceiling. It fails.**

The reported `measured` value is the **majority-order statistic** (the median, seed 44), not the
mean, so the precondition is cleared by a median sitting 0.39 SD inside a bound that a third of
the sample is outside. A margin roughly 2.6x smaller than the across-seed scatter, with a
declared violator in the sample, is not a cleared premise in any robust sense -- it is a
coin-flip that landed. **For a criterion marked `load_bearing: true` on a 3-seed run, this is
too thin to carry the interpretation the run hangs on it.**

**And the threshold sits almost on top of the degeneracy floor.** The saddle is
`ln(16) = 2.77259` (which `A0_OFF` reproduces to 5 decimal places on all three seeds); full
selectivity is entropy 0, which `A1_PRODUCTION` reaches (1.1e-08). The available dynamic range
is therefore 2.77259, and:

| point | entropy | % of range moved from the uniform saddle toward one-hot |
|---|---|---|
| `A0_OFF` saddle control | 2.77259 | 0.0% |
| C2 "certified degenerate" floor | 2.65 | 4.4% |
| **C1 "selective" ceiling** | **2.5** | **9.8%** |
| **`A2_SOFTSEL` median** | **2.4576** | **11.4%** |
| `A1_PRODUCTION` | ~0 | 100% |

So "selective retrieval" is operationally defined as **anywhere past 9.8% of the way off the
saddle**, and A2 clears it at 11.4%. The failing seed (2.5662) lands in the 4.4%-9.8% no-man's
land between "certified degenerate" and "selective". A2's retrieval is far closer to the
degenerate control than to genuine selection.

*(Cross-finding for governance, outside this autopsy's scope: the frozen-ledger question
`sd016_retrieval_selectivity_mechanism` carries `H1-drive-context-divergence` as `confirmed`.
The strongest in-run corroboration of that leg available here -- A2's ctxdiv 0.566 with entropy
2.4576 -- clears its own selectivity bar by 0.39 SD with 1/3 seeds violating. That does not
overturn H1, which rests on other runs, but it is worth a look during the next walk.)*

### 2b. Both load-bearing criteria are premises -- so is the PASS vacuous?

**As a mechanism verdict: yes, and demonstrably so, though not for the reason the wording
suggests.** The two `criteria[]` entries assert only that the probe was interpretable
(retrieval was selective; the terrain series was non-degenerate). Neither is a finding about
MECH-152. The MECH-152 result is that **A2_SOFTSEL FAILS both 194a thresholds** -- C1 0/3
seeds, C2 1/3 seeds, `mech152_A2_SOFTSEL.pass: false`. So does A1 (0/3, 0/3). **No arm in this
run passes MECH-152's criteria.**

The whole scientific reading is delegated to `interpretation.label`, which is computed from
exactly three inputs (driver, the `else` branch): `a1p`, `a2p`, and `subst` (the A2-vs-A1
recovery). **The control arm A0_OFF never enters the label decision at all** -- the driver says
so on purpose ("A0_OFF C2 ... reported in `acceptance_checks` as CONTEXT, not as
adjudication-gating preconditions"). And there is **no label branch for "the OFF control
outperforms both selection arms"**, which is precisely what happened. The five pre-registered
branches cover A2-vs-A1 in every combination and the control in none.

That matters because the control did not merely pass -- it **won**:

| arm | retrieval selectivity | `r_w_harm` | `r_w_goal` |
|---|---|---|---|
| `A0_OFF` -- cue-indexing **OFF**, ctx-div 0.0001 (no context conditioning at all) | none (uniform saddle) | **0.3559** | **-0.3548** |
| `A2_SOFTSEL` -- partially selective, ctx-div 0.566 | 11.4% off saddle | 0.1853 | -0.1812 |
| `A1_PRODUCTION` -- fully selective, ctx-div 1.06 | 100% (one-hot) | 0.0013 | -0.0077 |

**The DV is monotonically DECREASING in cue-indexed retrieval selectivity, across all three
arms, on both components.** MECH-152 asserts that a *cue-indexed* E1 context vector drives
terrain_weight. The arm with no cue-indexing and a near-constant `cue_context`
(`sel_context_divergence = 0.000117`) produces the strongest hazard/terrain correlation, and
would clear C2 on a seed majority. Whatever generates `r_w = 0.356` in `A0_OFF` **cannot be the
MECH-152 pathway**, because in that arm the pathway's input barely varies with context.

This is the substrate-ceiling fingerprint's angrier cousin: the classic tell is "negative
control passes, discrimination fails". Here the negative control does not just pass, it beats
both experimental arms and the discrimination criteria fail everywhere. That is not a ceiling
signature -- it is an **instrument-invalid signature**.

So: the PASS is not vacuous in the sense of a degenerate gate clearing itself (the premises are
real, and the 1-knob A1->A2 contrast is a genuine measurement). It is vacuous **as a MECH-152
verdict**: it certifies the probe ran, delegates the science to a label whose decision rule
excludes the arm that inverts its reading, and no scored criterion touches the claim.

### 2c. What "partial recovery" quantitatively means

`selection_hardness_partial_recovery` fires on `(not a2p) and subst`, where
`subst = harm_recovery > 0.15 and goal_recovery > 0.15`.

**Against the 194a bar** -- the reference the label's own name implies recovery *toward*:

| component | A1 | A2 | 194a bar | A2 as % of bar | **shortfall** |
|---|---|---|---|---|---|
| `r_w_harm` | 0.00131 | 0.18525 | > 0.5 | **37.1%** | 0.31475 |
| `r_w_goal` | -0.00768 | -0.18119 | < -0.3 | **60.4%** | 0.11881 |

**Against the A0_OFF control in the same run** -- A2 is not a recovery at all but a
**regression**: -0.1706 on harm (0.3559 -> 0.1853) and -0.1736 on goal magnitude
(0.3548 -> 0.1812). The A2-vs-A1 gain and the A2-vs-A0 loss are the same size to two decimal
places, because the three arms sit on a monotone ladder.

**Against its own noise** -- and this is the decisive one:

| | recovery | A2 across-seed SD | verdict |
|---|---|---|---|
| harm | 0.18395 | **0.19318** | recovery < SD |
| goal | 0.17351 | **0.19339** | recovery < SD |

**Both "substantial" recoveries are smaller than the across-seed standard deviation of A2's own
statistic**, on n=3. `RECOVERY_MARGIN = 0.15` was set from 922's A0-vs-A1 gap of ~0.35 -- i.e.
calibrated off the arm this run now shows to be the least functionally modulated of the three
(Section 3). The margin was never a noise-referenced bar and it does not clear one.

A2's per-seed harm values are 0.3824, 0.1771, **-0.0037**: one seed shows no effect and is
indistinguishable from A1. "Partial recovery" is one strong seed, one middling seed, and one
null.

### 2d. Is there a metric that actually shows recovery, and does it gate anything?

No. The only recovery quantity in the manifest is the `recovery` block above; it is not a
criterion, it is not a precondition, and it gates nothing. It selects a label string.

---

## 3. What the manifest's own unscored readouts show -- the finding this run really made

The driver recorded `w_harm_std` / `w_goal_std` / `final_terrain_loss` per cell. Nothing scores
them. They overturn the reading.

### 3a. Every arm's terrain_weight is functionally flat

MECH-152's claim text specifies the modulation depth directly: "hazard-gradient context ->
`w_harm > 0.8`, `w_goal < 0.5`; resource-proximate context -> `w_goal > 0.8`, `w_harm < 0.5`".
The driver's own training target implements exactly that -- `compute_terrain_loss` sets
`w_harm_target = 0.8 if hazard_max > 0.3 else 0.2` and `w_goal_target = 0.8 if hazard_max < 0.33
else 0.2`. **The asserted swing is 0.6.**

Observed standard deviation of `terrain_weight` over the collection series:

| arm | `w_harm_std` range | orders of magnitude below the asserted 0.6 swing |
|---|---|---|
| `A0_OFF` | 3.75e-07 .. 1.39e-06 | **~5.6 to 6.2** |
| `A1_PRODUCTION` | 1.94e-03 .. 7.08e-03 | ~1.9 to 2.5 |
| `A2_SOFTSEL` | 1.72e-04 .. 1.03e-02 | ~1.8 to 3.5 |

**No arm modulates terrain_weight within two orders of magnitude of what the claim asserts, and
the winning arm misses by six.** `A0_OFF`'s `r_w_harm = 0.356` is a Pearson correlation computed
over a signal that varies by roughly one part in a million on a sigmoid output bounded in
[0,1]. The correlation is arithmetically real and functionally meaningless: a terrain weight
that moves by 1e-6 scales nothing.

**Pearson r is scale-invariant. That is the whole defect.** It normalises out exactly the
quantity MECH-152 is a claim about. It therefore cannot distinguish "strong contextual precision
modulation" from "no modulation with a faintly hazard-correlated numerical residue" -- and in
this run it actively prefers the latter, ranking the arms in the exact inverse of their
modulation depth.

**The non-degeneracy guard cannot catch this by construction.** `terrain_weight_std_floor = 1e-9`.
`A0_OFF` clears that floor by ~375x while sitting ~1.6 million times below the claim's own
asserted swing. The guard is roughly six orders of magnitude too permissive to be a functional
non-degeneracy test, so the `a2_terrain_nondegenerate_premise` -- the second of the two
load-bearing criteria -- certifies almost nothing. `criteria_non_degenerate` reporting `true`
for all three entries is technically accurate and substantively empty.

### 3b. The terrain target was near-constant, so nothing was ever asked to modulate

`final_terrain_loss` is the mean over the collection series of
`((w_harm - w_harm_target)^2 + (w_goal - w_goal_target)^2) / 2`, with targets in {0.2, 0.8}.

Take a target that is 0.8 on a fraction `p` of steps and 0.2 otherwise, and an output that is
effectively constant (which the `w_*_std` figures above independently establish -- every cell is
constant to within 1e-2, most to within 1e-3). The best MSE any constant can achieve is the
target's own variance, `p(1-p) * 0.36`. Inverting the observed losses:

| cell | `final_terrain_loss` | implied bound on target switch rate `p` |
|---|---|---|
| A1 seed 42 | 1.03e-05 | **p <= 0.003%** |
| A2 seed 42 | 1.30e-05 | p <= 0.004% |
| A1 seed 44 | 7.55e-05 | p <= 0.02% |
| A2 seed 44 | 1.07e-04 | p <= 0.03% |
| A0 seed 44 | 7.10e-04 | p <= 0.20% |
| A0 seed 42 | 8.09e-04 | p <= 0.22% |
| A2 seed 43 | 4.30e-03 | p <= 1.2% |
| A1 seed 43 | 4.31e-03 | p <= 1.2% |
| A0 seed 43 | 7.21e-03 | **p <= 2.1%** |

**Across all nine cells, the terrain-precision target switched state on at most ~2% of
collection steps, and in the tightest cells on roughly 3 steps in 100,000.** The hazard field
varies (`hazard_std` 0.19-0.25) but essentially never crosses the 0.3 / 0.33 thresholds that
turn hazard variation into a *target* contrast. The terrain head therefore faced a near-constant
target, learned the constant (which is why the loss is tiny AND the output is flat -- those two
facts are the same fact), and had no gradient pressure to differentiate by context at any point.

The driver's docstring already flagged the neighbouring version of this problem -- it
"corrected" the inherited V3-EXQ-194 threshold of 0.1, which "nearly never fires at this env's
hazard-field floor of ~0.22". The correction moved the threshold to 0.3/0.33 but **did not make
the target bimodal**; it moved it from almost-never-firing to almost-always-firing. Either way
the target is constant and the contrast the claim is about never appears in the training or
collection distribution.

*Scope of this inference, stated honestly:* the bound is derived from the **collection**
series, which is exactly the series `r_w` is computed over, so the measurement conclusion is
direct. Extending it to the P0a/P1 **training** series is an inference -- same environment, same
thresholds, same `compute_terrain_loss` -- corroborated by the terminal near-zero `w_*_std`,
which is what a head trained on a constant target looks like. A redesign should measure the
training-side balance rather than inherit this inference.

**MECH-152 was never given the opportunity to express itself in this run, or in V3-EXQ-922,
which shares the machinery.**

---

## 4. Claim-layer mapping (Step 3)

**MECH-152** -- `mechanism_hypothesis`, `subject: e1_e3.cue_indexed_terrain_precision_modulation`,
status **provisional**, `epistemic_category: standard`, `implementation_phase: v3`,
`pending_retest_after_substrate: true`, `instantiates: SD-033c`,
`depends_on: [MECH-150, ARC-016, SD-010, ARC-035]`.

`claim_ids` accuracy: **correct and not inherited**. The queue entry justifies the single tag
explicitly, and the run directly exercises the terrain pathway. MECH-151 is recorded as
informative context only and is correctly not scored; ARC-041 is informed downstream and
correctly not tagged.

**Did the experiment test the claim under conditions where it could express itself? No.** The
claim asserts a 0.6-magnitude context-dependent swing in terrain_weight. The run (a) presented a
target contrast on <=2% of steps, and (b) scored the result with a scale-invariant statistic that
discards magnitude. Both independently prevent the claim from expressing itself; together they
make the test uninformative in either direction.

### The point governance most needs: the instrument critique cuts BOTH ways

This is the "illusory conflict resolution" check the skill requires, run explicitly.

MECH-152's entire evidence base is measured with the same scale-invariant Pearson-r DV:

| run | reading | DV | status of that DV |
|---|---|---|---|
| EXQ-194 | MIXED -- C1 PASS `r_w_harm = 0.70`, C2 FAIL `r_w_goal = -0.007` | Pearson r, target threshold 0.1 | driver's own docstring: threshold "nearly never fires" -- broken |
| EXQ-194a | PASS (phased training) | Pearson r | same family |
| V3-EXQ-922 | `does_not_support`, 0/3 both criteria | Pearson r, thresholds 0.5 / -0.3 | same family |
| **V3-EXQ-922a** | this run | same | **shown here to rank arms inversely to modulation depth** |

So the r_w_harm = 0.70 that promoted MECH-152 to provisional is **not more trustworthy** than the
0.0013 that now threatens to demote it. Both are correlations over a terrain_weight whose
functional amplitude was never checked, under a target contrast whose frequency was never
checked. The supporting evidence is single-pathway (one experiment family, one DV) and shares
the defect exactly.

**Consequence: this autopsy must not be read as rescuing MECH-152.** It does not. It says the
claim has never been tested at the magnitude it asserts -- in either direction -- and it explains
why nobody noticed.

**And the claim's own `what_would_answer` already names a decisive test that has never been
run.** Per the 2026-04-02 Kanashiro gain-control linkage recorded on the claim: "if terrain_weight
is genuine PRECISION gain (not just magnitude scaling), high w_harm should measurably REDUCE
harm-evaluation variability, not merely scale its mean -- the discriminator between
MECH-152-as-precision-gain and MECH-152-as-simple-magnitude-scaling, and also for whether MECH-152
and ARC-016 (temporal gain) are the SAME mechanism at different levels of description (both
subsumed by ARC-044)." **No experiment in the 194 / 194a / 922 / 922a family measures
harm-evaluation variability at all.** The claim carries a written decisive test that the entire
experimental lineage has bypassed.

---

## 5. Biological-reference triage (Step 4)

- **Closest reference mechanism:** vmPFC / OFC contextual precision scaling of harm-benefit
  evaluation. The claim's own notes cite Bechara et al. 1994 -- vmPFC lesion produces flat
  `w_harm = w_goal` regardless of sensory context, the Iowa Gambling Task deficit being
  specifically a *contextual precision scaling* failure rather than an absence of harm
  knowledge -- and Kanashiro et al. 2017 on gain modulation controlling signal-to-noise ratio,
  not only magnitude.
- **Faithful translation, NOT a formal-definition import.** `is_formal_import: false`. This is
  not a Pearl/Shannon/optimal-control import dressed as a mechanism; it is a direct translation
  of a documented neural gain-control pathway. The SD-003 failure mode does not apply.
- **Literature status: PRESENT.** `evidence/literature/targeted_review_sd_016/` (Bechara 1999
  anticipatory vmF; Lichtenberg 2017 BLA-OFC cue-expectation), `targeted_review_arc_041/`
  (vmPFC cognitive-map value 2025; OFC/vmPFC representational spaces 2024),
  `targeted_review_striatal_gain_control_bounding/`. **No `/lit-pull` commission is owed.**
- **Dependencies of the reference mechanism:** an amygdala-mediated cue-outcome association; a
  cue-indexed context representation (MECH-150 / SD-016 ContextMemory); an interoceptive /
  somatic-marker value signal; and -- the one that bites here -- **an experiential regime that
  actually presents both context types.**
- **Does the failure match a missing-dependency signature? Yes, precisely.** A vmPFC gain
  mechanism in an organism that encountered essentially one terrain context would present
  exactly as observed: a weight settled at the modal context's value, flat, with intact
  machinery. The Iowa Gambling Task is only diagnostic because the subject meets both
  advantageous and disadvantageous decks. Section 3b shows this run presented one deck ~98-100%
  of the time. **The FAIL is a discovered prerequisite -- contrastive terrain-context exposure at
  the operating threshold -- not a falsification.**

---

## 6. Four-layer diagnosis (Step 5)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear -- untested** | The claim asserts a 0.6-magnitude contextual swing; the run presented the contrast on <=2% of steps and scored with a scale-invariant DV. Neither supported nor weakened. |
| Biological reference | **clear** | vmPFC/OFC contextual precision scaling; faithful translation, not a formal import; lit present; failure matches the missing-experiential-contrast dependency signature. |
| Developmental / dependency prerequisites | **missing** | The reference mechanism's experiential prerequisite (both terrain contexts encountered) is absent from the collection/training distribution. MECH-150 / SD-016 retrieval selectivity is itself only 11.4% off the uniform saddle in A2. |
| Implementation completeness | **partial** | The pathway is wired end-to-end and produces a live output (`extract_cue_context` -> `terrain_weight`, trained through `compute_terrain_loss`), but it was never exercised under contrasting targets, so functional role is unestablished. Symbol present; role untested. |
| Environment adequacy | **wrong pressures** | `hazard_std` 0.19-0.25 is real variation, but it essentially never crosses the 0.3/0.33 target thresholds. The environment supplies hazard variance without supplying terrain-*target* contrast -- exactly the pressure the mechanism handles. |
| Measurement adequacy | **misleading** | Pearson r is scale-invariant and therefore blind to the modulation depth that IS the claim; it ranks the three arms in inverse order of their actual modulation. The non-degeneracy floor (1e-9) is ~6 orders too permissive. The claim's own stated discriminator (variance reduction / precision gain) is not measured at all. |
| Integration adequacy | **partially coupled** | The 1-knob A1->A2 selection swap does move the DV, so E1 retrieval and the terrain head are genuinely coupled; but the coupling's sign relative to selectivity is inverted across the full three-arm ladder, which no reading currently explains. |
| Scale / capacity | **unknown** | Not addressable: with a near-constant target, capacity was never taxed. |

### Failure-location summary (GOV-FAILLOC-1)

Reading the buckets as the skill defines them -- a bucket is `established` when its underlying
row reads adequate/complete, i.e. when that component is sound enough that the failure could
fairly be charged to it:

| bucket | reads from | this run |
|---|---|---|
| MECHANISM FAILED | Implementation completeness = **partial** | **partial** -- cannot be charged |
| MEASURES FAILED | Measurement adequacy = **misleading** | **not_established** -- the measures are the failing component |
| ENVIRONMENT FAILED | Environment adequacy = **wrong pressures** | **not_established** -- the environment is a failing component |
| REE FAILED | all three | **false** |

**Net classification: MIXED -- MEASUREMENT + ENVIRONMENT dominant. NOT chargeable to REE, and
NOT chargeable to MECH-152.** Two of the three gating components are independently inadequate
and the third is only partial, so REE FAILED is not reachable and neither is a single-bucket
MECHANISM read. Nothing in this run licenses the statement that REE failed to implement
contextual precision modulation; what it licenses is the statement that the test could not have
detected it if REE had.

**Recording-debt vs measurement-debt:** this is **measurement-debt (plus environment-debt), not
recording-debt.** Every readout needed to reach this diagnosis was recorded. The metric was
wrong, not absent -- so the repair is a redesigned DV and a fixed target distribution, and a
same-question re-run that merely records more would reproduce the same blind spot.

---

## 7. Learning extracted and repair pathway (Step 7)

**Node classification: `complex (probe-gated) / mystery (known data)`.** We already have the
data that settles what went wrong -- `w_*_std` and `final_terrain_loss` are in the manifest and
they are unambiguous. The frame (Pearson r over a near-constant target) is what is wrong. More
runs of the same design settle nothing. The repair is a **re-operationalisation of the DV plus a
fix to the target distribution**, which is one well-posed redesign, not a discrimination among
rival hypotheses -- so **no `fanout_recommendation` is emitted** (a single unambiguous
redesign is the GOV-FANOUT-1 exemption).

**Routing: `/queue-experiment`, NEW EXQ NUMBER (not a `922b` letter).** The scientific question
changes -- from "does terrain_weight *correlate* with hazard" to "does terrain_weight *modulate*
at the claimed depth, and is the modulation precision gain or magnitude scaling". A new letter
would signal a same-question implementation fix, which this is not.

### Redesign spec (draft -- for the confirming session / `/queue-experiment`)

1. **Fix the target contrast first, and gate on it.** Add a `terrain_target_balance` load-bearing
   precondition requiring both target states on >= 25% of steps each, in the training AND the
   collection series. Prefer deriving the 0.3 / 0.33 thresholds from the run's own hazard
   distribution (e.g. a median split) over the absolute constants inherited from 194/194a --
   Section 3b shows the inherited constants have now been on the wrong side twice, in opposite
   directions (0.1 nearly never fired; 0.3/0.33 nearly always fires).
2. **Score modulation DEPTH as the primary DV.** Use the between-context difference in mean
   terrain_weight -- `E[w_harm | hazard-gradient] - E[w_harm | resource-proximate]` -- with the
   claim's own band as the bar (`w_harm > 0.8` in hazard context, `< 0.5` in resource context).
   Demote Pearson r to a descriptive secondary readout. A scale-invariant statistic can never
   adjudicate a magnitude claim.
3. **Raise the non-degeneracy floor to something functional.** `terrain_weight_std > 1e-9` is not
   a guard. Tie it to the asserted swing -- e.g. `>= 0.05`, one-tenth of the 0.6 band.
4. **Add the precision-gain discriminator the claim's own `what_would_answer` names and no run
   has ever executed:** does high `w_harm` measurably REDUCE harm-evaluation variability, or only
   scale its mean? This is the MECH-152-vs-ARC-016 discriminator (both subsumed by ARC-044) and
   is arguably higher-value than re-testing the correlation.
5. **Keep A0_OFF and SCORE it.** In 922a the control outperformed both experimental arms on the
   scored DV and was structurally excluded from the label logic. Any successor must score the
   control on the mechanism criteria and must carry a verdict branch for "control outperforms the
   experimental arms" -- currently a shape the pre-registered branch set cannot express.
6. **Keep recording `w_harm_std` / `w_goal_std` / `final_terrain_loss` / `hazard_std`.** This run's
   optional-field discipline is the reason this diagnosis exists; it should be the family default.

### Transferable learning

- **A scale-invariant DV cannot adjudicate a magnitude claim.** Pearson r discards exactly what
  MECH-152 asserts. Whenever a claim states a target band (here `w_harm > 0.8`, `w_goal < 0.5`),
  the primary criterion must be stated on that band, not on a correlation with it.
- **A non-degeneracy floor is only a guard if it is referenced to the claim's own asserted
  magnitude.** A 1e-9 floor on a [0,1] sigmoid output passed a signal ~1.6 million times below
  the claimed swing while reporting `criteria_non_degenerate: true`. Floors set to catch
  arithmetic degeneracy (`pearson_r() = 0` artifacts) do not catch functional degeneracy, and the
  manifest field name does not distinguish them.
- **Verdict-label branch sets must include the control arm.** Declaring a control "context, not
  adjudication-gating" is defensible for *vacating* a contrast, but it also means no branch can
  fire when the control inverts the reading. 922a's five branches cover A2-vs-A1 exhaustively and
  the control not at all -- so the one outcome that actually occurred is unrepresentable.
- **A load-bearing premise cleared by a majority-order statistic should report its scatter.** The
  reported `measured` was the median; the mean, the SD, and the fact that 1 of 3 seeds violated
  the bound were all recoverable but none surfaced at the precondition. A load-bearing
  precondition whose margin is 0.39 SD is not distinguishable in the manifest from one whose
  margin is 5 SD.
- **A "recovery margin" calibrated from a prior run's arm gap inherits that arm's validity.**
  `RECOVERY_MARGIN = 0.15` was grounded in 922's ~0.35 A0-vs-A1 gap -- an arm now shown to be the
  least functionally modulated of the three. Recovery margins should be referenced to the current
  run's own across-seed scatter, which here would have refused the label (0.184 < 0.193).
- **A "diagnostic PASS = the probe ran" convention needs the label to be trustworthy.** The
  convention is honest and worth keeping, but it moves the entire epistemic load onto
  `interpretation.label`. When the label's decision rule omits an arm that inverts it, the PASS
  becomes a certificate of readiness attached to an unsound verdict -- and nothing in the
  indexer's flag vocabulary catches that.

### Re-derive brake (MOVE-3)

**Count for MECH-152 under R1-R3: 0. The brake does NOT fire.** Only one confirmed autopsy
target names MECH-152 (`failure_autopsy_V3-EXQ-922_2026-08-13`, run
`v3_exq_922_..._20260812T035119Z_v3`) and its `recommended_epistemic_category` is `standard`,
not `substrate_ceiling` -- so R3 excludes it. This autopsy is also not a `substrate_ceiling`
reading and does not add a hit. No re-queue refusal is owed; the redesign in this section is
permitted and is a *different* question with a *different* DV, which would be exempt in any case.

### Granularity-debt recurrence trigger: **DOES NOT FIRE**

`granularity_debt_cluster.py MECH-152` reports **1 target across 1 file**:

- `failure_autopsy_V3-EXQ-922_2026-08-13` [single], run
  `v3_exq_922_sd016_mech151_152_arc041_production_combo_20260812T035119Z_v3`,
  `claim_ids: [MECH-150, MECH-151, MECH-152, ARC-041]`, direction `mixed`, category `standard`.
- **Alignment distribution: `other` = 1** (free-text `claim_alignment`: "aligned -- the run's
  design maps 1:1 onto each claim's stated mechanism at each claim's own pre-registered
  granularity...").

The reader correctly declines to assert a clear on a free-text alignment, so I read the string:
it asserts alignment, **not** weakening. **No target reads `weakened`**, which per the skill's
own rule is decisive regardless of count -- a cluster with no `weakened` target is measurement or
implementation debt, not granularity debt. That is exactly what this autopsy concludes. This is
the second autopsy circling MECH-152, but the second signature is *instrument inadequacy*, which
is measurement debt, and my own `claim_alignment` reads `unclear -- untested`, not `weakened`.
`/claim-synthesis` is **not** recommended.

---

## 8. The HELD MECH-152 demotion -- the decisive read

**Context.** The 2026-08-16 `/governance` cycle HELD the automated `demote_to_candidate`
recommendation (conflict_ratio 0.667, exp_conf 0.315), recording MECH-152 as `discussing`, on
the explicit grounds that "MECH-152's owed ablation 922a has run but is unscored and
unadjudicated". **This autopsy is that owed adjudication.** The recorded hold said the condition
was "discharged in FACT but not yet in EVIDENCE". It is now discharged in evidence, and the
evidence does not point where either side of the hold expected.

**Decisive recommendation: DO NOT APPLY THE DEMOTION. MECH-152 stays `provisional`.**

**But the reason matters more than the outcome, and it is not the reason the hold anticipated.**

1. **922a does NOT rescue MECH-152.** The `selection_hardness_partial_recovery` label -- which on
   its face is the A0_OFF-closer-to-threshold reading the 922 autopsy identified as the live lead
   -- does not survive inspection. The recovery is below the across-seed SD of A2's own statistic
   (0.184 vs 0.193 harm; 0.174 vs 0.193 goal); it reaches 37% / 60% of the 194a bar; it is a
   *regression* against this run's own control; and it occurs at a modulation depth 2-3 orders of
   magnitude below what the claim asserts. **Governance must not read this PASS as support.**
2. **922a does NOT strengthen the falsification either.** It is non-contributory to the mechanism
   question in both directions.
3. **What 922a actually establishes is that the instrument behind the demotion cannot address the
   claim.** The conflict_ratio 0.667 is computed over exactly one experimental entry --
   V3-EXQ-922 -- which used the same Pearson-r DV, the same terrain machinery, and the same
   near-constant target distribution. In 922a that DV ranks the *cue-indexing-OFF* control
   highest and the *fully-selective* production arm lowest, which is incompatible with it
   measuring a cue-indexed pathway at all. Demoting on 922 would apply a conflict ratio computed
   from a single run whose instrument this successor has just shown to be non-diagnostic.
4. **The same critique disqualifies the supporting evidence.** EXQ-194's `r_w_harm = 0.70` -- the
   basis on which MECH-152 was promoted to provisional -- is the same statistic from the same
   family, measured with a target threshold (0.1) the driver's own docstring calls broken.
   **This autopsy is not a defence of MECH-152.** The honest position is that MECH-152's evidence
   base, supports and weakens alike, rests on a DV that cannot address its central assertion.
5. **Therefore: neither demote nor promote. Re-measure.** The claim is not "provisional pending
   more of the same"; it is "provisional pending its first valid measurement". Say so in the
   `evidence_quality_note` so the next automated cycle does not re-propose the same demotion on
   the same single entry a fourth time.

**Keep `pending_retest_after_substrate: true`, but re-scope it in the note.** The flag is kept
deliberately, per the skill's illusory-conflict-resolution rule: a `non_contributory`
recommendation must be paired with a pending retest, and the remaining "supports" have been
explicitly checked and found narrow and single-pathway (Section 4). What is owed, however, is a
**measurement redesign**, not a substrate build -- SD-016's substrate is not the blocker here and
no substrate work is recommended (Section 7, `recommended_substrate_queue_entry.action: "none"`).
The confirming session may prefer to clear the flag and carry the retest obligation in the note
instead; that is a judgment call for the Step 8 gate and is flagged there rather than decided
here.

**ARC-041's HELD dual-pathway disposition** is informed but not resolved by this run. MECH-151
`action_bias_div` was recorded as informative context only (A0 0.0306, A1 0.0509, A2 0.0556) and
is not scored. Nothing here licenses moving ARC-041.

---

## 9. Draft `evidence_quality_note` for governance (exact text -- NOT written by this skill)

> [2026-08-16 /failure-autopsy, V3-EXQ-922a, awaiting confirmation]: non_contributory. The owed
> soft-selection ablation ran and its self-routed `selection_hardness_partial_recovery` does NOT
> survive adjudication. A2_SOFTSEL fails both 194a criteria (C1 0/3, C2 1/3); the A2-vs-A1
> "recovery" (harm +0.184, goal +0.174) is smaller than A2's own across-seed SD (0.193 / 0.193)
> on n=3 and reaches only 37% / 60% of the bar. Decisively, the run's tagger-OFF control
> A0_OFF -- with no cue-indexing and sel_context_divergence 0.000117 -- scores HIGHEST
> (r_w_harm 0.356, r_w_goal -0.355, clearing C2 on 2/3 seeds), so the DV is monotonically
> DECREASING in cue-indexed retrieval selectivity across all three arms, which is incompatible
> with it measuring a cue-indexed pathway. Cause, from the manifest's own unscored readouts:
> terrain_weight std is 3.8e-7 to 1.0e-2 against the claim's asserted 0.6 swing (2 to 6 orders
> of magnitude low), the non-degeneracy floor is 1e-9 and therefore ~6 orders too permissive to
> catch it, and final_terrain_loss (1.0e-5 to 7.2e-3 against targets in {0.2,0.8}) bounds the
> terrain-target switch rate at <=2% of collection steps -- the terrain head faced a near-constant
> target and had no pressure to modulate. Pearson r is scale-invariant and cannot adjudicate a
> magnitude claim. THIS CUTS BOTH WAYS: EXQ-194's r_w_harm=0.70 (the promotion basis) and
> V3-EXQ-922's does_not_support come from the same DV and the same machinery, so the single
> conflicting entry driving conflict_ratio 0.667 is not diagnostic either. The 2026-08-16 HELD
> demotion should NOT be applied -- not because 922a rescues MECH-152 (it does not), but because
> MECH-152 has never been tested at the magnitude it asserts, in either direction. Route:
> /queue-experiment, NEW EXQ number -- score modulation DEPTH (between-context mean difference
> against the claim's own w_harm>0.8 / w_goal<0.5 band), gate on a terrain_target_balance
> precondition (both target states >=25% of steps), raise the non-degeneracy floor to ~0.05, score
> the OFF control on the mechanism criteria, and add the precision-gain-vs-magnitude-scaling
> discriminator this claim's own what_would_answer has named since 2026-04-02 and which no run in
> the 194/194a/922/922a family has ever measured. pending_retest_after_substrate retained but
> re-scoped: what is owed is a measurement redesign, not a substrate build. epistemic_category
> standard. PROMOTES NOTHING and DEMOTES NOTHING.

---

## 10. Hypothesis-space ledger (Step 9b) -- DRAFTED ONLY

Per staging mode, `hypothesis_space_registry.v1.json` was **not** written. The intended append
is carried in the companion JSON under `hypothesis_space_ledger_pending`: a NEW question
`mech152_terrain_modulation_depth` (Mode B new-question shortcut -- registered and partly
resolved in one edit, `pre_registered_utc` = `resolved_utc` = the run's own completion date
2026-08-14, never later than the run it adjudicates) with 4 hypotheses,
`initial_frozen_count: 4`. No growth-restriction check is owed: a question being registered in
this edit cannot carry a restriction, and no leg attaches to an existing question.

Two legs resolve `confirmed` (the measurement and the environment findings, both established by
the run's own data), two remain `alive` (selection-hardness suppression; mechanism absence at
the claimed depth) -- neither meets the elimination bar, which is the correct and honest outcome
for a run that could not address the mechanism question. All four `axis` labels
(`selection`, `intrinsic-architecture`, `measurement`, `environment`) already exist in the
registry's `axis_families.map`, so no taxonomy row needs adding.

The confirming interactive session (or the next `/governance` walk) applies it.

---

## 11. What the confirming human must decide (the skipped Step 8 gate)

1. **Ratify or reject the decisive read on the HELD demotion** (Section 8): do not demote, on
   instrument-inadequacy grounds rather than claim-strength grounds -- and confirm the framing
   that this is NOT a defence of MECH-152.
2. **Decide `pending_retest_after_substrate`**: retained `true` here on the skill's
   illusory-conflict-resolution rule, but the retest owed is a measurement redesign, not a
   substrate build. Clearing it and carrying the obligation in the note is a legitimate
   alternative.
3. **Confirm the redesign is a NEW EXQ number, not a `922b` letter** (the question changes).
4. **Confirm the scope of the instrument critique.** It bears on V3-EXQ-922 and EXQ-194/194a,
   which this autopsy does not formally re-adjudicate. Governance may wish to note the bearing
   on 922's `does_not_support` without reopening it, or to commission a re-adjudication.
5. **Optional cross-finding** (Section 2a): the `sd016_retrieval_selectivity_mechanism` ledger
   question carries `H1-drive-context-divergence` as `confirmed`; 922a's A2 clears its own
   selectivity bar by 0.39 SD with 1/3 seeds violating, at 11.4% off the uniform saddle. Worth a
   look, not a reversal.
