# Hippocampal Translation Maps — Literature Tranche 2: CA1 Transformation Mechanics

**Date:** 2026-09-09  
**Status:** active targeted literature synthesis; first pass landed; no claim promotion and no experiment-queue mutation  
**Parent:** `evidence/planning/hippocampal_translation_maps_literature_tranche_1.md`  
**Question:** does CA1 experimentally transform CA3-separated representations into a more entorhinal/cortical-readable code, or is the familiar “CA1 decoder/translator” account mainly a theoretical interpretation inherited from Complementary Learning Systems and comparator models?

---

## 1. First-pass verdict

The answer is already more specific than “yes” or “no”.

1. **The classical CA1-as-decoder claim is genuinely theoretical in origin.** McClelland & Goddard (1996) explicitly proposed an invertible hippocampal memory system in which dentate/CA3 support separated storage and CA1 helps decode retrieved CA3 representations so that an entorhinal/cortical pattern can be reinstated. This is a computational architecture, not direct physiological proof of a CA3→CA1→EC translation operation.
2. **Modern experiments now show a real CA3→CA1 representational transformation.** Maimon et al. (Nature, 2026) found ultrasparse predominantly single-field CA3 coding but dense multifield CA1 coding in very large naturalistic environments. The authors explicitly describe a CA3→CA1 sparse-to-dense coding transformation and show in a model that sparse input can accelerate learning of dense CA1 maps.
3. **That 2026 result does not establish the classical decoder claim.** The experiment demonstrates that the code changes across the CA3→CA1 boundary. It does not show that CA1 reconstructs the original entorhinal/cortical representation, nor that the output is specifically tailored to an EC receiver.
4. **CA1 appears to integrate multiple representational sources rather than merely invert CA3.** CA1 receives both CA3/Schaffer-collateral and entorhinal layer-III/perforant-path input. 2025–2026 experiments show that the balance of these inputs shapes reference frames, learning and stabilization.
5. **Comparator/mismatch accounts remain a serious rival.** CA1 is anatomically well placed to compare retrieved/predictive CA3 input with current entorhinal input, and human/animal evidence supports mismatch signals. This computation is related to translation but not equivalent to it.

So the currently defensible formulation is:

```text
CA3 separated / sparse retrieval or predictive structure
              +
entorhinal/current-context input
              ↓
CA1 integration / transformation / comparison
              ↓
dense, context-sensitive, output-facing representation
```

rather than:

```text
CA3 code → CA1 simply inverts it → original cortical code
```

---

## 2. Historical source of the decoder idea

### McClelland & Goddard 1996 — Complementary Learning Systems decoder

**Source:** J. L. McClelland & N. H. Goddard. *Considerations arising from a complementary learning systems perspective on hippocampus and neocortex.* Hippocampus 6(6):654–665 (1996). PMID 9034852; DOI `10.1002/(SICI)1098-1063(1996)6:6<654::AID-HIPO8>3.0.CO;2-G`.

The model divides the hippocampal memory system into:

- an entorhinal/cortical encoder;
- a separation/storage/retrieval system involving dentate gyrus and CA3;
- a decoding system intended to let a retrieved CA3 code reinstate an entorhinal pattern.

This is the historical basis for later descriptions of CA1 as a “decoder”. The important epistemic point is that the **need for a translation follows from the assumed representational mismatch in the model**. It is not itself an experimental observation.

### Schapiro et al. 2017 — two hippocampal learning regimes

**Source:** Anna C. Schapiro, Nicholas B. Turk-Browne, Matthew M. Botvinick & Kenneth A. Norman. *Complementary learning systems within the hippocampus: a neural network modelling approach to reconciling episodic memory with statistical learning.* Phil. Trans. R. Soc. B 372:20160049 (2017). DOI `10.1098/rstb.2016.0049`.

Their model separates:

- the **trisynaptic pathway** (EC→DG→CA3→CA1), which favours separated episodic representations;
- the **monosynaptic pathway** (EC→CA1), which learns overlapping/statistical structure.

This makes CA1 a convergence point where separated episodic input and overlapping entorhinal/statistical input can coexist. Again, this is important computational support for the *problem* of translation/integration, not direct evidence that CA1 performs an explicit inverse map.

---

## 3. The strongest new empirical anchor: CA3→CA1 sparse-to-dense transformation

### Maimon et al. 2026 — Nature

**Source:** Shir R. Maimon et al. *Sparse-to-dense coding transformation between hippocampal areas CA3 and CA1.* Nature 655:1242–1251 (2026). DOI `10.1038/s41586-026-10537-0`.

This is unusually relevant because it directly observes different coding regimes at consecutive stages of the hippocampal circuit in the same large-scale navigation problem.

In very long flight tunnels:

- CA3 place cells were predominantly ultrasparse/single-field;
- CA1 place cells were much denser and often multifield;
- the authors explicitly identify a **CA3-to-CA1 coding transformation**;
- their neural-network model shows that sparse CA3 inputs can support much faster learning of dense CA1 target maps than dense CA3 inputs;
- context/trajectory-history signals were more robust in CA1 than CA3 in a multicompartment environment.

### Why this matters for the translation programme

This is no longer merely an analogy that “different hippocampal stages probably use different codes”. A real transformation across the CA3→CA1 boundary is empirically visible.

But the strongest safe statement is:

> **CA1 reformats CA3-linked spatial information into a different, denser, context-sensitive code.**

The paper does **not** establish:

- that the dense CA1 representation is the same representation used by entorhinal cortex;
- that CA1 reconstructs a pre-existing cortical pattern;
- that the transformation is receiver-specific;
- that the transformation is necessary for cortical reinstatement;
- that the observed sparse→dense change generalizes from large-scale spatial coding to arbitrary episodic/semantic latent translation.

The paper's learning model is deliberately simplified and treats EC/CA2 inputs as additional non-plastic inputs in its main mechanistic analysis. Thus it supports a CA3→CA1 transformation but not the full CA3+EC integration story by itself.

---

## 4. CA3 influence on CA1 is causal and changes over learning

### Jiang et al. 2026 — Nature Communications

**Source:** Anqi Jiang et al. *Distinct CA3 inputs differentially shape the learning-dependent evolution of right CA1 spatial maps.* Nature Communications 17:5682 (2026). DOI `10.1038/s41467-026-72275-1`.

Two-photon CA1 imaging plus selective optogenetic inhibition showed that left- and right-origin CA3 inputs make different contributions over learning:

- early novel-environment learning: right CA3 input had stronger influence on refinement of right-CA1 spatial coding;
- later/stable phase: left CA3 input became more important for maintaining the stabilized map;
- CA3 axonal activity in CA1 showed a corresponding temporal redistribution.

**Programme consequence:** the CA3→CA1 interface is not a fixed static transform. Which upstream stream carries control changes over learning state. This is relevant to receiver/context-dependent translation, but the conditioning variable here may be developmental/learning phase rather than receiver state per se.

### 2026 optogenetic CA3 stimulation

A separate 2026 study, *CA3 transiently modulates spatial representation in CA1* (Progress in Neurobiology 263:102935), combined CA3 stimulation with CA1 imaging and found that stimulation could induce new CA1 place cells and shift existing CA1 fields, with effects largely disappearing by the next day.

**Negative boundary:** this shows causal influence and remapping, not a stable learned translation map. It is equally compatible with CA3 acting as a plasticity-driving input to a representation whose final form is jointly determined elsewhere.

---

## 5. Direct entorhinal input means CA1 is a convergence/comparison surface

### Huang et al. 2026 — coordinated CA3 and medial-entorhinal afferents

**Source:** Fengwen Huang et al. *The perforant pathway and CA3-Schaffer collateral afferents coordinate to regulate spatial learning.* Communications Biology 9:364 (2026). DOI `10.1038/s42003-026-09577-z`.

Dual-light stimulation of CA3→CA1 and MEC→CA1 afferents produced robust heterosynaptic LTP in dorsal CA1. The result provides circuit-level support that CA1 plasticity depends on coordinated information from both pathways rather than being only a feed-forward CA3 decoder.

### Deep/superficial CA1 subcircuits

Fernández-Ruiz et al. (2021) showed that superficial CA1 cells were more strongly associated with CA3-driven rate coding, while deep CA1 cells were more strongly influenced by entorhinal input and phase coding. Environmental cue availability shifted the balance between these regimes.

**Programme consequence:** “CA1 representation” may itself be too coarse a unit. Translation/integration may be implemented through **interleaved CA1 subcircuits with different input mixtures and output roles**.

---

## 6. CA1 can switch reference frames under learning

### Qian, Li & Magee 2025 — Nature Neuroscience

**Source:** Fish Kunxun Qian, Yiding Li & Jeffrey C. Magee. *Mechanisms of experience-dependent place-cell referencing in hippocampal area CA1.* Nature Neuroscience 28:1486–1496 (2025). DOI `10.1038/s41593-025-01930-5`; PMID 40169932.

In a familiar environment, CA1 contained both space-referenced and goal-referenced place cells. In a novel environment, the population became predominantly goal-referenced because many cells switched reference frame. Intracellular recordings showed that individual CA1 cells simultaneously received space- and goal-referenced synaptic inputs, and the ratio of those inputs related to the expressed reference frame; behavioural-timescale synaptic plasticity shaped the switch.

This is especially relevant to REE's shared-reference-frame thought:

> the same downstream population can receive multiple candidate relational frames and learn which frame governs the expressed representation.

That is closer to **reference-frame selection/integration** than to literal decoding.

---

## 7. Comparator/mismatch is a genuine rival computation

CA1 receives retrieved/predictive information from CA3 and current sensory/contextual input from entorhinal cortex, which motivated long-standing comparator accounts.

Human high-resolution fMRI work has found CA1 activity associated with associative mismatches, while DG/CA2/3 tracks associative retrieval success. This is compatible with CA1 comparing expected/retrieved structure against current input.

However, the comparator story should not be promoted to the exclusive CA1 function:

- some lesion/pathway evidence suggests mismatch detection is distributed across DG/CA3 as well as CA1;
- disrupting either CA3 or EC input to CA1 does not phenocopy complete hippocampal loss;
- modern CA1 data show coding transformation, reference-frame switching and output routing beyond a simple scalar mismatch signal.

Thus **comparison may be one operation inside the transformation surface**, not the whole answer.

---

## 8. A sharper computational decomposition

The literature now suggests separating at least four computations that older “CA1 translator” language tends to collapse:

1. **Reformatting** — sparse/separated CA3 code becomes a denser CA1 code.
2. **Integration** — CA1 combines CA3-linked retrieved/predictive input with direct entorhinal/current-context input.
3. **Reference-frame arbitration** — experience/plasticity determines which relational frame dominates the expressed CA1 representation.
4. **Comparison/error** — disagreement between retrieved/predicted and current input can be signalled.

A fifth question remains open:

5. **Receiver-specific decoding/reinstatement** — does the resulting CA1 output actively reconstruct a representation tailored to an entorhinal/cortical consumer?

The first four now have meaningful biological support. The fifth — closest to the original McClelland/Goddard “decoder” — remains much less directly demonstrated.

---

## 9. REE implications

This is highly relevant to the current `z_world` / consumer problem but should not be copied literally.

The CA1 analogy suggests that a useful bridge need not be:

```text
z_world → one universal decoder → all consumers
```

A more biologically disciplined family is:

```text
source representation
    + consumer/current-context input
    + reference-frame / learning-state gate
            ↓
small transformed read-surface
            ↓
consumer-specific use
```

and the transformation may be allowed to change during development before later stabilizing/sparsifying.

This gives three specific REE discriminators after the over-capacity decoder result:

- **pure source decoder:** `T(z_world)`;
- **source + consumer/context bridge:** `T(z_world, consumer_state/context)` with receiver-permutation control;
- **reference-frame bridge:** expose the same source content under an explicitly changed relational frame while holding information content constant.

If the second/third rescue held-out behaviour when the first does not, that would look much closer to the biological CA1 story than simply adding decoder depth.

---

## 10. Claim-overlap / minting decision after first pass

**No new claim is minted yet.**

Reasons:

- CA3→CA1 sparse-to-dense transformation is strong new literature evidence, but it bears primarily on the existing mutual-legibility/TCRT/reference-frame programme rather than establishing a new REE mechanism by itself;
- the exact CA1-as-decoder mechanism remains underdetermined;
- the unprocessed shared-reference-frame thought remains the correct place to decide whether a new distributed reference-frame mediation claim is warranted;
- any new claim should distinguish `reformatting`, `integration`, `reference-frame arbitration`, and `receiver-specific decoding` rather than minting “CA1 translation” as one bundle.

Accordingly this first pass generates **no new literature debt**.

---

## 11. Next dig inside tranche 2

The next narrow questions are:

1. **Output-specific CA1 channels:** do CA1 populations projecting to entorhinal, retrosplenial, subiculum, prefrontal or other targets carry measurably different relational codes?
2. **CA1→EC reinstatement:** is there causal evidence that hippocampal output reconstructs a specific entorhinal/cortical pattern rather than merely triggering cortical pattern completion?
3. **Deep versus superficial CA1:** can input/output sublayer anatomy explain partner-specific transforms without a generic translator?
4. **Temporal multiplexing:** do theta phase, gamma source and sharp-wave-ripple phase gate which representation/read-surface CA1 exposes?
5. **Development/pruning:** does the CA3→CA1 mapping begin broad/overcomplete and become sparse or partner-specific with learning?

These are now concrete enough for a second targeted pull rather than broad hippocampal searching.
