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
through `REE_assembly/scripts/governance_flag.py`; OR a candidate claim with a real
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

Pending. This section will be completed after the protocol above is committed.
