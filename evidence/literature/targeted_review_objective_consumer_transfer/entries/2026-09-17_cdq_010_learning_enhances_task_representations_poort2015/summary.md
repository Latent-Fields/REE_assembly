# Learning reshapes V1 -- and entangles it (Poort et al., 2015)

## Why this entry is here

This is the deliberate **counterweight**. The other four entries all push toward 'route the task into the
encoder'. This one records what that costs.

## The finding

Learning a visual discrimination improves the discriminability of **task-relevant** stimuli in mouse V1. At the
same time, V1 acquires **non-sensory** signals -- choice, reward, locomotion.

## Both halves matter

- **Supports MECH-567**: task supervision reaching the encoder improves precisely the discriminations the
  consumer needs.
- **Prices MECH-567**: task-shaping *entangles* the code. REE's `z_world` is a **shared** latent -- SD-106's own
  note lists SD-015, ARC-030, MECH-117, the EXQ-085h..o cluster, MECH-457 and ARC-065 as consumers.

This is the biological reason MECH-567 is registered in the **DreamerV3 auxiliary-head** shape rather than the
**MuZero consumer-only** shape: the latter would make `z_world` single-consumer by construction, which REE
cannot afford.

## Honest limit

The paper does not test the reshaped code against an *untrained* downstream use, so the shared-latent cost is
a risk to instrument for, not a demonstrated penalty.
