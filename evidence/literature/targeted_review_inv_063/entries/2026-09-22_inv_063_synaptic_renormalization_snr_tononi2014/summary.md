# Sleep and the price of plasticity (Tononi & Cirelli, 2014)

The synaptic homeostasis hypothesis holds that waking experience drives a net increase in synaptic
strength which is unsustainable in energy, space and signal-to-noise terms, and that sleep's
spontaneous activity renormalizes net synaptic strength through activity-dependent down-selection.
The formulation that matters for us is the review's own: waking learning *decreases* signal-to-noise
ratios, and sleep restores them. The quantity that is restored is a ratio. The quantity that is
reduced is a magnitude.

That asymmetry is the only account in this literature which predicts, rather than merely tolerates,
the pattern INV-063 leg B actually measured: frozen-battery MSE worse on 9/9 cells while the trained
contrastive objective moved the other way. If a consolidation pass renormalizes magnitudes while
improving relative separability, then a per-element reconstruction error -- a pure magnitude
statistic -- is expected to worsen, and a statistic defined on relative arrangement is expected to
improve, from one and the same weight change. The record already named this the objective-mismatch
signature. SHY says the mismatch is not an accident of tuning but the shape of the process.

The REE side of the mapping is where this becomes concrete, and it is also where I want to be
careful about what is doing the work. `compute_e2_world_loss` optimises an InfoNCE whose logits are
`-||pred_j - target_i||^2 / tau` -- a K-way discrimination among the in-batch targets. Cross-entropy
is taken over the prediction index, so within a row the target's own norm is constant and cancels;
what survives constrains only the relative arrangement of predictions against targets. The objective
is satisfied once each prediction is nearer its own target than any competitor, and it places no
lower bound whatever on the absolute distance to that target. Scoring it with per-element MSE is
reading a magnitude off a process that only ever controlled a ratio. That is an algebraic fact about
the REE objective, and it holds whether or not SHY is a correct account of biological sleep.

I have deliberately put the load on that algebra rather than on this paper, because SHY is contested.
Frank's standing objection (Neural Plast 2013;2013:394946) is that the hypothesis's cellular
mechanisms are poorly defined and that no theory of sleep function is complete without them; net
downscaling has not been observed universally across preparations. The directory's Cordi & Rasch
2020 entry is a further counterweight on robustness generally. A REE mechanism that *depended* on
SHY being true would import that dispute wholesale, which is why the claim this entry supports is
stated as a property of the measurement rather than as a fact about sleep.

One further caution, and it cuts against the cheapest falsifier rather than for it. The review
describes down-selection as *selective*, not as a uniform proportional rescaling. A selective process
is not a global gain change, so absorbing the across-sleep MSE delta with a single fitted scalar is
not what SHY predicts -- SHY predicts a structured, weight-specific change that a one-parameter
recalibration would only partly absorb. If the REE falsifier fits one scalar and absorbs, say, 60%
of the delta, that is neither a clean confirmation nor a refutation unless the threshold was
pre-registered. Confidence 0.58, the lowest of this batch: source quality 0.75 (Neuron, enormously
cited, but the proponents' own statement of a contested framework), mapping fidelity 0.55 (the
magnitude-versus-ratio dissociation transfers; the biology does not transfer at all), transfer risk
0.55 -- no synapses, no homeostat, and an unsettled dispute in the source field.
