# Thought Intake -- 2026-09-24 -- from components that work to an organism that works

**Date:** 2026-09-24
**Raw thought file:** `docs/thoughts/2026-09-24_from_components_to_functional_organism.md`
**Session:** `thought-organism-path-20260924` (umbrella main checkout, Mac)
**Digestion drafts:** `evidence/planning/thought_digestion_staged_2026-09-24_from_components_to_functional_organism.md` (draft-only; not applied)
**Orchestrator execution prompt (special output requested by the user):** `evidence/planning/orchestrator_execution_prompt_2026-09-24_functional_organism_path.md`

**Registration status: REGISTERED as MECH-586 (2026-09-24, chip-20260924-mech586-register).** The
section 6 YAML was applied verbatim to `claims.yaml` (id MECH-586 confirmed free at write time; max was
MECH-585), with `location: docs/architecture/precision_control.md#mech-586` and a registration line in
`notes`. It was originally staged, not applied, because `governance-20260924-workset` owned
`claims.yaml` during this intake pass. The digestion `what_would_answer` draft is NOT yet applied;
it awaits the user's approval.

## 1. Verbatim prompt

The user's seeds are quoted in the raw file:

> "It always tastes very close to working. But it really feels close now"
> "And what are the pieces needed to get it working? Do we know them now for sure?"
> "Could you look into this more to create a thought document which maps the path to functional organism"

The body is an assistant-authored evidence synthesis written at the user's request, frozen at
REE_assembly `d3b73c9ec9` and ree-v3 `4fc6f3d0f3`. It is treated here as a proposal. Its thesis:

- **What exists:** a better map of the necessary functions and several real failures.
- **What is missing:** a proven sufficient set of repairs.
- **The target:** a reproducible closed learning loop, not "install the remaining modules." In that
  loop the organism detects a consequential distinction, predicts what its own alternatives would
  change, selects and executes, experiences the outcome, and improves later choices without losing
  earlier competence.
- **The working hypothesis:** "decision-useful information surviving each handoff."

The user asked that an execution prompt for a `/metaworker-orchestrate` session be produced from it.

## 2. Premise re-measurement (CLAUDE.md "audit its premises")

Every factual premise was re-measured against state at about 07:10-07:20Z, after the thought's freeze.

| Premise in the thought | Re-measured | Verdict |
|---|---|---|
| pending_review lists 7: V3-EXQ-1077, 1078, 1012c, 1081, 1080, 1082 (diagnostics) + the 1066 ERROR | Same 7. Drafts exist for the six non-1066 items at `evidence/planning/failure_autopsy_V3-EXQ-{1077,1078,1012c,1080,1081,1082}_2026-09-24.json`, all `awaiting_human_confirmation`, none in `review_tracker.json`. 1066 has no autopsy. | **HOLDS; moved forward.** Drafted by `governance-20260924-workset`, not yet confirmed. |
| 1078 carries a vacuity flag; 1081 has a route-specific unmet precondition | 1078's draft autopsy agrees with the indexer's `vacuous_pass`. 1081's `precondition_unmet` is scoped to C3 only (`curiosity_route_positive_control`); C1 and C2 are met. | **HOLDS.** The 1081 draft also raised GFLAG-0437: SD-PP-B1's "no native route to E3" premise is false. |
| The world-forward-consumer entry still says "no native route" | The `SD-PP-B1` title in `substrate_queue.json` still says so (`proposed_REGISTRATION_ONLY`). | **HOLDS.** GFLAG-0437 routes the fix and has not been applied. |
| CURRENT_FRONT carries stale "queued/running" and re-pose-pending text despite the confirmed 09-23 re-pose | `docs/CURRENT_FRONT.md:15` says "V3-EXQ-1010 ... is queued and running". Line 17 says the re-pose is routed "(GFLAG-0312) ... until it happens". `failure_autopsy_zworld_actor_adequacy_locus_repose_2026-09-23.json` is `status: confirmed`. | **HOLDS.** Fix the source, then regenerate. Do not hand-edit the page. |
| Workset: 260 items, 33 ready, 0 in flight | `inter_governance_workset.v1.json` (generated 06:04:43Z): 260 / 33 / 0. Top ready at priority 25: IGW-219 sd105, IGW-220 SD-ZWORLD-SENSE-PATH-PARITY, IGW-221 SD-PP-B9, IGW-222 sd032b. | **HOLDS.** "0 in flight" is still a workset field only. In flight right now: the governance session, `igw-241` reserving V3-EXQ-1083, and the orchestrator science lane `science-20260924-sdppb5-alpha09` (launched 04:24Z on the Mac). |
| Candidate effort = `c.actions.shape[1]` | `ree-v3/ree_core/agent.py:7788` | **HOLDS.** See section 5, T4, and GFLAG-0447. |
| Closure dashboard: 72.3% / 34 remaining / 11 assembly-frontier | `closure_dashboard.md`: 72.3%, "64 done, 34 remaining, 10 deferred", 11 on the assembly frontier. | **HOLDS.** |
| SD-PP-B10/B11 are registration-only; sd105 is registration-only; SD-ZWORLD-SENSE-PATH-PARITY must not be restored | B10 and B11 are `proposed_REGISTRATION_ONLY`. SD-ZWORLD-SENSE-PATH-PARITY is `registered_no_build_owed_hygiene_path_divergence`. **sd105 is `pending_implementation`, `ready: true`** (IGW-219), not registration-only. | **PARTLY FALSE for sd105.** It is a ready build. The user HELD it on 2026-09-24 (orchestrate-20260924-0407) until the fresh-login re-raise at 2026-09-25T18:00Z. |
| "Generic SD-081 confirmation: first examine V3-EXQ-811a" | 811a exists (`evidence/experiments/v3_exq_811a_mech477_dualsystem_arbitration_falsifier/`). It credits **MECH-477**, not SD-081. V3-EXQ-1083 (the SD-081 adaptive-vs-fixed allocation falsifier) is being reserved right now by claim `igw-241-proposal-for-sd-081-exq-1083`. | **HOLDS, sharpened.** The warning is live: 1083 is being authored today. Whether 811a already answers part of its question is that session's call to check. |
| `sd106_objective_consumer_transfer` owns the encoder-to-consumer problem | It is a hypothesis-space question id (`hypothesis_space_registry.v1.json`), not a `substrate_queue` entry. | **HOLDS** (the id's kind is corrected). |

**Live context the thought did not have:**
- **Coordination plane:** PAUSED by `governance-20260924-workset`.
- **Cloud dispatchers:** ree-cloud-4 and ree-cloud-5 PAUSED until `clear_at 2026-09-25T18:00:00Z` (`scripts/dispatcher_pauses.json`, reason `account-handover-to-gmail-20260924`).
- **Experiment queue:** STARVED, depth 1 (only V3-EXQ-1067) against a floor of 3.
- **User decisions:** IGW-219 (sd105) and IGW-222 (sd032b) builds are HELD until that re-raise.

## 3. Key formulations (verbatim from the raw file)

- "The useful target is therefore not 'install the remaining modules.' It is to establish a reproducible closed learning loop"
- "a substantial part of the remaining difficulty lies in decision-useful information surviving each handoff"
- "A model can produce different predictions for different actions and still rank their consequences incorrectly."
- "Lower confidence in a hazard model does not establish safety."
- "A yoked trace alone cannot establish the benefit of actions that its comparison arm never executes."
- "If multiple causes coexist, abandon the assumption of one last missing piece."
- "If a competence loss can be removed by deleting a subsystem, that is positive progress, not a defeat for the programme."

## 4. Literature

The raw file's four anchors (Grimm 2020; Janner 2019; Pathak 2019; Keramati & Gutkin 2014) are cited
as design constraints, not as validation, and no REE confidence moves on them (`feedback_lit_exp_decoupled`).
Grimm's value equivalence is already cited by MECH-520. No independent verification pass was run
this session. None of the anchors is load-bearing for the one staged claim.

## 5. What is new vs. existing REE docs/claims

Cross-referenced against `docs/claims/claims.yaml`. Line numbers are as read at about 07:15Z. Claim
text was read, not token-matched.

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| **T1.** Closed learning loop as the target | **GOV-JURIS-1** (~103132): organism validation is a profile over D0-D7, not a scalar (defined in `docs/architecture/organism_level_validation_doctrine.md`; long form `evidence/planning/organism_level_validation_doctrine_20260916.md`). **ARC-130**: existence -> committed throughput -> ecological consequence -> retention. **ARC-131**: pass-in-isolation vs fail-in-composition. **ARC-120**: competence before authority. | **Already owned.** The loop sentence restates D3 + D4 + ARC-130 retention. |
| **T2.** Milestones A (minimal closed-loop agent) / B (integrated organism) / C (strict V3 closure) | No claim-shaped milestone ladder exists. By design, milestones are programme facts. A ratified milestone already exists: "viable minimal working intelligence achieved" (`thought_intake_2026-08-29_MILESTONE_...md`). Doctrine section 11 gates any further minimal-working-intelligence event behind **Q-108**. C = the closure plan. | **Already owned. Not registered.** **Reconciliation owed:** Milestone A here is a D3-scoped operational test in a declared task. It is NOT a rival to, or re-litigation of, the 2026-08-29 programme milestone. |
| **T3.** Difference vs correctness vs usefulness of action-conditioned futures (sec 5.1) | **ARC-002** (strong vs weak form; divergence "necessary but not sufficient"). **SD-013** falsifier: "the margin loss then buys action-sensitivity without buying causal identifiability". **SD-056** (action contrast as the learned target). **MECH-567/568** (encoder-to-consumer transfer). | **Already owned.** V3-EXQ-1082 should be tagged against SD-013 / ARC-002 when governance confirms its autopsy. |
| **T4.** Harm level / expected harm / prediction error / reliability / effort are distinct at the E3 boundary (sec 5.2) | **SD-011** (sensory vs affective harm). **MECH-069** (harm error not collapsible). **MECH-059** (confidence distinct from residual). **MECH-510** (prediction vs error precision). **MECH-359** (separate harm and effort channels). **Q-080** (is effort a harm or a foregone value? open). **MECH-354** (effort axis decoupled from harm). | **Already owned as claims. Found a concrete live defect in one ready build instead:** `sd032b-candidate-effort-proxy`'s `implementation_hint` names "a harm-forward rollout cost per candidate" as the effort producer. That would double-count harm against MECH-354. It pre-empts Q-080. It depends on the harm-forward head that V3-EXQ-1062a found worse than persistence in 6/6 cells. **Raised GFLAG-0447** (REE_assembly `bc7edc2465`, `evidence_discrepancy` on SD-032b / MECH-354 / Q-080) so the IGW-222 re-raise carries it. |
| **T5.** Uncertain danger must not become cheap danger (sec 5.3) | **MECH-485**: a magnitude + confidence pair fans out to three consumers; low confidence routes to orient/survey. **MECH-388**: pressure toward information gathering under hidden-state harm. **MECH-454**: uncertainty-gated option preservation, own options only, not harm. **Q-027**: irreversibility under uncertainty. **ARC-052** (`harm_precision_weighting`, candidate, v3) points the OTHER way: "E3's use of harm streams is weighted by their respective precisions", implemented as "E3 weights inputs by exp(-log_sigma)", so low-precision harm gets LESS influence. Its E3-weighting half (A) is unbuilt. **SD-PP-B11** (registration-only) would build a harm-reliability module. | **Adjacent but distinct. Register narrowly** (section 6). The delta is an asymmetry no claim states. Harm-forecast uncertainty may redirect control (investigate, shorten the trusted horizon, preserve alternatives) and may lower the authority of the forecast to UPDATE beliefs. It must not lower the weight of expected adverse cost in candidate ranking. MECH-485 says where low confidence routes, not whether cost is discounted. ARC-052 as written would discount. |
| **T6.** Pair a yoked internal-handoff diagnostic with an autonomous closed-loop evaluation | **GOV-JURIS-1** ("a live selection perturbation at most D2"; a yoked trace is D2, own-choice execution is D3), **GOV-PATHVALID-1**, **GOV-INTERVENE-1**, **GOV-BEHADJ-1**; the doctrine's D0 section already requires a self-yoked control. | **Already owned.** At most, a one-line GOV-JURIS-1 note that yoked readouts (`yoked_divergence_frac`) reach at most D2. Left to `/governance`. |
| **T7.** Reach is not benefit (V3-EXQ-1081 ranking reach through the proposer -> `rollout_with_world()` -> `world_forward()` route) | **ARC-130** (authority is not throughput is not ecological consequence), **GOV-JURIS-1**. | **Already owned.** Handle through the 1081 autopsy's evidence-domain line (at most D2). |
| **T8.** Deletion / simplification counts as progress | **GOV-DELETE-1** (near-verbatim), GOV-CONTRACT-3, ARC-140 (doctrine D6). | **Already owned.** |
| **T9.** Adaptive recovery after an unannounced environment change (Q-108) | **Q-108** (`open_question`, `substrate_conditional`, v4). AR-1 cue remapping is the nearest V3-expressible class, already flagged for `/governance` routing. | **Confirmed. Cross-reference only.** |
| **T10.** Separate the three ready items from the full organism path; the sequenced plan (sec 7) | A planning contribution, not claim-shaped. | **Not registered.** Carried into the orchestrator execution prompt, which is where a sequencing proposal belongs. |

## 6. Candidate claims -- STAGED for registration (not applied; see header)

One claim. Everything else in the thought is owned (section 5).

```yaml
- id: MECH-586   # PROVISIONAL -- re-check max MECH id at write time
  title: 'Harm-forecast uncertainty redirects control but does not discount expected adverse cost in
    selection: low confidence in a hazard prediction may lower that prediction''s authority to update
    beliefs, and may route control toward investigation, a shorter trusted planning horizon, or
    preservation of alternatives (MECH-485 orient/survey leg), but it must not by itself lower the
    weight that the predicted adverse outcome carries in E3 candidate ranking. Update-authority
    precision, prediction confidence, and adverse-outcome cost are three separable quantities at the
    E3 integration boundary.'
  claim_type: mechanism_hypothesis
  subject: harm_stream.uncertainty_not_discount_asymmetry
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v3
  version_relevance: v3_v4
  registered_utc: '2026-09-24'
  source_thought: docs/thoughts/2026-09-24_from_components_to_functional_organism.md
  location: docs/architecture/<TBD at registration -- harm-precision doc if one exists, else new stub>#mech-586
  depends_on:
  - ARC-052
  - MECH-485
  - MECH-510
  - MECH-059
  - SD-011
  - ARC-016
  source:
  - docs/thoughts/2026-09-24_from_components_to_functional_organism.md
  - evidence/planning/thought_intake_2026-09-24_from_components_to_functional_organism.md
  notes: 'Registered from thought 2026-09-24 sec 5.3 ("Uncertain danger must not automatically become
    cheap danger"). WHAT IT CONSTRAINS: ARC-052 (harm_precision_weighting) half (A) as written --
    "E3 weights inputs by exp(-log_sigma)" -- would make a low-precision harm forecast count LESS in
    selection; this claim asserts that is the wrong use of harm precision for the COST term, while
    leaving ARC-052''s attribution/commit-gating use and its precision-estimation half (B, V3-EXQ-977
    PASS) untouched. It is a boundary on ARC-052 and on SD-PP-B11 (registration-only harm-reliability
    module), to be read BEFORE either one''s E3-weighting half is built. WHAT IT IS DISTINCT FROM:
    MECH-485 (where low confidence ROUTES -- orient/survey -- not whether cost is discounted; this
    claim is compatible with and depends on it); MECH-510 (prediction vs error precision -- this claim
    uses the update-authority side of that split); MECH-454 (uncertainty-gated option preservation for
    the agent''s OWN options, explicitly not harm); MECH-388 (information-gathering pressure under
    hidden-state harm -- one of the redirect consumers, not the no-discount constraint); Q-027
    (defining irreversibility under uncertainty). FALSIFIER SHAPE (draft; digestion owns it): in a
    world with genuinely uncertain hazard forecasts, discount-by-precision should produce MORE
    realised avoidable harm than redirect-without-discount at matched reward and matched exposure;
    if it does not (or the redirect policy starves reward with no harm benefit), the asymmetry is
    unnecessary. Precondition: the harm-forward forecast must beat persistence (V3-EXQ-1062a found
    it did not, 6/6), otherwise there is no forecast whose confidence could matter. DO NOT build in
    V3. DO NOT queue an experiment. Route to /governance for a V3-vs-V4 routing decision: the claim
    is a design constraint on v3-phase ARC-052, but has no producer to test until a per-stream harm
    precision head and a better-than-persistence harm forecast both exist.'
```

If `/governance` prefers not to add a claim, the minimum acceptable alternative is a boundary note on
ARC-052 and on SD-PP-B11 carrying the same asymmetry. It must land before either one's E3 harm-weighting
half is built.

## 7. Affected existing claims

- **Cross-referenced (no edit):** GOV-JURIS-1, ARC-130, ARC-131, ARC-120, ARC-002, SD-013, SD-056, MECH-567, MECH-568,
  MECH-520, SD-011, MECH-069, MECH-059, MECH-510, MECH-359, MECH-354, Q-080, MECH-485, MECH-388, MECH-454, Q-027,
  ARC-052, GOV-DELETE-1, GOV-CONTRACT-3, ARC-140, Q-108, ARC-149, MECH-580.
- **Flag raised:** GFLAG-0447 (SD-032b / MECH-354 / Q-080). **Flag pre-existing, confirmed relevant:**
  GFLAG-0437 (SD-PP-B1 premise false, from the 1081 draft autopsy), GFLAG-0312 (the re-pose, now confirmed;
  the CURRENT_FRONT text trails it).
- **Nothing's status, confidence or evidence record was touched.** `claims.yaml` was not edited.

## 8. Next steps

1. **Apply the section 6 registration** once `governance-20260924-workset` releases `claims.yaml`.
   Choose `location`, re-check the max id, run `validate_claims.py --strict`, `build_claims_json.py`,
   and commit via `ree_commit.py`. Then update the raw file's `Claims registered:` line.
2. **Governance items this thought surfaces (routed, not performed):**
   - Confirm the six draft autopsies.
   - Tag 1082 against SD-013/ARC-002.
   - Record 1081 at most D2.
   - Apply GFLAG-0437 (SD-PP-B1 title).
   - Fix the CURRENT_FRONT source text trailing the 09-23 re-pose, then regenerate.
   - Disposition GFLAG-0447 before IGW-222 is re-raised.
   - Route the staged MECH-586.
3. **Milestone reconciliation:** any programme write-up that uses "Milestone A" must say it is a
   D3-scoped operational test and cite the 2026-08-29 ratified milestone. The Q-108 gate on any
   further minimal-working-intelligence event stands.
4. **The sequencing proposal (thought sec 7) goes to the orchestrator execution prompt**, not the registry.

## 9. Digestion drafts

`evidence/planning/thought_digestion_staged_2026-09-24_from_components_to_functional_organism.md`
drafts `what_would_answer` and a disposition for the staged MECH-586. It is draft-only, lands in the
same commit as this intake, and nothing in it is applied.
