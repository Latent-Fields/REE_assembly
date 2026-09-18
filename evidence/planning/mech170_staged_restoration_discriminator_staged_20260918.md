**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`, and it does not itself commission any experiment.** The build it refers to is commissioned separately, as `substrate_queue.json` entry `sd068-staged-restoration-mode` (candidate, `ready: false`). This document exists to state the ONE scientific question that must be answered before a MECH-170 experiment is worth designing, and to end in the decision only the user can make.

# MECH-170 staged restoration: what would discriminate a RECOVERY order from the already-banked DECLINE order?

- **Date:** 2026-09-18
- **Session:** `science-20260918-sd071-carveout-and-run` (metaworker, headless, ree-cloud-5)
- **Authority:** user decision 2026-09-18T22:54Z (real `AskUserQuestion`, Orchestrator decision lane `orchestrate-20260918-1840-cloud4`) on decision chip `chip-20260918-mech170-carveout-scope` -- **OPTION B, COMMISSION THE BUILD**, chosen over this session's recommendation to park. The MECH-121 carve-out is **NOT** widened.
- **Claim:** MECH-170 (`candidate`), `subject: dementia.sleep_restoration_dissociated_recovery_prediction`, `claim_type: mechanism_hypothesis`, `depends_on: [MECH-168, INV-047, MECH-120, MECH-121]`. One claim depends on it: **MECH-177**.
- **Related:** `GFLAG-0319` (resolved -- the purpose-contract carve-out), `GFLAG-0351` (open -- the SD-071 C3 reparameterisation finding), work chip `chip-proposal-exp-0905-paced` (open, unclaimed), proposal **EXP-0872 / EVB-1449**.

> **Correction on the record, because it bore on the cost the user was weighing.** The decision chip that produced OPTION B described MECH-170 as "a claim with no dependents named". That was wrong: **MECH-177 depends on MECH-170** (verified against `claims.yaml` 2026-09-18T23:0xZ). The error made option B look cheaper to decline than it was. It does not change the decision, which is already taken.

---

## 1. Why MECH-170 was never actually blocked by the purpose contract

MECH-170 was bundled into `GFLAG-0319` with SD-071 because the SD-068 harness's unconditional `EXPERIMENT_PURPOSE="diagnostic"` contract appeared to block both. The 2026-09-18 carve-out lifted that contract for instrument-validity claims only, and MECH-170 **fails both carve-out conditions structurally** -- it is a behavioural prediction, and its `depends_on` includes MECH-120 and MECH-121 directly, which is exactly what condition (ii) excludes.

That turns out not to matter, because **the purpose contract was never MECH-170's real blocker.** Two substrate-level blockers stand independently of it, and neither is touched by any carve-out. This document is about the second one, which is the harder of the two.

## 2. Blocker 1 -- the instrument runs the wrong direction (a BUILD)

`consolidation_lesion_harness.py::run_staged_sweep` (`:1806`) sweeps **damage only**: a single uniform diffuse-damage scalar `sigma` applied identically to each phase, with `observed_order` derived by ranking phases on damage-tolerance (which phase crosses 50% degradation at the lowest sigma). There is **no staged-RESTORATION mode** -- verified by grep: the string `restor` occurs exactly **once** in the 1,900-line harness, in unrelated prose about SHY flattening attractors (`:334`).

MECH-170 predicts a **recovery** order under sustained sleep-architecture restoration. The instrument cannot run that direction at all. This is `complicated (buildable)`, and it is what `substrate_queue.json` entry `sd068-staged-restoration-mode` commissions.

## 3. Blocker 2 -- THE OPEN QUESTION: the predicted recovery order is the banked decline order

This is the blocker that makes a MECH-170 experiment premature even once the build lands.

**The two orders coincide.** The harness's banked falsifier (header `:11-14`, measured by V3-EXQ-778a) asks whether functional failure under uniform damage emerges *"STAGED in reverse dependency order (REM >> NREM >> SWS) rather than uniform"* -- downstream-first. MECH-170's predicted recovery sequence is *"(1) improved confidence and precision in contextual attributions ... (2) improved new episodic memory consolidation (slot-filling) ... (3) improved contextual semantic memory (slot-formation)"* -- REM-analog, then NREM/MECH-121-analog, then SWS/MECH-120-analog. **The same downstream-first sequence.**

So a run reporting "recovery proceeds REM -> NREM -> SWS" reports an ordering the banked decline measurement already implies. It would look like a confirmation of MECH-170 while carrying no information about recovery specifically.

**And there is a sharper form of the problem, which is the real reason this cannot be waved through.** `phase_integrity_at_sigma` (`:1029`) gives **each phase a FRESH agent** -- deliberately, and the docstring says why: *"a serial pass would bake in the very error-compounding the non-vacuity contract must avoid"* (`:1039-1042`). Each phase's reading is therefore its own static, monotone transfer function of `sigma`. **Reading that same sigma grid in DESCENDING order is not a new measurement at all** -- it is the identical per-phase transfer functions re-indexed, so it would reproduce the decline order by arithmetic, exactly as a "restoration" result.

That failure mode is the same species as the one confirmed this session on SD-071's C3 ladder (`GFLAG-0351`): a manipulation that is a reparameterisation of an existing measurement, presented as an independent check. It is cheap to build and impossible to interpret. **A naive descending-sigma "restoration mode" must not be what gets built.**

## 4. Candidate discriminators

Each is a different answer to: *what measurement separates "the pipeline rebuilds in dependency order" from "the pipeline's phases have different damage tolerances, read backwards"?* Costs are architectural, not wall-clock.

### D1 -- Hysteresis (path asymmetry between damage and restoration)

**Measures:** each phase's integrity at the *same* sigma on an ascending (damage) path versus a descending (restoration) path from a damaged state, on **one agent instance carried through both**, reported as a per-phase hysteresis area.

**Why it discriminates:** if recovery merely retraces decline, the hysteresis area is ~0 on every phase and MECH-170's ordering claim is shown to carry nothing beyond the banked result -- *a real and informative refutation*. A per-phase-ORDERED nonzero hysteresis is a quantity the static damage-tolerance curves cannot produce, so it cannot be a reparameterisation artifact.

**Cost / tension, stated plainly:** requires abandoning the fresh-agent-per-phase isolation for the restoration arm, which the harness header explicitly warns bakes in error-compounding. That trade has to be made deliberately and recorded -- it weakens the SD-068 non-vacuity contract in exchange for making recovery measurable at all. Do not let a build resolve this silently.

### D2 -- Per-phase restoration RATE at fixed dose

**Measures:** with restoration "dose" held fixed, the number of restoration steps each phase needs to cross a fixed integrity threshold -- per-phase recovery time constants, not an ordering.

**Why it discriminates:** MECH-170's clinical content is explicitly temporal and dose-dependent -- *"only if intervention is sustained long enough for schema rebuilding"*. That is a RATE claim. Rates are not derivable from a static damage-tolerance curve at any sigma, so this is orthogonal to the banked result by construction.

**Cost:** the largest build. Needs a restoration *schedule* -- a new time axis (steps), not just a reversed sigma grid -- plus a threshold-crossing readout per phase. It is also the closest analog to the actual clinical protocol MECH-170 describes, which cuts both ways: most faithful, most expensive.

### D3 -- Selective (dependency-blocking) restoration

**Measures:** restore ONE phase at a time while holding the others damaged, and ask whether a downstream phase can recover *without* its upstream prerequisite -- e.g. can REM precision recover while NREM slot-filling is still damaged?

**Why it discriminates:** this tests the CAUSE MECH-170 asserts (*"the pipeline rebuilds in dependency order"*) rather than the correlate. Dependency-blocking gives an asymmetric prediction that damage-tolerance ordering does not: under MECH-170, restoring a downstream phase alone should NOT recover it; under a pure tolerance account, it should. That asymmetry is not expressible as a reparameterisation of the decline sweep.

**Cost:** the mildest. Needs a per-phase restoration mask and no new time axis, and it preserves the existing per-phase-independent measurement design, so it carries the least architectural tension with the SD-068 contract. **This session's assessment: best discriminating power per unit of build.** Recorded as an assessment, not a decision.

### Option N -- none of them

Also a legitimate answer. MECH-170 is a clinical-population prediction whose V3 analog may simply not be worth the build; its `what_would_answer` names *"a prospective sleep intervention study in early MCI"*, and every discriminator above is a V3 analog of that, not the thing itself. Its one dependent, MECH-177, may be reachable another way.

## 5. THE DECISION THE USER MUST MAKE

**Which discriminator (D1, D2, D3, some combination, or N) is MECH-170's eventual experiment to rest on?**

This must be answered before a MECH-170 run is designed, and it should be answered before the staged-restoration mode is built past its base sweep, because **the choice determines what the mode has to EXPOSE**:

| Choice | What the build must additionally expose |
|---|---|
| D1 | one agent instance carried across both path directions + per-phase hysteresis area |
| D2 | a restoration *schedule* (step axis) + per-phase threshold-crossing step counts |
| D3 | a per-phase restoration mask (restore phase X, hold others damaged) |
| N | nothing further; close the entry and route MECH-177 another way |

Until it is answered, a queueing session cannot pre-register a criterion that distinguishes MECH-170's prediction from the result already in hand -- which is precisely why `chip-proposal-exp-0905-paced` must not be worked as a `/queue-experiment` item yet.

**What has been done under OPTION B, and what deliberately has not.** Commissioned: the substrate entry (`sd068-staged-restoration-mode`, candidate, `ready: false`) and this document; and proposal EXP-0872's `blocked_by` re-recorded as the two substrate blockers above. **Not done, on purpose:** no `/implement-substrate` was started -- IGW auto-discovery stages that build as its own consented chip -- and no discriminator was selected, because selecting one decides what gets measured.
