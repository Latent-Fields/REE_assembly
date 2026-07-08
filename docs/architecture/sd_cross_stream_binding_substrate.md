# SD: cross_stream_binding_substrate

**Claim ID:** cross_stream_binding_substrate (named substrate; unregistered candidate `entities/selection.coherence_nonreducibility`)
**Subject:** latent.cross_stream_binding
**Status:** IMPLEMENTED (2026-07-08; validation V3-EXQ-720 queued)
**Registered:** 2026-07-08
**Depends on:** E2FastPredictor.rollout_with_world (SD-005 self/world split), MECH-089 (theta-gamma nesting, conceptual), MECH-270 (ephaptic coupling, conceptual)
**Blocks:** V3-EXQ-720 (641a retest on enriched substrate), `entities/selection.coherence_nonreducibility` candidate registration, INV-002 (coherence includes temporal/phase binding), the two 2026-04-23 intakes (binding + path_integral)

## Problem

The failure autopsy `failure_autopsy_V3-EXQ-641a_2026-06-06` (status: confirmed)
adjudicated V3-EXQ-641a as a **substrate ceiling, not a falsification**. With a
fair, contrast-matched control (shuffle-of-real-C), cross-stream phase-alignment
C(tau) over the `world_states` (z_world) and `states` (z_self) rollout streams
carried **no selection information beyond E**: coherence-specificity was 1/6
seeds (need 4), and the shuffle diverged >= the real coherence in 4/6 seeds.

The root cause is structural, and it is in exactly one place. In
`E2FastPredictor.rollout_with_world` (`ree-v3/ree_core/predictors/e2_fast.py`),
each candidate rollout advances the two streams with **two independent forward
models**:

```
z_self  = predict_next_self(z_self, action)   # E2 self transition (self_dim -> self_dim)
z_world = world_forward(z_world, action)       # E2 world transition (world_dim -> world_dim)
```

The **only** shared input is `action`. z_self's evolution never sees z_world and
vice versa; there is no common latent cause. Any co-variation between the two
streams' step-deltas is therefore whatever the shared action already induces --
which is precisely what E (the substrate's own per-candidate cost
`e3.score_trajectory`) already scores. Cross-stream coherence is a
reparameterisation of "these candidates share an action-mode", so it is
functionally redundant with E. This matches the autopsy signature exactly:
"the read has the symbol of cross-stream coherence but the V3 streams need not
carry the functional binding".

For coherence to carry selection information non-reducible to E, the two streams
must be **genuinely bound** -- share a common latent factor that co-drives both
rollouts and is not itself an image of the action/E.

## Solution

Introduce a **shared binding factor** into the candidate rollout, injected into
both stream transitions, gated behind a no-op-default flag.

### Mechanism (`CrossStreamBinder`, `ree_core/latent/cross_stream_binder.py`)

At each rollout step `t`, from the **joint** pre-transition state:

```
g_t = tanh( W_enc . [z_self_t ; z_world_t] )        # [B, bind_dim]  shared factor (joint cause)
b_t = W_out . g_t                                    # [B, bind_out_dim]  common perturbation
```

`bind_out_dim = min(self_dim, world_dim)`. The **same** perturbation `b_t` is
added to the first `bind_out_dim` components of **both** post-transition states,
scaled by a theta-gated strength:

```
gate_t = 0.5 * (1 + cos(2*pi*t / theta_period))      # MECH-089 theta window (gamma nested in theta)
k_t    = strength * gate_t
z_self [.., :bind_out_dim] += k_t * b_t
z_world[.., :bind_out_dim] += k_t * b_t
```

Because `b_t` is derived from the joint `(z_self_t, z_world_t)` state and is
added **identically** into both streams, the two streams' step-deltas now share
an explicit common component. Cross-stream delta-alignment (the harness's read)
now reflects a real shared latent factor whose trajectory is a genuine
per-candidate signature -- and permuting the per-candidate coherence values
(the SPEC shuffle control) destroys the candidate<->value correspondence.

### Why fixed (untrained) projections, not a learned head

`W_enc`, `W_out` are **fixed** `nn.Linear` maps, initialised deterministically
under the caller's seed. This is a deliberate, load-bearing choice:

1. **The retest cannot train a new head.** The 641a harness runs `agent.eval()`
   with online-only updates (`record_transition` + `update_z_goal`); it has no
   P0 curriculum for a new encoder. A learned binder would be
   untrained-random in the retest and prove nothing. So **phased training does
   NOT apply** to this SD.
2. **A fixed shared field is the minimal substrate that creates genuine
   binding.** The scientific question is whether *bound* streams (sharing a
   common latent cause) make coherence non-reducible -- not whether a *learned*
   binder helps. A fixed, joint-state-dependent shared perturbation is the
   smallest change that installs a genuine common cause. This is the
   ephaptic-field analog (MECH-270): a shared field that co-located populations
   both feel, imposed structurally rather than learned.
3. A **learned** binder (contrastive co-encoding, event-segment-conditioned
   shared factor) is a natural V4 extension but is explicitly out of scope here.

### Config (E2Config; all no-op default)

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `cross_stream_binding_enabled` | bool | `False` | master switch (OFF = byte-identical) |
| `cross_stream_binding_dim` | int | `16` | shared-factor dim (`bind_dim`) |
| `cross_stream_binding_strength` | float | `0.15` | coupling scale `strength` |
| `cross_stream_binding_theta_period` | int | `4` | theta window period in rollout steps (MECH-089) |

The `CrossStreamBinder` submodule is constructed on `E2FastPredictor` **only
when the master switch is enabled** -- so with the flag OFF no parameters are
created, no RNG is consumed at construction, and every existing experiment is
bit-identical.

## Architecture Context

- **Blast radius.** `rollout_with_world` is called by the hippocampal proposer
  (`hippocampal/module.py`) and the SD-003 attribution pipeline. With the flag
  ON, all candidate rollouts get the coupling; with the flag OFF (default),
  nothing changes anywhere.
- **No online-model contamination.** The coupling alters only the *imagined*
  rollout states used for candidate scoring/selection. The online E2 self-model
  update (`record_transition`) uses the *observed* z_self from `agent.sense`,
  not rollout states -- so binding never leaks into training targets.
- **MECH-089 (theta-gamma nesting).** The per-step shared code `b_t` is the
  gamma-rate content; the `theta_period` cosine gate is the theta window it
  nests within -- a structural realisation of the cross-frequency temporal
  packaging MECH-089 asserts. This is conceptual grounding, not a claim that
  MECH-089's ThetaBuffer is reused.
- **MECH-270 (ephaptic coupling).** The identical additive perturbation into
  both streams is the field-mediated shared-cause analog.
- **MECH-094 (hypothesis-tag write gate): does NOT newly apply.** The binder
  adds no memory-write surface and does not change `hypothesis_tag` semantics.
  Candidate rollouts keep their existing tags; the retest is a waking
  select-action diagnostic (`simulation_mode=False`). If a future experiment
  enables binding during replay-with-write, the existing `hypothesis_tag`
  machinery already governs that content unchanged.

## What This SD Enables

- **V3-EXQ-720** -- the 641a harness (E-orthogonal cross-stream-only coherence
  read + shuffle-of-real-C contrast-matched control) re-run with
  `cross_stream_binding_enabled=True`. Pass gate (pre-registered, identical to
  641a's): `>=4/6` seeds coherence_specific, real `frac_state_div_gated`
  exceeds shuffle by margin `>= 0.05`.
- On PASS: register the candidate `entities/selection.coherence_nonreducibility`
  (governance) and close both 2026-04-23 intakes positive; INV-002's
  temporal/phase-binding clause gains substrate support.
- On FAIL: the binding hypothesis is falsified *for this substrate design* --
  route `/failure-autopsy` to decide whether the fixed-field design is
  inadequate (V4 learned-binder) or the intakes close.

## Related Claims

INV-002 (coherence includes temporal/phase binding), MECH-089 (theta-gamma
nesting), MECH-094 (hypothesis-tag write gate), MECH-270 (ephaptic coupling),
MECH-269 (per-stream verisimilitude), ARC-006 (entities and binding), ARC-018
(rollout viability), candidate `entities/selection.coherence_nonreducibility`.
