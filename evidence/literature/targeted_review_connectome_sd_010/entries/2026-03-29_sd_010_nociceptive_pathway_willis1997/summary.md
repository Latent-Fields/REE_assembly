# Willis & Westlund (1997) -- Neuroanatomy of the Pain System and Modulation Pathways

## What the paper did

Willis and Westlund wrote a comprehensive review of the ascending nociceptive pathways and descending modulation systems, synthesizing anatomical and physiological data up to the mid-1990s. The review covers six distinct ascending pathways -- spinothalamic, spinomesencephalic, spinoreticular, spinolimbic, spinocervical, and postsynaptic dorsal column -- with particular emphasis on the spinothalamic tract as the principal nociceptive highway. The authors describe peripheral nociceptor sensitization, dorsal horn organisation, and thalamic relay nuclei in detail, before moving to cortical targets and descending analgesia systems including the periaqueductal gray.

## Key findings relevant to SD-010

The paper establishes that the spinothalamic tract is anatomically divisible into two functionally distinct sub-systems. The neospinothalamic (lateral) pathway carries signals from A-delta mechanothermal nociceptors via Rexed laminae I, IV, and V to the ventroposterolateral (VPL) thalamic nucleus, which projects to primary (S1) and secondary (S2) somatosensory cortex. This pathway mediates the sensory-discriminative dimension of pain -- location, intensity, temporal profile, and quality. It is fast-conducting and precisely topographically organised. The paleospinothalamic (medial) pathway carries C-fiber polymodal nociceptor signals via laminae I, IV, and VII to the intralaminar thalamic nuclei (notably the central lateral nucleus), which project diffusely to anterior cingulate cortex (ACC), insula, and amygdala. This pathway mediates the affective-motivational dimension -- unpleasantness, threat urgency, and the drive to escape. Spinothalamic cells projecting to the CL nucleus have very large receptive fields, often covering the entire body surface, which is consistent with a role in emotional salience rather than precise localisation.

The two pathways are not entirely independent: lamina I neurons project to both lateral and medial targets, and the insula straddles both systems. But the dominant functional distinction -- lateral-discriminative versus medial-affective -- is well supported by lesion data, electrophysiology, and imaging.

## Translation to REE

SD-010 proposes that the harm stream in REE V3 must be architecturally separated from the world-state stream (z_world). The neospinothalamic stream maps directly to what SD-011 later formalized as z_harm_s: a proximity- and intensity-encoding signal that is action-conditional (moving away from a hazard reduces proximity in a predictable way), making it learnable by a forward model E2_harm_s. The paleospinothalamic stream maps to z_harm_a: an accumulated homeostatic deviation that integrates C-fiber input over time, tracks threat urgency, and feeds motivational salience to E3 without requiring a forward model because it is not readily action-conditional at short timescales.

The key architectural implication is that conflating these two streams into a single harm encoder -- or worse, folding harm into z_world -- would reproduce the failure mode analogous to a brain that cannot distinguish "where and how bad" from "how urgent and aversive." EXQ-093/094 (bridge_r2=0) confirmed that z_world and z_harm are orthogonal after SD-010, which is exactly what the anatomy predicts: the neospinothalamic stream and the general somatosensory-via-dorsal-column world-state pathway are genuinely distinct.

## Limitations and caveats

The review is from 1997; subsequent work has added nuance, particularly regarding the insula's dual role and the convergence of nociceptive signals at multiple thalamic levels. The clean lateral/medial dichotomy is acknowledged even in this paper as a useful simplification. The mapping from biological pathway anatomy to REE's learned latent separation is analogical rather than derived: the biology provides strong structural motivation but does not prove that a trained neural network will learn the same functional separation. Furthermore, the biological evidence is primarily from rodents and non-human primates; the human data in 1997 was mostly lesion-based.

## Confidence reasoning

The source is high-quality (foundational review, widely cited, from a specialist in spinal nociception). The mapping fidelity is strong because SD-010's two-encoder design closely mirrors the functional distinction described in the paper. Transfer risk is modest -- the claim is architectural (the separation is necessary) rather than quantitative (a specific magnitude). Overall confidence 0.85.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1097/00004691-199701000-00002
