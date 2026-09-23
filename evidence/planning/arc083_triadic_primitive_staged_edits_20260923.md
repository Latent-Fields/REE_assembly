# ARC-083 follow-on: staged edits (ARC-150 triadic co-reference primitive)

**Status:** APPLIED 2026-09-23 as REE_assembly 20792df26d (ARC-150), under user-authorised --allow-overlap. Originally STAGED, NOT APPLIED. Drafted 2026-09-23 by session infallible-elion-289944 for
chip `chip-20260923-arc083-triadic-primitive` (follow-on to GFLAG-0309). Not applied because
`REE_assembly/docs/claims/claims.yaml` was owned by `governance-pause-20260923-1741` at the time
(task_claim.py arbitration, exit 3). This doc exists so the work survives the session.

**Apply this ONLY after** `task_claim.py check --resources REE_assembly/docs/claims/claims.yaml`
exits 0, and only if `grep -n triadic` on ARC-083 in claims.yaml still finds nothing (the claims
script aborts on its own if it does). The id is allocated AT WRITE TIME by `apply_claims.py`
(next free ARC-nnn); pass the id it prints to the other two scripts. `ARC-150` below is just the
id the dry run got.

## What the three edits do

1. **claims.yaml** (`apply_claims.py`): registers the new claim (triadic co-reference / declarative
   joint attention, on ARC-080 slot allocation); adds it to ARC-083 `depends_on`; re-annotates
   ARC-083's SD-039 edge; aligns ARC-083's leftover REQUIRES paragraph with the weakened title;
   adds ARC-083's missing `notes` field (its title already says "See notes"), including
   GFLAG-0309 disposition (b) for SD-039 = CANDIDATE for the motivational-weighting half of
   person-permanence only, not adopted as PILLAR 1, needs lit. No status/phase change.
2. **mirror_modelling_other_self_v5_plan.md** (`apply_plan.py`): MIRROR-1 drops the OBJ-2 + OBJ-3
   gate for the new claim; MIRROR-7 keeps SELF-7 on INV-064's own authority only; MIRROR-2's
   SELF-1 gate is deliberately UNCHANGED (mechanistic: ARC-010 reuses the self-model); roadmap
   note, prose, table row, source table and decision log updated.
3. **docs/architecture/arc_080_object_representation_primitive.md** (`apply_doc.py`): PILLAR 4
   rows and ordering diagram softened; anchored section for the new claim; Related Claims line.

## Dry-run results (2026-09-23, against live files)

- claims.yaml: 1185 -> 1186 claims, +ARC-150, only ARC-083 changed; validate_claims --strict
  0 errors (17 warnings, all pre-existing, none on ARC-083/150); ASCII-clean.
- v5 plan: check_plan_frontmatter --strict OK; check_plan_status_table_sync 0 findings.
- arc_080 doc: 32 changed lines, all anchors matched once.

## How to apply

Save each block below to a scratch dir (apply_claims.py reads `new_claim.yaml` and
`arc083_notes.txt` from its own directory), then:

```bash
A=/Users/dgolden/REE_Working/REE_assembly; D=$(date -u +%Y-%m-%d)
NID=$(/opt/local/bin/python3 apply_claims.py $A/docs/claims/claims.yaml $D)
/opt/local/bin/python3 apply_plan.py $A/evidence/planning/mirror_modelling_other_self_v5_plan.md $NID $D
/opt/local/bin/python3 apply_doc.py $A/docs/architecture/arc_080_object_representation_primitive.md $NID
/opt/local/bin/python3 $A/scripts/validate_claims.py --strict
/opt/local/bin/python3 $A/scripts/check_plan_frontmatter.py --strict
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/ree_commit.py --repo REE_assembly --push \
  -m "ARC-083 follow-on: register $NID triadic co-reference primitive; soften v5 readiness gates" -- \
  docs/claims/claims.yaml evidence/planning/mirror_modelling_other_self_v5_plan.md \
  docs/architecture/arc_080_object_representation_primitive.md
```

Then mark this doc APPLIED (status line) with the landing sha.

## `new_claim.yaml`

```yaml
- id: __NEWID__
  title: >-
    Triadic co-reference primitive (declarative joint attention / synchronic two-slot identification):
    the agent can hold its OWN slot and ONE OTHER agent's slot simultaneously bound to a SINGLE
    shared object referent, for no instrumental reason. This relational self-other-object binding --
    not a stable self (ARC-081) and not a generic object-persistence buffer (ARC-080 PILLAR 1) -- is
    the developmental prerequisite otherness inference (ARC-083) and theory of mind actually run
    through. It sits on ARC-080's slot-allocation machinery as a binding operation over two
    concurrently-live slots plus one object token.
  claim_type: architectural_commitment
  subject: representation.triadic_self_other_object_coreference
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v4
  v3_pending: false
  claim_level: architectural
  version_relevance: v4_v5
  registered_utc: '__DATE__'
  location: docs/architecture/arc_080_object_representation_primitive.md#__NEWIDLOWER__
  depends_on:
    - ARC-080    # slot-allocation machinery -- the primitive binds two concurrently-live slots + one object token
    - ARC-010    # the other-slot being bound is the mirror-modelled other (consumer and co-substrate)
  literature_anchors:
    - targeted_review_arc_083
  functional_restatement: >
    WHAT IT ASSERTS. A distinct relational capacity: two agent slots (self, other j) held live AT THE
    SAME TIME and co-bound to one shared object referent -- "I see that you and I are attending to
    THAT". Behavioural signature in humans: DECLARATIVE pointing (~12 months), where the infant directs
    another's attention to a thing in order to share it, not to obtain it. IMPERATIVE pointing (a
    request) is the matched control: same motor form, dyadic self->object with the other as a tool,
    no shared reference.

    WHY IT IS A SEPARATE PRIMITIVE AND WHERE IT SITS. It is neither a stable self (ARC-081 PILLAR 2)
    nor object persistence (ARC-080 PILLAR 1). It is a BINDING OPERATION over the ARC-080 object-file
    machinery: allocation of a second agent slot concurrent with the self slot, plus a co-reference
    link from both to one object token. ARC-083 (per-other slot) supplies the other slot's CONTENT;
    this primitive supplies the RELATION that makes that slot usable for otherness inference.

    BIOLOGY FIRST (targeted_review_arc_083, 2026-09-17, REE_assembly 06fa0a6183):
    (1) Sodian + Kristen-Antonow 2015 Dev Psychol -- the only confound-controlled longitudinal design
        in the pull (n=83, 12mo->50mo, gender + language controlled): 12-month DECLARATIVE pointing
        predicted 50-month false belief; imperative pointing did not; mirror self-recognition and
        level-1 perspective taking were both correlated with joint attention but mediated NONE of the
        path. The triadic act carried the route; the self-representational variable did not.
    (2) Bischof-Kohler 2012 -- the SUPPORTING source for the old self-stability prerequisite -- names
        its own mechanism as SYNCHRONIC IDENTIFICATION (holding self and other simultaneously in view),
        which is this relational two-slot capacity, not self-stability per se.
    (3) Danjo et al. 2018 (rat CA1) + Omer et al. 2018 (bat CA1), independent labs, same issue of
        Science: self and other positions are "jointly and discretely encoded" in ONE hippocampal
        population -- the neural format a concurrent two-slot binding over shared map/object machinery
        would use (and the reason this is placed on ARC-080's machinery, not in a separate social
        module).
    A supporting and a weakening source converging on the same correction is the main reason to
    register this rather than leave it as prose in GFLAG-0309.

    SCOPE / GUARD. architectural_commitment, substrate_conditional -- promote/demote suppressed; no
    code, no experiment. V4 phase to match ARC-083 (inherits ARC-083's v4 -> v5 generation flag in
    mirror_modelling_other_self_v5_plan; both are intrinsically social). Must NOT enter V3 closure.
  what_would_answer: |
    NON-DEGENERACY PRECONDITION: a multi-agent substrate (ARC-047 SocialGridWorld or successor) with at
    least one other agent, a shared object the other can attend to, and an attention/orientation
    readout for BOTH agents -- plus ARC-080 slots able to hold a second agent slot concurrently. Without
    a second agent whose attention is observable, the primitive cannot be exercised and any null is
    vacuous.
    CONFIRMING: agents with the triadic binding available acquire otherness inference (MIRROR-1
    OTHER_SELFLIKE tagging) and downstream other-state prediction faster or more robustly than agents
    lacking it, AND a readout of "self and other co-attending the same token" predicts later
    other-modelling competence better than a self-stability readout does (the Sodian 2015 structure,
    reproduced in-agent).
    FALSIFYING: otherness inference and other-state prediction develop equally well with the triadic
    binding lesioned (only dyadic self->object and other->object tracking available); or the
    self-stability readout, not the co-reference readout, carries the predictive path.
    SUBSTRATE: NOT BUILT. No multi-agent environment in ree_core; no concurrent second agent slot.
    Registration is not build authorisation.
  notes: >-
    Registered __DATE__ by chip chip-20260923-arc083-triadic-primitive (session infallible-elion-289944)
    as the owed follow-on (a) of GFLAG-0309 (resolved 2026-09-23, governance-flags-20260923, user
    decision rec-20260923-79832e4a: weaken ARC-083's REQUIRES to an ordering). ARC-083 depends_on now
    names this claim as its developmental prerequisite in place of the demoted ARC-081 gate.
    Existing-claim check before minting: claims.yaml has no joint-attention / triadic / co-reference
    claim. ARC-099 (language-bootstrap contract) lists "joint attention" in its enabling-condition
    inventory with no node behind it, and language_emergence_bootstrap_v6_plan LANG-4 treats joint
    attention as an "immediate consequence" of MIRROR-1. The Sodian 2015 ordering puts it the other
    way round -- joint attention PRECEDES and predicts other-modelling -- so this claim is the
    upstream node both of those point at, not a consequence of MIRROR-1. Neither ARC-099 nor the v6
    plan was edited here; re-pointing them is follow-on.
    Caveats carried from the pull: a mediation null (Sodian) is not a dissociation, and n=83 over 38
    months can hide a modest mediated effect; the hippocampal papers test one other agent, so the
    PLURAL (several concurrent other slots) is untested.
```

## `arc083_notes.txt`

```text
  notes: >-
    LITERATURE BASIS FOR THE 2026-09-23 WEAKENING (GFLAG-0309; targeted_review_arc_083, REE_assembly
    06fa0a6183; user decision rec-20260923-79832e4a). Weakening: Kartner/Keller/Chaudhary 2010
    (19mo Delhi vs Berlin: matched prosocial behaviour with the mirror-self-recognition link absent);
    Sodian+Kristen-Antonow 2015 (n=83, 12->50mo, controlled: neither mirror self-recognition nor
    level-1 perspective taking mediates the declarative-pointing -> false-belief path); Slaughter+Boh
    2001 (mother permanence outruns object permanence in the same infants -- REVERSES the PILLAR 1
    before PILLAR 4 ordering). Supporting: Bischof-Kohler 2012 (one-sided self-recognition/empathy
    contingency, but its own mechanism is synchronic identification, i.e. relational); Lucca et al.
    2025 supports only by subtraction (Hamlin 2007 non-replication). Wittmann 2016 (structured,
    context-signed self-other contamination in area 9) constrains the slot rather than the ordering:
    a PILLAR 4 build needs an explicit signed self-other coupling term.
    DISPOSITION (a) FOLLOW-ON, 2026-09-23 (chip-20260923-arc083-triadic-primitive): both the
    supporting and the weakening sources point at a triadic self+other+object binding rather than at
    ARC-081 self-stability. Registered as __NEWID__ and wired into depends_on as the developmental
    prerequisite. ARC-081 stays in depends_on as a soft default ordering only.
    DISPOSITION (b), 2026-09-23 -- IS SD-039's MOTIVATIONAL GHOST BANK THE RIGHT PRIMITIVE FOR
    PERSON-PERMANENCE? Verdict: CANDIDATE for the motivational-WEIGHTING half only; NOT adopted as
    PILLAR 1; NEEDS LIT before any stronger reading. For: Slaughter+Boh 2001 has the motivationally
    loaded entity persisting through longer occlusion than an inanimate one, which is what a
    wanting/arousal payload preserved past invalidation (SD-039, live in V3, V3-EXQ-494) would
    produce; the functional_restatement's "not a true object-file persistence buffer" treated that
    as a shortfall when it may be the operative mechanism. Against: SD-039 snapshots a GOAL STATE,
    not an ENTITY TOKEN -- it preserves "what I wanted", not "who is there" -- and ARC-083's slot is
    token-keyed, so the bank cannot by itself carry an other's identity through occlusion. And the
    source is thin: 17 completing infants, and Jackson/Campos/Fischer 1978's task-demand objection to
    the whole person/object decalage literature is unanswered. Working reading: person-permanence =
    token persistence (PILLAR 1 machinery) x motivational weighting (an SD-039-like payload on the
    token), with the weighting lengthening survival for significant others. What would move it: a
    targeted pull on person-vs-object permanence after 1978 and on whether attachment salience
    extends object persistence generally; architecturally, whether attaching an SD-039-style wanting
    payload to an ARC-080 token lengthens its occlusion survival. Not a claims.yaml status change;
    SD-039 itself unedited.
```

## `apply_claims.py`

```python
"""Apply the ARC-083 triadic-primitive edits to claims.yaml.

Usage: apply_claims.py <claims.yaml path> <UTC date YYYY-MM-DD>
Allocates the next ARC id from the file it is given (write-time allocation),
prints it, and rewrites the file in place. Pure string surgery -- every anchor
must match exactly once or it aborts without writing.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
path = Path(sys.argv[1])
date = sys.argv[2]
text = path.read_text(encoding="utf-8")

ids = [int(m) for m in re.findall(r"^- id: ARC-(\d+)$", text, re.M)]
new_id = "ARC-%03d" % (max(ids) + 1)


def once(old, new):
    global text
    n = text.count(old)
    if n != 1:
        sys.exit("ABORT: anchor matched %d times: %r" % (n, old[:80]))
    text = text.replace(old, new)


# 1. ARC-083 block bounds
start = text.index("\n- id: ARC-083\n") + 1
end = text.index("\n- id: ", start + 5) + 1
block = text[start:end]
if "triadic" in block.lower():
    sys.exit("ABORT: ARC-083 already mentions triadic -- work may be done")

# 2. depends_on: add the new primitive, re-annotate SD-039
once(
    "    - SD-039     # PREREQUISITE (DEV-NEED-021, partial) -- object-persistence substrate (ghost-goal bank; true object permanence is PILLAR 1, unregistered/future)\n",
    "    - SD-039     # CANDIDATE motivational-weighting half of person-permanence, NOT a substitute for token persistence\n"
    "                  # (GFLAG-0309 disposition (b), 2026-09-23: see notes). True object permanence is still PILLAR 1, unregistered/future.\n"
    "    - %s    # DEVELOPMENTAL PREREQUISITE (GFLAG-0309 disposition (a) follow-on, 2026-09-23): triadic co-reference /\n"
    "                  # declarative joint attention -- the relational self+other+object binding the evidence actually routes\n"
    "                  # otherness inference through (Sodian+Kristen-Antonow 2015), replacing ARC-081 as the prerequisite.\n" % new_id,
)

# 3. functional_restatement: bring the REQUIRES paragraph into line with the weakened title
once(
    "    developmental_needs_register DEV-NEED-021, otherness inference REQUIRES object\n"
    "    persistence + self-stability, so PILLAR 1 (permanence) and PILLAR 2 (self,\n"
    "    ARC-081) are prerequisites for PILLAR 4. Object permanence is only PARTIALLY\n"
    "    present (the SD-039 motivational ghost bank, not a true object-file persistence\n"
    "    buffer);",
    "    developmental_needs_register DEV-NEED-021, otherness inference was said to REQUIRE\n"
    "    object persistence + self-stability. WEAKENED 2026-09-23 (GFLAG-0309): PILLAR 1\n"
    "    (permanence) and PILLAR 2 (self, ARC-081) are a DEFAULT BUILD ORDERING for PILLAR 4,\n"
    "    not prerequisites; the prerequisite the evidence supports is the triadic co-reference\n"
    "    primitive %s. Object permanence is only PARTIALLY present (the SD-039 motivational\n"
    "    ghost bank, not a true object-file persistence buffer -- though see notes: the ghost\n"
    "    bank is a CANDIDATE for the motivational half of person-permanence);" % new_id,
)

# 4. notes: ARC-083's title says "See notes" but it had no notes field
notes = (HERE / "arc083_notes.txt").read_text(encoding="utf-8").replace("__NEWID__", new_id)
once(
    "  location: docs/architecture/arc_080_object_representation_primitive.md\n\n- id: MECH-340\n",
    notes + "  location: docs/architecture/arc_080_object_representation_primitive.md\n\n"
    + (HERE / "new_claim.yaml").read_text(encoding="utf-8")
    .replace("__NEWIDLOWER__", new_id.lower()).replace("__NEWID__", new_id).replace("__DATE__", date)
    + "\n- id: MECH-340\n",
)

path.write_text(text, encoding="utf-8")
print(new_id)
```

## `apply_plan.py`

```python
"""Patch mirror_modelling_other_self_v5_plan.md to match the weakened ARC-083.
Usage: apply_plan.py <plan path> <NEW_ID> <YYYY-MM-DD>
"""
import sys
from pathlib import Path

path = Path(sys.argv[1])
nid, day = sys.argv[2], sys.argv[3]
text = path.read_text(encoding="utf-8")


def once(old, new):
    global text
    n = text.count(old)
    if n != 1:
        sys.exit("ABORT: anchor matched %d times: %r" % (n, old[:80]))
    text = text.replace(old, new)


# frontmatter header
once("  last_updated: 2026-06-10\n  scope_claims: [ARC-010,",
     "  last_updated: %s\n  scope_claims: [ARC-010," % day)
once("ARC-047, ARC-083, INV-005]", "ARC-047, ARC-083, %s, INV-005]" % nid)
once(
    "    Otherness inference REQUIRES object-permanence AND a stable self, both V4 --\n"
    "    so every node here carries a cross_plan_link or readiness_gate back to a V4\n"
    "    sibling node (object_representation_v4:OBJ-2 permanence, OBJ-3/SELF-* self),\n",
    "    Otherness inference TYPICALLY DEVELOPS AFTER object-permanence and a stable\n"
    "    self (weakened from REQUIRES 2026-09-23, GFLAG-0309: a default build ordering,\n"
    "    not a gate); the developmental prerequisite the evidence supports is %s\n"
    "    triadic co-reference. Nodes still carry cross_plan_links back to V4 siblings\n"
    "    (object_representation_v4:OBJ-2 permanence, OBJ-3/SELF-* self) as ordering,\n"
    "    and MIRROR-2's SELF-1 gate stays a hard gate on its own MECHANISTIC ground\n"
    "    (ARC-010 reuses the self-model, so one must exist to reuse),\n" % nid,
)

# MIRROR-1
once(
    '      blocking_on: "DEV-NEED-021 prerequisite: others-as-object slots (object_representation_v4:OBJ-5) require object-permanence (OBJ-2) + self-stability (OBJ-3/self_model_v4) to exist first. There is no entity to tag OTHER_SELFLIKE until a token-keyed other-object slot can hold it."\n',
    '      blocking_on: "There is no entity to tag OTHER_SELFLIKE until a token-keyed other-object slot (object_representation_v4:OBJ-5) can hold it, and no route to otherness inference until %s triadic co-reference can bind that slot and the self slot to one shared object. OBJ-2 permanence + OBJ-3/self_model_v4 self-stability typically come first but are NOT a gate (DEV-NEED-021 weakened 2026-09-23, GFLAG-0309)."\n' % nid,
)
once(
    '        - "object_representation_v4:OBJ-5 (others-as-object: per-agent token-keyed slot) -- the slot MECH-031\'s tag attaches to; itself gated on OBJ-2 permanence + OBJ-3 self"\n',
    '        - "object_representation_v4:OBJ-5 (others-as-object: per-agent token-keyed slot) -- the slot MECH-031\'s tag attaches to; OBJ-2 permanence + OBJ-3 self are its default build ORDERING, not a gate (GFLAG-0309)"\n'
    '        - "%s triadic co-reference (declarative joint attention): self slot + other slot concurrently live and co-bound to one object token, on ARC-080 slot allocation -- the developmental prerequisite Sodian+Kristen-Antonow 2015 found carries the path to theory of mind (self-recognition mediated none of it)"\n' % nid,
)
once(
    '      last_updated: 2026-06-10\n      completion_note: "First V5 social step:',
    '      last_updated: %s\n      completion_note: "First V5 social step:' % day,
)

# MIRROR-7: keep the INV-064 gate on its own authority, drop the DEV-NEED-021 justification
once(
    "and the INV-064 maturational gate (self_model_v4:SELF-7) confirming self-stability precedes social depth.\"",
    "and the INV-064 maturational gate (self_model_v4:SELF-7). That gate is held on INV-064's own authority; its former DEV-NEED-021 'stable self must precede' justification was weakened to an ordering 2026-09-23 (GFLAG-0309).\"",
)
once(
    '        - "self_model_v4:SELF-7 / INV-064 maturational gate: a stable self must precede this social depth (DEV-NEED-021)"\n'
    "      last_updated: 2026-06-10\n",
    '        - "self_model_v4:SELF-7 / INV-064 maturational gate (held on INV-064\'s own authority; the DEV-NEED-021 \'stable self must precede\' reading is a default ordering since 2026-09-23, GFLAG-0309)"\n'
    "      last_updated: %s\n" % day,
)

# body prose
once(
    "DEV-NEED-021 spine: **self -> objects -> OTHERS -> language**. Otherness\n"
    "inference is not a free-standing capability -- it REQUIRES object-permanence\n"
    "(so an other persists as a trackable entity through occlusion) and a stable\n"
    "self (so there is a self-model to mirror FROM). Both are V4.",
    "DEV-NEED-021 spine: **self -> objects -> OTHERS -> language**. Otherness\n"
    "inference is not a free-standing capability. It TYPICALLY DEVELOPS AFTER\n"
    "object-permanence and a stable self -- a default ordering, not a requirement\n"
    "(weakened 2026-09-23, GFLAG-0309) -- and the prerequisite the developmental\n"
    "evidence supports is %s triadic co-reference (self + other co-bound to one\n"
    "object). Mirroring (MIRROR-2) separately needs a self-model to mirror FROM;\n"
    "that is a mechanistic dependency and stays a gate. All of these are V4." % nid,
)
once(
    "| MIRROR-1 | otherness inference / OTHER_SELFLIKE tag | MECH-031, MECH-032 | V5 (entry) | OBJ-5 others-as-object slot (needs OBJ-2 + OBJ-3) |",
    "| MIRROR-1 | otherness inference / OTHER_SELFLIKE tag | MECH-031, MECH-032 | V5 (entry) | OBJ-5 others-as-object slot + %s triadic co-reference (OBJ-2 + OBJ-3 default ordering only) |" % nid,
)
once(
    "  reported in `generation_flags[]` (current v4 -> recommended v5). ARC-083's\n"
    "  *prerequisites* (object-permanence PILLAR 1, self-stability PILLAR 2) stay\n"
    "  V4 -- only the others-as-object endpoint is social.",
    "  reported in `generation_flags[]` (current v4 -> recommended v5). ARC-083's\n"
    "  default-ordering predecessors (object-permanence PILLAR 1, self-stability\n"
    "  PILLAR 2) stay V4 -- only the others-as-object endpoint is social. Its\n"
    "  prerequisite %s (triadic co-reference) is registered v4 alongside it and\n"
    "  inherits the same v4 -> v5 flag." % nid,
)
once(
    "| [docs/architecture/developmental_needs_register.md](../../docs/architecture/developmental_needs_register.md) DEV-NEED-021 | otherness inference REQUIRES object-permanence + self-stability (the V4 prerequisites) |",
    "| [docs/architecture/developmental_needs_register.md](../../docs/architecture/developmental_needs_register.md) DEV-NEED-021 | otherness inference typically develops after object-permanence + self-stability (default ordering; weakened from REQUIRES 2026-09-23, GFLAG-0309) |\n"
    "| claims.yaml %s + evidence/literature/targeted_review_arc_083/ | triadic co-reference primitive -- the developmental prerequisite for MIRROR-1 |" % nid,
)

# decision log
text = text.rstrip("\n") + "\n" + (
    "- **%s** -- Readiness gates re-pointed to match the weakened ARC-083 (GFLAG-0309,\n"
    "  user decision rec-20260923-79832e4a; chip-20260923-arc083-triadic-primitive). The\n"
    "  DEV-NEED-021 'otherness REQUIRES object-permanence + self-stability' gates are now a\n"
    "  default build ORDERING: MIRROR-1 no longer gates on OBJ-2 + OBJ-3 and gains %s\n"
    "  (triadic co-reference / declarative joint attention, registered the same day) as its\n"
    "  prerequisite; MIRROR-7 keeps the SELF-7 gate on INV-064's own authority only. MIRROR-2's\n"
    "  SELF-1 gate is deliberately UNCHANGED: it is mechanistic (ARC-010 reuses the self\n"
    "  generative model, so a stateful one must exist), not the developmental ordering the lit\n"
    "  pull weakened. Basis: evidence/literature/targeted_review_arc_083/ (Sodian+Kristen-Antonow\n"
    "  2015, Kartner et al. 2010, Slaughter+Boh 2001, Bischof-Kohler 2012).\n" % (day, nid)
)
path.write_text(text, encoding="utf-8")
print("plan patched")
```

## `apply_doc.py`

```python
"""Patch arc_080_object_representation_primitive.md for the ARC-083 triadic primitive.
Usage: apply_doc.py <doc path> <NEW_ID>
"""
import sys
from pathlib import Path

path = Path(sys.argv[1])
nid = sys.argv[2]
text = path.read_text(encoding="utf-8")


def once(old, new):
    global text
    n = text.count(old)
    if n != 1:
        sys.exit("ABORT: anchor matched %d times: %r" % (n, old[:80]))
    text = text.replace(old, new)


once(
    "+ ARC-081 (self-stability prereq) + SD-039 (partial-permanence prereq). |",
    "+ ARC-081 (soft default ordering only -- weakened 2026-09-23, GFLAG-0309) + SD-039 (candidate "
    "motivational-weighting half of person-permanence) + **%s** (triadic co-reference -- the "
    "developmental prerequisite; see below). |" % nid,
)
once(
    "Per DEV-NEED-021, prerequisites are object-permanence (Pillar 1, partial via SD-039) + "
    "self-stability (Pillar 2 / ARC-081). See §5.1. |",
    "DEV-NEED-021's object-permanence (Pillar 1, partial via SD-039) + self-stability (Pillar 2 / "
    "ARC-081) are a DEFAULT BUILD ORDERING, not prerequisites (weakened 2026-09-23, GFLAG-0309); the "
    "prerequisite the evidence supports is %s. See §5.1. |" % nid,
)
once(
    "Gated on MECH-163 (multi-step hippocampal planning) and on Pillars 1+2 (per DEV-NEED-021: "
    "otherness inference REQUIRES object persistence + self-stability). [V4] |",
    "Gated on MECH-163 (multi-step hippocampal planning) and on %s (triadic co-reference over "
    "ARC-080 slot allocation). Pillars 1+2 typically come first but are not a gate "
    "(GFLAG-0309). [V4] |" % nid,
)
once(
    "DEV-NEED-021: otherness REQUIRES object persistence + self-stability\n"
    "  => PILLAR 1 + PILLAR 2 are prerequisites for PILLAR 4\n"
    "```\n",
    "DEV-NEED-021 (weakened 2026-09-23, GFLAG-0309): otherness TYPICALLY DEVELOPS AFTER\n"
    "  object persistence + self-stability  => PILLAR 1 + PILLAR 2 are a default ORDERING for PILLAR 4\n"
    "PREREQUISITE the evidence supports: %s triadic co-reference\n"
    "  (self slot + other slot, concurrently live, co-bound to one object token)  --> PILLAR 4\n"
    "```\n"
    "\n"
    '<a id="%s"></a>\n'
    "### %s -- triadic co-reference primitive (the PILLAR 4 prerequisite)\n"
    "\n"
    "Registered 2026-09-23 (chip-20260923-arc083-triadic-primitive), follow-on to GFLAG-0309. The\n"
    "targeted developmental pull (`evidence/literature/targeted_review_arc_083/`) found the\n"
    "self-stability half of DEV-NEED-021 unsupported as a necessity: in the one confound-controlled\n"
    "longitudinal design (Sodian + Kristen-Antonow 2015, n=83, 12->50 months) 12-month DECLARATIVE\n"
    "pointing predicted 50-month false belief, imperative pointing did not, and mirror self-recognition\n"
    "mediated none of the path. The supporting source (Bischof-Kohler 2012) names its own mechanism as\n"
    "synchronic identification -- holding self and other in view at once. Both point at the same thing:\n"
    "a relational binding of **two concurrently-live agent slots to one shared object token**.\n"
    "\n"
    "Architecturally that is a binding operation over this umbrella's slot machinery, not a new store:\n"
    "allocate an other-agent slot concurrent with the self slot, and co-reference both to one object\n"
    "file. Rat and bat CA1 (Danjo et al. 2018; Omer et al. 2018) code self and other positions jointly\n"
    "and discretely in one population, which is the format this predicts. ARC-083 supplies the other\n"
    "slot's content; %s supplies the relation that makes it usable for otherness inference. V4,\n"
    "design-only, substrate_conditional -- no code, no experiment, not in V3 closure.\n"
    % (nid, nid.lower(), nid, nid),
)
once(
    "- ARC-010, ARC-047, MECH-031/032/036/041 (Pillar 4 -- others, V4)\n",
    "- ARC-010, ARC-047, MECH-031/032/036/041 (Pillar 4 -- others, V4)\n"
    "- %s (Pillar 4 developmental prerequisite -- triadic co-reference / declarative joint attention, V4)\n" % nid,
)
path.write_text(text, encoding="utf-8")
print("doc patched")
```
