# SD-033a: Lateral-PFC-analog (mid-lateral rule/goal substrate)

**Claim ID:** SD-033a
**Subject:** pfc.lateral_pfc_analog
**Status:** IMPLEMENTED 2026-04-20
**Depends on:** SD-033, MECH-261, MECH-262 (MECH-116 deferred)
**Blocks:** MECH-261 write-gate-landing-consumer validation, MECH-262 rule-persistence
experiments, downstream SD-033b/c/d integrations that read rule-biased E3 scores.
**Parent design:** `sd_033_pfc_subdivision_architecture.md`

## Problem

MECH-261 is a dict-keyed write-gate registry on SD-032a (SalienceCoordinator).
It produces `write_gate(target) -> float in [0, 1]`. V3-EXQ-453 validates the
registry's shape and autonomic-target landing, but it does not yet have any
cortical-subdivision consumer that uses `write_gate("sd_033a")` as a
carrier-rhythm-analog admission predicate on an actual rule/goal substrate.
Without a consumer, MECH-261's claim (that mode-conditioned gating routes
offline writes to the right target) cannot be mechanistically tested on the
subdivision the spec designates as its primary customer.

SD-033a is specified by four functional signatures in the parent architecture
doc: (i) stimulus-abstracted rule format, (ii) distractor-resistant
persistence, (iii) top-down bias into E3, (iv) training-dependent emergence.
The MECH-261 spec assigns the following per-mode weights to sd_033a:
`external_task=1.0, internal_planning=1.0, internal_replay=0.05,
offline_consolidation=0.3`. The gate, therefore, licenses rule persistence
most during waking task engagement and during internal planning, suppresses
it during internal replay (rule persistence during DMN-style replay would be
psychosis-adjacent), and partially opens it during offline consolidation.

## Solution

Non-trainable arithmetic with a small frozen-random bias head whose last
`nn.Linear` is zeroed at init so the initial bias output is exactly zero.

**Module:** `ree_core/pfc/lateral_pfc_analog.py` (LateralPFCAnalog,
LateralPFCConfig). Agent-side wiring in `ree_core/agent.py` (`select_action`
tick block, `reset`, `__init__`).

**State:** `rule_state: torch.Tensor` buffer, shape `[1, rule_dim]`
(default rule_dim=16). Persistent across ticks within an episode.

**Update rule (rule persistence + rule writing, signature ii):**

```
gate = SalienceCoordinator.write_gate("sd_033a")   # in [0, 1]
eff_eta = update_eta * clip(gate, 0, 1)            # update_eta=0.05 default
source = delta_proj(z_delta) + world_pool_weight * world_proj(z_world)
rule_state <- (1 - eff_eta) * rule_state + eff_eta * source
```

Gate near zero (e.g. `internal_replay` where weight is 0.05) -> rule_state
nearly frozen; gate near 1 (external_task / internal_planning) -> rule_state
tracks source with ~20-step rise time. This is the REE-layer analog of the
Latchoumane out-of-phase falsification: when the mode-signal is nominally
elevated but the gate is suppressed (SWS / replay), the rule-update amplitude
is suppressed even if a raw signal is present.

**Read path (top-down bias into E3, signature iii):**

```
for each candidate trajectory c_k:
    summary_k = first-step z_world of c_k   # from c_k.world_states[:, 0, :]
joined = concat([rule_state.expand(K, -1), summaries], dim=-1)
bias_raw = rule_bias_head(joined).squeeze(-1)          # [K]
score_bias = clamp(bias_raw, -bias_scale, +bias_scale)  # bias_scale=0.1 default
```

Composed additively with dACC `score_bias` before E3.select(). E3 convention
is lower-is-better, so positive bias penalises a trajectory (rule-inconsistent
trajectories get higher cost).

**MECH-094 treatment:** MECH-261 generalises the hypothesis_tag semantics.
write_gate("sd_033a") = 0.05 under internal_replay means replay content cannot
meaningfully update rule_state. The gate IS the tag, via the registry. No
separate hypothesis_tag check is needed in LateralPFCAnalog.

**Stimulus-abstracted rule format (signature i):** rule_state is a
`[1, rule_dim]` latent. The two projections (delta_proj, world_proj) feed
into the same rule space, decoupled from raw perceptual templates.

**Training-dependent emergence (signature iv):** The bias head is an
`nn.Module` but in this landing implementation it is frozen-random with
the LAST `nn.Linear` weights and bias zeroed at init so initial output is
exactly zero. A trained-head variant is a deliberate deferred choice
(see DESIGN ALTERNATIVES below).

## Design Alternatives (load-bearing -- documented per user guidance 2026-04-20)

Three choice-points exist in this landing implementation. Each has a
documented alternative and a queued lit-pull task
(`REE_assembly/evidence/planning/task_inbox.md`) so a later pass can revisit
if the landing choice turns out empirically wrong.

### A1. Per-candidate bias vs uniform bias

**Chosen:** per-candidate. The bias head takes
`concat([rule_state, per-candidate z_world summary]) -> scalar`, producing
a `[K]`-shaped bias vector where K = num_candidates.

**Alternative:** a single scalar bias applied uniformly to every candidate
(rule_state -> scalar via a state-only head). This is the simpler design
and closer to "state-dependent gain" rather than "trajectory-conditional
eval."

**Lit-pull question (task_inbox 2026-04-20):** does biological lateral PFC
produce trajectory-specific top-down bias, or a uniform state-dependent
gain? Miller & Cohen 2001 framing assumes conditional-on-state rule-biasing;
Mansouri 2020 spiking evidence is mixed. If biology favours uniform-gain,
this is a simpler structural choice with a clean falsification signature
(bias vector should be K-constant).

### A2. Frozen-random bias head with last layer zeroed vs trained head

**Chosen:** frozen-random, last-Linear weights and bias zeroed at init so
initial output is exactly zero. Head parameters are registered but not
added to any optimizer by default. Phased-training for the head is deferred.

Rationale: SD-033a signature (iv) is training-dependent emergence; a trained
head requires an identifiable training target which V3 does not yet have
(the nearest candidates are supervised rule-relevant labels or
reinforcement-style gradient from E3 action outcomes -- both scope-expansions).

**Alternative:** trained head via the standard phased-training protocol (P0
encoder warmup -> P1 frozen-encoder head training on detached latents ->
P2 eval). This would instantiate signature (iv) as a causal claim rather
than as a deferred flag.

**Lit-pull question (task_inbox 2026-04-20):** how is the lateral-PFC
rule-bias projection shaped by learning, and on what training signal?
Evidence on training-dependent emergence should determine whether a V4
pass should add a phased-training loop, and if so, what the target is
(rule-label supervision? policy gradient? something else?).

### A3. Gate-modulated EMA persistence vs recurrent GRU / synaptic hold

**Chosen:** gate-modulated EMA.
`rule_state <- (1 - base_eta * gate) * rule_state + base_eta * gate * source`.
Simple scalar arithmetic, no recurrence, no learned persistence dynamics.

**Alternatives:**
- Recurrent GRU / GRUCell with gate as an auxiliary input (Mansouri 2020
  recurrent-activity-based persistence story).
- Synaptic-hold: short-term plasticity parameter slow relaxation;
  silent-synapse / short-term facilitation mechanism for non-activity-based
  persistence.

**Lit-pull question (task_inbox 2026-04-20):** is rule persistence in
biological lateral PFC recurrent activity (spiking persistence) or
synaptic-hold (short-term plasticity based)? Directly affects whether EMA
is a biologically reasonable compression or a misleading simplification.
If synaptic-hold is dominant, the EMA fails to capture the characteristic
slow-relaxation timescale; if recurrent-activity, a GRU would be a
tighter structural analog.

## Architecture Context

SD-033a is the primary consumer of MECH-261's write_gate registry as
realised on SD-032a (SalienceCoordinator). Its bias output composes
additively with SD-032b's dACC bias via `score_bias` on E3.select(). This
makes the composition order:

```
E3_bias = dacc_bias + lateral_pfc_bias
```

(Both lower-is-better.) dACC handles cost-of-control and payoff/effort
integration; lateral-PFC handles rule-conformity. These are distinct
biological circuits (ACC vs dlPFC/vlPFC axis) and their bias signals
are architecturally separate.

SD-033a interacts with SD-032a via the gate only. It does NOT consume
operating_mode as a soft vector; the gate is already a projection of
operating_mode through the per-target weight table. Future SD-033
subdivisions (b/c/d) will each consume their own per-subdivision gate
the same way.

Reset is per-episode (agent.reset -> lateral_pfc.reset -> rule_state.zero_).
rule_state does NOT persist across episodes, which is a V3 simplification --
SD-033a spec does not require cross-episode rule carry-over for the
current experiment slate. If a cross-episode rule-carry-over experiment
is later queued, this becomes a V4 extension.

## What This SD Enables

- **V3-EXQ-456:** validation experiment for SD-033a landing (five
  sub-tests: instantiation, gate-modulated update rate, bias reaches E3
  with zero-init contract, backward compat, reset clears rule_state).
- MECH-261 has a subdivision-side consumer. A future experiment can
  exercise the Latchoumane falsification analog: deliberately decouple
  the rule-update source from the gate-high mode and confirm the
  rule_state does not drift, even when mode=external_task.
- MECH-262 (rule-selective persistence) has a concrete substrate and can
  be experimentally probed.
- SD-033 parent can set SD-033a status to IMPLEMENTED, leaving SD-033b/c/d
  as the remaining candidate subdivisions (V3 or V4 depending on scope).

## Related Claims

- SD-033 (parent subdivision architecture)
- MECH-261 (operating-mode-conditioned write-target gating) -- primary
  consumer relationship
- MECH-262 (rule-selective persistence) -- this SD is the substrate
- SD-032a (SalienceCoordinator) -- gate source
- SD-032b (DACCAdaptiveControl) -- additive composition on E3 score_bias
- MECH-094 (hypothesis_tag write gate) -- generalised via MECH-261;
  no separate check needed in SD-033a

## Implementation Summary (2026-04-20)

**Module:** `ree_core/pfc/lateral_pfc_analog.py`
**Config:** `REEConfig.use_lateral_pfc_analog` (default False); sub-knobs
`lateral_pfc_rule_dim` (16), `lateral_pfc_update_eta` (0.05),
`lateral_pfc_world_pool_weight` (0.5), `lateral_pfc_bias_scale` (0.1),
`lateral_pfc_hidden_dim` (32).
**Data flow:** z_delta + z_world + gate -> rule_state update; rule_state +
per-candidate z_world summary -> score_bias -> additive compose with dACC
-> E3.select.
**Backward compatible:** disabled by default. When enabled with the
zeroed-last-layer head, initial bias output is exactly zero -- the agent
runs bit-identical to baseline until the head is deliberately trained.
**Smoke test (2026-04-20):** module instantiates; gate=1.0 rule update norm
~0.1 after single tick; gate=0.0 rule update exactly 0.0 (delta < 1e-6);
initial bias vector is exactly zero; reset() zeros rule_state. E2E five-
tick loop with SD-033a ON hits same multinomial-on-untrained-E3 edge case
as the baseline SD-033a-OFF agent -- confirmed not caused by this SD.
**Validation:** V3-EXQ-456 queued (diagnostic).
**Phased training:** deferred. Current head is frozen-random with zeroed
last Linear. A future ablation that trains the head requires P0 warmup ->
P1 frozen-encoder head training -> P2 eval.
