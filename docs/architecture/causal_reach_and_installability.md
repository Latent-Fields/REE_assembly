---
title: "Causal Reach, Installability, and the Mechanism-Organism Boundary"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 19
status: candidate
status_asof: 2026-08-25
status_claim: ARC-130
---

# Causal Reach, Installability, and the Mechanism-Organism Boundary

**Claim IDs:** ARC-130 (causal-reach ladder) + ARC-131 (installability); companion governance
rules GOV-PATHVALID-1 (positive-control production-path traversal) + GOV-INTERVENE-1
(oracle/non-oracle x silky/oddly-composed intervention taxonomy).
**Subject:** `architecture.mechanism_causal_reach_ladder` / `architecture.installability_as_composition_competence`
**Status:** candidate. Audit/interpretation framework only -- no new substrate, no runtime
instrumentation authorised. **Version-routing is flagged, not settled** (see below).
**Registered:** 2026-08-25
**Depends on:** ARC-120, MECH-480, GOV-FAILLOC-1 (ARC-130); MECH-457, MECH-459, ARC-120, ARC-130
(ARC-131); GOV-FAILLOC-1, ARC-130 (GOV-PATHVALID-1); GOV-PATHVALID-1, GOV-BEHADJ-1, GOV-DIAG-1
(GOV-INTERVENE-1)
**Source:** `docs/thoughts/2026-08-24_causal_reach_installability_and_when_a_mechanism_becomes_part_of_the_organism.md`

---

## Problem

ARC-120 already establishes that behavioural authority in REE is earned, not granted, and
generalises REE's existing gating mechanisms into one developmental sequence: existence ->
representation -> competence -> authority -> behavioural influence. But that sequence stops at
"behavioural influence" -- it has no granularity for what happens *after* a mechanism acquires
authority at one internal boundary. Several live V3 findings show authority acquired at one
selection boundary failing to reach committed behaviour (MECH-480's LOFC/dACC dissociation is the
cleanest existing instance), and separately, a mechanism that passes isolated component-level
validation can still fail to express itself once composed into the whole organism (drowned
signal, vanished preconditions, timing conflicts, insufficient competitive scale).

## Proposal

**ARC-130 -- the causal-reach ladder.** An 8-stage audit projection refining ARC-120's 5-stage
sequence with post-authority granularity: existence, representation, endogenous recruitment,
local operation, competitive authority (non-zero influence is not necessarily *competitive*
influence against the dominant arbitration term), committed throughput (survives any later
selector/latch/commitment boundary), ecological consequence (the changed behaviour has a valid
opportunity to matter in the environment), retention/generalisation. The correct unit for
recording mechanism status is the *furthest stage demonstrated*, not a flat
implemented/not-implemented label. This is an audit projection, not literal computational
topology -- REE is recurrent, distributed, multi-rate.

**ARC-131 -- installability as a dissociable competence.** A component-level PASS establishes that
an operation is *possible*; it does not establish that the whole agent can enter the states in
which the mechanism operates, that the mechanism remains competitive once other mechanisms are
enabled, or that later learning will preserve it. Installability (does the competence appear at
all once the rest of the organism is turned on) is explicitly distinguished from retention (does
competence survive subsequent learning/consolidation once it exists) -- these are logically
independent failure points; a mechanism can pass one and fail the other. MECH-457's
conversion-ceiling frontier is the closest existing instance -- REE governance notes already
informally call it "the competence FLOOR / installability explanandum."

**GOV-PATHVALID-1 -- positive-control production-path traversal.** A load-bearing positive control
that mocks/injects the state immediately downstream of a suspected causal edge can certify that
the *consumer* works given that state, but cannot certify that the *production organism* reaches
that state via its own endogenous pathway. Motivated by a concrete incident: a closure-exclusive
decommitment contract test appeared to pass because its harness directly inserted a committed
trajectory into the state under test, rather than the organism producing that state naturally
(`claims.yaml`'s V3-EXQ-460k `closure_exclusive_decommit_eval` finding is a structurally identical,
independently-reached instance of this exact defect shape).

**GOV-INTERVENE-1 -- the intervention-diagnostic taxonomy.** Diagnostic interventions must be
classified along two independent axes rather than one flat judgment: (1) epistemic content --
oracle (imports privileged, target-correct information; establishes achievable ceilings) vs.
non-oracle (perturbs a suspected variable without supplying the answer; establishes causal
sensitivity); (2) construction -- silky (minimally disruptive, distribution-preserving; localises
threshold/scale/timing failures) vs. oddly-composed (deliberately combines individually-plausible
states that rarely co-occur; stress-tests factorisation and shortcut-dependence). These axes are
orthogonal and must not be collapsed into one enum.

## Explicitly distinct from adjacent claims

- **ARC-120**: extended, not superseded. ARC-120 remains sole owner of the base 5-stage sequence;
  ARC-130 owns the refined post-authority granularity.
- **MECH-457 / MECH-459**: ARC-131 is the *general* installability property; MECH-457 is one
  specific instance (an actor-critic mechanism), and MECH-459 (competence retention) is a distinct
  *temporal* axis, not the same as installability's *compositional* axis. Promoting/demoting
  either MECH claim does not promote/demote ARC-131.
- **GOV-FAILLOC-1**: triages an *observed FAIL* after the fact into REE/mechanism/measures/
  environment buckets. GOV-PATHVALID-1 is upstream of that -- a design-time check on whether a
  *PASS* is entitled to the interpretation it's given.
- **GOV-BEHADJ-1**: its existing "positive, destructive, orthogonal negative control" triad
  classifies perturbations by *intended role*. GOV-INTERVENE-1 classifies interventions by two
  independent *properties* (imported information; construction relative to natural distribution)
  that cut across that role.

## Version-routing flag (needs `/governance` confirmation, not decided here)

Unlike a typical thought-intake registration, all four claims here are scoped `implementation_phase:
v3` / `version_relevance: v3` rather than the default v4/v4_v5 park, because this is an
audit/interpretation framework applicable to already-running V3 mechanisms and failure-autopsy
practice, not a proposal for new substrate. This is an explicit deviation, flagged for a future
governance cycle to confirm -- it could instead park these v4/v4_v5 like the sibling
persistence-taxonomy intake (ARC-128/MECH-497/MECH-498).

**DO NOT build a `MechanismReachTrace` runtime telemetry object from ARC-130** without a separate
build decision -- the source thought hedges this schema itself ("may be useful... not necessarily
as one monolithic runtime object"). Recorded here as an unbuilt instrumentation proposal only.

## Status and next steps

No claim's status, confidence, or evidence record is changed by this registration. Not yet applied
to `.claude/skills/failure-autopsy/SKILL.md` or `/queue-experiment`'s non-degeneracy checklist --
both GOV-PATHVALID-1 and GOV-INTERVENE-1 stay `status: candidate` and should be promoted only
after they have actually changed a real positive-control design or autopsy verdict, per the same
discipline GOV-HELDOUT-1 applies to itself. A duplication/literature audit for ARC-131 vs.
competence retention (MECH-459) is called for by the source thought itself and not yet performed.

See `evidence/planning/thought_intake_2026-08-24_causal_reach_installability_and_when_a_mechanism_becomes_part_of_the_organism.md`
for the full Stage 2 intake, including the novelty table against all cross-referenced claims and
the routing flag for the thought's originating methodological observation (literature-mining
discipline), which was deliberately left unregistered pending a routing decision.
