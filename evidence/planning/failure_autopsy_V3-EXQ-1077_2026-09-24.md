# Failure autopsy -- V3-EXQ-1077 (SD-PP-B9 H-harm-head-undertrained probe)

- **Status:** `awaiting_human_confirmation` (STAGING MODE -- drafted by a subagent of `/governance` session `governance-20260924-workset`; no claim opened, nothing committed, no index or pending_review regen, `hypothesis_space_registry.v1.json` NOT written)
- **Generated (UTC):** 2026-09-24T06:24:14Z
- **Target:** `v3_exq_1077_sdppb9_harm_head_undertrain_probe_20260923T184633Z_v3` (queue `V3-EXQ-1077`), `experiment_purpose: diagnostic`, `claim_ids: []`, `bears_on: ["mech055_harm_pe_source_validity"]`, `validates_substrate: SD-PP-B9-harm-forward-below-persistence-baseline`
- **Outcome:** FAIL, self-route `active_error_removed_AMBIGUOUS`
- **Parent:** `failure_autopsy_V3-EXQ-1062a_2026-09-23` (confirmed) -- this run is the cheapest leg (H-harm-head-undertrained) of its 4-leg GOV-FANOUT-1 portfolio on SD-PP-B9.
- **Machine / substrate:** ree-cloud-2, `linux-x86_64-py3.10-torch2.12.0+cpu`; `substrate_hash 3e6e0038...`, ree-v3 `320796d352`, clean, `substrate_stable_across_run: true`; 9042 s.

## 1. Gates run before reading metrics

| Check | Result |
|---|---|
| `check_dry_run_citations.py` over the run_id, `V3-EXQ-1077`, the 1062a run_id; `--family v3_exq_1077` | 0 dry; family = 1 real run. `dry_run_checked: true`, `excluded_dry_run_ids: []` |
| `check_autopsy_coverage.py V3-EXQ-1077 <run_id>` | not previously autopsied (AVAILABLE: YES) |
| `validate_recording.py` on the flat manifest | OK -- always-core complete (`recording_schema`, `substrate_hash`, `machine_class`, `elapsed_seconds`, full `config`, `seeds`) |
| Driver `--dry-run` reachability | not applicable -- no dry manifest in scope |

## 2. Premise audit (premises stated by the user, re-measured against the manifest)

| Premise | Re-measured | Verdict |
|---|---|---|
| (a) all three seeds converged (lr schedule exhausted, best held-out loss <= persistence) | `schedule_exhausted` 3/3, `cap_hit` false 3/3, stop 13500/12900/13400 of 40000, best held-out / persistence 0.997 / 0.939 / 0.994 | **HOLDS** |
| (b) reproduction control reproduced the online defect (persistence_dominated at eps 0.0 on >= 2/3) | ARM_ONLINE_B1 @ eps 0.0 persistence_dominated 3/3 (d -0.977 / -0.771 / -0.897) | **HOLDS** |
| (c) converged head is cannot_determine vs persistence -- not a ceiling verdict, not a refutation (declared null) of under-training | @ eps 0.1 (load-bearing): cannot_determine 3/3; driver N1 (still persistence_dominated) 0/3 | **HOLDS under the driver's grid -- QUALIFIED.** (i) The ledger's own pre-registered null for this leg, "skill stays <= 0 at convergence", is **not rejected** -- the outcome is consistent with it on 3/3 (CIs straddle 0). The two pre-registrations disagree on what the null is; "not a refutation" is true of the driver's N1 only. (ii) At eps 0.0 the converged head is persistence_dominated on s42 (d -0.0187, CI [-0.0274, -0.0115]). (iii) The removal of the ACTIVE error is not ambiguous (sec. 4); only positive skill is. The framing "removed active error only ambiguously" inverts this. |
| (d) 1077 must not be re-run or re-offered | -- | **HOLDS**; nothing below recommends it |
| (e) no absolute R2 threshold as a gate | driver gates only on d with a paired-bootstrap CI; R2s are reported, never gated | **HOLDS** |

## 3. Facts

**Design (pre-registered).** Stationary world, seeds 42/137/2026, 1062a's builders imported (driver sha256 recorded). One shared collection per seed: P0 30 eps (E1 + world-forward warmup), P1 60 eps x 90 steps = 1062a's P1 exactly (e2_harm_a online, batch 1, Adam lr 5e-4, eps 0.1), with every P1 transition banked. Two heads from the SAME init and SAME data: **ARM_ONLINE_B1** (the head P1 left) and **ARM_CONVERGED** (offline minibatch 64, lr halving vs best-so-far held-out, best checkpoint reloaded, stop at lr < 5e-4/256, cap 40000, reachability = best held-out <= persistence). Each evaluated on fresh 1800-step no-grad rollouts at eps 0.1 (matched) and eps 0.0 (1062a's condition). Instrument: `persistence_skill_gate.persistence_verdict`, d = (SSE_per - SSE_model)/(SSE_per + SSE_model), paired bootstrap 2000, 95% -- ready / persistence_dominated / cannot_determine. Routing on ARM_CONVERGED @ eps 0.1 among eligible seeds, quorum 2.

**Results.**

| seed | online eps0.1 d [CI] | online eps0.0 d | converged eps0.1 d [CI] | converged eps0.0 d [CI] | converged held-out/pers | online final snapshot on the same rows / pers |
|---|---|---|---|---|---|---|
| 42 | -0.918 [-0.926, -0.910] | -0.977 | -0.0006 [-0.0048, 0.0033] cd | -0.0187 [-0.0274, -0.0115] **pd** | 0.997 | 4.87e-5 / 1.53e-6 = **31.9x** |
| 137 | -0.687 [-0.722, -0.652] | -0.771 | +0.0023 [-0.0227, 0.0218] cd | -0.0038 [-0.0328, 0.0212] cd | 0.939 | 7.52e-6 / 1.33e-6 = **5.6x** |
| 2026 | -0.745 [-0.787, -0.702] | -0.897 | +0.0048 [-0.0039, 0.0137] cd | -0.0157 [-0.0377, 0.0032] cd | 0.994 | 8.05e-6 / 9.65e-7 = **8.3x** |

(cd = cannot_determine, pd = persistence_dominated. Eval rows at eps 0.1 / 0.0: 1776/1792, 582/313, 354/231; min 231 >= MIN_ROWS 32.)

Criteria: C1 (load-bearing, converged ready @ eps 0.1) **0/3**; driver N1 (converged still persistence_dominated) **0/3**; A1 (aliased cannot_determine) **3/3** -> `active_error_removed_AMBIGUOUS`. The ledger's registered null for this leg (skill <= 0 at convergence) is **not rejected**. N1's reachable region is narrow by construction: eligibility already requires held-out loss <= persistence on same-policy buffer rows, so N1 could fire only through a train-to-fresh-rollout generalisation failure (it did, once, at eps 0.0 on s42).

The "held-out/pers" column is the converged arm's 10% held-out split of the P1 buffer. These are the same rows the ONLINE head trained on, once each, so the last column is in-sample for the online head. The 5.6-32x figure is the online head's frozen FINAL snapshot, the thing 1062a evaluated. Its last-200-update tracking loss is lower: median 1.7-2.4x, mean 3.3-6.2x persistence.

**Non-gating readouts.**
- *In-sample bound* (fresh head from the same init, fitted with the same fitter on the eval rows themselves; permuted-delta twin as control). @ eps 0.1: s42 real ready d +0.016 [0.012, 0.020] vs twin pd -- separates; s137 real ready +0.066 [0.051, 0.081] vs twin ready +0.013 [0.002, 0.024] -- separates; s2026 real ready +0.046 [0.022, 0.068] vs twin ready +0.020 [0.002, 0.037] -- does NOT separate. The twin itself reads `ready` on 2/3 seeds even though nothing is learnable by construction, so the absolute in-sample statuses are inadmissible; only real-vs-twin separation can be read. By the driver's own pre-registered reading that gives "learnable but not learned" on 2/3 seeds: a weak signal from a same-row fit.
- *Cross-scoring*: each rollout's rows scored by the other head reproduce the swapped verdicts exactly.
- *Rollout identity across arms*: for every seed x epsilon, the ONLINE and CONVERGED rollouts have equal `sse_persistence`, `n_rows` and `n_latched_ticks` (the online head's residual SSE is 5-82x the converged head's on those rows). This is **by construction**, not an observation about the PE (sec. 7 Integration).

**Recording hygiene (cosmetic).** cannot_determine verdicts record `n_bootstrap: 0`; `persistence_skill_gate`'s `cd()` helper does not pass `len(vals)` on the CI-straddles branch. The CI is a real 2000-resample CI.

## 4. What the run established, and what it did not

1. **The sign of the 1062a defect comes from the online training protocol.** The measured ground is an in-sample pair. From the same init and the same banked data, the online head's final snapshot is 5.6-32x worse than persistence on rows it trained on, and the converged head is 0.94-1.00x on those same rows. So the active error is not a train/eval mismatch. It comes from online batch-1 Adam at lr 5e-4 on a target whose per-step MSE is ~1e-6. The run cannot tell whether optimiser noise or recency under a persistent-EMA target is the cause. On fresh matched-epsilon rollouts the online head is persistence_dominated 3/3 (CI upper <= -0.65) and the converged head is ~0. That supports the in-sample result without grounding it, because the eligibility gate largely selects where the converged head lands. This part is not ambiguous.
2. **Convergence does not produce positive skill.** C1 0/3; the ledger null "skill <= 0 at convergence" is not rejected. The converged head lands on the persistence point (R2 equal to persistence R2 to 3-4 decimals) -- the zero-delta optimum a residual head can represent.
3. **The remaining gap is aliased**, as pre-registered: a representation ceiling, a structurally wrong PE source, and "nothing to learn" all predict d ~ 0. The substrate entry's own arithmetic ("a representation ceiling on a residual head predicts skill ~ 0, not -72") now applies -- 1077's d ~ 0 is that signature, and equally the PE-source signature.
4. **The off-distribution disjunct was tested only on epsilon.** The leg reads "never converged, OR evaluated off its training distribution". The eps 0.0 residual is one seed (s42, d -0.019), 50x smaller than the online defect. The in-sample bound leans "learnable but not learned" on 2/3 seeds, consistent with a policy/state-distribution generalisation gap. Weak; recorded, not routed as a separate run.

## 5. Claim-layer map

`claim_ids: []` by design: the MECH-055 re-derive brake fired at N=2 (1062a autopsy) and refuses any V3-EXQ-1062b; that artifact's `refused_requeue_scope` exempts this probe (new EXQ, different mechanism, different DV, no claim tag). MECH-055 (candidate, `epistemic_category: standard`) is not verdicted here. No claims.yaml write is owed.

## 6. Biological-reference triage

Closest reference: dACC / anterior insula interoceptive-nociceptive prediction error against a slowly varying affective expectation. `targeted_review_connectome_mech_055` (5 entries) is present and bears directly: Hayden 2011 -- dACC carries **unsigned** surprise; Rutledge 2014 -- momentary affect is a **leaky integral over** prediction errors. REE's harm PE is the residual of a forward model **of the leaky integrator** (`z_harm_a` = encoder(EMA alpha 0.05 of proximity fields, persistent across episodes, + harm history len 10)); the fast input driving the innovation, 0.05 * (x(t) - level), is not in the head's input. Biology puts the integrator downstream of the PE. So a converged forward model of the integrator sitting at persistence is what the reference predicts. This is load-bearing for H-pe-source-structurally-wrong, not a caveat. Not a formal-definition import; no `/lit-pull` commission is owed.

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free; nothing verdicts MECH-055 |
| Biological reference | partial | integrator-downstream-of-PE ordering is reversed in REE (sec. 6) |
| Prerequisites | present | SD-PP-B9 piece 1 instrument live (ree-v3 88b1005), canary 6/6; piece 2 recording satisfied driver-locally |
| Implementation | partial (production protocol) / complete (probe) | online batch-1 Adam lr 5e-4 (E2HarmAConfig default) cannot fit a ~1e-6 target; the converged head is functional and sits at persistence |
| Environment | adequate | 1062a stationary env verbatim; rows >= 231 |
| Measurement | adequate | d + paired CI, no absolute floor, canary-pinned; `n_bootstrap: 0` cosmetic |
| Integration | coupled but inert **by construction** (missing link: neutralising default) | the head is live in the eval loop (`select_action` rolls e2_harm_a forward; the dACC PE reads it next tick). But the PE reaches candidate scores only as pe * dacc_effort_cost * candidate_effort. `candidate_effort` is trajectory length, uniform at `config.horizon` (agent.py:7789-7794), so the PE is a candidate-uniform shift. `harm_interaction` is identically 0 and `dacc_foraging_weight` is 0 in the 1062a config. Identical rollouts across the head swap were therefore the only possible outcome, and they carry no information about the PE. Inert by design for this probe; this rules out any behavioural DV for the next leg |
| Scale | adequate (optimisation) / open (data) | schedule exhausted under the cap 3/3; 2949-4113 transitions from one learning-policy trajectory |

**Failure-location (GOV-FAILLOC-1):** MECHANISM (training protocol) for the below-persistence defect; the positive-skill gap is unresolved and aliased. Measures and environment established; mechanism partial. **Not chargeable to REE.**

## 8. Recommended disposition

- `recommended_evidence_direction`: **non_contributory** (claim-free diagnostic).
- `recommended_epistemic_category`: **standard** (no suppression applies; failure mode in the note).
- Draft `evidence_quality_note` (for the manifest / evidence record, not a claim):

> V3-EXQ-1077 (claim-free diagnostic, bears_on mech055_harm_pe_source_validity; failure_autopsy_V3-EXQ-1077_2026-09-24). Under-training leg of the SD-PP-B9 fan-out. All preconditions met (reproduction control 3/3, canary 6/6, convergence 3/3). Convergence REMOVES the active error that made e2_harm_a score below persistence in 1062a (online d -0.69..-0.92 -> converged d within CI of 0 on 3/3 seeds at matched epsilon), and the online head's final snapshot is 5.6-32x worse than persistence even on rows it trained on -- so the below-persistence sign is an online batch-1 protocol artifact. Convergence does NOT produce positive skill: cannot_determine 3/3 (C1 0/3; driver N1 0/3; the registry null 'skill <= 0 at convergence' is not rejected). The remaining gap is aliased between a PE-source and a representation-ceiling reading; nothing here verdicts MECH-055. Downstream consequence: any residual-head harm PE computed from an online-trained e2_harm_a is dominated by model error; the next leg must score the residual-head PE of a CONVERGED head.

## 9. Routing (drafted; governance ratifies and chips)

**Routing: `queue-experiment`** -- the next GOV-FANOUT-1 leg, **H-pe-source-structurally-wrong** (readout axis): new EXQ number, `claim_ids: []`, `bears_on: mech055_harm_pe_source_validity`. On the same ticks, score an ensemble-disagreement PE (K converged heads, different inits, driver-local) against the residual-head PE of a converged head, with an exposure-matched baseline. Declared null: the alternative is no better separated from the VALENCE_HARM level than the converged residual-head PE. If null, the following proposal is **H-harm-head-representation-ceiling** (vary `harm_history_len` and z_harm_a per-step displacement, each setting fitted with 1077's converged fitter; DV skill-vs-persistence d), **not more training**.

**Does the evidence contradict the intended routing?** No -- biology (sec. 6) and the EMA mechanics favour testing the PE source first. But six design-audit constraints come from 1077 and belong in the PE-source leg's spec:

1. **Verdict aliasing.** Once the head sits at persistence, residual-head PE ~= raw innovation |z(t) - z(t-1)|. An "innovation-variance" source is then *not* an independent alternative. Make it a named baseline arm; the discriminating alternative is ensemble disagreement (or an input-level PE on the fast proximity field).
2. **Never compare against the online head's PE.** It is model error (1077); any alternative beats it trivially.
3. **Carry 1077's in-sample bound + permuted twin, plus a within-eval-distribution episode-split held-out fit,** as recorded non-gating readouts, so a null can be read as "nothing learnable" vs "learnable but not learned" (the undertrained leg's untested off-distribution form rides here rather than in a separate run).
4. **Record the converged head's action sensitivity** (see bears-on note 1).
5. **No behavioural DV.** Under the 1062a config the harm PE cannot change an action (sec. 7 Integration), so the DV must stay a readout.
6. **Epsilon-override mismatch.** The driver applies epsilon after `select_action`, and the agent's internal e2_harm_a rollforward uses the pre-override action. On ~10% of eps-0.1 ticks the dACC PE is therefore computed against a prediction for an action not taken. Score the studied PE from post-override pairs, or evaluate at eps 0.

Also: **H1-exposure-error-coupling** (environment axis) remains live and unrun; the PE-source leg's exposure-matched baseline touches it but does not adjudicate it. **SD-PP-B11** stays registration-only -- the ensemble in the PE-source leg is driver-local, and this autopsy does not recommend building B11. **V3-EXQ-1077 is not re-run or re-offered.** Per the skill, this autopsy does not `spawn_task` the follow-on; governance chips it after ratifying.

## 10. Recommended substrate_queue amendment (SD-PP-B9, `action: amend`)

- Append `failure_record` item: run `v3_exq_1077_sdppb9_harm_head_undertrain_probe_20260923T184633Z_v3`, `resolved: open`, `source: failure_autopsy_V3-EXQ-1077_2026-09-24`, metric and target as in the JSON.
- The 1062a `failure_record` item stays **open** (its target, skill > 0 on a curve-recorded matched-epsilon head, is still unmet). `resolves_prior_failure_record: []`.
- Mark the under-training leg **RUN** in `fanout_recommendation` (H-harm-head-undertrained: split -- (a) confirmed, (b) insufficient; next leg H-pe-source-structurally-wrong; H1 still live/unrun).
- Append to `implementation_hint`: piece (1) instrument LANDED (`experiments/_lib/persistence_skill_gate.py`, ree-v3 88b1005); piece (2) satisfied driver-locally; piece (3) under-training leg RUN, converged fitter is the required protocol for any downstream probe.
- `probe_queue_id: V3-EXQ-1077` -> completed; `experiment_queued: false` until the PE-source leg is queued.
- `severity` **unchanged (degrading)**; `substrate_paths` **unchanged** (the defect is the training protocol whose default lr lives in the already-listed `e2_harm_a.py`; the loop itself is driver-owned). `status` stays `pending_implementation` / `probe_gated`.

## 11. Bears-on notes (outside this target's scope; for governance)

1. **H3b's elimination rests on a non-converged head.** In `mech055_harm_pe_source_validity`, the 1062a autopsy SPLIT H3-persistence-dominated. Its child H3b ("head is action-blind, delta driven toward zero") was ELIMINATED on the ONLINE head's action sensitivity (0.46-1.19). 1077 shows that head was unconverged. That its action-dependence was noise is an inference, because 1077 recorded no action sensitivity for either head. The converged head sits at persistence. Recommend governance re-examine H3b's `eliminated` state. Not changed here.
2. **Out of scope, surfaced for a governance_flag decision:** with fixed-horizon candidates, `candidate_effort` is uniform in every run, so dACC's Shenhav effort term and Croxson interaction term are vacuous fleet-wide, not only here.

## 12. Hypothesis-space ledger (DRAFTED ONLY -- `hypothesis_space_ledger_pending` in the JSON)

Question `mech055_harm_pe_source_validity` (`growth_restriction` empty -- no STOP). Mode B resolve of the pre-registered leg **H-harm-head-undertrained**: recommended **split**. (a) "the online batch-1 protocol causes the active error" is **confirmed**, on the in-sample pair. (b) "convergence alone yields positive skill" is **alive / not supported**: C1 is 0/3, the registered null "skill <= 0 at convergence" is not rejected, and the driver grid calls the cell AMBIGUOUS. `control_passed` true, `non_degenerate` true, `met_elimination_bar` true (the skill's split mapping requires it; nothing is eliminated, so governance may set it false), `resolved_utc 2026-09-23T18:46:33Z`, `adjudicating_runs += V3-EXQ-1077`. Fallback if the user prefers the pre-registered grid literally: **alive** with `resolving_runs [V3-EXQ-1077]`. No new legs, no growth event, no new axis values. Mode D H-other checked: no signal fires. Basis annotations (no state change) drafted for H-harm-head-representation-ceiling, H-pe-source-structurally-wrong and H3-persistence-dominated.

## 13. Recurrence / brake checks

- **Re-derive brake:** not applicable (`claim_ids: []`). The MECH-055 brake from the 1062a autopsy is unaffected.
- **Granularity-debt trigger: does NOT fire.** `granularity_debt_cluster.py MECH-055`: 2 tagging targets (1062, 1062a), alignment distribution intact=2, no `weakened`. 1077 is untagged and adds nothing. This is measurement/implementation debt, not granularity debt.
- **GOV-DIAG-1:** 1077 is the first pure-diagnostic target carrying `bears_on: mech055_harm_pe_source_validity` (1062/1062a are claim-tagged, so they are not counted there). Chain count 1 of N=3.

## 14. Withdrawn arguments (checked and dropped)

- Reading the in-sample bound as a quorum verdict against the representation-ceiling leg: it is non-gating, fits and scores on the same rows, separates on only 2/3 seeds, and its effect sizes are small. A lean, not an elimination.
- Treating the eps 0.0 residual (s42) as evidence for the off-distribution disjunct: one seed, non-load-bearing epsilon, 50x smaller than the online defect.

## 15. Learning extracted

- Existing dependency strengthened: the 1062a defect's sign comes from the online batch-1 protocol. The online head's final snapshot is 5.6-32x worse than persistence on rows it trained on; the converged head is 0.94-1.00x.
- Implementation gap: no shared convergence-capable training protocol for e2_harm_a; every online-trained consumer gets a model-error PE.
- Measurement gap closed for this leg: skill-vs-persistence with a canary replaced the absolute R2 floor; loss curves recorded.
- Recording gap (small): converged head's action sensitivity not recorded.
- Biology divergence (load-bearing for the next leg): the PE is computed on the integrator, the reverse of the reference ordering.

## 16. Step 7b / 7c

- **7b (`autopsy_pre_routing_checks.py`, final artifact):** 1 fire. C1, C2 and C3 are inapplicable because there are no `claim_ids`, so they could not look; 7c carries the load.
  - **C7:** `persistence_heldout_loss` is bit-identical across arms. **Dismissed.** It is the persistence baseline on the converged arm's held-out buffer rows: a shared denominator, computed once per seed from the same rows for both arms, identical by design and never used as a between-arm DV. The between-arm quantities do vary: the online final snapshot is 5.6-32x persistence and the converged head is 0.94-1.00x on the same rows, and the eval d values differ.
- **7c red-team (model: fable, cross-model; drafter on Opus): CONTESTED (narrow).** Routing, severity and all three constraints (no 1077 re-run, no SD-PP-B11 build, no absolute R2 gate) survived. The red-team recomputed the 5.6-32x ratios (31.92/5.65/8.34), all 12 d values from the SSE fields, rollout identity in all 6 cells, and the 2/3 in-sample separation. Three findings, all applied:
  - **F1:** the draft wrote "declared null N1 0/3" into the ledger basis, but the ledger's registered null (skill <= 0 at convergence) is **not rejected**. Fixed everywhere; (b) now reads consistently as alive / not supported. Cheap confirmer: the registry `desc` of H-harm-head-undertrained against the converged-arm eps 0.1 CIs.
  - **F2:** "the dACC harm-PE changed no action" is true by construction (uniform `candidate_effort`, foraging weight 0), so it is not an observation. Fixed in sec. 7, removed from the severity note, and added as next-leg constraint 5. Cheap confirmer: `sed -n 7789,7794p ree_core/agent.py`.
  - **F3:** the active-error removal now rests on the in-sample pair, not on the eval-CI gap, which the eligibility gate largely selects. Fixed in sec. 4.
  - Hygiene applied: final-snapshot label, rows wording, softer mechanism wording (noise vs recency not separated), softer H3b verb, twin `ready` makes only separation admissible, epsilon-override mismatch, and the EMA's harm-event bump (`causal_grid_world.py:3080-3081`; the structural point is unchanged).
