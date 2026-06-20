# Hikosaka, Takikawa & Kawagoe 2000 — the SNr→SC permission gate, and the value-monopoly failure mode built into it

**Claim grounding:** ARC-107 (BG selector constitution), MECH-448 (F→eligibility demotion / permission gate) · ARC-106 component 3 (pallidal permission gate) + context arbitration
**Source:** Hikosaka O, Takikawa Y, Kawagoe R. *Physiological Reviews* 80(3):953–978 (2000). [DOI](https://doi.org/10.1152/physrev.2000.80.3.953) · PMID 10893428.
*According to PubMed.*

## What the paper synthesises

Hikosaka's review is the most complete electrophysiological account of a basal-ganglia permission gate in a single, tractable circuit: the control of saccadic eye movements. The substantia nigra pars reticulata (SNr) **tonically inhibits** the superior colliculus (SC). To make a purposive saccade, the right cortical signal must be selected — and this is done by the **caudate disinhibiting the SC** (pausing the SNr brake) for the chosen target. The basal ganglia have a second mechanism, via the external pallidum (GPe) and subthalamic nucleus (STN), that can *further enhance* the SNr→SC inhibition — a No-Go strengthening layered on top of the gate. Critically, the signals carried through this circuit are **strongly modulated by behavioural context** — working memory, expectation, and attention — and **reward expectation facilitates the rewarded saccade**.

## Why it matters for the ARC-107 constitution

This single circuit grounds three of ARC-107's components operating *together*, which is more than any other entry in the review does:

1. **Permission-to-commit gate** — SNr tonic inhibition of SC, released by caudate disinhibition. Commitment is brake-release, exactly the MECH-448 / Chevalier-Deniau framing, but here with primate single-unit data showing it during actual behaviour.
2. **STN-enhanced bounded No-Go** — the GPe/STN mechanism that strengthens the SNr→SC inhibition is the indirect/hyperdirect suppression that MECH-449 generalises into a bounded No-Go pressure, shown here as a real, separable layer.
3. **Context arbitration** — the design note's selection pipeline includes a "context arbitration" step, and Hikosaka is the grounding for it: the gate is set by working memory, attention, and expectation, not by a single fixed value. This is the cleanest demonstration that the BG permission gate is set by *multiple* context channels — precisely the precondition ARC-107 argues REE's single-scalar selector lacks.

## The double edge — why this entry is unusually honest

I weight this entry carefully because it cuts both ways, and the cut is exactly the one ARC-107 lives on. The same review that grounds "multi-channel context arbitration" also documents that **reward expectation facilitates the rewarded saccade**: a value signal can preferentially open the gate for the high-value target while the alternatives stay inhibited. That is the *biological analog of REE's F-monopoly* — a context-modulated permission gate can **still collapse onto a single dominant channel** if that channel monopolises the disinhibiting input. So Hikosaka grounds the structure ARC-107 wants *and* documents the failure mode MECH-448 must break, in the same circuit. The lesson for the build is sharp: the flexibility comes from the caudate carrying genuinely *different* context signals (memory vs attention vs reward), not from the gate per se. A REE permission gate fed only by F would reproduce the architecture and none of the flexibility. This entry therefore grounds the *necessity* of a multi-channel eligibility input, not the *sufficiency* of merely adding a gate — a distinction the design note's risk register (§5, "do not use a selector repair to paper over local signal-quality failures") already insists on.

The dual-direction psychiatric mapping is here too: STN/GPe can *enhance* the SNr→SC brake (over-active → akinesia/over-braking pole), and losing it yields premature or involuntary saccades (the impulsive pole) — the same Go-over-pressure / No-Go-over-pressure dyad ARC-107's psychiatric column tracks, observed in the oculomotor gate.

## Limitations

The modality is oculomotor — saccades — one step removed from REE's abstract committed-action classes, so the transfer is functional rather than literal. And as with the disinhibition entry, the literal SNr/SC tonic GABAergic mechanism has no REE counterpart; "permission" becomes an algorithmic commit-entry predicate. The grounding is of the functional logic and the demonstrated multi-channel precondition, not of the wiring.

## Confidence

**0.74 (supports)** — the highest of the three permission-gate entries because it carries primate electrophysiology and grounds three components at once, but explicitly discounted because the same data expose the value-monopoly failure mode at the gate, so it grounds the structure-plus-its-failure, not the sufficiency of the fix.
