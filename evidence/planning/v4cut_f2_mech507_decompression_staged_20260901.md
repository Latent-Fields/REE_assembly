# GOV-V4CUT-1 F2 -- staged registration: minimal-v3 trained decompression stage

**Status: AWAITING USER REVIEW.** Nothing in this document has been applied to
`claims.yaml`. Staged by session `metaworker-chip-20260901-v4cut-f2-mech507-trained-decompression`
(chip `chip-20260901-v4cut-f2-mech507-trained-decompression`), 2026-09-01.

## Why staged rather than registered

The dispatch task pointed at `/claim-synthesis` to execute this registration. That skill
does not fit the task mechanically (it decomposes FAIL clusters via a discrimination gate
on failure signatures keyed on `bears_on`/autopsy data; there is no FAIL cluster here --
this is a split proposed by an architectural cut-audit, GOV-V4CUT-1) and, more importantly,
its own contract states: "Proposal-first, governance-touching. Nothing lands in
`claims.yaml` without the user's explicit per-child approval... Not safe headless." This
session is a headless `claude -p` worker with no user to pause for. The sibling F1 session
(GFLAG-0101, `evidence/planning/v4cut_f1_arc134_p0_operator_staged_20260901.md`, landed
REE_assembly `a711317a85`) reached the same conclusion for the same reason and staged
rather than registered; this document follows that precedent for consistency. So: full
evaluation done below (verdict: the split holds, in a narrower form than the audit's own
text suggests), exact proposed registration drafted, staged here for review rather than
applied.

## Verdict on F2 (evaluation)

**The split holds, but not exactly as framed in the audit.** The audit's own grounds
("this is the same repair the P4 training-debt cluster already needs... the minimal
MECH-507 form is not new V4 machinery, it is the principled statement of the P4
remediation") were independently re-verified against the live V3 substrate and the live
registry as of 2026-09-01, and the finding is stronger than the audit states: the pattern
MECH-507 describes is not merely analogous to P4 debt -- it is **already partially built
and already separately registered as v3 work**, just never framed as one claim.

1. **A trained decompression/readout stage already exists in the V3 substrate**, contrary
   to MECH-507's own registration note ("no explicit decompression head exists in
   `ree_core`; ContextMemory read/write today is a fixed-slot lookup with no generative
   decompression stage" -- true, but scoped to E1/ContextMemory specifically).
   `ree-v3/ree_core/predictors/e2_fast.py` implements `E2WorldForward` /
   `e2.world_forward(z_world, action) -> predicted z_world`: exactly the structural pattern
   MECH-507's title names ("z_t decompresses into higher-dimensional predictions and
   candidate sensorimotor futures"), at the z_world compression site (SD-005's E3/
   Hippocampus domain), read throughout `agent.py`'s CEM candidate scoring
   (`e2.world_forward(z0_K, actions_K)`). It is coded and reachable, not a plan.
2. **It already has a registered, TRAINED form: SD-056** (`status: candidate`,
   `implementation_phase: v3`), "E2 world-forward action-conditional divergence
   preservation via auxiliary InfoNCE-style contrastive loss" -- implemented 2026-05-29 in
   `e2_fast.py` + `utils/config.py`, gated behind `e2_action_contrastive_enabled` (default
   `False`, bit-identical OFF). Its own `digestion_note` records the falsifier already
   exists in full (V3-EXQ-569e's script + three named acceptance-criteria fixes) and "was
   never re-queued" -- i.e. the remaining gap to a validated result is re-queuing, not
   building.
3. **The compression-side pairing also already exists as a registered v3 design**: SD-070,
   "z_world P0 anti-collapse encoder-training recipe... supplies the trained encoder that
   SD-031/E2WorldForward P1 and V3-EXQ-783 both require." SD-056 (decompression) and SD-070
   (compression) are already-registered v3 halves of exactly the reciprocal pairing
   MECH-507's title describes, at one site.
4. **This does not make MECH-523(c) stale.** MECH-523 ("no value-shaped objective reaches
   any encoder at all -- `compute_benefit_eval_loss` reads `z_world.detach()`") remains true
   of the DEFAULT-config substrate as of 2026-09-01: SD-056 is flag-gated OFF by default and
   unvalidated, SD-070 is a design, not a landed default. The claim below is not "MECH-523
   is wrong" -- it is "the repair MECH-523(c) implies is owed already has a coded, testable
   V3 path, which is new information worth registering on its own."
5. **A second, distinct site for the same pattern is the audit's actual citation**: the P4
   training-debt cluster (SD-080's zero-gradient `E2.action_object_head`/O, MECH-518's
   dual-role variance contention at O, MECH-517's interface-collapse ordering) is about
   MECH-523's site (a), not site (c) -- a DIFFERENT compression site than SD-056/SD-070
   target. Neither SD-080 nor MECH-518 nor MECH-517 itself asserts "O should get an
   explicit trained decompression/readout stage" as their prescribed remedy; SD-080 is
   diagnostic-only, MECH-517/518 test ordering and diversity effects, not decompression-head
   training. So the audit's own grounding citation is not, on inspection, a restatement of
   an existing claim -- it names debt at a site nothing yet proposes this specific repair
   for.
6. **This clears the bar the audit's own rejections set.** MECH-512 was rejected because
   "no knob exists at any timescale" (`e1_deep.py`) -- structurally unbuildable in V3.
   MECH-508 was rejected because "no v3-minimal form exists that is distinct from existing
   precision instrumentation" -- redundant, no new falsifier. Neither objection applies
   here: the mechanism is not just buildable but partially built (point 1-3), and the
   generalising claim below is distinct from SD-056/SD-070/MECH-523 individually (point 4)
   and from SD-080/MECH-518/MECH-517 individually (point 5) -- none of the six existing
   claims states the general requirement "a compression site is paired with a trained
   decompression stage before ceiling-nulls measured there are interpretable," and none
   connects the z_world existence-proof to the separately-owed O-site repair.

**Narrowing versus the audit's framing:** the audit describes this as "not new V4
machinery, it is the principled statement of the P4 remediation" (implying the new claim
IS the O-site fix). The evidence instead shows the more general form is what is new and
non-redundant, with SD-056/SD-070 as the existence proof and the O-site cluster as a
second, separately-falsifiable instance. The proposed claim below states it at that level
of generality rather than scoping it to O alone.

## Proposed new claim (id provisional -- re-check the actual max at registration time)

`git log` + the live registry put the current max MECH id at 529 as of 2026-09-01. The
sibling F1 staging doc (`v4cut_f1_arc134_p0_operator_staged_20260901.md`) also provisionally
claims MECH-530 for its own proposal. If both F1 and this proposal are approved in the same
pass, only one can actually be MECH-530 -- **allocate both ids at registration time by
re-checking the live max and `git log`, in registration order; do not both assume 530.**
This document uses MECH-531 as its working placeholder to avoid presupposing the collision
is resolved in this proposal's favor.

```yaml
- id: MECH-531
  title: "At least one of REE's designated compression sites (MECH-523) must be paired with an explicit TRAINED decompression/readout stage before representational-ceiling nulls measured there are interpretable as capacity findings -- this is the v3-testable core of MECH-507's reciprocal compression/decompression bridge, independent of the full E1 reframing MECH-507 itself remains scoped to. Two site-specific halves of this pattern already exist as registered but unvalidated/unbuilt v3 work: SD-056 (E2.world_forward trained via a contrastive divergence-preservation loss, coded 2026-05-29 in ree_core/predictors/e2_fast.py, default OFF, never re-queued for validation) supplies the decompression half at the z_world site, paired with SD-070's anti-collapse encoder-training recipe for the compression half at the same site. Separately, the P4 training-debt cluster at E2.action_object_head/O -- SD-080's zero-gradient finding, MECH-518's dual-role variance contention, MECH-517's interface-collapse ordering -- names the same repair owed at a second, independent compression site. This claim asserts the general requirement and is satisfied by confirming it at either site."
  claim_type: mechanism_hypothesis
  subject: representation.compression_site_decompression_pairing
  polarity: asserts
  status: candidate
  live_status:
    reading: candidate/v3_pending
    as_of: 2026-09-01
    needs_review: false
  epistemic_category: standard
  implementation_phase: v3
  v3_pending: true
  version_relevance: v3_v4
  registered_utc: '2026-09-01'
  depends_on:
    - MECH-507  # the full v4/v5 reciprocal-bridge reframing this claim pulls the v3-testable core forward from (SPLIT per GOV-V4CUT-1 F2 / GFLAG-0102)
    - MECH-523  # names the untrained compression sites this claim's "at least one" quantifies over
    - SD-056    # E2.world_forward trained decompression/prediction head -- coded, default OFF, unvalidated; the existence-proof instance at the z_world site
    - SD-070    # z_world anti-collapse encoder-training recipe -- pairs with SD-056 as the compression-side half at the same site
    - SD-080    # E2.action_object_head/O zero-gradient finding -- names the second site this claim's "at least one" could instead be satisfied at
    - MECH-518  # O's dual-role variance contention -- the P4-cluster reason a trained decompression stage is owed at O specifically
    - MECH-517  # interface-before-representation ordering -- the P4-cluster's methodological companion
  location: docs/architecture/selection_relevant_representation.md#mech-531  # NEW anchor to add
  what_would_answer: >
    CONFIRMING (either path suffices -- this claim is about the PAIRING pattern, not about
    which site instantiates it): (1) SD-056 is re-queued and lands with a validated run
    showing E2.world_forward's contrastive loss preserves action-conditional divergence
    (cand_world_pairwise_dist non-degenerate, above the 0.0000 collapse measured pre-fix) AND
    SD-070's anti-collapse encoder recipe is landed/exercised at the z_world site, jointly
    demonstrating a trained compression+decompression pairing in production; OR (2) an
    explicit trained decompression/readout stage is built at O (E2.action_object_head) and
    resolves or measurably improves the SD-080 zero-gradient finding / MECH-518's dual-role
    variance reallocation (ao_M5_r2_explained_by_action_alone moving back toward its
    pre-817a ~0.995 without M6's sign instability), and a representational-ceiling null
    previously measured at O (a V3-EXQ-817a-shaped rerun) becomes reproducibly different
    under the trained-decompression arm versus the frozen baseline.
    FALSIFYING: SD-056/SD-070 land and validate with no measurable effect on any downstream
    ceiling-null's interpretability, AND a trained decompression stage built at O produces
    no measurable change in O's gradient informativeness or in ceiling-null behaviour
    relative to the untrained baseline -- i.e. pairing a compression site with a trained
    decompression stage does not matter, and whatever explains the untrained-site
    pathologies MECH-523 describes is something else entirely.
  notes: >
    Registered from GOV-V4CUT-1 cut-audit finding F2
    (evidence/planning/v4_prerequisite_cut_20260901.md, Section 3), tracked as GFLAG-0102.
    SPLIT off MECH-507: MECH-507 itself is NARROWED to the full reciprocal-bridge reframing
    at E1/ContextMemory specifically -- which its own registration notes confirm does not
    exist in V3 ("ContextMemory read/write today is a fixed-slot lookup with no generative
    decompression stage") -- and remains implementation_phase v4, version_relevance v4_v5.
    Distinct from SD-056, SD-070 and MECH-523 individually: none of the three states the
    general requirement that a compression site be PAIRED with a trained decompression stage
    before ceiling-nulls measured there are interpretable, and none connects the z_world-site
    existence proof to the separately-owed O-site repair (SD-080/MECH-518/MECH-517). The
    audit's own grounding text reads as though the P4/O cluster IS this claim's minimal form;
    on inspection SD-080/MECH-518/MECH-517 do not themselves prescribe "train a decompression
    head at O" -- this claim is the connective, testable statement that was missing, not a
    restatement of an existing one.
```

### Proposed follow-on edits (also staged, not applied)

- **MECH-507's `notes` field**: append, once the sibling claim's actual id is allocated:
  "SPLIT 2026-09-0X per GOV-V4CUT-1 F2 (GFLAG-0102): the v3-testable core -- at least one
  compression site paired with a trained decompression/readout stage -- is pulled forward
  as MECH-5XX. This claim narrows to the FULL reciprocal-bridge reframing at E1/
  ContextMemory specifically; the 'DO NOT build in V3' caution above continues to apply to
  that scope exactly as registered." No change to MECH-507's `title`, `claim_type`,
  `status`, or `depends_on`.
- **MECH-523's `depends_on`**: once the sibling claim exists, consider adding it as a
  reverse-reference (MECH-523 names the sites; the sibling claim is the repair-pattern
  claim over those sites) -- optional, not required for correctness.
- **GFLAG-0102**: resolve with a note naming the registered id and this staging trail, once
  the user approves and the claim actually lands. Until then it stays open (this document
  does not resolve it).

## What is NOT proposed

No change to MECH-507's `title`, `claim_type`, `status`, `epistemic_category`, or
`depends_on`. No change to SD-056, SD-070, SD-080, MECH-517, MECH-518, or MECH-523's core
assertions -- this proposal only adds one new connective claim and a scoping note on
MECH-507. No build work is proposed or authorized by this document; re-queuing SD-056 or
building a decompression head at O are `/queue-experiment` / `/implement-substrate` actions
for a later session, contingent on this claim being approved first.
