# Frank, Loughry & O'Reilly 2001 -- The basal ganglia gate what becomes *available* in PFC, distinct from selecting the act

**Claim touched:** ARC-063 design element (ii), the availability-vs-expression distinction. Cross-ref MECH-309 and -- importantly -- the SD-033a rule_state pathway that arc_062_rule_apprehension:GAP-B needs populated with differentiated rule states.

## What the paper did
This is the foundational PBWM-lineage model. Frontal cortex provides robust active maintenance; the basal ganglia provide a *selective, dynamic gating function* that decides when frontal representations are rapidly updated in a task-relevant way -- "releasing the brakes" by disinhibition. The model is applied to a continuous-performance task requiring subroutine-like selective working-memory updating, where some items must be gated into maintenance and others ignored.

## Why it matters for ARC-063
This grounds the distinction I was most worried was a pun: that *availability* gating (which candidate rule becomes active and maintained) is architecturally separate from *expression/selection* (which action wins). Frank/O'Reilly show that the brain already factors these: the basal ganglia gate *what enters and updates* the frontal active set, while frontal cortex maintains and the downstream selection happens elsewhere. For ARC-063 this is close to literal -- the CandidateRule field's tolerance-gated availability maps onto basal-ganglia-gated updating of a PFC rule_state, which is exactly the SD-033a rule_state input that GAP-B's falsifiers found collapse without a rule-creator. The gating *function* ARC-063 needs is attested and well-modelled.

## The honest caveat
Two gaps. First, what gets gated here is task-relevant working-memory *content*, not a labelled rule; ARC-063 assumes the same gate type can admit a CandidateRule, which this model does not test. Second, the BG gate here is selective/binary per stripe, whereas ARC-063's tolerance gate is graded and threshold-based -- so this paper grounds the gating *function* and the availability/selection split, while the *graded, conflict-scaled* character of the threshold comes from the Cavanagh and Frank STN papers in this same review. The three together cover element (ii) better than any one alone.

## Confidence
0.70 -- supports. Higher mapping fidelity than the threshold papers because gating-of-availability is the literal modelled function, and lower transfer risk (a general working-memory mechanism, not a clinical manipulation). The discount is for the content-vs-rule target gap and the binary-vs-graded form gap.