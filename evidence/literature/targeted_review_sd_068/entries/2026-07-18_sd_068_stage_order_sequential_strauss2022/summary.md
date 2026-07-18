# Order matters: sleep spindles contribute to memory consolidation only when followed by REM sleep

**Strauss et al. (2022), _Sleep_ 45(4).** DOI: [10.1093/sleep/zsac022](https://doi.org/10.1093/sleep/zsac022). Retrieved via PubMed (PMID 35037060).

## What the paper did

The sequential hypothesis of sleep-dependent consolidation says memories are first replayed in NREM and then integrated in REM — two ordered steps. The trouble with testing it is that physiology never runs the experiment: in healthy sleep, N always precedes R. You cannot ask whether the order matters when you only ever observe one order.

Strauss and colleagues found their counterfactual in pathology. Patients with central hypersomnolence disorder — narcolepsy in particular — frequently enter sleep in REM before NREM, giving genuine R-N sleep cycles. Thirty-six patients performed a visual perceptual-learning task before and after a daytime nap truncated after a single sleep cycle; 67 naps entered the analysis, split by whether the cycle ran N-R or R-N. The comparison is over-nap change in performance as a function of sleep sequence.

The result is an order effect. Sleep spindles were associated with memory consolidation *only* in the physiologically-ordered N-R naps. In R-N naps, the same spindles carried no consolidation benefit. Separately, and less comfortably for the tidy story, rapid-eye-movements within R sleep were *negatively* associated with perceptual consolidation.

## How this maps to SD-068

SD-068 builds an experiment-layer harness that makes each phase of the MECH-120 → MECH-121 → MECH-123 pipeline independently diffuse-damageable, with per-phase quality readouts. Its stated non-vacuity carrier is *damage-tolerance staging order* plus a REM passthrough-vs-generative contrast — explicitly not feed-forward error-compounding, which the claim concedes is topology-baked.

The question this paper answers is a prior one: is the pipeline's ordering a real feature of the system, or an artefact of how we chose to draw the boxes? Strauss et al. say it is real, and in a specific way that matters here. The NREM contribution is *contingent* — spindles do work only when a REM phase follows them. A phase whose output only becomes useful downstream is, in damage terms, a fragile phase: perturb it and you lose everything it was holding in trust for the next stage.

That bears directly on the SD-068 smoke-test result. The harness observed a damage-tolerance order of (nrem, rem, sws), which the implementation note flags as a partial match that *inverts* REM-vs-NREM against the naive reverse-dependency prediction. Read through Strauss, the inversion looks less like a defect. If NREM's contribution is contingent on a downstream phase, NREM presenting as least damage-tolerant is what you should expect. And the negative rapid-eye-movement effect converges, from an entirely independent direction, with the harness's null generative-REM sensitivity: both are saying REM's contribution to output quality is not a monotone gain.

I want to be careful not to let that convergence do more work than it can bear. Two independent measurements pointing the same way is suggestive; it is not a confirmation, and the harness's REM null could still be a plumbing artefact that happens to sit next to a real biological non-monotonicity.

## Limitations and caveats

The sharpest limitation is a carving mismatch. The paper's "N" is NREM as a whole — spindle-bearing N2/N3 — whereas SD-068 splits SWS denoising from NREM slot-filling into two separately-instrumented phases. So this validates a *two*-phase ordering where the harness instruments three. Whether the SWS/NREM split is a real joint or a convenient one is untouched by this evidence.

The manipulation is also the wrong shape. Strauss et al. invert stage *order*; SD-068 applies a graded RMS-scaled Gaussian sigma to phase state. Order-inversion and diffuse damage are different perturbations and need not produce commensurable orderings. The paper tells us the pipeline is ordered; it does not tell us how that pipeline degrades under noise.

And the population is atypical by construction. Narcoleptic sleep architecture is what makes the design possible and simultaneously what limits its reach — one cannot straightforwardly read healthy pipeline dynamics off a disorder of sleep-state boundary control.

## Confidence reasoning

I set this at 0.68, with mapping fidelity (0.62) as the binding constraint rather than source quality (0.78). The paper itself is good: peer-reviewed in the field's primary venue, an ingenious design, adequate n for a patient sleep-lab study. What holds the aggregate down is that it validates the premise SD-068 needs at a coarser grain than SD-068 operates. It licenses "the pipeline is genuinely ordered and earlier phases can be contingent on later ones" — which is real support for the harness's staging-order non-vacuity argument — without licensing the specific three-phase decomposition or the diffuse-damage model. That is worth having, and it is not the same as validating the harness.
