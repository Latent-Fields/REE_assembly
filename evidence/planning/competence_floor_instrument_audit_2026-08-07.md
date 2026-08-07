# competence_floor — measurement-instrument audit

**Date:** 2026-08-07T20:13:58Z
**Question:** `competence_floor` (`evidence/planning/hypothesis_space_registry.v1.json`)
**Claims:** MECH-457, INV-088
**Trigger:** 2026-08-07 `/governance` GOV-FROZEN-1 anti-Goodhart audit — fan-out recurrence
(5 labelled fan-out portfolios, denominator 7 -> 20 hypotheses, 0 legs currently alive).
**Type:** instrument audit. **Not** hypothesis #21 — this questions the measurement frame,
not the mechanism space. **Zero new compute**: every number below is re-derived from
`arm_results[]` already committed in `evidence/experiments/<run_id>.json`.

---

## 0. Headline answers to the two questions this audit was asked

**Q1 — is the confirmed retention effect concentrated in one sub-skill or uniform across
all three?** **CONCENTRATED**, and not in the sub-skill the claim names. Both confirmed
retention mechanisms move *episode duration* far more than they move *foraging skill per
unit time*. On `H-retention-critic` the composite DV reports a **3.28x** effect; the
foraging **rate** effect is **1.42x** and the survival-duration effect is **2.41x** — the
composite is their product, so ~70% of the log-effect is duration, ~30% is rate.
`H-retention-consolidation` (kl0p30) is the same shape: composite 1.73x = rate 1.22x x
duration 1.43x. At the weakest anchor dose (kl0p03) the split is 12% rate / 86% duration;
at kl0p10 the foraging **rate falls** (0.97x) while the composite still rises (1.17x).
Direction of both confirmations survives; **effect size shrinks roughly 2x** and the
mechanistic reading changes from "protects foraging skill" to "keeps the agent alive
longer, and per-episode forage count follows".

**Q2 — does the z_world audit change how many of the 20 legs read as "eliminated" vs
"eliminated but confound-contaminated, re-test owed"?** **Fewer legs than feared, but one
finding is not merely contaminated — it is exactly the artifact.** The frozen-random-
projection defect is confined to the six Round-3 runs built with `cotrain_encoder=False`
and no `zworld_p0` warmup (V3-EXQ-770/771/772/780/781/782 — five registered legs plus the
MECH-459 probe). In every one of those legs the conclusion is independently carried by an
*uncontaminated* `raw_view` half, so the eliminations stand. The exception is
**`H-bc-prior` child 3** ("the imitation pathway does not install at all
on the detached z_world representation", currently `open_unowned`): its entire evidential
basis is one contaminated arm, and V3-EXQ-819a is direct counter-evidence. That child
should be **voided, not left open**. **The five retention legs are z_world-free and
completely uncontaminated** — the two confirmations are untouched by this defect.

**A third finding the audit was not asked for, and which is the more consequential one:**
the load-bearing observation that *spawned* an entire fan-out leg —
`H-approach-primitive`'s "approach-without-consummation" — is **contradicted by an
env-observable directed-approach statistic collected in the same run and discarded**. See
section 4. That is a concrete mechanism for the fan-out recurrence GOV-FROZEN-1 flagged.

---

## 1. What was actually measurable, and what the instrument threw away

### 1a. The sub-skill instrument already exists and already ran

`ree-v3/experiments/_lib/capability_eval.py::evaluate_seed` returns **eight** metrics per
(arm, seed) cell, not one. Three of them map onto the decomposition this audit was asked
for:

| requested sub-skill | existing metric | definition |
|---|---|---|
| approach-attempt rate | `planning_depth` | mean over episodes of the longest run of strictly-decreasing Manhattan distance to the nearest resource (`capability_eval.py:96`) |
| consumption-given-approach | `goal_reach_rate` (+ `foraging_competence`) | fraction of episodes collecting >= 1 resource; resources/episode |
| hazard-avoidance | `mean_hazard_hits`, `death_rate`, `survival_horizon` | `transition_type == "env_caused_hazard"` count; fraction of episodes ending health<=0; ticks survived |

All eight are present in the **flat** committed manifest
`evidence/experiments/<run_id>.json` under `arm_results[]`. (They are **absent** from the
stripped `runs/<run_id>/manifest.json` copy, and `metrics.json` is an empty stub in every
one of these runs — so the decomposition is invisible to anyone reading the run pack.)

### 1b. Where the trajectory instrument narrows to one number

`experiments/_lib/baselines/mech457_retention.py::make_probe_fn` (lines 277-283) runs the
full eight-metric `evaluate_seed` at every mid-training probe and then returns exactly one
key:

```python
def _probe(ep: int) -> Dict[str, Any]:
    probe_env = x734._make_env(seed, env_kwargs)
    row = evaluate_seed(...)                                   # 8 metrics computed
    return {"foraging_competence": round(float(row["foraging_competence"]), 6)}
```

`install_bc_prior` (lines 253-256) does the same at the post-BC install measurement.

Cost of that one-line projection, across the five retention runs:

| run | probe readings | episodes evaluated | metrics kept / computed |
|---|---|---|---|
| V3-EXQ-788 | 72 | 1,440 | 1 / 8 |
| V3-EXQ-789 | 108 | 2,160 | 1 / 8 |
| V3-EXQ-792 | 144 | 2,880 | 1 / 8 |
| V3-EXQ-792a | 288 | 5,760 | 1 / 8 |
| V3-EXQ-821 | 72 | 1,440 | 1 / 8 |
| **total** | **684** | **13,680** | **1 / 8** |

So the answer to "can the trajectories be re-scored into three curves?" is **partly**:

- **Terminal (end-of-refinement) decomposition: YES, fully recoverable** — that is section 3.
- **Trajectory (per-probe) decomposition: NO** — the data was computed and discarded, not
  merely un-analysed. Recovering it needs a re-run, but the fix is one line plus manifest
  plumbing, so a re-run is cheap and the instrument is not the blocker.

The `measurement_requirement` block on all four retention legs says, in capitals,
"records the post-installation competence TRAJECTORY, not terminal competence —
terminal-only measurement is precisely what kept this deficit invisible for ten legs".
That requirement was honoured for the *composite* and silently dropped for every
sub-skill. The same class of defect, one level down.

### 1c. The hazard-avoidance curve is unmeasurable on D3 by construction

`mean_hazard_hits == 0.000` in **every arm of every run audited**, including
`greedy_oracle`. That is not a null result — `D3_hazard_free` sets `num_hazards=0`,
`proximity_harm_scale=0.0`, `reef_enabled=False`
(`v3_exq_734_env_difficulty_competence_recovery_sweep.py:311-314`), so the channel cannot
fire. **The third requested curve does not exist on this rung.** Everything that looks
like "hazard avoidance" in this campaign is `death_rate` / `survival_horizon`, i.e.
starvation, which is *coupled to* foraging rather than independent of it (section 2).

A fourth channel is live and unexamined: `mean_contaminations` tracks `survival_horizon`
almost 1:1 in the competent arms (`local_view_greedy` 154.15 vs 154.2 ticks; `greedy_oracle`
188.55 vs 188.6) and sits at ~4-15 in the non-foraging arms. The competent policy registers
a contamination event on essentially every tick. Flagged, not diagnosed here.

---

## 2. The composite DV confounds foraging rate with episode length — and the two are
   anti-correlated at the floor

`foraging_competence` is **resources per EPISODE**, and episode length varies ~13x across
arms (15.0 to 200.0 ticks). Two regimes are visible in the raw cells:

- **forage-and-die** — high forage, contamination on nearly every tick, `death_rate`
  0.6-1.0, survival 57-170. `local_view_greedy` lives here (`death_rate` **0.650**).
- **camp-and-live** — forage ~0.15-0.60, contamination 4-15, `death_rate` **0.000**,
  survival pinned at the **200-tick step cap**.

So in D3 the *most survivable* policy is the *least competent* one, and `survival_horizon`
is **bimodal, not a monotone sub-skill**. This is the same pathology the
`D3_MEASUREMENT_VALIDITY` rider records for six earlier legs ("survival — maximised by NOT
foraging — dominates return"), showing up in the behavioural DVs rather than the return.

Within the *forage-and-die* regime, however, survival is genuinely **downstream** of
foraging (eating restores health), so a per-episode count **double-counts**: better
foraging -> longer episode -> more forage per episode. Reporting the per-tick rate
alongside removes the double-count. Both readings are given below.

---

## 3. Sub-skill decomposition (terminal eval, all arms, all five runs)

Derived from `arm_results[]`; `rate/tick` = `foraging_competence / survival_horizon`.

```
run    arm                        n  forage/ep   plan   goal    surv  death   haz  rate/tick  ret_frac
780    local_view_greedy          3     48.050  6.883  0.983   163.8  0.650  0.000    0.2934        -
780    greedy_oracle              3     57.200  7.667  1.000   191.5  0.317  0.000    0.2988        -
780    random_walk                3      0.933  2.567  0.550    46.0  1.000  0.000    0.0203        -
780    bcprior_ctrl_raw           3      7.217  3.517  0.700   120.0  0.583  0.000    0.0590        -
780    bcprior_treat_raw          3     11.667  4.933  0.950    57.9  0.983  0.000    0.1925        -
780    bcprior_ctrl_zworld        3      0.650  2.333  0.367    83.6  0.667  0.000    0.0066        -
780    bcprior_treat_zworld       3      1.950  3.033  0.783    92.2  0.683  0.000    0.0245        -
788    retcritic_scalar           3     11.667  4.933  0.950    57.9  0.983  0.000    0.1925    0.525
788    retcritic_distributional   3     38.300  6.817  0.967   139.4  0.833  0.000    0.2732    1.839
789    retaux_constant            3      4.600  3.833  0.767    88.8  0.717  0.000    0.0859    0.191
789    retaux_annealed            3     10.083  4.350  0.633   126.1  0.600  0.000    0.0963    0.408
789    retaux_off                 3      0.917  2.533  0.500   175.8  0.133  0.000    0.0061    0.046
792a   retcons_unconstrained      6     11.775  4.842  0.958    59.5  0.983  0.000    0.1903    0.509
792a   retcons_kl0p03             6     17.225  5.200  0.975    82.7  0.925  0.000    0.1995    0.814
792a   retcons_kl0p10             6     13.792  4.792  0.858    63.3  0.950  0.000    0.1845    0.580
792a   retcons_kl0p30             6     20.350  5.558  0.933    85.2  0.892  0.000    0.2317    0.895
821    local_view_greedy          3     34.167  7.750  1.000   150.5  0.767  0.000    0.2271        -
821    consumbind_extinct_off     3      0.000  2.500  0.000    17.8  0.983  0.000    0.0000    0.000
821    consumbind_extinct_on      3      0.000  2.583  0.000    15.0  1.000  0.000    0.0000    0.000
```

### 3a. `H-retention-critic` (CONFIRMED) — concentrated in duration

| metric | scalar | distributional | ratio |
|---|---|---|---|
| forage / episode (**the DV**) | 11.667 | 38.300 | **3.28x** |
| forage / tick | 0.1925 | 0.2732 | **1.42x** |
| survival_horizon | 57.87 | 139.40 | **2.41x** |
| planning_depth | 4.933 | 6.817 | 1.38x |
| goal_reach_rate | 0.950 | 0.967 | **1.02x (both at ceiling)** |

Log-effect share: **~29% foraging rate, ~74% survival duration** (shares are approximate —
composite = rate x duration holds per-episode, not exactly on means).

Two things follow. (i) `goal_reach_rate` is saturated in **both** arms: the scalar-critic
agent still finds and eats something in 95% of episodes. The distributional critic does
not restore *whether* the agent consumes — it changes *how long it keeps doing so*.
(ii) `planning_depth` (1.38x) tracks the per-tick rate (1.42x) closely, so the
approach-quality improvement is real but modest and consistent.

### 3b. `H-retention-consolidation` (CONFIRMED) — same shape, and the caveat survives

| arm vs unconstrained | forage/ep | forage/tick | survival | plan | goal |
|---|---|---|---|---|---|
| kl0p03 | 1.46x | **1.05x** | 1.39x | 1.07x | 1.02x |
| kl0p10 | 1.17x | **0.97x** | 1.06x | 0.99x | **0.90x** |
| kl0p30 | 1.73x | **1.22x** | 1.43x | 1.15x | 0.97x |

The registry's non-monotone-dose caveat **survives the decomposition and sharpens**: under
the per-tick DV, kl0p10 is the only arm *below* its control on foraging rate (0.969x) and
it also loses 10% of `goal_reach_rate`, yet its composite still reads as a 1.17x gain —
purely from surviving 1.06x longer. The strong anchor is the only dose that improves
foraging rate at all.

### 3c. `H-retention-auxiliary-decay` (ELIMINATED) — the `off` arm is a passive-survival
     policy, and this leg is owed the D3 rider

`retaux_off`: forage **0.917** (at the random-walk floor), survival **175.8**, `death_rate`
**0.133** — lower than `greedy_oracle`'s 0.317 and far below `local_view_greedy`'s 0.650.
Two of its three seeds sit exactly at the 200-tick cap with zero deaths.

The composite scores this as `retained_fraction 0.046`, i.e. **maximal erosion**. The
decomposition says it is not erosion into incompetence — it is a **strategy switch into
camp-and-live**. The elimination ("no schedule of the imitation auxiliary rescues
foraging retention") **stands**; its mechanistic label does not. "The auxiliary is
out-competed by the RL objective" is now specific: out-competed *toward passive survival*,
which is reward-coupling, not auxiliary decay.

**Concretely owed:** the `D3_MEASUREMENT_VALIDITY` rider was applied to H-credit, H-return,
H-curric, H-arbitr, H1-drive-schedule and H3-credit-horizon. It was **not** applied to
`H-retention-auxiliary-decay` — whose own data exhibits the pathology more clearly than any
leg that carries it. Proposed text in section 6.

### 3d. `H-consummation-binding` (ELIMINATED) — a degenerate comparison, not a
     discriminating null

Both arms: `foraging_competence` **exactly 0.000** on all 6 cells, `goal_reach_rate`
**0.000**, `planning_depth` 2.50/2.58, survival **17.8 / 15.0** — *below* `random_walk`'s
34.0 in the same env. Trajectory peaks are 0.4/0.0/0.0 and 0.85/0.0/0.0: neither arm
re-cleared the 1.0 floor at any of 12 readings, on any seed. The install was also ~3x
weaker in relative terms than the rest of the portfolio (post-BC 4.77 against a 34.17
`local_view_greedy` ceiling = 14% of ceiling, vs 20.93/48.05 = 44% elsewhere).

The manifest's `non_degenerate: true` is computed on the **anchors** clearing the floor,
not on the treatment cells being non-degenerate. Two arms tied at the absolute floor on
every sub-skill do not discriminate anything. The registry basis is honest about the
peaks; the `state: eliminated` + `met_elimination_bar: true` is not warranted by this
comparison. **Recommend downgrading to `alive` with an observation-bottleneck note, or
re-running at a stronger install.**

### 3e. `H-bc-prior` raw_view (SPLIT) — the composite *understates* the BC effect

| metric | ctrl_raw | treat_raw | ratio |
|---|---|---|---|
| forage / episode | 7.217 | 11.667 | 1.62x |
| forage / tick | 0.0590 | 0.1925 | **3.26x** |
| survival_horizon | 120.0 | 57.9 | **0.48x** |
| goal_reach_rate | 0.700 | 0.950 | 1.36x |
| planning_depth | 3.517 | 4.933 | 1.40x |

Here the confound runs the **other way**: the BC-primed agent trades survival for foraging
(it is in forage-and-die; its control is half in camp-and-live — control seeds are
0.300 / 0.550 / **8.100**, one seed carrying the mean). On a rate DV the behavioural-prior
effect is **twice as large** as the headline number. The `confirmed` child ("a
competence-directed behavioural prior CAN produce supra-lift-target competence on
raw_view") is strengthened, not weakened.

---

## 4. The fan-out-recurrence mechanism: one leg was spawned off a misread instrument

`H-approach-primitive`'s resolution carries a **LOAD-BEARING POSITIVE FINDING**: "in
raw_view the drive SUPPRESSED foraging (0.200 vs a 2.983 ctrl ...) while approach reward
was continuously earned — approach-without-consummation, the appetitive drive becoming
terminal rather than instrumental." That observation is what motivated
`H-consummation-binding`, which cost V3-EXQ-821 and came back fully degenerate (3d).

V3-EXQ-781 collected the env-observable directed-approach statistic in the same run:

| metric | approach_ctrl_raw | approach_treat_raw |
|---|---|---|
| planning_depth (**directed approach**) | 3.350 | **1.417 (0.42x)** |
| goal_reach_rate | 0.517 | 0.167 |
| survival_horizon | 169.6 | **200.0 (cap, 3/3 seeds)** |
| death_rate | 0.350 | **0.000** |
| mean_contaminations | 44.4 | **4.6** |

The treated agent's **directed approach fell by more than half** while proximity reward was
being earned at 0.698-0.707, it never died, and it barely moved (contamination 4.05-5.55
over 200 ticks). That is not an appetitive drive becoming terminal — it is
**proximity-camping**: parking near a resource, where a static agent collects the shaping
term continuously without executing an approach at all. A Goodhart of the shaping term,
not a consummation deficit.

This is checkable from data already committed, and it inverts the mechanistic reading that
seeded a fan-out leg. **The fan-out recurrence GOV-FROZEN-1 flagged has at least one
concrete cause: rivals are being enumerated from a composite DV's residue while the
env-observable statistic that would have discriminated them sits unread in the same
manifest.**

(One accuracy note: `treat < ctrl` holds on 3/3 seeds, so the elimination direction is
sound. The stated 0.067x magnitude is carried by a single control seed — the control is
0.300 / 0.550 / 8.100, not "tight".)

---

## 5. z_world contamination audit (part 2)

### 5a. The defect

`experiments/_lib/mech457_fanout.py` (untrained-encoder guard, lines 411-431): the P0 loop
buffers `latent.z_world.detach()`, so the gradient path terminates before the world
encoder and **0 of 61 latent_stack tensors change** (`max|delta| = 0.000e+00`, bit-identical).
`z_world` on that path is a frozen **random projection at initialisation**, never a
prediction-trained encoder. Discovered via V3-EXQ-780's BC install failure (diagnosed
2026-07-19), validated as an instrument by V3-EXQ-819/819a (2026-07-26/27).

### 5b. Contamination is determined by `cotrain_encoder`, not by "has a z_world arm"

The 819a autopsy already established the discriminator: an arm built with
`cotrain_encoder=True` routes gradient to the encoder from the actor-critic loss and is
**structurally distinct** from the detached-warmup defect. Extracting `cotrain_encoder`
from each committed manifest's `config` gives a clean generational split:

| round | runs | `cotrain_encoder` | `zworld_p0` | z_world arms | status |
|---|---|---|---|---|---|
| R1-R2 | 748, 751, 752, 753, 754, 755 | **True** | 0 | yes (`ac_zworld_*`, `*_zw`) | **not contaminated by this mechanism** (encoder trains from the AC loss; starts at random init) |
| R3 | 770, 771, 772, 780, 781, 782 | **False** | absent (=0) | yes | **CONTAMINATED — frozen random projection throughout** |
| retention | 788, 789, 792, 792a, 821 | n/a | n/a | **none** (`REF_REPRESENTATION = "raw_view"`) | **uncontaminated — no z_world arm exists** |
| MECH-475/476 | 836, 836a, 836c, 836d, 837 | n/a | n/a | none | uncontaminated |
| fixed instrument | 748a, 819, 819a | False | **60** | yes | the validated instrument |

(747 and 749 are `raw_view`-only. 765 reuses 751's `ac_zworld_rnd` cell verbatim — the
same three values 4.700/4.750/6.200.)

### 5c. Leg-by-leg verdict

| leg | state | z_world exposure | verdict |
|---|---|---|---|
| H-rep | eliminated | none in 747/749; control 748 is cotrain; re-run as 748a under `zworld_p0=60` | **stands** (already re-derived) |
| H-explore | split | 748, cotrain | **stands**; 748a re-ran it under the trained instrument |
| H-optim | confirmed | 751, cotrain, **z_world-only** | **stands** on the 819a criterion, but see 5d |
| H-credit / H-return / H-curric / H-arbitr | eliminated | 752-755, cotrain, both reps | **stand** |
| H1-drive-schedule | eliminated | 770, **detached** | z_world half contaminated; conclusion carried by the uncontaminated `raw` half ("floors on BOTH reps") — **stands, rider owed** |
| H2-reward-coupling | eliminated | 771, **detached** | same — **stands, rider owed** |
| H3-credit-horizon | eliminated | 772, **detached** | same — **stands, rider owed** |
| H-approach-primitive | eliminated | 781, **detached** | z_world half contaminated (and null either way: 0.300 vs 0.317); the load-bearing finding is on `raw` — **stands, rider owed** (but see section 4 for a separate problem with that finding) |
| **H-bc-prior child 3** | **open_unowned** | 780, **detached**, z_world-only | **VOID — see 5e** |
| H-bc-prior children 1-2 | confirmed / open_routed | raw_view | **stand** |
| H-retention-critic / -consolidation / -auxiliary-decay | confirmed / confirmed / eliminated | **none** | **untouched by this defect** |
| H-consummation-binding | eliminated | none | untouched here (but see 3d) |
| H-zworld-trained-instrument | confirmed | the fix itself | n/a |
| H-mech475-*, H-mech476-* | eliminated | none | untouched |

**Count: 0 of 20 legs need re-opening on z_world grounds.** Five registered legs ran a
contaminated z_world arm (H1-drive-schedule, H2-reward-coupling, H3-credit-horizon,
H-approach-primitive, H-bc-prior); in all five the conclusion is independently carried by
an uncontaminated raw_view half. **Four of them are owed a rider with no state change**
(section 6(ii)); the fifth's contamination is isolated to **`H-bc-prior` child 3, which is
void** (section 5e). The two CONFIRMED retention mechanisms have no z_world exposure at all.

### 5d. Caveat on the reference bands, which are cited campaign-wide

The **RND 5.22 plateau** — cited as a pre-registered reference band in essentially every
leg's `desc` — is `mean(4.700, 4.750, 6.200) = 5.217` from V3-EXQ-751's `ac_zworld_rnd`
arm: a **z_world arm** whose encoder began as a random projection and was shaped only by
the actor-critic loss (`cotrain_encoder=True`). By the 819a criterion this is not
*contaminated*, but it is also not a prediction-trained-representation number, and it is
the only band in the set that is z_world-derived (`local_view_greedy` 48.05, `greedy_oracle`
57.2, `random_walk` 0.933 and BC-expert 32.72 are all representation-independent or
raw_view). Worth stating wherever the band is cited rather than leaving it implicit.

### 5e. `H-bc-prior` child 3 is void, not open

Child 3 currently reads: *"and the imitation pathway does not INSTALL AT ALL on the
detached z_world representation"* — `state: open_unowned`, basis "V3-EXQ-780 z_world:
post_bc 0.583, 0/3 seeds took". Three facts:

1. That measurement is **the single purest instance of the defect**: `cotrain_encoder=False`,
   no `zworld_p0`, z_world-only, pre-fix. The BC gradient could not reach the encoder, so a
   0/3 install is what the *instrument* guarantees, not what the *pathway* shows.
2. **V3-EXQ-819a is direct counter-evidence**: with `zworld_p0=60`, the trained z_world
   arm beats the frozen random projection by mean paired AUC delta **+0.626** against a 0.3
   margin, 4/6 seeds clear, `n_seeds_harm=0`. `H-zworld-trained-instrument` is CONFIRMED on
   exactly this contrast.
3. Even within 780's own contaminated data, the z_world treatment beats its own control on
   **every** sub-skill — forage 3.00x, rate/tick 3.72x, `goal_reach_rate` 2.14x
   (0.367 -> 0.783), `planning_depth` 1.30x — and terminal forage (1.950) **exceeds** the
   post-BC install (0.583), i.e. competence *grew* under RL rather than eroding. The child's
   own framing ("never installed, arm uninformative") is not what the arm's sub-skill
   profile shows.

Child 3 is a live, unowned explanandum in the frozen ledger, i.e. a standing invitation to
spawn hypothesis #21 against an artifact. **It should be voided with the reason recorded,
not left open.** This is the single highest-value registry edit this audit recommends.

---

## 6. Registry disposition — proposed, NOT applied

**Nothing in `hypothesis_space_registry.v1.json` was written by this session.** Reasons,
stated so governance can override cheaply:

- The registry's schema has **no free-form audit-note slot** on a question. The closest
  precedent is the per-leg `resolution.d3_measurement_validity_rider`, which was added by
  `/claim-synthesis` MECH-457 (2026-07-22) under an explicit **user-approved option (b)**,
  promoting/demoting nothing. This audit is the same shape and should get the same
  authorisation.
- `/failure-autopsy` Step 9b is the registry's single producer, and its three modes
  (pre-register / resolve / discover) are all about *hypotheses*. An instrument rider is
  none of those.
- Two of the proposals below are **state changes** (5e void, 3d downgrade), which are
  governance's call under Step 2b, not a chip's.

Proposed edits, copy-paste ready:

**(i) `H-bc-prior` child 3 — void.** Set `children[2].state` to `"void_instrument_artifact"`
(or `"eliminated"` with `evidence_direction: "non_contributory"`), `routed_to: []`, and
append to its `basis`:

> VOIDED 2026-08-07 (competence_floor_instrument_audit_2026-08-07.md section 5e). This
> child's entire basis (V3-EXQ-780 z_world: post_bc 0.583, 0/3 install) was measured on the
> detached frozen-random-projection z_world instrument (`cotrain_encoder=False`,
> `zworld_p0` absent) that V3-EXQ-780 itself proved was never trained -- 0 of 61
> latent_stack tensors change, `max|delta| = 0.000e+00`. A 0/3 BC install is what that
> instrument guarantees, not what the imitation pathway shows. V3-EXQ-819a is direct
> counter-evidence (trained vs random-projection z_world, mean paired AUC delta +0.626 vs a
> 0.3 margin, 4/6 seeds, n_seeds_harm=0), and within 780's own data the z_world treatment
> beats its own control on every sub-skill (forage 3.00x, rate/tick 3.72x, goal_reach_rate
> 0.367->0.783, planning_depth 1.30x) with terminal forage 1.950 ABOVE the 0.583 install.
> Not an open explanandum; an instrument artifact. Any genuine installability-on-z_world
> question must be re-posed against the `zworld_p0`-trained instrument.

**(ii) Per-leg `instrument_validity_rider` on H1-drive-schedule, H2-reward-coupling,
H3-credit-horizon, H-approach-primitive** (state unchanged, `met_elimination_bar` unchanged):

> INSTRUMENT_VALIDITY RIDER (added 2026-08-07,
> competence_floor_instrument_audit_2026-08-07.md section 5c; PROMOTES/DEMOTES NOTHING and
> this leg STAYS eliminated). This leg's z_world arm ran on the detached
> frozen-random-projection encoder (`cotrain_encoder=False`, no `zworld_p0` warmup) that
> V3-EXQ-780 proved never trains, so its z_world half is uninterpretable as evidence about
> z_world. The elimination stands because it is independently carried by the raw_view half,
> which is uncontaminated. Do not cite the z_world arm of this leg as evidence in either
> direction.

**(iii) `H-retention-auxiliary-decay` — the D3 rider is owed here too:**

> D3_MEASUREMENT_VALIDITY RIDER (added 2026-08-07,
> competence_floor_instrument_audit_2026-08-07.md section 3c; PROMOTES/DEMOTES NOTHING and
> this leg STAYS eliminated). The `retaux_off` arm scored `retained_fraction` 0.046 --
> maximal erosion -- while achieving `survival_horizon` 175.8 and `death_rate` 0.133, i.e.
> LOWER mortality than `greedy_oracle` (0.317) and `local_view_greedy` (0.650), with 2 of 3
> seeds at the 200-tick cap and zero deaths. That is not erosion into incompetence; it is a
> strategy switch into passive survival, the same non-ranking-instrument pathology this
> rider records for H-credit / H-return / H-curric / H-arbitr / H1 / H3. The elimination
> stands ("no auxiliary schedule rescues foraging retention"); the mechanistic label is
> narrowed -- the auxiliary is out-competed by the RL objective TOWARD SURVIVAL, which is
> reward-coupling, not auxiliary decay.

**(iv) `H-retention-critic` and `H-retention-consolidation` — effect-size rider** (state
unchanged, both stay CONFIRMED):

> SUB-SKILL DECOMPOSITION RIDER (added 2026-08-07,
> competence_floor_instrument_audit_2026-08-07.md section 3a/3b; PROMOTES/DEMOTES NOTHING
> and this leg STAYS confirmed). The DV `foraging_competence` is resources per EPISODE and
> episode length varies ~2.4x across these arms, so it multiplies foraging rate by survival
> duration. Decomposed: H-retention-critic composite 3.28x = rate 1.42x x duration 2.41x
> (~29% / ~74% of the log-effect); H-retention-consolidation kl0p30 composite 1.73x = rate
> 1.22x x duration 1.43x. `goal_reach_rate` is at ceiling in BOTH arms of both legs
> (0.95-0.97), so neither mechanism restores WHETHER the agent consumes -- it extends how
> long it keeps doing so. The confirmations stand and the direction is unchanged; the
> effect on foraging skill per unit time is roughly half the headline figure.

**(v) `H-consummation-binding` — recommend downgrade to `alive`** with an
observation-bottleneck note per section 3d (both arms exactly 0.000 forage, 0.000
`goal_reach_rate`, survival 17.8/15.0 below `random_walk`'s 34.0, no trajectory peak
re-clearing the install floor on any seed, install at 14% of ceiling vs 44% elsewhere).
A tie at the absolute floor is not a discrimination. Governance's call; stated here so it
is on the record either way.

---

## 7. Answer to the question the audit was commissioned to settle

**Should the campaign open a 6th fan-out round?**

**No — not on the current instrument.** The recurrence GOV-FROZEN-1 flagged is not a
shortage of mechanism hypotheses; it is that each round enumerates rivals from the residue
of a composite DV that (a) multiplies foraging rate by survival duration, (b) has a
structurally dead hazard channel on D3, (c) discards seven of eight sub-skill metrics at
every trajectory probe, and (d) has already produced at least one leg (`H-consummation-
binding`) spawned off a misread of its own residue (section 4). A 6th round on that
instrument will manufacture a 21st hypothesis at the same rate as the previous five.

**Do this instead, in order — all cheap:**

1. **Void `H-bc-prior` child 3** (section 5e). It is the only *live* explanandum in the
   question and it is an artifact. Removing it removes the seed for hypothesis #21.
2. **Land the one-line probe fix** — have `make_probe_fn` return the full `evaluate_seed`
   row instead of projecting to `foraging_competence`, and plumb the sub-skill series into
   the manifest. `retained_fraction` / `competence_half_life` keep reading
   `foraging_competence` off the richer row, so the change is additive and every existing
   caller stays byte-identical in its verdict.
3. **Re-pose the DV before the next experiment, not after it** — report foraging *rate*
   alongside the per-episode count, and treat `survival_horizon` as a covariate to be
   reported rather than a sub-skill, since it is bimodal in D3 (section 2).
4. **Then** decide whether anything is left to fan out. On the decomposition, the two
   confirmed retention mechanisms are doing something narrower and better-specified than
   "retaining competence": they keep the agent alive long enough to keep foraging, with a
   modest (1.2-1.4x) improvement in foraging rate. That is a sharper claim than MECH-457
   currently carries and may be closer to a decidable question than a 6th round of rivals.

---

## Provenance

- Data: `REE_assembly/evidence/experiments/<run_id>.json` -> `arm_results[]` for
  V3-EXQ-747/748/748a/749/751/752/753/754/755/765/770/771/772/780/781/782/788/789/792/792a/
  819/819a/821/836/836a/836c/836d/837.
- No experiment was run, re-run, or queued. No substrate change. No compute.
- Not written by this session: `hypothesis_space_registry.v1.json`, `claims.yaml`, any
  manifest, `review_tracker.json`, `substrate_queue.json`.
- Chip: `chip-20260807-competence-floor-instrument-audit`.
