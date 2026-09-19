# V3-EXQ-1043a -- staged design (MECH-537 communication-subspace orientation contrast)

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, experiment_queue.json, or ree-v3/experiments/. No experiment is queued.**

- Campaign: `science-20260918-mech537-communication-subspace`
- Chip: `chip-20260918-mech537-communication-subspace-permutation-null`
- Authority: `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-1043_2026-09-17.json` (status `confirmed`, Step 8 gate held with the user 2026-09-17)
- Predecessor: `V3-EXQ-1043`, run `v3_exq_1043_mech537_communication_subspace_routing_20260916T111630Z_v3` (FAIL, `routing_signature_incomplete_undetermined`, `elapsed_seconds` 7079 for 3 seeds)
- Driver to modify: `ree-v3/experiments/v3_exq_1043_mech537_communication_subspace_routing.py` (1867 lines, origin/main)

## Why this file exists rather than a queued experiment

Three of the autopsy's four `required_changes` are fully specified and are worked out below,
to the point of implementation. The fourth -- **anchor C4b's absolute 0.5 ceiling from a
measured reference** -- cannot be executed as specified, because **no such measured reference
exists**. C4b is `load_bearing: true, scored_as_conjunct: true`, so its threshold is a pass
criterion, and the dispatching chip names this case explicitly as a STOP:

> The MEASURED REFERENCE for C4b's ceiling (required change 3). If you cannot identify one in
> the 1002/1008/1010 lineage, do NOT keep 0.5 and do NOT invent a constant -- that is a
> decision chip.

Raised as decision chip `chip-20260918-mech537-c4b-ceiling-anchor`. Everything below is
option-independent and should be implemented as written once that question is answered.

---

## 1. The C4b anchor search -- what was looked for, and what was found

C4b scores `sensitivity_ratio` from `_decision_sensitivity` (driver :707): the ratio of
`mean ||dz_world||` along the **complement component** of each of the five oracle decision
coordinates to that along its **communication-subspace component**, components taken
UN-NORMALISED. Pre-registered ceiling `INSENSITIVITY_RATIO_MAX = 0.50` (driver :385).

**Searched, exhaustively:**

| source | result |
|---|---|
| `experiments/v3_exq_1002_zworld_actor_adequacy_oracle_adapter.py` | 0 matches for `sensitivity_ratio` / `dz_world` / `INSENSITIV` |
| `experiments/v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis.py` | 0 matches |
| `experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py` | 0 matches |
| `REE_assembly/evidence/experiments/*.json` carrying `sensitivity_ratio` | 4 files: `arm_fingerprint_index.json`; V3-EXQ-1000 (`rsd_sensitivity_ratio_per_seed`, an RSD-engagement statistic); V3-EXQ-1006 (`action_sensitivity_ratio`); and V3-EXQ-1043 itself. None of the first three measures an encoder complement/comm `||dz_world||` ratio. |

**The lineage contains no measurement of this statistic at all.** Every measured value of it
in the corpus comes from V3-EXQ-1043 itself (eps_frac 0.10, per seed 42/43/44):

| reference | seed 42 | seed 43 | seed 44 | what it is |
|---|---|---|---|---|
| **measured (fitted subspace)** | 0.8368 | 0.8318 | 0.8718 | the quantity C4b scores; FAILED 0/3 against 0.50 |
| matched-rank random-subspace null | 1.3849 | 1.3870 | 1.2133 | C4a's comparator; **retention-confounded**, autopsy-withdrawn from the scored conjunct |
| **isotropic-Jacobian prediction** | 1.0331 | 1.0734 | 1.0382 | `mean_raw_norm_complement_component / mean_raw_norm_comm_component` on the **fitted** decomposition -- retention-matched by construction |
| generic whole-subspace probe (diagnostic, NOT this probe) | 0.5098 | 0.4578 | 0.5199 | different question by the driver's own statement; a generic complement direction puts ~1.5% of its energy on the decision coordinates |
| dry-run smoke, no-routing end | 6.46 | -- | -- | the far end of the dynamic range |

**Verification that the isotropic-Jacobian row is the autopsy's own statistic**, not a new
invention: the autopsy states the C4a margin predicted from retention geometry alone is
`0.348 / 0.267 / 0.365`. Recomputing it as `iso_pred(null) - iso_pred(measured)` from the
manifest's recorded `raw_norm_*_component` fields gives **0.3478 / 0.2667 / 0.3647** -- an
exact reproduction. The null's own measured ratio (1.3849) also sits essentially on its own
isotropic prediction (1.3808), which independently validates the prediction as a reference.

**Two findings that bear on the decision:**

1. **Nothing measured anywhere sits at or below 0.50 on the aimed probe.** The lowest
   measured value on this statistic is 0.8318. An absolute ceiling of 0.50 therefore has no
   demonstrated reachability -- exactly the anchor-reachability failure mode the driver itself
   warns about at `INSENSITIVITY_NULL_MARGIN` ("an absolute-only gate at 0.25 would then have
   been close to unmeetable by construction for a nonlinear MLP encoder").
2. **The only measured value near 0.50 is the GENERIC probe (0.510/0.458/0.520).** The 0.50
   constant looks calibrated -- consciously or not -- against the generic probe, while C4b
   scores the AIMED probe, whose scale is ~1.6x higher because the decision coordinates are
   not generic directions. The driver's docstring is explicit that these are different
   questions and that only the aimed one is MECH-537's.

Options put to the user are in the decision chip; none is adopted here.

---

## 2. Permutation null for C2 (`required_changes[3]`) -- SPECIFIED, implement as written

### 2.1 What is permuted

Refit `interface_probe.communication_subspace` (interface_probe.py:387) on **shuffled
sender-receiver pairing**: permute the rows of the receiver tensor `z_tr` relative to
`xs_tr[:, keep]`, holding `groups=g_tr`, `n_folds=RRR_FOLDS`, `ridge=ridge_tr` and the fit
seed identical to the observed fit.

### 2.2 The permutation MUST be WITHIN episode group, not across it

`_kfold_indices` (interface_probe.py:300-330) builds a **grouped** k-fold: it folds over the
distinct group values and every row of an episode lands entirely in one fold.

- **Across-episode permutation leaks.** If episode *i*'s sender rows are paired with episode
  *j*'s receiver rows and *i*, *j* land in different folds, a test row's target value is
  literally also a training-row target. The fit is then optimistic and the null is inflated,
  which biases the test toward declaring the observed contrast unremarkable.
- **Within-episode permutation is fold-safe and preserves the blocking exactly.** Row *n*
  keeps its group label `g_n`, and its permuted partner also comes from `g_n`, so the grouped
  fold structure is bit-identical to the observed fit's. It destroys the timestep-level
  sender-receiver correspondence, which is where the routing signal lives.

This is the direct reading of the chip's instruction ("Preserve the `groups=` episode
blocking ... shuffling across folds leaks and makes the null optimistic").

### 2.3 The statistic and the reference distribution

C2's DEFINITION is unchanged: `C2 = D_randrank - D_comm`, the rank-matched orientation
contrast. What changes is its reference: the hand-set `ORIENTATION_MARGIN = 0.05` floor is
replaced by the within-run permutation distribution.

Per seed, for `b = 1..N_PERM`:

1. permute `z_tr` within episode groups under permutation seed `seed * 104729 + b`;
2. refit `communication_subspace` at the same rank ladder; take the basis at the scored rank
   (section 3);
3. train the identical decoder on `P_comm_perm^(b) X` under the identical protocol -> `D_comm_perm^(b)`;
4. `C2_null^(b) = D_randrank - D_comm_perm^(b)`.

**The `ws250_randrank` comparator is held FIXED across replicates, deliberately.** It is the
same draw that enters `C2_obs`, so the comparison is PAIRED and the common term cancels: the
test is equivalent to asking whether `D_comm` sits below the distribution of
`D_comm_perm^(b)`. Re-drawing the random subspace per replicate would integrate the draw
noise into the null without matching it in the observed statistic, and would cost a second
decoder fit per replicate for strictly less power. The fixed draw and its `D_randrank` are
recorded either way.

### 2.4 Decision rule

One-sided permutation p-value per seed:

```
p_seed = (1 + #{b : C2_null^(b) >= C2_obs}) / (1 + N_PERM)
```

`alpha = 0.05`, one-sided. This is the conventional permutation-test alpha, not a domain
constant, and is NOT the withdrawn effect-size floor (which was also 0.05 -- the collision is
coincidental and should be called out in the driver docstring so a later reader does not
conflate them). The per-seed statistic is a p-value; seed aggregation is by the majority rule
in section 4.

`ORIENTATION_MARGIN = 0.05` is removed from the scored predicate. The raw contrast, its sd,
and the full null distribution are still recorded, so the old predicate remains recomputable
from the manifest.

### 2.5 N_PERM and cost

`N_PERM` drives cost linearly: each replicate is one RRR refit plus one decoder fit
(`ADAPTER_PASSES = 60`). `N_PERM = 200` gives a minimum attainable p of 1/201 = 0.00498,
comfortably below alpha. Recommended `N_PERM = 200` if the budget allows; `N_PERM = 100`
(min p 0.0099) is an acceptable fallback. Restrict the ladder to the single scored rank for
the permutation refits (`ranks=[r_pars]`) -- the full 1..32 ladder is not needed for the null
and is the expensive part of `communication_subspace`.

---

## 3. Parsimonious-rank read (`required_changes[1]`) -- SPECIFIED, implement as written

### 3.1 The selection rule

`r_pars` = the **smallest** rank whose grouped-CV held-out R^2 is within
`PARSIMONIOUS_R2_TOL = 1.0e-3` of the ladder maximum. This is the autopsy's own wording
("8-10, where heldout r2 is already within 0.001 of its maximum") and it is a within-run,
cross-validated rule, not a hand-set rank.

**Reproduced from the landed manifest's `rrr_heldout_r2_by_rank`:**

| seed | ladder max R^2 | `r_pars` @ tol 1e-3 | R^2 at `r_pars` | CV argmax rank |
|---|---|---|---|---|
| 42 | 0.9982016 | **8** | 0.9972673 | 32 |
| 43 | 0.9976504 | **10** | 0.9969034 | 32 |
| 44 | 0.9970947 | **10** | 0.9962551 | 32 |

Exactly the autopsy's 8 / 10 / 10. The rule is fully determined by the source; no choice is
being made here.

### 3.2 Where the parsimonious basis comes from

`communication_subspace` returns a basis only at its own `selected_rank`. Obtain the
parsimonious basis by re-calling the same library function with `ranks=[r_pars]` -- it then
refits on all rows at exactly that rank via `_rrr_fit_full_data`. **No change to
`interface_probe.py`.** Determine `r_pars` from the full-ladder call that already runs.

### 3.3 Which rank C2 is SCORED at

**C2 is scored at `r_pars`.** The autopsy: "The low-rank premise the biology supplies is not
testable at rank = dy, where the RRR fit is unconstrained OLS; it is testable there."

C2 at the CV-selected rank (= 32 on 3/3 seeds) is still computed and RECORDED, as is C2 as a
function of rank across the whole ladder, so the rank dependence is on the record and the
1043 comparison is direct. The `ws250_comm`, `ws250_perp` and `ws250_randrank` arms are
therefore instantiated at BOTH ranks; `ws250_full` is rank-independent and is fitted once.

---

## 4. Seed count (`required_changes[2]`) -- SPECIFIED, implement as written

`SEEDS = [42, 43, 44, 45, 46, 47]` (n = 6), `SEED_MAJORITY = 4`.

This is the proportional re-specification the autopsy requires and the chip pre-authorises:
the inherited rule is 2 of 3 = 2/3, so 6 seeds -> 4. It must be a LOCAL constant on 1043a, not
`x1002.SEED_MAJORITY` (which is the fixed 2 the autopsy warns about: leaving it at 2 while
raising n converts a majority clause into "any 2 seeds" and weakens the predicate).

Any other majority rule would be a decision chip and none is taken.

Carry forward from the autopsy, verbatim, into the driver docstring: *"at adequate n the
likely outcome is a confidence interval EXCLUDING 0.05 -- i.e. H1 falsified rather than
rescued. Raise n to settle the question, not to pass it."*

### Cost

V3-EXQ-1043 was 7079 s for 3 seeds (~2360 s/seed) -- but most of that is the warmup, which is
per seed and unchanged. Added per seed: 3 extra decode arms at `r_pars`, plus `N_PERM` RRR
refits and decoder fits at a single rank. Expect roughly 3-5x the 1043 wall clock at n=6 with
`N_PERM = 200`. Route to a cloud worker; do not run the smoke on the laptop beyond `--dry-run`.

---

## 5. Binding negatives -- carried into the driver, all still in force

- **Do NOT promote C4a to the scored conjunct.** Retention-confounded by the driver's own
  design decision; retention geometry alone predicts 0.348/0.267/0.365 of an observed
  0.548/0.555/0.342 margin, and on seed 44 geometry OVER-predicts. Keep it recorded as a
  diagnostic **with its confound stated in the manifest prose**, which the driver already does.
- **Do NOT extend the RRR rank ladder.** Mathematically impossible: rank <= dy = 32 and the
  ladder is already 1..32.
- **KEEP `EXPERIMENT_PURPOSE = "diagnostic"`** (driver :19, :314). Promoting it to `evidence`
  is a scope change the autopsy did not authorise.
- **No criterion asserting an exact committed ACTION.** `torch.multinomial` diverges across
  machine classes; assert upstream of the discrete quantizer, as this driver already does.
- **Not a lit-pull.** `targeted_review_mutual_legibility_communication_subspaces` already
  carries Semedo2019 / Binish2026 / Gonzalez2026.
- **Alphabetic suffix `V3-EXQ-1043a`**, not a new number.

## 6. Stated limitation to carry into the docstring

The encoder under test carries the **SD-106** limitation and 1043 ran with
`p0a_field_weight_on = 0.0`. SD-106 is an OPEN `substrate_queue.json` entry but its severity
is `degrading`, not `corrupting`, so the `/queue-experiment` Step 2.5c gate does not block.
Keep the `source_adequacy_ws250_full` readiness precondition (it MET at 0.9335 against a 0.80
floor). State the limitation; do not treat it as a blocker.

## 7. Noted, not resolved here

`claims.yaml` MECH-537 carries a live `notes` instruction "DO NOT queue an experiment from
this entry" (2026-09-08) alongside the `what_would_answer` "Disposition 2026-09-15" that mints
EXP-1403 and authorises exactly this run. Both are current text on the same entry. The
autopsy surfaced this to governance and its Step 8 gate confirmed the routing with the user
present; V3-EXQ-1043 has already run. Recorded here so a later reader does not re-litigate it,
and it is governance's to clean up, not this design's.


---

# ADDENDUM 2026-09-19 -- OPTION C RATIFIED, DRIVER BUILT, ONE CONSTANT STILL OPEN

**Status of this addendum: the driver is LANDED but NOT QUEUED.** Nothing runs it; no
`experiment_queue.json` entry exists.

## A1. What the user decided

`chip-20260918-mech537-c4b-ceiling-anchor`, answered 2026-09-19T00:49:12Z via the
Orchestrator's decision lane: **OPTION C -- measure the floor, then keep C4b ABSOLUTE above
it.** With the condition, verbatim: *"the rule that maps floor -> ceiling must be fixed in the
pre-registration BEFORE the run and must not be tunable after seeing data -- if your staged doc
does not already fix that rule, that single number/rule is one more decision chip."*

It did not. Section 1 of this file ended "Options put to the user are in the decision chip;
none is adopted here", and the Option C text as put was a *reachability gate* with the ceiling
retained at 0.50, not a map from floor to ceiling. So the map is genuinely unfixed and was
raised as `chip-20260919-mech537-c4b-floor-to-ceiling-rule` (Rule 1 arithmetic midpoint
`(F+I)/2` -- recommended, parameter-free; Rule 2 geometric `sqrt(F*I)`; Rule 3 keep 0.50 with F
as a reachability gate only). **That is the one thing still open.**

The driver implements Rule 1 in a single named function, `_c4b_ceiling`, so applying a
different answer is a one-expression change plus a re-run of the self-test.

## A2. The driver, as built

`ree-v3/experiments/v3_exq_1043a_mech537_communication_subspace_permutation_null.py`
(copied from the 1043 driver; `QUEUE_ID = "V3-EXQ-1043a"`, `SUPERSEDES = "V3-EXQ-1043"`,
`EXPERIMENT_PURPOSE` still `"diagnostic"`).

Six new instrument functions, all covered by `--self-test`:
`_parsimonious_rank`, `_permute_within_groups`, `_permutation_p_value`, `_jacobian_std_gram`,
`_jacobian_aligned_basis`, `_c4b_ceiling`.

**Gates run:** `--self-test` 45/45 PASS; `validate_experiments.py --strict` OK (0 findings of
any class); `--dry-run` smoke rc=0 end to end, exercising every new path.

Two self-tests are worth naming because they pin the design to its authority rather than to a
fixture: `_parsimonious_rank` is replayed over **V3-EXQ-1043's landed `rrr_heldout_r2_by_rank`**
and must return the autopsy's stated **8**; and `SEED_MAJORITY` is pinned to differ from
`x1002.SEED_MAJORITY`, which is the exact failure the autopsy named ("it is a fixed constant 2,
inherited from x1002").

## A3. The one design call this session made, and the road not taken

**WHICH RANK THE SCORED CRITERIA READ.** The autopsy names C2 ("read it at the PARSIMONIOUS
rank"). It does not mention C1/C3/C4/C5. But C4b splits each oracle decision coordinate **by
the same subspace** C2 is computed on, and C5 asks whether **that subspace** is stable -- so
scoring C2 at one rank and C4b/C5 at another would make the confirming conjunction a statement
about two different subspaces. That is not a coherent alternative; it is a defect.

**Call made:** the whole SCORED criteria set reads the parsimonious rank. The CV-selected-rank
configuration -- V3-EXQ-1043's exact one -- is computed and recorded in full alongside it, so
the 1043 comparison stays direct and a later autopsy can contest this against numbers rather
than against an absence.

**Road not taken, recorded:** score C2 at the parsimonious rank and leave C1/C3/C4/C5 at the
CV-selected rank. Written into the driver at the point of the decision, not only here.

Two consequences followed mechanically and are flagged so a reviewer checks them: the
`randrank_control_supra_trivial` readiness assert now reads `ARM_RAND_P` (it exists to show
C2's comparator can move, so it must report the arm C2 routes on), and the cross-seed stability
diagnostic now compares the parsimonious-rank bases.

## A4. INSTRUMENT RISK FOUND IN THE SMOKE -- must be settled before queueing

The `--dry-run` smoke printed:

```
[c4b] seed=42 SCORED rank=1 ratio=4.4625 floor(F)=4.4526 isotropic(I)=4.3328 ceiling=nan
```

`F > I`, so `_c4b_ceiling`'s reachability guard fired and C4b was correctly scored UNREACHABLE
rather than failed -- the guard working as designed. But it exposes a real structural question
that the arithmetic in the two references makes plain:

    measured ratio = (||b|| / ||a||) x (|J(u_out)| / |J(u_in)|)
    I              = (||b_fitted|| / ||a_fitted||)          -- SAME decomposition as measured
    F              = (||b_jac|| / ||a_jac||) x (|J(u_out_jac)| / |J(u_in_jac)|)

`measured` and `I` share a decomposition, so that pair is clean and retention-matched -- which
is exactly why `I` is a sound no-routing reference. **`F` is computed on a DIFFERENT
decomposition**, so it mixes a sensitivity factor (which the Jacobian alignment minimises, the
intended effect) with a geometry factor `||b_jac||/||a_jac||` (which it does not control). If
the geometry factor dominates, `F` can exceed `I` and the anchor is unscoreable.

At the dry run's rank 1 that is exactly what happens, and the three numbers collapsing to ~4.4
within 3% of each other says the geometry factor dominated and the sensitivity factor was ~1.
**Rank 1 is degenerate** (80 rows, ladder row-capped) and settles nothing about ranks 8-10,
where 1043a actually scores.

**This is not speculation to carry into a multi-hour run.** A mid-scale probe was written and
run for exactly this: `probe_c4b_anchor_reachability.py` calls `_run_seed` directly at ~40%
scale (zworld_p0 24 / p0 80 / p1 36 / bc 16+8, 5 permutations, 8 Jacobian states) and prints
`r_pars`, measured, F, I, the ceiling and whether `F < I`, at both ranks.

**Owed before queueing, in this order:**
1. Run that probe to a realistic rank and read `F` against `I`.
2. If `F < I` comfortably at rank 8-10, the anchor is reachable and Rules 1 and 2 are both
   workable -- proceed on whichever the user picks.
3. If `F >= I` at a realistic rank, **Rules 1 and 2 are BOTH unworkable** (each needs a
   measured interval to sit inside) and the honest answer to
   `chip-20260919-mech537-c4b-floor-to-ceiling-rule` is Rule 3 or a re-specified `F`. Say so
   on that chip rather than shipping a criterion that cannot score.

## A5. Cost, measured rather than assumed

V3-EXQ-1043 was `elapsed_seconds` 7079 for 3 seeds (~2360 s/seed), warmup-dominated. 1043a adds
per seed: 3 arms at the parsimonious rank, 2 decision-sensitivity probes with a third
(Jacobian-aligned) reference each, one Jacobian Gram (~`n_live` x `N_JACOBIAN_STATES` forward
passes, rank-independent so built once), and **`N_PERMUTATIONS` RRR refits plus decoder fits**
-- which is the dominant new cost and scales linearly.

At n=6 and `N_PERMUTATIONS = 200` expect roughly 3-5x the 1043 wall clock, i.e. ~10-12 hours.
Section 2.5 pre-registers `N_PERMUTATIONS = 100` (min attainable p 1/101 = 0.0099, still well
below alpha) as an acceptable fallback; choosing it on measured runtime grounds is inside the
pre-registration, and which value is in force is recorded in the manifest's `pre_registered`
block either way.

## A6. State

| item | state |
|---|---|
| driver | LANDED on `ree-v3` `main` (see commit trailer for shas), NOT queued |
| self-test | 45/45 PASS |
| `validate_experiments --strict` | OK, 0 findings |
| `--dry-run` smoke | rc=0, every new path exercised |
| queue entry | NOT written |
| floor -> ceiling rule | OPEN -- `chip-20260919-mech537-c4b-floor-to-ceiling-rule` |
| anchor reachability at a realistic rank | OPEN -- run `probe_c4b_anchor_reachability.py` |
