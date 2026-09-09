# Claim Synthesis -- MECH-074b (locus adjudication: retrieval-readout vs replay-sampling)

- **Claim:** MECH-074b -- "BLA analogue writes a content-selective per-trace arousal tag at
  encoding and applies a per-trace retrieval weight vector (NOT a scalar gain) on hippocampal
  readout." (`status: candidate`, `claim_type: mechanism_hypothesis`, registered 2026-04-21 as a
  split child of MECH-074)
- **Session:** angry-pascal-6fd799
  (`[chip_ref: chip-20260909-mech074b-retrieval-locus-synthesis]`, task_99d731ca)
- **Date:** 2026-09-09T17:53:10Z
- **Trigger:** **GFLAG-0156** (`evidence_discrepancy`, raised 2026-09-06 by
  `thought-digestion-v3-20260904-apply`, resolved-as-ROUTED 2026-09-09T17:47:08Z by /governance
  cycle governance-20260909 wave 4, which recorded the finding in
  MECH-074b's `evidence_quality_note` (REE_assembly `483a31d784`) but deliberately did NOT rewrite
  the claim text -- "rewriting a claim's asserted locus on a single mixed lit entry is a
  claim-level change, not a note refresh". This artifact is that claim-level pass.
- **Evidence read:** all four entries of `evidence/literature/targeted_review_mech_074b/`, the
  V3-EXQ-888 manifest, `docs/architecture/sd_035_amygdala_analog.md`, and the MECH-074 /
  MECH-074a / MECH-074b claim entries.

## TL;DR

**Verdict: (b) -- the mechanism is real and its selectivity is well-grounded, but the asserted
LOCUS is over-claimed and is narrowed here.** Zero compute, zero new claims, no experiment queued,
status NOT moved.

**The framing the chip inherited is a miscount, and correcting it is the finding.** GFLAG-0156 and
the governance note both describe this as *one mixed entry (Roozendaal & McGaugh 2011) against
three supporting siblings*, with the instruction to weigh it against them rather than let one entry
drive a rewrite. Reading all four, that is not the shape of the pull. **All three "supports"
entries independently and explicitly decline to support the retrieval locus** -- each one names it
as the weak point in its own mapping section, and each is scored `supports` on
**content-selectivity**, not on locus:

| Entry | dir / conf | Supports | Says about LOCUS |
|---|---|---|---|
| Adolphs 2001 (gist/detail lesion) | supports 0.75 | vector-not-scalar (opposite-signed detail effect) | "the unclean part is *locus*" -- describes an **encoding-time filter**; `mapping_fidelity` held to 0.7 *because* of this |
| Mather & Sutherland 2011 (ABC) | supports 0.68 | priority-weighted, not uniform | priority set "largely at perception and encoding ... carried through consolidation"; **"agnostic-to-contrary"** on the retrieval-time re-weighting |
| Sutherland & Mather 2012 | supports 0.60 | selective amplification, empirically | short-term attentional letter arrays; "nothing here speaks to a weight applied to consolidated traces"; corroborates "without testing the retrieval-locus" |
| Roozendaal & McGaugh 2011 | **mixed** 0.62 | encoding/consolidation side (i.e. MECH-074a) | places the established selective effect at **consolidation**; amygdala action **at retrieval is IMPAIRING** -- opposite sign to `w_i >= 1` |

**So on the question of content-selectivity the score is 4/4 supports. On the question of retrieval
locus the score is 0 supports, 3 silent-to-contrary, 1 actively contrary on sign.** Roozendaal is
not an outlier to be outvoted by its siblings; it is the only entry in the pull that *addresses*
locus at all. Weighing "3 vs 1" here would be counting votes cast on a different question.

**Three further lines converge on the same narrowing, independently of the literature:**

1. **GFLAG-0156's own suggested form** already names it: narrow "to a *sampling-priority* rather
   than *retrieval-enhancement* form".
2. **MECH-074b's own registered FALSIFYING clause** already contains it verbatim: if the per-trace
   weight has "composition authority over the replay SAMPLE (888) but no authority over item-level
   READOUT, ... the claim should be narrowed to the sampling path rather than retained as a
   retrieval-weight claim."
3. **V3-EXQ-888 -- the claim's sole experimental support -- measured exactly the sampling path.**
   Its `combination_rule` states "C2 alone is MECH-074b", and C2 is `address_route_authority`: the
   per-trace bias vector shifting **AOR (arousal over-representation) in a weighted sample drawn
   from the exploration/replay buffer**. Every precondition is phrased about "a weighted sample"
   and "how the sample is weighted". No item-level recall readout was measured, and
   `what_would_answer` precondition (b) says so explicitly -- a PASS obtained without
   within-episode central/gist-vs-peripheral items "would be vacuous with respect to the residual".

So the claim's only PASS is evidence for the sampling path, and the claim's own text says that is
the condition for narrowing to the sampling path.

## The decision

**MECH-074b's asserted locus is narrowed to a content-selective per-trace priority over the
hippocampal replay / reactivation SAMPLE.** The retrieval-time, item-level readout enhancement is
demoted from asserted mechanism to **explicitly unevidenced residual**, carrying a contrary-signed
prior from Roozendaal & McGaugh.

This is **(b), not (c).** The mechanism is not mis-located wholesale, for three reasons:

- The claim's **tag write is already at encoding** -- the title says so. Half of MECH-074b already
  sits on the locus Roozendaal supports.
- The **content-selectivity is robustly supported** (4/4), and it is a genuine, load-bearing design
  constraint that a scalar gain cannot satisfy (Adolphs' opposite-signed detail effect).
- The read-side operation **demonstrably exists and has authority** (888 C2, 3/3 seeds) -- over
  replay-sample composition. Replay/reactivation *is* the consolidation mechanism, so this reading
  moves MECH-074b onto the encoding/consolidation side that Roozendaal's "best-established" claim
  actually supports, rather than stranding it.

### Implication for the MECH-074 / 074a / 074b split -- the split SURVIVES and is strengthened

MECH-074b `depends_on` MECH-074a, the relation being that the retrieval bias consumes the
encoding-time arousal tag. Narrowing the locus does **not** collapse 074b into 074a:

- **MECH-074a** is a *scalar* multiplicative gain on write **STRENGTH** (`encoding_gain`, inverted-U,
  decaying window).
- **MECH-074b** is a *per-trace vector* over **WHICH traces are selected** (`retrieval_bias`).

These stay dissociable in kind, not merely in wiring, and the dissociation is directly evidenced:
888's **C4 separability** PASS shows both routes independently clear the authority floor, and
Adolphs 2001's opposite-signed detail effect is producible **only** by 074b's vector form, never by
074a's scalar. Both now sit on the encoding/consolidation side -- which is a *tightening* of the
parent's read/write-head story (two routes into one memory system), not a threat to it. The
`depends_on` edge is unchanged and becomes cleaner: tag written at encoding (074a's window),
consumed as sampling priority during replay.

### A second, previously unrecorded finding: the additive rule cannot produce the pattern its own best source shows

This is not part of GFLAG-0156 and is surfaced here because two entries flag it independently and
nothing in the claim records it.

The substrate rule is `w_i = 1 + alpha * arousal_tag_i`, `alpha in [0.3, 1.0]` -- **always >= 1**, so
it can only ever raise weights. But:

- **Adolphs 2001**, the pull's *highest-confidence* entry (0.75) and the claim's canonical warrant
  for vector-not-scalar, shows bilateral amygdala damage produced **poorer gist memory but
  *superior* detail memory** -- the two move oppositely. Removing the modulator made peripheral
  memory *better*.
- **Mather & Sutherland 2011** states the consequence directly: ABC predicts "genuine *absolute*
  impairment of low-priority items", and an additive weight ">= 1 ... cannot, on its own, produce
  absolute suppression of peripheral traces. ... the substrate would need a competitive
  normalisation step, not just an additive per-trace boost."
- **Sutherland & Mather 2012** is the honest limit on the other side: there, low-salience recall was
  *unchanged*, not impaired. So the absolute-suppression requirement is supported by the lesion data
  and the theory, but not by that behavioural experiment.

So Adolphs supports "**not scalar**" but does **not** support "**additive per-trace weight**"; it
supports a **competitive/normalising** form. The claim's registered target -- "central/gist items
~1.3x-2.0x **relative to** neutral baseline" -- papers over the distinction, because a purely
*relative* advantage is satisfiable by the additive rule while the lesion pattern is not. This is a
concrete substrate design flag for whoever builds the follow-up, and it is logged as a residual
below rather than acted on here (changing the weight rule is a substrate change, not a claim edit).

## Recording-quality caveat on V3-EXQ-888, sharpened

Governance recorded (correctly, and this artifact leans on it) that 888's PASS is not fully
re-derivable from its manifest. Reading the manifest directly, the caveat needs **one correction
and one refinement**:

- **Correction:** governance's note says "the manifest has **no** `combination_rule`". It does --
  `interpretation.combination_rule` is present and explicit: *"PASS iff C1 AND C4, where C4 = (C2
  AND C3) ... C3 alone is MECH-074a and C2 alone is MECH-074b."* That sentence is in fact what lets
  this synthesis attribute C2 specifically to MECH-074b, so it is load-bearing here.
- **Refinement:** the accurate statement is that the **preconditions** carry full `measured` /
  `threshold` / `met` triples and are re-derivable, whereas the four **criteria** are recorded in
  `interpretation.criteria_non_degenerate` as **bare booleans** (`C1..C4: true`) with no measured
  value and no threshold. So the readiness of the instrument is auditable; the verdict itself is
  not.

Net: 888 is good enough to establish *which route* was exercised (that is what
`combination_rule` + the precondition set give us, and it is all this synthesis needs), and not
good enough to re-derive the effect sizes. Nothing here leans on the latter.

## What was applied to claims.yaml

Narrow edits only; **status and `live_status` untouched**, per the chip's constraint -- a locus
correction is not a promotion judgement.

1. **`title`** -- "on hippocampal readout" replaced with the sampling-path scope, so the headline no
   longer asserts a locus the body disclaims (that mismatch is what GFLAG-0156 was raised about).
2. **`functional_restatement`** -- a `LOCUS SCOPE (2026-09-09)` block appended (nothing rewritten
   above it, so the original specification stays auditable): records the 4/4-vs-0/4 split, the
   contrary-signed retrieval prior, and demotes the item-level readout leg to unevidenced residual.
3. **`evidence_quality_note`** -- outcome recorded with a pointer to this artifact.

**Deliberately NOT changed:**

- **`what_would_answer` needs no edit and gets none.** It already encodes the correct test and the
  correct narrowing -- precondition (b) and the FALSIFYING clause anticipated this verdict. The
  claim's *test design* was right all along; only its *asserted scope text* lagged. This is the
  cleanest evidence that the narrowing is a correction rather than a redefinition.
- **`source`** -- the chip instructed folding the omitted pull into `source` "either way", noting
  the omission "is not in dispute". **That is already done and was already done before this chip
  was written**: all four `targeted_review_mech_074b` entries have been in `source` since the
  2026-09-06 thought-digestion apply (see the claim's own `notes`). The "omitted entirely" phrasing
  in GFLAG-0156 was accurate when the flag was *raised* and was carried forward verbatim into the
  wave-4 resolution note after it had ceased to be true. No action needed.
- **`digestion_note`** -- the deferred "grows with trace age" leg is left in place, but see residual
  R1: this synthesis materially changes how that leg should be read.

## Residuals (not actioned here)

- **R1 -- the trace-age leg is not merely untestable, it is evidence for the narrowing.** The
  `digestion_note` defers "BLA contribution grows with trace age (20 min -> 1 week)" as
  `substrate_conditional` on an unbuilt trace-age input. Roozendaal's entry makes a sharper point
  that nothing records: *"a growing effect over that window is exactly what a consolidation process
  looks like"*. SD-035 sources this leg to LaBar & Cabeza 2006 on increasing **amygdala-MTL
  connectivity** -- a systems-consolidation observation. So the leg most likely belongs to the
  consolidation account, and if it is ever split to its own id (as the digestion note offers) it
  should be registered on the consolidation side, not as a retrieval-time property.
- **R2 -- additive vs competitive weight rule** (section above). Affects
  `ree-v3/ree_core/amygdala/bla.py` and SD-035 line 91. A substrate question; needs an
  `/implement-substrate` pass, not a claim edit.
- **R3 -- derived site data is stale on the title.** The title string is carried into generated
  `docs/assets/data/{claims,brain_map,claim_dependency_process}.v1.json`. Not regenerated here, per
  CLAUDE.md **Narrow Edits Only** (a single-field change must not trigger a full index regen); the
  next `/governance` cycle's regen picks it up.
- **R4 -- GFLAG-0156 is already `resolved`** (2026-09-09T17:47:08Z), closed by wave 4 as
  *routed-to-this-chip* rather than as *done*. It is therefore **not re-resolved** here -- there is
  no open flag to flip, and re-opening it to immediately re-close it would add a spurious cycle.
  This artifact is the resolution's named deliverable; the decision is recorded in the claim and
  here.
