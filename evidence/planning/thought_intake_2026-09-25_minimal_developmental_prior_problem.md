# Thought Intake: The Minimal Developmental Prior Problem -- What Must an Organism Know Before It Can Learn?

**Date:** 2026-09-26
**Raw thought file:** `docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md` (804 lines, read in full)
**Session:** thought-intake-20260926. Drafted by a read-only research agent (drafting ids DP-1..DP-3),
reviewed and registered by the orchestrating session on 2026-09-26 as Q-112, ARC-157, MECH-597.
**Companion thoughts named by the raw file (read via their intakes, not re-derived):**
`2026-09-25_error_as_information_error_as_threat.md` (intake registered MECH-590/591) and
`2026-09-24_from_components_to_functional_organism.md` (intake registered MECH-586).
**Internal evidence anchors re-read:** `evidence/planning/babbling_e2_action_coverage_probe_20260925.md`
(FINAL), `evidence/planning/coupled_loop_repair_campaign_plan.md` (rows W2a, W2b, W3, N2, N5),
`evidence/planning/n5_ach_gated_unfreeze_probe_20260926.md`, GFLAG-0504 / GFLAG-0509, and the
V3-EXQ-1108 manifest (ran 2026-09-26T10:02Z, FAIL, pending review).

## Verbatim prompt (core proposal)

> How little inherited structure is enough for an organism to become learnable, and how much additional
> general structure makes development reliably tractable without smuggling in solutions to its
> environment?

The thought starts from the 2026-09-25 Phase-0 babbling result. The coded Phase 0 turned out to be the
agent's own native policy, and on most seeds it was near-monostrategy. That gave E2 nothing to learn
action distinctions from, so E2 rollouts were flat and E3 valuation had nothing to act on. The
"downstream flatness" had a developmental upstream cause. A structured, class-balanced babbler fixed E2
action discrimination. A one-off exposure was then overwritten by later narrow experience, and a
retained minority of developmental replay preserved it.

From this the thought builds four things:

1. **A classification.** Candidate developmental mechanisms are sorted on two independent axes:
   candidate-necessary vs developmental accelerator, and environment-general vs environment-specific.
   "Enabling architecture" (plasticity, memory, time, an action interface, self/world state) is a fifth
   class that is not a prior at all. It is kept out of the minimality question.
2. **A provisional candidate minimum:**
   - a valued, vulnerable self-state;
   - a small general basis for structured endogenous action ("specify how to explore an action space,
     not what the actions mean");
   - sensitivity to self-action contingency;
   - persistent but revisable memory.

   Around these sit general accelerators: PE-driven orienting, learning-progress curiosity, primitive
   persistence, developmental replay, freeze/unfreeze, chunking and splitting. There is also a
   content-general survival interrupt, keyed to deterioration of the valued self-state and not to
   environmental features.
3. **A discipline.** Prefer the least environment-specific intervention that restores development. An
   environment-specific prior is admissible only after general candidates fail, and needing one is
   itself a finding about the environment.
4. **An experimental programme.** The minimum is discovered by reduction and ablation, never guessed.
   Each removal should produce a specific predicted developmental failure. Restoring the element should
   repair development without encoding the environment's solution. Developmental trajectories are
   measured, not endpoint reward.

The thought also claims a convergence. Asking "what does an ignorant organism need?" regenerates
structures resembling axioms A1, A2 and A4 and derivations D1 and D2. It calls that convergence testable
and "not proof".

**Epistemic caution, honoured throughout:** "the candidate minimum below is deliberately provisional ...
not a claim promotion, build authorisation, experiment commission, or fixed minimal-prior
specification."

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage (id: what it already says) | Verdict |
|---|---|---|
| Sec 1 / 18: downstream E2 -> E3 -> valuation flatness can have a DEVELOPMENTAL upstream cause (behaviour exposed no action distinctions) | **ARC-074**'s WWA already names Phase 0 as "a candidate fifth locus" in the conversion-ceiling cluster (**MECH-439** F-dominance, **INV-088** representation ceiling / "differentiate-first", **MECH-457** competence floor). **MECH-588** Type A (repertoire absence) is the monostrategy etiology this is. **GFLAG-0504** (resolved) recorded the Phase-0 dead loop, and the campaign's W2a/W3 rows act on it. | **Already owned.** Cross-ref only. |
| Sec 5.2: structured endogenous action; a small generative basis used variably; "the prior should specify how to explore an action space, not what the actions mean" | **INV-073**: a developmental exploration epoch before RL is necessary, and too little exploration permanently restricts the option library. Its lit already includes **Garcia-Guzman 2026** (the thought's own first reference, corpus-verified with DOI) and Keren-Portnoy 2021. **ARC-074**: a reward-free Phase-0 babbling epoch before E3 scoring. **MECH-461** (i): an INNATE, REFINED action-primitive basis (Dominici 2011), which is not experience-free (Zeng 2021). It is the same idea as Hinnekens 2023's "small primitive set, variably recruited". **MECH-277**: action-space discovery by motor babbling before self-attribution. **SD-044**: a motor-primitive dictionary (V4, continuous control). Built substrate: `ree_core/developmental/structured_babbling.py` `StructuredBabbler` (ree-v3 main `2ea0e3c`, default-OFF; class-balanced incl. stay, runs uniform {1..4}). | **Already owned.** Cross-ref only. The 09-25 probe is D1 evidence on MECH-461's primitive-basis half, which its WWA calls "currently untested", and on ARC-074 (see Affected claims). No new claim. |
| The organism's own untrained policy is NOT a sufficient developmental source (native Phase 0 was LESS diverse than on-policy behaviour on 4/5 seeds) | Not stated in any claim. It is recorded in the babbling probe (S FAIL 1/5), the campaign decision 7b (rec-20260925-0ad0f56b) and the `StructuredBabbler` docstring. ARC-074's description still describes Phase 0 as "reward-free Hebbian ... E3 weighting suppressed", which the code never implemented. | **Owned as evidence and decision, not claim-shaped.** It belongs in ARC-074's `evidence_quality_note`, which GFLAG-0504's resolution deferred "to the W2a build". W2a has now landed, so the note is owed. Flagged, not registered. |
| Sec 5.3: self-action contingency sensitivity; changes temporally contingent on own action get preferential consideration | **MECH-277** (observe which sensory changes covary with motor output). **MECH-256 / SD-031** (forward-model comparator on the z_world reafferent stream). **SD-007 / MECH-098 / MECH-101** (reafference cancellation). **ARC-061** (comparator family). Lit: Keren-Portnoy 2021 (mobile-type contingency), Rovee-Collier 1999 (MECH-189). | **Already owned.** One point is new and folded into Q-112 as an ablation leg, not registered: "does agency emerge from generic prediction WITHOUT a contingency bias?" Note: V3's E2 world head is action-conditioned by construction (`e2_fast.py` `world_action_encoder`). No separable contingency-bias lever exists today, so "remove contingency bias" would currently also remove enabling architecture. |
| Sec 5.1 / 11: a valued self-state grounds "better/worse" before environmental goals exist (homeostatic RL, Keramati & Gutkin 2014) | **INV-095** (A2: existence has value). **INV-030** (viability relative to continuity, not scalar reward). **SD-012** homeostatic drive (Keramati & Gutkin 2014 already in its notes and corpus). **INV-069** (self as a dynamically sustained process; Laurencon 2021 homeostatic RL, corpus 2026-09-24). **ARC-138** regulation-first organisation: the earliest organising axes of z_world are relations to the organism's own regulatory constraints ("what changes me / what I can change / what is controllable"). That is sec 3's "first useful coordinate system". | **Already owned.** Cross-ref only. **Registry gap noted, not filled:** D1 and D2 are "(pending INV)" in `five_axioms_foundations.md` sec Architectural Mapping and have no registered claim. |
| Sec 3: early action constructs self / action / consequence / controllability as representational categories (Kanazawa 2026) | **ARC-138** (regulation-first; machine -> regulation -> interaction -> organised experience -> knowledge). **ARC-059** (self -> objects -> others ordering). **MECH-276** (scientist-agent). **MECH-570** (the self stage is not primitive at the level of self-knowledge). | **Already owned.** Kanazawa 2026 is NOT in the corpus (unverified). |
| Sec 6: an innate content-general survival interrupt. "Extreme deterioration in the valued self-state interrupts the current trajectory." Primitive preservation vs learned avoidance. | **SD-032c** (AIC-analog interoceptive-salience / urgency interrupt over drive + z_harm_a). **MECH-104** (unexpected harm spikes commitment uncertainty -> de-commitment). **ARC-046** (infant-stage hazard protection without catastrophic residue saturation). **MECH-279** (PAG freeze gate). **SD-099 / MECH-489** (defensive orienting). **SD-037** (override regulator). | **Mechanism already owned.** The one new element is the **content-generality constraint**: the innate interrupt must be keyed to self-state deterioration, never to environment features ("hazard tile -> LEFT"). It is folded into ARC-157 as the worked example of the general/env-specific axis, not registered alone. |
| Sec 7: PE-driven orienting may be derivable rather than hard-coded | **MECH-482 / MECH-483** (epistemic deficit -> orient/survey). **MECH-395** (cue-triggered orienting). **MECH-489** (defensive orienting). **MECH-327** (already cites Stahl & Feigenson 2015 for PE-targeted probe actions in play). **MECH-590** (registered 2026-09-25: the control significance of a PE is a LEARNED route, which is exactly the "orienting may emerge as a learned response" hypothesis). | **Already owned.** Cross-ref only. The "derivable?" test is folded into Q-112's ablation menu. |
| Sec 7: learning-progress curiosity as a later developmental achievement (needs a prediction history) | **MECH-314c** (learning-progress bonus, substrate landed). **MECH-455** (competence-based IM). **Q-044** (are 314a/b/c distinct). **ARC-136** (play frontier migrates as learning progress saturates; a developmental curriculum). | **Already owned.** The "not birth-level" ordering is a prediction for MECH-314c / ARC-136 digestion, noted in Q-112's accelerator register. Not registered. |
| Sec 7: primitive persistence (actions continue long enough for consequences to be observable) | Built into `StructuredBabbler` (persistent runs; persistence 0.68 in its contract). **MECH-490** (sleep and action-run coherence). | **Owned as substrate.** Not claim material. |
| Sec 7 / 18: developmental replay and PROTECTED RETENTION. One-off exposure is overwritten by later narrow experience; a retained minority preserves it. | **MECH-334**: critical-period closure. Without closure, diversity representations stay "vulnerable to gradient-driven overwriting". This is a PLASTICITY-REDUCTION mechanism on the SCORING/POLICY plane (EWC anchor). **MECH-496** extends that schedule to representational structure. **MECH-165**: offline (sleep) replay must sample trajectory-diverse content to keep multi-strategy viability. **INV-073** asserts the opposite direction: early DEFICITS are permanent. **ARC-074** asserts a one-off epoch. The campaign ADOPTED retained replay (decision 7b; W3 member gate (b) retention 5/5, frozen encoder). V3-EXQ-1108 (N2, ran 10:02Z today, FAIL, pending review) tested it under encoder training. | **Adjacent but distinct -> registered narrowly as MECH-597.** No claim states that developmental WORLD-MODEL (E2 action-consequence) knowledge is non-durable under narrower on-policy training, or that the remedy is REHEARSAL (retained replay) rather than plasticity reduction. The evidence exists (D1) but lives only in planning records. |
| Sec 8: freeze, destabilise, revise. Reliable knowledge resists incidental overwrite; persistent PE reopens it (ACh freeze/unfreeze). | **MECH-207** (ACh-permissive PE destabilisation; Sinclair 2021). **MECH-398** (ACh plasticity-gain gate). **MECH-083**. **MECH-401** (consolidation gated write authority). **MECH-592** (target- and time-restricted release). **ARC-152 / ARC-153**. Campaign **W2b** (ACh-gated unfreeze), BLOCKED: probe N5 was CANNOT_DETERMINE, the surprise signal did not separate a shift from no shift, and even an oracle FIFO unfreeze re-learned only 0.25-0.39 (< 0.47). **GFLAG-0509** deferred the re-phasing of 398/207 to v3. | **Already owned.** Cross-ref only. The empirical state (N5) is recorded in MECH-597's notes as the reason MECH-597 asserts only the FROZEN (retention) half. |
| Sec 9-10: chunk when distinctions stop predicting, split when they start to; applies to every vocabulary (percepts, E1/E2 schemas, episodes, goals, social categories, concepts). Three meanings of "primitive" (innate / developmental / reopened). | **ARC-069 / ARC-070 / ARC-071** (dynamic regranularisation: compose on repeated grounding, decompose on prediction failure). **MECH-317 / MECH-321 / MECH-323 / MECH-324** (chunk accumulation, maintenance, dissolution). **MECH-529** (replay-driven rebucketing of E1 equivalence classes: split / merge / reweight on consequential divergence). **MECH-531** (a merge/split operator over entities). **MECH-126** (overmerge / oversplit failure modes). **INV-101** (spurious splitting vs forced merging relative to the environment). **MECH-513** (memory reindexing after a split). "Innate primitive" = MECH-461; "developmental primitive" = ARC-071; "reopened primitive" = ARC-070. | **Already owned**, vocabulary by vocabulary. A single "one chunk/split law across all vocabularies" umbrella would be thin over ARC-069 + MECH-529 + INV-101, so it is not registered. The "splitting is a maintenance requirement, not an initial one" prediction is folded into Q-112's ablation menu. |
| Sec 4 / 12 / 13 / 17: a two-axis taxonomy (necessity vs accelerator x general vs env-specific) + enabling architecture; "least environment-specific intervention first"; an env-specific prior is an ecological finding; innate = procedures for discovering a world, not facts about it | **SD-090** has five functional-role classes (constitutive / developmental-scaffold / robustness-reserve / historical-contingency / true-redundancy) plus redundant_under_current_tests vs functionally_unnecessary. It has NO environment-generality axis and NO necessity-vs-accelerator split for developmental priors. **GOV-ECOL-1**: seeds vs world families (the replication axis the general/specific split needs). **GOV-INSERT-1**: insertion of the desired OUTCOME counts against a derivation. That is the ethics-layer sibling of "an env-specific prior encodes the environment's solution". **GOV-MATCHAUX-1**: scaffold-removal admissibility for representation objectives. **INV-101**: crystallisation target is environment-conditional. **DEV-NEED register** (`developmental_needs_register.md`) is the existing candidate register, but it has no necessity/accelerator/generality columns. | **Adjacent but distinct -> registered narrowly as ARC-157.** |
| Sec 13 / 14 / 19 / 20: the candidate minimum, and discovery by reduction/ablation (each removal gives a specific predicted failure; restoration repairs without env content; transfer across environments) | **INV-073** and **INV-055** each assert ONE element's necessity (exploration epoch; infant stage). **ARC-074** asserts one epoch. **Q-108** asks what a minimal-working-intelligence EVENT is (recovery from being wrong), not what a minimal developmental PRIOR is. **MECH-557** is a 3+2 reduction hypothesis over cognitive-contract candidates (a different set). **SD-090** has the removal-justification vocabulary. **GOV-ECOL-1** has the world-family replication. | **Genuinely new as a QUESTION -> registered as Q-112 (open_question).** The thought is explicit that the minimum is provisional, so the open_question form keeps it discoverable without asserting a set. |
| Sec 11: the axioms (A1, A2, A3, A4, D1, D2) re-derived as developmental necessities; "REE should be permitted to show one is unnecessary"; D2 needs a developmental behavioural manifestation | **GOV-INSERT-1** gives the derivational layer an experimental route, but only the INSERTION direction. **`axiom_chain_adversarial_audit.md`** asks "designed vs necessary". It also argues D2 does not follow from D1, because survival and accuracy come apart. **INV-042 / ARC-043** (the axiom stack). **MECH-158** (developmental motivation collapse). | **Adjacent. Folded into Q-112 as leg (c)**, not registered separately. A developmental-ABLATION route to axiom necessity is distinct from GOV-INSERT-1's insertion route and complements it. Alternative for the orchestrator: split leg (c) into its own Q if /governance wants the derivational layer to own it directly. |
| Sec 15: measure development, not endpoint reward; demonstrate the causal path | `developmental_metrics.md`; campaign I1 instruments (disc_h, fidelity k, action entropy); **GOV-PATHVALID-1 / GOV-BEHADJ-1** (causal path, behavioural adjudication); **GOV-JURIS-1** (D1/D2/D3 domains). | **Already owned.** Not claim material. |
| Sec 16: the developmental sequence (valued self -> action basis -> variation -> contingency -> models -> PE -> targeted exploration -> chunks -> splitting -> hierarchy) | **ARC-059** (self -> object -> other). **INV-064** (E1 -> E2 -> E3 maturation). **ARC-122** (four-phase curriculum). **ARC-138** (regulation-first). **ARC-136** (play frontier migration). **ARC-019** (staged curriculum with gates). | **Already owned** as an ordering family. The thought itself says "nothing requires the entire sequence to be explicitly programmed". Not registered. |
| Sec 2: infant locomotor primitives, "small vocabulary used variably -> larger specialised vocabulary" (Hinnekens 2023) | **MECH-461** (Dominici 2011: neonatal primitives retained and augmented). **MECH-496** (dimensionality as an outcome of a developmental schedule). | **Already owned.** Hinnekens 2023 is not in the corpus (unverified). It is a natural additional anchor for MECH-461. |

## Key formulations (verbatim, load-bearing)

> How little inherited structure is enough for an organism to become learnable, and how much additional
> general structure makes development reliably tractable without smuggling in solutions to its
> environment?

> **The organism must first generate experience from which useful distinctions can be learned.**

> **the prior should preferably specify how to explore an action space, not what the actions mean.**

> **extreme deterioration in the valued self-state interrupts the current behavioural trajectory and
> temporarily changes action selection away from its continuation.**

> **knowledge that has become reliable should become resistant to incidental overwrite, but persistent
> prediction failure should permit its internal structure to become plastic again.**

> **chunk when distinctions cease to predict meaningful differences; split when previously ignored
> distinctions acquire predictive or evaluative importance.**

> **prefer the least environment-specific intervention capable of restoring development.**

> this environment could not be reliably developed into under the current general prior set without
> additional ecological information.

> Innate structure need not primarily consist of facts about the world. It can consist of **procedures
> for discovering a world**.

> **Before an organism can reason well, it may need machinery whose purpose is simply to make useful
> reasoning learnable.**

> But this is explicitly a **candidate minimum**, not the minimum.

## Affected existing claims

- **ARC-074** -- cross-referenced by Q-112 and MECH-597. Two things are OWED, and this pass applies neither:
  - **Evidence note owed.** GFLAG-0504's resolution (2026-09-25T12:01Z) deferred ARC-074's
    `evidence_quality_note` "to the W2a build". W2a landed (ree-v3 `2ea0e3c`, 2026-09-25T19:45Z), and
    ARC-074 still carries no note of the 09-25 probe. That probe found the coded Phase 0 is the native
    policy, near-monostrategy on 4/5 seeds (S FAIL 1/5, DR FAIL 0/5), and that a structured L2
    generator is a sufficient source. Route to /governance.
  - **Citation to verify.** ARC-074's description glosses **Garcia-Guzman 2026** as a "pre-reward
    Hebbian phase as prerequisite for structured curriculum". The corpus record
    (`targeted_review_developmental_exploration_hippocampal_retrieval/.../garciaguzman2026`, tagged
    ARC-065/INV-073) and the raw thought both describe it as spontaneous infant arm movements exploring
    arm dynamics. That gloss looks like a mis-description and needs a check.
- **MECH-461** -- its WWA says the primitive-basis half is "currently untested". The 09-25 probe is D1
  (action-coverage) evidence bearing on that half: a small, class-balanced, persistent-run basis gave E2
  action discrimination 5/5 over the on-policy baseline, where the native policy did not. It says
  nothing about competence (MECH-461's DV is foraging), so it cannot close the half. Flag for
  /thought-digestion or /governance. No edit here.
- **INV-073** -- distinguished from MECH-597 (opposite direction: INV-073 = early DEFICITS are permanent;
  MECH-597 = early GAINS are fragile without rehearsal). Both can hold, and MECH-597 does not weaken INV-073.
- **MECH-334 / MECH-496** -- distinguished from MECH-597 (plasticity reduction on the scoring/policy plane
  or on representational structure, vs rehearsal on the world-model plane).
- **MECH-207 / MECH-398 / MECH-083** -- the unfreeze half of the thought's sec 8. Cross-ref only
  (`related_claims` on MECH-597, not `depends_on`, to avoid a v3 -> v4 prerequisite edge). N5's
  CANNOT_DETERMINE is cited as the reason MECH-597 asserts retention only.
- **SD-090** -- extended in spirit by ARC-157 (new axes), NOT amended. Alternative: the orchestrator may
  prefer ARC-157 as an SD-090 amendment. That needs a user steer, per the skill.
- **GOV-INSERT-1 / GOV-ECOL-1 / GOV-MATCHAUX-1** -- ARC-157 and Q-112 depend on them. Not modified.
- **INV-095 / INV-030 / SD-012 / INV-069 / ARC-138** -- the valued-self-state leg of Q-112. Not modified.
- **Q-108** -- distinguished from Q-112 (a minimal-working-intelligence EVENT vs a minimal developmental
  PRIOR SET).

No existing claim's status, confidence or evidence record is touched by this draft.

## Candidate claims -- REGISTERED this pass (Q-112, ARC-157, MECH-597)

Registered ids (drafting id -> real): DP-1 -> **Q-112**, DP-2 -> **ARC-157**, DP-3 -> **MECH-597**. MECH-597's
V3-EXQ-1108 evidence item was refreshed at registration: the 1108 autopsy was confirmed later on 2026-09-26. Proposed architecture stub: `docs/architecture/minimal_developmental_prior.md` (new; see
the frontmatter below). All three entries have `polarity: asserts`, `status: candidate`, and
`registered_utc: '2026-09-26'`. `what_would_answer` is deliberately omitted from the claim blocks. The
drafts are in the digestion staging file (next section) for /thought-digestion to review.

### Q-112 (open_question) -- the minimal developmental prior set

```yaml
- id: Q-112
  title: "What is the minimal set of inherited, environment-general structures an REE organism needs in order to become learnable -- to generate experience from which action-consequence, self/world and value distinctions can be learned -- and which of the current candidates (a valued, vulnerable self-state; a small general basis for structured endogenous action; sensitivity to self-action contingency; persistent but revisable developmental memory) are necessities, which are accelerators, which can emerge from the others, and which are environment-specific scaffolds, as determined by reduction and ablation from a deliberately over-provisioned general set in which each removal must produce its own predicted developmental failure and each restoration must repair development without encoding the environment's solution?"
  claim_type: open_question
  subject: development.minimal_developmental_prior_set
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v4
  version_relevance: v4_v5
  registered_utc: '2026-09-26'
  source_thought: docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md
  location: docs/architecture/minimal_developmental_prior.md#q-112
  depends_on:
  - INV-073
  - INV-055
  - ARC-074
  - MECH-461
  - MECH-277
  - SD-031
  - ARC-138
  - INV-095
  - INV-030
  - SD-012
  - ARC-059
  - INV-064
  - Q-108
  - SD-090
  - GOV-ECOL-1
  - GOV-INSERT-1
  - ARC-157
  - MECH-597
  source:
  - docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md
  - evidence/planning/thought_intake_2026-09-25_minimal_developmental_prior_problem.md
  - evidence/planning/babbling_e2_action_coverage_probe_20260925.md
  notes: >-
    Registered from secs 13, 14, 19 and 20 of the source thought, which is explicit: "this is explicitly
    a candidate minimum, not the minimum" and "the minimum should be discovered by reduction and
    ablation". An open_question keeps the candidate set discoverable without asserting it. WHAT IT ASKS,
    THREE LEGS: (a) NECESSITY -- which candidates, when removed from a set that develops, produce a
    specific predicted developmental failure (the thought's ablation menu: remove structured endogenous
    action / contingency bias / viability grounding / developmental retention / explicit orienting /
    chunking / splitting), and whether restoring the element repairs development without environment
    content; (b) GENERALITY -- whether the same small set bootstraps development across at least two
    predeclared world families (GOV-ECOL-1), and where an environment-specific scaffold becomes
    unavoidable (classified under ARC-157); (c) AXIOM MAPPING -- sec 11 observes that asking what an
    ignorant organism needs regenerates structures resembling A1 (a locus for contingency attribution),
    A2 (valued self-state), A4 (causal power + vulnerability), D1 (primitive preservation + learned
    anticipation) and D2 (act to obtain informative consequences). Leg (c) asks whether a developmental
    ablation of the implementation of A2/D1 (remove viability grounding) produces the predicted failure,
    or whether preservation/goal behaviour arises from another source. The thought says the convergence
    is "not proof" and "REE should be permitted to show one is unnecessary". EXTENDS: INV-073 (one
    element's necessity -- the exploration epoch), INV-055 (the infant stage), ARC-074 (Phase 0),
    MECH-461 (innate primitive basis + engagement drive), MECH-277 / SD-031 (contingency), ARC-138 /
    INV-095 / SD-012 (valued self-state). DISTINCT FROM Q-108: that asks what one minimal-working-
    intelligence EVENT (adaptive recovery from being wrong) must contain; this asks what inherited
    structure development needs BEFORE any competence exists. DISTINCT FROM MECH-557: a 3 + 2 reduction
    over the cognitive-contract ledger, a different candidate set. DISTINCT FROM GOV-INSERT-1: that
    records insertion-dependence as evidence AGAINST a derivation; leg (c) is the complementary
    ABLATION route (remove the axiom's developmental implementation and see whether development needs
    it). If /governance prefers, leg (c) can be split into its own Q owned by the derivational layer.
    ENABLING ARCHITECTURE (plasticity, memory, temporal ordering, self/world state, an action interface,
    a route from learned models to action selection) is excluded from the minimality question by
    construction (ARC-157). CURRENT V3 STATE, re-measured 2026-09-26: the structured-action leg is
    expressible (ree_core/developmental/structured_babbling.py StructuredBabbler, ree-v3 main 2ea0e3c,
    default-OFF) and already has D1 evidence (babbling_e2_action_coverage_probe_20260925.md: the native
    Phase-0 policy S FAIL 1/5, the L2 structured source sufficient 5/5 pre-post). The retention leg is
    MECH-597. There is NO separable contingency-bias lever: E2's world head is action-conditioned by
    construction (e2_fast.py world_action_encoder), so ablating "contingency bias" today would remove
    enabling architecture. The viability leg has SD-012 drive + the harm streams, but no clean
    "remove viability grounding while keeping exploration and modelling" arm. Literature: Garcia-Guzman
    2026 (corpus-verified, tagged INV-073/ARC-065), Keramati & Gutkin 2014 (corpus, SD-012),
    Keren-Portnoy 2021 (corpus, INV-073). NOT yet in the corpus / NOT verified: Hinnekens et al. 2023
    eLife, Kanazawa 2026 (PMID 42252157 as given), Sen & Gredeback 2021, Diedrichsen & Kornysheva 2015,
    Giszter 2015, Exton-McGuinness et al. 2015, Marjaninejad et al. 2019 (NMI). DO NOT build in V3 on the
    strength of this entry; DO NOT queue an experiment from it. Registration is not build
    authorisation.
```

### ARC-157 (architectural_commitment) -- two-axis developmental-prior classification, least-env-specific first

```yaml
- id: ARC-157
  title: "Every candidate developmental prior in REE is classified on two INDEPENDENT axes -- candidate-necessary vs developmental accelerator (improves speed, stability or robustness but is dispensable or derivable in principle), and environment-general vs environment-specific -- with enabling architecture (plasticity, memory, temporal representation, an action interface, self/world state, a route from learned models to action selection) held out as a separate class that is not a prior; and when development fails, interventions are admitted in order of increasing environment-specificity (structured endogenous exploration, then general contingency / information-seeking mechanisms, then memory / plasticity mechanisms, and only then environment-specific priors), so that a required environment-specific prior is recorded as an ecological finding about that environment ('this world could not be reliably developed into under the current general set without additional ecological information') rather than as an innate requirement. Inherited structure is preferentially PROCEDURAL (how to discover a world: vary action enough to see its consequences, credit changes that follow one's own action, preserve regularities, reopen them when they stop predicting) rather than ONTOLOGICAL (what the world contains)."
  claim_type: architectural_commitment
  subject: development.developmental_prior_classification
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v4
  version_relevance: v4_v5
  registered_utc: '2026-09-26'
  source_thought: docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md
  location: docs/architecture/minimal_developmental_prior.md#arc-157
  depends_on:
  - SD-090
  - GOV-ECOL-1
  - GOV-INSERT-1
  - GOV-MATCHAUX-1
  - INV-101
  - MECH-461
  - ARC-046
  - SD-032c
  - MECH-104
  - INV-030
  source:
  - docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md
  - evidence/planning/thought_intake_2026-09-25_minimal_developmental_prior_problem.md
  notes: >-
    Registered from secs 4, 6, 12, 13 and 17 of the source thought. WHAT IS NEW: SD-090 classifies a
    mechanism's functional ROLE in viability (constitutive / developmental-scaffold / robustness-reserve /
    historical-contingency / true-redundancy) and supplies a removal-justification vocabulary. It has no
    ENVIRONMENT-GENERALITY axis and no NECESSITY-vs-ACCELERATOR split for developmental priors, and it
    says nothing about the ORDER in which to admit rescue interventions. SD-090's developmental-scaffold
    class (needed during development, removable later) is NOT the same as this claim's accelerator class
    (improves development but is dispensable in principle). A mechanism can be a scaffold AND necessary,
    or an accelerator AND never removable. WORKED EXAMPLE OF THE GENERALITY AXIS (sec 6): a primitive
    survival interrupt is admissible as GENERAL only when it is keyed to deterioration of the valued
    self-state ("extreme deterioration ... interrupts the current behavioural trajectory"). The same
    function keyed to an environment feature ("hazard tile -> move LEFT") is an environment-specific
    scaffold. The mechanism is already owned (SD-032c urgency interrupt, MECH-104 harm-spike
    de-commitment, ARC-046 infant hazard protection); this claim adds only the content-generality
    constraint and the preservation-vs-learned-avoidance distinction. DISTINCT FROM GOV-INSERT-1: that
    rule is the derivational-layer sibling (inserting the desired ethical OUTCOME counts against a
    derivation). This is the developmental-layer analogue: inserting the environment's SOLUTION counts
    as ecological information, not as an innate requirement. Both are "what had to be inserted is a
    finding". DISTINCT FROM GOV-MATCHAUX-1: that is admissibility for representation-objective results
    (matched arbitrary auxiliary + removal); this is admission ORDER and classification for developmental
    priors. DISTINCT FROM GOV-ECOL-1: that separates seed replication from world-family replication.
    This claim NEEDS it, because the general/specific axis is only measurable by world-family
    replication. DISTINCT FROM INV-101: that makes the crystallisation TARGET environment-conditional;
    this makes the PRIOR's generality a classified, testable property. The existing DEV-NEED register
    (docs/architecture/developmental_needs_register.md) is the natural host for the two new columns
    (necessity/accelerator; general/specific), plus the thought's per-entry fields (predicted
    contribution, mechanisms it might emerge from, earliest operating stage, cost, what would show it
    unnecessary, what would show it merely accelerating, transfer expectation, ablation consequence,
    current evidence). That is a doc task, not done here. ALTERNATIVE FOR THE ORCHESTRATOR: fold this
    into SD-090 as an amendment (needs a user steer), or split the admission-order discipline out as a
    governance_rule. Registering it as one architectural_commitment keeps the classification and the
    discipline together, as the thought states them. DO NOT build in V3; DO NOT queue an experiment.
    The environment-specific-scaffold class is deliberately EMPTY at registration, as the thought
    requires: "left deliberately empty until an environment demonstrates their necessity".
```

### MECH-597 (mechanism_hypothesis, V3-testable -- flag for /governance routing) -- retained developmental replay

```yaml
- id: MECH-597
  title: "Developmental action-consequence knowledge acquired by the E2 world head from a structured, action-diverse developmental source is NOT durable under subsequent on-policy training that is narrower than the developmental distribution: a one-off developmental exposure is progressively overwritten, and durability requires that a retained, overwrite-protected fraction of the developmental experience continue to enter the head's training stream (developmental rehearsal) -- a replay-based protection on the world-model plane, distinct from plasticity reduction (critical-period closure) on the scoring/policy plane."
  claim_type: mechanism_hypothesis
  subject: development.retained_developmental_replay_durability
  polarity: asserts
  status: candidate
  epistemic_category: standard
  implementation_phase: v3
  version_relevance: v3_v4
  registered_utc: '2026-09-26'
  source_thought: docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md
  location: docs/architecture/minimal_developmental_prior.md#mech-597
  depends_on:
  - ARC-074
  - INV-073
  - MECH-334
  - MECH-165
  - MECH-277
  - MECH-588
  - SD-031
  related_claims:
  - MECH-207
  - MECH-398
  - MECH-083
  - MECH-496
  - MECH-401
  source:
  - docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md
  - evidence/planning/thought_intake_2026-09-25_minimal_developmental_prior_problem.md
  - evidence/planning/babbling_e2_action_coverage_probe_20260925.md
  - evidence/planning/coupled_loop_repair_campaign_plan.md
  notes: >-
    Registered from secs 1, 7 and 18 of the source thought ("a one-off developmental exposure was
    insufficiently durable ... retaining a minority of structured developmental replay preserved the
    advantage"). Scope is narrowed to what has been measured.
    EVIDENCE ON FILE (D1 only; none of it tagged to this id, and none is claimed here as a scoring
    entry): (1) babbling_e2_action_coverage_probe_20260925.md (FINAL). A SECONDARY, pre-registered,
    descriptive readout, not a verdict: over 9,000 on-policy updates (3x the developmental update
    exposure), one-off L2 kept >= 50% of its gain over the on-policy baseline on 2/5 seeds, while L2R
    (25% retained replay) kept it on 5/5 (ratios 1.31-1.53), with fidelity k = 10 on 5/5. It was
    stratum-independent (1 benign + 4 hazard-trapped seeds). Three of the L2R seeds came from a trailing
    block run after a resource-only reschedule; the L2_pre heads were reproduced exactly. (2) Campaign
    W3 member gate (coupled_loop_repair_campaign_plan.md row W3; record
    w3_e2_world_member_build_20260925.md). This is gated and D1: retention (b) was 5/5 (0.96-1.71) with
    a FROZEN encoder, and the label-shuffled replay twin failed (a) 0/5. (3) V3-EXQ-1108 (N2 at full
    post dose, ran 2026-09-26T10:02Z, outcome FAIL, PENDING REVIEW, not adjudicated here):
    - the frozen-encoder arm kept the bar ((a) 4/5, (b) 5/5);
    - with the encoder trained through the read path, re-encoded retained replay did NOT keep the bar
      ((a) 3/5, (e) 1/5), and stored-latent replay failed outright.
    So this claim is asserted for the FROZEN-READ-PATH regime. Whether rehearsal keeps developmental
    knowledge while the encoder itself moves is OPEN and belongs to the N2/1108 autopsy.
    WHAT IS NEW: ARC-074 asserts a one-off Phase-0 epoch. INV-073 asserts that early DEFICITS are
    permanent, which is the opposite direction to this claim (early GAINS are fragile without
    rehearsal). Both can hold, and neither weakens the other. MECH-334 protects crystallised diversity
    by PLASTICITY REDUCTION (EWC anchor) on the SCORING/POLICY plane. MECH-496 moves that schedule onto
    representational structure. MECH-165 requires diverse SLEEP replay for multi-strategy viability.
    None of them states the non-durability of developmental WORLD-MODEL knowledge, or REHEARSAL of
    developmental experience as its remedy. DELIBERATELY EXCLUDED, the unfreeze half of the thought's
    sec 8 (reopen retained knowledge under persistent PE, ACh-gated). That is MECH-207 / MECH-398 (v4;
    related_claims, not depends_on, to avoid a v3 -> v4 prerequisite edge) and campaign row W2b, which
    is BLOCKED: probe N5 (n5_ach_gated_unfreeze_probe_20260926.md) was CANNOT_DETERMINE; the gate did
    not separate a shift from no shift; and even an oracle FIFO unfreeze re-learned only 0.25-0.39
    against a 0.47 bar in 1200 steps. The thought's "freeze" is this claim; its "unfreeze" is not
    asserted here. SUBSTRATE: the generator is on ree-v3 main (StructuredBabbler, 2ea0e3c, default-OFF);
    the E2WorldMember with its retained buffer is on integration/coupled-loop-repair (042895a ->
    4070b0efa4), not main. V3-testable today through the committed probe harness. FLAG FOR /governance
    ROUTING: implementation_phase v3 and epistemic_category standard are proposed because the claim is
    cleanly testable on existing V3 substrate and already has D1 evidence. /governance decides the
    routing, and whether any of the three evidence items should be tagged to this id (claim_ids accuracy
    rule: none are tagged by this registration). NOT a V3 build authorisation. The campaign already
    owns the build.
```

### Proposed architecture stub (new file; parent category survey: "Development & Curriculum" max nav_order = 17)

```markdown
---
title: "The Minimal Developmental Prior Problem (Q-112, ARC-157, MECH-597)"
parent: "Development & Curriculum"
grandparent: Architecture
nav_order: 18
status: candidate
status_asof: 2026-09-26
status_claim: Q-112
---
```

Sections to write in the stub:

1. The problem and the observation that motivates it: the 09-25 probe chain (Phase 0 was the native
   policy -> near-monostrategy -> flat E2 -> flat E3).
2. ARC-157's two-axis table plus the enabling-architecture class; the admission-order discipline; the
   survival-interrupt worked example; procedural vs ontological inheritance.
3. Q-112's candidate register. Seed it with the thought's sec 13 entries and a pointer to the owning
   claim for each:
   - valued self-state -> INV-095 / SD-012 / ARC-138;
   - structured endogenous action -> INV-073 / ARC-074 / MECH-461 / StructuredBabbler;
   - contingency -> MECH-277 / SD-031;
   - retention -> MECH-597;
   - freeze/unfreeze -> MECH-207 / 398;
   - chunk/split -> ARC-069..071 / MECH-529;
   - LP curiosity -> MECH-314c;
   - orienting -> MECH-482 / 483 / 590;
   - survival interrupt -> SD-032c / MECH-104 / ARC-046.

   Then the ablation menu (sec 14) and the developmental DVs (sec 15).
4. MECH-597, with the evidence table and the frozen-vs-trained-encoder scope limit.
5. The three meanings of "primitive" (innate = MECH-461; developmental = ARC-071; reopened = ARC-070),
   as vocabulary only.
6. Out of scope, and why: the developmental sequence (owned by the ARC-059 / INV-064 / ARC-122 /
   ARC-138 family); the unfreeze rule (W2b / N5); the axiom convergence as proof (explicitly not).

## Next steps

1. **Literature pull before hardening** (`/lit-pull`, targeted review for Q-112 / ARC-157). These are NOT
   in the corpus and NOT verified:
   - Hinnekens et al. 2023 eLife (variability from motor primitives): also a natural MECH-461 anchor;
   - Kanazawa 2026 (PMID 42252157 as given): sec 3's "development structures sensorimotor information";
   - Sen & Gredeback 2021 (embodied mobile paradigm);
   - Diedrichsen & Kornysheva 2015 and Giszter 2015 (chunking; primitives);
   - Exton-McGuinness, Lee & Reichelt 2015 (PE and reconsolidation): a sibling anchor to Sinclair 2021
     for MECH-207;
   - Marjaninejad et al. 2019 NMI (general-to-particular motor babbling).

   Already in the corpus: Garcia-Guzman 2026, Keramati & Gutkin 2014, Keren-Portnoy 2021, Oudeyer &
   Kaplan 2007, Stahl & Feigenson 2015 (MECH-327 notes), Sinclair 2021.
2. **/governance items surfaced (flag, do not apply here):**
   - ARC-074's owed `evidence_quality_note`. GFLAG-0504 deferred it "to the W2a build"; W2a landed
     2026-09-25T19:45Z and the note is still absent.
   - ARC-074's Garcia-Guzman 2026 gloss (possible mis-description).
   - MECH-461's "primitive-basis half untested": the 09-25 probe is partial (D1, action-coverage)
     evidence.
   - MECH-597's v3 routing.
   - Whether ARC-157 should be an SD-090 amendment instead.
   - D1 and D2 have no registered INV ("pending INV" in `five_axioms_foundations.md`). This is a
     registry gap that Q-112 leg (c) leans on.
3. **Stale note found:** `coupled_loop_repair_campaign_plan.md` row N2 (last updated 2026-09-26T02:07Z)
   still says "queued V3-EXQ-1108 ... await its verdict". 1108 RAN at 10:02Z today (FAIL, in
   `pending_review.md` as non_contributory), so the row is stale. Owned by the campaign orchestrator and
   /failure-autopsy; do not chip (autopsy work is inline).
4. **Version routing:** Q-112 and ARC-157 are parked at v4 / `substrate_conditional`. MECH-597 is proposed at v3
   / `standard` and flagged for /governance, which decides.
5. **Do not queue anything from the thought's sec 14 ablation list.** Most legs lack a lever (no
   separable contingency-bias lever; no clean viability-grounding ablation; chunk/split operators are
   largely unbuilt: MECH-531 says no merge/split exists in `object_file_buffer.py`). The one live leg
   (retention) is already owned by the campaign (W3, N2 / V3-EXQ-1108).
6. **Registry discrepancy to check (low confidence):** auto-memory
   `project_ontogenetic_ordering_approach_before_avoidance.md` says the approach-before-avoidance
   ordering was "registered as a candidate MECH claim (via /claim-synthesis, 2026-07-10)". No
   claims.yaml entry was found by title or subject search. INV-094's notes refer to it only as a
   "hypothesis under active MECH-457 investigation". Either the memory overstates it or the entry lives
   under a non-obvious title. Relevant to Q-112 as an ordering-necessity candidate (a general or an
   environment-specific prior?).
7. Mark the raw thought processed at the top of the file, and remove the old `Status: raw /
   unprocessed` line:
   `Status: processed` / `Intake: evidence/planning/thought_intake_2026-09-25_minimal_developmental_prior_problem.md` /
   `Claims registered: Q-112, ARC-157, MECH-597` (done at registration).

## Digestion drafts

Draft `what_would_answer` text and recommended dispositions for Q-112, ARC-157 and MECH-597 are staged in
`evidence/planning/thought_digestion_staged_2026-09-26_thought_intake_batch.md`. They must land in the
SAME commit as this intake. They are proposals for /thought-digestion and are not applied to the claim
blocks above.
