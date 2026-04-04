# Frank 2005 -- Dynamic Dopamine Modulation in the BG: MECH-106 Mapping

**Source:** Frank, M.J. (2005). Dynamic dopamine modulation in the basal ganglia: a neurocomputational account of cognitive deficits in medicated and nonmedicated Parkinsonism. *Journal of Cognitive Neuroscience*, 17(1), 51-72. DOI: [10.1162/0898929052880093](https://doi.org/10.1162/0898929052880093)

---

## What the Paper Does

Frank presents a neural network model of the basal ganglia in which dopamine dynamically modulates the balance between direct and indirect striatal pathways. The core architecture: the direct pathway (D1-expressing MSNs) facilitates cortically specified actions, while the indirect pathway (D2-expressing MSNs) suppresses them. What the model adds beyond a static anatomy is a learning rule tied to phasic DA. Positive feedback produces phasic DA bursts, which activate D1 receptors and potentiate direct-pathway synapses -- lowering the threshold for future facilitation of the same action class. Negative feedback produces phasic DA dips, which relieve the tonic inhibition on D2 MSNs and strengthen indirect-pathway suppression -- raising the threshold against the same action class. The model is validated against probabilistic classification and reversal learning deficits in Parkinson's patients both on and off dopaminergic medication, explaining paradoxical cases where medication improves some deficits while worsening others (the DA overdose account).

## Key Findings

The critical finding for MECH-106 is the explicit demonstration of asymmetry. The direct and indirect pathways are not mirror images of a single threshold -- they are separate learning channels, each reinforced by a different sign of prediction error, and they modulate the system's response propensity in opposite directions. DA bursts lower the effective threshold for Go; DA dips raise the effective threshold against Go (which is functionally equivalent to raising the commitment threshold from the other side). This asymmetry is not incidental but the paper's central design choice: it is what explains why dopamine depletion in Parkinson's produces differential deficits in reward- versus punishment-driven learning, and why medication overdose (elevating DA where it was not needed) produces the opposite pattern.

The model also introduces the concept of dynamic range: what matters is not the absolute DA level but the range over which phasic changes can occur. Parkinson patients have compressed dynamic range, meaning both the D1 potentiation signal and the D2 relief signal are attenuated -- producing both reduced approach facilitation and reduced avoidance strengthening. This is mechanistically important for REE because it implies the commitment threshold asymmetry depends on the integrity of phasic signalling, not just tonic DA tone.

## REE Mapping to MECH-106

MECH-106 claims that the commitment threshold in REE's control plane is asymmetrically modulated by outcome valence: positive outcomes lower it (via D1 potentiation), negative outcomes raise it (via D2 pathway activation). Frank 2005 provides the biological substrate for exactly this claim. The direct pathway D1 potentiation mechanism is the cellular basis for why the commit threshold falls after success. The D2-mediated indirect pathway strengthening after DA dips is the basis for why the threshold rises after harm contact or large prediction error.

The REE translation requires one extension that the paper does not directly address: the commit threshold in REE is for entering and exiting a sustained commitment mode, not a single-trial discrete selection event. Frank's model handles phasic, trial-level modulation. Whether D1 potentiation produces hysteresis lasting across multiple steps -- keeping the threshold lowered for an extended commitment period -- depends on the timescale of D1 synaptic changes, which the paper treats as session-level learning rather than within-episode dynamics. This is the main mapping caveat, and it is non-trivial: MECH-106 requires a within-episode threshold change, not just a between-trial learning effect.

## Limitations and Confidence Reasoning

This paper is unambiguously the theoretical foundation for MECH-106's biological claim. The mechanism is explicit, mathematically implemented, and empirically validated in a human patient population. The confidence reduction comes entirely from the scope mismatch: Frank models discrete action selection thresholds, and REE needs commitment-mode dynamics that persist over multi-step trajectories. The extension is well-motivated -- there is no reason in principle why D1 potentiation would be confined to single trials -- but it has not been directly tested in the source. A more honest framing of MECH-106 is that Frank 2005 provides strong evidence for the cellular mechanism underlying asymmetric threshold modulation, while leaving the commitment-mode persistence component as a theoretical extrapolation requiring further empirical support. Confidence: 0.82.

*Based on article retrieved from PubMed (PMID: 15701239, DOI: [10.1162/0898929052880093](https://doi.org/10.1162/0898929052880093)).*
