# Failure autopsy -- V3-EXQ-1062 (MECH-055, affect channel separation)

- **Run:** `v3_exq_1062_mech055_affect_channel_separation_diagnostic_20260922T175212Z_v3`
- **Queue id:** V3-EXQ-1062 | **Backlog:** EVB-1413 | **Claim:** MECH-055
- **Outcome:** FAIL | **experiment_purpose:** diagnostic | **self-route:** `substrate_not_ready_requeue`
- **Machine:** ree-worker-3 (`linux-x86_64-py3.10-torch2.12.0+cpu`) | **elapsed:** 16,593 s (~4.6 h)
- **Seeds:** 42, 137, 2026 | **substrate_hash:** `3e103a9e…345f45` | **substrate_commit:** `9b3fbfd4e4`
- **Status:** awaiting_human_confirmation
- **Autopsy triggers:** BOTH -- a FAIL, and an `experiment_purpose: diagnostic` result.

## 0. Dry-run gate (Step 2a)

`check_dry_run_citations.py` run over the target and the family. The family contains a dry
sibling, `..._20260922T125835Z_v3`, so the bare queue id **V3-EXQ-1062 is AMBIGUOUS** and every
citation in this artifact uses the full run_id.

- Cited real run: `..._20260922T175212Z_v3` -- clean.
- `excluded_dry_run_ids`: `..._20260922T125835Z_v3`.
- `dry_run_checked: true` -- the checker script was run, not a raw field read.

`validate_experiments.py --checks dry_run_unreachable_criterion` fires on 11 drivers, all in the
`v3_exq_543*` family; **the 1062 driver is clean on that lint.** The lint demonstrably fires, so
this is a meaningful negative. The manual read of the reduction block was still performed --
see the finding in section 6.

## 1. Facts

Two arms ran; one was scored.

| arm | interval | gate | harm_a_forward_r2 | mean_harm_exposure | mean_dacc_pe |
|---|---|---|---|---|---|
| ARM_0_STATIONARY | 0 | **GREEN** | 0.940 / 0.940 / 0.977 | 0.00400 / 0.00609 / 0.00168 | 0.0960 / 0.0513 / 0.0559 |
| ARM_2_HIGH_SHIFT | 10 | **RED** | 0.954 / 0.948 / 0.932 | 0.01854 / 0.01476 / 0.01699 | 0.0744 / 0.0487 / 0.0733 |

The red arm failed exactly two readiness preconditions:

| precondition | measured | threshold | direction |
|---|---|---|---|
| `harm_exposure_relative_deviation_bounded` | **3.276** (~4.28x exposure) | 0.25 (1.25x) | upper |
| `pe_load_elevated_vs_stationary` | **-0.0332** | +0.05 | lower |

Criteria as reported:

| criterion | load-bearing | passed | measured | threshold | maps to |
|---|---|---|---|---|---|
| C1 harm channels not redundant | **yes** | false | **NaN** (`scored_arms: []`) | 0.9 upper | MECH-055 FALSIFYING (ii) |
| C2 axes not fixed ratio | **yes** | **true** | 0.271 | 0.8 upper | MECH-055 FALSIFYING (i) |
| C3 differential channel response | no | false | -0.478 | 0.2 lower | CONFIRMING, 2nd clause |
| C4 timing signatures differ | no | true | 0.0139 | 0.1 lower | CONFIRMING, companion |

**C1 was not failed -- it was never evaluated.** It is scored on SHIFT arms only; the single
shift arm went red, so `c1_arms == []` and `_worst_cell` over an empty list returns
`(nan, "(no finite cell)")`. The driver's own Step 4.5 red-team caught precisely this trap
(finding F1) and now runs a decidability test **before** any claim verdict, routing to
`substrate_not_ready_requeue` / `non_contributory`. That guard worked. What it does not do is
rewrite the criterion's own `passed` field, which still reads `false` -- so a reader who consumes
`criteria[].passed` without reading `scored_arms` will mistake an unevaluated criterion for a
failed one. C3 is likewise vacated: its matched-exposure premise is the very precondition that
failed.

## 2. Claim layer

MECH-055 (`claims.yaml:6125-6208`): status `candidate`, `epistemic_category: standard`,
`depends_on` ARC-005 / MECH-048 / MECH-054 / MECH-035. No `confidence`, no `evidence_quality_note`.

The claim **licenses this narrowed test and pre-specifies this exact self-route**: "a narrower
two-axis-plus-harm-only test CAN run now and should self-route substrate_not_ready if attempted
as a verdict on the full claim before the benefit-side channel lands." The run did what the claim
asked.

`claim_evidence.v1.json`: `experimental_confidence 0.0`, `literature_confidence 0.674`,
quadrant **`plausible_unproven`**, `genuine_exp_count 0`. **V3-EXQ-1062 is the first and only
experimental run ever tagged MECH-055.** Per the no-blending rule, the lit and exp figures are
reported separately and not combined: this is a strong-lit / zero-exp claim, the mirror of the
novel-discovery quadrant.

Tag accuracy: `claim_ids` is exactly `["MECH-055"]`, correctly scoped. MECH-035 is deliberately
untagged and MECH-054's benefit-side channel is out of scope -- both confirmed against claims.yaml.

## 3. Biological reference

Closest mechanism: BLA valence-specific projections carrying affective LEVEL (Namburi 2015)
versus dACC surprise / prediction-error signalling (Hayden 2011), with wanting/liking separable
inside the valence channel (Berridge 2009). Five literature entries were pulled 2026-09-19.

This is a **faithful biological translation, not a formal-definition import** -- the REE pair
(residue-field valence tag vs dACC-consumed forward-model residual) maps onto a genuinely
dissociable mammalian pair. **No biology divergence and no `/lit-pull` commission is owed.**
The failure does not resemble a missing biological dependency; it resembles a manipulation that
did not deliver the perturbation it was designed to deliver.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact -- untested** | decisive falsifier never scored |
| Biological reference | **clear** | lit already present; no divergence |
| Prerequisites | **present** | every readiness floor met on the green arm; `harm_a_forward_r2` 0.932-0.977 in EVERY cell incl. the red arm (floor 0.30) |
| Implementation | **complete** | four axes computed, forward model trained, accumulation trap avoided, F1-F7 applied |
| Environment | **wrong pressures -- SCHEDULE** | the shift ran from step 0 of P0, so the trained-then-shifted premise was never instantiated at any dose; exposure also ran ~4.28x |
| Measurement | **partial** | harm-forward ACTION-sensitivity never instrumented (no persistence baseline); precision leg pinned at cap ~95% of ticks; scored series 226-1784 (7.9x spread) |
| Integration | **coupled but inert -- BY STARVED UPSTREAM** | channels live and responsive; the decoupling manipulation never supplied the residual perturbation. Implementation NOT downgraded on this account. |
| Scale / capacity | **likely insufficient** | 0.84 s CPU/step forced dropping the interval-25 rung |

### Failure-location summary (GOV-FAILLOC-1)

**MIXED -- ENVIRONMENT primary (mis-SCHEDULED experimental pressure), with a MEASURES
contribution. Not chargeable to REE, and not chargeable to MECH-055.**

`mechanism: established` / `measures: partial` / `environment: not_established` / `ree: false`.

MECHANISM reads `established` per the mechanical table, because Implementation completeness is
`complete` and the lever mis-scheduling is an experiment-DESIGN defect rather than an
implementation defect in `ree_core`. Note separately that no mechanism VERDICT exists either way,
since C1 was never scored. (An earlier draft recorded `not_established` here; the red-team
correctly identified that as internally inconsistent with the Implementation row.)

## 5. The central adjudication: the manipulation was mis-SCHEDULED, not mis-dosed

Two separate errors sit on top of each other. The first is the run's own; the second was this
autopsy's first draft, withdrawn on the red-team finding and recorded here so a successor does not
retry it.

### 5a. The run's stated remedy is unsupported

The run routes `substrate_not_ready_requeue` -- correct -- and then prescribes: *"Re-queue under a
NEW letter at an adequate P0."* That remedy is not supported by its own data.

- P0 is the encoder-warmup phase (`P0_EPS = 30`), sized on measured CPU cost, not on any
  convergence criterion. "adequate" appears exactly once in the 1826-line driver -- in the routing
  string itself -- and is never operationalised.
- Neither failing precondition is a function of warmup length.
- `harm_a_forward_r2` was 0.932-0.977 in every cell including the failing arm (floor 0.30).
  (Strictly, that figure certifies **P1's** product, `e2_harm_a`, not P0's -- so it is corroborating,
  and the argument rests on the structural point above.)

### 5b. The actual root cause: the shift ran during training

**`world_rule_shift` was live from step 0 of P0, not enabled after training.** Verified directly:

- `_make_env(seed, interval)` is called exactly **once per cell, at `driver:643`**, *before* the
  P0+P1 training loop, and sets `world_rule_shift_enabled=(interval > 0)` at construction
  (`driver:459`). `world_rule_shift_enabled` appears nowhere else in the driver -- there is no
  toggle at the P1->P2 boundary.
- The shift fires inside `env.step()` (`causal_grid_world.py:2520`) on a cumulative counter whose
  own comment reads *"Cumulative step counter that does NOT reset on reset()"* (`:984-985`), and
  `_action_map` / `_world_rule_shift_count` are *"DELIBERATELY NOT reset here ... Permutations
  accumulate across episodes"* (`:1879-1885`).
- P0 30 eps + P1 60 eps x <=90 steps = up to 8,100 training steps at interval 10 -> **up to ~810
  accumulated depth-2 permutations before P2 begins.**

So the harm-forward model was *trained under continual permutation*. It learned an
action-marginalised predictor from the outset, and P2 then presented it with exactly the regime it
was trained on. **The lever's premise -- a learned stable map made "systematically wrong ... until
re-learned" -- was never instantiated at any dose.**

The manifest carried the signature all along: `harm_a_forward_r2` is **statistically
indistinguishable between arms** (0.932-0.954 shift vs 0.940-0.977 stationary) *despite* ~810
permutations during the shift arm's training. A model for which action-conditioning mattered could
not match a stationary-trained one under that regime.

### 5c. What the first draft got wrong, and why it matters

This autopsy's first draft read that equality as *"the dose failed to perturb the model"* and
prescribed a **multi-rung dose ladder** (intervals 0/100/50/25/10). That prescription is withdrawn.
A same-schedule ladder inherits the confound at **every rung** and aliases three live readings to
one flat-residual verdict:

- **H1** exposure and forward-model error are structurally coupled under this lever;
- **H2** the model adapted because it *trained* under the shift;
- **H3** the harm-forward model is persistence-dominated (`harm_history_len=10`; `z_harm_a` is a
  slow harm-history latent), so no action-map lever at any dose can raise its residual.

At the measured 0.84 s/step that would have been ~9 h of compute returning the same unevaluable C1.
The same sentence the draft aimed at the run's own remedy -- *"would spend another run reproducing
the same failure"* -- applied to the draft's own remedy.

### 5d. A supporting design-time root

The `pe_load_elevated_vs_stationary` precondition justifies itself by citing V3-EXQ-861e's
`ecological_novelty_mel_gradient_present_this_config` -- **a MEL-gradient DV, not the dACC harm-PE
it gates on.** No prior run has ever measured whether this lever moves *this* channel. The
precondition's premise was untested on its own DV.

What the shift *did* reach: mean E3 running precision fell **3.2x-6.5x** under shift. The lever
perturbs the world/E3 side without reaching the harm-forward side -- itself informative about what
it touches.

## 6. Instrument findings

1. **The design-time unsatisfiability guard was inert.** `assert_no_structurally_unsatisfiable_gate`
   runs under `--dry-run`, but detects only through `structural_max` / `structural_min` lambdas,
   and **none of this driver's eight `PreconditionSpec`s declares either**. It could not fire.
2. **The smoke could not have warned.** Under `--dry-run` the P2 budget is 60 steps while
   `FRESH_TICKS_MIN = 200`, so every arm is guaranteed red; and `CORR_MIN_N = 100` forces every
   routed statistic to NaN. The smoke therefore emitted `outcome=FAIL
   label=substrate_not_ready_requeue` -- **bit-identical routing to the real run** -- while
   carrying zero information about whether the real gate would pass.
3. **The precision leg ran far above its cap.** `mean_e3_precision` 24,872-250,856 against a
   saturation point of 15,000 (`prec_norm = min(precision/5000, 3.0)`); `mean_prec_norm` pinned
   2.93-3.00. The design-time red-team predicted the opposite regime (~95, a ~1.02 multiplier) --
   a 260x-2600x miss. The driver's scale-invariance argument means no verdict changes, but the run
   cannot speak to precision-weighting at all. `mean_prec_norm` is emitted per row and **not**
   rolled into the flat readout where a reader would see it.
4. **Emitted stale text.** `dv_symmetry_note` asserts the symmetry statement holds "for all three
   arms" while `full_config["arms"]` carries two. The manifest tells a reader there were three.
5. **`substrate_stable_across_run: false` over-reads.** `per_cell_hashes_disagree` is false with
   exactly one distinct cell hash -- every cell ran on one substrate. The flag reflects post-run
   **disk** drift on the worker between fingerprint resolution (15:02:37Z) and manifest write
   (17:52:12Z), not in-run instability. A reader should not discard this run on that flag.
6. **Heterogeneous statistical power inside the scored arm.** The commitment latch consumed 0% of
   ticks in seed 42 but 87% in seed 2026; scored series run 226-1784 points, and the worst cell
   clears the 200-selection floor by 19%.

## 7. Interpretable signal (stated before recommending non_contributory)

This FAIL is **not** information-free:

1. On the green stationary arm the load-bearing falsifier (i) criterion **C2 PASSED** (max
   pairwise axis R^2 0.271 vs a 0.8 ceiling, 3/3 seeds), and the unrouted harm-channel
   correlations were 0.215-0.493 against a 0.9 redundancy threshold. That is evidence against the
   collapsed-harm-scalar reading **at rest** -- though not under the decoupling manipulation the
   claim's falsifier (ii) requires, so it does not discharge C1.
2. The two channels **did** dissociate: `mean_valence_harm_delta` fell 54% under shift while dACC
   PE stayed flat. This cannot be credited, because the exposure premise for reading it was
   vacated -- but it is the direction a successor should expect.
3. The `world_rule_shift` lever is now characterised at one dose: it moves exposure, not
   forward-model error.

## 8. Re-derive brake and recurrence

**Brake does NOT fire.** 0 prior autopsy targets tag MECH-055 across 532 artifacts. Canary:
SD-003 at 74, MECH-090 at 33 -- the scan reaches `targets[].claim_ids`, so the zero is real. The
one corpus mention of MECH-055 is a dependency co-mention in
`failure_autopsy_V3-EXQ-963a_2026-09-02.json`, not a target tag. The driver's own embedded count
agrees (0). This is the **first autopsy on MECH-055**.

**Granularity-debt trigger: does NOT fire** (`granularity_debt_cluster.py MECH-055` -> 0 targets
across 0 files). A first autopsy cannot show recurrence.

## 9. Routing

**`/queue-experiment` -- re-queue as V3-EXQ-1062a** (alphabetic suffix: same scientific question,
implementation fix). Node class: `complex (probe-gated) / puzzle (known rules)`.

The successor must, **in order**:

1. **Fix the onset.** Train P0/P1 on the **stationary** env and enable the shift only at the P2
   boundary, by setting `env.world_rule_shift_enabled / _interval / _depth` after the training
   loop. These are public attributes -- **no substrate change is needed.**
2. **Instrument H3.** Carry a **persistence-baseline R^2** (`z_pred = z_harm_a(t-1)`, computed on
   the existing `r2_pairs` at zero extra env cost) as a readiness instrument, so a
   persistence-dominated harm-forward model is *measured* rather than assumed.
3. **Only then** ladder the dose -- and only if (1)+(2) show the residual can move at all.

Also fold in: declare `structural_min` on `fresh_select_sample_floor` so the design-time guard is
no longer inert; roll `mean_prec_norm` into the flat readout; fix the "all three arms" note.

**Explicitly NOT recommended:** lengthening P0 (section 5a), and a same-schedule multi-rung dose
ladder (section 5c -- this autopsy's own withdrawn first draft, recorded so it is not retried).

**GOV-FANOUT-1: no `fanout_recommendation` emitted, and the exemption is claimed on the RE-POSED
design only.** A same-schedule dose ladder would have been a power-bump of the braked design and
would have aliased H1/H2/H3 to a single verdict. The re-posed successor moves on the **schedule**
axis and adds a **measurement** instrument that discriminates H3 directly, so it is one unambiguous
design fix rather than a portfolio. Flagged as a judgement call.

**Substrate:** `amend` `SD-PP-B4-one-shot-world-rule-shift-lever` -- first entry in its currently
empty `failure_record`, severity `degrading`, paths
`ree_core/environment/causal_grid_world.py::_maybe_shift_world_rule`, and **add MECH-055 to its
`unblocks_claims`**. The record is written as an **ONSET** gap, which is exactly that entry's
registered subject ("one-shot world-rule shift has no env kwarg; modulo-schedule only") -- so the
`amend` target is right, though the first draft reached it for the wrong reason (it had written the
record as a *dose* gap, which did not match the entry's subject).

`degrading` is set deliberately, not left unset: the modulo schedule is **correct** behaviour for
its registered consumers (861e-class MEL producers) and does not make their evidence look
valid-but-false, which rules out `corrupting`; but it is a real, generalisable hazard for any
consumer using the lever as a post-training decoupler, which other experiments should see as a WARN.

**Claim layer:** direction `non_contributory`, category `standard` (both unchanged); what must
actually be applied is `diagnostic_evidence_adjudicated: true`, which MECH-055 does not carry
(verified: absent, while 47 of 1180 claims do carry the field, so the absence is meaningful).
`pending_retest_after_substrate: false` -- see the judgement call below.

**Category note for governance:** MECH-055's own `what_would_answer` flags that a stricter reading
could argue `substrate_conditional`. This autopsy does **not** recommend that move: it would put
MECH-055 into `_EPI_SUPPRESS_PROPOSAL` and mark it not-v3-testable, starving it of experiment lanes,
while the claim itself states a narrowed test can run now.

### Two judgement calls flagged for the user

- **`pending_retest_after_substrate: false`** is a deliberate deviation from the default pairing of
  a `non_contributory` reading with that flag. A retest **is** owed (V3-EXQ-1062a), but it is not
  gated on a build -- the onset fix uses public attributes that exist today. Setting the flag true
  would misroute the IGW workset's `_retest_blockers` into waiting for substrate work that nobody
  owes. `narrow_supports_flag: true` is set: MECH-055's only remaining support is literature
  (5 entries, exp_conf 0.0), which is narrow and single-pathway.
- **GOV-FANOUT-1 exemption** as argued above.

## 9b. Red-team record (Step 7c)

**Model: `fable`** -- cross-model, this session drafted on Opus 5. **Verdict: CONTESTED.**

The contested finding is F1 (section 5b/5c): the draft charged the failure to manipulation *dose*
and prescribed a dose ladder. **Independently verified by this session before acceptance** -- one
`_make_env` call at `driver:643` preceding the training loop, `world_rule_shift_enabled` set only
at `driver:459` with no P2-boundary toggle, and the `causal_grid_world.py:984-985` / `1879-1885`
non-reset comments reading as quoted. **Accepted**: the environment narrative, the
`failure_record_entry`, and the successor prescription are all revised above.

It did **not** move: `evidence_direction` (`non_contributory` stands), the claim-layer
recommendation, or the brake.

Targets it tried and that **held**: P0 not the binding constraint (on the structural argument);
C2's PASS is conservative (small n *and* lag-1 autocorrelation of 0.989 both inflate OLS R^2 toward
an **upper** ceiling, so passing is harder); the precision cap changes no verdict (between-arm
multiplier bias recomputed at 0.47%, de-biased PE rel-change ~ -0.029, still below the +0.05 floor;
`dacc_saturation_enabled` and `dacc_pe_cap` both off); the change-tail is storable and not already
true; brake count 0 with canary SD-003 at 74.

Hygiene items accepted and applied: the `failure_location.mechanism` inconsistency (now
`established`); pooled-mean prose that hid per-seed sign flips (now per-seed); "4-6x" corrected to
3.2x-6.5x; the C2 at-rest caveat moved into `failed_criterion`; the artifact count corrected 532 ->
533.

## 10. Frozen hypothesis-space ledger (Step 9b) -- NO ACTION OWED

Checked read-only against `evidence/planning/hypothesis_space_registry.v1.json`:
**64 questions scanned** (canary: `competence_floor`, `conversion_ceiling_root`,
`da_density_approach`, `inv088_diversity_readout`, `ceiling_vs_driver` -- the scan reaches
`questions[]`, so the zero below is a real zero).

- **No question carries MECH-055 in its `claims`.** Six questions keyword-match on
  affect/valence/channel-separation, but all belong to other claims -- the nearest,
  `arc021_channel_separation_necessity`, is ARC-021 / MECH-069.
- This autopsy emits **no `fanout_recommendation`** (section 9), so Mode A does not apply.
- The adjudicated leg is a **non-discriminating** `non_contributory`, which under the Mode B state
  mapping leaves a leg `alive` with state unchanged -- there is nothing to resolve.

**No registry write is owed, and none was made.** This matters procedurally: the registry is
currently held by an active claim from another session (`compassionate-pike-fe9174-autopsy`,
opened 2026-09-22T18:39:39Z for V3-EXQ-1073), so this autopsy had no write access to it. Because
no ledger action is owed, that contention costs nothing here -- but a successor that DOES emit a
fan-out for MECH-055 will need to open a new question, and should re-check contention first.

## 11. Contention and provenance notes

- **V3-EXQ-1073 is NOT covered by this artifact.** `task_claim.py open` arbitrated this session
  OUT of the 1073 artifacts and the registry, in favour of `compassionate-pike-fe9174-autopsy`
  (claimed 18:39:39Z, three minutes earlier) -- the session that ran the MECH-572 experiment and
  therefore holds its context. Reported rather than duplicated.
- **`pending_review.md` could not see V3-EXQ-1073**: it was generated at 18:26:25Z and that
  manifest landed at 18:28:56Z. The scope for this autopsy was taken from a direct manifest scan
  (1,065 files, 0 parse errors), not from the committed derived file.
- **The derive chain was deliberately NOT re-run.** `generate_pending_review.py` and
  `governance.sh` were both mid-edit by a concurrent session at scoping time, and a `/governance`
  cycle held a scope claim on `REE_assembly/evidence/`. Regenerating would have executed a
  half-edited script against a contended tree; scope was derived from manifests instead.
- **Coordination-plane pause:** already in force via the live `/governance` session
  (`gov-20260922-1756`), so this session's own pause claim correctly lost arbitration and none was
  needed.
- **No run pack exists for this run**, so it is currently inert to claim scoring
  (`claim_evidence.v1.json` still shows `exp_posterior.n_entries: 0` for MECH-055) regardless of
  what governance applies.
