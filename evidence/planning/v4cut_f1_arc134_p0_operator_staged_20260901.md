# GOV-V4CUT-1 F1 -- staged registration: minimal-v3 P0 grain operator

**Status: AWAITING USER REVIEW.** Nothing in this document has been applied to
`claims.yaml`. Staged by session `v4cut-f1-arc134-p0-grain-operator` (chip
`chip-20260901-v4cut-f1-arc134-p0-grain-operator`), 2026-09-01T16:03:35Z.

## Why staged rather than registered

The dispatch task pointed at `/claim-synthesis` to execute this registration. That skill
does not fit the task mechanically (it decomposes FAIL clusters via a discrimination gate
on failure signatures; there is no FAIL cluster here -- this is a split proposed by an
architectural cut-audit, GOV-V4CUT-1) and, more importantly, its own contract states:
"Proposal-first, governance-touching. Nothing lands in `claims.yaml` without the user's
explicit per-child approval... Not safe headless." This session is a headless
`claude -p` worker with no user to pause for. The closest real precedent for this exact
kind of split -- MECH-521/522, 2026-08-26 -- was itself explicitly recorded as
"user-gated" (MECH-521's own notes: "SPLIT 2026-08-26 by thought-digestion wave 1
(session insights-7fd98a-digestion, user-gated)"). Registering new, permanent claims.yaml
content unilaterally, headless, would depart from that precedent. So: full evaluation
done below (verdict: the split holds), exact proposed registration drafted, staged here
for review rather than applied.

## Verdict on F1 (evaluation)

**The split holds.** Evidence, verified against `claims.yaml` as of 2026-09-01:

1. **ARC-134's own `what_would_answer` already isolates P0 as a distinct, near-term
   buildable precondition**, separate from the richer dynamic-regrain claim: "(P0) AN
   ENDOGENOUS GRAIN OPERATOR MUST EXIST -- it does not... This is the largest disanalogy
   with the policy axis, where the operator was BUILT (2026-07-24) before the claim was
   scored," and calls exposing per-token match cost "the cheapest thing owed."
2. **The two "DO NOT build in V3" cautions in the registry (MECH-521's notes, and
   ARC-134's own notes) both target the SAME thing**: MECH-521's per-population settling
   dynamics ("a per-population formulation (see MECH-521) is the version that survives
   [the Badre & Nee 2018 objection]. DO NOT build in V3."). Neither caution scopes over a
   fixed-capacity, non-dynamically-regulated merge/split operator's mere existence.
3. **MECH-529 (already registered `version_relevance: v3_v4`) lists ARC-134's P0 as its
   own explicit non-degeneracy precondition**: "a corrigible representational grain
   (ARC-134 P0 merge/split operator landed and exercised -- without it the categories are
   environment-authored and the question cannot be posed)." A claim already straddling the
   v3/v4 boundary is blocked today without this operator -- concrete, present-tense
   testability evidence, not only an inference from V4's five primitives.
4. **The gap is a scoped, buildable engineering task**, not a probe-gated unknown:
   `ree_core/entities/object_file_buffer.py` has only `_birth`, `_enforce_capacity`,
   `_evict_stale`; no merge/split; matching is strict 1:1 greedy. This is `complicated
   (buildable)` in the work-graph debt vocabulary, directly analogous to ARC-070's
   policy-side operator (built 2026-07-24 before that claim was scored).
5. **A falsifier ladder is draftable using machinery ARC-134 already specifies**: MECH-126's
   overmerge/oversplit taxonomy as the DV, and a yoked/rate-matched random-regrain control
   (mirroring ARC-134's own L3 falsifier) to distinguish "corrigible by consequence
   evidence" from "fires but uninformatively."

This satisfies the dispatch brief's testability bar: the minimal v3 form is genuinely
buildable and falsifiable on the V3 substrate as it exists, using an existing DV
(MECH-126) and an existing falsifier-design pattern (ARC-134's own L3 yoked-control
logic) -- it is not a pull-forward of something nothing can test.

## Proposed new claim (id provisional -- allocate the actual next-free MECH id at
registration time; MECH-529 is the current max as of this writing, so MECH-530 is the
likely id, but re-check `git log` + current max before registering)

```yaml
- id: MECH-530
  title: "A merge/split operator over the existing EntityObservation boundary must exist and be corrigible by consequence evidence, at FIXED capacity -- no dynamic per-population regulation, no settling competition. This is the minimal P0 substrate floor ARC-134 and MECH-529 both name as currently absent: `ree_core/entities/object_file_buffer.py` has no merge or split of tokens anywhere, and matching is strict 1:1 greedy over a caller-built List[EntityObservation]. Distinguished from MECH-521/MECH-522: this claim asserts only that a corrigible operator exists and responds to consequence-divergence evidence (MECH-126's overmerge/oversplit taxonomy), not that occupancy is an emergent order parameter of a settling competition, and not that capacity itself is dynamically regulated -- those remain MECH-521/522's richer, explicitly v4/v5-deferred claims."
  claim_type: mechanism_hypothesis
  subject: entities.corrigible_grain_operator_p0
  polarity: asserts
  status: candidate
  live_status:
    reading: candidate/v3_pending/substrate_conditional
    as_of: 2026-09-01
    needs_review: false
  epistemic_category: substrate_conditional
  implementation_phase: v3
  v3_pending: true
  version_relevance: v3_v4
  registered_utc: '2026-09-01'
  depends_on:
    - ARC-134   # parent claim this splits the P0 substrate floor off of
    - MECH-126  # overmerge/oversplit failure taxonomy -- supplies the DV
    - MECH-045  # ObjectFileBuffer -- the only V3 site capacity and occupancy coexist at today
    - ARC-006   # binding substrate
    - ARC-080   # object-identity definition the operator's tokens must respect
    - ARC-070   # policy-axis precedent -- the analogous operator, already built 2026-07-24
  location: docs/architecture/selection_relevant_representation.md#mech-530  # NEW anchor to add
  what_would_answer: >
    NON-DEGENERACY PRECONDITION: the operator must be BUILT (merge + split over
    EntityObservation tokens, replacing the current strict 1:1 greedy match) and exercised
    at fixed capacity -- no capacity change, no per-population coupling/settling dynamics
    (those are MECH-521/522's scope, explicitly excluded here). A consequence-evidence
    signal must be wired: MECH-126's overmerge/oversplit taxonomy, or an equivalent
    prediction/consequence-divergence signal, available to drive correction.
    CONFIRMING: the operator's merge/split decisions track genuine consequence-divergence
    evidence (MECH-126 DV pair: overmerge_rate, oversplit_rate) with a net error reduction
    versus a YOKED, RATE-MATCHED RANDOM-REGRAIN control -- same number of merge/split
    events at the same ticks, targets chosen at random among eligible tokens (mirrors
    ARC-134's own L3 falsifier design, which exists precisely to distinguish "regrains" from
    "regrains informatively"). Capacity must remain fixed throughout (a manipulation check
    that no dynamic regulation crept in).
    FALSIFYING (any one): the operator's corrections are statistically indistinguishable
    from the yoked random control on both MECH-126 DVs (informationless regrain); the
    operator cannot be built/exercised without introducing per-population dynamics or
    dynamic capacity (collapses into MECH-521's scope, meaning this claim has no distinct
    minimal form); or building it requires a demand-manipulation environment ARC-134's own
    P2 precondition says does not yet exist (would mean the operator cannot even be
    exercised, not merely that it fails -- a substrate-not-ready result, not a falsification).
    EXPLICITLY NOT ASSERTING (MECH-521/522's scope, deferred v4/v5, unchanged by this
    claim): occupancy as an emergent order parameter of a coupling-vs-lateral-inhibition
    settling competition; dynamic/derived capacity; ephaptic coupling-constant
    specialisation. MECH-521's own notes ("DO NOT build in V3. DO NOT queue an
    experiment.") continue to apply to that scope exactly as registered.
  notes: >
    Registered from GOV-V4CUT-1 cut-audit finding F1
    (evidence/planning/v4_prerequisite_cut_20260901.md, Section 3), tracked as GFLAG-0101.
    SPLIT off ARC-134: ARC-134 itself (the full "grain rescales with circumstance,
    demand-sensitive" claim) and MECH-521/522 (settling-competition dynamics) are
    UNCHANGED -- both remain implementation_phase: v4, version_relevance: v4_v5. This claim
    is additive, asserting only the P0 substrate floor's existence and corrigibility.
    Rationale for a MECH id rather than an ARC id: this is a mechanism-level operator claim
    (parallel in kind to MECH-521, MECH-507), not itself an architectural commitment (ARC-134
    is the commitment this operator is a precondition for testing).
```

### Proposed follow-on edits (also staged, not applied)

- **ARC-134's `notes` field**: append a cross-reference once MECH-530 (or whatever id is
  actually allocated) is registered, e.g. "P0 (endogenous grain operator existence +
  corrigibility) split forward as MECH-530, 2026-09-0X, per GOV-V4CUT-1 F1 -- see that
  claim for the minimal-v3 falsifier. This claim's own richer demand-sensitivity assertion
  (P1-P3, the full L1/L2/L3 ladder) is unaffected and stays v4."
- **MECH-529's `depends_on`**: currently lists `ARC-134  # endogenous perceptual grain P0
  -- grain must be CORRIGIBLE for this loop to have a substrate`. Once MECH-530 exists,
  this line should point at MECH-530 instead (or in addition -- MECH-529's actual
  dependency is on the P0 operator's existence, which is now MECH-530's scope precisely,
  not ARC-134's broader claim).
- **GFLAG-0101**: resolve with a note naming the registered id and this staging trail,
  once the user approves and the claim actually lands.

## What is NOT proposed

No change to MECH-521, MECH-522, or ARC-134's `claim_type` / `status` / `implementation_phase`
/ `version_relevance` fields. Those three claims are correct as they stand and this
proposal does not touch their core assertions.
