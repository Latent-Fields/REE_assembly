# Frith, Blakemore & Wolpert (2000) -- Abnormalities in the Awareness and Control of Action

## What the paper did

This is a theoretical review in Philosophical Transactions B that consolidates the Frith-Blakemore-Wolpert programme on motor awareness. It is not a single experiment but a synthesis of the authors' own empirical work -- the tickle-cancellation studies, imaging of cerebellar attenuation, and clinical observations of schizophrenia -- into a unified forward-model account. The paper's purpose is to specify what the comparator signal is, where it sits in the motor loop, and how its failure produces specific psychopathologies of agency.

## Key findings relevant to an SD-003 successor

Three architectural commitments matter here. First, the central claim that any motor command is accompanied by an efference copy, and that this copy is used by a forward model to predict the sensory consequences of the command before they arrive. Second, the claim that a comparator then flags the mismatch between predicted and actual sensory input. Third, the clinical mapping: in delusions of control the patient still makes the movement but loses the prediction, so the reafferent signal arrives uncancelled and feels externally caused. The subjective content of the delusion (an alien force moving my arm) is read off the neural signal that the comparator was meant to silence.

For the REE context, the architecturally important point is that this is a single-pass mechanism. The predictor runs once, the comparator runs once, and the signal used for agency attribution is the difference between the predicted and observed reafferent state. There is no counterfactual rollout, no second pass under an alternative action. This is the biology that the retired two-pass SD-003 design was always reaching for but could not implement once SD-010 made z_world architecturally independent of z_harm.

## Translation to ARC-033 and the SD-003 successor

ARC-033 specifies a forward model E2_harm_s on the sensory-discriminative harm stream. Under the retired SD-003 design, the attribution signal was causal_sig = E3(z_harm_s_actual) - E3(z_harm_s_cf), requiring two passes (actual and counterfactual action). The Frith 2000 architecture suggests a cleaner alternative: causal_sig = z_harm_s_pred - z_harm_s_obs, where z_harm_s_pred = E2_harm_s(z_harm_s_t, a_t). Action-caused harm (or harm-avoidance) is what the agent predicted. Environment-caused harm is what it did not predict. This matches the biology directly and removes the need for counterfactual action generation.

The clinical framing is also relevant. Frith 2000 treats the comparator as the computational substrate of agency: when it works, I know this action was mine; when it fails, the action is alien. For REE this means the same E2_harm_s residual does two jobs at once: it trains the forward model (prediction error) and it attributes agency (comparator signal). The dual role is economical and matches Wolpert-style internal model theory.

## Limitations and caveats

Frith 2000 frames the comparator on generic sensorimotor reafference -- proprioceptive, visual, tactile. E2_harm_s operates on a narrower channel (nociceptive proximity / harm_obs_s), which carries more affective load and has sparser statistics. The transfer is conceptually plausible but the paper does not directly show that a forward model / comparator architecture works for nociception. Relatedly, the paper is strongest on the architectural claim and weakest on timing details: it does not quantify how long after action completion the comparator produces its signal, which matters for whether REE can use the signal to gate residue accumulation in real time.

A more subtle issue is that Frith 2000 does not cleanly dissociate predictor failure from comparator failure. Both would abolish agency in similar ways. For REE, any diagnostic experiment that tests the SD-003 successor needs to distinguish 'E2_harm_s is not learning' from 'E2_harm_s is accurate but the downstream comparator is broken'. The literature does not supply this dissociation directly.

## Confidence reasoning

Source quality is high (PhilTransB, canonical review by the architects of the comparator model, widely cited as the reference statement of the theory). Mapping fidelity is moderate-high because the architecture transfers cleanly -- a forward model plus a residual comparator is exactly the template REE needs -- but the channel specificity (generic sensorimotor vs nociceptive harm) is not directly shown. Transfer risk is moderate-low because the forward-model motif is substrate-independent in computational terms. Overall confidence 0.72.

Based on review article retrieved via PubMed Central. DOI: https://doi.org/10.1098/rstb.2000.0734
