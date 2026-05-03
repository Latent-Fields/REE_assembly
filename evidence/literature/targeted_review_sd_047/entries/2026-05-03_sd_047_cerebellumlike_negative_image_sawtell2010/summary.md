# Sawtell (2010): Cerebellum-like Negative Images in Mormyrid Electric Fish

The mormyrid electrosensory lobe is the canonical biological case
study for predictive cancellation circuits. Each electric organ
discharge produces a sensory reafference signal at the fish's own
electroreceptors, and the cerebellum-like Purkinje analog must subtract
this predictable pattern out so that genuinely novel signals — prey,
predators, conspecifics — survive into downstream computation.
Sawtell's 2010 *Neuron* paper used in vivo whole-cell recordings in
awake fish to show two things at once: granule cells selectively
combine sensory and motor mossy-fiber inputs, and Purkinje-like cells
acquire selectivity through anti-Hebbian plasticity tuned exactly to
the sensory-motor combinations the granule cells deliver. The phrase
"negative image" is Sawtell's: the circuit literally learns the
expected reafference and subtracts it.

The mapping into SD-047 is at the level of architectural principle
rather than substrate identity. MECH-098 (reafference cancellation) in
REE is the same kind of circuit. The substrate-ceiling argument for
why MECH-098 cannot currently be tested in V3 is essentially: the V3
env produces no continuous, autocorrelated noise floor for a
cancellation circuit to learn against. Sparse scheduled hazards are
single events, not patterns. The "predictable patterns" Sawtell's
circuit cancels are stochastic, time-varying, and have non-trivial
covariance structure with the fish's own movements. SD-047's spatial
perturbation field (smooth, autocorrelated AR(1)) and transient
Poisson events are the V3 analogs of that noise floor.

The honest caveat is that Sawtell's circuit is tuned to electrosensory
statistics, and there is no guarantee that the *specific* features
SD-047 manipulates — smoothness, autocorrelation timescale,
sparsity, lifespan — are the right discriminative dimensions for a
hazard-field comparator. The paper supports the architectural
commitment ("cancellation circuits exist and they require continuous
noise floors to learn") while leaving the feature-vocabulary question
open. This is the core risk SD-047's lit-pull is meant to expose: a
naive implementation that picks features by analogy to what makes
intuitive sense (smoothness ≈ weather, sparsity ≈ traps) may pick
the wrong features for the actual comparator REE has implemented. The
right move at implementation is to expose multiple feature axes and
let the comparator's actual learning curve tell us which it cares
about, rather than committing to one feature mapping in advance.

I read this paper as supporting SD-047 with confidence ~0.80 — the
architectural principle is well-established, the input-distribution
requirement (continuous autocorrelated noise) is exactly what SD-047
provides, and the canonical biology says this is the regime in which
the circuit works. The mapping caveat (electrosensory ≠ gridworld
hazard) is real but does not undermine the substrate-ceiling
diagnosis itself.

According to PubMed, [DOI: 10.1016/j.neuron.2010.04.018](https://doi.org/10.1016/j.neuron.2010.04.018).
