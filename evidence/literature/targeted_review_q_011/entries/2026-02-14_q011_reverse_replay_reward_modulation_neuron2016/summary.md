# Literature Summary: 2026-02-14_q011_reverse_replay_reward_modulation_neuron2016

## Claims Tested

- `Q-011`

## Source

- Ambrose RE, Pfeiffer BE, Foster DJ (2016), *Reverse Replay of Hippocampal Place Cells Is Uniquely Modulated by Changing Reward*.
- URL: `https://doi.org/10.1016/j.neuron.2016.07.047`

## Mapping to REE

- Reverse replay rates increased or decreased with reward changes, while forward replay remained comparatively stable.
- This pattern weakens `Q-011` as a hard minimum entropy-floor requirement, because replay allocation appears context- and reward-adaptive rather than uniformly entropy-preserving.

## Caveats and Mapping Limits

- The results address replay modulation, not direct entropy-floor control variables.
- Findings are from rodent reward-navigation settings and may not transfer directly to abstract deliberation regimes.
- Adaptive replay does not rule out soft entropy regularization under specific tasks.

## Direction and Confidence

- `evidence_direction`: `weakens`
- `confidence`: `0.72`
- Rationale: direct hippocampal replay modulation evidence is strong for policy adaptivity, with moderate uncertainty about exact entropy formalization in REE terms.
