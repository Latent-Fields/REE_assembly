# Failure Autopsy: V3-EXQ-873a (MECH-322 sleep-replay carveout fraction gate)

Generated: `2026-08-07T20:04:51Z`
Status: **confirmed**
Scope: single
Trigger: `experiment_purpose: "diagnostic"` PASS with no confirmed adjudication (2026-08-07 policy).

## 1. Dry-run gate

`scripts/check_dry_run_citations.py v3_exq_873a_mech322_sleep_replay_carveout_fraction_gate_20260804T062309Z_v3` → 0 dry, 1 clean. `elapsed_seconds=14239.12` (~3h57m) across 8 seeds × 3 arms — full-budget arithmetic present throughout.

## 2. Facts

**Run**: queue_id `V3-EXQ-873a`, `experiment_purpose: diagnostic`, `claim_ids: [MECH-322]`, `supersedes: v3_exq_873_mech322_sleep_replay_carveout`, `evidence_direction: supports`, PASS, label `replay_carveout_fires_and_fails_closed`.

**What MECH-322 asserts**: a sleep-phase-gated exception to REE's otherwise-strict rule (MECH-094) that behavioral "chunks" (ARC-071/MECH-323) may only be written from really-executed sequences. During designated sleep (SD-017), a chunk may be written from a *replayed* sequence, but only if three conditions jointly hold: (a) the replayed sequence already carries a top-quartile value-tag from real past executions; (b) it happens during genuine SWS, not waking; (c) the resulting chunk carries a `replay_origin=True` audit flag plus an accelerated corroboration deadline that dissolves it if no real waking re-execution occurs within N episodes. This is REE's analog of overnight procedural-memory consolidation via striatal offline replay (Albouy 2013 human fMRI; Graybiel 1998/2008 and Smith & Graybiel 2013 striatal chunking; Thompson 2026 rodent DLS procedural replay surviving hippocampal lesion) — a narrow, audited relaxation chosen over globally relaxing MECH-094 (2026-05-11 governance decision, R6 Option B).

**Predecessor V3-EXQ-873 (FAIL, `substrate_not_ready_requeue`)**: conflated two different things under one `SEED_PASS_FRACTION=1.0` statistic — (i) STOCHASTIC readiness (does a qualifying high-value candidate naturally emerge by the checkpoint — legitimately random per seed) vs. (ii) DETERMINISTIC AND-gate correctness (given a candidate + sleep + flag ON, does it mint — must succeed on every seed where (i) held). 873's one unlucky seed (303, no candidate, margin −0.157) zeroed the entire arm even though the other 2/3 seeds minted cleanly. 873's own confirmed autopsy (`recommended_epistemic_category: measurement_test_design_defect`) routed exactly the fix 873a implements: decouple the arm-level readiness gate (fraction of seeds clearing readiness, `n_cleared/n_seeds > 0.4` — an adjudicability check) from C1 (mint fraction, scored only over cleared seeds, `= 1.0`), and raise seeds 3→8 for power.

**873a's result**: 7/8 seeds cleared readiness in both chunking-on arms (`ARM_STRICT_FLAG_OFF`, `ARM_REPLAY_ON`; seed 303 again the one non-candidate outlier, correctly excluded from the mint-fraction denominator rather than vetoing the arm). Of the 7 cleared seeds in `ARM_REPLAY_ON`, **all 7 minted correctly** (`c1_mint_fraction=1.0`). Every fail-closed check held across all 8 seeds × 3 arms: `wake_refusal_minted=False` (C2), `low_value_refusal_minted=False` (C3), `ARM_STRICT_FLAG_OFF` (master switch off) minted nothing on any seed regardless of phase or value (C4, flagged safety-critical in the driver), `ARM_OFF` fully inert (C5). C6 (corroboration-deadline trackability) and C7 (audit-counter consistency) also passed.

**Real engineering catch during the fix** (documented in the driver, not in the original task brief): `SerotoninModule` defaults OFF, and when off, `enter_sws_mode()`/`exit_sleep_mode()` are no-ops that leave `.phase` pinned at `"wake"` forever — without an added co-requisite flag (`tonic_5ht_enabled=True`), PROBE 2 would be refused by condition (b) on every seed regardless of the flag under test, misreading as "carve-out never fires" when the real defect would have been "sleep substrate never switched on." Also fixed: reading candidates via `ChunkAccumulator._tally` directly rather than `formation_candidates()`, which had produced a spurious library key-collision refusal unrelated to MECH-322.

**One clean side-finding, not a defect**: all 7 minted replay-origin chunks in `ARM_REPLAY_ON` dissolved by run's end (`corroboration_deadline_fates: {dissolved: 7, still_tracked: 0}`) — none was corroborated by real waking re-execution within the corroboration window (two seeds, 505 and 707, dissolved almost immediately rather than riding the full window). This is the accelerated-dissolution safety valve firing exactly as designed (a replay-origin chunk is provisional until proven), not a MECH-322 defect. It does mean this run has nothing to say about whether a replay-origin chunk *can* survive corroboration in practice — a distinct, still-open question.

**Recording**: always-core fields all present (`recording_schema`, `substrate_hash`, `substrate_commit`, `machine=ree-worker-1`, `machine_class`, `elapsed_seconds`, `config`, `seeds=[101,202,303,404,505,606,707,808]`).

## 3. Claim-layer map

MECH-322 currently has **zero experimental entries** in the claim-evidence scoring index (`genuine_exp_count: 0`) — both the FAIL predecessor (873) and this PASS are absent from the scoring aggregate pending this confirmed autopsy. This is the **first genuine experimental support** for MECH-322 to be applied. The claim's `evidence: []` field in claims.yaml is empty; its `evidence_quality_note` currently ends with 873's `measurement_test_design_defect` verdict and does not yet mention 873a. `depends_on: [ARC-071, MECH-094, SD-017, SD-039, SD-014]` — all built and validated (ARC-071/MECH-323/324 confirmed via V3-EXQ-810a, 8/8 seeds). MECH-322's own `confidence`/`epistemic_category`/`invariant_type` fields are absent from claims.yaml — this is a gap governance should fill once it applies this autopsy (per GOV-CAT-1's own completeness sweep), not something this autopsy corrects directly.

The test let the claim express itself cleanly: the AND-gate's three conditions were each independently exercised (readiness/value, sleep-phase, master-switch), and all three fail-closed branches were probed on every seed. This is exactly the mechanics MECH-322 needed validated.

## 4. Biological-reference triage

**Closest mechanism**: hippocampal-striatal offline replay driving sleep-dependent procedural-memory consolidation. Dedicated literature review exists (`targeted_review_arc_071_composition/`, 10 entries 2026-05-10 through 2026-08-01) — Albouy 2013 (human fMRI, sleep replay motor consolidation), Graybiel 1998/2008 and Smith & Graybiel 2013 (striatal chunking/dual-operator dynamics), Yin & Knowlton 2006 (DLS/DMS habit), Wymbs 2012 (motor-chunking fMRI), Sakai 2003 (visuomotor chunk size), and — most directly relevant, added 2026-08-01, six days before this run — Thompson 2026 (rodent neuropixels: DLS procedural replay persists after hippocampal lesion, causally linked to next-day performance gains). MECH-322 is not a formal-definition import; it is a direct biological translation, and the specific safety machinery it adds (audit flag + accelerated dissolution) is explicitly justified in the claim's own notes as necessary *regardless* of biological fidelity ("biological replay is not an alignment or safety guarantee").

**Biological reference: clear.** No divergence to flag.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened | First genuine experimental support; AND-gate mechanics validated on all three conditions |
| Biological reference | clear | Well-grounded (Albouy 2013, Graybiel striatal-chunking literature, Thompson 2026 DLS replay-after-lesion) |
| Developmental / dependency prerequisites | present | ARC-071/MECH-094/SD-017/SD-039/SD-014 all built and validated (V3-EXQ-810a) |
| Implementation completeness | complete | Fixed instrument correctly separates stochastic readiness from deterministic mint-correctness; safety-critical master-switch catch documented |
| Environment adequacy | adequate | Reuses the validated ARC-071/810a schedule and env |
| Measurement adequacy | adequate | 8 seeds, fraction-based readiness decoupled from mint-correctness — the exact fix 873's autopsy prescribed |
| Integration adequacy | coupled | Exercises MECH-322 through MECH-323/324's real chunk-formation substrate and SD-017's sleep-phase gating together |
| Scale / capacity | adequate for what's tested | 8 seeds sufficient for the fraction-gate statistic; NOT designed to test whether a replay-origin chunk can survive corroboration (a distinct question) |

## 6. Learning extracted

1. **MECH-322's AND-gate mechanics are now validated**: it fires when all three conditions hold (7/7 cleared seeds minted) and fails closed independently on each condition (wake, low-value, master-switch-off — 0 spurious mints across 8 seeds × 3 arms).
2. **The 873→873a instrument fix pattern is confirmed correct**: decoupling stochastic-readiness (arm-level fraction, adjudicability check) from deterministic-correctness (mint fraction over cleared seeds only) is the right general fix for a "one unlucky seed vetoes the arm" defect — 873's own autopsy already cross-referenced this same pattern in V3-EXQ-882 (MECH-472, unrelated claim, same day).
3. **Open follow-up, not blocking**: no minted replay-origin chunk was corroborated by real re-execution within this run's window (7/7 dissolved). Whether a replay-origin chunk *can* survive corroboration in practice is untested by this run and worth a low-priority future characterization probe.

## 7. Repair pathway / routing

- **Recommended `epistemic_category`**: `standard`.
- **Recommended `evidence_direction`**: `supports`.
- **Recommended `recommended_substrate_queue_entry.action`**: `none` — MECH-322's substrate was already built 2026-07-22; no gap identified.
- **Routing**: `queue-experiment` — a future, low-priority, differently-scoped probe (new EXQ number, not a lettered continuation of 873a, since 873a's own question is answered) characterizing whether a replay-origin chunk can survive its corroboration deadline under realistic conditions. Not urgent; MECH-322's fire+fail-closed mechanics do not depend on the answer.
- **Draft `evidence_quality_note` addendum for MECH-322**: *"[2026-08-07 governance: V3-EXQ-873a (confirmed autopsy, failure_autopsy_V3-EXQ-873a_2026-08-07) supports MECH-322 -- first genuine experimental evidence for this claim. Fixed 873's seed-veto instrument defect (decoupled stochastic readiness from deterministic mint-correctness, n=8 seeds). 7/8 seeds cleared readiness; all 7 minted correctly; all fail-closed checks (wake, low-value, master-switch-off) held across 8 seeds x 3 arms. Note: all 7 minted replay-origin chunks dissolved without real-execution corroboration by run's end -- expected safety-valve behavior, not a defect, but leaves 'can a replay-origin chunk survive corroboration' as a distinct open question for a future low-priority probe. evidence_direction: supports.]"*

## 8. User confirmation (Step 8 gate)

User selected: **"Confirm support, but flag corroboration-survival as an open follow-up"** — same PASS/support verdict, with the corroboration-survival question explicitly named as a future low-priority probe rather than left implicit.
