# Dickinson & Balleine 1994 -- Motivational control of goal-directed action

**Claim under review:** MECH-295 -- liking-stream activation is a necessary intermediate between drive amplification (SD-012) and approach-cue selection.

**Tag:** (a) direct support for liking-required-for-drive-to-approach -- in pre-Berridge instrumental-conditioning vocabulary.

## What the paper did

Dickinson and Balleine consolidated a series of instrumental devaluation experiments into the canonical statement of incentive-learning theory. The paradigmatic experiment: rats are trained to lever-press for sucrose while hungry. Then the outcome is devalued (paired with lithium-induced illness, or specific-satiety induced) so that sucrose is no longer attractive. The question is whether the rats stop pressing the lever.

The answer turns on whether the rats have re-experienced the outcome in the new motivational state. Rats that consume devalued sucrose before the test (and thus experience its now-aversive hedonic impact) reduce lever-pressing. Rats that have not re-experienced the outcome continue pressing at high rates -- their action-selection has not updated despite knowing the outcome has been devalued. The drive-state / value-state shift does not directly rewire action selection. It has to propagate through experienced hedonic value of the outcome, and that experienced value then re-encodes onto the predictive cue / action.

## Why it matters for MECH-295

This is the foundational behavioural demonstration of the architectural principle MECH-295 commits to. Drive-state changes (or outcome value changes) do not produce changes in cue-driven or response-driven action selection on their own. They must route through the experienced hedonic value of the outcome -- the "liking-stream" in Berridge vocabulary. Only after that experience does the cue's incentive value update, and only then does approach behaviour follow drive.

The EXQ-483 failure mode -- override fires, drive amplified, approach_commit = 0.0 -- is the cue-side analogue of the Dickinson & Balleine finding. The drive is genuinely elevated, but the cue has not received liking-shaped incentive value, so drive cannot find a target. In their language: the agent has not done the incentive learning that connects drive state to cue value. In MECH-295's language: the liking-stream bridge is unwired.

This paper is the one I would cite first if asked to defend MECH-295's necessity claim from the behavioural-theory side. The Berridge work supplies the substrate; Dickinson & Balleine supply the principle.

## Limitations

The paradigm is instrumental devaluation rather than cue-driven approach under drive amplification. They are different experimental setups asking related questions: instrumental devaluation tests whether outcome-value updates propagate to action selection; MECH-295 in the EXQ-483 setting asks whether drive elevation propagates to cue-driven approach. Both tests rely on the same underlying mechanism (the routing-via-experienced-hedonic-value principle), but they are not identical paradigms.

The Dickinson & Balleine framework predates the Berridge wanting/liking decomposition, so their "incentive value, conditioned by experienced hedonic value" is the integrated motivational construct that Berridge later decomposes. The mapping to MECH-295 requires identifying their incentive-value-shaped-by-liking with the REE z_liking-shaped cue incentive code. That is a clean structural translation but it is a translation.

## Confidence reasoning

Source quality high (foundational, widely replicated, the behavioural anchor of incentive learning). Mapping fidelity high because the paper's paradigmatic finding is exactly the behavioural version of MECH-295's necessity claim. Transfer risk moderate (paradigm difference, vocabulary translation). Aggregate 0.80. Direction: supports.
