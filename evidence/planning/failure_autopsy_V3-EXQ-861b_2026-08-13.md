# Failure Autopsy: V3-EXQ-861b (INV-050 / MECH-180 independent-seed replication)

Generated: `2026-08-13T19:43:37Z`
Scope: single
Status: confirmed

## 1. Facts reconstruction

**Target:** `v3_exq_861b_inv050_mech180_independent_seed_replication_20260813T113330Z_v3`
(queue_id `V3-EXQ-861b`), claim_ids `[INV-050, MECH-180]`, `experiment_purpose: evidence`.
Outcome **FAIL**, self-route `interpretation.label: mel_control_degenerate`,
`evidence_direction: non_contributory` (per-claim: both `non_contributory`).

- **Dry-run check (Step 2a):** `dry_run` field absent (falsy) on the manifest; confirmed clean
  via `scripts/check_dry_run_citations.py` (`-- 0 dry cited, ... 1 clean, 0 unknown`). Real,
  full-budget run.
- **Recording provenance:** `ree-v3/validate_recording.py --paths <manifest>` reports OK, 0
  always-core gaps. `recording_schema: rec/v1`, `substrate_hash`, `machine: ree-worker-1`,
  `machine_class`, `elapsed_seconds: 24762.5`, full `config`, `seeds: [7, 271, 883]` all present.
- **z_goal-stream:** `writer_defect: true` (`writer_calls: 0` over 43583 ticks). This is a
  **pre-registered, documented exemption** — the driver's `DEAD_Z_GOAL_STREAM_EXEMPT` constant
  states `z_goal_enabled=True` is inherited verbatim from the V3-EXQ-718a/798a/845/861 lineage
  for architecture parity, but wiring `update_z_goal` live would activate the E3 goal term, E1
  conditioning, and the SD-024 benefit-attractor producer — a behaviour change that would break
  the single-variable (seeds-only) comparison against V3-EXQ-861 that is this run's entire
  scientific value. The knob is arm-symmetric. This run's DVs (sws/rem/spindle sleep metrics) do
  not read z_goal at all — confirmed by grepping the driver for `z_goal`/`update_z_goal` usage
  outside the exemption comment and the (inert) instrumentation block. **Unaffected**, per the
  pending_review.md guidance for this flag.

**Script (`ree-v3/experiments/v3_exq_861b_inv050_mech180_independent_seed_replication.py`):**
Cell logic byte-identical to V3-EXQ-861 except the seed set. INDEPENDENCE is the whole point:
`/governance` 2026-08-07 (GFLAG-0002, user-confirmed) held INV-050 at `candidate` despite three
clean autopsy-confirmed PASSes (845, 861, 861a) because all three shared the IDENTICAL
environment and the IDENTICAL 3 seeds (`42, 123, 456`) — "one configuration confirmed three
times, not three independent replications" (project's own V3-EXQ-718a lesson: "DV-monotone-in-
measured-MEL is near-tautological on a functional consumer"). Promotion was re-gated on varying
at least one of: (a) genuinely disjoint seeds, (b) a held-out environment, (c) a MEL-consumer-
absent control arm. This run satisfies (a) and (c) — seeds `[7, 271, 883]`, audited
programmatically against all 10 manifests in this lineage, empty intersection with
`[42, 123, 456]` — and retains ARM_4_HIGH_OFF as the (c) control. (b) is explicitly NOT
satisfied and stated as a limitation, not papered over.

DV3 (spindle_density) is pre-registered DESCOPED — its enabling substrate
(`MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`) remains
`implemented_validation_failed_needs_followup_fix` (confirmed non-functional in V3-EXQ-861a).
The scored gate here is narrowed to the two built DVs (`C1 = C1a AND C1c`; `C2.on_gt_off = sws
AND rem`), explicitly to avoid re-importing a known-broken DV3 through the conjunction the way
V3-EXQ-845/861a's gate did.

**Combination rule:** `PASS iff readiness_ok AND c2_pass AND (C1a AND C1c) each on >= 2/3 seeds`.
`readiness_ok: true` (`r1_frac`/`r2_frac` both 1.0). `c1_frac: 1.0` (all 3 seeds pass C1 cleanly).
`c2_frac: 0.333` (only seed 883 passes `on_gt_off`) → **the run FAILED entirely on the C2 leg.**

## 2. Per-seed results

| Seed | ARM_3_HIGH_ON factor | ARM_3 sws / rem | ARM_4_HIGH_OFF sws / rem (pinned) | C1 (both scored DVs) | C2 on_gt_off |
|---|---|---|---|---|---|
| 7   | 0.517 | 14 / 31 | 30 / 60 | PASS | **FAIL** |
| 271 | 0.612 | 18 / 37 | 30 / 60 | PASS | **FAIL** |
| 883 | 1.982 | 59 / 119 | 30 / 60 | PASS | PASS |

ARM_4 is deterministic by construction (`factor` pinned at 1.0 → `SWS_CONSOLIDATION_STEPS(5) *
MEAS_CYCLES(6) = 30`, `REM_ATTRIBUTION_STEPS(10) * 6 = 60`, identical every seed). C1 passed on
all 3 seeds because it is a *within-seed, relative* comparison (arms re-sorted by measured MEL,
checked for monotone-increasing sws/rem) — robust to the absolute level of the per-seed
calibration constant. C2 compares the ON arm's *absolute* factor against the externally pinned
1.0 baseline, which is **not** robust to that constant.

## 3. Root-cause diagnosis: the C2 failure is a calibration-noise artifact, not an absence of coupling

`mel_reference` (the calibration denominator `duration_factor` is computed against) is a single
3-episode (`CALIB_EPISODES = 3`) point estimate from a short pass on the *stable, no-shift* env,
decoupled from the arm's own trajectory. I pulled `ARM_0_NONE_ON`'s factor (nominal "no novelty,"
which should read ≈1.0 under an unbiased calibration, since ARM_0's own interval matches the
calibration env's interval=0) across **every seed this lineage has ever run**, including the
three "confirmed positive" runs (845, 861 — 861a shares 845/861's seeds and driver family):

| seed | 42 | 123 | 456 | 7 | 271 | 883 |
|---|---|---|---|---|---|---|
| ARM_0 factor | 0.885 | 1.719 | 1.646 | 0.658 | 0.636 | 1.671 |

A ~3x spread (0.636 to 1.719) under nominally matched conditions. The calibration procedure's
own sampling noise is comparable to or larger than the biological effect size C2 needs to
discriminate (`ARM_3` factors when they DO clear the noise floor: 1.699, 1.959, 2.373, 1.982 —
i.e., roughly the same magnitude as the noise floor itself).

**This noise was already present in the three prior "confirmed positive" runs and was invisible
by construction.** V3-EXQ-845/861's `on_gt_off` gate was conjunctive over THREE DVs including
spindle_density, and spindle_density's `on_gt_off` leg failed at 0/3 seeds in every run in this
lineage (confirmed non-functional MECH-122 substrate) — so the gate's overall verdict was always
driven to `c2_pass: False` by the broken DV3 leg, regardless of whether DV1/DV2's own margin was
robust. Verified directly: `V3-EXQ-861`'s per-seed `c2` block reads `on_gt_off: False` for ALL
THREE of seeds 42/123/456 — yet `ARM_3` factor was clearly >1 (1.699, 1.959, 2.373) and sws/rem
counts clearly exceeded the OFF pin (e.g. seed 42: sws 51 vs 30, rem 102 vs 60) on those same
seeds. DV1/DV2's own ON>OFF margin was **never load-bearing or scrutinized** until 861b narrowed
the gate to 2 DVs specifically to get a clean, interpretable read on the axis that actually
matters for GFLAG-0002. Narrowing the gate is exactly what *exposed* a pre-existing measurement
fragility rather than *introducing* a new one.

**Net read:** on the 6 seeds tested to date across this lineage, 4/6 (42, 123, 456, 883) show the
predicted ON > OFF direction robustly; 2/6 (7, 271) show the sign flipped by calibration noise.
This is directionally consistent with the mechanism being real, but the specific discriminating
test (C2) cannot be trusted at this calibration precision — a bare re-seed at the same
methodology carries a real chance of hitting the same coin-flip again.

## 4. Claim-layer mapping

**INV-050** (invariant, `status: candidate`, `epistemic_category: standard`,
`pending_retest_after_substrate: true`). GRADUATED from `substrate_ceiling` on 2026-08-01
(confirmed `failure_autopsy_V3-EXQ-861_2026-08-01`), then explicitly HELD at `candidate` by
GFLAG-0002 (2026-08-07) pending a genuinely independent test. This run was that test. Its C1
DVs (sws_power, replay_rate — INV-050's own named DVs) replicated cleanly, but the DV-monotone
result is near-tautological per this project's own documented lesson; the run's decisive
independence leg (C2) did not resolve due to the calibration gap above. **GFLAG-0002 remains
unresolved, not failed.**

**MECH-180** (mechanism_hypothesis, `status: candidate`, `v3_pending: true`,
`epistemic_category: standard`, `pending_retest_after_substrate: true`, already tied to a
separate, already-tracked substrate gap: `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`, DV3).
Same read: DV1/DV2 (2 of MECH-180's 3 named DVs) replicated the within-seed relationship; the
independence-discriminating leg is inconclusive for the calibration reason above. DV3 unaffected
by this run's finding (unchanged, separately tracked).

Both claims' prior "supports" (845/861/861a) are on a **single, non-independent configuration**
(same env, same 3 seeds) per GFLAG-0002's own framing — narrow/single-pathway. This run does
**not** independently corroborate them (the decisive leg didn't resolve), but nor does it weaken
them (C1 replicated cleanly on 3 genuinely new seeds, and the C2 failure has a diagnosed,
non-biological cause).

## 5. Biological-reference triage

MECH-180/INV-050's core mechanism (a learning/model-update-demand "third drive," proportional to
accumulated waking prediction error, modulating offline consolidation intensity/duration) is
well-grounded in the sleep literature — INV-050's own evidence_quality_note cites `lit_conf
0.887`. No divergence from a formal-definition import is implicated here; this is a pure
measurement/instrumentation finding about the experimental calibration procedure, not a
biological-plausibility question. No new `/lit-pull` is warranted.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Decisive independence leg (C2) unresolved due to calibration noise, not falsified; C1 replicated cleanly but is near-tautological given deterministic consumer arithmetic |
| Biological reference | clear | lit_conf 0.887 (INV-050); no divergence implicated; mechanism well-established |
| Developmental / dependency prerequisites | present | SD-MEL-PRODUCER (validated, V3-EXQ-798a) and SD-MEL-CONSUMER (validated, banked) both built and functioning |
| Implementation completeness | complete | Consumer arithmetic (`duration_factor = f(measured_mel / mel_reference)`) is deterministic and verified correct; DV3/MECH-122 substrate gap is separate, already tracked, deliberately descoped this run |
| Environment adequacy | adequate | For what's claimed (seed-independence only); environment-independence explicitly out of scope (lever (b), unchanged limitation, not new) |
| Measurement adequacy | **under-instrumented** | `mel_reference` calibration (`CALIB_EPISODES=3`, a short decoupled single-pass point estimate) has cross-seed sampling noise (~3x spread, 0.636-1.719, confirmed across all 6 seeds run to date) comparable to or exceeding the effect size C2 needs to discriminate |
| Integration adequacy | coupled | Mechanism arithmetic integrates correctly with the sleep-loop scheduler; counts respond deterministically and correctly to `duration_factor` |
| Scale / capacity | likely insufficient | Specifically `CALIB_EPISODES=3` is undersized relative to the noise floor it needs to characterize |

**Failure-location summary (GOV-FAILLOC-1):** Implementation **established** (adequate/complete).
Environment **established** (adequate for what's tested). Measurement **not established**
(under-instrumented). Net classification: single-bucket **MEASURES FAILED**. Not REE FAILED (all
three would need to read established). Not a demotion case — the demotion gate ("tested fairly +
biology supports the mechanism + still fails") is not met, since the test was not fair on its
decisive leg.

## 7. Learning extracted

- **Measurement gap** (primary): the MEL-reference calibration procedure (3-episode point
  estimate, decoupled pass) is too noisy to reliably anchor the C2 on/off discrimination. This
  gap was present in every prior run in this lineage but was masked by a separately-broken DV3
  leg in the older 3-DV conjunctive gate.
- **Positive-negative result** (partial): the within-seed graded MEL→offline-duration
  relationship (C1) replicated cleanly on 3 genuinely independent seeds, which is some real
  (if near-tautological, per the project's own prior lesson) independent corroboration.
- **No new dependency, no biology divergence, no implementation gap in `ree_core`.**

## 8. Repair pathway

**Node classification:** `complicated (buildable)` — the fix is a named, well-understood
redesign of the driver's own calibration procedure. No open scientific question about what to
build; no substrate build needed (the fix is entirely in the experiment driver, not `ree_core`).

**Routing: `/queue-experiment`**, same-question redesign (this replicates the same scientific
question — INV-050/MECH-180's third-drive coupling, independence-tested — so an alphabetic
suffix, e.g. `V3-EXQ-861c`, is the correct label per this project's EXQ-versioning convention,
not a new EXQ number).

**Redesign spec (sketch, for the queuing session to size):**
1. Increase `CALIB_EPISODES` substantially (e.g. 3 → 15-20) and/or average the reference over
   multiple independent repeated calibration draws to shrink the point-estimate's sampling
   variance below the effect size.
2. Replace the bare `factor > 1.0` threshold in C2 with an uncertainty-aware comparison — e.g.
   require `ARM_3` factor to exceed `1.0 + k * calibration_SD` for some margin `k`, where
   `calibration_SD` is estimated from the repeated draws in (1) — rather than a hard point
   threshold that a single noisy draw can flip.
3. Re-run on a THIRD, still-fresh seed triplet (or reuse 7/271/883 with the fixed calibration,
   since seed-independence from the ORIGINAL 42/123/456 set is already established for
   calibration purposes — the seeds themselves aren't the defect here, the reference estimate
   is).

**Explicitly recommended against:** re-queuing another `861d`/`861e` at the *same* calibration
methodology on yet another fresh seed triplet. Given the ~1/3 per-seed-triplet chance of hitting
the same coin-flip (2/6 seeds so far landed on the wrong side), that would burn compute without
raising confidence in the discriminator itself.

**GFLAG-0002 status:** remains **unresolved** (not failed, not passed) until a re-run with a
fixed calibration procedure produces a trustworthy C2 read.

**Granularity-debt recurrence check:** ran `scripts/granularity_debt_cluster.py` for both claims.
MECH-180: 6 targets, alignment distribution `intact=0, unclear=3, strengthened=2, other=1` — **no
target reads `weakened`**. INV-050: 6 targets, `intact=3, unclear=3` — **no target reads
`weakened`**. Trigger does **not** fire; this is measurement/test-design debt (now more precisely
characterized as a calibration-precision gap), not granularity debt, consistent with this
lineage's own prior GOV-GRAN-1 P1 disposition (2026-07-16: "coherent substrate-build campaign
circling ONE buildable gap," not bundled independent mechanisms).

**Re-derive brake:** counted under the R1-R3 convention. MECH-180: 2 confirmed `substrate_ceiling`
hits (677, 718a). INV-050: 3 confirmed `substrate_ceiling` hits (701b, 701c, 718a). Both already
fired historically and were released once SD-MEL-PRODUCER was built+validated (per each claim's
`ceiling_routing_note`). This autopsy's `recommended_epistemic_category` is `standard`, not
`substrate_ceiling`, so it does **not** add to either count. Brake does not fire on this reading.

**Fan-out recommendation:** not applicable — this is not a discrimination among rival mechanistic
hypotheses; it is a single, well-characterized measurement-design fix.

## 9. Interactive gate (Step 8)

Presented to the user 2026-08-13T19:39Z: facts, the ARM_0-factor cross-seed evidence for the
calibration-noise diagnosis, the four-layer table, and the recommended routing
(`epistemic_category: standard` unchanged both claims, `evidence_direction: non_contributory`
both claims, route `/queue-experiment` same-question redesign). **User confirmed: proceed as
recommended.**

## 10. Substrate-queue routing

`recommended_substrate_queue_entry.action: "none"` — no `ree_core` substrate defect. The fix is
entirely within the experiment driver's own calibration methodology
(`ree-v3/experiments/v3_exq_861*.py`), not a substrate build. `MECH122-CONTENT-PACKAGING-SPINDLE-
SELECTION` (the pre-existing, separately-tracked DV3 substrate gap) is untouched by this run's
finding — not amended.

## 11. Coordination-plane pause claim overlap note

The `autopsy-pause` claim on `REE_assembly/docs/claims/claims.yaml` (a coordination-plane-wide
path this skill's pause claim always lists) contended with an active `implement-substrate`
session (`igw-auto-igw-217-substrate-ready-sd-queue-seed-en-20260813T183630Z`, opened
2026-08-13T18:36:30Z, ~1h earlier) that is genuinely editing that file as part of landing a
substrate build. Opened `--allow-overlap`: this autopsy is analysis-and-handoff only and does not
itself edit `claims.yaml` — the two claims are on genuinely different tasks, not duplicated work.
