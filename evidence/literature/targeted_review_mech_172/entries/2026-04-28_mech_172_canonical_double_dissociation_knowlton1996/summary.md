# Knowlton, Mangels & Squire (1996) — A neostriatal habit learning system in humans

According to PubMed ([DOI](https://doi.org/10.1126/science.273.5280.1399); PMID 8703077).

## What the paper did

Two patient groups and matched controls were tested on a probabilistic classification (weather-prediction) task and on declarative recall of the training episode. The amnesic group had medial-temporal/diencephalic damage. The Parkinson group had basal-ganglia dysfunction without dementia. The design tries to dissociate a "habit" learning system from the declarative-recall system by lesioning each separately.

## Key findings

A double dissociation. Amnesic patients learned the probabilistic classification at a normal rate but could not recall the training episode. Parkinson patients had intact recall of the episode but failed to acquire the classification. The conclusion the authors draw is that the neostriatum supports a parallel habit-learning system that does not depend on the limbic-diencephalic apparatus.

## Mapping to MECH-172

MECH-172 is exactly the architectural prediction this paper is the canonical demonstration of. REE asserts that the model-free habit system (MECH-163, D1/D2/SNc loops) operates online and does not require the hippocampal-to-cortical consolidation pipeline that the E3 attribution system depends on. If that separation is real, then degrading one system should leave the other intact — and Knowlton's design is the classical operationalisation of that test.

The translation step that needs care is the disease mapping. Knowlton's "amnesic" group was diencephalic + medial-temporal lesions (Korsakoff-type, anoxia), and the "BG-impaired" group was Parkinson, not Huntington. MECH-172 talks specifically about early AD vs Huntington's. The inference chain is: AD's pathology profile (entorhinal/hippocampal first, Braak I–II) is amnesia-adjacent in the same architectural sense Knowlton uses, and HD's striatal MSN loss is BG-impairment-adjacent in the same sense Knowlton uses. That's a defensible chain but it is not a single direct test.

## Caveats

The decisive AD vs HD comparison this paper does not provide; that has to come from the more recent AD-procedural-sparing and HD-implicit-deficit literature (entries on Schmitz 2014 and Holl 2012 / Vaca-Palomares 2019 in this same review). Knowlton's role here is foundational architecture: it establishes that the habit and declarative systems are parallel, which is the structural claim MECH-172 then specialises to a particular pair of dementias.

## Confidence reasoning

I land at 0.86. Source quality is near-ceiling — Science 1996, replicated many times since. Mapping fidelity is strong (0.85) because REE's claim is essentially a corollary of Knowlton's framework, not a different claim. The reduction comes from transfer risk (0.30): the AD/HD framing of MECH-172 is one inference step removed from Knowlton's own groups, and one could imagine confounders (AD's later-stage striatal involvement; HD's mood/executive overlay) that complicate the clean architectural read. But the architectural prediction itself is exactly what was tested.
