---
title: Effort-Dissociating Environment (Q-080)
parent: "Development & Curriculum"
grandparent: Architecture
nav_order: 8
---

# Effort-Dissociating Environment (Q-080)

**Type:** environment feature (NOT a mechanism / SD claim — no claim ID minted).
**Subject:** `environment.effort_dissociation`
**Status:** IMPLEMENTED 2026-07-09.
**Serves:** open_question **Q-080** (`ethics_engine_3.effort_as_harm_energy_conservation`),
specifically the two load-bearing sub-questions **Q-080.a** (harm-coupling) and **Q-080.b**
(least-effort prior). Q-080.c (MECH-454 energy-grounding) is a separate follow-on blocked on
MECH-454's own unbuilt substrate and is NOT served here.
**Depends on:** SD-005 (obs split), SD-011 (z_harm_a / harm_obs_a), SD-012 (homeostatic
drive / energy currency), `use_proxy_fields` (CausalGridWorldV2 proxy mode).

---

## Why this env exists

Q-080 asks whether wasted/excessive **effort** is a **harm** in REE (routed into the
residue / allostatic / irreversibility-aware stream, with energy-conservation as an
evolutionarily-primary least-effort prior) — or only a **foregone value** (already handled
by the dACC EVC effort-cost term SD-032b, MECH-320/ARC-068 opportunity-cost, and the pACC
allostatic load SD-032e). That question is **untestable** until an environment
**dissociates effort from benefit**. REE's default `CausalGridWorld` energy channel decays
at a flat `energy_decay` per step regardless of action — effort and benefit are entangled.

This feature adds a deterministic layout in which two paths of **equal length** reach the
**same benefit** at **measurably different per-action energy cost**, plus a chronic-exertion
regime that can deplete (reversibly and irreversibly). It is the substrate the Q-080
resolution path called for; it mints **no mechanism** — the factorial ablations it hosts are
what answer Q-080.

## Non-degeneracy requirements (all satisfied; else a run self-routes `substrate_not_ready_requeue`)

1. **The two paths differ measurably in per-action energy cost.** A per-cell effort-cost
   grid gives the HIGH corridor an `effort_high_multiplier`x (default 3x) per-action energy
   drawdown vs the LOW corridor of **equal length** (same step-count → same time-cost, so
   the dissociation is purely energetic, isolated from ARC-068 opportunity-cost-of-time).
   *Verified:* low = 0.01/step, high = 0.03/step; high corridor drains more energy over the
   same traversal.
2. **Depletion actually accrues in the chronic regime.** A slow-recovery exertion
   accumulator (`_exertion_load`) accrues above `effort_exertion_threshold` (only the HIGH
   corridor crosses it) and recovers ~10x slower; sustained high effort accumulates it.
   *Verified:* exertion accrues on the high corridor, stays 0 on the low corridor.
3. **A tied/indifferent-benefit probe.** The two corridors terminate at a single shared
   resource, so benefit is **tied by construction** (`effort_benefit_asymmetry=0.0`, the
   default probe condition). The value-subtraction term is therefore indifferent between the
   paths on benefit — the regime where only a least-effort prior (or a harm-coupling) could
   break the tie toward low effort. *Verified:* cumulative benefit is identical along the two
   corridors at asym=0.

An **irreversible ratchet** (`_exertion_permanent`) accrues once the reversible load crosses
`effort_exertion_ratchet_mark` and recovery cannot erase it within the episode — the
"depletion it cannot cheaply reverse" that Q-080.a's *irreversibility-aware caution* targets.
*Verified:* the permanent component survives 200 rest-steps while the reversible load returns
to zero.

## Layout

Walled (non-toroidal) grid. Two vertical corridors, symmetric about the centre column, join a
bottom agent-start junction to a top single-resource junction:

```
  row 1     . . R . .        R = shared benefit resource (top junction)
  ...       #   |   #        left corridor  = LOW effort  (cost x1.0)
            L   .   H        right corridor = HIGH effort (cost x effort_high_multiplier)
  ...       #   |   #
  row s-2   . . A . .        A = agent start (bottom junction)
```

Path length via LOW = via HIGH (equidistant). No hazards on either path (pure effort
dissociation). Agent spawns equidistant to both corridor mouths.

## Config (env-only kwargs on `CausalGridWorld.__init__`; NOT surfaced through `REEConfig.from_dims`)

| Param | Default | Purpose |
|-------|---------|---------|
| `effort_dissociation_enabled` | `False` | master switch; OFF = bit-identical legacy |
| `effort_base_cost` | `0.01` | base per-action energy cost (× cell multiplier) |
| `effort_high_multiplier` | `3.0` | HIGH corridor cost multiplier (LOW = 1.0) |
| `effort_low_col_offset` / `effort_high_col_offset` | `2` / `2` | corridor column offsets from centre |
| `effort_exertion_threshold` | `0.02` | per-step effort above which exertion accrues (only HIGH crosses it) |
| `effort_exertion_accrual_rate` | `0.02` | reversible-load accrual per over-threshold step |
| `effort_exertion_recovery_rate` | `0.002` | slow reversible-load recovery per step |
| `effort_exertion_ratchet_mark` | `0.5` | load threshold above which the irreversible ratchet accrues |
| `effort_exertion_ratchet_rate` | `0.005` | irreversible-permanent accrual per step above the mark |
| `effort_harm_coupling_enabled` | `False` | **Q-080.a ON factor**: route effort into z_harm_a |
| `effort_harm_coupling_scale` | `1.0` | scale on the injected effort-harm term |
| `effort_harm_coupling_depletion_weight` | `1.0` | weight on `effective_depletion` in the injected term |
| `effort_benefit_asymmetry` | `0.0` | **Q-080.b control lever**: 0 = tied probe; >0 adds HIGH-path benefit |

Precondition: `effort_dissociation_enabled=True` requires `use_proxy_fields=True` (the
effort→harm coupling and interoceptive energy channels ride the proxy path); a `ValueError`
is raised at construction otherwise (loud-not-silent).

## Observables (obs_dict + info; present only when enabled — flat obs dims unchanged)

- `effort_cost_this_step` — energy spent to effort this step.
- `effort_cost_by_action` **[5]** — per-candidate-action effort cost from the current cell.
  This is the signal a **least-effort PRIOR** or a **per-action value-subtraction term**
  reads at SELECTION time (Q-080.b), before the move.
- `exertion_load` / `exertion_permanent` / `effort_depletion` — reversible / irreversible /
  total chronic-exertion depletion (Q-080.a: the state whose approach protective
  disengagement must anticipate, and whose non-reversibility caution scales to).
- `effort_corridor` — 0 junction / 1 LOW / 2 HIGH.
- (info) `effort_energy_cumulative`, `effort_harm_injected`.

## How the two ablations use it

Both ablations run on **one env**, factorial, with the value-subtraction (SD-032b dACC EVC)
+ allostatic (SD-032e pACC, SD-032c AIC) machinery ON in BOTH arms. No agent-code change is
needed for either factor.

- **Q-080.a HARM-COUPLING** — factorial `{effort_harm_coupling_enabled OFF/ON}`. When ON, the
  env folds the per-step effort + `effective_depletion` into `harm_exposure` and the
  `harm_obs_a_ema` hazard half. Because z_harm_a is `‖harm_obs_a‖` and SD-032e pACC /
  MECH-219 are **source-agnostic scalar integrators**, effort is thereby integrated into
  drive_level (pACC) and into the hysteretic suffering accumulator (MECH-219, whose sticky
  `alpha_rise ≫ alpha_fall` latch *is* the irreversibility-aware handling) and seen by the
  residue field — the "SD-032e effort-input variant" realised env-side. **ON wins ONLY** if
  it adds protective disengagement BEFORE depletion + caution scaled to the non-reversibility
  of the depletion that the OFF baseline lacks (strict seed majority). If OFF already
  reproduces those → effort is a foregone value; **do NOT mint a harm-coupling mechanism.**
- **Q-080.b LEAST-EFFORT PRIOR** — factorial `{least-effort prior OFF/ON}`. The prior is
  built in the experiment (no such primitive exists in `ree_core`) as a selection-time bias
  over `effort_cost_by_action`; the value-subtraction term (effort fed into the dACC
  `candidate_effort` / a per-action value term) is ON in both arms. Run at the tied-benefit
  probe (`effort_benefit_asymmetry=0.0`). **ON wins ONLY** if it defaults to the LOW path
  under tied benefit where the value-only arm leaves the tie unbroken (e.g. before value
  learning converges), seed majority. The `effort_benefit_asymmetry>0` control shows the
  value machinery is non-vacuous (it correctly prefers HIGH when benefit justifies it).

## Wiring points (source)

`ree-v3/ree_core/environment/causal_grid_world.py`:
- `__init__` kwargs + state; construction precondition.
- `_apply_effort_dissociation_layout()` — builds walls/corridors/effort grid; called from
  `reset()` after the normal per-episode state resets (layout override, so all counters /
  telemetry / proxy resets are inherited; OFF is bit-identical — the branch is not taken).
- `step()` — per-action effort energy cost + exertion accumulation (after `energy_decay`);
  effort→z_harm_a coupling injection (after the `harm_obs_a_ema` update); benefit-asymmetry
  bonus.
- `_effort_cost_by_action()`, `_effort_corridor_at()`, `_effort_effective_depletion()`,
  `_reset_effort_state()`.

Consumers this env is designed to exercise (all pre-existing, unchanged): SD-032b dACC
(`ree_core/cingulate/dacc.py`), SD-032e pACC (`ree_core/cingulate/pacc_analog.py`), SD-032c
AIC (`ree_core/cingulate/aic_analog.py`), SD-012 drive (`REEAgent.compute_drive_level`,
`goal.py`), MECH-320 tonic vigor (`ree_core/policy/tonic_vigor.py`), MECH-219 harm
accumulator (`ree_core/affect/harm_suffering_accumulator.py`).

## What this env is NOT

- Not a mechanism claim. Q-080 stays `open`; these ablations answer it. Minting a
  harm-coupling mechanism is explicitly gated on the Q-080.a ON arm winning.
- Not MECH-454's substrate (that is a reachable-option-dissociating env + an E3 option-value
  term — Q-080.c, separately blocked).
- Not surfaced through `REEConfig.from_dims` (env-only, SD-047/048/049/054 / infant
  precedent).
