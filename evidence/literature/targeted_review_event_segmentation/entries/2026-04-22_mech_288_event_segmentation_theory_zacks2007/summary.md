# Zacks et al. 2007 -- Event perception: a mind-brain perspective

According to PubMed, this is the canonical statement of Event Segmentation Theory (EST). [DOI](https://doi.org/10.1037/0033-2909.133.2.273)

## What the paper does

Zacks and colleagues synthesise behavioural, neuropsychological, and neurophysiological evidence to propose that the perception of event boundaries is a side-effect of an ongoing perceptual prediction system. Perceivers maintain an internal model that issues predictions about what is about to happen; when prediction error transiently spikes, an event boundary is perceived and the event model is updated. Between boundaries the model is held stable. The theory ties this account to specific neural structures: lateral prefrontal cortex for event-model maintenance, anterior cingulate and subcortical neuromodulatory systems for prediction-error evaluation.

## Findings relevant to MECH-288

For our purposes, the key claim is the trigger criterion: a transient increase in prediction error is what makes a moment a boundary. This is exactly the "(a) PE spike in a forward model" candidate trigger named in the MECH-288 spec. EST also distinguishes coarse from fine boundaries (different timescales of PE), which prefigures the hierarchical-timescale evidence we see in Baldassano 2017. And it commits to the position that event boundaries are not arbitrary external markers -- they are emergent properties of a continuous prediction system.

## Mapping to REE

MECH-288 trigger criterion (a) directly inherits the EST PE-spike account. The substrate's event_segmenter should emit a new segment_id whenever the prediction error in some forward model crosses a (possibly adaptive) threshold. The lifetime of a segment_id corresponds to the lifetime of an EST "event model" -- the interval over which the agent's predictions about the world remain coherent.

What EST does not settle: which forward model's PE counts. In REE we have several candidate forward models (E1 z_world, E2 z_self motor-sensory, harm forward model, etc.) whose PEs may or may not co-fire at boundaries. EST's theoretical commitment is at the cognitive level and does not legislate this choice for us.

## Limitations and caveats

EST was developed for human perception of everyday goal-directed activity. Whether substrate-level prediction errors in a much simpler latent-stream agent constitute the same kind of signal is an empirical question. The substrate plan should not assume that EST's specific cortical implementation (lateral PFC + ACC) maps onto REE's region scheme; only the algorithmic principle (PE spike triggers boundary) transfers cleanly. A second caveat: EST holds that knowledge structures (schemas) shape boundary placement -- a pure bottom-up PE substrate would not capture this. The architecture should leave room for top-down schema priors.

## Confidence reasoning

I score this 0.88 -- high. Source quality is excellent (Psychological Bulletin, exhaustive review with thousands of citations). Mapping fidelity is high because MECH-288's first trigger candidate is literally the EST formulation. Transfer risk pulls the score down slightly: human cognitive evidence does not automatically license the same mechanism in a simpler artificial substrate. But for purposes of saying "MECH-288 trigger criterion (a) has substantial biological grounding," EST is the strongest single source we can cite.
