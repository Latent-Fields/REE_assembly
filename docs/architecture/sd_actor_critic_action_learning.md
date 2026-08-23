---
title: "MECH-457: First-Class RPE-Driven Actor-Critic Action-Learning Substrate"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 11
status: implemented
status_asof: 2026-07-12
status_claim: MECH-457
---

# MECH-457: First-Class RPE-Driven Actor-Critic Action-Learning Substrate

**Claim ID:** MECH-457 (candidate / v3_pending)
**Subject:** `f_dominance_conversion_ceiling.actor_critic_action_learning_substrate`
**Status:** SUBSTRATE IMPLEMENTED 2026-07-12 (module + agent hooks + config-switchable A0–A3 arms landed, smoke-tested — see §7). **Validation experiment QUEUED + RUNNING: V3-EXQ-742** (`experiments/v3_exq_742_mech457_actor_critic_onoff.py`, ree-v3 `79fb5da`; priority 49, status `claimed` on origin/main as of 2026-07-12). The co-train update path is **resolved** — single-pass A2C (see §7 "Resolved: co-train-arm update path"). substrate_queue `sd_actor_critic_action_learning`, priority 1, `node_class: complicated (buildable)`. MECH-457 stays `candidate / v3_pending` — the substrate existing PROMOTES NOTHING; promotion awaits the V3-EXQ-742 result + a `/failure-autopsy` adjudication.
**Registered:** 2026-07-10
**Depends on:** SD-056 (e2 world-forward contrastive encoder, IMPLEMENTED 2026-05-29 `ree_core/predictors/e2_fast.py`), MECH-229 (VALENCE_WANTING, provisional/built)
**Unblocks:** MECH-457, `f_dominance_conversion_ceiling`, ARC-063
**Source autopsy:** `failure_autopsy_734-737-conversion-ceiling-competence_2026-07-11`

> **PROMOTES / DEMOTES NOTHING.** This design doc materializes the build spec the
> substrate_queue entry references; it registers no claim and cuts no promotion
> packet. The candidate design options (cand-A / cand-B) carry **placeholder ids**
> and are NOT registered into `claims.yaml` — registration (if any) is a later
> `/thought-digestion` + governance step.

---

## 1. The gap (V3-EXQ-724 → 737, stated as a build spec)

The conversion-ceiling competence portfolio (V3-EXQ-734/735/736/737/738) localized
REE's foraging wall to a **missing first-class action-learning system** *and* to the
**action-inadequacy of REE's frozen prediction-trained latent**:

- **V3-EXQ-724** (localization): the integrated all-ON agent forages ~0 resources/ep
  vs a 1.0 floor; the deficit held invariant across P1 budget, encoder-freeze, and
  mechanism count → localized to the **un-varied action-learning invariant**.
- **V3-EXQ-734** (env difficulty, non_contributory): REE all-ON recovers at **no**
  rung; PPO control recovers at D2 → difficulty is not the lever.
  ⚠️ **The first clause is VOID** — the `ree_trained_allon` arm ran on an untrained
  `z_world` (see the defect caveat below). The second clause (`vanilla_ppo` recovers
  at D2) is defect-free and stands.
- **V3-EXQ-735** (reward-balance, non_contributory): no approach-weighting arm
  supra-floor → reward-balance is not the lever.
- **V3-EXQ-736** (curriculum, precondition_unmet/vacuous): the agent cannot forage
  even the easy env → reinforces the floor.
- **V3-EXQ-737** (representation, ~~**LOAD-BEARING FAIL**~~ → **NOT ESTABLISHED**): a
  real trainable PPO actor + value baseline over REE's **frozen** `z_world` scored
  **0.217 res/ep @D3** — *below random (0.267)* and *below the same actor on raw
  pixels* (`ppo_raw_obs = 0.567`), both under the **1.0** competence floor. ~~The
  frozen prediction latent is a strictly *worse* action substrate than raw
  observation.~~
  ⚠️ **This bullet's conclusion is RETRACTED** — the `ppo_ree_latent` and
  `ree_bias_head` arms rode a `z_world` that was never prediction-trained, so the
  comparison was raw observation vs a **frozen random projection**, not vs a learned
  latent (see the defect caveat below). The `ppo_raw_obs` numbers themselves are
  defect-free and stand, as does the reading that the D3 bottleneck is policy
  learning.
- **V3-EXQ-738** (PASS anchor): a greedy 5×5 local-view forager scores **6.05 @D0,
  48.05 @D3** → the env is trivially forageable from the agent's local view; the wall
  is action-**learning**, not observability. *(Defect-free — no P0 warmup; unaffected
  by the caveat below.)*

> ### ⚠️ 2026-07-20 defect caveat (V3-EXQ-780 / 737a / 728)
>
> The `ree_trained_allon`, `ree_bias_head` and `ppo_ree_latent` arms cited in this
> section ran on a `z_world` that was **never prediction-trained**: the P0/P1 warmup in
> the `x734` `_train_all_on_agent` driver family builds three optimizer groups (e2,
> lateral-PFC bias head, OFC devaluation head) and **none covers any `latent_stack`
> parameter** (measured 0 of 4 world-encoder and 0 of 61 `latent_stack` tensors
> changed, bit-identical, on two independent drivers). Those arms therefore compared
> raw observation against a **frozen random projection**, not against a learned REE
> latent, and the claim that *"the frozen prediction latent is a strictly worse action
> substrate than raw observation"* is **NOT established**.
>
> The `ppo_raw_obs`, `vanilla_ppo`, `greedy_oracle`, `random_walk` and **V3-EXQ-738**
> anchors are structurally unaffected and **stand** — including the reading that the D3
> bottleneck is **policy learning** (carried by the defect-free `ppo_raw_obs` control).
> Retest owed: **V3-EXQ-734b / 737b** (SD-070 adoption validation,
> `zworld_p0_episodes=60`).
>
> Diagnosis: [`zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md`](../../evidence/planning/zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md) §6c.
> Blast-radius audit: [`zworld_evidence_blast_radius_2026-07-20.md`](../../evidence/planning/zworld_evidence_blast_radius_2026-07-20.md) §4.
> Fix (landed, DEFAULT OFF `zworld_p0_episodes=0`): `ree-v3/experiments/_lib/zworld_p0_warmup.py`.

**MECH-457 names the missing system.** Biological action learning is a dedicated
learning system, not a bias term on a prediction model: dorsal striatum acts as an
ACTOR, dissociable from the ventral-striatal value-prediction CRITIC (O'Doherty et
al. 2004), taught by a dopaminergic reward-prediction-error signal (Schultz, Dayan &
Montague 1997), with D1/D2 opponent credit assignment as a later refinement (Collins
& Frank 2014 OpAL). The ML statement of the same point: competent control comes from
directly optimizing a dedicated, separately-parameterized policy on expected return
with a value baseline (policy-gradient theorem / actor-critic, Sutton et al. 2000),
NOT from reading a policy off a value/prediction model.

**Build spec (from the substrate_queue `implementation_hint`).** Build MECH-457: a
parameterized actor trained on a reward-prediction-error teaching signal with a
value-baseline critic, architecturally distinct from the thin `bias_head` REINFORCE
over the SD-056 prediction-trained encoder. Per V3-EXQ-737, the actor must **NOT** ride
a frozen `z_world`; the action-learning loss **must co-shape / augment the
representation** (or add an action-adequate stream). *(This directive's stated
evidential basis is the V3-EXQ-737 bullet retracted by the caveat above — it is
retained as the prudent design default, not as an established finding, and the
frozen-vs-co-trained ablation below is what would settle it.)* The validation experiment **must**
carry a **frozen-vs-co-trained-encoder ablation arm** to settle the action-adequacy
sub-question empirically.

---

## 2. Co-shaping design (from REE_convergence intake)

> **Provenance.** This section wires in the SECONDARY convergence intake
> [`2026-07-11_action_representation_coshaping_synthesis.md`](https://github.com/Latent-Fields/REE_convergence/blob/master/reports/2026-07-11_action_representation_coshaping_synthesis.md)
> (landed REE_convergence master `42646d6`; snapshot ref `git-f0dda1d`), which
> completed **after** the substrate_queue entry was materialized and which the
> originating build session (`nice-blackwell-f367f8`) could not have seen. The
> synthesis surveys five external action-learning families for "what makes a latent
> good for control, not just prediction?" and triages each against REE's
> **biological-construction constraint** (follow brain-like construction where
> feasible). It **does NOT gate the build** — it de-risks the co-shaping *design*.

The 737 finding sharpens the build's open question to one edge: **the learning signal
from the MECH-457 actor-critic must reach back into the SD-056 encoder** (co-shaping),
because a latent trained only to be observation-predictive (SD-056 one-step
action-conditional contrastive) is not, on its own, an adequate substrate for a value
function or policy. The intake supplies two translatable instantiations of that edge,
ranked by (biological grounding × fit to MECH-457 × minimality).

### cand-A — CURL/UNREAL auxiliary co-training (ADOPT FIRST; the minimal instantiation)

The most-replicated finding in representation-for-RL is that **co-training the encoder
with a self-supervised auxiliary loss + the RL gradient simultaneously** beats both
reconstruction and freezing (CURL, Laskin et al. 2020 — an InfoNCE contrastive
auxiliary co-trained with the RL loss; UNREAL, Jaderberg et al. 2016 — auxiliary
reward-prediction and pixel/feature-control heads on A3C). REE's **SD-056 is already an
InfoNCE loss** — but it is prediction-trained and (per 737) consumed **frozen**.

**Adapter into REE (the minimal co-shaping loss):**

```
L = L_actor_critic(MECH-457)  +  beta * L_contrast(SD-056)  +  eta * L_reward_pred(MECH-229)
```

with the encoder receiving gradient from **all three** terms. Concretely:

- **Un-freeze SD-056** — let the MECH-457 actor-critic gradient flow into the
  `E2.world_forward` encoder (the direct negation of the 737 frozen instantiation).
- **Optional UNREAL-style reward-prediction auxiliary head** driven by **MECH-229
  VALENCE_WANTING** (the wanting/reward signal the RPE teacher already consumes),
  pulling the latent toward control-relevant structure.

This **is** the frozen-vs-co-trained ablation arm the 737 refinement owes: the arm is
exactly the `stop_grad` toggle on the actor-critic term into the encoder. It is the
**smallest delta** from what exists (SD-056 is already contrastive; the InfoNCE import
was already priced in at SD-056, so no new biological divergence) and is therefore the
recommended **first** thing the build tries.

**Biological-construction verdict: PASS (consistent).** Multi-objective shaping of
cortical representations is bio-plausible; no new formal import beyond the one SD-056
already accepted.

### cand-B — Successor-feature critic (ADOPT AS THE DEEP FORM)

SD-056 makes `(z_world_0, a_i) → z_world_1[i]` action-discriminable *one-step* —
necessary but not sufficient for a value function, which needs the representation to
predict **discounted future return** under the *policy's* future occupancy. The
successor representation is exactly that quantity made into a representation:

- **SR** (Dayan 1993): `M^pi(s, s') = E[ Σ_t γ^t 1(s_t = s') | s_0 = s, pi ]`;
  `V^pi = M^pi · R`.
- **SF** (Barreto et al. 2017): with state features `phi(s)`,
  `psi^pi(s) = E[ Σ_t γ^t phi(s_t) | pi ]`; `Q^pi(s,a) = psi^pi(s,a) · w` for reward
  `r = phi · w`. Generalized policy improvement transfers across tasks sharing
  dynamics but differing in `w`.

**Adapter into REE.** Add an auxiliary SF head on the SD-056 encoder that regresses
`psi^pi(z_world)` toward a bootstrapped target `phi(z_world) + γ · psi^pi(z_world')`
under the current MECH-457 policy. Then the **MECH-457 critic is literally `psi · w`**,
and **MECH-229 VALENCE_WANTING supplies `w`** (the reward weighting over features) — or
the features `phi` are seeded from the wanting/liking channels. This co-shapes
`z_world` toward *policy-conditioned return-predictiveness*, the precise property 737
showed the frozen prediction latent lacks.

**Biological-construction verdict: PASS (strongest).** This is not a formal import
bolted onto REE — it is the *faithful translation* of a mechanism biology is thought to
instantiate: the **hippocampal predictive map** (Stachenfeld, Botvinick & Gershman
2017, *The hippocampus as a predictive map*, Nat. Neurosci.) — place fields encode the
SR; grid cells approximate its low-dimensional eigenbasis. **Highest-value candidate.**

### The MuZero constraint-relaxation (principle only, not a module)

MuZero (Schrittwieser et al. 2020) trains its latent with **no** observation-prediction
loss at all — only value/policy/reward targets — the cleanest existence proof that
*observation-predictiveness is not required for action-adequacy; value/policy-shaping
is*. Adopt the **lesson** (co-training may be *allowed to degrade* one-step
observation-predictiveness if that buys value/policy-adequacy — SD-056 need not win
every batch), **not** the apparatus (MCTS + learned-model rollout; see §3).

---

## 3. Biological-construction NON-adoptions (anti-drift record)

Recorded explicitly so the MECH-457 build does **not** drift toward machinery that has
no faithful biological construction. These are deliberate non-adoptions under REE's
biological-construction constraint, not oversights:

| Non-adoption | Why refused |
|---|---|
| **MuZero MCTS / learned-model rollout planning** (Schrittwieser et al. 2020) | No faithful biological construction for tree search + unrolled learned-model planning. Import the *principle* (value/policy-shaped latent may relax reconstruction) only; the planning apparatus is out of scope for MECH-457's **model-free** RPE actor-critic. |
| **Dreamer backprop-through-learned-dynamics imagination actor** (Hafner et al. 2020/2023) | No biological analog differentiates through a world model to produce a policy gradient. It also duplicates, in a heavier and less faithful form, what MECH-457's model-free RPE actor-critic does. (Dreamer's *reward-head-inside-the-encoder-loss* term IS translatable — but it is already subsumed by cand-A; only the differentiable-imagination actor is the non-adoption.) |
| **Decision Transformer return-conditioned supervised sequence model** (Chen et al. 2021) | No biological construction for return-conditioned supervised action prediction over a transformer context; it discards RPE + critic — the exact structures MECH-457 asserts are missing. Its one transferable idea (conditioning action on a desired-return/goal signal) is already held in REE by MECH-307 (anticipatory-affect goal reps) + MECH-455 (competence-based IM). Boundary marker only. |

---

## 4. Validation experiment — ablation-arm coverage

The MECH-457 validation experiment must carry ablation arms covering **both** co-shaping
candidates, each scored against the **fair denominator**:

> **Yardstick:** the **V3-EXQ-738 local-view-achievable ceiling** (greedy 5×5-window
> forager: **48.05 @D3**, 6.05 @D0), via `experiments/_lib/capability_eval.py` — **NOT**
> the global teleport oracle (57.2), which reads privileged full-resource coordinates
> the learner never sees and inflates the bar ~28× above the 1.0 floor (WS-1
> observability-confound, `failure_autopsy_V3-EXQ-732a`). Load-bearing DV =
> `d3_foraging_competence_mean_resources_per_ep`, higher-is-better, target **≥ 1.0
> floor on a strict majority of seeds** at D3.

**Arm matrix (both sub-questions crossed):**

| Arm | cand-A axis (encoder) | cand-B axis (critic) | Tests |
|---|---|---|---|
| **A0 — frozen baseline** | encoder **frozen** (`stop_grad` on AC term) | plain value head | Reproduces the 737 latent-inadequacy level (predicted ≤ ~0.6). |
| **A1 — co-trained + plain value** | encoder **co-trained** (AC gradient flows) | plain value head | cand-A alone: does un-freezing SD-056 + minimal co-training clear the floor? |
| **A2 — frozen + SF-critic** | encoder **frozen** | **SF-critic** `psi · w` (w from MECH-229) | Isolates the SF-critic contribution absent encoder co-adaptation. |
| **A3 — co-trained + SF-critic** | encoder **co-trained** | **SF-critic** `psi · w` | The deep form: full cand-A + cand-B. |

- **cand-A (frozen vs co-trained)** is the A0/A2 → A1/A3 contrast (the mandatory
  frozen-vs-co-trained-encoder arm the substrate_queue spec requires).
- **cand-B (SF-critic vs plain value head)** is the A0/A1 → A2/A3 contrast.

**Pre-registered falsifier for cand-B (drafted, NOT registered).** If an SF-critic
co-shaped encoder (A3) does **not** lift all-ON foraging strict-above BOTH the
frozen-`z_world` actor (737, 0.217) and the raw-obs actor (0.567) on a majority of
seeds at D3 — using the 738 ceiling (48.05) as the fair denominator — then the SF-critic
earns no keep over the minimal CURL/UNREAL co-training (cand-A: A1). Conversely, a
robust supra-floor lift in A3 that A1 does **not** achieve supports the SF-critic as the
load-bearing co-shaping mechanism.

**Decision prediction.** A dedicated RPE actor-critic whose learning loss co-shapes the
encoder (A1/A3) should clear the 1.0 floor at D3 for a majority of seeds; the
frozen arms (A0/A2) are predicted to remain at or below the 737 latent-inadequacy level
(< 0.6). If the **co-trained** arms also stay sub-floor, the deficit is deeper than
action-learning credit assignment → **route re-autopsy, NOT a lettered floor re-test**.

---

## 5. Dependencies, siblings, and how this de-risks the campaign

- **Deps present → buildable now, no probe gate.** SD-056 (`ree_core/predictors/e2_fast.py`,
  implemented 2026-05-29) and MECH-229 (VALENCE_WANTING, provisional/built) both exist.
- **Sibling, not duplicate:** MECH-455 (competence-based intrinsic motivation) answers
  *what the agent should be motivated to get better at* (the **drive**); MECH-457 +
  cand-A/B answer *what representation + critic structure lets a learned actor convert
  that motivation into competent action* (the **substrate**). They meet at MECH-229.
  Both are WS-1 (`ree_ai_design_critique_plan`) competence-floor levers.
- **This section does NOT gate `/implement-substrate` MECH-457** — the build proceeds
  in parallel. It pre-loads the co-shaping design so the build's first ablation arm
  (cand-A: co-train vs freeze) and its deep arm (cand-B: SF-critic) are already argued
  and biologically triaged.

---

## 6. Primary sources (paraphrase-only)

- Successor representation: **Dayan 1993**, *Improving Generalization for Temporal
  Difference Learning: The Successor Representation*, Neural Computation.
- Successor features + GPI: **Barreto et al. 2017**, *Successor Features for Transfer in
  Reinforcement Learning*, NeurIPS (arXiv:1606.05312).
- Hippocampal predictive map (biological anchor for cand-B): **Stachenfeld, Botvinick &
  Gershman 2017**, *The hippocampus as a predictive map*, Nature Neuroscience.
- Contrastive RL auxiliary (cand-A): **Laskin, Srinivas & Abbeel 2020**, *CURL*
  (arXiv:2004.04136); **Jaderberg et al. 2016**, *Reinforcement Learning with
  Unsupervised Auxiliary Tasks* (UNREAL, arXiv:1611.05397).
- Actor/critic biological + ML grounding: **O'Doherty et al. 2004** (dorsal-actor /
  ventral-critic dissociation); **Schultz, Dayan & Montague 1997** (dopaminergic RPE
  teacher); **Collins & Frank 2014** (OpAL D1/D2 opponent credit); **Sutton et al.
  2000** (policy-gradient theorem); **Stooke et al. 2021** (decoupled
  representation/policy).
- Non-adoptions: **Schrittwieser et al. 2020** (MuZero, arXiv:1911.08265); **Hafner et
  al. 2020/2023** (Dreamer, arXiv:2010.02193 / 2301.04104); **Chen et al. 2021**
  (Decision Transformer, arXiv:2106.01345).

---

---

## 7. Implementation (landed 2026-07-12, session `nice-blackwell-f367f8`)

Built via `/implement-substrate` (PRIMARY routing from the autopsy). All config
defaults are no-op; with `use_actor_critic=False` the substrate is byte-identical
(verified: default `REEAgent` has `action_critic is None`, empty param group).

**Module** `ree_core/action_learning/actor_critic.py` — `ActorCriticPolicy(nn.Module)`
(+ `ActorCriticStep` dataclass). Shared Tanh trunk → `policy_head` (the dorsal-striatal
ACTOR, own `Categorical` over `config.e2.action_dim`) + `value_head` (plain CRITIC,
cand-A). When `use_sf_critic=True`: `phi_head` (state features), `psi_head` (successor
features), and a learned reward-weight `reward_w` (`r ~= phi·w`); the SF critic value is
`V_SF = psi·w` (cand-B). `select(z, deterministic)` returns the graph-connected
`ActorCriticStep`; `sf_reward_prediction(phi)` exposes `phi·w` for the reward-regression
loss. Trunk width 128 matches the validated V3-EXQ-734/737 PPO net so the frozen arm
reproduces 737.

**Config** (flat `REEConfig` fields, threaded through `from_dims`, all no-op default):
`use_actor_critic` (master), `actor_critic_cotrain_encoder` (**the frozen-vs-co-trained
ablation lever**), `actor_critic_use_sf_critic` (plain vs SF critic = cand-A vs cand-B),
`actor_critic_hidden=128`, `actor_critic_sf_feature_dim=32`. The four validation arms are
`(cotrain_encoder ∈ {F,T}) × (use_sf_critic ∈ {F,T})` = A0/A1/A2/A3.

**Agent wiring** (`ree_core/agent.py`): `self.action_critic` instantiated under the
master switch. Hooks:
- `actor_critic_step(latent, deterministic)` — applies the co-shape/detach lever
  (`z = latent.z_world` if `cotrain_encoder` else `z_world.detach()`) and returns the
  `ActorCriticStep`. A distinct dorsal/habitual action pathway; does NOT route through
  E3's cost argmin.
- `actor_critic_reward(latent)` — an OPTIONAL convenience helper for ONE
  substrate-internal reward, `R_t = detach(e3.benefit_eval(z_world) − e3.harm_eval(z_world))`
  (ARC-108). The substrate is teacher-AGNOSTIC; the validation experiment supplies its own
  reward. **Teacher source is an OPEN validation-design choice** (foraging reward is the
  clean grounded-by-construction default; this substrate signal needs the `benefit_eval` /
  `harm_eval` heads grounded via ARC-030 first — they start random-init behind the ARC-030
  warmup gate — with a readiness gate on a positive control before any arm is trusted).
- `actor_critic_parameters()` — actor + both critic heads (for the experiment optimizer).
- `actor_critic_encoder_parameters()` — `latent_stack.parameters()`, the z_world encoder
  the cotrain arm co-shapes (the ablation seam: cotrain adds these to the optimizer,
  frozen omits them).

**Training** (PPO/GAE + SF-TD losses) lives in the experiment, reusing
`x734._ppo_update` / `_compute_gae` — matching the REE convention where the bias_head
REINFORCE update also lives in the experiment.

**Smoke test PASS** (2026-07-12): backward-compat (defaults → `None`); plain-critic
forward; the ablation lever (frozen trains the actor-critic but NOT z_world; cotrain
flows gradient into z_world); SF-critic `phi/psi` shapes + `V_SF == psi·w`; the
substrate reward hook. Reused all-ON/PPO experiment modules (x724/x734/x737) still
import cleanly (no backward-compat break).

**Reward-hacking guard owed at validation** (§ "Reward-hacking hazard" was folded from
this build): the substrate `R_t` reads z_world through the (frozen-in-P1)
`benefit_eval`/`harm_eval` heads, so a co-shaped encoder could inflate the frozen benefit
head without real foraging. `R_t` is detached (no gradient path), and the eval DV is
UNSHAPED real foraging (not gameable); the validation MUST instrument a
`train_return_vs_eval_foraging_divergence` guard — a large divergence routes to
"substrate teacher inadequate", not to a false MECH-457 refutation. **Finding (2026-07-12):**
the all-ON recipe (x724/x734) does NOT ground `benefit_eval`/`harm_eval` (no
`record_benefit_sample`, no benefit optimizer — they stay random-init behind the ARC-030
warmup gate), so IF the substrate-signal teacher is chosen the validation must ground them
via the ARC-030 phased protocol in P0 + a readiness gate before P1. This is why the
foraging-reward teacher (grounded by construction) is the recommended default, and the
teacher source is left OPEN for the validation build (see §5 handoff).

**Resolved: co-train-arm update path (2026-07-12) → single-pass A2C, in V3-EXQ-742.** The
fork below was resolved to **option (i) single-pass A2C** — chosen by the operator 2026-07-12
and independently implemented by the queued validation `v3_exq_742_mech457_actor_critic_onoff.py`:
all arms take one advantage-weighted actor + value(+entropy) A2C backward per episode over the
in-order rollout graph (GAE advantages from detached values); co-train arms read live `z_world`
and add `actor_critic_encoder_parameters()` (= `latent_stack`) to the optimizer, frozen arms
read `z_world.detach()`. The grad-flow seam was verified directly (co-train → encoder grad
present; frozen → encoder grad absent; both → actor-critic grad present). A0 is accepted as a
valid frozen-encoder A2C baseline (it is not required to bit-reproduce 737's clipped-PPO
number; the A0↔A1 / A2↔A3 contrasts are learner-controlled because every arm shares the update).
The original fork analysis is retained below for the record.

**Fork analysis (superseded by the resolution above).** §7 says the
PPO update reuses `x734._ppo_update` / `_compute_gae`. That works verbatim for the **frozen**
arms (A0/A2): `actor_critic_step` detaches `z_world`, so the stored state is a fixed vector
and `_ppo_update`'s multi-epoch minibatch re-forward `policy(mb_states)` is well-defined —
this is exactly x737's `ppo_ree_latent` path. It does **NOT** transfer to the **co-train**
arms (A1/A3): there `z_world` must carry encoder gradient, but `z_world` is produced by
`latent_stack.encode(enc_combined, self._current_latent, prev_action=self._last_action, …)`
— **recurrent and stateful** (conditioned on the previous latent + last action, with
per-step side effects). So a shuffled-minibatch re-forward through `sense()` cannot reproduce
the rollout-time `z_world` and would corrupt agent state; there is no stateless differentiable
re-encode. The co-train arm therefore needs an explicitly chosen update scheme, e.g. one of:
- **(i) single-pass A2C-style co-train** — keep the rollout graph, compute one advantage-weighted
  actor + value (+ entropy) loss over the rollout, backward once into `action_critic` +
  `actor_critic_encoder_parameters()`. Bio/CURL-consistent, but drops PPO clipping/epochs, so
  **A0 no longer bit-reproduces 737's multi-epoch PPO** (loses the §7 "frozen arm reproduces
  737" anchor).
- **(ii) detached-PPO + separate encoder-directed auxiliary** — run the clipped multi-epoch PPO
  on detached `z_world` (identical for all arms, A0 reproduces 737), and co-shape the encoder
  with a *separate* CURL/UNREAL auxiliary (contrastive + reward-prediction) computed on stored
  obs. This is cand-A's literal "auxiliary co-training" reading, but the actor-critic gradient
  then does NOT flow into the encoder — which is what `actor_critic_cotrain_encoder=True` and
  the `actor_critic_step` live-`z_world` branch were built to mean.
- **(iii) retain-graph mini-PPO** — store the rollout-time graph-connected tensors and run the
  clipped update with `retain_graph` (no re-encode). Preserves both PPO and encoder gradient,
  at higher memory cost and a nonstandard "epochs over a fixed graph" semantics.

These are not interchangeable — (i) and (ii) answer the cand-A frozen-vs-co-trained ablation
with materially different encoders, and (ii) arguably tests a *different* claim than the one
`actor_critic_step` encodes. The choice was a validation-design decision owed to the substrate
author / operator before the A0–A3 experiment was written; it was not resolvable from the landed
artifacts. It was resolved to option (i) — see the "Resolved" note at the top of this block.

---

*Design doc authored 2026-07-11 (REE_convergence co-shaping synthesis wired into the
build artifacts); implementation landed 2026-07-12 by session `nice-blackwell-f367f8`
via `/implement-substrate`. Grounded in the materialized substrate_queue entry
`sd_actor_critic_action_learning` (REE_assembly `6e971edda2`) + the MECH-457 claim.
PROMOTES / DEMOTES NOTHING.*
