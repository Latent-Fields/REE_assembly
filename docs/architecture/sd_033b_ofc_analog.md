# SD-033b: OFC-analog (specific-outcome / task-structure substrate)

**Claim ID:** SD-033b
**Subject:** pfc.ofc_analog
**Status:** IMPLEMENTED 2026-04-26
**Depends on:** SD-033, MECH-261, MECH-263 (functional signatures deferred to behavioural EXQs)
**Blocks:** MECH-261 second consumer landing, MECH-263 falsification experiments
(devaluation sensitivity, same-sensory / different-task-role discrimination), downstream
SD-033 integrations that read outcome-state-biased E3 scores.
**Parent design:** `sd_033_pfc_subdivision_architecture.md`
**Sibling:** `sd_033a_lateral_pfc_analog.md`

## Problem

MECH-261 is a dict-keyed write-gate registry on SD-032a (SalienceCoordinator). Its
spec assigns per-mode weights to `sd_033b`: `external_task=1.0, internal_planning=0.5,
internal_replay=0.05, offline_consolidation=0.3`. SD-033a (Track 1 of the SD-033
landing) instantiated the first MECH-261 cortical-subdivision consumer; SD-033b is
the second consumer the spec designates. Without it, MECH-261 has only a single
load-bearing customer and the registry's claim of cluster-wide gate routing
remains under-tested.

SD-033b is specified by two functional signatures inherited from MECH-263: (a)
devaluation sensitivity (the substrate's bias output should change when the same
sensory stimulus is paired with a different outcome value), and (b) same-sensory /
different-task-role discrimination (the substrate should distinguish two
perceptually identical states that play different roles in task structure).
Both signatures require environment work that V3's grid-world cannot currently
exercise (outcome relabelling, task-role-distinct state pairs). The landing
implementation therefore validates the SUBSTRATE (gating, persistence, zero-init
contract, backward compat) and queues the behavioural validation to follow when
the env extension lands.

## Solution

Non-trainable arithmetic (gate-modulated EMA over an outcome-state code) plus a
small frozen-random bias head whose last `nn.Linear` is zeroed at init so the
initial bias output is exactly zero. Structurally parallel to SD-033a; the
distinction is the input source (z_world plus optional z_harm outcome pooling
vs SD-033a's z_delta plus z_world) and the consumer-side semantics (outcome /
task-structure bias vs rule bias).

**Module:** `ree_core/pfc/ofc_analog.py` (OFCAnalog, OFCConfig). Agent-side
wiring in `ree_core/agent.py` (`select_action` tick block, `reset`, `__init__`).

**State:** `state_code: torch.Tensor` buffer, shape `[1, state_dim]`
(default state_dim=16). Persistent across ticks within an episode.

**Update rule (outcome-state persistence + writing):**

```
gate = SalienceCoordinator.write_gate("sd_033b")          # in [0, 1]
eff_eta = update_eta * clip(gate, 0, 1)                    # update_eta=0.05 default
source = world_proj(z_world).mean(0)
       + outcome_pool_weight * outcome_proj(z_harm).mean(0)   # only when harm_dim > 0
state_code <- (1 - eff_eta) * state_code + eff_eta * source
```

Gate near zero (e.g. `internal_replay`, weight 0.05) -> state_code nearly frozen;
gate near 1 (`external_task`) -> state_code tracks source with ~20-step rise time.
The MECH-261 weights for sd_033b differ from sd_033a in `internal_planning`
(0.5 vs 1.0): outcome / task-structure representation can be partially updated
during planning rollouts (replanning re-evaluates outcome state) but not as
aggressively as rule state.

**Outcome-pool input is opt-in via config (`harm_dim > 0`):** when harm_dim is
zero (default), only the z_world projection contributes to source, so OFCAnalog
defaults to a pure task-structure / sensory-context substrate. Setting harm_dim
to the SD-011 z_harm dim turns on the second projection so outcome-magnitude
information enters the state code -- the architectural shape that MECH-263
devaluation sensitivity probes.

**Read path (top-down bias into E3):**

```
for each candidate trajectory c_k:
    summary_k = first-step z_world of c_k        # from c_k.world_states[:, 0, :]
joined = concat([state_code.expand(K, -1), summaries], dim=-1)
bias_raw = state_bias_head(joined).squeeze(-1)            # [K]
score_bias = clamp(bias_raw, -bias_scale, +bias_scale)     # bias_scale=0.1 default
```

Composed additively with SD-033a's lateral_pfc bias and SD-032b's dACC bias
before E3.select(). E3 convention is lower-is-better, so positive bias
penalises a trajectory.

**MECH-094 treatment:** as for SD-033a, MECH-261 generalises the
hypothesis_tag semantics. write_gate("sd_033b") = 0.05 under internal_replay
means replay content cannot meaningfully update state_code. The gate IS the
tag. No separate hypothesis_tag check is needed in OFCAnalog.

## Architecture Context

SD-033b is the second consumer of MECH-261's write_gate registry. Its bias
output composes additively with SD-033a's lateral_pfc bias and SD-032b's dACC
bias via `score_bias` on E3.select():

```
E3_bias = dacc_bias + lateral_pfc_bias + ofc_bias
```

(All lower-is-better.) dACC handles cost-of-control and payoff/effort
integration; lateral-PFC handles rule-conformity; OFC handles outcome /
task-structure conformity. These are distinct biological circuits and their
bias signals are architecturally separate.

**Bias-head reuse pattern (agent.py select_action):** when both lateral_pfc and
ofc are on, the per-candidate z_world summaries are built once in the
lateral_pfc tick block (`cand_world_summaries`) and reused
(`ofc_summaries = cand_world_summaries`); when ofc is on alone, the summaries
are built from scratch in the ofc block. Avoids redundant tensor stacking in
the common SD-033a + SD-033b on case.

Reset is per-episode (agent.reset -> ofc.reset -> state_code.zero_).
state_code does NOT persist across episodes (V3 simplification, parallel to
SD-033a).

## Design Choices and Deferrals

### D1. Frozen-random bias head with last layer zeroed (parallel to SD-033a A2)

**Chosen:** frozen-random, last-Linear weights and bias zeroed at init so
initial output is exactly zero. Head parameters are registered but not
added to any optimizer by default. Phased-training for the head is deferred
along with the MECH-263 behavioural signatures (devaluation sensitivity,
task-role discrimination) -- both require environment work.

This guarantees `use_ofc_analog=True` is bit-identical to OFF until the head
is deliberately trained, which makes pre-training experiments safe to enable
the flag without risking baseline divergence.

### D2. Outcome-pool weight defaults active (0.5) but harm_dim defaults zero

**Chosen:** outcome_pool_weight defaults to 0.5 (architectural shape preserved)
but harm_dim defaults to 0 (the outcome_proj is not constructed and
outcome contribution is zero). This makes the no-outcome configuration the
no-op default. Experiments that want to exercise the outcome-pool path set
harm_dim explicitly to the agent's z_harm dim and the outcome_proj is
built at construction.

### D3. MECH-263 functional signatures deferred to behavioural EXQs

The five-sub-test landing diagnostic (V3-EXQ-485) validates substrate wiring:
instantiation, gate-modulated update rate, bias zero at init, backward compat,
reset clears state_code. The MECH-263 functional claims -- devaluation
sensitivity and same-sensory / different-task-role discrimination -- require
environment extensions (outcome relabelling between trials,
perceptually-identical / task-distinct state pairs) that are not on any
current V3 roadmap item. They are queued separately and gated on the
appropriate environment work.

## What This SD Enables

- **V3-EXQ-485:** validation experiment for SD-033b landing (five sub-tests:
  instantiation + state_code shape, gate=1 vs gate=0 update modulation,
  bias zero at init, backward compat, reset clears state_code). Smoke PASS
  2026-04-26: 5/5 sub-tests PASS, gate=1 delta ~0.27 vs gate=0 delta=0.0,
  initial bias max-abs=0.0.
- MECH-261 has a SECOND subdivision-side consumer. Combined with SD-033a,
  this exercises the registry across two distinct cortical targets with
  distinct per-mode weights -- the structure MECH-261 was designed to gate.
- MECH-263 falsification path is unblocked at the substrate level. The
  next step (deferred) is the env extension and the behavioural EXQs.
- SD-033 parent advances: SD-033a + SD-033b implemented; SD-033c (dlPFC
  working-memory analog) and SD-033d as remaining candidate subdivisions.

## Related Claims

- SD-033 (parent subdivision architecture)
- MECH-261 (operating-mode-conditioned write-target gating) -- second
  consumer relationship
- MECH-263 (OFC functional signatures) -- this SD is the substrate; the
  behavioural validation is deferred
- SD-032a (SalienceCoordinator) -- gate source
- SD-032b (DACCAdaptiveControl) -- additive composition on E3 score_bias
- SD-033a (LateralPFCAnalog) -- sibling consumer; additive composition on
  E3 score_bias; shared per-candidate z_world summary in agent.py
- MECH-094 (hypothesis_tag write gate) -- generalised via MECH-261;
  no separate check needed in SD-033b

## Implementation Summary (2026-04-26)

**Module:** `ree_core/pfc/ofc_analog.py`
**Config:** `REEConfig.use_ofc_analog` (default False); sub-knobs
`ofc_state_dim` (16), `ofc_update_eta` (0.05),
`ofc_outcome_pool_weight` (0.5), `ofc_bias_scale` (0.1),
`ofc_hidden_dim` (32), `ofc_harm_dim` (0).
**Data flow:** z_world + optional z_harm + gate -> state_code update;
state_code + per-candidate z_world summary -> score_bias -> additive
compose with dACC + lateral_pfc -> E3.select.
**Backward compatible:** disabled by default. When enabled with the
zeroed-last-layer head, initial bias output is exactly zero -- the agent
runs bit-identical to baseline until the head is deliberately trained.
**Smoke test (2026-04-26):** module instantiates; gate=1.0 state_code
delta ~0.27 on single tick; gate=0.0 state_code delta exactly 0.0; initial
bias vector max-abs is exactly zero; reset() zeros state_code. Full
contracts suite 143/143 PASS with the SD-033b substrate landed (master
flag default-OFF preserves bit-identical baseline).
**Validation:** V3-EXQ-485 queued (diagnostic; smoke PASS 2026-04-26).
**Phased training:** deferred along with MECH-263 behavioural signatures.
Current head is frozen-random with zeroed last Linear. A future ablation
that trains the head requires P0 warmup -> P1 frozen-encoder head training
-> P2 eval, plus an env extension supplying devaluation / task-role-
distinct supervision.
