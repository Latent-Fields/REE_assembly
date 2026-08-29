# Failure Autopsy: V3-EXQ-822c (SD-078 / SD-082)

Generated: `2026-08-29T09:41:48Z`
Scope: single
Status: **confirmed** (user-adjudicated at the Step 8 gate, 2026-08-29)
Re-adjudication of: `failure_autopsy_2026-07-28-sweep.json` (its V3-EXQ-822b target)

**Headline.** The number that has driven this entire lineage for a month -- `on_prop_delta_mean =
off_prop_delta_mean = exactly 0.0`, recorded twice in `substrate_queue.json` as a "structural zero
on both arms" -- was **never measured**. It is the empty-list default of
`statistics.fmean(prop_deltas) if prop_deltas else 0.0`, and `n_prop_samples` is `0` in **all 18
cells** across V3-EXQ-822, 822a and 822b. The 822b autopsy's substrate attribution ("REINFORCE
never updates the last linear layer") is superseded. The real defect is one level upstream, is
structural, and is now measured.

---

## 0. Selection and mechanical gates

Target chosen from a freshly regenerated `pending_review.md` (2026-08-29T09:26:55Z, run against
current `origin/master` in a throwaway worktree -- the shared `REE_assembly` checkout is diverged
`[ahead 22, behind 104]` and was deliberately not disturbed). Five items are owed an autopsy; this
is one of them (the other four are listed in Section 8).

| Gate | Result |
|---|---|
| Dry-run (Step 2a), 822c + 822b + 822a + 822 | `0 dry cited, 0 dry in named families, 0 ambiguous, 4 clean, 0 unknown` |
| `dry_run_unreachable_criterion` lint | 11 warnings, **all** in the `v3_exq_543` lineage (b-l). No `822x` driver fires; 822c is not a smoke |
| Recording always-core (`validate_recording.py`) | **complete** -- `rec/v1`, `substrate_hash`, `machine`, `machine_class`, `elapsed_seconds`, `config`, `seeds` all present |
| Coverage (`check_autopsy_coverage.py`) | 822c uncovered; contention sweep clean |
| Step 7b pre-routing checks | **0 fires** |
| Re-derive brake (R1-R3) | **does not fire** -- 0 `substrate_ceiling` hits for SD-078 (3 prior targets) and SD-082 (1) |
| Granularity-debt trigger | **does not fire** -- no target reads `weakened`; alignment distribution `unclear=3` / `unclear=1` |

---

## 1. Facts

`v3_exq_822c_sd082_candidate_summary_fallback_fix_20260829T065645Z_v3`, queue_id V3-EXQ-822c,
`experiment_purpose: diagnostic`, outcome **PASS**, `evidence_direction: unknown`, claim_ids
SD-078 + SD-082, `supersedes` the 822b run. 2 arms (ARM_OFF / ARM_ON, the swept variable being
`crf_cue_centering`) x 3 seeds (101, 202, 303), `ree-worker-3`, 6063 s. Both arms build with
`lateral_pfc_rule_readout_consumer=True` and `lateral_pfc_train_rule_bias_head=True`;
`candidate_summary_source` is never set, so it is the default `'proposer'`.

**What 822c changed.** Exactly one thing: `_candidate_summaries()`. 822/822a/822b called only
`agent._candidate_world_summaries(candidates)`, which returns `None` on the default
`candidate_summary_source='proposer'`. 822c replicates the production `select_action` fallback
instead. I verified the replication line-by-line against `ree_core/agent.py` -- it matches
(the extra `.detach()` blocks gradient to the world model only, not to the head's own weights,
so it does not affect head training).

**Measured (all recomputed from `per_seed_rows`; every manifest aggregate reproduced exactly).**

| metric | ARM_ON | ARM_OFF | threshold |
|---|---|---|---|
| `prop_delta_mean` | 0.001662 | 0.001761 | floor 1e-3 |
| `last_layer_weight_delta_init_to_p1` (mean) | **-7.845e-05** | -- | `< 1e-3` -> "untrained" |
| `hidden_dead_relu_frac_p2_mean` | 0.5113 | 0.5172 | 0.90 confirm / 0.50 partial |
| `rule_summary_magnitude_ratio_p2_median` | **2.85e6 - 4.46e6** | similar | in-range `[1e-3, 1e3]` |
| `rule_state_diff` | 0.440 / 0.650 / 0.651 | ~0 | -- |
| `n_head_diag_samples` | 145 - 200 | 160 - 200 | floor 5 |

Per-seed propagation, which the aggregate hides:

| seed | ON | OFF | \|diff\| vs 1e-3 |
|---|---|---|---|
| 101 | 0.002027 | 0.000255 | 0.001771 **ON wins 7.9x** |
| 202 | 0.001993 | 0.002025 | 0.000033 tie |
| 303 | 0.000965 | 0.003002 | 0.002036 **OFF wins 3.1x** |

**The PASS means less than it looks.** `C1_head_diagnostics_interpretable` is literally
`c1 = ready` (driver line 754) -- the conjunction of the six readiness preconditions. This run's
PASS asserts that the diagnostics were *interpretable*, and nothing whatever about the science.

---

## 2. What the prior lineage actually established

`n_prop_samples` and `n_head_diag_samples` are **0 in every cell** of 822, 822a and 822b. So in
those three runs `prop_delta_mean`, `hidden_dead_relu_frac` and `rule_summary_magnitude_ratio` are
all **no-data defaults of `0.0`**, indistinguishable in the manifest from measured zeros. Two
`substrate_queue` failure records and two confirmed autopsies read them as measurements.

**One prior number *was* real, and this matters.** 822b's
`last_layer_weight_delta_init_to_p1 = 0.0` is a genuine read: the script computes it as
`post_p1_norm - init_norm` with a `.get(..., 0.0)` default, so a *missing* `post_p1` snapshot
would have produced `-0.148`, not `0.0`. Observing exactly `0.0` means `post_p1` was recorded and
equalled `init` exactly -- the weights really did not move.

The 822b autopsy's discipline was therefore **correct and is what makes this correction cheap**:
it explicitly separated the gated tick-sampled diagnostics from the ungated weight-norm snapshots,
and it was right that the latter were valid. What it could not see is that *both* families shared
a single upstream cause. **Ungated is not the same as unconfounded.** The weights did not move
because the driver's own REINFORCE loop never executed: `cs` was always `None`, so `ep_buf` never
accumulated, `outcome_buf` stayed empty, `_lpfc_reinforce_loss` hit its `len < 2` early return and
returned a tensor with no `grad_fn`, and the optimiser step was skipped on every episode. The
*substrate* optimiser was never exercised at all -- so the routing to "trace optimizer parameter
registration / gradient flow through the tanh / `ADV_MIN_THRESHOLD`" was aimed at code that had
never run.

With the driver fixed, the head trains: the last-layer norm delta moves from exactly `0.0` to
`7.8e-05`.

---

## 3. The real defect (structural, and now measured)

`compute_bias` receives `candidate_world_summaries`, built as `ws[0, 0, :]` per candidate. But
`ree_core/predictors/e2_fast.py` seeds the rollout with

```python
states       = [initial_z_self]
world_states = [initial_z_world]     # <- index 0
```

so **index 0 is the rollout's shared initial world state**. Candidates differ only in the actions
applied from `t >= 1`. `ws[0, 0, :]` is therefore **bit-identical across all K candidates by
construction**, and carries exactly zero candidate-discriminating information.

SD-082's own centering step then runs on it:

```python
summaries = summaries - summaries.mean(dim=0, keepdim=True)   # centering a constant -> 0
rule_repeated = self.rule_state.expand(k, -1)                 # identical across candidates too
joined = torch.cat([rule_repeated, summaries], dim=-1)
```

Centering a constant yields zero, leaving only float32 cancellation noise. Two independent lines
of evidence converge on this:

1. **Structural** -- the `world_states[0] = initial_z_world` seeding above, plus the fact that
   *both* `agent.py` sites (the `gated_policy` block ~7185-7204 and the fallback ~7412-7424) use
   the identical `ws[0, 0, :]`. The defect is unconditional on the default config.
2. **Numerical** -- the observed `rule_summary_magnitude_ratio` of 2.8e6-4.5e6 is exactly the
   scale float32 cancellation of near-identical O(1) vectors produces (~1e-7 relative residual
   against an O(1) `rule_state`). It is 4000x over the driver's own 1e3 ceiling, in **all six
   cells, both arms**.

This explains every observation at once: the bias is driven almost entirely by `rule_state`, which
is candidate-invariant, so `prop_delta` is small and arm-independent; ~51% of hidden units sit dead
identically in both arms; and the head barely trains because **there is no candidate-discriminating
signal for it to learn from**. "Untrained" is a downstream symptom, not the cause.

> **Caveat, stated rather than smoothed over.** I could not decompose the 4e6 ratio into its
> numerator and denominator from the artifact: `rule_state_norm` is already exposed by
> `get_state()` (`lateral_pfc_analog.py:485`) but the driver never records it, and the summary
> norm is computed inline and discarded. The structural argument is decisive on its own; the
> numerical argument is a strong corroboration, not an independent measurement. **Cheap
> confirmer:** record both norms in the amended run -- a one-line addition to
> `_head_diag_snapshot`.

### The consequence for SD-082's acceptance criterion

SD-082's `evidence_quality_note` states its own acceptance as *"`on_prop_delta_mean >= 0.001` with
an ON>OFF contrast"*. 822c supplies the first non-vacuous measurement of it: the **absolute floor
is met** (0.001662) but the **contrast is not** (OFF 0.001761 >= ON 0.001662). More importantly,
on this analysis the contrast is **structurally unpassable** as currently wired, not merely unmet
-- the only candidate-varying input is float noise. That is a governance-relevant difference.
It is flagged as read-across, **not adjudicated**: the run is diagnostic-purpose and
scoring_excluded, n=3, and the per-seed direction inverts.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | diagnostic, scoring_excluded; SD-078's downstream behaviour still untested |
| Biological reference | **clear** | corticostriatal rule-to-action readout; a wiring/contract defect, no translation error, no lit-pull owed |
| Prerequisites | **present** | SD-078 upstream chain healthy and measured healthy (`rule_state_diff` 0.44-0.65 ON vs ~0 OFF; cone 0.960; rule active 87.4% of P2) |
| Implementation | **partial (defective)** | consumer engaged, but its per-candidate channel is constant by construction and centering annihilates it |
| Environment | **adequate** | unchanged from 822a; not implicated |
| Measurement | **partial** | three defects -- see below |
| Integration | **coupled but unstable** | defect sits exactly at the E2-rollout / PFC-readout contract |
| Scale | **adequate** for the primary finding; **insufficient** for the ON-vs-OFF read (3 seeds, direction inverts) |

**The three measurement defects**, because they are reusable lessons rather than incidental:

1. **The headline flag is a difference of norms, not a movement measure.**
   `head_untrained_last_layer_static` compares `post_p1.last_linear_weight_norm` with
   `init.last_linear_weight_norm`. A weight matrix can rotate arbitrarily at constant norm and
   register zero -- and rotation is the expected form of learning for a REINFORCE readout. The
   right measure is `||W_post - W_init||` against `||W_init||`.
2. **It averages *signed* per-seed deltas** (+1.162e-4, -4.233e-4, +7.178e-5), permitting
   cross-seed cancellation. Latent here (all three magnitudes are also below 1e-3) but a real trap.
3. **The label ladder suppresses the run's own best finding.** Driver lines 743-752 test
   `head_untrained` *before* `magnitude_imbalance`, so the run emits a threshold call at 7.8e-05
   against 1e-3 on a proxy measure, and hides a direct measure sitting 4000x over its ceiling in
   all six cells. The correct label for this run is `magnitude_imbalance_confirmed_contributor`.

### Failure-location summary (GOV-FAILLOC-1)

**MIXED -- MECHANISM + MEASURES. Not chargeable to REE.** Implementation reads *partial
(defective)* and Measurement reads *partial*, so the precondition for a REE FAILED read (all three
of implementation / measurement / environment independently adequate) is not met and is not close
to met. Environment is not implicated.

---

## 5. Learning extracted

- **A no-data default that shares the numeric value of a meaningful result is the most expensive
  shape in this corpus.** `fmean(xs) if xs else 0.0` produced an "exactly 0.0" that read as a
  strong structural finding, survived two confirmed autopsies, motivated a substrate landing and
  an amend, and stood for a month. The fix is to make the empty case *unrepresentable* -- emit
  `None`/absent, or require the paired `n_samples` beside every aggregate -- not to remember to
  check `n_samples`.
- **Ungated is not unconfounded.** The prior autopsy correctly established that the weight-norm
  read was not gated by the failed precondition. Both families nonetheless shared one upstream
  cause, so a valid number still pointed the routing at code that had never executed.
- **A diagnostic's label ladder is a design decision that can suppress its own best finding.**
  Order by evidential strength or causal depth, not by the order the hypotheses were written down.
- **Centering is not a safe no-op on a degenerate input.** Applied to an input that is constant
  across candidates, SD-082's centering converts "identical and O(1)" into float32 noise and
  manufactures a 4e6 magnitude imbalance. A centering step should assert non-trivial cross-group
  variance in its input before it is trusted.

---

## 6. Routing -- `implement-substrate` (amend SD-082)

Work-graph classification: **`complicated (buildable)`** -- a named build with no open question.
No spike is owed; do not queue a probe to re-confirm what is structurally established.

- `action: amend`, `target_sd_id: SD-082`, `priority_suggested: 1`
- **`severity: corrupting`** -- on the default config `compute_bias` returns a bias that *looks*
  responsive and yields a `prop_delta` **above** the 1e-3 non-vacuity floor while carrying zero
  candidate information. Any experiment reading `prop_delta`, or any consumer reading `lpfc_bias`,
  gets an authentic-looking meaningless number.
- `substrate_paths`: `ree_core/pfc/lateral_pfc_analog.py::compute_bias`, `ree_core/agent.py`
- **Mark all three existing `failure_record` entries `superseded`** (not `resolved` -- nothing was
  fixed; a later, better-instrumented run overturned the read).

Fix options, in rough order of directness: (a) take a post-action index or horizon aggregate
(`ws[0, 1:, :].mean(0)` or `ws[0, -1, :]`); (b) make `candidate_summary_source='e2_world_forward'`
the default for this path -- it exists already (ARC-065 GAP-A) but changing a default is a wider
behavioural change and must be swept, not assumed; (c) guard `compute_bias` to flag when the
post-centering summary norm is at float-noise scale, so this can never again present as a
plausible number. **Fix both `agent.py` sites** -- they duplicate the same index. Record
`rule_state_norm` and the pre/post-centering summary norms while there.

Per-claim: both SD-078 and SD-082 stay `non_contributory`, `standard`, `pending_retest_after_substrate: true`,
`recommended_diagnostic_evidence_adjudicated: true`, status unchanged at `candidate_substrate_landed`.
SD-082's centering is **not falsified -- it is untested**, because its input never carried the
cross-candidate variance it was designed to preserve.

`standard` is chosen deliberately over the suppress-set categories: the finding is an
implementation + measurement defect with a bounded fix, not an assertion that either claim's answer
is gated on open-ended substrate work. Four of the six suppress-set values would additionally mark
these claims not-v3-testable, starving them of experiment lanes exactly when a concrete v3
experiment is what is owed. (Both prior autopsies in this lineage stamped values -- 
`competence_implementation_gap`, `precondition_unmet` -- that are outside the eight-value enum.)

---

## 7. Adversarial pass (Step 7c) -- scope limitation stated

> **User disposition at the Step 8 gate:** proceed and land with this gap documented.

The skill calls for an independent subagent to attack the conclusion. **This session operates under
a standing instruction not to call the Agent tool, so the independent red-team was NOT run.** In its
place I ran the adversarial checks directly, and they are recorded here so the gap is visible rather
than silently absorbed:

- **Recomputed every load-bearing aggregate** from `per_seed_rows`; all four reproduce the manifest
  exactly (weight delta, dead-ReLU mean, ON and OFF `prop_delta`).
- **Checked the flag arithmetic against the driver's own constants** -- `head_untrained`
  (7.845e-05 < 1e-3), `dead_relu_partial` (0.511 in [0.50, 0.90)), `magnitude_extreme` (4e6 > 1e3),
  `prop_nonvac` (1/3 seeds < 0.6 pass fraction). All correct as computed.
- **Tested the prose absolutes against the cells.** Found and reported the ON/OFF direction
  inversion across seeds that the aggregate hides -- the aggregate "OFF >= ON" is carried entirely
  by seed 303.
- **Falsified my own first hypothesis.** I initially read the 0.96 `zworld_cone_min_cosine` as
  cross-candidate spread, which would have made a 4e6 ratio arithmetically impossible. It is
  sampled across *ticks* (`zworlds.append(latent.z_world...)`), not across candidates. The
  correction is what led to the structural `world_states[0]` finding.
- **Checked the scope of the defect rather than assuming it.** `agent.py` has a `gated_policy`
  path that could have bypassed the fallback; I read it and it uses the identical `ws[0, 0, :]`.
- **Named the premise I could not verify** -- the ratio's decomposition (Section 3 caveat), with a
  cheap confirmer.

**Residual risk I would most want a second pair of eyes on:** whether `rule_state` could itself be
pathologically large (~1e6) rather than the summaries being annihilated. The structural argument
does not depend on it, but the two readings imply different fixes, and only the unrecorded norms
settle it.

---

## 8. Still owed (not autopsied here)

Four other targets are owed an autopsy, all uncontended and uncovered as of this session:

| Target | Purpose / outcome | Claims |
|---|---|---|
| `V3-EXQ-952` | diagnostic PASS, `phasic_warmup_rescue_confirmed` | (none) |
| `V3-EXQ-956` | diagnostic FAIL, `non_contributory` | (none) |
| `V3-EXQ-862b` | evidence FAIL, `weakens` | Q-040 |
| `V3-EXQ-936a` | evidence PASS, `weakens` -- *not* owed by this skill, but the PASS/`weakens` combination is worth a governance look | MECH-439 |

---

## 9. Step 8 gate -- user disposition

All three questions put to the user were answered as recommended:

1. **Supersession** -- confirm all three SD-082 `failure_record` entries (822, 822a, 822b)
   as `superseded`.
2. **SD-082 evidence direction** -- `non_contributory`: the centering mechanism is untested,
   not falsified.
3. **Step 7c red-team gap** -- proceed and land, with the limitation documented in Section 7.
