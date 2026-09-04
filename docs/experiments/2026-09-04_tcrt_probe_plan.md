# Temporary Coordinated Representational Transformations probe plan

Status: experiment plan / pre-architecture  
Date: 2026-09-04  
Source thought: `docs/thoughts/2026-09-02_temporary_coordinated_representational_transformations.md`  
Case: V3-EXQ-978 (hypothesis-generating; exact evidence artefact not yet located in current repository search)

## Question

Does successful REE behaviour depend on transiently coordinated transformation paths, rather than a fixed component, static route, or generic recurrence/state persistence?

## Hypotheses

**H1.** Success correlates with transient cross-component coordination trajectories more strongly than with any one component’s activation.

**H2.** Similar outcomes can be realised through different temporary coalitions while preserving functional transformation structure.

**H3.** Perturbing coordination timing/order harms performance even when per-component outputs/capacity are preserved.

**H4.** Narrow time-bounded protection of a critical representational path improves reliability beyond matched generic-capacity/noise controls.

**H5.** Fixed/static routing replays fail to reproduce or generalise the behaviour if temporal coordination is causally important.

## Measurements before intervention

Capture, using existing observability hooks where possible:

- iteration/step index;
- component/module identity;
- input/output or compact state signature;
- routing/selection influence using the nearest existing proxy (do not add a new “authority” mechanism yet);
- outcome metric;
- random seed and configuration;
- intervention mask when applicable; and
- protected-path metadata only if such a facility already exists.

Preserve raw traces so temporal permutations and trajectory alignment can be done offline.

## Controls

- activation-preserving temporal shuffle;
- fixed/static-router replay;
- top-specialist ablation;
- matched generic-capacity or noise-reduction control;
- recurrence/state-persistence matched control; and
- unperturbed successful and unsuccessful runs.

## Probe sequence

### Probe 0 — Trace sufficiency check

Instrumentation only. Verify that existing traces are sufficient to reconstruct candidate coordination trajectories without changing core architecture.

Pass: traces can distinguish at least component identity, order/timing, state signature, and outcome.  
Fail: add the minimum missing logging only; do not add authority-field machinery.

### Probe 1 — Trajectory alignment

Compare successful runs for repeatable transformation motifs while allowing component identity to vary.

Supports H1/H2 if motifs align more strongly by transformation pattern than by fixed component identity.

### Probe 2 — Temporal-order perturbation

Preserve component outputs/marginal statistics while shuffling selected coordination timing/order.

Supports H3 if performance degrades selectively relative to matched controls.

### Probe 3 — Static-router replay

Freeze or fit a routing pattern from successful runs and replay it across seeds/configurations.

Supports H5 if static replay reproduces less reliably/generalises worse than dynamic coordination.

### Probe 4 — Specialist-versus-coordination ablation

Compare removing the strongest putative specialist with preserving that component but breaking only its edges/window of coordination.

Supports process-over-module if coordination ablation is more damaging than specialist ablation after matched capacity control.

### Probe 5 — Protected-channel matched-control test

Temporarily protect one hypothesised representational path during a narrow transformation window.

Supports H4 only if benefit exceeds matched generic capacity/noise reduction and recurrence controls.

### Probe 6 — Cross-run substitution

Swap a functionally similar component into a coalition while preserving temporal structure.

Supports H2/process-over-module if behaviour survives identity substitution better than timing disruption.

## Falsification matrix

- One component predicts outcome and its ablation removes the effect -> favours specialist explanation.
- Temporal shuffle has no selective cost -> weakens H3/TCRT.
- Static-router replay matches dynamic behaviour -> weakens H5.
- Protected path performs no better than generic-capacity control -> weakens H4.
- Successful-run trajectories show no repeatable motifs -> weakens H1/H2.
- Effects vanish after persistence/recurrence matching -> favours generic state persistence.

## Execution order

1. Phase 0: trace sufficiency / instrumentation only.
2. Phase 1: observational trajectory alignment.
3. Phase 2: temporal shuffle and static-router replay.
4. Phase 3: specialist-versus-coordination ablation.
5. Phase 4: protected-channel test.
6. Phase 5: cross-run substitution.

## Decision gate

Do not add a core authority-field mechanism unless at least one effect is:

1. reproducible;
2. stronger than fixed/static or matched-capacity baselines; and
3. specifically dependent on temporal coordination/protection rather than generic recurrence or state persistence.

## Immediate implementation target

Start with Probe 0. Reuse existing logging/instrumentation and add only the minimum missing fields required to reconstruct a trajectory. No core routing, scoring, or authority semantics should change at this stage.
