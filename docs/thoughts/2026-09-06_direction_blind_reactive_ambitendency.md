Status: processed
Intake: evidence/planning/thought_intake_2026-09-06_direction_blind_reactive_ambitendency.md
Claims registered: MECH-535, MECH-536

# Direction-blind reactive ambitendency: is the V3-EXQ-978 fishtank oscillation catatonic ambitendency, and what does it say about the basal-ganglia contract?

**Date:** 2026-09-06
**Origin:** user thought during a fishtank read of V3-EXQ-978 (session exq978-fishtank, 2026-09-04/06), captured verbatim below and worked in conversation.
**Primary evidence:** V3-EXQ-978 episode-log companion (seed 42, 6 OFF-arm + 6 ON-arm frozen-policy rollouts; observational pass, not the scored DV). Manifest `evidence/experiments/v3_exq_978_sd018_directional_field_fishtank_20260903T111718Z_v3.json`; autopsy `evidence/planning/failure_autopsy_V3-EXQ-978_2026-09-03.md`; GFLAG-0131.

## The thought, verbatim

> the latest fishtank 978 has a few different behaviour types. there is the dithering in the first three, settling in 4, actual action in 5 then the last few episodes to have actual clear goal achievement within a weirdly oscillating path

> looking at the behaviours I would wonder if the ambitendency seen has anything to do with the catatonic ambitendency which in my mind shows there is something malfunctioning which may include contracts with basal ganglia systems

## What the log actually shows (checked per step)

- The 12 logged episodes are not one agent developing. Episodes 1-6 are six independent rollouts of the frozen OFF-arm policy; 7-12 replay the same six start layouts under the frozen ON-arm policy. Nothing learns between episodes.
- 10 of 12 episodes end in a two-cell limit cycle. The resource field at the agent's cell alternates high/low across the pair, so each cycle is one step toward food and one step away: ambitendency in the strict Kahlbaum / Bush-Francis sense (a goal movement started, retracted, restarted), not undirected dithering.
- 2 of 12 episodes are a boundary-press fixed point: the same action every step against the wall, 198/200 steps stationary. One of them sits on the same corner cell as the V3-EXQ-471 catatonic lock.
- The cycle is lethal by its own repetition: the causal-footprint contamination rule (+0.5 per visit, cell retyped at 2.0, 0.4 health per contaminated step) kills the agent at step 11-23 in a hazard-free env. The fixed point survives 200 steps eating nothing.
- The ON arm runs longer straight lines (up to 7 cells) before locking into the cycle; the one consumption inside a cycling episode is incidental to a straight run, not steered (the directional head's argmax is constant at cell 6 on every ON step).

## The reading

The sign matches catatonic ambitendency, and the co-occurrence of stupor and ambitendency from one frozen policy under different initial conditions matches the syndrome structure (one deficit, two attractors: fixed point and 2-cycle). But the mechanism is neither of REE's two registered catatonia routes.

- MECH-202B: commit gate frozen at maximum threshold. Not here: there is no gate in the loop.
- SD-036 subtype II: harm-stream lock upstream of an intact gate. Not here: no harm stream in the loop, hazard-free rung.
- Here: the eval reader is a bare argmax head on z_world, memoryless, re-deciding every step. z_world carries how close food is (the scalar proximity head trained, r2 ~0.71) but not which way (the directional head did not carry into the latent). A reactive policy conditioned on magnitude learns "at low proximity do X, at high proximity do Y"; on an adjacent pair of cells that is back-and-forth. Ambitendency = intact actor + direction-blind state + no persistence. A representational route, not a gating one.

## The basal-ganglia contract

Any persistence of two or more steps on the chosen action escapes a two-cycle, so a BG-like post-commit latch (ARC-107 root C; MECH-047 / MECH-266 hysteresis) would abolish the ambitendency immediately. It would not restore foraging: with a direction-blind latent a latched agent runs straight lines into walls, which is what the ON arm's transients already look like. Prediction: the latch converts ambitendency into perseveration without competence. That dissociates a gating deficit from a representational one (clinical echo: lorazepam restores movement without treating what lies underneath; analogy only, not evidence).

The local_view_greedy anchor forages 45.75 resources per episode with no latch at all, so commitment is not necessary given a good representation. What it buys is robustness to a degraded one. That is a defensible statement of the striatal contract, and the answer to the question above: the 978 reader has no BG contract to malfunction; what it shows is what an actor looks like without one.

## Do not harden until

- The latch prediction is actually run (eval-time action-persistence wrapper on the same OFF-arm policy; resources/episode must NOT rise while the cycle disappears). Cheap; routing is a /governance call.
- Literature check on ambitendency mechanism accounts (Northoff top-down OFC/mPFC-motor model; GABA-A / NMDA-R routes) to see whether a representational (goal-in-valence-not-direction) route has been proposed clinically. Not yet pulled.
