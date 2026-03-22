# Literature Summary: 2026-03-22_mech030_synaptic_homeostasis_tononi2006

## Claims Tested

- `MECH-030`

## Source

- Tononi G, Cirelli C (2006). *Sleep function and synaptic homeostasis*. Sleep Medicine Reviews.
- DOI: `10.1016/j.smrv.2005.05.002`
- URL: `https://www.sciencedirect.com/science/article/pii/S1087079205000523`

## Source Wording

The Synaptic Homeostasis Hypothesis (SHY) proposes that waking is associated with synaptic potentiation across
cortical circuits. Learning, sensory processing, and motor activity all strengthen synaptic connections, progressively
increasing metabolic cost and reducing the signal-to-noise ratio of neural representations. This accumulating
potentiation also saturates plasticity mechanisms, impairing the capacity for further learning.

Slow-wave sleep (SWS) reverses this drift. During SWS, slow oscillations produce a global, proportional downscaling of
synaptic weights -- reducing them toward a renormalized baseline. The evidence includes: (1) homeostatic regulation of
slow-wave activity (SWA) as a function of prior wake duration and learning intensity; (2) molecular markers of synaptic
strength (GluR1 phosphorylation, AMPA receptor levels) peaking at the end of waking and decreasing after sleep; (3)
behavioral performance gains after sleep attributable to SNR restoration rather than continued consolidation.

SHY predicts that the net effect of sleep is not storage of new memories but restoration of the dynamic range needed
for further learning. It is compatible with, but distinct from, active systems consolidation accounts (such as
Diekelmann & Born): downscaling and selective replay may occur in parallel, with downscaling providing the substrate
into which replayed representations are written.

## REE Translation

MECH-030 specifies that the offline sleep mode must recalibrate precision priors (alpha_k) and reopen option space.
SHY provides the biological precedent for why this recalibration is architecturally required and cannot be replaced by
continuous online normalization:

1. **Precision inflation during waking.** SHY's net waking potentiation is the analog of precision gains inflating
   during sustained online task engagement. Without a reset mechanism, the system becomes rigid -- option space
   contracts, and novel trajectories cannot be adequately evaluated.

2. **Global renormalization during sleep.** SHY's proportional downscaling maps onto recalibrating alpha_k precision
   gains to a baseline, restoring the dynamic range needed for subsequent planning episodes.

3. **Residue compression.** The overfit residue traces accumulated during dense online episodes (spurious attributions,
   miscontextualised harm) are candidates for downscaling. SHY provides a biologically grounded mechanism for this
   function.

4. **Sleep is not optional.** SHY supports the architectural requirement in ARC-011 that offline integration cannot
   be skipped: without it, plasticity capacity saturates and moral paralysis (the REE failure mode for omitted sleep)
   becomes inevitable.

## Caveat

MECH-030 is explicitly V4 scope in REE -- the sleep mode is not implemented in V1, V2, or V3 substrates. This entry
provides architectural motivation only.

SHY's global non-selective downscaling conflicts with a critical invariant of MECH-030 and ARC-020: genuine harm
MUST NOT be erased during consolidation. SHY by itself does not explain how harm-bearing residue traces are protected
from global downscaling. This gap requires an additional mechanism -- the hypothesis tag (MECH-094) is the REE
candidate for labelling genuine harm traces so they are excluded from downscaling. SHY provides the bulk process;
MECH-094 provides the protective gate. Neither source alone is sufficient for the full MECH-030 account.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.84`
