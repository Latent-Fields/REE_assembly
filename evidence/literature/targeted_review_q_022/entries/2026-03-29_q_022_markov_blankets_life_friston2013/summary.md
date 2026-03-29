# Life as we know it

**Friston (2013) -- Journal of the Royal Society Interface -- DOI: 10.1098/rsif.2013.0475 -- PMID: 23825119**

## What the paper did

Karl Friston presents a theoretical argument that life -- biological self-organisation -- is an inevitable emergent property of any ergodic random dynamical system that possesses a Markov blanket. The argument is mathematical: if a system has short-range couplings such that distant components become conditionally independent (a Markov blanket), then the internal states of that blanket will appear to minimise free energy about their blanket states. Free energy minimisation is mathematically equivalent to Bayesian inference. Therefore, any system with a Markov blanket will appear to engage in active Bayesian inference -- to model and act on its world to preserve its structural and functional integrity. The paper includes simulations of a 'primordial soup' demonstrating spontaneous self-organisation under these conditions. The Markov blanket is defined as the set of states that render internal and external states conditionally independent: sensory states (influenced by external but not internal) and active states (influenced by internal but not external) together form the blanket.

## Key findings relevant to Q-022

The critical contribution for Q-022 is the mathematical definition and its implications. The Markov blanket is a topological/structural concept: it specifies which states screen off which others in a conditional independence sense. It is not a geometric concept -- it does not describe the shape, dimensionality, or orientation of any representational space. D_eff (participation ratio) is a geometric concept: it measures how many effective dimensions a distribution uses. Hopfield familiarity is an item-level concept: it measures proximity to stored attractor states. These three are defined on different mathematical objects.

This mathematical orthogonality is the key insight for Q-022. The three framings of z_self quality that Q-022 is investigating (D_eff coherence, Hopfield familiarity, Markov blanket integrity) are not three ways of measuring the same thing. They are measuring three distinct properties of the self-model. Their empirical independence or coupling in trained REE networks is therefore an open question that cannot be resolved by definition alone -- it requires experimental dissociation (EVB-0069).

## REE translation

Q-022 asks: can D_eff and Hopfield stability dissociate in REE? The Friston 2013 formulation adds a third axis: Markov blanket integrity. The question becomes: are these three measures independent dimensions, or do they co-vary in practice?

Friston's formulation supports expecting them to be at least mathematically independent. A z_self that is coherent (low D_eff) can be in a novel configuration (low Hopfield familiarity) -- both MECH-119 and Q-022 predict this. A z_self with intact Markov blanket structure (appropriately screened off from direct external influence) can have any level of D_eff or familiarity. The expected design of EVB-0069 follows from this: three experimental conditions targeting the three regimes independently, measuring all three metrics.

For MECH-113, the three-way mathematical orthogonality means that a D_eff-only monitoring system can miss failures of familiarity (MECH-118) and failures of blanket integrity (a future MECH). The three monitoring signals are therefore not redundant -- they capture genuinely different dimensions of self-model quality.

## Limitations and caveats

Friston's paper is controversial. The claim that any system with a Markov blanket 'appears' to engage in active inference has been criticised as circular (every system can be described as minimising free energy; this does not mean every system literally does Bayesian inference) and as potentially unfalsifiable. For Q-022's purposes, the relevant claim is narrower: the mathematical definitions of D_eff, Hopfield familiarity, and Markov blanket integrity are distinct. This narrower claim is not controversial.

The application to REE's z_self requires establishing that z_self constitutes a Markov blanket in the relevant sense -- that z_self is appropriately screened off from direct external influence by z_world and the blanket states. This is an architectural property of the REE design (z_self is updated via motor-sensory reafference, not directly by world states) but has not been formally verified. The theoretical argument supports the possibility of three-way dissociation; it does not demonstrate it in REE.

## Confidence reasoning

Confidence is set at 0.72. The paper is highly influential and the mathematical argument for Markov blanket structural independence from representational geometry is sound. The limitation is that this is a theoretical existence argument: it establishes that the three-way dissociation is possible (mathematically) but does not demonstrate it empirically in any system resembling REE. This paper is best understood as the theoretical foundation for Q-022's experimental design, not as evidence for the dissociation itself.
