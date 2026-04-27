---
nav_exclude: true
---

# MECH-163 VTA / Planned-System -- V3 Full-Completion Gate Session Prompt

**Created:** 2026-04-26
**Purpose:** Structured starting point for the session that will design and write the
experiment that *cleanly* validates the VTA/hippocampally-planned arm of MECH-163. This
is the **V3 full-completion gate**, distinct from EXQ-327 (which cleared the
first-paper / habit-system gate) and distinct from the EXQ-483 / SD-037 family
(broadcast-override substrate, unrelated mechanism).

This document does NOT design the experiment. It assembles what must be settled
before the experiment can be written, and flags the reconciliation work that should
land first.

---

## Why this is its own program

MECH-163 asserts two parallel goal-directed systems:

- **Habit (SNc / dorsal-striatum / model-free):** sufficient for approach in
  familiar contexts via cached benefit/harm evaluation on value-flat
  HippocampalModule proposals (ARC-007 strict).
- **VTA / hippocampally-planned (VTA / accumbens + PFC / model-based):** required
  for novel contexts, long-horizon benefit accumulation, and prosocial planning.
  z_goal gradient shapes which trajectories HippocampalModule *proposes*; E3
  evaluates multi-step rollouts rather than post-hoc scoring random candidates.

EXQ-327 demonstrated that the **habit arm** carries the V3 first-paper gate:
benefit_ratio >= 1.3x with `goal_weight > 0.0` in E3 trajectory scoring. The
HippocampalModule there generates value-flat candidates and z_goal enters only
through scoring -- proposal generation is goal-blind. That is the habit
architecture by MECH-163's own definition.

The full-completion gate requires showing the **planned arm** does work the
habit arm cannot:

> A scenario where 1-step / habit-policy approach is *insufficient*, and where
> goal-seeded multi-step trajectory generation by HippocampalModule produces
> a discriminable behavioural advantage.

Without this, V4 social extension (INV-029 multi-agent benefit gradient over
trajectories, MECH-164 agent-indexed terrain inference) has no validated
planning substrate.

---

## What to read at session start

Before designing, read in order:

1. **`REE_assembly/docs/claims/claims.yaml`** -- MECH-163 entry (line ~10623),
   especially `evidence_quality_note`. EXQ-237a was redesign-flagged
   2026-04-06 for "task paradigm + substrate"; EXQ-327 cleared the habit arm
   on 2026-04-14. The note has not been updated since either event.

2. **`REE_assembly/docs/architecture/v3_v4_transition_boundary.md`** -- the
   "HippocampalModule multi-step planning" row (line 62) is still marked
   *TBD -- goal-seeded trajectory generation*. The row, the V4 social-extension
   dependency paragraph (lines 101-114), and the two-tier completion structure
   in `roadmap.md` lines 1202-1223.

3. **`ree-v3/experiments/v3_exq_327_mech163_goal_conditioned_nav.py`** --
   how the habit arm was operationalised (z_goal in scoring only; phased
   training; GOAL_CONDITIONED vs GOAL_ABLATED ablation pair). The new
   experiment is the natural extension: a third condition where z_goal enters
   *proposal generation*, not just scoring.

4. **`ree-v3/ree_core/hippocampal/`** -- HippocampalModule trajectory
   candidate generation. Where does CEM seed candidates? Is there a hook for
   z_goal-conditioned proposal sampling? If not, what's the smallest
   substrate change required?

5. **`REE_assembly/docs/architecture/sd015_hippocampal_nav_session_prompt.md`**
   -- the format and design discipline used for the first-paper gate. This
   document mirrors that one.

---

## Reconciliation work that should land first

Two items should be cleared *before* the experiment is written, otherwise the
governance record will mis-credit the result.

### R1. EXQ-327 manifest tagging
[claim_evidence.v1.json](../../evidence/experiments/claim_evidence.v1.json)
records EXQ-327 as the only experimental entry for MECH-163, direction
*weakens*, with `pass_runs: 0, fail_runs: 1`. The roadmap and the
goal_wanting_signal_chain doc both call it a PASS. Either:

- the run-pack manifest needs `evidence_direction: supports` with an
  `evidence_direction_note`, or
- the claim_id list on EXQ-327 should not include MECH-163 at all
  (since the habit arm is one half of the dual system; tagging MECH-163
  conflates the dual-system claim with its habit-arm component).

The cleanest fix is the second: EXQ-327 is the SD-015 / habit-arm gate, and
MECH-163 should accumulate its experimental evidence only from experiments
that test the **dual-system distinction** -- i.e., the planned arm doing
work the habit arm cannot. Drop MECH-163 from EXQ-327's claim_ids; reindex.

### R2. claims.yaml evidence_quality_note refresh
The current note still says `needs_redesign (task paradigm + substrate)`. Once
R1 lands, rewrite it to:

- record EXQ-237a as superseded (task-paradigm flaw),
- record EXQ-327 as covering the habit arm only,
- name the V3 full-completion gate as the still-pending discriminative test,
- list the substrate prerequisites that are already in place (HippocampalModule,
  z_goal seeding via SD-012/SD-015, ARC-030 D1/D2 competition, SD-039 anchor
  payload now landed) so it is clear this is a writing task, not a substrate
  task.

---

## Design questions to resolve in the session

### Q1: What scenario discriminates planned from habit?

Candidate paradigms (only one needed):

- **A. Detour/blockage:** familiar grid where the habit-cached short path
  becomes blocked mid-episode. Habit must re-explore; planned generates a
  novel multi-step detour seeded by z_goal. Predicts planned-arm
  benefit_ratio advantage **only** in blockage episodes.
- **B. Novel-context generalisation:** train in env A, test in
  topologically-novel env B with same resource semantics. Habit-arm
  benefit_ratio degrades (no cached S-R for B); planned-arm preserved
  because z_goal seeding is tied to resource semantics, not states.
- **C. Long-horizon benefit accumulation:** multi-resource episodes where
  optimal benefit requires sequencing visits beyond a single CEM
  horizon (rollout_horizon=30 from E2Config). Habit cannot plan
  multi-resource ordering; planned can.
- **D. Decoy / value-flat trap:** environment containing a habit-cached
  high-frequency low-benefit resource alongside a low-frequency
  high-benefit resource. Habit overfits to the cached one; planned, with
  z_goal seeded by current drive state, picks the higher-benefit option.

Paradigm B aligns most directly with MECH-163's biological grounding
(model-based control beats model-free in novel contexts; Daw et al. 2005,
already in MECH-163's lit support). Paradigm A is the cleanest within-episode
ablation. Paradigm C is the most ambitious but couples the test to E2
horizon limits, which is a separate research question. Paradigm D requires
the wanting/liking SD-015 substrate to be doing useful work, so couples
gate completion to MECH-229/230 evidence quality.

**Recommendation for the session:** start from A (detour) as primary; reserve
B (novel context) as a stretch follow-up if A passes. Both are within current
substrate.

### Q2: What's the proposal-generation hook?

Currently HippocampalModule CEM is value-flat. The minimal substrate change
for the planned arm:

- **Option 1:** weight initial CEM action distribution by z_goal-conditioned
  prior (additive log-prior on actions whose predicted next-state has
  higher cosine sim to z_goal).
- **Option 2:** seed initial CEM candidate trajectories from anchors whose
  goal_payload (SD-039) cosine-matches current z_goal -- treat anchors as
  habit-like memory of goal-relevant routes, with z_goal-current as the
  selector. This couples the gate to SD-039 and is the more biologically
  faithful instantiation (hippocampal place-cell-driven proposal vs
  cortical re-planning).
- **Option 3:** pure rejection sampling -- generate CEM candidates as today;
  reject and resample those whose final state has low z_goal proximity.

Option 2 is the right long-term answer (SD-039 was designed for exactly this
consumer), but the session should decide whether to wait for MECH-292/293
(SD-039 consumers) to land before running the gate, or to use Option 1 as a
faster minimal-substrate path and treat the SD-039 version as a stronger
follow-up.

### Q3: Acceptance criteria

A clean V3 full-completion-gate PASS requires:

- **C1:** Three conditions: HABIT (no goal in proposal generation,
  goal-weight in scoring -- the EXQ-327 setup), PLANNED (goal in proposal
  generation as decided in Q2), ABLATED (no goal anywhere).
- **C2:** PLANNED benefit_ratio strictly > HABIT benefit_ratio in the
  discriminative scenario (Q1) at >= 4/7 seeds. The size of the gap is the
  V3 full-completion-gate metric; pre-register it (suggested: >= 0.3
  benefit_ratio gap).
- **C3:** HABIT >= ABLATED in standard episodes (recovers EXQ-327's
  result -- if not, we have a regression in the habit arm and the gate is
  not interpretable).
- **C4:** PLANNED prox_r2 >= 0.7 (representation still intact across the
  added proposal-time goal coupling).
- **C5:** No catastrophic harm regression -- harm_ratio in PLANNED within
  10% of HABIT. The planned arm must not buy goal-approach by ignoring
  z_harm_a.

### Q4: Claim IDs

Per the `claim_ids` accuracy rule, what does the experiment *directly* test?

- **MECH-163** -- primary; the dual-system distinction.
- **SD-039** -- only if Option 2 is taken in Q2 (anchor-payload-driven
  proposal seeding); otherwise omit.
- **ARC-030** -- only if Q1 includes a paradigm that exercises
  approach/avoidance competition; otherwise omit.

Default: MECH-163 alone, unless a specific design decision pulls in SD-039.

---

## Constraints

- `CausalGridWorldV2` (10x10, `use_proxy_fields=True`) by default.
- SD-012 `drive_weight=2.0`, SD-015 wiring, ARC-030 already in default config.
- Phased training MANDATORY (P0 encoder warmup -> P1 frozen-encoder downstream
  training -> P2 evaluation).
- Smoke test (`--dry-run`) before queueing.
- Machine affinity: `any` unless Q2-Option-2 pulls in SD-039 substrate that
  has a hardware reason to pin (it does not, currently).
- EXQ number: at the time of writing, the queue's highest is V3-EXQ-493 and
  V3-EXQ-494 is reserved for SD-039 anchor-payload validation. The
  full-completion gate experiment should claim the next free number after
  those land (likely V3-EXQ-495 or higher); recheck `experiment_queue.json`
  and recent `runs/` directories at script-write time.

---

## What this prompt does NOT decide

- Which paradigm (Q1 A/B/C/D) -- session decides.
- Which proposal-generation hook (Q2 1/2/3) -- session decides; the choice
  determines whether the gate runs in the next sprint or is deferred until
  SD-039 consumers land.
- Whether multiple variants (e.g., A first then C) should be queued in
  sequence or in parallel.

---

## Expected outcome

If the full-completion gate **PASSES**: V3 has both a working habit arm
(EXQ-327) and a working planned arm (this experiment). MECH-163 is
discriminatively supported, V3 full completion is achieved, and V4 social
extension (MECH-164, INV-029 multi-agent benefit gradient) can be designed
on a validated planning substrate.

If the gate **FAILS**: diagnose the failure mode --
(a) z_goal proposal seeding doesn't produce different candidates from
value-flat (instrumentation problem -- check the proposal distribution);
(b) candidates differ but E3 scoring washes the difference out (interaction
between goal_weight in scoring and goal-seeding in proposals; consider
removing the scoring-side goal term in the PLANNED condition);
(c) chosen paradigm doesn't actually require multi-step planning (revisit
Q1 -- the habit arm should *fail* the discriminative scenario, otherwise the
test is uninformative).

Each failure mode has a targeted next experiment; none is fatal to the
overall MECH-163 program.

---

## Related claims and documents

- `MECH-163` -- dual goal-directed systems
- `MECH-164` -- agent-indexed terrain inference (V4, depends on MECH-163 gate)
- `SD-015` -- goal representation seeding (cleared by EXQ-327)
- `SD-012` -- homeostatic drive (substrate, in place)
- `SD-039` -- anchor goal-snapshot payload (substrate landed 2026-04-26;
  consumers MECH-292/293 still candidate)
- `ARC-007` -- value-flat HippocampalModule (the habit-arm constraint)
- `ARC-021` -- three BG learning loops (architectural context)
- `ARC-030` -- D1/D2 approach/avoidance competition

Reference documents:
- `REE_assembly/docs/architecture/v3_v4_transition_boundary.md` (line 62 row)
- `REE_assembly/docs/roadmap.md` (lines 1202-1223 two-tier completion)
- `REE_assembly/docs/architecture/sd015_hippocampal_nav_session_prompt.md`
  (analogous structure)
- `REE_assembly/evidence/planning/governance_meta_illusory_conflict_resolution.md`
  (EXQ-237a redesign rationale)
