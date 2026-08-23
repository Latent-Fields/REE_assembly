---
title: "Version-Layering Doctrine: V3 Primacy"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 17
---

# Version-Layering Doctrine: V3 Primacy

**Status:** architecture doctrine, 2026-06-17
**Triggering incident:** V3-EXQ-654e (2026-06-17) -- the DR-12 / first-V4 substrate
(`self_model_v4:SELF-4`) added an **unconditional** call-site for
`e2_forward_pe_per_candidate` into the shared V3 agent path
(`ree_core/agent.py::select_action`) while the matching `E3TrajectorySelector.select()`
parameter lived in a separate commit. A transient cross-checkout skew raised a
`TypeError` that crash-burned a V3 critical-path experiment (and, via the
crash-before-manifest hole, did so silently). A V4 change broke V3 by default.

---

## The invariant

> **No higher-version (V4/V5+) code may change V3 default execution behaviour.**

V3 closure is the primary objective. V4/V5 work is legitimate and encouraged, but
it is **preparatory**: it may add capability behind flags, register
version-scoped candidate claims, and stage substrate -- it may never make the
default V3 forward/select/train path behave differently, slower, or more
fragile than it would without the V4/V5 change present.

This is the safety counterpart to the existing scoping rules, not a new
restriction on V4 ambition:

- **Phase label follows dependency** (`feedback_phase_label_follows_dependency`):
  `implementation_phase` is a *prediction*, not a permission gate. The doctrine
  here is about *default-behaviour safety*, never about forbidding V4 work or
  reclassifying its scope.
- **Keep V4 ideas off the V3 critical path** (`feedback_ree_assembly_externalised_cognition`):
  capture them, register them, stage them -- without letting them gate or
  destabilise v3.

## Rules

1. **No-op / bit-identical by default.** Any V4/V5 change to shared code under
   `ree-v3/ree_core/` MUST be flag-gated and produce a bit-identical result when
   the flag is off. This extends the project's existing "no-op-default /
   bit-identical-when-omitted" convention (already used for `--remote-control`,
   the ARC-063 `mature_pool_dynamics` levers, etc.) to all cross-version edits.
2. **Conditional call-sites, never unconditional.** A V4/V5 call-site into a
   shared path must pass its new arguments only when the feature is enabled (or
   only when the injected value is present). An unconditional kwarg pass couples
   the shared path to a parameter that a skewed or older checkout may not have --
   this is the exact 654e failure. (Defensive alternative: a kwargs-tolerant
   callee, but the conditional call-site is preferred because it is explicit.)
3. **Separate ID namespaces.** V4/V5 experiments use `V4-EXQ-*` / `V5-EXQ-*`
   queue IDs (already in use: `V4-EXQ-001` is the DR-12 pilot). Results and
   claims stay distinguishable from the v3 evidence base.
4. **Generation-tagged, denominator-excluded.** V4/V5 plan nodes and claims carry
   `generation: v4|v5`; the closure snapshot excludes non-v3 generations from the
   v3 progress denominator (already implemented in `generate_closure_snapshot.py`
   / `serve.py` `CLOSURE_STATUS_WEIGHTS`). The v3 closure percentage must never
   move because V4/V5 work was added.
5. **Preparatory means registered, not built-into-v3.** V4/V5 intake (including
   the convergence demand pipeline, see
   `evidence/planning/convergence_demand_pipeline_plan.md`) terminates in
   registered candidate claims wired into `depends_on` -- it does NOT place a
   build dependency on a v3 critical-path node.

## Enforcement (mechanical guards)

The doctrine is backed by code-level guards. **All three landed 2026-06-17** (the
day of the 654e incident). The single anchor for every higher-version flag is the
registry `ree-v3/ree_core/version_layering.py` (`GENERATION_FLAGS`): when a V4/V5
master flag is added, it is appended there in the same pass, which keeps the
no-op-default guard exhaustive. The first entry is DR-12
(`e3.use_pe_confidence_weighting`).

- **Guard A -- conditional DR-12 call-site (`ree-v3/ree_core/agent.py`,
  `select_action`).** The `e2_forward_pe_per_candidate` kwarg is built into the
  `self.e3.select(...)` call **only** when `config.e3.use_pe_confidence_weighting`
  is on OR an injected per-candidate PE is present
  (`getattr(self, "_injected_e2_forward_pe", None) is not None`). The default V3
  path therefore never passes the kwarg, so a skewed/older
  `E3TrajectorySelector.select()` that lacks the parameter cannot raise a
  `TypeError` on the V3 critical path -- the exact 654e fix.
- **Guard B -- runner V3-parity smoke (highest leverage;
  `ree-v3/experiment_runner.py` + `ree-v3/tests/v3_parity_smoke.py`).** The shared
  `run_v3_parity_smoke()` builds a default tiny agent (every registered V4/V5 flag
  asserted off via `version_layering.assert_all_off`) and runs the default-path
  `agent.select_action` loop. It is wired two ways:
  (1) the **startup regression preflight** runs `tests/preflight/test_v3_parity_smoke.py`
  (the runner exits non-zero before claiming if it fails); (2) an **in-process,
  HEAD-gated gate** (`_run_v3_parity_gate`) re-runs the smoke after each per-pass
  `git pull` and, on any raise, sets a refuse-to-claim flag so the worker
  **logs + skips claiming that pass** instead of crash-burning. The skew
  self-heals on the next consistent pull (the runner does not exit). This is the
  guard that catches a skew landing *mid-session* in a long-lived `--loop` runner.
  Honoured via `--skip-preflight` / `REE_SKIP_PREFLIGHT=1`.
- **Guard C -- no-op-default contract test
  (`ree-v3/tests/contracts/test_version_layering_noop_default.py`).** Constructs
  the default agent/config and asserts: C1 every `GENERATION_FLAGS` entry defaults
  off; C2 every registered path resolves on a real config (renamed-flag drift
  guard); C3 the default build is **bit-identical** to an explicit-all-V4/V5-OFF
  build over the default `select_action` path; C4 that path runs without error.

## Why a doctrine and not just a test

The 654e incident was not a bad test; it was a *category* of change (a
higher-version edit silently entering the default path) that no single test
anticipated. The invariant gives reviewers and future sessions a one-line check
to apply to any cross-version edit -- "does this change V3 default behaviour?" --
and the guards make the common violation (an unconditional call-site into a
shared path) mechanically hard to land or hard to crash on.
