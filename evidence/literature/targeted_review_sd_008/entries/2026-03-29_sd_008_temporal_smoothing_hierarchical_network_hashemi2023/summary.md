# Robust and efficient representations of dynamic stimuli in hierarchical neural networks via temporal smoothing

**Hashemi et al. (2023) -- Frontiers in Computational Neuroscience**

## What the paper did

This computational modeling study examined how temporal smoothing affects the quality of neural representations in a hierarchical visual network processing dynamic (moving) stimuli. The authors framed neural coding as a tradeoff between efficiency (minimising redundancy, maximising information) and robustness (resistance to noise and transmission delay). They showed that smoothness -- making representations of similar inputs similar -- provides informational redundancy that helps downstream layers cope with the stochastic noise and inter-level transmission delays that are unavoidable in any biological or hierarchical computational system. The key insight is that when a dynamic stimulus is processed hierarchically, an upper layer always carries slightly older information than a lower layer due to transmission delay, so some degree of smoothing actually improves the coherence of cross-level representations.

## Key findings relevant to SD-008

The paper establishes that smoothing level is a genuine design parameter with quantifiable consequences for representational quality. At one extreme (no smoothing), representations are maximally information-dense but fragile to noise and delay. At the other extreme (heavy smoothing over many timesteps), representations become stable but fail to faithfully reflect the current state of a rapidly changing stimulus. The paper's simulations show this as a U-shaped quality curve: an intermediate smoothing level achieves the best balance. Crucially for SD-008, the authors demonstrate that excessive smoothing causes upper hierarchy layers to carry a weighted average of several past inputs rather than a faithful snapshot of the current event -- the precise failure mode identified in REE's LatentStack when alpha=0.3. With that low an alpha, z_world is approximately a 3-to-5 timestep weighted average, suppressing the response to any abrupt event (hazard onset, boundary crossing) to roughly 30% of the true signal.

## Mapping to REE

SD-008 fixes LatentStack's EMA alpha for z_world at >= 0.9. The paper supports the direction of this fix: reducing temporal smoothing (raising alpha) increases representational fidelity to the current event at the cost of some noise robustness. In REE's case the noise cost is acceptable because E1's LSTM already provides smoothed slow predictions; z_world's job is to be event-responsive, not smooth. The paper's framework can be read as justifying the design choice to use a high alpha specifically for event-relevant latents (z_world) while potentially retaining lower alpha for genuinely autocorrelated state components like z_self (body position is a genuinely smooth signal). This asymmetric design is implicit in SD-008 and the paper provides a principled rationale for it.

## Limitations and caveats

The paper models hierarchical transmission delay -- a scenario where smoothing at one level propagates errors to the next. REE's EMA is a single-level operation within LatentStack, so the hierarchical transmission argument applies only indirectly. The paper also does not specify a threshold alpha value analogous to SD-008's 0.9; that number comes from REE-specific experimental evidence (EXQ-023, EXQ-040) rather than from this theoretical framework. There is also a modality gap: the paper addresses visual motion processing, while REE's z_world encodes discrete event types in a gridworld. The conceptual transfer is valid but not a precise quantitative derivation.

## Confidence reasoning

The paper provides useful theoretical scaffolding for understanding why alpha matters as a design parameter, and its failure mode analysis (heavy smoothing degrades event responsiveness) directly matches the mechanism that motivated SD-008. Confidence is set at 0.68 rather than higher because the architecture mismatch is real, the specific threshold is not derived from this paper, and the paper's message is somewhat dual-use -- it could also be read as arguing against the high-alpha regime. The mapping fidelity is moderate: the conceptual claim is supported but the quantitative specifics are not.
