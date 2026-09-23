# GFLAG-0297 -- a non-permutation null for MECH-439 rung 3 (E3 channel commensurability): design on paper

**Generated:** 2026-09-23T19:20:47Z
**Session:** `great-thompson-014b27` (chip `chip-20260923-gflag0297-mech439-rung3-null`)
**Flag worked:** GFLAG-0297 (open). Read with GFLAG-0234 (resolved, user-approved target amendment),
GFLAG-0072 (resolved, class-entropy precondition) and `failure_autopsy_V3-EXQ-1012a_2026-09-14` (CONFIRMED).
**Substrate under validation:** `f_dominance_conversion_ceiling` rung 3 / SD-E3-CHANNEL-COMMENSURABILITY,
ree-v3 `c47b885`, `ree_core/predictors/e3_selector.py` (`_commensurability_scale` L1539,
`_update_channel_scale_estimates` L1556, `score_trajectory` channel terms L1677-1745).
**Claim:** MECH-439. **Its direction does not change on this record.** This is substrate-validation design, not a claim test.

**Outcome:** **V3-EXQ-1012c QUEUED**. ree-v3 `d4811c5025` (driver `experiments/v3_exq_1012c_e3_commensurability_eligibility_stage_validation.py` + queue entry), reconciled into the coordinator DB (`/queue/active`: present). Red-team (Step 4.5, **fable**, cross-model, run on the design spec before authoring): **CONTESTED**. All 6 findings were dispositioned (sec. 7), plus one further finding from the Step 3.5 code review. Smoke PASS on both cells.

---

## 0. Summary

1. **The whole magnitude-perturbation family is closed at the primary-score stage, not just the permutation.** Section 2 shows
   each form is either an identity of the operator, decided by a free design knob, or answers a question other than rung 3
   (whether the running estimate is current). Per-channel argmin agreement (the tautology doc's option 2, and the
   1012a autopsy's preferred replacement) is also entailed at this stage. **No primary-stage null can validate rung 3.**
2. **New measurement, from a manifest that has already landed: the primary stage is not where the executed action is decided in this regime.**
   V3-EXQ-571c ran the same 936-regime config (its starved arm is byte-identical to 1012a's OFF path). It recorded the
   modulatory shortlist active on **100%** of selections in all 16 cells, shortlist size **5-16 of k = 32**, and
   `final_commit_by_primary_frac` **0.005-0.146**. In `select()` the primary score reaches the executed action **only**
   through membership of the margin-eligible set. So 1012a's primary-argmin flip rate (0.82 / 0.72) bears on the
   executed action through eligibility alone.
3. **A criterion that is not an identity exists one stage down.** At the eligibility stage the operator's output meets a
   structure the operator does not define: a margin denominated in the score **range** (`raw <= min + 0.25 * range`).
   The operator equalises cross-candidate **SD**. Section 4 shows on paper that an eligibility-authority ratio can
   **PASS** (equal realised spread gives R = 0.998) and can **FAIL on a gate-green run**, in two separate ways that no gate
   reads:
   - **EMA lag:** one channel's realised per-tick spread at 5x or more of its running estimate. R = 0.26 at 5x and 0.135 at 10x.
   - **Shape:** a spike-shaped channel. **R = 0.227 with the operator working perfectly** (negative spike, r = 1).
     A positive spike at 3x gives R = 0.108 with the eligible set inflated to 28 of 32.

   571c's OFF shortlist sizes (9.5-15.7 fed, 6-8.5 starved, against a Gaussian expectation of 5.4) already show that
   the dominant channel's per-candidate distribution is right-skewed in this regime. So the shape failure is a live
   possibility here, not just a textbook case.

---

## 1. Premises re-measured (CLAUDE.md "audit its premises")

| Premise (from chip / flag) | Re-measured 2026-09-23 | Holds? |
|---|---|---|
| No 1012 successor queued | `grep V3-EXQ-1012 ree-v3/experiment_queue.json` -> none; no `1012c`/`rung3` script in `ree-v3/experiments/` | yes |
| 1012b refused because a scale permutation cannot equalise | GFLAG-0297 arithmetic (8/8 cells keep D dominant under both derangements) | yes -- and the 1012a autopsy had **already withdrawn** the permutation placebo in its own sec. 5c-bis before 1012b was built; 1012b implemented a withdrawn recommendation |
| The flag's structural note points at magnitude-perturbation / bootstrap | read; sec. 2 below closes both at the primary stage | holds as a pointer, fails as a design |
| GFLAG-0072 precondition applies (P1 raised toward action_dim, P2 armed) | GFLAG-0072 resolution note: "ANY future ARC-065/MECH-439/440/441 ... null must set P1 and arm P2". 1012a manifest: `use_modulatory_selection_authority: true` (P2 armed), `support_preserving_min_first_action_classes: 2` (P1 **not** raised) | yes; 1012a met P2, not P1 |
| Candidate count k unrecorded (autopsy change 4) | 571c manifest records `n_candidates` **32.0 in all 16 cells** of this regime | k = 32 is known for the regime. Independence flip baseline = 1 - 1/32 = **0.969**; 1012a's 0.82 / 0.72 sit below it (correlated rankings; no directional gloss) |
| The operator reaches the executed action | 571c: shortlist active 100%, `final_commit_by_primary_frac` 0.005-0.146 | **only via eligibility** (sec. 3) |

---

## 2. The primary-stage null family, closed on paper

Notation: live channels c with raw per-candidate term t_c,i. The operator divides by m_c = s_hat_c, an EMA
(alpha 0.05, so about a 20-tick memory) of that channel's tick-local cross-candidate SD sd_c(t), taken from **prior**
ticks. Primary score S_i = sum_c t_c,i / m_c. OFF: m_c = 1. D = the channel dominant under OFF (residue fed, harm starved).

| Null | What it perturbs | Outcome on paper | Verdict |
|---|---|---|---|
| **(a) Label permutation of m** (1012b) | which channel gets which divisor | with live scales spanning about 4 orders of magnitude, every bijection keeps D on top (GFLAG-0297) | **degenerate** (already refused) |
| **(b) Unit perturbation** -- multiply a channel's raw term by a constant lambda (e.g. rho_residue x 10) | the channel's units | at EMA convergence (lambda t)/(lambda s_hat) = t/s_hat exactly: the operator is **scale-equivariant by construction**, so a unit-invariance test cannot fail | **identity** |
| **(c) Divisor jitter** m_c <- m_c * exp(sigma * eps_c) | the magnitude of each divisor | difference from the operator is 0 at sigma = 0 (FAIL certain) and moves to the random-dictator / permutation regime as sigma grows (GFLAG-0297 arithmetic applies there). **The verdict is set by sigma, a free knob.** The only non-arbitrary sigma is the operator's own estimation error, the spread of log(sd_c(t)/s_hat_c(t)), which turns (c) into (d) | **knob-determined** |
| **(d) Bootstrap / tick-shuffle** m_c <- sd_c(t') from another tick of the same channel (the 1012a autopsy's fallback) | how current the scale estimate is | non-degenerate: it depends on how non-stationary sd_c is on about a 20-tick scale, which has never been measured. But **both outcomes are silent on rung 3**. "No difference" means gross unit conversion does the work; "difference" means currency matters. Neither says whether the monopoly is removed where the decision is made | **non-validating** (off-question) |
| **(e) Per-channel argmin agreement with the commit, OFF vs ON** (tautology doc option 2; the autopsy's *preferred* replacement) | nothing -- it is a DV | at the primary stage any rescaling that raises channel c's relative weight raises P(commit = argmin_c). OFF gives c about 1e-3-1e-5 of D's weight and ON gives it about 1/3. So "ON agrees with non-D channels more than OFF" is entailed | **entailed** |

**The durable point:** at the primary stage "commensurable" has **no referent outside the operator's own definition**
(equal cross-candidate SD). Every primary-stage DV either restates that definition, or its outcome is fixed by a knob,
or it answers an adjacent question. The primary-argmin lineage cannot validate rung 3, whatever null it uses. The
referent has to come from a structure the operator does not define. In this regime the next such structure is the
eligibility margin.

---

## 3. Where the operator's output reaches the executed action

`e3_selector.py` `select()` (L4120-4395), with 1012a's config (`use_modulatory_shortlist_then_modulate: true`, margin mode,
`use_go_nogo_constitution: false`, `use_f_eligibility_demotion: false`, `use_gap_scaled_commit_temperature: false`,
margin 0.25, config.py L1828) works as follows:

1. `raw_scores` = the operator-scaled primary scores (L3315; exposed as `self.last_raw_scores`), `raw_score_range = max - min` (L3316).
2. E = { i : raw_i <= min(raw) + 0.25 * raw_score_range }.
3. The executed candidate is the argmin (committed) or softmax sample (uncommitted) of `_modulatory_accum` over E. The
   primary score is **absent** from this step.

So the operator changes the executed action **only by changing E**, apart from the ticks with |E| <= 1. 571c measured
`final_commit_by_primary_frac` at 0.005-0.146 in exactly this configuration. A rung-3 validation that is meant to license
releasing the 936-family / 654h-class conversion-falsifier refusal (`f_dominance_conversion_ceiling.depends_on_unresolved[2]`)
has to be read at the eligibility stage or later. 1012a read it one stage earlier.

This is a **measurement**, not a new build: E is a pure function of the primary scores. Reconstructing it is three lines
on captured scores. It is **not** the final-commit replay the 1012a autopsy reserved for separate governance scoping
(7a, "Explicitly NOT recommended", last bullet), because it never touches `_modulatory_accum`.

---

## 4. The design (V3-EXQ-1012c, queued) and the on-paper failure demonstration

Full spec: section 6. Core:

- **DV.** For each channel c live by its EMA: J_c = tick-mean Jaccard distance between E(S) and E(S with c's scaled
  term removed), taken over ticks where c has content. **R = min_c J_c / max_c J_c.** R is 1 when every live channel moves
  eligibility equally and 0 when one channel alone decides eligibility.
- **References, neither of them a permutation, both computed on the same tick and the same candidates:**
  - **OFF shadow** (m = 1) is the monopoly anchor. It is **reported, never gated**; the tautology doc's Finding 2 is why.
  - **ORACLE shadow** (m_c = the tick-local sd_c(t)) is the decomposition anchor. It is the bootstrap idea done
    properly: not a null the operator must beat, but a way to separate EMA lag from shape.
- **C1:** per regime, PASS iff R_ON >= 0.25 in at least 3 of 4 seeds.

**Monte Carlo** (k = 32, margin 0.25, three standardised live channels, one channel "D" varied; scratchpad `elig_R.py`,
20,000 ticks per case):

| D's realised geometry | R | mean |E| | reading |
|---|---|---|---|
| Gaussian, r_D = 1 (perfect commensuration) | **0.998** | 5.4 | PASS is reachable |
| Gaussian, r_D = 3 | 0.408 | 5.4 | PASS |
| Gaussian, r_D = 5 | 0.260 | 5.4 | at the bar: **0.25 corresponds to "no live channel running at more than about 5x the others"** |
| Gaussian, r_D = 10 | **0.135** | 5.4 | FAIL (EMA lag) |
| Gaussian, r_D = 30 | 0.046 | 5.4 | FAIL |
| positive spike (one outlier cost), r_D = 1 | 0.808 | 9.6 | PASS; E already inflated |
| positive spike, r_D = 2 | 0.401 | 20.5 | PASS, marginal |
| positive spike, r_D = 3 | **0.108** | 28.2 | FAIL: the margin admits almost everything, so no primary channel has authority |
| negative spike (one standout candidate), r_D = 1 | **0.227** | 1.6 | **FAIL with a perfect operator** (shape; ORACLE fails too) |
| OFF-like scale gap 1e3 / 1e5 | 0.0014 / 0.0000 | 5.4 | the monopoly anchor |

Here r_D is D's realised per-tick spread relative to the others after normalisation: sd_D(t)/s_hat_D(t) against 1.

**Why this is not a V3-EXQ-1012 / 1012b / 1051-shaped defect:**

- **Not an identity.** R_ON depends on r_c(t), which is set by how non-stationary sd_c is relative to a roughly
  20-tick EMA, and on each channel's per-candidate **shape** relative to a range-denominated margin. The operator fixes
  neither. The operator equalises SD, and SD-equalisation is not range-equalisation: a single-candidate spike has
  standardised range up to sqrt(k - 1) = 5.57 at k = 32, against about 4.1 for 32 Gaussian draws, and the sign of the
  spike decides whether the margin swallows or starves the eligible set.
- **Can FAIL on a gate-green run.** The instrument gates (score reconstruction, |E| equal to the live shortlist size,
  selected candidate inside E) and the readiness preconditions (operator engaged, at least 2 channels live by EMA,
  enough ticks, clamp and residue protocols landed) read neither r_c(t) nor channel shape. Every FAIL row in the table is
  reachable with every gate green.
- **Can PASS.** First row.
- **Not knob-decided.** The single threshold is anchored in the arithmetic above (about a 5x realised dominance), not
  chosen to make a known outcome come out.
- **Not answerable from landed data.** 1012a recorded final scale estimates only, never per-tick sd_c(t), shape, or E.
  571c recorded shortlist sizes under OFF only.

**What PASS and FAIL would mean:**

- **PASS:** the operator's equalisation survives to the stage where the executed action is decided, tick by tick, in
  both regimes. That is the release condition `depends_on_unresolved[2]` actually needs. Governance makes the release
  call.
- **FAIL with the ORACLE passing** means EMA lag. The substrate amend is to the estimator: alpha, or a tick-local scale.
- **FAIL with the ORACLE failing** means shape. SD normalisation is mismatched to a range-denominated margin. The
  substrate amend is a robust or range-type scale, or a rank-based margin.
- **OFF also at or above the bar** means there is no eligibility-stage monopoly to remove in that regime, so rung 3 is
  moot there. That is informative, but it is not a PASS.

Every branch routes somewhere specific, and every branch is `non_contributory` for MECH-439.

---

## 5. What this does NOT do

- It does not grade whether the operator's re-ranking is "principled" (1012a autopsy sec. 5b). Section 2 argues that
  question has no referent at the primary stage. At the eligibility stage the question becomes whether the operator
  stops one channel deciding eligibility alone, which is what the conversion ceiling needs.
- It does not build the final-commit replay (`_modulatory_accum` over E). That stays reserved for governance scoping, per
  the confirmed autopsy.
- It does not test MECH-439.

---

## 6. Spec

The driver's module docstring is the authoritative as-built spec. It differs from the pre-red-team sketch in these ways:

- **Instrument gates, rebuilt per red-team F1/F2:**
  - **I1** is a real residual: live score against the reconstructed channel sum. The smoke measured a max relative residual of 1.06e-7.
  - **I1b** is 1012a's same-config replay self-check.
  - **I1c** is new: a genuine operator-OFF replay must equal the reconstructed S_OFF. This is independent proof that the captured per-candidate terms are the terms the selector used.
  - **I2** reproduces the selector's own margin ops in torch float32 on `agent.e3.last_raw_scores`, gated on a mismatch **rate** of 1% or less. The smoke had 0 mismatches in 28 shortlist-active ticks.
- **Capture.** `_last_commensurability_raw` is read after **each** `score_trajectory` call, never once per tick. The divisor comes from the **pre-tick** EMA snapshot, using `_commensurability_scale`'s warmup and floor semantics. Channel signs are +f, +harm, +residue, -benefit, -goal.
- **Content ticks** (sd_c(t) >= 0.1 * s_hat_c) are one shared tick set for ON, OFF and ORACLE. A channel enters R only with at least 30 content ticks; excluded channels are recorded with a reason.
- **Verdict grid is a partition.** Precedence is instrument first, then a per-regime class, one of {`not_ready`, `moot`, `commensurate`, `ema_lag`, `shape_range`}. PASS iff both regimes are `commensurate`; otherwise FAIL `fed_<class>__starved_<class>`. A red arm gate scopes out only its own regime. This was the Step 3.5 finding: the first build ANDed the two arm gates across the whole run, the V3-EXQ-785 defect.
- **Capture-collapse guard.** `criteria_non_degenerate` is false for a regime whose R_ON equals R_OFF in every cell: red-team F1's worst case, caught structurally.
- **Readouts reported, not buried (F4).** `r_realised_quantiles`, `shape_high_quantiles` / `shape_low_quantiles`, eligible-set sizes (ON / OFF / ORACLE / live), `final_commit_by_primary_frac`, k quantiles, and 1012a's primary flip rate recomputed for continuity.
- **Manifest direction.** The manifest emits `evidence_direction: non_contributory` **and** an `evidence_direction_note` **and** `evidence_direction_per_claim`. This closes the 1012a autopsy sec. 5g defect, where the indexer re-inferred `supports` from a PASS.
- **Regime.** Byte-identical to 1012a: seeds 42/43/45/46, P0 60, P1 to 200 genuine selections. P1 floor stays at 2 (see F5). R_BAR 0.25, SEEDS_REQUIRED 3.

**Smoke** (1 seed, P0 4, 60 steps; DV engaged, `substrate_not_ready` label expected at this n):

| cell | R_ON | R_OFF | R_ORACLE | final_commit_by_primary_frac |
|---|---|---|---|---|
| fed | 0.561 | 0.000 | 0.787 | 0.000 |
| starved | 0.818 | 0.044 | 0.752 | 0.125 |

The OFF anchor behaves as predicted, and the manipulation reaches the DV. This is a smoke reading, not a result.

---

## 7. Red-team (Step 4.5) and disposition

**Verdict: CONTESTED** (model **fable**, cross-model; this session ran on Opus). Findings file: session scratchpad `redteam_1012c.md`. One pass. It was not re-spawned, because no finding was BLOCKING and none changed the causal chain.

The reviewer **independently confirmed** that the criterion is not an identity: its own Monte Carlo gives R = 0.207 for a sparse-LOW channel at exactly unit SD. That matches this record's 0.227 from a different script.

| # | Finding | Disposition |
|---|---|---|
| F1 (HIGH) | The spec's I1 was `(a-b)+b`, an identity. A per-tick read of `_last_commensurability_raw` or a post-update divisor would have made E(S_OFF) equal E(S_ON), and the run would report "rung moot" with every gate green | **Fixed.** Residual gate + replay self-check + the new genuine-OFF-replay cross-check (I1c) + a structural ON/OFF separation check in `criteria_non_degenerate`. Verified on smoke |
| F2 (MED) | I2's exact equality is float32-ULP-fragile at ON-path score magnitudes (about 1e3-1e4): roughly a 70% chance a sound run is refused | **Fixed.** Float32 reconstruction with the selector's ops, gated on a 1% rate. The smoke had 0 mismatches |
| F3 (MED) | The verdict grid was not a partition; the ORACLE seed rule, the moot/PASS precedence, and undefined R were all unstated | **Fixed.** Partition with explicit precedence; the ORACLE uses the same 3/4 rule; zero-content channels are excluded with a reason; R = 0 when no channel moves E |
| F4 (MED) | `ema_lag` is close to unreachable (residue never resets per episode; bursts need duty > 0.97). The realistic outcomes are {PASS, shape_range}, and PASS is the prior | **Accepted and stated.** The PASS prior is in the docstring and in `interpretation.prior_note`; the shape index and r_c(t) are reported readouts; ON and ORACLE share one content-tick set |
| F5 (LOW) | The starved OFF gap is 4-25x, not 1e3-1e5. R_OFF is predictable at about 0 fed and 0.06-0.08 starved, so the moot branch is expected-dead. Raising P1 breaks the regime match | **Fixed** (premise corrected; moot documented as expected-dead). **P1 kept at 2:** GFLAG-0072's ceiling binds committed-class-entropy DVs, and this DV is candidate-level eligibility membership |
| F6 (LOW) | I3 is implied by the selector; only 3 of 5 channels can be live; `n_live >= 2` is a formality | **Accepted.** I3 is a recorded count only; the readiness precondition does not read R |
| extra | The reviewer notes that f's cross-candidate spread is relative ~1e-4 of its mean and is amplified to parity | **Recorded.** A PASS includes f's micro-spread by the operator's design (docstring, and sec. 8 below) |

**Step 3.5 code review, one further finding:** the first build ANDed the two arm readiness gates across the whole run, so one red arm would vacate the other arm's reading. **Fixed** with a per-regime `not_ready` class.

## 8. Notes for governance

- **A PASS licenses only what `depends_on_unresolved[2]` needs.** The operator's equalisation survives to the stage where the executed action is decided, in both regimes. Whether to release the 936-family / 654h-class refusal remains a /governance call. A PASS also counts f's ~1e-4-relative spread as a commensurate channel, which is the operator's design.
- **A `shape_range` FAIL is a substrate finding, not a null.** It means SD-normalisation is mismatched to a range-denominated margin. The amend is a robust or range-type scale, or a rank-based margin, and routes to `/implement-substrate` on `f_dominance_conversion_ceiling`.
- **Process observation.** 1012a's own Step 4.5 red-team finding (2) *added* the `majority_clears_floor` disjunct. The 1012a autopsy later found that disjunct made the criterion unfailable. A red-team fix can introduce the defect class it is meant to catch. 1012c has one criterion per regime and no disjunct.
- **Step 2.5c known limitation.** 1012c runs under open corrupting entry `contextmemory-write-path-addressing-degeneracy` (`ContextMemory.write` is live and its fix is default-off). It shapes the candidate inputs upstream of the stage under test. Rung 3 has to be validated in the regime the conversion falsifiers run in, which carries the same defect, as 1012a and 571c did. A later default flip changes the regime.
- **Step 9.5.** The plan-gap drift check flags `behavioral_diversity_isolation:GAP-K` (MECH-439 overlap) for `/inter-governance-brief`. Informational.
