# Failure autopsy (re-read) -- V3-EXQ-942 against ARC-023's narrowed falsifier

- **Generated (UTC):** 2026-09-23T19:55:42Z
- **Scope:** single. Re-adjudication for ARC-023 only (`readjudication_of: failure_autopsy_V3-EXQ-942_2026-08-21`).
- **Status:** confirmed 2026-09-23T20:09:32Z (Step 8: direction `mixed`, note-only, EXP-0548 stays gated with a new reason).
- **Session:** compassionate-greider-803fd7 (chip `chip-20260923-arc023-942-reread`)
- **Trigger:** GFLAG-0406 option A, user ruling 2026-09-23 (REE_assembly `6b0d1cb1dc`). ARC-023's falsifier is now **E3-only realized cadence**.
- **Dry-run gate:** `check_dry_run_citations.py V3-EXQ-942 <run_id>` found 0 dry and 1 clean. This is a full production run on ree-worker-1, substrate commit `f0cb0d59`, with a substrate_hash.
- **Raised:** GFLAG-0443 (the falsifier cannot be tested as written, and ARC-023's note carries a false premise).

## 1. What is and is not re-opened

The 2026-08-21 autopsy stands for INV-013 (non_contributory / derivational / STANDS) and for its C1 persistence reading (taus inverted). This re-read does not touch either. It answers one question: **what does 942's recorded E3 tick count say about ARC-023 as narrowed on 2026-09-23?** That autopsy listed ARC-023 under `read_across_not_adjudicated`, and this artifact is that adjudication.

## 2. The narrowed falsifier (ARC-023 `what_would_answer`, 2026-09-23)

- **CONFIRMING:** E3's realized update count is measurably below the per-step loops' count, **and it tracks its configured period within a pre-registered tolerance**.
- **FALSIFYING:** E3 is not slower than the per-step loops.
- **PARTIAL (named in the claim):** E3 is slowest but departs from its configured share beyond tolerance, "e.g. an ungated reset path forcing extra E3 updates".

## 3. Facts (the manifest's own `per_seed` cells, checked against the code as run at `f0cb0d59`)

| seed | steps | e1_tick | e2_tick (dead flag) | e3_tick | E3 share |
|---|---|---|---|---|---|
| 11 | 3750 | 3750 | 1250 | 572 | 0.153 |
| 23 | 3750 | 3750 | 1250 | 633 | 0.169 |
| 37 | 899 | 899 | 290 | 354 | 0.394 |

**The configured E3 share was a band of 0.05-0.20, not 0.10.** The period was not fixed at 10:

- `_e1_tick` calls `clock.update_e3_rate_from_beta(z_beta)` on every step with no gate (MECH-093; `agent.py:5406` as run).
- Defaults are `beta_rate_min_steps=5`, `beta_rate_max_steps=20` and `beta_magnitude_scale=1.0` (`config.py:2770-2772`).
- The period is therefore `int(20*(1-t) + 5*t)` with `t = clamp(|z_beta|)`.
- The run recorded neither `|z_beta|` nor the per-step period.

The "375/375/90 configured" figure assumes a fixed period of 10 and is **false as run**. It appears in the 2026-08-21 autopsy, in GFLAG-0406, and in ARC-023's own note. The first draft of this artifact inherited it; the Step 7c red-team caught it.

What this means per seed:

- **Seeds 11 and 23** (0.153, 0.169) sit inside the 0.05-0.20 band, so we cannot tell whether they departed from their configured period at all.
- **Seed 37** (0.394) exceeds even the fastest configured period (0.20). At least 0.19 of its ticks per step are reset-driven, because each pending reset adds at most one tick.

Other facts:

- **E1** is per-step (`e1_steps_per_tick=1`).
- **E2** is ungated: `e2_tick` has no consumer in `ree_core` as run.
- **E3 has a live consumer.** `generate_trajectories` returns cached candidates unless `e3_tick` fired.
- **E3 is slower than per-step on every seed.**
- **Reset sources as run.** Two live `phase_reset()` sources fired:
  - the harm trigger, on every owned `harm_signal < 0` step with no onset gate (`agent.py:10015` as run, ~11224 now);
  - the legacy commit-entry trigger, on every fresh variance crossing (`:9107` as run).

  Two did not fire: completion needs `beta_gate_bistable` (default False) and NCL re-assert needs `_ncl_hold_active` (default False). The split between the two live triggers was not recorded, so the seed-37 excess cannot be pinned on the harm trigger alone.
- **`is_committed` never flipping excludes nothing.** `e3_selector.py:4096` nulls `_committed_trajectory` every tick, before the driver reads it.
- **The readout is the clock flag, not realized `_e3_tick` calls.** The two differ by at most one per episode, because `agent.reset()` empties the candidate cache.
- **No tolerance was pre-registered.** The falsifier was written with these numbers in view.

## 4. Adjudication

- **FALSIFYING:** not met on any seed. This leg can only be met at E3 share 1.0, which needs a reset on every step. See §7 and GFLAG-0443.
- **CONFIRMING:** not met. No tolerance was pre-registered, so 942 cannot confirm by construction.
- **PARTIAL cell:** met on seed 37 with certainty (0.394 > 0.20, reset-driven). Undetermined on seeds 11 and 23.

**Direction for ARC-023: `mixed`** (user-confirmed). The case for `weakens` is real: under MECH-093 plus MECH-091, E3's rate is set step by step by arousal and salience, and on seed 37 E3 out-ticks E2's configured 1/3. But the user-accepted falsifier files this shape as partial, and applying `weakens` would re-open GFLAG-0406. The run is diagnostic (`scoring_excluded`) and the read is post-hoc, so this is a registry record and moves no confidence.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Confirming leg needs a pre-registered tolerance; falsifying leg not met and reachable only at share 1.0. |
| Biological reference | partial | Slow deliberative loop in thalamo-cortico-BG circuits; arousal-modulated rhythm and salience phase reset are biologically real, but a reset triggers on onset and is refractory, not per-sample. Lit: `targeted_review_connectome_arc_023`. |
| Prerequisites | present | SD-006 phase-1 clock; MECH-091 and MECH-093 wired. |
| Implementation | complete (clock), two live cadence modulators | MECH-093 arousal period (5-20); MECH-091 harm reset with no onset gate, unlike the transition-gated commitment-entry site. |
| Environment | adequate | Hazard density varies by seed; seed 37 dies at ~36 steps/episode. |
| Measurement | under-instrumented | Flag not invocation; no per-step period, `|z_beta|` or reset-by-trigger record; no pre-registered tolerance. |
| Integration | coupled | `e3_tick` gates candidate regeneration. |
| Scale | adequate | 3750 / 3750 / 899 steps. |

**Failure-location (GOV-FAILLOC-1):** MIXED (MECHANISM partial + MEASURES partial). This is not chargeable to REE.

## 6. Recurrence

- **Granularity-debt trigger: does not fire.** `granularity_debt_cluster.py ARC-023` found 0 tagging targets, and this target reads `unclear`, not `weakened`.
- **Re-derive brake: does not fire.** Category `standard` and direction `mixed` do not count under R3.
- **Step 9b: skipped.** `e-ladder-realised-timescale-separation` asks about persistence half-lives, not E3 cadence. This re-read adjudicates no pre-registered leg and emits no fan-out.

## 7. Routing (confirmed): `governance-note-only`

**ARC-023:**
- Direction `mixed`. Category `standard` (unchanged). Status stays `candidate`. `pending_retest_after_substrate: false`.
- **Note-only:** 942's manifest is untouched.
- Governance writes the JSON `recommended_evidence_quality_note`, which also **corrects the 375/375/90 premise** in ARC-023's existing note, and stamps live_status from this artifact.
- **`diagnostic_evidence_adjudicated` is deliberately NOT set.** It would stop the indexer re-minting an experimental proposal once the falsifier is tightened.

**EXP-0548: STAYS GATED, with its gating_reason REPLACED** (user-confirmed).
- The old v3_exq_131 freeze-artifact reason is resolved, because the narrowing bars that readout.
- The new reason is that the narrowed falsifier cannot be tested discriminatingly as written:
  - its FALSIFYING leg is reachable only at E3 share 1.0;
  - its "configured period" is arousal-modulated by MECH-093.
- Proposed gating_reason text is in the JSON `exp_0548_disposition.proposed_gating_reason_text`.
- Do NOT set the status back to `proposed`: this proposal is auto-generated, and the indexer carries forward only non-`proposed` status.
- Design notes for when the falsifier is tightened:
  - record the per-step period, `|z_beta|`, realized `_e3_tick` calls and resets by trigger;
  - pin or model MECH-093;
  - pre-register a tolerance;
  - replace the share-1.0 FALSIFY leg with a reachable one.
- Work-graph node until GFLAG-0443 is decided: `complex (probe-gated) / mystery (known data)`. More runs do not help while the falsifying leg is unreachable.

**Substrate:** `action: none`.

**GFLAG-0443** (raised and pushed this session, REE_assembly `ece3a27ed1`): tighten ARC-023's narrowed falsifier, and correct the false 375/375/90 premise. `/governance` owns it. This autopsy spawns no chip.

### Read-across, not adjudicated
- **MECH-091:** the harm trigger has no onset gate, while the commitment-entry trigger does. Its V3-EXQ-944b PASS ran with the ungated trigger.
- **MECH-093:** the arousal-driven E3 period is live and unconditional by default. Any "characteristic rate" reading of E3 must state the `|z_beta|` regime.
- **SD-006:** unchanged. Its R4 rejection of tick counts as a representational readout stands.
- **INV-013 / the C1 persistence reading:** untouched. **ARC-148:** untouched.

## 8. Learning extracted
1. A falsifier written after a run's numbers are known cannot be scored by that run. 942 lands in the partial cell the falsifier was written to hold it.
2. Re-measure a "configured" baseline against the code as run. Three artifacts carried 375/375/90 while MECH-093 made the configured E3 share a 0.05-0.20 band.
3. A falsifier whose falsifying leg needs a saturated regime (share 1.0) is not a test. Catch that when the falsifier is written.
4. A tick-count readout needs the per-step period, `|z_beta|` and resets by trigger recorded beside it (recording gap, Experimental Recording Standard §3c).

## 9. Step 7b / 7c / 8
- **7b:** `autopsy_pre_routing_checks.py` gave fire_count 0. C5 was inapplicable (no sibling .md at run time) and C7 was inapplicable (no arm-structured results), which is not an all-clear on those checks. On re-run over the final artifact with this .md present, fire_count was still 0 (C5 now applicable and silent; C6 and C7 inapplicable).
- **7c:** a **cross-model** pass (Fable; this session runs on Opus) returned **CONTESTED** with four defects, all verified in source and accepted:
  - A1: the configured share is a MECH-093 band, not 0.10.
  - A2: the harm attribution is unshown; commit-entry resets are live; `is_committed` is uninformative.
  - A3: `diagnostic_evidence_adjudicated` plus un-gating would cancel in the indexer, so the flag was dropped.
  - A4: the re-scoped design cannot discriminate, and the falsifier's FALSIFY leg is unreachable (now GFLAG-0443).

  The direction `mixed` survived.
- **8:** the user confirmed direction `mixed` (rec-20260923-fed93dfb), note-only (rec-20260923-e4e99a5d), and EXP-0548 staying gated with a new reason (rec-20260923-e532e1b3).
