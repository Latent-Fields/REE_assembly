# Non-production config drift -- corpus audit and lint scoping (2026-08-18)

**Chip:** `chip-20260816-nonproduction-config-drift-lint`. Authorised at the 2026-08-16
failure-autopsy batch confirmation gate, after four confirmed instances in one day of a
mechanism tested in a NON-PRODUCTION configuration:

- **927/928** (`failure_autopsy_927-928-mech267-cluster_2026-08-16.md`): `mode_partitioned_cem`
  defaults `False`; the validated fix is inert in production.
- **930** (`failure_autopsy_V3-EXQ-930_2026-08-16.md`): `use_contextual_safety_terrain`
  defaults `False` and was never enabled in the run -- MECH-303's gate never actually ran.
- **934** (`failure_autopsy_V3-EXQ-934_2026-08-16.md`): `salience_affinity_input_cap`
  defaults `None` (no clamp) and `use_external_task_drive` defaults `False`; the run's
  finding is conditional on both being off-default.
- **931/932** (`failure_autopsy_931-932-wanting-authority-cluster_2026-08-16.md`):
  `HippocampalConfig.wanting_weight` ships `0.0`, not the `0.5` the driver itself calls the
  "documented operating value".

Brief: "Add a warn-only `validate_experiments.py` lint for non-production config drift, plus
a corpus audit that scopes it ... AUDIT FIRST, then build only if justified -- calibrate
honestly like the 17/733 letter-drop audit."

This document is that audit, including the two framings that were tried and rejected before
a well-calibrated one was found, plus a numbers-only appendix so the audit is independently
re-runnable.

---

## 1. Why a single per-driver "is this config non-production" lint does not exist

The four cases above do not share one mechanical shape:

- **927/928 and 934** are, at bottom, a claim-status-vs-config.py-default mismatch: the
  driver DOES enable the knob (that is the whole point of the run), but the flag's SHIPPED
  default in `ree_core/utils/config.py` was never flipped to match. That is
  `REE_assembly/scripts/default_off_drift_guard.py`'s existing domain (claim status x
  corpus-wide knob enablement), not a per-driver authoring defect.
- **930** is a driver that never enables the knob its own docstring discusses at all -- but
  the docstring is explicit and CORRECT about that ("PURPOSE (diagnostic --
  substrate-readiness validation ... NOT a MECH-303 mechanism test)"). No static per-driver
  check can distinguish this legitimate, self-scoped substrate-readiness run from a driver
  that wrongly believes it is testing the gated mechanism, without reading and comparing two
  pieces of natural-language prose (the docstring's PURPOSE line against the manifest's
  `interpretation.label`) -- outside AST-lint reach.
- **931/932** is the one case with a genuine, confirmed SOFTWARE DEFECT behind it (see
  section 3) rather than only a governance/documentation gap.

So "detect non-production config drift" was not attempted as one predicate. Two candidate
mechanical framings that WOULD generalise across drivers were tried first; both failed
calibration hard enough to rule out shipping either.

---

## 2. Two rejected framings

### 2a. "Driver sets a default-off knob but never wires `agent=`/`enabled_default_off_flags=`
into the manifest writer" (a "recording gap")

Motivated by V3-EXQ-934's own autopsy point 6: *"Recording gap (minor, but exactly on
point): `enabled_default_off_flags` is null, yet this run's entire finding is conditional on
two default-off knobs ... A run whose finding is configuration-conditional should record the
enabled default-off flags machine-readably."*

Audited (2026-08-18, `ree-v3` at the session's working commit, 1371 files under
`experiments/` excl. `_lib/`, full parse of `config.py` + nested config classes reachable by
following `field(default_factory=XConfig)` imports, mirroring
`default_off_drift_guard.parse_knobs`):

```
total default-off knob names parsed: 345
total .py files under experiments/ (excl _lib): 1371
drivers with __main__: 1361
  -> of those, call a chokepoint manifest writer: 996
     -> of those, set >=1 default-off knob truthy in own source: 779
        -> of those, NO writer call wires agent=/enabled_default_off_flags=: 768
```

**768 of 996 (77%).** `experiments/_lib/manifest_core.py`'s own docstring says the recording
is deliberately opt-in ("Omitted entirely when no config-bearing agent was supplied at all --
never measured"), so almost the entire corpus reads as a "hit" under this framing. That is
not a defect signal at a 77% rate -- it is simply how most of the corpus is written. Building
a lint on this framing would either be ignored on sight or would need every existing driver
retro-fitted, neither of which fits "warn-only, calibrate honestly".

### 2b. "Driver's own `claim_ids` map (via `default_off_drift_guard.py`'s decl-grade
attribution) to a default-off knob the driver never sets"

Motivated by the idea that a driver testing claim X should touch at least one of the knobs
`default_off_drift_guard.py` already attributes to X by a `decl`-grade (heading, not
mid-prose) comment in `config.py`.

Audited the same way, restricting to `decl`-grade attributions only (per
`default_off_drift_guard.py`'s own advice that `mention`-grade is where its false positives
live):

```
claims with >=1 decl-attributed default-off knob: 166
drivers with extractable claim_ids: 1100
  -> of those, >=1 claim maps to a decl-attributed default-off knob: 666
     -> of those, >=1 such knob never set truthy anywhere in driver: 479
```

**479 of 666 (72%).** A claim id spans many narrow sub-experiments over months, and most
legitimately test one slice of the mechanism without touching every knob `config.py`
happens to attribute to that claim id in a field comment. `reafference_action_dim`
(SD-007/MECH-098) alone accounts for a large share of the noise -- a dimension-count knob
unrelated to what most SD-007/MECH-098 drivers actually manipulate. Same verdict as 2a: not
usable as a warn lint at this fire rate.

---

## 3. The signal that did calibrate: multi-arm `enabled_default_off_flags` collapse

`experiments/_lib/manifest_core.py::enabled_default_off_flags_for_agents` pools one or more
agents' default-off knobs with a plain `dict.update()` per agent (its own docstring: *"Later
agents in iteration order win on a disagreement -- a known, stated simplification for a
first cut of this feature, not a guarantee of per-arm attribution."*). On a genuine multi-arm
sweep of a default-off knob, only the LAST-CONSTRUCTED agent's value survives in the
manifest's top-level `enabled_default_off_flags` block.

**V3-EXQ-931 is the confirmed carrier** (`failure_autopsy_931-932-wanting-authority-cluster_2026-08-16.md`,
point 1): the driver declares

```python
ARM_WEIGHTS: Dict[str, float] = {
    "ARM_W0": 0.0, "ARM_W05": 0.5, "ARM_W50": 50.0,
    "ARM_W500": 500.0, "ARM_W5000": 5000.0,
}
```

sets `wanting_weight=ARM_WEIGHTS[arm]` per arm, and calls
`write_flat_manifest(..., agent=list(_ARM_AGENTS.values()))`. The manifest recorded
`hippocampal.wanting_weight: 5000.0` -- the last-constructed arm, the positive control --
even though the run's own `OPERATING_ARM` is `ARM_W05` (`0.5`). The construction site's own
comment names the hazard ("retained so write_flat_manifest can record
enabled_default_off_flags off each arm's own .config (the flags differ by arm ...") and
falls into it anyway.

This is a genuine, narrow, mechanical software defect -- not a semantic judgement about
"is this production" -- so it calibrates the way the rejected framings above could not.

### Detector

Fires when ALL of:

1. a default-off `REEConfig` field (`validate_experiments._default_off_knob_names()`, a
   same-repo static parse of `ree_core/utils/config.py`'s own dataclasses -- deliberately
   NOT a cross-repo import of `default_off_drift_guard.py`, so a cloud worker checkout with
   only `ree-v3` still works) is set from a **Subscript into a module-level dict/list
   literal carrying >=2 DISTINCT constant elements** -- a genuine per-arm sweep, not an
   incidental lookup;
2. the driver calls the sanctioned manifest writer (`write_flat_manifest` / `write_pack` /
   `ExperimentPackWriter`) with `agent=` bound to a **multi-agent expression** (a
   list/tuple/comprehension, or `list(...)`/`.values()`), never a single bare `Name`; and
3. that same call does **not** also pass `enabled_default_off_flags=` explicitly.

### Corpus calibration

2026-08-18, 1371 files under `experiments/` (excl. `_lib/`):

```
drivers with a module-level >=2-distinct-value collection feeding a default-off knob: 1
drivers hitting the full 3-part signal: 1
  ree-v3/experiments/v3_exq_931_cem_wanting_weight_selection_authority.py: ['wanting_weight']
```

**1 fire, exactly the confirmed carrier, nothing else.** Matches the calibration bar set by
the sibling chip's `disjunctive_criteria_load_bearing` lint (1 fire / 1437 drivers) and the
"17/733" reference point in `failure_autopsy_V3-EXQ-920a_2026-08-16.md`.

### What this deliberately does not catch

- **927/928, 934**: neither sweeps a default-off knob from a module-level >=2-distinct-value
  collection the way 931 does. Their drift is a claim-status/`config.py`-default mismatch,
  which is `default_off_drift_guard.py`'s domain, not this lint's.
- **930**: never enables the knob its docstring discusses at all, in a single-arm run whose
  own scoping is correct. No per-driver static check reliably separates that from a
  mis-scoped driver without semantic prose comparison.
- A **single-arm** driver relying on the same `enabled_default_off_flags_for_agents`
  auto-fill is invisible by design: `agent=` bound to one agent cannot collapse anything,
  because there is nothing to collapse.
- A knob set via a helper function, a `**kwargs` splat, or resolved through more than one
  level of indirection is invisible (same under-fire posture as this file's other lints,
  e.g. `dead_z_goal_stream_lint`'s one-level helper resolution).

### Registration

`ree-v3/validate_experiments.py`: `multi_arm_default_off_flags_collapse_lint()`, registered
in `CHECK_NAMES`, the `main()` dispatch loop, the report block, and
`tests/contracts/conftest.py`'s shared `corpus_scan` `path_lints` tuple (mirrored in
`tests/contracts/test_corpus_scan_sharing.py`'s `_PATH_LINTS`). WARN-only in both report and
`--strict` mode -- the one carrier's run is complete and already adjudicated at the
2026-08-16 confirmation gate, so hardening would block commits on history and retro-editing
it would falsify provenance. Opt-out: `MULTI_ARM_DEFAULT_OFF_FLAGS_EXEMPT = "<reason>"`.
Tests: `tests/contracts/test_multi_arm_default_off_flags_collapse_lint.py` (24 tests,
including the corpus-calibration pin and CHECK_NAMES/main-loop/report-block wiring checks).

---

## Appendix: reproducing the numbers

The two rejected framings (section 2) were throwaway scripts, not committed to the repo
(consistent with them not being shipped as a lint). The accepted signal (section 3) IS the
shipped lint; re-run its own numbers with:

```bash
cd /Users/dgolden/REE_Working/ree-v3
/opt/local/bin/python3 validate_experiments.py --checks multi_arm_default_off_flags_collapse
```
