# SD-009 event-contrastive supervision: target/channel mismatch

**Date:** 2026-07-18
**Status:** AWAITING GOVERNANCE ADJUDICATION
**Raised by:** SD-070 implementation session (`admiring-poincare-1c80af`)
**Concerns:** SD-009, MECH-100, and any claim resting on event-contrastive z_world supervision
**Requested action:** adjudicate at the next `/governance` cycle. **No claim status,
confidence, or evidence weighting was changed by the session that raised this.**

---

## Summary

SD-009 supervises the z_world encoder with a cross-entropy loss that classifies the
environment's `transition_type` from z_world. Measurement on the current substrate shows
that **this target is not decodable from the channel the loss reads**: a probe trained
directly on raw `world_obs`, with no encoder in the path at all, performs at or below
chance. The loss therefore cannot be transmitting the information SD-009 claims it
transmits, in this configuration.

The likely mechanism is a **type mismatch between the target and the encoder**:
`transition_type` is a property of the *transition* (t-1 -> t), whereas z_world is a
*static single-frame* encoding. The information is present in the observation *deltas*, and
concentrated in the **body** delta -- which SD-005's split encoder deliberately routes to
z_self, so z_world structurally cannot see it. On that reading SD-009 is in tension with
SD-005, and the fault is in the wiring, not the labels.

This is raised as a **question for governance, not a verdict.** In particular it does not
by itself demote SD-009 -- see "What this does NOT establish" below.

## Measurement

CausalGridWorldV2 at the x724 `ENV_KWARGS` rung, `use_proxy_fields=True`, exploratory
epsilon-mixed policy (eps=0.35), 60 episodes x 150 steps, n=721 labelled steps, seed 42.
Probe: identical MLP-128 per channel, class-balanced CE, 80/20 split, held-out macro-recall
minus its own chance baseline (chance = 1/k over the k classes with >= 3 held-out examples).

| channel | 3-class map (shipped) | 6-class repaired map |
|---|---|---|
| `world_obs` — **what z_world sees** | **-0.014** | **-0.060** |
| `body_obs` — what z_self sees | +0.121 | +0.144 |
| `body + world` (union) | -0.022 | -0.021 |
| world delta (`w_t - w_prev`) | +0.167 | +0.329 |
| **body delta (`b_t - b_prev`)** | **+0.240** | **+0.427** |
| body delta + body | +0.251 | +0.427 |

Supporting facts from the same rollout:

- **Label saturation.** `agent._EVENT_LABEL_MAP = {"none":0, "env_caused_hazard":1,
  "agent_caused_hazard":2}` maps every other `transition_type` to class 0. The env actually
  emits at least 12 distinct values. Measured raw balance: `hazard_approach` 0.758,
  `resource` 0.181, `env_caused_hazard` 0.042, `none` 0.016, `agent_caused_hazard` 0.004 ->
  mapped `c0=0.952, c1=0.046, c2=0.002`.
- **Rebalancing does not rescue it.** A repaired 6-class map giving `hazard_approach` and
  `resource` their own classes still probes at chance from `world_obs` (-0.060). So the
  finding is *not* reducible to class imbalance.
- **The channel is not information-poor in general.** From the same `world_obs`:
  hazard-in-view 0.961, resource-in-view 0.965, nearest-hazard distance 0.943,
  nearest-resource distance 0.948 (chance 0.5 / 0.5 / 0.333 / 0.333), and the SD-018
  resource-proximity target regresses at R^2 0.794. The world channel is richly decodable
  for *static scene structure*; it is specifically the *transition-type* target that is not.
- **Downstream consequence.** Trained through the encoder, the SD-009 head reaches held-out
  balanced accuracy 0.272-0.311 against chance 0.333 across the whole weight sweep -- i.e.
  it never rises above chance under any weighting tried.

The `body + world` union scoring *below* `body_obs` alone is expected small-sample
behaviour: 287 concatenated dims against 721 samples, with the 12 informative body dims
swamped by 275 world dims. It is noted for completeness and is not part of the argument.

## What this does NOT establish

1. **It does not show SD-009 never worked.** `claims.yaml:7319` records EXQ-020 PASS on the
   SD-009 mechanism (2026-03-20, `selectivity_margin=0.882`), and `claims.yaml:7283` records
   EXQ-023 PASS (2026-03-22, `event_selectivity_margin=0.084`). Those are **not** the
   statistic measured here. `selectivity_margin` is a cosine separation between class-mean
   z_world vectors; held-out classifier accuracy is a decodability statistic. A separation
   margin can be non-zero from *correlates* of the label (e.g. a hazard being in view)
   without the label itself being decodable. **Reconciling the two is exactly the
   adjudication work this artifact is asking for, and the reconciliation offered here is a
   hypothesis, not a finding.**
2. **It does not establish scope beyond the configuration measured.** One env
   (CausalGridWorldV2), one rung (x724 `ENV_KWARGS`), `use_proxy_fields=True`, one policy,
   one seed for the channel probe. EXQ-020/023 ran under different conditions that were not
   reproduced here. In particular, `use_proxy_fields=True` is what floods the label
   distribution with `hazard_approach` / `benefit_approach`; the pre-proxy-field regime may
   behave differently.
3. **It does not adjudicate MECH-100**, the mechanism claim SD-009 implements. MECH-100 may
   be true of the architecture while this particular supervision wiring fails to realise it.

## Candidate governance outcomes

Offered as options, not a recommendation:

- **(A) Scope-limit SD-009.** Add an `evidence_quality_note` recording that the
  event-contrastive supervision is non-transmitting under `use_proxy_fields=True` at the
  x724 rung, leaving status unchanged pending a reconciliation of EXQ-020's statistic.
- **(B) Mark the EXQ-020 / EXQ-023 evidence candidate-stale** pending re-measurement with a
  decodability statistic rather than a separation margin.
- **(C) Re-wire SD-009 rather than retire it.** If the diagnosis holds, the natural repair is
  to supervise the event target from a *delta* input (`z_world_t` vs `z_world_{t-1}`, or an
  explicit transition encoding), or to move the head onto the body/self stream where the
  information actually lives. Either is a substrate change needing its own SD.
- **(D) No action** -- if governance judges the configuration measured here to be outside
  SD-009's claimed operating envelope.

## Relationship to SD-070

SD-070 (`docs/architecture/sd_070_zworld_p0_anticollapse_recipe.md`, IMPLEMENTED
2026-07-18) **routes around** this rather than resolving it: its P0 replaces the
event-contrastive target with static scene-structure targets the world channel demonstrably
determines. SD-070's validity does not depend on how SD-009 is adjudicated, and SD-070 makes
no claim about SD-009's status.

Nothing in this artifact bears on the INV-088 coupling leg, on MECH-459 / return-scale, or
on either leg of the live GOV-FANOUT-1 discrimination.

## Reproduction

- `world_obs` / `body_obs` / delta channel probe: `probe_channel.py`
- decodability ceiling + candidate replacement targets: `probe_decodability.py`
- collapse-channel instrumentation (precision gate refuted): `probe_collapse_channel.py`

All three are session scratchpad scripts; their measurements and constants are reproduced in
full in the SD-070 doc and in `ree-v3/ree_core/latent/zworld_p0.py`'s module docstring, which
are the durable records. Re-deriving them needs only the harness config in
`ree-v3/experiments/_lib/baselines/exq783_zworld_granularity.py`.
