---
title: Reusable Computational Motifs and Content Binding
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 13
status: candidate
status_asof: 2026-08-25
status_claim: SD-101
---

# Reusable Computational Motifs and Content Binding

**Claim IDs:** SD-101 (architectural commitment) + MECH-503 (mechanism hypothesis, instantiates SD-101)
**Subject:** `control_plane.role_content_binding` / `control_plane.motif_selection_and_content_binding`
**Status:** candidate, v3_pending, epistemic_category substrate_conditional. Compass registration only --
no substrate exists yet. **DO NOT build in V3 or queue a V3 experiment without an explicit `/governance`
version-routing decision.**
**Registered:** 2026-08-25
**Depends on:** SD-091, MECH-481, ARC-071, MECH-323 (SD-101); SD-101, MECH-481, SD-091 (MECH-503)
**Source:** `docs/thoughts/2026-08-23_reusable_computational_motifs_content_binding_and_coalition_composition.md`

---

## Problem

REE's coalition/topology control (SD-091, MECH-481) already lets the control plane recruit a temporary,
demand-typed configuration of subsystems. But the recruitment target is a fixed, named subsystem --
MECH-481's coalition templates name subsystems directly per `ControlDemandType` (e.g. E1 sensory encoder,
E2 forward model, a hippocampal anchor set). Nothing in the existing substrate asks whether the unit being
recruited could instead be a **reusable computational role** -- an operation such as maintain, compare,
accumulate, sequence, retrieve, or estimate-uncertainty -- with different **content** bound into it on
different occasions, rather than a dedicated subsystem per (function, content) pair.

Corroborating literature (not yet independently `/lit-pull` reviewed): Osako et al. 2026 (*Nat Neurosci*,
DOI 10.1038/s41593-026-02410-0) show mice reuse neuronal subspaces (stimulus-processing,
memory-maintenance) across task phases carrying different content, with computation-specific lesion
effects in data-constrained RNNs. Driscoll, Shenoy & Sussillo 2024 (*Nat Neurosci*, DOI
10.1038/s41593-024-01668-6) and Tafazoli et al. 2026 (*Nature*, DOI 10.1038/s41586-025-09805-2)
corroborate shared dynamical motifs / neural subspaces across compositionally related tasks in
independent systems (multitask RNNs; monkey tasks).

## Proposal

Separate five dimensions the source thought argues should not be assumed to collapse into one another:
computational role/motif (`F`), representational content currently bound to it (`X_t`), substrate identity
realizing the role (`S_t`), coalition membership (`G_t`, SD-091's existing graph-valued output), and
task/context control (`theta_t`, `tau_t`). The tuple `R_t = (F, X_t, S_t, G_t, theta_t, tau_t)` is offered
by the source thought explicitly as a representational reminder, **not** a proposed implementation schema.

MECH-503 proposes inserting a role-selection + content-binding step into MECH-481's existing sequence
(monitor -> classify -> request -> **[select reusable motif -> bind content]** -> instantiate coalition/
topology -> operate -> reassess -> dissolve/sustain/escalate). Content binding and coalition/topology
instantiation are proposed as **separable causal axes**: a coalition x binding factorial (correct/wrong
coalition crossed with correct/wrong content binding) should produce dissociable failure signatures if the
axes are genuinely distinct -- this is MECH-503's primary falsifier.

## Explicitly distinct from adjacent claims

- **SD-091 / MECH-481** (coalition/topology control): extended, not duplicated. SD-091's output recruits
  *fixed named subsystems*; this claim asks whether the recruited unit could instead be a *reusable role*
  with content bound to it. SD-101/MECH-503 add a further, composable axis alongside SD-091's `G_t`, they
  do not alter or supersede it.
- **ARC-071 / MECH-323** (policy composition): a different compositionality axis, per the source thought's
  own explicit instruction not to conflate them. ARC-071 reuses *learned action/strategy structures* via a
  repetition-count + outcome-consistency accumulator (MECH-323). SD-101/MECH-503 concern reuse of a
  *cognitive operation* across different bound content, with no accumulator or repetition-driven formation
  process implied.
- **MECH-167** (interoceptive accumulation shared by `z_harm_a`/`drive_level`) and **ARC-061**
  (reafference-cancellation family across motor/interoceptive/propositional levels): narrow, already-built
  precedents for exactly this "same motif, different content" pattern -- cited as corroborating precedent,
  not depended-on as prerequisite machinery.
- **MECH-155 / MECH-156** (E1 general-associative-indexing reuse): a structurally similar intuition, but
  deliberately **not** wired as a dependency -- these carry an unresolved 2026-08-08 governance flag
  (E1-vs-HippocampalModule conflation) and importing that debt into a fresh registration was avoided.

## What would answer it

**Primary falsifier (MECH-503, Test D):** a coalition x binding factorial -- 2x2 crossing {correct
coalition, wrong coalition} x {correct content binding, wrong content binding}. Confirming: the two
manipulations produce dissociable failure signatures (wrong-coalition/correct-binding degrades *which*
subsystems interact while bound content stays usable to whichever engage; correct-coalition/wrong-binding
degrades *what* the correctly-recruited subsystems operate on while their interaction structure stays
intact). Failing: the two manipulations produce the same failure signature -- binding does no
discriminative work beyond what SD-091/MECH-481 already provide, and this claim should retire or fold into
MECH-481.

**Secondary (Test C, recombination):** two motifs developed/trained in separate contexts recombined for a
novel task never directly experienced; compare recombination (no structural learning) vs. de novo
mechanism learning vs. a control with one required motif unavailable.

**Non-degeneracy precondition** (learned from MECH-481's own 4-arm design): before trusting a Test D
dissociation, confirm the "correct" coalition and "correct" binding conditions are each independently
sufficient to solve the task above chance in isolation -- otherwise a null dissociation is uninformative,
not a verdict against separability.

## Status and next steps

No substrate exists. Both claims are `epistemic_category: substrate_conditional`, `implementation_phase:
v4`, registered as compass/architectural framing only. A future `/governance` cycle should explicitly weigh
whether a narrow slice (Test A/B, "same function, different content," against one of MECH-481's two
currently-templated `ControlDemandType`s) is cheaply testable against SD-091/MECH-481's existing V3 wiring
(`ree_core/claustrum/`) rather than waiting for a full V4 build -- this is a version-routing question for
governance, not decided here. A targeted `/lit-pull` on the three cited papers is a recommended next step.

See `evidence/planning/thought_intake_2026-08-23_reusable_computational_motifs_content_binding_and_coalition_composition.md`
for the full Stage 2 intake, including the novelty table against all cross-referenced claims.
