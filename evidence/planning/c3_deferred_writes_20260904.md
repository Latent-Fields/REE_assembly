# Campaign C3 — deferred registry writes and hand-backs (2026-09-04)

**Session:** `campaign-c3-20260904` (Mac, `DLAPTOP`), chip `chip-20260904-campaign-c3-unblockers`.
**Plan of record:** [`science_wave_campaign_plan_20260904.md`](science_wave_campaign_plan_20260904.md) section C3.

## Why this document exists

`/governance` session `governance-20260904-1347` held an exact-file pause for the whole of
this session on `REE_assembly/evidence/planning/substrate_queue.json`,
`REE_assembly/docs/claims/claims.yaml`, `ree-v3/experiment_queue.json` and
`experiment_proposals.v1.json`. `task_claim.py open` arbitrates on those files and returns
exit 3, and a stop is binding. Everything below is content this session **drafted and
verified but did not write**, recorded here so it is applied rather than lost. Nothing was
forced through a lock.

Two of the three campaign items turned out not to need the write they were commissioned for.
That is the substantive finding of this session and it is written up first.

---

## Item 1 — ContextMemory write-path validation: **STOPPED, do not queue**

`chip-20260904-contextmemory-writepath-validation`. Commissioned to queue, via
`/queue-experiment`, the ablation that substrate entry
`contextmemory-write-path-addressing-degeneracy` names in its own `validation_experiment`
field: flag ON vs OFF for both mechanisms (conscience bias and refractory), DV
`n_occupied_slots` in `ContextMemory.write()`, target `>= 2` occupied slots in both arms on
`>= 3/5` seeds, `experiment_purpose: diagnostic`.

**That experiment has already run, and it passed.**

| Run | Date | What it measured |
|---|---|---|
| **V3-EXQ-943** `v3_exq_943_contextmemory_write_selection_validation` (`run_role: validation`) | 2026-08-20 | "C1 occupancy floor MET: BIAS 16/16 occupied 5/5 seeds (round-robin 0.993-0.996, entropy ~4.0, self_repeat 0); REFRACTORY occupied 6/3/3/3/9, 5/5 seeds >=2 (lock seeds at exactly k+1=3); **LEGACY still 2/5** with seeds 7/13/100 locked. P0 min writes 2933." |
| **V3-EXQ-436g** `..._bias_writesel_ceiling_retest` | 2026-08-30 | "ADDRESSING half CONFIRMED FIXED: 16/16 occupied slots in every non-NO_WRITES cell on 5/5 seeds, transfer to this driver's own config confirmed by the new `bias_occupancy_confirms_fix` P0 gate." |

That is a flag-ON (bias), flag-ON (refractory), flag-OFF (legacy) ablation on
`n_occupied_slots` against the `>= 2 on >= 3/5 seeds` target — an exact match for the
commissioned design. It was autopsied as
`failure_autopsy_V3-EXQ-943_2026-08-21.json`, and the same substrate entry already records
the result in its `validation_record_943` and `governance_2026_08_30` fields.

**Why the campaign asked for a duplicate.** The entry's free-text `validation_experiment`
field is stale. It still reads "PENDING for BOTH mechanisms … not yet queued", three fields
above `validation_record_943`, which says the opposite. The campaign plan was written from
the stale field.

**Action taken:** no experiment queued. Raised **GFLAG-0132** (`stale_note`; ARC-045,
SD-017, MECH-166) — REE_assembly `35ae14089d`.

**Still owed, both genuinely governance's:**

1. Correct the `validation_experiment` field to name V3-EXQ-943 + V3-EXQ-436g.
2. **The human call this entry has been explicitly waiting on.** `validation_record_943`
   says, verbatim: *"Leave the 436f failure_record `resolved:open` until a human decides
   whether that occupancy result closes the corrupting 1-slot-bank defect."* That decision —
   not a missing experiment — is what gates `implemented_pending_validation ->
   implemented_validated`, and therefore what releases IGW-20260904-226/227 (ARC-045 retest)
   and GFLAG-0044. The 2026-08-26 HUMAN DECISION already recorded in the entry pulls the
   other way (both mechanisms are "mechanical occupancy workarounds", not a content-based
   write-selection policy), so this is a real decision with evidence on both sides, not a
   formality.

**Do NOT queue V3-EXQ-939** off the back of this. The entry states directly that the
`gumbel_learned` build "Does NOT unblock chip-20260814-queue-causal-sleep-matched-arm or
chip-20260818-mech152-redesign-queue-gated". The content half remains open (V3-EXQ-956
failed content discrimination; the H1–H4 portfolio V3-EXQ-969/970/971/972 all returned
methodological failures on 2026-09-02).

**Separate live finding, worth more than the above.** The validated fix is default-off and
non-contextmemory drivers still hit the defect: **V3-EXQ-994** (2026-09-03, EXT-007 claim
probe) measured `n_encode_written_slots = 1, 1, 16` across three seeds under the default
`contextmemory_write_selection=argmin`. The corrupting 1-slot bank is still reaching fresh
evidence, one day before this campaign was planned, because nothing makes a driver author
aware they must set the flag. Recorded in GFLAG-0132.

---

## Item 2 — SD-WAYPOINT-FIELD: landed, one registry write deferred

Code, contracts and documentation **landed** on `ree-v3` `main` (see the session's
WORKSPACE_STATE line for the sha) and the design doc
[`sd_waypoint_proximity_field.md`](../../docs/architecture/sd_waypoint_proximity_field.md)
is on `master`. Named SDs carry no `claims.yaml` entry in this repo (all 110 SD claim
entries are numeric; `SD-MEL-PRODUCER`, `SD-ORIENTING-DECISION-SCALE` etc. have none), so
**no claims.yaml write is owed** — the named id was chosen partly for that reason, and
partly to avoid racing governance for a numeric id while `claims.yaml` was locked.

**Deferred:** the `substrate_queue.json` entry. Drafted in full, schema-checked against the
live file, and ready to append verbatim at
`_scratch/c3/sd_waypoint_field_substrate_entry.json` — reproduced here so it survives the
scratchpad:

- `sd_id`: `waypoint-proximity-field-observable`
- `node_class`: `complicated (buildable)` · `status`: `implemented_pending_validation` ·
  `status_phase`: `validation_owed` · `ready`: `false`
- `severity`: `corrupting`. Any subgoal_mode experiment whose DV depends on goal-directed
  navigation returns a well-formed null while the agent is provably unable to perceive its
  target: nothing errors, the manifest is complete, and the result reads as a genuine "this
  mechanism has no effect on goal maintenance" finding. V3-EXQ-977 is the confirmed instance.
- `unblocks_claims`: `INV-086`, `MECH-428`
- `substrate_paths`: `ree_core/environment/causal_grid_world.py::CausalGridWorld._get_observation_dict`
- `failure_record`: the V3-EXQ-977 probe (0/0/1 waypoints visited, 0 sequences completed,
  seeds 42/43/44), target `>= 1 sequence completed by the agent's own unscripted policy on
  >= 2 of 3 seeds`.

**Validation experiment** could not be queued (`experiment_queue.json` locked). Chipped as
`chip-20260904-waypoint-field-validation`, which also carries the substrate_queue append
above as a secondary deliverable. Its design, and the three traps a driver author must
avoid, are in the "Validation" section of the SD doc.

---

## Item 3 — Unowned substrate blockers: **1 entry owed, not 13**

`chip-20260902-unowned-substrate-blockers`. The audit
(`scripts/audit_blocked_proposal_unblockers.py --bucket UNOWNED`) reports **29 blocked
proposals naming 37 distinct unowned blockers** as of 2026-09-04 (the chip was written
against a 13-of-19 measurement from 2026-09-02).

Cross-checking every blocker against four sources the audit script cannot see — open chips,
plan-of-record docs under `evidence/planning/`, `claims.yaml` phase and "DO NOT build"
notes, and `substrate_queue.json` entries whose free-prose `blocked_by` text its matcher
cannot resolve — collapses 37 to:

| Disposition | Count | Meaning |
|---|---|---|
| **DRAFT-ENTRY** | **1** | genuinely unowned and buildable: **MECH-054** |
| **GOVERNANCE-ROUTE** | 3 | done this session — GFLAG-0133/0134/0135 |
| **LEAVE-TO-CHIP** | 16 (+1 partial) | already covered by an open chip |
| **NO-ACTION** | 13 | correctly owned or phase-deferred elsewhere |
| **UNCERTAIN** | 3 | ARC-053, ARC-054, `no_meta_agent_benchmark_harness` |

**The audit over-reports, and this is the reusable finding.** It checks only
`substrate_queue.json`, so it cannot see (a) an open chip naming the same blocker in
different words, (b) a live plan-of-record doc already tracking it as a governance-reviewed
thread, (c) a `claims.yaml` note saying "DO NOT build in V3" or `implementation_phase: v5`,
or (d) a free-prose `blocked_by` string it cannot resolve to an existing `sd_id`. The
single most consequential correction: `chip-20260903-arc120-framing-evidence-tagging`
reclassifies six blockers at once (the ARC-120 family) from "unowned build" to
"already-chipped evidence tagging".

### Governance routings — **applied this session**

| Flag | Claims | Type | Finding |
|---|---|---|---|
| **GFLAG-0133** (`4b0f3f9f11`) | ARC-007, MECH-151 | `contested_disposition` | The build is not unowned — `mech151-action-bias-has-no-e3-ranking-channel` exists with status `proposed_GATED_on_ARC-007_governance_decision_DO_NOT_BUILD_YET` since 2026-08-18. The *decision* is unowned: `claims.yaml` ARC-007 is `provisional` with **empty notes**. Needs the entry's own A-or-B call. |
| **GFLAG-0134** (`142e2276ac`) | ARC-130 | `contested_disposition` | ARC-130's notes record the reach-stage instrumentation schema as "an UNBUILT instrumentation proposal … not authorised", so it cannot be adopted as an ordinary build. EXP-1344's `blocked_note` says the claim's testable core is already demonstrated (V3-EXQ-931 + three convergent instances) and the owed action is `/claim-synthesis` tagging — for which **no chip exists**. |
| **GFLAG-0135** (`2ae80ccb22`) | MECH-343 | `stale_note` | **Audit false negative.** EXP-0176's blocked_by prose says the regulator is "not yet designed (no design doc)", but `SD-061` already covers it (`implemented_pending_validation`, `unblocks_claims: [MECH-343, Q-056]`). Do not mint a duplicate. |

### The one entry still owed: MECH-054

Genuinely unowned and buildable — signed harm/benefit precision channels, design already
sketched in `docs/architecture/precision_control.md`, zero implementation (grep-confirmed).
Blocks EXP-0793 and LIT-0794 (MECH-043). A drafted entry in the live file's schema is at
`_scratch/c3/item3_draft_entries.json`; it must be appended with `status: proposed` and
`ready: false` — **proposed, not build-authorised**.

**Verification owed when it is applied** (the audit's own instruction): re-run
`audit_blocked_proposal_unblockers.py --bucket UNOWNED` and confirm EXP-0793 / LIT-0794 move
UNOWNED -> **OWNED**, not READY. If either moves to READY the status was mis-set.

### Uncertain — flagged rather than guessed

- **ARC-053 / ARC-054** (blocking EXP-0465, ARC-055). Both `candidate`,
  `implementation_phase: v3` — genuinely V3-scoped, not deferred. But their `claims.yaml`
  notes are conceptual/formal rather than implementation-level (ARC-053: a distributed
  Temporal Coherence Loop; ARC-054: a formal rollout-evaluation criterion
  `J(pi) = sum gamma^k V_hat_pi(t+k)`), and neither has the staged plan its dependent
  ARC-055 already carries. Minting ordinary backlog entries without a grounded
  `implementation_hint` would misrepresent them as routine builds. **Recommend** a scoping
  read of the relevant `ree_core/` modules, or a governance call on whether these warrant
  their own design pass first.
- **`no_meta_agent_benchmark_harness`** (blocking EXP-0525 / EXP-EXT008-EVAL-BOUNDARY,
  EXT-008). Q-069's notes say "the right response is to build the harness" but also, in the
  same breath, "Off the V3 / GAP-7 critical path; this is an outer-assembly-process
  question. DO NOT queue a V3 experiment against it." The harness is meta-tooling about
  REE's own research process, not a `ree_core` substrate change, and every
  `substrate_queue.json` entry read is scoped to `ree_core`. **Recommend** a governance call
  on where this is tracked at all, before an entry is drafted either way.

### One residual gap found in passing

`goal_pipeline:GAP-2` (blocking EXP-0710, INV-086) names three sub-builds. Two are chipped —
waypoint proximity field (item 2 of this campaign, landed) and
`chip-20260902-zgoal-parent-e3-consumer` (open). The third, **"benefit/wanting-driven
residue-centre allocation" for the VALENCE_WANTING write path, has no chip and no entry**.
Not drafted here; it needs its own ResidueField / harm_signal investigation.

---

## Provenance

Governance flags raised this session: GFLAG-0132 (`35ae14089d`), GFLAG-0133 (`4b0f3f9f11`),
GFLAG-0134 (`142e2276ac`), GFLAG-0135 (`2ae80ccb22`). Chips minted:
`chip-20260904-waypoint-field-validation`, `chip-20260904-fromdims-drop-wantingweight-997`.

**Unrelated trunk finding, chipped:** a full `ree-v3` suite run on the hub against `8f88b89`
returned 1 failed / 5596 passed / 28 skipped / 215 subtests in 26m57s. The failure —
`test_from_dims_flag_reachability.py::test_no_unregistered_from_dims_drop_site`, on
`wanting_weight` in `v3_exq_997_mech162_zresource_zworld_planning_reconvergence.py` — is
**pre-existing on `origin/main`** (driver committed `8d53fdb` by `daily-science-20260903`)
and unrelated to this session's change. It means an arm that looks ablated may be identical
to its control, so it carries a possible evidence-validity consequence for MECH-162.
Chipped as `chip-20260904-fromdims-drop-wantingweight-997`.
