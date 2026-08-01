# Thought intake: foundational AI paper catalogue as REE formal-ancestor and boundary material

**Date processed:** 2026-08-01
**Source email:** `19f8cd9533884afa`, subject `REE: a group of papers to have detailed discussion about while considering thought intakes`, received 2026-07-23
**Source form:** user-forwarded social-media list, "15 AI Research Papers Every AI Engineer Should Read"
**Document type:** thought intake / formal-ancestor catalogue
**Status:** captured for future discussion; no claim update, no substrate change, no experiment queued

---

## Intake decision

This email should be treated as a catalogue of foundational AI papers that can help REE Assembly keep its formal-ancestor map honest. It should not be treated as direct scientific evidence for any REE claim.

The list is broad ML canon, not a focused hypothesis. Several entries are already represented in REE's existing formal-background layer: transformers and LLMs are covered by the language/LLM mining notes and the anti-import discipline; RAG already has a convergence packet; actor/action learning docs already record non-adoptions of MuZero/Dreamer/Decision-Transformer-like imports; sparse selection and routing motifs already appear in targeted sparse/top-k and policy-decomposition work. The useful output here is therefore a boundary catalogue: what each paper teaches, what REE may mine, and what REE should not import.

---

## Primary sources checked

| # | Paper | Primary source | What it contributes | REE disposition |
|---|---|---|---|---|
| 1 | Vaswani et al. 2017, *Attention Is All You Need* | <https://arxiv.org/abs/1706.03762> | Transformer architecture: attention-centered sequence transduction without recurrence or convolution. | Boundary marker for MECH-007. REE can mine content-addressed selection and sequence-dependency problems, but not collapse precision, urgency, belief exclusivity, and action authority into one attention surface. |
| 2 | Hu et al. 2021, *LoRA: Low-Rank Adaptation of Large Language Models* | <https://arxiv.org/abs/2106.09685> | Freeze a large pretrained model and train low-rank adaptation matrices. | Useful future engineering counsel for adapter-style updates if REE ever has a large frozen substrate, but not evidence for a biological mechanism and not current V3 work. |
| 3 | Lialin et al. 2023, *Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning* | <https://arxiv.org/abs/2303.15647> | Survey and taxonomy of PEFT methods. | Background only. It may help future implementation discipline around small deltas and frozen bases, but it does not justify a REE claim by itself. |
| 4 | Dosovitskiy et al. 2020, *An Image is Worth 16x16 Words* | <https://arxiv.org/abs/2010.11929> | Vision Transformer: image patches as sequence units for transformer-based recognition. | Useful contrast for visual discretisation, but REE's grounding route is through object/action/event substrates, not patch-token sequence modeling. |
| 5 | Kingma and Welling 2013, *Auto-Encoding Variational Bayes* | <https://arxiv.org/abs/1312.6114> | Reparameterized variational inference for continuous latent-variable models. | Formal background for latent modeling. Potentially relevant to future measurement/null models, but not direct support for REE's residue, commitment, or typed-error machinery. |
| 6 | Goodfellow et al. 2014, *Generative Adversarial Networks* | <https://arxiv.org/abs/1406.2661> | Generator/discriminator minimax training. | Mostly boundary material. Adversarial training is not the same object as REE's governance, error typing, or ethical derivation. |
| 7 | Devlin et al. 2018, *BERT* | <https://arxiv.org/abs/1810.04805> | Bidirectional transformer pretraining plus task fine-tuning. | Language-system background only. It reinforces the value of self-supervised pretraining, but REE's self-supervision must stay grounded in E1/E2 prediction error rather than surface token statistics. |
| 8 | Rombach et al. 2021, *High-Resolution Image Synthesis with Latent Diffusion Models* | <https://arxiv.org/abs/2112.10752> | Diffusion in compressed latent space for efficient high-resolution generation. | Useful formal background for latent-space generative compression. No immediate REE claim or implementation follows. |
| 9 | Lewis et al. 2020, *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* | <https://arxiv.org/abs/2005.11401> | Combines parametric generation with non-parametric retrieved memory. | Already has a REE convergence packet (`CPKT-RAG-20260223`). Do not duplicate. Use the existing RAG intake if memory/provenance/updateability becomes live. |
| 10 | Brown et al. 2020, *Language Models are Few-Shot Learners* | <https://arxiv.org/abs/2005.14165> | Scaling language models improves task-agnostic few-shot performance. | Background and external benchmark pressure, not architecture authority. It sharpens the Bitter-Lesson comparison but does not replace REE's grounded-substrate requirements. |
| 11 | Fedus, Zoph, and Shazeer 2021, *Switch Transformers* | <https://arxiv.org/abs/2101.03961> | Sparse mixture-of-experts routing: different parameters selected per input. | Formal cousin to conditional compute and routing. REE can mine sparse-selection measurement ideas, but REE's routing remains typed, biologically constrained, and claim-specific. |
| 12 | Stiennon et al. 2020, *Learning to summarize from human feedback* | <https://arxiv.org/abs/2009.01325> | Reward-model training from human comparisons and RL fine-tuning. | Alignment/process background only. Human preference optimization is not REE ethics; it can shape behavior but cannot substitute for REE's commitment, harm, and coordination constraints. |
| 13 | Touvron et al. 2023, *LLaMA: Open and Efficient Foundation Language Models* | <https://arxiv.org/abs/2302.13971> | Efficient open foundation-model training on public data. | Benchmark and engineering context. It belongs in future formal comparison discussions, not in current REE substrate design. |
| 14 | Su et al. 2021, *RoFormer: Enhanced Transformer with Rotary Position Embedding* | <https://arxiv.org/abs/2104.09864> | Rotary position embedding for sequence position and relative dependency in attention. | Useful sequence-position formalism. REE already has grounded temporal/event structure through event segmentation and theta/trajectory machinery, so RoPE is a contrast source rather than an import target. |
| 15 | Ouyang et al. 2022, *Training language models to follow instructions with human feedback* | <https://arxiv.org/abs/2203.02155> | InstructGPT: supervised demonstrations plus reward modeling and RLHF to follow user intent. | Important alignment-history background. It is not evidence that preference-following is equivalent to REE's safety architecture. |

---

## Comparison against existing REE Assembly knowledge

### 1. Transformer and LLM papers are already governed by anti-import discipline

`evidence/planning/language_system_llm_mining_2026-06-04.md` and `thought_intake_2026-06-05_grammar_llms_v5_primitive_mining.md` already make the central move: LLMs can be mined for discretisation, vocabulary, sequence, and self-supervision lessons, but they are not the architecture to import. REE's sequence substrate remains grounded in hippocampal/event/action machinery, not a parallel transformer stack.

This paper list supports that stance. It adds no reason to change it.

### 2. Attention is a contrast case, not a replacement for MECH-007

`docs/architecture/why_attention_must_be_fragmented.md` already records the relevant distinction. "Attention" in REE is not one resource. Precision, commitment pressure, and exclusivity/collapse answer different control questions and must not write to the same register. The transformer paper is therefore a formal contrast: it shows the power of attention-like content addressing for sequence work, while REE's claim is that cognitive-agency architecture requires typed authority and fragmented control.

### 3. RAG is already in the convergence pipeline

The RAG paper should route through `evidence/planning/convergence_packets/inbox/2026-02-23_cpkt_rag_20260223.json`, not through a second intake. That packet already treats RAG as memory/tooling/control-plane material and recommends deferral pending governance review.

### 4. Scaling, PEFT, and adapters are engineering counsel

LoRA, PEFT, GPT-3, LLaMA, BERT, InstructGPT, and the RLHF summarization paper are most useful as engineering and evaluation background. They may help REE Assembly ask sharper questions about frozen substrates, small adapter deltas, externalized memory, and human-feedback training. They do not create biology-grounded mechanism evidence and should not be used to raise confidence in REE claims without a specific, later lit-pull or experiment.

### 5. Latent generative models are formal background, not direct evidence

VAE, GAN, and latent diffusion papers are relevant to latent-variable modeling, generative compression, and representation learning. They are not direct analogues of REE's distinctive elements: residue fields, typed commit boundaries, incommensurable error channels, and axiomatic ethics. They can provide measurement vocabulary or null models later, but not claim support now.

---

## What REE may mine from the list

- **Content-addressed selection:** attention and retrieval mechanisms show how stored items can be selected by content, but REE must keep typed authority.
- **Sequence-position measurement:** RoPE and transformer sequence work offer formal tools for long-range dependency and position sensitivity, but REE's event/theta structure remains the grounding layer.
- **Sparse routing:** Switch/MoE work is a useful formal cousin for conditional compute, routing load, and expert utilization metrics.
- **Adapter discipline:** LoRA/PEFT are useful for future frozen-base-plus-small-delta engineering, if REE ever has a substrate large enough for that pattern to matter.
- **Latent-space compression:** VAE and latent diffusion can inform null models for compressed latent representation, but only after a REE-specific attachment point is named.
- **External memory/provenance:** RAG remains relevant to updateable memory and source provenance; use the existing convergence packet.
- **Human-feedback alignment history:** RLHF papers are important background for comparison, but preference optimization is not REE's ethics or harm architecture.

---

## What REE should not do

- Do not create 15 separate literature records from this email. The email is a catalogue prompt, not 15 targeted claim-evidence pulls.
- Do not import transformer architecture into V3.
- Do not treat AI benchmark success as biological support for a REE mechanism.
- Do not treat RLHF or instruction-following as equivalent to REE alignment.
- Do not duplicate the existing RAG convergence intake.
- Do not edit `claims.yaml` from this note. A claim-level update would require a focused source-to-claim review, not a broad paper list.

---

## Follow-on assessment

No immediate follow-on task is warranted.

If a future formal-ancestor row, language-system design, sparse-routing mechanism, or memory/provenance mechanism becomes active, use this catalogue as a pointer list and run a focused per-row lit-pull at that time. Until then, the correct state is captured-as-background.
