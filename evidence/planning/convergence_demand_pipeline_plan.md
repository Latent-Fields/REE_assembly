---
# Process-lane plan. generation: process keeps these nodes OUT of the V3 closure
# % (read_closure counts only generation: v3) and renders them on the shared
# `process` tab alongside the arm-reuse tooling lane. This pipeline owns no
# scientific claims directly -- it TERMINATES in candidate claims registered into
# OTHER nodes' depends_on -- so its nodes track the intake machinery, not science.
closure_plan:
  id: convergence_demand_pipeline
  generation: process
  title: "Convergence Demand Pipeline (closure-driven external-inspiration intake)"
  registered: 2026-06-17
  last_updated: 2026-07-18
  scope_claims: []
  nodes:
    - id: "convergence_demand_pipeline:QUEUE"
      title: "Demand queue CDQ-001..005 (Section-4 rows) + governance Step-6b Sense hook"
      phase: 1
      status: done
      severity: high
      last_updated: 2026-06-17
      resume_condition: "First Action #1 landed 2026-06-17: convergence_demand_queue.v1.json + /governance Step-6b Sense pass"
    - id: "convergence_demand_pipeline:LOOP"
      title: "Sense -> Mine -> Register -> Adjudicate cadence (demand-driven, piggybacks governance)"
      phase: 1
      status: done
      severity: medium
      depends_on: ["convergence_demand_pipeline:QUEUE"]
      last_updated: 2026-06-17
    - id: "convergence_demand_pipeline:HIGH-DREAMCODER"
      title: "Execute HIGH row -- DreamCoder + DreamerV3 codebook intake -> registered candidate claim (arc_062 GAP-B/K, behavioral_diversity GAP-B)"
      phase: 2
      status: done
      severity: high
      depends_on: ["convergence_demand_pipeline:LOOP"]
      last_updated: 2026-06-19
      resume_condition: "DONE 2026-06-17: DreamCoder + DreamerV3-codebook intakes done; MECH-437 + MECH-438 registered candidate/substrate_conditional/generation:v4 wired into the arc_062 cluster depends_on (landed master dcca2cb). (Prior 'in flight as chip task_88e97a80' was a stale pointer -- task_88e97a80 is the closure-map process-lane task, not this work; reconciled 2026-06-19.)"
    - id: "convergence_demand_pipeline:HANDOFF-REACTIVATE"
      title: "Re-activate the REE_convergence -> REE_assembly handoff pipeline (first packet since 2026-02-24) on the HIGH row"
      phase: 2
      status: done
      severity: medium
      depends_on: ["convergence_demand_pipeline:HIGH-DREAMCODER"]
      last_updated: 2026-06-19
      resume_condition: "DONE 2026-06-19: end-to-end loop validated on the three June rows. All 3 June packets re-validated gate-ready; receipts CRCT-RULE-DISTINGUISHABILITY/-TONIC-EXPLORATION-NOISE/-QUALITY-DIVERSITY-20260619 authored (accepted; decision_ref evidence/decisions/convergence_packet_adjudication_2026-06-19.md) and mirrored back to REE_convergence/handoff/packets/receipts/ via run_cross_repo_handoff.py (first batch since 2026-02-24). Direct claims.yaml registration superseded the tool register step; receipts promote nothing."
    - id: "convergence_demand_pipeline:MED-ROWS"
      title: "Execute MED demand rows -- NoisyNet/RND exploration-floor; Quality-Diversity/MAP-Elites diversity-survives-commit"
      phase: 3
      status: done
      severity: medium
      depends_on: ["convergence_demand_pipeline:HANDOFF-REACTIVATE"]
      last_updated: 2026-06-19
      resume_condition: "DONE 2026-06-18..19: CDQ-002 (NoisyNet + RND/Plan2Explore -> MECH-440/441 candidate/substrate_ceiling/v3) and CDQ-003 (Quality-Diversity/MAP-Elites -> MECH-442 candidate/substrate_conditional/v3) Mine+Register complete with biology lit-pulls; both packets handed off + receipts mirrored 2026-06-19. Candidates only; no node promoted, no V3 dependency added."
    - id: "convergence_demand_pipeline:LOW-MUZERO"
      title: "Pull the COMPLETED MuZero/EfficientZero reanalyze adapter (replay write-gating, arc_062 GAP-K) through to a registered claim"
      phase: 3
      status: done
      severity: low
      depends_on: ["convergence_demand_pipeline:HANDOFF-REACTIVATE"]
      last_updated: 2026-06-19
      resume_condition: "DONE 2026-06-19 (session convergence-cdq005-muzero-reanalyze-20260619T1856Z; CDQ-005). MuZero/EfficientZero reanalyze intake (sources/muzero/, COMPLETED) pulled through to registered candidate claims MECH-443 (priority_weighted_replay_write_selection) + MECH-444 (staleness_gated_target_refresh_on_replay_write), both candidate/substrate_ceiling/generation:v3/v3_pending, each with a falsifier, wired (claim depends_on) into the GAP-K cluster (MECH-319/MECH-094/MECH-312/ARC-062). NON-DUPLICATIVE vs MECH-319 (the already-owned BINARY block-vs-admit gate, V3-EXQ-628 PASS): the pair adds the GRADED layer (which/how-strongly + freshness). Biology /lit-pull discharged BEFORE registering (evidence/literature/targeted_review_replay_prioritization_mech_319/, 5 sources, SUPPORTED-with-refinement; priority is update-utility/gain x need NOT reward magnitude). Arch stub docs/architecture/prioritized_replay_write_gating.md; GAP-K node convergence_2026_06_19 note added (no status/owner change). Promotion packet CPKT-MUZERO-REANALYZE-20260619 written + VALID + GATE-READY in REE_convergence/handoff/packets/outbox/. Candidates only -- promotes nothing, adds no V3 dependency. RESIDUAL (not blocking this node): the cross-repo handoff RUN + receipt-mirror of the new packet rides the HANDOFF-REACTIVATE cadence (which, like CDQ-002/003, treats direct claims.yaml registration as the load-bearing step; receipts promote nothing)."
    - id: "convergence_demand_pipeline:HIGH-CDQ007-COMPETENCE-BOOTSTRAP"
      title: "Execute CDQ-007 (HIGH) -- DreamerV3 stabilisation lens + VPT/AlphaStar BC-seed intake -> competence-bootstrap candidate claims wired into MECH-457"
      phase: 3
      status: done
      severity: high
      depends_on: ["convergence_demand_pipeline:LOOP"]
      last_updated: 2026-07-18
      resume_condition: >
        DONE 2026-07-18 (session hopeful-mcclintock-9b9948; CDQ-007). Routed by
        failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18 (confirmed; non_contributory /
        competence_implementation_gap; four axes eliminated -- capacity 769, drive-schedule 770,
        reward-coupling 771, credit-horizon 772; re-derive brake FIRED 7th). Biology /lit-pull
        discharged BEFORE registration per biology_before_formal_definitions:
        evidence/literature/targeted_review_competence_bootstrap_without_demonstrator/ (8 sources).
        Mined: sources/dreamer-v3/ EXTENDED with a second, non-overlapping lens
        (actor_critic_stabilisation.md; the pre-existing intake was codebook-only -> MECH-438) and
        NEW sources/vpt-bc-seed/. Registered MECH-459 (return-scale invariance blocks actor
        bootstrap), MECH-460 (transient behavioural-prior bootstrap), MECH-461 (innate
        action-primitive basis + reward-independent engagement drive) -- all candidate /
        implementation_phase v3 / v3_pending, each with a falsifier, all three wired into MECH-457
        depends_on. Arch stub docs/architecture/competence_bootstrap_mechanisms.md.
        COORDINATION HONOURED: the GOV-FANOUT-1 discrimination (V3-EXQ-780 H-bc-prior vs
        V3-EXQ-781 H-approach-primitive) is untouched and un-pre-empted -- 460/461 registered as an
        EVEN-HANDED pair, 459 flagged as a THIRD route belonging to neither leg,
        hypothesis_space_registry.v1.json deliberately NOT amended (a third ALIVE leg is a
        /governance decision under the GOV-FANOUT-1 growth contract),
        mech457_competence_bootstrap_explorer stays blocked_pending_discrimination. No build
        licensed, no experiment queued, nothing promoted. RESIDUAL (not blocking): the promotion
        packet + cross-repo handoff receipt ride the HANDOFF-REACTIVATE cadence, which since
        CDQ-002/003/005 treats direct claims.yaml registration as the load-bearing step (receipts
        are acknowledgment lineage and promote nothing).
---

# Convergence Demand Pipeline -- closure-driven external-inspiration intake

Status: ACTIVE (plan of record)
Created: 2026-06-17T15:11:59Z
Activated: 2026-06-17T17:24:56Z (First Action #1 landed)
Owner workstream: REE_convergence -> REE_assembly handoff
Generation: process (rendered on the closure map's shared `process` tab via the
`closure_plan:` frontmatter above; still excluded from the V3 closure % because
`read_closure` counts only `generation: v3`)

> This is a process plan, not a v3 substrate node. It describes how external
> AI-assembly projects are mined on demand to unstick *specific* open closure
> nodes, and how that mining terminates in **registered candidate claims** in
> `REE_assembly` rather than survey prose in `REE_convergence`.

---

## 1. Problem

`REE_convergence` already has the full machinery to translate an external model
into the REE comparison format and promote it into `REE_assembly`:
intake (`sources/<name>/source.yaml` + artifacts) -> comparison/scorecard ->
promotion packet (`handoff/packets/outbox/`) -> `tools/run_cross_repo_handoff.py`
-> receipt (`handoff/packets/receipts/`). DreamerV3, MuZero, DNC, JEPA,
Active-Inference, RAG, RT-2, GNN-planning and multimodal-agents are all intaken.

Two things stop it from "pushing progress onward":

1. **It is stale.** The last handoff packets landed 2026-02-24 (~4 months ago).
   The pipeline ran one big batch and went quiet.
2. **It is supply-driven, not demand-driven.** The Feb batch was a general
   survey of famous models, chosen by prominence, not by which *open closure
   node* they could unstick. Intakes completed in `REE_convergence` did not, in
   general, terminate in candidate claims wired into a specific blocked node's
   `depends_on`.

Net: a mature translation engine that is not pointed at the work that is
actually stuck.

## 2. Principle

**The closure map says what is mechanistically stuck; convergence finds who
solved it externally; the handoff registers candidate claims that unstick the
node.** Convergence becomes a *router*, not an archive.

A node is a *demand candidate* when its latest verdict is "mechanism unclear" or
"substrate ceiling" -- i.e. the necessity is established but the *mechanism* to
achieve it is not. These are exactly the nodes where an external design that has
already solved the analogous problem is highest-value.

## 3. Non-negotiable disciplines (carried from existing project doctrine)

- **Intake must REGISTER claims, not seed prose.** Every demand-driven intake
  terminates in a promotion packet that registers version-scoped candidate
  claims into `docs/claims/claims.yaml`, wired into the target node's
  `depends_on`, with an architecture-doc stub. "Future-registration" prose is a
  failure of the pipeline. (See memory: thought-intake-must-register-claims /
  intake-must-reap-claims.) Decide-whether-to-build is a *later* governance step.
- **V3 primacy.** V3 closure is the primary objective. Demand-driven intakes that
  map onto V4/V5-leaning mechanisms are *preparatory only*: they register
  candidate claims tagged `generation: v4|v5` and MUST NOT place a build
  dependency on the v3 critical path. The pipeline surfaces ideas; it does not
  reprioritise v3. (See the companion version-layering guard work, Section 7.)
- **Biology before formal definitions.** Where an external mechanism instantiates
  a formal concept that REE will own as an SD/MECH, commission a biology
  `/lit-pull` before registering (canonical failures SD-003, SD-010/011).

## 4. The demand queue (seeded from current open nodes, 2026-06-17)

Each row: a stuck node -> the external source whose solution maps onto its
mechanism gap -> intake action. Sources already (even partially) in
`REE_convergence` are marked; the rest are new intakes.

| Closure node(s) | Mechanism gap | External source | Intake state | Priority |
|---|---|---|---|---|
| `arc_062_rule_apprehension:GAP-B`, `:GAP-K`; `behavioral_diversity_isolation:GAP-B` | Minted rules must stay mutually distinguishable to remain selectable (CRF conflict-gate lockout: theta=0.15+0.25*(n_matched-1) gates out 7-8 co-matching rules) | **DreamCoder** (wake-sleep library abstraction; minted programs stay distinguishable to be selectable) + **DreamerV3 discrete latent codebook** (categorical keys separable by construction) | COMPLETED (DreamCoder + DreamerV3 codebook both intaken 2026-06-17) | HIGH -- DONE: MECH-437/438 registered + handed off (2026-06-19) |
| `behavioral_diversity_isolation:GAP-C`; `arc_062_rule_apprehension:GAP-H` | Tonic, state-conditioned exploration noise floor (MECH-313 LC-NE analog) -- distinct from a fixed epsilon schedule | **NoisyNet** (learned per-parameter, self-annealing, state-dependent noise); secondary **RND / Plan2Explore** (model-disagreement curiosity = MECH-314) | COMPLETED -- MECH-440/441 registered + handed off (2026-06-18..19) | MED |
| `behavioral_diversity_isolation:GAP-B` (conversion-to-committed-action) | Diversity must be maintained in a structure that survives the selection/commit step | **Quality-Diversity / MAP-Elites** (Cully et al. 2015: explicit behavioral-descriptor archive surviving selection) -- structurally the top-k shortlist fix already validated by V3-EXQ-569i | COMPLETED -- MECH-442 registered + handed off (2026-06-18..19) | MED |
| `sd_037_axis_b:P1b` -> `P2`/`P3`/`P4` | Automatic curriculum that keeps a target signal (z_harm_a sustained-threat window) in a learnable band | **PLR / Prioritized Level Replay** + **POET**; affective framing: active-avoidance / anxiety-as-pessimistic-prior RL | NEW | LOW (P1b in flight via V3-EXQ-625d; intake feeds the axis-(c) escalation only if 625d exhausts the env-kwarg surface) |
| `conversion_ceiling_campaign:P-comp`; `behavioral_diversity_isolation:GAP-K` (CDQ-007) | A learned actor-critic converter cannot extract a competent policy from a PROVABLY SUFFICIENT observation, and is invariant to every config/env/credit/capacity lever tried (four axes eliminated: 769 capacity, 770 drive-schedule, 771 reward-coupling, 772 credit-horizon). Readiness met on every leg (local_view_greedy 48-55, oracle 57-61 vs a 1.0 floor) yet every treatment arm forages at the ~0-1 floor. BC (imitation 32.72) is the only floor-clearing existence proof. | **DreamerV3** re-mined through the actor-critic STABILISATION lens (symlog, twohot/CE critic, one-sided percentile return normalisation, fixed entropy, imagination-horizon) + **VPT / AlphaStar / DQfD / JSRL** BC-seed-then-RL | COMPLETED 2026-07-18 -- MECH-459/460/461 registered + wired into MECH-457 `depends_on` | HIGH -- DONE |
| `arc_062_rule_apprehension:GAP-K` (replay write-gating) | Gating which replayed/imagined transitions may write to the rule layer | **MuZero/EfficientZero reanalyze** + hippocampal SWR prioritized replay | MuZero COMPLETED (`sources/muzero/`) -- pull the adapter through to a registered claim | LOW |

Maintained alongside this doc as a structured file: `convergence_demand_queue.v1.json`
(created by the first progress chip; mirrors this table for tooling).

### 4a. Routable-demand fields (added 2026-06-20)

The table above tells you what is stuck and which external source maps onto it,
but not *where the demand goes next* or *what is holding it back* — those lived
only in each row's prose `last_known_state_note`, invisible to any dispatcher.
Three machine-readable fields per row close that gap (backfilled onto
CDQ-001..006; minted on every new row by `/governance` Step 6b):

- **`routing_target`** (enum) — the downstream action once the row is unblocked:
  - `convergence_intake` — Mine a `REE_convergence/sources/<name>/` source then
    Register candidate claim(s) into `claims.yaml` wired into the node's
    `depends_on`. The native route (CDQ-001/002/003/005).
  - `design_query` — resolve a design fork on an **already-registered** claim;
    registers no new claim; routes to `/thought-digestion` or `/claim-synthesis`
    (CDQ-006, the MECH-442 descriptor fork).
  - `experiment` — needs a discriminative run; routes to `/queue-experiment`.
  - `decide_to_build` — claim(s) registered; needs a decide-whether-to-build
    adjudication before any substrate build.

  A biology `/lit-pull` is deliberately **not** a `routing_target`: under the
  Section-3 `biology_before_formal_definitions` discipline it is a mandatory
  precondition sub-step of `convergence_intake`/`design_query`, not a terminal
  route (CDQ-002/003/005 each ran one before registering).

- **`blocks_on`** (array) — machine-readable gates; `[]` = dispatchable now. Each
  entry `{"kind": "experiment"|"claim"|"substrate", "id", "clears_when", "note"}`.
  Encodes blockers that were prose-only — e.g. CDQ-004's "do not mine until
  V3-EXQ-625d resolves" and CDQ-006's gate on the MECH-439 689-successor.

- **`completion_criterion`** (object) — the exit gate: when the demand is
  satisfied. `{"kind": "claims_registered"|"design_resolved"|"experiment_pass"|
  "decision_recorded", "detail", "satisfied"}`. For `claims_registered`,
  `satisfied` is true once `registered_candidate_claims` is non-empty AND those
  claims are wired into the node's `depends_on`; the other kinds are set
  explicitly when the named artifact lands.

A dispatcher's "is this row ready?" check is then derivable
(`blocks_on` all clear AND `completion_criterion.satisfied == false`) with no
stored status field to drift. This is the schema prerequisite for the optional
next step — `/governance` Step 6b actually *emitting* a routed work-item for the
highest-priority unblocked row instead of only parking it.

## 5. The loop (cadence)

Small and continuous beats another big survey.

1. **Sense** (governance-adjacent, ~weekly or on closure-drift change): re-read
   the closure snapshot + drift report; for any node newly verdicted "mechanism
   unclear / substrate ceiling", add a demand-queue row naming the candidate
   external source.
2. **Mine** (per high-priority row): create/extend the `REE_convergence` intake;
   translate into the REE comparison format with an explicit **adapter delta**
   (how the external mechanism maps onto the REE locus named by the node).
3. **Register** (the value-add step): produce the promotion packet; run the
   cross-repo handoff; register version-scoped candidate claims into
   `claims.yaml` wired into the node's `depends_on` + arch-doc stub.
4. **Adjudicate** (later, normal governance): decide-whether-to-build per the
   usual promotion pipeline. The pipeline's job ends at a registered, testable
   candidate claim.

## 6. Success criteria

- Each completed demand-driven intake produces >=1 registered candidate claim
  wired into a real open node's `depends_on` (not orphan prose).
- The handoff pipeline is re-activated (first new packet since 2026-02-24).
- At least one stuck node's plan frontmatter gains a concrete
  mechanism-candidate it did not have before.
- No v3 critical-path node acquires a new dependency on V4/V5-tagged intake work.

## 7. Companion work (tracked separately)

- **Version-layering guards** (V3 primacy enforcement): doctrine + mechanical
  guards so higher-version substrate changes cannot destabilise v3. Motivated by
  the 2026-06-17 V3-EXQ-654e incident (a DR-12 / first-V4 substrate landed an
  unconditional call-site into the shared V3 agent path and crash-burned a v3
  critical-path experiment). See Section 3 "V3 primacy" for the pipeline-side
  rule; the runner/test guards are their own chip.
- **ERROR-observability fix**: a crash-before-manifest (empty `output_file`) is
  removed from the queue via `report_queue_remove` with no result row / manifest,
  so it never reaches `pending_review` or `/diagnose-errors` (the 654e silent
  stall). The FAIL/ERROR-class twin of the fixed UNKNOWN silent-drop bug. Own chip.

## 8. First actions (chips)

1. [DONE 2026-06-17] Build `convergence_demand_queue.v1.json` from Section 4 + add
   the "Sense" step to the governance cadence.
   - Queue file: `evidence/planning/convergence_demand_queue.v1.json`
     (schema `convergence_demand_queue/v1`; 5 rows CDQ-001..CDQ-005 mirroring the
     Section-4 table; append-only; every row carries `generation` +
     `blocks_v3_critical_path: false` for V3 primacy).
   - Sense hook: `/governance` **Step 6b** ("Convergence demand-queue Sense pass",
     non-interactive, read-only over `closure_status.md` + `closure_drift.md`),
     mirrored to both `.claude/skills/governance/SKILL.md` and
     `.agents/skills/governance/SKILL.md`. Runs each governance cycle right after the
     closure-drift reconcile (Step 5b) and appends a CDQ row for any node newly
     verdicted mechanism-unclear / `substrate_ceiling`. Chosen as the lightest durable
     hook (no new standing automation; piggybacks the existing governance cadence).
2. [DONE 2026-06-17] Execute the HIGH-priority row (DreamCoder + DreamerV3
   codebook) -> MECH-437 + MECH-438 registered candidate/substrate_conditional/
   generation:v4, wired into the arc_062 cluster (landed master dcca2cb).
3. [DONE 2026-06-19] Re-activate the handoff pipeline with the first targeted
   packets (end-to-end loop validated on three real stuck nodes -- CDQ-001/002/003
   -- before scaling). All three June packets re-validated gate-ready; receipts
   CRCT-RULE-DISTINGUISHABILITY / -TONIC-EXPLORATION-NOISE / -QUALITY-DIVERSITY-20260619
   authored (decision_ref `evidence/decisions/convergence_packet_adjudication_2026-06-19.md`)
   and mirrored back to `REE_convergence/handoff/packets/receipts/` via
   `run_cross_repo_handoff.py` -- the first batch since 2026-02-24. Direct
   `claims.yaml` registration superseded the tool register step; the receipts are
   acknowledgment lineage only and promote nothing.
