# Summary: Sensorimotor Contingencies as a Key Drive of Development: From Babies to Robots

**Entry ID:** 2026-05-16_devrobotics_sensorimotor_contingency_jacquey2019
**Claim IDs:** INV-060, MECH-194, MECH-197, ARC-050

## What the paper does

Jacquey, Baldassarre, Santucci, and O'Regan (2019) synthesize experimental data from infant developmental psychology and robotic modeling to argue that sensitivity to sensorimotor contingencies -- the learned relationship between action and sensory consequence -- is the core engine of early cognitive development. They identify four developmental domains (body knowledge, memory, generalization, goal-directedness), each operationally characterized by a distinct experimental paradigm and measurable metric. They then sketch a computational blueprint architecture grounding this in a robot setting.

## Key findings and metrics

The paper's most REE-relevant contribution is its specificity about measurement. Body knowledge is assessed by whether motor responses become limb-specific rather than globally diffuse -- a quality shift, not just a quantity shift. Memory is quantified by retention interval (1 day at 2 months, 3 months at 18 months) and reactivation window compression (from 24 hours to near-instantaneous). Generalization is measured by transfer success when stimulus or context changes at increasing delays. Goal-directedness is operationalized by the revaluation paradigm -- whether an agent selects the correct means to reach a devalued vs. valued goal.

The pivotal finding for REE is the 7-month dissociation: infants at this age demonstrate bidirectional contingency knowledge (competence) but cannot yet use it to select appropriate actions (calibration). This is exactly the competence-calibration dissociation that MECH-195 postulates -- play builds strategy structure, while real-signal recalibration sets magnitude thresholds.

## REE mapping

INV-060 claims that play type progresses as subsystem competence develops. The four domains map onto REE's subsystem architecture: body knowledge onto E1/E2 motor-sensory forward models, memory onto hippocampal replay, generalization onto z_world transferability, goal-directedness onto E3 revaluation under SD-012. The developmental pivots (3, 6, 9, 24 months) give temporal grounding for MECH-197's stage ordering. The 7-month dissociation directly supports MECH-195: play builds strategy structure; real-signal recalibration sets magnitude thresholds.

## Limitations and caveats

The paper does not address play explicitly -- sensorimotor contingency is the driver, not play per se. The blueprint architecture (Mannella 2018) is schematic; no implemented system demonstrates multi-stage developmental gating using these metrics as transition criteria. Competence-calibration dissociation is described phenomenologically rather than formally modeled as separate channels.

## Confidence reasoning

Confidence 0.75: solid supporting evidence for INV-060 and MECH-197 stage ordering, and moderate support for MECH-194/ARC-050, but significant inference required to bridge from contingency-sensitivity to play-frame mechanics specifically.
