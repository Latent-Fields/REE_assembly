# Authority-to-action stage trace: first probe

**Date:** 2026-08-22
**Session:** `authority-trace-probe-e7ec46`
**Instrument:** `ree-v3/scripts/authority_trace_probe.py` (ree-v3 `3ce4ee21b0` + fixes)
**Tests:** `ree-v3/tests/contracts/test_authority_trace_probe.py` (17, time-independent)
**Raw output:** `atp_default.json`, `atp_harm.json`, `atp_poscontrol.json` (session scratchpad)

## Question

Should REE carry a universal per-signal contract tracing every modulatory
signal through scoring -> eligibility -> arbitration -> committed behaviour ->
realised behaviour?

This probe was scoped as the cheap first measurement: sweep the flags that are
actually enabled in a default agent, produce the five-column table, and use the
fanout to decide whether the remaining ~160 are worth paying for.

> **SUPERSEDED IN PART BY THE UPDATE AT THE END OF THIS FILE (2026-08-22, same
> session).** The operating-point sweep, forced-lockstep mode, the root cause of
> the inertness, and a significant piece of PRIOR ART that this document's first
> version missed are all recorded there. Sections below are the first pass and
> are accurate except where the update says otherwise.

## Headline

**The fanout is not over signals. It is over operating points, and the default
operating point has no modulatory layer at all.**

At the bare default, `E3.select()`'s post-modulation `scores` tensor is
**bit-identical** to its pre-modulation `raw_scores` tensor on every tick. E3's
own diagnostics agree independently: `score_bias_abs_mean = 0.0`,
`score_bias_range_mean = 0.0`, `score_bias_to_raw_range_ratio = 0.0`,
`selected_candidate_rank_before_bias == selected_candidate_rank_after_bias`,
and all 20-odd `*_active` diagnostic booleans False.

So 11 of the 13 live flags measure INERT for **one structural reason, not
eleven independent ones**: there is no modulatory pathway switched on for them
to act through. A per-signal contract asserted at this operating point would be
asserting over a configuration in which the mechanism under contract is off.

## Population (three corrections to the starting assumption)

The starting estimate was "342 `use_*` flags, 28 default-True". Both were wrong,
and how they were wrong matters for anyone building a gate on this:

| | claimed | actual | why |
|---|---|---|---|
| `use_*` bool fields | 342 | **173** | a `from_dims`/`enable_goal_stream` SIGNATURE default (8-space indent) is indistinguishable from a dataclass field (4-space) under a `^\s*` regex |
| default-True | 28 | **13** | same double-count |
| default-False | 314 | 160 | same |

Two further cases defeat source parsing entirely:

* **`use_resource_encoder`** declares `False` as a dataclass field and `True`
  as an `enable_goal_stream` parameter. Its default depends on the construction
  path; no reading of the declaration settles it.
* **`use_consumer_conjunction_read`** is a constructor parameter that is never
  an attribute of any config object.

Discovery therefore introspects a live default-constructed config. On that
basis: **175 `use_*` bools reachable, 13 True.**

## The table (bare default: `REEConfig.from_dims`, no profile method)

3 seeds (11/12/13) x 200 steps. `ticks` is the number of state-identical fresh
E3 ticks available for stage comparison; comparison stops at the first divergent
action because past that the two agents are solving different problems.

| flag | dies at | spread ratio | commit flips | realised differs | ticks |
|---|---|---|---|---|---|
| `use_bla_analog` | INERT | 0.0000 | 0 | no | 76 |
| `use_cea_analog` | INERT | 0.0000 | 0 | no | 76 |
| `use_curiosity_novelty` | INERT | 0.0000 | 0 | no | 76 |
| `use_curiosity_uncertainty` | INERT | 0.0000 | 0 | no | 76 |
| `use_curiosity_learning_progress` | INERT | 0.0000 | 0 | no | 76 |
| `use_e3_diversity_entropy_bonus` | INERT | 0.0000 | 0 | no | 76 |
| `use_e3_diversity_stratified_select` | INERT | 0.0000 | 0 | no | 76 |
| `use_escape_relief_credit` | INERT | 0.0000 | 0 | no | 76 |
| `use_escape_safety_credit` | INERT | 0.0000 | 0 | no | 76 |
| `use_trainable_relief_critic` | INERT | 0.0000 | 0 | no | 76 |
| `use_trainable_safety_predictor` | INERT | 0.0000 | 0 | no | 76 |
| `use_support_preserving_cem` | REALISED | n/a | 0 | **yes** | 0 |
| `use_curiosity_familiarity` | **PRECONDITION_FAIL** | -- | -- | -- | 0 |

Null control (ON-vs-ON) clean on every measured row.

**Eligibility and arbitration columns are empty because those stages do not
run.** `use_modulatory_shortlist_then_modulate`, `use_f_eligibility_demotion`,
`use_go_nogo_constitution` and `use_dualsystem_arbitration` are all default-OFF,
so the live chain is scoring -> committed -> realised. Confirmed three ways:
source trace of the branch gates; E3 diagnostics
(`modulatory_shortlist_active=False`, `f_eligibility_demotion_active=False`);
and switching the flags on, which still yields INERT because the eligibility
branch additionally requires a populated `_modulatory_accum`.

### Two rows that are findings in their own right

**`use_curiosity_familiarity` -- PRECONDITION_FAIL.** The override does not
reach `HippocampalConfig` through `from_dims` at all. This flag **cannot be
ablated by the normal construction path**. Without the precondition check it
would have reported INERT -- a false negative indistinguishable from a finding.

**`use_support_preserving_cem` -- REALISED, 0 comparable ticks.** It is the one
live flag with genuine behavioural throughput, but the arms diverge on the FIRST
action, so the probe cannot localise which stage carries it. Localising a
signal that diverges immediately needs a forced-lockstep mode (execute arm A's
action in arm B while still reading B's stage outputs), which this probe does
not have. Named as a known limitation, not papered over.

## Second operating point: harm streams enabled

`use_bla_analog` and `use_cea_analog` are **default-ON consumers of a
default-OFF producer**. `LatentStack` constructs `harm_encoder` /
`affective_harm_encoder` only under `use_harm_stream` (SD-010) /
`use_affective_harm_stream` (SD-011), both default-OFF, so `latent.z_harm` and
`latent.z_harm_a` are `None` **even though the environment supplies `harm_obs`
(51-dim) and `harm_obs_a` (50-dim) and the canonical `StepHarness` passes both
into `sense()`**. The dims are configured (`harm_obs_dim=51`, `z_harm_dim=32`);
the encoders are simply never built.

This is the EXP-0155 shape (a registered mechanism with no causal channel),
found mechanically rather than by hand.

Re-probed with `--base use_harm_stream=true use_affective_harm_stream=true`,
3 seeds x 200 steps, 80 comparable ticks: **both still INERT.** So the
producer's absence is not the whole story for these two -- with `z_harm` live,
they still contribute nothing to the pre-commit score at this operating point.

## The real cost driver

Measured over the v3 experiment corpus (1361 `experiments/v3_exq_*.py` drivers):

* **343 distinct flag-set operating points**
* **196 distinct `use_*` flags** ever enabled by a driver (more than the 173
  config fields -- drivers also set env and constructor-only switches)
* 357 drivers enable no `use_*` flag at all
* only 5 drivers invoke a `goal_stream` profile method

The dominant operating-point dimension is **which streams exist**, not which
modulators are on: `use_proxy_fields` (531 drivers), `use_harm_stream` (442),
`use_affective_harm_stream` (414), `use_resource_proximity_head` (280).

A universal per-signal, per-stage contract is therefore not 173 x 5 = 865
assertions. Because the verdict is demonstrably operating-point-dependent, it is
**196 x 5 x 343**. That is the number that kills the universal-contract framing,
and it is measured rather than asserted.

## Instrument defects found while building it

Recorded because each is the exact failure class the probe exists to detect,
occurring inside the probe:

1. **Scored the wrong tensor.** The scoring column compared `last_raw_scores`
   (assigned `e3_selector.py:2773`) when every modulatory term lands between
   there and `last_scores` (`:3350`). It returned INERT for a contrast that
   moved the final score on every tick. Caught mid-sweep; verified
   differentially against the pre-fix commit. Had it not been caught, the
   published table would have been all false INERTs.
2. **Read inactive sentinels as sizes.** `modulatory_shortlist_size=0` and
   `f_eligibility_envelope_size=-1` are inactive markers, so an `is not None`
   test reported the eligibility stage ACTIVE in a config that skips it.
3. **Population double-counted ~2x** by source parsing (above).

## Recommendation

1. **Do not build per-signal, per-stage contracts.** The measured fanout is
   ~196 x 5 x 343, and 160 of 173 flags are default-off, so the overwhelming
   majority of such assertions would pin `authority == 0` on an inert knob --
   vacuous green.
2. **Do build the registry-completeness lint** -- no term may enter `scores`
   without a registered channel name. O(1) test cost for O(N) coverage. Today
   the registry is 9 names (`ofc, dacc, lpfc, vigour, liking, gated_policy,
   residual, mech341, route`) and `residual` explicitly absorbs "any future
   term" (`e3_selector.py:76`).
3. **Do keep the per-signal artefact a MEASUREMENT, not a contract**, on
   `inert_arm_knob.py`'s existing posture: record-and-warn at write, gate at
   adjudication.
4. **Highest-value extension is outward, to `claims.yaml`, not deeper into the
   substrate.** Both EXP-0155 and the BLA/CeA finding here are mismatches
   between a registered claim's asserted mechanism and the code's causal reach.
   Both ends already exist as data; the missing thing is the join.
5. **Next probe, if this is pursued:** run the same sweep at the ~10 most
   common real operating points rather than at the default, and add the
   forced-lockstep mode so an immediately-diverging signal can still be
   localised.

## Caveats

* Untrained agent, no warmup, `CausalGridWorldV2` 5x5, 200 steps. Signals whose
  contribution depends on learned statistics (learning-progress curiosity,
  trainable critics) may be structurally zero here for that reason alone,
  independent of the score_bias finding.
* `--base` takes flags only; profile methods (`enable_goal_stream`) are a
  further operating point this probe does not reach.
* The one REALISED row could not be stage-localised (see above).


---

# UPDATE (same session, after the operating-point sweep)

## Prior art this document's first version missed

`ree-v3/tests/test_flag_inertness.py` (3155 lines, built after the 2026-07-09
design+implementation audit) already does per-flag inertness probing, and exists
for the reason given at the top of this file: a config-gated mechanism that is
silently inert "measures the wrong thing and returns a plausible-looking null --
which then weights claim confidence as if it were a real negative result".

Two consequences.

**Recommendation 2 was half-redundant.** `test_flag_registry_is_current` IS the
O(1) registry-completeness gate recommended above -- for FLAGS. It enumerates
every top-level and nested `use_*` / `*_enabled` and fails if a new one appears
uncategorised, forcing "write a probe, or record it unprobed with a reason".
Extended to nested configs 2026-08-11.

**The gap is real but is about CHANNELS, not flags.** No equivalent gate exists
for score channels. `tests/contracts/test_mech451_finer_channel_gating.py` pins
the 9 channel names and asserts "residual exhaustiveness" -- it GUARANTEES the
catch-all works, which is the opposite of forcing registration. A new modulatory
term is contractually permitted to disappear into `residual`.

**Its own numbers answer the scaling question better than the argument above
did.** After ~13 months of hand-written probes: **101 flags PROBED, 80
KNOWN_UNPROBED, 3 KNOWN_INERT.** Hand-authoring stalls near 55% coverage. That
is the measured case for an automated ablation sweep -- not that hand probes are
wrong, but that they demonstrably do not finish.

## Forced-lockstep mode

The free run's stage comparison ends at the first divergent action, so a signal
that diverges immediately gets zero comparable ticks. `--lockstep` drives the
follower along the LEADER's action sequence: its own `select()` still runs and
every stage tensor is captured from it, but the action handed to the environment
is the leader's, so both arms see an identical world for the whole episode.
Implemented by wrapping `agent.select_action`, not by editing `StepHarness`.

The follower is a CHIMERA -- its E3 commitment state evolves from its own
selection while its world evolves from the leader's action. That is inherent to
a matched-state counterfactual, and is why lockstep is reported ALONGSIDE the
free run: the authority/throughput pairing IS the V3-EXQ-931/932 finding.

Effect on the one row the first pass could not localise:
`use_support_preserving_cem` went from **0 comparable ticks to 32, with 22
committed flips at matched state**.

## Operating-point sweep

8 operating points drawn from the real corpus, 2 seeds x 100 steps, lockstep on.
`sc_mv` / `cm_mv` = flags moving the score / the committed choice at matched
state.

| operating point | live flags | INERT | REALISED | PREF | sc_mv | cm_mv | matched ticks |
|---|---|---|---|---|---|---|---|
| bare default | 13 | 11 | 1 | 1 | 1 | 1 | 324 |
| `harm_stream` | 14 | 11 | 2 | 1 | 2 | 2 | 333 |
| `+affective_harm` | 15 | 11 | 3 | 1 | 3 | 3 | 396 |
| `resource_proximity_head` | 14 | 11 | 2 | 1 | 2 | 2 | 512 |
| `harm+aff+rph` | 16 | 11 | 4 | 1 | 4 | 4 | 371 |
| `event_classifier+rph` | 15 | 11 | 3 | 1 | 3 | 3 | 416 |
| `+sleep_loop` | 17 | 12 | 4 | 1 | 4 | 4 | 397 |
| `+ofc+support_preserving_cem` | 17 | 11 | 5 | 1 | 5 | 5 | 433 |

**Eleven default-ON flags moved NOTHING at any operating point, across ~3182
matched-state ticks**: `use_bla_analog`, `use_cea_analog`,
`use_curiosity_novelty`, `use_curiosity_uncertainty`,
`use_curiosity_learning_progress`, `use_e3_diversity_entropy_bonus`,
`use_e3_diversity_stratified_select`, `use_escape_relief_credit`,
`use_escape_safety_credit`, `use_trainable_relief_critic`,
`use_trainable_safety_predictor`.

**`sc_mv == cm_mv` at every operating point** -- not one instance of authority
without throughput. Every signal that moved the score also flipped the commit.
That is because the movers are STRUCTURAL flags (which streams and encoders
exist), not subtle modulatory biases; it is not evidence that the V3-EXQ-931
pattern is rare.

Flags that did move the commit, by operating-point count: `support_preserving_cem`
8/8, `harm_stream` 5/8, `resource_proximity_head` 5/8, `affective_harm_stream`
4/8, `event_classifier` 1/8, `ofc_analog` 1/8.

**Two rows that must NOT be read as findings.** `use_curiosity_familiarity` is
PRECONDITION_FAIL at all 8 points -- never measured, not "never moved" (and see
the correction below). `use_sleep_loop` shows no effect, but at one operating
point and 100 steps, which is near-certainly too short for a sleep loop to
trigger -- a measurement-window artifact, not a result.

## Root cause: score_bias is identically zero everywhere tested

`scores` is bit-identical to `raw_scores` in **12** configurations: the bare
default, the 8 corpus operating points, and `enable_goal_stream()` with
`use_ofc_analog` and `use_dacc`. Traced to two gates:

**(1) The producer sits behind a conjunction most drivers do not satisfy.**
`agent.py:6888` gates the dACC->E3 bias on
`self.dacc is not None and z_harm_a is not None`. `use_dacc` alone is
insufficient -- `z_harm_a` requires `use_affective_harm_stream` (SD-011). The
adapter is CONSTRUCTED either way, so it looks wired; `_dacc_last_bundle` stays
None. **98 of 1361 drivers set both.**

**(2) When it does run, the emitted bias has zero cross-candidate spread.** With
the conjunction satisfied, `_dacc_last_bias` is a real tensor with spread
`0.0` -- a uniform scalar added to every candidate, invariant under
argmin/softmax however large. This is the already-catalogued **F-C2** from the
2026-07-09 audit (`dacc_foraging_weight` "dead-by-construction on the E3 leg"),
independently re-measured here and extending beyond the foraging term to the
whole emitted bias. **Caveat: untrained adapter.** A trained head might produce
spread; that has not been shown either way.

## The actual hole -- and it is one assertion, not a contract matrix

`test_mech451_finer_channel_gating.py` passes `score_bias` in BY HAND:
`sel.select(cands, score_bias=torch.tensor([0.0, -0.3, 0.2, -0.1]))`. It tests
the decomposition machinery well and would keep passing if the production
producer were entirely dead. The residual-exhaustiveness contract likewise
guarantees the catch-all rather than forcing registration.

So the gap is not "we lack per-signal tracing". It is:

> **Nothing asserts that the production path ever produces a non-degenerate
> `score_bias`.** The flag-inertness harness checks flags; the channel contracts
> check decomposition against injected input. Neither closes the loop.

That is ONE assertion, not 196 x 5 x 343: *in a configuration satisfying the
producer's preconditions, the score_bias reaching `select()` has non-zero
cross-candidate SPREAD*. Spread, not magnitude -- which is exactly the F-C2
distinction and exactly the readiness floor the CEM work already ratified
(`authority_spread_ratio` >= 0.1).

## Corrections to this document's first version

* **The `use_curiosity_familiarity` finding was an OVER-CLAIM and its chip was
  withdrawn** (`chip-20260822-curiosity-familiarity-unablatable`). It IS
  ablatable by constructing `HippocampalConfig(...)` directly -- what
  `tests/contracts/test_sd025_curiosity_drive.py` C5 and drivers `v3_exq_767` /
  `v3_exq_768` all do -- and direct sub-config construction is an accepted idiom
  here (`v3_exq_228b/c/d` set `cfg.latent.use_resource_encoder` the same way). It
  is already listed PROBED in the inertness harness, and no driver passes it
  through `from_dims`. The residual real issue -- `from_dims` silently swallowing
  unknown kwargs, confirmed to have bitten `beta_gate_bistable` on 2026-08-22 --
  is scoped in the replacement chip
  `chip-20260822-fromdims-swallowed-flag-audit`.
* Two other apparent findings were likewise false: `use_interventional` is a
  local function parameter, not a config flag, and `use_resource_encoder` is set
  by attribute assignment by design.
* The general lesson, since it recurred three times in one session: the "does
  not land through `from_dims`" signal is necessary but nowhere near sufficient
  for "defect". Grep `experiments/` for how the flag is ACTUALLY set before
  calling anything broken.

## Revised recommendation

1. **Do not build per-signal, per-stage contracts.** Unchanged, and now with a
   second measured reason: hand-authored per-flag probes already exist and
   stalled at ~55% coverage after 13 months.
2. **Build the end-to-end score_bias spread assertion** (above). One test.
   Highest value per unit cost of anything in this document.
3. **The channel-registry lint is still worth having**, narrowed: it is about
   score channels, not flags -- the flag equivalent already exists.
4. **Keep the per-signal artefact a MEASUREMENT**, on `inert_arm_knob.py`'s
   record-and-warn-at-write / gate-at-adjudication posture. The automated sweep
   is what gets past the hand-authoring ceiling.
5. **Extend outward to `claims.yaml`.** Unchanged and reinforced: the BLA/CeA
   result and EXP-0155 are both mismatches between a registered claim's asserted
   mechanism and the code's causal reach.

## Residual caveats

* Untrained agent, no warmup, `CausalGridWorldV2` 5x5, 100-200 steps. Signals
  depending on learned statistics may be zero for that reason alone. This is the
  single largest threat to the inertness results and is NOT controlled for.
* `use_ofc_analog` moved the commit at one operating point while `score_bias`
  stayed zero, so OFC reaches selection by some path other than the score-bias
  channel. Not chased down.
* Operating points were reconstructed from driver source by regex over
  `use_*=True`, then filtered to those whose flags land through `from_dims`.
  Points needing direct sub-config construction or a profile method are not
  represented.
