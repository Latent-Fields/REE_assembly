# Literature Summary: MECH-056 / MECH-057

## Claim Tested

- `MECH-056` - Residue pressure should land in trajectory feasibility and commitment gating before representational overwrite.
- `MECH-057` - Precision control should escalate by depth/channel with bounded sensory influence.

## Source

- Yu AJ, Dayan P (2005), *Uncertainty, Neuromodulation, and Attention*, Neuron.
- DOI: `10.1016/j.neuron.2005.04.026`

## Mapping to REE

- The paper formalizes uncertainty-sensitive neuromodulation as dynamic gain control for inference and attention.
- This supports REE's precision-router framing: tune signal weighting first, then allow slower structural adaptation only when uncertainty remains persistent.
- It strengthens a trajectory-first control interpretation because channelized precision modulation can alter selection without immediate representational rewrite.

## Caveats and Mapping Limits

- Source is theory-oriented and predates REE-specific residue constructs.
- It does not directly specify L-space depth boundaries (`z_alpha`/`z_theta`/`z_delta`).

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.68`
- Rationale: strong theoretical fit for precision routing, moderate abstraction gap to REE residue geometry details.
