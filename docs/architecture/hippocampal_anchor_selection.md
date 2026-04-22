---
title: Hippocampal Anchor Selection (Regional Verisimilitude)
parent: Architecture
nav_order: 27
---

# Hippocampal Anchor Selection via Regional Verisimilitude

**Claim Type:** mechanism_hypothesis (candidate, V3-pending)
**Scope:** Anchor-state selection for hippocampal trajectory proposals issued between committed actions
**Depends On:** ARC-007, ARC-018, MECH-089 (theta-gamma nesting), MECH-092 (quiescent SWR replay), MECH-094 (hypothesis tag), SD-005 (z_self/z_world split), SD-010/SD-011 (harm stream separation)
**Status:** candidate
**Claim ID (reserved):** MECH-269
**Registration status:** NOT YET in `claims.yaml` — deferred pending release of active `implement-amygdala-analog` claim on that file (2026-04-21)
**Implementation phase:** V3

---

## The gap this closes

ARC-018 states that the hippocampus constructs counterfactual rollouts from "the current latent
state." ARC-007 states that path memory indexes experienced trajectories through latent space.
Neither document specifies **which slice of the current latent actually becomes the rollout
anchor**. The proposer is described as starting "from now" — but "now" is not a single point
in a distributed latent. It is a family of stream-local estimates (`z_world`, `z_self`,
`z_harm`, `z_goal`, ...) whose alignment with perception varies moment-to-moment.

Between committed actions — during the quiescent E3 heartbeat cycles that carry SWR-equivalent
replay (MECH-092) — the proposer is expected to generate useful candidate trajectories. If it
anchors on a low-verisimilitude region, the rollout carries a hidden lie forward: the starting
point is fiction, so the trajectory is fiction about fiction. If it refuses to anchor at all on
low-verisimilitude regions, the agent becomes incapable of probing the very territory where
its model is weakest — exactly the territory that most needs exploration.

MECH-269 supplies the missing selection mechanism and splits proposals into two mechanistically
distinct kinds: **anchored** and **probed**.

---

## The mechanism

### 1. Regional verisimilitude as a per-stream quantity

Verisimilitude is the alignment between E1/E2 predicted latent and the actually realized
latent, measured separately per stream. For each stream `s ∈ {world, self, harm, goal, ...}`,
the proposer has access to a running alignment score:

```
V_s(t) = align(ẑ_s(t | t-Δ), z_s(t))
```

where `ẑ_s(t | t-Δ)` is the prediction issued Δ steps ago for stream `s`, and `z_s(t)` is the
stream's current realized value. Concretely this can be instantiated as a short-window EMA of
the cosine similarity (or negative prediction error) per stream. MECH-098's reafference
cancellation feeds `V_world` specifically; the other streams use their own prediction/realization
comparison.

### 2. Anchor eligibility

A stream is **anchor-eligible** at time `t` if `V_s(t) ≥ θ_anchor(s)`. The proposer constructs
its rollout starting-state by composing only the anchor-eligible slice of the current latent.
Misaligned streams are held at their last-verified snapshot (an "anchor carryover") rather than
allowed to contaminate the rollout. This gives a principled per-stream construction of "now."

### 3. Probe mode (the exploration escape valve)

A pure anchor-eligibility gate would suppress proposals in the very regions the agent needs to
understand. The **probe channel** inverts the gate for a minority of proposals:

- A rollout is issued **as a probe** when it is explicitly seeded from a low-verisimilitude
  region (or from a hybrid where one stream is a low-V probe seed and the others are anchored).
- Probes carry a strengthened hypothesis tag (MECH-094) — they are marked as *more* fictional
  than anchored rollouts, not less. Their write-gate downstream is tighter; their role is
  information acquisition, not viability mapping.
- Probe candidates come from curiosity / novelty signals (e.g. stream-local prediction-error
  spikes) rather than from verisimilitude. In effect: "I cannot currently model this region;
  deliberately simulate into it to find out what it contains."

Anchored proposals update the viability map (ARC-018). Probe proposals **do not** update the
viability map until a subsequent realized trajectory validates them; they update curiosity /
epistemic-coverage structures instead.

### 4. Anchor/probe ratio under the heartbeat

The ratio between anchored and probe proposals is itself modulated by the control-plane
heartbeat (ARC-023) and by global precision / mode. High-harm / high-commitment contexts
push the mixture toward anchored-only (probe is cognitively expensive and can surface
intrusive simulation — see MECH-094 failure modes). Low-threat / high-drive contexts widen
the probe fraction. This falls out naturally from existing dACC / SalienceCoordinator gating
and does not need a new controller.

---

## Why regional, not global, verisimilitude

A global "overall model trust" scalar cannot do this job, for two reasons:

1. **Dissociable streams.** After SD-010/SD-011, `z_world` and `z_harm_s` can have very
   different alignment quality at the same moment (e.g. novel terrain is a `z_world` prediction
   failure but says nothing about `z_harm` tracking). Collapsing them wastes the decomposition
   the substrate is built to provide.
2. **Partial anchoring is useful.** In practice the proposer wants to roll forward from "current
   `z_self` + current `z_harm` + carried-forward `z_world`" when the world stream is temporarily
   unreliable but the agent's own state and affective load are well-tracked. A global gate
   would force all-or-nothing anchoring.

This is the same logic that made per-claim `evidence_direction` necessary (see
REE_assembly/CLAUDE.md): one verdict for a multi-part measurement is lossy.

---

## Relationship to existing claims

| Existing claim | Relationship |
|----------------|--------------|
| **ARC-018** (hippocampal rollouts / viability mapping) | MECH-269 specifies *how the starting state is chosen* for the rollouts ARC-018 describes. |
| **MECH-092** (SWR-equivalent replay in E3 quiescence) | Quiescent replay runs on anchored trajectories under MECH-269; probes do not enter the viability map via replay. |
| **MECH-094** (hypothesis tag as categorical write gate) | Probe proposals carry a strengthened tag; tag loss on a probe is the candidate mechanism for confabulatory planning, consistent with existing confabulation framing. |
| **MECH-098** (reafference cancellation) | Provides the per-step input to `V_world` specifically. |
| **MECH-089** (theta-gamma nesting) | The per-cycle "snapshot" the proposer anchors on is the theta-cycle-averaged summary, not the instantaneous latent. Regional verisimilitude is computed on these summaries. |
| **SD-005** (z_self / z_world split) | Precondition: MECH-269 is only meaningful once streams are separated. |
| **SD-010 / SD-011** (harm stream separation) | Same — gives `z_harm_s` its own V. |

---

## Predicted observables (V3 scope)

A V3 experiment validating MECH-269 would measure:

1. **Anchor-eligibility correctness:** the proposer should refuse to anchor on streams whose
   subsequent realized alignment is below `θ_anchor`, and rollouts so-anchored should produce
   smaller prediction-vs-outcome gaps than rollouts that anchor indiscriminately.
2. **Probe yield:** probe-tagged rollouts should preferentially target high-PE regions and
   should not populate the viability map until validated by realized experience.
3. **Streamwise dissociation:** the agent should be able to plan under partial-anchor conditions
   (one stream unreliable) and should fail gracefully — not catastrophically — as compared to
   a no-anchor-selection baseline, which should confabulate forward from corrupted starts.
4. **Heartbeat modulation of anchor/probe ratio:** manipulating salience / harm load should
   shift the observed mixture, without re-training.

Candidate experiment name (not yet queued): **v3_exq_NNN_mech269_anchor_probe_dissociation.py**.
Requires substrate hooks for per-stream V_s logging in `HippocampalModule.propose_trajectories`
and an anchor/probe label field on emitted candidate trajectories.

---

## Open design questions

1. **Threshold setting.** `θ_anchor(s)` per stream — hand-tuned, learned, or derived from the
   same precision signal that drives MECH-098 and dynamic-precision weighting (ARC-016)? First
   pass: tie it to a running quantile of the stream's own prediction-error distribution, so it
   is intrinsically adaptive.
2. **Carryover decay.** How long can an anchored stream "carry over" its last-verified snapshot
   before it itself becomes untrustworthy? Probably governed by stream-local forgetting rates
   already implied by MECH-089's theta-cycle horizon.
3. **Probe quota.** Is the probe fraction a hard budget per heartbeat window, or purely
   signal-driven? Budget is easier to implement and audit; signal-driven is more biologically
   plausible. Default to budget for V3 and revisit.
4. **Interaction with post-commit vs pre-commit channels** (the MECH-094 split). Probes are
   intrinsically pre-commit-like (rehearsal under tag); this may simplify rather than
   complicate the tag accounting.
5. **Failure mode to watch for.** If probe-tagged rollouts leak into the viability map because
   of tag erosion, the map becomes populated with fictional affordances. This is the
   architectural signature of confabulated planning and should be surfaced as a diagnostic
   counter, not just trusted to not happen.

---

## Biological routing of anchored vs probe replay

The anchor/probe distinction is not purely functional. It has a candidate physical substrate in
the known fan-out of ephaptically-coordinated hippocampal replay.

**Coordination substrate.** In CA1 and CA3, pyramidal-layer cell-body density is high enough
that the local field generated by the firing population re-modulates that population's own
spiking. During sharp-wave ripples this ephaptic field effect is the dominant synchronising
mechanism — tighter than synaptic transmission alone can produce (Anastassiou & Koch 2011;
Jefferys; Buzsáki on SWRs). MECH-269's per-stream verisimilitude readout is, in this framing,
plausibly implemented as stream-local field coherence: streams whose predictions align with
realized values produce coherent ensembles whose fields constructively reinforce; misaligned
streams produce incoherent fields. "Anchor-eligible" reduces to "field-coherent at read time."

**Fan-out targets.** Ephaptically-synchronised CA1/CA3 pyramidal output projects to a fixed set
of downstream sites, and these map one-to-one onto REE modules currently in place or under
construction:

| Biological projection | REE module |
|---|---|
| Subiculum → entorhinal deep layers → neocortex | E1 world-model consolidation writes |
| Medial/lateral PFC (direct from ventral CA1) | **SD-033a lateral-PFC analog** (MECH-267 mode-conditioning consumer) |
| Basolateral amygdala (ventral CA1 → BLA) | **BLA analog** (under active implementation 2026-04-21) |
| Nucleus accumbens / ventral striatum | E3 commitment / viability evaluation |
| Mammillary bodies via fornix (Papez) | flagged for investigation (see `project_papez_circuit_investigation`); not yet a module |

**Routing hypothesis.** The anchor/probe distinction predicts *different downstream
destinations*, not a shared destination with a flag attached:

- **Anchored replay** (high regional verisimilitude, trusted starting state) preferentially
  writes to **subiculum → EC → neocortex** and **SD-033a lateral PFC**. These are the
  destinations that update stored world structure and the viability map (ARC-018). Writing
  here commits the replayed content to long-term use.
- **Probe replay** (low-V seed, strengthened MECH-094 hypothesis tag) preferentially engages
  **BLA** (affective tagging without consolidation) and **NAc** curiosity/novelty circuits.
  These destinations do not update the viability map until a subsequently realized
  trajectory validates the probe.

Under this framing, MECH-094 (the hypothesis tag) is not an undifferentiated "this is
simulated" flag riding on top of otherwise identical replay. It is instantiated as a
*routing difference* — probes reach a different subset of downstream consumers. Tag loss
(confabulatory planning, PTSD-adjacent phenomenology) then has a specific biological
signature: probe content reaching consolidation destinations it should not reach
(EC/neocortex/lateral PFC). This is an auditable diagnostic, not just a hypothesis
about internal state.

**Why this matters for substrate implementation.** The MECH-269 claim originally read as a
purely computational gate inside `HippocampalModule.propose_trajectories`. The biological
routing hypothesis says the gate should instead be realized as *which downstream consumers
receive the replay output*. In V3 substrate terms: anchored rollouts publish to the channels
consumed by E1 consolidation, SD-033a lateral PFC, and the viability-map writer; probe
rollouts publish to the channels consumed by BLA (affective tagging) and the
curiosity/novelty scaffolding. Consumers remain responsible for whether they read — the gate
is at *routing*, not at a single source-side boolean.

**Separate-claim candidates implied by this section.** Two further MECH entries are implied
and should be registered alongside MECH-269 rather than folded into it:

1. **MECH-270 (candidate):** ephaptic field coherence as the physical substrate for per-stream
   verisimilitude readout. Keeps the function/substrate distinction clean — same failure
   mode as SD-003 and SD-010/011 if we conflate them.
2. **MECH-271 (candidate):** hypothesis-tag realization as differential downstream routing
   rather than source-side flag. Anchored-to-consolidation vs probe-to-curiosity is the
   observable signature.

These are noted here but not drafted as separate docs this turn.

---

## State-gating: sleep vs waking informational needs

The routing architecture of MECH-271 is silent on brain state. A conversation revision
(2026-04-21) adds the commitment that the routing itself is state-gated, because sleep and
waking serve distinct informational needs and therefore exploit the anchor/probe split
differently.

**Waking regime.** The anchor channel dominates. The hippocampus is being asked to support
decisions — give me rollouts from where I actually am to where I might go, and do it with
high fidelity to the current world state. Probe events happen (DMN-style micro-quiescence,
MECH-092) but they are minority events under a strong hypothesis tag (MECH-094) that prevents
their content from writing to commitment-relevant consumers. The anchored / probe balance
tips toward anchored.

**Sleep regime.** The probe channel has the floor. The computational work changes: it is no
longer "make this decision" but "revise the schema that decisions run against." That is
full-Bayesian restructuring — testing which action-outcome attributions held up across
episodes, creating new buckets for experiences that did not fit existing schemas, revising
causal graphs where the data has accumulated evidence for or against prior attributions.
Probe content is recruited heavily because novel combinations need to be tested; the
hypothesis tag remains on to preserve the distinction between tested-and-accepted
(consolidation-routed) and tested-but-not-committed (remains in repertoire).

Tang et al. 2017 offer the empirical hint: awake and sleep SWRs differ in their cortical
reactivation quality. Our architectural reading is that the difference is not incidental —
it reflects the functional regime switch between decision-support (awake, anchor-dominant)
and schema-revision (sleep, probe-dominant Bayesian work).

**Registered as MECH-272.** State-gated routing. Waking = anchor-dominant fan-out bias;
sleep = probe-dominant fan-out with Bayesian restructuring of the schema repertoire.
Falsifiable (primary): V3 experiments that compare replay-to-consumer routing during wake
vs simulated-sleep phases should show the dominance shift. Falsifiable (secondary): under
state-gating loss (e.g., REM-like protocols run in waking state), routing should lose the
regime-appropriate bias.

---

## Sleep-dependent self-model aggregation

The self-model has a waking half and a sleep half. The waking half is SD-003: E2's
counterfactual causal signature `E2(z_t, a_actual) − E2(z_t, a_cf)`, attributing the
discrepancy between predicted and actual outcome to the agent's own action. This is
probabilistic and single-episode. It gives us "in this episode, this action looks
self-initiated with probability p."

The sleep half is the aggregation that turns many single-episode attributions into a stable
self-model. Single-episode attribution misses:

1. **Delayed consequences** where an action-outcome link spans more episodes than a single
   waking rollout can encompass.
2. **Failed counterfactuals** where the counterfactual action would have produced the same
   outcome — the action felt voluntary but was not actually causally efficacious.
3. **Systematic attribution biases** that a single episode cannot distinguish from noise but
   aggregate evidence across episodes can detect and correct.

Full-Bayesian aggregation of SD-003 outputs during sleep, routed by the anchored channel to
E1 consolidation (world model revision) and to SD-033a (viability-map revision of which
actions the agent can credit to itself), is how REE builds a stable sense of self. Without
it, SD-003 gives the agent only an episode-local causal signature — not a durable self.

**Registered as MECH-273.** Sleep-dependent aggregation of single-episode SD-003 self-
attributions into a stable self-model. Falsifiable (primary): ablating the sleep-phase
aggregation step should leave single-episode self-attribution intact but degrade stability
of self-attribution across episodes — concretely, the agent should be less able to correct
previously-held spurious self-attributions when post-hoc evidence accumulates against them.
Falsifiable (secondary): the pattern should generalise — any attribution whose stable form
requires multi-episode Bayesian revision should show the same sleep-dependence.

INV-049 (the mathematical necessity of offline phases for model-building agents) sits
directly under this claim. This is the specific content offline phases are doing for the
self-model case.

---

## Other-attribution sleep dependence (V4-reserved)

The same architectural pattern extends to other-attribution when V4 adds it. V4's fast
empathy system (ARC-010, MECH-217 if wired) produces single-episode attributions of
other-agent action-outcome links: "agent j did action a, which looks causally responsible
for outcome o." By the same argument as MECH-273, these single-episode attributions need
sleep-phase Bayesian aggregation before they stabilise into a model of agent j's
dispositions and causal powers. Without it, V4's other-model is episode-local — which is
not what a stable theory of other minds requires.

**Registered as MECH-274, flagged V4.** The extension is architecturally parallel to
MECH-273 but operates on other-agent attributions rather than self-attributions. Not for
V3 implementation; flagged here to reserve the mechanism and prevent V4 from rediscovering
it independently.

---

## Anchor reset criteria (V3-EXQ-471 motivated extension, 2026-04-22)

The original MECH-269 specification gave per-stream verisimilitude a role in *initial*
anchor selection: which slice of the current latent is eligible to seed a rollout at the
moment the proposer fires. It did not commit to a *reset* criterion — under what
conditions an anchor that was valid at one heartbeat becomes invalid and must be
discarded, even if no new commit has occurred to obviously reset state.

V3-EXQ-471 forced this question. The trace (full discussion in
[psychiatric_failure_modes.md](psychiatric_failure_modes.md) "Catatonia, Subtype II")
shows the proposer locked onto an anchor formed at t=0 (the moment of a single hazard
contact) and continuing to issue rollouts from that anchor for 200 steps, despite 190
steps of subsequent quiet during which the world had clearly moved on. Mode stayed
`avoid`, action stayed locked, position stayed at `[2,1]`, energy went to zero — and the
proposer never reconsidered the anchor.

This is a real failure mode that the per-stream verisimilitude gate does not catch on
its own. `V_world` was probably perfectly fine at t=190 (predictions matched
realizations — both predicted and realized "still nothing happening"). The problem was
not that the anchor's streams had become unreliable; it was that the anchor was
*temporally stale* — it had been formed under conditions (`z_harm_a` = 0.82, hazard
adjacent) that no longer held by t=50, but nothing in the proposer noticed.

### What the reset criterion must commit to

Anchor reset is required when **the regulatory state of the streams the anchor was
composed from has materially changed**, even when those streams' verisimilitude remains
intact. Concretely:

1. **Decay-driven reset.** If a stream that was high-magnitude at anchor formation has
   decayed (per SD-036 GABAergic decay regulator) below a freshness threshold by anchor
   read time, the anchor for that stream is no longer trustworthy as a representation
   of the *current* mode-relevant state. The anchor was "I am in a high-harm context,
   plan accordingly"; the current state is "I am in a low-harm context"; the rollouts
   issued under the stale anchor are stale.

2. **Mode-context reset.** Anchors are formed under a particular operating mode
   (SD-032a `current_mode`). When the SalienceCoordinator's `mode_switch_trigger`
   fires, anchors composed under the previous mode should be evicted from the
   eligibility pool — not merely augmented with new ones. EXQ-471's pathology is
   precisely that no mode switch ever fired, so this criterion is necessary but not
   sufficient (the agent also needs the prior criterion).

3. **Time-since-formation cap.** A purely temporal cap (anchors older than N
   heartbeat cycles must be re-validated against current realization) is a defensive
   backstop against staleness that the regulatory-state criterion misses. Initial
   value: re-validate after ~10 theta cycles (~MECH-089 timescale) of being held
   without commit-driven update.

### Interaction with SD-036 GABAergic decay

The anchor reset criterion is the **read-side mirror of SD-036's write-side decay**.
SD-036 decays the streams; the reset criterion ensures the proposer notices that the
decay has happened. Without the reset criterion, SD-036 alone is insufficient: the
streams could decay back to baseline while the proposer continued to issue rollouts
from an anchor formed when they were high.

Architecturally this means:

```
SD-036 (regulator layer):  decays z_harm, z_beta toward baseline
        |
        v
MECH-269 reset criterion:  detects stream decay relative to anchor formation state
        |
        v
Anchor pool eviction:      stale anchors removed; proposer re-anchors on current state
        |
        v
Mode arbitration:           with current-state anchor, mode flip becomes possible
```

The chain is what unlocks the EXQ-471 pathology. SD-036 alone unlocks the streams but
not the proposer; reset criterion alone has nothing to react to without decay; mode
arbitration alone has nothing to switch on without a current-state anchor to evaluate.
All three are required and they are mechanistically coupled.

### What this implies for the design

The original design treated `V_s(t) ≥ θ_anchor(s)` as the only gate on anchor
eligibility. The reset criterion adds a second gate:

```
anchor_eligible(s, t) =
    (V_s(t) >= theta_anchor(s))                           # original verisimilitude gate
    AND
    (regulatory_state_drift(s, t, t_formation) < theta_drift)   # NEW reset gate
    AND
    (mode_at_formation == current_mode)                   # NEW mode-context gate
    AND
    (t - t_formation < max_anchor_age)                    # NEW temporal backstop
```

`regulatory_state_drift(s, t, t_formation)` is a per-stream measure of how much the
stream's value has changed between anchor formation and current read, normalized by
its plausible decay over that interval (so that "expected decay" is not flagged as
drift, only "more decay than the regulator would have produced" or "decay despite
formation conditions persisting"). The exact form is an open design question; first
pass is `|z_s(t) - z_s(t_formation)| / expected_drift(t - t_formation, tau_s)`.

### Predicted observable

A V3 experiment validating the anchor reset criterion would re-run V3-EXQ-471 with
SD-036 enabled and the reset criterion enabled. Predicted trace at seed 0 ep 0:

- t=0: hazard contact, `z_harm_norm` jumps to ~0.82, anchor formed at this state
- t=10–30: harm input ceases, `z_harm_norm` decays under SD-036
- t=~30: `z_harm_norm` has decayed below freshness threshold relative to anchor
  formation; reset criterion fires; anchor evicted
- t=~30+: proposer re-anchors on current low-harm state; rollouts now consider
  goal-seeking trajectories
- t=~40–50: mode flip from `avoid` to a goal-seeking mode; agent resumes navigation
- t=~50+: episode proceeds normally

Without the reset criterion, SD-036 alone is predicted to leave the agent in a
strange intermediate state — unlocked streams but stale anchors — possibly producing
*intermittent* or *delayed* recovery rather than the clean ~t=50 flip.

### Open design question

What happens during sleep-mode replay (MECH-272)? Sleep-mode probe-dominant routing
deliberately uses anchors that may be temporally stale or counterfactual. The reset
criterion as specified would suppress sleep-mode probe replay, which is wrong. The
likely resolution: the reset criterion applies to **anchored** proposals only;
**probe** proposals are explicitly exempt because their job is to seed from
non-current states. This preserves sleep-mode Bayesian restructuring (MECH-272)
while preventing waking-mode anchor staleness. This may need its own MECH ID if the
anchor/probe distinction in reset behaviour proves architecturally substantive.

---

## Status log

- **2026-04-21** — Design doc written. Claim ID **MECH-269** reserved but not yet in
  `claims.yaml`; registration deferred pending release of concurrent active claim on the
  registry file. Discussion origin: user-initiated exploratory question about anchor selection
  for inter-commit hippocampal proposals, linking verisimilitude to anchor eligibility and
  proposing the anchor/probe split as the answer to the exploration-suppression objection.
- **2026-04-21** (same session) — Biological routing section appended. Ephaptic coupling
  flagged as candidate substrate for regional verisimilitude readout; anchored-vs-probe
  distinction recast as a routing hypothesis into known hippocampal fan-out targets, mapped
  onto existing/active REE modules (E1 consolidation, SD-033a lateral PFC, BLA analog, NAc,
  Papez). MECH-270 and MECH-271 noted as implied separate claims.
- **2026-04-21** (later) — MECH-269/270/271 registered in `claims.yaml`. Targeted lit-pulls
  landed (Jadhav 2016, Girardeau 2017, Anastassiou 2011, Pfeiffer & Foster 2013, Dragoi &
  Tonegawa 2011/2013, English et al 2014, Tang et al 2017, Ólafsdóttir 2018, Buzsáki 2015,
  Foster 2017). MECH-269 literature_confidence 0.852; MECH-271 0.795; MECH-270 0.750.
- **2026-04-21** (later still) — State-gating / sleep-waking / self-model aggregation /
  V4 other-attribution sections added. MECH-272, MECH-273, MECH-274 registered. Discussion
  origin: user observation that sleep and waking serve distinct informational needs (sleep =
  Bayesian schema revision, waking = decision-support using existing schemas) and that the
  self-model has a waking half (SD-003) and a sleep half (aggregation of single-episode
  attributions).
- **2026-04-22** — Anchor reset criteria section added, motivated by V3-EXQ-471 catatonic
  lock trace (200-step `avoid`-mode lock with anchor stuck at t=0 harm event despite 190
  steps of subsequent quiet). Reset criterion specified as the read-side mirror of SD-036's
  write-side decay; introduces three additional anchor-eligibility gates (regulatory drift,
  mode-context, temporal cap). Identified as architecturally coupled with SD-036 (registered
  same session) — neither alone resolves the EXQ-471 pathology. Sleep-mode probe exemption
  flagged as open design question, possible candidate for new MECH if substantive.
