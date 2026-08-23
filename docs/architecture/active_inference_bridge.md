---
title: Active-Inference Bridge
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 1
---

# Active-Inference Bridge

**Created:** 2026-07-09
**Status:** first pass (WS-5 of `evidence/planning/ree_ai_design_critique_plan.md`)
**Companion to:** [`formal_ancestor_mapping.md`](formal_ancestor_mapping.md) (ARC-016 row + Arbitration/control section)
**Claims in scope:** ARC-016 (precision-to-commitment), ARC-021 / MECH-069 (three incommensurable error channels)

**Purpose.** REE's control-plane machinery — precision-weighted prediction error, action under uncertainty, exploration as information-seeking — is the free-energy / active-inference program (Friston and colleagues), re-derived from biology. REE's architecture docs pointedly do not cite it and reject its "single functional" framing. This doc does two things: (a) it **imports** the precision / epistemic-value / exploration calculus REE can reuse instead of re-deriving, and (b) it states the **exact** points where REE's design genuinely departs from a single free-energy functional — precisely, not as a blanket rejection. The headline correction: REE's standing "active inference is just one scalar" objection is *partly a strawman*, because active inference optimises a **factorized** objective over a **factorized** state. The defensible departure is narrower and sharper, and it is stated below.

**Sources.** Primary: Parr, Pezzulo & Friston (2022), *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior* (MIT Press); Da Costa, Parr, Sajid, Veselic, Neacsu & Friston (2020), *Active inference on discrete state-spaces: A synthesis* (J. Math. Psych. 99:102447). Supporting, already in the evidence base: Friston et al. (2012) *Dopamine, affordance and active inference* (`evidence/literature/targeted_review_connectome_arc_016/entries/2026-03-28_arc_016_precision_weighting_action_friston2012`); Friston et al. (2015) *Active inference and epistemic value* (`evidence/literature/targeted_review_q_044/entries/2026-05-11_q_044_active_inference_epistemic_value_friston2015`). New entries for this bridge live in `evidence/literature/targeted_review_active_inference_bridge/`.

---

## Part A — The math REE can inherit

Active inference casts perception/learning as minimisation of **variational free energy** and action as minimisation of **expected free energy** `G(π)` over policies `π`, under a generative model that factorises over hidden-state factors and a mean-field approximate posterior `Q(s_1:T | π) = ∏_τ Q(s_τ | π)`. Three components of that calculus map onto REE mechanisms REE currently runs *without* the underlying math.

### A1. Precision as inverse variance → ARC-016's commitment threshold

Active inference weights every prediction error by a **precision** term (the inverse variance of the relevant belief). High precision lets sensory evidence drive updates; low precision lets priors dominate. This is *exactly* the lever ARC-016 built as "E3-derived prediction variance sets the commitment threshold":

- **REE already has:** `commit_threshold = 2 × training_baseline_variance` (EXQ-018b PASS 5/5); a 40% precision drop produces a proportional 40-point commit-rate drop (EXQ-060 confirms the committed-condition beta-gate).
- **What active inference adds:** the closed form and, crucially, the **units** — surprise in nats — so the threshold can be stated as a precision (inverse variance) rather than a tuned constant, and REE can test *deviations* from the active-inference precision update instead of re-deriving both the mechanism and its metric.
- **Already grounded:** Friston et al. (2012) maps precision onto dopamine and is filed against ARC-016 (see source list). This bridge extends that entry from "precision exists as a signal" to "precision is the formal object REE's threshold should be expressed in."

### A2. Policy precision γ → the beta-gate's confidence-to-commit

Active inference selects policies by a softmax over `G(π)` with a scalar gain **γ** — the *precision over policies* — which the framework proposes corresponds to dopaminergic discharge (Da Costa et al. 2020; Friston et al. 2015). γ is the formal analogue of REE's **beta-gate**: the variable that decides how *decisively* a prediction converts to committed action. REE can adopt γ's update (a Gamma-prior precision that rises as expected free energy becomes more discriminating between policies) as the **null model** for its commit gate, and measure where the beta-gate's dynamics depart from it.

### A3. Expected-free-energy decomposition → a principled exploration metric

`G(π)` decomposes into two named, separable terms (Da Costa et al. 2020, verbatim):

- **Pragmatic / extrinsic value** — "the negative of Bayesian risk … when reward is log evidence"; i.e. expected log preference / utility.
- **Epistemic / intrinsic value** — "the expected information gain afforded by a particular policy, which can be about hidden states (i.e., **salience**) or model parameters (i.e., **novelty**) … it is this term that underwrites artificial curiosity."

Minimising `G(π)` therefore yields behaviour that is simultaneously risk-minimising (exploit) and ambiguity-resolving (explore) — the explore/exploit trade-off is *derived*, not tuned. **This is the exploration calculus REE's control plane currently lacks.** Concretely:

- **WS-1 / WS-9 hook:** any intrinsic-motivation or competence-earning mechanism REE builds should be scored against this epistemic-value decomposition (information gain about states = salience; about parameters = novelty) rather than a bespoke curiosity bonus. This connects to the existing `targeted_review_q_044` epistemic-value entry and to `drive_arbitration` (homeostatic active inference, Pezzulo 2015).
- **Governance hook:** where REE claims a "novelty" or "curiosity" or "uncertainty" driver, the active-inference decomposition tells you whether those are three mechanisms or three task-conditional readings of one information-gain term (the Q-044 collapse question). Adopt the decomposition as the null before positing separate substrates.

---

## Part B — Where REE genuinely departs (stated precisely)

This is the heart of WS-5. REE's docs reject active inference on the grounds that it "collapses everything into one scalar." That objection, *as stated*, is partly a strawman. The correction is not to abandon the departure — it is to relocate it to the place it actually holds.

### B0. The strawman, dissolved

Active inference does **not** optimise one undifferentiated scalar. The formalism (Da Costa et al. 2020):

- **factorises the generative model** over distinct hidden-state factors,
- uses a **mean-field posterior** `Q(s_1:T | π) = ∏_τ Q(s_τ | π)` — a product of per-factor marginals,
- and assembles `G(π)` as a **sum of separable terms** (risk + ambiguity; equivalently −extrinsic − epistemic value).

So "active inference can only represent one lumped objective" is false. It optimises a *factorized functional over a factorized state*. **If REE's objection stops at the number of scalars, it attacks a position no serious active-inference practitioner holds** — and REE can factorize objectives inside a free-energy framework without leaving it. The departure must be somewhere else.

### B1. The real departure for MECH-069 / ARC-021 — *commensurability*, not cardinality

Every term of `G(π)` — extrinsic and epistemic, risk and ambiguity — is measured in **nats** and **added together**. Active inference *assumes the value of information and the value of reward share a currency*: `G = risk + ambiguity` is a well-defined single number because both summands are surprise.

That shared-currency assumption is exactly what **MECH-069** denies. MECH-069's claim is not "there are three separate error terms" (active inference has separable terms too). It is the stronger claim that REE's three error channels —

1. **sensory-prediction error** (E1/E2 world-model surprise),
2. **motor-sensory error** (reafference / forward-model mismatch),
3. **harm / goal error** (E3 valenced consequence),

— are **incommensurable**: they have *no common currency at all*, so forcing them through *any* shared scalar mis-attributes credit **even after factorization**. The departure is:

> Active inference: objective is factorized, terms are **commensurable** (summable in nats).
> REE (MECH-069 strong form): channels are **incommensurable** (no shared scalar exists into which their errors can be combined without mis-crediting).

**Evidence that makes this a real, testable claim and not a preference:** V3-EXQ-009 (wider E2 capacity) produced *overfitting, not better harm attribution* — the motor-sensory channel could not learn harm attribution *regardless of capacity*. A single commensurable functional with enough parameters should eventually route harm credit through any channel; an incommensurable-channel architecture predicts it **cannot, at any capacity**. That is the falsifier:

- **Forced-shared-loss ablation** collapsing the three channels onto one scalar objective. If credit assignment fails to converge to the correct attribution *regardless of capacity/training*, MECH-069's strong form is supported. If it succeeds once given enough capacity, the commensurable-EFE null wins and MECH-069 must weaken from "incommensurable" to "usefully separated." (Cross-ref the `three_loop_learning_channels.md` architecture doc and the anatomical grounding in `targeted_review_reafference_streams`, Haak & Beckmann 2018 — three distinct white-matter pathways is the substrate argument *for* non-exchangeability.)

**Why the distinction matters for the project's credibility.** "We reject the one scalar" invites the correct reply "active inference factorizes — you haven't said anything." "We reject the shared currency, and here is the capacity-invariant ablation that would falsify us" is a scientific claim active inference genuinely does not make. Only the second is worth defending.

### B2. The real departure for ARC-016 — *multi-axis* precision

Active-inference precision (including policy precision γ) is a **scalar / low-dimensional gain on a common surprise currency**. It weights a single kind of prediction error more or less strongly. ARC-016 asserts **multi-axis / heterogeneous precision** — distinct precision on functionally-distinct channels — as the substrate of REE's mode regimes (focus / flow / panic / apathy).

That multi-axis structure is **not supplied by the standard formalism**. So it is a second, separate departure — and one REE has *not yet earned*:

> Active inference: one precision currency, gain-modulated. REE (ARC-016): several precision axes that are not exchangeable.

Honesty requires flagging that ARC-016's multi-axis precision is, at present, a **hypothesised enrichment** of the (imported) active-inference precision lever, not a re-derivation of an established one. The obligation ARC-016 incurs by departing here: **show that single-currency, gain-modulated precision cannot reproduce REE's mode transitions.** Until that demonstration exists, the parsimonious null is one precision axis, and the EXQ-396a/b and EXQ-454 calibration troubles (train-variance ≪ eval-variance; commitment threshold never engaging) are a reminder that even the *single-axis* precision circuit is not yet cleanly demonstrated end-to-end in eval. Multi-axis is a claim to test after single-axis precision is solid, not before.

### B3. What stays inside active inference (do not over-claim departure)

To keep the departure precise, note what is *not* a departure and should simply be imported:
- The precision-to-commitment mechanism (A1) — same object, adopt the units.
- The commit-confidence gate (A2) — γ is the null; measure deviation.
- Exploration as information gain (A3) — derive it, don't tune it.
- Separable objectives / factorized state — active inference already does this; REE may factorize freely *without* leaving the framework. Factorization is not the departure; **incommensurability** (B1) and **multi-axis precision** (B2) are.

---

## Part C — Summary table (the two departures)

| REE claim | Active-inference object it maps to | What REE **imports** | The **exact** departure | How to test the departure |
|---|---|---|---|---|
| **ARC-016** — precision→commitment circuit | Precision = inverse variance on prediction error; policy precision γ (≈ dopamine) | Precision units (nats); γ as the beta-gate null; the closed-form precision update | **Multi-axis precision**: several non-exchangeable precision axes vs one gain-modulated currency | Show single-currency precision cannot reproduce focus/flow/panic/apathy mode transitions; until then multi-axis is *hypothesised* |
| **ARC-021 / MECH-069** — three incommensurable error channels | Factorized `G(π)` = risk + ambiguity, summed in nats over a mean-field posterior | The factorized-objective framing itself (REE can factorize *inside* active inference) | **Incommensurability, not cardinality**: no shared currency across sensory / motor-sensory / harm error — vs commensurable, summable terms | Forced-shared-loss ablation: incommensurability predicts credit mis-attribution *regardless of capacity* (cf. V3-EXQ-009); commensurable-EFE predicts success with enough capacity |

**One-line statement of the corrected objection:** REE does not reject a scalar *objective* (active inference has one and it is factorized) — REE rejects a shared *currency* across error types, and a single precision *axis*. State it that way in every doc that currently says "one scalar."

---

## Part D — Cross-links and next actions

- **`formal_ancestor_mapping.md`** — the ARC-016 row and the Arbitration/control section now point here (see that doc's "Re-derivation vs departure" columns). The two departures above are the intended content of those rows' "documented departure" note.
- **`three_loop_learning_channels.md`** — MECH-069 / ARC-021's home doc; the forced-shared-loss falsifier (B1) belongs in its experiment list.
- **Existing evidence to reuse, not duplicate:** Friston 2012 (precision/dopamine, `arc_016` dir); Friston 2015 (epistemic value, `q_044` dir); Pezzulo 2015/2018 and Friston 2017 (`drive_arbitration`, `arc_025` dirs). This bridge adds only the 2022 textbook synthesis and the 2020 discrete-state math synthesis, which are what the equation-level departure argument needs.
- **Feeds:** WS-1 (competence floor) and WS-9 (intrinsic motivation) should adopt the epistemic-value decomposition (A3) as their exploration null; WS-6 (Bitter-Lesson rebuttal) can use B1/B2 as concrete examples of "priors that claim to be load-bearing and how we'd know."
- **Owed:** the two falsifiers (B1 forced-shared-loss capacity-invariance; B2 single-axis-precision sufficiency) are experiment designs, not yet queued. Route via `/queue-experiment` when a competent substrate exists (both are gated on the same competence floor as WS-1). Do **not** queue from this doc.

**Caveat.** This is a first pass built from the two synthesis sources plus the existing precision/epistemic-value entries. The equation-level claims (mean-field factorisation; risk+ambiguity decomposition; γ as policy precision) are quoted from Da Costa et al. 2020; a deeper pull on the continuous-state formulation (generalised coordinates, the Laplace approximation) would be needed before mapping ARC-016's *dynamics* (not just its threshold) onto active inference.
