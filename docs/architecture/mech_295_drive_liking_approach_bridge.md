# MECH-295: Drive -> Liking-Stream -> Approach Cue Bridge

**Claim ID:** MECH-295
**Subject:** drive_to_approach.liking_stream_bridge
**Status:** IMPLEMENTED (V3 substrate landed 2026-04-26)
**Reading commitment:** WEAK necessity (provisional)
**Registered:** 2026-04-26
**Implemented:** 2026-04-26
**Depends on:** SD-012, SD-014, SD-015, SD-016, MECH-117, ARC-036
**Blocks:** EXQ-483 catatonic-lock recovery; downstream behavioural validation of the V3 motivational stack

## Functional restatement

```
drive_level (SD-012)
   ->
liking_gain on goal-congruent outcome predictions
   ->
approach_cue_signal at action selection (E3 / BG)
```

The bridge is the missing wiring between SD-012 drive amplification, the SD-014 / SD-015 liking-stream substrate, and E3 / BG action selection. Without this bridge, drive amplification produces a passive `z_goal` latent without behavioural consequence -- the EXQ-483 catatonic-lock signature: override_signal climbs to mean 0.563, PAG release ratio ON_ON / ON_OFF = 1.69, but `approach_commit = 0.0` across all four arms.

## Strong vs weak reading

The lit-pull (`evidence/literature/targeted_review_mech295_liking_approach_bridge/SYNTHESIS.md`) cleanly motivates the architecture but does not arbitrate two readings of necessity:

- **Strong necessity:** elevated approach_commit requires elevated liking-stream activation (level-coupled).
- **Weak necessity:** baseline liking-stream activation is sufficient, but the bridge wiring must be intact -- if the link is severed, drive amplification produces no approach regardless of drive magnitude.

The DAT-knockdown finding (Pecina 2003: more wanting, unchanged liking) is incompatible with the strong reading but compatible with the weak reading. **MECH-295 commits to the WEAK reading provisionally.**

This V3 substrate implements the weak reading. The cue-side gain is a function of `drive * goal_proximity` -- the "is the bridge intact?" surface, not `drive * residue.liking` which would be the level-coupled strong reading. Setting `mech295_liking_to_approach_cue_gain=0.0` is the **severed-bridge** arm of the falsifiable test.

## Architecture

### Module

`ree-v3/ree_core/regulators/mech295_liking_bridge.py`:

- `MECH295LikingBridgeConfig` -- four sub-knob dataclass.
- `MECH295LikingBridge` -- pure arithmetic, no trainable parameters. Two compute methods:
  - `compute_anticipatory_liking_write(drive_level, z_goal_norm, simulation_mode)` -> scalar magnitude for the anticipatory liking write at the goal location.
  - `compute_approach_cue_score_bias(drive_level, candidate_proximities, simulation_mode)` -> per-candidate negative score_bias (E3 lower-is-better, so liking favours approach by reducing the score).
- `MECH295LikingBridgeOutput` -- diagnostic dataclass.
- `tick(drive_level, z_goal_norm, candidate_proximities, simulation_mode)` -- convenience orchestration helper that calls both compute methods and caches diagnostics. The agent normally calls the compute methods separately at their respective integration sites; `tick` exists for the contract tests and direct callers.

### Integration sites

Two integration sites in `ree-v3/ree_core/agent.py`:

#### (a) Anticipatory liking write -- `update_z_goal()`

After the existing SD-012 / SD-037 `effective_drive` computation and `GoalState.update()` call:

```python
if (
    self.mech295_bridge is not None
    and self.goal_state is not None
    and self.goal_state.is_active()
    and hasattr(self.residue_field, "update_valence")
):
    z_goal_norm = self.goal_state.goal_norm()
    write_value = self.mech295_bridge.compute_anticipatory_liking_write(
        drive_level=effective_drive,
        z_goal_norm=z_goal_norm,
        simulation_mode=False,
    )
    if write_value > 0.0:
        self.residue_field.update_valence(
            self.goal_state.z_goal,         # write at GOAL location
            component=VALENCE_LIKING,
            value=write_value,
            hypothesis_tag=False,
        )
```

This is the anticipatory cue-side pulse, distinct from the existing consummatory-contact write in `REEAgent.update_liking(benefit_exposure)` (which writes at the agent's current `z_world`, not at the goal). Both write paths target VALENCE_LIKING in the SD-014 valence vector but at different locations and from different mechanisms.

#### (b) Approach cue at action selection -- `select_action()`

After the lateral_pfc + ofc score_bias composition, before `e3.select()`:

```python
if (
    self.mech295_bridge is not None
    and self.goal_state is not None
    and self.goal_state.is_active()
    and self._current_latent is not None
):
    # Build per-candidate first-step z_world summaries (reuse from
    # lateral_pfc / ofc blocks if available, else build fresh).
    m295_summaries = ...   # [K, world_dim]
    with torch.no_grad():
        cand_proximities = self.goal_state.goal_proximity(m295_summaries).detach()
        base_drive = float(getattr(self.goal_state, "_last_drive_level", 0.0))
        eff_drive_m295 = (
            self.pacc.effective_drive(base_drive)
            if self.pacc is not None else base_drive
        )
        m295_bias = self.mech295_bridge.compute_approach_cue_score_bias(
            drive_level=eff_drive_m295,
            candidate_proximities=cand_proximities,
            simulation_mode=False,
        )
    if dacc_score_bias is None:
        dacc_score_bias = m295_bias
    else:
        dacc_score_bias = dacc_score_bias + m295_bias.to(...)
```

The pACC sensitisation is applied so the cue side sees the same effective drive that the write side used (no double counting -- the write side already received `effective_drive` post-pACC).

### Computation

#### Write side (anticipatory liking)

```
if simulation_mode or drive_to_liking_gain == 0.0:
    return 0.0
if drive_level < min_drive_to_fire:                  return 0.0
if z_goal_norm < min_z_goal_norm_to_fire:            return 0.0
return drive_to_liking_gain * drive_level * z_goal_norm
```

#### Cue side (per-candidate score_bias)

```
if simulation_mode or liking_to_approach_cue_gain == 0.0:
    return zeros([K])
if drive_level < min_drive_to_fire:
    return zeros([K])
liking_signal = drive_level * candidate_proximities.clamp(0, 1)
return -liking_to_approach_cue_gain * liking_signal      # NEGATIVE
```

Note that the cue side fires on `drive * candidate_proximities` directly, NOT on the residue-field VALENCE_LIKING readout. This is the weak-reading commitment: baseline liking-stream activation is sufficient; the bridge does not require the level-coupled write to produce the cue. The `drive_to_liking_gain` only controls the anticipatory write magnitude, which is observed downstream (residue field, replay prioritisation via SD-014 drive-weighted priority).

## Configuration

`REEConfig.use_mech295_liking_bridge` (master, default `False`). Sub-knobs:

| Sub-knob | Default | Purpose |
|----------|---------|---------|
| `mech295_drive_to_liking_gain` | 1.0 | Multiplier on `drive * z_goal_norm` for the anticipatory write. Set 0 to disable the write side without touching the cue side. |
| `mech295_liking_to_approach_cue_gain` | 0.5 | Multiplier on per-candidate liking signal for the score_bias. Set 0 to **sever** the cue side without touching the write side. |
| `mech295_min_drive_to_fire` | 0.1 | Drive floor. Below this, both sides are silent. |
| `mech295_min_z_goal_norm_to_fire` | 0.05 | Goal-norm floor for the write side. |

All wired through `REEConfig.from_dims()`.

## Backward compatibility

Master flag default `False`; `agent.mech295_bridge` is `None`; both integration sites are no-ops. **154/154 contracts + 7/7 preflight PASS with flag OFF** (bit-identical to pre-MECH-295 HEAD, 2026-04-26).

With master flag ON but both gain knobs at zero (`mech295_drive_to_liking_gain=0.0`, `mech295_liking_to_approach_cue_gain=0.0`), the bridge runs but produces zero write and zero score_bias -- still bit-identical to OFF for action selection.

## MECH-094

`simulation_mode` argument is honoured at both compute methods. When `True`:
- write returns `0.0`,
- cue returns zero score_bias,
- internal counters do not advance.

The agent calls the compute methods only on waking paths (`update_z_goal` from the experiment loop, `select_action` from the agent loop), passing `simulation_mode=False`. Replay / DMN paths must not route through these call sites; this is the same call-site-scoping pattern used by MECH-269 / MECH-287.

## Falsifiability

Two falsifiable predictions:

### Primary (weak reading)

A V3 factorial with the drive -> liking link intact vs severed (under matched `drive_level`) should show `approach_commit` recovers when the bridge is intact and collapses when severed. Operationally:

- Arm A (severed, control): `use_mech295_liking_bridge=True`, `mech295_drive_to_liking_gain=1.0`, `mech295_liking_to_approach_cue_gain=0.0`. Bridge wired but cue side cannot reach E3.
- Arm B (intact): `use_mech295_liking_bridge=True`, `mech295_drive_to_liking_gain=1.0`, `mech295_liking_to_approach_cue_gain=0.5`.

Prediction (weak reading): under matched drive elevation, Arm B `approach_commit_count > 0` while Arm A `approach_commit_count = 0` (or substantially lower).

### Secondary (strong-reading test)

Pharmacologically-inspired manipulation: block the hedonic-hotspot mu-opioid analog in the V3 substrate while drive is elevated. Under the strong reading, `approach_commit` collapses. Under the weak reading with intact bridge, `approach_commit` recovers via baseline liking. **Substrate not yet built** -- this is a future EXQ.

## Acceptance for V3-EXQ-493

V3-EXQ-493 is a six-part substrate-landing diagnostic (queued 2026-04-26). All sub-tests must PASS:

- **UC1 module-importable** -- `regulators.mech295_liking_bridge` importable.
- **UC2 master-OFF no-op** -- agent built with default config has `mech295_bridge is None`.
- **UC3 write-side fires** -- 30-tick env loop with forced drive=0.8 + benefit=0.4 -> `n_write_fires > 0`.
- **UC4 cue-side negative bias** -- `compute_approach_cue_score_bias(drive=0.6, prox=[0.1, 0.5, 0.9])` returns negative tensor with monotone proximity dependence.
- **UC5 severed-bridge collapse** -- with `liking_to_approach_cue_gain=0.0` and `drive_to_liking_gain=1.0`, cue-side bias is exactly zero even at `drive=0.9`; write side STILL fires. This is the falsifiable signature for the weak-necessity reading.
- **UC6 MECH-094 simulation gate** -- `simulation_mode=True` -> zero on both sides, counters do not advance.

**PASS = all 6 UCs PASS.** Smoke verified all 6 PASS via `--dry-run` on 2026-04-26.

## Behavioural validation (deferred)

Behavioural EXQ-483-style approach_commit recovery (4-arm with the orexin substrate ON plus this bridge in arms 2-3, measuring approach_commit recovery against the EXQ-483a all-zero baseline) is deferred to a successor EXQ once V3-EXQ-490 (MECH-269b) lands. The combined V_s rollout gating + drive -> liking -> approach bridge stack will be tested together; the Q-040 factorial structure already cross-points to MECH-295 as the dominant blocker if MECH-269b alone fails to recover approach.

## Biological grounding

Substrate evidence and architectural articulation, anchored in the lit-pull (`evidence/literature/targeted_review_mech295_liking_approach_bridge/`):

- **Pecina & Berridge 2005** (J Neurosci, doi:10.1523/JNEUROSCI.3331-05.2005) -- anatomical hedonic hotspot in NAc shell.
- **Castro & Berridge 2014** (Phys Behav, doi:10.1016/j.physbeh.2014.02.063) -- decade of hotspot mapping consolidated.
- **Smith Berridge & Aldridge 2011** (PNAS, doi:10.1073/pnas.1101920108) -- VP single-unit recording: drive change recodes palatability before cue firing. The strongest direct mechanistic anchor.
- **Berridge & Kringelbach 2015** (Neuron, doi:10.1016/j.neuron.2015.02.018) -- architectural articulation of liking as a necessary input to motivated approach, not a passive readout.
- **Dickinson & Balleine 1994** (Animal Learn Behav, doi:10.3758/BF03209866) -- foundational behavioural demonstration: drive-state shifts do not directly rewire action selection; they must route through experienced hedonic value of the outcome.
- **Pecina et al. 2003** (J Neurosci, doi:10.1523/JNEUROSCI.23-28-09395.2003) -- DAT-knockdown: more wanting, unchanged liking. The structural caution that constrains MECH-295 to the WEAK reading.

The cleanest direct test of MECH-295's necessity claim (mu-opioid antagonist in NAc shell hotspot + hunger + cue-approach) does not exist in the literature in a single paper. This is an experimental gap that the V3 substrate is designed to probe directly.

## Related claims

- **SD-012** -- homeostatic drive (the input).
- **SD-014** -- valence vector substrate (VALENCE_LIKING component is the write target).
- **SD-015** -- z_resource encoder (upstream of GoalState.update; goal-congruent surface depends on this seeding).
- **SD-016** -- frontal cue-indexed integration (cue_action_proj reads z_world; complementary to MECH-295 at the cue side but not redundant).
- **MECH-117** -- existing wanting/liking dissociation in REE (`benefit_eval_head` vs `z_goal_latent`). MECH-117 specifies the dissociation; MECH-295 specifies the necessity-chain that must hold for behavioural output.
- **ARC-036** -- hedonic hotspot anatomical substrate (prerequisite for the architectural claim).
- **MECH-094** -- call-site scoping + `simulation_mode` argument honour.
- **SD-037** -- broadcast override regulator. The bridge consumes `effective_drive` after SD-037's `override_goal_seeding_gain` amplification has already been applied in `update_z_goal()`.
- **MECH-269b** -- complementary candidate cause for EXQ-483 wired-but-inert. Q-040 factorial points evidence at MECH-295 if MECH-269b alone fails to recover approach_commit.
