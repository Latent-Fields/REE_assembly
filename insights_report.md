# Project Insights — 2026-06-09

Generated: 2026-06-09T22:23:22Z

---

## Experiment Health

- **Total runs:** 840 (PASS: 283 | FAIL: 437 | ERROR: 87 | UNKNOWN: 32 | INCONCLUSIVE: 1 | error rate: 10.4%)
  - PASS rate among ran-to-completion (PASS+FAIL): 39.3%. The high FAIL count is expected for a falsification-driven programme, not a defect signal.

- **High-iteration experiments** (3+ total iterations across queue + completed). Per the skill caveat, letter count ≠ single-claim attribution — claim_ids drift across letters, so the chains below are annotated with their actual claim history:
  - **EXQ-085 — 14 iterations** (085, b, c, e–o) — claim drift: started untagged → 085c tagged **MECH-071** → later letters dropped the tag (goal-navigation FAILs, not harm-calibration). All 14 FAIL. Per the canonical 085 trap, the corrected hypothesis migrated to **SD-015 → the 622/626 ladder** under fresh numbers — **not** a dead MECH-071 chain. Verify before shelving.
  - **EXQ-514 — 13 iterations** — **SD-049**. Mixed: 514g/h/i PASS, then 514j/k/l FAIL. Non-monotonic; the later FAILs likely test a different criterion than the PASS trio. Check `evidence_direction_per_claim` before treating j/k/l as evidence against SD-049.
  - **EXQ-418 — 13 iterations** — claim drift **SD-017 → SD-016 → SD-017**. 418f PASS (SD-016), surrounded by FAIL/ERROR/UNKNOWN. Latest 418l (SD-017) FAIL with **no same-base successor queued** (sleep substrate — see Stalled chains).
  - **EXQ-543 — 10 iterations** — **MECH-309** (543 PASS) then **ARC-062** leg (543c–k, all FAIL). MECH-309 leg has an active successor (**V3-EXQ-654a** in queue); the ARC-062 leg is held_pending_v3_substrate.
  - **EXQ-490 — 10 iterations** — claim drift MECH-269b → Q-040 → **MECH-295**. Resolved: 490k PASS (MECH-295). Q-040 cohort was contaminated/superseded 2026-05-07; live successor PASSed. **Not stalled.**
  - **EXQ-603 — 8 iterations** — Q-045 → untagged. 603j PASS; active successor **V3-EXQ-603l (SD-059)** in queue. Healthy.
  - **EXQ-610 — 6 iterations** — **INV-074** (crystallization-necessity). 610/610a ERROR → 610b–f FAIL. Active successor **V3-EXQ-655 (INV-074)** in queue. Iterating, not stalled.
  - Other 5+ chains: EXQ-445 (9), EXQ-047 (9), EXQ-540 (7), EXQ-433 (7, non_contributory — SD-029 monomodal-collapse), EXQ-020 (7), EXQ-002 (7), EXQ-325 (6), EXQ-166 (6), EXQ-076 (6), EXQ-074 (6).

- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - **UNTAGGED — 39 ERROR entries.** Dominant error class by a wide margin: crashes on queue items declaring neither `claim_id` nor `claim_ids`. This is exactly the class the 2026-06-06 rec-4a `validate_queue.py` WARN now flags (non-blocking). The WARN catches future cases; the 39 are historical residue.
  - **MECH-112 — 4 ERROR** (most-failing tagged claim).
  - **MECH-163 — 3 ERROR.**
  - **2 ERROR each:** SD-018, SD-012, SD-003, MECH-188, MECH-116, MECH-113, INV-052, ARC-007.

- **Stalled chains** (latest letter FAIL, no same-base successor queued, no obvious migration):
  - **EXQ-418l — SD-017 (sleep) — FAIL — no successor queued.** Sleep substrate work; the SD-016 leg PASSed (418f) but the SD-017 question stalled. Cross-check `sleep_substrate_plan.md` status table before re-queueing.
  - **EXQ-514l — SD-049 — FAIL — no successor queued.** Non-monotonic chain (PASS trio precedes the FAIL trio); confirm whether the FAILing criterion maps to SD-049 or a co-tested claim before calling it stalled.
  - EXQ-543k (ARC-062 leg) — FAIL, no successor on the ARC-062 leg specifically, but ARC-062 is correctly held_pending_v3_substrate, so this is a deliberate hold, not a stall.

---

## Substrate Bottlenecks

`substrate_queue.json`: 98 entries. 52 `implemented`, plus many `*_implemented` variants (phase_1/phase_2, validated, landed). No entry carries the bare `ready` status — the actionable not-yet-built work sits in these statuses:

- **`pending_implementation` (2 — these are the closest to "ready to build"):**
  1. **Bound multi-stream representation substrate** — world_states↔states carry co-varying binding info so cross-stream coherence C(τ) is non-reducible. *Off the V3 critical path — V4-leaning per the object-representation thread; type-vs-token fork is the first decision.*
  2. **Relief/safety escape-affordance bridge** — affordance-indexed avoidance credit + threat-gated E3 approach (wires MECH-302/303/304 into instrumental avoidance). **Most plausibly V3-buildable now.**
- **`proposed` (1):** MECH-269 Phase-2 T2 forward-predictor V_s routing (per-stream verisimilitude).
- **`design_question` (1):** MECH-314a Phase-2 novelty-source selection — architecture doc recommends Candidate 5A (rolling z_world buffer + first-action onehot); insertion deferred to a `/implement-substrate` session post user assent. **Note:** V3-EXQ-648 autopsy (2026-06-07) already flagged MECH-314a-Phase-2-impl as `validation_failed_pending_redesign` (curiosity bias zero-RANGE; novelty fed from collapsed proposer trace rather than e2.world_forward).
- **`candidate_v3_pending` (9):** includes serotonergic-REM precision setpoint, single-pass self-attribution comparator, E2_x dual-function substrate, harm-as-precision-weighted-PE (SD-020 upgrade), shared HarmForwardTrunk (competes with ARC-033), ARC-064 bottom-up rule-extraction + children, SD-029 reef substrate.

- **SDs with failure records** (experiments failed citing the missing/incomplete substrate): ~20 entries carry `failure_record`, several with 3–6 failures. The heaviest:
  - One entry with **6 failures** (`implemented`).
  - One **`parked_pending_env_entropy_precondition`** with **5 failures** — env-entropy precondition is a recurring blocker.
  - One **phase_1_implemented** with **4 failures**.
  - The **scaffolded_sd054_onboarding / Stage-H curriculum** entry (`curriculum_decomposition_IMPLEMENTED_2026_06_07`) gates GAP-2: `ready` stays false until V3-EXQ-603g clears G1≥2/3 ∧ G2≥2/3 ∧ ecological G3≥2/3. This is the single largest live substrate gate, blocking V3-EXQ-603f.

---

## Governance State

- **Claims pending V3 substrate (`v3_pending: true`):** 138 occurrences in claims.yaml (732 total `id:` lines in registry).
- **Pending promotion/demotion decisions** (`decision_status` in promotion_demotion_recommendations.md, generated 2026-06-09T21:08Z):
  - 412 `applied` | 86 `deferred` | **17 `pending_user`** ← the live human-decision queue.
  - `pending_user` rows include: ARC-046, ARC-072, MECH-121, MECH-346, MECH-347, SD-055, SD-057 (+10 more).
- **Evidence superseded (rework):** 36 manifests carry `evidence_direction: "superseded"`. These are correctly excluded from claim confidence/conflict ratios by the indexer.

---

## Literature Coverage

- **Priority-1 (high) backlog items still open: NONE.** No high-priority literature gap is currently unaddressed.
- **Total open literature items: 17** (2 `medium` — **MECH-306**, **Q-054**; 15 `low` — Q-055 through Q-069, a low-priority Q-claim sweep). Plus 8 `in_progress`, 1 `covered`.
- **Recently covered / in-flight (from WORKSPACE_STATE tail):** ARC-066 tonic-vigor, ARC-067 boredom, ARC-068 opportunity-cost (Niv 2007 — verdict: MECH-320 w_passive IS the ARC-068 implementation), ARC-070/071 decomposition/composition, INV-044/MECH-166/ARC-045 (9 entries), SD-003 (4 entries), contextual-memory-allocation-gate (slug claimed, verdict pending — gating the MECH-261 amend decision).

---

## Human-Intervention Patterns

Derived from WORKSPACE_STATE session history + error analysis:

- **Tasks that recurrently required human input:**
  - **Substrate implementation** — every `/implement-substrate` session pauses for user assent before insertion (MECH-314a Phase-2 explicitly "deferred to a session post user assent"; scaffolded_sd054 readiness gate held). Architectural-commitment substrates do not auto-proceed.
  - **Claim registration from thought-intake** — repeated user correction (twice on 2026-06-09 per memory) that intake must *register* candidate claims into claims.yaml in the same pass, not leave "future-registration" prose. High-friction, judgement-heavy.
  - **Governance fold-vs-separate / amend-vs-new-child decisions** — memory-allocation-gate disposition (2026-06-06) explicitly STOPped for user sign-off; B+D gated behind a lit verdict + a user decision.
  - **IGW auto-spawn** required a fix (2026-06-04 respawn-loop) — autonomous spawning had a 4-link loop; now cooldown-gated and launchd left disabled per user request.
- **Low-friction headless tasks:**
  - **lit-pull** — runs delegated/autonomous repeatedly without issue ("delegated autonomous, user at work: 9 entries, all on origin/master"; a 51-entry Q-claim sweep). The biology-before-formal-definitions gate is well-internalised.
  - **queue-experiment** — V3-EXQ-659/660/661 queued cleanly through the skill (smoke + validate + coordinator ingest) without intervention.
  - **insights / morning-digest / governance.sh** — read-only or scripted, run headless.

---

## Recommendations

1. **Resolve the 17 `pending_user` promotion/demotion decisions** — this is the live human-decision queue and the highest-leverage governance action. Prioritise ARC-046 and ARC-072 (conflict-resolution / substrate holds) and the SD-055/SD-057 pair (recently landed substrate, ripe for adjudication).

2. **Build the relief/safety escape-affordance bridge** (`pending_implementation`) — the most plausibly V3-buildable of the un-built substrates (wires existing MECH-302/303/304 into instrumental avoidance; not V4-deferred like the bound-multi-stream entry). Run it through `/implement-substrate` with the standard pre-insertion user assent pause.

3. **Close the MECH-314a Phase-2 redesign loop before re-queueing** — the design_question is already `validation_failed_pending_redesign` (V3-EXQ-648 autopsy: novelty must be fed from `e2.world_forward`, not the collapsed proposer trace). Apply the amend + correct the precondition, then `/queue-experiment V3-EXQ-648a`.

4. **Audit the two stalled FAIL chains against their plan-of-record before abandoning:** EXQ-418l (SD-017 sleep) against `sleep_substrate_plan.md`, and EXQ-514l (SD-049) per-criterion — confirm whether the FAILing criterion maps to the tagged claim or a co-tested one. Neither has a queued successor; both risk silent abandonment.

5. **Literature is healthy — no priority-1 gaps.** Only optional cleanup: the 2 `medium` open items (MECH-306, Q-054). The 15 `low` Q-claim items (Q-055–Q-069) are deferrable. No new lit-pull is warranted on priority grounds.
