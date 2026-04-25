---
nav_exclude: true
---

# Sleep-Aggregation Cluster: MECH-272 / MECH-273 / MECH-275 / MECH-285

**Claim cluster:**
- MECH-272 -- state-gated routing of hippocampal replay (anchor channel waking, probe channel sleep)
- MECH-273 -- sleep half of the self-model: full-Bayesian aggregation of single-episode SD-003 outputs
- MECH-275 -- general sleep-phase Bayesian aggregation across attribution domains (parent of MECH-273)
- MECH-285 -- sleep-consolidation priority biased by MECH-284 V_s residual schema-staleness map

**Status:** candidate, v3_pending (all four)
**Phase status (substrate):** none of the four implemented; this doc commits the build order
**Registered:** 2026-04-25
**Sibling docs (do NOT duplicate):**
- `sd_017_sleep_phase_architecture.md` -- minimal V3 SWS/REM phase machinery (parent infrastructure)
- `v_s_invalidation_runtime.md` -- MECH-284 online arm + MECH-287 trigger (already implemented through Phase 3)
- `sleep/offline_phases.md` -- V4 full sub-phase ordering (MECH-120-123)
- `default_mode.md` -- MECH-092 quiescent waking replay (V3 prerequisite)

**Lit-pull dependencies:**
- `targeted_review_mech285_sleep_replay_seed/SYNTHESIS.md` -- 5 verdicts grounding seed-pool, priority shape, timing, salience separation, dual-trace
- `targeted_review_connectome_mech_273/` -- 5 entries (lit_conf 0.77)
- `targeted_review_connectome_mech_275/` -- 4 entries (lit_conf 0.85)
- `targeted_review_v_s_foundation/SYNTHESIS.md` -- per-region V_s, dual-trace anchor preservation

**Depends on (substrate-ready as of 2026-04-25):**
SD-017 design only / no implementation; MECH-284 Phase 3 online arm; MECH-269 anchor selection +
hysteresis; MECH-287 broadcast trigger; SD-003 self-attribution + ARC-033 E2_harm_s + SD-013
contrastive training; MECH-094 simulation-mode write gate; AnchorSet dual-trace preservation.

**Implementation gaps to be closed (in order):**
1. Sleep-loop scaffolding (SD-017 minimal -- never implemented)
2. MECH-285 offline-arm replay sampler (deferred in v_s_invalidation_runtime.md)
3. MECH-272 routing gate (referenced by MECH-269/271/284 but no module exists)
4. MECH-275 general Bayesian aggregator
5. MECH-273 self-model specialisation

---

## Problem

The waking-phase architecture as of 2026-04-25 produces episode-local attribution and
schema-staleness signals, but does not aggregate them. SD-003 emits a per-episode causal
signature; MECH-284 emits a per-region staleness scalar; MECH-269 marks anchors inactive.
None of these are integrated across episodes. Without an offline aggregation pass:

- Episode-local self-attribution remains noisy. SD-003's causal_sig is computed on a
  single (z_t, a_actual, a_cf) tuple. Systematic biases (e.g. reward delay, observation
  noise on outcomes) propagate uncorrected into E2_harm_s. The agent has a *signature*
  but not a *self-model* in the durable sense (MECH-273).
- Schema-revision is single-step. MECH-284 staleness biases the next anchor selection
  (online), but the inactive anchor's content is never re-examined against accumulated
  evidence from other episodes. The dual-trace is preserved (MECH-269 mark_inactive)
  but never integrated.
- Other attribution domains (object schemas, social attribution, place schemas) need the
  same aggregation pattern. MECH-275 generalises the pattern; MECH-273 specialises it
  to self.

The cluster's job is to take the waking-phase residuals (SD-003 outputs, MECH-284
staleness map, AnchorSet dual-trace, MECH-276 counterfactual feedstock) and run a periodic
offline pass that:

1. Selects which content to re-examine (MECH-285, staleness-weighted broad coverage).
2. Routes that content through a different consumer set than waking (MECH-272, probe
   channel dominant).
3. Aggregates evidence across replays into a posterior update (MECH-275).
4. Specialises the aggregator output to write back to E2_harm_s and SD-033a (MECH-273).

---

## Architectural commitments

### C1. Sleep-mode entry is deterministic in V3

Sleep-mode entry triggers at end of every K episodes (configurable; default K=8 to match
SD-017 narrative). SD-037 broadcast-override-driven entry (sustained low-arousal, high
drive) is a known refinement but is **deferred to V4**. Reason: SD-037 just landed and is
under validation (V3-EXQ-483); coupling sleep entry to it now risks compounding uncertainty.

V3 sleep entry is a hard switch: external observation gating closes (MECH-122 placeholder),
goal-seeded action selection pauses (drive_level frozen at entry value), and the heartbeat
clock continues but routes ticks to the sleep loop instead of the action loop.

### C2. Module location: new `ree_core/sleep/` package

A self-contained package, mirroring the architectural cluster. Rationale: the four MECHs
share state (sleep phase, replay buffer, posterior store), share the dependency on the
StalenessAccumulator snapshot, and share MECH-094 simulation-mode tagging. Distributing
across hippocampal/, predictors/, pfc/ would triplicate the phase contract.

The package owns:

- `sleep/phase_manager.py` -- SleepPhase enum (`WAKING`, `SWS_ANALOG`, `REM_ANALOG`),
  entry/exit conditions, tick router. Wires into REEAgent.step().
- `sleep/replay_sampler.py` -- MECH-285. Reads StalenessAccumulator snapshot + AnchorSet
  dual-trace; emits ordered seed sequence per phase tick.
- `sleep/routing_gate.py` -- MECH-272. State-conditioned channel weights consumed by
  the existing MECH-271 hippocampal router (anchor vs probe channel destination weights).
- `sleep/bayesian_aggregator.py` -- MECH-275. Maintains posteriors per attribution domain;
  consumes probe-channel replay events; emits posterior-update messages.
- `sleep/self_model_aggregator.py` -- MECH-273. Subclass of the general aggregator
  specialised on SD-003 causal_sig posterior; writes corrected residuals into E2_harm_s
  via offline gradient pass.

### C3. Seed pool is BROAD; priority is staleness-proportional softmax

Per `targeted_review_mech285_sleep_replay_seed/SYNTHESIS.md` verdicts 1, 2, and 5:

- Seed pool = full AnchorSet (active + inactive anchors with dual-trace preserved).
  No active-only filter, no time-since-invalidation gate.
- Priority = `softmax(staleness[r] / temperature)` over the broad pool. Continuous,
  not threshold-gated. Temperature is a tunable scalar (default `1.0`); lower
  temperatures concentrate replay on the most-staled regions, higher temperatures spread
  it.
- Salience-driven replay (MECH-074b dopamine tag) operates on a separate channel
  (retrieval-SWR arm) and is not arbitrated against staleness here. MECH-285 modifies
  only the consolidation-SWR arm.
- MECH-284 must continue accumulating on inactive regions after `mark_inactive`. The
  online arm currently does this implicitly (the per-region accumulator is keyed on
  (scale, segment_id), independent of the AnchorSet active flag); the offline arm relies
  on this and the contract should be made explicit in the StalenessAccumulator docstring.

### C4. MECH-272 routing is a destination-weight flip, not a proposer change

MECH-271 already specifies that anchored replay routes to subiculum -> entorhinal deep ->
neocortex (E1 consolidation) and to SD-033a (rule/goal viability), and probe-channel
replay routes to attribution-aggregation consumers. MECH-272 says these route weights are
*state-gated*:

| Phase           | anchor_channel weight | probe_channel weight |
|-----------------|----------------------|---------------------|
| WAKING          | 1.0                  | 0.0                 |
| SWS_ANALOG      | 0.6                  | 0.4                 |
| REM_ANALOG      | 0.2                  | 0.8                 |

Defaults are placeholders -- the V3 validation experiment (EXP-0169 schema-revision arm)
should sweep these. The proposer (MECH-269) keeps producing anchor-rooted trajectories
in both phases; the *routing* changes which downstream consumer receives them. SWS-analog
biases toward consolidation (anchor channel still meaningful); REM-analog biases toward
attribution-revision (probe channel dominant).

### C5. MECH-275 posterior is a per-domain Gaussian over residuals

Initial implementation maintains one Gaussian-distributed posterior per attribution
domain. Domains in V3:

- `self` (MECH-273): posterior over E2_harm_s prediction residuals indexed by causal_sig
  bucket (e.g., quartile of causal_sig magnitude per anchor region).
- `place` (MECH-275 directly): posterior over per-region V_s residuals -- a Bayesian
  upgrade of MECH-284's leaky integrator.
- `object` and `other` are V4 domains (object-schema revision; MECH-274 social
  attribution). Schema slot reserved; no implementation in V3.

Each posterior is updated per replayed event with a standard mean-and-variance update:
prior = current posterior, evidence = SD-003 output for self / V_s residual for place,
likelihood variance = config-tunable. No reliance on a probabilistic-programming framework;
plain numpy/torch arithmetic.

The aggregator's output is a posterior-update message: `(domain, region, delta_mean,
delta_variance, n_replays)`. Consumers decide what to do with it.

### C6. MECH-273 writes back to E2_harm_s as offline gradient steps

The self-model aggregator's posterior over SD-003 residuals is consumed during sleep by
running a low-LR offline gradient pass on E2_harm_s, using the corrected residuals as
training targets. MECH-094 simulation-mode tag is set throughout (so this offline pass
does NOT propagate to E1 viability map updates -- it is a self-model parameter update,
not an experience write).

Default offline LR = `0.1 * waking_LR`. Number of offline gradient steps per sleep cycle
is bounded (default 100) to keep sleep-cycle wallclock predictable. SHY normalisation
(MECH-120, V4) is the natural follow-on but is **out of scope** for V3.

The alternative would be to maintain a runtime bias term added to E2_harm_s outputs at
inference time (no weight update). Rejected because: (a) the bias term grows unboundedly
across many sleep cycles without a rule for decay; (b) the biological mechanism is
synaptic update (NREM consolidation), and the engineering story is cleaner if we mirror
that; (c) downstream consumers (SD-013 contrastive training) already expect E2_harm_s as
a learnable module.

### C7. MECH-094 tag enforcement throughout

All replay events generated by the sleep loop carry `simulation_mode=True`. This blocks:

- Hippocampal viability map writes (MECH-094 already enforces this on simulated rollouts).
- StalenessAccumulator integration (already enforced -- `integrate()` is only called from
  `REEAgent.sense()`, which is the waking observation stream; sleep-loop ticks must not
  call sense()).
- E1 experience-stream consolidation (the SWS-analog routing is a *schema* update, not
  an episodic write).

The MECH-273 offline gradient pass on E2_harm_s is the single explicit exception: it IS a
parameter update during simulation-mode, but it is gated behind the self-model aggregator
specifically and does not propagate elsewhere.

---

## Phase ordering within a sleep cycle

```
SLEEP_ENTRY:
  - phase_manager: WAKING -> SWS_ANALOG
  - StalenessAccumulator.snapshot() -> staleness_map (frozen for this cycle)
  - replay_sampler.seed_pool = AnchorSet.all_with_dual_trace()
  - routing_gate.weights -> SWS_ANALOG row
  - external observation gating closes; drive_level frozen

SWS_ANALOG (N1 ticks, default 50):
  for tick in range(N1):
    seed = replay_sampler.draw(staleness_map)
    replay_event = hippocampal_proposer(seed, simulation_mode=True)
    routed = routing_gate.route(replay_event)
    if routed.anchor_channel:
      e1_consolidation_consumer(routed)        # context-template update (SD-017)
    if routed.probe_channel:
      bayesian_aggregator.update(routed)        # posterior accumulates

PHASE_SWITCH:
  - phase_manager: SWS_ANALOG -> REM_ANALOG
  - routing_gate.weights -> REM_ANALOG row
  - bayesian_aggregator.snapshot() -> posterior_at_phase_switch (debug)

REM_ANALOG (N2 ticks, default 50):
  for tick in range(N2):
    seed = replay_sampler.draw(staleness_map)        # same map, broader read in REM
    replay_event = hippocampal_proposer(seed, simulation_mode=True)
    routed = routing_gate.route(replay_event)
    bayesian_aggregator.update(routed)

WRITEBACK:
  - self_model_aggregator.offline_gradient_pass(e2_harm_s, n_steps=100)
  - StalenessAccumulator.partial_decay(replayed_regions, decay_factor=0.5)
    # regions that got replayed get an extra leak -- "this got addressed"
  - phase_manager: REM_ANALOG -> WAKING
  - external observation gating opens; drive_level resumes accumulating
```

The N1/N2 split is configurable; the SWS-bias-toward-anchor-channel and REM-bias-toward-
probe-channel is the load-bearing biological commitment. Setting N1=0 reduces the cycle to
"REM-only attribution revision"; setting N2=0 reduces it to "SWS-only schema consolidation."
Both edge cases are valid for ablation experiments.

---

## State and contracts

### Sleep-loop state

Owned by `sleep/phase_manager.py`. Per-cycle:

```
SleepCycleState:
  cycle_id: int                          # monotone counter
  entry_episode: int                     # which waking episode triggered entry
  entry_utc: str
  staleness_snapshot: Dict[RegionKey, float]  # frozen at entry
  current_phase: SleepPhase
  ticks_in_phase: int
  posterior_snapshots: List[...]         # one at SWS exit, one at REM exit
  writeback_summary: dict                # n_grad_steps, regions_decayed, etc.
```

### Posterior store

Owned by `sleep/bayesian_aggregator.py`. Lives across cycles:

```
DomainPosterior:
  domain: Literal["self", "place"]
  per_region: Dict[RegionKey, GaussianPosterior]  # mean, variance, n_evidence
  cycle_history: List[(cycle_id, snapshot)]
```

Persisted via the existing checkpoint path. MECH-275's per-region per-domain posterior
is the durable self/place model that survives across episodes.

### Routing-gate contract

`routing_gate.route(event) -> RoutedEvent` with `RoutedEvent.anchor_channel: float` and
`RoutedEvent.probe_channel: float`. Both consumers downstream multiply their write
strength by the channel weight. This is the single place MECH-272's state-conditioned
routing is enforced.

### MECH-285 sampler contract

`SleepReplaySampler.draw(staleness_snapshot) -> AnchorRef`:

```
def draw(self, staleness_snapshot):
    seeds = self._anchor_set.all_with_dual_trace()
    weights = softmax([staleness_snapshot.get(s.region_key, 0.0) / self.temperature
                       for s in seeds])
    return numpy.random.choice(seeds, p=weights)
```

Stateless across draws within a cycle; the snapshot is frozen at entry.

---

## Validation plan

| Phase | What lands | Validation experiment | Acceptance criterion |
|-------|-----------|----------------------|---------------------|
| A | Sleep loop scaffolding (`phase_manager`, default-no-op `replay_sampler`, `routing_gate`, `bayesian_aggregator` stubs); SD-017 SWS/REM phase contract | V3-EXQ-NNN smoke: agent runs N waking episodes, enters sleep, returns to waking; bit-identical waking trajectory with `use_sleep_loop=False` | bit-identical OFF; sleep cycle completes without exception ON |
| B | MECH-285 offline arm (`SleepReplaySampler` reads StalenessAccumulator snapshot, broad pool, staleness-softmax) | EXP-0168 (already drafted in proposals): high vs low waking trigger load over region R | sleep replay event count over R scales monotonically with `staleness[R]` at sleep entry, 2/2 seeds |
| C | MECH-272 routing gate: state-conditioned channel weights, wired into MECH-271 router | V3-EXQ-NNN: anchor-channel-only vs probe-channel-only sleep cycle | E1 ContextMemory updates only with anchor channel ON; aggregator posterior updates only with probe channel ON |
| D | MECH-275 general Bayesian aggregator: per-domain posteriors, update from probe-channel events, snapshot+decay contract | EXP-0169 (already drafted): seed waking with biased self-attribution; sleep aggregator should correct it | mean of `self`-domain posterior shifts toward true causal_sig by >= 0.5 SD across 3 sleep cycles |
| E | MECH-273 self-model offline gradient pass to E2_harm_s | V3-EXQ-NNN: with vs without offline writeback; measure E2_harm_s prediction residual on held-out tuples | residual decreases monotonically across 5 sleep cycles with writeback ON; flat or increasing OFF |

EXP-0168 and EXP-0169 are already in `experiment_proposals.v1.json` (status=gated). They
unblock at Phase B and Phase D respectively.

---

## Falsifiability and clinical mappings

Three failure modes per cluster member are predicted and would falsify the claim:

| Claim    | Failure mode                                                  | Predicted phenotype                                                         |
|----------|---------------------------------------------------------------|------------------------------------------------------------------------------|
| MECH-272 | Routing weights do not flip across phase                      | sleep cycle produces no aggregator updates; or waking writes get probe-routed |
| MECH-273 | Offline gradient pass diverges or overcorrects                | E2_harm_s residuals oscillate; SD-003 causal_sig drifts cycle-over-cycle    |
| MECH-275 | Posterior over place V_s diverges from MECH-284 ground truth  | sleep map never converges to schema-staleness; replay priority becomes random |
| MECH-285 | Replay event count over high-staleness region indistinguishable from low-staleness | EXP-0168 FAIL: priority is salience-driven only; staleness signal is inert  |

Clinical mappings (Daniel's interest; intentionally lightly stated):

- **PTSD intrusive replay:** MECH-094 tag loss + intact MECH-285 staleness priority -> traumatic
  trace gets high replay priority but is mis-routed (waking intrusion). Treatment target: tag
  function, not staleness suppression.
- **Confabulation in dementia:** MECH-273 offline writeback proceeds but on a corrupted SD-003
  causal_sig (E2_harm_s mis-predicting); the self-model accumulates stable false attributions
  across cycles. Distinct from psychosis (MECH-094 acute tag failure).
- **Depression rumination:** posterior in `self` domain drifts toward elevated harm-attribution
  baseline; replay priority biased toward most-negative regions; offline writeback amplifies the
  bias rather than correcting it. Plausible target: temperature increase in MECH-285 sampler,
  staleness leak rate increase in MECH-284.

---

## Out of scope (deferred to V4)

- SD-037-driven sleep entry (sustained low-arousal trigger). Currently V3 uses deterministic
  K-episode trigger.
- Object-schema and social-attribution domains (MECH-274 + MECH-275 object specialisation).
- SHY synaptic homeostasis (MECH-120) on the offline gradient pass.
- Spindle-equivalent thalamic gating (MECH-122) on observation stream during sleep --
  V3 uses a hard switch in `phase_manager`.
- Bidirectional ThetaBuffer (MECH-122 Phase 3 rewiring) -- V3 routing-gate is destination-only.
- Mode-conditioned replay-content selection beyond the staleness-vs-salience separation
  (Joo & Frank 2018 multi-mode SWR). V3 single-priority sampler is sufficient.

---

## Implementation plan (build order)

| # | Module / change                                              | Claim(s) implemented           | Estimated session count | Validation gate                     |
|---|--------------------------------------------------------------|-------------------------------|------------------------|-------------------------------------|
| 1 | `ree_core/sleep/__init__.py`, `phase_manager.py`, SleepPhase enum, REEAgent.step() integration, `use_sleep_loop` flag default False | -- (scaffolding for SD-017)    | 1                      | smoke: bit-identical waking OFF/ON  |
| 2 | `sleep/replay_sampler.py` SleepReplaySampler; AnchorSet.all_with_dual_trace() helper; explicit StalenessAccumulator inactive-region contract in docstring | MECH-285 (offline arm)         | 1                      | EXP-0168 PASS                       |
| 3 | `sleep/routing_gate.py` RoutingGate; extend MECH-271 router consumer (HippocampalRouter) with channel-weight multiplication | MECH-272                       | 1                      | C-phase ablation experiment         |
| 4 | `sleep/bayesian_aggregator.py` GeneralBayesianAggregator; per-domain GaussianPosterior; cycle snapshot + decay | MECH-275                       | 1-2                    | EXP-0169 PASS                       |
| 5 | `sleep/self_model_aggregator.py` SelfModelAggregator (subclass); offline E2_harm_s gradient pass; MECH-094 tag enforcement audit | MECH-273                       | 1                      | E-phase residual experiment         |

Each step lands behind its own master flag (`use_sleep_loop`, `use_mech285_sampler`,
`use_mech272_routing`, `use_mech275_aggregator`, `use_mech273_self_model`). Defaults all
False so the cluster lands incrementally without affecting any in-flight experiment. The
contract tests (`tests/contracts/`) get one new file per step asserting bit-identical
behaviour with the flag OFF and the new behaviour with the flag ON.

Total estimate: 5-6 implementation sessions, 5 validation experiments. The first two steps
unblock EXP-0168 (already drafted, gated). All five steps unblock EXP-0169.

---

## See also

- `sd_017_sleep_phase_architecture.md` -- parent infrastructure (phase machinery, Bayesian framing)
- `v_s_invalidation_runtime.md` -- MECH-284 / MECH-287 / MECH-269 online arm
- `sleep/offline_phases.md` -- V4 full sub-phase ordering
- `default_mode.md` -- MECH-092 quiescent waking replay
- `evidence/literature/targeted_review_mech285_sleep_replay_seed/SYNTHESIS.md` -- design verdicts
