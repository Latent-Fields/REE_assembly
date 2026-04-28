# Diba & Buzsaki 2007 -- Forward and reverse hippocampal place-cell sequences during ripples

According to PubMed: [10.1038/nn1961](https://doi.org/10.1038/nn1961) (PMID 17828259).

## What the paper did

Diba and Buzsaki recorded CA1 place-cell ensembles in rats running an elevated linear track and isolated the brief sharp-wave-ripple-associated sequence events that occurred at the end of each run and during pre-run pause epochs. They decoded the spatial trajectories represented by those sequences and asked whether the temporal order matched the spatial order of the just-traversed run.

## Key findings relevant to MECH-057b

Two distinct sequence types occurred. At the end of a run, the place-cell sequence recurred in reverse order -- a retrograde rehearsal of the path just taken. In the pause epoch before the next run, the sequence ran in forward order -- an anticipatory simulation of the upcoming path. Both events coincided with sharp-wave ripples, and the vector distances between place-cell pairs were preserved in the temporal structure. This gives MECH-057b two important architectural pieces. First, sequence completion is a discrete detectable event: the switch from reverse-replay (post-run, evaluative) to forward-replay (pre-run, anticipatory) marks the boundary. Second, the temporal structure to support a candidacy gate exists -- the system has a moment when it can verify completion of the just-finished trajectory and a separate moment when it emits candidates for the next.

## Mapping to REE

In REE, MECH-057b posits that hippocampal sequence completion gates the candidacy of trajectories for downstream evaluation. Diba and Buzsaki's data provide the temporal substrate for that gating: completion is event-detectable (reverse replay), and candidate emission is event-distinct (forward replay). The two are not the same event. This decouples the "is the just-finished sequence valid?" check from the "what is the next candidate?" emission, which is exactly what MECH-057b requires.

## Limitations and caveats

The paper documents the temporal structure but does not test that this structure acts as a control signal. The reverse/forward switch could be epiphenomenal of run timing rather than a candidacy gate. A direct test would silence reverse-replay events and ask whether subsequent forward-replay candidacy degrades. Additionally, the linear-track context constrains the topology of replay -- the open-field generalization comes from Pfeiffer & Foster (2013), which is why both papers are needed.

## Confidence reasoning

I score this 0.62, evidence_direction mixed. Source quality is high (foundational Nat Neurosci paper). Mapping fidelity is moderate because the paper documents the temporal structure rather than the gate function -- it provides the substrate on which MECH-057b can operate without testing the gating mechanism itself. Marked mixed because it strongly supports completion-as-detectable-event but is silent on the suppression of non-completing candidates that MECH-057b also posits.
