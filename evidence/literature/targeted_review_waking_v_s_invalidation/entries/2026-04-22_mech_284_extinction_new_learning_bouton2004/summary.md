# Bouton 2004 -- Context and Behavioral Processes in Extinction

According to PubMed ([DOI](https://doi.org/10.1101/lm.78804)).

## What the paper does

Bouton synthesises the behavioural literature on Pavlovian extinction and makes the now-canonical case that extinction does not destroy the original learning. Instead, extinction generates new, context-dependent learning that competes with the original. The empirical foundation is a constellation of phenomena that together rule out the erasure account: renewal (return of the extinguished response when the context shifts back to the original training context), spontaneous recovery (return of the response after a delay), reinstatement (return after re-exposure to the unconditioned stimulus), and rapid reacquisition (faster relearning of the original contingency than initial acquisition). All of these require the original learning to be preserved somewhere, with the extinction learning operating as an additional context-gated trace. The paper closes by examining four candidate mechanisms for extinction -- discrimination of a new reinforcement rate, generalisation decrement, response inhibition, and violation of a reinforcer expectation -- and finds the data most consistent with generalisation decrement and expectation violation operating jointly.

## Why it matters for V_s invalidation

This paper is the empirical anchor for the dual-trace property that V_s invalidation must respect. MECH-269 anchor reset should not erase the previously operative anchor; it should mark it as no longer operative *in the current context*, while preserving its retrievability when contextual cues re-favour it. The behavioural evidence Bouton synthesises -- particularly renewal -- rules out any architecture in which V_s drop equals trace erasure. Both anchors must coexist; routing between them is what the operative-anchor decision is.

This matters for MECH-272 (state-gated routing). The behavioural data say that the routing decision is context-gated, and that the original anchor's retrievability persists indefinitely under appropriate context cues. Architecturally this means MECH-272 should be a routing layer over a *set* of candidate anchors with persistent V_s values, not a winner-take-all operation that destroys non-winners. The Gershman2010 latent-cause framework formalises this: the posterior over latent causes is always over multiple causes, and routing is selection of which posterior to make operative.

## Implications for V3-EXQ-475

The freeze re-commit phenotype takes on a new shape under the dual-trace framing. The agent's hippocampal proposer is drawing trajectories from the original avoid-anchor not because the new safety information is failing to *invalidate* the avoid-anchor, but because the routing layer is failing to *switch operative anchors*. The avoid-anchor is still there (correctly preserved by the dual-trace property) but the new safety-anchor is not being elevated to operative status. This is a MECH-272 routing failure as much as a MECH-284 accumulation failure. The architectural fix may need to address both.

## Clinical resonance

The dual-trace property is the formal foundation for exposure-based therapies in PTSD, phobia, and OCD. Extinction does not erase the fear; it generates a competing safety memory whose retrieval is context-gated. Treatment failure often reflects routing-layer failure: the safety memory exists but contextual cues at home keep re-favouring the original threat memory. This is the V_s-architecture analogue of the routing problem MECH-272 needs to solve well -- and a candidate explanation for why exposure therapy gains do not always generalise.

## Confidence reasoning

Source quality high (Learn Mem, foundational review, very high citations). Mapping fidelity moderate (0.62) because the paper is behavioural-phenomenology not neural-substrate. Transfer risk low (0.30). Aggregate 0.65.
