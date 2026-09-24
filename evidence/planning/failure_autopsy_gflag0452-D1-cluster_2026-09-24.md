# Failure autopsy (staging) -- GFLAG-0452 D1 cluster: 8 PASSes that verify implementation by construction

- **Status:** `awaiting_human_confirmation`. This is a STAGING draft. Routing is not final, and nothing here has been applied to claims.yaml, manifests, review_tracker, substrate_queue or the hypothesis registry.
- **Generated:** 2026-09-24T09:13:39Z, by a governance-20260924 subagent (session `governance-20260924-autopsy-d1`).
- **Trigger:** GFLAG-0452 / user decision `rec-20260924-34e4e088`. The input is the D1 rows of `REE_assembly/evidence/planning/gflag0250_pass_driver_skim_20260924.{md,json}`.
- **Machine-readable twin:** `failure_autopsy_gflag0452-D1-cluster_2026-09-24.json`. It holds the full per-target `per_claim_recommendation` blocks.

## 0. Bottom line

I re-checked all 8 skim verdicts against the driver source and the manifest cells. **None is overturned.** One skim number is corrected: for 503a, seed 44's slot differentiation fell to 0.39, below the skim's stated range. Four findings are extended: the 517d comparator has no refractory, the 762 coordinator-write criterion is only a setter round-trip, the 757 modules are built by the driver, and the 538a precedent already covers 503a. The skim also did not scope a status consequence that matters. **Four claims were promoted candidate->provisional on runs in this cluster**:

- MECH-092, on 761
- MECH-287 and MECH-288, on 757
- MECH-302, on 517d + 517c

| Run | Claim (type) | Recommended direction | Claim status recommendation |
|---|---|---|---|
| V3-EXQ-500a (diagnostic) | SD-017 (design_decision) | supports -> **non_contributory** (it already had zero weight as a diagnostic_probe) | none, stays stable; set `diagnostic_evidence_adjudicated` |
| V3-EXQ-503a | SD-017 (design_decision) | supports -> **non_contributory** | none, stays stable |
| V3-EXQ-633 | MECH-094 (mechanism) | supports -> **non_contributory** | none, stays stable (carried by literature) |
| V3-EXQ-517c | MECH-302, SD-050 | supports -> **superseded** (duplicate of 517d) | see 517d |
| V3-EXQ-517d | MECH-302 (mechanism) | supports -> **non_contributory** | **provisional -> candidate** |
| V3-EXQ-517d | SD-050 (design_decision) | **USER CALL**. Default: supports stands, as detector implementation verification. Alternative: non_contributory | default: none, stays provisional |
| V3-EXQ-757 | MECH-288, MECH-287 (mechanism) | supports -> **non_contributory** | **provisional -> candidate** for both; MECH-287 also gets `epistemic_category: standard` |
| V3-EXQ-761 | MECH-092 (mechanism) | supports -> **non_contributory** | **provisional -> candidate** |
| V3-EXQ-762 | MECH-046 (mechanism) | supports -> **non_contributory** | none, stays provisional (its promotion predates 762); set `epistemic_category: standard` |

**The SD-versus-mechanism split, proposed as the batch rule the skim's routing note asked for:**

- An implementation-verification PASS may score `supports` on a design_decision SD only where the SD's content is "X is built and fires as specified", and only where the SD's own `what_would_answer` does not exclude the run's conditions. SD-050 via 517d is the candidate case; see the edge-case bullet below.
- It scores `non_contributory` on mechanism claims.
- It also scores `non_contributory` on an SD whose text asserts necessity or an effect. SD-017 ("REE-v3 *requires*... Without these offline phases... context representations remain globally undifferentiated") is that case. Governance already made this call for SD-017 liveness evidence in the 538a autopsy (confirmed 2026-07-10).
- **SD-050 is the edge case, so it is a user call.** The two claims' registered texts disagree:
  - MECH-302's `what_would_answer` D2 says a scheduled-injection-only run "is a valid SD-050 test and a VACUOUS MECH-302 test".
  - SD-050's own `what_would_answer` requires descents "produced by the agent's own trajectory (not scheduled injection)", with BOTH reuse sites checked on every fire. 517d uses scheduled injection and measures only `update_valence`.
- The draft default is `supports`. Choose `non_contributory` if SD-050's own falsifier governs. In that case SD-050 is left with no scoring exp support, and its 2026-08-29 promotion should be re-reviewed.

## 1. Scope checks (Step 1 / 2a)

- **Dry-run gate:** I ran `scripts/check_dry_run_citations.py` over all 8 run_ids. Result: 0 dry, 8 clean, exit 0. `excluded_dry_run_ids: []`.
- **Coverage:** I ran `scripts/check_autopsy_coverage.py`. All 8 report `AVAILABLE: YES`, so no prior artifact covers them.
- **Confidence weight of 500a (the brief asked for this):** it is already **zero**. Its `claim_evidence.v1.json` entry carries `scoring_excluded: diagnostic_probe`, because `build_experiment_indexes.py:3802-3804` excludes every diagnostic- or baseline-purpose run. The recommended direction change is record hygiene only.
- **Driver provenance:** I diffed the 517c and 517d drivers. The science is byte-identical, and the only 517d change is the `emit_outcome` sentinel. The other drivers are the committed versions the skim cited, with mechanical post-run commits only.

## 2. Per-target facts and verification

### V3-EXQ-500a -- SD-017 readiness probe (diagnostic)

- **C1:** phase counts are incremented unconditionally, once per cycle (driver :276, 283, 291, 299).
- **C2:** every phase duration is a loop constant. The replay "duration" is `sws_n_writes + rem_n_rollouts`, which was 8 + 6 in all 9 cycles, so CV = 0.0 exactly.
- **C3:** `replay_quality = rem + 0.25*sws + 0.1*div` (:311) evaluates to 6 + 2 + ~0.1. The bar of 8.0 (:139) is exactly the configured op-count term. Measured values were 8.1000-8.1011.
- **Ungated readout:** slot diversity was unchanged across the test phase (1.000/1.000 and so on).
- **Skim:** CONFIRMED.

### V3-EXQ-503a -- SD-017 sleep ON vs OFF pair

- **ARM_B:** it sets `sws_enabled = rem_enabled = use_sleep_loop = False` (:232-239) and runs zero training steps. Its zero writes, zero rollouts and zero ContextMemory change therefore hold by construction.
- **ARM_A bars:** C1 and C3 need 3 writes or rollouts against a configured 24 / 18. C2 needs a Frobenius change of 0.10 against a measured 4.50 / 4.70 / 5.03.
- **C4:** it duplicates C2 because B.M2 is identically 0.
- **Ungated readout:** in ARM_A, slot differentiation fell 0.999->0.783, 1.008->0.614 and 1.001->0.388. The skim said "0.61-0.78", which omits seed 44.
- **Why that fall is uninterpretable:** the slots start random and near-orthogonal, which is the ceiling of this metric, so any consolidation toward 20 preloaded randn prototypes must lower it. The fall is uninterpretable in either direction.
- **Precedent:** `failure_autopsy_V3-EXQ-538a` (confirmed and user-adjudicated) already ruled the SD-017 SWS/REM-write-liveness "supports" vacuous.
- **Skim:** CONFIRMED, with the numeric correction above.

### V3-EXQ-633 -- MECH-094 write gate

- **The manipulation:** the arms differ only in the `hypothesis_tag` boolean that the driver itself passes for sim events (:271-274). `ree_core/residue/field.py:690` and `:869` both return early on that tag.
- **Result:** GATE_ON contamination 0.0 and MI = ln 2 = 0.693147 are identities in every seed.
- **Setting:** ResidueField is exercised standalone, with no agent and no replay path.
- **Skim:** CONFIRMED.

### V3-EXQ-517c / 517d -- MECH-302 relief completion, SD-050 comparator

- **ARM_B:** it disables both the comparator and `valence_liking_enabled` (make_config :134-139), so C3 and C4 hold by construction.
- **ARM_A C1 is not by construction.** It is an env-dependent liveness floor: injections track agent survival, because the driver breaks on `done` (:254-255). The identical 517c design FAILED C1 on seed 43 (0 events from 1 injection) and passed only through the 2/3 fraction.
- **C2 duplicates C1:** the counted write is the relief block's own `update_valence` (`agent.py:7389-7407`). `p1_writes == p1_events` holds in all 6 ARM_A cells.
- **New finding, not in the skim:** `SufferingDerivativeComparator.tick` has **no refractory**. It fires on every tick where the drop across the 30-tick window is at least 0.005. That gives about 9-17 events per scheduled injection (1479/85, 129/8, 452/50). So an "event" is one tick that crosses the threshold, not one completed relief. Hazard-contact damage also feeds the comparator, so these ratios are upper-bound attributions. Each fire writes VALENCE_LIKING, and it also releases beta when `beta_gate.is_elevated` (`agent.py:7390`).
- **What MECH-302 says and why this run can't reach it:** MECH-302 claims relief REUSES the goal-achievement completion pipeline. In the code that reuse is hand-written into a separate block, and no beta release, phase reset or goal-achievement comparison was measured.
- **Independent ground from the claim's own text:** MECH-302's `what_would_answer` D2 already rules that a scheduled-injection-only run is a vacuous MECH-302 test, because non-contingent relief cannot credit anything the agent did.
- **Duplicate:** 517c is the same design and still scores. **Skim:** CONFIRMED and extended.

### V3-EXQ-757 -- MECH-288 / MECH-287 functional signature

- **C288_hit:** `GOAL_LEVELS` gaps of at least 10 (:154) were chosen to hit BOCPD's decisive rail, as the driver's own comment says. The result is 27/27 hits, which equals the number of planted boundaries.
- **Other criteria:**
  - Smooth-arm silence follows from 0.02 noise far below the rail.
  - C288_graded rides the fast z-score ticker: an open fraction of 0.237 against a bar of 0.20.
  - C287_dissoc feeds empty lists.
  - C287_tonic feeds 0.9-posterior events every tick against a 0.5 threshold.
- **Setup:** the modules are built by `_build_segmenter()` in the driver, not by the agent, and the run passes `pe_dict=None`. The latter is already recorded as GFLAG-0190 on MECH-288.
- **Skim:** CONFIRMED and extended.

### V3-EXQ-761 -- MECH-092 quiescent replay

- **The driver's own defence:** its docstring concedes that C4 is "code-structural (the `if e3_quiescent` gate)" at `agent.py:10912`, and rests the case on C1-C3. That defence fails:
  - C1 and C2 are env-dependent occurrence floors: a minimum of 19 quiescent and 2 salient ticks. C2's margin is thin, but these are non-vacuity preconditions, not tests of the claim.
  - C3 is guaranteed, because `replay()` returns a fixed 5 trajectories whenever `theta_buffer` is non-empty.
- **What is genuine:** the run drives the real production path, so it is an honest end-to-end *wiring* check.
- **What is untested:** SWR-equivalence and consolidation.
- **Skim:** CONFIRMED.

### V3-EXQ-762 -- MECH-046 CeA mode prior

- **The formula:** `mode_prior = clip((lf-thr)/cap*cap*gain)` (`cea.py:335-353`). The driver sets the inputs to 0.20 / 0.65 / 0.90 / 1.20 and its docstring predicts 0 / 0.15 / 0.40 / 0.70. The run measured 0.0 / 0.1499 / 0.3999 / 0.6999.
- **New finding:** the load-bearing C046_coordinator_write is the driver's own `salience.update_signal(...)` call (:252), read back from the same dict (:253). `update_signal` is `self._input_signals[name] = float(value)` (`salience_coordinator.py:494`), so the check is a setter round-trip. The production injection site at `agent.py:7991-7993` is not exercised.
- **Skim:** CONFIRMED and extended.

## 3. Claim-layer map

| Claim | Type | Status now | Genuine exp support before -> after | What promoted it |
|---|---|---|---|---|
| SD-017 | design_decision | stable, substrate_ceiling | 691 S, 503a S, 436c W -> 691 S, 436c W | lit (0.903) + 691; 538a ruled liveness vacuous |
| MECH-094 | mechanism | stable, standard | 499 S (UNKNOWN), 633 S -> 499 S | lit, 2026-04-24, before 633 ran |
| MECH-302 | mechanism | provisional, standard | 517c S, 517d S -> **none** | 517d + 517c (decision_log 2026-07-12) |
| SD-050 | design_decision | provisional, standard | 517c S, 517d S -> 517d S | 2026-08-29, implementation-level rationale |
| MECH-288 | mechanism | provisional, standard | 757 S -> **none** | 757 alone (decision_log 2026-07-14) |
| MECH-287 | mechanism | provisional, NO category | 757 S -> **none** | 757 alone (decision_log 2026-07-14) |
| MECH-092 | mechanism | provisional, substrate_conditional | 761 S -> **none** | 761 alone (decision_log 2026-07-15); consolidation half gated on `mech092-replay-consumer-missing` |
| MECH-046 | mechanism | provisional, NO category | 762 S -> **none** | promotion predates 762; 2026-07-15 kept provisional |

The MECH-287 and MECH-288 pre-registered promotion bars named integration tests beyond substrate implementation:

- MECH-287: the V3-EXQ-476 unlock test and a four-arm trigger-vs-accumulator factorial.
- MECH-288: integration into Phase 2 (ii)+(iii)+(iv) plus its falsifiable predictions.

The 2026-07-14 governance decision reinterpreted those bars as the promote-to-*active* gate. Under the original bars, 757 satisfies only the implementation clause. That is why this draft recommends the revert.

**Alternative reading for the user:** keep MECH-092, MECH-287, MECH-288 and MECH-302 at provisional, reading "provisional" as "substrate implemented and verified, plus literature". This is a judgment call, and it is the user's.

## 4. Biological-reference triage

All eight claims have present literature. None of the findings is a translation failure: the tests never reached the mechanism. There is one possible divergence, which remains an open puzzle. Relief dopamine is a phasic *offset* transient (Navratilova 2012), but the SD-050 comparator emits a sustained train of events across the whole healing descent. MECH-288's slow scale is a formal import (BOCPD), and its PE-spike trigger was never driven (GFLAG-0190).

## 5. Four-layer diagnosis (cluster summary; per-target rows are in the JSON)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (not exercised) | For every mechanism claim the claim was never at stake. SD-050 is strengthened at implementation level. |
| Biological reference | clear | All present; SD-050 offset-vs-train is an open puzzle. |
| Prerequisites | present | MECH-092's consolidation half is gated on the missing replay consumer (`mech092-replay-consumer-missing`, per governance_2026_09_01; the older SD-006 citation is stale). |
| Implementation | complete at module level | Two exceptions. MECH-302/SD-050 is partial: the comparator has no refractory. MECH-288 is partial: the PE trigger path was not driven. |
| Environment | n/a or adequate | Mostly synthetic streams with no environment. |
| Measurement | **misleading** | The shared defect: the criteria follow from the code. |
| Integration | isolated or partially coupled | 761 is the only run on the production path. 762's coordinator write bypasses `agent.py`. |
| Scale | n/a | |

**Failure location (GOV-FAILLOC-1):** every target reads MEASURES, with MECH-302/SD-050 reading MIXED MEASURES+MECHANISM(partial). **Not chargeable to REE.** These are PASSes whose evidential weight is withdrawn, not REE failures.

## 6. Cluster pattern

This is **one test-design property, not eight bugs.** In every run the DV is read from the module being switched, and the manipulation is that module's enable flag or its input. That verifies implementation, not mechanism.

Two lineages share the pattern:

- **Substrate-level discriminative pairs:** 503a, 633, 517c/d.
- **"Wall-independent functional signature" confirmers:** 757, 761 and 762, from 2026-07-14/15. The GOV-CONFIRM-1 evidence-confirmer detector surfaced these as "confirmable with built substrate", and their designs turned "substrate built" into scored supports.

Recurrence risk sits with any other GOV-CONFIRM-1 confirmation run. Governance may want that template reviewed. I have not adjudicated it here.

## 7. Learning extracted, repair pathway

- **Measurement gap (all targets).** Each claim names its own discriminating test:
  - MECH-094: tag *provenance* on live replay/DMN writes.
  - MECH-302: relief vs goal-achievement on the *same* downstream readouts.
  - MECH-092: consolidation benefit, gated on `mech092-replay-consumer-missing`.
  - MECH-287/288: the 476 unlock test, the four-arm factorial, and a real-`pe_dict` run.
  - MECH-046: mode/salience shift latency in the closed loop.
- **Implementation gap (secondary, puzzle):** the comparator has no refractory. A draft `amend` on the `MECH-302` substrate_queue entry is included with `severity: degrading` and `user_decision_owed: true`. Drop it if the user reads per-tick firing as intended.
- **Recording/process gap:** 517c was never marked superseded when 517d landed. This is the known `supersedes`-hands-nothing-to-governance failure.
- **Routing:**
  - `governance-demotion`: 517d (MECH-302), 757 and 761.
  - `governance-reclassify`: 500a, 503a, 633, 517c and 762.
  - Follow-on experiments are listed per target under `followon_not_chipped`. **No chips were spawned**: this is staging, and the parent session holds the gate.
- **Re-derive brake:** this autopsy is not a ceiling reading. Every target stamps category `standard` with a `test_design` marker and adds no R3 hit. Existing counts from prior autopsies are SD-017 12, MECH-094 4, MECH-302 3, MECH-092 1, others 0. The live MECH-302 brake means a MECH-302 mechanism test must be a new EXQ number, not another 517 letter.
- **Granularity-debt trigger:** does not fire. No target reads `weakened`, so this is measurement debt.

## 8. Draft evidence_quality_notes

The exact text for each claim is in the JSON, under `targets[].recommended_evidence_quality_note`.

## 9. Step 9b -- hypothesis-space ledger (pending, not written)

`hypothesis_space_ledger_pending.entries = []`. There is no fan-out. None of the 8 runs is a pre-registered leg, and a by-construction PASS discriminates nothing. There is one bears-on note: 503a against `sd017_arc045_mech166_slot_differentiation_sleep` / `H-sleep-differentiates-context-slots`. It is non-discriminating, so that leg stays alive.

## 10. Step 7b -- mechanical pre-routing checks

The first run fired 4 times, all of them C2 ("an existing substrate entry already unblocks this claim"). Every fire was dismissed for routing, since a D1 finding owes no build. Two of them are relevant to follow-on work:

- **MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION** (SD-017, fired on 500a and 503a): a different axis from this finding. Dismissed.
- **mech245 / mech248** (MECH-094): **mech248-retrieval-side-source-attribution-readout** is the natural instrument for the MECH-094 tag-provenance follow-on. Governance should route that follow-on through it.
- **SD-086** (MECH-046): the calibrated z_harm_a scalar readout is a dependency of a closed-loop MECH-046 test.

On the re-run after these dispositions were recorded, there were 0 fires. C5 was inapplicable, since that check is keyed on prose.

## 11. Step 7c -- adversarial red-team (cross-model: **fable**; the draft was written on Opus 5.5)

**Verdict: CONTESTED (narrowly).** Both contested items were accepted and applied, and no status move was overturned.

1. **The absolute "PASS can fail only if the code breaks" was false for the 517c/517d ARM_A leg.** 517c seed 43 failed C1.
   - Confirmer: `jq '.results_arm_a_mech302_on[]|{seed,p1_events,c1_pass}'` on the 517c manifest.
   - Applied: the wording is now "the discriminating contrast holds by construction; the ARM_A floor is an env-dependent liveness leg". MECH-302 now also cites its own D2 clause.
2. **SD-050 `supports` conflicted with SD-050's own `what_would_answer`.**
   - Confirmer: `grep -c "not scheduled injection" claims.yaml` returns 1.
   - Applied: SD-050 is now an explicit user call.

**Numbers the red team recomputed:**

- 517d events per injection: 17.40 / 16.13 / 9.04.
- 500a replay_quality: 8.09995, against a bar that is exactly 6 + 2.
- 503a final slot differentiation: 0.7832 / 0.6141 / 0.3878.
- 633 MI: ln 2 exactly.

**Hygiene fixes applied:**

- The MECH-092 gate is re-cited.
- The beta release is stated as conditional on `is_elevated`.
- SD-050's scoring count is stated as going from 2 to 1.
- 761 C2 is relabelled as a precondition.
- The ratio caveat is added.

**Confirmed by the red team:**

- All four status reverts and all four "stays", checked against the decision log and claims.yaml.
- No `change` tail is already true.
- The per-claim manifest write reaches the field the indexer reads (`build_experiment_indexes.py:3700`).
- The 517c `superseded` write must be explicit, because supersession across experiment types is not automatic.

## 12. What the Step 8 gate (parent session) must decide

1. **The batch SD-versus-mechanism rule** (section 0).
2. **SD-050 direction on 517d:** supports (the default) or non_contributory.
3. **The status reverts** for MECH-092, MECH-287, MECH-288 and MECH-302, against the "provisional = implemented + lit" alternative.
4. **Whether to file the optional comparator-refractory `amend`**, drafted with severity `degrading`.
5. **The read-across for V3-EXQ-499 (MECH-094):** same design, not adjudicated here.
6. **Whether to review the GOV-CONFIRM-1 confirmer design template**, since three of these runs came from it.
