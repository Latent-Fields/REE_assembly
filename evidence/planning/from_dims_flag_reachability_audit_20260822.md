# `REEConfig.from_dims()` flag-reachability audit

**Date:** 2026-08-22T14:25:12Z
**Session:** `serene-yalow-3dd4b0` (chip `chip-20260822-fromdims-swallowed-flag-audit`)
**Substrate base:** `ree-v3` `origin/main` @ `cd1e127`
**Artifact:** `ree-v3/tests/contracts/test_from_dims_flag_reachability.py` (the standing guard)

## Question

`REEConfig.from_dims(**kwargs)` silently ignores an unknown kwarg -- no error,
no warning -- so `from_dims(some_flag=False)` can be a complete no-op while
reading exactly like a working ablation. Nothing in the repo enumerated *which*
knobs are affected. `tests/test_flag_inertness.py::test_flag_registry_is_current`
gates that every flag is *categorised*, which is a different question from
whether it is *reachable through the canonical constructor*.

This audit answers the reachability question by EXECUTION, not by source
parsing: it calls `from_dims` with each knob overridden and reads the value
back off the live config tree.

## Method

- Recursive walk of every `*Config` object reachable from `REEConfig` (**17**
  objects). `scripts/authority_trace_probe._config_objects` descends only one
  level and cannot see the six two-deep objects under `hippocampal`.
- **1006** scalar fields swept (bool / int / float; `str` fields are
  enum-validated and excluded). Each is set to two values of its own type and
  read back per config path.
- Verdicts: `LANDS` / `PARTIAL` (lands on some paths carrying the name) /
  `UNREACHABLE`.
- Call-site scan: AST over `experiments/**` (1466 files) for names passed into
  `from_dims` or one of its four forwarding classmethods.

## Headline results

| verdict | count |
|---|---|
| `LANDS` | 856 |
| `UNREACHABLE` | 149 |
| `PARTIAL` | 1 |

Of the **206** bool flags, **37** are unreachable through `from_dims`.

**Signature membership is not the answer, and comes apart in BOTH directions.**
Six names land with no signature entry (explicit `kwargs.pop` reads:
`use_iterative_inference`, `inference_settle_iters`,
`inference_convergence_rel_tol`, `use_self_recurrence`,
`self_recurrence_e1_coupling`, `use_cross_module_consolidation` + companions),
and one name has a signature entry and still does not land
(`sd016_diversification_weight` -- see Defect 1).

**The two naming conventions used elsewhere are insufficient.** 13 of the 37
unreachable bools match neither `use_*` nor `*_enabled`, including
`beta_gate_bistable` -- the flag whose silent swallow was measured live on
2026-08-22 (session `igw-232-mech091-driver-successor`), which left MECH-091's
completion trigger structurally unreachable.

## Classification (the part that matters)

A flag being unreachable through `from_dims` is **not** by itself a defect.
Direct sub-config construction (`HippocampalConfig(...)`), attribute assignment
(`cfg.latent.use_resource_encoder = True`) and profile methods
(`enable_goal_stream`) are all accepted idioms in this repo.

| class | count | meaning |
|---|---|---|
| Reachable by an accepted alternative idiom | 26 | documentation gap |
| No confirmed caller anywhere | 6 | dataclass-only; nothing has ever set it |
| **Live `from_dims` call site losing a value** | **7 names** | **defect** |

This distinction is what invalidated the predecessor chip
(`chip-20260822-curiosity-familiarity-unablatable`, withdrawn):
`use_curiosity_familiarity` is unreachable through `from_dims` but is ablated
by `HippocampalConfig(...)` in `test_sd025_curiosity_drive.py` C5 and drivers
`v3_exq_767` / `v3_exq_768`. It is a documentation gap, not a defect.

## Confirmed defects

### 1. `sd016_diversification_weight` -- OPEN, and the sharpest of the seven

In the `from_dims` signature since 2026-06-05; the body never assigns it. So it
is **accepted** (no `**kwargs` swallow, no `TypeError`) and then dropped. A
signature entry actively *advertises* reachability, which makes this worse than
the `**kwargs` case.

Consumer: `ree_core/agent.py` `compute_prediction_loss`, gated
`_div_w > 0.0 and sd016_enabled`. **10 of 11 drivers** pass
`SD016_DIVERSIFICATION_WEIGHT = 0.5` and trained with the diversification loss
term OFF (`v3_exq_418f` passes 0.0 and is unaffected): `v3_exq_265a`,
`418l`, `436a`, `436b`, `436c`, `436d`, `436e`, `436f`, `500a`, `503a`.

Five *other* drivers (`418e`, `418g`, `418i`, `418j`, `418k`) set the same
field by attribute assignment and are unaffected -- the working idiom is already
in the corpus, next to the broken one.

**Repair (written and verified 2026-08-22, NOT landed):** one line in
`from_dims`, beside the other SD-016 assignments:

```python
config.sd016_diversification_weight = sd016_diversification_weight
```

Verified: with it, `from_dims(sd016_diversification_weight=0.5)` yields 0.5 and
the default stays 0.0, so every unaffected driver is bit-identical. It was NOT
landed because `ree_core/utils/config.py` was held by a concurrent claim -- see
"Concurrency" below.

### 2. `harm_descending_mod_enabled` -- SEVEREST: a dead ablation axis

`v3_exq_325`'s DESCENDING vs CONTROL arms are distinguished **only** by this
kwarg. The driver has no downstream `if descending:` branch; it relies on the
substrate honouring the config (`agent.py:4940` reads it), and its own comment
says so ("we measure the latent AFTER sense() which includes descending
modulation").

**Verified by construction:** `make_config(True)` and `make_config(False)`
return configs whose `REEConfig` top-level fields are **identical**. The two
arms are the same experiment.

Affects 6 drivers: `v3_exq_325`, `325a`, `325c`, `325d`, `325e`, `325f`.
Companion knob `descending_attenuation_factor` is dropped in the same calls
(harmless today -- every call passes 0.5, which is the default).

### 3. `gated_policy_use_differential_heads` -- an unarmed mechanism, 10 files

Passed `True` in all ten, commented `# ARC-062 fix.` -- so the fix is not
applied, in **both** arms (it sits in the shared builder; the arm difference is
`**xtal_kwargs`). Consumer: `agent.py:1128`. The same builder sets
`config.heartbeat.beta_gate_bistable` and `config.harm_descending_mod_enabled`
by attribute assignment three lines later, and **those land** -- the working
idiom is in the file, immediately below the broken one.

Affects `v3_exq_610`, `610a`-`610f`, `655`, `656`, and
`experiments/_lib/baselines/exq610_inv074_crystallization_baseline.py`.

### 4. `use_resource_encoder` -- `v3_exq_527`

`True` on the GOAL_PRESENT arm, `False` on GOAL_ABSENT; both dropped, so no
`ResourceEncoder` is built and the arm's own probe condition
(`latent.z_resource is not None`, line 313) can never hold. The arms still
differ on `use_identity_classifier` / `z_goal_enabled`, so the experiment is
not wholly dead -- but the z_resource pathway it names is absent. Reachable via
`enable_goal_stream` (`config.py:6273`) and by attribute assignment, which the
same driver uses two lines later.

### 5-6. `harm_surprise_pe_enabled` / `harm_nonredundancy_weight` -- DECORATIVE, not dead

These look identically at risk to Defect 2 and **are not**. `v3_exq_324` and
`v3_exq_323` each realise the arm in their **own training loop**
(`if pe_enabled:` / `if nonredundancy_weight > 0.0:`), so the experiments remain
valid; only the config flag is inert. Recorded here so a later session does not
fold them into Defect 2 on the strength of the shape. `harm_obs_ema_alpha` is
dropped in the same `v3_exq_324` call and is harmless twice over (value equals
the default; the driver computes its own EMA).

### 7. `wanting_weight` -- NOT A DEFECT (negative control)

The single `PARTIAL`. A **name collision** between two independent knobs:
`HippocampalConfig.wanting_weight` (CEM scoring, default 0.0) and
`GhostGoalBankConfig.wanting_weight` (ghost priority, default 1.0).
`from_dims` targets the hippocampal one and lands on it correctly. Registered
so a later session does not "repair" it by plumbing `from_dims` into the ghost
bank, which would silently couple two unrelated knobs.

## Not done, on purpose

No `from_dims` signature entries were mass-added. Adding a parameter for every
dataclass field is a **convention change, not a repair**, and all 26
alternative-idiom flags already have a working path. Each defect above records
its measured blast radius so the decision can be taken per flag by whoever owns
the claim.

## The standing guard

`ree-v3/tests/contracts/test_from_dims_flag_reachability.py` (15 tests, green on
`origin/main` @ `cd1e127`) pins the reachability set and the drop-site set. A
newly-added flag that `from_dims` cannot set now forces a decision, and a new
call site that loses a value fails immediately, naming the files.

Every assertion was **differentially validated** -- each was shown to fail when
the condition it guards is violated (registry entry removed; phantom entry
added; new drop site; stale registry path; alternative-idiom flag mis-filed;
non-recursive walk), and to pass on the real state. Reverting the Defect-1
repair fails both the defect pin **and** the call-site test, with the latter
independently naming all 11 affected drivers -- i.e. the guard would have caught
Defect 1 cold.

Roughly half the tests are negative controls, including a positive control that
a synthetic unknown kwarg still reads as unreachable (without it, a sweep that
stopped overriding anything would report every flag as landing and the whole
file would pass vacuously).

**Known cost:** the call-site scan is a seventh independent parse of
`experiments/` (~1184 of 1466 files), which is exactly what
`tests/contracts/conftest.py`'s shared `corpus_scan` exists to delete. Folding
it in needs a new rglob-scoped entry beside `prereg_share_feasibility_lint`
(the `path_lints` share is driver-major and does not contain
`experiments/_lib/baselines/`, which holds one of the confirmed drop sites).
Deliberately not done in the same change, because that fixture carries
exact-count pins whose purpose is to fail when a file set moves. Tracked as
follow-on.

## Concurrency -- why Defect 1 is unrepaired

`task_claim.py open` arbitration refused this session's claim on
`ree_core/utils/config.py`: `elated-jackson-f12eae-docs` (claimed
2026-08-22T12:30:26Z, ~84 min earlier) owns it for ARC-065 GAP-A head training.

The mechanical hazard was live, not theoretical: the shared checkout held **18
uncommitted lines of theirs** (`use_e2_world_uncertainty_online_training` plus
four `e2_world_uncertainty_*` scalars on `LatentStackConfig`) alongside this
session's 13. Committing `config.py` would have swept their in-flight work
under this change -- the read-modify-write contamination documented in
`CLAUDE.md`. This session's insertion was backed out at Edit level (never
`git checkout --`, which would have destroyed their lines) and verified: their
18 lines intact, mine gone.

**Handover to `elated-jackson-f12eae-docs`, and it is load-bearing:** their new
`use_e2_world_uncertainty_online_training` is a `use_*` flag added as a
dataclass field with **no `from_dims` entry** -- the identical shape as the
MECH-307 incident (84 drivers) and `beta_gate_bistable`. The new contract test
already fires on it in the shared checkout, before their change has ever run,
and will fail their commit until they choose: give it a `from_dims` entry
immediately before `**kwargs` (the documented convention, so no positional
index moves), or register it as reachable-by-alternative-idiom. That is the
guard doing its job on its first live case.

Because the registry was first derived against a working tree containing their
edits, it was re-derived in a throwaway worktree at `origin/main` -- which
caught one phantom entry (`use_e2_world_uncertainty_online_training`, which does
not exist on trunk). The committed registry describes trunk, not the shared
checkout.
