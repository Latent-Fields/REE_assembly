# Experiment: EXQ-020 — Action-Loop Completion Gate (MECH-057a)

**EXQ ID:** EXQ-020
**Claim:** MECH-057a (`agentic_extension.action_loop_completion_gate`)
**Substrate:** ree-v2 (`CausalGridWorld` with `subgoal_mode=True`)
**Script:** `ree-v2/experiments/action_loop_completion_gate.py`
**Status:** queued (smoke-tested 2026-03-15; full run pending)

---

## Background

MECH-057a was split from MECH-057 on 2026-03-15 to cleanly separate:

- **MECH-057a** (this claim): action-loop completion gate — suppresses HippocampalModule
  from generating new competing candidates while a committed action sequence is executing.
  V2-testable with multi-step substrate.
- **MECH-057b**: thought-loop trajectory promotion gate — V3-scoped, requires
  HippocampalModule promotion policy not present in V1 or V2.

**Prior FAILs (substrate-limited, not architecture falsifications):**

| Run | Substrate | Result | Failure mode |
|-----|-----------|--------|--------------|
| EXQ-004 (EVB-0042) | ree-v1-minimal | FAIL | Single-step atomic grid actions; no "action in progress" state |
| EXQ-007 | ree-v1-minimal | FAIL | Same substrate limitation |
| V2 re-run (attribution_completion_gating, 2026-03-15) | ree-v2 (standard CausalGridWorld) | FAIL | Same: atomic single-step grid actions persist in base CausalGridWorld |

All three FAILs showed the **correct effect direction** (FULL < NO_ATTRIBUTION < NO_GATING)
but sub-threshold magnitude. EXQ-020 removes the substrate limitation by extending
CausalGridWorld with a `subgoal_mode` that creates genuine multi-step committed sequences.

---

## What it tests

MECH-057a predicts that an **action-loop completion gate** is load-bearing when:

1. Actions span multiple sub-steps (committed waypoint sequences, not single-step moves)
2. A competing sensory stream or candidate set could interrupt mid-sequence
3. Completion vs. interruption makes a measurable difference to harm

When the gate is enabled, `REEAgent.generate_trajectories()` returns **cached candidates**
from the last generation call rather than invoking `HippocampalModule` for fresh proposals.
This holds the action plan stable while the sequence executes.

---

## Substrate extension

`CausalGridWorld(subgoal_mode=True)`:

- **3 waypoint cells** placed at episode reset; labeled entity type 6 `"waypoint"`.
- Agent must visit waypoints in order: W0 → W1 → W2.
- Visiting W0 starts a **committed sequence** (`sequence_in_progress=True`).
- Visiting W1 earns `waypoint_visit_reward=0.2`; sequence continues.
- Visiting W2 earns `waypoint_completion_reward=0.8`; sequence completes; waypoints respawn.
- Visiting a waypoint out of order: no effect (cell stays on grid).
- **Timeout:** if `sequence_commitment_timeout=20` steps pass without hitting the next
  waypoint, the sequence resets and waypoints respawn.
- **Hazards remain active** (4 env-caused hazards, drifting) — real interruption pressure.
- `info['sequence_in_progress']` (bool) and `info['sequence_step']` (int) exposed every step.
- Backward-compatible: `subgoal_mode=False` (default) preserves all original behaviour.

---

## Agent modification

`REEAgent.generate_trajectories(sequence_in_progress=False)`:

- New `sequence_in_progress` parameter forwarded from environment `info` dict.
- When `config.action_loop_gate_enabled=True` AND `sequence_in_progress=True` AND
  cached candidates exist: returns `_committed_candidates` (gate active).
- Otherwise: invokes `HippocampalModule.propose_trajectories()` as normal; caches result.
- Cache cleared on `agent.reset()` (episode boundary).
- `update_residue(harm, owned=bool)`: new `owned` parameter. When `owned=False`,
  residue accumulation is skipped for this harm event (attribution ablation).
- Gate ablated via `config.action_loop_gate_enabled=False` (NO_GATE condition).
- Attribution ablated via `owned=True` always (NO_ATTRIBUTION condition).

---

## Conditions

| Condition | Gate | Attribution | Implementation |
|-----------|------|-------------|----------------|
| **FULL** | enabled | enabled | `gate=True`; G = -harm_during_sequence; residue only when `sequence_in_progress=True` |
| **NO_GATE** | disabled | enabled | `gate=False`; HippocampalModule proposes fresh candidates every step mid-sequence; same G and residue as FULL |
| **NO_ATTRIBUTION** | enabled | disabled | `gate=True`; G = -total_harm; residue for all harm regardless of sequence state |

---

## Experimental parameters

| Parameter | Value |
|-----------|-------|
| `num_episodes` | 250 |
| `max_steps` | 100 |
| `seeds` | 7, 42, 99, 13, 77 (5 seeds) |
| `grid_size` | 10 |
| `num_hazards` | 4 |
| `num_waypoints` | 3 |
| `waypoint_visit_reward` | 0.2 |
| `waypoint_completion_reward` | 0.8 |
| `sequence_commitment_timeout` | 20 |
| `e1_lr` | 1e-4 |
| `policy_lr` | 1e-3 |
| `e2_lr` | 1e-3 |

**Primary metric:** mean total harm in the final quartile of episodes
(last 62 of 250 episodes per condition per seed), averaged across all 5 seeds.

---

## Pass criteria

Both criteria must hold for full PASS:

1. `harm[NO_GATE] / harm[FULL] >= 1.10` — gate removal degrades harm avoidance by ≥10%
2. `harm[NO_ATTRIBUTION] / harm[FULL] >= 1.05` — attribution removal shows measurable effect ≥5%

If only criterion 1 passes: **partial PASS** — gate is load-bearing but attribution effect
not confirmed at this scale. Record with note.

If neither passes despite multi-step substrate: **informative FAIL** — stronger negative
signal than V1/V2 FAILs because the substrate limitation has been removed.

---

## Smoke run (2026-03-15, 5 episodes, 1 seed)

Smoke run confirms the experimental machinery is functional:

| Condition | harm (last-Q) |
|-----------|--------------|
| FULL | 1.000 |
| NO_GATE | 1.800 |
| NO_ATTRIBUTION | 1.200 |

- Criterion 1: NO_GATE/FULL = 1.80 ≥ 1.10 ✓
- Criterion 2: NO_ATTR/FULL = 1.20 ≥ 1.05 ✓
- Smoke verdict: PASS (5 episodes, not statistically valid — full run required)

**Note:** Smoke run result is directionally encouraging but statistically meaningless at
5 episodes / 1 seed. The full run (250 episodes × 5 seeds × 3 conditions) is required
for a valid verdict. Full run queued as EXQ-020.

---

## Expected interpretation

**If PASS:**
- The action-loop gate is load-bearing: mid-sequence replanning causes ≥10% more harm.
- MECH-057a confirmed on genuine multi-step substrate.
- Update MECH-057a status: `candidate → provisional`.

**If PARTIAL_PASS (criterion 1 only):**
- Gate is load-bearing; attribution effect is sub-threshold.
- Attribution signal may need larger substrate (longer sequences, more hazards) to manifest.
- Record as partial PASS; MECH-057a remains candidate pending attribution confirmation.

**If FAIL:**
- Both mechanisms are non-load-bearing even with multi-step substrate.
- Stronger negative signal than prior FAILs.
- Examine: does the agent actually complete sequences? (seq_completed metric)
  If seq_completed ≈ 0, the sequence reward signal is insufficient and the
  substrate doesn't create real committed sequences for the gate to protect.
- Possible redesign: increase waypoint_completion_reward, reduce hazards,
  or lengthen timeout before re-testing.

---

## Claim lineage

- Originates from MECH-057 (2026-02-25 adjudication, hybridize outcome)
- Split 2026-03-15: MECH-057a (this experiment) + MECH-057b (V3-scoped)
- Prior FAILs: EXQ-004 (EVB-0042), EXQ-007, V2 re-run — all substrate-limited
- Effect direction confirmed in V1: FULL < NO_ATTRIBUTION < NO_GATING
- EXQ-020 is the first test with correct substrate for MECH-057a
