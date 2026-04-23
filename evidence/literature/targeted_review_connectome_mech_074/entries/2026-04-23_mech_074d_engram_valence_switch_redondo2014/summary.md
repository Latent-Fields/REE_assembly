# Summary: Redondo et al. (2014) — Bidirectional switch of hippocampal memory engram valence

**Source:** Redondo RL, Kim J, Arons AL, Ramirez S, Liu X, Tonegawa S (2014). *Nature*, 513(7518):426–430. [DOI: 10.1038/nature13725](https://doi.org/10.1038/nature13725)

**Claim tested:** MECH-074d — BLA analogue emits a remap_signal on harm-PE spike when predictor-attribution flags specific latent codes — partial (~one-third) remap, NOT wholesale replacement.

---

## What the paper does

Redondo and Tonegawa colleagues at MIT label hippocampal dentate gyrus (DG) or BLA engram cells with ChR2 during contextual fear or reward conditioning, then attempt to switch the valence of those memories by reactivating the engram during opposite valence conditioning. The central finding is a dissociation: DG engram cells can switch valence (fear→reward or reward→fear) when reactivated under opposite conditioning, but BLA engram cells cannot. The functional connectivity between DG engram cells and BLA engram cells changes when DG valence is switched.

## Key findings relevant to MECH-074d

1. **DG contextual engram can switch valence**: Reactivating DG engram cells during opposite conditioning transfers valence — the context now evokes fear when it previously evoked reward, and vice versa. This shows hippocampal contextual representations are plastic and can be partially remaapped.

2. **BLA engram valence cannot be switched**: The same manipulation applied to BLA-labelled cells fails — BLA-labelled engram retains its original valence signature. This supports the attribution-gating component of MECH-074d: BLA valence attribution is more stable than hippocampal contextual coding.

3. **DG-BLA functional connectivity changes**: When DG engram valence is switched, DG-to-BLA functional connectivity changes. This is consistent with MECH-074d's architecture: remap_signal from BLA gates which hippocampal codes are updated, and successful remap changes the DG-BLA relationship.

## REE translation and mapping

MECH-074d proposes that BLA emits remap_signal when both conditions are met: (a) harm-PE spike above threshold, and (b) predictor-attribution flags specific latent codes. The remap targets ~30-35% of codes (partial, not wholesale). Redondo et al. provide indirect support:

- BLA valence stability supports the claim that BLA-attribution gating is valence-consistent: BLA does not arbitrarily trigger remap.
- DG plasticity supports partial remap: the DG contextual engram can update while BLA valence attribution remains anchored — this is consistent with partial remap that updates contextual coding without overwriting the harm-valence association.
- DG-BLA connectivity change accompanying the switch is consistent with the post-remap architectural change that MECH-074d anticipates.

However, the mapping is *indirect and mixed*:

The paper's paradigm involves explicit optogenetic whole-engram reactivation during opposite conditioning — not the spontaneous harm-PE-triggered remap that MECH-074d proposes. The BLA engram rigidity shown here could constrain MECH-074d's remap amplitude: if BLA valence attribution is fixed (Redondo), why does BLA emit remap_signal at all in MECH-074d? The resolution is that in MECH-074d, BLA triggers a *contextual* remap via hippocampal write, not a BLA *self*-remap — this distinction is absent in Redondo's experimental design.

## Limitations and caveats

The explicit optogenetic design is the key limitation. Moita et al. (2004) — already in this directory — provides direct in vivo electrophysiological evidence for partial place-cell remapping triggered by fear conditioning (training-box correlation 0.57 → 0.39), which is more directly quantitatively relevant to MECH-074d's ~30-35% overwrite parameter. This Redondo paper provides complementary evidence for the engram-architecture underlying that remap, not a direct test of the remap mechanism.

The BLA engram rigidity finding could be read as *weakening* MECH-074d if interpreted as evidence that BLA valence coding never updates. The REE resolution is that BLA does not remap *itself*; it triggers hippocampal remapping. Whether this distinction is biologically valid is uncertain.

## Confidence reasoning

Confidence 0.62 (mixed). Nature landmark study, well-replicated engram manipulation. Partial support for DG plasticity and BLA attribution stability; no direct test of PE-triggered partial remap with attribution gating. Moita 2004 remains the primary direct evidence for MECH-074d's remap amplitude claim.
