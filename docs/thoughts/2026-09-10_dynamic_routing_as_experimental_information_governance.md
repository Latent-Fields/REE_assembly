# Dynamic routing as experimental information governance

**Date:** 2026-09-10  
**Status:** thought / assay-generative note; not a claim registration, queue mutation, or `ree_core` implementation instruction  
**Parent:** `2026-09-10_dynamic_information_governance_propagating_causal_privilege.md`  
**Related:** `2026-09-07_mutual_legibility_implementation_assays.md`; `2026-09-09_hippocampal_replay_interface_maintenance_supplement.md`; `../../evidence/planning/hippocampal_campaign_assay_specifications_20260910.md`

---

## 1. The next question

If dynamic information governance is real, then the immediate task is not to build a wave generator into REE. It is to determine whether REE already exhibits, or benefits from, a **time-varying routing geometry** in which otherwise-intact information gains and loses causal access to downstream systems.

The key distinction is now:

- **representation:** what information exists in a subsystem;
- **transformation:** whether another subsystem could in principle decode or use that representation;
- **routing / causal privilege:** whether that information is presently permitted to influence the next state of the organism.

A static bridge asks whether sender state `x` can be mapped into a receiver-compatible state `y`.

A dynamic-routing account asks an additional question:

> At which moments, and under which organism-level state, does the sender's information become causally effective at the receiver and then propagate onward?

This introduces time and sequence into mutual legibility. Two systems can be mutually interpretable yet fail to communicate because their periods of effective receptivity do not coincide. Conversely, a weak signal can become behaviourally dominant if routing successively opens the appropriate downstream consumers.

The candidate mechanism should therefore be treated first as a **diagnostic hypothesis about effective connectivity**, not as a new semantic module.

---

## 2. Minimal formal object

Let `h_i(t)` denote the state of subsystem `i`, and let `W_ij` denote whatever transformation is already available from subsystem `i` to subsystem `j`.

Introduce a routing state `r(t)` that modulates effective transmission:

```text
m_i->j(t) = g_ij(r(t), c(t)) * W_ij h_i(t)
```

where `c(t)` may include existing control-plane quantities such as precision, gain, arousal, mode, veto, or commitment state.

The important object is `g_ij`: a changing gain over directed interfaces.

The routing state need not initially obey a physical wave equation. A graph-propagating low-rank gain vector, recurrent gating process, or small dynamical field is enough to test the computational proposition.

The hypothesis becomes stronger if `r(t)` is partly endogenous:

```text
r(t+1) = F(r(t), aggregate_activity(t), control_state(t), context(t))
```

That permits circular causality:

```text
local subsystem states
        ↓
organising routing state
        ↓
changed effective connectivity
        ↓
changed subsystem states / action
        ↓
updated routing state
```

This is the computational analogue worth testing before making any claim about electrophysiological waves or ephaptic coupling.

---

## 3. The strongest immediate prediction

The anaesthesia-inspired prediction is not simply that reducing routing reduces information flow.

It is more discriminating:

> A system can preserve, or even increase, total intermodule information transfer while losing selective directional tuning, motif diversity, and behaviourally appropriate causal sequencing.

Therefore the useful comparison is not `more information` versus `less information`.

It is:

```text
high-volume, weakly governed transfer
vs
selective, directionally organised transfer
```

If the latter produces better integrated behaviour at matched or lower total information volume, that is evidence that routing organisation matters independently of raw channel capacity.

This also creates a direct falsifier. If flattened, shuffled, or temporally scrambled routing performs as well as structured routing once activation and message volume are matched, a dedicated dynamic information-governance layer is unnecessary.

---

## 4. Start with observation, not intervention

The first experiment should ask whether the existing organism already contains signatures of dynamic routing without adding any new mechanism.

Record aligned trajectories from interfaces already identified in the mutual-legibility programme, using only sources that retain the relevant content. In the current V3 state this means **not** treating trained `z_world` as an admissible information-preserving sender after V3-EXQ-1010; begin with `rawfield25` and use `ws250_pca32` as a replication source where appropriate.

Candidate directed interfaces include:

- richer world observation / `rawfield25` -> decision-facing state;
- world representation -> E1;
- world representation -> E2;
- E1 -> E2/action consequence consumer where a real causal path exists;
- hippocampal candidate/proposal state -> E3 selection;
- replay state -> E1 or other genuine sleep consumer;
- relevant control-plane state -> interface gain or consumer sensitivity;
- decision-facing state -> committed action.

For each directed pair, estimate time-resolved predictive influence using transfer entropy, conditional mutual information, directed information, Granger-like predictive gain, or another estimator appropriate to the recorded variables. No single estimator should be treated as the phenomenon itself.

The important outputs are:

1. **directionality** — does influence preferentially run along specific paths at specific times?
2. **stability** — do similar contexts produce similar routing trajectories?
3. **motif repertoire** — does successful behaviour contain a richer set of repeated directed-flow motifs than failed or degraded behaviour?
4. **alignment** — do discovered flow directions line up with known causal producer -> consumer paths?
5. **behavioural coupling** — do motif transitions predict commitment, successful foraging, harm avoidance, or other downstream behaviour beyond static representation quality?

A positive observational result would justify perturbation. A null result should sharply reduce priority for a new routing mechanism.

---

## 5. Routing motifs rather than one global wave

The travelling-wave analogy should not force REE into one global sweep.

The more general hypothesis is that cognition may use a **repertoire of recurrent routing motifs**. Examples might include:

```text
perception -> world model -> prediction -> valuation -> commitment
```

or

```text
memory -> counterfactual reconstruction -> harm/benefit evaluation -> veto
```

or during offline processing:

```text
hippocampal replay -> slow model -> schema/interface update
```

The biological analogue may be spatial propagation across cortex. In REE, where the architecture is a graph rather than a cortical sheet, the corresponding object may be a **propagating pattern over directed module interfaces**.

The wave metaphor is retained only if the discovered routing state has meaningful propagation: adjacent or functionally coupled interfaces become permissive in an ordered sequence with a characteristic direction, speed, persistence, and repertoire.

If what emerges is instead sparse event-driven switching, that is still compatible with dynamic information governance but not with a literal wave analogue.

---

## 6. Anaesthesia-like lesions

The strongest causal assay is to impair routing while preserving as much local computation and total information exchange as possible.

Candidate lesions:

### A. Gain flattening

Replace the endogenous `g_ij(t)` with a constant mean gain while preserving total transmitted magnitude.

Question: does behaviour worsen because causal selectivity is lost despite comparable transfer volume?

### B. Direction shuffle

Preserve the same gain distribution and temporal autocorrelation but permute which directed edges receive privilege.

Question: does the identity of the privileged path matter?

### C. Phase / timing shuffle

Preserve edge-specific gain trajectories but destroy their relative temporal ordering.

Question: is sequencing itself load-bearing?

### D. Propagation break

Allow local routing state but remove the dependency that permits privilege to propagate to neighbouring or downstream interfaces.

Question: are isolated gates sufficient, or is ordered propagation necessary?

### E. Stereotyped slow-mode lock

Constrain routing to a small number of slow, high-amplitude global modes.

This is the most direct computational analogue of the possibility that anaesthesia does not abolish global dynamics but collapses flexible multiplexed routing into stereotyped modes.

### F. Top-down removal

Retain feed-forward routing but remove higher-order feedback contributions to the routing field.

Question: does the system still propagate information but lose context-sensitive or goal-sensitive organisation?

Each lesion should be budget matched wherever possible for message count, activation norm, mean gain, and local endpoint competence.

The desired anaesthesia-like phenotype is:

```text
local representations remain informative
+ local modules remain competent
+ total exchange is preserved or increased
+ directional selectivity / motif repertoire collapses
+ integrated behaviour degrades
```

That phenotype would be much more informative than simply silencing modules.

---

## 7. Static bridge versus dynamically routed bridge

The current mutual-legibility programme already asks whether constrained transformations can restore receiver use across frozen endpoints. Dynamic routing should be inserted as an additional explanatory level rather than replacing that programme.

Compare:

- `L0`: native interface;
- best admissible static bridge from the existing bridge ladder;
- the same bridge with temporally structured routing gain;
- the same bridge with gain statistics preserved but direction/time shuffled;
- a dynamically routed native interface without learned transformation where dimensions permit.

The decisive possibilities are:

### Static bridge sufficient

If a static low-rank bridge completely restores receiver use and dynamic routing adds nothing, the problem is primarily coordinate/interface transformation.

### Dynamic routing necessary after bridge

If a static bridge restores decodability but not causal use or behaviour, and structured routing restores the latter, then **mutual legibility and causal access are separable problems**.

### Routing without bridge sufficient

If appropriately timed gain exposes already-compatible content to the receiver without transformation, the apparent interface failure was actually a gating/access failure.

### Neither helps

The bottleneck lies elsewhere: sender content, receiver computation, downstream valuation/selection, or an unmeasured transformation.

This decomposition is valuable regardless of whether the routing hypothesis survives.

---

## 8. Replay may maintain causal access correspondence

The current hippocampal campaign distinguishes local consolidation, retrieval triggering, stable routing, and interface repair. Dynamic information governance suggests another object that replay may maintain:

> **causal access correspondence** — the learned relation between a reinstated representation and the routing state that gives that representation appropriate downstream influence.

A stored episode may remain intact. The receiving system may remain competent. A static map between the two may even remain approximately valid. Yet retrieval can fail if the episode no longer recruits the correct route through downstream consumers.

Replay could therefore maintain both:

```text
sender representation <-> receiver representation
```

and

```text
reinstated episode <-> appropriate routing trajectory
```

This yields a discriminating extension of Assay B.

After controlled representational or interface drift, compare:

- correctly paired replay;
- marginal-matched shuffled replay;
- local rehearsal only;
- receiver-local adaptive repair;
- correct representational pairing with routing trajectory shuffled;
- correct routing trajectory with representational pairing shuffled.

If representational pairing is correct but routing pairing is wrong, local memory can remain intact while downstream behaviour fails. That would identify a failure mode unavailable to a purely static interface account.

Conversely, if shuffled routing has no cost once the representational bridge is correct, causal-access correspondence is unnecessary.

---

## 9. Relationship to ephaptic coupling

Ephaptic coupling is a possible biological implementation clue, not part of the computational hypothesis.

The abstraction REE should borrow is:

> aggregate local activity may produce a mesoscopic organising state that feeds back onto local effective connectivity.

To test whether this feedback matters computationally, compare two routing generators with matched output statistics:

1. **externally imposed routing schedule** — the gain trajectory is supplied independently of module activity;
2. **endogenous recurrent routing field** — the same class of gain trajectory is generated partly from the aggregate activity of the modules it regulates.

If both perform identically, endogenous field feedback is unnecessary.

If the recurrent field improves robustness, context adaptation, rapid reconfiguration, or recovery after perturbation, then the circular coupling itself becomes a legitimate architectural candidate.

No result here should be described as evidence that REE has an ephaptic mechanism. It would only establish that an analogous recurrent field-level organisation is computationally useful.

---

## 10. Relationship to consciousness should remain downstream

The anaesthesia literature makes the hypothesis tempting to interpret as a consciousness mechanism. REE should resist making that claim at this stage.

The near-term claim is narrower and experimentally reachable:

> flexible cognition may depend on selective, dynamically organised causal access between otherwise-competent subsystems.

Anaesthesia is useful because it supplies a natural family of perturbations in which substantial neural activity and information exchange continue while behavioural responsiveness and flexible integration collapse.

If an REE routing lesion reproduces an analogous dissociation, that would make the mechanism relevant to future theories of consciousness. It would not by itself demonstrate consciousness or unconsciousness in REE.

---

## 11. Failure modes and adversarial controls

The programme should actively try to kill the idea.

### Hidden attention mechanism

A routing field could simply be renamed attention. Compare it against a conventional context-conditioned scalar or sparse attention gate with matched parameter count and training signal.

### Extra compute

Dynamic routing may win merely because it adds parameters and recurrent computation. Match parameter and compute budgets and include a random recurrent-control field.

### Representation repair disguised as routing

A sufficiently expressive routing mechanism can encode semantic transformations. Constrain the first tests so routing modulates gain or access only and cannot synthesize new content.

### Off-manifold rescue

A routed bridge may force the consumer through unnatural states. Retain the receiver-manifold and dynamic-compatibility guards from the mutual-legibility programme.

### Behavioural shortcut

The field may learn action labels directly. Use same-action mismatches, held-out environments, and causal replacement controls.

### Estimator artefact

Directed-information measures can hallucinate direction under shared drivers, autocorrelation, or unequal signal-to-noise. Use conditional controls, temporal surrogates, known synthetic networks, and multiple estimators.

### Mere arousal scalar

If one global gain variable explains all effects, there is no evidence for a propagating routing geometry. Compare the field against a one-dimensional global arousal/gain control.

### Static topology sufficient

If fixed communication-subspace structure predicts behaviour as well as time-varying routing, keep the simpler static account.

---

## 12. Suggested staged programme

This should be a staged extension of the existing interface campaign rather than a separate architecture project.

### Stage 0 — no organism change

Build time-resolved directed-flow telemetry on frozen existing trajectories and known-information-preserving sources.

### Stage 1 — motif discovery

Ask whether successful behaviour shows reproducible directional-flow motifs, richer repertoire, or stronger directionality than degraded behaviour.

### Stage 2 — exogenous routing overlay

Introduce an evaluation-layer gain field without changing `ree_core`. Compare structured, flattened, direction-shuffled, timing-shuffled, and slow-mode-locked conditions.

### Stage 3 — bridge interaction

Combine routing with the frozen-endpoint bridge ladder and dynamic-compatibility assay to separate transformation from access.

### Stage 4 — replay correspondence

Test whether replay maintains representational mapping, routing correspondence, both, or neither under controlled drift.

### Stage 5 — endogenous field

Only if the previous stages support the mechanism, test a recurrent routing state generated partly from aggregate subsystem activity.

### Stage 6 — architectural consideration

Only after causal evidence and adversarial controls should a routing mechanism be considered for permanent integration into REE.

---

## 13. What would count as a strong result?

The strongest early result would not be a prettier flow diagram. It would be a dissociation:

1. sender information remains present and decodable;
2. receiver-local competence remains intact;
3. total intermodule exchange remains matched or higher;
4. structured routing is selectively disrupted;
5. behavioural integration degrades;
6. restoring the correct routing trajectory rescues causal use without improving sender information or receiver-local competence;
7. matched random, static, global-gain, and shuffled-routing controls do not rescue equivalently.

That would establish dynamic information governance as a distinct computational layer.

The strongest null would also be valuable:

> once representational adequacy and static mutual legibility are solved, temporally structured routing contributes nothing beyond a simple gain scalar or fixed communication subspace.

That result would tell us not to build this layer.

---

## 14. Broader architectural implication

The emerging possibility is that REE may require three distinct kinds of organisation:

```text
CONTENT
What is represented?

LEGIBILITY
How can one subsystem interpret another?

JURISDICTION
Which representation is allowed to influence which subsystem now?
```

The third is not merely inhibition or attention in the ordinary sense. The stronger hypothesis is that jurisdiction itself has **dynamics, propagation, repertoire, and history**.

That gives a possible computational meaning to a propagating wave in REE:

> not a travelling packet of thought, but a travelling frontier of causal privilege across the cognifold.

The important next step is therefore empirical. Before inventing such a field, test whether the existing organism already reveals the need for one, and whether carefully controlled routing perturbations explain variance that representation quality and static interface geometry cannot.
