# Dynamic information governance: propagating causal privilege, anaesthesia, and the routing geometry of cognition

**Date:** 2026-09-10  
**Status:** raw-to-refined thought; design-generative, not a claim registration and not an instruction to modify `ree_core`  
**Trigger:** Misawa et al. (2026), *Awake cortex stabilizes traveling waves for global and reliable information routing*, together with the current REE mutual-legibility, hippocampal-interface, anaesthesia, and `z_world` work  
**Related REE documents:**
- `2026-09-07_mutual_legibility_implementation_assays.md`
- `2026-09-09_hippocampal_campaign_adjudication.md`
- `2026-09-09_hippocampal_replay_interface_maintenance_supplement.md`
- `../../evidence/planning/hippocampal_campaign_assay_specifications_20260910.md`

---

## 1. Origin of the thought

The motivating observation is not merely that travelling waves occur in cortex, nor that anaesthesia changes brain rhythms. The more interesting result is that wakefulness appears to change the **relationship between physical propagation and directional information flow**.

Misawa et al. used high-density electrocorticography (ECoG) over much of the right cerebral hemisphere in rats and compared visual-evoked cortical travelling waves during wakefulness and isoflurane anaesthesia. Their principal result is counterintuitive in a way that is useful for REE:

- travelling waves exist in both states;
- absolute transfer entropy can be higher under anaesthesia;
- awake waves are more stable and show a richer repertoire of widespread motifs;
- information transfer is more selectively aligned with the direction of wave propagation during wakefulness;
- the authors call this relationship **informational tuning**.

Thus the awake brain is not distinguished simply by more activity or even more total information transfer. What seems to improve is the **reliability, selectivity, geometry, and organisation of information flow**.

This suggests a possible distinction that has not yet been explicit enough in REE:

> A system may contain information, and may even exchange large amounts of information, while still lacking an organisation that determines which information is permitted to become causally influential where and when.

That organisation can be called **dynamic information governance**.

The corresponding REE hypothesis is that cognition may require not only representations and transformations, but also a changing routing geometry that confers **temporary causal privilege** on particular flows through the organism.

The travelling-wave analogy is therefore not primarily:

> information moves like a wave.

It is:

> the organism continuously constructs a spatiotemporal pattern that determines which otherwise-available information can effectively influence which downstream process next.

---

## 2. The central distinction: representation, transformation, and jurisdiction

REE already has increasingly explicit questions about representation and interface transformation.

A sender may contain task-relevant information. A receiver may nevertheless fail to use it because the sender and receiver are not mutually legible. A bridge or communication subspace may recover that relationship.

But that still leaves a third question:

> Even when a representation exists and a valid transformation exists, **when is that transformed message allowed to matter?**

This suggests three distinct objects.

### 2.1 Representation

Let `h_i(t)` denote the state of subsystem `i` at time `t`.

This answers:

> What does this subsystem currently represent or contain?

### 2.2 Transformation / interface

Let `W_ij` denote a native or learned mapping from subsystem `i` to subsystem `j`.

This answers:

> If information from `i` is delivered to `j`, in what form can `j` use it?

### 2.3 Dynamic causal privilege

Let `g_ij(t)` denote the momentary effective conductivity or gain of the `i -> j` relation.

A minimal message model is then:

```text
m_i->j(t) = g_ij(t) * W_ij(h_i(t))
```

The new object is `g_ij(t)`.

It answers:

> At this moment, how much jurisdiction does `i` have over `j`?

The important claim is not that every REE edge needs a scalar gate. The scalar is merely the simplest implementable abstraction. The deeper proposal is that effective connectivity may have a **dynamic geometry**, potentially low-dimensional, structured, propagating, and partly endogenous.

A representation can therefore be intact but causally silent. A transformation can be correct but unavailable at the wrong time. A high-volume channel can be behaviourally useless if it is not selectively coordinated with the rest of the organism.

This is the computational distinction suggested by the anaesthesia result.

---

## 3. What could a “travelling wave” mean in REE?

REE does not need a literal two-dimensional cortical sheet or a physical wave equation in order to test the underlying idea. The useful abstraction is propagation over an **interaction graph**.

Nodes might initially correspond to concrete producer/consumer sites already identified in the mutual-legibility inventory rather than to broad labels such as “memory” or “perception”. Edges are actual causal interfaces.

A travelling wave analogue would then be a structured temporal evolution of edge or node receptivity.

Several implementations are possible.

### 3.1 Propagating gain field

Define a low-dimensional routing state `r(t)` from which edge gains are derived:

```text
g_ij(t) = G_ij(r(t), context(t))
```

and allow `r(t)` to evolve according to:

```text
r(t+1) = F(r(t), organism_activity(t), control_state(t), context(t))
```

A local change in routing state could increase the probability that neighbouring or functionally adjacent edges become permissive on subsequent timesteps.

This is the cleanest first implementation because it separates the hypothesis from any commitment to oscillations.

### 3.2 Phase-coded gating

Each subsystem could possess a phase-like receptivity variable. Messages have greater downstream influence when sender and receiver phases occupy compatible regions.

A travelling wave is then a phase gradient moving across the graph.

This is biologically evocative but should be a later implementation because it introduces unnecessary degrees of freedom before the simpler routing hypothesis is established.

### 3.3 Dynamic edge conductivity

Instead of a node-level wave, allow a low-rank field over edges. The system may transiently form routes such as:

```text
perception -> world evidence -> prediction -> valuation -> commitment
```

or:

```text
hippocampal reinstatement -> cortical representation -> prediction repair -> policy reconsideration
```

while alternative routes are partially suppressed.

This formulation may map most directly onto **causal privilege**.

### 3.4 Precision / attentional front

The field could initially be implemented using quantities already adjacent to REE's control-plane ideas: gain, precision, arousal, mode, veto, or prediction-error relevance.

This is attractive because it may reveal that the needed routing geometry partly already exists implicitly.

The danger is premature identification. A control-plane scalar is not automatically a travelling routing field. The experiment should establish whether a distributed and temporally structured access variable exists before it is equated with any existing mechanism.

### 3.5 Endogenous field feedback: the ephaptic analogue

A later model can make the routing field partly generated by the aggregate activity it subsequently regulates:

```text
local activity -> field state -> altered local effective connectivity -> new activity
```

This resembles the computational role one might abstract from ephaptic coupling, where extracellular fields generated by neural activity can feed back onto neuronal excitability without ordinary synaptic transmission.

This is **not** required by the travelling-wave result and should remain a separate hypothesis. The useful REE question is whether an endogenous aggregate coordination variable confers capabilities that an externally imposed routing schedule does not.

---

## 4. Why this matters specifically now

This thought lands at a useful point in the current REE experimental programme.

### 4.1 `z_world` has already separated information loss from routing failure

V3-EXQ-1010 now gives a binding negative result for the trained `z_world`: on the over-capacity decoder ladder, decision-relevant oracle content was not recoverable under the validated probe conditions. The current assay specification therefore excludes trained `z_world` as the sender for the new hippocampal/mutual-legibility assays and uses the measured-adequate `rawfield25` source primarily, with `ws250_pca32` as a later replication source.

This is helpful rather than disappointing for the present thought.

Dynamic routing cannot recover information that has been destroyed at encoding. That supplies a hard boundary:

```text
content absent -> routing hypothesis cannot rescue
content present + native use absent -> routing/interface hypotheses become admissible
```

The routing field must therefore be tested on a source already proven to contain the relevant information.

### 4.2 The live bottleneck is already an interface-instrument bottleneck

The implementation-ready hippocampal assay specification records that REE currently lacks the needed communication-subspace estimator, bridge ladder, causal-replacement harness, receiver-manifold guard, and dynamic-compatibility scorer. Assays A and B are therefore instrument-blocked rather than substrate-blocked.

That instrument family is precisely where dynamic information governance can be tested without changing the organism.

The mutual-legibility work already established the correct first principle:

> diagnosis without changing the organism.

The same rule should bind here.

Before adding a routing field to `ree_core`, measure whether existing REE trajectories already display organised directional information flow and whether such organisation predicts behavioural competence.

### 4.3 Static mutual legibility may be insufficient

The mutual-legibility programme already distinguishes static bridgeability from dynamic compatibility. A bridge that maps `x_t` into a receiver-compatible point but produces the wrong downstream trajectory is not a successful interface.

The present thought extends that one step further:

> a dynamically compatible transformation may still require correct **temporal access** to become causally useful.

Thus a complete interface may have at least three properties:

1. representational content survives;
2. sender and receiver are mutually legible;
3. their interaction occurs within the correct routing state.

That third property is a candidate missing variable.

---

## 5. A stronger interpretation of hippocampal replay

The current replay/interface-maintenance work asks whether paired replay can restore cross-system access after representational drift while local information remains intact.

That framing should now be widened cautiously.

Replay may maintain not only:

```text
sender representation <-> receiver representation
```

but:

```text
sender representation
    -> appropriate access/routing state
    -> receiver representation
    -> appropriate downstream consumer
```

Call this **causal access correspondence**.

A replay event could therefore train or refresh at least three distinct things:

- the sender content itself;
- the transformation between sender and receiver;
- the context/timing/routing state under which the receiver should grant the sender causal influence.

This gives a particularly sharp role to correct-versus-shuffled replay.

A shuffled replay arm can preserve:

- the same events;
- the same activity volume;
- the same sender marginals;
- the same receiver marginals;
- the same gross plasticity opportunity;

while destroying the **identity of which sender event should acquire access to which receiver state under which context**.

If correct replay repairs downstream use while shuffled replay does not, and endpoint-local competence remains equivalent, the result would no longer be describable merely as “more consolidation”. It would support maintenance of a structured interface or routing relation.

The existing replay-maintenance supplement correctly warns that biological evidence has not yet closed this chain. That remains true. Dynamic information governance is therefore a **design-generative extension**, not a new established mechanism.

---

## 6. Anaesthesia as an information-governance lesion

The most useful anaesthesia hypothesis is not “anaesthesia switches processing off”.

The Misawa result argues directly against such a crude interpretation: absolute transfer entropy was not lower under anaesthesia. Instead, informational tuning was poorer.

Bhattacharya et al. (2022) provides a complementary result under propofol in non-human primates. Loss of consciousness increased and organised slow-delta travelling waves while higher-frequency alpha/beta waves decreased, lost structure, and changed propagation directions. Thus unconsciousness need not correspond to disappearance of waves or disappearance of large-scale organisation. One form of large-scale organisation can become **too dominant**, reducing the richer multiplexed organisation associated with cognition.

This suggests a possible common computational lesion across anaesthetic mechanisms:

> loss of flexible, selective, state-appropriate control over which information flows become causally privileged.

Different drugs could produce that lesion differently.

One could imagine at least three anaesthesia-like failures in REE:

### 6.1 Routing flattening

All channels become similarly permissive.

Total information flow can remain high or even rise, but directional selectivity collapses.

Prediction:

```text
high transfer volume + low routing selectivity + poor behaviour
```

### 6.2 Routing domination

One slow/global mode captures excessive routing authority, suppressing alternative faster or more specialised routes.

Prediction:

```text
high global coherence + low routing repertoire + poor flexible behaviour
```

This is conceptually closer to the propofol slow-delta result.

### 6.3 Routing fragmentation / instability

Routes form but do not remain stable long enough for multi-step information transfer.

Prediction:

```text
local decodability intact + short-lived directional influence + poor long-horizon coordination
```

These three lesions can all impair organised cognition without deleting stored representations.

That provides a much stronger experimental notion of an “anaesthesia-like” REE state than simply suppressing module activity.

---

## 7. The relation to consciousness should remain carefully bounded

The neuroscience motivates an organisational hypothesis. It does not establish a sufficient condition for consciousness.

REE should therefore avoid the inference:

```text
travelling routing field present => consciousness
```

or even:

```text
informational tuning present => consciousness
```

The defensible computational hypothesis is narrower:

> flexible integrated behaviour may depend on selective, reliable, temporally structured information routing, and general anaesthesia provides a biological perturbation in which this organisation changes profoundly while substantial neural activity and information transfer continue.

If REE later develops an analogous transition, that would be relevant to theories of conscious organisation. It would not by itself establish subjective experience.

This distinction is especially important because the proposed routing layer may be useful even in architectures where no consciousness claim is made.

---

## 8. Informational tuning for REE

Misawa et al.'s most useful contribution may be methodological rather than architectural: they measure how well **information-flow direction aligns with propagation direction**.

REE can formulate a graph analogue.

Suppose at time `t` the candidate routing field predicts a preferred set or direction of edges `R(t)`, while observed trajectory data permit estimation of directed predictive influence `I_ij(t)`.

Define a descriptive routing-fidelity score such as:

```text
RF(t) = information influence carried on preferred/routing-aligned edges
        ---------------------------------------------------------------
        total comparable directed influence
```

or a contrastive tuning index:

```text
TI(t) = (I_aligned - I_offroute) / (I_aligned + I_offroute + epsilon)
```

The exact metric should not be fixed from this thought. Transfer entropy, conditional mutual information, directed information, lagged predictive improvement, or perturbational causal measures may each be appropriate depending on the interface.

The important experimental distinction is between:

- **amount** of intermodule information transfer;
- **selectivity** of transfer;
- **stability** of the preferred routes;
- **repertoire/diversity** of route motifs;
- **behavioural appropriateness** of the routes;
- **causal necessity** of route-specific traffic.

A wake-like REE signature would not simply maximize transfer.

It might instead occupy a regime in which transfer is **sparse enough to be selective, rich enough to be flexible, stable enough to complete a computation, and dynamic enough to change with context**.

This is a much more interesting optimisation target.

---

## 9. Immediate experiment programme: measure before building

The first tranche should be an observational and intervention-light campaign layered onto the existing mutual-legibility apparatus.

### Experiment DIG-0 — directed-flow telemetry

**Question:** Does unmodified REE already exhibit structured directional information flow across concrete producer-consumer interfaces?

Record aligned trajectories from a small set of already load-bearing interfaces, starting with those for which information-preserving sources and actual consumers are known.

For each interface estimate, with held-out temporal blocks and appropriate lag controls:

- directed predictive influence;
- influence magnitude;
- preferred lag;
- stability across nearby timesteps;
- stability across episodes;
- context dependence;
- relationship to action commitment and behavioural success.

Do not begin by forcing a wave model onto the data.

**Useful positive result:** high-competence episodes show more selective/stable sequences of directed influence than matched low-competence episodes despite similar total activity/traffic.

**Strong negative result:** performance is unrelated to any reproducible routing structure after nuisance variables are controlled.

### Experiment DIG-1 — route motif discovery

Treat each short time window as a directed influence graph.

Cluster these graphs to ask whether REE naturally occupies a limited repertoire of recurring routing motifs.

Measure:

- motif count/effective repertoire;
- transition probabilities between motifs;
- context specificity;
- duration;
- behavioural outcome conditional on motif;
- whether motifs form recurring ordered sequences rather than independent states.

A travelling-wave analogue may appear as a **trajectory through routing motifs** rather than literal translation of one motif across space.

### Experiment DIG-2 — externally imposed low-rank routing overlay

Only after DIG-0/1 establish a measurable substrate, introduce an **experiment-layer** routing overlay over frozen endpoints.

Use the known-information-preserving `rawfield25` sender first.

Compare:

1. native routing;
2. low-rank context-conditioned routing;
3. temporally shuffled routing;
4. edge-permuted routing preserving gain distribution;
5. flat/uniform routing;
6. high-traffic random routing matched for total transmitted norm/message count.

The field must initially carry **no semantic content** of its own. It may alter gains, timing, or access only.

This prevents a routing controller from secretly becoming another policy network.

### Experiment DIG-3 — anaesthesia-like lesions at matched information volume

Construct lesion families explicitly designed to preserve gross traffic.

#### FLAT
Equalise edge gains.

#### SHUFFLE-TIME
Preserve the gain values and edge identities but permute timing.

#### SHUFFLE-EDGE
Preserve temporal gain statistics but permute which edges receive them.

#### DOMINANT-SLOW
Drive the system with one broad, slowly changing routing mode.

#### FRAGMENT
Increase routing-state turnover so routes fail to persist.

#### FEEDBACK-CUT
Allow an imposed field but remove activity-dependent updating of the field.

The decisive anaesthesia-like result is not reduced traffic. It is:

> behaviour deteriorates while total intermodule transfer is matched or increased, and the deterioration tracks loss of routing selectivity/stability/repertoire.

### Experiment DIG-4 — static bridge versus dynamically routed bridge

Use the existing frozen-endpoint bridge ladder.

Compare a bridge with identical parameters under:

- continuously available transmission;
- context-appropriate dynamic routing;
- wrong-phase / shifted routing;
- route-shuffled routing.

This directly tests whether mutual legibility alone is sufficient.

A result of:

```text
static bridge ~= dynamically routed bridge
```

would weaken the need for this new layer.

A result of:

```text
correct dynamic routing > identical bridge with matched but mistimed availability
```

would show that temporal access contributes beyond coordinate transformation.

### Experiment DIG-5 — replay repairs causal access correspondence

This should fan into hippocampal Assay B rather than become an unrelated experiment family.

After controlled task-relevant drift:

- correct intersystem replay;
- shuffled-pair replay at matched marginals;
- local rehearsal;
- receiver-local adaptation;
- no maintenance;
- correct replay with routing updates disabled;
- correct replay with transformation updates disabled, if separable.

Ask separately whether replay restores:

1. endpoint-local information;
2. static bridgeability;
3. routing fidelity;
4. causal receiver use;
5. held-out behaviour.

This decomposition can determine whether replay is maintaining storage, transformation, access geometry, or some combination.

### Experiment DIG-6 — endogenous field feedback

Only if earlier experiments support routing as load-bearing, compare:

- an externally scheduled routing field;
- an endogenous field with the same marginal statistics but whose evolution depends on aggregate module activity.

This is the correct stage at which to test an ephaptic-like abstraction.

The key question is not whether it looks biologically wave-like. It is whether **closing the activity -> field -> activity loop adds robustness, rapid coordination, or adaptive routing that cannot be reproduced by a matched open-loop schedule**.

---

## 10. Falsifiers and rival explanations

This thought should be easy to kill if it is unnecessary.

### F1 — traffic amount is sufficient

If performance is explained by total transmitted activity/information and route selectivity adds nothing, dynamic governance is not needed.

### F2 — static interface suffices

If a fixed bridge between frozen endpoints restores the full behavioural phenotype regardless of timing or routing manipulation, the problem is mutual legibility rather than dynamic access.

### F3 — ordinary control-plane gain suffices

If existing precision/gain variables already explain the full effect and no distributed route geometry is required, a separate routing field is redundant.

### F4 — the routing controller performs cognition itself

If the routing field has access to semantic targets, oracle labels, action values, or future outcomes, successful routing becomes uninterpretable.

The first field must be content-poor and capacity constrained.

### F5 — representation loss masquerades as routing failure

The V3-EXQ-1010 lesson binds this entire programme. Sender content must be independently demonstrated before routing failure can be claimed.

### F6 — receiver off-manifold shortcuts

A routed bridge may simply drive a consumer into unnatural but effective states. The receiver-manifold guard remains mandatory.

### F7 — temporal correlation masquerades as causality

Directed predictive measures can report common-driver structure. Causal replacement/ablation and matched timing controls are required before “causal privilege” language is promoted beyond hypothesis.

### F8 — behavioural arousal confound

High-competence runs may trivially contain more activity or exploration. Compare matched action count, movement, opportunity, episode phase, and gross activation where relevant.

### F9 — wave metaphor overfitting

A useful routing system need not propagate smoothly. If the best model consists of abrupt switching between global routing modes, retain the information-governance result and discard the travelling-wave analogy.

That would still be scientific progress.

---

## 11. Relationship to the REE control plane

The control plane already contains candidate quantities such as precision, gain, mode, arousal, and veto. Dynamic information governance could relate to them in several ways.

### Possibility A — control plane drives routing

Control state selects or biases routing motifs.

```text
control state -> routing geometry -> effective intermodule influence
```

### Possibility B — routing state is part of the control plane

What has been described abstractly as precision/gain may ultimately need a distributed rather than scalar representation.

### Possibility C — bidirectional relation

Routing determines which prediction errors and state changes become visible to control mechanisms, while the control mechanisms reshape routing.

```text
control <-> routing <-> representational systems
```

This is the most biologically suggestive option but should not be assumed.

The empirical question is whether a low-dimensional routing variable explains variance in effective intermodule causality that existing recorded control variables do not.

---

## 12. Relation to E1, E2, commitment, and the cognifold

If this hypothesis is useful, its importance may eventually go beyond one interface.

E1 and E2 are not merely stores. They participate in different predictive timescales and forms of consequence modelling. A coherent decision may require information to acquire causal privilege in an ordered manner:

```text
observation
 -> current-world interpretation
 -> fast possible consequence
 -> deeper persistent expectation
 -> self/other/harm/benefit significance
 -> counterfactual comparison
 -> commitment
```

This should not be hard-coded as a universal serial pipeline. The point is that a successful cognitive act may correspond to a **temporally organised traversal of representational territories**.

The term *cognifold* is useful here if treated literally as a structured space of available cognitive states and relations. A routing field would define which directions through that space are currently dynamically accessible.

This gives one possible meaning to the intuition that higher-order cognition may involve a “representation of the representation system itself”. The organising variable need not explicitly encode a prose-like map saying “this is perception, this is memory, this is self”. It could instead emerge as a compact dynamical object describing **which regions of representational state space can currently influence which others**.

If stable invariants later emerge from this routing geometry — for example recurrent routes involving self, harm, other, memory, prediction, action — those invariants should be discovered rather than imposed.

---

## 13. Why the anaesthesia convergence could be especially informative

General anaesthetic agents differ substantially in molecular targets and network effects, yet converge behaviourally on profound loss of responsiveness/conscious experience at sufficient dose.

REE can use this as a comparative-inference strategy rather than a consciousness proof.

For each well-characterised anaesthetic state in the literature, ask:

- what happens to travelling-wave directionality?
- what happens to wave repertoire?
- what happens to long-range feedback/feedforward balance?
- what happens to effective connectivity?
- what happens to excitation/inhibition structure?
- what happens to complexity/integration measures?
- what happens to thalamocortical and corticocortical routing?
- what remains active despite behavioural unresponsiveness?

Then ask whether these seemingly different lesions share a more abstract computational phenotype:

> abundant local processing with degraded flexible governance of global causal access.

If that convergence survives detailed literature review, REE gains a biologically motivated family of perturbations rather than a single anaesthesia analogy.

If it does not survive, the hypothesis should be narrowed to the specific travelling-wave/informational-tuning phenomenon.

---

## 14. Biological mechanism: what is known and what remains speculative

The travelling-wave result does **not** identify ephaptic coupling as the mechanism of informational tuning.

The biological wave can arise from interacting synaptic, cellular, anatomical, oscillatory, and field-level dynamics. The Misawa study is principally evidence about the geometrical relation between observed waves and directional information transfer.

There is nevertheless independent biological evidence that extracellular fields are not always passive readouts. Anastassiou et al. showed that physiologically plausible extracellular fields can alter membrane potential and entrain action potentials through ephaptic coupling, independent of conventional synaptic transmission. Buzsáki, Anastassiou, and Koch reviewed how synchronous population currents generate extracellular fields and how sufficiently coherent field gradients can in turn alter neuronal excitability.

That motivates — but does not establish — an additional REE idea:

> a useful organising variable may be both produced by local processing and able to alter the effective excitability/connectivity of the same system.

This creates circular causation across scales without requiring a homuncular controller.

However, the experiment should distinguish:

```text
routing is useful
```

from:

```text
endogenous field feedback is necessary for useful routing
```

The latter is a much stronger claim and belongs later in the programme.

---

## 15. Broader supporting observations from travelling-wave research

The Misawa result is not isolated from the broader travelling-wave literature.

Luo and Ester (2025) reported forward and backward travelling waves linking visual and frontal/motor regions during working-memory-guided behaviour. The waves predicted behavioural timing and were absent when participants selected and prepared a response but did not execute the memory-guided action. This is consistent with the idea that waves may organise the timing and direction of interactions needed to turn represented content into behaviour.

Mohanta et al. (2024 preprint) reported anterior-to-posterior alpha waves associated with predictions and posterior-to-anterior waves associated with mismatch-driven model updating in human intracranial recordings. Because the work is a preprint, it should be treated as suggestive rather than definitive, but the computational structure is strikingly REE-relevant: the direction of propagation differs for prediction versus correction.

Together these studies motivate a general question:

> Is directionality itself part of the computation — not merely a side effect of where activity happened to begin?

REE is unusually well positioned to test this because its internal causal paths are inspectable and can be selectively perturbed.

---

## 16. A possible minimal formalism

A deliberately small model is preferable to a biologically decorated one.

Let the organism be a directed graph `G=(V,E)`.

Each node has representational state:

```text
h_i(t)
```

Each edge has a baseline transform:

```text
W_ij
```

A low-dimensional routing state:

```text
r(t) in R^k, with k << |E|
```

induces effective gains:

```text
g_ij(t) = sigmoid(a_ij^T r(t) + b_ij + c_ij(context_t))
```

and message passing:

```text
m_ij(t) = g_ij(t) W_ij h_i(t)
```

The routing state evolves by:

```text
r(t+1) = F r(t) + U phi(h(t)) + V control(t) + noise
```

with constraints preventing `r` from directly encoding action labels or oracle targets.

A “propagating” version constrains `F` and the edge loadings so that nearby interfaces in a declared functional graph tend to become active sequentially rather than arbitrarily.

Key observables are then:

- gain entropy;
- effective number of open routes;
- route persistence;
- route transition entropy;
- routing/information-flow alignment;
- motif repertoire;
- behaviour conditional on routing state;
- causal effect of route-preserving versus route-destroying perturbations.

This is sufficient to test the idea. A physical oscillation is not.

---

## 17. What success would look like

The strongest result would not be “adding waves improves score”. That is too easy and too underspecified.

A convincing progression would look more like this:

1. unmodified competent REE already shows reproducible, context-dependent directed-flow motifs;
2. motif selectivity predicts behaviour above total traffic/activity;
3. temporally or topologically scrambling those motifs impairs behaviour while traffic is matched;
4. a constrained routing overlay can rescue an interface failure without adding semantic content;
5. the same bridge without correct timing fails or performs worse;
6. anaesthesia-like routing lesions produce high-traffic but low-selectivity states;
7. correctly paired replay restores routing fidelity after controlled drift better than matched shuffled replay;
8. this restoration predicts recovered causal consumer use and behaviour;
9. only after those findings, an endogenous activity-generated field outperforms matched open-loop routing.

That chain would justify architectural incorporation.

Anything materially weaker should remain an external diagnostic or descriptive model.

---

## 18. What failure would teach us

This programme is useful even if the central hypothesis fails.

- If no organised directional motifs exist, REE's present cognition is probably too feed-forward/local or the chosen measurement scale is wrong.
- If motifs exist but scrambling them does nothing, they are descriptive epiphenomena.
- If static bridges rescue everything, interface geometry matters but dynamic routing does not.
- If gain amount explains behaviour, ordinary precision/control may suffice.
- If only high-capacity routing networks work, the routing mechanism is probably performing hidden cognition rather than governing information flow.
- If replay restores bridgeability but not routing structure, interface reassociation may be sufficient without causal-access maintenance.
- If total information transfer falls whenever behaviour falls, the anaesthesia-like “high traffic, poor tuning” analogy does not reproduce in REE.

These are all informative outcomes.

---

## 19. Provisional vocabulary

The following terms appear useful if kept distinct.

**Dynamic information governance**  
The time-varying organisation that determines which available information can exert effective causal influence across the organism.

**Causal privilege**  
Temporary elevation of one representation/pathway's ability to alter downstream state relative to competing available pathways.

**Routing geometry**  
The structured pattern of effective intersystem access at a moment or over a short trajectory.

**Routing motif**  
A recurring configuration of directional causal/informational influence.

**Causal access correspondence**  
A learned or maintained relation specifying not only how one representation maps to another, but under which context/timing/routing state it becomes usable by the appropriate consumer.

**Informational tuning (biological term from Misawa et al.)**  
Selective alignment between travelling-wave propagation direction and directional information flow.

**REE informational-tuning analogue**  
A descriptive measure of alignment between a candidate routing geometry and measured directed influence in REE. It should not be assumed equivalent to the biological measure without explicit methodological mapping.

---

## 20. Immediate routing recommendation

This thought should **not** immediately create a new permanent REE module.

The high-gain next move is to amend/fan out the existing mutual-legibility and hippocampal instrument work so that the planned instrumentation can additionally measure temporal directional influence and routing selectivity.

The recommended order is:

```text
measurement
 -> descriptive routing motifs
 -> matched causal perturbation
 -> external routing overlay
 -> anaesthesia-like lesion family
 -> replay/access-maintenance test
 -> only then endogenous field architecture
```

This preserves the current discipline of diagnosing interfaces before changing the organism.

The first concrete design deliverable should therefore be a **dynamic-routing companion specification** for the existing communication-subspace/bridge instrument, not an implementation in `ree_core`.

---

## 21. Bottom line

The travelling-wave result suggests a distinction that may be highly relevant to several current REE problems.

A cognitive organism may require more than:

```text
what information exists
```

and:

```text
how representations translate into one another.
```

It may also require:

```text
which information is presently permitted to matter,
where it may matter,
in what order,
and for how long.
```

That is an information-governance problem.

On this view, the functional analogue of a cortical travelling wave in REE is not a packet of content passing from module to module. It is a **travelling frontier of causal privilege**: a dynamically organised pattern of receptivity and effective connectivity that makes some routes temporarily authoritative while leaving others latent.

Anaesthesia is especially informative because it suggests that cognition can fail without silence. Information transfer may remain abundant while its organisation becomes noisy, stereotyped, mistimed, or monopolised by the wrong global mode.

That provides a concrete new hypothesis for REE:

> **Competent integrated behaviour depends not on maximising intermodule information flow, but on dynamically governing its selectivity, stability, repertoire, and causal timing.**

The hypothesis is close enough to the current interface bottleneck to test now, yet separable enough from the permanent architecture that it can be falsified cleanly.

---

## References / biological anchors

1. Misawa K, Chinen K, Kawabata A, Kaiju T, Suzuki T, Komura Y. **Awake cortex stabilizes traveling waves for global and reliable information routing.** *iScience*. 2026;29(8):116728. DOI: `10.1016/j.isci.2026.116728`.
2. Kyoto University. **Organized when awake, chaotic when not: Traveling waves in rat brains give hints about information transfer in consciousness.** Research news, 23 July 2026.
3. Bhattacharya S, Donoghue JA, Mahnke M, Brincat SL, Miller EK. **Propofol Anesthesia Alters Cortical Traveling Waves.** *Journal of Cognitive Neuroscience*. 2022;34(7):1274-1286. DOI: `10.1162/jocn_a_01856`.
4. Luo C, Ester EF. **Traveling waves link human visual and frontal cortex during working memory-guided behavior.** *Proceedings of the National Academy of Sciences of the United States of America*. 2025;122(30):e2415573122. DOI: `10.1073/pnas.2415573122`.
5. Mohanta S, Cleveland DM, Afrasiabi M, et al. **Traveling waves shape neural population dynamics enabling predictions and internal model updating.** bioRxiv preprint, 2024. DOI: `10.1101/2024.01.09.574848`. Treat as non-peer-reviewed until publication status changes.
6. Anastassiou CA, Perin R, Markram H, Koch C. **Ephaptic coupling of cortical neurons.** *Nature Neuroscience*. 2011;14:217-223. DOI: `10.1038/nn.2727`.
7. Buzsáki G, Anastassiou CA, Koch C. **The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes.** *Nature Reviews Neuroscience*. 2012;13:407-420. DOI: `10.1038/nrn3241`.

## Source-intake note

The immediate trigger was Darren Orf's 9 September 2026 *Popular Mechanics* article, **Scientists Turned Off Consciousness in Rats. Then Their Brains Started Going Wild**, which accurately pointed toward the counterintuitive high-transfer/low-tuning result. The scientific argument in this thought is grounded preferentially in the primary Misawa et al. paper and the related primary literature above rather than in the magazine framing.
