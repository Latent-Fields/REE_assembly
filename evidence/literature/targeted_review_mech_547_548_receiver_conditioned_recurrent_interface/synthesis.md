# Targeted review — MECH-547 receiver-conditioned translation and MECH-548 recurrent interface stability

**Date:** 2026-09-09  
**Status:** literature pull landed; literature-only, no claim promotion/demotion and no experiment-queue mutation  
**Trigger:** MECH-547 and MECH-548 were registered on 2026-09-08 after the parent mutual-legibility literature pull and therefore owed claim-specific literature review.  
**Parent research tranche:** `evidence/planning/hippocampal_translation_maps_literature_tranche_1.md`

## Sources banked

### MECH-547

1. Hahamy, Dubossarsky & Behrens 2023, Nature Neuroscience — context-specific past-event reactivation at event boundaries. **Supports weaker analogue.**
2. Teyler & Rudy 2007, Hippocampus — hippocampal indexing and cue-triggered cortical reinstatement. **Mixed / strong rival mechanism.**
3. Staresina & Wimber 2019, Trends in Cognitive Sciences — hippocampal pattern completion followed by cortical reinstatement. **Supports weaker analogue.**
4. Song et al. 2026, Nature Communications — causally relevant past-event reinstatement precedes updating of the current situational representation. **Supports relational/context-sensitive access.**

### MECH-548

5. Gonzalez et al. 2026, Nature — partner-specific hippocampal/retrosplenial communication subspaces show experience- and sleep-dependent plasticity/stability. **Mixed / adjacent support.**
6. Fenton 2024, Nature Reviews Neuroscience — apparent place-field remapping can coexist with more stable co-firing/manifold organisation registered to different environments. **Mixed / rival framing for what counts as drift.**
7. Madar et al. 2025, Nature Neuroscience — behavioural-timescale synaptic plasticity continually drives population-level hippocampal representational shifting. **Supports the non-stationary-endpoint premise only.**

---

## MECH-547 verdict

### What the literature supports

There is substantial converging evidence that hippocampal/medial-temporal retrieval is **conditioned by the current cue, context, event boundary and relational relevance** rather than exposing all stored content through one fixed readout.

The biologically safe formulation is:

> current state/query helps determine which already-stored relational or episodic information is reinstated and made available downstream.

This is genuinely aligned with the motivation for MECH-547.

### What it does not yet support

None of the reviewed neuroscience sources demonstrates the registered artificial mechanism:

```text
T(sender state, receiver state) > T(sender state)
```

with receiver-state permutation destroying the additional gain.

The literature is equally compatible with at least two simpler explanations:

1. **hippocampal indexing / pattern completion** chooses the correct stored ensemble;
2. a **sender-side context-sensitive retrieval operation** selects the relevant content before the receiver sees it.

Therefore the exact MECH-547 mechanism remains **candidate**, and its decisive evidence must still come from the registered matched-capacity `T(A,B)` versus `T(A)` and receiver-permutation assay.

### Literature direction

**Overall: modestly supportive of the construct, not confirmatory of the mechanism.**

The biological evidence should increase confidence that *state-dependent access* is a real computational pattern, but should not be used to skip the receiver-conditioning discriminator.

---

## MECH-548 verdict

### What the literature supports

The reviewed biology strongly supports two premises:

1. endpoint representations are not stationary — hippocampal population codes continue to change under learning/plasticity;
2. interareal communication geometry can itself change with experience and brain state while retaining different stability profiles for different partners.

Thus a one-step bridge assay is scientifically incomplete. A useful interface must be checked against the evolving native dynamics of the coupled systems.

### What it does not support

No reviewed biological source directly demonstrates either of MECH-548's two registered mechanisms:

- repeated translated outputs accumulating **off-manifold compounding** because they re-enter as ordinary receiver state;
- **semantic double-counting** caused by repeated re-injection of already-present transmitted content.

No biological source in this pull performs the critical registered comparison:

```text
cumulative translated-state reuse
versus
clean-base / temporary-overlay reuse
```

Fenton 2024 also supplies an important rival: apparent coordinate drift can coexist with stable underlying relational/manifold structure. A bridge that binds to the stable relation may remain coherent without needing an explicit clean-base mechanism.

### Literature direction

**Overall: biologically motivated but mechanism-unproven.**

The literature justifies doing the recurrence-stability assay. It does not raise MECH-548 above candidate status.

---

## Cross-claim consequence for the hippocampal translation-map programme

The pull strengthens the distributed formulation developed in the archaeology/literature tranche:

```text
reference-frame conversion / relational indexing / context-selective retrieval
                    +
partner-specific low-dimensional communication
                    +
dynamic interface maintenance
```

rather than:

```text
hippocampus = generic translator
```

The strongest explicit coordinate-transformation evidence in tranche 1 lies in retrosplenial→entorhinal circuitry; the hippocampal evidence is stronger for indexing, relational maps, partner-specific subspaces, pattern completion and replay/reinstatement.

---

## Claim-minting decision

**No new claim was minted in this literature tranche.**

Reason: the candidate new content is already partitioned across existing claims, while the genuinely new anatomical/reference-frame formulation belongs to the still-separate shared-reference-frame thought and requires its own overlap/intake pass. Minting a broad “hippocampal translator” mechanism now would both duplicate existing claims and overstate the literature.

Accordingly there is **no further literature debt generated by this tranche**.

The pre-existing MECH-547/548 literature debt that triggered this review is closed by the seven entries above. Derived literature indexes/confidence aggregates may be rebuilt by the normal index/governance pipeline; no claim status field should change merely because the pull landed.
