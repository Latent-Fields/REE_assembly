# Unwritten prerequisite discovery: design and prospective pilot

Protocol frozen: 2026-09-20T19:22:13Z. Owner: codex-20260920-unwritten-edge-discovery.
Chip: chip-20260920-unwritten-edge-discovery-skill. The user explicitly authorized
completion in Codex after the initial account/Fable stop-check; no account was changed.

## Question and boundary

Can a bounded audit of high-leverage V3 closure nodes find genuinely unregistered
prerequisites with enough precision to justify a standing `/unwritten-edges` skill?
An unresolved registered prerequisite is backlog, not a discovery. An unwritten
edge often terminates at an unwritten node, but this is a hypothesis, not a theorem:
two existing nodes can still lack the right connection, and gate prose can be stale.
Report those separately. Do not search for a new inferential `supports` edge layer.
The negative measurement in `claims_edge_type_split_20260904.md` section 8 stands.

Search two boundaries: registry to executable substrate, and current closure to
future roadmap. A dependency must name a function needed by a falsifier, an absent
provider, a consequence that can be tested, and an owner/registration route. A
plausible architecture idea without that chain is discarded.

## Pre-registered evaluation (before detector output or node adjudication)

Select EIGHT unfinished V3 nodes in deterministic leverage order. Include assembly
frontier nodes in ranking, but respect their intentional construction state; do
not turn `assembling` into failure. Exclude done, closed, parked and deferred nodes.
Rank lexicographically by (1) number of distinct transitive downstream V3 closure
nodes, (2) number of distinct downstream claims in the claims prerequisite DAG
seeded by the node and its closure descendants' `unblocks_claims`, (3) literal live
front match, (4) number of claims whose `what_would_answer` explicitly names this
node or its directly unblocked claim IDs. Final tie break: full node ID ascending.
Use explicit `depends_on` only for graph reachability; `cross_plan_link`, coupling,
scope-claim lists and prose mentions are NOT prerequisite edges. Record unresolved
references instead of inventing graph connections. Report all four rank components.
This conservative ranking can undercount prose-only shared roots; that limitation
is part of the measurement, not permission to hand-pick interesting cases.

Apply the re-pose check to all eight before enumerating machinery. A matching open
re-pose flag, GOV-FROZEN-1 fan-out recurrence, or explicit prohibition on a new
portfolio stops that question's enumeration. Record the existing route; do not
duplicate its flag. A stop remains in the eight-node sample, with zero nominations.
Do not replace stopped or unproductive nodes with more promising ones.

Unit of nomination = distinct proposed missing function/artefact at a specific
interface, not every keyword hit. Merge duplicate detector hits and cross-node
instances before counting. Preserve raw hits and the merge map. Every bounded
pilot hit is adjudicated, including obvious false positives; do not remove already
registered items from the denominator after seeing their status. Global detector
counts are calibration, not the pilot denominator. The known MECH-092 case is a
separate positive control, excluded from precision and any held-out skill check.

Let N be distinct pilot nominations and U those verified to need a NEW registered
node. Report precision U/N, node yield, reasons for rejection, detector yield,
existing-node edge repairs, and re-pose stops separately. A flag about stale prose
does not become an unwritten-node hit. Unresolved nominations count as non-hits for
shipping and remain explicit; uncertainty must not improve precision.

**Do not ship a skill if U/N < 0.50, N < 5, U < 3, or the new nodes arise from fewer
than two selected closure nodes.** All conditions must pass. N=0 is insufficient
evidence, not perfect precision. These are practical pilot thresholds, not a claim
of population accuracy; eight leverage-selected nodes are not a random sample.
Report a Wilson interval as a descriptive uncertainty bound only. Do not revise
the threshold after seeing results. A positive pilot additionally requires at
least three non-degenerate GOV-HELDOUT-1 historical checks on cases not used to
write the wording. MECH-092 cannot count. No skill is written before adjudication.

## Stage 0b: stop before enumeration

Read `docs/CURRENT_FRONT.md`, the owning plan's current fields, matching hypothesis
space entries and open governance flags. Resolve which QUESTION a gate belongs to:
sharing an upstream re-pose does not prohibit auditing an independent downstream
instrument, but it DOES prohibit inventing another remedy for the frozen question.
Record that distinction explicitly. Respect assembly-vs-closure and existing
`revisit_after` gates. No fifth portfolio on `zworld_actor_adequacy_locus` while its
re-pose prohibition remains live (GFLAG-0312 and successors).

## Stage 1: cheap nominations, manual verdicts

Only extraction, ranking, source-location and simple syntax scans are scripted.
No script decides necessity, scientific adequacy, absence, or a new registration.

- **D1 producer / consumer:** syntax-scan `ree_core` for assigned names without a
  load in the same function. Trace nominated paths by hand through callers,
  attribute writes, returned values and side effects. An ignored return can still
  perform useful work. For each relevant representation record who reads it and
  the smallest content-shuffle intervention and DV that could expose its causal
  contribution. Absence of a shuffle test is a measurement gap, not proof that
  content has no effect or a new substrate component is required.
- **D2 stale gate:** extract exact claim, substrate and closure IDs from current
  gate fields; join live status with source provenance. Completion of a parent
  does not prove completion of every phase or clearance of its validation gate.
  Historical prose and positive statements of completed prerequisites are common
  false positives. Completed-node references nominate a check, not a conclusion.
- **D3 absent-artefact prose:** case-insensitive phrases `does not exist`,
  `no consumer`, `never read`, `not yet built`, `must be built`, `no instrument`,
  plus spacing/hyphen variants. Run across all claims without seeding MECH-092.
  Require that the positive control is recovered. Wider phrases may be reported
  separately, never quietly substituted to improve the outcome.
- **D4 terminal blocked:** inspect not-complete substrate entries with an explicit
  empty `depends_on_unresolved`, and unfinished closure nodes with no explicit
  dependency. Missing field is distinct from empty list. Substrate status is free
  prose: normalize exact simple tokens and unambiguous leading completion tokens,
  retain raw text, classify ambiguous/qualified statuses as unknown. `implemented`
  plus an owed retest is not an unwritten build. A terminal executable task can
  legitimately have no dependencies.
- **D5 missing instrument:** from the actual falsifier extract named DVs and look
  for recorder/metric/manifest producers and consumers. Search results alone cannot
  establish semantic absence: trace aliases, derived metrics and driver-local
  instruments. Record paths/lines and the search scope, including experiments.
- **D6 measurement deferral:** extract prose mentions, then manually distinguish
  deferral-of-measurement from background, historical and inferential citations.
  Report genuine cycles/common absent sinks; keep this a report, not a new edge
  type. MECH-092/121/209 share one consumer and must not become three discoveries.

## Stage 2: grounded obligate partners, through `/cross-field`

Use the existing `.claude/skills/cross-field/SKILL.md` retrieval, translation,
mapping-caveat and false-import checks. Do not create another translation engine.
Narrow its question to: for THIS demonstrated function, which partner components
are necessary in the reference mechanism, and is each PRESENT,
REGISTERED-NOT-BUILT, or UNWRITTEN in REE? Every row needs an inspected source,
`grounded` or `conjecture`, an explicit transfer limitation, and a falsifiable
consequence. Conjecture cannot justify registration; a non-falsifiable partner is
discarded. Literature necessity in one implementation is not universal necessity.
Keep analogue strength separate from REE experimental confidence. Retain the
cross-field field-diversity ledger. The chip authorizes a registration-only pilot;
no downstream experiment or architectural import is authorized. A scientific
choice or scope call still pauses for the user with a concrete proposal.

## Stage 3: forward check in both directions

For each nomination search the V4/V5 closure plans and transition-boundary docs,
not merely a stale `implementation_phase` or old memory. First ask whether a
registered future node already provides the function, then whether a V3-only
substitute would lock out the better interface. Assign a routing class per row:
V3-NATIVE, V4-PULL-FORWARD, or STOPGAP-WITH-RETIREMENT-CONDITION. For rejected
nominations this describes the proposed function's route, not build permission.
Necessity for V3 determines its phase; V4-labelled does not mean optional.
Nevertheless this chip explicitly reserves V4 pull-forward choices for the user,
and any actual stopgap/fossilisation trade-off must pause, name alternatives, and
name the retirement condition. Never silently make an architecture scope decision.

## Stage 4: durable output and repeat-run contract

Each surviving finding has exactly ONE terminal registration: substrate entry
with `sd_id`, `unblocks_claims` and
`proposed_REGISTRATION_ONLY_not_a_build_authorisation`; OR a governance flag raised
through `/Users/dgolden/REE_Working/scripts/governance_flag.py`; OR a candidate claim with a real
falsifier. Existing registrations are linked, not re-created. Do not confuse a
surviving stale-note flag with a U hit. No experiment is queued; no substrate is
built. Register the process itself as a candidate governance claim whether the
pilot is positive or negative; the observed hit rate is its evidence.

`unwritten_edge_rejected_ledger.json` retains each rejected/duplicate proposal,
stable interface key, source observations, verdict, existing owner, and a specific
reopening test. A repeat run suppresses only an unchanged proposition whose
reopening condition has not occurred; changed code or changed falsifier earns a
new adjudication. Never suppress by claim ID alone. The report and JSON preserve
every nomination and its adjudication, including candidates that create no node.

## Pilot results


Completed 2026-09-21 (pilot extraction 2026-09-20). The protocol above was committed and pushed as `5c486824fe8711bd07b54ab3bde23f36bfbb7b19` before running the detectors. No threshold or sample was changed after inspection. All 189 hashed inputs were byte-identical at the next-day continuation. Implementation fixes before final extraction qualified local future-plan node IDs, accepted null dependency lists, joined substrate/closure completion as well as claim status, and kept underscore-prefixed completion states for review. These repair extraction; they do not decide outcomes.

**Decision: DO NOT SHIP `/unwritten-edges`.** There are 39 distinct nominations, one verified new prerequisite (2.56%), two stale-note findings, and 36 rejected missing-node propositions. The 95% Wilson interval is 0.45%-13.18%, descriptive only. Yield is 1/8 selected nodes (1/7 audited); the pre-registered 50% precision, three-new-node minimum and two-source-node breadth all fail. Even excluding every obvious syntactic false positive cannot rescue the failed U>=3/breadth conditions. No skill or mirror was created and no GOV-HELDOUT-1 skill test is claimed. This is a negative result about this detector-and-ranking recipe, not evidence that all unwritten prerequisites have been found.

### Ranked sample and pre-check

| Rank | Node | Downstream nodes | Downstream claims | Live front | WWA routes | Decision |
|---|---|---:|---:|---:|---:|---|
| 1 | arc_062_rule_apprehension:GAP-B | 12 | 475 | 0 | 28 | Audit independent boundary only |
| 2 | behavioral_diversity_isolation:GAP-C | 3 | 175 | 0 | 22 | Audit independent boundary only |
| 3 | global_workspace_jlens:A | 3 | 70 | 0 | 9 | Audit independent boundary only |
| 4 | sd_037_axis_b:P1b | 3 | 13 | 0 | 13 | Audit independent boundary only |
| 5 | commitment_closure:GAP-4 | 2 | 419 | 0 | 34 | Audit independent boundary only |
| 6 | behavioral_diversity_isolation:GAP-B | 2 | 261 | 0 | 47 | Audit independent boundary only |
| 7 | behavioral_diversity_isolation:GAP-I | 2 | 213 | 0 | 76 | STOP: existing GFLAG-0297 / 0312 / 0329 re-pose |
| 8 | arc_062_rule_apprehension:GAP-I | 2 | 105 | 0 | 8 | Audit independent boundary only |

All eight remain in the sample. SD-037's `assembling` state is respected as construction, not failure; MECH-268's separately re-posed discriminator was not expanded. No fifth `zworld_actor_adequacy_locus` portfolio was opened. The graph snapshot has 119 V3 nodes (64 done, 34 remaining, 11 assembling, 10 deferred), 45 eligible unfinished nodes, and 420 nodes across generations. These live counts replace the older numbers in the chip. Fan-out includes completed descendants exactly as preregistered; it measures registered reach, not remaining unblockable work. Claims reach excludes the seed claims.

The current front did not appear in the top eight under literal, explicit-DAG ranking. Shared observation-interface roots are often prose/cross-plan relationships rather than explicit prerequisites. This is a material limitation: a leverage rank derived only from explicit edges can miss the very boundary debt sought. Do not silently add inferred edges to improve the pilot. A future revised rank needs a new prospective comparison and user-authorized rerun, not a skill presented as validated now.

### Detector measurement and controls

Global calibration: 1,168 claims, 188 substrate entries; D3 found **85 claims / 97 phrase hits**, D4 found **56** non-exact-complete entries with explicit empty dependencies, and D1 found **10** unread local names with zero parse errors. The chip's 86/57 were earlier observations, not acceptance targets. Substrate status normalization classified 90 exact-complete, 36 completion-prefix-needs-review, 58 unknown and four not-complete; the large unknown bucket is retained honestly because statuses are free prose. Nothing assumes an enum.

| Detector | Distinct pilot nominations | New nodes | Interpretation |
|---|---:|---:|---|
| D1 | 1 | 0 | Dead alias, live score consumer |
| D2 | 26 | 0 | Mostly history/completed validation prerequisites; two stale notes |
| D3 | 3 | 1 | One absent instrument, one subthreshold consumer, one retracted error |
| D4 | 15 | 0 | Existing owners and implementation/validation conflation |
| D5 | 3 | 1 | Same new node as D3; J-lens and GateDVRecorder already exist |
| D6 | 0 | 0 | 789 ID mentions screened for relations, no new absent sink/cycle |

Rows overlap; do not sum this table for N. D2 retained 212 raw occurrences, D4 19 selected-node occurrences, D3 three. D1 links one of the global ten hits to a selected falsifier. The JSON contains every raw hit and its many-to-one mapping. D6 mentions are relation-screening candidates, not 789 missing-node nominations: a citation is not a deferral edge. Its complete grouped screen and common-gate report are preserved. No supports layer or other edge schema was added.

**Positive control, excluded from U/N:** D1 found `_do_replay` assignments to `replay_trajs` at agent.py:10858/10865 with no local read; D3 independently recovered MECH-092 without a seeded search. The existing `mech092-replay-consumer-missing` registration prevents a second discovery. Scope remains MECH-092's benefit half and MECH-205; MECH-121/209 still require balanced replay scheduling and conversion competence. This case is motivating, never held-out.

### Surviving prerequisite and output routes

UEP-034 registers `mech318-within-episode-rule-switch-instrument`, with `unblocks_claims: [MECH-318]`, `ready: false` and the exact registration-only status. MECH-318's falsifier requires adaptation timing at an in-episode rule switch. Driver 606b explicitly alternates environments between episodes, resets the agent at each boundary, and defers within-step switching. CausalGridWorld's reef-axis setting is established in initialization. Existing ARC-064/MECH-316/317/318 entries cite the words `multi-rule-context substrate` but do not register an environment event/measurement provider. This is a missing node at the registry-to-code boundary, not evidence for a new recurrent architecture. The existing MECH-318 queue gate is repointed from that prose placeholder to the new ID; no sibling gates are broadened.

Acceptance is operational: an emitted trace contains a real rule change during a continuous episode, preserves agent state at that event, records event time for evaluation without supplying a privileged task-ID cue, and permits an adaptation-time contrast against recurrent-state ablation and no-switch controls. The absence claim is falsified by an existing registered/provider path meeting that contract. Scientific success/failure thresholds belong to a separately authorized experiment. ARC-062 GAP-B competence and SD-082 validation remain independent gates; registering the instrument clears neither. `pending_retest_after_substrate` is an obligation, not new support.

Forward verdict: **V3-NATIVE**, required by an existing V3 falsifier. The V4/V5 inventory and belief-state, option, memory and plasticity plans contain related internal architecture but no provider for the required environment event and DV. Cross-episode hidden-state continuity (W5) remains a separate V4 question. No V3 internal substitute is selected and no retirement/scope trade-off is silently decided. An actual architecture choice still goes to the user. The rejected `v4_loop_segregation` nomination is labelled V4-PULL-FORWARD provenance because that provider already landed; it does not authorize a new pull-forward.

UEP-018 and UEP-029 survive only as governance stale-note flags: MECH-318 still calls ARC-062 GAP-C open despite its done status; behavioral-diversity GAP-C still calls its done GAP-C-build child owed. Terminal flags are GFLAG-0397 (UEP-018) and GFLAG-0398 (UEP-029), neither a U hit. The registration process itself is recorded as **GOV-UNWRITTEN-1**, a candidate governance claim with this negative measurement and a prospective reopening falsifier. No experiment, build, claim promotion or third graph edge type was created.

### Grounded partners and rejected-edge ledger

The companion [partner audit](cross_field_unwritten_edges_2026-09-20.md) chains the existing `/cross-field` method over five inspected primary sources in three fields. Every partner has a PRESENT / REGISTERED-NOT-BUILT / UNWRITTEN disposition, a grounding label, transfer limitation, falsifiable consequence and content-shuffle question. RL2 does **not** require within-episode task switches: this obligation comes from MECH-318 itself. Analogue literature strength never updates REE experimental confidence. The cross-field document retains scientific translations as a draft with no architecture routing; completion of this chip does not depend on adopting them.

The [rejected-edge ledger](unwritten_edge_rejected_ledger.json) contains all 38 rejected missing-node propositions, including the two routed stale notes. Each names an interface, observed evidence, existing owner, and a reopening test. Reject by proposition, never by claim ID. After landing, UEP-034 is REGISTERED-NOT-BUILT on a repeat run, not another discovery.

### Every nomination and adjudication

The machine-readable [pilot](unwritten_edge_pilot_20260920.json) preserves complete source hashes, rankings, pre-check, raw extraction, hit map, forward verdicts and reopening conditions. This compact table is the human audit trail.

| Nomination | Proposed missing function | Adjudication |
|---|---|---|
| UEP-001 | Infant hazard-protection / curriculum exit readiness | Existing curriculum exit fix is mentioned historically; no absent provider established. |
| UEP-002 | Rule discriminator substrate | Phase 1 implementation is present; evidence gate remains. Free-text status is not an enum indicating missing machinery. |
| UEP-003 | Commitment entry / output gating | Substrate landed; validation and the right commitment-boundary DV remain distinct obligations. |
| UEP-004 | Asymmetric mode hysteresis | Existing mechanism and sibling comparison, not an unregistered prerequisite. |
| UEP-005 | Ecological gradedness measurement | Existing mechanism; its discriminator is already under GFLAG-0299 re-pose. No replacement machinery enumerated. |
| UEP-006 | Context anchor sets | The gate inventories existing anchor sets; completion is not a missing prerequisite. |
| UEP-007 | Ghost-goal / rumination guard | Absorbed mechanism and existing guard are contextual references. |
| UEP-008 | Drive bridge into selection | Known drive bridge and precedent, not an unowned build. |
| UEP-009 | Completed mechanism conjunction | Completed constituents still owe an integration measurement; no new constituent found. |
| UEP-010 | Phase-2 selector amendment | Amendment validated in 648a; not an absent component. |
| UEP-011 | Entropy bonus consumption in E3 scoring | The unused mech341_bonus_tensor is only an alias: mech341_bonus changes scores, the modulatory accumulator and LCG terms. Completed implementation can still need armed validation. |
| UEP-012 | Selection state machine and ecological exposure | State machine is implemented; non-degenerate ecological exposure remains an empirical precondition. |
| UEP-013 | Implemented SD-018 amendment | Implemented, pending validation; implementation and validation must not be conflated. |
| UEP-014 | Limb-damage state | Historical confound in arousal tests, not a missing state channel. |
| UEP-015 | Agency-comparator baseline readiness | C0 readiness is a measurement precondition on existing substrate. |
| UEP-016 | Salience operating-mode transition | The switch/event machinery exists; its mention does not assert absence. |
| UEP-017 | Nonzero bias exposure | Built code still needs bias_fraction above zero; this is non-vacuity, not a new build. |
| UEP-018 | Rule-state input wiring | Existing wiring is present and ARC-062 GAP-C is done, but MECH-318 what_would_answer still calls GAP-C open. Survives as stale-note flag only. |
| UEP-019 | Closure operator integration | Existing closure operator; an integration check is not another operator build. |
| UEP-020 | Factorial arousal component | The factorial component exists; empirical factorial separation can remain open. |
| UEP-021 | Broadcast override consumers | Consumers exist but their base signals are below input thresholds. The phrase no consumer output is not no consumer. |
| UEP-022 | Differentiable CEM default-off control | The note names a deliberate default-off safety gate, not absent machinery. |
| UEP-023 | Context baseline / overflow control | Existing baseline and historical overflow diagnosis are being cited. |
| UEP-024 | Registered observation-interface substrate | Implemented pending validation. Frozen root forbids adding another portfolio from this reference. |
| UEP-025 | Candidate-selection gradient path | Registered partial implementation has residual empirical limits. Empty dependency list does not erase the owner. |
| UEP-026 | Horizon-depth substrate | The old build route is later acknowledged implemented with negative validation. MECH-267 references describe this same interface. |
| UEP-027 | Probe warmup | Implemented and validated; a legitimate terminal task can have no dependencies. |
| UEP-028 | Persistent program handle during reselection | Implemented owner exists. The duplicate mech090 handle-fix entry is superseded; the live handle must be armed and its identity measured. |
| UEP-029 | Noise injection-site implementation | Child build is done while the parent resume_condition still calls it owed. Survives as stale-note flag, not an unwritten node. |
| UEP-030 | CRF availability maintenance | READY and validated; empty dependency list is expected after completion. |
| UEP-031 | Escape-affordance bridge | Registered and built; old phase prerequisite remains in historical prose. |
| UEP-032 | Commitment-boundary DV recorder | GateDVRecorder has landed; committed identity and boundary diagnostics are available. The prompt predated this reconciliation. |
| UEP-033 | J-lens discriminative concentration instrument | Readout fitting, evaluation, concentration and gates already exist. Upstream observation competence remains the gate. |
| UEP-034 | Within-episode rule-switch event and adaptation-time instrument | NEW: current driver alternates environments at episode boundaries and resets the agent; it cannot emit the within-episode switch event needed by MECH-318. The multi-rule-context prerequisite has only prose, no provider ID. |
| UEP-035 | Modulatory score-to-choice conversion | ARC-065 / GAP-A local lift and the authority build are registered. Their completion does not establish general conversion competence. Merge these mentions, do not invent another encoder remedy. |
| UEP-036 | Claim-evidence indexer repair | The matching phrase explicitly retracts a nonexistent indexer defect. Negated historical text is a false positive. |
| UEP-037 | Scaffolded ecological calibration | Scaffold is implemented; residual ecological calibration does not imply an unregistered build. |
| UEP-038 | Contested-mode occupancy probe | Probe already queued and registered. This audit queues nothing. |
| UEP-039 | Segregated selection loops | Future-labelled provider already exists; withdrawn validation is not absence. No new pull-forward decision made. |

### Reproduction and limits

`unwritten_edge_pilot_detectors.py` is an evidence-local, read-only extraction helper, not an installed workflow. Run it with `--base /Users/dgolden/REE_Working --output <scratch.json>` for ranking only. Then perform the manual re-pose check and repeat with one `--allowed-node <id>` for each permitted node. The original snapshot and source hashes in the pilot JSON are the reproducibility reference: later registry updates change counts. Do not run this helper unattended as a standing discovery rule.

The D1 AST scan is a cheap local-name screen, not interprocedural liveness analysis; side effects, aliases, attribute consumers and dynamic dispatch need human tracing. D2 preserves historical gate prose, which dominates false positives; exact-ID joining misses aliases such as bare Phase 3 GAP-C (found manually here). D4 empty lists are not evidence of an absent prerequisite. D5 and partner necessity are manual, bounded by the inspected drivers/tree. No assertion of complete recall is possible from one high-leverage sample. No future build budget or architecture was estimated.

Validation: strict claim validation and the derived claims JSON rebuild are required at landing; complete raw-hit mapping and artifact consistency are checked. Only the pilot's new governance claim, one nomination and its direct queue gate are changed. The public-information impact review covers update-docs, nav assignment and site/export generators: internal evidence/source routes and one candidate registry row change, with no new public navigation or scientific status claim. No public-explorer export is published; that remains owned by its existing redaction-review publication process at its next reviewed refresh. Existing inter-governance workset edits are foreign and excluded from the commit.
