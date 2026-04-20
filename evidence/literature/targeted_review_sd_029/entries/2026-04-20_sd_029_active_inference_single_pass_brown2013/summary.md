# Brown, Adams, Parees, Edwards, Friston (2013): Active inference, sensory attenuation and illusions

*Cognitive Processing* 14(4), 411-427. DOI: 10.1007/s10339-013-0571-3

## What the paper did

Brown and colleagues derived sensory attenuation and agency attribution from active-inference / free-energy-minimisation principles. Rather than treating attenuation as a separate cancellation operation performed by a dedicated comparator, they argued it is the Bayesian-optimal consequence of precision modulation within a single hierarchical generative model. The paper reviews the force-matching illusion (Shergill 2003) and delusions-of-control in schizophrenia as test cases for the framework.

## Key theoretical claims

Two directly relevant to SD-029. First, the active-inference formulation does not require an explicit counterfactual branch. Attenuation emerges because, during self-generated action, the brain attenuates the precision of ascending sensory prediction errors so that descending motor predictions can dominate and drive behaviour. The comparator operates continuously within one forward pass, not between a factual and a counterfactual rollout. Second, failures of this mechanism (as in schizophrenia) are precision failures rather than residual-computation failures: the prediction error is computed but is not properly down-weighted, so self-generated stimuli are experienced as externally caused. The paper explicitly contrasts this with comparator models that posit a separate counterfactual pathway.

The key quotation on the comparator reference: "The only way that the underlying cause of the sensations can be resolved is by reference to proprioceptive input -- that is only generated internally." The reference is the internally generated prediction itself, not a branched alternative.

## Mapping to SD-029

This paper is the theoretical-mechanism grounding for SD-029's architectural choice. SD-003 proposed a counterfactual (cf_gap) design: compute `E2(., a_actual)` and `E2(., a_cf)` and compare them to detect agent causation. SD-029 replaces this with a single forward pass conditioned on the actual action and treats the residual as the agency signal. Brown 2013 is the formal argument that this is not a pragmatic simplification -- it is the biologically and Bayesian-optimal architecture. The counterfactual branch is redundant because precision modulation already disambiguates self-caused from externally-caused reafference within one pass.

The paper also suggests what may be missing from the current V3 SD-029 implementation. V3-EXQ-433a C2 FAILED to find attenuation. If the implementation computes `z_harm_s_observed - E2_harm_s(z_harm_s_{t-1}, a_actual)` as a raw residual without any precision-weighting mechanism during approach-to-harm events, the architecture Brown 2013 formalises is incomplete. In active inference, attenuation requires both (i) the forward prediction and (ii) precision modulation that attenuates the ascending prediction-error pathway during self-generated action. A V3 implementation that has (i) but lacks (ii) would be expected to underperform on C2.

## Caveats

This is a theoretical / computational paper, not an empirical study. Its predictions are tested indirectly via fits to force-matching-illusion data and schizophrenia psychophysics elsewhere in the literature, not by direct quantitative fit in this paper itself. The mapping onto the REE architecture is strong because both are computational systems built around prediction-error minimisation, but the paper does not provide a ready-made implementation recipe. Also, the paper works primarily in the sensorimotor / tactile domain -- nociceptive-stream extension is not addressed directly. Read Brown 2013 for the theoretical warrant of the single-pass design, not for the nociceptive transfer (which rests on Lalouni 2020 and 2025).

## Confidence reasoning

Source quality is moderate: peer-reviewed but theoretical. The authors include Friston, who is the principal proponent of the active-inference framework, giving the argument canonical status. Mapping fidelity is high -- the formal structure of "single-pass precision-weighted prediction error as agency signal" maps almost directly onto SD-029's functional restatement. Transfer risk is low because the argument is framework-level, not tied to a specific species or task. Aggregate 0.68, capped below the empirical papers because theory-without-direct-experiment can always turn out to be wrong on the specifics. This paper is the architectural-theory anchor for why SD-029 should work; it does not by itself tell us it does work on V3 harm events.
