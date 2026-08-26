# Thought intake -- representation -> authority -> selection (2026-08-26)

**Date:** 2026-08-26
**Raw thought file:** [`docs/thoughts/2026-08-26_representation_authority_selection.md`](../../docs/thoughts/2026-08-26_representation_authority_selection.md)
**Session:** `insights-7fd98a` (Remote Control, interactive)
**Session development doc (code-verified; read this for the evidence):**
[`representation_authority_selection_bottleneck_20260826.md`](representation_authority_selection_bottleneck_20260826.md)
**Claims registered this pass:** ARC-133, ARC-134, MECH-516, MECH-517, MECH-518, MECH-519, MECH-520, MECH-521

---

## 1. Verbatim prompt

The thought was given directly in conversation across four turns. Core proposal,
verbatim:

> "Representation itself must relate to why something might be selected. Object
> representation systems where decisions for what make an object relate to the why
> of selection. That is to say relating to usefulness which would relate to goals,
> harm, and things like metabolic or interoceptive state (hunger and thirst etc)
> and possibly other basic drives like information need. Objects and episodes then
> hold useful information, indeed very compressed information which could help with
> selection etc. The previous idea I had of higher order representations in the
> latent field may not quite be all the story especially since higher level latents
> may be more abstract but without there being a funnel they are not necessarily
> compressed to extract useful representative values."

Three subsequent turns extended it:

> "Alone what I just thought of might just end up with horrendously over compressed
> representations that mean nothing. But being able to check predictions based on
> the higher level representations across time given the temporal representation
> spread might hold open perception where it would otherwise collapse. This... might
> bring in the ephaptic coupling again to regulate the level at which perception is
> considered."

> "Precision as previously described and described elsewhere is not representational
> depth though." *(a correction to this session's first collision check -- see 3.2)*

> "Could coherence extent set slot count though... Perhaps the number of related
> coherencies. That would be too simple though right?"

## 2. What's new vs existing REE docs/claims

| thread in the thought | existing REE coverage | verdict |
|---|---|---|
| representation/authority/selection are one bottleneck | INV-088 (`world_goal_evaluator_bounded_by_z_world_differentiation`); the whole `conversion_ceiling_campaign` | **already-owned** -- cross-ref only |
| a modulatory signal must carry per-candidate range, not per-tick magnitude | **MECH-359** states this almost verbatim (registered 2026-06-09 from the user's own June thought) | **already-owned** -- cross-ref only |
| objects/episodes as compressed selection-relevant carriers | SD-057 `IncentiveTokenBank` (live), SD-039/MECH-292 ghost bank, ARC-080 spine | **already-owned in part** -- the carriers exist |
| **usefulness as the INDIVIDUATION criterion for an object** | MECH-278 individuates causally; nothing individuates by use | **genuinely new -> ARC-133** (rival to MECH-278) |
| **graded value delivered categorically at the consumer boundary** | MECH-359 (signal range), MECH-463 (global scalar); a `consumer sensitivity / interface collapse` search returns **0** | **genuinely new -> MECH-516** |
| **interface must be fixed before representation is testable** | INV-088/MECH-458 assert the opposite ordering (differentiate-first) | **genuinely new -> MECH-517** (explicit rival) |
| **O is both compression and CEM search geometry** | SD-080 (O frozen); nothing on the dual role | **genuinely new -> MECH-518** |
| information need as a basic drive | MECH-388 (epistemic ACTION pressure), MECH-314b (epistemic reward BONUS), MECH-443 (gain x need write priority) | **adjacent-but-distinct -> MECH-519** (a CARRIER claim: which structure holds it) |
| **cross-time prediction holds perception open** | ARC-088 (behavioural anti-collapse), SD-070 (a z_world training recipe), INV-091 (viable band) | **adjacent-but-distinct -> MECH-520** (representational, general) |
| dynamic perceptual grain | **ARC-069/070/071 + MECH-321** own this for POLICY; MECH-166 for context slots OFFLINE; part-whole search returns **0** | **genuinely new for perception -> ARC-134** |
| ephaptic regulates the level of perception | MECH-499 (content aggregation), MECH-500 (readiness authority) | **genuinely new third function -> MECH-521** |
| coherence extent sets slot count by counting | -- | **refuted by argument** (circular); recorded inside MECH-521, not registered as its own claim |

## 3. Key formulations (the load-bearing sentences)

**3.1 The funnel.** "higher level latents may be more abstract but without there
being a funnel they are not necessarily compressed to extract useful representative
values." Located precisely: ARC-004 stratifies L-space **by timescale**, so z_delta
is not more abstract, it is *slower*. Slowness is a proxy for abstraction, not
abstraction.

**3.2 The user's correction, which changed the analysis.** "Precision as previously
described and described elsewhere is not representational depth though." This
session's first collision check mapped "level of perception" onto MECH-002/003's
`tau` (temporal depth / prediction horizon) and was **wrong** -- `alpha_tau` is a
gain on prediction error at a timescale, an orthogonal axis to the grain at which
content is carved. Redoing the check on the correct axis found ARC-069/070/071,
which is what made ARC-134 possible. Recorded because the error was load-bearing
and the correction came from the user, not from the analysis.

**3.3 The over-compression guard.** "Alone what I just thought of might just end up
with horrendously over compressed representations that mean nothing." Empirically
vindicated by SD-070's own history (z_world measured collapsing to participation
ratio ~1.06) and by V3-EXQ-817a.

**3.4 The circularity.** "the number of **related** coherencies... too simple though
right?" -- correct, and the reason is that *related* presupposes the grain decision.

## 4. Affected existing claims (cross-reference only; nothing amended)

`depends_on` wiring added on the new claims points at: MECH-278, ARC-080, ARC-006,
MECH-359, SD-057, MECH-344, ARC-069/070/071, MECH-321, MECH-166, MECH-126,
MECH-288, MECH-463, MECH-464, MECH-439, MECH-346, MECH-319, MECH-294, MECH-487,
SD-080, SD-004, SD-055, SD-056, INV-088, MECH-458, MECH-443, MECH-444, SD-049,
MECH-388, MECH-314b, ARC-088, SD-070, INV-091, MECH-006, ARC-004, MECH-140,
MECH-450, MECH-089, MECH-499, MECH-500, MECH-228, Q-077.

**No existing claim's status, confidence, evidence record, or text was modified in
this pass.** Confirmed by diff: the only change to `claims.yaml` is an append.

**Two live conflicts are registered deliberately** (user instruction, 2026-08-26:
register mutually exclusive claims so testing and literature can adjudicate):

- **ARC-133 vs MECH-278** -- rival object-individuation criteria.
- **MECH-517 vs INV-088/MECH-458** -- rival experimental orderings.

Both follow REE's existing "conflict with X, pending adjudication" idiom (cf.
ARC-022, MECH-006/MECH-085).

## 5. Candidate claims -- REGISTERED this pass

| id | one-line | phase / epistemic |
|---|---|---|
| **ARC-133** | selection-relevance as an object-individuation criterion (rival to MECH-278) | v4 / substrate_conditional |
| **ARC-134** | the unit of percept is dynamic, not fixed (perceptual ARC-069) | v4 / substrate_conditional |
| **MECH-516** | graded value, categorical interface | v3 / standard |
| **MECH-517** | interface before representation (rival ordering) | v3 / standard |
| **MECH-518** | one tensor, two masters (O as compression AND CEM search geometry) | v3 / standard |
| **MECH-519** | epistemic value is episode-borne, not object-borne | v4 / substrate_conditional |
| **MECH-520** | predictive obligation as representational anti-collapse | v4 / substrate_conditional |
| **MECH-521** | settling-derived slot occupancy; the field as coupling constant | v4 / substrate_conditional |

Architecture doc: [`docs/architecture/selection_relevant_representation.md`](../../docs/architecture/selection_relevant_representation.md).

## 6. Next steps

1. **`/governance` routing decision on MECH-518.** It is the one claim cheaply
   testable on existing V3 substrate (record `cand_world_pairwise_dist` under
   V3-EXQ-817a's ARM_0 vs ARM_1). Deliberately NOT queued here -- the re-derive
   brake is live on neighbouring lineages and the routing call is governance's.
   Its result also determines how V3-EXQ-817a should be read, which bears on SD-004,
   SD-080, ARC-133 and MECH-517 simultaneously.
2. **`/governance` fork decision on ARC-133**: fourth coregistered facet under
   ARC-080's OBJ-1, or primary criterion demoting MECH-278 to evidence.
3. **Literature to pull before hardening** (none load-bearing for registration, none
   verified in this pass):
   - ARC-133: affordance-based categorisation (Gibson); teleological/functional
     categories in infant cognition (Gergely & Csibra); predator-category
     literature unifying causally-dissimilar items by relation-to-organism.
   - MECH-520: value-equivalent models (Grimm et al. 2020), bisimulation metrics
     (Ferns et al.), MuZero's reconstruction-free latent -- **already an intake lane**
     (`REE_convergence/sources/muzero/`, CDQ-005), so this is translation not import.
   - MECH-521: the settling/occupancy claim specifically. The 2026-06-06 binding pull
     (Lisman & Jensen, Fries, von der Malsburg, Locatello) is on file but was pulled
     for BINDING, not for grain regulation.
4. **Deliberately left unregistered:** the naive "count the related coherencies"
   mechanism (refuted by argument inside MECH-521); and a build spec for the
   object-field soft bank read (a substrate design, not a proposition -- it belongs
   to `/implement-substrate` if ARC-133 is ever routed).
5. **`/thought-digestion` is owed on all eight.** Per the ingestion skill this pass
   stops at `candidate` and deliberately drafts no `what_would_answer`.

## 7. Honest limits of this pass

- The **833-line development doc** contains the evidence; this intake is a summary
  and should not be read as the argument.
- **MECH-516's affect instance is contested** by MECH-464 and the pattern rests on
  the other three instances. Recorded in the claim's own `notes`.
- **MECH-517 has a result cutting against it** (the 734/737b/742a autopsy explicitly
  rejects `substrate_ceiling` on the representation). Recorded in its `notes`.
- **MECH-521 carries a real negative** (V3-EXQ-725a failed coherence-specificity
  1/6). Recorded in its `notes`.
- No literature was pulled or verified in this pass. Every lit anchor above is
  named as a recommendation, not as support.
