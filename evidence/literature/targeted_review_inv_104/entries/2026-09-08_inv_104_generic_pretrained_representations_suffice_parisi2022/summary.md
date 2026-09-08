# The Unsurprising Effectiveness of Pre-Trained Vision Models for Control (Parisi et al., ICML 2022)

## Why this entry exists

A literature pull for INV-104 that returned four papers all agreeing with it would be a bad pull.
INV-104 registers its own vacuity route -- F1 -- and says explicitly that a null there is a useful
result: if `R_k >= 0.75` for every measurable class through a compression trained on generic
predictive or reconstruction objectives with no class-specific pressure, then generic compression
already preserves what the organism needs, the preservation contract does no work, and the pressure
to complicate z_world should be relieved rather than resisted. This is the closest published
approximation to that condition that I could find, and it is included on those terms.

## What they did

Parisi and colleagues take encoders pre-trained on standard out-of-domain vision corpora -- MoCo,
CLIP and relatives, trained on ImageNet-scale data with no access to any control task -- freeze
them, and use their features to train visuo-motor policies across four quite different domains:
Habitat navigation, DeepMind Control, Adroit dexterous manipulation, and Franka Kitchen. They vary
training method, augmentation, and which layer of the feature hierarchy is read out. The headline is
that frozen pre-trained features are "competitive or even better than ground-truth state
representations" for training control policies -- and that this holds despite the encoders never
seeing in-domain data.

Read against INV-104, the structure of that experiment is close to the F1 condition. The compression
had no reward signal, no organism, no consequence structure, and no class-specific pressure of any
kind. Whatever the downstream policies needed, the generic objective preserved -- at a level
competitive with having the true state handed to you.

## How far it actually weakens the claim

Less far than the headline suggests, and I want to be precise about where the slack is.

First, the measurement is not F1's measurement. F1 asks for a per-class retained fraction R_k
against a raw-input ceiling and an untrained-projection floor. Parisi et al. report task-level
policy performance against a ground-truth-state arm. Those coincide only if the tasks require every
class the contract lists, and they do not.

Second -- and this is the substantive limit -- the benchmark tasks have thin consequence structure.
Short-horizon manipulation and navigation require class 1 (consequence, opportunity and threat) and
some of class 2. They require very little of class 3 (persistence and temporal relation across time),
essentially nothing of class 4 (causal ancestry, intervention handles), and nothing at all of class 5
(independently evolving trajectories). So the classes most at risk from generic compression are the
classes these benchmarks are least able to detect the loss of. F1 requires the null "for every class
measurable at this stage"; this paper demonstrates it for the easiest classes on tasks that do not
test the hard ones.

Third, there is a data-scale confound that is easy to miss. These encoders saw ImageNet-scale
real-world imagery. REE's z_world is trained on its own comparatively tiny synthetic stream. "Generic
objectives preserve what control needs" may be a statement about corpus scale rather than about
compression objectives, and the two have very different implications for whether SD-070's P0a warmup
is enough to make the site non-degenerate (NDP-1).

Fourth, the finding is contested in the setting REE most resembles. Schneider et al. (NeurIPS 2024,
arXiv 2411.10175) benchmarked pre-trained visual representations in *model-based* RL and found them
"not more sample efficient than learning representations from scratch" and no better out of
distribution, tracing the difference to the quality of the learned dynamics model. REE's z_world does
not feed a model-free policy; it feeds E1/E2 rollout, which is a model-based consumer. If the
model-based result is the right reference, this entry's weakening force largely evaporates -- and
notably, "the dynamics model is where it goes wrong" is close to INV-104's own phrasing about leaving
distinctions "recoverable through its dynamics".

## Confidence

0.64, direction `weakens`. It is a well-executed ICML paper making a real point against the claim,
and recording it as anything other than disconfirming would be dishonest bookkeeping. But its
transfer to INV-104 is limited by a measurement mismatch, by benchmark tasks that under-sample the
contract's hard classes, by a data-scale confound, and by a direct contradiction in the model-based
setting. On balance it should raise the prior that F1 is live for class 1 specifically, and should
not much move it for classes 3-5.
