# INV-075 HANDOFF Arm -- Targeted Literature Pull (Why Handoffs Fail)

- **Created:** 2026-05-17T18:54:27Z
- **Session:** inv075-314bc-binary-handoff-litpull-2026-05-17T184554Z
- **Sibling of:** `evidence/planning/inv075_signal_register.md` (Part B deliverable; Part A binary resolved in that file's "Binary resolution" section)
- **Scope:** INV-075 consequent arm **(iii) HANDOFF** only. The antecedent and the **(ii) LOCK** arm are already well-covered in the corpus (Pathak ICM, Deidda depolarizing GABA, Huang BDNF, Pizzorusso PNN, Morishita Lynx1, Aton two-stage gate, Kleinman cross-channel predictive) and were **deliberately NOT re-pulled**. This pull targets the under-covered question: *what makes a handoff (transfer of maintenance to a durable non-extinguishing signal) succeed vs. fail after the establishing signal is gone, and specifically why did V3-EXQ-543g's outcome-coupled REINFORCE handoff fail?*
- **Motivating failure:** V3-EXQ-543g attempted a handoff -- couple the gated-policy weighting to episode return so a durable return signal maintains the gating after the bootstrapping (diversity) signal fades. It **FAILED**: ARM_3 (gated + dACC, outcome-coupled) = 0.243, regressing **below** ARM_2 (gated-only, no handoff) = 0.444. The handoff did not merely fail to help -- it actively degraded the already-established gated representation.
- **lit_conf scale:** 0.0-1.0, parallel/decoupled from experimental confidence (per governance: lit and exp evidence are not co-equal; this is a sanity-check + mechanism-harvest signal, not a confidence-blend input).

---

## Convergent verdict (one line)

Biology and ML agree: **a durable maintenance signal maintains an *already-locked* structure; handoff *alone*, onto an unlocked structure, via a *sparse outcome* objective, provably degrades the representation it was meant to preserve.** 543g failed for the textbook reason; a working handoff for the gated policy requires (a) a prior at-least-partial LOCK and (b) a *dense, representation-aligned* maintaining objective -- never sparse episode-return REINFORCE.

---

## Findings

### F1 -- Lock and handoff are JOINTLY required; the structural lock's stabilizing effect itself depends on ongoing drive (and vice versa)

- **Paper:** Faini, Aguirre, Landi, Lamers, Pizzorusso, Ratto, Deleuze, Bacci (2018), "Perineuronal nets control visual input via thalamic recruitment of cortical PV interneurons," *eLife* 7:e41520.
- **lit_conf:** 0.84 (direct, mechanistic, in-vivo causal manipulation of exactly the lock x drive interaction).
- **What it predicts about handoff:** Handoff-alone is **not** the normal biological configuration. PNN (the structural LOCK) and ongoing sensory drive (the durable maintaining/HANDOFF signal) are *co-dependent*: PNN-mediated stabilization of thalamic input onto PV cells is itself **abolished by removing visual drive** (2-3 days monocular deprivation "significantly counteracted" the PNN-removal effect), and removing the PNN resets the circuit toward a juvenile, destabilized state. The mature circuit is held by **lock AND drive together**; neither alone suffices.
- **Implication for 543g / a working handoff:** 543g handed maintenance to a durable signal with **no lock in place** (crystallize_enabled was off in the 543g lineage). The biology predicts exactly this is insufficient: the durable signal maintains a *locked* circuit, it does not protect an unlocked, still-plastic one from being overwritten. Supports 543h pursuing the LOCK first; a handoff, if used, must be lock-assisted.

### F2 -- Closing/locking the critical period is REQUIRED for the established circuit to mature and persist (handoff without lock leaves it immature)

- **Papers:** (a) "Closing the Critical Period Is Required for the Maturation of Binocular Integration in Mouse Primary Visual Cortex," *Front. Cell. Neurosci.* 2021 (PMC8663722). (b) Lensjo et al. 2017, "Removal of Perineuronal Nets Unlocks Juvenile Plasticity Through Network Mechanisms of Decreased Inhibition and Increased Gamma Activity," *J. Neurosci.* 37(5):1269 -- PNN removal resets the network to an immature/juvenile, destabilized state.
- **lit_conf:** 0.80.
- **What it predicts about handoff:** The transition from "established by a transient signal" to "stable mature structure" *requires the lock as a gating step*. Ongoing activity (handoff) without the lock does not consolidate the structure -- it remains in the plastic, overwrite-vulnerable regime.
- **Implication for 543g:** An outcome-coupled handoff applied while the gated heads are still plastic cannot consolidate them; their representation stays overwrite-vulnerable to the dominant F-error / competitive gradient (the INV-074 mechanism that motivated INV-075 in the first place). The lock is the prerequisite, not an alternative, to a durable handoff.

### F3 -- The transient developmental (establishing) signal is *designed* to self-extinguish, and a separate maintenance regime takes over only after maturation -- they are temporally staged, not substitutable

- **Paper:** "Transient downregulation of BDNF is required for GABAergic maturation in rat primary visual cortex," *PMC6355630*; corroborated by the Hensch critical-period-regulation reviews (PNAS 2017 1820836117; Hensch Ann. Rev. Neurosci. 2004) -- experience installs the molecular brake (PNN/Otx2/NARP/BDNF cascade) that then maintains the circuit *non-cell-autonomously*.
- **lit_conf:** 0.72 (supports the staging logic; less direct on the *failure* mode).
- **What it predicts about handoff:** A successful biological handoff is **sequenced**: establishing signal peaks -> drives installation of a *distinct* durable brake -> establishing signal is then withdrawn. The durable maintainer (the brake + tonic drive) is a *different mechanism class* from the establishing signal, and it is put in place **before** the establishing signal fades. A handoff that simply re-points the *same* circuit's update rule at a new (outcome) target, with no distinct durable structure installed first, is not the biological pattern and is predicted to fail.
- **Implication for 543g:** 543g re-used the *same* gated-policy update pathway and coupled it to episode return -- it did not install a distinct durable maintainer before the diversity signal faded. Predicted to fail; matches the result.

### F4 -- Sparse-outcome targets provably collapse an established representation (the precise 543g mechanism)

- **Paper:** Lyle, Rowland, Dabney (2022), "Understanding and Preventing Capacity Loss in Reinforcement Learning," arXiv:2204.09560 (DeepMind / Oxford).
- **lit_conf:** 0.86 (a *theorem*, Corollary 1, plus empirical QR-DQN sparse-reward collapse -- directly on point).
- **What it predicts about handoff:** Training a representation against a **sparse / non-stationary outcome target degrades it**: "capacity loss." Corollary 1 proves that when the return signal is ~0 (sparse reward), "the feature representation converges to the zero vector for every state, **independent of the learning rate**." The proposed fix, InFeR, regularizes features toward their **initialization values** -- i.e. an *anchor / soft-lock toward the pre-handoff representation*.
- **Implication for 543g (THE key finding):** Episode return is a **sparse, delayed, non-stationary** signal. Coupling the gated-policy weighting to it is exactly the Lyle setup. The theory predicts the gated representation collapses toward a degenerate subspace -- which is precisely what ARM_3 (0.243) regressing *below* the no-handoff ARM_2 (0.444) shows. **The handoff did not under-maintain; the sparse outcome objective actively destroyed the established representation.** And InFeR's fix (anchor toward the pre-handoff representation) *is a lock* -- independent ML confirmation that a working handoff needs a lock-like anchor.

### F5 -- Handing a representation to a durable RL objective alone induces dormant-neuron / plasticity loss; pretrained representations degrade under the new objective

- **Papers:** Sokar, Agarwal, Castro, Evci (2023), "The Dormant Neuron Phenomenon in Deep Reinforcement Learning," ICML (PMLR 202) -- pretrained networks degrade under the RL objective; ReDo recycles dormant units. Corroborated by the loss-of-plasticity literature (Dohare et al.; "Maintaining Plasticity via Regenerative Regularization," arXiv:2308.11958).
- **lit_conf:** 0.74.
- **What it predicts about handoff:** Re-pointing an established network at a durable RL objective is **not maintenance-neutral**: it drives units dormant and erodes the established representation unless an explicit preservation mechanism (recycling / regularization toward a reference) is added.
- **Implication for 543g:** Outcome-coupled REINFORCE on the gated heads is the degradation regime, not a benign maintainer. A corrected handoff would need an explicit preservation term (lock-like anchor or unit-recycling), not bare reward-coupling.

### F6 -- Naive supervised<->RL handoff causes catastrophic forgetting; the working fix is to FREEZE the parameters critical to the established skill (a partial lock)

- **Paper:** Yuan, Chen, Yu, Shi, Jin, Lee, Mitra (2025), "Mitigating Forgetting Between Supervised and Reinforcement Learning Yields Stronger Reasoners," arXiv:2510.04454.
- **lit_conf:** 0.70 (LLM-domain, but the handoff-failure structure transfers cleanly).
- **What it predicts about handoff:** A naive objective handoff degrades the prior representation because the new objective's gradient conflicts with the parameters the old skill needs. The empirically working fix is **selective parameter freezing of the established-skill-critical weights** -- i.e. a *targeted partial lock co-located with the handoff*.
- **Implication for 543g:** Confirms (independently of biology and of Lyle) that a working handoff is *handoff + partial lock on the load-bearing weights*, not handoff alone. 543g had no such freeze.

### F7 -- The handoff objective's gradient destructively interferes with the established representation (negative-transfer / gradient-coupling path)

- **Papers:** "Gradient Coupling: The Hidden Barrier to Generalization in Agentic RL," arXiv:2509.23870; Yu et al. 2020, "Gradient Surgery for Multi-Task Learning" (PCGrad), NeurIPS; "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning," NeurIPS 2023.
- **lit_conf:** 0.66 (mechanism-of-interference support; somewhat general).
- **What it predicts about handoff:** When a second objective is added on top of an established representation, conflicting gradients cause **negative transfer** -- the new objective's updates can increase loss / degrade structure on the original. Auxiliary objectives that are *representationally aligned* (classifier-style, disentangling) mitigate this; misaligned sparse ones amplify it.
- **Implication for 543g:** Episode-return REINFORCE is gradient-misaligned with the diversity structure (sparse, credit-assignment-lagged). The interference path explains *how* ARM_3 went below ARM_2: the handoff gradient actively fought the established gated representation.

---

## What a WORKING handoff for the gated policy would need (synthesis)

Convergent across F1-F7, biology and ML agree on three necessary conditions; 543g had **none** of them:

1. **A prior at-least-partial LOCK.** Biology: PNN/closure is a *prerequisite* for the durable signal to maintain (F1, F2). ML: InFeR anchor-to-initialization (F4) and selective freezing of skill-critical params (F6) are the working fixes. => Handoff is *lock-assisted*, never standalone. **Directly endorses 543h's MECH-334 crystallization route.**
2. **A DENSE, representation-aligned maintaining objective -- not sparse outcome return.** Lyle Cor.1 (F4) makes sparse-return maintenance provably collapse-inducing regardless of learning rate; F5/F7 corroborate. A corrected handoff would use a *dense per-step* objective aligned to the structure being preserved (e.g. a Kleinman-style cross-channel predictive auxiliary loss -- already in corpus as the lock/auxiliary anchor -- or an InFeR-style anchor to the pre-fade gated representation), explicitly NOT episode-return REINFORCE.
3. **The durable maintainer installed BEFORE the establishing signal fades, as a distinct mechanism.** F3: biological handoff is temporally staged with a *separate* durable brake installed pre-withdrawal -- not the same update rule re-pointed at a new target (which is exactly what 543g did).

**Why 543g specifically failed (one sentence):** It re-pointed the same gated-policy update at a *sparse, delayed episode-return* signal with *no lock and no distinct durable maintainer*, hitting the Lyle Corollary-1 sparse-target representation-collapse regime plus negative-transfer interference -- so ARM_3 degraded *below* the no-handoff baseline rather than maintaining the gated structure.

---

## Recommendation for V3-EXQ-543h (feeds the active crystallization session)

**Pursue the LOCK (MECH-334 crystallization), not a standalone corrected handoff.** The literature is convergent that handoff-alone is the wrong arm here: it is biologically non-canonical (F1-F3), provably collapse-inducing under sparse outcome targets (F4), and degradation-prone under bare RL re-pointing (F5-F7). If a handoff is to be retained at all, it must be **lock-assisted and dense/representation-aligned** (anchor-to-pre-fade-representation or cross-channel predictive auxiliary), and must **never** be sparse outcome-coupled REINFORCE -- that specific design (543g) is the predicted-failure case, now mechanistically explained.

---

## Method note

PubMed/web/arXiv targeted search, 2026-05-17. Queries simplified and fallen back to web search per CLAUDE.md when broad terms returned review-only hits. Deliberately excluded already-corpus-covered anchors (Pathak, Deidda, Huang, Pizzorusso, Morishita, Aton, Kleinman) to keep this pull strictly on the under-covered handoff-failure question. Confidences are lit_conf (parallel signal), not experimental confidence, and are NOT to be blended into claim overall_conf (per governance feedback_lit_exp_decoupled).
