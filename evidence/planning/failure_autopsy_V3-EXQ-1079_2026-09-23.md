# Failure autopsy -- V3-EXQ-1079 (SD-PP-B10 test 1, alpha_world operating-point probe)

- **run_id**: `v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3`
- **queue_id**: V3-EXQ-1079 · **outcome**: PASS · **purpose**: diagnostic · **claim_ids**: `[]`
- **bears_on**: SD-PP-B10, SD-PP-B5, MECH-573, MECH-574, INV-063, MECH-582, SD-008
- **Adjudicated by**: governance cycle `governance-pause-20260923-1741`, inline under /governance Step 1.5 route A
- **Red-team (Step 7c)**: CONTESTED, cross-model (fable; session model Opus 5). Four findings adopted; each independently re-verified before adoption.

## 1. Why this run exists

V3-EXQ-1073 and V3-EXQ-1075 never set `alpha_world`, so both inherited `REEConfig.from_dims`'
default of 0.3 (`ree_core/utils/config.py:7562`; EMA at `ree_core/latent/stack.py:1584`) against
SD-008's stable floor of >= 0.9. SD-PP-B5's governance-ratified validated-NEGATIVE verdict
(cycle `governance-20260923-0717`) rests on those two runs. GFLAG-0433 raised the operating-point
problem; GFLAG-0434 raised that the action-blind null they rest on is an EMA warm-up artifact.

## 2. What the run found -- the verdict STANDS

Pre-registered route GROWS, 3/3 seeds, label `alpha_world_amplifies_present_action_read`.
Paired row bootstrap (512 rows, 2000 resamples) on `d_act(0.9) - d_act(0.3)`:

| seed | delta | CI | PC delta | rows aligned | instrument live |
|---|---|---|---|---|---|
| 42  | +0.3228 | [0.2846, 0.3601] | +0.1528 | yes | yes |
| 123 | +0.1627 | [0.1407, 0.1857] | +0.0592 | yes | yes |
| 456 | +0.2636 | [0.2356, 0.2919] | +0.1831 | yes | yes |

All four pre-registered preconditions met. The verdict is ROBUST: `d_act(0.9) > d_act(0.3)` in
every 64-row block of every seed. `d_act`'s null is genuinely ANALYTIC -- verified in code, since
`_swap_errors` averages the ERRORS over the four alternative actions rather than the predictions,
so there is no Jensen term, and the recorded random-init head sits at |d| <= 0.022 in all 9 cells.

**Raising alpha_world from 0.3 to 0.9 really does increase the head's action read.** That much is
solid, and it confirms GFLAG-0433's premise as MEASURED: per-step z_world displacement is 3.0-3.1x
larger at 0.9 (`rms_dz_per_dim` 0.0073-0.0086 -> 0.0228-0.0261).

## 3. Three readings that did NOT survive the red-team

### 3a. The head does NOT improve with alpha -- the persistence flip is baseline-driven

`persistence_relative_skill` goes -0.2335/-0.0748/-0.3019 at alpha 0.3 to +0.2429/+0.1303/+0.1992
at 0.9, which reads as the head becoming competent. It is not:

| alpha | persistence_r2 (42/123/456) | model_r2 (42/123/456) |
|---|---|---|
| 0.3 | 0.9272 / 0.9324 / 0.9352 | 0.8828 / 0.9214 / 0.8792 |
| 0.9 | 0.5480 / 0.5835 / 0.5553 | 0.7247 / 0.6795 / 0.7030 |

`model_r2` FALLS on 3/3 seeds. Less EMA smoothing makes copy-the-input a much worse predictor; the
head is an absolutely WORSE predictor at 0.9 and merely loses by less. `skill_vs_identity_1075_order`
stays NEGATIVE at every alpha (-5.82/-2.24/-8.39 at 0.3; -2.14/-2.08/-2.68 at 1.0).

### 3b. The battery is non-stationary, on a DEAD agent

Governance re-probe (seeds 42/123/456, driver env params `size=5 num_hazards=1 num_resources=3`):
the agent dies of `health_depleted` at step **32 / 27 / 22** after `env.reset()`, and
`|world_state|` accrues without bound -- 5.9 at step 31, 8.5 at 100, 21.2 at 300, 39.7 at 600.

The driver **never reads `done`**: `env.step()` returns `(flat_obs, harm_signal, done, info,
obs_dict)` and both `_collect_battery` (:330) and the P0 loop (:499) take `out[-1]`, discarding
`out[2]`. With `BURN_IN_STEPS = 30`, **every one of the 512 battery rows is post-death.** The
driver's own docstring (:147) records this as *inherited unchanged from V3-EXQ-1075*.

Governance recompute of `d_act` from `per_row_se_*` at alpha 0.3:

| rows | seed 42 | seed 123 | seed 456 |
|---|---|---|---|
| 0-63 (the 1075-comparable window) | **-0.0762** | +0.0556 | **-0.0321** |
| 64-511 | +0.1991 | +0.2384 | +0.2577 |
| 448-511 | +0.4049 | +0.2964 | +0.2903 |

### 3c. So GFLAG-0432's conclusion is regime-dependent, not merely mis-evidenced

GFLAG-0432 argues the trained OFF head "already reads its action" because 0.8331/0.8790/0.7068
leads a measured blind null by 0.20-0.30. Against the corrected burn-in null the head sits BELOW on
3/3. And the fallback conclusion (that `d_act` at 0.3 is positive) holds only on the full drifted
battery: on rows 0-63 it is NEGATIVE on 2 of 3 seeds. The remedy is therefore **not** a better
measured null -- any measured null on this battery inherits the drift -- but an analytic null AND a
fixed battery.

## 4. Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | n/a -- `claim_ids: []` by design |
| Biological reference | n/a -- instrument/operating-point probe |
| Prerequisites | present -- all 4 pre-registered preconditions met |
| Implementation | complete -- ARM_OFF re-run of the landed 1075 driver; substrate_commit `a906c8a24c`, clean |
| Environment | **wrong pressures** -- battery collected from a dead agent, `done` never read |
| Measurement | **misleading** -- analytic null is sound, but the DV is strongly non-stationary |
| Integration | coupled -- manipulation moves the DV monotonically, PC live 3/3 |
| Scale | adequate in row count, NOT in independence (one ordered trajectory) |

**Failure location (GOV-FAILLOC-1): MIXED -- MEASURES + ENVIRONMENT.** Not chargeable to REE and
not to the mechanism.

## 5. Consequence for SD-PP-B5: QUALIFY, do not re-open

The validated-negative is **not a clean negative** -- both runs behind it ran at a damped operating
point violating SD-008 and on the dead-agent battery. But nothing here shows the manipulation
works: the head's absolute predictive quality falls with alpha and it remains below the identity
predictor at every alpha tested. So the verdict is qualified and its basis recorded, not reversed.

## 6. Routing

1. **/queue-experiment** -- re-validate the SD-PP-B5 question at `alpha_world >= 0.9` on a battery
   that resets on `done`. A NEW question, not a lettered re-run of 1075.
2. **Shared instrument defect** -- the dead-agent battery affects at least V3-EXQ-1073/1075/1079.
   Its corpus reach is NOT established here and is raised to the user as a scoping decision.

Any re-validation must report `model_r2` alongside any persistence-relative skill, so a baseline
collapse can never be read as head improvement.

## 7. Addendum (2026-09-24, GFLAG-0448) -- the dead-agent battery does NOT apply to V3-EXQ-1073
Section 6 item 2 (and, in the JSON, net_classification, implementation_hint and the SHARED INSTRUMENT DEFECT finding) say V3-EXQ-1073 also collected its battery after the agent died without reading `done`. That is FALSE for 1073: its _sample_probe_battery and P0 loop unpack `done` and reset (ree-v3 experiments/v3_exq_1073_mech572_precision_provenance_gain.py:1054-1057, 1170-1175, 1422-1426). The post-death defect applies to V3-EXQ-1075 and V3-EXQ-1079 only -- this driver's docstring records inheritance from 1075, and the extension to 1073 was not verified. Consequence for SD-PP-B5: of the two runs its validated-negative rests on, only 1075 carries the dead-agent defect; BOTH still ran at alpha_world 0.3 (unchanged, correct). SD-PP-B5's validation_outcome carries the matching correction (REE_assembly 65bb05ec9c). Found by failure_autopsy_V3-EXQ-1082_2026-09-24 sec. 2.
