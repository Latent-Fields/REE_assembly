# MECH-501 literature pull -- targeted_review_connectome_mech_501

Timestamp: 2026-09-24T11:24:25Z. All citations verified via PubMed metadata this session.

## Entries
- 2026-09-24_mech_501_transient_corrects_forward_displacement_maus2009 -- supports, 0.55 -- abrupt-offset transients pull a forward-extrapolated position estimate back toward the sensed position, graded by transient vs motion strength (closest match to the core computational event; passive perception, no commitment).
- 2026-09-24_mech_501_predict_present_reconstruct_past_hogendoorn2022 -- supports, 0.45 -- TICS framework "predict the present, reconstruct the past" is nearly isomorphic to ARC-129 + MECH-501; theory, perception only.
- 2026-09-24_mech_501_prediction_revision_latency_cost_blom2021 -- supports, 0.40 -- EEG decoding: predictive activation must be overcome when a trajectory unexpectedly reverses (a measurable revision event specific to violated expectation).
- 2026-09-24_mech_501_unexpected_events_global_motor_suppression_wessel2017 -- mixed, 0.40 -- surprise recruits the STN/hyperdirect stopping network (supports the interrupt trigger = MECH-090/342 territory) but gives no evidence for state-estimate reconstruction.
- 2026-09-24_mech_501_chronostasis_backdating_abolished_by_violation_yarrow2001 -- weakens (the analogy), 0.45 -- chronostasis back-referral happens when the post-saccadic prediction is CONFIRMED and disappears when the target is displaced unpredictably; opposite dependency to MECH-501's trigger.

## Named anchors (the four phenomena in the claim's note)
- Chronostasis: verified (Yarrow et al. 2001 Nature, doi 10.1038/35104551). Analogy does NOT hold -- violation abolishes the backward referral. Recommend dropping it as an analogue.
- Intentional binding: verified (Haggard, Clark, Kalogeras 2002 Nat Neurosci, doi 10.1038/nn827). Not entered: it is temporal compression of action and outcome for voluntary actions (reversed for TMS-evoked movements); it involves no interruption, no violation-triggered correction, and no forward-displaced state estimate. Analogy does not hold beyond "perceived time is inferred".
- Sensorimotor temporal recalibration: verified (Stetson, Cui, Montague, Eagleman 2006 Neuron, doi 10.1016/j.neuron.2006.08.006). Not entered: it is slow trial-wise adaptation of the action-sensation delay, not a within-trial discontinuity. The one relevant detail -- illusory reversals engage ACC/MFC, read as comparison of a recalibrated vs a less-plastic timing representation -- is weak indirect support for keeping two estimates, but does not evidence interrupt-triggered reconstruction.
- Saccadic predictive remapping: verified (Duhamel, Colby, Goldberg 1992 Science, doi 10.1126/science.1553535). Not entered: remapping is the forward/anticipatory half (supports ARC-129-style forward displacement, not MECH-501). I searched for what happens to remapped representations when a saccade is cancelled (countermanding) and found nothing in PubMed with simplified queries -- that is the experiment that would actually test MECH-501 in this domain.
- Stop-signal / hyperdirect: covered by Wessel & Aron 2017 (Neuron, doi 10.1016/j.neuron.2016.12.013). Supports interruption, not reconstruction.

## Implications for the claim TEXT
1. The note is right to call the four phenomena loose analogies; the pull shows three of four do not map at all and chronostasis runs the opposite way. Suggest replacing them in the note with the motion-extrapolation / transient-correction literature (Maus & Nijhawan 2006 Vision Res doi 10.1016/j.visres.2006.08.028; 2009 JEP:HPP doi 10.1037/a0012317; 2008 Psych Sci blind-spot doi 10.1111/j.1467-9280.2008.02205.x) and Hogendoorn 2022 as the real perceptual precedent.
2. Scope: all positive evidence is perceptual (external object position under neural delay). Nothing found shows violation-triggered backward correction of the agent's OWN state estimate during a committed action, nor that it is separable from decommitment. The claim's distinctive content (distinct from and downstream of MECH-090/342; consequence-weighted trigger) remains unevidenced. Keep substrate_conditional; treat as "computational extension of a perceptual mechanism", not "neurally supported".
3. Suggested amendment: the corrected estimate should be predicted to be GRADED by the relative strength of the violation signal vs the forward model (Maus & Nijhawan 2009), not an all-or-none discontinuity. Falsifier risk: an alternative in which surprise simply degrades/flushes the state estimate (Wessel & Aron's cognitive disruption) rather than re-anchoring it toward s_hat(t) -- an REE test should measure direction of the change, not just its magnitude.
4. Postdiction (Eagleman & Sejnowski 2000 Science, doi 10.1126/science.287.5460.2036) is a rival to the forward-displaced premise itself (ARC-129): if percepts are postdictive rather than extrapolated, there is no forward estimate to pull back. Worth noting on ARC-129.

## Could not verify / not found
- No study found of remapping or state-estimate content after a countermanded saccade or stopped reach.
- No study directly comparing expected vs unexpected corrections of matched magnitude on state representation (the claim's corollary); Blom et al. 2021 is the nearest (unexpected reversal cost) but has no matched expected-correction arm.
