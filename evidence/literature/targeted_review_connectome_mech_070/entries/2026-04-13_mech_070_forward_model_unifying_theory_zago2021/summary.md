# Zago et al. (2021) -- The Forward Model: A Unifying Theory for the Role of the Cerebellum in Motor Control and Sense of Agency

## What the paper did

This review synthesises the evidence for the cerebellum as the neural substrate of forward internal models, extending the original Wolpert et al. framework to encompass not just motor control but also the sense of agency. The authors propose that the forward model operates by integrating an efference copy (a copy of outgoing motor commands from motor and premotor cortex) with actual sensory feedback, detecting mismatches as sensory prediction errors. These errors serve motor control adaptation, sensory attenuation, and the attribution of self-generated vs. externally generated events.

## Key findings relevant to MECH-070

The paper is unambiguous about timescale: the cerebellum computes predictions of the immediate next state of the body, specifically to compensate for sensory feedback delays that would otherwise destabilise rapid movements (visual feedback delays of 30-80 ms; reaching movement times of a few hundred milliseconds). The language throughout is of online, moment-to-moment correction -- there is no description of the cerebellum performing multi-step lookahead or extended rollout. Longer-timescale processing -- contextual knowledge, belief reasoning, explicit agency judgments -- is assigned to prefrontal cortex. The functional dissociation the paper documents is therefore: cerebellum = short-horizon, implicit, sensorimotor; prefrontal cortex = longer-horizon, explicit, contextual. This is the reverse of what MECH-070 originally claimed for E2 vs. E1.

## How findings translate to REE

The MECH-070 claim as originally stated held that E2 has a longer planning horizon than E1. The neurological grounding was the rollout_horizon design parameter (E2=30, E1=20). Zago et al. argue the biological forward model is precisely bounded to short timescales -- the cerebellum predicts one step ahead in continuous motor time to bridge the feedback delay. The cortical (E1) analogue is the longer-horizon processor. This matters for REE: if E2's function is most naturally 1-step forward prediction and E1's function is slower, longer-horizon world modelling (LSTM with prediction_horizon=20), then the correct direction of the horizon comparison is E1 > E2, not E1 < E2. The experimental evidence (EXQ-132, EXQ-212) showing E2 degrades faster across extended horizons is consistent with this biological picture -- a cerebellar-style model doing what it was designed for (1-step) but breaking down when asked to do what cortex does (20-30 steps).

## Limitations

This review extends the forward model framework specifically to agency, so some of the cortical contribution it describes is specifically about self-attribution rather than planning. The prefrontal cortex in this account is involved in belief-based agency reasoning, not necessarily in longer rollout planning in the REE sense. Additionally, the cerebro-cerebellar loop literature (not reviewed here) suggests that extended cerebellar loops through parietal and prefrontal cortex may produce effective longer prediction horizons when the chain is considered as a system -- so the short-horizon claim may be specific to the cerebellar module in isolation.

## Confidence reasoning

Confidence is 0.68 weakening. The paper is a solid but not foundational review, and its extension to agency introduces some ambiguity in the cortical-longer-horizon claim. The direction of evidence is clearly against MECH-070's original framing: the cerebellar analogue (E2) is described as the short-horizon system. This aligns with the experimental failures already documented in the evidence_quality_note of MECH-070 itself, making the literature convergent with internal experimental evidence.
