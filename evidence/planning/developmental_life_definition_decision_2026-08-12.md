# Developmental Life Definition: Decision Memo

**Date:** 2026-08-12T17:28Z | **Session:** `mech357-pressure-scoping-11e9c9` (chip `chip-20260812-developmental-life-definition-scoping`) | **Status:** scoping/synthesis, no code or experiment changes; one narrow registry fact-update (see §5)

**Answers:** `developmental_readiness_investigation_2026-08-12.md` §19 item 1 — "decide what a developmental life is supposed to demonstrate." That investigation deferred this decision explicitly; this memo makes the call and links it to GAP-9.

---

## 1. The two prerequisites for a fair MECH-357 test (from `competence_via_lifelong_practice_and_sleep_synthesis_2026-08-10.md` §6)

An integrated "long life + non-parametric practice + sleep" test needs:

- **(a) Layout continuity across segments** — removes the environment-luck confound in the within-life development readout. Owner: `chip-20260810-fishtank-developmental-ecology` item 1.
- **(b) A MECH-357 pressure design that genuinely forces the LESION arm to fail its own negative control** — without this, the discrimination test is structurally vacuous (both arms survive/fail together regardless of the mechanism). Owner: `chip-20260810-mech357-pressure-scoping`.

## 2. Current status (checked this session, 2026-08-12)

**(a) LANDED.** Confirmed via `chip-20260810-lifelong-practice-competence-synthesis`'s own 2026-08-11T16:57Z resolution note: V3-EXQ-913 (ree-v3, queued) combines layout continuity + a microhabitat cue + a sleep-vs-no-sleep ablation, with MECH-357 confirmed active in `_make_config()`.

**(b) NOT landed — and this session found it is in a *worse* state than "unlanded."** `chip-20260810-mech357-pressure-scoping` (resolved 2026-08-11, same session-id lineage as this one) did not build a fix; it produced a scoping recommendation: try the already-built, zero-new-code SD-029 `scheduled_external_hazard` mechanism before committing to genuine agent-directed predator pursuit. That recommendation **was built and run** as **V3-EXQ-603t** (`ree-v3` commits `242fd7e`/`24482c5`, manifest `v3_exq_603t_instrumental_avoidance_scheduled_external_hazard_20260811T173724Z_v3`, run 2026-08-11T17:37Z) — **and it also failed discrimination.** `ARM_LESION` (no gate) hit full survival ceiling on all 3 seeds (`g_h_frac=1.0`, median episode length 200/200 = the step cap, `per_seed_avoidance_efficacy=[0,0,0]`), i.e. the scheduled-hazard field produced *less* conflict than 603s's exact-tie result, not more. `primary_pass=false`, `evidence_direction=non_contributory`.

This is the **5th** inconclusive-by-design-defect MECH-357 combined-fix attempt (603h → 603k → 603r → 603s → 603t), not 4 as both the 2026-08-10 synthesis doc and the 2026-08-12 investigation doc state — both predate or missed this run. **As of this writing, V3-EXQ-603t sits unreviewed** in `pending_review.md` and neither `substrate_queue.json`'s `failure_record` nor `claims.yaml`'s MECH-357 `evidence_quality_note` had been updated to reflect it. See §5.

The one candidate this scoping chip named but did not try — genuine agent-directed predator pursuit — remains untried; a partial substrate primitive for it (`env: hazard_agent_pursuit`, sibling to `hazard_food_attraction`, ree-v3 commit `39b5ca8`) already exists but has not been threaded through any driver.

## 3. GAP-9 (sleep reachability): recommendation

`sleep_substrate_plan.md`'s GAP-9 (registered 2026-08-12, `complicated (buildable)`, severity high, status `open`) establishes that `SleepLoopManager`'s only autonomous trigger, `notify_episode_end()`, fires exclusively at inter-episode/segment boundaries — a true single-continuous-life driver (`num_episodes=1`) has zero such boundaries by construction, so sleep cannot fire at all, regardless of cadence configuration. Three candidate fixes are named (step-count/time-based trigger; MEL/fatigue-based trigger reusing GAP-5b's accumulator; an experimenter-inserted "virtual boundary"), with the design choice left open.

**Recommendation is tiered, and turns out to already be in motion — no new build is owed right now.**

1. **For an OBSERVATIONAL long-single-life study** (the V3-EXQ-920 shape: watch one natural trajectory, no manipulation) — leaving sleep unreachable is an acceptable, documented controlled variable, **provided the write-up says so explicitly and draws no consolidation claim.** This is already the discipline in practice: `chip-20260812-exq920-multiseed-degradation-retrospective` (open) is scoped to report any degradation trend as "prolonged-wake-**associated**, not proven caused by absence of sleep," precisely because there is no sleeping arm.
2. **For a CAUSAL "does sleep matter" test**, GAP-9's own endogenous-trigger fix turns out **not to be on the critical path**: `ree_core/sleep/phase_manager.py`'s `force_cycle()` already exists as a manual, experimenter-triggered override, usable inside a single-life driver *today*, without waiting on a design decision among GAP-9's three candidates. `chip-20260812-causal-sleep-deprivation-matched-arm-design` (open) is already scoped exactly this way — a matched-arm (force-sleep vs continued-wake) design using `force_cycle()` directly, explicitly labelled as an experimenter-triggered causal control rather than natural sleep onset.
3. **Deciding among GAP-9's three candidate autonomous-trigger designs is also already chipped and appropriately sequenced ahead of any build**: `chip-20260812-sleep-onset-multiinput-litsynth` (open) is scoped to weigh the three against existing sleep-drive literature (Borbély two-process model, Meyniel's leaky-accumulator, existing REE lit-pull corpus already cited there) before any of them gets built. Building one now, ahead of that synthesis, would pre-empt a scoping step already in flight for good reason (three real design candidates, biology-before-formal-definitions is this repo's own standing principle).

**Net: I am not spawning a GAP-9 build chip.** The three already-open chips (§3.2, §3.3, and the retrospective in §3.1) already cover exactly the ground a new chip would cover, in the right order (literature synthesis and observational-vs-causal design *before* committing to an autonomous-trigger implementation). Spawning a fourth here would be the "second, staler tracker" this repo's chip-discipline explicitly warns against.

## 4. Decision: what should a developmental-age experiment target?

Options per the governing question: (a) gradient-based learning, (b) non-parametric practice via MECH-357, (c) both in parallel.

**Recommendation: (b), sequenced correctly, with (a) held as a contingent future decision — not (c).**

- **(a) is not currently a near-term option.** No driver architecture exists for a long, non-frozen (gradient-updating) single life; every long-life driver in the current corpus (906-lineage, V3-EXQ-920, V3-EXQ-913) runs `_observational_run()` under `torch.no_grad()` specifically because it evaluates a policy already trained by a separate curriculum stage. Building an alternative would be a genuinely new, unscoped architecture project — no design doc, no owner, no estimate exists anywhere in this corpus. It is not ready to chip.
- **(b) is close, not exhausted, and cheaper.** The mechanism exists, is wired, and demonstrably engages (`avoidance_efficacy` has reached 0.633 in at least one run) — what has failed 5 times running is the *pressure design* needed to make the test discriminating, not the mechanism itself. One candidate (agent-directed pursuit) remains untried, and a `/failure-autopsy` of 603t (not yet run — see §5) may surface a design defect cheaper than a new pursuit AI, exactly as 603h → 603s's autopsies each did. This is real, bounded, sequenceable work, not an open-ended build.
- **(c), "both in parallel," is the wrong call precisely because the two options are not symmetric in readiness.** Parallelizing a fully-unscoped large build against a nearly-sequenced smaller one would just divide attention without buying anything — (a) has no design to parallelize against yet.
- **The sequencing that actually matters: (b)'s eventual result — pass or fail — is the thing that should decide whether (a) gets scoped at all.** If MECH-357, once fairly tested, is confirmed (practice does build competence without weight updates), that is a far cheaper mechanism to build a developmental-age study around than a new gradient-updating-life architecture, and (a) can stay a longer-horizon item. If MECH-357 is cleanly *falsified* (not another design-defect null, an actual negative with the pressure confound removed), that is itself strong, specific evidence that non-parametric within-life competence isn't achievable with what's built today — which is exactly the finding that would justify prioritising (a)'s architecture investment. Either way, (b)'s outcome is informative for (a) in a way that running them blind in parallel would not be.

This recommendation is contingent on the same caveat the 2026-08-10 synthesis doc already flagged (§7 there): even a fairly-tested MECH-357 might independently hit the same F-dominance/rule-apprehension ceiling MECH-309/`conversion_ceiling_root` describe for gradient-trained selection, since `avoidance_efficacy` still feeds a `score_bias` into the same downstream selection machinery. That risk doesn't change the sequencing recommendation — it's a reason the fair test matters, not a reason to skip it.

## 5. What this session did and did not do

**Did:** Read the two source documents in full; traced the two prerequisites to their current state via git log / manifest / substrate_queue.json / claims.yaml; found and logged (via a narrow, schema-matching `failure_record` append to `substrate_queue.json`'s `mech357-freeze-incompatible-pressure-mechanism` node, JSON-validated before commit) that V3-EXQ-603t already ran and failed, which neither `substrate_queue.json` nor `claims.yaml` reflected; wrote this memo.

**Did not, and why:**
- **Did not edit `claims.yaml`.** It is governance-only per this repo's CLAUDE.md High-Contention Files list; the MECH-357 `evidence_quality_note` needs a governance-reviewed addition analogous to the existing 603h/603r/603s paragraphs, not a unilateral one from a scoping chip.
- **Did not spawn a `/failure-autopsy` chip for V3-EXQ-603t.** Per this repo's chip-spawning discipline, adjudicating a FAIL that hasn't been autopsied yet is `/failure-autopsy` work, one of exactly two categories reported inline rather than chipped (the other being `/governance` work) — `pending_review.md` is already the re-deriving worklist that routes this, and it already lists the run. **Reported here, and flagged in the closing summary to the user**, rather than duplicated as a chip.
- **Did not spawn a GAP-9 build chip.** See §3 — three chips already open cover this ground in the right order.
- **Did not spawn a "6th MECH-357 pressure attempt" chip.** Premature: which design (agent-directed pursuit, a further pressure-mechanism iteration, or a step back to question whether the G_H discrimination criterion itself is well-posed after 5 misses) should be decided by 603t's own autopsy, not guessed here. Chipping a specific build now would risk exactly the hazard this repo's CLAUDE.md names for autopsy-adjacent follow-on: racing ahead of a not-yet-written adjudication.
- **Did not build or queue anything**, per this task's own scope.

## 6. Follow-on (for the user / next governance-or-autopsy pass, reported inline per §5)

- **V3-EXQ-603t needs a `/failure-autopsy`.** It is a real, unreviewed FAIL with a novel failure signature (LESION at ceiling, not a tie) relative to 603s, sitting in `pending_review.md` since 2026-08-11T17:37Z.
- **`chip-20260810-lifelong-practice-competence-synthesis`** (the integrated practice+sleep test) remains correctly withdrawn — prerequisite (b) is now further from landing, not closer, after 603t. Do not re-spawn it until a pressure design actually clears discrimination.
- **The three open GAP-9-adjacent chips** (`chip-20260812-exq920-multiseed-degradation-retrospective`, `chip-20260812-causal-sleep-deprivation-matched-arm-design`, `chip-20260812-sleep-onset-multiinput-litsynth`) should proceed in their existing scope and order; nothing in this memo changes their design, only confirms none of them needs to wait on GAP-9's own endogenous-trigger build.
