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
