# van Moorselaar, Huang & Theeuwes (2023) -- Distractor processing indices are shaped by target expectations

## What the paper did

The distractor positivity, or PD, is the workhorse neural marker in the proactive-suppression literature: a salient distractor that fails to capture attention elicits it, and its amplitude is routinely read as an index of how strongly the distractor was suppressed. This study asked whether that reading is safe. It compared search where the target feature was fixed across trials against search where it varied randomly, measuring both the N2pc, which indexes target selection, and the PD.

## Key findings relevant to Q-082

Target selection was unaffected by the manipulation -- neither manual response times nor the N2pc changed. The PD, however, was reliably attenuated when target features varied. If the PD were a clean index of distractor suppression, a manipulation that leaves target selection intact should not move it. The authors conclude that the PD partly reflects the upweighting of target features, driven by regularities across preceding search episodes, and therefore cannot be attributed unequivocally to suppression.

## How this translates to Q-082

This entry does something narrower than the other three in this directory and it is worth being explicit about the difference. It is not evidence about REE's architecture. It is a discount applied to a body of *other* evidence -- the substantial human literature that cites PD amplitude as demonstrating a dedicated proactive suppression process. If that marker conflates suppression with target upweighting, then the affirmative case for the first horn of Q-082 in humans is weaker than a citation count would suggest.

What survives that discount is the parsimonious reading I have been circling in the Forschack and McPeek entries: a single competitive process in which candidates are weighted, targets are upweighted by history and goal, and what looks like suppression is the relative consequence rather than a separate operation. That is architecturally close to what REE already has in precision-weighted cue routing plus the MECH-254 top-k bottleneck, which is precisely the possibility Q-082 was registered to keep open rather than assume away.

I should note the field politics honestly, because they bear on how much weight this deserves. This is a contested literature in which the same research groups repeatedly dispute each other's markers, and van Moorselaar and Theeuwes are long-standing critics of the signal suppression hypothesis. That does not make the result wrong -- the manipulation is clean and the dissociation between an unchanged N2pc and an attenuated PD is the right test -- but it does mean it should not be treated as a settled correction to the field.

## Limitations and confidence

Single study, contested area, and it establishes impurity of a marker rather than absence of the process the marker was meant to track. REE has no PD analogue, so nothing here transfers structurally. Confidence 0.64, the lowest in this directory, which reflects its role: it removes support from one side of the question rather than adding support to the other.

As with the other Q-082 entries: this is grounding for a gated open question. Q-082 carries explicit do-not-build and do-not-queue instructions and is answered, if at all, by MECH-467's battery plus ablation of REE's existing mechanisms. Nothing here moves that gate.

*Retrieved via PubMed. [DOI](https://doi.org/10.1162/jocn_a_01986)*
