# Literature Summary: 2026-04-04_mech_061_sc_decision_termination_threshold_stine2023

> **Reconstructed 2026-08-14 from this entry's own `record.json`.** The original
> summary.md was never written: the entry landed in the 2026-04-04 batch pull
> (`0498fe4bcd`, 10 lit-pulls / 412 entries) with `summary_path: "summary.md"`
> declared and no such file on disk, and it was the only one of the eight
> `targeted_review_mech_061` entries missing one. Nothing here is new reading of
> the paper -- every section below is the corresponding `record.json` field,
> reproduced. Where a sibling entry's summary carries interpretation beyond the
> record, this one deliberately does not.

## Claims Tested

- `MECH-061`

## Source

- Stine GM, Trautmann EM, Jeurissen D, Shadlen MN (2023), *A neural mechanism for terminating decisions*.
- Neuron
- DOI: `10.1016/j.neuron.2023.05.028`
- PMID: 37352857

## What the Source Claims

The lateral intraparietal area (LIP) accumulates sensory evidence via
drift-diffusion dynamics. The superior colliculus (SC) monitors LIP activity and
applies a threshold: when LIP crosses the bound, SC fires a discrete burst that
terminates the decision and initiates the motor command. LIP and SC have distinct
single-trial dynamics (LIP: continuous accumulation; SC: discrete bursting). SC
inactivation impairs this threshold sensor, prolonging LIP buildup and delaying
decision termination.

**Study context.** Simultaneous LIP and SC recordings in macaque monkeys
performing a random-dot motion discrimination task (perceptual decision ->
saccadic response). Focal SC inactivation experiments provide causal evidence.
Single-trial neural dynamics modelled using drift-diffusion and threshold burst
models.

## Mapping to REE

The LIP-SC architecture provides the strongest available empirical model for
MECH-061's commit-boundary token. LIP is the pre-commit accumulation channel --
it runs prediction-error-weighted evidence integration, the computational analog
of REE's E2 counterfactual simulation. The SC burst is the boundary token: a
discrete neural event that marks the phase transition from deliberation to
commitment. After the burst, the relevant errors are no longer "which option has
more evidence" (LIP-level predictive errors) but "was the executed action
consequence correct" (post-commitment realized errors). MECH-061 claims this
transition is mediated by a dedicated reclassification signal -- the SC burst is
the closest biological correlate identified in the literature.

## Caveats and Mapping Limits

SC's role here is in the oculomotor circuit. The mapping to REE's commitment
boundary requires accepting that an analogous threshold-sensor mechanism operates
in prefrontal / BG circuits for higher-order cognitive decisions. This is
plausible but not demonstrated by this paper. Furthermore, the SC burst terminates
deliberation and initiates the motor plan but the paper does not examine what
happens to E2-style predictive error channels after burst -- the reclassification
half of MECH-061 is inferred, not shown.

Recorded failure signatures:

- The SC burst mechanism is specifically in the context of perceptual decisions driving saccadic eye movements; generalization to higher-level cognitive or harm-attribution commitment decisions is inferred, not demonstrated.
- The paper identifies a threshold mechanism but does not characterize what happens to error signals or learning after the SC burst -- MECH-061's claim about error reclassification is not directly tested.
- SC inactivation prolonged deliberation (LIP buildup) but the specific effect on post-commitment error routing was not the primary study target.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.77`
- `confidence_components`: source_quality 0.92, mapping_fidelity 0.73, transfer_risk 0.38
- Rationale: This is the most direct empirical match for MECH-061 in the current
  review set. Stine et al. identify the superior colliculus (SC) as a
  threshold-sensor that applies a burst mechanism to LIP's accumulated evidence
  signal, terminating deliberation and initiating commitment. The discrete SC
  burst is structurally equivalent to a commit-boundary token: it is a dedicated
  neural event that marks the transition from evidence accumulation to action
  execution. SC inactivation experiments provide causal evidence that this
  threshold-crossing mechanism is necessary for normal decision termination. The
  main discount comes from the fact that SC in this context drives saccadic eye
  movements, and the generalization to higher-order commitment events in
  non-motor domains requires an abstraction step.
