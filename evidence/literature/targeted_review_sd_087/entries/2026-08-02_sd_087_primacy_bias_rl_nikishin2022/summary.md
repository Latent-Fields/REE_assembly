# The Primacy Bias in Deep Reinforcement Learning (Nikishin et al., ICML 2022)

## What the paper did

Nikishin and colleagues identify a failure mode they name, after the cognitive-science effect, the *primacy bias*: deep RL agents tend to rely on early interactions and discount useful evidence encountered later. The mechanism they propose is structural rather than incidental. Because deep RL trains on a progressively growing dataset, and because the earliest transitions in that dataset are collected while the policy is still near-random, the network has ample opportunity to overfit to a set of experiences that are unrepresentative of anything it will later need. That early fit shapes the representation in a way that makes subsequent learning from novel situations harder.

They dissect which algorithmic choices exacerbate the bias, then propose a deliberately blunt remedy: periodically reset part of the agent -- discarding the fitted weights while retaining the replay buffer. It works, consistently improving performance on both Atari 100k (discrete action) and the DeepMind Control Suite (continuous action).

## Why this matters for SD-087

Of the three computational entries in this pull, this is the one whose substrate actually matches REE's. Achille et al. work on supervised vision CNNs; Dohare et al. work mainly on task-incremental supervised sequences. Nikishin et al. work on a deep RL agent training on a growing experience distribution, which is what REE's agent is. No cross-paradigm leap is required to state the mapping, which is why this entry carries the lowest transfer risk of the four.

The translation to branch (a) is direct. If the harm head is shaped during early training by the EMA accumulated-harm target -- which, given `harm_surprise_pe_enabled` defaults to False at `config.py:2306`, is what every default-trained agent does -- then primacy bias predicts that later evidence is comparatively ignored. Newly enabling a prediction-error target partway through is exactly "evidence encountered later". The predicted result is that the loss changes and the representation does not, which is the V3-EXQ-856 dissociation.

The more valuable contribution, though, is to experimental design rather than diagnosis. SD-087's registered falsifier specified a post-hoc two-arm flip, and 856 executed it faithfully; the trouble is that a post-hoc flip cannot discriminate branch (a) from branch (b), because both predict the same null. This paper suggests the discriminating design: train with the flag on *from initialization*, and add a reset arm on the harm head. If a from-initialization arm reproduces SD-020's benefit, branch (a) is supported and the encoder is exonerated. If it does not, branch (b) -- the encoder or environment -- becomes much harder to avoid. That is a genuinely better-powered successor to the falsifier as written.

## Limitations

The intervention axis is not the same, and I do not want to gloss that. Nikishin et al. change *which data the network has effectively fitted*, by resetting weights; SD-087 changes *which target the network is fitted against*, with the data stream unchanged. Both are "early training determines late outcome" stories, but only the former was measured here. Discarding a value function overfitted to early exploration data is not obviously the same operation as discarding a representation fitted to the wrong harm target -- which means the remedy might transfer even where the diagnosis does not.

Two further constraints. The headline evidence is that resets *improve* performance; that is an intervention result, not a direct measurement of irreversibility in an un-reset agent. One could accept every result in this paper and still hold that 856's null comes from branch (b). And the gains were demonstrated in deliberately sample-limited regimes (Atari 100k in particular). REE's harm-stream curriculum is not sample-limited in that way, and the effect size outside that regime is not established here. There is also a structural question I cannot resolve from this paper: `z_harm_a` is an auxiliary affective head, not the control-loop value function, and the primacy mechanism may be weaker or absent for a head whose gradients do not drive action selection.

## Confidence reasoning

Source quality 0.85 (ICML, strong empirical work across two benchmark families). Mapping fidelity is the highest of the computational entries at 0.68, because the substrate matches. Transfer risk is the lowest in the pull at 0.28.

Aggregate 0.74, set slightly above the component mean. The upward adjustment is deliberate and is about governance value rather than diagnostic strength: this is the only entry that yields a concrete, cheap, directly runnable next arm, and a paper that tells you what to do next is worth more to a claim sitting at `candidate` than one that only tells you what might have happened. Direction is `supports`, scoped to branch (a).
