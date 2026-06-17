# Convergence Demand Pipeline -- closure-driven external-inspiration intake

Status: ACTIVE (plan of record)
Created: 2026-06-17T15:11:59Z
Activated: 2026-06-17T17:24:56Z (First Action #1 landed)
Owner workstream: REE_convergence -> REE_assembly handoff
Generation: meta/process (NOT a v3 closure node -- intentionally carries no
`closure_plan` frontmatter so it does not enter the closure progress denominator)

> This is a process plan, not a v3 closure node. It describes how external
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
| `arc_062_rule_apprehension:GAP-B`, `:GAP-K`; `behavioral_diversity_isolation:GAP-B` | Minted rules must stay mutually distinguishable to remain selectable (CRF conflict-gate lockout: theta=0.15+0.25*(n_matched-1) gates out 7-8 co-matching rules) | **DreamCoder** (wake-sleep library abstraction; minted programs stay distinguishable to be selectable) + **DreamerV3 discrete latent codebook** (categorical keys separable by construction) | DreamCoder NEW; DreamerV3 PARTIAL (`sources/dreamer-v3/`, extend codebook angle) | HIGH (in flight: chip task_88e97a80) |
| `behavioral_diversity_isolation:GAP-C`; `arc_062_rule_apprehension:GAP-H` | Tonic, state-conditioned exploration noise floor (MECH-313 LC-NE analog) -- distinct from a fixed epsilon schedule | **NoisyNet** (learned per-parameter, self-annealing, state-dependent noise); secondary **RND / Plan2Explore** (model-disagreement curiosity = MECH-314) | NEW | MED |
| `behavioral_diversity_isolation:GAP-B` (conversion-to-committed-action) | Diversity must be maintained in a structure that survives the selection/commit step | **Quality-Diversity / MAP-Elites** (Cully et al. 2015: explicit behavioral-descriptor archive surviving selection) -- structurally the top-k shortlist fix already validated by V3-EXQ-569i | NEW | MED |
| `sd_037_axis_b:P1b` -> `P2`/`P3`/`P4` | Automatic curriculum that keeps a target signal (z_harm_a sustained-threat window) in a learnable band | **PLR / Prioritized Level Replay** + **POET**; affective framing: active-avoidance / anxiety-as-pessimistic-prior RL | NEW | LOW (P1b in flight via V3-EXQ-625d; intake feeds the axis-(c) escalation only if 625d exhausts the env-kwarg surface) |
| `arc_062_rule_apprehension:GAP-K` (replay write-gating) | Gating which replayed/imagined transitions may write to the rule layer | **MuZero/EfficientZero reanalyze** + hippocampal SWR prioritized replay | MuZero COMPLETED (`sources/muzero/`) -- pull the adapter through to a registered claim | LOW |

Maintained alongside this doc as a structured file: `convergence_demand_queue.v1.json`
(created by the first progress chip; mirrors this table for tooling).

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
2. Execute the HIGH-priority row (DreamCoder + DreamerV3 codebook) -- already
   spawned as chip task_88e97a80.
3. Re-activate the handoff pipeline with that first targeted packet (validates
   the end-to-end loop on a real stuck node before scaling to the MED rows).
