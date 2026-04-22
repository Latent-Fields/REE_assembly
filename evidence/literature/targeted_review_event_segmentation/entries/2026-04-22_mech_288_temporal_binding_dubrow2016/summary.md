# DuBrow & Davachi 2016 -- Temporal binding within and across events

According to PubMed, this fMRI study dissociated within-event vs across-event encoding mechanisms in the hippocampal-PFC system. [DOI](https://doi.org/10.1016/j.nlm.2016.07.011)

## What the paper does

fMRI during encoding of consecutive face and object stimuli, with subsequent serial recall tested both within and across event boundaries. The authors examined which neural signatures during encoding predicted later serial-order memory under each condition.

## Findings relevant to MECH-288

Successful serial encoding within events relied on increased HC-vmPFC functional connectivity. Successful encoding across event boundaries relied on univariate activation in middle hippocampus and left ventrolateral PFC. The two regimes are functionally dissociable. This means downstream consumers of MECH-288 segment_ids must be able to switch processing modes based on whether a boundary just fired.

## Mapping to REE

MECH-288 segment_id transitions must be observable as discrete events to downstream consumers, not merely as continuous changes in context. The substrate API should expose a boundary_emitted flag at the moment of segment_id transition so consumers can switch processing modes (within-segment incremental binding vs across-segment cross-boundary integration). This is a small but architecturally important API choice -- a substrate that exposes only the segment_id (not the transition event) leaves consumers to infer boundaries themselves.

## Limitations and caveats

The within/across distinction here is in human fMRI of episodic encoding; substrate consumers in REE (anchor sets, V_s readouts) operate at finer temporal scales and on simpler latent streams. The functional-distinction principle transfers; the specific neural implementation does not. The substrate should pick its own consumer-side switching logic, not try to inherit HC-vmPFC vs HC-lvlPFC routing.

## Confidence reasoning

0.75. Solid replication-class fMRI. Mapping moderate because the architectural lesson (expose boundary as discrete signal) is what matters; the specific neural circuitry does not transfer.
