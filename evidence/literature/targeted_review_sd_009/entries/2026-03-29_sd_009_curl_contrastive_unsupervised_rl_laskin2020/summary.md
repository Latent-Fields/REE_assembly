# CURL: Contrastive Unsupervised Representations for Reinforcement Learning

**Laskin, Srinivas & Abbeel (2020) -- ICML 2020**

## What the paper did

CURL introduces a contrastive auxiliary objective that can be layered on top of any model-free RL algorithm to improve the quality of the encoder learning from raw pixel observations. The contrastive objective works by specifying positive pairs -- two different augmentations of the same observation -- and training the encoder to maximise agreement between their representations via Noise Contrastive Estimation (NCE). Crucially, the contrastive loss is an auxiliary objective: it runs alongside the standard RL objective (actor-critic or DQN gradients) without replacing it. Both losses backpropagate through the encoder simultaneously. The authors tested CURL on top of SAC (continuous control, DeepMind Control Suite) and Rainbow DQN (Atari), achieving 1.9x sample efficiency gains over the prior state of the art at the 100k interaction step benchmark.

## Key findings relevant to SD-009

The paper's central finding is a demonstration that RL objectives alone are insufficient to train good visual encoders for control tasks. The reward signal is too sparse and too indirect to force the encoder to maintain the structured representations needed for effective decision-making. An auxiliary discriminative objective -- one that requires the encoder to distinguish between observations in some way -- dramatically improves the encoder's representational quality. This is the same logic that motivates SD-009: E1's prediction loss and E3's harm/goal loss do not require z_world to distinguish between hazard-present and hazard-absent states if both states have similar prediction error profiles. The CE auxiliary loss in SD-009 fills this gap in exactly the way CURL fills the analogous gap in pixel-based RL.

The mechanism is also comparable at a computational level. In CURL, positive pairs must agree in the encoder's output space regardless of surface-level augmentation differences -- this forces the encoder to find invariant categorical structure. In SD-009, the CE loss requires the encoder to assign observations to the correct event-type category -- this forces z_world to maintain a latent geometry where hazard-present states occupy a distinct region from hazard-absent states. Without the auxiliary objective in either case, the encoder is free to learn any representation that minimises the primary loss, including degenerate representations that collapse categorical distinctions.

## Mapping to REE

SD-009 can be understood as a supervised version of CURL's auxiliary objective principle. Where CURL uses unsupervised contrastive learning (no external labels, just augmentation consistency), SD-009 uses supervised CE over event categories. Supervised CE is a stronger and more targeted signal: it directly tells the encoder which category an observation belongs to, whereas CURL's signal is derived from the assumption that two augmentations of the same observation should have similar representations. In REE's gridworld, event-type labels (hazard present, absent, neutral) are directly available from the environment, so the supervised CE approach in SD-009 is feasible where it might not be in purely visual RL settings. CURL validates the general principle; SD-009 applies it in a stronger supervised form that is possible in REE's label-rich environment.

## Limitations and caveats

The loss form in CURL is contrastive-unsupervised, not CE-supervised. This is not a minor technical detail: the two objectives impose different structures on the latent space. CURL encourages augmentation-invariant features, which may or may not align with harm-relevant event categories. SD-009's CE loss explicitly targets the event-type categories that matter for ethical evaluation. The degree to which CURL's strong results transfer to SD-009's specific claim (CE auxiliary loss preserves event-type discriminability) is thus indirect. Additionally, CURL was demonstrated on high-dimensional visual observation spaces where the gap between raw pixels and useful representations is especially large; REE's gridworld is lower-dimensional, so the relative benefit of auxiliary supervision may be smaller in absolute terms.

## Confidence reasoning

The paper is high quality and its empirical results are strong and reproducible across two major RL benchmarks. The conceptual mapping to SD-009 is solid: auxiliary discriminative objectives improve encoder representations in RL settings where the primary loss is insufficient. Confidence is set at 0.74, reflecting genuine support for the mechanism while acknowledging that the specific loss form differs and the modality gap between pixel RL and REE's gridworld encoder introduces some transfer uncertainty.
