# GOV-DIAG-1 re-pose — the MECH-321 / ARC-070 / MECH-288 policy-decomposition chain

**Written:** 2026-08-14T01:14:14Z
**Session:** `metaworker-chip-20260812-govdiag1-repose-mech321-chain`
**Chip:** `chip-20260812-govdiag1-repose-mech321-chain`
**Routed by:** `/governance` 2026-08-12 (session `sd-016-h3-algorithm-3370cd`) from the
GOV-DIAG-1 standing audit (`scripts/check_diagnostic_chain_recurrence.py`)

**This document promotes and demotes nothing.** It touches no claim (the chain is
`claim_ids: []` by construction), queues no experiment, and writes no hypothesis-space
resolution. It re-poses a question, refuses several re-queues, and hands two
already-earned ledger resolutions to `/governance` to apply.

---

## 0. The signal

Three `bears_on` tokens tripped the N≥3 recurrence threshold on one shared chain:
ARC-070 (6 hits), MECH-321 (6 hits), MECH-288 (3 hits). All six hits are
pure-diagnostic (`claim_ids: []`) **and** no-verdict (`recommended_evidence_direction`
in `{non_contributory, inconclusive}`), so they accumulate zero on both claim-keyed
brakes — the re-derive brake and GOV-CEIL-1 — and could circle indefinitely with no
mechanical stop.

| # | run | artifact | date |
|---|---|---|---|
| 1 | `v3_exq_816b_mech321_policy_decomposition_harshened_env_20260726T123216Z_v3` | `failure_autopsy_V3-EXQ-816b_2026-07-26` | 07-26 |
| 2 | `v3_exq_816c_mech321_vs_pe_decoupling_comparator_20260726T105608Z_v3` | `failure_autopsy_816c-822_2026-07-26` | 07-26 |
| 3 | `v3_exq_816d_mech321_policy_decomposition_harshened_env_v2_20260726T185006Z_v3` | `failure_autopsy_2026-07-28-sweep` | 07-28 |
| 4 | `v3_exq_830_mech321_scale_resolved_rollout_boundary_20260727T204927Z_v3` | `failure_autopsy_2026-07-28-sweep` | 07-28 |
| 5 | (same run) | `failure_autopsy_V3-EXQ-830_2026-07-29` | 07-29 |
| 6 | `v3_exq_839_sd084_midexec_reachability_20260729T220727Z_v3` | `failure_autopsy_V3-EXQ-839_2026-07-30` | 07-30 |

V3-EXQ-830 contributes two hits because the counter keys on `(artifact stem, run_id)`
and two artifacts adjudicate it. V3-EXQ-816 and V3-EXQ-820 are **not** in the count:
their cluster autopsy carries non-empty `claim_ids`, so they are the claim-keyed
brake's business, not GOV-DIAG-1's.

MECH-288's 3 hits are the subset `{830 ×2, 839}`. As the routing chip anticipated,
the three tokens are one chain seen from three angles, and one re-pose addresses all
three.

---

## 1. What specifically prevented a verdict, run by run

| run | what was actually measured | why no verdict |
|---|---|---|
| 816b | `low_vs_steps = 0` (floor 5) every cell; `off_pe_mean_worst = 0.008594` vs `pe_elevated_floor = 0.01` → `pe_elevated = false` | The load-bearing DV was a contrast **within low-V_s states**. Zero such states existed, so `C_MAIN` was not evaluable. Positive controls (`vs_tracking_live`, `off_forward_pe_varies`, `off_forward_pe_bounded`) all green — a clean, correctly-instrumented non-reading. |
| 816c | `region_vs_min_over_cells = 0.9338`, `region_vs_var_best = 0.000275`, `total_low_vs_steps = 0`, `spearman_unc_vs_pe_mean_over_cells = 0.0832` (coupled floor 0.2), `pe_heterogeneous = true`, `vs_heterogeneous = false` | This one **did** reach an answer (`vs_pe_decoupled_proxy_saturation`, outcome PASS), and it was adjudicated `non_contributory` and its hypothesis left `alive` pending 816b. See §3 — this is the hinge of the whole chain. |
| 816d | `off_pe_mean_worst = 0.008675`; `predecessor_816b_off_pe_mean_worst = 0.0086`; `low_vs_steps = 0` | Third consecutive environment-axis escalation. Forward-PE across the ladder: **0.0080 → 0.0086 → 0.0087**, i.e. under 0.0007 total movement, each step within noise of the last, never crossing the 0.01 floor; low-V_s occupancy stayed at exactly zero at every dose. |
| 830 | `on_n_sweeps = 2393`, `on_n_sweeps_with_slow = 0`, `on_n_sweeps_cofire = 0`; `decomp_n_evaluated_midexec = 0` in **all 10 cells** against `decomp_n_evaluated_precommit` 1862–2618 | Two separate occupancy zeros in one run: the MECH-288 slow scale never fired on the rollout stream, and MECH-321's R4 mid-execution hook was shown **structurally unreachable** (`post_action_update` destroys `_committed_trajectory` every tick; the hook requires cross-tick persistence). |
| 839 | `total_midexec_on = 415`, `total_midexec_off = 0`, negative-control tier bit-identical | The exception that proves the rule: 839 **fixed** an occupancy gate (SD-084's persistent handle) and then reported occupancy only. Its behavioural criterion C4 was declared explicitly non-load-bearing; the driver's own docstring says "this run adjudicates REACHABILITY only." A verdict on whether R4 *helps* was deferred by design. |

---

## 2. The common failure — and it is one failure, not five

**Every one of the six died at a trigger-occupancy gate, and in five of the six the
load-bearing DV was itself conditional on that occupancy.**

That conditioning is the mis-posing, and it has a precise consequence: it **aliases two
different worlds into one non-verdict**. When a run returns "no data in the low-V_s
subset", that is equally consistent with

- *no effect* — decomposition at prediction-failure loci does not help (a real answer,
  the null the campaign wanted to be able to reach), and
- *no occasion* — the agent never entered the state the trigger keys on (not an answer
  at all).

A subset-conditional DV is **undefined** on the empty subset, so it cannot distinguish
them. Every run therefore returned "not evaluable" rather than a direction, which is
exactly the `non_contributory` / `inconclusive` signature GOV-DIAG-1 counts. And because
occupancy was treated as a *precondition to be hoped for* — something the environment
might eventually supply — the natural next move after each non-reading was to escalate
the environment. That is the loop: 816 → 816b → 816d, three escalations, 0.0007 of
forward-PE, zero low-V_s steps throughout.

Two aggravating design choices made the loop self-sustaining:

1. **The trigger threshold was ABSOLUTE, on a readout whose absolute scale is a property
   of how well-trained the agent is.** `low_vs_steps ≥ 5` and `forward-PE ≥ 0.01` are
   fixed floors. A competent agent has low PE by definition, so the better the agent
   works, the less the instrument can see — the trigger becomes *less* reachable as the
   substrate matures. There is no environment dose that fixes an instrument whose
   sensitivity is inversely coupled to the system's competence.

2. **The readout was a proxy that had already been measured as saturated and decoupled
   from the construct it stands in for.** 816c measured region-V_s at
   `region_vs_min_over_cells 0.9338` with `var_best 0.000275` and
   `spearman(V_s, forward-PE) = 0.0832` against a coupling floor of 0.2, while forward-PE
   in the *same cells* was genuinely heterogeneous (`pe_heterogeneous = true`,
   `pe_var_best 8.64e-7 > 1e-9` floor) and positive controls confirmed
   `vs_tracking_live = true` (not the degenerate constant-1.0 fallback). The claim's own
   gloss reads V_s as "cannot reliably predict outcomes" — i.e. forward-model prediction
   error. The implemented readout is a latent-*stability* proxy. 816c showed the two are
   not the same quantity in a trained encoder.

**So the question was mis-posed, not under-powered.** More seeds cannot populate an empty
subset; a harsher environment cannot lower a saturated proxy that is statistically
independent of the quantity the environment moves. The GOV-DIAG-1 reading is correct.

---

## 3. The hinge: 816c reached an answer and the chain did not consume it

This is the finding that most changes what should happen next, and it is a process
finding rather than a scientific one.

816c is the **measurement-axis leg** of the pre-registered GOV-FANOUT-1 portfolio, and it
returned a clean PASS with every positive control green and an explicit answer-label:

> `H-vs-proxy-saturation CONFIRMED: PE varies while V_s stays flat -> region-V_s decoupled
> from forward-PE -> reframe MECH-321 R1 trigger toward forward-model disagreement`

The 2026-07-26 adjudication deliberately did **not** flip the leg, on a stated condition:

> "if 816b shows env can create low-V_s regions, the proxy could still be usable, so 816c
> *narrows* but does not meet the elimination bar."

**That condition has since been tested twice and resolved against usability.** 816b
(`low_vs_produced = false`) and 816d (`low_vs_produced = false`, one dose harsher) both
returned zero low-V_s steps. The deferral's own trigger fired on 2026-07-26 and
2026-07-28 and the leg was never revisited.

Consequence, verified in `hypothesis_space_registry.v1.json` today: the question
`policy_decomposition_discrimination` (claims ARC-070 / MECH-321, `initial_frozen_count: 6`)
has **all six hypotheses still `alive` after six runs**. Every later session that opened the
registry therefore saw six live rivals and no recorded eliminations, and picked another one
to escalate. The chain partly circled because runs that *did* produce resolvable answers
were left unresolved in the ledger.

### 3b. A second structural defect in that question

The six frozen hypotheses are not one rival set. Two are about the **science**
(`H-r1-reduces-lowvs-pe`, axis `policy`; `H-r1-r5-dissociable`, axis `arbitration`).
Four are about **why we could not look** (`H-env-underdrives-uncertainty` / environment,
`H-vs-proxy-saturation` / measurement, `H-representation-axis` / representation,
`H-algorithm-axis` / algorithm).

Mixing them into one frozen set means no run can ever resolve the question: a run that
produces no occasion cannot eliminate the science legs (there is no data) and cannot
eliminate the other instrument legs either (a null on one instrument axis says nothing
about the other three). Six-alive-after-six-runs is that structure's signature, not bad
luck. **Instrument hypotheses belong in a readiness spike whose output is a working
instrument, not in the discrimination question they are supposed to make measurable.**

---

## 4. What has already been metabolized elsewhere — verified, not assumed

The chain touched three distinct sub-questions. **Two of them have since reached verdicts
through exactly the re-pose GOV-DIAG-1 prescribes**, in work that post-dates the last hit
(2026-07-30) and therefore never appeared in the audit. Verified against the registry and
the manifests today:

**(a) `decomposition_scale_heterogeneity` (from 830) — CLOSED.** 3 pre-registered
hypotheses, 3 resolved: `H-scales-dissociable-on-rollout` eliminated,
`H-slow-fires-only-with-fast` eliminated, `H-slow-never-fires-on-rollout` confirmed. A
clean 3 → 1 narrowing. 830's own autopsy explicitly refused a re-queue of 830 (§8c).

**(b) The R4 mid-execution / task-benefit branch (from 830's R4 half and 839) — CLOSED,
and closed by the re-pose this document would otherwise be recommending.** The lineage:
830 (R4 structurally unreachable) → SD-084 persistent handle built → 839 (reachability
validated, 415 evaluations) → 844 (first task-effect test; `weakens`) → 867 (bias never
engaged) → 867a (n=2, underpowered) → 867b (pool-exhausted; screen-soundness falsified) →
**919**.

V3-EXQ-919 is the re-pose, and its own load-bearing criterion states the change in one
line:

> "Over ALL measured seeds (no screen, no tiering, no post-hoc selection), the
> unconditional whole-episode mean harm signal … **Bar unchanged from 844/867/867a/867b;
> the DV and the unit of comparison are what moved.**"

It reached a verdict: C1 measured −0.0037281 against a 0.0 threshold → FAIL,
`evidence_direction: weakens`, `non_degenerate: true`, all preconditions green, n = 40
seeds, A-A null-control replicate pairs bit-identical. The registry records
`mech321_harm_aware_selection_task_effect` → `H-harm-aware-reduces-task-harm`
**eliminated**. Its autopsy (2026-08-13) routes to `/implement-substrate` **amend** and
states "Do not re-queue the magnitude-only design under a new letter."

The refusals on that branch were made at the time and are recorded here so they are not
re-litigated: **867c was refused** (2026-08-05 batch autopsy — "Refuse a same-design 867c
(bigger pool, same screen-then-match methodology)", explicitly invoking the re-derive
brake's spirit without claiming a literal firing), and **the magnitude-only re-letter was
refused** (919 autopsy, 2026-08-13).

**(c) `policy_decomposition_discrimination` — STILL OPEN, 0 of 6 resolved.** This is the
residue, and it is precisely the sub-question the chain kept re-attempting on the
environment axis. ARC-070's own `live_status` (as of 2026-08-09) says so independently:
the reading stays `candidate/v3_pending` because "the natural-prediction-failure trigger
(env-blocked, V3-EXQ-816/830) and MECH-321's task-benefit leg remain separately open."

Note what §4(b) does *not* close: 919 tested **harm-aware selection** (the
`SD-hazard-aware-policy-decomposition` mechanism). It says nothing about whether
decomposition triggered by **prediction failure** — ARC-070's actual content — helps. The
rest of this document is about that.

---

## 5. The re-operationalization

### 5a. What is actually being asked

ARC-070 asserts: *when a chunked primitive's predicted outcome is unreliable, re-segment
it into finer primitives.* The load-bearing word is **when**. The claim is a
**selectivity** claim — that decomposition *at prediction-failure loci specifically* is
better than the alternative — not a claim that decomposition is good.

Restated so a run can reach a verdict either way:

> **Does decomposition placed at high-forward-prediction-error loci produce a better
> whole-episode outcome than the same amount of decomposition placed elsewhere?**

Three things about that restatement, each fixing one identified defect:

- "the same amount … placed elsewhere" makes the comparison **rate-matched**, which is
  what isolates *selectivity* from *decomposition per se*. The old design compared
  against OFF, which cannot separate them.
- "whole-episode outcome" makes the DV **unconditional**, which is what breaks the
  no-effect / no-occasion aliasing.
- "high-forward-prediction-error loci" moves the trigger onto the construct the claim
  names, off the proxy 816c measured as saturated and decoupled.

### 5b. Trigger — rank-based, not absolute

Fire on the **top-q% of committed-chunk rollout steps by forward-model PE, ranked within
the run**, with `q` a pre-declared design constant.

This is the single change that retires the environment ladder rather than escalating it.
Occupancy stops being an outcome of the run and becomes a parameter of the design: a
quantile trigger fires on the top q% *whatever the absolute PE scale is*, so the "no
occasion" branch is eliminated by construction and no environment harshening is required.
It also removes the perverse coupling in §2(1) — a better-trained agent no longer becomes
a less measurable one.

That the signal exists at usable resolution is not an assumption; 816c measured it in
exactly the cells where V_s was flat: `pe_heterogeneous = true`, `pe_var_best 8.64e-7`
against a `1e-9` floor. The forward-PE signal has dynamic range. Only the absolute-floor
framing (`pe_elevated_floor = 0.01`) made it look unusable.

### 5c. Arms — the discriminating comparison

| arm | description |
|---|---|
| `ARM_OFF` | no decomposition — structural zero, as in V3-EXQ-904's OFF arm |
| `ARM_PE` | decompose at top-q% forward-PE loci |
| `ARM_YOKED` | decompose at the **same per-episode rate and same depth** as `ARM_PE`, at PE-uninformative loci (rate schedule taken seed-by-seed from `ARM_PE`'s realised fire times) |

**The load-bearing contrast is `ARM_PE` vs `ARM_YOKED`.** `ARM_OFF` is retained as a
manipulation check, not as the scientific comparison.

None of the six chain runs had a rate-matched control. V3-EXQ-820's ARM_2 was a different
*trigger* (R5 bottleneck) firing at its own uncontrolled rate — a different-mechanism
comparison, not a rate control — and its R1 side never fired, so the contrast was vacuous
in any case. This is a genuinely new discriminator, not a re-run.

Optionally a fourth arm, `ARM_BOUNDARY` (MECH-288 boundary trigger, rate-matched the same
way), makes `H-r1-r5-dissociable` answerable as a by-product. V3-EXQ-904 established
(2026-08-08, PASS, `supports` ARC-070) that the boundary trigger fires and drives
decomposition — 180 real MECH-288 boundary fires → 180 decompositions — so the
PE-vs-boundary contrast that was vacuous in 820 is now buildable.

### 5d. DV and power — reuse 919's shape verbatim

Unconditional whole-episode mean harm signal (with steps-to-goal / return as declared
secondaries) over **all** measured seeds: no screen, no tiering, no post-hoc
divergence-tick windowing. n ≥ 40 paired seeds as a pre-registered hard floor. A-A
null-control replicate pairs to discharge matching validity by construction.

This shape is not proposed on theory. V3-EXQ-919 ran it on this substrate and it reached a
decisive reading where four prior generations had not (`enough_seeds: true`, SE 0.02292,
`per_arm_gate.all_green: true`, `aa_control.ok: true` with `max_abs_delta: 0.0`).

### 5e. Occupancy becomes a manipulation check, never a gate

Report fires-per-episode per arm. Readiness is only the trivial existential —
`ARM_PE` fires > 0, `ARM_OFF` exactly 0, and `|rate(ARM_PE) − rate(ARM_YOKED)|` within a
pre-declared tolerance. **No `low_vs_steps ≥ N` precondition anywhere.** That precondition
is the aliasing device itself; carrying it forward would reproduce the chain.

### 5f. Pre-declared null

`ARM_PE` − `ARM_YOKED` whole-episode harm delta ≤ 0 (within 1.0 × SE over ≥ 40 paired
seeds) → **ARC-070's prediction-failure-selectivity leg is refuted at this grain.**

That null is reachable regardless of what the environment does, which is the entire point
of the re-pose. Both directions are verdicts.

---

## 6. What is REFUSED

Per GOV-DIAG-1's prescribed response, in the re-derive brake's spirit. None of these is a
literal brake firing (no target in this chain is stamped `substrate_ceiling`; counts are
0 for all three tokens), and each is recorded as spirit-not-letter.

1. **V3-EXQ-816e — and any fourth environment-axis escalation of the 816 design.**
   Evidence: 816 → 816b → 816d moved `off_pe_mean_worst` 0.0080 → 0.008594 → 0.008675,
   under 0.0007 total across two escalations, each within noise of the last, never
   reaching the 0.01 floor, with `low_vs_steps = 0` at every dose. The axis is saturated.
   This is the specific letter a session reading only the six autopsies would queue next,
   and it is refused.

2. **Any re-queue keyed on region-V_s as the prediction-failure readout** — i.e. any
   driver carrying a `vs_heterogeneity_low_vs_steps_present` readiness gate or an absolute
   `low_vs_steps ≥ N` precondition. 816c settled this on green positive controls; proxy
   saturation is not fixed by more seeds, a harsher environment, or a lower absolute
   threshold. This refusal is a **design-class** refusal, deliberately broader than a
   single letter, because the chain's next move was available under several letters.

3. **The `H-algorithm-axis` probe as pre-registered** — "re-run 816d's environment config
   with the R1 V_s-drop trigger threshold lowered". Refused **as specified**: it keeps the
   dead proxy and merely moves its absolute threshold, so it inherits defect §2(2) intact.
   Its *intent* — make the trigger fire — is absorbed in full by §5b, which achieves it on
   a readout with measured dynamic range. **This refuses the probe, not the hypothesis**;
   the leg's disposition is /governance's call (§7).

4. Already standing, recorded so they are not re-litigated: **867c** (2026-08-05),
   **re-queue of V3-EXQ-830** (830 autopsy §8c), **any new letter of the magnitude-only
   harm-aware selection design** (919 autopsy, 2026-08-13 — routes to
   `/implement-substrate` amend instead).

**Explicitly NOT refused:** `H-representation-axis` (recompute forward-PE at finer
granularity or a different normalisation). It is largely *absorbed* by §5b — a within-run
rank **is** a normalisation — and what remains of it is a legitimate variation of the
re-posed design rather than a repetition of the chain.

---

## 7. Handed to `/governance` — two ledger resolutions already earned by existing data

Not written here (this document writes no resolution, and
`hypothesis_space_registry.v1.json` is a high-contention exposed file whose Step 9b writes
belong to `/failure-autopsy` and `/governance`). Both are supported by runs already in the
corpus; neither needs a new experiment.

**(i) `policy_decomposition_discrimination` / `H-vs-proxy-saturation` → `confirmed`.**
Basis: V3-EXQ-816c, outcome PASS, all positive controls green
(`vs_tracking_live = true` — not the degenerate constant-1.0 fallback — `pe_control_ok`,
`forward_pe_varies`, `forward_pe_bounded`, `enough_paired_steps = 1654 > 30`).
`region_vs_min_over_cells = 0.9338`, `region_vs_var_best = 0.000275`,
`total_low_vs_steps = 0`, `spearman_unc_vs_pe_mean_over_cells = 0.0832` against a
`spearman_coupled_floor` of 0.2, with `pe_heterogeneous = true` and
`vs_heterogeneous = false`. The 2026-07-26 adjudication held the leg alive on the stated
condition that 816b might show the environment can create low-V_s regions; **816b and 816d
both returned `low_vs_produced = false`**, so that condition has been tested at two doses
and resolved against proxy usability. The deferral's own trigger has fired.

**(ii) `H-env-underdrives-uncertainty` → `superseded` (recommended), or `eliminated` (the
stronger reading available, flagged as a judgement call).**
The conservative recommendation is `superseded`/moot, and the reason to prefer it is
honesty about the pre-registration: 816b's and 816d's pre-registered *elimination* branch
was "forward-PE elevated but V_s flat", and neither run took it — both recorded
`pe_elevated = false` (0.008594 and 0.008675 against the 0.01 floor), so on the literal
null the runs read "dose insufficient, direction correct" and the leg stays alive. What
makes it moot rather than merely unfinished is §7(i): since V_s is decoupled from
forward-PE (spearman 0.083), raising PE **cannot** lower V_s, so even a successful future
harshening would not restore the V_s readout. The hypothesis is no longer load-bearing for
this question whatever its truth value.
The stronger reading — that the elimination branch's *spirit* obtained, since V_s did not
move by a little but not at all (`low_vs_steps = 0` at every dose) while PE did move — is
available and defensible, but it stretches a pre-registered floor after the fact, so it is
surfaced rather than recommended.

**Not resolvable, and deliberately left alive:** `H-r1-reduces-lowvs-pe` and
`H-r1-r5-dissociable`. There is no data on either — that is the whole finding. They must
be **re-operationalized** off the V_s readout per §5 rather than resolved.

**Structural recommendation (§3b):** when this question is next touched, split it — keep
the two science hypotheses in `policy_decomposition_discrimination` and move the
instrument hypotheses into a readiness spike whose output is a working instrument. A
frozen set that mixes the two cannot be resolved by any run.

---

## 8. Follow-on

- **`/queue-experiment`** — build the §5 design (rank-based PE trigger, `ARM_PE` /
  `ARM_YOKED` / `ARM_OFF`, unconditional whole-episode DV, n ≥ 40, A-A control). Chipped
  as `chip-20260814-mech321-pe-selectivity-repose`, whose STOP-CHECK requires that §7's
  ledger resolutions have been applied (or the re-pose otherwise ratified) first, so the
  build cannot race ahead of the governance call on legs that are still formally alive.
- **`/governance`** — apply §7(i) and §7(ii); consider §3b. Reported inline per the
  standing rule that governance work is not chipped.
- **Nothing else.** No substrate build is warranted by this document: the substrate fires
  the mechanism (904: 180 boundary fires → 180 decompositions; 839: 415 mid-execution
  evaluations), and the defect was in the question, not the code.

---

## 9. Marker

The `diagnostic_recurrence_metabolized` marker for these six hits is homed on
`policy_decomposition_trigger:REPOSE` in
`evidence/planning/policy_decomposition_trigger_plan.md`, created by this session because
no `*_plan.md` closure-plan node owned this work-stream — the same gap
`mech303_safety_threshold_plan.md` was registered to close on 2026-08-13, and the reason
the marker had nowhere to live. The exclusion is hit-scoped: only these six hits are
subtracted, so a **new** chain later circling ARC-070 / MECH-321 / MECH-288 re-accumulates
to N and fires again, as designed.
