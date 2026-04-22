# DuBrow & Davachi 2014 -- Temporal memory is shaped by encoding stability and intervening item reactivation

According to PubMed, this fMRI study showed that hippocampal pattern similarity across intervening items predicts subsequent successful order memory, and that category shifts (event boundaries) reduce that similarity. [DOI](https://doi.org/10.1523/JNEUROSCI.2535-14.2014)

## What the paper does

Subjects encoded sequences of celebrity faces and common objects, then completed a recency discrimination test. fMRI tracked hippocampal pattern similarity across pairs of items separated by three intervening items (some of which crossed a category boundary). The authors trained a face-vs-object classifier on encoding patterns and applied it during recency judgments to test for associative reinstatement.

## Findings relevant to MECH-288

Hippocampal pattern similarity across intervening items predicted subsequent successful order memory. Category shifts (boundary analogues) interrupted this stability. The intervening item category was reinstated during recency judgments. This validates the within-segment / across-segment distinction MECH-288 architecturally enforces.

## Mapping to REE

The substrate translation: items within a segment share a hippocampal context representation; segment boundaries flush this context. The MECH-288 event_segmenter, by emitting a new segment_id at boundaries, gives downstream consumers (anchor sets, temporal-order representations) the signal needed to implement the within/across distinction. Without explicit segment_id transitions, consumers would have to infer the boundary themselves -- duplicating the comparator code MECH-288 is supposed to centralise.

## Limitations and caveats

DuBrow used categorical shifts (face/object) as event-boundary proxies, which are perceptually obvious. Whether substrate-detected boundaries from latent change-points produce the same kind of pattern-similarity drop is an empirical V3 question. The architecture supports the right shape of effect; whether the magnitude transfers is the V3 test.

## Confidence reasoning

0.78. Solid JNeurosci paper. Mapping is solid for the architectural claim (segment boundaries should produce hippocampal context discontinuity); transfer risk is the usual concern about category-shift boundaries vs latent-stream boundaries.
