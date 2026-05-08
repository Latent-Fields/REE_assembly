# Ormond, Serka & Johansen 2023 — Enhanced Reactivation of Remapping Place Cells during Aversive Learning

**Source:** Journal of Neuroscience, [DOI 10.1523/JNEUROSCI.1450-22.2022](https://doi.org/10.1523/JNEUROSCI.1450-22.2022) (PubMed PMID 36596695). According to PubMed.

## What the paper did

Long-Evans rats learned to navigate a multi-arm maze in which some arms ended in food reward and others delivered an aversive air-puff. The authors recorded CA1 place cells during the task and during subsequent sleep, then asked two questions: does the new task structure induce remapping, and are the remapping cells preferentially recruited into sharp-wave ripple replay events?

## Key findings relevant to the SD-011 generalization

Two coupled results:
1. *Partial remapping.* Task learning induced partial remapping — some place cells reorganized to encode the new affective task structure, while others remained stable. This is consistent with Moita 2004, Wang 2012, and Gauthier & Tank 2018: affect-channel tagging is partial, not wholesale.
2. *Replay enrichment.* Cells that remapped were preferentially recruited into sharp-wave ripple events compared with stable cells, despite having similar firing rates during waking navigation. So the new affect-tagged representation gets privileged access to the consolidation pathway.

This matters for the SD-011 generalization because it couples the map-tagging question to the sleep/replay machinery. Affect-channel-relevant cells are not just spatially repositioned — they get stitched into replay, which is the substrate by which the new representation can stabilize and propagate to neocortex.

## REE translation

This is the bridge between the SD-011 architecture and the sleep/consolidation claims (MECH-285, INV-049, the user's "I cracked it" sleep insight). Affect-stream map-tagging is not a static labeling — it has a dynamic write-into-replay step that ensures the tagged representation propagates downstream. For V3/V4, this argues that the architectural slot for an affect channel needs both a place-cell write-channel *and* a replay-recruitment bias.

## Limitations and caveats

The task confounds reward and aversive arms — the replay enrichment cannot be cleanly attributed to either valence alone. The headline framing is "context change" rather than "aversive-specific." A cleaner test would isolate aversive-only remapping and confirm replay enrichment is preserved. The replay analysis is sleep-state rather than during waking quiescence — the two regimes may behave differently.

## Confidence

0.78 — recent, methodologically careful, directly addresses the consolidation-pathway coupling that the simpler remapping papers don't. Bounded by the mixed-valence design.
