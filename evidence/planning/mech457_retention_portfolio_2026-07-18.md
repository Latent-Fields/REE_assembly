# MECH-457 RETENTION discrimination portfolio (GOV-FANOUT-1 consumer half)

- **Generated:** 2026-07-18
- **Session:** `priceless-lewin-f47019` — "MECH-457 retention fanout portfolio"
- **Producer half:** `failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18.{md,json}` → `cluster_pattern.fanout_recommendation`
- **Question:** `competence_floor` in `hypothesis_space_registry.v1.json`
- **Claims:** MECH-457 (candidate / v3_pending), INV-088 — **this portfolio promotes and demotes nothing**
- **Status:** legs PRE-REGISTERED; probes **substrate-blocked**, zero experiments queued

---

## Headline

The four-leg retention portfolio recommended by the 780/781/782 cluster autopsy is **designed and pre-registered, but not queued: all four legs require substrate that does not exist.** The Step 2.5 readiness gate of `/queue-experiment` is a hard stop — no script written, no queue entry appended. Each leg's missing capability is minted below as a named `complicated (buildable)` node in `substrate_queue.json`, which is the correct route (`/implement-substrate`, not another `/queue-experiment` iteration).

This inverts the standing work-graph reading. `substrate_queue.json:mech457_competence_bootstrap_explorer` sits at `blocked_pending_discrimination` — waiting on a discrimination to license the build. That discrimination is **itself build-gated**. The node stays `blocked_pending_discrimination`; what changes is that its blocking discrimination now has four named, buildable prerequisites instead of an unspecified one.

---

## 1. Why the question changed shape

Ten prior legs of the `competence_floor` campaign asked **which mechanism PRODUCES competence**. Every one was adjudicated against a treatment arm that never left the ~0–1 floor (credit sweep 0.2–0.45; archive/return, curriculum, arbitration all collapsing to the sparse-RL baseline).

V3-EXQ-780's `raw_view` arm broke that. It reached **20.933** foraging competence immediately post-BC — the **first supra-lift-target observation in the entire campaign** (target 13.05, inside the 32.72 BC-expert band, against a 48.05 `local_view_greedy` ceiling). RL refinement then **eroded it to 11.667**.

780 was self-routed `bc_prior_not_the_axis`. That self-route was **REJECTED on autopsy**: its pre-registered null required "treat still forages ~0 both reps", and 11.667 / 20.933 falsifies the null's antecedent. H-bc-prior was therefore **not eliminated** and remains `alive`.

So the open question is no longer *which mechanism produces competence* — a behavioural prior demonstrably does. It is **why produced competence is not RETAINED**. That inversion also runs against the biological expectation: reward-driven refinement of an imitated skill should improve it, not degrade it.

V3-EXQ-782 R-(b) supplies the leading mechanism candidate: the shared CTRL critic is **flat and uninformed** — `std(V)/std(G) = 0.041` against a 0.25 collapse threshold, pre-reward-vs-far separation ratio **0.016** against a 0.25 floor. An uninformed baseline yields an unbaselined, high-variance advantage, which is exactly what drifts a policy off an installed prior.

**The prior ten legs could not have detected a retention deficit, because their arms never produced competence to retain.**

---

## 2. The four legs

Reference build for all legs: the **NON-REGRESSED** configuration — 128-wide / 3x budget / `z_world` detached / credit-replay 3 / topk 32. **NOT** the 769-falsified 256/5x.

Reference bands: competence floor **1.0** · RND plateau **5.22** · lift target **13.05** · BC-expert **32.72** · `local_view_greedy` ceiling **48.05** · `greedy_oracle` **57.2** · random_walk **0.933**.

| hid | Axis | Intervention | Null (declared) |
|---|---|---|---|
| `H-retention-critic` | `algorithm` | BC-install to the raw_view ~20.9 point, then the SAME RL refinement with a distributional/two-hot critic vs the current scalar critic | The installed prior erodes identically under both critics → the critic baseline is **not** the retention mechanism |
| `H-retention-consolidation` | `policy` | BC-install, then RL with a trust-region / KL-anchor to the **installed** policy vs unconstrained | Anchoring does not preserve competence → retention is **not** a drift-protection problem |
| `H-retention-auxiliary-decay` | `learning-signal` | BC-install, then sweep `bc_aux_coef` persistence (constant / annealed / off), measuring competence **half-life** | Half-life invariant to the schedule → the prior is **not** being out-competed by the RL objective |
| `H-consummation-binding` | `intrinsic-architecture` | Approach drive gated to **EXTINGUISH** on resource contact and hand off to a consummatory act, vs 781's non-extinguishing terminal drive | Competence still flat → the binding is **not** what 781 lacked |

`H-consummation-binding` is motivated by 781's load-bearing positive finding: the approach drive was earned at **0.707** while raw_view foraging was *suppressed* to **0.200** from a **2.983** control, tight across all three seeds — approach-without-consummation.

### Mandatory design constraints (carried into every leg's eventual script)

1. **Trajectory, not terminal.** Every leg MUST record the post-installation competence **trajectory**. Terminal-only measurement is precisely what kept this deficit invisible for ten legs. `H-retention-auxiliary-decay` reads a half-life, which is a trajectory statistic by construction; the other three must sample competence on a fixed post-install schedule.
2. **Interpretation grid MUST enumerate a "manipulation succeeded and then decayed" branch.** V3-EXQ-780's grid enumerated only a ~0 null, so a *successful* manipulation was scored as a null — and the covariate that catches it (`post_bc_foraging_competence`) was already present and declared, but never consumed by the routing logic. **Route on declared covariates, not only on the terminal criterion.**
3. **Install verification is a precondition, not a result.** 780's `z_world` arm took the BC seed 0/3 (post-BC 0.583) while raw_view took it 3/3 at 20.933. A leg whose install did not take is uninformative about retention and must self-route `substrate_not_ready_requeue`, never a retention verdict.

### Anti-alias audit

`H-retention-critic` and `H-retention-consolidation` can **both** yield "competence preserved". They are kept separable by construction:

- the **critic** leg changes the **value estimator** (what the baseline knows), leaving the update rule untouched;
- the **consolidation** leg changes the **update constraint** (how far the policy may move), leaving the value estimator untouched.

**A leg that changes both aliases them and is disallowed.** This is the reason `H-retention-consolidation` must be operationalised as a KL-anchor to a *frozen snapshot of the installed policy* rather than via the BC auxiliary: anchoring through `bc_aux_coef` would anchor to the *demonstrator*, aliasing directly with `H-retention-auxiliary-decay`.

### Coverage audit

The four legs partition the retention pathway into: what the baseline **knows** (critic), how far the policy may **move** (consolidation), how long the prior is **held** (auxiliary decay), and whether the drive **terminates correctly** (consummation binding). The first three are retention-of-an-installed-policy; the fourth tests whether 781's drive-side null was itself an artefact of a missing consummatory act. No live hypothesis from the autopsy's `live_hypotheses` block is unrepresented.

---

## 3. Axis-family reasoning (stated explicitly, not left to the map)

`axis_families.map` groups per-leg axes into families so `build_hypothesis_space.py` can distinguish **successive refinement** from **CIRCLING** (new legs re-entering a family that already holds eliminated legs). The `process` family already holds 6 eliminated legs, so this portfolio invites a circling verdict.

**Two corrections, in order of weight.**

**(a) The autopsy's caution overstates the arithmetic.** It states that three of the four axes (`algorithm`, `policy`, `learning-signal`) map to `process`. Read against the live map, `learning-signal` maps to **`constitution`**, not `process`. The actual split is:

| Axis | Family |
|---|---|
| `algorithm` | `process` |
| `policy` | `process` |
| `learning-signal` | **`constitution`** |
| `intrinsic-architecture` | **`constitution`** |

So **two** of four re-enter `process`, not three, and two land in `constitution`.

**(b) The re-entry that remains is not circling, and the distinction is measurable rather than rhetorical.** Every eliminated `process` leg intervened on how competence is **DISCOVERED**, adjudicated against an arm at the ~0–1 floor. These legs intervene on whether **already-installed** competence is **RETAINED**, are adjudicated from a **20.933** starting point, and read a **trajectory** rather than a terminal value. A retention deficit was not merely unobserved by the prior legs — it was **unobservable** to them, because their arms never produced competence to retain.

**Decision: keep the locus-based axis labels; do NOT introduce a `retention` axis.** `axis_families` is explicitly drawn on **intervention locus** ("what layer of the system a hypothesis blames"), and the map's own `_provenance_caveat` names confirmation-by-construction as the live risk it guards against. "Retention" is a **question shape**, not a locus. Minting a `retention` axis would encode question-shape into a locus taxonomy purely to dodge an unfavourable score — which is the gerrymandering the caveat warns about, done deliberately. A critic swap is an `algorithm` intervention whether the question is discovery or retention.

Consequently **no new row is added to `axis_families.map`**, and no `indeterminate` convergence_class is forced. The dispute is recorded here and in the growth event's `note`, which is the mechanism the map's `_authority` field designates: *"Disputing a row here is the correct way to dispute a convergence verdict."*

---

## 4. Re-derive brake — permits (not re-derived)

MECH-457 carries **6** prior `substrate_ceiling` / `non_contributory` autopsies, far past the threshold of 2, so `/queue-experiment` Step 2.5b flags it. The producer-half autopsy records `re_derive_brake.fired: false` with an explicit rationale, which this consumer half **reads rather than re-derives**:

- **different question** — retention of installed competence, not discovery of it;
- **different null** — erosion-under-manipulation, not stays-at-floor;
- **different measurement** — competence trajectory post-installation, not terminal competence;
- **a positive control no prior leg possessed** — raw_view reached 20.933, where all 6 braked autopsies adjudicated arms stuck at the ~0–1 floor.

The brake is not being overridden; it does not apply to a re-pose with these four properties.

---

## 5. Substrate readiness — ALL FOUR LEGS BLOCKED

`/queue-experiment` Step 2.5 verified each leg's required capability against the live substrate. Evidence is `file:line` from `ree-v3/`.

| Leg | Required capability | Status | Evidence |
|---|---|---|---|
| `H-retention-critic` | distributional / two-hot critic | **ABSENT** | Value head is `nn.Linear(hidden, 1)` (`ree_core/action_learning/actor_critic.py:110`, decoded `:147`); loss is scalar MSE (`experiments/_lib/mech457_fanout.py:255,422`; `mech457_explorer_classes.py:699,799`). Zero hits for `twohot` / `hl_gauss` / `value_bins` / `atoms` / `symlog` in `ree_core/` or `experiments/`. |
| `H-retention-consolidation` | KL-anchor to a frozen policy snapshot | **ABSENT** | No `kl_coef` / `kl_penalty` / `ref_policy` / `target_kl` anywhere. No policy `deepcopy` / `state_dict()` snapshot in any `_lib` training module. "frozen" in `actor_critic.py:31,76` refers to a frozen **z_world encoder**, not a policy. PPO clip exists only in `v3_exq_734:210,581` — the 457 loop is vanilla A2C with no ratio and no clip (`mech457_fanout.py:254-257`). |
| `H-retention-auxiliary-decay` | `bc_aux_coef` **schedule** | **ABSENT** (cheapest gap) | `bc_aux_coef` is a constant float (`mech457_explorer_classes.py:537`), read once per episode (`:702`). The scheduling pattern already exists beside it — `coef_schedule` / `entropy_schedule` are `(ep, n_episodes) -> float` callables at `:535`, applied at `:616-617`. ~6 lines to mirror. |
| `H-consummation-binding` | consummatory act distinct from movement | **ABSENT** (most invasive) | `ACTIONS = {0..4}` is four moves + no-op (`causal_grid_world.py:79-81`); consumption is **automatic on cell entry** (`:1931-1936`, inside the move branch of `step()`). Adding a CONSUME action changes `action_space_size` (`:1185`) and therefore every actor head's `action_dim`, and busts all cached arm fingerprints. |

**One escape hatch was checked and fails.** The successor-feature critic (`use_sf_critic`, `actor_critic.py:116-125`) looked like a built alternative value estimator. It is not usable here: it is hard-wired `False` on every 457 path (`mech457_fanout.py:153,335`; `mech457_explorer_classes.py:830`), has no field in `BootstrapExplorerConfig` (`mech457_bootstrap_explorer.py:108-152`), and **its training losses live only in V3-EXQ-742** (`v3_exq_742:357-372`) — nothing in `_lib` computes the psi Bellman target or the reward regression. Flipping the flag without porting that block leaves `reward_w` at zero-init and `V_SF ≡ 0`: an **untrained** critic, not an alternative one. That would be a degenerate arm read as a scientific verdict — the exact P0-readiness trap the skill's readiness gate exists to catch.

**Note the drive half of leg 4 IS built.** Extinction-on-contact is the default (`causal_grid_world.py:1931-1932`, per-axis `:1955-1972` with `per_axis_restoration_fraction = 1.0` driving the axis drive to exactly 0), and the anti-extinction knobs (`goal.py:64` `drive_ema_alpha`, `:81` `drive_floor`) are wired. Only the **consummatory act** — contact affording rather than effecting consumption — is missing.

---

## 6. Routing

Four `complicated (buildable)` nodes minted in `substrate_queue.json`. Each is a named build with no open question, so the route is `/implement-substrate`, **not** another `/queue-experiment` iteration.

| sd_id | Leg unblocked | Size |
|---|---|---|
| `mech457_distributional_critic` | `H-retention-critic` | moderate — bin support + target projection + CE loss + expectation-decode for GAE |
| `mech457_policy_kl_anchor` | `H-retention-consolidation` | moderate — policy snapshot + KL penalty term against a frozen reference |
| `mech457_bc_aux_schedule` | `H-retention-auxiliary-decay` | **small (~6 lines)** — mirror the proven `entropy_schedule` callable pattern |
| `mech457_consummatory_act` | `H-consummation-binding` | large / invasive — changes `action_space_size`, so it re-keys every actor head and busts cached arm fingerprints |

Recommended build order: `mech457_bc_aux_schedule` first (smallest, proven pattern, and its leg reads a half-life so it is the most direct trajectory measurement of the four), then `mech457_distributional_critic` (attacks the measured 782 R-(b) candidate directly), then `mech457_policy_kl_anchor`, with `mech457_consummatory_act` last on cost.

**Queue nothing until at least two legs are buildable.** GOV-FANOUT-1 exists precisely because adjudicating a leg in isolation is how a confident-but-wrong elimination enters the frozen ledger — validated concretely by this very cluster, where 781's elimination alone would have rested on no demonstration that competence was reachable at all, and 780 alone would have recorded an elimination its own covariate falsifies.

`mech457_competence_bootstrap_explorer` stays `blocked_pending_discrimination` throughout. MECH-457 stays candidate / v3_pending. **This portfolio promotes and demotes nothing.**

---

## 7. Ledger delta

Four legs appended to `competence_floor` as a labelled fan-out growth event per invariant `labelled_fanout_growth`:

- `initial_frozen_count`: **12 → 16**
- `initial_frozen_count_at_registration`: **7 — UNCHANGED**
- `fanout_source`: this document
- each leg carries `pre_registration_source` pointing here

**Invariant 3a(a) holds trivially and maximally cleanly:** these legs have **no adjudicating runs at all** — their probes are substrate-blocked and nothing is queued — so pre-registration necessarily precedes any resolution, and the git commit of this document is the durable witness.

**On the numerator.** Registering four legs moves the surviving-vs-frozen ratio from 2/12 = 0.167 to 6/16 = 0.375. That direction is **honest and unflattering**: it records that the question just got *wider*, not that it narrowed. This is the opposite of the padding the sanctioning decision flagged when it declined `H-return-scale` (which would have moved 0.167 → 0.231 purely by adding an unadjudicated leg to the numerator at *adjudication* time). Registering at **fan-out design time**, before any probe exists, is the moment the invariant sanctions.

The producer-half autopsy deliberately registered nothing, honouring V3-EXQ-782's pre-declaration that an already-concentrated reading makes no registry write. That deferral is discharged here, by the session that designed the portfolio.

### Recurrence flag — fired by this write, and answered

`check_hypothesis_space_integrity.py` returns **0 flags (a=0 b=0 c=0 d=0)** and records the four new legs as git-witnessed pre-registrations. It does raise one **ACTIONABLE** signal, which fires because this is `competence_floor`'s **third** labelled portfolio:

> *fan-out recurrence (N>=3 portfolios): the question may be MIS-POSED rather than under-enumerated. Re-pose the operationalization before opening another portfolio (routing only; promotes/demotes nothing).*

**That flag is correct, and this portfolio is what it asks for rather than another instance of what it warns against.** The warning is against opening a further portfolio *on the same operationalization*. This portfolio changes the operationalization itself: from "which mechanism produces competence" (terminal competence, adjudicated against a floor-bound arm) to "why is produced competence not retained" (competence trajectory, adjudicated from a 20.933 positive control). The autopsy reaches the same conclusion independently — *"the campaign was posing the wrong question shape for all ten previously-resolved legs"* — and its non-convergence caveat explicitly warns that an improving reduction ratio "should not be read as approaching an answer".

So the flag is discharged by re-posing, not by enumeration. **If these four legs resolve and a fourth portfolio is proposed on the retention operationalization, the recurrence flag should be treated as blocking at that point** — that would be the pattern it exists to catch.
