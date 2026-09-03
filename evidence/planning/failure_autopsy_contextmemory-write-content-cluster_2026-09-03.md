# Failure autopsy -- ContextMemory write-content discrimination portfolio (V3-EXQ-969 / 970 / 971 / 972)

- **Generated (UTC):** 2026-09-03T04:15:52Z
- **Scope:** cluster (4 targets)
- **Status:** confirmed (user, interactive Step 8 gate, 2026-09-03T05:04:52Z)
- **Session:** autopsy-20260903-fails-diagnostics
- **Ledger question:** `contextmemory_write_content_discrimination` (registered 2026-08-29 by `failure_autopsy_V3-EXQ-956_2026-08-29`)
- **Substrate entry:** `contextmemory-write-path-addressing-degeneracy` (`implemented_pending_validation`, severity `corrupting`, priority 1)

## 0. One-paragraph summary

These four runs are the complete H1-H4 fan-out portfolio the V3-EXQ-956 autopsy opened, and they all
returned on 2026-09-02. **None of the four adjudicated its leg.** Three returned FAILs that are gate
artifacts rather than nulls, and the fourth returned a PASS its own driver says must not be read as a
scientific verdict. The common cause is not four independent bugs: it is one mis-posed instrument --
the 2-cluster occupied-set Jaccard -- used unchanged by every leg, against a directive dated four days
earlier not to build against it. The one genuinely load-bearing measurement in the portfolio is H4's,
and it points upstream of everything the other three tested.

> **This artifact was materially revised after an adversarial red-team pass.** Two claims in the first
> draft are **withdrawn on measurement**: that H1 demonstrated the objective family is *capable* (it is a
> trained-set readout; the generalization readout is flat), and that a ~10x training-budget shortfall was
> a shared cause (the realised schedule is the lineage's normal one). A third is **inverted**: H2's
> baseline mismatch is *conservative* for its null, not destructive of it. Section 10 records the full
> disposition; the withdrawn arguments are kept rather than deleted, because an argument that was tested
> and dropped is a signal to the next session.

## 1. Facts reconstruction

### 1.1 Dry-run gate (Step 2a)

`check_dry_run_citations.py` over all four run_ids: **0 dry cited, 0 dry in named families, 0
ambiguous, 4 clean, 0 unknown** (exit 0). `dry_run` is not a manifest key in any of the four, and no
`DRY_RUN_UNREACHABLE_CRITERION_EXEMPT` appears in any driver. No run is excluded from any statistic
below.

### 1.2 Recording provenance

`validate_recording.py` returns OK on all four -- 0 always-core gaps, 0 provenance drops, exit 0.
Every manifest carries `recording_schema`, `substrate_hash`, `substrate_commit`, `machine_class`,
`elapsed_seconds`, full `config` and explicit `seeds`. **There is no recording debt in this cluster**;
the defects below are design defects, not omissions.

### 1.3 The four legs

| Leg | Run | Status | Self-route label |
|---|---|---|---|
| H1 loss-objective mismatch | V3-EXQ-970 | FAIL | `h1_content_referencing_objective_not_confirmed_either_regime` |
| H2 operating point | V3-EXQ-969 | FAIL | `h2_no_operating_point_improves_content_discrimination_null_holds` |
| H3 task-pressure required | V3-EXQ-971 | FAIL | `h3_task_coupled_objective_fails_margin_null_confirmed` |
| H4 input distribution | V3-EXQ-972 | PASS | `h4_supported_representation_undifferentiated` |

All four carry `claim_ids: []` and `experiment_purpose: "diagnostic"`.

## 2. What actually went wrong, leg by leg

### 2.1 H1 (V3-EXQ-970) -- the strongest positive in the portfolio, discarded by an unclearable gate

Two regimes were run so that a positive could not be confounded with H4.

**Regime A (real agent latents) never produced its DV.** `probe_heldout_real_latent_jaccard` is
`null` in **12 of 12** cells, with `probe_heldout_insufficient: true` and `n_heldout_dangerous: 0`
in all 12. The held-out split is gated on `len(states_dangerous) > N_HELDOUT + MIN_H1_BUF` =
`200 + 8` = **209**; the observed dangerous-state counts across all 12 cells are 171, 174, 176, 176,
181, 182, 183, 186, 189, 191, 194, 195 -- **maximum 195**. The gate is unreachable at this schedule
in every possible world, not merely unmet on this run. The consequence chain is visible in the
manifest: DV null -> `mean_..._regime_a = NaN` -> `untrained_baseline_headroom met: false` ->
`red_arms: ["Regime_A"]`, `n_paired_seeds_regime_a: 0`, `p_value_regime_a: NaN`. Since the
load-bearing criterion is an OR across regimes, it collapsed to a single-regime test.

**Regime B (synthetic 2-cluster stream) hit the DV's best possible value on the data it trained on --
and generalized not at all.** The trained arm returned
`probe_2cluster_jaccard_trained_clusters = [0.0]*6` -- perfect separation on 6/6 seeds -- and this is the
number that must not be over-read. That readout evaluates on **the exact bases the arm trained on**
(fresh noise draws, same cluster identity). The portfolio's own **generalization** readout, on a fresh
cluster pair from the same generative family, is flat:

| readout | untrained | trained |
|---|---|---|
| `mean_probe_2cluster_jaccard_trained_clusters_regime_b` | 0.5833 | **0.0** |
| `mean_probe_2cluster_jaccard_fresh_clusters_regime_b` | 0.4166666666666667 | **0.4166666666666667** |

Identical to full float precision. Regime B is a bare `write_addr_tagger` MLP -- no environment, no
agent, no `write()` during training -- run for 15,000 Adam steps on two fixed centroids, with
`final_h1_loss = -2.0` on 6/6, i.e. saturated at the L1 divergence maximum. **That is memorisation of two
points with zero transfer, not a demonstration of content-conditioning capability.** (It is not
degenerate slot-collapse either -- every trained cell routes the two clusters to two *distinct* singleton
slots; collapse would read J = 1.0. But the untrained tagger already produces J = 0.0 on 2 of 6 seeds by
initialisation alone, so "two clusters -> two slots" is the weakest capability demonstration this DV
admits.)

**The gate defect is real and independent of that.** The untrained baseline was `[0.5, 1.0, 1.0, 0.0, 0.0, 1.0]`, so the paired diffs are
`[0.5, 1.0, 1.0, 0.0, 0.0, 1.0]`: **two of six pairs are exactly zero**. A zero-magnitude pair
contributes nothing under sign-flip, so the attainable exact p-grid is multiples of `1/2**4`, whose
floor is **0.0625** -- against `alpha_corrected = 0.025`. Recomputed independently in this session:
`2**-4 = 0.0625` one-sided, and the manifest's reported `p_value_regime_b` is exactly 0.0625, i.e.
the floor. **No outcome at this untrained baseline could have cleared the gate.**

The driver's own red-team pass identified this shape at n=5 and believed it fixed by moving to n=6
(`"n=6 lowers the floor to 1/2**6 = 0.015625 < 0.025, restoring genuine two-sided discriminability"`).
That figure holds only with **zero tied pairs**, and the tie count is a property of the untrained
baseline, which is not under the experimenter's control and was not addressed by the fix.

Two further observations: `final_h1_loss` sits on its analytic bound (`-2.0` to 7+ significant
figures; the objective is `-L1` between two probability vectors, bounded above by 2), and
`mean_probe_2cluster_jaccard_fresh_clusters` is bit-identical between the untrained and trained
Regime B arms (`0.4166666666666667` both) while the trained-clusters readout moved 0.583 -> 0.0.

**Reading: H1 was not adjudicated, and it produced no evidence of capability.** The self-route's
"not confirmed in either regime" is accurate in outcome though not in reasoning -- the gate was
unclearable, *and* the underlying generalization result would not have supported the leg anyway. H1
remains formally **alive** only because Regime A -- the real-latent regime that would actually have
tested it -- never ran.

### 2.2 H2 (V3-EXQ-969) -- a pinned instrument and a cross-seed-set baseline

The gating criterion was attainable in principle: the readiness precondition passed (pooled untrained
baseline 0.85 against a 0.25 floor), and an all-correct Phase A sign test at n=10 would return
two-sided p = 0.00195 against `alpha_corrected = 0.0125` (recomputed independently this session). So
this leg failed on data, not on an unreachable bar. But the data cannot bear the reading:

- **Phase B has no untrained arm at its own seeds.** Its six configs (seeds 42,7,13,100,200,300) are
  graded against Phase A's disjoint 10-seed pool (seeds 11,23,31,47,53,61,79,83,97,101, mean 0.85).
  The same instrument on the Phase-B seed family reads 0.400 (V3-EXQ-956, V3-EXQ-971) and 0.4167
  (V3-EXQ-970). The untrained tagger never receives gradient and the probe runs post-training in
  `eval()` on a synthetic stream, so the untrained DV is a function of the random init -- i.e. of the
  seed -- and not of the training arm. The reported deltas (+0.150 / +0.067 / +0.067 / +0.039) are
  therefore cross-seed-set; against a seed-matched ~0.4167 the same trained means would give roughly
  +0.583 / +0.500 / +0.500 / +0.472. Same sign, magnitudes differing by ~4-12x.
- **Phase A's paired test is pinned.** `n_seeds_tied: 8` of 10, all at delta 0 with both arms at
  J = 1.0 (the DV's worst value); `n_seeds_wrong_direction: 2`; `n_seeds_correct_direction: 0`. The
  paired sign-flip p-value is **1.0**, the maximum the test can return. The two seeds that did move
  both moved the wrong way, which is consistent with V3-EXQ-956's own +0.267 wrong-direction move and
  is the one weakly informative signal here -- but at 0 correct of 10 it cannot be separated from the
  instrument being pinned.
- **The DV cannot resolve gain.** `w=0.1` and `w=2.0` -- 20x apart -- produced bit-identical per-seed
  DV vectors (`[1.0, 0.5, 1.0, 1.0, 1.0, 1.0]`) and identical occupied sets cell-for-cell. `w=8.0`
  (80x from the lowest) differs on exactly one seed.

**Reading: the null's DIRECTION is well-supported; its universality is not.** Correcting the baseline
to be seed-matched makes the null *stronger*, not weaker: every tested operating point's **mean** moved
Jaccard the wrong way by roughly 0.5 (W0P1 -0.500, W2P0 -0.500, W8P0 -0.472; one-sided sign-flip p(drop)
0.969 / 0.969 / 0.938), 7-12x larger than the cross-seed-set comparison reported and in the same
direction. Phase A agrees, with 0 of 10 seeds improving. So the baseline mismatch was **conservative**
for H2's null.

**Stated precisely, because the mean hides a dissent** (and the 7b C6 check caught an earlier draft
over-claiming here): per seed the split is identical across all three weights -- 4 of 6 seeds worse
(42, 100, 200 by 1.0; 300 by 0.5), 1 tied (13), and **seed 7 BETTER by 0.5** (0.667 at w=8.0). Seed 7 is
the only cell in the leg that improved, and it improved under every weight. The claim is therefore about
means and about 4 of 6 seeds, not about every seed. What the instrument cannot license is the universal claim: 8/10 Phase A seeds sat pinned
at the DV's worst value and 20x-apart gains were indistinguishable, so "none of these four operating
points helped, and all four hurt" is earned, while "no operating point could help" is not. **H2 stays
alive on that residual, not on any positive signal, and it is the closest of the four to elimination.**

### 2.3 H3 (V3-EXQ-971) -- graded by a test its own siblings rejected, on an objective that did not train

Two independent problems, either of which alone voids the null:

- **The grading criterion.** H3's load-bearing criterion is a bare mean-margin comparison at n=5 with
  no permutation test and no multiplicity correction (`grep -n "permutation\|alpha_corrected"` returns
  0 hits in the driver). Both sibling drivers demote exactly this reading on exactly this DV, in their
  own docstrings: V3-EXQ-969 measures a **25-68%** false-positive rate under the null and demotes it
  to `raw_margin_reading`; V3-EXQ-970 measures **~15%** and demotes it to
  `H1_bare_margin_reading_non_gating`. H3 uses it as its gate. This is a portfolio-level
  inconsistency that a design audit should have caught before queueing.
- **The objective did not train.** `h3_loss_mean_first_episode_trained = 0.6273` ->
  `h3_loss_mean_last_episode_trained = 0.6514` -- the coupling loss **rose** across training, while
  the untrained arm fell slightly (0.6675 -> 0.6641). A mechanism that was not instantiated cannot
  supply a null.

Separately, the trained arm's write behaviour **collapsed toward the single-slot regime the substrate
entry exists to prevent**: entropy 3.96-3.98 -> 0.785-1.484 bits, `self_repeat_rate` 0.059-0.064 ->
0.714-0.882, with `probe_2cluster_jaccard` pinned at 1.0 on 5/5 seeds. `n_occupied_slots` stayed
16/16 in both arms, so the collapse is in the policy, not the slot inventory.

**Reading: `h3_..._null_confirmed` is not supportable.** The leg stays alive.

### 2.4 H4 (V3-EXQ-972) -- the one load-bearing measurement, and its PASS is not a verdict

The PASS token here is a measurement-validity gate. The manifest's own criterion says, verbatim,
*"This is a MEASUREMENT criterion, not a pass/fail on a scientific direction"*, and the driver adds
*"do not read `passed: true` here as 'H4 refuted' or `passed: false` as 'H4 supported'"*. The
`h4_supported` half of the self-route label comes from the explicitly non-gating `h4_reading`, which
compares 0.0281 against a floor the manifest itself calls *"a conservative noise floor for a
cosine-similarity statistic, not a rigorously derived value"*.

The measurement itself is substantive and first-of-kind in this lineage:

| statistic | per-seed | mean |
|---|---|---|
| intra-class cosine, safe | 0.9818, 0.9785, 0.9792, 0.9814, 0.9811 | **0.9804** |
| intra-class cosine, dangerous | 0.9713, 0.9720, 0.9671, 0.9731, 0.9728 | **0.9713** |
| inter-class cosine | 0.9489, 0.9421, 0.9506, 0.9472, 0.9500 | **0.9478** |
| separability score | 0.0277, 0.0331, 0.0225, 0.0301, 0.0269 | **0.0281** |

Train-time write-stream latents sit in a narrow cone, and safe and dangerous states are very nearly
collinear within it under this statistic. This is the SD-008 under-differentiation cone, measured at
*training time* for the first time in this lineage -- the exact observation H4's pre-registration said
was un-instrumented.

**Hedge, and it matters for how far this can be pushed:** `separability_score` is an **uncentred** cosine
contrast, which is insensitive to structure a learned projection could still exploit (a large common mean
dominates all three cosines). It supports *"the classes are not linearly separated in the raw write
stream"*; it does **not** support the stronger *"there is no structure for any objective to condition
on"*. The cheap confirmer for the stronger claim is a held-out linear probe (logistic regression,
safe-vs-dangerous) on the same recorded latents.

The leg's non-gating cross-reference probe reproduces V3-EXQ-956 **cell-for-cell and set-for-set**
(J = [1.0, 0.5, 0.3333, 0.5, 1.0], mean 0.667; occupied sets `{4}|{4}`, `{6,10}|{10}`, `{7}|{2,7,8}`,
`{0}|{0,2}`, `{9}|{9}`), which is a useful instrument-stability result across drivers.

**Reading: the direction is well-evidenced; the threshold crossing is not, and the leg has no
comparator arm.** H4 stays alive but is now the best-supported of the four.

## 3. The cluster shape -- one structural property, not four bugs

### 3.1 The instrument

The 2-cluster occupied-set Jaccard DV (`PROBE_CLUSTERS = 2`, `PROBE_JITTER = 0.0078`, `PROBE_N = 1500`,
`LATENT_DIM = 64`, margin 0.25, n = 5/6/10) is **near-binary**. Portfolio-wide, **72 of 89 cells** carrying
`probe_2cluster_occupied` have both clusters' occupied set at cardinality 1, so Jaccard can only be 0.0 or
1.0. (Restricted to the 53 cells in 969/971/972 the figure is 45/53 with histogram
`{0.0: 4, 0.333: 2, 0.5: 5, 1.0: 42}`; the 89-cell denominator, which includes 970's 36 cells, is the
honest one and gives the same conclusion.)

Everything above follows from this one property:

| leg | how the near-binary DV bit |
|---|---|
| H2 | 8/10 seeds tied at delta 0 -> paired p = 1.0, the test's maximum |
| H1 | 2/6 tied pairs -> exact p-grid floor 0.0625 > alpha 0.025 |
| H3 | a bare mean-margin test on a near-binary DV at n=5 (25-68% / ~15% measured FPR) |
| H2 | 20x-apart gain settings indistinguishable |

### 3.2 The directive that was already on the record

The substrate entry `contextmemory-write-path-addressing-degeneracy`'s own `implementation_hint`,
amended **2026-08-29** -- four days before these runs -- says, verbatim:

> "FINDING: the C2 instrument itself is mis-posed, not merely hard to satisfy -- the 2-cluster
> occupied-SET Jaccard at n=5 seeds with tiny within-cluster jitter (0.0078) collapses to a
> near-binary, aliasing-prone statistic ... An untrained, unlearned tagger passes the bar ~8% of the
> time by chance alone. **DO NOT build a third loss design against C2 as currently written.** ...
> redesign the instrument -- e.g. mutual information over the contingency table, not set-Jaccard --
> before treating content-discrimination as a standalone gate."

All four legs use the unchanged instrument. **Two of them (H1/970 and H3/971) are new loss designs
graded against it** -- the class the directive names. H2 and H4 are not loss designs. No
mutual-information statistic, no K >= 4 cluster extension, and no per-draw contingency table appears in
any of the four drivers or manifests.

**How this was resolved (user decision, 2026-09-03).** The directive is dated 2026-08-29, and
**governance itself routed this H1-H4 portfolio on 2026-08-30**, the day after. Put to the user at the
Step 8 gate, the decision was that **the later routing supersedes** and the directive is overridden. The
directive is therefore quoted here as the origin of the instrument finding -- which the portfolio's own
data independently confirm -- and **not** as a standing prohibition. No refusal is recorded (section 5).

### 3.3 The budget -- an argument this autopsy tested and WITHDREW

An earlier draft named a "~10x under-run training budget" as a second shared cause. **Withdrawn on
measurement.** The realised step counts equal the lineage precedent seed-for-seed:

| | seeds 42, 7, 13, 100, 200 |
|---|---|
| V3-EXQ-956 `n_write_calls_per_seed_GUMBEL_UNTRAINED` | [1546, 1460, 1478, 1576, 1446] |
| V3-EXQ-970 `n_write_calls_per_seed_regime_a` (untrained) | [1546, 1460, 1478, 1576, 1446, 1321] |

Identical on all five shared seeds. The gap to the nominal 15,000 is the harness's ordinary
early-termination schedule -- episodes break on `done`, and dangerous episodes end at about 3.8 steps
(191 dangerous states over 50 dangerous episodes) against ~27 for safe ones. That is an **environment**
property, and it is precisely the schedule the substrate entry registered as *"a real training
schedule"*. So under-training cannot explain any difference from V3-EXQ-956, and the four legs are not
graded `implementation: partial` on this basis.

The observation is not useless: it is exactly why 970's `N_HELDOUT = 200` gate was unreachable against
~180 realised dangerous states. It is recorded here as a tested-and-dropped argument rather than deleted,
so a later session does not re-derive it.

### 3.4 Is it N bugs or one property?

**One property.** The four legs differ in mechanism (objective class, gain, task coupling, input
distribution) and in failure signature (uncomputable DV, unclearable p-floor, pinned paired test,
rejected criterion), yet every comparative conclusion in the portfolio traces back to the same
near-binary DV. That is the load-bearing signal: a convergent limitation across four structurally
different mechanisms. (The budget is *not* a second shared cause -- section 3.3.)

### 3.5 The convergent read -- stated as a hypothesis, not a finding

**Three of the four legs point away from "a better write-side objective fixes this", and the fourth
measures an input stream with little exploitable structure.**

- **H2:** every tested operating point moved Jaccard the *wrong* way by ~0.5 seed-matched; 0 of 10 Phase A
  seeds improved.
- **H3:** the coupled objective did not train (loss rose 0.6273 -> 0.6514) and its arm collapsed toward
  the single-slot regime.
- **H1:** no *transferable* capability even on a synthetic stream engineered to carry content structure --
  trained-cluster Jaccard 0.0 but fresh-cluster Jaccard 0.4167, identical to untrained.
- **H4:** real train-time latents at separability 0.0281.

The leading hypothesis is that the binding constraint sits **upstream of the addressing policy**, in the
write stream's representation.

**Three limits, stated because an earlier draft of this autopsy overstated exactly here.** (1) H1's
synthetic result is memorisation of two centroids with zero generalization; the claim that it shows the
objective family is *capable* is **withdrawn**. (2) H4's statistic is an uncentred cosine contrast and
cannot distinguish "no structure" from "structure off the raw axis". (3) The near-binary DV limits all
three comparative legs. **This is the hypothesis the redesigned instrument should be built to test, not a
finding to apply** -- and per section 9 the upstream lever itself belongs to SD-070, not to this entry.

## 4. Failure-location summary (GOV-FAILLOC-1)

All four targets are claim-free (`claim_ids: []`), so this is the claim-free form of the rule.

| bucket | 969 | 970 | 971 | 972 |
|---|---|---|---|---|
| MECHANISM | not established | not established | not established | not established |
| MEASURES | not established | not established | not established | **established** |
| ENVIRONMENT | established | established | established | established |
| **REE FAILED** | **no** | **no** | **no** | **no** |

**Net: MEASURES-dominant across the cluster; REE is not engaged.** The REE bucket cannot be reached on
any of the four, because MEASURES fails on three and the fourth has no comparative arm at all. Note that
`implementation` is graded **complete for the schedule this lineage uses** on 969/970/971 -- the earlier
`partial` grading rested on the withdrawn budget argument (section 3.3). 971 is the one leg with a genuine
implementation problem, and it is specific rather than budgetary: its objective did not converge.

Nothing in this portfolio is evidence that REE failed to do anything; the mechanisms were not fairly
tested. 972 is the exception in kind rather than degree -- not a failure at all, but an informative
measurement.

## 5. Repair pathway

**Node classification:** `complicated (buildable)`. The fix is a named build with no open question --
the substrate entry already specifies it. This is not `complex (probe-gated)`: no further spike is
needed to know what to do.

**Routing: `implement-substrate`**, amending `contextmemory-write-path-addressing-degeneracy`.

**Re-derive brake: count met, brake does NOT fire, NO re-queue refused -- by user decision.** The count
is past threshold: the substrate entry holds open failure records for V3-EXQ-943, V3-EXQ-956 and
V3-EXQ-436g, and by the R1-R3 counter the claims it unblocks stand at **SD-017: 12**, **ARC-045: 4**,
**MECH-166: 4** prior confirmed ceiling-hit targets. (These four targets carry `claim_ids: []`, so the
claim-keyed counter returns 0 for them directly.)

An earlier draft of this artifact **refused** a further write-side loss design, on the strength of the
substrate entry's 2026-08-29 directive. **That refusal is withdrawn.** At this autopsy's Step 8 gate
(2026-09-03) the user was shown that the directive predates the portfolio by four days while governance
itself routed the H1-H4 portfolio on 2026-08-30, the day after, and directed that **the later routing
supersedes** -- so the directive is read as overridden and no refusal is recorded.

**What that does not change.** The instrument finding rests on measurement, not on the directive: 72 of
89 portfolio cells can only return Jaccard 0.0 or 1.0; 969 Phase A's paired test returned its maximum
p of 1.0 with 8 of 10 seeds tied; and 970 Regime B's attainable p-floor (0.0625) exceeds its own alpha
(0.025). **The instrument redesign remains this autopsy's recommended routing on the evidence.** A future
session is free to queue another loss design against the unchanged instrument, but should read section
3.1 first and expect the same resolution limits.

**No fan-out recommendation is emitted.** The bottleneck routes to one unambiguous build. Fanning out
again before the instrument can resolve graded change would reproduce this portfolio.

**The upstream lever is declared, not absorbed.** H4's measurement makes the input-distribution route the
leading hypothesis, and this entry's *own* `implementation_hint` already says that lever is
*"Secondary/complementary lever (NOT this entry): raise z_world entropy via the SD-070 encoder recipe"*.
The amend therefore carries a non-empty `depends_on_unresolved` naming SD-070. Filing an
input-distribution finding here with an empty gate list is the undeclared-gate pattern GFLAG-0114 flagged
on 2026-09-02, and the red-team caught this artifact doing exactly that.

### Granularity-debt recurrence trigger: **does NOT fire from this autopsy**

`granularity_debt_cluster.py` counts targets whose own `claim_ids` name a claim. All four targets here
are claim-free, so they contribute **0 tagging targets** and this autopsy adds nothing to any cluster.

Reported for governance, not as this autopsy's routing: the **standing** SD-017 cluster independently
sits at 17 targets across 10 files (ARC-045 and MECH-166 at 9 each), with a mixed alignment
distribution that does include `weakened` readings, and **no `claim_synthesis_SD-017*` artifact
exists**. On inspection, however, that cluster's distribution is dominated by measurement and
substrate-debt readings (`measurement_gap`, `precondition_unmet`, "total upstream confound"), which is
the same diagnosis this autopsy reaches. **The recurrence is instrument debt, not granularity debt** --
the claims are not coarse, the instrument is mis-posed -- so this autopsy does **not** recommend
`/claim-synthesis`, and records the reasoning so a later session need not re-derive it.

## 6. Residual risks this autopsy is NOT resolving

1. **Could Regime B's J = 0.0 be degenerate collapse?** **Checked and answered: no.** Every trained
   Regime B cell routes the two clusters to two *distinct* singleton slots (`{9}/{5}`, `{4}/{3}`,
   `{14}/{1}`, `{3}/{14}`, `{5}/{3}`, `{1}/{3}`); single-slot collapse would read J = 1.0. The result is
   memorisation without transfer (section 2.1), which is a different and milder failure than collapse.
2. **Whether the write stream carries structure a *learned projection* could use.** H4's uncentred cosine
   cannot see it. A held-out linear probe on the recorded latents settles this cheaply and should be part
   of the redesign.
3. **Whether H2 should be eliminated rather than left alive.** Its null is directionally well-supported;
   only the DV's resolution holds it open. A redesigned instrument may close it immediately, and it should
   be the first leg re-run.

## 7. Step 7b / 7c

- **7b (`autopsy_pre_routing_checks.py`):** `fire_count: 0`. C1/C2/C3 report **inapplicable**
  (claim-keyed, and no target carries `claim_ids`), and C5 inapplicable (no sibling `.md` at check
  time). Per the skill, *inapplicable is not "no fire"* -- the claim-keyed checks could not look here,
  so 7c carries the load.
- **7c (adversarial red-team, Fable):** see section 8.

## 8. Red-team verdict -- CONTESTED, accepted in full

Run on **Fable**, a different model from the drafter, with the drafter's reasoning withheld and the
ordering enforced (conclusion first, then raw evidence, then an independent recompute). Six
verdict-moving defects, **all accepted and applied**; the drafter independently re-verified the two most
consequential against the manifests before accepting.

| # | Defect | Disposition |
|---|---|---|
| D1 | The amend filed the input-distribution finding on an entry whose own hint disclaims that lever, with `depends_on_unresolved: []` (the GFLAG-0114 undeclared-gate pattern) | **Accepted.** `depends_on_unresolved` now names the SD-070 encoder recipe; section 5 states the split. |
| D2 | No `hypothesis_space_ledger_pending` block | **Accepted.** Block added; this session applies it directly (section 9b in the JSON). |
| D3 | `substrate_paths` named `experiments/_lib/probes/context_write_c2_probe.py`, which does not exist -- the probe is inlined per driver | **Accepted.** Path removed. |
| **D4** | The convergent read's "PERFECT separation -> the objective family is CAPABLE" is a **trained-set** readout; the generalization readout is flat and was never cited | **Accepted, claim WITHDRAWN.** Verified independently: `fresh_clusters_regime_b` is 0.4166666666666667 for *both* arms while `trained_clusters` went 0.5833 -> 0.0. Sections 2.1 and 3.5 rewritten. |
| **D5** | The "~10x under-run budget" is the harness's normal early-termination schedule, identical to V3-EXQ-956 seed-for-seed | **Accepted, argument WITHDRAWN.** Verified independently: 956 `[1546,1460,1478,1576,1446]` == 970 on all five shared seeds. Section 3.3 rewritten; `implementation` re-graded on 969/970/971. |
| **D6** | The cross-seed-set baseline is **conservative** for H2's null; the seed-matched contrast makes the null *stronger*, so "the data cannot bear the reading" is inverted | **Accepted, reading INVERTED.** Section 2.2 rewritten. |

Hygiene also accepted: `45/53` restated as the portfolio-wide `72/89`; the refusal's wording reconciled
and governance's 2026-08-30 routing of this portfolio noted; 972's uncentred-cosine limit hedged with a
linear-probe confirmer.

**7b did not and could not catch any of these.** Its claim-keyed checks (C1/C2/C3) reported
*inapplicable* because no target carries `claim_ids`, and C7 found nothing. That is the case the skill
warns about -- *inapplicable is not "no fire"* -- and it is why 7c carried the whole load here.

## 9. What governance should apply

1. **Amend** `contextmemory-write-path-addressing-degeneracy` with the four failure records, the
   instrument-redesign hint, and a `depends_on_unresolved` naming the **SD-070 encoder recipe** -- the
   upstream lever belongs there, not here (see the JSON sibling).
2. **The 2026-08-29 C2 directive is superseded** by governance's 2026-08-30 routing (user decision at
   this autopsy's gate). Governance may wish to mark it so in the substrate entry, so the contradiction
   does not resurface. No re-queue refusal is recorded.
3. **Do not** set any `evidence_direction` or `epistemic_category` on SD-017 / ARC-045 / MECH-166 from
   these runs -- they are claim-free and contribute to no claim's confidence.
4. **Ledger:** all four legs stay `alive` with `resolving_runs` and `basis` recorded (Step 9b).
   `initial_frozen_count` stays 4 -- there is no growth here. H2 is flagged as the leg closest to
   elimination and the first to re-run once the instrument is redesigned.

## 10. Disposition of withdrawn arguments

Recorded rather than deleted, per the skill's rule that a tested-and-dropped argument is a signal to the
next session.

| Argument | Status | Why |
|---|---|---|
| "H1 shows the objective family is CAPABLE of content-conditioning" | **WITHDRAWN** | The supporting readout is trained-set; the generalization readout is flat (0.4167 == 0.4167). |
| "A ~10x under-run training budget is a shared cause across all four legs" | **WITHDRAWN** | The realised schedule equals V3-EXQ-956's seed-for-seed; it is the environment's early-termination behaviour and the schedule the substrate entry registered. |
| "H2's data cannot bear the null reading" | **INVERTED** | The baseline mismatch is conservative for the null; seed-matched, every operating point moved the wrong way by ~0.5. |
| "The input distribution is the binding constraint" | **RETAINED, downgraded to leading hypothesis** | It loses its H1 leg and now rests on H2's direction plus H4's measurement, with H4's statistic hedged. |
| "REFUSED: do not queue a further write-side loss design against the unchanged instrument" | **WITHDRAWN** | User decision at the Step 8 gate: governance's 2026-08-30 routing supersedes the 2026-08-29 directive. The instrument finding itself is unaffected -- it rests on measurement. |
