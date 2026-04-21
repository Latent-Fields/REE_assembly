# SD-033 Governance Plan

**Registered:** 2026-04-20
**Status:** active
**Scope:** translate the 2026-04-20 GAP MEMO + OCD thought set into claims, lit-pulls, and an EXQ test battery that together close the "governance layer inert" gap identified in the memo.

---

## One-line framing

> REE-V3 is not missing cognition. It is missing governance.
> -- 2026-04-20_analysis_of_missing_pieces_and_work_to_do.md

Operating-mode signals already exist (SD-032a SalienceCoordinator, dACC bundle, MECH-261 write-gate registry). The basal-ganglia-like gate substrate already exists (BetaGate MECH-090, MECH-260 action-class suppression, MECH-091 urgency interrupt). What is missing is (a) a trained SD-033a bias pathway, (b) a closure operator that turns evaluation off, (c) explicit mode hysteresis, (d) mode-conditioning of hippocampal proposals, and (e) dACC conflict saturation. This plan registers the missing claims, queues lit-pulls, and queues the OCD-mapped test battery that falsifies them.

## Source thoughts

Provenance for every claim registered under this plan:

| Thought file | Role |
|---|---|
| [docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md](../../docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md) | GAP MEMO - identifies governance as the missing layer |
| [docs/thoughts/2026-04-20_modes.md](../../docs/thoughts/2026-04-20_modes.md) | Six-step mode-binding implementation sketch |
| [docs/thoughts/2026-04-20_ocd1.md](../../docs/thoughts/2026-04-20_ocd1.md) | OCD as mode-governance failure; four constraints on closure |
| [docs/thoughts/2026-04-20_ocd2.md](../../docs/thoughts/2026-04-20_ocd2.md) | (supplementary OCD intake) |
| [docs/thoughts/2026-04-20_ocd3.md](../../docs/thoughts/2026-04-20_ocd3.md) | Eight OCD subtypes mapped to control-plane failures (test-battery source) |
| [docs/thoughts/2026-04-20_ocd4.md](../../docs/thoughts/2026-04-20_ocd4.md) | SD-033 as Go/Hold/No-Go gating substrate; explicit SD-033 test matrix |

## Existing substrate (not to be duplicated)

| OCD-memo function | Already implemented | Location |
|---|---|---|
| Hold (bistable commitment latch) | MECH-090 bistable BetaGate + ARC-028/MECH-105 hippocampal completion release | `ree-v3/ree_core/heartbeat/beta_gate.py`, `ree_core/agent.py` |
| No-Go (recency-bias suppression over action classes) | MECH-260 `DACCAdaptiveControl._action_history` | `ree-v3/ree_core/cingulate/dacc.py` |
| Mode register with hysteresis (Schmitt-trigger on aggregate) | SD-032a SalienceCoordinator (enter-only) | `ree-v3/ree_core/cingulate/salience_coordinator.py` |
| Write gating per mode | MECH-261 dict-keyed registry | same |
| Urgency interrupt (hyperdirect analog) | MECH-091 z_harm_a-triggered beta release | `ree-v3/ree_core/agent.py` |
| Descending modulation gate | SD-032c AICAnalog `harm_s_gain` | `ree-v3/ree_core/cingulate/aic_analog.py` |
| Rule/goal bias (scaffolded, inert) | SD-033a LateralPFCAnalog with zeroed last-Linear bias head | `ree-v3/ree_core/pfc/lateral_pfc_analog.py` |

The OCD thoughts are wiring instructions for this substrate, not a mandate to build new gate machinery.

## Claim registrations

All four are registered 2026-04-20 with `status: candidate`, `implementation_phase: v3`, `v3_pending: true`, and an `evidence_quality_note` pointing back to this plan and the source thoughts.

| ID | Name | Instantiates / depends on |
|---|---|---|
| **SD-034** | `governance.closure_operator` - "done" token that binds beta release, temporary No-Go on the just-completed rule_state, and residue discharge within the relevant domain | SD-033, MECH-090, MECH-260, MECH-094 |
| **MECH-266** | `salience.asymmetric_mode_hysteresis` - distinct enter vs exit thresholds per operating mode (ocd2 step 2) | SD-032a, MECH-259 |
| **MECH-267** | `hippocampal.mode_conditioned_proposals` - HippocampalModule.propose_trajectories conditioned on operating_mode in addition to world_state (ocd2 step 4) | SD-004, SD-032a, MECH-261 |
| **MECH-268** | `dacc.conflict_saturation` - dACC `pe` signal caps / habituates under repeated identical outcomes (ocd1 constraint 4) | SD-032b, MECH-258, MECH-260 |

## Lit-pull backlog

Each task is captured as a `- [ ] Lit-pull (...)` entry in [evidence/planning/task_inbox.md](./task_inbox.md); each entry closes with "On completion, revisit `evidence/planning/sd033_governance_plan.md`." so the plan is the surfacing point when the biology lands.

| Pull | Grounds |
|---|---|
| Closure operator biology | SD-034; OFC/ACC sequence-completion cells (Rich & Shapiro 2009; Schuck 2016); post-completion refractory period on re-entry; task-set disengagement (Collins & Frank 2014) |
| Asymmetric mode hysteresis biology | MECH-266; BG direct/indirect pathway asymmetries; tonic DA hysteresis (Cools 2008; Collins & Frank 2014); Schmitt-trigger biology in decision thresholds |
| Mode-conditioned hippocampal proposals | MECH-267; state-dependent replay content (Pfeiffer & Foster 2013; Olafsdottir 2018); goal-directed replay bias; task-set-conditioned replay |
| dACC conflict saturation | MECH-268; habituation of dACC error signals (Bryden 2019); EVC saturation dynamics (Shenhav 2016); repeated-identical-outcome adaptation |

## SD-033 test battery (ocd4 table)

Nine experiment proposals, one per ocd4 row. Registered as EXP entries in
`REE_assembly/evidence/planning/manual_proposals.v1.json` (status `queued`,
target_repo `ree-v3`). They do NOT go into `ree-v3/experiment_queue.json`
yet -- SD-034, MECH-266, MECH-267, and MECH-268 are candidate / v3_pending
and the substrate extensions under each proposal's prerequisites are not
yet implemented. When the substrate lands, the proposals become script-
authoring work items; reserved queue slots V3-EXQ-460..468 are assigned to
the matching scripts at that time.

| ocd4 test | Failure probed | Primary claims tagged | Proposal | Reserved queue slot |
|---|---|---|---|---|
| Verified-but-not-released | No-Go - closure missing | SD-034, MECH-260, MECH-261 | EXP-0156 | V3-EXQ-460 |
| Delayed-reward persistence | Hold - goal-field maintenance | MECH-090, SD-033a, SD-034 | EXP-0157 | V3-EXQ-461 |
| Rule binding | Go + Hold - rule install and persist | SD-033a, MECH-262, MECH-267 | EXP-0158 | V3-EXQ-462 |
| Conflict saturation | dACC pe capping | MECH-268, SD-032b, MECH-258 | EXP-0159 | V3-EXQ-463 |
| Competing goals | lateral inhibition in Go selection | MECH-266, SD-032a, MECH-259 | EXP-0160 | V3-EXQ-464 |
| Intrusive simulation filtering | MECH-094 hypothesis-tag isolation under OCD-like pressure | MECH-094, MECH-261, MECH-267 | EXP-0161 | V3-EXQ-465 |
| Satisficing (No-Go thresholding) | residue discharge under sufficient action | SD-034, MECH-094 | EXP-0162 | V3-EXQ-466 |
| Mode stickiness (Hold decay) | asymmetric enter vs exit thresholds | MECH-266, SD-032a | EXP-0163 | V3-EXQ-467 |
| Commitment vs contradiction | adaptive gate thresholds under counter-evidence | SD-034, MECH-268, MECH-090 | EXP-0164 | V3-EXQ-468 |

Each proposal's `prerequisites` field lists the substrate that must be
implemented before the script can be authored and queued. Several
prerequisites (e.g. `ResidueField.discharge_domain()`, counter-evidence
injection hooks, competing-goals env variant) are env / API extensions
not yet on any roadmap item -- surfacing those in the proposals gives the
next substrate-implementation session explicit work to route.

When ready to author scripts, cross-reference each EXP against its
reserved V3-EXQ slot and refer back to this plan doc plus the ocd4 thought
file for acceptance criteria.

## OCD failure-mode axis and REE axis

From ocd4:

```
under-binding  <->  over-binding
(depression)       (OCD / rigidity)
```

This plan targets the OCD side of the axis by name, but the same substrate landing enables the depression-side tests (Go failure, insufficient Hold). Those are deferred until closure-operator evidence is in.

## Status checklist

- [x] Anchor doc created (this file)
- [x] Auto-memory entry `project_sd033_governance_plan.md` written; `MEMORY.md` pointer added
- [x] task_inbox.md entries added (4 lit-pulls)
- [x] SD-034 registered in claims.yaml
- [x] MECH-266/267/268 registered in claims.yaml
- [x] claims.json rebuilt (2026-04-20: 518 claims, 68 invariants OK)
- [x] 9 EXP proposals registered in manual_proposals.v1.json (EXP-0156..0164; V3-EXQ-460..468 reserved)
- [x] SD-034 closure operator implemented 2026-04-20 (ree_core/governance/closure_operator.py); EXP-0156/0162 scripts authored (V3-EXQ-460, V3-EXQ-466) and queued; all landing sub-tests PASS; contracts regression suite green (24/24)
- [x] MECH-267 mode-conditioned hippocampal proposals implemented 2026-04-20 (ree_core/hippocampal/module.py operating_mode parameter + ree_core/utils/config.py HippocampalConfig.mode_conditioning_enabled + per-mode CEM-noise multipliers); EXP-0158/0161 scripts authored (V3-EXQ-462, V3-EXQ-465) as substrate-landing diagnostics; all 10/10 sub-tests PASS on smoke; behavioural successors deferred pending EXP-0155 (cue_action_proj diagnostic) and forced-replay injection hook respectively
- [x] MECH-268 dACC conflict saturation implemented 2026-04-20 (ree_core/cingulate/dacc.py f_sat = 1.0 / (1.0 + strength * max(0, n_rec - grace)) over FIFO outcome history; ClosureOperator wired to call dacc.reset_outcome_history(); REEConfig.from_dims wired with 4 saturation knobs + closure_reset_outcome_history); EXP-0159 (V3-EXQ-463, 7 sub-tests) and EXP-0164 (V3-EXQ-468, 6 sub-tests, 4-arm A/B/C/D interaction) authored as substrate-landing diagnostics; all 13/13 sub-tests PASS on smoke; behavioural arms (500+ step sustained outcome / counter-evidence injection) deferred -- need env extensions not on roadmap
- [ ] REE_assembly + ree-v3 pushed
- [ ] WORKSPACE_STATE Recent Work entry added
- [ ] TASK_CLAIMS closed as done

## EXQ-script authoring gated on substrate

The 9 V3-EXQ-460..468 scripts are NOT written yet. Each EXP proposal
lists the specific substrate / API extensions blocking it. Start-here
order when picking this back up:

1. SD-034 closure operator implementation (highest leverage -- unblocks
   EXP-0156, EXP-0157, EXP-0162, EXP-0164).
2. MECH-266 asymmetric hysteresis extension to SalienceCoordinator
   (unblocks EXP-0160, EXP-0163).
3. ~~MECH-267 mode-conditioned proposals on HippocampalModule~~
   IMPLEMENTED 2026-04-20. EXP-0158 (V3-EXQ-462) and EXP-0161
   (V3-EXQ-465) authored as substrate-landing diagnostics and smoke-
   tested PASS. Full behavioural successors still blocked on
   EXP-0155 (cue_action_proj forward-path diagnostic) and a
   forced-replay injection hook respectively.
4. ~~MECH-268 dACC pe saturation in DACCAdaptiveControl~~
   IMPLEMENTED 2026-04-20. EXP-0159 (V3-EXQ-463) and EXP-0164
   (V3-EXQ-468) authored as substrate-landing diagnostics and smoke-
   tested PASS (13/13 sub-tests). Closure operator threads
   reset_outcome_history flag; ClosureEvent.outcome_history_reset
   stamps the reset. Behavioural arms (500+ step sustained outcome /
   counter-evidence injection) deferred -- env extensions not yet
   on roadmap.

Each proposal's `prerequisites` field is the punch list.

## When to revisit

- Each `- [ ] Lit-pull (...)` entry in task_inbox.md closes with a pointer to this doc.
- Governance cycles that surface one of {SD-034, MECH-266, MECH-267, MECH-268} will see their `evidence_quality_note` cite this plan.
- Each EXQ script's docstring and queue `title` reference the ocd4 row and this plan.
- `MEMORY.md` lists `project_sd033_governance_plan.md` as a permanent pointer.

If the plan mutates mid-implementation, this file is the single source of truth - update here, every other view follows.
