# Failure autopsy -- V3-EXQ-464e + V3-EXQ-467e (MECH-266 / SD-032a cluster)

- **Generated (UTC):** 2026-08-13T04:16:33Z
- **Scope:** cluster (2 targets)
- **Status:** confirmed (interactive gate cleared 2026-08-13)
- **Session:** pensive-franklin-1e285b (worktree)
- **Claims under test:** MECH-266, SD-032a

---

## 0. Dry-run gate (Step 2a)

`scripts/check_dry_run_citations.py` run over all 9 candidate run_ids considered for this
autopsy **before any metric was read**: `0 dry cited, 0 dry in named families, 0 ambiguous,
9 clean, 0 unknown`. Both targets are real, full-budget runs.

- `dry_run_checked: true`
- `excluded_dry_run_ids: []` (none found)

Additionally, the two targets share substrate-identical code: their `substrate_commit`s
differ (`2399196f2075` for 467e, `fa4b01372d12` for 464e) but the only diff between those
commits is `experiment_queue.json` (a `phase3-queue:` snapshot, 23 deletions, no substrate
change). **The cluster is one substrate observed through two structurally-different tests**,
not two systems.

---

## 1. Facts

### Targets

| | run_id | queue_id | landed (UTC) |
|---|---|---|---|
| T1 | `v3_exq_467e_mech266_mode_stickiness_behavioural_20260813T001847Z_v3` | V3-EXQ-467e | 2026-08-13T00:18 |
| T2 | `v3_exq_464e_mech266_competing_goals_behavioural_20260813T020141Z_v3` | V3-EXQ-464e | 2026-08-13T02:01 |

Both: `experiment_purpose: evidence`, `outcome: FAIL`, `evidence_direction: non_contributory`,
self-route `interpretation.label = substrate_not_ready_requeue`,
`route_reason = external_task_mode_not_occupied`. Seeds `[42, 43, 44]`. Predecessors
V3-EXQ-467d / V3-EXQ-464d (declared "successor, NOT supersede").

### Which criterion failed

The **absolute / negative-control criterion passes on both; the discrimination-enabling
precondition fails on both.**

| | `foraging_contact_guard` (thr 0.667) | `external_task_occupancy_reachable` (thr 0.667) | load-bearing criteria | `criteria_non_degenerate` |
|---|---|---|---|---|
| T1 467e | **1.0 MET** (3/3 seeds) | **0.0 NOT MET** | C1 fail 3/3, C2 pass 2/3 | C1 `false`, C2 `false` |
| T2 464e | **1.0 MET** (3/3 seeds) | **0.333 NOT MET** (1/3 seeds) | **C1 pass 3/3, C2 pass 3/3** | C1 `false`, C2 `false` |

T2 is a **vacuous pass**: both load-bearing criteria pass on every seed with maximal
separation, and both are flagged degenerate.

### The convergent shape -- bang-bang mode occupancy

`fraction_in_external_task` per arm/ratio cell:

**T2 (464e), 3 seeds x 2 arms:**

| seed | ARM_SYMMETRIC | ARM_ASYM_STICKY_TASK | occ_min | C1 | C2 |
|---|---|---|---|---|---|
| 42 | 0.0000 (ext 0 / plan 2215 steps, 15 switches) | **1.0000** (ext 1825 / plan 0, **0 switches**) | 0.0 | pass | pass |
| 43 | 0.0000 (ext 0 / plan 2409 steps, 15 switches) | **1.0000** (ext 2410 / plan 0, **0 switches**) | 0.0 | pass | pass |
| 44 | 0.4331 (ext 1045 / plan 1368, 16 switches) | **1.0000** (ext 1628 / plan 0, **0 switches**) | 0.4331 | pass | pass |

**T1 (467e), 3 seeds x 5 hysteresis ratios:**

| seed | r=0.10 | r=0.50 | r=1.00 | r=1.50 | r=2.00 |
|---|---|---|---|---|---|
| 42 | **1.0000** (0 sw, dwell 119.7) | 0.0 (12 sw, 76.2) | 0.0 (12 sw, 67.9) | 0.0 (12 sw, 84.1) | 0.0 (12 sw, 59.7) |
| 43 | 0.8073 (2 sw, dwell 144.3) | 0.0 (12 sw, 59.8) | 0.0 (12 sw, 51.7) | 0.0 (12 sw, 84.2) | 0.0 (12 sw, 84.1) |
| 44 | **1.0000** (0 sw, dwell 184.6) | 0.0 (12 sw, 76.0) | 0.0 (12 sw, 84.2) | 0.0 (12 sw, 43.3) | 0.0 (12 sw, 43.4) |

**19 of 21 cells sit at exactly 0.0 or exactly 1.0.** The two exceptions are 0.4331 (T2 seed 44
symmetric) and 0.8073 (T1 seed 43, r=0.10). `n_switches` at every r >= 0.50 is exactly 12 =
`n_episodes`, identical across a 20x sweep of the rail -- i.e. **the rail has no graded effect
on switching once the agent is outside the mode.**

### Expected vs observed

Expected (T1): a graded dose-response -- lower exit rail -> harder to leave -> longer dwell,
monotone non-increasing in `r`. Expected (T2): the sticky arm holds `external_task` longer
than the symmetric arm, with both arms genuinely occupying the mode.

Observed: a **step function**. The agent is pinned *inside* `external_task` at r=0.10 and
pinned *outside* it at every r >= 0.50, with no intermediate regime anywhere in the swept
range. Under the two-arm contrast the same saturation appears as perfect separation (1.0 vs
0.0) with zero switching on the sticky arm.

### Recording provenance

`ree-v3/validate_recording.py` reports both manifests **missing `config` and
`elapsed_seconds`** (always-core gap, advisory). This does **not** block adjudication here:
`substrate_hash`, `substrate_commit` (clean, `dirty: false`), `machine_class`, `seeds` and --
decisively -- `pre_registered_thresholds.affinity_input_cap = 2.0` are all present, so the
knob under calibration is recorded. Logged as a minor recording gap to close on the successor,
not as the blocking finding.

---

## 2. The self-route is factually wrong (Step-2 adjudication)

Per the standing rule, `interpretation.label` is a hypothesis, not a verdict. Here the label's
stated *cause* is contradicted by the run's own data.

`route_reason: "external_task_mode_not_occupied"` asserts the contested mode is not occupied.
**It is occupied -- at 100% of steps, on the sticky arm of every 464e seed, and at r=0.10 on
every 467e seed.** In the predecessors 464d/467d the mode read `0.0` on *every* seed and arm;
that is no longer true.

The gate reaches "not occupied" because it computes `min()` across arms (464e:610-634) or
across ratio arms (467e:592). That statistic **cannot distinguish two different pathologies**:

- (a) *unreachable* -- occupancy 0.0 everywhere (the 464d/467d state), and
- (b) *reachable but all-or-nothing* -- occupancy {0.0, 1.0} (the 464e/467e state).

Both yield `min = 0.0`. The label was written for (a) and is being applied to (b).

**The routing consequence is not cosmetic.** Under (a) the fix is "supply external-task
pressure" -- which is exactly what `mode-governance-engagement`'s `implementation_hint` still
says. Under (b) that build is *already done and working*, and the open problem is the opposite
one: the drive now dominates absolutely and nothing produces a mixed regime.

### What actually happened

The driver's own header records the two predecessor bugs and their fixes: (1) `_clone_for_arm()`
dropped the `GoalState` z_goal attractor on clone (`GoalState` is not an `nn.Module`, so
`state_dict()`/`load_state_dict()` never touched it), pinning `goal_state.is_active()=False`
and hard-gating engagement to 0; (2) `dacc_pe` was uncapped at ~15-17, two orders of magnitude
above `external_task_drive`'s [0,1]-bounded contribution. The fix added
`salience_affinity_input_cap` (ree-v3 `9bcde4cb63`) at `AFFINITY_INPUT_CAP = 2.0`.

**Both fixes worked.** They over-corrected: "external_task never wins" became "external_task
wins absolutely."

Critically, the driver author flagged this exact risk in-source (464e:165-174):

> "Starting point from a scratch diagnostic ... ARM_ASYM_STICKY_TASK occupancy 1.0
> (n_switches=0) vs ARM_SYMMETRIC 0.3 (n_switches=2) on a seed that previously read 0.0 on
> both arms -- the intended MECH-266 over-binding signature, no saturation degeneracy. **NOT
> yet re-derived/justified against the full 3-seed curriculum -- this run is that calibration
> check, not a confirmed final value.**"

So this run **is a declared calibration check, and it returned its answer**: on the full
3-seed curriculum the symmetric arm collapses from the scratch-diagnostic 0.3 to 0.0 on 2 of
3 seeds. `AFFINITY_INPUT_CAP = 2.0` is mis-calibrated. That is a real, interpretable,
pre-registered result -- and it is the reason this cluster is **not** non-contributory at
every layer, only at the MECH-266 claim layer.

---

## 3. Three distinct measurement defects

**M1 -- `min()` conflation (both targets).** As above: the non-vacuity statistic cannot
separate "unreachable" from "saturated". Emits a factually-false `route_reason`.

**M2 -- 467e's gate is anti-correlated with its own predicted effect.** The gate requires
`min over ALL ratio arms (fraction_in_external_task) > 0.1` -- occupancy above floor at *every*
rail including the loosest (r=2.00). But C1's hypothesis is that a high rail makes the mode
*easy to leave*. **The stronger MECH-266's effect, the more certainly the gate fails.** It is
not literally unsatisfiable -- a graded, moderate effect could hold occupancy above 0.1 at all
r while dwell declines -- but it is satisfiable only in the narrow band where the mechanism is
present *and weak*. The gate was imported from 464e's two-arm setting (where "both arms
occupied" is defensible) into a dose-response sweep that deliberately spans both sides of the
transition, under the V3-EXQ-643 same-statistic rule. The same-statistic rule is right; the
error is that in a sweep the *matched* statistic is per-arm occupancy conditioned on the
regime, not the min across a range designed to cross it.

**M3 -- `mean_dwell` is mode-agnostic.** `_eval_mode_dwell` (467e:418-455) accumulates
`all_run_lengths` on *any* mode change (`if new_mode != prev_mode`), so `mean_dwell` is the
mean run length across whichever mode the agent occupies. The rail is a uniform exit-rail
(`coord.set_hysteresis_ratio(r)`), so a mode-agnostic dwell is a defensible *choice* -- but
because occupancy flips completely across the step, the statistic silently changes **which
mode it summarizes** partway through the sweep. C1 therefore compares dwell in `external_task`
at r=0.10 against dwell in `internal_planning` at r >= 0.50. The four upper values are
unmanipulated noise (seed 42: 76.2, 67.9, 84.1, 59.7; seed 43 is *increasing*: 59.8, 51.7,
84.2, 84.1), and C1's monotonicity test fails on that noise rather than on the mechanism.

M3 is why C1 fails 3/3 even though the r=0.10 -> r=0.50 drop (119.7 -> 76.2 on seed 42) is
large and in the predicted direction.

---

## 4. Claim-layer mapping

**MECH-266** (`mechanism_hypothesis`, `provisional`, `v3_pending: false`,
`implementation_phase: v3`, `depends_on: [SD-032a, MECH-259, SD-033]`) asserts SD-032a's mode
register should carry per-mode `(enter_threshold, exit_threshold)` pairs with
`exit < enter` for stable modes (Schmitt trigger), asymmetry magnitude calibrated per mode.

**SD-032a** (`design_decision`, `stable`, `epistemic_category: standard`) specifies
`operating_mode` as a discrete variable over four modes and states: *"Mode transitions are
discrete, not graded -- though the switch threshold itself may be graded and learnable."*

**Did the experiment test the claim under conditions where it could express itself? No.**
MECH-266 predicts a *graded* asymmetry in how hard each mode is to leave. Both runs observed
the system only at two saturated operating points, never in a regime where a graded exit
threshold could differentiate anything. `claim_ids` tagging is accurate (both claims are
genuinely the subject), but neither run scored them.

**Tension worth flagging to governance:** SD-032a says transitions are discrete while the
*threshold* may be graded; MECH-266's behavioural falsifiers (both 464 and 467 lineages) test
for graded *occupancy/dwell*. Whether a discrete-transition register can produce the graded
occupancy signature these tests look for is precisely hypothesis H2 below -- and it is a
question about the claim pair's own internal consistency, not only about calibration.

---

## 5. Biological-reference triage

Closest mechanism: basal-ganglia direct/indirect pathway asymmetry with tonic-DA-dependent
hysteresis, and the AIC-dACC salience network (Menon & Uddin 2010) switching between
large-scale networks.

**Lit status: present.** Biology lit-pull complete 2026-04-27, six entries in
`evidence/literature/targeted_review_connectome_mech_266/entries/` (Fallon 2016, O'Reilly
2006, Cools 2019, Cools & D'Esposito 2011, Cools 2008, Collins & Frank 2014 OPAL). **No
`/lit-pull` commission is owed.**

**Is this a formal-definition import?** Partly, and the divergence is already on record and is
load-bearing. The claim's own `evidence_quality_note` carries implementation recommendation
(1): *"keep enter and exit thresholds independently tunable rather than locking to a fixed gap
(Cools 2008 inverted-U is smooth modulation, not fixed-gap Schmitt trigger)."* "Schmitt
trigger" is an electronics formalism; the biology it is standing in for is **smooth,
baseline-dependent modulation**.

**Does the failure resemble a known dependency being absent?** Yes, and pointedly. The observed
bang-bang, zero-switch, all-or-nothing arbitration is the **exact opposite of the inverted-U
smooth modulation** the lit-pull identified as the biological reality. A real BG gate does not
pin to one action set with zero exits; tonic DA sets a continuously-varying stability/flexibility
balance. So the saturation is not merely a tuning inconvenience -- it is a signature that the
current implementation reproduces the *symbol* of a hysteretic gate (rails, thresholds,
setters) without its *functional role* (a graded stability/flexibility trade-off). That is a
translation gap, and the lit-pull anticipated it four months ago.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | Neither run let MECH-266 express; no graded regime was ever entered. Not weakened -- untested. |
| Biological reference | **clear** | BG direct/indirect + tonic-DA hysteresis; 6-entry lit-pull complete. Observed bang-bang is the inverse of the Cools inverted-U smooth modulation the lit-pull specified. |
| Developmental / dependency prerequisites | **present** | SD-032a implemented; MECH-259 symmetric baseline present; the two 464d/467d blocking bugs are fixed and the fix demonstrably works (occupancy 0.0 -> 1.0). |
| Implementation completeness | **partial** | `AFFINITY_INPUT_CAP = 2.0` over-corrects. Symbol-of-mechanism present (rails, per-mode thresholds, `set_hysteresis_ratio`); functional role (graded stability/flexibility trade-off) absent at this operating point. |
| Environment adequacy | **adequate** | Contact guard 3/3 both runs; P2 contact rates 0.149-0.362; 69-215 contact events/seed. The foraging substrate is engaged. |
| Measurement adequacy | **under-instrumented / misleading** | Three defects M1/M2/M3 (Section 3). M2 makes the 467e gate anti-correlated with effect size; M3 makes C1 ill-posed across the step. |
| Integration adequacy | **coupled but unstable** | `external_task_drive` x `dacc_pe` x salience argmax now interact bang-bang; the cap moves *where* the step sits, not whether there is a step. |
| Scale / capacity | **unknown** | 3 seeds; 12 (467e) / 15 (464e) eval episodes per cell. Adequate to establish saturation; not powered to characterise a narrow mixed band if one exists. |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads from | Established? |
|---|---|---|
| MECHANISM FAILED | Implementation completeness = `partial` | **not_established** |
| MEASURES FAILED | Measurement adequacy = `under-instrumented / misleading` | **established** |
| ENVIRONMENT FAILED | Environment adequacy = `adequate` | **not_established** |
| REE FAILED | requires all three above adequate/complete | **false** |

**Net classification: MIXED (MECHANISM partial + MEASURES established) -- not chargeable to
REE.** Implementation reads `partial`, so the REE-FAILED bar is not met and no organism-level
"REE failed" reading is licensed by this cluster.

---

## 7. Cluster pattern

| Experiment | Claim | Absolute / negative-control criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-467e | MECH-266, SD-032a | contact guard **PASS** 3/3 (1.0) | occupancy gate **FAIL** (0.0); C1 fail 3/3, C2 pass 2/3 | step function at r in (0.10, 0.50); dwell noise above the step |
| V3-EXQ-464e | MECH-266, SD-032a | contact guard **PASS** 3/3 (1.0) | occupancy gate **FAIL** (0.333); C1+C2 **vacuous PASS** 3/3 | perfect arm separation 1.0 vs 0.0; zero switches on sticky arm |

**One structural property, not two independent bugs.** The two drivers differ in design (a
5-point dose-response sweep vs a 2-arm contrast), in DV (`mean_dwell` monotonicity vs
cross-arm occupancy margin), and in what a PASS would look like -- yet they return the same
underlying observation from substrate-identical code: **the SalienceCoordinator arbitrates
bang-bang, with no mixed-occupancy regime anywhere in the swept range.**

The two live readings:

- **substrate_calibration** -- a different operating point (cap value, or per-signal caps)
  admits a mixed regime; the arbiter can mix and the cap sweep simply has not found it.
- **structural_bang_bang** -- SD-032a's discrete argmax register cannot produce graded
  occupancy at *any* cap; the cap relocates the step but never removes it.

These force different planning decisions (calibrate vs redesign the mode register), and the
banked data cannot separate them: every observation to date is consistent with both. That is
what makes this a **discrimination**, and why the routing below is a portfolio rather than a
single build.

---

## 8. Learning extracted

1. **The `mode-governance-engagement` substrate build SUCCEEDED at its stated goal.**
   External_task occupancy moved from `0.0` on every seed/arm (464b/c/d, 467b/c/d) to `1.0` on
   the sticky arm of every 464e seed. Two substrate_queue failure records asserting "0.0 at
   EVERY seed" are now factually stale (Section 9).
2. **`AFFINITY_INPUT_CAP = 2.0` is mis-calibrated on the full curriculum** -- the answer to the
   calibration check the driver declared itself to be. The scratch-diagnostic symmetric-arm
   occupancy of 0.3 does not survive the 3-seed curriculum (0.0 on 2/3).
3. **A non-vacuity gate built on `min()` across a swept range is anti-correlated with the
   effect it gates** when the sweep is designed to cross a transition. Generalises beyond this
   pair: a same-statistic gate must be conditioned on the regime, not minimised across it.
4. **A mode-agnostic dwell statistic is unsafe as a DV when occupancy is not stationary across
   the sweep** -- it silently changes referent mid-experiment.
5. **A "vacuous pass" can be maximal-effect-size.** 464e's C1/C2 pass on 3/3 seeds with perfect
   separation, and are correctly flagged degenerate. Effect size is not evidence of
   non-degeneracy; the driver's `criteria_non_degenerate` flag earned its keep here.
6. **The observed saturation is the inverse of the claim's own biological basis** (Cools 2008
   inverted-U smooth modulation), which the 2026-04-27 lit-pull had already flagged as
   implementation recommendation (1). The divergence was predicted and is load-bearing.

---

## 9. Routing (confirmed at the interactive gate, 2026-08-13)

**Routing: `implement-substrate`** (re-derive brake mandated) **with a GOV-FANOUT-1
discrimination portfolio attached.**

### Re-derive brake -- FIRES, with a stated qualifier

Six prior `substrate_ceiling` hits for MECH-266 and SD-032a under the R1-R3 convention
(464b, 467b, 464c, 467c, 464d, 467d), against `RE_DERIVE_BRAKE_THRESHOLD = 2`.

**REFUSED: a naked V3-EXQ-464f / 467f re-queue** -- another lettered iteration of the same
question, at the same cap, behind the same gate, against the same substrate. That is exactly
the loop the brake exists to stop.

**Qualifier, stated rather than used to wave the brake away:** genuine substrate enrichment
*did* land between letters d and e (`salience_affinity_input_cap`, ree-v3 `9bcde4cb63`,
2026-08-12, plus the `_clone_for_arm` GoalState fix), and it demonstrably moved the system
(0.0 -> 1.0 occupancy). This is the documented condition under which the threshold may be
raised for a claim whose substrate is being enriched between letters. It does not license
another same-question letter; it does license the calibration and instrumentation work below,
which are different questions.

**Permitted under the brake:** the H1/H2/H3 portfolio (new questions, different DVs, one of
them requiring no new run); a re-scoring of banked data; substrate work on the arbiter.

### `epistemic_category: standard` -- NOT a 7th ceiling hit

Confirmed at the gate. Rationale: the substrate did not ceiling here, it **advanced**. The
blocker is calibration plus three measurement defects. Stamping `substrate_ceiling` would add
a 7th hit toward GOV-CEIL-1 demotion of a claim whose substrate just improved, and would place
MECH-266 in `_EPI_SUPPRESS_PROPOSAL` (hiding it from GOV-GRAN-1) *and* mark it not-v3-testable
(starving it of experiment lanes) -- precisely when the next three experiments are worth
running. `standard` is behaviour-preserving; the diagnosis lives in the note fields.

### Granularity-debt recurrence trigger: **DOES NOT FIRE** (this cycle)

Read via `scripts/granularity_debt_cluster.py MECH-266` -- **7 tagging targets across 4 files**
(not a filename grep). Alignment distribution: `intact=3, weakened=2, unclear=1, unstamped=1`.
At least one target reads `weakened`, so a genuine FAIL signature is present, and the
signatures *have* changed structurally across letters (b/c/d: mode never occupied, 0.0
everywhere -> e: mode occupied but all-or-nothing). That is the shape that normally routes to
`/claim-synthesis`.

It is **not** routed there this cycle because the newest signature change is attributable to a
*known, named, single cause* -- the cap over-correction -- rather than to the broad claim
hiding several finer mechanisms. Decomposing MECH-266 now would be decomposing against an
instrument with three identified defects (M1/M2/M3) and an operating point already known to be
wrong. **Re-run this trigger after the H1/H2 portfolio resolves**: if a calibrated,
correctly-gated substrate still produces structurally-different failures, that is genuine
granularity debt and `/claim-synthesis` becomes the right call. Recorded as
`granularity_debt_trigger.fires: false` with `defer_until` set, so GOV-GRAN-1's standing scan
still sees the cluster.

### Substrate queue -- `amend` `mode-governance-engagement`

Existing entry `sd_id: mode-governance-engagement` (priority 1, `unblocks_claims:
[MECH-266, SD-032a]`) already covers this gap. **Do not create a duplicate.**

Its `implementation_hint` is now **out of date in its stated direction**: "supply an
external-task pressure ... that produces genuine external_task occupancy" -- that build has
landed and works. The open problem is the opposite: the drive now dominates absolutely and
nothing yields a mixed regime.

**Prior failure records to mark resolved** (confirmed at the gate):

- `mode-governance-engagement` -> item `v3_exq_464c_...` ("fraction_in_external_task = 0.0
  both arms all seeds") -> `resolved`, cited to `v3_exq_464e_...`
- `mode-governance-engagement` -> item `v3_exq_467c_...` ("n_switches = 12 == n_episodes for
  every hysteresis ratio") -> `resolved` for the zero-occupancy half, cited to
  `v3_exq_467e_...`. **Note the switching half is NOT resolved** -- `n_switches == n_episodes`
  still holds at every r >= 0.50 in 467e; only the occupancy assertion is overturned.
- `sd_salience_contested_mode_occupancy` -> item "V3-EXQ-464b / 464c / 467d / 464d (all four
  FAIL) | fraction_in_external_task = 0.0 at EVERY seed WITH use_external_task_drive=True"
  -> `resolved`, cited to `v3_exq_464e_...` / `v3_exq_467e_...`

Leaving these open would keep telling future sessions the mode is unreachable and invite a
rebuild of work already done.

### GOV-FANOUT-1 portfolio (confirmed at the gate)

Three legs on three distinct design axes, each with a declared null:

| Leg | Hypothesis | Axis | Probe | Declared null |
|---|---|---|---|---|
| **H1** | Cap mis-calibration -- some `AFFINITY_INPUT_CAP` (or per-signal caps) admits a mixed regime | representation | Sweep the cap across the full 3-seed curriculum; DV = per-arm `fraction_in_external_task`, reported per-arm (never `min`) | No cap value yields per-arm occupancy in (0.1, 0.9) on >= 2/3 seeds |
| **H2** | Structural bang-bang -- SD-032a's discrete argmax cannot produce graded occupancy at any cap | constitution | Instrument the salience aggregate **margin** directly (continuous, pre-argmax), not the discrete mode label; characterise its distribution across caps | The margin distribution is unimodal/graded (i.e. saturation is a cap artefact, not structural) |
| **H3** | Instrumentation -- the gate and dwell statistic are ill-posed; verdicts are artefacts | instrumentation | **Re-score banked 464e/467e data**: per-arm occupancy gate conditioned on regime + occupancy-conditioned dwell. No new run required | Re-scoring changes no verdict |

**Run H3 first -- it is free.** It consumes only banked data and can invalidate the premises of
H1/H2 before either burns compute. H2 is the leg that would otherwise never get asked: every
prior experiment in this lineage read the *discrete mode label*, which is exactly the variable
that cannot distinguish "graded arbitration rendered discrete at the output" from "arbitration
that is discrete all the way down."

Pre-registered as a new frozen-ledger question `mech266_mode_arbitration_saturation` (Mode A,
three legs `alive`) -- no existing question covers MECH-266/SD-032a, so no
`growth_restriction` check applies.

### Draft `evidence_quality_note` for governance (do not apply from this skill)

> V3-EXQ-464e / 467e (2026-08-13, cluster autopsy
> `failure_autopsy_mech266-464e-467e-cluster_2026-08-13`): non_contributory at the claim layer
> -- neither run scored MECH-266. The predecessor blockers ARE fixed: the `_clone_for_arm`
> GoalState drop and the uncapped `dacc_pe` are corrected, and external_task occupancy moved
> from 0.0 on every seed/arm (464b/c/d, 467b/c/d) to 1.0 on the sticky arm of every 464e seed.
> The `mode-governance-engagement` build succeeded. The fix over-corrected:
> `AFFINITY_INPUT_CAP=2.0` produces bang-bang arbitration -- 19 of 21 arm/ratio cells at
> exactly 0.0 or 1.0 occupancy, zero switches on the sticky arm, `n_switches == n_episodes` at
> every hysteresis ratio >= 0.50 -- so no mixed regime exists in which a graded exit threshold
> could express. 464e's C1/C2 pass 3/3 with maximal separation and are correctly flagged
> degenerate (vacuous pass). Three measurement defects identified: the non-vacuity gate's
> `min()` across arms/ratios conflates "mode unreachable" with "mode saturated" and emits a
> factually-false `route_reason: external_task_mode_not_occupied`; 467e's min-over-all-ratios
> gate is anti-correlated with its own predicted effect (a stronger hysteresis effect drives
> occupancy to 0 at high rails, failing the gate); and `mean_dwell` is mode-agnostic, so C1
> compares dwell in external_task at r=0.10 against dwell in internal_planning at r>=0.50.
> Category `standard`, NOT `substrate_ceiling` -- the substrate advanced rather than ceilinged,
> and a 7th ceiling stamp would suppress the claim from GOV-GRAN-1 and mark it not-v3-testable
> exactly when the discriminating experiments are worth running. Whether the saturation is a
> cap artefact (H1) or structural to SD-032a's discrete argmax register (H2) is unresolved and
> pre-registered as `mech266_mode_arbitration_saturation`; H3 re-scores the banked data at zero
> compute cost. Minor recording gap: both manifests omit `config` and `elapsed_seconds`
> (`affinity_input_cap` IS recorded in `pre_registered_thresholds`).

### Follow-on NOT chipped

Per the standing rule, a `/failure-autopsy` session does not `spawn_task` follow-on that
depends on its own not-yet-governance-reviewed routing. The H1/H2/H3 portfolio, the
`mode-governance-engagement` amend, and the three failure-record resolutions are **reported
here and in the closing note**; `/governance` chips them once Step 2b/4/6a ratifies the
disposition (checking `igw_routine_ledger.json` / `igw_assignments.json` first, since IGW
auto-discovery may already have staged the substrate build).
