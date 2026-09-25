# Thought Intake: REE Assembly as continuous scientific assurance

**Date:** 2026-09-25
**Raw thought file:** `docs/thoughts/2026-09-24_ree_assembly_as_continuous_scientific_assurance.md`
**Session:** thought-backlog-20260925 (drafted by a read-only agent; registered by the orchestrating session)
**Digestion drafts:** none produced.

## 1. Verbatim prompt (core proposal)

> REE Assembly is becoming a continuous scientific-assurance system for constructing an
> experimental organism.

The thought asks whether REE Assembly's style of work exists elsewhere and what it can borrow.
Its answer: no single field matches REE end to end. REE has converged on a hybrid of systems
engineering (MBSE and V&V), assurance cases (with defeaters), self-driving laboratories,
distributed control planes (desired vs observed state, leases, reconciliation), hermetic and
reproducible builds, and cognitive-architecture construction.

It proposes six imports:

1. machine-readable causal interface contracts for load-bearing handoffs;
2. explicit defeaters attached to claim-evidence relationships;
3. one canonical execution-state model (lease + heartbeat + epoch), with the workset as a derived view;
4. null-regeneration tests for consequential generators;
5. identity independent of generation order;
6. a permanent vertical-slice organism assay, frozen once a sound D3 assay exists.

It lists five things not to import and three small pilots (A: one interface record; B:
authoritative in-flight state; C: null regeneration). It also gives six falsifiers of itself.
Its header states that the document itself authorises no claim, governance, substrate,
experiment or confidence change. That bound is honoured here. The one registration below is a
`candidate` governance rule, which is not a confidence change.

## 2. What's new vs. existing REE docs/claims

| # | Thread in the thought | Existing REE coverage (cited) | Verdict |
|---|---|---|---|
| T1 | Core thesis: Assembly is "a continuous scientific-assurance system for constructing an experimental organism". It maintains the warranted relation theory -> computation -> experiment -> evidence -> inference -> organism behaviour. | `docs/architecture/developmental_governance_review.md` (2026-05-16) Part 1 already maps REE onto assurance and traceability practice: "REE's claims.yaml is functionally a flat-file GSN" (Kelly 1998), IEC 61508 bidirectional traceability, Ramesh & Jarke rationalisation links. **INV-077** (evaluation channels are evidence-producing boundaries mediated by governance). **GOV-PROC-1**, **GOV-STRAT-1**. The 07-31 causal-realisation intake sec 14 has the same theory->computation->experiment->behaviour chain nearly verbatim. | **Already owned** as framing. Not claim-shaped. |
| T2 | Sec 1, MBSE/V&V: verification vs validation, component vs complete-system integration, requirement-to-evidence traceability. | **GOV-JURIS-1** (D0-D7 evidence-domain profile), **ARC-130** (stage-qualified reachability: existence -> ... -> committed throughput -> ecological consequence -> retention), **ARC-131** (installability: passes in isolation, fails in composition), **INV-105** (latent-access ladder). Traceability: IMPL-018 plus the May review. | **Already owned.** The thought's own list (local validity ... adaptive recovery) is the D0-D7 table. |
| T3 | Sec 1 lesson + 8.1 + Pilot A: machine-readable **causal interface contracts** (producer, consumer, schema, units, lifetime, update authority, confidence semantics, activation conditions, mediator, expected effect, invariances, invalidating observations) for load-bearing handoffs. | **Agent side: ARC-144** (the contract is boundary-indexed: `C = { A -> B : I_AB, tolerated distortion, receiver capability, fallback }`, one entry per directed interface), **ARC-142**, **INV-104** (first instantiated contract, observation -> z_world -> E1/E2), **MECH-530** (typed E3 outputs). **Instrument side:** `evidence/planning/thought_intake_2026-07-31_architectural_causal_realisation_graph.md` proposes a `MechanismRealisation` record with the same fields (producers, consumers, temporal preconditions, mediators, invariances, `invalid_if`) and a four-case pilot with pre-registered success and failure criteria (sec 12). It routes the pilot to stay **outside the claims registry until it shows scientific utility** (sec 15.4). **Per-experiment enforcement already exists:** GOV-CAPCONTRACT-1 (declare and preflight constructed/enabled/reached), GOV-PATHVALID-1, `/queue-experiment` 2.5a (one-tick reachability probe) and 2.5d (falsifier-runnability trace: EVENT/DV/INSTRUMENT, ABSENT/INERT). **Re-measured:** the 07-31 pilot has never run. No realisation record exists anywhere in REE_assembly, ree-v3 or scripts (grep for `MechanismRealisation` / `causal_realisation`: only the intake itself). | **Already owned** (concept and pilot design). **Tooling proposal, not a claim.** The thought's Pilot A is the 07-31 pilot at n=1. Follow-on F5. |
| T4 | Sec 2: assurance cases in general (claim / argument / evidence / assumptions / context). | The May review (GSN mapping; AMLAS; Proposal G5 "Assurance Claim Point" per queue entry naming "which defeaters the experiment addresses"). The queue docstring and criteria discipline. | **Already owned.** |
| T5 | Sec 2 + 8.2: **explicit defeaters** as first-class objects attached to claim-evidence relationships. "A positive result with an unresolved defeater should be visibly different from an uncontested positive result." | **Partly owned. Three pieces exist:** (a) a *raising channel*: `governance_flags.v1.json` via `scripts/governance_flag.py` (types `evidence_discrepancy`, `contested_disposition`, `stale_note`, `promotion_review`; 509 items, 42 open); (b) *resolved* defeaters as per-edge qualifiers in `claim_evidence.v1.json` entries (`scoring_excluded` 2147, `degeneracy_reason` 101, `duplicate_of` 79, `superseded_by_substrate` 5, `recorded_preconditions_unmet` 2, `evidence_direction: superseded/non_contributory`); (c) *defeater classes and detectors* as GOV rules: GOV-JURIS-1 (scope defeater: D1 result narrated as D3), GOV-CAPCONTRACT-1 (inadmissible negative), GOV-PATHVALID-1 (mocked precondition), GOV-FAILLOC-1, GOV-DRY-1, GOV-APPLY-1, GOV-SUBPATH-1, GOV-CRITBAR-1, GOV-MATCHAUX-1. **Not owned:** what an evidence edge's status is *while a defeater is open*. **Measured:** no summary surface reads open flags (`serve.py`, `explorer.html`, `build_claims_json.py`, `generate_current_front.py`: 0 references). Resolved `evidence_discrepancy` flags stayed open for median 3.3d, p90 8.9d, max 26.5d (n=201). In that window the edge counts as uncontested support. **The gap was named on 2026-05-16** ("no policy requires an explicit named defeater register before promotion", Bloomfield & Rushby Assurance 2.0; Part 6 table "no structured defeater register") and **never registered**. **Live now:** GFLAG-0453 (open) says V3-EXQ-569i's matched-noise arm is bit-identical to the proposer arm. `claim_evidence` still counts 569i as `supports` for **ARC-065**, which is `stable` with quadrant `confirmed_established` (0.786). GFLAG-0453 also covers V3-EXQ-499 (`supports`, MECH-094, `stable`). GFLAG-0454 (open) says V3-EXQ-811a's familiarity manipulation may have measured recency; 811a is counted as `supports` for MECH-477 and MECH-163. | **Genuinely new, registered narrowly as GOV-DEFEAT-1** (section 3). It is scoped to the open-window status and summary-layer visibility of evidence edges. It reuses the flag registry as the defeater store and adds no new registry. |
| T6 | Sec 2 display: per-claim D0-D7 profile plus "Open defeaters: GFLAG-..." | GOV-JURIS-1 requires the `Evidence domain reached / Domains not tested` line in upward summaries. It deliberately has "no hook, no gate, no score". The only machine surface is the human-maintained `current_front_evidence_domain.json` for the lead EXQ (`generate_current_front.py`). | **Owned as a rule.** Display is tooling, folded into follow-on F2. |
| T7 | Sec 3: self-driving labs; bounded **expected-information-gain** advisory priority score (discrimination x centrality x domain elevation x reuse / cost, with vacuity and duplication penalties); "the umpire remains more important than the ruler". | Qualitative form: the work-graph debt vocabulary (umbrella `CLAUDE.md`: "only reducible unknowns convert effort into information"). Candidates: GOV-FANOUT-1 (bottleneck fan-out), GOV-REUSE-1 (reanalysis first = duplicate penalty), GOV-CONFIRM-1. Vacuity penalty: `/queue-experiment` 2.5a/2.5d and GOV-CRITBAR-1. Anti-Goodhart: **GOV-FROZEN-1**, **GOV-BEHADJ-1** ("umpire, not ruler" is its wording), **GOV-META-1**. **Measured precedent against ranking heuristics:** GOV-UNWRITTEN-1's leverage-ranked pilot **failed its shipping threshold** (U=1 of N=39, 2.56%). The IGW `_priority_score` is severity/status-based only. | **Tooling proposal, advisory only. Not a claim.** Lowest priority (F8). |
| T8 | Sec 4 + 8.3 + Pilot B: one authoritative observed-execution-state model (spec vs status: owner, lease, heartbeat, epoch, machine, worktree, last progress); the workset should be a derived view over it. | Phase 3 coordinator (`ree-v3/coordinator/`, live since 2026-05-29): DB is authoritative for task claims and chips (cutover 2026-08-28), heartbeats, `dispatcher_leases`, `dispatch_campaigns`, `claim_log`. The hub materializer renders the git registries from the DB. That is the desired-state vs observed-state split and the materialised-view pattern. **Measured defect in the derived view:** the workset's `summary.in_flight` counts only closure-gap items whose `owner_exq` is in the live queue (`generate_inter_governance_workset.py` `_infer_lane` ~L2888, summary ~L3670). It reads neither coordinator claims nor `igw_assignments`. The workset generated 2026-09-25T10:03:08Z reports `in_flight: 0, assigned: 0` while its own summary lists `live_exqs: [V3-EXQ-1067, 1090, 1099, 906c]`, and `TASK_CLAIMS.json` has 13 active claims under 6h old. This is the thought's "0 in flight while sessions are alive" class, reproduced today. | **Already owned architecturally; one concrete derivation defect.** Engineering follow-on F1. Not a claim. |
| T9 | Sec 4: long-running orchestrators reviving one another. "Revival should restore service, not resurrect obsolete authority." Lease plus monotonic fencing token/epoch; Erlang/OTP supervision. | `scripts/dispatcher_control.py` leases: fail-closed expiry, `MAX_LEASE_HOURS`, authorisation windows. **Investigated 2026-08-26:** `evidence/planning/lease_outlives_claim_investigation_20260826.md`. Its one confirmed case was a resumed orchestrator that kept renewing a lease for hours after its own `/session-land`. Gating renew on a live TASK_CLAIMS claim was **rejected on measurement**: expiry already bounds it, and the identities are free-text. A print-only advisory shipped instead. Coordinator `upsert_dispatcher_lease`: newest `requested_at` wins, so a revived holder's renew *wins* over a newer holder. That is exactly the resurrection shape; no fencing is in place. | **Partly owned and partly rejected-on-measurement.** A fencing epoch is a *different* predicate from the rejected gate, so it is not barred, but it is an engineering item owned by the orchestrator machinery (`feedback_leave_metaworker_orchestration_to_orchestrator`). Follow-on F6. Not a claim. |
| T10 | Sec 5 + 8.4 + Pilot C: hermetic generation; a **null-regeneration test** (regen, regen again, zero semantic diff); generated documents as projections, never competing sources of truth. | Umbrella `CLAUDE.md` "Narrow Edits Only". Per-generator idempotency tests exist: `test_compact_rendering_is_idempotent`, `test_manual_proposal_status_survives_two_regen_cycles_via_backlog_id`, `test_mint_missing_manual_backlog_ids_is_idempotent` (`test_build_experiment_indexes.py`), `test_rebuild_is_idempotent_and_replaces_atomically` (`test_derived_evidence_db.py`), and `promote_status_history.py`, which is idempotent by contract. Incident-driven fixes: chip-20260902-indexer-run-timestamp-rendering-drift, chip-20260907/0911/0923 disposition-revert fixes (last one REE_assembly `16a08a789e6`), the negative-instrument audit (2026-09-22). Experiment-input hermeticity: `arm_reuse_fingerprint_plan.md` (content fingerprint, refuse-by-default), `substrate_hash`, `machine_class` (cross-class `torch.multinomial` divergence). Detector home: `scripts/steward/` (d010 denominator integrity, d101 divergence content-equivalence). **Not present:** a cross-generator "regen twice -> zero semantic diff" canary. | **Principle owned; one tooling gap.** Follow-on F3. Not a claim. |
| T11 | 8.5: stable identity independent of list position, discovery order or regeneration timing. | **Already fixed 2026-09-04** (campaign C5). `build_experiment_indexes.py` "Stable proposal-id allocation" block: persisted, append-only `evidence/planning/proposal_id_allocations.v1.json` keyed `(backlog_id, lane)`; ids are never reassigned or recycled. It explicitly rejects content-hash ids ("would renumber the ENTIRE corpus exactly once"). The measured motive: 718 of 916 ids churned by one regen, and 172 chips withdrawn. EXQ ids: manual lettering policy. **Residual found:** `scripts/generate_inter_governance_workset.py` L2942-2945 (text from 2026-06-21, commit `0e409601fd0`) still tells every `/queue-experiment` brief that "auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle". The block comment near L3500 says the same. Both became false on 2026-09-04. | **Already owned.** One stale-text follow-on (F4). |
| T12 | Sec 5: human dispositions must live in canonical state that generators consume, never in generated state they can erase. | The carry-forward fixes above; memory `reference-manual-proposal-status-reverted-by-regen`; **GOV-STRAT-1** (a fast layer must not silently change a slower layer's commitment). | **Already owned** (as incident-driven fixes). The F3 canary is its general guard. |
| T13 | Sec 6: an append-only **scientific event ledger** with state as a materialised view. The thought cautions: only if a pilot shows it reduces disagreement. | Event sourcing is partial but real. Coordinator append logs: `claim_log`, `heartbeat_log`, `git_intent_log`, `workspace_state_entries`, `igw_log_entries`, `recommendation_log_entries`. Phase-2b materializer: registries rendered from the DB. Status-history plane SHP-3: append-only, change-only `status_history/status_snapshot.v1.jsonl` answers "what did we believe on DATE". `evidence/decisions/decision_log.v1.jsonl` (597 rows). `completion_note_history`, `prompt_history`, governance-flag lifecycle. No per-claim status event stream: `claims.yaml` history is git. | **Partly owned; tooling proposal.** Do not build (the thought's own caution plus GOV-META-1). F9. |
| T14 | Sec 7: cognitive-architecture construction methodology is immature; REE's D0-D7 split may be stronger than typical practice (Jimenez et al. 2021). | The D0-D7 doctrine owns the substance. Jimenez 2021 and Canty & Abolhasani 2026 are **not** in the literature corpus (grep verified). | **Literature observation only.** Not a claim; per `feedback_lit_exp_decoupled` it moves no confidence. Optional lit-pull (F10). |
| T15 | 8.6: a **permanent vertical-slice organism assay**. Once a sound D3 assay exists, freeze a family of them and re-run the seven questions (detect, represent, reach selection, alter action, alter world, learn, retain) at every major integration wave, as an organism integration/regression test. | The assay itself is **P4 "one useful choice, end to end"** in `evidence/planning/orchestrator_execution_prompt_2026-09-24_functional_organism_path.md` (gated on a preflight and a user decision D1). **Re-measured: not commissioned.** It has no queue entry (`ree-v3/experiment_queue.json` grep) and no preflight file. Freezing: **GOV-ECOL-1** ("A frozen ecological suite is a FUTURE requirement; when built it is frozen before use"). Retention: ARC-130's retention stage. Periodic challenge: **GOV-DELETE-1**. Cross-version reference: **GOV-V3FREEZE-1**, **GOV-BRIDGE-1**. Coexistence gate: **GOV-UMPIRE-1**. **No claim mentions capability regression or backward transfer** (0 hits). The May review noted BWT/FWT is absent. | **Adjacent. NOT registered this pass:** its object (a sound D3 assay) does not yet exist, and GOV-ECOL-1 already registers the frozen-suite requirement at the same level of abstraction. The one new element is the re-run-at-every-integration-wave cadence, with a regression recorded as a D6 finding. That goes to `/governance` as a proposed one-sentence GOV-ECOL-1 amendment, **triggered by the first confirmed P4 PASS** (next step 3). Falsifier 6 of the thought (brittle regression targets) travels with it. |
| T16 | Sec 9: what not to import (no SysML bureaucracy, no maturity score, the causal graph stays falsifiable, optimisation must not set the agenda, prefer deletion). | GOV-JURIS-1 ("never a scalar ladder"), GOV-DELETE-1, GOV-META-1, GOV-BEHADJ-1, GOV-FROZEN-1. The 07-31 intake secs 10-11 (the realisation graph is a hypothesis, falsifiable at runtime). | **Already owned.** |
| T17 | Sec 10: six planes (theory, realisation, experimental, assurance, control, organism), kept mutually consistent without being merged. | Organising frame. Nearest: **GOV-STRAT-1** (artefact update-rate layers, a different axis) and **GOV-ANALOGY-1**. | **Not claim-shaped.** Kept as vocabulary in the intake only. |
| T18 | Sec 11: behaviour alone cannot show an ethical representation was causally operative, as opposed to a hard-coded heuristic, an incidental reward landscape, an external veto, an "other" never consulted, or a consumer that ignored the signal. | **SENT-17** (a substitution must preserve ethical-process representations and their causal authority, not just the action distribution). **INV-105** ("causally used" != "behaviourally beneficial"). **ARC-130**, **GOV-PATHVALID-1**, **GOV-JURIS-1** (D2 vs D3), **INV-077**. | **Already owned.** The five-alternative list is a useful design checklist for the V5 ethical assays (next step 5); no claim. |
| T19 | Sec 12-13: three methodology pilots, and six falsifiers of the thought. | Pilots map to F5 / F1 / F3. Falsifier 4 ("explicit defeater tracking merely duplicates governance flags without improving interpretation") is carried as GOV-DEFEAT-1's primary kill condition. | Used as design constraints. |
| T20 | Conclusion: "make the orchestration boring (deterministic, idempotent, lease-based, reproducible, derived from canonical state) and the science layer sophisticated". | The stated direction of the Phase-3 cutover and the Narrow Edits / carry-forward work. | Framing; not claim-shaped. |

**GOV-ANALOGY-1 note.** The thought compares REE *Assembly* with external engineering disciplines.
It does not compare REE (the agent) with Assembly, so GOV-ANALOGY-1 does not bind. The thought also
labels its anchors "analogues ... not evidence that their methods validate REE", which respects that
rule's spirit.

---

Summary: 17 threads are already owned or are framing. Two (T3, T15) are adjacent and routed as
follow-on work and a trigger-conditioned `/governance` amendment. One (T5) is genuinely new and
registered narrowly.

## 3. Key formulations (verbatim, load-bearing)

> The thing being continuously maintained is not only executable code. It is the warranted
> relationship between the theory REE states, the computation REE implements, the experiment REE
> performs, the evidence REE obtains, the inference REE is allowed to make, and the behaviour of the
> assembled organism.

> A positive result with an unresolved defeater should be visibly different from an uncontested
> positive result.

> Revival should restore service, not resurrect obsolete authority.

> Generated documents should remain projections, never competing sources of truth.

> Experiments, claims, hypotheses, work obligations and decisions should keep identity because of
> what they are, not because of where they happened to appear in a generated list.

> The umpire remains more important than the ruler.

> Not "did we build the proposed part?" but "does the intended information traverse the causal
> chain, reach an authorised consumer, alter a decision, alter the world, and survive into later
> learning?"

## 4. Premise re-measurement (CLAUDE.md "audit its premises")

| Premise in the thought | Re-measured 2026-09-25 ~10:40Z | Verdict |
|---|---|---|
| The workset reports "0 in flight" while sessions are alive | `inter_governance_workset.v1.json` (generated 10:03:08Z): `in_flight 0, assigned 0`, while its own `live_exqs` lists 4 EXQs; 13 active claims under 6h old | **HOLDS.** Cause located: `in_flight` is derived only from closure-gap `owner_exq` in the live queue |
| Generated experiment identifiers renumber | True until 2026-09-04; fixed by stable proposal-id allocation (campaign C5) | **STALE.** Residual stale instruction text remains in the workset generator |
| Manual dispositions are overwritten by regeneration | Three incidents (09-07, 09-11, 09-23); carry-forward fix landed `16a08a789e6` | **Held; fixed incident by incident.** No general guard |
| The causal-realisation proposal "already points strongly in this direction" | The 07-31 intake exists; its pilot has never run | **HOLDS.** The pilot is still owed |
| "REE already represents much of this [defeaters] through failure autopsies, evidence-quality notes and governance flags" | Flags are the raising channel and edge qualifiers are resolved defeaters. The open window is invisible at the summary layer (measured, see sec 6) | **HOLDS, sharpened** |

## 5. Affected existing claims

No existing claim's status, confidence, evidence record or text was touched.

- **GOV-JURIS-1**: extended by GOV-DEFEAT-1. Where JURIS bounds what a result may claim (scope),
  GOV-DEFEAT-1 bounds how a result may be presented while a specific doubt about it is open. Composes;
  does not amend. `/governance` may prefer to fold GOV-DEFEAT-1 into GOV-JURIS-1's summary-line
  template ("... / Open defeaters: GFLAG-..."). That fold is left open deliberately.
- **GOV-CAPCONTRACT-1, GOV-PATHVALID-1, GOV-FAILLOC-1, GOV-DRY-1, GOV-APPLY-1, GOV-SUBPATH-1,
  GOV-CRITBAR-1, GOV-MATCHAUX-1**: named as *defeater classes and detectors*. GOV-DEFEAT-1 does not
  duplicate any of them. It governs the interim status of the edge they target.
- **GOV-ECOL-1**: a proposed amendment (re-run cadence and regression as a D6 finding) is routed to
  `/governance`, triggered by the first confirmed functional-organism P4 PASS. Not applied.
- **ARC-144 / ARC-142 / INV-104 / GOV-CAPCONTRACT-1**: own the interface-contract concept (T3).
- **SENT-17 / INV-105 / ARC-130**: own the ethical-traceability argument (T18).
- **GOV-UNWRITTEN-1**: cited as the measured precedent against leverage-ranking heuristics (T7).

## 6. Candidate claims -- REGISTERED this pass

- **GOV-DEFEAT-1**: `governance.epistemics.open_defeater_contested_evidence`. Open-defeater rule:
  evidence named by an open `evidence_discrepancy` / `contested_disposition` flag is CONTESTED
  at the summary layer until countered. It keeps its score but loses its standing as uncontested,
  and it cannot carry a promotion or a "confirmed/established" description on its own.
  `status: candidate`, `epistemic_category: governance_rule`, `implementation_phase: v3`,
  `version_relevance: v3` (it binds the current Assembly, like GOV-JURIS-1).
  `depends_on`: GOV-JURIS-1, GOV-CAPCONTRACT-1, GOV-PATHVALID-1.
  `location`: `docs/architecture/evidence_defeaters.md#gov-defeat-1` (new stub).

Evidence seed, measured at registration:
- No summary surface reads open flags.
- Resolved `evidence_discrepancy` flags were open for median 3.3d, p90 8.9d, max 26.5d (n=201).
- GFLAG-0250 -> 0452: 19 of 22 load-bearing `supports` PASSes were defective. The flag was open 14
  days before the status moves (MECH-302/288/287/092 provisional -> candidate; MECH-033 active ->
  provisional).
- GFLAG-0245: a byte-identical duplicate was counted as two supports for MECH-033 for 14 days.
- Live now: GFLAG-0453 against ARC-065 (`stable`, `confirmed_established`); GFLAG-0454 against
  811a -> MECH-477.

Bounding cost case: GFLAG-0197 (open 16 days, then found already discharged with no counted edge).
A claim-level join would have shown SD-025 as contested with no cause. That argues for edge-level
keying and for "open, unadjudicated" wording rather than "defeated".

Nothing else registered: every other thread is owned (sec 2).

## 7. Next steps

1. **Mechanise GOV-DEFEAT-1 cheaply before judging it.** Claim-level MVP: carry open flags into
   `claims.json` and the claim page, and name them beside lead claims in CURRENT_FRONT / insights
   and the governance promotion agenda. An optional `--run-id` on `governance_flag.py raise` adds
   edge-level keying. Kill condition, from the thought's own falsifier 4: if after >= 3 governance
   cycles the display never changes a promotion, a summary sentence or a flag's resolution
   priority, demote GOV-DEFEAT-1 toward superseded.
2. **Literature, before hardening GOV-DEFEAT-1.** Bloomfield & Rushby 2020 (arXiv:2004.10474,
   "Assurance 2.0", indefeasibility/defeaters) is already cited in
   `developmental_governance_review.md`, but this pass did NOT re-verify it. OMG SACM is cited by
   the raw thought and was also not verified.
3. **GOV-ECOL-1 amendment, trigger-conditioned.** When the functional-organism P4 assay is
   confirmed PASS, propose to `/governance` that the frozen assay be re-run at every major
   integration wave, with a regression recorded as a D6 finding. Carry the thought's falsifier 6
   (brittle regression targets) with it. Until then, nothing to do.
4. **Engineering follow-ons** (ranked in the drafting file). Workset `in_flight` derivation;
   null-regeneration canary; stale EXP-ephemeral text in the workset generator; running the
   2026-07-31 causal-realisation pilot; a lease fencing epoch (orchestrator-owned); no EIG score
   and no unified event ledger for now.
5. **V5 ethical-assay design checklist.** Sec 11's five alternatives (heuristic fired / reward
   landscape / external veto / other never consulted / consumer ignored the signal) should be
   the control set for any future "ethical representation is causally operative" assay. Hand this
   to the loveability/ethical-agency plan owner. No claim; SENT-17 owns the principle.
6. Raw thought marked `Status: processed` with this intake linked.
