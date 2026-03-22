# Literature Summary: 2026-03-22_mech030_maladaptive_consolidation_walker2004

## Claims Tested

- `MECH-030`

## Source

- Walker MP, Stickgold R (2004). *Sleep, Memory, and Plasticity*. Annual Review of Psychology.
- DOI: `10.1146/annurev.psych.56.091103.070307`
- URL: `https://www.annualreviews.org/doi/10.1146/annurev.psych.56.091103.070307`

## Source Wording

Walker & Stickgold review evidence that sleep consolidates multiple forms of memory -- declarative, procedural, and
emotional -- with NREM and REM sleep serving complementary roles. REM sleep is specifically implicated in emotional
memory consolidation: affectively charged material is selectively strengthened relative to neutral material during
sleep, in a process dependent on intact REM architecture.

The review also covers evidence for maladaptive consolidation. Fear-conditioned memories are potentiated by sleep,
not attenuated. In individuals with PTSD, the disrupted sleep architecture -- characterized by fragmented NREM,
REM intrusions into NREM, and elevated REM density early in the night -- is associated with intrusive re-experiencing
(flashbacks, nightmares), hyperarousal, and emotional dysregulation during waking. This suggests a failure mode in
which offline consolidation amplifies rather than integrates distressing memory content.

The paper notes that sleep deprivation or fragmentation impairs subsequent emotional regulation, reducing the
capacity to contextualise affective responses and increasing reactivity to threat cues. The offline consolidation
process, when disrupted or dysregulated, can therefore contribute to -- rather than correct -- maladaptive
memory and mode-selection patterns.

## REE Translation

MECH-030 assumes that the offline sleep mode produces constructive recalibration: spurious residue is reduced,
genuine harm is contextualised (preserved but placed in context), mode boundaries are restored. Walker & Stickgold's
evidence complicates this in two ways that are architecturally important:

**Failure mode 1: Over-consolidation of harm traces.**
ARC-020 requires that genuine harm must not be erased during offline consolidation. But the biological evidence
shows that sleep can go further than mere preservation: affectively charged and fear-conditioned material is
selectively *strengthened*. In REE terms, this risks amplifying harm residue beyond its calibrated magnitude,
producing residue overgeneralisation (a MECH-030 failure mode explicitly noted in sleep.md). The design implication:
the offline mode needs not just a protection gate for genuine harm traces, but a precision ceiling on how much
harm residue can be amplified during consolidation.

**Failure mode 2: Disrupted consolidation distorts mode boundaries.**
In PTSD, REM intrusions into NREM disrupt the orderly hippocampal-cortical transfer. The result is not neutral
failure to consolidate -- it is active distortion: mode boundaries become hypervigilant (spurious threat
classification) and option space contracts (avoidance). This is the biological analog of the REE failure modes
listed in the sleep contract: residue overgeneralisation and brittle/frozen policy selection. The critical point
for REE architecture is that partial or malformed offline consolidation may be *worse* than no consolidation:
a half-completed offline phase that does not enforce the commit boundary protection could produce an REE system
exhibiting the computational equivalent of PTSD -- an offline replay that re-enacts harm scenarios without
integrating them.

**Design warnings for V4:**
1. The offline phase must be atomic with respect to commit boundary protection -- partial offline cycles must
   not be able to issue commit signals mid-replay.
2. Harm residue amplification must be bounded -- the offline phase must preserve without inflating.
3. The hypothesis tag (MECH-094) must survive the offline phase intact; tag loss during offline replay is
   the REE analog of the PTSD mechanism of tag-less intrusive re-experiencing.

## Caveat

MECH-030 is explicitly V4 scope -- not implemented in V1, V2, or V3 REE substrates. This entry is
architectural motivation and design warning only.

The PTSD analogy is instructive but should not be over-read: PTSD involves HPA axis dysregulation, structural
hippocampal changes, and multiple reinforcing factors that do not map onto single REE design parameters. The
failure signatures are directional warnings, not precise predictions. The paper (2004) predates the most detailed
PTSD sleep neurobiology work; more specific mechanistic content is in Walker (2009) and the dedicated PTSD
sleep literature. The mixed rating reflects that the paper both supports the consolidation function of sleep
and documents the failure modes that constrain how that function must be implemented in REE.

## Direction and Confidence

- `evidence_direction`: `mixed`
- `confidence`: `0.78`
