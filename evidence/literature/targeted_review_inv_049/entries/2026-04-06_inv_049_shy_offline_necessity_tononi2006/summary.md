# Tononi & Cirelli (2006) -- Synaptic Homeostasis and the Offline Necessity Argument

**Claim tested:** INV-049 -- offline update phases are a general computational necessity for model-building agents.

## A Second Route to the Same Conclusion

McClelland et al. 1995 established that sequential online learning causes catastrophic interference -- new updates obliterate old representations. Tononi and Cirelli 2006 provide a second, independent reason why online-only operation fails: even if you could solve the interference problem, continuous waking learning would exhaust the system's representational capacity. Synaptic weights are not infinite; potentiation is metabolically costly; and signal-to-noise ratio degrades as more and more connections approach saturation. Sleep, on this view, is the price paid for having plastic synapses at all.

## The Synaptic Homeostasis Argument

The synaptic homeostasis hypothesis (SHY) proposes that waking experience drives net potentiation of synapses across the cortex. This is not selective strengthening of a few connections -- it is a broad upward drift in mean synaptic weight. Left unchecked, this drift would make further learning impossible (saturated synapses cannot be further potentiated) and metabolically catastrophic (maintaining high-weight synapses is energetically expensive). Slow-wave sleep, via cortical slow oscillations and hippocampal sharp-wave ripples, provides a mechanism for global synaptic downscaling: weights are reduced proportionally, preserving relative differences (i.e., learned structure) while restoring the system to a sustainable operating point.

## Why This Supports INV-049's Generality Claim

The capacity saturation argument is substrate-independent in a way that complements the CLS interference argument. You do not need to be a biological brain to face this problem. Any learning system that accumulates updates in shared parameters faces some version of weight saturation or bias drift over sufficiently long continuous operation. The offline phase is the mechanism by which the system renormalises -- restoring its dynamic range for the next waking cycle. For REE specifically, this maps onto the need for periods during which action is suspended and the world model (E1/E2) is reorganised not merely by replaying episodes but by normalising the parameter landscape relative to accumulated prediction error.

## Honest Caveats

The mapping from SHY to INV-049 requires real abstraction. SHY is a theory about specific biological mechanisms -- synaptic weight magnitudes, UP and DOWN states in cortical slow oscillations, the specific role of sharp-wave ripples. The claim that 'parameter saturation' in an artificial system like REE is analogous to 'synaptic saturation' in biology is plausible but not demonstrated. SHY is also contested within neuroscience: the completeness of global synaptic downscaling, the relative contributions of NREM and REM sleep, and whether the primary function of sleep is really homeostatic renormalisation or something more like active consolidation (the Rasch-Born view) -- these debates are live. None of this undermines the basic INV-049 necessity argument, but it means SHY's specific mechanism should not be taken as established fact at the detailed level. At the level of 'offline phases are necessary,' the convergence with CLS is strong.
