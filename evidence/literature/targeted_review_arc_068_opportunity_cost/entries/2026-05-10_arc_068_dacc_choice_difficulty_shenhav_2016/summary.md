# Shenhav, Straccia, Botvinick & Cohen 2016 -- Choice-difficulty reinterpretation of dACC

**Citation:** Shenhav A, Straccia MA, Botvinick MM, Cohen JD. Dorsal anterior cingulate and ventromedial prefrontal cortex have inverse roles in both foraging and economic choice. *Cogn Affect Behav Neurosci*. 2016;16(6):1127-1139. PMID: 27580609. [DOI](https://doi.org/10.3758/s13415-016-0458-8).

## What the paper does

Shenhav et al. replicate and extend the Kolling 2012 foraging-vs-economic-choice study with a larger sample and explicit methodological corrections (choice biases, broader foraging-value range). Their reinterpretation: what Kolling et al. read as a dACC signal tracking foraging value is better described, once these corrections are applied, as a signal tracking choice DIFFICULTY. They further extend the finding by showing that the same difficulty-vs-foraging-value collapse applies to economic-choice tasks, and that the inverse pattern in vmPFC is also generic across choice types. The conclusion: dACC and vmPFC are not dissociated into a foraging-vs-economic-choice division of labour; both are engaged similarly across choice types, and the apparent foraging-specific dACC signal is a methodological artefact of the original task design.

## Why this matters for ARC-068

The paper is the COUNTER-EVIDENCE entry for the R1 verdict (ARC-068 vs SD-032b boundary). The Kolling 2016 review (separate entry, PMID 26774693) is the load-bearing anchor on one side of the debate; Shenhav 2016 is the load-bearing anchor on the other. The synthesis CANNOT pretend the question is settled.

If Shenhav's reinterpretation prevails, the SD-032b dACC foraging_value bundle component (currently in `ree_core/cingulate/dacc.py` per the SD-032b implementation_note) loses some of its biological grounding -- the dACC signal it modelled may be choice-difficulty rather than foraging-value. By extension, any ARC-068-vs-SD-032b architectural argument that leans on substrate-level distinction ('they're different signals in dACC') is weakened. The cleanest architectural recovery is to anchor ARC-068 PRIMARILY on the Niv 2007 mesolimbic-DA tonic-scalar substrate (which Shenhav does not contest) and treat any dACC engagement as a downstream consequence -- the dACC may be tracking the choice difficulty INDUCED by an opportunity-cost computation rather than computing the opportunity cost directly. SD-032b retains its dACC anchor but the synthesis should acknowledge the contested status.

The R1 verdict is therefore not a clean separation. The architectural distinction between ARC-068 (always-on cost-of-passivity at trajectory-score level, anchored on tonic mesolimbic DA via Niv 2007) and SD-032b (task-conditioned switch-when-current-bad at mode-switch level, anchored on dACC via Kolling 2016 with the Shenhav reinterpretation pending) is best framed as a TIMESCALE / KERNEL distinction (long-run reward history vs current-environmental average) rather than a SUBSTRATE distinction (DA vs dACC). The two architectural commitments compose because they compute different things, not because they live in different brain regions.

## Caveats

The paper is one side of an active debate. Kolling 2016's response (separate entry) addresses the methodological challenges but does not retract the foraging-value interpretation. The empirical evidence (larger sample, methodological corrections) is non-trivial but not decisive; the debate is ongoing. The synthesis cannot use Shenhav 2016 as a settled refutation of Kolling, only as a serious challenge that constrains how strongly ARC-068 / SD-032b can lean on dACC-as-source.

A second caveat: the implication chain from Shenhav 2016 to ARC-068 is multi-step. Shenhav directly contests the dACC-foraging-value substrate claim, which is most directly relevant to SD-032b. The ARC-068 implication is one step removed: SD-032b loses some grounding, and consequently the architectural separation between ARC-068 and SD-032b cannot rest on substrate. The mapping_fidelity score is moderate (0.70) for that reason.

A third caveat: fMRI inference. The choice-difficulty-vs-foraging-value distinction is itself a model-fitting question, and both interpretations are consistent with much of the data. R1 should report the contested status rather than picking a winner.

## Confidence reasoning

Source quality high (large-sample fMRI with explicit replication and methodological corrections). Mapping fidelity moderate (one step removed from ARC-068; contested status; the relevance is via weakening of an adjacent claim's substrate anchor). Transfer risk moderate-to-high (fMRI inference, contested interpretation, multi-step implication chain). Aggregate 0.72.

According to PubMed, this paper appears under the cited PMID with the DOI as listed. Direction `weakens` because the paper undermines a substrate anchor that the ARC-068 architectural argument adjacent-relies-on; not direction `supports` even though the paper is methodologically strong, because the ARC-068 commitment fares better when ITS own anchor (Niv 2007 mesolimbic DA) survives uncontested while the dACC-foraging-value side of the contrast weakens.
