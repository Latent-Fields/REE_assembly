# Active inference as message passing on a factor graph (de Vries & Friston 2017) — Q-079

**Source:** Bert de Vries & Karl J. Friston, "A Factor Graph Description of Deep Temporal Active Inference," Frontiers in Computational Neuroscience 11:95 (2017), DOI 10.3389/fncom.2017.00095.
**Direction:** weakens (the distinct-novel-object reading of Q-079).

## What the paper does

This is the bridge result. De Vries and Friston specify a full active-inference process — a deep temporal generative model, perception and learning by variational free-energy minimisation, and **policy selection by expected-free-energy minimisation** — entirely as neuronal message passing on a Forney-style factor graph (the substrate later automated in ForneyLab and RxInfer). Nothing in the agent lives outside the graph: inference and action are the same minimisation on the same object.

## Why it bears on Q-079

The research map treats "action-coupled inference" (active inference) as a *separate* nearby formalism from the graphical-model substrate (factor graphs / MRFs / DBNs), and the provisional research claim leans on the idea that no single object combines them. This paper shows the combination is already standard: put active inference **on** the factor graph and you get directed evidence update (a), undirected/cyclic coherence (b, inherited from Frey's unification), action coupling, and precision modulation (precision is just inverse variance in the generative model) — all under one representation and one algorithm. The DLIF "action loop" is not an addition to the graphical-model substrate; it is a way of reading it.

Combined with Frey (a+b) and the structure-learning / RGM entries (c, d), this entry is what lets the four-capacity combination land inside a single framework family rather than requiring a new mathematical object.

## Limits and caveats

The generative-model structure is specified, not learned — capacity (c) needs the separate structure-learning apparatus (Smith et al 2020; Bayesian model reduction). Scale here is fixed hierarchical depth, not a renormalisation operator — capacity (d) is the RGM 2024 contribution. And there is **no residue / non-erasure primitive**: active inference has precision and salience, but nothing that behaves like REE's moral residue. That gap is the one component the literature cannot fill, and it routes to ARC-013's open V3-EXQ-587, not to a DLIF object.

## Confidence reasoning

0.72. Friston + de Vries authorship and a clean methodological demonstration give high source quality and fidelity to the "one substrate carries inference + action" claim. Transfer risk is moderate because REE's commitment/selection machinery is not literally EFE-minimisation — so this is an existence proof that action coupling sits on the graph, not a claim that REE's selector *is* active inference.
