# Wilson et al. 2014 — Humans use directed and random exploration to solve the explore-exploit dilemma

**Citation.** Wilson RC, Geana A, White JM, Ludvig EA, Cohen JD. (2014). Humans use directed and random exploration to solve the explore-exploit dilemma. *Journal of Experimental Psychology: General* 143(6):2074-81. [DOI](https://doi.org/10.1037/a0038199). PMID 25347535.

## What the paper did

Wilson and colleagues built the Horizon task to dissociate two qualitatively different exploration strategies. Subjects play two-armed bandit games where one arm has been demonstrated four times and the other has been demonstrated only once before they begin making choices. The number of choices a subject will make after that point — the horizon — is either 1 or 6. Under horizon=1, only the next choice matters; under horizon=6, the subject can exploit anything they learn from an early information-gathering choice for five further trials.

The two strategies the task was built to dissect are: (a) **directed exploration**, where the subject explicitly biases toward the less-informed arm because the prospective information is valuable for future trials, and (b) **random exploration**, where the subject simply makes a less consistent choice — higher decision noise. A model with both knobs (an information bonus and a decision-noise parameter) was fit to each subject's choices. Subjects had both higher information bias AND higher decision noise in horizon=6 relative to horizon=1. Both effects were significant and independently modulated. The paper concluded that both strategies are present in human exploration and can be separately tuned.

## Relevance to Q-043

This is the behavioural foundation for Q-043's premise that MECH-313 and MECH-314 are separate, independently calibrable mechanisms rather than two readings of one underlying quantity. The directed strategy in Wilson's framing is state-dependent and information-seeking — that maps onto MECH-314 (structured curiosity bonus driven by uncertainty over rule discrimination). The random strategy is state-independent decision noise — that maps onto MECH-313 (stochastic noise floor that prevents complete deterministic collapse). Wilson 2014 establishes that humans can independently turn each knob: longer horizons increase BOTH, and parameter recovery confirms the model can separately identify them from choice data.

For the V3 parametric sweep that Q-043 proposes, Wilson 2014 supplies the behavioural-level prediction. If MECH-313 and MECH-314 are independently load-bearing in REE, a calibration sweep on SD-054 should find a Pareto frontier where both objectives (behavioural diversity, task reward) are jointly maximised at some non-extremal (w_313, w_314) combination, much as Wilson's subjects sit at non-extremal mixtures of the two strategies under horizon=6.

## Caveats and what this paper does NOT establish

Wilson 2014 is purely behavioural; it does not pin down the substrate of either strategy. The neural-system attribution work happens in two follow-on papers (sibling entries: Zajkowski 2017 establishes that the directed system is in the right frontopolar cortex via inhibitory TMS, and Warren 2017 establishes that the random system is sensitive to LC-NE manipulation via atomoxetine). Wilson 2014 also does not adjudicate between a softmax-temperature account of random exploration and a tonic-NE account — those are observationally indistinguishable at the choice level.

The Horizon task uses two-armed bandits with fixed within-game distributions, which is a much simpler substrate than SD-054 reef. The transfer from Wilson's task to REE's reef-vs-forage environment is not literal; what carries is the algorithmic-level claim that two distinct mechanisms exist and are separately tunable.

I am also aware that the random-exploration effect size in Wilson 2014 is modest compared to the directed-exploration effect, leaving some room for alternative interpretations where decision noise is a measurement artifact rather than a genuine strategy. The TMS and pharmacological dissociations in the sibling papers address this.

## Confidence reasoning

I assign 0.85. Source quality is high (J Exp Psych Gen, replication across two experiments, parameter recovery), mapping fidelity is high (Wilson's directed/random dissociation cleanly maps onto MECH-314/MECH-313 algorithmic roles), and transfer risk is modest (different task structure but substrate-general algorithmic distinction). The 0.85 is conservative because the random-exploration effect is the smaller of the two, and one could argue that MECH-313 is the harder leg to defend on Wilson alone — the supporting evidence for it comes more from the Warren atomoxetine paper.
