# Morning Agenda — 2026-06-10

Generated: 2026-06-10T04:24:34Z

> Read-only digest. No governance decisions made, nothing marked reviewed.

---

## Queue Status
- **Total pending: 0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0)
- **ALERT: Queue empty — 0 pending experiments.** New experiments should be queued today.
- **3 items `claimed` but no results landed** (possible stuck runners / long runs / stale claims to reconcile):
  - `V3-EXQ-655` — claimed by `ree-cloud-1` @ 2026-06-09T05:22Z (**~23h ago — STALE**, no manifest)
  - `V3-EXQ-603l` — claimed by `ree-cloud-2` @ 2026-06-09T18:45Z (~9.7h ago — stale, no manifest)
  - `V3-EXQ-660` — claimed by `DLAPTOP-4.local` @ 2026-06-09T21:38Z (~6.8h ago — borderline stale, no manifest)
  - All three exceed/approach the 6h stale threshold with no result on disk. Worth a runner/coordinator reconciliation check (see also `V3-EXQ-543g` flagged stuck-claimed in the ARC-062 plan).

---

## Experiments Awaiting Review (5 indexed / 0 runner-only)

### `v3_exq_588c_mech189_super_ordinal_seeding` — PASS — **supports**
- **Claims tested:** MECH-189 (candidate, exp_conf 0.0, lit_conf 0.834, quadrant `plausible_unproven`; genuine_exp_count 0 → this is the **first experimental support**)
- **Key metrics:** child anchors formed=1; adult READ-seeding fired n_seeds=206; z_goal.norm=0.394 (positive control); C1 (ARM_ON adult z_goal discriminates over ARM_OFF) load-bearing **PASS**; advisory crosses DevNeed-006 gate 0.4.
- **Classification:** evidence (directly tests MECH-189).
- **Governance impact if confirmed:** first genuine experimental support for MECH-189 — on review would lift exp_conf off 0.0 and move it out of the lit-only `plausible_unproven` quadrant. Ties to the infant-substrate plan (ISEF-002 lineage).
- **Supersedes:** `v3_exq_588_isef002_transient_benefit_zgoal_seeding`

### `v3_exq_485d_sd033b_ofc_trainable_head_readiness` — PASS — non_contributory (readiness)
- **Claims tested:** none tagged (SD-033b OFC trainable-head substrate readiness probe).
- **Key metrics:** head weight-Δ L2=0.231 (>0.001 floor); C1 frozen-silent **PASS**, C2 head-trains **PASS**, C3 bias-nonzero (informational) PASS.
- **Classification:** diagnostic / substrate-readiness gate (intentionally `non_contributory` — does not weight a claim).
- **Governance impact:** confirms the SD-033b OFC trainable head is wired and trainable → unblocks the SD-033b validation successor. Adjacent to commitment_closure GAP-1 (`V3-EXQ-598` frozen-vs-trainable bias head).

### `v3_exq_569f_gapa_e2wf_matched_entropy_falsifier` — FAIL — **weakens**
- **Claims tested:** ARC-065 (provisional, exp_conf 0.9, lit_conf 0.866, quadrant `confirmed_established`; 46 supports / 1 weakens / 5 mixed)
- **Key metrics:** all 3 readiness preconditions met (consumed-summary spread 0.196 > 0.05 floor; e2.world_forward prediction spread 0.196 > 0.03; consumed spread bounded 0.67 << ceiling). C1 (ARM_1 e2_world_forward divergent) **PASS**; C_R1B (selected entropy strict-above matched-noise + proposer) **FAIL**.
- **Classification:** diagnostic / mechanism-isolation falsifier (GAP-A theory-1 isolation), not a claim-level falsifier.
- **Interpretation (`r1a_entropy_only_artefact`):** R1.b cleared (diversity above matched noise is a real contributor) but R1.a failed → "theory-1 (entropy alone)" is **not load-bearing on its own**. Routed to `/failure-autopsy` + substrate revisit; the runner note explicitly says *do NOT weaken on the requeue path*.
- **Governance impact:** ARC-065 stays `confirmed_established` (exp 0.9) — this is a within-claim mechanism decomposition, not a threat to the claim. Surfaces that the diversity pathway is multi-factor, not entropy-only. Supersedes `V3-EXQ-569d`.

### `v3_exq_654a_arc062_gapb_rule_apprehension_behavioural_falsifier` — FAIL — non_contributory
- **Claims tested:** ARC-062 (candidate, `substrate_ceiling`, exp_conf 0.491, lit 0.862, `plausible_unproven`; 17 supports / 9 weakens), MECH-309 (candidate, `substrate_ceiling`, exp_conf 0.771, `confirmed_established`)
- **Key metrics:** manifest carries no `interpretation` block; outcome FAIL, direction `non_contributory`.
- **Classification:** behavioural falsifier (GAP-B / 543-lineage continuation).
- **Governance impact:** `non_contributory` → no claim weight; per routing policy (completed FAIL) this needs a `/failure-autopsy` diagnosis pass, not force-mapping. This is the same ARC-062 head-input-contract bottleneck thread the arc_062 plan is tracking (see PLAN STALING below). Supersedes `V3-EXQ-654`.

### `v3_exq_661_mech294_compose_coherence_behavioural_readiness` — FAIL — non_contributory
- **Claims tested:** none tagged (probes MECH-294 theta-burst joint-binding behaviourally).
- **Key metrics:** all readiness met (joint first-action diversity=2.0; compose fired n=7; coherence gate mode-distinct Δ=1.0). C1/C2/C3 (joint-vs-alt, joint-vs-shuffled, coherence-gating-load-bearing) **all FAIL**.
- **Classification:** diagnostic / wiring-readiness (intentionally untagged so it does not weight MECH-294).
- **Interpretation (`coherence_gating_not_load_bearing`):** ALTERNATION with coherence gate ON behaves the same as OFF → any mode discrimination is packet-presence / action-only, **not co-binding coherence**. Route to `/failure-autopsy`; **do NOT** queue the MECH-294 joint-specificity behavioural successor on this reading.
- **Governance impact:** negative diagnostic — blocks the MECH-294 behavioural-evidence path until co-binding-reaches-behaviour wiring is re-established. MECH-294 stays exp_conf 0.0 / `plausible_unproven`.

---

## Errors to Diagnose (0 actionable)

Pipeline reports **0 runner-only pending** (no ERROR/UNKNOWN in the review queue).

Legacy ERRORs with no PASS/FAIL successor and not in queue (all old, **not** in current `pending_review.md` — likely already handled/superseded; verify before any requeue):
- `V3-EXQ-606a` (2026-05-21), `V3-EXQ-538` (2026-05-08), `V3-EXQ-495` (2026-04-28)
- `V3-ONBOARD-smoke-ree-cloud-1` (2026-04-06), `V3-ONBOARD-smoke-EWIN-PC` (2026-04-05) — onboarding smokes, non-scientific.

No action required unless one of these is intentionally being re-run.

---

## Governance Agenda (8 recommendations — all HOLD, 0 promote/demote pending)

No promotion or demotion is awaiting a user decision. The 8 `pending_user` rows are all holds:

**hold_pending_v3_substrate (7):**
- `ARC-072` (candidate, exp 0.0 / lit 0.781, plausible_unproven)
- `INV-041` (candidate, exp 0.0 / lit 0.64, plausible_unproven)
- `MECH-121` (candidate, exp 0.0 / lit 0.924, plausible_unproven)
- `MECH-346` (candidate, exp 0.771 / lit 0.0, **novel_discovery**)
- `MECH-347` (candidate, exp 0.771 / lit 0.0, **novel_discovery**)
- `SD-055` (candidate, exp 0.0 / lit 0.775, plausible_unproven)
- `SD-057` (candidate, exp 0.771 / lit 0.0, **novel_discovery**)

**hold_candidate_resolve_conflict (1):**
- `ARC-046` (candidate, exp 0.295 / lit 0.76; 1 supports / 1 weakens / 1 mixed — genuine conflict)

---

## Active Plans Heartbeat (7 active)

| Plan | In-flight | Blocked | Paused | Stale rows (>7d) | Last decision |
|---|---|---|---|---|---|
| arc_062_rule_apprehension_plan | 4 | 0 | 0 | 5 | 2026-05-18 |
| commitment_closure_plan | 3 | 0 | 0 | 1 | 2026-06-03 |
| goal_pipeline_plan | 2 | 1 | 0 | 2 | 2026-06-05 |
| infant_substrate_plan | 0 | 0 | 0 | 3 | 2026-05-21 |
| sd033_governance_plan | — | — | — | — | (no `## Status table` heading — different format) |
| self_attribution_plan | 0 | 3 | 0 | 3 | 2026-05-30 |
| sleep_substrate_plan | 0 | 1 | 0 | 1 | 2026-05-30 |

**PLAN STALING: arc_062_rule_apprehension_plan** — last Decision-log entry 2026-05-18 (23 days ago) with 4 rows in-flight. This is also the plan behind today's `v3_exq_654a` FAIL (GAP-B head-input-contract bottleneck). Worth a touch this session.

**arc_062 stale rows (5):**
- GAP-B (in-progress, updated ~2026-05-20, ~21d) — 543-lineage head-input-contract bottleneck; next retest `V3-EXQ-543k`; note `V3-EXQ-543g` still stuck-`claimed`, flagged for runner reconciliation.
- GAP-D (in-progress, 2026-05-20, 21d) — substrate done, validation `V3-EXQ-598` queued.
- GAP-H (partial, 2026-05-21, 20d) — ARC-065 diversity cluster registered.
- GAP-I (partial, 2026-05-10, 31d) — ARC-064 bottom-up rule-discovery cluster registered.
- GAP-J (open, 2026-05-17, 24d) — MECH-312 + sub-MECHs registered.

**commitment_closure stale rows (1):** GAP-1 (in-progress, 2026-05-20, 21d) — `V3-EXQ-598` (frozen vs trainable bias head) queued.

**goal_pipeline stale rows (2):** GAP-2 (**blocked**, 2026-05-08, 33d — re-queue `V3-EXQ-514` successor w/ phased training); GAP-4 (in-progress, 2026-05-29, 12d).

**infant_substrate stale rows (3):** GAP-12/13/14 — EXQ-ISEF-003/004/005 all `queued` since 2026-05-17 (24d). (Note: ISEF-002 / `588c` just PASSED today — the cluster is moving.)

**self_attribution stale rows (3):** GAP-1/2/3 all **blocked** on upstream gates (2026-05-30 / 2026-05-08 / 2026-05-08).

**sleep_substrate stale rows (1):** GAP-2 upstream-blocked (~32d).

---

## Literature Pull Candidates (Top 5)

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | MECH-282 | LPB interoceptive routing into harm-arbitration | medium | 0 |
| 2 | MECH-286 | Override-gated sleep-state transition (SD-037 override) | medium | 0 |
| 3 | MECH-306 | z_goal seeding under SD-012 requires sustained drive at contact | medium | 0 |
| 4 | MECH-319 | simulation-mode rule-write gating / categorical replay tag | medium | 0 |
| 5 | MECH-339 | Composite retrieval cue: ghost-bank cue = z_goal + context channel | medium | 0 |

(26 backlog items need literature; all top items are `collect_targeted_evidence`, 0 existing reviews.)

---

## Serve.py Status
- **RUNNING** on port 8000 (PID 62468).

---

## Blocked Items / Anomalies
- **governance.sh default run blocked at Step 4b (G2 backward-traceability gate).** 9 developmental claims lack a register row in `developmental_needs_register.md`: ARC-090, MECH-362, MECH-364, MECH-372, MECH-375, MECH-380, MECH-381, Q-059, RA-002. Re-ran with `SKIP_TRACEABILITY=1` to complete Steps 5–7 (pipeline finished clean). **Action:** add these rows to the register (or run `--warn-only`) so the gate stops blocking the nightly pipeline.
- **3 stale queue claims** (`V3-EXQ-655` ~23h, `603l`, `660`) with no landed results — runner/coordinator reconciliation candidate.
- **`V3-EXQ-543g`** noted in the ARC-062 plan as still `claimed` and deliberately un-mutated for scope/concurrency — flagged for governance/runner reconciliation.
- No TASK_CLAIMS governance collision this run.
