# MECH-307 is implemented but UNREACHABLE through `REEConfig.from_dims()`

**Found:** 2026-08-07T20:10:30Z
**Found by:** session `metaworker-chip-20260807-arc030-mech307-retest`
(chip `chip-20260807-arc030-mech307-retest`, `/queue-experiment` for ARC-030)
**Substrate:** ree-v3 `46569178541c0cb6bfd5d24257cd4b6e220ad083`
**Status:** `blocked_substrate` -- ARC-030 retest NOT queued; routed to `/implement-substrate`

---

## Summary

The 2026-08-07 `/governance` ceiling audit (`check_substrate_ceiling_audit.py`) flagged
ARC-030 as "ceiling-may-have-lifted" on the grounds that **MECH-307 is now implemented**.
That premise is true at the `claims.yaml` and `ree_core/` source level and **false at
runtime for every experiment driver**, because the MECH-307 master flag is silently
dropped by the factory constructor those drivers use.

This is the `[memory] reference-reeconfig-from-dims-silent-kwargs` failure mode: a
`REEConfig` knob needs **three** sites, and MECH-307 has only one.

| Site | Required | MECH-307 |
|---|---|---|
| 1. dataclass field on `REEConfig` | yes | **present** -- `ree_core/utils/config.py:5324` |
| 2. named parameter in `from_dims()` signature | yes | **MISSING** -- absorbed by `**kwargs`, dropped, no error |
| 3. post-`cls()` re-apply of the resolver inside `from_dims()` | yes | **MISSING** |

Site 3 is independently required even if site 2 were added: `from_dims` assigns fields
*after* `cls()`, so `__post_init__` (which holds the resolver, `config.py:5427-5436`) has
already run and the three sub-flags are never forced True.

Both neighbouring master flags get this right, so the pattern is established and MECH-307
is the odd one out:

- **MECH-090** -- `from_dims` re-applies its resolver explicitly at `from_dims:1798-1804`,
  with the comment *"from_dims sets fields AFTER cls(), so `__post_init__` ran before this
  assignment -- re-apply the OR-only resolver here so factory-built configs behave
  identically to direct-construction configs."*
- **GAP-3 sleep-aggregation cluster** -- its resolver sits directly below MECH-307's in
  `__post_init__` (`config.py:5438-5445`) and its own comment states *"from_dims() handles
  the factory path separately (it sets fields after cls(), so it re-invokes the bundle via
  `enable_sleep_aggregation_cluster()`)."*

## Reproduction (verified 2026-08-07, ree-v3 `4656917854`)

```python
from ree_core.utils.config import REEConfig

# A. direct construction -- resolver runs, all four gaps ON
c = REEConfig(use_mech307_conjunction=True)
#   use_mech307_conjunction              = True
#   use_mech307_split_surprise           = True
#   use_mech307_schema_multichannel      = True
#   use_mech307_predicted_location_write = True

# B. from_dims -- the idiom EVERY driver uses. All four stay OFF, no error.
c2 = REEConfig.from_dims(body_obs_dim=8, world_obs_dim=32, action_dim=5,
                         self_dim=32, world_dim=32,
                         use_mech307_conjunction=True)
#   use_mech307_conjunction              = False
#   use_mech307_split_surprise           = False
#   use_mech307_schema_multichannel      = False
#   use_mech307_predicted_location_write = False

# C. **kwargs silently swallows anything -- `totally_bogus_flag_xyz=True` also
#    raises nothing, so there is no signal at the call site.

# D. post-hoc assignment does NOT repair it -- the resolver lives in
#    __post_init__ and does not re-run:
c4 = REEConfig.from_dims(...); c4.use_mech307_conjunction = True
#   use_mech307_split_surprise = False   (still)
```

**All twelve** MECH-307 parameters are missing from the `from_dims` signature:
`use_mech307_conjunction`, `use_mech307_split_surprise`, `use_mech307_schema_multichannel`,
`use_mech307_predicted_location_write`, `use_mech307_signed_pe`,
`use_mech307_consumer_conjunction_read`, `mech307_anticipatory_liking_gain`,
`mech307_z_beta_schema_gain`, `mech307_conjunction_gain`,
`mech307_conjunction_wanting_threshold`, `mech307_conjunction_liking_threshold`,
`mech307_conjunction_z_beta_threshold`.

## Blast radius

AST scan of `ree-v3/experiments/**/*.py`:

- **84 drivers** pass a MECH-307 flag **into `from_dims`** -> silently dropped, ran with all
  four gaps OFF.
- **0 drivers** use direct `REEConfig(...)` construction (the route that works).
- **18 drivers** set MECH-307 attributes post-hoc via `setattr`. Post-hoc setattr of a
  **sub-flag** DOES work (the sub-flags are what runtime reads); post-hoc setattr of the
  **master** flag does nothing.

The scaffolded lineage that ARC-030's retest is built on is in the affected set --
V3-EXQ-603q, V3-EXQ-866a and V3-EXQ-866b all construct via `from_dims` with
`use_mech307_conjunction=True`, so **all three ran with MECH-307 entirely OFF**.

Separately, `experiments/scaffolded_sd054_onboarding.py:1890/1895` toggles
`agent.config.use_mech307_conjunction` False/True at the P1 goal-pipeline freeze/unfreeze.
Per (D) above that assignment is inert: nothing in `ree_core` reads the master flag at
runtime (only `__post_init__` does), so the freeze/unfreeze does not change MECH-307 state
either way.

## Why no contract test caught it

`tests/contracts/test_mech307_conjunction_contract.py` and
`test_mech307_consumer_conjunction.py` build their config with
`REEConfig.from_dims(...)` **without** the MECH-307 flags and then `setattr` each
**sub-flag** individually. Sub-flag setattr works, so the four gaps are genuinely
mechanism-verified and those contracts are sound. What is untested is the
**master-flag-through-the-factory** route -- i.e. exactly how all 84 drivers ask for it.

The mechanism is fine. The way every consumer requests it is what is broken.

## Consequence for ARC-030

ARC-030's `what_would_answer` names the fix path for its retest gate as *"GAP-1 (MECH-307
split-channel substrate, landed 2026-05-11, readiness V3-EXQ-540g PASS 2026-05-15) and
GAP-7/SD-057 object-bound incentive-salience layer ... together replaced the dead seeding
path"*. V3-EXQ-540g is unaffected (it sets the sub-flags directly and is a valid readiness
result), but every **behavioural** run in the scaffolded lineage since then had MECH-307
off. So either the seeding fix is attributable to GAP-7/SD-057 alone, or ARC-030's retest
premise is not yet satisfied. Both readings block the retest as designed.

Queuing the retest anyway by setting the sub-flags explicitly was considered and
**rejected**: 603q/866b's commit-verified competence (`base_mean_survival` 33.9 vs a 37.7
reference, z_goal ~0.40-0.47 sustained through P2) was measured with MECH-307 OFF.
Turning it on changes the substrate underneath the COMBINED arm whose competence *is*
ARC-030's mandatory G0 non-degeneracy precondition. V3-EXQ-866a already failed G0 on a
smaller deviation from 603q, so this would very likely burn a long cloud run and return
`non_contributory` again -- the re-derive loop the brake exists to prevent.

## Recommended repair (`/implement-substrate`)

1. Add the twelve MECH-307 parameters to the `REEConfig.from_dims()` signature.
2. Assign them onto `config` in the `from_dims` body, then **re-apply the OR-only resolver**
   after `cls()` -- copy the MECH-090 shape at `from_dims:1798-1804`:
   ```python
   if use_mech307_conjunction:
       config.use_mech307_split_surprise = True
       config.use_mech307_schema_multichannel = True
       config.use_mech307_predicted_location_write = True
   ```
3. Add a contract test asserting `from_dims(use_mech307_conjunction=True)` lights all three
   sub-flags, with a direct-construction parity case, so site 2 and site 3 cannot regress
   independently. This is the assertion that was missing.
4. Consider a broader guard: `from_dims`'s `**kwargs` silently swallowing an unknown flag is
   the general mechanism here, not a MECH-307 quirk. A check that rejects (or at minimum
   warns on) unconsumed `**kwargs` would close this whole class. Scope that separately --
   it will surface other latent drops and needs its own triage.

**After the repair**, the ARC-030 retest needs a readiness step before it is worth
queuing: re-run the 603q/866b configuration with MECH-307 genuinely ON and confirm the
scaffolded lineage still clears the G0 non-degeneracy gate. Only then is the
COMBINED-vs-NOGO_ONLY discriminative pair (design fully pre-specified in ARC-030's
`what_would_answer`) a meaningful run.

## Related

- `[memory] reference-reeconfig-from-dims-silent-kwargs` -- the general failure mode.
- `failure_autopsy_V3-EXQ-866a_2026-08-03` -- concluded 866a's config was "line-by-line
  identical" to 603q. That comparison was of the *source text* of the two `_make_config`
  calls; it could not have caught this, because both texts request MECH-307 and neither
  gets it.
- `v3_exq_866b_603q_substrate_regression_check_20260803T192405Z_v3` -- established the
  substrate reproduces 603q. That finding stands; it was simply measured with MECH-307 off
  at both ends, which is a like-for-like comparison.
