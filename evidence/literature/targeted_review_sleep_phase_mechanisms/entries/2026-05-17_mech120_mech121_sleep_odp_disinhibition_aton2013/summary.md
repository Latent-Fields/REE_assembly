# Sleep Converts Waking Disinhibition Into Lasting ODP via NREM Slow-Wave Phase-Locking

## Source
Aton SJ, Broussard C, Dumoulin M, Seibt J, Watson A, Coleman T, Frank MG (2013). Visual experience and subsequent sleep induce sequential plastic changes in putative inhibitory and excitatory cortical neurons. *PNAS*, 110(8), 3101-6. DOI: 10.1073/pnas.1208093110

---

## What the paper did

In freely behaving cats at the critical period, simultaneous recordings from fast-spiking (FS) interneurons and putative principal (excitatory) neurons in extragranular visual cortex during monocular deprivation (MD) and subsequent sleep. OD was assessed before MD, after MD, and after post-MD sleep.

## Key findings

MD induces FS interneuron depression (via spike-timing-dependent depression) and a response shift toward the deprived eye -- effectively disinhibiting open-eye-biased principal neurons during waking. During post-MD NREM sleep, principal neurons increase firing and become phase-locked to slow waves. OD shifts were only measurable after sleep, not after waking MD alone. Shift magnitude was proportional to MD-induced FS changes and to sleep-associated principal neuron phase-locking; neurons firing 40-300 ms after neighboring FS neurons during slow waves showed the greatest OD shifts.

## Translation to REE

This paper reveals the two-stage gate structure of ODP: (1) waking experience creates an instructive signal in the inhibitory network (FS depression specifies which neurons should be strengthened); (2) sleep converts this into lasting synaptic change via slow-wave-phase-locked principal neuron firing. OD shifts require sleep -- waking encoding alone is insufficient.

For MECH-120/MECH-121: the harm/goal signal accumulated during waking tags which trajectories are to be consolidated (FS disinhibition is the analog of the harm/benefit tagging signal), but the E1 weight update requires the slow-wave phase-locking that only occurs during NREM. If waking dynamics produce excessive tagging of dominant trajectories (WTA forward model dominance), gate 1 is corrupted before gate 2 opens -- sleep cannot consolidate clean instructions when the instructions themselves are biased toward a single dominant strategy. This is the two-stage gate argument for why waking-level WTA must be corrected rather than relying on sleep to rescue it.

## Limitations

The FS -> principal neuron disinhibition mechanism is cat visual cortex specific. The implication that 'corrupted waking tagging corrupts sleep consolidation' follows logically from the two-stage gate model but is not directly tested in this paper.

## Confidence

Confidence 0.87. Excellent source quality (PNAS, in vivo simultaneous recordings, Frank lab). Mapping fidelity good for the two-stage gate logic; moderate transfer step to REE computational architecture.
