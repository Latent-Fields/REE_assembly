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

The single most important thing on the board is the **post-724 competence-recovery campaign** (`conversion_ceiling_campaign:CAMPAIGN`), currently the queue's top priorities. It is a **multi-track diagnostic fan-out** trying to localize the diffuse competence deficit along orthogonal axes — every track is `experiment_purpose=diagnostic`, `claim_ids=[]`, `non_contributory`, **brake-exempt**, promotes nothing:

| Queue | prio | Axis it isolates | Crux |
|---|---|---|---|
| **V3-EXQ-737** (Track-1d) | **155 (lead)** | **policy mechanism on REE's own representation** | The direct H1 test 724 prescribed: bolt a real trainable **PPO actor-critic onto REE's frozen `z_world` latent** and ask whether it forages where the bias-head stack cannot. |
| V3-EXQ-734 (Track-1a) | 150 | **env difficulty** + learner-adequacy | Holds the 724-A0 recipe fixed, steps env difficulty D0→D3; folds in the 732a **vanilla-PPO-on-identical-obs** control. |
| V3-EXQ-735 (Track-1b) | 42 | **drive/reward balance** | Is the 728 forage-vs-survive inversion an approach-vs-avoid weighting failure vs an architecture failure? |
| V3-EXQ-736 (Track-1c) | 40 | **curriculum / transfer** | Two-stage easy→hard training; does competence transfer? |

**The genuinely hard part** — why there is no obvious next move, exactly as you said:

1. **The obvious build is explicitly refused until H1 vs H2 resolves.** H1 = REE's action-generation stack is the bottleneck (a real policy head recovers competence → build a first-class action-learning substrate). H2 = the observation/env interface is unlearnable by *any* policy at this scale (the oracle only wins on *privileged* nearest-resource access the agent's observation may not afford → the target is the *encoding*, not the policy — a policy build would be wasted). 724 cannot distinguish them (no learned non-REE control, never varied the policy mechanism). User judgment at the gate: *"H2 is cheap to rule out and expensive to skip"* → queue the discriminator (737/734) **before** committing to any build.
2. **You cannot just re-run behavioural falsifiers** — the re-derive brake has fired (21st ARC-062 / 20th MECH-309); 722 and 719b are refused, and their DVs are undefined without competence anyway.
3. **The deficit is diffuse** — 724 varied three factors *and their combination* and none recovered. There is no single knob; the parsimonious reading points at the *un-varied* constant (bias-head-only REINFORCE), which is an **architectural translation gap** (prediction-rich, action-poor), not a tunable — plausibly a V-generation-scale build gated behind confirming H1.
4. **Even the competence yardstick is confounded.** The WS-1 competence floor (V3-EXQ-732a) came back **observability-confounded** — a global-oracle ceiling vs a 5×5 local-view learner — 732a terminal, 732b refused, `capability_eval.py` needs a local-view ceiling anchor. That is precisely why 734 folds a vanilla-PPO learner-adequacy control onto the *same observation interface*: the measurement instrument is under repair at the same time as the thing it measures.

## Recommendations

1. **Run the H1/H2 discriminator first — V3-EXQ-737 (lead) and V3-EXQ-734.** This is the campaign's own decided next step and the only thing that unlocks a non-wasted build. 737 (PPO on REE's frozen `z_world`) + 734 (env-difficulty staircase + vanilla-PPO on raw obs) together separate "REE's *representation* can't support foraging" from "REE's *action stack* can't exploit a fine representation" from "the *env* is unlearnable." Don't propose any competence-substrate build until these score.
2. **Anticipate the likely H1 outcome without pre-committing to it:** if 737/734 point at H1, the owed build is a **first-class policy/action-learning substrate** (a dorsal-striatal actor-critic analog) under `f_dominance_conversion_ceiling` — a real architectural addition, not a lever. Worth pulling the motor-learning / actor-critic literature now (724 §4 flags it un-pulled) so the build isn't lit-blind when the gate opens.
3. **Fix the competence yardstick in parallel** — `capability_eval.py` needs the local-view ceiling anchor the 732a confound exposed, else every competence DV in this campaign inherits the global-vs-local-oracle confound. This is low-risk instrument work that de-risks tracks 734–737.
4. **Lower-tier, genuinely buildable now:** **MECH-090** (BetaGate commit-entry readiness conjunction) is the *only* ready-and-unimplemented SD (P2, 0.72 in the promotion table) — independent of the competence wall, no dependency wait.
5. **Governance is clean** — only Q-080 pending. No action beyond the user's open-question narrowing call.

> **Correction vs a naive read of the failure-record ranking:** "attack f_dominance" / "queue the GAP-B falsifier" is stale — that face is built, validated, and lifted on GAP-A, and the brake refuses more falsifiers. The real work is upstream (competence) and its next step is a *diagnostic to decide what to build*, not a build.
