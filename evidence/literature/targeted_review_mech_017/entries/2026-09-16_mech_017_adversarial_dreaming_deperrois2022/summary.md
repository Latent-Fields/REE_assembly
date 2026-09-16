# Learning cortical representations through perturbed and adversarial dreaming (Deperrois, Petrovici, Senn & Jordan, 2022)

This is the entry in the pull that implements MECH-017 rather than describing it, and it is
therefore the one that can be wrong in an informative way. The authors build a cortical
architecture in the shape of a generative adversarial network and run it through three states with
different objectives. In wake, the encoder maps external input upward and the generator
reconstructs it, under a reconstruction loss with a Gaussian latent regulariser. In NREM, latent
codes are recalled from a hippocampal buffer, rendered back into images, perturbed by suppressing
early sensory units, and the encoder is trained to recover the original latent from the corrupted
render -- "perturbed dreaming". In REM, stored memories are mixed with noise and the generator
adversarially produces activity that the encoder must learn to classify as internally rather than
externally driven. They train on CIFAR-10 and SVHN.

The result that matters for REE is the ablation, not the headline. Linear readout of semantic
category from the learned latent gives 58.25% on CIFAR-10 and 78.92% on SVHN for the full model.
Remove REM and both collapse -- 46.00% and 42.30%. Remove NREM and they barely move: 58.00% and
73.25%, with NREM's contribution showing up instead as robustness to occluded inputs. So the two
offline phases are not redundant and they do not do the same job. One buys semantic fidelity, the
other buys robustness, and the model that has only replay has the robustness and not the fidelity.

That dissociation is the finding I would carry into REE. MECH-017 lists replay-based learning,
prediction error minimisation and uncertainty recalibration as though they were three descriptions
of one consolidation process. This model says they are a division of labour, and that an offline
phase built solely around replaying stored latents -- which is the natural first implementation,
and the one ARC-007's hippocampal path-replay framing invites -- would be the ablated-REM variant.
It would look like it was working. It would improve robustness. And on the measure MECH-017
actually cares about, the fidelity of the generative model, it would be the worse of the two
designs by twelve points on CIFAR-10 and thirty-six on SVHN.

The caveats are substantial and the authors state most of them. Credit assignment is
backpropagation with no proposed cortical implementation; training is batched; convolutional
layers and the simple hippocampal buffer are acknowledged as biologically unrealistic; and the
architecture needs feedforward and feedback streams that can be separated by brain state, with
lateral interactions gated off by a mechanism the paper does not supply. To that I would add a
concern of REE's own: "world model" here means a model of static 32x32 image statistics. There is
no time, no agency and no consequence in CIFAR-10. MECH-017 is about the model that grounds
decisions in an environment, and the gap between those two things is wide enough that the twelve
points should be read as a demonstration that the dissociation is possible, not as a measurement of
how large it would be in REE. The measure itself is also a proxy -- linear separability of
categories, which a substrate could improve while its forward predictions got worse.
