---
closure_plan:
  id: zworld_adequacy
  title: "observation -> z_world encoding adequacy (the V3 binding-constraint interface)"
  generation: v3
  registered: 2026-09-11
  last_updated: 2026-09-11
  scope_claims: [INV-088, MECH-457, SD-015, ARC-030, MECH-117, ARC-065]
  sibling_plans: [goal_pipeline, conversion_ceiling_campaign, ree_ai_design_critique]
  related_threads:
    - "cross_plan_root_cause_synthesis_20260902.md -- the synthesis that named this interface the binding constraint (39 of 43 remaining nodes chain to it)"
    - "substrate_queue.json SD-106 (the live build) and SD-018 (predecessor shape (a), VALIDATED-NEGATIVE)"
    - "hypothesis_space_registry.v1.json question `zworld_actor_adequacy_locus` (alive 0, H-F confirmed)"
  registered_note: >
    NEW plan doc (session jolly-neumann-a8857e, 2026-09-11,
    chip-20260911-zworld-adequacy-closure-owner). Closes a closure-map ownership
    gap surfaced by /governance gov-20260911 -- GOV-DIAG-1
    (scripts/check_diagnostic_chain_recurrence.py) fired two ACTIONABLE
    recurrences, bears_on tokens INV-088 and MECH-457, both at N=3 on ONE
    pure-diagnostic chain (V3-EXQ-1002 -> 1008 -> 1010). The user adjudicated
    that chain CONVERGED, not mis-posed -- the counter keys on
    non_contributory/inconclusive and a claim-free diagnostic scores
    non_contributory BY CONSTRUCTION however decisively it resolves, and this
    chain terminated in a confirmed mechanism (H-F-content-discarded-at-encode),
    a named repair site, and a routed build (SD-106). The prescribed way to stop
    a metabolized chain re-firing is a hit-scoped
    `diagnostic_recurrence_metabolized` marker on the OWNING closure_plan node
    (/governance skill 6a-v-ter). THAT MARKER HAD NO HOME -- no node anywhere
    owned this chain, so the recurrence would have re-fired every governance
    cycle forever, which is precisely the alarm-fatigue failure mode the rule
    itself names as a Goodhart vector.
  registration_decision_note: >
    OWN PLAN rather than a node on an existing plan. Evidence for the decision,
    recorded because the chip asked for it either way. (1) Every plan whose
    closure_plan nodes touch INV-088 / MECH-457 / SD-018 was enumerated
    mechanically (parse every evidence/planning/*_plan.md frontmatter, match
    node.unblocks_claims against INV-088, MECH-457, SD-018, SD-106, SD-015,
    ARC-030, MECH-117, ARC-065). Eight nodes matched, across five plans --
    arc_062_rule_apprehension GAP-H, behavioral_diversity_isolation GAP-A/GAP-B,
    goal_pipeline GAP-2/GAP-4/GAP-7, infant_substrate GAP-2/GAP-12. Every match
    was on the DOWNSTREAM claims (ARC-065 / ARC-030 / MECH-117 / SD-015), never
    on the interface itself; none mentions the encoder, and six of the eight are
    already `done`. (2) The nearest candidate, goal_pipeline:GAP-2, is
    "SD-049 Phase 2 hybrid encoder behavioural validation", status `done`, closed
    on the V3-EXQ-514o PASS -- its SD-015 / MECH-117 / ARC-030 overlap with this
    interface is incidental and re-opening a node closed on an unrelated PASS to
    host this chain would corrupt that closure record. (3) The positive ground:
    this interface is not a sub-item of any one plan -- the 2026-09-02 cross-plan
    synthesis found 39 of 43 remaining V3 nodes chain TO it, so its correct
    closure-map shape is a target that many plans cross_plan_link INTO, which is
    a plan, not a node buried inside one of its own dependents. SCOPE HELD
    DELIBERATELY NARROW: this plan owns the ENCODING half (observation ->
    z_world). The downstream rollout half (z_world -> E1/E2, the SD-e1 ITEM 2
    validation run that the same synthesis names as the other unowned
    critical-path item) is NOT claimed here -- it is a different substrate entry
    on a thread this registration did not verify, and inventing a node for it
    would be exactly the confident-but-wrong ownership this plan exists to fix.
    It is recorded in the body as explicitly-unowned so the next governance cycle
    can see it. NO claims.yaml edits were made by this registration -- every
    claim's status / implementation_phase is unchanged; this is closure-map
    registration only, not a promotion, demotion, or build authorisation.
  nodes:
    - id: "zworld_adequacy:ZW-1"
      title: "observation -> z_world preserves decision-relevant content (SD-106 generic bottleneck variance preservation)"
      phase: 1
      status: assembling
      awaiting: SD-106
      assembly_status: queued
      revisit_after: 2026-10-15
      severity: high
      owner_exq: V3-EXQ-1010
      unblocks_claims: ["INV-088", "MECH-457", "SD-015", "ARC-030", "MECH-117", "ARC-065"]
      depends_on: []
      cross_plan_link: ["goal_pipeline:GAP-2", "ree_ai_design_critique:WS-1"]
      last_updated: 2026-09-11
      blocking_on: >
        The SD-106 build (substrate_queue.json, status pending_implementation,
        ready true, priority 1, node_class "complicated (buildable)"). Nothing
        upstream of it is unresolved -- depends_on_unresolved is empty and the
        measurement harness already exists -- so this node is
        awaiting_construction, not probe-gated.
      what_is_established: >
        The three-run diagnostic chain resolved the locus. V3-EXQ-1010's
        over-capacity decoder sweep put five decoder rungs spanning about
        77,000x in parameters on SD-018's OFF-arm frozen latent -- best held-out
        oracle-action agreement 0.6839 / 0.6846 / 0.6656, 0 of 3 seeds clearing
        the 0.80 bar -- while the SAME ladder on the SAME latent memorises the
        training split at 0.9996-0.9998, and a PCA-32 of the encoder's own
        250-dim input AT THE ENCODER'S OWN 32-dim WIDTH clears 3 of 3 at
        0.8836 / 0.8729 / 0.8763. The same architecture at RANDOM INITIALISATION
        scores 0.7155 / 0.6895 / 0.7084 -- at or above the trained latent on
        3 of 3 seeds. So the binding problem is NOT width (PCA-32 at the same
        width clears it), NOT consumer capacity (no decoder up to 12.67M
        parameters recovers it), and NOT consumer learning (H-B eliminated at
        V3-EXQ-1002). It is that the observation -> z_world objective supplies NO
        GRADIENT toward decision-relevant content, leaving the latent at or below
        its own random-initialisation quality. Frozen-ledger question
        `zworld_actor_adequacy_locus` now reads alive 0, with
        H-F-content-discarded-at-encode CONFIRMED (confirmed but not exclusive --
        H-C's split already attributes part of the gap to geometry).
      resume_condition: >
        Node closes when the observation -> z_world latent reaches PCA-32 parity
        at the consumer rung -- at least 0.85 held-out oracle-action agreement at
        x734.PPOPolicyNet / PPO_TRUNK_HIDDEN on a SEED MAJORITY -- re-measured by
        re-running experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py
        UNCHANGED after SD-106 lands. The harness, the dataset recipe, the
        PCA-32 anchor and the random-init negative control all already exist and
        need no new build, so this is a re-run and not a new /queue-experiment
        design. Advance owner_exq to the re-run's run_id at that point. If the
        re-run MISSES the bar with SD-106 correctly implemented, that is a
        pre-registered refutation of the generic-preservation shape, not a
        reason for a third encoder shape -- route it to /failure-autopsy and
        re-open ZW-2's hold on the record there.
      governance_2026_09_11: >
        Node registered (closure-map ownership only). Case 3 in closure-drift
        terms while SD-106 is unbuilt -- owner_exq V3-EXQ-1010 has reached a
        terminal state (confirmed autopsy, non_contributory) but the closure it
        gates is a substrate build, not a further experiment, so the node is
        legitimately non-terminal. Recorded explicitly even though the
        `assembling` status already exempts it from the drift passes, so the
        judgement survives a later status change.
      diagnostic_recurrence_metabolized:
        date: 2026-09-11
        metabolized_hits:
          - v3_exq_1002_zworld_actor_adequacy_oracle_adapter_20260905T005017Z_v3
          - v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis_20260907T233826Z_v3
          - v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3
        covers_tokens:
          - INV-088
          - MECH-457
        note: >
          CONVERGED, NOT MIS-POSED -- user adjudication, /governance gov-20260911.
          GOV-DIAG-1's reading ("the question may be mis-posed, not
          under-powered") does not apply to this chain, and the reason is a known
          property of the counter rather than a judgement call- it keys on
          recommended_evidence_direction in {non_contributory, inconclusive}, and
          a claim-free diagnostic (claim_ids []) scores non_contributory BY
          CONSTRUCTION however decisively it resolves its fork. This chain
          resolved: 1002 eliminated H-B (consumer learning) with a
          capacity-matched frozen-latent oracle-adapter probe; 1008 split H-C and
          eliminated its linear child, which WITHDREW one of the two independent
          grounds holding SD-018 shape (b); 1010 confirmed
          H-F-content-discarded-at-encode against an in-run PCA-32 control and a
          random-init negative control, taking the frozen ledger question
          `zworld_actor_adequacy_locus` to alive 0. The prescribed response was
          carried out in full- the mechanism was named, the repair site was
          named (the observation -> z_world objective, not the decoder and not
          the width), the build was ROUTED and MINTED as SD-106 with a numeric
          acceptance target set by an in-run control, and the same-question
          re-queue was refused in the re-derive brake's spirit (the layer-wise
          decode profile is recorded as a legitimate LATER refinement, not the
          cheapest next step). The exclusion is hit-scoped, as designed- a NEW
          diagnostic chain later circling INV-088 or MECH-457 can still
          re-accumulate to N and fire.
    - id: "zworld_adequacy:ZW-2"
      title: "SD-018 shape (b) raw-field side-channel -- HELD as a bypass of the interface, not a repair"
      phase: 1
      status: upstream_blocked
      severity: medium
      owner_exq: null
      unblocks_claims: ["SD-015", "ARC-030", "MECH-117"]
      depends_on: ["zworld_adequacy:ZW-1"]
      cross_plan_link: []
      last_updated: 2026-09-11
      blocking_on: >
        Held by decision, on ONE surviving ground, pending ZW-1. SD-018 shape (a)
        (supervise one named feature, resource proximity) is
        VALIDATED-NEGATIVE- V3-EXQ-978 trained the directional head, found
        z_world already decodes the field (OFF r2 0.71 sense / 0.86 encoder), and
        behaviour sat at or below random walk in BOTH arms. Shape (b)
        (side-channel the raw field past z_world) is known to be a large
        PERFORMANCE lever- the raw-field arm reaches 0.979 agreement and 51.5
        cloned res/ep against z_world's 0.664 and 16.9. It was held on two
        independent grounds; V3-EXQ-1008's H-C split WITHDREW ground (i) (the
        predecessor's H-C condition). Ground (ii) stands alone and still holds
        the build- shape (b) BYPASSES the observation -> z_world interface rather
        than repairing it, and that interface is the V3 binding constraint, so
        promoting it would bank exactly the confident-but-wrong localisation
        GOV-FANOUT-1 exists to prevent. This node exists so that a
        single-grounded hold on a known performance lever is VISIBLE on the
        closure map with its reversal condition attached, instead of living only
        in a substrate_queue governance note.
      resume_condition: >
        Do NOT build shape (b) while ZW-1 is open. Revisit only on one of two
        triggers- (a) ZW-1 closes, at which point shape (b) is moot because the
        interface itself carries the content; or (b) SD-106 lands correctly and
        the unchanged V3-EXQ-1010 re-run still misses the 0.85 bar on a seed
        majority, which refutes generic-preservation and makes the
        bypass-vs-repair trade a live governance question again rather than a
        settled hold. Either way the decision is /governance's, not an
        /implement-substrate session's- ground (ii) is an explicit override of
        the design doc's own fallback rule and must be reversed on the record.
      governance_2026_09_11: >
        Node registered (closure-map ownership only). Case 3 in closure-drift
        terms- legitimately non-terminal pending the upstream ZW-1 build, with no
        owner_exq because the held decision is not owned by any experiment.
---

# observation -> z_world encoding adequacy (V3 binding constraint)

**Registered 2026-09-11** (session `jolly-neumann-a8857e`,
`chip-20260911-zworld-adequacy-closure-owner`). Closure-map registration only --
no claim status changed, no build authorised.

## Why this plan exists

Two separate things converged on the same missing object.

**1. A metabolized diagnostic chain had nowhere to record that it was
metabolized.** `/governance` gov-20260911 ran GOV-DIAG-1
(`scripts/check_diagnostic_chain_recurrence.py`) and got two ACTIONABLE
recurrences -- `bears_on` tokens `INV-088` and `MECH-457`, both at N=3 on one
chain:

```
v3_exq_1002_zworld_actor_adequacy_oracle_adapter_20260905T005017Z_v3
  -> v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis_20260907T233826Z_v3
    -> v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3
```

The user adjudicated it CONVERGED rather than mis-posed. The prescribed way to
stop a metabolized chain re-firing is a hit-scoped
`diagnostic_recurrence_metabolized` marker on the **owning** closure-plan node.
There was no owning node, so the marker could not be placed and the audit would
have re-fired both tokens every cycle -- the alarm-fatigue Goodhart vector that
GOV-DIAG-1's own design notes name.

**2. The interface itself was unowned.** The 2026-09-02 cross-plan root-cause
synthesis found that **39 of 43 remaining V3 closure nodes chain to the
observation -> z_world -> E1/E2 interface**. The encoding half of that interface
appeared in no plan's `closure_plan` frontmatter at all.

## What the chain established

| eliminated | how |
|---|---|
| H-B, consumer learning | V3-EXQ-1002, capacity-matched frozen-latent oracle-adapter probe |
| H-C linear child | V3-EXQ-1008 portfolio re-basis (split H-C; withdrew one of the two grounds holding SD-018 shape (b)) |
| width | PCA-32 of the encoder's own 250-dim input, at the encoder's own 32-dim width, clears the bar 3/3 (0.8836 / 0.8729 / 0.8763) |
| consumer capacity | no decoder rung up to 12.67M parameters recovers it (~77,000x sweep) |

What survives is **H-F-content-discarded-at-encode**, CONFIRMED (not exclusive --
H-C's split still attributes part of the gap to geometry). The trained latent
scores **at or below its own random initialisation** on 3/3 seeds
(0.6839/0.6846/0.6656 trained vs 0.7155/0.6895/0.7084 random-init), while the
same ladder memorises the training split at 0.9996-0.9998. The
observation -> z_world objective supplies no gradient toward decision-relevant
content.

Frozen-ledger question `zworld_actor_adequacy_locus` now reads `alive: 0`.

## The live front

**SD-106** -- `encoder.generic_bottleneck_variance_preservation`, the successor
shape to SD-018. `pending_implementation`, `ready: true`, priority 1,
`complicated (buildable)`, `depends_on_unresolved: []`. Minted by gov-20260911
as a NEW `sd_id` rather than a third SD-018 shape, on the reasoning that a
named-feature entry which returned NULL should not absorb evidence for a
different mechanism.

**Acceptance target (ZW-1's closure condition):** the observation -> z_world
latent reaches PCA-32 parity at the consumer rung -- **>= 0.85 held-out
oracle-action agreement** at `x734.PPOPolicyNet` / `PPO_TRUNK_HIDDEN` on a
**seed majority** -- re-measured by re-running
`experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py` **unchanged**.
The harness, dataset recipe, PCA-32 anchor and random-init negative control all
already exist; this is a re-run, not a new experiment design.

## Deliberately NOT owned here

The **rollout half** of the binding-constraint interface -- `z_world` -> E1/E2,
including the SD-e1 ITEM 2 validation run that the 2026-09-02 synthesis names as
the *other* unowned critical-path item -- is **not claimed by this plan**. It is
a different substrate entry on a thread this registration did not verify, and
inventing a node for it would be the same confident-but-wrong ownership this
plan exists to fix. It is recorded here so the next governance cycle can see
that it is still unowned and route it deliberately.

The **layer-wise decode profile** (localise *where* along the path the content is
lost) is a legitimate later refinement, explicitly **not** refused by the
re-derive brake -- it is simply not the cheapest next step, because the dominant
missing term is a pressure absent *everywhere* along the path rather than a loss
at one point in it.

## Decision log

- **2026-09-11** -- plan registered; ZW-1 and ZW-2 created; hit-scoped
  `diagnostic_recurrence_metabolized` marker placed on ZW-1 covering the three
  chain run_ids and the tokens `INV-088` / `MECH-457`. Own plan rather than a
  node on an existing plan; the enumeration behind that decision is in
  `registration_decision_note` above. No `claims.yaml` edits.
