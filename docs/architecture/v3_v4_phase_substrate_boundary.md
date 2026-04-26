---
nav_exclude: true
---

# V3/V4 Phase Substrate Boundary -- Architectural Commitment

**Registered:** 2026-04-26
**Status:** active architectural commitment for the V3 working-model phase
**Scope:** what stays v4-deferred, why, and the conditions under which a V3 promotion
revisit would be triggered
**Origin:** thought_intake_2026-04-09_verisimilitude_ethics.md (Apr 9 verisimilitude /
ephaptic / TCL formalisation) + 2026-04-26 V_s status review

---

## TL;DR

The V3 working-model uses a **synaptic approximation** of regional verisimilitude (V_s),
its temporal-depth integration (D_V), its routing realisation (MECH-271), and its
fast-broadcast invalidation (MECH-287). The full phase-channel substrate -- ARC-053
Temporal Coherence Loop, MECH-225 oscillatory cross-frequency multiplexing, MECH-226
TCL biophysical substrate (inferior olive + cerebellum + thalamus + cortex), MECH-228
ephaptic field-level coherence support, MECH-227 anaesthesia-collapse model, MECH-270
ephaptic substrate of V_s -- stays **v4-deferred**.

The architectural bet: the synaptic V3 form is **sufficient for V3 working-model
deliverables** (closed-loop agent with V_s invalidation runtime, D_V-aware rollout
selection, hypothesis-tag-as-routing). The V4 phase substrate **refines, not replaces**,
the V3 form. V3 → V4 is a substrate-richness upgrade, not a re-implementation.

This commitment is reversible -- see "When to revisit" below -- but is the working
default for closing out V3.

---

## What stays v4-deferred (the held cluster)

| ID | Title | Rationale for V4 deferral |
|---|---|---|
| **ARC-053** | Temporal Coherence Loop (distributed phase-alignment substrate) | Requires inferior olive + cerebellum + thalamic-pacing analogues with phase-locked timing primitives; the V3 substrate has no oscillator infrastructure |
| **ARC-054 V4 form** | D_V trajectory selection over phase-coherent V(t) | V3 form (synaptic EMA over V_s readout) is now landed -- see `dv_temporal_depth_v3_form.md`; the V4 form upgrades the V_s readout to a phase-aligned V(t) component |
| **ARC-055** | Explicit V(t)/D_V signal availability (cross-loop) | Requires full V(t) computation with phase-aligned content; V3 reads the synaptic V_s stand-in instead |
| **MECH-225** | Oscillatory cross-frequency multiplexing | Requires gamma/theta/beta/delta carriers and phase-of-firing routing; V3 has no oscillatory carriers |
| **MECH-226** | TCL biophysical substrate (IO + cerebellum + thalamus + cortex) | Direct substrate of ARC-053; same blocker |
| **MECH-227** | Anaesthesia-collapse model | Predictive only; no V3 dependency |
| **MECH-228** | Ephaptic field-level coherence support | The biophysical mechanism enforcing phase alignment; presupposes oscillatory substrate (MECH-225) |
| **MECH-270** | Ephaptic substrate of V_s | Same as MECH-228 specialised to V_s; V3 uses synaptic V_s readout, V4 will read from ephaptic field strength |
| **ARC-056** | Ethics-as-coherence (β_j · D_{V,j}) | Multi-agent extension; presupposes single-agent D_V (now landed at V3) and a multi-agent substrate (V4 social systems) |
| **INV-067/068/069** **V4-form readings** | Verisimilitude as full V(t), D_V over phase-coherent integration, self as phase-coherence trajectory | The V3 readings of these invariants are honoured by the V3 synaptic forms; the V4 readings require the phase substrate |

The V3 *implementation surfaces* of V_s / D_V / MECH-271 routing / MECH-287 broadcast
land as `instantiates: <V4 claim>` substrate without claiming the V4 substrate is
present. Governance treats them as compatible refinement substrates, not contradictions.

---

## What the V3 synaptic form covers (the bet)

| V4 capability | V3 synaptic stand-in | Sufficient for? |
|---|---|---|
| V(t) precision-weighted phase-aligned correspondence | MECH-269 per-region V_s scalar (per stream, per (scale, segment_id)) | V_s invalidation runtime, anchor-reset hysteresis, staleness accumulator, broadcast trigger |
| D_V temporal persistence of coupling | ARC-054 V3: rollout-horizon EMA over V_s readout | Hippocampal rollout evaluation; MECH-124 z_goal salience contest; freeze-recommit cycle damping |
| Phase-channel hypothesis tag (MECH-094 biophysical realisation) | MECH-271 V3: discrete routing table over (replay_kind, destination) pairs | Confabulation-vs-psychosis dissociation audit; consolidation gating; SD-033a / SD-035 destination wiring |
| Continuous ephaptic broadcast | MECH-287b (parallel session): continuous broadcast strength on top of MECH-287 binary trigger | Soft re-weighting path; gradual freeze release without oscillation |
| Self as coherence trajectory (D_self) | ARC-054 V3 restricted to `stream = z_self` | Single-agent coherence accounting; reuse of D_V infrastructure |
| Multi-agent ethics-as-coherence | Not in V3 | Deliberate V4 deferral (social systems) |

The architectural bet is that the working-model deliverables (closed-loop agent that
escapes catatonic-lock, computes commitment-aware D_V, routes consolidation correctly,
and supports MECH-094 audit) can be demonstrated with the synaptic forms, and that the
V4 phase substrate then improves robustness, biological plausibility, and clinical
predictive power *without changing the architectural commitments*.

---

## What this leaves out -- the imaginary-plane question

The V3 synaptic forms compute V_s, D_V, and routing over **real-valued scalar streams**.
The V4 phase substrate adds a **complex-valued / phase-coordinate** dimension. There is
a class of computations -- those involving relative phase relationships across streams
that propagate through phase-locked transduction -- that the synaptic form *cannot
approximate without explicit phase variables*. These include:

- **Cross-stream binding via phase coincidence** (Singer / Engel binding-by-synchrony).
  The synaptic substitute is destination-co-firing within an integration window; this
  works for low-cardinality binding (a few streams) but degrades combinatorially.
- **Trajectory representation as theta-sequenced phase code** (Foster / Wilson 2007).
  The synaptic substitute is sequential rollout step-indices; this loses the analogue
  position-within-cycle that biology uses to compress sequence into sub-second windows.
- **Imagination-vs-perception phase-channel separation** (the Apr 7 phase_segregation
  intake: top-down predictions invading the sensory phase channel = hallucination). The
  synaptic substitute is MECH-094 source-side flag + MECH-271 routing-side audit; this
  catches confabulation but cannot model the failure mode where the same content
  occupies the wrong phase channel.
- **Inferior olive timing-reference for action commitment**. The synaptic substitute is
  the discrete BetaGate release event; this works for binary commit/release but cannot
  model the smooth phase-locked timing that biology uses for sub-second motor
  coordination.

The bet is that **none of these are required for V3 working-model deliverables**. The
imagination-vs-perception question is the most architecturally important deferral; the
others are biological-fidelity refinements. See the discussion in the originating
session for the long-form argument.

---

## When to revisit (revocation conditions)

This commitment is reversible. Triggers that would force a V3 promotion of part of the
v4-held cluster:

1. **A V3 working-model failure mode that the synaptic forms demonstrably cannot
   represent.** Concrete example: if MECH-271 routing audit cannot distinguish a
   substrate-level confabulation from a tag-loss confabulation without phase-channel
   information, MECH-228 ephaptic gets promoted.
2. **An EXQ FAIL where the diagnostic narrows to "missing phase variable".** Distinct
   from "missing substrate" -- governance must be able to articulate *why* a synaptic
   approximation could not have produced the missing signal.
3. **Multi-agent V3 work attempted (not currently planned).** ARC-056 ethics-as-
   coherence is V4 because social systems are V4; if a V3 social experiment is forced,
   ARC-056 + ARC-054 multi-agent extension promotes.
4. **An external constraint** (clinical use case, third-party comparison) requires
   biological-substrate fidelity. This would be a goal-posts shift, not a substrate
   discovery, and should be explicitly framed as such.

Triggers that should *not* force promotion:

- "Ephaptic coupling is biologically real and the agent doesn't have it." This is true
  but is the entire point of the V3/V4 boundary. The promotion criterion is functional
  insufficiency, not biological completeness.
- "The Apr 9 intake formalises V(t) and we should implement it fully." The intake
  registered the claims; the V3 promotion of ARC-054 is the V3 reading of that
  formalisation. The V4 reading remains v4 by design.

---

## Governance hooks

- All v4-held claims in the table above carry `implementation_phase: v4` in claims.yaml.
  This produces `hold_pending_v3_substrate` recommendations from the governance
  pipeline, which is **incorrect labelling** for these specifically -- they are
  v4-by-design, not v4-by-prerequisite. Action: governance.sh should be taught to read
  this document and emit `held_v4_by_architectural_commitment` instead, distinguishing
  the two failure modes. Deferred to a separate governance-tooling session.
- The substrate_queue.json `held_v4` block should reference this document so the user-
  facing dashboard surfaces the architectural commitment, not just the held status.
  Deferred to next governance cycle.

---

## Cross-references

- **`dv_temporal_depth_v3_form.md`**: ARC-054 V3 promotion (the first v4-deferred claim
  to land in V3 form).
- **`mech_271_routing_v3_substrate_plan.md`**: V3 routing substrate (the second
  v4-deferred concept to land in V3 form).
- **`v_s_invalidation_runtime.md`**: V_s synaptic substrate, which the V3 forms read
  from.
- **`mech_269b_vs_rollout_gating.md`** (parallel session): symmetric V_s gating on
  E1/E2; same V3-synaptic-approximation pattern.
- **`evidence/planning/thought_intake_2026-04-09_verisimilitude_ethics.md`**: original
  V(t)/D_V/TCL formalisation that names the V4 substrate.
- **`evidence/planning/thought_intake_2026-04-07_phase_segregation_perception_imagination.md`**:
  the imagination-vs-perception phase-channel claim that motivates the most
  architecturally important V4 deferral discussed above.
