# Failure autopsy -- V3-EXQ-689d (MECH-448 F->eligibility demotion falsifier)

**Generated** 2026-07-20T06:04Z - **Session** `youthful-moser-3b6f74`
**Target** `v3_exq_689d_mech448_f_eligibility_demotion_falsifier_20260621T063408Z_v3`
**Landed outcome** PASS / `evidence_direction: supports` / `claim_ids: [MECH-448]`
**Status** confirmed (user-ratified at the Step 8 gate, 2026-07-20)

**Commissioned by** [`hold_weighted_e3_readout_corpus_sweep_2026-07-20.md`](hold_weighted_e3_readout_corpus_sweep_2026-07-20.md)
sec 5 item 2 (REE_assembly `4ceb7d22f9`), itself commissioned by
[`failure_autopsy_V3-EXQ-699_2026-07-20.md`](failure_autopsy_V3-EXQ-699_2026-07-20.md) sec 11.1.

> **One line.** The corpus sweep's two defects are confirmed at code and data level, and a
> **third, independent defect** -- the substrate changed MID-RUN, splitting exactly along the
> surviving seeds -- means `C_PRIMARY` has **zero validly-controlled seeds**. MECH-448's conversion
> finding is withdrawn (`non_contributory` / `measurement_test_design_defect`) and the claim reverts
> `provisional -> candidate`. The substrate itself is demonstrably built and doing real work.
> **No manifest was edited.**

---

## 1. Facts reconstruction

### 1a. What the run claimed

Four arms x three seeds (42/43/44), `MIN_SEEDS_FOR_PASS = 2`. The self-route label
`demotion_converts_committed_diversity` requires four criteria, of which exactly one is
finding-bearing:

| criterion | result | finding-bearing? |
|---|---|---|
| `C_READINESS` (route-range, e2-divergence, envelope-excludes) | 3/3 seeds | no -- readiness |
| `C_RANK_PRESERVING` (eligible set is an F-rank prefix) | frac exactly 1.0, 3/3 | no -- structural |
| **`C_PRIMARY`** (committed entropy strict-above BOTH collapsed controls) | **2/3 seeds** | **YES** |
| `C_SAFETY` (ON harm <= OFF + tol) | 2/3 seeds | no -- safety guard |

### 1b. Per-seed C_PRIMARY, the whole finding

| seed | ARM_ON `selE` | ARM_PROPOSER_CTRL | ARM_MATCHED_NOISE | verdict | margin |
|---|---|---|---|---|---|
| 42 | 1.1849 | 1.2760 | 1.2760 | **FAILS** | -0.0911 |
| 43 | 0.6930 | 0.0047 | 0.0047 | passes | +0.6883 |
| 44 | 0.9374 | 0.7505 | 0.7505 | passes | +0.1869 |

Killing either survivor flips the run to FAIL.

---

## 2. Defect 1 -- hold-weighted DV (CONFIRMED)

`experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py:598` accumulates
`selected_class_counts[int(action[0].argmax())] += 1` per env step from the `select_action` return
value; `:535` accumulates `pool_class_counts` from the e3_tick-gated candidate list.
`ree_core/agent.py:5430` returns the HELD action on `not ticks["e3_tick"]` before `e3.select()` is
reached, and `generate_trajectories` (`agent.py:4812`) returns CACHED candidates on the same
condition. Both histograms are therefore weighted by **hold duration** (cadence default 10, varying
5-20 under MECH-093).

`e3_hold_weighted_readout_lint` fires on this script naming exactly lines **535, 598**. (It also
carries defect form 1 -- a stale-diagnostics read at `:551` -- plus precondition-directionality
warnings.)

The primary DV `selected_action_class_entropy` (`:650`) is a class-histogram entropy: a
**distribution-shape statistic**, which the sweep's triage table classes **DISQUALIFYING** --
replication reweights the distribution that the statistic measures.

**The 663 calibration does not rescue it.** That replay bounded the cost at <1% and sign-varying,
but explicitly only where arm symmetry cancels the defect AND the DV is a continuous magnitude.
Neither holds: the DV is an entropy, and arm exposure is grossly asymmetric --

| seed | CTRL `n_p1_ticks` | OFF | ON | max spread |
|---|---|---|---|---|
| 42 | 387 | 2715 | 510 | **7.0x** |
| 43 | 3616 | 3629 | 3574 | 1.02x |
| 44 | 224 | 156 | 238 | 1.53x |

**Effective N is an order of magnitude below the histogram counts.** At cadence ~10, ARM_ON seed 44's
238 env steps are approximately **24 genuine selections**; seed 42's 510 are approximately 51. An
entropy estimated over ~24 independent draws across 5 classes is not a stable statistic at the
0.187-nat resolution the finding turns on.

---

## 3. Defect 2 -- vacuous matched-noise control (CONFIRMED, and worse than reported)

`ARM_PROPOSER_CTRL` (temp 1.0) and `ARM_MATCHED_NOISE` (`MATCHED_ENTROPY_TEMPERATURE = 2.5`, `:226`)
are identical **on every recorded metric on all three seeds** -- not only `selected_class_counts`,
but `selected_action_class_entropy`, `proposer_pool_class_entropy`, and `n_p1_ticks`
(387 / 3616 / 224 exactly). Identical tick counts mean identical trajectories: the two arms did not
merely converge, **they are the same arm**.

`temperature` IS declared per-arm (`:219`, `:226`), IS folded into `arm_fingerprint` (the two arms
hash differently), and IS passed to the selection call at `:546`. It has no behavioural effect
because the `candidate_summary_source="proposer"` path resolves by deterministic argmin -- there is
no sampling step for a temperature to widen. The "matched-entropy flat-hot sampling-noise control"
is therefore **unmeetable by construction** in the regime it was instantiated in.

The run's own pre-registered guard caught it -- `matched_noise_verified_lifting: false`,
`matched_noise_lift_seeds_over_proposer: 0` -- and the manifest note states plainly that this
"makes the C_PRIMARY noise comparison vacuous". **The run PASSED anyway**, because the criterion
`strict above BOTH` degrades silently to `strict above ONE` when the two bars carry the same number.
The guard was informational, not gating.

Consequence: the "NOT noise-as-diversity" half of `C_PRIMARY` -- one of its two load-bearing halves
-- **never tested anything**. This is the 699 sec 11.6 signature: two nominally independent readouts
agreeing exactly is a defect tell, not a validation. It is independent of hold-weighting and
**survives a DV repair**.

---

## 4. Defect 3 -- NEW: the substrate changed MID-RUN, splitting along the finding

Not previously reported -- neither the corpus sweep nor the 699 autopsy caught it. It is visible
**only** because `arm_fingerprint` carries a per-cell `substrate_hash`.

| arm | seed | `substrate_hash` | C_PRIMARY |
|---|---|---|---|
| ARM_PROPOSER_CTRL | 42 / 43 / 44 | `19b4073c41b9...` | -- |
| ARM_MATCHED_NOISE | 42 / 43 / 44 | `19b4073c41b9...` | -- |
| ARM_OFF | 42 / 43 / 44 | `19b4073c41b9...` | -- |
| ARM_ON | 42 | `19b4073c41b9...` | **FAILS** |
| **ARM_ON** | **43** | **`fc6d17ce5fa3...`** | passes |
| **ARM_ON** | **44** | **`fc6d17ce5fa3...`** | passes |

Ten of twelve cells ran on `19b4073c`; ARM_ON seeds 43 and 44 ran on `fc6d17ce`. Arms execute in
declaration order, so the substrate changed **between ARM_ON seed 42 and ARM_ON seed 43** -- i.e.
`ree_core` was edited on `DLAPTOP-4.local` while the run was in flight on 2026-06-21.

**The split maps onto the finding exactly:**

- The **only** seed whose treatment arm shares a substrate with its own controls -- seed 42 -- is
  the seed that **FAILS** C_PRIMARY.
- **Both** surviving seeds compare a treatment arm on `fc6d17ce` against controls on `19b4073c`.

So for seeds 43 and 44 the within-seed ON-vs-CTRL contrast is **not a controlled comparison**: the
demotion toggle is confounded with a substrate change of unknown content. This is a confound, not
contamination-scale noise, and no margin arithmetic bounds it.

**`C_PRIMARY` therefore has zero validly-controlled surviving seeds.** That single fact is
sufficient to withdraw the finding independently of defects 1 and 2, and it too survives a DV
repair.

**Recording note.** A top-level-only `substrate_hash` -- the always-core field this manifest is in
fact MISSING -- would have recorded one hash for the run and hidden this entirely. The per-arm
fingerprint is what made it detectable. This is an argument for per-cell substrate stamping as the
primitive, not merely a per-run one.

---

## 5. What SURVIVES -- adjudicated separately

Per the 699 precedent that a defective instrument can leave the readiness correct while destroying
the finding:

| criterion | why it survives |
|---|---|
| `C_READINESS` | `EXCLUDED_COUNT_FLOOR = 0.0`, strict `>`. Threshold-invariant: replication cannot manufacture a positive from an all-zero record. 3/3 seeds; `demotion_active_frac` 1.0; `excluded_count_mean` 0.152. |
| `C_RANK_PRESERVING` | measured **exactly 1.0** -- a saturated fraction has nowhere to move under reweighting. |
| `C_SAFETY` | reads realized per-env-step harm from `env.step`. The env step **is** the correct sampling unit for a realized-harm rate, so hold-weighting is not a defect here but the intended denominator. |

**Reading: the MECH-448 substrate is built, active, non-degenerate, rank-preserving, and safe.**
The envelope really does exclude on a genuinely divergent pool, and really does preserve F-rank. The
demotion lever exists and does real work. What has no uncontaminated basis is the **conversion
finding** -- the claim that it lifts committed diversity -- which is the part that moved MECH-448
toward `supports`.

---

## 6. Recording-standard audit

Against `experimental_recording_standard_2026-07-12.md` sec 3b always-core:

| field | present |
|---|---|
| `recording_schema` | **MISSING** |
| top-level `substrate_hash` | **MISSING** (per-arm only, via `arm_fingerprint`) |
| `machine` | present (`DLAPTOP-4.local`) |
| `machine_class` | **MISSING** at top level (per-arm: `darwin-arm64-py3.13`) |
| `elapsed_seconds` | **MISSING** |
| `config` | present |
| `seeds` | present (in `config`) |

This is **recording-debt**, and it interacts with defect 3: the standard's per-run `substrate_hash`
would not have surfaced the mid-run split. The re-run spec below requires per-cell stamping and an
explicit invariance assertion.

---

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear -- untested** | The claim was never validly tested. Not weakened: the instrument failed before the claim was put at risk. |
| Biological reference | **clear** | Carandini & Heeger 2012 canonical divisive normalisation; Louie/Khaw/Glimcher 2013 value DN; Mink center-surround. `targeted_review_connectome_mech_439` exists (5 lit entries, `lit_conf` 0.849). No biology divergence implicated -- this is not a translation failure. |
| Prerequisites | **present** | MECH-439 / MECH-447 / ARC-107 / Q-078 available; readiness passed 3/3. |
| Implementation | **complete** | Envelope active on 1.0 of P1 ticks, excludes on a divergent pool, preserves rank exactly. The lever is built. |
| Environment | **adequate** | GAP-A foraging substrate produced a divergent pool (`cand_world_pairwise_dist` 0.154 vs 0.03 floor). |
| **Measurement** | **MISLEADING** | Hold-weighted shape statistic; a control that is bit-identical to its baseline; ~24-51 effective selections on the surviving seeds. |
| **Integration / run hygiene** | **BROKEN** | Substrate changed mid-run; treatment and control cells ran different builds. |
| Scale / capacity | **likely insufficient** | Effective N per surviving seed is ~24-51 genuine selections against a 0.187-nat margin. |

**Dominant layer: measurement + run hygiene.** Recommended `epistemic_category`:
`measurement_test_design_defect`.

---

## 8. Illusory-conflict check (MANDATORY)

Three runs tag MECH-448:

| run | outcome | per-claim direction | purpose | status after this autopsy |
|---|---|---|---|---|
| V3-EXQ-689d | PASS | `supports` | evidence | **WITHDRAWN here** |
| V3-EXQ-689h | PASS | `supports` | **diagnostic** | **SURVIVES** (verified immune) |
| V3-EXQ-699 | PASS | `non_contributory` | diagnostic | already withdrawn (699 autopsy) |

**689h verified structurally immune.** `v3_exq_689h_pcomp_demotion_x_gonogo_composition.py` has
**zero** occurrences of `agent.select_action`, `env.step`, or `clock.advance`. It drives the
selector directly on synthetic candidate banks (`N_BANKS = 80` decision contexts per seed-arm), one
fresh committed argmin per bank, no cadence and no env loop -- the same structural immunity that
protects 689g. The hold-weighted lint does **not** fire on it. Its `committed_class_entropy_nats` DV
is therefore replication-free.

**No conflict is unmasked.** MECH-448 has **zero `weakens` and zero FAIL runs** across its entire
evidence base (6 entries: 1 exp + 5 lit, all `supports`). Withdrawing 689d removes a support without
revealing any suppressed opposing evidence. The `confirmed_established` quadrant is not hiding a
conflict.

**But the remaining support IS narrow and single-pathway -- flag it explicitly:**

1. **`genuine_exp_count` drops 1 -> 0.** 689h is `purpose: diagnostic`, so the indexer never counted
   it as genuine experimental evidence. After withdrawal MECH-448 has **no genuine experimental
   entry at all**; `experimental_confidence` 0.712 becomes underdetermined rather than merely lower.
2. **689h tests a different proposition.** Its finding is `demotion_x_gonogo_additive` -- demotion as
   one factor in a 2x2 composition with Go/No-Go -- not the standalone conversion assertion MECH-448
   makes.
3. **Single pathway.** 689h shares the synthetic-bank selector-level pathway with 689g. After
   withdrawal, **nothing survives from the embodied env-loop pathway**. MECH-448's distinguishing
   assertion is that demotion lifts committed diversity *in an agent*; that has no uncontaminated
   test remaining.
4. **689h carries its own flags** -- anchor-reachability (`assert_anchor_reachable` absent on seven
   readiness anchors) and precondition-directionality. It is not a clean substitute and should not
   be cited as one.

Per the standing rule, `lit_conf` and `exp_conf` are reported separately and never blended:
MECH-448 after this autopsy is **strong-lit (0.849, 5 entries) / zero-genuine-exp**.

**Downstream check -- MECH-449 and ARC-107 are NOT damaged.** MECH-449's evidence is V3-EXQ-689g,
independently verified structurally immune by the corpus sweep (sec 4b), and its criteria are
threshold-invariant (`safety_violations == 0`). Two couplings need noting but neither is evidential:

- MECH-449 `depends_on` includes MECH-448. The dependency is architectural (both are ARC-107 legs),
  not evidential -- 689g does not rest on 689d.
- MECH-449's `evidence_quality_note` cites "the MECH-448 689d promotion precedent" as the rationale
  for its own `candidate -> provisional` promotion. That is **note hygiene, not an evidential
  dependency**: 689g independently cleared MECH-449's named validation gate (3/3 seeds convert,
  0 safety violations). Governance should nonetheless **rewrite that sentence** so a reader does not
  later infer that MECH-449's standing rests on a withdrawn finding.

---

## 9. Learning extracted

1. **A pre-registered guard that does not GATE is not a guard.** `matched_noise_verified_lifting`
   fired correctly, was recorded honestly, was described accurately in the manifest note -- and the
   run passed. A criterion of the form `strict above BOTH X and Y` degrades **silently** to
   `strict above X` when `X == Y`; nothing in the pass logic notices that the conjunction collapsed.
   Conjunctive criteria over multiple controls need an explicit **control-distinctness assertion**.
2. **A control must be reachable in the regime it is instantiated in.** `MATCHED_ENTROPY_TEMPERATURE`
   is inert under a deterministic-argmin proposer path. This is the `assert_anchor_reachable` failure
   mode (SD-068 cluster autopsy Learning 1) in a new location: a *negative control* that is unmeetable
   by construction, rather than a readiness anchor that is unreachable by construction.
3. **NEW DEFECT CLASS -- intra-run substrate divergence.** A run whose cells do not share one
   `substrate_hash` is not a controlled experiment, and nothing in the current pipeline checks this.
   It is invisible to a per-run `substrate_hash` (which the standard currently specifies), invisible
   to both E3 lints, and survives any DV repair. It is detectable **cheaply and retroactively** from
   the `arm_fingerprint` blocks already present on every multi-arm manifest.
4. **Per-cell recording caught what per-run recording would have hidden.** The arm-reuse
   fingerprint machinery was built for cache-matching, not provenance auditing -- but its per-cell
   `substrate_hash` is the only reason defect 3 is knowable. Provenance granularity should follow the
   *unit of comparison*, not the unit of execution.
5. **Effective N, not row count, is the sample size for a shape statistic.** 238 env steps at
   cadence 10 is ~24 genuine selections. Manifests should emit `n_fresh_select` / `n_latched` so
   the true denominator is auditable without reconstructing the cadence.
6. **A defective instrument can leave readiness correct while destroying the finding** -- the 699
   precedent, reconfirmed. Adjudicate criteria separately; do not let one verdict cover a run.

---

## 10. Routing

**Primary: `/queue-experiment` -- same-question instrument repair, alphabetic suffix (`V3-EXQ-689i`
or next free letter).** This is INSTRUMENT REPAIR of a run that never validly measured its primary
DV -- the sanctioned 785 -> 785a / 708 -> 708a shape -- not a re-test of the same claim against the
same ceiling.

The re-run MUST fix all three defects; fixing only the DV leaves defects 2 and 3 intact and would
reproduce a differently-broken PASS:

1. **Gate the DV on a fresh selection.** Accumulate `selected_class_counts` only on
   `ticks["e3_tick"]` (or clear-before-select and record only on repopulation). Emit
   `n_fresh_select`, `n_latched`, `fresh_select_yield`. Reference implementation:
   `experiments/v3_exq_785a_mech463_arousal_exogenous_urgency_decomp.py`. Apply identically to
   `pool_class_counts` at `:535`.
2. **Repair or replace the matched-noise control**, and make its distinctness **gating**. Either
   instantiate it on a path where temperature is live (a sampling selection step), or replace it with
   a control that is demonstrably distinct. Add a hard assertion that no two control arms produce
   identical class-count vectors, and make `matched_noise_verified_lifting` **block the PASS** rather
   than inform it.
3. **Assert substrate invariance across cells.** Stamp `substrate_hash` per cell (already available
   via `arm_fingerprint`) and **fail the run** if the set of hashes across all cells has cardinality
   > 1. Additionally freeze the working tree for the run's duration, or run on a cloud worker at a
   pinned commit rather than on the Mac against a live checkout.
4. **Power the entropy DV to its effective N.** Raise `p1_measurement_episodes` and/or seeds so each
   cell yields a stable class histogram over genuine selections; declare the target
   `n_fresh_select` up front. Note the raw exposure asymmetry (7x on seed 42) must also be addressed
   or explicitly modelled -- equal env steps do not imply equal selections.
5. **Stamp the always-core** via `experiments/_lib/manifest_core.stamp_recording_core(...)` --
   `recording_schema`, top-level `substrate_hash`, `machine_class`, `elapsed_seconds`.

**Re-derive brake: NOT FIRED.** By literal count this is the second `non_contributory` autopsy
tagging MECH-448 (699 was the first), which meets `RE_DERIVE_BRAKE_THRESHOLD = 2`. It is recorded as
not fired on the same grounds the 699 autopsy recorded, and the user ratified this at the Step 8
gate: the recommended category is `measurement_test_design_defect`, **not** `substrate_ceiling`; the
substrate is demonstrably built (readiness / rank-preservation / safety all survive on threshold
invariance); and the corrected re-run asks a genuinely different question -- "does the effect exist
when measured correctly" -- rather than re-posing the same question against the same ceiling. The
brake exists to stop lettered iterations circling a ceiling; refusing instrument repair on a claim
whose substrate is already proven built would invert its purpose.

**Secondary: corpus scan for intra-run substrate divergence (NEW, recommended -- not run here).**
Defect 3 is a new class with unknown corpus-wide exposure. The scan is cheap and retroactive: for
every manifest carrying `arm_results[].arm_fingerprint`, collect the set of `substrate_hash` values
and report every run with cardinality > 1. Any hit is a run whose arms are not mutually controlled,
independent of hold-weighting. Recommend this as a follow-on chip; deliberately NOT executed in this
session (scope discipline).

**No `/lit-pull` owed.** The biology is present and supporting (`targeted_review_connectome_mech_439`,
5 entries, `lit_conf` 0.849) and no biology divergence is implicated -- the failure is instrumental,
not a translation gap.

**No `/claim-synthesis` owed.** The granularity-debt recurrence trigger is checked and does **not**
fire in spirit: this is the second autopsy touching MECH-448, but 699 and 689d are two targets of
**one** measurement-defect discovery (the same corpus sweep), not two structurally different failure
signatures circling a coarse claim. Recorded as `fires: false` with that rationale so the standing
`check_granularity_debt_recurrence.py` scan can see the reasoning rather than a bare absence.

---

## 11. Draft `evidence_quality_note` for MECH-448 (governance to write -- NOT written here)

> **2026-07-20 (failure_autopsy_V3-EXQ-689d): the V3-EXQ-689d conversion finding is WITHDRAWN;
> status reverted provisional -> candidate.** The 2026-06-21 PASS that promoted this claim rested on
> `C_PRIMARY` (committed-action-class entropy strict-above both collapsed controls), which is invalid
> on three independent grounds. (1) HOLD-WEIGHTED DV: `selected_class_counts` is accumulated per env
> step from the `select_action` return value (script `:598`, and `:535` for the pool), but
> `agent.py:5430` returns the HELD action on `not ticks["e3_tick"]`, so the histogram is weighted by
> hold duration -- a distribution-shape statistic is DISQUALIFYING under the
> `hold_weighted_e3_readout_corpus_sweep_2026-07-20` triage, and the 663 <1% calibration does not
> apply (entropy DV; arm exposure differs up to 7-fold within seed 42). Effective N on the surviving
> seeds is ~24-51 genuine selections, against a weaker-survivor margin of 0.187 nats. (2) VACUOUS
> CONTROL: `ARM_MATCHED_NOISE` is bit-identical to `ARM_PROPOSER_CTRL` on every metric on all three
> seeds -- `temperature` is inert on the deterministic-argmin proposer path -- so the "not
> noise-as-diversity" half of `C_PRIMARY` never tested anything; the pre-registered guard
> `matched_noise_verified_lifting: false` fired without blocking the PASS. (3) INTRA-RUN SUBSTRATE
> DIVERGENCE (new): `ARM_ON` seeds 43 and 44 ran on `substrate_hash fc6d17ce...` while every control
> and `ARM_ON` seed 42 ran on `19b4073c...`. The two seeds carrying the finding are exactly the two
> whose treatment arm was not substrate-matched to its controls; the one properly-controlled seed
> (42) FAILS `C_PRIMARY` (1.1849 < 1.2760). `C_PRIMARY` therefore has ZERO validly-controlled seeds.
> **What SURVIVES:** `C_READINESS` (0.0 floor, strict `>`, 3/3), `C_RANK_PRESERVING` (exactly 1.0,
> saturated) and `C_SAFETY` (realized per-env-step harm from `env.step` -- correct sampling unit).
> The MECH-448 substrate is built, active, non-degenerate, rank-preserving and safe; it is the
> CONVERSION finding that has no uncontaminated basis. **Evidence base after withdrawal:**
> `genuine_exp_count` 1 -> 0. V3-EXQ-689h (PASS/supports) survives -- verified structurally immune
> (synthetic candidate banks, no env loop) -- but is `purpose: diagnostic`, tests
> `demotion_x_gonogo_additive` rather than the standalone conversion assertion, shares the
> synthetic-bank pathway with 689g, and carries its own anchor-reachability flag. **No `weakens` is
> unmasked (zero weakens, zero FAIL runs), but the remaining support is narrow and single-pathway:
> nothing survives from the embodied env-loop pathway.** Reported decoupled: strong-lit
> (`lit_conf` 0.849, 5 entries) / zero-genuine-exp. Retest pending the corrected re-run
> (`pending_retest_after_substrate: false` -- this is instrument repair, not a substrate gap).

**Also recommended for MECH-449 (note hygiene only, no status change):** rewrite the clause citing
"the MECH-448 689d promotion precedent" in its `evidence_quality_note`. MECH-449's standing rests
independently on V3-EXQ-689g, which is structurally immune; the sentence should not leave a reader
inferring that it rests on a withdrawn finding.

---

## 12. Scope note

Analysis and handoff only. **No manifest, `claims.yaml`, `review_tracker.json`, or
`substrate_queue.json` was edited.** The landed 689d manifest is untouched, per the corpus sweep's
standing rule that completed runs are re-adjudicated via `/failure-autopsy`, never rewritten.
`hypothesis_space_registry.v1.json` was **not** written: no registered question tags MECH-448,
MECH-449 or ARC-107, this autopsy emits no `fanout_recommendation`, and its non-discriminating
`non_contributory` verdict narrows no hypothesis (per the Step 9b mapping table, such a leg stays
`alive`). The adjacent `conversion_ceiling_root` leg `H-f-dominance` is noted as thematically
related -- MECH-448 is the F-demotion lever -- but it is registered against MECH-457 / ARC-065 with
`V3-EXQ-737` as its adjudicating run, and is untouched by this withdrawal.
