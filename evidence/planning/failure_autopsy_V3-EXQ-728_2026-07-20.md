# Failure autopsy — V3-EXQ-728 trained all-ON capability point (2026-07-20)

**Target:** `v3_exq_728_trained_allon_capability_point_20260720T155414Z_v3`
**Outcome:** FAIL · `evidence_direction: non_contributory` · `claim_ids: []` · `experiment_purpose: baseline`
**Self-route (hypothesis, not a verdict):** `substrate_not_ready_requeue`
**Scope:** single (`generate_pending_review.py` shows this as the only pending item)
**Status:** confirmed · **Routing:** `implement-substrate` → then `queue-experiment` (V3-EXQ-728a)
**Recommended epistemic_category:** `competence_implementation_gap`
**bears_on:** `ree_ai_design_critique_plan:WS-3`, `zworld_untrained_encoder_defect`

PROMOTES / DEMOTES NOTHING. `claim_ids` is empty; nothing in `claims.yaml` moves.

---

## 1. Facts

The `zworld_encoder_guard` was adopted by this driver (landed `f2e8e2f`, 2026-07-20 06:30) and fired on the `ree_trained_allon` arm:

| Measurement | Value |
|---|---|
| `world_encoder` tensors changed | **0 of 4** (max\|delta\| `0.000e+00`, bit-identical) |
| `latent_stack` tensors changed | **0 of 61** |
| `world_path` tensors changed | 0 of 6 |
| `p0_episodes` | 200 |
| seeds failed | **3 of 3** (42, 43, 44), `guard_checked: true` |
| P0 ticks actually executed | 4212 / 35280 / 3000 |

Frozen throughout: `split_encoder.world_encoder.{0,2}.{weight,bias}`.

**Env readiness was clean, so this is the encoder defect in isolation.** The greedy nearest-resource oracle cleared the competence floor at **6.333 resources/ep against a 1.0 threshold** — 6.3× — and `yardstick_discriminates` was true. There is no sparse-or-lethal-env confound to compete with the encoder explanation.

**The run was correctly not vacated.** The guard is arm-scoped: `random_walk` and `greedy_oracle` run no P0 warmup and their premise does not involve `z_world`, so both stayed green and scored; only `ree_trained_allon` was refused. `non_degenerate: true` is correct on that basis. Recording is complete — `validate_recording.py` reports the manifest **OK** with `substrate_hash` present (`77b72ca1…`), so the diagnosis is falsifiable and the arms are reuse-eligible.

Reported context, explicitly not a verdict: `trained_allon_capability_valid: false`; normalized positions `foraging -0.0247`, `goal_reach -0.08`, `planning_depth -0.2214`, `survival_horizon +5.63`. The trained arm forages **below the random-walk floor**.

**Second independent strike.** `v3_exq_728_trained_allon_capability_point.py` defines its **own** `_train_all_on_agent` copy at `:481` — this is a different driver from V3-EXQ-737a's. The defect is therefore **per-copy**, not confined to the shared `_lib` path, exactly as [`zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md`](zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md) §6c predicted for all six callers. §6d recorded that the guard had landed as a shared module but was called by **no driver** as of 2026-07-19T21:26Z; this run is the evidence that adoption now works.

**Mechanism, read from source.** `_train_all_on_agent` builds exactly three optimizer groups — `agent.e2.parameters()`, `lateral_pfc.bias_head_parameters()`, `ofc.devaluation_bias_head_parameters()` — none covering any `latent_stack` parameter, and the P0 loop buffers `latent.z_world.detach()`. No gradient can reach the world encoder. The phase is named "world-model (encoder/e2) warmup" and trains no part of the world encoder.

---

## 2. Point 1 — is the self-route `substrate_not_ready_requeue` correct?

**UPHELD, with a scope sharpening.**

The adjudication matters because the *same label* was **rejected** a week earlier: [`failure_autopsy_V3-EXQ-786_2026-07-20`](failure_autopsy_V3-EXQ-786_2026-07-20.json) found it "mislabels a test-design defect as substrate immaturity (the V3-EXQ-642 pattern)". So the label cannot be accepted on its face.

| Discriminator | V3-EXQ-786 (rejected) | V3-EXQ-728 (upheld) |
|---|---|---|
| Instrument | defective — the test design itself | **sound** — guard arm-scoped, anchors green and scored, `non_degenerate: true` |
| Env precondition | implicated | **passed independently**, oracle 6.333 vs 1.0 floor |
| Defect locatable in code | no | **yes** — three optimizer groups, none covering `latent_stack`; `z_world.detach()` in the P0 buffer |
| Independent reproduction | — | **two drivers** (737a shared-`_lib`, 728 own copy), 3/3 seeds each |
| Fix route | unknown | **confirmed** — SD-070 per the V3-EXQ-783 adjudication |
| Substrate entry | — | `sd_zworld_warmup_optimizer_group`, `ready: true`, priority 1 |

That is substrate immaturity, not test design.

**The sharpening:** "requeue" is only well-formed *after* the build lands. Routing is `implement-substrate` **first**, then a V3-EXQ-728a same-question re-run. Queuing 728a before the build reproduces this exact result.

**Category is `competence_implementation_gap`, not `substrate_ceiling`** — matching 737a. The substrate is not at its limit; it has a missing optimizer group with a known fix. This also correctly keeps the run **out of the R3 ceiling-brake count**: a broken instrument-of-training is not evidence of a ceiling, and counting it as one would invert the brake's purpose.

---

## 3. Point 2 — does the defect invalidate the 2026-07-09 capability point?

**Yes, and this is established by code archaeology rather than inference.**

`v3_exq_728_trained_allon_capability_point_20260709T224533Z_v3` is **PASS**, already in `review_tracker.reviewed_run_ids`, self-routed `trained_allon_capability_point_landed`.

Driver commit history:

| commit | date | change |
|---|---|---|
| `c83221c` | 2026-07-09 18:10 | driver created — **the 07-09 run (22:45Z) executed against this** |
| `0f153a4`, `47ed14a` | 2026-07-12 | pack_writer migration — **manifest writing only** |
| `f2e8e2f` | 2026-07-20 06:30 | guard fan-out — **detection only** |

Dispositive checks:

- `git diff c83221c HEAD -- <driver> | grep '^[+-].*torch\.optim'` → **zero changed lines**.
- `c83221c` carries the same three optimizer groups (`e2`, lPFC bias head, OFC devaluation head) at `:491/:493/:497`.
- `grep -c latent_stack` at `c83221c` → **0**. The string does not occur in that revision.
- Same `latent.z_world.detach()` at the P0 buffer (`:547`, `:605`).

So the 07-09 run's `ree_trained_allon` arm also executed on a frozen random projection. Its `trained_allon_capability_point_landed` label is **false** — no trained all-ON capability point was ever landed.

Corroboration (circumstantial, reported second): the two runs' numbers are near-identical, as expected if both measured the same untrained encoder.

| metric | 07-09 | 07-20 (guarded) |
|---|---|---|
| foraging_competence | 0.1667 | 0.1167 |
| goal_reach_rate | 0.1167 | 0.10 |
| planning_depth | 1.333 | 1.417 |
| survival_horizon | 70.48 | 66.22 |

**A compounding recording gap.** `validate_recording.py` reports the 07-09 manifest missing **six always-core fields** — `recording_schema`, `substrate_hash`, `machine_class`, `elapsed_seconds`, `config`, `seeds`. That absent `substrate_hash` is precisely why the substrate identity had to be recovered by driver-commit archaeology rather than a one-command hash comparison.

**Consequence — the finding governance can act on.** `ree_ai_design_critique_plan.md` marks **WS-3 DONE (2026-07-09)**, citing "calibration V3-EXQ-727 + TRAINED all-ON point V3-EXQ-728" and claiming the "reported alongside every all-ON run" clause closed. That clause is **not** closed. The yardstick itself (`experiments/_lib/capability_eval.py`) is built and unaffected, and the 727 calibration survives; only the trained point is void.

Recommended writes (governance applies, not this skill):
1. Set `evidence_direction: superseded` on the 07-09 manifest with the note drafted in the JSON artifact.
2. Reopen WS-3 in `ree_ai_design_critique_plan.md` — status off DONE, gated on `sd_zworld_warmup_optimizer_group`, noting what survives.

---

## 4. Point 3 — `bears_on` tagging and the GOV-DIAG-1 counter

`claim_ids: []`, so the re-derive brake and GOV-CEIL-1 — both claim-keyed — are structurally blind to this run. GOV-DIAG-1 is the only counter that can see it, and it reads `bears_on`.

Tagged: **`ree_ai_design_critique_plan:WS-3`** (this run *is* WS-3's trained all-ON capability point) and **`zworld_untrained_encoder_defect`** (the named competence-gap this chain circles). Per GOV-DIAG-1 (b), these are namespaced work-stream / competence-gap tokens, not incidental claim ids.

This target is a GOV-DIAG-1 (a) recurrence hit: confirmed, `claim_ids: []`, `non_contributory`. **Count after this autopsy: 1 of N=3. Does not fire.**

**Two prior strikes on this same defect are invisible to the counter — worth recording so the shortfall is auditable rather than silent:**

1. `failure_autopsy_V3-EXQ-737a_2026-07-20.json` is confirmed, `claim_ids: []`, `non_contributory` — **fully eligible** — but carries **no `bears_on` field**, so it contributes to no token. Recommend governance backfill `bears_on: ["zworld_untrained_encoder_defect"]` on that target, taking the token to 2.
2. The first strike, V3-EXQ-780, was written up as `zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md` — a diagnosis `.md`, not a `failure_autopsy_*.json` — so it is **outside the corpus shape** the counter reads and cannot be counted without re-homing it.

Had both been countable the token would stand at 3, i.e. at the trigger. GOV-DIAG-1 is non-falsifying-safe by design, so an untagged corpus silently reports zero.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | `claim_ids: []`, baseline, non_contributory |
| Biological reference | n/a | implementation fault, not a translation question |
| Prerequisites | **missing** | a gradient path reaching `latent_stack` + a supervision target that is not action-uninformative (SD-070 supplies both) |
| Implementation | **partial/defective** | the phase named "world-model warmup" trains no part of the world encoder |
| Environment | adequate | oracle 6.333 vs 1.0 floor, 6.3× clear |
| Measurement | adequate | the guard is what made a 3.2-hour run interpretable rather than quietly wrong |
| Integration | partially coupled | |
| Scale | **not the binding constraint** | P0 ran 4212–35280 ticks and moved zero tensors; episode count provably cannot alter this |

---

## 6. Learning extracted

- **The guard's first real dividend is a retrospective one.** Its value was argued prospectively (737a), but the larger payoff here was licensing a re-read of an already-reviewed PASS — one that had cleared review, closed a plan work-stream, and would never have re-surfaced. A detector firing on a new run should trigger an audit of every prior run on the same code path, not just adjudication of the run it fired on.
- **Code archaeology beats metric similarity for retrospective invalidation, and the order of reporting matters.** Near-identical numbers are suggestive; "zero changed `torch.optim` lines and `latent_stack` appears zero times in the older revision" is dispositive.
- **A missing `substrate_hash` converts a cheap check into an expensive one.** Six absent always-core fields turned a one-command hash comparison into an archaeology session.
- **"Substrate not ready" and "test design defective" emit the same self-route label** and must be separated by whether the *instrument* stayed sound. 786 was rejected on this label days earlier; the discriminators here were the arm-scoped guard, the independently-passing env precondition, and a defect locatable in code across two drivers.
- **A plan work-stream marked DONE on the strength of a run inherits that run's validity, and nothing re-checks it.** WS-3 went DONE citing V3-EXQ-728; when the run was invalidated 11 days later, nothing propagated.
- **An unstamped `bears_on` silently zeroes a governance counter** — and a first strike written as a `.md` rather than a `failure_autopsy_*.json` is outside the corpus entirely.

---

## 7. Routing

**Primary: `implement-substrate`** — `sd_zworld_warmup_optimizer_group` (`ready: true`, priority 1, `complicated (buildable)`). Scope includes this driver's own `_train_all_on_agent` copy at `:481`.

**Secondary: `queue-experiment` V3-EXQ-728a**, same-question alphabetic suffix, **gated on the build landing**:
- Re-run on the SD-070 training path so `ree_trained_allon` measures a *learned* `z_world`; promote the guard from a recorded precondition to a **gating** one on that arm now that a green path exists.
- Assert non-zero world-path weight delta, PR retention ~0.658, P0/P1 phase separation preserved (SD-070 per V3-EXQ-783).
- Keep the arm-scoped policy — the two anchors must stay independently scored, as they were here.

**No refusal applies.** The re-derive brake did not fire (claim-keyed, `claim_ids: []`; and the category is not `substrate_ceiling`). A 728a re-run is not a letter circling a ceiling — it is the retest the build unblocks. It must not be queued before the build lands.

**Substrate queue: `amend`, not `create`.** The entry already carries this run as its second `failure_record` (added by session `angry-gauss-b9d787`). Replace only the trailing "ADJUDICATION STILL OWED" clause with this autopsy's verdict; do **not** append a third record. Everything else in the entry is correct as written.

**Hypothesis-space ledger (Step 9b): skipped.** No `fanout_recommendation` — GOV-FANOUT-1 exempts a bottleneck routing to one unambiguous build. And the run adjudicates no pre-registered leg: its trained arm ran on a frozen random projection, so resolving any `competence_floor` hypothesis from it would misattribute an untrained-encoder measurement to a representation claim — the same reasoning 737a used to skip.

---

*Adjudicated by session `commit-push-ordering-fae508`. Inputs: the 07-20 and 07-09 728 manifests; `ree-v3` driver git history (`c83221c`, `0f153a4`, `47ed14a`, `f2e8e2f`); `failure_autopsy_V3-EXQ-737a_2026-07-20.json`; `failure_autopsy_V3-EXQ-786_2026-07-20.json`; `zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md` §6c/§6d; `substrate_queue.json:sd_zworld_warmup_optimizer_group`; `claims.yaml` GOV-DIAG-1; `ree_ai_design_critique_plan.md` WS-3; `ree-v3/validate_recording.py` on both manifests. Per CLAUDE.md, `/failure-autopsy` does not mark runs reviewed — `review_tracker.json` is left to the governance walk.*
