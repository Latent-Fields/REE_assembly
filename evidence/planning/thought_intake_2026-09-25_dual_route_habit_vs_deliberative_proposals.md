# Thought Intake: Two Proposal Routes -- Habit (Action Space) and Deliberative (Abstract Action-Object Codec)

**Date:** 2026-09-25
**Raw thought file:** `docs/thoughts/2026-09-25_dual_route_habit_vs_deliberative_proposals.md`
**Session:** bt0925-dualroute (headless intake worker under orchestrate-20260924-breakthrough; chip `chip-20260925-dual-route-proposals-claim`)
**Registration state:** one candidate MECH is DRAFTED here (section 6) and was **NOT registered in this pass**. The `claims.yaml` claim was refused by arbitration (exit 3; owner `igw-auto-igw-221-substrate-ready-sd036-eval-repli-20260925T133629Z`, SD-036 implement-substrate). The brief's fallback applies: `/governance` registers it from the paste-ready block in section 6. See the resume note there.

## 1. Verbatim prompt (core proposal)

The user made these remarks live, while the orchestrator was explaining the coupled loop-repair campaign's two proposal mechanisms: action-space proposals (ASP, row W1-alt, landed on `integration/coupled-loop-repair` at ree-v3 `1a16595`) and the abstract action-object codec (row W1, being built).

> "I hope the abstract space one wins. It seems more cognition like."

> "It seems a bit like both exist in my mind. One for habits and one for more complex behavioural additions"

The proposal: REE should not have to choose between the two generators. Both kinds of candidate generation belong in one agent, as two concurrent routes.

- A **habit route** proposes directly over the primitive action repertoire. It is cheap, close to motor output, and exact when the repertoire is small (ASP).
- A **deliberative route** proposes in a learned abstract action-object space. It is state-dependent and supports composing novel multi-step behaviour (the W1 codec, which lives in SD-004's space O).

The two routes are arbitrated. With practice, choices migrate from the deliberative route to the habit route.

## 2. Premises re-measured before drafting

| Premise (orchestrator's gloss) | Re-measured against | Holds? |
|---|---|---|
| REE already has a habit/planned split at `dualsystem_habit_depth` vs planned depth | SD-081 `implementation_note` and notes; MECH-163 title; the Dezfouli 2013 lit entry (`targeted_review_connectome_mech_163/entries/2026-07-27_...dezfouli2013`) | **Holds, but it is a SCORER-side split, not a proposer-side one.** SD-081's two pathways are two depth reads (`max(2, habit_depth)` vs full horizon) of the SAME model-based E3 scorer over the SAME candidate pool. Whatever the proposer produces, both reads score it. Nothing in REE today separates candidate GENERATION into routes. So the proposed mapping (ASP = habit proposer, codec = deliberative proposer) adds a new element. It does not reuse SD-081 unchanged. |
| Habit control runs over primitives; goal-directed control runs over abstract representations that support composition and chunking | Daw, Niv & Dayan 2005 (on file: `targeted_review_connectome_mech_163/entries/2026-04-05_mech163_uncertainty_competition_daw2005`); Dezfouli & Balleine 2013 (on file, above); Graybiel 2008 (on file: `targeted_review_action_policy_decomposition/entries/2026-04-28_action_policy_habit_chunking_graybiel2008`) | **Partly inverted by the literature REE already holds.** (a) In Daw 2005 both controllers act over the same primitive action set. They differ in VALUATION (cached vs tree search), not in how actions are represented. (b) In Dezfouli & Balleine 2013 and Graybiel 2008, the CHUNKED multi-step sequence is the *habitual* unit, and a single goal-directed process selects between individual actions and chunks. So "composition belongs to the deliberative route" is not what the chunking literature says. The reconciled reading, and the one this intake registers: the deliberative route **composes** novel combinations. A practised composition is then **cached as a habitual chunk** (ARC-071 / MECH-323 transfer). A mature habit route therefore proposes chunks as well as primitives. ASP over 5 one-hot moves is the newborn / early-practice form of the habit route, not its general form. |
| The two routes are concurrent and arbitrated | Daw 2005; Balleine & O'Doherty 2010 (on file: `.../2026-04-05_mech163_corticostriatal_balleine_odoherty_2010`) | Holds. DMS/vmPFC (goal-directed) and DLS (habitual) are concurrently active and dissociable in rodents and humans. Daw 2005 arbitrates by relative uncertainty, which is SD-081/MECH-477's rule. |
| Behaviour migrates goal-directed -> habitual with practice | Balleine & O'Doherty 2010; Graybiel 2008 | Holds (the overtraining -> habit shift). REE already registers the TRANSFER mechanism as ARC-071 (with MECH-323 / MECH-324) and a practice-maturity arbitration weight as MECH-312b. |
| In A1's regime an abstract route could beat ASP | A1 draft v3b regime (5 discrete moves); W1-alt row (ASP pool is stratified and format-homogeneous: all one-hot) | **Structurally unfavourable to the codec.** With 5 primitive moves, ASP enumerates the first action exactly, and there is no composition for an abstract space to exploit on the first step. A codec advantage can appear only where abstraction matters: multi-step continuations, chunked actions, or a larger or compositional action space. |

## 3. What's new vs. existing REE docs/claims (novelty table)

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| Two dissociable control pathways, habit vs goal-directed, concurrent | MECH-163 (restated 2026-07-27: habit = depth-limited read of the forward model, planned = full-horizon read); SD-081 (built, default-OFF) | Already owned at the **scoring** locus. Cross-ref only. |
| Arbitration by relative uncertainty or reliability | MECH-477 (arbitrator required, V3-EXQ-811a PASS); SD-081 (the weight); MECH-312a (reliability weighting); MECH-235 (vmPFC spectrum, urgency shifts toward habitual) | Already owned. The new claim reuses it and does not re-assert it. |
| Practice migrates behaviour from the deliberative to the habitual form | ARC-071 (transfer by chunking; unbuilt at the DV that matters); MECH-323 (DLS-analog chunk accumulator); MECH-324 (maintenance); MECH-312b (practice-maturity weight); Q-085 (committed-macro grain as a controllability parameter) | Already owned as a mechanism. What is new is its **observable at the proposer**: the route-of-origin share of committed choices drifting toward the habit route with practice. |
| Habit as a cached action-chunk lookup (DLS slot) | SD-045 (**retired**, superseded by ARC-071) | Distinguish. SD-045 was a cached-lookup store. The habit route here is a generator over the action repertoire, with no value cache. |
| Same-effector competition between habitual and deliberative outputs | MECH-234 (single action channel -> winner-takes-all) | Consistent. In CausalGridWorld both routes must compete for one action channel, so the routes' candidates meet in one selection and are not expressed in parallel. |
| Abstract action-object space as the planning substrate | SD-004 (action objects as the hippocampal map backbone; implemented); SD-080 (the `action_object_head` gets zero gradient, so O is a frozen random projection; the W1 codec is the repair); MECH-523 (untrained compression sites) | Owned as SUBSTRATE. What is new is using O as a proposal ROUTE that stands alongside a primitive-space route rather than replacing it. |
| **Candidate GENERATION split into two routes of different representational format (primitive action space vs learned abstract action-object space), arbitrated, with situational dominance and practice migration visible as the route of origin of committed choices** | None. SD-081, MECH-163 and MECH-477 all act on one candidate pool after generation. ARC-071 moves content between pathways without naming proposal routes. The campaign treats ASP vs codec as **rivals** in a head-to-head (rec-20260925-6a675285, rec-20260925-38b81685), not as coexisting routes. | **Adjacent-but-distinct: register narrowly** (section 6) and distinguish explicitly from SD-081's scorer-side split. |

## 4. Key formulations

- "It seems a bit like both exist in my mind. One for habits and one for more complex behavioural additions" (user, 2026-09-25).
- "I hope the abstract space one wins. It seems more cognition like." (user, earlier the same day). Recorded as a stated preference. It does not bear on the claim's truth, and A1's head-to-head stays pre-registered as it is.
- Intake's reconciled formulation: **the deliberative route composes, the habit route caches what composition has made routine.** "Primitive vs abstract" is the early-life picture. "Cached vs composed" is the general one.

## 5. Affected existing claims

- **Cross-referenced (as `depends_on` in the draft):** SD-081, MECH-477, MECH-163, SD-004, SD-080, ARC-071, MECH-323, MECH-312b, Q-085, MECH-234.
- **Distinguished from:** SD-081/MECH-163 (scorer-side depth split over one pool); SD-045 (retired cached-lookup habit store); the campaign's ASP-vs-codec head-to-head (rival framing).
- **Amended:** none. No claim's status, confidence or evidence was touched. `claims.yaml` was not edited in this pass.

## 6. Candidate claims -- REGISTERED 2026-09-26 as MECH-596 (session thought-intake-20260926)

**Why not registered:** `task_claim.py open` for `REE_assembly/docs/claims/claims.yaml` exited 3 at 2026-09-25T19:24Z. The owner is `igw-auto-igw-221-substrate-ready-sd036-eval-repli-20260925T133629Z` (IGW-20260925-221, SD-036 implement-substrate STAGED). The brief's instruction for exactly this case: do not edit `claims.yaml`; complete the intake and the plan item; leave registration as a precise resume note. The user has said they will run `/governance`.

**RESUME NOTE (for /governance or the next ingestion session):**
1. `task_claim.py open` on `REE_assembly/docs/claims/claims.yaml` and `REE_assembly/docs/assets/data/claims.json`.
2. Re-check the max MECH id at write time: `grep -oE "^- id: MECH-[0-9]+" REE_assembly/docs/claims/claims.yaml | grep -oE "[0-9]+$" | sort -n | tail -1`. It was 595 at 2026-09-25T19:26Z, so the draft is `MECH-596` if still free. Replace `MECH-XXX` below.
3. Append the block below verbatim. Either add a `#mech-XXX` anchor section to `docs/architecture/sd_081_dualsystem_uncertainty_arbitration.md` or point `location` at a new stub. The SD-081 doc is the recommended home, because the claim's main job is to be distinguished from SD-081.
4. Run `validate_claims.py --strict` and `build_claims_json.py`, then commit through `ree_commit.py` with only those paths.
5. Update the raw thought's marker: replace the `Registration pending:` line with `Claims registered: MECH-XXX`. Update this section's heading to REGISTERED.
6. Update the coupled-plan row `W1-both`, which cites "MECH-XXX (drafted, pending registration)".

```yaml
- id: MECH-XXX
  title: "dual_route_proposal_generation. Candidate actions reach E3 selection from TWO concurrently active proposal ROUTES that differ in the representational format they search: a HABIT route that enumerates or samples directly over the agent's action repertoire (primitives early in life, practised chunks later; cheap, state-light, exact when the repertoire is small) and a DELIBERATIVE route that searches a learned abstract action-object space (SD-004 O, decoded to actions), which is state-dependent and composes novel multi-step behaviour. Both routes' candidates meet in one selection (single action channel, MECH-234) under reliability arbitration (MECH-477 / SD-081), so that the habit route supplies the committed choice in familiar states and the deliberative route when novelty or composition is required, and practised deliberative compositions migrate into the habit route's repertoire (ARC-071 / MECH-323 transfer). This is a PROPOSER-side split, distinct from SD-081's SCORER-side split (two depth reads of one E3 scorer over one candidate pool)."
  claim_type: mechanism_hypothesis
  subject: hippocampal.proposal.dual_route_generation
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v3
  v3_pending: true
  version_relevance: v3_v4
  registered_utc: '<date -u +%Y-%m-%d at registration>'
  source_thought: docs/thoughts/2026-09-25_dual_route_habit_vs_deliberative_proposals.md
  location: docs/architecture/sd_081_dualsystem_uncertainty_arbitration.md#mech-xxx
  depends_on:
  - SD-081
  - MECH-477
  - MECH-163
  - SD-004
  - SD-080
  - ARC-071
  - MECH-323
  - MECH-312b
  - Q-085
  - MECH-234
  source:
  - docs/thoughts/2026-09-25_dual_route_habit_vs_deliberative_proposals.md
  - evidence/planning/thought_intake_2026-09-25_dual_route_habit_vs_deliberative_proposals.md
  notes: >
    ORIGIN: user remark 2026-09-25 (orchestrate-20260924-breakthrough), verbatim "It seems a bit like
    both exist in my mind. One for habits and one for more complex behavioural additions", on hearing
    the coupled loop-repair campaign's two proposal mechanisms described side by side: action-space
    proposals (ASP, plan row W1-alt, ree-v3 1a16595 on integration/coupled-loop-repair) and the
    abstract action-object codec (plan row W1). The campaign currently runs them as RIVALS in a
    pre-registered head-to-head (rec-20260925-6a675285, rec-20260925-38b81685); this claim asserts
    they are better modelled as COEXISTING ROUTES. That does not change A1: the head-to-head stays as
    registered, and the INT-BOTH arrangement is plan row W1-both, non-blocking.
    DISTINCT FROM SD-081 / MECH-163: those split SCORING (a depth-limited and a full-horizon read of the
    same E3 scorer over the same candidate pool; e3_selector.py _score_depth_limit). They are silent on
    where candidates come from. This claim splits GENERATION. The two splits are orthogonal (proposer
    route x scorer read is a 2x2), and the INT-BOTH design must decide the crossing, not assume it.
    DISTINCT FROM ARC-071 / MECH-323: those are the TRANSFER mechanism (chunk formation). This claim
    predicts transfer's observable at the proposer (route-of-origin share drifting to the habit route
    with practice) and uses transfer to grow the habit route's repertoire beyond primitives.
    DISTINCT FROM SD-045 (retired): that was a cached-lookup habit store indexed by state and outcome
    signatures. The habit route here generates over the repertoire and caches no values.
    LITERATURE (all already on file; no new pull made): Daw, Niv & Dayan 2005 (concurrent controllers,
    uncertainty arbitration; both act over the SAME primitive actions and differ in valuation, so this
    paper does not support "habit = primitives, deliberative = abstract"); Balleine & O'Doherty 2010
    (DMS/vmPFC vs DLS concurrency and dissociation; overtraining shifts control to habit); Dezfouli &
    Balleine 2013 and Graybiel 2008 (the CHUNK is the habitual unit). The last two invert the naive
    "composition belongs to the deliberative route" gloss. The registered reading is: the deliberative
    route composes, and the habit route caches the compositions practice has made routine. The
    abstract-space-as-deliberative-proposal-substrate element is REE-specific (SD-004). Hierarchical
    PFC action representation (Badre; Botvinick) is the right literature for it and is NOT yet pulled
    or verified.
    PREDICTION (registered with the claim; not a what_would_answer, which is left to /thought-digestion).
    Non-degeneracy preconditions: both routes pass their member gates (ASP G-ASP (a)-(d); codec W1
    (a)-(d) + containment + (f)); each committed candidate carries a route-of-origin tag; familiarity
    separates familiar from novel contexts (AUC >= 0.7, the MECH-163 bar); and the regime contains
    states where the deliberative pool holds options the habit pool lacks (checked with the env-Q
    oracle diagnostic, rec-20260925-a16786f5). Without that last condition, clause (ii) is untestable.
    With both routes present and arbitrated: (i) the combination outperforms either route alone on the
    A1 criteria (paired mean), OR the routes' contributions differ by situation; (ii) the habit route
    supplies the majority of committed choices in familiar states, and the deliberative route's share
    rises in novel or composition-requiring states; (iii) with repeated exposure to a fixed layout, the
    habit route's share of committed choices in that layout rises (migration), faster with ARC-071
    chunk formation ON.
    FALSIFIED IF, with the preconditions met: (a) INT-BOTH is no better than the best single route AND
    the route-of-origin share is flat across familiar vs novel (the second route adds nothing and is not
    situationally recruited); or (b) the familiar/novel ordering of (ii) is absent or reversed; or
    (c) no practice drift appears under (iii). (a) falsifies the claim as a whole; (b) and (c) falsify
    the allocation and migration clauses respectively. A null under unmet preconditions is
    non_contributory. In A1's 5-discrete-move regime a null on (i) is EXPECTED by structure (ASP
    enumerates the first move exactly, and there is nothing to compose) and is not evidence against.
    ROUTING: implementation_phase v3 because both routes exist or are being built on the integration
    branch. The discriminating readout (composition) probably needs a regime A1 does not have. Flag for
    a /governance routing decision. DO NOT build INT-BOTH ahead of the W1 codec passing its gates. DO
    NOT queue an experiment from this registration. Registration is not build authorisation.
```

## 7. Next steps

- **Registration** (above): `/governance` or the next ingestion session, once `claims.yaml` is free.
- **Plan item:** added as row `W1-both` in `evidence/planning/coupled_loop_repair_campaign_plan.md`. It is NON-BLOCKING for A1, lands on BRANCH after W1 passes its gates, and has debt class `complex (probe-gated)`. It carries the open design items: which regime lets abstraction matter; the proposer-route x scorer-read crossing; route-of-origin tagging; pool union vs arbitration-weighted proposal budget.
- **Owed to the user, unchanged by this intake:** the pre-A1 tie rule for the INT-CODEC vs INT-ACT head-to-head (A1 O2).
- **Literature:** a light pull on hierarchical PFC action representation (Badre 2008; Botvinick 2008/2009) before the "abstract space = deliberative proposal substrate" element is hardened. It was not pulled here; the three core anchors were already on file.
- **Digestion:** none drafted. `/thought-digestion` writes the what_would_answer after registration.
