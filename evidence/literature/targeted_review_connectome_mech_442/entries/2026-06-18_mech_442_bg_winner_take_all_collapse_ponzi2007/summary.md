# Ponzi 2007 -- the basal-ganglia gate is winner-take-all and collapses to a single action

*According to PubMed.* Ponzi 2007, *Neural Networks* ([DOI](https://doi.org/10.1016/j.neunet.2007.12.040)).

## What the paper did
This is a firing-rate dynamical model of basal-ganglia action selection grounded in BG anatomy: cortico-striatal synapses encoding cue-action associations, medium-spiny neurons representing actions, and dopamine-driven three-factor plasticity. A *double* winner-take-all selects exactly one cue and exactly one action. On a delayed cue-reward task the model shows a transition over learning: from an *exploratory* phase, where actions are generated essentially at random, to a *stable directed* phase, where the agent always chooses the single correct action for each state.

## Key findings relevant to MECH-442
This is the load-bearing counter-evidence -- and it is exactly what makes the lit-pull worth running before registering. The basal-ganglia selection gate, in its canonical computational form, is a winner-take-all that resolves to *one* action, and as the reward gradient strengthens it collapses from diverse-exploratory to single-directed. In REE's vocabulary, that collapse is the biological face of MECH-439 F-dominance: the committed selector is *supposed* to converge on the value-maximizing action. Diversity does not survive the selection gate; it is something that exists *before* the winner-take-all (the exploratory phase) and is squeezed out as exploitation takes over.

## How it translates to REE
The implication for MECH-442 is sharp and constructive: a behavioral-descriptor archive cannot be a structure that operates *at* the committed argmax to keep multiple niches selectable simultaneously -- the biological gate is a single-winner device. The archive has to live *upstream of* the winner-take-all, or *restrict the eligible set before* it. That is precisely what the already-validated V3-EXQ-569i top-k shortlist does: it shortlists an eligible set (the k F-best) and then runs the within-set selection. The MAP-Elites generalization is then "make the eligible-set restriction behavioral-descriptor-indexed rather than F-rank-indexed" -- an upstream eligible-set move, not an at-argmax per-niche store. So this paper *weakens* the naive at-the-gate reading of MECH-442 and *corrects* its framing toward an upstream / eligible-set-restriction mechanism, leaving the F-dominated argmax itself biologically faithful.

## Limitations and confidence
It is a model, not a measurement, and an older one; but its framing (BG as a winner-take-all that exploits once learned) is canonical and well-supported across the selection-problem literature. It weakens the *at-the-argmax per-niche* reading with good fidelity, while not weakening the upstream-archive reading -- so I record it as `weakens` for MECH-442 as originally framed, with the explicit note that it sharpens rather than refutes the underlying idea. Net confidence 0.66.
