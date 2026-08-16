# Failure autopsy -- V3-EXQ-931 + V3-EXQ-932 cluster: wanting SELECTION AUTHORITY vs behavioural COUPLING

**Status:** `awaiting_human_confirmation` (STAGING MODE -- Step 8 interactive gate not run; routing is DRAFT).
**Generated:** 2026-08-16T18:25:45Z
**Scope:** cluster (2 targets)
**Both targets are UNTAGGED** (`claim_ids: []`, `experiment_purpose: "diagnostic"`). GOV-FAILLOC-1's
claim-free branch applies: the Claim-alignment row is `n/a` and the four-layer table below is the only
structured diagnosis. Nothing here is chargeable to a claim, and no `per_claim_recommendation` key
exists to write -- see "Per-claim recommendation" below.

| | Run 1 | Run 2 |
|---|---|---|
| run_id | `v3_exq_931_cem_wanting_weight_selection_authority_20260814T123949Z_v3` | `v3_exq_932_zgoal_wanting_coupling_reinstrument_20260814T155424Z_v3` |
| queue_id | V3-EXQ-931 | V3-EXQ-932 |
| outcome | FAIL | PASS |
| self-route label | `wanting_scoring_lacks_selection_authority_at_operating_weight` | `wanting_behaviour_coupling_detected` |
| machine | ree-cloud-2 (`linux-x86_64-py3.10-torch2.12.0+cpu`) | ree-cloud-2 (same class) |
| substrate_commit | `a57e6dd832` (clean) | `c38e083d59` (clean) |
| elapsed | 1446.7 s | (not stamped) |

---

## 0. Dry-run gate (Step 2a) -- run BEFORE any metric was read

```
scripts/check_dry_run_citations.py v3_exq_931_..._v3 v3_exq_932_..._v3
-- 0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown   (exit 0)
```

Both manifests carry no truthy top-level `dry_run` (931 stamps `dry_run` explicitly false; 932 omits
it). `dry_run_checked: true`, `excluded_dry_run_ids: []`. No cluster member, replicate or population
statistic in this artifact draws on a smoke.

Recording provenance: both manifests carry the always-record core -- `recording_schema: rec/v1`,
`substrate_hash`, `substrate_commit`, `machine` / `machine_class`, full `config`, explicit `seeds`.
931 additionally carries `elapsed_seconds`, `per_arm`, `arm_results` (with per-cell `arm_fingerprint`),
`pre_registered_thresholds`, `enabled_default_off_flags` and `ethics_preflight` (`decision: allow`,
all seven flags false). 932's per-step episode log is committed
(`v3_exq_932_.../..._episode_log.json`, 2.27 MB, 1013 steps). **The recording is adequate in both
cases** -- which matters below, because it is what let this autopsy recompute 932's partial and
per-seed correlations without a re-run. This is the good case of the recording-debt distinction, not
an instance of it.

---

## 1. Facts -- V3-EXQ-931 (FAIL)

### What it manipulated

`REEConfig.hippocampal.wanting_weight`, consumed at
`ree_core/hippocampal/module.py::HippocampalModule._score_trajectory` (the `wanting_weight *
mean(VALENCE_WANTING)` term subtracted from the CEM terrain score). Five arms x five seeds
(42/43/45/46/47), 10 episodes x 40 steps, MECH-293 ghost-probe stack OFF in every arm.

### Primary DV

`selection_flip_rate` = fraction of GENUINE E3 refit ticks at which
`argmin_i(terrain_i - w*wanting_i) != argmin_i(terrain_i)`, computed by counterfactual re-score over
the actual candidate pool, gated on `ticks["e3_tick"]` (so the ~10x cadence-latching inflation of the
2026-08-14 readiness probe is removed; `n_latched_ticks` is reported alongside as the auditable
denominator).

### The dose-response, which is the finding

| arm | wanting_weight | flip rate (mean) | seeds with any flip | wanting_authority_ratio |
|---|---|---|---|---|
| ARM_W0 | 0.0 | 0.0000 | 0/5 | 0.00375 |
| **ARM_W05 (operating)** | **0.5** | **0.0000** | **0/5** | **0.00375** |
| ARM_W50 | 50.0 | 0.0761 | 4/5 | 0.00375 |
| ARM_W500 | 500.0 | 0.3912 | 5/5 | 0.00371 |
| ARM_W5000 (pos. control) | 5000.0 | 0.8025 | 5/5 | 0.00374 |

`wanting_authority_ratio` = `wanting_spread_mean / terrain_spread_mean` ~= **0.0037** in every arm:
the wanting term's spread ACROSS candidates within a scoring tick is ~0.37% of the terrain term's.
That is the mechanism of the null, and it is the V3-EXQ-604c uniform-broadcast hazard by name -- the
term is present and non-constant, but it acts as a near-uniform offset, so it cannot move an argmin
until it is scaled by ~10^2.

### Which criterion failed

`C_AUTH_operating_weight_has_authority` -- a **discrimination** criterion (does the operating-weight
arm choose differently from ablation), `load_bearing: true`, FAILED (`c_auth_seed_fraction: 0.0`
against a 0.6 bar). All four non-load-bearing gates PASSED:

- `P0_ablated_flip_rate_zero` -- structural negative control, 0.0 exactly (arithmetic identity).
- `P1_wanting_field_live` -- 1.0 vs 0.8 floor; worst-arm nonzero-tick fraction 0.87 mean.
- `P2_formation_matched` -- 0.0 vs 0.05 tolerance, episode 1 only, so scoring weight is isolated from
  signal formation.
- `P3_instrument_can_detect_authority` -- **1.0 vs 0.6**: the positive control flipped an argmin in
  5/5 seeds.

**This is what makes 931 a clean, well-powered NEGATIVE rather than a null of unknown power.** The
instrument is positively demonstrated capable on live candidate pools inside this very run, with the
shipped predicate, and the negative control is an arithmetic identity. There is no vacuity here to
adjudicate away.

### The reported, non-gating C_BEHAV -- the second finding, and the more important one

`c_behav_proximity_gap_vs_ablated`: ARM_W05 **0.0**, ARM_W50 **0.0**, ARM_W500 0.00033, ARM_W5000
**0.0**. Per-cell `mean_resource_proximity` is **bit-identical to 16 significant figures** between
ARM_W0 and ARM_W5000 (0.6229773644254133) *while ARM_W5000 flips 80% of argmins*. The manifest's own
`c_behav_note` states this and its reason: E3's own downstream action selection re-scores, so the
flipped hippocampal-CEM pick does not reach the executed action. Verified independently here:
`REEAgent.select_action` (`ree_core/agent.py:5815`) runs E3 selection over the candidate pool using
`self.e3.last_scores`, entirely independently of `_score_trajectory`'s internal elite pick.

*Note on the manifest's line citations:* `c_behav_note` cites `agent.py:11415/11432/11449` for the
re-scoring block; those line numbers do not resolve to it at current HEAD (they land in the SWS-replay
block). Line drift, not a substantive error -- the mechanism is confirmed at `select_action`.

### Two provenance points a reader must not be misled by

1. **Top-level `enabled_default_off_flags` records `hippocampal.wanting_weight: 5000.0`** -- the
   POSITIVE-CONTROL arm's value, not the operating configuration. This is not a driver bug: the
   driver deliberately passes all five arm agents (`agent=list(_ARM_AGENTS.values())`), and
   `experiments/_lib/manifest_core.py::enabled_default_off_flags_for_agents` collapses them
   **last-wins**, a limitation its own docstring states ("Later agents in iteration order win on a
   disagreement -- a known, stated simplification ... not a guarantee of per-arm attribution"). The
   ground truth is fully recoverable from `per_arm[*].wanting_weight`. Consequence: for any
   dose-response driver whose manipulation IS a default-off config field, the top-level block reports
   one arm's value for a field that varies by design. **Legibility defect, not an adjudication
   blocker.**
2. **The shipped default is 0.0, not 0.5.** `HippocampalConfig.wanting_weight: float = 0.0`
   (`ree_core/utils/config.py:2055`), with a docstring reading "Default 0.0 (backward compat). Set
   ~0.3-0.5 for goal-directed navigation". So `ARM_W05` is the *documented recommended* value, not the
   shipped default; several named constructor presets do set 0.5 (config.py:5951, 8591, 8671). **In
   the stock production configuration this pathway is OFF entirely (w=0), i.e. ARM_W0 IS production.**
   The driver's "operating value" language is defensible but should be read as "documented operating
   value", and this distinction belongs in the confirmation gate.

---

## 2. Facts -- V3-EXQ-932 (PASS)

### What it is, and what its PASS actually gates

916a's substrate verbatim (`use_proxy_fields=True`, `tonic_5ht_enabled=True`,
`update_benefit_salience()` wired) with 906c's coupling instrument ported byte-for-byte. 3 seeds
(0/1/2), 50 warmup + 5 eval episodes, 1013 pooled eval steps.

Its `combination_rule` is explicit and honest: **"This gates MEASUREMENT VALIDITY, not coupling
detection"**. All three load-bearing criteria (`residue_wanting_measurable`, `z_goal_measurable`,
`couplings_adequately_powered`) passed; whether any coupling clears the |r| >= 0.15 floor is REPORTED,
never gated. So the PASS says the instrument produced a well-powered measurement -- it does not say a
coupling was found. **The self-route label `wanting_behaviour_coupling_detected` is a hypothesis about
the reported (non-gating) half, and that is the half this autopsy adjudicates.**

### Reported couplings, as the manifest presents them

| coupling | r | rho | n | manifest reading |
|---|---|---|---|---|
| `zgoal_t_to_approach_t1` | +0.0000 | +0.0000 | 998 | near-null |
| `zgoal_t_to_benefit_t1t3` (906c's harm_signal>0 def) | -0.0321 | -0.0324 | 998 | near-null |
| `zgoal_t_to_benefitexp_t1t3` | +0.1801 | +0.1553 | 998 | **NON-TRIVIAL** |
| `wanting_t_to_approach_t1` | +0.0000 | +0.0000 | 998 | near-null |
| `wanting_t_to_benefitexp_t1t3` | +0.1506 | +0.0859 | 998 | **NON-TRIVIAL** |
| `wanting_t_to_moved_t1` | +0.3726 | +0.3433 | 998 | **NON-TRIVIAL** |
| `wanting_t_to_reefexit_t1` | +0.1333 | +0.1263 | 998 | near-null |
| `wanting_zgoal_contemporaneous` | +0.6534 | +0.4939 | 1013 | **NON-TRIVIAL** |

### Autopsy-side re-analysis of the committed episode log (no re-run required)

All figures below were recomputed from
`evidence/experiments/v3_exq_932_zgoal_wanting_coupling_reinstrument/..._episode_log.json` using the
driver's own `_lagged_pairs` definitions. They are an autopsy re-read of already-recorded data, not
new evidence, and nothing in the manifest is edited.

**(a) DV base rates over all 1013 pooled steps.**

```
modes:            shelter 618 | avoid 218 | freeze 176 | explore 1 | approach 0
moved:            True 103 (10.2%)          benefit_exposure>0: 220 (21.7%)
harm_signal>0:    6 (0.59%)                 transition_type reef_exit: 10 (0.99%)
z_goal:           zero on 90.4% of steps    residue_wanting: zero on 0.0% of steps
```

**`approach` mode fires 0 times in 1013 steps.** `_classify_mode` applies affect precedence
(freeze > assert > shelter > avoid > approach > ...) and the regime is harm-saturated:
shelter+avoid+freeze account for 1012 of 1013 steps. So the `approach` indicator has **zero variance**,
and `_pearson_r` / `_spearman_r` return **exactly 0.0** on zero-variance input by design
(documented: "degrade gracefully to (0.0, n) on degenerate input"). The two `*_to_approach_t1`
couplings are therefore **structurally unsettable**, not measured nulls -- yet the manifest's summary
table labels them "near-null" and `criteria_non_degenerate` marks both `_powered: true`. **Power
certifies n; it does not certify variance.** This is the same class of defect as the dry-run
"structurally unsettable criterion" trap the skill warns about, reached by a different route
(mode-precedence saturation rather than episode truncation).

Two further DVs sit at rare-event base rates the n>=200 gate cannot see:
`zgoal_t_to_benefit_t1t3` has **6 positives**, `wanting_t_to_reefexit_t1` has **10**.

**(b) z_goal is identically zero in 2 of 3 seeds.**

```
seed 0  n=595  z_goal mean 0.00000 std 0.000000  nonzero   0 | wanting mean 0.419 std 0.468
seed 1  n=232  z_goal mean 0.00000 std 0.000000  nonzero   0 | wanting mean 0.669 std 0.288
seed 2  n=186  z_goal mean 0.07974 std 0.077996  nonzero  97 | wanting mean 1.307 std 0.568
```

All 97 nonzero z_goal ticks are in **seed 2 alone**. The `z_goal_nondegenerate` precondition measured
`chan_max_std_z_goal = 0.0780` -- which is exactly seed 2's standard deviation, because the predicate
is a **MAX across seeds** (`chan_max_std = {k: max(r["chan_std"]... for r in seed_results)}`, driver
line 1432). **One varying seed of three certifies the channel as non-degenerate while two are
structurally flat.** Consequently:

- `zgoal_t_to_benefitexp_t1t3` (+0.180) is **undefined within seeds 0 and 1** and +0.532 within seed 2.
  The pooled figure is a **between-seed artifact**: seed 2 differs from the others in *both* variables
  (only nonzero z_goal, and the highest wanting mean), so pooling manufactures the association. It
  rests on n=1 seed.
- `wanting_zgoal_contemporaneous` (+0.653) has the same shape: undefined in seeds 0/1, **+0.857 in
  seed 2**.
- Cross-check: the manifest's `z_goal_stream.active_frac` for this run is **0.0087** (97 of 11166
  ticks), consistent with the above.

**(c) Partial correlations against z_goal -- the question the driver never asked.**

The driver computes **no partial correlations anywhere** (verified: no partialling code, all couplings
bivariate), despite reporting `wanting_zgoal_contemporaneous r = 0.65` in the same manifest. Computed
here (pooled, and per seed):

| coupling | pooled r | **partial r \| z_goal** | seed 0 | seed 1 | seed 2 |
|---|---|---|---|---|---|
| `wanting -> moved(t+1)` | +0.3726 | **+0.4317** | +0.4543 | +0.5524 | +0.2823 |
| `wanting -> benefitexp(t+1..3)` | +0.1506 | **+0.0442** | +0.1861 | +0.2590 | +0.2848 |
| `wanting -> reef_exit(t+1)` | +0.1333 | +0.1766 | +0.1849 | +0.3450 | +0.0117 |
| `zgoal -> benefitexp(t+1..3)` | +0.1801 | n/a (x==z) | undefined | undefined | +0.5322 |

Readings, in descending confidence:

1. **`wanting -> moved(t+1)` is ROBUST.** It *strengthens* under partialling on z_goal (0.373 ->
   0.432) and replicates in all three seeds (0.28-0.55) with 103 positives. It is not a z_goal
   common-driver artifact. This is the one coupling that survives every check applied here.
2. **`wanting -> benefit_exposure` is NOT ESTABLISHED.** Its pooled partial on z_goal collapses to
   +0.044, and its Spearman rho (0.086) is already below the pre-registered floor. Note the honest
   complication: every *within-seed* bivariate r (0.19-0.28) exceeds the pooled r, i.e. pooling
   attenuates it -- so the right conclusion is "the pooled estimator is the wrong one here", not
   "the effect is zero". It needs seed-as-factor plus partialling before it can be read either way.
3. **Both z_goal couplings are BETWEEN-SEED ARTIFACTS** resting on a single seed, per (b).
4. **Both approach couplings are VACUOUS**, per (a).

So of the four couplings the manifest flags NON-TRIVIAL, **one survives** (`wanting -> moved`), one is
unestablished, and two are single-seed artifacts.

---

## 3. Claim-layer mapping

Not applicable. Both runs carry `claim_ids: []` by deliberate design, and both docstrings state why:
931's primary DV "measures whether a substrate pathway has selection authority -- an
instrument/admissibility fact, not a hypothesis about the organism"; 932 is observational and
"promotes nothing, weights no governance". Neither run has a claims.yaml entry to strengthen, weaken,
narrow or demote.

Claims the findings are *reported into* (per the drivers' own text) but which this autopsy does **not**
weigh: MECH-236 (`evidence_quality_note`), SD-014, MECH-203 (via the
`mech203-valence-pool-admissibility` substrate item, whose trained-substrate half these runs do not
discharge -- 931 is explicitly its untrained-substrate probe for the wanting half only), and
GFLAG-0033.

---

## 4. Biological-reference triage

**Closest reference mechanism:** mesolimbic incentive salience -- Berridge's wanting/liking
dissociation. The correspondence is close and directly relevant: `VALENCE_WANTING` is written by
`REEAgent.update_benefit_salience()` through a serotonergic benefit-salience transform and consumed as
a scoring bias, which is a recognisable translation of incentive salience as a *motivational* rather
than *hedonic* signal.

**Is it a formal-definition import?** No -- this is a biology-grounded translation, not a Pearl/Shannon
/optimal-control import. The SD-014 substrate entry already cites Smith/Berridge/Aldridge 2011
(incentive sensitization raises wanting without raising liking) as the design basis for the
write-path decouple. So the "formal import with no biology lit" failure mode (SD-003's canonical
28-FAIL cost) does **not** apply here.

**Existing literature:** `evidence/literature/wanting_liking_sleep_consolidation_synthesis.md` and
`targeted_review_hippocampal_dopamine_gain` exist and are adjacent. Neither is a targeted review of
**incentive salience as a SELECTION/effector mechanism** -- the specific question these two runs raise.
Lit status: **partial**, not absent. A `/lit-pull` is therefore *optional and secondary*, not the
autopsy's primary output.

**Does the failure resemble a missing dependency of the reference mechanism?** Yes, and this is the
load-bearing biological read. In mammals, mesolimbic wanting is *not* an epiphenomenal correlate: it
invigorates and directs approach -- it has motivational authority over action selection. What 931+932
jointly describe is a signal with the **correlational signature of incentive salience and none of its
effector coupling**: it tracks the situation and predicts subsequent locomotion, while the pathway by
which it could bias selection is (a) ~270x too weak at the documented operating value, (b) off
entirely at the shipped default, and (c) behaviourally inert even when forced to full authority.
That is the skill's "symbol of the mechanism, not its functional role" precisely. The biology does
**not** say the mechanism is wrong; it says the translation is missing the effector link.

---

## 5. Four-layer diagnosis

### V3-EXQ-931

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | `claim_ids: []` by design (GOV-FAILLOC-1 claim-free branch) |
| Biological reference | **partial** | mesolimbic incentive salience is a clear reference; the failure matches a missing *effector* dependency, not a wrong mechanism. Adjacent lit exists; no targeted review of selection authority |
| Prerequisites | **present** | all five wiring conditions live (`update_residue`, `update_benefit_salience`, tonic_5ht, proxy fields, forced z_goal); P1 and P2 both pass |
| Implementation | **partial** | term exists and is arithmetically correct (P0/P3 prove it), but `wanting_authority_ratio ~= 0.0037` -- ~270x too small to move an argmin at w=0.5; shipped default is 0.0, so the pathway is OFF in production |
| Environment | **partial / too sparse** | NUM_HAZARDS=1 is the *only* probed setting yielding both harm and benefit; early death on 3/5 seeds; contact_rate at this env's foraging competence ceiling; untrained E1/E2 throughout |
| Measurement | **adequate** (C_AUTH) / **under-instrumented** (C_BEHAV) | C_AUTH: argmin-rank DV, arithmetic negative control, in-run empirical positive control at 5/5 seeds, genuine-refit denominator. C_BEHAV: one per-step proximity magnitude at the competence ceiling -- explicitly non-gating and correctly so |
| Integration | **partially coupled** | **the headline.** 80% argmin flips at ARM_W5000 produce bit-identical `mean_resource_proximity` -- the hippocampal CEM elite pick does not reach the executed action; E3 `select_action` re-scores |
| Scale / capacity | **likely insufficient** | 10 x 40 steps, untrained substrate, 429 genuine refit ticks pooled per arm |

**Failure-location summary (GOV-FAILLOC-1):** Implementation reads `partial`, Environment reads
`partial`, Measurement reads `adequate` only for the load-bearing criterion. **REE FAILED is NOT
reached** and must not be written.
**Net classification: MIXED -- MECHANISM + ENVIRONMENT, not chargeable to REE.** The mechanism bucket
is the dominant one (a scoring term ~270x below authority, plus a downstream decoupling at the
CEM->`select_action` seam); the environment bucket contributes (untrained, early-death-limited,
competence-ceilinged). The measures bucket is explicitly NOT established for C_AUTH -- that is what
makes this negative load-bearing rather than vacuous.

### V3-EXQ-932

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | `claim_ids: []` by design |
| Biological reference | **partial** | wanting -> locomotion is the closest real mesolimbic signature the run recovers (invigoration of locomotor output); no targeted review of it |
| Prerequisites | **present (wanting) / missing (z_goal)** | 916a writer fix confirmed live (`residue_wanting` nonzero on 100% of steps, std 0.56). z_goal formation absent in 2/3 seeds under emergent (unforced) conditions |
| Implementation | **partial** | writer path repaired and demonstrably live; z_goal formation is not reliably produced without the forced `update_z_goal` 931 uses |
| Environment | **wrong pressures** | harm-saturated: shelter 618 / avoid 218 / freeze 176 of 1013 steps. This is what makes `approach` unreachable and `harm_signal>0` a 0.6% event |
| Measurement | **under-instrumented / misleading** | (i) two DVs with zero variance reported as "near-null"; (ii) power gate on n only, no variance or base-rate floor; (iii) **no partialling against z_goal** despite reporting r(wanting,z_goal)=0.65 in the same manifest; (iv) pooling across seeds with no seed factor while one seed differs structurally in both variables; (v) `chan_max_std` non-degeneracy is a MAX across seeds, so 1 of 3 certifies |
| Integration | **partially coupled** | wanting tracks locomotion; the causal seam to selection is separately shown absent by 931 |
| Scale / capacity | **adequate (wanting) / insufficient (z_goal)** | 1013 pooled steps and 103 `moved` positives support the surviving coupling; 97 active z_goal ticks in one seed do not support the z_goal reads |

**Failure-location summary (GOV-FAILLOC-1):** **REE FAILED is NOT reached.**
**Net classification: MEASURES (coupling-read validity) + ENVIRONMENT (harm-saturated regime); MIXED,
not chargeable to REE.** Stated precisely, because 932 is a PASS: the **gated** measurement-validity
PASS stands and is correct on its own terms (`residue_wanting` genuinely varies -- the first time in
this lineage). What does not stand is the **reported, non-gating** coupling narrative, of which one
channel survives scrutiny and three do not.

---

## 6. Cluster pattern -- the reconciliation

| Experiment | Question | Absolute / negative-control criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-931 | Does wanting have CAUSAL AUTHORITY over CEM selection? | P0 ablation flip=0.0 PASS; P3 positive control 5/5 seeds PASS | C_AUTH at w=0.5: **0/5 seeds** FAIL | Clean, well-powered NEGATIVE for the scoring pathway |
| V3-EXQ-932 | Does wanting CORRELATE with subsequent behaviour? | preconditions all PASS (measurement validity) | non-gating: 1 of 4 flagged couplings survives partialling + per-seed replication | Genuine wanting -> locomotion coupling; z_goal couplings are single-seed artifacts |

**These are NOT in tension. They compose into one mechanism, and the composition is the finding.**

Three measured facts must hold simultaneously:

1. At the documented operating weight the wanting term never changes the CEM argmin (0/5 seeds), and
   at the *shipped default* (0.0) the pathway is absent entirely.
2. Even when the term is forced to full authority (w=5000, 80% argmin flips), executed behaviour is
   **bit-identical to ablation** -- so the CEM elite pick has no behavioural throughput on this
   substrate at all.
3. `residue_wanting` nonetheless predicts locomotion at t+1 (r=0.373; partial on z_goal +0.432; all
   three seeds).

Fact 2 is decisive for the reconciliation: the correlation in fact 3 **cannot** be flowing through the
pathway ablated in fact 1, because that pathway is shown to have no behavioural throughput even at
10^4x its documented weight. The causal route is affirmatively excluded at two independent points, not
merely unobserved.

**Verdict: `correlation without selection authority` -- the parent's live hypothesis -- is the
best-supported reading.** `residue_wanting` is a real, live, shared UPSTREAM state correlate (built by
the agent's own harm/benefit contact through the residue field), and both it and locomotion are driven
by the same situational variables. It is not a selection input, and on this substrate nothing at the
hippocampal CEM scoring layer is.

The parent's two alternatives, adjudicated explicitly:

- **"932's coupling is confounded by a common driver (e.g. z_goal)."** Directly tested here, since the
  driver never did. **Rejected for the load-bearing coupling** -- `wanting -> moved` *strengthens*
  under partialling on z_goal and replicates within every seed. **Confirmed for the z_goal couplings
  themselves**, which are between-seed artifacts resting on the one seed where z_goal varied at all.
  So the confound hypothesis is right about the wrong channels.
- **"931's operating weight simply sits below the authority threshold."** **True and now quantified**
  (`wanting_authority_ratio` 0.0037; first flips at w~50; 5/5 seeds only at w~500). But it is **not a
  defeater**, because fact 2 shows that buying authority buys argmin flips and nothing else. Raising
  the operating weight would change what the CEM picks and not what the organism does.

**Independent bugs or one structural property?** **One structural property, with a second instance of
an already-registered pattern.** The substrate_queue entry `modulatory-bias-selection-authority`
already records three convergent instances of "scoring-layer signals do not reach the committed
argmax" (MECH-314 curiosity bias, MECH-320 vigor penalty, MECH-341 within-class temperature), plus a
2026-06-10 amendment extending it to "range must be ROUTED into the modulatory bias, not merely exist".
931 is a **fourth instance at a NEW call site one layer upstream** -- inside the hippocampal CEM's own
elite selection -- which is exactly the gap
`failure_autopsy_V3-EXQ-914-914a_2026-08-13` flagged and declined to route ("the implemented E3.select
fix does not reach into the hippocampal CEM's own internal elite-selection/refit step ... flagged for a
future session if this call site recurs"). **It has now recurred, with a dose-response and a positive
control.** 931 also *supersedes* that autopsy's second learning ("the existing lever (wanting_weight)
already covers it"): the lever does not cover it, because the lever's authority does not propagate.

932's defects are a **separate, independent** instrument matter (DV degeneracy, no partialling, MAX-
across-seeds certification) and are not part of the structural property.

---

## 7. Learning extracted

1. **A signal can be live, non-degenerate, and behaviourally predictive while having zero selection
   authority.** Measuring coupling and measuring authority are different experiments, and a PASS on
   the former says nothing about the latter. 931+932 are the worked pair.
2. **Selection authority does not imply behavioural throughput.** ARM_W5000 flips 80% of CEM argmins
   with bit-identical resource proximity. Any future experiment that manipulates a hippocampal-CEM
   scoring knob and reads a behavioural DV will return a structural null that *looks like* a substrate
   or claim finding. This is the single most reusable thing in this cluster.
3. **`wanting_authority_ratio` is the reusable readiness statistic.** ~0.0037 predicts the null
   directly; any scoring-layer lever should report the ratio of its own cross-candidate spread to the
   dominant term's *before* a behavioural falsifier is queued. This generalises the 2026-06-10
   `modulatory-bias-selection-authority` amendment (assert cross-candidate range exists) by one step:
   assert the range is *competitive*, not merely nonzero.
4. **"Powered" is not "non-degenerate".** 932 gates every coupling on `n >= 200` and reports eight
   channels `powered: true`, while two of the eight have a zero-variance DV (`approach`, 0/1013) and
   two more sit at 0.6% / 1.0% base rates. A coupling gate needs a **positive-rate floor on the
   dependent variable**, not just a pair count.
5. **A MAX-across-seeds non-degeneracy predicate lets 1 of N seeds certify a channel.** 932's
   `chan_max_std_z_goal` passed on seed 2 alone while seeds 0 and 1 were identically zero, and every
   pooled z_goal statistic in the manifest inherits that. For a channel that gates a coupling read,
   the predicate should be **min across seeds** (or per-seed reporting with an explicit N-of-M rule).
6. **Report a partial whenever two candidate drivers are measured in the same run.** 932 reports
   r(wanting, z_goal) = 0.65 in the same manifest as the wanting couplings and partials nothing. The
   partials cost nothing here -- they were recomputed from the committed episode log in minutes.
7. **Good recording converted a would-be re-run into a re-analysis.** Because 932 committed a full
   per-step episode log, the partial and per-seed corrections above required no compute. This is the
   Experimental Recording Standard paying off, and it is why 932a should NOT re-run to obtain them.
8. **Multi-arm manifests collapse `enabled_default_off_flags` last-wins.** For a dose-response driver
   whose manipulation IS a default-off field, the top-level block reports one arm's value (931: 5000.0,
   the positive control). Documented, recoverable from `per_arm`, but a live mis-reading hazard.
9. **The shipped `wanting_weight` default is 0.0.** Language like "the operating weight" should be
   read as "the documented recommended weight"; production runs with this pathway absent.

---

## 8. Repair pathway and DRAFT routing (Step 8 gate NOT run -- staging mode)

Node classification per `docs/architecture/work_graph_debt_vocabulary.md`:

- **931 -> `complicated (buildable)`.** The bottleneck is named, single, and has no open question: give
  hippocampal-CEM scoring-layer signals competitive authority *and* a route to the committed action.
  Just build it -- do not queue a spike to reconfirm a dose-response that is already measured.
- **932 -> `complicated (buildable)`** for the instrument fix (the DV redesign and the gate changes are
  all named builds), with one residual **`complex (probe-gated) / puzzle (known rules)`**: under what
  conditions does z_goal form at all in an emergent, unforced regime? 931 forces
  `update_z_goal(0.5, 0.9)` every tick (`active_frac` 0.996); 932 lets it emerge and gets 0.0087, flat
  in 2/3 seeds. That is a missing fact, not a missing build.

### DRAFT routing -- V3-EXQ-931: `implement-substrate`

`recommended_substrate_queue_entry.action = "amend"` on **`modulatory-bias-selection-authority`**
(status `implemented`), adding one `failure_record` item. Amend rather than create: the entry's own
implementation_hint already frames the exact bottleneck ("scoring-layer signals do not reach the
committed argmax") across three prior instances; 931 is the fourth, at a call site the implemented fix
explicitly does not reach. Creating a parallel entry would fragment one bottleneck across two records.

Proposed severity/`substrate_paths` changes are drafted in the JSON and are **a question for the
confirmation gate, not a settled call** -- see "For the human at the gate" below.

**The re-derive brake does NOT fire** (`fired: false`): both targets are claim-free, so the R1-R3
convention has no `targets[].claim_ids` to count and no per-claim ceiling total exists. The routing to
`implement-substrate` is reached on the merits of the structural finding, not by a brake. No
same-claim re-queue is refused, because there is no claim.

### DRAFT routing -- V3-EXQ-932: `queue-experiment` (V3-EXQ-932a, alphabetic suffix)

Same scientific question, broken instrumentation -> lettered iteration per the EXQ versioning policy.
Required changes:

1. **Drop or redefine the `approach` DV.** It is unreachable under this env's affect-precedence chain
   (0/1013). If retained for 906c comparability, it must be reported as `unsettable`, never "near-null".
2. **Add a non-degeneracy gate on every DV** -- a positive-rate floor (e.g. `>= 5%` and `>= 20`
   positives), alongside the existing pair-count floor. `zgoal_t_to_benefit_t1t3` (6 positives) and
   `wanting_t_to_reefexit_t1` (10) fail any such floor today.
3. **Change `z_goal` non-degeneracy from MAX-across-seeds to per-seed**, and report per-seed couplings
   plus a within-seed pooled estimate beside every pooled figure.
4. **Report partial correlations against z_goal** for every wanting coupling, and vice versa.
5. **Address the z_goal regime**: either adopt 931's forced-formation configuration (making the z_goal
   half comparable to 931 and to 906c) or declare the emergent-regime question as the separate spike.

**Do NOT re-run to obtain items 3 and 4** -- they are already recoverable from the committed episode
log, as demonstrated in Section 2(c). 932a's compute is justified by items 1, 2 and 5 only.

### Draft `evidence_quality_note` texts (for governance to write -- NOT written here)

**V3-EXQ-931:**
> Claim-free diagnostic (`claim_ids: []`); weights no claim. Clean, well-powered NEGATIVE for the
> hippocampal-CEM wanting scoring pathway: `selection_flip_rate = 0.0` in 5/5 seeds at the documented
> operating weight (0.5), with the in-run positive control (w=5000) flipping an argmin in 5/5 seeds and
> the ablation arm at exactly 0.0 -- so the instrument is demonstrated capable and the null is not
> vacuous. Mechanism: `wanting_authority_ratio ~= 0.0037` (the wanting term's cross-candidate spread is
> ~0.37% of the terrain term's), the V3-EXQ-604c uniform-broadcast hazard; first flips appear at w~50.
> Second, stronger finding (reported, non-gating): at w=5000 the CEM argmin flips on 80% of genuine
> refits while `mean_resource_proximity` stays bit-identical to ablation, so the hippocampal CEM elite
> pick has no behavioural throughput -- `REEAgent.select_action` re-scores downstream. Fourth
> convergent instance of the `modulatory-bias-selection-authority` bottleneck, at a call site one layer
> upstream of E3.select that the implemented fix does not reach (predicted by
> `failure_autopsy_V3-EXQ-914-914a_2026-08-13`, which this run supersedes on the point that
> "wanting_weight already covers it"). Failure-location: MIXED (MECHANISM+ENVIRONMENT), not chargeable
> to REE. Note the shipped `HippocampalConfig.wanting_weight` default is 0.0, so ARM_W0 is the
> production configuration and ARM_W05 is the documented recommended value.

**V3-EXQ-932:**
> Claim-free observational diagnostic (`claim_ids: []`); weights no claim. Its PASS gates MEASUREMENT
> VALIDITY only, by the driver's own combination_rule, and that PASS stands: `residue_wanting` is
> genuinely live for the first time in the 906/916 lineage (nonzero on 100% of 1013 steps, std 0.56),
> confirming the V3-EXQ-916a writer fix. The reported, non-gating coupling narrative does NOT stand in
> full. Of the four couplings flagged non-trivial, only `wanting -> moved(t+1)` survives autopsy
> re-analysis of the committed episode log: r=+0.373, partial r|z_goal = **+0.432** (it strengthens),
> replicated in all 3 seeds (0.28/0.55/0.28). `wanting -> benefit_exposure` collapses under partialling
> (+0.151 -> +0.044) and its Spearman was already below the pre-registered floor. Both z_goal couplings
> (`zgoal -> benefitexp` +0.180, `wanting <-> zgoal` +0.653) are BETWEEN-SEED artifacts: z_goal is
> identically zero in seeds 0 and 1 (all 97 active ticks in seed 2), and the `chan_max_std`
> non-degeneracy predicate is a MAX across seeds, so one seed certified the channel. Both
> `*_to_approach_t1` couplings are STRUCTURALLY UNSETTABLE, not near-null: `approach` mode fires 0/1013
> times under a harm-saturated affect-precedence chain (shelter 618 / avoid 218 / freeze 176), and the
> estimator returns exactly 0.0 on zero-variance input -- their `powered: true` flag certifies n, not
> variance. Failure-location: MEASURES (coupling-read validity) + ENVIRONMENT, MIXED, not chargeable to
> REE. Re-instrument as V3-EXQ-932a; items 3-4 of that spec need no re-run.

### Per-claim recommendation

**There is no claim to key a `per_claim_recommendation` on.** Both targets carry `claim_ids: []`, so
the field is set to `{}` in the JSON, deliberately and explicitly, rather than inventing a key. This is
stated here so a later reader (and GOV-APPLY-1, which can read only that field) can distinguish "no
claim exists" from "the producer forgot". Governance should apply the two `evidence_quality_note`
drafts above to the **manifests**, not to any claim.

### Granularity-debt recurrence trigger

**Does not fire.** `granularity_debt_cluster.py` counts autopsy TARGETS whose own `targets[].claim_ids`
name a claim; both targets here name none, so no claim's cluster count moves and no
`claim_alignment: weakened` reading exists to contribute. Not run for a claim id, because there is no
candidate id to run it for.

### Fan-out (GOV-FANOUT-1) -- DRAFTED, NOT REGISTERED

The remaining open question **is** a discrimination, not a single build: *if wanting has no selection
authority and the CEM pick has no behavioural throughput, why does wanting predict locomotion?* Three
live hypotheses on different design axes are drafted in the JSON's `fanout_recommendation`, and the
intended pre-registration is held in `hypothesis_space_ledger_pending` (Step 9b is drafted-only in
staging mode; **no `hypothesis_space_*` file was read for write or modified**).

The cheapest decisive leg is worth naming here: **931's own arm structure already contains the
discriminator it did not measure.** Running 932's coupling instrument inside 931's ARM_W0 vs ARM_W5000
contrast tests whether `wanting -> moved` is identical with the scoring pathway ablated and with it at
full authority. If identical, the CEM route is excluded directly and only the shared-situation and
reverse-causation hypotheses remain.

---

## 9. For the human at the confirmation gate

1. **Severity stamp on the substrate amendment is a real decision, not bookkeeping.** This autopsy
   drafts `severity: "corrupting"` for `modulatory-bias-selection-authority`, on the ground that a
   behavioural DV downstream of a hippocampal-CEM scoring manipulation returns a *structural* null that
   reads as a substrate or claim finding -- which is what invalidated V3-EXQ-914/914a. But `severity:
   corrupting` arms the `/queue-experiment` Step 2.5c **block** on `substrate_paths`, and these are hot
   paths. The draft scopes them narrowly (`module.py::_score_trajectory`, `agent.py::select_action`)
   to bound the blast radius. **Confirm `corrupting`, or downgrade to `degrading` (WARN not BLOCK), at
   the gate.**
2. **"Operating weight" vs shipped default.** Should 931's finding be recorded as "no authority at the
   documented operating weight (0.5)" or, more strongly, as "the pathway is absent in the stock
   configuration (default 0.0) *and* has no authority at the documented value"? The second is what the
   config actually says. This affects how MECH-236's note is worded.
3. **Is `wanting -> moved` worth a claim?** It is the only coupling here that survives partialling and
   per-seed replication, and it has a clear mesolimbic reference (incentive salience invigorating
   locomotor output). It currently attaches to nothing. A new Q-claim or an SD-014 child may be
   warranted -- but that is a `/claim-synthesis` judgement, not this autopsy's to make.
4. **Whether to commission a `/lit-pull`.** Adjacent literature exists
   (`wanting_liking_sleep_consolidation_synthesis.md`, `targeted_review_hippocampal_dopamine_gain`),
   so lit status is `partial`, not `absent`, and no divergence-from-a-formal-import is in play. A
   targeted review of *incentive salience as a selection/effector mechanism* would be genuinely useful
   for the substrate build, but it is secondary to it and this autopsy does not route it.
5. **Nothing here is chargeable to REE.** Both targets are MIXED under GOV-FAILLOC-1. If any of this
   is summarised onward, it must not be paraphrased as "wanting does not work in REE" -- the accurate
   statement is that the wanting signal is live and behaviourally predictive, and the *scoring pathway
   that would give it authority* is sub-threshold, off by default, and behaviourally disconnected.

---

*Staging-mode artifact. Steps 1-7 and 9 complete; Step 8 (interactive gate) deferred; Step 9b drafted
into `hypothesis_space_ledger_pending` and NOT applied; Step 10 (claim close / land) not run -- the
parent session commits. No claims.yaml, manifest, review_tracker.json, substrate_queue.json,
pending_review.md or experiment index was read for write or modified by this session.*
