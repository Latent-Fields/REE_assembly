# The unfailable-criterion class: a decision-ready recommendation for MECH-428, and a systemic pass

**Generated:** 2026-09-11T14:23:54Z
**Session:** `confident-panini-0cdba7` (chip `chip-20260910-merge-unfailable-criteria-redesign`, items 2 and 3)
**Companion:** `mech536_c1_reposed_confinement_criterion_20260911.md` (item 1, GFLAG-0233, landed `5e6c37fce9`)
**Status of this document:** **item 2 is a RECOMMENDATION, not an applied decision.** See section 0.

---

## 0. Why this stops at a recommendation

The merging chip says "pick a direction, record which and why, then build the replacement". I have
done the first two and deliberately **not** the third, because both upstream sources put the choice
with governance and neither has yet exercised it:

- `exq884a_mech428_c1_structurally_unfailable_redteam_blocking_20260908.md` section 6 lists the four
  candidates as "none of them this session's to choose", and routes them to "`/governance` Step 2b,
  then `/queue-experiment` on the ratified design".
- `governance_flag_adjudication_20260909.md` GFLAG-0227 classifies the criterion redesign
  **NEEDS-DECISION**: "not resolvable by a registry edit alone, **requires governance to pick a
  direction** and then a new experiment build."

The user's 2026-09-10 approval of the docket therefore approved *that governance picks* — it did not
pick. This is the exact contrast with item 1: GFLAG-0233's docket entry recommended a specific
option (1) and that recommendation was approved, so implementing it was executing a ratified
direction rather than making a new call. Building a driver here on a direction I chose would race
ahead of the confirmation the four candidates were explicitly held for.

**So what follows is written to be ratifiable in one reading**, with the arithmetic independently
re-derived and the disqualifying evidence for each rejected option stated.

---

## 1. MECH-428: the defect, independently re-derived

`lift_fraction` at steady state is the closed form `alpha / (1 - (1 - alpha) * decay^T)` in the mean
inter-credit-event interval `T` alone, with `alpha = 0.05` and `decay = 0.995` fixed `GoalConfig`
defaults. Re-derived this session, matching the source document exactly:

| `T` | closed-form `lift_fraction` |
|---|---|
| 6.5 (realized) | 0.6215 |
| 15 | 0.4208 |
| **22 (geometric max leg, 12x12 grid)** | **0.3351** |
| 26.14 (where C1 would first fail) | 0.3000 |
| 40 | 0.2246 |

C1's floor is 0.30. The greedy Manhattan walk reaches its waypoint in exactly its Manhattan
distance, at most `11 + 11 = 22` on this grid. **The bar is unreachable from above by 4.1 steps of
horizon**, so C1 has no failing region and the run records `PASS / supports` whatever the substrate
does.

**A second, independent vacuity, and it is the one that decides the recommendation.** The source
document records `z_world` coherence 0.998 — an untrained encoder on a low-variety hazard-free grid.
Verified this session: the parked driver
(`ree-v3/experiments/_scratch/v3_exq_884a_mech428_subgoal_bootstrapped_goal_seeding.py`, 796 lines)
contains **no P0 encoder-training phase at all**, and says so itself at lines 268-269 ("the
dry-run-observed `z_world` norm magnitude for an UNTRAINED encoder"). The "structured parent
attractor" the DV certifies is therefore ~0.61 x one nearly-constant direction, which a constant
vector fed to `credit_subgoal_attainment` every ~7 ticks would reproduce with no environment at all.

## 2. Recommendation: option 1, CONDITIONED on option 2 — and they are not alternatives

> **Recommended: (1) score the parent's CONTENT, not its norm — with (2) P0 encoder training as its
> PRECONDITION, not as a competing option.**

MECH-428 is a claim about *subgoal-bootstrapped* goal seeding: the parent goal should be **structured
by the attained subgoals**. A norm ratio cannot distinguish "structured by attained subgoals" from "a
running average of whatever the encoder emitted" — those two have the same norm. Only a content DV
separates them, and a content DV has nothing to bite on while the encoder is untrained and `z_world`
is a constant direction. Hence the conditioning: **option 1 alone, on the current untrained
substrate, would be a second unfalsifiable criterion** — the alignment would be ~1.0 against every
control because every vector is nearly the same vector.

**Concrete falsifier shape:** parent alignment with the representations of the **attained** subgoals,
against two pre-registered controls in the same run — (a) a **shuffled** control (the same subgoal
representations, permuted across attainment events) and (b) a **non-attained** control (subgoals
present but never credited). C1 passes only if attained alignment exceeds **both** controls by a
margin scaled on the SD of the delta plus an absolute floor ([memory]
`feedback_effect_size_pass_gate_margin`). A parent that is merely an EMA of a constant-direction
encoder output fails this by construction — which is precisely the failing region the current C1
lacks.

### Why the other two are rejected, with the disqualifying reason

**Option 4 (withdraw the 0.30 floor; score the residual above the closed-form prediction) — rejected,
and it inverts the defect rather than removing it.** The source document's own measurement is that
the closed form predicts the measured `lift_fraction` to **within 1.5% on every seed** (0.6161 vs
0.6156, 0.6016 vs 0.6077, 0.6286 vs 0.6341). The residual is therefore ~0 *by construction*, so a
criterion on it is not unfailable but very nearly **unpassable**. Trading a criterion that always
passes for one that always fails is not a repair — both are pre-determined.

**Option 3 (manipulate `T` as an independent variable) — rejected as the PRIMARY criterion, but keep
it as a recorded diagnostic.** It is a genuine measurement, and it would convert the identity from a
confound into a test. But what it tests is that the EMA accumulates and decays as its own closed form
says — a property of `credit_subgoal_attainment`'s arithmetic, not of MECH-428's mechanism. A PASS
would certify the code, not the claim. It is worth recording alongside option 1 (it is nearly free,
and it validates the instrument), but it cannot carry the verdict.

**Option 2 is not rejected — it is promoted to a precondition** (section 2 above).

### What ratifying this costs

One design + build cycle on a driver that already exists and is smoke-green apart from its criterion
and its missing P0, plus the P0 training time. The SD-094 environment fix in the parked driver is
confirmed sound and carries forward unchanged.

---

## 3. Systemic pass (chip item 3): THREE instances, and the detector is working

The consolidation pass asked whether two independently-flagged claims with the same structural defect
indicate something systemic. Scanning `governance_flags.v1.json` and `evidence/planning/` for the
signature (a pre-registered criterion that is an arithmetic property of the thing it validates):

| # | claim | flag | the identity | driver |
|---|---|---|---|---|
| 1 | MECH-536 / MECH-535 | GFLAG-0233 (now resolved) | `period2_cycle_present` is False for every `k >= 2` latch by construction | V3-EXQ-1007a, parked `.blocked` |
| 2 | MECH-428 | GFLAG-0227 (resolved) | `lift_fraction` closed form clears its own 0.30 bar for all reachable `T` | V3-EXQ-884a, parked `.blocked` |
| 3 | **MECH-439** | **GFLAG-0234 (resolved)** | rung-3 shares tend to `1/k` and clear a `1e-3` floor by three orders of magnitude | **V3-EXQ-1012, parked `.blocked`** |

**The reassuring half: all three were caught BEFORE any fleet time was spent.** Each was found by the
`/queue-experiment` Step 4.5 adversarial red-team (model `fable`) returning BLOCKING, each driver was
authored and smoke-green, and each was parked rather than queued. That is the Step 4.5 pass doing
exactly the job it was added for, three times, and it is direct evidence for its GOV-HELDOUT-1
falsifier ("if after ~10 uses no CONTESTED or BLOCKING finding has survived verification, remove this
step"). It has survived verification three times.

**The worrying half, and it is a process gap rather than a science gap: the residual outlives the
flag.** In all three cases the governance flag is now **resolved** — its registry half landed — while
the actual criterion re-posing did not. Because the flag is closed, `/governance` will not re-surface
any of them on a later cycle, so each residual survives only as a chip. For MECH-428 that chip is the
one this session is executing. **For MECH-439 there is no open chip at all**:
`chip-20260907-e3-commensurability-validation` is marked `done` (it queued the validation), and the
re-posing GFLAG-0234 recommends (its option A — re-pose onto a selection-level DV, commit-flip rate
under shadow OFF/ON scoring, and amend the architecture doc and the autopsy's identical sentence
together) is owned by nothing. A chip has been raised for it alongside this record.

**One structural observation worth a governance decision of its own** (not acted on here): a flag
whose verdict is NEEDS-DECISION is being resolved when its *registry* half is applied, leaving the
decision itself unowned. Three for three, the un-owned half is the one that matters scientifically.

## 4. What this document does NOT do

- It does not edit `claims.yaml` (a `/governance` cycle, `gov-20260911`, held it while this was written).
- It does not pick MECH-428's criterion — section 0.
- It does not touch MECH-439 beyond raising a chip; GFLAG-0234's own recommendation stands as written.
