# Literature Summary: 2026-02-14_v3pfc_modelbased_prediction_error_integration_neuron2011

## Claims Tested

- `MECH-060`

## Source

- Daw ND, Gershman SJ, Seymour B, Dayan P, Dolan RJ (2011), *Model-based influences on humans' choices and striatal prediction errors*.
- URL: `https://doi.org/10.1016/j.neuron.2011.02.027`

## Mapping to REE

- The study separates model-based planning influence from model-free learning influence at the behavioral model level.
- Neural analyses also show post-outcome prediction error content that reflects both influences.
- This yields `mixed` evidence for `MECH-060`: it supports computational distinction between planning/control and attribution/learning, while showing biological coupling rather than a perfectly clean split.

## Caveats and Mapping Limits

- The task and readouts do not directly implement REE pre-commit/post-commit channels.
- Measurements are primarily striatal/BOLD correlates and not explicit channelized control-plane state variables.
- The result constrains strict decoupling assumptions but does not falsify engineered dual-stream implementations.

## Direction and Confidence

- `evidence_direction`: `mixed`
- `confidence`: `0.66`
- Rationale: high-quality experimental paradigm with relevant computational dissociation, but only partial observability for REE channel boundaries.
