# Summary: Seymour, Daw, Roiser, Dayan & Dolan (2012) — Serotonin selectively modulates reward value coding in the human brain

**Claim tested:** MECH-186 (valence_wanting_floor — tonic serotonergic floor on VALENCE_WANTING)  
**Evidence direction:** supports | **Confidence:** 0.65

## What the paper did

Seymour and colleagues used acute tryptophan depletion (ATD) — a dietary manipulation that transiently reduces central serotonin synthesis — in healthy human participants undergoing fMRI while completing a Pavlovian conditioning task with both monetary rewards and mild physical punishments. ATD was compared to a balanced amino acid control mixture within subjects. The design specifically aimed to test whether serotonin selectively affects reward or punishment processing, or both equally.

## Key findings relevant to MECH-186

ATD selectively impaired neural and behavioural representations of reward outcome value without significantly affecting punishment processing. In vmPFC and lateral putamen, the blood-oxygen-level-dependent signal tracking reward value was attenuated under ATD relative to control; punishment-related signals were relatively preserved. Behaviourally, participants showed reduced sensitivity to reward magnitudes under depletion. This is direct causal evidence in humans that 5-HT level selectively supports benefit-side valuation — the exact asymmetry MECH-186 predicts: when serotonin is depleted, VALENCE_WANTING floor drops and goal terrain becomes illegible, while harm avoidance (punishment) remains relatively functional.

## Translation to REE

MECH-186's core claim is that tonic 5-HT maintains the wanting floor — the minimum non-zero VALENCE_WANTING in the residue field — so that the agent can still detect and pursue benefit even when under chronic harm. Seymour et al. provides human causal evidence for this claim at the neural and behavioural level: pharmacologically lowering 5-HT impairs reward value coding (vmPFC) and reward sensitivity. The valence asymmetry (reward more affected than punishment) is exactly what MECH-186 predicts, and the result is in humans using a well-validated depletion protocol.

## Limitations and caveats

Tryptophan depletion is a blunt instrument: it reduces central 5-HT synthesis systemically, not specifically in DRN projections to vmPFC. The mapping from acute ATD to the chronic harm-exposure scenario in REE requires inference. The conditioned reinforcers used here (monetary, physical) are not identical to the benefit/hazard structure of the CausalGridWorld. The neural localisation to vmPFC is consistent with MECH-186 but not required by it — the REE residue field is a latent computational structure, not a one-to-one vmPFC mapping.

## Confidence reasoning

Source quality is high (0.85): J Neuroscience, within-subject human ATD design, fMRI, behavioural validation. Mapping fidelity moderate (0.72): causal serotonin manipulation + valence asymmetry + reward value coding impairment all align, but the residue field construct is not directly analogous to vmPFC reward coding. Transfer risk moderate (0.35): human study reduces species transfer risk; acute ATD to chronic depletion mapping is the main gap. Aggregate confidence: 0.65.
