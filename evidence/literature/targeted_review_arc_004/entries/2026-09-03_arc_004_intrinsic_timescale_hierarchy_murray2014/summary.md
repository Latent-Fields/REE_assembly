# A hierarchy of intrinsic timescales across primate cortex

Murray and colleagues (Nature Neuroscience, 2014) took single-unit recordings pooled from
several laboratories across macaque cortex -- sensory through parietal to prefrontal -- and
asked a question that, as they point out, had surprisingly little direct evidence behind it
despite hierarchy being a founding organising principle of cortex: are areas specialised in
the *temporal* domain? They measured the timescale of intrinsic, task-independent
fluctuations in spiking activity by fitting exponential decay to the spike-count
autocorrelation across time lags, and found a hierarchical ordering. Sensory areas show
short timescales; prefrontal areas show long ones. Their reading is that intrinsic timescales
reflect areal specialisation for task-relevant computation over multiple temporal ranges.

ARC-004's own MEASUREMENT section proposes this exact technique -- per-layer lag-k
autocorrelation and persistence half-life over `z_beta`, `z_theta`, `z_delta` -- and its PASS
criterion is this result's exact shape: a monotonic ordering of effective persistence along
the stack, with `z_delta` slowest. So this paper is the empirical precedent for both halves
of ARC-004's test design at once. It establishes that "the levels of a hierarchy are
stratified by intrinsic timescale" is a real, measurable property of a hierarchical system
rather than a modelling convenience, and that autocorrelation decay is an adequate estimator
of it. That is worth having on the record for a claim that, as of 2026-09-01, has zero
entries in `claim_evidence.v1.json` and has never been tested.

What it is *not* is evidence about REE's stack, and the distinction matters enough that I
want it stated rather than left to inference. Murray et al. measure cortical **areas**,
connected in a directed feedforward/feedback hierarchy established independently of the
timescale data. ARC-004 is about **layers of a single latent state vector**. And the
registry's own finding from 2026-09-01 is that as built those layers are not a hierarchy of
the relevant kind at all: three parallel first-order filters sharing one hardcoded
`alpha_shared = 0.3`, each applied to a within-tick function of the same input. So this entry
supports the *target property* while remaining entirely silent on whether the substrate can
express it. It should never be cited as evidence that L-space is multi-timescale.

Two further discounts. The recordings are pooled across laboratories, tasks and preparations,
so the ordering is a between-dataset regularity -- a failure of the ordering within an
individual animal would not have been visible. And the measure is of *intrinsic* fluctuation,
i.e. of the persistence of spontaneous dynamics, which is a slightly different thing from the
temporal aggregation of task-relevant information that ARC-004's layers are supposed to be
doing. The literature has largely treated these as the same quantity; it is worth not
forgetting that this is an assumption.

Recorded as `supports` at 0.68. High source quality, moderate mapping fidelity -- the method
transfers exactly, the object measured does not.
