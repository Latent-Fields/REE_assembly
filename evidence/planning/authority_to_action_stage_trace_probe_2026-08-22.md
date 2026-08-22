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
