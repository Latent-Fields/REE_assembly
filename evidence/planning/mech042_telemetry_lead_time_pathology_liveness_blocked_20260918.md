# MECH-042 sub-claim (2) -- pathology liveness measurement and substrate refusal

- **Date:** 2026-09-18
- **Session:** `igw-245-proposal-for-mech-042` (IGW-20260918-245)
- **Claim:** MECH-042 -- "Telemetry exposure channels report internal control-plane state for diagnostics."
- **Proposal:** `EVB-1407` / `EXP-0790` (experimental lane) -> **`blocked_substrate`**
- **Predecessor record:** `GFLAG-0335` (2026-09-17), `ree-v3` `b93374e`
- **Outcome:** sub-claim (2) is NOT queued. The refusal is **claim-internal** -- MECH-042's own
  pre-registered non-degeneracy precondition is what fails, not an invented bar.

---

## 1. What was already settled before this session

MECH-042 has two CONFIRMING sub-claims, both required, and its own 2026-09-16 disposition splits
them by artifact type:

- **Sub-claim (1) READ-ONLY / NON-PARTICIPATION -- LANDED, needs nothing further.**
  `ree-v3/tests/contracts/test_mech042_telemetry_readonly_nonparticipation.py`, 5 checks,
  mutation-tested before landing (injecting one `torch.rand(1)` into the read path breaks C1/C2),
  so its green is not vacuous.
- **Sub-claim (2) DEVELOPMENTAL-SAFETY LEAD TIME -- was authored as V3-EXQ-1053, smoke-tested, and
  REFUSED at `/queue-experiment` Step 4.5** on a BLOCKING red-team verdict. Driver committed
  unqueued with a DO-NOT-QUEUE header; slot closed `--not-landed`.

`GFLAG-0335` recorded four verified blockers and stated the owed work:

> OWED: repair (1)-(4) and re-run Step 4.5 before queueing sub-claim (2).

**This session's finding is that blocker (1) is not repairable on the current substrate, and that
the requirement it belongs to is unsatisfiable.** Blockers (2), (3) and (4) *are* repairable
(dependency-closure exclusion, a fixed observation horizon, and out-of-sample threshold
calibration respectively); they are not the reason for the refusal and are recorded in section 5
so a successor does not rediscover them.

## 2. The requirement that cannot be met

MECH-042's `what_would_answer` pre-registers, for sub-claim (2):

> a pre-registered detector on the telemetry stream flags it with POSITIVE lead time over a
> matched detector on the behaviour stream (harm / reward), sign-consistent across **>=3 seeds and
> >=2 pathology types**

and makes behavioural manifestation a **non-degeneracy precondition**:

> the injected pathology must eventually MANIFEST behaviourally (harm rate or reward departs from
> control within the life), **otherwise lead time is undefined**.

So a pathology that does not manifest behaviourally cannot contribute a lead time *by the claim's
own terms*. The claim names four candidate pathologies. **Only one of the four manifests on the
current substrate**, so the ">=2 pathology types" clause cannot be satisfied under any outcome.

## 3. The measurement

Direct probe, `REEConfig.from_dims` at the driver's own operating config
(`size=10, num_hazards=3, num_resources=6, use_proxy_fields=True`, `alpha_world=0.9`,
`use_commit_readiness=True`, `use_salience_coordinator=True`, `use_dacc=True`), seed 0, fixed
150-tick horizon, injection held from tick 60. Each arm compared against a CONTROL run that is
identical up to the injection. `act_div` = number of ticks whose committed action differs from
CONTROL. Telemetry surface = the nine MECH-042 channels.

| Pathology (claim's own wording) | Injection used | `act_div` | harm mean (CONTROL `-0.0125`) | max abs telemetry delta | Verdict |
|---|---|---|---|---|---|
| precision collapse via `recalibrate_precision_to` | `recalibrate_precision_to(0.01, step=1.0)` | **83** | `-0.0166` | precision `200.9`, running_variance `100.0`, `beta_elevated` `1.0`, `e3_steps_per_tick` `7.0`, `salience_mode_prob` `0.278`, `residue_coverage_pct` `0.0625` | **LIVE** |
| stuck commit latch via an unreachable release | `commit_readiness._readiness = 0.0` | **0** | `-0.0125` | `readiness` `1.0`, every other channel `0.0` | INERT |
| stuck commit latch, **gate explicitly enabled** | as above + `use_commit_readiness_gate=True` (default `False`) | **0** | `-0.0125` | `readiness` `1.0`, every other channel `0.0` | INERT |
| mode lock via SalienceCoordinator switch threshold | `set_enter_threshold(m, 999.0)` for every **real** mode name | **0** | `-0.0125` | **every channel `0.0`** | INERT |
| residue overgeneralisation via kernel bandwidth | `rbf_field.bandwidth = 8.0` | 84 | `-0.0125` | precision `0.0046`, `salience_mode_prob` `0.0011`, rest `0.0` | NEAR-INERT |
| residue bandwidth, opposite direction (control) | `rbf_field.bandwidth = 0.02` | 84 | `-0.0125` | precision `0.0054`, `salience_mode_prob` `0.0012`, rest `0.0` | NEAR-INERT |

Three of these deserve comment, because each is a *different* reason for inertness:

- **Mode lock is inert even though the injection DEMONSTRABLY ENGAGED.** The mode set visited
  collapsed from `{external_task, internal_planning}` under CONTROL to `{external_task}` under the
  lock -- transitions really were suppressed -- and yet **every one of the nine telemetry channels
  moved by exactly `0.0` and not one action changed.** This is a stronger and independent
  confirmation of `GFLAG-0335`'s blocker (1): that session found the injection wrote dead keys
  (`SalienceCoordinatorConfig.enter_thresholds` is `field(default_factory=dict)` and `agent.py`
  never populates it, so a `{"focused","diffuse"}` fallback fired while the real names are
  `external_task` / `internal_planning` / `internal_replay` / `offline_consolidation`). Using the
  **correct** names fixes the injection and the arm is *still* a second control -- because
  `operating_mode` has no effective live consumer. Independently recorded:
  `DEFAULT_GATE_WEIGHTS` registers only `sd_033a..d` / `hc_viability` / `sensory_buffer` /
  `autonomic` / `e3_policy`, and `residue_field.accumulate()` and `e2_harm_s` are ungated. Open
  unclaimed chip `chip-20260917-sd032a-operating-mode-no-consumer` owns the general gap.
- **The commit latch is inert with the gate ON as well as OFF.** `use_commit_readiness_gate`
  defaults to `False` (`config.py:3328`), which alone would explain an inert arm; setting it
  `True` and pinning `_readiness = 0.0` (below `commit_readiness_floor = 0.05`) still yields
  `act_div = 0`. The readiness scalar is computed and exposed as telemetry but does not gate
  behaviour at this operating point. **This is a new finding, not previously recorded.**
- **Residue bandwidth is near-inert in BOTH directions, which is the diagnostic shape.** An arm
  that moves selection (84 divergences) while leaving harm exactly at the control value and the
  residue telemetry channels at `0.0` is not a behavioural manifestation. The cause is already
  recorded from 2026-09-17 (`mech023_residue_geometry_substrate_blocked_20260917.md`): the kernel
  bandwidth `1.0` is ~8x the reachable `z_world` manifold (max pairwise distance `0.1249`), so the
  field is already spatially near-uniform and *widening* it is close to a no-op. Both directions
  were run precisely so that "no effect" could not be read as a one-sided threshold artifact.

## 4. Verdict

**C1 ("positive lead time, sign-consistent across >=3 seeds and >=2 pathology types") cannot
discriminate under any outcome**, because only one of the four claim-named control-plane
pathologies manifests behaviourally, and the claim itself declares lead time undefined for the
others. Queueing a run anyway would produce a `substrate_not_ready_requeue` / `precondition_unmet`
artifact at best, and at worst a spurious PASS resting on a single pathology.

This is **not** a re-derivation of the conversion / F-dominance ceiling. It is a specific,
separately-actionable fact about the control plane: **three of its four injectable pathologies
have no live consumer**, so the control plane cannot currently be perturbed in more than one way.

Node class: `complicated (buildable)` -- every gap below is a build, not an unknown. Route is
`/implement-substrate`, not another lettered experiment.

## 5. Release condition, and what a successor should NOT rediscover

**Release condition:** at least TWO of MECH-042's named control-plane pathologies demonstrably
manifest behaviourally (harm rate or reward departs from control within the life) at the operating
config under test. Concretely, any one of these three unblocks it by supplying a second live
pathology:

1. `operating_mode` gains a live consumer on a path the behavioural DV depends on
   (`mode-governance-engagement` switching half; SD-032a / MECH-266 / MECH-261; chip
   `chip-20260917-sd032a-operating-mode-no-consumer`).
2. `CommitReadiness` readiness gains an effective behavioural consumer -- i.e. pinning readiness
   below `commit_readiness_floor` with `use_commit_readiness_gate=True` actually changes committed
   actions. **Currently unowned; this document is its first record.**
3. `residue-field-kernel-resolution` lands (bandwidth brought to a scale where the field is not
   near-uniform), making a bandwidth perturbation a real manipulation. Already owed via
   `GFLAG-0337` / `mech023_residue_geometry_substrate_blocked_20260917.md`.

**Repairs already worked out for blockers (2)-(4), so they are not redone from scratch:**

- **(2) injected-channel exclusion is incomplete.** Excluding only the injected channel is not
  enough: `recalibrate_precision_to` hard-sets `_running_variance`, and
  `committed = commit_variance < effective_threshold` reads that *same* variable
  (`e3_selector.py:3843-3847`, confirmed this session), so the retained channel `is_committed` is
  the arithmetic identity `1[injected < threshold]` and `beta_elevated` inherits it. The fix is to
  exclude the whole **arithmetic dependency closure** of the injected variable, pre-registered per
  pathology -- for precision collapse that is `{precision, running_variance, is_committed,
  beta_elevated}`.
- **(3) lead time is censored at an outcome-dependent n.** `StepHarness.run_episode` breaks on
  `r.done` (`_harness.py:465`), so tick count is an OUTCOME of the manipulation and
  `lead = n - t_telemetry` rewards a cell that merely survives longer. The fix is a **fixed global
  tick horizon** -- keep resetting the env until a pre-registered budget H is reached, so every
  cell contributes exactly H ticks and both detectors are censored at the same H. Additionally,
  the load-bearing criterion should count only cells where the behaviour detector actually fired,
  which removes censoring from the load-bearing path entirely.
- **(4) the matched-false-alarm gate cannot fail.** `tau` is the 0.95 quantile of a series and the
  FA rate is then measured on that same series, so both sides equal `~floor(0.05(m-1))/m` by
  arithmetic -- the claim's own named degeneracy guard is inert. The fix is **out-of-sample
  calibration**: split the control arm's post-baseline window, calibrate `tau` on one half and
  measure FA on the other. The tau must also be calibrated on a control statistic computed with
  **the same exclusion set (hence the same column count)** as the pathology arm it will be applied
  to; the refused driver calibrated on a 9-column control statistic and applied it to 7- and
  8-column pathology statistics.

**Also worth keeping:** a per-arm "this arm diverges from CONTROL" precondition would have caught
blocker (1) mechanically rather than by red-team inspection, and should be standard in any
injected-pathology design.

## 6. Substrate-path overlap (Step 2.5c), disposed

`substrate_queue.json` lists **SD-082** as `severity: corrupting` with `substrate_paths` including
`ree_core/predictors/e3_selector.py`, which `agent.get_state()` reads. Disposed of as **NOT
REACHABLE**, on this session's own reading rather than by inheriting the predecessor's call:
SD-082's defect is the SD-078 rule-state -> action-bias coupling in
`lateral_pfc_analog.py::compute_bias`, reached only via `lateral_pfc_rule_readout_consumer` (a
no-op default flag this work never enables) and `_lpfc_reinforce_loss` (never imported here).
SD-082's own `severity_note_2026_09_09` records that `substrate_paths` was **deliberately emptied**
because the defect is RESOLVED (822c fix landed `ree-v3 ef88faa`, 822d confirmed the amend
engaged), and `governance_2026_09_15` and `governance_2026_09_16` both assert `substrate_paths ==
[]`; the live non-empty value contradicts all three. That inconsistency is already raised as
**`GFLAG-0333`** and is not re-raised here.

## 7. Lanes

- `EXP-0790` (experimental) -> `blocked_substrate`.
- **`LIT-0791` (literature_review) is deliberately left `proposed`.** MECH-042's `why_now`
  includes `missing_literature_evidence`, and the literature lane is not affected by this
  substrate gap. Per the `(backlog_id, proposal_type)` identity rule, only the `experimental` row
  was written.
