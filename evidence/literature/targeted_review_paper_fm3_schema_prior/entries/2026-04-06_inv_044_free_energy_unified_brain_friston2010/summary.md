# Friston (2010) — The free-energy principle: a unified brain theory?

**Source:** Friston K. The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience* 2010; 11(2): 127–138. DOI: [10.1038/nrn2787](https://doi.org/10.1038/nrn2787)

## What the paper argues

Friston proposes that perception, action, and learning can all be understood as instances of free energy minimisation: the brain maintains a hierarchical generative model of the world and continuously acts to minimise the divergence between its predictions and its sensory inputs. The key architectural distinction for FM3 is the separation of two processes that operate at different timescales: inference (computing the posterior over current states under a fixed generative model -- perception and attribution) and learning (updating the generative model itself -- prior construction and schema formation). These are formally distinct operations with distinct computational roles.

In the hierarchical generative model, higher levels encode the prior: the precision-weighted expectations about context structure, the transition probabilities, and the relational topology of the latent space. Lower levels compute prediction errors under these priors. Perception is posterior inference given the model. Learning is model update. The two are separated not merely for convenience but by the mathematical structure of variational inference: you cannot optimise the parameters of the generative model while simultaneously using those parameters to evaluate the likelihood of current observations without introducing circularity.

## How this connects to FM3 (architectural separation of prior construction and posterior inference)

The free energy framework provides the formal basis for why prior construction and posterior inference must be architecturally separated -- which is the core claim of FM3. The argument is not merely that it is difficult to do both simultaneously; it is that attempting to do so produces a degenerate outcome. If the generative model (the prior, the schema) is being updated during the same pass as the posterior is being computed under that model, the gradient signals mix: the model is pulled simultaneously toward explaining current observations (inference) and toward a structurally more efficient generative model (learning). These two gradients are not aligned. The result is that neither inference nor learning converges: the posterior is computed under a prior that is shifting during the computation, and the prior is updated based on a posterior that reflects both the current evidence and the model instability.

In REE terms, this is the failure mode MECH-166 predicts: slot-formation (generative model update, schema installation) and slot-filling (posterior inference, causal attribution) cannot be co-computed because the slot structure (the prior) is the very thing that must be fixed for the attribution inference to be well-posed. Friston's framework formalises why this separation is an architectural constraint, not merely a practical convenience.

The free energy principle also provides a natural account of what offline consolidation achieves: it is the phase during which the generative model can be updated without interference from ongoing inference demands. The update stabilises the prior, making the schema available as a fixed context for the next cycle of attribution inference.

## Honest caveats

Friston does not make the connection to sleep or memory consolidation explicit in this paper. The mapping from the formal separation of inference and learning to the offline/online phase structure of sleep-dependent consolidation is an inferential step that the paper itself does not take. The free energy principle treats inference and learning as occurring on different timescales within a continuous system, not as occupying different sleep stages.

The mapping from 'degenerate prior under simultaneous co-computation' to the empirical phenomena of sleep-dependent schema consolidation also requires bridging from a computational-level theory to a mechanistic-level claim. The paper provides the computational rationale for the architectural separation; the empirical grounding for why that separation is implemented by sleep (rather than, for example, by simple temporal interleaving within a waking session) must come from other sources.

This makes Friston (2010) best used in §3 as the formal backbone -- establishing why the prior-before-posterior constraint is a genuine architectural requirement -- rather than as primary empirical evidence. The empirical evidence that the constraint is violated by online computation comes from Tse et al. (2007), van Kesteren et al. (2012), and Sanders et al. (2020).

## Why cite this in §3

The FM3 argument makes a strong claim: that online co-computation is architecturally incoherent, not merely inefficient. That claim needs formal grounding, not just empirical analogy. Friston (2010) provides the computational architecture that makes the incoherence claim precise: prior construction and posterior inference are formally distinct operations in a hierarchical generative model, and collapsing them produces circular optimisation rather than convergence. Without this formal anchor, the FM3 argument can be deflected as merely a conjecture about implementation. With it, the argument has a principled basis in the mathematics of hierarchical Bayesian inference.
