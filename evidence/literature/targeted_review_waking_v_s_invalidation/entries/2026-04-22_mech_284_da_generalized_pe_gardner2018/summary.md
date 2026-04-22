# Gardner, Schoenbaum & Gershman 2018 -- Rethinking Dopamine as Generalized Prediction Error

According to PubMed ([DOI](https://doi.org/10.1098/rspb.2018.1645)).

## What the paper does

Gardner, Schoenbaum, and Gershman propose that midbrain dopamine encodes a *generalized* prediction error -- not just reward PE in the Schultz1997 sense, but PE about sensory features as well. The empirical anchors are two phenomena that the canonical reward-PE framework cannot accommodate. Sensory preconditioning: pair stimulus A with stimulus B, then pair B with reward, then test responses to A. Animals respond to A even though A was never paired with reward, indicating the brain learned an A-B sensory association during the preconditioning phase. Identity unblocking: change the identity of an expected reward (same value, different flavour) and dopamine responds, despite no reward-PE. Both findings require dopamine to carry information about violated sensory expectations, not just violated reward expectations. The authors weave these into a hybrid RL framework that lies between pure model-based and pure model-free.

## Why it matters for V_s invalidation

This paper carries more architectural weight for the broadcast trigger role than Schultz1997 because it removes the constraint that the trigger must be reward-shaped. V_s is concerned with whether the currently anchored schema is still the right schema for the regional dynamics. Many of the violations that should drop V_s have nothing to do with reward -- they are violations of sensory predictions, transition predictions, identity predictions. A reward-PE-only trigger would miss these. A generalized-PE trigger captures them naturally.

The clean architectural reading is now: OFC (Wilson2014) maintains the local schema label; DA (Gardner2018) carries the broadcast generalized-PE; the OFC labelling integrates DA signals to update its representation; MECH-284's accumulator output is OFC representational drift; MECH-269's anchor reset fires when the OFC labelling crosses a discrete boundary. This two-substrate architecture is the most parsimonious account I can construct from the literature in this pull.

LHb still has a role -- it is upstream of the dopamine dip specifically -- but once we accept generalized PE, LHb is a special case (the value-PE component) of a broader DA broadcast that does not exclusively pass through LHb. The architectural commitment matters: if MECH-284's trigger is LHb-only, sensory-PE invalidation must work through some other circuit; if it is generalized DA, LHb is one input among several and the architecture is simpler.

## What the paper does not do

It does not address aggregation. The generalized-PE framing is still single-event and scalar. How single PEs aggregate into a sustained schema downweight -- the MECH-284 accumulator step proper -- is not in this paper. Sensory preconditioning and identity unblocking are single-trial phenomena. The integration timescale of the accumulator is the architectural commitment the literature has not yet made explicit.

## Clinical resonance

If DA encodes generalized PE, then DA-related disorders should produce mixed deficits across reward learning and schema updating. Schizophrenia displays exactly this pattern -- aberrant salience attribution affects both reward (delusional reward attribution) and sensory schema (hallucinated content as failure of sensory schema invalidation). The Gardner framework predicts that pure dissociations -- reward learning preserved with schema updating broken, or vice versa -- should be rare. That is a useful constraint on what failure modes a V_s account needs to explain.

## Confidence reasoning

Source quality high. Mapping fidelity 0.78 -- the highest in the trigger-side cluster because generalized PE is exactly what V_s needs from a broadcast signal. Transfer risk low (0.30). Aggregate 0.75.
