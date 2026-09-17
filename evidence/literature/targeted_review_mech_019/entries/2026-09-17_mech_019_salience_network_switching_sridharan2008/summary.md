# A critical role for the right fronto-insular cortex in switching between central-executive and default-mode networks (Sridharan, 2008)

**Claim tested:** MECH-019 -- Control plane shapes modes of cognition, not discrete choices.
**Direction:** mixed | **Confidence:** 0.60

## What the paper did

Sridharan, Levitin and Menon ran three fMRI experiments -- an auditory event-segmentation task, a
visual oddball attention task, and task-free rest -- and found the same pattern in all three:
central-executive network up, default-mode network down, with right fronto-insular cortex and
anterior cingulate active at the transition. Applying Granger causality analysis to the BOLD time
series, they concluded that the right fronto-insula plays a critical and causal role in
*initiating* the switch between the two networks, and does so across paradigms and modalities.

This became one of the foundational papers for the triple-network model and for the idea of a
salience network with switching authority over large-scale brain state.

## Why this is in a MECH-019 pull

Chiefly for construct correspondence, and it is unusually close. REE's SalienceCoordinator is
explicitly the cingulate/anterior-insula analogue; its input channels are literally named
`aic_salience`, `dacc_pe`, `dacc_foraging`, `dacc_difficulty`. Its output is a soft vector over
{external_task, internal_planning, internal_replay, offline_consolidation}, and the first two of
those stand in reasonable correspondence to CEN and DMN. So this paper speaks to the architectural
premise MECH-019 inherits from ARC-005: that there is a salience-driven module with authority over
which large-scale cognitive mode is occupied, and that it sits in the anterior insula and cingulate.
On that question the evidence is good and the correspondence is not strained.

## And why it does not settle the claim -- in fact pulls slightly against it

MECH-019's distinctive assertion is that the control plane is *not* a discrete chooser. The
literature it inherits describes this circuit as a switch. Sridharan et al.'s own language is
switching, initiation, causal trigger; the whole framing is of a discrete event with an identified
initiator. That is a much better description of the substrate's `mode_switch_trigger` -- a boolean
that fires when a salience aggregate crosses the MECH-259 threshold and the argmax has changed --
than of continuous landscape-shaping.

I do not think this falsifies anything, and I want to be careful not to overstate it. The
switch-like framing may simply be what a graded process looks like through a haemodynamic filter,
which is the honest reading. But it is worth recording that the dominant framing in the biological
literature MECH-019 draws on is the one the claim is arguing against, and that the claim's
inheritance from ARC-005 is therefore not as clean as it might appear.

## The methodological limits, which are the real story here

Two, and both are serious enough that I have capped confidence at 0.60 despite the paper's
standing.

The first is temporal resolution. The haemodynamic response unfolds over seconds. MECH-019 turns on
whether probability mass migrates over several *ticks* before a flip, or whether occupancy sits
flat and snaps. That distinction is entirely below what fMRI can resolve. This paper is not weak
evidence about transition shape; it is silent on it. Any reading of "the insula switches networks"
as evidence *for* discreteness would be reading the measurement's resolution as a property of the
brain -- which is the same error, in the opposite direction, that the Latimer entry in this pull
warns about.

The second is Granger causality on BOLD. Regional differences in haemodynamic lag can produce
spurious directionality, independent of any neural influence, and this specific analysis attracted
published criticism on exactly those grounds. The switching *phenomenon* -- CEN up, DMN down, with
salience-network activation at the transition -- is robust and widely replicated. The *causal
initiation* claim rests on a contested inferential route.

## Confidence

0.60, mixed. The entry constrains where REE's control plane sits and gives the SalienceCoordinator's
anatomy genuine biological warrant. It constrains almost nothing about how that control plane
operates, which is what MECH-019 actually claims. Filing it as `supports` would mistake
architectural placement for dynamical evidence, and filing it as `weakens` would give far too much
weight to a framing artefact of the measurement. Mixed is the accurate label.
