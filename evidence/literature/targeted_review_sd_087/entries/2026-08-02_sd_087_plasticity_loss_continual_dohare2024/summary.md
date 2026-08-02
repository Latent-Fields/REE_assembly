# Loss of plasticity in deep continual learning (Dohare et al., Nature 2024)

## What the paper did

Dohare and colleagues asked whether standard deep learning can keep learning indefinitely, and answered no. Across Continual ImageNet, class-incremental CIFAR-100, Online Permuted MNIST and a PPO ant-locomotion task, networks trained on a long sequence of tasks progressively lose the ability to learn new ones -- degrading, in the paper's headline phrasing, until they learn no better than a shallow network. The numbers are stark: networks that began around 88% accuracy on early Continual ImageNet tasks had lost substantial plasticity by the 2,000th task and eventually fell *below a linear network*; the incrementally trained CIFAR-100 system ended 5% below a retrained one; the PPO ant improved for about 3 million steps, then collapsed and was failing every episode by 20 million. In Online Permuted MNIST up to 25% of units were dead after 800 tasks.

The loss occurred across a wide range of architectures, optimizers, activation functions, batch normalization and dropout, which is what makes this more than a quirk of one setup. It was substantially eased by L2 regularization, particularly combined with weight perturbation. Their proposed fix, continual backpropagation, reinitializes a small number of the least-used units during training -- typically fewer than one per step, with a replacement rate as low as 1e-5 -- while protecting freshly initialized units for a maturity threshold so they are not immediately recycled.

## Why this matters for SD-087

Branch (a) of SD-087's post-856 explanation -- that `harm_surprise_pe_enabled` must be on from the start of training -- has a precondition that is easy to skip past: it requires that a network's capacity to be *re-taught* decays with training rather than staying constant. If plasticity were constant, flipping the flag late would work as well as flipping it early, and the V3-EXQ-856 null would have to be explained some other way. This paper is the strongest venue-verified evidence that the precondition holds in general.

Applied to run 856, the account is coherent: if the harm head has lost plasticity by the time the flag is flipped, then the flip is being applied to a network that can no longer act on it. That reproduces the observed dissociation -- loss target moved (`mean_harm_obs_ema` 0.0 -> 0.0245), downstream signature did not (`mean_cov_z_harm_a` essentially flat). The paper also hands REE something more useful than a diagnosis: a remedial arm. A reinitialization schedule on the harm head is a concrete, cheap intervention that a follow-up experiment can carry alongside the from-initialization arm.

## Limitations, and why I did not score this higher

The horizon mismatch is the dominant problem and it cuts straight at the mapping. Plasticity loss here accrues over hundreds to thousands of *task boundaries*. REE's manipulation was one flag flip inside a single training run with no task-incremental structure at all. Invoking this paper to explain 856 requires assuming REE's regime already induces comparable plasticity decay -- and that assumption is unmeasured. If it is false, the mechanism simply had no time to operate and this entry explains nothing about the run.

Two further caveats. Because L2 regularization plus weight perturbation substantially eases the effect, a substrate that already applies weight decay to the harm head should expect an attenuated version, weakening the support correspondingly. And the paper's diagnostic is unit death and loss of representational diversity -- not target mis-specification. An agent whose `z_harm_a` is saturated because it was trained against the wrong target is not obviously suffering the same failure as an agent whose units have died. Those are two different pathologies that happen to produce the same surface symptom of "new signal fails to take".

## Confidence reasoning

Source quality is the highest in this pull at 0.92 -- Nature, with replication across architectures, optimizers and both supervised and RL settings. But I have deliberately let the aggregate track mapping fidelity (0.52) rather than venue, and set it at 0.62. A Nature paper about the wrong horizon is still about the wrong horizon, and prestige should not be used to launder a loose mapping; that is precisely the kind of move the `mapping_fidelity` component exists to prevent. Transfer risk is 0.40, held down from higher by the PPO ant demonstration, which shows the phenomenon is not confined to supervised vision.

Direction is `supports`, and specifically it supports the *precondition* for branch (a) rather than branch (a) itself. That is a weaker and more honest claim than "this explains run 856".
