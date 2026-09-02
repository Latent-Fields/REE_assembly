# Shazeer et al. (2017) -- competent components that the gate never selects

**Claim tested:** ARC-131 (installability is a competence dissociable from isolated component-level validation)
**Direction:** supports | **Confidence:** 0.70

## What the paper did

The sparsely-gated mixture-of-experts layer places thousands of feed-forward subnetworks behind a
trainable gate that selects a handful per example, the design that made conditional computation
practical at scale (models up to 137 billion parameters, on language modelling and machine
translation). The result the paper is famous for is the capacity gain. The result that matters here
is the one they had to solve on the way, reported almost in passing: "We have observed that the
gating network tends to converge to a state where it always produces large weights for the same few
experts." And crucially: "This imbalance is self-reinforcing, as the favored experts are trained
more rapidly and thus are selected even more by the gating network."

Their fix was not architectural but an added objective -- importance and load auxiliary losses,
where the importance loss "encourages all experts to have equal importance". Nothing in the primary
task objective causes the components to be used.

## Why it bears on ARC-131

The experts are the cleanest imaginable instance of ARC-131's subject: components that would pass
any isolated test, since they are just feed-forward networks that work fine standing alone. Their
failure is entirely at the level of the composed system's recruitment dynamics. No expert is broken.
No expert is even suboptimal in the relevant sense. They are simply never entered, and the system's
own learning makes that condition worse rather than better over time.

Two things transfer. The first is ARC-131's specific claim that composition changes "the
scale/variance of competing signals" -- here the gate's own learning dynamics *are* the competing
signal, and they operate against the un-recruited component with a rich-get-richer geometry. This is
a concrete, mechanistically legible instance of a channel ARC-131 states abstractly.

The second is more useful to REE's audit practice. Because the imbalance is self-reinforcing, "run it
longer" is not a remedy -- the null deepens. And because the fix required an auxiliary term that
exists for no other purpose, the diagnostic question is not "was the mechanism recruited" but "what
in the architecture would ever recruit it". That is precisely the finding ARC-131 records for the
inert coalition controller: typed control demands exist, coalition templates exist, a controller
exists, and no endogenous monitor invokes any of it. Shazeer et al. supply the external precedent
that this is a normal and expected failure of composed systems, not an REE-specific oversight.

## Limitations and caveats

The gate is a single differentiable routing layer trained jointly with its experts. REE's
recruitment paths are heterogeneous, partly hand-written, and mostly not differentiable, so the
specific rich-get-richer mechanism does not transfer. What transfers is the structural point that
recruitment is a distinct function from competence and can fail on its own.

The remedy emphatically does not transfer, and this is the caveat I would most want a future reader
to carry. MoE experts are interchangeable in kind, which is what makes load-balancing coherent; REE's
mechanisms are typed and non-substitutable. Forcing uniform recruitment across REE mechanisms would
violate ARC-131's own explicit caution -- that some mechanisms should be conditionally recruited,
developmentally staged, or mutually inhibitory, and the requirement is that the architecture *can*
compose or recruit the mechanism where its own claim assigns it a role, not that it must always be
active. Cite this paper for the failure. Do not cite it for the fix.

Finally, the paper documents this as an obstacle it routed around, not as a controlled study of
non-recruitment. There is no measurement of how often it occurs, under what conditions, or how large
the resulting capability loss is.

## Confidence reasoning

Source quality 0.85, and the reason is not the citation count. The specific finding has been
independently re-derived by essentially every large mixture-of-experts system built since -- load
balancing is now standard practice because leaving it out reproduces the collapse. That kind of
repeated independent re-encounter is stronger evidence than a single controlled study. Mapping
fidelity 0.70: good on the failure mode, weaker on everything else, and explicitly zero on the
remedy. Transfer risk 0.40. Aggregate 0.70.
