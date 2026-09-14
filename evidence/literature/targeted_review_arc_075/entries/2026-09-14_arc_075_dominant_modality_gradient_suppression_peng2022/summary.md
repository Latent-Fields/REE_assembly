# Peng, Wei, Deng, Wang & Hu (2022) -- on-the-fly gradient modulation

**What they did.** Peng and colleagues noticed that audio-visual models often beat their single-modality counterparts while still leaving each modality's own representation under-trained, because one modality (sound for wind, vision for drawing) dominates the shared objective. Their fix, OGM-GE, watches the discrepancy between the modalities' contributions and damps the gradient of whichever is ahead, adaptively and throughout training. Suppression on its own risked hurting generalization, so they added a dynamically changing Gaussian noise term. The combination improved several fusion methods.

**Why it matters for ARC-075.** Read alongside Wu et al. (2022), this is a second, methodologically independent demonstration that competitive capture under a shared objective is the default outcome, and that suppressing the leader's update magnitude is what breaks it. At the level of the operator it is nearly MECH-333 verbatim: detect the dominant scoring pathway, reduce its effective update, let the others reach viable weight. Nothing here involves re-ordering data or scheduling phases -- the lever is magnitude.

**The caveat worth keeping.** The authors could not simply suppress the winner; they needed injected noise to avoid a generalization penalty. I read that as a warning for REE: turning F down during the open window may need a paired diversity-injection source, or the agent simply learns less rather than learning more broadly. REE already has candidates for that (babbling, curiosity), but it should be a designed pairing, not an afterthought.

**Limits.** Supervised classification with labels, so "contribution" is well defined; in REE the credit split between F and the diversity heads for a good commitment is much murkier. No window, no release, no test that balance persists -- the closure and post-closure validation halves of ARC-075 are untouched.

**Confidence.** 0.6: good support for the open-window operator, with an explicit cost signature, and no bearing on crystallization.
