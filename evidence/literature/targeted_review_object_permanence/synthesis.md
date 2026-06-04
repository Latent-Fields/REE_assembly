# Synthesis — Object permanence (lit pull L2)

**Pull:** L2 from `evidence/planning/object_representation_thread_2026-06-04.md` section 4.
**Date:** 2026-06-04. **Claims grounded:** ARC-080 (umbrella), ARC-006, MECH-045 (parallel lit
signal, no promotion -- ARC-080 is `candidate`/`architectural_commitment`/v4, exempt from exp gating).
The ARC-080 object-representation umbrella was registered the same day (commit `075ebbe76d`, "Option A"
thin spine); its own `functional_restatement` names these L1/L2 pulls as its biology grounding. The
permanence pillar (PILLAR 1) is named in ARC-080 as a **future child, not yet registered**.
**Companion pull:** L1 object-files & feature binding (`targeted_review_object_files_feature_binding`,
sibling session) grounds the same ARC-006/MECH-044/MECH-045 layer from the binding side.

Five entries, all human-infant developmental cognition:

| Entry | Anchor | Direction | What it grounds |
|---|---|---|---|
| Baillargeon, Spelke & Wasserman 1985 | drawbridge VOE | supports | Permanence is a REPRESENTATIONAL competence, present ~5 mo, dissociable from manual search |
| Spelke 1990 | core-knowledge principles | supports | Continuity = permanence stated formally; cohesion = the object-file unit |
| Kellman & Spelke 1983 | partly-occluded rod | supports | Token-unity across an occluding gap is bound by COMMON MOTION, not static features |
| Xu & Carey 1996 | numerical identity | mixed | **Token (spatiotemporal) individuation precedes and is distinct from type (kind) individuation** |
| Diamond 1985 | A-not-B + PFC lesion | supports | Search failure is a recall/inhibition READOUT limit, not loss of the representation |

## The headline: token before type, and REE has it inverted

The through-line of all five papers, and the reason this pull was commissioned, is the
**token-vs-type distinction** the memo flags in section 2.2. The biology is unusually clean on
ordering:

- An object is carried through occlusion by **spatiotemporal continuity** — one connected path
  through space and time (Spelke's continuity principle; Kellman & Spelke's common-motion unity;
  Xu & Carey's spatiotemporal numerical identity). This is **token-instance** tracking: *this
  particular thing, here is where it went.*
- **Kind/property** individuation — "a duck and a ball must be two things" — is a **later**,
  separate capacity (~12 months in Xu & Carey), not the route by which young infants track
  identity through occlusion.

REE's live object machinery is built on the *later* route and lacks the *earlier* one. The whole
SD-015 → SD-049 → SD-057 lineage keys identity on a **type tag** (resource category, ~3 kinds).
That is property/kind individuation — developmentally the second thing to arrive — and Xu & Carey
show it is *not* what permanence rests on. REE's developmental order is therefore inverted: it has
a type identity and no spatiotemporal token tracker, while permanence is precisely the token
tracker. The memo's "first design fork" (type vs token vs anchor as the unit) is answered by the
literature: **token, established spatiotemporally.**

## Mapping to the three REE targets the brief named

**(1) The permanence pillar (ARC-080 PILLAR 1; future child, not yet a registered claim).** The pull
licenses the pillar as a real representational primitive worth building (Baillargeon: permanence
exists as a competence) and tells it what to build: a spatiotemporally-keyed token that persists
across a perceptual gap (Spelke continuity, Xu & Carey), bound by motion/spatiotemporal coherence
rather than static features (Kellman & Spelke), and read out through a *separate*, fallible,
delay-sensitive retrieval stage (Diamond). When the ARC-080 umbrella and its permanence child are
registered, re-tag these five entries to that child.

**(2) MECH-045 (object-file-like buffers provide minimal entity persistence across time).** Four
of five entries tag MECH-045 directly. They ground the *existence* and *unit* of the buffer
(Baillargeon, Spelke, Kellman & Spelke) and add the architectural lesson that a buffer is not
enough — it needs a delay-sensitive readout that can perseverate independently of the store
(Diamond). MECH-045 currently has no biology lit at all; this pull and the L1 companion close that
gap. (MECH-045 remains `provisional`, design-only, not in ree-v3 code — lit_conf is a parallel
signal and does not promote it.)

**(3) The SD-039 / MECH-292 / MECH-293 ghost-goal bank — what it does and does NOT deliver.** This
is the sharpest result for REE. The ghost bank delivers **motivational** persistence: a goal-value
snapshot that survives when its spatial anchor is out of view, queried by wanting-rank. Diamond's
store/readout dissociation actually *validates the ghost bank's architecture* — a persistent store
plus a separate readout is the right shape, and it is the shape biology uses. But three of these
papers show what the ghost bank does **not** deliver for permanence:
  - It keys on a **spatial anchor**, not a **spatiotemporally-tracked token**. Xu & Carey's token
    identity is "this object on this trajectory," not "the value that was at this place."
  - Its payload is a **goal-value snapshot**, not an **object-identity code** — it answers "do I
    still want the thing that was over there," not "is *that* object still there, and where now."
  - Its binding/recall is by **wanting-rank and anchor**, not by **common-motion unity** (Kellman
    & Spelke) or **numerical individuation** (Xu & Carey). It cannot answer "how many distinct
    objects" or "is this the same one."

So the ghost bank is a correct *motivational*-persistence primitive and a correct store/readout
*template*, but it is not object permanence and would not become so by adding a fourth per-object
store on the existing type key — that would reproduce REE's gap (type, not token) rather than close
it. True permanence requires the token-instance layer REE does not yet have.

## Caveats carried across the pull

- All evidence is human-infant looking-time or reaching; the bridge to a machine persistence buffer
  is conceptual, not measured. Mapping fidelity, not source quality, is the binding constraint and
  is logged per entry.
- The drawbridge paradigm (Baillargeon) has a documented low-level confound; the permanence
  conclusion leans on the wider VOE corpus, not that paradigm alone.
- The look-based (Baillargeon) vs reach-based (Diamond/Piaget) permanence measures dissociate and
  which indexes "real" permanence is a live controversy; Diamond's competence/performance reading is
  one resolution, not a settled fact.
- Off the V3-closure critical path. Doc/lit grounding only — no claim registered, no substrate
  built, no experiment queued. Per the memo, the only V3-era-safe action is the documentation spine;
  everything substrate-level is V4 / late-V3.
