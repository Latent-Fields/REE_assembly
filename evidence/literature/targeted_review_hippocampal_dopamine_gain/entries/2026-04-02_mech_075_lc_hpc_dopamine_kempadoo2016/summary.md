# Kempadoo et al. (2016) — LC, Not VTA, Drives Dorsal Hippocampal Dopamine: Reframing MECH-075

**Claims tested:** MECH-075
**Evidence direction:** mixed | **Confidence:** 0.71

---

## What the paper did

Kempadoo, Mosharov, Choi, Sulzer, and Kandel (Eric Kandel's Columbia lab) used optogenetic and neurochemical tools to systematically map the source of dopamine release in the dorsal hippocampus of mice. The finding was unexpected and has since been replicated: VTA dopaminergic axons are anatomically sparse in dorsal hippocampus. The primary source of dopamine in dorsal hippocampus is locus coeruleus (LC) neurons, which co-release dopamine alongside norepinephrine from the same terminals. Photostimulation of LC axons in dorsal hippocampus produced detectable dopamine release (measured by HPLC), and this LC-stimulated dopamine release in dorsal HPC enhanced spatial learning and memory in novel object location and recognition tasks.

## Key findings for MECH-075 — and the reframing problem

MECH-075 claims that BG dopaminergic signals (via VTA) set the gain/threshold on hippocampal attractor basins, modulating the probability of trajectory retrieval. Kempadoo et al. establish that for the *dorsal* hippocampus — which is the primary substrate for spatial navigation, cognitive mapping, and the planning circuitry that MECH-075 is supposed to modulate — the catecholaminergic gain input comes primarily from LC, not VTA.

This is not a refutation of dopaminergic gain modulation in hippocampus; it is a reframing of its anatomy. The key implications for REE:

**What survives:** Dopaminergic/catecholaminergic gain modulation of hippocampal memory encoding and retrieval is real. LC-derived dopamine in dorsal HPC enhances spatial memory — this is consistent with MECH-075's claim that catecholaminergic signals modulate the strength of hippocampal encoding and thus the depth of attractor basins in the viability map.

**What requires revision:** MECH-075 frames this as BG/VTA-mediated. For the dorsal HPC planning/navigation circuit, the gain signal comes from LC, which is an arousal/novelty signal (not a BG-mediated reinforcement signal). LC responds to novelty, prediction errors, and changes in arousal — not to reward-specific signals in the BG sense. This means that the dorsal HPC attractor gain control is tied to arousal/novelty rather than specifically to BG value signals.

**The ventral HPC story is different:** VTA dopamine does reach ventral hippocampus (Lisman & Grace 2005, already in this evidence set). The VTA-mediated novelty loop (HPC novelty detection → VTA dopamine release → ventral HPC LTP) is a real circuit, but it primarily affects ventral HPC encoding, not dorsal HPC spatial/planning circuitry. For REE's viability map, which is grounded in the dorsal HPC spatial substrate, the relevant modulator is LC.

## The revised MECH-075 architecture

A revised account distinguishes:
- **Dorsal HPC attractor gain:** LC catecholaminergic signal, responds to novelty and arousal. Sets encoding depth for new trajectory segments encountered during exploration. High arousal = deep encoding = strong attractor basin.
- **Ventral HPC attractor gain:** VTA dopaminergic signal, responds to prediction error and reward. Sets encoding depth for value-relevant events. High RPE = deep encoding = strong affective attractor basin.

Both are hippocampal gain modulation, but via different sources with different functional triggers. MECH-075's claim survives in principle but requires anatomical subdivision by hippocampal axis. Whether this distinction matters for REE's current implementation depends on whether dorsal and ventral HPC attractor basins are treated as the same substrate.

## Limitations

Mouse study. The finding has been extended in human neuroimaging where LC volume and activity predict hippocampal-dependent memory, consistent with Kempadoo et al. The LC → dorsal HPC dopamine finding has been replicated (see subsequent PNAS papers). The attractor-depth mechanism is inferred from behavioural memory enhancement, not from direct measurement of CA3/CA1 attractor dynamics. The paper does not test whether LC stimulation modulates retrieval (as opposed to encoding) — MECH-075's "retrieval bias" function requires separate grounding.
