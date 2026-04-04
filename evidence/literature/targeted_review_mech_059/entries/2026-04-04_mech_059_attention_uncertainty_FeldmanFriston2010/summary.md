# Feldman & Friston (2010) — Attention, Uncertainty, and Free-Energy

**Citation:** Feldman H, Friston KJ. Attention, Uncertainty, and Free-Energy. *Front Hum Neurosci*. 2010;4:215. DOI: 10.3389/fnhum.2010.00215. PMID: 21160551.

**Relevance to MECH-059:** Direct. The closest existing statement in the predictive coding literature of the structural separation MECH-059 requires.

---

Feldman and Friston make an argument that, once you see it, is hard to unsee. The brain is not just trying to predict sensory signals — it is simultaneously trying to assess how reliable those signals are. These are not the same problem. You can have a large prediction error because the world did something unexpected (high error, high reliability), or because your sensors are noisy (high error, low reliability), or because you are genuinely uncertain about model parameters (moderate error, uncertain reliability). Treating precision as a direct function of error magnitude collapses these distinct epistemic situations into a single undifferentiated signal.

The paper's concrete proposal is that these two estimation problems are implemented in different neural substrates. Prediction error is encoded in the firing rate of error units — primarily superficial pyramidal cells. Precision is encoded not in firing rate but in the post-synaptic gain applied to those error units, controlled by inhibitory interneurons and modulated by neuromodulators including acetylcholine. This is a hardware-level separation: the error signal and the confidence in that error signal travel through different physical channels and are modified by different cell types.

The paper goes further in arguing that this is not merely an implementation convenience but a logical necessity. When precision itself depends on the state of the world — that is, when environmental reliability is context-sensitive — the system must infer precision from observations using its own generative model, in parallel with inferring world states. You cannot bootstrap precision from error magnitude without circularity, because the error magnitude is itself dependent on the precision estimate. The two inferences must proceed in tandem, using shared but distinct information.

For REE, this translates directly to MECH-059. The confidence channel (tracking uncertainty in z_world or z_harm model parameters) must not be derived from prediction error magnitude, because prediction error magnitude is a joint function of world state and model confidence — it does not uniquely determine either. A system that derives its confidence channel from its residual error has no independent confidence signal at all; it has just relabelled the error with a delay. The MECH-059 experimental result (|corr(score_dispersion, PE)| = 0.067) is exactly what Feldman and Friston's framework predicts should be true of a correctly implemented system.
