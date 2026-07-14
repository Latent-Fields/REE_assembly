---
closure_plan:
  id: ree_ai_design_critique
  generation: meta
  title: "REE AI-Design Critique (cross-cutting workstream roadmap)"
  registered: 2026-07-09
  last_updated: 2026-07-10
  owner: strategic
  summary: >
    A durable, resume-across-sessions roadmap for the "REE as an AI design"
    critique -- where REE is ahead, reinvents the wheel, is flawed, or needs
    work -- as ~14 workstreams (WS) in leverage/dependency tiers. generation:
    meta -> a strategic design-critique roadmap, NOT a V3 substrate-closure map;
    segmented out of the V3 closure % (its threads are lit-pulls, bridge docs,
    governance rules, and diagnostics that CONSUME V3 results rather than owning
    substrate claims). Node status mirrors the plan's own resume-primitive Status
    table. PROMOTES/DEMOTES NOTHING directly.
  scope_claims: []
  sibling_plans: [conversion_ceiling_campaign, commitment_closure]
  nodes:
    - id: WS-1
      tier: 0
      title: "Capability floor before structure -- isolate can-it-act from does-structure-help"
      status: in_progress
      severity: load-bearing
      last_updated: 2026-07-10
      note: >
        CONSUMES V3-EXQ-724/732/732a (does not re-queue). 4th diagnostic
        (719a->724->732->732a) bottoming out on the same competence floor; 732a
        autopsy found the learner-adequacy gate observability-confounded
        (global-oracle reference vs 5x5 local view). Re-operationalized: needs a
        local-view-achievable ceiling in WS-3 capability_eval.py before a fair
        probe. Currently blocked-on-upstream (all-ON forages ~0). REFUSED
        V3-EXQ-732b. Diagnostic; claim_ids=[].
    - id: WS-2
      tier: 1
      title: "Ceiling-claim demotion rule (new GOV-* pre-registered falsification/demotion rule)"
      status: open
      severity: high
      last_updated: 2026-07-09
      note: "NOT STARTED. Pre-registered demotion rule for substrate_ceiling / pending_retest_after_substrate."
    - id: WS-3
      tier: 1
      title: "Capability-eval yardstick (minimal benchmark independent of any REE claim)"
      status: done
      severity: high
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> reusable block ree-v3/experiments/_lib/capability_eval.py. Separates claim-wrong from substrate-cant-act."
    - id: WS-4
      tier: 2
      title: "Formal-ancestor mapping (top ~30 load-bearing MECH/ARC to nearest formal ancestor)"
      status: done
      severity: medium
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> docs/architecture/formal_ancestor_mapping.md (per-row lit-pull)."
    - id: WS-5
      tier: 2
      title: "Active-inference bridge (precision / epistemic value / exploration math REE can inherit)"
      status: done
      severity: medium
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> docs/architecture/active_inference_bridge.md (targeted lit)."
    - id: WS-6
      tier: 2
      title: "Bitter-Lesson rebuttal (why scale + search won't eat this structure)"
      status: done
      severity: medium
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> docs/architecture/bitter_lesson_position.md (steelmans Sutton)."
    - id: WS-7
      tier: 2
      title: "Corrigibility positioning (commit-boundary vs the formal corrigibility literature)"
      status: done
      severity: medium
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> docs/architecture/corrigibility_positioning.md (maps MECH-090)."
    - id: WS-8
      tier: 2
      title: "Cognitive-architecture graveyard (Soar / ACT-R / LeCun AMI ceilings -> anti-patterns)"
      status: done
      severity: medium
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> docs/architecture/cognitive_architecture_graveyard.md (9 anti-patterns)."
    - id: WS-9
      tier: 2
      title: "Intrinsic-motivation lit (Oudeyer, Schmidhuber curiosity, Baldassarre) feeding WS-1"
      status: done
      severity: medium
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> evidence/planning/intrinsic_motivation_competence_mechanisms.md."
    - id: WS-10
      tier: 3
      title: "Minimal 2-agent world (put any load on the ethics thesis, currently V5-only)"
      status: open
      severity: medium
      last_updated: 2026-07-09
      note: "NOT STARTED. Needs substrate/experiments (Tier 3)."
    - id: WS-11
      tier: 3
      title: "Early-gating vs late-judging demo (REE early commit-gating beats a Constitutional-AI-style late judge)"
      status: open
      severity: medium
      last_updated: 2026-07-09
      note: "NOT STARTED. Needs substrate/experiments (Tier 3)."
    - id: WS-12
      tier: 4
      title: "Similarity / dehumanization failure mode (sufficiently-like-me gates care -> out-group exclusion)"
      status: done
      severity: high
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> EXT-009 in docs/claims/claims.yaml (reflexive failure mode as a first-class claim)."
    - id: WS-13
      tier: 4
      title: "Moral-philosophy red-team (adversarial audit of the axiom chain)"
      status: done
      severity: high
      last_updated: 2026-07-09
      note: "DONE 2026-07-09 -> docs/architecture/axiom_chain_adversarial_audit.md (cites EXT claims)."
    - id: WS-14
      tier: 1
      title: "Bottleneck fan-out escalation rule (new GOV-* claim: escalate a discrimination brake from sequential retry to fan-out)"
      status: done
      severity: high
      last_updated: 2026-07-10
      note: "DONE 2026-07-10 -> GOV-FANOUT-1 in claims.yaml (constructive complement to the re-derive brake)."
---
# REE AI-Design Critique — Roadmap Plan

**Created:** 2026-07-09
**Owner thread:** strategic / cross-cutting (not a single substrate build)
**Purpose:** A durable, resume-across-sessions roadmap for pursuing a broad "REE as an AI design" critique — where REE is ahead, where it reinvents the wheel, where it is flawed, and where it needs work — plus the external lenses that should keep guiding it. Each thread below is a workstream (WS) with a concrete first deliverable so it can be picked up cold.

This doc is the resume primitive. Update the **Status table** whenever a WS advances. Keep prose changes in the per-WS sections.

---

## How to read this

The critique produced ~13 actionable threads. They are grouped into tiers by leverage and dependency:

- **Tier 0 — Unblock.** The one thing everything else waits behind.
- **Tier 1 — Epistemic hygiene.** Cheap, internal, no substrate needed. Do early.
- **Tier 2 — Theory grounding.** Literature + writing. Parallelizable, mostly lit-pulls + bridge docs.
- **Tier 3 — Thesis exercise.** Needs substrate/experiments. Puts real load on the central claim.
- **Tier 4 — Adversarial ethics.** Red-team the moral foundation.

**Do not duplicate in-flight work.** The competence-floor idea (WS-1) overlaps the already-queued **V3-EXQ-724 competence-localization diagnostic** (routed by failure_autopsy_V3-EXQ-719a). WS-1 should *consume* 724's result, not re-queue it. Check `ree-v3/experiment_queue.json` and `conversion_ceiling_campaign_plan.md` before spawning any experiment here.

---

## Status table (resume primitive)

| WS | Tier | Title | First deliverable | Status |
|----|------|-------|-------------------|--------|
| WS-1 | 0 | Capability floor before structure | Read V3-EXQ-724 result; competence-floor experiment isolating "can it act" from "does structure help" | **IN PROGRESS** — 724 landed `competence_deficit_diffuse`; autopsy `failure_autopsy_V3-EXQ-724_2026-07-09` localized it to the un-varied invariant (bias-head-only policy learning over prediction-only reps; REE is prediction-rich/action-poor). H1/H2 discriminator **QUEUED 2026-07-09 as V3-EXQ-732** (`policy_learning_discriminator`, diagnostic, claim_ids=[], brake-exempt): B0 = 724 A0 incompetence anchor; B1 (H1) = REE prediction-trained representation + full trainable A2C action head; B2 (H2) = vanilla A2C on the identical raw-obs vector, no REE machinery. B1/B2 share one online A2C learner + budget so the contrast isolates the representation front-end (matched-learner variant of the autopsy sketch — no algorithm confound); env/oracle/B0 reused verbatim from 724; DV = P2 mean_resources/ep vs 1.0 floor. `validate_experiments --strict` OK; dry-run PASS; LANDED ree-v3 `main` 1ab745d; coordinator `/queue/add` applied:true, `/queue/active` PRESENT. **Grid → build direction:** B2∧B1 clear → H1 (build action/policy substrate); B2 clears ∧ B1 fails → deeper H1 (narrow to representation/drives); B2 fails → H2 (target observation encoding); B1 clears ∧ B2 fails → flag leakage. Numbers land when the fleet executes 732 → route to `/failure-autopsy` for adjudication before any build. **TERMINAL (2026-07-10):** 732 ran under-powered (A2C) → its autopsy REJECTED the H2 self-route → **V3-EXQ-732a** power-fixed it (PPO, ~30× updates on both arms, entropy+count-novelty, forage-bonus+reward-std scaling, a NEW learner-adequacy gate). 732a self-routed `substrate_not_ready_requeue`; `failure_autopsy_V3-EXQ-732a_2026-07-10` (confirmed) finds the adequacy gate **observability-confounded** — its reference is the privileged-global oracle (`_oracle_action`/`OraclePolicy` reads all resource coords + teleport-beelines; sanity-oracle 57.2 res/ep) while the learner sees a 5×5 LOCAL view (L0 vanilla PPO = 0.7 res/ep = 1.2% of oracle; the `0.5×oracle=28.6` threshold is 28× the discriminator's own 1.0 floor, structurally unreachable by any local-view policy), so H1 vs H2 stays **UNRESOLVED**. This is the **4th diagnostic (719a→724→732→732a) bottoming out on the same floor** — pre-registered by 732 as terminal (power is not the lever: L0 stayed fragile at 30× budget). **REFUSED V3-EXQ-732b** same-question power bump. **Re-operationalized:** the adequacy reference must be a **local-view-achievable ceiling** (add a 5×5-window `resource_field_view` greedy anchor to the WS-3 `capability_eval.py` yardstick; demote the global oracle to floor-achievability control only) — see the WS-1 section. A fair, different-question probe is authored via `/queue-experiment` (new EXQ number) only after this reference lands AND a substrate clears the competence floor (currently blocked-on-upstream: all-ON forages ~0). PROMOTES/DEMOTES NOTHING (diagnostic, claim_ids=[]). |
| WS-2 | 1 | Ceiling-claim demotion rule | New GOV-* claim: pre-registered falsification/demotion rule for `substrate_ceiling` / `pending_retest_after_substrate` | NOT STARTED |
| WS-3 | 1 | Capability-eval yardstick | Minimal capability benchmark suite (independent of any REE claim) to separate "claim wrong" from "substrate coarse" | **DONE** (2026-07-09) → reusable block `ree-v3/experiments/_lib/capability_eval.py` built (4 metrics + oracle/random anchors, reuses V3-EXQ-724 instrumentation); calibration V3-EXQ-727 + TRAINED all-ON point V3-EXQ-728 (P0=200+P1=90, 724 A0 recipe; reports all four metrics on the 727 scale) both authored/queued (dry-run PASS). Yardstick is now the standing denominator wired into trained all-ON runs — "reported alongside every all-ON run" clause closed. Numbers land when the fleet executes 727/728 |
| WS-4 | 2 | Formal-ancestor mapping | Table mapping top ~30 load-bearing MECH/ARC to their nearest formal ancestor + that ancestor's measurement math | **DONE** (2026-07-09) → `docs/architecture/formal_ancestor_mapping.md`; per-row `/lit-pull` confirmation still owed |
| WS-5 | 2 | Active-inference bridge | Lit-pull + bridge doc: precision / epistemic value / exploration math REE can inherit; document exact departures | **DONE** (2026-07-09) → `docs/architecture/active_inference_bridge.md`; lit `targeted_review_active_inference_bridge/` (Parr/Pezzulo/Friston 2022 + Da Costa 2020); departures stated as *commensurability-not-cardinality* (ARC-021/MECH-069) + *multi-axis precision* (ARC-016); formal_ancestor_mapping rows cross-linked |
| WS-6 | 2 | Bitter-Lesson rebuttal | Written, cited answer to "why won't scale + search eat this structure?" | **DONE** (2026-07-09) → `docs/architecture/bitter_lesson_position.md`; steelmans Sutton, engages Chollet/ARC + o3-on-ARC hinge, lands on a falsifiable (i) scale-invariant-priors vs (ii) scaffolding partition with per-item demotion falsifiers; scaled-baseline experiments (i.2/WS-11, i.4 forced-shared-loss) still owed |
| WS-7 | 2 | Corrigibility positioning | Position the commit-boundary against the formal corrigibility literature (MIRI et al.) | **DONE** (2026-07-09) → `docs/architecture/corrigibility_positioning.md`; maps MECH-090/091/094/061 onto the Soares 2015 desiderata + Off-Switch Game (Hadfield-Menell 2017) + Thornley 2024 shutdown theorems; key findings: commit boundary gives a fresh pre-commit intervention window but *relocates* (not removes) the resistance incentive to post-commit, MECH-091 urgency interrupt is corrigible only insofar as its **internal** salience trigger is (inherits the manipulation incentive), REE's incommensurable-channels design is an unexpected partial match to Thornley's incomplete-preferences escape; cross-links SENT-12/14 refusal-channel tension; per-claim `/lit-pull` confirmation still owed |
| WS-8 | 2 | Cognitive-architecture graveyard | Study of how Soar / ACT-R / LeCun AMI hit their ceilings; extract anti-patterns REE must avoid | **DONE** (2026-07-09) → `docs/architecture/cognitive_architecture_graveyard.md`; 9 anti-patterns mapped to REE exposures + governance-mass:cognitive-mass ratio; per-source `/lit-pull` confirmation still owed |
| WS-9 | 2 | Intrinsic-motivation lit | Lit-pull (Oudeyer, Schmidhuber curiosity, Baldassarre) feeding WS-1 competence + goal/wanting pipeline | **DONE** (2026-07-09) → `evidence/planning/intrinsic_motivation_competence_mechanisms.md`; 4 lit entries added to `targeted_review_intrinsic_motivation_exploration/` (Oudeyer&Kaplan 2007 typology→MECH-314c, Schmidhuber 2010 compression-progress→MECH-314c mixed, Mirolli&Baldassarre 2013 competence-based-IM→UNREGISTERED, Bellemare 2016 pseudocounts→MECH-314a). **Headline: REE's IM stack is entirely *knowledge-based*; WS-1's competence floor is the predicted symptom of a missing *competence-based* IM drive. Top-ranked mechanism (goal-achievement-progress wanting, goal pipeline/drive plane) REGISTERED 2026-07-09 as candidate **MECH-455** (competence-based IM; v3_pending; PROMOTES NOTHING). #2 per-candidate MECH-314c learning-progress, #3 latent pseudocount MECH-314a, both blocked by the EMA→E3-selection routing (EXQ-141b/590a).** |
| WS-10 | 3 | Minimal 2-agent world | Trivial 2-agent environment that puts *any* load on the ethics thesis (currently V5-only) | NOT STARTED |
| WS-11 | 3 | Early-gating vs late-judging demo | One concrete task where REE's early commit-gating demonstrably beats a Constitutional-AI/RLHF-style late judge | NOT STARTED |
| WS-12 | 4 | Similarity / dehumanization failure mode | First-class claim: "sufficiently-like-me" gates care → structural out-group exclusion; make it explicit + testable | **DONE** (2026-07-09) → `EXT-009` in `docs/claims/claims.yaml` (reflexive failure mode + red_team_question + 4 candidate_mitigations; cross-links Axiom 5/7, INV-001, MECH-164, INV-070/071/072, ethics-perimeter plan) |
| WS-13 | 4 | Moral-philosophy red-team | Adversarial audit of the axiom chain (does love *really* expand transitively under uncertainty?) | **DONE** (2026-07-09) → `docs/architecture/axiom_chain_adversarial_audit.md`; cites EXT-009; ready for external-ethicist handoff |
| WS-14 | 1 | Bottleneck fan-out escalation rule | New GOV-* claim: when a brake fires on a *discrimination*, escalate from sequential retry to a diverse **parallel portfolio** (declared nulls + coverage/aliasing design-audit) | **DONE** (2026-07-10) → `GOV-FANOUT-1` in `claims.yaml` (constructive complement to GOV-CEIL-1/GOV-DIAG-1/re-derive-brake; reuses their detection, adds the response). Wired: `/failure-autopsy` (`fanout_recommendation`), `/queue-experiment` Step 2.5b, `/governance` Step 6a-v-quater, graveyard antibody. Worked example: the 737/738/739 portfolio (P-A representation / P-B measurement / P-C observation axes) that replaced the 719a→724→732→732a sequential chain; P-B ran first and refuted H2 (floor reachable from the 5×5 local view) |

---

## Tier 0 — Unblock

### WS-1 — Capability floor before structure
**Why:** The conversion-ceiling campaign's own terminal finding is that the fully-integrated all-ON agent is not behaviourally *competent* enough to produce measurable committed behaviour (forages 0.065 / 0.0 / 0.455 resources/ep, below the 1.0 floor on 0/3 seeds). You cannot demonstrate that commitment gating matters on an agent that cannot forage. This is the Bitter Lesson biting: structure was specified faster than capability was earned. **Highest-leverage item on the board — most other WS wait behind it.**

**First deliverable:**
1. Read the V3-EXQ-724 competence-localization result the moment it lands (do not re-queue; it is already routed by 719a).
2. If 724 confirms a competence floor, design (via `/queue-experiment`) a minimal experiment that isolates *"can this substrate act at all"* from *"does the REE structure help"* — e.g. a deliberately monolithic/dumb policy scaffold that just forages competently, then re-introduce E1/E2/E3 + commitment gating and measure the *delta*. The claim under test is not "gating helps" but "the substrate can reach the capability floor at which gating is measurable."

**Dependencies:** V3-EXQ-724 (in flight). Feeds from WS-9 (intrinsic motivation) for the competence-earning mechanism — now registered as **MECH-455** (competence-based IM / goal-achievement-progress wanting; candidate, v3_pending). The WS-1 competence experiment is the MECH-455 ON/OFF delta on the goal pipeline.
**Consumes:** `conversion_ceiling_campaign_plan.md`, `failure_autopsy_V3-EXQ-719a`.

**Terminal finding + re-operationalization (2026-07-10, session jolly-bohr-f89cfc; routed here by governance from `failure_autopsy_V3-EXQ-732a_2026-07-10`, status confirmed).**

The H1/H2 discriminator chain designed to localize the competence floor has **bottomed out on the same floor a 4th time (719a → 724 → 732 → 732a)** and is now terminal. Sequence: 724 localized the deficit to the un-varied invariant (prediction-rich/action-poor reps) → 732 tried to discriminate H1 (action/policy substrate) vs H2 (observation encoding) but ran **under-powered** (A2C, small update budget) and its autopsy REJECTED the H2 self-route → **V3-EXQ-732a** applied all four prescribed power-fixes (PPO minibatched learner at ~30× the 732 update budget on both B1/B2; entropy 0.03 + count-based novelty; explicit forage-bonus + running-std reward scaling + advantage normalization; and a **NEW learner-adequacy readiness gate**). 732a self-routed `substrate_not_ready_requeue` because that new gate failed — and its confirmed autopsy finds the gate **observability-confounded, not the substrate inadequate**:

- **The confound.** The adequacy gate references `0.5 × sanity_oracle = 28.6 res/ep`, but the oracle and the learner do not see the same world. `_oracle_action` / `capability_eval.OraclePolicy` reads `env.resources` — **every** resource coordinate — and teleport-beelines to the global nearest with zero exploration cost. The learner sees only a **5×5 LOCAL view** of the 12×12 grid (`causal_grid_world.py` `world_obs_dim`: local 175 + contamination/hazard/resource field slices). No 5×5-local-view policy can reach 50% of a globally-omniscient teleport oracle: L0 vanilla PPO on the *trivial* sanity env (hazards/reef/contamination OFF) = **0.7 res/ep = 1.2%** of the oracle's 57.2, and the `28.6` threshold is **28× the discriminator's own 1.0 competence floor on an easier env** — structurally unreachable. So `learner_adequate=False` is untrustworthy and **H1 vs H2 remains UNRESOLVED**.
- **Power is not the lever.** L0 stayed fragile (cleared the fair 1.0 floor on only 1/3 sanity seeds) even at 30× the update budget with novelty exploration and reward shaping. 732's autopsy pre-registered *exactly* this recurrence as the terminal signal — the operationalization (*local-view foraging-rate vs a global-privileged oracle on reef-bipartite CausalGridWorldV2*) conflates policy competence with the structural local-view-vs-omniscient gap, and four diagnostics have paid down power/instrumentation without moving the question.

**REFUSED — V3-EXQ-732b same-question power bump.** Forbidden by 732's pre-registration; the refusal comes from the **autopsy-stream recurrence** (the claim-keyed re-derive brake counter is 0 because the chain is `claim_ids=[]`, so the mechanical brake never fires — the recurrence is caught only by reading the chain). A *different-question* probe with a fair reference is allowed only after the re-operationalization below AND a competent substrate exists.

**Re-operationalized adequacy reference — the WS-1 design fix.** Any future competence/adequacy gate must reference a **local-view-achievable ceiling**, never the global teleport oracle:

1. **Concrete home = the WS-3 capability yardstick** (`ree-v3/experiments/_lib/capability_eval.py`, calibrated by V3-EXQ-727/728). As built, `build_report` normalizes every metric to `[random_walk_floor, greedy_oracle_ceiling]` and `OraclePolicy` **is** the privileged-global oracle — so the yardstick's own 100%-mark inherits the exact confound 732a exposed. **The fix (author via `/queue-experiment` with the next competence probe — do NOT hand-edit the live harness that V3-EXQ-727 already ran on):** add a **local-view ceiling anchor** — a greedy forager that sees only the 5×5 `resource_field_view` window and steps up its local resource gradient — and normalize adequacy to `[random_floor, local_view_ceiling]`, or gate on ≥ a fraction of a strong local-view learner's asymptote. Keep the global `greedy_oracle` **only** as the floor-achievability control (`oracle_clears_floor`, which the autopsy explicitly permits), never as the learner-adequacy denominator.
2. **Equivalent alternative the autopsy names:** give the floor-achievability control the learner's own 5×5 view, so "floor" means "reachable by a local-view policy" rather than "reachable by an omniscient oracle."

V3-EXQ-727 (PASS / `capability_yardstick_calibrated`) is **not invalidated** — it validly showed `oracle > random` (discrimination) and `oracle ≥ 1.0` (floor-achievability). Only its *normalization ceiling* is observability-unfair; the local-view anchor is an **additive** second ceiling, not a replacement.

**No `substrate_queue` write** (autopsy `recommended_substrate_queue_entry.action = none`): neither H1 nor H2 is confirmed, so no substrate target is licensed. The build target is exactly what a *fairly-operationalized* competence probe would decide — and that operationalization is this fix. **PROMOTES/DEMOTES NOTHING** (diagnostic, `claim_ids=[]`).

**Consumes (this update):** `failure_autopsy_V3-EXQ-732a_2026-07-10.{md,json}`, `failure_autopsy_V3-EXQ-{732,724,719a}`. **Coordinates with — do not duplicate:** V3-EXQ-724 (competence-localization), WS-3 V3-EXQ-727/728 (yardstick calibration + trained all-ON point), `goal_pipeline_plan.md:GAP-2` (the MECH-455 competence-based-IM ON/OFF delta is the WS-1 competence experiment once the substrate is competent).

---

## Tier 1 — Epistemic hygiene (cheap, do early)

### WS-2 — Ceiling-claim demotion rule
**Why:** 34 claims carry `substrate_ceiling` + 64 carry `pending_retest_after_substrate`, and the category explicitly says a failed discrimination is *not* a falsification. Honest, often correct — but it is also the exact structural incentive that lets a theory never lose. 72% of 871 claims are `candidate`. Risk: the registry fills with beautiful unkillable hypotheses.

**First deliverable:** Register a new **GOV-*** claim encoding a pre-registered rule, e.g.: *"A claim that hits the substrate ceiling N times without a positive result on any richer substrate is demoted, not parked indefinitely; the competing reading (the mechanism is inert / doing no work) must be carried with equal weight until a positive discrimination exists."* Define N, the "richer substrate" bar, and the demotion target state. Wire it into the governance cycle.

**Dependencies:** none. Pure governance. Do now.
**Skill path:** claim registration in `claims.yaml` (governance-only edit under an active claim) + `governance` skill.

### WS-14 — Bottleneck fan-out escalation rule
**Why:** GOV-CEIL-1 (WS-2), GOV-DIAG-1, and the `/failure-autopsy` re-derive brake all *detect* that work is circling one root and *refuse* another same-question sequential letter — but none prescribes the constructive next move, so the default is a single re-posed sequential probe. A single discriminator can silently inherit the prior confound and return a confident-but-wrong verdict; the failure mode is **building the wrong substrate on a laundered artifact**, not lost time. The 719a→724→732→732a competence chain is the worked example: four sequential discriminators circling the same floor, the last two inheriting the 732 global-oracle confound.

**Deliverable (DONE 2026-07-10):** Registered **GOV-FANOUT-1** (`claims.yaml`, governance_rule; PROMOTES/DEMOTES NOTHING on register) — the constructive complement to the detection rules. When a brake fires AND the open question is a *discrimination* (which-hypothesis, not a single named build), the standard escalates from sequential retry to a **diverse parallel portfolio**: enumerate the live hypotheses, design ≥K legs each on a *different* design axis (representation / measurement / observation / drive / algorithm — never power-bumps), each declaring its null, adversarially design-audited for coverage + verdict-aliasing before queuing, run in parallel (accepting some legs are `non_contributory`). Wired: `/failure-autopsy` (emit `fanout_recommendation` on a brake-fired discrimination — producer), `/queue-experiment` Step 2.5b (portfolio-vs-sequential + declared-null + design-audit — consumer), `/governance` Step 6a-v-quater (surface fanout-candidate lineages), `cognitive_architecture_graveyard.md` antibody (sequential-retry-instead-of-fan-out).

**Worked example (this session, 2026-07-10):** the 737/738/739 portfolio replaced the 719a→724→732→732a sequential chain — P-A trainable policy head on the REE latent (representation), P-B local-view-achievable ceiling anchor (measurement), P-C observation-encoder probe (observation, held to reserve). P-B (V3-EXQ-738) ran first and refuted H2 (the 1.0 floor is reachable from the 5×5 local view), re-valuing P-C to reserve — an early answer the sequential chain could not have produced.

**Dependencies:** none. Pure governance; reuses the existing brake detection. Complements WS-2.
**Skill path:** claim registration in `claims.yaml` + skill wiring (`/failure-autopsy`, `/queue-experiment`, `/governance`, both dirs).

### WS-3 — Capability-eval yardstick
**Why:** The project currently cannot cleanly tell "the claim is wrong" from "the substrate is too coarse" partly because it has no *independent* capability yardstick. A small, claim-agnostic benchmark suite fixes this and directly supports WS-1 and WS-2.

**First deliverable:** A minimal capability-eval suite (foraging competence, survival horizon, goal-reach rate, simple planning depth) that is *independent of any REE mechanism claim* and reported alongside every all-ON run. It becomes the denominator: "structure X moved capability metric Y by Z on a substrate already above the competence floor."

**Dependencies:** light. Pairs with WS-1.

**Progress (2026-07-09, session vigorous-yalow-bc7f39):**
- Built the reusable, claim-agnostic reporting block `ree-v3/experiments/_lib/capability_eval.py`. Four env-observable metrics, no REE mechanism dependency: `foraging_competence` (mean resources/ep — the same statistic as the V3-EXQ-724 competence DV, reused), `survival_horizon` (mean ticks survived + death_rate on `agent_health<=0`), `goal_reach_rate` (fraction of episodes collecting ≥1 resource), `planning_depth` (longest strictly-decreasing nearest-resource-distance run — an env-observable multi-step-directedness proxy). Exposes `RandomPolicy`/`OraclePolicy`/`REEForwardPolicy`, `evaluate_seed`, `summarize_arm`, `build_report` (normalizes any policy to `[random_floor, oracle_ceiling]` per metric). The greedy oracle is reused verbatim from V3-EXQ-724's positive control (no duplication).
- Queued **V3-EXQ-727** (baseline; `claim_ids=[]`; PROMOTES NOTHING; prio 100) calibrating the yardstick over `random_walk` / `ree_p0warmup_allon` / `greedy_oracle` × 3 seeds. Self-route: oracle clears the 1.0 competence floor AND oracle>random on foraging → `capability_yardstick_calibrated`, else `substrate_not_ready_requeue`. Dry-run PASS (oracle 3.5 > random 0.0 forage/ep; all four metrics separate the policies). LANDED ree-v3 `main` 843db71; coordinator `/queue/active` PRESENT.
- **727 deliberately did NOT re-train the all-ON stack** — the *trained* all-ON denominator on the full metric set is produced by V3-EXQ-728 (below).
- **Owed step CLOSED (2026-07-09T17:12Z, session priceless-newton-eebcc3):** authored + queued **V3-EXQ-728** (baseline; `claim_ids=[]`; PROMOTES NOTHING; prio 100) via `/queue-experiment` — the TRAINED all-ON capability point. Three arms × 3 seeds: `random_walk` (floor) / `ree_trained_allon` (all-ON 714 ARM_ON trained with the **V3-EXQ-724 A0 recipe**: P0=200 world-model warmup + P1=90 two-head REINFORCE [lateral-PFC bias + OFC devaluation], SD-056 e2 encoder FROZEN through P1) / `greedy_oracle` (ceiling, reused verbatim from 724). Eval via the yardstick's `REEForwardPolicy` + `build_report` — the **identical** path 727 used for its `ree_p0warmup_allon` arm, so the 727 (P0-warmup only) vs 728 (P0+P1 trained) comparison isolates the P1 competence-training effect with no eval-protocol confound. Reports all four metrics' normalized positions for the trained point on the 727 floor/ceiling scale; the trained point's supra-floor status is REPORTED CONTEXT, not a governance verdict (excluded from scoring). NO baseline mint (substrate in flux for this lineage; the trained point IS the denominator, not a reusable OFF arm). `validate_experiments --strict` OK; dry-run PASS (oracle 3.5 > random 0.0 forage/ep; trained P0+P1 harness runs clean; all four metrics normalize). LANDED ree-v3 `main` c83221c; coordinator `/queue/add` applied:true, `/queue/active` PRESENT. **This closes WS-3's "reported alongside every all-ON run" clause** — the reusable yardstick is built + validated + calibrated + wired into trained all-ON runs. The trained numbers land when the fleet executes 727/728.

---

## Tier 2 — Theory grounding (literature + writing; parallelizable)

### WS-4 — Formal-ancestor mapping
**Why:** Much of REE re-derives, from biology, machinery that has a mature formal literature — and pays the cost of rebuilding without collecting the benefit of the existing math. Biology-first convergence onto an independent formalism is itself evidence (the KAUST/Neural-Computers convergence argument), but only if the mapping is made explicit.

**First deliverable:** A table mapping the top ~30 load-bearing MECH/ARC to their nearest formal ancestor and that ancestor's measurement apparatus. Seed rows:
- MECH-163 (VTA/hippocampal MB vs SNc habit MF arbitration) → Daw, Niv & Dayan 2005 uncertainty-based arbitration (has a worked arbitration formalism — adopt it, test *deviations*).
- Valenced viability map + hippocampal trajectory proposal → Successor Representation (Dayan 1993; Stachenfeld et al. 2017 hippocampus-as-SR); Dreamer V3 / MuZero latent planning.
- Precision routing / act-under-uncertainty → active inference (see WS-5).
- Commit + a0→a1→a2 stepping + urgency interrupt (MECH-090/091) → options framework (Sutton/Precup/Singh) + option interruption.
- Broadcast/override + narrative depth → Global Workspace Theory (Dehaene neuronal-workspace formalization); ties to SD-064 J-lens work.
- E1/E2 slow/fast world-model split → JEPA / hierarchical world models (already referenced in `jepa_e1e2_integration_contract.md`).

**Reserve novelty for the genuinely new parts:** residue/ownership, the commit boundary + hypothesis tag, the axiomatic ethics derivation.
**Dependencies:** none. Big payoff. Parallelize with a lit-pull per row.

### WS-5 — Active-inference bridge
**Why:** Precision-weighted prediction error, action-under-uncertainty, epistemic vs pragmatic value — this is the free-energy program (Friston). REE's docs pointedly *don't* cite it and reject the single-functional framing. But active inference can be done with *factorized* objectives, so the "one scalar" objection is partly a strawman — and it hands you the calculus for free.

**First deliverable:** `/lit-pull` on active inference (Parr, Pezzulo & Friston textbook; precision & epistemic value) → a bridge doc that (a) imports the precision/epistemic-value math REE can reuse, and (b) documents the *exact* points where REE's three-incommensurable-channels design genuinely departs from a single free-energy functional. Cross-link ARC-021 / MECH-069.
**Dependencies:** feeds WS-4.

### WS-6 — Bitter-Lesson rebuttal
**Why:** REE is the maximally hand-structured bet (871 claims, "demote drift back to biology"). Sutton's Bitter Lesson says hand-engineered structure loses to scale + search. WS-1's competence floor is arguably that lesson biting. The project needs an explicit, written answer — not a dismissal.

**First deliverable:** A cited position doc answering "why won't scale + search eat this structure?" Steelman Sutton; engage the rebuttals (Chollet's "measure of intelligence" / ARC on why *some* priors pay; the structure-vs-scale debate). Land on a falsifiable stance: which parts of REE claim to be scale-invariant priors vs which are scaffolding that scale would replace.

### WS-7 — Corrigibility positioning
**Why:** "Corrigibility" is used as a design goal; there is a formal literature on why naive corrigibility fails (MIRI corrigibility papers; Soares et al.). The commit-boundary is a fresh angle *on* corrigibility and should be argued against that backdrop rather than in isolation.

**First deliverable:** A short positioning doc: map REE's commit-boundary + beta-gate + hypothesis-tag onto the formal corrigibility desiderata; show where it helps, where it is silent, where it could fail. Ties to the SENT-* sentinel layer and ethics perimeter.

### WS-8 — Cognitive-architecture graveyard
**Why:** The "integrate everything into one mind" architecture has a graveyard (Soar, ACT-R, LeCun's 2022 AMI position paper). Studying *how they hit their ceilings* is the cheapest way to avoid repeating them.

**First deliverable:** A study doc extracting concrete anti-patterns (where integration overhead outran capability, where hand-specified structure ossified) and mapping each to a REE risk — especially the governance-mass-vs-cognitive-mass ratio flagged in the critique.

### WS-9 — Intrinsic-motivation lit-pull
**Why:** Directly relevant to WS-1 (competence floor) and to the goal/wanting/liking pipeline.

**First deliverable:** `/lit-pull` on intrinsic motivation / developmental robotics (Oudeyer; Schmidhuber curiosity/compression; Baldassarre) → candidate mechanisms for *earning* competence, feeding WS-1 and `goal_pipeline_plan.md`.

**DONE 2026-07-09** → [`intrinsic_motivation_competence_mechanisms.md`](intrinsic_motivation_competence_mechanisms.md). Four canonical sources pulled into `targeted_review_intrinsic_motivation_exploration/`. Key result: REE already holds the whole *knowledge-based* IM typology (MECH-314 info-gain / MECH-314a novelty / MECH-314c learning-progress = Oudeyer&Kaplan's typology re-expressed; Bellemare pseudocounts = MECH-314a's RL estimator), but has **no competence-based IM** (Baldassarre & Mirolli's second family: reward = goal-achievement progress). The competence floor WS-1 is chasing is the predicted failure of earning skills with a knowledge-based drive alone. Ranked substrate-implementable mechanisms with plane/claim tags in the doc; **#1 = goal-achievement-progress wanting (goal pipeline / drive plane, REGISTERED 2026-07-09 as candidate MECH-455)**. Substrate caveat surfaced: world-model-side bonuses (#2 MECH-314c per-candidate, #3 MECH-314a pseudocount) are inert until the EMA→E3-selection routing is repaired (EXQ-141b/590a) — the competence-based mechanism is partly exempt because it injects into the wanting path, another reason it ranks first.

---

## Tier 3 — Thesis exercise (needs substrate; puts load on the central claim)

### WS-10 — Minimal 2-agent world
**Why:** The entire philosophical payoff — ethics from modelling others as self-like, love as mechanism, responsibility as the point — is **V5, multi-agent**. V3 is single-agent. So the claim REE exists to demonstrate is currently *untouched by running code*. The axioms are doing philosophical, not computational, work.

**First deliverable:** Spec (not necessarily build) a trivial 2-agent environment that puts *any* load on the ethics thesis — e.g. two agents in `CausalGridWorld` where one can harm/benefit the other's viability gradient. Enough to make MECH-164 (shared/leaked z_beta) and the "sufficiently-like-me" similarity model do *some* measurable work. Coordinate with `multi_agent_ecology_v5_plan.md` and `fast_empathy_v5_plan.md` — this is a deliberate early down-payment on V5, scoped minimal.
**Dependencies:** WS-1 (need single-agent competence first) — an agent that can't act alone can't be ethical toward another.

### WS-11 — Early-gating vs late-judging demonstration
**Why:** REE's whole pitch is that RLHF / Constitutional AI "operate too late." That pitch is currently an assertion. One concrete demonstration would be worth 200 candidate claims.

**First deliverable:** Design a single task where a late-judging baseline (score/filter after generation) demonstrably fails and REE's early commit-gating demonstrably succeeds — the vmPFC/EVR intuition made executable (correct knowledge, catastrophic choice). This is the flagship falsifiable win the project should be hunting.
**Dependencies:** WS-1, WS-3 (need a capability yardstick + a competent substrate to run it on).

---

## Tier 4 — Adversarial ethics

### WS-12 — Similarity / dehumanization failure mode
**Why:** Axiom 5 grounds ethics in modelling others as *sufficiently like me*. That means the architecture has a built-in dehumanization channel: anything classified as **not** sufficiently-like-me falls *outside* the care gradient by construction — structurally, the computational shape of out-group exclusion and the mechanism of every atrocity. A design that locates ethics in similarity inherits similarity's failure mode. Currently unaddressed.

**First deliverable:** Register a first-class claim naming this failure mode, plus a red-team question: what prevents the similarity model from gating care in a way that reproduces dehumanization? Candidate mitigations to evaluate (uncertainty-driven expansion as a floor; a similarity *lower bound* on care). Cross-link Axiom 5, Axiom 7 (love's expansion), INV-001, ethics perimeter.

**Status (2026-07-09): DONE.** Registered as **`EXT-009`** (`claim_type: external_failure_mode`, `subject: ree.similarity_gated_care_collapse`, `reflexive: true`) in `docs/claims/claims.yaml`, landed on `origin/master`. Carries `red_team_question` and four `candidate_mitigations` (Axiom-7 love-expansion as a hard care FLOOR; a similarity lower-bound where care saturates at a positive constant rather than dropping to zero; INV-070 epistemic-responsibility coupling of the care-gate; INV-071/Axiom-8 language-mediated re-admission as a standing duty). `ree_mechanism` points at INV-029/070/071/072 + MECH-164 as *partial/candidate* addresses (not a solved defence), explicitly distinguishing it from EXT-001..008 where `ree_mechanism` names REE's *solution*. **Not a duplicate** of INV-072 (violence corollary) / INV-070 / INV-071: those treat similarity-collapse as a clinical/human signature and as ethical invariants; EXT-009 turns the same structure back on REE's *own* design as a discoverable, standing red-team caution and asks what in the architecture prevents it. Chose `external_failure_mode` because it is the registry's failure-mode namespace and is exempt from governance promote/demote (correct for a standing caution) and avoids the V3-pending / asked-bucket gates. **Feeds WS-13** (moral-philosophy red-team): the "does love *really* expand transitively, or does 'sufficiently like me' quietly gate it?" audit is the philosophical half of the same question — WS-13 should cite EXT-009 as the registered structural statement it is stress-testing.

### WS-13 — Moral-philosophy red-team
**Why:** Since ethics is the thesis, the right critics are adversarial philosophers/ethicists, not only ML people. The axiom chain makes strong moves (love expands transitively to *universal* love under uncertainty) that deserve hostile scrutiny.

**First deliverable:** An adversarial audit of the axiom chain — does love *really* expand transitively under uncertainty, or does the "sufficiently like me" clause quietly gate it (linking WS-12)? Where does the derivation smuggle in a premise? Produce a list of the chain's load-bearing-but-contestable steps for external ethicist review.

---

## Cross-cutting notes

- **Sequencing:** WS-1 unblocks WS-10/WS-11. WS-2/WS-3 are do-now hygiene with no dependencies. Tier-2 WS-4..WS-9 are lit/writing and can run in parallel by different sessions. WS-12/WS-13 pair.
- **Skill paths:** lit threads → `/lit-pull`; new claims → `claims.yaml` + `governance`; experiments → `/queue-experiment` only; never hand-edit the queue.
- **Anti-duplication check** before starting any WS: `ree-v3/experiment_queue.json`, `conversion_ceiling_campaign_plan.md`, other `*_plan.md` status tables, `TASK_CLAIMS.json`.
- **Source:** distilled from a 2026-07-09 strategic critique session (ahead / reinventing / flawed / needs-work + external lenses). See WORKSPACE_STATE Recent Work for that session.
