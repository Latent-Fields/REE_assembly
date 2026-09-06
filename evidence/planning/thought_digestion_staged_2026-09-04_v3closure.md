# STAGED (not applied): `/thought-digestion v3-closure` -- 2026-09-04 unattended campaign

**Status: APPLIED 2026-09-06T19:27:10Z (session `thought-digestion-v3-20260904-apply`).** The user reviewed all 21 groups on 2026-09-06 and approved every draft as written; all 47 `what_would_answer` fields, the epistemic_category changes, 7 `digestion_note`s, the depends_on / related_claims / source edits and 23 proposals (EXP-1379..EXP-1401) were applied to `claims.yaml` / `manual_proposals.v1.json`, and the governance flags below were raised via `governance_flag.py`. This file is now the archival record of the drafts; the registry is authoritative.

~~**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`.**~~

**Started:** 2026-09-04T21:02:59Z · **Session:** `thought-digestion-v3-20260904` (Mac, main checkout, no worktree)
**Mode:** unattended / staged-for-review, GROUPED (wave-of-groups, edge-first, `cap=5 floor=3.0`, lettered
families atomic, a group edge must include at least one STRUCTURAL signal -- token overlap alone never
reaches the floor). Draft-only: every wave's agent output is appended here verbatim; the user reviews the
whole batch once and the orchestrator applies only what is approved, then `build_claims_json.py` + commit.

**Deviation from the skill, stated plainly:** the skill's generic "Unattended / overnight mode" says to
stage to an untracked scratch file. This campaign stages to THIS tracked file instead, committed
pathspec-limited under the session's own TASK_CLAIMS entry, because untracked staging was lost once before
(chip-20260807-thoughtdigestion-trial-5: worktree GC'd before the drafts were read). The pattern follows
`thought_digestion_staged_2026-08-08_trial2_5claims.md`.

**Scope:** `closure_status.md` "Remaining work to close v3" (33) + "Assembly frontier" (10) -> 41 core
claim ids, expanded one hop along `depends_on` (240), intersected with the undigested backlog
(no `what_would_answer`, no `digestion_note`, `implementation_phase` not in v4/v5/v6/post_v5), plus
lettered-family closure -> **47 claims in 21 groups (10 solos)**. Wave 1 of 2026-08-27 (17 claims,
REE_assembly 25c05dbd6e) is already applied and therefore excluded.

**Prior drafts found and handed to agents (extract-before-invent):** MECH-485 (loop branch
`thought-loop/digestion-2026-08-25`, with the user's own `human_review_note`); ARC-113 (pilot wave
`thought_digestion_v3closure_wave1_drafts_20260826.md`, never applied).

| group | members | fan-in | why grouped |
|---|---|---|---|
| G1 | MECH-181, MECH-353, MECH-354, SD-017, SD-083 | 24 | SD-017 sleep-phase hub: SD-083/MECH-354/MECH-181 all `depends_on` it; MECH-353~354 same batch + namespace |
| G2 | MECH-074, MECH-074a-d | 8 | lettered family (amygdala read/write head split) -- atomic |
| G3 | MECH-104, MECH-106, MECH-234, MECH-250, SD-105 | 2 | control-plane commitment namespace; 104->106 `depends_on`; interrupt/release/entropy-floor siblings |
| G4 | ARC-048, INV-057, MECH-182, MECH-192 | 5 | ARC-048->MECH-192 `depends_on`; signal-legibility namespace |
| G5 | ARC-120, ARC-121, SD-034 | 12 | ARC-121->SD-034 `depends_on`; earned-authority / shared epistemic state |
| G6 | MECH-294, MECH-341, MECH-442 | 11 | MECH-442 `depends_on` both; action-diversity through commit |
| G7 | MECH-206, MECH-288, SD-084 | 10 | MECH-288->SD-084 `depends_on`; hippocampal comparator / event-segment |
| G8 | ARC-057, SD-024, SD-025 | 8 | SD-024<->SD-025 and ARC-057->SD-025 `depends_on`; DA / curiosity |
| G9 | MECH-349, MECH-527 | 3 | rule-mint / attractor-escape namespace |
| G10 | ARC-061, SD-047 | 1 | ARC-061->SD-047 `depends_on`; reafference comparators |
| G11 | ARC-029, MECH-025b (+MECH-025 read-only context) | 0 | committed/uncommitted modes namespace |
| solos | MECH-273, MECH-258, MECH-485, ARC-113, ARC-037, INV-104, INV-063, MECH-332, MECH-474, SD-063 | -- | no structural edge >= floor to any other undigested claim |

---

## GOVERNANCE FLAGS (collected across waves -- read these FIRST)

**Rollup generated 2026-09-04T21:29:11Z by the orchestrator from the agent reports below (mechanical extraction; read the per-claim sections for the full text).**

Claims with a drafted disposition: **47 of 47** -- complete.

| disposition | count |
|---|---|
| (a) | 22 |
| (b) | 2 |
| (c) | 13 |
| (c2) | 2 |
| (f) | 5 |
| (g) | 3 |

### Per-claim dispositions

| claim | report | recommended disposition (first 150 chars) |
|---|---|---|
| ARC-029 | G11 | **(a) testable now** -- the blocker is instrument design, not |
| ARC-037 | S_ARC-037 | **(c) substrate-blocked -> `substrate_conditional`**, carrying (g) partial merge |
| ARC-048 | G4 | (c) substrate-blocked, `substrate_conditional` -- the falsifiable |
| ARC-057 | G8 | **(a) testable now** -- the ecological form is correctly V4-deferred, |
| ARC-061 | G10 | **(c) substrate-blocked -- `substrate_conditional`** (NOT `substrate_ceiling`): the family claim's distinctive content is the *cross-level* shared sig |
| ARC-113 | S_ARC-113 | **(f) defer with a durable `digestion_note`** -- the pilot's call stands, but for a *different and narrower* reason than the pilot gave: the stage-imp |
| ARC-120 | G5 | **(b) derivational** -- its falsification condition is a standing |
| ARC-121 | G5 | **(b) derivational** -- ARC-121's own stated falsifier is about REE's |
| INV-057 | G4 | (c2) `out_of_domain` -- this is a **fused** claim whose evidential leg |
| INV-063 | S_INV-063 | (a) testable now -- the intake ladder (SD-MEL-PRODUCER `world_rule_shift`, |
| INV-104 | S_INV-104 | **(a) testable now**, narrowed to a **class-1 pilot with class 2 as the |
| MECH-025b | G11 | **(a) testable now** -- the mechanism is live, both positive |
| MECH-074 | G2 | (a) testable now -- the parent is **not** a pure index: it owns the two-route-separability assertion, 888 confirmed it on the replay-sampling path at  |
| MECH-074a | G2 | (a) testable now -- the claim's own registered falsifier has a **two-sided** form ("threat-context recall improves ... OR neutral recall is harmed") a |
| MECH-074b | G2 | (a) testable now, on a **narrowed** residual -- 888 already answered the "the address route has independent authority and is not scalar-equivalent" le |
| MECH-074c | G2 | (c) substrate-blocked -- **`substrate_conditional`**, blocking substrate = the **SD-011 AffectiveHarmEncoder magnitude regime** (`//LowFreq(z_harm_a)/ |
| MECH-074d | G2 | (c) substrate-blocked -- **`substrate_conditional`**, blocking substrate = **MECH-153's supervised context-labeling objective** (unbuilt) over the SD- |
| MECH-104 | G3 | **(a) testable now** -- the *endogenous* half of the claim is |
| MECH-106 | G3 | **(c) substrate-blocked -- `substrate_conditional`**, blocking substrate |
| MECH-181 | G1 | **(c2) out_of_domain -- the claim is FUSED, and should be SPLIT**; the |
| MECH-182 | G4 | (c) substrate-blocked, `substrate_conditional` -- but with the most |
| MECH-192 | G4 | (g) **merge with sibling -- PROPOSE ONLY: PARTIAL absorption into |
| MECH-206 | G7 | **(c) substrate-blocked -- `substrate_conditional`** (not |
| MECH-234 | G3 | **(c) substrate-blocked -- `substrate_conditional`**, reframed onto the |
| MECH-250 | G3 | **(g) merge with sibling -- PROPOSE ONLY: partial absorption into |
| MECH-258 | S_MECH-258 | (c) substrate-blocked, **`substrate_ceiling`** -- the mechanism is BUILT and has been EXERCISED repeatedly under gates that pass cleanly (597b C0 3/3  |
| MECH-273 | S_MECH-273 | **(a) testable now** -- the sleep half is BUILT, EXERCISED, and confirmed non-degenerate with a genuine zero-movement OFF arm (V3-EXQ-702), yet neithe |
| MECH-288 | G7 | **(a) testable now** -- the substrate is built, live in-agent, and |
| MECH-294 | G6 | **(a) testable now** -- the V3 leg has a validated driver and a landed |
| MECH-332 | S_MECH-332 | (a) testable now -- both pathways are BUILT in `ree_core/` and the 2x2 falsifier is already pre-registered in `experiments/v3_exq_878_mech332_efferenc |
| MECH-341 | G6 | **(a) testable now** -- the claim is ratified `provisional` at a scope |
| MECH-349 | G9 | **(a) testable now** -- the module is built, default-OFF but armable, |
| MECH-353 | G1 | **(a) testable now** -- the substrate is built, calibrated and |
| MECH-354 | G1 | **(c) substrate-blocked, `substrate_conditional`** -- the two-bound |
| MECH-442 | G6 | **(f) defer, with a durable `digestion_note`** -- the claim's mechanism |
| MECH-474 | S_MECH-474 | (f) defer with a durable `digestion_note` -- the claim's own registered four-regime menu contains one regime ("counterfactual simulation") that has no |
| MECH-485 | S_MECH-485 | **(c) substrate-blocked -- `substrate_conditional`**, unchanged. The mechanism has never been exercised because three of its five preconditions still  |
| MECH-527 | G9 | **(g) merge with sibling -- PROPOSE ONLY** (partial absorption into |
| SD-017 | G1 | (c) substrate-blocked, **`substrate_ceiling` -- UNCHANGED and correct** |
| SD-024 | G8 | **(a) testable now** -- and note that the *core* falsifier has already |
| SD-025 | G8 | **(a) testable now** -- the drive's *propagation* is validated in vitro |
| SD-034 | G5 | **(a) testable now** -- the umbrella's OWN primary falsifier (is closure |
| SD-047 | G10 | **(f) defer -- with a durable `digestion_note`, and specifically NOT a new experiment.** The falsifier does not need drafting or running: SD-047 pre-r |
| SD-063 | S_SD-063 | (a) testable now -- the head is BUILT, trainable, demonstrably live (relative |
| SD-083 | G1 | **(a) testable now -- and legs (i)-(iii) are ALREADY ANSWERED CONFIRMING by |
| SD-084 | G7 | **(a) testable now** -- with the important qualification that the |
| SD-105 | G3 | **(f) defer with a durable `digestion_note`** -- the claim was |

### Governance flags extracted (74 lines; some reports list several per claim)

| report | claim | flag |
|---|---|---|
| G1 | SD-017 | `stale_note` -- SD-017's `evidence_quality_note` closes on 2026-08-30 with |
| G1 | MECH-181 | `stale_note` -- the standing "INV-050 / MECH-180 MEL producer is parked / blocked" |
| G1 | MECH-353 | `evidence_discrepancy` -- V3-EXQ-642b's own manifest already contains the deciding |
| G1 | MECH-354 | `contested_disposition` -- MECH-354 is registered `candidate` with |
| G1 | SD-083 |  |
| G10 | ARC-061 | `stale_note` -- see GOVERNANCE FLAG 3 and GOVERNANCE FLAG 5 below. |
| G10 | SD-047 | the block records a supports/PASS while the index scores a weakens, and the two have disagreed in sign since 2026-05-04.** |
| G11 | ARC-029 | `evidence_discrepancy` -- **ARC-029's `provisional` status rests |
| G11 | ARC-029 | `stale_note` -- **two routing notes in ARC-029's own |
| G11 | ARC-029 | `contested_disposition` -- **ARC-029 has no explicit |
| G11 | MECH-025b | `evidence_discrepancy` -- **the 2026-08-03 `weakens/standard` |
| G11 | MECH-025b | `evidence_discrepancy` (minor, registry/index disagreement) -- |
| G2 | MECH-074 | `stale_note` -- MECH-074 still carries `v3_pending: true` and a `live_status.evidence` of `decision:...@2026-04-25 hold_pending_v3_substrate/applied`, while its two stated release conditions (substrate lands; EXQ-A/B-equ |
| G2 | MECH-074a | `stale_note` -- the `evidence_quality_note` asserts "this is the first [experimental entry]" and `exp_conf now 0.775`; there are now two entries (659, 888) and `exp_conf` is 0.755. The promotion gate is still unmet so st |
| G2 | MECH-074b |  |
| G2 | MECH-074c |  |
| G2 | MECH-074d |  |
| G3 | MECH-104 | `stale_note` -- MECH-104's `status_note` stops at EXQ-365 (2026-04-14) and omits |
| G3 | MECH-104 | `evidence_discrepancy` -- MECH-104's `active` status rests on a conjunction |
| G3 | MECH-106 | `evidence_discrepancy` -- MECH-106 is `provisional` on a single non-excluded |
| G3 | MECH-106 | `contested_disposition` -- MECH-106 and SD-011 (`status: stable`) make |
| G3 | MECH-234 | `contested_disposition` -- MECH-234 has sat at `candidate` since 2026-04-15 with |
| G3 | MECH-250 | `stale_note` (concerns MECH-108, surfaced via MECH-250's dependency) -- |
| G3 | SD-105 | `contested_disposition` -- SD-105 was registered 2026-09-04 asserting the |
| G3 | SD-105 | `stale_note` -- `evidence/planning/substrate_queue.json`, |
| G4 | - | The 2026-04-05/06 "Steve" cohort (MECH-182, MECH-192, |
| G4 | - | `fast_empathy_v5_plan.md`'s 2026-06-10 decision-log entry |
| G4 | - | The 2026-04-06 intake's Next Step 4 (social.md stubs for |
| G4 | ARC-048 | `stale_note` -- ARC-048 is registered as the pre-linguistic bridge to INV-003 |
| G4 | INV-057 | `contested_disposition` -- INV-057 is `claim_type: invariant` / |
| G4 | MECH-182 | `stale_note` -- MECH-182's registered mechanism ("this cross-modal |
| G4 | MECH-192 | `contested_disposition` -- MECH-192 as registered is near-analytic and its |
| G5 | SD-034 | `evidence_discrepancy` -- **V3-EXQ-466e (PASS, `{SD-034: supports}`, |
| G5 | SD-034 | `stale_note` -- SD-034's `implementation_note` records "616 LOC" and two |
| G5 | SD-034 | `stale_note` -- two flags on this claim are now decidable and should be closed |
| G5 | ARC-120 | `promotion_review` -- **ARC-120 carries `exp_count 0` while pre-existing, |
| G5 | ARC-120 | `stale_note` -- ARC-120 acquired a 5-entry literature pull on **2026-09-02** |
| G5 | ARC-121 | `contested_disposition` -- **ARC-121 is a FUSED claim and its literature pull is |
| G5 | ARC-121 | `evidence_discrepancy` -- ARC-121 declares MECH-482 as a dependency and as an |
| G6 | MECH-294 | `evidence_discrepancy` -- **V3-EXQ-840b, MECH-294's sole genuine experimental |
| G6 | MECH-294 | `stale_note` -- `evidence/planning/substrate_queue.json` entry |
| G6 | MECH-341 | `stale_note` -- `evidence/planning/substrate_queue.json` entry `sd_id: MECH-341` |
| G6 | MECH-442 | `contested_disposition` -- **PARTIAL-ABSORPTION PROPOSAL (proposal only; no id |
| G6 | MECH-442 | `stale_note` -- MECH-442's `notes` assert *"substrate_conditional on a |
| G7 | MECH-206 | `contested_disposition` -- **MECH-206's functional slot has an incumbent |
| G7 | MECH-288 | `stale_note` -- **MECH-288's promotion bar is half-satisfied and the |
| G7 | MECH-288 | `evidence_discrepancy` -- **the shipped fast-scale trigger is not the |
| G7 | MECH-288 | `promotion_review` -- **evidence attribution gap.** MECH-288 sits at |
| G7 | SD-084 | `stale_note` -- **SD-084's 2026-08-10 routing block directs work that had |
| G7 | SD-084 | `promotion_review` -- **a validated design decision reads as evidence-free.** |
| G8 | ARC-057 | `stale_note` -- ARC-057's `notes` open with *"The curiosity/exploration drive |
| G8 | SD-024 |  |
| G8 | SD-025 |  |
| G9 | MECH-349 | `evidence_discrepancy` -- MECH-349 has zero entries in |
| G9 | MECH-349 | `stale_note` -- MECH-349's `notes` end "Validation V3-EXQ-639", but 639 is |
| G9 | MECH-527 | `stale_note` -- MECH-527's `notes` state "the above-action-level perturbation |
| G9 | MECH-527 | `contested_disposition` -- MECH-527 partially duplicates MECH-343/SD-061 with |
| G9 | MECH-527 | `promotion_review` (low priority, informational) -- V3-EXQ-694 |
| S_INV-063 | INV-063 | MECH-205's `what_would_answer` non-degeneracy precondition |
| S_INV-063 | INV-063 | INV-063 is a FUSED claim (testable REE leg + |
| S_INV-063 | INV-063 | the run designed above would supply, as a by-product, |
| S_INV-063 | INV-063 | two coverage gaps found in the sleep plan-of-record. |
| S_INV-104 | INV-104 | `REE_assembly/evidence/planning/substrate_queue.json`, |
| S_INV-104 | INV-104 | INV-104's own `notes` cite "MECH-100 / SD-009 (event-type CE |
| S_INV-104 | INV-104 | INV-104 carries a single |
| S_MECH-258 | MECH-258 | `stale_note` -- MECH-258's `evidence_quality_note` and `live_status.evidence` are two adjudications behind. They record only "[2026-05-08 governance]: EXQ-445h supports (C1 wins=2/3 seeds) ... First clean supporting evid |
| S_MECH-258 | MECH-258 | `contested_disposition` -- V3-EXQ-597c was routed by a **confirmed** failure autopsy on 2026-05-24 (`/queue-experiment -> V3-EXQ-597c`, with a two-fix redesign spec: raise `dacc_bias_max_abs` to 20.0; per-component telem |
| S_MECH-258 | MECH-258 | `evidence_discrepancy` -- the "harm_a forward R2 = 0.94-0.99 / 0.91-0.94" figure is cited on MECH-258 (and in the 445h substrate_queue metric) as supporting evidence, but on a target measured to be range-degenerate (SD-0 |
| S_MECH-258 | MECH-258 | `contested_disposition` (low priority) -- MECH-259 is `stable` on `genuine_exp_count: 1` (V3-EXQ-455, exp_conf 0.575) while the `depends_on` edge it declares to MECH-258 ("the magnitude compared against threshold") has n |
| S_MECH-485 | MECH-485 | `evidence_discrepancy` |
| S_MECH-485 | MECH-485 | `stale_note` |
| S_SD-063 | SD-063 | `evidence_discrepancy` -- **SD-063 was promoted to `provisional` on evidence that |
| S_SD-063 | SD-063 | `evidence_discrepancy` -- **fresh, reviewed, unrouted calibration evidence.** |
| S_SD-063 | SD-063 | `stale_note` -- **`evidence/planning/substrate_queue.json` SD-063 entry (line 6317) |

**Cross-cutting findings the orchestrator wants the reviewer to see first:**

1. **Reviewed evidence that never propagated into the registry** recurs in G1 (SD-083 telemetry), G5 (V3-EXQ-466e absent), G8 (SD-024 promotion), G10 (SD-047's own falsifier fired 2026-05-04), S_MECH-485 (2026-08-09 governance note claims an application that never happened; Q-090's live falsifier dangles), S_MECH-332 (GAP-11 done since May).
2. **Dead ablation axes / knobs that are live but not efficacious**: S_MECH-332 (`harm_descending_mod_enabled` silently swallowed by `from_dims`, ARM_BOTH bit-identical to ARM_E2_ONLY), G8 (fishtank family sets `curiosity_weight` but never `benefit_terrain_live_producer`, so SD-025's bonus is identically 0.0), G1 (SD-083 retention flat across a 14x penalty), G6 (all MECH-294/341 nulls measured at the 2-of-5 class clamp), G7 (`agent.py:5448` passes `pe_dict=None`, so MECH-288's observation path runs the fallback detector).
3. **Merge proposals (g), propose-only, route to /governance**: MECH-192 -> MECH-191/183 (G4); MECH-250 -> MECH-108 (G3); MECH-527 -> MECH-343/SD-061 (G9); MECH-354 slow leg -> SD-SLEEP-ENTRY-PRESSURE (G1); MECH-474 -> MECH-261 SalienceCoordinator (S_MECH-474); ARC-120 ladder -> ARC-130 (G5); MECH-442 partial absorption (G6); ARC-037 legs -> MECH-256/MECH-072 (S_ARC-037).
4. **Standing project-memory corrections**: the MEL producer is validated (V3-EXQ-798a, 2026-07-30), not parked (G1, S_INV-063); ARC-120/ARC-121 originate from the 2026-08-06 thought, not the 2026-08-27 intake (G5).
5. **Never arm together**: SD-105 couples to MECH-104/106/234/250 through `last_precommit_probs` (G3); SD-105 manufactures the DV that MECH-294/341/442 read out (G6).


---

## GROUP REPORTS (appended as they land; verbatim agent output)

---

<!-- G2 appended 2026-09-04T21:17:34Z -->
## G2 -- MECH-074 lettered family (amygdala as read/write head for the valenced hippocampal map)  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the group brief says a lettered family is atomic and that the key question is whether the parent MECH-074 is now a pure index. **My view: it is NOT.** The parent carries a residual assertion of its own -- that the head's authority over the hippocampal map *decomposes into two independently sufficient routes* (write-STRENGTH and write-ADDRESS) -- and that assertion has been directly tested. `V3-EXQ-888` (2026-08-04, PASS/supports, 3/3 seeds, non-degenerate) registers `C1_head_authority` and `C4_separability` against **MECH-074 itself**, with `C3` alone against MECH-074a and `C2` alone against MECH-074b (`evidence/experiments/v3_exq_888_mech074_readwrite_head_route_dissociation_20260804T075257Z_v3.json`, `criteria[].claim`; `combination_rule`: "C4 (separability) is the load-bearing criterion for the PARENT claim MECH-074"). So disposition (e)/(g) is **wrong** for the parent: it has its own falsifier, its own criteria, and `claim_evidence.v1.json` gives it `genuine_exp_count: 1, exp_conf 0.705, evidence_quadrant confirmed_established`. What it does *not* have is any residual role as an evidence router -- the routing job named in its `evidence_quality_note` is done.

- **(i) same-claim / merge candidates:** **none.** MECH-074a and MECH-074b were the plausible merge pair (both are "BLA biases which traces win"), and the merge is empirically refuted rather than merely judged unlikely: 888's four-arm design isolates them (`ARM_TAG_OFF` = arousal tag off, encoding gain live -> strength route only -> MECH-074a; `ARM_GAIN_FLAT` = gain flattened, per-trace tags live -> address route only -> MECH-074b) and **both single-route arms independently clear the margin on 3/3 seeds** (address-route delta vs OFF 0.1506 / 0.0909 / 0.1061; strength-route delta vs OFF 0.3249 / 0.1769 / 0.2491; margin 0.03; OFF arm flat, |AOR_z| <= 0.0107). Two routes, separately sufficient -- do not merge. MECH-074c is a different module (CeAAnalog, scalar/fast) and MECH-074d a different operation (remap), no merge pressure. The one *outward* merge pressure worth naming is MECH-074d <-> **MECH-153** (see (iv)), and it is a dependency, not a merge.

- **(ii) contradictions / undercut premises:**
  1. **MECH-074b's own load-bearing literature now partially undercuts its locus.** A targeted review landed 2026-08-07 (`evidence/literature/targeted_review_mech_074b/`, 4 entries, none of them in the claim's `source` list) and one entry is scored **mixed/weakening**: Roozendaal & McGaugh 2011 -- "the best-established amygdala memory effect is on CONSOLIDATION ... at RETRIEVAL the amygdala/glucocorticoid effect is documented as IMPAIRING, not a positive per-trace enhancement" (`entries/2026-08-07_mech_074b_consolidation_vs_retrieval_roozendaal2011/record.json`, confidence 0.62). That is a locus dispute *between MECH-074b and MECH-074a*: the same paper is MECH-074a's top citation and supports it. It does not refute 074b (888 shows the address route has real in-substrate authority), but 074b's registered claim of a *retrieval-time* per-trace weight now carries a named literature cost that its block does not record.
  2. **MECH-074b's premise depends on MECH-074a's write path.** `w_i = 1 + alpha * arousal_tag_i` is undefined if the encoding-time tag is never written (`bla_retrieval_tag_at_encoding`, default True, exposed as False specifically to reproduce the named scalar-failure signature -- `ree_core/amygdala/bla.py:187-191`). A 074b null is uninterpretable unless the tag-write precondition is reported green; 888 reports it as `address_route_nonuniform` (retrieval_bias range 0.429 vs floor 0.01).
  3. **MECH-074c's selectivity leg is undercut by its own substrate.** `CeAAnalog.tick()` is a pure function of `||LowFreq(z_harm_a)||_1 / n` (`ree_core/amygdala/cea.py`, "Selectivity constraint" docstring: "because z_harm_a is the SD-011 affective stream, magnitude there IS affective valence load"). So "must fire on harm-affective valence, not generic arousal" cannot be a property of this module -- a magnitude-matched non-harm drive fires identically **by arithmetic**. V3-EXQ-895 recorded exactly this (`interpretation.selectivity_leg.why_not_gated`, DV-symmetry artifact class). MECH-074c is therefore a **fused claim**: legs 1-2 + fast:slow are REE/CeA legs; leg 3 is an SD-011 encoder leg wearing a CeA label.

- **(iii) shared falsifier:** **yes -- V3-EXQ-888's route-dissociation instrument is the family's shared falsification apparatus for the parent, 074a and 074b, and its precondition block should be cross-referenced rather than re-derived.** The five readiness gates are: `n_traces_sufficient` (>= 8; measured 40), `gt_arousal_spread` (buffer std of the ground-truth arousal label >= 0.02; measured 0.067-0.097 -- **the single statistic every AOR routes on**, since all four AORs are differences of means of `gt_arousal`, so zero spread forces every AOR to 0 no matter how the sample is weighted), `buffer_gt_alignment` (== 1.0), `strength_route_nonuniform` (memory_strength range >= 0.05; measured 1.07), `address_route_nonuniform` (retrieval_bias range >= 0.01; measured 0.429), plus the `OFF_AOR_Z_FLAT_MAX <= 0.02` instrument control. MECH-074b's and MECH-074a's drafts below point at this block instead of restating it.

- **(iv) cross-cutting finding:** **three, and the third is the most consequential thing in this report.**
  1. *Confound now RESOLVED, and must not be re-introduced.* The strength/address confound between 074a and 074b was real (before 888, a single-arm ON/OFF result on either claim was uninterpretable because both routes move the same DV). 888's 2x2 dissolved it. **Any future 074a or 074b run must keep both single-route arms**; a two-arm ON/OFF successor would silently re-create the confound.
  2. *Confound LIVE, and it invalidates the embodied reading of MECH-074c.* In the only embodied measurement of the CeA fast route (895's non-gating `SELECTIVITY_PROBE`, 4 seeds, 2044 ticks), **`embodied_fire_count = 0` on every seed**, with `lf_harm_max = 0.216` against `cea_fast_route_threshold = 0.5`. All five of 895's gated criteria (C1-C5) therefore come from **driven/synthetic arms**; in the live loop `fast_prime` is identically zero. MECH-074c's `provisional` status rests on a mechanism that has never fired in an embodied run. This is the family's largest non-degeneracy hazard and is the first line of 074c's draft below.
  3. *MECH-074d's four-fold failure is a KNOWN, ALREADY-REGISTERED precondition failure owned by another claim.* 894c's decisive reading was that within- and cross-context Jaccard were **identical (1.0000 exactly) in 10/15 cells** -- the attribution head selects a deterministic, context-invariant target set. **MECH-153** (candidate, registered 2026-03-31) says precisely this about the input side: "without this objective, hazard-proximate and hazard-distal context vectors remain near-identical (cosine_sim approximately 1.0), leaving the MECH-150 retrieval pathway functionally silent", and adds the framing that matters here -- "**This is an implementation precondition, not a claim that MECH-150 is false.**" The signatures match (0.9999 cosine / 1.0000 Jaccard) and SD-035's own 2026-08-09 addendum already states the mechanism: "the legacy ContextMemory write path homogenises the slot bank to off-diagonal cosine 1.0000 within ~24 episodes, **which defeats ANY attribution rule**". The supervised context-labeling objective MECH-153 requires is **not built** -- no `context_label` / `supervised_context` knob exists anywhere in `ree-v3/ree_core/` (verified with `/usr/bin/grep`), and its own validation run V3-EXQ-504 returned `inconclusive`. So MECH-074d is not a claim whose mechanism failed four times; it is a claim whose *input* has never existed, tested four times.

- **Currency findings (stale notes, landed blockers, unreviewed results):**
  1. **MECH-074 parent `v3_pending: true` is STALE.** Substrate landed 2026-04-21; the parent now has a reviewed, non-degenerate experimental PASS of its own (888). Its `live_status.evidence` still reads `decision:MECH-074@2026-04-25 ... hold_pending_v3_substrate`, and its `evidence_quality_note` still says "v3_pending until BLAAnalog + CeAAnalog substrate lands". Both conditions are discharged.
  2. **888 IS reviewed** -- `review_tracker.json` carries it in **both** `reviewed_run_ids` and `discussed_experiment_dirs`. SD-035's `what_would_answer` (written in the 2026-08-07 digestion pass) still describes it as "STILL PENDING REVIEW as of this digestion pass". Stale.
  3. **MECH-074b `v3_pending: true` is STALE and its `live_status` carries NO evidence block at all**, despite 888's C2 passing 3/3 seeds against it and `claim_evidence.v1.json` giving it `pass_runs 1, exp_conf 0.705, overall 0.794, evidence_quadrant confirmed_established`. Its note's condition ("v3_pending until substrate lands and EXQ-B+ follow-up is queued") is doubly discharged.
  4. **MECH-074b's `source` list is two lit-pulls stale** -- the whole `targeted_review_mech_074b/` (4 entries, 2026-08-07: Mather 2011, Sutherland & Mather 2012, Roozendaal & McGaugh 2011 *mixed*, Adolphs 2001) is absent from the block.
  5. **MECH-074a's note says "this is the first [experimental entry]"** -- there are now **two** (V3-EXQ-659 2026-06-09, V3-EXQ-888 2026-08-04) and the quoted `exp_conf 0.775` has drifted to **0.755**. The promotion gate it names (`exp_conf >= 0.80 AND >= 4 entries`) is still unmet, so the status is right and only the note is wrong.
  6. **SD-035 `metric_trajectory` note "MECH-074b retrieval_bias hippocampal-consumer wiring deferred (substrate produces signal but HippocampalModule does not yet read)" is STALE** -- `HippocampalModule.get_exploration_arousal_tags()` and retrieval_bias-weighted sampling exist (`ree-v3/ree_core/hippocampal/module.py:2920-3021`) and are fed from `ree-v3/ree_core/agent.py:10548` and `:12567`.
  7. **SD-035's data-flow spec is WRONG about one consumer, and this bounds MECH-074b.** The spec says "E3.select (BLA retrieval_bias reweights candidate proposals)". In code the only consumers are `hippocampal.diverse_replay(...)` (gated on `replay_diversity_enabled`, MECH-165) and the REM reverse-replay pass. **`retrieval_bias` never reaches `E3.select`.** So the address route is exercised on the *replay-sampling* path only -- which is exactly what 888 could measure, and is why 888 is a composition result, not a readout result.
  8. **MECH-074c's code pointer is dead**: "urgency interrupt at ree-v3/ree_core/agent.py:869-886" now lands in the `ConditionedSafetyStore` block (agent.py has grown past 12k lines). The deferred migration into `fast_prime` is still not done.
  9. **MECH-074c's "fast:slow ratio out of scope pending SD-032c AIC comparator wiring" is STALE as to the blocker** -- `AICAnalog` exists and is constructed in the agent (`ree_core/cingulate/aic_analog.py`; `agent.py:792-803`, `aic_urgency_threshold`), emitting `aic_salience` + `urgency_signal` per tick. The comparator is now `complicated (buildable)`. The *real* blocker is finding (iv)(2): the CeA gate never fires embodied.
 10. **SD-035's 2026-08-09 addendum's "STILL OWED: the MECH-074d implementation_note in claims.yaml was NOT written" is still owed** -- MECH-074d carries no `implementation_note` field today.
 11. **MECH-074d's owed fix has a live workstream that post-dates 894c but has produced nothing scored against the claim.** `ree-v3 76cbf84` "repair ContextMemory.write() deterministic single-slot fixed point" (2026-08-19), then V3-EXQ-943 (PASS), 946 (PASS, label `context_informative_address_found_at_operating_point`), 956 (FAIL), 969/970 (FAIL, 970 = `h1_content_referencing_objective_not_confirmed_either_regime`), 971, 972 (PASS, label **`h4_supported_representation_undifferentiated`**). **Every one is `evidence_direction: non_contributory` with `claim_ids: null`** -- diagnostics, not evidence, and none tests MECH-074d. The gate is not discharged.
 12. **Nothing from this family is queued.** `ree-v3/experiment_queue.json` holds 3 items (V3-EXQ-1002, 983a, 993a); none touches MECH-074*. The family also does not appear in `docs/CURRENT_FRONT.md` or `evidence/planning/closure_status.md` -- it is off the live closure front, which is priority context for all five dispositions below.

---

### MECH-074 -- Amygdala functions as read/write head for valenced hippocampal map (parent, split into 074a-d)

**Recommended disposition:** (a) testable now -- the parent is **not** a pure index: it owns the two-route-separability assertion, 888 confirmed it on the replay-sampling path at 3/3 seeds, and the one genuinely open residual is whether that separability survives on a *second, independent* readout consumer.
**Extracted from:** V3-EXQ-888's own `combination_rule` and `criteria[].claim` mapping (C1 + C4 are registered against this claim), plus SD-035's `what_would_answer` residual-gap section. Not drafted fresh.
**Currency check:** `evidence/experiments/v3_exq_888_..._20260804T075257Z_v3.json` (PASS, 3/3 seeds, `non_degenerate: true`, `degeneracy_reason: ""`); reviewed -- present in `review_tracker.json` `reviewed_run_ids` **and** `discussed_experiment_dirs`; `claim_evidence.v1.json` MECH-074 `genuine_exp_count 1 / exp_conf 0.705 / confirmed_established`. Substrate present and wired (`ree_core/amygdala/bla.py`, `cea.py`; master knob `use_amygdala_analog=False`, per-module `use_bla_analog`/`use_cea_analog` default True *under* the master). Consumer audit found the spec's third consumer (E3.select) **absent** -- see currency finding 7. Reverse-deps checked: MECH-074a-d, MECH-078, MECH-361, SD-035.
**epistemic_category (proposed):** `standard` (no change; currently unset and inferred as `standard` from `mechanism_hypothesis` -- leave inferred).
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION: reuse V3-EXQ-888's readiness block verbatim; do not re-derive it. All five must be reported green in-run: n_traces >= 8; buffer std of the ground-truth arousal label >= 0.02 (this is the statistic EVERY AOR routes on -- all four AORs are differences of means of gt_arousal, so zero spread forces every AOR to 0 regardless of weighting); buffer/label index alignment == 1.0; memory_strength range across buffer traces >= 0.05 (the strength route cannot move a weighted sample if encoding_gain does not vary); retrieval_bias range across buffer traces >= 0.01 (same for the address route). Plus the instrument control: the fully-OFF arm must be flat, |AOR_z(OFF)| <= 0.02 on every seed (888 measured -0.0006 / -0.0107 / +0.0063). For a run on a NEW consumer, add: the consumer must be shown to actually receive a non-uniform weight vector -- HippocampalModule silently ignores a retrieval_bias whose numel does not equal the buffer length (hippocampal/module.py:2964), so a length mismatch degenerates to uniform sampling with no error.
> CONFIRMING: four arms at matched seeds (FULL / TAG_OFF = strength route only / GAIN_FLAT = address route only / OFF). Head authority: AOR_z(FULL) - AOR_z(OFF) >= 0.03 on >= 2/3 seeds. Separability: BOTH single-route arms independently clear the same floor -- AOR_z(TAG_OFF) - AOR_z(OFF) >= 0.03 AND AOR_z(GAIN_FLAT) - AOR_z(OFF) >= 0.03. On a NEW consumer (E3.select proposal reweighting, once wired per SD-035's data-flow spec) the address-route arm must clear 0.06, i.e. 2x the across-seed SD of that arm's delta as measured in 888 (0.0313), because the 0.03 absolute floor sits at exactly 1 SD there and would not distinguish replication from noise; the strength-route arm's observed SD is 0.0740, so its replication floor is 0.15.
> FALSIFYING: FULL clears but NEITHER single-route arm does -- authority without separability, i.e. one undifferentiated write channel rather than a read/write head with two routes, which is the parent's specific residual assertion and the only thing it still claims beyond the children. Also falsifying: the OFF arm is not flat (|AOR_z| > 0.02), which voids the instrument rather than the claim; or, on the new consumer, both single-route deltas fall below their replication floors with all preconditions green -- separability would then be a property of the replay-sampling path only, and the parent's scope should be narrowed to that path in text rather than left general.
**Proposal sketch (only for a/d):**
- title: `V3-EXQ-<next>: MECH-074 read/write-head route separability on a SECOND readout consumer (E3.select proposal reweighting)`
- related_claims: MECH-074, MECH-074a, MECH-074b, SD-035, ARC-007, MECH-073, MECH-165 (the `replay_diversity_enabled` gate that currently owns the only live consumer)
- acceptance_checks: (1) 888's five readiness gates green per arm; (2) OFF-arm flatness |AOR_z| <= 0.02; (3) head authority delta >= 0.03 on >= 2/3 seeds; (4) both single-route arms >= their replication floors (0.06 address / 0.15 strength); (5) a wiring precondition that `retrieval_bias.numel() == n_candidates` at the E3 consumer, reported, not assumed.
- Note the prerequisite: this run cannot be written until the E3.select consumer named in SD-035's data-flow spec actually exists. Until then this is `complicated (buildable)` on a small wiring change, not `complex (probe-gated)`.
**depends_on additions (if any):** none. (Optionally `MECH-165` as a *note*, since `replay_diversity_enabled` currently gates the only live consumer of the address route -- but that is a wiring fact, not a conceptual dependency.)
**GOVERNANCE FLAG:** `stale_note` -- MECH-074 still carries `v3_pending: true` and a `live_status.evidence` of `decision:...@2026-04-25 hold_pending_v3_substrate/applied`, while its two stated release conditions (substrate lands; EXQ-A/B-equivalent evidence) are both discharged and it now holds a reviewed PASS of its own (888, exp_conf 0.705, `confirmed_established`). Recommend clearing `v3_pending` and refreshing `live_status.evidence` to point at 888. **Also `promotion_review`:** with one genuine supporting run and no weakening runs, `candidate -> provisional` is a live question for the governance pass -- flagged, not applied, and explicitly not a `shown` recommendation.

---

### MECH-074a -- BLA analogue applies an arousal-dependent multiplicative gain to HippocampalModule write strength

**Recommended disposition:** (a) testable now -- the claim's own registered falsifier has a **two-sided** form ("threat-context recall improves ... OR neutral recall is harmed") and the second side has never been measured by any run, because AOR is a composition statistic that cannot separate "threat recall improved" from "neutral recall displaced".
**Extracted from:** the claim's `functional_restatement` "Falsifiable:" clause, restated identically in `ree-v3/ree_core/amygdala/bla.py` ("Falsification signatures (per sub-claim): MECH-074a"), plus SD-035's `what_would_answer` residual gap (ii) which already names this exact unexecuted run.
**Currency check:** two genuine experimental entries now, not one -- V3-EXQ-659 (2026-06-09, PASS/supports, arousal-over-representation PRIMARY-minus-ABLATION 0.135/0.033/0.213) and V3-EXQ-888 C3 (2026-08-04, strength-route deltas 0.325/0.177/0.249, 3/3). `claim_evidence.v1.json`: `genuine_exp_count 2, pass_runs 2, fail_runs 0, exp_conf 0.755, overall 0.784, confirmed_established`. Promotion gate (`exp_conf >= 0.80 AND >= 4 entries`) still unmet -- status `provisional` is correct. Substrate live: inverted-U gain in `bla.py` (`encoding_gain_max 2.5`, `arousal_threshold_on 0.4`, `arousal_peak 0.7`, window 18000 / half-life 3600 -- all matching the claim's registered numbers), per-episode peak gain carried to the trace as `memory_strength` (`agent.py:3903`). The zero-sum compensation form the second falsifier half would route to already exists as `bla_retrieval_bias_compensation` (default 0.0, `bla.py:463-469`).
**epistemic_category (proposed):** `standard` (leave inferred).
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION: (1) BLA must actually tick in the live loop -- report `bla_n_ticks > 0`; this is the exact defect that vacated V3-EXQ-474's C2-C5 (an env.step 5-tuple unpacking bug left `bla_n_ticks = 0` and turned the run into synthetic BLAAnalog.tick() unit tests). (2) The gain must VARY: per-episode peak encoding_gain range across the buffer >= 0.05 (888's MS_RANGE_FLOOR), with at least one episode above `bla_arousal_threshold_on = 0.4` and not every threat episode pinned at the inverted-U peak -- a saturated gain is a constant and tests nothing. (3) BOTH DVs must be live: threat-item recall and neutral-item recall each strictly between floor and ceiling in the gain=1 baseline, so that a DECREMENT in neutral recall is measurable at all. (4) The DV must be RECALL ACCURACY on a probe, NOT the arousal-over-representation statistic used by V3-EXQ-659 and V3-EXQ-888. This is the load-bearing precondition: AOR is a share-of-a-fixed-budget measure, so an AOR increase and a neutral-recall decrement are the SAME event expressed twice -- the existing evidence therefore cannot address the second half of this claim's own falsifier even in principle.
> CONFIRMING: two arms at matched seeds -- ARM_GAIN (use_amygdala_analog=True, use_bla_analog=True, defaults) vs ARM_GAIN_1 (`override_bla_encoding_gain` pinned to 1.0, everything else bit-identical). Threat-context recall accuracy delta >= max(0.05 absolute, 1 SD of the across-seed delta) on >= 2/3 seeds, AND neutral recall delta > -0.02 on the same seeds. Both halves required -- a threat-recall gain alone is not a PASS of this falsifier as registered.
> FALSIFYING: with preconditions green, threat-recall delta below the floor on >= 2/3 seeds -- the encoding-gain arithmetic buys replay-composition bias (659/888) but no recall benefit, and the claim's mapping from write strength to retrievability is mis-specified. SEPARATELY falsifying the arithmetic but not the mechanism: threat gain bought at neutral cost (neutral recall delta <= -0.05), which is the claim's own named second failure mode and routes to `bla_retrieval_bias_compensation` (0.1-0.3, the zero-sum form already implemented and default-off) rather than to abandoning the claim.
**Proposal sketch (only for a/d):**
- title: `V3-EXQ-<next>: MECH-074a live-loop threat-vs-neutral recall under BLA encoding gain (the unexecuted half of SD-035 EXQ-B)`
- related_claims: MECH-074a, MECH-074, SD-035, MECH-073, ARC-007
- acceptance_checks: `bla_n_ticks > 0`; per-episode peak-gain range >= 0.05 with >= 1 episode above 0.4 and no saturation at 2.5; baseline neutral recall non-degenerate (not 0.0 or 1.0); C1 threat-recall delta >= max(0.05, 1 SD) on >= 2/3 seeds; C2 neutral-recall delta > -0.02 on the same seeds; C3 bit-identical control with `use_amygdala_analog=False` (already contract-guarded by `tests/test_flag_inertness.py` probe F-P1 and `tests/contracts/test_feature_flag_boot_matrix.py` `tpj_and_amygdala` row).
**depends_on additions (if any):** none.
**GOVERNANCE FLAG:** `stale_note` -- the `evidence_quality_note` asserts "this is the first [experimental entry]" and `exp_conf now 0.775`; there are now two entries (659, 888) and `exp_conf` is 0.755. The promotion gate is still unmet so status does not move; only the note needs refreshing, plus a `live_status.evidence` pointer to 888 alongside 659.

---

### MECH-074b -- BLA writes a content-selective per-trace arousal tag and applies a per-trace retrieval weight vector (NOT a scalar gain)

**Recommended disposition:** (a) testable now, on a **narrowed** residual -- 888 already answered the "the address route has independent authority and is not scalar-equivalent" leg; what remains untested is the actual LaBar & Cabeza dissociation (central/gist vs peripheral items *within* an emotional event), and one further leg (trace-age growth) is not implemented at all and should be split out rather than silently carried.
**Extracted from:** the claim's `functional_restatement` "Falsifiable:" clause; `bla.py`'s MECH-074b falsification signature ("...or if a uniform retrieval boost produces the same behaviour (scalar-equivalent), the content-selective form has collapsed"); and 888's `ARM_GAIN_FLAT` design, whose preconditions this draft cross-references rather than re-derives.
**Currency check:** the claim reads as untested (`v3_pending: true`, `live_status` with no `evidence` block) but is not: 888's C2 is registered against MECH-074b and passes 3/3 seeds (`claim_evidence.v1.json`: `pass_runs 1, fail_runs 0, exp_conf 0.705, overall 0.794, confirmed_established`). The implementation risk the block flags ("Requires HippocampalModule to carry a per-trace arousal_tag field") is **closed**: the tag is written per trajectory (`agent.py:3904`, `hippocampal/module.py:2885/2917/3142`), read back via `get_exploration_arousal_tags()` (module.py:2920), turned into `w_i = 1 + alpha*tag_i` at `bla.py:459-469` (`alpha` default 0.6, in the claim's [0.3, 1.0] band), and consumed as sampling weights at `module.py:2951-3021`. **But** the consumer coverage is narrower than SD-035's spec: `retrieval_bias` reaches `diverse_replay` (gated on `replay_diversity_enabled`) and the REM reverse-replay pass only -- it never reaches `E3.select` (currency finding 7). A 2026-08-07 targeted lit-pull (4 entries, one mixed/weakening on the retrieval locus) is absent from the block's `source`. The claim's "BLA contribution grows with trace age (20 min -> 1 week)" leg has **no implementation**: `arousal_tag` is a static scalar written once at encoding, with no age term anywhere in `bla.py` or `hippocampal/module.py`.
**epistemic_category (proposed):** `standard` for the claim as a whole (leave inferred). Flagging separately that the **trace-age-growth leg is `substrate_conditional`** and should be carried in a `digestion_note` or split to its own id rather than left inside a `standard` claim, where it silently drags on any promotion.
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION: see MECH-074's own what_would_answer for the shared readiness block (n_traces, gt_arousal spread, buffer/label alignment, both route-nonuniformity floors, OFF-arm flatness) -- do not re-derive it. Two additions specific to this claim: (a) the arousal tag must be written AT ENCODING (`bla_retrieval_tag_at_encoding=True`); the module exposes False precisely to reproduce the named scalar failure signature, so that setting is the NEGATIVE CONTROL ARM, not a misconfiguration. (b) The environment/harness must expose CENTRAL/GIST vs PERIPHERAL items WITHIN the same episode, each with independently measurable recall. Without (b) the run re-measures 888's between-trace threat-vs-neutral contrast, which is already answered and is NOT the LaBar & Cabeza central/peripheral dissociation this claim is about; a "PASS" obtained that way would be vacuous with respect to the residual.
> CONFIRMING: three arms at matched seeds -- ARM_VECTOR (per-trace w_i = 1 + alpha*tag_i, alpha in [0.3, 1.0]), ARM_SCALAR (uniform w = 1 + alpha*mean(tag) across all traces; equivalently `bla_retrieval_tag_at_encoding=False`), ARM_OFF. Confirming requires ALL THREE of: (1) in ARM_VECTOR, central/gist recall advantage over peripheral items of 1.3x-2.0x relative to the neutral baseline (the claim's own registered target magnitude) on >= 2/3 seeds; (2) ARM_SCALAR's dissociation indistinguishable from ARM_OFF's (delta below 0.02) -- the scalar form must NOT reproduce it; (3) ARM_OFF's dissociation flat within |0.02|.
> FALSIFYING: ARM_SCALAR reproduces ARM_VECTOR's dissociation within the margin -- the content-selective form is not load-bearing and the claim collapses to a scalar retrieval gain, which is the failure signature the claim was registered to exclude. Independently falsifying: ARM_VECTOR's dissociation misses the floor with all preconditions green -- the per-trace weight then has composition authority over the replay SAMPLE (888) but no authority over item-level READOUT, and the claim should be narrowed to the sampling path rather than retained as a retrieval-weight claim. NOT falsified by, and not testable as, the "BLA contribution grows with trace age" leg: no age term exists in the substrate, so that leg is substrate_conditional on an unbuilt trace-age input and must not be scored in this run.
**Proposal sketch (only for a/d):**
- title: `V3-EXQ-<next>: MECH-074b central/peripheral dissociation under vector vs scalar BLA retrieval bias`
- related_claims: MECH-074b, MECH-074a (supplies the encoding-time tag; a 074b null is uninterpretable if the tag write is not green), MECH-074, SD-035, ARC-007
- acceptance_checks: shared 888 readiness block; `bla_retrieval_tag_at_encoding` true in ARM_VECTOR / false in ARM_SCALAR with all else bit-identical; within-episode central vs peripheral item recall both non-degenerate in ARM_OFF; C1 vector dissociation 1.3x-2.0x on >= 2/3 seeds; C2 scalar-arm dissociation <= 0.02 above OFF; C3 OFF flatness.
**depends_on additions (if any):** none required (MECH-074a is already listed, correctly, with the right rationale comment). Optionally record MECH-165 as the current gate on the only live consumer.
**GOVERNANCE FLAG (two):**
- `stale_note` -- `v3_pending: true` and an empty `live_status` on a claim that holds a reviewed 3/3-seed PASS (888 C2), `exp_conf 0.705`, `confirmed_established`; and the block's `source` omits the entire 2026-08-07 `targeted_review_mech_074b/` pull. Recommend clearing `v3_pending`, adding a `live_status.evidence` pointer to 888, and folding in the four lit entries.
- `evidence_discrepancy` -- one of those new lit entries (Roozendaal & McGaugh 2011, `evidence_direction: mixed`, confidence 0.62) explicitly weakens this claim's RETRIEVAL locus while supporting MECH-074a's encoding locus: "the best-established amygdala memory effect is on CONSOLIDATION ... at RETRIEVAL the amygdala/glucocorticoid effect is documented as IMPAIRING". The claim text does not record this, and a governance pass should decide whether 074b's locus needs narrowing (e.g. to a *sampling-priority* rather than *retrieval-enhancement* form) before more experiment budget goes to it.

---

### MECH-074c -- CeA analogue emits a fast subcortical priming signal (fast_prime), distinct from MECH-046's cortical mode-prior write

**Recommended disposition:** (c) substrate-blocked -- **`substrate_conditional`**, blocking substrate = the **SD-011 AffectiveHarmEncoder magnitude regime** (`||LowFreq(z_harm_a)||_1/n` never reaches `cea_fast_route_threshold` in an embodied run), which is itself an instance of the V3 observation->z_world binding constraint. Legs 1-2 are genuinely answered in the *driven* regime and should not be re-run; everything the claim asserts about *in-loop* function is untestable until the gate fires.
**Extracted from:** the claim's own 3-leg "Falsifiable:" clause; V3-EXQ-895's `evidence_scope_note` (which self-declares the PARTIAL scope) and `interpretation.selectivity_leg` (which banks the readiness denominator for a successor, explicitly so the successor "need not re-derive it"). Drafted by narrowing those, not from a blank page.
**Currency check:** V3-EXQ-895 (2026-08-08) is PASS/supports with all five criteria green -- C1 onset latency 0 steps (<= 2), C2 fitted half-life 4.0 (in [3,5]), C3 retained fraction at override-window end 0.297 (<= 0.50), C4 cortical confirmation holds 1.0 retained with arm separation 0.703 (>= 0.40), C5 max |fast_prime| 0.8 <= `mode_prior_log_odds_max` -- and `non_degenerate: true`. **But** its non-gating embodied probe records `embodied_fire_count = 0` on all 4 seeds (570 / 720 / 638 / 116 ticks), `lf_harm_max` 0.202 / 0.093 / 0.216 / 0.122 against `cea_fast_route_threshold = 0.5`, and `fast_prime_max = 0.0` everywhere. So the gated criteria are driven-regime results. Two of the claim's own scope notes have gone stale: the SD-032c AIC comparator now **exists** (`ree_core/cingulate/aic_analog.py`, constructed at `agent.py:792-803`), so the fast:slow leg is buildable; and the `agent.py:869-886` urgency-interrupt pointer no longer resolves. `claim_evidence.v1.json`: `genuine_exp_count 1, pass_runs 0 recorded as fail 0, exp_conf 0.714, overall 0.735, confirmed_established`.
**epistemic_category (proposed):** `substrate_conditional` -- **contested; see the flag.** The strict discriminator asks whether the mechanism has ever been exercised: in the regime the claim is *about* (embodied, in-loop, prefiguring cortical output) it never has -- zero fires, so there is no signal for anything downstream to absorb, which rules out `substrate_ceiling`. The counter-argument is that legs 1-2 hold real positive driven-regime evidence, and this category suppresses promote/demote on a `provisional` claim.
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION -- this is the whole finding, not a formality: the CeA fast gate must actually FIRE in the regime being measured, at its REGISTERED threshold. The only embodied measurement to date (V3-EXQ-895's non-gating SELECTIVITY_PROBE, 4 seeds, 2044 ticks total) recorded embodied_fire_count = 0 on every seed with max ||LowFreq(z_harm_a)||_1/n = 0.216 against cea_fast_route_threshold = 0.5, and fast_prime identically 0.0. Any embodied MECH-074c run must therefore report fire_count > 0 with the threshold at default before any DV is read; a run that LOWERS the threshold to force firing measures the threshold, not the claim, and must be reported non_contributory. Legs 1 (onset latency) and 2 (decay under cortical non-confirmation, plus overridability and boundedness) are ALREADY ANSWERED in the driven regime by V3-EXQ-895 (C1 0 steps <= 2; C2 half-life 4.0 in [3,5]; C3 0.297 <= 0.50; C4 hold 1.0 / separation 0.703; C5 0.8 bound) -- do not re-run them; cite 895.
> CONFIRMING (the residual, in-loop leg): with the gate firing at its registered threshold in an embodied run, fast_prime's onset must PRECEDE the AIC/dACC comparator's threshold crossing on the same harm event by >= 3 sim steps on >= 2/3 seeds (the claim's registered 1-2 vs 5-10 step spec, i.e. the ~5:1 fast:slow ratio floored conservatively), while |fast_prime| stays <= cea_mode_prior_log_odds_max so the fast route never dominates cortex, and cortical confirmation arriving inside the override window still holds the pulse (>= 0.90 retained) as it does under driven input.
> FALSIFYING: with the gate firing, fast_prime and the AIC crossing are simultaneous, or AIC leads -- the signal is not functionally a PRIME (it arrives too late to prefigure cortical output), which is the module's own registered MECH-074c failure signature. Also falsifying: in-loop, the pulse proves non-overridable (cortical confirmation cannot flip it within the 5-10 step window) -- the override discipline that bounds this claim would then be false in the only regime that matters.
> LEG 3 IS NOT A MECH-074c LEG (fused-claim finding, stated here so it stops being re-litigated): "CeA must fire on harm-affective valence, not generic arousal" cannot be tested as a CeA-module manipulation, because CeAAnalog.tick() is a pure function of ||LowFreq(z_harm_a)||_1/n -- a magnitude-matched non-harm drive fires IDENTICALLY by arithmetic (the DV-symmetry artifact class, per failure_autopsy_V3-EXQ-604c and 895's own interpretation.selectivity_leg). Selectivity is a property of the upstream SD-011 AffectiveHarmEncoder. That leg should be re-registered against SD-011 with 895's already-banked readiness denominator: mean AUROC against the same hazard-proximity label of 0.674 (encoder input), 0.622 (CeA gate statistic), 0.540 (generic activation), reference floor 0.60 -- i.e. the encoder's own harm-discriminativeness is currently only marginally above the floor, which is the real question hiding inside this leg.
**Proposal sketch (only for a/d):** n/a -- not (a). If the encoder regime is ever raised (or a threat-dense curriculum reaches the gate), the successor is fully specified above and 895 already banked its denominator, so it is `complicated (buildable)` at that point rather than a fresh design.
**depends_on additions (if any):** none strictly needed -- SD-011, SD-032c and MECH-046 are already listed. Recommend a `digestion_note` recording that leg 3 belongs to SD-011 and that the fast:slow leg is now unblocked on the SD-032c side (AICAnalog exists) and blocked only on the firing precondition.
**GOVERNANCE FLAG (two):**
- `contested_disposition` -- proposing `epistemic_category: substrate_conditional` on a `provisional` claim suppresses promote/demote. The case for it: the claim's in-loop content has never been exercised (0 fires embodied). The case against: legs 1-2 hold genuine driven-regime PASSes and 895 is already scored `supports`. Governance should choose explicitly rather than let the tag drift; a middle option is to leave the category inferred and record the firing precondition as a `digestion_note`, which preserves the evidence reading while still preventing a vacuous successor.
- `stale_note` -- (i) "Urgency interrupt at ree-v3/ree_core/agent.py:869-886" no longer resolves (that range is now the ConditionedSafetyStore block); the deferred migration into `fast_prime` is still undone. (ii) The 2026-08-08 note's "fast:slow ratio ... out of scope pending SD-032c AIC comparator wiring" is stale as to the blocker -- AICAnalog is built and wired; the actual blocker is the never-firing embodied gate.

---

### MECH-074d -- BLA emits a remap_signal on harm-PE spike when predictor-attribution flags specific latent codes (partial, ~one-third remap)

**Recommended disposition:** (c) substrate-blocked -- **`substrate_conditional`**, blocking substrate = **MECH-153's supervised context-labeling objective** (unbuilt) over the SD-016 / E1 `ContextMemory` store. The four consecutive negative results are a *precondition* failure of the attribution head's INPUT, not four independent refutations of the remap mechanism, and MECH-153 registered this exact failure signature five months earlier for a different consumer.
**Extracted from:** the claim's `functional_restatement` "Falsifiable:" clause; the four autopsy records already inline in the block (894 / 894a / 894b / 894c); and SD-035's `substrate_queue.json` OPEN failure_record, whose target I quote verbatim rather than re-invent -- "an entropy-weight/loss-formulation change, OR a verified context-discriminating input signal to the attribution head, that clears C1 AND C2 on >= 2/3 seeds without relying on scalar loss-term retuning alone".
**Currency check:** the substrate is built and works mechanically -- `ree_core/amygdala/bla.py` remap gate plus the learnable `ree_core/amygdala/attribution_head.BLAAttributionHead` (landed 2026-08-09, `ree-v3 25e04cf5f5` + `d2c8d6f2f0`, default-off via `bla_attribution_head='contribution_threshold'`); 894/894a established compute/fire/write/partiality are correct across four PE-sigma thresholds. `claim_evidence.v1.json`: `genuine_exp_count 4, pass_runs 0, fail_runs 4, exp_conf 0.414, plausible_unproven`; demotion `provisional -> candidate` applied 2026-08-16 -- **that demotion is not disputed here.** What IS new since 894c (2026-08-10): (a) `ree-v3 76cbf84` "repair ContextMemory.write() deterministic single-slot fixed point" (2026-08-19); (b) a ContextMemory write-address workstream -- V3-EXQ-943 PASS, 946 PASS (`context_informative_address_found_at_operating_point`), 956 FAIL, 969 FAIL, 970 FAIL (`h1_content_referencing_objective_not_confirmed_either_regime`), 971, 972 PASS (`h4_supported_representation_undifferentiated`). **All seven carry `evidence_direction: non_contributory` and `claim_ids: null`** -- none is scored against MECH-074d, so the owed fix is NOT delivered. And the deeper input: MECH-153's required supervised context-labeling objective is **not built** -- no `context_label` / `supervised_context` symbol anywhere in `ree-v3/ree_core/` (verified with `/usr/bin/grep`), and its validation run V3-EXQ-504 returned `inconclusive`. SD-035's 2026-08-09 addendum independently states the mechanism: the legacy ContextMemory write path homogenises the slot bank to off-diagonal cosine 1.0000 within ~24 episodes, "which defeats ANY attribution rule".
**epistemic_category (proposed):** `substrate_conditional` -- **this is a proposal to RE-TAG, and the reasoning must be read with its history.** The 894c autopsy deliberately moved this claim `substrate_conditional -> standard` in order to expose it to the ordinary promotion/demotion pass; that pass ran on 2026-08-16 and the demotion was applied. The exposure purpose is therefore **spent**, and leaving it `standard` now means each future cycle re-litigates a demotion that has already happened on a claim whose input mechanism does not exist. The strict discriminator supports the tag: the attribution head has never been exercised with a context-discriminating input, so there is no signal for a downstream mechanism to absorb (which is what `substrate_ceiling` would require).
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION -- the attribution head must be given a context-DISCRIMINATING input, and the run must PROVE it in-run before scoring anything. V3-EXQ-894c's decisive reading was that within-context and cross-context Jaccard similarity were IDENTICAL (1.0000 exactly) in 10/15 cells -- the head had converged to a deterministic, context-INVARIANT target set. That is the same signature MECH-153 registered on 2026-03-31 for the E1 ContextMemory store (cosine_sim 0.9999 between hazard-proximate and hazard-distal context vectors, 0/3 seeds), and SD-035's own 2026-08-09 addendum states the legacy write path homogenises the slot bank to off-diagonal cosine 1.0000 within ~24 episodes, "which defeats ANY attribution rule". So a retest is VACUOUS unless it first reports, sustained over the scoring window: off-diagonal ContextMemory slot cosine <= 0.90, AND within-context vs cross-context Jaccard separable at all (not both exactly 1.0). The MECHANICAL half needs no further testing -- 894 and 894a established that candidates compute, the gate fires under `use_e2_harm_a=True`, writes land, and partiality holds, across four PE-sigma thresholds; a fifth run of that is redundant compute.
> CONFIRMING: under a store that PASSES the differentiation precondition, and at some operating point, C1 attribution_mass_excess > 0.05 AND C2 context_jaccard_gap > 0.05 on >= 2/3 seeds, with the partiality half still holding (fraction of perturbed codes ~0.33, not wholesale). This is SD-035's open failure_record target verbatim; do not weaken it, and do not substitute C1 alone -- C1 recovered fully under the trained head in 894b (0/3 -> 3/3) while C2, the actual Moita 2004 dissociation this claim is about, stayed at 0/3, so C1 alone is a known false-positive route.
> FALSIFYING: with the differentiation precondition demonstrably GREEN, C2 still stays at 0/3 seeds -- the Moita 2004 contextual-vs-auditory dissociation is then not reproducible by an attribution-gated remap in this architecture, and the claim is refuted on its critical half rather than deferred again. Note what would survive that: the partiality half (~one-third remap, not wholesale replacement) held on 2/3 seeds in 894 and could be retained as a narrowed residual claim about remap SHAPE with the attribution-gating half withdrawn. Four routes are already closed by measurement and must not be re-proposed: PE-threshold recalibration/dilution (894a, Spearman -1.0 monotone), trainability alone (894b, doubled budget), entropy_weight/MSE scalar retune (894c, swept [0.02, 0.01, 0.005, 0.001], `passing_arm_ids=[]`, and the predicted C1-vs-C2 tradeoff came out INVERTED at spearman -1.0), and a fifth mechanical-gate readiness run.
**Proposal sketch (only for a/d):** n/a -- not (a). The next artifact owed is a BUILD (MECH-153's supervised context-labeling objective, or a validated substitute from the 943/946/956/969-972 write-address workstream), not an experiment. V3-EXQ-946's `context_informative_address_found_at_operating_point` is the single most promising existing lead and is the thing a `/implement-substrate` chip should be pointed at.
**depends_on additions (if any):** **add `MECH-153`** (E1 ContextMemory requires a supervised context-labeling objective; without it context vectors stay near-identical) and **`SD-016`** (the E1 z_world ContextMemory query path that owns the store). This is the single most load-bearing edit this group recommends: it converts four apparently independent refutations into one named, already-registered, already-owned upstream precondition, and it makes the dependency machine-readable so the next governance pass does not re-derive it.
**GOVERNANCE FLAG (three):**
- `contested_disposition` -- MECH-153's own registration says of the identical failure signature: "**This is an implementation precondition, not a claim that MECH-150 is false.**" By that precedent MECH-074d's four weakens results measure an absent input, not a false mechanism. This does **not** argue for reversing the 2026-08-16 demotion (`exp_conf 0.414`, `conflict_ratio 0.80` are real and the demotion "records what the evidence already shows"); it argues for re-tagging `epistemic_category` to `substrate_conditional` so the claim stops being re-demoted for a precondition it cannot satisfy, and for routing it to `/implement-substrate` rather than `/queue-experiment`. Governance to ratify or reject; not applied here.
- `evidence_discrepancy` -- SD-035's open failure_record target ("a verified context-discriminating input signal") has had a substantial workstream land against it since 894c (ree-v3 `76cbf84` plus V3-EXQ-943/946/956/969/970/971/972, 2026-08-19 to 2026-09-02), yet every one of those runs is `non_contributory` with `claim_ids: null`, so nothing has updated MECH-074d or the SD-035 entry. The `resolved: open` record and the claim's `pending_retest_after_substrate: true` are both accurate but neither reflects that the fix is being actively probed and that V3-EXQ-972 reports `h4_supported_representation_undifferentiated` -- i.e. current evidence points at the representation, not the head.
- `stale_note` -- SD-035's `status_note_addendum_20260809` records "STILL OWED: the MECH-074d implementation_note in claims.yaml was NOT written" (deferred at the time because another session held a binding arbitration verdict on claims.yaml). It is still not written; the trainable-head build record lives only in `docs/architecture/sd_035_amygdala_analog.md` "Second pass: trainable attribution head". Additionally, SD-035's `metric_trajectory` still asserts "MECH-074b retrieval_bias hippocampal-consumer wiring deferred (substrate produces signal but HippocampalModule does not yet read)", which is false as of the current tree.

---

### Cross-group note for the orchestrator (not a disposition)

SD-035 itself is not in this group but is the parent substrate for all five claims and accumulated four stale statements found during this pass (currency findings 2, 6, 7, 10). Two of them -- the E3.select consumer that the spec asserts and the code does not implement, and the "HippocampalModule does not yet read" line -- would each change how a reviewer reads MECH-074b. If any group is digesting SD-035, these belong there; otherwise they are worth a single `stale_note` flag on SD-035 in their own right.

---

<!-- G4 appended 2026-09-04T21:17:34Z -->
## G4 -- signal legibility / language-as-externalisation cluster  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** The assigned rationale was
  co-occurrence scoring (ARC-048 <-> MECH-192 = 6.00 via `depends_on` + "functional states /
  requires"; INV-057 <-> MECH-192 = 4.00; INV-057 <-> MECH-182 = 3.79 via the shared
  social-signal namespace). My own view after reading the live blocks is sharper and changes
  the whole shape of the pass: **all four members are the fan-out around a single hub claim,
  MECH-191, which has ALREADY been digested** and carries a fully-worked `what_would_answer`
  using an explicit Leg A (testable now, receiver-free) / Leg B (blocked on the social stack)
  split. MECH-191 `depends_on` MECH-182 (it is registered as "extends MECH-182 from one signal
  to the full repertoire"); INV-057, MECH-192 and ARC-048 all `depends_on` MECH-191. So this
  group is not four independent falsifier-drafting jobs. It is **one already-written falsifier
  plus three positioning decisions relative to it**, and the single most valuable thing this
  pass can do is stop three claims re-deriving a test that exists, and identify the one genuinely
  new manipulation the group is missing (MECH-192's signal-side ablation). Standing instruction 1
  (extract before inventing) and 6 (cross-reference rather than re-derive) do most of the work here.

- **(i) same-claim / merge candidates:**
  - **MECH-192 <-> MECH-191 Leg B / MECH-183: PARTIAL absorption, propose merge, do NOT retire.**
    MECH-192 as registered ("z_beta leakage can only produce functional state-matching if the
    perceived signal maps onto a corresponding internal state") is close to **analytic** -- it
    reads as a definitional truth about what a mapping is, not an empirical assertion. Its
    necessity framing is already covered by MECH-191's Leg B falsifier clause (receiver decoding
    "drops toward chance when the receiver's own homologous internal-state machinery is
    ablated/absent") and by MECH-183's OTHER_SELFLIKE ON/OFF 2x2. **The residual is real but
    narrow, and nobody currently owns it: MECH-191 Leg B ablates the RECEIVER; MECH-192's own
    content requires ablating the SIGNAL** (an energy- and information-matched scramble at fixed
    coupling). Those are different manipulations and the receiver-side one does not test the
    signal-side one. Disposition (g) below, with the narrowed residual written out.
  - **INV-057 <-> MECH-191 Leg A: FUSED, not merge.** INV-057's architectural consequence
    ("stereotyped signals are causally generated by their referent states, not conventional") is
    MECH-191 Leg A's assertion verbatim; INV-057 adds nothing REE-side beyond it. What INV-057
    uniquely owns is the *evidential move* from comparative ethology, which no REE substrate can
    settle. Disposition (c2), with the REE leg explicitly assigned to MECH-191.
  - **MECH-182 <-> MECH-191 Leg A: overlapping but NOT merge.** MECH-191's own notes say it
    "extends MECH-182 from one signal to the full repertoire", so MECH-182 looks like the
    single-signal special case. It is not: MECH-191 Leg A is **receiver-free and learning-free**
    (it asserts causal production only), whereas MECH-182's whole novelty over the classical
    acoustic literature (Andics 2014, Balint 2022) is the **learning** step (cross-modal
    association acquired from self-experience) and the **generalisation** step (same feature in
    another agent). Neither is in MECH-191. Keep both.
  - **ARC-048 <-> INV-003: FUSED, not merge.** ARC-048's premise leg ("language is not a separate
    cognitive system") is INV-003's assertion, already digested as a `derivational` code-path
    audit. Its consequence leg (the bootstrap requires functional states to pre-exist as
    referents; language is a *bandwidth increase over the same channel*) is ARC-048's alone and
    is the falsifiable part. Two-leg template written out below, as the group brief asked.

- **(ii) contradictions / undercut premises:** No outright contradiction, but **one real
  premise-undercut that changes a falsifier and that neither claim states.** INV-057 argues
  "legible without species-specific learning, therefore causally generated, therefore not
  conventional" -- it treats *not socially conventional* as interchangeable with *not learned*.
  MECH-182 says the harm-signal mapping **is** learned: acquired privately from self-experience
  by the harm attribution stream. These are compatible only under a distinction neither claim
  makes -- **socially conventional (acquired by transmission from conspecifics) vs individually
  learned from self-experience with one's own homologous state.** This is not pedantry: it
  changes what falsifies INV-057. Under the naive reading, "cross-species reading requires prior
  exposure" falsifies INV-057; under the sharpened reading it does not (self-experience with
  one's own state *is* the exposure, and that is precisely MECH-182's mechanism). INV-057's
  falsifier must therefore be stated over CONVENTION, not over LEARNING, or MECH-182 falsifies
  INV-057 by construction. I have written it that way below.

  Second, softer undercut: **ARC-048's premise presupposes a pre-linguistic externalisation
  channel already exists** ("language adds bandwidth to a channel that already exists"). MECH-191
  Leg B's finding -- re-confirmed by me on 2026-09-04 -- is that no such channel exists in
  `ree_core/` at all. So ARC-048's non-degeneracy precondition is **strictly stronger than
  INV-003's**: INV-003 needs a language mechanism; ARC-048 needs a language mechanism AND a
  pre-linguistic channel to measure bandwidth *against*. Without the denominator, "higher
  bandwidth" is not a measurable predicate.

- **(iii) shared falsifier:** Yes, and it is already written. **MECH-191's `what_would_answer`
  Leg B RELEASE CONDITION** -- ARC-047 (scent/broadcast channel) plus ARC-010/MECH-031/MECH-032
  (other-agent modelling) -- is the identical gate for MECH-182 Leg B, MECH-192, and ARC-048's
  channel prerequisite. All three should point at it verbatim rather than restate it. Separately,
  **MECH-191's Leg A non-degeneracy precondition** (the internal-state channel and the candidate
  signal-analog event must BOTH show non-degenerate variance across the run -- state activates
  and goes quiescent, event fires and fails to fire) is the reusable precondition shape for
  MECH-182 Leg A and for ARC-048's referent-partition gate. And **MECH-183's already-drafted
  rejected-proxy list** is reusable as a negative control across the group: proxy (a)
  "simulated other-distress cues without an actual other-agent model" and proxy (b) "cross-modal
  z_beta activation from a correlated same-agent cue" are both explicitly non-diagnostic for the
  social claims -- but note that **proxy (b) IS the correct test for MECH-182 Leg A**, and
  MECH-183's own text says so ("tests sensory association learning, i.e. MECH-182"). That is the
  single most useful extraction in this group: MECH-182's Leg A design already exists in the
  registry, written by someone else, and labelled with MECH-182's id.

- **(iv) cross-cutting finding:** Two, and both are group-level.
  1. **The entire 2026-04-05/06 "Steve" cohort is epistemic-category orphaned.** MECH-182,
     MECH-192, MECH-193, ARC-048 and INV-057 carry **no `epistemic_category` and no
     `implementation_phase`**. The indexer therefore *infers*: `standard` for the three
     `mechanism_hypothesis` entries (exp_conf required for promotion; `lit_only` / `low_exp` /
     discrepancy flags fire normally) and `substrate_coherence` for INV-057 (promote/demote
     suppressed, as though it were a foundational REE design choice). Every structurally
     identical claim registered *later* carries the explicit tags -- ARC-047, MECH-405, MECH-505,
     MECH-506, MECH-194, ARC-115, ARC-117, ARC-118 are all `substrate_conditional` +
     `implementation_phase: v5`. Consequence: the cohort generates **permanent lit-only
     promotion-queue noise on claims that are structurally unbuildable in V3**, and INV-057's
     suppression is right by accident and wrong by reason. One tagging pass fixes all five.
  2. **Mutual confound -- the group has a mandatory run ORDER.** A null on MECH-192 is
     uninterpretable unless MECH-183 is pinned (a flat legibility response cannot be
     distinguished from "there is no leakage to modulate"); a null on MECH-183 is uninterpretable
     unless MECH-191 Leg A is pinned (a signal that is not state-specific carries nothing to
     leak). The chain **MECH-191 Leg A -> MECH-183 -> MECH-192** must be established in that
     order, and MECH-182 Leg B sits downstream of the same chain. Any proposal that runs a
     legibility or generalisation manipulation before Leg A passes is vacuous by construction.

- **Currency findings** (each verified this pass, 2026-09-04):
  1. **All four members have ZERO experimental evidence.** `evidence/experiments/claim_evidence.v1.json`:
     ARC-048 `exp_conf 0.0`, 2 lit entries, `lit_conf 0.746`; INV-057 `exp_conf 0.0`, 5 lit
     entries, `lit_conf 0.862`; MECH-182 `exp_conf 0.0`, 3 lit, `0.708`; MECH-192 `exp_conf 0.0`,
     3 lit, `0.787`. All four `evidence_quadrant: plausible_unproven`, `genuine_exp_count: 0`,
     `fail_runs: 0`. Each one's `latest_run_id` is a **2026-04 literature entry, not a run**
     (e.g. INV-057 and MECH-192 both point at
     `2026-04-06_mech_192_dog_recognize_emotion_multimodal_albuquerque2016`).
  2. **The one experiment manifest that names MECH-191 does not count.**
     `evidence/experiments/v3_exq_723_jlens_dispositional_readout_diagnostic_20260709T151028Z_v3.json`
     states verbatim: `experiment_purpose=diagnostic, EXCLUDED from governance scoring;
     claim_ids=[] -- SD-064 global-workspace claim + MECH-191 signal-legibility referenced for
     CONTEXT only`. No group member has any run-level evidence at all.
  3. **Substrate re-confirmed absent (independent re-check of MECH-191 Leg B's and MECH-183's
     2026-08-08 findings).** `grep -ril` over `/Users/dgolden/REE_Working/ree-v3/ree_core/` returns
     **zero** hits for `other_agent`, `multi_agent`, `OTHER_SELFLIKE`, `attribution_stream`,
     `empathy`, `vocal`, `timbre`, `acoustic`. Same for
     `/Users/dgolden/REE_Working/ree-v3/experiments/_lib/`. `z_beta` exists but is documented in
     `ree_core/latent/stack.py:14` as `z_beta [beta_dim] -- affective latent (arousal/valence;
     integrates self + world signals)` -- a **SELF** stream in the shared stack, exactly as
     MECH-183 recorded. **Trap flagged so the next pass does not repeat it:** the sole `legib`
     hit under `ree_core/` is `ree_core/agent.py:10050`, a comment reading "provenance is legible
     at the call site" -- unrelated to signal legibility. Do not read it as substrate.
  4. **Nothing is queued to build.** `evidence/planning/substrate_queue.json` has **zero**
     entries for ARC-048, INV-057, MECH-182, MECH-192, MECH-191, MECH-183, ARC-047 or MECH-041.
  5. **Plan-orphan status, split.** MECH-191 IS in `fast_empathy_v5_plan.md` `scope_claims`
     (`[ARC-010, MECH-031, MECH-112, SD-011, MECH-183, MECH-191, MECH-359, MECH-360]`).
     **MECH-192, MECH-182, MECH-193 and INV-057 are in NO plan's `scope_claims`**, despite being
     the direct siblings of the two that are. **ARC-048 is NOT in
     `language_emergence_bootstrap_v6_plan.md` `scope_claims`** (`[ARC-009, INV-003, INV-007,
     MECH-010, MECH-014, MECH-308]`) despite being registered explicitly as "the pre-linguistic
     bridge to INV-003", and despite that plan's node `LANG-2` being literally "the pre-linguistic
     substrate inventory communication needs before it can bootstrap".
  6. **STALE: a reassignment flag was raised and never applied.** `fast_empathy_v5_plan.md`
     decision log, 2026-06-10: "Reassignment flags raised for the existing social claims this plan
     builds on whose subject is intrinsically social (ARC-010, MECH-031, MECH-183, MECH-191)."
     As of 2026-09-04 **neither MECH-183 nor MECH-191 carries an `implementation_phase` field in
     `claims.yaml`** -- contrast ARC-047 and MECH-405, which both carry `implementation_phase: v5`.
  7. **STALE: the 2026-04-06 intake's own Next Step 4 is unexecuted.** It says "social.md should
     gain stubs for MECH-191/192/193 and ARC-048 when social extension work begins".
     `docs/architecture/social.md` (mtime 2026-08-30, so actively maintained -- it has *since*
     grown MECH-505 and MECH-506 sections) contains **zero** occurrences of MECH-191, MECH-192,
     MECH-193, ARC-048, INV-057 or MECH-182. The only adjacent hits are MECH-183/MECH-405 inside
     the MECH-505 text. This is a gap in a live file, not a dormant file.
  8. **KNOB finding, decisive for MECH-182.** The learner MECH-182's mechanism runs in --
     `BLAAttributionHead`, `ree-v3/ree_core/amygdala/attribution_head.py` (SD-035 / MECH-074d) --
     **exists but is DEFAULT-OFF**: `ree_core/utils/config.py:6017` sets
     `bla_attribution_head: str = "contribution_threshold"`, i.e. the fixed **non-trainable**
     rule. That module's own docstring states the fixed rule "has no learned component ... and no
     mechanism by which it could become more selective with experience". Furthermore its
     selectivity sits at a **documented competence floor**: V3-EXQ-894 (FAIL, weakens) and
     V3-EXQ-894a (FAIL, weakens, 4-point sigma sweep) with autopsy
     `failure_autopsy_V3-EXQ-894a_2026-08-08` diagnosing `competence_implementation_gap`
     (per-seed: one selective, one context-blind-deterministic, one null, stable at every
     threshold). Any MECH-182 learning test on default config is vacuous.
  9. **NEW downstream consumer for ARC-048.** ARC-118 (registered 2026-08-01, "worldly reference
     is inherited through the world model") `depends_on: [ARC-048, INV-003]` and is tagged
     `substrate_conditional` / `implementation_phase: v5` / `version_relevance: v5_v6`. ARC-048's
     own epistemic status is currently **less specified than its own dependent's**.

---

### GROUP-LEVEL GOVERNANCE FLAGS

**GOVERNANCE FLAG -- `stale_note`:** The 2026-04-05/06 "Steve" cohort (MECH-182, MECH-192,
MECH-193, ARC-048, INV-057) carries no `epistemic_category` and no `implementation_phase`, so the
indexer infers `standard` for the three mechanism_hypotheses and fires `lit_only`/`low_exp` flags
perpetually against claims that are structurally unbuildable in V3, while INV-057 gets
`substrate_coherence` suppression for the wrong reason. Every later-registered structural twin
(ARC-047, MECH-405, MECH-505, MECH-506, MECH-194, ARC-115, ARC-117, ARC-118) carries explicit
`substrate_conditional` + `v5`. Recommend a single tagging pass across the cohort; per-claim
proposals below. MECH-193 is out of my group but is in the same cohort and same condition --
flagged here so it is not missed.

**GOVERNANCE FLAG -- `stale_note`:** `fast_empathy_v5_plan.md`'s 2026-06-10 decision-log entry
records reassignment flags raised for MECH-183 and MECH-191; neither claim has an
`implementation_phase` field in `claims.yaml` as of 2026-09-04. The flag was raised and never
applied. (MECH-183 and MECH-191 are read-only context for me -- no draft, no disposition; this is
a plan/registry consistency finding only.)

**GOVERNANCE FLAG -- `stale_note`:** The 2026-04-06 intake's Next Step 4 (social.md stubs for
MECH-191/192/193 and ARC-048) is unexecuted against a file that has been actively maintained since
(`docs/architecture/social.md`, mtime 2026-08-30, gained MECH-505/MECH-506 sections). Zero
references to any of the four. Also: MECH-192, MECH-182, MECH-193 and INV-057 appear in no plan's
`scope_claims`, and ARC-048 is missing from `language_emergence_bootstrap_v6_plan.md`
`scope_claims` / node LANG-2 despite being the registered pre-linguistic bridge to INV-003.

---

### ARC-048 -- Language is a high-bandwidth externalization of pre-existing functional states, not a separate cognitive system

**Recommended disposition:** (c) substrate-blocked, `substrate_conditional` -- the falsifiable
leg needs BOTH a symbol channel (MECH-014 / LANG-3, absent) and a pre-linguistic externalisation
channel to measure bandwidth against (ARC-047, absent), so it is gated on two unbuilt substrates,
not one, and the premise leg is already owned and already digested by INV-003.

**Extracted from:** the claim's own `notes` (the Steve-yelp / Daniel-sentence referent pair);
the 2026-04-06 intake section 3 "The language bootstrap"
(`evidence/planning/thought_intake_2026-04-06_steve_signal_legibility_language_bootstrap.md`);
INV-003's already-drafted `what_would_answer` (for the premise leg and the audit-target framing);
MECH-191's Leg A/Leg B template (for structure). Not drafted fresh.

**Currency check:** (a) INV-003's 2026-08-07 finding -- no `language` / `symbol_channel` /
`communication_channel` / `message_passing` implementation under `ree_core/` -- re-confirmed by my
own greps 2026-09-04; the only language artifacts remain the `LANGUAGE_EXPLICITATION` enum label
in `ree_core/claustrum/control_demand.py` (no implementation) and the "doesn't exist yet in
ree_core" comment in `ree_core/claustrum/coalition_templates.py`. (b) The *pre-linguistic* channel
ARC-048 additionally needs is ARC-047's seven scent fields -- `claims.yaml` ARC-047 is `candidate`,
`confidence: 0.0`, `implementation_phase: v5`, and my grep confirms zero broadcast/scent-emission
implementation under `ree_core/`. (c) ARC-048 has 2 literature entries, `exp_conf 0.0`,
`plausible_unproven`; no run has ever named it. (d) ARC-048 is absent from
`language_emergence_bootstrap_v6_plan.md` `scope_claims` and from node LANG-2's enabling-conditions
checklist, though LANG-2 is exactly the node its content belongs to. (e) ARC-118 (2026-08-01)
already `depends_on` ARC-048 and is tagged `substrate_conditional` / v5.

**epistemic_category (proposed):** `substrate_conditional`
(with `implementation_phase: v6`, `version_relevance: v5_v6` -- matching ARC-118's tagging and the
`language_emergence_bootstrap_v6` tier; governance to arbitrate v5 vs v6, since the channel
prerequisite is a v5 node and the language layer is v6).

**Draft `what_would_answer`:**

> **ARC-048 IS FUSED -- a metaphysical premise plus an operational consequence, with opposite
> ownership. Split them; do not test the group as one thing.**
>
> **LEG A -- THE PREMISE ("language is not a separate cognitive system"). NOT ARC-048's to
> answer. Already owned, already digested.** This is INV-003's assertion ("language emerges as
> functional self-representation, not a bolt-on"), and INV-003 already carries a full
> `what_would_answer` specifying the resolution route: a **code-path audit** (category
> `derivational`), not a trained behavioural experiment, run against whatever function turns agent
> state into emitted symbols and received symbols into agent-state updates, asking whether that
> path reads from and writes to the shared self-representational latent substrate (z_self,
> `ree_core/latent/stack.py`, `ree_core/latent/self_recurrence.py`) or is architecturally
> isolated. **See INV-003's own `what_would_answer` for the precondition, the audit target, and
> both verdict conditions. Do not re-derive them here.** ARC-048 adds nothing to Leg A and must
> not be credited or debited by its outcome.
>
> **LEG B -- THE OPERATIONAL CONSEQUENCE (the falsifiable part ARC-048 alone owns).** Two
> independent, separately-measurable predictions follow from "language is a bandwidth increase
> over an existing functional-state channel, and the bootstrap requires functional states to
> pre-exist as referents":
>
> **NON-DEGENERACY PRECONDITION (strictly stronger than INV-003's -- three gates):**
> (1) A signalling mechanism that both emits and consumes symbols must exist and execute -- the
> same gate INV-003 states, confirmed unmet 2026-08-07 and re-confirmed 2026-09-04. The
> designated landing site is MECH-014's minimal signalling channel, instantiated at
> `language_emergence_bootstrap_v6:LANG-3` (status `blocked`).
> (2) **A PRE-LINGUISTIC externalisation channel must ALSO exist**, because "higher bandwidth than
> the existing channel" has no denominator without one and prediction B2 has no baseline
> partition. That channel is ARC-047's scent/broadcast fields; see MECH-191's own
> `what_would_answer` Leg B RELEASE CONDITION for the exact substrate list -- **do not re-derive
> it.** This gate is what makes ARC-048 harder than INV-003, and it is the reason ARC-048 cannot
> ride INV-003's audit.
> (3) The functional-state channels used as the referent partition must each show non-degenerate
> cross-episode variance -- z_harm_a, z_goal, and z_beta valence must each activate AND go
> quiescent within the run (the same variance shape MECH-191 Leg A's precondition specifies). A
> referent partition with a channel pinned always-on or always-off is degenerate and the mutual
> information in B2 is undefined at the floor; the run self-routes `substrate_not_ready`.
>
> **CONFIRMING (B1 -- ORDERING / referent precedence):** with the signalling channel open, an
> agent whose functional-state channels are ablated or floored fails to stabilise ANY signal,
> while a matched agent with intact functional states and no prior signalling history does
> stabilise signals -- i.e. the referents are load-bearing for bootstrap, not incidental.
> **CONFIRMING (B2 -- ISOMORPHISM / bandwidth-monotonicity):** the emergent signal repertoire's
> discriminative partition is a **refinement** of the pre-linguistic functional-state partition --
> higher resolution over the SAME referents (the yelp -> "my leg hurts when I walk on wet grass"
> relation in the claim's own notes) -- not a cross-cut of it. Metric: mutual information between
> emitted-signal identity and functional-state identity exceeds MI between signal identity and an
> entropy-matched task-arbitrary partition (e.g. tokens keyed to grid coordinates), by a margin
> scaled on the SD of the cross-seed delta plus an absolute floor, on at least 2/3 seeds.
>
> **FALSIFYING (B1):** signals stabilise just as readily over an arbitrary non-functional-state
> referent set as over functional states -- language is then a general symbol-learning capacity
> and ARC-048's "pre-existing functional-state referents" requirement is doing no work.
> **FALSIFYING (B2):** the emergent partition **cross-cuts** the functional-state partition (the
> signals carve the task, not the state space), or MI with functional states is
> indistinguishable from MI with the entropy-matched arbitrary partition -- language is then a
> separate channel that merely co-exists with the functional-state channel, not a
> bandwidth increase over it, which is precisely the "separate cognitive system" reading ARC-048
> denies.
>
> **Note on what does NOT falsify ARC-048:** expressive breadth or grammaticality of the emergent
> signalling. INV-003 already records that fluency is a different question; the same exclusion
> applies here, and more sharply, because ARC-048's claim is about the referent architecture, not
> the channel's expressive power.

**Proposal sketch (only for a/d):** n/a -- not proposing an experiment; both gates are unmet and
`substrate_queue.json` carries no entry for any of the required substrate.

**depends_on additions (if any):** add **ARC-047** (the pre-linguistic broadcast channel that
precondition (2) requires -- currently a hard prerequisite that appears nowhere in ARC-048's
`depends_on`) and **MECH-014** (the minimal signalling channel precondition (1) requires).
Existing `[INV-003, MECH-191, MECH-192]` all stay.

**GOVERNANCE FLAG:** `stale_note` -- ARC-048 is registered as the pre-linguistic bridge to INV-003
but is absent from `language_emergence_bootstrap_v6_plan.md` `scope_claims`
(`[ARC-009, INV-003, INV-007, MECH-010, MECH-014, MECH-308]`) and from node `LANG-2`'s
enabling-conditions checklist, which is the exact node its content belongs to. Recommend adding
ARC-048 to that plan's `scope_claims` and naming "functional states pre-exist as referents" as an
explicit LANG-2 enabling condition. Second, `contested_disposition` -- ARC-048 currently carries no
`epistemic_category`/`implementation_phase` while its own dependent ARC-118 is
`substrate_conditional`/v5; the parent should not be less specified than the child.

---

### INV-057 -- Cross-species signal legibility evidences that stereotyped signals are functionally specific (causally generated), not socially conventional

**Recommended disposition:** (c2) `out_of_domain` -- this is a **fused** claim whose evidential leg
is comparative ethology that no REE substrate at any level can settle, and whose architectural leg
is already asserted and already digested as MECH-191 Leg A; reframe to name MECH-191 as the owner
of the REE leg and record the out-of-domain proof obligation here.

**Extracted from:** the claim's own `notes` (the Albuquerque 2016 / Molnar 2010 / Ekman 2009
argument as written); the 2026-04-06 intake's INV-057 block and its literature section; MECH-191's
already-drafted Leg A (for the architectural leg, which I point at rather than restate). Not
drafted fresh.

**Currency check:** (a) INV-057 has 5 evidence entries, **all literature**
(`lit:empirical_behavioral` x2, `lit:review_historical`, `lit:review_neuroscience`,
`lit:review_systematic`), `exp_conf 0.0`, `genuine_exp_count 0`, quadrant `plausible_unproven`; its
`latest_run_id` is the Albuquerque 2016 literature entry, not a run. (b) Because it is
`claim_type: invariant` + `invariant_type: universal` with **no explicit `epistemic_category`**,
the indexer resolves it to `substrate_coherence` -- "foundational design choices that ARE the
substrate" -- which is the wrong description of an empirical argument from dog-human communication
studies. The promote/demote suppression it currently receives is correct in effect and wrong in
reason, which means it will be re-litigated by every future governance walk. (c) INV-057 appears in
no plan's `scope_claims`. (d) Precedent for the reframe exists in-registry: 17 claims carry
explicit `epistemic_category: out_of_domain`, including one invariant (INV-062) and the SOC-HUM-1..4
cohort, which pairs `out_of_domain` with a `functional_restatement` field; RA-001/002/003 are the
`claim_type: research_anchor` precedent. (e) INV-057 has a downstream consumer: ARC-117
(`related_claims: [..., MECH-192, INV-057, MECH-191]`), so it must not be retired.

**epistemic_category (proposed):** `out_of_domain`
(and see the governance flag: `claim_type` review toward `research_anchor` is warranted but is
deliberately NOT proposed as an in-place edit -- `REE_assembly/CLAUDE.md` says do not change
`claim_type` in place. The explicit `epistemic_category` is the safe, sufficient action now.)

**Draft `what_would_answer`:**

> **INV-057 IS FUSED and its title gives it away: it is EVIDENTIAL in form ("X evidences that
> Y"), not architectural. An invariant should assert Y; INV-057 asserts the inference X |- Y.
> Split the two legs; only Leg 1 belongs to INV-057.**
>
> **LEG 2 -- THE ARCHITECTURAL CONSEQUENCE Y ("stereotyped signals are causally generated by
> their referent states, not conventional"). NOT INV-057's to answer.** This is MECH-191 Leg A's
> assertion verbatim, and MECH-191 already carries the full REE-side test: per-signal specificity
> of the internal-state channel against the other state channels and a quiescent baseline, plus a
> state-variable ablation that must collapse the corresponding signal-analog event, for the four
> signals whose internal-state correlate exists in `ree_core/` today (whine/z_goal,
> huff/E3-discard-at-breath-cadence, yelp/z_harm_a, tail-wag/z_beta-positive-valence). **See
> MECH-191's own `what_would_answer` Leg A -- its non-degeneracy precondition, its specificity
> and ablation criteria, and its falsifier. Do not re-derive them here.** INV-057 must not be
> separately credited or debited by that outcome; a MECH-191 Leg A pass is not additional
> evidence for INV-057, it is the same evidence counted once.
>
> **LEG 1 -- THE EVIDENTIAL PREMISE X (INV-057's own, and out of REE's domain). This is a
> literature observation, not an experiment. No substrate at any level helps.**
>
> **PROOF OBLIGATION / LITERATURE OBSERVATION:** the observation must hold that cross-species
> affective reading occurs **without species-specific training or convention exposure** --
> Albuquerque 2016 (dogs integrate face + voice to recognise human emotion, untrained,
> cross-modal); Molnar 2010 (perceivers **blind from birth** classify emotional valence from dog
> barks, which is the load-bearing case because it removes any visual-convention learning route);
> Ekman 2009 (the Darwinian universality review). The formal move INV-057 makes is: if the
> mapping were socially conventional, cross-species reading would require separate,
> species-pair-specific learning; it does not; therefore the signal is a causal product of the
> state.
>
> **SHARPENING REQUIRED BEFORE THIS IS FALSIFIABLE, and it is not optional -- as written the
> claim is falsified by its own sibling.** INV-057 uses "not socially conventional" as though it
> meant "not learned". MECH-182 asserts that the harm-signal mapping IS learned -- privately,
> from self-experience, by the harm attribution stream. The two are consistent only under the
> distinction **socially conventional (acquired by transmission from conspecifics, hence
> species-pair-specific) vs individually learned from self-experience with one's own homologous
> internal state (hence available to any architecture that has the homologous state)**. INV-057's
> falsifier must be stated over CONVENTION, not over LEARNING. Under the naive reading, a finding
> that legibility requires prior exposure falsifies INV-057; under the sharpened reading it does
> not, because self-experience with one's own state IS the relevant exposure -- and that is
> exactly MECH-182's mechanism.
>
> **COUNTEREXAMPLE (what would refute Leg 1), in descending order of decisiveness:**
> (1) **The domestication confound resolved against the claim** -- the cleanest available
> counterexample and one the claim's current notes never state. Dogs are the *worst* test case:
> ~15k years of co-evolution with humans could plausibly have selected for human-directed
> signalling, which is a shared-history explanation, not a functional-specificity one. A
> well-powered failure to replicate automatic cross-species affect reading in a **non-domesticated,
> phylogenetically distant species pair** would show the effect is carried by co-evolutionary
> history, not by causal generation from shared functional states.
> (2) A well-powered demonstration that naive perceivers with no prior exposure to the emitting
> species perform at chance, and that accuracy is a monotone function of species-specific
> exposure -- convention/statistical learning, not causal generation.
> (3) A demonstration that the acoustic/behavioural features carrying the effect are **arbitrary
> with respect to the production physiology** -- i.e. that the same functional state produces
> systematically different signals across populations with matched physiology, which is what a
> conventional signal looks like and what a causally-generated one cannot be.
>
> **CONFIRMING (Leg 1):** replication of the blind-perceiver and untrained cross-modal results,
> extended to at least one non-domesticated species pair, with accuracy invariant to prior
> exposure to the emitting species.
>
> **NOTE ON SCOPE:** no REE run, of any substrate generation, can confirm or falsify Leg 1. A
> MECH-191 Leg A pass is a REE-internal *analogue* of the causal-generation conclusion, not
> evidence about biology. Treating REE evidence as confirmation of Leg 1 (or biological evidence
> as confirmation of the REE leg) is the fusion this split exists to prevent.

**Proposal sketch (only for a/d):** n/a.

**depends_on additions (if any):** none. `[MECH-191]` is correct and is exactly the pointer Leg 2
needs.

**GOVERNANCE FLAG:** `contested_disposition` -- INV-057 is `claim_type: invariant` /
`invariant_type: universal`, so with no explicit `epistemic_category` the indexer resolves
`substrate_coherence` and suppresses promote/demote as if it were a foundational REE design
choice. It is not: it is an argument from comparative ethology with 5 literature entries and zero
experimental entries, and its architectural half is already owned by MECH-191. Recommend setting
`epistemic_category: out_of_domain` explicitly, and opening a separate review of whether
`claim_type` should become `research_anchor` (precedent RA-001/002/003; SOC-HUM-1..4 show the
`out_of_domain` + `functional_restatement` pattern). Not proposed as an in-place `claim_type` edit
-- `REE_assembly/CLAUDE.md` forbids that; it needs the supersede-with-new-claim route or an
explicit governance decision. **Do not retire or merge INV-057:** ARC-117 lists it in
`related_claims`, and the argument-form content (legibility-as-evidence-for-functional-specificity)
is genuinely not stated anywhere else.

---

### MECH-182 -- Vocalization timbre as learned cross-modal harm-approach signal, generalizing to other-agent vocalizations

**Recommended disposition:** (c) substrate-blocked, `substrate_conditional` -- but with the most
useful finding in the group attached: **Leg A is blocked on ONE small build (an arousal-modulated
self-produced observable that re-enters the agent's own observation) plus a knob flip, NOT on the
whole ARC-047 social stack**, which makes it the group's cheapest unblock; only Leg B needs the
full social substrate.

**Extracted from:** **MECH-183's already-drafted `what_would_answer`, rejected-proxy (b)** --
"cross-modal z_beta activation from a correlated same-agent cue (tests sensory association
learning, i.e. MECH-182, not social attribution)". That proxy was rejected *for MECH-183's
purposes* and explicitly labelled as testing MECH-182; for MECH-182 it is the correct design and
it was already written. Plus the 2026-04-05 intake's seven structural steps
(`evidence/planning/thought_intake_2026-04-05_steve_dog_emotional_mirroring.md`, MECH-182 section),
which supply the Leg A / Leg B cut (steps 1-4 vs steps 5-7). Plus MECH-191's Leg A precondition
shape. Not drafted fresh.

**Currency check:** (a) MECH-182 has 3 literature entries (`lit:neuroimaging_comparative` x2,
`lit:review`), `exp_conf 0.0`, `genuine_exp_count 0`, `plausible_unproven`; latest entry is the
2026-04-05 Yu 2024 rodent-contagion literature record, not a run. (b) **The learner exists but is
default-off and floored** -- `BLAAttributionHead`, `ree-v3/ree_core/amygdala/attribution_head.py`
(SD-035 / MECH-074d) implements the trainable attribution head, but
`ree_core/utils/config.py:6017` sets `bla_attribution_head: str = "contribution_threshold"`, the
fixed non-trainable rule; that module's own docstring says the fixed rule "has no learned
component ... and no mechanism by which it could become more selective with experience". Its
selectivity is additionally at a documented competence floor: V3-EXQ-894 and V3-EXQ-894a both
FAIL/weakens, autopsy `failure_autopsy_V3-EXQ-894a_2026-08-08` = `competence_implementation_gap`,
per-seed pattern (one selective, one context-blind-deterministic, one null) stable across a
4-point sigma sweep. (c) **The signal does not exist at all** -- zero `vocal` / `timbre` /
`acoustic` / `cross_modal` hits under `ree_core/` (2026-09-04); `BreathOscillator`
(`ree_core/heartbeat/clock.py`, MECH-108) is a cyclic internal phase counter, **not** an emitted
or re-perceived observable, so it does not satisfy the requirement despite being the nearest
existing thing. `body_obs` exists (`ree_core/latent/stack.py`, `ree_core/agent.py`,
`ree_core/environment/causal_grid_world.py`) and is the plausible carrier if one were built.
(d) Leg B's substrate (other-agent model, OTHER_SELFLIKE, attribution stream) re-confirmed absent
2026-09-04 -- identical to MECH-183's and MECH-191 Leg B's findings. (e) MECH-182 is in no plan's
`scope_claims`, though its generalisation MECH-191 is in `fast_empathy_v5_plan.md`.

**epistemic_category (proposed):** `substrate_conditional`
(with `implementation_phase: v5` for consistency with MECH-405/ARC-047, noting that Leg A alone
could be pulled earlier if the self-observable is built -- governance may prefer to record that
asymmetry rather than tag the whole claim v5).

**Draft `what_would_answer`:**

> **MECH-182 IS CONJUNCTIVE across a LEARNING step and a GENERALISATION step, with very different
> readiness -- split it, mirroring MECH-191's Leg A/Leg B pattern. The intake's own seven
> structural steps give the cut: steps 1-4 are Leg A, steps 5-7 are Leg B.**
>
> **LEG A -- SELF-EXPERIENCE CROSS-MODAL LEARNING (intake steps 1-4). Blocked on one small build
> plus a knob, not on the social stack.** The assertion: an arousal-modulated, self-produced
> observable becomes, through experience, a learned predictor of harm-approach, acquired by the
> harm attribution stream. This is the leg carrying MECH-182's novelty -- the acoustic substrate
> itself is already documented (Andics 2014, Balint 2022); what is novel is that the mapping is
> *learned from self-experience*.
>
> **NON-DEGENERACY PRECONDITION (Leg A) -- three gates, all currently unmet:**
> (1) **A self-produced observable must exist**: some agent-emitted quantity that (i) is modulated
> by arousal (the natural carrier is z_beta, which is live in `ree_core/latent/stack.py` as the
> shared affective latent) and (ii) **re-enters the agent's own observation stream** so that an
> association can be learned over it. Confirmed absent 2026-09-04: no vocal/timbre/acoustic
> channel anywhere under `ree_core/`, and `BreathOscillator` (`ree_core/heartbeat/clock.py`) is an
> internal phase counter that is neither emitted nor re-perceived and therefore does **not**
> satisfy this gate.
> (2) **The trainable attribution head must be ON and above its competence floor**:
> `bla_attribution_head` must be set to `"trainable"` -- it **defaults to
> `"contribution_threshold"`** (`ree_core/utils/config.py:6017`), a fixed rule which by its own
> module docstring cannot acquire a cue-outcome association at all. A run on the default knob
> tests a fixed threshold and can neither confirm nor falsify a LEARNED association; it must
> self-route `substrate_not_ready`. Additionally the head's attribution selectivity must clear the
> V3-EXQ-894a competence floor on at least 2/3 seeds (autopsy
> `failure_autopsy_V3-EXQ-894a_2026-08-08`, `competence_implementation_gap`) -- otherwise a null
> is attributable to the head, not to the claim.
> (3) **Joint non-degenerate variance** (same shape as MECH-191 Leg A's precondition): the
> candidate observable must vary with arousal across the run, AND harm-approach episodes must both
> occur and fail to occur. An observable pinned to a constant, or a harm-approach rate at 0 or 1,
> tests nothing.
>
> **CONFIRMING (Leg A):** with gates (1)-(3) satisfied, the agent's harm-approach signal (the
> z_harm_a forward model, `ree_core/predictors/e2_harm_a.py`) comes to be driven by the
> self-observable at a lead time it did **not** have at initialisation -- predictive gain from the
> observable rises across training and exceeds a **shuffled-observable control** by a margin
> scaled on the SD of the cross-seed delta plus an absolute floor, on at least 2/3 seeds -- AND
> ablating the observable channel (not merely decorrelating it) degrades harm-approach lead time
> back toward the shuffled control. The association must be shown **acquired**: a matched agent
> trained with the observable held constant must NOT show the gain.
>
> **FALSIFYING (Leg A):** the predictive gain is already present at initialisation -- the mapping
> is architectural, not learned, which falsifies the "learned from self-experience" step that is
> MECH-182's entire novelty over the classical acoustic literature; OR, with the head trainable
> and the floor cleared, the gain never rises above the shuffled-observable control across
> training on at least 2/3 seeds -- which falsifies the cross-modal association itself.
>
> **LEG B -- CROSS-AGENT GENERALISATION (intake steps 5-7). BLOCKED, identical gate to MECH-191
> Leg B.** The assertion: the learned association transfers, so the same feature in ANOTHER
> agent's output activates the observer's harm-approach signal via the attributed other-model.
> **RELEASE CONDITION: see MECH-191's own `what_would_answer` Leg B RELEASE CONDITION -- ARC-047
> (broadcast channel) plus ARC-010/MECH-031/MECH-032 (other-agent modelling), both re-confirmed
> absent 2026-09-04. Do not re-derive it; MECH-182 implies no build beyond what MECH-183/MECH-191
> already require.** Do **not** substitute a scripted-partner or simulated-other-distress proxy:
> MECH-183's own `what_would_answer` already evaluated and rejected that (its proxy (a)) as
> non-diagnostic -- a PASS would not validate and a FAIL would not invalidate.
> **CONFIRMING (Leg B, once substrate exists):** the same observable carried by an OTHER agent
> activates the observer's harm-approach signal, and the transfer is gated by OTHER_SELFLIKE
> tagging (present vs absent) rather than by raw feature similarity.
> **FALSIFYING (Leg B):** transfer occurs at statistically indistinguishable magnitude with
> OTHER_SELFLIKE off as on -- this falsifies the "via the attributed other-model" step and reduces
> MECH-182 to plain stimulus generalisation, which is not a novel claim.
>
> **ORDER CONSTRAINT:** Leg B is uninterpretable before Leg A passes. If the self-experience
> association was never learned, there is nothing to generalise, and a Leg B null measures the
> absent Leg A rather than the generalisation step.

**Proposal sketch (only for a/d):** n/a as a queueable experiment -- but recording the **cheapest
unblock in the group** for the substrate queue, since it is materially smaller than everything
else here: a single self-produced, arousal-modulated observable that is written into the agent's
own observation (natural carrier: a scalar derived from z_beta, delivered alongside `body_obs`),
plus flipping `bla_attribution_head` to `"trainable"` and clearing the V3-EXQ-894a floor. That
combination makes MECH-182 Leg A testable **without any multi-agent substrate at all**. It should
be a `substrate_queue.json` entry; it currently is not one.

**depends_on additions (if any):** add **MECH-074d / SD-035** (the `BLAAttributionHead` the
learning step actually runs in -- MECH-182 names "the harm attribution stream" in prose but has no
dependency on the mechanism that implements it, which is why the default-off knob and the
competence floor went unnoticed against this claim) and **ARC-047** (Leg B's broadcast channel).
Existing `[INV-005, MECH-031, MECH-032]` all stay.

**GOVERNANCE FLAG:** `stale_note` -- MECH-182's registered mechanism ("this cross-modal
association is learned from self-experience by the harm attribution stream") presumes an
attribution learner that is (a) **default-off** (`ree_core/utils/config.py:6017`,
`bla_attribution_head = "contribution_threshold"`, the fixed non-trainable rule) and (b) at a
**documented competence floor** (V3-EXQ-894 / V3-EXQ-894a both FAIL/weakens, autopsy
`failure_autopsy_V3-EXQ-894a_2026-08-08` = `competence_implementation_gap`). Neither fact is
recorded against MECH-182, and either alone would make a Leg A run vacuous. Per
`REE_Working/CLAUDE.md` ("a claim can be `active` while its knob is default-off; check the knob,
not the status"), this belongs in the claim's own text.

---

### MECH-192 -- Signal legibility is prerequisite for fast empathy coordination: z_beta leakage (MECH-183) requires perceivable signals that map onto observer's own functional states

**Recommended disposition:** (g) **merge with sibling -- PROPOSE ONLY: PARTIAL absorption into
MECH-191 Leg B / MECH-183, retaining a narrowed residual.** As registered the claim is close to
analytic and its empirical content is already covered twice over; the residual that is genuinely
unowned is the **signal-side** ablation (energy- and information-matched scramble at fixed
coupling), which neither MECH-191 Leg B (which ablates the RECEIVER) nor MECH-183 (which ablates
the COUPLING) performs.

**Extracted from:** MECH-191's already-drafted Leg B (the receiver-ablation falsifier that absorbs
MECH-192's necessity framing); MECH-183's already-drafted `what_would_answer` (the OTHER_SELFLIKE
ON/OFF 2x2 that absorbs the coupling half, and the rejected-proxy list); the 2026-04-06 intake
section 1 "The legibility condition" and the MECH-192 block. The residual manipulation is the one
piece I derived, and only because the extraction showed nobody owns it.

**Currency check:** (a) MECH-192 has 3 literature entries, `exp_conf 0.0`, `genuine_exp_count 0`,
`plausible_unproven`; `latest_run_id` is the Albuquerque 2016 literature entry. (b) Its named
dependency **MECH-183 has no experimental evidence either** (`exp_conf 0.0`, 5 lit entries) and
its `what_would_answer` records the substrate as confirmed absent (IGW-200 feasibility assessment
`exp_0137_mech_183_feasibility_assessment.md`, 2026-06-11), which I independently re-confirmed
2026-09-04. So MECH-192's prerequisite-of-a-prerequisite is itself unpinned. (c) MECH-192 has
three reverse-references -- **ARC-048 `depends_on: [..., MECH-192]`**, ARC-115
`related_claims`, ARC-117 `related_claims` -- so a full retirement would strand ARC-048; partial
absorption is the only safe route. (d) MECH-192 is in no plan's `scope_claims`, despite MECH-183
and MECH-191 both being in `fast_empathy_v5_plan.md`'s. (e) MECH-192 has become the registry's
standing example of "the nearest live analogue is z_beta leakage, which is affective not
propositional" -- both ARC-115 and ARC-117 use it that way in their notes, which is a further
reason to keep the id alive.

**epistemic_category (proposed):** `substrate_conditional`
(with `implementation_phase: v5`, matching MECH-405/MECH-505/ARC-047).

**Draft `what_would_answer` (for the NARROWED RESIDUAL):**

> **AS REGISTERED, MECH-192 IS NEARLY ANALYTIC and therefore not yet falsifiable.** "z_beta
> leakage can only produce functional state-matching if the perceived signal maps onto a
> corresponding internal state in the observer" is a statement about what a mapping *is*, not an
> empirical prediction -- there is no world in which an unmapped signal produces state-matching.
> Its empirical content appears only when legibility becomes a **graded, manipulable variable**.
> That narrowing is the claim, and it is what the residual below states.
>
> **NARROWED RESIDUAL CLAIM:** coordination benefit from z_beta leakage is **monotone in signal
> legibility, holding attribution coupling and channel information fixed**. This is the
> SIGNAL-side ablation. It is distinct from -- and not tested by -- MECH-191 Leg B (which ablates
> the RECEIVER's homologous internal-state machinery) or MECH-183 (which ablates the COUPLING via
> OTHER_SELFLIKE ON/OFF). Nobody currently owns it.
>
> **NON-DEGENERACY PRECONDITION -- three gates, and the first two are NOT MECH-192's to satisfy:**
> (1) **MECH-191 Leg A must have PASSED.** The emitter's signal must first be shown to be a
> causal, state-specific product of the internal state; otherwise "legibility" of that signal has
> no referent and the manipulation measures channel noise. **See MECH-191's own
> `what_would_answer` Leg A precondition and criteria; do not re-derive them here.**
> (2) **MECH-183 must be PINNED.** The z_beta leakage channel must be demonstrated live and
> attribution-gated (its OTHER_SELFLIKE ON/OFF x distress-present/absent 2x2). **See MECH-183's
> own `what_would_answer`; do not re-derive it.** Grading legibility over an unpinned leakage
> channel is uninterpretable in **both** directions: a null cannot distinguish "legibility does
> not matter" from "there is no leakage to modulate", and a positive cannot distinguish leakage
> from ordinary perceptual inference.
> (3) **MECH-192's OWN gate, and the one that makes the claim falsifiable at all:** legibility
> must be manipulable as a graded variable **while attribution coupling is held fixed AND channel
> information is matched** -- i.e. a permuted/scrambled signal carrying identical information
> content and identical channel energy but no state-homology, versus the true signal, across at
> least three graded levels. Both arms must produce non-zero, non-identical coordination-cost
> variance. **Without the information-matched scramble the claim is unfalsifiable by
> construction** (any degradation is attributable to lost information rather than lost
> legibility), which is precisely the defect the current registration has.
>
> **CONFIRMING:** coordination cost (or observer state-matching accuracy) is **monotone in signal
> legibility** across the graded levels, with coupling strength and channel information held
> constant, on at least 2/3 seeds; the true-signal vs matched-scramble gap exceeds a margin scaled
> on the SD of the cross-seed delta plus an absolute floor; AND the monotone relation **survives
> ablating the observer's explicit inference/prediction pathway** toward the other's state, so the
> effect is on the leakage channel rather than on inference (the same dissociation MECH-183's
> CONFIRMING clause (2) demands, applied to the signal side).
>
> **FALSIFYING:** coordination is statistically indistinguishable between the true signal and the
> information-matched scramble at fixed coupling -- legibility is doing no work, the benefit is
> carried by information availability plus coupling alone, and MECH-192's "prerequisite" framing
> is false as an empirical claim; OR coordination tracks coupling strength but is **flat in
> legibility** across the full graded range -- same conclusion, and MECH-192 collapses entirely
> into MECH-183 with nothing left over.
>
> **RELEASE CONDITION: identical to MECH-191 Leg B -- ARC-047 (broadcast channel) plus
> ARC-010/MECH-031/MECH-032 (other-agent modelling). See MECH-191's own text. MECH-192 implies no
> build beyond what MECH-183/MECH-191 already require, plus the scramble control, which is an
> experiment-design item, not substrate.**

**Merge proposal detail (disposition (g)), for the orchestrator to route:**
- **Surviving id:** MECH-192 (narrowed), and MECH-191 (absorbing).
- **Absorbed id:** none retired. This is **partial** absorption with a narrowed residual, exactly
  the shape the brief anticipates.
- **What text moves to MECH-191 Leg B's rationale:** the necessity statement ("z_beta leakage can
  only produce functional state-matching if the perceived signal maps onto a corresponding
  internal state in the observer") and the cross-species explanatory framing (Albuquerque 2016,
  Silva 2011, "explains why fast empathy works cross-species without shared language"). Both are
  rationale for MECH-191 Leg B's receiver-ablation falsifier and read as duplication where they
  currently sit.
- **What STAYS as MECH-192:** the graded signal-side legibility manipulation with an
  information-matched scramble at fixed coupling -- the residual above. Retitle in the direction
  of "coordination benefit from z_beta leakage is monotone in signal legibility at fixed
  attribution coupling".
- **Reverse-deps needing repointing:** **none if the residual is retained** (which is the
  recommendation). For completeness, were MECH-192 retired outright, three references would need
  repointing: `ARC-048.depends_on`, `ARC-115.related_claims`, `ARC-117.related_claims` -- and
  ARC-048 would be stranded, since ARC-048's "functional states as referents" premise leans on
  MECH-192's legibility condition. That is an additional reason not to retire.

**depends_on additions (if any):** add **ARC-047** (the broadcast channel the release condition
names). Existing `[MECH-183, MECH-191]` are both correct and are exactly the two pointers gates (1)
and (2) need.

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-192 as registered is near-analytic and its
empirical content is covered by MECH-191 Leg B (receiver ablation) and MECH-183 (coupling
ablation); the partial-merge proposal above narrows it to the one manipulation nobody owns (the
signal-side, information-matched scramble at fixed coupling). Requires a governance decision on
retitle + text migration, not a silent edit. Second, `stale_note` -- MECH-192 appears in no plan's
`scope_claims` although both of its `depends_on` targets (MECH-183, MECH-191) are in
`fast_empathy_v5_plan.md`'s; recommend adding it there so the residual arm is tracked against
`fast_empathy_v5:EMP-4` (the A/B/C/D dissociation node), which is the node it belongs to.

---

<!-- G7 appended 2026-09-04T21:17:34Z -->
## G7 -- hippocampal comparator / event-segment / persistent program handle  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the brief groups them on
  MECH-288 <-> SD-084 = 4.32 (SD-084 `depends_on` MECH-288; the program handle persists across
  event segments) and MECH-206 <-> MECH-288 = 3.28 (same hippocampal namespace, both comparators
  emitting a boundary/surprise signal). Both links hold, but the sharper axis after research is a
  **three-stage pipeline all three claims sit on**: `latent / PE stream -> a graded mismatch
  readout -> a consumer that must actually read it`. Each claim owns a different stage, and
  **two of the three have a hole at the consumer end while the third is the one case where that
  hole was found and closed**. SD-084's whole content is "the consumer could not see the signal
  because the handle was torn down every tick"; MECH-206's consumer (replay output) is verified
  to have *no reader anywhere in `ree_core/`*; MECH-288's consumers are built but the claim has
  been credited by exactly one synthetic run while its substrate ran live in 23 indexed
  experiments. That reframing is what drives the dispositions below.

- **(i) same-claim / merge candidates:** **No merge recommended for any pair**, but there is a
  real, already-half-acknowledged convergence to record. MECH-288's own `notes` state that
  MECH-287's "upstream anchor-side comparator stage" (Vinogradova 2001 CA1/CA3 mismatch + O'Mara
  2009 + Lisman & Grace 2005) "is best read as the BIOLOGICAL substrate that MECH-288
  instantiates computationally", and `ree_core/regulators/invalidation_trigger.py`'s module
  docstring has already executed that collapse in code ("The upstream CA1/CA3 mismatch comparator
  substrate ... is collapsed here to a subscription on the MECH-288 boundary queue"). **MECH-206
  is the third face of that same biological comparator** -- CA3 pattern-completed prediction vs
  entorhinal actual, graded output -- pointed at a *third* consumer (surprise-buffer write /
  replay priority) rather than at the region partition (MECH-288) or the broadcast trigger
  (MECH-287). So the correct architectural reading is **one graded mismatch readout with three
  consumers at three thresholds**, not three comparators. I do **not** propose merging MECH-206
  into MECH-288 because MECH-206 carries content MECH-288 does not have anywhere: the
  **bidirectional connectivity shift** (CA1-EC up / CA1-CA3 down = *retrieval suppression of the
  now-erroneous prediction*), which is a second, dissociable functional leg with no analogue in
  the segmenter. Recommended instead: `related_claims` cross-links MECH-206 <-> MECH-288 <->
  MECH-287, and a governance note folding MECH-206 into the MECH-287/MECH-288 architectural
  reconciliation that MECH-288's notes already opened and left as "a downstream governance
  decision". SD-084 is a different claim class entirely (lifetime of a handle on E3Selector) --
  no merge pressure in either direction.

- **(ii) contradictions / undercut premises:** two, both real, neither a logical contradiction.
  1. **MECH-206's premise that a graded PE magnitude is what ranks episodes for replay is
     undercut *in the built substrate* by this group's own MECH-288.** The only replay-priority
     ranker that exists in `ree_core/` is `ree_core/sleep/replay_sampler.py` (MECH-285 Phase B),
     and it draws seed anchors "with probability proportional to a softmax over the frozen
     staleness signal" -- i.e. keyed on MECH-284 staleness over `RegionKey = (scale, segment_id)`,
     **which is MECH-288's segment ID**. The functional slot MECH-206 claims for a graded CA1 PE
     signal already has an incumbent occupant sourced from MECH-288's region partition. This is
     not a contradiction (both could be true; biology plausibly uses both), but it means
     **MECH-206's falsifier must be *discriminative* against staleness-priority**, not merely
     confirmatory of PE-priority. Drafted that way below.
  2. **MECH-288's canonical "PE-spike is the primary trigger" is not what the observation path
     actually runs.** `ree_core/agent.py:5448` calls
     `event_segmenter.step(latent_dict=..., pe_dict=None, t=...)`. `event_segmenter.py:139-142`
     documents the consequence: with no `pe_dict` the fast scale falls back to
     `agg(t) = sum_s ||z_s(t) - z_s(t-1)||`, a **latent-delta magnitude, not prediction error**.
     So on the observation stream as wired today the fast/inner scale is a *change* detector, not
     the PE-threshold detector Verdict 1 named primary (Zacks 2007 EST). The rollout stream is
     different: `ree_core/policy/policy_decomposition.py:581` does pass `pe=pe_signature`. This
     undercuts the "PE-proportional" framing that MECH-206 and MECH-288 share, and it is the
     single most important non-degeneracy precondition for any MECH-288 test.

- **(iii) shared falsifier:** yes, one precondition serves all three and should be written once
  on MECH-288 and cross-referenced. Call it the **LIVE GRADED-MISMATCH PRECONDITION**: *the
  statistic actually driving the mechanism under test must (a) be the quantity the claim names
  (forward prediction error, not a latent-delta proxy -- assert `pe_dict` is supplied and
  non-empty on the stream under test), and (b) have non-zero cross-tick variance and a
  non-saturated dynamic range over the measurement window.* MECH-206's draft below points at
  MECH-288's copy of this rather than re-deriving it. SD-084's own precondition is the
  reachability half of the same idea and is already discharged (V3-EXQ-839).

- **(iv) cross-cutting finding:** **two mutual confounds, and one template.**
  *Confound 1:* a null on MECH-206 is uninterpretable until a replay CONSUMER exists --
  `substrate_queue.json` entry `mech092-replay-consumer-missing` records, VERIFIED against source
  2026-09-01, that `Agent._do_replay` (agent.py:10366) computes `replay_trajs` and "ENDS at
  :10428 without ever reading the variable", with "no reader of replay output anywhere" in
  `ree_core/`. Every downstream consequence MECH-206 predicts is measured on replay output.
  *Confound 2:* a null on any MECH-288 downstream falsifier is uninterpretable while the
  observation-path fast scale is running the latent-delta fallback (see (ii).2) -- a null would
  be about a detector the claim does not describe. *Template:* SD-084 is the worked example of
  exactly this failure mode caught and fixed -- V3-EXQ-830 recorded
  `decomp_n_evaluated_midexec = 0` in all 10 cells against `precommit` 1862-2618, was correctly
  diagnosed `competence_implementation_gap` **not** `substrate_ceiling`, and the repair made the
  hook reachable (V3-EXQ-839: 415 vs 0). The group's lesson, stated once: **before any of these
  claims is read as ceilinged, check that its consumer exists and reads.**

- **Currency findings (all verified this pass, with the file checked):**
  1. **MECH-288's substrate is BUILT and the Phase-2 integration half of its promotion bar has
     LANDED** -- `ree_core/hippocampal/event_segmenter.py` exists; `substrate_queue.json` shows
     `MECH-269 | implemented`, `MECH-284 | implemented`, `MECH-287 | implemented`,
     `MECH-288 | implemented`. The claim's `evidence_quality_note` (2026-07-14) still describes
     "integration into Phase 2 (ii)+(iii)+(iv) downstream substrate plus the falsifiable
     predictions" as the open gate. **Half of that gate is now closed**; only the falsifiable
     predictions remain. Stale as written.
  2. **`use_event_segmenter` defaults to `False`** (`ree_core/utils/config.py:2761`) -- MECH-288
     is `provisional` with a default-OFF knob, exactly the "check the knob, not the status" case.
     It is nonetheless enabled in **23 indexed runs** (scan of `evidence/experiments/*.json`
     configs), from V3-EXQ-646 (2026-06-06) through V3-EXQ-938 (2026-08-18).
  3. **None of those 23 runs carries `MECH-288` in `claim_ids`.** `claim_evidence.v1.json` gives
     MECH-288 `experimental_confidence 0.66` from `genuine_exp_count: 1` -- the single synthetic
     isolation run V3-EXQ-757 -- against `literature_confidence 0.86` / 11 lit entries, quadrant
     `confirmed_established`, `overall_confidence 0.81`. The live substrate has been running
     under 22 other experiments and credits the claim nowhere. Flagged.
  4. **The rollout-side caller MECH-288's own code says does not exist, exists.**
     `event_segmenter.py:34` reads "nothing yet calls with `input_stream="rollout"` until
     ARC-070/MECH-321 lands"; `policy_decomposition.py:532/546/581` calls
     `boundary_on(stream="rollout", ...)`, and V3-EXQ-938 records
     `boundary_fires_mean_pe_arm 276.95` / `boundary_fires_mean_yoked_arm 287.325` over 40 seeds.
     Substrate docstring stale; the claim's 2026-07-24 note is correct.
  5. **MECH-206 has ZERO indexed evidence of any kind** -- `claim_evidence.v1.json` returns
     `null` for MECH-206 (its two `source:` literature records are filed under MECH-205's
     targeted review and credited there). Its dependency MECH-205 is `stable` (2 PASS / 1 FAIL,
     exp_conf 0.668); MECH-092 exp_conf 0.66; MECH-256 exp_conf 0.0. The 2026-09-01 `SD-003 ->
     MECH-256` repoint on MECH-206's `depends_on` is present and correctly annotated in the live
     block.
  6. **MECH-206's own comparator has no substrate and no substrate_queue entry.** Grep of
     `ree_core/` finds no `surprise_buffer` / `SurpriseBuffer` symbol and no CA1-style
     two-channel comparator; the only CA1 reference is `invalidation_trigger.py`'s docstring
     saying that comparator is *collapsed away* into a BoundaryEvent subscription. What does
     exist is MECH-205's single-channel path: `config.surprise_gated_replay` (default `False`,
     `config.py:3350`) writing a PE-magnitude scalar into the `VALENCE_SURPRISE` residue channel
     (`agent.py:10677-10726`), with `pe_surprise_threshold` promoted to `1e-5` by GFLAG-0075 on
     2026-09-01. That is a *graded PE tag*; it is not a two-channel prediction-vs-actual
     comparator and it does not write a ranked buffer.
  7. **`closure_status.md:409` is NOT stale (checked, and I am recording the negative result).**
     The row `hippocampal_planning_v4:HPL-6` reads "MECH-205 surprise buffer + MECH-206 CA1 PE
     comparator present (sleep_substrate stack)" in the *prerequisite* column of a row whose
     status is `blocked` -- it states an unmet precondition, not a presence assertion. No flag.
  8. **SD-084's substrate is present and its validating run has landed and been reviewed.**
     `E3Selector._persistent_committed_trajectory` set at `e3_selector.py:4122`, declared
     `:543`; flag `use_persistent_committed_program_handle` default `False`
     (`config.py:5380`); consumer union at `agent.py:6799-6811`; liveness invariant enforced
     unconditionally at `agent.py:6771-6772` (`if not self.beta_gate.is_elevated: ... = None`)
     immediately upstream of its only consumer. `V3-EXQ-839` manifest: `outcome PASS`,
     `total_midexec_on 415`, `total_midexec_off 0`, `n_on_cells_attributable_with_midexec 4/4`,
     `negative_control_expectation_held true`, `non_degenerate true`. In
     `review_tracker.json`'s `reviewed_run_ids`. Contract
     `tests/contracts/test_mech321_midexec_natural_reachability.py` present.
  9. **SD-084's 2026-08-10 routing note is stale and its chip_ref does not exist.** The note
     says "Routing: queue a successor MECH-321 R4 EVIDENCE experiment (new EXQ,
     claim_ids=[MECH-321]) testing the behavioural/task effect ... Chipped
     `chip-20260810-mech321-r4-behavioural-effect`." That experiment **already ran nine days
     earlier**: `v3_exq_844_mech321_r4_midexec_task_effect_20260801T013315Z_v3`,
     `claim_ids: ["MECH-321"]`, `outcome FAIL`, `evidence_direction weakens`,
     `non_degenerate true`, label `midexec_decomposition_does_not_reduce_harm`
     (`harm_delta_mean_post_divergence -0.00326`, `rel_improvement -0.0696`,
     `effect_size_ok false`), and it is in `reviewed_run_ids`. Grep of `TASK_CHIPS.json` finds
     **no** `chip-20260810-mech321-r4-behavioural-effect`; the real chip is
     `chip-20260731-mech321-r4-successor`, `status done`, resolved `2026-07-31T19:23:09Z` --
     i.e. resolved the day *before* 844 ran. Flagged.
 10. **SD-084 carries `evidence: []` and `claim_evidence.v1.json` returns `null` for it**, which
     is *correct by construction* (V3-EXQ-839 was declared `claim_ids: []` so it weights
     nothing) but means the index shows a validated design decision as evidence-free. Flagged as
     an attribution question for governance, not as a defect in the run.

---

### MECH-206 -- CA1 acts as a PE-proportional comparator that writes episodes to the surprise buffer

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`** (not
`substrate_ceiling`): the CA1-equivalent two-channel comparator the claim's own "REE architectural
implication" paragraph specifies has never been built, and the consumer its predictions are
measured on (replay output) is verified to have no reader anywhere in `ree_core/`, so zero
non-degenerate attempts have been possible and none has been banked either way.

**Extracted from:** the claim's own `notes` -- its two explicit `Predicts:` clauses ("(1)
disrupting CA1 activity specifically (not CA3 or DG) should impair surprise buffer population
while leaving forward replay intact; (2) the CA1 mismatch signal during replay should correlate
with which features the agent subsequently treats as causally relevant") and the load-bearing
gradedness argument ("A binary match/mismatch flag would not support the priority ordering
MECH-205 requires"). Non-degeneracy precondition cross-referenced from MECH-288 rather than
re-derived (see preamble (iii)). Discriminative arm added from the MECH-285 incumbent found this
pass.

**Currency check:** (a) `claim_evidence.v1.json` -> MECH-206 is `null`: no experimental and no
literature entries credited to it. (b) `grep -rln "surprise_buffer\|SurpriseBuffer" ree_core/` ->
no matches; the only `CA1` string in `ree_core/` is
`ree_core/regulators/invalidation_trigger.py:15`, which states the CA1/CA3 comparator is
*collapsed* into a MECH-288 BoundaryEvent subscription with "No PE or latent input". (c) What
does exist is MECH-205's single-channel write: `config.surprise_gated_replay` default `False`
(`ree_core/utils/config.py:3350`), `pe_surprise_threshold 1e-5` (`:3365`, raised from 0.001 by
GFLAG-0075 2026-09-01), writing to `VALENCE_SURPRISE` at `agent.py:10677-10726`. (d) The
downstream is dead: `substrate_queue.json` -> `mech092-replay-consumer-missing`,
`status: proposed_REGISTRATION_ONLY_not_a_build_authorisation`, `unblocks_claims: [MECH-092,
MECH-205]`, implementation_hint verified against source 2026-09-01. (e) The only *built*
replay-priority ranker is `ree_core/sleep/replay_sampler.py` (MECH-285 Phase B), which ranks on
MECH-284 staleness keyed on `(scale, segment_id)` -- MECH-288's key -- is explicitly "a NO-OP
CONSUMER", and is default-off (`use_mech285_sampler`). (f) `closure_status.md:409` HPL-6 lists
"MECH-205 surprise buffer + MECH-206 CA1 PE comparator present" as an *unmet prerequisite* of a
`blocked` row -- consistent with all of the above, not a contradicting note.

**epistemic_category (proposed):** `substrate_conditional`

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (three conjuncts, all measured on the run's own data; the run is
> unreadable until all three hold).**
> (1) *Comparator exists and both channels are live.* A CA1-equivalent submodule must receive two
> genuinely distinct inputs on the same tick -- a CA3-like pattern-completed anchor
> representation and an entorhinal-like actual/variation representation -- and the run must
> report non-zero cross-tick variance in BOTH channels separately, plus a channel-decorrelation
> floor (|corr(ch_CA3, ch_EC)| < 0.95 over the window). A single-channel residual computed from
> one stream is MECH-256's comparator, not this claim's: if only one channel varies, the run
> self-routes `substrate_not_ready_requeue` and says nothing about MECH-206.
> (2) *The mismatch statistic is PE, not a latent delta.* See MECH-288's own
> `what_would_answer` LIVE GRADED-MISMATCH PRECONDITION -- **do not re-derive it**. The identical
> hazard applies here: `agent.py:5448` currently passes `pe_dict=None` to the one comparator-ish
> substrate that exists, which silently degrades it to `sum_s ||z_s(t) - z_s(t-1)||`
> (`event_segmenter.py:139-142`). Any MECH-206 test must assert its mismatch input is forward
> prediction error and record which quantity it used.
> (3) *The consumer reads.* Replay output must be consumed by something. As of 2026-09-01
> (`substrate_queue.json:mech092-replay-consumer-missing`, verified against source) `_do_replay`
> discards `replay_trajs` and no reader exists in `ree_core/`, so every DV below is currently
> unmeasurable. The run must report a non-zero count of replayed episodes that reached a
> consumer; a zero here is a substrate verdict, never a claim verdict.
>
> **CONFIRMING (two legs; leg A is the priority claim, leg B the suppression claim -- the claim
> is fully confirmed only by both, and leg A alone is the weaker "PE-tagging" reading).**
> *Leg A -- graded PE ranks replay, and does so better than the incumbent staleness ranker.*
> Three arms at matched seeds and matched replay budget: (i) CA1-comparator PE-magnitude
> priority; (ii) MECH-285 staleness priority (`replay_sampler.py`, the built incumbent); (iii)
> BINARISED CA1 priority -- the same comparator thresholded to a match/mismatch flag, which is
> the claim's own stated null ("a binary flag would not support the priority ordering MECH-205
> requires"). CONFIRMED requires BOTH: (a) rank correlation between per-episode CA1 mismatch
> magnitude and post-replay forward-model improvement on that episode's content, Spearman
> rho >= 0.3 with the 95% CI excluding 0 across >= 6 seeds; AND (b) arm (i) beats arm (iii) on
> forward-PE reduction per replay slot by a margin exceeding max(1.0 x SD of the per-seed delta,
> an absolute floor of 2% relative), with consistent sign across seeds. Arm (ii) is reported as
> the competitive baseline: MECH-206 is confirmed *as the priority signal* only if (i) is not
> beaten by (ii); if (ii) wins, MECH-206 survives only as a tagging mechanism and the priority
> claim is transferred to MECH-284/MECH-288.
> *Leg B -- retrieval suppression (Bein 2020 bidirectional shift).* On high-mismatch ticks the
> agent's reliance on the pattern-completed prediction must FALL within the same or the next
> tick: the weight/gate on the CA3-like channel into downstream selection drops monotonically
> with mismatch magnitude, with a non-zero negative slope whose CI excludes 0, and the effect
> must be specific -- no equivalent drop on a matched control channel (the EC-like actual input,
> which Bein 2020 predicts should go UP).
>
> **FALSIFYING.**
> With all three preconditions green: (a) mismatch magnitude does not rank-order post-replay
> improvement (rho CI includes 0), OR the graded arm is statistically indistinguishable from the
> BINARISED arm (iii) -- the latter is the sharpest falsifier available, because it directly
> refutes the claim's load-bearing gradedness argument while leaving "CA1 tags surprising
> episodes" intact; (b) the CA3-channel reliance does not fall with mismatch, or falls
> symmetrically on the control channel (no bidirectional shift -- a generic arousal/gain effect,
> not the claimed connectivity dissociation); (c) a CA1-specific lesion impairs forward replay
> as much as it impairs buffer population (the claim's Predict-(1) requires the dissociation, not
> just the impairment). Any of (a)+(b) together refutes the claim as stated; (a) alone with (b)
> holding demotes it to "CA1 tags, something else ranks".

**Proposal sketch (only for a/d):** n/a -- blocked. What must land first, in order:
(1) a replay CONSUMER (`mech092-replay-consumer-missing`, currently REGISTRATION-ONLY and
explicitly *not* a build authorisation; note its own scope-honesty caveat that it unblocks
MECH-092's benefit half and MECH-205 leg (iii) only); (2) a two-channel CA1-equivalent comparator
submodule, which has **no substrate_queue entry at all** and needs one before it can be built.
Until (1) and (2), MECH-206 is `complex (probe-gated)` only in the trivial sense that the probe
cannot be run.

**depends_on additions (if any):** none required (MECH-205 / MECH-092 / MECH-256 are correct, and
the 2026-09-01 SD-003 -> MECH-256 repoint is sound). Recommend adding `related_claims:
[MECH-288, MECH-287, MECH-285]` -- MECH-288/MECH-287 as the same-comparator convergence (preamble
(i)), MECH-285 as the incumbent occupying the replay-priority slot (preamble (ii).1).

**GOVERNANCE FLAG:** `contested_disposition` -- **MECH-206's functional slot has an incumbent
from within its own dependency graph.** The claim argues a graded CA1 PE readout is required to
rank episodes for replay ("a binary match/mismatch flag would not support the priority ordering
MECH-205 requires"). The only replay-priority ranker actually built,
`ree_core/sleep/replay_sampler.py` (MECH-285 Phase B), ranks by MECH-284 staleness keyed on
MECH-288 `(scale, segment_id)` -- a different signal for the same job. Governance should decide
whether MECH-206 is (i) an alternative to be tested discriminatively against MECH-285 (leg A arm
(ii) above), or (ii) complementary (tagging vs region-staleness at different timescales), and
record the decision on both claims. Also worth recording that MECH-206's comparator has no
`substrate_queue.json` entry, so it is currently invisible to the build pipeline.

---

### MECH-288 -- Event-segment detection: two-level hierarchical detector emitting outer.inner segment IDs

**Recommended disposition:** **(a) testable now** -- the substrate is built, live in-agent, and
its downstream Phase-2 consumers are all `implemented`; what has never been run is the claim's
own **primary** falsifiable prediction (boundary alignment with task-natural transitions at
above-chance rate with a bounded false-positive rate), and that is a V3-tractable experiment that
can be authored today against instrumentation the fleet already emits.

**Extracted from:** the claim's own `functional_restatement`, which already carries three
pre-registered falsifiers -- "Falsifiable (primary)" (boundary at task-natural event transitions
above chance, bounded FP rate over a noise baseline, with the hierarchical slow/fast alignment
split), "Falsifiable (secondary, downstream usefulness)" (anchor-set partitions keyed on
segment_ids beat uniform place-binning on anchor-reset latency, re-running EXQ-475 with MECH-288 +
MECH-269), and "Falsifiable (tertiary, MECH-287 coupling)" (lesioning MECH-288 silently lesions
MECH-287's broadcast trigger while tonic-arousal modulation survives). My job here is to turn
those into house structure and to add the non-degeneracy precondition they lack -- **not** to
design a new test. The precondition is new and is the substantive addition.

**Currency check:** (a) Substrate BUILT: `ree_core/hippocampal/event_segmenter.py`
(`BoundaryEvent`, `boundary_on()`, per-stream isolated detectors). (b) Default-OFF:
`use_event_segmenter: bool = False` at `ree_core/utils/config.py:2761` -- status `provisional`,
knob off. (c) Downstream Phase 2 (ii)/(iii)/(iv) ALL LANDED per `substrate_queue.json`:
`MECH-269 implemented`, `MECH-284 implemented`, `MECH-287 implemented` ("Invalidation trigger --
Phase 2(iv) ... BoundaryEvent subscriber"), `MECH-288 implemented`; the claim's 2026-07-14
`evidence_quality_note` still frames that integration as an open gate. (d) The claim's tertiary
falsifier is now *architecturally guaranteed* rather than open:
`ree_core/regulators/invalidation_trigger.py` docstring -- "The trigger is a BoundaryEvent
subscriber, NOT an independent comparator ... Trigger output is strictly a function of
(boundary_events, config). No PE or latent input", with the dissociation named as its own test
C5. (e) Exercised live in **23 indexed runs** (config scan of `evidence/experiments/*.json`),
V3-EXQ-646 -> V3-EXQ-938; V3-EXQ-938 records `boundary_fires_mean_pe_arm 276.95` /
`boundary_fires_mean_yoked_arm 287.325` over 40 seeds. (f) **None** of the 23 credits MECH-288:
`claim_evidence.v1.json` -> `genuine_exp_count 1`, `experimental_confidence 0.66`, sole
`latest_run_id` V3-EXQ-757 (2026-07-14, PASS/supports, action-free synthetic isolation),
`literature_confidence 0.86` / 11 entries, `overall_confidence 0.81`,
`evidence_quadrant confirmed_established`. (g) V3-EXQ-757 is in `reviewed_run_ids`. (h) **Spec
divergence found this pass:** `agent.py:5448` passes `pe_dict=None`, so the observation-path fast
scale runs the documented latent-delta fallback `sum_s ||z_s(t)-z_s(t-1)||`
(`event_segmenter.py:139-142`) rather than the PE-threshold detector Verdict 1 names primary;
the rollout path does pass PE (`policy_decomposition.py:581`). (i) Stale substrate docstring:
`event_segmenter.py:34` says nothing calls `input_stream="rollout"` yet -- `policy_decomposition.py`
does, and has since ARC-070/MECH-321 landed.

**epistemic_category (proposed):** `standard` (V3-tractable; substrate built and exercised; the
missing element is a run that measures the claim's own prediction, not substrate enrichment --
so explicitly **not** `substrate_ceiling` and **not** `substrate_conditional`).

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (the LIVE GRADED-MISMATCH PRECONDITION; MECH-206 and any other
> consumer claim should cross-reference this text rather than re-derive it).** Four conjuncts,
> all asserted from the run's own manifest:
> (1) *The segmenter is on and firing.* `use_event_segmenter=True` and boundary fires > 0 on
> BOTH scales in the measurement window on every measured cell. (V3-EXQ-938's
> `boundary_fires_mean_* ~= 277-287` shows this instrumentation already exists.)
> (2) *The trigger under test is the trigger the claim names.* The run MUST record which fast-scale
> input it used. `agent.sense()` currently calls `step(..., pe_dict=None, ...)`
> (`agent.py:5448`), which per `event_segmenter.py:139-142` degrades the fast scale to a
> latent-delta magnitude `sum_s ||z_s(t) - z_s(t-1)||`, NOT the PE-spike trigger of Verdict 1.
> A run that leaves `pe_dict` unset is testing the latent-change detector and must say so; it
> cannot be read as evidence for or against the PE-threshold commitment.
> (3) *Specificity is asserted per scale, not pooled.* Per V3-EXQ-757's own recorded caveat, the
> fast/inner PE-threshold scale "fires ~15% on ANY stationary z-score stream by construction",
> so it is a gradedness readout only. Any hit-rate gate must be stated separately for slow/outer
> (specificity-bearing) and fast/inner (descriptive), and the fast scale's ~15% construction
> floor must be the chance baseline it is compared against -- never 0.
> (4) *Ground-truth boundaries are independently defined.* The task-natural transition labels
> (goal-cell arrival, harm onset, mode switch, episode-phase change) must be emitted by the
> environment/harness, not derived from any quantity the detector itself consumes; otherwise the
> alignment metric is circular.
>
> **CONFIRMING (primary -- the claim's own pre-registered prediction, now made measurable).**
> An agent with MECH-288 enabled produces boundaries aligned to task-natural transitions above
> chance with a bounded false-positive rate, hierarchically split as the claim specifies:
> (a) *slow/outer* boundaries align with high-level task transitions (goal switch, episode-phase
> change) -- hit rate within a +/-2-tick tolerance window exceeding the shuffled-label chance
> baseline by more than max(1.0 x SD of the per-seed hit-rate delta, an absolute floor of 0.15
> in hit-rate units), consistent in sign across >= 6 seeds; (b) false-positive rate on a matched
> stationary/noise stretch stays below a pre-registered ceiling (V3-EXQ-757's C288_silence
> generalised to the in-agent case -- there it was 27 A-slow vs 0 B-slow); (c) *fast/inner*
> boundaries align with within-segment perceptual transitions (place-field crossing, action
> subgoal completion) above the ~15% construction floor of precondition (3), reported with its
> own CI. *Secondary (downstream usefulness), unchanged from the claim text:* per-region V_s
> readouts keyed on segment_ids produce more informative anchor-set partitions than uniform
> place-binning, measured by anchor-reset latency (the claim names re-running EXQ-475 with
> MECH-288 + MECH-269 enabled). *Tertiary (MECH-287 coupling), now near-vacuous by construction:*
> lesioning MECH-288 silently lesions MECH-287's broadcast trigger while tonic modulation
> survives -- `invalidation_trigger.py` is a pure BoundaryEvent subscriber with "No PE or latent
> input", so this is a code-level contract, not an open empirical question; keep it as a
> regression test (its C5), not as promotion evidence.
>
> **FALSIFYING.**
> With all four preconditions green: (a) slow/outer boundary times are statistically
> indistinguishable from the shuffled-label baseline -- the detector fires, but not *where the
> events are*; or (b) the false-positive rate on the stationary stretch is high enough that the
> above-chance alignment in (a) is explained by firing rate alone (formally: alignment fails once
> the chance baseline is rate-matched to the observed fire rate -- this is the sharpest
> falsifier, and it is the in-agent generalisation of the specificity caveat V3-EXQ-757 already
> flagged); or (c) the hierarchy does not separate -- slow and fast boundaries align with the
> same class of transition at the same rate, refuting Verdict 2's two-scale commitment and
> reducing the substrate to a single detector with a redundant second parameterisation; or (d)
> segment-keyed anchor partitions do not beat uniform place-binning on anchor-reset latency,
> which would refute the *reason the claim exists* (that the V_s invalidation cluster needs a
> substrate-native region partition) even if the boundaries themselves are well-placed. (d)
> alone is the disposition-changing one: it would move MECH-288 from "the region partition" to
> "a boundary detector in search of a consumer".

**Proposal sketch (only for a/d):**
- **Title:** `V3-EXQ-<next> -- MECH-288 in-agent boundary alignment: slow/fast segment boundaries
  vs task-natural transitions, rate-matched chance baseline`
- **related_claims:** `MECH-288` (primary, `claim_ids: ["MECH-288"]` -- the point of the run),
  bears_on `MECH-269`, `MECH-284`, `MECH-287`, `ARC-070`.
- **acceptance_checks:**
  1. **Precondition gates** (all four above), each with a measured value and threshold in the
     manifest's `interpretation.preconditions` block, per house recording standard.
  2. **`pe_dict` declaration gate:** the run states explicitly, per arm, whether the fast scale
     received forward PE or ran the latent-delta fallback. Recommend running BOTH as arms -- this
     is cheap, it directly adjudicates the spec/substrate divergence flagged below, and a
     difference between them is itself a finding.
  3. **C1 (slow alignment):** hit rate vs +/-2-tick tolerance window, against a **rate-matched
     shuffled-label** baseline (not a naive uniform baseline), >= 6 seeds, effect gate
     `max(1.0 x SD of per-seed delta, 0.15 absolute)`.
  4. **C2 (bounded FP):** false-positive rate on a matched stationary stretch below a
     pre-registered ceiling; the in-agent analogue of V3-EXQ-757's C288_silence.
  5. **C3 (hierarchy separation):** slow-vs-fast alignment profiles differ across the two
     transition classes (a scale x transition-class interaction), fast scale compared against its
     own ~15% construction floor.
  6. **Negative control:** `use_event_segmenter=False` arm -- zero BoundaryEvents, zero
     MECH-287 broadcasts, bit-identical action sequences, so a null in C1 can never be confused
     with an inert arm.
  7. Ground-truth transition labels emitted by the harness and recorded in the manifest, per
     precondition (4).

**depends_on additions (if any):** none. `MECH-269 / MECH-284 / MECH-287 / ARC-070` are all
correct and all now `implemented`. (Note the deps are downstream *consumers*, not upstream
prerequisites -- unusual but deliberate and documented in the inline comments; leave it.)

**GOVERNANCE FLAG 1:** `stale_note` -- **MECH-288's promotion bar is half-satisfied and the
claim text does not say so.** The `evidence_quality_note` (2026-07-14) states the
promote-to-active gate as "integration into Phase 2 (ii)+(iii)+(iv) downstream substrate plus the
falsifiable predictions above". `substrate_queue.json` now shows MECH-269, MECH-284, MECH-287 and
MECH-288 all `implemented`, and `invalidation_trigger.py` implements the Verdict-3 subscriber
architecture exactly. The integration half has landed; only the falsifiable predictions remain.
Recommend an appended note recording that, so the next governance cycle does not re-read the gate
as wholly open. Related, lower priority: `ree_core/hippocampal/event_segmenter.py:34` still says
nothing calls `input_stream="rollout"`, contradicted by `policy_decomposition.py:532/546/581`;
and the same file's header still calls MECH-288 "candidate v3_pending" though it is `provisional`
with `v3_pending: false` since 2026-07-14.

**GOVERNANCE FLAG 2:** `evidence_discrepancy` -- **the shipped fast-scale trigger is not the
trigger the claim commits to, on the observation path.** MECH-288's Verdict 1 makes "PE-spike the
primary trigger (Zacks 2007 EST canonical)" and the title names a "PE-threshold detector on the
fast scale (z_world+z_self)". `ree_core/agent.py:5448` calls
`event_segmenter.step(latent_dict=..., pe_dict=None, t=...)`, and `event_segmenter.py:139-142`
documents that with no `pe_dict` the aggregator falls back to
`sum_s ||z_s(t) - z_s(t-1)||` -- a latent-delta magnitude. So every one of the 23 indexed runs
that enabled the segmenter exercised, on the observation stream, a **latent-change** detector,
not the PE detector. (The rollout stream is unaffected: `policy_decomposition.py:581` passes
`pe=pe_signature`.) Governance should decide whether to (i) wire the observation-side `pe_dict`
and re-baseline, or (ii) amend the claim to state that the observation-side fast scale is a
latent-change detector by design with PE reserved for the rollout stream. Either way the
divergence should be on the claim before any run is read as testing the PE commitment.

**GOVERNANCE FLAG 3:** `promotion_review` -- **evidence attribution gap.** MECH-288 sits at
`experimental_confidence 0.66` from `genuine_exp_count: 1` (V3-EXQ-757, an action-free synthetic
isolation test) while its substrate ran live inside 22 further indexed experiments, none of which
names MECH-288 in `claim_ids`. Two questions for governance: (i) should any of those 22 (e.g.
V3-EXQ-904 PASS/supports, or V3-EXQ-938's `boundary_fires_mean_*` instrumentation over 40 seeds)
be credited as bearing on MECH-288 retrospectively via `bears_on`; and (ii) note the index-vs-
registry mismatch -- `docs/assets/data/claims.json` reports MECH-288 as
`assembly_state: "mature"`, `epistemic_stance: "shown"` off `overall_confidence 0.81`, while the
registry status is `provisional` with an explicitly open promote-to-active gate. This is a
derived-vs-registry reading gap of exactly the shape that has caused mis-promotions before, and
it is worth an explicit adjudication rather than leaving the two artifacts disagreeing.

---

### SD-084 -- e3.persistent_committed_program_handle: a committed-program handle that survives per-tick teardown

**Recommended disposition:** **(a) testable now** -- with the important qualification that the
question SD-084 was registered to answer (is the MECH-321 R4 mid-execution hook *reachable* under
the standard driver loop?) has **already been answered affirmatively and cleanly** by V3-EXQ-839,
so the falsifier below is written as the claim's **standing regression + residual** condition: the
untested half is the **liveness INVARIANT** the claim's own title asserts, which no run has ever
measured. Digestion is not promotion, so I recommend no status change here; the appropriate
status move (and the `evidence: []` attribution problem) is raised as a flag for `/governance`.

**Extracted from:** the claim's own `implementation_note` -- the V3-EXQ-839 acceptance criterion
taken verbatim from `failure_autopsy_V3-EXQ-830_2026-07-29.md`
(`decomp_n_evaluated_midexec > 0` on a standard `select_action -> update_residue` loop with no
hand-injected preconditions), the two pre-registered seed tiers (ATTRIBUTABLE 3/47/71/89;
NEGATIVE CONTROL 23/53), and the title's own liveness assertion ("Liveness is an INVARIANT
(reaped whenever the beta gate is not elevated), not a list of clear sites: agent.py has ten
`beta_gate.release()` sites and only five clear `_committed_trajectory`"). The residual falsifier
is that last sentence turned into a measurement. Sibling cross-reference: MECH-321's existing
`what_would_answer` owns the *behavioural* question ("does aborting a stale committed macro
improve task performance") -- SD-084's draft deliberately does not re-derive it.

**Currency check:** (a) Substrate present and matches the note exactly: declaration
`e3_selector.py:543`, set at commit entry `e3_selector.py:4122`, flag
`use_persistent_committed_program_handle: bool = False` at `config.py:5380`, consumer union at
`agent.py:6799-6811` (F-driven handle checked first, so the OFF path is byte-for-byte the legacy
`_mid_traj = self.e3._committed_trajectory`). (b) **The liveness invariant is enforced
structurally**, unconditionally, at `agent.py:6771-6772` -- `if not self.beta_gate.is_elevated:
self.e3._persistent_committed_trajectory = None` -- placed immediately upstream of its only
consumer, with a 25-line comment explaining why an invariant beats a list of clear sites. Counted
this pass: **10 real `self.beta_gate.release()` call sites** in `agent.py` (6604, 6669, 6731,
6897, 6993, 7025, 7040, 7069, 7114, 9853 -- the grep also returns 2 comment lines) against **7**
explicit `_persistent_committed_trajectory = None` clears (3650, 6680, 6737, 6772, 6907, 6999,
10673), so 4-5 release sites are covered by the invariant alone, exactly as the note describes.
(c) V3-EXQ-839 landed and PASSED: `total_midexec_on 415`, `total_midexec_off 0`,
`n_on_cells_attributable_with_midexec 4/4` (matching pre-registration exactly),
`negative_control_expectation_held true`, `non_degenerate true`,
`mean_action_divergence_frac_attributable_tier 0.159`. In `reviewed_run_ids`. (d) Contract
`tests/contracts/test_mech321_midexec_natural_reachability.py` present in `ree-v3`. (e)
`claim_evidence.v1.json` -> SD-084 is `null` and the registry block carries `evidence: []` --
correct by construction (`claim_ids: []` on the diagnostic, by design) but it leaves a validated
claim reading as evidence-free. (f) **The routing note is stale** -- see the flag below.

**epistemic_category (proposed):** `standard`. Explicitly **not** `substrate_ceiling`: the
2026-08-10 governance note already recorded "Recommended epistemic_category: standard (not
substrate_ceiling -- nothing ceilinged)", and the V3-EXQ-830 diagnosis was
`competence_implementation_gap` -- the mechanism was never reachable, not tested and found
wanting. That distinction is the group's template finding (preamble (iv)) and should be preserved
on the claim.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (three conjuncts; conjuncts 1-2 are DISCHARGED and are retained
> as the standing regression gate, conjunct 3 is what the residual test below adds).**
> (1) *Multi-action programs are committed at all.* At least one cell of EACH arm commits a
> multi-action ARC-071 chunk (`len(remaining) > 1`, gate (6) of the mid-execution conjunction).
> A seed that commits none is `substrate_not_ready_requeue`, never a substrate verdict -- this is
> exactly what the V3-EXQ-839 NEGATIVE CONTROL tier (seeds 23, 53) exists to demonstrate rather
> than assert. STATUS: met (839: `total_multi_action_commits 793`; 844 carried the identical
> precondition, measured 139 on the worst OFF cell against threshold 0).
> (2) *Pre-commit decomposition is live.* `decomp_n_evaluated_precommit > 0` -- a zero means the
> decomposition machinery is not running at all, a config error rather than a finding. STATUS:
> met (844: 1724 on the worst OFF cell; V3-EXQ-830: 1862-2618).
> (3) *Commit identity is instrumented (NEW -- the residual test needs this and no run has it).*
> Every consumed handle must be recorded together with a commit-epoch/identity token
> (`chunk_sequence` + the commit tick that installed it) and the beta-elevation epoch current at
> consumption time, so a consumed handle can be checked against the commit it claims to point at.
> Without this field the staleness DV below is unmeasurable and the run says nothing.
>
> **CONFIRMING (two legs).**
> *Leg A -- REACHABILITY (discharged; retained as regression).* With the flag ON, the
> mid-execution hook fires under a standard `select_action -> update_residue` loop with nothing
> hand-injected: `decomp_n_evaluated_midexec > 0` on the attributable tier, and `== 0` in the OFF
> arm with the arms otherwise bit-identical on the negative-control tier. CONFIRMED 2026-07-29 by
> V3-EXQ-839 (415 vs 0; 4/4 attributable seeds; 23/53 bit-identical as pre-registered) and pinned
> by `tests/contracts/test_mech321_midexec_natural_reachability.py`. Any future run showing the
> ON-arm midexec count returning to 0 refutes the claim's central assertion and means the
> teardown has been reinstated somewhere.
> *Leg B -- LIVENESS INVARIANT (the residual, never measured).* The claim's title asserts that
> liveness is an invariant, not a list of clear sites, because `agent.py` has ten
> `beta_gate.release()` sites and only some clear the handle; the invariant is the single
> unconditional reap at `agent.py:6771-6772`. CONFIRMED requires: across a run with the flag ON
> and >= 6 seeds, **zero** hook fires consume a handle whose commit-identity token differs from
> the commit currently holding beta elevated -- i.e. `n_stale_handle_consumptions == 0` with a
> non-zero denominator (>= 100 total fires, so the zero is not vacuous). The load-bearing
> adversarial condition is a beta elevation arising from a path OTHER than the commit that
> installed the handle (MECH-091 safety release/re-elevation, the rung-6 duration release, the
> SD-034 closure de-commit, and the E3-tick non-commit release are the named candidates); the
> run must demonstrate at least one such elevation occurred, or the zero is untested rather than
> earned.
>
> **FALSIFYING.**
> (a) *Leg A:* the ON-arm midexec count is 0 while preconditions (1)-(2) are green -- the handle
> is not surviving the teardown and the claim is simply false. (b) *Leg B (the live risk):* any
> non-zero `n_stale_handle_consumptions` -- the hook fires against a program whose commit has
> been released, which the note itself names as the failure the invariant exists to prevent
> ("gate (2) below would then re-open on a LATER, unrelated commit with the dead program still
> installed"). Because a mid-execution fire RELEASES THE COMMIT LATCH and aborts the remaining
> macro (the claim's own NOT-A-PURE-DIAGNOSTIC warning), a stale consumption is not a cosmetic
> defect: it aborts a *live, unrelated* committed program. (c) *Vacuity check that would void
> the whole reading:* the adversarial elevation of Leg B never occurs in the run, so the zero is
> a zero-denominator artifact -- report as `substrate_not_ready_requeue`, not as CONFIRMED.
> **Out of scope, deliberately:** whether the now-reachable hook IMPROVES task outcome. That is
> MECH-321's question -- see MECH-321's own `what_would_answer`, do not re-derive it here -- and
> it has already been answered negatively once (V3-EXQ-844 FAIL/weakens,
> `midexec_decomposition_does_not_reduce_harm`). A behavioural null on MECH-321 does **not**
> falsify SD-084; SD-084 asserts reachability and liveness, not benefit, and conflating the two
> is precisely the `competence_implementation_gap` / `substrate_ceiling` confusion this claim was
> registered to resolve.

**Proposal sketch (only for a/d):**
- **Title:** `V3-EXQ-<next> -- SD-084 handle-liveness invariant: no stale committed-program handle
  is ever consumed by the MECH-321 R4 hook` (DIAGNOSTIC; `claim_ids: ["SD-084"]` -- **not** `[]`
  this time, see flag below).
- **related_claims:** `SD-084` (primary), bears_on `MECH-321`, `ARC-071`, `MECH-090`, `MECH-091`.
- **acceptance_checks:**
  1. Preconditions (1)-(3) above, with (3) implemented as a new manifest field pairing each hook
     fire with `(commit_tick, chunk_sequence_hash, beta_elevation_epoch)`.
  2. **C1:** `n_stale_handle_consumptions == 0` over >= 6 seeds with `n_total_midexec_fires >=
     100` (839's 415 shows this volume is attainable).
  3. **C2 (adversarial coverage, the anti-vacuity gate):** >= 1 beta elevation per seed arising
     from a non-commit path -- otherwise the run self-routes `substrate_not_ready_requeue`.
  4. **C3 (regression):** Leg A re-asserted -- ON midexec > 0 on the attributable tier, OFF == 0,
     negative-control tier bit-identical between arms. Reuse V3-EXQ-839's seed tiers verbatim
     (3/47/71/89 attributable; 23/53 negative control) so the comparison is like-for-like; seed
     47 is the documented cleanest cell (OFF/ON identical on multi-action commits 30, total
     commits 72, precommit 343).
  5. Behavioural delta recorded as **non-gating payload only** (839's precedent), since a
     mid-execution fire changes committed action sequences by design.

**depends_on additions (if any):** none. `MECH-321 / ARC-070 / ARC-071 / MECH-288` are all
correct: MECH-288 is genuinely upstream here (the hook's trigger is
`event_segmenter.boundary_on(stream="rollout", ...)` via `policy_decomposition.py:581`), which
also confirms the group's 4.32 edge is a real substrate dependency, not just topic adjacency.
*Asked explicitly by the brief:* **ARC-113 does NOT depend on SD-084** -- ARC-113's `depends_on`
is `[ARC-062, ARC-063, MECH-338, MECH-316, ARC-069, ARC-070, ARC-071]`. The relationship is
indirect (SD-084 -> MECH-321 -> ARC-070/ARC-071 -> ARC-113), and SD-084 does bear on ARC-113's
"counterfactual simulation -> behavioural interaction -> outcome comparison" stage boundary by
making mid-execution re-evaluation of a committed program reachable at all. No `depends_on` edit
recommended; ARC-113 is being digested elsewhere and this is offered only as context for that
agent's use.

**GOVERNANCE FLAG 1:** `stale_note` -- **SD-084's 2026-08-10 routing block directs work that had
already been done nine days earlier, and cites a chip_ref that does not exist.** The block reads:
"Routing: queue a successor MECH-321 R4 EVIDENCE experiment (new EXQ, claim_ids=[MECH-321])
testing the behavioural/task effect of the now-reachable hook ... Chipped
`chip-20260810-mech321-r4-behavioural-effect`." That experiment is
`v3_exq_844_mech321_r4_midexec_task_effect_20260801T013315Z_v3` -- `claim_ids: ["MECH-321"]`,
`outcome FAIL`, `evidence_direction weakens`, `non_degenerate true`, interpretation label
`midexec_decomposition_does_not_reduce_harm` (`harm_delta_mean_post_divergence -0.00326`,
`rel_improvement -0.0696`, `effect_size_ok false`, `rel_floor_ok false`) -- which ran
**2026-08-01**, is in `reviewed_run_ids`, and used this claim's own `behavioural_delta` block as
its design template exactly as the routing asked. Grep of `TASK_CHIPS.json` finds **no**
`chip-20260810-mech321-r4-behavioural-effect`; the actual chip is
`chip-20260731-mech321-r4-successor`, `status done`, resolved `2026-07-31T19:23:09Z`. Two
corrections needed: (i) append to SD-084's `implementation_note` that the routed successor RAN and
returned FAIL/weakens for MECH-321 (with the run_id), so no future session re-queues it; (ii) drop
or correct the non-existent chip_ref. Note the FAIL is for **MECH-321**, not SD-084 -- SD-084's
own reachability claim is untouched by it, and MECH-321's `what_would_answer` already absorbs
844 correctly. This is a records defect, not an evidence defect.

**GOVERNANCE FLAG 2:** `promotion_review` -- **a validated design decision reads as evidence-free.**
SD-084 is `status: candidate_substrate_landed`, `evidence: []`, and `claim_evidence.v1.json`
returns `null` for it, while its validating diagnostic V3-EXQ-839 PASSed cleanly (415 vs 0,
attributability 4/4 as pre-registered, negative control held, non_degenerate), was CONFIRMED by
`failure_autopsy_V3-EXQ-839_2026-07-30`, was ratified by governance on 2026-08-10, and is in
`reviewed_run_ids`. The zero-evidence reading is an artifact of the (correct, deliberate)
`claim_ids: []` on a diagnostic. Governance should decide whether to (i) add V3-EXQ-839 to
SD-084's `evidence` / `bears_on` so the registry reflects the validation without weighting a
diagnostic as claim evidence, and/or (ii) advance the status now that the substrate is landed AND
its acceptance criterion is measured. I make no promotion recommendation -- digestion is not
promotion -- but leaving a validated claim indistinguishable from an unvalidated one is the exact
condition that produced the SD-084 defect in the first place (a mechanism that had never executed
and looked, from the registry, as though it had).

---

<!-- G1 appended 2026-09-04T21:18:57Z -->
## G1 -- sleep-phase (SD-017) hub cluster  (agent report)

### Group preamble

**Why these are together (restate, then my own view).** The assignment grouped these on
`depends_on` edges into SD-017 (SD-083 6.25, MECH-354 6.00, MECH-181 5.04) plus a
same-namespace/same-batch edge MECH-353 <-> MECH-354 (5.00). Restated: SD-017 is the offline-phase
hub and the other four are, on paper, its consumers.

**My own view: the structural edges are real but two of them are DEAD or MIS-LABELLED, and the
group's actual common property is something else entirely.** The live shape is:

- **SD-083's SD-017 edge is a PROSPECTIVE PORT edge, and the port is now unreachable.** SD-083 lives
  in the `mech457` retention TESTBED (`experiments/_lib/mech457_offline_consolidation.py`), *not* in
  `ree_core/sleep/`; the sleep plan records this deliberately ("What landed (NOT in this plan's
  substrate)", `sleep_substrate_plan.md` 2026-07-29 entry). The cognifold port into the SD-017 sleep
  loop is gated on "836b and/or 836c score SUPPORTED". Both scored `weakens`, both redesigns
  (836d/836e) scored `weakens`, and the consumer claim MECH-476 is now **`status: retired`**. The
  trigger can never fire.
- **MECH-354's SD-017 edge is genuinely live and is ALREADY PARTIALLY BUILT outside this group** --
  as `SD-SLEEP-ENTRY-PRESSURE` (`EntryPressureAccumulator` in `ree_core/sleep/mel_consumer.py`,
  ree-v3 `63e70d622c`, 2026-08-26): a Borbely Process-S running SUM with an offline `discharge()` on
  every completed sleep cycle. That is MECH-354's SLOW variant, with the wrong integrand.
- **MECH-181's SD-017 edge is live and its substrate is now complete on BOTH sides** (SD-MEL-PRODUCER
  validated 2026-07-30; SD-MEL-CONSUMER capability proven 2026-07-08).
- **MECH-353 has essentially no SD-017 content** and sits in the group only via the MECH-354 batch
  edge. That is fine -- it earns its place a different way (see (iii)/(iv)).

**The property this group actually shares: every one of them has failed, or is at risk of failing, at
the INSTRUMENT rather than at the mechanism.** 642a/642b (peak against a hard clamp), the whole
436b..436g lineage (whole-bank cosine, occupancy, write content), 969-972 (a 2-cluster Jaccard whose
attainable p-floor exceeds its own alpha), 836b (a fixed margin not scaled to per-arm noise). SD-083
is the sole exception, and it is the only one whose instrument telemetry is clean end to end. That is
why every draft below leads with a precondition about the DV's **resolvable range**, not merely about
the knob being on.

**(i) Same-claim / merge candidates.**
- **MECH-353 vs MECH-354: NOT the same claim, no merge.** Different antecedent (external constraint
  with capacity RETAINED vs. cost accumulated from one's own successful effort), opposite pole
  (assert/escalate vs. stop/disengage), different family (SD-029 comparator vs. SD-012 homeostatic).
  They share only the MECH-342 release ACTUATOR, which both claims already say explicitly. Keep
  separate.
- **MECH-354 -- PARTIAL-ABSORPTION candidate at an already-BUILT mechanism OUTSIDE the group**
  (brief rule 4g's second case). `SD-SLEEP-ENTRY-PRESSURE` already instantiates the *form* MECH-354's
  slow leg asserts: a time-integrating Process-S SUM, single crossing threshold, offline discharge on
  completed sleep, refractory floor on fire rate, default-off (`use_entry_pressure`). What it does
  NOT instantiate is MECH-354's *content*: the integrand is waking **prediction error** (MEL), not
  **effort**; there is one bound, not two; and there is no in-task STOP emission. **Expect PARTIAL
  absorption with a narrowed residual**, not supersession -- see the merge block under MECH-354.
- **SD-083 vs SD-017: no merge**, and the separation is load-bearing (different substrate, different
  optimisee -- SD-083 consolidates the testbed actor-critic `RepAgent` policy, the `ree_core/sleep/`
  cluster acts on E1/E2/E3 latents only, verified in the plan 2026-07-29).
- **MECH-181 vs SD-017 / MECH-180: no merge.** MECH-181 is a lifespan-scale consumer, not a
  granularity variant. But MECH-181 IS internally FUSED (out-of-domain epidemiology leg + testable
  REE leg) and should be SPLIT -- see its section.

**(ii) Contradictions / undercut premises.**
- **SD-083's premise is undercut at the root.** Its title and `implementation_note` define it as the
  instrument that "Unblocks MECH-476's two blocked_substrate falsifier arms". MECH-476 is
  `status: retired`, `superseded_by: [MECH-459, MECH-460]`, with `live_status.evidence.verdict`
  (2026-08-01): "WITHDRAWN per the claim's own pre-registered falsifier ... all three arms
  (dose/836a, novelty-tagging/836d, interval/836e) independently confirm retention invariant to the
  manipulated variable". SD-083 therefore currently `depends_on` a retired claim, and its own stated
  onward purpose is discharged. This does not falsify SD-083 -- the instrument did what it asserted --
  but it means SD-083's disposition must be argued on instrument validity, not on service to MECH-476.
- **SD-017's own live finding constrains MECH-181's test design.** SD-017's 2026-08-30 entry shows
  the ONLINE write path alone collapses the ContextMemory bank from mean pairwise slot cosine 0.000
  (NO_WRITES) to 0.9992 (written). So MECH-181's REE leg must NOT be posed on any ContextMemory
  differentiation DV -- it would inherit SD-017's own ceiling. It must ride the MEL -> sleep-cadence
  DV (`sws_n_writes` / `rem_n_rollouts`), which is instrument-clean and un-pinned since GAP-5b.
- **MECH-353 and MECH-354 predict OPPOSITE behaviour on a shared observable.** Repeated failure to
  achieve an intended outcome over a long window: MECH-353 predicts assert/escalate (with
  ARC-016-gated DECOMMIT only after the window), MECH-354 predicts stop-and-recover. Not a
  contradiction between the claims (the antecedents differ), but a mutual confound in any single
  experiment -- see (iv).

**(iii) Shared falsification condition -- there are TWO, and both are worth cross-referencing rather
than re-deriving.**

1. **HEADROOM ON A BOUNDED ACCUMULATOR.** The canonical statement is `failure_autopsy_V3-EXQ-642a_2026-08-30`'s
   `learning_extracted[1]`, quoted verbatim in the 642b autopsy: *"A criterion built on a PEAK of a
   hard-clamped integrator is degenerate whenever the integrator can reach its clamp ... Prefer a DV
   with headroom (mean, time-to-threshold, area under the accumulation curve) or record the
   saturation fraction alongside the peak."* This binds **MECH-353** (`z_block_cap` 1.5), **MECH-354**
   (two bounds, by construction), **MECH-181** (`mel_duration_factor` clamped to [0.5, 3.0]) and
   **SD-083** (`capture_max`, saturated at 0.989 by N=900). MECH-354's and MECH-181's drafts point at
   MECH-353's precondition (1) rather than restating it.
2. **OFFLINE-PHASE LIVENESS + PRODUCER-SUPRA-NOISE.** Shared by **SD-017** and **MECH-181**: the
   offline pass must fire (non-zero `sws_n_writes` / `rem_n_rollouts` in the ON arm, exactly 0 in the
   OFF arm -- the 436c/436d counters), AND the waking signal driving it must be measurably
   above-reference (V3-EXQ-718a's ecological MEL ~1e-5, noise-level and scrambled vs the novelty
   label, is the vacuity signature). SD-017's entire seven-run 436 lineage is a history of exactly
   these preconditions failing.

**(iv) Cross-cutting findings.**
1. **Mutual confound, asymmetric in time.** Today MECH-353 is UNCONFOUNDED by fatigue *by
   construction* -- no fatigue accumulator exists, so nothing competes for the disengage observable.
   The reverse will not hold: once MECH-354's accumulator is built, its stop/disengage DV is
   confounded by MECH-353's ARC-016-gated DECOMMIT, which fires on the same observable from the
   opposite antecedent. **Standing constraint recorded in MECH-354's draft precondition (2):** any
   MECH-354 run must set `use_blocked_agency=False` or pin `z_block`. A null on MECH-354 measured
   with z_block live would be uninterpretable.
2. **The whole group's blocker is migrating UPSTREAM in one direction, toward the
   observation -> z_world -> E1/E2 interface.** SD-017's ceiling moved write-ADDRESSING (436f) ->
   write-CONTENT (436g, 2026-08-30) -> INPUT DISTRIBUTION (V3-EXQ-972, 2026-09-02: train-time
   write-stream latents at separability 0.0281). Independently, SD-MEL-PRODUCER's fix was also an
   upstream one -- the world had to invalidate LEARNED STRUCTURE (action-map re-permutation) rather
   than add noise, because `E2.world_forward(z_world, a)` is what has to become wrong. Two
   independent threads in this group converge on the same interface.
3. **"Knob live" is not "knob efficacious", and SD-083 is the clean demonstration.** In V3-EXQ-836e
   the offline penalty was installed on 10/10 seeds in every ON arm and its coefficient varied 14x
   (0 -> 52.8 -> 86.5 -> 98.9), yet `retained_fraction` was flat (0.712 / 0.707 / 0.860 / 0.723); in
   836d the WEAKER-penalty arm retained MORE (0.950 unpaired vs 0.834 paired). **Every draft in this
   group therefore needs a POTENCY precondition, not just a liveness precondition** -- a
   demonstration that the mechanism's magnitude reaches the DV -- otherwise a null is uninterpretable.
   This is the single most reusable finding of the pass.

**Currency findings (each verified against the named file/run this session).**

| # | Finding | Source checked |
|---|---|---|
| C1 | **SD-083 `implementation_note` "NOT YET VALIDATED by experiment: V3-EXQ-836b (INTERVAL) and V3-EXQ-836c (NOVELTY) exercise it" is STALE.** All four ran: 836b + 836c 2026-07-29, redesigns 836d + 836e 2026-08-01. All `non_degenerate: true`. All four manifests name `"substrate": "SD-083 offline policy-consolidation window (ree-v3 42ab95f688)"`. | `evidence/experiments/v3_exq_836{b,c,d,e}_*.json` |
| C2 | **SD-083's consumer claim MECH-476 is RETIRED** (2026-08-01, `superseded_by: [MECH-459, MECH-460]`). SD-083 `depends_on` a retired claim, and its cognifold-port trigger ("836b/836c SUPPORTED", `sleep_substrate_plan.md` 2026-07-29) is unreachable. | `claims.yaml` MECH-476; `sleep_substrate_plan.md` |
| C3 | **SD-083 has `evidence: []` and NO entry in `claim_evidence.v1.json`**, despite four non-degenerate runs whose declared substrate IS SD-083. The runs carry `claim_ids: ["MECH-476"]` only. | `claims.yaml`; `evidence/experiments/claim_evidence.v1.json` |
| C4 | **MECH-353 `evidence_quality_note` "NO experimental evidence yet" is STALE in one direction.** Three runs have landed (642 2026-06-06, 642a 2026-08-29, 642b 2026-08-31). `v3_pending: true` remains CORRECT, but the reason has changed from "no run" to "the criterion is arithmetically dead". | `evidence/experiments/v3_exq_642*.json` |
| C5 | **MECH-353 `implementation_note` ends at "V3-EXQ-642b queued 2026-08-31 ... v3_pending remains TRUE until [it] passes".** 642b RAN and FAILED; governance ratified `non_contributory` on 2026-09-01 from confirmed `failure_autopsy_V3-EXQ-642b_2026-09-01` (REE_assembly `5ff838702b`). The note has no landing entry for it. | 642b manifest `evidence_direction_note`; autopsy .md |
| C6 | **DECISIVE, and not the falsifier question: on 642b's OWN recorded data, with the SAME pre-registered margins, swapping `z_block_peak` -> `z_block_mean` gives C1 and C2 PASS on 3/3 seeds** (separations 0.681 / 0.590 / 0.771 vs a 0.20 margin; BLOCK means 0.767-0.835 vs a 0.20 floor). No new run is needed to know the answer; a **claim-carrying** run is needed to bank it -- all of 642/642a/642b carry `claim_ids: []`. | `failure_autopsy_V3-EXQ-642b_2026-09-01.md` sections 1-2 |
| C7 | **MECH-181's mechanism now has VALIDATED substrate on BOTH sides.** `SD-MEL-CONSUMER` status `implemented`, capability PROVEN 2026-07-08 (718a injection positive control: graded MEL -> exact-monotone offline duration, DV [9,13,18,24,30,38] tracking injected [0.6..2.5], all seeds). `SD-MEL-PRODUCER` status `implemented`, **`ready: true`, `validated_utc: 2026-07-30`** (V3-EXQ-798a PASS, `producer_validated_graded_learnable`). The 2026-07-08 "producer parked" reading was UN-PARKED by the user 2026-07-21. | `substrate_queue.json` both entries |
| C8 | **SD-017 `evidence_quality_note` ends 2026-08-30 with "Routed instead to the already-frozen hypothesis_space portfolio `contextmemory_write_content_discrimination` (H1-H4, none yet queued)" -- STALE.** H1-H4 were queued and RAN as V3-EXQ-969/970/971/972, returning 2026-09-02; `failure_autopsy_contextmemory-write-content-cluster_2026-09-03.md` confirmed 2026-09-03. Verdict: none of the four adjudicated its leg (instrument resolution floor); H4 is the load-bearing measurement. | that autopsy |
| C9 | **The blocking substrate entry has moved on from SD-017's own scoping.** `contextmemory-write-path-addressing-degeneracy` is still `implemented_pending_validation` but now carries a NON-EMPTY `depends_on_unresolved` naming **SD-070 (raise z_world entropy)**, added 2026-09-03. SD-017's `pending_retest_after_substrate` scoping ("after-WRITE-PATH-CONTENT") is one level behind. | `substrate_queue.json` |
| C10 | **MECH-354: no substrate exists, and no substrate_queue entry either.** `grep -ri fatigue ree-v3/ree_core/` returns only (a) `CausalGridWorldV2`'s AR(1) observation-noise nuisance term (`fatigue_enabled/_ar_coeff/_noise_scale/_contribution_weight` -- an SD-048 interoceptive-noise source) and (b) `PCCConfig.fatigue_weight`, which SUBTRACTS SD-012 `drive_level` from a stability estimate. Neither accumulates with effort, neither has bounds, neither emits STOP. **`ARC-078` has ZERO occurrences in `ree_core/`.** | `ree-v3/ree_core/`; `substrate_queue.json` |
| C11 | **MECH-354's SLOW (Process-S) leg is PARTIALLY BUILT outside the group.** `SD-SLEEP-ENTRY-PRESSURE` (`EntryPressureAccumulator`, `ree_core/sleep/mel_consumer.py`, ree-v3 `63e70d622c`, 2026-08-26, default-off `use_entry_pressure`): a running SUM over per-step waking demand, `discharge()` on every completed sleep cycle, plus a `steps_since_sleep` refractory floor. Its own docstring names Borbely Process-S -- the same anchor MECH-354 cites. **Integrand is prediction error, not effort; one bound, not two; no in-task STOP.** | `ree-v3/ree_core/sleep/mel_consumer.py`; `sleep_substrate_plan.md` GAP-9 follow-up row |
| C12 | **SD-017 received a literature entry TODAY** (`2026-09-04_sd_017_computational_role_sleep_reorganization_yoshida2023`, `latest_timestamp_utc 2026-09-04T14:36:16Z`). Standing: exp=3 genuine (2 supports / 1 weakens), lit=19, exp_conf 0.652, lit_conf 0.908, quadrant `confirmed_established`. Worth knowing before any confidence read. | `claim_evidence.v1.json` |
| C13 | **MECH-353's own falsifier demands an ablation arm that has NEVER been run.** Its `functional_restatement` says the claim is falsified "if blocked-action behaviour is fully explained by existing harm + suffering + decommit machinery". 642, 642a and 642b all compare BLOCK vs CONTROL *with* `use_blocked_agency: true` (run-level `enabled_default_off_flags`). There has been no `use_blocked_agency=False` necessity arm. | 642b manifest `enabled_default_off_flags`; MECH-353 `functional_restatement` |

---

### SD-017 -- REE-v3 requires a minimal sleep-phase infrastructure: an SWS-analog phase (bidire...

**Recommended disposition:** (c) substrate-blocked, **`substrate_ceiling` -- UNCHANGED and correct**
(built, exercised seven times, readiness gates now clean, and the signal is absorbed by a downstream
shared mechanism), but the BLOCKING SUBSTRATE has moved and the claim's `pending_retest_after_substrate`
scoping should be re-scoped a fifth time, from "after-WRITE-PATH-CONTENT" to "after the write-content
INSTRUMENT redesign AND an input-separability probe".

**Extracted from:** the claim's own `notes` ("context representations remain undifferentiated
(cosine_sim -> 1.0)") plus the 2026-08-30 governance entry in `evidence_quality_note` (WAKING_ONLY
0.9993; NO_WRITES 0.000 vs 0.9992 once written) and the 436d-methodology-check's Recommendation #4,
whose six DV repairs 436e implemented. Nothing here is invented; this is the lineage's own accumulated
precondition list turned into house structure.

**Currency check:** verified (a) `evidence_quality_note` is current through 2026-08-30 and **stale
from 2026-09-02** -- the H1-H4 portfolio it calls "none yet queued" ran as V3-EXQ-969/970/971/972
(`failure_autopsy_contextmemory-write-content-cluster_2026-09-03.md`, confirmed 2026-09-03); (b) the
blocking substrate entry `contextmemory-write-path-addressing-degeneracy` is still
`implemented_pending_validation` and gained a `depends_on_unresolved` naming SD-070 on 2026-09-03;
(c) a fresh literature entry landed 2026-09-04 (C12). **That cluster autopsy explicitly instructs (its
section 9, item 3): "Do NOT set any `evidence_direction` or `epistemic_category` on SD-017 / ARC-045 /
MECH-166 from these runs -- they are claim-free."** This draft respects that: it changes the
falsifier's PRECONDITIONS, not the claim's evidence stamps.

**epistemic_category (proposed):** `substrate_ceiling` (unchanged).

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (four gates; the first three are met on the current substrate, the
> fourth is the one this claim now fails):
> (a) OFFLINE-PHASE LIVENESS -- pooled `sws_n_writes >= 1` and `rem_n_rollouts >= 1` in the sleep-ON
> arm and exactly 0 in WAKING_ONLY (the 436c/436d counters; 436c measured 800 / 600). A run that
> discards `run_sleep_cycle()`'s metrics dict cannot distinguish "write never fired" from "fired with
> no effect" and is inadmissible (the 436b recording gap).
> (b) WRITE-PATH LIVENESS AND OCCUPANCY -- non-zero waking write-path calls in BOTH arms (436f: 15,078)
> AND `n_occupied_slots >= 2` on `>= 3/5` seeds (436e's `sufficient_occupancy_for_c1` gate). This is
> MET only with `E1Config.contextmemory_write_usage_balancing` ON: 436g measures 16/16 occupancy on
> 5/5 seeds. No driver in `ree-v3/experiments/` sets that flag by default, so a driver written today
> silently runs the legacy argmin path and reproduces the 1-of-16 fixed point.
> (c) METRIC INTEGRITY -- the statistic must be computed over OCCUPIED slots only, with similarity and
> occupancy reported SEPARATELY and NEVER as a product (the whole-bank `slot_cosine_sim` scores a
> 12-well-separated-slot arm WORSE, 0.076, than a single-slot arm, 0.009 -- anti-correlated with what
> this claim predicts); and `context_memory.memory.requires_grad_(False)` so Adam drift cannot
> manufacture spread (the NO_WRITES arm is the run-time-derived null, tolerance 4.0 sigma; 436f
> measured max |z| = 1.67). The derived `sws_slot_diversity` (1 - `slot_cosine_sim`) inherits the same
> confound and is equally inadmissible.
> (d) INPUT-SIDE SEPARABILITY FLOOR -- the write-stream latents ENTERING `ContextMemory.write` must
> carry class structure the bank could differentiate on. Assert this with a HELD-OUT LINEAR PROBE
> (logistic regression, safe-vs-dangerous) on the recorded train-time latents, beating its own
> permuted-label null. V3-EXQ-972 measures the uncentred separability at 0.0281 (intra-class safe
> 0.9804, intra-class dangerous 0.9713, inter-class 0.9478) -- the SD-008 under-differentiation cone,
> measured at TRAINING time for the first time in this lineage -- and the 2026-09-03 cluster autopsy
> states that an uncentred cosine "does not support the stronger 'there is no structure for any
> objective to condition on'". Until this probe clears, any slot-differentiation contrast is measuring
> the input cone, not sleep.
>
> CONFIRMING: with (a)-(d) all met, in a run whose DV can resolve GRADED change (the 2-cluster
> occupied-set Jaccard is disqualified: 72 of 89 cells in the 969-972 portfolio can return only 0.0 or
> 1.0; use a mutual-information statistic over the full contingency table with `PROBE_CLUSTERS >= 4`
> and report the FRESH-cluster generalization readout as load-bearing) -- occupied-slot mean pairwise
> cosine in SWS_THEN_REM is LOWER than in a write-matched WAKING_ONLY arm by at least
> `max(1.5 * SD(per-seed paired delta), 0.05 absolute)`, on `>= 3/5` seeds, sign-consistent across
> seeds, leave-one-out stable, with OCCUPANCY MATCHED between arms so the reduction is content and not
> recruitment. SD-017's own directional prediction is the WAKING_ONLY end -- an undifferentiated bank
> without the offline phases -- and that half is ALREADY CONFIRMED at 0.9993 (V3-EXQ-436g, 2026-08-30).
>
> FALSIFYING: with (a)-(d) all met, a resolving DV, and adequate power (the 2026-08-19 pre-registered
> probe derives n = 38-2485 for a cosine contrast depending on the effect, so either meet that n or use
> a deterministic DV instead), the occupied-slot similarity contrast is null or REVERSED (sleep >=
> waking) on `>= 3/5` seeds and leave-one-out stable. Explicitly NOT falsifying: any of the seven
> 436-lineage results to date (436, 436a, 436b, 436c, 436d, 436e, 436f, 436g) -- every one failed
> upstream of the comparison, at (a), (b), (c) or a bug, which is precisely why `evidence_direction` on
> all of them is `non_contributory`.

**Proposal sketch:** N/A (disposition c). The owed work is a BUILD, not an experiment:
`contextmemory-write-path-addressing-degeneracy`'s own `implementation_hint` item (1) -- replace the
2-cluster Jaccard with a mutual-information statistic over the full contingency table, `PROBE_CLUSTERS
>= 4`, record per-draw contingency tables, size held-out splits as a FRACTION of realised class count
(970's `N_HELDOUT=200` against ~180 realised dangerous states was unreachable in 12/12 cells), and
assert objective convergence as a precondition. The re-derive brake stands at 4 substrate_ceiling hits
for SD-017 and a V3-EXQ-436h is REFUSED.

**depends_on additions (if any):** none to `claims.yaml`. Recommend instead that
`pending_retest_after_substrate` be re-scoped in the note to name BOTH the instrument redesign and the
SD-070 input-separability gate, so the scoping matches the substrate entry's own
`depends_on_unresolved` (C9).

**GOVERNANCE FLAG:** `stale_note` -- SD-017's `evidence_quality_note` closes on 2026-08-30 with
"Routed instead to the already-frozen hypothesis_space portfolio
`contextmemory_write_content_discrimination` (H1-H4, none yet queued)". H1-H4 were queued and returned
2026-09-02 as V3-EXQ-969/970/971/972; `failure_autopsy_contextmemory-write-content-cluster_2026-09-03`
is confirmed. The material update for this claim is that the ceiling has MOVED one level upstream --
from write-CONTENT to the INPUT DISTRIBUTION (H4/V3-EXQ-972, separability 0.0281), with the hedge that
H4's uncentred cosine cannot distinguish "no structure" from "no linearly-separated structure", the
cheap confirmer being a held-out linear probe. Append the landing; **do not** set
`evidence_direction`/`epistemic_category` from those four claim-free runs (that autopsy forbids it
explicitly).

---

### MECH-181 -- Cognitive reserve (produced by education, bilingualism, complex occupation, so...

**Recommended disposition:** **(c2) out_of_domain -- the claim is FUSED, and should be SPLIT**; the
epidemiology + clinical-PSG leg is `out_of_domain` and belongs in its own `research_anchor` /
`literature_synthesis` claim, while the reframed REE leg is **(a) testable now** on substrate that is
validated on both sides as of 2026-07-30.

**Extracted from:** the claim's own `notes` -- its stated mechanism chain ("complex, socially engaging,
novel activities generate substantial daily prediction error ... This drives MECH-180 (adaptive sleep
upregulation), maintaining strong SWS replay and REM simulation capacity") is already, verbatim, the
SD-MEL-PRODUCER -> SD-MEL-CONSUMER pathway that exists in `ree_core/sleep/mel_consumer.py`. The
falsifier below is that chain instrumented, plus MECH-181's own distinctive "reserve" content (matched
insult, differential retention). The out-of-domain leg is the `notes`' "Novel prediction" paragraph.

**Currency check:** verified against `substrate_queue.json` and `ree_core/`:
- `SD-MEL-CONSUMER` status `implemented`; consumer capability PROVEN 2026-07-08 (confirmed
  `failure_autopsy_V3-EXQ-718a_2026-07-08`): the injection positive control shows graded MEL ->
  exact-monotone graded offline duration, DV `[9,13,18,24,30,38]` tracking injected `[0.6..2.5]` on all
  seeds.
- **`SD-MEL-PRODUCER` status `implemented`, `ready: true`, `validated_utc: 2026-07-30`** -- V3-EXQ-798a
  PASS, `producer_validated_graded_learnable` (confirmed `failure_autopsy_V3-EXQ-798a_2026-07-30`). The
  knob is `world_rule_shift_enabled/_interval/_depth/_scope` on `CausalGridWorldV2`
  (`ree_core/environment/causal_grid_world.py` ~line 755+): it periodically re-permutes the
  action -> displacement map so `E2.world_forward(z_world, a)` becomes systematically wrong until
  re-learned. This is the FIX for the exact failure MECH-181's chain previously hit.
- The 2026-07-08 "ecological demonstration re-parked" note is superseded: the user **UN-PARKED** it on
  2026-07-21 (`SD-MEL-PRODUCER.note`). The re-derive brake that fired in 2026-07-08 refused a
  *same-environment* re-grade (no V3-EXQ-718b); the new environment is the sanctioned entry point,
  named in SD-MEL-CONSUMER's own note ("the entry point is a NEW graded-MEL environment/test-bed").
- The ecological end-to-end MECH-180 run that the producer entry says it now enables is described as
  "still-gated, separately-queued" and is **NOT in `ree-v3/experiment_queue.json`** (3 items:
  V3-EXQ-1002, 983a, 993a). It is owed and unqueued.

**epistemic_category (proposed):** `standard` **for the reframed REE leg**. If governance declines the
split and keeps the claim as written (dementia incidence at matched pathological burden; PSG response
to enrichment sessions), then `out_of_domain` is the correct stamp and no REE experiment can move it.
This is a real fork and should be decided explicitly rather than inherited.

**Draft `what_would_answer`** (REE leg; the out-of-domain leg's proof obligation is stated after it):

> NON-DEGENERACY PRECONDITION (five gates):
> (1) PRODUCER SUPRA-REFERENCE -- the graded-enrichment arms must produce a measured waking MEL
> gradient ABOVE the calibrated stable-base reference. The vacuity signature is V3-EXQ-718a's: measured
> ecological MEL ~1e-5, noise-level and SCRAMBLED with respect to the novelty label, with
> `conv_rel_drop ~0.98`. Grade novelty with SD-MEL-PRODUCER's `world_rule_shift_*` knob (action-map
> re-permutation), NEVER with `env_drift_interval` -- V3-EXQ-677 measured a high-vs-low mean-PE
> difference of 8.8e-07 against a 0.01 threshold on that knob, because moving hazards adds sampling
> noise, not learning load.
> (2) THE GRADIENT MUST BE LEARNING LOAD, NOT NOISE -- elevated PE counts only if it DECAYS within a
> stationary window; `steps_since_world_rule_shift` is emitted in env `info` for exactly this. A
> matched-PE OBSERVATION-NOISE negative-control arm must NOT reproduce the effect (grading observation
> noise produces a monotone MEL ladder by construction on any substrate -- the DV-symmetry artifact
> class, and the reason V3-EXQ-798a carried this control).
> (3) CONSUMER LIVE AND UN-PINNED -- `use_mel_consumer=True`, and cumulative `sws_n_writes` /
> `rem_n_rollouts` must VARY across arms. The vacuity signature is V3-EXQ-677's scheduler-pinned
> SWS=80.0/80.0, REM=60.0/60.0 with zero cross-arm variance.
> (4) HEADROOM -- `mel_duration_factor` is clamped to `[mel_duration_factor_min 0.5,
> mel_duration_factor_max 3.0]`. If the top arm saturates at 3.0 the contrast is a cap artefact; report
> the per-arm saturation fraction alongside the factor. This is the same shape as MECH-353's
> precondition (1) -- see MECH-353's own `what_would_answer`, do not re-derive.
> (5) CHANNEL ATTRIBUTION -- an ENRICHED arm with `use_mel_consumer=False` must show the SAME
> offline-phase duration as an IMPOVERISHED arm with the consumer off, so any enrichment effect is
> attributable to the MEL channel rather than to enrichment changing episode length or boundary count
> (note that under the boundary-only trigger, episode count IS sleep count -- `sleep_substrate:GAP-9`).
>
> CONFIRMING (two legs; both are required, and the second is MECH-181's distinctive content over
> MECH-180):
> (i) MAINTENANCE -- across `>= 3` enrichment levels (impoverished / moderate / enriched) at `>= 5`
> seeds, measured above-reference waking MEL is monotone in enrichment level, AND cumulative
> offline-phase work (`sws_n_writes + rem_n_rollouts`) is monotone in MEASURED MEL -- not in the
> novelty LABEL, the distinction on which V3-EXQ-718's C1 failed 0/3 while its C2 passed 3/3 -- on
> `>= 3/5` seeds.
> (ii) RESERVE -- after a MATCHED degradation insult applied identically to both histories (a fixed
> ablation of ContextMemory slots, or fixed noise injected into the E3 attribution path; identical
> magnitude, identical schedule, applied after the enrichment phase), the ENRICHED-history agent
> retains more attribution/competence than the IMPOVERISHED-history agent, by
> `max(1.5 * SD(per-seed paired delta), an absolute floor derived from the consumer-OFF arm's spread)`,
> on `>= 3/5` seeds. This is the only leg that tests "reserve" rather than "responsiveness", and it is
> what makes MECH-181 more than a restatement of MECH-180.
>
> FALSIFYING: with (1)-(5) met, ANY of --
> (i) offline-phase work is flat or non-monotone in MEASURED MEL (the maintenance chain does not close);
> (ii) at matched insult, enriched and impoverished histories show no retention difference (there is no
> reserve, only responsiveness);
> (iii) DECISIVE -- the retention difference SURVIVES with `use_mel_consumer=False`. MECH-181 asserts
> specifically that the protection runs THROUGH the MEL-driven sleep loop; a difference that persists
> with the loop disabled is an environment/exposure effect and refutes the claim's mechanism even
> though it would leave the epidemiology untouched.

**Out-of-domain leg, stated so it is not lost in the split.** Proof obligation: the epidemiological
premise (education, bilingualism, occupational complexity and social engagement reduce clinical
dementia incidence and delay onset at MATCHED pathological burden -- Stern 2009, Lancet Neurology) and
the clinical prediction (enrichment sessions produce measurable PSG change -- increased SWA, increased
spindle density -- on following nights, within weeks and BEFORE any cognitive improvement is
measurable, distinguishing restored learning drive from improved mood). A counterexample is a
controlled enrichment trial in early dementia showing cognitive/mood benefit with NO PSG change on the
same timescale, or PSG change with no dose-relation to enrichment intensity. No REE substrate at any
level bears on either; this resolves by literature and by clinical trial, and per the epistemic-category
table these belong as `research_anchor` / `literature_synthesis` rather than as a mechanism hypothesis.

**Proposal sketch (leg (a) of the split):**
- **title:** "MECH-181/MECH-180 ecological cognitive-reserve chain: graded world-rule-shift novelty ->
  above-reference waking MEL -> graded offline-phase work -> differential retention at matched insult"
- **related_claims:** MECH-181 (primary), MECH-180, INV-050, INV-049, SD-017, MECH-204
- **acceptance_checks:** all five preconditions above emitted as explicit P0 gates (producer
  supra-reference with the decay check; the matched-PE noise negative control; consumer un-pinned;
  saturation fraction reported; consumer-OFF attribution arm); `claim_ids` naming MECH-181 and MECH-180
  with per-claim direction; monotonicity scored against MEASURED MEL not the novelty label;
  `>= 5` seeds; leave-one-out reported in-line.
- **Sequencing note:** leg (i) is runnable TODAY with zero new build (both substrates validated, all
  knobs present). Leg (ii) needs a small insult harness (slot ablation / E3 noise injection), which is
  `complicated (buildable)`, not probe-gated. Do not mint this as a fresh lineage if the
  "still-gated, separately-queued MECH-180 ecological end-to-end run" is scheduled -- MECH-181's leg (i)
  IS that run plus a per-claim tag, and leg (ii) is one extra phase on the same driver.

**depends_on additions (if any):** none in `claims.yaml`. Record `SD-MEL-PRODUCER` and
`SD-MEL-CONSUMER` in an `implementation_note` (they are substrate-queue ids, not claims).

**GOVERNANCE FLAG:** `stale_note` -- the standing "INV-050 / MECH-180 MEL producer is parked / blocked"
reading (SD-MEL-CONSUMER's 2026-07-08 re-park note, and the corresponding session memory) is superseded
twice over: the user un-parked it 2026-07-21, and `SD-MEL-PRODUCER` reached `ready: true` /
`validated_utc: 2026-07-30` on V3-EXQ-798a PASS. MECH-181's REE leg is no longer substrate-blocked, and
the ecological end-to-end run that both substrate entries name as owed is **not in the live queue**.
Secondary: MECH-181 is FUSED (out-of-domain epidemiology + testable REE mechanism) -- recommend a split
decision at governance, since the epistemic_category depends entirely on which leg the claim is taken to
assert.

---

### MECH-353 -- Blocked-agency / control-failure affect stream (z_block): an integrated readou...

**Recommended disposition:** **(a) testable now** -- the substrate is built, calibrated and
demonstrably working; all three failures to date are one measurement defect (a peak statistic against a
hard clamp), and the deciding statistic is ALREADY in the 642b manifest passing 3/3 at the
pre-registered margins.

**Extracted from:** the claim's own `functional_restatement` "Falsifiable:" clause (the assert/persist
signature, the z_harm_a dissociation under matched controllability, and the "fully explained by
existing machinery" necessity condition), sharpened by `failure_autopsy_V3-EXQ-642b_2026-09-01` sections
2-4. This is extraction, not fresh design.

**Currency check:** verified:
- `evidence_quality_note`'s "NO experimental evidence yet" is stale as to RUNS (642 2026-06-06, 642a
  2026-08-29, 642b 2026-08-31) though correct as to BANKED evidence -- all three carry `claim_ids: []`,
  so `claim_evidence.v1.json` has **no MECH-353 entry at all** and `v3_pending: true` correctly stands.
- `implementation_note` ends at "V3-EXQ-642b queued 2026-08-31 ... v3_pending remains TRUE until [it]
  passes"; 642b RAN and FAILED, and governance ratified `non_contributory` 2026-09-01 from confirmed
  `failure_autopsy_V3-EXQ-642b_2026-09-01`. The note has no landing entry.
- **The substrate WORKS.** Against the 642a autopsy's own stated success target, CONTROL-arm
  `z_block_mean` fell from 1.26-1.35 (legacy absolute floor) to **0.064-0.177** of a 1.5 cap, and
  BLOCK-CONTROL mean separation improved **4.1x-9.3x**. Readiness gates all met: `world_forward` C0
  probe margin 0.508-0.624 against a 0.1 floor, `world_encoder` tensors moved 4/4 on every seed.
  C0 PASS 3/3, C3 (assert-not-withdraw) PASS 3/3.
- `substrate_queue` entry `sd_blocked_agency_mismatch_floor_calibration` is
  `implemented_pending_validation`, severity deliberately LEFT at `corrupting` -- because CONTROL
  `z_block_peak` still reaches 1.500 on 3/3 seeds, so any NEW experiment reading a peak-shaped
  blocked-agency DV still gets a zero separation that LOOKS like a valid negative. That is the live
  trap this draft's precondition (1) exists to close.
- The `z_goal_stream.writer_defect` flag on 642b is a **detector false positive** (the driver pins the
  goal directly, `GOAL_PIN=0.5`, bypassing the counted writer) -- do not treat it as a recording gap.

**epistemic_category (proposed):** `standard`. **Explicitly NOT `substrate_ceiling`** -- the claim's own
`live_status.evidence` from the 2026-06-06 autopsy already directs this ("characterise as a measurement
/ test-design gap, NOT substrate_ceiling. Do not record substrate_ceiling on any claim from this run"),
and 642a/642b reconfirm the same shape: readiness gates pass, no downstream mechanism absorbs the
signal, the criterion is arithmetically dead.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (four gates):
> (1) HEADROOM ON THE DECIDING STATISTIC -- the criterion must NOT read `z_block_peak`, nor any max or
> difference-of-maxima against `z_block_cap` (1.5, `ree_core/affect/blocked_agency.py:153`). Both arms
> touched exactly 1.500 on 3/3 seeds in BOTH 642a and 642b, so `z_block_separation` was 0.0 by
> arithmetic regardless of behaviour. Use `z_block_mean` (or time-above-threshold, or area under the
> accumulation curve) and REPORT the per-arm saturation fraction alongside it.
> (1b) DO NOT SUBTRACT A STRUCTURALLY-ZERO TERM -- 642's C2 was
> `(z_block_sep - z_harm_a_sep) >= C2_MARGIN`, and `z_harm_a_sep` is a structural 0.0 because harm is
> held at zero by design in this env, so C2 merely inherited C1's zero with nothing to offset it. State
> the dissociation POSITIVELY: "z_block separates on a headroom statistic AND z_harm_a does not", each
> tested against its own margin.
> (2) DETECTOR READINESS (already met; keep as a gate) -- the SD-029 comparator must be discriminative:
> `world_forward` C0 probe margin `>= 0.1` on the P0a+P0b-trained substrate (642b measured
> 0.508/0.532/0.624), and P0 warmup must have MOVED `split_encoder.world_encoder` tensors (642b: 4/4 on
> every seed), i.e. z_world is a prediction-trained encoder and not a frozen random projection. An
> untrained encoder makes the whole detector vacuous -- that was V3-EXQ-642's original 2026-06-06
> failure.
> (3) CALIBRATION LIVE -- `blocked_agency_outcome_mismatch_floor_mode = "baseline_relative"`, and the
> CONTROL arm's `z_block_mean` must sit well below cap. 642b: 0.064-0.177 of 1.5 (PASS). 642a's legacy
> absolute mode: 1.26-1.35 (the vacuity signature -- z_block accumulating on ordinary world-model error).
> (4) THE RUN MUST CARRY `claim_ids: ["MECH-353"]`. V3-EXQ-642, 642a and 642b are all claimless
> diagnostics, so however they score they bank nothing for or against this claim. This is why
> `claim_evidence.v1.json` has no MECH-353 entry despite three completed runs.
>
> CONFIRMING: in `CausalGridWorldV2` with `scheduled_action_block_*` (external move-cancel, no damage,
> no layout change) and with harm and goal-value held constant, on `>= 3/5` readiness-cleared seeds:
> (i) `z_block_mean(BLOCK) - z_block_mean(CONTROL) >= 0.20` with `z_block_mean(BLOCK) >= 0.20` -- 642b's
> already-recorded values are 0.681 / 0.590 / 0.771 and 0.767-0.835, i.e. 3/3 on the same margins;
> (ii) DISSOCIATION -- `z_harm_a` shows no separation of comparable magnitude under the same
> manipulation, and under a MATCHED controllability manipulation with capacity-belief COLLAPSED the
> response flips to the SD-019b withdraw signature (the hand-off the claim asserts) rather than
> persisting as assert;
> (iii) BEHAVIOUR -- the BLOCK arm shows effort escalation and/or alternative-action search relative to
> CONTROL (the MECH-320 vigor signature; C3 in 642a/642b, already PASS 3/3), with DECOMMIT (MECH-342,
> ARC-016-gated) appearing only after the assertion window rather than in place of it;
> (iv) NECESSITY -- an arm with `use_blocked_agency=False` and everything else identical does NOT
> reproduce the BLOCK-arm behavioural signature.
>
> FALSIFYING: with (1)-(4) met, ANY of --
> (i) `z_block` fails to separate BLOCK from CONTROL on a headroom statistic under a genuine external
> block;
> (ii) it separates but `z_harm_a` separates by a comparable amount under the same manipulation (the
> signal is harm re-labelled, not a distinct stream);
> (iii) DECISIVE, and the leg this lineage has NEVER run: the `use_blocked_agency=False` arm reproduces
> the blocked-action behaviour using only the existing harm (SD-011) + suffering (SD-019b) + decommit
> (MECH-342/ARC-016) machinery. The claim's own falsifier text names exactly this condition, and every
> run to date has compared BLOCK vs CONTROL with `use_blocked_agency: true` at run level -- so the
> necessity question is untested.

**Proposal sketch (a):**
- **title:** "V3-EXQ-642c -- MECH-353 z_block discriminative validation on a HEADROOM statistic, with a
  `use_blocked_agency=OFF` necessity arm"
- **related_claims:** MECH-353 (primary, direction to be scored); bears_on SD-029, MECH-112, MECH-320,
  MECH-342, ARC-016, SD-011, SD-019b, SD-070, SD-056
- **acceptance_checks:**
  1. `claim_ids: ["MECH-353"]` -- NOT a claimless diagnostic (the single most important change from
     642/642a/642b).
  2. C1/C2 recomputed on `z_block_mean` at the UNCHANGED pre-registered margins (`C1_MARGIN 0.20`,
     `Z_BLOCK_MIN 0.20`, `C2_MARGIN 0.20`) -- moving the STATISTIC off a provably dead one is not the
     same as moving a threshold to fit a result, and the 642b autopsy makes exactly this distinction.
  3. Per-arm `z_block` SATURATION FRACTION recorded alongside every statistic.
  4. C2 restated positively (z_block separates AND z_harm_a does not), not as a difference of
     separations.
  5. NEW ARM: `use_blocked_agency=False` necessity ablation, scored on the behavioural DV.
  6. Seeds raised from 3 to 5 (642b's `SEED_PASS_FRACTION` is 0.667; at n=3 that is 2 seeds).
  7. P0 gates retained verbatim from 642a/642b (`world_forward_c0_margin_supra_floor >= 0.1`,
     `zworld_world_encoder_trained`), plus `blocked_agency_outcome_mismatch_floor_mode ==
     "baseline_relative"` asserted in the manifest.
- **Note for the author:** the answer is very likely already known (C6). The purpose of the run is to
  BANK it under a claim id on a criterion that can express it, and to settle (iv)/(iii), which no
  existing data touches.

**depends_on additions (if any):** consider adding **SD-070** and **SD-056** to MECH-353's `depends_on`.
Both are hard preconditions of the detector -- `implementation_note` already says "the action-outcome
comparator is only discriminative once the encoder + action-conditional world_forward (SD-056) are
trained" -- and both appear in every 642-lineage run's `bears_on` while being absent from the claim's
`depends_on`.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- V3-EXQ-642b's own manifest already contains the deciding
statistic and it PASSES: swapping `z_block_peak` -> `z_block_mean` at the SAME pre-registered margins
gives C1 and C2 on 3/3 seeds (separations 0.681 / 0.590 / 0.771 vs a 0.20 margin; BLOCK means
0.767-0.835 vs a 0.20 floor), while the recorded `outcome` is FAIL and `evidence_direction` is
`non_contributory`. This is not a request to re-score 642b -- it is claimless and correctly banks
nothing -- but the gap between "what the substrate demonstrably does" and "what the registry records"
is now 3 runs and ~3 months wide, and a single claim-carrying V3-EXQ-642c on a headroom statistic could
clear MECH-353's `v3_pending`. Secondary: the substrate entry
`sd_blocked_agency_mismatch_floor_calibration` remains `implemented_pending_validation` with severity
`corrupting` precisely because the peak trap is still live for any NEW experiment -- the fix is a
headroom-DV REQUIREMENT on this substrate, not a severity downgrade.

---

### MECH-354 -- Effort/fatigue stop-recover homeostatic accumulator: a two-bound (hysteretic) ...

**Recommended disposition:** **(c) substrate-blocked, `substrate_conditional`** -- the two-bound
hysteretic effort accumulator does not exist anywhere in `ree_core/`, has no `substrate_queue` entry,
and its named consumer ARC-078 has zero occurrences in the substrate, so zero non-degenerate
experimental attempts are currently possible and no evidence has been or could have been banked either
way. (A PARTIAL-absorption merge proposal for the SLOW leg follows, PROPOSE-ONLY.)

**Extracted from:** the claim's own `functional_restatement` "Falsifiable:" clause, which already names
the three legs (a) time-on-task independent of harm/controllability, (b) incentive-reversibility, (c)
rest-recovery. The draft turns those into house structure and adds the preconditions the group's
measurement history makes mandatory.

**Currency check:** verified against `ree-v3/ree_core/` and `substrate_queue.json`:
- **No fatigue accumulator exists.** `grep -ri fatigue ree-v3/ree_core/` returns exactly two families,
  neither of which is MECH-354's: (a) `CausalGridWorldV2`'s `fatigue_enabled / fatigue_ar_coeff 0.995 /
  fatigue_noise_scale / fatigue_contribution_weight` -- an AR(1) *observation-noise* drift term, i.e.
  the SD-048 interoceptive nuisance source, explicitly a stochastic attractor audited by `INF-ENV-004`;
  and (b) `PCCConfig.fatigue_weight 0.5` in `ree_core/cingulate/pcc_analog.py`, which SUBTRACTS SD-012
  `drive_level` from a stability estimate (`stability -= fatigue_weight * drive`). Neither accumulates
  with effort, neither has bounds, neither emits STOP, neither recovers with rest.
- **`ARC-078` has ZERO occurrences in `ree_core/`.** The claim's named cost/benefit consumer is
  unimplemented.
- **No `substrate_queue` entry exists** for MECH-354 or for an effort/fatigue accumulator. So this is
  not even "queued but unbuilt" -- it is unregistered.
- The environment DOES have a decoupled effort axis to build against:
  `effort_harm_coupling_enabled / _scale / _depletion_weight` and the Q-080.b control lever
  `effort_benefit_asymmetry` (`causal_grid_world.py` ~line 755), the latter explicitly documented as
  the positive control proving the effort machinery is non-vacuous.

**epistemic_category (proposed):** `substrate_conditional`. **Blocking substrate (unregistered, name it
when queueing):** a two-bound hysteretic effort/time-on-task accumulator on the SD-012 homeostatic side
(hosted by the SD-048 interoceptive channel), emitting an in-task STOP into MECH-342 as a NEW deficit
input alongside the R-c execution-readiness deficit, with the recover half on SD-012/SD-017 and an
ARC-078 cost/benefit consumer.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (five gates; gate (0) is currently UNMET and every gate below it is
> conditional on the build):
> (0) EXISTENCE -- an F accumulator with TWO bounds must exist and be reachable from the agent loop.
> It does not today: `ree_core/` contains no effort-driven accumulator, `ARC-078` appears nowhere, and
> the only two things named "fatigue" are an environment observation-noise AR(1) term and a PCC
> stability subtrahend reading SD-012 `drive_level`. Until (0) is satisfied this claim is untestable in
> principle, not merely unqueued.
> (1) TWO-BOUND LIVENESS AND HEADROOM -- BOTH bounds must be reached and neither pinned: each seed must
> show F crossing the UPPER bound at least once AND recovering to the LOWER bound at least once, with
> the fraction of steps spent at each bound reported. An F pinned at either bound reproduces the exact
> V3-EXQ-642a/642b degeneracy -- see MECH-353's own `what_would_answer` precondition (1) for the full
> statement of why a bounded-accumulator DV must have headroom; do not re-derive it here.
> (2) DISCONFOUNDING FROM z_block (MECH-353) -- the run MUST set `use_blocked_agency=False`, or pin
> `z_block` to a constant. MECH-353's ARC-016-gated DECOMMIT fires on the SAME observable
> (disengagement) from the OPPOSITE antecedent (external block with capacity retained). With both live,
> a stop/disengage DV cannot attribute, and a null on MECH-354 would be uninterpretable.
> (3) HARM AND CONTROLLABILITY PINNED -- `z_harm_a` and the SD-019b/Q-036 escapability gate held
> constant across the time-on-task axis. If they drift, the disengage is the suffering pole, which is
> precisely the DEV-NEED-002 conflation this claim exists to cure.
> (4) THE EFFORT AXIS MUST BE REAL AND DECOUPLED FROM HARM -- use `CausalGridWorldV2`'s
> `effort_harm_coupling_enabled=False` setting so effort cost is not a harm proxy, and run the Q-080.b
> `effort_benefit_asymmetry > 0` positive control to prove the effort machinery is non-vacuous before
> reading any negative result.
>
> CONFIRMING (three legs, matching the claim's own (a)/(b)/(c); all three are required, since (a) alone
> is shared with the suffering pole):
> (a) TIME-ON-TASK -- disengagement hazard rises monotonically with time-on-task at FIXED harm and FIXED
> controllability, on `>= 3/5` seeds, effect `>= max(1.5 * SD(per-seed delta), an absolute floor derived
> from the F-OFF arm's spread)`.
> (b) INCENTIVE-REVERSIBILITY -- raising incentive at a FIXED accumulated F measurably delays or cancels
> the STOP. This is the leg that discriminates the Boksem-Tops cost/benefit recalibration account from a
> pure-depletion account, which predicts no incentive effect at fixed F.
> (c) REST-RECOVERY, THE DECISIVE DISSOCIATOR -- after a rest / offline phase, re-engagement latency and
> disengagement hazard return toward baseline, AND a matched suffering/learned-helplessness arm
> (uncontrollable aversion, SD-011/SD-019b) run on the SAME DV shows NO rest-recovery. Without the
> matched comparison arm this leg is not a dissociation, only a description.
>
> FALSIFYING: with the accumulator built and (1)-(4) met, ANY of --
> (i) (a) holds but (b) and (c) do not -- the stop is neither incentive-reversible nor rest-recoverable,
> so on its OWN decisive dissociator the signal is indistinguishable from the SD-011 suffering pole and
> MECH-354's claim to be a separate stream on the SD-012 side is refuted;
> (ii) (c) holds but the matched helplessness arm ALSO recovers with rest -- rest-recovery is then not
> the dissociator the claim rests on;
> (iii) PARSIMONY -- feeding the EXISTING SD-012 `drive_level` (which MECH-342 and the PCC already read)
> directly into MECH-342 as a deficit input reproduces (a), (b) and (c) without any two-bound hysteretic
> accumulator. MECH-354 asserts the "smallest computational form" is Meyniel's two-bound accumulator; if
> a one-bound leaky drive suffices, the claim is over-specified and should be narrowed rather than
> confirmed.

**Proposal sketch (only for a/d):** N/A -- disposition (c). The owed work is an `/implement-substrate`
build with no open question (`complicated (buildable)`), which should be REGISTERED in
`substrate_queue.json` first, since no entry exists today.

**depends_on additions (if any):** add **MECH-353** to MECH-354's `depends_on` -- not as a dependency of
the mechanism but as a recorded CONFOUND edge, since precondition (2) makes MECH-354's testability
conditional on z_block's state. If governance prefers not to overload `depends_on` with confound edges,
record it in `notes` instead, but record it somewhere machine-visible: it is the kind of constraint that
gets rediscovered by a failed run.

**MERGE PROPOSAL (g) -- PROPOSE ONLY, partial absorption with a narrowed residual.**
- **Surviving mechanism (already BUILT, outside the group):** `SD-SLEEP-ENTRY-PRESSURE` --
  `EntryPressureAccumulator` in `ree-v3/ree_core/sleep/mel_consumer.py` (ree-v3 `63e70d622c`,
  2026-08-26, default-off `use_entry_pressure`; `sleep_substrate_plan.md` GAP-9 follow-up row).
- **Partially absorbed:** MECH-354's SLOW "sleep-pressure (Process-S) variant whose recover phase is
  offline (SD-017)". The built mechanism already supplies: a time-integrating running SUM over per-step
  waking demand that grows monotonically with waking steps; a crossing threshold
  (`entry_pressure_threshold`, scaled by `entry_pressure_gain`); an OFFLINE reset (`discharge()` on
  every completed sleep cycle); and a refractory floor bounding fire rate. Its own docstring cites
  Borbely Process-S -- the same anchor MECH-354 cites (Borbely et al. 2016, J Sleep Res).
- **NOT absorbed -- the narrowed residual, which is MECH-354's real remaining content:** (1) the
  INTEGRAND is waking PREDICTION ERROR (MEL), not EFFORT -- so the built accumulator is a
  learning-demand drive, not a cost drive, and MECH-354's distinctive antecedent ("accumulates from your
  own successful effort") is untested; (2) it is ONE-bound, not two -- there is no lower recovery bound
  and no hysteresis, only a discharge-to-zero; (3) it emits SLEEP ENTRY, not an in-task STOP, so nothing
  reaches MECH-342 or ARC-078; (4) the entire FAST within-task variant is absent.
- **Reverse-deps needing repointing if governance accepts any absorption:** none in `claims.yaml` --
  `grep MECH-354` returns no other claim's `depends_on`. MECH-354's OWN `depends_on` (SD-012, SD-048,
  MECH-342, ARC-078, SD-017, SD-011) is unaffected. So the absorption is cheap: it narrows MECH-354's
  text, it does not re-point a graph.
- **Recommended framing:** do NOT retire MECH-354. Narrow its slow leg to the single testable residual
  "**the Process-S entry-pressure accumulator's integrand should be EFFORT, not prediction error**" --
  which is a small, well-posed, buildable comparison on an EXISTING mechanism (swap the integrand behind
  a flag, compare entry timing under a graded effort axis at fixed MEL) -- and keep the FAST two-bound
  in-task accumulator as MECH-354's own unbuilt content. Expect PARTIAL absorption, not supersession.

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-354 is registered `candidate` with
`v3_pending: true` and reads as ordinary pending-experiment work, but nothing has been built, nothing is
queued, and it has no `substrate_queue` entry, while a mechanism implementing a substantial part of its
SLOW leg (`SD-SLEEP-ENTRY-PRESSURE`) landed 2026-08-26 with no cross-reference in either direction.
Governance should decide (i) whether to register the fast accumulator as a substrate-queue build, and
(ii) whether to accept the partial absorption above and narrow the slow leg to the integrand question.
Leaving it as-is means a future session re-derives a fatigue accumulator without noticing that a
Process-S accumulator with an offline discharge already exists in `ree_core/sleep/`.

---

### SD-083 -- consolidation.offline_policy_consolidation_window: an OFFLINE, trace-selective ...

**Recommended disposition:** **(a) testable now -- and legs (i)-(iii) are ALREADY ANSWERED CONFIRMING by
banked, non-degenerate telemetry in V3-EXQ-836d and V3-EXQ-836e.** Only leg (iv) (trace selectivity,
per-parameter-group Fisher mass) lacks a readout, and that is a manifest addition or a reanalysis of
recorded state, NOT a new experiment. Governance's real work on this claim is evidence ROUTING and a
`depends_on` repoint, not a run.

**Extracted from:** the claim's own title and `implementation_note`, which state four checkable
properties (interval-accumulated capture `c(N)=capture_max*(1-exp(-N/tau))`; novelty gating; trace
selectivity via Fisher of the policy log-likelihood; and the orthogonality assertion "BUILDS PROTECTION
without retraining, so post_bc is invariant to the interval"). Turned into an instrument-validity
falsifier and checked against the per-arm telemetry actually recorded in 836d/836e.

**Currency check:** verified -- and this claim's registry state is the most stale in the group:
- `implementation_note` says "**NOT YET VALIDATED by experiment**: V3-EXQ-836b (INTERVAL) and
  V3-EXQ-836c (NOVELTY) exercise it". Both ran 2026-07-29; the noise-scaled redesigns 836d (novelty) and
  836e (interval) ran 2026-08-01. All four are `non_degenerate: true`, all four declare
  `"substrate": "SD-083 offline policy-consolidation window (ree-v3 42ab95f688)"`, and 836e's per-arm
  gate is `all_green: true` with zero red or structurally-vacuous arms.
- `status: candidate_substrate_landed`, `live_status.as_of: 2026-07-29`, `evidence: []`, and no entry in
  `claim_evidence.v1.json` -- because all four runs carry `claim_ids: ["MECH-476"]` only.
- **The consumer claim is RETIRED.** MECH-476 is `status: retired`, `superseded_by: [MECH-459,
  MECH-460]`, verdict 2026-08-01 "WITHDRAWN per the claim's own pre-registered falsifier". SD-083 thus
  `depends_on` a retired claim.
- The cognifold PORT into the SD-017 sleep loop that SD-083's `implementation_note` registers as a
  follow-on is gated on "836b and/or 836c score SUPPORTED" (`sleep_substrate_plan.md`, 2026-07-29). All
  four arms scored `weakens`. **That trigger can never fire, and no sleep GAP should be opened for it.**

**epistemic_category (proposed):** `standard`. (Not `substrate_ceiling` -- nothing downstream absorbs
its signal; not `substrate_conditional` -- it is built, exercised four times, and its own asserted
properties are directly measured.)

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION: the window must actually run and its knob must be demonstrably live and
> demonstrably OFF in the control -- `use_offline_consolidation=True` on ON arms;
> `offline_ewc_installed=True` on every ON arm and `False` on the N=0 / OFF arm;
> `offline_n_fisher_states > 0`; and `mean_offline_ewc_penalty_recent > 0` on ON arms and exactly `0.0`
> on OFF. All four hold in V3-EXQ-836e: `window_n0` installed 0/10 seeds, penalty 0.0, capture 0.0;
> `window_n150 / n400 / n900` installed 10/10 each, penalty 0.246 / 0.316 / 0.346,
> `offline_n_fisher_states` 256 in every ON arm.
>
> CONFIRMING (SD-083's four asserted properties, each stated with the measured value that already
> answers it):
> (i) INTERVAL ACCUMULATION -- `offline_capture_resource` follows `c(N) = capture_max * (1 - exp(-N/tau))`:
> strictly increasing and saturating in `window_steps`, with `offline_effective_ewc_coef = capture *
> offline_ewc_max_coef`. MEASURED (836e, `offline_ewc_max_coef = 100.0`): capture
> 0.0 / 0.5276 / 0.8647 / 0.9889 and eff_coef 0.0 / 52.76 / 86.47 / 98.89 at N = 0 / 150 / 400 / 900.
> **CONFIRMED.**
> (ii) DOSE-INTERVAL ORTHOGONALITY -- the claim's own "BUILDS PROTECTION without retraining, so post_bc
> is invariant to the interval and the INTERVAL axis is orthogonal to the DOSE axis". MEASURED (836e):
> `post_bc_foraging_competence = 9.53` in ALL FOUR interval arms including N=0, identical to the
> reported precision. **CONFIRMED**, and this is the strongest single result -- it is the property that
> makes the interval axis interpretable at all.
> (iii) NOVELTY GATING (Moncada 2007) -- the paired/unpaired contrast must move
> `offline_novelty_factor` and hence `offline_effective_ewc_coef`, with capture, Fisher mass and post_bc
> matched. MEASURED (836d): paired novelty 1.0 -> eff_coef 77.69; unpaired novelty 0.05 -> eff_coef
> 3.88; `offline_capture_resource` 0.7769 and `offline_fisher_mass` 28.33 and `post_bc` 4.61 IDENTICAL
> across both arms. **CONFIRMED** -- the gate moves exactly one factor and nothing else.
> (iv) TRACE SELECTIVITY -- the Fisher is computed on the POLICY log-likelihood, so value-head
> parameters must receive ~0 weight (this is the property that distinguishes SD-083 from the ONLINE
> GLOBAL MECH-475 KL anchor, and it is the claim's stated distinctive content). Assert directly:
> per-parameter-GROUP Fisher mass, policy head vs value head, with the value-head share below (say) 1%
> of total. **NOT YET MEASURED** -- 836b/c/d/e report only a scalar `offline_fisher_mass`. This is the
> one open leg, and it is a manifest field, not an experiment.
> (v) RNG NEUTRALITY -- snapshot/restore around the window must leave post-window RNG state identical to
> the OFF arm. Covered at the unit level by
> `ree-v3/tests/contracts/test_sd083_offline_consolidation.py` (12/12) but never asserted in a run
> manifest; worth promoting to a manifest gate.
>
> FALSIFYING: `offline_capture_resource` non-monotone in `window_steps`, or flat, or not saturating
> (the c(N) form is wrong); OR `post_bc` moving with the interval (the window is RETRAINING rather than
> building protection, and the interval/dose axes are NOT orthogonal, which would invalidate every
> interval-arm reading built on this instrument); OR the novelty gate leaving `offline_effective_ewc_coef`
> unchanged between paired and unpaired (there is no novelty gating, only an unconditional anchor); OR
> value-head Fisher mass comparable to policy-head Fisher mass (the anchor is GLOBAL, not
> trace-selective, and SD-083's asserted distinction from MECH-475 collapses -- this is the sharpest
> available falsifier and the only one still open).
>
> POTENCY -- STATED SEPARATELY BECAUSE IT IS NOT SD-083's OWN CLAIM, BUT IS MANDATORY FOR ANY CONSUMER
> USING THIS INSTRUMENT: 836d/836e show the penalty is LIVE but not EFFICACIOUS. `retained_fraction` is
> invariant to a penalty whose coefficient varies ~14x (836e: 0.712 / 0.707 / 0.860 / 0.723 across
> eff_coef 0 / 52.8 / 86.5 / 98.9; leave-one-out stable across 10 folds, verdict `weakened` in all 10),
> and in 836d the WEAKER-penalty unpaired arm retained MORE than the paired arm (0.950 vs 0.834) --
> the wrong direction. Any future experiment consuming this window MUST carry a POTENCY precondition:
> demonstrate that the applied penalty CONSTRAINS the parameter update (e.g. post-refinement
> parameter-space distance from theta* falls measurably as eff_coef rises), because without it a null on
> the consumer claim cannot distinguish "no consolidation process" from "the anchor was too weak to
> matter". This distinction is not settled by anything on record.

**Proposal sketch (a):**
- **title:** "SD-083 instrument-validity readout: per-parameter-group Fisher mass (policy vs value head)
  and window RNG-neutrality, emitted from the existing `consolidate_offline_window` path"
- **related_claims:** SD-083 (primary), MECH-459, MECH-460 (the live successors of MECH-476), MECH-475
  (the online-global contrast this claim asserts it differs from), MECH-441
- **acceptance_checks:** (1) manifest emits per-parameter-group Fisher mass with value-head share
  reported; (2) manifest emits RNG-state equality against the OFF arm; (3) `claim_ids` names SD-083 with
  an explicit direction; (4) the four already-confirmed properties (i)-(iii) are re-emitted in the same
  manifest so the whole instrument-validity claim is banked in ONE artifact rather than reconstructed
  from four MECH-476-tagged runs; (5) a POTENCY readout (parameter-space distance from theta* as a
  function of eff_coef) so the potency gap is measured rather than inferred.
- **Cost note:** this is a reanalysis / instrumentation pass on an existing testbed path, not a new
  lineage. It should NOT be sized like the 836 runs.

**depends_on additions (if any):** **REPOINT, do not add.** `depends_on: [MECH-476, MECH-475, MECH-441,
SD-017]` currently names a RETIRED claim. Repoint `MECH-476 -> MECH-459, MECH-460` (per MECH-476's own
`superseded_by`), and either drop the `SD-017` edge or re-label it in `notes` as a PROSPECTIVE PORT edge
whose trigger is now unreachable -- as written it makes SD-083 look like live sleep-substrate work,
which it is not, and which the sleep plan explicitly warns against ("do not open a sleep GAP for it
pre-emptively").

**GOVERNANCE FLAG (two, kept separate):**

1. `evidence_discrepancy` -- SD-083 has `evidence: []` and no `claim_evidence.v1.json` entry, while FOUR
   non-degenerate runs (V3-EXQ-836b, 836c, 836d, 836e) declare SD-083 as their substrate, exercise its
   every asserted property, and record telemetry that CONFIRMS three of the four (capture curve
   0.0/0.5276/0.8647/0.9889; post_bc identical at 9.53 across all interval arms including N=0; novelty
   gate 1.0 -> eff_coef 77.69 vs 0.05 -> 3.88 with everything else matched). Its `implementation_note`
   still reads "NOT YET VALIDATED by experiment". The runs carry `claim_ids: ["MECH-476"]` only, so
   nothing routed. This is a routing gap, not a promotion request -- digestion does not promote -- but
   it is the clearest case in the group of banked evidence that never reached its claim.

2. `stale_note` -- SD-083's stated purpose is DISCHARGED and its onward gate is UNREACHABLE. It exists
   "to unblock MECH-476's two blocked_substrate falsifier arms"; both arms ran, both plus their
   redesigns scored `weakens`, and MECH-476 is now `status: retired` (superseded by MECH-459/MECH-460).
   The registered cognifold PORT into the SD-017 sleep loop is gated on "836b and/or 836c score
   SUPPORTED" (`sleep_substrate_plan.md`, 2026-07-29), which can never happen. Governance should (a)
   move SD-083 off `candidate_substrate_landed` to whatever status fits a validated instrument whose
   consumer retired, (b) repoint `depends_on`, and (c) record in the sleep plan that the SD-083 port
   trigger is dead so a later sleep session does not go looking for it. **Do NOT excrete SD-083** -- it
   is a landed, contract-tested, four-times-exercised instrument in the same `mech457` testbed where
   MECH-476's successors MECH-459/MECH-460 live, so it may still be consumed; only its framing is stale.

---

<!-- G3 appended 2026-09-04T21:18:57Z -->
## G3 -- control-plane commitment modulation cluster  (agent report)

### Group preamble

**Why these are together (restated, then my own view).** The grouping was made on namespace
(`control_plane.*`) plus title overlap on interrupt / release / independent-proposal / variability.
That is right about the namespace and misleading about the mechanism. The five partition into two
sub-clusters that the substrate itself already separates, in as many words:

- **Sub-cluster A -- the COMMIT gate** (the inequality `running_variance < effective_threshold`,
  ARC-016 / MECH-090): MECH-104 (fast surprise impulse on the *numerator*), MECH-106 (slow valence
  bias on the *denominator*), MECH-250 (periodic hard *release* bypassing the inequality),
  MECH-234 (whether more than one proposal can hold the effector at once).
- **Sub-cluster B -- the SELECTION softmax temperature** (what E3 does *given* it is choosing):
  SD-105 alone.

`/Users/dgolden/REE_Working/ree-v3/ree_core/regulators/phasic_surprise_burst.py` lines 9-21 draws
exactly this line for the MECH-104/SD-069 pair: *"RELATIONSHIP TO MECH-104 (important -- do not
conflate) ... THIS module routes the same surprise event to the E3 SELECTION softmax temperature
instead ... Same biological substrate, same source signal, different consumer."* The same reading
applies to MECH-250 vs SD-105.

**(i) same-claim / merge candidates.**
- **MECH-104 vs MECH-106: NOT the same claim, and no merge.** They act on opposite sides of one
  inequality at different timescales (MECH-104 = fast prediction-error impulse on `running_variance`;
  MECH-106 = slow outcome-valence EMA on `commit_threshold`). Because they move the same inequality,
  they are *mutually confounded in measurement* -- see (iv) -- but they are distinct mechanisms.
  MECH-106 `depends_on: MECH-104`; that dependency is real and I recommend keeping it (MECH-106's own
  notes position it explicitly as "distinct from MECH-104 (volatility interrupt, fast)").
- **MECH-250 -> MECH-108: STRONG PARTIAL merge pressure, pointing at an already-BUILT mechanism
  outside the group.** Full proposal under MECH-250 below. Headline: MECH-108's BreathOscillator is
  built (`ree_core/heartbeat/clock.py`), automatically wired (`agent.py:7287` -> `agent.py:9256`),
  and MECH-250's biological grounding is *already inside MECH-108's own code comment*
  (`clock.py:28`: "Biological basis: exhalation-phase respiratory coupling"). Expect PARTIAL
  absorption with a genuinely non-empty residual (WINDOW vs BOUNDARY; SOFTEN vs HARD-RELEASE).
- **MECH-234: not a merge candidate.** It is a lit-derived *design ruling on MECH-090*, not a
  parallel mechanism; its ruling has already been applied (its own notes: "Layer 3 ... is not
  warranted").
- **SD-105 vs MECH-313: no merge.** SD-105's own title positions it as the *state-dependent*
  complement of MECH-313's *state-independent* constant lift on the SAME channel; both knobs exist
  and are independently toggleable (`use_noise_floor`, `use_selection_entropy_floor`, both default
  False). But they must never be armed together without an arm pinning one -- SD-105's own
  `implementation_note` says it is applied *after* MECH-313, so MECH-313's readout
  (`noise_floor_temp`) deliberately reports the PRE-multiplier value.

**(ii) contradictions / undercut premises.**
1. **MECH-234 does NOT contradict the single-commitment assumption the others rest on -- it
   RATIFIES it for V3, and in doing so makes itself unfalsifiable here.** `ree_core/environment/`
   contains exactly one environment (`causal_grid_world.py`); its `action_dim` (line 1529) is a
   single discrete channel of 5 (6 with the consummatory act). MECH-234's *same-effector* leg
   ("winner-takes-all, not independent parallel expression") is therefore TRUE BY CONSTRUCTION in
   V3, and its *cross-effector* leg has no substrate to run on. So it neither threatens nor supports
   the other four.
2. **MECH-106 collides in SIGN with SD-011 (`status: stable`) on the very same variable.**
   `e3_selector.select()` composes `effective_threshold` as base -> `(1 - MECH-108 sweep)` ->
   `(1 + SD-011 urgency)` -> SD-093/MECH-426 (`predictors/e3_selector.py:3599-3625`). SD-011, as
   *fixed on 2026-08-26*, RAISES `effective_threshold` under accumulated threat -- i.e. harm makes
   commitment MORE permissive ("D2 avoidance escape response"). MECH-106 asserts the opposite: harm
   raises the biological threshold = *lowers* the variance-space threshold = commitment HARDER (and
   its own driver implements exactly that, `v3_exq_231a...py:261-269`). Both are latent by default
   (`urgency_weight = 0.0`; MECH-106 unbuilt), so there is no live conflict today -- but the moment
   MECH-106 is landed in the substrate it lands on the same multiplicative chain as a `stable`
   claim with the opposite sign under harm. Flagged.
3. **SD-105's own premise is undercut by a same-day BLOCKING red-team verdict that the claim block
   does not mention.** See the SD-105 entry and GOVERNANCE FLAG 5.

**(iii) shared falsifier.** Yes -- and it is a PRECONDITION rather than a test. All four
commit-gate claims are assertions about one inequality, and every one of them is vacuous unless
both sides of that inequality have live dynamic range in the run. State it once here; each of
MECH-104 / MECH-106 / MECH-250 cross-references it rather than re-deriving it.

> **THE COMMIT-GATE DYNAMIC-RANGE PRECONDITION (shared, G3).**
> `commitment_threshold = 0.40` in *variance space* (`ree_core/utils/config.py:1022`), and
> `variance_commit_threshold()` is the identity (`e3_selector.py:265`). The measured un-inflated
> operating point of `running_variance` is **0.005420** (V3-EXQ-794, recorded verbatim in
> `config.py:1058`) -- i.e. **~74x below the threshold**. The default agent is therefore
> *permanently committed*, which is precisely the degeneracy MECH-104's own `functional_restatement`
> predicts ("world_forward training drives running_variance to near-zero, permanently locking the
> agent in committed state"). Consequently any run adjudicating MECH-104 / MECH-106 / MECH-250 MUST
> report, from its CONTROL arm: (a) the realised `running_variance` range and its distance to
> `effective_threshold`; (b) the realised **committed-fraction, which must be strictly between 0
> and 1** -- at 1.0 no de-commitment can be observed, at 0.0 there is no commitment to break;
> (c) whether the SD-076 floor is binding. On (c), note the floor is *conditional*:
> `_apply_wci_rv_floor()` runs only inside the `use_waking_confidence_inflation` branch
> (`e3_selector.py:809-833`), and that flag defaults False (`config.py:1046`). When it IS armed, the
> floor is `waking_confidence_rv_floor = 0.01` absolute (`relative_frac` defaults 0.0, so the
> absolute path is the live one) and V3-EXQ-794 measured `rv_final` EXACTLY 0.010000 on all four
> arms -- a saturation signature, not a null. Either way the gap to 0.40 is 40x-74x.

**(iv) cross-cutting finding -- the committed-fraction is a shared confound that crosses the
sub-cluster boundary, so SD-105 is coupled to the other four despite the different consumer.**
`self.last_precommit_probs = probs.detach()` is written *inside* `e3_selector.select()`
(`e3_selector.py:3590`) -- and that is the distribution SD-105's controller integrates (its module
docstring: "the PREVIOUS waking tick's E3 pre-commit selection distribution
(`agent.e3.last_precommit_probs`)"). So anything that changes *how often the agent is uncommitted*
-- MECH-104's spike, MECH-106's bias, MECH-250's release, MECH-108's sweep -- changes the population
of ticks over which realised selection entropy is measured. Two consequences, both operational:

- **A null on SD-105's headroom restoration is uninterpretable unless the commit duty cycle is
  pinned or reported.** SD-105's entropy EMA is not a pure measure of policy confidence; it is
  confounded with the commit duty cycle. MECH-108 is *already on by default in every
  experiment-built config* (see Currency finding 5), injecting an uncommitted window every 50
  steps into exactly that trace.
- **Symmetrically, a de-commitment result on 104/106/250 measured on an SD-105-armed agent is
  uninterpretable**, because the selection temperature was being moved by a controller reading the
  very duty cycle under test.

**Pin one; never arm both live.** This is structurally the same defect the V3-EXQ-963b red team
found *within* the selection channel (finding F1: a closed-loop set-point controller sitting on the
DV it regulates). The group-level extension is that the loop also closes *through the commit gate*,
not only within selection -- which is new, and is not recorded anywhere I could find.

**Currency findings (verified this pass).**

1. **MECH-104's `status_note` is STALE.** It stops at EXQ-365 (2026-04-14). `claim_evidence.v1.json`
   shows two later non-excluded PASSes: `v3_exq_126...` re-run (2026-04-21T20:23:36Z) and
   **`v3_exq_623_mech104_volatility_interrupt_discriminative_pair` (2026-06-01T15:20:50Z, PASS)** --
   and 623 is the *important* one, being the first run to add the behavioural de-commitment gates
   (C6/C7) that the claim's own title asserts. Current index: `exp_conf 0.77`, 11 experimental
   entries, quadrant `confirmed_established`, `fail_runs 2` (both excluded: `superseded` /
   `non_contributory`).
2. **MECH-104's Route-2 is STILL NOT in the substrate, and every Route-2 result is
   driver-injected.** No `surprise_coeff`, no rv-directed `surprise_threshold`, no gated
   `_running_variance +=` anywhere under `ree_core/`. The impulse is poked in from the driver with
   an experimenter-chosen magnitude in every case: `v3_exq_061...py:~171`
   (`agent.e3._running_variance = float(...) + spike_magnitude`), `v3_exq_062b...py:347`
   (`agent.e3._running_variance += spike_magnitude`), and `v3_exq_623...py` docstring
   (`running_variance += SPIKE_MAGNITUDE * (surprise - SURPRISE_THRESHOLD)`). The substrate says so
   itself: `regulators/phasic_surprise_burst.py:32` -- *"the signal experiments already poke to fake
   MECH-104"*. Meanwhile EXQ-204, the one run that measured the **endogenous** spike, recorded
   `harm_spike_rv ~1.6-1.9e-6` -- roughly **five orders of magnitude** below the ~0.39 excursion
   needed to cross a 0.40 threshold. The claim's own `notes` do say Route (2) is "for later V3
   phases", so this is not a false statement in the block; it is a currency fact that changes how
   the `active` status should be read.
3. **MECH-106 has NO substrate implementation at all.** Zero hits for `MECH-106` and zero for
   `valence_bias` anywhere under `ree_core/`. The live `effective_threshold` chain
   (`e3_selector.py:3599-3625`) carries a MECH-108 sweep term, an SD-011 urgency term and an
   SD-093/MECH-426 term -- and no valence term. EXQ-231a's `_effective_threshold_vb()`
   (`v3_exq_231a...py:261`) is a **driver-local function**. The claim's `notes` sentence
   "V3 implementation: valence_bias updated at each E3 tick via a slow EMA on outcome valence
   signal" is a *plan written in the present tense*; it has not landed. MECH-106 is `provisional`
   on exactly one non-excluded experimental entry (`exp_conf 0.575`, quadrant `plausible_unproven`).
4. **SD-105's registered validation experiment was NOT queued, and its own substrate_queue entry
   says otherwise.** `evidence/planning/substrate_queue.json`
   (`sd_phasic_burst_decay_and_warmup_headroom.validation_experiment`) reads *"V3-EXQ-963b ...
   queued by campaign-c2c-20260904"*. It was not: ree-v3 commit **`d2104f8`** is titled
   *"V3-EXQ-963b driver: BLOCKING red-team verdict recorded, NOT queued"*; the live queue snapshot
   (ree-v3 `99817b6`, today) holds only V3-EXQ-1002 / V3-EXQ-983a / V3-EXQ-993a; and
   `git log -S"963b" -- experiment_queue.json` returns nothing. The driver exists and is lint-clean
   but is deliberately unqueued.
5. **MECH-108's `epistemic_category: substrate_conditional` looks stale, and it matters because
   MECH-250 depends on it.** The BreathOscillator is built (`heartbeat/clock.py`, `sweep_active`),
   automatically wired (`agent.py:7287` computes `sweep_reduction`, passed at `agent.py:9256`), and
   `REEConfig.from_dims()` defaults `breath_period = 50` (`config.py:8169`, assigned at
   `config.py:9791`) against the dataclass default of 0 (`config.py:3148`). Since every experiment
   builds its config through `from_dims`, **MECH-108 is ON by default in practice**, not merely
   buildable. It nonetheless carries **zero evidence rows**. The likely reason is arithmetic and is
   the key input to MECH-250 below: the sweep multiplies the threshold by `(1 - 0.25)`, i.e.
   0.40 -> 0.30, against an rv operating point of ~0.0054 -- still ~55x away, so **MECH-108's
   softening cannot produce a single uncommitted step at the current operating point.**
6. **MECH-234, MECH-250 and SD-105 each have zero evidence rows** in `claim_evidence.v1.json`
   (consistent with `candidate`). MECH-104: 11 experimental + 5 literature. MECH-106: 1 non-excluded
   experimental + 5 literature.
7. **None of the five is on the live front.** `docs/CURRENT_FRONT.md` (generated 2026-09-04T14:17Z):
   "The live front is the observation -> z_world -> E1/E2-rollout interface, **not the selector**:
   39 of 43 remaining v3 nodes chain to it." This should temper how much new compute the group
   attracts -- it argues for one well-targeted MECH-104 run and deferral/merge elsewhere.
8. **SD-105's block is substantively complete but has one gap and one questionable field.** Present:
   id/title/claim_type/subject/polarity/status/live_status/epistemic_category/implementation_phase/
   v3_pending/version_relevance/claim_level/registered_utc/depends_on/related_claims/source/
   functional_restatement/implementation_note. Its `source` design doc
   (`docs/architecture/sd_105_selection_entropy_headroom_floor.md`, 164 lines) exists. Missing:
   `location` (all four siblings in this group carry one), and no `notes`. The questionable field is
   `epistemic_category: standard` -- see the SD-105 entry. The design doc is *also* stale: line 151
   still names V3-EXQ-963b as the validation and it contains no mention of the freeze/share problem.

---

### MECH-104 -- Unexpected harm events spike commitment uncertainty (LC-NE volatility interrupt), enabling de-commitment.

**Recommended disposition:** **(a) testable now** -- the *endogenous* half of the claim is
substrate-live and default-on, and the one question no run has ever asked (does the UN-INJECTED
surprise spike actually de-commit?) is answerable on today's substrate with V3-EXQ-623's design
minus its driver injection.

**Extracted from:** V3-EXQ-623's pre-registered criteria (C1-C5 signal-magnitude gates, C6
behavioural de-commitment ratio >= 2.0x) fused with V3-EXQ-204's endogenous spike measurement
(`harm_spike_rv ~1.6-1.9e-6`, and its C1-C4 as recorded in the claim's own `status_note`). These
are the two halves of MECH-104's title that have never been run in the same arm. Not drafted fresh.

**Currency check:** `status_note` stops at EXQ-365 but two later PASSes exist, 623 being decisive
(`claim_evidence.v1.json`, `latest_run_id = v3_exq_623_..._20260601T152050Z_v3`). Route-2 is absent
from `ree_core/` (no `surprise_coeff`; grep of the whole tree); every Route-2 run injects from the
driver (`v3_exq_061...py:~171`, `v3_exq_062b...py:347`, `v3_exq_623...py` docstring), which
`regulators/phasic_surprise_burst.py:32` states outright. The SD-076 rv floor
(`config.py:1053`, gated on `use_waking_confidence_inflation`, default False at `config.py:1046`)
landed 2026-07-22 -- *after* MECH-104 went active -- and is now a load-bearing precondition of every
rv readout. V3-EXQ-623 additionally ran with `use_mech090_readiness_conjunction=False` and
`use_commit_readiness_gate=False`, so the evidence is at a readiness-gates-OFF configuration.

**epistemic_category (proposed):** `standard` (keep / set explicitly). The endogenous EMA path is
built and default-on and nothing downstream absorbs its signal -- the signal is simply small, which
is a measurable fact rather than a ceiling. **If the run below falsifies the behavioural leg while
replicating the selectivity leg, THAT is the moment to re-tag `substrate_ceiling`** (built,
repeatedly exercised, causal signal cannot reach the outcome metric) and route to substrate work on
the rv-to-threshold gap.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** See the group's shared COMMIT-GATE DYNAMIC-RANGE PRECONDITION
> (G3 preamble (iii)); do not re-derive it. Specific to this run, the CONTROL (gate-ON,
> no-injection) arm must report and satisfy: (a) realised `running_variance` range and its distance
> to `effective_threshold` (base 0.40, `config.py:1022`); (b) realised committed-fraction strictly
> between 0 and 1 -- a run at 1.0 cannot observe a de-commitment; (c) `n_unexpected_harm_events >= 10`
> occurring *in committed state* (V3-EXQ-623 C5); (d) the SD-076 floor's binding fraction --
> `running_variance` must not sit at `waking_confidence_rv_floor` for more than 10% of ticks, which
> is the exact clamp V3-EXQ-794 hit (`rv_final` EXACTLY 0.010000 on all four arms); and (e)
> **`breath_period = 0` in BOTH arms**, because `from_dims` otherwise arms MECH-108's sweep by
> default and a sweep-driven uncommitted window would be misread as a surprise-driven one. And,
> load-bearing: **no line of the driver may write `agent.e3._running_variance` in the ON arm** --
> the entire question is whether the endogenous impulse suffices.
>
> **CONFIRMING.** On a matched-seed pair over >= 3 seeds sharing trained weights and episode
> sequence -- ENDOGENOUS-ON vs ABLATED (`_ema_alpha = 0.0`, variance frozen; the V3-EXQ-204
> ablation) -- the ON arm shows BOTH legs *in the same arm*: (i) SELECTIVITY: endogenous
> `delta_var_unexpected` exceeds `delta_var_expected` by more than 3 SD of the per-seed delta AND by
> an absolute floor of 1e-4, in >= 2 of 3 seeds; and (ii) SUFFICIENCY: committed -> uncommitted
> transitions attributable to those events (V3-EXQ-623's 20-tick POST_SPIKE_WINDOW attribution)
> occur at >= 2.0x the ABLATED arm's rate, with the ABLATED rate reported and non-degenerate, in
> >= 2 of 3 seeds. Leg (ii) in the absence of any injection is what has never been shown.
>
> **FALSIFYING.** Leg (i) replicates and leg (ii) does not: the endogenous `delta_var_unexpected` is
> real and selective but stays far below the rv-to-threshold gap, so committed -> uncommitted
> transition rates are statistically indistinguishable between ON and ABLATED. V3-EXQ-204's own
> endogenous magnitude (`harm_spike_rv ~1.6-1.9e-6` against a ~0.39 gap) *predicts exactly this
> outcome*, so it must be treated as the live alternative hypothesis, not the surprise. This
> refutes the "enabling de-commitment" half of the title while leaving "spikes commitment
> uncertainty" standing, and is grounds to demote MECH-104 from `active` and to re-tag it
> `substrate_ceiling`. A second, distinct falsifying pattern: the ABLATED arm shows the *same*
> transition rate, which means the observed transitions were never surprise-driven at all (most
> likely MECH-108's sweep, or the readiness gates) -- which is why precondition (e) is mandatory.

**Proposal sketch (a):**
- **title:** `V3-EXQ-<next> -- MECH-104 endogenous volatility interrupt: does the UN-INJECTED surprise spike de-commit? (supersedes V3-EXQ-623's behavioural leg, which injected)`
- **related_claims:** `MECH-104`, `ARC-016`, `MECH-090`, `SD-076`, `MECH-108` (as a pinned-off confound)
- **acceptance_checks:** C1-C2 selectivity as above; C3 ABLATED flat (`delta_var_unexpected < 1e-6`);
  C4 cross-condition discriminative delta; C5 `n_unexpected_harm >= 10` in committed state;
  **C6 de-commitment ratio >= 2.0x with the ABLATED denominator reported**; C7 committed-fraction in
  (0,1) in every arm; C8 `breath_period == 0` asserted at runtime in both arms; C9 no write to
  `_running_variance` outside `update_running_variance()` (assert by source lint, as V3-EXQ-623's
  own driver could not). Declare a `dv_headroom` precondition **denominated on the same statistic
  each criterion routes on** -- the V3-EXQ-963b F3 lesson (max_abs read 1.55x headroom where the
  4-of-5-seed statistic read a 2.3x shortfall).

**depends_on additions:** `SD-076` -- the waking-confidence rv floor is now a precondition of every
MECH-104 readout and postdates the claim's promotion.

**GOVERNANCE FLAG:** `stale_note` -- MECH-104's `status_note` stops at EXQ-365 (2026-04-14) and omits
the two later non-excluded PASSes, including V3-EXQ-623 (2026-06-01), which is the strongest evidence
on file and the only run to test the behavioural half of the title.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- MECH-104's `active` status rests on a conjunction
*across* runs that no single run establishes: endogenous SELECTIVITY (V3-EXQ-204) plus
driver-INJECTED SUFFICIENCY (V3-EXQ-061 / 062b / 623). The only endogenous magnitude ever measured
(`harm_spike_rv ~1.6-1.9e-6`) is ~5 orders of magnitude below the ~0.39 rv-to-threshold gap, and
`regulators/phasic_surprise_burst.py:32` describes the injection path as experiments that "poke to
fake MECH-104". This does not make the claim wrong; it makes `active` a stronger reading than the
evidence supports until the run above is done.

---

### MECH-106 -- Commitment threshold is asymmetrically modulated by outcome valence: positive outcomes lower it, negative outcomes raise it.

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`**, blocking substrate
= the valence-bias term on `effective_threshold`, which has never existed in `ree_core/`; the sole
supporting run emulated it inside its own driver, and that emulation is *symmetric*, so the
ASYMMETRY the claim is named for has not in fact been tested.

**Extracted from:** the claim's own `functional_restatement`
(`commit_threshold_effective = commit_threshold_base x (1 + valence_bias)`) and V3-EXQ-231a's five
pre-registered criteria (C1 `da_divergence > 0.20`, C2 `threshold_asymmetry > 1.20`,
C3 `latency_ratio_vb > 2.0`, C4 `latency_ratio_nb in [0.5, 2.5]`, C5 `asymmetry_delta > 1.0`), read
against that driver's actual implementation at `v3_exq_231a...py:147-152, 261-269, 546-557`.

**Currency check:** **No substrate implementation exists.** Zero hits for `MECH-106` and zero for
`valence_bias` in `ree_core/` (whole-tree grep). The live `effective_threshold` composition
(`e3_selector.py:3599-3625`) is base -> MECH-108 sweep -> SD-011 urgency -> SD-093/MECH-426; there is
no valence term. `_effective_threshold_vb()` at `v3_exq_231a...py:261` is driver-local. The claim's
`notes` line "V3 implementation: valence_bias updated at each E3 tick via a slow EMA" is an unlanded
plan in the present tense. Index: `exp_conf 0.575`, `genuine_exp_count 1`, quadrant
`plausible_unproven`, `fail_runs 0` (the two EXQ-231 FAILs are `scoring_excluded: superseded`).

**Additionally, and this is the substantive finding: V3-EXQ-231a's C2 is not independent of its C1.**
The driver sets `BIAS_WEIGHT = 1.2` and
`effective_threshold = base * (1 + 1.2 * (da - 0.5))` (`v3_exq_231a...py:152, 269`) -- a **symmetric
linear map in `da` about 0.5**. C2's metric is
`threshold_asymmetry = threshold_pos_vb / threshold_neg_vb` (line 547), which under that map is a
deterministic function of C1's `da_divergence = da_pos - da_neg`. Working the recorded numbers:
`da_divergence = 0.73-0.78` gives, e.g. at `da_pos ~= 0.87 / da_neg ~= 0.11`,
`(1 + 1.2 x 0.37) / (1 + 1.2 x -0.39) = 1.444 / 0.532 = 2.71` -- which is exactly the reported
`threshold_asymmetry = 2.7-2.8`. So C2 could not have failed once C1 passed. More importantly, a
symmetric linear modulation **cannot distinguish "asymmetric valence modulation" (Frank 2005's
asymmetric D1/D2 dynamic range, which is MECH-106's actual assertion) from "any monotone valence
modulation"**. The asymmetry half of the title is untested.

**epistemic_category (proposed):** `substrate_conditional` (set explicitly). Per REE_assembly
CLAUDE.md's sharpened discriminator: the mechanism the claim asserts has *never been exercised in the
substrate* -- the code does not exist -- and the one banked positive result comes from a driver
emulation whose functional form does not match the claim. That is `substrate_conditional`, not
`substrate_ceiling` (nothing downstream is absorbing a signal; there is no signal in the substrate).

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** See the group's shared COMMIT-GATE DYNAMIC-RANGE PRECONDITION
> (G3 preamble (iii)); do not re-derive it -- and note MECH-106 needs it *twice over*, because both
> the base threshold and the valence-modulated threshold must sit where `running_variance` can
> actually cross them. Specific to this claim: (a) the run must exhibit a **differentiated valence
> history** -- `da_pos - da_neg > 0.20` measured, which is the precise failure that made the original
> V3-EXQ-231 a design flaw rather than a claim failure ("PERSISTENT and REACTIVE conditions produced
> identical commit values"); (b) latency-to-commit must be finite and unsaturated in BOTH the
> positive-history and negative-history conditions -- an episode-length-censored latency in the
> negative condition measures the episode budget, not the threshold; (c) the modulation must be
> implemented **asymmetrically**, i.e. with independent gains for the positive and negative
> directions (`w_pos != w_neg` as free parameters), because a symmetric linear map makes the
> asymmetry criterion an arithmetic consequence of the divergence criterion (see V3-EXQ-231a above)
> and therefore vacuous; (d) MECH-104's impulse and SD-011's urgency term must be pinned OFF
> (`urgency_weight = 0.0`, no rv injection) -- they move the same inequality (G3 preamble (iv)).
>
> **CONFIRMING.** With independent positive/negative gains and a matched-seed VALENCE_BIAS vs NO_BIAS
> ablation over >= 5 seeds: (i) the **direction** leg -- mean latency-to-commit is longer after a
> negative-outcome history than after a positive one in the VALENCE_BIAS arm, by more than 3 SD of
> the per-seed latency delta and by an absolute floor of 5 ticks, in >= 4 of 5 seeds, while the
> NO_BIAS arm shows a latency ratio inside [0.5, 2.5] (V3-EXQ-231a's C4, retained as the
> no-manipulation control); and (ii) the **asymmetry** leg, which is the claim's actual content --
> the fitted `|w_neg| / |w_pos|` is bounded away from 1.0 (>= 1.5, or <= 0.67) with a
> per-seed-bootstrap CI excluding 1.0, in >= 4 of 5 seeds. Leg (ii) must be measured, not assumed:
> it is what separates MECH-106 from the weaker claim "outcome valence modulates the commit
> threshold at all".
>
> **FALSIFYING.** Either (i) fails -- valence history does not shift commitment latency once
> MECH-104 and SD-011 are pinned off, which would say the EXQ-231a result was carried by the
> driver's hand-set `BIAS_WEIGHT` rather than by any property of outcome valence -- or (i) passes
> and (ii) fails, i.e. `|w_neg| / |w_pos|` is statistically indistinguishable from 1.0. The second
> is the more likely and the more informative: it would refute MECH-106 *as written* (asymmetric)
> while supporting a narrower successor ("outcome valence modulates the commit threshold
> monotonically"), and would be grounds to demote from `provisional` and re-title. A third pattern:
> the seed-42 anomaly recorded in `evidence_quality_note` ("near-zero divergence, no commitments")
> recurs on more than 1 of 5 seeds -- that is precondition (a) failing, not a result, and the run
> must be re-designed rather than adjudicated.

**Proposal sketch:** none -- this is disposition (c), not (a). The run above is only writable once
the valence-bias term exists in `e3_selector`'s `effective_threshold` chain **with independent
positive/negative gains**. That is a small, well-specified substrate build (one EMA + one
two-gain multiplier at `e3_selector.py:3599`, alongside the existing MECH-108 and SD-011 terms) and
is the correct thing to route to `/implement-substrate` -- but it MUST be designed against the
SD-011 sign collision below, not landed beside it silently.

**depends_on additions:** none. (`MECH-104`, `MECH-090`, `ARC-016`, `MECH-105` are all correct and
live. `MECH-104` is `active`; per the G3 brief's question, MECH-106 inherits a **live but
narrower-than-advertised** precondition -- MECH-104's endogenous selectivity is real and
substrate-live, its de-commitment sufficiency is driver-injected only. So the precondition is not
dead, but MECH-106 should not be read as inheriting "de-commitment demonstrably works".)

**GOVERNANCE FLAG:** `evidence_discrepancy` -- MECH-106 is `provisional` on a single non-excluded
run (V3-EXQ-231a) in which (1) the mechanism was implemented **in the driver, not the substrate**
(no `valence_bias` anywhere in `ree_core/`), and (2) criterion C2 (`threshold_asymmetry > 1.20`) is
an arithmetic consequence of criterion C1 (`da_divergence > 0.20`) under that driver's own
symmetric linear map `base * (1 + 1.2 * (da - 0.5))` -- reproduced numerically above -- so the
"5/5 criteria" count over-states the independent evidence, and the **asymmetry** the claim is named
for was never tested.

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-106 and SD-011 (`status: stable`) make
**opposite-sign** predictions about how harm modulates `effective_threshold`, on the same
multiplicative chain in `e3_selector.select()` (`e3_selector.py:3599-3625`). SD-011's block was
sign-flipped on 2026-08-26 to RAISE the threshold under accumulated threat (commit *more* readily,
"D2 avoidance escape response"); MECH-106 asserts harm makes commitment *harder*. Both are latent by
default (`urgency_weight = 0.0`; MECH-106 unbuilt), so there is no live defect -- but this must be
adjudicated **before** any MECH-106 substrate build lands, or the two will silently cancel.

---

### MECH-234 -- DMS (goal-directed) and DLS (habitual) corticostriatal circuits can produce simultaneous parallel motor outputs only when targeting anatomically distinct motor effector pools...

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`**, reframed onto the
REE leg (cross-effector parallel expression), which is blocked on a multi-effector environment that
does not exist; the out-of-domain leg (the DMS/DLS anatomy) is already discharged by the two reviews
the claim itself cites, and the claim's *design ruling* has already been applied.

This is a **FUSED claim** and I am following the brief's instruction to reframe to the REE leg and
name the other. The two legs:
- **Out-of-domain leg (dominant in the title):** "DMS/DLS produce simultaneous parallel outputs only
  across anatomically distinct effector pools; within a pool, BG winner-takes-all." This is
  neuroanatomy. It is resolved, by Redgrave et al. (2010) `10.1038/nrn2915` and Balleine &
  O'Doherty (2010) `10.1038/npp.2009.131`, both already cited in the block. No REE substrate at any
  level bears on it. It should not be carried as an open mechanism_hypothesis.
- **REE leg (the reframe):** "in a substrate whose outputs share one effector pool, an independent
  parallel habitual channel (Layer 3) is not warranted; MECH-090 BetaGate's same-effector
  suppression is the correct model." This is a **design ruling on MECH-090** and it has already
  fired -- the block's own `notes` say Layer 3 "is not warranted" and names Layers 1+2 as the
  correct implementation.

**Extracted from:** the claim's own `notes` ("REE DESIGN IMPLICATION" paragraph) and its
`literature_evidence`. No `experimental_test` field exists; nothing drafted fresh.

**Currency check:** `ree_core/environment/` contains exactly one environment,
`causal_grid_world.py`. Its action space is a single discrete channel: `action_dim` (line 1529) is 5,
growing to 6 when the consummatory-act flag is on (lines 544, 2341-2344). There is no second
effector pool and no multi-effector environment anywhere in the tree. Zero evidence rows in
`claim_evidence.v1.json`. Zero reverse-dependencies in `claims.yaml` (checked by structural scan of
`depends_on` / `related_claims` / `supersedes` / `blocks` / `conflicts_with`). `depends_on: MECH-090`
(`active`) and `ARC-021` (`provisional`) are both live. **Answering the G3 brief's question
directly: MECH-234 does NOT contradict the single-commitment assumption the other four rest on -- it
is the claim that RATIFIES it for V3, and its same-effector leg is true by construction here.**

**epistemic_category (proposed):** `substrate_conditional` (set explicitly), with the out-of-domain
leg named in the claim text. Rationale for choosing `substrate_conditional` over `out_of_domain`:
the residual REE question *would* be helped by a substrate (a multi-effector environment), which is
the discriminator the brief's (c2) reserves `out_of_domain` for the absence of. Governance may
alternatively prefer to reclassify `claim_type: literature_synthesis` and close the REE leg as an
applied design ruling -- I flag that as the live alternative rather than deciding it here.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** The test requires an environment with **>= 2 anatomically
> distinct effector pools** -- two independently-commandable action channels whose commands are not
> mutually exclusive within a step. `ree_core/environment/causal_grid_world.py` has exactly one
> (`action_dim` 5-6, a single discrete choice, `causal_grid_world.py:1529, 2341-2344`), so on the
> current substrate the same-effector leg is TRUE BY CONSTRUCTION and the cross-effector leg is
> UNTESTABLE -- there is no non-degenerate run available and any "confirmation" would be vacuous.
> Additionally: a habitual channel distinct from the E3 deliberative channel must be separately
> observable (E1-direct or a policy-chunking output per `ree_core/policy/policy_chunking.py`,
> ARC-071), so that "both computed" can be distinguished from "one was expressed".
>
> **CONFIRMING (conditional on a multi-effector substrate landing).** With two channels A and B, and
> a committed E3 trajectory addressing channel A: (i) CROSS-DOMAIN -- the habitual output on channel
> B is expressed at a rate statistically indistinguishable from its uncommitted baseline (a
> ratio within [0.85, 1.15] with a bootstrap CI excluding 0.5), i.e. commitment does not suppress the
> other pool; AND (ii) SAME-DOMAIN -- the habitual output on channel A is suppressed relative to its
> uncommitted baseline by more than 3 SD of the per-seed suppression delta and by an absolute floor
> of 50% expression loss, in >= 2 of 3 seeds. The claim's content is the CONJUNCTION and the
> DISSOCIATION between (i) and (ii); either alone is a weaker claim.
>
> **FALSIFYING.** Either (i) fails -- commitment suppresses the *other* effector pool too, which
> would mean REE's commitment is a global gate rather than a per-effector one and would invalidate
> the "Layer 3 applies in multi-effector environments" half of the ruling -- or (ii) fails, i.e. the
> habitual channel is expressed on the committed effector concurrently with the deliberative one,
> which would refute the winner-takes-all model MECH-090's BetaGate encodes and reopen the Layer 3
> design question the claim closed. **For the out-of-domain leg, a counterexample looks like:** a
> peer-reviewed report of *simultaneous, independently-expressed* DMS- and DLS-driven motor output
> within a single effector pool in an intact animal (i.e. not sequential alternation and not
> cross-pool), which would contradict Balleine & O'Doherty (2010)'s qualification and require the
> title's "only when" to be weakened.

**Proposal sketch (only for a/d):** n/a.

**depends_on additions:** none. (`MECH-090` active, `ARC-021` provisional; both correct.)

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-234 has sat at `candidate` since 2026-04-15 with
zero evidence rows and zero reverse-deps while its operative content (a design ruling: do not build
Layer 3) was applied long ago. It is either (a) a `literature_synthesis` whose REE consequence has
been discharged, or (b) a `substrate_conditional` mechanism awaiting a multi-effector environment
that is not on any roadmap I could find. Leaving it as an undifferentiated `candidate`
mechanism_hypothesis costs governance a recurring adjudication with no possible next step.

---

### MECH-250 -- The end of exhalation provides a hard, periodic release signal for committed motor programs via respiratory-motor coupling...

**Recommended disposition:** **(g) merge with sibling -- PROPOSE ONLY: partial absorption into
MECH-108 (already BUILT and default-on, outside the group), with a narrowed but genuinely non-empty
residual.** MECH-250 must not be superseded outright: its residual is the only breath-timed
mechanism that can actually fire at the substrate's current operating point.

**Merge proposal, in the required form.**
- **Surviving id:** `MECH-108` (BreathOscillator). Built at `ree_core/heartbeat/clock.py`
  (`sweep_active`, `_breath_phase_step`, `_sweep_amplitude`, `_sweep_duration`), automatically wired
  at `agent.py:7287` (`sweep_reduction = self.clock.sweep_amplitude if self.clock.sweep_active else
  0.0`) and consumed at `agent.py:9256` -> `e3_selector.py:3600-3601`.
- **Absorbed id:** `MECH-250`, **partially**.
- **What text moves:** MECH-250's respiratory-motor-coupling biology (diaphragm and accessory-muscle
  relaxation at end-expiration; the cross-species observation -- dogs timing initiation to a sharp
  outbreath, human vocalisation on expiration, skilled striking actions clustering at exhale-end)
  should move into MECH-108's `notes` as its biological grounding. **MECH-108's code already carries
  a one-line version of it** (`clock.py:28`: "Biological basis: exhalation-phase respiratory coupling
  cyclically modulates..."), so the claims registry is currently *behind its own substrate* on this
  point -- the merge closes that gap rather than opening a new one.
- **What must NOT be absorbed (the residual, and it is real):** two orthogonal distinctions the
  claim itself draws and that the substrate genuinely does not implement.
  1. **WINDOW vs BOUNDARY.** MECH-108 asserts a sweep *window* (`sweep_duration = 5` of every
     `breath_period = 50` steps). MECH-250 asserts a *phase boundary* event at exhale-end. The
     boundary is derivable from `clock._breath_phase_step` but is not exposed as an event, and
     `EXHALE` / `receive_respiratory_phase` appear nowhere in `ree_core/`.
  2. **SOFTEN vs HARD-RELEASE, and this is the load-bearing half.** MECH-108 multiplies the
     threshold by `(1 - sweep_amplitude)` = `(1 - 0.25)`, i.e. **0.40 -> 0.30**. Against the measured
     un-inflated `running_variance` operating point of **0.005420** (V3-EXQ-794, quoted at
     `config.py:1058`) that is still ~55x away -- **so MECH-108's softening cannot produce a single
     uncommitted step at the current operating point.** This is almost certainly why MECH-108 has
     zero evidence rows despite being on by default. MECH-250 instead asserts an unconditional
     `beta_gate.release()` -- and `BetaGate.release()` exists (`ree_core/heartbeat/beta_gate.py:178`,
     with ten call sites in `agent.py`). **A hard release is therefore the only breath-timed
     mechanism that can fire at all on this substrate**, which makes MECH-250's residual more
     valuable after the merge, not less.
- **Reverse-deps needing repointing:** **none.** Structural scan of `claims.yaml` finds zero
  `depends_on` / `related_claims` / `supersedes` / `blocks` / `conflicts_with` references to
  MECH-250. (Note the *forward* chain MECH-250 -> MECH-108 -> MECH-104 exists and is unaffected.)

**Extracted from:** the claim's own `notes` -- specifically its explicit MECH-108 contrast ("not a
threshold-softening effect but a positive release trigger: it actively drives beta_gate.release()")
and its implementation hint ("extend BetaGate with `receive_respiratory_phase(phase) -> release at
EXHALE_END`, driven by the MultiRateClock breath cycle state"). Not drafted fresh.

**Currency check:** `beta_gate.release()` exists (`heartbeat/beta_gate.py:178`). The MultiRateClock
tracks a breath cycle (`clock.py:83-97`) but exposes only the boolean `sweep_active` (line 108) --
**no phase-boundary event, no `receive_respiratory_phase`, no `EXHALE` token anywhere in
`ree_core/`** (whole-tree grep). So MECH-250's implementation hint is accurate and unbuilt.
Meanwhile its dependency MECH-108 is *further along than the registry says*: built, auto-wired, and
ON by default in every experiment-built config because `REEConfig.from_dims()` defaults
`breath_period = 50` (`config.py:8169`, assigned `config.py:9791`) against a dataclass default of 0
(`config.py:3148`) -- yet MECH-108 carries `epistemic_category: substrate_conditional` and zero
evidence rows. MECH-250's other dependencies: `ARC-028` `candidate`, `MECH-091` `candidate`,
`MECH-090` `active`. Zero evidence rows for MECH-250 itself.

**epistemic_category (proposed):** `substrate_conditional` (set explicitly) for the residual after
absorption. The positive release trigger has never been exercised because the code does not exist;
blocking substrate = a phase-boundary event on `MultiRateClock` plus
`BetaGate.receive_respiratory_phase()`. This is a small, well-specified build.

**Draft `what_would_answer`** (written for the residual, i.e. after the MECH-108 absorption -- the
question is *hard release at a boundary*, not *periodic uncommitted windows*, which is MECH-108's):

> **NON-DEGENERACY PRECONDITION.** See the group's shared COMMIT-GATE DYNAMIC-RANGE PRECONDITION
> (G3 preamble (iii)); do not re-derive it. Specific to this claim, and decisive: the run must
> establish that **MECH-108's existing threshold softening is INERT at the run's own operating
> point** -- report `effective_threshold` under sweep (`0.40 x (1 - sweep_amplitude)`) against the
> realised `running_variance` distribution, and confirm the softened threshold is not crossed. If
> the sweep alone *does* produce uncommitted steps in this configuration, MECH-250's residual is not
> separable from MECH-108 in that run and the run cannot adjudicate it -- re-derive the operating
> point first. Additionally: (a) the committed-fraction in the release-OFF control arm must be
> strictly between 0 and 1, and specifically **high** (> 0.8) -- a hard release is only observable
> against a background of sustained commitment; (b) the breath cycle must be running
> (`breath_period > 0`) and the exhale-end boundary must be counted, with `n_boundaries >= 20` per
> episode-block; (c) MECH-104's surprise impulse must be pinned off (no rv injection,
> `_ema_alpha` at its default) so that de-commitments cannot be attributed to two mechanisms at
> once (G3 preamble (iv)).
>
> **CONFIRMING.** With a `receive_respiratory_phase(EXHALE_END) -> beta_gate.release()` build, on a
> matched-seed RELEASE-ON vs RELEASE-OFF pair (both with `breath_period = 50`, so MECH-108's sweep is
> identical in both arms and cancels): (i) **PHASE-LOCKING** -- committed -> uncommitted transitions
> in the ON arm cluster at the exhale-end boundary, with a circular-phase concentration over the
> breath cycle whose Rayleigh test rejects uniformity at p < 0.01 in >= 2 of 3 seeds; and
> (ii) **CAUSAL CONTRIBUTION** -- the ON arm's transition rate exceeds the OFF arm's by more than
> 3 SD of the per-seed rate delta and by an absolute floor of 1 transition per 5 breath cycles.
> Leg (i) is what distinguishes MECH-250 from any generic periodic de-commitment, and (ii) is what
> distinguishes it from MECH-108's already-present sweep.
>
> **FALSIFYING.** (ii) holds but (i) fails: transitions increase but are uniformly distributed over
> the breath cycle, meaning the mechanism is a periodic release *rate* rather than a
> *phase-locked boundary* event -- that refutes MECH-250 as written and collapses the residual back
> into MECH-108's window model, i.e. it makes the full absorption correct after all. Alternatively,
> (i) and (ii) both hold but the OFF arm shows the same transition rate once `breath_period = 0` is
> also tested as a third arm -- meaning the transitions were produced by the sweep, not the release.
> A third pattern, and the cheapest to hit: the OFF arm's committed-fraction is already < 0.8 in
> the control, so there was never sustained commitment for a release to break -- that is the
> precondition failing, and is a re-design signal, not a result.

**Proposal sketch (only for a/d):** n/a -- disposition is (g), and the run above is only writable
after the (small) substrate build. If governance prefers, route
`MultiRateClock` phase-boundary event + `BetaGate.receive_respiratory_phase()` to
`/implement-substrate` as a single entry, since it is fully specified by the claim's own hint.

**depends_on additions:** none needed; `MECH-108`, `ARC-028`, `MECH-091`, `MECH-090` are all present
and correct.

**GOVERNANCE FLAG:** `stale_note` (concerns MECH-108, surfaced via MECH-250's dependency) --
MECH-108 carries `epistemic_category: substrate_conditional` while its BreathOscillator is built
(`heartbeat/clock.py`), auto-wired (`agent.py:7287` -> `9256` -> `e3_selector.py:3600`), and ON by
default in every experiment-built config (`REEConfig.from_dims` defaults `breath_period = 50`,
`config.py:8169/9791`, against a dataclass default of 0 at `config.py:3148`). It nonetheless has zero
evidence rows -- most likely because its 25% threshold softening (0.40 -> 0.30) is arithmetically
inert against an rv operating point of ~0.0054. Either the category is stale, or MECH-108 is a
*built-but-inert* mechanism, which is a different and more interesting finding. Worth one
adjudication.

---

### SD-105 -- Selection-entropy headroom floor: a TONIC behavioural-variability set-point on the E3 selection softmax temperature (one-sided integral controller in log-temperature)

**Recommended disposition:** **(f) defer with a durable `digestion_note`** -- the claim was
registered today and is well-formed, but its own registered validation route was **killed the same
day** by a BLOCKING red-team verdict that neither the claim block nor its design doc records, and
the named fix requires a substrate capability SD-105 does not have. What must be resolved first is
named precisely below. (Secondary reading, if governance prefers a category to a defer:
`substrate_conditional` on the freeze/share API.)

**Extracted from:** the claim's own `functional_restatement` and `implementation_note`; the module
docstring at `ree-v3/ree_core/regulators/selection_entropy_floor.py` (which specifies the controller
and its `get_state()` reporting surface, including `headroom_met`, `saturated`,
`n_ticks_saturated`); the design doc
`REE_assembly/docs/architecture/sd_105_selection_entropy_headroom_floor.md`; and -- decisively --
the STEP 4.5 RED-TEAM VERDICT block at
`ree-v3/experiments/v3_exq_963b_mech063ii_tonic_phasic_dissociation_retest.py:544-640`.

**Currency check -- the block is complete but two of its statements are already false.**
- *Complete:* the block carries id/title/claim_type/subject/polarity/status/live_status/
  epistemic_category/implementation_phase/v3_pending/version_relevance/claim_level/registered_utc/
  depends_on (SD-074, MECH-313)/related_claims (SD-104, SD-069, MECH-063)/source/
  functional_restatement/implementation_note. Its design doc exists (164 lines). **Missing:**
  `location` (all four siblings in G3 carry one) and `notes`. One reverse-dep: SD-104
  `related_claims`.
- *Built and default-off, as claimed:* `ree_core/regulators/selection_entropy_floor.py` exists;
  `use_selection_entropy_floor: bool = False` with `_target 0.15`, `_gain 0.5`,
  `_max_temperature_ratio 8.0`, `_ema_decay 0.2`, `_deadband 0.05` (`config.py:4430-4446`, wired
  through `from_dims` at `config.py:7359-7364, 8793-8794`); application site at `agent.py:1225`.
  Contracts B1-B10 exist. Zero evidence rows. Substrate_queue entry
  `sd_phasic_burst_decay_and_warmup_headroom` is `implemented_pending_validation` /
  `status_phase: validation_owed`, both legs built.
- **FALSE STATEMENT 1 -- "validation is V3-EXQ-963b" (in `functional_restatement`), and
  substrate_queue's `validation_experiment: "... queued by campaign-c2c-20260904"`.** V3-EXQ-963b
  was **not queued**. ree-v3 commit `d2104f8` is titled *"V3-EXQ-963b driver: BLOCKING red-team
  verdict recorded, NOT queued"*; the live queue snapshot (ree-v3 `99817b6`, 2026-09-04) contains
  only V3-EXQ-1002 / 983a / 993a; `git log -S"963b" -- experiment_queue.json` returns nothing.
- **FALSE STATEMENT 2 (implicit) -- that arming SD-105 in a difference-of-arms design is sound.**
  Red-team finding **F1, "CONFIRMED / NOT FIXED (the blocking core)"**: *"SD-105 is a closed-loop
  SET-POINT controller on S_sustained_entropy -- the exact DV C1's dS_tonic contrast reads... A
  set-point controller applies a DIFFERENT lift per arm precisely because arms start at different
  entropies, so it COMPRESSES the contrast rather than cancelling it."* Verified against
  V3-EXQ-963a's own per-arm data: at `SEF_TARGET = 0.12` the controller would lift some arms and
  hold others on 4 of 5 seeds, and *"on seeds 23/29/37 it lifts exactly the TONIC-OFF arms and holds
  the TONIC-ON arms -- differentially compressing dS_tonic in the direction that destroys C1."* The
  verdict also notes SD-105's R5 gate *"passes by construction (the controller drives T0P0 toward
  0.12 > E_SAT_LOW) -- a gate certifying its own subject."* The named fix (successor requirement
  (a)): converge the controller ONCE and apply a **single FROZEN, SHARED multiplier** uniformly to
  all arms -- and *"SD-105 has no freeze/share API today, so this is a substrate or driver-harness
  build, not a config change."*
- The design doc is stale in the same way: line 151 still names V3-EXQ-963b as the validation, and
  the doc contains no mention of freeze/share or of F1.

**epistemic_category (proposed):** **`substrate_conditional`** (change from the currently-registered
`standard`). Rationale against the CLAUDE.md discriminator: the mechanism is *coded* but has been
**exercised zero times** (no evidence rows, no queued run), and the only validation design put
forward has been shown to be structurally unable to discriminate; the upstream capability it now
depends on -- a converge-once / freeze / share-multiplier mode -- is *planned but not built*. That
is `substrate_conditional`, not `substrate_ceiling` (nothing downstream is absorbing SD-105's
signal; SD-105 is itself the thing that would absorb the *consumer's* signal). Governance may
reasonably prefer to leave `standard` and rely on the defer note; I flag the disagreement rather
than assume it.

**Note on what IS already discharged.** SD-105 splits cleanly into two legs and only one is in
doubt. The **arithmetic/design leg** -- one-sidedness (multiplier never < 1.0), the reporting cap
(`saturated` surfaced rather than hidden), tonic placement after MECH-313 and before the SD-069
phasic delta, and EMA/integrator survival across `reset()` -- is a proof obligation already
discharged by contracts B1-B10 in
`ree-v3/tests/contracts/test_sd104_sd105_burst_decay_and_entropy_headroom.py`. Only the **empirical
leg** (that the floor restores usable dynamic range *without distorting the contrast a consumer
reads*) is open, and F1 is a direct argument that as a live closed loop it does distort it.

**Draft `what_would_answer`** (written for the FROZEN-multiplier form, which is the only form that
can be validated; the live closed-loop form is what F1 rules out):

> **NON-DEGENERACY PRECONDITION.** (a) The controller must have something to do: the **un-armed**
> baseline realised normalized selection entropy on the warmed agent must sit **at or below the R5
> saturation floor** -- V3-EXQ-963a measured 0.0195-0.153 against V3-EXQ-779a's 0.152-0.610 on the
> same design -- because if the baseline already clears the band, an entropy floor is inert and the
> run measures nothing. (b) The multiplier must be **FROZEN AND SHARED**: converged once (e.g. on
> the T0P0 baseline during warmup) and then applied as a single constant to every arm in the read
> phase. A LIVE closed loop is disqualified by construction in any difference-of-arms design whose
> DV is realised selection entropy -- see the V3-EXQ-963b F1 verdict at
> `v3_exq_963b...py:556-580`; do not re-derive that argument, and do not accept "armed identically
> in all arms, so it cancels" (that reasoning was explicitly withdrawn by the session that wrote
> it). (c) `saturated` must be reported per arm and must be **False** -- a saturated controller has
> stopped integrating and the cell is uninformative by SD-105's own reporting contract. (d) The
> **committed-fraction must be pinned and reported per arm** (G3 preamble (iv)): SD-105 integrates
> `e3.last_precommit_probs`, which is written inside `select()`, so the entropy EMA is confounded
> with the commit duty cycle -- MECH-108's sweep is on by default and MECH-104/MECH-250 would move
> it further. (e) `use_noise_floor` (MECH-313) must be pinned in a known state, since it is the
> state-independent lift on the same channel.
>
> **CONFIRMING.** With a frozen, shared multiplier `m >= 1.0` applied uniformly: (i) **HEADROOM
> RESTORED** -- the T0P0 baseline entropy moves from below `E_SAT_LOW` (0.02) to inside the
> 0.02-0.98 band on >= 4 of 5 seeds, with `saturated = False` throughout; AND (ii) **CONTRAST
> PRESERVED, which is the load-bearing half** -- the tonic contrast `dS_tonic` measured under the
> frozen multiplier is statistically indistinguishable from the same contrast measured with the
> multiplier off, on a per-seed paired comparison (paired difference CI containing 0, and
> |mean paired difference| below 0.25 x the multiplier-off `|dS_tonic|`). Leg (ii) is exactly what
> the live closed loop fails and what a frozen multiplier is claimed to fix; a run reporting only
> (i) has certified its own subject (the R5-passes-by-construction defect F1 names).
>
> **FALSIFYING.** (i) holds and (ii) fails -- the frozen multiplier lifts every arm off the floor
> but still compresses `dS_tonic` beyond the band above. That would mean the compression is not an
> artifact of the *closed loop* but of *raising the temperature at all*, i.e. entropy headroom and
> contrast fidelity are not jointly achievable on this channel, and SD-105's central assertion
> (that the warmup branch of the autopsy's fork is the right one, and re-deriving R5's band is
> wrong) is refuted -- the autopsy's *second* branch would then be the only one left. Second
> falsifying pattern: (i) fails because reaching the target requires a multiplier beyond
> `selection_entropy_floor_max_temperature_ratio` (8.0), i.e. `saturated = True` -- the floor is
> unreachable on a warmed agent, and SD-105 is inert where it is needed most. Third: the frozen
> multiplier restores baseline entropy but the consumer's own criterion (MECH-063 (ii) C1) still
> cannot discriminate for the *independent* reasons F2/F5/F6 name (additive-in-temperature phasic
> delta shrinking against a lifted baseline; per-arm warm caches making `dS_phasic` a
> weights-difference; `R_transient` with no lever-off control) -- in which case SD-105 is vindicated
> and the *consumer's* design is the problem, and that must be recorded as such rather than charged
> back to SD-105.

**Proposal sketch (only for a/d):** n/a -- disposition is (f). What must be resolved first, verbatim
for the `digestion_note`:

> DEFERRED 2026-09-04 (thought-digestion G3). SD-105's registered validation V3-EXQ-963b was NOT
> queued: ree-v3 `d2104f8` records a BLOCKING Step-4.5 red-team verdict whose core finding (F1) is
> that SD-105, as a LIVE closed-loop set-point controller, sits on the exact DV the consumer's
> criterion reads and differentially compresses it -- verified against V3-EXQ-963a per-arm data
> (on seeds 23/29/37 it lifts the TONIC-OFF arms and holds the TONIC-ON arms). Both outcomes of the
> R6 guard are unproductive (R6 fails -> requeue; R6 passes -> SD-105 was inert) and R5 passes by
> construction. RESOLVE FIRST, in order: (1) build the converge-once / FREEZE / SHARE-multiplier
> mode named in that verdict's successor requirement (a) -- SD-105 has no such API today, so this is
> a substrate or driver-harness build, not a config change; (2) re-point
> `substrate_queue.sd_phasic_burst_decay_and_warmup_headroom.validation_experiment` and this claim's
> `functional_restatement` off V3-EXQ-963b onto the successor; (3) update
> `docs/architecture/sd_105_selection_entropy_headroom_floor.md` (line 151 still names 963b and the
> doc has no freeze/share section). Until (1) lands, SD-105 has no runnable validation and its
> `implemented_pending_validation` reading should not be read as "one run away".

**depends_on additions:** none required. `SD-074` and `MECH-313` are both correct and were verified
resolved before the build (substrate_queue `depends_on_resolved_note`, 2026-09-04). Consider adding
`MECH-108` to `related_claims` -- MECH-108's sweep is on by default and perturbs the commit duty
cycle that SD-105's entropy EMA integrates (G3 preamble (iv)); that coupling is currently recorded
nowhere.

**GOVERNANCE FLAG:** `contested_disposition` -- SD-105 was registered 2026-09-04 asserting the
autopsy's "warmup must leave headroom" branch and naming V3-EXQ-963b as its validation. On the same
day, ree-v3 `d2104f8` recorded a BLOCKING red-team verdict whose core finding (F1, "CONFIRMED / NOT
FIXED") is that SD-105 cannot be validated as a live closed loop in a difference-of-arms design whose
DV is the quantity it regulates, and requires a freeze/share API SD-105 does not have. Neither the
claim block, its `functional_restatement`, its `implementation_note`, nor its design doc records
this. The claim is not thereby wrong -- but "IMPLEMENTED ... validation is V3-EXQ-963b" currently
reads as one run from resolution when it is one substrate build plus a re-designed run away.

**GOVERNANCE FLAG:** `stale_note` -- `evidence/planning/substrate_queue.json`,
`sd_phasic_burst_decay_and_warmup_headroom.validation_experiment`, states V3-EXQ-963b was "queued by
campaign-c2c-20260904". It was not (ree-v3 `d2104f8`; the live queue snapshot `99817b6` holds only
V3-EXQ-1002 / 983a / 993a; `git log -S963b` on the queue file is empty). The entry sits at
`status_phase: validation_owed` with no owner for the owed validation.

---

<!-- G5 appended 2026-09-04T21:18:57Z -->
## G5 -- earned authority / shared epistemic state / rule_state closure  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the brief grouped these on ARC-121
  `depends_on` SD-034 (6.00) and on ARC-120 <-> ARC-121 sharing an architectural namespace plus a
  claimed common source, the 2026-08-27 developmental-integration intake (4.25). **The second half of
  that rationale is wrong and should not be carried forward** (see Currency findings 1). The grouping
  nevertheless holds for a better reason that the similarity metric could not see: **all three are
  UMBRELLA/FRAMING claims sitting on top of already-built machinery, each of which has already had its
  sharp, testable content decomposed out into named children** -- ARC-120 -> ARC-130/ARC-131,
  SD-034 -> MECH-445/MECH-446, ARC-121 -> MECH-482/MECH-483. That shared shape, not the subject
  matter, is what makes them one digestion problem: the standing risk for all three is drafting a
  falsifier that silently re-tests a child's question, and the correct output for each is a falsifier
  fenced to the residual the children do NOT own.

- **(i) same-claim / merge candidates:** **No merge inside the group.** ARC-120 and ARC-121 are not
  two readings of one commitment: different `subject` namespaces
  (`architecture.competence_before_authority_framing` vs
  `architecture.epistemic_state_centrality_framing`), disjoint `depends_on` sets except MECH-094, and
  different falsification corpora (ARC-120's is the registry of accepted authority-granting
  mechanisms; ARC-121's is the set of belief/uncertainty containers in `ree_core/`). ARC-121 does NOT
  name a substrate ARC-120 presupposes -- ARC-120's authority gates are predicates over eligibility,
  mode and provenance, none of which requires a unified epistemic-state object; ARC-120 would survive
  intact in an architecture where every mechanism kept private belief state.
  **Merge pressure exists, but it points OUTSIDE the group in all three cases, and in all three cases
  the registry has already adjudicated it as non-supersession:** ARC-130 (`depends_on: ARC-120`,
  "base 5-stage sequence this refines/extends -- NOT superseded, ARC-120 remains sole owner of its own
  sequence"); ARC-128 (`depends_on: SD-034`, "DISTINCT FROM SD-034: SD-034 is a single IMPLEMENTED
  instance"); MECH-482/483 (`depends_on` of ARC-121, its local instances). **One PARTIAL absorption is
  worth proposing (g), and only one:** ARC-120's title carries a five-stage ladder
  ("existence -> representation -> competence -> authority -> behavioural influence") whose first four
  stages are reproduced verbatim inside ARC-130's longer, better-evidenced ladder
  ("existence, representation, endogenous recruitment, local operation, competitive authority,
  committed throughput, ecological consequence, retention/generalisation"), and ARC-130 has a
  2026-08-26 `evidence_quality_note` adjudicating its ladder CONFIRMED-SUPPORTS while ARC-120 has
  `exp_count 0`. Proposal: **narrow ARC-120's title to its ORDERING assertion** ("authority is earned
  through demonstrated competence, never granted merely because a computation exists") and have the
  ladder itself cross-reference ARC-130 rather than restate it. Absorbed text: the parenthetical
  stage list. Surviving id: ARC-120 (it is the `depends_on` target of both ARC-130 and ARC-131 and
  cannot be retired). Reverse-deps needing no repointing: ARC-130, ARC-131, ARC-135
  (`related_claims`), GOV-CAPCONTRACT-1 (`related_claims`). This is a narrowing, not a merge; I am
  proposing it, not applying it.

- **(ii) contradictions / undercut premises:** **Yes -- one sharp, and it is the group's best finding.**
  ARC-121 asserts that REE's mechanisms *increasingly converge* on a SHARED epistemic-state object,
  and it names **MECH-482 (`epistemic_deficit`) as its first dependency, i.e. as an instance of that
  convergence.** In `ree_core/` today, `epistemic_deficit` is referenced in exactly **4 files** --
  its own module `ree_core/policy/epistemic_deficit.py`, `ree_core/policy/__init__.py`,
  `ree_core/utils/config.py` (declaration only), and `ree_core/agent.py`, where it is wired as a
  **single-consumer source for one knob** (`curiosity_learning_progress_source == "epistemic_deficit"`,
  agent.py:1815-1920). Harm/ethics evaluation, replay, planning and the closure operator -- the exact
  consumers ARC-121's own title enumerates -- do not read it. Compare `hypothesis_tag` (MECH-094,
  ARC-121's fourth dependency): 24 files, 11 subpackages. **ARC-121's own dependency set therefore
  contains both its cleanest confirming instance and its cleanest counterexample**, and the
  counterexample is the more recently worked one (its substrate entry
  `sd_epistemic_deficit_multitarget_readiness` was added 2026-08-30 and is still
  `implemented_pending_validation`). This is not fatal -- one private container falsifies the
  convergence TREND, not the framing -- but it must be in the claim's falsifier text rather than
  discovered again by the next session.
  A second, weaker tension, worth recording because it is ARC-120's first live test case rather than a
  problem: SD-034's `functional_restatement` calls mode-conditioning a "critical falsifiability
  constraint," while the closure operator's newest firing route (`habenula_tick`, ARC-108 JOB-2,
  2026-06-22) deliberately does NOT gate on operating mode ("the abort does NOT gate on
  mode-conditioning -- a worse-than-expected outcome aborts content-wise regardless of operating
  mode", closure_operator.py:546-548). It is still gated on `hypothesis_tag is False` (MECH-094) and
  `beta_gate.is_elevated`, so **ARC-120 survives its most recent test case** -- but SD-034's
  mode-conditioning clause has an unrecorded carve-out.

- **(iii) shared falsifier:** Yes, one, and it runs from SD-034 to ARC-121, not the other way.
  ARC-121's confirming metric -- how many distinct `ree_core/` subpackages read a given epistemic
  container -- is measured on objects SD-034 and MECH-094 own (`rule_state`, `hypothesis_tag`).
  ARC-121's draft below therefore **quotes the census rather than re-deriving a separate notion of
  "shared"**, and any future revision of what counts as a shared epistemic object should be made once,
  in ARC-121, and cross-referenced by the others. In the other direction there is **no** shared
  falsifier between SD-034 and ARC-120: SD-034's residual question is an ablation (is closure
  necessary?), ARC-120's is a registry audit (is any accepted authority ungated?), and running one
  tells you nothing about the other.

- **(iv) cross-cutting finding:** **All three claims' residual falsifiers are ADJUDICATION or AUDIT
  obligations, not new experiments -- with exactly one exception, and identifying that exception is
  the point of this pass.** ARC-120's is a registry/design-review predicate plus a cross-tag of
  evidence that already exists (ARC-130's 2026-08-26 note names the runs and explicitly assigns them
  to ARC-120's rung); ARC-121's is a static code census, decidable today with no run at all; SD-034's
  retained core (five-part token firing, No-Go install, residue discharge) is already discharged by
  V3-EXQ-460d (`n_closures >= 1`, `nogo_installed >= 1`) and V3-EXQ-466e (PASS/supports). **The one
  genuinely un-run question in the group is SD-034's OWN primary falsifier -- the over-specification
  ablation ("can MECH-090/260/094 tuning alone produce the closure signature?") -- which no child owns
  and which has never been run in five months and thirteen SD-034-lineage experiments.** Every one of
  those thirteen tested whether closure has DE-COMMIT AUTHORITY; none tested whether closure is
  NECESSARY. The mutual-confound corollary: a null on MECH-445/446 (de-commit coupling/magnitude) is
  NOT a null on SD-034, and the registry already enforces this correctly -- all of 460h/460i/460j/460k
  /460l/715/717 are tagged to MECH-445/446 and none to SD-034. Do not let a future session read the
  460-lineage FAIL history as SD-034 evidence.

- **Currency findings (stale notes, landed blockers, unreviewed results):**
  1. **The grouping rationale's source attribution is wrong.** ARC-120 and ARC-121 were both registered
     **2026-08-06** with `source: docs/thoughts/2026-08-06_scientific_evolution_of_ree.md` (the
     historical-archaeology intake, Observations 4 and 3 respectively). The 2026-08-27
     developmental-integration intake
     (`evidence/planning/thought_intake_2026-08-27_developmental_integration_and_readiness_programme.md`)
     merely **cross-references ARC-120** in its novelty table ("already owned") and lists it under
     `related_claims` for GOV-CAPCONTRACT-1 and ARC-135; **ARC-121 does not appear in that document at
     all** (grep: zero hits). Reading that doc for "their shared source" yields nothing about ARC-121.
  2. **ARC-120 has an unrecorded literature pull.** `evidence/literature/targeted_review_arc_120/`,
     5 entries dated **2026-09-02** (daw2005 uncertainty arbitration 0.74; lee2014 reliability
     arbitration 0.78; haruno2001 responsibility-gated control 0.72; luna2015 protracted control
     maturation 0.62; blumberg2013 twitch-bootstrapped authority, `mixed` 0.66). `lit_conf 0.852`,
     `overall_confidence 0.852`, `exp_conf 0.0`, quadrant `plausible_unproven`. The claim's `notes`
     still read as though no evidence pull had been attempted.
  3. **ARC-121's literature pull is still landing -- four entries are dated TODAY (2026-09-04).**
     9 entries total; `lit_conf 0.746`. **Two are `weakens`**: bach2012 (uncertainty encoded in
     distinct neural systems, 0.72 -- described in its own summary as "the clearest direct
     counter-evidence in the pull") and namburi2015 (dissociable BLA->NAc / BLA->CeM circuits with a
     causal double dissociation, 0.65). Seven support. Neither the pull nor its two weakens entries is
     reflected in ARC-121's block. Note the scope problem this creates -- see GOVERNANCE FLAG 5.
  4. **SD-034: V3-EXQ-466e is absent from claims.yaml.** `grep -c 466e claims.yaml` = 0.
     `v3_exq_466e_sd034_satisficing_residue_discharge_behavioural_20260625T030205Z_v3` ran
     **2026-06-25**, **status PASS**, `evidence_direction_per_claim: {SD-034: supports}`,
     `scoring_excluded: None` -- it is the **only genuine, non-excluded experimental entry SD-034 has**
     (`genuine_exp_count 1`, `pass_runs 1`, `fail_runs 0`, `exp_conf 0.616`, `overall 0.766`). It is
     already marked reviewed in `review_tracker.json`. Meanwhile SD-034's `live_status.evidence` still
     points at `failure_autopsy_V3-EXQ-466d_2026-06-24` (`non_contributory`) -- the SUPERSEDED
     predecessor -- with `as_of: 2026-07-11`. The block's most recent governance note is 2026-06-19.
  5. **The 460h re-queue named in SD-034's 2026-06-19 claim-synthesis note has long since run, and so
     have four successors.** 460h (2026-06-20), 460i (06-21), 460j (06-21), 460k (06-22), 460l
     (06-22), plus V3-EXQ-715 (07-06), 715a (07-06) and 717 (07-07). **Every one is tagged to
     MECH-445/MECH-446** (460l additionally MECH-090/342/ARC-108); **none to SD-034** -- the
     decomposition held exactly as designed. Outcomes: 460h/i/j/k/l all `non_contributory`;
     `substrate_queue.json` `f_dominance_conversion_ceiling` records
     "460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING"; 460k FAILed
     `closure_exclusive_eval_armed_hold 0/3`; V3-EXQ-717 is a `weakens` on MECH-445. All reviewed;
     `pending_review.md` shows **0 pending** as of 2026-09-04T18:57:45Z.
  6. **SD-034's `implementation_note` is stale in two ways.**
     `ree-v3/ree_core/governance/closure_operator.py` is now **816 LOC**, not the "616 LOC" recorded;
     and the note describes **two** completion entry points (automatic `tick()`, explicit
     `emit_closure`) while the code has **three** -- a **habenula negative-RPE abort**
     (`habenula_tick` / `ClosureOperatorConfig.habenula_abort_enabled` /
     `habenula_delta_threshold` / counter `_n_habenula_aborts`, exposed in `get_state()` as
     `n_habenula_aborts`) added by **ARC-108 JOB-2 on 2026-06-22**, which fires the SAME five-part
     `_fire`. `grep -c habenula_abort claims.yaml` = **0** -- this third caller of SD-034's operator is
     recorded nowhere in the registry.
  7. **SD-034's `pending_retest_after_substrate: true` is probably stale.** The retest it names is the
     non-cap-pinned de-commit DV, which was decomposed to MECH-445/446 on 2026-06-19 and has since had
     its own eight-run history. The umbrella inherited the flag from before the decomposition.
  8. **The 2026-06-13 `demote_to_candidate` deferral is still open and is now decidable.** Its own text
     says "re-evaluate the `conflict_ratio` post-rebuild before any provisional->candidate move."
     Post-rebuild (index generated 2026-09-04T14:48:23Z): `fail_runs 0`, `pass_runs 1`,
     `genuine_exp_count 1` -- every historical weakens is excluded as
     `stale_substrate` / `non_contributory` / `superseded`. The deferral should be formally closed as
     no-longer-applicable rather than left standing.
  9. **ARC-120 has zero experimental entries despite evidence at its rung existing and being named.**
     ARC-130's 2026-08-26 `evidence_quality_note` (chip-20260826-arc130-authority-throughput-evidence-tagging)
     explicitly withholds MECH-314/MECH-320 (`failure_autopsy_604a-624a-630_2026-06-03`) and MECH-341
     (V3-EXQ-614d) from itself on the ground that they "instantiate a DIFFERENT, EARLIER rung failure
     -- local operation without competitive authority ... which is the transition this claim's own
     notes explicitly assign to ARC-120," and says they were "left untagged on that basis, not
     overlooked." They were never tagged to ARC-120 either.
  10. **ARC-128 checked, as instructed: registered 2026-08-25, `depends_on: SD-034`,
      `epistemic_category: substrate_conditional`, `implementation_phase: v4`, DO-NOT-BUILD-in-V3, and
      NOT present in `claim_evidence.v1.json`. Its central factual assertion about SD-034 is
      CODE-CONFIRMED**: `ClosureEvent.reason` carries only
      `"auto-stable" | "explicit" | "skipped:<cause>"` (closure_operator.py:209), so SD-034 genuinely
      does not distinguish suspension from disengagement from interruption. ARC-128 is a legitimate
      V4 generalisation, not a duplicate, and no merge is indicated in either direction.
  11. **`substrate_queue.json` (177 entries) has NO entry for ARC-120, ARC-121, ARC-128 or MECH-511**
      -- consistent with ARC-120's own "introduces no new mechanism" and with ARC-128/MECH-511's
      explicit V4 parks. **MECH-511 checked as instructed**: it is `substrate_conditional` / v4 /
      "DO NOT build in V3 and DO NOT queue a V3 experiment", and it is a per-event *learning*
      eligibility gate, **not** a competence-gated *write-authority* build for ARC-120; the 2026-08-27
      intake lists it only as an `related_claims` neighbour. The two SD-034-relevant substrate entries
      are `commitment-closure-control-plane` (still `amend_implemented_pending_validation`) and
      `SD-034` itself (`implemented`).
  12. **Master switch is default-OFF and bit-identical OFF**: `use_closure_operator: bool = False`
      (config.py:5876), with `use_closure_env_completion_hook: False` and
      `closure_decommit_hold_ticks: 0`. `agent.py:2277-2284` enforces
      `use_closure_operator=True requires use_lateral_pfc_analog=True`. Per project memory
      `reference_claim_status_vs_default_off_flag`, SD-034's `provisional` status does not imply the
      knob is on in any production profile -- it is not.

---

### SD-034 -- Closure operator over committed rule_state: on satisfaction of a committed rule_state's...

**Recommended disposition:** **(a) testable now** -- the umbrella's OWN primary falsifier (is closure
emergent from MECH-090/260/094 tuning?) has never been run in thirteen lineage experiments, and it is
cheaply runnable today because the operator is BUILT, reaches `n_closures >= 1` on the 603n substrate,
has one PASSing non-degenerate DV (466e), and is bit-identical OFF -- so the ablation arm is free.

**Extracted from:** the claim's own `functional_restatement`, "Falsifiable (primary)" and
"Falsifiable (secondary)" clauses, verbatim in substance; the non-degeneracy gate is lifted from the
2026-06-12 amend's own retest gate ("n_closures>=1 reachable + nogo_installed>=1 on >=2/3 seeds");
the DV and its demonstrated non-vacuity come from V3-EXQ-466e. Nothing here is invented from a blank
page.

**Currency check:** `ree-v3/ree_core/governance/closure_operator.py` read (816 LOC; `use_closure_operator`
default False at `utils/config.py:5876`; three firing routes; `get_state()` exposes `n_ticks`,
`n_closures`, `n_habenula_aborts`, `stable_tick_count`, `active_pe_cap`, `last_event`);
`agent.py:2277-2284, 10189-10210` (lateral-PFC precondition, `notify_env_completion` hook);
`evidence/experiments/claim_evidence.v1.json` (2026-09-04T14:48:23Z: SD-034 exp=1 lit=9,
`exp_conf 0.616`, `pass_runs 1`, `fail_runs 0`, latest run 466e);
`v3_exq_466e_.../manifest.json` (PASS, `{SD-034: supports}`, 2026-06-25T03:02:05Z);
manifests for 460h/460i/460j/460k/460l/715/717 (all `evidence_direction_per_claim` on MECH-445/446,
none on SD-034); `review_tracker.json` (466e, 466d, 460h, 717 all reviewed); `pending_review.md`
(0 pending, 2026-09-04T18:57:45Z); `substrate_queue.json` (`SD-034` = `implemented`,
`commitment-closure-control-plane` = `amend_implemented_pending_validation`);
`docs/architecture/persistent_process_termination_taxonomy.md` sections 1-2a (ARC-128 comparison);
`closure_status.md` line 72 (`commitment_closure:GAP-4-battery`, in_progress, "466e RAN + PASSED");
`cross_plan_root_cause_synthesis_20260902.md` lines 122/138 (the 460 lineage's `substrate_not_ready`
self-routes share the observation->z_world->E1/E2 interface root; the GAP-4 battery's *b behavioural
cohort members will hit that gate, the non-behavioural members will not).

**epistemic_category (proposed):** `standard` -- **unchanged, and deliberately so.** SD-034 is
`design_decision`, its mechanism is BUILT and has been EXERCISED non-degenerately (466e), and the
residual question is a straight ablation on existing substrate. It is therefore neither
`substrate_conditional` (the code exists and has run) nor `substrate_ceiling` (the ON arm's DV is not
absorbed downstream -- 466e PASSed it). The `substrate_ceiling` reading applies to the DE-COMMIT
face, which is MECH-445/446's, not this umbrella's. No `live_status.reading` marker on SD-034
proposes either substrate category.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION -- two-sided, because this test has a tuned control arm that can be
> made vacuous as easily as the treatment arm. (ON side) `use_closure_operator=True` with
> `use_lateral_pfc_analog=True` (enforced, agent.py:2277), on the 603n foraging-competent substrate,
> and the closure path must demonstrably fire: `n_closures >= 1` AND `nogo_installed >= 1` on >= 2/3
> seeds -- this is the exact gate the 2026-06-12 amend pre-registered, and the exact defect
> V3-EXQ-460c hit (`n_closures = 0` despite env `sequence_completions` of 2/5/6). The residue-discharge
> DV must be non-flat, i.e. reproduce V3-EXQ-466e's demonstrated separation, not sit at floor.
> (OFF-tuned side) the control arm must be a real search and not a token one: at least 3 distinct
> settings each of the MECH-090 beta commit/release thresholds, the MECH-260 action-history depth, and
> the MECH-094 mode-gating predicate, with the BEST-performing member reported as the control, not the
> mean. If `n_closures = 0` in ON, or the tuned sweep collapses to a single point, the run self-routes
> `substrate_not_ready_requeue` and MUST NOT be scored in either direction. Report `n_ticks`,
> `n_closures`, `n_habenula_aborts` and the `skipped:<cause>` histogram from `ClosureOperator.get_state()`
> for every arm, so a null is attributable to a named skip cause rather than to "closure did nothing".
>
> CONFIRMING: three arms -- ON, OFF-baseline, OFF-tuned. SD-034 is supported if the ON arm reproduces
> the five-part token JOINTLY -- (a) MECH-090 beta release surviving `closure_decommit_hold_ticks`,
> (b) targeted MECH-260 No-Go on the just-completed action class, (c) within-domain residue attenuation
> with the 1e-6 floor asserted intact (the "residue cannot be erased" invariant), (d) a `closure_event`
> reaching SD-032a, (e) MECH-268 dACC pe rebaseline -- while the OFF-tuned arm reproduces at most ONE
> of the five; and if the ON-vs-OFF-tuned gap on the 466e residue-discharge DV exceeds
> max(1.5 x the pooled SD of the per-seed ON-minus-OFF-tuned delta, an absolute floor of 10% of the
> OFF-baseline within-domain residue mass) on >= 2/3 seeds. Scoring the five components SEPARATELY is
> load-bearing: a scalar composite would let a large residue effect mask the absence of the No-Go
> pulse, which is precisely the failure the 2026-06-12 amend was built to fix.
>
> FALSIFYING: the OFF-tuned arm reproduces >= 4 of the 5 components AND its residue-discharge DV lands
> within 1 SD of ON on >= 2/3 seeds. Then closure is emergent from the existing MECH-090/MECH-260/
> MECH-094 substrate and SD-034 is over-specification -- this is the claim's own primary falsifier,
> unchanged. SECONDARY (also the claim's own, and it routes elsewhere rather than weakening SD-034):
> if ON resolves verified-but-not-released but introduces PREMATURE disengagement -- beta released
> before the terminal step on a fraction of multi-step episodes exceeding OFF-baseline by more than
> the same margin -- then the SD-033a completion-condition detector or the mode-conditioning logic is
> wrong, not the operator; that outcome self-routes to the detector and MUST NOT be recorded as a
> weakens on SD-034.
>
> SCOPE FENCE (mandatory, and the reason this draft is fenced rather than broad): the closure->beta
> COUPLING face and the de-commit MAGNITUDE face are NOT in scope. They were decomposed out to
> MECH-445 and MECH-446 on 2026-06-19 (user-approved, spec
> `evidence/planning/claim_synthesis_SD-034-closure_2026-06-19.md`) and have since accumulated eight
> further runs of their own (460h/i/j/k/l, 715, 715a, 717). A null on either is NOT a null on SD-034,
> and no de-commit DV may be scored against this claim.

**Proposal sketch (a):**
- **title:** `V3-EXQ-466f -- SD-034 closure-operator NECESSITY ablation: three-arm ON / OFF-baseline /
  OFF-tuned(MECH-090 + MECH-260 + MECH-094 sweep) scored componentwise on the five-part done token`
- **related_claims:** SD-034 (primary, direction expected `supports` or `weakens`); MECH-090,
  MECH-260, MECH-094 (co-tagged -- the tuned arm is a direct test of THEIR sufficiency, so if
  OFF-tuned reproduces the signature they gain a `supports` while SD-034 takes the `weakens`);
  MECH-268, SD-032a (co-tagged, `non_contributory` expected -- they are components (d)/(e), not the
  question). **Explicitly NOT tagged:** MECH-445, MECH-446 (scope fence).
- **acceptance_checks:**
  1. ON arm gate: `n_closures >= 1` AND `nogo_installed >= 1` on >= 2/3 seeds, else
     `substrate_not_ready_requeue` and no scoring.
  2. OFF-tuned arm carries >= 3 settings per knob (9 configurations minimum); the best member is
     reported as the control and the full sweep is in the manifest.
  3. All five token components scored and reported separately; no scalar composite in the verdict.
  4. Residue floor invariant asserted: no field weight below 1e-6 in any arm.
  5. Bit-identical-OFF check: `use_closure_operator=False` reproduces OFF-baseline exactly (the
     existing contract in `test_sd034_decommit_hold_and_env_hook.py` covers the shape).
  6. `get_state()` telemetry (`n_ticks`, `n_closures`, `n_habenula_aborts`, `skipped:<cause>`
     histogram) emitted per arm per seed.
  7. `habenula_abort_enabled=False` in ALL arms -- the ARC-108 JOB-2 route is a third caller with
     different (deliberately un-mode-gated) semantics and would confound the necessity question.
  8. >= 3 seeds; per-seed deltas reported so the SD-scaled gate is computable rather than asserted.
- **Priority note:** per `cross_plan_root_cause_synthesis_20260902.md` line 138, GAP-4-battery's
  *behavioural* cohort members will hit the observation->z_world->E1/E2 interface gate; this ablation
  is a **non-behavioural** member of that battery (it scores the token's own components, not an
  ecological outcome), so it does NOT chain to that binding constraint and is runnable now. That
  distinction is the reason this is disposition (a) and not (c).

**depends_on additions (if any):** **ARC-108** -- if governance accepts the habenula abort as a
legitimate third caller of SD-034's `_fire`, it belongs in SD-034's dependency/cross-reference set;
today the coupling exists only in `ree-v3/CLAUDE.md` and in code. Recorded as a proposal, not applied.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- **V3-EXQ-466e (PASS, `{SD-034: supports}`,
2026-06-25T03:02:05Z, reviewed, `scoring_excluded: None`) is the ONLY genuine scoring experimental
entry SD-034 has and it appears nowhere in `claims.yaml`.** SD-034's `live_status.evidence` still
cites the superseded `failure_autopsy_V3-EXQ-466d_2026-06-24` (`non_contributory`) at
`as_of: 2026-07-11`, and the block's most recent governance note is 2026-06-19. The index already
reflects 466e (`exp_conf 0.616`, `overall 0.766`, `fail_runs 0`); the claim text does not. A session
reading only the block would conclude SD-034's evidence record is uniformly negative, which is the
opposite of the current state.

**GOVERNANCE FLAG:** `stale_note` -- SD-034's `implementation_note` records "616 LOC" and two
completion entry points; `closure_operator.py` is 816 LOC with **three** firing routes, the third being
the ARC-108 JOB-2 habenula negative-RPE abort (`habenula_tick`, `habenula_abort_enabled`,
`habenula_delta_threshold`, `_n_habenula_aborts`, added 2026-06-22, firing the same five-part `_fire`).
`grep -c habenula_abort claims.yaml` = 0. Additionally, that route **deliberately does not gate on
operating mode**, which is an unrecorded carve-out from SD-034's `functional_restatement`
mode-conditioning clause ("critical falsifiability constraint per SD-034 spec", also restated in the
module docstring). Either the clause needs a stated exception or the route needs a justification in
SD-034's block.

**GOVERNANCE FLAG:** `stale_note` -- two flags on this claim are now decidable and should be closed
rather than left standing: (i) `pending_retest_after_substrate: true`, whose named retest (the
non-cap-pinned de-commit DV) was decomposed to MECH-445/446 on 2026-06-19 and has since run eight
times under those ids; (ii) the 2026-06-13 `demote_to_candidate` recommendation, recorded as DEFERRED
pending a post-rebuild `conflict_ratio` re-evaluation -- post-rebuild is now available
(2026-09-04T14:48:23Z: `fail_runs 0`, `pass_runs 1`, all historical weakens excluded as
`stale_substrate`/`non_contributory`/`superseded`), so the deferral is resolved and the demotion is
not indicated.

---

### ARC-120 -- Behavioural/write authority in REE is (and should remain) EARNED through demonstrated...

**Recommended disposition:** **(b) derivational** -- its falsification condition is a standing
design-review predicate over the registry of ACCEPTED authority-granting mechanisms, discharged by
audit and by adjudicating evidence that already exists, never by a new experiment; the claim's own
notes say it "introduces no new mechanism" and is "falsified in the design sense." **Sequencing
condition on the category flip:** apply the evidence cross-tag flagged below FIRST and hold
`epistemic_category` at `standard` until it lands, because `derivational` suppresses promote/demote
and would freeze the one adjudication route ARC-120 has.

**Extracted from:** the claim's own `notes` -- "falsified in the design sense by any future accepted
mechanism that grants behavioural or write authority WITHOUT a competence-like gate" -- turned into a
decidable audit with a named corpus and a named non-degeneracy floor; plus ARC-130's 2026-08-26
`evidence_quality_note`, which supplies the confirming-side experimental instances by name and
explicitly assigns them to this claim's rung. The four gate TYPES in the CONFIRMING clause are
ARC-120's own `depends_on` set read as a taxonomy, not a fresh invention.

**Currency check:** live block re-read at `claims.yaml:81928-81971` (status `candidate`,
`epistemic_category: standard`, deps ARC-107 / SD-032b / MECH-261 / MECH-094 after the 2026-08-10 edge
correction that removed MECH-368 and INV-039); `claim_evidence.v1.json` (exp=0, lit=5,
`lit_conf 0.852`, `overall 0.852`, `pass_runs 0`, quadrant `plausible_unproven`, latest entry
`2026-09-02_arc_120_uncertainty_arbitration_daw2005`); `evidence/literature/targeted_review_arc_120/`
(5 entry dirs, all 2026-09-02, no SYNTHESIS.md yet); ARC-130 block (`claims.yaml:89891+`,
`depends_on: ARC-120`, "NOT superseded, ARC-120 remains sole owner of its own sequence", plus its
`evidence_quality_note`'s "CHECKED AND DELIBERATELY NOT TAGGED" paragraph); ARC-131 block
(`depends_on: ARC-120`, extends it "in the composition direction");
`thought_intake_2026-08-27_developmental_integration_and_readiness_programme.md` lines 65/68/82/190/234
(ARC-120 cited as already-owning the competence-to-authority bridge and the research-philosophy
principles; the capture's own recommendation is "test whether existing machinery suffices before
proposing a controller -- that is a workstream, not a claim"); `substrate_queue.json` -- **no ARC-120
entry, nothing to build**, consistent with the claim's own text; MECH-511 read in full and confirmed
NOT to be an earned-authority build (v4, `substrate_conditional`, explicit DO-NOT-BUILD-in-V3, and a
LEARNING-eligibility gate rather than a write-authority gate); `closure_operator.py:546-548, 559-586`
for the habenula test case below.

**epistemic_category (proposed):** `derivational` **once the cross-tag lands; `standard` until then.**
Rationale for not proposing `substrate_coherence` (the value `architectural_commitment` would
otherwise infer): `substrate_coherence` is for design choices that ARE the substrate, whereas ARC-120
is a *predicate over* substrate choices and is genuinely refutable by a single counterexample -- the
audit has a real fail state, which `substrate_coherence` would obscure. Rationale for not leaving it
`standard` permanently: `standard` demands `exp_conf` for promotion, and ARC-120 will never generate
its own experiment; leaving it there guarantees perpetual `lit_only` / `low_exp` flags. Note this is
the OPPOSITE recommendation to ARC-130, which correctly stays `standard` because its distinctive
post-authority clause does have its own runnable content.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION: this is an audit, and an audit over an empty or trivial corpus is the
> characteristic vacuity here. The corpus is every mechanism that ACTUALLY GRANTS AUTHORITY -- i.e.
> whose effect is to admit a signal to a committed-selection surface, a memory/representation write
> path, or a consolidation-rate control -- that was ACCEPTED (registered `active`/`stable`/
> `provisional`, code present in `ree_core/`, reachable on a production path, not default-off-and-
> never-enabled) since ARC-120's registration on 2026-08-06. **At least 5 such mechanisms must be in
> the corpus**; with 0-2 the correct output is "insufficient corpus", never "confirmed". Each must be
> classified gated/ungated by READING ITS ADMISSION PREDICATE IN CODE, not by reading its claim prose
> -- a claim whose text promises a gate that the code does not implement counts as UNGATED, and that
> asymmetry is the whole point of running the audit against `ree_core/` rather than against
> `claims.yaml`.
>
> CONFIRMING: every mechanism in the corpus conditions its authority grant on at least one
> competence-like predicate -- per-event eligibility (ARC-107), a learnable rather than fixed store
> (SD-032b), operating-mode write gating (MECH-261), real-vs-simulated provenance tagging (MECH-094),
> or a demonstrable equivalent. WORKED CONFIRMING INSTANCE, already in the record and usable as the
> audit's first row: the ARC-108 JOB-2 habenula de-commit (`ClosureOperator.habenula_tick`, ree-v3,
> 2026-06-22) grants a genuinely NEW behavioural authority -- abort a live commitment on a
> worse-than-expected outcome -- and gates it on `hypothesis_tag is False` (MECH-094, so a replay/DMN
> outcome cannot abort a waking commitment) AND `beta_gate.is_elevated` (nothing to de-commit
> otherwise). That is a competence-like gate, so **ARC-120 survives its most recent test case**, and
> it survives it in the informative direction: the gate was added for a reason internal to the
> mechanism, not to satisfy this claim. On the experimental side, ARC-120's rung is discharged by the
> authority-ABSENT findings ARC-130's 2026-08-26 note explicitly assigns to it -- MECH-314/MECH-320
> score-bias terms "dominated by the primary harm/goal score term, so they never change argmax"
> (`failure_autopsy_604a-624a-630_2026-06-03`), and MECH-341 firing "but leaving committed-class
> entropy invariant" (V3-EXQ-614d). These are instances of authority correctly NOT granted to a
> mechanism that had not earned it.
>
> FALSIFYING: one accepted, production-reachable mechanism whose authority-admission predicate reads
> ONLY on signal presence or magnitude -- no eligibility, mode, learnability or provenance condition --
> and whose acceptance was not flagged as a deliberate exception. One clean instance falsifies the
> normative half ("should remain"); a second instance PLUS a governance decision declining to add a
> gate falsifies the descriptive half ("is"). NEAR-MISS SHAPE TO REJECT, so the audit does not
> manufacture a false positive: an ungated INTERNAL scalar that cannot reach a committed surface is
> NOT a counterexample here -- it fails at competitive authority or committed throughput, which are
> ARC-130's rungs, not this claim's. The discriminator is whether the ungated signal demonstrably
> reaches a committed action, a durable write, or a consolidation rate.
>
> PROOF/AUDIT OBLIGATION (the artifact this claim resolves into, in place of an experiment): a dated
> table of the post-2026-08-06 authority-granting mechanisms, each with its admission predicate quoted
> from `ree_core/` and classified against the four gate types above, re-run at each governance cycle
> that accepts a new authority-granting mechanism. ARC-120 closes as resolved-by-derivation when that
> table has been maintained across a meaningful corpus with no ungated row; it is refuted the first
> time a row is ungated and stays ungated by decision.

**Proposal sketch (only for a/d):** not applicable -- this is (b). The deliverable is the audit table
above, not a queue entry. Explicitly do NOT queue an experiment for ARC-120: the claim's own text says
it "introduces no new mechanism" and has "nothing to build," and `substrate_queue.json` correctly
holds no entry for it.

**depends_on additions (if any):** none. **ARC-130 and ARC-131 already depend on ARC-120** (not the
reverse) and that direction is correct and should not be inverted -- ARC-120 is the base sequence, and
both extenders explicitly refuse to supersede it. See the (i) preamble for the narrowing proposal
(absorb the ladder parenthetical into ARC-130's, keep the ordering assertion here).

**GOVERNANCE FLAG:** `promotion_review` -- **ARC-120 carries `exp_count 0` while pre-existing,
CONFIRMED evidence at its own rung sits untagged, by an explicit decision recorded in a sibling
claim.** ARC-130's 2026-08-26 `evidence_quality_note` (chip-20260826-arc130-authority-throughput-
evidence-tagging) withholds `failure_autopsy_604a-624a-630_2026-06-03` (MECH-314/320) and V3-EXQ-614d
(MECH-341) from ARC-130 on the ground that they instantiate "local operation without competitive
authority ... the transition this claim's own notes explicitly assign to ARC-120," and says they were
"left untagged on that basis, not overlooked" -- but no corresponding tag to ARC-120 was ever made.
Recommend a cross-tag pass mirroring chip-20260826 exactly (set `diagnostic_evidence_adjudicated: true`
on ARC-120 with an `evidence_quality_note` naming those runs), since both are `claim_ids: []`
diagnostic-purpose findings that will otherwise never reach the index. This is adjudication of
existing evidence, not promotion.

**GOVERNANCE FLAG:** `stale_note` -- ARC-120 acquired a 5-entry literature pull on **2026-09-02**
(`evidence/literature/targeted_review_arc_120/`, `lit_conf 0.852`, one `mixed`: blumberg2013
twitch-bootstrapped authority) with no SYNTHESIS.md and no reflection in the claim's `notes`, which
still read as though the claim had never been evidenced. Per project memory `feedback_lit_exp_decoupled`
the literature is not co-equal with experiment, so this must not by itself move status -- but the pull
should be summarised into the block, and blumberg2013 in particular (authority bootstrapped from
pre-competence spontaneous twitching) is the nearest thing in the record to a biological counterexample
to a strict competence-before-authority ordering and deserves an explicit disposition rather than
silence.

---

### ARC-121 -- REE's mechanisms increasingly converge on maintaining and consuming a SHARED epistemic...

**Recommended disposition:** **(b) derivational** -- ARC-121's own stated falsifier is about REE's
substrate-development trajectory, which is decidable TODAY by a static census of `ree_core/` with no
experiment and no substrate work; and running that census already surfaces a live counterexample
inside the claim's own dependency set, which is a stronger and cheaper result than any experiment
would have produced.

**Extracted from:** the claim's own `notes` -- "Falsified in the design sense if REE's future substrate
development keeps adding local, mechanism-private belief/uncertainty representations rather than
converging toward anything approximating one shared epistemic-state object" -- operationalised into a
counting rule with a stated exclusion list, plus the measured baseline below. The "shared" predicate is
NOT re-derived here: it is defined once, in this claim, on the objects SD-034 and MECH-094 own, and the
group's other drafts point at it rather than restating it (preamble (iii)).

**Currency check:** live block re-read at `claims.yaml:81972-82013`; `claim_evidence.v1.json`
(exp=0, lit=9, `lit_conf 0.746`, `pass_runs 0`, quadrant `plausible_unproven`, latest entry
`2026-09-04_arc_121_vmpfc_lesion_moral_judgment_koenigs2007` at 14:28Z **today**);
`evidence/literature/targeted_review_arc_121/` -- 9 entry dirs, 5 dated 2026-09-02 and 4 dated
2026-09-04, including two `weakens` whose summaries I read in full (bach2012, namburi2015).
**Code census run against `/Users/dgolden/REE_Working/ree-v3/ree_core/`:** `hypothesis_tag` -> 24
files across `amygdala/`, `pfc/`, `sleep/`, `hippocampal/`, `residue/`, `predictors/`, `governance/`,
`latent/`, `cingulate/`, `regulators/`, `policy/` (11 subpackages); `rule_state` -> 10 files across
`pfc/`, `predictors/`, `cingulate/`, `regulators/`, `policy/`, `governance/`, `environment/`
(7 subpackages); `epistemic_deficit` -> **4 files** (`policy/epistemic_deficit.py`,
`policy/__init__.py`, `utils/config.py`, `agent.py`), with `agent.py:1815-1920` wiring it solely as
`curiosity_learning_progress_source == "epistemic_deficit"`. `E2WorldUncertaintyHead`
(`predictors/e2_world_uncertainty.py`) and `EpistemicDeficitAccumulator` are the only two
uncertainty/belief container classes in the tree by class-name search. Dependency blocks read:
MECH-482 (`substrate_conditional`, `candidate`, `pending_retest_after_substrate: true`, 2026-08-30
autopsy of V3-EXQ-964 found C2 "STRUCTURALLY UNSATISFIABLE" because `reset()` clears all persistent
targets every episode); MECH-483 (`substrate_conditional`, already carries a
`what_would_answer` -- used as the house-structure exemplar for this pass; no `orient_survey` /
`survey_regime` symbol exists in `ree_core/`, so it is genuinely unbuilt); SD-034 (see above);
MECH-094 (the shared object, 24 files). `substrate_queue.json`: no ARC-121 entry;
`sd_epistemic_deficit_multitarget_readiness` added 2026-08-30T07:25Z,
`implemented_pending_validation`. **ARC-121 is not mentioned anywhere in the 2026-08-27 intake.**

**epistemic_category (proposed):** `derivational`. The question is settled by working through the
architecture as built, not by experiment, and there is no substrate to wait for -- so neither
`substrate_conditional` (MECH-482 IS built and exercised; MECH-483 is not, but ARC-121 does not depend
on MECH-483 being built to be assessable) nor `substrate_ceiling` (nothing downstream is absorbing a
signal; the claim is about code topology). `derivational` also correctly suppresses `narrow_open_question`,
which would be meaningless for a convergence-trend framing.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION: the census must run over epistemic CONTAINERS -- a class or persistent
> agent attribute that holds belief / uncertainty / possibility / commitment state and is instantiated
> on a production path in `ree_core/` -- not over every module that mentions a keyword. The sharing
> measure for a container is the number of DISTINCT top-level `ree_core/` subpackages that READ it,
> excluding (i) its own defining module, (ii) that package's `__init__.py`, and (iii)
> `ree_core/utils/config.py`, which carries declarations only and would otherwise make every container
> look one-subpackage-shared. A census in which every container scores identically -- all shared or all
> private -- is uninformative about CONVERGENCE (which is a claim about a trend, not a state) and must
> be reported as uninformative rather than as a verdict; convergence requires at least two containers
> at different sharing levels and a defensible ordering by date of addition.
>
> CONFIRMING: newly added epistemic containers are read across >= 3 distinct subpackages -- they JOIN
> the existing shared objects rather than adding private ones -- and the shared:private ratio is
> non-decreasing across successive substrate additions. MEASURED BASELINE, ree-v3 `ree_core/` as of
> 2026-09-04, which any future census should be diffed against rather than re-derived:
> `hypothesis_tag` (MECH-094) = 24 files / 11 subpackages, spanning amygdala, PFC, sleep, hippocampal,
> residue, predictors, governance, latent, cingulate, regulators and policy -- strongly shared, and
> exactly the cross-mechanism consumption pattern ARC-121's title asserts (prediction, replay,
> harm/ethics evaluation, planning and learning all read it); `rule_state` (SD-033a / SD-034) = 10
> files / 7 subpackages -- shared, and read by both the closure operator and E3 selection, i.e.
> commitment really is a first-class object several mechanisms consume rather than one module's local
> variable. Those two are the claim's genuine confirming core and they are strong.
>
> FALSIFYING: newly added epistemic containers are confined to their own defining module plus the
> agent constructor -- private, single-consumer, with no cross-mechanism read path. **THIS PATTERN IS
> ALREADY PRESENT, and the instance sits inside ARC-121's OWN `depends_on` set.** `epistemic_deficit`
> (MECH-482, `ree_core/policy/epistemic_deficit.py`, substrate entry SD-102) is referenced in exactly
> 4 files -- its own module, `policy/__init__.py`, `utils/config.py` (declaration), and `agent.py`,
> where it is instantiated only when `curiosity_learning_progress_source == "epistemic_deficit"` and
> consumed as a single-purpose curiosity/learning-progress source (agent.py:1815-1920). It is NOT read
> by harm/ethics evaluation, replay, planning, or the closure operator -- the precise consumers
> ARC-121's title enumerates -- and its substrate was still being actively extended on 2026-08-30
> (`sd_epistemic_deficit_multitarget_readiness`, `implemented_pending_validation`) without acquiring a
> shared read path. So REE's most actively-developed belief/uncertainty addition is mechanism-private,
> which is the falsifying pattern the claim itself specifies. CALIBRATION, so this is not over-read:
> ONE private container falsifies the convergence TREND, not the framing -- the correct response is to
> amend ARC-121 from "increasingly converge" to "converge on some, not all, epistemic constituents",
> or to route `epistemic_deficit` into a shared read path and re-census. ARC-121 is falsified OUTRIGHT
> only if a SECOND post-registration epistemic container is added with no shared read path and no
> accepted plan to give it one -- at that point private-by-default is the architecture's actual
> practice and the framing is describing an aspiration rather than a trend.

**Proposal sketch (only for a/d):** not applicable -- (b). Deliverable is the dated census table
(container, defining module, reading subpackages, date added, shared/private), regenerable in one
`grep` pass, with the 2026-09-04 baseline above as row zero. Do NOT queue an experiment: the claim's
own notes already say it is "not directly falsifiable by a single experiment," and the reason is not
that it is hard to test but that it is not an experimental question at all.

**depends_on additions (if any):** none to ARC-121 itself. **Proposed cross-reference in the OTHER
direction (propose only):** MECH-482's block should record that its single-consumer wiring is
ARC-121's live counterexample, so that the next session extending SD-102 knows a second REE-level
claim is watching that wiring. Deliberately NOT proposing that ARC-121 depend on MECH-511, MECH-512 or
Q-079 -- the claim's own notes already fence Q-079's DLIF and SD-062's claims-index graph as "adjacent
and orthogonal, not merged," and that fence is correct and should be preserved.

**GOVERNANCE FLAG:** `contested_disposition` -- **ARC-121 is a FUSED claim and its literature pull is
scoring the wrong leg.** Its title and its stated falsifier are both about **REE's own architecture**
("REE's mechanisms increasingly converge...", falsified by "REE's future substrate development"),
which is a code-auditable, derivational question. The 9-entry pull (2026-09-02 and 2026-09-04, latest
14:28Z today) instead adjudicates a **biological-plausibility** leg -- whether the BRAIN uses one
shared epistemic-state object -- and produces two `weakens` on that basis: bach2012 (uncertainty
encoded in distinct neural systems; its own summary calls it "the clearest direct counter-evidence in
the pull") and namburi2015 (causal double dissociation between BLA->NAc and BLA->CeM valence circuits).
Both summaries are careful and explicitly flag the gap -- namburi2015's own limitations section notes
the dissociation is at an INPUT stage upstream of the vmPFC "common currency" hub the supporting
entries address, and bach2012's notes that "anatomically distinct encodings do not entail functionally
private state." So the entries are sound; the ROUTING is not. Recommend: (i) split the biological leg
out explicitly (either a `related_claims` pointer to the valuation/common-currency literature question
or a narrow sibling registration), (ii) re-scope the existing 9 entries as bearing on that leg, and
(iii) score ARC-121 itself on the code census. Left as-is, ARC-121 will accumulate biology `weakens`
against a claim about a Python package -- and per project memory `feedback_lit_exp_decoupled`, that
literature must not be treated as load-bearing for a REE-architecture assertion in any case.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- ARC-121 declares MECH-482 as a dependency and as an
instance of epistemic-state convergence, while the code shows `epistemic_deficit` is a 4-file,
single-consumer, mechanism-private container with no read path from harm evaluation, replay, planning
or closure. The claim's premise and its own dependency's implementation disagree. Not urgent and not a
demotion trigger (both are `candidate`), but it should be recorded on both blocks rather than
rediscovered: it is the concrete content of ARC-121's falsifier, and MECH-482's next substrate pass is
where it would cheaply be fixed.

---

### Cross-group note for the orchestrator (not a claim disposition)

The campaign brief attributed ARC-120 and ARC-121 to the **2026-08-27 developmental-integration
intake**. Both were registered **2026-08-06** from
`docs/thoughts/2026-08-06_scientific_evolution_of_ree.md` (Observations 4 and 3). The 2026-08-27
document cross-references ARC-120 four times as "already owned" and **never mentions ARC-121**. If any
other group's brief, or any tracked review file, carries the same attribution, it should be corrected
there too -- **`stale_note`**.

---

<!-- G6 appended 2026-09-04T21:18:57Z -->
## G6 -- committed-action diversity through selection  (agent report)

### Group preamble

- **Why these are together (restated, then my view).** The task framing was: MECH-442 `depends_on`
  both MECH-341 and MECH-294; 442 asserts diversity SURVIVES the commit, 341 asserts E3 scoring
  PRESERVES class diversity upstream, and 294 was assumed to "supply the per-cycle binding that makes
  *class* well-defined". **Two of those three premises do not survive contact with the substrate,**
  and the corrections are the main product of this pass:

  1. **MECH-294 does NOT define "class".** "Trajectory class" is defined in exactly one place --
     `ree-v3/ree_core/predictors/e3_score_diversity.py::E3ScoreDiversity._first_action_classes`
     (line 143): `int(first_step.argmax().item())`, i.e. the argmax of the candidate's *first action
     step*, over `action_dim == 5`. It has no dependence on theta-packet binding whatsoever.
     MECH-294's contribution to this pipeline is a **modulatory channel source**
     (`modulatory_channel_route_source="coherence"`, per-candidate co-binding coherence with a
     cross-candidate RANGE), which feeds the same selection authority MECH-442 would restrict. So
     294 relates to 442 as *one candidate content-source for the within-eligible-set bias*, not as
     the class-definer. MECH-442's `depends_on: MECH-294` comment ("selection-authority/binding
     substrate the archive must route around F with") is right about the *channel* and wrong if read
     as depending on 294's joint-binding **content** clause -- see the `depends_on` note under
     MECH-442.
  2. **MECH-442's mechanism is already largely BUILT, under MECH-341.** MECH-341 Option 2,
     `E3ScoreDiversity.stratified_select` (e3_score_diversity.py:240-330), is, verbatim from its own
     docstring: *partition candidates by first-action class -> per class pick the argmin-score
     candidate as class representative -> sample across class representatives with
     `softmax(-best_in_class_score / T)`*. That is a behavioural-descriptor partition, a **per-niche
     F-best elite**, and a **coverage-aware commit rule** -- MECH-442's stated mechanism, with the
     descriptor pinned to first-action class. It runs on BOTH the committed and uncommitted selection
     paths since the 2026-05-28 retune, and it carries the unit-range authority normalisation
     (2026-06-03). MECH-442's `notes` never mention this module; they cite only `e3_selector.select`
     top-k / modulatory-authority. **MECH-442's "not yet built" premise is materially stale.**

- **(i) same-claim / merge candidates.** **MECH-341 and MECH-442 are NOT the same claim** -- they are
  separated by an explicit, ratified scope boundary and by different readouts:
  MECH-341's 2026-06-14 ratification carries the EXPLICIT CAVEAT that it asserts scoring-layer
  **preservation** and *"does NOT assert that the preserved diversity reaches the COMMITTED action"*;
  MECH-442's DV is exactly committed-action-class entropy. So they are complementary layers, and the
  brief's second horn is the right one: **442 is the downstream test whose non-degeneracy
  precondition is 341 holding.**
  BUT there is real, **partial** merge pressure pointing at MECH-341's already-built
  `stratified_select` (in-group) and at MECH-448's built `f_demotion` eligibility envelope
  (out-of-group, `e3_selector.py:3757-3765`, which takes precedence over `top_k`). Between them they
  already instantiate: descriptor partition + per-niche elite + coverage-aware commit
  (`stratified_select`), and eligible-set restriction upstream of the argmax with F removed from the
  final arbitration (`f_demotion` / `top_k`). **Proposed PARTIAL absorption with a narrowed
  residual** (details in the MECH-442 entry): MECH-442's surviving, genuinely-unbuilt residual is
  only *(a)* descriptors OTHER than first-action class (committed-action class,
  `e2.world_forward` strategy signature) and *(b)* placing the niche partition at the **eligible-set
  restriction** stage of `select()` (composed with `f_demotion`/`top_k`) rather than at the
  score-composition stage. No full merge; no id retired.
  MECH-294 is not a merge candidate with either.

- **(ii) contradictions / undercut premises.** One live undercut, and it runs 294 -> 442.
  MECH-442's dependency on MECH-294 is stated as needing the binding substrate "to route around F
  with". V3-EXQ-840b (2026-08-01) returned `weakens` on 294's joint clause. If that weakens stands,
  it does **not** undercut 442 -- what 442 needs is the *routing channel* (which demonstrably works:
  `route_range_per_arm_mean` JOINT 0.069 / ALT 0.057 / OFF+SHUF 0.0, `route_active_frac` 1.0), not
  the joint-vs-alternation content claim. So the dependency should be read/annotated as channel-only.
  No contradiction between 341 and 442; no contradiction between 341 and 294.
  Second, weaker tension: MECH-442's own load-bearing lit weakens (Ponzi 2007, `weakens`, conf 0.66)
  says the BG gate is a WTA that collapses to one action -- 442 already accommodates this by placing
  the archive upstream of the argmax, so this is a scoping constraint rather than a contradiction,
  and it is the same constraint `f_demotion`/`top_k` already satisfy.

- **(iii) shared falsifier.** **YES, and it already exists and must NOT be re-derived: ARC-065's
  `what_would_answer` "ARMED-CONVERSION" non-degeneracy precondition** (live in claims.yaml; already
  written to be cross-referenced by MECH-440/441, MECH-442's cluster siblings). Restated only for
  navigation, not for copying:
  - **(P1)** `support_preserving_min_first_action_classes = action_dim` (5), asserted from the
    MEASURED `mean_distinct_first_action_classes >= 0.9 * action_dim` (>= 4.5) **in every arm**. At
    the shipped default of 2 the pool realises ~2-3 classes of 5, so committed-class entropy is
    capped **identically in every arm** -- an arm-invariant ceiling no diversity lever can move.
  - **(P2)** `use_modulatory_selection_authority = True` with measured
    `authority_rel_deviation_mean > 0.05` in every arm carrying a modulatory lever.
  - Third leg: ARC-062 gated-policy heads + learned context discriminator ON in every arm.
  - Evidence that both are load-bearing and neither substitutes: V3-EXQ-949 (2026-08-25, 5 seeds)
    measured yoked committed-action divergence **0.000 with P1 alone, 0.000 with P2 alone, 0.3675
    with both**, at a measured pool diversity of 4.856 vs the 4.5 floor.
  - ARC-065's text is explicit: **"A null with either clamp in place is VACUOUS and must self-route
    `substrate_not_ready_requeue`, never `weakens`."**

  All three G6 claims read out on the *same statistic family* -- a distribution over first-action /
  committed-action classes at the E3 commit (entropy, or TV between arms) -- so this one precondition
  block is the correct shared text for all three, and each entry below points at it rather than
  restating it.

  **Second shared item (the pseudo-replication answer the brief asked for).** The de-duplication the
  memory `reference-hold-weighted-e3-readout-form2` warns about is already solved by a shared helper:
  `ree-v3/experiments/_lib/fresh_select.py` (`FreshSelectProbe` / `FreshSelectCounter`). It clears the
  E3 select diagnostics before every `select_action`, so a **latched (held) tick contributes NO row**,
  and emits `n_fresh_select` / `n_latched` / `fresh_select_yield` / `replication_factor` per cell.
  The established denominator floor is `nominal window ticks / beta_rate_max_steps=20` (the MECH-093
  worst-case cadence) -- V3-EXQ-840b used floor 180, measured 400. **Any falsifier in this group must
  state its candidate/selection counts on the fresh-select denominator and record
  `replication_factor`;** the raw per-tick count is ~9x pseudo-replicated (840b's own precondition
  text says so).

- **(iv) cross-cutting finding (the mutual confound).** **Every negative result currently on file for
  this group was measured under P1 at its default of 2 -- so a null on any one of them is
  uninterpretable until P1 is lifted.** Concretely: V3-EXQ-840b (MECH-294's only genuine experimental
  entry, and the sole basis for `exp_conf 0.249` and the `substrate_ceiling -> standard` category
  graduation) ran with `support_preserving_min_first_action_classes=2` (driver line 485) and measured
  `worst_diversity_joint = 2.0022` against its own local floor of 1.0 -- i.e. **2.0 of 5 classes**,
  versus ARC-065's ratified 4.5. MECH-341's three supporting runs (569d / 614a / 660) were all
  measured under the same clamp, which additionally means `stratified_select` was operating at its
  bare minimum (`min_classes_for_stratification = 2` against a pool realising exactly ~2 classes) --
  a preservation claim tested where there is almost nothing to preserve. And MECH-442, if built and
  tested today, would inherit the identical ceiling.
  Second cross-cutting item: **SD-105** (selection-entropy headroom floor, registered 2026-09-04,
  being digested elsewhere -- NOT digested here) is a **direct confound for any test in this group**:
  it is a one-sided integral controller that raises the E3 selection softmax temperature until
  realised normalised selection entropy sits at a floor. That *manufactures* the DV all three claims
  read out on. Any MECH-341/294/442 falisifier must either run SD-105 OFF, or hold it as a matched
  constant across arms **and record the controller's realised log-temperature per arm**; a
  floor-pinned readout also compresses the headroom an archive lift would have to move into (SD-105's
  own text makes exactly this argument about the R5 headroom gate).

- **Currency findings (verified this pass).**
  1. **`substrate_queue.json` -> `sd_id: MECH-341`** still reads
     `status: amend_validated_v3_exq_614c_614d_zero_committed_authority`, `ready: true`. That string
     predates 614e, 660, 660a/660b and the 2026-06-14 ratification. **Stale.**
     (`closure_status.md` line 59 is *correct* and current: `behavioral_diversity_isolation:GAP-B`
     -- "MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250)".)
  2. **`substrate_queue.json` -> `sd_id: mech294_coherence_magnitude_strengthening`** is still
     `ready: false` with a status string describing the **V3-EXQ-840** diagnosis. Its own
     `diagnosis_correction` (2026-07-31) concluded *"No ree_core substrate change is warranted...
     there is nothing to strengthen"*, and V3-EXQ-840b then ran and resolved the line on 2026-08-01.
     The entry has never been closed out, and its `recommended_next_step` (reconcile the confirmed
     autopsy artifact `failure_autopsy_batch-687a-...-2026-07-30.json`, whose "sub-floor
     cross-candidate range" claim does not match 840's own `per_arm_gate` data) appears unactioned.
     **Stale + an open reconcile.**
  3. **MECH-341 `status_note` cites `exp_conf 0.871 > 0.62` at the 2026-06-14 ratification.** The
     live index (`claim_evidence.v1.json`, generated 2026-09-04T14:48Z) now reads
     **`experimental_confidence 0.683`**, 3 supports : 0 weakens, `evidence_quadrant
     confirmed_established`, latest run V3-EXQ-660 (2026-06-10). Still clears the 0.62 gate, so the
     ratification stands, but the quoted figure is stale by ~0.19.
  4. **MECH-442's "not yet built" premise is stale** -- see preamble (2) and the MECH-442 entry.
  5. **The conversion-ceiling campaign has moved off the selection face.**
     `conversion_ceiling_campaign_plan.md` (7 nodes, 0% closed, all `assembling`): `:P-comp` RAN
     non_contributory; `:P2-rootC` RAN TERMINAL (715/715a/717 all FAIL, "selection-face lift RULED
     OUT, delta -63"); `:P4-learned-gating` **EXHAUSTED / retired**; `:FULLSTACK` RAN TERMINAL
     (V3-EXQ-714 readiness abort); `:CAMPAIGN` "converged on competence gate"
     (724 -> 732 -> 732a -> 737/738); `:GENERATION` (the missing 6th face, MECH-458) **blocked on
     upstream INV-088 z_world differentiation**. MECH-442 is **not** a face in that plan. This is
     directly consistent with [memory] `project_v3_binding_constraint_observation_interface`.
  6. **`claims.json` shows MECH-294 `awaiting: modulatory-bias-selection-authority`** -- that
     substrate is `implemented / ready: true` in `substrate_queue.json` and was consumed by 840b.
     Minor derived-field staleness; low priority.

---

### MECH-294 -- Theta-burst packet contains multi-content joint binding: each ~125 ms theta cycle binds a {goal_latent, action_proposal, risk_estimate, state_summary} tuple

**Recommended disposition:** **(a) testable now** -- the V3 leg has a validated driver and a landed
substrate lift (P1 raised to `action_dim`, proven necessary by V3-EXQ-947/949) that makes a
*non-vacuous* re-measurement of the exact 840b criteria buildable today; the current `weakens` was
measured under the clamp ARC-065's ratified precondition declares vacuous.

**Extracted from:** the claim's own `functional_restatement` "Falsifiable (primary)" / "Falsifiable
(secondary)" clauses, plus V3-EXQ-840b's pre-registered outcome map
(`evidence_direction_note`) and its `interpretation.preconditions` block -- turned into house
structure, not designed fresh. The non-degeneracy half is cross-referenced to ARC-065, not
re-derived.

**Currency check (what was verified, and where).**
- `ceiling_routing_note`'s "RESOLVED 2026-08-01 ... clean weakens, all readiness green" is
  **accurate as far as it goes**: `v3_exq_840b_..._20260801T120516Z_v3.json` shows
  `non_degenerate: true`, all 12 preconditions met, 10 seeds (42-51),
  `route_range_per_arm_mean` JOINT 0.06924 / ALT 0.057463 / OFF 0.0 / SHUF 0.0,
  C1 mean TV 0.087 with 3/10 seeds >= the 0.1 floor (7 required), C2 mean TV 0.1928 with 7/10.
- **But two things in that same manifest were not carried into the claim text.** (a) The driver's
  pass rule is a *conjunction*: `c1_pass = (seeds_above_floor >= 7) AND (mean_tv > baseline_tv)`
  (driver line 968-969), where `baseline_tv = _cross_seed_baseline_tv()` is documented in the driver
  as *"Mean pairwise within-arm cross-seed TV (**the noise band C1/C2 must exceed**)"*. Measured
  `cross_seed_baseline_tv = 0.7669`; `exceeds_baseline` is **false for BOTH C1 and C2**. So the
  claim's "C2 ... moot given C1" is imprecise -- **C2 independently failed its own baseline
  conjunct**, i.e. even the maximal JOINT-vs-SHUFFLED manipulation did not clear the design's own
  noise band, and the run therefore never demonstrated that *any* contrast in the design could
  produce a PASS. (b) The run used `support_preserving_min_first_action_classes=2` (driver line 485)
  and measured `worst_diversity_* = 2.0022` of `action_dim=5` -- ARC-065's P1 clamp at its default.
- `substrate_queue.json::mech294_coherence_magnitude_strengthening` is stale (`ready: false`,
  V3-EXQ-840-era status string) and its `recommended_next_step` reconcile of the 2026-07-30 batch
  autopsy is unactioned. Its `diagnosis_correction` conclusion ("no substrate change warranted") is
  sound and was borne out by 840b.
- Substrate confirmed present and default-OFF: `use_multi_content_theta_packet` (config.py:3306,
  `False`), `theta_packet_compose_per_candidate_coherence` (config.py:3340, `False`); module
  `ree_core/latent/multi_content_theta_packet.py`. Claim status `active`-adjacent but knobs
  default-off, per [memory] `reference-claim-status-vs-default-off-flag` -- so any arm must assert
  the knobs from measured per-arm quantities, not from the config, which 840b correctly did.

**epistemic_category (proposed):** `standard` -- **no change** (the 2026-08-01 graduation was the
right call on the information then available; the vacuity finding is raised as a governance flag for
adjudication, not applied unilaterally here). If governance accepts the flag, the correct move is to
re-adjudicate the 840b *entry* to `non_contributory / substrate_not_ready_requeue` and restore
`pending_retest_after_substrate: true`, **not** to move the category back to `substrate_ceiling` --
the ceiling this category once named (upstream range not routed) is genuinely resolved.

**Draft `what_would_answer`:**

> **SCOPE.** This claim is FUSED. Its PRIMARY falsifier is out-of-substrate for V3: joint
> multi-content decoding on hippocampal+amygdala+BG+ACC theta-resolved population recordings,
> showing whether semantically-distinct streams (goal vs risk vs state) are simultaneously decodable
> within one theta cycle, versus Kay et al. 2020's cross-cycle alternation. No such analysis is
> published; that leg resolves by literature/collaboration, not by REE (`evidence_quality_note` and
> `ceiling_routing_note` both already say so). What follows is the **REE leg only** -- the
> substrate-side joint-vs-alternation discriminator the 2026-04-26 governance hold named as
> route (a).
>
> **NON-DEGENERACY PRECONDITION.** Four conditions, all asserted from MEASURED per-arm quantities,
> never from config.
> (1) **The armed-conversion block: see ARC-065's own `what_would_answer` (P1 + P2 + the ARC-062
> gated-policy leg) -- do not re-derive it here.** P1 is the one V3-EXQ-840b did not have:
> `support_preserving_min_first_action_classes` must equal `action_dim`, with measured
> `mean_distinct_first_action_classes >= 0.9 * action_dim` (>= 4.5 of 5) **in every arm**. 840b ran
> at 2 and measured 2.0022, i.e. the committed-action distribution was capped at ~2 realised classes
> identically in all four arms, which bounds any between-arm TV by construction. A null measured
> under that clamp self-routes `substrate_not_ready_requeue`, never `weakens`.
> (2) **The 840b readiness block, retained verbatim in kind:** `joint_route_range_supra_floor`
> (JOINT routed per-candidate coherence cross-candidate RANGE > 0.01 on the 7th-largest per-seed
> value -- the SAME-STATISTIC safeguard against the V3-EXQ-661 rescale-invisible scalar null),
> `routed_range_bounded` (< 1e6, the 643a explosion ceiling),
> `adequate_committed_window_sample` (worst-cell `n_p1_ticks_past_window` >= 200 -- the precondition
> V3-EXQ-840 actually failed, per the corrected diagnosis in
> `substrate_queue.json::mech294_coherence_magnitude_strengthening.diagnosis_correction`).
> (3) **De-duplication, mandatory and explicit:** committed-action counts must be accumulated on the
> **fresh-select denominator** via `experiments/_lib/fresh_select.py` (diagnostics cleared before
> every `select_action`, so a latched/held tick contributes no row), with
> `adequate_fresh_selection_sample` >= `nominal_window_ticks / beta_rate_max_steps(20)` on the
> `MIN_SEEDS_FOR_PASS`-th largest per-seed value, and `n_latched` / `replication_factor` reported
> per cell. Raw per-tick accumulation is ~9x pseudo-replicated and voids the readout
> ([memory] `reference-hold-weighted-e3-readout-form2`).
> (4) **An instrument positive control on the DV itself, which 840b lacked.** A yoked
> same-arm-vs-same-arm control must diverge on 0 ticks (V3-EXQ-949's
> `paired_control_is_bit_identical`), AND at least one arm contrast in the design must be shown
> capable of exceeding `cross_seed_baseline_tv` -- otherwise the pre-registered pass rule
> (`mean_tv > baseline_tv`, driver line 968) is unsatisfiable by construction and a FAIL is a
> `measurement_test_design_defect`, not a claim verdict. In 840b `cross_seed_baseline_tv = 0.7669`
> and the largest observed contrast was 0.1928, so no arm cleared it.
> **SD-105 (selection-entropy headroom floor) must be OFF, or matched-constant across all arms with
> its realised log-temperature recorded per arm** -- an entropy controller acting on the E3 softmax
> directly manufactures this DV.
>
> **CONFIRMING.** On a pool with `mean_distinct_first_action_classes >= 4.5` and routed coherence
> supra-floor and mode-distinct (JOINT > ALT > SHUF ~ 0), the committed-action-class distribution
> under JOINT differs from ALTERNATION by mean paired TV **> max(0.1, cross_seed_baseline_tv)** on
> **>= 7/10 seeds** (C1), AND JOINT differs from SHUFFLED on the same bar (C2). Both must hold: C1
> alone with C2 failing is `multi_content_present_joint_not_isolated` -> `mixed`, and does NOT
> promote the joint clause. Effect-size gate scaled per [memory]
> `feedback_effect_size_pass_gate_margin`: the absolute floor 0.1 is retained as a floor, and the
> `cross_seed_baseline_tv` conjunct supplies the SD-of-the-delta half -- do NOT drop the baseline
> conjunct to make the test pass.
>
> **FALSIFYING.** With every precondition above met -- including P1 at >= 4.5 classes and a
> demonstrated capacity for some contrast to exceed the baseline -- JOINT remains
> indistinguishable from ALTERNATION on the committed-action distribution (C1 fail). That is the
> Kay-2020 parsimonious outcome: the joint-packet clause is over-specified at the
> behavioural-committed-action level this substrate can measure. It weakens the *joint* clause only;
> it does not touch MECH-089's theta-gamma multiplexing substrate, on which MECH-294 depends and
> which is separately lit-anchored (Lisman & Jensen 2013, Colgin 2009, Igarashi 2014).
> A **second** independent falsifying route, if the committed readout stays resolution-limited:
> per the claim's own "Falsifiable (secondary)", manipulate V_s anchor-eligibility so packet
> components differ in temporal vintage, and show that downstream consumers (E3 commit gate, dACC
> adaptive control) respond **no differently** to the component-typed packet than to a
> homogeneous-latent null on a readout upstream of the committed argmax (e.g. the routed
> cross-candidate range distribution, or the rank-order of the eligible set) -- a readout not
> subject to the class-count ceiling.

**Proposal sketch (for (a)):**
- **title:** `V3-EXQ-840c -- MECH-294 theta-packet joint-binding committed-action falsifier, ARMED-CONVERSION re-measurement (supersedes V3-EXQ-840b)`
- **related_claims:** `MECH-294` (primary), `ARC-065` (precondition owner), `MECH-089`, `MECH-269b`,
  `MECH-341` (the class definition the DV is built on)
- **acceptance_checks:**
  - R1 `support_preserving_min_first_action_classes = action_dim`; measured
    `mean_distinct_first_action_classes >= 4.5` in **all four** arms (ARC-065 P1).
  - R2 `use_modulatory_selection_authority = True`; measured `authority_rel_deviation_mean > 0.05`
    in all packet-ON arms (ARC-065 P2).
  - R3 the four 840b readiness preconditions unchanged (`routed_range_bounded`,
    `joint_route_range_supra_floor` 0.01, `candidate_first_action_diversity_supra_floor` -- floor
    RAISED from 1.0 to 4.5, `adequate_committed_window_sample` 200).
  - R4 fresh-select denominator + `n_latched` / `replication_factor` recorded per cell;
    `adequate_fresh_selection_sample >= 180`.
  - R5 yoked same-arm instrument control diverges on 0 ticks.
  - C1 JOINT vs ALT mean paired TV `> max(0.1, cross_seed_baseline_tv)` on >= 7/10 seeds.
  - C2 JOINT vs SHUF, same bar.
  - Outcome map unchanged from 840b (`joint_binding_behaviourally_load_bearing` -> supports;
    `multi_content_present_joint_not_isolated` -> mixed; `joint_indistinguishable_from_alternation`
    -> weakens; **any** readiness red -> `substrate_not_ready_requeue` / non_degenerate=false).
  - SD-105 OFF (or matched-constant with realised log-temperature recorded per arm).
  - Reuse the 840b driver and its OFF-arm fingerprint where eligible; the P1 change alters the arm
    fingerprint, so a fresh OFF-arm mint is expected -- emit it with
    `include_driver_script_in_hash=False` per the standing arm-reuse rule.
- **Sequencing note:** this is a *substrate-lift retest*, not a re-derive. 840b is one run and the
  re-run changes a clamp ARC-065's ratified precondition names as decisive; no re-derive brake
  applies. If governance prefers not to spend cloud time here (MECH-294 blocks no closure node),
  the honest fallback is disposition (f) with a `digestion_note` recording the P1 vacuity so the
  `weakens` is not read as stronger than it is.

**depends_on additions (if any):** none required. Optional annotation: MECH-294's own
`depends_on` is complete; it is MECH-442's inbound edge that needs the channel-vs-content
clarification (see MECH-442).

**GOVERNANCE FLAG:** `evidence_discrepancy` -- **V3-EXQ-840b, MECH-294's sole genuine experimental
entry (the `weakens` behind `exp_conf 0.249` and the 2026-08-01 `substrate_ceiling -> standard`
graduation), was measured under ARC-065's P1 clamp at its default of 2** (driver line 485;
`worst_diversity_* = 2.0022` of `action_dim=5`, vs ARC-065's required >= 4.5), and its own
pre-registered `mean_tv > cross_seed_baseline_tv` conjunct was **false for both C1 and C2**
(`cross_seed_baseline_tv = 0.7669`; largest contrast 0.1928). ARC-065's ratified
`what_would_answer` states that a null under either clamp "is VACUOUS and must self-route
`substrate_not_ready_requeue`, never `weakens`". The clamp's decisiveness was established by
V3-EXQ-947/949 (2026-08-25), i.e. **after** the 2026-08-01 autopsy -- so this is a
landed-result-vs-earlier-adjudication conflict, not an error by that autopsy. Requested adjudication:
(i) re-classify the 840b entry `weakens -> non_contributory / substrate_not_ready_requeue` on BOTH
the flat and the nested `runs/**/manifest.json` (per [memory]
`reference-indexer-reads-runs-pack-not-flat` -- the indexer scores the nested pack, and MECH-341's
own 660a incident is the precedent for this exact half-applied-reclassification bug), and restore
`pending_retest_after_substrate: true`; or (ii) retain the `weakens` with an explicit recorded
caveat. Either way the `standard` category should stay -- the original ceiling is genuinely resolved.

**GOVERNANCE FLAG:** `stale_note` -- `evidence/planning/substrate_queue.json` entry
`mech294_coherence_magnitude_strengthening` still carries `ready: false` and a V3-EXQ-840-era status
string, though its own `diagnosis_correction` (2026-07-31, session `confident-morse-af47a8`)
concluded no substrate change is warranted and V3-EXQ-840b then closed the line on 2026-08-01. Its
`recommended_next_step` -- reconcile the confirmed autopsy artifact
`failure_autopsy_batch-687a-707c-840-748a-833-842-810b-673-614-798afail_2026-07-30.json`, whose
"sub-floor cross-candidate range" finding contradicts the run's own `per_arm_gate` data
(measured 0.063841 vs floor 0.01, ~6x headroom) -- appears unactioned. Close the entry and reconcile
the autopsy.

---

### MECH-341 -- e3_scoring_preserves_trajectory_class_diversity. E3 score aggregation over CEM-supplied candidates must preserve trajectory-class diversity

**Recommended disposition:** **(a) testable now** -- the claim is ratified `provisional` at a scope
that was only ever measured with the candidate pool clamped to ~2 of 5 first-action classes, which is
the degenerate boundary of its own mechanism (`min_classes_for_stratification = 2`); the now-validated
raised-P1 substrate makes a genuinely non-degenerate test of the preservation assertion buildable
today, and it can fail.

**Extracted from:** the claim's `notes` ("Falsifier sequence: Phase P2 diagnostic... P3 substrate
work + B_only / ablate_B arms"), the `implementation_note`'s V3-EXQ-611/611b/611c acceptance
criteria (C1 `stratified_fired > 0`; C2 `entropy_bonus_max_abs >= 0.7 * scale`; C3
`selected_classes >= 2` with `frac_pre_ge2 >= 0.5`), the 2026-06-14 ratification's EXPLICIT CAVEAT
(scope = preservation, NOT committed-action conversion), and the 660b autopsy's retirement of the
graded-in-K falsifier as over-specifying a *preservation* claim. Nothing designed from a blank page;
the one genuinely new element is the raised-P1 arm, which comes from ARC-065 / V3-EXQ-947/949.

**Currency check (what was verified, and where).**
- **Substrate present and default-OFF, verified in code:** `use_e3_score_diversity` master
  (`ree_core/utils/config.py:4758`, `False`); module
  `ree_core/predictors/e3_score_diversity.py`; `apply_entropy_bonus` (line 165) and
  `stratified_select` (line 240) both present; `_first_action_classes` (line 143) is the sole
  definition of "trajectory class" = `int(first_step.argmax().item())`. `stratified_select` is
  consulted on BOTH the committed and uncommitted selection paths (2026-05-28 retune) and carries the
  2026-06-03 unit-range authority normalisation (`use_selection_authority` +
  `authority_min_range_floor`). Verified: the claim text is faithful to the code.
- **Evidence index (current):** `claim_evidence.v1.json` @2026-09-04T14:48Z --
  `experimental_confidence 0.683`, `genuine_exp_count 3`, **3 supports : 0 weakens**,
  `evidence_quadrant confirmed_established`, `pass_runs 3`, latest run
  `v3_exq_660_mech341_within_class_representative_diversity_20260610T044109Z_v3`. Status
  `provisional`, `v3_pending: false`, `pending_retest_after_substrate: false` -- all consistent with
  the 2026-06-14 ratification. **The `status_note`'s quoted `exp_conf 0.871` is stale (now 0.683);
  the ratification still clears the 0.62 gate, so no consequence beyond the number.**
- **Closure obligation: none open.** `closure_status.md` line 59 --
  `behavioral_diversity_isolation:GAP-B` records "MECH-341 STRAND CLOSED 2026-06-14 (ratified
  provisional, commit 80f4fcf250)".
- **Stale substrate_queue entry:** `sd_id: MECH-341` still reads
  `amend_validated_v3_exq_614c_614d_zero_committed_authority`, `ready: true` -- five months and four
  runs out of date. Flagged below.
- **The un-noticed clamp.** All three supporting runs (569d 2026-05-31, 614a 2026-05-30, 660
  2026-06-10) predate V3-EXQ-947/949 (2026-08-25) and were measured with
  `support_preserving_min_first_action_classes` at the shipped default of 2. Since
  `min_classes_for_stratification = 2`, the mechanism was tested at exactly the boundary where it
  first engages -- with a 2-class partition of a K-candidate pool, each "niche" is large, which is
  precisely the regime where the *within-class* representative lever (660's PASS,
  `within_class_rep_cond_entropy 4.862` vs legacy 4.781, a thin +0.08 nats against a 0.05 threshold)
  has the most room, and the *across-class* preservation assertion has almost none.

**epistemic_category (proposed):** `standard` -- **no change**. The claim has 3 clean supports, no
open ceiling, and its `pending_retest_after_substrate` is correctly `false` (the committed-action
conversion is explicitly NOT a MECH-341 retest, per the ratification note and the inline comment at
claims.yaml:64964). The proposed run below is a *strengthening/robustness* test of an already-
provisional claim, not a ceiling retest.

**Draft `what_would_answer`:**

> **SCOPE, ratified 2026-06-14 and load-bearing for reading this falsifier.** MECH-341 asserts
> **scoring-layer PRESERVATION** -- that E3 score aggregation does not collapse an upstream-diverse
> candidate pool onto a single deterministic ranking. It does **NOT** assert that the preserved
> diversity reaches the COMMITTED action; that conversion is the shared E3 selection-authority
> ceiling tracked on `behavioral_diversity_isolation:GAP-A` / MECH-439 F-dominance, and is MECH-442's
> territory, not this claim's. A flat committed-action-class entropy is therefore **not** evidence
> against MECH-341 (614e and 660 both showed byte-identical committed-class entropy while MECH-341
> passed). Two falsifier shapes are additionally RETIRED and must not be resurrected:
> (a) **graded-in-K dose-response** -- retired by confirmed `failure_autopsy_V3-EXQ-660b_2026-06-11`
> because a graded response over-specifies a binary preserve-or-collapse claim (three convergent
> iterations 660 / 660a / 660b; no 660c); (b) **in-isolation clearance via the
> `entropy_bias_scale` lever** -- V3-EXQ-616 proved mathematically that a uniform additive bias
> cannot move a single-class CEM proposer output (bit-identical across scales 1/2/4/8), so the
> B_only arm's structural bound sits at the *proposer* layer (SP-CEM presence), not the score-layer
> knob. MECH-341 is a preserver, never an in-isolation generator.
>
> **NON-DEGENERACY PRECONDITION.**
> (1) **There must be something to preserve, and this is the condition every run to date missed.**
> Measured `mean_distinct_first_action_classes` in the PRE-scoring candidate pool must be
> `>= 0.9 * action_dim` (>= 4.5 of 5), i.e. `support_preserving_min_first_action_classes` raised to
> `action_dim` -- **see ARC-065's own `what_would_answer` (P1) for the full statement and the
> V3-EXQ-949 evidence; do not re-derive it here.** At the shipped default of 2 the pool realises
> ~2-3 classes and `min_classes_for_stratification = 2` is only just satisfied, so a "preservation"
> verdict is measured at the mechanism's degenerate boundary.
> (2) The substrate must be OPERATIVE and measured as such, not assumed from config
> (`use_e3_score_diversity` and both sub-flags default `False`): `n_stratified_fired > 0` on every
> ON arm and every seed (the V3-EXQ-611 C1 criterion -- 611's ARM_2 recorded
> `n_stratified_fired = 0` across all seeds and that FAIL was a wiring artefact, not a claim result),
> and `entropy_bonus_max_abs` non-trivial relative to the observed `mean_top2_class_gap` (the 611c
> C2 lesson: `lambda = 0.05` produced a 0.045 bonus against gaps of 0.27-1.96 and was inert; the
> defaults are now `lambda = 0.5`, `bias_scale = 1.0`).
> (3) **De-duplication:** the pre/post class counts and the within-class representative entropy must
> be accumulated on the **fresh-select denominator** (`experiments/_lib/fresh_select.py` -- select
> diagnostics cleared before every `select_action`, latched ticks contribute no row), with
> `n_fresh_select`, `n_latched` and `replication_factor` reported per cell. A held/latched E3 decision
> re-counted per tick inflates every class count by the hold factor (~9x) and is the standing
> hold-weighted readout hazard.
> (4) SD-105 (selection-entropy headroom floor) OFF or matched-constant with realised log-temperature
> recorded per arm.
>
> **CONFIRMING.** On a pool with measured `mean_distinct_first_action_classes >= 4.5`: the number of
> distinct first-action classes SURVIVING the E3 scoring step (post-score, pre-commit) is
> strict-above the same quantity with `use_e3_score_diversity = False`, on >= 2/3 seeds; and the
> established within-class-representative readout `H(rep_signature | committed_class)` (the 660
> corrected readout mandated by the 614e autopsy's Learning #2 -- **not** committed-class entropy)
> remains strict-above legacy-argmin by a margin exceeding both an absolute floor and the
> cross-seed SD of the delta. The already-established instance at the clamped pool is 660:
> 4.862 vs 4.781 nats, +0.081 against a 0.05 threshold -- **note this margin is thin and its
> SD-scaled robustness was never established**, which is part of what the raised-P1 arm would test.
>
> **FALSIFYING.** Two distinct routes, either sufficient.
> (i) **Collapse at a genuinely diverse pool:** with `mean_distinct_first_action_classes >= 4.5`
> upstream and the substrate measured operative, the post-scoring distinct-class count does NOT
> exceed the `use_e3_score_diversity = False` control (the diverse pool is collapsed by scoring
> regardless of the preserver) -- MECH-341's preservation assertion fails exactly where it should
> bite hardest. (ii) **Boundary artefact:** the 660 within-class-representative lift does not
> replicate at the raised pool -- at ~4.9 classes the niches are small (often singletons, where
> `stratified_select`'s own code short-circuits to argmin: `len(class_idxs) < 2`), so a +0.08 nats
> effect that vanishes when niches shrink would indicate the ratified result was an artefact of the
> 2-class clamp rather than a property of the preserver. Either outcome is a genuine weakening and
> would put the 2026-06-14 ratification back in front of governance.

**Proposal sketch (for (a)):**
- **title:** `V3-EXQ-660c -- MECH-341 scoring-layer class-diversity preservation at an ARMED (raised-P1) candidate pool`
  (note: the retired "660c" label was for the *graded-in-K* successor, which stays retired; if the
  collision is judged confusing, mint a fresh number rather than a letter -- flagging it here rather
  than deciding it, per the EXQ versioning policy's "when in doubt, new number".)
- **related_claims:** `MECH-341` (primary), `ARC-065` (precondition owner + parent pathway),
  `MECH-442` (consumer of the preserved diversity -- reads the same class statistic downstream),
  `INV-076`, `MECH-257`
- **acceptance_checks:**
  - R1 measured `mean_distinct_first_action_classes >= 4.5` (of 5) in **every** arm, pre-scoring.
  - R2 `n_stratified_fired > 0` on every ON arm and seed; `entropy_bonus_max_abs` recorded against
    the measured `mean_top2_class_gap`.
  - R3 fresh-select denominator; `n_latched` / `replication_factor` per cell.
  - R4 `use_e3_score_diversity = False` control arm, bit-identical baseline asserted from the
    substrate hash.
  - C1 post-scoring distinct-class count strict-above the OFF control on >= 2/3 seeds.
  - C2 `H(rep_signature | committed_class)` lift over legacy-argmin exceeding
    `max(absolute_floor, k * SD(delta))` -- i.e. re-run 660's C2 with an SD-scaled gate rather than
    the bare 0.05 that the original cleared by 0.031.
  - Negative control (declare explicitly, so a null is interpretable): committed-CLASS entropy is
    expected to stay flat -- it is the EXPECTED negative control per the 660 interpretation grid,
    NOT a gate, and must not be read as a MECH-341 failure.
  - Arms: 2x2 over {P1 clamp 2, P1 clamp `action_dim`} x {`use_e3_score_diversity` OFF, ON} so the
    clamp's own contribution is dissociated from the preserver's.
- **Value if it PASSES:** converts MECH-341's supports from "stack-only / single-pathway"
  (`narrow_supports_flag`, recorded 2026-06-11 and still standing) to a result established at a
  non-degenerate pool, which is the outstanding condition on any future promotion above
  `provisional`.

**depends_on additions (if any):** consider adding **`ARC-065` is already present**; no new edges
needed. Worth recording in the claim text (not as an edge): the raised-P1 dependency is on
`support_preserving_min_first_action_classes`, i.e. on SP-CEM / ARC-065 GAP-A, which the claim
already depends on.

**GOVERNANCE FLAG:** `stale_note` -- `evidence/planning/substrate_queue.json` entry `sd_id: MECH-341`
still reads `status: amend_validated_v3_exq_614c_614d_zero_committed_authority`, `ready: true`,
describing a state superseded by V3-EXQ-614e (2026-06-07), V3-EXQ-660 (2026-06-10), the 660a/660b
reclassifications (2026-06-11) and the 2026-06-14 ratification that closed
`behavioral_diversity_isolation:GAP-B` for this claim. Update or close the entry. Separately,
MECH-341's own `status_note` quotes `exp_conf 0.871` where the live index now reads 0.683 -- the
ratification still stands (gate 0.62) but the figure should be corrected or dated when the note is
next touched.

---

### MECH-442 -- Committed-action diversity survives the selection/commit step via a behavioral-descriptor eligible-set ARCHIVE (Quality-Diversity / MAP-Elites analog)

**Recommended disposition:** **(f) defer, with a durable `digestion_note`** -- the claim's mechanism
is substantially already built (under MECH-341 and MECH-448, unnoticed by its 2026-06-18
registration), its genuine residual is a descriptor generalisation whose test is currently
unmeasurable for the same P1 reason as the rest of the group, and the whole conversion-ceiling
campaign has RUN TERMINAL on the selection face and re-routed upstream to generation/competence. It
has fan-in 0 and blocks no closure node. **What must be resolved first, specifically:** (1) ARC-065's
P1+P2 armed-conversion clamps lifted and held in every arm; (2) the `:GENERATION` face
(MECH-458 / ARC-065 rarity-seeking) unblocked from INV-088 z_world differentiation; (3) governance
adjudication of the partial-absorption proposal below, which determines whether there is a distinct
claim left to test at all.

**Extracted from:** the claim's own `notes` FALSIFIER clause (verbatim: *"if a
behavioral-descriptor-indexed committed-selection archive does NOT lift committed-action-class
entropy strict-above BOTH collapsed-proposer and matched-noise on >=2/3 seeds BEYOND the
descriptor-free top-k shortlist (V3-EXQ-569i), OR lifts it only by selecting F-dominated/unsafe
actions past the per-niche-elite bound..."*) and its pre-registered 2x2 discriminator. Turned into
house structure, with the non-degeneracy half cross-referenced (not re-derived) to ARC-065 and the
comparator set corrected for what has been built since 2026-06-18.

**Currency check (what was verified, and where).**
- **`substrate_conditional` is correct as a category, but the "not yet built" premise is
  materially stale.** `MECH-341::E3ScoreDiversity.stratified_select`
  (`ree-v3/ree_core/predictors/e3_score_diversity.py:240-330`) is, by its own docstring,
  *"1. Partition candidates by first-action class. 2. Per class, pick the argmin-score candidate as
  class representative. 3. Sample across class representatives with
  `softmax(-best_in_class_score / stratified_temperature)`."* That is a behavioural-descriptor
  partition, a per-niche F-best elite, and a coverage-aware commit rule -- MECH-442's mechanism, with
  the descriptor pinned to first-action class. It runs on the committed path and is validated
  (V3-EXQ-611c C1/C3, 614d/614e C3 readiness, 660 PASS). MECH-442's notes never mention this module.
- **The eligible-set half is also built, and by more than top-k.** `e3_selector.py:3751-3765`:
  MECH-448 / ARC-107 `shortlist_mode == "f_demotion"` builds a rank-preserving divisive-normalisation
  **F-eligibility envelope** (F decides eligibility only; F is then REMOVED from the within-eligible
  argmin), and it **takes precedence over** `margin` / `top_k`. `top_k` itself has since gained a
  conflict-graded k (`modulatory_shortlist_conflict_graded`, `k = clamp(round(k_max -
  (k_max-1)*gap_norm), 1, K)`). MECH-448 is `candidate` with a `what_would_answer` already drafted;
  MECH-449 is `provisional` / `shown`. So MECH-442's stated comparator ("BEYOND the descriptor-free
  top-k shortlist, V3-EXQ-569i") is **out of date**: the route of record is now the MECH-448
  demotion + MECH-449 Go/No-Go stack.
- **The campaign has moved off this face.** `evidence/planning/conversion_ceiling_campaign_plan.md`
  (7 nodes, 0% closed): `:P-comp` RAN non_contributory (699, precondition_unmet, "no build owed");
  `:P2-rootC` RAN TERMINAL (715/715a/717 all FAIL -- *"selection-face lift RULED OUT, delta -63"*);
  `:P4-learned-gating` **EXHAUSTED / retired**; `:FULLSTACK` RAN TERMINAL (V3-EXQ-714 readiness
  abort, C2 never scored); `:CAMPAIGN` *"converged on competence gate"* (724 -> 732 -> 732a ->
  737/738); `:GENERATION` (MECH-458) **blocked on upstream INV-088**. MECH-442 is not a face.
  `substrate_queue.json::f_dominance_conversion_ceiling` records
  `selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD`
  via MECH-448/449 (V3-EXQ-689g PASS, promoted provisional 2026-06-22) -- **four days after MECH-442
  was registered**, with `GAP_A_lift_generalisation_NOT_yet_demonstrated` and `PROMOTES_NOTHING`.
- **Evidence:** `claim_evidence.v1.json` -- `genuine_exp_count 0`, `exp_conf 0.0`, 5 literature
  entries (4 supports / 1 weakens = Ponzi 2007, conf 0.66), `lit_conf 0.756`,
  `evidence_quadrant plausible_unproven`. Fan-in **0** (nothing depends on MECH-442). No manifest
  under `evidence/experiments/` references MECH-442 outside derived indexes.
- **No archive code exists:** grep for `map_elites` / `behavioral_descriptor` / `behavioural_descriptor`
  / `niche` across `ree-v3/ree_core/` and `ree-v3/experiments/_lib/` returns nothing relevant (the
  only `niche` hits are ecological niches in `causal_grid_world.py`). So the *descriptor-general*
  archive genuinely does not exist -- which is what keeps `substrate_conditional` correct.
- `ceiling_decision: deferred` / `ceiling_routing_note` ("DO NOT build in V3 until routed by
  experiment") is **still accurate and should be retained**.

**epistemic_category (proposed):** `substrate_conditional` -- **no change.** The descriptor-general
archive has never been built or exercised, so `substrate_ceiling` (built AND exercised, downstream
mechanism absorbs the signal) does not apply; the existing `live_status.reading:
candidate/substrate_conditional` marker was checked and is correct.

**Draft `what_would_answer`:**

> **PRECEDENCE NOTE (read before designing any run).** Three things already instantiate parts of
> this claim, and a falsifier that ignores them tests nothing new:
> (a) **`MECH-341::stratified_select`** is already a descriptor-indexed per-niche-elite archive with
> a coverage-aware commit rule, for `descriptor = first-action class`;
> (b) **`MECH-448` `f_demotion`** (e3_selector.py:3757) is already an eligible-set restriction
> upstream of the argmax with F removed from the within-eligible arbitration -- and it takes
> precedence over `top_k`;
> (c) **`MECH-449`** Go/No-Go constitution is the validated partner (V3-EXQ-689g PASS).
> The comparator in this claim's registered FALSIFIER ("BEYOND the descriptor-free top-k shortlist,
> V3-EXQ-569i") is therefore **superseded**: the baseline arm must be the MECH-448 demotion +
> MECH-449 stack (the conversion route of record), not 569i top-k. **MECH-442's remaining testable
> residual is exactly two things:** (i) a descriptor OTHER than first-action class -- specifically
> the `e2.world_forward` strategy signature or the realised committed-action class -- and (ii) niche
> partitioning placed at the **eligible-set restriction** stage of `E3TrajectorySelector.select`
> (composed with `f_demotion`), rather than at MECH-341's score-composition stage.
>
> **NON-DEGENERACY PRECONDITION.** **See ARC-065's own `what_would_answer` ARMED-CONVERSION block
> (P1 + P2 + the ARC-062 gated-policy leg) -- MECH-440 and MECH-441 already cross-reference that
> text and this claim does the same; do not re-derive it.** Two additions specific to this claim:
> (3) **The descriptor must be non-degenerate independently of the class ceiling.** The realised
> number of occupied NICHES per tick, on the proposed descriptor, must be measured `>= 3` and must
> exceed the number of first-action classes -- otherwise the "generalised" descriptor is a relabelling
> of MECH-341's existing partition and the arm is a duplicate of a built mechanism, not a test of a
> new one. Report niche-occupancy histograms per arm.
> (4) **De-duplication is mandatory and must be stated in the driver**: committed-action counts and
> niche-occupancy counts on the **fresh-select denominator**
> (`ree-v3/experiments/_lib/fresh_select.py` -- diagnostics cleared before every `select_action`, so
> a latched tick contributes no row), with `n_fresh_select >= nominal_window_ticks /
> beta_rate_max_steps(20)`, and `n_latched` / `replication_factor` emitted per cell. Without this the
> "committed-action-class entropy" DV is inflated ~9x by held decisions and every arm difference is
> an artefact of differing hold durations -- a real hazard here because a coverage-aware commit rule
> *changes hold duration by design*.
> (5) **SD-105 (selection-entropy headroom floor) must be OFF, or matched-constant across arms with
> its realised log-temperature recorded per arm.** SD-105 is a one-sided integral controller that
> raises the E3 selection temperature until realised normalised selection entropy hits a floor --
> i.e. it directly manufactures this claim's DV, and if it is pinning the floor it also compresses
> the headroom an archive lift would have to move into. A MECH-442 result measured with SD-105 live
> and unrecorded is uninterpretable in either direction.
>
> **CONFIRMING.** On an armed pool (>= 4.5 of 5 first-action classes, authority ON, gated policy ON),
> in the pre-registered **2x2 (F-de-collapse) x (behavioural-descriptor archive vs the MECH-448/449
> route of record)** ablation under the C+D composite: the descriptor-archive arm lifts
> committed-action-class entropy **strict-above** BOTH the collapsed-proposer control AND the
> matched-noise control on **>= 2/3 seeds**, AND strict-above the MECH-448/449 baseline arm by a
> margin exceeding both an absolute floor and the cross-seed SD of the delta, **WITHOUT** a
> per-niche F-quality regression: no committed action may exceed the per-niche-elite F bound, and no
> harmful action class may be globally disinhibited (the Ponzi-2007 safety constraint that motivates
> keeping the archive upstream of the argmax; the same safety guard MECH-448's own
> `what_would_answer` states).
>
> **FALSIFYING.** Either (i) the descriptor archive does NOT lift committed-action-class entropy
> beyond the MECH-448/449 baseline on >= 2/3 seeds with all preconditions met -- the behavioural
> descriptor earns no keep over F-rank eligibility restriction, and the fix is rebalancing F's E3
> variance share directly (MECH-439); or (ii) it lifts entropy only by admitting candidates past the
> per-niche-elite F bound or by disinhibiting a harmful class -- a quality/safety regression, which
> under Ponzi 2007 is the predicted failure of putting niching too close to the commit. Note the
> asymmetry deliberately: a NULL here is only informative once ARC-065's P1 is lifted; under the
> default clamp a null self-routes `substrate_not_ready_requeue`.

**Proposal sketch:** *not applicable* -- disposition is (f), no experiment proposed. The design above
is recorded so it is ready to queue if and when the deferral conditions clear. If governance instead
wants to act now, the cheapest informative step is **not** a build: it is the **partial-absorption
adjudication** below, which may show there is no distinct claim left to build.

**Proposed `digestion_note` (durable, for the claim block):**
> Digested 2026-09-04 (`/thought-digestion v3-closure`, G6). DEFERRED, not orphaned; category stays
> `substrate_conditional`; `ceiling_decision: deferred` and the "DO NOT build in V3 until routed by
> experiment" note both stand. Three specific conditions must resolve before this is queueable:
> (1) ARC-065's ARMED-CONVERSION P1 (`support_preserving_min_first_action_classes = action_dim`,
> measured >= 0.9*action_dim per arm) and P2 (`use_modulatory_selection_authority`, measured
> `authority_rel_deviation_mean > 0.05`) both held in every arm -- V3-EXQ-949 (2026-08-25) measured
> yoked committed divergence 0.000 / 0.000 / 0.3675 for P1-only / P2-only / both;
> (2) the `conversion_ceiling_campaign:GENERATION` face (MECH-458) unblocked from INV-088 z_world
> differentiation -- every other face of that campaign has RUN TERMINAL and the selection-face lift
> is recorded RULED OUT (`:P2-rootC`, delta -63);
> (3) governance adjudication of the partial-absorption finding: MECH-341's built
> `E3ScoreDiversity.stratified_select` already implements descriptor-partition + per-niche F-best
> elite + coverage-aware commit for `descriptor = first-action class`, and MECH-448's built
> `f_demotion` envelope already implements eligible-set restriction upstream of the argmax with F
> removed from within-eligible arbitration. The residual unbuilt content of MECH-442 is (a) a
> descriptor other than first-action class (`e2.world_forward` strategy signature / committed-action
> class) and (b) niche partitioning at the eligible-set stage rather than the score-composition
> stage. The registered comparator "beyond the descriptor-free top-k shortlist (V3-EXQ-569i)" is
> superseded by the MECH-448/449 conversion route of record (V3-EXQ-689g PASS, 2026-06-22).

**depends_on additions (if any):**
- **Add `MECH-448`** (and optionally `MECH-449`) -- the F-eligibility-demotion envelope is now the
  baseline this claim must beat, and is the built instance of "eligible-set restriction upstream of
  the argmax". Its absence from `depends_on` is why the stale top-k comparator survived.
- **Annotate `MECH-294`** (do not remove): the dependency is on the *modulatory channel routing*
  (`modulatory_channel_route_source`, cross-candidate route range -- demonstrably functional:
  JOINT 0.069 / ALT 0.057 / OFF+SHUF 0.0 in V3-EXQ-840b), **not** on MECH-294's joint-binding
  content clause, which V3-EXQ-840b returned `weakens` on. As written, the edge comment invites the
  wrong inference.
- No change to `MECH-341` / `MECH-439` / `ARC-065` / `ARC-062` edges.

**GOVERNANCE FLAG:** `contested_disposition` -- **PARTIAL-ABSORPTION PROPOSAL (proposal only; no id
retired, nothing deleted).**
- **Survivors:** `MECH-341` (in-group) and `MECH-448` (out-of-group, already BUILT). **Absorbed
  (partially):** `MECH-442`.
- **What text moves:** MECH-442's mechanism description -- "partitions the eligible candidate set by
  a behavioral descriptor ... and retains the F-best candidate WITHIN each behavioral niche, then
  commits by a coverage-aware rule" -- is already realised by
  `E3ScoreDiversity.stratified_select` (partition by first-action class -> argmin within class ->
  softmax across class representatives, with unit-range authority normalisation), and its
  "eligible-set restriction UPSTREAM of the winner-take-all commit, F unchanged at the argmax" half
  is already realised by MECH-448's `f_demotion` envelope. MECH-442's Cully/Mouret/Pugh literature
  anchors and the Ponzi-2007 upstream-placement constraint should be **copied** (not moved) onto
  MECH-341's and MECH-448's blocks as external-analog grounding, since they are the strongest
  available theoretical justification for machinery those claims already own.
- **Narrowed residual retained under MECH-442** (this is a partial absorption, not supersession):
  *"committed-action diversity is better preserved by a niche partition on a descriptor OTHER than
  first-action class -- specifically the `e2.world_forward` strategy signature or the realised
  committed-action class -- and by placing that partition at the eligible-set restriction stage of
  `E3TrajectorySelector.select` (composed with `f_demotion`) rather than at MECH-341's
  score-composition stage."* Title and notes to be narrowed accordingly.
- **Reverse-deps needing repointing: NONE** -- MECH-442 has **fan-in 0** (verified against the full
  registry: no claim lists it in `depends_on`). This is a clean absorption with no downstream
  breakage, which is unusual and is the main reason it is worth doing rather than leaving the
  overlap latent.
- **Why raise it rather than act:** MECH-442 is a convergence-intake claim (CDQ-003 /
  CPKT-QUALITY-DIVERSITY-20260618) whose value is partly as a record that the external QD/MAP-Elites
  frame was evaluated against REE. Narrowing it preserves that record while removing the false
  implication that its mechanism is unbuilt. Digestion proposes; governance decides.

**GOVERNANCE FLAG:** `stale_note` -- MECH-442's `notes` assert *"substrate_conditional on a
behavioral-descriptor eligible-set archive beyond top-k not yet built"* and name V3-EXQ-569i top-k as
the comparator. Both were true on 2026-06-18 and are not true now: (a) a descriptor-indexed
per-niche-elite archive with a coverage-aware commit rule IS built (`stratified_select`, under
MECH-341, validated through V3-EXQ-660); (b) the conversion route of record is MECH-448 demotion +
MECH-449 Go/No-Go (V3-EXQ-689g PASS, 2026-06-22, four days after registration), not 569i top-k; and
(c) `top_k` itself has since gained conflict-graded width. The claim's `ceiling_routing_note` and
`ceiling_decision: deferred` remain correct and should be kept.

> **Orchestrator correction (2026-09-04T21:18:57Z):** the G5 dispatch prompt said ARC-120/ARC-121 were registered from the 2026-08-27 developmental-integration intake; the G5 agent verified they were registered 2026-08-06 from `docs/thoughts/2026-08-06_scientific_evolution_of_ree.md`. The grouping edge (same namespace + title overlap) stands; the source attribution in the prompt was wrong.

---

<!-- G8 appended 2026-09-04T21:22:55Z -->
## G8 -- dopamine / RBF density / curiosity drive  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the assigned rationale is the
  `depends_on` lattice plus shared hippocampal-module namespace (SD-024 <-> SD-025 = 7.25;
  ARC-057 <-> SD-025 = 6.00). That is correct but understates the relation. These three are
  **one mechanism cut at three levels**: SD-024 is the PRODUCER (DA writes extra RBF centres into
  `benefit_rbf_field`), SD-025 is the CONSUMER (CEM trajectory scoring reads
  `density * (1 - familiarity)` off that same field), and ARC-057 is the assertion that the
  PRODUCT of those two -- and only the product -- yields approach behaviour, with no valence
  gradient anywhere. They are not the same claim (the 768a single-drive arms separate them
  cleanly: SD-024-alone margin 0.0, SD-025-alone-on-a-flat-map -0.01, both-on 14.53), but they
  share a single failure surface: **if the producer writes nothing, all three read zero, and no
  amount of consumer-side tuning can tell you so.** That is not hypothetical -- it is the
  confirmed 2026-07-20 defect, and (finding 8 below) it is live again right now in the entire
  fishtank experiment family.

- **(i) same-claim / merge candidates:** **No merge recommended, in-group or out.** Justification,
  since the merge pressure is real enough to need one:
  - *SD-024 vs SD-025* are producer/consumer and are experimentally dissociable: V3-EXQ-768a's 2x2
    already measured each alone at ~0 and only the conjunction at 14.53, and V3-EXQ-900 tested
    SD-024's allocation mechanism with **no CEM/selection step anywhere in the design** (its own
    `dv_symmetry_note`). Two claims that a run has already dissociated must not be merged.
  - *ARC-057 vs {SD-024, SD-025}* is a level distinction, not a granularity duplicate: ARC-057's
    content is the *super-additivity* plus the negative ("no explicit approach gradient is
    required"), which is exactly what the C4 weight-zeroing control in 768a and the L2c control in
    766 test and which neither design_decision asserts.
  - *External merge pressure checked and REJECTED: MECH-314a (structured-curiosity striatal
    novelty).* This is the closest already-BUILT sibling and it looked like a duplicate on the
    name. It is not. Verified in `ree-v3/ree_core/policy/structured_curiosity.py:829-870`:
    MECH-314a reads `residue_field.rbf_field` (the **harm/main** field) and scores
    *minimum distance to the nearest active centre* -- an inverse-distance NOVELTY term, integrated
    into E3's `dacc_score_bias` in `select_action()`. SD-025 reads `benefit_rbf_field` via
    `compute_representational_density` and scores **density**, integrated into the hippocampal
    `_score_trajectory` CEM path. Different field, opposite polarity on "density", different
    integration site. Merging them would destroy a real dissociation.
    **But this pair deserves a governance note in its own right** (flagged below): REE now carries
    two independently-flagged curiosity channels reading two different RBF fields at two different
    scoring sites, and nothing in the registry states how they compose or whether they double-count.
    That question is unowned.

- **(ii) contradictions / undercut premises:** one real contradiction, internal to SD-025.
  SD-025's `notes` assert two functional properties that **MECH-458 (registered 2026-07-17, the
  curiosity=exploitation-amplifier reframe) has since measured to be substantially weaker than the
  text claims**:
  1. *"The familiarity component (visit-count EMA) prevents the agent from endlessly circling
     already-explored regions"* -- MECH-458's force decomposition of the identical V3-EXQ-767a data
     puts the familiarity discount at its **ceiling** (after 12 forced visits) at 20.4 against a
     density-attraction force of 39.3 (1.93x weaker), and at **exactly 0.00 at the decision
     point**, because familiarity starts at zero. So the brake is not "prevents"; it is a lagging,
     reactive, roughly-half-strength discount that contributes nothing to the first move.
  2. The title's *"information-seeking bias"* framing. MECH-458 establishes the drive has
     **zero proactive pull toward unshaped / under-represented regions** and is 100% parasitic on
     prior DA shaping (768a flat-map arm = 0). In the Bellemare-2016 sense of information-seeking
     (bonus HIGH for low-count states) SD-025's polarity is **inverted**. The mechanism is
     accurately described by the rest of SD-025's text ("favors regions of higher representational
     density"); it is the word *information-seeking*, and the anti-perseveration sentence, that are
     now known to over-claim.
  ARC-057 is **not** contradicted by MECH-458 -- MECH-458 explicitly scopes itself to the diversity
  side and says ARC-057 (approach side) is correct there. But ARC-057's `notes` inherit the same
  framing ("The curiosity/exploration drive seeks information gain (novel or unexplored
  representational structure)"), which is the sentence MECH-458 refutes. Recommended as a
  `stale_note`, not a demotion: nothing about the *approach* result changes.

- **(iii) shared falsifier:** yes, and it is the single most useful output of this pass.
  **All three claims share one non-degeneracy precondition, and it is currently the binding
  constraint on the whole group: the SD-024 live producer must be ON and the resulting
  curiosity bonus must vary ACROSS CANDIDATES.** Concretely:
  `residue.benefit_terrain_live_producer = True` AND `hippocampal.curiosity_weight > 0` AND a
  per-run `curiosity_bonus_range` (max-min across CEM candidates, not the mean) strictly greater
  than zero. `agent.py:11570` is the **sole** caller of `ResidueField.accumulate_benefit` anywhere
  in `ree_core/` (verified by grep this session), it is gated on that flag, and the flag defaults
  to `False`. With it off, `compute_local_density` early-returns zeros on an empty active mask,
  `_curiosity_bonus` returns exactly 0.0, and every arm of every ablation is bit-identical.
  SD-025's and ARC-057's drafts below **cross-reference SD-024's precondition text rather than
  re-deriving it**, per brief rule 6.

- **(iv) cross-cutting finding (the mutual confound):** **the group's entire positive evidence base
  is IN VITRO, and the two live-path runs that exist show the SD-024 -> SD-025 handoff is roughly
  three orders of magnitude weaker in vivo than in the diagnostic geometry.** Measured, not
  inferred:
  - V3-EXQ-795 (live, `benefit_terrain_live_producer=True`, `curiosity_weight=0.5`,
    `da_allocation_scale=4.0`): the argmin-relevant statistic, cross-candidate range of the
    curiosity bonus, `curiosity_bonus_range_mean_on = 0.01767` (per-seed 0.01361 / 0.02503 /
    0.01438; SD 0.00521). The run's **own hand-built positive control**, on the same statistic and
    the same weight, read **13.83**. Ratio ~780x. 795 PASSed because its floor `L4A_RANGE_FLOOR`
    is `1e-9` -- it asked "is this non-zero", not "is this big enough to move a selection".
  - V3-EXQ-900 (live, `benefit_terrain_live_producer=True`, `da_allocation_scale=40.0` -- ten times
    795's): only **6 of 57** live benefit events allocated a cluster of size >= 2;
    `mean_cluster_size = 1.316`. And `mean_benefit_magnitude` was essentially identical at
    cluster>=2 (0.5577) and cluster==1 (0.5582), so the discriminator in vivo is **`drive_level`,
    not benefit magnitude** -- the DA signal is `benefit_exposure * drive_level` and drive_level is
    what rarely gets high enough.
  The confound this creates is symmetric and must be stated on every proposal in this group:
  **a null on ARC-057's live-path interaction is uninterpretable unless SD-024's live expansion
  RATE is pinned in the same run**, because "no interaction" and "the producer only fired 6 times
  in 57 opportunities" are indistinguishable from the outcome metric alone. Conversely a live
  SD-025 null is uninterpretable without the cross-candidate range. Every draft below therefore
  makes the *rate* and the *range* preconditions, not findings.

- **Currency findings (all verified this session; each names the file checked):**
  1. **STALE / already done.** SD-024's `implementation_note` says *"substrate_queue.json SD-024
     depends_on_unresolved should drop SD-004 (implemented) and MECH-232"*. Checked
     `REE_assembly/evidence/planning/substrate_queue.json`: SD-024's entry now reads
     `"depends_on_unresolved": []`. Note can be retired.
  2. **STALE / already done.** SD-025's `implementation_note` says *"substrate_queue.json SD-025
     depends_on_unresolved still lists SD-024 (now implemented) -- drop it"*. Checked: SD-025's
     entry now reads `["ARC-057", "MECH-111", "INV-051"]` -- SD-024 already dropped.
  3. **STALE.** SD-024's `implementation_note` calls the `depends_on: MECH-232` *"a circular/stale
     gate (MECH-232 is candidate...)"*. `docs/assets/data/claims.json`: **MECH-232 is now
     `status: stable`, `epistemic_stance: shown`, `assembly_state: mature`.** The dependency is
     resolved, not circular; the sentence describes a state that no longer obtains.
  4. **STALE, and materially so.** `substrate_queue.json` SD-024 carries
     `"validation_experiment": "PENDING -- live-path efficacy (producer ON vs OFF), not yet
     queued"`. It **ran**: `v3_exq_795_sd024_benefit_terrain_live_path_efficacy_20260720T235007Z_v3`
     -- outcome PASS, `evidence_direction: supports`, `experiment_purpose: diagnostic`,
     `non_degenerate: true`, machine `ree-cloud-2`, 3 seeds, and it **is** in
     `review_tracker.json.reviewed_run_ids`. The queue entry has been wrong since 2026-07-20.
  5. **STALE by ~9 hours.** SD-025's 2026-07-20 SUBSTRATE note says *"What they do not establish --
     and what nothing yet establishes -- is LIVE-PATH efficacy"*. V3-EXQ-795 started
     2026-07-20T23:45Z, i.e. the same day, and establishes exactly that (in the weak "non-zero"
     sense; see the (iv) caveat, which is the sentence that should replace it).
  6. **PROMOTION CANDIDATE, unflagged.** `v3_exq_900_sd024_da_cluster_allocation_representational_functional_20260808T103846Z_v3`
     is `experiment_purpose: **evidence**` (not diagnostic), PASS, supports, reviewed, and is
     SD-024's *first confidence-bearing experimental result*. `claim_evidence.v1.json` now gives
     SD-024 `experimental_confidence 0.715`, `evidence_quadrant confirmed_established`,
     `genuine_exp_count 1`, `pass_runs 1`, `fail_runs 0`; `claims.json` already carries
     `epistemic_stance: shown`. **SD-024's `status` is still `candidate` and its `live_status.as_of`
     is still `2026-07-11`** -- i.e. the live_status predates both live runs. Flagged below.
  7. **STALE.** `docs/assets/data/claims.json` SD-025 carries `"awaiting": "SD-024"`. SD-024 has
     been implemented since 2026-07-16 and live-wired since 2026-07-20.
  8. **NEW DEFECT, same class as the one that was fixed.** Ten fishtank-family manifests
     (`v3_exq_906/906a/906b/906c/909/911/912/913/920 x2`) set `use_da_modulated_rbf_density: true`
     **and** `curiosity_weight: 0.05`, and **none of them sets `benefit_terrain_live_producer`**
     (grep count 0 in every manifest, and 0 in all **16** fishtank driver scripts under
     `ree-v3/experiments/*fishtank*.py`). None of those drivers calls `accumulate_benefit`
     directly either. Since `agent.py:11570` is the sole producer and the flag defaults `False`,
     **the SD-025 curiosity bonus is identically 0.0 in every fishtank run from 2026-08-09 through
     at least 2026-08-14**, despite the config reading as though curiosity is on. Flagged below.
  9. **PARTIALLY done.** `arc_057_ecological_env_decision_2026-07-16.md` sec 7 asks that
     `substrate_queue.json` SD-025 gain `status: implemented` / `node_class` (**done** -- both now
     present) and that its `depends_on_unresolved` be *annotated* as an env/claim gate on the
     ecological Test C rather than a gate on the built substrate (**not done** -- the list is
     still bare).
  10. **No duplication.** `ree-v3/experiment_queue.json` currently holds **3** items, none touching
      this group. `TASK_CHIPS.json` (3023 chips) contains only two SD-025 hits, both `done`
      telemetry chips from 2026-08-10. `governance_flags.v1.json` (8 flags) contains **no** flag
      for ARC-057 / SD-024 / SD-025 / MECH-458. Every proposal and flag below is new.

---

### ARC-057 -- Approach behavior toward reward locations emerges from the interaction of DA-mediated re...

**Recommended disposition:** **(a) testable now** -- the ecological form is correctly V4-deferred,
but the *live-path* form of the 2x2 interaction is buildable today on flags that already exist and
have already been demonstrated to work (795, 900), and it is the one arm that would convert
ARC-057's provisional reading from an in-vitro geometry result into an in-vivo one.

**Extracted from:** the claim's own `notes` -- the paragraph beginning *"Testable: ablate DA
modulation of hippocampal resolution while preserving the curiosity drive... Neither alone
sufficient"* -- re-operationalised onto the statistic V3-EXQ-768a already validated (continuous CEM
score-margin, replacing the saturating argmin gate that made V3-EXQ-768 vacuous), and onto the live
path V3-EXQ-795 opened. Sub-prediction (3) in the same `notes` (extinction when DA modulation
ceases) supplies the second arm. Nothing here is invented from a blank page.

**Currency check:**
- V3-EXQ-768a manifest (`..._20260717T064620Z_v3.json`) confirmed present and in
  `review_tracker.json.reviewed_run_ids`; it is the run that moved ARC-057 candidate -> provisional.
- `claim_evidence.v1.json` ARC-057: `experimental_confidence 0.0`, `genuine_exp_count 0`,
  `pass_runs 0`, `evidence_quadrant plausible_unproven`, `literature_confidence 0.732` from 3
  `lit:computational_model` entries. **ARC-057's `provisional` rests on a diagnostic-purpose run
  (excluded from confidence scoring by design) plus literature -- it carries zero experimental
  confidence.** That is not an error; it is the documented consequence of "the promotion is the
  gate-clearing action, not a confidence increment". It is worth stating because it bounds how much
  the current status can be leaned on.
- Ecological Test C: `arc_057_ecological_env_decision_2026-07-16.md` sec 6 -- DECISION RECORDED,
  deferred to V4, co-blocked on the conversion / F-dominance ceiling. **Still current**; nothing in
  `substrate_queue.json` or the queue has re-opened it.
- Both mechanisms verified BUILT and DEFAULT-OFF in `ree-v3/ree_core/`:
  `utils/config.py:3041 use_da_modulated_rbf_density = False`, `:3045 da_allocation_scale = 0.0`,
  `:3002 benefit_terrain_live_producer = False`, `:2521 curiosity_weight = 0.0`. So the brief's
  "check whether they are BUILT and default-on" resolves to **built, all four knobs default-off** --
  the claim's non-degeneracy precondition is a config assertion, not an assumption.

**epistemic_category (proposed):** `substrate_coherence` (keep the value inferred from
`claim_type: architectural_commitment`; do not set an explicit override).
*Why not `substrate_ceiling`:* per the sharpened discriminator in `REE_assembly/CLAUDE.md`, a
ceiling requires the mechanism to have been *exercised repeatedly under non-degenerate conditions*
with a downstream mechanism absorbing the signal. The live-path 2x2 has been run **zero** times;
768a/767a/766 all populate the terrain from the driver script. There is no absorption evidence, so
"ceiling" would be a guess. *Why not `substrate_conditional`:* the code exists and works
(795 L1a/L2a/L3a/L4a all green, 900 C1/C2/C4 all green), which is exactly what
`substrate_conditional` denies. The env-constrained **ecological** leg (Test C) *is*
substrate-conditional, but it is a scoped sub-claim, not ARC-057 entire -- flagged in the draft
rather than re-categorising the claim.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (three parts; the run is vacuous without all three).
> (1) **Live producer, not driver-populated terrain.** `residue.benefit_terrain_live_producer=True`
> and the driver must NEVER call `ResidueField.accumulate_benefit` outside a declared positive
> control. This is the precondition SD-024's own `what_would_answer` states; see it and do not
> re-derive. Every prior ARC-057 run (766 / 767 / 767a / 768 / 768a) populated the terrain from the
> driver and therefore tested the mechanism, not the agent.
> (2) **Producer actually fired at a measurable rate.** Report `n_benefit_events`,
> `n_expansion_events` (cluster_size >= 2) and `mean_cluster_size` per arm. Floor:
> `n_expansion_events >= 5` pooled (V3-EXQ-900's own floor, met there at 6). Below that floor the
> both-ON arm is not distinguishable from the SD-025-alone arm and the 2x2 is uninterpretable --
> this is the group's mutual confound, and it must be a gate, not a post-hoc note.
> (3) **The selection statistic varies across candidates and across seeds.** The load-bearing
> statistic is the CONTINUOUS CEM score-margin (768a's re-operationalisation; the binary argmin
> gate that saturated at exactly 1.0 with zero cross-seed variance is what made V3-EXQ-768 vacuous
> and MUST NOT be reintroduced). Require non-zero cross-seed variance on the both-ON margin and a
> non-zero cross-candidate range on the curiosity bonus (V3-EXQ-795's L4a statistic).
>
> CONFIRMING. A 2x2 ablation (both-OFF / DA-ON+curiosity-OFF / DA-OFF+curiosity-ON /
> both-ON) run end-to-end through `REEAgent` on a real `CausalGridWorldV2` episode loop with the
> live producer, at >= 8 seeds, supports ARC-057 iff **all four** hold:
> - **C1 (super-additivity, the claim itself):** `margin(both-ON) - margin(DA-only) -
>   margin(curiosity-only) + margin(both-OFF)` exceeds `max(3 x SD_seed(that contrast), 1.0)`, where
>   `SD_seed` is the cross-seed SD of the interaction contrast. The absolute floor of 1.0 is
>   inherited from 768a's C1 (which measured 14.37 in vitro); the SD-scaled term is what makes the
>   gate meaningful at the far smaller in-vivo effect sizes measured in 795.
> - **C2 (neither alone):** each single-drive arm's margin is within `1 x SD_seed` of the both-OFF
>   arm. In vitro 768a read 0.0 and -0.01; a live run reading materially above zero on a single arm
>   is itself informative and must not be waved through.
> - **C3 (no valence gradient -- ARC-057's negative half):** repeat the both-ON arm with all benefit
>   WEIGHTS zeroed while leaving centre POSITIONS intact (768a's C4 weight-zeroing control, and 766's
>   L2c). The margin must be statistically indistinguishable from the unzeroed both-ON arm. If
>   zeroing the value collapses the margin, approach was riding value, not density, and ARC-057's
>   central negative claim fails regardless of C1.
> - **C4 (extinction, ARC-057 notes sub-prediction 3):** after a maintained both-ON phase, remove
>   the reward contingency (DA modulation ceases; FIFO centre lifecycle overwrites the cluster) and
>   show the approach margin decays toward the both-OFF level over a bounded number of episodes.
>   This is the arm that discriminates *"there is more map"* from *"a gradient was installed"*: a
>   gradient account predicts persistence, the expansion account predicts decay.
>
> FALSIFYING. Any of:
> (a) the interaction contrast fails C1 **while precondition (2) is met at a healthy expansion
> rate** -- i.e. the producer demonstrably fired and the conjunction still bought nothing over the
> single arms. This is the direct refutation.
> (b) C3 fails -- weight-zeroing collapses the margin -- which refutes "no explicit approach
> gradient is required" even if C1 passes.
> (c) a single-drive arm alone produces the full margin (C2 fails), which would make ARC-057 an
> additive claim about one drive, not an interaction claim.
> **NOT falsifying, and this is the trap this claim has already fallen into twice:** a null with
> `n_expansion_events < 5`, a null with zero cross-seed variance on the load-bearing statistic, or a
> null read off a driver-populated terrain. Those are `measurement_degeneracy` (the V3-EXQ-768 and
> V3-EXQ-767 verdict), not evidence, and must route to re-operationalisation rather than to
> ARC-057's confidence.
>
> SCOPE BOUND, stated so a future reader does not over-read a PASS. This falsifier addresses the
> INTERNAL (SD-024-workaround) form of ARC-057 on the live path. It does **not** address the
> ECOLOGICAL form -- approach emerging where the *environment itself* carries location-dependent
> information density -- which `arc_057_ecological_env_decision_2026-07-16.md` sec 6 defers to V4,
> co-blocked on conversion-ceiling closure. That leg alone is `substrate_conditional`. It also does
> not bear on strategy-diversity GENERATION, which MECH-458 scopes out explicitly.

**Proposal sketch:**
- **title:** `ARC-057 live-path DA-expansion x curiosity interaction: does the 768a super-additivity
  survive when the benefit terrain is built by the agent's own reward contacts?`
- **related_claims:** `ARC-057` (primary), `SD-024`, `SD-025`, `MECH-232`, `ARC-007`
  (weight-independence / no-valence-gradient), `MECH-094` (replay must not expand),
  `MECH-233` (harm asymmetry, C4 control in 900).
- **acceptance_checks:** `benefit_terrain_live_producer=True` and driver contains no bare
  `accumulate_benefit` call outside the declared positive control; `n_expansion_events >= 5` pooled;
  load-bearing statistic is the continuous CEM score-margin with non-zero cross-seed variance and
  non-zero cross-candidate range; >= 8 seeds; all four arms of the 2x2 present plus the C3
  weight-zeroed replicate and the C4 extinction phase; cloud machine class
  (`linux-x86_64-py3.10-torch2.12.0+cpu`) -- per the cross-machine multinomial-divergence rule the
  DV must be asserted upstream of any discrete quantizer, which the continuous margin already is;
  `experiment_purpose: evidence` (not `diagnostic`) if the intent is to move ARC-057's currently-zero
  experimental confidence rather than only to clear a gate.
- **Sequencing note:** should run AFTER, or jointly with, SD-024's live-expansion-rate proposal
  below. Running it first risks a null that precondition (2) cannot adjudicate. A single driver
  emitting both readouts is the cheaper resolution and is what I would recommend.

**depends_on additions:** none. Current `[MECH-232, ARC-007, SD-004]` is correct and now fully
resolved upstream (MECH-232 stable, ARC-007 provisional/shown, SD-004 implemented). Note that
**SD-024 and SD-025 are named in the title but are NOT in `depends_on`** -- ARC-057 depends on
MECH-232 (the mechanism) rather than SD-024 (the design decision implementing it). That is defensible
and I do not recommend changing it, but a reader tracing the lattice will not find SD-024/SD-025 from
ARC-057; SD-025 -> ARC-057 exists in the reverse direction only.

**GOVERNANCE FLAG:** `stale_note` -- ARC-057's `notes` open with *"The curiosity/exploration drive
seeks information gain (novel or unexplored representational structure)"*. MECH-458 (candidate,
registered 2026-07-17, anchored on 767a + 768a) establishes the drive has **zero** proactive pull
toward unexplored/unshaped structure and is 100% parasitic on prior DA shaping. The ARC-057 *result*
is untouched (MECH-458 says so in terms), but this sentence in ARC-057's own notes now states the
opposite of a measured finding registered in the same registry. Recommend a one-line amendment
pointing at MECH-458, not a status change.

---

### SD-024 -- DA-modulated RBF center density: dopaminergic signal at reward encounters allocates m...

**Recommended disposition:** **(a) testable now** -- and note that the *core* falsifier has already
been run and passed (V3-EXQ-900, evidence-purpose); what remains testable-now is the quantitative
residual that the live runs surfaced (the expansion RATE), which is also ARC-057's blocking
precondition. This claim is closer to promotion than its `candidate` status suggests -- see the flag.

**Extracted from:** the claim's own `notes` (the parameter list `da_allocation_scale`,
`da_jitter_radius`, `num_centers`; the MECH-233 harm-asymmetry constraint; the MECH-094 replay gate;
the three named informative failure modes craving / anhedonia / perseveration) **plus** the criteria
V3-EXQ-900 actually instantiated (C1 `rho(da, cluster_size)`, C2 `rho(cluster_size, density)`,
C4 harm-never-clusters). The draft below turns the already-run design into the standing falsifier and
adds the one gate 900 did not have.

**Currency check:**
- `substrate_queue.json` SD-024: `status: implemented_pending_validation`,
  `depends_on_unresolved: []`, `node_class: complicated (buildable)`,
  `validation_experiment: "PENDING -- live-path efficacy (producer ON vs OFF), not yet queued"`.
  **That last field is stale** -- V3-EXQ-795 ran 2026-07-20 and is reviewed (currency finding 4).
- `claim_evidence.v1.json` SD-024: `experimental_confidence 0.715`,
  `evidence_quadrant confirmed_established`, `genuine_exp_count 1`, `pass_runs 1`, `fail_runs 0`,
  `latest_run_id v3_exq_900_...20260808T103846Z_v3`, `literature_confidence 0.694` over 5 lit
  entries (4 electrophysiology, 1 computational; direction counts 3 supports / 2 mixed / 1 weakens).
- `claims.json` SD-024: `epistemic_stance: shown`, `status: candidate`,
  `assembly_state: remaining`.
- Code verified: `residue/field.py:466-469` reads `use_da_modulated_rbf_density` (default False) and
  `da_allocation_scale` (default 0.0); `field.py:709-736` is `add_residue_cluster`;
  `agent.py:11560-11576` is the sole live producer, gated on `benefit_terrain_live_producer`
  (default False) with `benefit_live_producer_threshold` 0.1, passing
  `dopamine_signal = benefit_exposure * drive_level`, and deliberately placed BEFORE the
  `goal_state` guard.
- Lit caveat worth carrying: the Retailleau & Morris 2018 entry in `claim_evidence.v1.json`
  (conf 0.75, supports) records that the perseveration phenotype there arises from **D1
  blockade**, whereas SD-024's `notes` predict perseveration from **DA locked high** -- the entry
  itself says *"The claim's failure-mode taxonomy may have the sign inverted"*. That is a live,
  unresolved discrepancy inside SD-024's own evidence set and it is reflected in the draft below.

**epistemic_category (proposed):** `standard` (the value inferred from
`claim_type: design_decision`; no explicit override needed). It is V3-tractable, the substrate is
built, and it has a green evidence-purpose run -- exactly the `standard` dispatch.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION. The DA -> cluster-size relation must be measured through the **real
> substrate call path**, not by constructing clusters in the test, and the live sample must carry
> rank information:
> (1) A P0 readiness sweep over a well-separated `DA_SWEEP` (e.g. 0.0 -> 1.0 in 0.2 steps) at
> synthetic locations must yield `rho(da, cluster_size) >= 0.9` and
> `rho(cluster_size, density) >= 0.9`. This certifies the instrument before any live claim is read.
> (2) The LIVE sample must contain `n_expansion_events` (events allocating cluster_size >= 2)
> `>= 5` pooled across seeds. **A live sample in which every event allocated the same cluster size
> carries no rank information and a correlation over it is vacuous** -- this is the precondition,
> and V3-EXQ-900 met it only barely (6 events out of 57 benefit events, at
> `da_allocation_scale=40.0`).
> (3) `benefit_terrain_live_producer=True` with no direct `accumulate_benefit` call in the driver
> outside a declared control -- `agent.py:11570` must be the writer. This is the shared group
> precondition; ARC-057's and SD-025's falsifiers point here rather than restating it.
>
> CONFIRMING (mechanism -- **already satisfied by V3-EXQ-900, 2026-08-08, PASS/supports**; retained
> as the standing falsifier).
> - **C1:** over live benefit events, `rho(dopamine_signal, allocated cluster_size) >= 0.3`.
>   *(measured 0.533)*
> - **C2:** `rho(cluster_size, weight-independent density readout) >= 0.3`. *(measured 0.517)*
> - **C4 (MECH-233 asymmetry):** across **every** live harm event, zero cluster allocations on the
>   harm/threat terrain. *(measured: 0 of 1403)*
> - **C5 (MECH-094 gate):** a replay/simulation-tagged event allocates zero expansion. Enforced in
>   code at `field.py:665` and asserted at the `agent.py` call site; must be re-asserted in any run
>   that exercises replay.
>
> CONFIRMING (the RESIDUAL, not yet tested, and the part that matters downstream). SD-024 as written
> asserts expansion happens *"at reward encounters"* -- unqualified. The live data says it happens
> at a **small minority** of them. A dose-response arm sweeping `da_allocation_scale` and, separately,
> `drive_level`, supports the claim in its downstream-usable form iff the **expansion FRACTION**
> (`n_expansion_events / n_benefit_events`) rises monotonically with DA and reaches a regime where
> the resulting cross-candidate curiosity-bonus range exceeds `max(3 x SD_seed, 0.05)` -- where
> `SD_seed = 0.0052` and the observed live range was `0.0177` in V3-EXQ-795 against a
> same-statistic positive control of `13.83`. Pin `drive_level` explicitly: V3-EXQ-900 measured
> `mean_benefit_magnitude` at cluster>=2 (0.5577) and at cluster==1 (0.5582) as effectively
> identical, so **benefit magnitude is not the discriminator in vivo and `drive_level` is the
> untested lever**.
>
> FALSIFYING.
> - `rho(da, cluster_size)` at or below zero on a live sample meeting precondition (2) -- the
>   allocation rule does not track DA in the live agent.
> - Any live harm event allocating a cluster (refutes the MECH-233 asymmetry the claim explicitly
>   preserves, and would invalidate the SD-024 workaround's central selectivity argument).
> - A replay-tagged event allocating expansion (refutes the MECH-094 gate).
> - **Residual-specific:** the expansion fraction stays flat, or the achievable cross-candidate
>   range stays at the ~0.018 order, across the full sweep of `da_allocation_scale` and
>   `drive_level`. That would not refute SD-024's *mechanism* -- C1/C2 would still hold -- but it
>   would establish that the mechanism cannot reach a magnitude the downstream consumer can use,
>   and **that finding would convert the SD-024 -> SD-025 handoff to `substrate_ceiling`**
>   (built, exercised, non-degenerate, signal absorbed downstream), which is precisely the
>   discriminator `REE_assembly/CLAUDE.md` sets out. Say so in the run's interpretation rather than
>   recording a bare PASS on C1/C2.
> - **Lit-side counterexample to watch (does not by itself refute):** SD-024's `notes` predict
>   perseveration from DA locked HIGH; the Retailleau & Morris 2018 entry in
>   `claim_evidence.v1.json` records perseveration from D1 **blockade**. Per the lit/exp decoupling
>   rule this is non-load-bearing for the claim's status, but the failure-mode taxonomy in `notes`
>   should be reconciled or explicitly scoped rather than left carrying a possible sign inversion.

**Proposal sketch:**
- **title:** `SD-024 live DA-expansion dose-response: does expansion FRACTION and the resulting
  cross-candidate curiosity range scale with da_allocation_scale and drive_level?`
- **related_claims:** `SD-024` (primary), `MECH-232`, `SD-025` (the consumer whose range is the
  downstream DV), `ARC-057` (whose precondition (2) this discharges), `MECH-233`, `MECH-094`,
  `SD-012` (the phasic-DA scaling rule `benefit_magnitude * drive_level`).
- **acceptance_checks:** P0 sweep `rho >= 0.9` on both legs; `n_expansion_events >= 5` per sweep
  cell (not just pooled -- 900's pooled-only floor is what makes its 6/57 hard to read);
  `benefit_terrain_live_producer=True` and no driver-side `accumulate_benefit`; report expansion
  FRACTION per cell, not only counts; report `curiosity_bonus_range` (max-min across candidates) as
  a co-primary DV; `drive_level` swept as an independent axis from `da_allocation_scale`;
  `experiment_purpose: evidence`; cloud machine class; >= 3 seeds per cell (900 used 3; more if the
  fraction is noisy).
- **Reuse note:** V3-EXQ-900's OFF/low-DA cells are the natural baseline; its arms were fingerprinted
  (`arm_fp/v1`, `substrate_hash` recorded). Check
  `reanalysis_query.py --claim SD-024` before queueing -- 900's own `notes` record that at
  2026-08-08 the only prior manifest was 795 and reanalysis was not possible, but 900 itself is now
  bankable and the dose axis may be partly recoverable from its `readiness_sweep`.

**depends_on additions:** none required. Current `[SD-004, SD-014, MECH-232]` is now fully resolved
(SD-004 implemented, MECH-232 **stable**, SD-014 candidate/gated_v3). The `implementation_note`
sentence calling MECH-232 a "circular/stale gate" should be retired -- see currency finding 3.

**GOVERNANCE FLAG (two, separable):**
1. `promotion_review` -- **SD-024 is `status: candidate` while carrying
   `experimental_confidence 0.715`, `evidence_quadrant confirmed_established`,
   `epistemic_stance: shown`, one reviewed evidence-purpose PASS (V3-EXQ-900, 2026-08-08) and one
   reviewed diagnostic PASS (V3-EXQ-795), zero conflicting runs.** Its `live_status.as_of` is
   `2026-07-11`, i.e. it predates both live runs and the whole implementation. This is a promotion
   candidate that has never been put in front of a governance cycle. Recommend `/governance` read
   V3-EXQ-900 against SD-024 and either promote or record why not; digestion does not promote.
2. `stale_note` -- `substrate_queue.json` SD-024
   `validation_experiment: "PENDING -- live-path efficacy (producer ON vs OFF), not yet queued"` is
   contradicted by a landed, reviewed, PASSing run (V3-EXQ-795, 2026-07-20). Same field's
   `status: implemented_pending_validation` should be re-read in light of V3-EXQ-900 being
   evidence-purpose. Also in this bucket: SD-024's `implementation_note` MECH-232-is-circular
   sentence (MECH-232 is now `stable`), and the two "NOTE for governance ... depends_on_unresolved
   should drop" instructions in SD-024 and SD-025, both of which have **already been carried out**
   in `substrate_queue.json` and now read as outstanding work that isn't.

---

### SD-025 -- Curiosity drive: information-seeking bias in hippocampal trajectory scoring that favo...

**Recommended disposition:** **(a) testable now** -- the drive's *propagation* is validated in vitro
(767a) and its *live non-zero-ness* is validated (795), but **the question SD-025 has never been
asked is whether the live bonus is large enough to change a committed action**, and that is
V3-tractable today on existing flags. I considered (f) defer-with-digestion_note and reject it: the
blocking fact is measured, the instrument exists, and the run is cheap.

**Extracted from:** SD-025's own `notes` final line -- *"Test: ARC-057 requires BOTH SD-024 and
SD-025 active. Neither alone should produce significant approach behavior (interaction effect, not
additive)"* -- which is ARC-057's test, not SD-025's; and from the drive-mechanism criteria
V3-EXQ-767a already instantiated (L1a propagation margin, L1c weight-independence, L2a familiarity
anti-perseveration, L2b MECH-094 replay control). Per brief rule 6, the interaction half is
**cross-referenced to ARC-057's draft above and deliberately not re-derived here**; what follows is
the SD-025-specific residual: consequentiality of the drive on the live path.

**Currency check:**
- **SD-025 has ZERO confidence-bearing experimental evidence.** `claim_evidence.v1.json`:
  `experimental_confidence 0.0`, `genuine_exp_count 0`, `pass_runs 0`,
  `evidence_quadrant plausible_unproven`, `literature_confidence 0.782` over 3 lit entries
  (fmri_connectivity, mouse_behavior_calcium_imaging, theoretical_review), latest entry
  `2026-08-01_sd_025_mouse_ofc_information_value_bussell2026`. V3-EXQ-767 / 767a / 795 are all
  `experiment_purpose: diagnostic` and excluded from confidence scoring by design.
- The 2026-07-20 SUBSTRATE note's closing sentence -- *"what nothing yet establishes -- is LIVE-PATH
  efficacy"* -- is **superseded the same day** by V3-EXQ-795 (PASS, L3a live bonus non-zero, L4a
  cross-candidate range non-zero). It should be amended rather than left standing.
- **But 795 establishes far less than "efficacy" reads.** Its floors are
  `L3A_BONUS_FLOOR = 1e-9` and `L4A_RANGE_FLOOR = 1e-9`. The measured live cross-candidate range was
  `0.01767` (SD 0.00521 over 3 seeds) against the run's own same-statistic positive control of
  `13.83`. **"Live-path efficacious" in that manifest means "not identically zero", and should not
  be read as "moves selection".**
- `claims.json` SD-025 carries `"awaiting": "SD-024"` -- stale since 2026-07-16/20.
- `substrate_queue.json` SD-025: `status: implemented`, `node_class: complicated (buildable)`,
  `ready: false`, `design_doc: null`, `depends_on_unresolved: ["ARC-057","MECH-111","INV-051"]`.
  The `design_doc: null` is wrong -- the design lives at
  `docs/architecture/sd_024_da_modulated_rbf_density.md#curiosity-drive`, which is exactly SD-025's
  own `location`. And per `arc_057_ecological_env_decision_2026-07-16.md` sec 7 the
  `depends_on_unresolved` list should be annotated as a gate on the ecological **Test C**, not on
  the built substrate -- still not done.
- Code verified: `hippocampal/module.py:140` builds `FamiliarityTracker` only when
  `curiosity_weight > 0.0`; `:1704-1731` `_curiosity_bonus` computes
  `cw * mean(density * (1 - familiarity))`; `utils/config.py:2521 curiosity_weight = 0.0`,
  `:2541 familiarity_bandwidth = 0.20` (the 1.0 -> 0.20 move recorded in the notes **has landed**).
- **New defect, currency finding 8:** ten fishtank manifests and sixteen fishtank drivers set
  `curiosity_weight: 0.05` and `use_da_modulated_rbf_density: true` but never
  `benefit_terrain_live_producer`. `agent.py:11570` is the sole producer in `ree_core/` (grep-verified
  this session) and the flag defaults False, so **the SD-025 bonus is identically 0.0 across the
  entire 906/909/911/912/913/920 family** -- a config that reads as "curiosity on" and is not.

**epistemic_category (proposed):** `standard` (inferred from `claim_type: design_decision`; no
explicit override). *Why not `substrate_ceiling` yet:* the mechanism is built and has been exercised,
but only once on the live path and never with an outcome/behavioural DV downstream of it -- so
"something downstream absorbs the signal" is currently a hypothesis, not a repeated observation.
The proposal below is precisely the run that would license the `substrate_ceiling` re-tag; see its
FALSIFYING clause.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION. **See SD-024's `what_would_answer` precondition -- do not
> re-derive it.** SD-025 is the consumer of SD-024's product and inherits its preconditions
> wholesale: live producer on, driver never calls `accumulate_benefit`, `n_expansion_events >= 5`.
> Two SD-025-specific additions:
> (1) `curiosity_weight > 0` AND the `FamiliarityTracker` actually constructed
> (`module.py:140` -- at `curiosity_weight = 0.0` the tracker is never built and every ablation is
> bit-identical, which is a silent no-op, not a null).
> (2) **The argmin-relevant statistic must be the cross-candidate RANGE of the bonus, never its
> mean.** `_curiosity_bonus` returns a scalar per candidate trajectory; a component common to all
> candidates is inert in the CEM selection and cancels. Report `max-min across candidates` per
> decision and require it strictly non-zero. V3-EXQ-795 already routes on this statistic (its L4a,
> and the V3-EXQ-643 correction it cites); a design that reports only
> `curiosity_bonus_abs_mean` reproduces the V3-EXQ-604c broadcast-scalar failure mode.
> (3) **Do not let a saturating binary preference gate be load-bearing.** V3-EXQ-767's single
> load-bearing gate `L1a_pref_A_on` pinned at exactly 1.0 on all 8 seeds and the run was adjudicated
> vacuous; 767a's continuous CEM score-margin is the sanctioned replacement. Any SD-025 gate must
> carry non-zero cross-seed variance.
>
> CONFIRMING (mechanism -- **already satisfied in vitro by V3-EXQ-767a, 2026-07-17,
> adjudicated REAL/non-vacuous**; retained as the standing falsifier).
> - **L1a propagation:** the curiosity term produces a non-zero continuous CEM score-margin
>   `min(sparse) - min(dense)` favouring the denser region. *(measured 39.26, range 26.95-45.61
>   over 8 seeds)*
> - **L1c weight-independence (ARC-007-strict):** zeroing the benefit VALUE while leaving centre
>   positions intact leaves the margin unchanged (`<= 0.1`). *(measured 0.0)* This is what makes it a
>   representational-density drive rather than a disguised value gradient, and it is SD-025's single
>   most distinctive property.
> - **L2a familiarity anti-perseveration** and **L2b MECH-094 replay control** (replay must not raise
>   familiarity). *(measured 20.05 and 0.0)*
>
> CONFIRMING (the RESIDUAL, and the actual open question). SD-025 supports its downstream role iff,
> on a LIVE run with a behavioural outcome DV, the curiosity term **changes committed action**:
> a same-seed, same-substrate `curiosity_weight` ON/OFF contrast must yield a non-zero
> **committed-action divergence rate** (fraction of decisions where the selected candidate differs
> between arms) exceeding `max(3 x SD_seed, 0.02)`, with the cross-candidate bonus range reported
> alongside as the mechanistic explanation of whatever is observed. Anchor for calibration: the live
> range measured in V3-EXQ-795 is `0.0177` (SD `0.0052`, n=3 seeds) against a hand-built positive
> control of `13.83` on the same statistic -- so the design must sweep `curiosity_weight` and
> `da_allocation_scale` far enough to establish whether ANY reachable setting produces divergence,
> not merely test the 795 operating point.
>
> FALSIFYING.
> - L1c fails (zeroing benefit weights collapses the margin): SD-025 is a value-follower, not a
>   density-follower, and its distinguishing property is refuted.
> - L2b fails (replay raises familiarity): the MECH-094 gate the drive depends on is broken.
> - **Residual-specific:** the committed-action divergence rate is indistinguishable from zero
>   across the full reachable `curiosity_weight` x `da_allocation_scale` sweep **while the
>   preconditions are green** (producer on, expansion events >= 5, cross-candidate range strictly
>   positive). That is the `substrate_ceiling` signature by the discriminator in
>   `REE_assembly/CLAUDE.md`: built, exercised, non-degenerate, and the signal absorbed downstream
>   before it reaches committed action. On that outcome, re-tag SD-025
>   `epistemic_category: substrate_ceiling` naming the absorbing mechanism, and stop re-running the
>   existing design.
> - **NOT falsifying:** any null from a run with `benefit_terrain_live_producer` unset. That is the
>   fishtank-family configuration and it makes the bonus identically 0.0 regardless of
>   `curiosity_weight` -- a no-op, not a result.
>
> SCOPE BOUND. This falsifier addresses the DRIVE and its live consequentiality only. It does not
> address the SD-024 x SD-025 INTERACTION (that is ARC-057's `what_would_answer`; see it), and it
> does not address strategy-diversity GENERATION -- MECH-458 establishes that this drive is a
> reward-conditional exploitation amplifier with zero proactive pull toward under-represented
> regions, so a diversity null here supports MECH-458 and says nothing against SD-025.

**Proposal sketch:**
- **title:** `SD-025 live-path consequentiality: does the curiosity bonus change committed action, or
  only exist?`
- **related_claims:** `SD-025` (primary), `SD-024` (producer, supplies the preconditions),
  `ARC-057` (the interaction this deliberately does NOT test), `ARC-007` (weight-independence),
  `MECH-094` (replay gate), `MECH-111` (the broken broadcast-novelty -> E3 path 767 was scoped
  against), `MECH-458` (the polarity claim that bounds how a diversity null is read).
- **acceptance_checks:** `benefit_terrain_live_producer=True`, driver makes no direct
  `accumulate_benefit` call outside a declared positive control; `FamiliarityTracker` constructed
  (assert `curiosity_weight > 0` reaches `module.py:140`); primary DV = committed-action divergence
  rate between same-seed ON/OFF arms; co-reported mechanistic DV = cross-candidate bonus range
  (max-min), never the mean; `curiosity_weight` and `da_allocation_scale` swept, not fixed at 795's
  operating point; no binary saturating gate load-bearing; >= 8 seeds; cloud machine class;
  `experiment_purpose: evidence` -- SD-025 currently has `genuine_exp_count 0`, so a further
  `diagnostic` run leaves its experimental confidence at 0.0 whatever it finds.
- **Reuse note:** V3-EXQ-795's ARM_OFF/ARM_ON are fingerprinted (`arm_fp/v1`,
  `driver_script_in_substrate_hash: false`, `reuse_eligible: true`, substrate_hash `402e3f5a...`) but
  the substrate has moved on since 2026-07-20, so treat 795 as a calibration anchor rather than a
  reusable arm.

**depends_on additions:** none. But recommend `/governance` **annotate rather than change**
`depends_on: [SD-024, SD-004, ARC-057, MECH-111, INV-051]`: SD-004 and SD-024 are implemented, while
ARC-057 / MECH-111 / INV-051 gate the **ecological Test C**, not the built substrate. This is
`arc_057_ecological_env_decision_2026-07-16.md` sec 7's outstanding follow-up and it is still open in
`substrate_queue.json` (currency finding 9). Also worth a one-line fix there:
`design_doc: null` should be `docs/architecture/sd_024_da_modulated_rbf_density.md#curiosity-drive`.

**GOVERNANCE FLAG (three, separable):**
1. `evidence_discrepancy` -- **the entire fishtank experiment family runs with the SD-025 curiosity
   channel dead while its config reads as though curiosity is on.** Ten manifests
   (`v3_exq_906_20260809T003857Z`, `906a_20260809T081031Z`, `906b_20260809T163034Z`,
   `906c_20260810T014711Z`, `909_20260810T011652Z`, `911_20260809T201208Z`, `912_20260810T190239Z`,
   `913_20260810T213204Z`, `920_20260811T210906Z`, `920_20260814T223432Z`) set
   `curiosity_weight: 0.05` and `use_da_modulated_rbf_density: true`; **zero** of them, and zero of
   the sixteen `ree-v3/experiments/*fishtank*.py` drivers, set `benefit_terrain_live_producer`, and
   none calls `accumulate_benefit` directly. Since `agent.py:11570` is the sole producer and the flag
   defaults `False`, `_curiosity_bonus` returns exactly 0.0 in every one of those runs. This is the
   **same defect class** as the 2026-07-20 no-producer incident, re-armed by a flag that was added
   default-off and never adopted by the drivers that would need it. Any fishtank reading, telemetry
   or narrative that treats curiosity as an active channel in those runs is unsupported.
   Note the `chip-20260810-fishtank-sd025-novelty-telemetry` chip (status `done`) surfaced
   `last_novelty_score` into exactly this family -- that telemetry would have been reading zero.
   Worth a targeted check of whatever consumed it.
2. `stale_note` -- SD-025's 2026-07-20 SUBSTRATE note (*"what nothing yet establishes -- is
   LIVE-PATH efficacy"*) was superseded the same day by V3-EXQ-795. Recommended amendment is not a
   simple deletion: replace it with the *quantified* reading -- live-path efficacy is established in
   the weak sense (non-zero, floors at 1e-9) and the cross-candidate range is `0.0177` against a
   `13.83` same-statistic positive control. Also in this bucket: `claims.json`
   `"awaiting": "SD-024"`, and `substrate_queue.json` `design_doc: null`.
3. `contested_disposition` -- **SD-025's own text contradicts MECH-458, which is registered in the
   same registry and anchored on SD-025's own runs.** Specifically: the title's *"information-seeking
   bias"* (MECH-458: the polarity is inverted relative to Bellemare-2016 information-seeking; the
   drive is reward-conditional exploitation) and the `notes` sentence *"The familiarity component
   ... prevents the agent from endlessly circling already-explored regions"* (MECH-458: the brake is
   1.93x weaker than the force it opposes at its own ceiling, and exactly 0.00 at the decision
   point). MECH-458 is `candidate/v3_pending`, so this is not a settled fact that mandates a
   rewrite -- it is a genuine contested disposition that `/governance` should adjudicate rather than
   a digestion pass silently resolving. If MECH-458 is upheld, SD-025's `notes` need the
   anti-perseveration sentence scoped and the title's "information-seeking" qualified.

---

### Group-level note not attributable to a single claim

**`contested_disposition` (unowned question, raised for routing, no draft attached):** REE now has
**two independently-flagged curiosity channels** and no registry statement of how they compose.
SD-025 reads *density* off `benefit_rbf_field` and biases the hippocampal CEM `_score_trajectory`;
MECH-314a reads *minimum distance to the nearest active centre* off `residue_field.rbf_field` (a
different field, opposite polarity on the same word "density") and biases E3's `dacc_score_bias` in
`select_action()` -- verified in `ree-v3/ree_core/policy/structured_curiosity.py:829-870` and
`ree_core/hippocampal/module.py:1704-1731`. `module.py:157` even names both gates in one comment
(`curiosity_weight (SD-025) or use_structured_curiosity (MECH-314)`), which is where the composition
question becomes visible in the code. They are separately gated, so today they are simply never both
characterised together; nothing establishes whether enabling both double-counts, cancels, or
composes. This is **not** a merge candidate (see preamble (i)) -- it is an unasked design question
that will bite the first run that turns both on, and the
`curiosity_budget_split_eligibility_design_2026-08-22.md` ratification (Design B, build-gated on its
section 11 probe) covers allocation *among* the MECH-314 sub-flavours only, not the
SD-025 / MECH-314 seam.

---

<!-- G9 appended 2026-09-04T21:22:55Z -->
## G9 -- structural mint / stuckness escape pair  (agent report)

### Group preamble

- **Why these are together (restated, then my view).** The grouping hypothesis was that MECH-349
  and MECH-527 are two instances of one "triggered structural event" pattern -- a detector crosses
  a threshold, a non-gradient structural change fires, and the falsifier template is shared
  (non-degeneracy = detector demonstrably fires; confirming = post-trigger state differs from a
  no-trigger control; falsifying = no difference, or the detector never fires).
  **My view: the pattern is real but THIN, and it holds at exactly one layer -- the non-degeneracy
  precondition -- not at the confirming/falsifying legs.** The two claims' post-trigger states are
  measured in incommensurable units (MECH-349: a persistent structural population, measured in
  slot-occupancy and pairwise direction distance, entirely inside the substrate; MECH-527: a
  transient organism-level behavioural escape, measured in escape probability and discovery
  latency against an ecology that does not exist). They share no arm, no DV, no ecology and no
  substrate module. They are also at different maturity: MECH-349's mechanism is BUILT and has
  been EXERCISED five times; MECH-527's is half-built and its built half has already returned
  an adverse prior. They are NOT merge candidates with each other.
  What they *do* share is a specific, non-obvious degeneracy shape which I found empirically in
  MECH-349 and which structurally threatens MECH-527 -- see (iii) below. That shared precondition
  is worth writing once and cross-referencing, and it is the real yield of the grouping.

- **(i) same-claim / merge candidates.** *Not with each other* -- see above; no shared subject,
  substrate module, config namespace or DV. `subject:` fields are `policy.candidate_rule_field.mint`
  vs `policy.stuckness_triggered_attractor_escape`; the only overlap is the leading `policy.`
  segment, which is why the lexical grouping metric (4.25 on "candidate / action / bottom-up
  above-threshold") fired. The overlap is vocabulary, not mechanism.
  **But each has a live out-of-group merge pressure, and one of them is decisive:**
  - **MECH-527 <-> MECH-343 / SD-061 (STRONG, disposition (g)).** MECH-343
    (`difficulty_gated_proposal_entropy`) asserts: when goal progress stalls with goal salience
    preserved, transiently increase proposal-generation entropy UPSTREAM of action selection
    (wider hippocampal/CEM candidate set + higher within-class temperature), then decay once a
    workable candidate is found. That is MECH-527's mechanism, one channel deep, with the same
    trigger shape and the same decay clause. SD-061 BUILT it
    (`ree-v3/ree_core/cingulate/stuck_state_detector.py` +
    `ree-v3/ree_core/policy/difficulty_gated_proposal_entropy.py`), and V3-EXQ-694 already
    EXERCISED it. MECH-527's `depends_on` names MECH-440/313/482/314b/314c and does not mention
    MECH-343 or SD-061 anywhere. This is partial absorption, not supersession: MECH-527 has a
    genuine residual (escalation ACROSS channels above the trajectory layer; the false-bottom
    ecology; the failure-not-uncertainty trigger selectivity). Proposal in the MECH-527 section.
  - **MECH-349 <-> nothing.** It is already the narrowest face of ARC-063 (CREATE), with
    MECH-350 (REPRESENT) / MECH-351 (GATE) / MECH-352 (CREDIT) as distinct, non-overlapping
    faces of the same module. No merge indicated.

- **(ii) contradictions / undercut premises.** No contradiction *between* the two claims. But
  **MECH-527's own premise is contradicted by the substrate, and its own nominated trigger is
  contradicted by a lit-pull that landed the day it was registered:**
  1. MECH-527 `notes`: "the above-action-level perturbation channels ... do not [exist] -- DO NOT
     queue an experiment against this until both exist". **False for channel 1.** SD-061 is
     `implemented_pending_validation` in `substrate_queue.json` and both halves are in `ree_core`.
     The regulator's own docstring states its purpose in MECH-527's exact terms: it "lifts
     PROPOSAL-layer entropy ... only when stuck", explicitly NOT the action-selection softmax,
     with decay carried by the detector's asymmetric EMA. Of MECH-527's five named channels
     (candidate trajectories / strategy proposals / retrieved attractors / goal decompositions /
     precision-authority of the dominant attractor), **the first is built; the other four are not.**
  2. MECH-527 nominates MECH-482's `epistemic_deficit` as the trigger. The 2026-09-01 targeted
     lit-pull (`evidence/literature/targeted_review_connectome_mech_440/SYNTHESIS_2026-09-01_mech440_mech527.md`
     s.5 rec.3) establishes that the landed SD-102 accumulator is fed by candidate-specific
     predictive *uncertainty*, *persistent realized prediction error*, and predictive-system
     *disagreement* -- and that in MECH-527's paradigm case (a settled, confident, persistently
     failing attractor) two of those three inputs are *suppressed* exactly when the trigger should
     fire. The claim's premise that MECH-482 is a "natural trigger substrate" is undercut by its
     own commissioned literature.
  3. **My own addition, not in the synthesis:** the better-fitting built detector is SD-061's
     `StuckStateDetector`, and it too is only a partial fit -- and in an instructive way. Its four
     axes are goal-progress stall, E3 score margin, committed-action-class diversity, and dACC
     choice difficulty. Axes 1 and 3 (stall, lock-in) are exactly MECH-527's trigger. Axes 2 and 4
     are *near-tie / ambiguity* axes -- low score margin and small EV spread -- which MECH-527
     explicitly names as the case that must produce NO exploration ("two well-understood, similarly
     -good actions warrant NO exploration"). With `combine_mode="mean"` (the default), the built
     detector therefore carries **50% wrong-signed evidence for MECH-527's trigger**. That is not
     a refutation; it is a precisely-specifiable non-degeneracy requirement (below) and a cheap
     substrate amendment (a MECH-527-scoped `combine_mode` / axis mask).
  4. MECH-349's `notes` claim "Validation V3-EXQ-639". V3-EXQ-639 is `outcome: PASS` but
     `evidence_direction: non_contributory` with `claim_ids: []`, and `claim_evidence.v1.json`
     has **no entry at all for MECH-349** (nor MECH-350/351/352). The real CRF data lives under
     SD-078/ARC-063 attribution. Not a contradiction, but the claim's own text points at the
     wrong artifact.

- **(iii) shared falsifier.** There IS one shared, reusable artifact, and it is narrower and
  better than the one the grouping hypothesised. Both claims' triggers can fail non-vacuity in
  **two opposite directions**, and a falsifier that guards only one of them is defeated by the
  other. I name it here once so both drafts can cross-reference rather than re-derive:

  > **TRIGGERED-STRUCTURAL-EVENT PRECONDITION (G9).** A run testing a threshold-triggered
  > structural event is non-vacuous only if the trigger is shown to be a TRIGGER -- i.e. it fires,
  > and it also does NOT fire -- across the measured window, and if the discriminating input is
  > shown to be what carried the firing.
  > **(A) NEVER-FIRES pole:** the detector must exceed its threshold on >= 2/3 seeds from
  > naturally-arising conditions, not only from an experimenter-induced impasse or a warm-started
  > pool. A run in which the event count is 0, or in which every event occurs inside a scripted
  > induction window, measures nothing.
  > **(B) ALWAYS-FIRES / SATURATE pole (the one usually missed):** the detector must also be BELOW
  > threshold for a non-trivial fraction of the window, and the structural resource the event
  > consumes must not be exhausted early. If the trigger is pinned high, or the resource saturates
  > and the event becomes structurally impossible thereafter, then the ON-vs-OFF contrast is a
  > DOSE difference, not a TIMING difference, and any post-trigger delta is uninterpretable as
  > evidence for a *triggered* mechanism. Report the duty cycle (fraction of ticks above
  > threshold) and the event-count time course, not just the total.
  > **(C) SELECTIVITY:** where the detector aggregates several inputs, report each input's
  > separate contribution. A claim whose distinctive assertion is *which* condition triggers the
  > event cannot be tested by a detector that fires on a correlated always-on channel.

  Empirical warrant for (B): it is not hypothetical -- it is the *measured* state of MECH-349's
  substrate in both of its configurations (see that section). For MECH-527 it is a live structural
  risk: `StuckStateDetector`'s EMA is deliberately asymmetric (`ema_alpha_rise` 0.3 vs
  `ema_alpha_fall` 0.05, a 6:1 hysteresis), which is exactly the shape that pins a score high once
  raised.

- **(iv) cross-cutting finding.** **Both claims' `notes` are stale in the same direction and by the
  same mechanism: the claim's own prose is being used as the record of substrate state, and the
  substrate has moved underneath it in both cases -- in opposite directions.** MECH-349's notes
  under-report (they cite a non-contributory readiness run as "validation" and are silent on the
  SD-078 centering fix, the availability-maintenance amend, and V3-EXQ-806/822, all of which
  post-date the `live_status.as_of` of 2026-07-11). MECH-527's notes over-report a blocker (they
  declare a channel unbuilt that is built and exercised, and a lit-pull owed that has already
  landed -- on the *same day* the claim was registered, 2026-09-01). Neither claim can be safely
  routed from its own text. This is the group's most transferable finding: for any claim whose
  notes assert a build status, the `notes` are a *hypothesis about the substrate*, and the
  substrate_queue entry plus a `ree_core` grep is the check.

- **Currency findings (explicit, one line each).**
  1. **SD-061 is BUILT.** `substrate_queue.json` -> `SD-061`, status `implemented_pending_validation`,
     priority 5. Modules: `ree-v3/ree_core/cingulate/stuck_state_detector.py` (detector) and
     `ree-v3/ree_core/policy/difficulty_gated_proposal_entropy.py` (regulator). Config knob
     `use_difficulty_gated_proposal_entropy: bool = False` (`ree_core/utils/config.py:4945`) --
     built, wired, default-OFF. **Contradicts MECH-527's "channels do not exist".**
  2. **SD-061 has been EXERCISED, with an adverse prior.** V3-EXQ-694
     (`v3_exq_694_sd061_difficulty_gated_proposal_entropy_readiness_20260619T224714Z_v3.json`,
     PASS, `claim_ids: []`, reviewed): the stuck arm widened the candidate set 32 -> 40, and
     `first_action_entropy` FELL on 3/3 seeds (-0.0812 / -0.0734 / -0.0953) while the
     no-widening control drifted mixed in sign (-0.0224 / +0.0139 / +0.0914). Count-widening
     without entropy-widening. MECH-343's `what_would_answer` already carries this as a
     "PRIOR TO CARRY IN". **MECH-527 must power against it, not rediscover it.**
  3. **The MECH-527 lit-pull HAS LANDED.** `chip-20260830-mech440-targeted-lit-pull` ran
     2026-09-01 (session `c1-lit-pull-mech440-20260901`), widened to MECH-527 as the claim asked.
     Entries at `evidence/literature/targeted_review_connectome_mech_527/` (Karlsson/Tervo/Karpova
     2012 supports; Neuringer/Kornell/Olufs 2001 mixed; Mladenovic & Hansen 1997 supports,
     formal precedent only); joint synthesis at
     `targeted_review_connectome_mech_440/SYNTHESIS_2026-09-01_mech440_mech527.md`.
     `claim_evidence.v1.json` shows MECH-527 with 4 lit entries, `lit_conf 0.89`, quadrant
     `plausible_unproven`. **MECH-527's `notes` still say the pull "SHOULD widen its target"
     (future tense) and its `evidence:` list is `[]`.** Three named revisions are owed
     (rename toward Variable Neighborhood Search; soften "attractor escape" -- Neuringer found
     variability rising *around a preserved dominant response*, i.e. added variation, not
     relocation; and fix the trigger-substrate mismatch). **Escalating breadth is recorded by
     that synthesis as biologically UNSUPPORTED** -- only an algorithmic precedent exists, which
     under the biology-before-formal-definitions invariant is not grounding.
  4. **MECH-482's own `what_would_answer` is stale.** It says the target-bound uncertainty
     substrate is "not yet built in V3"; SD-102 landed 2026-08-29 (ree-v3 `b69a1b8`) and
     `substrate_queue.json` -> `sd_epistemic_deficit_multitarget_readiness` is
     `implemented_pending_validation`. Out of group; reported because MECH-527 leans on it.
  5. **MECH-349's substrate is complete and its blocker is cleared.** `substrate_queue.json` ->
     `crf-availability-maintenance` reads "This substrate entry is complete; no further CRF
     amend owed" (2026-06-19). ARC-063's own `what_would_answer` states "CREATE/REPRESENT/GATE/
     CREDIT (MECH-349-352) landed". `use_candidate_rule_field: bool = False`
     (`config.py:4063`) -- built, default-OFF.
  6. **MECH-349 has landed, unattributed evidence.** V3-EXQ-806
     (`..._sd078_centered_rule_field_context_key_20260725T191042Z_v3.json`, PASS / **supports**,
     `claim_ids: ['SD-078']`, reviewed) and V3-EXQ-822
     (`..._sd078_rule_selection_consumer_20260726T112152Z_v3.json`, **FAIL**,
     `evidence_direction: unknown`, `claim_ids: ['SD-078']`) both carry full mint diagnostics.
     Neither names MECH-349. `claim_evidence.v1.json` has no MECH-349 entry.
  7. **The project-memory "escape-forward reuse" lead is a NAME COLLISION -- checked and
     excluded.** `ree-v3/ree_core/pfc/e2_escape_affordance_linker.py` is the post-603i SD-059 /
     MECH-358 relief/safety **threat**-escape affordance readout ("where out is under threat"),
     with `escape_affordance_bridge.py` and `trainable_escape_affordance_learner.py`. It is
     physical escape from a threat, not escape from a policy attractor. It is **not** the built
     mechanism MECH-527 describes and should not be cited as such.
  8. **No false-bottom ecology exists** (`grep -rin "detour|delayed.return|false.bottom|
     suboptimal loop" ree-v3/ree_core ree-v3/experiments/_lib` -> zero hits), confirming the
     intake's own gap row. **But one is documented in the record and is cheaper to build than
     the claim assumes** -- see the MECH-527 proposal sketch (MECH-457 / V3-EXQ-769 D3 passive-
     survival optimum).
  9. **MECH-080 is complementary, not overlapping.** MECH-080's OCD leg is "attractor lock-in
     (abnormally deep basin, MECH-076, **normal signals cannot trigger basin exit**)". MECH-527
     is a candidate identity for those normal signals. MECH-080 is the pathological *absence* of
     MECH-527, which makes it a falsifier route (lesion the escalation, reproduce the signature),
     not a duplicate.
 10. **MECH-497 / MECH-498 do NOT duplicate MECH-527** (the brief flagged this as possible
     disposition-(g) territory; I checked and it does not hold). MECH-497 is self-referential
     *measurement* corruption of a stopping variable (checking degrades the confidence that
     gates termination). MECH-498 is progress-gated *disengagement* (MVT: stop investing). Neither
     injects variation, and neither is triggered-then-decaying. The four claims form a clean
     taxonomy under ARC-128 rather than a duplication: MECH-343 = try harder (widen), MECH-527 =
     try differently (escalate above the action level), MECH-498 = give up, MECH-497 = fail to
     stop. **MECH-527 does not `depends_on` ARC-128 and should.**

---

### MECH-349 -- CandidateRule mint (ARC-063 CREATE face): a non-gradient structural event mints...

**Recommended disposition:** **(a) testable now** -- the module is built, default-OFF but armable,
the mint fires non-degenerately in the current SD-078-centered configuration, and the claim's own
assertion is measurable entirely UPSTREAM of the MECH-439 F-dominance conversion ceiling that
blocks its parent ARC-063, so it does not inherit that blocker.

**Extracted from:** the claim's own `notes` (the three-clause mint predicate: recurrence >=
`crf_mint_recurrence_threshold`, no existing `context_tag` cosine >= match threshold, free slot
exists) verified line-by-line against
`ree-v3/ree_core/policy/candidate_rule_field.py::_maybe_mint` (lines 432-502); plus the sibling
ARC-063 `what_would_answer` (for what is explicitly NOT owed here); plus measured mint diagnostics
from V3-EXQ-666c, V3-EXQ-806 and V3-EXQ-822. Not drafted fresh.

**Currency check:**
- `_maybe_mint` implements the asserted predicate exactly, including the optional ARC-062 seed
  (`seed_from_arc062: bool = True`, `candidate_rule_field.py:154`; `init_avail = min(1.0,
  tolerance_floor + 0.5 * |gating_weight - 0.5| * 2)`).
- `crf-availability-maintenance` (substrate_queue) is **complete, ready flipped True 2026-06-19**;
  the notes' implied "awaiting V3-EXQ-639 validation" framing is stale by ~3 months.
- V3-EXQ-639 is PASS but `non_contributory` with `claim_ids: []` -- it is a readiness diagnostic,
  not a validation of MECH-349.
- **The mint is demonstrably LIVE.** V3-EXQ-806 `baseline_allocated=True` arm:
  `crf_n_minted` 3 / 10 / 10, `crf_max_pairwise_rule_dist` 1.598 / 1.701 / 1.701,
  `crf_n_retired` 0, `crf_frac_active` 0.518 / 0.706 / 0.490 across seeds 101/202/303.
  V3-EXQ-822: `crf_n_minted` 16 / 16 / 16, `crf_max_pairwise_rule_dist` 1.711 on all three seeds.
- **And it is degenerate in BOTH available configurations, in opposite ways** -- this is the
  central finding and the reason the falsifier below is shaped as it is:
  - *Churn pole (legacy / uncentered).* V3-EXQ-666c `ARM_0_OFF`: `crf_n_minted_total`
    302 / 257 / 239 with `crf_n_retired_total` 302 / 257 / 239 and
    `crf_max_pairwise_rule_dist` **0.0** on all three seeds. Hundreds of mints, one slot, zero
    differentiation -- mint-retire thrash, the novelty clause failing because the uncentered
    context key is common-mode dominated (the SD-078 fault, `1 bucket raw vs 20 centered`).
    Same signature in V3-EXQ-806's `baseline_allocated=False` arm: 1 minted, dist 0.0.
  - *Saturate-and-freeze pole (mature + maintenance -- the CURRENT config).* `n_slots: int = 16`
    (`candidate_rule_field.py:145`). V3-EXQ-822 minted **16 of 16** with
    `crf_live_rules_final: 16` and no retirements. Mechanism: `availability_maintenance` floors
    every rule's availability at `maintenance_floor = 0.45`, while the mature retirement floor is
    `mature_retire_floor = 0.05`, so **no rule can ever fall below the retire floor** and clause
    (c) of the mint predicate ("a free slot exists") becomes permanently unsatisfiable once the
    pool fills. The field mints its 16 rules in an early burst and then **structurally cannot
    mint again for the rest of the run.** MECH-349 asserts an *ongoing*, regularity-contingent
    structural creator; what the substrate currently exhibits is a one-shot fill.
- **A second, independent vacuity in the ARC-062-seed leg.** `init_avail` from the seed spans
  [0.30, 0.80] (`tolerance_floor = 0.3`, plus `0.5 * confidence`). It is then overwritten by
  `max(init_avail, 0.45)` under `availability_maintenance`. So whenever the ARC-062 discriminator's
  `gating_weight` lies in **(0.35, 0.65)** -- confidence < 0.30 -- the seed contributes **exactly
  nothing**, in the very configuration every recent CRF run uses. Only one manifest in the whole
  evidence tree even records `seed_from_arc062`
  (`v3_exq_876a_mech025_doing_mode_convergence_redesign_...`), so this leg is effectively untested.

**epistemic_category (proposed):** `standard`.
Explicitly **not** `substrate_conditional` -- the code exists and has been exercised five times
(639, 666a, 666b, 666c, 806, 822), which is the discriminator the REE_assembly CLAUDE.md note
gives ("the mechanism has genuinely never been exercised"). Explicitly **not** `substrate_ceiling`
-- the F-dominance ceiling absorbs the *committed-action* signal downstream of MECH-351/352 and
SD-033a; it does not touch MECH-349's own DVs, which are mint counts, retirement counts and
pairwise rule-direction distance inside the field. ARC-063's parent falsifier is blocked by that
ceiling; MECH-349's is not, and conflating them is what has kept this claim parked.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION. Apply TRIGGERED-STRUCTURAL-EVENT PRECONDITION (G9) in full; this
> claim is the one the (B) pole was written from. Concretely, and all four must hold in the same
> run before any verdict is admissible:
> (a) *Mint fires.* `crf_n_minted >= 2` and `crf_live_rules_final >= 2` on >= 2/3 seeds. A run with
> 0 or 1 live rules measures nothing (V3-EXQ-806's `baseline_allocated=False` arm and every
> uncentered-key arm fail here).
> (b) *Mints are DISTINCT, not churn.* `crf_max_pairwise_rule_dist > 0` -- ideally at the pinned-
> direction scale ~1.6-1.7 -- AND `crf_n_retired_total / crf_n_minted_total <= 0.25`. The
> V3-EXQ-666c `ARM_0_OFF` signature (302 minted, 302 retired, dist 0.0) is the canonical
> vacuous-positive: a large mint count that is evidence of nothing.
> (c) *The pool does NOT saturate inside the measurement window.* Report `crf_live_rules_final /
> crf_n_slots` and the **mint time course** (mints per 10% of the episode). At least one mint must
> occur in the final third of the window, and `crf_live_rules_final < crf_n_slots` at the end. A
> run that fills 16/16 slots in an early burst and then freezes has converted the asserted
> *triggered creator* into a *one-shot initialiser*, and its ON-vs-OFF delta is a dose contrast,
> not a trigger contrast. With `crf_availability_maintenance=True` and `crf_maintenance_floor
> (0.45) > crf_mature_retire_floor (0.05)` this failure is the DEFAULT, so the run must either
> lower `maintenance_floor` below the retire floor for a subset of rules, raise `crf_n_slots`
> above the number of distinguishable regimes the ecology affords, or extend the window until
> mints demonstrably become regularity-limited rather than slot-limited.
> (d) *The seed leg is separately non-vacuous, or is explicitly not under test.* If the ARC-062
> top-down leg is claimed, report the distribution of `|arc062_gating_weight - 0.5|` at mint
> events. Under `availability_maintenance` any mint with confidence < 0.30 has its seed
> contribution entirely overwritten by `maintenance_floor`. If 100% of mints fall below that,
> the seed leg is UNTESTED regardless of outcome and must be reported as such, not as a null.
>
> CONFIRMING. On the SD-078-centered context key with the mature-pool + maintenance stack, in an
> ecology presenting >= 3 separable (context-regime -> action-object) regularities:
> (1) *Recurrence-gating is real.* Mint events occur only after the keyed regularity has recurred
> `>= crf_mint_recurrence_threshold` (3) times: the measured recurrence count at mint is >= 3 on
> 100% of mint events, and a matched control arm with the threshold raised (e.g. 3 -> 12) shows
> mint count falling monotonically, with the surviving mints still distinct (dist unchanged within
> noise). If raising the threshold does not reduce mints, the counter is not what is gating.
> (2) *Novelty-gating is real.* Mints track the number of *distinct* regularities the ecology
> offers, not elapsed time or tick count. Across a 3-regime vs a 1-regime variant of the same
> ecology, `crf_live_rules_final` in the 3-regime variant exceeds the 1-regime variant by
> >= 2 rules on >= 2/3 seeds, with the 1-regime variant holding at 1-2. Additionally, a matched
> control that lowers `mature_mint_block_threshold` (0.8 -> 0.5) must produce FEWER mints (a
> stricter novelty gate blocks more), establishing the block is load-bearing rather than inert.
> (3) *The minted population is distinct by construction.* `crf_max_pairwise_rule_dist >= 1.5`
> (against the observed pinned-direction scale of 1.598-1.711) on >= 2/3 seeds -- this is
> MECH-350's assertion and is reported here only as the CREATE face's output being well-formed;
> do not re-derive it, cross-reference MECH-350.
> PASS gate scaling: the between-variant rule-count delta in (2) must exceed max(2 rules,
> 2 x SD of the within-variant per-seed rule count), with the 2-rule absolute floor binding.
>
> FALSIFYING.
> (1) Mint count is insensitive to the recurrence threshold across a >= 4x sweep while the
> preconditions hold -- the asserted "recurs above threshold" trigger is not the mechanism;
> minting is driven by context-key drift, tick count, or slot availability instead.
> (2) Mint count is insensitive to the number of distinct regularities the ecology presents
> (1-regime and 3-regime variants produce statistically indistinguishable
> `crf_live_rules_final`) -- the novelty clause is inert and the "creator" is a timer.
> (3) The 666c signature reappears on the SD-078-centered key with maintenance ON -- high
> `crf_n_minted_total` with `crf_n_retired_total` of comparable magnitude and
> `crf_max_pairwise_rule_dist` at or near 0 -- i.e. the centering fix does not generalise beyond
> the ecology 806 was run in. This falsifies the CREATE face as a *structural* creator: it mints
> tokens, not slots.
> NOT FALSIFYING. A null on any downstream committed-action or behavioural DV. That is the shared
> MECH-439 F-dominance conversion ceiling, which sits below MECH-351/352 and SD-033a and is
> owned by ARC-063's own `what_would_answer` precondition (2) and by the `f_dominance_conversion_
> ceiling` substrate line. MECH-349 asserts that a distinct slot is MINTED, not that minting
> changes behaviour. Routing such a null to MECH-349 would repeat the ARC-062 GAP-B
> C1-holds/C2-fails misattribution 21 autopsies have already recorded.

**Proposal sketch (disposition (a)):**
- **Title:** `MECH-349 CREATE-face mint predicate falsifier: recurrence-gating x novelty-gating x
  non-saturating pool`
- **Related claims:** MECH-349 (primary), MECH-350 (REPRESENT -- cross-referenced for the
  distinctness readout, not re-derived), ARC-064 (bottom-up regularity source), ARC-062
  (seed leg, arm-able separately), ARC-063 (parent; explicitly NOT under test here).
- **Design:** 2x2x(regime-count) on the SD-078-centered + mature-pool + maintenance stack.
  Factor 1 `crf_mint_recurrence_threshold` in {3, 12}; factor 2 `crf_mature_mint_block_threshold`
  in {0.8, 0.5}; factor 3 ecology regime count in {1, 3}. Slot pressure relieved
  (`crf_n_slots` raised above the regime count, or `crf_maintenance_floor` lowered below
  `crf_mature_retire_floor`) so precondition (c) can be met -- **this is the one substrate
  parameter change the experiment requires, and it is a config-only change, no build.**
  Optional 5th arm arming `crf_seed_from_arc062` with the gating-weight distribution recorded.
- **Acceptance checks:**
  - C0 (non-vacuity, self-routing): preconditions (a)-(c) above met on >= 2/3 seeds in the
    reference arm; else `substrate_not_ready_requeue`, no verdict.
  - C1 (recurrence-gating, load-bearing): mint count at threshold 12 strictly below threshold 3
    on >= 2/3 seeds, with `crf_max_pairwise_rule_dist` preserved within noise.
  - C2 (novelty-gating, load-bearing): `crf_live_rules_final` 3-regime minus 1-regime >= 2 on
    >= 2/3 seeds; AND mint count at block-threshold 0.5 strictly below 0.8.
  - C3 (diagnostic only, not a gate): mint time course shows >= 1 mint in the final third.
  - C4 (negative control): OFF arm (`use_candidate_rule_field=False`) bit-identical to the
    pre-CRF baseline.
  - **Explicitly excluded from the gate:** any committed-action-class or behavioural DV. Record
    them as diagnostics; a null there routes to `f_dominance_conversion_ceiling`, not to MECH-349.

**depends_on additions:** none required. (Optional, low value: SD-078 as the context-key fix the
mint now depends on for non-degeneracy -- currently invisible from MECH-349's block, which is
part of why its evidence is unattributed.)

**GOVERNANCE FLAG:** `evidence_discrepancy` -- MECH-349 has zero entries in
`claim_evidence.v1.json` while three landed, reviewed runs carry its headline diagnostics under
SD-078/ARC-063 attribution: V3-EXQ-806 (PASS/supports, `crf_n_minted` 3-10, dist 1.598-1.701),
V3-EXQ-822 (**FAIL**, `evidence_direction: unknown`, 16/16 slots minted, dist 1.711) and
V3-EXQ-666c (`ARM_0_OFF` 302 minted / 302 retired / dist 0.0). The same gap affects MECH-350,
MECH-351 and MECH-352 (all four `NOT FOUND` in the index). Requested action: attribute the
existing manifests to the CREATE/REPRESENT faces (or record explicitly why they cannot be), and
adjudicate V3-EXQ-822's `unknown` direction -- a FAIL whose mint and representation diagnostics
are healthy (16 minted, dist 1.711, `crf_frac_active_p2` 0.87-0.89) but whose consumer leg failed
is exactly the kind of run that is silently read as evidence against the wrong face.

**GOVERNANCE FLAG:** `stale_note` -- MECH-349's `notes` end "Validation V3-EXQ-639", but 639 is
`non_contributory` with `claim_ids: []`, and the notes predate and omit the SD-078 centering fix
(2026-07-25), the completed `crf-availability-maintenance` amend (ready 2026-06-19), and
V3-EXQ-806/822. `live_status.as_of` is 2026-07-11. Suggested amendment: replace the validation
pointer with SD-078 + the 806/822 pair, and record the saturate-and-freeze interaction
(`maintenance_floor 0.45 > mature_retire_floor 0.05` -> retirement can never fire -> the mint
predicate's free-slot clause becomes permanently blocking at 16/16) as a known non-degeneracy
constraint on any future CRF run, since it silently affects MECH-350/351/352 as well.

---

### MECH-527 -- Stuckness-triggered attractor-escape exploration: a triggered, organism-level...

**Recommended disposition:** **(g) merge with sibling -- PROPOSE ONLY** (partial absorption into
MECH-343/SD-061, which already owns and has BUILT the trajectory-proposal channel), leaving a
**narrowed residual** that stays **(f) deferred / substrate_conditional** with three named,
resolvable blockers -- because the claim as currently written straddles a built-and-exercised leg
and an unbuilt leg, and its `notes` misreport which is which.

**Extracted from:** the claim's own `notes` falsifier sketch (false-bottom ecology; >= 3 arms
no-perturbation / low-level action noise / stuckness-triggered strategy perturbation; organism-level
DVs escape probability, discovery latency, basin quality, post-resolution decay,
no-unnecessary-exploration control) -- these are good and are preserved verbatim below; PLUS the
commissioned lit synthesis
`evidence/literature/targeted_review_connectome_mech_440/SYNTHESIS_2026-09-01_mech440_mech527.md`
s.5 (three owed revisions, and the trigger-substrate mismatch that becomes the precondition);
PLUS MECH-343's already-drafted `what_would_answer`, which is substantively the falsifier for
MECH-527's built channel. Not drafted fresh.

**Currency check:**
- **Channel 1 of 5 is BUILT and default-OFF.** `substrate_queue.json` -> `SD-061`
  `implemented_pending_validation`; `ree-v3/ree_core/cingulate/stuck_state_detector.py` (graded
  `stuck_score` in [0,1] from goal-progress stall + E3 score margin + committed-class diversity +
  dACC choice difficulty, gated by goal salience, asymmetric EMA rise 0.3 / fall 0.05) and
  `ree-v3/ree_core/policy/difficulty_gated_proposal_entropy.py` (`extra_candidates =
  round(candidate_widen_max * s)`, `temperature_gain = 1 + temperature_gain_max * s`, applied to
  `HippocampalModule.propose_trajectories` and the differentiable-CEM within-class temperature).
  Knob `use_difficulty_gated_proposal_entropy: bool = False` (`config.py:4945`).
  **The claim's "the above-action-level perturbation channels ... do not [exist]" is wrong for
  this channel and right for the other four** (strategy proposals, retrieved attractors, goal
  decompositions, precision/authority of the dominant attractor -- no `ree_core` analogue found).
- **Channel 1 has been EXERCISED with an adverse result** -- V3-EXQ-694, detail in preamble
  currency finding 2. Count widened 32->40; first-action entropy fell 3/3.
- **The lit-pull the notes request has already landed** (preamble currency finding 3), including
  the finding that **escalating breadth -- MECH-527's most distinctive commitment -- has NO
  biological support**, only the algorithmic Variable Neighborhood Search precedent, which the
  biology-before-formal-definitions invariant does not accept as grounding.
- **The nominated trigger substrate does not fit.** MECH-482's SD-102 accumulator
  (`ree-v3/ree_core/policy/epistemic_deficit.py`, landed 2026-08-29 `b69a1b8`) is fed by
  predictive uncertainty + persistent realized prediction error + inter-predictor disagreement;
  MECH-527's paradigm case (confident, settled, persistently failing) suppresses the first and
  third. Only the persistent-PE channel matches. MECH-482 additionally has its own open
  readiness debt (`sd_epistemic_deficit_multitarget_readiness`,
  `implemented_pending_validation`; V3-EXQ-964 was structurally unsatisfiable per its own
  `evidence_quality_note`), so it is not a substrate one can lean on today.
- **The better-fitting built detector is SD-061's, and it is 50% wrong-signed** (preamble (ii)(3)).
  This is a *cheaper* blocker than it looks: `StuckStateDetector` treats each axis as Optional and
  inert when `None`, so a MECH-527-scoped trigger is a config/wiring change (stall + committed-
  diversity only, `combine_mode` mean over the two), not a build.
- **No false-bottom ecology exists** -- confirmed by grep across `ree_core` and
  `experiments/_lib`. **But one is already documented.** `failure_autopsy_V3-EXQ-769_2026-07-17`
  (via `ree-v3/experiments/_lib/mech457_probe_envs.py`) records that on the D3_hazard_free rung
  the trained ON arm learned a locally stable, high-survival, **persistently inadequate** policy
  -- keep moving to avoid self-contamination, survive all 200 steps, death 0, forage ~0 -- while
  the better strategy (forage) went undiscovered. That is a false bottom by MECH-527's own
  definition ("a locally stable but persistently inadequate basin"), it arose naturally rather
  than by construction, and `MetabolicForageWrapper` is the already-written switch that dissolves
  it. The ecology blocker is therefore `complicated (buildable)` at the experiment layer (an env
  wrapper, the established `_lib` probe-scaffold pattern), not `complex (probe-gated)`.
- **Taxonomy check requested by the brief: MECH-527 does NOT duplicate MECH-497/498** -- preamble
  currency finding 10. It does not duplicate MECH-080 either; MECH-080 is its pathological absence
  (finding 9).

**epistemic_category (proposed):** `substrate_conditional` -- **unchanged, but only for the
narrowed residual defined below.** The current value is right for the wrong reason: it is
justified today by "channels do not exist", which is false for channel 1; it remains justified for
the residual (channels 2-5 genuinely do not exist, the escalation ladder does not exist, and no
false-bottom ecology exists). If the merge below is NOT accepted and the claim keeps the
trajectory-widening leg, then the honest category for that leg is whatever MECH-343 carries
(currently `substrate_ceiling`), and the claim would be split-category -- which is itself the
argument for the merge.

**Draft `what_would_answer`:**

> SCOPE NOTE. This claim's trajectory-proposal-widening leg is MECH-343/SD-061's question, already
> built (`ree_core/policy/difficulty_gated_proposal_entropy.py`) and already partially measured
> (V3-EXQ-694). **See MECH-343's own `what_would_answer` -- in particular its
> SHARED-CONVERSION-PRECONDITION (G4) reference, its "DECLARE WHICH TEMPERATURE the entropy DV
> reads" clause (SD-061's CEM proposal-layer knob vs the SD-069/MECH-313 E3 select() softmax --
> different knobs; a run that conflates them cannot attribute its result), and its "PRIOR TO
> CARRY IN" record that V3-EXQ-694's ON arm entropy FELL on 3/3 seeds. Do not re-derive any of
> it.** What follows tests only what is left after that: escalation ACROSS channels, and the
> trigger's selectivity.
>
> NON-DEGENERACY PRECONDITION. Apply TRIGGERED-STRUCTURAL-EVENT PRECONDITION (G9) in full, plus
> three requirements specific to this claim, all of which must be reported before any verdict:
> (a) *A genuine false bottom must be demonstrated to EXIST in the ecology, by a control that has
> nothing to do with this claim.* Show that a competent-by-other-means agent (an oracle, a shaped-
> reward arm, or a hand-coded policy) attains materially better basin quality than the no-
> perturbation arm converges to, and that the no-perturbation arm's policy is STABLE (low
> committed-class turnover) and CONFIDENT (high score margin) while it sits there. Without that
> control, a null on escape is indistinguishable from "there was nothing to escape to". The
> MECH-457 / V3-EXQ-769 D3_hazard_free passive-survival optimum is a documented instance and the
> `MetabolicForageWrapper` in `experiments/_lib/mech457_probe_envs.py` is the dissolving control.
> (b) *The trigger must be selective, and the near-tie axes must be shown NOT to be carrying it.*
> This claim's load-bearing distinction is that unresolvedness triggers and uncertainty does not.
> SD-061's `StuckStateDetector` combines four axes, of which two (E3 score margin, dACC choice
> difficulty) are near-tie/ambiguity axes that this claim asserts should trigger NOTHING. Report
> each axis's separate contribution to `stuck_score` at every firing. CONFIRMING requires that
> the stall and committed-diversity axes carry the firing in the false-bottom condition; if the
> two near-tie axes carry it, the run has tested MECH-440's trigger, not this one, and must
> self-route rather than report a verdict.
> (c) *The trigger must fire from naturally-arising blockage, and must also NOT fire.* Detector
> peak must exceed threshold and then decay on >= 2/3 seeds from ecological stuckness, not from
> an experimenter-induced impasse (V3-EXQ-694 induced its impasse; that route is already spent).
> Report the duty cycle: with `ema_alpha_rise` 0.3 vs `ema_alpha_fall` 0.05, a pinned-high score
> is the expected failure and turns every arm contrast into a dose contrast. Duty cycle must lie
> strictly inside (0.05, 0.80).
> (d) *If MECH-482's `epistemic_deficit` is used as the trigger, the persistent-PE channel must
> be isolated.* Per the 2026-09-01 synthesis, the uncertainty and disagreement inputs are
> suppressed exactly in the confident-but-failing case, so an unmodified `epistemic_deficit` that
> fails to rise is a substrate artifact, not evidence against the claim. Either consume the
> persistent-PE channel only, or use the SD-061 stall + committed-diversity axes, and say which.
>
> CONFIRMING (the claim's own registered design, preserved). A >= 3-arm run in a demonstrated
> false-bottom ecology -- (1) no perturbation; (2) low-level ACTION noise (MECH-313/MECH-440
> class); (3) stuckness-triggered perturbation ABOVE the action level -- on organism-level DVs:
> arm 3 strictly beats BOTH arm 1 and arm 2 on escape probability and discovery latency, with
> basin quality after escape strictly better than the false bottom's, AND perturbation magnitude
> decays after resolution, AND the no-unnecessary-exploration negative control holds (a matched
> near-tie condition with two well-understood, similarly-good options produces NO perturbation
> above arm 1's baseline). Effect-size gate: the arm-3-minus-arm-1 escape-probability delta must
> exceed max(2 x SD of the per-seed delta, an absolute floor of 0.20 escape probability), on
> >= 2/3 seeds.
> ESCALATION LEG (separately gated, and currently the claim's weakest commitment). Under CONTINUED
> stuckness the perturbation must broaden across channels, not merely intensify within one: at
> least one channel beyond candidate trajectories must be shown to engage, later than channel 1,
> and only after channel 1 has failed to resolve. **Recorded as a KNOWN GAP rather than an
> asserted property**: the 2026-09-01 synthesis found no biological support for graded escalation
> (Karlsson 2012 gives the destabilise-then-decay, nothing gives the ladder), and the only
> precedent is algorithmic. Do not gate the claim's verdict on this leg until it has grounding.
>
> FALSIFYING.
> (1) With the preconditions met, arm 3 does not beat arm 2 -- low-level action noise escapes the
> false bottom as often and as fast as above-action-level perturbation. This is the claim's own
> load-bearing distinction from MECH-440/MECH-313 and its failure is the cleanest refutation.
> (2) The no-unnecessary-exploration control fails: arm 3 perturbs in the matched near-tie
> condition as much as in the false-bottom condition. The trigger is uncertainty after all, and
> the claim collapses into the operationalisation V3-EXQ-959 already weakened.
> (3) Perturbation rises under stuckness and never decays after resolution -- falsifies the
> annealing/triggered half, leaving a tonic floor (which MECH-313 already owns and V3-EXQ-687
> found non-propagating).
> (4) Variation rises but the policy does not RELOCATE: the dominant response stays dominant with
> rare variants beneath it, and basin quality is unchanged. This is Neuringer, Kornell & Olufs
> (2001, PMID 11199517) under extinction, flagged by the 2026-09-01 synthesis as the specific
> reason "attractor escape" is over-claimed. It falsifies the ESCAPE framing while leaving a
> weaker "variability injection under stuckness" reading standing -- **record it as a narrowing,
> not a demotion**, and rename accordingly.
> NOT FALSIFYING. A null on channel 1 (candidate-trajectory widening) alone. V3-EXQ-694 already
> established that count-widening does not lift first-action entropy; that is MECH-343's owed
> question and its `what_would_answer` routes such a null to the conversion-ceiling line, not to
> a weakening.

**Merge proposal, disposition (g) -- PROPOSE ONLY, for /governance to accept or reject:**
- **Surviving id:** MECH-343 (with SD-061 as its design decision) absorbs the
  trajectory-proposal-widening leg. MECH-527 **survives, narrowed** -- this is partial absorption,
  not supersession.
- **Absorbed id / text that moves:** from MECH-527's title and notes, the clause "transiently
  injects variation ABOVE the immediate-action level -- perturbing candidate trajectories" (the
  first named channel only) and the post-resolution decay clause as it applies to that channel.
  Both are already asserted by MECH-343 and BUILT by SD-061; MECH-527 restates them without
  citing either.
- **What MECH-527 RETAINS (the residual, and it is substantial):** (1) escalation ACROSS channels
  2-5 under continued stuckness -- unbuilt, and biologically unsupported per the 2026-09-01
  synthesis, so it should be carried as a known gap; (2) the false-bottom ECOLOGY requirement and
  its organism-level DVs, which MECH-343's proposal-entropy framing does not supply; (3) the
  trigger-selectivity assertion (unresolvedness, not near-tie uncertainty), which is precisely
  where SD-061's built detector does NOT match and which is the sharpest new content in the claim.
- **Reverse-deps needing repointing:** I checked `grep -n "MECH-527" claims.yaml` -- **none.**
  MECH-527 is 4 days old (registered 2026-09-01) and nothing depends on it, so the merge is
  cheap now and gets more expensive with every week it waits. `depends_on` edges pointing OUT of
  MECH-527 (MECH-440/313/482/314b/314c) are all "distinguished-from" annotations and are unaffected.
- **Also owed regardless of the merge decision** (all three from the commissioned synthesis, none
  yet applied): rename toward Variable Neighborhood Search framing; soften "attractor escape" to
  "variability injection under stuckness" pending evidence; and resolve the MECH-482 trigger
  mismatch. The synthesis calls the third "cheap and [it] should happen before any falsifier is
  designed".

**depends_on additions:**
- `MECH-343` -- the widening-under-stall claim this restates one channel of. **Required**; without
  it the duplication is invisible from either block.
- `SD-061` -- the built detector + regulator that is MECH-527's channel-1 substrate and its
  best-fitting (though 50% wrong-signed) trigger.
- `ARC-128` -- the termination-taxonomy umbrella MECH-497/498 both instantiate; MECH-527 is the
  escalate-before-disengaging member and is currently the only one of the four not attached to it.
- `MECH-080` -- the pathological absence of this mechanism (OCD attractor lock-in, "normal signals
  cannot trigger basin exit"), which supplies an independent clinical falsifier route.
- `Q-080` -- the MVT/foraging effort-dissociation environment (built 2026-07-09), cited by
  MECH-498 as an existing asset and a candidate host for a delayed-return false bottom.

**GOVERNANCE FLAG:** `stale_note` -- MECH-527's `notes` state "the above-action-level perturbation
channels and the false-bottom ecology do not [exist] -- DO NOT queue an experiment against this
until both exist" and that the lit-pull "SHOULD widen its target". Both are out of date. SD-061
(detector + proposal-entropy regulator) is `implemented_pending_validation` and was exercised by
V3-EXQ-694 on 2026-06-19; the widened lit-pull ran 2026-09-01 (the day the claim was registered)
and delivered three named revisions plus a finding that escalating breadth is biologically
unsupported. `evidence: []` in the claim block while `claim_evidence.v1.json` shows 4 lit entries
at `lit_conf 0.89`. The DO-NOT-QUEUE instruction is still substantially correct for the residual
(channels 2-5, the ecology) but is being justified by a premise that no longer holds, which is
how a claim gets parked for the wrong reason.

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-527 partially duplicates MECH-343/SD-061 with
no cross-reference in either direction, and is currently `substrate_conditional` on a premise the
substrate contradicts for its built leg. Requested decision: accept or reject the partial-absorption
proposal above, and apply the three revisions the commissioned 2026-09-01 synthesis owes this claim
(rename toward VNS; soften "attractor escape" per Neuringer 2001, where variability rose while the
rank ordering of responses was PRESERVED -- added variation, not relocation; and resolve the
MECH-482 trigger mismatch, which the synthesis calls cheap and pre-falsifier). Raising this now is
deliberate: the claim has zero reverse-deps at 4 days old, and the merge cost only rises.

**GOVERNANCE FLAG:** `promotion_review` (low priority, informational) -- V3-EXQ-694
(`v3_exq_694_sd061_difficulty_gated_proposal_entropy_readiness_20260619T224714Z_v3.json`) is
`outcome: PASS`, is in `reviewed_run_ids`, and carries `claim_ids: []`. It is the only exercise of
the SD-061 substrate and its entropy result (ON-arm `first_action_entropy` fell -0.0812/-0.0734/
-0.0953 on 3/3 seeds while control drift was mixed in sign) is load-bearing for MECH-343 and now
for MECH-527. It is currently attributable to neither. MECH-343's `what_would_answer` already
carries the numbers by hand as a "PRIOR TO CARRY IN" -- which works, but means the index shows
MECH-343 with 0 experimental entries while a directly relevant measured prior exists.

## SOLO REPORTS (appended as they land; verbatim agent output)

---

<!-- S_MECH-485 appended 2026-09-04T21:22:55Z -->
## G14 -- MECH-485 predicted-harm/confidence threshold-gated triage  (agent report)

### Group preamble
- **Solo note:** this claim had no group-mate because its only natural partner, `Q-090`, was drafted alongside it in the same 2026-08-07 staging file and *its* draft WAS applied on 2026-08-09 -- `Q-090` already carries a `what_would_answer` in live `claims.yaml`, so it is out of the campaign's "currently lacking `what_would_answer`" population. MECH-485 is the orphaned half of that pair. The cross-claim mandate therefore reduces to one cross-reference, handled inline below: MECH-485's falsifier must not re-derive Q-090's, and Q-090's live text already points back at MECH-485 for its inherited precondition -- which is currently a **dangling pointer**, because the text it points at does not exist. Fixing MECH-485 repairs Q-090 too.
- **`human_review_note` in the loop-branch copy:** **none present.** The loop-branch copy at `prior/MECH-485_loopbranch.yaml` is field-for-field the same block as live `claims.yaml` (id/title/claim_type/subject/polarity/status/live_status/epistemic_category/implementation_phase/version_relevance/registered_utc/depends_on/location/source/notes/evidence) -- no `human_review_note`, no `what_would_answer`, nothing to quote.

---

### MECH-485 -- "A single predicted-harm/success magnitude with an associated confidence (epistemic_deficit) term, computed from E2/E3 forward rollouts, is threshold-gated into three distinct consumers..."

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`**, unchanged. The mechanism has never been exercised because three of its five preconditions still have no substrate at all; the one that *has* landed since (the confidence half) landed default-off and with its own validation still owed, which strengthens rather than weakens the blocked reading.

**Extracted from:** the 2026-08-07 staged draft recovered at `prior/MECH-485_staged_20260807.md` ("DRAFT 1 -- `MECH-485`"), which itself extracted from the claim's own `notes` (Addendum 5 synthesis; the "DO NOT build ahead of (a)/(b)/(c)" paragraph) and from `INV-012`'s `what_would_answer` LEG 0 / LEG 3. **Not re-invented.** Every structural element below -- the (A)/(B) split, the five inherited preconditions, the sixth magnitude-x-confidence dissociability guard, the three confirming signatures, the three named falsification routes with distinct remedies, and the "order of attack" tail -- is the 2026-08-07 text. What changed is listed under Currency check and is marked inline in the draft with `[updated 2026-09-04]`.

**Currency check** (every substrate/run reference in the 2026-08-07 text re-verified against live trees today; `REE_assembly` at `dc14195bf`, `ree-v3` at `f22d65c`):

| Precondition / reference | 2026-08-07 said | Verified 2026-09-04 | Delta |
|---|---|---|---|
| (1) Leg 0 / `MECH-439` conversion ceiling | `ceiling_decision: exhausted`, no differentiated E3 candidates | still `ceiling_decision: exhausted`, `status: candidate`, `epistemic_category: standard`, `assembly_status: in_progress`, `live_status` re-stamped `as_of 2026-09-01` | **unchanged -- still unmet** |
| (2) magnitude half: `predicted_harm_delta` | declared line 111, assigned line 665, **zero readers** | still exactly 2 sites in the canonical tree (`ree_core/pfc/e2_escape_affordance_linker.py:111` and `:665`); `/usr/bin/grep -rn predicted_harm_delta --include="*.py"` over `ree_core/`, `tests/`, `experiments/` returns **no reader**. (The other 6 repo hits are stale copies inside `ree-v3/.claude/worktrees/{keen-elion-70debb,zen-jang-c29713,focused-ishizaka-c3cba9}`, not the canonical tree.) | **unchanged -- still write-only.** But see the NUANCE below, which is new and was NOT in the 2026-08-07 finding |
| (2, nuance) the `harm_delta` *head* | not separately examined | the head IS trained (targets built at `:594-598`) and IS read -- but only at `:448-449`, inside the relief readout, as `clamp01((predict_head("harm_delta") + predict_head("threat_termination")) / 2)`. So a predicted-harm quantity reaches a consumer **only after being averaged with an unrelated head and clamped to [0,1]**. No consumer anywhere sees a standalone predicted-harm magnitude. | **NEW, and it sharpens the precondition rather than clearing it** |
| (3) confidence half: `epistemic_deficit` | "zero hits anywhere in `ree_core/`"; MECH-482/483 unbuilt | **BUILT.** `ree_core/policy/epistemic_deficit.py` exists (SD-102, wired 2026-08-29 ree-v3 `b69a1b8`, readiness rebuild `bd58ab6` 2026-09-01); 125 hits in `ree_core/`; contract suites `tests/contracts/test_mech_482_epistemic_deficit_accumulator.py` and `test_sd_epistemic_deficit_multitarget_readiness.py` (23); driver `experiments/v3_exq_964_mech482_epistemic_deficit_validation.py` | **CHANGED -- the single biggest currency finding of this pass** |
| (3, knob) | n/a | **default-off**: `curiosity_learning_progress_source: Literal["broadcast","epistemic_deficit"] = "broadcast"` (`ree_core/utils/config.py:4576-4578`); `"broadcast"` is documented bit-identical | built != armed |
| (3, validation) | n/a | `V3-EXQ-964` (`..._20260829T215030Z_v3.json`) ran **FAIL**, `evidence_direction: non_contributory` -- governance `governance-20260830-0630` ratified the autopsy: C2 was **structurally unsatisfiable** (per-episode `reset()` keeps `n_targets == 1`, all 32 candidates match it, readout is a CONSTANT vector that cannot move an argmax). Readiness rebuild landed 2026-09-01 (`substrate_queue.json` `sd_epistemic_deficit_multitarget_readiness`, status `implemented_pending_validation`, `ready: false`) behind six no-op-default knobs; it measured FOUR causes of the collapse, two of which the autopsy never named (R3 update/readout frame mismatch, R4 hard-threshold saturation). Its own `validation_owed` field says a NEW-letter 964 successor is required and was **not queued** -- confirmed: `ree-v3/experiment_queue.json` holds only `V3-EXQ-1002`, `V3-EXQ-983a`, `V3-EXQ-993a`. | **confidence half is built-but-unvalidated; MECH-482 itself is still `candidate/v3_pending/substrate_conditional`** |
| (4) leg-1 target pathways | BetaGate takes no harm term; `cancel_window`/`veto_window` zero hits | `ree_core/heartbeat/beta_gate.py`: the string `harm` appears in **no** method signature or body (checked against the full `def` inventory: `is_elevated`, `refractory_remaining`, `committed_run_length`, `apply_refractory`, `note_closure_coupled_elevation`, `note_closure_commit_intent`, `elevate`, `release`, `propagate`, `should_admit_elevation`, `receive_hippocampal_completion`, `get_held_state`, `get_state`, `reset`). `cancel_window` / `veto_window` / `cancel_open`: **0 hits each** in `ree_core/` | **unchanged -- still unmet** |
| (5) leg-3 retention mechanism | "does not exist in any form; deliberately NOT registered pending lit-pull" | **REGISTERED** as `MECH-487` (title: bounded, provenance-tagged retention buffer for rejected/uncommitted E3 candidates, riding on the MECH-094 gate under the MECH-322 template), already in this claim's `depends_on` with an explanatory comment, and carrying its own `what_would_answer`. Still `candidate` / `substrate_conditional`. **Still unbuilt**: `retained_alternative`, `retain_candidate`, `rejected_candidate`, `counterfactual_retention`, `candidate_retention` -- 0 hits each in `ree_core/`; `MECH-487` appears in no `ree_core/`, `experiments/` or `tests/` file. | **PARTIALLY CHANGED -- registered, not built. The claim's own `notes` are now internally inconsistent**: the "LOAD-BEARING UNREGISTERED DEPENDENCY" paragraph still says the mechanism is deliberately unregistered, while `depends_on` already carries MECH-487 saying it was registered on the same day |
| `INV-012` LEG 0 / LEG 3 cross-reference targets | LEG 3 "added later same day" | both still live in `INV-012.what_would_answer` (LEG 0 at "CURRENTLY UNMET"; LEG 3 present, with its own four-part non-degeneracy precondition and its confabulation-bound). `INV-012` is `status: active`, `epistemic_category: substrate_conditional`, and `depends_on` now carries BOTH `MECH-485` and `MECH-487` | **cross-references still valid; LEG 3 is now better served by MECH-487 directly** |
| Reverse deps (fan-in 3) | n/a | confirmed exactly three: `INV-012` (active/substrate_conditional), `Q-090` (candidate/substrate_conditional), `MECH-487` (candidate/substrate_conditional) | confirmed |
| Own evidence | n/a | `evidence: []`; no manifest under `evidence/experiments/` references MECH-485 | never run |

**Net currency verdict:** one of the five preconditions moved (the confidence half went from "does not exist" to "built, default-off, validation owed"); one moved halfway (leg-3 retention went from "unregistered" to "registered as MECH-487, still unbuilt"); three are byte-for-byte unchanged. The disposition does not move: **the claim is still untestable by construction, not merely unfavoured.**

**epistemic_category (proposed):** `substrate_conditional` -- **no change.** This is `substrate_conditional` and not `substrate_ceiling` on the ARC-062/ARC-063 test: the mechanism has never been exercised at all (leg-1 wiring and leg-3 retention have no code), so there is no built-and-exercised pipeline whose signal a downstream mechanism could be absorbing. The existing `live_status.reading: candidate/v3_pending/substrate_conditional` marker is consistent and should be re-stamped `as_of: '2026-09-04'` with the precondition-(3) movement noted.

**Draft `what_would_answer`:**

> Answered by ABLATING THE FAN-OUT, once the substrate exists: does routing
> one magnitude+confidence signal to three regime-specific consumers do
> anything a single graded response would not?
>
> Two separable assertions, which can fail independently:
> (A) SHARED SOURCE -- the three legs are driven by the SAME predicted
> magnitude + confidence pair, not by three independently-computed triggers
> that merely co-vary. This is Addendum 5's synthesis; Addendum 2's own
> earlier reading (three "functionally distinct consumers" of shared
> representational substrate) is the competing hypothesis, not a strawman.
> (B) DIFFERENTIATED RESPONSE -- the fan-out is genuinely regime-gated, not
> one uniform response whose intensity happens to scale with magnitude.
>
> NON-DEGENERACY PRECONDITION (five parts; as of 2026-09-04 ONE is partially
> met and FOUR are unmet -- this claim is untestable by construction, not
> merely unfavored):
> (1) Leg 0 cleared -- E3 must select among genuinely graded, differentiated
> candidates, or there is nothing for a magnitude to be computed OVER. See
> INV-012's own what_would_answer LEG 0 for the full statement and the
> MECH-439 `ceiling_decision: exhausted` evidence; do NOT re-derive it here.
> Re-verified 2026-09-04: MECH-439 is still `exhausted`, `live_status`
> re-stamped 2026-09-01. UNMET.
> (2) The magnitude half must exist AND be consumed AS A MAGNITUDE.
> `predicted_harm_delta` (ree_core/pfc/e2_escape_affordance_linker.py:111,
> assigned :665) is the nearest existing forward-rollout predicted-harm
> quantity, and a grep over ree_core/, tests/ and experiments/ still finds
> ZERO readers of that field (re-verified 2026-09-04; unchanged since
> 2026-08-07). [updated 2026-09-04] The underlying `harm_delta` HEAD is not
> dead -- it is trained (:594-598) and read at :448-449 -- but only inside
> `clamp01((harm_delta + threat_termination) / 2)`, so the one path by which
> a predicted-harm prediction reaches any consumer destroys its identity by
> averaging it with an unrelated head and clamping it to [0,1]. A signal
> that is only ever consumed pre-averaged cannot gate three regimes at two
> cut-points, and a magnitude nothing consumes cannot gate anything at all.
> UNMET -- and note the remedy is now narrower than "wire it up": the field
> needs a consumer that sees it UNAVERAGED.
> (3) The confidence half must exist. [updated 2026-09-04 -- this is the one
> precondition that has MOVED since the original draft.] It now does:
> MECH-482's EpistemicDeficitAccumulator is BUILT and wired
> (ree_core/policy/epistemic_deficit.py, SD-102, ree-v3 b69a1b8 2026-08-29;
> multi-target readiness rebuild bd58ab6 2026-09-01), with 23 contracts. But
> it is NOT USABLE for this claim yet, for two independent reasons that must
> both be discharged before any MECH-485 run is scored: (a) it is DEFAULT-OFF
> -- `curiosity_learning_progress_source` defaults to `"broadcast"`, which is
> documented bit-identical, so an experiment that does not explicitly arm
> `"epistemic_deficit"` is testing nothing; (b) its own validation is OWED
> and its first attempt was structurally void -- V3-EXQ-964 (2026-08-29) is
> FAIL / non_contributory because the per-episode reset kept `n_targets == 1`
> and the per-candidate readout was a CONSTANT vector that cannot move an
> argmax, and the 2026-09-01 readiness build found four causes of that
> collapse (two of them not named by the autopsy) and explicitly recorded
> that a new-letter successor is required and was not queued. So the
> confidence term exists as code and does NOT yet exist as a discriminating
> quantity. Any MECH-485 run must gate on the readiness statistics that build
> exposed -- `n_targets >= 2`, `last_readout_deficit_range > 0`,
> `last_lp_dev_range > 0` -- BEFORE reading a verdict, or it will silently
> reproduce 964's vacuity one level up. PARTIALLY MET.
> (4) The leg-1 target pathways must accept a predicted-harm input.
> BetaGate (ree_core/heartbeat/beta_gate.py) exists but takes no harm or
> predicted-harm term in any method signature or body (re-verified against
> its full `def` inventory, 2026-09-04); MECH-138's cancel-window has no
> substrate presence at all (`cancel_window`/`veto_window`/`cancel_open`:
> zero hits in ree_core/). So leg 1 is still a claim about a wire that does
> not exist, between an endpoint that exists and one that does not. UNMET.
> (5) Leg 3's retention mechanism must exist. [updated 2026-09-04] It is now
> REGISTERED -- MECH-487, the bounded provenance-tagged retention buffer for
> rejected/uncommitted E3 candidates, riding on the MECH-094 imagination/
> reality write gate under the MECH-322 audited-exception template -- and is
> already in this claim's depends_on. It is NOT BUILT: no retention or
> persistence of losing E3 candidates exists in ree_core/ (five distinct
> name-shapes checked, zero hits each; MECH-487 appears in no substrate,
> experiment or test file). Cross-reference MECH-487's own what_would_answer
> and INV-012's LEG 3 for what the mechanism must do and for the
> confabulation bound it must respect; do NOT re-derive either here. UNMET.
> NOTE for whoever next edits this claim's `notes`: the "LOAD-BEARING
> UNREGISTERED DEPENDENCY" paragraph there is now stale -- it says the
> retention mechanism is deliberately unregistered pending a lit-pull, which
> that same lit-pull discharged on 2026-08-07 by registering MECH-487.
>
> PLUS one non-degeneracy guard specific to THIS claim rather than
> inherited: (6) MAGNITUDE AND CONFIDENCE MUST BE MEASURABLY DISSOCIABLE in
> the test distribution. The claim asserts a two-dimensional gate
> (magnitude x confidence) fanning into three regimes. If confidence is in
> practice a monotone function of magnitude -- confidently-predicted harms
> are also large ones -- the gate collapses to one dimension, only two
> regimes are ever occupied, and leg 2 (orient/survey) is never entered.
> A run under those conditions would report "no three-way structure" for a
> reason that has nothing to do with whether the claim is true. Require a
> reported joint distribution over (magnitude, confidence) with populated
> off-diagonal cells -- specifically high-magnitude/low-confidence, which
> is the ONLY cell that distinguishes leg 2 from leg 1 -- before any
> verdict is read. [updated 2026-09-04] This guard is now the DIRECT
> generalisation of V3-EXQ-964's confirmed failure, not a hypothetical: 964
> was void precisely because the confidence-side readout was constant across
> candidates. A constant confidence term populates exactly one column of this
> joint distribution, so precondition (6) and precondition (3b) are the same
> failure at two scales and must be reported together.
>
> CONFIRMING signature (all three, not any one):
> (i) FAN-OUT IS LOAD-BEARING -- collapsing the three consumers into a
> single graded response (interrupt probability scaled by magnitude, no
> orient/survey regime, no retention) degrades performance on at least two
> of the three legs' own outcome metrics relative to the intact pipeline.
> Scale the PASS gate on the SD of the paired per-seed delta (>= 2 SD) with
> an absolute floor, not on a raw difference.
> (ii) DOUBLE DISSOCIATION OF CUT-POINTS -- sweeping the interrupt
> threshold moves the leg-1/leg-3 boundary WITHOUT moving the leg-2
> boundary, and sweeping the epistemic_deficit threshold moves the leg-2
> boundary WITHOUT moving the leg-1/leg-3 boundary. This is what separates
> "one signal, independently-placed cut-points" from "three signals": three
> independent triggers would not show each sweep confined to its own
> boundary.
> (iii) SHARED SOURCE IS SUFFICIENT -- substituting a leg-specific,
> independently-computed trigger for the shared signal in any single leg
> yields no improvement over the shared signal on that leg's own metric.
>
> FALSIFYING, in three distinct ways with three distinct remedies:
> -- THREE-SIGNAL reading: the shared signal underperforms a leg-specific
> trigger in at least one leg by a margin that survives the other legs
> being held intact. Then the legs need different COMPUTATIONS, not
> different thresholds on one, and Addendum 2's pre-synthesis reading was
> right. Remedy: demote MECH-485 from a unity claim to "three mechanisms
> sharing E2/E3 forward-prediction substrate" and keep each leg. NOTE this
> is a partial falsification -- MECH-485 can fail AS A UNITY CLAIM while
> every individual leg survives, and that outcome must not be recorded as
> refuting the legs.
> -- DECORATIVE FAN-OUT: a single graded response reproduces the intact
> pipeline's benefit on all three legs' metrics. Then threshold-gating is
> a description of the response curve, not a mechanism, and (B) is false
> even if (A) holds. Remedy: retire the three-consumer structure, keep the
> shared-signal claim.
> -- OVER-CONSTRAINED SCALE: no placement of the two cut-points leaves all
> three legs simultaneously non-degenerate -- every setting at which leg 1
> fires usefully starves leg 3 of retainable candidates, or vice versa.
> This is Q-090's independent-criterion reading generalized to the whole
> pipeline, and it falsifies the "one scale partitioned at two cut-points"
> architecture specifically. Remedy: give the legs independent admission
> criteria, which is exactly what Q-090 asks about for leg 3 -- see Q-090's
> own what_would_answer, which is already written and which inherits this
> precondition block rather than restating it.
>
> ORDER OF ATTACK, if this is ever built. [updated 2026-09-04 -- the
> ordering has CHANGED, because precondition (3) moved.] Precondition (2) is
> still the cheapest and is still independently useful: giving
> `predicted_harm_delta` a consumer that reads it UNAVERAGED is a smaller
> step than anything else here, and its result is informative regardless of
> MECH-485's fate. Precondition (3) is now second rather than blocked --
> what it needs is not a build but the OWED V3-EXQ-964 successor (new
> letter, readiness config armed on both arms, gated on n_targets >= 2 and a
> non-constant per-candidate readout before C2 is scored), which the
> 2026-09-01 readiness build recorded as required and did not queue.
> Preconditions (4) and (5) remain the expensive ones and are unchanged. Do
> not treat the whole pipeline as one indivisible build.

**Proposal sketch:** none -- disposition (c) does not mint. Four of the six preconditions are unmet and the fifth is only partially met, so any `EXP-####` would describe a run nothing can execute. (The one runnable adjacent item -- the V3-EXQ-964 successor -- belongs to MECH-482 / `sd_epistemic_deficit_multitarget_readiness`, not to MECH-485, and is flagged separately below rather than minted here.)

**depends_on additions (if any):** carry forward the 2026-08-07 proposal, unchanged and still valid --
1. **Add `MECH-094`** -- `MECH-094  # imagination/reality write gate -- leg 3's retained content must stay provenance-distinguishable`
2. **Add `MECH-322`** -- `MECH-322  # the one bounded, audited exception through MECH-094 -- template shape any leg-3 retention must follow`
Both are named as load-bearing by `INV-012` LEG 3, and MECH-487's own title now explicitly rides on the MECH-094 gate under the MECH-322 template, which makes the edge more clearly warranted today than it was on 2026-08-07. **Not proposed:** a reverse edge to `INV-012` (it already depends on MECH-485; the reverse would make the graph cyclic) -- cross-reference in text instead.

---

**GOVERNANCE FLAG (1 of 2):** `evidence_discrepancy`

> **The 2026-08-09 governance note records an application that never happened, and the same commit destroyed the source text.**
>
> `MECH-485.notes` ends with: *"[2026-08-09 governance, GFLAG-0009 resolution]: applying the what_would_answer drafted 2026-08-07 (evidence/planning/thought_digestion_staged_2026-08-07_mech485_q090.md, staged but never applied) verbatim..."*
>
> That application did not occur. Verified:
> - **`REE_assembly` `d8ccbce59eab574d76b747d060abdf1bbc4edc19`** ("governance: cycle 2026-08-09 -- resolve 8 open governance flags (GFLAG-0004/0005/0008/0009/0014/0015/0018)", 2026-08-09T06:26Z, author `nooarche`). Reading `git show d8ccbce59e:docs/claims/claims.yaml`, the MECH-485 block at that commit has fields `title, claim_type, subject, polarity, status, live_status, epistemic_category, implementation_phase, version_relevance, registered_utc, depends_on, location, source, notes, evidence` -- **no `what_would_answer`**. The note asserting the application is itself one of that commit's insertions.
> - **The field is still absent today** at `REE_assembly` `dc14195bf` (verified by loading `claims.yaml` and checking the parsed block's keys). `evidence: []`.
> - **The same commit DELETED the source.** `d8ccbce59e` removed `evidence/planning/thought_digestion_staged_2026-08-07_mech485_q090.md` (322 lines), which had been added by `4d0371304c` ("thought-digestion: STAGE what_would_answer drafts for MECH-485 + Q-090 (headless chip, not applied)"). So the staging file was destroyed in the same commit that claimed to have consumed it, leaving no in-tree copy of the drafted text.
> - **The sibling from the same staging file WAS applied.** `Q-090` carries a live `what_would_answer` whose opening is the staged Draft-2 text (with a lit-pull revision visible at "THE READINGS ... this claim's targeted lit-pull"). So this is not a wholesale non-application of GFLAG-0009: **one of the two drafts landed and the other was silently dropped**, which is exactly why nothing downstream caught it.
> - **Consequential, not cosmetic.** `Q-090`'s live falsifier says *"(1) INHERITED -- everything MECH-485's own what_would_answer requires ... Do NOT re-derive it here; see MECH-485."* That is a pointer into a field that does not exist -- Q-090's non-degeneracy precondition is currently unresolvable as written. Applying the draft above repairs Q-090 as a side effect.
>
> **Requested action:** raise as `evidence_discrepancy` (`stale_note` would understate it -- the note asserts a completed governance action, not merely an out-of-date fact). Resolution should (a) apply the re-derived `what_would_answer` above, (b) correct the 2026-08-09 notes paragraph to record that the application was recorded but not performed and was completed on the resolution date, naming `d8ccbce59e`, and (c) re-stamp `live_status.as_of` to the resolution date.

**GOVERNANCE FLAG (2 of 2):** `stale_note`

> **The `predicted_harm_delta` dead-readout callout, carried in MECH-485's own notes since 2026-08-09, is still true but is now stated too weakly -- and it belongs to SD-059/MECH-358, not here.**
>
> The 2026-08-09 note says `predicted_harm_delta` "is computed and never consumed anywhere in ree_core -- benign-by-design or worth a substrate check, not adjudicated here." Re-verified 2026-09-04 at `ree-v3` `f22d65c`: the **field** still has exactly one write and zero reads in the canonical tree. But this pass additionally established that the **head** behind it is trained (`e2_escape_affordance_linker.py:594-598`) and IS read at `:448-449` -- only ever as `clamp01((harm_delta + threat_termination) / 2)`. So the accurate statement is not "a trained output nothing has ever checked" but "a predicted-harm prediction that no consumer can see unaveraged". That distinction changes the remedy: the fix is not merely "wire `predicted_harm_delta` to something" but "expose it to a consumer that does not pre-average it", and it is the cheapest single step toward MECH-485 precondition (2). Recommend routing to a substrate check against `SD-059`/`MECH-358` (the escape-affordance linker's own claims), where it has an owner, rather than leaving it as an unadjudicated aside in MECH-485's notes.
>
> **Second, separable item, surfaced by the same pass and stated here so it is not lost:** `substrate_queue.json` `sd_epistemic_deficit_multitarget_readiness` is `implemented_pending_validation` / `ready: false`, and its 2026-09-01 `implementation_log` entry records `validation_owed`: a **new-letter V3-EXQ-964 successor** arming the readiness config on both arms and gating on `n_targets >= 2` plus a non-constant per-candidate readout before C2 is scored -- explicitly "NOT queued by this build session". Confirmed still not queued: `ree-v3/experiment_queue.json` contains only `V3-EXQ-1002`, `V3-EXQ-983a`, `V3-EXQ-993a`. This is MECH-482's owed work, not MECH-485's, but MECH-485's precondition (3) cannot clear until it runs, so it is the binding item on this claim's critical path. Route to `/queue-experiment` under MECH-482 / SD-102.

---

<!-- G10 appended 2026-09-04T21:25:35Z -->
## G10 -- self-attribution comparators / multi-source dynamics  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the brief pairs them because ARC-061 `depends_on` SD-047 (6.00; cancellation/comparators/reafference overlap) -- SD-047 is the Level-1 calibration substrate whose enriched causal background is supposed to make ARC-061's motor comparator honestly testable. **My own view sharpens this into a dependency that has already been discharged and returned a negative.** SD-047 is not "pending" for ARC-061; it was built (2026-05-03), validated for readiness (V3-EXQ-509 PASS), and then exercised against its two named consumers three times -- V3-EXQ-510 (MECH-095, 4-arm sweep, 2026-05-04), V3-EXQ-529 (MECH-098, 2026-05-06) and V3-EXQ-741 (MECH-095, guarded test-bed, 4 arms, 2026-07-12). All three returned null-or-negative. So the group's real content is not "what would test these" but "the test ran, the pre-registered falsifier branch fired, and neither block absorbed the result."

- **(i) same-claim / merge candidates:** **No -- these two are not the same claim at different granularity and must not be merged.** ARC-061 is a taxonomic architectural_commitment (one motif, three levels); SD-047 is an environment design_decision. They are correctly separate. **But there are two real granularity findings inside the group:**
  1. **ARC-061 under-enumerates its own family.** It names three levels (MECH-095 motor / ARC-058 interoceptive / MECH-094 propositional) and omits the **encoder-level reafference comparator** -- MECH-098 (`encoder.reafference_cancellation`, `z_world_corrected = z_world_raw - ReafferencePredictor(z_world_raw_prev, a_prev)`), which is *live in code* at `ree-v3/ree_core/latent/stack.py:42` (`class ReafferencePredictor`), gated by `reafference_action_dim > 0`, and is by far the most-tested member of the motif (18 genuine exp entries, exp_conf 0.438). SD-047's own **title** names MECH-098 as a co-beneficiary, so the omission is visible from inside the group. This is a **PROPOSE-ONLY (g)-style narrowing/extension**, not a merge: adding MECH-098 as an explicit fourth level (`encoder / perspective-shift`, timescale: per-tick, forward model: `ReafferencePredictor`, authorship tag: residual after perspective-shift subtraction) would make the family claim match the substrate. Reverse-deps needing repointing: none (ARC-061 has fan-in 0; SD-047's only reverse-dep is ARC-061 itself).
  2. **ARC-061's Level-1 operationalisation is specified in a retired architecture.** Its `functional_restatement` and its backing doc both define Level 1 as `E2_harm_s(z, a_actual) - E2_harm_s(z, a_cf)` -- a **two-pass counterfactual gap** -- and the doc says outright "the counterfactual branch is the SD-003/SD-029 pipeline". SD-003 was **superseded 2026-04-18** (by MECH-256 + SD-029) precisely because the 2026-04-18 14-entry literature synthesis found the **single-pass** comparator (Frith 2000, Shergill 2003, Blakemore 1998) to be the biologically-evidenced mechanism, not the two-pass counterfactual. ARC-061 was registered 2026-05-03, *after* that supersession, and still carries the two-pass framing. SD-029 (`residual = observed - predicted`, single-pass on z_harm_s) and SD-031 (single-pass on z_world) are the live instantiations. See SD-003's own already-drafted `what_would_answer` -- it states this in terms: "SD-003 is superseded ... THE LIVE FALSIFIER IS SD-029'S". **ARC-061's Level-1 row should be re-pointed to the single-pass family and should not re-derive that history.**

- **(ii) contradictions / undercut premises:** **Yes -- one direct, one structural.**
  - **Direct:** SD-047's own pre-registered `Falsifiable:` clause says "if flat-failure across all arms, route MECH-095 from substrate_ceiling to substrate_conditional (Woo/Spelke branch)". V3-EXQ-510's manifest literally records `"outcome_branch": "WOO_SPELKE"` with `n_c1 = n_c2 = n_c3 = 0` in **all four** arms. The consequent was **not applied**: `substrate_queue.json` records "MECH-095 epistemic_category reclassification to substrate_conditional **deferred pending further analysis**", and it has stayed deferred for four months. See GOVERNANCE FLAG 2.
  - **Structural:** ARC-061's whole Level-1 leg presupposes SD-047 supplies an adequate exafference background. V3-EXQ-741's confirmed autopsy states the opposite as its finding -- "SD-047's world-caused drift is **not a structurally-distinct OTHER**, so the env cannot make the comparator load-bearing and the baseline pre-empts it". **SD-047's outcome undercuts ARC-061's premise**, and it does so from *inside* the dependency edge the brief grouped them on.

- **(iii) shared falsifier:** **Yes, and it is already written -- do not re-derive it.** MECH-095's `what_would_answer` contains the group's shared **NON-DEGENERACY PRECONDITION (HARD)**: *a test of the motor comparator is informative only on a substrate that supplies a genuine second agent -- a structurally-distinct OTHER whose actions are causally attributable separately from ambient world drift*, together with the two guards any valid run must report (probe-partition non-degeneracy AND self/world training-label balance, both mirrored from V3-EXQ-741) and the explicit refusal of any further single-agent SD-047 letter. **Both G10 claims cross-reference that block for their Level-1 / consumer-side precondition.** Level 2 and Level 3 have their own already-drafted blocks that ARC-061 should point at rather than restate: ARC-058's `what_would_answer` (three-arm shared-trunk-vs-independent arbitration, plus its finding that *no manifest in the corpus carries `claim_ids` including ARC-058* -- the arbitration has never been run) and MECH-094's `what_would_answer`, which carries the explicit instruction **"DO NOT RE-DERIVE ELSEWHERE. This is the group's shared write-gate condition."**

- **(iv) cross-cutting finding:** **The "add agent-independent stochastic noise so the comparator has an exafference background" design strategy has now been executed twice, independently, at two different levels, and produced a null both times.** Level 1 = SD-047 (env noise: AR(1) weather field + Poisson transients + drift sources); Level 2 = SD-048 (interoceptive noise: autonomic + sensitisation + fatigue). Both implemented the same day (2026-05-03), both built to the same 1:1-2:1 calibration band, both validated with the same pre-registered 4-arm Asai sweep (OFF / 0.25x / 1.0x / 4.0x). Outcomes:

  | consumer test | claim | date | outcome / direction |
  |---|---|---|---|
  | V3-EXQ-509 | SD-047 (readiness only) | 2026-05-03 | PASS / supports |
  | V3-EXQ-510 | MECH-095 + **SD-047** | 2026-05-04 | FAIL / MECH-095 mixed, **SD-047 weakens**, branch `WOO_SPELKE` |
  | V3-EXQ-529 | MECH-098 (on SD-047) | 2026-05-06 | FAIL / **weakens** |
  | V3-EXQ-741 | MECH-095 (guarded test-bed) | 2026-07-12 | non_contributory / 1st **valid** ceiling hit |
  | V3-EXQ-512a | SD-048 | 2026-05-04 | **non_contributory** |
  | V3-EXQ-902 | SD-048 | 2026-08-09 | FAIL / **non_contributory** |

  Two independent substrates, four independent consumers, zero positive discrimination. **This is a finding about the design hypothesis, not two coincidences:** adding *unstructured, agent-independent* stochastic variation does not create the contrast a reafference comparator needs, because such variation is not a structurally-distinct causal *source* -- it is background. That is exactly the reading V3-EXQ-741's autopsy reached for Level 1, and SD-048's twin nulls are the independent replication of it at Level 2. **Mutual-confound consequence:** a null on ARC-061 as a whole is uninterpretable, because two of its three levels have never been validly exercised (Level 1 exercised only to a confirmed ceiling; Level 2's ARC-058-vs-ARC-033 arbitration never run at all) while Level 3 alone is `stable`/confirmed. A conjunction test over 1 live and 2 unexercised legs is vacuous by construction.

- **Currency findings (stale notes, landed blockers, unreviewed results):**
  1. **ARC-061 notes: "Level 1 (MECH-095) substrate_ceiling, SD-047 pending" -- STALE on both halves.** SD-047 is not pending: implemented 2026-05-03, `substrate_queue.json` status `implemented`, ready `True`. And MECH-095's ceiling is no longer mapped to SD-047 at all -- it was re-pointed 2026-07-12 to `multi_agent_ecology_v5:MAE-3`, and MECH-095's `implementation_phase` was **reassigned v3 -> v5**.
  2. **ARC-061 notes: "Level 2 (ARC-058) V3-tractable but no calibration SD" -- STALE, and self-contradictory within the same field.** Two paragraphs earlier the same `notes` block names SD-048 as the Level-2 calibration SD. SD-048 is implemented (2026-05-03), and `substrate_queue.json`'s SD-048 entry lists `unblocks_claims: ["ARC-058", "ARC-033", "ARC-061"]` -- ARC-061 by name.
  3. **ARC-061's backing doc `docs/architecture/reafference_comparator_family.md` is stale in the same way** (last updated 2026-05-03): "Gap 1: Level 2 substrate enrichment SD (highest priority) -- Level 2 has no SD claim ... Suggested claim: `SD-NNN` (`body.interoceptive_noise_dynamics`)". That claim exists: it is SD-048, `subject: body.interoceptive_noise_dynamics`, registered the same day. The doc also still records MECH-095 as `status: active` (it is `candidate` since GOV-CEIL-1, 2026-07-11).
  4. **ARC-061 carries NO `implementation_phase`** while depending on MECH-095 (`v5`), ARC-058 (`v3`/`v3_pending`), SD-047 (`v3`) and SD-048 (`v3`/`v3_pending`), and its own designated closure node (doc Gap 2 / Gap 3, cross-level interaction) is explicitly V4/V5 territory. Per phase-follows-dependency this should be `v5`. See GOVERNANCE FLAG 5.
  5. **SD-047 `evidence_quality_note`: "Validation pending: V3-EXQ-509 (substrate-readiness diagnostic; queued) -> V3-EXQ-510 (4-arm sweep...)" -- BOTH RAN, 16 months of registry time ago.** 509 PASS/supports 2026-05-03; **510 FAIL 2026-05-04 with `evidence_direction_per_claim: {"MECH-095": "mixed", "SD-047": "weakens"}` and `outcome_branch: "WOO_SPELKE"`.** The `notes` field repeats the same stale "queued / pending" text.
  6. **SD-047's `live_status.evidence` (as_of 2026-07-11) cites only `v3_exq_509_..._20260503T103241Z_v3`, verdict `supports/PASS`** -- i.e. it records the *readiness smoke* and omits the *behavioural weakens that landed the next day*. The index disagrees in sign: `claim_evidence.v1.json` gives SD-047 `genuine_exp_count: 1`, `genuine_exp_direction_counts: {"weakens": 1}`, `latest_run_id: v3_exq_510_sd047_mech095_live_env_comparator_gap...`, `experimental_confidence: 0.125`, `evidence_quadrant: "plausible_unproven"`. **The readiness PASS is not scored at all.** See GOVERNANCE FLAG 1.
  7. **`substrate_queue.json`'s SD-047 entry still carries `status: implemented`, `ready: True`, `priority: 1`, `unblocks_claims: ["MECH-098", "MECH-099"]`** (MECH-095 was removed 2026-07-11). But MECH-098's own SD-047-substrate test -- V3-EXQ-529, which really does run on the enriched env (`multi_source_dynamics_enabled=True, weather_field_enabled=True, transient_events_enabled=True`, three arms keyed on SD-047 x reafference) -- is **FAIL / weakens**. So SD-047's live queue entry advertises an unblock that its own consumer evidence does not support. See GOVERNANCE FLAG 4.
  8. **No unreviewed-result flag: all of it is already reviewed.** V3-EXQ-509, 510, 741, 047l, 047m, 529, 512a and 902 are all present in `review_tracker.json` `reviewed_run_ids` (510 additionally has a `discussed_experiment_dirs` entry "V3-EXQ-510"). The problem is not unreviewed evidence -- it is **reviewed evidence that never propagated back into the two registry blocks**.
  9. **Methodological caveat on V3-EXQ-510, recorded so a later reader does not over-weight it.** Its only non-degeneracy guard is "condition pool non-empty" (`c*_evaluable = ratio is not None`, driver lines 415-452); there is **no minimum class-count floor**. The agent-caused pool collapses across arms while env-caused rises -- seed 42: `agent_caused` 1410 / 933 / 150 / 85 and `env_caused` 66 / 165 / 376 / 362 for ARM_0/1/2/3 -- so the 1:1-2:1 calibration band is met near ARM_1 and inverts to ~1:2.5 (ARM_2) and ~1:4.3 (ARM_3). This is the same class-imbalance family that later invalidated V3-EXQ-047l (probe saturation) and 047m (training-label saturation). **The conclusion nevertheless survives**, because V3-EXQ-741 carried *both* guards, reported `non_degenerate: true` on all four arms, and reproduced the flat null. Treat 510 as corroborated-by-741 rather than as independently load-bearing.
  10. **A faint non-monotonicity is present in 510 and was never remarked on.** `ratio_agent_over_env` runs 1.145 / 1.159 / 1.206 / 1.193 across ARM_0..ARM_3 -- a shallow inverted-U peaking at ARM_2, the pre-registered Asai shape and the pre-registered peak arm. It is nowhere near the C1 threshold of 1.5, so it changes no verdict, and I flag it only so nobody later mistakes it for a missed signal: the ordering is right and the magnitude is absent, which is a *shallow-slope* reading, not a *no-mechanism* reading.

---

### ARC-061 -- Self-attribution is implemented via a family of forward-model comparators at motor, interocep...

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`** (NOT `substrate_ceiling`): the family claim's distinctive content is the *cross-level* shared signature, no run in the corpus has ever carried `claim_ids` including ARC-061 (`claim_evidence.v1.json`: ARC-061 **absent**), and the substrate its own backing doc designates for that test -- simultaneous activation of all levels with a structurally-distinct OTHER, i.e. `multi_agent_ecology_v5:MAE-1 -> MAE-2 -> MAE-3` -- **does not exist in any form**, so zero non-degenerate attempts are currently possible.

**Extracted from:** the claim's own `functional_restatement` ("Shared diagnostic signature across all three levels: symmetric over/under-attribution errors under substrate miscalibration (Asai 2016 S/N-slope), non-monotonic noise-dependence (Ward 2010 stochastic resonance), and bidirectional surface consequences from single substrate pathology (Jardri & Deneve 2013; Nassar 2021)") plus its backing doc `docs/architecture/reafference_comparator_family.md` sections "Shared diagnostic principles" 1-3 and "Implementation gaps" Gap 2/Gap 3. **Not drafted fresh** -- the three per-level falsifiers already exist and are cross-referenced rather than restated (MECH-095, ARC-058, MECH-094 `what_would_answer`).

**Currency check:** verified against `claims.yaml` live blocks (MECH-095 `candidate`/`substrate_ceiling`/**phase v5**; ARC-058 `candidate`/`v3_pending`, no epistemic_category; MECH-094 `stable`/`standard`; SD-047 `provisional`; SD-048 `candidate`/`standard`/`v3_pending`); `substrate_queue.json` (SD-047 and SD-048 both `implemented`, `ready: True`; SD-048's `unblocks_claims` names ARC-061); `evidence/planning/multi_agent_ecology_v5_plan.md` (MAE-3 `blocked` on MAE-2 on MAE-1; MAE-3's `completion_note` records governance ACTING on the v5 reassignment 2026-07-12); `closure_status.md` line 394 (MAE-3 `blocked`, high); `evidence/experiments/claim_evidence.v1.json` (ARC-061 has no entry); `ree-v3/ree_core/latent/stack.py:42` (`ReafferencePredictor` present, gated on `reafference_action_dim > 0`). Findings 1-4 above are all stale-note findings on this claim or its doc.

**epistemic_category (proposed):** `substrate_conditional`. *(Note for the reviewer: `claim_type: architectural_commitment` would default-INFER `substrate_coherence`. Both suppress promote/demote, so nothing breaks either way, but `substrate_conditional` is the more informative tag here -- it says "waiting on an unbuilt upstream substrate", which is true and actionable, whereas `substrate_coherence` says "this IS the substrate", which is not what ARC-061 asserts. It is explicitly NOT `substrate_ceiling`: ARC-061 has zero banked positive evidence of its own, and the ceiling belongs to its Level-1 dependency, not to it.)*

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** ARC-061 asserts that three (see the note below on four) comparators are **one motif**, not three independent mechanisms. Its distinctive content is therefore **cross-level**, and a test is non-vacuous only if every level it quantifies over is simultaneously live and independently manipulable in the *same* run. Concretely, all four conditions must hold and be reported:
> (1) **Level 1 live** -- for the motor comparator this requires a structurally-distinct OTHER. **Do not re-derive this: see MECH-095's own `what_would_answer` NON-DEGENERACY PRECONDITION (HARD)**, including its two mandatory guards (probe-partition non-degeneracy AND self/world training-label balance, both reported, mirroring V3-EXQ-741) and its explicit refusal of any further single-agent SD-047 letter. As of 2026-09-04 this is bound to `multi_agent_ecology_v5:MAE-3`, which is `blocked` on MAE-2 on MAE-1; none of the three is built.
> (2) **Level 2 live** -- the ARC-058-vs-ARC-033 arbitration must actually have been run. **See ARC-058's own `what_would_answer`**, whose "CURRENTLY OUTSTANDING, NOT YET RUN" clause records that *no manifest in the evidence corpus carries `claim_ids` including ARC-058*: the V3-EXQ-445 series tested SD-032b's downstream pipeline and the V3-EXQ-511/512/512a/902 series tested SD-048's own noise-discriminability, neither of which is the shared-trunk-vs-independent comparison. A shared-signature test that reads an unexercised Level 2 is vacuous.
> (3) **Level 3 live and non-saturated** -- **see MECH-094's own `what_would_answer`**, which carries the standing instruction "DO NOT RE-DERIVE ELSEWHERE. This is the group's shared write-gate condition." Its three sub-conditions (simulation content actually generated and reaching the write sites; the paired waking arm producing non-zero durable writes on the same channels; the call-site set re-derived from the *current* tree at run time) are inherited verbatim.
> (4) **The shared-signature metric itself must be non-degenerate** -- each level must be independently perturbable along its own calibration axis (Level 1: `multi_source_intensity_scale`; Level 2: the SD-048 noise scale; Level 3: the tag's decision threshold or an injected tag-corruption rate) with at least 3 non-extreme points per axis, and each axis must produce a *measurable* change in that level's own attribution error before any cross-level statement is made. A level whose error is flat across its own axis contributes no information to the family claim and must be reported as such, not averaged in.
>
> **CONFIRMING.** With all four preconditions met, the family claim is supported if the **shape** of the miscalibration response is shared across levels while the **substrate** is not:
> (a) *Symmetric over/under-attribution* -- at each level independently, shallowing the comparator slope produces BOTH over-attribution (self-credit for other-caused change) and under-attribution (missing own causal footprint) across the S/N range, rather than a unidirectional bias; the sign of the error must reverse across the calibration axis at every level, with the reversal consistent in >= 2/3 seeds per level.
> (b) *Non-monotonic noise-dependence* -- each level's attribution accuracy is an inverted U over its own calibration axis, with an interior optimum (peak strictly at a non-endpoint arm), and the peak is >= 2 SD of the per-arm delta above both endpoint arms with an absolute lift floor of 0.04 on that level's own discrimination metric (the same floor V3-EXQ-741 pre-registered for Level 1). Direction-only agreement is not enough -- the interior peak must clear the floor, or the result is "ordering right, magnitude absent" (which is what V3-EXQ-510 actually produced: `ratio_agent_over_env` 1.145/1.159/1.206/1.193 across ARM_0..3, peaking at the pre-registered ARM_2 but never approaching the C1 threshold of 1.5).
> (c) *Single substrate pathology -> bidirectional surface consequences* -- a single injected calibration perturbation at one level produces divergent surface failure modes in >= 2 downstream consumers of that level, in opposite directions (the Jardri & Deneve / Nassar signature).
> (d) *The distinctively architectural clause* -- the three (four) levels' response shapes are **superimposable after per-level rescaling of the calibration axis**, i.e. one shape parameter family fits all levels, while the per-level optima sit at different absolute noise magnitudes and different timescales. This is what makes ARC-061 more than the conjunction of its parts.
>
> **FALSIFYING.** ARC-061 is refuted -- and reduces to "three independent mechanism discoveries that happen to share a metaphor" -- if, with all preconditions met, **the shapes dissociate**: any level shows a monotonic (not inverted-U) calibration response while another shows an interior optimum; or the error-direction reversal in (a) occurs at one level and is absent at another; or the rescaled response curves in (d) cannot be fit by a common shape family (formally: a per-level-free-shape model beats the shared-shape model on held-out seeds at every candidate rescaling). It is **also** refuted, in a different and more interesting direction, if a *single* level's miscalibration reliably propagates to another level's attribution error in a run where the levels were manipulated independently -- that would make the levels one coupled mechanism rather than one repeated motif, which is a stronger claim than ARC-061 makes and would require re-registration rather than promotion.
>
> **WHAT IS NOT A VERDICT.** A conjunction over per-level results is not a test of this claim. As of 2026-09-04, Level 3 is `stable`/confirmed_established, Level 1 has exactly one valid exercise (V3-EXQ-741) and it was a confirmed ceiling hit re-pointed to V5, and Level 2's defining arbitration has never run. "Two of three levels pass" would say nothing about whether they are the same motif. Equally, the twin nulls on the two calibration substrates (SD-047 Level 1; SD-048 Level 2 via V3-EXQ-512a and V3-EXQ-902, both `non_contributory`) do **not** falsify ARC-061 -- they show the *enabling environment* strategy failed, which is upstream of the shared-signature question and is SD-047's / SD-048's problem, not ARC-061's.
>
> **SCOPE CORRECTIONS OWED BEFORE THIS CLAIM IS TESTED (all currency findings, none requiring an experiment).** (i) Level 1 is specified here as a **two-pass counterfactual gap** `E2_harm_s(z, a_actual) - E2_harm_s(z, a_cf)` routed through "the SD-003/SD-029 pipeline"; SD-003 was superseded 2026-04-18 in favour of the **single-pass** comparator family (MECH-256, concretely SD-029 on z_harm_s and SD-031 on z_world) on the 14-entry Frith/Shergill/Blakemore synthesis. Re-point Level 1 to the single-pass family; **see SD-003's own `what_would_answer` for that history, do not re-derive it.** (ii) The family omits the **encoder-level** instantiation, MECH-098 (`z_world_corrected = z_world_raw - ReafferencePredictor(z_world_raw_prev, a_prev)`, live at `ree-v3/ree_core/latent/stack.py:42`), which is the same motif at a per-tick timescale and is the best-evidenced member (18 genuine exp entries). (iii) "SD-047 pending" and "Level 2 ... no calibration SD" are both stale: SD-047 and SD-048 are both implemented (2026-05-03) and SD-048's queue entry names ARC-061 in `unblocks_claims`.

**Proposal sketch (only for a/d):** n/a -- disposition (c). The eventual closure node is already designated: `docs/architecture/reafference_comparator_family.md` **Gap 3** ("cross-level interaction experiment ... Deferred pending both SDs validated") and **Gap 2** ("V4-1 territory -- multi-agent ecology + full simultaneous activation of all three comparator levels"). Its enabling substrate is `multi_agent_ecology_v5:MAE-1 -> MAE-2 -> MAE-3`. Do **not** queue a single-agent ARC-061 probe: the re-derive brake recorded in MECH-095's `what_would_answer` and in `substrate_queue.json`'s `agency_comparator_testbed_sd047` entry explicitly refuses further single-agent work on this lineage, and a family test inherits that refusal through its Level-1 leg.

**depends_on additions (if any):**
- **PROPOSE (needs reviewer assent, changes the claim's scope):** add **MECH-098** as the encoder-level fourth instantiation. If accepted, the `functional_restatement` gains a Level-0/encoder row and the cross-level summary table gains a column; no reverse-deps need repointing (ARC-061 has fan-in 0).
- **PROPOSE (bookkeeping, no scope change):** set `implementation_phase: v5` (currently absent) -- phase-follows-dependency, given MECH-095 is `v5` and the closure node is V4/V5. This removes ARC-061 from V3-completion accounting, which is the honest position.
- Existing `depends_on` (MECH-095, ARC-058, MECH-094, SD-047, SD-048) is otherwise correct and should be left alone.

**GOVERNANCE FLAG:** `stale_note` -- see GOVERNANCE FLAG 3 and GOVERNANCE FLAG 5 below.

---

### SD-047 -- Multi-source environmental dynamics: concurrent stochastic event sources at distinct spatia...

**Recommended disposition:** **(f) defer -- with a durable `digestion_note`, and specifically NOT a new experiment.** The falsifier does not need drafting or running: SD-047 pre-registered its own, the run happened on 2026-05-04, and the manifest records the falsifying branch by name (`"outcome_branch": "WOO_SPELKE"`). What must be resolved before this claim can be correctly dispositioned is a **governance decision on evidence that already exists** -- absorb V3-EXQ-510's `weakens` into the block, and either apply or formally withdraw the pre-registered Woo/Spelke consequent. A new experiment is affirmatively **contraindicated**: the re-derive brake in `substrate_queue.json` (`agency_comparator_testbed_sd047`) and in MECH-095's `what_would_answer` explicitly refuses a further single-agent SD-047 letter.

**Extracted from:** this claim's **own `functional_restatement` "Falsifiable:" clause**, verbatim -- "a 4-arm noise-level sweep (OFF / 0.25x / 1.0x / 4.0x) should reproduce V3-EXQ-506 C1-C3 FAIL pattern in the OFF arm and show an inverted-U (Asai 2016) across noise arms, peaking near ARM_2 default calibration. Woo/Spelke falsifier: if flat-failure across all arms, route MECH-095 from substrate_ceiling to substrate_conditional." Structured below into house form and annotated with the run that already executed it.

**Currency check:** `ree-v3/ree_core/environment/causal_grid_world.py` -- substrate **present and live**: `multi_source_dynamics_enabled` (default `False`), `multi_source_intensity_scale`, `weather_field_enabled`, `transient_events_enabled`, `n_drift_sources` as flat `__init__` kwargs (lines ~403-432, state at ~1004-1031, stepping at ~2969-2985); `_multi_source_n_env_events` / `_multi_source_n_agent_events` counters and `transition_type` tagging present. **Not** factored into `ree-v3/experiments/_lib/baselines/` (the only `_lib` hit is a comment in `exq610_inv074_crystallization_baseline.py`). Drivers `v3_exq_509_...`, `v3_exq_510_...`, `v3_exq_741_...` all exist in `ree-v3/experiments/`. Evidence: V3-EXQ-509 PASS/supports (2026-05-03); **V3-EXQ-510 FAIL 2026-05-04, `evidence_direction_per_claim: {"MECH-095": "mixed", "SD-047": "weakens"}`, `outcome_branch: "WOO_SPELKE"`, `n_c1 = n_c2 = n_c3 = 0` in all four arms, C4 (gap >= 0.1) the only criterion passing**; V3-EXQ-529 (MECH-098 on the SD-047 substrate) FAIL/weakens 2026-05-06; V3-EXQ-741 non_contributory 2026-07-12 (1st valid ceiling hit). All are in `review_tracker.json` `reviewed_run_ids`. Index: `claim_evidence.v1.json` gives SD-047 `experimental_confidence: 0.125`, `genuine_exp_count: 1`, `genuine_exp_direction_counts: {"weakens": 1}`, `latest_run_id: v3_exq_510_...`, `evidence_quadrant: "plausible_unproven"` -- i.e. **the readiness PASS the block cites is not scored, and the only scored entry is a weakens**. `substrate_queue.json` SD-047: `status: implemented`, `ready: True`, `priority: 1`, `unblocks_claims: ["MECH-098", "MECH-099"]` (MECH-095 removed 2026-07-11), with the Woo/Spelke consequent recorded as "deferred pending further analysis". Findings 5-10 above are all currency findings on this claim.

**epistemic_category (proposed):** **`standard`** (currently unset, which infers `standard` from `claim_type: design_decision` -- so this is a recommendation to leave it, stated explicitly because the temptation here is wrong). **Do NOT tag SD-047 `substrate_ceiling` or `substrate_conditional`.** The ceiling belongs to the *consumer* (MECH-095), not to SD-047: SD-047's own substrate was built to spec, verified bit-identical-OFF, verified in the 1:1-2:1 calibration band, and then **validly exercised** -- so it has a genuine, interpretable landed negative on its scope clause, not a signal absorbed downstream and not an unbuilt upstream. `standard` with a `weakens` on the record is the honest reading, and it is what keeps the demote/discrepancy machinery live on this claim rather than suppressed.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** SD-047 asserts two separable things, and they have separate preconditions. **(A) The build clause** -- three concurrent stochastic sources at *distinct* spatial/temporal scales, bit-identically OFF, sweepable on one lever. Non-degenerate only if, per arm: all three sources demonstrably fire (non-zero weather-field delta, non-zero transient appear/disappear count, non-zero drift-move count -- the `_multi_source_n_env_events` decomposition, reported per source, not pooled), the OFF arm draws no RNG and is bit-identical to the pre-SD-047 env, and the env-caused : agent-caused event ratio sits in the pre-registered **1:1-2:1** band. **(B) The enabling clause** -- that this background is "dense enough for agency-detection comparators (MECH-095) and reafference cancellation (MECH-098) to be honestly tested at substrate level". Non-degenerate only if the consumer test additionally reports **a minimum class count per attribution condition** (agent_caused / env_caused / agent_collateral / env_correlated) and the ratio stays inside the calibration band *in the arm being read*. **This second guard was absent from V3-EXQ-510** -- its only check is pool-non-emptiness (`c*_evaluable = ratio is not None`, driver lines 415-452) -- and the pools duly collapsed (seed 42: `agent_caused` 1410 / 933 / 150 / 85 against `env_caused` 66 / 165 / 376 / 362 for ARM_0..ARM_3, i.e. the band is met near ARM_1 and inverts to ~1:2.5 at ARM_2 and ~1:4.3 at ARM_3). Any future reading of clause (B) must carry the guard; **for the consumer-side precondition itself, do not re-derive -- see MECH-095's own `what_would_answer` NON-DEGENERACY PRECONDITION (HARD)** and its two mandatory guards.
>
> **CONFIRMING.** (A) is confirmed and stays confirmed: **V3-EXQ-509 (2026-05-03, PASS/supports)** plus the implementation smoke (200 ticks, all three sources ON, scale=1.0: `env_events=330 / agent_events=169`, ratio 1.95:1, inside the band) plus 7/7 preflight and 184/184 contracts green with the master switch OFF. (B) would be confirmed by the claim's own pre-registered pattern: the OFF arm reproduces the V3-EXQ-506 C1-C3 FAIL signature while at least one enabled arm clears **all** of C1 (gap_agent / gap_env_caused >= 1.5), C2 (gap_agent / gap_agent_collateral >= 1.5) and C3 (gap_agent / gap_env_correlated >= 1.5) alongside C4 (gap_agent >= 0.1), with the arm-level lift forming an **inverted U peaking at ARM_2 (scale 1.0)** -- the Asai 2016 non-monotonic prediction -- and the peak clearing both >= 2 SD of the per-arm delta and an absolute floor (0.04 on the consumer's own discrimination metric, the floor V3-EXQ-741 pre-registered).
>
> **FALSIFYING.** The claim's own words: "**Woo/Spelke falsifier: if flat-failure across all arms, route MECH-095 from substrate_ceiling to substrate_conditional.**"
>
> **THIS BRANCH HAS FIRED. The falsifier ran and returned FALSIFYING for clause (B).** V3-EXQ-510 (2026-05-04, `v3_exq_510_sd047_mech095_live_env_comparator_gap_20260504T074619Z_v3`): FAIL, 3 seeds x 4 arms, `n_c1 = n_c2 = n_c3 = 0` in **every** arm (C4 the only criterion passing, 3/3 seeds, every arm), and the driver's own classifier recorded `"outcome_branch": "WOO_SPELKE"` with `evidence_direction_per_claim: {"SD-047": "weakens"}`. The pre-registered inverted-U is present in *ordering only* and absent in magnitude (`ratio_agent_over_env` 1.145 / 1.159 / **1.206** / 1.193 across ARM_0..ARM_3 -- peak at the pre-registered ARM_2, but against a threshold of 1.5). This is corroborated, not contradicted, by the two later valid runs: **V3-EXQ-741** (2026-07-12) re-ran the 4-arm sweep on a purpose-built test-bed carrying *both* the guards 510 and 047l/047m lacked, reported `non_degenerate: true` on all four arms, and found no arm discriminating (best routing improvement +0.028 against the 0.04 floor; the gradient-head framing actively hurt recall at -0.114; the baseline already carried contact recall 0.75-0.93) -- with the confirmed autopsy's reading being precisely a refutation of clause (B): *SD-047's world-caused drift is not a structurally-distinct OTHER, so the env cannot make the comparator load-bearing and the baseline pre-empts it.* And **V3-EXQ-529** (2026-05-06) tested the clause's *other* named beneficiary, MECH-098, on the SD-047 substrate (`multi_source_dynamics_enabled=True, weather_field_enabled=True, transient_events_enabled=True`; ARM_0 no-SD-047/no-reafference, ARM_1 SD-047 only, ARM_2 SD-047 + reafference) and returned **FAIL / weakens**. Both named consumers, four valid exercises, zero positive discrimination.
>
> **WHAT THE CLAIM SHOULD BECOME (narrowing proposal, PROPOSE-ONLY -- governance decides).** Split the two clauses that this single claim currently fuses. **Keep, as the surviving verified residual:** SD-047 provides three concurrent, independently-ablatable, bit-identically-OFF stochastic event sources at distinct spatial and temporal scales, calibrated to a 1:1-2:1 env:agent event ratio at `multi_source_intensity_scale = 1.0`, with a single sweep lever -- *confirmed* (V3-EXQ-509 + smoke + contracts). **Retire, as refuted by its own pre-registered falsifier:** the clause that this background is "dense enough for agency-detection comparators (MECH-095) and reafference cancellation (MECH-098) to be honestly tested at substrate level" -- four valid exercises against both named consumers, none positive, and the mechanism of the negative is now understood (unstructured agent-independent variation is background, not a structurally-distinct causal source). Nothing is deleted: the retired clause and its evidence chain stay in the block as history, exactly as SD-003's `what_would_answer` handles its own 28-FAIL chain.
>
> **DO NOT QUEUE A SUCCESSOR SWEEP.** The re-derive brake refuses it: `substrate_queue.json`'s `agency_comparator_testbed_sd047` entry is marked "exhausted as the MECH-095 ceiling substrate", and MECH-095's `what_would_answer` states that a run on any single-agent substrate, *including a further SD-047 letter*, "is explicitly REFUSED ... and should self-route `substrate_not_ready`, not count as a verdict." The residual live question -- whether a *structured* second causal source rescues the comparator -- is `multi_agent_ecology_v5:MAE-1 -> MAE-2 -> MAE-3`, not another intensity arm.

**Proposal sketch (only for a/d):** n/a -- disposition (f). What is owed is registry work, not an experiment: (1) absorb V3-EXQ-510's `weakens` into `live_status.evidence` alongside (not instead of) the V3-EXQ-509 readiness PASS, with the `WOO_SPELKE` branch named; (2) replace the "Validation pending: V3-EXQ-509 (queued) -> V3-EXQ-510 ... pending" text in both `notes` and `evidence_quality_note` with what actually happened; (3) apply or formally withdraw the pre-registered Woo/Spelke consequent (GOVERNANCE FLAG 2); (4) reconcile `substrate_queue.json`'s SD-047 `unblocks_claims` with V3-EXQ-529's result (GOVERNANCE FLAG 4); (5) decide the narrowing above.

**depends_on additions (if any):** none. `depends_on: [SD-022, SD-029]` is correct, and the 2026-08-10 edge correction that removed MECH-095 (reversed edge -- SD-047 is the prerequisite that unblocks MECH-095, not a dependent of it) is right and should be left alone. **Note for the reviewer:** the `notes` field's justification for that correction quotes the original inline comment "the primary substrate_ceiling claim this UNBLOCKS" -- the *edge direction* remains correct, but the *unblocking* it asserts has since been empirically disconfirmed, and MECH-095 was removed from the queue entry's `unblocks_claims` on 2026-07-11. The note should say so rather than leaving the unblocking claim standing unqualified.

---

## GOVERNANCE FLAGS

> **GOVERNANCE FLAG 1** -- `evidence_discrepancy` -- **SD-047: the block records a supports/PASS while the index scores a weakens, and the two have disagreed in sign since 2026-05-04.**
> `live_status.evidence` (as_of **2026-07-11**) reads `from: v3_exq_509_sd047_multi_source_substrate_readiness_20260503T103241Z_v3, verdict: supports/PASS` -- a substrate-*readiness* smoke. The behavioural sweep landed the **next day**: `v3_exq_510_sd047_mech095_live_env_comparator_gap_20260504T074619Z_v3`, FAIL, `evidence_direction_per_claim: {"SD-047": "weakens"}`. `claim_evidence.v1.json` scores SD-047 as `genuine_exp_count: 1`, `genuine_exp_direction_counts: {"weakens": 1}`, `latest_run_id: v3_exq_510_...`, `experimental_confidence: 0.125`, `evidence_quadrant: "plausible_unproven"` -- **the readiness PASS the block cites is not scored at all.** Both `notes` and `evidence_quality_note` still describe 509 as "queued" and 510 as "pending". The run is reviewed (`review_tracker.json`), so this is a propagation failure, not an unreviewed result. **Ask:** update `live_status.evidence` to carry both entries with the weakens as the operative one, and rewrite the two stale "pending" paragraphs.

> **GOVERNANCE FLAG 2** -- `contested_disposition` -- **A pre-registered falsifier branch fired 2026-05-04 and its consequent has been "deferred pending further analysis" ever since; the further analysis arrived 2026-07-12 and reached a different conclusion, but the deferral was never closed either way.**
> SD-047's own `Falsifiable:` clause: "if flat-failure across all arms, route MECH-095 from `substrate_ceiling` to `substrate_conditional`." V3-EXQ-510's manifest records `"outcome_branch": "WOO_SPELKE"` with C1-C3 failing in all four arms. `substrate_queue.json` records the consequent as "**MECH-095 epistemic_category reclassification to substrate_conditional deferred pending further analysis**". V3-EXQ-741 (2026-07-12) then supplied that further analysis and governance chose to **keep** `substrate_ceiling` and re-point it to `multi_agent_ecology_v5:MAE-3` (with `implementation_phase` v3 -> v5). That may well be the right call -- MECH-095's own `what_would_answer` argues it, and MAE-3 is genuinely unbuilt, which is textbook `substrate_conditional` shape anyway. **But the pre-registered branch was never formally discharged.** Leaving a fired pre-registration silently un-applied is the failure mode pre-registration exists to prevent. **Ask:** governance either applies the consequent, or records an explicit, reasoned withdrawal of the Woo/Spelke branch in both `claims.yaml` and `substrate_queue.json` -- and, if withdrawing, states which observation would now trigger the `substrate_ceiling -> substrate_conditional` route instead. **Not for this digestion pass to adjudicate; MECH-095 is outside G10.**

> **GOVERNANCE FLAG 3** -- `stale_note` -- **ARC-061's `notes` and its backing architecture doc both describe a Level-2 substrate gap that was closed on the day the claim was registered, and a Level-1 dependency state that is two governance decisions out of date.**
> (a) `notes`: "Level 2 (ARC-058) V3-tractable but no calibration SD" -- contradicted **within the same field** two paragraphs earlier ("Level 2 ... SD-048 ... is the calibration SD"), and by `substrate_queue.json`, where SD-048 is `implemented` / `ready: True` with `unblocks_claims: ["ARC-058", "ARC-033", "ARC-061"]`.
> (b) `notes`: "Level 1 (MECH-095) substrate_ceiling, SD-047 pending" -- SD-047 has been `implemented` since 2026-05-03, and MECH-095's ceiling was re-pointed away from SD-047 to `multi_agent_ecology_v5:MAE-3` on 2026-07-12 with `implementation_phase` reassigned v3 -> v5.
> (c) `docs/architecture/reafference_comparator_family.md` (last updated 2026-05-03, front-matter `status_asof: 2026-07-12`): "**Gap 1: Level 2 substrate enrichment SD (highest priority)** -- Level 2 has no SD claim ... Suggested claim: `SD-NNN` (`body.interoceptive_noise_dynamics`)". That is SD-048 verbatim, registered the same day. The doc also still records MECH-095 as `status: active` (it is `candidate` since GOV-CEIL-1, 2026-07-11) and describes Level 1's counterfactual branch as "the SD-003/SD-029 pipeline" although SD-003 was superseded 2026-04-18.
> **Ask:** refresh both, and while doing so consider the two scope corrections in ARC-061's draft above (re-point Level 1 to the single-pass family; add MECH-098 as the encoder-level fourth instantiation).

> **GOVERNANCE FLAG 4** -- `evidence_discrepancy` -- **`substrate_queue.json`'s SD-047 entry advertises an unblock its own consumer evidence refutes.**
> The entry carries `status: implemented`, `ready: True`, `priority: 1`, `unblocks_claims: ["MECH-098", "MECH-099"]` (MECH-095 having been removed 2026-07-11). But **V3-EXQ-529** (2026-05-06) tested MECH-098 *on the SD-047 substrate* -- the driver enables `multi_source_dynamics_enabled`, `weather_field_enabled` and `transient_events_enabled` and runs three arms keyed on SD-047 x reafference -- and returned **FAIL / weakens**, reviewed. So SD-047 currently unblocks nothing that has since passed, at `priority: 1`. **Ask:** either narrow `unblocks_claims` to reflect the landed results, or annotate the entry the way the MECH-095 removal was annotated, so a future `/implement-substrate` walk does not read `priority: 1, ready: True` as live headroom.

> **GOVERNANCE FLAG 5** -- `stale_note` (bookkeeping) -- **ARC-061 carries no `implementation_phase` while its Level-1 dependency is `v5` and its closure node is V4/V5.**
> MECH-095 was reassigned v3 -> v5 on 2026-07-12 (user-confirmed, phase-follows-dependency, and explicitly "removed from V3-completion accounting"). ARC-061 `depends_on` MECH-095 and its own designated closure node -- `reafference_comparator_family.md` Gap 2/Gap 3, cross-level interaction requiring simultaneous activation of all levels with a structurally-distinct OTHER -- is bound to `multi_agent_ecology_v5:MAE-1 -> MAE-2 -> MAE-3` (all `blocked`, nothing built). **Ask:** set `implementation_phase: v5` on ARC-061 so it leaves V3-completion accounting alongside its dependency. Low-risk: ARC-061 has fan-in 0, so no reverse-dep repointing is needed.

---

<!-- S_MECH-273 appended 2026-09-04T21:25:35Z -->
## G12 -- MECH-273 sleep-half self-model aggregation (solo agent report)

**Solo note:** no structural edge to another UNDIGESTED claim reached the floor, so the cross-claim mandate (i)-(iv) reduces to cross-references against ALREADY-DIGESTED neighbours, which are handled inline below: SD-003 (superseded 2026-04-18; its `what_would_answer` explicitly redirects the live falsifier to SD-029, and I cross-reference rather than re-derive it), INV-049 (digested; its NON-DEGENERACY PRECONDITION about the SD-017 write-gate is reused verbatim-in-substance for MECH-273's E1 leg), SD-017 (being digested in G1 this campaign -- NOT digested here; read only as the plan-of-record ceiling that scopes MECH-273's E1 leg), and INV-050 (digested; its "validate the producer with the consumer ABSENT" lesson is imported as the design's third-arm control).

---

### MECH-273 -- The self-model has a waking half and a sleep half. The waking half is SD-003 (single-episode counterfactual self-attribution via E2). The sleep half is full-Bayesian aggregation...

**Recommended disposition:** **(a) testable now** -- the sleep half is BUILT, EXERCISED, and confirmed non-degenerate with a genuine zero-movement OFF arm (V3-EXQ-702), yet neither of the two banked PASSes evaluates the claim's own primary falsifier; the design-of-record already contains the un-run test and it is runnable today with one extra config value.

**Extracted from:** THREE existing sources, composed -- not drafted fresh.
1. The claim's own `functional_restatement` -> "Falsifiable (primary): ablating the sleep-phase aggregation step should leave single-episode SD-003 intact but degrade stability of self-attribution across episodes. The agent should be less able to correct previously-held spurious self-attributions when post-hoc evidence accumulates against them."
2. `REE_assembly/docs/architecture/sleep_aggregation_cluster.md` line 352, **Phase E row of the Validation plan** -> "with vs without offline writeback; measure E2_harm_s prediction residual on **held-out** tuples | residual decreases monotonically across **5** sleep cycles with writeback ON; flat or increasing OFF." This is the claim's own pre-registered acceptance criterion and it has never been run.
3. `sleep_aggregation_cluster.md` line 351 + `evidence/planning/sleep_substrate_plan.md` line 451, the **EXP-0169 spec** -> "seed waking with biased self-attribution; sleep aggregator should correct it. Acceptance: mean of `self`-domain posterior shifts toward true causal_sig by >= 0.5 SD across 3 sleep cycles."
The draft below is (1) operationalised by (2) and (3), plus one control arm the sources do not name (see Currency check item 6).

**Currency check:** every "not yet built" / "queued" / "no experiment yet" note in the claim was verified against code, manifests and the plan-of-record. Six findings, four of them stale-note corrections:

1. **The sleep half IS BUILT.** `ree-v3/ree_core/sleep/self_model_aggregator.py` exists (345 lines, `SelfModelAggregator(BayesianAggregator)`, `offline_gradient_pass(e2_harm_s, replayed_regions, n_steps, domain="self", use_snapshot, harm_replay_buffer)`), landed 2026-04-25 as Phase E. `substrate_queue.json` `sd_id: MECH-273` is `status: implemented`, `implementation_status: implemented`, `ready: true`. Flags in `ree_core/utils/config.py`: `use_mech273_self_model` (default False, line 6465), `mech273_offline_lr_scale=0.1`, `mech273_offline_n_steps=100`, `mech273_partial_decay_factor=0.5`. Per project doctrine (check the knob, not the status) the knob exists and is default-off, reachable via the bundle flag `use_sleep_aggregation_cluster` (added 2026-05-16, GAP-3) which force-enables all eight sub-flags through `enable_sleep_aggregation_cluster()`.
2. **`evidence_quality_note` is STALE.** It reads "Candidate, no direct experiment yet." The claim has been `provisional` since 2026-06-23 and carries **two** genuine experimental PASSes (`claim_evidence.v1.json`: `genuine_exp_count: 2`, `pass_runs: 2`, `fail_runs: 0`). The sentence that follows it -- "Natural validation pathway is a V3 experiment that runs SD-003 across many episodes with and without a sleep-phase aggregation step, and tests whether the agent can correct a seeded spurious self-attribution when counter-evidence accumulates" -- is still ACCURATE and still UN-RUN, and is exactly the falsifier drafted below. Recommend rewriting the first sentence and keeping the second.
3. **`implementation_note` is STALE in three places.** (a) "Lands at Phase 5 ... as ree_core/sleep/self_model_aggregator.py" -- it landed 2026-04-25. (b) It describes the GAP-4 defect implicitly ("offline gradient writeback to E2_harm_s") without recording that the **synthetic batch was replaced with replay-derived tuples on 2026-05-16** (`sleep_substrate_plan.md` decision log 2026-05-16, GAP-4 blocked -> done; `agent.py:5732-5744` populates `_harm_replay_buffer` on the waking stream when `hypothesis_tag=False`; `phase_manager.py:443` snapshots it at SLEEP_ENTRY). (c) It does not mention `use_sleep_aggregation_cluster`, which is now the correct way to arm the pathway.
4. **The EXP-0169 citation is WRONG, in three documents at once.** `claims.yaml:43245` says "Validation experiment EXP-0169 template (already in experiment_proposals.v1.json)". I checked all three proposal registries (`experiment_proposals.v1.json`, `experiment_proposals_index.v1.json`, `manual_proposals.v1.json`): **EXP-0169 is `claim_id: MECH-290`** -- the OCD Layer-2 backward-credit-sweep ablation (`backlog_id: EVB-0547`, `status: gated`, added 2026-04-28), with no relation to sleep. `claims.yaml:47666` cites the same EXP-0169 correctly as the MECH-290 proposal, so claims.yaml contradicts itself. Meanwhile `sleep_aggregation_cluster.md:351/354/406/416` assigns EXP-0169 to **Phase D / MECH-275**, and `sleep_substrate_plan.md:350/436/451` assigns it to **MECH-273**. Zero proposals in any registry name MECH-273 in `claims_tested`. Net: MECH-273 has **no registered validation proposal at all**; the design text exists only inside the two architecture/plan docs.
5. **`sleep_substrate_plan.md`'s own status table contradicts its own decision log.** Line 335 still reads "MECH-273 SelfModelAggregator Phase E | contracts only; **uses synthetic batch**" -- superseded by that same file's 2026-05-16 entry closing GAP-4 (line 1327ff). Low-cost one-line fix in the plan-of-record.
6. **What the two PASSes actually measured -- the central finding.** Both are plumbing-level, not falsifier-level:
   - **V3-EXQ-574** (2026-05-16, PASS, supports, 3 seeds 42/7/13, 3 cycles): acceptance was `C1_min_steps_per_cycle=100`, `C2_min_regions_some_cycle>=1`, `C3_min_loss_cycle1>=1e-4 AND loss decreases`. That is "the bounded pass ran, consumed >=1 posterior region, and its own **training** loss went down" (per-seed mean_loss 3.2e-3 -> 5.0e-5 etc.). There is **no held-out set, no OFF arm, and no self-attribution DV**. The runs/ pack's `metrics.json` is `{"values": {}}` (empty) -- the scoreable content is in the flat JSON only.
   - **V3-EXQ-702** (2026-06-23, PASS, supports, seeds 42/7/123, machine ree-cloud-2): the MECH-273 criterion is, verbatim, "ARM_ON E2_harm_s param L2 delta >= 1e-05 AND mech273_n_offline_steps>0 on >=2/3 seeds; ARM_OFF zero movement". Measured: ON `mech273_param_delta_l2` 0.3783 / 0.3747 / 0.3745 with 100 offline steps; OFF exactly 0.0 with 0 steps; `harm_replay_buffer_len: 12` in both arms; `non_degenerate_per_claim: {"MECH-273": true}`. That is a rigorous, genuinely-non-degenerate proof that **the writeback fires and moves parameters** -- it is not evidence that the movement improves anything, and it says nothing about durability, spurious-attribution correction, or cross-episode stability.
   So MECH-273 is `provisional` on the strength of two mechanism-fires criteria. The claim's own scientific content -- "without the sleep half, REE has an episode-local causal signature but not a durable self-model" -- has never been put at risk. (See GOVERNANCE FLAGS.)
7. **Confidence has drifted since promotion.** `status_note` records the 2026-06-23 promotion at `exp_conf 0.824`; `claim_evidence.v1.json` today reports `experimental_confidence: 0.662` (`exp_posterior.mean 0.5789`, `n_support_w 0.375`, n=2), `literature_confidence 0.856` (5 lit entries), `overall_confidence 0.778`, `conflict_ratio` effectively 0 (`direction_counts` supports 6 / mixed 1 / weakens 0). Newest entry is a 2026-09-03 literature SOURCE (`2026-09-03_mech_275_sleep_reactivation_decision_ambivalence_chend2026`, supports, conf 0.50).
8. **The E1 leg is ceilinged; the E2_harm_s leg is not.** MECH-273 asserts routing "to E1 and SD-033a". SD-017 is `epistemic_category: substrate_ceiling` with `pending_retest_after_substrate: true`, re-scoped 2026-08-30 to the `ContextMemory.write` **CONTENT** gap (`e1_deep.py`); the 2026-08-30 confirmed autopsy `failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30#V3-EXQ-436g` records addressing FIXED (16/16 slot occupancy) but WAKING_ONLY `slot_cosine_sim 0.9993`, i.e. E1 context slots still do not differentiate. INV-049's already-digested `what_would_answer` carries the same precondition and the same 436b/c/d history -- **do not re-derive it, cross-reference INV-049's precondition text for anything that reads E1 ContextMemory.** MECH-273's Phase-E writeback path, by contrast, touches only `E2_harm_s` parameters and the aggregator's `self`-domain posterior, neither of which passes through `ContextMemory.write`. Hence the falsifier below is deliberately scoped to the E2_harm_s + posterior leg, and the E1-consolidation leg is quarantined behind SD-017.
9. **Plan-node status.** `sleep_substrate:GAP-3`, `GAP-3b`, `GAP-4` are all `status: done` and sit in `closure_status.md`'s "Done (64)" bucket -- but all three carry `live.needs_review: true` with `needs_review_reasons: ["newest_forward_predates_later_decision_event(s)"]` and a `2026-08-30` `non_contributory/substrate_ceiling` stamp inherited from the 436g cluster autopsy, whose subject is SD-017/MECH-166, not MECH-273. That inherited stamp should not be read as a MECH-273 ceiling verdict.

**epistemic_category (proposed):** **`standard`** -- set EXPLICITLY (currently unset; inference from `mechanism_hypothesis` would give the same value, but pinning it forecloses a future mis-tag). Applying the sharpened 2026-08-07 discriminator: NOT `substrate_conditional`, because the mechanism is not merely planned -- `self_model_aggregator.py` exists and V3-EXQ-702 exercised it under a genuinely non-degenerate ON/OFF contrast; NOT `substrate_ceiling`, because that requires the mechanism to have been exercised *repeatedly against its own outcome metric* with a downstream absorber eating the signal, and MECH-273's outcome metric (held-out residual / posterior correction / cross-episode stability) has been evaluated **zero** times. Nothing is absorbing the signal; nobody has looked. The explicit `standard` should carry the scope rider that the **E1-consolidation leg inherits SD-017's `substrate_ceiling`** and is excluded from the falsifier.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION** (all seven must hold in the ON arm, or the run is `scoring_excluded`, not scored -- the V3-EXQ-514m/642 vacuity discipline; V3-EXQ-702's own per-claim guards are the reusable template):
> (P1) **The sleep phase must actually fire, N>=5 times.** The pathway is armed with `use_sleep_aggregation_cluster=True` (which force-enables all eight sub-flags via `enable_sleep_aggregation_cluster()`; setting `use_mech273_self_model` alone leaves the cluster silent -- that was GAP-3). Sleep entry is boundary-only via `SleepLoopManager.notify_episode_end()` (sleep_substrate:GAP-9), so the driver MUST be multi-episode (GAP-7) with `sleep_loop_episodes_K` chosen such that at least 5 cycles complete, or `use_within_life_sleep_trigger=True` with `within_life_sleep_step_ceiling` set. Report the realised cycle count; fewer than 5 completed cycles = excluded.
> (P2) **The consolidation window must be non-empty.** `mech273_n_offline_steps > 0` and the realised `mech273_n_offline_steps` per cycle must equal it (the config documents `n_steps <= 0` as a silent no-op diagnostic mode -- a run that lands there registers a wired aggregator that never updates anything).
> (P3) **The replay buffer must be non-empty AND non-constant at SLEEP_ENTRY.** `harm_replay_buffer_len > 0` is necessary but NOT sufficient: `offline_gradient_pass` falls back to a synthetic `(z_harm_s zeros, round-robin one-hot action)` batch on an empty/None buffer, which is precisely the GAP-4 defect closed 2026-05-16, and a batch of near-identical real tuples is the same vacuity with better paperwork. So additionally require `Var(z_harm_s)` across the snapshotted buffer to exceed a pre-registered floor and `>= 2` distinct actions present. This is the live risk on this substrate: a competent agent routes around hazards, which is exactly how V3-EXQ-843 was invalidated by zero harm exposure (MECH-203) and is the same pathology that has kept SD-029's C2 unevaluable across 13+ runs. Report harm-contact counts per seed.
> (P4) **The `self`-domain posterior store must be non-empty at WRITEBACK**: `n_regions >= 1` with a non-uniform staleness snapshot (V3-EXQ-574's C2 and V3-EXQ-702's `mech285_snapshot_is_uniform: false` guard).
> (P5) **The OFF arm must show genuine zero movement**: `mech273_param_delta_l2 == 0.0` and `mech273_n_offline_steps == 0`, as V3-EXQ-702 demonstrated on 3/3 seeds. A non-zero OFF arm means the bit-identical-OFF guarantee has regressed and the contrast is uninterpretable.
> (P6) **The waking half must be intact and measurable in BOTH arms.** MECH-273 predicts that ablating the sleep half leaves single-episode attribution intact; if per-episode attribution is itself flat or unmeasurable, "degraded cross-episode stability" has no baseline to degrade from. Report the waking-half attribution signal (MECH-256/SD-029 comparator output, C1-equivalent `forward_r2 >= 0.9`) in both arms. Do NOT gate on SD-029's C2 (Shergill-style self-vs-external attenuation): per SD-029's own already-digested falsifier that criterion has never once been evaluable on this substrate, and importing it would import a known vacuity.
> (P7) **E1 EXCLUSION.** No acceptance criterion may read `ContextMemory` slot content or `slot_cosine_sim`. That path is behind SD-017's live `substrate_ceiling` (`ContextMemory.write` CONTENT gap, confirmed 2026-08-30 by V3-EXQ-436g: addressing fixed 16/16, WAKING_ONLY `slot_cosine_sim` 0.9993) -- see INV-049's own `what_would_answer` for the full precondition, do not re-derive it. A MECH-273 verdict that depends on E1 differentiation is a verdict on SD-017.
>
> **CONFIRMING** (three arms, matched seeds, >= 5 seeds; ARM_OFF = `use_sleep_aggregation_cluster=False`; ARM_ON = cluster True with `mech273_offline_n_steps=100`; **ARM_SLEEP_NO_WRITEBACK** = cluster True with `mech273_offline_n_steps=0`, i.e. the full sleep loop, replay sampling, routing and posterior accumulation all running but MECH-273's own gradient step suppressed. The third arm is load-bearing and is the INV-050 lesson imported: without it, any positive result is a verdict on the sleep cluster as a whole -- SD-017 + MECH-285 + MECH-272 + MECH-275 -- and MECH-273 collects credit for its neighbours' work. It costs one integer):
> - **C1 (held-out residual; the design-of-record's own Phase-E gate).** E2_harm_s one-step prediction residual on a HELD-OUT set of `(z_harm_s, a, z_harm_s')` tuples collected during waking but excluded from the replay buffer, measured after each of 5 sleep cycles. CONFIRM: residual decreases monotonically across the 5 cycles in ARM_ON, and is flat-or-increasing in BOTH ARM_OFF and ARM_SLEEP_NO_WRITEBACK. Effect gate: `delta_residual(ON) - delta_residual(NO_WRITEBACK) >= max(0.5 * SD(delta across seeds), 0.02)` in normalised residual units, on >= 3/5 seeds.
> - **C2 (spurious-attribution correction; the EXP-0169 spec).** Seed a spurious self-attribution -- inject a biased `self`-domain posterior mean at a known region, or run a waking block in which the agent's action reliably co-occurs with a harm outcome it does not cause -- then let post-hoc counter-evidence accumulate. CONFIRM: the `self`-domain posterior mean at that region shifts toward the true causal_sig by **>= 0.5 SD within 3 sleep cycles** in ARM_ON, and by **< 0.15 SD** in both ARM_OFF and ARM_SLEEP_NO_WRITEBACK.
> - **C3 (durability, with an anti-flattening guard).** Cross-episode variance of the attribution at a fixed region over the final K episodes is LOWER in ARM_ON than in both controls, AND -- this half is what distinguishes a durable model from a collapsed one -- ARM_ON still tracks a deliberate mid-run change in the true causal_sig with a lag of <= 2 sleep cycles. Both halves required. The guard is not hypothetical: the claim's own mixed literature entry (`2026-04-28_type_prototype_sleep_disruption_hennies2017`, Hennies 2017) reports that cued reactivation during SWS *abolishes* rather than attenuates the sleep abstraction benefit, so "replay flattens everything toward a constant" is a live outcome that would satisfy a variance-only criterion while refuting the claim.
>
> **FALSIFYING** (any one is a genuine refutation of MECH-273 as stated, provided P1-P7 hold):
> - **F1 (the decisive one -- inert writeback).** ARM_ON is statistically indistinguishable from ARM_SLEEP_NO_WRITEBACK on C1 AND C2, while ARM_OFF differs from both. The sleep *loop* does work; MECH-273's *offline gradient pass* -- the specific step this claim asserts is the self-model's sleep half -- contributes nothing beyond it. Parameters demonstrably move (V3-EXQ-702, L2 delta 0.37) without improving anything, i.e. the movement is noise injection. This is the outcome the two banked PASSes are structurally incapable of detecting.
> - **F2 (no correction).** ARM_ON fails to correct a seeded spurious self-attribution (C2 shift < 0.15 SD over 3 cycles) despite P1-P4 all holding -- directly refutes "correcting for delayed consequences, failed counterfactuals, and systematic attribution biases".
> - **F3 (no durability, or false durability).** ARM_ON shows no reduction in cross-episode attribution variance relative to the controls; OR it reduces variance but fails the C3 tracking half (lag > 2 cycles, or no movement at all on a genuine mid-run causal_sig change). The second branch refutes the claim's own words -- a self-model that cannot revise is not durable, it is stuck -- and is the specific reading Hennies 2017 warns about.
> - **F4 (the waking half suffices).** ARM_OFF matches ARM_ON on C1/C2/C3 with the waking comparator intact (P6). Refutes "without the sleep half, REE has an episode-local causal signature but not a durable self-model" -- the episode-local signature would then already be durable, and the sleep half is redundant rather than constitutive.
> - What would NOT count either way: a run failing P1-P7 (`scoring_excluded`, non-contributory); any criterion reading E1 `ContextMemory` slot content (that is a verdict on SD-017); and a re-run of the V3-EXQ-574 / V3-EXQ-702 mechanism-fires criteria, which are already banked and cannot move this claim further in either direction.

**Proposal sketch (disposition (a)):**
- **title:** "MECH-273 sleep-half ablation: held-out E2_harm_s residual, spurious-self-attribution correction, and cross-episode attribution stability under a three-arm cluster-ON / writeback-suppressed / cluster-OFF contrast"
- **related_claims:** `claim_ids_tested: [MECH-273]` (single-claim by design -- the ARM_SLEEP_NO_WRITEBACK control exists precisely so the result is not shared with the rest of the cluster). Cross-referenced but NOT tagged: MECH-275 (parent aggregator; needs its own run once the MECH-276 feedstock is built), MECH-285 / MECH-272 (already have their 702 evidence), SD-029 / MECH-256 (waking half, P6 only), SD-017 / INV-049 (E1 leg, excluded by P7), INV-050 (source of the third-arm control pattern), ARC-033 (the E2_harm_s parameters actually updated), SD-033a (the viability-map consumer -- a secondary DV if the bias head is live; note `commitment_closure:GAP-1` records SD-033a's bias head as untrained, so do not gate on it).
- **acceptance_checks:**
  - P0: all of P1-P7 above reported per seed; any seed failing any of them is `scoring_excluded`, not scored (V3-EXQ-702's per-claim non-degeneracy-guard pattern, reused verbatim).
  - C1: `delta_residual(ON) - delta_residual(NO_WRITEBACK) >= max(0.5 * SD_across_seeds(delta), 0.02)`, monotone decrease over 5 cycles in ON, >= 3/5 seeds.
  - C2: `self`-domain posterior mean shift toward true causal_sig `>= 0.5 SD` within 3 cycles in ON and `< 0.15 SD` in both controls, >= 3/5 seeds.
  - C3: cross-episode attribution variance ON < both controls, AND ON tracks a mid-run true-causal_sig change with lag <= 2 cycles, >= 3/5 seeds.
  - PASS = C1 AND C2 (C3 supporting/secondary). FAIL = F1 (the ON-vs-NO_WRITEBACK null) -- and F1 must be pre-registered as a real FAIL, not routed to "substrate not ready", because the substrate demonstrably fires (V3-EXQ-702).
  - Machine: route to cloud (`machine_affinity: "any"`; 702 ran on ree-cloud-2). Multi-episode driver per GAP-7; `sleep_driver_pattern` declared in the manifest as 702 did.
- **Cheap prerequisite worth doing first:** a dry-run smoke that forces P1-P4 green with a stubbed gradient step, as a POSITIVE control on the instrument -- a `--dry-run` that short-circuits ahead of the writeback would report green while measuring nothing (the V3-EXQ-591g pattern).

**depends_on additions (proposed, three):**
- **`SD-029`** -- the 2026-09-01 repoint (`sd003-groupAC-20260901`) moved `SD-003 -> MECH-256` and its own note says SD-029 was "deliberately NOT added -- add it only if a specific-stream dependency is actually meant." For MECH-273 it **is** meant: `offline_gradient_pass` updates `E2_harm_s` and only `E2_harm_s`, and the aggregator is specialised on "the SD-003 causal_sig posterior in the `self` domain" (config.py comment, line ~6455). MECH-273 depends on the concrete z_harm_s instantiation, not merely on the stream-agnostic comparator. This closes a question that repoint explicitly left open.
- **`ARC-033`** -- the claim's own `implementation_note` says "Depends on substrate already shipped: SD-003 + **ARC-033 E2_harm_s** + SD-013", and the gradient pass literally writes ARC-033's parameters, yet ARC-033 is absent from `depends_on`.
- **`SD-017`** -- currently reached only transitively via INV-049. A direct edge is honest bookkeeping: SD-017's `substrate_ceiling` is what scopes MECH-273's E1 leg out of the falsifier (P7), and a future reader should not have to walk through INV-049 to find that.

---

### GOVERNANCE FLAGS

**FLAG 1 -- `contested_disposition`.** MECH-273 is `provisional` (promoted 2026-06-23) on two experimental entries whose acceptance criteria are both **mechanism-fires**, not falsifier-level: V3-EXQ-574 = "bounded pass ran >= 100 steps, consumed >= 1 posterior region, own training loss decreased" (no held-out set, no OFF arm, no attribution DV; `runs/.../metrics.json` is `{"values": {}}`); V3-EXQ-702 = "ARM_ON E2_harm_s param L2 delta >= 1e-05 AND n_offline_steps > 0; ARM_OFF zero movement". Both are rigorous *as plumbing checks* and V3-EXQ-702's OFF-arm zero is genuinely non-degenerate -- but neither puts the claim's assertion ("without the sleep half, REE has ... not a durable self-model") at any risk. The claim's own pre-registered Phase-E acceptance criterion in `sleep_aggregation_cluster.md` line 352 has never been run. Recommend: no demotion (the evidence is sound for what it measures), but record on the claim that `provisional` currently rests on substrate-fires evidence, and that the owed run is the Phase-E residual/correction ablation above. Note the sibling asymmetry: `sleep_substrate:GAP-3b`'s own outcome note kept MECH-285's residual owed work visible ("only 1 genuine exp entry") and MECH-275's ("owed to a LATER run once MECH-276 is built"), but recorded MECH-273 as simply delivered -- the same residual exists for MECH-273 and was not carried forward.

**FLAG 2 -- `stale_note`.** `claims.yaml` MECH-273 `evidence_quality_note` opens "Candidate, no direct experiment yet" -- false since 2026-05-16; the claim is `provisional` with `genuine_exp_count: 2`, `pass_runs: 2`, `fail_runs: 0`. The note's second sentence (the natural validation pathway) is still correct and still owed; keep it, fix the first sentence.

**FLAG 3 -- `stale_note`.** `claims.yaml` MECH-273 `implementation_note` still reads as a forward-looking build plan ("Lands at Phase 5 ... Flag use_mech273_self_model default False ... runs after Phases A-D land"). Phase E landed 2026-04-25; GAP-4 (synthetic batch -> replay-derived tuples) closed 2026-05-16; the arming route is now `use_sleep_aggregation_cluster` (GAP-3, 2026-05-16), which the note does not mention. Same-family stale line in the plan-of-record: `evidence/planning/sleep_substrate_plan.md` line 335 still says "MECH-273 SelfModelAggregator Phase E | contracts only; **uses synthetic batch**", contradicted by that same file's own 2026-05-16 decision-log entry at line 1327.

**FLAG 4 -- `stale_note` (mis-citation, three documents).** "Validation experiment EXP-0169" is wrong wherever it is attached to MECH-273 or to the sleep cluster. In all three proposal registries, **EXP-0169 is `claim_id: MECH-290`** (OCD Layer-2 backward-credit-sweep ablation, `backlog_id: EVB-0547`, `status: gated`, added 2026-04-28) -- and `claims.yaml:47666` cites it correctly that way, so claims.yaml contradicts itself against `claims.yaml:43245`. Meanwhile `docs/architecture/sleep_aggregation_cluster.md` (lines 351/354/406/416) assigns EXP-0169 to **Phase D / MECH-275** and `evidence/planning/sleep_substrate_plan.md` (lines 350/436/451) assigns it to **MECH-273**. No proposal in any registry names MECH-273 in `claims_tested`. Fix: strike the EXP-0169 reference from MECH-273's `implementation_note`, mint a real proposal id for the Phase-E ablation sketched above, and reconcile the two architecture/plan docs (which currently also disagree with each other about which claim EXP-0169 belongs to).

**FLAG 5 -- `evidence_discrepancy`.** `status_note` records the 2026-06-23 promotion at `exp_conf 0.824`; `claim_evidence.v1.json` now computes `experimental_confidence: 0.662` (`exp_posterior`: alpha 1.375 / beta 1.0 / mean 0.5789 / `n_support_w` 0.375 over the same n=2 entries), with `overall_confidence 0.778` and `conflict_ratio` effectively 0. No new experimental evidence has landed since promotion, so this is a scorer/weighting recomputation rather than a change in the underlying record -- worth a one-line reconciliation on the claim so a future reader does not treat 0.824 as current. Also worth noting for the record: `sleep_substrate:GAP-3 / GAP-3b / GAP-4` all carry `live.needs_review: true` (`newest_forward_predates_later_decision_event(s)`) with a `2026-08-30 non_contributory/substrate_ceiling` stamp inherited from `failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30#V3-EXQ-436g`, whose actual subject is SD-017 / MECH-166. That inherited stamp is not a MECH-273 ceiling verdict and should not be read as one.

---

<!-- S_MECH-474 appended 2026-09-04T21:25:35Z -->
## G20 -- Learning-mechanism meta-selection (solo claim; agent report)

**Solo note:** single-claim assignment, so the four cross-claim questions (i)-(iv) do not apply within the group; the merge/contradiction analysis that would have gone there is directed OUTWARD at two already-built mechanisms (MECH-261, SD-083) and is carried in the per-claim body and the GOVERNANCE FLAG blocks below.

---

### MECH-474 -- LEARNING-MECHANISM META-SELECTION (narrow form): the control plane selects among the learning regimes REE actually has...

**Recommended disposition:** (f) defer with a durable `digestion_note` -- the claim's own registered four-regime menu contains one regime ("counterfactual simulation") that has no learning path in V3 and cannot be given one without contradicting MECH-094 (status `stable`), so the falsifier is not authorable until governance adjudicates whether to narrow the menu to three; the menu must NOT be narrowed inside a digestion pass, because MECH-474's own notes pre-register the four and explicitly warn against silent redesign.

**Extracted from:** the claim's own `notes` FALSIFIER + NON-DEGENERACY GUARD paragraphs, which are a verbatim carry of candidate 4 in `/Users/dgolden/REE_Working/REE_assembly/evidence/planning/thought_intake_2026-07-19_conservative_skill_refinement_multi_timescale_learning.md` (section "N3. Meta-selection of learning strategy" + "Candidate claims" item 4), and their expansion into `acceptance_checks` on proposal EXP-0401 in `evidence/planning/manual_proposals.v1.json`. Nothing is drafted fresh; the draft below is the existing falsifier put into house structure, with the substrate preconditions made explicit and one arm's satisfiability corrected.

**Currency check** (five findings, three of them stale-note class):

1. **The claim's own closing sentence "Live V3-adjacent question; testable now. See EXP-0401." is STALE and now contradicted.** EXP-0401 is `status: blocked_substrate`, `blocked_by: [MECH-094, MECH-319]`, recorded 2026-09-02 by `chip-proposal-exp-1110-paced` (`evidence/planning/manual_proposals.v1.json`, `experiment_proposals.v1.json`). Two further auto-minted proposals on the same claim, **EXP-1081** (`claim_probe_mech_474`) and **LIT-1082** (`targeted_review_mech_474`), both backlog `EVB-1585`, are ALSO `blocked_substrate`. So all three routes to evidence on this claim are currently closed.
2. **I verified the substrate gate at source rather than trusting the note.** `ree_core/agent.py:10501 _do_replay` builds `replay_trajs` from `hippocampal.replay(...)` / `diverse_replay(...)` and the function then **ends** -- the assignment is dead, no parameter update, trailing comment "hypothesis_tag=True: these trajectories cannot update residue (MECH-094 -- enforced in ResidueField.accumulate)". `ree_core/regulators/simulation_mode_rule_gate.py` exists and instantiates the write gate. MECH-094 is `status: stable`; MECH-319 is `status: provisional`. Confirmed: a fixed "counterfactual simulation" arm would be a structurally inert no-learning arm, and `experiments/_lib/precondition_gate.assert_no_structurally_unsatisfiable_gate` would refuse the run at setup. The blocked_note is accurate.
3. **Zero evidence of any kind.** `docs/assets/data/claims.json["MECH-474"]` carries only `{assembly_state: gated_v3, epistemic_stance: believed, status: candidate, subject, title, type}` -- **no `exp_conf`, no runs**. `grep -c MECH-474 evidence/experiments/claim_evidence.v1.json` = 0. The only file under `evidence/experiments/` mentioning the id is a test fixture (`scripts/test_proposal_lane_carry_forward.py`). Not present in `evidence/planning/substrate_queue.json`; not present in `docs/CURRENT_FRONT.md` or `evidence/planning/closure_status.md`. Reverse-deps: **fan-in 0** confirmed -- the only other `MECH-474` occurrence in `claims.yaml` is a prose comment on ARC-092 (line ~70081) recording that MECH-474 references ARC-092 as motivational context only.
4. **Two of the five `depends_on` are themselves unbuilt.** MECH-312b (`practice_maturity_weighting`) and MECH-312c (`affective_stream_modulation_of_arbitration`) are both `reading: candidate/v3_pending/substrate_conditional`, `epistemic_category: substrate_conditional`; `grep practice_maturity ree_core/` returns nothing. MECH-261 is `stable` and BUILT; MECH-163 and MECH-179 are `candidate`. The claim's note calls all five "PARTIAL PRECEDENT" without distinguishing built from unbuilt -- worth correcting when the note is next touched, since it currently reads as though five precedents exist.
5. **The blocked_note's own sibling cross-reference is WRONG.** It says "sibling proposal LIT-1111 shares backlog_id EVB-1585 and is deliberately left 'proposed' -- the literature-grounding route is unaffected by this substrate gap." In fact **LIT-1111 belongs to MECH-515, backlog EVB-1611**; MECH-474's literature sibling is **LIT-1082 (EVB-1585)**, and it is **`blocked_substrate`, not `proposed`**. So the note's stated intent -- keep the literature route open, because a substrate gap cannot block a literature review -- was NOT achieved on the actual sibling. See GOVERNANCE FLAG 1.

**On SD-083 (the campaign's G1 finding), asked directly:** SD-083 `consolidation.offline_policy_consolidation_window` is `candidate_substrate_landed`, implemented 2026-07-29, but its locus is **`ree-v3/experiments/_lib/mech457_offline_consolidation.py`, NOT `ree_core/`** -- the claim's own `implementation_note` says so explicitly ("a MECH-476 falsifier INSTRUMENT, not a cognifold faculty"), and its knob `BootstrapExplorerConfig.use_offline_consolidation` defaults `False`. It is therefore **an implementation of ONE FIXED ARM of MECH-474's design (regime 4, offline consolidation), not a selector and not control-plane substrate**: it is switched by run configuration at start, never state-dependently chosen. Its telemetry is **not reusable as evidence for meta-SELECTION** -- 836b/836c/836d/836e vary INTERVAL and NOVELTY *within* the offline arm and never place an offline regime against an online regime as alternatives something chooses between. Worse for the prior: **V3-EXQ-836e (interval) and V3-EXQ-836d (novelty) are both `status: FAIL`, `evidence_direction: weakens`** for MECH-476 (836b is `superseded`), and MECH-476 is now `retired` (superseded by MECH-459/460). So the one regime MECH-474 would have counted on to win a sub-task in the fixed-arm baseline has, on the only substrate that instruments it, failed to produce a retention benefit. That **lowers the prior that the non-degeneracy guard can be met** and is the single most decision-relevant fact for whoever eventually authors this experiment. (Note also the SD-083 id collision resolved 2026-09-01: the `substrate_queue.json` build task formerly called SD-083 was renamed to `mech324_reacquisition_window_isolation`; the CLAIM keeps SD-083. Do not read the queue entry as this claim.)

**On the plasticity-window memory, asked directly:** MECH-474 is **V3-scoped and NOT `substrate_conditional` on the plasticity-neuromodulator territory** (`project_plasticity_window_neuromodulators`). That memory is about a state-conditional plasticity **GAIN scalar** (ACh / PV / BDNF gating *how strongly* any learning writes) and it explicitly lists the "common confusion" adjacents. MECH-474 selects **WHICH learning process runs**, not how hard it writes -- a different quantity on a different axis, and it needs no neuromodulatory gain scalar to be tested. **Flagging the confusion the memory asks to be caught:** MECH-474's phrase "state- and mode-dependent" is exactly the wording most likely to make a future session file it under ACh-gating. It should not be. MECH-474 is blocked by MECH-094's write-suppression of simulated content, which is an entirely separate mechanism.

**Substrate scan result (the selector question, asked directly):** `grep ree_core/` for `learning_mode`, `plasticity_gate`, `meta_select`, `update_rule`, `learning_rate_schedule`, `consolidation_mode` returns **only** `ThetaBuffer.set_consolidation_mode()` (`latent/theta_buffer.py:235`, called from `agent.py:12411/12485` to bracket the SWS schema pass). **There is no selector over learning mechanisms in `ree_core/`.** What DOES exist, and is the material finding of this pass, is `ree_core/cingulate/salience_coordinator.py` -- see GOVERNANCE FLAG 2.

**epistemic_category (proposed):** `substrate_conditional` (currently `standard`). This satisfies the sharpened discriminator in `REE_assembly/CLAUDE.md`: the mechanism has genuinely never been exercised (0 runs, 0 evidence either way) and the precondition gate would refuse a run at setup, so no non-degenerate attempt is possible -- it is not `substrate_ceiling`, which requires the mechanism to have been built and run repeatedly. **Caveat to record with the tag:** this is an unusual sub-case -- the missing substrate is not merely unbuilt but *deliberately forbidden* by a `stable` claim, so "wait for the upstream substrate" is the wrong remedy; the remedy is a governance adjudication. **If governance narrows the registered menu to three regimes, the category reverts to `standard` and the claim is testable immediately** on the design drafted below.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (three parts, all mandatory, checked BEFORE any verdict is read).**
> **(P1) Every fixed arm must be a real learning path.** Each regime named in the registered menu must, when pinned, actually change parameters. This is currently FALSE for "counterfactual simulation": `REEAgent._do_replay` (`ree_core/agent.py:10501`) discards its replay trajectories (dead assignment, no update), MECH-319's `simulation_mode_rule_gate` suppresses arbitration-weight writes during ghost/replay/DMN passes, `GhostGoalBank` carries no trainable parameters, and the only replay that drives updates lives inside `run_rem_attribution_pass` -- which IS regime 4 (offline consolidation), not regime 3. A pinned regime-3 arm is therefore a structurally inert no-learning arm and `experiments/_lib/precondition_gate.assert_no_structurally_unsatisfiable_gate` must refuse the run. **Until the registered menu is adjudicated (narrowed to three, or MECH-094 revisited), this precondition cannot be met and NO verdict on MECH-474 is admissible.**
> **(P2) The task mix must actually dissociate the regimes.** In the FIXED-ARM baseline, run first and read before the selecting arm ever runs, **at least two distinct regimes must each win on a DIFFERENT sub-task**, each win exceeding a margin scaled on the SD of the per-sub-task delta across seeds plus an absolute floor. If one regime dominates every sub-task there is nothing to select between: report `substrate_not_ready_requeue`, not a verdict. Prior evidence says do not assume this: the offline-consolidation regime, on the only substrate that instruments it (SD-083, `experiments/_lib/mech457_offline_consolidation.py`), produced `weakens` on both V3-EXQ-836d and V3-EXQ-836e.
> **(P3) The selector must be observed to switch.** Log the realised regime-choice distribution per seed and per sub-task. A selector whose distribution is degenerate (one regime above a pre-registered occupancy ceiling, e.g. >0.9 of decision points, or entropy below a pre-registered floor) is a fixed arm wearing a different label; its result is not evidence about selection and must be reported as degenerate, not as PASS or FAIL.
>
> **CONFIRMING (MECH-474 supported).** With P1-P3 met, the selecting arm's per-sub-task and aggregate performance **beats EVERY fixed-regime arm**, not merely their mean, by a margin scaled on the SD of the DELTA (paired across shared seeds) plus an absolute floor. The every-regime bar is load-bearing and is not negotiable: **beating the mean is satisfied by a selector that always picks the single best fixed regime, which demonstrates no selection at all.** Additionally, the selector's realised choice must **covary with the state/mode variable** the claim names -- i.e. the regime chosen on sub-task X differs systematically from the regime chosen on sub-task Y, in the direction the fixed-arm baseline (P2) says each sub-task rewards. A selector that beats every fixed arm while choosing at random or choosing invariantly with state supports "an ensemble helps", not "the control plane selects".
>
> **FALSIFYING (one universal learning rule suffices).** With P1-P3 met, the selecting arm fails to beat the best fixed regime -- i.e. its aggregate falls within, or below, the margin band around the best single fixed arm -- on a mix the baseline has DEMONSTRABLY shown to dissociate the regimes. This is a clean, decision-relevant negative: regime meta-selection buys nothing at this granularity, and REE should keep applying one learning rule with the mode-conditioned write gating it already has (MECH-261). A second, weaker falsifying pattern: the selector beats every fixed arm but P3's choice distribution shows it collapsed onto the single best regime -- that falsifies *selection* while leaving the ensemble result intact, and must be reported as such rather than as support.

**Proposal sketch:** not applicable under disposition (f) -- EXP-0401 already exists and holds the design; it should stay `blocked_substrate` and be UNBLOCKED (not re-minted) the moment governance adjudicates. The one edit EXP-0401 needs on unblocking is to its `design` field: with a three-regime menu, "fixed-regime arms (one per regime)" becomes three arms, and the `*** SCOPE: NARROW FORM ONLY ***` warning should be re-worded so it forbids re-ADDING counterfactual simulation as well as forbidding imitation / language-mediated scaffolding.

**depends_on additions (if any):** add **MECH-094** and **MECH-319** to `depends_on` (or, if `depends_on` is reserved for build prerequisites in the ARC-092 sense, record them as an explicit `blocked_by` on the claim). This is a genuine build/adjudication dependency, not a topical reference: MECH-094's write-suppression is precisely what makes one of the claim's four registered arms unsatisfiable, and both proposals already carry `blocked_by: [MECH-094, MECH-319]` while the claim itself records nothing. Note this is the *opposite* shape to the 2026-08-10 ARC-092 edge correction on this same claim (which removed a topical, non-build reference) -- here the falsifier design demonstrably does invoke the mechanism.

**digestion_note (durable text proposed for the claim):**
> DEFERRED at digestion 2026-09-04. Not testable as registered. The four-regime menu names "counterfactual simulation", which has NO learning path in V3: `_do_replay` discards its trajectories, MECH-319 suppresses rule writes during ghost/replay/DMN, and building a write-enabled counterfactual learning regime would contradict MECH-094 (status `stable`). A pinned regime-3 arm is structurally inert, so this claim's own pre-registered non-degeneracy guard can never be met on the registered menu and the precondition gate will refuse the run. This is a GOVERNANCE ADJUDICATION, not a build: either (a) narrow the registered menu to the three regimes REE has -- after which EXP-0401 is buildable as a three-regime falsifier and this claim reverts to `standard` -- or (b) decide deliberately how a counterfactual-learning regime coexists with MECH-094. **The menu must not be narrowed silently.** EXP-0401 / EXP-1081 / LIT-1082 all `blocked_substrate`; 0 runs, 0 exp_conf, fan-in 0. Separately: MECH-261's SalienceCoordinator already supplies a built, exercised, state-dependent soft mode vector over exactly {external_task, internal_planning, internal_replay, offline_consolidation} plus an `e3_policy` write gate -- read the merge-pressure note before designing a NEW selector.

---

#### GOVERNANCE FLAG 1 -- `stale_note`
**MECH-474's blocked_note names the wrong literature sibling, and the intent it states was not carried out.** The note (identical text on EXP-0401, EXP-1081 and LIT-1082 in `evidence/planning/experiment_proposals.v1.json` and `manual_proposals.v1.json`) asserts: *"sibling proposal LIT-1111 shares backlog_id EVB-1585 and is deliberately left 'proposed' -- the literature-grounding route is unaffected by this substrate gap."* Verified: **LIT-1111 has `claim_id: MECH-515` and `backlog_id: EVB-1611`**, and is unrelated to MECH-474. MECH-474's actual literature sibling is **LIT-1082, backlog EVB-1585 -- and it is `blocked_substrate`, not `proposed`.** Two consequences: (a) the note is factually wrong about which proposal it is describing; (b) the substantive point it makes is right and should be ACTED ON -- a `blocked_substrate` gate on the *experimental* route is not a reason to block a *literature review*, so **LIT-1082 should be returned to `proposed`**. The literature route (meta-learning / learning-to-learn, complementary learning systems, arbitration between model-free and model-based control) is exactly where a claim with zero evidence and a governance-blocked experimental route can still make progress -- and the intake's own `/lit-pull` routing already asked for it while warning that CLS is heavily represented already (MECH-316, ARC-064, MECH-211).

#### GOVERNANCE FLAG 2 -- `contested_disposition` (merge pressure toward an already-built mechanism; PROPOSE ONLY, partial absorption)
**MECH-261 already instantiates most of MECH-474's mechanism content, and nobody has noticed.** MECH-474's `notes` dismiss MECH-261 as partial precedent that "gates WHICH SUBSTRATE MAY WRITE by mode". Read at source, it is substantially more than that:
- `ree_core/cingulate/salience_coordinator.py:75` `DEFAULT_MODE_NAMES = ["external_task", "internal_planning", "internal_replay", "offline_consolidation"]` -- **a four-way mode set that maps almost one-to-one onto MECH-474's four-regime menu**, including the same `offline_consolidation` and the same replay/simulation mode.
- `tick()` computes `operating_mode` as a **soft probability vector via softmax over state-driven affinity logits** (`dacc_pe`, `dacc_foraging`, `dacc_difficulty`, `drive_level`, `is_offline`) with MECH-266 asymmetric enter/exit hysteresis. That is a **state-dependent selector over modes**, built and running.
- `DEFAULT_GATE_WEIGHTS` (line 87) is a per-target x per-mode gain table whose targets include **`e3_policy`** -- "E3 policy update direct gate" -- consumed at `agent.py:7662` (`e3_gate = self.salience.write_gate("e3_policy")`), plus gate-modulated EMA updates for `sd_033a` (rule state, `agent.py:7804`) and `sd_033b` (OFC state code, `agent.py:7970`).
- It has **behavioural evidence**: `v3_exq_455_sd032a_salience_behavioral_20260420T223056Z_v3` records `evidence_direction_per_claim: {SD-032a: supports, MECH-259: supports, MECH-261: supports}`, and `use_salience_coordinator` appears in ~20+ experiment drivers.
**What this changes.** MECH-474's assertion decomposes into two parts. Part A -- *"the control plane selects among learning regimes, state- and mode-dependently, rather than applying one rule universally"* -- is **already built, exercised, and supported** by MECH-261 at the write-gain granularity. Part B -- *"and this selection outperforms every fixed regime"* -- is **genuinely unregistered and untested**, and is the real residual. So this is partial absorption with a narrowed residual, not clean supersession. **Concrete consequence for the eventual build: the MECH-474 falsifier is not a new selector, it is an ABLATION of an existing table.** Fixed arms = `SalienceCoordinator` pinned to each mode (or `use_salience_coordinator=False` plus a hand-pinned mode) vs. the live mode vector, on a mix that dissociates them. That is a far cheaper experiment than EXP-0401's 300-minute multi-arm design assumes, and it does not require building anything. Caveats stated honestly: (i) `use_salience_coordinator` defaults **False** and `salience_apply_to_dacc_bias` defaults **False**, so the gate's reach into learning is currently a dACC score-bias scaler plus two EMA updates -- it does **not** gate the actor-critic policy gradient itself, which is a real gap between MECH-261 and MECH-474's "learning mechanism" framing; (ii) MECH-261's gate table is **hand-specified and fixed**, not learned, so it selects but does not adapt; (iii) pinning to `internal_replay` reproduces the same inert-arm problem as regime 3, so a three-mode pin (`external_task` / `internal_planning` / `offline_consolidation`) is what is satisfiable. **Recommended governance action:** do not merge or retire either claim. Amend MECH-474's `notes` to record MECH-261 as a *substantially instantiating* precedent rather than a partial one, restate the claim's testable residual as Part B above, and add MECH-261's mode vector as the named selection substrate -- ideally in the same pass that adjudicates the four-vs-three menu question.

#### GOVERNANCE FLAG 3 -- `evidence_discrepancy`
**A landed negative bears on this claim's non-degeneracy guard and is not recorded against it.** V3-EXQ-836d (`novelty_tagging_consolidation_redesign`) and V3-EXQ-836e (`interval_dependent_consolidation_redesign`), both `status: FAIL`, `evidence_direction: weakens`, exercised SD-083's offline policy-consolidation window -- the only V3 implementation of MECH-474's regime-4 learning path -- and found no interval- or novelty-dependent retention benefit (their consumer claim MECH-476 is now `retired`, superseded by MECH-459/460). MECH-474's non-degeneracy guard requires at least two regimes to win on different sub-tasks in the fixed-arm baseline; this result is direct evidence that offline consolidation may not be one of them. It should be recorded on MECH-474 as a prior-lowering note (not as `weakens` -- the runs did not test MECH-474 and `claim_ids_tested` is `["MECH-476"]`), so that whoever unblocks EXP-0401 reads it before spending 300 minutes on a design whose step-0 gate may fail.

---

<!-- S_ARC-037 appended 2026-09-04T21:26:48Z -->
## G16 -- ARC-037 (solo)  (agent report)

### Solo note
Solo claim: no group preamble. ARC-037 lost its only strong partner (SD-047, routed to G10) because the edge
was lexical. The cross-claim work that a group would have supplied was done instead against the
already-digested self-attribution/comparator cluster (INV-076 / MECH-257 / SD-029 / SD-031 / MECH-095,
applied 2026-08-27, and MECH-256's standing `digestion_note`) plus the two claims that turn out to own
ARC-037's two legs (MECH-072, MECH-136). Verdict on the three options the task posed: **(i) with a
sharpening**. ARC-037 is the architectural umbrella, but its unique residual is narrower than its own text --
see "Decomposition" below. It is **not** a duplicate of ARC-061 (that claim is the *producer* family; ARC-037
is the *consumer*), and it does carry a non-load-bearing out-of-domain anatomy leg.

---

### ARC-037 -- REE requires a causal attribution routing circuit (anterior insula equivalent) that classifies pred...

**Recommended disposition:** **(c) substrate-blocked -> `substrate_conditional`**, carrying (g) partial merge
pressure and (c2) a named out-of-domain leg -- the E3 half of the routing circuit does not exist in `ree_core/`
at all, the E1 half exists only as a dormant parameter fed either a constant or an environment oracle, and the
one run that ever exercised the E1 half did so offline under a ground-truth axis its own autopsy declared
wrong; so zero non-degenerate exercises have been possible, which is CLAUDE.md's `substrate_conditional`
definition and not `substrate_ceiling`.

**Extracted from:** MECH-071's own `what_would_answer` (ARC-037's own `depends_on`) for the calibration-gap
metric, its EXQ-026 >0.03 threshold, and -- decisively -- its `CAVEAT` about the `transition_type` axis;
MECH-072's title/criteria for the E1-leg operationalisation; `failure_autopsy_V3-EXQ-877_2026-08-03.md` for
the ground-truth-axis defect; ARC-037's own `notes` for the two named misrouting pathologies. Not drafted
fresh -- every element below is an extraction plus one composition step (the dissociation).

---

#### Decomposition (this is the load-bearing finding)

ARC-037 as written is three assertions welded together. Two are already owned elsewhere:

| Leg | ARC-037's text | Already owned by | Status of that owner |
|---|---|---|---|
| **Classifier** | "a module that reads causal_sig ... and classifies each prediction error event as agent-caused or environment-caused" | **MECH-256** (general single-pass comparator), concretely **SD-029** (z_harm_s) / **SD-031** (z_world); **MECH-095** (TPJ, the built one); umbrella'd by **ARC-061** | MECH-256 candidate/v3_pending with a standing `digestion_note`; SD-029 + MECH-095 `substrate_ceiling`; SD-031 standard/blocked on GAP-6 |
| **E1 leg** | "Environment-caused errors: routed to E1 world-model update and residue field R(x,t), not E3" | **MECH-072** -- "Foreseeable-harm gating on residue accumulation reduces false attribution without degrading harm avoidance" | candidate/`v3_pending`; one run (V3-EXQ-877, FAIL/weakens, reclassified `non_contributory` on a measurement defect) |
| **E3 leg** | "Agent-caused errors: routed with full weight to E3 harm_eval and trajectory planning updates" | **MECH-136** owns the *magnitude* (agency-gain correction), not the routing | candidate, no evidence, no `what_would_answer` |

**ARC-037's unique residual is therefore the DIFFERENTIAL/dissociation assertion**: that ONE shared attribution
signal gates BOTH channels in OPPOSITE directions -- the dorsal/ventral striatal dissociation Dorfman et al.
(2021) reports. Nothing else in the registry asserts that. A per-channel gate (MECH-072 alone) is a strictly
weaker claim and is *not* what ARC-037 says. The falsifier below is written against that residual, and
deliberately does **not** re-derive the classifier question (see MECH-256 / SD-029 / SD-031 / MECH-095's own
`what_would_answer` fields -- do not re-derive) or MECH-072's own single-channel question.

---

#### Currency check (what was verified, and against what)

1. **The E3 leg does not exist.** `grep -rn "ARC-037"` over `ree-v3/ree_core/` returns **nothing**. No routing
   module; `ree_core/predictors/e3_selector.py` and `e2_harm_*.py` contain no agency/agent-caused/`owned`
   conditioning of any kind (only unrelated "blocked-agency" MECH-353 score-bias strings). There is no E3-side
   consumer of any attribution signal.
2. **The classifier exists but its output is consumed by nothing.** `ree_core/comparator/tpj_comparator.py`
   (MECH-095) computes `agency_signal` and a boolean `is_self_caused`. In `ree_core/agent.py` these are cached
   as `_tpj_last_agency_signal` / `_tpj_last_is_self_caused` (lines 3945-3950) and the agent's own comment says
   "cached for diagnostics". Grepping every consumer of those two attributes across `ree_core/`,
   `experiments/_lib/`, and `tests/`: only `experiments/_lib/stream_recorder.py:349` (a recorder) and
   `tests/contracts/test_tpj_bla_wiring_contracts.py` read them. **The boolean label
   `_tpj_last_is_self_caused` is read by no production code path at all.** Master flag `use_tpj_comparator`
   defaults `False` (`ree_core/utils/config.py:3995`). The comparator module's own docstring shows the intended
   wire (`residue.set_agency_context(attribution)`) -- `set_agency_context` **does not exist anywhere in the
   repo**. It is an aspirational docstring, i.e. exactly ARC-037's missing circuit.
3. **The E1 gate exists as a dormant parameter.** `agent.update_residue(harm_signal, world_delta, hypothesis_tag,
   owned)` gates residue accumulation on `owned` (`agent.py:10745`: `if owned and not hypothesis_tag ...`) and
   scales it by `world_delta` (`residue/field.py:667`, capped 2x). Both are the ARC-037 E1 hook. Their live
   values: the canonical harness (`experiments/_harness.py:363`) passes `world_delta=None, owned=True`
   unconditionally, and **no caller anywhere in `experiments/`, `ree_core/` or `tests/` passes a non-None
   `world_delta`**. The handful of scripts that vary `owned` (`v3_exq_001`, `040`, `671a`, `809`) source it from
   `info["transition_type"] == "agent_caused_hazard"` -- the **environment's ground-truth oracle**, not the
   agent's own comparator. So even the E1 half is not agent-computed anywhere in the live path.
4. **The E1 half HAS been exercised once, under a different claim tag -- and this is not recorded on ARC-037.**
   `v3_exq_877_mech072_discriminator_gate_full.py` (2026-08-02, FAIL/weakens) gates residue accumulation on the
   real ARC-033/SD-011 counterfactual `causal_sig` (`should_accumulate` at line 593, feeding an eval-side
   `eval_residue.accumulate(...)`). Its `CLAIM_IDS = ["MECH-072"]` -- ARC-037 is not tagged. It is nonetheless
   the only run in the corpus that instantiates any part of ARC-037's routing. It does **not** convert ARC-037 to
   `substrate_ceiling`: the gate was applied to a shadow/eval residue field rather than the live learning
   channel, the E3 arm was absent, and the run's verdict was reclassified `non_contributory` /
   `measurement_test_design_defect`, not a ceiling hit.
5. **The ground-truth axis is the decisive precondition, and it is now known to be wrong.**
   `failure_autopsy_V3-EXQ-877_2026-08-03.md` (confirmed) established that CausalGridWorldV2's
   `agent_caused_hazard` / `env_caused_hazard` labels encode **hazard-object provenance** (diachronic: did the
   env place this tile, or did the agent's own contamination footprint), whereas the comparator computes
   **proximal avoidability** (instantaneous: would a different action this tick have avoided it) -- and the two
   are **anti-correlated for the contamination mechanic**. MECH-071's own `what_would_answer` carries this
   forward as a standing CAVEAT. Every existing `owned=` wiring uses precisely those provenance labels. Any
   ARC-037 test scored against `transition_type` measures the wrong axis.
6. **`depends_on` is current but the `notes` prose is stale.** `SD-003` was repointed to `MECH-256` on
   2026-09-01 (session `sd003-groupAC-20260901`, comment in-block), but the `notes` field still says the module
   "reads causal_sig (from SD-003 counterfactual E2 output)" and calls itself "the architectural bridge between
   SD-003 ... and the learning channels". SD-003 has been `superseded` since 2026-04-18. Prose repair owed.
7. **The V3-EXQ-1001 write is fresh and correct as to direction.** 2026-09-04 governance
   (cycle `governance-20260904-1347`) recorded `non_contributory` and set `epistemic_category: standard`. The
   manifest states verbatim that "ARC-037's own E3/E1 routing/gating is NOT exercised here". `n_ceiling_hits` for
   ARC-037 reads **0**. Confidence: `claim_evidence.v1.json` has **no entry** for ARC-037 (`null`);
   `docs/assets/data/claims.json` shows `assembly_state: gated_v3`, `epistemic_stance: believed`.
8. **No closure node owns ARC-037.** `self_attribution_plan.md` has GAP-1..GAP-6; every one owns a *comparator*
   claim (GAP-1 ARC-033/ARC-058, GAP-2 SD-029/MECH-256, GAP-3 MECH-257, GAP-4 lit, GAP-5 SD-030, GAP-6 SD-031).
   The downstream routing consumer -- ARC-037 -- has no node in that plan or any other.
9. **No substrate_queue entry.** `substrate_queue.json` contains no ARC-037 / routing-circuit / insula entry.
   Current proposals are the auto-generated boilerplate pair **EXP-1231** ("Reduce uncertainty for ARC-037 via
   targeted experiment runs") and **LIT-1232** ("Improve literature grounding..."), both `proposed`. The older
   chip `chip-proposal-exp-0494` is stale (ids renumbered; see `science_wave_campaign_plan_20260904.md`, and note
   `chip-proposal-exp-0440` already recorded a session mis-attributing ARC-037's objective text to ARC-043).
10. **Literature is genuinely absent for ARC-037** -- verified in the 1001 autopsy against `evidence/literature/`:
    no dedicated targeted review; ARC-037 appears only incidentally inside 3 `targeted_review_ext_005` entries.
    The only source is the single 2026-03-29 MECH-071 lit pull (Dorfman 2021).
11. **The offline escape hatch does NOT apply to ARC-037.** SD-031's 2026-09-04 amend cleared its
    balanced-event precondition for a *comparator-only offline readout* (RandomPolicy collection scored
    offline) while keeping the STANDING PROHIBITION on any design "that reads the residual from the LIVE agent
    loop until GAP-6 clears". ARC-037's assertion is about **routing into learning**, which is by construction a
    live-loop read. The prohibition therefore still binds ARC-037 even though it no longer binds SD-031.

**Answer to the task's specific substrate question (independently verified, and it is a NEGATIVE):** the
`predictor-attribution` head the G2 agent found is `ree_core/amygdala/attribution_head.py`
(`BLAAttributionHead`, SD-035 / MECH-074d). It is **not** what ARC-037 names. Its own docstring is explicit:
it is "a learned, context-conditioned attribution over ContextMemory slots", "an attribution-weighted MIXTURE
OF PER-SLOT HARM predictions", and "ASSOCIATIVE attribution, not a causal-contribution measure". Its output
gates BLA `remap_signal` (`bla.py:499-524`, `remap_requires_attribution`), not the E3-vs-E1 learning channels,
and it says nothing about agent-caused vs environment-caused. **ARC-037 is therefore NOT
`substrate_conditional` on MECH-153 / SD-016**, and those should not be added to `depends_on`. (For the record:
SD-016 is `implemented`/`substrate_ceiling`, MECH-153 candidate -- but they gate the BLA head's input, a
different circuit.)

**epistemic_category (proposed):** `substrate_conditional` -- changing the value set four days ago; see the
GOVERNANCE FLAG below, which is why this is a proposal and not an assertion.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (four parts; all four must be reported in the manifest, else `substrate_not_ready`, NOT a verdict).**
> **(P1) The ground-truth agency partition must be PROXIMAL-AVOIDABILITY, not `transition_type`.** Confirmed
> 2026-08-03 (`failure_autopsy_V3-EXQ-877_2026-08-03.md`): CausalGridWorldV2's
> `agent_caused_hazard`/`env_caused_hazard` labels encode hazard-OBJECT PROVENANCE (diachronic) and are
> ANTI-CORRELATED with proximal avoidability for the contamination mechanic, which is exactly the axis a
> comparator computes. Every existing `owned=` wiring in `experiments/` uses those labels, so this is the
> default failure and must be actively defeated: derive the label by replaying `a_stay` (and, better, the full
> action set) from the pre-action state against the environment's own step function, and report the
> provenance-vs-avoidability agreement rate. An ARC-037 run scored against `transition_type` is refused as a
> verdict. See MECH-071's own `what_would_answer` CAVEAT -- do not re-derive it.
> **(P2) Both channels must be demonstrably MOVABLE in the OFF arm.** E1 side: the residue field must be
> non-empty and `world_delta`-sensitive (report `num_harm_events` > 0 and non-zero residue variance across
> locations -- note the live default is `world_delta=None`, so a run that leaves the canonical harness
> untouched measures nothing). E3 side: `harm_eval(z_world)` must show the graded none < approach < contact
> structure with a calibration gap above the EXQ-026 anchor (>0.03) in the OFF arm -- a flat harm_eval means the
> E3 channel has no calibration for routing to modulate, which is instrumentation failure, not disconfirmation.
> **(P3) The classification input must be non-degenerate.** Agent-caused and environment-caused hazard events
> must both be present at >= the minimum-class count the design pre-registers (V3-EXQ-1001's construction-
> balanced RandomPolicy collection reached 6132 minimum-class events and is the existence proof that this is
> achievable). This is the SAME gate that blocks SD-029's C2, MECH-257's C2 and SD-031's discriminative arm.
> **Important scope note: SD-031's 2026-09-04 amend does NOT release ARC-037.** That amend clears the gate only
> for a comparator-only OFFLINE readout and explicitly keeps the STANDING PROHIBITION on reading from the LIVE
> agent loop until `self_attribution:GAP-6` clears. ARC-037 asserts routing INTO LEARNING and is therefore a
> live-loop read by construction; the prohibition still binds it.
> **(P4) The attribution signal driving the gate must be the AGENT'S OWN comparator output, never the
> environment oracle.** An oracle-driven arm is a legitimate positive control (it upper-bounds the effect) but
> is not a test of ARC-037, which asserts a circuit inside the agent.
>
> **CONFIRMING.** ARC-037's unique content is a DOUBLE DISSOCIATION, not a gate on either channel alone -- the
> classifier question belongs to MECH-256/SD-029/SD-031/MECH-095 and the single-channel E1 question to MECH-072;
> ARC-037 is confirmed only by evidence no one of those can supply. Under a 2x2 (routing OFF / ON) x (channel
> read: E1 residue, E3 harm_eval) design with the same comparator signal driving both gates, ARC-037 is
> supported when the SAME signal moves the two channels in OPPOSITE directions and the interaction term -- not
> either main effect -- clears threshold:
> (C1, E1 leg) env-caused harm events accumulate residue while agent-caused-only gating REDUCES false
> attribution: `false_attr_rate(ON) < false_attr_rate(OFF)` (this is MECH-072's own C1, cross-referenced, not
> re-derived; V3-EXQ-877 measured 0.753 gated vs 0.506 ungated -- the wrong direction -- under the P1 defect);
> (C2, E3 leg) agent-caused prediction errors produce a LARGER `harm_eval` calibration gap under routing-ON than
> routing-OFF, delta >= max(0.03, 1.0 x SD of the per-seed delta), the 0.03 floor taken from MECH-071/EXQ-026;
> (C3, the dissociation itself, and the only criterion unique to ARC-037) the routing-ON minus routing-OFF
> effect has OPPOSITE sign on the two channels, and the interaction exceeds both main effects, on a strict
> majority of >= 3 seeds. Threshold for C3: |interaction| >= max(0.04, 1.0 x SD of the per-seed interaction),
> the 0.04 absolute floor taken from the MECH-095/SD-047 `recall_improvement` anchor already pre-registered in
> `substrate_queue.json` for the sibling comparator test.
> Additionally, the two named pathologies must be REPRODUCIBLE BY INVERSION as positive controls: forcing
> env-caused errors into E3 must inflate harm attribution on non-avoidable events (the "false guilt /
> moral overattribution" arm of the notes), and forcing agent-caused errors into E1 must produce the MECH-136
> moral blind spot (harm_eval under-weighting of the agent's own harm). A routing circuit that cannot be broken
> in these two directions is not doing the work the claim assigns it.
>
> **FALSIFYING.** ARC-037 is refuted -- as distinct from its constituents -- if, with P1-P4 all satisfied:
> (a) C3 fails while C1 and/or C2 pass, i.e. the entire benefit is captured by a SINGLE-channel gate and adding
> the second channel's gate contributes nothing beyond it. That result says there is a *gate* (MECH-072's
> claim, or MECH-136's) but no *routing circuit*, and ARC-037 should then be excreted into whichever of those
> two survives; or
> (b) the two channels move in the SAME direction under the shared signal -- no dissociation, so one common
> learning-rate/salience modulation explains the effect and the agent-vs-environment classification is doing no
> work; or
> (c) the oracle-driven positive control also fails to produce the dissociation, which places the fault in the
> channel architecture rather than in the classifier and refutes ARC-037 independently of any comparator
> result; or
> (d) the effect survives only when the label is `transition_type` provenance and vanishes under the P1
> proximal-avoidability label -- ARC-037 would then be a claim about a diachronic self-occupancy trace, not
> about a comparator-fed routing circuit, and should be re-registered as such (this is exactly routing
> recommendation 2 of the V3-EXQ-877 autopsy, which proposed "a new claim for diachronic/footprint-based
> self-caused-harm attribution ... requiring its own (likely memory/trace-based) mechanism").
> A run that merely reproduces the classifier's own failure (comparator cannot separate the classes) is
> `non_contributory` for ARC-037, NOT falsifying: that is MECH-256/SD-029/SD-031's question and is answered in
> their own `what_would_answer` fields.
>
> **DISPOSITION AS OF 2026-09-04: `substrate_conditional`, not `substrate_ceiling`.** Applying CLAUDE.md's
> sharpened discriminator: the E3-side routing consumer does not exist in `ree_core/` (verified by grep -- no
> agency conditioning anywhere in `e3_selector.py`); the E1-side hook exists as a dormant parameter
> (`update_residue(owned=, world_delta=)`) fed `True`/`None` by the canonical harness and, where varied at all,
> by the environment oracle rather than a comparator; the comparator's own boolean output
> (`_tpj_last_is_self_caused`) is read by no production code; and `use_tpj_comparator` defaults False. Zero
> non-degenerate exercises have been possible, `n_ceiling_hits` reads 0, and no positive evidence is banked
> either way -- which is `substrate_conditional` by definition, not the built-and-repeatedly-exercised
> signature of `substrate_ceiling`. The blocking substrate is NOT the comparator family (that is upstream and
> separately tracked): it is the ABSENT routing/gating module itself, which has no `substrate_queue.json` entry
> and no closure node in `self_attribution_plan.md` (GAP-1..6 all own comparators, none owns the consumer). In
> work-graph terms the wire is `complicated (buildable)` -- source `owned`/`world_delta` from a comparator
> instead of the oracle, add the symmetric E3-side path -- while the *test* of it is `complex (probe-gated)` on
> P1 and P3.
>
> (Digested 2026-09-04, thought-digestion campaign `v3-closure`, G16 solo.)

**Proposal sketch:** not applicable -- disposition is (c), not (a)/(d). The buildable prerequisite is stated
under "depends_on / substrate additions" below rather than as an experiment proposal, because queueing an
ARC-037 experiment before the routing module exists would reproduce V3-EXQ-1001 (a run whose own manifest says
the routing "is NOT exercised here").

**depends_on additions (proposed):**
- **`MECH-072`** -- ARC-037's E1 leg is MECH-072's claim verbatim (foreseeable-harm gating on residue
  accumulation). Currently unlinked in either direction. This is the single most valuable edge to add.
- **`MECH-136`** -- ARC-037's E3 leg presupposes the agency-gain correction; MECH-136 already names ARC-037's
  misrouting pathology ("the moral blind spot described by MECH-136") but the dependency is one-way prose only.
- **`MECH-095`** -- the classifier that actually exists in `ree_core/` (the current `depends_on` names only
  MECH-256, the general/abstract comparator).
- **Cross-reference, NOT `depends_on`: `ARC-061`.** ARC-061 is the umbrella over the classifier *family*;
  ARC-037 is the umbrella over what consumes it. Making one depend on the other would misstate the relation --
  a `related_claims`/see-also edge is correct.
- **Do NOT add** `MECH-153` / `SD-016` (the BLA attribution head is a different circuit -- see the negative
  finding above), and do NOT re-add `SD-003` (superseded 2026-04-18; the 2026-09-01 repoint to MECH-256 is
  correct).

---

### GOVERNANCE FLAGS

**FLAG 1 -- `contested_disposition`.** ARC-037's `epistemic_category` was set to `standard` four days ago
(2026-09-04, cycle `governance-20260904-1347`, from `failure_autopsy_V3-EXQ-1001_2026-09-04`). That artifact's
own stated reason is provenance-clearing, not adjudication: "the claim carries no `epistemic_category` field at
all today, so set one -> `standard`" (autopsy table: "storable and not yet true, so this clears both by value
and by provenance"). This digestion proposes **`substrate_conditional`** instead, on the substrate evidence in
the Currency check above (no E3-side routing consumer anywhere in `ree_core/`; E1 hook dormant; comparator
boolean output read by no production code; `use_tpj_comparator` default False; 0 ceiling hits; no banked
evidence). Note the secondary consequence: `standard` means "exp_conf required for promotion", so ARC-037 is
currently sitting in a bucket whose flags (low_exp / impl_no_exp) will fire against a claim that cannot be
tested at all -- whereas `substrate_conditional` suppresses promote/demote and routes to substrate work, which
is the correct action. Because this contests a same-day governance write, it is raised for adjudication rather
than proposed as an application. (Secondary: `architectural_commitment` would otherwise *infer*
`substrate_coherence`; the explicit `standard` overrides that inference, so this is a live choice among three
values, not two.)

**FLAG 2 -- `stale_note`.** ARC-037's `notes` field still describes the module as reading "causal_sig (from
SD-003 counterfactual E2 output)" and calls itself "the architectural bridge between SD-003 (what was
agent-caused) and the learning channels". SD-003 has been `superseded` since 2026-04-18 (by MECH-256 + SD-029),
and `depends_on` was correctly repointed to MECH-256 on 2026-09-01 -- but the prose was not. Two mentions to
repoint; no scientific content changes.

**FLAG 3 -- `evidence_discrepancy`.** `v3_exq_877_mech072_discriminator_gate_full` (2026-08-02) is the only run
in the corpus that instantiates any part of ARC-037's routing -- it gates residue accumulation on the real
ARC-033/SD-011 `causal_sig` (`should_accumulate`, script line 593) -- yet its `CLAIM_IDS = ["MECH-072"]` and
ARC-037 carries no trace of it. It should NOT be retro-tagged as evidence (the gate ran on a shadow eval-side
residue field, the E3 arm was absent, and the verdict was reclassified `non_contributory` /
`measurement_test_design_defect`), but its ground-truth-axis finding is a hard precondition on any future
ARC-037 test and belongs in ARC-037's `evidence_quality_note`. Related, and separately actionable: routing
recommendation 1 of that confirmed autopsy -- a `/queue-experiment` redesign (proposed letter V3-EXQ-877a) with
a proximal-avoidability ground truth -- **has not landed**: no queue entry (queue holds 3 items, none matching),
no script, no manifest, no `substrate_queue.json` entry, and no chip in `TASK_CHIPS.json`. It is an owed
follow-on now ~4.5 weeks unactioned, and it is the prerequisite that would unblock BOTH MECH-072 and ARC-037's
P1.

**FLAG 4 -- `stale_note` (planning-artifact scope gap).** `self_attribution_plan.md` GAP-1..GAP-6 each own a
comparator claim; none owns the downstream routing consumer. ARC-037 has no closure node in any plan and no
`substrate_queue.json` entry, so nothing re-derives it -- which is how a claim whose two legs are separately
tracked (MECH-072, MECH-136) can have its own integrative assertion go unowned indefinitely. Recommend either a
`self_attribution:GAP-7` (routing consumer) or an explicit note in the plan that ARC-037 is deliberately out of
scope for it.

**FLAG 5 -- `stale_note` (proposal hygiene, low priority).** ARC-037's live proposals are the auto-generated
boilerplate **EXP-1231** / **LIT-1232**. LIT-1232 is genuinely warranted -- ARC-037 has **no** dedicated
targeted literature review (verified against `evidence/literature/`: it appears only incidentally inside 3
`targeted_review_ext_005` entries), and its sole source is one 2026-03-29 Dorfman-2021 pull, which is thin
support for a claim whose entire architecture rests on the dorsal/ventral striatal dissociation. EXP-1231's
boilerplate objective ("Reduce uncertainty for ARC-037 via targeted experiment runs") should not be actioned
while the disposition is `substrate_conditional`. The older `chip-proposal-exp-0494` is stale (ids renumbered),
and `chip-proposal-exp-0440` already recorded a session mis-attributing ARC-037's objective text to ARC-043.

---

### (c2) The out-of-domain leg, named as required

ARC-037's title carries "(anterior insula equivalent)" and its `notes` close with "The anterior insula
substrate is consistent with its known role in interoception, agency attribution, and moral judgement." That
is a neuroanatomical assertion resolvable only by literature, not by any REE run -- a genuine second leg. It is
**not load-bearing**: strike the anatomy and the REE content (a shared attribution signal differentially gating
two learning channels) is unchanged and still falsifiable exactly as drafted above. So the correct handling is
reframe-to-the-REE-leg, with the anatomy leg routed to **LIT-1232** (which is the right vehicle and is
independently justified by the total absence of a targeted review). This is a *fused* claim only in the weak
sense -- the anatomy is motivation and naming, not a premise -- so it does **not** warrant an `out_of_domain`
category on ARC-037 itself.

### (g) Merge pressure, PROPOSE ONLY

Not a merge to execute, but the pressure is real and points at two already-registered claims rather than at a
group sibling:
- **Surviving id: ARC-037** (narrowed). **Text that should MOVE OUT:** the classifier sentence ("a module that
  reads causal_sig ... and classifies each prediction error event as agent-caused or environment-caused") is
  MECH-256/SD-029/SD-031's content and should become a cross-reference; the E1-routing sentence
  ("Environment-caused errors: routed to E1 world-model update and residue field R(x,t), not E3") is MECH-072's
  content and should become a cross-reference. **Text that STAYS:** the differential/dissociation assertion and
  the two misrouting pathologies.
- **Expect PARTIAL absorption with a narrowed residual, not supersession.** After both moves ARC-037 still
  asserts something neither owner does -- that the two channels are gated in opposite directions by one shared
  signal. That residual is what the falsifier above tests, and it is why the recommendation is (c) + (g), not
  (e) excrete.
- **Reverse-deps to repoint if the narrowing is ever applied:** `grep "ARC-037"` over `claims.yaml` shows no
  claim currently lists ARC-037 in its `depends_on` (fan-in 1 as given; the reference in MECH-136's family is
  prose, not a dependency edge), so a narrowing is cheap today. Outside `claims.yaml` the references are:
  `experiments/v3_exq_1001_ext005_sd031_attribution_causal_shift.py` (secondary claim tag),
  `failure_autopsy_V3-EXQ-1001_2026-09-04.{md,json}`, `evidence/planning/governance_flag_triage_20260901.md`,
  `literature_claim_tag_audit.md`, `proposal_tick_massmint_triage_20260901.md`,
  `thought_intake_2026-08-04_milestone_inspectable_artificial_organism.md` (which links ARC-037 to
  `GOV-V3FREEZE-1`'s inspectability framing), and `thought_digestion_staged_2026-09-04_v3closure.md`. None
  requires repointing for a narrowing; all would need a currency pass if ARC-037 were ever excreted, which is
  **not** recommended.

---

<!-- S_ARC-113 appended 2026-09-04T21:26:48Z -->
## G15 -- ARC-113 (solo)  (agent report)

- **Solo note:** single-claim assignment, so the cross-claim mandate does not apply; the cross-references that would have been group findings are carried inline below against MECH-263 / SD-033b (digested and applied 2026-08-27, REE_assembly `25c05dbd6e`), ARC-062 (the gating claim), ARC-063 and its face family MECH-349/350/351/352, and SD-078 -- none of which are digested here.

---

### ARC-113 -- The rule pipeline is an ORDERED CYCLE of non-collapsible stages: experience -> pattern sensitivity -> candidate regularity apprehension -> ...

**Recommended disposition:** **(f) defer with a durable `digestion_note`** -- the pilot's call stands, but for a *different and narrower* reason than the pilot gave: the stage-implementation audit it asked for is delivered below and it does **not** unblock the claim, because it shows the "intact baseline" ARC-113's own non-degeneracy guard requires is the all-ON FULLSTACK configuration that terminally FAILed at readiness (V3-EXQ-714), while the gate as literally worded is discharged and gates the wrong thing.

**Extracted from:** ARC-113's own `notes` (`FALSIFIER SHAPE` + `NON-DEGENERACY GUARD` blocks) -- turned into house structure and **corrected** from an *ablation* manipulation to a *collapse* manipulation (see "Why the registered falsifier shape is the wrong manipulation" below). Second source: the 2026-09-02 literature pull, specifically Zhu 2026 (arXiv 2607.11696), which is an executed instance of exactly the corrected manipulation. Third source: ARC-062's own `what_would_answer` precondition (2), pointed at rather than re-derived, per brief rule 6.

---

#### Currency check (everything below verified this session, read-only)

| # | Finding | Source checked |
|---|---|---|
| C1 | **ARC-113 still has no `what_would_answer` and no `digestion_note`.** The 2026-08-26 pilot was never applied. | `docs/claims/claims.yaml` L82219-82277 |
| C2 | **Two ARC-113 sessions have run since the pilot, both landed.** (a) 2026-09-02 `/lit-pull` IGW-238: 5 entries, `literature_confidence 0.823`, landed `388dbe5768`. (b) 2026-09-03 `/queue-experiment` IGW-240: proposal **DECLINED**, EVB-1226/experimental -> `blocked_substrate`, landed `436d919981`. | `evidence/planning/igw_routine_ledger.json`; `git show 436d919981` |
| C3 | **The 2026-09-03 decline is sound on the behavioural route and I do not contest it.** Its load-bearing ground is that a stage ablation today returns an *undifferentiated decrement*, which ARC-113's own guard converts into a **refutation** of a claim the run never tested. | `experiment_proposals.v1.json` `gating_reason` (EVB-1226) |
| C4 | **The decline's "zero per-stage discriminating readouts" premise is over-broad.** It grepped for a stage *framework* (`stage_ablation` / `ablate_stage` / `rule_pipeline` / `stage_signature` -- I re-ran all four, still 0 hits). But 6 of the 11 stages already expose a per-mechanism `get_state()` diagnostic surface. Correct statement: there is no *stage-comparison* readout; there are per-mechanism readouts. | `ree-v3/ree_core/**` (table below) |
| C5 | **ARC-113's gate names a release condition that is DISCHARGED as written.** The gate says the release condition is "GAP-B yielding differentiated rule state". ARC-062's own registered `what_would_answer` records C1(c) "ARM_ON rule field matured (`crf_frac_active >= 0.30`)" as **repeatedly, non-degenerately CLEARED** (654j: `crf_frac_active` 0.94). | `claims.yaml` ARC-062 L51004-51068 |
| C6 | **And a second, stronger discharge landed three days after ARC-113 was registered.** SD-078 (`status: candidate_substrate_landed`) measured, on the real CandidateRuleField over the real V3-EXQ-669b context stream: raw `z_world` key -> **1 rule, `max_pairwise_rule_dist` 0.0000**; centered key (`crf_cue_centering=True`) -> **9 rules, dist 1.7011**. Validated by **V3-EXQ-806, PASS/supports, 2026-07-25**. ARC-113 was registered 2026-07-22 and its gate has never been revisited against this. | `claims.yaml` SD-078 L71915+ |
| C7 | **What is genuinely NOT discharged is the downstream conversion ceiling**, MECH-439 F-dominance -- and that binds only the **behavioural** readout (`committed_class_entropy_nats`), not a representation-level one. This is ARC-062 `what_would_answer` precondition (2) verbatim. GAP-B was still `in-progress` / `non_contributory` / brake fired as of 2026-09-02. | ARC-062 `what_would_answer`; EVB-1226 `blocked_note` |
| C8 | **MECH-316 (cross-episode regularity extraction / successor representation) has NO implementation in `ree_core`** -- zero hits for `successor_representation`, `MECH-316`, `cross_episode_regularity`. ARC-113's notes list MECH-316 among the claims that "largely instantiate" its stages. That is **wrong for MECH-316**. | `/usr/bin/grep -rln` over `ree-v3/ree_core/` |
| C9 | **The open chip `chip-20260902-arc113-stage-implementation-audit` is still `open`, unclaimed.** Its deliverable is the table below; it can be discharged from this report. | `TASK_CHIPS.json` |
| C10 | The 2026-09-01 V4 prerequisite cut classifies ARC-113 under **`validation_of_inherited_capability`**, in the "ARC-063 candidate-rule faces (9: MECH-349..352, SD-078, SD-082, MECH-317, ARC-113, MECH-314b)" bucket -- i.e. governance already reads it as a validation item on the ARC-063 family, not a new build. | `evidence/planning/v4_prerequisite_cut_20260901.md` L182 |

---

#### The stage-implementation audit (the claim's own named FIRST MOVE, delivered)

Every "wired" verdict below is grounded in `ree-v3/ree_core/` code, not in a registered flag -- per the chip's own instruction and the registered-but-unwired hazard. "CORE" = unconditionally instantiated in `agent.py`; a `use_*` name = the gating config flag with its **default**.

| # | ARC-113 stage | `ree_core` locus | Wiring | Discriminating readout that exists TODAY | Owning claim |
|---|---|---|---|---|---|
| 1 | experience | `predictors/e1_deep.py`, `latent/zworld_p0.py`, `environment/` | **CORE** (`agent.py:406`) | `z_world` pairwise cosine (SD-078 measured min 0.9767, 0 pairs < 0.8) | SD-008 / SD-066 |
| 2 | pattern sensitivity | `hippocampal/event_segmenter.py` | `use_event_segmenter` = **False** | segment-boundary rate; fast PE-z, slow BOCPD-Gaussian on `z_goal` | MECH-288 |
| 3 | candidate regularity apprehension | `policy/candidate_rule_field.py::_maybe_mint`; `policy/gated_policy.py` | `use_candidate_rule_field` = **False** (and *requires* `use_lateral_pfc_analog=True`); `use_gated_policy` = **False** | `crf_n_active_last`, `crf_frac_active`, `n_minted` (`get_state`, L821+) | **MECH-349** (CREATE face), ARC-062, ARC-063 |
| 4 | representation | `candidate_rule_field::active_rule_state()` -> `pfc/lateral_pfc_analog.py` `rule_state` (gate-modulated EMA) | `use_lateral_pfc_analog` = **False** | **`crf_max_pairwise_rule_dist`** (0.0000 raw vs 1.7011 centered); `lateral_pfc.get_state()` L522 | MECH-350 (REPRESENT face), SD-033a |
| 4b | (retrieval / select gate) | `candidate_rule_field::gate_and_select()` | same flag | `crf_n_maintained_reactivatable`, `maintained_pairwise_distance()` | MECH-351 (GATE face); MECH-338 -- registered "structural slot only, hard-gated on the GAP-L biology lit-pull" |
| 5 | prediction | `predictors/e2_fast.py`, `e2_world.py`, `e2_harm_a/s.py` | **CORE** (`agent.py:407`) | E2 forward-model error; `world_forward` divergence (GAP-A) | E2 substrate |
| 6 | counterfactual simulation | `hippocampal/module.py` rollout; `pfc/frontopolar_analog.py` | rollout **CORE** (`agent.py:410`); frontopolar `use_frontopolar_decommit` = **False** | `frontopolar.get_state()` L453 | SD-003 / ARC-092; SD-033e / MECH-264 |
| 7 | behavioural interaction | `predictors/e3_selector.py` | **CORE** (`agent.py:409`) | `committed_class_entropy_nats` -- **the ceiling-pinned metric** | MECH-439 (the blocker) |
| 8 | outcome comparison | `candidate_rule_field::credit()` (eligibility-trace); `comparator/tpj_comparator.py`, `comparator/suffering_derivative_comparator.py` | CRF flag; `use_tpj_comparator` = **False**; `use_suffering_derivative_comparator` = **False** | availability delta on credit; `_n_retired` | MECH-352 (CREDIT face) |
| 9 | regularity refinement | `candidate_rule_field` retire / availability decay / mature-pool dynamics | `crf_mature_pool_dynamics` = **False**; `crf_availability_maintenance` = **False** | `_n_retired`, availability trajectory, `mature_retire_floor` crossings | ARC-063 amends (654b/666 lineage) |
| 10 | generalisation | `policy/policy_chunking.py` (ChunkAccumulator MECH-323 + ChunkLibrary MECH-324); `policy/policy_decomposition.py`; **MECH-316: ABSENT** | `use_policy_chunking` = **False**; `use_policy_decomposition` = **False**; MECH-316 **not implemented at all** | chunk lifecycle counters (`get_state` L1385/L1719); decomposition `get_state` L851 | ARC-070 / ARC-071; **MECH-316 absent (C8)** |
| 11 | long-term integration | `sleep/bayesian_aggregator.py`, `sleep/cross_module_consolidation.py`, `sleep/replay_sampler.py` | `use_sleep_loop` = **False**; `use_sleep_aggregation_cluster` = **False** | aggregator state dicts L286/L340 | SD-038 / MECH-286 family |

Cross-check against the standing ARC-063 absence record in `REE_assembly/CLAUDE.md`'s epistemic-categories note ("ARC-063's `CandidateRuleField` has landed only 4 of its 6 distinctive mechanisms"): the 4 absent ones map exactly onto **stage 6** (hippocampal-rollout-eligibility shaping), **stage 9** (the full status lifecycle -- split / merge / retire), **stage 8** (structured evidence-trace records) and **stage 11** (sleep wiring). The audit and that note agree independently.

**Four audit findings, in order of how much they move the disposition:**

**A1 (the blocking one, and it is NEW).** 7 of 11 stages -- and every stage that is *specific to the rule pipeline* rather than to the agent's core loop -- sit behind a **default-OFF** flag. So the "intact baseline" ARC-113's own NON-DEGENERACY GUARD demands ("the intact baseline must show LIVE VARIANCE on the discriminating metric FOR EACH STAGE") is **not the default configuration**. It is an all-ON, co-armed configuration -- which is precisely the **FULLSTACK arm, V3-EXQ-714, 2026-07-07: terminal FAIL, self-routed `substrate_not_ready_requeue` at readiness, C2 never scored** (recorded in MECH-263's and SD-033b's `governance_2026_09_01` blocks). ARC-113's guard therefore has a *known-failing* precondition, and neither the pilot nor the 2026-09-03 decline stated this. It is the single strongest reason (f) survives contact with the audit.

**A2 (the constructive one).** The **ARC-063 face family already IS a stage decomposition with independent switches inside one module.** MECH-349 (CREATE) / MECH-350 (REPRESENT) / MECH-351 (GATE) / MECH-352 (CREDIT) partition ARC-113 stages 3, 4, 4b, 8-9 at sub-module granularity, each with its own knob and its own diagnostic. That is the cheapest collapse-test apparatus available and it does not need building -- which materially changes the "not-yet-designable" verdict of 2026-09-03 for the *representation-plane* route, without changing it for the behavioural one.

**A3.** No stage-comparison readout exists (C4): the 6 `get_state()` surfaces are per-mechanism and were never designed to be commensurable across stages. A collapse test needs a *paired* metric on ONE seam, which is why the corrected falsifier below is per-seam rather than the registered 11-way ablation grid.

**A4.** MECH-316 is absent (C8) and MECH-338 is a structural slot only. ARC-113's `WHAT IS NEW` paragraph overstates instantiation for both. Stage 10 (generalisation) is the least-instantiated stage in the cycle.

---

#### Why the registered falsifier shape is the wrong manipulation (this is the correction the pilot alluded to)

ARC-113's registered `FALSIFIER SHAPE` is a **stage ABLATION**: remove or short-circuit one stage, look for a characteristic failure signature. But the property the claim actually asserts is **non-collapsibility** -- that two adjacent stages are not one stage. Ablation and collapse are different manipulations and they license different inferences:

- **Ablation removes capacity.** Any decrement is confounded with capacity loss, and in a substrate with a downstream ceiling every ablation reads the same flat decrement regardless of whether the stages are separable. This is exactly the aliasing the 2026-09-03 decline identified -- and, because ARC-113's guard converts an undifferentiated decrement into a *refutation*, the registered design is not merely uninformative, it is actively unsafe.
- **Collapse holds capacity constant and removes only the BOUNDARY** -- the isolation between two stages. If two stages are genuinely non-collapsible, deleting the boundary must cost something. If it costs nothing, they were one stage. That is the direct falsifier of the asserted property, it needs no downstream behavioural conversion, and it is immune to the capacity confound.

The corrected manipulation has an executed external template. **Zhu 2026** (`entries/2026-09-02_arc_113_stage_isolation_bottleneck_induction_zhu2026`, supports, conf 0.68) reports precisely this: stages that communicate only through a compressed symbolic state outperform a shared undifferentiated context, and the ablations show *the gains come from the isolation itself*, not the stage vocabulary -- the `Struct-SR` variant (structured intermediate representations **without** enforced isolation) collapsed accuracy below even the unstructured baseline. Its recorded `failure_signatures` also establish the test is **non-degenerate in both directions**: on BBEH-Linguini the staged architecture was *worse* than monolithic (pass@1 58.3% -> 46.5%). A manipulation that has been observed to go both ways is a falsifier, not a formality.

Two constraints the literature imposes on the discriminator:

- **Use a FUNCTIONAL discriminator, never a resource/anatomical one.** Jia 2011 (`..._common_dissociable_induction_components_jia2011`, **mixed**, conf 0.58 -- the only non-supporting entry in the pull) shows rule identification and rule extrapolation share a prefrontal-parietal core while recruiting component-specific networks on top. Shared substrate is fully compatible with non-collapsibility. A discriminator keyed on shared modules or shared parameters would read a *working* pipeline as collapsed.
- **Do not expect one-region-per-stage.** Capkova 2025 (conf 0.75, the strongest support: OFC / principal sulcus / ACC lesions produce *qualitatively different* failure signatures) simultaneously records that 2 of 5 lesion groups produced **no** deficit on any parameter, and that OFC and ACC lesions shared some post-lesion signatures. Partial dissociation is the expected positive result; total dissociation is not the bar.

---

**epistemic_category (proposed):** **`substrate_ceiling`** (currently explicit `standard`).

Applying the sharpened 2026-08-07 discriminator in `REE_assembly/CLAUDE.md`: ARC-113's stage mechanisms **are built and have been exercised repeatedly under non-degenerate conditions** -- the GAP-B readiness gates C1(a)-(f) clear cleanly and inheritably (654j: `crf_frac_active` 0.94, GAP-A divergence 0.080, propagation non-vacuity, MECH-448/449 both live) -- and what stops the test is a **downstream, shared** absorber, MECH-439 F-dominance, which is the *worked example for `substrate_ceiling` in that very section*, and which is ARC-062's category too. **Counter-case, stated rather than hidden:** ARC-113's own object -- a stage *comparison* -- has never been exercised at all and has 0 experimental entries, which is the `substrate_conditional` signature. I come down on `substrate_ceiling` because the blocker is shared-and-downstream and because ARC-113 inherits real positive evidence up to the handoff point; a governance reviewer preferring `substrate_conditional` on the never-exercised-object ground would not be unreasonable. **Either explicit value suppresses promote/demote, which is the practical point** -- see GOVERNANCE FLAG 2.

---

**Draft `what_would_answer`:**

> **THE MANIPULATION IS COLLAPSE, NOT ABLATION.** The property asserted is non-collapsibility, so the test deletes the BOUNDARY between two adjacent stages while holding capacity constant -- it does not delete a stage. An ablation removes capacity, and in this substrate every ablation returns the same flat decrement whether or not the stages are separable; because this claim's guard converts an undifferentiated decrement into a refutation, the ablation design would refute a claim it never tested. Ablation is therefore superseded here as the operative falsifier. External template and existence proof that the manipulation discriminates in both directions: Zhu 2026 (arXiv 2607.11696), whose `Struct-SR` arm -- structured stage representations *without* enforced isolation -- fell below even the unstructured baseline, while on BBEH-Linguini the staged architecture lost to the monolithic one.
>
> **NON-DEGENERACY PRECONDITION (four parts; all required, and none is currently met together).**
> (1) *Differentiated rule state must be LIVE in the staged (intact) arm.* Metric: `crf_max_pairwise_rule_dist > 0` with at least 2 concurrently-active rules. This is not a formality -- SD-078 established that under raw-`z_world` keying the pool is structurally capped at ONE rule, so `crf_max_pairwise_rule_dist == 0.0` is a **tautology** (the metric needs two concurrent rules), which is exactly how the V3-EXQ-654b/654d cells were misread as retire-churn. The known-good setting is `crf_cue_centering=True` (SD-078, `candidate_substrate_landed`; measured 9 rules at dist 1.7011 against 1 rule at 0.0000; validated V3-EXQ-806 PASS 2026-07-25).
> (2) *Capacity match at the seam.* The collapsed and staged variants must carry equal parameter count and equal information capacity across the manipulated boundary. Without this the comparison measures capacity, not boundary, and reproduces the ablation confound under a new name.
> (3) *The DV must be read UPSTREAM of the conversion ceiling.* Any committed-behaviour readout (`committed_class_entropy_nats` and relatives) is pinned by MECH-439 F-dominance before any stage manipulation can express itself. **See ARC-062's own `what_would_answer`, precondition (2) "SHARED DOWNSTREAM CONVERSION CEILING" -- do not re-derive it here.** The same precondition is the one MECH-263 and SD-033b both point at. A collapse run scored on committed behaviour is uninterpretable, in either direction.
> (4) *The stages being compared must both be INSTANTIATED in the arm.* 7 of the 11 stages are behind default-OFF flags and MECH-316 (generalisation) has no implementation at all, so the "intact baseline" is an all-ON co-armed configuration -- the FULLSTACK arm, which terminally FAILed at readiness (V3-EXQ-714, 2026-07-07, C2 never scored). Until an all-ON arm clears its own readiness, a whole-cycle test has no valid intact baseline. A **seam-local** arm (two adjacent stages ON, the rest at default) escapes this and is the only currently-designable form.
>
> **FALSIFYING.** For some adjacent stage pair (i, i+1), the capacity-matched **collapsed** variant matches the **staged** variant on that seam's discriminating metric within a pre-registered equivalence bound -- i.e. deleting the boundary costs nothing. Because this is an *equivalence* claim, a failure to reject a difference is NOT sufficient: the bound must be pre-registered as `max(0.5 x SD of the paired-by-seed collapsed-minus-staged delta, absolute floor 0.05 in the metric's normalised units)`, cleared on a majority (>=2/3) of seeds. Collapse-without-loss at ONE seam is a **partial refutation, scoped to that seam** (and MECH-263's own note that it fuses the `representation` and `prediction` stages makes that seam the pre-registered most-likely-fused candidate). Collapse-without-loss at EVERY testable seam refutes the ordered-cycle reading as a whole.
>
> **CONFIRMING.** Each collapsed pair costs a measurable amount that exceeds the equivalence bound, AND the cost signatures are **seam-SPECIFIC** -- different seams degrade different metrics, in the manner Zhu 2026 reports for isolation removal (the system abandons the induced rule and anchors on instance-specific detail) and Capkova 2025 reports across OFC / principal-sulcus / ACC lesions (qualitatively different failures, not a common decrement). A **uniform** cost of equal size at every seam is NOT confirming: that is capacity loss or the conversion ceiling, and is the same undifferentiated-decrement signature the guard already treats as fatal.
>
> **DISCRIMINATOR CONSTRAINT.** The discriminator must be FUNCTIONAL -- "does removing this boundary produce this specific failure?" -- never resource-based or module-based. Jia 2011 (the one mixed entry in this claim's literature pull) shows rule identification and extrapolation share a prefrontal-parietal core while recruiting component-specific networks on top; shared machinery is compatible with functional non-collapsibility, so a shared-substrate discriminator would read a working pipeline as collapsed. Correspondingly, partial dissociation is the expected positive result: Capkova 2025 found 2 of 5 lesion groups with no deficit at all, and shared signatures between OFC and ACC.
>
> **CURRENT STATE.** Not falsified; not tested. 0 experimental entries; `literature_confidence` 0.823 over 5 entries (4 supports + 1 mixed, 2026-09-02). The whole-cycle route is blocked by precondition (4); the behavioural route is blocked by precondition (3). The seam-local representation-plane route is the first non-vacuous test available and is gated only on the corrected gate below, not on GAP-B.

---

**Proposal sketch:** not applicable at (f). Recorded for the governance reviewer as the run to mint **once the gate is corrected**, not to mint now: *"ARC-113 seam-local stage-collapse probe (apprehension/representation seam)"* -- arms `staged` (MECH-349 mint + MECH-350 represent as separate faces) vs `collapsed` (mint writing directly into `rule_state` with no distinct field representation), capacity-matched, `crf_cue_centering=True`, `use_lateral_pfc_analog=True`, DV `crf_max_pairwise_rule_dist` + `rule_state` differentiation, 3 seeds, scored entirely upstream of E3. `related_claims`: ARC-113, ARC-063, MECH-349, MECH-350, SD-078. This is deliberately NOT minted here: ARC-113 carries a standing user-visible DO-NOT-QUEUE gate, and only `/governance` should amend it.

**`depends_on` additions:** add **SD-078** (the differentiation source that discharges the gate's literal wording and supplies precondition (1)) and **MECH-439** (the actual live blocker on the behavioural route, currently unnamed in ARC-113's `depends_on` despite being the whole reason the gate exists). Consider adding MECH-349/350/351/352 -- the faces that concretely instantiate stages 3/4/4b/8-9 -- though ARC-113's own "do NOT re-register them" instruction argues for leaving those as prose cross-references only.

---

#### Exact `digestion_note` text to write (disposition (f))

```
digestion_note: >
  [2026-09-04 thought-digestion, solo pass; supersedes the un-applied 2026-08-26
  pilot recommendation, which reached the same (f) on weaker grounds.] DEFERRED.
  Falsification condition IS drafted (see what_would_answer) and is a CORRECTION
  of the FALSIFIER SHAPE in the notes below: the operative manipulation is a
  capacity-matched stage COLLAPSE, not a stage ABLATION. Ablation removes
  capacity, so in this substrate every ablation returns the same flat decrement
  whether or not stages are separable -- and this claim's own non-degeneracy
  guard converts an undifferentiated decrement into a REFUTATION, so the
  registered ablation design would refute a claim it never tested. That is the
  same aliasing the 2026-09-03 /queue-experiment decline identified
  (EVB-1226/experimental -> blocked_substrate, REE_assembly 436d919981).

  THE GATE BELOW IS OVER-BROAD AND MUST BE NARROWED BY GOVERNANCE, NOT OBEYED AS
  WRITTEN. Its stated release condition -- "GAP-B yielding differentiated rule
  state" -- is DISCHARGED: ARC-062's own what_would_answer records C1(c)
  (crf_frac_active >= 0.30) as repeatedly, non-degenerately cleared (654j: 0.94),
  and SD-078 (candidate_substrate_landed; V3-EXQ-806 PASS 2026-07-25, three days
  AFTER this claim was registered) measured 9 differentiated rules at
  max_pairwise_rule_dist 1.7011 under crf_cue_centering=True, against 1 rule at
  0.0000 on the raw z_world key. What is NOT discharged is the DOWNSTREAM MECH-439
  F-dominance conversion ceiling, which binds ONLY behavioural readouts. Corrected
  gate: DO NOT QUEUE ANY ARC-113 TEST SCORED ON COMMITTED BEHAVIOUR until MECH-439
  lifts. Representation-plane tests are not gated by GAP-B.

  THE STAGE-IMPLEMENTATION AUDIT THIS CLAIM NAMES AS ITS FIRST MOVE IS DONE
  (2026-09-04, grounded in ree-v3/ree_core/, not in registered flags; discharges
  chip-20260902-arc113-stage-implementation-audit). Four findings: (1) 7 of 11
  stages sit behind default-OFF flags, so the "intact baseline" this claim's
  non-degeneracy guard requires is NOT the default config -- it is the all-ON
  co-armed FULLSTACK arm, which terminally FAILed at readiness (V3-EXQ-714,
  2026-07-07, C2 never scored). This is why the WHOLE-CYCLE test stays deferred
  even with the gate corrected. (2) The ARC-063 face family (MECH-349 CREATE /
  MECH-350 REPRESENT / MECH-351 GATE / MECH-352 CREDIT) already partitions stages
  3, 4, 4b and 8-9 with independent switches and per-face diagnostics inside one
  module -- the cheapest available collapse apparatus, needing no new build.
  (3) There is no STAGE-COMPARISON readout, though 6 stages expose a
  per-mechanism get_state(); the 2026-09-03 "zero readouts" finding was correct
  about a stage framework and over-broad about readouts. (4) MECH-316
  (cross-episode regularity extraction) has NO implementation in ree_core at all,
  and MECH-338 is a structural slot only -- so the WHAT IS NEW paragraph below
  overstates instantiation for both, and generalisation (stage 10) is the
  least-instantiated stage in the cycle.

  WHAT MUST BE RESOLVED BEFORE THIS LEAVES (f): governance narrows the gate to
  the behavioural route (above), and either (a) an all-ON arm clears its own
  readiness, releasing the whole-cycle test, or (b) a seam-local
  representation-plane collapse probe on the apprehension/representation seam is
  minted under the narrowed gate -- capacity-matched, crf_cue_centering=True,
  scored entirely upstream of E3. Route (b) needs no GAP-B closure and is the
  cheaper path to this claim's first experimental evidence.

  PROMOTES NOTHING; MOVES NO STANCE.
```

---

#### GOVERNANCE FLAG 1 -- `stale_note` (highest value)

**ARC-113's `notes` gate cites a release condition that is discharged, and gates the wrong route.** The gate reads "*** GATED: DO NOT QUEUE THE ABLATION WHILE ARC-062 GAP-B IS UNRESOLVED ***" with release condition "GAP-B yielding differentiated rule state". Differentiated rule state is delivered: ARC-062's own registered `what_would_answer` reports C1(c) repeatedly and non-degenerately cleared (654j `crf_frac_active` 0.94), and SD-078 -- `candidate_substrate_landed`, validated V3-EXQ-806 PASS 2026-07-25, i.e. **three days after ARC-113 was registered** -- measured 9 rules at `max_pairwise_rule_dist` 1.7011 under `crf_cue_centering=True` versus 1 rule at 0.0000 raw. The surviving blocker is MECH-439 F-dominance, which binds **only** the behavioural readout. As written the gate blocks representation-plane tests it has no ground to block. This is the 2026-08-26 pilot's FLAG 5, never applied, now substantiated against a specific landed-and-validated substrate knob rather than the discharged V3-EXQ-654g the pilot cited. **Requested action:** amend the gate to "DO NOT QUEUE ANY ARC-113 TEST SCORED ON COMMITTED BEHAVIOUR while MECH-439 is unresolved", and correct the `WHAT IS NEW` paragraph's instantiation claims for MECH-316 (absent) and MECH-338 (structural slot only).

#### GOVERNANCE FLAG 2 -- `contested_disposition`

**ARC-113's explicit `epistemic_category: standard` on an `architectural_commitment` is the root cause of the recurring auto-minted proposal.** `architectural_commitment` infers `substrate_coherence`, which suppresses promote/demote; the explicit `standard` overrides that and makes the indexer treat ARC-113 as a promotion-gated testable claim. EVB-1226's `reasons` are exactly the resulting flags: `lit_only_above_cap`, `low_exp_conf`, `missing_experimental_evidence`, `insufficient_experimental_replication`. That is why a proposal has now been minted three times (EXP-0486 -> EXP-0274 -> EXP-0278) against a claim whose own notes forbid queuing, burning a full `/queue-experiment` substrate-readiness pass each cycle. Setting an explicit `substrate_ceiling` (my recommendation) or `substrate_conditional` suppresses promote/demote and removes the pressure at the claim level. **This complements, and does not replace,** the machinery work already in flight (`chip-20260903-proposal-tick-honors-claim-gates`, resolved `done`; `chip-20260904-indexer-mints-gated-claims-as-blocked`, still `open`) -- the machinery fix generalises, the category fix is the correct per-claim setting regardless.

#### GOVERNANCE FLAG 3 -- `stale_note` (not this claim; found in passing, cheap to fix)

**SD-033b's applied `what_would_answer` cites a path that does not exist.** It reads "ree_core/pfc_analogs/ofc_analog.py, landed 2026-04-25". Verified this session: `ree-v3/ree_core/pfc_analogs/` **does not exist**; the file is at `ree-v3/ree_core/pfc/ofc_analog.py`. This was raised as FLAG 3 in the 2026-08-26 pilot, was never applied, and the stale path was then carried **into** the corrective 2026-08-27 digestion field (`25c05dbd6e`) -- so a pass whose purpose was correction propagated the defect into a more authoritative field than the note it came from. One-line fix.

#### GOVERNANCE FLAG 4 -- `stale_note` (chip hygiene, no adjudication needed)

`chip-20260902-arc113-stage-implementation-audit` is `open` and unclaimed. Its deliverable -- the 11-row stage table against ARC-062/063, MECH-338, MECH-316 and ARC-069-071, grounded in real consumers, with the no-live-variance stages flagged (its step 4) -- **is the table in this report**. It can be landed to `evidence/planning/arc_113_rule_pipeline_stage_audit.md` and the chip resolved `--status done`, or the chip left open for a session that will also land the file. It should not be re-worked from scratch.

---

#### Cross-references NOT digested here (per task scope)

- **MECH-349** (ARC-063 CREATE face -- the mint) and **SD-034** (closure operator over committed `rule_state` -- the CLOSE face) are being digested elsewhere in this campaign and are untouched here. For the record, both sit inside ARC-113's cycle: MECH-349 is stage 3 (apprehension), SD-034 terminates stage 7->8 (behavioural interaction -> outcome comparison) by releasing the commitment latch. If either digestion drafts a falsifier on the create/close *boundary*, it is drafting one of ARC-113's seams -- worth a cross-pointer at merge time.
- **MECH-263 / SD-033b** (digested and applied 2026-08-27): their shared non-degeneracy precondition is the competence floor / MECH-457, and ARC-113 should **point at ARC-062's `what_would_answer` precondition (2)** for the conversion-ceiling half rather than re-derive either -- which the draft above does. MECH-263's self-declared fusion of the `representation` and `prediction` stages is retained from the pilot as ARC-113's pre-registered most-likely-fused seam.

---

<!-- S_MECH-258 appended 2026-09-04T21:26:48Z -->
## G13 -- MECH-258 (solo)  (agent report)

### Solo note
Solo claim: no structural edge to another UNDIGESTED claim, so the cross-claim mandate is discharged by cross-referencing the already-DIGESTED z_harm_a family (SD-086, SD-087, MECH-219, INV-089/INV-090, MECH-091) and the already-drafted falsifier text of the parent SD-032b and sibling ARC-058 rather than re-deriving; the substantive cross-claim finding is that MECH-258 inherits its non-degeneracy precondition wholesale from SD-086/SD-087 (z_harm_a is measured range-degenerate) and its downstream ceiling wholesale from SD-032b/MECH-439, and is the shared upstream that six reverse-deps hang off.

---

### MECH-258 -- z_harm_a enters action selection as a precision-weighted prediction error (harm_surprise_PE, SD-020) against an internal pain forward model (E2_harm_a), not as a raw magnitude

**Recommended disposition:** (c) substrate-blocked, **`substrate_ceiling`** -- the mechanism is BUILT and has been EXERCISED repeatedly under gates that pass cleanly (597b C0 3/3 + C1 2/3; 862b P1/P1'/P2 3/3, non-degenerate), yet every discriminative reading has been absorbed downstream: by the payoff-dominated E3 score (862b: pe's maximum attainable variance share of ||dACC bias|| is <= 1e-6) and by the committed-action entropy floor (445h: `action_class_entropy = 0.0` in ALL arms, the MECH-439 F-dominance blocker that `REE_assembly/CLAUDE.md`'s own worked example names as hitting "SD-032b's dACC pathway" specifically).

**Extracted from:** the claim's own `functional_restatement` "Falsifiable:" clause (raw-magnitude consumer reproducing Baliki 2010/2012 patterns => precision weighting is unnecessary overhead); the pre-registered C0/C1/C2 of `ree-v3/experiments/v3_exq_597b_mech258_pe_vs_raw_post_spcem.py` (the only run ever tagged MECH-258-only); the redesign spec in `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-597b_2026-05-23.md` section 7; the quantified sensitivity bound in `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-862b_2026-08-29.md`; and, for the liveness half, the already-digested `non_degeneracy_precondition` of **SD-086** and **SD-087** (do not re-derive -- see their own text).

**Currency check:** every "queued"/"not yet built" note on this claim was verified against code and evidence, and four are stale:

1. **BUILT, and default-off on two independent flags.** `E2HarmAForward` exists at `ree-v3/ree_core/predictors/e2_harm_a.py`; the precision weighting is live at `ree-v3/ree_core/cingulate/dacc.py:186-225` (`_affective_pe`: `pe = ||z_harm_a - z_harm_a_pred||`, `pe_out = pe * (1 + min(precision/dacc_precision_scale(500), 3.0))`, then the SD-034 cap and MECH-268 saturation). The forward roll is wired in the live path at `ree-v3/ree_core/agent.py:10016-10044`. Gates: `use_e2_harm_a: bool = False` (`utils/config.py:3545`), `use_dacc: bool = False` (`:3572`), and the consumer gain `dacc_weight: float = 0.0` (`cingulate/dacc.py:67`). So the claim's mechanism is present but reached only by an explicitly-configured run -- check the knob, not the status.
2. **The title FUSES two different mechanisms and only one of them is this claim's.** "harm_surprise_PE, SD-020" is the *encoder training target* -- `harm_surprise_pe_enabled: bool = False` (`utils/config.py:3495`), consumed in `agent.py:11391-11401`, where "expected" is a scalar EMA (`self._harm_obs_ema`), **not** E2_harm_a. The claim's actual subject is the *consumer* path in `dacc.py`. These are separately flagged, separately default-off, and were separately (in)validated. Any falsifier must say which it drives; 597b drove the dACC one and left `harm_surprise_pe_enabled` alone.
3. **"Validation experiment: V3-EXQ-445 queued" is stale.** The 445 series ran to 445h (2026-05-08). Both 445h manifests are `status: FAIL`, `evidence_direction: non_contributory`, and their `evidence_direction_per_claim` covers only `MECH-260` and `SD-032b` -- **MECH-258 is in `claim_ids_tested` with no per-claim direction**, which is why `claim_evidence.v1.json` does not count 445h for this claim at all.
4. **The claim's index reading is much weaker than its own notes suggest.** `claim_evidence.v1.json` -> MECH-258: `genuine_exp_count: 1`, `pass_runs: 0`, `fail_runs: 1`, `exp_conf 0.28`, `evidence_quadrant: plausible_unproven`, `latest_run_id: v3_exq_597b_...20260521T131756Z_v3` (mixed). `lit_conf 0.849` on 9 entries carries the 0.707 overall. So the strength here is literature (Seymour 2019, Chen 2023, Horing 2022, Song 2021), not substrate.
5. **The routed V3-EXQ-597c was never authored.** The 2026-05-24 **confirmed** autopsy routed `/queue-experiment -> V3-EXQ-597c` with a full redesign spec. No `v3_exq_597c*` script exists in `ree-v3/experiments/`, `git log --all -S 597c -- experiments` is empty, `ree-v3/experiment_queue.json` contains no dACC/MECH-258 item, no manifest exists, and `evidence/planning/governance_flags.v1.json` has no MECH-258/597c flag. Open, unexecuted routing, 3.5 months old.
6. **The autopsy's recommended `evidence_quality_note` was never applied.** MECH-258's `evidence_quality_note` in `claims.yaml` still ends at the 2026-05-08 line ("EXQ-445h supports (C1 wins=2/3 seeds) ... First clean supporting evidence"), and `live_status.evidence` still reads `from: failure_autopsy_V3-EXQ-445h_2026-06-19`, `verdict: supports/standard`. Nothing on the claim records the 597b measurement_gap.
7. **SD-020's status moved under this claim.** MECH-258's title asserts it "Upgrades SD-020 from provisional to prerequisite". SD-020 was promoted to `stable` (2026-04-22), **DEMOTED stable -> candidate 2026-08-09** (GFLAG-0005: the promoting run V3-EXQ-324b was a standalone bench reimplementation with zero `REEAgent` / `harm_surprise_pe_enabled` / `compute_harm_accum_loss` references), then re-promoted candidate -> `provisional` 2026-08-10 after V3-EXQ-324d (the first genuine real-flag-path test: 1/5 seeds pass, 4 near-zero/negative, reclassified `non_contributory`). SD-020 is currently `provisional`, not stable, and its own shipped path has still never produced a clean positive.
8. **The Q-040.c lineage is closed by user decision.** `failure_autopsy_V3-EXQ-862b_2026-08-29`: "No 862c mandated (user-confirmed)". Any MECH-258 letter must not be a back-door re-entry into that lineage; it must adopt 862b's stated requirement (a) -- an arithmetic-reachability check at authoring time.

**epistemic_category (proposed):** `substrate_ceiling`

*Why ceiling and not conditional:* the code exists, is reachable, and has been driven -- 597b trained E2_harm_a to R2 0.912/0.937 on two seeds and 862b got the V_s gate to fire on z_harm_a 3/3 (14/2/32 holds) with dACC engagement 3/3. That is real positive evidence up to the handoff point, which is exactly the `substrate_ceiling` signature in `REE_assembly/CLAUDE.md` (2026-08-07 sharpening), and it aligns MECH-258 with the `ceiling_decision: deferred` already recorded on its parent SD-032b rather than minting a new reading.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (four conjuncts; three are currently MEASURED AS FAILING, which is why this claim is tagged `substrate_ceiling` rather than testable-now):
>
> (P1) **z_harm_a must be a live, non-saturated signal.** Do not re-derive this -- it is SD-086's and SD-087's own precondition; see SD-086 `non_degeneracy_precondition` (linear decode of behavioural mode / harm-event status from z_harm_a must clear a floor with non-zero cross-seed variance) and SD-087's. Current reading: FAILING. V3-EXQ-856 (SD-087's own falsifier) and V3-EXQ-857a (Q-086, `num_hazards` 4/1/0) both find within-episode `cov_z_harm_a` far below the 0.05 saturation floor with inverted mode ordering (shelter > avoid > freeze), and the signature survives BOTH the `harm_surprise_pe_enabled` flip and the environment-harshness sweep; the 2026-08-08 GFLAG-0006 correction closed the last escape route (flag-from-start was already tested in 856's ARM_ON). Consequence specific to THIS claim, and it is the sharpest finding of this pass: **a near-constant z_harm_a makes E2_harm_a trivially accurate, so `pe = ||z_harm_a - z_harm_a_pred||` collapses toward a constant near zero.** The high forward R2 (445h 0.94-0.99; 597b 0.91-0.94) that this claim's own `evidence_quality_note` cites as "first clean supporting evidence" is therefore NOT independent support for MECH-258 -- on a range-degenerate target it is the predicted consequence of the degeneracy, and it is equally consistent with the claim being untestable here.
>
> (P2) **The two representations must be separable in this substrate.** Compute, per seed, `corr(model_pe, raw_norm)` where `model_pe = ||z - z_pred||` and `raw_norm = ||z||` over eval ticks. If |corr| is not bounded away from 1 (pre-register, e.g. |corr| <= 0.8), then "PE" and "raw magnitude" are the same variable in this environment and NO downstream design -- behavioural or otherwise -- can discriminate them; the run self-routes `substrate_not_ready`. This is cheap and is answerable by REANALYSIS of series V3-EXQ-597b already recorded (it computed `corr_model_pe` and `corr_raw_norm` per seed), so GOV-REUSE-1 applies: run it before authoring anything.
>
> (P3) **Arithmetic reachability of the scored DV.** Per `failure_autopsy_V3-EXQ-862b_2026-08-29`: `bundle["pe"]` reaches the bias through exactly one path -- `control_required = pe * dacc_effort_cost (0.1)` (`dacc.py:397`) x per-candidate effort (= horizon 10, `agent.py:6919-6923`) x `dacc_weight` (0.5) -- against payoff components `-E3.last_scores` of ~500-1800, giving an upper-bound pe-driven std of ||bias|| of `0.5*0.1*10*sqrt(32)*std(pe) = 2.83*std(pe)` and a measured **variance share <= 1e-6 in every cell (max direct-path |rho| ~ 0.0002-0.0010 against a 0.3 bar)**. Any DV taken on total bias or on the E3 score must be shown, at authoring time, to admit a pe-driven variance share above a pre-registered floor; otherwise the criterion is arithmetically unreachable whether or not the mechanism is real, and a null is uninterpretable. Current reading: FAILING at default gains. NOTE the paired trap: 862b's suggested remedy of a "pe-isolated readout" (`bundle["control_required"]` / `bundle["effort_term"]`, `dacc.py:460-461`) is **NOT** a valid MECH-258 DV, because `control_required` is a deterministic linear function of `pe`, so `corr(control_required, model_pe) = 1` by construction. It is an identity, not a measurement. The escape is arm contrast (PE_FORWARD vs RAW_NORM_ABLATION) on a payoff-NORMALISED behavioural DV, never component isolation.
>
> (P4) **Committed-action diversity must exist at all.** See SD-032b's own `what_would_answer` clause (b) and its `ceiling_routing_note` -- do not re-derive. Current reading: FAILING (445h `action_class_entropy = 0.0` across ALL arms; MECH-439 F-dominance ~88-89% of E3 variance, tracked by ARC-108/MECH-450). Additionally, per 597b, `bias_clip_saturation_frac` must be < 0.1: at `dacc_bias_max_abs = 2.0` against `dacc_suppression_weight = 4.0` the post-clip output was a constant 2.0 in every step of every seed of BOTH conditions, so E3 received no dACC variation at all.
>
> CONFIRMING: with P1-P4 satisfied, a two-arm within-seed contrast holding everything else fixed -- ARM_PE (`use_e2_harm_a=True`, dACC consumes `pe = ||z_harm_a - E2_harm_a(z_harm_a_prev, a_taken)||`) vs ARM_RAW (`use_e2_harm_a=False`, dACC falls back to `||z_harm_a||`) -- shows (a) behavioural-adjustment magnitude in ARM_PE scales with the precision-weighted PE and is materially DECOUPLED from raw z_harm_a magnitude, while ARM_RAW's adjustment tracks raw magnitude; and (b) the context-dependence the claim's `functional_restatement` names: for a matched nociceptive input, adjustment magnitude is larger in the high-precision (unexpected / uncontrollable) condition than the low-precision (expected / controllable) condition in ARM_PE, with no such split in ARM_RAW. Thresholds: PASS requires the ARM_PE precision-split effect to exceed both an absolute floor and a margin scaled on the SD of the per-seed delta, in >= 2/3 seeds, with the per-seed C1 gate from the 597b autopsy applied (exclude any seed whose `harm_a_forward_r2 < 0.3` from the win-count denominator -- 597b's sole "win", seed 13, was a degenerate-regime artefact at R2 = -1.624 on 170 samples).
>
> FALSIFYING: with P1-P4 satisfied, ARM_RAW reproduces ARM_PE's behavioural signature within the seed-noise band -- i.e. a raw-magnitude consumer of z_harm_a delivers the same context-dependence and the same Baliki-style adjustment profile -- which is the claim's own registered falsifier ("precision weighting is unnecessary overhead"). Equally falsifying: ARM_PE shows adjustment magnitude that tracks raw magnitude and is uncorrelated with the precision-weighted PE, once P3 has established that a correlation was arithmetically detectable.
>
> NOT falsifying: any null with P1, P3 or P4 unmet. Six runs now sit in this shape -- 597 (post-clip Pearson undefined), 597b (measurement_gap, suppression term ~80% of pre-clip bias), 475b (z_harm_a never wired), 862 (`dacc_weight=0`), 862a (borrowed 0.85 V_s threshold never crossed by z_harm_a's 0.989-1.000 band), 862b (variance share <= 1e-6) -- and every one was correctly adjudicated `non_contributory` or `mixed`, never `does_not_support`. Preserve that: this claim has zero opposing experimental evidence, and its `plausible_unproven` quadrant should not be read as a negative result.
>
> E3 PSEUDO-REPLICATION HAZARD (form 2, `e3_hold_weighted_readout_lint`): every DV proposed above is accumulated per env step from `select_action`'s return value or the e3_tick-gated candidate list, so it is hold-weighted (`agent.py:5430` returns the HELD action on `not ticks["e3_tick"]`; cadence default 10, 5-20 under MECH-093). Per the triage test, a continuous behavioural-adjustment magnitude is AT RISK (continuous margin against a non-trivial floor), and any distribution-shape statistic -- `action_class_entropy`, PE variance, adjustment histograms -- is DISQUALIFYING, because replication reweights the distribution itself. Do not cite the 663 sub-1% calibration here: the two arms differ in what drives the dACC bias and therefore may differ in hold duration, which is exactly the case the memory says the calibration does not bound (measured spreads to +152%). Any letter must record per-tick fresh-vs-held provenance and score on e3_tick-gated ticks only.

**Proposal sketch:** none. This disposition is deliberately NOT (a). Two reasons, both evidential rather than cautious: the four preconditions above are three-quarters measured-failing, and the user has already closed the adjacent Q-040.c lineage ("No 862c mandated (user-confirmed)"). The right response to a `substrate_ceiling` is substrate enrichment, and the enrichment MECH-258 needs is already owned elsewhere and shared: **SD-086's readout swap** (which, if it restores z_harm_a's cross-state range, clears P1 and P2 at once) and **ARC-108/MECH-450** on the F-dominance conversion ceiling (which clears P4, and clears it for ARC-062, SD-032b and MECH-480 simultaneously). The only cheap thing owed here is the P2 reanalysis of 597b's stored series, which needs no new run.

**Reverse-deps (fan-in 6, all via `depends_on`) and which inherit the precondition:**

| Claim | Status | Inherits? |
|---|---|---|
| **SD-032b** (dACC-analog; "precision-weighted PE drives dACC policy update") | candidate, `ceiling_decision: deferred` | **Fully -- P1-P4.** Its own `what_would_answer` already names clause (a) "MECH-258 ... not yet substrate-validated as live" and clause (b) the entropy floor. Cross-reference it; do not re-derive. Same ceiling, same fix. |
| **MECH-480** (LOFC execution-gain dissociable from dACC strategy authority) | candidate | **Fully -- P3 and P4 especially.** Its DV *is* the dACC authority channel; V3-EXQ-870a came back `non_contributory`. A MECH-480 null is uninterpretable until P3/P4 clear. |
| **Q-041** (unified meta-level threshold supervisor?) | open | **Fully, as a named gate.** Its own note lists MECH-258 among four substrate gates and holds `hold_pending_v3_substrate`. Consistent already; no change owed. |
| **Q-042** (when should the dynamic-precision update fire?) | resolved | **Partly, and its note is stale.** It records empirical resolution as gated on "(a) MECH-258 substrate implementation" -- but E2_harm_a and the dACC PE path LANDED 2026-04-19. The live gate is the ceiling, not implementation. Repoint. |
| **MECH-268** (dACC conflict saturation caps/habituates the pe signal) | provisional | **Only conditionally.** Its validating run V3-EXQ-463 drove the saturation with a SYNTHETIC `z_harm_a_pred = torch.zeros(4)` (`v3_exq_463_mech268_dacc_conflict_saturation.py:220,226`), i.e. a unit-level harness. So its *arithmetic* content (`_saturation_factor`, `dacc.py:236-259`) does not inherit P1/P2, and its `provisional` reading is safe. Any *behavioural* extension of MECH-268 inherits all four. |
| **MECH-259** (salience-network switch threshold) | **stable** | **Partly, and this is the one to look at.** It names MECH-258 as "the magnitude compared against threshold", but its `stable` reading rests on a single genuine experimental entry (`v3_exq_455_sd032a_salience_behavioral`, `genuine_exp_count: 1`, exp_conf 0.575) which drove salience from the coordinator, not from the harm PE. Its promotion does not depend on this claim, but the dependency edge is currently unvalidated in the direction it is written. |

**depends_on additions (proposed):**
- `MECH-439` -- the shared F-dominance conversion ceiling that absorbs this claim's behavioural signal (already the named blocker on SD-032b's `ceiling_routing_note`; making it explicit here lets one ARC-108/MECH-450 fix unblock the cohort visibly).
- `SD-086` -- the z_harm_a readout-form claim whose resolution is precondition P1/P2 for this one.
- Consider recording `SD-020` in the title/notes as **provisional** rather than the pre-2026-08-09 reading (see Currency check 7); the title's "upgrades SD-020 from provisional to prerequisite" is coincidentally correct again after the 2026-08-10 re-promotion, but only by accident.

---

**GOVERNANCE FLAG 1:** `stale_note` -- MECH-258's `evidence_quality_note` and `live_status.evidence` are two adjudications behind. They record only "[2026-05-08 governance]: EXQ-445h supports (C1 wins=2/3 seeds) ... First clean supporting evidence for shared-substrate harm prediction on dACC reef" and `from: failure_autopsy_V3-EXQ-445h_2026-06-19 / verdict: supports/standard`. But (i) both 445h manifests are `FAIL` / `non_contributory` and their `evidence_direction_per_claim` omits MECH-258 entirely, so the index does not count 445h for this claim; (ii) the claim's only counted genuine experiment is V3-EXQ-597b (`mixed`, FAIL, adjudicated `measurement_gap`, confirmed 2026-05-24), whose autopsy wrote a specific recommended `evidence_quality_note` for governance to apply, and it was never applied. Recommend applying that note verbatim and re-pointing `live_status.evidence` to 597b.

**GOVERNANCE FLAG 2:** `contested_disposition` -- V3-EXQ-597c was routed by a **confirmed** failure autopsy on 2026-05-24 (`/queue-experiment -> V3-EXQ-597c`, with a two-fix redesign spec: raise `dacc_bias_max_abs` to 20.0; per-component telemetry with a per-seed C1 gate) and was never authored, never queued, and never run -- verified against `ree-v3/experiments/`, `git log --all -S`, `experiment_queue.json`, the evidence corpus, and `governance_flags.v1.json`. This pass recommends **NOT** simply executing it as specified: 862b's later measurement shows fix 2 as written (component isolation) yields an identity, not a measurement (see P3), and fix 1 alone does not lift P4. Governance should decide explicitly between (a) formally withdrawing the 597c routing as superseded by the ceiling reading, or (b) re-specifying it against the P1-P4 gate. Leaving it silently unexecuted is the worst of the three.

**GOVERNANCE FLAG 3:** `evidence_discrepancy` -- the "harm_a forward R2 = 0.94-0.99 / 0.91-0.94" figure is cited on MECH-258 (and in the 445h substrate_queue metric) as supporting evidence, but on a target measured to be range-degenerate (SD-086/SD-087/Q-086: `cov_z_harm_a` below the 0.05 floor, mode ordering inverted, insensitive to both the training-target flag and hazard density) a near-perfect one-step forward R2 is the *predicted consequence of the degeneracy*, not independent support. Recommend the R2 figure be re-read as a precondition diagnostic rather than as confirming evidence, on both MECH-258 and ARC-058 (whose `what_would_answer` uses per-stream `forward_r2` as its CONFIRMING metric and would inherit the same artefact).

**GOVERNANCE FLAG 4:** `contested_disposition` (low priority) -- MECH-259 is `stable` on `genuine_exp_count: 1` (V3-EXQ-455, exp_conf 0.575) while the `depends_on` edge it declares to MECH-258 ("the magnitude compared against threshold") has never been exercised in a run that supported it. Not a demotion recommendation; a request that governance check whether MECH-259's stable reading is scoped to non-harm salience sources, and record that scoping if so.

---

<!-- S_INV-104 appended 2026-09-04T21:26:48Z -->
## G17 -- INV-104 organism-relevant distinction preservation across compression (solo agent report)

### Solo note

Single-claim group, so the four cross-claim questions reduce to the one the task posed: **is INV-104's
falsifier really ARC-138's operational consequence (fused / derivational), or an independent
measurable?** Answer, with the argument, because it decides the disposition:

**Independent measurable, not fused -- they manipulate different variables and each survives the
other's falsification.**

- **ARC-138** manipulates *the organism* (vulnerability / affordance set), holds observation
  statistics matched, and reads *latent organisation*. Its registered non-redundant prediction is
  exactly that: "agents with matched sensory statistics but different vulnerabilities or affordances
  develop systematically different latent organisations of the same environment".
- **INV-104** manipulates *the compression step* (which distinction classes it preserves), holds the
  organism fixed, and reads *downstream recoverability plus organism-level competence*.
- ARC-138 false / INV-104 true is coherent: latent organisation could be fully determined by objective
  scene structure (ARC-138 refuted) while it remains true that a compression step which destroys
  access to controllability costs downstream competence. Recoverability-of-X is not a claim about what
  *carves* the latent.
- ARC-138 true / INV-104 false is coherent: regulatory constraints could demonstrably shape the
  carving while *no* class is ever actually destroyed by any compression REE uses -- generic
  predictive compression already preserves all five -- making the preservation requirement vacuous.
  This is the cluster's own red-team 5 and MECH-520's counter-constraint, and it is INV-104's
  falsification route F1 below.

**But there is a real OPERATIONAL fusion risk, and it should be fixed at digestion rather than
discovered later.** INV-104's notes say "Its first test is the gated chip named on ARC-138"
(`chip-20260904-regulatory-anchoring-matched-aux`, A perceptual / B matched-arbitrary-auxiliary /
C regulatory anchoring). That experiment's manipulated variable is *regulatory vs arbitrary
anchoring* -- ARC-138's variable. It is a good ARC-138 test and only an indirect INV-104 test: a null
on C-vs-B refutes "regulatory anchoring organises the latent", not "destroying access to class k is a
developmental regression". If that one chip is allowed to stand as the sole test of both claims, a
single null will be read as evidence against both, which is the fused-claim failure mode. **INV-104's
own sharpest test is an ablation/restoration ladder on ONE class with a raw-input ceiling arm and an
untrained-projection floor arm** -- drafted below, and reusing an instrument REE already built.

Two further notes that belong here rather than in the per-claim block:

- **INV-104 is itself internally fused across five classes with wildly different substrate readiness**
  (verified in code and claims.yaml, see Currency check). Class 1 is built and exercised three times;
  class 2 is one default-off knob away; classes 3/4/5 are genuinely unbuilt. One scalar
  `epistemic_category` cannot be right for all five. Flagged below.
- **The measurement precedent the campaign pointed at is directly reusable and its two disclosed
  defects must be inherited as preconditions, not silently reused.** V3-EXQ-972's
  `mean_separability_score = 0.0281` (vs a self-described "conservative", not-derived, noise floor of
  0.05) is the input-side under-differentiation reading for SD-017's write stream. Its own confirmed
  autopsy names both defects: the statistic is an **uncentred cosine contrast** that "does not support
  the stronger *there is no structure for any objective to condition on*", and it has **no permutation
  null for temporal/episode autocorrelation** (the driver's red-team disclosed this and declined to
  fix it; no per-state episode/step index reaches the manifest, so it cannot be computed post hoc).
  The autopsy names the cheap confirmer verbatim: *"a held-out linear probe (logistic regression,
  safe-vs-dangerous) on the same recorded latents."* The draft below adopts that confirmer AND the
  permutation null as preconditions.

**Currency findings (all verified this pass):**

1. **V3-EXQ-1002 is IN FLIGHT, not landed.** `ree-v3/experiment_queue.json` shows
   `status: claimed`, priority 90, 240 min. No manifest under
   `REE_assembly/evidence/experiments/` (1000 and 1001 exist; 1002 does not). So the gate INV-104's
   notes and ARC-138's chip both name is live-pending, not indefinitely deferred -- and its two
   trivial-baseline / ceiling arms are already MEASURED in the queue entry and are reusable now.
2. **V3-EXQ-1002's arms are the instrument INV-104 needs, already calibrated.** Measured and recorded
   in the queue entry: `rawfield_ceiling` (adapter on the raw 25-dim resource_field_view)
   **0.985 / 0.980 / 0.973 held-out**; `zworld_untrained` NEGATIVE CONTROL (same 2x128 MLP adapter on
   an untrained z_world projection) **0.688 / 0.681 / 0.695**; trivial baselines repeat-previous-action
   0.566 / 0.580 / 0.572 and majority-class 0.250 / 0.248 / 0.246. Per GOV-REUSE-1 these are cited, not
   re-run.
3. **SD-070 is IMPLEMENTED but is NOT on any default agent path.** `ree_core/latent/zworld_p0.py`
   exists (ZWorldP0Config + ZWorldP0Trainer), and its own implementation_note says it is
   "BIT-IDENTICAL OFF BY CONSTRUCTION, not by flag ... nothing runs unless an experiment explicitly
   constructs a trainer". Grep confirms: the only callers are experiment drivers via
   `experiments/_lib/zworld_p0_warmup.run_zworld_p0` (728, 898, 948). **Consequence for INV-104: a
   preservation verdict measured without the P0a stage is measuring MECH-523's untrained compression
   site, not a compression step.** This is precondition NDP-1 below and it is the single most
   important non-degeneracy fact for this claim.
4. **Class 2's primitive is BUILT and DEFAULT-OFF, not missing.** `ree_core/utils/config.py:884`:
   `e2_action_contrastive_enabled: bool = False` (weight 0.01, temperature 0.1,
   min_batch_classes 2), commented "Default OFF -- bit-identical to pre-SD-056". Per
   `reference_claim_status_vs_default_off_flag`, the knob is the fact, not the status. Class 2 is a
   knob-flip away, not substrate-blocked.
5. **Classes 3/4/5 are genuinely unbuilt.** Class 3's temporal-spread carrier is the ARC-004 depth
   cascade, which MECH-523 verified is untrained at three sites (beta/theta/delta encoders appear zero
   times in `agent.py`, no loss, no optimiser, one hardcoded shared EMA). Class 4's episode-side
   substrate MECH-430 is `substrate_conditional`, `implementation_phase: v4`. Class 5 needs the
   multi-agent env ARC-047, unbuilt, v4/v5 -- and the causal-compression intake itself refused to chip
   it for exactly that reason.
6. **The class-1 record is more nuanced than INV-104's notes compress it to.** The notes say
   "V3-EXQ-813/948/978: information present, unused". Verified: 978 measured OFF-arm decode
   **r2 0.710 sense-path / 0.858 encoder-path** (present); 948 measured a downstream reader on
   z_world alone at **0.5 res/ep** vs z_world + the raw 25-dim field at **2.233** vs raw obs at
   **9.033**, against a 1.0 competence floor. Those are two different mechanisms -- MECH-517's own
   digestion_note (5) draws exactly this distinction, calling 948 **under-exposure** ("content absent
   from the reader's input") rather than **categorical collapse**. The compressed phrase is defensible
   but the distinction is load-bearing for INV-104: *linear decodability is not the INV-104 test*.
7. **SD-018's substrate_queue amend is stale** -- see GOVERNANCE FLAG 1.
8. **INV-104's `location` doc exists and is current**:
   `docs/architecture/regulation_first_representation.md#inv-104` resolves and carries the five-class
   list verbatim; no doc/claim drift.

---

### INV-104 -- Organism-relevant distinction preservation across representational compression: any compression, abstraction or consolidation step on the observation -> z_world -> E1/E2 path...

**Recommended disposition:** **(a) testable now**, narrowed to a **class-1 pilot with class 2 as the
second arm** -- the instrument (V3-EXQ-1002's capacity-matched frozen-latent adapter), the ceiling
arm, the floor arm and the trained-compression recipe (SD-070 P0a) all exist and are measured, so
nothing here is substrate-blocked; the *run* stays gated on V3-EXQ-1002 (which decides which
interface the organism-level leg is read through) but the *falsifier* is not, and classes 3/4/5
remain `substrate_conditional` rows inside the claim rather than a blanket category on it.

**Extracted from:** the claim's own `notes` (the class list, the "removable scaffolds" clause, the
class-2 three-rival adjudication frame, and the VERSION-ROUTING FLAG's "class 1's directional row has
already been probed"); `docs/thoughts/2026-09-04_z_world_representation_contract.md` sections
"Minimal acceptance criteria" and "Failure modes to guard against" (both lifted almost directly into
CONFIRMING and the preconditions); GOV-MATCHAUX-1's two required controls (used verbatim as
NDP-6 and CONFIRMING (iv)); and two existing REE instruments -- **V3-EXQ-1002's three-arm
capacity-matched adapter design with its calibrated bar** and **V3-EXQ-972's separability probe plus
the held-out-logistic-probe confirmer its confirmed autopsy names**. Nothing below is designed from a
blank page; the only new content is the *normalisation* (retained fraction between a measured floor
and a measured ceiling) and the reconstruction-loss-invariance clause that INV-104's own "regardless
of reconstruction or prediction loss" wording demands.

**Currency check:** see items 1-8 in the Solo note. Verified in source, not assumed:
`ree-v3/experiment_queue.json` (1002 `claimed`, arms measured); `ree-v3/ree_core/latent/zworld_p0.py`
+ grep of all callers (SD-070 off the default path); `ree-v3/ree_core/utils/config.py:884`
(`e2_action_contrastive_enabled = False`); `REE_assembly/evidence/planning/substrate_queue.json`
queue[44] (SD-018 failure_record, amend_status stale); `evidence/planning/failure_autopsy_V3-EXQ-978_2026-09-03.md`
sections 4-7 (r2 0.710/0.858, re-derive brake fired on INV-088 + MECH-457, discriminate-before-build);
`evidence/planning/failure_autopsy_contextmemory-write-content-cluster_2026-09-03.md` sections 2.4 /
3.5 (the 0.0281 measurement, its uncentred-cosine hedge, the named confirmer);
`evidence/experiments/v3_exq_972_.../manifest.json` (H4_NOISE_FLOOR 0.05 self-described as not
rigorously derived; intra/inter cosines 0.9804 / 0.9713 / 0.9478);
`ree-v3/experiments/v3_exq_972_...py` lines 95-130 and 200-225 (the exact statistic and its disclosed
permutation-null gap); claims.yaml blocks for MECH-100 (stable, evidence_quality_note),
SD-009 (candidate, demoted 2026-08-08), MECH-523, MECH-517, MECH-520, SD-070, INV-035, MECH-496,
INV-101, MECH-430, MECH-256, SD-056, ARC-138, GOV-MATCHAUX-1.

**epistemic_category (proposed):** **`standard`** at claim level, **with a per-class readiness table
added to `notes`** (classes 1-2 `standard`/V3-tractable; classes 3, 4, 5 `substrate_conditional`,
blocked on ARC-004 depth-encoder training / MECH-430 (v4) / ARC-047 (v4-v5) respectively).
*Rationale, and it has a mechanical consequence:* the current blanket `substrate_conditional`
suppresses promote/demote and dispatches the reader to "wait for the upstream substrate" -- correct
for class 5, wrong for class 1, whose scaffold (SD-018 directional head) landed 2026-09-02 and ran
green on an 8/8 precondition gate in V3-EXQ-978, and wrong for class 2, whose primitive is a
default-off boolean. Left as-is, INV-104 is frozen behind an unbuilt v4-v5 multi-agent environment it
does not need for its pilot. **Fallback:** if V3-EXQ-1002 returns H-C (geometry mismatch), the
class-1 row -- built, exercised repeatedly, non-degenerate gates passing, signal absorbed downstream --
matches the `substrate_ceiling` discriminator in `REE_assembly/CLAUDE.md` and should be re-tagged
`substrate_ceiling`, not `substrate_conditional`. If 1002 returns H-B, `standard` stands.

**Draft `what_would_answer`:**

> **SCOPE.** This falsifier is written for ONE preservation class at a time, on ONE named compression
> step, and is instantiated here for **class 1 (consequence / opportunity-and-threat)** at the
> **observation -> z_world encoder step** (`ree_core/latent/stack.py` SplitEncoder world path, SD-005),
> which is the only compression site in `ree_core` that has a training signal at all (MECH-523).
> Class 2 (controllability / intervention-sensitivity) is the second instantiation and is reachable by
> setting `e2_action_contrastive_enabled = True` (default False). Classes 3, 4 and 5 are
> substrate_conditional and carry no falsifier yet; per-class falsification NARROWS the preservation
> list, it does not retire the claim.
>
> **THE TWO-TIER MEASUREMENT, because the obvious one-tier version is already known to mislead.**
> T1 (PRESENCE): a held-out probe -- centred logistic regression for a categorical class, ridge for a
> continuous one -- on the frozen compressed representation. T2 (RECOVERABILITY-IN-USE, which is what
> the claim actually asserts): a **capacity-matched supervised adapter** (V3-EXQ-1002's own 2x128 MLP)
> behaviour-cloning an oracle that must use the class, trained from the FROZEN representation, and
> scored as a **retained fraction**
> `R_k = (acc_compressed - acc_untrained_projection) / (acc_raw_input - acc_untrained_projection)`.
> T1 alone is NOT the test: V3-EXQ-978 measured the class-1 field linearly decodable at r2 0.710
> sense-path / 0.858 encoder-path while V3-EXQ-948 measured a downstream reader on that same latent at
> 0.5 res/ep against a 1.0 competence floor (raw obs 9.033). "Present" and "recoverable through its
> dynamics" came apart on this exact class, which is why INV-104's own wording says "preserve, OR leave
> recoverable through its dynamics" and why R_k, not r2, is the verdict statistic.
>
> **NON-DEGENERACY PRECONDITIONS -- all six must be reported in the manifest, and any one unmet makes
> the verdict vacuous rather than negative.**
> NDP-1 THE COMPRESSION STAGE IS TRAINED. `zworld_p0_episodes > 0` (the SD-070 P0a recipe via
> `experiments/_lib/zworld_p0_warmup.run_zworld_p0`), with the P0a held-out grounding lift reported
> (SD-070 measured +0.23 to +0.47 across four heads / 3 seeds; V3-EXQ-978 measured field r2
> 0.678 / 0.627 / 0.653). SD-070 is bit-identical-off by construction and appears on NO default agent
> path, so without this the site is an untrained random projection and a "not preserved" verdict is
> MECH-523's finding restated, not evidence about compression.
> NDP-2 IT IS A COMPRESSION, NOT A COLLAPSE AND NOT AN IDENTITY. z_world participation ratio inside the
> SD-070 trained band, PR in [4.0, 6.5] (measured 5.19 / 5.41 / 4.64 at world_dim=128, 3 seeds; the
> collapsed reference is 1.06; the untrained-random reference is 9.21 / 6.63 / 8.56). At PR ~ 1 the
> run measures SD-070's collapse; at PR ~ untrained-random nothing was compressed.
> NDP-3 THE CLASS IS DETERMINABLE FROM THE ENCODER'S OWN INPUT. Raw-input ceiling arm held-out accuracy
> >= 0.90 (V3-EXQ-1002 measured 0.985 / 0.980 / 0.973 for class 1). A low ceiling means the environment
> does not instantiate the distinction -- V3-EXQ-978's "environment too sparse" vacuity, generalised.
> NDP-4 THE FLOOR ARM IS PRESENT. Same-capacity adapter on an UNTRAINED z_world projection, so R_k has
> a real zero (V3-EXQ-1002 measured 0.688 / 0.681 / 0.695). Elevation over
> `max(majority-class, repeat-previous-executed-action)` is reported alongside (measured 0.250 / 0.566
> class), because an adapter can clear a floor on a trivial shortcut.
> NDP-5 THE ORGANISM-LEVEL DV HAS RESOLUTION. Report the DV quantum and the within-arm seed spread, and
> require the claimed effect to exceed one quantum. V3-EXQ-978's arm difference was one third of one
> 0.05 res/ep quantum, and its within-arm spread was 21x the arm-mean difference -- a null under those
> conditions is uninterpretable, not negative.
> NDP-6 GOV-MATCHAUX-1 COMPLIANCE ON THE RESTORATION LEG. (i) a matched arbitrary-auxiliary control with
> equal head capacity, loss budget, update frequency and training examples, targeting learnable but
> organism-irrelevant structure, with any entropy/difficulty mismatch REPORTED not silently accepted;
> and (ii) evaluation with the auxiliary head REMOVED, scored on downstream organism-level measures,
> never on the objective's own probe accuracy or loss.
> NDP-7 INSTRUMENT HYGIENE, inherited from V3-EXQ-972's disclosed defects. Any cosine/similarity
> statistic used as a supporting read must be CENTRED (972's `separability_score` is an uncentred
> contrast and its own autopsy states it "does not support the stronger 'there is no structure for any
> objective to condition on'"), and must carry a block-shuffle permutation null over stored
> `(episode_idx, step_idx)` -- the fix 972's red-team specified and did not build. Without the null,
> slow representation drift across an episode block can read as class separation. Any absolute
> threshold on such a statistic must be reported as calibrated-or-not; 972's 0.05 floor is
> self-described as "a conservative noise floor ... not a rigorously derived value".
>
> **CONFIRMING (INV-104 supported for class k) -- all four, on >= 3 of 5 seeds:**
> (i) DESTRUCTION IS REAL: `R_k <= 0.25` through the trained compression while NDP-3 holds
> (ceiling >= 0.90). The step discards most downstream access to a class its own input determines.
> (ii) THE LOSSES DO NOT SEE IT -- this is the clause "regardless of reconstruction or prediction
> loss", and without it the claim reduces to ordinary representation-learning. Report
> `delta world_obs reconstruction loss` and `delta E2 one-step prediction MSE` between the
> access-destroyed and access-restored arms and require both to fall within 1 SD of the within-arm
> seed spread. If restoring class-k access also visibly improves reconstruction/prediction, the result
> is consistent with INV-104 but does not discriminate it from generic representation learning, and
> must be reported as non-discriminating.
> (iii) RESTORATION PAYS, WITH THE SCAFFOLD REMOVED: training a class-k scaffold and then REMOVING the
> head at evaluation raises `R_k` by >= 0.20 absolute AND raises an organism-level DV
> (resources/episode against the 1.0 D3 competence floor; secondarily harm_rate) by
> >= `max(2 x SD of the seed-matched delta, one DV quantum)`.
> (iv) IT IS NOT JUST MORE SUPERVISION: `delta_class-k - delta_matched-arbitrary >= 2 x SD` of the
> seed-matched delta on the organism-level DV. Absent (iv) the finding is "extra supervision helps",
> which GOV-MATCHAUX-1 rules inadmissible as evidence that an objective ORGANISES a latent.
>
> **FALSIFYING -- three independent routes, any one of which is decisive for the class:**
> F1 VACUITY (falsifies the contract's usefulness, and the claim's own registration text says a null
> here is a useful result). `R_k >= 0.75` for every class measurable at this stage, through a
> compression trained on generic predictive / reconstruction objectives alone with NO class-specific
> pressure. Then generic compression already preserves what the organism needs, the preservation
> contract does no work, and pressure to complicate z_world is reduced. This is the cluster's own
> red-team 5 and MECH-520's counter-constraint.
> F2 NO-COST (falsifies the normative half, and is the sharpest route). Condition (i) holds -- access
> IS destroyed -- but restoring it moves no organism-level DV: the delta between access-restored and
> access-destroyed arms sits within 1 SD of the within-arm seed spread on >= 4 of 5 seeds, with NDP-5
> demonstrated (DV quantum smaller than the claimed effect). Then destroying class k is NOT a
> developmental regression, and class k is struck from the preservation list.
> F3 SCAFFOLD DEPENDENCE (falsifies the claim's own removability clause on its own instance). The
> improvement in (iii) is present with the auxiliary head attached and disappears when it is removed at
> evaluation. Per the source thought, that "demonstrated supervision dependence rather than emergence
> of a useful world representation".
>
> **ONE CONDITIONAL-INTERPRETATION CLAUSE, and it is why the RUN is gated even though this text is
> not.** If V3-EXQ-1002 returns H-B (a capacity-matched supervised adapter CAN reproduce the
> `local_view_greedy` oracle from the frozen z_world, i.e. the consumer never learned the mapping),
> then the organism-level leg of (iii)/(iv)/F2 is being read through a reader that cannot use ANY
> representation, and **F2 is inadmissible** -- a flat organism-level DV under H-B is a consumer
> finding, not evidence against preservation. Under H-B the falsifier runs through the oracle-adapter
> readout rather than the production policy. Under H-C (geometry mismatch) the production readout is
> the right one and F2 is admissible. This is MECH-517's ordering dependency, made explicit rather than
> assumed away.

**Proposal sketch (disposition (a)):**

- **Title:** "INV-104 class-1 preservation ladder: retained-fraction of organism-relevant distinction
  access through the trained z_world compression, with scaffold-removal and matched-arbitrary-auxiliary
  controls"
- **related_claims:** `INV-104` (primary), `GOV-MATCHAUX-1` (the admissibility rule the design
  instantiates), `MECH-523` (the untrained-site precondition), `SD-070` (the trained-compression
  recipe), `SD-018` (the class-1 scaffold), `MECH-517` (the H-B/H-C interpretation gate), `ARC-138`
  (adjacent, NOT co-tagged as the DV -- see the fusion-risk note above).
  **NOT `INV-088`, NOT `MECH-457`** -- the re-derive brake fired on both in the confirmed
  V3-EXQ-978 autopsy (13 and 2 prior ceiling readings), and a redesign under a new question is
  precisely what that brake permits.
- **Arms (5), 5 seeds:** A0 `rawfield_ceiling` (adapter on the raw 25-dim `resource_field_view`);
  A1 `zworld_untrained_projection` (floor); A2 `zworld_p0_generic` (SD-070 P0a with generic
  scene-structure / anti-collapse objectives only -- the F1 verdict arm); A3
  `zworld_p0_plus_class1_scaffold`, head REMOVED at evaluation; A4 `matched_arbitrary_auxiliary`,
  equal capacity / loss budget / update frequency / matched target entropy, head removed at
  evaluation.
  **GOV-REUSE-1:** A0 and A1 are already measured by V3-EXQ-1002 (0.985 / 0.980 / 0.973 and
  0.688 / 0.681 / 0.695) -- cite, do not re-run, unless the encoder config differs from 1002's, in
  which case say so in the entry note.
- **acceptance_checks:** NDP-1..NDP-7 as gating preconditions (each a named manifest field with its
  measured value and threshold); CONFIRMING (i)-(iv) as the scientific criteria; F1/F2/F3 pre-registered
  as named verdict labels so the reading cannot be selected after the fact; the H-B/H-C conditional
  clause pre-registered as an interpretation gate keyed on V3-EXQ-1002's emitted label.
- **Sequencing / STOP-CHECK:** gated on V3-EXQ-1002 having LANDED and been autopsied (currently
  `status: claimed`, in flight). Coordinate with
  `chip-20260904-regulatory-anchoring-matched-aux` -- that chip is ARC-138's A/B/C anchoring test;
  this is INV-104's preservation ladder; they share arms A1/A4 and the GOV-MATCHAUX-1 controls and
  could be run as one driver with two pre-registered readouts, but **must not share one verdict
  label**.
- **Class-2 follow-on (same design, one knob):** repeat with class 2, oracle = an
  intervention-sensitivity discrimination (does the transition differ under intervention), enabling
  `e2_action_contrastive_enabled=True`. This is also the operational form of the three-rival
  adjudication frame INV-104's notes record: rival (a) predicts A2 already achieves high `R_2`
  (= F1 for class 2); rival (c) predicts `R_2` rises with SD-056 enabled without any explicit "self"
  target; rival (b) predicts organism-level DV does not move even when `R_2` does (= F2 for class 2).

**depends_on additions (recommended):**
- **`MECH-523`** -- not merely adjacent: its finding that REE's designated compression sites are
  systematically untrained is INV-104's NDP-1, and without it every preservation verdict on this claim
  is uninterpretable. This is the single most consequential missing edge.
- **`SD-005`** -- the split-encoder world path IS the compression step the class-1 instantiation
  names; INV-104 currently depends on SD-070 (the training recipe) but not on the structure it trains.
- (Optional, weaker) `MECH-516` / `MECH-518` if governance wants the interface-collapse mechanism
  wired explicitly rather than reached via MECH-517.

**GOVERNANCE FLAG 1 -- `stale_note`:** `REE_assembly/evidence/planning/substrate_queue.json`,
`queue[44]` (SD-018), `failure_record[0]` still reads
`amend_status: "AWAITING VALIDATION -- directional field head landed 2026-09-02 ... target re-tested
by the owed 948-shape probe with use_resource_field_head OFF vs ON"`. That re-test HAS run:
V3-EXQ-978 (2026-09-03), whose confirmed autopsy section 7 explicitly instructs *"amend SD-018 --
record the failure_record item and move `amend_status` off 'AWAITING VALIDATION' to
validated-negative-for-shape-(a)"*. The 978 record was appended as `failure_record[1]`
(`resolved: "open"`) but the status move on `failure_record[0]` was never made, and no
`validated_negative` marker exists anywhere on this entry (grep confirms the marker exists on other
entries, so the convention is live). Reader consequence: `/implement-substrate` and CURRENT_FRONT both
still present SD-018 as an un-owned buildable awaiting validation, when shape (a) has been validated
negative and shape (b) is explicitly withheld pending V3-EXQ-1002.

**GOVERNANCE FLAG 2 -- `stale_note`:** INV-104's own `notes` cite "MECH-100 / SD-009 (event-type CE
auxiliary loss -- class 1)" as an EXISTING SINGLE-CLASS INSTANCE which INV-104 "generalises rather
than duplicates", with no caveat. The record says that instance is contested: MECH-100's
`evidence_quality_note` records that all four supporting runs date from 2026-03-18/20, roughly four
months before SD-070 landed, and were "gathered under a training recipe the substrate has since
replaced for cause"; SD-070's own entry measured the SD-009 target unlearnable from the channel its
loss reads (MLP-128 probe on raw `world_obs` at or below chance, lift -0.014 / -0.060); V3-EXQ-897
(2026-08-08), the first re-measurement under the fixed substrate, "reads the other way" with
OFF >= ON on 3/3 seeds; and SD-009 was demoted provisional -> candidate on 2026-08-08.
**This is NOT a request to re-litigate MECH-100** -- governance dispositioned it on 2026-08-10 (left
at `stable` + caveat, GFLAG-0019/0020 both closed). It is a request that INV-104's notes carry the
caveat, because a preservation invariant citing a class-1 scaffold as precedent should not present
that scaffold's evidence as clean. Suggested one-line addition to INV-104 notes, no status change
anywhere.

**GOVERNANCE FLAG 3 -- `contested_disposition`:** INV-104 carries a single
`epistemic_category: substrate_conditional` over five preservation classes whose substrate readiness
differs by years of roadmap. Verified: class 1 built and exercised three times (SD-018 directional
head landed 2026-09-02, V3-EXQ-978 ran it on an 8/8 green precondition gate); class 2's primitive
built and default-OFF (`ree_core/utils/config.py:884`); class 3 blocked on the untrained ARC-004 depth
cascade (MECH-523 site b); class 4 on MECH-430 (v4); class 5 on ARC-047 (v4-v5, unbuilt, and the
causal-compression intake deliberately declined to chip it). `substrate_conditional` suppresses
promote/demote and dispatches the reader to "wait for the upstream substrate", which freezes a
V3-tractable class-1 pilot behind an unbuilt multi-agent environment it does not need. Recommended
disposition for governance: set `epistemic_category: standard` and add a per-class readiness table to
`notes`; re-tag to `substrate_ceiling` for the class-1 row only if V3-EXQ-1002 returns H-C. The claim's
own VERSION-ROUTING FLAG already says this needs a `/governance` routing decision -- this is that
decision, made concrete.

---

<!-- S_INV-063 appended 2026-09-04T21:26:48Z -->
## G18 -- INV-063 (solo)  (agent report)

**Solo note:** single-claim assignment, no group; the cross-claim mandate is discharged against the
named read-only context claims (INV-049, INV-050) inside the per-claim entry below, where the
merge-pressure question (i) and the shared-falsifier question (iii) are answered explicitly.

---

### INV-063 -- minimum_entropy_intake_sleep_dependency

**Recommended disposition:** (a) testable now -- the intake ladder (SD-MEL-PRODUCER `world_rule_shift`,
validated 2026-07-30) and a *pinnable* offline budget (the K-episode scheduler that V3-EXQ-677 proved
gives zero cross-arm variance in SWS/REM step counts) together make this claim's distinctive content --
*same sleep, less material* -- separable from INV-050's *more material, more sleep*, so it is a fresh
V3 falsifier rather than a merge.

**Extracted from:** primarily the claim's own `description` (the four named starvation legs) turned into
DVs; the non-degeneracy machinery is extracted rather than re-derived from three existing sources --
INV-050's own `what_would_answer` non-degeneracy precondition (the "consumer's own deterministic
MEL->duration mapping" degeneracy, and the V3-EXQ-718a lesson "the producer must be validated with the
consumer ABSENT"), MECH-205's `what_would_answer` non-degeneracy precondition (the surprise-gated-replay
liveness gate: `surprise_gated_replay`, `valence_enabled`, non-zero surprise writes, `_pe_ema > 0`, PE
variance), and SD-MEL-PRODUCER's `implementation_hint` (the reducibility / matched-PE-noise
DV-symmetry control). Per brief rule 6 the Type-1/2 leg's liveness gate is a pointer to MECH-205's text,
not a re-derivation.

**Currency check:** (all verified this pass, 2026-09-04)

1. **`entropy_intake` / `information_intake` are measured NOWHERE.** `/usr/bin/grep -rn` over
   `/Users/dgolden/REE_Working/ree-v3/ree_core` for `entropy_intake` and `information_intake` returns
   zero hits. `sleep_pressure` as a named quantity: zero hits (the only near-match is the
   `SLEEP_ENTRY = "sleep_entry"` phase label at `ree_core/sleep/phase_manager.py:55`). So the claim's
   own IV has no instrument under its own name -- **but it has two usable proxies**, below. This is a
   naming gap, not a substrate gap.
2. **SD-MEL-PRODUCER: CONFIRMED `implemented` / `ready: true`,** `validated_utc: 2026-07-30`,
   `validation_note` = V3-EXQ-798a PASS (2026-07-29), confirmed
   `failure_autopsy_V3-EXQ-798a_2026-07-30`, verdict `producer_validated_graded_learnable`
   (`substrate_queue.json` queue entry `SD-MEL-PRODUCER`). Its knob is
   `causal_grid_world.py:791-794` `world_rule_shift_enabled/_interval/_depth/_scope`, all no-op
   defaults; the mechanism re-permutes the action->displacement map so `E2.world_forward(z_world, a)`
   is invalidated at each shift and re-learnable between shifts, **graded by shift RATE**. `unblocks_claims`
   = `[MECH-180, INV-050]` -- **INV-063 is not named**, though this is the exact instrument it needs.
3. **SD-SLEEP-ENTRY-PRESSURE: CONFIRMED `implemented` / `ready: true`, priority 2, and its
   `failure_record` is marked `resolved`** by V3-EXQ-933a (2026-08-26, diagnostic PASS, 3/3 seeds:
   sub-threshold demand crosses at step 5 vs the 933 baseline of 0 fires in 120 steps; supra-threshold
   fires at rate 0.5 = the refractory cap, vs 933's 120/120 chatter). Code confirmed at
   `ree_core/sleep/mel_consumer.py` (`EntryPressureAccumulator`, `use_entry_pressure`,
   `entry_pressure_gain`, `entry_pressure_threshold`, all default OFF / inert). **Its `unblocks_claims`
   is EMPTY** -- INV-063 is not named there either.
   *Verdict on the task's hypothesis that this is "the substrate INV-063 needs": it is the right
   SHAPE (a time-integrating Process-S term that sums per-step waking demand) but the WRONG ROLE.*
   It governs sleep ENTRY TIMING. INV-063 is not a claim about when sleep starts; it is a claim about
   whether sleep, once running, has anything to work on. Enabling it would in fact be an **anti-control**
   for INV-063 (see the non-degeneracy precondition): it makes low intake produce *less* sleep, which
   is precisely the confound the falsifier must exclude. It is listed below as a flag to be held OFF.
4. **Zero evidence of any kind.** `evidence_backlog.v1.json` EVB-1349 (INV-063): `source_counts
   {experimental: 0, literature: 0}`, `overall_confidence 0.0`, `conflict_ratio 0.0`, reasons
   `[missing_experimental_evidence, missing_literature_evidence, synthetic_signals_only]`. **INV-063
   does not appear in `docs/assets/data/claims.json` at all** (grep returns the worktree copies but not
   the live file), consistent with a claim carrying no runs. No manifest under
   `evidence/experiments/` mentions it; no entry in `ree-v3/experiment_queue.json` mentions it.
5. **Fan-in 0 confirmed.** `grep -n "INV-063" claims.yaml` returns exactly one line (29780, its own
   `- id:`). No claim depends on it. Nothing propagates from its falsification -- which is why the
   2026-09-01 mass-mint triage ranked it **score 0** (`proposal_tick_massmint_triage_20260901.md:171`).
6. **Three proposals already exist and are all auto-generated, none designed:** EXP-0687 +
   LIT-0688 (`experiment_proposals.v1.json` items 348/349, both `status: proposed`, generic
   acceptance_checks "At least 2 additional runs with distinct seeds") and EXP-0736 /
   `chip-proposal-exp-0736` from the 2026-09-01 mass mint. The draft below is what any of those
   should be replaced by; none of them contains a design.
7. **INV-063 is NOT in the sleep plan-of-record's scope.** `evidence/planning/sleep_substrate_plan.md`
   `scope_claims` (line 7, and repeated at every node) lists SD-017, MECH-204/205/272/273/275/285,
   INV-049, INV-050, MECH-180, Q-041/042, SD-029, MECH-111, MECH-256, ARC-045, MECH-166 --
   **INV-063 is absent**, as are MECH-209/210/211 (three of its seven `depends_on`). It is also absent
   from `docs/CURRENT_FRONT.md` and `evidence/planning/closure_status.md` (0 hits each; "sleep" does
   not appear in CURRENT_FRONT.md at all). It is genuinely off the live front.
8. **Its `depends_on` are in mixed health** (checked directly in claims.yaml):
   MECH-205 `stable` / `standard` (the healthiest, and the leg-2 instrument);
   MECH-121 `candidate` / **`substrate_conditional`**; MECH-210 `candidate` /
   **`substrate_conditional`**; MECH-209 `candidate` / **`out_of_domain`** (dream phenomenology);
   MECH-211 `candidate`, **no `epistemic_category` and no `what_would_answer`** (undigested);
   INV-049 `candidate` / `substrate_conditional`; SD-017 provisional (`pending_substrate_reconfirmation:
   true`, and per INV-049's own what_would_answer the write-gate homogenisation FAIL of
   V3-EXQ-436b/c/d is unresolved). The falsifier below is deliberately routed AROUND the
   substrate_conditional / out_of_domain dependencies (see "legs deliberately excluded").
9. **Stale note found in a neighbour (not in INV-063).** MECH-205's `what_would_answer` states
   "`pe_surprise_threshold` **STILL DEFAULTS TO 0.001** (config.py:3035)". That is now false:
   `ree-v3/ree_core/utils/config.py:3365` reads `pe_surprise_threshold: float = 1e-5`, with the
   comment at :3363 attributing the promotion to **GFLAG-0075 (2026-09-01)**. The cited line numbers
   have also drifted (3026/3035 -> 3350/3365). Raised as a GOVERNANCE FLAG below because INV-063's
   leg-2 falsifier points at that text.

**epistemic_category (proposed):** `standard` -- for the **REE leg only** (see the fused-claim split
below). The substrate the narrowed falsifier needs is built and validated; nothing here is
substrate_conditional. The *psychiatric-gradient leg* is `out_of_domain` and should be split out
rather than tagged onto the same claim.

**Fused-claim finding (brief rule 4(c2)).** INV-063 as written contains two claims that no single
test can address:
- **REE leg (testable now, this is the claim I am drafting for):** below a threshold of environmental
  entropy intake, the offline phase's *functional output degrades disproportionately*, at fixed offline
  budget, because it is starved of material.
- **Epidemiological leg (`out_of_domain`):** low-entropy environments (urban, institutional, routine)
  systematically produce anxiety / depression / cognitive-rigidity gradients, and high-entropy
  environments (nature, fractal structure) are protective. No REE substrate at any level tests this;
  it resolves by clinical / environmental-psychiatry literature. LIT-0688 is already minted against
  exactly this and is the correct home for it. **Recommend the description be split** so the REE leg
  can promote or demote on evidence without dragging the epidemiological leg's confidence with it.

**Cross-claim mandate, discharged against the read-only context (INV-049, INV-050):**
- **(i) merge candidates -- NO, and this was the live risk.** The task asked me to check for a duplicate
  reading. It is not one, and the discriminator is crisp: **INV-050 varies intake and measures sleep
  QUANTITY (with the consumer ON: `sws_power`, `replay_rate`, `mel_duration_factor` -- its DVs are the
  consumer's output). INV-063 varies intake and measures sleep EFFICACY AT PINNED QUANTITY (with the
  consumer OFF).** The two are orthogonal manipulations of the same knob, and INV-063's version is the
  one INV-050's own `what_would_answer` calls the missing control ("a consumer-absent control arm ...
  isolating whether sws_power/replay_rate track MEASURED MEL because of the third-drive coupling this
  invariant asserts, or merely because the consumer mechanically guarantees the correlation"). A
  correctly-designed INV-063 run therefore *supplies INV-050's outstanding non-degeneracy arm as a
  by-product*. Not (g).
- **(ii) contradiction / undercut premise -- one real tension, and it is INV-063's own weakest point.**
  INV-050 asserts a *proportional* third drive (sleep scales with MEL). INV-063 asserts a *floor* --
  "a MINIMUM level ... is required", with failures that are "specific, proportional". Those two words in
  one sentence are in tension: a pure proportionality is INV-050 restated at the low end and adds
  nothing; a genuine floor is a knee, a non-linearity INV-050 does not predict. **The falsifier below
  pre-registers the shape test that forces the distinction**, and pre-registers what happens when the
  data say "smooth, no knee" (partial absorption into INV-050 with a narrowed residual -- (g) as a
  contingent OUTCOME, not as today's disposition).
- **(iii) shared falsification condition -- YES, and it should be cross-referenced, not re-derived.**
  Everything about validating that the intake ladder is real (measured waking MEL monotone across arms;
  relative spread > 0.25 per V3-EXQ-701c; the reducibility requirement that elevated PE must DECAY
  within a stationary window, tracked by `steps_since_world_rule_shift`; the matched-PE observation-noise
  negative control against the DV-symmetry artifact) is already written down as SD-MEL-PRODUCER's
  design constraint and re-stated in INV-050's what_would_answer. INV-063's draft points at it.
- **(iv) cross-cutting finding.** All three claims share one confound with opposite valence, and naming
  it is the single most useful thing this pass produces: **the MEL consumer mechanically couples intake
  to sleep duration.** For INV-050 that coupling is the hypothesis (and its near-tautology is the
  hazard). For INV-063 that same coupling is *pure confound* -- if the consumer is ON, low intake
  shortens sleep, and any degraded function is explained by "less sleep", never by "less material". So
  **a null on INV-063 is uninterpretable unless the offline budget is pinned and shown to be pinned from
  measured output.** Conversely, INV-050's `pending_retest_after_substrate` is still `true` and its
  GFLAG-0002 promotion question is still open specifically for want of a consumer-absent arm -- so the
  two claims are best served by ONE run carrying both arms, not two runs.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (five gates; every one must be asserted from MEASURED RUN OUTPUT, never
> from config -- this claim has zero runs, so the first run must not be the vacuous one):
>
> (P1) THE INTAKE LADDER MUST BE REAL, NOT NOMINAL. Intake is graded with the validated
> SD-MEL-PRODUCER knob (`world_rule_shift_enabled/_interval/_depth`, `ree_core/environment/
> causal_grid_world.py:791-794`), NOT with `env_drift_interval` -- V3-EXQ-677 established that drift
> only MOVES hazards, whose optimal prediction is their mean, so it adds sampling NOISE, not learning
> LOAD (C1 manipulation check differed by 8.8e-07 against a 0.01 threshold; sleep counts identical
> across arms). Manipulation check, pre-registered as a gate BEFORE any DV is read: mean waking MEL
> strictly monotone across the four intake arms with relative spread > 0.25 (the V3-EXQ-701c relative
> criterion; the absolute ABS_MEL_FLOOR=1e-4 of 701c is structurally unreachable on a converged base
> and must NOT be reused). Plus the producer's own reducibility control: elevated PE must DECAY within
> a stationary window (assert against the emitted `steps_since_world_rule_shift`), and a matched-PE
> observation-noise arm must NOT reproduce the DV pattern -- otherwise the ladder is grading noise and
> any monotone DV is the DV-symmetry artifact SD-MEL-PRODUCER's design note names by that name.
>
> (P2) THE OFFLINE BUDGET MUST BE PINNED, AND SHOWN PINNED. `use_mel_consumer=False`,
> `use_entry_pressure=False`, `use_within_life_sleep_trigger=False` (all default False at
> `ree_core/utils/config.py:6291/6337` and `mel_consumer.py`). Assert from output that
> `cumulative_sws_writes` and `cumulative_rem_rollouts` have ZERO cross-arm variance -- the exact
> scheduler-pinned property (SWS=80/REM=60) that V3-EXQ-677 recorded as a defect for MECH-180 is the
> control this claim requires. Without it, low intake -> low MEL -> shorter sleep -> worse function is
> the consumer's arithmetic, not this invariant; see INV-050's own what_would_answer on that degeneracy
> and failure_autopsy_V3-EXQ-718a_2026-07-08's "the producer must be validated with the consumer ABSENT".
>
> (P3) SLEEP MUST ACTUALLY FIRE, AND THE OFFLINE PATHWAY MUST BE UNSILENCED. Multi-episode driver, so
> `SleepLoopManager.notify_episode_end()` is reachable at all (sleep_substrate:GAP-9: under a true
> single-continuous-life driver, `num_episodes=1`, there are zero within-life boundaries and NO cadence
> config can make a cycle fire). AND `use_sleep_aggregation_cluster=True` (`config.py:6263`, default
> False) -- sleep_substrate:GAP-3 records that eight independent default-False flags otherwise leave
> the offline-consolidation pathway entirely silent. Assert non-zero SWS writes and non-zero REM
> rollouts in EVERY arm including the lowest-intake arm: if the floor arm simply never slept, the whole
> comparison is vacuous in the V3-EXQ-514m/642 sense.
>
> (P4) THE TYPE-1/2 INSTRUMENT MUST BE LIVE. Do not re-derive this: see MECH-205's own
> what_would_answer NON-DEGENERACY PRECONDITION verbatim (`surprise_gated_replay=True` AND
> `valence_enabled=True`; a NON-ZERO count of VALENCE_SURPRISE writes; `_pe_ema > 0` at the replay call
> so `surprise_weight` is not pinned at its 0.3 fallback; genuine PE VARIANCE across episodes). One
> correction to that text when applying it: its warning that `pe_surprise_threshold` "STILL DEFAULTS TO
> 0.001" is STALE -- the default is now 1e-5 (`config.py:3365`, promoted by GFLAG-0075 2026-09-01), so
> the trap it describes is closed; the liveness assertions themselves still stand and must still be made
> from output.
>
> (P5) THE LADDER MUST NOT BE READ THROUGH A BROKEN SLOT INSTRUMENT. Any DV routed through
> ContextMemory slot differentiation (`slot_cosine_sim`) is currently confounded: V3-EXQ-436b/436c/436d
> (2026-08-02..08-04) found SWS_THEN_REM collapses `slot_cosine_sim` toward ~1.0 -- homogenisation, the
> OPPOSITE of SD-017's prediction -- with a suspected untested `ContextMemory.write_gate` bias-collapse
> root cause still unresolved (see INV-049's what_would_answer, and the substrate_queue entry
> `contextmemory-write-path-addressing-degeneracy`, status `implemented_pending_validation`). The Type-3
> leg is therefore EXCLUDED from this falsifier (below) rather than measured through that instrument.
>
> CONFIRMING (two legs, both at pinned offline budget, four intake arms
> `world_rule_shift_interval` in {0 = never / long / medium / short}, >= 3 seeds):
>
> (C1) STARVATION, i.e. monotone degradation of offline FUNCTION as intake falls, with sleep quantity
> held constant. Leg A (Types 1/2 contrastive replay): the count of VALENCE_SURPRISE residue writes per
> waking period and the realised `surprise_weight` at the replay call fall monotonically with intake,
> and the replay start-selection distribution collapses toward uniform (rising entropy of the
> start-selection histogram / falling spread of replay priority) -- i.e. surprise-gating has nothing
> left to prioritise. Leg B (E1 world-model updating): the ACROSS-SLEEP improvement in world-forward
> prediction error, measured on a FROZEN held-out battery with the V3-EXQ-701b/701c frozen-probe
> instrument (pre-sleep PE minus post-sleep PE on the same frozen battery, so the DV is what sleep
> ADDED, not how hard the waking period was), falls monotonically with intake. Both legs monotone
> (non-increasing across intake-sorted arms) on >= 2/3 seeds.
>
> (C2) THE FLOOR, which is what makes this claim distinct from INV-050 and is the load-bearing leg.
> The degradation must be DISPROPORTIONATE at the low end -- a knee, not a slope. Pre-registered shape
> test: the per-seed drop in the C1 DVs between the two LOWEST intake arms exceeds the drop between the
> two HIGHEST arms by a margin of `max(2 x pooled cross-seed SD of the arm-to-arm delta, 20% of the
> highest arm's DV value)` (SD-scaled gate plus an absolute floor, per the project's effect-size
> convention), on >= 2/3 seeds, in the SAME direction on both legs. A run that satisfies P1-P5, C1 and
> C2 would be the first evidence of any kind for this claim and the first demonstration that offline
> function has a material FLOOR distinct from INV-050's proportional drive.
>
> FALSIFYING (three distinguishable outcomes, all informative, pre-registered so the run cannot be
> re-read after the fact):
>
> (F1) FLAT. With P1-P5 all met -- the intake ladder demonstrably graded and reducible, offline budget
> demonstrably pinned, sleep demonstrably firing in every arm, the MECH-205 instrument demonstrably
> live -- the C1 function DVs do NOT degrade monotonically with falling intake (< 2/3 seeds on either
> leg, or non-monotone ordering). Offline function is then insensitive to intake at fixed budget: the
> starvation mechanism this invariant asserts does not exist, and the invariant is genuinely falsified
> rather than substrate-confounded.
>
> (F2) SMOOTH, NO KNEE -- the partial falsification, and the likeliest outcome. C1 passes (monotone
> degradation) but C2 fails: degradation is proportional across the whole ladder with no
> disproportionate low-end collapse. Then the word "minimum" in this claim is not earned: what has been
> shown is a proportional intake->function relation, which is INV-050's third drive observed on the
> function side rather than the quantity side. Pre-registered consequence: this invariant's residual
> narrows to whatever survives -- the FUNCTION-SIDE (as opposed to quantity-side) reading and the
> function-SPECIFICITY reading -- and the threshold content is retired into INV-050 rather than kept
> here as a separate invariant. (This is the merge fork; it is an OUTCOME of the test, not a
> disposition to take before running it.)
>
> (F3) NON-SPECIFIC. C1 and C2 both pass but the two legs degrade in LOCKSTEP with no differential
> sensitivity -- i.e. the same intake reduction hits Types 1/2 replay and E1 world-model updating by
> statistically indistinguishable amounts. Then the claim's specific content ("insufficient surprising
> episodes starve Types 1/2 ... insufficient novel event sequences starve E1 ...", four function-specific
> thresholds) is unsupported; what survives is an undifferentiated "less input, less offline benefit",
> which is close to trivial. The claim should then be re-registered in the weak general form and its
> per-function threshold structure withdrawn.
>
> LEGS DELIBERATELY EXCLUDED FROM THIS FALSIFIER, with reasons (stated so a later reader does not
> mistake the narrowing for an oversight):
> - **Type 3 NREM schema consolidation** ("insufficient schema material starves NREM Type 3
>   consolidation"): its natural DV routes through ContextMemory slot differentiation, which is
>   confounded per P5 (V3-EXQ-436b/c/d homogenisation, unresolved write-gate root cause). Blocked on
>   substrate_queue `contextmemory-write-path-addressing-degeneracy` (`implemented_pending_validation`).
>   Its parent MECH-121 is `substrate_conditional` for the same family of reasons.
> - **E2 motor-sequence learning** ("insufficient high-entropy sensory input degrades E2 motor-sequence
>   learning"): blocked by the action-learning competence floor. `substrate_queue`
>   `mech457_competence_bootstrap_explorer` is `blocked_pending_dependency` (MECH-229 outstanding), and
>   SD-MEL-PRODUCER's own note records that agent competence under load is deliberately out of its scope
>   (V3-EXQ-677 `goal_success = 0.0` in BOTH arms). A motor-learning DV measured on a floored policy
>   cannot discriminate starvation from the floor.
> - **The psychiatric risk gradient** (urban/institutional vs nature/fractal): `out_of_domain`. No
>   REE substrate at any level bears on it; it resolves by environmental-psychiatry literature and is
>   already covered by the minted LIT-0688. See the fused-claim split.
>
> SECOND INTAKE AXIS, NOT USED HERE BUT NAMED FOR THE FOLLOW-UP: the closer analogue of "environmental
> entropy" in this claim's own sense (structural heterogeneity rather than temporal rule-change rate) is
> the infant_substrate_expansion triple `harm_gradient_enabled` / `microhabitat_enabled` /
> `transient_benefit_enabled` (`causal_grid_world.py:619/632/660`, all default False, all
> substrate-confirmed by V3-EXQ-576 / 577a / 589 PASS). It is a better semantic match -- a flat
> homogeneous world vs a heterogeneous graded one is exactly this claim's urban-vs-nature contrast in
> miniature -- but it has never been validated as a graded MEL producer, so using it as the PRIMARY
> ladder would put an unvalidated IV under an unrun claim. Correct sequencing: run the falsifier above
> on the validated `world_rule_shift` ladder first; if it passes, the structural-heterogeneity axis is
> the held-out-environment replication that would answer the generality question. Note also that
> `world_rule_shift_scope` is a reserved-but-unbuilt hook for exactly a "structural-statistics variant"
> (`causal_grid_world.py:789-790`; the validator at :821 currently rejects anything but `"action_map"`),
> so a third, purpose-built structural-entropy knob is a cheap later addition behind the existing master
> switch.

**Proposal sketch (disposition (a)):**
- **title:** `INV-063 entropy-intake floor: offline function degradation at PINNED offline budget
  (consumer-absent graded-intake ladder)`
- **claim_ids / related_claims:** primary `INV-063`; secondary `INV-050` (this run carries the
  consumer-absent arm INV-050's own what_would_answer names as its outstanding non-degeneracy control,
  and GFLAG-0002's promotion question is gated on exactly that), `MECH-205` (leg A is a direct read of
  its surprise-gating instrument under intake starvation), `MECH-180` (quantity-side sibling, arms
  pinned here). Register INV-050/MECH-205 with an explicit per-claim direction; do NOT tag MECH-121,
  MECH-209, MECH-210, MECH-211 -- three are substrate_conditional/out_of_domain and the fourth is
  undigested, and tagging them would be the surface-substrate_conditional-as-ready anti-pattern.
- **design:** 4 intake arms x >= 3 seeds, `world_rule_shift_interval` in {0, long, medium, short} at
  fixed `_depth`, plus a matched-PE observation-noise negative control arm; `use_mel_consumer=False`,
  `use_entry_pressure=False`, `use_within_life_sleep_trigger=False`,
  `use_sleep_aggregation_cluster=True`, `surprise_gated_replay=True`, `valence_enabled=True`;
  multi-episode driver (GAP-9 reachability).
- **acceptance_checks (pre-registered, in gate order):**
  1. R1 ladder real: mean waking MEL strictly monotone across the four arms, relative spread > 0.25;
     PE decays within stationary windows against `steps_since_world_rule_shift`; the matched-PE-noise
     arm does NOT reproduce the DV pattern. (Gate -- DVs not read if R1 fails.)
  2. R2 budget pinned: `cumulative_sws_writes` and `cumulative_rem_rollouts` show zero cross-arm
     variance, from measured output. (Gate.)
  3. R3 non-vacuity: non-zero SWS writes AND non-zero REM rollouts in EVERY arm including the lowest;
     non-zero VALENCE_SURPRISE writes and `_pe_ema > 0` in the HIGHEST arm. (Gate.)
  4. C1 leg A: surprise-write count, realised `surprise_weight`, and replay start-selection spread all
     non-increasing across intake-sorted arms, >= 2/3 seeds.
  5. C1 leg B: across-sleep frozen-battery world-forward PE improvement non-increasing across
     intake-sorted arms, >= 2/3 seeds.
  6. C2 knee: low-end arm-to-arm drop exceeds high-end arm-to-arm drop by
     `max(2 x pooled cross-seed SD of the delta, 20% of the highest arm's DV)`, >= 2/3 seeds, same
     direction on both legs.
  7. Manifest carries `claim_ids_tested`, `evidence_class`, `evidence_direction`, and per-claim
     direction for INV-050 / MECH-205; the F1/F2/F3 self-route labels above are pre-registered in the
     driver so the outcome is classified, not narrated.
- **Supersedes / replaces:** EXP-0687 and EXP-0736 (`chip-proposal-exp-0736`) -- both auto-minted
  placeholders with no design. LIT-0688 should be RETAINED and re-scoped to the out_of_domain
  epidemiological leg only.

**depends_on additions (if any):** none required for the narrowed REE leg. If the claim is split as
recommended, the surviving REE-leg claim's `depends_on` should DROP `MECH-209` (out_of_domain dream
phenomenology, bears only on the four-function taxonomy's experiential labels, not on the intake
mechanism) and should ADD `MECH-180` (the quantity-side sibling whose pinning is this falsifier's
control). `emergent_from: [SD-017]` and `pending_substrate_reconfirmation: true` should be RETAINED --
the Type-3 leg genuinely does sit behind SD-017, which is why that leg is excluded above.

**GOVERNANCE FLAG 1 -- `stale_note`:** MECH-205's `what_would_answer` non-degeneracy precondition
asserts that `pe_surprise_threshold` "STILL DEFAULTS TO 0.001 (config.py:3035)" and builds its central
trap warning ("a run that enables the flag and inherits the default threshold writes ZERO
VALENCE_SURPRISE entries ... and reads vacuously") on that default. **The default is now 1e-5**
(`ree-v3/ree_core/utils/config.py:3365`), promoted by GFLAG-0075 on 2026-09-01, with the promotion
recorded in the adjacent comment at :3363. The cited line numbers are also stale (3026/3035 ->
3350/3365). The warning is now describing a closed trap as if it were open, on a `stable` claim whose
what_would_answer other claims (including this draft) point at. Recommend a targeted text correction,
not a regen.

**GOVERNANCE FLAG 2 -- `contested_disposition`:** INV-063 is a FUSED claim (testable REE leg +
`out_of_domain` environmental-psychiatry leg) carried under a single `invariant` / `emergent` /
`candidate` registration with `overall_confidence 0.0` and zero sources of either kind. As registered
it can never resolve: an experimental result on the REE leg cannot move a claim whose text also asserts
a clinical epidemiological gradient, and a literature pull on the epidemiological leg cannot move a
claim whose text also asserts an offline-function starvation mechanism. Recommend governance split it
into (i) the REE leg, `standard`, carrying the falsifier drafted above, and (ii) an
`out_of_domain` / literature-synthesis claim carrying the psychiatric gradient, with LIT-0688 re-scoped
onto (ii). Flagged rather than acted on: splitting a registered claim is a governance write, not a
digestion write.

**GOVERNANCE FLAG 3 -- `evidence_discrepancy`:** the run designed above would supply, as a by-product,
the consumer-absent control arm that **INV-050's own `what_would_answer` names as its outstanding
non-degeneracy requirement** and on which **GFLAG-0002 (open since 2026-08-07, "promotion re-gated on a
genuinely independent test ... and/or a consumer-absent control per the claim's own what_would_answer
non-degeneracy precondition") is still gated**. INV-050 also still carries
`pending_retest_after_substrate: true`. Governance should be aware that these two claims' outstanding
evidence needs are satisfiable by ONE run and should not be queued as two, and that INV-063 -- a fan-in-0,
zero-evidence, off-front claim that the 2026-09-01 triage correctly scored 0 in isolation -- is
substantially MORE valuable when queued as INV-050's missing control than its dependent-count ranking
suggests.

**GOVERNANCE FLAG 4 -- `stale_note`:** two coverage gaps found in the sleep plan-of-record.
(a) `evidence/planning/sleep_substrate_plan.md` `scope_claims` omits INV-063, MECH-209, MECH-210 and
MECH-211 while including every other member of the sleep cluster (SD-017, MECH-204/205/272/273/275/285,
INV-049, INV-050, MECH-180, Q-041/042, SD-029, MECH-111, MECH-256, ARC-045, MECH-166) -- so four sleep
claims have no plan-of-record node and are invisible to the plan's own resume/gating machinery.
(b) `SD-MEL-PRODUCER.unblocks_claims` is `[MECH-180, INV-050]` and
`SD-SLEEP-ENTRY-PRESSURE.unblocks_claims` is `[]`; INV-063 is the natural third consumer of the
producer knob and appears in neither, which is why nothing has ever surfaced it as buildable. Both are
narrow single-field corrections, not a regen.

---

<!-- G11 appended 2026-09-04T21:29:11Z -->
## G11 -- committed vs uncommitted operating modes  (agent report)

### Group preamble

- **Why these are together (restated, then my own view).** The grouping rationale was
  namespace adjacency: both sit under `subject: cognitive_modes.*`, both use the word
  "committed", and MECH-025b is a lettered child whose parent (MECH-025, read-only context
  here) rides along. **My own view is much stronger than namespace adjacency, and it is the
  central finding of this pass: in the ree-v3 substrate the two claims are contrasts on the
  SAME SCALAR, at different granularity.** `ree_core/predictors/e3_selector.py:3674`
  computes `committed = commit_variance < effective_threshold` where `commit_variance` is
  `self._running_variance` on the default path, and `current_precision` (line 771-773) is
  `1.0 / (self._running_variance + 1e-6)`. So **"committed" is exactly the event "precision
  above `1/effective_threshold`"** -- a monotone threshold on the same quantity MECH-025b
  calls "the precision level at which the action was committed". Governance has already
  recorded this empirically without drawing the G11 consequence: ARC-016's 2026-07-25
  promotion-to-`stable` verdict reads "mean_rho_rv_vs_commit -0.955; commit-rate tracks
  E3-derived precision monotonically ... Structural only (no harm DV); **the ARC-029
  behavioural consequence layer is separate**". That sentence is the cleanest available
  statement of what each G11 claim owes: ARC-016 owns the structural precision->commitment
  circuit (now `stable`); **ARC-029 owes its behavioural (harm-DV) consequence, and MECH-025b
  owes its accountability-weight consequence -- both of the same circuit.**

- **(i) same-claim / merge candidates.** **No merge, in either direction, and I recommend
  against (g) for both.** They share a substrate variable but not a dependent variable:
  ARC-029's DV is harm-per-step across the threshold (a between-regime contrast); MECH-025b's
  DV is residue accumulated per unit harm as a function of precision *within* the committed
  regime (a within-regime gradient). One can pass while the other fails, in both directions.
  On the specific merge pressure the task named -- **MECH-025b vs MECH-487 / MECH-485 leg 3 /
  Q-090 (the 2026-08-07 responsibility-counterfactual-memory cluster) -- I checked all three
  live blocks and MECH-025b is NOT a duplicate reading of MECH-487.** MECH-487 is a *retention
  buffer*: it persists WHICH rejected E3 candidate existed past the tick it was rejected on
  (its own `what_would_answer` says the novel content is "identity + persistence", over and
  above MECH-264's transient `cfv_now` scalar). MECH-025b asserts a *weighting function*:
  that the precision at commit time scales the residue/accountability attached to the action
  actually taken. MECH-487 is about the counterfactual arm; MECH-025b is about the taken arm.
  They meet only at INV-012 (both are consumed by it -- MECH-487 by Leg 3, MECH-025b's content
  by the Leg 1/Leg 3 "could have done otherwise" premise), and INV-012 already carries both
  without conflating them. **No merge proposed; no absorbed id; no reverse-dep repointing.**

- **(ii) contradictions / undercut premises.** No direct contradiction, but there is a real
  **one-directional premise undercut, and it runs from ARC-029's territory into MECH-025b**.
  MECH-025b's stated rationale (its own 2026-04-02 notes) is that "actions committed at higher
  precision carry higher residue weight **because the agent was in a state where it could have
  done otherwise with finer discrimination**". That "could have done otherwise" premise is
  exactly INV-012 **Leg 0**, which INV-012's own live `what_would_answer` records as
  **CURRENTLY UNMET**: MECH-439 carries `ceiling_decision: exhausted` (still, as of its latest
  entry `failure_autopsy_V3-EXQ-571b_2026-09-01`), i.e. E3 has not been shown to select among
  genuinely differentiated candidates. Consequence, and it cuts both ways so it must be stated
  carefully: **the 671b operationalization does not DEPEND on Leg 0** (it correlates E3's own
  precision against residue, both independently confirmed live that run -- the 2026-08-03
  autopsy says so explicitly and it is correct), **but the RESPONSIBILITY READING of a PASS
  would**. So a future MECH-025b PASS licenses "precision scales residue weight" and does NOT
  licence "precision scales *accountability*" until Leg 0 clears. That asymmetry belongs in the
  falsifier and is written into the draft below.
  Second, milder undercut, running the other way: ARC-029 asserts two *operating modes*, which
  presupposes sustained occupancy of each. The substrate record says the default does not
  provide it (see (iv)). If ARC-029's mode premise fails, MECH-025b is unaffected -- its DV is
  a within-committed gradient and needs only spread, not sustained occupancy. **MECH-025b is
  therefore the CHEAPER of the two to run, and is not gated on ARC-029.**

- **(iii) shared falsifier.** Yes, and it is a *precondition*, not a whole falsifier. Both
  claims' non-degeneracy precondition is a statement about **one distribution: the within-run
  distribution of `commit_variance` relative to `effective_threshold`**. ARC-029 needs BOTH
  SIDES of that threshold occupied within a single run; MECH-025b needs GRADED SPREAD on the
  committed side. Since 2026-09-02 (ree-v3 `48f85f0`, "MECH-027: precision-scaled commit
  temperature") there is a single always-set per-tick diagnostic for exactly this quantity --
  `last_score_diagnostics["precision_margin_norm"]`, `0` at the threshold, `1` as
  `commit_variance -> 0`, computed unconditionally on every world-variance-mode tick and
  deliberately NOT gated on any flag ("mirrors `conflict_gap_norm`'s always-set convention").
  **MECH-025b's draft below cross-references ARC-029's precondition text rather than
  re-deriving it, and both drafts name `precision_margin_norm` as the shared instrument.**

- **(iv) cross-cutting finding (the mutual confound -- the reason this is a group).**
  Because committed-ness and precision are the same scalar, **any manipulation that moves one
  moves the other, and neither claim's existing test controls for this.** Concretely:
  - **ARC-029's only supporting run does its ablation by pinning precision.** V3-EXQ-063a's
    own summary states the method: "force `agent.e3._running_variance = commit_threshold +
    0.1` and `agent.e3._committed_trajectory = None` before each SELECT step". With
    `commitment_threshold = 0.40` (variance space; `ree_core/utils/config.py:1022`) that pins
    the ablated arm at `rv = 0.50`, i.e. `current_precision = 2.0`, against a gate-active arm
    whose operating point in this substrate family has been measured as low as `rv = 0.005420`
    (V3-EXQ-794, quoted in `config.py`'s SD-076 block) -- **a precision difference of up to
    ~90x between arms.** `current_precision` / `_running_variance` is read by at least: dACC
    (`cingulate/dacc.py:373`, `precision_norm = min(current_precision/500, 3.0)`), the
    serotonin REM entry point (`agent.py:12250`), the harm-nonredundancy penalty scale
    (`config.py:3484`), the MECH-204 sleep writeback (`sleep/phase_manager.py:603`), and the
    heartbeat/BreathOscillator sweep logic. `config.py:1049-1052` states the coupling in its
    own words: unbounded downward rv drift "would both pin the agent permanently 'committed'
    and explode precision". **So V3-EXQ-063a is not a commitment-gate ablation; it is a global
    precision manipulation, and its harm gap is unattributable between the two.** This is the
    same confound class the 2026-06-03 autopsy already caught on V3-EXQ-630 in the other
    direction ("SD-022 limb-damage degrade drives commitment via running_variance") -- nobody
    has yet applied that finding backwards to 063a, which is the run ARC-029's `provisional`
    status rests on.
  - **MECH-025b's DV is a range-restricted slice of ARC-029's contrast.** 671b samples only
    committed steps, i.e. only the `rv < 0.40` tail. Restriction of range attenuates a Pearson
    correlation, and **the C1 bar of `> 0.15` was never derived from an expected effect size
    under that restriction** -- it is inherited unchanged from 671 and 671a. A null against an
    underived bar is weak evidence in either direction.
  - **Therefore: a null on either claim is uninterpretable unless the other's variable is
    pinned.** The correct ablation for ARC-029 is one that moves the **THRESHOLD**, leaving
    `rv` (and every precision consumer) untouched -- which the substrate already provides, via
    the MECH-108 BreathOscillator (`ree_core/heartbeat/clock.py:20-31`,
    `effective_threshold = base_threshold * (1.0 - sweep_amplitude)`). That is the single
    most actionable output of this pass and it is written into ARC-029's proposal below.

- **Currency findings (stale notes, landed blockers, unreviewed results).**
  1. **ARC-029, STALE (2026-06-03, ~3 months).** `evidence_quality_note` says of V3-EXQ-630:
     "Redesign queued (confound-isolation arm)." **It was never queued and never ran.** The
     live `ree-v3/experiment_queue.json` holds 3 items, none referencing ARC-029; there is no
     630-successor manifest anywhere under `REE_assembly/evidence/experiments/`; there is no
     `substrate_queue.json` row for ARC-029; and there is no open chip or IGW assignment for it.
  2. **ARC-029, STALE (2026-04-05, ~5 months).** "EXQ-125a redesign (num_hazards=8,
     hazard_harm=0.05, 5 seeds, harm_obs passed to sense()) is the correct follow-up."
     **V3-EXQ-125a never ran** -- no manifest, no queue row. (Its stated purpose was partly
     served incidentally: 063a's operating point of ~-0.055 harm/step shows the ~100x
     harm-floor collapse EXQ-227 diagnosed is not binding at 063a's env parameters.)
  3. **ARC-029, currency POSITIVE.** Its `depends_on` claims have both moved since the last
     ARC-029 run: **ARC-016 is now `stable`** (promoted 2026-07-25, verdict quoted above),
     and MECH-090 is `active` (latest 2026-08-03, `non_contributory/competence_implementation_gap`).
     ARC-029 is the named remaining behavioural layer of a now-stable structural claim.
  4. **MECH-025b, currency POSITIVE and decisive for the redesign.** A materially better
     instrument landed **32 days after 671b ran**: `precision_margin_norm` (ree-v3 `48f85f0`,
     2026-09-02 18:36:45Z), a normalized, always-set, per-tick graded precision margin at the
     commit boundary. 671b (2026-08-03) had to use raw `current_precision`, whose per-seed
     scale varies by ~37x in that very run (see the flag below). `precision_margin_norm` is
     scale-free by construction and is exactly the regressor this claim's DV wants.
  5. **MECH-025b, the substrate does NOT have a discrete precision mode.** I grepped
     `ree_core/` for `precision_mode`, `high_precision`, `action_precision`: **no such knob
     exists.** Precision is a continuous scalar throughout, which is what MECH-025's own
     `what_would_answer` already says the literature requires ("Friston 2013 records precision
     as continuous, not a discrete mode switch"). The claim's title phrase "high-precision
     action MODE" has no substrate referent as a mode; it does have one as a *level*. The
     falsifier below is written at the level, not the mode, and that is a deliberate narrowing.
  6. **Commitment-sustainment (the precondition the task asked me to pin down).** Answer from
     the substrate, not from inference: **at default settings a natural commit lasts ~1 tick.**
     `ree_core/utils/config.py:5053-5074` records V3-EXQ-460i's finding verbatim: "the active
     SD-034 de-commit control-plane **fragments the latch to ~1-tick blips even with the lever
     OFF**, so there was no sustained occupancy to shorten", and the earlier 460h "sustained
     ~2400-step monolithic natural-commit hold did not reproduce". Independently,
     `_committed_trajectory` is torn down every tick by the last statement of
     `post_action_update` (`config.py:5345-5356`), which is why the MECH-321 R4 mid-execution
     hook had **never executed in any experiment** (`decomp_n_evaluated_midexec = 0` in all 10
     V3-EXQ-830 cells). This is the mechanical basis of memory
     `feedback_dont_queue_commitment_dependent_behavioural`, and it is confirmed.
  7. **BUT the sustainment levers now exist and ARE reachable (checked, not assumed).** Five
     default-`False` knobs bear on occupancy: `use_natural_commit_latch_hold`,
     `use_persistent_committed_program_handle`, `use_e3_reselection_shortcircuit`,
     `use_closure_commit_entry`, `closure_exclusive_decommit_eval`. Because of the MECH-307
     `from_dims`-unreachability precedent I verified reachability by AST rather than by
     eyeballing: `REEConfig.from_dims` (968 parameters) **has all five in its signature and
     assigns all five in its body.** So this is "built, reachable, and never exercised in any
     ARC-029 or MECH-025b run" -- not "code does not exist". That distinction is what sets
     ARC-029's disposition below.
  8. **Sole ARC-029 support is non-degenerate only vacuously.** V3-EXQ-063a's C3 gate reads
     "committed cond has more committed than uncommitted steps: **1156 vs 0**", and
     `n_uncommitted_active_stable = 0.0`. The gate-active arm was committed on 100% of eval
     steps. **The "committed vs uncommitted operating modes" contrast the claim's title asserts
     has never been observed within a single run.** 063a measured gated-vs-ablated agents, not
     modes.

---

### ARC-029 -- Committed and uncommitted operating modes produce measurably distinct harm out...

**Recommended disposition:** **(a) testable now** -- the blocker is instrument design, not
missing substrate: the commit gate is built and heavily exercised, the mode-alternation driver
(MECH-108 BreathOscillator threshold modulation) and the occupancy levers are all built and
`from_dims`-reachable, and what has never been done is a *precision-invariant* ablation with
both regimes occupied inside one run.

**Extracted from:** the claim's own `notes` block (the EXP-0085 gate-ablation design, the
stable/volatile second dimension, and the 2026-04-05 Humphries-2012 hazard-density interaction
prediction -- all three carried through into the draft below), **plus** ARC-016's 2026-07-25
promotion verdict, which names ARC-029 as its own separate behavioural-consequence layer.
Not drafted fresh.

**Currency check:** verified against `ree-v3/experiment_queue.json` (3 items, no ARC-029 row),
`REE_assembly/evidence/planning/substrate_queue.json` (no row), the full manifest set under
`REE_assembly/evidence/experiments/` (41 files mention ARC-029; latest genuine run is
`v3_exq_063a_..._20260602T172531Z_v3`, PASS 5/5, `evidence_direction: supports`), `TASK_CHIPS.json`
and `igw_assignments.json` (no open work). Both routing notes in the claim's own text
("Redesign queued", "EXQ-125a ... correct follow-up") are stale -- neither ever ran. Code checked:
`e3_selector.py:265-274, 771-773, 3653-3690`, `config.py:1010-1032, 5053-5074, 5345-5356`,
`heartbeat/clock.py:20-31`; `from_dims` reachability of all five occupancy levers confirmed by AST.

**epistemic_category (proposed):** `standard` -- **explicit, and this is a correction, flagged
below.** ARC-029 currently carries NO explicit `epistemic_category`, so the indexer infers
`substrate_coherence` from `claim_type: architectural_commitment` (per REE_assembly/CLAUDE.md's
dispatch table), which suppresses promote/demote. That inference is wrong for this claim: it
makes an empirical behavioural prediction with a harm DV, it has been experiment-gated
throughout (EXQ-063, 125 x3, 227, 063a, 630), and it was promoted candidate -> provisional on
experimental confidence (`conf=0.774`). It is not `substrate_ceiling` (its readiness gates have
NOT passed non-degenerately -- see finding 8) and not `substrate_conditional` (the code exists
and evidence is banked both ways). `standard` is the honest value.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (three parts; all three must hold before C1 is read as
> evidence -- this claim's entire experimental record fails at least one of them).**
> **(P1) BOTH REGIMES MUST BE OCCUPIED WITHIN A SINGLE RUN.** The claim asserts two operating
> *modes*, which is a within-agent contrast, not a between-arm one. Every prior test measured a
> gated agent against a differently-configured agent: V3-EXQ-063a's gate-active arm recorded
> `n_committed_active_stable = 1155.5` against `n_uncommitted_active_stable = 0.0`, so its C3
> "non-degeneracy" gate (1156 vs 0) passed vacuously and the two-mode contrast was never
> realised. Require, per seed, in the alternating arm: `committed_step_fraction` in [0.15, 0.85]
> AND mean committed-run length >= 3 consecutive ticks, on >= 4/5 seeds. The run-length half is
> load-bearing and not a formality: V3-EXQ-460i established that "the active SD-034 de-commit
> control-plane fragments the latch to ~1-tick blips even with the lever OFF" and that 460h's
> sustained ~2400-step hold did not reproduce, so a 50/50 committed/uncommitted split composed
> of 1-tick alternations is NOT two operating modes and must fail this gate. If P1 cannot be met
> at default settings, it is met by arming `use_natural_commit_latch_hold` (and, for macro
> programs, `use_persistent_committed_program_handle` + `use_e3_reselection_shortcircuit`) --
> all three are default-`False`, all three are in `REEConfig.from_dims`, and none has ever been
> armed in an ARC-029 run. **If P1 still fails with those armed, ARC-029 converts to
> `substrate_conditional` on commitment-occupancy sustainment and this falsifier is not readable.**
> **(P2) THE MODE MANIPULATION MUST NOT MOVE PRECISION.** In ree-v3, `committed` is
> `commit_variance < effective_threshold` (`e3_selector.py:3674`) and
> `current_precision = 1/(running_variance + 1e-6)` (`:771`), so commitment and precision are
> the same scalar; ARC-016's own promotion verdict measures `mean_rho_rv_vs_commit = -0.955`.
> An ablation that forces `running_variance` -- as V3-EXQ-063a's does, to
> `commit_threshold + 0.1 = 0.50`, i.e. `precision = 2.0`, against an operating point measured
> as low as `rv = 0.005420` (V3-EXQ-794) -- simultaneously perturbs dACC precision gating
> (`dacc.py:373`), the harm-nonredundancy scale, serotonin REM entry, the MECH-204 sleep
> writeback, and the heartbeat sweep. Its harm gap is therefore unattributable between "the
> commitment gate did work" and "the agent's precision was crushed" -- structurally the same
> confound the 2026-06-03 autopsy used to retag V3-EXQ-630 `non_contributory` ("SD-022
> limb-damage degrade drives commitment via running_variance"). Require instead that the mode
> driver act on the **THRESHOLD**: MECH-108's BreathOscillator already does exactly this
> (`clock.py:20-31`, `effective_threshold = base_threshold * (1.0 - sweep_amplitude)`), leaving
> `running_variance` and every precision consumer untouched. Gate on it: the distribution of
> `current_precision` must be statistically indistinguishable between the alternating arm and a
> static control arm (paired per-seed mean and SD difference below a pre-registered floor). Set
> `sweep_amplitude` from the run's own measured `rv` distribution, not from a guess -- with
> `commitment_threshold = 0.40`, pushing an agent operating at `rv ~= 0.33` uncommitted needs
> `sweep_amplitude > 0.18`, while one operating at `rv ~= 0.0054` needs `> 0.986`. This is why
> EXQ-199's earlier BreathOscillator attempt recorded `committed_step_count = 0` on both seeds:
> the amplitude was not calibrated to the lineage's own operating point.
> **(P3) THE HARM DV MUST BE OFF THE FLOOR.** EXQ-227 diagnosed that SD-010/011/012 cut harm
> rates ~100x, making any gate signal undetectable at the original `num_hazards=4,
> hazard_harm=0.02` parameters. Require a per-seed harm rate at least an order of magnitude
> above the measurement floor; V3-EXQ-063a's ~-0.055 harm/step is a demonstrated workable
> operating point, so this is a calibration requirement, not an open problem.
>
> **CONFIRMING.** With P1-P3 met, within the SAME agent and seed: mean harm-per-step during
> committed windows is lower than during uncommitted windows in the STABLE environment, with a
> paired per-seed delta exceeding `max(0.5 * SD(per-seed paired delta), 0.002 harm/step)` and
> the same sign on >= 4/5 seeds; AND the gap NARROWS in the volatile environment
> (`gap_volatile < gap_stable`, >= 4/5 seeds) -- the context-dependence half, which is the part
> that distinguishes ARC-029 from a generic "commitment is good" claim; AND, as the sharper
> version of the same prediction already written into this claim's own notes from the
> Humphries 2012 pull, the advantage is strongest at LOW hazard density (2-3 hazards) and
> weakest or reversed at HIGH density (6-8), i.e. a significant density x mode interaction
> rather than only a main effect.
>
> **FALSIFYING.** With P1-P3 all met and the precision-invariance gate P2 clean, the committed
> and uncommitted windows show no harm difference (paired delta within the noise band on a
> majority of seeds), or a difference in the wrong direction in the STABLE condition. Because
> the manipulation is threshold-side, such a null CANNOT be explained away as a precision
> artifact, which is the one exemption every prior ARC-029 test has been able to claim. This
> would be a genuine falsification: the commitment gate would be shown to be structurally real
> (ARC-016, `stable`) but behaviourally inert on harm, and ARC-029 should be narrowed to the
> structural claim or retired in favour of ARC-016. Distinguish this from "still an instrument
> problem" strictly by P1/P2: if occupancy or precision-invariance fails to gate cleanly, the
> run is `non_contributory`, not evidence.

**Proposal sketch (a):**
- **title:** `V3-EXQ-063b -- ARC-029 within-run committed/uncommitted harm contrast under threshold-modulated mode alternation (precision-invariant ablation)`
- **related_claims:** `ARC-029` (primary), `ARC-016` (the now-`stable` structural circuit this
  is the behavioural layer of), `MECH-090` (the beta gate), `MECH-108` (the BreathOscillator
  supplying threshold-side mode alternation), `MECH-025b` (shares P1/P2; a joint run can emit
  both DVs from one rollout -- see the cross-claim note)
- **acceptance_checks:**
  - `G0_occupancy` (GATING): per seed, `committed_step_fraction` in [0.15, 0.85] AND mean
    committed-run length >= 3 ticks, on >= 4/5 seeds. Report the full run-length histogram, not
    just the mean -- a 1-tick-blip distribution with a long tail can hit a mean of 3.
  - `G1_precision_invariance` (GATING): paired per-seed difference in `current_precision` mean
    and SD between ARM_ALTERNATE and ARM_STATIC below a pre-registered floor; `running_variance`
    is never written by the driver (assert no direct assignment to `e3._running_variance`
    anywhere in the driver -- this is a source-level check, and it is the one V3-EXQ-063a would
    have failed).
  - `G2_harm_floor` (GATING): per-seed harm rate >= 10x the measurement floor.
  - `C1_harm_gap_stable`: paired committed-vs-uncommitted harm delta > `max(0.5*SD(delta), 0.002)`,
    same sign >= 4/5 seeds.
  - `C2_context_dependence`: `gap_volatile < gap_stable` on >= 4/5 seeds.
  - `C3_density_interaction`: significant hazard-density (2-3 vs 6-8) x mode interaction, gap
    largest at low density.
  - `C4`: no fatal errors; >= 5 seeds.
- **Route note for the queue entry:** this is `/queue-experiment` work, not a re-run of an
  existing script -- 063a's driver must not be copied, because its ablation method is the defect.

**depends_on additions (if any):** add **`MECH-108`** (the BreathOscillator is the only built
mechanism that can drive within-run mode alternation threshold-side; ARC-029's testability now
rests on it). Optionally note `ARC-016`'s promotion to `stable` in `status_note` -- the existing
`depends_on: [ARC-016, MECH-090]` is otherwise correct and needs no change.

**GOVERNANCE FLAG (1 of 3):** `evidence_discrepancy` -- **ARC-029's `provisional` status rests
on a run whose ablation is confounded and whose non-degeneracy gate passed vacuously.**
V3-EXQ-063a (2026-06-02, PASS 5/5, the sole `supports` entry in `claim_evidence.v1.json`;
`exp_conf = 0.4`, 1 support / 1 weaken) ablates the commitment gate by forcing
`e3._running_variance = commit_threshold + 0.1`, which is a global precision manipulation
affecting dACC gating, harm-nonredundancy scaling, serotonin REM entry, MECH-204 sleep
writeback and the heartbeat sweep -- structurally the same confound the 2026-06-03 autopsy used
to retag V3-EXQ-630 `non_contributory`, never applied backwards to 063a. Separately, its C3
non-degeneracy criterion reads `1156 committed vs 0 uncommitted`, so the two-mode contrast the
claim asserts was never realised. Recommend governance consider retagging 063a
`non_contributory / measurement_test_design_defect` (which would leave ARC-029 with zero
non-confounded experimental support and make the `provisional` reading itself reviewable), or
at minimum record the confound on the claim so the next reader does not treat 063a as settled.

**GOVERNANCE FLAG (2 of 3):** `stale_note` -- **two routing notes in ARC-029's own
`evidence_quality_note` promise follow-ups that never happened.** (a) 2026-06-03: "Redesign
queued (confound-isolation arm)" -- not in `experiment_queue.json`, no manifest, no
`substrate_queue.json` row, no chip, no IGW assignment; ~3 months stale. (b) 2026-04-05:
"EXQ-125a redesign (num_hazards=8, hazard_harm=0.05, 5 seeds, harm_obs passed to sense()) is
the correct follow-up" -- V3-EXQ-125a never ran; ~5 months stale. Both should be corrected to
say the work was never queued, so the claim stops reading as though a fix is in flight.

**GOVERNANCE FLAG (3 of 3):** `contested_disposition` -- **ARC-029 has no explicit
`epistemic_category`, so it infers `substrate_coherence` from `claim_type:
architectural_commitment`, which suppresses promote/demote gating -- while the claim is in fact
managed as experiment-gated** (promoted on `conf=0.774` from EXQ-063; five experimental
entries; `exp_conf` tracked in `claim_evidence.v1.json`). Setting `epistemic_category: standard`
explicitly would align the dispatch with how the claim is actually governed, but it *un-suppresses*
promote/demote and so is a governance decision, not a digestion edit. Flagged for ratification,
not applied.

---

### MECH-025b -- High-precision action mode carries responsibility attribution: the precision...

**Recommended disposition:** **(a) testable now** -- the mechanism is live, both positive
controls already clear on this substrate, the only fair test to date used a pooled estimator
that is confounded by seed, and a strictly better scale-free regressor (`precision_margin_norm`)
landed 32 days after that test.

**Extracted from:** the claim's own `evidence_quality_note` (the V3-EXQ-671 -> 671a -> 671b
gate-hardening sequence: residue-accumulation positive control added at 671a, precision-variance
positive control added at 671b, both clearing at 671b), plus the 671b driver's own docstring
(`ree-v3/experiments/v3_exq_671b_mech025b_precision_responsibility.py:52-90`), from which the
central defect below is taken verbatim. Not drafted fresh.

**Currency check:** live block re-read (its `depends_on` already carries the 2026-09-01
SD-003 -> MECH-256 repoint, so that chip is landed and no longer pending). Run record verified:
`v3_exq_671b_..._20260803T022036Z_v3.json`, FAIL 4/6, `n_samples = 179`, `n_seeds = 4`,
`pooled_precision_spread = 160658`, both positive-control gates clear
(residue 14.76 vs 1e-6 floor; precision spread 160658 vs floor 1). No successor queued: no
`671c` in `experiment_queue.json`, no `substrate_queue.json` row, no open chip (the only
`TASK_CHIPS.json` hits are the completed SD-003 repoint chips). Substrate re-checked: **no
`precision_mode` / `high_precision` / `action_precision` knob exists in `ree_core/`** --
precision is continuous only. `precision_margin_norm` confirmed live and unconditional
(`e3_selector.py:3676-3690`, pre-seeded at `:3402`, dict assigned unconditionally at `:3323`);
landed ree-v3 `48f85f0`, 2026-09-02.

**epistemic_category (proposed):** `standard` -- **unchanged.** It is already `standard` and
that is correct: the mechanism is built, exercised, and both positive controls clear, so it is
neither `substrate_conditional` nor `substrate_ceiling`. (Note against the obvious objection:
INV-012 Leg 0 being unmet does NOT make this claim substrate-blocked, because the 671 lineage's
DV does not require differentiated candidates -- it gates the *interpretation*, not the
*measurement*. See preamble (ii).)

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** Four parts. The first two are already implemented and
> already clearing -- keep them. The third and fourth are new and are what 671b lacked.
> **(P1) RESIDUE MUST ACCUMULATE UNDER COMMITTED HARM**, per seed, above a floor -- the gate
> added at 671a after V3-EXQ-671 measured C1 and C2 as exactly 0.0 across 778 committed
> harm-events because `ResidueField.total_residue` never moved (671b: 14.76 vs a 1e-6 floor).
> **(P2) PRECISION MUST VARY WITHIN EACH SEED'S OWN COMMITTED-STEP POPULATION**, checked
> GROUPED BY SEED rather than pooled -- the gate added at 671b, whose own docstring gives the
> reason: "a flat/pooled spread check can pass purely from BETWEEN-seed differences in average
> precision ... while precision is still pinned WITHIN every individual seed's own
> committed-step population". Keep this exactly as built.
> **(P3) THE ESTIMATOR ITSELF MUST BE WITHIN-SEED, AND THIS IS THE PART 671b GOT WRONG.**
> 671b applies P2's own reasoning to the independent variable's *spread* and then computes the
> DEPENDENT statistics by pooling raw `current_precision` across seeds
> (`pooled_precision.extend(r["precision_samples"])`, then one Pearson r and one median split
> over the pooled list). Per-seed precision spread in that run differs by ~37x
> (seed 0: 160611.76; seed 1: 5674.23; seed 2: 4300.25; seed 3: 0.00 at n=1), so the pooled
> median split is close to a seed-identity split. The consequence is visible in the run's own
> per-seed table: every seed's correlation is non-negative (+0.0505, +0.1017, +0.0651, 0.0000)
> while the POOLED correlation is NEGATIVE (-0.0446), and 2 of the 3 non-degenerate seeds have
> ratios above the 1.1 bar (1.1327, 1.1471) while the pooled ratio is 1.0618. That is a
> between-group confound inverting the sign of every within-group constituent, and the driver's
> own docstring already identifies the correct frame -- "the claim under test is about a
> within-run relationship" -- immediately before pooling across runs. Require: the primary
> statistic is a per-seed correlation (Fisher-z averaged across seeds), the median split is
> taken WITHIN each seed, the regressor is scale-free (`precision_margin_norm`, or per-seed
> z-scored `current_precision`), and any seed with fewer than 20 committed harm-events is
> excluded from the primary estimator and reported separately -- 671b's seed 3 contributed
> n=1 with a fill-value correlation of 0.0 and a ratio of 0.0 into a pooled n of 179.
> If a pooled statistic is reported at all it is a diagnostic, and pre-registration must say
> that a sign disagreement between pooled and within-seed estimates resolves in favour of the
> within-seed one.
> **(P4) THE PASS BAR MUST BE DERIVED, NOT INHERITED.** `C1 > 0.15` has been carried unchanged
> from 671 through 671a to 671b and was never derived from an expected effect size. Because the
> sample is restricted to committed steps -- i.e. to the `commit_variance < effective_threshold`
> tail of the same scalar the commit gate thresholds on -- the correlation is range-restricted
> by construction and attenuated relative to any unrestricted estimate. Pre-register the bar
> from a measured range-restriction correction or from a stated minimum practically-relevant
> effect, and state it before the run.
>
> **CONFIRMING.** With P1-P4 met: the within-seed correlation between commit-time precision
> (`precision_margin_norm`) and residue accumulated per unit harm is positive, the Fisher-z
> averaged estimate exceeds the pre-registered bar with a 95% CI excluding 0, and the
> within-seed high/low median-split ratio exceeds its bar on >= 4/5 seeds with >= 20 events each.
> **Scope limit on what a PASS licenses, and it is not decorative:** this would confirm that
> precision SCALES RESIDUE WEIGHT. It would NOT yet confirm the claim's stated rationale, that
> higher precision implies higher ETHICAL ACCOUNTABILITY "because the agent ... could have done
> otherwise with finer discrimination" -- that premise is INV-012 Leg 0, recorded in INV-012's
> own `what_would_answer` as CURRENTLY UNMET (MECH-439, `ceiling_decision: exhausted`, latest
> entry `failure_autopsy_V3-EXQ-571b_2026-09-01`). Do not re-derive Leg 0 here: see INV-012's
> own `what_would_answer`, Leg 0. A PASS therefore promotes the mechanistic half and leaves the
> accountability bridge explicitly gated.
>
> **FALSIFYING.** With P1-P4 met and >= 5 seeds each carrying >= 20 committed harm-events, the
> within-seed correlation is null or negative and the within-seed ratio does not clear its bar
> on a majority of seeds. This IS real claim pressure -- unlike 671 (degenerate), 671a
> (single-seed, missing precision-variance control) and 671b (confounded estimator), none of
> which is. The philosophical bridge would then be unsupported on its own chosen
> operationalization, and MECH-025b should be narrowed to the mechanistic reading (precision
> co-varies with residue) or retired in favour of MECH-025 plus MECH-256, with INV-012's Leg 1/3
> carrying the responsibility content instead. Note there is no biological reference to check a
> null against: by the claim's own 2026-04-02 decomposition note it is a philosophical
> construct, not a translated neuroscience finding, so literature cannot rescue a null here.
>
> **INSTRUMENT NOTE (currency).** `precision_margin_norm` -- normalized 0 at the commit
> threshold to 1 at maximal confidence, set on every world-variance-mode tick and deliberately
> ungated ("mirrors `conflict_gap_norm`'s always-set convention") -- landed in ree-v3 `48f85f0`
> on 2026-09-02, 32 days AFTER 671b ran. It is scale-free across seeds by construction and is
> the correct regressor for P3. Also note the substrate has no discrete precision MODE
> (`ree_core/` has no `precision_mode` / `high_precision` / `action_precision` knob); the
> claim's title phrase "high-precision action mode" is testable only as a LEVEL, which is how
> this falsifier is written and is consistent with MECH-025's own literature finding that
> Friston 2013 records precision as continuous rather than as a discrete mode switch.

**Proposal sketch (a):**
- **title:** `V3-EXQ-671c -- MECH-025b precision-margin x residue within-seed regression (per-seed estimator, MECH-027 precision_margin_norm, 5 seeds)`
- **related_claims:** `MECH-025b` (primary), `MECH-025` (parent; supplies the "precision is
  continuous, not a mode" constraint), `ARC-016` (the precision->commitment circuit, `stable`),
  `MECH-256` (the self-attribution half the responsibility reading needs), `INV-012` (Leg 0
  gates the accountability interpretation of a PASS)
- **acceptance_checks:**
  - `G1_residue_accumulates` (GATING, per seed): unchanged from 671a/671b.
  - `G2_precision_spread_grouped_by_seed` (GATING): unchanged from 671b -- keep the GROUP-mode
    `check_degeneracy`, do not revert it to a flat/pooled check.
  - `G3_per_seed_power` (GATING): >= 5 seeds, each with >= 20 committed agent-owned harm-events;
    seeds below 20 excluded from the primary estimator and reported separately.
  - `G4_estimator_is_within_seed` (GATING, source-level): the primary C1/C2 statistics are
    computed per seed and aggregated (Fisher-z for r; per-seed median split for the ratio); no
    cross-seed pooling feeds a gating criterion.
  - `C1_within_seed_correlation`: Fisher-z averaged per-seed r(`precision_margin_norm`,
    residue-per-unit-harm) exceeds the pre-registered bar, 95% CI excluding 0.
  - `C2_within_seed_ratio`: per-seed high/low median-split ratio > bar on >= 4/5 qualifying seeds.
  - `C3_world_forward_r2 > 0.05`, `C4_harm_pred_std > 0.01` (retained from 671b), `C5` no fatal errors.
  - **Reported, non-gating:** the pooled statistics, alongside the between-seed variance
    component, so the 671b confound is visible rather than silently repeated.
- **Efficiency note for the orchestrator:** G1/G2 here and G0/G1 in ARC-029's proposal read the
  same `precision_margin_norm` stream from the same rollout. If both are queued, a single driver
  emitting both DVs is cheaper and makes the mutual confound in preamble (iv) directly
  measurable in one run rather than inferred across two.

**depends_on additions (if any):** none required. `depends_on: [MECH-025, ARC-016, INV-012,
MECH-256]` is correct and current (the SD-003 -> MECH-256 repoint landed 2026-09-01). I
considered adding `MECH-487` and rejected it -- see preamble (i): MECH-487 concerns the
retained counterfactual arm, MECH-025b the weighting of the taken arm; they are siblings under
INV-012, not dependencies.

**GOVERNANCE FLAG (1 of 2):** `evidence_discrepancy` -- **the 2026-08-03 `weakens/standard`
verdict on MECH-025b rests on a pooled estimator that is confounded by seed and whose sign
inverts every one of its constituents.** V3-EXQ-671b computes its gating C1/C2 on samples
pooled across 4 seeds whose per-seed precision spreads differ by ~37x (160611.76 / 5674.23 /
4300.25 / 0.00), so the pooled median split approximates a seed-identity split. Per-seed
correlations: +0.0505, +0.1017, +0.0651, 0.0000 -- **all non-negative.** Pooled correlation:
**-0.0446.** Per-seed ratios: 0.9214, 1.1327, 1.1471, 0.0000 -- **2 of 3 non-degenerate seeds
clear the 1.1 bar.** Pooled ratio: 1.0618. Seed 3 contributed n=1 with fill-value statistics
(r = 0.0, ratio = 0.0) into the pooled n = 179. The driver's own docstring identifies exactly
this failure class for the positive control ("cross-seed variance masks within-seed pinning")
and then commits it on the DV, having stated one line earlier that "the claim under test is
about a within-run relationship". Recommend re-adjudicating 671b from
`weakens/standard` to `non_contributory / measurement_test_design_defect` (or `inconclusive /
measurement_gap`), routing to V3-EXQ-671c above. **This does not amount to confirming the
claim** -- every per-seed correlation is still well below the 0.15 bar -- but it removes the
only recorded claim pressure against MECH-025b, so the disposition is materially affected.

**GOVERNANCE FLAG (2 of 2):** `evidence_discrepancy` (minor, registry/index disagreement) --
the 671b manifest carries `evidence_direction: "mixed"` and `claim_evidence.v1.json` scores it
accordingly (`genuine_exp_direction_counts: {mixed: 1, weakens: 0}`), while the claim's
`live_status.evidence.verdict` records `weakens/standard`. The registry and the indexed
evidence disagree about the direction of the single genuine experimental entry for this claim.
Whichever way flag 1 above is resolved, the two should be made to agree (this is the
`supersedes`-class silent-loss pattern the CLAUDE.md EXQ-versioning section warns about: a
governance verdict applied to `live_status` without a corresponding manifest direction change
never reaches the indexer).

---

<!-- S_SD-063 appended 2026-09-04T21:29:11Z -->
## G21 -- SD-063 E2 conditional predictive-uncertainty head  (agent report)

### Solo note
Single-claim group: no cross-claim mandate applies. The cross-claim work that *is* load-bearing here is
vertical rather than lateral -- SD-063's head is the producer for three downstream consumers built after
its promotion (MECH-314b per-candidate curiosity, MECH-482/SD-102 epistemic-deficit accumulator, and the
never-exercised E3 commit gate the claim's own title names). Findings on those consumers are reported
under Currency check and in the three GOVERNANCE FLAG blocks, not as a group preamble.

---

### SD-063 -- E2 world-forward carries a conditional predictive-uncertainty head (distribution-free quantile form) feeding E3 commitment gating

**Recommended disposition:** (a) testable now -- the head is BUILT, trainable, demonstrably live (relative
pvar spread 1.31-3.20 on trained arms), and the calibration falsifier can be scored with an instrument that
already exists and already ran three days ago (V3-EXQ-977's `coverage_80` / `coverage_err_80`), so the
missing `what_would_answer` is a write-down, not a design problem.

**Extracted from:** four sources, none invented. (1) The head module's own docstring P2 plan
(`/Users/dgolden/REE_Working/ree-v3/ree_core/predictors/e2_world_uncertainty.py:58` -- "P2: evaluate
held-out CRPS, precision_error_corr, and -- the SD-063 falsifier -- that the E2WorldForward agency residual
is unchanged") and the design doc's Validation section
(`/Users/dgolden/REE_Working/REE_assembly/docs/architecture/sd_063_e2_conditional_uncertainty_head.md:112-115`).
(2) V3-EXQ-716a's own pre-registered thresholds, reused verbatim as the confirming bars
(`crps_improve_frac` 0.02, `corr_floor` 0.15, `c3_preserve_frac` 0.75, `readiness_norm_residual_floor` 0.05).
(3) SD-063's OWN literature evidence, which already states the calibration gap as its central open risk:
`2026-07-08_sd_063_beyond_pinball_loss_calibration_chung2021` (direction `mixed`, conf 0.6) whose third
failure signature reads, verbatim from `claim_evidence.v1.json`: "The paper's calibration metric (ECE over
quantile levels) is not what V3-EXQ-712 measured (CRPS + precision_error_corr); a head that wins on CRPS
can still be miscalibrated in the Chung sense, so SD-063's diagnostic PASS does not certify calibration."
The falsifier below is that sentence turned into a scored criterion. (4) The coverage instrument itself,
already implemented and run in `v3_exq_977_arc052_harm_stream_conditional_precision.py` (per-arm
`coverage_80`, `coverage_err_80` over the same 9 quantile levels).

**Currency check:** eleven items verified; six are stale-note or unrouted-evidence findings.

1. *Block currency.* The block handed to me is byte-equivalent in content to the live
   `claims.yaml` (lines 70745-70854); only YAML scalar style differs. No drift. SD-063 has NO
   `what_would_answer`, NO `epistemic_category`, NO `digestion_note`; `status: provisional`,
   `v3_pending: false`, `depends_on: [MECH-059, SD-031]`.
2. *Reverse-deps: ZERO.* No claim in `claims.yaml` lists SD-063 in `depends_on` (checked by loading the
   whole registry, not by grep). MECH-482 references the head only in prose notes. So the fan-in 0 in the
   task header is matched by fan-out 0 in the registry, despite three real code-level consumers. See
   GOVERNANCE FLAG 2.
3. *The head is BUILT.* `ree-v3/ree_core/predictors/e2_world_uncertainty.py` -- `E2WorldUncertaintyHead`
   + `E2WorldUncertaintyConfig`, 9 fixed levels 0.1..0.9, pinball loss, `predictive_variance` =
   monotone-rearranged (`torch.sort`) `[q0.1,q0.9]` IQR / `IQR_TO_STD_10_90=2.5631`, squared, meaned over
   dims, under `no_grad`. **`[q0.1, q0.9]` is explicitly documented as "the nominal-80% predictive
   interval" (line 89)** -- so nominal coverage is well-defined for this head without any new design work.
4. *It is DEFAULT-OFF, on three independent flags,* all `False` in
   `ree-v3/ree_core/utils/config.py`: `LatentStackConfig.use_e2_world_uncertainty` (323),
   `LatentStackConfig.use_e2_world_uncertainty_online_training` (339),
   `E3Config.use_conditional_precision_gate` (1114). Instantiation is agent-level
   (`agent.py:584-623`); training is `agent.py:_train_e2_world_uncertainty` (4379+), gated on
   `train_online` AND `self.training` AND not `hypothesis_tag`.
5. *It IS consumed -- but not by the consumer the claim's title names.* Live consumers found in
   `ree_core/`: (i) MECH-314b per-candidate curiosity via `curiosity_uncertainty_source=
   "e2_predictive_variance"` (`policy/structured_curiosity.py:403`, `agent._curiosity_per_candidate_
   uncertainty`); (ii) MECH-482/SD-102 `policy/epistemic_deficit.py` (uses the head's pvar AND its median
   vs `e2.world_forward`'s point prediction as a disagreement signal); (iii) the E3 commit gate,
   `e3_selector.py:3667-3675`.
6. *The E3 commit gate has NEVER been exercised.* `use_conditional_precision_gate` is set `True` in
   **zero** experiment drivers -- a whole-tree grep finds it only in `ree_core/`, in two contract test
   files (`tests/contracts/test_sd063_conditional_uncertainty_head.py`,
   `test_from_dims_flag_reachability.py`), in `tests/test_flag_inertness.py`, and in **docstring prose**
   inside `v3_exq_716.py` / `v3_exq_716a.py`. No driver ever passes `conditional_predictive_variance` into
   `E3.select()`. See GOVERNANCE FLAG 1.
7. *What 716a actually scored.* `v3_exq_716a_..._20260709T193517Z_v3.json` (PASS, `evidence`,
   `claim_ids:[SD-063]`, `supports`, 3/3 seeds) measures C1 `crps_quantile` 0.0886 vs `crps_point` 0.0981,
   C2 `precision_error_corr_quantile` 0.385 vs `precision_error_corr_point` 0.0, C3 `cf_gap` 1.452
   preserved. All three are **offline predictor-quality metrics on held-out transitions.** No coverage,
   no calibration, and no selection-level or commitment-level DV anywhere in the manifest.
8. *Fresh, decisive, unrouted coverage evidence (2026-09-03).* `v3_exq_977_arc052_harm_stream_conditional_
   precision_20260903T112134Z_v3.json` (PASS, `claim_ids:[ARC-052]`, reviewed 2026-09-03 by
   `governance-20260903T2013`) runs the SAME head class at the SAME 9 levels across three streams x
   {point, quantile} x 5 seeds and records `coverage_80` per arm. On **z_world -- SD-063's own stream** the
   trained quantile head under-covers its nominal 80% band on **5/5 seeds**: 0.7186 / 0.7346 / 0.7119 /
   0.7015 / 0.7104, mean 0.7154, mean `coverage_err_80` 0.0846. Same direction on z_harm_s (mean 0.7076);
   z_harm_a is close to nominal (mean 0.7781). `precision_error_corr` beats its permutation null 5/5 on
   every quantile arm (0.22-0.75), and `pvar_relative_spread` is 1.31-3.20, so the head is LIVE, not
   random-init. **Scope caveat, stated rather than glossed: 977 ran with `encoders_trained: False`**, i.e.
   an untrained z_world encoder -- the exact P0 condition SD-063's own phased protocol requires and 716a
   supplied. So this is strong, seed-consistent evidence that the *form* under-covers, measured on a
   weaker latent than SD-063's validated config; it is NOT yet a verdict on SD-063's own configuration.
   That is precisely why the falsifier below is worth queueing rather than declaring already-answered.
9. *The claim's title-half about magnitude is contradicted at selection level by V3-EXQ-949 (PASS,
   2026-08-25, MECH-314b, reviewed).* With the head trained and consumed per-candidate
   (`head_latched_pvar_relative_spread` 1.341, `pcv_relative_spread_mean` 0.639, `n_pcv_nonnull_ticks` 320),
   the head's per-candidate deviation is `last_uncertainty_dev_range_mean` **1.52e-05** against a
   `raw_score_range_mean` of **277.3** -- seven orders of magnitude down -- and `yoked_divergence_frac` is
   **0.0** over 320 ticks. It becomes behaviourally consequential (`yoked_divergence_frac` 0.35) ONLY in
   `ARM_B314_ON_AUTH_ON`, i.e. only when `use_modulatory_selection_authority` rescales it. The head's
   output carries no native authority at its natural scale.
10. *Same pattern one layer down.* `v3_exq_964_mech482_epistemic_deficit_validation_20260829T215030Z_v3`
    is a **FAIL** whose interpretation label is literally
    `accumulator_live_but_never_changes_committed_action` -- the SD-102 accumulator that eats SD-063's head
    output is live and inert. This is the same shape the MECH-485 agent is checking for
    `predicted_harm_delta`, arriving twice independently downstream of this head.
11. *substrate_queue.json is STALE on SD-063* (`evidence/planning/substrate_queue.json:6317-6333`):
    `"ready": false`, `"unblocks_claims": []`, `"validation_experiment"` still points at V3-EXQ-716 (the
    non_contributory diagnostic) rather than 716a (the scoring confirmation that promoted the claim), and
    `"last_seen_session": "substrate-queue-reconcile-20260708T2009Z"` -- 2026-07-08, one day BEFORE the
    716a promotion and seven weeks before the three consumers landed. See GOVERNANCE FLAG 3.
12. *IMPL-022 already requires the metric that is missing.*
    `docs/architecture/jepa_e1e2_integration_contract.md:193` requires
    `latent_uncertainty_calibration_error` "(if uncertainty head present)". SD-063 is the only uncertainty
    head in `ree_core/`. A whole-tree grep of `ree-v3` for `latent_uncertainty_calibration_error` returns
    **nothing** -- the contract field is declared and never emitted.

**epistemic_category (proposed):** `standard`. Not `substrate_ceiling` and not `substrate_conditional`:
the head exists, has been trained and exercised non-degenerately in at least three independent runs (716a,
949, 977), and the falsifier's blocking condition is an unqueued experiment, not missing code or an
absorbing downstream mechanism. (The *consumer* half -- the E3 commit gate -- is built-but-unexercised,
which is an unqueued-test condition, not a ceiling.)

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (all four must hold in the scored run, or the run self-routes
> `substrate_not_ready` rather than reporting a verdict):
> (i) ENCODER TRAINED -- the P0 warmup ran (`encoders_trained: true`); an untrained z_world encoder yields
> a near-invariant latent and a trivially-fittable spread (the MECH-353 / V3-EXQ-642 vacuity lesson, and
> the reason V3-EXQ-977's `encoders_trained: false` coverage reading is indicative rather than decisive).
> (ii) HEAD TRAINED, NOT RANDOM-INIT -- `e2_world_uncertainty_last_pvar_relative_spread >= 1.0` evaluated
> across all action classes at a fixed z_world. RELATIVE spread, never absolute range: per
> `e2_world_uncertainty.py`'s measured note, an UNTRAINED head has the LARGER absolute range (8.63e-04 vs
> 7.14e-04) and passes any absolute-range gate, so `last_uncertainty_dev_range > 0` is necessary but NOT
> sufficient (this is the corrected ARC-065 section-5 gate; V3-EXQ-949 used `HEAD_REL_SPREAD_FLOOR = 1.0`).
> (iii) TRANSITIONS NON-DETERMINISTIC ENOUGH FOR AN INTERVAL TO MEAN ANYTHING -- this arm's own normalised
> held-out residual `norm_residual = point_rmse / target_std >= 0.05` (716a's
> `readiness_norm_residual_floor`; 977 measured 0.087-0.155 and 716a 0.414). A deterministic transition set
> makes the nominal-80% band trivially wide-or-empty and the coverage test vacuous.
> (iv) SUFFICIENT HELD-OUT MASS -- `n_test >= 200` held-out transitions per arm per seed (977's floor;
> 716a banked 714 eval / 2142).
>
> CONFIRMING (all three, majority of >= 3 seeds, with the SD-031 guard held):
> (C1) CALIBRATION -- empirical coverage of the monotone-rearranged `[q0.1, q0.9]` band on held-out
> `(z_world_t, a_t) -> z_world_{t+1}` transitions matches its nominal 0.80:
> `|coverage_80 - 0.80| <= max(0.03, 2 x SD(coverage_80) across seeds)`. The absolute floor of 0.03 is
> what stops a high-variance run from passing by being noisy.
> (C2) THE WIDTH CARRIES INFORMATION BEYOND A CONSTANT -- (a) `pvar_relative_spread > 0` and
> (b) `precision_error_corr >= 0.15` (716a's `corr_floor`) AND above its own permutation-null p95 (977's
> instrument; measured p95 ~0.055 there). Both legs are required: (a) alone is passed by a head whose
> width varies arbitrarily, (b) alone is undefined for a constant-width band.
> (C3) IT BEATS THE NULL IT CLAIMS TO REPLACE -- CRPS improvement over the matched point head
> >= 2% (716a's `crps_improve_frac`), and `precision_error_corr` strictly above E3's running-variance EMA
> null, which is 0.0 by construction.
> (C4, the consumer half the title asserts) WITH `E3Config.use_conditional_precision_gate = True` and the
> head supplying `conditional_predictive_variance`, a YOKED comparison against the EMA fallback (identical
> seeds, identical candidate sets, gate the only difference) shows `yoked_divergence_frac > 0` on
> >= 300 candidate ticks -- i.e. the per-input spread changes at least some commit/hold decisions.
>
> FALSIFYING (any one):
> (F1) COVERAGE SYSTEMATICALLY OFF -- `|coverage_err_80| > 0.05` with the SAME SIGN on >= 4 of 5 seeds.
> This is the Chung-2021 failure mode already carried as `mixed` literature on this claim, and it is
> exactly what V3-EXQ-977 measures on z_world at 5/5 seeds under-covering (0.7015-0.7346, mean err 0.0846)
> with an untrained encoder. A pinball head can win CRPS and still be miscalibrated; if C1 fails while C3
> passes, SD-063's per-prediction spread is a good RANKING signal and a bad PROBABILITY, and the claim
> must be narrowed to the ranking reading (which is what the E3 commit gate, a threshold comparison in
> variance space, actually needs) rather than kept as stated.
> (F2) THE INTERVAL WIDTH CARRIES NO INFORMATION BEYOND A CONSTANT -- `precision_error_corr` fails to beat
> its permutation null, or `pvar_relative_spread` is at floor while precondition (ii) passes. The head is
> then an expensive constant band and the EMA null is not beaten.
> (F3) CONSUMER INERTNESS -- C4's `yoked_divergence_frac == 0.0` with all four preconditions met. The head
> is computed and never consumed at the commit gate; SD-063's "feeding E3 commitment gating" clause is
> then false as stated, independently of C1-C3. Precedent that this is a real risk, not a formality:
> V3-EXQ-949's `ARM_B314_ON_AUTH_OFF` (`yoked_divergence_frac` 0.0, per-candidate deviation 1.5e-05 vs a
> score range of 277) and V3-EXQ-964's FAIL label `accumulator_live_but_never_changes_committed_action`.
> (F4) SD-031 GUARD BREACHED -- the E2WorldForward agency residual (`cf_gap`) drops below 0.75 of its
> head-OFF value under joint training (716a's `c3_preserve_frac`). Structurally defended (separate module,
> detached inputs and target) but still empirically required on every scoring run.

**Proposal sketch (disposition a):**
- *title:* "V3-EXQ-XXX -- SD-063 conditional-uncertainty head: nominal-interval calibration and E3
  commit-gate consumption" (two-part: a calibration arm reusing 716a's phased P0/P1/P2 protocol with
  `encoders_trained: true`, and a yoked commit-gate arm that is the first ever exercise of
  `use_conditional_precision_gate`).
- *related_claims:* SD-063 (primary), MECH-059 (the confidence channel this realizes), SD-031 (the agency
  residual guard, F4), IMPL-022 (the contract field `latent_uncertainty_calibration_error` this run would
  be the first to emit). Report-only cross-references, no claim_ids beyond SD-063 unless the driver
  genuinely scores them.
- *acceptance_checks:* preconditions (i)-(iv) above as gating readiness checks; C1/C2/C3 as the
  calibration arm's scored criteria (per-seed majority of 5); C4 as the commit-gate arm's scored criterion
  with F3 pre-registered as its own off-ramp label (`head_computed_never_consumed_at_commit_gate`), so an
  inert result is a recorded finding rather than an ambiguous FAIL; F4 as a hard guard on both arms.
  Emit `coverage_80` / `coverage_err_80` per arm per seed (lift the instrument verbatim from
  `v3_exq_977_arc052_harm_stream_conditional_precision.py`) and `latent_uncertainty_calibration_error`
  under IMPL-022's stable key.
- *cheap first move, before queueing anything:* re-run 977's coverage instrument over 716a's already-banked
  configuration. If the deficit survives a trained encoder, F1 fires on existing evidence and the
  calibration arm can be skipped in favour of a narrowing.

**depends_on additions (if any):** none on SD-063 itself -- `[MECH-059, SD-031]` is correct and complete.
On the CONSUMER side, MECH-482 (and SD-102's registry surface) should list SD-063 in `depends_on`: three of
its inputs read this head, its own notes say so in prose, and the registry currently has zero reverse-deps
on SD-063. Proposed, not applied; raised as GOVERNANCE FLAG 2.

---

### The 2026-09-02 intake question: does "uncertainty non-dissipation across a blind rollout horizon" belong in SD-063's own `what_would_answer`?

**No -- and it does not need its own claim either. The intake's routing (an `IMPL-022` contract-field
addition, deliberately not `MECH-NEW-1`) is correct, and I would additionally decline to fold it into
SD-063.** Read in full:
`/Users/dgolden/REE_Working/REE_assembly/evidence/planning/thought_intake_2026-09-02_decision_useful_counterfactual_world_models_under_uncertainty.md`
(novelty table row 8; section 2 "Proposed IMPL-022 contract-field addition"; the "No MECH-NEW-1 was minted,
deliberately" paragraph).

Three reasons, in order of weight:

1. **DIFFERENT OBJECT.** SD-063's head is a strictly ONE-STEP conditional readout: `forward(z_world_t,
   a_t) -> [B, D, Q]` over the single transition to `z_world_{t+1}`, and nothing in `ree_core/` iterates
   it. `latent_uncertainty_horizon_dissipation_rate` is a property of a MULTI-STEP BLIND ROLLOUT -- the
   per-step signed change in the predictor's own uncertainty with no observation ingested after step 0.
   Folding it into SD-063's falsifier would make SD-063 refutable by the behaviour of an iteration path it
   does not assert, does not implement, and whose consumer is elsewhere (ARC-018 / MECH-033 hippocampal
   rollouts; MECH-385/ARC-091 belief-state, both v4). That is category error, and it would make an
   otherwise-clean V3-tractable falsifier v4-blocked.

2. **THE INTAKE'S OWN NON-DEGENERACY CLAUSE RULES IT OUT IN V3 TODAY.** The proposed check reads: "the
   check is vacuous unless the environment supplies genuinely ambiguous histories (one observation history
   compatible with several hidden continuations); a fully observable domain self-routes
   `substrate_not_ready` rather than reporting a PASS." REE's V3 test bed is CausalGridWorldV2. So a claim
   minted now would be born `substrate_conditional` with zero possible evidence -- and SD-063, whose own
   falsifier is scoreable this week, would inherit that block if the measurable were folded into its
   `what_would_answer`.

3. **BUT THE PRODUCER LINK IS REAL AND SHOULD BE RECORDED, JUST NOT AS A FALSIFIER CLAUSE.** The intake is
   right that SD-063 is "the existing REE component that could emit the per-step series; nothing else
   currently does". The correct home for that is the producer-side note on the IMPL-022 field (already
   drafted in the intake) plus a one-line cross-reference in SD-063's `notes`/`implementation_note` -- not
   a clause in `what_would_answer`, which is the claim's refutation condition and must stay scoreable.

**What DOES resolve SD-063's placeholder is the calibration falsifier above, not the horizon measurable** --
and the two are close enough to be confused, so the boundary is worth stating: calibration is coverage
AT A POINT (does the nominal-80% band contain 80% of realized next-states?); dissipation is the TRAJECTORY
of that estimate across a blind horizon. The intake makes exactly this distinction in its own novelty table
("`latent_uncertainty_calibration_error` measures calibration at a point, not its trajectory across a blind
horizon"). SD-063 owns the first; it does not own the second.

**One qualification for the parent.** If `/governance` decides the *requirement* (not merely the metric) is
claim-worthy, the intake already names the right shape -- a `mechanism_hypothesis` at
`docs/architecture/precision_control.md` with `depends_on: [MECH-510, MECH-059, SD-063, MECH-385]`. I do
not recommend minting it now: the thought proposes no mechanism for producing non-dissipation, explicitly
denies the density-matrix construction any privileged status, and the V3 substrate cannot make it
non-vacuous. Defer until a partially-observable test bed with verified multi-modal hidden continuations
exists.

---

**GOVERNANCE FLAG 1:** `evidence_discrepancy` -- **SD-063 was promoted to `provisional` on evidence that
never tested the half of the claim its title asserts.** The title says the head feeds "E3 commitment
gating"; the promoting run V3-EXQ-716a scores only offline predictor quality (CRPS, precision_error_corr,
agency-residual preservation) on held-out transitions. `E3Config.use_conditional_precision_gate` has never
been `True` in any experiment driver in the repo (verified by whole-tree grep: matches occur only in
`ree_core/`, three test files, and two experiment DOCSTRINGS). Two independent downstream runs show the
head's output going nowhere at the decision level: V3-EXQ-949 `ARM_B314_ON_AUTH_OFF` (`yoked_divergence_frac`
0.0 over 320 ticks; per-candidate deviation 1.52e-05 against a 277.3 score range; non-zero only under the
authority rescale, at 0.35) and V3-EXQ-964 FAIL labelled `accumulator_live_but_never_changes_committed_action`.
Recommended: do not demote -- the producer-side evidence is genuine -- but record that SD-063's provisional
standing covers the PRODUCER clause only, and gate any further promotion on the C4/F3 commit-gate arm above.
This is the same "computed and never consumed" shape being checked for `predicted_harm_delta` under
MECH-485.

**GOVERNANCE FLAG 2:** `evidence_discrepancy` -- **fresh, reviewed, unrouted calibration evidence.**
`v3_exq_977_arc052_harm_stream_conditional_precision_20260903T112134Z_v3` (PASS, reviewed 2026-09-03 by
`governance-20260903T2013`, whose Step-2b PASS skim recorded "NOTHING FOUND" against ARC-052's own
criteria) carries per-arm `coverage_80` telemetry showing the SD-063 head form under-covering its nominal
80% interval on z_world at 5/5 seeds (mean 0.7154, mean `coverage_err_80` 0.0846) and on z_harm_s (mean
0.7076). SD-063 is not among that run's `claim_ids`, so this deposits no SD-063 evidence and nothing routed
it. It is nonetheless the first empirical instance of the exact failure mode SD-063's own `mixed`
literature entry (Chung 2021) predicted, and it is measured on the same head class at the same nine
quantile levels. Caveat that must travel with the flag: `encoders_trained: false` in 977, so this is
indicative of the FORM, not yet a verdict on SD-063's own P0-trained configuration. Recommended: route it
as a recorded finding on SD-063 and let the C1 arm settle it. Sub-item, registry hygiene: SD-063 has ZERO
reverse-`depends_on` in `claims.yaml` despite three live code consumers -- MECH-482 at minimum should list
it.

**GOVERNANCE FLAG 3:** `stale_note` -- **`evidence/planning/substrate_queue.json` SD-063 entry (line 6317)
is fourteen months of drift behind in miniature.** It carries `"ready": false` and `"unblocks_claims": []`
with `"validation_experiment"` pointing at V3-EXQ-716 (the `non_contributory` diagnostic) rather than
V3-EXQ-716a (the scoring confirmation that actually promoted the claim on 2026-07-09), and
`"last_seen_session": "substrate-queue-reconcile-20260708T2009Z"` -- one day before that promotion and
seven weeks before MECH-314b (2026-08-08, ree-v3 c0e0ce8), SD-102/MECH-482 (2026-08-29) and ARC-052's
V3-EXQ-977 (2026-09-03) all landed as consumers of this head. A session reading the queue today would
conclude SD-063 is an unvalidated build that unblocks nothing. Recommended: `ready: true`,
`validation_experiment` -> the 716a run_id, `unblocks_claims: [MECH-314b, MECH-482, ARC-052]`, and a
`last_seen_session` refresh. Secondary: IMPL-022's required metric `latent_uncertainty_calibration_error`
(`docs/architecture/jepa_e1e2_integration_contract.md:193`, "if uncertainty head present") is declared and
emitted nowhere in `ree-v3` -- an unmet contract requirement whose only possible producer is this head.

---

<!-- S_MECH-332 appended 2026-09-04T21:29:11Z -->
## G19 -- MECH-332 nociceptive-attenuation dual-pathway dissociation  (agent report)

**Solo note:** single-claim assignment, so the four cross-claim questions reduce to cross-referencing the already-digested neighbours: MECH-332's D1 leg is SD-021's falsifier, its D2 leg is SD-029's C2 falsifier, and its non-degeneracy floor is inherited from MECH-090 (commit gate live) + SD-011 (harm-channel regime declared) + MECH-219 (z_harm dynamic range). The draft below points at those rather than re-deriving them. The one genuinely new finding is a measured harness defect that invalidates the two existing runs' recorded blocker.

---

### MECH-332 -- Nociceptive attenuation on z_harm_s is implemented by two mechanistically dissociable parallel pathways...

**Recommended disposition:** (a) testable now -- both pathways are BUILT in `ree_core/` and the 2x2 falsifier is already pre-registered in `experiments/v3_exq_878_mech332_efference_aic_dissociation.py`; the only thing standing between the claim and a verdict is a ~4-line driver plumbing repair (the identical repair already applied to the sibling v3_exq_325 family on 2026-08-22), NOT a substrate gap. Reframe to the REE leg per the FUSED pattern: the anatomical/pharmacological leg is `out_of_domain` and already answered.

**Extracted from:** (1) the claim's own `functional_restatement` D1/D2/D3 dissociation predictions; (2) their operationalisation and pre-registered thresholds in `/Users/dgolden/REE_Working/ree-v3/experiments/v3_exq_878_mech332_efference_aic_dissociation.py` (lines ~119-160, 279-283) and in the manifest's `pre_registered_thresholds`; (3) that driver's mandatory `custom_information.d3_operationalization_note`, which is the correct reading of "additive" on this substrate and is carried into the draft verbatim in substance; (4) sibling falsifiers SD-021 / SD-029 / MECH-090 / SD-011 / MECH-219 `what_would_answer` for the inherited preconditions. Nothing here is drafted from a blank page.

**Currency check:** five findings, four of them stale-note or discrepancy class.

1. **MEASURED TODAY (2026-09-04, ree-v3 trunk, read-only execution of `REEConfig.from_dims`): the Pathway-2 factor was NEVER ARMED in either V3-EXQ-878 or V3-EXQ-878a.** Both drivers build their config as `REEConfig.from_dims(..., heartbeat=HeartbeatConfig(beta_gate_bistable=True), **agent_kwargs)` where `agent_kwargs` carries `harm_descending_mod_enabled=True` (`experiments/v3_exq_878a_mech332_commitment_calibration.py:240-248`; `experiments/_lib/baselines/exq878_mech332_efference_aic_baseline.py:107-112`). Executing that exact call on trunk today returns:
   - `use_aic_analog -> True` (lands; AIC module is constructed and ticking)
   - `harm_descending_mod_enabled -> False` (**dropped** -- not a declared `from_dims` parameter; swallowed by the `**kwargs` catch-all)
   - `heartbeat.beta_gate_bistable -> False` (**dropped** -- whole sub-config object swallowed)
   - `latent.use_e2_harm_s_forward -> True` (lands; Pathway 1 was armed)
   The `agent.sense()` consumer is gated `if harm_descending_mod_enabled and new_latent.z_harm is not None:` (`ree_core/agent.py:5326-5335`), so that block was **never entered in any arm of any 878-family run**. Pathway 2 was not merely un-triggered -- it was not wired.
2. **The manifest carries the proof and nobody read it.** In `v3_exq_878_..._20260803T023041Z_v3.json`, `ARM_BOTH` and `ARM_E2_ONLY` are **bit-identical on every metric at every seed** (`self_other_discrimination_ratio` 1.223990714993279 / 2.4471959317738206 / 181733.03020497164; `z_harm_s_ratio` 1.0; identical event counts) despite differing only in the two Pathway-2 flags -- and `ARM_AIC_ONLY` is likewise indistinguishable from `ARM_NEITHER`. The 2x2 collapsed to a 1x2 on the E factor. This is the same signature as the EXQ-325a "DESCENDING == CONTROL bit-identical" failure that the 2026-08-22 correction traced to exactly this cause. Note also that the manifest's per-arm `harm_descending_mod_enabled: true` field records the driver's **intended** flags dict, not the realised config -- so the manifest actively asserts an arming that did not happen.
3. **The 2026-08-22 `from_dims` correction never reached this claim.** SD-021 and SD-032c both carry a long `[2026-08-22 correction, chip-20260822-exq325-family-evidence-disposition]` block in their `evidence_quality_note`. MECH-332's note stops at 2026-08-08 and has no equivalent. The repair itself (`chip-20260822-fromdims-exq325-dead-ablation-axis`) was **325-family-scoped**: `experiments/v3_exq_325a_sd021_descending_pain_modulation.py:130-133` now sets both flags by attribute assignment with an explicit "from_dims() silently drops unknown kwargs" comment, while `v3_exq_878` and `v3_exq_878a` still route them through `from_dims` on trunk today. `tests/contracts/test_from_dims_flag_reachability.py` lists both 878 drivers in `USAGE_DRIVEN_SUBCONFIG_DROP_SITES["heartbeat"]` and explicitly defers the evidence question ("Whether this invalidates any of these drivers' recorded evidence is a /governance + /failure-autopsy question, deliberately NOT adjudicated here").
   *Honest counterweight, stated so this is not over-read:* the `beta_gate_bistable` drop is **not by itself** sufficient to explain `n_committed_steps=0`, because V3-EXQ-325a suffered the same drop and still recorded `n_committed_steps=6000`. The `harm_descending_mod_enabled` drop **is** decisive and sufficient for the ARM_BOTH == ARM_E2_ONLY collapse, i.e. for D1 and D3 being structurally unevaluable.
4. **`commitment_closure_plan.md` GAP-11 is DONE and has been since 2026-05-17** (that plan's status table, row GAP-11: "DONE 2026-05-17: committed_mode_curriculum.py harness helper IMPLEMENTED; P0/P1/P2/clone_trained_agent API; smoke PASS"). MECH-332's `evidence_quality_note` still says both dissociation arms are "blocked until full substrate stack lands (MECH-256 + SD-021 jointly requiring committed-mode substrate -- see commitment_closure_plan.md GAP-11)". That sentence was already stale on the day it was written and is four months stale now. Neither 878 driver uses `committed_mode_curriculum` either.
5. **The v3_pending gate flagged by the run's own manifest was never lifted.** `custom_information.v3_pending_gate_stale_note` (2026-08-03) says: "claims.yaml MECH-332 still carries v3_pending=true / hold_pending_v3_substrate dated 2026-05-19, predating (or missing) the ARC-033 (e2_harm_s.py) + SD-032c (aic_analog.py) substrate mapping confirmed by this experiment's own code review. Flagged for governance to lift as a companion action." As of today the block still reads `v3_pending: true`, `live_status.reading: candidate/v3_pending`, `as_of: 2026-07-11`, `verdict: hold_pending_v3_substrate/applied`. The companion action never ran.

*Substrate confirmations (positive):* Pathway 2 is fully built -- `ree_core/cingulate/aic_analog.py` computes `harm_s_gain = 1.0 - base_attenuation * mode_weight * drive_protect` and `ree_core/agent.py:5307-5335` multiplies `z_harm` by it (z_harm_a deliberately untouched). Pathway 1's forward model is built -- `ree_core/predictors/e2_harm_s.py` (`E2HarmSForward`, action-conditioned residual-delta, SD-013 interventional/contrastive training). Neither needs a new build. **But Pathway 1 is not an attenuator on this substrate**: `ree_core/utils/config.py:162` states "z_harm bypasses reafference correction by construction", and the E2_harm_s residual is consumed by the MECH-276 ScientistAttributionBuffer / SD-003 attribution pipeline, never subtracted from sensed z_harm_s. `substrate_queue.json` (sd_id MECH-256) confirms the comparator side: "Mechanism is wired end-to-end (E2_harm_s ARC-033 + interventional training SD-013 + balanced-hazard curriculum SD-029)".

**epistemic_category (proposed):** `standard`.
Explicitly **not** `substrate_ceiling`: the ceiling test requires the mechanism to have been "built AND exercised, repeatedly, under genuinely non-degenerate conditions" -- Pathway 2 has been exercised **zero** times, and both 878-family runs self-recorded `non_degenerate: false` / `n_committed_steps=0`. The 2026-08-08 note in this claim's own text proposes routing a 5th re-queue "through /failure-autopsy for a ceiling read"; on finding 1 that ceiling read would be taken on evidence from a dead ablation axis and would stamp a ceiling the substrate has never been given a chance to hit.
Explicitly **not** `substrate_conditional` either: the operational discriminator for that category is that "the code it needs does not exist yet", and here both modules exist and are independently wireable. The blocker is a driver plumbing defect, which is `complicated (buildable)`, not `complex (probe-gated)`.

**FUSED-claim reframe (rule c2).** MECH-332 fuses two legs and only one is a REE question.
- **out_of_domain leg (already answered, no REE run bears on it):** that the two attenuation mechanisms are anatomically and pharmacologically distinct in mammals -- spinal dorsal-horn / S1-insula efference-copy subtraction versus pgACC -> PAG -> RVM opioid-tone-modulated behavioural-state gating; and the clinical mapping (D1 failure = phantom-limb-class pain, D2 failure = impaired stress-induced analgesia). This leg is carried by De Preter & Heinricher 2024 (PMID 38749825, PAG/RVM as behavioural-state gating, NOT efference-copy), Hofbauer 2001 (S1-vs-ACC double dissociation), Lalouni 2020 (~40% self/other threshold shift), and SD-021's 8-entry corpus at `literature_confidence: 0.852`. A counterexample would be a study showing PAG/RVM performing per-step motor-prediction cancellation, or showing efference-copy nociceptive suppression that is abolished by naloxone (i.e. one pathway, opioid-mediated, wearing two faces). No V3 run can bear on it and none should be scored against it. *Adjacent, but not the source:* `docs/thoughts/2026-02-11_opioid_receptors.md` (mu-opioid as commitment stabiliser rather than pleasure generator) is marked `Status: processed` into `docs/architecture/control_plane.md` (MECH-048), not into MECH-332; it supplies the opioid-tone framing behind Pathway 2's ON/OFF-cell gating but is not this claim's provenance (which is the 2026-05-17 self_attribution:GAP-4 lit-pull synthesis). `pharmacological_predictions.v1.json` has no MECH-332 or SD-021 entry -- registering the naloxone-reversal prediction there would be the clean home for this leg.
- **REE leg (the testable claim, and the one the draft below falsifies):** does the V3 substrate need **two** attenuation pathways to reproduce the z_harm_s attenuation signature, or does one suffice? Concretely: are the two implemented modules' signature effects **independent and non-interfering** -- each surviving undegraded when the other is co-active -- or does one crowd out / subsume the other?

**Claim-text defect to fix alongside (this is why "additive" cannot stand as written).** The title asserts "their attenuation effects are additive". On this substrate there is no combined-gain number to sum: Pathway 2 multiplies `z_harm` in `sense()`; Pathway 1 emits a prediction residual consumed by a different subsystem. The 878 driver already declared the honest reading and it should be promoted into the claim text: *not "the numbers sum", but "neither pathway crowds out or overwrites the other's effect when both are wired in"*. Recommend amending the title/`functional_restatement` D3 clause from ADDITIVITY to INDEPENDENCE / NON-INTERFERENCE.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (four gates; all four must be recorded in the manifest as MEASURED values, and the first is the one both prior runs silently failed).**
>
> (P0) **REALISED-CONFIG PROOF, not declared flags.** V3-EXQ-878 and 878a both recorded `harm_descending_mod_enabled: true` per arm while the live config held `False`, because `REEConfig.from_dims()` silently drops undeclared kwargs and whole sub-config objects. Any run scored against this claim MUST (i) set both Pathway-2 knobs by **attribute assignment on the returned config** (`config.harm_descending_mod_enabled = True`, `config.heartbeat.beta_gate_bistable = True`) -- the idiom `v3_exq_325a_sd021_descending_pain_modulation.py:130-133` already uses -- and (ii) **read the values back off the constructed config** and emit those read-back values, not the intended flags dict. Additionally: `ARM_BOTH` and `ARM_E2_ONLY` must **differ** on at least one Pathway-2-sensitive quantity (e.g. `z_harm_s_mean_uncommitted`). A bit-identical ARM_BOTH/ARM_E2_ONLY pair is not a null result -- it is proof the A factor is inert, and it self-routes `substrate_not_ready`.
>
> (P1) **COMMITMENT LIVE (inherited -- see MECH-090's own `what_would_answer` for the persistent-handle / object-identity precondition; do not re-derive).** `n_committed_steps >= 8` in every A=ON arm on at least 2 of 3 seeds, AND `z_harm_s_mean_committed > 0`. In V3-EXQ-878 the reported `z_harm_s_ratio = 1.0` in every arm was a fabricated 0/0 (`z_harm_s_mean_committed = 0.0`, `n_committed_steps = 0`), not a measured null.
>
> (P2) **EVENT BALANCE, ENFORCED AS A GATE (inherited -- this is SD-029's C0/C2 precondition; see SD-029's own `what_would_answer` for why it has been the binding constraint for 13+ runs, and do not re-derive it).** Per seed, per E=ON arm: `n_agent_caused_trials >= 6` AND `n_env_caused_trials >= 6`, AND `residual_agent_caused_mean > 1e-3`. This must **gate** `d2_pass`, not merely be recorded beside it: V3-EXQ-878 seed 13 had `n_agent_caused_trials = 0`, whose `self_other_discrimination_ratio = residual_env / max(1e-6, residual_agent)` evaluated to 1.8e5 and trivially cleared the 1.15 floor, scoring `d2_pass: true` vacuously.
>
> (P3) **HARM CHANNEL LIVE AND NON-SATURATED (the precondition shared across the z_harm_s / z_harm_a family; see MECH-219's `what_would_answer` for the dynamic-range wording and SD-011's for the regime-declaration requirement).** The run must declare `harm_history_len`, `use_gabaergic_decay`, and `limb_damage_enabled`, and z_harm_s must show nonzero variance across both the committed/uncommitted partition and the agent-caused/env-caused partition. A flat or saturated z_harm_s makes both `z_harm_s_ratio` and `self_other_discrimination_ratio` fabricated quantities regardless of how the flags landed.
>
> **CONFIRMING** (thresholds pre-registered in V3-EXQ-878; PASS on >= 2 of 3 seeds). Four-arm 2x2 on Factor E (`use_e2_harm_s_forward`) x Factor A (`use_aic_analog` + `harm_descending_mod_enabled`), arms ARM_BOTH / ARM_E2_ONLY / ARM_AIC_ONLY / ARM_NEITHER, identical arena and curriculum across arms:
> - **D1 (Pathway 2 works without Pathway 1):** `|z_harm_s_ratio[AIC_ONLY] - z_harm_s_ratio[BOTH]| <= 0.20` AND both `<= z_harm_s_ratio[NEITHER] - 0.03`. That is: commitment-gated attenuation of z_harm_s appears whether or not the efference-copy forward model is trained, and is near-equal in magnitude with and without it.
> - **D2 (Pathway 1 works without Pathway 2):** `|self_other[E2_ONLY] - self_other[BOTH]| <= 0.60` AND both `>= 1.15`. That is: the residual `z_harm_s_observed - E2_harm_s(z_harm_s_{t-1}, a_actual)` is measurably smaller on agent-caused than on externally-caused hazard transitions, with the descending pathway entirely absent -- and the Shergill-2003 **partial**, graded pattern, not binary abolition (this is the same discriminator SD-029's CONFIRMING clause states; a near-total attenuation falsifies there and here).
> - **D3 (independence / non-interference, NOT literal additivity):** `z_harm_s_ratio[BOTH] <= z_harm_s_ratio[AIC_ONLY] + 0.15` AND `self_other[BOTH] >= self_other[E2_ONLY] - 0.15`. That is: each pathway's own signature metric survives undegraded when the other is co-active. No summed-gain number is claimed or measured, because Pathway 1 is not a gain on z_harm_s at all -- it is a prediction residual consumed by the MECH-276 attribution buffer, while only Pathway 2 multiplies z_harm in `agent.sense()`.
> - **SELECTIVITY (from SD-021's already-drafted falsifier, cross-referenced not re-derived):** z_harm_a must remain unattenuated in every A=ON arm. Attenuating both streams is the Hofbauer-2001 violation SD-021 already names.
>
> **FALSIFYING** (any one, with P0-P3 all met -- otherwise the run is non_contributory, not a refutation):
> - **D1 fails:** with Pathway 1 ablated, z_harm_s attenuation during committed traversal collapses to the ARM_NEITHER level (`z_harm_s_ratio[AIC_ONLY] > z_harm_s_ratio[NEITHER] - 0.03`). Pathway 2 is then not independent -- it requires the forward model, and there is one pathway with two triggers, not two pathways.
> - **D2 fails:** with Pathway 2 ablated, `self_other[E2_ONLY] < 1.15` on a seed whose event counts clear P2. Self/other discrimination on z_harm_s then depends on descending modulation, again collapsing the two pathways into one.
> - **D3 fails:** either signature metric degrades by more than 0.15 when the other pathway is co-active -- one pathway crowds out or overwrites the other, refuting independence directly (this is the falsification most likely to be informative, since it is the only one of the three that cannot be produced by a mis-wired ablation).
> - **SELECTIVITY fails:** z_harm_a is also attenuated in A=ON arms.
>
> **NOT falsifying, and this is the load-bearing exclusion:** a bit-identical or near-identical pair of arms that differ only in flags proven un-landed at P0. Both existing MECH-332 runs (V3-EXQ-878 2026-08-03, V3-EXQ-878a 2026-08-08) fail P0 on measurement and are `non_contributory` for that reason, over and above the `n_committed_steps = 0` reason their autopsies recorded.

**Proposal sketch (disposition a):**
- **Title:** `V3-EXQ-878b -- MECH-332 dual-pathway dissociation, 2x2 with realised-config arming proof (supersedes V3-EXQ-878/878a)`
- **related_claims:** `MECH-332` (primary), `SD-021`, `SD-032c`, `SD-029`, `MECH-256`, `MECH-090`, `SD-011`
- **Pre-work (blocking, and it is a driver repair, not a substrate build):** port the `chip-20260822-fromdims-exq325-dead-ablation-axis` idiom into `experiments/v3_exq_878_mech332_efference_aic_dissociation.py` and `experiments/_lib/baselines/exq878_mech332_efference_aic_baseline.py` -- set `harm_descending_mod_enabled`, `descending_attenuation_factor`, and `heartbeat.beta_gate_bistable` by attribute assignment on the returned config, then read them back and record the read-back values per arm. Route through `/queue-experiment` under a **new letter**; do not re-use an 878/878a id. Note that the `heartbeat` sub-config drop is registered but NOT yet repaired anywhere in the repo (`test_from_dims_flag_reachability.py` `USAGE_DRIVEN_SUBCONFIG_DROP_SITES`), so this run would be the first to arm `beta_gate_bistable` for real in either the 321, 325 or 878 lineage.
- **acceptance_checks:**
  - `C0a` (arming): per arm, read-back `harm_descending_mod_enabled` and `heartbeat.beta_gate_bistable` equal the intended values; ARM_BOTH and ARM_E2_ONLY differ on `z_harm_s_mean_uncommitted`. Hard gate -- fail routes `substrate_not_ready`, not a verdict.
  - `C0b` (commitment): `n_committed_steps >= 8` and `z_harm_s_mean_committed > 0` in both A=ON arms, >= 2/3 seeds.
  - `C0c` (event balance): `n_agent_caused_trials >= 6` and `n_env_caused_trials >= 6` per seed per E=ON arm; gates C2 rather than sitting beside it.
  - `C0d` (channel live): z_harm_s variance > 0 across both partitions; regime fields (`harm_history_len`, `use_gabaergic_decay`, `limb_damage_enabled`) declared in the manifest.
  - `C1` = D1, `C2` = D2, `C3` = D3, `C4` = z_harm_a selectivity, thresholds exactly as pre-registered above; `PASS_MIN_SEEDS = 2`.
  - Arena/curriculum held at the 878 configuration (SD-022 `limb_damage_enabled=True` + SD-029 balanced-event curriculum with the EXQ-479 calibrated params), which demonstrably produced 12 agent-caused / 12 env-caused trials on 2 of 3 seeds -- keep it, and add a seed-selection or seed-count bump so 3 of 3 clear C0c.
- **Cost note:** 878a already established that training budget is not the lever for the commitment gate; C0b's outcome under a genuinely-armed bistable gate is the open empirical question, so run at the S0_baseline budget (180 eps) rather than repeating the 3x sweep.

**depends_on additions (if any):**
- `SD-032c` -- the AIC-analog IS the live Pathway-2 implementation (the raw beta-gate path is legacy/backward-compat only) and it is co-tagged on both existing runs, yet it is absent from `depends_on`.
- `MECH-090` -- Pathway 2's trigger is E3 commitment; MECH-090's `what_would_answer` carries the persistent-handle precondition this claim's P1 inherits.
- `MECH-276` (or `SD-003`) -- the actual consumer of the Pathway-1 residual. Recording it is what makes the "Pathway 1 is not a gain" fact structural in the registry rather than buried in a driver docstring.

---

### GOVERNANCE FLAGS

**FLAG 1 -- `evidence_discrepancy` (MECH-332, SD-021, SD-032c).** Both experiments ever run against MECH-332 (V3-EXQ-878, V3-EXQ-878a) had the Pathway-2 ablation axis **dead**: `harm_descending_mod_enabled=True` and `heartbeat=HeartbeatConfig(beta_gate_bistable=True)` are passed to `REEConfig.from_dims()` and silently dropped -- measured by direct execution on trunk 2026-09-04 (`harm_descending_mod_enabled -> False`, `heartbeat.beta_gate_bistable -> False`, while `use_aic_analog -> True` and `latent.use_e2_harm_s_forward -> True`). The corroborating evidence is already inside the 878 manifest: ARM_BOTH and ARM_E2_ONLY are bit-identical on every metric at every seed. Consequence: the 2026-08-03 and 2026-08-08 governance notes' shared conclusion -- "Pathway 2's claim-intrinsic trigger never had a chance to fire", "budget is NOT the lever" -- is confounded, and the 2026-08-08 note's proposed remedy ("route a 5th same-mechanism re-queue through /failure-autopsy for a ceiling read") would stamp `substrate_ceiling` on a mechanism that has never once been armed. **Recommend: do not take the ceiling read; re-tag both runs' `evidence_direction_note` with the arming defect; queue the repaired 878b.** This is the same defect class as, and directly parallel to, the `chip-20260822-exq325-family-evidence-disposition` correction that SD-021 and SD-032c already carry -- that repair was 325-family-scoped and the 878 family was left unrepaired on trunk.

**FLAG 2 -- `stale_note` (MECH-332).** Three stale items in this claim's own text, none of which required an experiment to detect: (i) the `evidence_quality_note` says both dissociation arms are "blocked until full substrate stack lands ... see commitment_closure_plan.md GAP-11" -- **GAP-11 has been `done` since 2026-05-17** per that plan's own status table, i.e. it was already stale when written; (ii) the note carries no equivalent of the `[2026-08-22 correction]` block that both SD-021 and SD-032c carry, despite the correction bearing directly on this claim's only two runs; (iii) the V3-EXQ-878 manifest's `custom_information.v3_pending_gate_stale_note` (2026-08-03) explicitly asked governance to lift the `v3_pending` gate as a companion action, on the ground that `hold_pending_v3_substrate` dated 2026-05-19 predates the ARC-033 + SD-032c substrate mapping -- the block still reads `v3_pending: true` / `hold_pending_v3_substrate/applied` today. Both modules are built; the hold has no remaining referent.

**FLAG 3 -- `evidence_discrepancy` (SD-029, and by inheritance MECH-256).** SD-029's `what_would_answer` (digested 2026-08-07) states that C2 "has never once been evaluable, because training/eval produces near-single-class agent-caused vs env-caused hazard-event distributions". V3-EXQ-878 ran four days earlier (2026-08-03) on the SD-029 balanced-event curriculum with the EXQ-479 calibrated params and recorded **12 agent-caused and 12 env-caused trials on 2 of 3 seeds**, with `self_other_discrimination_ratio` = 1.224 (seed 42) and 2.447 (seed 7) -- i.e. the graded, partial self/other attenuation pattern SD-029's CONFIRMING clause asks for, at values clearing its own 1.15 discrimination floor. That is not a promotion case (the run is non_contributory overall, the ratio was measured in a MECH-332 driver, and seed 13 degenerated) but it is a live counterexample to "never once evaluable" and it identifies a curriculum configuration that demonstrably produces the balance SD-029 has been waiting 13+ runs for. **Recommend: reconcile SD-029's precondition text against the 878 arena config, and consider it as the arena for SD-029's own retest.**

**FLAG 4 -- `contested_disposition` (MECH-332 / instrumentation).** V3-EXQ-878's `analysis.per_seed` records `d2_pass: true` on **all three** seeds including seed 13, which had `n_agent_caused_trials = 0`. `self_other_discrimination_ratio` is computed as `residual_env / max(1e-6, residual_agent)`, so a zero-event seed yields 1.8e5 and clears the 1.15 floor by five orders of magnitude. The run's own `pre_registered_thresholds` include `n_event_floor: 6`, but it evidently did not gate `d2_pass`. Any D2 verdict carried forward from this family is therefore vacuous on that seed. **Recommend: the event floor must gate the criterion, not sit beside it** -- folded into the draft `what_would_answer` P2 above.
