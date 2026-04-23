# Summary: Ciocchi et al. (2010) — Encoding of conditioned fear in central amygdala inhibitory circuits

**Source:** Ciocchi S, Herry C, Grenier F, Wolff SBE, Letzkus JJ, Vlachos I, Ehrlich I, Sprengel R, Deisseroth K, Stadler MB, Muller C, Luthi A (2010). *Nature*, 468(7321):277–282. [DOI: 10.1038/nature09559](https://doi.org/10.1038/nature09559)

**Claim tested:** MECH-074c — CeA analogue emits a fast subcortical priming signal (fast_prime) on low-frequency z_harm_a with an overridable decay window.

---

## What the paper does

Ciocchi and colleagues — the Luthi group at the FMI Basel — use in vivo electrophysiology combined with optogenetics to dissect the internal microcircuitry of the central amygdala (CeA) during fear conditioning. The core finding is a functional dissociation within CeA: the lateral subdivision (CeL) is required for fear acquisition (lesion during conditioning abolishes learning), while the medial subdivision (CeM) drives conditioned fear output responses. The CeL-to-CeM pathway is inhibitory (GABA), and cell-type-specific plasticity in this pathway — phasic fear cells increase firing to CS+ while tonic cells decrease — gates whether CeM produces an output and regulates generalisation.

## Key findings relevant to MECH-074c

1. **CeM as the output stage**: CeM neurons project to brainstem/hypothalamus and drive the behavioural fear response. This is the substrate for MECH-074c's fast_prime: the CeM output biases the harm action channel in REE.

2. **CeL as the acquisition and gating layer**: CeL activity is required during conditioning but not at output expression time. This is consistent with MECH-074c's `theta_cea_fast` threshold gating: past conditioning (CeL learning) determines when CeM fires.

3. **Inhibitory disinhibition architecture**: CeL inhibits CeM tonically; fear conditioning shifts CeL to a state that disinhibits CeM during CS presentation. This disinhibition mechanism is rapid — consistent with the fast latency requirement of MECH-074c (1–2 sim steps = ~100–200 ms).

4. **Regulation of generalisation**: CeL phasic/tonic balance also regulates fear generalisation, directly relevant to MECH-074c's selectivity requirement: fast_prime must fire on harm-affective valence, not generic arousal.

## REE translation and mapping

MECH-074c's CeAAnalog emits fast_prime as a scalar pulse biasing the harm channel within 1–2 sim steps. Ciocchi et al. establish the substrate: CeM disinhibition via CeL is the biological implementation of this fast channel. The architecture is distinct from MECH-046's cortical mode-prior write (the slower CeA→cortex pathway). In REE, `theta_cea_fast` maps to the threshold at which CeL disinhibition fires CeM output; the decay window maps to the post-CS inhibitory rebound documented in CeA electrophysiology.

Note: a separate entry for Ciocchi 2010 exists in `targeted_review_sd_035` tagged to SD-035 (the amygdala substrate claim). That entry addresses the substrate instantiation. This entry is specifically about MECH-074c's fast-priming output claim.

## Limitations and caveats

This paper characterises the CeA microcircuit architecture and conditioning-dependent plasticity but does not directly measure the latency of CeM output relative to stimulus onset. The 1–2 sim-step (100–200 ms) latency for fast_prime is from Mendez-Bertolo 2016 (amygdala LFP). Additionally, the paper focuses on fear-conditioned responses (slow CS); whether the disinhibition mechanism can produce fast_prime for unconditioned harm signals (novelty-driven z_harm_a spikes) is an open question.

## Confidence reasoning

Confidence 0.78. Landmark Nature study with direct optogenetic circuit dissection; CeL/CeM architecture is highly replicated. The gap is latency: the 1–2 sim step specification of fast_prime needs Mendez-Bertolo as the latency anchor. This paper provides the substrate and gating logic.
