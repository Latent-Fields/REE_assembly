# Diba & Buzsaki 2007 -- forward and reverse SWR modes

## What the paper did

Rats ran an elevated linear track while place-cell activity and hippocampal local field potential were recorded. The analysis aligned spike sequences with sharp-wave-ripple events and asked whether replay occurred in the same direction as the animal's run or in the reverse direction, and at what behavioural epochs each direction predominated.

## Key findings relevant to MECH-285

Two modes were clearly distinguishable. Forward sequences -- cells firing in the same order the animal would encounter their place fields on the upcoming run -- appeared in anticipation of the run, coinciding with sharp waves. Reverse sequences -- the same cells firing in opposite order -- appeared at the end of a run. Vector distances between the place fields were preserved in the temporal structure of both, so the topological information was faithful in both directions. The paper established that SWR content has direction as an intrinsic variable and that the behavioural context in which each direction occurs is distinct.

## Translation to REE

MECH-285's sampler topology needs to cope with this dual-mode phenomenology. A single staleness-weighted sampler, run at all offline moments, would predict mode-independent seed distributions -- but Diba & Buzsaki show the seed state itself differs by mode. Forward seeds live near the animal's current position; reverse seeds live at the run endpoint. For the MECH-285 design this has concrete implications: the priority signal may need to be factored per mode. The same accumulated V_s staleness might generate a forward-replay bias toward goal-directed schema revision and a reverse-replay bias toward outcome-coupled credit assignment, depending on which trigger is active. A single scalar priority per anchor is probably insufficient.

This bears on the priority-shape question indirectly. The paper does not pit proportional against threshold-gated schemes, but it does establish that the sampler has internal structure beyond "one weight per anchor". Whatever MECH-285 settles on should be compatible with a forward/reverse factorisation.

## Limitations and caveats

This is awake replay on a linear track, not sleep. The translation to sleep SWR content is standard in the field (sleep SWRs include both forward and reverse sequences; Joo & Frank 2018 review) but not directly demonstrated in this paper. The study also predates most of the priority-shape and salience-interaction literature and does not manipulate those variables.

## Confidence reasoning

Foundational, well-cited phenomenological result. Source quality high. Mapping fidelity moderate -- the paper constrains the MECH-285 architecture but does not directly test its priority-shape or timing verdicts. Transfer risk moderate. Aggregate confidence 0.67.
