---
nav_exclude: true
---

# MECH-271 Hypothesis-Tag-as-Routing -- V3 Substrate Landing Plan

**Claim:** MECH-271 (hypothesis tag realised as differential downstream routing of
hippocampal replay, not source-side boolean).
**Status:** candidate, implementation_phase: v3, v3_pending: true.
**Registered:** 2026-04-21. Plan written: 2026-04-26.
**Depends on:** MECH-094 (the tag this claim reframes), MECH-269 (anchor/probe distinction),
MECH-269b (parallel-session: symmetric V_s gating on E1/E2 -- MECH-271 routing reads from
gated streams), ARC-007 (path memory), ARC-018 (viability map), SD-033a (lateral-PFC-analog
destination), SD-035 (BLA-analog destination).
**Architectural commitment (V3):** the hypothesis tag is implemented as a routing-
destination weighting vector attached to each replay event, not as a boolean write gate.
The V3 form uses synaptic destination weights (no ephaptic substrate); V4 will refine the
routing signal to a phase-channel coordinate (MECH-228 ephaptic field-coherence).

---

## Why this is "small" (the user's framing)

Most of the substrate MECH-271 needs is already implemented:

- **MECH-269 anchor/probe distinction** -- LANDED 2026-04-22 (Phase 2 ii AnchorSet, dual-
  trace `mark_inactive` not erase, k=5 hysteresis).
- **MECH-094 hypothesis tag (categorical write gate)** -- LANDED earlier (REEAgent
  simulation_mode flag; consumed by MECH-275/273 sleep aggregator paths).
- **SD-033a lateral PFC analog** -- LANDED 2026-04-20 (V3-EXQ-456 PASS).
- **SD-035 amygdala-analog (BLA + CeA)** -- LANDED 2026-04-21 (V3-EXQ-473/474 PASS).
- **ARC-018 viability map** + **ARC-007 path memory** -- LANDED earlier in V3.

What MECH-271 adds is the *routing table* + the *write-destination dispatcher* + the
*audit hook* that flags tag loss. This is roughly 200-300 LOC plus a contracts test
suite -- consistent with the "small" framing.

---

## V3 substrate (what to land)

### 1. RoutingTable (new, `ree_core/hippocampal/replay_routing.py`)

Static destination weights per (replay_kind, destination_name) pair:

| destination_name | anchored | probe | source claim |
|---|---:|---:|---|
| `e1_consolidation`            | 1.0  | 0.0  | MECH-271 (subiculum -> entorhinal -> neocortex) |
| `lateral_pfc_viability_map`   | 1.0  | 0.0  | SD-033a (anchored destination) |
| `bla_affective_tagging`       | 0.2  | 1.0  | SD-035 (probe destination) |
| `nac_curiosity_scaffolding`   | 0.0  | 1.0  | NAc novelty fan-out |
| `e3_planning_evaluation`      | 1.0  | 0.4  | both kinds inform planning, anchored dominates |

`replay_kind` is determined at draw time:
- **Anchored** = MECH-269 anchor-set draw (active anchor with V_s_anchor >= reset
  threshold).
- **Probe** = MECH-285 sleep-priority draw (high-staleness softmax) OR an explicit
  `is_probe=True` waking draw (deferred V4: waking probe replays).

### 2. ReplayEvent payload extension

Existing replay events already carry `simulation_mode` (MECH-094 boolean). Add:

- `replay_kind: Literal["anchored", "probe"]`
- `routing_weights: dict[str, float]` -- looked up from RoutingTable at emission time

Both fields are `Optional` and default to backward-compatible values when MECH-271 is
disabled (anchored / `{e1_consolidation: 1.0, lateral_pfc_viability_map: 1.0}` -- the
pre-MECH-271 implicit assumption).

### 3. Destination dispatcher (in REEAgent.consume_replay)

Each downstream consumer (E1 ContextMemory writeback, SD-033a LateralPFCAnalog gate,
SD-035 BLA encoding, NAc-curiosity scaffolding, E3Selector) is given a
`destination_name` registration string. The dispatcher passes the replay event to a
consumer if `routing_weights[destination_name] >= consumer_threshold` (default 0.5,
configurable per consumer).

This is the only behavioural change. With the master flag OFF, all consumers see all
replays (current behaviour); with the master flag ON, anchored consumers see only
anchored replays and probe consumers see only probe replays, modulated by the table.

### 4. Audit hook (MECH-094 tag-loss detector)

A new `tag_loss_audit` counter increments when a probe replay reaches a destination with
`anchored_weight > 0.8 AND probe_weight < 0.2`. This is the auditable confabulatory-
planning signature MECH-271 names. Surface as `mech271_tag_loss_count` in
SleepCycleState.last_metrics + REEAgent.diagnostic_signals.

In a healthy substrate this counter stays at 0; under deliberate ablation
(`mech271_force_tag_loss_rate=0.X`) it accumulates at the expected rate. The audit hook
is the substrate-level test that makes confabulation distinguishable from psychosis (the
psychosis signature is at MECH-094 source-side; confabulation is the routing-side leak
this counter catches).

### 5. Configuration

Master flag `use_mech271_routing` (default False, bit-identical-when-OFF preserved).
Sub-knobs:

- `mech271_consumer_threshold` (default 0.5)
- `mech271_force_tag_loss_rate` (default 0.0; ablation knob for the audit-hook test)
- `mech271_routing_table_path` (default uses the static table above; path allows
  experiment-specific overrides without code edit)

---

## Contracts test suite (`tests/contracts/test_mech_271_routing.py`)

10 tests, parallel to the SD-035 / Sleep-Phase-A pattern:

- M1 import + module exposure
- M2 default-OFF backward-compat (ContextMemory, LateralPFCAnalog, BLA all see all replays)
- M3 OFF-no-instantiation (no RoutingTable created when flag OFF)
- M4 ON-anchored-replay reaches e1_consolidation + lateral_pfc, NOT bla / nac
- M5 ON-probe-replay reaches bla + nac, NOT e1_consolidation
- M6 e3_planning_evaluation receives both kinds (mixed-destination correctness)
- M7 audit hook fires on forced tag loss (force_tag_loss_rate=1.0 -> count == n_probe)
- M8 audit hook quiet on healthy substrate (force_tag_loss_rate=0.0 -> count == 0)
- M9 routing_table_path override loads correctly
- M10 bit-identical-OFF leaks no `mech271_*` keys

---

## Validation experiment (queue after implement-mech269b lock releases)

`V3-EXQ-492` (proposed): MECH-271 routing-as-tag substrate validation. 4-arm:

- `A0_off`: master flag OFF (baseline; reproduces current behaviour)
- `A1_routing_only`: master flag ON, force_tag_loss_rate=0.0 (clean substrate)
- `A2_forced_leak`: master flag ON, force_tag_loss_rate=0.5 (deliberate confabulation
  injection)
- `A3_high_leak`: master flag ON, force_tag_loss_rate=1.0 (full tag loss)

Acceptance:

- C1: A1 reduces consolidation writes from probe replays vs A0 (`>=70%` reduction in
  ContextMemory write events tagged probe).
- C2: A2 audit count tracks injection rate within +/-10% (instrumentation correctness).
- C3: A3 reproduces a confabulation behavioural signature -- specifically, an increase in
  E1-prediction-divergence on held-out probe content (`>=2x` relative to A1).
- C4: bit-identical OFF (A0 vs pre-flag baseline within 1e-9 on all run metrics).

The behavioural signature in C3 grounds MECH-271's clinical claim that probe content
reaching consolidation produces an *auditable* confabulatory-planning failure mode
distinct from psychosis (which is a source-side MECH-094 failure -- different
experiment).

---

## Failure modes / known caveats

**Static routing table** is a V3 simplification. Biology likely has the routing weights
adapt under learning (e.g. cortical schemas that gain reliable predictive value should
attract more anchored-replay routing; novel schemas should gain probe-routing capacity).
Adaptive routing is V4 work, dependent on MECH-228 ephaptic field-coherence (the
biological mechanism that lets routing be dynamically modulated per-event).

**Single audit counter** is a V3 minimum. A richer audit would track per-destination
leak rates and per-source-region leak rates -- diagnostic for tracing *which* schema is
driving confabulation. V3 lands the single counter; V4 may add per-region breakdown if
clinical use cases (psychiatric simulation experiments) require it.

**No phase-channel routing** is the V4 deferral. MECH-271's full claim is that the tag
is realised as ephaptically-coordinated routing -- the phase channel IS the tag at the
biophysical level. V3 approximates this with a discrete routing table; V4 adds the
continuous phase-channel coordinate per MECH-228 + the per-destination phase-coupling
strength per ARC-053 TCL.

---

## Cross-references

- **MECH-094**: source-side tag (already implemented; this claim refines downstream
  realisation).
- **MECH-269 / MECH-269b** (parallel session): anchor/probe distinction at source +
  symmetric V_s gating on E1/E2.
- **SD-033a, SD-035**: anchored / probe destinations whose dispatchers MECH-271 wires.
- **`v3_v4_phase_substrate_boundary.md`**: explicit V4 deferral commitment for the
  phase-channel realisation.
- **`v_s_invalidation_runtime.md`**: parent V_s document that names MECH-271 as the
  routing-side companion claim.

---

## Lock coordination

This plan does not edit `ree-v3/ree_core/hippocampal/module.py` -- that file is held
by the active `implement-mech269b` session. MECH-271 substrate code lands in a follow-
up `/implement-substrate` session, scheduled after implement-mech269b releases its lock.
That ordering is appropriate substrate-wise too: MECH-271 routing reads from the V_s
gating that MECH-269b adds, so MECH-269b lands first.
