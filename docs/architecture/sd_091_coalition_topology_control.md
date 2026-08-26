---
title: "SD-091: Coalition/Topology Control Substrate"
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 17
status: candidate/v3_pending
status_asof: 2026-08-03
status_claim: SD-091
---

# SD-091: Coalition/Topology Control Substrate

**Claim IDs:** SD-091 (architectural commitment) + MECH-481 (mechanism hypothesis, instantiates SD-091)
**Subject:** `control_plane.coalition_topology_control` / `control_plane.typed_coalition_instantiation`
**Status:** candidate, v3_pending, epistemic_category substrate_conditional. **Steps 1-3 landed 2026-08-02**
(ree-v3, chip `chip-20260802-sd091-implement-mvp`): `ree_core/claustrum/` -- `control_demand.py`,
`coalition_templates.py`, `coalition_controller.py`; 13 contract tests pass. **Steps 4-6 landed 2026-08-03**
(ree-v3, chip `chip-20260802-sd091-live-wiring`): the module is now wired into `REEAgent.__init__`/`reset()`/
`select_action`, and all 8 named consumer-site targets (E1/E2 sensory path, hippocampal anchor-set/
persistence-appraisal, BetaGate/MECH-090 commit-entry + motor-commitment, hippocampal write-consolidation)
read `coalition.write_gate()`/`channel_gain()` -- 9 new contract tests
(`tests/contracts/test_sd091_coalition_controller_wiring.py`) confirm bit-identical-off, per-template target
isolation, the doc's own step-6 live-tick smoke test, and the BetaGate never-force-open guardrail through the
real `_readiness_margin` composition. `use_coalition_controller` defaults `False` (bit-identical off).
**Step 7 (`/queue-experiment` the MECH-481 4-arm falsifier) is the one remaining step** -- ablatable now that
steps 4-6 land, but not yet queued. See `ree-v3/CLAUDE.md` "SD-091 / MECH-481" entry for the full writeup.
**Registered:** 2026-08-02
**Depends on:** ARC-005, MECH-004, MECH-019, MECH-039, MECH-063, SD-076 (SD-091); SD-091, MECH-019, MECH-063
(MECH-481)
**Source:** `docs/thoughts/2026-08-01_metacognitive_control_selective_cognitive_coalition_instantiation.md`

---

## Problem

REE's control plane (ARC-005) currently produces one kind of output: parametric modulation -- precision, gain,
learning rate, commitment threshold, rollout horizon, candidate count, replay, interruptibility, veto threshold.
All of this alters how already-engaged systems operate. It does not specify which systems are engaged in the
first place.

The source thought argues this is an incomplete account of metacognitive control. A confidence, error, or
provenance-conflict estimate only becomes metacognitively *effective* if it can change the composition of
subsequent cognition, not just its gain. A doubtful perception plausibly needs renewed sensory sampling; a
doubtful memory plausibly needs provenance reconstruction; an ethical conflict plausibly needs longer-horizon
comparison and social/invariant review. These are different *subsystem recruitment patterns*, not different
settings of the same scalar knobs.

SD-091 asserts the control plane needs a second, graph-valued output \(G_t\) alongside the existing mode
\(M_t\) and parameter \(\theta_t\) outputs. MECH-481 asserts the specific mechanism: typed control demands
(a taxonomy of ~10 classes) map to typed coalition templates. Both claims are `epistemic_category:
substrate_conditional` and currently unfalsifiable -- nothing exists to ablate. This doc is the scoping pass
that has to happen before `/implement-substrate` can build anything, per the claims' own notes ("No EXP
proposal minted yet -- nothing exists to ablate until an `/implement-substrate` pass lands a minimal
coalition-control module").

---

## Architectural distinction (from the source thought)

\[
C_t = (M_t,\ \theta_t,\ G_t,\ \tau_t,\ \Gamma_t)
\]

- \(M_t\): current cognitive mode -- **already built** (SD-032a `SalienceCoordinator.operating_mode`, 4-way
  soft vector over `{external_task, internal_planning, internal_replay, offline_consolidation}`).
- \(\theta_t\): gain/precision/gate settings -- **already built** (ARC-005/MECH-004 signal-to-knob map).
- \(G_t\): the active functional interaction graph -- **does not exist**. This is what SD-091 adds.
- \(\tau_t\): temporal coordination requirements -- deferred; see Scope boundary below.
- \(\Gamma_t\): coalition persistence/completion/dissolution conditions -- minimal version only; see below.

This doc does not re-derive that framing (read the source thought for the claustrum grounding and the full
falsification programme). It answers the four scoping questions the task requires: what is the smallest
buildable \(G_t\) primitive, which typed-demand classes to wire first, how it composes with the existing
\(M_t\)/\(\theta_t\) machinery, and which guardrails are hard constraints on the build.

---

## 1. Minimum-viable coalition-control primitive

MECH-481's falsifier (see claims.yaml `what_would_answer`) needs Arms 2, 3, and 4 to be genuinely different
mechanisms, not three configurations of one knob. The smallest structure that satisfies this:

**\(G_t\) as a sparse, per-tick, per-subsystem recruitment/suppression vector (a star topology, not a full
edge-labelled graph).** Concretely:

```
CoalitionState:
  participating: dict[str, float]     # subsystem name -> recruitment weight in [0, 1]
  suppressed: dict[str, float]        # subsystem name -> suppression weight in [0, 1]
  channel_gain: dict[str, float]      # subsystem name -> temporary gain multiplier, scoped to this coalition
  demand_type: ControlDemandType
  opened_tick: int
  max_duration_ticks: int             # hard timeout -- Gamma_t floor
  completion_condition: Callable[[AgentState], bool]
```

This is deliberately **not** the full \(G_t\) the source thought sketches (no explicit pathway-open/attenuate
edges, no \(\tau_t\) temporal-coordination spec). A star topology -- the controller as hub, recruited
subsystems as spokes, no subsystem-to-subsystem edges -- is the smallest structure that is still graph-*valued*
(participation is a different kind of thing than a scalar, satisfying SD-091's actual claim) while remaining
buildable in one pass and cheap to reason about. Promote to edge-level topology only if Arm 4 passes and a
follow-on claim needs to distinguish "which subsystems are recruited" from "how they specifically
interconnect" -- do not build that speculatively now.

**Composition with existing machinery.** `participating`/`suppressed` are read by consumer sites as a
*multiplier* on whatever the existing MECH-261 mode-gate already computes there:

```
effective_recruitment(target) = mode_gate(target) * coalition_gate(target)
```

where `mode_gate` is the existing `SalienceCoordinator.write_gate(target)` (SD-032a/MECH-261, already built)
and `coalition_gate(target) = participating.get(target, 1.0) * (1 - suppressed.get(target, 0.0))`. Absence
from either dict is a no-op multiplier of 1.0, so `use_coalition_controller=False` is bit-identical to today.
This multiplicative composition is the same pattern already used throughout the cingulate cluster (AIC
`harm_s_gain`, pACC `effective_drive`) -- reuse it rather than inventing a second gating idiom.

**Persistence (\(\Gamma_t\)), minimal version.** A coalition dissolves when EITHER `completion_condition(state)`
returns true OR `tick - opened_tick >= max_duration_ticks`, whichever comes first. No escalation logic, no
graded engagement/disengagement curve. This is deliberately conservative: MECH-481's own falsifier text scopes
persistence dynamics as "a follow-on refinement, not part of this claim's primary falsifier -- register
separately if Arm 4 passes" (scenario 5). The guardrail "treat persistence and dissolution as load-bearing" is
still honoured because both conditions are real, measured, and configurable -- not a permanent no-op -- but the
MVP does not need graded persistence to run the primary falsifier.

**Injection, not derivation.** The controller does **not** implement steps 1-2 of MECH-481's sequence (Monitor,
Classify). It exposes `request_coalition(demand_type, tick, context=None)` as the single entry point, and
whatever upstream signal wants to trigger a coalition calls it. This mirrors the existing pattern for AIC/PCC/
pACC (`ree_core/cingulate/*_analog.py`), all of which take injected signals via `update_signal()`/explicit
args rather than deriving their own from scratch. It is also the direct reading of SD-091's own scope
statement in claims.yaml: "this claim commits only to the architectural necessity of the graph-valued output
existing at all" -- not to an automatic typed-uncertainty classifier, which is separate future work. For the
MECH-481 4-arm falsifier itself, the experiment driver plays the Monitor+Classify role directly (the task
battery is deliberately constructed with known discrepancy types per trial, so the driver calls
`request_coalition(SENSORY_RESAMPLE, tick)` / `request_coalition(PROVENANCE_CHECK, tick)` at scripted trial
onsets). Arm 1 (monitoring-only) needs no new substrate at all -- REE already has distributed confidence and
reality-coherence-conflict signals; Arm 1 just uses those without ever calling `request_coalition`.

**Module location.** New top-level `ree_core/claustrum/` directory, paralleling `cingulate/`, `amygdala/`,
`pag/`, `hippocampal/` -- `ree_core/claustrum/control_demand.py` (the `ControlDemandType` enum, see below) and
`ree_core/claustrum/coalition_controller.py` (`CoalitionController`, `CoalitionControllerConfig`,
`CoalitionState`).

---

## 2. Which typed control-demand classes to build first

MECH-481's taxonomy has 10 classes. Building all 10 up front is out of scope -- most of them recruit
subsystems that do not exist yet in ree_core (checked directly: no `social`, `language`, or `reality_coherence`
module anywhere under `ree_core/`). Building a coalition template against a consumer substrate that isn't
there either produces an untestable template or forces a second, unplanned substrate build.

**Build exactly 2 at MVP: `SENSORY_RESAMPLE` and `PROVENANCE_CHECK`.**

This is not an arbitrary pick of "the two easiest" -- it is the literal worked pair from both source documents.
The source thought's own fully-specified example is `PROVENANCE_CHECK`. MECH-481's `what_would_answer` names
its illustrative minimal battery as "a perceptual-doubt trial requiring resampling and a provenance-doubt
trial requiring source reconstruction" -- i.e. `SENSORY_RESAMPLE` and `PROVENANCE_CHECK`, matched at difficulty.
Building precisely what the falsifier's own text calls for is the smallest thing that still lets Arm 3
(untyped) and Arm 4 (typed) differ meaningfully, because:

- Two types recruit genuinely disjoint subsystem sets, so a correctly-typed template produces a measurably
  different \(G_t\) per trial type. With only one type there is nothing to mismatch against and Arm 3 vs Arm 4
  collapse to the same behaviour by construction -- two is the minimum count for the ablation to be
  non-vacuous.
- Both map onto **already-built** consumer substrate, so no second implementation pass is smuggled into "just
  wiring the coalition controller":

  | Type | Recruits (existing substrate) | Suppresses |
  |---|---|---|
  | `SENSORY_RESAMPLE` | sensory encoder / E1 (`ree_core/predictors/e1_deep.py`) precision-routing target; E2 fast forward model (`e2_fast.py`) | E3 candidate-count throttling (temporarily raise `candidate_count` ceiling is a *parametric* side-effect the coalition may request via its own `channel_gain`, not a separate axis) |
  | `PROVENANCE_CHECK` | hippocampal anchor set / ARC-038 viability map (`ree_core/hippocampal/anchor_set.py`, `module.py`); MECH-269 persistence/appraisal compute (`persistence_appraisal_compute.py`); BetaGate / MECH-090 commit-entry predicate (`agent.py`, as the "E3 commitment monitor") | immediate motor commitment (attenuate BetaGate elevation eligibility); associative lock-in (attenuate hippocampal write-consolidation gate) |

  The `PROVENANCE_CHECK` recruit/suppress list above is taken directly from the source thought's own worked
  example (`docs/thoughts/2026-08-01_...md`, "Example" block), substituting the actual ree_core module names
  for the generic description. There is no equivalent existing "reality-coherence loop" *module* in ree_core
  (the phrase is used conceptually in claims.yaml/the source thought, not as a named component) -- the closest
  existing analogs are the hippocampal anchor/persistence substrate and BetaGate, and those are what the MVP
  template actually recruits. Do not invent a new reality-coherence module to satisfy the literal wording; if
  a future iteration needs one, that is its own claim.

**The other 8 classes stay register-only for now** (declared in the `ControlDemandType` enum so the taxonomy
is stable and extensible -- callers requesting an unregistered type get a no-op with a diagnostic counter, not
a crash, mirroring the codebase's "safe no-op default" convention). Rough triage for whoever picks this up
next, not a commitment of this doc:

- `INVARIANT_CONFLICT_REVIEW` and `COMMITMENT_REOPEN` are plausibly near-buildable next -- SD-034 (governance
  closure operator) and BetaGate/MECH-090 already exist and are close matches for their consumer substrate.
- `ACTION_OUTCOME_RECALIBRATION` overlaps SD-003 counterfactual attribution / dopamine-analog credit
  assignment, also plausibly near-buildable.
- `COUNTERFACTUAL_EXPANSION` needs deliberative branching, which SD-033e scopes as V4 work in the SD-032 doc --
  do not build a coalition template against a consumer that doesn't exist yet.
- `SOCIAL_MODEL_CHECK` and `LANGUAGE_EXPLICITATION` have no consumer substrate in ree_core at all as of this
  writing.
- `CROSS_HORIZON_RECONCILIATION` needs a multi-horizon comparison capability beyond E3's current single-horizon
  selector (`e3_selector.py`) -- unconfirmed, needs its own check before scoping.
- `SAFE_DEFER` is worth flagging as a possible taxonomy mismatch rather than a build target: "defer safely"
  reads as raising a commitment threshold / lowering confidence-to-commit, which is squarely *parametric*
  modulation (Arm 2 territory), not subsystem recruitment. It may not need coalition machinery at all. Leave
  this open for whoever registers the next batch rather than resolving it here.

---

## 3. Wiring into existing control-plane machinery (ARC-005 / MECH-004)

`CoalitionController` is instantiated in `agent.py` alongside (not inside) `SalienceCoordinator`, and the
dependency between the two is **one-directional**: the coalition controller reads the current `operating_mode`
(for the multiplicative composition above) but never writes into `SalienceCoordinator`'s mode selection or
`update_signal()` registry. This is a structural choice, not a naming convention, and it is what makes the
"keep coalition instantiation distinguishable from... mode classification" guardrail (below) enforceable rather
than aspirational: \(M_t\) selection cannot be perturbed by \(G_t\), by construction.

Integration point in `REEAgent.select_action`: `coalition.tick(current_tick)` runs after
`coordinator.tick()` (so it can read the freshly-updated `operating_mode`) and before consumer sites resolve
their effective recruitment weight. `CoalitionController.write_gate(target_name)` is the consumer-facing
accessor, deliberately named to match `SalienceCoordinator.write_gate(target_name)` (MECH-261) -- two
independent registries with the same call shape, composed multiplicatively at each consumer site, not merged
into one dict. Keeping them separate (rather than adding coalition entries into MECH-261's existing
`{target: {mode: weight}}` registry) matters because they answer different questions on different timescales:
`operating_mode` is a coarse, ~persistent regime (4 states); \(G_t\) is a transient, typed, per-trial
recruitment structure that can fire within any operating mode. Collapsing them into one registry would make it
impossible to later ask "did this coalition fire during external_task or during internal_planning" -- a
question MECH-481's Arm 4 scoring plausibly needs.

Config, following the `REEConfig`/`from_dims()` three-site pattern (see [memory]
`reference-reeconfig-from-dims-silent-kwargs`): `use_coalition_controller` (master, default `False`,
bit-identical off), `coalition_types_enabled` (default `[SENSORY_RESAMPLE, PROVENANCE_CHECK]`),
`coalition_max_duration_ticks` (default TBD by whoever builds this, informed by typical trial length in the
MECH-481 battery), `coalition_channel_gain_scale` (default 1.0).

---

## 4. Guardrails carried forward as hard constraints

These are verbatim from the source thought and MECH-481's registration notes, restated here as *structural*
constraints on the build (not reminders) so `/implement-substrate` can check against them directly:

- **Do not claim the claustrum is the seat of consciousness or metacognition.** Doc/docstring language only;
  no substrate consequence, but must not be dropped from comments/config names when this is built.
- **Do not collapse coalition control into global broadcasting.** Enforced structurally: `participating` is a
  sparse per-type dict, never a global all-on default. The untyped condition (Arm 3, "all discrepancy types
  collapse into one undifferentiated REFLECT trigger") is exactly the broadcasting failure mode, and it is a
  *test arm*, not the controller's own default behaviour -- if the controller's un-configured state ever looks
  like Arm 3, that is a bug.
- **Do not grant a central router unrestricted representational or governance authority.** Enforced
  structurally: `CoalitionController` never touches representational content, never computes reward, and can
  only *attenuate* participation -- it cannot raise BetaGate/MECH-090 commit-entry readiness above what
  BetaGate's own predicate independently allows. Coalition suppression of the "E3 commitment monitor" target
  can only lower commit-readiness or reallocate already-permitted attention, never force-open the commit
  boundary. This is the one guardrail with a concrete failure mode worth a contract test once built: assert
  `coalition_gate` on any BetaGate-adjacent target is monotone non-increasing in effect on commit-readiness.
- **Preserve typed authority/invariant/commit-boundary constraints (SD-034).** `coalition_gate` composes
  multiplicatively with, and never bypasses, SD-034/MECH-090 gates -- see the composition rule in Section 3.
- **Treat persistence and dissolution as load-bearing.** \(\Gamma_t\) is a real, measured, configurable
  timeout + completion-condition (Section 1), not a permanent no-op, even though the MVP's falsifier doesn't
  score persistence dynamics directly (scenario 5 is explicitly deferred).
- **Keep the biological mapping explicitly provisional.** Restate in module docstrings: the claustrum
  correspondence is functional/hypothesis-generating, not anatomical, per the source thought's own framing.
- **Keep coalition instantiation distinguishable from attention, global arousal, E3 trajectory selection, mode
  classification, confidence computation, working memory, and conscious access.** Structural arguments per
  mechanism, so this isn't just asserted:
  - *vs. mode classification*: one-directional dependency (Section 3) -- coalition reads mode, mode never
    reads coalition.
  - *vs. attention/precision (ARC-005/MECH-004)*: the coalition controller gates **which** subsystems'
    precision-routing is active this tick; it never itself computes a precision value. ARC-005/MECH-004 keep
    doing that unmodified.
  - *vs. E3 trajectory selection (`e3_selector.py`)*: coalition can attenuate the commit-monitor's readiness
    but never proposes, ranks, or selects candidate trajectories -- that stays E3's exclusive job.
  - *vs. confidence computation*: coalition **consumes** confidence/coherence signals as a trigger (via
    `request_coalition`) but does not produce them.

---

## Minimum-viable V3 implementation path

Ordered. Do not skip ahead.

1. **`ControlDemandType` enum** (`ree_core/claustrum/control_demand.py`) -- all 10 names from MECH-481's
   taxonomy declared up front (cheap, no dependency, avoids an enum-schema break later), but only 2 have real
   templates (step 3).
2. **`CoalitionController` + `CoalitionControllerConfig` + `CoalitionState`**
   (`ree_core/claustrum/coalition_controller.py`) -- the star-topology recruit/suppress/gain primitive,
   `request_coalition()` injection API, `write_gate(target)` accessor, minimal `Gamma_t` (timeout +
   completion-condition). No consumer wiring yet. `use_coalition_controller=False` no-op default.
3. **Wire the 2 MVP templates** (`SENSORY_RESAMPLE`, `PROVENANCE_CHECK`) as data into a
   `COALITION_TEMPLATES` dict, per the recruit/suppress table in Section 2.
4. **Wire consumer read sites.** Each named subsystem (E1/E2 sensory path; hippocampal anchor set/persistence-
   appraisal; BetaGate/MECH-090) calls `coalition.write_gate(name)` and composes it multiplicatively with
   whatever it already reads from `SalienceCoordinator.write_gate(name)`.
5. **Integrate into `REEAgent.select_action`** -- `coalition.tick()` after `coordinator.tick()`, reading
   `operating_mode` one-directionally (Section 3).
6. **Smoke test before queuing**: manually call `request_coalition(SENSORY_RESAMPLE, tick)` and
   `request_coalition(PROVENANCE_CHECK, tick)` in a dry run and confirm the two produce measurably different
   `write_gate()` outputs at every consumer site named in Section 2's table. This is the cheapest possible
   check that Arms 3 vs 4 of the falsifier *can* differ before spending a queued experiment on it.
7. **`/queue-experiment` the MECH-481 4-arm falsifier** once 1-6 land and the smoke test passes.

**Steps 1-2** are pure scaffolding (no behavioural effect possible yet, since nothing calls
`request_coalition`). **Steps 3-4** are what make \(G_t\) causally do something. **Step 5** integrates it into
the live agent loop. **Steps 6-7** validate.

**Register-only, no V3 implementation in this pass:** `PROVENANCE_CHECK`'s sibling 8 types remain declared-but-
untemplated (Section 2) until their own consumer substrates exist or are separately scoped.

---

## Falsification signatures

Substrate-level, designed to distinguish "the primitive is missing/misconfigured" from "the claim is actually
wrong" -- read together with MECH-481's own `what_would_answer` (4-arm PASS/FAIL/non-degeneracy criteria,
which this section does not restate).

**SD-091 (graph-valued output) is over-specified** if: Arm 2 (parametric-only) matches Arm 4 (typed coalition)
on the matched problem class -- i.e. raising precision/commitment threshold alone reproduces the type-selective
corrective behaviour with no subsystem-recruitment machinery at all. This is the claim's own stated falsifier
(claims.yaml `what_would_answer`).

**Typing specifically is doing no work** (a narrower, distinct failure from the one above -- coalition
instantiation as a mechanism may still be right, but the *typed* dimension is superfluous) if: Arm 3 (untyped,
one undifferentiated recruitment set) matches Arm 4 on the matched problem class. A generic "reflect harder"
coalition would suffice; the taxonomy adds nothing.

**The primitive is present but miswired** (not evidence against either claim) if: Arm 4 shows no measurable
difference between `SENSORY_RESAMPLE`-tagged and `PROVENANCE_CHECK`-tagged trials in which subsystems are
actually recruited -- e.g. both templates end up touching an overlapping subsystem set, or the multiplicative
composition with `mode_gate` zeroes the coalition signal out under the harness's operating mode. Check this
before treating a null Arm-4 result as informative: MECH-481's own non-degeneracy check (Arm 1 baseline
confidence/provenance signals must show non-zero cross-trial-type variance) rules out one confound; a
same-\(G_t\)-for-different-types check on Arm 4 directly (log `participating`/`suppressed` per trial and diff)
rules out this one.

**Persistence/dissolution failure** (secondary, scenario 5 per MECH-481's own scoping -- not part of the
primary falsifier, register separately if Arm 4 passes) if: coalitions measurably dissolve before
`completion_condition` fires, or routinely hit `max_duration_ticks` without dissolving, across trial types.

---

## Related claims

- **SD-091, MECH-481** -- this cluster
- **ARC-005** -- control plane precision/mode routing (parametric axis, unmodified by this claim)
- **MECH-004** -- signal-to-knob wiring map (the parametric analogue of this doc's Section 3)
- **MECH-019, MECH-039** -- modes as regions in control-channel space (the \(M_t\) axis this claim adds a
  parallel \(G_t\) axis alongside, not a replacement for)
- **MECH-063** -- orthogonal tonic/phasic axes (precedent for "add an axis without collapsing existing ones")
- **SD-032, SD-032a (SalienceCoordinator / MECH-261)** -- the existing mode-gate registry this doc's
  `write_gate` accessor deliberately mirrors and composes with, not replaces
- **SD-034** -- governance closure operator; commit-boundary constraint this claim must not bypass
- **MECH-090** -- commit-entry predicate (BetaGate); the concrete "E3 commitment monitor" target named in
  Section 2's `PROVENANCE_CHECK` template
- **SD-076** -- waking confidence inflation; one of the typed-discrepancy sources coalition instantiation
  would eventually need to consume (not built in this pass)

## References

Primary source: `docs/thoughts/2026-08-01_metacognitive_control_selective_cognitive_coalition_instantiation.md`
(full claustrum-grounding, falsification programme, and literature-pull targets -- not repeated here).

Template followed: `docs/architecture/sd_032_cingulate_integration_substrate.md` (minimum-viable-first
implementation ordering, subdivision table format, falsification-signature format).
