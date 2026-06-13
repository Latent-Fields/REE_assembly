---
title: "MECH-219: Affective-Harm Hysteretic Integrator (z_harm_suffering)"
parent: "Affect, Harm & Nociception"
grandparent: Architecture
nav_order: 7
---

# MECH-219: Affective-Harm Hysteretic Integrator (z_harm_suffering)

**Claim ID:** MECH-219 (`affect.affective_harm_hysteretic_integration`)
**Unblocks:** SD-019b (`harm_stream.suffering_accumulator`), Q-036
**Status:** IMPLEMENTED 2026-06-10 (substrate; SD-019b stays `v3_pending` until the
validation EXQ PASSes)
**Depends on:** SD-019a (z_harm_un, the drive input), SD-011 (z_harm_s/z_harm_a),
SD-022 (body-damage, folded into the drive), SD-058 (escapability source, soft)
**Plan-of-record (full design rationale):**
[`evidence/planning/mech_219_hysteretic_integrator_design.md`](../../evidence/planning/mech_219_hysteretic_integrator_design.md)

This doc records the **as-built** substrate. The planning memo is the authoritative
design spec (Q-036 adjudication, escapability-source selection, dynamics,
distinct-from contracts, migration plan, validation sketch, governance follow-ups).

---

## What was built

Three-tier harm-affect hierarchy; MECH-219 is the tier-2 -> tier-3 step:

```
z_harm_s   (SD-010/011)   fast nociception                       BUILT
   |  EMA alpha=0.2 (SD-019a, harm_un_ema)
z_harm_un  (SD-019a)      medium "make it stop" unpleasantness    BUILT
   |  MECH-219 controllability-gated hysteretic integration       THIS SUBSTRATE
z_harm_a   (suffering)    slow, persistent, controllability-gated z_harm_suffering
```

**Module:** `ree-v3/ree_core/affect/harm_suffering_accumulator.py`
(`HarmSufferingAccumulator` + `HarmSufferingAccumulatorConfig` +
`HarmSufferingAccumulatorOutput`). Pure-arithmetic regulator (no `nn.Module`, no
learned parameters, no gradient flow); sibling to the MECH-353 BlockedAgency /
MECH-313 / MECH-320 / MECH-342 pattern. It owns only the scalar suffering state
`s_t`; the agent builds the `z_harm_suffering` LatentState vector.

### Dynamics (per waking tick, gated `simulation_mode=False`)

```
u_t      = ||z_harm_un||  (+ body_damage_weight * ||z_harm_a||)   # drive
g_t      = 1 - escapability_t                                      # controllability gate
drive_t  = g_t * u_t  (+ pe_gain * unsigned_PE_t)
# asymmetric (hysteretic) accumulation:
alpha    = alpha_rise if drive_t > s_{t-1} else alpha_fall         # alpha_rise >> alpha_fall
s_t      = clip(s_{t-1} + alpha * (drive_t - s_{t-1}), 0, s_cap)
# optional Schmitt latch (default off): latched flips True > theta_on, False < theta_off
output   = s_t (* latched if enabled)
```

`z_harm_suffering` = the `z_harm_un` direction scaled to magnitude `s_t` (same dim
as z_harm_un), so `||z_harm_suffering|| == s_t`.

- **Controllability gate** `g_t = 1 - escapability` (Salomons 2004 / Loffler 2018):
  under full control (escapability=1) `drive_t=0` -> suffering does not accrue even
  at high unpleasantness. The falsifiable dissociation.
- **Hysteresis** `alpha_rise >> alpha_fall`: fast build, slow release (the
  recovery-failure / chronic-pain signature; Baliki 2012). Emerges here, not from a
  separate input.

### Escapability source (pluggable)

`harm_suffering_escapability_mode`:
- `constant` (default `1.0`) -> `g=0` -> inert. **Dependency-free; bit-identical OFF.**
- `avoidance_efficacy` -> SD-058 `InstrumentalAvoidanceGate.effective_efficacy()` --
  the literal escapability construct. Soft dependency on the `v3_pending` SD-058
  substrate; this is the mode the behavioural validation exercises once SD-058 clears.
- `external` -> `REEAgent.set_harm_suffering_escapability()` seam for a scripted
  validation schedule.

**Never** sourced from MECH-353 `capacity_belief` (= `1 - w*||z_harm_a||`) -- that
closes a `z_harm_a -> capacity_belief -> z_harm_a` loop. `capacity_belief` is a
validation cross-check only.

### z_harm_a re-source migration (per-consumer redirect)

`use_harm_suffering_accumulator` is the master flag; per-consumer redirect flags
`harm_suffering_redirect_{aic,pag,mech091,dacc,pacc}` (all default OFF) stage the
migration. Redirects are **magnitude-based** (`||z_harm_suffering||`):

- **v1 wires** the urgency/PAG/interrupt consumers: AIC urgency (`aic_z_norm`), PAG
  MECH-279 freeze drive (`pag_z_norm`), MECH-091 urgency-interrupt (`_urgency_signal`).
- **dACC/pACC flags are defined but UNWIRED** (no-ops): their E2_harm_a forward models
  are keyed on the current `z_harm_a` dim (`z_harm_a_dim != harm_dim`), so they
  migrate last after measuring R^2 -- v1 keeps them on legacy `z_harm_a`.

**Body-damage fold-in:** `body_damage_weight` (default 0.0) folds `||z_harm_a||` into
the drive so SD-022 / EXQ-319 / EXQ-323a non-redundancy evidence is preserved.

---

## Wiring (ree-v3/ree_core/agent.py)

- Built in `__init__` when the master flag is on. **Precondition:** requires
  `use_harm_un=True` (loud `ValueError` otherwise -- z_harm_un is the drive input).
- Ticked in `sense()` immediately after the SD-019a z_harm_un EMA and **before** the
  SD-032 consumers (AIC in sense; PAG/pACC in select_action), so a redirect reads the
  suffering output on the same tick.
- `reset()` clears `s_t` per episode.
- **MECH-094:** `update()` is a no-op under `simulation_mode` (hypothesis_tag) -- replay
  / DMN ticks do not accumulate suffering on imagined outcomes.

## Contracts

`ree-v3/tests/contracts/test_mech_219_harm_suffering_accumulator.py` (11): C1
bit-identical OFF; C2 config validation; C3 controllability gate; C4 hysteresis;
C5 MECH-094 sim no-op; C6 body-damage fold-in; C7 bistable latch; C8 precondition;
C9 escapability source modes; C10 LatentState field populated + detach + dim parity;
C11 redirect flags default off + AIC redirect.

## Validation (separate /queue-experiment session)

Not queued in the build session. The controllability-dissociation falsifier (memo
Section 7): matched nociception under **escapable vs inescapable** conditions ->
C1 (gate) suffering accrues inescapable, stays low escapable; C2 (hysteresis) slow
release; C3 (non-vacuity / distinct-from z_harm_un + anti-correlates with MECH-353
z_block_assert); C4 (SD-021 parity). PASS clears the SD-019b / Q-036 gate.

## Distinct-from (anti-duplication, memo Section 5)

- **vs SD-019a z_harm_un:** symmetric/controllability-independent EMA vs
  asymmetric/controllability-gated. Escapability=constant=1 collapses MECH-219 toward
  inert.
- **vs SD-022 body-damage z_harm_a:** env-sourced slow EMA, not controllability-gated;
  body-damage is folded into the MECH-219 drive, not discarded.
- **vs MECH-353 blocked-agency:** same controllability axis, opposite pole
  (capacity-RETAINED assert vs capacity-COLLAPSED withdraw); they anti-correlate.
- **vs SD-032e pACC:** pACC drifts on the z_harm_a MECH-219 produces; MECH-219 runs
  upstream.
