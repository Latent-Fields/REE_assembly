# MECH-319: Simulation-Mode Rule-Write Gate (Categorical Replay Tag)

**Claim ID:** MECH-319
**Subject:** policy.arbitration.simulation_mode_write_gating_substrate_ree_novel_function
**Status:** IMPLEMENTED 2026-05-10 (substrate landed; behavioural validation deferred to V3-EXQ-543c-successor)
**Registered:** 2026-05-10 (cluster registration session)
**Depends on:** MECH-094 (architectural principle), MECH-312 (arbitration layer)
**Blocks:** V3-EXQ-543c-successor (artificial-write-channel-routing falsifier)

## Problem

MECH-094 names the architectural principle that simulation / replay /
DMN-generated content must NOT update the agent's persistent rule
state, by being routed through a categorical write gate keyed to a
hypothesis tag. The principle is silent on *which substrate* carries
the categorical signal and *at which layer* the gate operates.

In the V3 substrate prior to this commit, three arbitration-layer
write sites each handled simulation gating in isolation:
- `GatedPolicy.forward(simulation_mode=True)` (ARC-062 Phase 1) returns
  zeros and increments a skip counter.
- `LateralPFCAnalog.update(...)` (SD-033a) is mode-conditioned via
  `MECH-261 write_gate("sd_033a")` (continuous mode gate, not a
  categorical simulation-mode tag).
- `HippocampalModule` ghost-goal probes (MECH-293) carry
  `hypothesis_tag=True` per `record_committed_trajectory`.

Three problems:

1. **No unified seam.** Each call site has its own simulation-mode
   handling, with no central authority that translates a caller-
   supplied tag and a debug / falsifier flag into the final
   admit/block decision.
2. **No diagnostic surface.** Experiments cannot observe how often
   the gate fires, at which sites, and under which mode (waking vs
   replay).
3. **No falsifier pathway.** Phase 2 of arc_062 requires a config
   flag that artificially routes simulation-mode passes through the
   write channel anyway, predicting monomodal-collapse re-emergence
   via the MECH-094 / MECH-319 generalisation. Without a single
   coordinator, the V3-EXQ-543c falsifier would have to flip multiple
   per-module flags inconsistently.

MECH-319 is the substrate-level instantiation of MECH-094 at the rule-
arbitration layer that solves all three.

## Substrate-availability premise

Well-anchored biologically (Pull 3 SYNTHESIS R1 GENUINE-NOVELTY-CONFIRMED
conf 0.72; literature in
`evidence/literature/targeted_review_mech_312_arbitration_divergences/`):

- **Joo & Frank 2018 (Nat Rev Neurosci):** SWR review. The discriminable
  sharp-wave-ripple machinery is the biological substrate that
  carries the categorical "this is replay, not waking" signal. Treats
  downstream effects as continuous strength modulation; the write-gate
  function is REE-specific.
- **Foster & Wilson 2006 (Nature):** reverse replay. Concrete structural
  marker (temporal-reverse compressed sequences during awake quiescence)
  demonstrating the substrate-level identifiability that MECH-319's
  categorical tag relies on. Documents the discriminable signal but
  does not show downstream regions exploiting it as a write-gate.

## REE-novel function

The architectural commitment that downstream rule-write machinery uses
the discriminable replay signature to **suppress arbitration-weight
updates** that would otherwise fire if the same rule were applied
during waking action. Plausible at the cellular / synaptic level but
biologically unverified (Pull 3 R1 verdict). The V3 falsification path
is the artificial-write-channel-routing config flag (`admit_writes=True`)
threaded through this module's `effective_simulation_mode` primitive.

## Solution

### Module

`ree-v3/ree_core/regulators/simulation_mode_rule_gate.py` -- pure-
arithmetic regulator (no `nn.Module` inheritance, no learned parameters)
sibling to `GABAergicDecayRegulator` (SD-036) and
`BroadcastOverrideRegulator` (SD-037).

### Single primitive

```python
gate.effective_simulation_mode(simulation_mode: bool, site: str) -> bool
```

Translates the caller-supplied simulation tag and the configured
falsifier flag into the final admit/block decision the downstream
arbitration-write site should observe.

Truth table `(master_on, admit_writes, caller_sim) -> output`:

| master | admit_writes | caller_sim | output | semantic |
|--------|--------------|------------|--------|----------|
| OFF    | (any)        | (any)      | identity (caller_sim) | bit-identical pre-MECH-319 |
| ON     | False        | False (waking) | False  | admit waking write |
| ON     | False        | True (replay)  | True   | block simulation write -- MECH-319 normal |
| ON     | True         | False (waking) | False  | admit waking; flag has no effect |
| ON     | True         | True (replay)  | **False** | **admit simulation write -- V3-EXQ-543c falsifier** |

The gate is idempotent for waking calls (always returns False), so
wiring it into existing waking call sites is bit-identical regardless
of `admit_writes`. The falsifier-control asymmetry surfaces only when
`caller_sim=True` (replay paths, ghost-goal probes, DMN passes).

### Diagnostic counters

Per-call + per-site:
- `n_calls_total`, `n_waking_admitted`, `n_simulation_blocked`,
  `n_simulation_admitted` (the falsifier path).
- `per_site_calls`, `per_site_waking_admitted`,
  `per_site_simulation_blocked`, `per_site_simulation_admitted` --
  keyed on canonical site labels `SITE_GATED_POLICY`,
  `SITE_LATERAL_PFC`, `SITE_DEFAULT`. New consumer call sites can pass
  arbitrary strings.

### Config

- `REEConfig.use_simulation_mode_rule_gate: bool = False` -- master,
  bit-identical OFF.
- `REEConfig.simulation_mode_rule_gate_admit_writes: bool = False` --
  V3-EXQ-543c falsifier flag.

Construction raises `ValueError` when `admit_writes=True` without the
master flag also on (loud-not-silent guard against mis-configuration
-- `admit_writes` is meaningless without the substrate to gate).

### Agent wiring

Two existing arbitration-write call sites in `REEAgent.select_action`
consult the gate when it is instantiated:

1. **GatedPolicy block** (line ~2752): the literal `simulation_mode=False`
   passed to `gated_policy.forward(...)` is replaced by
   `gate.effective_simulation_mode(False, site=SITE_GATED_POLICY)`.
   Bit-identical for the waking path; the seam is exposed for V3-EXQ-543c
   replay-driven invocations.

2. **LateralPFCAnalog block** (line ~2640): consult the gate before
   `lateral_pfc.update(...)`.
   ```python
   eff_sim = gate.effective_simulation_mode(False, site=SITE_LATERAL_PFC)
   if eff_sim:
       skip lateral_pfc.update(...)
   else:
       proceed with the existing MECH-261 mode-conditioned EMA
   ```
   The `compute_bias` call still runs (arbitration RECEIVES the bias
   even during simulation -- it just does not write back into
   `rule_state` on simulation ticks). Bit-identical for waking;
   falsifier-routed simulation writes to `lateral_pfc` would be
   skipped under default MECH-319 ON, admitted under
   `admit_writes=True`.

`REEAgent.reset()` calls `gate.reset()` per episode to clear
diagnostic counters. The gate has no persistent state across ticks.

### MECH-094 invariance

This substrate does NOT modify MECH-094, `GatedPolicy.forward`'s
`simulation_mode` argument semantics, or `LateralPFCAnalog.update`.
The gate is a pre-call coordinator that wraps the `simulation_mode`
argument that callers ALREADY pass. With MECH-319 disabled, every
arbitration-write call site behaves bit-identically to its
pre-MECH-319 form.

### Backward compatibility

- `use_simulation_mode_rule_gate=False` (default) -> `agent.simulation_mode_rule_gate`
  is `None`; both call sites take the legacy literal path.
- 288/288 contract + preflight tests PASS with master OFF
  (regression-clean; the suite was 273 pre-MECH-319, plus 15 new
  MECH-319 contracts).
- With master ON and waking-only callers (the only regime
  `select_action` currently exercises), the gate returns False at
  every site. Bit-identical to baseline.

## Architecture Context

### Relation to MECH-094

**KEEP-AS-IS verdict (Pull 3 R1 + Pull 4 R3): MECH-094 is not edited.**

MECH-094 names the **architectural principle**: a categorical phi(z)
write gate keyed to a hypothesis tag, with the simulation-mode-
suppressed write channel. MECH-319 names the **specific substrate
instantiation**: the unified categorical write gate that operates at
the rule-arbitration layer (MECH-312 sub-mechanisms), with SWR
machinery as the substrate-level analog of the simulation tag.

The two coexist:
- MECH-094 is the principle that downstream architectural work may
  instantiate at multiple layers (rule arbitration, rule-state
  abstraction, future arbitrators).
- MECH-319 is the first such substrate-level instantiation, scoped
  to the rule-arbitration layer.

Future architectural work may name additional MECH-319-siblings for
other function-sites where MECH-094's write-gate principle should
apply (e.g. MECH-094 at the rule-state abstraction layer of MECH-318).
These are deferred until the substrate sites are themselves wired.

### Relation to MECH-261

MECH-261 (mode-conditioned write-gate registry on SD-032a
SalienceCoordinator) is a complementary, continuous gate. MECH-261
returns a per-mode weight in `[0, 1]` that scales the magnitude of
the EMA update on `LateralPFCAnalog.rule_state`. MECH-319 is a
*categorical* (binary admit/block) pre-gate keyed to the simulation
tag of the **caller**, not the operating mode of the agent.

The two gates compose:
- Caller is waking (`caller_sim=False`) -> MECH-319 admits ->
  MECH-261 modulates the EMA strength based on operating mode.
- Caller is simulation (`caller_sim=True`), MECH-319 normal -> MECH-319
  blocks the entire `update()` call, MECH-261 is never consulted.
- Caller is simulation, MECH-319 falsifier (`admit_writes=True`) ->
  MECH-319 admits -> MECH-261 modulates as if the caller were waking.

### Phase 1 vs Phase 2

This is a **Phase 1 substrate landing**. The behavioural test that
flips `admit_writes=True` and routes a replay-driven invocation
through the rule-arbitration layer is V3-EXQ-543c-successor, deferred
until the MECH-313 / MECH-314 / MECH-318 sibling substrates have
landed (see `arc_062_rule_apprehension_plan.md` GAP-K and the
2026-05-10 cluster-registration decision-log entry).

## What This SD Enables

- **V3-EXQ-543c-successor falsifier:** a paired-arm experiment
  comparing `admit_writes=False` (MECH-319 normal) vs `admit_writes=True`
  (artificial-write-channel-routing) under a replay-driven invocation
  path. Predicted: monomodal-collapse re-emergence under
  `admit_writes=True`. This experiment validates BOTH MECH-094 and
  MECH-319 simultaneously.
- **Future MECH-319-siblings** at other arbitration sites can plug
  into the same gate by passing a new site label.
- **Diagnostic observability:** experiment manifests can include
  `gate.get_state()` to report how often the gate fired and at which
  sites.

## Validation experiment

`V3-EXQ-546` substrate-readiness diagnostic queued. Six sub-tests
(UC1-UC5 + UC3b precondition):

- **UC1** forward-pass instantiation + canonical diagnostic keys.
- **UC2** master-OFF backward-compat (`agent.simulation_mode_rule_gate is None`).
- **UC3** truth-table coverage across the 6 valid `(master, admit_writes,
  caller_sim)` combinations.
- **UC3b** precondition raises `ValueError` on `admit_writes=True`
  without master ON (loud-not-silent).
- **UC4** select_action wiring contract: gate sees waking calls from
  both `gated_policy` and `lateral_pfc` sites after one
  `act_with_split_obs` tick; `n_simulation_*` counters remain zero.
- **UC5** MECH-094 invariance: master-OFF and master-ON-with-waking-
  caller produce bit-identical wiring outputs; asymmetry surfaces
  only at `caller_sim=True`.

Smoke 6/6 PASS 2026-05-10. 15 contract tests in
`tests/contracts/test_mech_319_simulation_mode_rule_gate.py` PASS.
288/288 full preflight + contracts PASS.

Behavioural validation -- the V3-EXQ-543c-successor falsifier with
the `admit_writes=True` arm and a replay-driven invocation path -- is
queued separately AFTER MECH-313 / MECH-314 / MECH-318 sibling
substrates have landed.

## Related Claims

- **MECH-094** (architectural principle this substrate instantiates;
  KEEP-AS-IS per Pull 3 R1 + Pull 4 R3 verdicts).
- **MECH-312** (the arbitration layer whose write-gate this implements;
  parent of the MECH-312a/b/c/d sub-mechanisms that the gate suppresses
  during simulation passes).
- **MECH-261** (mode-conditioned continuous write gate; complementary
  to MECH-319's categorical pre-gate).
- **ARC-062** (rule apprehension; arc_062 GAP-K hosted this substrate
  landing).
- **MECH-313 / MECH-314 / MECH-318** (sibling ARC-065 / ARC-064
  substrates landed in separate spawned tasks the same day).
- **MECH-293** (ghost-goal probes; future call site that will pass
  `simulation_mode=True` through the gate).
- **SD-033a** (LateralPFCAnalog; one of the two wired arbitration-write
  call sites).
- **MECH-309** (logical-necessity claim that motivates the broader
  ARC-062 cluster).

## Lit-pull anchors

- `evidence/literature/targeted_review_mech_312_arbitration_divergences/synthesis.md`
  R1 GENUINE-NOVELTY-CONFIRMED verdict (conf 0.72) + R5 KEEP-AS-IS
  recommendation for MECH-094 paired with MECH-319 registration as
  REE-novel candidate substrate claim.
- Pull 4 R3 KEEP-AS-IS reaffirmation.

## Files touched in landing pass (2026-05-10)

- `ree-v3/ree_core/regulators/simulation_mode_rule_gate.py` (NEW)
- `ree-v3/ree_core/regulators/__init__.py` (export)
- `ree-v3/ree_core/utils/config.py` (`REEConfig` fields + `from_dims` kwargs)
- `ree-v3/ree_core/agent.py` (import + `__init__` instantiation +
  `select_action` GatedPolicy + LateralPFC site wiring + `reset` hook)
- `ree-v3/tests/contracts/test_mech_319_simulation_mode_rule_gate.py`
  (NEW, 15 tests)
- `ree-v3/experiments/v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness.py` (NEW)
- `ree-v3/experiment_queue.json` (V3-EXQ-546 appended)
- `ree-v3/CLAUDE.md` (MECH-319 SD entry appended)
- `REE_assembly/docs/architecture/mech_319_simulation_mode_rule_gate.md` (THIS FILE, NEW)
- `REE_assembly/docs/claims/claims.yaml` (MECH-319 status + evidence_quality_note update)
- `REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md`
  (GAP-K row + decision-log entry)
