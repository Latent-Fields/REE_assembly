# Changing the denominator moves the optimum

Sardana, Portes, Doubov and Frankle modified the Chinchilla scaling laws to include inference
cost alongside training cost, and asked where the optimum sits when you are paying for a model
over its whole deployed life rather than only paying to build it. Their answer: anyone
expecting substantial inference demand — their worked case is on the order of a billion
requests — should train models *smaller and longer* than Chinchilla-optimal. They trained 47
models to check it, found quality still improving as tokens-per-parameter is pushed to extreme
ratios up to 10,000, and noted that laws fitted only at typical ratios overestimate the
marginal value of extra tokens out at those extremes.

Q-093 makes an unusual choice of denominator. It refuses parameter count, refuses per-step
compute, and insists on total lifetime cost: developmental compute, environmental experience,
inference, memory storage and retrieval, offline replay and consolidation, adaptation after
change, planning and counterfactual simulation. Framed that way it can look like special
pleading — a denominator chosen because it flatters the system being defended. This paper is
the evidence that it is not. Within the mainstream scaling-law literature, on its own terms,
moving from training-only to training-plus-inference accounting *demonstrably relocates the
optimum*. The choice of denominator is a substantive empirical commitment, not a framing
preference, and Q-093 is on solid ground in making it explicit.

It also shows the shape of the instrument. The result comes from fitting cost-versus-quality
curves across many configurations, not from comparing two systems at two points. Q-093's
`what_would_answer` asks for scaling curves rather than a single head-to-head, and this is what
that looks like when done properly.

Where it stops is the caveat that matters most, and it cuts against REE rather than for it.
This paper's lifetime cost counts pre-training and inference only. It excludes memory storage
and retrieval, offline replay and consolidation, and post-deployment adaptation — precisely the
terms Q-093 requires, and precisely the terms where REE's replay, residue and consolidation
machinery *add* cost with no counterpart in a deployed transformer. Adopting this accounting
wholesale would bias the comparison in REE's favour, which is the opposite of what the claim
needs. A REE system could plausibly win on inference and lose on consolidation, and nothing
here would detect that.

One further hazard worth carrying into the protocol: the optimum depends on an *assumed*
inference demand. Q-093 specifies no comparable deployment-volume parameter, so a
REE-versus-baseline lifetime-cost verdict could be flipped by an unstated assumption about how
much the systems get used. That parameter must be fixed and declared before any comparison is
run, not chosen afterwards. Confidence 0.68: strong, well-controlled work supporting the
measurement half of Q-093 and silent on its architectural half.
