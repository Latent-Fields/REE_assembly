# Project Insights — 2026-07-10

Generated: 2026-07-10T16:34:12Z

> **Corpus caveat:** `runner_status.json` completed entries span **2026-02-26 → 2026-06-09**
> (840 runs). Since the Phase-3 cutover (2026-05-28/29), live results are written by the
> coordinator to per-run manifests, so `runner_status.json` is **no longer the live record**
> for June–July runs. Experiment-health numbers below are the historical Feb–Jun corpus;
> governance/substrate/backlog numbers are current-state.

---

## Experiment Health

- **Total runs (Feb–Jun corpus):** 840 — PASS: 283 | FAIL: 437 | ERROR: 87 | UNKNOWN: 32 | INCONCLUSIVE: 1
  - **Error rate: 10.8%** (87 / 807 terminal). FAIL rate 54% — high, but FAIL = "ran, criteria not met," the expected mode for a falsification-driven programme.
- **ERROR root-cause breakdown** (the actionable slice):
  - `exit code 1` (genuine code bug): **65**
  - `no sentinel / silent` (no PASS/FAIL emitted): **11**
  - `infra SIGTERM (-15/137)` (cloud-scaler shutdown-during-run): **9** — infra, not code; already mitigated by the runner `_transient_exit_codes` set
  - reentrant-IO: 1 · Windows FS permission: 1
- **High-iteration experiments** (3+ lettered iterations — repeated diagnose/rework cycles):
  - **EXQ-085 — 14 iters** (085, b–o) — claims: MECH-071 *(⚠ claim drifted mid-chain; last letters re-tagged SD-015/ARC-030 — do not attribute all 14 to MECH-071)*
  - **EXQ-418 — 13 iters** (418, a–l) — claims: SD-016, SD-017 (sleep/aggregation lineage)
  - **EXQ-514 — 13 iters** (514, a–l) — claims: SD-049 (Phase-2 behavioural validation ladder)
  - **EXQ-490 — 10 iters** — claims: MECH-269b, MECH-295, Q-040
  - **EXQ-543 — 10 iters** — claims: ARC-062, MECH-309
  - **EXQ-047 — 9 iters** — claims: MECH-095, SD-005
  - **EXQ-445 — 9 iters** — claims: *(none tagged)*
  - **EXQ-603 — 8 iters** — claims: Q-045 (harm-pathway / foraging-competence ecology)
  - EXQ-433 (7, SD-029) · EXQ-540 (7, MECH-307) · EXQ-074/076 (6, MECH-112/116/117) · EXQ-166 (6) · EXQ-325 (6) · EXQ-610 (6, INV-074)
- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - **MECH-112 — 4 ERRORs** (EXQ-074, 225a, 225b, 074d) — most error-prone claim in the corpus
  - **MECH-163 — 3 ERRORs** (237b, 237c, 495)
  - ARC-007 (2) · MECH-113 (2) · MECH-116 (2) · SD-003 (2) · SD-012 (2) · SD-018 (2) · MECH-188 (2) · INV-052 (2)

---

## Substrate Bottlenecks

Substrate queue: **106 items** (54 implemented/validated).

- **Ready & not-yet-implemented** (buildable now): **MECH-090** (P2 — BetaGate commit-entry readiness conjunction). *(The other 48 `ready:true` items are already implemented/validated.)*
- **Highest failure-record count** ≠ **the live front.** The raw ranking (below) is dominated by `f_dominance_conversion_ceiling` (26), ARC-062 (11), MECH-256 (10), SD-049-PHASE-2 (9), `v4_loop_segregation` (9), `modulatory-bias-selection-authority` (15, now `implemented`), ARC-065 (7), commitment-closure (7), SD-037 (6). But most of those records are **historical** — read the entry state before treating any as "the thing to go build." The actual state (from the substrate-queue notes + autopsies dated 2026-07-05→10) is in the next section.

### The live front is NOT "attack f_dominance" — it's a competence wall discovered 2026-07-08

The `f_dominance_conversion_ceiling` **selection face is substantially won and is not buildable work:**
- Both selection-face levers are **BUILT + VALIDATED + PROMOTED-provisional** — MECH-448 (rank-preserving F→eligibility demotion, V3-EXQ-689d PASS) and MECH-449 (Go/No-Go, V3-EXQ-689g PASS). The demotion envelope ~doubled committed diversity (0.938 vs 0.371) and **lifted the selection-face conversion ceiling on the GAP-A foraging substrate.**
- The parallel routes are exhausted, not open: the cross-loop **arbitration-reweighting** route is retired (709/711/713 all terminal FAIL, autopsy 2026-07-05); the conflict-graded-k / gap-scaled-commit-T parametric family is refuted (689a/689c); the rung-6/7 **de-commit-duration** face ran terminal (460h–460l, 715/715a/717) and is co-blocked on the same wall below.
- `ready:false` here means **"no buildable substrate item is owed,"** not "waiting for a build." The queue note is explicit: flipping it to ready would misread as work-to-pick-up.

**What actually blocks everything (719a, 2026-07-08 — first direct competence measurement of the integrated all-ON agent):** P2 foraging **0.065 / 0.0 / 0.455 resources/ep against a 1.0 floor — 0/3 seeds.** The reframe that collapses the whole bottleneck list: the recurring "substrate_not_ready" wall (654h / 485i / 625e / 460h / 460i, all self-routed) is **ONE competence root, not N independent sampling failures** — committed-action dissociation DVs are **undefined until the agent can competently forage at all.** The re-derive brake has fired (21st ARC-062 / 20th MECH-309); same-claim behavioural re-tests (722, 719b) are **refused.**

**724 (2026-07-09) localized it — and the answer is "diffuse":** an OFAT sweep over {P1 training budget, encoder freeze, mechanism count} + their combination — **every arm sub-floor (0.13–0.30 vs 1.0; oracle clears at 6.05).** The agent *acts* (commits to 5 classes at ~1.4 nats entropy) but forages ≈0 and is contaminated 7–11×/ep — **uniformly incompetent action, not frozen.** The autopsy's load-bearing insight: the deficit lives in the **one invariant 724 never varied** — policy is learned only through a thin **bias-head REINFORCE over prediction-trained representations** (e2 world-forward contrastive). REE is **prediction-rich, action-poor**: a substantial world model, but action learned as a bias term. No first-class policy-learning substrate exists (dorsal-striatal actor-critic analog is un-instantiated).

**The sequential chain (719a→724→732→732a) bottomed out on the same floor 4× and was replaced by a parallel portfolio (WS-14 / GOV-FANOUT-1, 2026-07-10).** The 732/732a discriminators inherited an **observability confound** — the learner-adequacy gate referenced a *privileged-global* teleport oracle (57.2 res/ep) while the agent sees only a 5×5 local view, making the threshold structurally unreachable and leaving H1 vs H2 unresolved. Fix landed: `LocalViewGreedyPolicy` (a 5×5-window-only ceiling anchor) added to `capability_eval.py`; the global oracle demoted to floor-achievability control. The three-axis portfolio replacing the chain: **P-A `V3-EXQ-737`** (trainable PPO/A2C policy head on REE's frozen `z_world` latent — the H1 representation test), **P-B `V3-EXQ-738`** (local-view ceiling anchor — the measurement/H2 test), **P-C V3-EXQ-739** (observation-encoder probe, held to reserve).

**Current state (2026-07-10): H2 refuted, H1 is the surviving hypothesis.** P-B (`V3-EXQ-738`, ran 15:16Z) **refuted H2** — the 1.0 floor *is* reachable from the 5×5 local view, so the observation interface is not the wall and P-C is de-valued to reserve. That leaves **H1** — REE's action-generation stack (bias-head-only policy over prediction-only reps) is the bottleneck. The live gate is **`V3-EXQ-737`** (queued, awaiting the fleet): if a real trainable policy head on REE's own frozen latent forages where the bias-head stack cannot, the owed build is a **first-class action-learning substrate** (dorsal-striatal actor-critic analog) under `f_dominance_conversion_ceiling`. The dorsal-striatal / actor-critic literature that build needs is un-pulled (724 §4) and is being pulled now as a forward de-risk.

---

## Governance State

- **Claims pending V3 substrate (`v3_pending: true`): 221** (of 877 claims; `implementation_phase: v3` on 311). This is the structural backlog — the bulk of the registry is waiting on V3 substrate before any evidence can move it.
- **Pending promotion/demotion decisions: 1** (`Q-080`, `narrow_open_question`, `pending_user`). All other 102 recommendations are `applied` — governance board is otherwise clean.
- **Evidence superseded / reworked:** **100 manifests** carry a `superseded` marker (rework from lettered re-runs; correctly excluded from claim confidence by the indexer).

---

## Literature Coverage

- **Backlog note:** `evidence_backlog.v1.json` tracks **365 experimental / 1 literature** item — literature is *not* tracked there. Actual literature lives in `evidence/literature/` as **376 `targeted_review_*` dossiers**, indexed in `INDEX.md`.
- **No priority-1 literature gaps open** in the backlog (all P1 items are in_progress or covered; the 148 `open` items are all medium-priority experimental, not literature).
- **Recent lit-pull targets** (from WORKSPACE_STATE, last ~4 weeks): RHM6 relational-harm/love, DRV3 drive-arbitration, **Q-019 three-gate basal-ganglia** (DLS habit lesion / MD thalamus / VLS territory — landed 2026-07-10). Literature pulls are running low-friction and headless.

---

## Human-Intervention Patterns

Derived from WORKSPACE_STATE session labels (last ~30 sessions) and the error corpus:

- **Recurrently needs human input:**
  - **Substrate implementation** (`implement-substrate-*`) — every instance pauses for plan/scope confirmation before building (MECH-449, scaffolded_sd054). Highest-touch task type.
  - **Governance disposition** (`govdecision-*`, `governance-cycle-*`) — interactive by design; pauses before applying promote/demote decisions.
  - **Failure autopsy** (`failure-autopsy-445h`, 732a) — claim-attribution and "is this substrate-not-ready vs a real fault" calls repeatedly need a judgement pass (the EXQ-085 / EXQ-654 claim-drift traps are the canonical reason).
- **Low-friction / headless-safe** (completed without intervention across multiple recent sessions):
  - **lit-pull** — 3/3 recent runs clean (RHM6, DRV3, Q-019).
  - **nightly /update-docs** — scheduled, bot-identity commits, no intervention.
  - **igw-ledger / phase-tag hygiene** (arc034, gapk) — mechanical, "PROMOTES NOTHING" closes.
  - **queue-experiment** — runs through the skill's smoke-test gate without dispute.

---

## The live campaign — and why the next step is neither obvious nor easy

The most important thing on the board is the competence-localization portfolio (`conversion_ceiling_campaign:CAMPAIGN` / WS-14). Every track is `experiment_purpose=diagnostic`, `claim_ids=[]`, `non_contributory`, **brake-exempt**, promotes nothing:

| Queue | Axis it isolates | State (2026-07-10) |
|---|---|---|
| **V3-EXQ-737** (P-A) | **policy mechanism on REE's own representation** — trainable PPO/A2C head on REE's frozen `z_world` latent | **LIVE H1 GATE — queued, awaiting fleet.** Forages where the bias-head stack cannot ⇒ H1 confirmed. |
| V3-EXQ-738 (P-B) | **measurement / observation** — local-view-achievable ceiling anchor | **RAN 15:16Z — refuted H2.** 1.0 floor *is* reachable from the 5×5 local view. |
| V3-EXQ-739 (P-C) | observation-encoder probe | **Reserve** — de-valued once P-B refuted H2. |
| V3-EXQ-734/735/736 | env difficulty / drive-balance / curriculum | Secondary recovery axes, still queued (lower prio). |

**The genuinely hard part** — why there is no obvious next move, exactly as you said:

1. **The obvious build stays refused until H1 is *confirmed*, not merely un-refuted.** With H2 now refuted (738), the surviving hypothesis is H1 = REE's action-generation stack is the bottleneck. But "H2 is false" ≠ "H1 is true" — 737 has to actually show a real policy head on REE's own latent forages before committing to a first-class action-learning substrate build. The whole point of the WS-14 portfolio was to *avoid* building the wrong substrate on a laundered artifact.
2. **You cannot just re-run behavioural falsifiers** — the re-derive brake has fired (21st ARC-062 / 20th MECH-309); 722 and 719b are refused, and their DVs are undefined without competence anyway.
3. **The deficit is diffuse** — 724 varied three factors *and their combination* and none recovered. There is no single knob; the parsimonious reading points at the *un-varied* constant (bias-head-only REINFORCE), which is an **architectural translation gap** (prediction-rich, action-poor), not a tunable — plausibly a V-generation-scale build gated behind confirming H1.
4. **The measurement instrument had to be repaired mid-diagnosis.** The 732/732a discriminators were **observability-confounded** (global teleport oracle vs 5×5-local-view learner), which is *why* the sequential chain bottomed out 4× — each pass paid down power/instrumentation without moving the question. Fixed now (`LocalViewGreedyPolicy` anchor), but it means four diagnostics were partly spent laundering the yardstick rather than answering the science.

## Recommendations

1. **The next real answer is gated on the fleet running `V3-EXQ-737`** — it's queued; there is no session-level action that advances it, only running the runner. This is the live H1 gate and the only thing that unlocks (or rules out) a non-wasted action-learning build. Everything else here is preparation for its outcome.
2. **De-risk the likely H1 build now (in flight):** if 737 confirms H1, the owed build is a **first-class action-learning substrate** (dorsal-striatal actor-critic analog) under `f_dominance_conversion_ceiling` — a real architectural addition, not a lever. The dorsal-striatal / actor-critic literature it needs is un-pulled (724 §4); that lit-pull is now running as a spawned session (`task_12291f81`). This is the one genuinely actionable, non-blocked forward task.
3. **Already handled — do not re-do:** the competence-yardstick fix (`LocalViewGreedyPolicy` in `capability_eval.py`) is landed; the H2 test (738) has run and refuted; MECH-090 substrate is landed-and-subsumed. None of these is open work.
4. **Lower-tier, genuinely buildable now:** **MECH-090** (BetaGate commit-entry readiness conjunction) is the *only* ready-and-unimplemented SD (P2, 0.72 in the promotion table) — independent of the competence wall, no dependency wait.
5. **Governance is clean** — only Q-080 pending. No action beyond the user's open-question narrowing call.

> **Correction vs a naive read of the failure-record ranking:** "attack f_dominance" / "queue the GAP-B falsifier" is stale — that face is built, validated, and lifted on GAP-A, and the brake refuses more falsifiers. The real work is upstream (competence) and its next step is a *diagnostic to decide what to build*, not a build.
