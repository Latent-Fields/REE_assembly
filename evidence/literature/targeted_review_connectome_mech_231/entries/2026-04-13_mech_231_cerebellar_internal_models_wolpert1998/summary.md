# Wolpert, Miall, Kawato (1998) -- Internal models in the cerebellum

## What the paper did

This is the foundational theoretical review establishing the paired forward/inverse internal model framework for cerebellar computation. Wolpert, Miall, and Kawato proposed that the cerebellum houses forward internal models -- predicting the sensory consequences of motor commands -- and inverse internal models -- computing the motor command needed to achieve a desired state. The forward model receives an efference copy, a copy of the outgoing motor command, and predicts the upcoming sensory state before feedback arrives, thereby bridging the delay between command and consequence. The paper proposed a modular MOSAIC architecture in which multiple paired models compete to control different movement contexts.

## Why this supports MECH-231

The key contribution for MECH-231 is precisely what made this paper uncomfortable for MECH-070: the cerebellar forward model is characterised as a one-step delay-compensation device, not a multi-step planner. Its functional role is to bridge a single feedback delay interval -- tens to hundreds of milliseconds in biological systems -- and then hand back to the sensory system. The paper assigns no multi-step rollout function to the cerebellum; that role belongs implicitly to higher cortical structures involved in planning. MECH-231 claims that E2 operates as a short-horizon efference-copy forward model whose prediction accuracy degrades faster than E1's across multi-step horizons. Wolpert et al. provide the biological grounding for exactly this: if E2 is the cerebellar analogue, it should be a 1-step transition predictor, and E1 (the cortical slow predictor, LSTM) should be the longer-horizon system. The experimental findings in EXQ-132 and EXQ-212, which showed E2 degrades faster across multi-step horizons, are what you would expect from a 1-step device asked to extrapolate beyond its native operating range.

## What the MECH-070 entry said and how the framing changes

The earlier entry for MECH-070 assigned this paper an evidence_direction of weakens, because MECH-070 claimed E2 had a longer planning horizon than E1 -- the inverse of what Wolpert et al. describe. The paper itself has not changed. What changed is the claim direction. MECH-231 is the corrected reformulation: E2 is the short-horizon system. With that correction, the paper no longer contradicts the claim; it supports it. The biological archetype and the corrected REE claim are now aligned.

## Limitations

The paper is theoretical -- it proposes the framework but does not measure rollout degradation in a way that maps directly to REE's multi-step prediction error curves. The biological short-horizon is about delay compensation in continuous motor control; REE's rollout_horizon governs discrete-step prediction in a grid world, which is a different computational problem. The MOSAIC extension of the framework allows chaining of paired models, potentially yielding longer effective horizons through composition -- though each individual model in that account remains a 1-step predictor. The mapping from cerebellar biological timescales to REE's discrete step count is architecturally motivated rather than experimentally demonstrated in the REE substrate.

## Confidence reasoning

Confidence is set at 0.74, slightly higher than the 0.72 assigned in the MECH-070 weakening entry. The source quality is essentially unchanged -- this is the canonical foundational paper by the field's primary architects. Mapping fidelity is slightly improved because the direction now aligns: the paper characterises a 1-step predictor, MECH-231 claims a 1-step predictor. The main residual uncertainty is the transfer from continuous biological motor control to discrete grid-world steps, which remains indirect. The claim does not rest solely on this theoretical alignment -- the experimental evidence from EXQ-132 and EXQ-212 is the direct substrate-level test -- but this paper provides the strongest neurobiological rationale for why MECH-231's corrected direction is right.
