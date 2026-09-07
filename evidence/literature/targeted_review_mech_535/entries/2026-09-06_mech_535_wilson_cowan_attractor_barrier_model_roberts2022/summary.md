# Roberts and Conour (2022) -- a Wilson-Cowan model of catatonia and its treatment

**Question served:** Q2 (any computational account locating the deficit in the goal representation?) -- documented null. Also Q3/Q4 context.

## What the paper did

A two-population Wilson-Cowan model -- excitatory pyramidal cells and parvalbumin-positive interneurons, each summarised by a mean spike rate -- is parameterised so that it has two stable states separated by an unstable barrier. The transition from the high-rate to the low-rate state "represents the termination of a cortical activity pattern," and the authors' interpretive move is that "if the barrier is high then the system becomes stuck in a functional pattern and is interpreted to represent symptoms of catatonia such as posturing or perseveration." Benzodiazepines enter as increased inhibitory synaptic weight (more GABA-A current), which lowers the barrier and makes transitions more fluid; antipsychotics and lamotrigine enter as other parameter changes. The model is fitted to Bush-Francis totals in a residential schizophrenia cohort and used to explain treatment effect sizes and to suggest individualised dosing.

## What it says, and does not say, about the locus

This is the only computational model of catatonia the pull found, and it is a state-transition model: the pathology is that a selected cortical pattern cannot be released. There is no agent, no environment, no goal, no spatial variable and no policy. The paper does not mention ambitendency, approach/withdraw oscillation or goal representation. So Q2's null holds in computational psychiatry as well as in the clinic -- and it is a null of *unrepresentability* rather than of a hypothesis tested and rejected. A two-variable rate model cannot be asked what a state representation carries.

## How this bears on MECH-535 and MECH-536

For MECH-535 the entry is a marker: the existing computational treatment of catatonia sits at the persistence-excess pole (stuck behind a barrier), the opposite dynamics from a memoryless reactive actor that re-decides every step and never holds a course. Anyone who thinks 978's cycling is "a catatonia model like the Wilson-Cowan one" has the sign of the persistence deficit backwards. For MECH-536 the paper is mildly informative: it models too much persistence as the pathology and "make release easier" as the cure, which is consistent with persistence being a dial whose excess pole is perseveration -- the "latch yields perseveration, not competence" arm of MECH-536's prediction -- though the paper never contrasts persistence with representational adequacy and so does not test the dissociation.

## Caveats and confidence

Single-group modelling paper in a pharmacology venue; cohort synthesis rather than trial data; the fit is to BFCRS *totals*, so the model has never been asked which sign it produces. "Barrier height" is not a post-commit latch on a discrete action. Confidence 0.35.
