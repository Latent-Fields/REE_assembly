# Literature Summary: 2026-02-14_mech058_byol_ema_target_predictor_separation

## Claims Tested

- `MECH-058`

## Source

- Grill JB, Strub F, Tallec C, et al. (2020), *Bootstrap your own latent: A new approach to self-supervised Learning*.
- URL: `https://doi.org/10.48550/arXiv.2006.07733`

## Mapping to REE

- BYOL trains an online predictor against a momentum-updated target network.
- This strongly supports `MECH-058` because it is a concrete demonstration that slow target-anchor dynamics and fast predictor adaptation can stabilize substrate learning.

## Caveats and Mapping Limits

- BYOL is image-centric and does not include explicit commitment routing or social/ethical control channels.
- The paper does not specify pre-commit versus post-commit error attribution flows.
- Stability results are empirical and architecture-specific; transfer to REE lane coupling requires adapter validation.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.78`
- Rationale: direct mechanistic match on EMA target-anchor plus fast predictor separation, with moderate scope gap beyond representation learning.
