---
nav_exclude: true
---

# Thought Intake: Hippocampal Episodic Organisation Beyond Trajectory Generation

**Raw thought file:** `docs/thoughts/2026-08-19_hippocampal-episodic-organisation.md`
**Session:** thought-intake-20260819-fresh, 2026-08-20
**Status:** processed, claims registered (MECH-495, Q-095); governance flag raised on the
slot-differentiation objective
**Sibling intake:** `evidence/planning/thought_intake_2026-08-19_context-inference-active-persistent-control.md`
(this thought explicitly cross-references that one via event boundaries; read as a pair)

---

## Verbatim prompt

See `docs/thoughts/2026-08-19_hippocampal-episodic-organisation.md` for the full text.

Core proposition, condensed: REE's hippocampal system is cast primarily as a trajectory
generator, which may capture only part of the computational role required. A richer account
asks how REE converts a continuous experience stream into distinct, retrievable episodes and
contextual structures -- via episodic binding, event segmentation, pattern separation, pattern
completion, indexing, and remapping. The hippocampal contribution may be less "propose
trajectories" than **determine what experience belongs with what**, and therefore which prior
experience is relevant now.

**The load-bearing refinement, and the reason this intake matters beyond re-description:**

> The goal should probably not be maximal pattern separation. [...] The desired memory topology
> is closer to: **related experiences overlap appropriately; behaviourally distinct latent
> situations separate appropriately.** This means that "more diverse slots," greater occupancy,
> or lower representational overlap is not by itself a biological or computational objective.

---

## What's New vs. Existing REE Docs (novelty table)

| Existing claim/doc | What it already covers | What this thought adds |
|---|---|---|
| **MECH-147** (DG-mediated pattern separation gates trajectory disambiguation) | DG must produce non-redundant sparse encodings of similar `z_world` states before rollouts are generated, preventing near-identical trajectory proposals. Motivated by Sakon & Suzuki 2019. Status `candidate`, phase **v4**. | Covers separation, and covers it as a **monotone good**. Its stated ablation prediction is that removing the layer "should specifically collapse trajectory diversity" -- i.e. diversity-collapse *is* the failure signature. This thought asserts the objective is **non-monotone**: past a point, further separation destroys the overlap that generalisation and memory linking require. MECH-147 has no notion of separation being excessive, and no notion of *appropriate* overlap for related experiences. |
| **MECH-242** (pattern completion for familiar trajectories vs vector-based construction for novel ones) | A genuine dissociation: attractor-based completion suffices within a learned residue field; vector-based construction is required to generalise to novel environments. | Covers completion, and covers the completion/construction split well. Does not address the **organisation** question -- what determines which stored episode completion should retrieve, or how the store is structured so that completion retrieves the *relationally* right thing rather than the *nearest* thing. |
| **MECH-154** (E1 as an addressable associative manifold with internal indexing) | E1 supports retrieval, traversal, ordering, pattern separation and pattern completion; parietal-analogue functions are properties of E1 connectivity and representational geometry, not a separate module. | This is the closest existing claim to the thought's "indexing" leg and largely subsumes it. Novelty here is low. What MECH-154 does not supply is a **normative target for the geometry** -- it says the manifold is addressable, not what good addressing looks like. |
| **MECH-288** (two-level event segmenter) | Built substrate (`ree_core/hippocampal/event_segmenter.py`): PE-threshold fast scale, BOCPD-Gaussian latent change-point slow scale; emits `outer.inner` segment IDs consumed as region keys. | Covers segmentation. New here is the **reciprocal coupling**: persistent context mismatch should increase separation or start a new episode, while successful pattern completion should support persistence within the current context. MECH-288 currently runs open-loop with respect to context arbitration -- boundaries are produced, never fed back from a context decision. |
| **MECH-074d** (BLA `remap_signal` on harm-PE spike with attribution gating) | Partial (~one-third) remap, not wholesale replacement, fired on harm-PE spike when predictor-attribution flags specific latent codes. **Demoted 2026-08-16.** | Covers remapping, but from a **single affective trigger** (harm PE with attribution). The thought's remapping is triggered by *explanatory reallocation* -- experience being better explained as belonging to a different latent situation -- which is the MECH-494 criterion in the sibling intake, not a harm signal. Different trigger, same downstream operation. |
| **SD-017 / ARC-045 / MECH-166** (sleep-driven slot differentiation) | The lineage that has been **operationally measuring memory quality as differentiation** for six experiment generations (V3-EXQ-436a..436f). ARC-045's own premise: "without bidirectional flow, context representations remain **globally undifferentiated**". PASS/FAIL has been gated on `slot_cosine_sim` (and `sws_slot_diversity = 1 - slot_cosine_sim`, emitted by every sleep-pass driver: `v3_exq_242/243/245/245a/245b/246`). | **This is where the thought bites, and it is a distinct criticism from the ones already recorded.** The 2026-08-07 governance reversal established that `slot_cosine_sim` was a **measurement defect** (whole-bank mean off-diagonal cosine, no occupancy mask, tracking content-similarity x occupancy-fraction -- scoring a 12-well-separated-slot arm at 0.076, *worse* than a single-slot arm at 0.009). V3-EXQ-436e then repaired the DV to occupied-slots-only, and 436f traced the residual failure to a genuine substrate defect (`write()` addressing by `scores.mean(0).argmin()`, deterministic single-slot fixed point). **All three findings are about whether differentiation is being measured correctly, or produced at all. None asks whether differentiation is the right OBJECTIVE.** This thought does, and answers no. |
| `behavioral_diversity_acceptance_criteria.md` / **MECH-313**, **ARC-065**, **MECH-439**, **MECH-442** | The behavioural-diversity governance ladder and the F-dominance conversion ceiling; `MECH-442` (MAP-Elites-style behavioural-descriptor archive) as the parked fix. | Same structural point one level down: the diversity ladder is a set of **scalar magnitude** criteria. `Q-092` (the "umpire, not ruler" intake, 2026-08-11) already made the analogous move on the **behavioural** side -- replacing "how much diversity" with "are the organisations *discriminable*". **This thought is the representational-side counterpart of Q-092**, and the two should be read together: both replace a magnitude target with a relational/discriminability target. That parallel is strong independent support for the reframing and should be stated wherever either is discussed. |

**Net assessment.** Five of the thought's six named capabilities (binding, segmentation,
separation, completion, indexing, remapping) are **already covered** by existing claims, several
with built substrate. Registering them again would be duplication. The genuinely new content is
concentrated in two places:

1. **The relational-topology objective** -- separation is not a monotone good; the target is
   *related experiences overlap appropriately, behaviourally distinct latent situations separate
   appropriately*, and diversity/occupancy/low-overlap are **not objectives in themselves**.
   This is normative and architectural, it contradicts an assumption embedded in live PASS/FAIL
   criteria, and it is testable. Registered as **MECH-495**.
2. **The thought's own honest falsifier** -- if existing REE machinery already produces
   appropriate episodic discrimination, completion and context-sensitive retrieval, this is a
   reinterpretation rather than a missing function. Registered as **Q-095**, deliberately as an
   open question rather than an assertion, because the thought itself declines to assert it.

Episodic binding is the one capability with a genuine gap (no single claim asserts that objects,
locations, actions, internal states, goals, outcomes and temporal relations are bound into **one**
coherent event representation), but the thought does not develop it beyond naming it, and it is
substantially entangled with MECH-154 and MECH-288. Recorded here as an unregistered gap rather
than forced into a claim.

---

## Governance flag: the slot-differentiation objective (RAISED)

**Why this is raised now rather than left as claim text.** The timing is unusually tight:

- The V3-EXQ-436 lineage has run **six generations** (436a bug -> 436b recording gap -> 436c
  write_gate defect -> 436d metric defect -> 436e DV repair -> 436f substrate defect), and a
  **re-derive brake fired** at 436f (3rd `substrate_ceiling` hit against a threshold of 2),
  refusing a same-question 436g re-queue until the write-path build landed.
- **That build has now landed** (ree-v3 `76cbf844`, recorded 2026-08-19 in `17ee8c318b`;
  refractory write-selection mode `692f8526d0` recorded in `3d868dd89c`).
- The validation experiment is **not yet queued** -- `ree-v3/experiment_queue.json` is empty as
  of 2026-08-20T03:1xZ.
- The landing note for the refractory mode already records that "the occupied-slot cosine DV
  cannot discriminate the arms at 5 seeds."

So the next thing to happen in this lineage is the design of a validation run, and on current
trajectory it will be scored against an occupied-slot cosine **differentiation** DV -- the same
objective, correctly measured at last. If MECH-495 is right, a seventh generation would be spent
optimising toward a target that is not the right target, and a PASS would be as uninformative as
a FAIL.

**What the flag asks governance to adjudicate:** whether the DV for the post-write-path-build
validation run should remain a differentiation statistic, or be re-specified as a
**relational-topology** statistic (agreement between representational similarity structure and
latent-context structure -- e.g. a representational-similarity correlation against the 2x2 design
below), before that run is designed. It does **not** ask for any status, confidence or
`evidence_direction` change on SD-017 / ARC-045 / MECH-166 / MECH-147 -- those are governance's
call, and this intake deliberately changed none of them.

**What the flag does not claim.** It does not claim the six generations were wasted; 436d/436e/436f
each established something real and the substrate defect they converged on was genuine and is now
fixed. It claims only that a *fourth*, independent question -- is the objective right? -- has never
been asked in this lineage, and that the cheapest moment to ask it is before the next run is
designed rather than after it scores.

---

## Key formulations

**The topology target (verbatim from the raw thought):**

> related experiences overlap appropriately; behaviourally distinct latent situations separate
> appropriately

**The 2x2 discriminating design.** Vary perceptual similarity and latent-context identity
independently:

| | same latent context | different latent context |
|---|---|---|
| **similar appearance** | should OVERLAP (generalisation) | should SEPARATE (this is the hard cell) |
| **different appearance** | should OVERLAP (linking across surface change) | should SEPARATE |

The diagonal cells are what any similarity-driven memory gets right for free. **The two
off-diagonal cells are the entire test**: similar-appearance/different-context is where a
nearest-match store fails by merging, and different-appearance/same-context is where a
maximal-separation store fails by splitting. A differentiation-maximising objective scores the
first cell correctly and the second cell **backwards** -- which is precisely why the objective
and the metric are separable questions.

**The reciprocal coupling (interface to the sibling thought):**

> context inference influences memory segmentation, and memory organisation influences subsequent
> context inference

Event boundaries are the shared interface: persistent context mismatch (MECH-494's criterion)
should raise separation or open a new episode; successful pattern completion should support
persistence within the current context (MECH-493's hysteresis).

---

## Affected existing claims

- **SD-017 / ARC-045 / MECH-166** -- their operative DV's *objective* is challenged. Governance
  flag raised; **no status, confidence, `evidence_direction` or
  `pending_retest_after_substrate` change made by this intake.**
- **MECH-147** -- its ablation prediction ("collapse trajectory diversity" as the failure
  signature) presumes separation is a monotone good. Cross-referenced from MECH-495; not
  modified. Note MECH-147 is phase **v4**, so this is not urgent for it the way it is for SD-017.
- **Q-092** ("umpire, not ruler") -- the behavioural-side counterpart of the same magnitude ->
  relational reframing. Cross-referenced in both directions is worth doing at the next governance
  touch; this intake cross-references from MECH-495 only.
- **MECH-288** -- gains the reciprocal-coupling proposal (boundaries fed back from context
  arbitration). Cross-referenced, not modified.
- **MECH-074d** -- remapping trigger contrast (harm-PE vs explanatory reallocation) noted.
  Cross-referenced, not modified.

---

## Candidate claims (REGISTERED)

- **MECH-495** -- the memory-organisation objective is relational appropriateness, not maximal
  separation; diversity/occupancy/low-overlap are not objectives in themselves.
  `mechanism_hypothesis`, status `candidate`, `epistemic_category: standard`, phase v3.
- **Q-095** -- does explicit hippocampal episodic organisation add predictive or behavioural
  capability beyond existing trajectory memory, or is it a reinterpretation of mechanisms REE
  already has? `open_question`, status `open`.

**Deliberately NOT registered:** episodic binding as a distinct claim (named but undeveloped in
the raw thought; entangled with MECH-154/MECH-288 -- recorded above as a gap), and the six
capabilities individually (already covered by MECH-147/154/242/288/074d).

---

## Next steps

1. **Governance adjudication of the flag comes first**, before the post-write-path-build
   validation run is designed. That is the whole point of raising it now.
2. **Build the 2x2 environment family once, for both intakes.** The sibling thought's
   perceptually-similar/opposing-policy environment pair is a special case of this 2x2 (it is the
   similar-appearance/different-context cell). One substrate serves MECH-493, MECH-494 and
   MECH-495; building two would be waste.
3. **Specify the relational-topology statistic before running anything.** The natural form is a
   representational-similarity correlation between the memory's similarity structure and the
   ground-truth latent-context structure, which requires the environment to expose ground-truth
   context labels -- a design constraint on step 2, not an afterthought.
4. **Targeted literature pull**: episodic binding, pattern separation/completion trade-offs
   (specifically the separation-generalisation tension rather than separation alone), hippocampal
   indexing theory, remapping, event boundaries, and latent-state inference. The raw thought's own
   intake note asks for exactly this list.
5. **Do not queue an experiment from this intake yet.** MECH-495's test depends on step 2's
   substrate and step 1's DV decision.
