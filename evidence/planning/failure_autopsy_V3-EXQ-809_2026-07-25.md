# Failure Autopsy — V3-EXQ-809 (SD-004 unknown-direction)

**Generated:** 2026-07-25T17:59:14Z
**Scope:** single · **Status:** confirmed (user-gated) · **Kind:** flagged PASS (unknown direction)
**Run:** `v3_exq_809_sd080_action_object_init_invariance_20260723T061050Z_v3`
**Queue:** V3-EXQ-809 · diagnostic · PROMOTES NOTHING
**Tagged claim:** SD-004 · **Also bears on:** SD-080 · **Outcome:** PASS · **Direction:** unknown → adjudicated
**Substrate:** `71a91095…` · machine ree-cloud-2 · 3 seeds · recording-core complete

---

## 1. Facts

809 is the "cheaper prior probe" the SD-080 scoping spike (`action_object_invariance_spike_2026-07-22.md` §4.2) prescribed: re-run the EXQ-003 TERRAIN-vs-RANDOM contrast with `E2.action_object_head` re-initialised at several random seeds. All 4 preconditions passed (ao_head_reinit_divergence 9.94 ≫ 0.1; cem_elite_refit_consumed_action_objects 1.0; d2_cross_seed_spread 2.14 ≫ 0.02; residue_field_shaped_by_warmup_harm 52 ≫ 1). Both criteria non-degenerate.

- **C1_mechanism_proposal_invariance (non-load-bearing): NOT invariant.** Re-drawn heads shift first-action distributions (pairwise TV up to 0.15; ao_param L2 9.94). The head content **reaches the CEM proposals**.
- **C2_behavioural_init_effect_below_seed_noise (load-bearing): PASSED.** Behaviour is invariant to AO-head re-init.

Label: **`ao_content_reaches_proposals_but_not_behaviour`** — O's content is not behaviourally load-bearing.

## 2. Provenance and the SD-080 finding

The 2026-07-22 spike found `E2.action_object_head` receives **zero gradient** from every REE training path: O is a frozen random projection fixed at initialisation, **state-invariant** (99.5% of variance explained by action label; head params bit-identical after 40 warmup episodes), not the "learned world-effect compression" SD-004's design doc specifies. SD-080 was registered from that spike (`candidate`, `depends_on: [SD-004, ARC-018, SD-056]`). 809 is the live behavioural confirmation of that static finding, and session `dazzling-taussig-f58f4c` is concurrently fleshing out SD-080 + an SD-004 cross-reference note.

## 3. The unknown-direction adjudication

The spike **pre-declared both directions** for this exact result. 809 lands on the *"defect is real but not load-bearing"* branch: O's content is not what produced EXQ-003's survival advantage — **terrain/residue navigation is the operative mechanism.** W.r.t. the tagged claim SD-004 this splits by sub-claim:

| SD-004 sub-claim | 809 effect |
|---|---|
| Behavioural validation (EXQ-114 99.2% harm reduction; EXQ-003 6× survival) | **Untouched.** 809 re-inits head *content*, does not ablate the pathway. SD-004 stays `implemented`. |
| Efficiency / "semantically-grounded learned compression" rationale | **does_not_support.** The semantic grounding is behaviourally inert. |
| SD-080 (frozen random projection) | **supports.** Content reaches proposals, washes out behaviourally = the prediction. |

The "unknown" was an un-hardcoded diagnostic label, not genuine measurement ambiguity — the run is clean and decisive.

## 4. Biological / claim triage

This is a **formal-vs-functional import** issue, not a biology gap. SD-004's doc asserts a *learned* compression to world-effects; nothing trains the head. The divergence between the asserted mechanism (semantic grounding) and the operative one (terrain/residue) is **load-bearing by default**. No lit-pull owed — the spike already diagnosed it.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **SD-004 does_not_support (rationale) · SD-080 supports** | behavioural PASS preserved; rationale demoted |
| Biological reference | **formal import** | asserted learned compression never trained |
| Prerequisites | **the gap IS the finding** | head needs a consequence-grounding objective it never receives |
| Implementation | **correctly placed, untrained** | call sites/consumers fine; missing training objective |
| Environment | **adequate** | CausalGridWorldV2; replicates EXQ-003 |
| Measurement | **adequate & decisive** | all 4 preconditions passed; C2 denominator non-degenerate |
| Integration | **coupled at proposal, decoupled at behaviour** | CEM reads the head; content does not reach behaviour |
| Scale | **adequate** | — |

**Recommended `epistemic_category`: `standard`** (both claims). **`narrow_supports_flag: true`** — SD-004's surviving mechanistic support is now single-pathway: the harm-reduction/survival PASSes stand, but their mechanism is attributed to terrain/residue navigation, not O's semantic grounding.

## 6. Draft `evidence_quality_note` (governance to write)

> V3-EXQ-809 (2026-07-23, action-object init-invariance prior probe; diagnostic; confirmed failure_autopsy_V3-EXQ-809_2026-07-25; PROMOTES NOTHING). The "cheaper prior probe" from the SD-080 spike §4.2: re-run EXQ-003 TERRAIN-vs-RANDOM with `action_object_head` re-initialised at several seeds. RESULT (`ao_content_reaches_proposals_but_not_behaviour`): re-drawn heads differ (ao_param L2 9.94; first-action TV up to 0.15) and reach the CEM proposals (C1 rejected), but load-bearing C2 shows behavioural init-effect BELOW seed noise — O's content is NOT behaviourally load-bearing. All 4 preconditions passed; both criteria non-degenerate. DIRECTION w.r.t. SD-004: **does_not_support, SCOPED to SD-004's efficiency / semantic-grounding RATIONALE ONLY.** SD-004's behavioural validation (EXQ-114 harm reduction; EXQ-003 survival) is EXPLICITLY PRESERVED and SD-004 STAYS implemented — 809 does not touch the MAP_NAV pathway, only head content. Per the spike's pre-declared "defect real but not load-bearing" branch: SD-004's efficiency rationale is demoted (the actual mechanism producing EXQ-003's survival is terrain/residue navigation). SUPPORTS SD-080 (frozen random projection; correctness-not-capability finding).

## 7. Routing (user-confirmed)

1. **Governance-apply** the direction adjudication above (SD-004 `does_not_support` rationale-scoped, behavioural PASS preserved; SD-080 `supports`).
2. **Chippable `/queue-experiment` follow-on** — the spike §4.2 **3-arm consequence-grounding falsifier** (ARM_0 frozen / ARM_1 consequence-grounded / ARM_2 shuffled-target control), testing the orthogonal **capability** question (would grounding O improve planning?). This is `/queue-experiment` work (a new scientific question), so it is chipped, not inlined. Coordinate with `dazzling-taussig-f58f4c`. Substrate build for SD-080 is `complicated (buildable)` but the spike says explicitly: do not widen without the falsifier first.

## 8. Hypothesis-space ledger (Step 9b): skipped cleanly

809 emits no `fanout_recommendation` and there is no registered hypothesis-space question owned by SD-004 or SD-080. The §4.2 3-arm falsifier is a genuine future discrimination portfolio — pre-register its legs (Mode A) when it is queued, not now.
