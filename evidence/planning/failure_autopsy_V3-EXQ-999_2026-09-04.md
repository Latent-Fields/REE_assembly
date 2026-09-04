# Failure autopsy -- V3-EXQ-999 (MECH-161, vigilance inverted-U heartbeat sweep)

- **run_id**: `v3_exq_999_mech161_vigilance_inverted_u_heartbeat_20260903T211939Z_v3`
- **queue_id**: V3-EXQ-999 | **claim**: MECH-161 | **purpose**: `evidence` | **outcome**: FAIL
- **generated_utc**: 2026-09-04T14:22:46Z | **session**: governance-20260904-1347
- **status**: `awaiting_human_confirmation` (staging mode -- Step 8 gate is OWED, not waived)
- Facts reconstruction, with every number and every probe: [`facts_V3-EXQ-999.md`](facts_V3-EXQ-999.md)

---

## 1. One-paragraph summary

The run aborted at its first seed on a P0 readiness precondition that describes itself as the
"positive control that hazard-avoidance behaviour was trained at all", measuring **-0.2608**
against a **+0.05** floor, and self-routed `substrate_not_ready_requeue`. **The self-route's
verdict (non-contributory) is right; its causal story is wrong.** Replaying the driver's own
readout on the same env config and seeds shows that a policy which takes the geometrically
correct avoidant action on **every single step** -- a perfect avoider -- scores
**sensitivity = +0.0000** and **also fails the +0.05 gate**, while policy-free nulls with zero
hazard knowledge score **-0.06 to -0.44** with single-seed values spanning **+0.109 to -0.583**.
The observed -0.2608 sits inside that null band. The gate therefore has no power to separate
"avoidance untrained" from "avoidance perfect", and the run tells us nothing about the substrate's
readiness -- only that the instrument is broken. This is the skill's canonical
`precondition_unmet` case: *the precondition test itself is wrong*, not the branch's assumption.

## 2. What was tested, and what actually ran

MECH-161 asserts that ready vigilance requires an **arousal regulator** holding an optimal
sensitivity on the LC-NE inverted-U, implemented via MECH-093's heartbeat-frequency modulation.
V3-EXQ-999 trains one agent per seed at P=10, freezes it, and evaluates it at five forced
heartbeat periods `[5, 8, 10, 15, 20]`, asking whether hazard-detection sensitivity peaks at an
interior level (C1_interior_max_margin).

The baseline level (P = 10) is evaluated first so the P0 gate can abort cheaply. It did:

| precondition | measured | threshold | direction | met |
|---|---|---|---|---|
| `baseline_avoidance_discrimination_margin` | **-0.260797342192691** | 0.05 | lower (`met iff >= `) | **false** |

`p0_readiness_gate` raised `P0NotReady`, `run_experiment` stamped `{"seed": 11,
"p0_not_ready": true}` and **`break`ed the seed loop**. Seeds 23 and 37 never ran. 43m52s of
compute produced one aborted seed.

**Which criterion failed: an ABSOLUTE (positive-control) one.** The decisive *discrimination*
criterion was never evaluated -- `criteria_non_degenerate.C1_interior_max_margin: false` in the
manifest is a **hardcoded literal on the abort branch**, not a measurement. This is the inverse of
the substrate-ceiling fingerprint (there the negative control passes and discrimination fails);
here the absolute bar failed and discrimination was never reached.

**Recording provenance.** `validate_recording.py` reports **OK -- 0 always-core gaps**:
`recording_schema`, `substrate_hash` (`4de17226...`), `substrate_commit` (`7d896c94`, clean),
`machine`/`machine_class`, `elapsed_seconds`, full `config` and explicit `seeds` are all present.
The dry-run gate is clean (`check_dry_run_citations.py`: 2 clean, 0 dry, for this run and
V3-EXQ-981); `validate_experiments.py --checks dry_run_unreachable_criterion` fires 11 fleet-wide
warnings, **none on this driver**.

## 3. The finding -- the P0 gate cannot discriminate by construction

The readout, verbatim from the driver: `sensitivity(P) = hit_rate(P) - false_alarm_rate(P)`,
where `hit_rate` is the rate at which the agent's chosen action equals `_avoidant_action` in the
HIGH hazard bin, and `false_alarm_rate` is the same rate in the SAFE bin. `_avoidant_action` is
`argmax_a dot(action_delta_a, agent - nearest_hazard)`.

**The response is defined as the correct answer.** "Avoidant" means matching the away-from-hazard
geometric argmax -- a quantity that is well-defined and equally matchable in *every* bin. There is
no signal/noise asymmetry, so the signal-detection framing does not hold. Consequence, measured
rather than argued (probe scripts in this directory; same env kwargs, same seeds, same
compare-before-step ordering):

| policy | seed 11 | seed 23 | seed 37 | mean | clears +0.05? |
|---|---|---|---|---|---|
| **`oracle_avoid`** -- correct avoidant action EVERY step | +0.0000 | +0.0000 | +0.0000 | **+0.0000** | **NO** |
| **`oracle_avoid_held`** -- avoidant action at each E3 tick (P=10), held | -0.0735 | -0.1216 | +0.1651 | **-0.0100** | **NO** |
| null: uniform-random every step | -0.1208 | -0.0360 | -0.2219 | -0.1262 | no |
| null: random held P=5 | -0.2297 | +0.0095 | -0.1696 | -0.1299 | no |
| null: random held P=10 | +0.1090 | -0.3745 | +0.0835 | -0.0607 | no |
| null: random held P=20 | -0.2538 | -0.5832 | -0.4700 | -0.4357 | no |
| **V3-EXQ-999, trained agent, P=10, seed 11** | **-0.2608** | (never ran) | (never ran) | -- | **NO** |

`oracle_avoid` gives `hit_rate = false_alarm_rate = 1.000` on all three seeds. **No threshold
above zero can be passed by a perfect avoider.** And the null is not centred on zero -- it is
strongly negative and enormously dispersed, so the observed -0.2608 is an ordinary draw from it.

Two structural contributors, both measured:

**(a) The SAFE bin is a far-corner artifact.** `hazard_field_view` is normalised by the global
field max, so with one hazard and `hazard_field_decay = 0.5` the agent's own cell reads exactly
`1/(1 + 0.5 d)`. Therefore **HIGH (>= 0.50) is `d <= 2`** and **SAFE (< 0.15) is `d >= 12`**.
On a 10x10 grid `d >= 12` is *unreachable* for a centred hazard (max d = 10) and is a far-corner
wedge otherwise. Census over 40 resets per seed: SAFE is **1.1-2.2% of non-wall cells**
(0, 0 and 1 SAFE cells on the three first-episode grids). In those cells the designated avoidant
action walks into a wall or off the edge -- a clamped no-op -- in **93.3-100% of SAFE-bin steps**.
`false_alarm_rate` is therefore measuring *pressing into the boundary at maximum distance*, not
*taking flight from nothing*.

**(b) The mitigation the driver relied on does not touch this.** The driver's own Step-4.5
red-team raised the near-empty SAFE band as Family 2 and dispositioned it, verbatim, as
*"mitigated by the pre-existing MIN_BIN_COVERAGE_STEPS=5 per-(seed,level) coverage gate"*.
A **count floor is not a bias check**: SAFE n in the null runs ranged 4-207 per (policy, seed),
so the geometry-selected, wall-clamped cells clear the floor comfortably and the mitigation never
engages. (This is the 7c family "a gate that cannot discriminate by construction, graded
adequate" -- caught here by hand, exactly as that rule anticipates.)

**Aggravating design choice.** The gate aborts on the **first** seed. With a cross-seed null SD of
roughly 0.2, a single draw decided the fate of the whole 3-seed run. Nothing about seed 11 was
privileged; in V3-EXQ-981 seed 11 was in fact the *least* negative of the three (-0.027 vs -0.477
and -0.789).

## 4. This is the SECOND run blocked by the same instrument

`_avoidant_action` exists in exactly **two** drivers in `ree-v3/experiments/`; exactly **one**
other manifest in the corpus carries the `"avoidant"` bin key. Both are here:

| run | when | statistic | measured | threshold | met |
|---|---|---|---|---|---|
| V3-EXQ-981 (MECH-027) | 2026-09-03T05:30Z | `positive_control_hazard_sensitivity` | **-0.4307** | +0.05 | false |
| V3-EXQ-999 (MECH-161) | 2026-09-03T21:19Z | `baseline_avoidance_discrimination_margin` | **-0.2608** | +0.05 | false |

Same apparatus, same thresholds (SAFE < 0.15, HIGH >= 0.50, coverage 5), same env family, same
seeds `[11, 23, 37]`, same +0.05 bar. **2 of 2.** That is a structural property of the apparatus,
not two independent bugs. 981's per-seed baseline margins were -0.027 / -0.477 / -0.789; its most
extreme single cell is a HIGH-bin avoidant rate of **1/180 = 0.0056**, 36x below the 1/5 uniform
expectation, sitting beside a SAFE-bin rate of **10/10 = 1.000** in the same block.

**And the reuse claim was already refuted when V3-EXQ-999 was authored.** The queue entry states
the readout was *"reused verbatim from V3-EXQ-981's **calibrated** ... apparatus"*. It was reused
from 981's **driver**, not from 981's **result**: 981's manifest landed 16 hours earlier with the
positive control already failed, and 981's autopsy was **confirmed at 2026-09-03T20:04Z, 75
minutes before V3-EXQ-999 started**. A GOV-REUSE-1 / Step-2.5a readiness check that reads a
predecessor's source but not its manifest re-inherits the predecessor's blocker.

## 5. Claim-layer mapping -- do not let this touch MECH-161 in either direction

MECH-161: `candidate`, `implementation_phase: v3`, `depends_on: [MECH-026, MECH-093, ARC-016,
ARC-044]`, **`evidence: []`**, **no `epistemic_category`**, **no `evidence_quality_note`**, **no
`pending_retest_after_substrate`**. This is the first run ever to tag it.

Did the experiment let the claim express itself? **No, twice over.**

1. **It aborted before any discriminating level ran.** Nothing was measured on the rate axis.
2. **Even a completed run would have addressed only the claim's SHAPE premise.** MECH-161 asserts
   ready vigilance *requires an arousal REGULATOR*. This driver forces the heartbeat period
   externally and, by design, re-asserts `agent.clock._current_e3_steps = P` after every
   `_e1_tick()` precisely so that MECH-093's `update_e3_rate_from_beta` **cannot** act. That is a
   defensible operating-point sweep for the background question *does an interior optimum exist on
   the rate axis*, and the driver says so. It is not, and could not be, a test of the regulator
   assertion. MECH-026's own `what_would_answer` records the regulator as **UNBUILT**, verbatim:
   *"no such controller exists in `ree_core/`"*. A future disposition must narrow the scope
   accordingly rather than reading a shape result as a regulator result.

The claim tag itself is accurate (not inherited-without-re-evaluation), and this is not an
out-of-domain/clinical claim, so no reclassification applies. MECH-093's prior FAIL (EXQ-097,
`p1_rate_gap = -0.74` against `>= 2.0`) is worth carrying forward: the rate channel is wired but
z_beta does not track harm salience, so a regulator built on it has no working input yet.

## 6. Biological-reference triage

**Closest reference:** LC-NE adaptive gain -- tonic/phasic noradrenergic modulation setting an
operating point on an inverted U between missed signals and hypervigilant false alarms, read out
as signal-detection sensitivity. **Not a formal-definition import**: the inverted-U is imported
faithfully from a real, well-evidenced literature.

**Does the failure resemble a missing biological dependency?** Partly, and usefully: in the
reference system the operating point is *regulated* by a signal that tracks task utility /
threat, and here the analogous signal (z_beta -> rate) is already known not to track harm salience
(EXQ-097). But that is not what stopped this run. What stopped this run is an instrument.

**Two translation choices with no literature behind them**, and this is the load-bearing part:

1. **Rate, not gain.** MECH-161 asserts the arousal parameter carrying the inverted-U is the E3
   *update period*. The corpus has Aston-Jones & Cohen 2005 (adaptive gain) and Langner & Eickhoff
   2013 (vigilant attention) but **nothing** on whether sampling *period* rather than *gain* is the
   right analogue. This is a real divergence, not a caveat.
2. **The SDT operationalisation.** `targeted_review_sd_069` (Nuiten et al. 2026) reads arousal
   effects off a yes/no detection task where the response is a report **independent of the stimulus
   geometry**, separating criterion from sensitivity via SDT + drift-diffusion. This driver defines
   the response *as* the correct-answer geometry -- which is exactly what collapses the oracle to
   zero. The literature already shows what a valid readout looks like; it simply was not used.

**lit_status: `partial`** -- present for the LC-NE inverted-U / vigilant-attention biology
(`targeted_review_connectome_mech_026` Langner & Eickhoff 2013; `targeted_review_connectome_mech_313`
Aston-Jones & Cohen 2005; `targeted_review_sd_069` Nuiten 2026; `targeted_review_arc_066_tonic_vigor`);
**absent** for MECH-161 itself (no `targeted_review_mech_161`; MECH-161 appears in no `SYNTHESIS.md`)
and absent for the rate-vs-gain choice. A `/lit-pull` commission is **not** the primary routing --
the biology of the shape premise is adequately covered and the blocker is an instrument -- but a
targeted pull on "is sampling period or gain the LC-NE arousal analogue" would retire divergence (1).

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | Aborted before any discriminating level. And by design the run bypasses the regulator MECH-161 is about, so it could only ever have addressed the shape premise. |
| Biological reference | **clear** (for the shape) / **partial** (for the translation) | LC-NE inverted-U is well evidenced. Rate-vs-gain and the SDT operationalisation are unwarranted; Nuiten 2026 shows the right readout shape. |
| Prerequisites | **MIXED** | MECH-093's rate channel implemented and probe-verified live; ARC-016 stable. But MECH-161's regulator is UNBUILT (MECH-026 `what_would_answer`) and MECH-093's z_beta does not track harm salience (EXQ-097 `p1_rate_gap` -0.74). |
| Implementation completeness | **partial** | `_train_warmup` trains e1, the e2 world-forward model and the e3 `harm_eval` head -- **no action policy on harm**. `NAV_BIAS = 0.25` overrides a quarter of training actions *toward* the hazard. Trained avoidance has never been demonstrated on this bed by any run. |
| Environment adequacy | **too sparse** | SAFE band = `d >= 12`: unreachable for a centred hazard on 10x10, 1.1-2.2% of non-wall cells otherwise, avoidant action a wall no-op in 93-100% of those steps. |
| Measurement adequacy | **misleading -- DOMINANT** | Oracle scores +0.0000 and fails the +0.05 gate; nulls score -0.06 to -0.44; observed -0.2608 lies inside the null band. The gate cannot discriminate, and it aborts on one seed of a statistic with cross-seed SD ~0.2. |
| Integration adequacy | **isolated** | Harness bypasses `agent.step()`; `force_heartbeat` overwrites MECH-093's output every tick. Legitimate for a sweep, but no regulator loop was exercised. |
| Scale / capacity | **unknown** | 150x100 warmup cannot be assessed for sufficiency until a valid avoidance readout exists. |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | **not_established** -- implementation is `partial` (no harm-conditioned policy training) and the mechanism was never exercised. |
| MEASURES FAILED | **not_established** -- measurement reads `misleading`; the measures are the *defect*, not a passing bucket. |
| ENVIRONMENT FAILED | **not_established** -- environment reads `too sparse`. |
| REE FAILED | **false** -- none of the three reads adequate/complete. |

**Net: MIXED (MEASURES + ENVIRONMENT, MECHANISM never exercised) -- not chargeable to REE.**
The measurement layer is dominant.

### Recording-debt vs measurement-debt

**Both, and they are separable.** The *measurement debt* is the readout itself (section 3) -- the
metric was blind by construction and needs redesign. Separately there is genuine **recording debt**:
the P0-abort branch stamps only `{"seed": 11, "p0_not_ready": true}` into `arm_results`, throwing
away the baseline level's `hit_rate`, `false_alarm_rate`, per-bin `n`/`avoidant` counts,
`coverage_ok`, `n_e3_ticks`/`committed_fraction` and `world_forward_r2` -- **all of which existed
at run time**. From the manifest alone one cannot tell whether -0.2608 came from a near-zero
hit rate, an inflated false-alarm rate, or an under-covered SAFE bin. That decomposition is what a
reader needs, and it costs nothing to write
(`experimental_recording_standard_2026-07-12.md` 3b/3c). The re-queue must close it.

## 8. Recurrence, brake and granularity checks

- `granularity_debt_cluster.py MECH-161` -> **0 targets across 0 files**. Granularity-debt trigger
  **does NOT fire**. No `claim_alignment` distribution exists to report (empty cluster), and with
  zero targets the "at least one `weakened`" precondition is trivially unmet.
- **Re-derive brake (R1-R3, confirmed artifacts only, run 2026-09-04 from `/Users/dgolden/REE_Working`)**:
  `BRAKE HITS for MECH-161 = 0`, total tagging targets = 0. Below the threshold of 2 --
  **brake does NOT fire**, and a same-question lettered re-queue is permitted.
- `check_autopsy_coverage.py V3-EXQ-999` -> `AVAILABLE: YES`. No prior artifact covers it.
- **Forward warning, recorded on the JSON's `re_derive_brake.note`:** this target *will* count as
  hit 1 under the R1-R3 step-4 fallback (`recommended_evidence_direction: non_contributory`,
  category `standard`), even though the diagnosis is an instrument defect. The enum-only category
  vocabulary has no spelling for "measurement defect", so step 2's INSTRUMENT token match can never
  fire on a compliant category. A future session must not read a count of 2 on MECH-161 as a
  substrate ceiling without re-reading this artifact.

## 9. Learning extracted

1. **A positive control must be validated against a measured ORACLE, not only against a null.**
   Here the null is strongly negative *and* the oracle is exactly 0.000, so no threshold above zero
   can pass a perfect avoider -- a failure invisible to any check that only asks whether the
   statistic moves.
2. **An SDT-shaped statistic is only SDT-shaped if the response is defined independently of the
   correct answer.** Defining "avoidant" as matching the away-from-hazard argmax makes hit and
   false-alarm the same measurement taken in two places.
3. **A per-cell COUNT floor does not mitigate a SELECTION bias.** `MIN_BIN_COVERAGE_STEPS = 5` was
   the stated mitigation for the near-empty SAFE band and never engaged.
4. **"Reused verbatim from <prior run>'s calibrated apparatus" is a claim about that run's RESULT,
   not its source.** 981's positive control had already failed at -0.4307; its autopsy was confirmed
   75 minutes before 999 started.
5. **A normalised proximity field plus fixed global bin thresholds makes bin membership a function
   of entity PLACEMENT.** SAFE < 0.15 silently means `d >= 12`, structurally unreachable on 10x10
   whenever the hazard is not near a corner. Check threshold *reachability* against geometry before
   reusing bins.
6. **An early-abort branch that stamps only `{seed, p0_not_ready}` destroys the decomposition of the
   very number that caused the abort.** Record the level's cells even when aborting.
7. **A P0 gate that aborts on the FIRST seed turns a statistic with a large cross-seed null SD into
   a coin flip on one draw.** Evaluate readiness over the seed set.

## 10. Repair pathway and routing

**Work-graph classification.** The readout repair is `complicated (buildable)` -- the defect and its
fix are both named, so build it; do not queue a spike to re-confirm it. The sub-question *is
hazard-avoidant behaviour learnable under this warmup at all* is `complex (probe-gated) / puzzle
(known rules)` -- a missing fact, obtainable by one probe. That split is why the fan-out below
carries an H2 leg rather than assuming the readout fix suffices.

**PRIMARY ROUTING: `/queue-experiment`, alphabetic suffix `V3-EXQ-999a`.** Same scientific question
(interior optimum vs monotone on the heartbeat-rate axis), implementation fix to the instrument --
so a letter, not a new number. Non-negotiables for the re-queue:

- a hazard-sensitivity DV whose **response is independent of the correct-answer geometry**
  (hazard-field gradient actually descended per step; time-to-hazard-contact; or an explicit
  alarm/withdraw response category), with **a measured oracle arm and a measured random arm** in the
  same run and the pass bar **derived from their separation** rather than hand-picked;
- **bins re-derived on the per-episode field distribution** (quantiles) or a lower
  `hazard_field_decay` / larger grid, plus reporting of per-bin `n` **and the wall-clamp fraction**
  of the designated response;
- **the readiness gate evaluated over all seeds**, not aborting on seed one;
- **the recording gap closed** -- per-bin `n`/`avoidant`, `hit_rate`, `false_alarm_rate`,
  `coverage_ok`, `committed_fraction` and `world_forward_r2` stamped **even on the abort path**, via
  `experiments/_lib/manifest_core.stamp_recording_core(...)`, per
  `experimental_recording_standard_2026-07-12.md` 3b/3c.

**SECONDARY: `recommended_substrate_queue_entry.action = "create"`**
(`HAZARD-AVOIDANCE-READOUT-AND-TESTBED`, `severity: corrupting`, `priority_suggested: 1`,
`node_class: complicated (buildable)`, `unblocks_claims: [MECH-161, MECH-026, MECH-027]`). No
existing entry in the 169-entry `substrate_queue.json` covers a hazard-avoidance readout, a
hazard-sensitivity positive control, an avoidance training regime, or an arousal regulator -- checked
by `unblocks_claims` and by title/blob match. This create is **not** a `ree_core` build; its purpose
is to make the shared defect visible to `/queue-experiment` Step 2.5c so a **third** driver cannot
copy-paste the apparatus and score a criterion on it without a P0 gate. `severity: corrupting` is
chosen deliberately: the statistic is emitted as a measurement and has already been *read* as one
(section 11). If governance would rather fold this into the re-queue than carry a queue entry, say
so explicitly -- the failure mode to avoid is the gap staying unregistered.

**GOV-FANOUT-1 fan-out emitted** (3 legs, 3 different axes, each with a declared null):
H1 readout-invalid (`measurement`), H2 avoidance-genuinely-absent (`learning-signal`),
H3 env-band-absent (`environment`). Emitted despite the immediate repair looking like one named
build, because a re-queue fixing *only* the readout returns non-contributory again if H2 holds, and
the corpus contains no evidence either way about whether avoidance is trainable here. All three axis
labels are already classified in `axis_families.map`; no map addition needed.

**Not routed to `/lit-pull`** as primary (the shape premise's biology is adequately covered), and
**not routed to `/claim-synthesis`** (granularity trigger does not fire: 0 tagging targets), and
**not to governance-demotion** (the highest threshold is nowhere near met -- the claim was never
tested).

## 11. Read-across, not adjudicated

- **V3-EXQ-981's confirmed autopsy attributes this same reversed sign to the ENVIRONMENT** -- its
  four-layer environment row reads *"wrong pressures ... The DV/env pairing is not hazard-sensitive,
  which invalidates anything built on top of it"*, repeated in its `evidence_quality_note`. The
  oracle probe here locates the reversal in the **readout**: a perfect avoider scores +0.0000 on the
  same statistic, which no property of the environment can explain. **That is a correction to one of
  981's four failed-precondition attributions and nothing more.** 981's overall disposition
  (non_contributory, `standard`, never tested, routing `queue-experiment`) is unaffected; its other
  three failed preconditions (replay-channel reachability, precision-margin headroom,
  commit-temperature headroom) are untouched. Re-adjudicating a confirmed artifact is out of this
  target's scope -- governance may route it as a re-adjudication or record it as a bears-on note on
  MECH-027.
- **MECH-026's stated blocker is untouched.** It carries `epistemic_category: substrate_conditional`
  and names MECH-161's regulator as UNBUILT and as its own non-degeneracy precondition. Worth
  governance noting that the first attempt to probe MECH-161 chose to *bypass* the regulator rather
  than build it, so nothing of the V3-EXQ-999a shape will move MECH-026 either.
- **Provenance note, flagged not investigated.** The driver was authored under
  `/metaworker-orchestrate` session `daily-20260903-exq999-mech161`, whose queue-entry DEVIATIONS
  block records the script as left untracked and uncommitted in ree-v3 with the queue append
  deferred. Whether the shipped driver is byte-identical to the reviewed one is checkable --
  `arm_fingerprint.driver_script_hash = cb6ddc671f20a6743c2fc73fb2ba88e2a6cf27cb2d4b6660be58d2d60a8a439e`
  against the landed file -- but was not checked here. Infrastructure observation, not a claim-layer
  finding.

## 12. Recommended dispositions (governance applies; this skill only recommends)

- `recommended_evidence_direction`: **`non_contributory`**
- `recommended_epistemic_category`: **`standard`**. Deliberately not `substrate_ceiling` /
  `substrate_conditional`: those assert the claim's answer is gated on substrate work, and they
  would suppress MECH-161 from GOV-GRAN-1 surfacing and from v3 experiment lanes -- exactly wrong for
  a candidate claim with zero evidence whose instrument has never worked. MECH-161 carries no
  category today, so this is a first stamp.
- `pending_retest_after_substrate`: **true** (required pairing for any non_contributory /
  substrate-limitation recommendation).
- **Narrow-supports check (also required by that pairing):** MECH-161's `evidence` is `[]` -- **zero**
  prior entries of any direction. There are no supports to be narrowed or made illusory, so the
  check is satisfied honestly and vacuously. `narrow_supports_flag: false`.
- `recommended_diagnostic_evidence_adjudicated`: **NOT set** -- `experiment_purpose` is `"evidence"`,
  and that flag is only for `diagnostic`/`baseline` targets.
- `status_change`: none -- MECH-161 stays `candidate`.
- The full drafted `evidence_quality_note` text is in the JSON's
  `recommended_evidence_quality_note`; governance writes it verbatim.
- `per_claim_recommendation.MECH-161.change` ends on
  `-> epistemic_category: standard`, which is **storable** (a claims.yaml field) and **not yet true**
  (MECH-161 carries no `epistemic_category`), so GOV-APPLY-1 can clear it both by value and by
  provenance.

## 13. Step 7b fires

`/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/autopsy_pre_routing_checks.py --artifact
failure_autopsy_V3-EXQ-999_2026-09-04.json --json`

**`fire_count: 0`, `fires: []`.**

| check | result | disposition |
|---|---|---|
| C1-strict (driver already exists for the recommended experiment) | quiet | Nothing to act on. The recommended `V3-EXQ-999a` does not exist. |
| C2-strict (recommended substrate entry already exists) | quiet | Consistent with the manual sweep of all 169 `substrate_queue.json` entries in section 10 -- no entry covers this gap by `unblocks_claims` or by title/blob. `create` stands. |
| C3 (literature exists for a question declared ABSENT) | quiet | Consistent, and note the artifact declares `lit_status: "partial"` with an explicit scope string ("PRESENT for ... ABSENT for ..."), which is the shape C3 cannot read on its own. Carry to the Step 8 gate for the user to check. |
| C5 (a run already scored on a bed the prose calls unique/unrun) | ran clean on the final pass **with** the sibling `.md` present (it reported `inapplicable -- no sibling .md narrative` on the first, JSON-only pass) | Nothing to act on. |
| C6-narrow (a metric agrees across arms in most seeds and dissents in a minority) | `inapplicable` -- prose asserts an absolute, but no target manifest carries a top-level `arm_results` array of >= 4 rows | Correct: one seed, one aborted arm. **Read as "could not look", not as "no fire".** |
| C7 | `inapplicable` -- no arm/condition-structured array with >= 2 arms and >= 2 seeds | Correct: the run aborted after one seed. **Read as "could not look", not as "no fire".** |

(Both runs -- JSON-only and with the sibling `.md` -- returned `fire_count: 0`.)

**`inapplicable` is not "no fire".** C6 and C7 were structurally blind here, and C1/C2/C3's claim-keyed
lookups had only a single claim with zero prior evidence to work with. The manual work in sections
3, 4 and 10 -- the oracle/null probes, the two-driver recurrence table, and the hand sweep of
`substrate_queue.json` -- carries the load the mechanical checks could not. Step 7c (the parent
session's red-team) should point at the routing decisions in section 10 and at the `create`
recommendation in particular.

## 14. Open questions this autopsy could NOT settle

1. **Was avoidance actually trained?** Undecidable from the record: the abort discarded the
   `hit_rate` / `false_alarm_rate` decomposition and the per-bin counts, and no valid readout exists
   to answer it with. This is H2 in the fan-out, not a conclusion.
2. **Would a corrected readout show an interior optimum on the rate axis?** Entirely untouched. The
   sweep never ran.
3. **Should V3-EXQ-981 be re-adjudicated** on the environment-vs-readout attribution (section 11)?
   A governance decision, deliberately not taken here.


## Red-team pass (Step 7c) and revision -- 2026-09-04T14:50:27Z

**Reviewer:** Fable 5.1 (separate agent, reasoning withheld, JSON-first). **Verdict: CONTESTED. Contest ACCEPTED on all six findings** by the confirming governance session (governance-20260904-1347).

- **F1 (mechanism relocated).** The draft's "no signal/noise asymmetry; a perfect avoider scores 0" was wrong: its oracle was an always-respond policy, which scores d'=0 in any SDT task. A CONDITIONAL avoider (flee iff HIGH, else random) scores +0.905 and PASSES the +0.05 gate. The real defect is **action HOLD x geometry**: E3 decides every P steps (the IV) while the readout scores every step, and SAFE is only reachable walking away / HIGH only walking toward -- the same conditional oracle held at P=10 collapses to +0.038. 981's per-bin rates (SAFE 0.87-0.89, HIGH 0.10-0.27) are exactly the held-walker signature.
- **F2 (DV-IV confound).** sensitivity(P) is monotone in P under a hazard-blind null (-0.23 -> -0.60) and noise under a perfect discriminator; C1 is confounded with the IV for ANY agent. 999a as first specified could not test MECH-161; the readout must be scored at E3 decision ticks (hold-invariant).
- **F3.** The headline "oracle cannot pass" does not reproduce at the driver's 20-episode budget (seed 23: SAFE n=0 -> rate 0.0 -> +1.0, passes); P0 never gates on `coverage_ok`.
- **F4 (routing).** The substrate `create` was incoherent: driver-file `substrate_paths` can never match the Step 2.5c import gate, and `corrupting` failed the skill's definition (both uses caught by P0; nothing invalidated). `dv-dynamic-range-precondition-class` (pending, degrading, MECH-027, cites 981) already owns the failure class -> **amend** it with the 999 instance, unblocks_claims += MECH-161.
- **F5.** The 981 read-across is a relabel of the same signature, not a contradiction; 981's confirmed disposition stands.
- **F6.** The three fan-out legs were pre-bound to one run id; H2/H3 now get their adjudicating runs at queue time.
- **Survived:** FAIL on the absolute/precondition criterion; `non_contributory` + `standard`; brake 0; 2-of-2 driver family failing the same control; no action policy trained on harm; 999a letter defensible; driver hash matches the landed file.

Withdrawn readings retained under `withdrawn_readings_2026_09_04` in the JSON. Routing: `/queue-experiment` V3-EXQ-999a with the corrected non-negotiables (`routing_note_2026_09_04`), shared with the open 981a re-queue chip.


## Confirmation -- 2026-09-04T18:55:13Z

Status **confirmed** at the /governance Step 8 gate (session governance-20260904-1347, user present). Decisions: {"Q1": "Apply all four as revised", "Q2_SD031_gate": "Amend SD-031 what_would_answer + self_attribution GAP-6 to accept construction-balanced (RandomPolicy, offline-scored) comparator-only designs for the ARC-065 diversity half", "Q3": "Add 6 buildable v3 substrate stubs", "Q4": "Apply the three August staging-autopsy ledger blocks now", "recommendation_agreement": "3 of 4 recommended options selected (Q4 against); logged via record_recommendation_outcome.py"}
