# Brown et al 2022 -- PWS Hypothalamic Volume

## Source
Brown SSY, Manning A, Goldstone AP, Manning KE. "Hypothalamic volume is associated with body mass index in patients with Prader-Labhart-Willi syndrome." Brain Communications 2022. DOI: 10.1093/braincomms/fcac229

## Key claim
Adults with Prader-Willi syndrome show hypothalamic volume reductions that correlate with BMI. PWS is the canonical clinical model of pathological insatiable hunger; the hypothalamic structural alteration is consistent with the long-standing clinical hypothesis of impaired satiety / drive-regulation failure.

## Why this matters for REE V3
PWS is the human pathology equivalent of an SD-036/SD-012 regulator failure. The clinical phenotype tells V3 what regulator failure looks like in the wild:
- drive_level saturated (insatiable hunger)
- no shutdown signal despite metabolic surplus (obesity)
- the failure mode is NOT zero drive (which would be safe) -- it is SATURATED drive (which is pathological).

This argues that the V3 regulator layer must be bidirectional: shutdown-after-need-met AND override-when-need-overrides-fear. The SD-036 fix to V3-EXQ-471 should be evaluated against PWS as a failure scenario for the regulator going the wrong direction.

## Failure signatures supporting REE
- **Saturated drive failure mode**: Absence of regulator produces stuck-at-max, not stuck-at-zero. Implementation implication: the regulator's failure mode matters as much as its normal function.
- **Graded substrate alteration**: Volume changes correlate with behavioural severity; supports graded regulator function rather than all-or-nothing.

## Caveats
- PWS is multi-system and genetic; volume changes could be cause, consequence, or correlate.
- Imaging-behaviour link is correlational.
