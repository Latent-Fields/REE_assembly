# Failure Autopsy — V3-EXQ-032/032b/032c/396a: E1/E2-self tick-omission (precedent-audit follow-on)

**Generated:** 2026-07-26T17:33:45Z
**Scope:** cluster (4 targets sharing one structural defect, discovered via a precedent audit of the V3-EXQ-826 finding in `failure_autopsy_batch-822a-826-817a-827_2026-07-26.md` §1, which flagged the `v3_exq_032` family and `v3_exq_396a` for a dedicated defect audit — this is that audit)
**Status:** confirmed (user-adjudicated via AskUserQuestion, 2026-07-26)
**Follow-on from:** session `optimistic-ellis-4357c6` (2026-07-26)

---

## Shared root cause (verified independently in this session, source-read)

`REEAgent.compute_prediction_loss()` (`ree-v3/ree_core/agent.py:8549`) hard-returns a zero-gradient stub whenever `len(self._world_experience_buffer) < 2`. That buffer is appended to **only** inside `_e1_tick()` (`agent.py:4641/4675`), itself called **only** from `act()` / `act_with_split_obs()` / `act_with_log_prob()` (`agent.py:8208/8238/8260`) — never from `sense()`.

`REEAgent.compute_e2_loss()` (`agent.py:9542`) hard-returns a zero-gradient stub whenever `len(self._e2_transition_buffer) < 2`. That buffer is appended to **only** inside `record_transition()` (`agent.py:8493-8510`), a public method none of the four scripts ever call.

All four scripts (`v3_exq_032_mech102_energy_escalation.py`, `v3_exq_032b_mech102_ttype_escalation.py`, `v3_exq_032c_mech102_dense_grid.py`, `v3_exq_396a_arc016_precision_sweep_rv_fix.py`) drive their training loop with `agent.sense(obs_body, obs_world)` + random-action selection, then call `agent.compute_prediction_loss()` + `agent.compute_e2_loss()` every step. `grep -n "record_transition\|\.act(\|act_with_split_obs\|act_with_log_prob"` across all four returns **zero matches**. So `total_loss = e1_loss + e2_loss` is unconditionally a zero-gradient tensor for the full run in all four scripts, and `optimizer.step()` on `standard_params` (`body_obs_encoder`, `world_obs_encoder`, `latent_stack`, `e1`, most of `e3`) is a structural no-op — this pipeline stays at random init from first step to last.

**This is the identical mechanism diagnosed for V3-EXQ-826** (`failure_autopsy_batch-822a-826-817a-827_2026-07-26.md` §1: "Implementation: absent (this run) — script never ticks E1 under random-action rollout... not a substrate-readiness or convergence problem — E1 itself is functional; the experiment script's driving loop never engages it"). That autopsy's own precedent check read these four scripts' docstrings citing this exact pattern as established convention, and flagged them unverified. This autopsy performs that verification and confirms the defect is present in all four.

**What is NOT broken:** in `v3_exq_032b` (and, by inspection, the sibling scripts), `agent.e2.world_forward` and `agent.e3.harm_eval_head` are trained via **separate script-local replay buffers** (`wf_data`, `harm_buf_pos`/`harm_buf_neg`) with their own dedicated optimizers, entirely independent of `compute_e2_loss()`/`compute_prediction_loss()`. These two components genuinely receive gradients and genuinely fit — which is why `world_forward_r2` measures high (0.92–0.95) despite the encoder never training. The measured `causal_sig` in each script is therefore produced by **trained heads sitting on a fixed, deterministic, random-init perceptual embedding** (`z_world`), not by the agent's intended trained perception→attribution pipeline.

---

## 1. V3-EXQ-032b — MECH-102/ARC-024/SD-003 (PRIMARY — the only target with live governance weight)

### Facts
`v3_exq_032b_mech102_ttype_escalation_20260319T054952Z_v3`. Status PASS, 5/5 criteria, `evidence_direction: supports` on all three tagged claims (MECH-102, ARC-024, SD-003). `world_forward_r2=0.9481`. `causal_sig` escalates cleanly: none `-0.0316` → hazard_approach `+0.0055` → contact `+0.0169`, `n_contact=71`. Currently **ACTIVE (non-superseded)** in `claim_evidence.v1.json`, and is 1 of MECH-102's 3 distinct-experiment `supports` entries (`genuine_exp_count=24` inflated by the claim's own documented duplicate-emission pattern; ~12 distinct real experiments; `pass_runs=3`, `exp_conf=0.411`).

Design intent (per the script's own docstring, quoting the design rationale): "With random policy, causal_sig = E3(E2(z, a_rand)) − mean_cf(E3(E2(z, a_cf)))... The escalation ladder tests whether state-level energy (ttype) predicts action-level consequentiality." The design explicitly assumes `z` (i.e. `z_world` from `agent.sense()`) is a meaningful, trained perceptual representation. It is not — it is untouched random init for the entire run.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | the intended full-pipeline test (trained perception + trained attribution) was never run; only the attribution half trained |
| Biological reference | clear | graded threat-energy escalation (approach-gradient before contact) is a well-grounded operationalisation; no biology divergence |
| Prerequisites | present | E1/E2/E3 modules and their dependencies are functional; the break is script-side wiring, not a missing mechanism |
| Implementation | partial | `world_forward` + `harm_eval_head` trained via their own local buffers/optimizers (independent of the bug); `body_obs_encoder`/`world_obs_encoder`/`latent_stack`/E1/most-of-E3 never received a gradient |
| Environment | adequate | CausalGridWorldV2's ttype split is a sound operationalisation of the energy-escalation ladder in principle |
| Measurement | confounded | `causal_sig` reflects two trained heads reading a frozen, random-init embedding — plausibly a random-features effect (a downstream model can often fit deterministic dynamics/discrimination atop a fixed random projection; cf. random-feature / random-projection literature), not evidence the full agent pipeline exhibits the escalation signature |
| Integration | isolated | trained (world_forward, harm_eval) and untrained (encoder, E1, E2-self) components coexist without ever being jointly validated |
| Scale | adequate for what was actually measured | n_contact=71 ≥ floor; the scale concern is about what was measured, not how much |

### Biological reference
Closest mechanism: graded, energy-scaled threat response (approach-gradient signalling preceding contact) — a standard predictive-processing / threat-appraisal account, well supported in the literature MECH-102 already cites. No divergence in the *design intent*; the gap is entirely at the implementation-wiring layer, identical in kind to V3-EXQ-826.

### Recommended classification
- `epistemic_category`: **`competence_implementation_gap`** (component present, not correctly coupled/trained — same category used for the structurally analogous V3-EXQ-822a finding)
- `evidence_direction`: **`non_contributory`** — does not confirm the full-pipeline claim as framed (the encoder pipeline was never exercised as intended), and does not contradict it either. Distinct from `weakens`: nothing about this result argues against MECH-102/ARC-024/SD-003, it simply never tested them under the conditions the design intended.
- **User-confirmed** (2026-07-26, AskUserQuestion): mark superseded pending a corrected re-run, per the `non_contributory` recommendation.
- `pending_retest_after_substrate`: **false** — this is not a substrate gap requiring new architecture; it is a script-wiring fix. The re-derive brake does **not** fire (R3 counts only `substrate_ceiling` readings; this is `competence_implementation_gap`).

### Draft `evidence_quality_note` (governance to apply, not written here)
> SUPERSEDED (2026-07-26, failure-autopsy V3-EXQ-032-family): V3-EXQ-032b's `standard_params` optimizer (body_obs_encoder, world_obs_encoder, latent_stack, E1, most of E3) never received a gradient for the entire run — `agent.sense()` was called instead of `act*()`/no `_e1_tick()` call, and `record_transition()` was never called, so `compute_prediction_loss()`/`compute_e2_loss()` were structurally pinned to their zero-gradient stubs (identical mechanism to the V3-EXQ-826 finding). Only `world_forward` and `harm_eval_head` trained, via separate script-local buffers, atop a perceptual embedding (`z_world`) frozen at random init. The measured causal_sig escalation ladder is real but reflects downstream-head discriminability on frozen random features, not the intended trained perception→attribution pipeline. Reclassified `evidence_direction: non_contributory`, `epistemic_category: competence_implementation_gap`. Superseded by a corrected re-run once queued (see routing below). MECH-102's remaining supports (059c, 533) are flagged for the same-signature audit — see companion note.

---

## 2. V3-EXQ-032 — MECH-102 (`weakens`, already negative)

### Facts
`v3_exq_032_mech102_energy_escalation_20260318T201910Z_v3`, FAIL, `evidence_direction: weakens`/`mixed` across duplicate-emitted entries. Uses an E3-guided (harm-minimizing) policy, split by `harm_exposure` EMA — the predecessor design 032b explicitly replaced. Its own claims.yaml note attributes the FAIL to "harm_exposure EMA operationalization does not work at harm_scale=0.02 (contact too rare for EMA to accumulate)."

### Root-cause correction
That attribution is **incomplete**: even setting the EMA/harm_scale issue aside, this script shares the identical tick-omission defect (`sense()`-only, `compute_prediction_loss`/`compute_e2_loss`, no `act*()`/`record_transition()`) — the same source-read confirms zero matches. So the FAIL is genuinely overdetermined: the policy-avoidance issue (n_high=0, documented) would have blocked a clean read even with a trained encoder, and the encoder was never trained regardless. The FAIL verdict itself does not need correcting (it is already negative and the stated cause is real), but the **evidence_quality_note should be extended** to note the shared root cause, so a future re-design doesn't fix only the EMA/harm_scale issue and assume the rest of the pipeline was sound.

### Four-layer diagnosis
Same shape as 032b's table (claim alignment unclear, biological reference clear, prerequisites present, implementation partial, environment adequate — but here compounded by the policy-avoidance confound already documented, measurement confounded, integration isolated, scale: n/a since it never reached a clean measurement window).

### Recommended classification
`epistemic_category: competence_implementation_gap` (additively, alongside the already-documented policy-avoidance issue). `evidence_direction`: leave as-is (`weakens`/already FAIL — this experiment does not carry positive governance weight to protect, and the FAIL conclusion is not undermined by the new finding, only its causal narrative is extended). No supersession needed.

---

## 3. V3-EXQ-032c — MECH-102 (`weakens`/`mixed`, already negative)

### Facts
`v3_exq_032c_mech102_dense_grid_20260319T055000Z_v3`, FAIL. Dense-grid variant of 032; same script-signature (`sense()`-only, no `act*()`/`record_transition()`) confirmed via the same grep.

### Recommended classification
Same as 032: `epistemic_category: competence_implementation_gap` added to the existing FAIL narrative; `evidence_direction` unchanged (already negative, no live governance weight at risk).

---

## 4. V3-EXQ-396a — ARC-016/MECH-093 (`non_contributory`, no live governance weight)

### Facts
Three runs, all FAIL/`non_contributory`. ARC-016's `live_status` is already anchored to a later, unaffected run (`v3_exq_818_...`); MECH-093's `live_status` already points to an unrelated 2026-05-17 autopsy. Confirmed same script signature (`sense()`-only, no `act*()`/`record_transition()`).

### Recommended classification
`epistemic_category: competence_implementation_gap` (extends the existing `non_contributory` read with the now-known mechanism). No governance action required — already carries zero live weight, and `non_contributory` is already the correct direction for a run that never exercised its intended pipeline.

---

## Cluster pattern

**Structural property, not four independent bugs.** All four scripts inherited one convention — "random-action rollout via `agent.sense()` + `compute_prediction_loss()`/`compute_e2_loss()`, no `act*()`, no `record_transition()`" — that the V3-EXQ-822a pattern (calling `agent._e1_tick(latent)` directly, and `record_transition()` for E2-self) shows how to do correctly. The convention was propagated across the `v3_exq_032` family and into `v3_exq_396a` without anyone verifying the buffer-population precondition. This is exactly the shape the V3-EXQ-826 autopsy predicted when it flagged these four scripts as an unverified precedent.

**Governance-weighted reading:** only 032b carries live governance weight (it is currently ACTIVE `supports` evidence for MECH-102/ARC-024/SD-003). 032/032c/396a are already negative/non-contributory and this finding only extends their causal narrative — it does not change their status.

---

## Newly discovered scope extension (flagged, NOT investigated to completion in this session — chipped as follow-on per user instruction)

While computing 032b's exp_conf impact, MECH-102's other two distinct-experiment `supports` entries were checked at grep-level only:

- **V3-EXQ-059c** (`v3_exq_059c_sd010_mech102_advantage_fixed.py`): confirmed `agent.sense()` calls (lines 205/373/425), confirmed `compute_prediction_loss()`/`compute_e2_loss()` calls feeding a `standard_params` optimizer (lines 157/169/305/306/312), **zero** `record_transition()`/`act*()` matches.
- **V3-EXQ-533** (`v3_exq_533_mech102_harm_stream_ablation.py`): confirmed `agent.sense()` calls, confirmed `compute_prediction_loss()` feeding `standard_params` (lines 133/135/157/162), **zero** `record_transition()`/`act*()` matches. Note: 533's PASS criteria (`voluntary_harm_rate`, `food_rate`) are measured directly from environment behaviour under a random policy, not via `causal_sig`/`world_forward`/`harm_eval` — so the *causal relevance* of the shared code defect to 533's specific PASS criteria is less obviously direct than for 032b, and needs its own read before concluding anything.

**If both are confirmed to share the defect in a governance-relevant way, MECH-102 would have zero valid positive experimental support** (all 3 of 3 `supports` entries invalidated) — a materially larger finding than what this session was scoped for. **Per user instruction (2026-07-26 AskUserQuestion), this is flagged as a chip for a dedicated follow-on failure-autopsy, not investigated further here.**

---

## Routing

**All four → `/queue-experiment`, redesign (same question, new letter), NOT `/implement-substrate`.** The fix (per the V3-EXQ-826 precedent and the V3-EXQ-822a pattern already used correctly): after `agent.sense(...)`, call `agent._e1_tick(latent)` to populate `_world_experience_buffer` and give `compute_prediction_loss()` real gradients; and call `agent.record_transition(z_self_t, action, z_self_t1)` each step to populate `_e2_transition_buffer` and give `compute_e2_loss()` real gradients — while preserving each script's random-action-selection design intent (no policy confound introduced). **User-confirmed (2026-07-26): chip this queuing as its own follow-on session rather than running `/queue-experiment` inline here**, since that skill has its own smoke-test/code-review discipline.

Re-derive brake: **did not fire** for any of the four targets (none read `substrate_ceiling`; all read `competence_implementation_gap`, which R3 excludes by design).

Granularity-debt recurrence trigger: **does not fire.** No target here reads `claim_alignment: weakened` for MECH-102 (032b reads `unclear`; 032/032c were already `weakens` for an independently-documented reason, extended not replaced). This is one script-wiring defect discovered across four sibling scripts, not recurring structurally-different FAILs against one claim.

Step 9b (frozen hypothesis-space ledger): **evaluated, skipped.** No `fanout_recommendation` is emitted (this is a single clear implementation fix, not a discrimination among live rival hypotheses), and no pre-existing `hypothesis_space_registry.v1.json` question tags MECH-102/ARC-024/SD-003/ARC-016/MECH-093 (checked directly — 0 of 12 questions match). Nothing to pre-register or resolve.

---

## Foreign TASK_CLAIMS entry swept into this session's claim-open commit

Per CLAUDE.md remedy (a): opening this session's TASK_CLAIMS claim (commit `c9df79ae9d`) carried a foreign, **complete** uncommitted claim-close entry `igw-auto-igw-209-proposal-for-arc-112-20260726T170308Z` (fields modified: `closed_at`, `completion_note`, `status` — a full close-out, not a half-write) along with it. Preserved, not reverted — surfaced here per the standing remedy.

## Uncommitted working-tree state observed (out of scope, flagged only)

At session start, `REE_assembly`'s working tree carried ~1150 lines of `git status` output unrelated to this autopsy: a diverged `master`/`origin/master` (ahead 1, behind 1), 11 files in the "staged-deletion" (`D `) HEAD/worktree-skew pattern (docs-site restructuring plus deleted `v3_exq_824` manifest/metrics/summary files), and stash entries tagged `gov-cycle-in-progress-optimistic-ellis-4357c6-153722`. This looks like an interrupted governance cycle from the session this autopsy follows on from. **Not touched, not investigated, and not part of this autopsy's scope** — flagged here so it is not lost, and so this artifact's own commit (via `ree_commit.py`'s private index) is understood to have deliberately not interacted with that state.
