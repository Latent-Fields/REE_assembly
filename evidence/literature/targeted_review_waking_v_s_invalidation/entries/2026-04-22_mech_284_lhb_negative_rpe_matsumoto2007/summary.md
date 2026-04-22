# Matsumoto & Hikosaka 2007 -- Lateral Habenula as a Source of Negative Reward Signals in Dopamine Neurons

According to PubMed ([DOI](https://doi.org/10.1038/nature05860)).

## What the paper does

Matsumoto and Hikosaka recorded simultaneously from lateral habenula and midbrain dopamine neurons in macaques performing a saccade task with positionally biased reward. Three findings carry the architectural weight. First, LHb neurons inverted the dopamine sign: excited by no-reward-predicting targets, inhibited by reward-predicting ones. Second, the LHb response *preceded* the DA inhibition on unrewarded trials by tens of milliseconds, ruling out the alternative that LHb merely mirrors DA. Third, weak electrical micro-stimulation of LHb produced strong, time-locked inhibition of dopamine neurons, establishing causal direction. Taken together, this is the substrate paper for the claim that the brain has a dedicated nucleus broadcasting "the prediction failed" upstream of the dopamine dip.

## Why it matters for V_s invalidation

For our architecture, this is the strongest candidate substrate for the broadcast trigger event in MECH-284. The dopamine dip from Schultz1997 is the broadcast itself; LHb provides the upstream computation that selects when to fire. That matters because if MECH-284 needs an accumulator that integrates trigger events into a per-schema staleness signal, we need to know that the trigger biology is more than just "DA dipped because reward did not arrive at this exact moment" -- we need a circuit that can flag "the prediction failed in a way that ought to invalidate the underlying expectation". LHb is that circuit. The selectivity of its response to no-reward cues, not just to reward omission, is exactly the abstraction step required.

The mapping limitation is honest. LHb in this paper computes a value-PE, not a model-fit-PE. The leap to V_s is that V_s is concerned with whether a hippocampal anchor still describes the regional dynamics adequately, which is closer to a model-fit construct than a value construct. Bromberg-Martin & Hikosaka 2011 (the next paper in this pull) extends LHb to information-prediction-errors, which closes some of the gap. But the field has not, as of 2024 to my knowledge, recorded LHb during a task that cleanly dissociates "the model is wrong" from "reward is worse than expected". That dissociation is what V3 would need to claim LHb specifically as the MECH-284 trigger substrate rather than DA dip generally.

## Clinical resonance

The clinical reading goes both ways and is informative for our failure-mode analysis. LHb *hyperactivity* maps to depression and learned helplessness: the broadcast trigger fires too easily, every schema is invalidated, the agent withdraws into action-paralysis. LHb *hypoactivity* maps to inflexibility and perseveration: the trigger underfires, stale schemas are not invalidated, the agent perseverates on dead routines. The V3-EXQ-475 freeze re-commit phenotype maps closer to the second pattern -- single events register (so the trigger has *some* function) but the integral never accumulates (so either the trigger is too weak or the accumulator gain is too low). LHb biology cannot distinguish those two without a separate measurement of the post-LHb integration; that is the gap MECH-284 fills.

## Confidence reasoning

Source quality is high (Nature, primate single-unit + causal stimulation, well replicated). Mapping fidelity is the limiting factor (0.65) because the construct is reward-PE not schema-fit-PE. Transfer risk is low (0.30) because LHb circuitry is conserved and the clinical mapping is independently supported. Aggregate 0.72.
