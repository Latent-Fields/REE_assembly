# Q-081 Cross-Stream Organisation — Retrospective Telemetry Audit

**Date:** 2026-07-22T03:41:55Z
**Session:** `busy-wu-8041f2` (worktree)
**Spike type:** `complicated (buildable)` — scoping audit, not a probe
**Answers:** open question 6 of `docs/thoughts/2026-07-12_organisational_principles_of_cognition_across_heterogeneous_timescales.md` — *do REE's current logs contain sufficient telemetry to test cross-stream organisation?*
**Gates:** `Q-081` (`what_would_answer` names this audit as the precondition), `MECH-466`, `INV-091`, `ARC-112`
**Substrate audited:** `ree-v3` @ `65b2943276`; corpus `REE_assembly` @ `009f82ba75` (665 flat manifests + pack runs, 268 MB)

---

## Verdict

**NO — the existing corpus cannot answer Q-081 retrospectively. But no substrate change is needed.**

The gap is entirely in the **recording** and **configuration** layers, not the substrate. The signals overwhelmingly exist and are reachable at runtime; nothing durably writes them down, and four of them are switched off by default.

This splits the answer three ways, and the distinction matters because each layer has a different cost:

| Layer | State | Implication |
|---|---|---|
| **Runtime reachability** | **10 of 14 signals** computed per-step and reachable today | Good news — no substrate work |
| **Persistence** | **0 of 665 manifests** carry a per-step multi-stream trace | Fatal for retrospective analysis |
| **Configuration** | **4 of 14 signals do not exist under stock defaults** | Silent-null trap for any new run |

Consequence for routing: `MECH-466` was registered as **"retrospectively testable — no substrate change needed"** on the grounds that REE "already emits every required landmark". The first half of that is **wrong as stated** and should be corrected: REE *can* emit them, but has never *recorded* them, and its boundary segmenter is default-OFF. The claim's substance survives intact — the fix is a recording harness plus a config, not a substrate change — but "retrospectively testable" must become "prospectively testable on a cheap dedicated recording run".

---

## 1. Persistence layer — why retrospective analysis is impossible

**No manifest in the corpus contains a per-timestep multi-stream trace.**

- Grepping the corpus for `per_step` / `timeseries` / `trace` / `per_timestep` returns hits, but on inspection **every one is a scalar aggregate**, not a series: `harm_per_step_naive` (a float), `criteria/per_step_increases` (a 3-element threshold ladder), `per_seed[].R2.per_step_rel_delta` (2 floats). None is a time series.
- This is consistent with the Experimental Recording Standard's own corpus audit (`experimental_recording_standard_2026-07-12.md` §1), which measured **raw per-episode returns / trajectories at 0%**. That standard governs *manifest-level aggregates*; Q-081 needs *per-timestep vectors*. The standard does not cover this class of readout at all.

**The one partial precedent — and why it still fails Q-081.**

17 `*_episode_log.json` files exist, across 10 experiment families (~1.5% of the corpus): `223`/`223a` minimal-vertebrate, `471`/`475`/`524`/`664`/`665` fishtank showcases, `483`/`483a`/`483b` broadcast-override. These *are* genuine per-step multi-stream traces:

```
steps[] keys: t, action, pos, energy, health, harm_event, harm_signal, hazards,
              resources, mode, n_cands, transition_type, world_change_norm,
              z_beta_val, z_harm_norm, z_world_norm
```

Two reasons this cannot serve Q-081:

1. **It records norms, not vectors.** `z_world_norm` collapses a 32-D `z_world` to a single scalar; `z_harm_norm` and `z_beta_val` likewise. Q-081 asks whether streams "occupy recurrent system-level *configurations*" — a configuration is a point in a multi-dimensional state space, and a norm destroys exactly the structure being asked about. Recurrent-state and transition-matrix analysis over a 1-D norm is not a weakened version of the test; it is a different, uninformative one.
   - Partial exception worth keeping: `mode` and `transition_type` **are** categorical state labels, i.e. genuine transition-motif material. They are the only Q-081-shaped fields the corpus contains — for one stream, in 10 unrelated families.
2. **Coverage is wrong and not extensible.** None of the 10 families is a cross-stream experiment; they are showcases and single-mechanism ablations. And there is **no shared writer** — the episode-log block is copy-pasted across 15 experiment scripts with no `experiments/_lib/` recorder (confirmed: `_lib/` has 24 modules, none of them a trace/episode recorder). So the pattern cannot be turned on for a new experiment without re-implementing it.

---

## 2. Runtime reachability — the 14 signals

Verdicts: **EXPOSED** = returned in a dict; **LIVE** = readable attribute after `act()`; **TRANSIENT** = computed then discarded.

| # | Signal | Holder | Verdict | Frequency | Default-OFF flag |
|---|---|---|---|---|---|
| 1 | E1 hidden state | `agent.e1._hidden_state` (h, c) | LIVE | every step | — |
| 2 | E2 PE | *see §2.1 — not instrumented as a stream* | partial | only if loop calls `update_residue()` | — |
| 3 | E3 candidate scores | `agent.e3.last_scores` / `.last_raw_scores` | LIVE | **E3 tick only (~1 in 10)** | — |
| 4 | E3 commitment state | `agent.e3.get_commitment_state()` | EXPOSED | E3 tick; beta gate every step | — |
| 5 | `z_self` | `agent._current_latent.z_self` `[B,32]` | LIVE | every step | — |
| 6 | `z_world` | `agent._current_latent.z_world` `[B,32]` | LIVE | every step | — |
| 7 | `z_harm_s` | `agent._current_latent.z_harm` `[B,32]` | LIVE | every step | **`latent.use_harm_stream=False`** |
| 8 | `z_harm_a` | `agent._current_latent.z_harm_a` `[B,16]` | LIVE | every step | **`latent.use_affective_harm_stream=False`** |
| 9 | `z_goal` | `agent.goal_state.z_goal` `[1,32]` | LIVE | **only when loop calls `update_z_goal()`** | stays zero if never updated |
| 10 | `operating_mode` | `agent._salience_last_tick["operating_mode"]` | LIVE | E3 tick only | **`use_salience_coordinator=False`** |
| 11 | beta | `agent._current_latent.z_beta` `[B,64]`; `agent.beta_gate.is_elevated` | LIVE | every step | — |
| 12 | boundary broadcasts | `agent.hippocampal._boundary_event_queue` | LIVE but **destructively drained** | **event-sparse** (~1/40 slow; fast capped 1/2) | **`hippocampal.use_event_segmenter=False`** |
| 13 | hippocampal proposals | `agent._committed_candidates` | LIVE | E3 tick only | — |
| 14 | residue updates | `agent.update_residue()` return dict | EXPOSED | **harm-event-sparse** (writes only when `harm_signal < 0`) | — |
| + | offline/sleep markers | `agent.e1._offline_mode`; `SleepLoopManager.state.phase` | LIVE | every 100 steps / episode-end | `SleepLoopManager` not owned by the agent |

All six flags verified `= False` at their definition sites in `ree_core/utils/config.py` (lines 86, 97, 1827, 1836, 2456, 3292).

**The most useful single find:** `agent.get_state() -> AgentState` (`ree_core/agent.py:9777`, dataclass at `:263`) is an **ungated one-call snapshot** carrying `latent_state` (hence z_self / z_world / z_harm / z_harm_a / z_beta), `precision`, `running_variance`, `step`, `harm_accumulated`, `is_committed`, `beta_elevated`, `e3_steps_per_tick`, `serotonin_state`. A recorder can get most of the checklist from one call per step.

There is **no** aggregate per-step telemetry dict from `act()` — `REEAgent.act()` (`agent.py:7878`) returns only an action tensor. Four partial aggregators exist (`update_residue()` metrics, `get_state()`, `_last_control_vector` (gated), `_salience_last_tick` (gated)); only `get_state()` is both broad and ungated.

### 2.1 E2 PE is the weakest link — and Q-081 lists it as a stream

There is **no per-step E2-self prediction error on the default path.** What the codebase calls prediction error (`e3_selector.py:3286`) is `actual_z_world - committed_trajectory.world_states[1]` — an **E3/world-rollout** error, not E2's `predict_next_self` error — and it is only computed when the experiment loop calls `update_residue()`, never from `act()`. That `update_running_variance` is called from exactly one place in `ree_core`, and that experiment scripts routinely call it themselves (e.g. `experiments/v3_exq_396a_arc016_precision_sweep_rv_fix.py:197`), confirms the substrate does not maintain it in the hot loop.

True per-step E2-self error is computed transiently in two places and discarded except for a derived scalar: `_update_blocked_agency` (`agent.py:3282`, only `z_block` survives) and `_update_tpj_comparator` (`agent.py:3047` → `agent._tpj_last_agency_signal`), both behind default-OFF flags (`use_blocked_agency`, `use_tpj_comparator`).

**So "E2 PE" as a per-step stream does not currently exist.** Any Q-081 design must either drop it, substitute the E3 world-rollout error and say so explicitly, or enable a comparator flag.

---

## 3. The sampling trap — a recorder can *manufacture* Outcome B

This is the finding most likely to invalidate a Q-081 experiment, and it is not obvious.

REE's multi-rate clock (`config.py:2122-2124`) defaults to **E1 every step, E2 every 3, E3 every 10**. Between E3 ticks, `select_action` short-circuits (`agent.py:5463`) and returns the held action — so **E3 candidate scores, `operating_mode`, hippocampal proposals and commitment state are not recomputed on 9 of every 10 steps; they are held stale.**

A naive per-step recorder therefore writes 9 duplicated values followed by 1 fresh value, for every E3-derived stream. Cross-stream analysis over that trace will find strong, highly regular shared structure — **which is precisely Outcome B (structure trivially implied by the configured rates), arriving as an artefact of the sampler rather than a property of the system.** Q-081's `what_would_answer` already names the rate-matched shuffle control as "not optional"; this audit adds the sharper point that **the shuffle control must be matched to the actual tick schedule, and the trace must carry a per-signal freshness/tick flag** so held values can be distinguished from recomputed ones. Without that flag the shuffle control cannot be constructed correctly after the fact.

Two further recording hazards:

- **Boundary events are destructively drained.** `agent.py:4217-4220` calls `drain_boundary_events()` / `drain_broadcast_events()` and **discards the returned lists**, then clears the queue at the start of the next `sense()`. A recorder must sample after `act()` and before the next `act()`, or it records nothing — silently.
- **Event-sparse ≠ missing.** Boundary broadcasts (~1/40 steps) and residue writes (harm-events only) are legitimately sparse. A non-degeneracy guard is needed at both ends: `MECH-466` already carries one (boundary rate must not be floor- or ceiling-pinned), and it should be applied to residue too.

---

## 4. What is actually needed (all `complicated (buildable)`)

No unknowns remain — this is execution backlog, not discovery debt.

1. **A shared per-step recorder** in `experiments/_lib/` (there is none). Sample `agent.get_state()` + the E3/salience/hippocampal caches + drained boundary events, once per env step, into a per-run trace artifact. Must emit a **per-signal freshness flag** (§3) and store **vectors, not norms** (§1).
2. **Store the trace by reference, not inline.** At 32-D × ~6 streams × steps × seeds this is far too large for a git-tracked manifest; the Recording Standard §3d already mandates content-addressed pointers for bulky arrays. The coordination plane must not absorb this.
3. **A config profile enabling the four dark signals** — `use_harm_stream`, `use_affective_harm_stream`, `use_salience_coordinator`, `use_event_segmenter` (+ `use_invalidation_trigger` for MECH-287 broadcasts). Note this makes the run **non-default substrate**, which must be declared: results describe a configuration REE does not normally run in.
4. **An explicit decision on E2 PE** (§2.1) — drop, substitute-and-declare, or enable a comparator flag.
5. **`z_goal` and sleep-phase markers need the experiment loop to drive them** — `update_z_goal()` is loop-called, and `SleepLoopManager` is not instantiated by `REEAgent`. The harness must own both or those streams are flat.

Once (1)–(5) exist, one cheap dedicated recording run yields the trace, and `Q-081`/`MECH-466` become analysis-only over it.

---

## 5. Claim-registry corrections this audit implies

Not applied by this session — flagged for `/governance`.

- **`MECH-466` notes** say "REE already emits every required landmark (MECH-288 boundary pulses, the beta commitment gate, mode transitions, sleep-phase markers), so no substrate change is needed." **Correct the first clause**: the boundary segmenter and salience coordinator are default-OFF, sleep-phase management is not agent-owned, and nothing has ever recorded any of it. The conclusion (*no substrate change needed*) **stands**; "retrospectively testable" does not.
- **`Q-081` `what_would_answer`** should absorb §3: the rate-matched shuffle control must be matched to the **actual tick schedule**, and the trace must carry per-signal freshness flags, or Outcome B cannot be excluded.
- **`ARC-112` / `INV-091`** unaffected — neither depends on retrospective availability.
