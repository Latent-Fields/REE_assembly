---
title: Formal-Ancestor Mapping
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 11
---

# Formal-Ancestor Mapping

**Created:** 2026-07-09
**Status:** first pass (WS-4 of `evidence/planning/ree_ai_design_critique_plan.md`)
**Purpose:** Map REE's load-bearing MECH/ARC claims to their nearest formal ancestor in the ML / computational-neuroscience literature, and to that ancestor's *measurement apparatus*. REE re-derives much of its machinery from biology and currently pays the rebuild cost without collecting the benefit of the existing math. Making the mapping explicit does two things at once:

1. **Turns convergence into evidence.** When a biology-first derivation lands on the same structure as an independent formal program, that convergence is itself support for the structure being necessary rather than a design choice (the same argument REE already makes about the KAUST / Neural-Computers comparison).
2. **Hands REE ready measurement tools.** Each ancestor comes with an established way to *quantify* the thing REE is asserting — an arbitration weight, a value-function error, a subspace dimensionality, an interruption bound. Adopting the ancestor's yardstick lets experiments test *deviations* from a known baseline instead of re-deriving both the mechanism and its metric.

**How to use this table.** For each row: (a) if REE's claim is a re-derivation, adopt the ancestor's formalism as the null/baseline and design experiments around the *delta*; (b) if REE genuinely departs, document the departure precisely (that is where the novelty budget should go). The last section lists the parts that have **no** clean ancestor and should stay novel.

**Caveat.** This is a first pass built from the claim titles and the core-architecture summary. Citations are to the canonical primary sources; a per-row `/lit-pull` should confirm the precise formalism and pull any REE-specific corroborating work before a row is used to justify a substrate change. Treat un-lit-pulled rows as *hypothesised* ancestry.

---

## Mapping table

### Arbitration / control

| REE claim | What it asserts | Nearest formal ancestor | Ancestor's measurement apparatus REE can adopt | Re-derivation vs departure |
|---|---|---|---|---|
| **MECH-163** — habit (SNc/dorsal-striatum, model-free) vs hippocampally-planned (VTA/ventral-striatum+PFC, model-based) systems in parallel | Two goal-directed controllers arbitrated by context novelty / horizon | **Daw, Niv & Dayan (2005)**, *Uncertainty-based competition between prefrontal and dorsolateral striatal systems* — the canonical MB/MF arbitration model; **Gläscher, Daw, Dayan & O'Doherty (2010)** for the state-prediction-error signature | Arbitration weight as a function of each system's **posterior uncertainty**; the **two-step task** (Daw et al. 2011) as a behavioural readout that dissociates MB from MF via reward × transition interaction | **Re-derivation.** Adopt the uncertainty-weighted arbitration as REE's null; test whether REE's context-novelty gate reproduces the Daw weighting or deviates. The two-step task is a ready competence probe. |
| **ARC-021 / MECH-069** — three BG-like cortico-striatal loops need *incommensurable* learning channels; sensory PE, motor-sensory error, harm/goal error cannot be collapsed | Credit must be routed to the right loop by error *type* | **Doya (1999)** cerebellum(supervised)/basal-ganglia(reward)/cortex(unsupervised) tripartite learning; multi-objective / **modular RL** (Russell & Zimdars 2003); **active inference** as the single-functional null — see [`active_inference_bridge.md`](active_inference_bridge.md) §B1 | Per-channel error signals kept on **separate value heads**; test for **cross-channel credit leakage** as a measurable failure (does collapsing them mis-attribute credit?) | **Re-derivation with a sharp point.** Doya already argues distinct learning rules per structure; REE's "incommensurable" is the stronger claim. **Precisely** (bridge §B1): the departure is *commensurability*, not cardinality — active inference already factorizes objectives, so "one scalar" is a strawman; REE's real claim is *no shared currency* across error types. Measure via forced-shared-loss ablation that must fail to converge *regardless of capacity* (cf. V3-EXQ-009). |
| **ARC-016** — modes as control-plane regimes on shared machinery; the precision→commitment circuit | Precision routing sets the behavioural regime (focus/flow/panic/apathy) | **Active inference** precision-weighting (Friston et al. 2012, *Dopamine, affordance and active inference*); Parr/Pezzulo/Friston 2022 + Da Costa et al. 2020 — full bridge in [`active_inference_bridge.md`](active_inference_bridge.md) | Precision as **inverse variance on prediction error**; policy precision γ (≈ dopamine) as the beta-gate null; expected-free-energy decomposition into epistemic vs pragmatic value gives a principled exploration metric | **Re-derivation of vocabulary + one departure.** REE has the mechanism, not the calculus — import the precision units + γ (bridge §A). The **documented departure** (bridge §B2): REE's *multi-axis* (heterogeneous) precision vs active inference's single gain-modulated currency — currently *hypothesised*, owes a demonstration that single-axis precision cannot reproduce the mode transitions. |
| **ARC-030 / MECH-112/116/117** — symmetric Go(approach)/NoGo(avoidance); wanting (goal-distance) vs liking (benefit receipt) dissociable | Opponent approach/avoid channels; incentive salience ≠ hedonic evaluation | **Frank (2005)** BG Go/NoGo opponent model (D1/D2); **Berridge & Robinson (1998)** wanting/liking dissociation | Go/NoGo as **separable learning rates on positive vs negative RPE**; wanting/liking dissociated behaviourally (cue-triggered approach vs consumption) | **Re-derivation.** Frank's model gives a ready parameterisation for the symmetric-drive claim; Berridge gives the exact experimental dissociation MECH-117 needs. |

### Planning / world model

| REE claim | What it asserts | Nearest formal ancestor | Measurement apparatus | Re-derivation vs departure |
|---|---|---|---|---|
| **ARC-007 / ARC-018** — hippocampus stores/replays paths through residue-field terrain; explicit rollouts + post-commit viability mapping | Explicit multi-step trajectories over a valenced map (not implicit recurrent continuation) | **Successor Representation** (Dayan 1993); **hippocampus-as-SR** (Stachenfeld, Botvinick & Gershman 2017); **Dreamer V3** (Hafner et al. 2023) / **MuZero** (Schrittwieser et al. 2020) for learned-latent planning | SR matrix M(s,s′) as the "viability terrain" object; **grid/place-field predictions** of SR as a validation target; latent-rollout **value-prediction error** as the planning-quality metric | **Re-derivation with a distinctive twist.** The SR is the natural formal home of the "viability map"; the *residue field reshaping the terrain* is the novel part (SR does not have non-erasable owned-consequence writes). Map the map to SR, keep residue novel. |
| **ARC-001 / ARC-002** — E1 persistent deep predictor; E2 fast forward predictor of affordances | Slow deep world-model + fast one-step action-conditioned predictor | **JEPA / hierarchical world models** (LeCun 2022 AMI position paper; already referenced in `jepa_e1e2_integration_contract.md`); **cerebellar forward-model** theory (Wolpert, Miall & Kawato 1998) for E2 | Joint-embedding **prediction error in latent space** (not pixel space); forward-model accuracy as one-step **sensory-prediction error** | **Re-derivation.** E1/E2 is a slow/fast world-model decomposition JEPA formalises. Adopt latent-space PE as the metric; the *typed* split from E3 (below) is where REE differs. |
| **MECH-089** — E1 updates batched into theta-cycle summaries before reaching E3 (cross-frequency packaging) | Temporal multiplexing of updates across frequency bands | **Theta-gamma phase coding** (Lisman & Idiart 1995; Lisman & Jensen 2013) | Items-per-theta-cycle capacity (~7±2 in the Lisman model) as a **capacity metric** on the packet | **Re-derivation.** Direct descendant of Lisman coding; adopt its capacity prediction as a testable bound on ThetaBuffer size. |

### Commitment / temporal abstraction

| REE claim | What it asserts | Nearest formal ancestor | Measurement apparatus | Re-derivation vs departure |
|---|---|---|---|---|
| **MECH-090 / MECH-091 / ARC-030** — beta gate propagates E3→action only at commit; step a0→a1→a2 while committed; salient events phase-reset (urgency interrupt) | Commit to a temporally-extended action; interrupt on salience | **Options framework** (Sutton, Precup & Singh 1999); **interrupting options / call-and-return** (Sutton et al.; Bacon, Harb & Precup 2017 option-critic) | Option **termination function** β(s) as the formal analogue of the beta gate; **interruption improvement theorem** bounds when aborting a committed option is value-improving | **Re-derivation.** MECH-090/091 is literally option commitment + interruption. Adopt the termination-function formalism; the *residue/ownership* attached at commit is the non-standard addition. |
| **MECH-057 / MECH-061** — sequence completion verified before E3 eligibility; commit-boundary token reclassifies pre/post-commit error routing | A typed boundary where simulation becomes owned action | **No single clean RL ancestor** — closest is the model-based *plan-then-commit* separation and **options** initiation sets; the *typed error re-routing* is closer to a **gating/credit-assignment** switch | Measure as a **routing switch**: does post-commit error write to different targets than pre-commit? | **Partial departure.** The boundary *as a first-class typed object* has no standard ancestor. This is REE-distinctive (see novel list). |
| **MECH-094** — simulation-mode vs real-experience content kept distinct; failure = confabulation (sim encoded as real) | Imagination without belief update / without durable write | **Model-based RL imagined rollouts** (Dyna, Sutton 1991) do this implicitly; the *explicit tag* has no clean ancestor. Nearest cognitive-science framing: **reality monitoring** (Johnson & Raye 1981) | Reality-monitoring paradigms give a behavioural signature; ablating the tag should **produce confabulation** as a measurable error class | **Departure.** Dyna separates imagined from real by bookkeeping, not by a load-bearing tag whose failure is a named pathology. Keep novel; borrow reality-monitoring as the *validation* lens. |

### Access / broadcast

| REE claim | What it asserts | Nearest formal ancestor | Measurement apparatus | Re-derivation vs departure |
|---|---|---|---|---|
| **SD-064** — capacity-limited selection-for-broadcast bottleneck; contents reportable + causally load-bearing; automatic behaviour bypasses it | Global-workspace-like access channel | **Global Workspace Theory** (Baars 1988); **Global Neuronal Workspace** formalization (Dehaene, Kerszberg & Changeux 1998; Dehaene & Changeux 2011) | The **ignition** signature (nonlinear all-or-none broadcast); **access vs phenomenal** distinction (Block 1995) already cited by SD-064; the **J-lens/J-space** readout (already queued as V3-EXQ-723) | **Re-derivation, well-aligned.** SD-064 explicitly adopts GWT framing. Adopt the ignition metric as the workspace-ablation cliff (Experiment B in `global_workspace_jlens_plan.md`). |

### Ethics / social (mostly V5, mapped for completeness)

| REE claim | What it asserts | Nearest formal ancestor | Measurement apparatus | Re-derivation vs departure |
|---|---|---|---|---|
| **MECH-164** — Axiom V (love) as coordination-preserving trajectory selection; shared/leaked z_beta | Model the other with the same machinery; their affect enters your register | **Mirror / shared-representation** accounts (Gallese & Goldman 1998 simulation theory); **inverse RL / theory-of-mind as inference** (Baker, Saxe & Tenenbaum 2009); **cooperative IRL** (Hadfield-Menell et al. 2016) | Behavioural: does modelling the other's value gradient change committed action toward preserving it? CIRL gives a formal welfare-alignment objective to compare against | **Re-derivation of a hard problem.** The self-other-same-machinery move is simulation theory; CIRL is the nearest formal welfare objective. This is V5 and untested — see WS-10/WS-12/WS-13. |
| **ARC-024** — harm/benefit as asymptotic proxy gradients in world-latent space | Reward as a shaped gradient toward an unreachable limit, not a binary contact signal | **Potential-based reward shaping** (Ng, Harada & Russell 1999); **shaped/dense reward** design | Ng et al. give the *policy-invariance* guarantee for potential-based shaping — a formal check that the gradient does not distort the optimal policy | **Re-derivation.** ARC-024's "gradient not endpoint" is reward shaping; adopt the policy-invariance test to check the CausalGridWorldV2 gradient field is well-formed. |

---

## What should stay novel (no clean ancestor — spend the novelty budget here)

These are the parts of REE with no off-the-shelf formal ancestor. They are the project's genuine contributions and should be developed *as such*, not mapped away:

1. **The residue field** — persistent, non-erasable, owned-consequence traces written at the `z_world` location where a committed action occurred, reshaping the terrain future trajectories are scored against. RL has no primitive for a memory that *cannot* be zeroed, optimised away, or reset between episodes. This is REE's model of guilt/regret/moral learning and has no ancestor in the table above.
2. **The commit boundary + hypothesis tag as a first-class typed object** (MECH-061/MECH-094) — the structural difference between "imagined harm" and "committed harm." Dyna/model-based RL separate imagined from real by bookkeeping; REE makes it a load-bearing boundary whose failure is a *named pathology* (confabulation). The ownership-attaches-at-commit semantics is novel.
3. **The axiomatic ethics derivation** (ARC-043 stack; INV-001 no-ethics-module) — ethics as a *consistency condition* on being a mortal, uncertain, mutually-modelling agent, rather than a reward term or a constitution. No formal ancestor derives ethical objectives from agency+vulnerability+similarity axioms. (This is also the part most in need of adversarial scrutiny — see WS-12/WS-13.)
4. **Three *incommensurable* error channels** (the strong form) — Doya (1999) argues distinct learning *rules* per structure; REE's stronger claim is that the three errors cannot share a scalar objective *at all*. If it survives the forced-shared-loss ablation, that is a novel result, not a re-derivation.

---

## Suggested next actions

- **Per-row `/lit-pull`** to confirm the precise formalism before any row justifies a substrate change; upgrade rows from "hypothesised ancestry" to "confirmed."
- **Priority rows for the current campaign:** MECH-163 (adopt Daw arbitration + two-step task — directly relevant to the competence-floor / WS-1 work) and ARC-007/018 (adopt the SR as the viability-map baseline).
- **WS-5 (active-inference bridge) DONE** (2026-07-09) → [`active_inference_bridge.md`](active_inference_bridge.md): imports the precision / policy-precision / epistemic-value calculus, and states the two exact departures (incommensurable *currency* not cardinality for ARC-021/MECH-069; multi-axis precision for ARC-016). **Feed WS-6** (Bitter-Lesson rebuttal) with the "what stays novel" list — those four items are REE's answer to "why won't scale eat this?"
- Cross-link this doc from the load-bearing claims in `claims.yaml` (a `formal_ancestor:` reference field) so the mapping is discoverable from the registry.
