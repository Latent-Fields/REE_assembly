---
title: "MECH-189: Super-Ordinal Goal-Anchor ContextMemory Writes Substrate"
parent: "Memory & Hippocampus"
grandparent: Architecture
nav_order: 10
status: candidate
status_asof: 2026-07-10
status_claim: MECH-189
---

# MECH-189: Super-Ordinal Goal-Anchor ContextMemory Writes Substrate

**Claim ID:** MECH-189
**Subject:** development.super_ordinal_goal_formation
**Substrate:** built 2026-06-09 (as-built doc). Promotion is gated on the MECH-189 validation retest (the V3-EXQ-588 successor with a new letter) — building the substrate PROMOTES NOTHING. Governance status is carried by the `status:` frontmatter / claims.yaml.
**Registered (substrate doc):** 2026-06-09
**Closure node:** `infant_substrate:GAP-11` (EXQ-ISEF-002 transient-benefit-patch z_goal seeding)
**Depends on:** INV-041, SD-016, INV-037, INV-038, MECH-117, MECH-112
**Blocks / unblocks:** DEV-NEED-006, DEV-NEED-024, the MECH-189 retest (V3-EXQ-588 successor with a NEW letter)

## Problem

MECH-189 asserts: *"During the child phase, high-salience benefit contacts under
high contextual complexity are written to persistent ContextMemory as
super-ordinal goal anchors that bias adult z_goal seeding across novel episodes."*

The `V3-EXQ-588` (EXQ-ISEF-002) FAIL was reviewed `non_contributory` for MECH-189
(`failure_autopsy_V3-EXQ-588_2026-05-19`, confirmed): the transient-benefit-patch
env feature (GAP-3) works (C2/C3 confirmed), but the run measured the
**within-episode `GoalState` attractor** (MECH-112 / DEV-NEED-006 infant gate), not
the **child-phase ContextMemory super-ordinal write path** the claim actually
describes. The autopsy and `developmental_needs_register.md:136` both conclude:

> "MECH-189 needs **cue-indexed persistent goal-anchor writes** and an **adult
> z_goal seeding readout** before it can be gated."

V3 had no such substrate. The `IncentiveTokenBank` (SD-057) is per-object and
**per-episode** (`GoalState.reset()` clears it); the ghost-goal bank (MECH-292) is
over hippocampal anchors. Neither is the **cross-episode** super-ordinal z_goal
store MECH-189 needs. `GoalState` itself resets z_goal each episode. So the
mechanism the claim describes — childhood-formed meta-goals that *persist across
adult episodes* — had no place to live.

DEV-NEED-024 (Super-ordinal goal formation) carries the open question this
substrate must answer: **"What contextual-complexity threshold triggers a
super-ordinal write?"**

## Solution

A new **agent-owned, cross-episode-persistent** cue-indexed store
`SuperOrdinalGoalMemory` (`ree-v3/ree_core/goal.py`, sibling to
`IncentiveTokenBank`), wired into `REEAgent.update_z_goal`. NOT reset by
per-episode `agent.reset()` — cross-episode persistence is the defining property
of a super-ordinal goal hierarchy versus an episodic z_goal.

### Store

Each slot is a `(key = z_world context [world_dim], value = z_goal anchor
[goal_dim], strength)` triple — **cue-indexed**: the key is the context cue, the
value is the stored super-ordinal goal. Pure stateful tensor store + cosine
arithmetic; no `nn.Module`, no trainable parameters, no gradient flow.

### WRITE (child phase only)

After the within-episode `GoalState.update()`, the current z_goal is written as a
super-ordinal anchor keyed on the current z_world context **iff the MECH-189
conjunction holds**:

- **(a) high salience** — `salience = benefit_exposure * (1 + drive_weight *
  effective_drive) >= super_ordinal_salience_threshold`. The drive-modulated
  "large benefit spike"; routine low contacts do not clear it, transient-benefit
  patches do.
- **(b) high contextual complexity** — `complexity >=
  super_ordinal_complexity_threshold`. **Pluggable** (`super_ordinal_complexity_mode`):
  - `"novelty"` (default, self-contained): `complexity = 1 - max
    cosine(z_world, occupied anchor keys)`. Empty store → 1.0 (first contacts
    bootstrap the hierarchy); a context already covered by an anchor → low
    complexity → no write (the spec's *selective neoteny* — adult-routine
    stability).
  - `"external"`: complexity supplied by the caller, so an experiment can drive
    it from E1 cue-context entropy / prediction-error without coupling the
    substrate to those optional channels.

  The mode/threshold is the **DEV-NEED-024 adjudication target** — to be settled
  by the validation EXQ and a follow-on lit-pull, not hard-coded here.

  > **Literature verdict (DEV-NEED-024, 2026-06-10 — directional, not a settle).**
  > The follow-on lit-pull
  > ([`targeted_review_connectome_mech_189`](../../evidence/literature/targeted_review_connectome_mech_189/SYNTHESIS.md);
  > combined view
  > [`mech_189_evidence_overview.md`](../../evidence/literature/mech_189_evidence_overview.md))
  > finds the gate biologically justified but the default `'novelty'` *form*
  > questionable on two counts: (1) **reference set** — biological novelty is
  > comparator-mismatch against the *whole world model* (Lisman & Grace 2005),
  > not `1 − cosine` to the goal-anchor keys; (2) **functional form** — the signal
  > should be **prediction-error magnitude** (Aberg 2017) and likely
  > **signed/nonmonotonic** (Quent 2022 U-shape: schema-congruent *and*
  > schema-incongruent both encode), not a monotonic dissimilarity. **Recommendation:**
  > prefer `super_ordinal_complexity_mode='external'` fed by an E1/E2
  > prediction-error / surprise signal; if `'novelty'` is retained, reference the
  > world model rather than anchor keys and consider a signed form. **Transfer
  > caveat:** the cited PEs are value/RL prediction errors, whereas REE's E1/E2 PE
  > is a forward-model error — the validation EXQ should not assume they are
  > interchangeable. Lit signal only; does not change MECH-189 status/confidence.

Writes are permitted only while `write_enabled` (the **child phase**). The
curriculum freezes writes at the child→adult transition via
`REEAgent.set_super_ordinal_write_enabled(False)` (the MECH-334 `on_phase3_entry`
crystallization precedent).

**Allocate vs reinforce (gate (b) governs formation only):** gate (a) high
salience is required for *any* write. A contact within `merge_similarity` of an
existing anchor key **reinforces** that anchor (EMA-blend key+value toward the
*current* z_goal, raise strength) — and this proceeds on salience alone,
*regardless* of complexity, because a recurring high-salience context should
strengthen its existing super-ordinal goal toward the matured z_goal. Gate (b)
high contextual complexity governs only the **allocation of a NEW anchor** (a
genuinely novel/rich context warrants a new meta-goal). Without this split the
anchor would freeze at the tiny z_goal captured at its first contact and never
learn the matured childhood meta-goal — surfaced and fixed by the V3-EXQ-588c
smoke test, which went from anchor norm 0.019 (frozen-at-first-contact) to 0.373
(matured) after the correction.

### READ (adult z_goal seeding readout)

Each `update_z_goal` tick, when the live z_goal norm is below
`super_ordinal_seed_below_norm` (default 0.4 — matching the DEV-NEED-006 gate, i.e.
the agent has no strong episodic goal of its own), the store is queried with the
current z_world; if the best-matching anchor clears
`super_ordinal_seed_match_threshold`, z_goal is pulled toward the retrieved
super-ordinal anchor via `GoalState.cue_pull` (no benefit pulse). This is the
*"stored z_goal anchors bias z_goal seeding in adult episodes even in novel
contexts"* readout.

### Config (all no-op defaults; bit-identical OFF)

On `GoalConfig` (mirrored through `REEConfig.from_dims`):

| Param | Default | Purpose |
|-------|---------|---------|
| `use_super_ordinal_goal_anchors` | `False` | master switch |
| `super_ordinal_n_slots` | `16` | cue-indexed anchor slots |
| `super_ordinal_salience_threshold` | `0.5` | WRITE gate (a) |
| `super_ordinal_complexity_mode` | `"novelty"` | WRITE gate (b) mode |
| `super_ordinal_complexity_threshold` | `0.3` | WRITE gate (b) floor |
| `super_ordinal_merge_similarity` | `0.8` | reinforce-vs-allocate |
| `super_ordinal_write_alpha` | `0.3` | EMA blend into a slot |
| `super_ordinal_seed_below_norm` | `0.4` | READ: seed only when z_goal below |
| `super_ordinal_seed_match_threshold` | `0.3` | READ: min retrieval match |
| `super_ordinal_seed_strength` | `0.1` | READ: cue-pull strength |

## Architecture Context

The store sits between `GoalState` (episodic z_goal attractor) and the cortical
goal pipeline. It reuses `GoalState.cue_pull` (the SD-057 L6 directional nudge)
for the adult seeding path and the existing `update_z_goal` salience/drive signals
for the write gate. It does not modify `GoalState`, the `IncentiveTokenBank`, the
hippocampal ghost-goal bank, or the E1 `ContextMemory` — it is a strictly additive
agent-level store.

`INV-037`/`INV-038` (stored vs active z_goal): the super-ordinal anchors are the
*stored* representation; the live `GoalState._z_goal` is the *active* one. The
write threshold is what makes childhood special (`INV-041`): constrained
affordances + high-complexity contexts maximise super-ordinal formation, while
adult routine contexts are low-complexity and do not trigger writes (selective
neoteny, `INV-056`).

## What This SD Enables

- The `infant_substrate:GAP-11` MECH-189 retest (a `V3-EXQ-588` successor with a
  NEW letter), measuring adult z_goal seeding from childhood-formed anchors.
- DEV-NEED-006 / DEV-NEED-024 gating.

## Validation

`V3-EXQ-588c` (`experiments/v3_exq_588c_mech189_super_ordinal_seeding.py`,
`experiment_purpose=diagnostic`, `claim_ids=["MECH-189"]`, supersedes the 588
ISEF-002 chain). Forced-feed child phase (decoupled from the foraging-contact
ceiling that blocked 588) forms cross-episode anchors → freeze →
adult episodes seed a fresh sub-floor z_goal from the anchors with no benefit
pulse. ARM_ON vs ARM_OFF × 3 seeds.

- **Load-bearing C1 (discrimination):** ARM_ON adult median z_goal exceeds the
  per-seed ARM_OFF baseline by a clear margin (the MECH-189 write+read path moves
  adult z_goal where the no-store baseline gives ~0). This is the substrate
  question.
- **Advisory (reported, not gating):** fraction of ARM_ON seeds crossing the
  DEV-NEED-006 / 588 governance gate (0.4). On the untrained-encoder readiness
  harness the matured-z_goal anchor norm ceilings at ~0.37 (the forced-feed
  z_world-EMA asymptote ≈ 0.9·‖z_world‖), so 0.4 is regime-bound — a near-miss
  with strong discrimination still validates the substrate and routes the
  absolute gate to a trained-encoder evidence successor, not a substrate failure.
- **Readiness / non-vacuity** (else `substrate_not_ready_requeue`): ARM_ON anchors
  form, seeding fires, and a positive-control adult z_goal is non-zero.

Dry-run PASS (C1 discrimination 1.0; ARM_ON 0.28 vs ARM_OFF 0.0). Full-scale probe
post gate-fix: ARM_ON adult median 0.364, anchor norm 0.373, vs ARM_OFF ~0.

## MECH-094

Waking-only. `update_z_goal` is the waking seeding path; `write(simulation_mode=True)`
is a no-op, so replay/DMN content cannot form super-ordinal anchors.

## Phased training

Not applicable — pure stateful store + cosine arithmetic; no learned parameters.

## Related Claims

INV-041, INV-037, INV-038, INV-055, INV-056, SD-016, MECH-112, MECH-116, MECH-117,
MECH-329 (wanting-before-liking ordering; child of MECH-189), MECH-292/293
(ghost-goal bank; distinct hippocampal-anchor store), SD-057 (IncentiveTokenBank;
distinct per-object per-episode store), MECH-094, DEV-NEED-006, DEV-NEED-024.
