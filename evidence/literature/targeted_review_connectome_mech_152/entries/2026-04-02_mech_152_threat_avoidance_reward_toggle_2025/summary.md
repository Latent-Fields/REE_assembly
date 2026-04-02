# Klumpers & Roelofs (2025) — Intersect Between Threat, Active Avoidance, and Reward

## What the paper does

Klumpers and Roelofs review how brain mechanisms for conditioned threat (fear), active avoidance, and reward approach intersect and interact. They propose a neural toggle-switch model: the brain transitions between fear/avoidance and approach/reward states based on cost-reward evaluation in vmPFC/OFC. The amygdala drives threat responses, the nucleus accumbens drives approach motivation, and vmPFC/OFC serves as the arbiter that determines the balance based on contextual evaluation.

## Relevance to MECH-152

MECH-152 claims that cue-indexed context from E1 projects to a terrain_weight signal [w_harm, w_goal] that scales E3's harm and goal scoring. This is architecturally analogous to the toggle switch: contextual evaluation (E1 ContextMemory) determines whether the system emphasizes harm avoidance (high w_harm) or goal approach (high w_goal).

The paper's finding that vmPFC/OFC integrates cost-reward information to control the threat-approach balance maps directly onto MECH-152's design. In hazard-gradient contexts, w_harm should dominate; in resource-proximate contexts, w_goal should dominate. This is exactly what EXQ-194 tested (C1 PASS for harm pathway, C2 FAIL for goal pathway).

## Categorical vs continuous

The toggle-switch framing implies discrete states (threat mode vs approach mode), while MECH-152 proposes continuous modulation. The biological evidence actually supports both: the amygdala-NAcc competition is continuous at the neural level but can produce categorical behavioral outcomes (freeze vs approach). MECH-152's continuous terrain_weight may be the more faithful representation of the underlying neural dynamics, with categorical behavior emerging from downstream thresholding.

## Confidence reasoning

Good source quality. The threat-reward balance principle directly supports MECH-152. Confidence moderated by the Pavlovian conditioning context vs REE's spatial navigation context.
