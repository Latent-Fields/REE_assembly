# Learning Task Informed Abstractions (Fu, Yang, Agrawal & Jaakkola, ICML 2021)

## What the paper did

TIA attacks the same failure as the bisimulation line but names its mechanism differently, and the difference is what makes this entry worth a separate slot. The authors' complaint is not that reconstruction discards decision-relevant content -- it is that reconstruction **spends the model's budget in the wrong place**:

> "excess model capacity is devoted to representing background information when learning from complex visual inputs. The background conveys no information about the task."

Their remedy introduces a Task Informed MDP, realised by training two models that both learn visual features via cooperative reconstruction, with one adversarially dissociated from the reward signal so that reward-correlated features and distractors are explicitly separated. They report gains over Dreamer, DBC and DeepMDP on DeepMind Control with natural-video distractors, on Atari, and -- most usefully for us -- on a synthetic **ManyWorld** benchmark where TIA's margin over Dreamer widens monotonically as more distractors are added.

## Why the allocation framing is the one SD-106 needs

The other ML entries in this pull argue about whether a generic objective *retains* what a controller needs. SD-106's measurements make that the wrong question. V3-EXQ-1041 established, order-free, that the code reaches 0.951-0.980 of the achievable PCA-32 ceiling: a great deal is retained, and generic compression is running near optimally. What SD-106 cannot do is *prioritise*. A fixed 32-dimensional budget optimised against total variance will fill itself in variance order, and there is no guarantee -- and, after V3-EXQ-1023's 0.719 consumer-rung agreement, some reason for doubt -- that decision-relevant directions are the high-variance ones.

That is exactly TIA's diagnosis, stated in terms of budget rather than of information content. It is the closest match in this pull to the shape of REE's actual evidence.

The ManyWorld dose-response is the other contribution. A monotone widening of the gap as task-irrelevant variance increases is the experimental design REE could copy at the encoder plane: vary the irrelevant-variance fraction and watch whether the consumer-rung gap tracks it. That converts the (a)/(b) pair from a pair of readings into something measurable.

## What this paper does not say

Three things, and the first is the one most easily misread. **TIA does not abandon reconstruction.** It keeps cooperative reconstruction and adds an adversarially dissociated distractor model alongside it. So the evidence here is against *unpartitioned* generic reconstruction, not against reconstruction as a component. A successor to SD-106 that simply deleted the variance-preservation term would not be the change this paper supports.

Second, the method needs a reward signal -- the distractor model is defined by being adversarially dissociated *from the reward*. Where no such signal exists at the stage the encoder is trained, which is SD-106's situation in a P0 warmup under a RandomPolicy, the mechanism cannot be applied as written.

Third, TIA's own empirical standing is contested: Tomar et al. (in this same pull) report that TIA and other reconstruction-based methods fail dramatically with distractors relative to a simple reward-plus-transition-prediction baseline. I am relying on the diagnosis, which has held, rather than on the remedy, which has not settled.

## Mapping caveat

The "background" here is literal image background and the misspent capacity is a convolutional world model's, whereas SD-106's budget is 32 latent dimensions over a non-image observation stream. The mechanism transfers as an argument about bounded codes and variance-ordered allocation; the magnitude does not. Whether REE's observation stream even contains a substantial high-variance task-irrelevant component is precisely what is unmeasured.

## Confidence

0.75. Source quality 0.85 (ICML main conference, a stated formalism, results across three benchmark families). Mapping fidelity 0.74 is the best in the ML half of this pull, because the failure is stated in terms of budget, which is the form SD-106's evidence takes -- discounted because the budget is a world model's rather than a fixed-width latent's. Transfer risk 0.42, matching the Zhang entry and for the same reason: the effect is demonstrated by injecting task-irrelevant variance at a chosen magnitude, and REE's own value on that axis is unknown.
