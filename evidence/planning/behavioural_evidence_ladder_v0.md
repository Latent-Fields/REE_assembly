# Behavioural Evidence Ladder v0

**Status:** v0, curated 2026-08-27. Derived from the reviewed evidence record, not from claim
status fields or from memory.
**Source of truth used:** `evidence/experiments/review_tracker.json` (2854 reviewed run ids,
last review 2026-08-25T18:42:08Z) + the flat run manifests in `evidence/experiments/`.
`claim_evidence.v1.json` (generated 2026-08-26T19:46:18Z; 5668 entries over 565 claims) was used
only to *enumerate* candidate runs; every entry below was then read from its own manifest.
**Motivating request:** `docs/thoughts/2026-08-27_developmental_integration_and_readiness_programme.md`
section 18.4.

---

## The claim this document is making

> **REE already exhibits genuine behaviour and causal mechanism effects; REE has not yet
> demonstrated robust, accumulating, general organism-level competence.**

Both halves are load-bearing. Rungs 1 and 2 below are populated with real, matched-control,
multi-seed results. Rungs 3, 4, 6 and 7 are **empty**, and rung 5 holds one component-level
result only. The empty rungs are reported as findings, with the specific runs that attempted
them and the specific reason each fell short — not as a to-do list.

This is not a marketing document and it is not a confession. It is a map of where the evidence
actually reaches.

---

## How to read a rung

Rungs are in increasing order of what they license you to say about the *organism*:

| Rung | Claim licensed | Populated? |
|---|---|---|
| 1 | Mechanism bites — a targeted manipulation moves the predicted variable | **Yes — 5 entries** |
| 2 | Behavioural competence — meaningful task above a matched baseline | **One, provisional** |
| 3 | Flexible competence — behaviour changes appropriately after a rule/goal change | **Empty** |
| 4 | Developmental acquisition — a capability appears through experience | **Empty** |
| 5 | Retention / generalisation — survives time/offline integration, transfers | **One, component-level** |
| 6 | Integrated organism competence — several faculties working together | **Empty** |
| 7 | Independent reproduction | **Empty** |

---

## Three corpus-wide caveats that apply to EVERY entry

These are properties of the evidence base, not of any single run. They are stated once here
rather than repeated eleven times below.

### C1. No run on this ladder can name the organism it tested.

The canonical-profile mechanism exists — `docs/architecture/canonical_profiles/ree_v3_baseline.json`,
schema `canonical_profile_freeze/v1`, frozen 2026-08-12T16:19:41Z. But its only version, `v0`,
carries `"overrides": {}` and its own description reads "Placeholder canonical profile -- the
mechanism only, zero admitted overrides."

Measured 2026-08-27: **zero manifests in `evidence/experiments/` reference a canonical profile
at all.** Every experiment on this ladder assembled its own flag bundle. So "REE-v3" as it
appears in each row below denotes a *script-specific instantiation*, and two rows are not
guaranteed to be the same organism. This is the single largest obstacle to reading the ladder
vertically — you cannot currently assume rung-1 mechanism X and rung-2 competence Y were
demonstrated in the same animal.

What *is* recoverable per run varies, and the ladder is honest about which:

| Provenance grade | What is recorded | Entries |
|---|---|---|
| **Full** | `substrate_commit` (+ clean/dirty) + `substrate_hash` + `machine_class` | 948, 926a, 829a, 888 |
| **Partial** | `substrate_hash` + `machine_class`, no commit | 832, 757, 728b |
| **Weak** | none of the three | 614a, 603q, 691, 485m |

A "weak" row can be re-run but cannot be re-run *against the substrate it actually tested*.

### C2. Every experimental evidence entry in the corpus is `evidence_level: C`.

Of 5668 index entries, 2612 are experimental and **all 2612 are level C**; there is no level-A
or level-B experimental evidence anywhere in the record. Nothing on this ladder is a
higher-grade result being under-reported.

### C3. GOV-PATHVALID-1 applies, and it disqualifies more than it looks like it should.

`GOV-PATHVALID-1` (`docs/claims/claims.yaml`, status `candidate`, registered 2026-08-25):

> A load-bearing positive control ... must traverse the production path it claims to validate.
> Directly injecting or mocking the state immediately downstream of a suspected causal edge can
> certify that a downstream consumer works GIVEN that state, but cannot certify that the
> production organism can reach that state via its own endogenous pathway.

Applied to this corpus, that rule separates two things a casual reader would merge: a mechanism
characterised on a **harness-supplied input stream** (a component test) from a mechanism
exercised on **state the organism itself produced**. Both are legitimate science. Only the
second says anything about the organism. Each entry below carries an explicit
**production-path** line saying which it is.

---

# Rung 1 — Mechanism bites

*A targeted manipulation moves the predicted internal or behavioural variable.*

Five entries. This is the rung REE is genuinely strong on.

---

## 1.1 — The observation interface, not the policy learner, is the competence bottleneck

- **Run:** `v3_exq_948_observation_interface_re_representation_probe_20260825T142115Z_v3`
  (queue `V3-EXQ-948`, 2026-08-25, `ree-worker-1`)
- **Outcome:** PASS. `experiment_purpose: diagnostic`, `claim_ids: []` — **promotes nothing**,
  scoring-excluded by construction.
- **Design:** four PPO arms differing *only* in what observation they are given, plus three
  non-REE anchors. Seeds 42/43/44. Pre-registered `declared_null` and an `any`-aggregation
  combination rule stated in the manifest before the run.
- **Matched controls:** `random_walk` anchor (the floor), `local_view_greedy` and `greedy_oracle`
  (ceilings). All four arms share the same PPO learner, environment and training budget, differing only in `obs_dim` and which channels the observation carries.

| Arm / anchor | foraging competence (resources/episode, mean of 3 seeds) |
|---|---|
| `random_walk` (floor) | 0.933 |
| **`ppo_ree_latent`** (REE latent only, 32-d) | **0.500 — below the random floor** |
| `ppo_localfield_only` | 1.217 |
| **`ppo_latent_plus_localfield`** | **2.233** |
| `ppo_raw_obs` | 9.033 |
| `local_view_greedy` | 48.05 |
| `greedy_oracle` (ceiling) | 57.2 |

- **Effect size:** re-representation lift = **+1.733 resources/episode** (2.233 − 0.500), a 4.5×
  improvement from restoring one channel. Raw observation is 18× the REE latent.
  Per-seed `ppo_ree_latent` = [0.25, 0.50, 0.75]; `majority_supra_floor: false`, 0/3 seeds.
- **Uncertainty:** 3 seeds, no confidence intervals reported. The `ppo_ree_latent` vs
  `ppo_latent_plus_localfield` gap is large relative to the per-seed spread; the
  `ppo_raw_obs` per-seed values [12.05, 12.00, 3.05] are *not* — one seed is 4× below the
  other two.
- **Establishes:** the environment is learnable to ~9 resources/episode by a standard PPO agent
  given raw observations; the same learner given REE's latent representation performs *below a
  random walk*; and restoring a single local-field channel recovers a significant fraction of
  the loss. The competence ceiling is located at the **observation interface**, not at the
  policy learner and not at the environment's difficulty.
- **Does NOT establish:** anything about REE's own action selection — every arm here is PPO,
  not REE's selection stack. It does not establish that fixing the interface would lift REE to
  competence (nothing here tests that), it does not eliminate a substrate ceiling downstream,
  and per its own declared null it "does NOT re-open H-policy-learning".
- **Production path (GOV-PATHVALID-1):** compliant. No state is injected; the arms differ by
  which real channels the observation vector carries.
- **Reproduce:**
  ```
  cd ree-v3 && git checkout 8202bd7b4a6be82ce8528ed26886e6b1c7695e22
  /opt/local/bin/python3 experiments/v3_exq_948_observation_interface_re_representation_probe.py
  ```
- **Substrate identity:** commit `8202bd7b`, clean; `substrate_hash 59b5e6f4f55fc5ad…`;
  `machine_class linux-x86_64-py3.10-torch2.12.0+cpu`; epoch `ree_hybrid_guardrails_v1`.
  Non-default flags recorded in `enabled_default_off_flags`. No canonical profile (C1).

> **Why this is the entry to show an outsider first.** It is the most recent, has the tightest
> design, states its own null before the run, and its headline finding is *against* the project.
> A result that locates your own ceiling is easier to inspect than to dismiss.

---

## 1.2 — Recency-suppression content, not merely its presence, drives No-Go conversion

- **Run:** `v3_exq_926a_mech449_perseveration_nogo_falsifier_20260814T171050Z_v3`
  (queue `V3-EXQ-926a`, supersedes `V3-EXQ-926`, 2026-08-14, `ree-worker-3`)
- **Outcome:** PASS, `evidence_direction: supports`, claims MECH-449 + ARC-107. Seeds 42/43/44.
- **Design:** three arms — `ARM_OFF` (gate off), `ARM_CONSTITUTION` (live dACC recency vector),
  `ARM_SHUFFLED` (the *same* vector, permuted). 32 banks, 4 candidates.
- **Matched control:** `ARM_SHUFFLED` is the important one — it holds the vector's magnitude and
  distribution fixed and destroys only its *content*/candidate alignment.

| Criterion | Measured | Threshold |
|---|---|---|
| C1 perseveration conversion (load-bearing) | 0.969 / 0.969 / 1.000 per seed | ≥0.5 on ≥2 seeds |
| C2 recency content specificity | constitution 0.979 vs **shuffled 0.000** | gap ≥0.3 |
| C3 safety fail-open violations | 0 | 0 |
| readiness: suppression cross-candidate range | 0.75 | ≥0.25 |
| readiness: pre-No-Go eligible set size | 3.0 | ≥2.0 |

- **Effect size:** specificity gap **0.979** (conversion 0.979 with the real vector, 0.000 with
  the shuffled one), 3/3 seeds clearing.
- **Uncertainty:** 3 seeds, no CI. The manifest itself supplies the strongest caveat, and it is
  reproduced here verbatim rather than paraphrased: *"once the No-Go removes the incumbent from
  a set that HAS alternatives, the committed argmin necessarily changes, so C1 near 1.0 measures
  CAN-THE-AXIS-ACT, not an effect size."*
- **Establishes:** the perseveration axis of the MECH-449 Go/No-Go constitution is live and
  content-sensitive, and — the finding of record — that it is **structurally gated by envelope
  width**: at the stock `f_eligibility_envelope_floor` of 0.30 the identical mechanism converted
  1/16, because the MECH-448 envelope collapses to the fail-open protect-min. This interaction
  is documented nowhere in the MECH-449 build notes or in `V3-EXQ-689g`.
- **Does NOT establish:** any behavioural consequence. MECH-260 is deliberately **not tagged**
  by this run precisely because its own falsifier is behavioural and is blocked on the MECH-457
  competence floor (`V3-EXQ-445h` measured `action_class_entropy = 0` in *both* arms — vacuous
  at that floor). It also does not establish the effect at stock configuration: the run used a
  relaxed `f_eligibility_envelope_floor` of **0.1**, not the stock 0.30.
- **Production path (GOV-PATHVALID-1):** **compliant, and deliberately so.** The manifest notes
  that its predecessor `V3-EXQ-689g` exercised the safety and staleness axes with "injected …
  constructed tensors"; here the suppression vector comes from a real `DACCAdaptiveControl`
  history via `record_action()` + `_suppression_penalty()`. This run is a worked example of the
  rule being satisfied — and 689g is a worked example of the shape the rule warns about.
- **Reproduce:**
  ```
  cd ree-v3 && git checkout 2c70b6dc06187a229cfc1d01842d6e7fe98459d2
  /opt/local/bin/python3 experiments/v3_exq_926a_mech449_perseveration_nogo_falsifier.py
  ```
- **Substrate identity:** commit `2c70b6dc`, clean; `substrate_hash 80d76ab05e9c0f84…`;
  `machine_class linux-x86_64-py3.10-torch2.12.0+cpu`. No canonical profile (C1).

---

## 1.3 — MECH-341 is necessary for action-class diversity, and insufficient alone

- **Run:** `v3_exq_614a_mech341_p3_behavioural_falsifier_3arm_20260530T193245Z_v3`
  (queue `V3-EXQ-614a`, supersedes `V3-EXQ-614`, 2026-05-30, `ree-cloud-3`)
- **Outcome:** PASS, interpretation label `PASS_C2_C3_only_mech341_load_bearing_in_stack_only`.
  Claims MECH-341 + ARC-065. Seeds 42/43/44 × 3 arms = 9 cells, 9 completed.
- **Design:** a four-axis substrate (A = SP-CEM proposer, B = MECH-341, C = noise floor, D = VS)
  with three arms. Interpretation grid pre-registered in the manifest with all four outcome
  branches and their routings written *before* the run.
- **Matched control:** `ARM_1_ablate_B` — everything on except MECH-341. This is a true ablation
  control, not a comparison against a different configuration.

| Arm | axes | mean selected-class entropy (nats) | mean unique classes |
|---|---|---|---|
| `ARM_0_B_only` | B only | **0.000** | 1.00 |
| `ARM_1_ablate_B` | A,C,D on; B off | 0.526 | 2.67 |
| `ARM_2_ALL_ON` | A,B,C,D | **0.684** | 3.33 |

- **Effect size:** necessity delta = **+0.158 nats** (0.684 − 0.526), against a pre-registered
  `necessity_entropy_delta` threshold of 0.1. Rung-1 pass count: 0/3 seeds for B-only,
  2/3 for ablate-B, 3/3 for ALL_ON.
- **Uncertainty:** 3 seeds; the delta (0.158) is modest relative to the per-arm spread
  (`ARM_2` unique classes per seed = 5, 2, 3). No CI reported.
- **Establishes:** MECH-341 contributes measurably to behavioural diversity *within the assembled
  stack*, and — the sharper half — **cannot produce any diversity in isolation**: B-only
  collapses to a single action class on 3/3 seeds, 11806/11806 ticks.
- **Does NOT establish:** that diversity is *useful*. Nothing here measures task performance;
  entropy over selected action classes is not competence. Nor does it establish MECH-341's
  sufficiency — C1 (`R2c_b_only_rung1`) is explicitly `false`.
- **Production path (GOV-PATHVALID-1):** compliant. Arms differ by substrate flags only.
- **Reproduce:**
  ```
  cd ree-v3
  /opt/local/bin/python3 experiments/v3_exq_614a_mech341_p3_behavioural_falsifier_3arm.py
  ```
- **Substrate identity:** **weak provenance** — no `substrate_commit`, no `substrate_hash`, no
  `machine_class` recorded. `config_summary` captures the flag bundle
  (`use_per_stream_vs + use_vs_rollout_gating`, `mech341_entropy_bias_scale 2.0`,
  `z_goal_enabled`, `drive_weight 2.0`, `alpha_world 0.9`, `reef_enabled`). Epoch
  `ree_hybrid_guardrails_v1`. This run **cannot be reproduced against the substrate it tested.**
---

## 1.4 — Exposure regime, not the labelling objective, differentiates context memory

- **Run:** `v3_exq_832_inv041_childhood_exposure_context_diff_20260727T214521Z_v3`
  (queue `V3-EXQ-832`, 2026-07-27, `DLAPTOP-5.local`)
- **Outcome:** PASS, `evidence_direction: supports`, claims INV-041 + MECH-153.
  **Seeds 0–4 (five seeds — the joint-best on this ladder alongside 757).** `non_degenerate: true`.
- **Design:** a clean 2-factor dissociation. Three arms crossing exposure regime against
  supervision:

| Arm | `a_frac` (context-A exposure) | supervised labelling | mean cosine (ContextMemory A vs B) |
|---|---|---|---|
| `ARM_CHILDHOOD` | 0.50 (balanced/forced) | yes | **−0.025** (differentiated) |
| `ARM_ADULT` | 0.05 (avoidance-shaped) | yes | 0.99975 (collapsed) |
| `ARM_CHILDHOOD_UNSUP` | 0.50 | **no** | 0.99970 (collapsed) |

- **Matched controls:** two, and they isolate different things. `ARM_ADULT` holds the labelling
  objective identical and varies only exposure. `ARM_CHILDHOOD_UNSUP` holds exposure identical
  and removes labelling. Both collapse; only the conjunction differentiates.
- **Effect size:** C1 delta (adult − childhood) = **1.025** cosine units, threshold 0.1 —
  a 10× margin. C2 delta (unsupervised − childhood) = **1.025**, same threshold. Both pass.
- **Uncertainty:** 5 seeds, no CI reported, but the separation (−0.025 vs 0.9997) is close to
  the maximum the metric admits; this is not a marginal effect.
- **Establishes:** balanced early exposure is a **necessary prerequisite** for ContextMemory
  differentiation, and it is not reducible to the supervised labelling objective. An
  avoidance-shaped exposure schedule leaves the representation undifferentiated *despite
  identical supervision*.
- **Does NOT establish:** any behavioural capability. Cosine similarity between memory slots is
  a representational statistic. Nothing in this run shows the differentiated representation is
  *used*, or that the organism behaves differently as a result. **This is the nearest miss on
  rung 4 and the reason rung 4 is empty** — see that section.
- **Production path (GOV-PATHVALID-1):** compliant. The manipulation is the environment's
  exposure schedule; the representation is the organism's own.
- **Reproduce:**
  ```
  cd ree-v3
  /opt/local/bin/python3 experiments/v3_exq_832_inv041_childhood_exposure_context_diff.py
  ```
- **Substrate identity:** **partial provenance** — `substrate_hash af30d00c33b8e168…`,
  `machine_class darwin-arm64-py3.13-torch2.12.0`, no `substrate_commit`.
  **This is the only entry on the ladder run on the Mac machine class**, which matters:
  `torch.multinomial` is known to return different categories on `linux-x86_64`/torch 2.12
  than on `darwin-arm64` from a bit-identical probability tensor at the same seed
  (see `reference-cross-machine-class-contract-divergence`). This run's DV is a cosine, not a
  sampled action, so it is unlikely to be affected — but it has not been re-run cross-class.

---

## 1.5 — Event-boundary trigger: phasic hit, silence, and storm suppression dissociate

- **Run:** `v3_exq_757_mech288_mech287_event_boundary_trigger_functional_20260714T200049Z_v3`
  (queue `V3-EXQ-757`, 2026-07-14, `ree-worker-1`)
- **Outcome:** PASS, `evidence_direction: supports`, claims MECH-288 + MECH-287. Seeds 0–4.
- **Design:** three constructed input conditions (`boundaries` / `smooth` / `storm`) driven
  through `EventSegmenter` + `InvalidationTrigger` at **canonical defaults**
  (`EventSegmenterConfig()`, `InvalidationTriggerConfig()`), 600 ticks/run, 60 warmup.
  Six criteria across the two claims, all pre-registered with thresholds.

| Measure | Boundaries condition | Smooth condition (control) |
|---|---|---|
| mean slow-trigger hit rate | **1.000** (threshold ≥0.7) | — |
| mean slow-trigger count | 27.0 | **0.0** (threshold ≤1.0) |
| mean broadcast fraction | **1.000** | dissociation arm **0.0** (threshold 0.0) |
| mean boundary posterior | 0.938 | — |
| posterior spread / open fraction | 0.431 / 0.237 | thresholds 0.05 / 0.2 |

  Storm condition: **373 suppressed vs 34 broadcast**.

- **Effect size:** a clean double dissociation — 1.000 vs 0.000 on both the hit/silence contrast
  and the broadcast contrast, 5 seeds. `all_posteriors_in_unit_interval: true`. All six criteria
  non-degenerate.
- **Uncertainty:** 5 seeds; the contrast is at the metric's rails, so seed variance is not the
  binding constraint here. Input-side readiness positive controls all cleared by wide margins
  (fast input contrast 7.25 vs floor 3.0; slow z_goal shift ratio 697.6 vs floor 2.0).
- **Establishes:** the invalidation trigger fires on genuine event boundaries, is silent on
  smooth input, grades its posterior, and suppresses under boundary storms rather than
  broadcasting — the full predicted functional signature, at canonical defaults.
- **Does NOT establish** — and this is the sharp limit — **that the organism ever produces such
  boundaries endogenously.** The w/s/g signals here are synthetic, generated by the harness with
  `boundary_spacing 20`, `shift_w 2.0`, `seg_noise 0.05`. Nothing connects this to REE's own
  world model or to behaviour.
- **Production path (GOV-PATHVALID-1):** **this is a pre-edge component test.** The input stream
  the mechanism consumes is supplied by the harness, not produced by an upstream REE stage. Per
  the rule, it certifies that the *consumer* works given a correct signal; it does not certify
  that the production organism can reach that signal. Reported as such — this is exactly the
  reporting move the rule requires, not a full-pathway result.
- **Reproduce:**
  ```
  cd ree-v3
  /opt/local/bin/python3 experiments/v3_exq_757_mech288_mech287_event_boundary_trigger_functional.py
  ```
- **Substrate identity:** partial — `substrate_hash b97578aeea0ffe46…`,
  `machine_class linux-x86_64-py3.10`, no `substrate_commit`.

---

# Rung 2 — Behavioural competence

*The agent performs a meaningful task above an appropriate matched baseline.*

**One entry, and it is provisional.** Read the uncertainty paragraph before citing it.

---

## 2.1 — The escape-affordance bridge raises survival above a matched base arm (provisional)

- **Run:** `v3_exq_603q_sd059_mech358_escape_affordance_bridge_evidence_20260617T042830Z_v3`
  (queue `V3-EXQ-603q`, supersedes `V3-EXQ-603o`, 2026-06-17, `ree-cloud-3`)
- **Outcome:** PASS, claims SD-059 + MECH-358, label
  `escape_affordance_bridge_lifts_survival_safety_carries`. 5 arms × 3 seeds.
- **DV:** mean Stage-H episode length (survival duration) — an environment-observable behavioural
  outcome, not an internal statistic. Supplemented by AUC-survival and time-to-first-death.
- **Pre-registered pass rule** (in the manifest, before the run):
  `readiness_met AND both_bridge_mean_survival >= base_mean_survival * 1.10`.
  The binary G_H episode-length gate was declared **supplementary, not load-bearing**.

| Arm | mean survival | per-seed |
|---|---|---|
| `ARM_BASE_IA_ONLY` (control) | 37.73 | [67.63, 9.13, 36.43] |
| `ARM_RELIEF_BRIDGE` | 38.41 | [56.13, 6.03, 53.08] |
| `ARM_SAFETY_BRIDGE` | 46.57 | [56.83, 43.08, 39.80] |
| **`ARM_RELIEF_SAFETY_BRIDGE`** | **61.01** | [47.48, 19.03, 116.53] |
| `ARM_NAV_CONTROL` (competence control) | 39.81 | [47.45, 17.40, 54.58] |

- **Effect size:** **+61.7%** survival lift over the matched base arm, against a pre-registered
  +10% margin. `relief_lifts: false`, `safety_lifts: true`, `both_lifts: true` — the two halves
  are not equivalent, and relief alone does essentially nothing (+1.8%).
- **The matched controls are good.** `ARM_BASE_IA_ONLY` carries the full defensive chain (PAG
  freeze + ilPFC gate + driver + fed harm stream + harm-pathway training from 603k + trained
  safety predictors from 603j) and differs *only* by the bridge flags. `ARM_NAV_CONTROL`
  (spawn-in-reach) independently rules out "the bridge arm just navigates better": it sits at
  39.81, essentially at base.
- **Uncertainty — read this before citing the +61.7%.** Three seeds, and the per-seed structure
  does not support the headline as a robust effect:
  - Paired per-seed differences (both-bridge − base) are **−20.15, +9.90, +80.10**.
  - The effect **reverses on seed 42** (base 67.63 > both-bridge 47.48).
  - Mean paired difference +23.28, SD of differences ≈ 51.5, so a paired *t* ≈ 0.78 on 2 df
    (*p* ≈ 0.52). The arm mean is carried substantially by one seed's 116.53.
  - The run's own PASS is legitimate under its pre-registered rule, which was a **mean-lift
    threshold, not a significance test**. Both statements are true; do not let the PASS stand
    in for the second one.
- **Establishes:** on this substrate and environment, enabling both halves of the escape-affordance
  bridge raised mean survival over an otherwise-identical arm by more than the pre-registered
  margin, and the lift is not attributable to generic navigation competence.
- **Does NOT establish:** a robust or replicated effect (see above); anything about *foraging* —
  survival here is largely hazard avoidance, and the corpus-level yardstick (§ rung 6) shows the
  survives-but-does-not-forage signature explicitly; and nothing about generalisation, since
  this is one environment.
- **Production path (GOV-PATHVALID-1):** compliant. Readiness controls confirm PAG freezes and
  the ilPFC gate engage on the base arm before any bridge claim is read
  (`pag_freeze_frac 1.0`, `gate_engaged_frac 1.0`, `harm_disc_frac 1.0`), so the bridge is
  extending a live substrate rather than substituting for an inert one.
- **Reproduce:**
  ```
  cd ree-v3
  /opt/local/bin/python3 experiments/v3_exq_603q_sd059_mech358_escape_affordance_bridge_evidence.py
  ```
- **Substrate identity:** **weak provenance** — no commit, no hash, no machine class. Per-arm
  `arm_fingerprint` records are present (`arm_fp/v1`, `substrate_hash 0e67292a…`,
  `machine_class linux-x86_64-py3.10`, `substrate_n_files 100`), which partially recovers what
  the top-level fields omit.

### Why nothing else reached rung 2

The project has a claim-agnostic capability yardstick (`ree-v3/experiments/_lib/capability_eval.py`,
built 2026-07-09) reporting four environment-observable metrics. **63 run manifests in the corpus report
it.** Across every one of them, no REE-driven arm clears the random-walk floor on foraging or
goal-reach. Representative reviewed rows:

| Run | REE arm foraging (res/ep) | `random_walk` floor | `greedy_oracle` ceiling |
|---|---|---|---|
| `V3-EXQ-727` (P0-warmup all-ON) | 0.25 / 0.00 / 0.45 | 0.40 / 0.20 / 0.20 | 6.75 / 6.20 / 6.05 |
| `V3-EXQ-728b` (trained all-ON) | 0.25 / 0.00 / 0.45 | same | same |
| `V3-EXQ-734` (`vanilla_ppo` comparator) | 0.35 / 0.60 / 0.00 / 0.50 | 0.40 / 0.20 / 0.20 / 0.10 | — |
| `V3-EXQ-948` (`ppo_ree_latent`) | 0.25 / 0.50 / 0.75 | 1.05 / 0.90 / 0.85 | 57.2 |

That is the honest state of rung 2: one provisional entry on a survival DV, and a yardstick that
says the general foraging/goal-reach case is not there.
---

# Rung 3 — Flexible competence — **EMPTY**

*Behaviour changes appropriately after a rule, context or goal change.*

This rung is empty, and the reason is specific rather than "nobody tried". Outcome devaluation
is the canonical test of goal-directed flexibility, and the project ran a dedicated
three-experiment lineage at it. All three are **FAIL**, all three reviewed, all three
`evidence_direction: non_contributory` (claims unweakened, not falsified).

| Run | C1 behavioural shift | C2 discrimination separation | Verdict |
|---|---|---|---|
| `v3_exq_485k_sd033b_demotion_devalued_rerank_behavioural_20260621T192541Z_v3` | false (1/3 seeds) | false (0/3) | FAIL — `substrate_not_ready_requeue` |
| `v3_exq_485l_sd033b_devaluation_nogo_behavioural_20260622T063547Z_v3` | false (1/3) | false (1/3) | FAIL — `substrate_not_ready_requeue` |
| `v3_exq_485m_sd033b_devaluation_decoupled_head_behavioural_20260622T143349Z_v3` | **true (3/3)** | false (1/3) | FAIL — `conversion_ceiling_persists_despite_go_nogo` |

**The nearest approach — and why it does not clear the bar.** `V3-EXQ-485m` (2026-06-22,
claims SD-033b + MECH-263, 3 seeds) *did* produce a devaluation behavioural shift:
`max_test_deval_shift = 1.0` against `max_ceiling_deval_shift = 0.0` on the matched ceiling arm,
3/3 seeds, with all readiness positive controls met (`readiness_met: true`, devalued-state bias
range supra-floor 3/3). Behaviour changed after the goal changed.

It fails rung 3 because **the change was not selective.** C2 (committed-class separation between
contexts) passed on 1/3 seeds; C1b (bias-vector inversion) on 1/3. The confirmed autopsy
`failure_autopsy_V3-EXQ-485m_2026-06-22` corrected an auto-labelled `weakens` to
`non_contributory` and recorded the reading directly:

> "Ruling out the magnitude artifact, the valuation face does not convert in ISOLATION. 3rd
> convergent fails-C2-alone datum (654i demotion, 654j Go/No-Go, 485m OFC): conversion is
> emergent from the assembled stack, not any single selection-face."

A behaviour that shifts on devaluation but does not discriminate *which* option to shift toward
is not flexible competence — it is a shift. Promoting it to rung 3 would be exactly the stretch
this document is built to avoid.

**What would fill this rung:** a devaluation or reversal run in which C1 *and* a discrimination
criterion both clear on a majority of seeds, against a matched non-devalued control.

---

# Rung 4 — Developmental acquisition — **EMPTY**

*A capability appears through experience and was demonstrably absent earlier.*

Empty at the level of **capability**. The corpus has strong evidence of *representations*
acquired through experience, and none of a *behavioural capability* appearing that was absent
before.

**The nearest miss is 1.4 above** (`V3-EXQ-832`). It has everything rung 4 asks for structurally
— a manipulation of developmental exposure, a matched control that received the same supervision
but a different exposure schedule, five seeds, a 10× margin — except that the thing acquired is
a differentiated ContextMemory (cosine −0.025 vs 0.9997), not a capability. The document's own
governing principle applies against it:

> "Behaviour is the final arbiter; internal measures are diagnostic instruments … an elegant
> latent, gate or memory statistic is not organismal competence unless it can eventually alter
> appropriate behaviour."
> — `2026-08-27_developmental_integration_and_readiness_programme.md` §18.6

Two further runs bear on this rung and both point the same way:

- `v3_exq_875a_mech471_competence_provenance_20260804T114106Z_v3` (FAIL, reviewed) — designed
  to attribute competence to its acquisition history, with `acquired_A_pre_perturb` vs
  `post_perturb_A` arms. All arms sit between 0.0 and 0.9 res/ep against a floor of ~0.2–0.4;
  there is no acquired competence for the provenance question to bite on.
- `v3_exq_882a_mech472_context_memorization_generalization_20260805T110228Z_v3` (FAIL, reviewed) —
  `in_context` vs `held_out` foraging are statistically indistinguishable (e.g. 0.333 vs 0.417;
  0.167 vs 0.917; 0.583 vs 0.167 across seeds) and both at floor. Neither memorisation nor
  generalisation is demonstrated, because neither arm is competent.

**What would fill this rung:** a paired pre/post design on a behavioural DV where the pre-training
measurement is at floor, the post-training measurement clears it on a majority of seeds, and a
matched no-experience control stays at floor.

---

# Rung 5 — Retention / generalisation — **one entry, component-level**

*The acquired capability survives time / offline integration, and transfers.*

## 5.1 — Savings: reacquisition is 4× faster than acquisition, and dose-dependent

- **Run:** `v3_exq_829a_mech324_rapid_reacquisition_window_isolation_fix_20260801T062510Z_v3`
  (queue `V3-EXQ-829a`, supersedes `v3_exq_829_mech324_rapid_reacquisition_falsifier`,
  2026-08-01, `ree-worker-1`)
- **Outcome:** PASS, `evidence_direction: supports`, claims MECH-324 + MECH-323.
  **Six seeds — the largest seed set on this ladder** (11, 23, 37, 43, 59, 71).
- **Design:** acquisition → dissolution → reacquisition, with `window_isolation` as the
  manipulated axis and a sweep over `f_reacq` ∈ {1.0, 0.5, 0.25, 0.1}. Six criteria, three
  load-bearing.

| Measure | Value |
|---|---|
| median repetitions to **acquire** | 20.0 |
| median repetitions to **reacquire**, isolation ON | **5.0** |
| median repetitions to reacquire, isolation OFF (control) | **90.0** |
| dose-response ρ (isolation ON, window 100) | 0.99999998 (floor 0.8) |
| dose-response ρ (isolation ON, window 30) | 0.99999998 |
| dose-response ρ (isolation OFF) | `null` — no gradient |

- **Effect size:** **4× savings** (20 → 5 repetitions) with the window isolation on, and an
  **18× penalty** (5 → 90) with it off. The `f_reacq` sweep is monotone and near-perfectly
  linear: `f_reacq` 1.0/0.5/0.25/0.1 → median reacquisition 20/10/5/2, with 6/6 seeds
  uncensored at every point. That is a textbook dose-response, not a threshold artefact.
- **Uncertainty:** 6 seeds, medians reported rather than means (appropriate for censored
  reacquisition counts), `n_uncensored = 6` at every sweep point. **One caveat the manifest
  flags itself:** `criteria_non_degenerate` records **`C2: false`** — the dose-response criterion
  is marked degenerate even though it passed, because `f_reacq` mechanically sets the forced bar
  (`forced_bar` = 20/10/5/2 exactly tracks the medians). Read C2 as a plumbing check, not as an
  independent finding. C1, C3, C4, C5, C6 are all non-degenerate.
- **Establishes:** the MECH-323/324 crystallisation machinery exhibits genuine savings — a
  dissolved trace is re-acquired substantially faster than it was first acquired — and that this
  depends on window isolation, with the isolation-off arm reproducing the flat signature of the
  superseded `V3-EXQ-829` (criterion C6, passed). Retention discriminates erasure (C3, passed,
  load-bearing).
- **Does NOT establish** — and this is why the rung header says *component-level*: this is a
  **driven harness, not an organism**. Trials are supplied by the experiment
  (`target_sequence [1,2,3]`, `filler_sequence [0,4]`, `target_outcome 1.6`, `filler_outcome 0.4`,
  `consistent_noise_sd 0.02`); nothing here is foraging, navigating, or acting in an environment.
  It also demonstrates **retention, not generalisation** — the second half of this rung's
  definition is untested. There is no transfer condition.
- **Production path (GOV-PATHVALID-1):** partially compliant, and the boundary matters. The
  causal edge under test (acquire → dissolve → reacquire) is traversed endogenously *within* the
  mechanism; nothing downstream of that edge is injected. But the trial stream *entering* the
  mechanism is harness-supplied, so this certifies the crystallisation component, not that the
  organism generates such repeated experience for itself.
- **Reproduce:**
  ```
  cd ree-v3 && git checkout e39cc54f1fdeb6bf6732f9d26d27bcd9904532f3
  /opt/local/bin/python3 experiments/v3_exq_829a_mech324_rapid_reacquisition_window_isolation_fix.py
  ```
- **Substrate identity:** commit `e39cc54f`, clean; `substrate_hash dbeed081d922c7c6…`;
  `machine_class linux-x86_64-py3.10-torch2.12.0+cpu`.

### Considered for this rung and rejected — sleep consolidation

`v3_exq_691_q055_sleep_consolidation_diversity_persistence_20260620T103320Z_v3`
(queue `V3-EXQ-691`, PASS, reviewed, claims SD-017 + MECH-120, label `sleep_preserves_diversity`)
is the obvious candidate for "survives offline integration". **It does not survive scrutiny as a
between-arm result**, and it is listed here so a future reader does not re-promote it:

| Arm | entropy t0 | t1 | t2 |
|---|---|---|---|
| `ARM_SLEEP_ON` | 0.711 | 0.672 | **0.569** |
| `ARM_SLEEP_OFF` | 0.711 | 0.672 | **0.645** |
| `ARM_REPLAY_ABLATED` | 0.711 | 0.672 | 0.573 |

The sleep-on arm ends with **lower** trajectory-class diversity than the sleep-off control.
The PASS is carried by a *within-arm* criterion — 2 of 3 seeds in `ARM_SLEEP_ON` labelled
"preserves" (`persist_fraction: 0.5`, one seed "erodes") — not by any contrast against the
control arm, which runs in the opposite direction to the label. The readiness gate did confirm
the knob is not inert (`armA_consolidation_write_passes_mean 75.0` vs `armB 0.0`), so the
mechanism ran; the diversity claim is what does not follow. Provenance is weak (no commit, no
hash, no machine class, `seeds: null`).
---

# Rung 6 — Integrated organism competence — **EMPTY**

*Several faculties remain functional together in a canonical long-life organism.*

Empty, and this is the rung where the evidence is not merely absent but **points the other way**.
Two runs bear on it directly.

## The counter-evidence: `V3-EXQ-728b`

- **Run:** `v3_exq_728b_trained_allon_capability_point_20260721T113845Z_v3`
  (queue `V3-EXQ-728b`, supersedes `V3-EXQ-728`, 2026-07-21, `ree-cloud-4`, seeds 42/43/44)
- **Outcome:** PASS with `experiment_purpose: baseline`, `claim_ids: []` — it is the yardstick
  denominator, **reported context, not a governance verdict**. Its guard was GREEN on all three
  seeds (world encoder 4/4 tensors moved per seed, `world_encoder_max_abs_delta` 0.085–0.103,
  `n_seeds_failed = 0`), which is what makes it the *first valid* trained all-ON capability point:
  its predecessor `V3-EXQ-728` was scientifically void on a frozen `z_world` projection.

| Metric | random floor | **trained all-ON** | oracle ceiling | normalised position |
|---|---|---|---|---|
| foraging competence (res/ep) | 0.267 | **0.233** | 6.333 | **−0.005 (at floor)** |
| goal reach rate | 0.167 | **0.167** | 1.000 | **0.000 (at floor)** |
| planning depth | 1.933 | **1.433** | 4.267 | **−0.214 (below floor)** |
| survival horizon (ticks) | 11.5 | **81.6** | 21.2 | **+7.21 (far above ceiling)** |

**Reading, stated plainly:** with a correctly prediction-trained `z_world` encoder and every
mechanism enabled, the organism sits **at or below a random walk on foraging, goal-reach and
planning depth, while surviving roughly 4× longer than the greedy oracle.** It stays alive and
does not collect resources. This is the **survives-but-does-not-forage** signature — a known
MECH-457 competence-floor / MECH-180 instance (goal_success ≈ 0 = death-by-hazard-avoidance-
without-foraging), recorded in `evidence/planning/ree_ai_design_critique_plan.md` WS-3.

Two things must be held together here. Surviving 4× the oracle is not nothing — hazard avoidance
is a real, trained behaviour and it is the mechanism behind the rung-2 entry above. And it is
also not integrated competence, because the faculty that would make survival *worth* anything is
at floor.

## The nearest attempt: `V3-EXQ-096a`

`v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` (PASS, reviewed, 8 claims:
SD-005, SD-006, ARC-007, ARC-016, MECH-089, MECH-090, MECH-093, MECH-094) is the only run in the
corpus that *attempts* whole-stack integration: four phases, all V3 components active
simultaneously, 5/5 criteria met, `fatal_error_count: 0`. It records real numbers —
E1 final loss 0.00075; R²(z_self→body) 0.9935 vs R²(z_world→body) 0.4496, self-other gap 0.544;
harm 1.107/episode in phase 1 falling to 0.373 in phase 3 (a 66% reduction).

It does not qualify for rung 6, for three reasons, in increasing order of severity:

1. **No matched control.** The harm reduction is a *within-run* phase-1-vs-phase-3 comparison
   (random policy vs trained agent, different training exposure), not a contrast against an
   otherwise-identical arm. Per this document's own bar, that is a rung-0 anecdote on that DV.
2. **No seeds, no substrate identity.** `seeds: null`, no `substrate_commit`, no
   `substrate_hash`, no `machine_class`. It is a single run from 2026-03-25 on a substrate that
   can no longer be named.
3. **Decisive: two of the faculties read exactly zero.** `beta_block_rate: 0.0` and
   `commitment_rate: 0.0`. A claim that several faculties are *functional together* is refuted
   by its own manifest when two of them never fired. The "5/5 criteria met" verdict is real, but
   the criteria did not include those two rates.

**What would fill this rung:** a run against a *populated* canonical profile (see C1 — `v0` is an
empty placeholder), with several faculties each independently shown non-degenerate in that same
run, on a behavioural DV, against a matched arm, over ≥3 seeds.

---

# Rung 7 — Independent reproduction — **EMPTY**

*Another person or environment reproduces the effect from the public instructions.*

Empty, and this one is verifiable rather than inferred. Every `machine` field across the flat
manifest corpus resolves to a machine the project owner controls:

| Machine | manifests | owner |
|---|---|---|
| `ree-cloud-2` | 209 | project fleet |
| `ree-cloud-4` | 130 | project fleet |
| `ree-worker-1` (hub) | 95 | project fleet |
| `ree-cloud-1` | 68 | project fleet |
| `ree-worker-3` | 64 | project fleet |
| `ree-cloud-3` | 60 | project fleet |
| `DLAPTOP-4.local` | 49 | Daniel Golden (Mac) |
| `DLAPTOP-5.local` | 13 | Daniel Golden (same Mac, renamed) |

**The closest thing, and why it is not rung 7.** The contributor ledger
(`REE_assembly/contributors/contributions.json`) records a genuinely external machine:
`EWIN-PC`, owner `GoldenEoin1983`, **35 experiments**, 2026-04-18 to 2026-04-21. Its runner
status file survives at `evidence/experiments/runner_status/EWIN-PC.json` and shows it executing
project-assigned queue items (`V3-EXQ-195`, and `V3-EXQ-471` pending) and writing results back
under `C:\Users\Eoin\REE_Working\...`.

That is **donated compute on the project's own queue**, directed by the project owner — not an
independent party reproducing a named effect from public instructions. It demonstrates that the
runner installs and runs on a third-party Windows machine, which is a real portability result and
worth saying; it demonstrates nothing about the reproducibility of any finding on this ladder.
None of the 35 runs is tagged to a machine in the current flat-manifest corpus.

**What would fill this rung:** someone outside the project running one of the reproduction
commands above, on their own hardware, from the public `START_HERE` route, and recovering the
reported contrast — with their manifest landing in the corpus under their own machine identity.

---

# What this ladder adds up to

**The strong claim REE can make.** Five mechanism-level demonstrations with matched controls,
pre-registered criteria, 3–5 seeds, and — in the best cases — controls that hold magnitude fixed
and vary only content (926a's shuffled vector), ablate exactly one axis (614a), or cross two
factors (832). One of them (948) locates the project's own competence ceiling and is the single
most inspectable result in the corpus. These are real results and they should not be erased by
the competence-floor diagnosis.

**The claim REE cannot make.** There is no demonstration that a capability was acquired through
experience and then used; no demonstration that behaviour reorganises appropriately when the goal
changes; no whole-organism integration result that survives its own manifest; and no independent
reproduction. The one behavioural-competence entry (603q) has a per-seed structure that does not
support its headline number, and the corpus-wide capability yardstick puts the trained all-ON
organism at or below a random walk on three of its four metrics.

**The structural obstacle, restated.** Because `ree_v3_baseline@v0` is an empty placeholder and
no manifest references a canonical profile, the ladder **cannot currently be read vertically.**
Rung 1.2's Go/No-Go organism, rung 1.4's context-memory organism and rung 2.1's escape-bridge
organism are three different flag bundles. Populating a canonical profile is what would convert
this from a list of separately-defensible results into a claim about one animal.

---

## Method, so this can be redone or contested

1. Candidate set: `claim_evidence.v1.json` entries with `source_type: experimental`,
   `status: PASS`, no `scoring_excluded` value, and `run_id ∈ review_tracker.reviewed_run_ids`.
   That yields **195 reviewed candidate runs**.
2. Every entry below was then read from its own manifest in `evidence/experiments/`. No entry
   was placed on the basis of a claim's `status` field, a `live_status.reading`, or an index row.
3. Runs were ranked toward: an explicit matched control arm; ≥3 seeds; criteria and thresholds
   pre-registered in the manifest; readiness/positive controls reported; and recoverable
   substrate identity.
4. The capability-yardstick sweep (63 run manifests reporting `foraging_competence`) was read
   exhaustively to establish that rung 2 and rung 6 are empty rather than unsearched.
5. GOV-PATHVALID-1 was applied to each candidate individually; two entries (757, 829a) are
   labelled as component-level rather than production-path as a result, and none was silently
   promoted past it.

**Scope of this document.** Curation only. No experiment was run or queued, nothing was marked
reviewed, and no claim's status, confidence or `evidence_direction` was changed in producing it.

**Known omissions.** This is v0. It reads **17 runs in detail** — 7 placed on rungs (948, 926a,
614a, 832, 757, 603q, 829a), 1 rejected with reasons (691), and 9 read as negative or contextual
evidence (485k, 485l, 485m, 875a, 882a, 728b, 096a, 727, 734) — drawn from 195 reviewed PASS
candidates and ~945 flat manifests. Runs held in per-experiment directories without a flat
manifest (e.g. `v3_exq_455_sd032a_salience_behavioral`, `v3_exq_326a_wanting_gradient_nav_fix`)
were not opened; a v1 pass should sweep those, since older lineages are where the remaining
behavioural candidates would be. The literature corpus is deliberately excluded — this ladder is
experimental evidence only.
