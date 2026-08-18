# D-001 cycle-1 adjudication — proposal to /governance

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

- **Adjudicated:** 2026-08-18T04:29:37Z, session `chip-20260817-d001-unowned-v3-claims` (headless, `ree-cloud-5`)
- **Base:** `REE_assembly` `b3b95d7938` (clean read of `origin/master` in a detached worktree — the shared cloud-5 checkout was `[ahead 194, behind 178]` and its `docs/claims/claims.yaml` differed, so it was not used)
- **Detector:** D-001 `phase_generation_mismatch`, 27 findings
- **Ratchet verdict:** `refine` — 24 suppressions recorded, detector demoted to list-only
- **Ratchet artefacts:** `scripts/steward/docs/DETECTORS.md` (D-001 entry), `scripts/steward/state/suppressions.yaml`, `scripts/steward/state/steward_ledger.jsonl` (28 records), `scripts/steward/detectors/d001_phase_generation_mismatch.py`

---

## What governance is being asked to decide

**Three claims carry a stale `implementation_phase: v3` that should read `v4`.** Nothing else in this file needs a decision; the other 24 findings were adjudicated as false positives and suppressed with reasons, which is within the Steward's own authority.

| claim | owning node | current | proposed | `v3_pending` |
|---|---|---|---|---|
| ARC-053 | `deferred_by_commitment:DEF-1` | `v3` | `v4` | *(absent)* |
| ARC-054 | `deferred_by_commitment:DEF-1` | `v3` | `v4` | `true` → remove |
| MECH-270 | `deferred_by_commitment:DEF-2` | `v3` | `v4` | `true` → remove |

### Why this is drift and not a deliberate arrangement

Two independent signals agree, neither of which was constructed by this session.

**1. The reassignment was already performed for their siblings and not for them.** Both nodes deliver a cluster of claims, and the rest of each cluster has already moved:

```
DEF-1  unblocks ARC-053(v3)  ARC-054(v3)  ARC-055(v4)
DEF-2  unblocks MECH-225(v4) MECH-226(v4) MECH-227(none) MECH-228(v4) MECH-270(v3)
```

**2. Both node notes name the drift in so many words.** `DEF-1`: *"NOTE phase-tag drift: ARC-053/ARC-054 currently read implementation_phase: v3 in claims.yaml while this doc treats the cluster as v4-deferred — reconcile in the held-reassignment batch (the v4_planning_index already flags this produces misleading hold_pending_v3_substrate recs)."* `DEF-2`: *"MECH-270 currently reads implementation_phase: v3 (drift, same note as DEF-1)."*

The held-reassignment batch those notes point at has not run. The notes are dated 2026-06-11; the drift has stood since.

### Consequence of leaving it

The `deferred_by_commitment` lane exists to hold work that is **deliberately parked** — its header says `generation: deferred` "keeps these out of every generation percentage (V3 closure and the V4/V5/V6 roadmaps)". So the closure percentage is **not** wrong today either way. What the stale label does produce is the specific harm DEF-1's own note names: `ARC-054` and `MECH-270` carry `v3_pending: true`, which per the V3-Pending Gate means "cannot be promoted until V3 experiments provide evidence" — for substrate the project has committed to **not building in V3**. That generates the misleading `hold_pending_v3_substrate` recommendations the note warns about, indefinitely, for work that is correctly parked.

### Authority note

`claims.yaml` edits are governance's, so nothing here was applied. No plan frontmatter was edited either — the plan side is already correct, it is the claim labels that lag — so **no closure number moved and no A/B regeneration of `generate_closure_snapshot.py` was required.**

---

## The other 24 findings — adjudicated, suppressed, no decision needed

Recorded here so the disposition is reviewable, not to ask for a ruling.

**A premise correction first, because it changes how the set reads.** D-001 does **not** fire on claims with no closure node — it opens with `if not owners: continue`. All 27 *are* owned, just never by a `generation: v3` plan. The dominant failure mode is therefore not a missing plan but **deliberate cross-generation ownership**, which frontmatter alone cannot distinguish from drift.

**Clinical lane, cross-generation by construction (13)** — INV-062, MECH-186, MECH-187, MECH-188, MECH-203, MECH-206, MECH-208, MECH-209, MECH-210, MECH-286, MECH-343, Q-056, SD-036. `psychiatric_failure_modes_plan.md`'s header: *"a syndrome is not a version. Its claims are scattered ACROSS generations by construction … filing the programme under any single version splits every syndrome in half."* Reinforced by a recorded **user decision of 2026-08-06** in the `MOTIVATIONAL-TAXONOMY` completion note, which was asked exactly D-001's question for MECH-186/187/188 and answered that the v3 label is correct while the claims stay in the clinical lane. Re-escalating these re-litigates a settled decision.

**Refuted by the owning node's own text (2)** — MECH-163 (`hippocampal_planning_v4:HPL-1`: *"This is the ONLY node whose claim is implementation_phase: v3. It is the gate, not a V4 step"*) and MECH-308 (`language_emergence_bootstrap_v6:LANG-7`: *"MECH-308 stays implementation_phase v3/v3_pending in claims.yaml (NOT reassigned here…)"*). In both, a human already considered the reassignment and wrote down the decision against it.

**Forward-roadmap back-pointer (9)** — ARC-088, ARC-106, MECH-099, MECH-124, MECH-261, MECH-264, MECH-333, MECH-384, MECH-436. `goal_deliberation_v4_plan.md`: *"Each node's readiness_gate lists the V3-era prerequisites (claims/tracks) that must land before the V4 substrate step is honest to build."* Six of the owning nodes are `status: done` literature-grounding nodes that explicitly "PROMOTE NOTHING". Follows the already-accepted `D-001:MECH-099` precedent verbatim. Note MECH-264 and MECH-308 share the `held_v4_by_architectural_commitment` verdict, and MECH-308's was explicitly adjudicated as "keep the v3 label" — so that verdict does not by itself imply a label change.

### Precision and the floor

**3 confirmed / 27 = 0.11**, against the SKILL.md floor of 0.6. Under the most generous defensible reading — also counting SD-036 and MECH-286, which have live V3 experiments (`V3-EXQ-854` queued; `v3_exq_891` PASS 2026-08-08), as real denominator holes — it is 5/27 = 0.19. Both far below, so D-001 is demoted to list-only: still reported, never escalated.

A sharper predicate was **measured rather than assumed**: fire only when a sibling co-listed in the same owning node has already been reassigned off v3. That cuts **27 → 9**, keeps all 3 confirmed, and drops all 13 clinical plus MECH-163 and MECH-308 — but reaches only **3/9 = 0.33**, because inside a v4 plan most co-listed claims are v4 anyway. Tightening further would fit the predicate to the same 3 cases it would then be validated on, which `GOV-HELDOUT-1` exists to forbid. Hence suppressions (per-claim, reasoned, reversible) rather than a predicate change.

**Resume condition:** restore escalation once these three are dispositioned **and** one full cycle has run with the suppressions live, **if** the unsuppressed residue then measures ≥ 0.6.
