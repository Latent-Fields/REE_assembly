# Failure Autopsy — V3-EXQ-687 (Q-045 / MECH-313 / MECH-260 four-arm tonic-noise / exploration-floor ablation)

- **generated_utc**: 2026-06-18T05:53:43Z
- **run_id**: `v3_exq_687_q045_mech313_mech260_4arm_tonic_noise_ablation_20260617T200433Z_v3`
- **queue_id**: V3-EXQ-687
- **machine**: ree-cloud-2
- **outcome**: FAIL → `interpretation_label=substrate_not_ready_requeue` → `evidence_direction=non_contributory` (per-claim Q-045 / MECH-313 / MECH-260 all `non_contributory`)
- **scope**: single (with explicit cluster-shape read against the sibling chains)
- **status**: confirmed (interactive gate cleared 2026-06-18; both recommended routings adopted)
- **flag adjudicated**: this is a diagnostic self-route the pipeline flagged (`substrate_not_ready_requeue`). The autopsy adjudicates whether the branch's assumption was genuinely unmet. **It was** — two of four pre-registered non-vacuity preconditions failed; the self-route correctly refused a verdict rather than emit a false `weakens`.

---

## 1. Facts — reconstruction (no interpretation)

687 IS the registered Q-045 four-arm tonic-noise / exploration-floor ablation (both-OFF / 313-only / 260-only / both-ON; ARC-062 gated-policy ON all arms) on the now-survival-competent `scaffolded_sd054_onboarding` substrate (full 603q survival config held CONSTANT across arms; only `use_noise_floor` [MECH-313] + `use_dacc`/`dacc_suppression` [MECH-260] vary). It ran to completion: all 12 cells (4 arms × 3 seeds 42/43/44) reached P2 (`reached_p2=true`, `measured_steps` 3780–5940, well above the `MEASURED_STEPS_FLOOR=100`).

**Preconditions (`manifest.preconditions`, fully populated — NOT empty):**

```
preconditions_met : false
pre_reach    : true   per_arm_reach_frac all 1.0
pre_zgoal    : true   zgoal_frac 0.75   (z_goal_norm_peak 0.379–0.514)
pre_mech260  : FALSE  per_dacc_arm_operative_frac {ARM_2: 0.0, ARM_3: 0.0}
pre_nondegen : FALSE  selected_action_entropy zero spread (constant=0, spread<=1e-9)
measured_steps_floor 100 ; z_goal_floor 0.4 ; min_fraction 0.6667
```

**Per-cell facts (all 12 cells):** `selected_action_entropy = 0.0`, `unique_actions = 1`, `reef_fraction = 0.0`, `position_entropy ≈ 1.87–2.17`. **dACC arms (ARM_2, ARM_3, all seeds):** `dacc_forward_calls_max` 2572–3909, `dacc_history_len_max = 8` (FIFO full at `dacc_suppression_memory=8`), `dacc_max_suppression = 0.0`, `mech260_operative = false`.

**Q-045 grid (read only because all preconditions held — they did NOT, so this is reported for completeness, NOT used):** every arm entropy 0.0; `both_beats_off=false`; all collapse flags false; `linear_sum_of_singleton_lifts=0.0`, `both_on_lift=0.0`.

**Expected vs observed.** Expected: a non-trivial committed-action-class entropy in ≥1 arm, with the two mechanisms either independently lifting, jointly load-bearing, or directionally coupled (the five-way Q-045 grid). Observed: every arm collapses the committed action class to a single value (`unique_actions=1`), and the dACC anti-recency channel produces exactly zero suppression. **Which criterion failed: a non-vacuity / negative-control precondition (PRE_NONDEGEN + PRE_MECH260), NOT a discrimination criterion.** The discrimination grid never ran.

## 2. Script pass/fail logic

`_interpret` (script lines 749–760): `if not pre["preconditions_met"]: return substrate_not_ready_requeue / non_contributory for all three claims`. A genuine `weakens` (`fail_no_diversity`) is reachable ONLY when **all four** preconditions hold (lines 62–63, 764–772). The four preconditions each guard a documented 603-lineage failure mode (script lines 59–74). Two of them fired. The self-route is the pre-registered safety net working as designed.

## 3. Claim-layer map (claims.yaml, current)

| Claim | status | category / phase | flags | 687 verdict |
|---|---|---|---|---|
| Q-045 | open | implementation_phase v3 | pending_retest_after_redesign | non_contributory (weights nothing) |
| MECH-313 | candidate_substrate_landed | v3, substrate_ceiling | v3_pending, pending_retest_after_redesign | non_contributory |
| MECH-260 | candidate | v3, substrate_ceiling | v3_pending, pending_retest_after_redesign, pending_retest_after_substrate (460e) | non_contributory |

Did the experiment test the claims under conditions where they could express? **No.** The substrate was monostrategy-locked, so neither MECH-313 (tonic noise) nor MECH-260 (anti-recency) could move a committed action class that was collapsed to a single value upstream of both mechanisms. An implementation/prerequisite gap, not a claim falsification. `claim_ids` are accurate (the script tests all three directly).

## 4. Biological-reference triage

- **MECH-313** = LC-NE tonic noise floor (Aston-Jones & Cohen 2005 adaptive gain). Faithful translation; substrate-landed. Biology is an existence proof for the *class*.
- **MECH-260** = dACC anti-recency / monostrategy suppression (Scholl & Klein-Flugge 2018; Kolling 2015). Faithful translation.
- The FAIL resembles what happens biologically if a **known dependency is absent**: an exploration/anti-recency channel cannot diversify behaviour when the action-selection bottleneck downstream is locked to a single committed program. The dependency is the **committed-action-diversity conversion** (the GAP-A authority→top-k-shortlist stack), not the claims themselves.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | claims never exercised; not weakened |
| Biological reference | clear | 313 (LC-NE tonic) + 260 (dACC anti-recency) faithful; substrate blocks the test |
| Developmental / dependency prerequisites | **missing** | GAP-A committed-action-diversity conversion (569i top-k stack) un-armed in `_make_config`; MECH-260 FIFO record/score decoupling under MECH-090 committed stepping |
| Implementation completeness | partial | MECH-313 present-but-non-propagating; MECH-260 wired-but-inert (`dacc_max_suppression=0.0`) |
| Environment adequacy | adequate | survival-competent 603q substrate; all cells reach P2 alive |
| Measurement adequacy | adequate | the 4 pre-registered preconditions caught the vacuity exactly as designed |
| Integration adequacy | isolated → unstable | the diversity/exploration channels do not reach the committed argmax |
| Scale / capacity | adequate | not a budget issue (12/12 cells completed) |

**Recommended `epistemic_category`: `substrate_ceiling`** (unchanged for all three) + `pending_retest_after_substrate`.

## 6. Root cause of each failed precondition

### 6.1 PRE_NONDEGEN (`selected_action_entropy=0.0`, `unique_actions=1`, all 12 cells)
The frozen-P2 policy emits a single committed action class per measured step while `position_entropy≈2.0` (it traverses varied cells on a constant action). This is the **committed-action-diversity / monostrategy lock**. 687's `_make_config` (lines 291–350) does **NOT** arm the GAP-A conversion stack: no `use_modulatory_selection_authority`, no `use_modulatory_channel_routing`, no `candidate_summary_source="e2_world_forward"`, no `use_modulatory_shortlist_then_modulate` (`mode=top_k`), no `use_e3_score_diversity`. It ran the plain SP-CEM main path (ARC-065 default), so it inherited the un-converted GAP-A ceiling by construction — the exact lock the 569i top-k-shortlist conversion (PASSED) was built to break.

### 6.2 PRE_MECH260 (`dacc_max_suppression=0.0` with full FIFO)
`DACCAdaptiveControl._suppression_penalty(c) = count(c in _action_history)/len` (dacc.py:271–282). With the executed action constant, a naive expectation is suppression `→1.0`, not `0.0`. `0.0` across all dACC seeds means the candidate classes the FIFO **scores** (`candidate_action_classes` — the fresh per-candidate first-action argmax) never match the executed class the FIFO **records** (`record_action(argmax(action[0]))`). **Most-likely mechanism (NOT line-pinned; flagged diagnose-first per the interactive gate):** the MECH-090 bistable committed-stepping latch executes a committed trajectory step (recorded) while the fresh CEM proposals scored each tick drift to a different class — so recency matches are structurally ~0 and the MECH-260 penalty never fires. This reproduces the **"MECH-260 FIFO non-operative on a call-path bypass"** failure the 687 docstring itself names (lines 18–20) from the prior 603 / 603a–e series. Wired-but-inert, not weak. Line-level confirmation is routed into the successor's diagnose-first step.

### 6.3 MECH-313 non-propagation (question 3)
`noise_floor_active=true` on ARM_1 + ARM_3, yet `selected_action_entropy=0.0` on those arms too. MECH-313 lifts the **softmax temperature**, which only affects the *uncommitted multinomial* branch and is invisible to the argmax/committed-stepping path the monostrategy-locked policy is on; a temperature lift over a class-collapsed candidate pool yields one class regardless. This is precisely the **"a non-propagating noise channel would reproduce the GAP-A `r1a_entropy_only_artefact` outcome"** the GAP-C governance note pre-registered. **PRE_NONDEGEN is the degeneracy pre-check that caught it** and refused the false `weakens`.

## 7. Cluster shape (load-bearing)

The two failed preconditions are **ONE structural property, not two independent bugs**: the *monostrategy committed-action lock*. PRE_NONDEGEN is its direct readout (committed class collapsed); PRE_MECH260 is its dACC-side consequence (committed-stepping decouples the FIFO record/score streams so anti-recency cannot fire); MECH-313's non-propagation is the same lock denying the temperature channel any committed-class authority. The same property blocks the structurally-different sibling claims:

| Experiment / node | Claim | Negative-control / non-vacuity criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-687 (this) | Q-045/MECH-313/MECH-260 | PRE_NONDEGEN, PRE_MECH260 FAIL | grid never ran | committed-action lock; tonic-noise non-propagating |
| arc_062 GAP-B (654-series) | MECH-309/ARC-062 | crf_frac_active / readiness | committed-class entropy | CRF-gate lockout → monostrategy |
| sd_037 axis-b (625d) | SD-037 axis-b | entropy non-degeneracy | committed entropy | entropy 0.0 |
| behavioral_diversity_isolation:GAP-A (569g/h) | ARC-065 | route_range / e2-divergence MET | committed-action entropy strict-above control | `conversion_ceiling_persists` |

Convergence across structurally-distinct claims = the substrate has the wiring the claims assert but does not deliver committed-action diversity at the granularity they need. The fix is the GAP-A *conversion* layer (already built; 569i top-k shortlist PASSED), not a new mechanism.

## 8. Learning extracted

- The Q-045 collapse-vs-separate question (does MECH-313 collapse into MECH-260?) **cannot be tested on a monostrategy-locked substrate** — both mechanisms are downstream of the committed-action bottleneck, so neither can express until the GAP-A conversion is armed.
- The pre-registered non-vacuity preconditions (PRE_NONDEGEN + PRE_MECH260) **did their job**: they caught a non-propagating tonic-noise channel and a non-operative dACC channel and refused a false `weakens` against Q-045/MECH-313/MECH-260.
- MECH-260 is **structurally non-operative** on the `scaffolded_sd054_onboarding` frozen-P2 committed-stepping path (`dacc_max_suppression=0.0` with a full FIFO) — the documented call-path-bypass failure, now reproduced on the survival-competent substrate.
- 687 inherited the un-converted GAP-A ceiling because its `_make_config` did not arm the 569i conversion stack — the single most actionable gap for the successor.

## 9. Repair pathway / routing (user-confirmed at the interactive gate)

**Primary routing: `queue-experiment` — a 687-successor that ARMS the 569i-validated GAP-A conversion stack** (`use_modulatory_selection_authority` + `use_modulatory_channel_routing` + `candidate_summary_source="e2_world_forward"` + `use_modulatory_shortlist_then_modulate`/`mode=top_k` + `use_e3_score_diversity`), held CONSTANT across all four arms (it is scaffolding, not what is under test — only `use_noise_floor` / `use_dacc` continue to vary), **plus a new MECH-260-operativity non-vacuity precondition**: `dacc_max_suppression > 0` on the dACC arms on ≥2/3 seeds, else self-route `substrate_not_ready_requeue` again. The conversion substrate already EXISTS and PASSED at 569i, so this is a re-arm, not a new substrate build.

**Escalation:** if the successor still shows `dacc_max_suppression=0.0` with a full FIFO, that escalates the dACC FIFO record/score decoupling to `/implement-substrate` on the MECH-090 committed-stepping bypass (the line-pinned diagnosis deferred from §6.2).

**Governance applies — no weakens, no status change.** Q-045 stays open; MECH-313 stays candidate_substrate_landed / substrate_ceiling / v3_pending; MECH-260 stays candidate / substrate_ceiling / v3_pending. 687 self-routed `non_contributory` so it weights nothing.

**Draft `evidence_quality_note` (for governance to write IF it chooses; this skill does not write it):**
> V3-EXQ-687 (Q-045/MECH-313/MECH-260 4-arm tonic-noise ablation) self-routed substrate_not_ready_requeue → non_contributory: PRE_NONDEGEN (committed selected_action_entropy=0.0, unique_actions=1 all 12 cells — the same monostrategy lock as arc_062 GAP-B / sd_037 axis-b / GAP-A) AND PRE_MECH260 (dacc_max_suppression=0.0 with a full FIFO — MECH-260 non-operative on the scaffolded_sd054 committed-stepping path) both failed. MECH-313's noise floor was active but non-propagating (temperature lift invisible to the argmax/committed path; the GAP-C r1a_entropy_only_artefact the degeneracy pre-check was built to catch). Not a falsification — 687 did not arm the 569i-validated GAP-A conversion stack. Successor re-arms the conversion stack + adds a dacc_max_suppression>0 precondition. Claims unchanged.

`recommended_substrate_queue_entry.action = none` — the GAP-A conversion substrate (modulatory-bias-selection-authority TOP-K shortlist) already exists and is validated by 569i; the residual MECH-260 operativity item is diagnose-first inside the successor, escalating to an `amend` only if it reproduces.

## 10. Routing decision the user confirmed
- **687 successor:** Re-arm GAP-A conversion stack + MECH-260 non-vacuity precondition (escalate to `/implement-substrate` on the dACC decoupling only if suppression stays 0.0 with a full FIFO).
- **MECH-260 root cause in the artifact:** stated as the most-likely committed-stepping FIFO record/score decoupling, explicitly NOT line-pinned, line-level confirmation routed into the successor's diagnose-first step.
