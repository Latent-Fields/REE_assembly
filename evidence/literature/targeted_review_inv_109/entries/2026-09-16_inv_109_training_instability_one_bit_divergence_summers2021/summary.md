# Nondeterminism and Instability in Neural Network Optimization (Summers & Dinneen, ICML 2021)

## What the paper did

Summers and Dinneen set out to answer a question the field had mostly been answering by folklore: when two runs of the same training recipe produce different models, which source of randomness is responsible? They build an experimental protocol that lets them vary one source at a time -- parameter initialisation, data ordering, data augmentation, and the low-level floating-point nondeterminism of GPU kernels -- and measure the resulting model diversity, using disagreement between the trained models' predictions and representational distance rather than top-line accuracy. The design is the contribution as much as the result: isolating sources requires holding everything else bit-fixed, which most reproducibility studies do not do.

The headline finding is that the isolation was, in a sense, wasted effort -- and that is what makes it interesting. Every source produces statistically indistinguishable diversity. Changing only the initialisation seed moves the endpoint about as far as changing the initialisation, the data order, the augmentation stream and the kernel nondeterminism together. To explain this the authors look past the individual sources to the procedure itself, and show that training is unstable end-to-end: a **one-bit** perturbation to a single initial parameter is sufficient to send the run to a "vastly different" set of final weights. Their closing section proposes two mitigations (accelerated ensembling, test-time augmentation) which reduce the *variance of the reported metric* without touching the instability underneath.

## How this bears on INV-109

INV-109 asserts that re-running a documented deterministic recipe reconstitutes an operating regime, and licenses a within-run paired comparison and nothing whatever about the identity of the artifact a prior run measured. Read alongside this paper, that stops being a methodological scruple and becomes a statement about the dynamics: the map from recipe to endpoint is not approximately injective, so there is no sense in which a faithful reproduction lands "near" the original endpoint in weight space.

The specific value here is that it closes off the most natural objection to INV-109, which is gradualist -- *surely if we pin enough of the recipe, the endpoints converge?* Summers and Dinneen answer it directly. Pinning everything but one bit is not enough. There is no pinning budget at which the endpoint comes back. That is why INV-109 can say a pinned substrate COMMIT is not a substitute: the commit constrains the code path, and the code path is not what is unstable.

It also reframes what V3-EXQ-1010 recorded. The weight deltas against 1008 (seed 42: 0.2930078 against 0.2929618) and `substrate_stable_across_run: false` read, in the audit, like evidence of something having gone slightly wrong -- a machine-class artefact, a drift to be tightened up. On this paper's account they are the ordinary and expected signature of having re-derived rather than loaded, and tightening the pin would not have removed them.

## Limitations, and where the mapping thins

Two gaps are worth being honest about. The first is domain: all of this is supervised image classification trained to convergence, and REE's endpoints come from short, heavily-constrained episodic curricula (60 P0a + 200 P0 + 90 P1 episodes in the 1010 lineage). A curriculum that contracts hard toward a fixed point could be better conditioned than CIFAR-scale SGD, and this paper does not rule that out. The inference direction is still safe -- instability in the easier setting makes endpoint non-identity in the harder one more likely, not less -- but the *magnitude* does not transfer, and nothing here predicts how far apart two REE reproductions will land.

The second is the dependent variable. The paper measures functional diversity, not weight identity. INV-109's prescription is a recorded `hash_tensor_state` at both endpoints, re-verified at every evaluation boundary. Summers and Dinneen never hash anything; they measure whether the models disagree on inputs. That is arguably the stronger result -- the reproductions are not merely different objects, they are different functions -- but it is a proxy for what INV-109 actually asks to be checked, and an entry citing this paper as showing "the weights differ" would be over-reading it.

There is also a mild irony worth recording. The paper's own remedy is to make the reported metric more stable across runs. Applied to REE, that would make the regime-level agreement (participation ratios, in-band consumer-width values) *more* convincing while leaving the endpoint-identity claim exactly as unsupported as before. That is precisely the failure INV-109 was registered to catch, arriving under the banner of better methodology.

## Confidence

0.82. Venue and design are both strong, the finding is directly load-bearing for the claim's central mechanism, and the one-bit result is unusually clean as a refutation of the gradualist objection. The discount is entirely transfer: vision classification to episodic encoder curricula, and functional diversity to weight-state identity. Neither is a reason to doubt the paper; both are reasons not to quote its numbers as if they were REE's.
