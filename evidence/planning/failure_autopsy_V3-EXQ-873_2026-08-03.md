# Failure Autopsy: V3-EXQ-873 (MECH-322 sleep-replay carve-out AND-gate)

**Generated:** 2026-08-03T10:35:09Z | **Status:** confirmed | **Scope:** single (cross-referenced structural cluster with `failure_autopsy_V3-EXQ-882_2026-08-03.md` -- see Section 5)

## 1. Facts reconstruction

- **Run:** `v3_exq_873_mech322_sleep_replay_carveout_20260802T213319Z_v3`, queue_id `V3-EXQ-873`, `experiment_purpose=diagnostic`, `outcome=FAIL`, `evidence_direction=unknown` (self-routed).
- **Dry-run check:** `check_dry_run_citations.py` on this run_id -> 0 dry, 1 clean. Not a smoke.
- **Recording:** `validate_recording.py` -> OK, always-core complete (recording_schema, substrate_hash, machine/machine_class, elapsed_seconds, config, seeds all present). No recording gap.
- **Self-route label:** `substrate_not_ready_requeue`.
- **Design (3 arms x 3 seeds = 9 cells).** `ARM_OFF` (chunking off, C5 inertness control), `ARM_STRICT_FLAG_OFF` (chunking on, `use_chunk_replay_origin_path=False` -- master-switch control, C4), `ARM_REPLAY_ON` (the carve-out itself, C1/C2/C3/C6/C7). Each `ARM_REPLAY_ON`/`ARM_STRICT_FLAG_OFF` cell runs 3 probes at a single fixed sleep checkpoint episode against ONE real, tracked, not-yet-registered sub-sequence (never an injected/synthetic one, per the driver's documented fix for an earlier `formation_candidates()` key-collision bug):
  - PROBE 1 (condition b, WAKE): attempt with the real high-value sequence while genuinely awake -> MUST refuse.
  - PROBE 2 (conditions a+c, SWS): same sequence, genuinely asleep -> MUST mint a `replay_origin=True` chunk, IF a real qualifying candidate exists.
  - PROBE 3 (condition a, SWS): a distinct sequence with a deliberately-below-threshold value_tag -> MUST refuse.
- **The load-bearing criterion, C1 (`carveout_fires_under_valid_conditions`), is doubly gated:** `c1_arm_green = gate_by_arm[ARM_REPLAY_ON]` (a readiness precondition, `replay_high_value_candidate_available`, evaluated on the **worst of the arm's 3 seeds**) AND `c1_pass = frac(seeds where success_minted and success_minted_replay_origin) >= SEED_PASS_FRACTION` where `SEED_PASS_FRACTION = 1.0` ("deterministic plumbing check, no stochastic slack" -- driver comment).
- **Per-seed readout (`ARM_REPLAY_ON`):**

  | Seed | Candidate available? | Margin above threshold | `success_minted` | `success_minted_replay_origin` |
  |---|---|---|---|---|
  | 101 | Yes | +0.970 | **True** | **True** |
  | 202 | Yes | +0.355 | **True** | **True** |
  | 303 | No | -0.157 | False | False |

  Seed 303's real tracked sub-sequence pool (120 outcomes recorded, same as the other seeds) simply never produced one whose mean crossed `replay_value_threshold()` by the fixed checkpoint episode -- a natural-exploration outcome, not an error.
- **Every other measured behaviour matches spec, in every seed tested:** PROBE 1 wake-refusal held in all `ARM_REPLAY_ON` seeds (C2 pass=true); PROBE 3 low-value refusal held wherever attempted (C3 pass=true); `ARM_STRICT_FLAG_OFF` (master switch off) never minted in any seed regardless of phase or value (C4 pass=true, `chunk_acc_n_replay_formed=0` and `chunk_lib_n_replay_origin=0` throughout); `ARM_OFF` stayed fully inert (C5 pass=true); the corroboration-deadline state was trackable for both minted chunks (C6 pass=true, both later `dissolved` -- a documented fate, not a failure); and the audit counters agreed with the boolean readout on both successful mints (C7 pass=true).
- **Non-degeneracy readiness precondition (`salient_harm_events_fire`) passed** (0.0267 vs 0.01 floor, direction=lower) -- the hazard grid was genuinely exercised, so this is not a vacuous-environment case.
- **Expected vs observed:** expected -- given MECH-323/324 real-execution formation is already confirmed reliable at 8/8 seeds (V3-EXQ-810a), the docstring anticipated the AND-gate's own plumbing (mint under valid conditions, refuse under every invalid one) was the "near-deterministic" open question, with only candidate-availability varying by seed. Observed -- the plumbing answered cleanly and unambiguously wherever it could be exercised (2/2), and correctly did nothing where it could not (1/3, by design, not by defect). The **failed criterion is a readiness precondition** (worst-of-3-seed candidate availability), not a discrimination criterion -- the AND-gate itself was never shown to misbehave in any of the 9 cells run.

## 2. Claim-layer mapping (MECH-322)

- **Text:** "Narrow exception path that permits ARC-071 chunk formation from replayed (hypothesis_tag=True) sequences during designated sleep phase, IF the replayed sequence carries a value-tag from prior real-executed episodes AND the formed chunk carries a `replay_origin=True` audit flag with accelerated dissolution if not corroborated." Resolves the ARC-071 lit-pull R6 governance escalation (Option B carve-out, decided 2026-05-11).
- **Status:** `candidate`, `v3_pending: true`, `implementation_phase: v3`. `registered_utc: 2026-05-11`. Prior evidence: **none** -- this is MECH-322's first-ever experimental test (confirmed independently via the re-derive-brake recipe below, and by the driver's own GOV-REUSE-1 audit: 9 prior manifests carry `chunk_acc_n_replay_formed` but all ran with the flag OFF).
- **Depends on:** ARC-071 (chunking machinery), MECH-094 (the strict gate this is an exception to), SD-017 (sleep phase), SD-039 (anchor goal-payload / value-tag transport), SD-014 (valence-vector recording). All independently confirmed live in this run's own substrate-readiness note (entry point traced end-to-end: `REEAgent.note_chunk_replay_sequence` -> `PolicyChunking.note_replay_sequence` -> `ChunkAccumulator.record_replay_sequence`, reading the real `serotonin.phase`, not a caller override).
- **Did the experiment test the claim under conditions where it could express itself?** Yes, cleanly, in 2 of 3 seeds -- and in the third, the claim's own fail-closed condition (a) is exactly what correctly suppressed the mint. `claim_ids` accuracy: correct, single-claim, first test -- no inherited-tag risk (EXQ-048-style).

## 3. Biological-reference triage

- **Closest mammalian mechanism:** hippocampal-striatal offline replay driving sleep-dependent motor-sequence consolidation (Albouy 2013), striatal chunk formation via dorsolateral-striatum plasticity (Graybiel 1998, 2008; Smith & Graybiel 2013), motor-chunk fMRI signatures (Wymbs 2012), procedural sleep replay (Thompson 2026) -- all catalogued in `evidence/literature/targeted_review_arc_071_composition/` (10 entries, dated 2026-05-10 through 2026-08-01).
- **Is this a faithful biological translation or a formal-definition import?** Biological translation, explicitly. MECH-322 exists *because* the lit-pull found biology does NOT cleanly gate the chunking write path the way ARC-071's original strict pre-registration assumed (hippocampal activity leads ventral striatal replay during sleep consolidation) -- MECH-094's blanket `hypothesis_tag=False` requirement was *more conservative than biology*, and MECH-322 is the registered, audited, narrow relaxation. `lit_status: present` and load-bearing at registration, not something this autopsy needs to commission.
- **Does the failure resemble a missing-dependency signature?** No. Every dependency this run could exercise (real-execution history, sleep-phase detection, value-tag transport, audit-flag propagation, accelerated-dissolution tracking) worked. The one thing that didn't happen -- a real high-value candidate existing at a fixed checkpoint in one particular seed's natural exploration -- is not a missing dependency; it is normal seed-to-seed variance in how quickly a repeated high-value sub-sequence accumulates enough tracked outcomes.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** | The AND-gate mechanism fired correctly under every valid attempt (2/2) and refused correctly under every invalid one (wake, master-switch-off, no-candidate, low-value) across all 9 cells. |
| Biological reference | **clear / present** | Sleep-replay motor consolidation literature is directly on point and was the registration basis for MECH-322 itself (ARC-071 R6). |
| Developmental / dependency prerequisites | **present** | ARC-071, MECH-094, SD-017, SD-039, SD-014 all independently confirmed live; MECH-323/324 formation reliability already established (V3-EXQ-810a, 8/8 seeds). |
| Implementation completeness | **complete** | Entry point traced end-to-end in the driver's own substrate-readiness note; this run is the first to flip the flag and exercise it, and it worked. |
| Environment adequacy | **adequate** | Non-degeneracy precondition (`salient_harm_events_fire`) passed; the hazard grid was genuinely exercised. |
| Measurement adequacy | **under-instrumented / test-design gap** | `SEED_PASS_FRACTION=1.0` and a worst-of-3-seed readiness gate treat "does a real high-value candidate naturally emerge by a fixed checkpoint episode" (stochastic, seed-dependent) as if it had the same certainty as "does the AND-gate mint correctly given one exists" (the actual deterministic plumbing check the criterion is named for). One seed's natural non-emergence zeroes the entire arm gate and buries 2/2 clean confirming cells under a `substrate_not_ready_requeue` label. |
| Integration adequacy | **coupled and stable** | No cross-module instability observed; every safety/fail-closed branch behaved identically to its documented spec. |
| Scale / capacity | **adequate** | 120 tracked outcomes per seed by the checkpoint (same across all seeds); the shortfall in seed 303 is a threshold-margin miss (-0.157), not a starved sample. |

## 5. Cluster pattern (structural property, cross-referenced with V3-EXQ-882)

V3-EXQ-873 (MECH-322) and V3-EXQ-882 (MECH-472) are structurally unrelated claims -- one a policy-chunking sleep-replay AND-gate, the other a held-out-context competence-promotion gate -- autopsied together only because both landed in the same 2026-08-03 pending-review FAIL backlog sweep. They nonetheless share one **failure shape**:

| Target | Claim | Readiness precondition (worst-of-3-seed) | What the clearing seed(s) showed |
|---|---|---|---|
| V3-EXQ-873 | MECH-322 | `replay_high_value_candidate_available`: 2/3 seeds clear, 1/3 (seed 303, margin -0.157) does not | The 2 clearing seeds gave a clean, unambiguous **positive** result (carve-out minted correctly, `replay_origin=True`, in both) |
| V3-EXQ-882 | MECH-472 | in-context survival floor (90 ticks): 1/3 seeds clear (seed 43, at every exposure), 2/3 (seeds 42/45) never do, at any exposure up to 10x budget | The 1 clearing seed solved immediately and stayed solved; the 2 non-clearing seeds showed a stable, non-improving **difficulty split**, itself informative |

**Structural property, not two independent bugs:** in both cases a worst-of-N=3-seed readiness gate is used as a hard pass/fail veto on the run's own load-bearing adjudication, so a single hard or unlucky seed's natural (non-error) outcome zeroes the ENTIRE arm/run's read -- even though the seeds that *did* clear the precondition are themselves fully informative (confirming in 873's case, difficulty-diagnostic in 882's case). This is distinct from the arm-vs-arm vacating defect `experiments/_lib/precondition_gate.py` was built to close (V3-EXQ-785, `failure_autopsy_V3-EXQ-785_2026-07-19.md`): that library fix stops one ARM's structurally-impossible precondition from vacating a DIFFERENT arm's valid result. The pattern here is one level down -- a **within-arm, cross-seed** worst-case reduction (each driver's own local `_worst()`-style helper, computed *before* calling `evaluate_arm_gate`), which the shared library is agnostic to. Both 873 and 882 are among the 55 drivers using `precondition_gate.py`, so this convention is plausibly common across other precondition-gated diagnostics in the corpus, not unique to these two.

**General design lesson (for future precondition-gated diagnostics, not just these two re-queues):** a readiness precondition that depends on natural stochastic variation (an exploration outcome, an environment-difficulty draw) should not be aggregated worst-of-N at small N (here, N=3) as a hard veto. Either raise N enough that requiring all seeds to clear is statistically reasonable, or use a fraction-based pass rule with the precondition-fail rate reported as an informational readiness statistic rather than a hard gate on the load-bearing criterion.

## 6. Learning extracted

- MECH-322's AND-gate (`ChunkAccumulator.record_replay_sequence`) mints correctly under genuine valid conditions and fails closed correctly under every invalid condition tested -- this is now positive-leaning evidence for the mechanism, not a null result.
- The experiment's own test design conflates a stochastic readiness precondition (candidate availability by a fixed episode) with the deterministic criterion it is meant to gate, at `SEED_PASS_FRACTION=1.0` -- this is a **measurement/test-design gap**, not a substrate or claim problem.
- Recording is complete; this is not a recording-debt case.

## 7. Repair pathway

**Diagnosis category (work-graph debt vocabulary):** `complicated (buildable)` -- the fix is a named, well-understood change to the driver's own aggregation logic (no open scientific question).

**Routing:** `/queue-experiment` -- same-question letter, **V3-EXQ-873a**. Fix:
1. Decouple C1's pass/fail from the arm-wide readiness veto: evaluate `success_minted and success_minted_replay_origin` only among the seeds where `replay_high_value_candidate_available` held, rather than requiring 1.0 across all seeds including ones where the precondition was structurally unattemptable.
2. Raise seed count (6-8, matching V3-EXQ-810a's convention) so the gate is not fragile to a single seed's natural exploration variance, and so there is enough N to report a fraction-based pass bar (e.g. `SEED_PASS_FRACTION` applied only to attempted seeds, plus a minimum-attempted-seed-count floor) rather than an all-or-nothing worst-case.
3. Report `replay_high_value_candidate_available` rate as an informational readiness statistic in the manifest rather than a hard veto on the load-bearing criterion.

**Re-derive brake:** does not fire -- 0 prior `substrate_ceiling`/`non_contributory` autopsies tag MECH-322 (verified via the R1-R3 counting recipe against the confirmed-autopsy corpus; this is the first).

**Draft `evidence_quality_note` (for governance to apply, not written here):**

> [2026-08-03 failure autopsy, V3-EXQ-873, confirmed failure_autopsy_V3-EXQ-873_2026-08-03]: FIRST experimental test of MECH-322. The load-bearing criterion (C1) reads FAIL only because a worst-of-3-seed readiness precondition (a real high-value candidate must naturally emerge by a fixed sleep checkpoint) failed in 1/3 seeds; in the other 2/3, the AND-gate minted a `replay_origin=True` chunk exactly as specified, and every fail-closed branch tested (wake-refusal, master-switch-off, low-value, no-candidate) passed cleanly across all 9 cells. This is a test-design defect (an overly strict worst-of-N-seed aggregation conflating a stochastic precondition with a deterministic plumbing check), not a substrate ceiling or claim weakening -- read as evidence_direction=mixed leaning supports pending a corrected re-run. Route: /queue-experiment V3-EXQ-873a with a decoupled, fraction-based readiness gate and 6-8 seeds. No claim-status change; v3_pending stays True pending the corrected re-run.

## 8. Interactive gate (user-confirmed 2026-08-03)

User selected: **"Test-design defect, re-queue with fixed aggregation"** -- `epistemic_category=measurement_test_design_defect`, `evidence_direction` recorded as mixed/inconclusive-leaning-supports with the 2/2 clean positive signal noted explicitly, routed to `/queue-experiment V3-EXQ-873a`. User also confirmed the shared cluster write-up with V3-EXQ-882 (worst-of-N-seed veto structural property).
