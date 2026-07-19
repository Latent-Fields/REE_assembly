# Failure Autopsy -- V3-EXQ-785 (MECH-463 arousal variance-amplifier decomposition)

- **Generated:** 2026-07-19T10:53:44Z
- **Session:** `commit-push-ordering-fae508` -- "V3-EXQ-785 MECH-463 asymmetric-arm autopsy"
- **Scope:** single run, two arms
- **Status:** confirmed (user-gated 2026-07-19)
- **Machine-readable companion:** `failure_autopsy_V3-EXQ-785_2026-07-19.json`

---

## Headline

**The manifest's self-route `substrate_not_ready_requeue` is wrong, and it buries a strong result.**

The run has two arms and **only one is vacuous**. The whole-run gate flattened a GREEN arm's
well-powered finding because a *different* arm was degenerate -- and the degenerate arm is the
only one whose statistic points the claim's way.

| Arm | Gate | Preconditions | measured rho (pre-registered +0.6) | Read |
|---|---|---|---|---|
| `harm_incumbent` | **GREEN** | **6 of 6 met**; 3959 committed ticks; ~396/decile; incumbent margin 0.882 | **-0.8303** | strong, *opposite* direction |
| `entropy_incumbent` | RED | 5 of 6 -- P7 fails (1 component vs required >= 2) | +0.5879 | near-miss "support", arithmetically forced |

---

## 1. Facts

**Manifest:** `outcome: FAIL`, `evidence_direction: non_contributory`, `non_degenerate: false`.

`degeneracy_reason` names exactly one precondition:
`entropy_incumbent::n_components_with_nontrivial_share`, measured **1.0** against threshold **1.5**.

All twelve other preconditions across both arms are `met: true`.

**Recording provenance:** always-core is **COMPLETE** -- `recording_schema`, `substrate_hash`
(`849de508...`), `machine`, `machine_class` (`linux-x86_64-py3.10`), `elapsed_seconds` (459.79),
full `config`, explicit `seeds` `[0,1,2,3,4]`. A `substrate_ceiling` reading would have been
falsifiable here; it is not the reading, but the provenance is sound.

**Recording gap (secondary finding):** `custom_information.per_tick_sink` declares
`..._per_tick.jsonl`, and that file is **absent from disk** -- checked in `evidence/experiments/`
and by a repo-wide `find`. It does *not* block the headline adjudication (the decile profiles are
in the manifest) but it does block the one reanalysis that would test the mechanism directly:
commit *rate* per urgency decile.

---

## 2. Why the self-route label is wrong

The scored arm's criterion did not return a null. It returned **rho = -0.8303 against a
pre-registered +0.6** -- a strong effect in the *opposite* direction, on ~396 committed ticks per
decile with per-decile share SD 0.05-0.08 (SE ~0.003, so the 0.970 -> 0.831 span is of order
**40 SE**).

Meanwhile the only claim-favourable number in the run (`entropy` rho +0.5879, gap +0.0374 clearing
its 0.02 threshold) comes from a decomposition where the incumbent `CH:mech341` holds share
**1.0065** and every other component sits below |0.01| (`f` -0.0013, `harm_weighted` -0.0048,
`residue_weighted` -0.0004). A single-component decomposition cannot measure redistribution. The
gate was right to call it RED.

**So: the clean arm contradicts the claim, the vacuous arm appears to support it, and the label
records "substrate not ready."**

### 2a. The entropy arm's RED was foreseeable at design time

This is the sharpest finding, and it is a **test-design defect, not a substrate gap**.

```
config.regimes[1].expected_incumbent_share = 1.043
```

That value is committed in the manifest's own config, pre-registered from the script docstring's
2026-07-18 seed-0 measurement table. Shares sum to exactly 1.0 by construction (full covariance
attribution), so an incumbent share **above unity** forces every other component to sum to -0.043
and none can plausibly clear the |0.01| floor. P7 requires **two** components above that floor.

**The regime could not pass its own gate, and the number proving it was in the config.**

The script had already derived the governing principle -- its P1 note says the authority gate is
applied *only* to regimes whose incumbent is a modulatory channel, because asserting it elsewhere
"would make that regime structurally un-passable and silently collapse the two-regime design back
to one." P7 was applied **without** that conditioning and did the analogous damage in reverse.

---

## 3. What the clean arm actually found

`harm_incumbent`, gate GREEN, incumbent `harm_weighted` as pre-registered (margin 0.8816),
mean shares `harm_weighted` 0.9368 / `f` 0.0552 / `residue_weighted` 0.0080.

| decile | urgency_mean | incumbent share | total variance |
|---|---|---|---|
| 0 | 0.06965 | 0.96988 | 2.855e-06 |
| 1 | 0.07442 | 0.96742 | 2.486e-06 |
| 2 | 0.08141 | 0.97569 | 7.146e-06 |
| 3 | 0.08892 | 0.97238 | 6.747e-06 |
| 4 | 0.09422 | 0.95453 | 6.896e-06 |
| 5 | 0.09967 | 0.95152 | 8.673e-06 |
| 6 | 0.10448 | 0.93954 | 7.923e-06 |
| 7 | 0.11275 | 0.96065 | 1.239e-05 |
| 8 | 0.12121 | 0.84575 | 3.583e-05 |
| 9 | 0.12541 | 0.83079 | 4.023e-05 |

**Decomposing the share into share x total separates the claim's two premises, and they have
opposite signs:**

```
decile 0 -> decile 9
  TOTAL cross-candidate variance      x14.1     <- AMPLIFICATION premise: CONFIRMED
    incumbent absolute variance       x12.1
    non-incumbent absolute variance   x79.2     <- CONCENTRATION premise: CONTRADICTED
```

Arousal **does** amplify selection variance, strongly. But it amplifies the **subordinate**
channels about **6.5x faster** than the incumbent, so the dominant channel's share *falls*.

### 3a. This outcome has no cell in the pre-registered grid

The script enumerates four outcomes: SUPPORTS (rises in both), MIXED/REFINE (rises only in the
harm regime), REFUTES (**flat** in both with gate GREEN), INVALID (gate RED). The observed
behaviour is a strong monotone **decrease** -- neither "rises" nor "flat". Even with a
regime-conditioned gate, the run had **no valid self-route available**.

### 3b. Bearing on the registered consequence

MECH-463 states that under F-dominance this makes affective engagement "ENTRENCH F rather than
convert diversity." The clean arm points the other way: arousal **broadens** the variance base.
If that survives an exogenous test, arousal is a candidate **diversity lever**, which bears
directly on the conversion-ceiling programme.

Scope caveat the script itself records: the substrate offers no F-incumbent cross-candidate regime
(`f` is 0.055 here), so this is evidence about the **mechanism**, not directly about F-entrenchment.

---

## 4. A candidate reasoning error in the claim (flagged, not scored)

MECH-463's `functional_restatement` argues that "shrinking the commit threshold makes commitment
fire on whichever candidate already has the largest score separation."

But `effective_threshold * (1.0 - urgency_applied)` (e3_selector.py:2679-2686, cited by the claim
itself) is an **admission** threshold. Lowering it is **less** selective -- it *admits*
lower-separation ticks. That predicts a more heterogeneous committed set at high urgency and a
**falling** dominant-channel share: exactly the observed -0.83.

This is a *candidate*, not established -- the run cannot separate it from the endogeneity confound.
But if correct, the defect is in the claim's derivation, and no amount of re-running fixes a
prediction whose sign is wrong.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened on concentration / strengthened on amplification** | the claim is compound; the halves separated cleanly with opposite signs |
| Biological reference | clear | LC-NE / D1-D2 global gain. Not a missing-dependency signature -- a mis-derived *sign* in translating "global gain" into "concentrates on the dominant channel" |
| Prerequisites | present | SD-011 harm stream fed via `sense()`, SD-056 contrastive candidates, 396a EMA driven (commit rate 0.964) |
| Implementation | complete | instrumentation landed ree-v3 `435322f` behind `e3_score_decomp_enabled` |
| Environment | adequate for harm regime, inadequate for a second identity | no non-degenerate second cross-candidate regime exists |
| Measurement | **under-instrumented** | (1) gate applied whole-run not per-regime; (2) grid has no monotone-decrease cell |
| Integration | coupled | conditioning variable and incumbent share the `z_harm_a` source by design |
| Scale | adequate | 5 seeds x 800 ticks x 2 regimes; 3959 committed ticks scored; all 10 deciles populated vs `MIN_DECILES_POPULATED` 6 |

**Recommended `epistemic_category`:** `measurement_test_design_defect`
**Recommended `evidence_direction`:** `mixed` (corrected from `non_contributory`)

---

## 6. Threats to the finding (why this is not a demotion)

1. **Endogeneity -- the leading rival.** `urgency_applied` is emergent, not manipulated. High-urgency
   ticks are also **near-hazard** ticks (env `hazard_harm` 0.5), whose candidate geometry may differ
   for reasons unrelated to arousal. This alone is why no governance weaken is routed.
2. **The harm-stream coupling runs AGAINST the finding.** `urgency_applied` derives from `z_harm_a`
   while the incumbent is `harm_weighted` -- shared source. But that coupling would push the share
   **up**; the observation is a **fall**. It strengthens rather than explains away.
3. **Under-differentiated `z_world`** (participation ratio ~1.06): absolute variances are tiny
   (2.9e-06 to 4.0e-05). Bites the generalisation, not the across-decile comparison.
4. **Single regime.** With the entropy arm vacated, the **channel-agnostic** half of the claim is
   untested at a second incumbent identity.

---

## 7. Routing

**`complex (probe-gated) / puzzle (known rules)`** -- the frame is well-posed, the rival is named,
and one missing *fact* decides it: does the redistribution survive **exogenous** urgency with
hazard proximity controlled?

- **Re-derive brake: does NOT fire.** MECH-463 has **zero** prior autopsies (registered 2026-07-18;
  this is its first test), and this category is `measurement_test_design_defect`, not
  `substrate_ceiling`. The routed re-test also changes the design axis (observational ->
  exogenous manipulation) rather than re-posing the same measurement.
- **GOV-FANOUT-1: exempt.** Two hypotheses are live, but a *single* redesign discriminates both --
  exogenous manipulation breaks the endogeneity by construction and the proximity covariate
  measures the rival in the same run.
- **Granularity-debt trigger: does not fire** (first autopsy on this claim). **Forward flag:**
  MECH-463 is visibly compound; if a second autopsy produces another distinct signature, take
  `/claim-synthesis` seriously. A split was offered at the gate and **deferred by the user** in
  favour of re-queue only.
- **Substrate queue entry: `none`.** No substrate gap -- every mechanism the probe needs is
  implemented, wired and confirmed live by the six met preconditions.

### Re-queue spec -- V3-EXQ-785a (`/queue-experiment`)

1. **Manipulate urgency EXOGENOUSLY** (the load-bearing change, and why it gets a new letter).
2. Record a **hazard-proximity covariate** per tick; report the profile conditioned on it.
3. **Regime-condition the P7 gate** exactly as P1 already is.
4. **Replace or drop** the `entropy_bias_scale=1.0` regime -- target >= 2 components above |0.01|
   with incumbent share materially below 1.0, or state plainly that agnosticism is untested.
5. Add a **monotone-decrease cell** to the interpretation grid.
6. Score **amplification and concentration as separate criteria**.
7. **Durably emit the per-tick sink** per `experimental_recording_standard_2026-07-12.md`; call
   `experiments/_lib/manifest_core.stamp_recording_core(...)`.
8. Record **commit rate per urgency bin** -- the direct test of the admission-threshold mechanism.

---

## 8. Learning extracted

1. **A non-vacuity gate must be conditioned on the regime it is meaningful for**, or one arm's
   structural RED silently vacates another's valid result. This script derived that rule for P1 and
   did not apply it to P7. When a design earns a regime-conditioning rule for one precondition,
   audit *every* precondition against it.
2. **A pre-registered incumbent share above 1.0 is a design-time proof that a
   >= 2-components gate must fail.** `expected_incumbent_share = 1.043` was committed alongside the
   gate it made unsatisfiable. One arithmetic step at queue time would have caught it for free.
3. **Always record and read the DENOMINATOR of a share criterion.** Share alone says "refuted";
   share *and* total says amplification confirmed at 14.1x while concentration is contradicted.
4. **An interpretation grid enumerating "rises" and "flat" has no cell for "falls."** Cover the
   sign-reversed case, or a strong contrary result cannot self-route and gets buried.
5. **Check whether a confound runs WITH or AGAINST the observed direction** before discounting a
   result. Here the shared-source coupling would raise the share; the observation is a fall.
6. **A modulator acting on an ADMISSION threshold dilutes rather than concentrates.** Where a
   prediction depends on the sign of a threshold effect, name the parameter and check its direction
   in the code before queuing.
7. **Declaring a per-tick sink path is not recording it.** The named file is absent, so the one
   reanalysis that would test the mechanism is unavailable at full compute cost already spent.

---

## 9. Hypothesis-space ledger -- APPLIED 2026-07-19T15:26:01Z (see 9a)

Step 9b was **deliberately skipped**: the live V3-EXQ-779b autopsy session holds
`hypothesis_space_registry.v1.json` as an active TASK_CLAIMS resource (claimed 2026-07-19T09:52:16Z).
User confirmed the skip at the interactive gate.

The intended blocks are in the JSON companion under
`targets[0].hypothesis_space_ledger_pending` -- a new question `arousal-variance-amplifier` with
three pre-registered hypotheses (`H-arousal-concentrates`, `H-arousal-broadens`,
`H-endogenous-hazard-geometry`), `initial_frozen_count` 3, **all left `alive`** (no bits claimed:
`non_degenerate` is false and urgency was endogenous, so the elimination bar is not met).

**APPLIED** at the V3-EXQ-785a adjudication -- see section 9a below.


---

## 9a. Ledger APPLIED at the V3-EXQ-785a adjudication (2026-07-19T15:26:01Z)

Applied by session `governance-641c45`. The blocker named above had lifted: the V3-EXQ-779b
autopsy session's claim on `hypothesis_space_registry.v1.json` flipped to `done` at
2026-07-19T11:52Z, and the registry was clean in the working tree.

V3-EXQ-785a **meets the elimination bar this cycle could not** -- gate GREEN, `non_degenerate`
true, urgency EXOGENOUS (i.i.d. uniform over a pre-registered grid), 1757 independent committed
selections across an 8.5x urgency range vs this run's 1.8x endogenous range.

| Hypothesis | Drafted | Applied | Bits |
|---|---|---|---|
| `H-arousal-concentrates` | alive | **eliminated** | 1 |
| `H-arousal-broadens` | alive | **eliminated** | 1 |
| `H-endogenous-hazard-geometry` | alive | **alive** (amended -- see below) | 0 |

**Reduction this cycle: 2 of 3.** Both arousal hypotheses are contradicted under clean exogenous
manipulation: `var_total` fold 0.970 (rho -0.086) where this run measured 14.1x, and incumbent
share 0.9375 -> 0.9411 (gap +0.0036, rho +0.31) where this run measured a 0.970 -> 0.831 fall at
rho -0.83. The null is tight, not underpowered -- SE ~0.0044 puts the gap under 1 SE, where this
run's 0.139 fall would have been 30+ SE -- and internal validity held (`effective_threshold`
0.3761 -> 0.2570, a real 32% reduction, with nothing downstream responding). So **this run's
entire profile, amplification and dilution alike, was the endogeneity confound.**

### The one amendment to the drafted blocks

`H-endogenous-hazard-geometry` was **not** recorded as confirmed, though the residual logic invites
it. Its apparent direct support is a **between-seed artifact**. Pooled over all 1757 committed rows
the hazard covariate looks like it reproduces this run's profile -- `corr(hazard_prox_mean, share)`
= -0.187 and `corr(hazard_prox_mean, log10 var)` = +0.171, the same signs as the 785 result. But
within seed the effect vanishes and mostly **reverses**:

| seed | r(hazard, share) | tertile share gap | var fold |
|---|---|---|---|
| 0 | +0.089 | +0.011 | 0.93x |
| 1 | +0.076 | +0.012 | 1.07x |
| 2 | +0.041 | +0.005 | 1.01x |
| 3 | -0.125 | -0.014 | 1.02x |
| 4 | +0.135 | +0.014 | 1.07x |

Across the 5 seed means, `r(mean hazard, mean share)` = -0.78 and `r(mean hazard, mean var)` =
+0.77, carried largely by seed 0 (mean share 0.833, mean var 4.47e-05, ~7x the other seeds). This
is Simpson's paradox on n=5. Per the Step 9b mapping table that is the *does-not-discriminate* row:
`resolving_runs` and `basis` recorded, state unchanged, no bit claimed. Confirming it needs a run
that **manipulates** hazard proximity, or a within-seed design with enough seeds to separate the
two. (Noted for whoever picks that up: seed 0's mean share of 0.833 is near-identical to this run's
endpoint of 0.831.)

Leg-level `evidence_direction` is recorded as `weakens` for both eliminated legs, per the registry's
leg vocabulary (`{weakens, non_contributory}`); the manifest's claim-level `does_not_support` is
preserved alongside as `manifest_evidence_direction`.

### This run's own direction moved past the recommendation below

Section 10's recommended `mixed` is **superseded**. Because 785a shows the amplification half was
confound-borne too, this run's manifest moved to `evidence_direction: superseded` with
`superseded_by: V3-EXQ-785a` (CLAUDE.md supersession policy), which the indexer treats as inactive
so it no longer weights MECH-463. An independent precision defect compounds it, identified in the
785a manifest: this run read `e3.last_score_diagnostics` without clearing it, so latched ticks
re-recorded the previous tick's diagnostics as new rows -- its "3959 committed ticks / ~40 SE"
reflect ~440 genuine selections (~9.0x pseudo-replication).

**MECH-463 stays `candidate`.** Three caveats bound the result and are recorded in its
`evidence_quality_note`: channel-agnosticism is untested (single regime -- the entropy regime was
dropped with recorded evidence that CH:mech341 absorbs ~99-115% of cross-candidate variance at every
`entropy_bias_scale` tried); z_world is under-differentiated (participation ratio ~1.06), leaving
live the reading that the substrate cannot *express* the effect; and the scope is the SD-011
commit-threshold route only, not every arousal route.

### Correction to section 4

Section 4's flagged "candidate reasoning error" is itself **mis-signed**. `committed = variance <
commit_threshold * (1 - urgency)` is an UPPER bound, so raising urgency makes admission **stricter**,
not "less selective"; and the gated quantity is the z_world *running variance* (world-model
stability), not candidate separation, because `use_harm_variance_commit` is off. 785a's C3 measured
commit rate flat at ~0.99-1.00 across all six levels despite the 32% threshold movement, which rules
out differential admission as the mechanism regardless of sign.

---

## 10. Governance hand-off summary (as recommended at the 785 gate -- partly superseded, see 9a)

| Item | Recommendation |
|---|---|
| `evidence_direction` | `non_contributory` -> **`mixed`** |
| `epistemic_category` | `measurement_test_design_defect` |
| Claim status | **candidate (unchanged)** -- do NOT demote |
| Substrate queue | `action: none` |
| Routing | `/queue-experiment` -> **V3-EXQ-785a** |
| Ledger | apply `hypothesis_space_ledger_pending` |
| New claim flags | `compound_claim_premises_separated`, `single_regime_only` |

Exact `evidence_quality_note` text for governance to write is in the JSON companion at
`targets[0].recommended_evidence_quality_note`.

> **Do not cite the entropy regime's rho +0.5879 as support for MECH-463.** It is an
> arithmetically forced single-component artifact and is the run's only claim-favourable number.
