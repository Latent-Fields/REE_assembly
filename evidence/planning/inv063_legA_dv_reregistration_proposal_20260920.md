# INV-063 leg A: proposed replacement DV set, staged for /governance

**Status: STAGED PROPOSAL. Nothing here is written to `claims.yaml`, `governance_flags.v1.json`
dispositions, `substrate_queue.json` or `experiment_proposals.v1.json`. No experiment is queued.
V3-EXQ-1071's driver stays UNQUEUED at ree-v3 `9700362aa5`. There is no experiment budget on
INV-063.**

- Session `inv063-lega-dv-rereg-20260921` (Mac `DLAPTOP`, main checkout), drafted 2026-09-24T07:05Z,
  from `chip-20260920-inv063-lega-dv-reregistration`.
- Discharges the re-registration owed by GFLAG-0389 / GFLAG-0390 and named in INV-063's
  `evidence_quality_note` and in `inv063_legb_wording_proposal_20260920.md` section 5.
- Source of truth for every code fact below: ree-v3 `origin/main` `4fc6f3d` (2026-09-24). Line
  numbers are re-resolved at that sha; several cited elsewhere have drifted.

---

## 0. Premise audit: what changed between the chip and this draft

The chip was written on 2026-09-21 against the claim text as it stood on 2026-09-20 and asked for
"the exact current leg-A sentence verbatim". **That sentence no longer exists.** Between
2026-09-21 and 2026-09-23 /governance rewrote INV-063's `what_would_answer` wholesale: the leg-B
proposal was APPLIED, the (P-FAIL) clause was registered (retroactively, 2026-09-22), the
GFLAG-0407 / MECH-573 skill-score requirement was added, and the three circular leg-A DVs
("count of VALENCE_SURPRISE residue writes", "realised `surprise_weight` at the replay call",
"start-selection distribution collapses toward uniform") were **removed entirely**. GFLAG-0389,
GFLAG-0390 and GFLAG-0394 are all now `resolved`.

Four consequences, each of which changes what this document has to be:

1. **This proposal replaces a PLACEHOLDER, not the circular DVs.** The live text already records
   the debt -- "leg A must first be RE-REGISTERED with a DV that is not a transform of
   `e3_prediction_error`" -- and names one candidate in passing. What is missing, and what nothing
   in the registry currently supplies, is the *operational* DV: a definition, its direction, its
   recording requirement, and the independence argument. That is this document.
2. **Coordination with `inv063_legb_wording_proposal_20260920.md` is MOOT, not owed.** It is
   applied. Verified against `origin/master`: the leg-B sentence and the (P-FAIL) clause are both
   live, and each of the three strings this proposal edits occurs **exactly once** in
   `what_would_answer` and is disjoint from both. One /governance pass can apply this alone.
3. **The chip's warning not to re-propagate the "legitimate, useful outcome" error is already
   discharged** -- (P-FAIL) now carries that language legitimately, with the retroactive note
   explaining why. Nothing here re-asserts the false claim about the pre-2026-09-22 text.
4. **The two ungated P1 sub-controls are already registered as a requirement** ("must actually
   gate rather than be recorded and ignored"). The *driver* still does not implement it; that is
   V3-EXQ-1071 code work and stays out of scope here (section 5).

Nothing in this audit weakens the finding the chip was built on. GFLAG-0389's circularity result
is re-verified against `4fc6f3d` in section 3a and is quantified there for the first time.

## 1. What is proposed, in three edits

- **EDIT 1** replaces the one-sentence leg-A DV placeholder with the operational DV set.
- **EDIT 2** appends two preconditions (P6 selection-instrument resolution, P7 ladder adequacy) to
  the NON-DEGENERACY PRECONDITION paragraph.
- **EDIT 3** changes C2's abscissa in the CONFIRMING sentence from arm INDEX to measured MEL. This
  is not scope creep: re-specifying leg A alone leaves C2 readable as arm SPACING, which is the
  second half of GFLAG-0389's finding and is measured in section 4a.

Each target string occurs exactly once. Everything else -- P1-P4, the excluded legs, F1-F3 as
restated in FALSIFYING, (P-FAIL), the whole leg-B block including the GFLAG-0407 skill-score
clause, the second-intake-axis note, `status`, `epistemic_category`, confidence, the literature
entries -- is untouched.

## 2. Exact text

### 2a. CURRENT, verbatim from `origin/master:docs/claims/claims.yaml`

EDIT 1 target (one occurrence, inside the `DV:` run of the CONFIRMING paragraph):

> DV: Leg A needs a replacement offline-function DV independent of e3_prediction_error -- a
> candidate is the replay start-selection composition (which episodes are drawn), not the surprise
> weight that scores them.

EDIT 2 target (one occurrence, the NON-DEGENERACY PRECONDITION paragraph, quoted whole for
position; only an append is proposed):

> NON-DEGENERACY PRECONDITION: P1-P4 stand as written, but leg A must first be RE-REGISTERED with
> a DV that is not a transform of e3_prediction_error, and the two P1 sub-controls the driver
> already computes (PE decay within a stationary window, and the matched-PE noise arm) must
> actually gate rather than be recorded and ignored. Any slot-routed DV stays excluded, now for a
> stronger reason than P5 gives: writing at all homogenises the bank.

EDIT 3 target (one occurrence, the CONFIRMING head):

> CONFIRMING: At pinned offline budget with an independent leg-A DV and a leg-B readout
> demonstrated to improve across sleep at all, both legs degrade monotonically as intake falls AND
> the drop between the two lowest arms exceeds the drop between the two highest by the
> pre-registered SD-scaled margin, on at least 2/3 seeds in the same direction on both legs.

### 2b. PROPOSED -- EDIT 1 replacement

> DV: Leg A is the COMPOSITION of replay start selection -- WHICH buffer entry is drawn -- and
> never the magnitude that scores the entries. Admissible leg-A statistics are functions of the
> SELECTED INDICES only, which makes them invariant to any common positive rescaling of the
> priority vector and therefore independent of `e3_prediction_error` by construction, since the
> surprise weight enters `get_valence_priority` as exactly one positive scalar on the only live
> valence channel (see the independence criterion below). PRIMARY (A1'): SELECTION DIVERGENCE FROM
> THE SURPRISE-BLIND NULL -- per waking period, over every `_do_replay` call, the total-variation
> distance in [0, 1] between the normalised histogram of the indices the live selector chose and
> the normalised histogram the SAME argmax rule returns on the SAME recorded priority vectors with
> the `VALENCE_SURPRISE` drive weight set to 0. It is 0 exactly when surprise gating makes no
> difference to which episode is replayed -- the registered intent, "surprise-gating has nothing
> left to prioritise" -- and it FALLS as intake falls, so it carries C1's polarity. Because the
> harm and liking valence channels are default-off and unset by this lineage's agent builder
> (`ree_core/utils/config.py:3904-3905`), the null reduces to the selector's own tie-break index,
> which is a KNOWN BIAS in one direction: when the most surprising entry happens to sit at that
> index, A1' under-reads. SECONDARY, RECORDED ALONGSIDE (A2'): the modal share of selected indices
> and the normalised entropy of the selected-index histogram. Both are composition statistics and
> both are admissible; note that their DIRECTION is the OPPOSITE of the prose this claim carried
> until 2026-09-20 -- under an argmax selector, losing the signal CONCENTRATES selection on the
> tie-break index rather than spreading it toward uniform, so entropy FALLS and modal share RISES
> as intake falls. NOT ADMISSIBLE as leg-A DVs, for reasons measured rather than asserted: any
> statistic of priority MAGNITUDE -- the max-minus-min spread registered as A3 until 2026-09-20,
> any share of priority mass, any Gini or entropy computed over normalised priorities. The spread
> is the surprise weight times the valence spread, a pure multiplicative carry of the manipulation
> check; and every mass-normalised statistic fails scale invariance through
> `get_valence_priority`'s additive `epsilon = 1e-6` floor
> (`ree_core/residue/field.py:988`), which at this lineage's measured scale exceeds the signal by
> ~230x and pins every mass share at 1/T. The rank correlation between replay priority and episode
> PE is likewise NOT a leg-A DV -- it is scale-invariant but reads PE as a variable, so it cannot
> discharge "independent of e3_prediction_error"; record it as a diagnostic only. RECORDING
> REQUIREMENT, part of the DV and not an implementation detail: per replay call, the full priority
> vector, the chosen index, the runner-up index, the argmax-to-runner-up gap, and the count of
> distinct float32 priority values; per arm-period, the number of replay calls.

### 2c. PROPOSED -- EDIT 2 append (two sentences, added to the end of the NON-DEGENERACY paragraph)

> (P6) THE SELECTION INSTRUMENT MUST BE RESOLVED, NOT TIED. A composition DV is only invariant
> while the argmax is decided in float32 arithmetic: priorities are `surprise_weight * valence +
> 1e-6`, so once the across-entry differences fall below the float32 ulp at that floor
> (1.19e-13, measured) every entry compares equal and the selector returns its tie-break index
> unconditionally, which reads as maximal concentration and is instrument death. Assert from
> output, per arm including the floor arm, that the distinct-float count exceeds 1 and that the
> argmax-to-runner-up gap exceeds that ulp on a stated majority of replay calls, and that each
> arm-period recorded at least 30 replay calls. Bench-measured headroom on this lineage's
> configuration is ~4 orders of magnitude, so this is a guard against a known degeneracy, not an
> expected failure -- but it must be asserted, because starvation is precisely what drives the
> signal toward the floor, so the instrument would fail first in the very arm the claim needs.
> (P7) THE LADDER MUST BE ADEQUATELY SPACED FOR A KNEE. The two MEL steps C2 divides by -- floor
> arm to next-lowest, and highest arm to second-highest -- must each exceed the per-seed
> monotonicity tolerance P1 already computes. A ladder that fails this cannot carry a knee test at
> all, and the failure is (P-FAIL), never the FALSIFYING branch.

### 2d. PROPOSED -- EDIT 3 replacement of the C2 clause

> CONFIRMING: At pinned offline budget with an independent leg-A DV and a leg-B readout
> demonstrated to improve across sleep at all, both legs degrade monotonically as intake falls AND
> the degradation is DISPROPORTIONATE AT THE LOW END MEASURED AGAINST MEASURED INTAKE, NOT AGAINST
> ARM INDEX: the DV change per unit of measured waking MEL between the two LOWEST-intake arms
> exceeds that between the two HIGHEST by the pre-registered SD-scaled margin (2x the pooled
> cross-seed SD of the per-unit-MEL slope, or 20% of the highest arm's slope, whichever is
> larger), on at least 2/3 seeds in the same direction on both legs, with P7 asserted on every
> scored seed. The abscissa is measured MEL and not the arm index because P1 constrains the
> ladder's monotonicity and total spread but says NOTHING about its spacing, so an arm-index knee
> is satisfiable by a ladder whose low-end MEL step is simply larger -- and is: V3-EXQ-1069's
> landed MELs already yield knee=True on seed 456 under the arm-index rule, from the manipulation
> check alone with no DV read (excess 9.605e-06 against a 9.402e-06 margin;
> evidence/planning/inv063_legA_dv_reregistration_proposal_20260920.md section 4a). Under the
> per-unit-MEL form a DV that is any affine function of MEL gives an excess of identically zero,
> which is what makes the spacing route unavailable rather than merely unlikely.

## 3. The independence criterion, operationally

### 3a. Test 1 -- SCALE INVARIANCE. RUN, on the live code path.

**Mechanism, re-verified at `4fc6f3d`.** Replay start selection is
`HippocampalModule._select_valence_weighted_start` (`ree_core/hippocampal/module.py:3036`): it
scores every theta-buffer entry with `ResidueField.get_valence_priority` and returns the
**argmax**, defaulting to the most recent entry (`module.py:3062`) and breaking ties toward the
FIRST index (strict `>` from `-inf`, `module.py:3073`). Priority is
`dot(evaluate_valence(z), drive_state) + epsilon`, `epsilon = 1e-6` (`field.py:988`).
`drive_state[VALENCE_SURPRISE]` is `min(1.0, _pe_ema * 5.0)` (`agent.py:10986`, written at
`agent.py:11010`), and `_pe_ema` is an EMA of `e3_metrics["prediction_error"]`, which
`agent.py:11064` republishes as `metrics["e3_prediction_error"]` -- the MEL the manipulation check
gates on. With `valence_harm_enabled` and `valence_liking_enabled` both default-False
(`config.py:3904-3905`) and unset by this lineage's builder, the dot product reduces to
`A2 * v(z) + epsilon`: the MEL dependence is exactly ONE positive scalar multiplying the whole
vector. An argmax is invariant to that; a normalised magnitude is not, because of the additive
epsilon.

**Measured.** Bench probe against the real `ResidueField` / `get_valence_priority`
(`scratchpad/indep_probe.py`; seed 42, T=12 buffer at the reachable z_world scale, four
`VALENCE_SURPRISE` writes of 8e-06..3.5e-05, i.e. V3-EXQ-1069's measured MEL scale; only the
surprise channel written, matching the config verification above):

| surprise weight `s` | argmax | priority spread (max-min) | top-of-mass share | normalised entropy of mass | distinct float32 values |
|---|---|---|---|---|---|
| 8.0e-05 | 7 | 3.452e-10 | 0.0833499752 | 0.999999998 | 12 |
| 1.0e-04 | 7 | 4.316e-10 | 0.0833541113 | 0.999999997 | 12 |
| 1.4e-04 | 7 | 6.041e-10 | 0.0833623399 | 0.999999994 | 12 |
| 2.13e-04 | 7 | 9.190e-10 | 0.0833772414 | 0.999999986 | 12 |
| 1.0e-02 | 7 | 4.315e-08 | 0.0845649971 | 0.999989322 | 12 |
| 1.0 | 7 | 4.314e-06 | 0.0862861917 | 0.999938689 | 12 |

and directly as the invariance statement, rescaling the whole priority vector by `c`:

| `c` | argmax | top-3 ordering | top-of-mass share |
|---|---|---|---|
| 1e-03 | 7 | [7, 1, 9] | 0.0835288624 |
| 1e-02 | 7 | [7, 1, 9] | 0.0845649971 |
| 0.1 | 7 | [7, 1, 9] | 0.0859533410 |
| 10.0 | 7 | [7, 1, 9] | 0.0863241877 |

**Verdicts, stated per candidate as the criterion requires:**

- **A1' (divergence from the surprise-blind null) -- INVARIANT.** It is a function of selected
  indices only; the argmax and the full top-3 ordering are unchanged across four orders of
  magnitude of `c` and across the whole plausible `s` range. Invariance is exact in real
  arithmetic, subject only to P6.
- **A2' (modal share, entropy of the selected-index histogram) -- INVARIANT**, same argument, same
  evidence.
- **Priority-mass statistics -- FAIL, rejected.** Top-of-mass share moves monotonically with the
  surprise weight (0.08335 -> 0.08629 as `s` goes 8e-05 -> 1; 0.08353 -> 0.08632 under `c` alone).
  It carries the manipulation check directly.
- **A3-as-registered-until-2026-09-20 (max-minus-min spread) -- FAIL, and quantitatively.** The
  spread scales linearly with `s`: 3.452e-10 at `s`=8e-05 to 4.314e-06 at `s`=1, a factor 1.25e4
  for an `s` ratio of 1.25e4. It is the surprise weight times a constant. This is GFLAG-0389's
  finding measured rather than argued.
- **Mass statistics additionally carry no signal at all at the measured scale.** With `A2` ~2.1e-04
  and `v` ~2.0e-05, `A2*v` ~4.26e-09 against `epsilon = 1e-6` -- the floor exceeds the signal by
  ~235x, so every mass share sits at 1/T = 0.0833 and the normalised entropy of mass is 0.99999999.
  A DV of that family would have been a constant dressed as a measurement.

**Limits of this probe, stated rather than papered over.** It exercises the real
`get_valence_priority` and the real selector rule on a synthetic buffer and synthetic writes at
the measured scale; it is not a full agent run, one seed, one buffer geometry. It is sufficient for
what test 1 asks -- invariance is a property of the arithmetic, and the rejections are
demonstrated, not inferred. It is NOT evidence about how these DVs behave across real arms; that
is test 2.

### 3b. Test 2 -- EMPIRICAL NON-CO-MOVEMENT. NOT RUN. OWED, and why.

**V3-EXQ-1069 does not record the quantity, and cannot.** Its manifest carries
`sleep_driver_pattern: "none (no sleep pass is configured or fired)"`; it measures MEL and nothing
else by design (`scope_note`: "Measures INV-063's P1 manipulation check and NOTHING else"). With
no sleep pass and no replay calls there is no start-selection composition in its 12 cells, and its
`arm_results` carry no priority, replay or selection field. A search of
`REE_assembly/evidence/experiments/` for the leg-A shim's own output keys
(`a3_replay_priority_spread`, `a3_start_selection_entropy`) returns **no landed run at all**: the
V3-EXQ-1071 driver that records them has never been queued.

**Registered as owed, not invented.** The empirical half of the independence criterion -- that the
candidate DV is not determined by MEL across arms and seeds -- **cannot be discharged from landed
data** and must be demonstrated by the first run that measures A1'/A2', BEFORE its C1/C2 verdict
is read: per seed, the rank correlation between the arm-ordered A1' values and the arm-ordered
MELs, reported with the verdict. A perfect rank correlation is not by itself disqualifying (both
are expected to fall with intake); what would disqualify is A1' being a deterministic function of
MEL, which the scale-invariance result in 3a already excludes structurally. The empirical check is
there to catch an unmodelled path, and it stays owed until a run exists.

## 4. C2, protected -- the part that a leg-A fix alone does not fix

### 4a. The knee is already present in the manipulation check. Reproduced.

V3-EXQ-1071's own `_knee` rule applied to V3-EXQ-1069's landed MELs, treating MEL itself as the DV
(pooled cross-seed SD of the arm-to-arm delta = 4.701e-06; margin =
max(2 x pooled, 20% of the HIGH arm)):

| seed | hi_drop (HIGH-MED) | lo_drop (LOW-NONE) | excess | margin | knee? |
|---|---|---|---|---|---|
| 42 | 1.738e-06 | 4.494e-07 | -1.289e-06 | 9.402e-06 | False |
| 123 | 1.972e-06 | 3.438e-06 | 1.466e-06 | 9.402e-06 | False |
| 456 | 6.729e-06 | 1.633e-05 | 9.605e-06 | 9.402e-06 | **True** |

This reproduces the figure the red-team reported. A knee verdict is available on seed 456 from the
manipulation check alone, with no DV read at all -- so under the arm-index rule a confirmed C2 on
ANY DV that tracks intake is not distinguishable from "the interval values {0, long, medium, short}
happen to be spaced with a bigger MEL step at the low end".

### 4b. The MEL ladder's spacing, measured

| seed | MEL steps NONE->LOW, LOW->MED, MED->HIGH | P1 monotonicity tol | steps below tol |
|---|---|---|---|
| 42 | 4.494e-07, 5.741e-06, 1.738e-06 | 4.03e-07 | none |
| 123 | 3.438e-06, 1.249e-07, 1.972e-06 | 4.59e-07 | LOW->MED |
| 456 | 1.633e-05, 3.728e-06, 6.729e-06 | 3.17e-07 | none |

The steps differ by up to 36x within a single seed (456: 1.633e-05 vs 3.728e-06). The ladder is
graded, per P1; it is nowhere near evenly graded, which is exactly the freedom the arm-index knee
rule reads as signal.

### 4c. Why the per-unit-MEL form, and why NOT the extrapolation form

Two spacing-robust forms were considered and one is rejected on measurement:

- **REJECTED -- fit the DV against MEL on the three highest arms and test the floor arm's
  shortfall against the prediction.** It requires extrapolating beyond the fitted span, and on
  V3-EXQ-1069's measured ladder the extrapolation distance EXCEEDS the fitted span on 2 of 3
  seeds: gap/span = 0.060 (seed 42), 1.639 (seed 123), 1.562 (seed 456). Two thirds of the seeds
  would be prediction-variance-dominated.
- **PROPOSED -- local secants in MEL** (EDIT 3): the DV change per unit MEL between the two lowest
  arms versus between the two highest. No extrapolation. Its conditioning requirement is exactly
  the two denominators, and on the landed ladder all three seeds clear it: lo denominator
  4.494e-07 / 3.438e-06 / 1.633e-05 against tolerances 4.03e-07 / 4.59e-07 / 3.17e-07, hi
  denominator 1.738e-06 / 1.972e-06 / 6.729e-06. **Seed 42's low-end denominator clears by only
  1.12x** -- thin, which is why P7 is a stated precondition with a (P-FAIL) consequence rather
  than a footnote. Note that seed 123's LOW->MED step (1.249e-07) is below tolerance but is NOT
  one of the two denominators C2 uses, so it does not block C2; it does mean the middle of that
  seed's ladder is unresolved.

The property that makes this a spacing control rather than a rescaling: for a DV that is any
affine function of MEL, both secants equal the same constant and the excess is identically zero,
regardless of how the arms are spaced. The seed-456 artefact in 4a is removed by construction, not
by margin tuning.

### 4d. What is narrowed, stated explicitly

C2 is **not** weakened in what it asserts -- it still requires a disproportionate low-end drop on
>= 2/3 seeds in the same direction on both legs, at the same effect-size convention. Two things
change and both are narrowings: the abscissa becomes measured intake rather than arm index, and
the test acquires a conditioning precondition (P7) whose failure routes to (P-FAIL) rather than to
the FALSIFYING branch. A ladder that cannot resolve its own end steps now yields "no verdict"
where it previously yielded a knee.

## 5. What this does NOT change

- **Does not reverse the `substrate_conditional` conversion** (GFLAG-0390, user decision
  2026-09-20). It supplies the leg-A half of what that conversion named as owed.
- **Does not queue anything, and does not unblock the ladder.** Leg B remains blocked on a readout
  that is readable and correct-signed together (the live text's own substrate dependency, with the
  GFLAG-0407 skill-score requirement). A re-specified leg A is necessary and not sufficient.
- **Does not fix the V3-EXQ-1071 driver.** Three defects stand, recorded in
  `inv063_legA_dv_circularity_20260920.md` section 3 and NOT addressed here: the two registered P1
  sub-controls are computed and never reach `gating_ok` (and the authoring smoke shows both WOULD
  fire -- the noise arm's A3 exceeds the HIGH arm's at lower MEL, and PE RISES in the stationary
  window); the leg-B refusal route is an all-four-arms AND; and `need` is computed from
  `len(seeds)` rather than scored seeds. EDIT 2's P6/P7 and EDIT 1's recording requirement add
  further driver work. All of it is `/queue-experiment` work on an unqueued driver with no budget.
- **Does not touch** `status` (stays `candidate`), confidence, `invariant_type`, the excluded legs,
  P1-P5 as written, the leg-B block, (P-FAIL), the second-intake-axis note, the five 2026-09-08
  literature entries, or the `non_contributory` dispositions of V3-EXQ-1063 and V3-EXQ-1069.

## 6. Proposed dispositions, for /governance to accept or revise

| Item | Proposed disposition |
|---|---|
| EDIT 1 (leg-A DV set) | **APPLY.** It is the re-registration GFLAG-0389/0390 recorded as owed; without it leg A has a placeholder where a DV should be, and the claim cannot be re-queued even if leg B's substrate appears. |
| EDIT 2 (P6, P7) | **APPLY WITH EDIT 1.** P6 is what makes EDIT 1's invariance claim true in float32 rather than only in the reals; P7 is what makes EDIT 3 conditionable. Applying EDIT 1 alone would register an invariance guarantee with no assertion behind it. |
| EDIT 3 (C2 abscissa) | **APPLY**, or, if /governance prefers to keep the arm-index rule, **narrow C2 explicitly** and record that a confirmed C2 is not attributable to the DV -- section 4a is the measurement that forces one or the other. Leaving both the arm-index rule and a fixed leg A standing is the one option this document argues against. |
| Test 2 (empirical non-co-movement) | **REGISTER AS OWED** on the first run that measures A1'/A2', reported before its C1/C2 verdict is read. It cannot be discharged from landed data (section 3b). |
| GFLAG-0389 / GFLAG-0390 | Already `resolved`. This document is the discharge of the re-registration they named; a resolution note pointing here would close the loop, but no status change is proposed. |
| V3-EXQ-1071 driver defects | **NOT a governance disposition.** Chip to `/queue-experiment` if and when leg B's substrate dependency is met. No budget now. |

Cross-refs: `evidence/planning/inv063_legA_dv_circularity_20260920.md` (GFLAG-0389);
`evidence/planning/inv063_legb_wording_proposal_20260920.md` (GFLAG-0394, applied);
`evidence/planning/inv063_legb_tau_bind_20260920.md` (GFLAG-0382);
`evidence/planning/inv063_p1_gate_and_infonce_tau_20260919.md`;
`evidence/planning/failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20.md`;
`evidence/planning/falsifier_completion_and_runnability_audit_20260921.json`;
manifest `v3_exq_1069_inv063_p1_gate_798a_p0_20260920T082003Z_v3`.

---

## 7. Addendum, 2026-09-24: peer review, one correction and one strengthening

Reviewed the same day by session `vigilant-colden-ac4766-inv063dv`, which had been dispatched
on this identical task (a third dispatch; path-based arbitration did not fire because its claim
named `..._20260924.md` against this file's `..._20260920.md`). It stood down rather than write a
second proposal, closed its claim `--not-landed` naming `f6cc06142f`, and **superseded GFLAG-0445
into GFLAG-0446** (`REE_assembly b9fd0a89c6`), so /governance now sees ONE open leg-A item rather
than two overlapping ones. Its review re-verified independently that all three EDIT target
strings occur exactly once on `origin/master` and are disjoint from the leg-B sentence and the
(P-FAIL) clause. Three points came back; all three are taken up here.

### 7a. The Test-1 probe is now landed and re-runnable (auditability gap, closed)

Section 3a's measurements were originally cited to a session-scoped scratchpad path that no
longer resolves -- leaving the single arithmetic claim the whole proposal rests on auditable only
on trust. The probe is now landed alongside this document, following the existing
`evidence/planning/*_probe_*.py` convention (12 prior instances):

```
/opt/local/bin/python3 /Users/dgolden/REE_Working/REE_assembly/evidence/planning/inv063_legA_independence_probe_20260924.py
```

Deterministic (`torch.manual_seed(42)`), ASCII-only output, `REE_V3_PATH`-overridable. Re-run
2026-09-24 against ree-v3 `origin/main` `4fc6f3d` with torch 2.12.0: it reproduces every figure in
section 3a exactly -- argmax 7 and top-3 ordering [7, 1, 9] preserved across all four rescalings
`c` in {1e-3, 1e-2, 0.1, 10}; `top_mass_share` 0.0835288624 -> 0.0863241877 across those same
rescalings; the retired A3 spread 3.45153e-10 (s=8e-05) -> 4.31449e-06 (s=1); float32 ulp at the
epsilon floor 1.19209e-13; `A2*v` 4.26e-09 against `epsilon` 1e-6, a ratio of 0.00426. It also
prints the verdicts, so a reader does not have to reconstruct which candidate each column kills.

### 7b. STRENGTHENING: the MEL form of the surprise weight is itself CONDITIONAL, and this sharpens the finding

Section 3a stated that `drive_state[VALENCE_SURPRISE]` is `min(1.0, _pe_ema * 5.0)` and verified
that the harm and liking channels are default-off. It did not state that **the MEL form is itself
gated**. Verified at `agent.py:10984-10986`:

```python
surprise_weight = 0.3
if self.config.surprise_gated_replay and self._pe_ema > 0:
    surprise_weight = min(1.0, self._pe_ema * 5.0)
```

So the weight is the **constant 0.3** unless `surprise_gated_replay` is True AND `_pe_ema > 0`.
The conclusion in 3a holds by two independent routes -- INV-063's own P4 requires
`surprise_gated_replay=True`, and this lineage's builder sets it
(`experiments/v3_exq_1071_inv063_four_arm_intake_ladder.py:351`) -- so this is a strengthening,
not a correction.

**And it sharpens what leg A's circularity actually is.** In the ungated branch the weight is a
constant, hence not a transform of `e3_prediction_error` at all: the circularity GFLAG-0389 found
is **specifically a property of the P4-pinned regime**, which is the only regime in which leg A
can be measured (P4 is what makes the MECH-205 instrument live). It is therefore not an incidental
coupling that a differently-configured run could avoid -- it is entailed by the precondition the
claim itself requires. That is an argument for re-registering the DV rather than re-configuring
the run, and it belongs in the record.

### 7c. CORRECTION to this document: EDIT 3 closes a degree of freedom in the CRITERION; it does not measure the confound away

Section 4c ends "the spacing route is unavailable rather than merely unlikely". **That overclaims,
and is corrected here.** What EDIT 3 establishes exactly:

- **First-order, and this is the real gain:** for a DV that is any AFFINE function of MEL, both
  per-unit-MEL secants equal the same constant and the excess is identically ZERO regardless of
  how the arms are spaced. That is precisely the shape that produced the seed-456 artefact in 4a,
  so an affine DV can no longer manufacture a knee out of spacing. The arm-index rule has no
  such null.
- **Residual, second-order:** for a genuinely CURVED DV the two secants sample curvature over
  windows of different widths (on V3-EXQ-1069's ladder the low-end and high-end MEL steps differ
  by up to 36x within one seed, per 4b), and a wider window averages more curvature. The
  comparison therefore retains a magnitude-level spacing dependence. P7 BOUNDS that dependence by
  requiring both denominators to be resolved; it does not remove it.
- **What is not established by any of this:** whether the actual A1'/A2' is near-affine in MEL.
  That is exactly the OWED Test 2 (section 3b), and it cannot be settled from landed data.

So the honest reading for /governance, and the one this addendum asks to be recorded with EDIT 3:
the per-unit-MEL abscissa **closes the spacing degree of freedom in the criterion's definition**;
it has not **measured** the confound away, and it does not pre-empt Test 2. This weakens no
verdict above -- 4a's reproduction of a knee from MEL alone under the arm-index rule stands
unchanged, and it is still the measurement that forces either EDIT 3 or an explicit narrowing of
C2 -- but "unavailable" was the wrong word for a guarantee that holds strictly only at the affine
null.

### 7d. Unchanged residuals, stated so the hand-off is unambiguous

Neither session is working these, and neither is claimed: **(i)** the empirical non-co-movement
measurement (Test 2), which needs a run that does not exist; **(ii)** the three V3-EXQ-1071 driver
defects in `inv063_legA_dv_circularity_20260920.md` section 3, which are `/queue-experiment` work
on an unqueued driver with no budget. Nothing in this addendum applies anything to `claims.yaml`.
