# Farrer et al. (2003) -- Graded inferior parietal activation as a parametric comparator for agency discrepancy

## What the paper did

Farrer and colleagues used PET imaging with a virtual hand paradigm to parametrically modulate the degree of motor-sensory mismatch experienced by subjects. Participants made hand movements while watching a virtual hand on screen. In four conditions, the virtual hand's movement was either perfectly aligned with the subject's actual movement (0 degrees rotation), slightly offset (25 degrees), substantially offset (50 degrees), or entirely produced by another person (100% other-caused). This design allowed the investigators to examine whether inferior parietal activation scales monotonically with the degree of discrepancy -- i.e., whether it behaves like a comparator rather than a binary switch.

## Key findings relevant to MECH-095

The results were unambiguous. Activation in the right inferior parietal lobe (covering the TPJ region) increased monotonically as the discrepancy between intended and observed movement grew larger. Insula activation showed the inverse relationship -- decreasing as discrepancy increased, tracking the progressive loss of the self-agency experience. The authors conclude that the level of activity in these specific brain areas "maps onto the experience of causing or controlling an action" in a graded, parametric fashion.

This is the most direct available evidence for the comparator mechanism underlying MECH-095. A comparator that fires a binary alarm could not produce a graded dose-response. What Farrer et al. demonstrate is that the inferior parietal comparator outputs a continuous mismatch signal proportional to the prediction error.

## Translation to REE and the EXQ-121 failure

MECH-095 proposes that the TPJ-equivalent comparator in REE computes the divergence between E2's efference-copy prediction of z_self_{t+1} and the actually observed z_self_{t+1}. When divergence is zero, no residue is attributed. When divergence is large, the state change is attributed to z_world and a residue candidate is generated. Farrer et al. support this architecture and add a constraint: the comparator's output should be a graded signal scaled to the mismatch magnitude, not a binary flag.

The EXQ-121 FAIL (AgencyComparator ON produced AUC=0.411 vs ABLATED AUC=0.745) is particularly interesting in this light. The comparator appears to be actively hurting performance when present. One hypothesis: the current REE implementation may be applying the comparator output as a hard gate (binary suppression) rather than as a graded weighting, and the imperfect forward model in V3 is generating too many false positives -- incorrectly classifying self-caused changes as world-caused. Farrer et al.'s graded signal suggests that a better implementation would have the comparator weight residue attribution by mismatch confidence, falling back to a prior when the forward model is uncertain.

## Limitations and caveats

The visuomotor rotation manipulation introduces discrepancy at the display level rather than at the level of internal forward-model mismatch. A true efference-copy comparator fires before sensory feedback arrives, using the motor command itself to generate a predicted sensory state. The rotation paradigm tests what happens when the comparison is made -- the mismatch is visible and consciously registerable. This means the study captures the comparator's output and its behavioral consequences, but not the feedforward computation itself. Whether the same inferior parietal region also responds to pre-sensory efference-copy comparison (as opposed to post-hoc visual mismatch detection) remains less directly tested.

Additionally, PET has limited temporal resolution; the study cannot say whether the inferior parietal activation precedes or follows the subjective sense of losing agency. Temporal order matters for whether this is a cause or a consequence of the attribution process.

## Confidence reasoning

Confidence is set at 0.85 -- the highest of the three new entries. The parametric design provides strong evidence for the comparator's graded response profile, which is a specific prediction that discriminates between a comparator mechanism and alternative accounts (e.g., a general conflict monitor, a social inference region, or a simple attention switch). The graded dose-response is exactly what MECH-095 requires. Transfer risk is modest because the computational abstraction maps cleanly across species and task contexts.
