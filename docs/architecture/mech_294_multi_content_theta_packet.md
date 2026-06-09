# MECH-294 Multi-Content Theta-Burst Packet -- Substrate Design Memo

- **Status:** design memo (substrate not yet implemented). Plan-of-record for the
  `/implement-substrate` pass that would unblock MECH-294.
- **Author session:** `mech294-multi-content-theta-packet-memo` 2026-06-09.
- **Routed by:** `/queue-experiment` substrate-readiness gate (Step 2.5) found
  MECH-294 `blocked_substrate` on 2026-06-09 -- the claim asks for a behavioural
  experiment, but the V3 substrate implements only single-content temporal
  averaging (MECH-089 ThetaBuffer), so any MECH-294 experiment on the current
  substrate would be vacuous (it cannot construct a joint multi-content packet to
  test).
- **Claim:** [MECH-294](../claims/claims.yaml) (candidate, `v3_pending`,
  `implementation_phase: v3`).
- **Parent mechanism:** [MECH-089](../claims/claims.yaml) ThetaBuffer
  (`ree-v3/ree_core/latent/theta_buffer.py`).
- **Literature anchor:** `evidence/literature/targeted_review_mech294_theta_burst_packet/`
  (7 entries; SYNTHESIS verdict SPARSE-BUT-NOT-FALSIFYING). No new lit-pull was
  needed for this memo -- the existing review already isolates the single
  load-bearing empirical risk (Kay et al. 2020 cross-cycle alternation), which is
  what the discriminative experiment below is built to resolve.
- **Scope:** design only. This memo does NOT edit `claims.yaml`, does NOT queue
  experiments, and does NOT change substrate code. It specifies the substrate, the
  joint-read interface, the Kay-2020 falsifier resolution, and the discriminative
  validation experiment that an implementation pass would build.

---

## 1. What MECH-294 actually claims (and what is load-bearing)

MECH-294: each ~125 ms theta cycle binds a **{goal_latent, action_proposal,
risk_estimate, state_summary}** tuple into **one phase-aligned packet**, and the
proposer reads that packet as a **joint object** -- which `action_proposal` is on
the table is interpretable only against the `goal_latent` and `risk_estimate`
co-bound in the *same* cycle.

The **load-bearing** part is the word *joint*. MECH-294 is explicitly NOT the claim
that one content stream is theta-locked, nor that several streams alternate one per
cycle. It is the claim that four heterogeneous streams are bound **within one
cycle** so that a downstream reader can condition on the co-binding.

Two further commitments ride on the claim:

1. **Verisimilitude vintaging (MECH-269/269b).** The packet is not a homogeneous
   "current latent". Each component carries its own temporal vintage: an
   anchor-eligible stream (high per-stream V_s) contributes its *current* value;
   a misaligned stream (low V_s) contributes its *last-verified snapshot*. The
   packet is a **stream-typed object whose components may have different ages**.
2. **Rollout-ahead-of-real-time.** The packet at cycle `t` feeds the rollout
   step at `t+1`; the rollout horizon must exceed sensory arrival latency or the
   packet's gates fire after the action is already committed. (This is a timing
   property of the consumer loop, satisfied by REE's existing E3-heartbeat /
   committed-trajectory-stepping machinery -- MECH-090 -- and is not the part the
   substrate gap blocks. It is noted here for completeness; the binding-window
   substrate is what is missing.)

## 2. The current substrate, and why it is `blocked_substrate`

`ree-v3/ree_core/latent/theta_buffer.py` (MECH-089) implements **single-content
temporal averaging**:

- It buffers ONLY `z_world` and `z_self`
  (`ThetaBuffer.update(z_world, z_self)`).
- `summary()` returns the **theta-cycle-AVERAGED** `z_world` -- the mean over the
  last `buffer_size` E1 ticks.
- The sole caller is `ree-v3/ree_core/agent.py:3382`:
  `self.theta_buffer.update(latent_state.z_world, latent_state.z_self)`.

There is no `z_goal`, no `action_proposal`, no `z_harm_s`/`z_harm_a`, no
gamma-sub-slot routing, no per-cycle joint-binding window, and no joint-read
interface anywhere in `ree_core` or `experiments` (repo-wide grep is empty).

So the substrate today can express exactly ONE of MECH-294's four streams
(`state_summary`, via the averaged `z_world`), in a **homogeneous, single-vintage,
content-averaged** form. It is structurally incapable of constructing the joint
multi-content packet MECH-294 is about. Any behavioural experiment "testing
MECH-294" on this substrate would measure a homogeneous-latent null, not the
joint-packet hypothesis -- the canonical vacuous-probe failure mode (cf. the
V3-EXQ-642 / MECH-353 "symbol of mechanism without functional input" lesson). The
readiness gate is correct to block it.

## 3. The four streams and their concrete REE sources

The substrate's job is to gather the four content streams from their distinct
upstream producers, route each into its own typed sub-slot, and bind them into one
per-cycle packet. The REE-v3 sources are all already implemented:

| MECH-294 stream    | REE-v3 source                                                              | Vintage signal (V_s key) |
|--------------------|----------------------------------------------------------------------------|--------------------------|
| `goal_latent`      | `GoalState.z_goal` (`agent.goal_state`, SD-012/SD-015/MECH-230)            | `z_goal`                 |
| `action_proposal`  | hippocampal CEM proposer first-step action-object: `trajectory.actions[:, 0, :]` from `HippocampalModule.propose_trajectories` (ARC-018) | (no V_s stream; see note below) |
| `risk_estimate`    | `z_harm_s` (sensory, SD-010) + `z_harm_a` (affective, SD-011) from `LatentState` | `z_harm_s`, `z_harm_a`   |
| `state_summary`    | `z_world` summary from the existing MECH-089 ThetaBuffer averaging path     | `z_world`                |

Notes on sourcing:

- **`goal_latent`.** Already V_s-gated at the E1 read site (`agent.py:3369-3378`
  routes `z_goal` through `vs_rollout_gate.gate_stream("z_goal", ...)`). The packet
  reuses the same per-stream V_s and the same snapshot-or-current discipline -- the
  packet does not invent a second gating policy; it consumes MECH-269b's.
- **`action_proposal`.** The CEM proposer emits K candidate trajectories. The
  packet binds the **first-step action-object** of the proposer's current best (or
  committed) candidate -- the proposal "on the table" this cycle. This is a control
  stream, not a sensory latent, so it has no `per_stream_vs` entry. Its "vintage"
  is the proposal's age in E3-heartbeat ticks (cheap to track on the
  HippocampalModule side; the packet records it as `action_proposal_age` rather than
  a V_s value). This asymmetry is deliberate and is one of the design forks in S9.
- **`risk_estimate`.** Two sub-components (sensory `z_harm_s`, affective `z_harm_a`)
  per SD-010/SD-011. They keep distinct sub-slots; the packet does NOT pre-collapse
  them to a scalar -- a downstream reader that wants total risk can reduce, but the
  joint structure must preserve the dual-stream distinction so the SD-011
  dissociation survives into the packet.
- **`state_summary`.** Sourced from the existing MECH-089 averaged `z_world`, so
  the parent mechanism is reused verbatim, not replaced.

## 4. Proposed substrate: `MultiContentThetaPacket` (sibling module)

**Decision: a sibling module, not an in-place ThetaBuffer rewrite.** The ThetaBuffer
is depended on by MECH-092 replay, MECH-122 consolidation
(`consolidation_summary`), and the SD-006/MECH-089 cross-rate E3 read. Rewriting it
risks those consumers and breaks the bit-identical-OFF guarantee. Instead add
`ree-v3/ree_core/latent/multi_content_theta_packet.py` with a
`MultiContentThetaPacket` class that COMPOSES the existing ThetaBuffer for its
`state_summary` slot and gathers the other three streams itself. MECH-089 stays
exactly as it is; MECH-294 is a strict additive layer on top.

### 4.1 The per-cycle binding window

A theta cycle is the interval between two E3 heartbeat ticks (the E3 rate is
`N_e3` env steps, MECH-089's existing definition). Within one such cycle, E1 fires
at the gamma rate multiple times. The packet:

1. **Opens** a binding window at each E3-heartbeat boundary (the cycle start).
2. **Accumulates** per-stream values into typed sub-slots during the window
   (each E1 tick pushes the current latents; the proposer pushes the current
   best/committed first-action when it refits).
3. **Seals** the packet at the next E3-heartbeat boundary, producing one
   immutable `ThetaPacket` for that cycle, which the proposer/E3 read as a joint
   object on the *next* cycle.

This makes the binding **phase-aligned**: every component bound into packet `P_t`
was observed within the same theta cycle `[t, t+1)`, and "co-bound in the same
cycle" is exactly the within-window membership the joint-binding claim requires.

### 4.2 Gamma-sub-slot routing

Each stream gets a fixed, typed sub-slot in the packet -- the substrate analogue of
distinct gamma frequencies routing distinct content (Colgin 2009, Lisman & Jensen
2013). Concretely the sealed `ThetaPacket` is a small dataclass:

```
@dataclass
class ThetaPacket:
    cycle_index: int
    goal_latent:       Optional[Tensor]   # [1, goal_dim]   or snapshot
    action_proposal:   Optional[Tensor]   # [1, action_object_dim]
    risk_sensory:      Optional[Tensor]   # [1, harm_dim]   (z_harm_s)
    risk_affective:    Optional[Tensor]   # [1, harm_dim]   (z_harm_a)
    state_summary:     Tensor             # [1, world_dim]  (MECH-089 averaged z_world)
    # per-component vintage metadata (Section 4.3)
    vintage: Dict[str, ThetaPacketVintage]
```

The sub-slots are **type-separated, not concatenated into one vector**. Keeping
them addressable by name is what makes the joint-read interface (S5) able to
condition action on goal-and-risk; a flat concat would lose the typing the claim
needs and would silently collapse the SD-011 dual-stream distinction.

### 4.3 Per-stream V_s vintaging (MECH-269 / 269b reuse)

For each stream `s` with a `per_stream_vs[s]` entry (`z_goal`, `z_harm_s`,
`z_harm_a`, `z_world`), the packet applies the **same snapshot-or-hold discipline**
MECH-269b already implements in `vs_rollout_gate`:

- If `V_s[s] >= snapshot_refresh_threshold` (default 0.5): the slot takes the
  **current** value and refreshes the stream's snapshot.
- If `V_s[s] < hold_threshold` (default 0.4): the slot takes the **held snapshot**
  (last-verified value), and the packet marks that component `stale` with its age.
- The 0.4-0.5 dead-band is the existing MECH-269b Schmitt hysteresis -- reuse it,
  do not invent a second one.

Each component records a `ThetaPacketVintage{is_current: bool, age_ticks: int,
v_s: float}`. `action_proposal` has no V_s entry; its vintage is
`age_ticks = proposal age in E3 ticks`, `v_s = None`. This is what makes the packet
a "stream-typed object whose components have potentially different temporal
vintages" (MECH-294 functional restatement) rather than a homogeneous current
latent -- and it is the substrate hook for MECH-294's **secondary** falsifiable
prediction (manipulating which streams are anchor-eligible changes which components
are current-vs-stale, and downstream consumers should respond differently than to a
homogeneous-latent null).

### 4.4 Wiring (agent.py)

- Build `self.multi_content_theta_packet` in `REEAgent.__init__` when
  `config.use_multi_content_theta_packet` is True; else `None`.
- In `sense()` / `_e1_tick`, immediately after the existing
  `self.theta_buffer.update(...)` call (`agent.py:3382`), also push the current
  per-stream latents into the packet's open window
  (`packet.observe(z_goal, z_harm_s, z_harm_a, per_stream_vs, ...)`).
- On the proposer side, when the CEM refits, push the current first-action
  (`packet.observe_action_proposal(trajectory.actions[:, 0, :])`).
- At each E3 heartbeat, seal the current packet and expose it via
  `agent.last_theta_packet` for the proposer/E3 to read on the next cycle.
- The `state_summary` slot is filled by calling the existing
  `theta_buffer.summary()` at seal time -- no duplication of the averaging logic.

## 5. Joint-read interface

The point of the packet is that a reader conditions on the co-binding. The
interface exposes both the typed components AND a small set of joint reductions so
consumers do not each re-implement the conditioning:

```
class ThetaPacket:
    def joint_context(self) -> Tensor
        # type-tagged concat of [goal_latent, action_proposal, risk_sensory,
        # risk_affective, state_summary], each prefixed with a learned/whatever
        # type embedding so the reader can tell streams apart. The ONE place a
        # flat vector is produced -- for a consumer that wants a single context
        # tensor (e.g. a bias head). Stale components substitute their snapshot.

    def action_conditioned_on(self, goal=True, risk=True) -> Tensor
        # returns the action_proposal slot annotated with the co-bound goal and
        # risk -- the literal "which action is on the table, read against the
        # goal and risk co-bound this cycle" operation. This is the joint read
        # the proposer/E3 uses.

    def risk_vector(self) -> Tensor          # max/concat over sensory+affective
    def is_component_stale(self, name) -> bool
```

Consumers in V3 that can read the packet without new training:

- **E3 commit gate / dACC adaptive control** -- read `joint_context()` as an
  additional, type-typed score-bias input (parallel to the existing
  lateral_pfc / ofc / mech295 chain). The packet is additive and bias-scale
  clamped, so it cannot dominate.
- **Hippocampal proposer** -- read `action_conditioned_on(goal, risk)` to bias the
  *next* cycle's candidate seeding toward goal-and-risk-consistent first actions.

In the **first** implementation pass the packet should be wired **read-only** (it
is constructed and exposed and logged, but its `joint_context` is composed into the
E3 bias chain behind a separate sub-flag), so the substrate-readiness validation
(S7) measures whether the packet CAN be built and is non-degenerate before any
behavioural-authority experiment depends on it. This mirrors how SD-039 / MECH-292
landed the payload substrate read-only before the behavioural consumer.

## 6. The Kay 2020 risk and how the substrate distinguishes joint-binding from alternation

**The risk (from the lit synthesis, the single load-bearing empirical challenge).**
Kay et al. 2020 (Cell) shows theta cycles carrying distinct content packets at the
~125 ms binding-window timescale, but the *demonstrated* scheme is **alternation
across cycles** (one content stream per cycle), not joint binding within one cycle.
Alternation is the **parsimonious** read: if you only ever decode one content axis
per cycle, you cannot tell a genuinely-joint packet from a one-stream-per-cycle
sequence that your single-axis analysis collapsed. Alternation, if it is the *only*
architecture present, **falsifies** MECH-294.

**Why the substrate must make this discriminable.** A substrate that simply emits a
four-slot packet every cycle does NOT settle the question -- you could fill those
four slots by round-robin (slot `i` carries real content only on cycle `i mod 4`,
held-snapshot otherwise) and it would look identical at the slot level. The
substrate must therefore distinguish two *operating regimes* and the experiment
must measure which one carries the downstream signal:

- **JOINT regime.** Every cycle's packet binds **all four streams' current
  (or V_s-held) values simultaneously**, and the joint-read
  `action_conditioned_on(goal, risk)` is computed from same-cycle co-membership.
- **ALTERNATION control.** A matched substrate variant where each cycle exposes
  **exactly one** stream's current value and holds the other three at their prior
  snapshots, cycling which stream is "live" round-robin. Same four slots, same
  total information bandwidth across four cycles -- but no within-cycle
  co-binding.

The discriminator is **whether the downstream consumer's behaviour depends on
within-cycle co-binding that the alternation control cannot provide**. Concretely:
the substrate exposes a `packet_binding_mode in {"joint", "alternation",
"shuffled"}` config so the experiment can hold *bandwidth and content identical*
and vary *only* the binding structure.

The shuffled control is the third, strongest, leg: **independent-content** -- each
slot is filled from a *different cycle's* value for that stream (a temporal
shuffle with matched marginal statistics), so the four components are real and
current-looking but were never co-observed. If `joint` and `shuffled` produce the
same downstream behaviour, the co-binding is inert and MECH-294 is not doing work
on this substrate (a substrate-ceiling finding, not necessarily a claim
falsification -- see S7 interpretation grid).

## 7. The discriminative validation experiment

A substrate-readiness diagnostic (claim-free, `claim_ids=[]`) -- it validates that
the substrate can build a non-degenerate joint packet and that the joint regime is
behaviourally separable from the matched alternation/shuffled controls. It does NOT
yet weight MECH-294 confidence; that is the behavioural successor gated on this
passing.

### 7.1 Arms (matched seeds, matched content, only binding-mode varies)

| Arm | `use_multi_content_theta_packet` | `packet_binding_mode` | Purpose |
|-----|----------------------------------|-----------------------|---------|
| ARM_0 OFF        | False | n/a          | bit-identical-OFF baseline (homogeneous-latent null) |
| ARM_1 JOINT      | True  | `joint`      | the MECH-294 hypothesis |
| ARM_2 ALTERNATION| True  | `alternation`| Kay-2020 parsimonious control (one stream live/cycle) |
| ARM_3 SHUFFLED   | True  | `shuffled`   | independent-content control (real but never co-observed) |

All arms share the **same seeds** (e.g. 42/43/44), the **same env**, the **same
content streams** (the four slots carry identical marginal values across arms -- the
controls differ only in *which cycle's* value lands in each slot and whether the
co-binding is real). This is the matched-seeds, matched-content discipline that
makes the binding-structure the single manipulated variable.

### 7.2 Pre-registered acceptance thresholds

Substrate non-degeneracy gates (must pass or the run self-routes
`substrate_not_ready_requeue`, protecting the claim from a vacuous result):

- **G0 packet completeness.** In ARM_1, >= 2/3 seeds produce sealed packets in
  which all four streams are populated (current or V_s-held) on >= 80% of cycles.
  A packet that is chronically missing `goal_latent` (e.g. goal pipeline inert) is
  not testing MECH-294 -- it routes to the goal-pipeline blocker, not here.
- **G1 vintage heterogeneity (the stream-typed-object check).** Across ARM_1
  cycles, the fraction of packets whose components have >= 2 distinct vintages
  (some current, some held) is > 0 on >= 2/3 seeds. If every component is always
  current, the V_s vintaging is inert and the MECH-294-secondary prediction is
  untestable -- a substrate-ceiling note, not a pass.

Discriminative gates (the actual readiness result):

- **C1 joint != alternation.** A pre-registered downstream readout (proposer
  first-action distribution, OR E3 committed-class distribution, OR a held-out
  goal-and-risk-consistency score) differs between ARM_1 and ARM_2 by more than the
  between-seed noise band (effect size pre-registered, e.g. total-variation distance
  of the committed-class distribution >= 0.10, exceeding the ARM_1-vs-ARM_1
  cross-seed baseline). This is the operational "within-cycle co-binding carries
  signal the one-stream-per-cycle scheme cannot".
- **C2 joint != shuffled.** Same readout differs between ARM_1 and ARM_3 by the
  same pre-registered margin. This is the stronger leg: the co-binding must matter
  *as co-binding*, not just as four-streams-present.

### 7.3 Interpretation grid (pre-registered)

| Outcome | Reading | Routing |
|---------|---------|---------|
| G0+G1 pass, C1 pass, C2 pass | Substrate constructs a non-degenerate joint packet AND the within-cycle co-binding is behaviourally load-bearing vs both controls. | PASS -> queue the MECH-294 behavioural-evidence successor; the substrate readiness gate is cleared. |
| G0+G1 pass, C1 pass, C2 FAIL | Joint beats alternation but ties shuffled: "four streams present" carries the signal, not their co-observation. | Substrate-ceiling-ish: MECH-294's *multi-content* part is supported, the *joint-binding* part is not yet isolated. Refine the readout to a genuinely conjunctive one (a readout that needs same-cycle goal x risk x action) before claiming joint binding. Do NOT promote MECH-294's joint clause. |
| G0+G1 pass, C1 FAIL | Joint indistinguishable from alternation. | This is the Kay-2020 parsimonious outcome surviving on REE's own substrate: the joint-packet hypothesis is not doing work here. Route to a `failure-autopsy` -- either the downstream consumer is not conditioning on co-binding (wiring) or the claim is over-specified (genuine). Either way the **claim's joint clause is not promotable** and the 2026-04-26 governance hold stands. |
| G0 or G1 FAIL | Packet degenerate (missing streams / single-vintage). | `substrate_not_ready_requeue` to the upstream blocker (goal pipeline for missing `z_goal`; V_s/MECH-269 wiring for single-vintage). Not a MECH-294 result. |

The C1-FAIL row is the substrate-side discriminator the 2026-04-26 governance hold
explicitly demanded ("a substrate-side falsification test that can discriminate
joint-packet from cross-cycle alternation"). This experiment IS that test.

## 8. Config, backward compatibility, MECH-094

- **Master flag:** `REEConfig.use_multi_content_theta_packet` (default `False`;
  wired through `REEConfig.from_dims`). OFF -> `agent.multi_content_theta_packet is
  None`, the `sense()`/proposer push sites are skipped, MECH-089 ThetaBuffer
  behaviour is byte-identical. This is the bit-identical-OFF guarantee every V3
  substrate carries.
- **Sub-flags:** `theta_packet_binding_mode` (`"joint"` default / `"alternation"`
  / `"shuffled"`); `theta_packet_compose_into_e3_bias` (default `False` -- the
  read-only-first discipline of S5); `theta_packet_snapshot_refresh_threshold`
  (0.5) and `theta_packet_hold_threshold` (0.4) reusing MECH-269b defaults;
  `theta_packet_bias_scale` (0.1, mirrors lateral_pfc/curiosity) for when the E3
  composition is enabled.
- **MECH-094.** The packet is built only on the waking `sense()` path. Every
  observe/seal method takes `simulation_mode` and is a no-op when True (a replay /
  DMN tick must not seal a waking packet). Same defensive pattern as MECH-313 /
  MECH-320 / MECH-341. The `state_summary` reuse inherits ThetaBuffer's existing
  consolidation gating untouched.
- **Phased training:** none required. The packet is pure gather/route/seal
  arithmetic + dataclass plumbing over already-trained latents; no new encoder
  head, no gradient flow. (If a future pass adds a *learned* type embedding or a
  trained joint-read head, that pass would need P0/P1/P2 -- out of scope here.)
- **Contracts** (the implementation pass would add
  `tests/contracts/test_multi_content_theta_packet.py`): C1 default-OFF no-op /
  bit-identical ThetaBuffer; C2 ON builds a 4-slot sealed packet at the E3 boundary;
  C3 V_s-held substitution fires when a stream's V_s drops below the hold threshold
  and the component is marked stale with a vintage age; C4 `joint` vs `alternation`
  vs `shuffled` produce structurally distinct packets from the same input stream
  (the substrate-side discriminability the experiment depends on); C5 MECH-094
  simulation_mode no-op; C6 `action_conditioned_on` returns the action slot
  annotated with the same-cycle goal+risk.

## 9. Open design forks (flag for the implementation session / governance)

1. **`action_proposal` vintage has no V_s.** The control stream is not a sensory
   latent, so it has no `per_stream_vs` entry. The memo proposes an
   E3-tick `age_ticks` proxy. Alternative: derive a proposal-confidence scalar
   from the CEM elite-score spread and treat it as a pseudo-V_s. The age proxy is
   simpler and sufficient for the readiness experiment; revisit if the behavioural
   successor needs proposal-vintage to be on the same scale as the sensory V_s.
2. **`risk_estimate` = `z_harm_s` + `z_harm_a` kept as two sub-slots vs collapsed.**
   Memo keeps them separate to preserve the SD-011 dissociation into the packet. A
   collapsed scalar-risk slot would be cheaper but would erase exactly the
   distinction SD-011 spent its evidence establishing. Keep separate.
3. **Read-only-first vs compose-into-E3-immediately.** Memo recommends read-only
   first (S5) so the readiness experiment is clean. The behavioural successor flips
   `theta_packet_compose_into_e3_bias` on. A session that wants one experiment could
   run both, but the two-step keeps the substrate-validation non-vacuous.
4. **Binding-window = E3 cycle vs a dedicated theta clock.** Memo reuses the E3
   heartbeat as the cycle boundary (MECH-089's existing definition). If a future
   claim needs theta and the E3 rate to dissociate, the packet would need its own
   clock -- out of scope; noted so it is not silently assumed away.

## 10. What this memo does and does not do

- **Does:** specify a sibling `MultiContentThetaPacket` substrate, its four-stream
  sourcing, gamma-sub-slot typing, per-cycle phase-aligned binding window, V_s
  per-stream vintaging (MECH-269/269b reuse), joint-read interface, the
  joint-vs-alternation-vs-shuffled regime distinction that resolves the Kay-2020
  falsifier, and a matched-seed pre-registered discriminative validation experiment
  with a full interpretation grid.
- **Does not:** edit `claims.yaml` (MECH-294 stays candidate / `v3_pending`; the
  2026-04-26 governance hold stands until the C1/C2 discriminative test passes),
  queue any experiment, or change substrate code. The `/implement-substrate` pass
  that picks this up would land the module behind the OFF-default master flag, then
  `/queue-experiment` the S7 readiness diagnostic; only its PASS (per the S7.3 grid)
  would clear the substrate-readiness gate that found MECH-294 `blocked_substrate`.

---

### References (existing lit, reused -- no new pull)

`evidence/literature/targeted_review_mech294_theta_burst_packet/` (7 entries):
Lisman & Jensen 2013 (theta-gamma neural code, substrate), Colgin et al. 2009
(gamma routes distinct content streams, substrate), Igarashi et al. 2014 (LEC-CA1
two-stream cross-region joint binding within a theta window -- closest direct
analogue), Wikenheiser & Redish 2015 (goal_latent is theta-cycle-resolved),
**Kay et al. 2020 (cross-cycle alternation -- the falsifier this design resolves)**,
Hasselmo 2005 (theta phase segregates two functional contents), Pfeiffer & Foster
2013 (joint start+goal+trajectory content, SWR regime). SYNTHESIS verdict:
SPARSE-BUT-NOT-FALSIFYING; the substrate is well-anchored, the four-stream
within-cycle joint-binding specialisation is untested in the wet literature, and
the within-cycle-vs-across-cycle question (Kay 2020) is the named promotion-blocker
-- which the S7 discriminative experiment is built to settle on REE's own substrate.
