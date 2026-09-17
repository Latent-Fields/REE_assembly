# Failure autopsy -- V3-EXQ-1043 (MECH-537)

**STATUS: `confirmed`** -- interactive Step 8 gate held 2026-09-17.

| | |
|---|---|
| run_id | `v3_exq_1043_mech537_communication_subspace_routing_20260916T111630Z_v3` |
| queue_id | V3-EXQ-1043 |
| claims | MECH-537 (first experimental evidence for this claim) |
| purpose | `diagnostic` (excluded from confidence scoring) |
| outcome | FAIL -- C1, C3, C4a, C5 passed; C2 and C4b (both load-bearing) failed |
| self-route | `routing_signature_incomplete_undetermined` |
| machine | ree-cloud-2, `linux-x86_64-py3.10-torch2.12.0+cpu`, 7079 s |

---

## 1. Facts

`check_dry_run_citations.py` over every cited id: **4 clean, 0 dry**. `validate_recording.py`: **complete**, no always-core gaps.

All **7 readiness preconditions** met (worst seed each): source adequacy 0.9335 vs 0.8; elevation over the strongest trivial predictor 0.3532 vs 0.2; RRR held-out r2 0.9971 vs 0.5; random-rank control 0.2188 vs 0.05; held-out steps 1965 vs 500; encoder trained 0.2884 vs 1e-6; z_world participation ratio 3.8375 vs 2.0.

| criterion | type | measured | threshold | passed |
|---|---|---|---|---|
| C1 full-minus-comm | absolute (rank-confounded) | 0.17174 | >= 0.05 | yes |
| **C2 orientation, rank-matched** | **discrimination, load-bearing** | **0.03196** | >= 0.05 | **no** |
| C3 complement retains | absolute upper bound | 0.01366 | <= 0.05 | yes |
| C4a null-margin | discrimination, *not scored* | 0.48155 | >= 0.15 | yes |
| **C4b absolute ceiling** | **absolute, load-bearing** | **0.84684** | <= 0.5 | **no** |
| C5 single-subspace premise | premise | 0.63574 | >= 0.36995 | yes |

C2 per-seed `[0.03724, 0.04949, 0.00916]` -- **every value positive**, none clearing the floor. Its predicate is a three-way conjunction (floor AND mean >= 2*sd AND seed-majority) and all three clauses fail together: 0.03196 < 0.05, 0.03196 < 0.03377, 0 of 3 seeds clear. The dedicated non-positive falsification predicate returns False, so no rank-explains-it falsification is licensed either. This is the driver's designed fifth branch -- an explicit "no verdict claimed".

C5 held, so the run was **not** routed away to MECH-547 / MECH-555.

## 2. Claim layer

**MECH-537** (`mechanism_hypothesis`, `candidate`, `epistemic_category: standard`, `implementation_phase: v3`, registered 2026-09-08). This is its **first** experimental evidence: an unrestricted grep over all 513 `failure_autopsy_*` artifacts finds no reference to it in any field.

**Flagged to governance, not resolved here:** the claims.yaml entry contradicts itself. Its `notes` end `"DO NOT queue an experiment from this entry."` (2026-09-08) while `what_would_answer` carries a 2026-09-15 disposition minting proposal EXP-1403 and authorising exactly this run. Both are live text on the same entry.

## 3. Biological reference

Communication-subspace routing between populations (Semedo et al. 2019, V1->V2) is a directly measured neural phenomenon, and the REE operationalisation uses the same estimator family (cross-validated RRR). **Not a formal-definition import.** Literature is **PRESENT** -- `targeted_review_mutual_legibility_communication_subspaces` carries Semedo2019, Binish2026, Gonzalez2026. Caveat recorded rather than smoothed: MECH-537's own notes say those references were taken from the originating thought's reference list and are not independently verified.

The load-bearing translation gap is about **rank**, and it is a finding about the substrate rather than the probe: in cortex the communication subspace is strictly lower-rank than the receiver population, whereas here cross-validation saturates and selects rank = dy, where the RRR is unconstrained OLS.

## 4. Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | **unclear** -- the claim could have expressed itself; the discriminating contrast was underpowered. NOT a weakening. |
| Biological reference | clear; lit present |
| Prerequisites | present (7/7) |
| Implementation | partial -- probe complete; the encoder under test carries SD-106 and ran with `p0a_field_weight_on = 0.0` |
| Environment | adequate -- the readiness gate establishes the oracle action IS in the sender |
| Measurement | **under-instrumented -- DOMINANT** |
| Integration | coupled; **not** rank-censored (see withdrawn W2) |
| Scale | likely insufficient (n=3) |

**Failure location (GOV-FAILLOC-1):** mechanism `not_established`, measures `not_established`, environment `partial`, REE **false**. **Net: MIXED, MEASURES-dominant -- not chargeable to REE and not to MECH-537.**

## 5. Routing

`queue-experiment`, **alphabetic suffix V3-EXQ-1043a** (same scientific question, instrument repair; CLAUDE.md's tie-break is the letter). Debt class `complex (probe-gated) / puzzle (known rules)`.

1. **Anchor C4b's 0.5 ceiling** from a measured reference. Do **not** promote C4a to the scored conjunct.
2. **Report C2 as a function of rank**, read at the parsimonious rank (8-10, where held-out r2 is within 0.001 of max). The low-rank premise is not testable at rank = dy.
3. **If n is raised, re-specify `SEED_MAJORITY` proportionally** (it is a fixed constant 2). Honest expectation: at adequate n the likely outcome is a CI *excluding* 0.05 -- H1 falsified, not rescued.
4. **Give C2 a within-run reference distribution** via a permutation null on the RRR fit.

**REFUSED:** a same-design n=3 re-pose. **Substrate queue: `none`.** **Secondary routing: none** -- explicitly not a lit-pull.

## 6. Gates

- **Re-derive brake: DOES NOT FIRE.** Count **0** for MECH-537 (R1-R3 recipe, committed corpus). A lettered re-test is this question's second measurement, not a re-derive loop.
- **Granularity-debt trigger: DOES NOT FIRE.** 0 tagging targets.
- **Step 7b: 1 fire (C7, `heldout_steps`), dismissed with reason** -- a readiness sample count shared by all four arms by construction, never a discriminating metric. C1/C2/C3 were applicable and did not fire.
- **Step 7c: `CONTESTED`**, run on the **session model (Opus 5) -- a SAME-MODEL pass**; the prescribed cross-model (fable) spawn failed on a monthly spend limit and the skill's stated fallback was used. 8 verdict-moving findings, **all accepted and applied**; 13 checks cleared.

## 7. Withdrawn arguments

**W1 -- "C4a is the better-anchored statistic."** Withdrawn. The driver marks it `retention_confounded` for a stated reason the draft never engaged. Retention geometry alone predicts margins of 0.348 / 0.267 / 0.365 against observed 0.548 / 0.555 / 0.342 -- and on seed 44 it **over-predicts**. Promoting it would have scored a known-confounded statistic in place of a control-free one.

**W2 -- "the rank was censored by the ladder ceiling."** Withdrawn. `RRR_RANKS = range(1,33)` is the full admissible range (rank <= dy = 32), the r2 curve is flat to seven significant figures above rank ~10, and the design's own pre-registered hazard was a *low* selected rank. Replaced by the surviving finding: **this interface has no low-rank bottleneck.**

**W3 -- "raise the seed count, deriving n from the observed sd."** Withdrawn as stated: only one of three clauses responds to n, the sd is a population sd that does not shrink, and `SEED_MAJORITY` is fixed at 2.

**W4 -- "require the successor to record the sensitivity arrays and rank curve."** Withdrawn: already recorded in this run, and that recording is what refutes W2.

## 8. Frozen ledger

New question `mech537_communication_subspace_orientation` registered (Mode A, 3 legs, all `alive`): H1-small-but-real (measurement), H2-no-orientation (instrumentation), H3-no-low-rank-bottleneck (representation). Three distinct axis families. Growth-restriction check inapplicable -- new question.

## 9. Owed to `/governance`

1. Apply `per_claim_recommendation` -- MECH-537: direction `mixed`, category `standard`, and the applicable edit `diagnostic_evidence_adjudicated: true` (verified absent on the claim).
2. Write the drafted `evidence_quality_note`.
3. Set `evidence_direction` on the manifest/index and mark the run reviewed.
4. **Decide the claims.yaml contradiction** in section 2.
5. Chip the V3-EXQ-1043a re-test. This session spawned no chip off its own unreviewed routing.
