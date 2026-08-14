# MECH-357 pressure-mechanism attempt 6: agent-directed hazard pursuit -- build + validation design

**Author session:** intelligent-elgamal-222d2b (`/implement-substrate`)
**Date:** 2026-08-14T06:23:06Z
**SD/claim:** SD-058 (architecture) + MECH-357 (mechanism); both `candidate` / `v3_pending`
**Scoping precursor:** [`mech357_freeze_incompatible_pressure_scoping_2026-08-10.md`](mech357_freeze_incompatible_pressure_scoping_2026-08-10.md) SS3
**Architecture doc:** [`../../docs/architecture/sd_058_instrumental_avoidance_acquisition.md`](../../docs/architecture/sd_058_instrumental_avoidance_acquisition.md)
**Validation experiment:** V3-EXQ-603u (run_id family `v3_exq_603u_instrumental_avoidance_agent_pursuit`)

---

## Problem

MECH-357 (the infralimbic-PFC-analog freeze-suppression + instrumental-avoidance gate,
`ree_core/pfc/infralimbic_avoidance_gate.py`) is **IMPLEMENTED**. SD-058 stays `v3_pending`
until its Stage-H validation EXQ PASSes. That validation asks a single question: under threat
pressure, does the INTACT arm (gate ON) survive better than the LESION negative control (gate
OFF)? Five prior attempts failed **not** because the gate is wrong, but because the **pressure
mechanism** never reintroduced the Pavlovian-instrumental conflict the paradigm needs:

| attempt | pressure mechanism | outcome |
|---|---|---|
| 603h/603k/603r | static hazard field | LESION survivable (freeze/release adequate); no discrimination |
| 603s | mobile-predator drift (`env_drift_interval=1`, high prob) | `G_H_INTACT_frac = G_H_LESION_frac = 0.6667` -- **exact tie** |
| 603t | SD-029 `scheduled_external_hazard` (discrete adjacency) | `G_H_LESION_frac = 1.0` -- LESION hit ceiling, i.e. *less* conflict |

The common defect (traced in the scoping doc SS1-SS3): **every prior pressure mechanism left
hazard motion agent-INDEPENDENT.** `_drift_hazards`'s undirected and food-attraction branches
never reference the agent's position, so an undirected freeze/release cycle stays reachable
indefinitely -- the threat is a one-shot spawn-position lottery, not a sustained,
behaviour-contingent pursuit. Config-only levers over agent-independent motion are exhausted
across 3 distinct designs.

## Solution (this build)

Thread the **already-built** `hazard_agent_pursuit` env parameter (added to
`CausalGridWorldV2` by ree-v3 `39b5ca8`, contract-tested in
`tests/contracts/test_hazard_agent_pursuit.py`) through the Stage-H `_build_env` of
`scaffolded_sd054_onboarding.py`. `hazard_agent_pursuit` is the agent-directed sibling of
`hazard_food_attraction`: with per-drift-tick probability it sorts a drifting hazard's
candidate directions toward the agent's CURRENT cell (Manhattan-nearest), gated on
`reef_enabled` and only firing on an `env_drift` tick. It is the **one remaining candidate**
(scoping SS3) that makes the threat continuous and behaviour-contingent -- a pursuing hazard
closes distance unless the agent actively escapes to the reef refuge, which is the sustained
Pavlovian-instrumental conflict Moscarello & LeDoux (2013) active avoidance requires.

### Data flow

```
driver sets cfg.scaffold_hazard_stage_hazard_agent_pursuit = 0.9
    -> _build_env(cfg, phase="hazard") passes hazard_agent_pursuit=<cfg field>
    -> CausalGridWorldV2._drift_hazards()          [reef_enabled=True, env_drift_prob=0.3 already on]
    -> per drift tick, with prob 0.9, hazard biases its step toward (agent_x, agent_y)
```

### Config change (one field, no-op default)

`ScaffoldedSD054OnboardingConfig.scaffold_hazard_stage_hazard_agent_pursuit: float = 0.0`.
Default `0.0` == the `CausalGridWorldV2` constructor default; the `elif hazard_agent_pursuit
> 0.0` branch in `_drift_hazards` is never entered, so 603g/603h/603r/603s/603t and every
other caller are **bit-identical**. Verified by smoke: default config -> `env.hazard_agent_pursuit
== 0.0`; set 0.9 -> `env.hazard_agent_pursuit == 0.9`; 40 Stage-H steps under pursuit=0.9 with
the bipartite layout run without error.

Not a `REEConfig` field -- an experiment-driver dataclass field set directly by the driver, so
no `REEConfig.from_dims` wiring is involved.

## Validation (V3-EXQ-603u)

Driver `v3_exq_603u_instrumental_avoidance_agent_pursuit.py`, a copy of the **603s** driver
(which already carries the mobile-predator drift) with `hazard_agent_pursuit=0.9` added. The
pressure is therefore **603s + directedness**: the arms keep 603s's mobile drift
(`env_drift_interval=1`, `env_drift_prob=0.6`, so hazards move every step) and add
`scaffold_hazard_stage_hazard_agent_pursuit=0.9` -- the SINGLE isolated change vs 603s, so a
moving hazard now chases the agent's current cell 90% of the time instead of drifting at
random. This is the cleanest isolation of "directedness": 603s was frequent+undirected (exact
tie); 603u is frequent+directed. Same 3-arm structure and readiness gates:

- **ARM_LESION** (use_ia=False, driver=False, midline spawn) -- negative control.
- **ARM_INTACT** (use_ia=True, driver=True, midline spawn) -- the test.
- **ARM_POSCTRL** (reef-refuge spawn) -- survivability positive control.

**Acceptance (from the failure record):**
- **PRIMARY (load-bearing):** `G_H_INTACT_frac > G_H_LESION_frac` AND `G_H_INTACT_frac >= 2/3`.
  The 603s exact tie is the specific failure to break -- the intact arm must clear the lesion
  arm in the intact direction.
- **R4 headroom-below:** `G_H_LESION_frac < 0.667` -- the pursuit pressure must make the LESION
  negative control FAIL its own survival gate (the 603t LESION-ceiling failure to break).
- **R5 survivability-above:** POSCTRL clears `>= 2/3` -- pressure is not simply lethal.

`EXPERIMENT_PURPOSE = "evidence"`, `claim_ids = ["MECH-357"]` -- matching the established
603r/603s/603t lineage rather than the generic substrate-readiness `diagnostic` default. The
run's whole design IS a claim-tagged LESION/INTACT dissociation, and its pre-registered
CONFIRMING/FALSIFYING/NON-DISCRIMINATIVE routing protects the claim from a design-defect FAIL:
a tie or ceiling self-routes to `substrate_not_ready_requeue` / `non_contributory` (not a
`weakens`), exactly as 603s/603t did. A purpose change mid-lineage would also fragment the
evidence family and break manifest comparability.

## Out of scope: the eligibility-trace leak:learn imbalance

The queue entry flags that `infralimbic_avoidance_gate.py`'s efficacy learner decays much
faster than it credits (credit fires only when harm drops after a directed action; decay fires
on every other under-threat tick), underflowing the **learned** `avoidance_efficacy` toward
zero. This is filed as a **separate `substrate_queue.json` line item** and is deliberately NOT
part of this build. Read of the gate confirms it does **not confound** the G_H window this
validation measures: `effective_efficacy = max(avoidance_efficacy, scaffold_floor)`, and the
Stage-H protective-scaffold floor (0.8, annealing) keeps `effective_efficacy` high during the
G_H measurement window regardless of the learned component. The underflow degrades P1/P2
transfer/persistence -- a separate readiness concern -- not the Stage-H discrimination.

## What a PASS means / does not mean

- PASS (PRIMARY + R4 + R5): the last untried pressure lever breaks the tie; MECH-357 has a
  valid discriminative Stage-H test and SD-058 can move toward governance evidence (a
  subsequent `EXPERIMENT_PURPOSE="evidence"` run, not this diagnostic).
- FAIL with R1 (PAG freezes on LESION) + R5 (POSCTRL survives) + gate engaging, but INTACT not
  beating LESION: freeze-suppression insufficient to rescue survival even under the strongest
  agent-directed pressure -- routes to a MECH-357 mechanism re-examination, and elevates the
  eligibility-trace follow-on from "separate" to "candidate confound worth resolving first".
- FAIL with LESION still clearing the gate: pursuit=0.9 too gentle -- recalibrate
  (raise `env_drift_prob` so hazards move more often, or the pursuit probability is already at
  ceiling so the lever itself is spent).
