# Failure Autopsy (Diagnostic Adjudication) -- MECH-457 retention CONFIRMS: V3-EXQ-788 + V3-EXQ-792a

**Generated:** 2026-07-25T23:10:32Z - session `competence-floor-fan-out-46b459`
**Scope:** cluster (2 diagnostic PASS-confirms, one claim/portfolio) - **Status:** confirmed (user-adjudicated 2026-07-25)
**Targets:** V3-EXQ-788 (H-retention-critic) - V3-EXQ-792a (H-retention-consolidation) - both **DIAGNOSTIC PASS**, both **excluded from scoring**, both promote/demote nothing.

> **Why this autopsy exists.** Both runs completed, PASSed, and were marked *reviewed* in `review_tracker.json` -- but neither was ever *adjudicated*: no autopsy existed and both legs stayed `alive` in the frozen ledger. That staleness is why the 2026-07-25 V3-EXQ-821 autopsy treated H-retention-critic as un-run and chipped a duplicate `/queue-experiment` (this session). "reviewed" != "adjudicated". This autopsy adjudicates both and resolves both legs (Step 9b Mode B).

---

## 1. Facts (no interpretation)

**Shared baseline (mutually corroborating).** The NON-REGRESSED reference RL refinement (raw_view, 128-wide, 3x budget, z_world detached, credit-replay 3/topk 32, bc_aux 0.5 -- NOT the 769-falsified 256/5x) erodes a BC-installed competent policy to **~half** its installed competence in **both** control arms:

| Experiment | Control arm | Control retained_fraction | Treatment | Treatment retained_fraction | Margin | Floor / arm-margin |
|---|---|---|---|---|---|---|
| V3-EXQ-788 (3 seeds) | scalar-MSE critic | **0.525** | distributional (two-hot/HL-Gauss) critic | **1.839** | **1.314** | 0.5 / 0.15 |
| V3-EXQ-792a (6 seeds) | unconstrained policy | **0.509** (drift 0.705 measured) | KL-anchor kl0p30 | **0.895** (anchor-bound, drift suppressed 0.562) | **0.386** | 0.5 / 0.15 |

Consistent with V3-EXQ-780 (raw_view competence 20.933 -> 11.667 under RL = retained ~0.557). Both runs: anchors clear the floor, BC install took, `non_degenerate: true`, retention-TRAJECTORY DV (probe every 250 ep), interpretation grid carries the mandatory `succeeded_then_decayed` branch, routes on `post_bc_foraging_competence`.

**V3-EXQ-788** -- single-knob = the value estimator only (scalar vs distributional); update rule byte-identical across arms (value term dispatched alone via `mech457_fanout.critic_value_loss`), anti-aliased vs consolidation / bc_aux / KL-anchor. Self-route `retention_critic_retains_competence` (PASS).

**V3-EXQ-792a** -- single-knob = the update constraint only (unconstrained vs KL-anchor to the installed post-BC policy, 3 doses kl0p03 / kl0p10 / kl0p30); anti-aliased vs critic / bc_aux. Supersedes V3-EXQ-792 (nondiscriminative FAIL). Self-route `retention_consolidation_protects_competence` (PASS). **Per-dose (the caveat):**

| dose | retained_fraction | margin vs control | mean policy KL | drift suppression | anchor-bound |
|---|---|---|---|---|---|
| kl0p03 | 0.814 | 0.305 | 0.810 | **-0.148** (increased) | false |
| kl0p10 | 0.580 | 0.072 (< 0.15) | 0.857 | **-0.215** (increased) | false |
| kl0p30 | **0.895** | 0.386 | 0.309 | **+0.562** | **true** |

Non-monotone: only the strongest anchor cleanly binds and suppresses drift; the load-bearing criterion (>=1 anchored arm retains AND beats margin) passes cleanly at kl0p30 (and kl0p03).

---

## 2. Claim-layer mapping

`MECH-457` (dedicated RPE-driven actor-critic policy-learning substrate; a value-baseline critic architecturally distinct from the thin bias_head REINFORCE readout). Status **candidate**, `v3_pending: true`, `epistemic_category: standard`, depends_on SD-056 / MECH-229 / MECH-459 / MECH-460 / MECH-461. Both runs are `experiment_purpose=diagnostic`, `claim_ids=["MECH-457"]` = relevance tag only -> **excluded from governance confidence/conflict scoring**. Neither changes MECH-457's status. Both **corroborate its core claim** that a value-baseline critic (and, by 792a, protection of an acquired policy) is load-bearing for competent action learning.

---

## 3. Biological-reference triage

- **788 (critic):** closest mechanism = **distributional value coding in midbrain dopamine** (Dabney/Kurth-Nelson/Uchida 2020). Real dopaminergic neurons carry a *distribution* of value predictions, not a scalar mean. The distributional critic is the **biology-faithful** translation; the scalar-MSE critic is the impoverished **formal import** -- and it is the scalar form that fails to retain. Biology SUPPORTS the confirmed mechanism.
- **792a (consolidation):** closest mechanism = **protection-against-interference / systems + synaptic consolidation** of acquired skills (motor-skill, sleep-dependent). The KL-anchor to the installed policy is a **trust-region formal translation** (EWC / policy-distillation family) of a biologically real protective function. Confirmed at strong anchoring; the non-monotone dose-response is a tuning question, not a biology divergence.

---

## 4. Four-layer diagnosis (both targets)

| Layer | 788 | 792a |
|---|---|---|
| Claim alignment | intact (corroborating) | intact (corroborating) |
| Biological reference | clear (distributional dopamine code) | clear (interference protection / consolidation) |
| Prerequisites | present (install took; anchors clear) | present (install took; anchors clear; drift measured) |
| Implementation | complete (mech457_distributional_critic) | complete (mech457_policy_kl_anchor) |
| Environment | adequate (D3 raw_view, solvable) | adequate |
| Measurement | adequate (trajectory DV, succeeded_then_decayed branch) | adequate (trajectory DV; control drift measured directly) |
| Integration | coupled + stable | coupled but **dose-sensitive** (only kl0p30 clean) |
| Scale | adequate (3 seeds, ref build) | adequate (6 seeds, ref build) |

**Dominant diagnosis (both):** clean pre-registered discrimination -> `epistemic_category = standard`. Not a ceiling, not a measurement fault, not an implementation gap in the tested mechanism.

---

## 5. Cluster read (the load-bearing output)

The competence_floor **retention** sub-portfolio (which of four loci sets the decay half-life of an installed competent policy) is now **fully resolved**, and the four legs split cleanly by axis family:

| Retention leg | axis / family | state | run |
|---|---|---|---|
| H-retention-auxiliary-decay | learning-signal / **constitution** | eliminated (weakens) | V3-EXQ-789 |
| H-consummation-binding | intrinsic-architecture / **constitution** | eliminated | V3-EXQ-821 |
| H-retention-critic | algorithm / **process** | **CONFIRMED** | V3-EXQ-788 |
| H-retention-consolidation | policy / **process** | **CONFIRMED** (caveat) | V3-EXQ-792a |

**Structural property:** the retention deficit is a **PROCESS-family** problem -- the value estimator and the update constraint each independently restore retention of the BC-installed prior (from ~0.51 to 0.81-1.84 retained_fraction) -- **not** a constitution-family one (drive architecture / auxiliary persistence do not protect). Two independent process mechanisms confirmed; two constitution mechanisms eliminated.

---

## 6. Learning extracted

1. **H-retention-critic CONFIRMED** (788): a flat/uninformed scalar critic is a retention failure mode; a distributional value estimator retains an installed policy (0.525 -> 1.839).
2. **H-retention-consolidation CONFIRMED with caveat** (792a): a KL-anchor consolidation constraint protects an acquired policy, but only at strong anchoring (kl0p30 0.895; weak/mid anchors increased drift and kl0p10 missed the margin floor).
3. **The baseline half-erosion replicates** across 788 (scalar 0.525), 792a (unconstrained 0.509) and 780 (~0.557) -- the reference RL refinement erodes the BC install to ~half, and two disjoint process fixes each restore it.
4. **Registry staleness is a coordination hazard:** 788 ran 2026-07-19/20 and PASSed, yet stayed `alive, un-run` and unadjudicated, causing the 821 autopsy to double-order it. `reviewed` (review_tracker) != `adjudicated` (autopsy + Step 9b Mode B).

---

## 7. Routing (user-confirmed 2026-07-25)

- **Adjudication:** confirm both diagnostic PASSes. `H-retention-critic -> confirmed` (788); `H-retention-consolidation -> confirmed` with recorded caveat (792a). MECH-457 unaffected (diagnostic), stays candidate / v3_pending; `epistemic_category = standard` for both.
- **Ledger (Step 9b Mode B):** resolve both legs under `competence_floor`; set `decision.decidable = true` (decidable_now) -- `decision_log_ref` stays `null` (human owns `decided`). `initial_frozen_count` unchanged (16); pre_registered_utc <= resolved_utc for both.
- **Routing:** `governance` -- the resolutions flow to the next `/governance` walk. **No substrate build** (re-derive brake = 0; 0 substrate_ceiling autopsies on MECH-457). **No same-claim re-queue.** An optional (non-blocking) dose-response refinement of the KL-anchor is a *different question* (a new EXQ if pursued), NOT a lettered re-run of 792a.
- **Duplicate-order cleanup:** the 821-autopsy chip that spawned this session asked to build V3-EXQ-822 as a "new" H-retention-critic leg -- **do not build it**; 788 already answers it. This autopsy removes the staleness that caused the double-order.

## 8. Draft `evidence_quality_note` (governance writes; this skill does not touch claims.yaml)

> MECH-457 competence_floor RETENTION sub-portfolio fully resolved (2026-07-25, diagnostics, do not score). Of four named loci setting the decay half-life of a BC-installed competent policy under continued RL: CONFIRMED (process family) -- value estimator, a distributional critic retains 1.839 vs a flat scalar critic 0.525 (V3-EXQ-788); update constraint, a strong KL-anchor to the installed policy retains 0.895 vs unconstrained 0.509 with non-monotone dose-response (V3-EXQ-792a). ELIMINATED (constitution family) -- auxiliary persistence (V3-EXQ-789), consummatory binding (V3-EXQ-821). The reference RL refinement erodes the BC install to ~half its installed competence; two disjoint process mechanisms each restore it. Corroborates MECH-457's core claim (a value-baseline critic is load-bearing); MECH-457 stays candidate/v3_pending. competence_floor retention decision is decidable_now.
