> **Elaborates Section 4.6 (Offline Integration / Sleep) of `REE_CORE.md`.**

# Sleep Contract (Required Interface)

## Purpose
Offline sleep integrates experience accumulated during online action.
It preserves harm facts while preventing runaway residue and rigidity.

## Inputs
- Replay buffer: (observations, actions, latents, trajectories)
- Residue traces: R values associated with contexts and latent regions
- Precision history: alpha_k values over time

## Outputs
- Updated world model parameters
- Updated residue field R (cleaned, contextualised, compressed)
- Updated precision gains alpha_k

## Invariants
- Genuine harm MUST NOT be erased
- Spurious or misattributed residue MAY be reduced
- Sleep operates on slower timescales than online action

## Failure if omitted
- Residue overgeneralisation
- Moral paralysis or burnout
- Brittle or frozen policy selection