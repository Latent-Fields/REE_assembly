# Walker & van der Helm 2009 -- Overnight Therapy? REM Sleep and Emotional Memory

**Claim tested: MECH-123**
**Evidence direction: supports**

## What the paper claims

REM sleep provides a neurochemical state uniquely suited to emotional memory recalibration. During REM: low noradrenaline and serotonin (aminergic withdrawal), elevated acetylcholine, and hippocampal theta activity combine to allow reactivation of emotional memories with simultaneous depotentiation of their affective charge. The SFSR (Sleep to Forget and Sleep to Remember) hypothesis: REM retains the informational content of emotional experience but reduces autonomic reactivity and the emotional 'sting'. REM disruption (PTSD, sleep apnoea) produces persistent heightened emotional reactivity -- the failure mode predicted by SFSR.

## Mapping to MECH-123

MECH-123 claims REM resets precision priors (commitment_threshold, precision_ema_alpha) after content consolidation, and must be last in sequence because recalibrating before replay corrupts evidence weighting.

The SFSR mechanism is the biological implementation of this claim. In REE terms:
- 'Precision prior' = the weighting applied to harm-signalling and commitment-threshold parameters
- These parameters encode how strongly recent high-valence (high-salience, high-harm) experiences influence action selection
- SFSR: REM reduces the affective charge of recently consolidated emotional memories -- in REE terms, it reduces the precision weighting on harm-associated z_world content without erasing the informational content
- The result is a recalibrated commitment_threshold: the threshold for committing to actions in situations that resembled recent harm events is renormalised

The ordering constraint is supported by SFSR logic: precision recalibration operates on consolidated memory. You cannot depotentiate the affective charge of a memory that has not yet been encoded stably. Therefore NREM consolidation (MECH-121) must precede REM recalibration (MECH-123). Running REM before NREM would attempt to recalibrate the affective weighting of memories that are still in hippocampal temporary storage -- this would corrupt the evidence weighting of newly consolidated schema.

## Failure mode evidence

The PTSD connection is the strongest empirical argument for MECH-123: PTSD involves disrupted REM sleep AND persistent heightened reactivity to harm-associated stimuli -- exactly the failure mode MECH-123 predicts. The affective charge of traumatic memories is not depotentiated, leading to hyperactivation of harm-signalling and lowered action commitment thresholds in harm-associated contexts. This is strong convergent evidence for the precision recalibration function of REM.

## What the paper does not say

The SFSR hypothesis covers affective / emotional precision. MECH-123's scope is broader: it includes recalibration of commitment_threshold and precision_ema_alpha as general precision parameters, not only for emotionally valenced content. Walker-van der Helm do not make the 'REM must be last' ordering argument explicitly. The paper treats REM as performing this function without deriving why it must follow NREM.

## Evidence quality note

High quality (Psychological Bulletin, comprehensive review). The PTSD/REM disruption evidence is particularly strong. The SFSR mechanism (low noradrenaline enabling affective depotentiation) is well-supported by pharmacological studies (noradrenaline blockers during sleep affect emotional memory consolidation in predictable ways).
