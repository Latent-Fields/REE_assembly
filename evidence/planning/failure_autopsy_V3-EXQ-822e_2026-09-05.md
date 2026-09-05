# Failure autopsy -- V3-EXQ-822e (SD-082 candidate-discriminating bias, spread-valued DV)

- **Status:** `confirmed` -- drafted headless on behalf of governance session `governance-20260905`,
  red-teamed cross-model at Step 7c (verdict **CONTESTED**), and ratified at the Step 8 human gate.
- **Generated (UTC):** 2026-09-05T09:56:19Z
- **Confirmed (UTC):** 2026-09-05T10:59:11Z, by `governance-20260905 (user gate, inline route A)`
- **Scope:** single
- **Run:** `v3_exq_822e_sd082_candidate_discriminating_bias_spread_20260905T025644Z_v3`
- **Queue id:** V3-EXQ-822e (`supersedes` V3-EXQ-822d) -- `experiment_purpose: evidence`
- **Claims:** SD-078, SD-082 (both `candidate_substrate_landed`, `epistemic_category: standard`,
  `pending_retest_after_substrate: false`)
- **Outcome:** FAIL, `evidence_direction: unknown` (per-claim unknown/unknown),
  `non_degenerate: false`, self-route `substrate_not_ready_requeue`
- **Ran:** 2h04m on `ree-cloud-2`, machine class `linux-x86_64-py3.10-torch2.12.0+cpu`,
  substrate hash `db37d602026bc63a0216c1169e0e54d42798d42c278df8404dc7356835ea54fd` (identical
  across all ten cells of this run). That hash **differs** from 822d's (`0944cbbe...`) even though
  822d's and 822e's P0-P2 outputs are bit-identical -- the hash folds the driver and config, not
  `ree_core` alone, so the difference does **not** mean the substrate moved between the two runs.
- **Dry-run gate:** checked, clean. `excluded_dry_run_ids: []`; the target manifest carries no
  truthy `dry_run` and every cited run (822, 822a, 822b, 822c, 822d, 822e) is a full-budget run.
- **Disposition:** `non_contributory` on **both** claims, `epistemic_category: standard` on both --
  held at the gate. Nothing promotes; nothing demotes.

**Headline.** The run's verdict is void, and -- after the red team -- its *scientific content* is
weaker than the draft claimed. Two independent findings, both load-bearing:

1. **The verdict is instrument-voided.** One of nineteen readiness preconditions failed, and that
   precondition is a statistic two prior confirmed autopsies had already written down as
   mis-specified -- promoted, unrepaired, from a diagnostic flag to a gate by this letter's own
   red-team pass.
2. **The criteria that passed cannot be credited to training.** C1 and C2 have no init-head
   control, and a *random-init* head of this driver's exact shape clears C1's floor in 99% of
   Monte-Carlo trials. Repairing the gate would therefore not have produced a usable `supports`.

And a third fact that governs the routing: **822e is a bit-for-bit deterministic replay of 822d**,
so its FAIL was arithmetically certain at queue time and a byte-identical successor would buy
nothing.

---

## 1. Facts (no interpretation)

### 1a. What the run measured

822e replaces 822d's dependent variable, on the instruction of the ratified cluster autopsy
`failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30` (REE_assembly `40dd17331e`,
governance-ratified `54dbe477be`). The new DV is `prop_ratio_raw` -- the cross-candidate
range / mean-abs of the **raw pre-tanh** propagated action bias, read at the raw stage because the
consumer's `bias_scale*tanh(raw/bias_scale)` output stage manufactures apparent cross-candidate
range out of a perfectly uniform raw shift. The raw stage is recomputed from the substrate's own
head and cross-checked each tick against the substrate's real output inverted through
`atanh`; the residual is itself a readiness gate.

Design: 5 seeds (101/202/303/404/505) x 2 arms (`ARM_ON` / `ARM_OFF` on `crf_cue_centering`,
SD-078's rule-pool knob). SD-082's own fix (`candidate_summary_source="proposer_post_action"`)
is passed **unconditionally in both arms**, so C1/C2 are absolute criteria applied identically in
both, and the ON/OFF contrast (C4) belongs to SD-078 alone.

### 1b. Criteria, as scored

| Criterion | Claim | Load-bearing | Result | Number |
|---|---|---|---|---|
| C1 raw discrimination index, ARM_ON, per-seed median >= 1.0 on >= 3/5 seeds | SD-082 | yes | **PASS** | 4/5 seeds; `mean_median_ratio` 1.846; worst seed 0.985 |
| C2 pooled argmax-flip fraction >= 0.02 | SD-082 | yes | **PASS** | 0.0583 (107 flips / 1834 ticks) |
| C4 SD-078 index contrast: ON-OFF >= 0.25 on >= 4/5 seeds **and** mean >= 0.25 | SD-078 | yes | **FAIL** | seed clause **passed** 4/5; mean clause **failed** at 0.0541 |
| C1b same floor on ARM_OFF | -- | no (reported) | pass | 4/5 seeds; `mean_median_ratio` 1.792 |
| C3 legacy magnitude floor, both arms | -- | no (diagnostic) | fail to discriminate | `legacy_floor_discriminates: false`, `legacy_contrast_mean` -3.56e-4 |
| C5 post-tanh spread | -- | no (diagnostic) | pass | ON 2.153e-3 / OFF 2.704e-3 |

`overall = ready AND c1 AND c2` (driver L1548). `criteria_non_degenerate` is **true** for C1, C2
and C4 individually.

**Read the two PASS rows with Section 3b in hand.** C1's and C2's bars are *absolute floors with no
untrained reference*, and Section 3b shows an untrained head clears both. They are not evidence
about training.

### 1c. Readiness: 18 of 19 met

Met: z_world cone (worst 0.960 vs 0.90 floor) - ON pool differentiated / OFF pool pinned -
ON rule active - prop-sample sufficiency (worst cell 145 against a floor of 20) - fix engaged
(worst summary spread ratio 2.702e-3 vs 1e-3 floor; **0** manual fallbacks; **0** degenerate
centering ticks) - spread measurable - no degenerate tick - dispatch engaged - capture active -
head-diag sufficient - raw replica matches substrate (worst atanh residual 5.96e-8) - uniform
negative control reads as uniform (`uniform_control_ratio_worst` **0.000** in every cell) -
control probes sampled - flip resolution (1834 >= **200**, the manifest's `flip_ticks_floor`; the
50 quoted in the driver's prose comment is not the gate -- 1834 clears both) - and **all three
`dv_headroom` gates** (`raw_discrimination_index` 4.482 vs 2.0, headroom 2.24x;
`argmax_flip_fraction` 1.0 vs 0.04, 25.0x; `sd078_ratio_contrast` 3.891 vs 0.5, 7.78x).

**Not met -- the only one:** `bias_head_actually_trained`. `last_layer_weight_delta_worst`
= **-0.003772** at cell `ARM_OFF/seed101`, against `LAST_LAYER_WEIGHT_DELTA_FLOOR = 1e-3`,
`direction: "lower"`.

Consequence (driver L1631-1634): `label = "substrate_not_ready_requeue"` and
`dir_082 = dir_078 = overall_dir = "unknown"`. No claim direction survives the conjunction.

### 1d. The ten cells' last-layer weight-norm deltas

`last_layer_weight_delta_init_to_p1 = post_p1.last_linear_weight_norm - init.last_linear_weight_norm`
(driver L1164-1166), aggregated by `_worst_cell(..., mode="min")` (L1402-1404).

| cell | init norm | post_p1 norm | delta (signed) | \|delta\| |
|---|---|---|---|---|
| ARM_OFF/101 | 0.14822289 | 0.14445074 | **-0.00377215** | 0.00377215 |
| ARM_ON/101 | 0.14822289 | 0.14614676 | **-0.00207613** | 0.00207613 |
| ARM_OFF/202 | 0.13874765 | 0.14582394 | +0.00707629 | 0.00707629 |
| ARM_ON/202 | 0.13874765 | 0.14489892 | +0.00615127 | 0.00615127 |
| ARM_OFF/303 | 0.13077457 | 0.14449343 | +0.01371886 | 0.01371886 |
| ARM_ON/303 | 0.13077457 | 0.13907506 | +0.00830048 | 0.00830048 |
| ARM_OFF/404 | 0.14622717 | 0.14879671 | +0.00256954 | 0.00256954 |
| ARM_ON/404 | 0.14622717 | 0.14847751 | +0.00225034 | 0.00225034 |
| ARM_OFF/505 | 0.15451919 | 0.16571026 | +0.01119107 | 0.01119107 |
| ARM_ON/505 | 0.15451919 | 0.16011803 | +0.00559884 | 0.00559884 |

Minimum `|delta|` across all ten cells: **0.00207613**, i.e. **2.08x** the 1e-3 floor.
ON-arm mean signed delta (the sibling diagnostic's input): **+0.00404496**.

### 1e. 822e is a bit-for-bit deterministic replay of 822d

Every one of the **28 per-cell statistics the two manifests share is identical, in all ten cells**
(`crf_*`, `hidden_dead_relu_frac_p2_*`, `last_layer_weight_delta_init_to_p1`, `n_prop_samples`,
`prop_delta_mean`, `rule_flip_frac`, `rule_state_diff`, `rule_state_norm_p2_median`,
`summary_spread_ratio_p2_*`, `zworld_cone_min_cosine`, and every counter -- 28/28 identical, 0
differing). Both runs: `ree-cloud-2`, `linux-x86_64-py3.10-torch2.12.0+cpu`, config p0/p1/p2 =
60/70/40, seeds 101-505. P0, P1 **and** P2 replayed exactly; 822e only *added* new DVs
(`prop_ratio_raw`, the controls) computed on the same P2 ticks.

This is a fact about the run, not an interpretation, and it has three consequences worked out in
Section 3c: the FAIL was predictable at queue time, the draft's proposed 822f was a re-print, and
SD-078's `inconclusive` is predetermined for any same-seed re-run.

### 1f. Recording provenance

Always-core present: `recording_schema`, per-cell `arm_fingerprint.substrate_hash`, `machine` /
`machine_class`, `elapsed_seconds`, `config`, explicit `seeds`. Per-cell `head_diag_by_phase`
carries `init` / `post_p0` / `post_p1` / `post_p2` norms. **There is no recording gap** -- the
recording was good enough for the run to diagnose itself *and* good enough for a third party to
falsify the draft's diagnosis offline (every readiness input sits in `per_seed_rows`, and 822d's
manifest is bit-comparable).

---

## 2. Claim layer

| | SD-078 | SD-082 |
|---|---|---|
| type | design_decision | design_decision |
| status | candidate_substrate_landed | candidate_substrate_landed |
| epistemic_category | standard | standard |
| implementation_phase | v3 | v3 |
| pending_retest_after_substrate | false (cleared 2026-08-30) | false (cleared 2026-08-30) |
| substrate_queue entry | none | SD-082, `implemented_pending_validation`, ready false, severity `corrupting`, `validation_experiment: V3-EXQ-822d`, 5 failure records (822/822a/822b superseded, 822c resolved, **822d open**) |

**Did the experiment let the claims express themselves?** SD-082: it recorded the numbers, but
after Section 3b the honest answer is **no** -- the criteria it recorded them against do not
separate SD-082's mechanism from the head's initialisation. SD-078: only through C4, which is
correctly attributed (Section 4) but under-powered on its mean clause and joint with SD-082's
uncreditable readout.

**`claim_ids` accuracy.** Both tags are correct. SD-082 is the subject. SD-078 is a co-tag whose
knob is the arm axis -- the driver says so in terms ("SD-078 IS A CO-TAG, NOT THE SUBJECT") and the
822d cluster autopsy established the same reading.

**Note on `claims.yaml` state at read time.** `docs/claims/claims.yaml` did not parse in the
working tree at draft time (`yaml.scanner.ScannerError: mapping values are not allowed here`, line
74376, inside an unrelated `v4_v5` aspect-closure entry). SD-078 and SD-082 were read textually and
are structurally intact. The committed HEAD copy parses cleanly, so this is another session's
uncommitted working-tree edit, not a landed break. Flagging it for governance -- this autopsy made
no edit to the file.

---

## 3. The defect

Three parts. **3a** is the sign-convention defect the draft found. **3b** is the deeper defect the
Step 7c red team found, which survives repairing 3a and is what withdraws the draft's read-across.
**3c** is the replay fact that governs the routing.

### 3a. The statistic is not the quantity the gate names (sign convention)

The gate is called `bias_head_actually_trained` and its own description says it certifies that the
head trained ("Without it, the cross-candidate structure that a random first layer plus ReLU
already possesses could be reported as a trained coupling", driver L1912-1924). The quantity
actually computed is the **signed difference of two L2 norms**:

```python
# L1164-1166
last_layer_weight_delta_init_to_p1 = float(
    head_diag_by_phase.get("post_p1", {}).get("last_linear_weight_norm", 0.0)
    - head_diag_by_phase["init"]["last_linear_weight_norm"])

# L1402-1404
last_layer_worst, last_layer_cell = _worst_cell(
    rows, "last_layer_weight_delta_init_to_p1", mode="min")
head_trained = bool(last_layer_worst >= LAST_LAYER_WEIGHT_DELTA_FLOOR)
```

Movement is `||W_p1 - W_init||`. The reverse triangle inequality gives
`||W_p1 - W_init|| >= | ||W_p1|| - ||W_init|| |`, so a **negative** delta of -0.003772 is not
evidence of a static head -- it is a **lower bound of 0.003772 on how far the weights moved**,
3.8x the gate's own floor. Taking the `min` of the *signed* quantity and testing it with
`direction: "lower"` therefore fails exactly the cells that trained inward, and only those.

**Every cell clears the floor on `|delta|`.** Min `|delta|` = 0.00207613 (Section 1d).

**Three independent corroborations that ARM_OFF/seed101's head moved.** In that same cell the
first-layer weight norm rose 3.24391580 -> 3.25520253 (+0.01128673), the first-layer bias norm rose
0.40546107 -> 0.41057566 (+0.00511459), and the last-layer **bias** norm rose 0.03551145 ->
0.04040926 (+0.00489781). Adam carries no weight decay here (`weight_decay` absent, default 0;
driver L961-962), so the norm shrink is not regularisation. The optimiser demonstrably stepped.

**The driver disagrees with itself inside one manifest.** Below the gate, the sibling diagnostic
computes an absolute form and reads the head as trained:

```python
# L1582-1584
"head_untrained_last_layer_static": bool(
    abs(on_last_layer_delta) < LAST_LAYER_WEIGHT_DELTA_FLOOR),
```

`diagnostic_flags.head_untrained_last_layer_static` is **false** while `readiness_head_trained` is
also **false** -- the two mean opposite things and disagree. **But the "cheap lint" reading is
weaker than the draft claimed** (red-team hygiene H6): the two differ in **quantifier** as well as
sign -- the gate takes the `min` over all ten cells, the sibling takes the ON-arm **mean** -- and a
*signed* ON-arm mean (+0.004045) would also have passed. The lint would have fired here; it does
not isolate the sign as the cause.

**This was known, twice, in writing, before the run.**

- `failure_autopsy_V3-EXQ-822c_2026-08-29` (confirmed, user-adjudicated), measurement defect (i):
  "The headline flag is computed from a DIFFERENCE OF NORMS ... not a parameter distance
  `||W_p1 - W_init||`, so it cannot distinguish 'the weights did not move' from 'the weights
  rotated at constant norm' -- and rotation is exactly what a REINFORCE readout would do." Its
  defect (ii) additionally warned that the signed form "permits cross-seed cancellation ... latent
  here but a real trap."
- `failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30` (confirmed, user-gated
  2026-08-30T15:41:56Z): "Carried-forward defect: 822c's documented measurement defect #1
  (last_layer_weight_delta computed as a difference of NORMS, so rotation at constant norm reads as
  zero) is unfixed -- the ARM_OFF seed-101 value is **-0.003772**, which a movement measure cannot
  be." That is the identical cell and the identical number.
- 822e's own Step-4.5 red team then **promoted** it: from the queue entry note, "'the bias head
  actually trained' promoted from a diagnostic flag to a readiness gate."

Neither prior autopsy emitted a routable repair item for it. The corpus's memory of the defect was
prose only, so the promotion had nothing to collide with.

**Scoping, a second-order defect.** The gate is quantified over the **minimum of all ten cells**,
including the pool-control arm. C1 gates on `ARM_ON` alone -- and 822e's red team moved C4's
headroom out of run-level readiness precisely so that "a genuine SD-078 null cannot void an SD-082
result". The same reasoning was not applied to this gate, so `ARM_OFF` holds a veto over `ARM_ON`'s
absolute criteria. Both cells that failed are seed 101 (ON as well as OFF), so arm-scoping alone
would not have saved this run -- but the asymmetry is real and should be fixed alongside the
statistic.

### 3b. No movement floor can do what the gate's NAME says -- and a random head clears C1

> **WITHDRAWN at the Step 8 gate.** The draft asserted that "the gate's stated intent is certified
> in all ten cells" from `|delta|`. That is false, and the correction is the load-bearing change in
> this artifact. Recorded rather than deleted, because the withdrawn claim was the draft's whole
> argument for a cheap re-run.

Repairing 3a's sign convention turns the gate into a *correct optimizer-liveness check* -- it would
catch the 822b failure mode, where `post_p1 == init` exactly. It does **not** turn it into the test
its own text names. The arithmetic:

- The last layer is `nn.Linear(hidden_dim=32, 1)` -- **32 parameters**
  (`lateral_pfc_analog.py` L155, L254).
- The optimiser is `torch.optim.Adam(..., lr=LR_LPFC_BIAS=5e-4)` with no weight decay
  (driver L554, L961-962). Adam's first-step per-parameter displacement is approximately `lr`
  regardless of gradient scale, so **one** step moves the tensor by about
  `5e-4 * sqrt(32) = 2.83e-3` in Frobenius norm -- **2.8x the 1e-3 floor** -- with up to 70 P1
  steps available (one per P1 episode, L1095-1109).

A gate that any live optimiser passes on step one cannot certify that "the cross-candidate
structure a random first layer plus ReLU already possesses" is not being reported as a trained
coupling. It is a liveness test wearing a trainedness name.

**And the criterion downstream of it has the same problem.** Monte Carlo, 200 trials, a head of the
driver's exact shape at default init (last-layer norm rescaled to the recorded 0.148, `rule_state`
norm 0.19 as recorded, K=32 centered random summaries):

| statistic | random-init head | 822e measured |
|---|---|---|
| raw discrimination index, median | **3.93** | C1 `mean_median_ratio` **1.846** |
| p5 / p95 | 1.68 / 5.41 | worst seed 0.985 |
| fraction clearing C1's 1.0 floor | **0.99** | 4/5 seeds |

(The driver's own iid reference at L1675 is 5.15, consistent with this.) **C1's PASS is *below* what
an untrained head produces**, and C2's argmax flips likewise do not require training. So:

- The read-across "SD-082's substantive result is very likely a PASS" is **withdrawn**. A
  counterfactual PASS would have recorded `supports` for *"the **trained** rule->bias readout
  produces a candidate-DISCRIMINATING raw bias"* on criteria an untrained head satisfies -- the
  exact misreport the gate's author named.
- `non_contributory` now stands on **two** grounds, not one: the instrument-voided gate **and** the
  uncreditability of C1/C2. The second is the one that survives any re-score.
- Open doubt 4 in the draft (seed 101 anomalous on two statistics) is a symptom of the same gap.

**The fix is half-built already.** `_init_positive_control` (driver L682) snapshots the head at
init, and the synthetic probe is already run through the *trained* head. Running that same probe
through the **init** head and scoring `trained - init` is a few lines. A criterion of the form
"index >= absolute floor" can only be read as evidence about training when the floor is calibrated
against the untrained distribution of the same statistic.

### 3c. The FAIL was arithmetically certain at queue time

From Section 1e: P1 was unchanged between 822d and 822e, and the offending value
`-0.003772154450416565` at ARM_OFF/seed101 is **already in 822d's flat manifest** (identical `init`
0.1482228934764862 and `post_p1` 0.14445073902606964) and is **quoted verbatim in the 822d cluster
autopsy** (`.md` L390). With the gate quantified as `min >= 1e-3` over all cells, the 822e readiness
FAIL was computable before the queue entry was written (ree-v3 `be5b413`).

The draft's learning #1/#2 ("a documented defect that is never routed gets promoted") is correct but
understated: the promotion was made **against a manifest that already showed the gate failing**.
That is a queue-time Step-4.5 defect, and it generalises into the standing check now recorded as
learning #1 in Section 7.

---

## 4. SD-078 and C4

**C4 is correctly attributed; the contamination the question anticipates runs the other way.**
What both arms carry unconditionally is **SD-082's** fix. The **arm axis itself is
`crf_cue_centering`, SD-078's own knob**. So an ON/OFF contrast is exactly the right shape for
SD-078 and exactly the wrong shape for SD-082 -- which is why 822e's design puts C4 out of the PASS
conjunction and computes `dir_082` with no contrast quantity in it at all. C4 is not contaminated
by SD-078's fix. (Confirmed by the red team against the manifest: `candidate_summary_source` is
passed unconditionally, not per-arm, and the `combination_rule` says so in terms.)

**What C4's FAIL actually says.** The criterion is a conjunction of a seed clause and a mean
clause. The **seed clause passed**: 4/5 seeds cleared the 0.25 margin (+0.559, +0.775, +1.476,
+0.339). The **mean clause failed**, at `contrast_mean` 0.0541, because seed 101 contributes
**-2.879**. With `contrast_sd` 1.694 over 5 seeds the driver's own
`contrast_t_like_diagnostic_only` is **0.0714** -- a mean indistinguishable from zero at this n.
The driver's design rule (d) is explicit that such a null is not a falsification, and its own
three-valued logic would have emitted **`inconclusive`** for SD-078 (`sd078_headroom_ok` true, `c4`
false, `c4_negative` false; L1644-1651) had run-level readiness passed. Nothing here licenses
`weakens`.

**Three further reasons not to read C4's FAIL against SD-078.**

1. The single dissenting cell, `ARM_OFF/seed101`, is the **same cell** that failed the trainedness
   gate -- and it carries the **highest index in the entire matrix** (4.316) in the arm whose rule
   pool is pinned to one rule (`rule_state_diff` 0.0, `crf_max_live_rules` 1). An anomalous cell on
   two independent statistics at once.
2. C4 is computed on the SD-082 **consumer's own output**, so it is a joint test of SD-078's pool
   *and* SD-082's readout. After Section 3b that readout is not merely unvalidated but
   **uncreditable** without an init control, so a null cannot be attributed to the pool.
3. At `contrast_sd` 1.69 with n=5 the mean clause was never a test SD-078 could pass reliably. The
   successor must **pre-register the SD-078 contrast at a seed count its variance can support**, or
   declare it diagnostic-only -- and emit `inconclusive` by construction rather than a sign read off
   one outlier.

**`inconclusive` is predetermined for a same-seed re-run.** The per-seed contrasts are recorded and
a replay on seeds 101-505 reproduces them exactly (Section 1e), so `inconclusive` is a known output
of the draft's proposed 822f, not something it would test.

Meanwhile SD-078's own differentiation passed decisively as a readiness precondition for the fourth
time: ARM_ON 16 rules, max pairwise distance 1.711, `on_rule_state_diff_mean` 0.6502 against
ARM_OFF's 3.24e-10.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** (both) | The readiness conjunction voided both directions to `unknown` before either claim could be scored -- and the criteria that did pass (C1 4/5 at 1.846; C2 0.0583) are satisfied by an untrained head, so they credit neither claim. C4 failed on its mean clause alone at t-like 0.0714. Neither supported nor weakened. |
| Biological reference | **clear** | Corticostriatal rule-to-action readout; unchanged from 822c/822d. Not implicated; no lit-pull owed. |
| Developmental / dependency prerequisites | **present** | 18/19 readiness preconditions met, all three `dv_headroom` gates met, both in-loop controls fired, the raw-replica cross-check holds to 5.96e-8. |
| Implementation completeness | **complete** (substrate) | The SD-082 amended path is engaged and behaving for a second consecutive run. `ree_core` is not implicated. The incomplete implementation is the driver's instrument -- now on two counts, the gate's sign AND the missing init control. |
| Environment adequacy | **adequate** | Unchanged; not implicated. |
| Measurement adequacy | **misleading** | THE finding, on two independent grounds. (i) Signed difference-of-norms gating a quantity named "trained"; `min` over the signed value; `direction: lower`. (ii) No movement floor can test trainedness on a 32-parameter layer (one Adam step moves it ~2.8e-3), and the discrimination criterion it gates is cleared by a random-init head in 99% of trials. Third, independent point: C4's mean clause is a one-outlier veto over its own seed clause. |
| Integration adequacy | **coupled** | The 822c E2-rollout/PFC-readout contract defect is repaired and stable. |
| Scale / capacity | **adequate for C1/C2 as measurements; insufficient for C4's mean clause** | 5x2 cells, 145-240 ticks/cell, 1834 pooled flip ticks; but `contrast_sd` 1.694 at n=5. (C1/C2's problem is the missing control, not the n.) |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | **not established** -- never scored; the substrate's implementation reads `complete`. |
| MEASURES FAILED | **established** -- the readiness instrument is mis-specified AND the discrimination criterion lacks its control; Measurement reads `misleading`. |
| ENVIRONMENT FAILED | **not established** -- adequate, never implicated. |
| REE FAILED | **false** |

**Net classification: MEASURES -- single bucket, NOT chargeable to REE.** The GOV-FAILLOC-1
precondition for a REE FAILED read (Implementation, Measurement and Environment each independently
adequate) is not met and is not close to met: Measurement reads `misleading`.

### Recommended `epistemic_category`

`standard` for **both** claims -- confirming, not moving, what they already store. **Held at the
Step 8 gate.** The finding is a measurement/instrument defect with a named, bounded, driver-local
fix. Reaching for `substrate_ceiling` or `substrate_conditional` here would put both claims into
`_EPI_SUPPRESS_PROPOSAL` and strip their v3-testable lane on the strength of an instrument that was
never validated against its own null.

---

## 6. Re-derive brake (R1-R3 recount, verbatim)

Recipe run 2026-09-05 over every `status: confirmed` `failure_autopsy_*.json`. **Independently
re-run by the cross-model Step 7c red team, which reproduced both counts exactly, run for run.**

**SD-082 -- prior counted hits: 3**

```
RUN v3_exq_822b_sd082_head_internals_diagnostic_20260727T180919Z_v3
   latest: failure_autopsy_2026-07-28-sweep.json | cat=competence_implementation_gap | sqe_action=amend | dir=non_contributory | COUNTS=True
RUN v3_exq_822c_sd082_candidate_summary_fallback_fix_20260829T065645Z_v3
   latest: failure_autopsy_V3-EXQ-822c_2026-08-29.json | cat=standard | sqe_action=amend | dir=non_contributory | COUNTS=True
RUN v3_exq_822d_sd082_post_action_summary_validation_20260830T144323Z_v3
   latest: failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30.json | cat=standard | sqe_action=amend | dir=non_contributory | COUNTS=True
COUNT: 3
```

**SD-078 -- prior counted hits: 5**

```
RUN v3_exq_822_sd078_rule_selection_consumer_20260726T112152Z_v3
   latest: failure_autopsy_816c-822_2026-07-26.json | cat=precondition_unmet | sqe_action=create | dir=non_contributory | COUNTS=True
RUN v3_exq_822a_sd078_rule_selection_consumer_20260726T145526Z_v3
   latest: failure_autopsy_batch-822a-826-817a-827_2026-07-26.json | cat=competence_implementation_gap | sqe_action=amend | dir=non_contributory | COUNTS=True
RUN v3_exq_822b_sd082_head_internals_diagnostic_20260727T180919Z_v3
   latest: failure_autopsy_2026-07-28-sweep.json | cat=competence_implementation_gap | sqe_action=amend | dir=non_contributory | COUNTS=True
RUN v3_exq_822c_sd082_candidate_summary_fallback_fix_20260829T065645Z_v3
   latest: failure_autopsy_V3-EXQ-822c_2026-08-29.json | cat=standard | sqe_action=amend | dir=non_contributory | COUNTS=True
RUN v3_exq_822d_sd082_post_action_summary_validation_20260830T144323Z_v3
   latest: failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30.json | cat=standard | sqe_action=amend | dir=non_contributory | COUNTS=True
COUNT: 5
```

**Verdict: the literal prior counts meet the threshold (3 and 5 against N=2) and the brake DOES NOT
FIRE.** The draft gave three grounds; **two are withdrawn** and the release now rests on one.

### 6.1 The one honest ground

**The counted hits are a bookkeeping artefact of `amend` being used for failure_record appends.**
Every counted hit qualifies because its `recommended_epistemic_category` is
standard / competence_implementation_gap / precondition_unmet (none an instrument marker) and its
`sqe_action` is `create` or `amend`, so `owes` is true and the R3(4) direction fallback applies. But
look at what those `amend`s actually did:

- **822b** -- its own `resolved_note` says *"Nothing in the substrate was fixed; the read was
  wrong."* An instrument defect.
- **822d** -- its `amend` is a `failure_record` **append** whose target is *"cross-candidate SPREAD
  ... prop_delta cannot answer this"*: a **DV redesign**, no code.
- **822c** -- the shared-initial-state contract defect, which **was** repaired in `ree_core`.

So **the true substrate-ceiling count for this lineage is 1**, not 3. And this artifact's own target
is instrument-only (`standard` per claim, `recommended_substrate_queue_entry.action: none`, the
defect entirely inside the experiment driver) -- which is R3 clause 2's *principle*: instrument
repair is the correct route, a brake is not. **The brake is released on that ground and no other.**

*Mechanically, why this target does not count* (red-team hygiene H4, correcting the draft): in the
SKILL's Step-7 recipe the target is dropped on the **first test** inside `counts()` --
`recommended_epistemic_category_per_claim` reads `standard` for both claims, which is non-empty and
does not contain `substrate_ceiling`, so the function returns `False` before any of clauses (1)-(4)
runs. The draft's account (clause 2 does not literally match `standard`, so clause 3 carries the
release) describes a path that never executes. `ree-v3/validate_queue.py::_autopsy_counts_toward_brake`
reaches the same verdict by a **different** route -- it reads only the blanket
`recommended_epistemic_category`, passes the first guard on direction `non_contributory`, finds no
instrument marker at clause 2, and releases at clause 3 on `fired: false` **and**
`literal_count_meets_threshold: true` with no build owed. **The two are therefore not byte-identical**
(hygiene H5); both release here, and whoever maintains the lockstep rule should reconcile them.

### 6.2 Two grounds withdrawn

- **WITHDRAWN -- the IMPLEMENTED-line consumer release.** `validate_queue.py::_substrate_is_built`
  reads the latest counted autopsy's `target_sd_id` (SD-082) and clears when a `ree-v3/CLAUDE.md`
  line carries `IMPLEMENTED` or `VALIDATED`. That line -- *"SD-082:
  pfc.lateral_pfc.rule_selection_action_consumer -- IMPLEMENTED 2026-07-26"* -- landed in ree-v3
  `d4f7580` on **2026-07-26**, i.e. **before all three counted hits** (822b 07-27, 822c 08-29, 822d
  08-30), and the check is stateless. For this lineage the consumer gate could never have blocked,
  however many letters circled. Citing it as independent corroboration is citing a check that cannot
  fail. **Vacuous.**
- **WITHDRAWN -- "no same-granularity re-derivation is being proposed."** True of 822e-vs-822d;
  **false** of the 822f the draft actually routed (same EXQ letter-series, same `claim_ids`, same
  substrate, same seeds, same DV, same criteria -- precisely the shape MOVE-3 refuses). It also
  mis-described clause 3, which governs whether *this target* counts and says nothing about the
  prior hits.

### 6.3 What is refused, and why 822f is licensed

**`refused_requeue`: "byte-identical 822f refused; design-changed 822f licensed."**

822f as now routed is **not** a same-question letter in the MOVE-3 sense, and that is the only
reason it is licensed. It changes the **load-bearing criterion** (a trained-minus-init
discrimination index replaces an absolute index a random head also clears), it adds the **control**
that criterion needs, and it changes the **seeds**. A byte-identical 822f -- the draft's routing --
is refused outright: 822e is a bit-for-bit replay of 822d (Section 1e), so a same-seed re-run
reproduces every number exactly and is a re-print, not evidence.

`supersedes_autopsy: failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30` -- **its routing
only**, not its disposition. That cluster autopsy commissioned 822e; 822e discharged the
commission, and the red team then established that the re-posed design cannot adjudicate the
question it was commissioned to adjudicate. The 822d target's `non_contributory` disposition and
`failure_autopsy_V3-EXQ-822c_2026-08-29`'s dispositions **stand unchanged**.

**What upstream substrate is owed: none.** The SD-082 per-candidate-summary amend is confirmed
engaged for the second consecutive run (worst summary spread ratio 2.702e-3; 0 fallbacks; 0
degenerate centering ticks). Leave the SD-082 `substrate_queue` entry at
`implemented_pending_validation` / `ready: false`, leave `severity: corrupting` and
`substrate_paths` untouched (they describe the **resolved** 822c `compute_bias` defect), and leave
the **open 822d failure_record item open** -- 822e did not resolve it, and after the red team it is
clear no run on this instrument could have. **Recommended** bookkeeping for governance's Step 6a
sweep: advance `validation_experiment` from `V3-EXQ-822d` to `V3-EXQ-822f`, recording in the same
move that 822f is the *design-changed* successor, not the byte-identical replay the draft routed.

### Granularity-debt recurrence trigger: DOES NOT FIRE

`granularity_debt_cluster.py`, 2026-09-05. SD-082: **3 tagging targets** across 3 files
(`failure_autopsy_2026-07-28-sweep` / `v3_exq_822b`; `failure_autopsy_V3-EXQ-822c_2026-08-29` /
`v3_exq_822c`; `failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30` / `v3_exq_822d`),
alignment distribution **unclear=3**. SD-078: **5 tagging targets** across 5 files (adding
`failure_autopsy_816c-822_2026-07-26` / `v3_exq_822` and
`failure_autopsy_batch-822a-826-817a-827_2026-07-26` / `v3_exq_822a`), alignment distribution
**unclear=5**. **No target reads `weakened`** in either cluster, which the reader's own rule
classifies as measurement or implementation debt regardless of count. The signatures also do not
differ structurally: 822/822a/822b are one measurement-starvation shape, 822c the shared-initial-
state contract defect, 822d the magnitude-DV mis-attribution, 822e the difference-of-norms gate and
the missing init control -- **five measurement defects in a row on one claim**, which is instrument
debt, not a coarse claim.

---

## 7. Learning extracted

1. **Queue-time check -- the one this lineage most needed. When a successor changes only its DVs on
   the same seeds, budgets and box, it is a DETERMINISTIC REPLAY: re-score the recorded rows offline
   before spending compute.** 822e reproduced 822d bit-for-bit (28/28 shared per-cell statistics
   identical in all ten cells), because P0/P1/P2 were unchanged and only new DVs were added on the
   same P2 ticks. The offending -0.003772 was already in 822d's manifest and already quoted in 822d's
   autopsy, so the readiness FAIL was **arithmetically certain before the queue entry was written**.
   Two hours five minutes of cloud compute bought a number that was on disk. The check belongs at
   `/queue-experiment` Step 4.5: *if the predecessor's rows already contain every input to a new
   gate, evaluate the gate on them first.*
2. **A movement floor is not a trainedness test, at any sign.** Repairing this gate's sign makes it a
   correct *optimizer-liveness* check (it would catch 822b's `post_p1 == init`), but not the test its
   name and docstring assert. The last layer is 32 parameters; Adam at lr 5e-4 displaces it ~2.8e-3
   on a single step, 2.8x the floor. **General form: when a precondition's NAME asserts a causal
   property ("actually trained") and its STATISTIC is a magnitude floor, ask what the floor's null
   distribution is under the property's NEGATION.** Here a random-init head clears the downstream
   criterion in 99% of trials, so the floor discriminates nothing.
3. **A discrimination criterion needs an INIT CONTROL, not a trainedness gate upstream of it.** The
   two are not substitutes and the design treated them as if they were. The correct construction is
   already half-built: `_init_positive_control` snapshots the head at init (L682) and a synthetic
   probe already runs through the trained head. "Index >= absolute floor" is evidence about training
   only when the floor is calibrated against the untrained distribution of the same statistic.
4. **A documented measurement defect that is never routed to a repair does not stay harmless -- it
   gets promoted.** Named defective by the 822c autopsy (2026-08-29), re-named as
   carried-forward-and-unfixed by the 822d cluster autopsy (2026-08-30, citing the very value
   -0.003772), then elevated from diagnostic flag to gating readiness precondition by 822e's
   red-team pass (2026-09-04) with no repair. Two confirmed autopsies wrote it down; neither emitted
   a routable item, so the corpus's memory of it was prose.
5. **A red-team finding of the form "X should gate rather than sit in `diagnostic_flags`" carries an
   unstated premise: that X measures what its name says.** When the flag being promoted is one a
   prior autopsy already called mis-specified, the promotion must be paired with the repair -- and,
   as this case shows, the repair must be checked against the flag's *purpose*, not only its sign, or
   a footnote becomes a run-voiding gate that still does not test what it claims.
6. **Sign convention is a first-class property of a readiness statistic.** A difference of norms is
   not a distance; `|d(norm)|` lower-bounds the true movement, so a `direction: lower` gate on the
   *signed* quantity fails precisely the cells that trained inward. **But the "gate and its sibling
   diagnostic disagreeing is a cheap lint" reading is weaker than first stated:** the two differ in
   *quantifier* as well as sign (all-cell `min` vs ON-arm mean), and a signed ON-arm mean (+0.004045)
   would also have passed. The lint fires; it does not isolate the sign.
7. **Run-level readiness is a hard conjunction and therefore a single point of failure for every
   claim's direction.** 822e's red team correctly moved C4's `dv_headroom` *out* of run-level
   readiness for exactly this reason, and in the same pass moved a defective statistic *in*. A
   precondition should gate only the criteria it bears on; here the pool-control arm holds a veto
   over the treatment arm's absolute criteria.
8. **`substrate_not_ready_requeue` is a lossy label.** The driver emits it for *any* unmet readiness
   precondition, so it cannot distinguish a substrate gap from a broken instrument, and a governance
   reader who trusts the label books substrate debt that is not owed. This family would benefit from
   splitting it (`substrate_not_ready` vs `instrument_not_ready`).
9. **Recording note, not a gap.** The recording was good enough for the run to diagnose itself *and*
   for a third party to falsify that diagnosis: `head_diag_by_phase` carries the per-cell norms,
   `per_seed_rows` carries every readiness input, and 822d's manifest is bit-comparable, so the
   replay identity was provable in a 30-second script. 822f should record `||W_p1 - W_init||`
   directly, and the **init-head index alongside the trained one**.
10. **C4's mean clause is an under-powered construction, independently of all the above.** A 5-seed
    mean with sd 1.694 gives t-like 0.0714, so one outlier cell sets the sign. `>= margin on >= 4/5
    seeds AND mean >= margin` is not two gates -- the mean clause is a one-outlier veto over the seed
    clause, and here it fired. Pre-register such a contrast at a seed count its own measured variance
    can support, or emit `inconclusive` by construction.

### Read-across, not adjudicated

- **WITHDRAWN (Step 8 gate).** The draft recorded "SD-082's substantive result is very likely a PASS
  this run could not record." Withdrawn per Section 3b -- recorded rather than deleted because it was
  the draft's load-bearing argument for a cheap re-run. A random-init head clears C1's floor in 99%
  of trials, above 822e's 1.846, so a counterfactual PASS would have mislabelled init structure as a
  trained coupling.
- Under the same counterfactual `dir_078` would have been `inconclusive`, not `weakens` -- and that
  outcome is **predetermined** for any same-seed replay (Section 4).
- `hidden_dead_relu_frac_p2_mean` is 0.5140 (ON) / 0.5127 (OFF) -- over half the consumer head's
  hidden ReLU units dead in both arms, the same reading 822d recorded. Flagged by the driver as
  `dead_relu_partial_contributor`; it did not prevent C1/C2 clearing, but it caps the achievable
  index. It is registered as its own hypothesis leg (H4) and is **not** adjudicated by 822f.
- The per-cell `substrate_hash` is identical across all ten cells of this run but **differs** from
  822d's despite bit-identical P0-P2 outputs. The hash folds driver and config, not `ree_core`
  alone -- do not infer a substrate change from a changed hash.

---

## 8. Routing

**Node classification: `complex (probe-gated)` / `puzzle (known rules)`.** A fact is missing:
whether the readout's measured discrimination exceeds what the head's **initialisation** already
provides. Nobody has measured the index on an untrained head of this shape inside this driver. It is
a `puzzle (known rules)` rather than a `mystery (known data)` because the missing fact is obtainable
by a named measurement under rules already in the driver -- get the fact, do not reframe. *(The
draft's `complicated (buildable)` was correct only for the sign-convention repair, which is no longer
the load-bearing change.)*

### 8.1 Routed: `/queue-experiment` V3-EXQ-822f as a REAL DESIGN CHANGE

Five requirements, all ratified at the Step 8 gate:

**(a) Load-bearing criterion becomes a TRAINED-vs-INIT discrimination index.** Run
`_init_positive_control` / the existing synthetic probe through the **init** head as well as the
trained head, and gate and score on the **trained-minus-init** index rather than an absolute floor.
Pre-register the margin from the random-init distribution -- either the Monte-Carlo **p95 of 5.41**
(200 trials, driver-shape head, K=32 centered random summaries, last-layer norm rescaled to the
recorded 0.148, `rule_state` norm 0.19) or, preferably, an init distribution **measured in-run**
across the same seeds. An absolute index `>= 1.0` is **not** a criterion.

**(b) New seeds.** Not 101/202/303/404/505. 822e is a bit-for-bit replay of 822d on those seeds.

**(c) Trainedness gate re-specified** as `||W_p1 - W_init||` per parameter tensor (absolute, a real
distance), scoped to the **treatment arm's** cells -- or, if the pool-control arm keeps a veto, the
driver must say why. Keep it as a liveness check and **describe it as one**; it is no longer
load-bearing for the trained-vs-init question, which (a) now owns.

**(d) Keep the C4 / SD-078 contrast**, read through the driver's three-valued logic --
`inconclusive` at t-like 0.07 is the honest emission and must be emitted as such rather than
collapsing into a run-level FAIL. Pre-register the SD-078 contrast at a seed count its variance can
support (`contrast_sd` 1.69 at n=5), or declare it diagnostic-only.

**(e) Record the offline re-score** of 822e's recorded rows (below) as provenance, **not** as
evidence for SD-082.

Cost: comparable to 822e (~2h05m on a cloud worker) plus the init-head pass, which is cheap.

### 8.2 Fan-out (GOV-FANOUT-1)

The bottleneck is a **discrimination**, and after the red team it is a two-way one:

| leg | reading | adjudicated by |
|---|---|---|
| **H1-trained-discriminating-readout** | the discrimination comes from the trained rule->bias coupling (SD-082's assertion) | **V3-EXQ-822f** |
| **H-init-structure** | the discrimination is real but is the init structure of a random first layer + ReLU | **V3-EXQ-822f** |
| H2-uniform-common-mode | the raw bias is candidate-uniform; spread is tanh-manufactured | *its own probe* -- not 822f |
| H3-upstream-summary-starvation | the index is set upstream by summary/mask homogeneity | *its own probe* -- not 822f |
| H4-dead-head-capacity | a half-dead head caps the achievable index | *its own probe* -- not 822f |

822f adjudicates exactly the first two, because the init-head control makes them **complementary
under a single measurement** -- a portfolio of one measurement over two legs, not a sequential
re-pose, and emphatically not a power-bump (822e's bars were *cleared*; the defect is that clearing
them means nothing). **H2/H3/H4 are not assigned to 822f** and must not be read as bearing on it:
H3's own adjudication condition is a hidden-mask decomposition and H4's is an
initialisation/activation variation, neither of which 822f performs. Assigning them to 822f was an
internal contradiction in the draft (red-team Finding 3), now corrected. Do **not** queue them off
this artifact; each carries a probe sketch in the registry entry.

### 8.3 Withdrawn routing (recorded, not deleted)

The draft routed *"a SAME-QUESTION alphabetic successor V3-EXQ-822f whose ONLY substantive change is
the trainedness instrument ... everything else -- the DV, C1/C2/C4, the arm axis, the controls, the
seeds -- byte-identical to 822e."* **Refused**, for two reasons: it is a deterministic replay that
would reproduce C1 (4/5, 1.846), C2 (0.0583) and C4 (mean 0.0541, seed 101 -2.879) exactly plus a
passing gate -- the draft's own counterfactual **is** that run's result, already derivable from
disk -- and it would then record `supports` for SD-082 on criteria a random-init head also satisfies.
The draft's rationale ("the verdict should be re-earned by 822f") was procedural rather than
epistemic: the same computation on the same seeds yields the same numbers.

### 8.4 Explicitly NOT recommended

- **A byte-identical or same-seed 822f** -- refused; see 8.3.
- **Recording the counterfactual PASS** by any route, offline re-score included. The criteria cannot
  distinguish a trained coupling from init structure, so the label would be wrong however produced.
- `/implement-substrate` -- nothing in `ree_core` is implicated.
- `/lit-pull` -- the biology is not in question.
- governance demotion -- neither claim was tested; demoting off an instrument defect is the exact
  error the 822d cluster autopsy withdrew.
- `/claim-synthesis` -- the recurrence reader classifies this as measurement debt.
- `/diagnose-errors` -- the run completed; there is no crash.

### 8.5 What governance may do for the record

**For the record only, and explicitly not evidence for SD-082:** re-score 822e's recorded rows
offline under the `REE_assembly/CLAUDE.md` "Fallback workaround" path. Every input to the readiness
conjunction is in the manifest (18 `readiness_*` fields True, `c1_pass`, `c2_pass`, the ten
`head_diag_by_phase` cells), so re-running the conjunction with `abs()` on
`last_layer_weight_delta_init_to_p1` costs nothing and documents that the only unmet precondition
falls away under the correct statistic. That establishes the **instrument** defect and nothing else.
It does **not** license writing `supports`, `PASS`, or
`sd082_candidate_discriminating_bias_confirmed`.

### Recommended manifest disposition (governance writes; this skill does not)

Write **both copies** and rebuild the index:

- flat: `evidence/experiments/v3_exq_822e_sd082_candidate_discriminating_bias_spread_20260905T025644Z_v3.json`
- pack: `evidence/experiments/v3_exq_822e_sd082_candidate_discriminating_bias_spread/runs/v3_exq_822e_sd082_candidate_discriminating_bias_spread_20260905T025644Z_v3/manifest.json`

- `evidence_direction`: **`non_contributory`**;
  `evidence_direction_per_claim`: `{SD-078: non_contributory, SD-082: non_contributory}`
- `evidence_direction_note`: as drafted in the JSON artifact -- it carries **both** grounds
  (instrument-voided readiness; C1 uncreditable without an init control).
- `non_degenerate`: **keep `false`**, on two grounds now: readiness was voided, *and* the
  load-bearing discrimination criterion is uncreditable without an init-head control. Note
  `criteria_non_degenerate` is true for C1/C2/C4 individually and every control probe fired, so this
  is not a *measured* degeneracy. Suggested `degeneracy_reason`: "run-level readiness voided by a
  mis-specified trainedness precondition (signed difference of weight norms gated with direction
  lower over the minimum cell), AND the load-bearing discrimination criterion C1 uncreditable without
  an init-head control (a random-init head of this shape clears its 1.0 floor in 99 percent of
  Monte-Carlo trials); no individual criterion was measured degenerately".
- Category enum: **`standard`** (both claims; confirms the stored value).
- Supersession: 822e's manifest already carries `supersedes: V3-EXQ-822d`. **Do not** set
  `evidence_direction: superseded` on 822d's manifest off this run. 822e strictly *contains* 822d's
  measurement, but 822d's own DV was withdrawn by its own confirmed autopsy, so its
  `non_contributory` already stands for the right reason.

Because `non_degenerate: false` already excludes the run from confidence and conflict scoring, this
write changes **nothing** in the indexer's arithmetic -- it corrects the human-readable record only.

### Per-claim recommendation

Both claims already store `epistemic_category: standard`, `pending_retest_after_substrate: false`
and `status: candidate_substrate_landed`, and **this run moves none of them**. Both dispositions are
therefore **note-only**, and both `change` strings end on a citation stamp
(`-> stamp this artifact`) rather than an already-true storable value, so GOV-APPLY-1's row stays
actionable and clears via the provenance stamp once governance writes the note. The exact
`evidence_quality_note` text for each claim is drafted verbatim in the JSON artifact under
`recommended_evidence_quality_note_per_claim`.

`recommended_diagnostic_evidence_adjudicated` is deliberately **not** set: `experiment_purpose` is
`evidence`, and the flag exists to mark an adjudicated-and-expected zero on a diagnostic, not to
paper over an evidence gap on a claim that should accumulate scoring entries.

---

## 9. Step 7c red team and Step 8 gate

**Step 7c -- cross-model, read-only. Model `fable-5.1`. Verdict: CONTESTED.** Findings file:
`redteam_822e.md` (session scratchpad; path recorded in the JSON artifact's `red_team.findings_file`).

It **confirmed** the diagnosis on every number it recomputed -- the trainedness-gate arithmetic and
all ten signed deltas (Finding 5), C4's statistics and the driver's three-valued logic (Finding 6),
the substrate / claims / manifest state and the supersession call (Finding 7), and the unstated
premise that both arms carry SD-082's fix (Finding 8). It **contested** the routing and two things
resting on it.

| # | Finding | Disposition |
|---|---|---|
| 1 | 822e is a bit-for-bit replay of 822d; the FAIL was predictable at queue time; "re-earned by 822f" is hollow | **APPLIED** -- Sections 1e, 3c, 6.3, 8.3; learning #1 |
| 2 | No movement floor can discharge the gate's stated intent; a random-init head clears C1 in 99% of trials | **APPLIED** -- Section 3b; read-across withdrawn; second ground for `non_contributory`; 822f redesigned |
| 3 | The 4-leg registry question omits the init-structure rival and assigns H3/H4 to a run that cannot adjudicate them | **APPLIED** -- new qid, 5 legs, H2/H3/H4 unassigned |
| 4 | The recount is right; brake ground 2 is vacuous, ground 3 mis-describes clause 3; the direction is defensible on a ground the draft does not use | **APPLIED** -- Section 6.1-6.2 |
| 5 | Trainedness-gate arithmetic | **CONFIRMED** (carried; H6 nuance applied) |
| 6 | C4 and the three-valued logic | **CONFIRMED** (carried) |
| 7 | Substrate, claims, manifest disposition, supersession | **CONFIRMED** (carried) |
| 8 | Unstated premise "both arms carry SD-082's fix" | **CONFIRMED** (carried) |
| H1 | flip-resolution floor is 200, not 50 | **APPLIED** -- Section 1c |
| H4 | `this_target_counts_basis` names a mechanism that never fires | **APPLIED** -- Section 6.1 |
| H5 | the SKILL recipe and `validate_queue.py` are not byte-identical | **APPLIED** -- Section 6.1 |
| H6 | gate and sibling differ in quantifier as well as sign | **APPLIED** -- Sections 3a, 7.6 |
| H7 | JSON said Step 7c was skipped | **APPLIED** -- `mechanical_checks` and `staging_note` updated |
| H8 | substrate_hash differs 822d-vs-822e despite identical outputs | **APPLIED** -- header, read-across |

H2 and H3 required no change (both verified the draft's own numbers).

**Step 8 gate -- user decision, binding (2026-09-05):**

> "No replay; 822f = init-head control + new seeds."

Both claims **held** at `non_contributory` with `epistemic_category: standard`. The draft's routing
is withdrawn and recorded; the design-changed 822f is the ratified route.

---

## 10. Mechanical checks

- **Dry-run gate:** clean; `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- **Step 7b `autopsy_pre_routing_checks.py`:** `fire_count: 0`, `fires: []` against the draft. One
  `inapplicable` entry (C5, prose-keyed). **Re-run owed** against this final confirmed pair by the
  applying session -- the routing, node classification and read-across all changed.
- **`granularity_debt_cluster.py`:** does not fire (Section 6).
- **Re-derive brake R1-R3:** prior counts 3 (SD-082) / 5 (SD-078), independently reproduced by the
  red team; this target does not count; brake does not fire; released on one ground (Section 6.1);
  byte-identical requeue refused (Section 6.3).
- **Hypothesis-space ledger (Step 9b):** no existing question lists SD-078 or SD-082 (53 questions
  checked; independently confirmed by the red team). A new question is **warranted** and is DRAFTED
  in full registry schema in the JSON artifact's `hypothesis_space_ledger_pending`
  (`draft_for_governance: true`) -- qid `sd082_candidate_discriminating_readout_locus`, **five**
  legs, `initial_frozen_count` 5, all `alive`, axes `readout` / `intrinsic-architecture` /
  `representation` (all already in `axis_families.map`; no new family row needed). **The registry
  was not written by this session.**
- **Step 7c red team:** RUN (Section 9).
- **Step 8 interactive gate:** RUN (Section 9).
- **Not done by this session, by design:** no `claims.yaml`, manifest, `review_tracker`,
  `substrate_queue`, hypothesis-space registry, governance-flag or `WORKSPACE_STATE` edit; nothing
  committed; no chip spawned.

## 11. Open doubts

1. **The init-head control is estimated, not measured in-run.** The 99%-clearance figure comes from
   a 200-trial Monte Carlo over a head of the driver's *shape*, not from this driver's actual
   initialisation inside its actual loop. The estimate is strong enough to withdraw the read-across
   (the margin is large: median 3.93 vs a 1.0 floor, and 822e's 1.846 sits below the untrained
   median), but 822f must **measure** the init distribution rather than inherit this number.
2. **`||W_p1 - W_init||` is not recoverable from the manifest** -- only its lower bound `|d(norm)|`
   is. If some cell's true movement were dominated by rotation, the bound understates it; that
   direction is safe here (the bound already clears), but 822f must record the real thing.
3. **Over half the consumer head's hidden ReLU units are dead in both arms** (0.514 / 0.513). C1 and
   C2 cleared anyway, so it is not blocking, but an index measured through a half-dead head is a
   weaker instrument than the design assumes. Registered as leg H4; **not** adjudicated by 822f.
4. **Seed 101 is anomalous on two statistics at once** -- the only negative last-layer deltas in the
   matrix (both arms) and the -2.879 C4 outlier from its OFF cell's 4.316 index in a single-rule
   pool. This autopsy treats those as independent facts. They may not be; a common cause would
   matter to both C4's power and the trainedness read, and no one has looked. Section 3b makes this
   more pressing, not less: an index of 4.316 in a *pinned* pool is close to the untrained median.
5. **What the offline re-score is allowed to establish is narrower than it looks.** It is arithmetic
   over recorded fields and it settles the instrument question completely -- but Section 3b means it
   cannot be walked forward into a direction for SD-082. Governance should record it as provenance
   and stop there.
6. **`docs/claims/claims.yaml` did not parse in the working tree at draft time** (line 74376, an
   unrelated v4_v5 entry). The committed HEAD copy parses cleanly, so it is a live session's
   uncommitted edit. Not caused by, and not touched by, this session -- but governance should confirm
   it is cleared before any claims-layer write.
