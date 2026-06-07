# LMAN variability is a rapidly state-gated signal (Kao, Wright & Doupe 2008)

According to PubMed. Source: Kao, Wright & Doupe, *Journal of Neuroscience* (2008), [DOI 10.1523/JNEUROSCI.2250-08.2008](https://doi.org/10.1523/JNEUROSCI.2250-08.2008) (PMC3022006).

## What the paper did

The previous two entries establish that a dedicated basal-ganglia pathway *generates* exploratory variability and that this contribution is *tunable*. This paper supplies the missing piece for MECH-341's specific sub-clause — that the diversity signal weight can be amplified to parity — by showing that the variability output is a rapidly switchable *state*, not a fixed property of the circuit. The authors recorded from single neurons in LMAN (the output nucleus of the anterior forebrain pathway, the songbird pallial–basal-ganglia loop critical for vocal plasticity) while male zebra finches sang in two social contexts: "directed" (singing to a female) and "undirected" (singing alone).

## Key findings relevant to the claim

The same LMAN neurons switched signaling mode with context. During directed singing, neurons fired reliable single spikes precisely locked to the song — a low-variability, near-deterministic mode. During undirected singing, the same neurons showed prominent burst firing and substantial trial-to-trial variability, with burst structure and timing varying across repeats. Critically, the *average* song-locked firing pattern of each neuron was similar across contexts, implying a common underlying signal onto which a state-dependent variability component is added or removed. Different LMAN neurons in the same bird showed distinct firing patterns, suggesting subsets jointly encode song features rather than a single global noise term. The authors frame this as pallial–basal-ganglia circuits contributing to motor learning through multiple mechanisms: patterned signals that guide changes in output, plus *state-dependent variability* that subserves motor exploration.

## How this maps to REE (MECH-341)

MECH-341 does not merely require a diversity circuit to exist; it requires its signal weight to be amplifiable to *competitive parity* with the dominant deterministic pathway — diversity as a controllable state. Kao et al. show precisely this: the variability output of the basal-ganglia-loop nucleus is a rapidly switchable, context-gated state, dissociable from the underlying task-locked signal, that the system can drive toward exploration (high variability) or exploitation (precise, deterministic) on demand. The observation that the diversity signal is distributed across neurons with distinct patterns is a useful warning for REE instrumentation: a single scalar "exploration temperature" would under-describe what is, biologically, a structured multi-channel signal — a caution that resonates with the V3-EXQ-569 finding that diversity must be measured as per-candidate variance, not a global scalar.

## Limitations and confidence

This is the most indirect of the three MECH-341 entries. It concerns state-gating of an *output-stage* variability signal, one further step removed from MECH-341's named scoring/aggregation locus than the Kojima and Ölveczky studies. The gating variable is social context, which has no direct REE analog beyond "some state modulates the diversity weight." And the transfer from songbird vocal control to REE candidate scoring remains substantial. I include it because it is the cleanest evidence that the diversity weight is a genuine, rapidly tunable knob rather than a fixed circuit property — the specific clause of MECH-341 about amplifying the diversity circuit to parity. I score this **supports at 0.6**: source quality 0.82, mapping fidelity 0.5 (lowest of the three, locus-distance), transfer risk 0.45.
