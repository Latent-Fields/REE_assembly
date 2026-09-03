# V3-EXQ-978 -- SD-018 directional resource-field head validation

Outcome: **FAIL** (directional_head_did_not_change_zworld_at_this_operating_point)

| arm | mean res/ep | seeds supra 1.0 floor | held-out field decode r2 | z_world PR |
|---|---|---|---|---|
| field_loss_off | 0.2667 | 0/3 | 0.7099108375254861 | 3.986 |
| field_loss_on | 0.2833 | 0/3 | 0.7092775745104517 | 3.989 |

Anchor: local_view_greedy worst seed = 45.7500 against the 1.0 floor (cell local_view_greedy|seed42).

PASS iff C_on_clears_floor (load-bearing) AND C_off_subfloor_replication. C_decode_lift is REPORTED, not gating: it attributes a lift rather than producing one, and a lift with a flat decode is a real and interesting result (it would mean the auxiliary loss helped by some route other than exposing the gradient) that must not be suppressed into a FAIL.

The reader is PPO on z_world alone (32 dims) in BOTH arms -- no side-channel, unlike 948.
The manipulation is upstream, in the P0a objective, at resource_field_weight=0.5.

A fishtank episode log companion is written alongside this manifest and is rendered by
REE_assembly's /fishtank_viz.html. It is a SEPARATE observational pass, not the scored data:
per step it carries the agent's position, the true resource-gradient argmax, and (ON arm) the
argmax z_world's own head predicts -- so the amend's subject matter is directly watchable.
