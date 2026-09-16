---
title: "Organism-Level Validation Doctrine (GOV-JURIS-1, GOV-ECOL-1, GOV-HOTHER-1, GOV-DELETE-1, Q-108)"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 21
status: candidate
status_asof: 2026-09-16
status_claim: GOV-JURIS-1
---

# Organism-Level Validation Doctrine

**Status:** candidate governance doctrine, registered 2026-09-16 from
`docs/thoughts/2026-09-16_local_mechanism_success_vs_organism_level_intelligence.md`
(intake: `evidence/planning/thought_intake_2026-09-16_local_mechanism_success_vs_organism_level_intelligence.md`).
The full doctrine -- domain definitions, the developmental matched-final-state arms, the dynamic-interface
check, the Adaptive Recovery Battery design seed and the progress-report template -- lives in
`evidence/planning/organism_level_validation_doctrine_20260916.md`. This page is the registry anchor; it
does not restate that document.

**Governing principle.** Evidence receives no broader jurisdiction than the experiment earned. A mechanism
earns architectural confidence locally; an organism earns cognitive confidence only when those mechanisms
remain jointly useful under novelty, perturbation, development and ecological change. The doctrine is an
**umpire, not a ruler** (GOV-BEHADJ-1, GOV-UMPIRE-1): it does not require every experiment to test the
whole organism, it requires the summary layer to say which domains a result did and did not reach.

## The evidence-domain profile

Eight orthogonal domains, never a scalar ladder:

| Domain | Question | Nearest existing REE instrument |
|---|---|---|
| D0 instrument validity | Did the experiment measure what it says it measured? | GOV-PATHVALID-1, GOV-DRY-1, the recording standard |
| D1 local mechanism validity | Does the mechanism have the claimed property? | INV-105 rungs 1-2 |
| D2 local causal consequence | Does manipulating it change the intended downstream computation? | INV-105 rungs 5-6, ARC-130 local operation / authority |
| D3 closed-loop behavioural consequence | Does live organism behaviour improve? | ARC-130 committed throughput, GOV-BEHADJ-1 |
| D4 ecological generalisation | Does it survive a changed WORLD, not just a changed seed? | ARC-130 retention / generalisation; `rebinding_ecological_harness.py` (MECH-456) |
| D5 developmental validity | Does it work when acquired developmentally; does history matter at matched final capacity? | ARC-143, MECH-549 |
| D6 integrated compatibility and simplification | Does it stay useful in the assembled organism; can redundant machinery be removed? | GOV-MATCHAUX-1, GOV-CONTRACT-3, ARC-140 |
| D7 adaptive recovery | Can the organism discover its own model is wrong and recover without being told which part failed? | none built; Q-108 |

## Claims anchored here

### GOV-JURIS-1 {#gov-juris-1}

**Evidence-domain jurisdiction rule.** Any text that carries a result UPWARD -- closure-plan or roadmap
node, architectural recommendation, milestone or progress summary (`CURRENT_FRONT.md`,
`insights_report.md`, the morning digest, a governance headline), default-on decision, or a statement
about REE's competence -- carries an explicit `Evidence domain reached: D? / Domains not tested: ...`
line naming the SPECIFIC untested domains. A frozen-latent decoder result reaches at most D1; a live
selection perturbation at most D2; seeds alone never reach D4. Raw manifests and per-run autopsies are
exempt. Distinct from ARC-130 (per-mechanism) and INV-105 (per-variable), which it composes with; the
positive-evidence mirror of GOV-CAPCONTRACT-1. Manual discipline: no hook, no gate, no score.

### GOV-ECOL-1 {#gov-ecol-1}

**Seeds-versus-worlds reporting rule.** Stochastic replication (`N seeds`) and world-family replication
(`N environment families / N orthogonal perturbation classes`) are reported separately, and a result is
never called general, robust or transferable on seeds alone. A world-family count of 1 is a named debt
(`ecological transfer untested`), not an implied property. A frozen ecological suite is a FUTURE
requirement; when built it is frozen before use (GOV-FROZEN-1 discipline). Precedent: MECH-456's
V3-EXQ-733b/733c PASSes held at provisional until the world-driven V3-EXQ-745 leg existed. Proposed
mechanical hook, not applied: a `world_family` / `perturbation_class` field in the recording standard.

### GOV-HOTHER-1 {#gov-hother-1}

**H-other / model-misspecification route.** Every important `hypothesis_space_registry.v1.json`
question preserves an explicit route outside its partition. It is not a catch-all after a null; it fires
on pattern-level signals (no leg explains the full outcome; seeds or environments pick incompatible legs;
interaction-only effects; omitted timing or development explains the variance; several legs simultaneously
required; every survivor needs a rescue clause). When it fires, rotate the claim (GOV-ROTATE-1) or expand
the partition as a labelled growth event BEFORE another rescue run. Distinct from failure-autopsy Mode C
(a named discovered mechanism) and GOV-GRAN-1 (claim-side re-graining). As of 2026-09-16 the ledger has 60
questions and zero H-other legs. Proposed implementation surface, not applied: failure-autopsy Step 9b
Mode D check; `h_other_events[]` per question; counted by `check_hypothesis_space_integrity.py`.

### GOV-DELETE-1 {#gov-delete-1}

**Deletion-pressure rule.** Construction earns a later obligation to attempt simplification: once several
validated local repairs coexist, the bundle is periodically challenged by removal, low-complexity
replacement, route consolidation, bridge-capacity reduction and removal of downstream compensation after
an upstream repair. Competence retained after removal is a POSITIVE result. Judged under GOV-CONTRACT-3's
matched-budget test; distinct from GOV-MATCHAUX-1 (admission-time, one objective) and GOV-SUBTRACT-1
(documents, not mechanisms). Registered with its GOV-HELDOUT-1 check stated as only partly non-degenerate
(V3-EXQ-223 is the one clean prior case); it earns its keep when the interface campaign first yields a
bundle to challenge.

### Q-108 {#q-108}

**The minimal-working-intelligence event.** What one non-oracular adaptive-recovery episode would have to
contain (mismatch detection, information-directed adaptation, internal update without a failure label,
behavioural recovery, retention, transfer to a second perturbation, ablation attribution), and which of the
six perturbation classes AR-1..AR-6 is first non-vacuous on the substrate REE actually has. Design seed
only (doctrine sections 10-11); `substrate_conditional`, v4; do not queue from this entry. AR-5 (interface
drift) is blocked on Q-107's missing controlled-drift intervention; AR-4 on the absent provenance-genealogy
substrate; AR-1 (cue remapping) is the nearest V3-expressible class, flagged for `/governance` routing.

## Not registered from this thought

- **Section 3 (developmental history is causal) and section 4 (static legibility is the wrong object)** are
  already owned: ARC-143 / MECH-549 and MECH-547 / MECH-548 / MECH-556 / MECH-561 / ARC-145 / INV-105.
- **Section 7 (the scientific machinery is part of the experimental context)** -- the
  creature / experiment / instrument / governance-interpretation attribution of an apparent CHANGE -- is
  the success-side mirror of GOV-FAILLOC-1's four failure buckets and is proposed to `/governance` as an
  amendment extending that rule's scope from "REE failed" reads to "REE improved" reads, not registered
  as a new rule.
- **The Adaptive Recovery Battery** stays a design seed inside the planning document until enough
  substrate exists to make one perturbation class non-vacuous.
