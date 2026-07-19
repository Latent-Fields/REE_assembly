# Finding — why the V3-EXQ-780 behavioural prior did not install on `z_world`

**Scope:** SECONDARY finding of `failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18` (learning #7, four-layer row "Implementation: **partial — z_world 0/3 install failure**").
**Status:** confirmed, diagnosed. **Generated:** 2026-07-19T15:40:17Z.
**This note promotes and demotes nothing.** MECH-457 stays `candidate` / `v3_pending`. No claims.yaml, manifest, review_tracker, or substrate_queue edit is made here.

---

## Verdict

**Account (a) — representational-capacity — is what is MEASURED. But its stated cause is wrong, and the true cause is worse.**

The demonstrator's action classes are indeed not recoverable from the detached `z_world` latent. But this is **not** a capacity limit of a prediction-trained representation. It is that, on this code path, **the `z_world` encoder is never trained at all**. `z_world` in V3-EXQ-780 is a **frozen random projection at initialisation**.

So the honest classification is a fourth account the autopsy's (a)/(b)/(c) grid does not contain:

> **(d) The representation was never constructed.** The BC path is correctly wired and the demonstrator's observations do reach the encoder input; the encoder that was supposed to turn them into a useful latent is frozen at its random initialisation, so BC was asked to install a competent policy on top of a fixed random map.

**Consequence, stated plainly as the routing brief requires:** the `z_world` arm of V3-EXQ-780 **tested nothing**. It is uninformative about H-bc-prior *and* uninformative about `z_world` as a learned representation. It should not be read as evidence that a behavioural prior fails on `z_world`, nor that `z_world` is a poor representation. This must be fixed before any future `z_world` imitation arm is run or interpreted.

---

## 1. Evidence

### 1a. The manifest already contained the discriminator

`v3_exq_780_mech457_bc_prior_discrimination_20260718T123325Z_v3.json`, `arm_results`, per seed:

| rep | `bc_warmstart_action_match_recent` (42/43/44) | `bc_aux_action_match_recent` | `post_bc_foraging_competence` |
|---|---|---|---|
| z_world | 0.339 / 0.307 / 0.372 | ~0.28–0.29 | 0.55 / 0.40 / 0.80 |
| raw_view | 0.873 / 0.878 / 0.865 | 0.42–0.58 | 17.75 / 26.15 / 18.90 |

The failure is **upstream of behaviour**: the imitation head never learned to predict the demonstrator's action on `z_world`. This field was recorded and declared; it was simply not consumed. (Same process lesson as autopsy learning #8.)

### 1b. Account (c) — interface — RULED OUT

`resource_field_view` is a genuine slice of `world_state`, verified empirically at **offset 225** of the 250-d vector (`causal_grid_world.py:68`, `:3082`; layout 175 `local_view` + 25 `contamination_view` + 25 `hazard_field_view` + 25 `resource_field_view`). `_sense` passes `world_state` to the encoder. `LocalViewGreedyPolicy`'s own docstring asserts it reads "exactly what the REE encoder senses" — and that is true. **The demonstrator's decision variable does reach the encoder input.**

### 1c. Account (b) — BC-loss plumbing — RULED OUT

`warmstart_bc_rep` computes CE against `rep.step(state).logits`; for `z_world` that is `agent.actor_critic_step` → `action_critic.select(z.detach())`. Measured directly on the 780 path:

```
[plumbing] z_world BC loss=1.6414  total_grad_norm=0.415904
           params_with_nonzero_grad=6/8  logits_requires_grad=True
```

Gradient flows and reaches the actor trunk. The encoder's exclusion from the optimizer is **deliberate** (`cotrain_encoder=False`, the 765 retest showed co-training is destructive on `z_world`), not a mis-wiring. The BC loss is correct.

### 1d. The actual fault — the encoder is never trained (INDEPENDENTLY VERIFIED)

Snapshotting every `latent_stack` tensor before/after `fan.warmup_zworld` → `x734._train_all_on_agent`, on the **exact 780 code path**:

```
latent_stack tensors: 61
latent_stack changed: 0/61
world-path tensors: 9 -> changed: 0
  split_encoder.world_encoder.0.weight: max|delta| = 0.000e+00
  split_encoder.world_encoder.0.bias:   max|delta| = 0.000e+00
  split_encoder.world_encoder.2.weight: max|delta| = 0.000e+00
  split_encoder.world_encoder.2.bias:   max|delta| = 0.000e+00
```

**Bit-identical, not merely small.** Mechanism (already identified in `evidence/experiments/zworld_near_static_characterisation_2026-07-18.md` for the neighbouring x724/x734 configuration, and reproduced here on the 780 path specifically): the P0 loop buffers `latent.z_world.detach()`, so the gradient path terminates before `latent_stack.split_encoder.world_encoder`, which therefore receives no gradient.

This contradicts the substrate's own documentation. `make_zworld_agent` and `ZWorldRep` describe training the policy on "the **FROZEN PREDICTION-TRAINED** encoder (Stooke 2021)". It is frozen **at initialisation**, and was never prediction-trained. The docstring describes an intent the code does not implement.

### 1e. Decodability probe — how much the demonstrator is recoverable

Offline probes fit **to convergence** (400 full-batch epochs — far more gradient than BC's 300 single-pass episode updates), on 6,523 on-expert states, seed 42, held-out 20%:

| probe | test accuracy |
|---|---|
| majority-class baseline | 0.2534 |
| **z_world, linear** | **0.2805** |
| **z_world, MLP(128) converged** | **0.4146** |
| raw 5×5 view, MLP(128) — positive control | **0.9586** |
| `max(resource_field_view)` scalar only, MLP(128) | **0.2552** |

Readings:

1. **`z_world` is essentially not linearly separable** for this decision — 0.281 against a 0.253 floor.
2. **The representation, not the BC budget, is the binding constraint.** A converged MLP extracts 0.415; the run's own BC reached 0.339/0.307/0.372. BC got most of what is extractable. Even the *ceiling* is far below the 0.87 that produced competence 20.9 on raw_view. Giving BC more budget on this representation would not have installed the prior.
3. **The SD-018 supervision target is action-uninformative.** `max(resource_field_view)` alone decodes at 0.2552 — indistinguishable from majority-class. The scalar says *how close* a resource is; the demonstrator needs *which way*. Even had the encoder trained as designed, its only resource-relevant supervision (`stack.py:893`, "Maps z_world → scalar in [0,1] predicting max(resource_field_view)") carries **zero** action-discriminative information. This is a second, independent defect that would survive fixing the first.
4. Some directional signal does survive the random projection (0.415 > 0.253) — Johnson-Lindenstrauss-style residue through the `Linear(250,64) → ReLU → Linear(64,32)` bottleneck — but heavily degraded.

Point 3 also explains 781 coherently: its approach drive used `max(resource_field_view)`, precisely the scalar that *is* available, and produced approach-without-consummation — appetitive magnitude without directional commitment.

---

## 2. Campaign-wide implication

Across the 13 `competence_floor` legs carrying paired `z_world` / `raw_view` arms (742–782):

- **No `z_world` treatment arm ever cleared the 5.22 RND plateau.** Campaign maximum is 2.933 (755).
- Only **2 of 15** `z_world` treatment arms ever cleared the 1.0 competence floor.
- Every high outlier in the campaign came from `raw_view` (7.217, 11.667, and 780's 20.933 post-BC).

A representation that is a fixed random projection produces exactly this signature. **Every `z_world`-arm null in the campaign is therefore weaker evidence than it appears** — not because the mechanisms under test failed, but because the arm's representation was never constructed. This does not overturn any leg's adjudication (the eliminations rested on `raw_view` arms and on joint reads), but it means **`z_world`-arm nulls should not be cited as evidence about `z_world`**.

**Two caveats, stated rather than smoothed over:**

- **Arm reuse inflates apparent replication.** The `reuse_mint` blocks show heavy cross-leg reuse: `sparse_zw` reads 0.233 in four separate legs; `credit_ctrl_raw` and `drive_ctrl_raw` are both exactly 7.217. Legs are not independent samples; effective n is well below the nominal 31 per representation.
- **Both representations are near-floor.** `raw_view`'s median (0.550) is also below the 1.0 floor; its advantage comes from a handful of outliers, not a shifted distribution. The clean separation is at the ceiling, not the centre. The contrast is between two near-floor conditions — against a `local_view_greedy` anchor of 48.05.

---

## 3. INV-088 cross-link — CHECKED, and it does NOT hold as posed

The routing brief asked whether this is the INV-088 "z_world under-differentiation" thread surfacing in a sharper readout. **Verified, and the answer is no — it is retrodiction-compatible, not predicted.** Reasons, each checkable:

1. **INV-088's actual claim is a different claim.** `claims.yaml` INV-088 = `world_goal_evaluator_bounded_by_z_world_differentiation` — a bound on **E3 evaluator quality** (`harm_eval`/`benefit_eval` reading `z_world`). The "caps strategy diversity" framing is from the arc_062 plan header, not the claim text.
2. **Its only weighted experimental entry WEAKENS it.** V3-EXQ-744a: `mean_delta_r2=0.130`, fails the 0.15 floor + 2×SD gate with preconditions met. INV-088 is `status: candidate`, `pending_substrate_reconfirmation: true`.
3. **The corpus explicitly forbids the link.** `zworld_near_static_characterisation_2026-07-18.md` states: *"No bearing on V3-EXQ-780 vs V3-EXQ-781. Neither leg of the GOV-FANOUT-1 discrimination is supported or weakened by anything here."*
4. **Direction of dependency is the reverse of the hypothesis.** claims.yaml: *"INV-088 rides the MECH-457 competence portfolio because a validly-moving z_world-differentiation gradient requires a converter that can clear the foraging floor; until that discrimination resolves, INV-088 has no test-bed."* INV-088 is governance-**downstream** of this campaign, not upstream of it.
5. **The 750 diversity result cannot be quoted.** Its load-bearing precondition `dense_pair_matched_competent` failed (measured 0, threshold 1); `evidence_direction_per_claim.INV-088 = "unknown"`.

**What IS a genuine link:** the untrained-encoder fact is the *same substrate fact* the `zworld_near_static_characterisation` doc measured (0/61 frozen tensors, 6.7× contrast attenuation, 56% retained resource-proximity variance). This note reproduces it on the 780 path and adds a **new, sharper readout** — supervised action-decodability of a competent demonstrator (0.415 ceiling vs 0.959) — which is more direct than either the ridge-R² probes or the downstream diversity metrics. That readout is available to INV-088's antecedent leg, but it does **not** speak to INV-088's coupling leg (evaluator quality), which remains untouched.

---

## 4. Recommended substrate queue entry (NOT written to substrate_queue.json — governance applies it)

```yaml
recommended_substrate_queue_entry:
  title: z_world encoder receives no gradient under the x724/x734 P0 warmup protocol
  kind: substrate_defect
  severity: high
  blast_radius: >
    Every z_world arm in the MECH-457 competence_floor campaign (742-782) and any
    future experiment building a z_world rep via warmup_zworld / _train_all_on_agent.
  evidence:
    - "weight-delta on the V3-EXQ-780 path: latent_stack 0/61 tensors changed;
       split_encoder.world_encoder.{0,2}.{weight,bias} max|delta| = 0.0 (bit-identical)"
    - "mechanism: the P0 loop buffers latent.z_world.detach(); gradient terminates
       before latent_stack.split_encoder.world_encoder"
    - "decodability: converged MLP on frozen z_world reaches 0.415 demonstrator-action
       accuracy vs 0.959 on the raw 5x5 view, against a 0.253 majority-class floor"
    - "docstring/behaviour mismatch: make_zworld_agent + ZWorldRep document a
       'FROZEN PREDICTION-TRAINED encoder (Stooke 2021)'; it is frozen AT INIT"
  required_fix_has_two_parts:
    - part_1_gradient_path: >
        Restore a gradient path to the world encoder during P0 (prediction/forward
        objective), OR make the untrained state explicit and assert it at rep-construction
        time so no future experiment silently inherits a random projection.
    - part_2_supervision_target: >
        The SD-018 head supervises max(resource_field_view) -- a SCALAR magnitude that
        this note measures at 0.2552 action-decodability, i.e. chance. Fixing part 1
        alone would train the encoder toward an action-uninformative target. A
        directional / spatial-structure objective is needed.
  known_refuted_fix: >
    "Just enable the prescribed P0 training" is ALREADY REFUTED in-corpus: SD-070 reports
    prescribed P0 (SD-009+SD-018, dim=128) drops participation ratio 9.21 -> 1.06 and
    contrast ratio 0.1222 -> 0.0726 -- training as prescribed COLLAPSES z_world. Root
    cause is a wiring fault (transition_type is a transition property; z_world is a static
    single-frame encoding -- see sd009_event_contrastive_channel_mismatch_2026-07-18.md).
    The replacement recipe (scene-structure grounding + class-balanced CE + VICReg)
    recovers 0.137 -> 0.238, 3/3 seeds. V3-EXQ-783 already runs the
    {dim 32,128} x {untrained,trained} crossing.
  gate_on_dependents: >
    Do NOT run or interpret a z_world imitation arm until part 1 lands. Do NOT read any
    existing z_world-arm null as evidence about z_world.
  debt_class: "complicated (buildable) for part 1; complex (probe-gated) -> puzzle (known rules) for part 2"
```

---

## 5. Learning extracted

1. **The z_world arm of V3-EXQ-780 tested nothing.** Its representation was a frozen random projection. Record it as uninformative, not as a null.
2. **A docstring asserting a training regime is not evidence the regime ran.** Three separate modules described a "prediction-trained encoder" that receives zero gradient. A weight-delta assertion at rep-construction time would have caught this at 742, ten legs ago.
3. **Supervised decodability of a competent demonstrator is a sharp, cheap representation probe.** It cost ~2 minutes of CPU and separated capacity from plumbing from interface where 13 behavioural legs could not. Consider it a standing readiness check for any arm whose manipulation depends on a learned representation.
4. **A scalar-magnitude supervision target cannot teach a directional decision.** `max(resource_field_view)` decodes actions at chance. This is independent of, and survives, the untrained-encoder fault.
5. **Verify a cross-link before asserting it.** The INV-088 connection was plausible, was explicitly checked, and does not hold in the direction proposed — the corpus disclaims it and the dependency runs the other way.

---

*Diagnosed by session `blissful-hugle-5dd043` (MECH-457 780 z_world BC install-failure diagnosis). Inputs: the 780 manifest; `mech457_{fanout,explorer_classes}.py`; `ree_core/agent.py` `actor_critic_step`; `ree_core/latent/stack.py`; `causal_grid_world.py`; `zworld_near_static_characterisation_2026-07-18.md`; `claims.yaml` INV-088; the cluster autopsy. Two purpose-built verification runs (weight-delta on the 780 path; converged decodability probes) executed in scratchpad, not queued as experiments. Probe is single-seed (42); its 0.415 ceiling corroborates the run's own 3-seed BC accuracies (0.307-0.372) independently. P0 was run at 25 episodes rather than 200 in the probe, justified by the 0/61 bit-identical result: P0 magnitude provably cannot alter z_world content when the entire latent stack is frozen.*
