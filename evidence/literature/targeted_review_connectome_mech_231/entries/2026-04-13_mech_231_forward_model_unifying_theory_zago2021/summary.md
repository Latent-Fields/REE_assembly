# Zago, McIntyre, Senot, Lacquaniti (2021) -- The Forward Model: A Unifying Theory for the Role of the Cerebellum in Motor Control and Sense of Agency

## What the paper did

This 2021 review extends the Wolpert et al. framework to address the sense of agency -- the subjective feeling of being the cause of one's own actions. Zago and colleagues propose a unified account in which the cerebellar forward model generates predictions that are compared against sensory feedback to compute prediction errors. When efference copy accurately predicts the outcome, the action is registered as self-generated; when the prediction fails, agency is attributed elsewhere. The review distinguishes two levels of processing: the cerebellum handles rapid, implicit, sensorimotor-level predictions, while prefrontal cortex contributes to longer-timescale, explicit, belief-based judgments about agency. This division of labour is central to the paper's theoretical contribution.

## Why this supports MECH-231

Zago et al. provide an explicit anatomical and computational argument for the E2 < E1 horizon ordering that MECH-231 asserts. The cerebellum, operating on efference copy at the sensorimotor level, is characterised as the short-horizon immediate-prediction system. Prefrontal cortex -- the biological analogue closer in function to E1's slow world-model role -- handles the longer-timescale contextual reasoning. If E2 maps to the cerebellar forward model and E1 maps to cortical slow prediction, then MECH-231's claim that E2's prediction accuracy degrades faster across multi-step horizons follows directly. The paper does not frame this as a problem to be corrected; it frames it as a functional specialisation. Short-horizon prediction is what the cerebellum is for. MECH-231 accepts this characterisation and builds on it.

## The contrast with the MECH-070 entry

The MECH-070 entry assigned this paper evidence_direction: weakens because MECH-070 claimed E2 had a longer planning horizon than E1. The biological evidence runs the other way, and this paper was one of three that collectively made MECH-070 untenable. MECH-231 is the corrected claim -- E2 is the short-horizon system -- and the same biological evidence that undermined MECH-070 now supports MECH-231 directly. The paper has not changed; the claim has been corrected to match what the evidence always said.

## Limitations

The prefrontal contribution in Zago et al. is specifically to the sense of agency and conscious judgment, not to world-model planning per se. This adds a layer of cognitive processing not directly present in REE's E1, which is a predictive LSTM operating on sensory streams rather than a model of intentional agency attribution. The timescale distinction the paper makes is qualitative and biological; it does not generate a quantitative prediction about how many discrete steps a cerebellar-analogue model should be able to roll out before degrading. The review also does not directly compare degradation rates across multi-step horizons -- it makes claims about division of labour, not about the shape of the error-vs-horizon curve that MECH-231 predicts experimentally.

## Confidence reasoning

Confidence is set at 0.69, essentially matching the 0.68 from the MECH-070 entry. The source quality is good -- a well-cited review in Frontiers in Systems Neuroscience from researchers with strong cerebellar experimental backgrounds. Mapping fidelity is moderate and unchanged: the biological timescale distinction is real, but the prefrontal contribution in the paper is to agency attribution rather than planning in the REE sense, creating some misalignment at the edges. Transfer risk is also unchanged. The paper's contribution to MECH-231 is supporting the direction -- confirming that the biological analogue divides labour exactly as MECH-231 claims -- rather than providing quantitative evidence about the degradation gradient specifically.
