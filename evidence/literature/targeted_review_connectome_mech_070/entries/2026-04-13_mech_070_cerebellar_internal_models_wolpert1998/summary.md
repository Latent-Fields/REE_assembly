# Wolpert, Miall, Kawato (1998) -- Internal models in the cerebellum

## What the paper did

This is the foundational theoretical review establishing the paired forward/inverse internal model framework for cerebellar computation. Wolpert, Miall, and Kawato proposed that the cerebellum houses forward internal models (predicting the sensory consequences of motor commands) and inverse internal models (computing the motor command needed to achieve a desired state). The forward model receives an efference copy -- a copy of the outgoing motor command -- and predicts the upcoming sensory state before feedback arrives. The paper proposed a modular MOSAIC architecture in which multiple paired models compete to control different movement contexts.

## Key findings relevant to MECH-070

The forward model's functional role is precisely characterised: it compensates for sensory feedback delays that range from roughly 10 ms (small fast animals) to 100 ms or more (larger animals and complex visual feedback paths). Visual feedback delays for reaching movements are comparable to the movement time itself -- a few hundred milliseconds. The cerebellar forward model therefore operates on a prediction horizon bounded by the delay it is trying to compensate: it predicts the next state, not a sequence of states. This is not incidental -- the entire rationale for a forward model in this account is that it bridges one delay interval, then hands back to the sensory system. The paper does not describe multi-step rollout as a cerebellar function; that role is implicitly assigned to higher cortical structures involved in planning.

## How findings translate to REE

MECH-070 claims that E2 (the cerebellar analogue in REE, operating in the z_self/motor domain via efference copy) has a planning horizon that exceeds E1 (the cortical analogue). Wolpert et al. directly contradict this: the biological forward model they describe is a one-step delay-compensation device, not a long-horizon planner. If REE's E2 is correctly mapped to the cerebellar forward model, its natural operation is 1-step prediction. The rollout_horizon parameter in the original V3 implementation (E2=30, E1=20) represented a design choice -- possibly an incorrect one -- rather than a biologically grounded constraint. The experimental failures (EXQ-132, EXQ-212 showing E2 degrades faster across horizons than E1) are coherent with this: you would expect a one-step device to degrade gracefully over 1 step but deteriorate rapidly when asked to roll out 20-30 steps.

## Limitations

The paper is theoretical -- it proposes the framework but does not directly measure planning horizon in a way that maps to REE's rollout_horizon parameter. The biological short-horizon is about delay compensation in continuous motor control; REE's rollout_horizon governs discrete-step planning in a grid world, which is a different computational problem. The mapping is architecturally motivated, not experimentally proven. Additionally, Wolpert et al.'s framework has been extended since 1998, with some later work (e.g., cerebro-cerebellar loops in cognitive domains) suggesting broader cerebellar roles that may involve longer effective horizons when chained through cortical loops.

## Confidence reasoning

This is a 0.72 confidence weakening of MECH-070. The source itself is impeccable -- the foundational paper in the field by its primary architects. The weakening direction is clear: the cerebellar forward model is characterised as short-horizon, one-step, delay-compensating. The confidence is not higher because the mapping from biological cerebellar timescales to REE's discrete rollout_horizon is indirect, and because the evidence_quality_note in MECH-070 has already partially acknowledged the problem (E2 training horizon is separate from rollout_horizon). This paper does not, however, rescue the original claim -- it firmly places the cerebellar analogue as the shorter-horizon system relative to cortex.
