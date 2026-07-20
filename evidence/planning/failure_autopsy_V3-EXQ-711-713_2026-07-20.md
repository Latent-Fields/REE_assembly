# Failure autopsy — V3-EXQ-711 + V3-EXQ-713: PARTIAL withdrawal of conjoined interpretation labels

**Generated** 2026-07-20T06:09:33Z · **Session** `quirky-shaw-67e9b2` · **Scope** cluster (2 targets)
**Status** confirmed (user-adjudicated at the Step 8 gate, 2026-07-20)
**Origin** [`hold_weighted_e3_readout_corpus_sweep_2026-07-20.md`](hold_weighted_e3_readout_corpus_sweep_2026-07-20.md)
sec 4c (REE_assembly `4ceb7d22f9`), which named these two as "findings that are two claims joined at a seam".
**Prior autopsies (both `confirmed`, both superseded ONLY in part by this document):**
[`failure_autopsy_V3-EXQ-711_2026-07-04`](failure_autopsy_V3-EXQ-711_2026-07-04.md) ·
[`failure_autopsy_V3-EXQ-713_2026-07-05`](failure_autopsy_V3-EXQ-713_2026-07-05.md)

> **One line.** This is a **PARTIAL withdrawal, not a full one.** Each label is literally two
> conjoined claims and they split exactly along the 699/708 triage seam: the **arbitration-mechanics
> half SURVIVES** on threshold invariance, the **"does not convert the ceiling" half is WITHDRAWN**
> as resting on a hold-weighted distribution-shape statistic. **No `evidence_direction` changes** —
> both runs were already `non_contributory` on all three claims and carry zero scoring weight. What
> the withdrawal actually costs is the **713 route-exhaustion verdict**.

---

## 0. The two things this document does NOT do

Stated first because the natural misreading of a withdrawal is that something was demoted.

1. **It does not change any `evidence_direction`.** Both manifests were already governance-overridden
   to `non_contributory` on MECH-439 / ARC-108 / ARC-110 — 711 on 2026-07-04, 713 on 2026-07-05 —
   and `claim_evidence.v1.json` records all six entries as `scoring_excluded: "non_contributory"`
   (entries 4770-4772, 4789-4791; `scored: null`, `weight: null`). The self-routed
   `weakens ARC-108/ARC-110` survives only in `evidence_direction_original_self_route`. **There is no
   live directional weight to withdraw**, so the withdrawal cannot demote anything.
2. **It does not disturb the re-derive brake or the 713x refusal.** Both rest on
   `substrate_ceiling` / `non_contributory`, which this re-adjudication *strengthens*. See sec 6.

**No manifest was edited.** Completed runs are re-adjudicated, never rewritten.

---

## 1. The defect, verified in source (not trusted from the lint)

`ree_core/agent.py:5430` returns the **held** action on `not ticks["e3_tick"]`, before `e3.select()`
is reached. Both scripts accumulate a committed-class histogram per **env step**:

| | `select_action` call | `committed_class` derivation | accumulation |
|---|---|---|---|
| 711 | `experiments/v3_exq_711_ascending_spiral_gain_validation.py:836` | `:893` `int(action[0].argmax().item())` | `:910-914`, inside the `is_p2` block |
| 713 | `experiments/v3_exq_713_bounded_parity_controller_validation.py:869` | `:938` same | `:955-959`, inside the `is_p2` block |

So `committed_class_entropy_nats` is **hold-weighted**: cadence default 10
(`utils/config.py:2017`), varying 5-20 under MECH-093 arousal (`heartbeat/clock.py:52-70`). It is a
**distribution-shape statistic**, which per the sweep's triage table is **DISQUALIFYING** — replication
reweights the distribution itself, which is exactly what the statistic measures. No diagnostics latch
is touched, so `e3_diagnostics_staleness_lint` (form 1) is structurally blind to both.

The per-arm `committed_class_counts` in the manifests confirm the DV is literally that histogram
(e.g. 711 seed 42 OFF `{0:438, 1:293, 2:2, 3:1445, 4:3}` → 0.880290 nats).

---

## 2. The seam — what survives and what is withdrawn

### 2a. SURVIVES (threshold-invariant ⇒ SAFE)

| | criterion | site | measured vs threshold | why invariant |
|---|---|---|---|---|
| **711** | `limbic_loop_can_win` | `:1098` | **3.0 vs 3.0** at `LIMBIC_WIN_PASS_FRACTION = 0.75` | per-seed strict `clg_limbic_ge_motor_ticks > 0`; duplication cannot manufacture a positive from an all-zero record |
| **711** | `learned_cross_loop_weights_moved_off_init` | — | **4897.79931641 vs 1e-06** | weight-space magnitude, not a per-step readout |
| **713** | `limbic_loop_parity_win` | `:1155` | **4.0 vs 3.0** | `clg_limbic_parity_band_ticks > 0 and not saturated`; strict `>0` |
| **713** | `no_saturation_blowup` | — | **exactly 0.0 vs 0.0** | the strongest form of threshold invariance — an exact-zero reading |
| **713** | weights moved | — | **0.16938061 vs 1e-06** | as above |
| both | `frac_pre_ge2` | — | **exactly 1.0**, every seed, both arms | a ratio saturated at 1.0 has nowhere to move |

**Therefore these findings STAND, unqualified:**

- **711 — "ascending spiral gain LETS LIMBIC WIN."** The ascending gain does lift the limbic loop to
  ≥ motor effective column weight. (It stands alongside, not against, the 711 autopsy's separate
  finding that the win was a *saturated runaway* — that finding rested on `clg_m_range_peak` 4897.8
  and `w_eff` ratios, also SAFE.)
- **713 — "BOUNDED PARITY WIN."** The bounded target-parity controller delivers a **fair,
  non-saturated** limbic parity win on 4/4 divergent seeds. The 711 monopoly was genuinely repaired.
  The prior autopsy's learning "711 'missing controller' gap CLOSED" **survives intact**.

The substrate is demonstrably built and doing real work. That is not in question.

### 2b. WITHDRAWN (DISQUALIFYING)

The **"DOES NOT CONVERT the ceiling / ceiling-intrinsic / weakens ARC-108, ARC-110"** half of both
labels. Load-bearing `C1_learned_strict_above_static` is a **+0.05 nat margin** on the hold-weighted
`committed_class_entropy_nats`.

**711** — `C1_n_seeds = 1` of `C1_n_divergent = 3` (divergent = {42, 44, 46}, `gapa_divergence` true both arms):

| seed | OFF | ON | delta | vs +0.05 margin | arm exposure (`n_p2_ticks`) |
|---|---|---|---|---|---|
| 42 | 0.880290 | 1.033241 | +0.152951 | **clears +0.1030** | 2181 → 2051 (−6.0%) |
| 44 | 1.091586 | 1.042311 | −0.049275 | short **0.0993** | 1722 → 1179 (**−31.5%**) |
| 46 | 1.203696 | 0.993895 | −0.209801 | short **0.2598** | 2083 → 1936 (−7.1%) |

**713** — `C1_n_seeds = 0` of `C1_n_divergent = 4` (divergent = {42, 44, 46, 47}):

| seed | OFF | ON | delta | vs +0.05 margin | arm exposure |
|---|---|---|---|---|---|
| 42 | 0.880290 | 0.915550 | +0.035260 | short **0.0147** | 2181 → 2407 (+10.4%) |
| 44 | 1.091586 | 1.090475 | **−0.001111** | short **0.0511** | 1722 → 1698 (−1.4%) |
| 47 | 0.553877 | 0.535169 | −0.018708 | short **0.0687** | 5039 → 5237 (+3.9%) |
| 46 | 1.203696 | 1.128848 | −0.074848 | short **0.1248** | 2083 → 1597 (**−23.3%**) |

**713 is the most fragile C1 in its lineage.** Seed 44's raw delta of **−0.0011** is indistinguishable
from zero at any plausible noise scale; three of four seeds sit inside the 699 autopsy's
**demonstrated-reachable 0.115-0.134 nat flip band**, and seed 42 misses by 0.0147 — an order of
magnitude *inside* it.

**The 663 calibration does not rescue either run.** The matched replay measured
+0.01% / +0.64% / −0.87% (sub-1%, sign-varying), but that bounds the defect **only** where arm
symmetry cancels it *and* the DV is a continuous magnitude. Both exclusions bind here: the DV is an
entropy, and **the arms differ in hold duration**
(`failure_autopsy_V3-EXQ-699_2026-07-20.md` sec 4d). The measured per-seed exposure asymmetries above
are the direct evidence that arm symmetry does not hold.

> **Correction to the sweep's sec 4c figures.** The sweep reports 711 at "+65% exposure spread". The
> **+65.4%** reading is seed **45**, which is `gapa_divergence = False` on **both** arms and therefore
> **not in the C1 evaluation set**. The largest spread on a *divergent* seed is **−31.5%** (seed 44).
> Similarly 713's "+30%" measures **−23.3%** (seed 46), with the divergent range spanning
> +10.4% → −23.3% ≈ 33.7 pp. **The verdict is unchanged** — a 31.5% arm-exposure asymmetry is far
> outside the regime where the 663 calibration applies — but the record should carry the measured
> numbers.

---

## 3. Claim-layer mapping

| claim | type | what the SURVIVING half bears on | what the WITHDRAWN half bore on |
|---|---|---|---|
| **MECH-439** | MECH | nothing directly | the "ceiling-intrinsic" narrow corroboration — **withdrawn** |
| **ARC-108** | ARC | cross-loop learned reweighting is live and controllable (mechanism non-vacuity) | the `weakens` — already dead as live weight; now also **unwarranted in its reasoning** |
| **ARC-110** | ARC | loop segregation carries live cross-loop variance; limbic loop can reach parity | as ARC-108 |

The architectural commitments ARC-108 / ARC-110 are **untouched in both directions**. They were not
weakened before this document (the July overrides saw to that), and they are not strengthened by it.
What changes is that the *reasoning* behind the original self-route is now known to be
instrument-contaminated as well as substantively rejected — belt and braces on the same conclusion.

---

## 4. Four-layer diagnosis (applies to both targets)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** (was: weakened) | the conversion question was never validly measured; the claim could not express itself through a hold-weighted readout |
| Biological reference | partial | ascending-spiral limbic→motor gain (Haber 2000) is a faithful anatomical translation; the *readout*, not the mechanism, is the defect |
| Prerequisites | **present** | all readiness gates met and SAFE — divergent seeds, live cross-loop variance, named-channel routing, weights moved, parity/win gates |
| Implementation | **complete** | 713's bounded controller works as designed; `no_saturation_blowup` exactly 0.0 |
| Environment | adequate | single-arena limitation is a separate, already-recorded caveat |
| **Measurement** | **misleading** | **dominant layer.** Hold-weighted distribution-shape DV against a +0.05 nat margin under 23-31% arm-exposure asymmetry |
| Integration | coupled | arbitration and selection faces couple as designed |
| Scale / capacity | unknown | untestable while the readout is contaminated |

**Dominant diagnosis: measurement-debt, not recording-debt.** The readout was *computed wrong*, not
computed-and-discarded. A re-run must change the DV (accumulate on E3 ticks only, or read a
fresh-selection latch), not merely record more fields. `recommended_epistemic_category` stays
**`substrate_ceiling`** for both — unchanged from the July autopsies, and now doubly grounded.

---

## 5. Cluster pattern — the compounding redirect

The July 2026 adjudication chain redirected the conversion route **away from** arbitration-reweighting
**toward** the MECH-448 selection/eligibility face (713 autopsy `learning_extracted`:
"committed-action conversion is a selection/eligibility-face op (MECH-448, lifting on GAP-A), not
arbitration reweighting"). That redirect is now **unsupported at both ends**:

| end of the redirect | status after the sweep |
|---|---|
| **FROM** — arbitration-reweighting "exhausted" (709/711/713) | **withdrawn here**: the terminal leg's C1 is disqualified |
| **TO** — MECH-448 selection face (689d) | **compromised** per sweep sec 4b: `C_PRIMARY` is a class-histogram entropy passing on exactly 2/3 seeds, weaker margin 0.187 nats, arms differing **7-fold** in exposure — *plus* an independent defect, a matched-noise control **bit-identical** to its baseline with the pre-registered guard `matched_noise_verified_lifting: false` firing **without blocking the PASS** |

**This is one structural property, not two independent bugs.** A single instrument defect —
hold-weighted committed-class entropy — is the load-bearing DV on *both* sides of a route-selection
decision, so the decision to abandon one route for another was made on two readings of the same
broken ruler. Neither the abandonment nor the destination is currently evidenced.

Per the Step 8 adjudication this is recorded as a cluster finding here; the MECH-448 half is carried
by the already-recommended `/failure-autopsy` of **689d** (sweep routing item 2), which must also
address 689d's independent matched-noise vacuity — a defect that survives any DV repair.

---

## 6. What the withdrawal costs, and what it does NOT

### Withdrawn: the 713 route-exhaustion verdict

The 713 override note asserts:

> "713 is the FIRST run in the 709→711→713 arbitration lineage where the conversion question was
> VALIDLY measured — a FAIR bounded limbic parity win — and C1 STILL failed (ON 0.870 < OFF 0.877).
> The cross-loop-arbitration-reweighting conversion route is EXHAUSTED."

**The first clause survives; the second does not.** The parity win *was* fair and *was* validly
measured (sec 2a). But "C1 STILL failed" is a reading of the disqualified statistic, and the two means
quoted — 0.870129 vs 0.877113, a gap of **0.0070 nats** — are ~5% of the flip band. **"EXHAUSTED" is
withdrawn as unsupported.** The correct statement is: *the arbitration-reweighting route has never been
validly tested for conversion at fair parity.* The 709 (sub-threshold) and 711 (saturated) legs fail
for their own independently-SAFE reasons and remain unconverted; 713 removed those confounds and then
measured conversion with a broken instrument.

### NOT withdrawn: the re-derive brake and the 713x refusal

Per the Step 8 adjudication, **both stand.**

- The brake fired on `substrate_ceiling` / `non_contributory` (MECH-439 11th, ARC-108 8th, ARC-110
  3rd). This re-adjudication leaves every one of those directions **unchanged** — indeed it adds a
  second, independent reason the runs are non-contributory. **The brake count is undisturbed.**
- **A same-question `713x` re-letter remains REFUSED.** Re-opening the arbitration-reweighting route
  requires a **corrected-DV** instrument, not another letter circling the same ceiling on the same
  broken readout. A re-letter would reproduce the defect at the same compute cost — precisely the loop
  the brake exists to stop.

The upstream substrate `f_dominance_conversion_ceiling` is **not built** (parked behind MECH-457 +
INV-088), so the `implement-substrate` routing of both July autopsies also stands unchanged.

---

## 7. Mandatory illusory-conflict check

**Required because** withdrawing the "no conversion" half removes evidence bearing on ARC-108 /
ARC-110 in one direction without supplying it in the other.

**Result: the check is structurally satisfied, for an unusual reason — there was no live weight in
either direction to begin with.**

1. **Nothing is removed from the scoring layer.** All six `claim_evidence.v1.json` entries were
   already `scoring_excluded: "non_contributory"`. Withdrawing the reasoning behind an
   already-excluded entry cannot change any conflict ratio, confidence, or promotion state.
2. **No "supports" is left narrower.** This withdrawal removes a `weakens`-flavoured *reading*, not a
   `supports`. The usual illusory-conflict hazard — clearing FAILs until a thin remaining support
   looks robust — does not arise, because ARC-108 / ARC-110 gain nothing here.
3. **The genuine hazard is the opposite one, and it is flagged.** The risk is not that ARC-108/110 look
   falsely strong; it is that the **planning layer** looks falsely *settled* — a route recorded as
   "exhausted" and a redirect recorded as sound, both resting on the same broken instrument (sec 5).
   That is surfaced as the cluster finding, not buried.
4. **Both runs remain `pending_retest_after_substrate: true`** on all three claims, unchanged.

**Conclusion: no illusory conflict resolution.** Confidence and conflict ratios for MECH-439,
ARC-108 and ARC-110 are **arithmetically unchanged** by this document.

---

## 8. Learning extracted

1. **A conjoined interpretation label can split cleanly along the contamination seam.** 711 and 713
   each pack a *mechanism-achieved* claim and a *conversion-failed* claim into one label string. The
   first rests on strict `>0` counts and exact-zero readings (SAFE); the second on a hold-weighted
   entropy margin (DISQUALIFYING). Adjudicating the label as a unit would have been wrong in **both**
   directions — discarding a real substrate achievement, or preserving an unwarranted ceiling verdict.
2. **Label-writing guidance:** a self-route label of the form `<X>_but_<not-Y>` is a compound
   assertion. Where X and Y rest on readouts of different triage classes, they should be emitted as
   **separate criteria with separate direction fields**, not concatenated into one label.
3. **An already-`non_contributory` run can still carry live load — through the planning layer.** The
   scoring layer had correctly neutralised both runs, yet the 713 note was still steering route
   selection, a brake, and a redirect. **Governance-override to `non_contributory` neutralises
   claim weight but does NOT neutralise a written verdict.** Re-adjudication must inspect override
   notes, not just `evidence_direction`.
4. **713's exact-`0.0` saturation reading is the cleanest threshold-invariance instance in the corpus**
   — a worked example of the sweep's SAFE class: measured exactly at threshold and structurally unable
   to move under replication.
5. **One broken instrument on both sides of a route decision is a distinct failure class.** When the
   same disqualified DV is load-bearing for both "route A is exhausted" and "route B is the answer",
   the *decision between them* is unevidenced even if each side's other criteria are sound.
6. **A divergence-gated experiment's exposure-asymmetry statistics must be computed over the divergent
   subset.** The sweep's +65% figure came from a non-divergent seed outside the C1 evaluation set.
   The verdict held, but the audit trail should quote the numbers that entered the decision.

---

## 9. Routing

**`governance-adjudication` (partial re-adjudication).** No re-queue, no substrate build, no demotion.

Governance should:

1. **Leave both manifests untouched** and both `evidence_direction` values at `non_contributory` for
   MECH-439 / ARC-108 / ARC-110. No index rebuild is required for direction purposes.
2. **Append the `evidence_quality_note` text drafted below** to each manifest's existing note, so the
   partial withdrawal travels with the run.
3. **Record the 713 route-exhaustion withdrawal** in the `v4_loop_segregation` substrate_queue entry
   the 713 autopsy amended: the "terminal negative for the arbitration-reweighting conversion route"
   framing must be softened to "never validly tested for conversion at fair parity".
4. **Carry the sec 5 compounding finding into the 689d autopsy** (sweep routing item 2).
5. **Take no action on V3-EXQ-709** — PASS-SAFE, adjudicated invariant in both directions by the 708
   autopsy sec 11.

### Draft `evidence_quality_note` — V3-EXQ-711

> [PARTIAL RE-ADJUDICATION 2026-07-20 per confirmed failure_autopsy_V3-EXQ-711-713_2026-07-20
> (user-adjudicated), following the hold-weighted-E3-readout corpus sweep (form 2). The conjoined
> interpretation label splits along the triage seam. SURVIVES: "ascending spiral gain LETS LIMBIC WIN"
> — `limbic_loop_can_win` is a per-seed strict `clg_limbic_ge_motor_ticks > 0` (:1098), 3.0 vs 3.0 at
> LIMBIC_WIN_PASS_FRACTION 0.75, threshold-invariant; weights moved 4897.8 vs 1e-06; `frac_pre_ge2`
> exactly 1.0. The 2026-07-04 saturated-runaway finding also survives (SAFE weight-space statistics).
> WITHDRAWN: the "does not convert the ceiling / ceiling-intrinsic" half. `C1_learned_strict_above_static`
> is a +0.05 nat margin on `committed_class_entropy_nats`, accumulated per env step from
> `int(action[0].argmax())` on the `select_action` return (:836/:893/:910-914); `agent.py:5430` returns
> the HELD action on `not ticks["e3_tick"]`, so the DV is hold-weighted — a distribution-shape statistic,
> DISQUALIFYING. Only seed 42 clears (+0.1030); shortfalls 0.0993 (s44), 0.2598 (s46). Max divergent-seed
> arm exposure asymmetry −31.5% (s44); the sweep's "+65%" is s45, non-divergent and outside the C1 set.
> The 663 calibration (<1%, sign-varying) does NOT apply — the arms differ in hold duration (699 autopsy
> sec 4d). evidence_direction UNCHANGED (`non_contributory` all three, already scoring_excluded);
> `pending_retest_after_substrate` UNCHANGED; re-derive brake UNCHANGED. PROMOTES NOTHING, DEMOTES NOTHING.]

### Draft `evidence_quality_note` — V3-EXQ-713

> [PARTIAL RE-ADJUDICATION 2026-07-20 per confirmed failure_autopsy_V3-EXQ-711-713_2026-07-20
> (user-adjudicated), following the hold-weighted-E3-readout corpus sweep (form 2). SURVIVES: the
> "BOUNDED PARITY WIN" half — `limbic_loop_parity_win` is `clg_limbic_parity_band_ticks > 0 and not
> saturated` (:1155), 4.0 vs 3.0; `no_saturation_blowup` measured EXACTLY 0.0 vs threshold 0.0, the
> strongest form of threshold invariance; weights moved 0.1694 vs 1e-06; `frac_pre_ge2` exactly 1.0.
> The 2026-07-05 learning "711 missing-controller gap CLOSED — fair non-saturated limbic parity win on
> 4/4 divergent seeds" STANDS. WITHDRAWN: the "does not convert the ceiling / ceiling-intrinsic" half,
> AND with it the verdict that the cross-loop-arbitration-reweighting conversion route is EXHAUSTED.
> `C1_learned_strict_above_static` is a +0.05 nat margin on the hold-weighted `committed_class_entropy_nats`
> (:869/:938/:955-959; `agent.py:5430`) — DISQUALIFYING. ZERO seeds clear; shortfalls 0.0147 (s42),
> 0.0511 (s44), 0.0687 (s47), 0.1248 (s46); seed 44's raw delta is −0.0011, indistinguishable from zero;
> the quoted ON 0.870129 vs OFF 0.877113 gap is 0.0070 nats, ~5% of the 699 flip band. This is the most
> fragile C1 in its lineage. Max divergent-seed exposure asymmetry −23.3% (s46), range 33.7 pp; the 663
> calibration does NOT apply (arms differ in hold duration, 699 autopsy sec 4d). CORRECTED READING:
> the arbitration-reweighting route was never VALIDLY TESTED for conversion at fair parity — not that it
> was tested and exhausted. RETAINED UNCHANGED: evidence_direction `non_contributory` all three (already
> scoring_excluded), `pending_retest_after_substrate`, the re-derive brake (MECH-439 11th / ARC-108 8th /
> ARC-110 3rd — all directions unchanged), the REFUSAL of a same-question 713x re-letter (re-opening the
> route requires a CORRECTED-DV instrument, not another letter on the same broken readout), and the
> `implement-substrate` routing to `f_dominance_conversion_ceiling` (not built; parked behind MECH-457 +
> INV-088). COMPOUNDING FINDING: the July redirect FROM this route TO the MECH-448 selection face is
> unsupported at both ends — 689d's `C_PRIMARY` is compromised by the same defect (sweep sec 4b), plus an
> independent bit-identical matched-noise control. PROMOTES NOTHING, DEMOTES NOTHING.]

---

## 10. Hypothesis-space ledger (Step 9b)

**No ledger write.** No question in `hypothesis_space_registry.v1.json` covers MECH-439 / ARC-108 /
ARC-110 or the 709→711→713 lineage; this autopsy emits **no `fanout_recommendation`** (the routing is
a partial withdrawal with the refusal retained, not a discrimination portfolio) and **adjudicates no
pre-registered leg**. Per the skill, Step 9b skips cleanly. `initial_frozen_count` and all
`total_initial` series are unaffected.
