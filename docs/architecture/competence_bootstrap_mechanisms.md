---
title: Competence-bootstrap mechanisms (MECH-459 / MECH-460 / MECH-461 / MECH-475 / MECH-476)
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 1
---

# Competence-bootstrap mechanisms (MECH-459 / MECH-460 / MECH-461 / MECH-475 / MECH-476)

Status: **ARCHITECTURE STUB -- candidate claims only. Nothing here is built, and nothing here
adjudicates the live discrimination.**

Registered: 2026-07-18 (CDQ-007 convergence-demand intake)
Owning demand row: `evidence/planning/convergence_demand_queue.v1.json` -> CDQ-007
Pipeline of record: `evidence/planning/convergence_demand_pipeline_plan.md` Section 5 steps 2-3
Target node: **MECH-457** (`action_learning_as_first_class_actor_critic_substrate`)

---

## 1. The gap these three claims address

MECH-457's substrate is **built** (`ree-v3/ree_core/action_learning/actor_critic.py`,
`ActorCriticPolicy`: dorsal-striatal actor + value critic + optional successor-feature critic).
It does not work. The learned converter cannot extract a competent policy from a **provably
sufficient** observation, and is **invariant to every config / env / credit / capacity lever
tried**:

| Axis | Experiment | Outcome |
|---|---|---|
| capacity | V3-EXQ-769 | falsified (raw ON regressed 6.48 -> 0.12) |
| drive-schedule | V3-EXQ-770 | hit its pre-registered null |
| reward-coupling | V3-EXQ-771 | hit its pre-registered null |
| credit-horizon | V3-EXQ-772 | hit its pre-registered null |

Readiness was met on every leg (`local_view_greedy` 48-55, oracle 57-61 against a 1.0 floor), yet
every treatment arm forages at the ~0-1 floor on **both** `z_world` and raw representations.
Behavioural cloning (imitation, 32.72) is the **only** floor-clearing existence proof.

Cluster autopsy: `evidence/planning/failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json`
(confirmed; `non_contributory` / `competence_implementation_gap`; re-derive brake FIRED for the
7th time -- it **refuses** any further config/env/credit/capacity re-queue).

MECH-457 is **intact but necessary-not-sufficient**: a dedicated actor-critic is required and is
not enough. The *mechanism that makes the converter bootstrap competence* is unknown.

## 2. Coordination constraint (read before touching any of this)

The successor **GOV-FANOUT-1** portfolio is the live open discrimination, pre-registered ALIVE in
the `competence_floor` question of `evidence/planning/hypothesis_space_registry.v1.json`:

- **H-bc-prior** -- a competence-directed behavioural-prior / imitation seed (V3-EXQ-780)
- **H-approach-primitive** -- an innate, non-extinguishing, demonstrator-free approach drive
  (V3-EXQ-781)

Both experiments are queued and `claimed`. The substrate-queue entry
`mech457_competence_bootstrap_explorer` is deliberately `blocked_pending_discrimination`
(node_class `complex (probe-gated)`).

**These three claims INFORM which competence-directed dependency to build. They do not decide the
discrimination and they license no build.** MECH-460 maps onto the H-bc-prior leg; MECH-461 maps
onto the H-approach-primitive leg; MECH-459 is a **third axis** that belongs to neither leg and
**widens** the hypothesis space rather than narrowing it (see §6).

## 3. MECH-459 -- return-scale invariance blocks actor bootstrap

**Source:** DreamerV3 (Hafner et al. 2023, arXiv:2301.04104), mined through the actor-critic
**stabilisation** lens -- `REE_convergence/sources/dreamer-v3/actor_critic_stabilisation.md`
(claims `DREAMER-V3-MOD-003/004`, `-OBJ-002/003/004`, probes `-P-007/008`). Distinct from the
existing codebook lens (MECH-438).

**The observation that motivates it.** REE's MECH-457 update stacks **two two-sided normalisers**
(`experiments/_lib/mech457_fanout.py::train_rawview_ac_rl`):

```
scale  = reward_std.std + 1e-6                      # Welford RUNNING std -- normaliser 1
scaled = [r / scale for r in ep_rewards]
advs, rets = _compute_gae(scaled, ...)
adv_t = (adv_t - adv_t.mean()) / (adv_t.std() + 1e-8)   # per-episode -- normaliser 2
```

Normaliser 2 is a **scale-invariance operator**: after it the policy gradient depends only on the
*shape* of the within-episode advantage vector and is **exactly invariant to any multiplicative
rescaling**. Read the eliminated axes through it: any lever that changes *how much* a forage event
or an intrinsic drive is worth is **divided out by construction**. Invariance is predicted, not
surprising.

The complementary half is DreamerV3's named failure: in an episode with zero forage contacts the
reward stream is `harm_signal + novelty_bonus` only, GAE over it yields an advantage vector of pure
critic error plus exploration jitter, and per-episode standardisation rescales that noise to **unit
variance** so the actor takes a full-magnitude step on it. This is exactly the
"amplification of near-zero returns" that DreamerV3's `max(1, Per95 - Per5)` clamp exists to
prevent (Appendix E).

**The claim.** A self-normalising (two-sided) return/advantage pathway is *sufficient* to produce
converter invariance to magnitude levers and to convert a near-zero-signal episode into a
full-magnitude noise gradient; the corrective is DreamerV3's recipe -- a **stationary** magnitude
compressor (symlog, not a running normaliser), a **one-sided** percentile normaliser
`max(1, S)`, and a **distributional (twohot/CE) critic** in place of the scalar MSE head that
collapses a bimodal sparse-return distribution onto its never-observed mean.

**The honest counterweight (recorded in the claim, not hidden).** V3-EXQ-772's potential-based
shaping changes advantage *shape*, not just scale, so a pure scale operator would **not** divide it
out -- and 772 still floored. The claim survives only in the weaker form that the shape change is
swamped because standardisation re-amplifies the co-present novelty noise (`0.1/sqrt(n)`, firing on
**every** step and dominant in a ~0-forage episode) back to unit variance alongside it. That weaker
form is what the falsifier tests.

**Structural caveat.** DreamerV3 also trains its actor entirely on **imagined** 15-step rollouts;
REE trains on **real `env.step` calls only**, and SD-056's `e2` is a contrastive *representation*,
not a rollout source. That ingredient is a **structural** difference, not a tuning one, and is
explicitly **out of scope** for MECH-459 -- it is the `DREAMER-V3-P-008` open-loop horizon-divergence
probe instead (`puzzle (known rules)`: the missing fact is measurable without building anything).

**Falsifier.** A shape-preserving normaliser knock-out: replace **only** the per-episode
`(adv - mean)/(std + 1e-8)` with `adv / max(1, Per95(adv) - Per5(adv))`, everything else
byte-identical. If the foraging floor does not move, MECH-459 is refuted.

## 4. MECH-460 -- transient behavioural-prior bootstrap

**Source:** VPT (Baker et al. 2022, arXiv:2206.11795), AlphaStar (Vinyals et al. 2019), DQfD
(Hester et al. 2018), JSRL (Uchendu et al. 2022) -- `REE_convergence/sources/vpt-bc-seed/`.

**The decomposition (the transferable finding).** What a BC prior supplies is **not** primarily a
competent action distribution. The evidence forces **tractable exploration / state-visitation** as
the primary function: VPT reports that RL from a random initialisation in the same action space
obtains essentially no reward and never reliably reaches even the first link in the item chain,
while VPT-initialised RL reaches the diamond pickaxe -- a **presence/absence** result, not a
speed-up. Three further functions are separable: a competent action distribution (the *vehicle*),
**value-side grounding** (DQfD's large-margin loss; plain BC does **not** supply it, and its
ablation costs most of the benefit), and **strategic-diversity preservation** (AlphaStar).
Representation transfer is unsupported by these sources.

**Transience -- where the literature is weakest, and REE's real question.** None of VPT, AlphaStar
or DQfD anneals its prior term to zero: the first two keep a frozen prior permanently as a KL
regulariser, DQfD never evicts demonstration transitions. The only strong transience construct is
**JSRL's rollout handoff**: a guide policy acts for the first `h` steps and the exploration policy
for the remaining `H - h`, with `h` *decreasing* as the exploration policy clears a threshold; at
`h = 0` the guide is out of the action path entirely.

**Why REE needs no permanent external demonstrator.** REE already owns both demonstrator candidates
**in-substrate**: `LocalViewGreedyPolicy` (48-55) and `OraclePolicy` (57-61), instantiated in
`ree-v3/experiments/_lib/mech457_fanout.py::run_anchor_cell` -- the same deterministic reference
policies that produced the readiness numbers. Under JSRL's admissibility bar (better than random,
manual engineering explicitly permitted) either qualifies. The demonstrator is **a hand-written
function inside REE's own experiment lib**, so REE's transience question is not "how do we stop
paying for demonstrations" but the cleaner **"does the seed leave a residue in the converter after
the guide leaves the action path."**

**Delta vs what V3-EXQ-780 already instantiates** (mapping, *not* a change request):

| Literature mechanism | In 780? |
|---|---|
| BC warm-start on demonstrator-visited states | Yes (`warmstart_bc_rep`, `mech457_explorer_classes.py:335`, 300 eps) |
| Persistent pull toward the prior during RL | In *form* only -- 780 uses a CE auxiliary to the **live** demonstrator (`bc_aux_coef=0.5`); the literature's anti-forgetting result is for **KL to a frozen snapshot of the agent's own post-BC weights** (demonstrator departed). Different objects. |
| Coefficient annealing | Absent -- and absent from all four papers too |
| Value/critic-side seeding (DQfD margin) | Absent -- 780 seeds `logits` only; `value_head` / the SF critic (`reward_w` zero-init) start **cold** |
| Rollout handoff `h -> 0` | Absent -- no guide/exploration split in the episode |

**Falsifier.** Competence that collapses to the 0-1 floor the instant the prior leaves the action
path (JSRL `h = 0` endpoint) refutes the *seed* reading -- the prior would be a permanent crutch,
not a bootstrap. A **flat** response across demonstrator quality (`random_walk` /
`local_view_greedy` / `greedy_oracle`) also refutes it and points at the converter, not the seed.

## 5. MECH-461 -- innate action-primitive basis + reward-independent engagement drive

**Source:** the mandatory biology `/lit-pull` discharged **before** registration per the
`biology_before_formal_definitions` invariant --
`evidence/literature/targeted_review_competence_bootstrap_without_demonstrator/` (8 sources).

**The claim, in two parts.**

1. **The action basis is innate and refined, never constructed.** Dominici et al. 2011 (*Science*,
   10.1126/science.1210617): the two neonatal motoneuron primitives are **retained** into adulthood
   and augmented, with matching primitives across rat/cat/macaque/guineafowl. Development refines a
   pre-specified basis. "Learner with no action prior fails" is the biological **default**, not an
   anomaly. Zeng et al. 2021 adds the qualifier that the innate seed is demonstrator-free but not
   *experience*-free: deprived of proprioceptive feedback from its **own self-generated** activity,
   the CPG fails to mature.
2. **A reward-independent engagement drive is necessary.** Ahmadlou et al. 2021 (*Science*,
   10.1126/science.abe9681) dissect a ZIm circuit whose function is converting stimulus presence
   into **investigation**, independent of learned reward value. Szczypka et al. 2001 (*Neuron*) is
   the necessity result and the closest biological analog of REE's signature: dopamine-deficient
   mice with **intact perception, intact motor apparatus and intact hedonics starve in front of
   food** -- readiness met on every leg, foraging at floor.

**The two objections the pull surfaced, recorded in the claim rather than suppressed.**

- **Non-extinction is unmeasured, and the best-specified account points the other way.** Kesner et
  al. 2022 propose *environment prediction error* as seeking's currency -- which **quiesces** as the
  world model improves. No source tests a drive surviving sustained non-reward. This lands exactly
  on the property H-approach-primitive most needs.
- **The biological failure mode is a CEILING deficit, not a FLOOR one.** Volman et al. 1995: untutored
  finches sing -- structured but abnormal. Demonstrator-deprivation in biology degrades competence;
  it does not produce REE's near-zero floor. This is a substantive mismatch that travels with any
  downstream use of the analogy, in **either** direction.

**A framing correction worth carrying forward.** The "is the prior outgrown?" worry **inverts** in
biology. Mackevicius et al. 2023 (*eLife*): sequences self-organise with **no** tutor, tutor content
then binds onto that scaffold -- and the birds that **failed** to learn were those whose *untutored*
sequences had already crystallised. Biology's risk is **premature crystallisation of self-generated
structure locking out later demonstrator input**, not a BC prior becoming a permanent crutch.

**Falsifier.** A sustained, non-extinguishing approach drive that leaves the actor at the passive-
survival floor on both representations (the V3-EXQ-781 pre-registered null, with
`mean_approach_reward_recent` confirming the drive actually fired) refutes it.

## 6. What this stub does NOT do

- **It does not adjudicate H-bc-prior vs H-approach-primitive.** MECH-459 in particular is a
  **third** option -- demonstrator-free convergence via value-pathway stabilisation, with neither
  an imitation seed nor an innate drive. Its existence **widens** the hypothesis space. It must not
  be allowed to pre-empt the running experiments.
- **It does not read the 32.72 imitation result as support for the bc-prior leg.** BC is a
  supervised cross-entropy update that **never touches the return pathway at all** -- so the one
  method that works is exactly the one that bypasses the value/advantage machinery. That is equally
  consistent with all three claims here. BC clearing the floor **does not discriminate**, which is
  precisely why every falsifier above is about an *intermediate* quantity rather than final foraging
  competence.
- **It does not license a build.** Not the twohot critic, not the percentile normaliser, not an
  imagination loop, not a guide-policy handoff. `mech457_competence_bootstrap_explorer` stays
  `blocked_pending_discrimination`.
- **It does not promote or demote anything.** MECH-457 stays `candidate` / `v3_pending`; all three
  new claims are registered `candidate`.
- **It does not register a third hypothesis in the pre-registration registry.** MECH-459 is a
  claim, not a pre-registered hypothesis; whether `competence_floor` should gain a third ALIVE leg
  is a `/governance` decision under the GOV-FANOUT-1 growth contract, deliberately left to that
  process.

---

## 7. MECH-475 -- uninformative value baseline makes optimisation iatrogenic

Registered `candidate` / `v3_pending` 2026-07-22 (`/claim-synthesis`, `split_from: MECH-457`;
`evidence/planning/claim_synthesis_MECH-457_2026-07-22.md`, user-approved per-child).

**Claim.** In REE's MECH-457 actor-critic pathway the value baseline is **uninformative on the
policy's own state distribution** (V3-EXQ-782 R-(b): `std(V)/std(G) = 0.041` against a 0.25
collapse threshold; pre-reward-vs-far separation 0.016 against a 0.25 floor), so the advantage
carries variance rather than signal and **added optimisation pressure is iatrogenic** -- it drives
competence *below its own control* rather than plateauing under a ceiling.

**The five instances (read as a set, which no single autopsy could):**

| target | intervention | control | treatment | direction |
|---|---|---|---|---|
| V3-EXQ-769 | more capacity + 5x budget | raw ON 6.48 | 0.12 | worse |
| V3-EXQ-781 | earned approach drive (fired 0.70) | raw 2.983 | 0.200 | worse |
| V3-EXQ-771 | metabolic reward-coupling | reward 3.47 / survive ~170 | 1.12 / death 100% | worse |
| V3-EXQ-780 | unconstrained RL after BC install | post-BC 20.933 | 11.667 | worse |
| V3-EXQ-789 | RL vs persistent imitation auxiliary | installed | decayed at every schedule | worse |

**Why not MECH-459 re-labelled.** MECH-459 (section 3) asserts the two-sided normaliser makes the
gradient scale-invariant, so magnitude levers **cannot move** the floor -- an *inertness*
prediction. MECH-475 asserts the baseline is uninformative, so added optimisation **actively
degrades** -- a *destructiveness* prediction. They predict opposite signs, and 769/781/771 are
magnitude-class levers MECH-459 calls inert that were in fact destructive. MECH-459's own probe
splits the same way: V3-EXQ-782 R-(a) **weakened** its normaliser half while R-(b) **corroborated**
its critic half -- MECH-475 is that corroborated half promoted to a falsifiable object.

**Positive control already on file.** V3-EXQ-788: a distributional critic **retains** 1.839 of
installed competence where the scalar critic does not.

**Falsifier (decisive).** Re-run the three destructive acquisition-side treatments (769 / 781 /
771) with the V3-EXQ-788 distributional critic in place, else byte-identical. SUPPORTED if the
treatment-below-control inversion reverses or flattens in >= 2 of 3; WEAKENED (and withdrawn) if
treatments still land below their own controls with an informative baseline. Trajectory, not
terminal. Full `what_would_answer` + lit grounding (Sutton 2000 baseline-as-variance-reduction;
O'Doherty 2004 silent-critic-as-lesion; Rothenhoefer 2017 VS-lesion, recorded as a two-way
divergence; Salamone 2003 / Szczypka 2001 DA-deficient starving-in-front-of-food) in the claim
body and the synthesis document. Owed: `/lit-pull targeted_review_mech_457_baseline_informativeness`.

## 8. MECH-476 -- competence retention dissociable from acquisition

Registered `candidate` / `v3_pending` 2026-07-22 (`/claim-synthesis`, `split_from: MECH-457`).

**Claim.** **Acquiring** competence and **retaining** it are dissociable capabilities with separate
substrate requirements; REE has the first and lacks the second. BC installs foraging competence at
20.933 on raw_view (3/3 seeds) and 32.72 on z_world; unconstrained RL then erodes it to 11.667,
while a distributional critic (788: retains 1.839) and a KL anchor to the installed snapshot (792:
retains 0.778 vs 0.525 unconstrained, still plastic) each preserve it. Retention is set by the
**value estimator** and the **update constraint**, not by continued demonstration (789 eliminates
the imitation-auxiliary schedule axis at every setting).

**Distinctive, testable content -- what MECH-459/460 do not assert.** MECH-459 owns the critic
lever; MECH-460 owns the behavioural-prior lever (and already names KL-to-a-frozen-own-snapshot).
Neither asserts the **dissociation itself** (retain-without-acquiring: the KL anchor acquires
nothing; acquire-without-retaining: BC), nor **consolidation-as-interference-resistance**, which
makes install **dose** and offline **interval** the untested levers -- V3-EXQ-780 ran a single BC
dose straight into RL with no offline interval, so REE has never tested for a consolidation
*process*, only for concurrent *regularisation*.

**Falsifier.** An A -> B -> A retrograde-interference design (Krakauer 2005): A = BC-install; B =
interfering unconstrained-RL phase; re-measure A. Vary install **dose** and A->B **interval**.
SUPPORTED if interference-resistance grows with dose and/or interval (a consolidation process);
WEAKENED (and withdrawn into MECH-459/460) if retained fraction is invariant to both and tracks
only the concurrent constraint coefficient. Third arm from behavioural tagging (Moncada 2007):
pair a sub-threshold BC dose with a novelty episode (the landed RND drive) inside the window --
SUPPORTED if it consolidates only in the novelty-paired condition. Retained-fraction trajectory,
never terminal; an install that did not take self-routes `substrate_not_ready_requeue`. Lit
grounding (Krakauer 2005, Walker 2003, Moncada 2007, STC review Bin Ibrahim 2024; known
sleep/replay/trace-selectivity divergence recorded) in the claim body. Owed: `/lit-pull
targeted_review_mech_457_consolidation` (trace-selective vs global). Cross-link:
`evidence/planning/sleep_substrate_plan.md` (SD-017 / MECH-204) is the natural home if the interval
arm returns SUPPORTED.

## 9. What sections 7-8 do NOT do

- **They do not promote or demote MECH-457.** It stays `candidate` / `v3_pending`, retained as the
  narrowed umbrella; MECH-475/476 are registered `candidate`.
- **They do not license a build.** Not the distributional critic as a standing default, not a
  consolidation window -- each is a *falsifier design*, gated on its experiment resolving.
- **They create no pre-registration fan-out growth event.** MECH-475's reading rides the existing
  `conversion_ceiling_root` H-objective-misspecification leg; MECH-476's rides the existing
  `competence_floor` H-retention-critic / H-retention-consolidation legs.
