# Failure autopsy: V3-EXQ-1087 (MECH-321 per-leaf harm discriminability, diagnostic PASS)

- Run: `v3_exq_1087_mech321_perleaf_harm_discriminability_20260924T121217Z_v3` (ree-worker-3, 3070 s)
- Generated: 2026-09-25T01:41:50Z, session orchc0925-autopsyB-1087 (orchestrate-20260924-1707)
- Status: **confirmed** under the user's standing delegation via orchestrate-20260924-1707. All readiness preconditions are met.
- **Provenance of the deciding branch (red-team F1, accepted). Governance must ratify this at Step 2b.** 'T <= 0.20 and not harm-tracking -> 919 non_contributory' was pre-registered in the DRIVER at queue time: orchestrate-20260924 pre-flight CHANGE 3, red-team F1/F2, orchestrator decision Q-1087 = A. It REFINES the user-ratified two-branch rule of 2026-09-23/24 (rec-20260924-b52804ea: high tie rate -> non_contributory; low tie rate -> the conditional weakens becomes unconditional). Under that literal rule T = 0.078 satisfies the condition. Even then, Option A and the open GFLAG-0462 (919's DV is 87% post-death) would leave 919 at best 'conditional stands', never unconditional. The refinement was fixed before data. It closes a premise the ratified rule left implicit: that a discriminative input is a harm-informed one. This run measures that premise false.
- Indexer adjudication: `vacuous_pass`. Verdict: **false flag** (section 2).
- Chip: chip-autopsy-v3-exq-1087.

## 1. Facts

**Dry-run gate.** `check_dry_run_citations.py` over the 1087 run, the v3_exq_1087 family and the re-adjudicated 919 run: 0 dry, 3 clean. `validate_recording.py`: always-core complete. `substrate_stable_across_run: false` is process-snapshot drift. All cells share hash d6e55b77. The stamped commit ea8ea74f does not describe that hash, so the commit mapping is recording debt, but the run executed one substrate.

**What the run is.** This is the successor that failure_autopsy_MECH-320-defect-cluster_2026-09-23 required before V3-EXQ-919's `weakens` on MECH-321 could be read unconditionally. It replays 919's untrained ARM_SELECTION_ON regime: seeds 11/23/47/71/3, 12 ep x 60 steps, HAZARD_TUNED overlay, config asserted equal to 919's `_arm_flags`. An instance wrapper on `select_harm_aware_leaves` records every Stage-2 call. The ground truth for each leaf comes from executing its own action sequence on a deep-copied env, with RNG saved and restored. A probe-OFF control replicate of seed 11 matched the probe-ON actions exactly (mismatch 0).

**Pre-registered criteria and results (pre-done, Stage-2-active, >= 2 leaves):**

| Readout | Value | Threshold / reading |
|---|---|---|
| C1 tolerance-tie rate T (load-bearing) | **0.0782** (19/243), exact-tie 0 | <= 0.20 -> discriminative |
| C2 harm-tracking excess vs chance | **-0.070**, z **-2.23**, n=223 | <= -0.05 and z <= -2 -> anti-tracking |
| C2 excess vs best-constant-index null | -0.197 (null 0.511) | tracking needs >= +0.05 |
| marginal-preserving permutation null (red-team recompute) | z -2.76, p 0.0026 | survives the non-uniform chosen index |
| per-seed hit vs chance (red-team) | 11: .367/.388, 23: .394/.394, **47: .171/.333, 71: .179/.363**, 3: .460/.433 | anti carried by 2/5 seeds; no seed tracks |
| per-unit Spearman(penalty, GT key) | median -0.5, mean -0.10 (129 neg / 11 zero / 102 pos, n=242) | positive if the penalty tracked harm |
| P(chosen idx 0) | 0.144 vs chance 0.333 | chosen index is non-uniform |
| Stage-1 clamp saturation (R3) | 0.992 | label qualifier |
| Kept-leaf first action executed (R5) | 0.292 (discarded leaf: 0.163) | reported |
| 919 post-death harm share (R4) | 0.867 | Option A gate (< 0.5 needed for "unconditional") |
| Post-done calls (excluded, descriptive) | excess -0.278, z -18.3, n=958 | not used |

Label: `stage2_discriminative_anti_harm_tracking__stage1_clamp_saturated`. The driver's own recommendation is `recommended_readjudication_of_919 = non_contributory`.

**Expected vs observed.** The two anticipated outcomes were a high tie rate (harm-blind) or a low tie rate with harm tracking. What came back is a third outcome, pre-registered from the AMBER pre-flight: the leaves are clearly separated by the harm penalty, but the separation does not track realised harm. If anything it runs against it.

## 2. The vacuous_pass flag is a false flag

`build_experiment_indexes.py` check (3b) fires on any load_bearing:true criterion with passed:false under an overall PASS. Here that criterion is C2. In this driver C2 is a **partition selector**: tracking, anti and neither each pick a 919 re-adjudication branch, and `passed:false` selects the non_contributory branch. It does not leave a gate cleared on nothing. The gate proper is C1. C1 is decisive (0.078, far from both the 0.20 and 0.50 cut-points), non-degenerate (n=243 vs floor 30), and `criteria_non_degenerate` is true for both criteria. Driver-side fix, cosmetic and not retro-applied: tag C2 `role: "selector"`.

Indexer side note: claim_evidence.v1.json reads this diagnostic's PASS as `supports` at 0.75 for MECH-321. `scoring_excluded: diagnostic_probe` keeps that out of confidence, but the direction shown in conflicts.md is wrong. The recommended direction for 1087's own manifest is `non_contributory`.

## 3. Claim layer

MECH-321 (candidate, v3_pending, epistemic_category standard, pending_retest_after_substrate true) is about policy decomposition via the event segmenter. Harm-aware leaf selection is its downstream task-effect leg, built as SD-hazard-aware-policy-decomposition. The only experimental `weakens` readings on that leg were 844 (a competence_implementation_gap) and 919. The 919 reading was already stamped CONDITIONAL on the harm input being discriminative (2026-09-23 note, applied 2026-09-24).

1087 answers that condition. The input IS discriminative, and it is NOT harm-informed: pooled below chance (z -2.23; permutation z -2.76), carried by seeds 47 and 71, with no harm tracking on any seed. So 919 did not test "harm-aware selection reduces harm". It tested "selection by a per-leaf number that anti-correlates with harm does not reduce harm", and that says nothing about MECH-321. By the driver's pre-registered refinement, 919 moves **weakens -> non_contributory** (see the provenance note above: under the literal ratified rule, a low tie rate would have satisfied the condition).

A separate route leads to the same place. 919's DV is 87% post-death harm (GFLAG-0462), which by Option A would at best have left the reading conditional.

## 4. Biological reference

Threat-imminence-gated defensive path selection comes from the commissioned lit-pull targeted_review_threat_modulated_defensive_path_selection: Fanselow PIC, Mobbs 2007 vmPFC->PAG categorical shift, and Evans/Branco 2018 synaptic-threshold escape. In the animal, both the graded bias and the categorical override read a *learned*, outcome-grounded threat estimate for each candidate path. REE copies the structure but feeds it two things instead:

- an untrained E2 rollout. 919 and the replay are untrained, E2's world head has no waking objective (GFLAG-0485), and ree_core does no waking gradient learning at defaults (GFLAG-0491);
- a residue harm channel written from `z_harm.norm()` on every tick through an untrained HarmEncoder. It can act as an occupancy map (driver CHANGE 3).

In biology, removing the learned threat map would produce exactly this: selection that is active and consistent but not protective. So the FAIL points to a missing prerequisite, not to falsification. Not a formal import; lit present.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (1087) / unclear (919 leg) | 919 did not test harm-aware selection with a harm-informed input |
| Biological reference | partial | structure faithful; the learned per-path threat estimate is absent |
| Prerequisites | missing | trained E2 world head (GFLAG-0485/0491); harm-event-grounded valence |
| Implementation | **partial** | inert-by-defect on the harm input. `_decomposition_harm_penalty` (hippocampal/module.py:1128-1153, unchanged since 919 per `git log -L`) averages valence over ALL rollout_horizon predicted states of a single-primitive leaf. rollout_horizon is 30, so 29 of the 30 averaged states follow zero-action padding (red-team F6). The drift is measured in this run: the median end/mean pairwise predicted-state distance is 4.74. The contrast therefore comes mostly from action-uninformative drift, the GFLAG-0485 shape. Stage-1 harm_bias sits at its clamp on 99.2% of leaves (valence_bounding_enabled default False), which is a neutralising default. |
| Environment | adequate | 919 overlay reproduced; GT separates the leaves on 223/243 units |
| Measurement | adequate | C1 decisive. The C2 anti reading survives a marginal-preserving permutation null (z -2.76), so it does not depend on the misspecified chance null. Limit: the pooled signal comes from 2/5 seeds. Anti and neither route identically. |
| Integration | partially coupled | the kept leaf's first action was executed on 29% of units (vs 16% for a discarded leaf); the input is coupled but not harm-informed |
| Scale | adequate | 243/223 units vs floors of 30 |

**Failure-location (GOV-FAILLOC-1):** MECHANISM, with implementation partial because the harm input is not harm-informed. Measures and environment are adequate. **Not chargeable to REE.** The 919 negative is re-read as a wiring/prerequisite gap.

**Replay fidelity caveat.** The per-seed elementwise action match to 919 is 0.53-0.99. That is expected: ree_core has moved since 2026-08-11, and torch.multinomial differs across machine classes. The penalty function itself has not changed since 919. Every structural cause named above was present in 919's substrate: the zero-action padding, the clamp with bounding off, the per-tick z_harm-norm write, and the untrained agent.

## 6. Learning extracted

- **Existing dependency strengthened:** harm-aware path selection needs a harm-informed per-candidate threat estimate. A discriminative but untrained estimate produces selection that looks engaged (98% firing, low tie rate) and tracks realised harm on no seed. Pooled, it runs below chance (2/5 seeds).
- **Implementation gap:** the per-leaf penalty's horizon is mostly zero-action padding.
- **Implementation gap:** Stage-1 is a constant offset (clamp-saturated).
- **Integration gap:** the Stage-2 kept leaf decides the executed action on only 29% of units.
- **Tooling:** a load_bearing partition-selector criterion needs `role: "selector"`, or the indexer raises a false `vacuous_pass`.
- Candidate mechanism for the *anti* direction (hypothesis, not established): if the harm channel accumulates z_harm norm at visited cells, leaves toward already-visited (survived) cells score worse and leaves toward novel, possibly hazardous cells score better.

## 7. Repair pathway and routing

Node class: `complicated (buildable)` for the input fix (penalty horizon, valence bounding, harm-event-grounded write). The trained-E2 prerequisite belongs to the governance-owned native waking-trainer row (GFLAG-0491).

**Routing: implement-substrate.** Amend SD-hazard-aware-policy-decomposition:
- add the 1087 failure item;
- mark the 919 item **superseded**;
- set severity **corrupting**. The selection passes every "engaged" readiness check while its input does not track harm, so evidence reading it as harm-informed looks valid and is not. Blast radius: runs with `decomposition_use_harm_aware_selection=True` (default-off);
- set substrate_paths to `hippocampal/module.py::_decomposition_harm_penalty` and `policy/policy_decomposition.py::harm_bias`, `::select_harm_aware_leaves`.

This supersedes the 2026-08-13 amend's order of work: escapability or predictability channels added onto a non-harm-informed penalty would not be testable.

**Re-derive brake: FIRES.** MECH-321 already had 2 counting hits (867, 938). This non_contributory target, which owes an amend, is the 3rd. **REFUSE** any same-claim harm-aware-selection task-harm re-test (a 919 letter, a 1087 letter, or a new-number MECH-321 task-harm test) until the per-leaf harm input is harm-informed. Exempt: a trained-agent diagnostic of the penalty input itself, or a different-mechanism test.

**Granularity-debt trigger: does not fire.** `granularity_debt_cluster.py MECH-321` finds 10 targets: weakened=4 (844 x2, 919 x2), intact=2, other=2, unclear=2. After this re-adjudication, 919 reads unclear. The only remaining weakened reading is 844, and 844 is itself a competence_implementation_gap. The lineage circles one downstream leg with implementation and measurement defects. It is not a set of structurally different failures of MECH-321.

**Draft evidence_quality_note (MECH-321, append):** see the JSON `recommended_evidence_quality_note` (exact text).

**Governance applies (not this skill), after ratifying the refinement named in the header:**
1. V3-EXQ-919 manifest evidence_direction weakens -> non_contributory.
2. V3-EXQ-1087 evidence_direction -> non_contributory.
3. The MECH-321 note plus `diagnostic_evidence_adjudicated`, and stamp live_status.evidence.from with this artifact.
4. The substrate amend above.
5. Resolve GFLAG-0462: the 919 re-adjudication it asked for is delivered here.
6. The `hypothesis_space_ledger_pending` block: qid `mech321_harm_aware_selection_task_effect`, leg H-harm-aware-reduces-task-harm, eliminated -> **alive**, because its only decisive run no longer meets the elimination bar.

Step 9b was not written directly. `hypothesis_space_registry.v1.json` is claimed by the parallel autopsy session orchc0925-autopsyA-1083, and the ledger should move in step with the 919 direction change that governance applies.

**Follow-on not chipped** (autopsy rule). After ratification, governance chips `/implement-substrate` for the amend.

## 8. Step 7b / 7c

- 7b: 0 fires; C5 and C7 inapplicable (C5 ran before this .md existed; C7: single-arm run).
- 7c: fable, CONTESTED, 3 findings accepted (section 9).

## 9. Red-team (7c)

Model: **fable** (cross-model; this session runs Opus 5.5). Verdict: **CONTESTED**, with the routing judged defensible. Every load-bearing number was recomputed from raw `stage2_events` and reproduces exactly: T 0.07819 (19/243); C2 excess -0.07025, z -2.2255; constant null 0.51121 (idx 2); Stage-1 saturation 0.99177; kept-leaf 0.29218. `git log -L` confirms the penalty function is unchanged since a4a1b1d (2026-08-01). The brake count of 2 (867, 938) reproduces.

- **F1 (CONTESTED, accepted):** the deciding branch is a driver-level refinement (CHANGE 3; orchestrator Q-1087), not the user-ratified two-branch rule. Under the ratified rule, T = 0.078 would satisfy the condition. Confirmer: `sed -n 158,161p failure_autopsy_MECH-320-defect-cluster_2026-09-23.md`; `grep -n "CHANGE 3"` in the driver. Disposition: provenance corrected in the header, JSON confirmation_note and evidence note; the departure is disclosed for governance Step 2b; routing kept. Why it is kept: the refinement was fixed before data; the premise the ratified rule relied on (discriminative means harm-informed) is measured false; and GFLAG-0462 independently bars an unconditional reading.
- **F2 (in the artifact's favour, accepted):** the anti reading survives a marginal-preserving permutation null (z -2.76, p 0.0026). The "fragile" wording is removed.
- **F3 (accepted):** the pooled anti signal is carried by 2 of 5 seeds; there is no harm tracking on any seed; the Spearman distribution is bimodal. Wording narrowed.
- **Hygiene (applied):** blast radius stated; in-run drift ratio cited. The indexer DOES read `role: "selector"` (build_experiment_indexes.py ~675-693, verified). The 1-step GT here is not the GT a trained-E2 re-test would use.
- **Attacks that failed:** vacuous_pass false flag; zero-action padding; sign convention (-0.5 means anti); replay fidelity (the re-adjudication rests on structural facts present in 919's substrate); brake fires; severity corrupting; 919 failure item superseded; ledger eliminated -> alive.

Record: `.scratch/orch-20260924-1707/autopsy/redteam_1087.md` (scratch, not committed).
