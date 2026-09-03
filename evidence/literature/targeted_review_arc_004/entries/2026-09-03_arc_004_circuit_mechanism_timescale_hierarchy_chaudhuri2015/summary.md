# A Large-Scale Circuit Mechanism for Hierarchical Dynamical Processing in the Primate Cortex

Chaudhuri, Knoblauch, Gariel, Kennedy & Wang (Neuron, 2015) built a large-scale dynamical
model of macaque neocortex on directed, weighted tract-tracing connectivity, and asked what
minimally has to differ between areas for a hierarchy of timescales to appear. Their answer
is the reason this is the sharpest entry in the pull. The local microcircuit is, in their
words, "qualitatively canonical, i.e. the same across areas, but ... quantitative inter-areal
differences are crucial". Every area runs identical threshold-linear dynamics with **fixed
and identical time constants** -- `tau_E = 20 ms`, `tau_I = 10 ms` -- and identical coupling
parameters. The single thing that varies is a gradient of excitatory connection strength per
neuron along the hierarchy, indexed by basal dendritic spine count on layer-3 pyramidal
neurons, which "increases sharply from primary sensory to prefrontal areas". Out of that, a
hierarchy of timescales emerges: sensory areas respond transiently, association areas
integrate and show persistent activity, prefrontal persistence running to several seconds.
The model produces multiple temporal hierarchies depending on input modality, and the slow
prefrontal and temporal areas turn out to dominate global dynamics.

ARC-004's non-degeneracy precondition rests on exactly this possibility. It argues the claim
is not vacuously true by construction because timescale differentiation "must emerge from the
recursive top-down architecture ... rather than from a built-in rate split". Chaudhuri et al.
is the existence proof that such emergence is real: identical local time constants
throughout, and a monotonic persistence hierarchy nonetheless. That is genuine support, and
it is support for the specific logic ARC-004 uses rather than for its conclusion.

But the model earns its hierarchy with two ingredients, and naming both is where this entry
does its real work. The areas are coupled in a **directed hierarchy** -- information passes
up and down between distinct levels -- and they are differentiated by a **graded structural
parameter**. Set that against `LatentStack.encode` as built: three parallel first-order
filters, one shared `alpha_shared = 0.3`, each applied to a within-tick function of the same
input. Neither ingredient is present. The layers are not in series, and nothing is graded
across them. So the model tells us the as-built stack cannot express the property at all --
which is precisely the degeneracy the 2026-09-01 `evidence_quality_note` recorded, arrived at
by a completely independent route. A null result from the current stack would be a fact about
the wiring, not a finding about the claim, and this paper is the external argument for why.

There is a second implication that ARC-004 does not yet address. The internal serial-smoothing
probe reached the claim's own PASS bar on wiring alone -- `z_delta - z_beta` half-life delta
of +4.342 against a 0.510 bar, 10/10 seeds, with untrained encoders and a fidelity check of
`max|manual - stack.encode()| = 0.000e+00`. Serial arrangement with one shared constant was
enough. The biological existence proof needed the graded parameter *as well*. That does not
make the internal result wrong, but it does mean a REE stack that clears the bar by wiring
alone is a thinner instantiation of "multi-timescale" than the system this model describes,
and it is worth knowing that before the awaited substrate is built and the claim re-tested.

The caveats are the ordinary cross-domain ones and they are not small. This is a simulation
of macaque cortex fitted to tract-tracing data; "areas" are not "layers of a latent state
vector"; and the persistence arises from recurrent excitatory-inhibitory population dynamics
that a first-order EMA does not have, so there is no mechanism by which a connectivity
gradient could produce an analogous effect in REE parameter-for-parameter. REE has no
spine-count analogue, and its nearest available knob -- a per-layer alpha -- is exactly the
built-in rate split the precondition disclaims. What this entry licenses is two conditional
statements, and no more: identical time constants do not preclude a timescale hierarchy, and
parallel filters over a shared input do preclude one.

Recorded as `supports` at 0.74.
