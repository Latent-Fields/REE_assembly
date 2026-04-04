# Literature Summary: 2026-04-04_mech060_active_inference_motor_adams2013

## Claims Tested

- `MECH-060`

## Source

- Adams RA, Shipp S, Friston KJ (2013), *Predictions not commands: active inference in the motor system*. Brain Structure and Function 218(3): 611-643.
- DOI: 10.1007/s00429-012-0475-5
- PMID: 23129312
- URL: https://pubmed.ncbi.nlm.nih.gov/23129312/

## Mapping to REE

MECH-060 claims that pre-commit simulation error and post-commit realized-error must be kept responsibility-distinct through a write-boundary enforced at the commitment point. A natural question is whether any biological system instantiates such a dual-channel architecture with a genuine structural separation -- or whether the idea is a REE-specific engineering requirement with no clear precedent.

Adams, Shipp and Friston (2013) provide the most precise biological parallel in the motor literature. The active inference framework resolves a long-standing paradox in motor neuroanatomy: corticospinal projections originate in infragranular layers and are highly divergent, sharing the anatomical signature of top-down modulatory connections, not driving motor commands. The authors' resolution is that descending motor projections carry proprioceptive predictions -- what the motor system expects the body to feel if the intended action executes -- while ascending spinal pathways carry the prediction error between expected and actual proprioception. Action occurs not because a command is sent but because the predicted proprioceptive state creates a discrepancy that spinal reflexes act to minimise.

The structural dual-channel maps directly onto MECH-060. The descending prediction stream is the pre-commit simulation channel: it carries the forward model's expected sensory consequence before the action's realized outcome is known. The ascending prediction-error stream is the post-commit realized-error channel: it carries the mismatch between predicted and actual sensory state, available only once action has partially or fully executed. The two streams are anatomically separated -- descending via corticospinal projections, ascending via dorsal horn pathways -- which instantiates a biological write-boundary.

The precision-weighting mechanism is particularly relevant. Adams et al. formalise that motor cortex can up-weight its predictions by increasing the estimated precision of the descending signal relative to ascending feedback. During committed action sequences, this precision elevation effectively down-weights the realized-error stream until the action completes -- the system trusts its simulation channel and attenuates post-commit feedback. This is a functional analogue of MECH-060's write-boundary enforcement: the residue field (REE's durable harm record) should not be updated by pre-commit simulation errors, only by realized outcomes, just as spinal adaptation should not be driven by predicted proprioception but by actual mismatch.

## Caveats and Mapping Limits

- The domain is motor control and sensory attenuation, not harm attribution or ethical responsibility. The conceptual mapping requires an inferential step.
- Precision-weighting is not identical to write-boundary enforcement: precision modulates signal amplitude continuously, whereas a write-boundary is a discrete gating event at the commitment point.
- The paper does not test contamination consequences -- what happens to motor learning if the pre-action prediction stream is mixed with the post-action error stream -- so it cannot directly support the MECH-060 prediction that contamination is detectable and harmful.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.68`
- Rationale: the active inference motor framework provides a well-evidenced biological instantiation of the pre-commit simulation / post-commit realized-error dual-channel structure, and the precision-weighting mechanism is a functional analogue of write-boundary enforcement; confidence limited by domain mismatch and absence of contamination-consequence testing.
