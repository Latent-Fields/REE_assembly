# Reward-tethered place cells (Masala et al., 2026, bioRxiv preprint)

## What the paper did

Masala and colleagues imaged hippocampal CA1 in freely behaving mice with longitudinal single-cell calcium imaging, tracking the same neurons across an unexpected reduction in reward magnitude. The design matters more than the technique here: the reward *location* was held constant while its *value* was downshifted. That is precisely the manipulation MECH-143 stands or falls on, and it is a manipulation surprisingly few papers in this literature actually perform -- most vary where the reward is, which conflates value change with spatial change.

## Key findings relevant to the claim

Three results bear directly on MECH-143. First, CA1 population activity encoded reward magnitude through elevated event rates at high-value locations -- a value signal in dorsal hippocampus, present before anything was changed. Second, the authors isolated a subpopulation they call *reward-tethered place cells*: neurons with genuine spatial fields distributed across the environment that simultaneously carry activity anchored to the high-value reward location. These are not reward cells masquerading as place cells; they are place cells that also carry value. Third, and most awkward for the claim as written, when reward was reduced the population activity equalised and these reward-tethered cells underwent rapid, selective remapping -- and that remapping *preceded* the behavioural adjustment.

That last detail is the one that closes off the easy escape route. If the remapping had followed the behavioural change, one could argue the map was responding to altered occupancy or altered running trajectories rather than to value as such. It did not.

But the paper also supplies the sentence that rescues what REE actually needs: *the broader spatial map remains intact*. The reorganisation was selective, not global. The terrain was not redrawn.

## How this translates to REE

MECH-143 as currently worded conflates two claims that this paper prises apart. The weaker claim -- that the spatial geometry over which ARC-007's trajectory proposal module navigates is not recomputed when goal value changes -- survives intact, and is arguably strengthened, since here is a direct value manipulation that leaves the broader map stable. The stronger claim -- that dorsal CA1 place cells are *insensitive* to goal value, full stop -- does not survive. A tagged subpopulation is exactly what value-sensitivity looks like.

I think the honest reframing is that dorsal CA1 does not look like a value-free map so much as a stable terrain carrying a sparse, separable value annotation, where the annotation can be rewritten without redrawing the terrain. That is a *better* substrate for ARC-007 than a genuinely value-blind map would be, because it explains how the proposal module can be sensitive to which goals are currently worth pursuing without needing a value-computation stage of its own. But it is not what MECH-143 says, and the claim should be narrowed rather than defended.

## Limitations and caveats

This is a preprint. It has not been peer reviewed, and MECH-143's status should not move on it alone -- I have capped source_quality at 0.60 for that reason and that reason only; the method itself is strong. It is also a purely appetitive manipulation in mice, so it speaks to reward magnitude and not to the aversive side of the residue field. And the authors' own framing -- that the remapping updates an internal model of the world when expectations are violated -- is closer to value computation than ARC-007's no-new-value-computation constraint comfortably allows. REE's reading of "map intact, therefore no new value computation during planning" is an inference the authors do not make.

## Confidence reasoning

0.62. High mapping fidelity (0.85) because this is the decisive design; moderate source quality (0.60) because of preprint status; moderate transfer risk (0.35) for the rodent-to-architecture step. Direction is **mixed** rather than *weakens* because the paper simultaneously refutes the strong reading and supplies direct support for the narrow reading REE actually depends on. Recorded as mixed so that governance sees both halves rather than a net that hides them.
