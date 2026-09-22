# precondition_gate structural-bound coverage: triage of the bound-less call sites

Written 2026-09-22T20:55:43Z. Probe for chip `chip-20260922-precondition-bound-coverage-triage`.
Measured against ree-v3 **pinned commit `8f10214e6a`** (`origin/main` at the time of writing) --
not the shared working tree, which carries other sessions' uncommitted edits.

Context: ree-v3 `fa7696381c` made `assert_no_structurally_unsatisfiable_gate`
(`experiments/_lib/precondition_gate.py`) honest -- a `PreconditionSpec` declaring neither
`structural_max` nor `structural_min` now audits as `not_evaluated` rather than silently
`satisfiable`, and the guard prints a coverage denominator. It deliberately did not retro-fit the
call sites and deliberately did not become a blocking gate. This document answers the question
that left open: **of the bound-less drivers, how many could actually carry a structural bound?**

---

## HEADLINE

Of the **67 bound-less drivers** (of 108 that call the guard, at `8f10214e6a`):

| Bucket | Drivers | Specs | Meaning |
|---|---:|---:|---|
| **(A) MECHANICALLY DERIVABLE** | **15** | 74 | The bounding number is pre-registered in the driver, and the bound **can actually fire** for a declared arm or run mode. |
| **(B) DERIVABLE BUT NEEDS A DESIGN DECISION** | **30** | 124 | A bound exists in principle but is either *inert* (provably never binds) or requires pre-registering something the driver does not currently declare. |
| **(C) GENUINELY NOT BOUNDABLE** | **22** | 94 | Every spec measures an emergent substrate quantity with no design-time ceiling. `not_evaluated` is the correct and final answer. |

**The decision this supports: do not run a 67-driver retro-fit campaign.** Run a 15-driver one,
and gate it behind a single shared enabler (below), because all 15 are the *same defect*.

Two findings matter more than the bucket split itself:

1. **Bucket A is not 15 unrelated retro-fits. It is one defect class, 15 times.** Every
   bucket-A driver fails the same way V3-EXQ-1062 did: a **sample-count floor sized for the
   full run, evaluated under a reduced `--dry-run` / smoke budget that cannot reach it**. The
   fix is not 15 bespoke lambdas; it is one convention -- *put the resolved run-mode budget
   into the arm context* -- after which each driver needs a one-line `structural_max`.

2. **The coverage gap is much larger than the 67/108 file-level figure suggests, and much of
   it is already mitigated by a different mechanism.** At spec level only **110 of 526 specs
   (20.9%)** carry a bound. But **221 specs carry `applies_to`**, which discharges disposition
   (a) ("not meaningful for this regime") -- the other half of the module's own two-disposition
   model. The genuinely unguarded population is the **263 of 526 specs (50%) that carry
   NEITHER**, concentrated in **19 of the 67** bound-less drivers that use no regime
   conditioning at all.

---

## CORRECTION TO THE PUBLISHED FIGURE

`precondition_gate.py`'s docstring currently states: *"108 drivers call the guard, 43 declare a
structural bound, and 65 (60%) declare neither."* That count is a `grep` for the strings
`structural_max|structural_min`. An AST count of actual `PreconditionSpec(...)` keyword arguments
gives **108 drivers, 41 bounded, 67 bare**.

The 4-driver delta is entirely `grep` over-counting, and each case is instructive:

| Driver | Why grep called it bounded |
|---|---|
| `v3_exq_834_arc071_mech323_budget_coupled_ceilings.py` | declares a local variable `structural_max_depth` -- a different referent that shares the token |
| `v3_exq_839_sd084_midexec_reachability.py` | prose: *"No `structural_max` / `structural_min` is declarable: both are emergent"* -- a file documenting that it is bucket C |
| `v3_exq_874b_mech467_distractor_three_leg_battery.py` | comment: *"no pre-registered constant bounds, so no structural_max/min applies"* |
| `v3_exq_1062a_...postshift.py` | genuinely bounded (it *does* declare `structural_max`); counted correctly by both -- included here only because it landed on `main` mid-measurement (see Limitations) |

Three of the four are files that say *in words* they cannot be bounded, counted as bounded.
This is the "token match is not referent match" failure applied to the instrument's own
self-report. **Recommend updating the docstring figure to 41/67 and citing the AST method.**

---

## (A) MECHANICALLY DERIVABLE -- 15 drivers

All 15 share one shape. The driver pre-registers a sample-count floor computed from the
**full-run** budget, then resolves a **reduced** budget under `--dry-run`/smoke while leaving the
floor at full size. The guard cannot see this because **the arm context does not carry the
budget**.

### The worked example, verified

**`v3_exq_1062_mech055_affect_channel_separation_diagnostic.py`** (the motivating case):
- `FRESH_TICKS_MIN = 200`; spec `fresh_select_sample_floor` has `threshold=float(FRESH_TICKS_MIN)`.
- `_run_cell` resolves `p2_budget = 60 if dry_run else P2_STEP_BUDGET` (`P2_STEP_BUDGET = 1800`).
- `arm_contexts = {a["arm_id"]: {"arm_id": ..., "is_shift": ...}}` -- **the budget is not in ctx.**
- Under `--dry-run` the floor of 200 is unreachable from 60 steps. The guard ran and proved nothing.

Bound (`n_fresh_select` cannot exceed the number of P2 steps):

```python
# ctx gains one key:
arm_contexts = {a["arm_id"]: {"arm_id": a["arm_id"], "is_shift": a["is_shift"],
                              "p2_budget": 60 if dry_run else P2_STEP_BUDGET} for a in ARMS}
# spec gains one line:
structural_max=lambda ctx: float(ctx["p2_budget"]),
```

### Second verified case, independently confirming the class

**`v3_exq_840_mech294_theta_packet_binding_committed_action_falsifier.py`** (and `840b`):
- `NOMINAL_WINDOW_TICKS = P1_MEASUREMENT_EPISODES * (STEPS_PER_EPISODE - MEASURE_AFTER_TICK)`
  = `20 * (200 - 20)` = **3600**; `FRESH_SELECT_FLOOR = 3600 // BETA_RATE_MAX_STEPS` = **180**.
- `COMMITTED_WINDOW_FLOOR = 200`.
- Dry-run resolves `p1 = DRY_RUN_P1 = 2`, `steps = DRY_RUN_STEPS = 30`,
  `measure_after = DRY_RUN_MEASURE_AFTER_TICK = 2` -> window = `2 * (30 - 2)` = **56 ticks**.
- Both floors (180, 200) exceed the entire 56-tick dry-run window. `ARM_CONTEXTS` is a
  module-level constant that never learns the mode.

Bound: `structural_max=lambda ctx: ctx["window_ticks"] / BETA_RATE_MAX_STEPS` (and
`ctx["window_ticks"]` for the committed-window spec), once ctx carries the resolved window.

### Third verified case

**`v3_exq_977_arc052_harm_stream_conditional_precision.py`**: `R0_MIN_TEST_TRANSITIONS = 200`;
dry-run resolves `collect_eps = DRY_RUN_COLLECT = 3`, `steps_ep = DRY_RUN_STEPS = 25` -> at most
**75** transitions collected, and the test split is a subset of those. Floor 200 is unreachable.
Bound: `structural_max=lambda ctx: float(ctx["collect_eps"] * ctx["steps_ep"])`.

### The full bucket-A set

| Driver | Bound-less spec(s) carrying the pattern |
|---|---|
| `v3_exq_1012a_e3_commensurability_selection_level_regime_validation.py` | `decomp_samples_sufficient` |
| `v3_exq_1018_mech005_nu_path_authority_live_agent.py` | `commit_channel_live`, `fresh_selects_per_cell` |
| `v3_exq_1062_mech055_affect_channel_separation_diagnostic.py` | `fresh_select_sample_floor` **(verified)** |
| `v3_exq_571c_e3_variance_monopoly_presence_936_regime.py` | `decomp_samples_sufficient`, `n_live_channels` |
| `v3_exq_687a_mech313_committed_authority_dissociation.py` | `fresh_select_sufficiency` |
| `v3_exq_791a_channel_routing_cross_class_magnitude_replication.py` | `adequate_fresh_selection_sample`, `fresh_selection_yield_supra_cadence_floor` |
| `v3_exq_799_mech048_stability_temperature_behavioural_did.py` | `fresh_select_sufficiency` |
| `v3_exq_805_arc016_eval_derived_commit_threshold.py` | `commit_decision_count` (`MIN_COMMIT_DECISIONS = 200.0`) |
| `v3_exq_833_stageh_strict_goal_isolation_dv.py` | `survival_above_floor` |
| `v3_exq_840_mech294_theta_packet_binding_committed_action_falsifier.py` | `adequate_fresh_selection_sample`, `adequate_committed_window_sample` **(verified)** |
| `v3_exq_840b_mech294_...falsifier.py` | same two **(verified, same constants)** |
| `v3_exq_970a_contextmemory_write_content_h1_mi_instrument.py` | `writepath_engaged` |
| `v3_exq_972a_sd070_write_stream_heldout_linear_probe.py` | `writepath_engaged` |
| `v3_exq_977_arc052_harm_stream_conditional_precision.py` | `n_test_transitions_supra_floor` **(verified)** |
| `v3_exq_983_ext002_residue_error_persistence.py` | `revisit_denominator` (`THRESH_C4_MIN_REVISITS = 20` vs dry-run `max_steps = min(30, ...)`) |

Four were verified end-to-end by reading the dry-run resolution and arithmetic (1062, 840, 840b,
977, plus 805/983 pattern-confirmed at the constant level). The remaining nine match the
structural signature -- integer count floor, reduced-budget mode present, threshold not
mode-aware -- but their dry-run products were not re-derived individually.

### Note: some drivers already solved this by hand

`v3_exq_1015` (`P0B_MIN_STEPS_DRY = 5` vs `P0B_MIN_STEPS = 200`), `v3_exq_848/848a/848b`
(`DRY_P3_SALIENCE_TICK_FLOOR = 5.0` vs `P3_SALIENCE_TICK_FLOOR = 150.0`), `v3_exq_940`/`941`
(`SMOKE_MIN_REALISED_TICKS`), `v3_exq_874b` (`SMOKE_MIN_EVENTS`) all scale the **floor** with the
budget. They are not in bucket A -- they are already protected, by a hand-written convention that
**bucket A's 15 drivers simply did not adopt**. That this convention exists and is used by at
least 7 drivers is the strongest argument that the bucket-A fix is routine rather than novel.

`v3_exq_1015` additionally already carries capacity in ctx (`p0a_episodes`, `p0b_episodes`) and
uses `applies_to=lambda c: c["p0b_episodes"] > 0` to scope out its zero-warmup arms -- i.e. it
handles disposition (a) correctly and needs no `structural_max`.

---

## (B) DERIVABLE BUT NEEDS A DESIGN DECISION -- 30 drivers

Two sub-shapes.

### B1. Bounded fraction, bound is INERT (9 drivers)

`v3_exq_813`, `836`, `836a`, `836b`, `836c`, `836d`, `836e`, `885`, `925a`, `948`.

Canonical: the `836*` family's `install_took_strict_majority`, where
`install_took_frac = n_install_took / n_cells` is a fraction in `[0, 1]` tested against
`INSTALL_TOOK_MAJORITY = 0.5`. A `structural_max=lambda ctx: 1.0` is trivially correct and
**provably never binds**.

**The design decision is whether an inert bound is worth writing.** It would convert
`not_evaluated` -> `satisfiable`, which repairs the *coverage denominator* honestly, but catches
nothing. Recommendation: write these only if the coverage statistic is going to be used as a
gate; otherwise they are ceremony, and ceremony in a safety instrument teaches readers that a
green audit means less than it does.

### B2. Config-determined liveness indicator (21 drivers)

`v3_exq_1006`, `1072`, `794`, `794a`, `800`, `839`, `844`, `850`(h1), `850`(h2), `860`, `864`,
`864a`, `867`, `867a`, `867b`, `874b`, `940`, `941`, `964`, `983a`.

Specs named `*_live`, `*_engaged`, `*_landed`, `*_fired`, `*_confirmed` -- e.g. `1012a`'s
`clamp_config_landed` / `residue_protocol_landed`, `1072`'s `offline_pathway_live`, the SD-076
family's `rv_live` / `f1_recalib_engaged`.

These assert *"the thing this arm is supposed to be doing is switched on"*. Their value is
**fully determined by the arm's own configuration**, which is exactly what ctx holds -- so a
bound is derivable. **The design decision is which disposition they belong to.** For an arm that
deliberately switches the feature OFF (a control arm), the honest declaration is
`applies_to` (disposition (a), "not meaningful here"), **not** `structural_max` (disposition (b),
"vacuous, exclude from scoring"). Getting this backwards is the failure the module docstring
warns about most sharply: treating (b) as (a) launders a vacuous arm into a citable one.

So B2 is not a lambda-writing task. It is: *for each of these specs, decide whether the OFF arm is
scoped-out-but-scorable or vacuous-and-excluded, and declare accordingly.* That is a per-driver
scientific judgement and should be made by whoever owns the claim, not by a retro-fit sweep.

`v3_exq_1072` is worth calling out: its five `MIN_*` readiness floors are all `0.0` with strict
`>`. A structural bound is derivable (counts cannot exceed `SMOKE_STEPS = 150`) but can never
bind against a floor of zero -- B1-inert in a B2 costume.

---

## (C) GENUINELY NOT BOUNDABLE -- 22 drivers

`v3_exq_1010`, `1015`, `1044`, `1046`, `1050`, `114a`, `120a`, `266b`, `801`, `802`, `830`,
`834`, `841`, `846`, `848`, `848a`, `848b`, `919`, `932a`, `938`, `964a`, `978`.

Every spec measures an emergent substrate quantity: a correlation or `r2`
(`harm_a_forward_r2`, `e2_world_r2_adequate`), a range or spread (`rollout_score_range`,
`cond_message_spread`, `precision_cross_seed_sd`), an elevation or divergence
(`head_native_elevation`, `theta_summary_divergence`), a participation ratio, a variance, a
reproduction fraction against a measured reference (`1010`'s `MEMORISE_FLOOR = 0.95`).

**These are the honest `not_evaluated` cases and the new reporting is already correct for them.**
Two of them (`839`, `874b` -- classified B here on other specs) say so in their own source. No
action; a bound would have to be invented, and an invented bound on a substrate quantity is a
pre-registration of the result.

One nuance inside C: the `114a`/`120a`/`266b` family's `candidate_action_diversity` (threshold
`1.5`) is bounded by the size of the action space, a design-time constant. That is a derivable but
inert bound -- B1 in character. It is left in C because the action-space size is not currently a
module constant in those drivers, so lifting it is a change to what they pre-register.

---

## METHOD, AND WHAT THIS INSTRUMENT CANNOT SEE

Measurement is AST-based, not `grep`-based: every `PreconditionSpec(...)` call is parsed and its
keyword arguments inspected. Scripts are in this session's scratchpad; the pipeline is
reproducible from the pinned SHA in ~30s.

**Denominator check.** All 108 guard-calling drivers build their specs from literal
`PreconditionSpec(...)` calls -- **zero** construct them dynamically. So the spec-level
denominator (526) is complete, not a lower bound.

Per CLAUDE.md's negative-instrument rule, the blind spots this triage's own search carries,
measured rather than asserted:

1. **A canary caught a real miss.** The first version of the bucket-A detector **failed to flag
   V3-EXQ-1062 itself** -- twice. Once because 1062's dry-run budget is an inline
   `60 if dry_run else ...` expression rather than a `DRY_RUN_*` module constant; once because
   the spec name `fresh_select_sample_floor` did not match a regex containing only the plural
   `samples`. The detector now asserts that 1062 reproduces before reporting any count. Without
   that canary the headline would have read **6**, not 15 -- a 60% under-count, in the
   fail-quiet direction.
2. **Lowercase-local thresholds are invisible to a constant-name scan.** 10 specs across 8
   drivers set `threshold=` from a lowercase local rather than an uppercase module constant
   (`848`'s `salience_tick_floor`, `940`/`941`'s `min_ticks`/`min_dist`, `874b`'s `min_events`).
   Checked by hand: **all 8 are the already-mode-aware pattern**, so this blind spot skews toward
   already-protected drivers and does not inflate C at A's expense. It is not zero-risk.
3. **ctx keys resolve for only 23 of 67 drivers.** Where the arm context is built inside a
   helper, the key list is unresolved, so "does ctx already carry the bounding number" is a
   *lower* bound: 4 drivers confirmed (`1015`, `1050`, `801`, `266b`). The bucket-A remedy does
   not depend on this -- all 15 need a ctx addition regardless.
4. **`origin/main` moved mid-measurement.** The first pass ran against a ref that advanced
   (`a4c47c5` V3-EXQ-1062a landed during it), which is how the 1062a discrepancy surfaced. Every
   number here was re-derived against pinned `8f10214e6a`. Bucket counts were identical across
   both refs; the totals moved 107->108 drivers and 518->526 specs.

---

## RECOMMENDATION

**Run a bucket-A campaign only, and land the shared enabler first.**

1. **Enabler (1 change, `experiments/_lib/`):** a convention -- and ideally a small helper -- for
   injecting the **resolved run-mode budget** into every arm context. Every one of the 15
   bucket-A drivers is blocked on the same thing: the guard is handed a ctx that cannot see
   whether this is a dry run. Without it, all 15 fixes are bespoke; with it, each is one line.
2. **Bucket A (15 drivers):** add the ctx key and the `structural_max` lambda. Expected yield:
   the guard starts refusing `--dry-run` invocations whose sample floors are unreachable --
   which is precisely the smoke-test-passes-then-real-run-is-vacuous failure that burned
   V3-EXQ-1062.
3. **Bucket B2 (21 drivers): do NOT sweep.** Route to the owning claim. The question is
   `applies_to` vs `structural_max` -- disposition (a) vs (b) -- and getting it wrong
   manufactures support rather than merely burying a result.
4. **Bucket B1 (9 drivers) and bucket C (22 drivers): no action.** B1's bounds are inert; C's
   would have to be invented.
5. **Update the docstring's 43/65 figure to 41/67** and state the AST method, so the instrument's
   own self-report is not itself a token-match artifact.

**Still not recommended, and not reopened here:** making the guard blocking, or adding a coverage
floor. At 20.9% spec-level coverage either would fire on a large majority of correct drivers, and
CLAUDE.md is explicit about what happens to a guard that fires on correct code. The case for
report-not-block is stronger after this triage, not weaker: **44 of the 67 bound-less drivers
(B1 + C, plus the inert half of B2) are bound-less because a bound is meaningless for them,
not because anyone forgot.**
