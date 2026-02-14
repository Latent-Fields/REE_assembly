# Literature Summary: 2026-02-14_v3hippo_future_path_replay_nature2013

## Claims Tested

- `ARC-007`
- `ARC-018`
- `MECH-033`
- `MECH-056`

## Source

- Pfeiffer BE, Foster DJ (2013), *Hippocampal place-cell sequences depict future paths to remembered goals*.
- URL: `https://www.nature.com/articles/nature12112`

## Mapping to REE

- During awake sharp-wave ripple events near choice points, hippocampal sequences were observed to represent trajectories ahead of the animal and often toward remembered goals.
- This supports REE assumptions that hippocampal machinery can generate candidate trajectory rollouts rather than only replaying past episodes.
- The result strengthens `ARC-007` and `ARC-018` and supports `MECH-033` as a rollout interface hypothesis.

## Caveats and Mapping Limits

- The evidence is from rodent spatial navigation tasks; transfer to abstract non-spatial planning requires additional support.
- The study does not directly measure REE control-plane precision channels or commitment-stage channel separation.
- It supports rollout generation but not by itself the full `MECH-056` residue placement claim.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.79`
- Rationale: direct neural sequence evidence for prospective rollout behavior with moderate abstraction gap to REE module boundaries.
