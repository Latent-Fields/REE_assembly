# Failure autopsy -- V3-EXQ-861g / V3-EXQ-861h cluster (INV-050 / MECH-180)

**Generated:** 2026-08-23T18:15:21Z
**Scope:** cluster (GOV-FANOUT-1 isolation legs of qid `inv050_mech180_861e_producer_vs_intervention_isolation`)
**Status:** `confirmed` 2026-08-23T18:15:21Z. Step 8 adopted **adopt_hold**: H3 supported as a substrate/machine delta (not substrate-only); CONTROL passes; claims STAND note-only; do **not** confirm H3 in the hypothesis ledger yet; wait for V3-EXQ-861f; no new queue letter; no substrate create.

**Companion:** `failure_autopsy_861g-861h-mech180-cluster_2026-08-23.json`

**Session:** `cursor-autopsy-861gh-20260823`

These two runs are the completed isolation legs the confirmed
`failure_autopsy_V3-EXQ-861e_2026-08-21` commissioned. They are
`experiment_purpose: diagnostic`. Evidence direction is pinned
`non_contributory` by construction. Neither claim's status, confidence, or
`v3_pending` may move on them.

861f (H1, `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation`) is still
**claimed** on `ree-cloud-4` as of 2026-08-23T11:45:10Z. It is not a cluster
member.

---

## 0. Gates run before any metric was read

| Gate | Result |
|---|---|
| Coverage | `check_autopsy_coverage.py` AVAILABLE: YES for 861g/861h. 861e already covered (confirmed). 861f not complete. |
| Contention | `claim_target_sweep.py` AVAILABLE: YES. |
| `check_dry_run_citations.py` | **0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean**. Family `v3_exq_861`: 0 dry / 8 real. Stamp `dry_run_checked: true`, `excluded_dry_run_ids: []`. |
| `validate_recording.py --paths` | **2 complete, 0 always-core gaps.** No run packs. |
| `validate_experiments.py --checks dry_run_unreachable_criterion` | Corpus fires are all `v3_exq_543*`. These drivers silent. Dry-run reduction exists but this autopsy cites full-budget manifests only. |
| Re-derive brake | Does **not** fire. Recommends `standard`, not `substrate_ceiling`. MECH-180=2, INV-050=3 under R1-R3. |
| Granularity-debt trigger | Does **not** fire. See Section 9. |

Both ran to completion (`outcome: FAIL`, no traceback). Not `/diagnose-errors` targets.

---

## 1. Facts

### 1a. V3-EXQ-861g -- H3, algorithm axis, pin `f810969`

`v3_exq_861g_inv050_mech180_h3_substrate_pin_f810969_20260822T175951Z_v3`
FAIL | `experiment_purpose: diagnostic` | `claim_ids: [INV-050, MECH-180]` |
`ree-cloud-2`, `linux-x86_64-py3.10-torch2.12.0+cpu` | 20057 s |
seeds `[7, 271, 883]` | pin `f810969` verified (`authority_spread_ratio` absent) |
`compares_against_run_id`: 861e | `fanout_hypothesis: H3`

**Grid (inherited 861e combination rule).** readiness_ok true (R1 1.0, R2 2/3, R3 1.0).
C1a/C1c pass. C2 1/3 (seed 883 only). Seed 7 not-ready (R2). Seed 271 ready,
factor **1.007** vs C2 margin **1.140** -- HIGH-graded but below noise floor.
Self-route `mel_coupling_below_calibration_noise_floor` -- **refused** (combination-rule leftover; 861e already refused this stamp).

**H3 discrimination (the DV).**

| Cell | substrate | calib_draws | factor | machine |
|---|---|---|---|---|
| 861c recorded | f810969 | 5 | **1.2145974718547234** | ree-cloud-4 |
| 861g n5 control | f810969 (pinned) | 5 | **1.2145974718547234** | ree-cloud-2 |
| 861g n10 primary | f810969 (pinned) | 10 | **1.0070073961703054** | ree-cloud-2 |
| 861e recorded | 17befb8c | 10 | **0.8844596840125855** | ree-worker-1 |

Pin positive control is bit-identical to 861c. Primary stays above 1.0.
`hypothesis_supported: true`. `verdict_label`:
`h3_supported_old_substrate_retains_high_grading_at_n10`.
`calib_draws_alone_moves_readout: false` (both sides stay HIGH-graded by the
`>1.0` bar) even though n5-to-n10 drops factor by **0.208**. That magnitude
is H1-compatible and does **not** meet the driver's "H1 from the other side"
bar (which required n10 collapse below 1.0).

### 1b. V3-EXQ-861h -- CONTROL, representation axis, pin `17befb8c`

`v3_exq_861h_inv050_mech180_contextmemory_write_lock_control_20260822T222844Z_v3`
FAIL | diagnostic | same claims | `ree-cloud-4` | 33562 s |
same seeds | pin `17befb8c` verified | `fanout_hypothesis: CONTROL`

**Grid.** Same leftover: C2 1/3. Seed 271 not-ready (R2) on 17befb8c.
Seed 7 C2 miss (factor 1.017 vs margin 1.141). Seed 883 C2 pass (1.975).
Self-route refused for the same reason.

**CONTROL discrimination (the DV).** Seed 271 ARM_3_HIGH_ON, in-run:

| Variant | factor | insufficient cycles | locked |
|---|---|---|---|
| refractory (k=2) | 0.8844596876005758 | **0 / 6** | false |
| argmin_legacy | 0.8844596840125855 | **6 / 6** | true |

Repair engaged. Factor unchanged (delta 3.6e-9).
`control_passes: true`. `verdict_label`:
`control_PASSES_write_address_lock_not_load_bearing_for_mel`.
Not a fourth frozen hypothesis.

### 1c. z_goal_stream -- non-gating, both legs

861g: ticks 84915, writer_calls 0, writer_defect true.
861h: ticks 53795, writer_calls 0, writer_defect true.
Lineage-wide `DEAD_Z_GOAL_STREAM_EXEMPT`. Scored DVs and measured MEL do not
read z_goal. Not the C2 cause. Not measurement/recording debt on these criteria.

### 1d. Recording

Always-core present on both. `substrate_stable_across_run: true` on both.
Reuse-ineligible (historical pin / pin+write-path). No run packs.

---

## 2. Claim-layer mapping

**INV-050** (invariant, emergent from SD-017): status `candidate`,
`epistemic_category: standard`, `pending_retest_after_substrate: true`,
`live_status.evidence.from` = `failure_autopsy_V3-EXQ-861e_2026-08-21`.
GFLAG-0002 still unresolved.

**MECH-180** (mechanism_hypothesis): status `candidate`, `v3_pending: true`,
`epistemic_category: standard`, `pending_retest_after_substrate: true`.
Same `from` stamp. DV3 still descoped (MECH-122 flag OFF).

Did the experiment test the claims under conditions where they could express
themselves? **No -- by design.** These are instrument-isolation legs. The
drivers pin `evidence_direction` non_contributory and per-claim `unknown`.
Indexer drops `unknown` so it does not vote. Do not treat the grid FAIL as
`weakens`. Out-of-domain trap does not apply (the claims' decisive test is
this ecological MEL-sleep bed; the isolation question is well-posed).

Change strings must **not** end on `-> standard` (already true). Note-only
apply; end on this artifact slug so GOV-APPLY-1 stays ACTIONABLE until
provenance is stamped.

---

## 3. Biological-reference triage

Closest mechanism: homeostatic sleep-pressure regulation scaling SWS
depth/duration with prior waking learning load (process-S analog), plus
novelty-triggered hippocampal replay during SWS (Wilson & McNaughton 1994,
Tononi & Cirelli 2003, Stickgold 2001). Not a formal-definition import.
`lit_status: present` (`targeted_review_inv_050`,
`targeted_review_connectome_mech_180`). No new `/lit-pull`. The isolation
findings do not resemble a missing biological dependency; they isolate a
measurement/substrate-execution confound on one seed's MEL factor.

---

## 4. Four-layer diagnosis

| Layer | 861g (H3) | 861h (CONTROL) |
|---|---|---|
| Claim alignment | unclear -- diagnostic, non-voting | unclear -- diagnostic, non-voting |
| Biological reference | clear; lit present | clear; lit present |
| Prerequisites | present (pin control met) | present (write repair engaged) |
| Implementation | complete for the H3 question (pin verified) | complete for the CONTROL question (refractory fired) |
| Environment | partial -- seed 7 R2-fail; 271 C2-miss; 883 C2-pass | partial -- 271 still R2-fails and stays collapsed on 17befb8c after unlock |
| Measurement | adequate for H3; grid C2 leftover is not this leg's DV | adequate for CONTROL |
| Integration | coupled | coupled |
| Scale | adequate | adequate |

**Failure-location (GOV-FAILLOC-1), both targets:**

- mechanism: `not_established`
- measures: `not_established` (isolation instruments worked; leftover is the inherited grid)
- environment: `partial`
- ree: false
- net: **MIXED, not chargeable to REE**

Demotion gate is not met.

---

## 5. Cluster pattern

| Experiment | Claim | Negative-control / absolute | Discrimination | Read |
|---|---|---|---|---|
| 861g | INV-050 / MECH-180 | C2 pinned_ok 2/3; pin control = 861c 1.2146 | Grid C2 1/3 FAIL; H3 HIGH-graded at n10 **PASS** | H3 supported (substrate/machine). Grid leftover. |
| 861h | INV-050 / MECH-180 | C2 pinned_ok 2/3; write-repair engaged | Grid C2 1/3 FAIL; CONTROL factor unchanged **PASS** | Write-lock not load-bearing for MEL. Grid leftover. |

**One structural property, not two independent bugs.** Both legs inherit
861e's C2 1/3 combination-rule FAIL. Both isolation discriminations are
informative. Remaining required portfolio leg is 861f (H1).

---

## 6. Learning extracted

- H3 declared-null **SUPPORTED**: seed 271 stays HIGH-graded (1.007 > 1.0) at
  n=10 on f810969; 861e's collapse below 1.0 is a substrate/**machine**
  delta (861g `ree-cloud-2` vs 861e `ree-worker-1` vs 861c `ree-cloud-4`).
  Do not ledger-confirm this as substrate-only.
- Pin positive control is bit-identical to 861c (1.2145974718547234).
- n5-to-n10 on the SAME pin still drops factor by 0.208. H1-compatible
  magnitude; does not meet the driver's H1-from-the-other-side bar. Leave
  H1 alive for 861f.
- CONTROL **PASSES**: unlocking ContextMemory writes does not restore HIGH
  grading; factor stays at 861e's 0.884 to 3.6e-9. Repair actually engaged
  (3x6 vs 1x6 slots). Write-lock is not a confound on 861f/861g.
- Self-route `mel_coupling_below_calibration_noise_floor` is again a
  combination-rule leftover.
- Dead z_goal remains lineage-wide, exempted, non-gating.
- Do not restamp `substrate_ceiling`. Do not bump CALIB_DRAWS. Do not
  queue H2 until H1 and H3 have both scored.

**Withdrawn (recorded, not deleted):** treating 1.007 as a clean
substrate-only confirm; rubber-stamping the self-route; treating write-lock
as load-bearing for MEL; treating z_goal writer_defect as the C2 cause.

---

## 7. Routing (user-confirmed)

Node: `complex (probe-gated) / puzzle (known rules)` -- the remaining fact
is H1 (861f already running). Not `complicated (buildable)`.

| Diagnosis | Route |
|---|---|
| H3 / CONTROL isolation | **record**; do not queue another letter of this grid |
| H1 | **wait** -- `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation` claimed on ree-cloud-4 |
| H2 | follow-on only; still aliased until H1+H3 both scored |
| Claims | `non_contributory` / `standard` / status stays `candidate`; note-only |
| Substrate queue | `action: none` (SD-MEL-CONSUMER, SD-MEL-PRODUCER, and `contextmemory-write-path-addressing-degeneracy` already exist; CONTROL discharged the last as not MEL-load-bearing) |
| Lit | none |
| Demotion | no |

**Draft `evidence_quality_note` (governance applies):**

> [2026-08-23 confirmed failure_autopsy_861g-861h-mech180-cluster_2026-08-23] V3-EXQ-861g (H3) and V3-EXQ-861h (CONTROL) are diagnostic isolation legs, non-voting. H3: pin f810969 verified; n5 control bit-identical to 861c factor 1.2145974718547234; n10 factor 1.007 stays HIGH-graded while 861e collapsed to 0.884 on 17befb8c -- H3 SUPPORTED as substrate/machine delta (861g ree-cloud-2 vs 861e ree-worker-1), not substrate-only; not ledger-confirmed pending 861f. CONTROL: refractory repair engaged (0 vs 6 insufficient cycles); factor unchanged at 0.884; write-address lock not load-bearing for MEL. Grid C2 1/3 is combination-rule leftover; do not rubber-stamp self-route. Status, confidence, v3_pending UNCHANGED. GFLAG-0002 remains unresolved. Wait for V3-EXQ-861f.

---

## 8. Re-derive brake

`fired: false`. Recommends `standard`. Counts do not advance.
`refused_requeue: false` in the brake-of-ceiling sense -- but this autopsy
still **refuses a same-grid letter**. The remaining required probe is
already queued.

---

## 9. Granularity-debt

`granularity_debt_cluster.py` before this artifact:

- MECH-180: 10 targets / 9 files; `unclear=5, intact=2, strengthened=2, other=1`. **No `weakened`.**
- INV-050: 9 targets / 9 files; `unclear=5, intact=4`. **No `weakened`.**

This cluster stamps `claim_alignment: unclear` on both targets. Trigger
does **not** fire.

---

## 10. Step 7b / 7c

**7b.** First pass C1 fired (861f driver on disk, not named). Disposed by
naming `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation`. Final
pass: `fire_count` 0. C5 inapplicable (no sibling `.md` at check time).

**7c.** CONTESTED (2), 10 CONFIRMED, 0 REFUTED. F8 (machine confound)
adopted into the hold. F9 (manifest `unknown` vs recommended
`non_contributory`) noted: indexer drops `unknown`; top-level direction is
already `non_contributory`; this skill does not edit manifests.

---

## 11. Step 9b

Existing qid `inv050_mech180_861e_producer_vs_intervention_isolation`.
`growth_restriction`: absent. Mode B, **leave alive**:

- `H-substrate-machine-delta`: record V3-EXQ-861g in `adjudicating_runs` +
  `resolving_runs` with basis; **state stays `alive`** (user hold).
- `H-measurement-rng-confound`: record V3-EXQ-861f in `adjudicating_runs`;
  stay alive.
- CONTROL: not appended (not a fourth frozen hypothesis).
- `decision.distance_phrase` updated: H3 isolation landed, H1 still running.

---

## 12. Read-across (not adjudicated)

- V3-EXQ-861f (H1) -- still claimed.
- H2 follow-on -- do not queue.
- 861d / MECH-122 -- flag OFF; do not amend `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`.
- SD-017 occupancy -- not moved.
- V3-EXQ-943 -- write-address occupancy; 861h does not validate that SD.
- V3-EXQ-910b and V3-EXQ-946 -- other pending diagnostics, different questions.
- V3-EXQ-944a -- ERROR, `/diagnose-errors`.
- GFLAG-0002 -- remains unresolved.

**Chip policy:** this session does not `spawn_task` its own routing follow-on.
Nothing spawned.
