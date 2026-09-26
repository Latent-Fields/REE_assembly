# Thought intake: nicotinic filtering as a gate on migration from deliberative action to habit

**Date:** 2026-09-26
**Status:** intake / candidate — do not register a new claim until reconciled with the pending dual-route proposal-generation claim from 2026-09-25.
**Origin:** live discussion: whether nicotinic acetylcholine receptors are centrally involved in routing which actions become habitual rather than planned.

**Primary REE anchors:**
- `evidence/planning/thought_intake_2026-09-25_dual_route_habit_vs_deliberative_proposals.md` — proposer-side habit versus deliberative routes; practice migration is proposed but the write mechanism is not specified.
- `evidence/planning/thought_intake_2026-05-04_smoothened_da_ach.md` — dopamine–acetylcholine (DA–ACh) temporally windowed striatal policy writing; registered into MECH-453 / ARC-154.
- `docs/architecture/dopamine_into_gating.md` — implemented signed reward-prediction-error (RPE) three-factor learning in E3 (`w_chan`, `W_lat`).
- ARC-071 / MECH-323 / MECH-324 / MECH-312b — practice-dependent chunk formation, transfer/maintenance, and maturity weighting for habitual control.
- MECH-163 / SD-081 / MECH-477 — habitual versus planned scoring and reliability arbitration.

---

## 1. Seed idea

Nicotinic acetylcholine receptors (nAChRs) may help determine **which executed actions earn the right to become routable without prospective deliberation**.

The useful formulation is *not*:

> nicotinic receptor activation = habit mode.

Nor is it:

> acetylcholine chooses the habit controller instead of the planning controller.

A better mechanistic hypothesis is:

> striatal cholinergic timing, acting partly through presynaptic nicotinic receptors on dopamine terminals, changes the temporal contrast and local eligibility of dopaminergic teaching signals. This helps determine which recently active corticostriatal action representations are selectively reinforced strongly and specifically enough to migrate from deliberative construction into a cached/chunked habitual proposal repertoire.

So the nicotinic system is better treated as part of the **habit-acquisition write gate** than as the **habit/planning arbitration switch**.

In short:

**planning makes an action possible; repeated successful execution supplies evidence; cholinergic/nicotinic gating helps decide whether that evidence is written selectively enough for the action to become cheap, direct and habitual.**

---

## 2. What the biology actually supports

### 2.1 Dorsolateral striatum is required for canonical habit formation

Yin, Knowlton & Balleine (2004) showed that dorsolateral-striatal lesions preserve outcome expectancy but prevent the normal emergence of outcome-insensitive habitual responding. When the habit system is disrupted, control reverts toward goal-directed action.

This supports REE's existing distinction between a mature habit route and deliberative control, but says nothing by itself about nAChRs.

- PMID 14750976; DOI 10.1111/j.1460-9568.2004.03095.x

### 2.2 nAChRs participate directly in dopamine- and activity-dependent corticostriatal plasticity

Partridge et al. (2002) showed that nAChR activation in dorsal striatum contributes to dopamine- and activity-dependent long-term depression of corticostriatal synaptic efficacy. This places nicotinic signalling at exactly the kind of synapse whose modification could support stimulus–response / habit learning.

- PMID 11923419; PMCID PMC6758294.

### 2.3 The crucial nAChR function is a dopamine *filter*, not a scalar gain

Presynaptic beta-2-containing nAChRs on striatal dopamine terminals are tonically engaged by acetylcholine released from cholinergic interneurons. Under tonic engagement they raise release probability for isolated / low-frequency dopamine activity but also produce short-term depression, reducing the relative impact of subsequent high-frequency bursts.

When cholinergic interneurons pause and local acetylcholine falls — or when those nAChRs are otherwise functionally switched off/desensitised — low-frequency dopamine release falls while burst-evoked release becomes relatively favoured. The result is an increased phasic-to-tonic contrast: dopamine release more faithfully reflects the firing pattern of dopamine neurons.

That is a much more useful REE abstraction than a generic `ACh_gain` parameter. The gate is **frequency- and timing-sensitive**.

Relevant synthesis:
- Exley & Cragg (2008), *Presynaptic nicotinic receptors: a dynamic and diverse cholinergic filter of striatal dopamine neurotransmission*, PMCID PMC2268048.
- Sulzer, Cragg & Rice-associated striatal dopamine-release literature reviewed in PMCID PMC4850498.

### 2.4 Cholinergic pauses are learned, salient-event-linked timing events

Striatal cholinergic interneurons pause around salient or conditioned events after learning, approximately coincident with phasic changes in dopamine-neuron activity. This creates a plausible temporal conjunction between:

`state/action trace` + `salient outcome` + `phasic dopamine` + `acetylcholine/nAChR state`.

That conjunction is well placed to solve credit assignment: **which of the action representations active just before this outcome should actually be changed?**

- Zhang et al. (2018), *Neuron*, PMCID PMC5993868.

### 2.5 But cholinergic signalling is not simply pro-habit

Experimental disruption of dorsal-striatal cholinergic signalling can *increase* habitual responding. Silencing vesicular acetylcholine transport promoted habits, with dorsomedial-striatal acetylcholine loss sufficient to reproduce maladaptive habit-like behaviour in mice (Favier et al. 2020; PMID 33164988).

Other work suggests dorsolateral-striatal cholinergic interneurons can contribute strongly to exploration and behavioural flexibility rather than being necessary for the canonical habit function of the dorsolateral striatum itself (Amaya & Smith 2021; PMCID PMC8562003).

Therefore the candidate REE mechanism should **not** be "acetylcholine strengthens habits". A better interpretation is that cholinergic signalling governs the *specificity, timing, revision and flexibility* of reinforcement writing. Both too little and incorrectly timed gating could cause maladaptive habitual control, by different routes.

### 2.6 Nicotine provides an informative perturbation, not the physiological model

A 2025 study found that nicotine enhanced cue control over behaviour and dopamine release in dorsolateral striatum, with the behavioural effect blocked by the nAChR antagonist mecamylamine (PMID 40812200). Extended nicotine self-administration has also been shown to shift responding from goal-directed to habitual and to recruit dorsolateral-striatal / nigrostriatal circuitry (PMID 24823947).

These findings are compatible with nAChRs influencing cue-driven habitual action, but nicotine is pharmacologically abnormal: agonism rapidly desensitises high-affinity nAChRs and can functionally resemble turning parts of the receptor filter "off". Nicotine should therefore be treated as an intervention that exposes the filter, not as evidence that physiological nAChR activation monotonically promotes habits.

---

## 3. REE archaeology: what is already present

REE already contains almost all of the *pieces*, but they presently terminate at different boundaries.

### A. Habit versus deliberative control exists

The 2026-09-25 dual-route intake proposes two concurrent **proposal-generation** routes:

1. a cheap habit route over primitives and later practised chunks; and
2. a state-dependent deliberative route over learned abstract action objects.

It explicitly predicts practice-driven migration from deliberative composition to habitual proposal, but leaves the biological/computational write rule for that migration open.

REE also already contains the older **scorer-side** planned/habit split (SD-081 / MECH-163), arbitration by reliability (MECH-477), and practice/chunk transfer machinery (ARC-071 / MECH-323 / MECH-324 / MECH-312b).

### B. DA–ACh write gating exists

The May DA–ACh thought intake was registered on 2026-09-25:

- MECH-453 owns temporally coordinated DA–ACh striatal writing;
- ARC-154 separates action selection from reinforcement marking, plasticity permission, persistence and effort calibration;
- Q-109 asks whether acetylcholine-gated waking traces are later used by sleep/offline processing.

Its computational sketch already has:

`policy_update = DA_event × ACh_gate × context_match × policy_trace_strength × effort_adjustment`.

### C. Learned dopaminergic E3 gating exists in code

`docs/architecture/dopamine_into_gating.md` records an implemented E3 three-factor learning rule in which a signed RPE updates learned channel weights (`w_chan`) and a learned lateral-inhibition matrix (`W_lat`) from waking eligibility traces.

That machinery currently treats the RPE as the teaching event. It does not appear to contain a receptor-like mechanism that changes the **contrast/eligibility of that teaching event according to temporally structured cholinergic state**, nor does it direct those gated writes specifically into habit-route maturation.

### D. The missing join

The pieces currently look like:

`deliberative proposal -> action -> outcome -> DA/ACh write window`

and separately:

`practice/chunking -> habitual proposal repertoire`.

What is not yet explicit is:

`deliberative proposal`
`    -> executed action`
`    -> outcome / signed RPE`
`    -> acetylcholine/nAChR timing filter`
`    -> selective corticostriatal credit`
`    -> repeated context-specific evidence`
`    -> chunk / cached proposal becomes habit-route eligible`

This thought therefore proposes a **bridge**, not a new standalone controller.

---

## 4. Candidate architectural interpretation

### 4.1 Habit should be earned by selectively gated consolidation

A proposed sequence:

1. **Deliberative construction** proposes a novel action or multi-step action object.
2. **E3 commitment** selects it and lays an eligibility trace containing the state/context, selected action/chunk, route of origin and relevant appraisal features.
3. **Outcome evaluation** produces the signed teaching signal already represented by E3 RPE machinery.
4. **Cholinergic/nicotinic filtering** determines how diagnostic that teaching event is relative to tonic background and whether the recent trace receives selective plasticity credit.
5. Repeated successful, context-stable gated writes accumulate evidence that the action/chunk can be proposed directly.
6. **ARC-071 / MECH-323 transfer** promotes the practised composition into the habit repertoire.
7. Thereafter the habit proposer can emit it cheaply, while deliberative control remains available when reliability falls, contingencies change or novelty rises.

The important conceptual move is:

> **habit is not repetition alone. Habit is repeated action whose learning events have survived credit-assignment and context-specificity gates sufficiently often to justify bypassing prospective reconstruction.**

### 4.2 nAChR state should modulate *contrast*, not merely learning rate

Do not implement the biological idea as:

`delta_eff = delta * ACh_level`.

That would lose the central frequency-filter property and could even assign the biology in the wrong direction.

A better abstraction is something like:

`delta_habit = delta_signed × G_phasic_contrast × eligibility_action × context_specificity`

where `G_phasic_contrast` is high when the temporal relation between cholinergic state and the teaching event makes the event diagnostic rather than tonic/background.

At V3 scale, `G_phasic_contrast` need not model receptor kinetics. It can be a bounded local write factor attached to the waking eligibility trace, with an explicit future mapping to beta-2-containing presynaptic nAChR filtering.

### 4.3 Separate three questions that are easy to conflate

The proposed architecture keeps distinct:

1. **Which action wins now?** — E3 commitment / action selection.
2. **How strongly and specifically should this outcome modify the just-used action representation?** — DA–ACh / nAChR write filtering.
3. **Has this representation accumulated enough stable evidence to become directly proposable as a habit?** — chunk / habit-route transfer.

The nicotinic mechanism belongs primarily to (2), thereby influencing (3). It should not be inserted directly into (1) unless separate evidence demands that.

---

## 5. Relationship to the 2026-09-25 dual-route proposal thought

This is a mechanistic refinement of that thought.

The dual-route intake currently says:

> the deliberative route composes, the habit route caches what composition has made routine.

This intake proposes the missing verb between those clauses:

> **the deliberative route composes; DA–ACh/nicotinic-gated reinforcement determines what repeated compositions receive sufficiently selective credit; ARC-071/MECH-323 then transfers the mature representation into the habit route.**

Thus the route shift should not be implemented as a simple repetition counter or elapsed-practice threshold if a richer learning trace is available.

Practice count can remain evidence, but it should not be the cause by itself.

---

## 6. Novelty against existing claims

| Element | Existing owner | Disposition |
|---|---|---|
| Habit vs deliberative controllers / scorers | SD-081, MECH-163, MECH-477 | Existing |
| Proposal-generation split into habit and deliberative routes | 2026-09-25 dual-route intake; claim still pending registration in that intake | Existing/pending |
| Practice-dependent chunk transfer into habit | ARC-071, MECH-323, MECH-324, MECH-312b | Existing |
| DA–ACh temporally gated striatal policy write | MECH-453 | Existing |
| Separate selection / marking / permission / persistence / effort calibration | ARC-154 | Existing |
| Three-factor signed-RPE E3 learned gating | ARC-108 + MECH-450 implementation | Existing |
| **nAChR-like frequency/contrast filtering of the teaching signal, rather than scalar acetylcholine gain** | No explicit owner found | **Novel refinement** |
| **Use that gated teaching evidence as the bridge that earns transfer from deliberative composition into the habit proposer** | No explicit owner found | **Novel bridge** |
| acetylcholine/nAChR as the real-time habit/planning selector | No; evidence is mixed and argues against overclaiming | **Do not register** |

The safest governance action is therefore **not** to create an independent "nicotinic habit switch" claim. Reconcile this intake with MECH-453 / ARC-154 and the pending dual-route-proposer claim, then register only the narrow bridge if it remains unowned.

---

## 7. Candidate claim, deliberately narrow

### Candidate MECH — `nicotinic_filtered_habit_transfer`

**Draft only; ID not assigned.**

> Migration of a practised action representation from deliberative construction into REE's habitual proposal repertoire should depend on selectively gated reinforcement evidence rather than repetition alone. In the biological analogue, striatal acetylcholine and presynaptic nicotinic acetylcholine receptors shape the frequency/temporal contrast of dopamine release and corticostriatal plasticity, providing a candidate mechanism by which phasic outcome signals selectively reinforce recently active action channels. In REE, an nAChR-like `phasic_contrast/write_gate` should modulate the waking action eligibility trace used by ARC-071 / MECH-323 habit-transfer machinery. The gate modifies **credit and write eligibility**, not the immediate arbitration between habit and deliberative controllers.

**Depends on:** MECH-453, ARC-154, ARC-071, MECH-323, MECH-324, MECH-312b, ARC-108, MECH-450, and the pending 2026-09-25 dual-route proposal-generation claim.

**Epistemic category:** mechanism hypothesis / substrate conditional.

**Version relevance:** V3 experimentable abstraction; receptor-level biological fidelity V4+.

---

## 8. V3 falsifiable implementation sketch

Do not begin with receptor simulation. Add the smallest factor that distinguishes this hypothesis from the existing scalar-RPE rule.

For each waking committed action/chunk, retain:

- proposal route of origin;
- selected action/chunk identity;
- context/state signature;
- signed RPE / realised value signal;
- existing action eligibility trace;
- a bounded **phasic-contrast/write-gate** value;
- subsequent contingency stability / outcome variance.

Then compare at least:

### Arm A — repetition-only transfer

Habit maturity grows mainly with execution count / practice.

### Arm B — scalar gated transfer

Habit maturity grows with `signed_RPE × generic_ACh_gate × eligibility`.

### Arm C — phasic-contrast gated transfer

Habit maturity grows only when the teaching event is temporally/structurally diagnostic enough to pass a nAChR-like contrast gate.

A minimal abstract update:

```text
habit_credit_t =
    eligible_action_trace_t
    * positive_or_signed_teaching_component_t
    * phasic_contrast_gate_t
    * context_specificity_t

habit_maturity[action_or_chunk, context] += habit_credit_t
```

Transfer to the habit proposer occurs only after maturity crosses a threshold **and** outcome variance / contingency instability remain acceptably low (compose with MECH-323 / MECH-324 rather than replacing them).

The gate should be bounded and inspectable. It should not be allowed to smuggle in outcome value or route identity; otherwise the experiment becomes circular.

---

## 9. Predictions and falsifiers

### Prediction 1 — better credit specificity

Compared with repetition-only transfer, a gated-write arm should produce fewer inappropriate habits when several actions are co-active, when distractors are present, or when reward arrives near competing traces.

**Falsifier:** no improvement over count-matched repetition or generic scalar gain.

### Prediction 2 — appropriate migration with practice

In stable familiar contexts, the route-of-origin share of committed choices should migrate from deliberative to habitual as selectively reinforced chunks mature.

**Falsifier:** gated transfer does not alter route migration, or merely slows/speeds all learning uniformly.

### Prediction 3 — preserved flexibility under contingency reversal

Because the gate writes context-specific evidence rather than a global cached action, contingency change should weaken or suppress the habitual proposal and restore deliberative dominance faster than an indiscriminate write rule.

**Falsifier:** the gated arm is equally or more perseverative after outcome devaluation / contingency reversal.

### Prediction 4 — phasic filter beats matched scalar learning-rate control

A frequency/contrast-style gate should outperform a control with the same total integrated update magnitude but no temporal selectivity.

This is the critical test distinguishing the present idea from "just tune the learning rate".

**Falsifier:** a matched scalar gain reproduces all behavioural and credit-assignment effects.

### Prediction 5 — receptor abstraction may be unnecessary

It is entirely possible that REE's existing eligibility traces + MECH-453 write window + ARC-071/MECH-323 transfer already produce the needed behaviour without an additional nAChR-like factor.

**Falsifier of architectural necessity:** ablating the proposed phasic-contrast factor produces no meaningful loss once those existing mechanisms are fully coupled.

That is a successful scientific outcome: the biology would have inspired a test, not dictated an ornamental module.

---

## 10. Implications for REE's ethical testbed — without an ethical scorer

REE has **no ethical scorer**, and this thought must not imply one. Ethical causation in REE is supposed to emerge through the same ordinary machinery that constructs and evaluates trajectories: representations of self and others, predicted harm and benefit, uncertainty, vulnerability, responsibility, relationship/love, memory, affect, and commitment. The axioms are hypotheses about what becomes causally operative in that machinery, not inputs to a separate moral-value function.

Habit formation nevertheless matters to the ethical experiment because the same action can have different **causal ancestry**.

A prosocial action might be produced because, on this occasion, trajectory construction and selection are actively sensitive to another agent's state, predicted harm, responsibility, relationship and future possibility. The outwardly identical action might later be emitted as a cheap learned chunk because earlier experience repeatedly reinforced that response in similar contexts.

Those are behaviourally similar but experimentally different. The second case does not show that an ethical scorer has gone offline — none exists. It shows that the current action may depend less on the rich representations whose causal role REE is intended to test, because some of their previous work has been compressed into a learned proposal.

Accordingly, the relevant measurements are:

- route of origin of the committed action;
- which self/other, harm/benefit, responsibility, relationship and future-state representations actually contributed to the action on that trial;
- whether changed-other state, devaluation, novelty or conflict reopens richer trajectory construction;
- whether ablation of the relevant representations changes newly composed behaviour, mature habitual behaviour, or both;
- whether a habit remains appropriately revisable when the circumstances that originally made it useful no longer hold.

The key experimental question is therefore not:

> did an ethical evaluator approve this action?

It is:

> **did the representations and mechanisms that instantiate REE's ethical hypotheses causally shape the learning and/or present selection of this action, and can that causal history be demonstrated by intervention?**

Habit can therefore be scientifically useful to REE. It lets the experiment distinguish **online causal participation** from **earlier causal participation that has subsequently been compressed into policy**. A fast prosocial habit may be a product of prior self/other and responsibility-sensitive learning while requiring less recomputation on each occurrence. That is a hypothesis to test, not evidence of a separate ethical subsystem.

---

## 11. Recommended next action

1. **Do not add a receptor-specific module immediately.** First connect the existing MECH-453 / ARC-154 write-window outputs to the habit-transfer observables in ARC-071 / MECH-323 and the pending dual-route proposer design.
2. Add route-of-origin + habit-maturity observability if not already present.
3. Run the repetition-only vs generic-gate vs phasic-contrast-gate comparison with matched total update magnitude.
4. Register a new claim only if the phasic-contrast term adds explanatory or behavioural power beyond the existing generic DA–ACh write gate.
5. If it survives, retain the computational name `phasic_contrast/write_gate`; treat beta-2-containing striatal nAChRs as its biological exemplar rather than requiring literal receptor simulation.

---

## 12. Bottom line

REE already had both ends of this idea.

It has a route by which complex behaviour can be **constructed** and a proposed route by which practised behaviour can be **emitted habitually**. It also has DA–ACh-gated policy writing and implemented dopaminergic three-factor learning.

The missing bridge is a rule for **which successful deliberative actions are allowed to become habitual**.

Nicotinic striatal biology suggests a principled answer: not every dopamine event should write equally. Local cholinergic/nicotinic state can make some teaching events more temporally diagnostic than others, protecting credit assignment and shaping which action traces consolidate.

So the compact REE hypothesis is:

> **The habit route should not learn from repetition alone. It should inherit only action representations that have accumulated sufficiently specific, context-stable, neuromodulator-gated evidence to justify bypassing deliberative reconstruction.**

And the nicotinic insight is narrower but potentially crucial:

> **nAChRs may be a biological implementation of the filter that decides when dopamine is informative enough to help write that shortcut.**