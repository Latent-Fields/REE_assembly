# Work-graph debt classification sweep — 2026-08-27

**Generated:** 2026-08-27T19:43:28Z (session `f-dominance-regime-retest-ddbe10`, umbrella worktree; trial chip, deliberately not in TASK_CHIPS.json)
**Vocabulary:** `REE_assembly/docs/architecture/work_graph_debt_vocabulary.md` — tokens `complicated (buildable)`, `complex (probe-gated)`, `puzzle (known rules)`, `mystery (known data)`, `aleatoric (irreducible)`; the bracket is part of the token.
**Sources swept:** `closure_status.md` (2026-08-25 snapshot) Remaining-34 + Assembly-frontier-10 tables; plan frontmatter (`resume_condition` / `blocking_external` / latest governance notes) of the 12 plans holding those nodes; `substrate_queue.json` (incl. its existing per-entry `node_class` tags); `claims.yaml` status for the memory-cluster ids; spot-verification of allegedly-pending runs against actual manifests.
**Method:** the razor — recurse "is *that* buildable?" down each dependency chain; a node is *blocked* only at a link that is not buildable on demand. Where a node's own work is execution and it sits behind someone else's unknown, it is classified `complicated (buildable)` **gated on** the named token-bearing node, per the vocabulary's "gated on X is well-formed only if X resolves to a token" rule.

---

## The headline structural finding

The 34-node "remaining" backlog is not 34 independent walls. Almost every high-severity `blocked` label terminates, after one or two hops, in **one of two live unknowns**:

- **U1 — the competence wall** (MECH-457 cluster; `mech457_competence_bootstrap_explorer`, substrate_queue `node_class: complex (probe-gated)`): the integrated all-ON agent is not behaviourally competent enough to produce measurable committed behaviour (719a/724/732/737 lineage; re-derive brake fired at the 7th non_contributory; four axes eliminated 769-772). Per `CURRENT_FRONT.md` the hypothesis space is down to **1 of 20 rival explanations standing (~80% ruled out)** — this unknown is nearly discharged.
- **U2 — the F-dominance conversion question** (MECH-439 / `behavioral_diversity_isolation:GAP-I` -> `conversion_ceiling_campaign:FULLSTACK`; substrate_queue `f_dominance_conversion_ceiling`, `node_class: complex (probe-gated)`): does per-candidate diversity convert to committed action off the reef env, on a threat-engaged pool — now re-posable only with the corrected (non-hold-weighted) DV instrument, which has **landed** (ree-v3 `c309bc6486`).

Everything gated on U1/U2 is execution debt behind two spikes, not fourteen separate mysteries. That concentration is itself the actionable result: two probe results would flip roughly a dozen `blocked` labels to plain backlog.

---

## Summary table

| node | current label in docs | assigned token | one-line rationale |
|---|---|---|---|
| `behavioral_diversity_isolation:GAP-I` (MECH-439) | in_progress | **complex (probe-gated)** | The live U2 unknown itself; 936's C2 DV was arithmetically unreachable, so the corrected-DV regime retest is the owed spike. |
| `conversion_ceiling_campaign:FULLSTACK` | assembling (ran_exhausted_for_substrate) | **complex (probe-gated)** | The spike *vehicle* for U2: co-armed full-stack arm, DV committed-class entropy; assembly is execution, the verdict is the unknown. |
| `conversion_ceiling_campaign:GENERATION` (MECH-458) | assembling (blocked_on_upstream) | **complex (probe-gated)** | Whether diversity is generation-limited (vs merely un-converted) is a genuine empirical fork no analysis settles; probe upstream of selection. |
| `conversion_ceiling_campaign:P4-learned-gating` + `behavioral_diversity_isolation:GAP-K` (ARC-108/MECH-450) | assembling (blocked_on_upstream) | **complicated (buildable)** | The stated upstream block (corrected-DV instrument) has LANDED (`c309bc6486`); the residual hold is a governance *decision* (713x re-letter held 2026-08-21), not an unknown. See mislabeled list. |
| `mech457_competence_bootstrap_explorer` (U1; 724/732/737 lineage) | blocked_pending_discrimination | **complex (probe-gated)** | Correctly probe-gated on the GOV-FANOUT-1 H-bc-prior vs H-approach-primitive discrimination; "do NOT build blind" is right, and the space is down to 1 standing rival. |
| `self_attribution:GAP-1` (445h forensic / ARC-033 vs ARC-058) | blocked | **complicated (buildable)** gated on GAP-I [complex (probe-gated)] | The 3-arm 445i re-run is fully specified; it is unmeasurable until U2 lifts. Steward D-007 already re-pointed the gate correctly 2026-08-18. |
| `self_attribution:GAP-2` (SD-029/MECH-256 retest) | blocked | **complicated (buildable)** gated on FULLSTACK | Same gate as GAP-1 ("not a separate gap"); retest recipe known, would be vacuous pre-U2. |
| `self_attribution:GAP-3` (MECH-257 3-arm) | blocked | **complicated (buildable)** | Pure depends_on chain behind GAP-1/GAP-2; zero independent unknown. |
| `self_attribution:GAP-6` (SD-031) | blocked | **complicated (buildable)** gated on GAP-I | Diversity half = U2; the other half (world_dim >= 128) is a config knob satisfiable the same day. Claims.yaml states the hold as a prohibition — correctly held, but all execution once U2 lifts. |
| `sd_037_axis_b:P1b` | assembling | **complicated (buildable)** gated on FULLSTACK | The 625d joint-composite protocol is fully written; 625e's autopsy consolidated the blocker into U2. |
| `sd_037_axis_b:P2 -> P3 -> P4` | blocked x3 | **complicated (buildable)** | Pure phase chain behind P1b; three "blocked" rows that are one queue of labour. |
| `global_workspace_jlens:A` (J-lens readout) | blocked | **puzzle (known rules)** gated on U1 | Definite question, definite instrument (723a-style readout, gates fixed and non-degenerate); missing only the fact, obtainable the moment a competent substrate exists. |
| `global_workspace_jlens:GATE-B` (SD-027/MECH-254 build) | open | **complicated (buildable)** gated on A [puzzle (known rules)] | The build is specified; the pre-registered trigger (A positive) is currently unresolved, so *not* mislabeled — the hold is correct. |
| `global_workspace_jlens:B` (ablation cliff) | blocked | **complicated (buildable)** | Pure chain behind GATE-B; four-cell factorial already designed in resume_condition. |
| `global_workspace_jlens:MECH-191` | open (memory: "blocked") | **puzzle (known rules)** gated on A | The unblock check is a definite fact read off A's result (does the dispositional readout clear the tonic-accumulator wall). |
| `policy_decomposition_trigger:REPOSE` (ARC-070/MECH-321) | blocked | **mystery (known data)** | 938 is cleanly executed and null *at this grain*; governance explicitly refused another env-axis letter — "reopen only on a different operationalization". The data is in hand; a frame is owed, not more runs. |
| `commitment_closure:GAP-4` (OCD battery / MECH-090) | in_progress | **puzzle (known rules)** | The de-commit falsifier lineage (460k, successor 935a) is in flight on a purpose-built dissociable eval substrate; rules known, fact pending. |
| `commitment_closure:GAP-7` (MECH-091 trigger wiring) | blocked | **complicated (buildable)** | Its own blocking_external reads "substrate_queue MECH091-SALIENT-EVENT-TRIGGER-WIRING (V3, **buildable now**)". Flagship mislabel. |
| `sleep_substrate:GAP-2` (SD-017 retest cohort) | upstream_blocked | **complicated (buildable)** gated on arc_062:GAP-B | Retest cohort (418m/436b successors) is specified; gate is the differentiated-rule_state substrate, which itself terminates in U1/U2. |
| `arc_062_rule_apprehension:GAP-B` (MECH-309 falsifier) | in_progress | **complex (probe-gated)** (absorbed into U1) | The 719a reframe made this part of the competence wall. NOTE: its resume_condition still says "654h QUEUED + PENDING" — 654h ran terminal FAIL/non_contributory 2026-06-21 (manifest verified); text is 2 months stale. |
| `arc_062:GAP-I`, `GAP-I-absorption`, `GAP-J`, `behavioral_diversity_isolation:GAP-G` | blocked / blocked_pending_substrate x4 | **complicated (buildable)** | Four rows, one gate: all pure depends_on GAP-B; each is specified work (MECH-318 retire-vs-promote gate, MECH-312 family falsifiers, MECH-314 Goldilocks) the day GAP-B resolves. |
| `infant_substrate:GAP-14` (EXQ-ISEF-005) | blocked_pending_substrate | **mystery (known data)** | 591 + the 2026-07-21 knob-routing trace prove the Phase-0->1 gate is structurally unreachable and 667a's knobs are disjoint/attenuated — "needs a DIFFERENT DESIGN". More letters of the same design cannot move it; a re-operationalization is owed. |
| `mech357_avoidance_efficacy:BUILD` | open | **complex (probe-gated)** | Concur with the queue's own tag: the wiring (thread `hazard_agent_pursuit` through Stage-H `_build_env`) is trivial; whether it yields G_H_INTACT/G_H_LESION discrimination is genuinely untested after 5 config-only failures. Chip already open. |
| `orienting_epistemic_deficit_v3:ORNT-1` (MECH-395) | blocked | **complicated (buildable)** gated on the E3 cue-authority ceiling [complex (probe-gated), V3-EXQ-812 successor] | The orienting-mode build is specified; its block is the shared selection-authority unknown, which has a named successor probe. |
| `orienting_epistemic_deficit_v3:ORNT-2` (MECH-482 accumulator) | open (blocker text: MECH-482 non-degeneracy precondition) | **complicated (buildable)** | Both 2026-08-22 gates CLEARED per the plan's own status table (doc reviewed; SD-063 training landed `88287f11c6`); residual is a thin, already-chipped 2x2 validation, then the accumulator build. Near-mislabel: the frontmatter resume_condition lags its own status table. |
| INV-050 MEL producer link (+ INV-051, a-fortiori) | parked, re-derive brake fired | **complex (probe-gated)** | Consumer PROVEN (718a C3 exact-monotone); the unknown is whether *ecological* graded MEL exists at all — unanswerable on the converging env (~1e-5, noise). Spike: 701-style frozen-window MEL readout on a non-converging / continual-shift env. Do not touch until that env exists; brake is correct. |
| MECH-088 four-plane psychiatric taxonomy | blocked_substrate (memory) | **complicated (buildable)** (V4-leaning) + one owed adjudication | Zero of four plane knobs exist — that is execution backlog, deliberately deferred, not a wall. One genuine non-build item rides along: the unadjudicated MECH-085 vs MECH-006 conflict (a decision, cheap). |
| MECH-178 (NA REM-suppression) | blocked (memory) | **complicated (buildable)** (V4-leaning) | The NA plane is specified biology-first build work; nothing unknown gates starting it — it is prioritization. |
| MECH-179 (MEL type -> phase composition) | blocked (memory) | **complicated (buildable)** gated on INV-050 producer [complex (probe-gated)] | Build half is backlog (typed MEL channels + scheduler coupling); its testability additionally rides the ecological-MEL unknown above. |
| Play-mode cluster (ARC-049/050, MECH-194..199, INV-058..060) | blocked_substrate (memory) | **complicated (buildable)** | Re-verified today: zero substrate in `ree_core/` (one comment-only grep hit). Entirely specified architecture (play_mode.md + ~27 lit entries/claim) with no unknown at its head — pure, large, execution backlog. |
| SD-033e frontopolar de-commit validation | blocked (memory) | **complicated (buildable)** gated on U1 | Lever BUILT bit-identical-OFF; validation script written, validator-clean, smoke-passing, unqueued. Only ENV_KWARGS + P0 target change once U1 names a competent committed-foraging test-bed. |
| Interrupted-task resumption substrate (ID TBD) | unregistered gap (memory) | **complicated (buildable)** | Next action is a lit-pull + claim registration — fully specified scoping labour, startable on demand; nothing epistemic gates it. |
| Imagination-licit-learning principle (ARC-XXX TBD) | unregistered gap (memory) | **complicated (buildable)** | Three independent surfacings, none registered; the owed work is a Stage-2 intake + lit-pull. The licit/forbidden boundary Q-claims become puzzles *after* registration. |
| MECH-303 / MECH-304 (memory labels "blocked") | — | **(no open node)** | STALE: MECH-304 promoted active 2026-07-15 (V3-EXQ-763 PASS); MECH-303 promoted active 2026-08-22 (V3-EXQ-939a PASS); `mech303_safety_threshold_plan` is 100% done. Memory labels need retiring, not classification. |

Aleatoric note: **no node in this sweep earns `aleatoric (irreducible)`.** Every blocked chain terminates in a reducible unknown (U1, U2, the MEL-producer question, the pursuit-discrimination question) or in plain labour. The one existing aleatoric tag in `substrate_queue.json` (INV091-NULL-VALIDATION-RUN-LENGTH, `closed_aleatoric`) is already closed and was not re-adjudicated here. Assigning aleatoric anywhere else in this graph would bury reducible work.

---

## Non-obvious calls

### REPOSE is a mystery (known data), not a dead end
`policy_decomposition_trigger:REPOSE` is the cleanest textbook case in the sweep: V3-EXQ-938 was well-executed (rate-matched, non-degenerate, 0 seeds out of tolerance) and returned a null *at this grain*, and governance explicitly refused both a lettered successor and a fourth env-axis escalation. The node keeps the bare word "blocked" in the snapshot, but nothing buildable or runnable is owed — what is owed is a different operationalization of "prediction failure triggers decomposition" (different grain, different readout, or a different behavioural surface). Until someone does that reframing work, queueing anything here is waste; after it, the node becomes a puzzle with a definite experiment.

### infant GAP-14 is a mystery, not substrate-blocked
The label `blocked_pending_substrate` suggests waiting on a build. But the record says otherwise: 591 proved the Phase-0->1 advancement gate structurally unreachable under the training regime, and the 2026-07-21 read-only knob trace proved a "re-run with the lift ON" (667a) is not viable because one swept knob is disjoint from the E3 path and the other attenuated. The blocker is a *design* that cannot work as posed; the move is re-operationalizing the curriculum-vs-flat comparison (or folding it into the U1 resolution), not waiting for a substrate delivery.

### jlens A is a puzzle, not complex — the instrument already exists
It is tempting to tag Experiment A `complex (probe-gated)` because it is an investigation. But the probe design is finished and de-confounded (723a fixed the degenerate gates; criteria_non_degenerate all True); the only reason the answer is missing is that the substrate it must read is competence-limited. Rules held, fact missing -> `puzzle (known rules)`, gated on U1. This matters for prioritization: when U1 clears, A costs one run, and GATE-B / B / MECH-191 cascade behind it as plain labour — the whole jlens plan's "5%" understates how spring-loaded it is.

### GATE-B is correctly held — a build hold is not a mislabel
GATE-B looks like a mislabel candidate (open, build fully specified, nothing unknown about *how*). It is not: the plan pre-registered a build trigger (A returns compact-positive) and the trigger's prior supporting read was superseded. Building the SD-027 access gate now would spend effort ahead of the fact that licenses it. `complicated (buildable)` gated on A is the honest reading — buildable, deliberately not built.

### The chip-tagged node_class fields in substrate_queue mostly agree with this sweep
Where entries already carry `node_class` (f_dominance_conversion_ceiling, mech457 explorer, mech357 pressure mechanism, sd_salience mode-occupancy: all `complex (probe-gated)`; the SD-09x fix family: `complicated (buildable)`; mech151: `mystery (known data)`), this sweep independently reproduces every one of them. The disagreements found are all in the *closure plans and memories*, not the queue — the queue's tagging discipline (wired 2026-07-10) is working; the older plan frontmatter and project memories are where labels rot.

### Staleness found in passing (not classification, but load-bearing)
- `arc_062:GAP-B` resume_condition: "V3-EXQ-654h QUEUED + PENDING" — 654h ran terminal FAIL/non_contributory 2026-06-21T17:57Z. The 2026-07-09 reconcile absorbed the competence-wall reframe but never corrected this sentence.
- `orienting:ORNT-2` frontmatter resume_condition still names two gates as un-owned; the same plan's status table records both CLEARED 2026-08-22.
- Memory files `project_mech303_promote_active_zworld_blocked` and `project_mech304_behavioural_falsifier_substrate_blocked` describe claims that have since been promoted active; both should be retired or rewritten.

---

## Mislabeled as blocked (execution/decision backlog wearing a wall's label)

Ordered by how much the mislabel costs.

1. **`commitment_closure:GAP-7` (MECH-091 salient-event trigger wiring)** — status `blocked` while its own blocking_external says the substrate_queue item is "V3, buildable now". Two of three triggers unwired; this is a sitting `/implement-substrate` task.
2. **`conversion_ceiling_campaign:P4-learned-gating` / `behavioral_diversity_isolation:GAP-K` (ARC-108/MECH-450)** — `blocked_on_upstream` where the named upstream (corrected non-hold-weighted DV instrument) landed in ree-v3 `c309bc6486`; the remaining hold is the governance decision on the 713x re-letter (held 2026-08-21). A decision is owed, not an unknown and not a build.
3. **`orienting:ORNT-2` (MECH-482 accumulator)** — carried as gated on its non-degeneracy precondition; both gates cleared 2026-08-22. Residual: run the already-chipped 2x2 diversity validation, then build the accumulator. Effectively buildable now.
4. **Play-mode cluster** — "blocked_substrate" is a *queueing* verdict (correct: no experiment is queueable), but as a work-graph node the cluster is pure execution backlog: architecture documented, literature banked, zero unknowns at its head. Nothing prevents starting ARC-049's frame-tag build except prioritization.
5. **MECH-178, MECH-088 planes** — same shape as play-mode: deliberately-deferred V4-leaning builds described with blocked language. The only genuinely non-build item in MECH-088's chain is the cheap MECH-085-vs-MECH-006 adjudication.
6. **Interrupted-task resumption + imagination-learning principle** — both live only as memory files saying "do not register without a lit-pull". The lit-pull *is* buildable-on-demand labour; three independent surfacings of the imagination item argue it should stop being ambient.
7. **(Label debt, not work debt)** MECH-303 / MECH-304 memory "blocked" labels — the claims are active; nothing is blocked because nothing is open.

Pure-chain rows inflating the blocked count without independent content (correctly labeled, but worth reading as *one* queue each): `sd_037_axis_b:P2/P3/P4`, `self_attribution:GAP-3`, `jlens:B`, `arc_062:GAP-I/GAP-I-absorption/GAP-J` + `behavioral:GAP-G` — eight table rows, two actual gates (FULLSTACK, GAP-B).

---

## Highest-yield probes (max 5)

1. **Finish the U1 competence discrimination (GOV-FANOUT-1: H-bc-prior vs H-approach-primitive).** 1 of 20 rivals standing; one more discriminating result names WHICH competence dependency to build and converts `mech457_competence_bootstrap_explorer`, jlens A->GATE-B->B->MECH-191, SD-033e validation, and the GAP-B retest wall into plain backlog. Highest fan-out per token of compute in the whole graph.
2. **The corrected-DV FULLSTACK conversion probe (U2).** Co-armed full-stack arm on a competence-repaired substrate, scored with the landed fresh-select GateDV instrument (never the hold-weighted readout). A verdict either way flips ~9 blocked rows (self_attribution GAP-1/2/3/6, sd_037_axis_b P1b->P4) to execution, or falsifies the selection-face framing entirely. Sequencing note: it consumes probe 1's output — these two are a pipeline, not alternatives.
3. **MECH-357 hazard-pursuit discrimination test.** Cheapest spike in the sweep: the pursuit mechanism is already built in the env, the wiring is a mirrored config thread, the chip is open, and it is the *last* untried pressure design — a null here terminates a 5-attempt lineage cleanly instead of leaving it ambient.
4. **Graded-MEL diagnostic on a non-converging environment (INV-050 producer).** Build a continual-shift test-bed, re-run the 701-style frozen-window raw-PE readout. Converts the MEL-producer unknown into a puzzle; a positive additionally releases INV-051 and MECH-179's testability, and it is commitment-free (diagnostic, exempt from the re-derive brake).
5. **GENERATION-face measurement (MECH-458).** Measure per-candidate strategy diversity *upstream* of selection. If generation is the limiter, five faces of selection machinery are aimed at the wrong stage — this probe protects the whole conversion campaign against a category error and is independent of probes 1-2, so it can run in parallel.

---

*Scope note (v1.0): classification only, per the spawning instruction. Nothing in v1.0 was built, queued, or chipped; no claims.yaml / substrate_queue / plan-frontmatter edits were made.*

---

# Addendum v1.1 — same-day verification corrections + routing (user-directed)

**Added:** 2026-08-27, same session, after the user directed that the identified work be routed (chips + flags + reconcile edits). Chip-rule STOP-CHECK-style verification before spawning overturned **three** v1.0 rows — recorded here so the table above is not read uncorrected.

## Corrections to v1.0

1. **`mech357_avoidance_efficacy:BUILD` — the probe already ran, negative; token migrates `complex (probe-gated)` -> `mystery (known data)`.** The pursuit wiring landed 2026-08-14 and V3-EXQ-603u (2026-08-16 governance) returned G_H_LESION_frac = 1.0: all four pressure designs are now exhausted (substrate_queue entry `validated_negative`). The sibling eligibility-trace repair's validation **V3-EXQ-603v ran PASS/supports 2026-08-27T18:47Z (unreviewed)**. The owed work is the substrate entry's own named precondition: the zero-compute reanalysis of the recorded 603s/603t/603u trajectories. Probe #3 in the highest-yield list is therefore replaced by that reanalysis (chipped below). The v1.0 plan-staleness observation stands — the plan node still read `open`/unbuilt; reconcile note added.
2. **`commitment_closure:GAP-7` (MECH-091) — not merely buildable: essentially RESOLVED pending review.** The trigger wiring landed 2026-08-17 (ree-v3 `6293b239`); validation 944 was voided on a control degeneration, its autopsy-routed successor **V3-EXQ-944b ran PASS/supports 2026-08-25 (unreviewed)**. No chip warranted; this is pending_review + a node flip — flagged (GFLAG-0067). v1.0's "flagship mislabel" verdict was right in direction but understated: the node was not just buildable, the build and its validation are both done.
3. **`conversion_ceiling_campaign:GENERATION` — NOT freely parallel.** v1.0's probe #5 said it "can run in parallel"; the node's `upstream_block_reason` says it is ORDERING-GATED on INV-088 z_world differentiation (a rarity term over an under-differentiated map has nothing to range over). `blocked_on_upstream` is accurate; token stays `complex (probe-gated)` but the spike must wait on INV-088. Not chipped.

## Routing performed (this session, user-directed)

**Plan-frontmatter reconcile notes** (docs-only, dated fields, no status changes; REE_assembly `61669463f6`): `arc_062:GAP-B` (stale "654h QUEUED+PENDING" — ran terminal 2026-06-21), `orienting:ORNT-2` (resume_condition lagged its own status table's gates-cleared record), `mech357:BUILD` (overtaken by 603u/603v, above).

**Governance flags raised** (stale_note; on origin/master): **GFLAG-0067** (MECH-091 — review 944b, flip GAP-7), **GFLAG-0068** (MECH-357 — review 603v, flip BUILD, reanalysis chipped), **GFLAG-0069** (ARC-108/MECH-450/MECH-439 — blocked_on_upstream stale, GateDV instrument landed `c309bc6486`; the residual is the held 713x re-letter *decision*, adjudicate it).

**Memory labels retired** (session memory, not repo): MECH-303 and MECH-304 "blocked" memories rewritten as tombstones (both claims active: 2026-08-22 / 2026-07-15).

**Chips spawned** (all recorded in TASK_CHIPS.json with STOP-CHECKs incl. `task_claim.py check`; model guidance embedded per prompt — Fable for the three high-judgment items, Opus for builds/pulls):

| chip_ref | routes to | model | discharges |
|---|---|---|---|
| chip-20260827-mech357-trajectory-reanalysis | analysis memo -> /governance | fable | mech357 mystery (known data) |
| chip-20260827-arc070-repose-reoperationalization | design spike -> /governance | fable | REPOSE mystery (known data) |
| chip-20260827-competence-final-discriminator | /queue-experiment | fable | U1 (last standing rival) |
| chip-20260827-inv050-nonconverging-mel-env | /implement-substrate + /queue-experiment | opus | INV-050 producer unknown (user-authorized un-park) |
| chip-20260827-mech482-accumulator-build | /implement-substrate | opus | ORNT-2 build (gates cleared) |
| chip-20260827-litpull-task-resumption | /lit-pull + registration | opus | unregistered resumption gap |
| chip-20260827-litpull-imagination-licitness | /lit-pull + Stage-2 intake | opus | thrice-surfaced unregistered principle |
| chip-20260827-infant-gap14-redesign-scoping | staged proposal -> /governance | opus | GAP-14 mystery (known data) |

**Deliberately NOT chipped:** FULLSTACK corrected-DV probe (sequenced behind U1 + the GFLAG-0069 decision — governance chips it once ratified); GENERATION (INV-088-gated, correction 3); jlens A/GATE-B/B/MECH-191 (spring-loaded behind U1, correctly held); the U2-gated execution chains (self_attribution GAP-1/2/3/6, sd_037_axis_b P1b-P4, sleep GAP-2, arc_062 GAP-I/J + behavioral GAP-G); play-mode / MECH-088 planes / MECH-178 (deliberate V4-leaning deferrals — chip on request); 603v and 944b review (pending_review walk, governance-owned).
