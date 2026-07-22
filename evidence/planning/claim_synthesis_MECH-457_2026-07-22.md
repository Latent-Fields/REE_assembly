# Claim synthesis — MECH-457 (competence floor / conversion ceiling)

**Status: PROPOSAL. Registers nothing. Promotes nothing. Demotes nothing.**
**Generated:** 2026-07-22T04:36:55Z · session `elegant-curran-fe12ba`
Trigger: granularity-debt recurrence fired in
`failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22` §6
(19 confirmed autopsy targets across 8 files, structurally distinct signature each time).

Nothing below reaches `claims.yaml` without explicit per-child user approval.

---

## 0. The governance conflict this proposal must clear first

`MECH-457` currently carries:

```yaml
granularity_debt_disposition: coherent_campaign   # GOV-GRAN-1 human-adjudicated 2026-07-16
```

whose note says **"/claim-synthesis CONTRAINDICATED: a split would duplicate
ARC-065/MECH-314, MECH-455 and INV-088 -- every candidate sub-claim already has an
owner."** That adjudication was correct on the evidence available on 2026-07-16 and it
is not being overturned casually. Five things have changed since, and they are the
whole warrant for re-opening:

1. **+9 autopsy targets** (765 was the newest at the time of that disposition; the
   corpus now runs through 769 / 770 / 771 / 772 / 780 / 781 / 782 / 788 / 789 / 792 /
   734 / 737b / 742a).
2. **The question shape changed, twice, by explicit user adjudication.**
   `competence_floor_reposing_2026-07-19.md` §5c split `H-bc-prior` three ways —
   *acquisition* CONFIRMED, *retention* OPEN, *installability-on-z_world* OPEN. The
   campaign's first ten legs all asked "which mechanism PRODUCES competence" against an
   arm that never left the floor; that is no longer the open question.
3. **The 2026-07-16 note's own anti-duplication argument no longer holds.** It named
   ARC-065 / MECH-314 / MECH-455 / INV-088 as the owners of every candidate sub-claim.
   Those are all *drive-side / diversity-side* owners. Neither of the two children
   proposed here is a drive claim; and MECH-459/460/461 — registered **2026-07-18, after
   that disposition** — are themselves a partial decomposition of MECH-457, which is
   evidence the campaign has already been decomposing under a field that says it should
   not.
4. **GOV-FROZEN-1 now reports `convergence_class: CIRCLING`** for `qid
   competence_floor` — 16 legs, `families_closed [instrumentation, representation,
   world]`, **`families_fresh` EMPTY** — and its recorded response, quoted in MECH-457's
   own note, is *"RE-POSE the operationalization, not open portfolio 4."* **A
   decomposition is the re-pose.** The registry is already asking for this operation
   under a different name.
5. **The re-derive brake does NOT fire.** MECH-457 = **0** confirmed `substrate_ceiling`
   hits under the R1–R3 convention across all 19 targets. This is not a
   ceiling-exhaustion demotion case.

**If the children below are approved, the `granularity_debt_disposition` field must be
updated in the same pass** (`coherent_campaign` → a decomposed disposition naming the
children and this document). Leaving it as-is would put a contradiction in the registry.

### Honest reading of the "19 targets" number

19 is a count of **autopsy targets in the campaign**, not of claim-weighted `weakens`
entries against MECH-457. Several targets carry `claim_ids: []` (728, 734, 737a — all
diagnostics), and V3-EXQ-711/713 tag MECH-439 / ARC-108 / ARC-110 rather than MECH-457.
Only 742/742a, 765, 769, 770–772, 780, 781, 789, 792 tag MECH-457 directly, and most of
those are `diagnostic` / `non_contributory`. The recurrence signal is real, but it is a
signal about **how many structurally different ways this claim has been probed**, not
about accumulated negative weight. Read it that way.

---

## 1. Step-3 discrimination gate

Classified target by target. Only the fourth class is granularity debt.

### 1a. EXCLUDED — test-design / instrument debt

| Target | Why excluded |
|---|---|
| **V3-EXQ-780** | Interpretation-grid defect. The grid enumerated only a `~0` null, so a **successful** manipulation was scored as a null; the covariate that catches it (`post_bc_foraging_competence`) was declared and never consumed. Its *result* is load-bearing below; its *FAIL label* is not signal. |
| **V3-EXQ-792** | Under-powered (n=3) with a structurally weak control (the unconstrained arm's KL is a hard-coded `0.0` sentinel, not a measurement). The **load-bearing criterion PASSED**; a `load_bearing: false` dose-response leg vacated it. |
| **V3-EXQ-711 / 713** | Hold-weighted E3 readout (pseudo-replication form 2). Also not MECH-457-tagged. |

### 1b. EXCLUDED — substrate-not-ready / implementation defect

| Target | Why excluded |
|---|---|
| **V3-EXQ-750** | `substrate_starved_precondition_unmet`. |
| **V3-EXQ-728** | Untrained z_world encoder; `claim_ids: []`; self-route `substrate_not_ready_requeue` UPHELD. |
| **V3-EXQ-734** | `encoder_moved_in_p0: false` on all 4 rungs × 4 seeds — z_world a frozen random projection. Run INVALID. |
| **V3-EXQ-737a** | REE-latent arms confounded by the same defect (the `ppo_raw_obs` control arm is valid and is counted below). |
| **V3-EXQ-742a frozen arms** | `encoder_moved_in_p0: false` in P0 on every arm; only the two `cotrain` arms are valid. |
| **780's z_world half** (BC install 0/3, post-BC 0.583) | Same defect class. **This is why no "z_world installability" child is proposed** — see §5. |

`sd_zworld_warmup_optimizer_group` is `implemented_pending_validation` and its adoption
is **per-copy incomplete** (728b validated one driver; 734 and 742a are two more copies
it did not reach). That is an owned `complicated (buildable)` node, not a missing claim.

### 1c. EXCLUDED — genuine single-point falsification

None. MECH-457's *necessity* assertion has never been falsified; what has repeatedly
failed is an implicit *sufficiency* reading the claim text never separates out. There is
no clean single reproducible FAIL of the claim as written, so the demotion route does
not apply.

### 1d. RESIDUE — genuine, non-degenerate, substrate-ready, structurally distinct

Eighteen surviving signatures, every one with `control_passed: true`,
`non_degenerate: true`, and readiness anchors clearing the floor
(`local_view_greedy` 48.05, `greedy_oracle` 57.2 vs a 1.0 floor):

| # | Target | Distinct signature |
|---|---|---|
| 1 | 747 / 749 | representation is not the wall (`H-rep` eliminated) |
| 2 | 748 | sparsity *is* a wall, but a dense teacher reaches only ~11% of ceiling |
| 3 | 751 | RND clears the floor unsupervised (5.22) — **necessary, not sufficient** |
| 4 | 752 | backward credit-sweep collapses to sparse-RL baseline |
| 5 | 753 | Go-Explore archive/return collapses likewise |
| 6 | 754 | AMIGo goal-frontier curriculum collapses likewise |
| 7 | 755 | explore/exploit arbitration adds nothing over fixed RND |
| 8 | 765 | composed explorer plateaus at ~13% of the achievable ceiling |
| 9 | 769 | capacity amend **regresses** (raw ON 6.48 → 0.12); avoidance learned *without* approach |
| 10 | 770 | drive-schedule not the axis |
| 11 | 771 | reward-coupling (metabolic forage-to-survive env) not the axis |
| 12 | 772 | credit-horizon not the axis |
| 13 | 781 | approach drive **earned** (0.70) while foraging **suppressed** (2.983 → 0.200) |
| 14 | 782 R-(a) | forage |adv| mass already concentrated pre-normaliser (C_pre 1.92 / 1.20) |
| 15 | 782 R-(b) | critic **flat and uninformed** — std(V)/std(G) = 0.041 vs a 0.25 threshold |
| 16 | 788 | distributional critic **retains** 1.839 of installed competence (a PASS) |
| 17 | 789 | imitation auxiliary *succeeded then decayed* at every schedule |
| 18 | 737b + 742a-cotrain | every learner **below its own random-walk anchor** while surviving 8.5× the oracle |
| 19 | 780 raw_view | competence installed at **20.933**, eroded by unconstrained RL to **11.667** |

**≥ 2 distinct, genuine, non-degenerate, substrate-ready signatures: the gate CLEARS.
PROCEED to decomposition.**

---

## 2. Step-4 — the common thread

> **In every surviving failure, competence is destroyed by optimisation rather than
> merely not produced by it — MECH-457 names the machinery that optimises and never
> names either the informativeness of the baseline that makes optimisation safe, or the
> retention of a competent point once reached.**

(This sentence was revised after the §4.0 reconciliation. The first draft read *"failure
of the RETURN to make competent foraging its optimum"*; V3-EXQ-771 falsified that
reading — see §4.0 — and the surviving thread is the destructiveness, not the objective.)

The corpus has, without ever saying so in a claim:

- **built** the machinery (`ree_core/action_learning/actor_critic.py`, 2026-07-12) and
  found it does not produce competence;
- **shown competence is representable and installable** on this policy class and
  observation interface (BC 20.9 raw_view 3/3, 32.72 z_world; local_view_greedy 48.05
  from the same 5×5 field);
- **shown RL refinement destroys it** (20.933 → 11.667) and that the destruction is
  preventable (788 critic 1.839; 792 anchor 0.778 vs 0.525 unconstrained, still plastic);
- **shown every learner ends below its own random-walk anchor** at foraging while
  surviving 8.5× longer than the policy that *defines* competence on the DV.

A learner that is worse than random at the scored task and far better than the oracle at
staying alive is not hitting a ceiling. It is **succeeding at a different task**.

MECH-457 bundles three separable propositions and asserts only the first:

1. **Machinery** — a dedicated first-class actor-critic substrate is required
   (MECH-457's actual text; **intact, necessary-not-sufficient, retained**).
2. **Objective** — the return the actor maximises makes competent foraging its optimum
   (**never asserted; now the leading failure account**).
3. **Retention** — an optimum, once reached, survives continued refinement
   (**never asserted; empirically dissociated from acquisition since 2026-07-19**).

---

## 3. Proposed fate of MECH-457

**NARROWED-AND-RETAINED umbrella.** Not superseded, not demoted.

- **Retain** the necessity assertion, unchanged in substance.
- **Add an explicit sufficiency disclaimer** to the claim body: MECH-457 asserts the
  machinery is *required*, not that it is *sufficient*; the sufficiency reading is what
  742 (2026-07-13) weakened and what 770/771/772 recorded as
  "INTACT but necessary-not-sufficient".
- **Wire the two children below as reverse-deps**, alongside the existing
  MECH-459 / 460 / 461 partial decomposition.
- **Status unchanged: `candidate` / `v3_pending`.** The V3-pending gate holds regardless.

---

## 4. Candidate child claims

Ids are **working labels**; allocate the next free MECH-* at registration time (check
`claims.yaml` max **and** recent `git log` for concurrent additions).

### 4.0 The V3-EXQ-771 reconciliation — RUN, and it redirects Child A

Child A was first drafted as *"the deficit is a property of the return, not the
learner"* (objective mis-specification), with V3-EXQ-771 pre-registered as its sharpest
falsifier: 771 ran a **metabolic forage-to-survive** environment, so if the objective
were the wall, competence should have appeared there. **The check is decidable offline
from 771's existing manifest and was run in this session.** Result:

| arm (metabolic env, 771) | foraging competence | survival | **mean_episode_reward** |
|---|---|---|---|
| `greedy_oracle` | 60.77 | 200.0 | **34.25** |
| `local_view_greedy` | 55.53 | 194.9 | **31.58** |
| `random_walk` | 1.47 | 79.8 | **4.56** |
| `metab_ctrl_zworld` | 0.30 | 182.2 | 0.56 |
| `metab_ctrl_raw` | 2.98 | 169.6 | 3.47 |
| **`metab_treat_zworld`** | **0.42** | **70.8** (death rate **1.0**) | **0.90** |
| **`metab_treat_raw`** | **0.62** | **71.2** (death rate **1.0**) | **1.12** |

**On the metabolic env the objective IS well-specified.** Return ranks the scored DV
correctly and steeply: competence earns 31–34, random earns 4.56, and the learners earn
**0.90–1.12 — roughly four times LESS return than a random walk**, while dying in
**100% of episodes** where the controls survive to 170–200 steps.

This is **outcome (b)**: Child A as originally framed is **falsified at first contact,
before any new compute.** A learner that earns a quarter of random-walk return on an
objective that ranks the target behaviour correctly is not "correctly optimising a
different objective". It is not optimising.

**What survives, and what does not.**
- **Does NOT survive:** objective mis-specification as the *mechanism* of the competence
  floor. 771 removes the passive-survival optimum and the floor stays.
- **DOES survive, and matters:** objective mis-specification as a **measurement-validity
  defect of `D3_hazard_free`**. There, `random_walk` earns **−1.006** and the oracle
  survives 20.4 steps against PPO's 175 — the return genuinely does not rank the scored
  DV. Every campaign elimination measured on `D3_hazard_free` (752–755, 765, 769, 770,
  772, 737b, 742a) was therefore conducted on a yardstick where the scored behaviour is
  not return-optimal. That does not make the objective the cause; it makes those
  **eliminations weaker than they read**. This is the same shape as MECH-459's
  "the invariance may be a property of the measuring instrument" argument, on a
  different instrument.
- **The 2026-07-22 user adjudication is not overturned here** — it selected objective
  mis-specification over the `learner_or_observability_ceiling` reading for the
  734/737b/742a cluster, and on `D3_hazard_free` that selection stands. What 771 shows
  is that the reading does not *generalise* into a mechanism claim. **This needs the
  user's call** (§8).

**What the 771 numbers point at instead** is drafted as the revised Child A below.

---

### Child A (REVISED after §4.0) — `uninformative_baseline_makes_optimisation_iatrogenic` (working id **MECH-462**)

**The pattern 771 exposed, which no claim in the registry names.** Across the corpus,
interventions that add optimisation pressure or an earned learning signal to REE's
actor-critic pathway make competence **worse than their own controls** — not merely
inert:

| Target | Intervention | Control | Treatment | Direction |
|---|---|---|---|---|
| 769 | more capacity + 5× budget | raw ON 6.48 | **0.12** | **worse** |
| 781 | earned approach drive (fired at 0.70) | raw 2.983 | **0.200** | **worse** |
| 771 | metabolic coupling | reward 3.47 / survive 170 | **1.12 / die 100%** | **worse** |
| 780 | unconstrained RL after BC install | post-BC 20.933 | **11.667** | **worse** |
| 789 | RL vs a persistent imitation auxiliary | installed | **decayed at every schedule** | **worse** |

Five independent instances. A ceiling does not do this; a ceiling plateaus. **Something
is actively converting optimisation pressure into competence loss**, and 782 R-(b)
already measured a mechanism that predicts exactly this signature: the critic is **flat
and uninformed** — `std(V)/std(G) = 0.041` against a 0.25 collapse threshold, pre-reward
vs far separation 0.016 against a 0.25 floor. An uninformative baseline yields an
advantage carrying variance rather than signal, so *more gradient means more drift*,
whatever direction the drift is pushed from. And the corrective confirms it from the
other side: 788's distributional critic **retains** 1.839.

| field | value |
|---|---|
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `f_dominance_conversion_ceiling.baseline_informativeness` |
| `polarity` | `asserts` |
| `status` | `candidate` |
| `epistemic_category` | `standard` |
| `claim_level` | `mechanistic` |
| `implementation_phase` / `v3_pending` | `v3` / `true` |
| `depends_on` | MECH-457 (the pathway), MECH-459 (owns the *normaliser/critic-form* lever; this claim owns the *baseline-informativeness → iatrogenic-optimisation* consequence) |

**Claim (one line).** In REE's actor-critic pathway the value baseline is **uninformative
on the policy's own state distribution**, so the advantage carries variance rather than
signal and **added optimisation pressure is iatrogenic**: capacity, budget, earned
intrinsic drive, environmental coupling and post-install refinement each reduce
competence below their own controls, and the magnitude of the loss tracks baseline
uninformativeness rather than the identity of the intervention.

**`what_would_answer` (draft).**
> Two readouts, in decreasing order of decisiveness.
> **(a) REVERSAL.** Re-run the three destructive treatments (769 capacity/budget, 781
> approach drive, 771 metabolic coupling) **with the V3-EXQ-788 distributional critic in
> place**, everything else byte-identical. **SUPPORTED** if the treatment-below-control
> inversion reverses or flattens in ≥2 of 3. **WEAKENED** if treatments still land below
> their controls with an informative baseline — the destructiveness is then not the
> baseline's doing and this claim is withdrawn.
> **(b) DOSE.** Record `std(V)/std(G)` and the pre-reward-vs-far separation ratio as
> declared covariates on every arm of every future MECH-457-family run, and test whether
> the control→treatment competence *delta* is predicted by baseline informativeness
> across the existing five instances. **SUPPORTED** if the correlation holds and is
> signed as predicted.
> Mandatory: trajectory, not terminal — this signature is invisible to terminal-only
> measurement, which is what hid it for nineteen targets.

**Why this is not MECH-459 re-labelled.** MECH-459 asserts that the two-sided
**normaliser** makes the gradient scale-invariant, so magnitude levers *cannot move* the
floor — an **inertness** prediction. This claim asserts the **baseline** is uninformative,
so added optimisation *actively degrades* — a **destructiveness** prediction. They make
opposite predictions about the sign of the treatment effect and are independently
falsifiable: 769/781/771 are all magnitude-class levers that MECH-459 predicts should be
*inert*, and they were **destructive**. MECH-459's own probe (782 R-(a)) additionally
**weakened** its normaliser half (`C_pre` 1.92 / 1.20 above the 0.5 tiny threshold) while
**corroborating** the critic half — which is exactly this claim's half of that composite.

**Lit grounding.** The `targeted_review_actor_critic_action_learning` dossier already on
file supplies the frame: Sutton et al. 2000 (the value baseline is variance reduction —
an uninformative baseline reduces nothing) and O'Doherty et al. 2004 (a ventral-striatal
critic dissociable from the dorsal actor; a *silent* critic is a specific lesion, not a
degraded actor). Commission
`targeted_review_mech_457_baseline_informativeness` before registration — the biological
question is whether a mammalian actor with an uninformative critic degrades rather than
plateaus, for which the dopamine-depletion literature already on file
(`arc_068/salamone_correa_2003`; `cdq_007/szczypka2001` — dopamine-deficient mice with
intact perception, motor apparatus and hedonics **starve in front of food**) is the
entry point and is a strikingly close match to the observed signature.

---

### Child A-original — `return_optimum_misalignment` — **WITHDRAWN before proposal**

| field | value |
|---|---|
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `f_dominance_conversion_ceiling.return_objective_adequacy` |
| `polarity` | `asserts` |
| `status` | `candidate` |
| `epistemic_category` | `standard` |
| `claim_level` | `mechanistic` |
| `implementation_phase` / `v3_pending` | `v3` / `true` |
| `depends_on` | MECH-457 (the optimiser whose objective this names), MECH-459 (the normaliser that makes *magnitude* levers inert, which is why this claim specifies a structural term) |

**Claim (one line).** REE's D3 foraging deficit is a property of the **return**, not of
the learner: with an unbounded episode, a dominant survival/harm term and **no
opportunity-cost-of-time term**, the return-optimal policy is passive survival — so a
correctly-optimising learner lands *below its own random-walk anchor* on the foraging DV
while exceeding the oracle's survival, and the missing component is an
**average-reward-rate / cost-of-time** term rather than a larger consumption weight.

**Cluster evidence it explains.** #9 (769 avoidance-without-approach), #13 (781 approach
earned, consumption suppressed), #18 (all learners sub-random, PPO survival 175.0 vs
oracle 20.4 while foraging 17× less), and — from the other side — #19 + #16/#17 (the
policy class *can* represent competence, so this is not a capacity or representation
account). It also retro-explains #4–#7 and #10–#12 as a class: every one of those levers
changes *how* the learner searches or *how much* a term is worth, and none of them
changes *which policy is optimal*.

**`what_would_answer` (draft).**
> A **return-decomposition diagnostic**, learner held fixed. Record per-term return
> attribution (survival / harm / consumption / proximity / novelty) alongside
> `foraging_competence`, evaluated on a fixed reference set: `greedy_oracle`,
> `local_view_greedy`, `random_walk`, and the trained ON arm.
> **SUPPORTED** if the *competent* reference policies earn **lower total return** than
> the trained arm — i.e. competence is genuinely sub-optimal under the return as given.
> **WEAKENED** if the oracle's decomposed return already exceeds the trained arm's: the
> learner is then failing to find a return-optimal policy it could reach, and the
> policy-learning / observability route re-opens.
> Second arm (conditional on SUPPORTED): add an explicit per-step time cost /
> average-reward-rate baseline and re-measure D3 competence against the 13.05 lift
> target.

**WITHDRAWAL BASIS.** Its pre-registered falsifier V3-EXQ-771 was run in this session
(§4.0) and returned **outcome (b)**: on the metabolic env the return ranks competence
correctly and steeply (oracle 34.25, random 4.56) and the learners still floored, at
**0.90–1.12 return — a quarter of random walk — dying in 100% of episodes.** The
mechanism reading does not survive. **Not proposed for registration.** Recorded here in
full because (i) the withdrawal is the finding, and (ii) the *measurement-validity* half
of it — that `D3_hazard_free` does not rank its own scored DV — does survive and is
carried into §8 as a rider on the campaign's existing eliminations rather than as a
claim. The return-decomposition diagnostic the 2026-07-22 autopsy routed remains worth
running for that validity purpose; it is no longer a mechanism falsifier.

**Lit grounding.** Two entries already on file, and they do not simply agree:
- `targeted_review_arc_062_refuge_forage_ecology/2026-05-09_arc_062_risk_allocation_canonical_lima1999`
  — **Lima & Bednekoff 1999** risk-allocation. Load-bearing prediction (2): under
  **chronic** high risk, antipredator effort *drops*, because prey must feed sometime.
  This **corrects** the 2026-07-22 autopsy's biological-reference line, which read the
  observed long-survival / near-zero-intake policy as "what a real forager does under
  high perceived predation risk." Under *chronic* risk it is not. The behaviour is
  biologically **wrong**, which strengthens rather than weakens the mis-specification
  reading: what is absent is the state-dependent term that forces feeding.
- `targeted_review_arc_068_opportunity_cost/2026-05-10_arc_068_tonic_dopamine_opportunity_cost_niv_2007`
  — **Niv, Daw, Joel & Dayan 2007**, average-reward-rate as the opportunity cost of
  time, reported by tonic dopamine, setting response vigor. This is the named missing
  term. Sibling support: Guitart-Masip 2011 (human RTs track experienced reward rate).
  **Dissenting result, recorded, not buried:** Zénon 2016 finds levodopa alters the
  effort/reinforcement ratio rather than the opportunity cost — i.e. the *dopaminergic
  implementation* of the term is contested even where the *computational* term is not.
- Commission `targeted_review_mech_457_return_objective_adequacy` for the RL half
  (potential-based shaping invariance; reward mis-specification / objective-proxy
  divergence) before registration.

---

### Child B — `competence_retention_dissociable_from_acquisition` (working id **MECH-463**)

| field | value |
|---|---|
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `f_dominance_conversion_ceiling.acquisition_retention_dissociation` |
| `polarity` | `asserts` |
| `status` | `candidate` |
| `epistemic_category` | `standard` |
| `claim_level` | `mechanistic` |
| `implementation_phase` / `v3_pending` | `v3` / `true` |
| `depends_on` | MECH-457, MECH-459 (critic-side lever), MECH-460 (prior-side lever) |

**Claim (one line).** **Acquiring** competence and **retaining** it are dissociable
capabilities requiring separate substrate: REE has the first and lacks the second, and
retention is supplied by properties of the **value estimator** and the **update
constraint** — not by continued demonstration — with consolidation properly defined as
**resistance to retrograde interference**, hence dependent on install *dose* and elapsed
*time*, neither of which REE has ever varied.

**Cluster evidence it explains.** #19 (install 20.933 → erode 11.667, 3/3 seeds took),
#17 (789: the auxiliary *succeeded then decayed* at every schedule — the demonstration
axis eliminated), #16 (788: a distributional critic retains 1.839), #15 (782 R-(b): the
shared control critic is flat and uninformed, std(V)/std(G) = 0.041 — the measured
mechanism of the erosion), plus 792's load-bearing PASS (KL anchor 0.778 / 0.871 vs
0.525 unconstrained, *and still plastic*).

**Anti-duplication — what this asserts that MECH-459 and MECH-460 do not.**
This is the part to scrutinise hardest, because both siblings are close:
- MECH-459 owns the **critic/normaliser lever**; MECH-460 owns the **behavioural-prior
  lever** (and already names KL-to-a-frozen-own-snapshot as the literature's
  anti-forgetting object). Neither asserts that acquisition and retention are
  **dissociable capabilities**; each is a claim about one lever.
- The distinctive content is therefore (i) the **double dissociation** itself — a
  mechanism can retain without acquiring (the KL anchor acquires nothing) and acquire
  without retaining (BC); (ii) **consolidation-as-interference-resistance**, which makes
  **install dose** and **elapsed offline time** the untested levers — V3-EXQ-780 ran a
  single BC dose straight into RL with no offline interval, so REE has never tested for
  a consolidation *process* at all, only for concurrent *regularisation*; (iii)
  **trace selectivity** — 792's own §3 records that a global KL coefficient cannot
  express *which* traces are protected, whereas the biology's protection is
  trace-specific.
- **If the falsifier below returns invariance, this child collapses back into
  MECH-459/460 and should be withdrawn rather than kept as an umbrella.** That is the
  intended failure mode and it is what keeps this from being a third lever claim.

**`what_would_answer` (draft).**
> An **A → B → A retrograde-interference design**, the standard consolidation assay.
> A = BC-install competence; B = an interfering unconstrained-RL phase; then re-measure
> A. Vary **two** factors REE has never varied: **install dose** (BC episodes) and
> **A→B interval** (offline steps before refinement begins). DV: retained fraction
> *trajectory*, never terminal competence.
> **SUPPORTED** if resistance to interference grows with install dose and/or with the
> A→B interval — retention is then a dose/time-dependent consolidation *process*.
> **WEAKENED** if retained fraction is invariant to both and tracks only the concurrent
> constraint coefficient — there is then no consolidation process, only a regulariser,
> and this child is withdrawn into MECH-459/460.
> Prerequisite (inherited from the retention portfolio, non-negotiable): an install that
> did not take is uninformative about retention and must self-route
> `substrate_not_ready_requeue`, never a retention verdict.

**Lit grounding.**
- **Krakauer et al. 2005** (J Neurosci), *Adaptation to visuomotor transformations:
  consolidation, interference, and forgetting* — consolidation **defined** as resistance
  to retrograde interference, and shown to emerge both with elapsed time and with
  **doubled initial training**. This is the direct source of the design above.
- **Walker et al. 2003** (Nature), *Dissociable stages of human memory consolidation and
  reconsolidation* — at least three separable post-acquisition stages; reactivation
  returns a consolidated memory to a labile state (the direct analog of RL refinement
  destroying an installed policy).
- On file: `targeted_review_systems_consolidation_waking_propagation` (Frankland &
  Bonhoeffer 2005 systems consolidation; Carr 2011 awake replay; Tambini 2019).
- Commission `targeted_review_mech_457_consolidation` on **trace-selective vs global**
  consolidation (Frey & Morris tagging-and-capture as the entry point). The 792 autopsy
  already recommended this as *secondary*; this child makes it **primary** and it must
  land **before** registration, per Step 5.

---

## 5. Children explicitly DECLINED

Recording the refusals, because on this skill the refusals are most of the value.

| Candidate | Why declined |
|---|---|
| **z_world installability** (BC installs 3/3 on raw_view at 20.933, **0/3** on z_world at 0.583) | The user's own caution is correct and decisive: the z_world half is confounded by the untrained-encoder defect. `encoder_moved_in_p0` was false across 734, 742a-frozen and the 737 REE-latent arms; `sd_zworld_warmup_optimizer_group` is `implemented_pending_validation` with **per-copy incomplete adoption**. Registering a claim here would manufacture a mechanism from an implementation fault — the exact Step-3 failure mode. **Route: `/implement-substrate` amend (collapse the duplicated `_train_all_on_agent` copies onto the single SD-070 path), then re-test whether 0/3 reproduces.** Revisit only if it does. |
| **Consummatory binding** (781: approach earned at 0.70 while foraging suppressed 2.983 → 0.200) | Already owned three ways: the 780/781/782 autopsy routed it to the standing basal-ganglia-commitment reading and *deliberately registered no new leg for it*; MECH-461 owns the innate-primitive + engagement-drive half; `H-consummation-binding` is a live registry leg (`substrate_blocked` on `mech457_consummatory_act`). It is **corroborating evidence for Child A**, not a claim — approach-without-consummation is what an objective with no consumption optimum looks like from the drive side. |
| **Policy-learning capacity** | `H-policy-learning` stays `alive` by explicit user adjudication (2026-07-22); a null produced under a mis-specified objective does not discriminate it. Not claim-level, and pre-empting it here would be the "confident-but-wrong verdict on a laundered artifact" GOV-FANOUT-1 exists to prevent. |
| **A fourth "objective vs learner" umbrella** | Would duplicate Child A at a coarser grain. Declined. |

---

## 6. If approved — registration checklist (Step 7)

1. Re-read the `claims.yaml` insertion region immediately before editing (concurrency);
   allocate ids from the live max **and** recent `git log`.
2. Register approved children as `candidate` with `what_would_answer`, `depends_on`,
   and an architecture-doc stub under
   `docs/architecture/competence_bootstrap_mechanisms.md` (where MECH-459/460/461 live).
3. Amend MECH-457: sufficiency disclaimer, reverse-dep wiring, and — **mandatory** —
   update `granularity_debt_disposition` away from `coherent_campaign` with a note
   pointing at this document (§0).
4. `python scripts/build_claims_json.py`; confirm the children appear and the stance
   tally moved.
5. `scripts/ree_commit.py` over `docs/claims/claims.yaml`,
   `docs/assets/data/claims.json`, this file; verify the per-item delta; push `HEAD:master`.
6. Frozen-ledger: the two children do **not** add hypothesis legs. Child A's leg
   (`H-objective-misspecification`, axis `reward`) is already being pre-registered on
   `qid conversion_ceiling_root` by the 2026-07-22 cluster autopsy §7; Child B's legs
   (`H-retention-critic`, `H-retention-consolidation`) already exist on
   `qid competence_floor`. **No fan-out growth event is created by this synthesis** —
   which is the point: this is the GOV-FROZEN-1 re-pose, not portfolio 4.

## 7. Hand-off (post-approval, not this session)

- **Child A's blocking check is DONE** — the 771 reconciliation was run in this session
  (§4.0) and redirected the child. No further gating check is owed before its lit-pull.
- `/lit-pull` × 2, **before** registration:
  `targeted_review_mech_457_baseline_informativeness` (Child A, revised),
  `targeted_review_mech_457_consolidation` (Child B).
- `/queue-experiment`: the **reversal** design (Child A — 769/781/771 treatments re-run
  with the 788 distributional critic) and the **A→B→A interference** design (Child B);
  plus 792a (re-power, measured control drift, ≥6 seeds) and 734a (SD-070 path, guard
  green-gating), both already routed by their own autopsies.
- `/implement-substrate`: amend `sd_zworld_warmup_optimizer_group` — collapse the
  duplicated `_train_all_on_agent` copies.

---

## 8. Open decisions for the user (this document decides none of them)

1. **Approve / edit / reject Child A (revised)** — `uninformative_baseline_makes_optimisation_iatrogenic`.
2. **Approve / edit / reject Child B** — `competence_retention_dissociable_from_acquisition`.
3. **The `D3_hazard_free` validity rider.** §4.0 establishes that on `D3_hazard_free`
   the return does not rank the scored DV (`random_walk` mean_episode_reward −1.006;
   oracle survives 20.4 vs PPO 175). Nine campaign eliminations were measured there.
   Options: (a) record the rider on MECH-457's `evidence_quality_note` and leave the
   eliminations standing; (b) additionally annotate the affected legs' `basis` in
   `hypothesis_space_registry.v1.json` as measured-on-a-non-ranking-yardstick; (c) treat
   it as grounds to re-open specific eliminations. **Recommend (a)+(b)** — the legs stay
   eliminated, but a reader can see what they were measured against. **(c) should not be
   done wholesale:** 771 shows that fixing the objective does not lift the floor, so
   re-running those legs on a ranking yardstick would likely reproduce the same nulls at
   full cost.
4. **The 2026-07-22 adjudication.** It selected objective mis-specification for the
   734/737b/742a cluster, and that selection stands **for `D3_hazard_free`**. §4.0 shows
   it does not generalise into a mechanism claim. Confirm that narrowing, or overrule it.
5. **`granularity_debt_disposition`.** If any child is approved, this field must move off
   `coherent_campaign` in the same pass (§0).
