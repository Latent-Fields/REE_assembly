**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml.**

The one registry edit this session DID make is `evidence/planning/hypothesis_space_registry.v1.json`
qid `mech321_harm_aware_selection_task_effect` -> `decision.live_gate` (a live-state field the chip
brief explicitly instructed to bring up to date). No claim status, confidence, `evidence_direction`,
`v3_pending` or `resolution.state` was touched anywhere.

# MECH-321 harm-aware selection -- measurement redesign

- **Session:** `metaworker-chip-20260808-mech321-repose-measurement-design` (headless, metaworker-dispatch)
- **Chip:** `chip-20260808-mech321-repose-measurement-design`
- **Written:** 2026-08-08T09:15:37Z
- **Deliverable:** chip option (a) -- a concrete redesigned experiment plan ready to hand to `/queue-experiment`.
- **Scope:** design/scoping only. No experiment script written, no queue entry appended, no `/queue-experiment` invocation.

---

## 0. Summary for the reader in a hurry

Four generations (V3-EXQ-844 / 867 / 867a / 867b) have failed to test MECH-321's load-bearing
task-outcome criterion. The 2026-08-05 autopsy concluded the *matched-pair design family* is
structurally falsified and called for a redesigned DV. **That routing is right and this design
follows it. Its stated reason is wrong, and the correction matters, because the wrong reason
would send the redesign after the wrong problem.**

Three findings, each derived from V3-EXQ-867b's own recorded manifest:

1. **The screen-soundness falsification is an instrumentation artifact, not a fact about the
   mechanism.** 867b's screen cells are run with no RNG reset; its measurement cells are not.
   The two phases therefore measure *different agents*, so the prefix-monotonicity argument the
   screen rests on never applied. The violation appears in the **OFF arm**, which carries no
   manipulation at all -- so "the ON-arm manipulation perturbs decomposition timing" cannot be
   what produced it. (§2)
2. **Matched-pairing was never actually falsified.** At the full measurement schedule the
   matching held *perfectly*: 4 `both_decompose`, **0** `on_only`, **0** `off_only`. The
   discordant tiers -- the ones whose existence would demonstrate the manipulation perturbing
   decomposition -- are empty. (§2.3)
3. **The real defect is that the DV is conditioned on the wrong event.** The manipulation is
   *unconditionally* active: ON-arm `decomp_n_harm_bias_nonzero` is 270-1005 on **every one of
   the 10 measured seeds**, including all six "neither-decompose" seeds used as negative
   controls. Conditioning C1 on the rare mid-execution decomposition discards 6 of 10
   experimental units and, on this run's own numbers, discards the *lower-variance* ones. The
   "negative control" tier is not a control -- `action_sequences_identical: false` on all six. (§3)

So the redesign is not merely "a different DV because the old one broke". It is: **stop
conditioning on a rare downstream event when the manipulation is active everywhere, stop
spending 53% of the compute budget on a screen that is anti-informative, and spend the whole
budget on seeds** -- which is the only axis that buys precision here (§4: between-seed effect
heterogeneity SD 0.145 vs within-seed measurement SE 0.018, an 8x ratio).

The proposed run (§5) reaches **SE ~= 0.023 at n=40 seeds for ~1.9x 867b's compute**, against
867b's realised SE of 0.111 at n=4 -- a ~4.8x precision gain -- and carries an A-A control that
discharges the `what_would_answer` precondition (2) *by construction* rather than by assumption.

**This design is deliberately NOT a fifth same-family iteration.** It changes the experimental
unit (all seeds, not screened matched pairs), the DV (unconditional whole-episode, not
post-divergence-windowed fresh-tick), and the sampling strategy (no screen). Per the EXQ
convention in CLAUDE.md that is a **new number**, not a `867c` letter -- see §7.

---

## 1. What each of the four prior generations actually failed on

| Run | Date | Failure | Load-bearing? |
|---|---|---|---|
| V3-EXQ-844 | 2026-08-01 | C2 (mechanistic PE-reduction) passes; C1 (harm outcome) weakens. Root cause found in source: no harm signal reached the redecomposition step and there was no ranked selection at all. | yes -- and it produced the substrate build |
| V3-EXQ-867 | 2026-08-02 | Manipulation never engaged (`decomp_n_harm_bias_nonzero=0`, both arms, all seeds). No SD-029 hazard tuning; three stream flags missing. | no -- `non_contributory` |
| V3-EXQ-867a | 2026-08-03 | Manipulation engages (972 nonzero). C1 ran on **n=2** matched seeds with opposite-signed deltas. Power guard was vacuous (`min(6, n_observed)`). | no -- `non_contributory` |
| V3-EXQ-867b | 2026-08-04 | Hard floor n>=6 + 48-candidate screen. Still only **n=4**; pool declared exhausted. Screen-soundness check falsified on 5/7 seeds. | no -- `non_contributory` |

The substrate is not in question. `SD-hazard-aware-policy-decomposition` (built 2026-08-01)
engages correctly and reads the harm signal correctly; that has been true since 867a. Every
failure since has been a **measurement** failure.

---

## 2. Re-diagnosis of V3-EXQ-867b's screen-soundness falsification

### 2.1 What 867b claimed, and why the claim was reasonable

The driver's module docstring argues, correctly in form:

> `_run_cell` at K episodes is a bit-identical PREFIX of the same cell at N>K episodes (same RNG
> reset at cell entry via `arm_cell`, same per-cell env seed, nothing in the loop reads
> `episodes`), and `PolicyDecomposition.reset()` is explicitly NOT called on the agent's
> per-episode reset, so `decomp_n_decomposed_midexec` accumulates monotonically across the whole
> cell. Therefore: screened both-arms-decompose at SCREEN_EPISODES ==> both-arms-decompose at the
> full EPISODES (guaranteed).

The argument is valid **given identical initial conditions**. The two phases do not have them.

### 2.2 The defect, located in source

`ree-v3/experiments/v3_exq_867b_mech321_harm_aware_selection_matched_pool.py`:

- **Measurement cells** (line ~1138) enter through `with arm_cell(seed, ...)`. `_ArmCell.__enter__`
  (`experiments/_lib/arm_fingerprint.py:808-812`) calls `reset_all_rng(self.seed)` when
  `do_reset` is true, which it is by default. So every measurement cell begins from a torch RNG
  state that is a pure function of `seed`.
- **Screen cells** (lines 516 and 528) call `_run_cell(...)` **directly**. There is no `arm_cell`
  and no `reset_all_rng` anywhere in `_screen_pool`.
- `_build()` (line ~375) constructs `REEAgent(cfg)` with no seeding of its own. Only the
  *environment* is seeded per cell (`env_kwargs_hazard_tuned` sets `kwargs["seed"] = seed`).
  `torch.nn.Module` weight init draws from torch's **global** RNG -- the exact hazard documented
  at length in `arm_fingerprint.seeded_construct`'s docstring.

Consequence: a screen cell for `(seed S, ARM_OFF)` and a measurement cell for `(seed S, ARM_OFF)`
run **different agents** -- same environment layout, different initial weights -- because the
screen cell's weights are a function of however many draws the preceding 0..68 screen cells
consumed. The 4-episode cell is not a prefix of the 12-episode cell. It is a different
trajectory.

### 2.3 The proof is arithmetic, and it is in the run's own manifest

`multi_action_commits` is a monotone counter. If the 12-episode cell genuinely contained the
4-episode cell as a prefix, it could not end **lower**. In the **OFF arm** it does, on five seeds:

| seed | OFF `multi_action_commits` @4ep (screen) | @12ep (measure) | OFF `decomp_midexec` @4ep | @12ep |
|---|---|---|---|---|
| 31 | 4 | **0** | 2 | **0** |
| 41 | 7 | **0** | 3 | **0** |
| 51 | 24 | **0** | 9 | **0** |
| 77 | 30 | **0** | 19 | **0** |
| 19 | 32 | **0** | 1 | **0** |

Two independent reasons this cannot be the manipulation:

1. It is the **OFF arm**. `decomp_n_harm_bias_nonzero == 0` and
   `decomp_n_harm_override_fires == 0` on **every** OFF measurement cell (verified across all 10
   seeds). The manipulation is inert there by construction.
2. A monotone counter decreasing over a strict superset of episodes is not a behavioural
   finding of any kind. It is a statement that the two runs are not the same run.

And the converse direction is just as stark -- seeds 11 and 23 were selected as *zero-activity
negative controls* on the strength of `multi_action_commits = 0` in **both** arms at the screen,
then produced 95/126 and 293/284 multi-action commits at measurement and landed in
`both_decompose`. That is not "decomposition started in a later episode"; it is a different
trajectory from tick 0.

### 2.4 What this does and does not overturn

**Overturned:** the inference recorded in the confirmed autopsy, in `claims.yaml` MECH-321's
`evidence_quality_note` and `what_would_answer`, and in the hypothesis-space registry's
`observation_bottleneck` -- that the screen-soundness violation is *"direct evidence the ON-arm
manipulation itself perturbs whether/when decomposition fires, undermining the matched-pair
premise structurally"*. 867b's data does not show that. The manipulation's inertness in the arm
where the violation appears rules it out.

Indeed 867b's own tier table points the other way: at the full measurement schedule,
`on_only_decompose: []` and `off_only_decompose: []`. **Zero discordant seeds out of ten.** Every
seed that decomposed mid-execution did so in *both* arms. If the manipulation materially
perturbed whether decomposition fires, the discordant tiers are exactly where it would show, and
they are empty.

**Not overturned:** the routing. A redesigned DV that does not depend on post-hoc
divergence-tick matching is still the right next move -- for the reason in §3, which is stronger
and independent of the screen defect. Governance ratified the routing on 2026-08-07; this design
implements it. Only the *rationale* recorded alongside it needs correcting.

**Also not overturned:** the pool-exhaustion finding, but it needs re-reading. "Only 7 of 48
candidates screen-matched" is a statement about a screen that does not predict the measurement,
so it does not license the conclusion that seeds which decompose are rare. The measurement-side
base rate is the trustworthy one: **4 of 10 measured seeds landed `both_decompose`** (~40%),
which is not an exhausted pool.

### 2.5 Generalisable instrumentation gap (affects any screen-then-measure driver)

`validate_experiments.agent_construction_before_seed_lint` does **not** fire on 867b, and is
correct not to under its stated Tier-1 scope: it only fires on a function whose own flow contains
*both* an agent construction and a seed call in the wrong order. Here `_build` / `_run_cell` /
`_screen_pool` contain **no** seed call at all -- the scoped-out "constructs an agent with NO seed
call anywhere in its own local flow" case -- and `main`'s `arm_cell` use is correctly ordered at
the one site that has it.

The uncovered shape is: **a driver that wraps SOME cells in `arm_cell` and runs OTHERS bare, then
compares the two.** Each site is individually defensible; the comparison between them is not.
Any screen-then-measure, pilot-then-confirm, or calibrate-then-run design can reproduce it.
Raised separately as a governance flag (§8); a lint proposal is out of this chip's scope.

---

## 3. The deeper defect: the DV is conditioned on an event the manipulation does not need

This is the finding that actually justifies the redesign, and it is independent of §2.

MECH-321's harm-aware selection runs at **two** phases -- pre-commit and mid-execution (the R4
first and second phases). The baseline module already records this explicitly:

> Every seed shows `harm_bias_nz > 0` (precommit-phase decomposition evaluates the seeded chunk
> regardless of whether it is ever committed multi-action -- so harm-aware selection engaging is
> orthogonal to SD-084 reachability).
> -- `experiments/_lib/baselines/sd084_midexec_reachability.py`

867b's measurement confirms it. ON-arm engagement across all 10 measured seeds:

| seed | tier | `harm_bias_nonzero` | `harm_override_fires` | ON vs OFF actions identical? |
|---|---|---|---|---|
| 31 | neither | 276 | 90 | no |
| 41 | neither | 462 | 152 | no |
| 103 | both | 375 | 120 | (not in null set) |
| 8 | both | 1005 | 334 | (not in null set) |
| 22 | neither | 612 | 202 | no |
| 51 | neither | 309 | 100 | no |
| 77 | neither | 579 | 189 | no |
| 19 | neither | 975 | 317 | no |
| 11 | both | 270 | 89 | (not in null set) |
| 23 | both | 972 | 323 | (not in null set) |

Two things follow, and both are damaging to the existing design:

**(a) The "negative control" tier is not a control.** Seeds 19/22/31/41/51/77 were scored
`neither_decompose` and used as zero-activity nulls. The manipulation fired 276-975 times on
each of them, and `action_sequences_identical` is **false** on all six -- the arms genuinely
behave differently there. A tier defined by absence of *mid-execution* decomposition says nothing
about whether the manipulation is active. This has been carried unchanged since 867a.

**(b) C1 threw away 6 of its 10 experimental units, and kept the noisier 4.** Whole-episode harm
delta (ON minus OFF; positive = ON less harmful):

| subset | n | mean | sd | SE | mean/SE |
|---|---|---|---|---|---|
| all measured seeds | 10 | **+0.0111** | 0.1465 | 0.0463 | +0.24 |
| `both_decompose` (what C1 used) | 4 | -0.0230 | 0.2391 | 0.1195 | -0.19 |
| `neither_decompose` (discarded) | 6 | **+0.0339** | **0.0529** | 0.0216 | **+1.57** |

The discarded units have **4.5x lower spread** than the retained ones, and lean in the predicted
direction. This is not an argument that the effect is real -- n=6, and the subset was selected
post hoc. It *is* a demonstration that conditioning on mid-execution decomposition is
concentrating the design onto its highest-variance stratum while discarding the phase where the
manipulation is most reliably active.

**(c) The windowing machinery is close to a no-op anyway.** For the 4 C1 pairs, the first
divergence tick is 51/60/60/12 out of 720 ticks, so the "post-divergence window" is 93-98% of the
run. Windowed and whole-run deltas agree closely (seed 8: -0.349 vs -0.327; seed 11: -0.040 vs
-0.024; seed 23: +0.012 vs +0.002; seed 103: +0.183 vs +0.257). What the windowing *does* change
is the `fresh_only` e3-tick restriction, which retains 111/130/573/260 ticks across the four
seeds -- a 5x swing in effective sample per unit, injected straight into the between-unit
variance for no gain in the estimand.

---

## 4. Where the precision actually comes from (the number that decides the design)

Decomposing the per-seed delta's variance on 867b's measurement cells -- within-seed measurement
noise estimated by a 12-block (one block per episode) SE, combined across arms:

```
mean within-seed SE of the delta          0.01837
between-seed SD of the delta              0.14654
implied seed-level effect heterogeneity   0.14538      (sqrt(0.14654^2 - 0.01837^2))
```

**The between-seed term is ~8x the within-seed term.** Consequences, and they are decisive for
how the budget should be spent:

- Adding **episodes per seed** buys almost nothing. Per-seed delta SD as a function of episode
  count: 12ep 0.1465, 6ep 0.1477, 4ep 0.1488, 3ep 0.1500. Cutting 12 -> 4 episodes inflates
  per-seed SD by **1.6%** while cutting per-seed cost **3x**.
- Adding **seeds** is the only lever that moves the pooled SE.
- 867b spent 12 episodes/cell to reach a within-seed SE of 0.018 against a heterogeneity floor of
  0.145. Most of that per-cell compute bought precision the design cannot use.

And the screen was pure overhead: **69 screen cells x 4 episodes = 276 episodes**, against 20
measurement cells x 12 episodes = 240 episodes. The screen consumed **53.5% of the entire
compute budget** (516 episodes, 36,988 s, ~71.7 s/episode) to produce a seed selection that §2
shows was anti-informative -- it rejected both seeds (11, 23) that turned out to be the lineage's
established attributable seeds, and selected five (31/41/51/77/19) that showed zero decomposition
at measurement.

---

## 5. The proposed design

**Working title:** MECH-321 harm-aware selection, unconditional whole-episode harm rate.
**Question (unchanged):** does harm-aware selection in the redecomposition path reduce realised
task harm relative to harm-blind selection?

### 5.1 Unit of comparison -- CHANGED

The experimental unit is the **seed**, and **every measured seed is a unit**. No screening, no
tiering, no post-hoc selection of units by their decomposition behaviour. This is the change that
removes precondition (2)'s dependence from the design rather than trying to satisfy it: there is
no matching assumption left to verify because there is no matching.

### 5.2 DV -- CHANGED

Per seed, paired: `mean_harm_signal(ON) - mean_harm_signal(OFF)` over the **whole run**, all
ticks, positive = ON less harmful. Both quantities are already recorded per cell by the existing
`_run_cell` (`mean_harm_signal`); no new instrumentation is required.

Dropped, deliberately: `_first_divergence_tick`, `_windowed_delta`, `_mean_at`, and the
`fresh_only` e3-tick restriction. Justification in §3(c) -- they change the estimand by ~nothing
and add a 5x per-unit swing in effective sample.

**Pre-registered secondary (reported, never gating):** the same delta restricted to the
`fresh_only` ticks, so the new DV can be cross-read against the 844/867/867a/867b lineage on the
same runs. Reporting both is what makes this design a successor rather than a fresh start.

### 5.3 Arms -- UNCHANGED

`ARM_SELECTION_OFF` and `ARM_SELECTION_ON` exactly as in 867a/867b: hazard-tuned env
(`HAZARD_TUNED_ENV_OVERLAY`) + abort mechanism ON + the three stream flags
(`HAZARD_TUNED_STREAM_FLAGS`) in both arms; the only difference is
`decomposition_use_harm_aware_selection`, at the SD doc's recommended defaults
(`HARM_BIAS_GAIN=0.1`, `HARM_BIAS_SCALE=0.1`, `HARM_THREAT_FLOOR=0.1`, `HARM_THREAT_REF=0.5`,
`HARM_OVERRIDE_W_THRESHOLD=0.9`). Do not move these -- this design repairs the measurement, not
the manipulation.

### 5.4 Schedule -- UNCHANGED at 12 x 60

Keep `EPISODES=12`, `STEPS_PER_EPISODE=60`. §4 shows 4-6 episodes would be statistically
*superior* per unit of compute, and that option is recorded in §6 as the fallback if the run
cannot be afforded. It is **not** the primary, because changing the episode count changes how
trained the agent is at measurement time and therefore the regime the claim is being tested in,
which would confound the comparison against all four prior generations. Regime comparability is
worth more here than the ~1.4x precision, given that the whole point of this run is to be
readable against the lineage.

### 5.5 Seed pool and n -- CHANGED

**n = 40 measurement seeds**, drawn deterministically from a pre-registered candidate list, taken
in order, with **no screening and no exclusion on any measured quantity**. 867b's 48-candidate
list plus the lineage seeds is more than sufficient as a source; the pool is not exhausted (§2.4
-- the measurement-side `both_decompose` base rate is ~40%, and in any case this design does not
require decomposition to occur).

Fixed cell count = 40 x 2 = **80 measurement cells** = 960 episodes ~= **19.1 h** at 867b's
measured 71.7 s/episode. For comparison 867b itself ran 10.3 h. Route to a cloud worker.

Power, at the sd = 0.1465 measured in §4:

| n seeds | SE of pooled mean | detectable at 1xSE | 95% CI half-width |
|---|---|---|---|
| 4 (867b actual) | 0.1195 | 0.120 | 0.234 |
| 10 | 0.0463 | 0.046 | 0.091 |
| 21 (867b's budget, reallocated) | 0.0320 | 0.032 | 0.063 |
| **40 (proposed)** | **0.0232** | **0.023** | **0.045** |
| 80 | 0.0164 | 0.016 | 0.032 |

At n=40 the run either detects an effect at the pre-registered bar or bounds it to +/-0.045 at
95%, against typical OFF-arm whole-run harm of ~-0.16. **A bounded null is a real result here**
and would be the first decisive reading in five attempts -- that is the design's actual purpose
and it should be stated as such in the queue entry.

### 5.6 Bar -- UNCHANGED

`EFFECT_SIZE_K_SIGMA = 1.0`, `REL_IMPROVEMENT_FLOOR = 0.0`, carried verbatim. The autopsy is
right that moving the bar changes the question. What changes is that n is now set by the power
table above rather than by a floor guess, and the guard is a hard `n_seeds >= 40` on **measured
cells**, which cannot be softened by any observed quantity because no unit is ever excluded.

### 5.7 Preconditions (P0) -- one carried, one REPLACED

1. **`harm_bias_engages` (carried).** ON-arm `decomp_n_harm_bias_nonzero > 0`; OFF-arm `== 0`.
   Assert **per cell**, not per run -- 867b satisfied it in aggregate while individual cells
   varied 270-1005. This is `what_would_answer` precondition (1).

2. **A-A NULL CONTROL (new -- this is what discharges precondition (2) by construction).**
   4 additional seeds run as `ARM_SELECTION_OFF` vs `ARM_SELECTION_OFF` -- two cells, identical
   config slice, identical seed, both entered through `arm_cell`. Because `arm_cell.__enter__`
   calls `reset_all_rng(seed)` and the config slices are identical, the two cells must be
   **bit-identical**: `action_sequence` equal and delta **exactly 0.0**.

   Any nonzero A-A delta means the measurement path carries an uncontrolled source of variation
   and **the run is void** -- reported `non_degenerate: false`, no C1 reading emitted. Cost:
   4 x 2 x 12 = 96 episodes (~1.9 h, ~10% of budget).

   This is the direct fix for §2. 867b's screen defect is precisely an uncontrolled source of
   variation between two cells that were assumed comparable, and precisely the thing an A-A
   control detects. It also replaces the `neither_decompose` "negative control" tier, which §3(a)
   shows is not a control.

   **Every cell in the run -- measurement and control alike -- enters through `arm_cell`. There is
   no bare `_run_cell` call anywhere in the driver.** State this as a review-checkable property in
   the queue entry.

### 5.8 Covariates -- reported, never gating

Per seed: `decomp_n_decomposed_midexec` (both arms), `decomp_n_harm_bias_nonzero`,
`decomp_n_harm_override_fires`, `max_z_harm_a_norm`, `multi_action_commits`, and the
`both/on_only/off_only/neither` tier label. Reported for description and for the pre-registered
heterogeneity analysis below -- **never** used to select or weight units.

**Pre-registered heterogeneity analysis (secondary, reported, non-gating).** Spearman correlation
between ON-arm engagement (`decomp_n_harm_bias_nonzero`) and the per-seed delta. On 867b's 10
seeds this is **-0.273**, and the single most-engaged seed (8: 1005 fires, 334 overrides) is also
the single worst outcome (-0.327) -- the outlier that drives most of the sd in §4. Pre-registering
this stops it being read as a post-hoc rescue: if a negative engagement-outcome relation replicates
at n=40, "the mechanism is actively harmful at high threat-scale" becomes the live hypothesis, and
that is a genuine finding about MECH-321, not a measurement artifact. Escapability (Cooper 2016)
and predictability/certainty (Fanselow 2022; Blanchard & Blanchard 1989) are the lit-pull-confirmed
secondary gaps already flagged as deferred at the 2026-08-01 build -- they are the natural place to
look if this relation holds.

### 5.9 What C2 does

`C2_MECHANISTIC_PE_REDUCTION` (forward-PE lower in ON) stays as the non-load-bearing mechanistic
corroboration, computed on the same unconditional whole-run basis. Already supported by
V3-EXQ-844; it should continue to hold.

### 5.10 How this design fails each of the four prior failure modes

| Prior failure | Why it cannot recur here |
|---|---|
| **844** -- no harm signal reached the step; no ranked selection | Structural gap closed by the 2026-08-01 substrate build. Guarded per cell by P0 (1). |
| **867** -- manipulation never engaged | Hazard-tuned env overlay + three stream flags carried verbatim. Guarded per cell by P0 (1), which would have caught 867 on its first cell. |
| **867a** -- n=2, vacuous power guard | n=40 fixed by design. The guard is on **measured cells**, and since no unit is ever excluded, `n_units == n_seeds` identically -- there is no observed quantity for a `min()` to collapse onto. |
| **867b** -- pool exhausted; screen soundness falsified | **No screen exists.** No unit is selected on any measured quantity, so there is no selection assumption to falsify and no pool to exhaust. The specific defect behind the falsification (§2.2) is excluded by the every-cell-through-`arm_cell` rule and detected by the A-A control. |

---

## 6. Fallback if the 19 h budget is refused

Drop to **6 episodes x 60 steps, n=80 seeds** -- same 960-episode budget, SE 0.0165 instead of
0.0232 (§4: per-seed sd rises only 0.1465 -> 0.1477). Statistically strictly better.

The cost is regime comparability: a 6-episode agent is less trained than the 12-episode agents of
all four prior generations, so the run answers the question in a regime the lineage has not
measured. Acceptable only if explicitly noted in the queue entry and the manifest, and it should
not be the default. Do **not** take the further step to 3-4 episodes: mid-execution decomposition
needs enough training to produce multi-action commits at all, and while this DV does not condition
on that, a regime where it never occurs stops being a test of MECH-321's R4 phase in any sense.

---

## 7. Identifier -- new number, not `867c`

CLAUDE.md's EXQ convention: a new letter is for "the scientific question is unchanged but the
implementation was wrong"; a new number is for "the mechanism under test changed, **or the
experimental design is substantially different**".

The question is unchanged, but the design is substantially different on three axes at once --
unit of comparison (§5.1), DV (§5.2), sampling strategy (§5.5) -- and the autopsy explicitly
refused a `867c`. The convention's own tiebreak is "when in doubt: new letter", but this is not a
doubtful case: a reader who saw `867c` would reasonably expect the screened matched-pair design
with another parameter moved, which is exactly the thing being retired.

**Recommend a new EXQ number**, with `"supersedes"` **omitted** -- 867b is not superseded by this
run, it is a *different* measurement of the same question, and its screen-soundness finding
retains standalone value as the instrumentation record. Assign the number at queue time by
checking the live max in `ree-v3/experiment_queue.json` **and** recent `git log` (CLAUDE.md
Concurrency Rules) -- not from any number written here.

---

## 8. Corrections owed to already-landed artifacts

Governance-owned. Flagged, not applied by this session -- these touch a **confirmed** autopsy's
recorded root cause and `claims.yaml` narrative fields, which is a `/governance` disposition, not
a chip's to make.

1. `evidence/planning/failure_autopsy_2026-08-05_pending_review_batch.{md,json}` section 2 --
   "That is direct evidence the ON-arm manipulation changes decomposition timing/occurrence
   itself" is not supported by the run's data (§2.3, §2.4). The routing it produced is unaffected.
2. `docs/claims/claims.yaml` MECH-321 `evidence_quality_note` (2026-08-04 entry) and
   `what_would_answer` -- same sentence, same correction.
3. `evidence/planning/hypothesis_space_registry.v1.json` `mech321_harm_aware_selection_task_effect`
   -- `decision.observation_bottleneck` and the hypothesis `resolution.basis` carry the same
   inference. **`live_gate` has been updated by this session** (chip-instructed); the other two
   fields are left for governance.

Raised as a `governance_flag.py` `evidence_discrepancy` on MECH-321 so it reaches the next
`/governance` cycle rather than living only in this file.

Separately, the instrumentation gap in §2.5 (`arm_cell` on some cells but not others, invisible to
`agent_construction_before_seed_lint`) is a `ree-v3` lint/tooling item, out of this chip's scope.

---

## 9. Hand-off to `/queue-experiment`

Everything above is design. The next session should run `/queue-experiment` proper -- code review
pass, smoke test, queue entry, ID assignment at write time -- and must **not** copy-and-modify
`v3_exq_867b_...py`, since that file contains the §2.2 defect. The reusable pieces are:

- `experiments/_lib/baselines/sd084_midexec_reachability.py` -- `HAZARD_TUNED_ENV_OVERLAY`,
  `HAZARD_TUNED_STREAM_FLAGS`, `env_kwargs_hazard_tuned`, `substrate_stack_flags`. Unaffected by
  the defect; use as-is.
- 867b's `_build`, `_register_chunk`, `_arm_flags`, `_config_slice`, `_run_cell` bodies -- sound
  in themselves. The defect is in **how `_run_cell` is called** from `_screen_pool`, and
  `_screen_pool` does not exist in this design.
- Per CLAUDE.md, mint the `ARM_SELECTION_OFF` measurement cells reuse-eligible
  (`include_driver_script_in_hash=False`), as 867a/867b did.

Open items a `/queue-experiment` session must settle that this design deliberately does not fix:

- The exact 40-seed candidate list, pre-registered in the driver as a literal tuple.
- Whether `ree_core/**` has moved since 867b (2026-08-04). If it has, the OFF-arm fingerprints
  will not match and no arm reuse is available -- omit `try_reuse_cell` rather than leave it as
  dead code, the call 867a and 867b both made.
- Machine routing: 19 h wants a cloud worker, and per §4 the run is single-threaded-ish like the
  rest of the corpus, so the hub is the right default rather than a larger box.
