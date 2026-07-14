# Adaptive gain and the role of the locus coeruleus-norepinephrine system in optimal performance

**Class surveyed:** EXPLORE-EXPLOIT MODE | **Evidence direction:** supports | **Confidence:** 0.68

**Source:** Gary Aston-Jones, Jonathan D. Cohen (2005). *Adaptive gain and the role of the locus coeruleus-norepinephrine system in optimal performance.* Journal of Comparative Neurology 493(1):99-110 DOI: 10.1002/cne.20723

Aston-Jones & Cohen's adaptive-gain theory describes the locus-coeruleus-norepinephrine system as occupying two dissociable modes: a *phasic* mode that fires to task-relevant outcomes and locks in exploitation of the current task, and a *tonic* mode of elevated baseline firing that disengages and drives search for alternatives. Anterior cingulate and orbitofrontal cortex, monitoring task utility, set which mode is active -- an explicit top-down mode/gating signal, not a per-outcome scalar reward.

The distinctive capability for REE is *bidirectional arbitration*. A novelty bonus can only push exploration up; adaptive gain can both raise exploration (tonic) when utility wanes and switch it off (phasic) to sharpen exploitation once utility is found. That 'switch to exploit and lock it in' half is exactly the floor->competent transition, and it is the half a positive-only novelty addend structurally cannot produce.

Buildability is high: a scalar gain/temperature variable m that multiplies policy logits (high tonic gain -> flatter/noisier policy = explore; phasic -> sharper = exploit), driven by a running utility/advantage estimate the critic already produces. It composes with -- rather than duplicates -- an RND bonus: the bonus reshapes reward, the mode modulates the policy's stochasticity/commitment and can anneal exploration into competent exploitation.

Confidence 0.68: a strong, canonical mechanistic account, but it is primate neurophysiology + modelling, not a demonstration of closing an RL competence gap -- the transfer is by analogy. Its value is that the 'consolidate into exploitation' capability is a real, cheap, composable addition that directly tests whether arbitrated commitment (not more novelty) is what REE's gap needs.
