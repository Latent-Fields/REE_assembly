---
nav_exclude: true
---

# MECH-269b: Symmetric V_s Gating on E1/E2 Cortical Rollouts

**Claim ID:** MECH-269b
**Subject:** cortical_world_model.regional_verisimilitude_rollout_gating
**Status:** IMPLEMENTED 2026-04-26
**Registered:** 2026-04-26
**Instantiates:** MECH-269 (V_s anchor selection on the hippocampal proposer)
**Depends on:** MECH-269, MECH-284, SD-005, SD-010, SD-011, ARC-033
**Blocks:** Q-040 (factorial test of MECH-269b vs SD-032b dACC behavioural-revision); the
EXQ-483 / EXQ-483a wired-but-inert failure mode (override fires, PAG releases up,
approach_commit = 0 across all arms).
**Lit-pull:** `evidence/literature/targeted_review_mech269b_vs_rollout_gating/` (7 entries,
mean conf ~0.69; symmetric-application gap explicit).

---

## Problem

MECH-269 (Phase 1 + Phase 2 i/ii/iii + Phase 3 online arm via MECH-284) gives the
hippocampal proposer a per-stream verisimilitude V_s read-out that gates anchor
selection: an anchor whose V_s_anchor falls below threshold for k consecutive ticks is
marked inactive (dual-trace; Bouton 2004). The proposer then preferentially draws from
anchors whose stream-mixture remains aligned to perception.

That gating stops at the proposer. The cortical world models (E1 sensory predictor and
the E2 forward family -- E2_harm_s ARC-033, E2_harm_a MECH-258, the main z_self
transition) consume the *current-tick* per-stream latents indiscriminately. If a stream
has decayed alignment (V_s low) but the latent value still arrives at full magnitude, E1
predicts the next world from a stale-but-confident-looking input and E2 rolls a forward
trajectory off a stale-but-confident-looking transition starting state. Downstream
consumers -- dACC adaptive control (SD-032b), E3 commit gate, the broadcast override
regulator (SD-037), the closure operator (SD-034) -- see precision-weighted prediction
errors computed against the wrong reference, and produce no corrective behavioural
revision.

This is the wired-but-inert failure mode. EXQ-483 / EXQ-483a (SD-037 broadcast override
4-arm) made it concrete: override_signal mean climbed from 0.0 to 0.56 in the ON arms,
PAG release count rose from 5.3 OFF to 9.0-9.3 ON, but approach_commit stayed at 0.0
across all four arms including the SD-036-only baseline. Every regulator in the V3
control stack fires correctly; nothing in the policy layer revises. MECH-269b is one
candidate root cause; MECH-295 (drive -> liking-stream bridge) is a complementary
candidate. The two are not mutually exclusive and the Q-040 factorial holds the
broadcast-override / dACC / drive-modulation arms ON in both arms so the MECH-269b
contribution is isolated.

---

## Solution

A regulator-layer substrate: **VsRolloutGate**. Per-stream snapshot store + per-stream
per-side threshold table + a single primitive that returns either the current latent value
or its held snapshot when the V_s for that stream falls below the relevant side's
threshold. Two consumers in the agent loop:

1. **E1 side**: gate z_world and z_self before each E1 forward call
   (`predict_long_horizon`, `generate_prior`, `extract_cue_context`).
2. **E2 side**: gate z_harm_a before the per-tick E2_harm_a forward step in
   `select_action()`. The E2_harm_s counterfactual (used in SD-003 / training loops) is
   covered by the same primitive but not invoked from the per-tick agent path.

Snapshot semantics: at each tick, before E1/E2 consume any latent, refresh the snapshot
of stream s to `latent[s].detach().clone()` if `V_s[s] >= snapshot_refresh_threshold`. On
the consume side, `gate(latent_state, side)` returns a copy with each stream replaced by
its snapshot when `V_s[s] < theta_gate[side][s]`. When no snapshot has ever been recorded
(early ticks, V_s never above threshold), the gate passes the current value through
unchanged so the agent never operates on `None` latents.

Held-snapshot, NOT zero / NOT mask: this matches the architectural claim that misaligned
streams contribute "held-snapshot values, NOT current latent values, to the forward
prediction." Zeroing would lose the stream entirely; masking would change downstream
network input shape; the held snapshot keeps the same dimensionality and the same
distribution, but freezes the contribution to its last-trusted value. This is the
analogue of MECH-269 dual-trace: nothing is erased, the current trace just stops being
the operative one.

Per-stream not per-region: V_s is computed per latent stream (z_world, z_self, z_harm_s,
z_harm_a, z_goal, z_beta) by MECH-269 Phase 1; that same flat dict is the gate's
input. Per-region V_s (Phase 2 iii / T4) is consumed by the proposer side; the cortical
rollout gate operates on the per-stream readout because cortical predictors are
stream-typed not region-typed.

### Configuration

All on `REEConfig`, all defaulting to no-op. `from_dims()` accepts the same names.

| Param | Type | Default | Purpose |
|---|---|---|---|
| `use_vs_rollout_gating` | bool | False | master switch |
| `vs_gate_snapshot_refresh_threshold` | float | 0.5 | snapshot refresh fires when `V_s[s] >= this` |
| `vs_gate_streams` | tuple[str,...] | `("z_world","z_self","z_harm_s","z_harm_a","z_goal","z_beta")` | streams covered |
| `vs_gate_e1_threshold` | float | 0.4 | global E1-side threshold (per-stream override below) |
| `vs_gate_e2_threshold` | float | 0.4 | global E2-side threshold |
| `vs_gate_e1_threshold_per_stream` | dict[str,float] | `{}` | per-stream override on E1 side |
| `vs_gate_e2_threshold_per_stream` | dict[str,float] | `{}` | per-stream override on E2 side |
| `vs_gate_unknown_stream_passes` | bool | True | when no snapshot or no V_s, passthrough current value |

Per-stream override is a dict so a single stream can have an asymmetric setting (e.g.
z_harm_s tighter on the E1 side because sensory predictions are noisier when nociceptive
alignment drifts) without bloating the constructor signature.

### Data flow

```
encode() -> LatentState
  -> hippocampal.update_per_stream_vs(latent, goal_state)  # MECH-269 Phase 1
  -> [if use_vs_rollout_gating]
       vs_rollout_gate.update_snapshots(latent, hippocampal.per_stream_vs)
  -> sense() returns latent

_e1_tick(latent, ...)
  -> [if use_vs_rollout_gating]
       gated = vs_rollout_gate.gate(latent, side="e1")
     else gated = latent
  -> total_state = cat(gated.z_self, gated.z_world)
  -> e1(total_state, z_goal=...) / extract_cue_context(gated.z_world)

select_action(latent, ...) -- E2_harm_a step:
  -> [if use_vs_rollout_gating]
       z_harm_a_in = vs_rollout_gate.gate_stream("z_harm_a", _harm_a_prev, side="e2")
     else z_harm_a_in = _harm_a_prev
  -> e2_harm_a(z_harm_a_in, action)
```

### Diagnostics

`VsRolloutGate` exposes:

- `snapshots: dict[str, Tensor]` -- last-trusted value per stream
- `per_stream_held_count_e1: dict[str, int]` -- how many ticks each stream's E1 input was held
- `per_stream_held_count_e2: dict[str, int]` -- same on E2 side
- `per_stream_refresh_count: dict[str, int]` -- snapshot refreshes per stream
- `last_held_e1: dict[str, bool]` / `last_held_e2: dict[str, bool]` -- this-tick state

These are the falsifiable per-arm metrics for the Q-040 validation experiment.

---

## Architecture context

MECH-269 (proposer-side V_s) and MECH-269b (cortex-side V_s) are siblings under a single
shared V_s computation. Phase 1 already populates `hippocampal.per_stream_vs` with the
flat per-stream dict; MECH-269b is a *consumer* of that dict, not a competing producer.
Per the lit-pull SYNTHESIS (`targeted_review_mech269b_vs_rollout_gating/`), the
symmetric-application novelty -- one V_s vector consumed by both proposer anchor
selection and cortical forward predictors -- is the load-bearing architectural
commitment. The cortical-side primitive (precision-weighted PE gating in cortex,
Bastos 2012; Feldman & Friston 2010; Kanai 2015) is well-supported; the symmetric
half is genuinely novel ground.

The gate is intentionally outside `LatentStack.encode()` because:

1. Encoding is differentiable; gating decisions consume `per_stream_vs` which is computed
   *after* encoding and is not part of the loss graph.
2. The gate produces a *consumed copy* of `LatentState` for the rollout sites, leaving
   the canonical latent stream (used by training losses, residue accumulation, valence
   updates, etc.) unchanged. Only forward predictors see the gated copy.

This separation preserves all existing training pipelines bit-identically: aux losses
on z_world, z_harm_s, z_harm_a, z_goal continue to operate on the un-gated stream because
the gate is invoked only at the E1/E2 forward call sites.

### Relationship to other claims

| Claim | Relationship |
|---|---|
| MECH-269 (parent) | provides `per_stream_vs` dict that this consumer reads |
| MECH-284 | online staleness accumulator -- V_s_anchor with staleness goes to proposer; this gate consumes the raw V_s without staleness adjustment |
| MECH-098 | reafference cancellation feeds V_world -- one signal source for the V_s vector, not the gating mechanism itself |
| MECH-269b | THIS DOC -- cortical-side gate consumer of MECH-269 V_s |
| MECH-295 | complementary candidate cause of EXQ-483 wired-but-inert; not mutually exclusive with MECH-269b; Q-040 factorial isolates this one |
| ARC-033 / MECH-258 | E2_harm_s / E2_harm_a forward models; this gate decides whether their input streams come from current latent or held snapshot |
| SD-016 | `extract_cue_context(z_world)` consumes z_world; gated when E1 side fires on z_world |

---

## What this SD enables

- **Q-040** (open question registered 2026-04-26): is V_s generalisation to E1/E2
  forward predictions the missing link that unblocks SD-032b dACC behavioural-revision
  on the EXQ-483 wired-but-inert failure mode? PASS = MECH-269b ON arm produces non-zero
  approach_commit AND non-zero dACC-driven score-bias contribution; FAIL points at
  upstream blockers (MECH-295 liking-bridge).
- A read-side closure for V_s on the cortical predictor surface, parallel to MECH-269 /
  MECH-090's `use_vs_commit_release` read-side closure for behavioural commitment.
- A per-stream falsifiable signature for clinical aberrant-precision phenotypes
  (psychosis-spectrum, autism-spectrum) -- corroborative not primary evidence.

---

## ML/AI engineering notes

The gate is a *per-stream gain* primitive at the input to a forward predictor. Standard
ML parallels:

- **Stop-gradient on the snapshot (held value)**: the snapshot is `.detach().clone()` so
  gradients never flow back through the held-substitute path. This prevents the gate from
  silently injecting gradients from a stale state into encoder training. Standard EMA /
  target-network discipline.
- **Held-value vs zero-mask**: zero-masking inputs to a learned downstream model is
  known to confuse models that did not see masked inputs at training time; the held value
  preserves shape and approximate distribution. Same reasoning behind BERT's `[MASK]`
  token vs straight zeros.
- **Hysteresis on the gate**: not introduced in this implementation. The
  snapshot_refresh_threshold (0.5) sits comfortably above the gate threshold (0.4) so a
  stream straddling 0.4-0.5 oscillates between holding and refreshing within a band; this
  is intentional (Schmitt-trigger style hysteresis lite, mirroring MECH-269 anchor-set
  k-streak design). True per-tick streak counters are the next refinement once the
  primitive validates.
- **Default no-op**: `vs_gate_e1_threshold = vs_gate_e2_threshold = 0.4` means with V_s
  initialised to 1.0 and the EMA at tau=0.1, the gate effectively never fires on a
  well-aligned agent; it engages only when V_s drifts under the kind of perception drift
  MECH-287 broadcasts respond to. This avoids degrading baseline behaviour while
  surfacing the held-snapshot path under the failure-mode conditions.

What NOT to import from ML:

- **Trainable gate**: the gate is non-trainable scalar arithmetic; making it learnable
  would couple it to the loss graph and turn it into a per-stream attention layer, which
  is architecturally a different claim.
- **Soft gating**: temptation is to interpolate `lambda * current + (1 - lambda) *
  snapshot` with `lambda = sigmoid(V_s)`; per the SD spec the architectural commitment
  is hard threshold + held snapshot. Soft interpolation would lose the falsifiable
  per-stream held-count signature.

---

## Phased training

Not applicable. The gate is non-trainable arithmetic; no parameters; no encoder warmup
needed.

---

## MECH-094 (hypothesis tag) compliance

The gate runs only inside the waking call sites (`agent.sense`, `agent._e1_tick`,
`agent.select_action`). It does not author replay / simulation content. No
`hypothesis_tag` check is required because call-site scoping is the gate (same pattern
as MECH-269 Phase 1 / Phase 2 ii / 2 iii, MECH-288, MECH-287, MECH-284).

If a future caller invokes `vs_rollout_gate.gate(...)` from a replay path, the gate would
return held-snapshot values for misaligned streams in the replayed content -- which is
behaviourally correct for replay too, but the diagnostic counters would conflate waking
and replay holds. A `simulation_mode` argument can be added without API breakage when a
replay consumer is wired.

---

## MECH-284 staleness wiring (Q-040b strong reading, 2026-04-29)

The substrate landed 2026-04-26 used raw `per_stream_vs[s]` against fixed side
thresholds (default 0.4). EXQ-490 / 490b / 490c all had to override the
thresholds to smoke values (0.85 / 0.85 / 0.95) to make the gate fire under
realistic V_s readings. That made the diagnostic "C1 fires" trivially true and
left the strong-reading question -- can the gate discriminate STALE from
ALIGNED streams without a smoke override -- untestable.

The 2026-04-29 follow-up wires MECH-284 region staleness into the threshold
comparison:

```python
if config.use_staleness_lookup and per_stream_staleness is not None:
    effective_vs = raw_vs - per_stream_staleness[stream]
    if effective_vs >= side_threshold:
        passthrough
    else:
        hold (substitute snapshot)
```

`per_stream_staleness` is aggregated by
`HippocampalModule.compute_per_stream_staleness()` via:

```
For each stream s currently tracked by per_stream_vs:
    staleness[s] = max over active anchors a where s in a.stream_mixture
                   of staleness_accumulator.lookup_by_anchor_key(a.key)
```

`max` (not mean) captures the worst staleness the stream is currently exposed
to: a stream's V_s is a global readout but the underlying staleness lives per
(scale, segment_id) region; if any region the stream participates in is stale,
the gate should treat the stream as stale. Mean would dilute under multi-region
coverage.

REEAgent caches the dict once per waking tick (top of `_e1_tick`) and reuses it
for both the E1 gate call and the E2_harm_a gate_stream call later in
`select_action`. The aggregator is pure arithmetic over the existing
StalenessAccumulator + AnchorSet state -- no new persistent state.

**Configuration.** A new master flag `use_vs_gate_staleness_lookup` (default
False) turns the wiring on. When True, agent build raises ValueError unless
`use_staleness_accumulator=True` AND `use_anchor_sets=True` -- the aggregator
has nothing to walk otherwise. The legacy raw-V_s path (default-OFF) is
retained byte-for-byte for backward compatibility with EXQ-490 / 490b / 490c.

**Q-040b acceptance.** With this wiring, V3-EXQ-490d (the 490c successor) can
run without smoke threshold overrides: under sustained MECH-287 broadcast
activity the staleness on stale-region anchors climbs, per-stream staleness
follows, effective_vs falls below the realistic 0.4 threshold, and the hold
path fires. C1 (gate fires) becomes a non-trivial measurement; C4 (severance:
holds vanish when staleness lookup is OFF) becomes the falsifiable test of
the strong reading.

**MECH-094 compliance.** `compute_per_stream_staleness()` is invoked only from
`_refresh_vs_gate_staleness()` which itself is invoked only from `_e1_tick()`,
a waking-stream call site. Replay / simulation paths must not call it. Same
call-site-scoping pattern as MECH-269 Phase 1 / 2 ii / 2 iii, MECH-288,
MECH-287, MECH-284.

**Diagnostics.** `vs_gate_staleness_lookup_calls` counts the number of times
the aggregator subtracted a staleness scalar this episode.
`vs_gate_max_staleness_<stream>` records the per-stream max staleness the gate
has been asked to subtract this episode. Both reset per-episode.

**Out of scope (deferred).**
* Per-region cortical gate (would consume per_region_vs directly; requires
  region-typed E1/E2; deferred to V4 -- listed under open architectural
  alternatives below).
* Staleness-aware snapshot refresh (current refresh path uses raw V_s only; if
  a stream's region staleness is high, snapshot refresh continues, capturing
  fresher live content but the gate's hold decision uses the staleness-adjusted
  V_s. Whether to also gate the refresh side is an open question for a
  follow-up pass, not addressed here).

---

## Backward compatibility

`use_vs_rollout_gating=False` by default. With the flag off, `agent.vs_rollout_gate` is
None and every integration site is a no-op. Existing experiments unaffected. With the
flag on but V_s at its default 1.0 seed and aligned latents (typical first-100-tick
behaviour), the gate fires zero times -- bit-identical to flag-off in the well-aligned
regime. Held-snapshot substitutions appear only when V_s drops below threshold, which is
the intended falsifiable signature.

---

## Validation experiment

V3-EXQ-490 (queued in same pass as substrate landing): Q-040 factorial. Two arms ON_OFF
(MECH-269b OFF) and ON_ON (MECH-269b ON), both arms with use_broadcast_override=True,
use_dacc=True, GoalConfig.drive_weight=2.0 (SD-012 ON), full V_s invalidation circuit
ON (use_per_stream_vs / use_event_segmenter / use_invalidation_trigger / use_anchor_sets
/ use_per_region_vs / use_staleness_accumulator / use_mech284_hysteresis /
use_vs_commit_release). 3 seeds. Acceptance:

- C1: V_s gating physically wired -- in the ON_ON arm, at least one stream's
  `per_stream_held_count_e1` or `per_stream_held_count_e2` registers > 0 across the run.
- C2: Differential approach -- ON_ON arm produces approach_commit > 0 in at least 2 / 3
  seeds; ON_OFF arm reproduces the EXQ-483 zero-baseline.
- C3: dACC behavioural-adjustment magnitude -- ON_ON arm shows non-zero
  `dacc_score_bias_magnitude` consistent with PE flowing to E3 score-bias; ON_OFF arm
  is approximately zero.

If C1 fails the substrate is not wired correctly (debug). If C1 passes but C2/C3 fail
that is the Q-040 FAIL branch and points evidence toward MECH-295 (liking-bridge) as
the dominant blocker. If C1+C2+C3 all pass, MECH-269b is the missing link and the
architectural commitment is supported (one piece of substrate evidence, not full
promotion).

`experiment_purpose = "diagnostic"`. Substrate validation, not direct claim governance.

---

## Open architectural alternatives (DESIGN-DOC ONLY -- not implemented)

A. **Soft sigmoid gate** -- `lambda = sigmoid((V_s - theta) * gain)` with held =
   `lambda * current + (1-lambda) * snapshot`. Smoother behavioural transitions; loses
   per-stream held-count diagnostic; not the architectural commitment. Would need its
   own claim if adopted.

B. **Per-region cortical gate** -- consume `hippocampal.per_region_vs` instead of
   `per_stream_vs`. Requires E1/E2 to be region-typed, which they are not in V3.
   Deferred.

C. **Streak-counter hysteresis** -- like MECH-269 anchor-set's `hysteresis_k`, require
   k consecutive below-threshold ticks before holding. Would smooth out single-tick
   oscillations at the cost of a slower response. Deferred to a follow-up
   refinement-pass after V3-EXQ-490 lands data on the raw threshold gate.

D. **Trainable per-stream gain head** -- replace scalar V_s with a learned head off
   `[per_stream_vs vector + tick_context]`. Substantively different claim
   (precision-as-attention rather than precision-as-V_s); would need its own SD entry.
