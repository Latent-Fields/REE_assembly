# Failure Autopsy — V3-EXQ-059c & V3-EXQ-533: MECH-102 encoder-untrained defect audit (follow-on)

**Generated:** 2026-07-26T17:40:12Z
**Scope:** cluster (2 targets, same precedent-audit lineage as `failure_autopsy_V3-EXQ-032-family_2026-07-26.md`)
**Status:** confirmed (user-adjudicated via AskUserQuestion, 2026-07-26)
**Follow-on from:** `failure_autopsy_V3-EXQ-032-family_2026-07-26.md` §"Newly discovered scope extension", which flagged both targets at grep-level only and explicitly deferred the depth-check this autopsy performs.

---

## Shared background (established by the 032-family autopsy, re-verified independently here)

`REEAgent.compute_prediction_loss()` (`ree-v3/ree_core/agent.py:8549`) hard-returns a zero-gradient stub when `len(self._world_experience_buffer) < 2`; that buffer is appended to only inside `_e1_tick()` (`agent.py:4641`), called only from `act()`/`act_with_split_obs()`/`act_with_log_prob()` (`agent.py:8208/8238/8260`) — never from `sense()`. `compute_e2_loss()` (`agent.py:9542`) is the same shape, gated on `record_transition()` (`agent.py:8493`), which neither script calls. Both scripts drive their loop with `agent.sense(obs_body, obs_world)` + random-action selection; grep for `record_transition|\.act(|act_with_split_obs|act_with_log_prob` returns zero matches in both.

**This autopsy's job was to determine whether that shared code signature is *causally load-bearing* for each script's specific PASS criteria — the depth-check the precedent audit explicitly skipped.** The answer differs sharply between the two targets.

---

## 1. V3-EXQ-059c — MECH-102/SD-010 (governance-weighted; currently one of MECH-102's 2 live `supports` entries)

### Facts
`v3_exq_059c_sd010_mech102_advantage_fixed_20260321T084609Z_v3`. Status PASS, 4/4 criteria. `claim_ids_tested: [MECH-102, SD-010]`, `evidence_direction: supports` on both. `world_forward_r2=0.954`. Contact-rate reduction: ethical policy 0.0048 vs random policy 0.0458 (~9.5x). No `substrate_hash`/`config`/`seeds`/`recording_schema` in the manifest (archival pre-recording-standard run; `validate_recording.py` confirms the always-core gap — informational only, not actionable for a run this old).

Script docstring: *"Ethical policy: argmin_{a} harm_eval_z_harm(harm_enc(harm_bridge(E2(z_world, a))))"* — the design explicitly assumes `z_world` (from `agent.sense()`) is a meaningful, trained perceptual representation.

### Source-level trace (this autopsy's contribution beyond the grep-level flag)

Read the full 670-line script (`ree-v3/experiments/v3_exq_059c_sd010_mech102_advantage_fixed.py`). Confirmed exactly which parameters receive gradients:

- `standard_params` (line 157-163): `agent.named_parameters()` minus `harm_eval_head`, `harm_eval_z_harm_head`, `world_transition`, `world_action_encoder` — i.e. `body_obs_encoder`, `world_obs_encoder`, `latent_stack`, E1, most of E3. Optimized only inside `if total_loss.requires_grad:` (line 308), where `total_loss = agent.compute_prediction_loss() + agent.compute_e2_loss()` (line 305-307). Per the established defect, this is always a zero-gradient stub — **`optimizer.step()` for `standard_params` never actually executes for the entire run.**
- `agent.e2.world_transition` + `world_action_encoder` (`world_forward_params`, line 164-167): trained via a **separate** `world_forward_opt`, fed by a script-local `wf_data` buffer built from `z_world_curr = latent.z_world.detach()` (line 207, explicitly `.detach()`-ed — frozen by design in this script, not just incidentally frozen by the bug). MSE against the actual next-state `z_world`. Genuinely trained; R²=0.954 confirms it.
- `harm_bridge` (`nn.Linear(world_dim, HARM_OBS_DIM)`, line 141): a **standalone module, not part of `agent` at all**. Trained via its own `harm_bridge_opt`, MSE-regressing `z_world_curr` (frozen) against the actual `harm_obs` vector (line 256-265). Genuinely trained.
- `harm_enc` (`HarmEncoder`, line 140): also standalone. Trained via `harm_enc_opt` jointly with `agent.e3.harm_eval_z_harm_head` (via `harm_z_harm_opt`) on a stratified buffer of normalized hazard-proximity labels (line 282-298, confirmed `.step()` calls on both optimizers).

**The eval-time "ethical" policy (line ~373-404) computes `z_world` from `agent.sense()`, then for each candidate action runs `agent.e2.world_forward(z_world, a)` -> `harm_bridge` -> `harm_enc` -> `agent.e3.harm_eval_z_harm_head`, and picks `argmin`.** Every one of the four downstream modules is genuinely, separately trained via direct supervised MSE losses against ground-truth environment quantities. The only frozen link in the chain is `z_world` itself — literally random init for the entire run, since `standard_params` never receives a gradient.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | the intended full-pipeline test (trained perception + trained attribution) was never run; the design's own docstring assumes z_world is a meaningfully-trained representation |
| Biological reference | clear | approach-gradient harm avoidance (avoidance leverage before contact, not at contact) is a well-grounded operationalisation; no biology divergence |
| Prerequisites | present | E1/E2/E3 and SD-010's HarmEncoder separation are functional; the break is script-side wiring |
| Implementation | partial | four downstream modules (world_forward, harm_bridge, harm_enc, harm_eval_z_harm_head) trained via genuine supervised losses on a **frozen** z_world; body_obs_encoder/world_obs_encoder/latent_stack/E1 never received a gradient |
| Environment | adequate | CausalGridWorldV2's hazard/resource layout is a sound operationalisation in principle |
| Measurement | confounded | the 9.5x contact-rate reduction is a real, robust effect **of four supervised auxiliary heads composed on a frozen embedding** — a demonstration that supervised approach-avoidance control can be built on top of an untrained encoder, not that REE's intended self-supervised E1/E2-self representation-learning pathway produces this behaviour |
| Integration | isolated | trained (world_forward/harm_bridge/harm_enc/harm_eval) and untrained (encoder/E1/E2-self) components coexist without ever being jointly validated |
| Scale | adequate for what was measured | n_contact=95 (ethical eval) well above the C4 floor of 10 |

### Biological reference
Same as 032b's: graded approach-gradient threat avoidance, well supported by the predictive-processing / threat-appraisal literature MECH-102 already cites. No divergence in design intent; the gap is entirely implementation-wiring, and — unlike 032b's passive `causal_sig` readout — here it is directly load-bearing on the actual **behavior-selecting** policy, which makes the result more architecturally interesting (a real engineering demonstration) but *less* informative about MECH-102's specific mechanism (violence/harm-avoidance emerging from the agent's own experientially-trained world model), since that mechanism was never engaged.

### Recommended classification (user-confirmed)
- `epistemic_category`: **`competence_implementation_gap`** (identical category to 032b — component present, not correctly coupled/trained)
- `evidence_direction`: **`non_contributory`** — does not confirm the full-pipeline claim as framed (the perceptual pipeline was never exercised as intended) and does not contradict it either.
- Mark **superseded** pending a corrected re-run (same routing precedent as 032b).
- `pending_retest_after_substrate`: **false** — script-wiring fix, not a substrate gap. Re-derive brake does **not** fire (R3 counts only `substrate_ceiling`; this reads `competence_implementation_gap`).
- **SD-010 is NOT implicated.** SD-010's own claim (dedicated HarmEncoder pathway separate from z_world) is validated by other runs (EXQ-058b, EXQ-056c) that train HarmEncoder directly from `harm_obs`, independent of this script's z_world-freezing defect. 059c's SD-010 tag reflects reuse of an already-validated component inside a MECH-102 test, not fresh SD-010 evidence — SD-010's `status: implemented` is unaffected.

### Draft `evidence_quality_note` (governance to apply, not written here)
> SUPERSEDED (2026-07-26, failure-autopsy V3-EXQ-059c-533): V3-EXQ-059c's `standard_params` optimizer (body_obs_encoder, world_obs_encoder, latent_stack, E1, most of E3) never received a gradient for the entire run — identical mechanism to V3-EXQ-032b/826 (`agent.sense()` only, no `act*()`/`_e1_tick()`/`record_transition()`). The eval-time "ethical" action-selecting policy (argmin harm_eval_z_harm(harm_enc(harm_bridge(E2(z_world,a))))) is computed entirely from this frozen z_world, piped through four separately/genuinely-trained supervised modules (world_forward R2=0.954, harm_bridge, harm_enc, harm_eval_z_harm_head). The measured 9.5x contact-rate reduction is real but demonstrates that supervised auxiliary heads composed on a frozen embedding can produce hazard-avoidance behaviour, not that REE's intended self-supervised E1/E2-self pathway does. Reclassified `evidence_direction: non_contributory`, `epistemic_category: competence_implementation_gap`. SD-010 is not implicated (its own supporting runs, EXQ-058b/056c, train HarmEncoder directly from harm_obs, independent of this defect). Superseded by a corrected re-run once queued (folded into the existing 032-family `/queue-experiment` follow-on).

---

## 2. V3-EXQ-533 — MECH-102 (already scoring-excluded; structurally different finding)

### Facts
`v3_exq_533_mech102_harm_stream_ablation_20260506T094157Z_v3`. Status PASS (C1: arm1_vhr <= arm0_vhr*1.2 TRUE; C2: arm1_food >= arm0_food*0.7 TRUE). `experiment_purpose: "diagnostic"`. `claim_ids: [MECH-102]`.

Script docstring is explicit about intent: *"NOTE: MECH-102 has epistemic_category=substrate_ceiling. This experiment probes the V3 approximation... NOTE: We do NOT expect harm_rate to strictly decrease in V3 (substrate ceiling). Primary outcome is diagnostic: documents V3 substrate ceiling for MECH-102... evidence_direction_per_claim: {"MECH-102": "does_not_support"} is the expected outcome."* Manifest's own `note` field: *"MECH-102 substrate_ceiling diagnostic... Expected: no strong effect."*

### Source-level trace

Read the full 274-line script (`ree-v3/experiments/v3_exq_533_mech102_harm_stream_ablation.py`). Confirmed the same code signature the precedent audit flagged: `agent.sense(obs_body, obs_world[, obs_harm])` (line 133/135), `compute_prediction_loss()` feeding `optimizer` (the full `agent.parameters()`, line 157-162), zero matches for `record_transition`/`act*`. So the encoder pipeline is confirmed never-trained here too.

**But the action-selection line (139) is `action_idx = np.random.randint(0, env.action_dim)` — literally independent of `latent` (the `agent.sense()` output), of `z_world`, and of `use_harm_stream`.** The `latent` variable is computed every step (line 133/135) but never read again — it is dead code with respect to behaviour. Both arms (`ARM_0_no_harm_stream`, `ARM_1_harm_stream`) construct the identical `CausalGridWorldV2` with identical params, run under the identical seeded (`torch.manual_seed(seed); np.random.seed(seed)`) uniform-random policy, and differ *only* in an observation channel (`obs_harm`) that is fed into an agent pipeline whose output is never consulted for any decision.

**Consequence: the encoder-untrained defect is present but causally irrelevant to C1/C2.** `voluntary_harm_rate`/`food_rate` are determined entirely by environment-level hazard/resource layout under uniform-random actions, blind to any agent internal state (trained or not). The small observed arm0/arm1 differences (vhr 0.7978 vs 0.7990; food_rate 4.575 vs 4.408) are most plausibly attributable to RNG-stream perturbation from the differently-sized agent construction under `use_harm_stream=True` vs `False` desynchronising the shared global RNG before the `np.random.randint` draws — the same class of confound previously diagnosed and fixed in `v3_exq_141d_mech111_novelty_drive_rng_desync`. This was not chased to a definitive proof (it does not change the routing), but it is the most likely explanation for the criteria being anything other than bit-identical between arms, and it reinforces (rather than undermines) the conclusion that the measured "effect" carries no MECH-102-relevant signal.

### The scoring-weight finding (distinct from, and more consequential than, the encoder-defect question)

`REE_assembly/evidence/experiments/claim_evidence.v1.json` line ~114632: this entry already carries **`"scoring_excluded": "diagnostic_probe"`**, set by `build_experiment_indexes.py` because `run.experiment_purpose in ("diagnostic", "baseline")` (line ~2328) — this `continue`s *before* the entry is ever appended to `claim_to_entries[claim_id]`, so **V3-EXQ-533 contributes ZERO weight to MECH-102's `pass_runs`/`exp_conf`/`genuine_exp_count` right now, regardless of today's finding.** Verified directly: `matrix["claims"]["MECH-102"].genuine_exp_direction_counts.supports == 3` is fully accounted for by 059c (1) + 032b's known duplicate-emission (2 entries, same underlying run) — **533 was never one of the 3.** claims.yaml's own SUBSTRATE-CEILING FLAG note (2026-05-02) independently corroborates this: *"only EXQ-032b (ttype) and EXQ-059c (advantage_fixed) PASSed"* — 533 is not named among the claim's own documented supporting runs.

However, the raw per-entry `evidence_direction` field for this (already-excluded) entry is **mechanically tagged `"supports"`** with `"confidence_rationale": "PASS with supporting direction"` — the indexer's blind status-to-direction mapping for a PASS, applied without regard to the script's own explicit `evidence_direction_per_claim` declaration or the manifest's stated diagnostic intent. This mislabeled tag is what `claims.yaml`'s MECH-102 `live_status.evidence` block currently cites verbatim:
```yaml
live_status:
  evidence:
    from: v3_exq_533_mech102_harm_stream_ablation_20260506T094157Z_v3
    as_of: 2026-05-06
    verdict: supports/PASS
```
This is the single most governance-visible (dashboard-facing) evidence pointer for MECH-102 right now, and it is inaccurate relative to the experiment's own stated design and result interpretation — even though it carries zero scoring weight.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (uninformative, not weakened) | policy is blind to any agent state by construction; the run cannot discriminate for or against MECH-102 |
| Biological reference | n/a | no policy mechanism is being tested; this is an environment-level baseline-disruption check |
| Prerequisites | present | irrelevant to the result, since the defect never reaches the measured metric |
| Implementation | absent (for what the docstring frames as the test) | encoder never trained, AND the policy never reads its output regardless |
| Environment | adequate | identical between arms by design |
| Measurement | near-vacuous | C1/C2 are structurally almost incapable of failing given a uniform-random, agent-state-blind policy; any observed difference is plausibly RNG-stream noise, not a "harm stream" effect |
| Integration | n/a | no integration is exercised |
| Scale | n/a | 3 seeds/arm is fine for what is actually a near-deterministic environment-only comparison |

### Recommended classification (user-confirmed)
- **No supersession, no evidence_direction reclassification for scoring purposes** — the entry already carries zero weight (`scoring_excluded: "diagnostic_probe"`).
- **Label-accuracy correction recommended** (informational, not a governance-weight action): correct the per-entry `evidence_direction` from `"supports"` to `"does_not_support"` (or `"non_contributory"`) to match the script's own declared `evidence_direction_per_claim` and the manifest's stated intent, and update MECH-102's `live_status.evidence` block to stop citing this run as `"supports/PASS"` anchor evidence, or if it remains the most recent evidence pointer, correct its verdict text to reflect what the run actually shows (a near-vacuous, policy-blind baseline check, not a supporting behavioural result).
- Recommended `epistemic_category` if governance wants to formalize the diagnostic's own reading: **`vacuous_pass`** or **`measurement_test_design_defect`** (a permissive criterion that cannot meaningfully fail given the policy design) — **not** `competence_implementation_gap` (that category implies the defect reaches the result; here it doesn't).

### Draft note (governance to apply, not written here)
> LABEL CORRECTION (2026-07-26, failure-autopsy V3-EXQ-059c-533): V3-EXQ-533's action selection (`np.random.randint`) is independent of `agent.sense()`'s output by construction — the sensed latent is never consulted for behaviour, so neither the confirmed encoder-untrained defect (agent.sense()-only, no act*()/record_transition()) nor `use_harm_stream` itself can causally affect `voluntary_harm_rate`/`food_rate`. The run's own docstring declares its expected result as `does_not_support` and its manifest note frames it as documenting a substrate ceiling; the entry's mechanical `evidence_direction: "supports"` tag (from the indexer's PASS-to-supports default) contradicts this. The entry already carries `scoring_excluded: "diagnostic_probe"` and so has zero weight in MECH-102's exp_conf/pass_runs — this is a labeling-accuracy fix, not a scoring change. Recommend correcting the tag to `does_not_support` and updating MECH-102's `live_status.evidence` pointer, which currently cites this run as "supports/PASS."

---

## Governance-relevant correction to this session's own framing (user-confirmed to state explicitly)

The task that opened this autopsy assumed MECH-102 has **3** distinct-experiment `supports` entries (032b, 059c, 533) that could all be invalidated. That framing is not quite right, and the correction matters for anyone re-deriving this later:

- **533 was never a scored `supports` entry.** It has carried `scoring_excluded: "diagnostic_probe"` since it was indexed (`experiment_purpose: "diagnostic"`), so it contributes nothing to `pass_runs=3` / `exp_conf=0.411` / `genuine_exp_count=24` regardless of anything found in this autopsy.
- **The `pass_runs=3` / `genuine_exp_direction_counts.supports=3` figure is fully explained by just 2 distinct experiments**: 032b (counted **twice** due to the claim's own already-documented duplicate-emission pattern — two differently-formatted `run_id` strings for the same underlying run) + 059c (once). claims.yaml's own 2026-05-02 SUBSTRATE-CEILING FLAG note independently confirms this: *"only EXQ-032b (ttype) and EXQ-059c (advantage_fixed) PASSed."*
- **Net effect is nonetheless the same magnitude of finding the task anticipated, via a different mechanism**: 032b is already recommended for `non_contributory` reclassification (prior autopsy, pending governance application) and this autopsy now recommends the same for 059c. Applying both would leave MECH-102 with **zero** remaining `supports` entries among its 24 `genuine_exp_count` entries (currently 11 `weakens` + updated `mixed` counts, 0 `supports`) — i.e., MECH-102 would indeed have zero valid positive experimental support, just from 2 reclassifications rather than 3, since 533 was inert from the start.
- 533's contribution to this session is a **different, real finding**: a mislabeled evidence-direction tag on an already-excluded diagnostic entry, which happens to be the claim's current `live_status.evidence` anchor — worth fixing for dashboard accuracy, independent of the scoring question.

---

## Cluster pattern

**Not one structural property here — two distinct findings sharing a superficial code signature.** 059c shares 032b's exact failure mode (frozen z_world load-bearing on the measured result via trained downstream heads) and gets the identical disposition. 533 shares only the *code signature* (agent.sense()-only, no act*()/record_transition()) but the defect is proven causally inert for its specific criteria, because its policy never reads the sensed latent at all — a materially different (and in this case less consequential) finding. The two should not be narrated as "the same bug hit both" without this distinction; doing so would have led to over-crediting 533 as invalidated evidence when it was already worth zero.

---

## Routing

- **059c → `/queue-experiment` redesign (same question, new letter), folded into the existing 032-family follow-on chip** (per user instruction): the fix is identical — after `agent.sense(...)`, call `agent._e1_tick(latent)` and `agent.record_transition(...)` each step, preserving the random-action training design intent, while keeping the "ethical" eval policy's argmin structure unchanged. One redesign session can cover 032/032b/032c/396a/059c together since they share one root cause and one fix.
- **533 → no re-queue.** The diagnostic already documents what it set out to document (a permissive, policy-blind baseline check); the fix needed is a **label correction** in `claim_evidence.v1.json`/`claims.yaml`, not a re-run. Flagged to governance, not `/queue-experiment`.

**Re-derive brake**: did not fire for either target. 059c reads `competence_implementation_gap` (R3 excludes non-`substrate_ceiling` categories). 533 reads `measurement_test_design_defect`/`vacuous_pass`-adjacent, also excluded by R3.

**Granularity-debt recurrence trigger**: checked via `granularity_debt_cluster.py MECH-102` — 3 targets (032, 032b, 032c) currently tagged, alignment distribution `unclear=3`, **no target reads `weakened`** → does not fire (confirmed by the tool, matching the 032-family autopsy's own conclusion). Adding 059c (`unclear`) does not change this: still implementation debt, not granularity debt.

**Step 9b (frozen hypothesis-space ledger)**: evaluated, skipped. No `fanout_recommendation` (single clear implementation-gap diagnosis for 059c; label-only fix for 533, not a discrimination among rival hypotheses). Checked `hypothesis_space_registry.v1.json` directly: 0 of 12 questions tag MECH-102 or SD-010. Nothing to pre-register or resolve.

---

## Follow-on chip

Per user instruction, 059c's redesign fix is folded into the existing 032-family `/queue-experiment` follow-on (spawned by the prior session `optimistic-ellis-4357c6` / this session's predecessor autopsy). This session additionally spawns a chip covering the label-correction for 533 and the `live_status.evidence` pointer fix, since that is a distinct governance-application task the prior chip does not cover.
