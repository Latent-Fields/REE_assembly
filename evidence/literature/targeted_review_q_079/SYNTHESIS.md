# Q-079 — DLIF / structured-uncertainty-field novelty drill (R1)

**Date:** 2026-06-20
**Claim:** Q-079 — "Is there a distinct, useful mathematical object (a 'structured uncertainty field' / dynamic latent-scale inference field, DLIF) that jointly provides directed evidence update, cyclic coherence constraint, latent-node birth/death/merge/split, granularity/scale shift, action coupling, precision modulation, offline consolidation, AND residue/non-erasure — or does it collapse to a re-notation of existing formalisms?"
**Status of claim:** candidate, `epistemic_category: out_of_domain`, `version_relevance: v4_v5`, off the v3 strict green-board (target 2026-07-19).
**Drill type:** R1 = the `what_would_answer` novelty falsifier. Literature + derivation, not an REE agent experiment.
**Verdict:** **ANSWERED-NEGATIVE** (the object collapses to a re-notation / engineering synthesis of existing formalisms; the one candidate-distinct ingredient — residue — is not shown separable here, and that separability is ARC-013's open V3-EXQ-587, not a DLIF result).

---

## 1. The four load-bearing capacities (a–d) + residue

The falsifier turns on whether a **single existing formalism** already jointly delivers:

- **(a)** directed evidence update
- **(b)** cyclic coherence constraint
- **(c)** latent-node birth/death/merge/split
- **(d)** granularity/scale shift

…and, for the ANSWERED-POSITIVE branch only, whether **residue/non-erasure** is shown **separable** from salience + uncertainty (pilot HA2 = ARC-013's open evidence path V3-EXQ-587), not merely re-described.

## 2. Coverage matrix (earned cell-by-cell, per the non-degeneracy guard)

`Y` = native/first-class; `~` = partial / needs an explicit add-on; `N` = not provided. Each load-bearing cell is backed by a literature entry under `entries/`; the remaining rows are the research-map formalisms enumerated for completeness (no separate entry needed — their single-capacity scope is uncontested).

| Formalism | (a) directed update | (b) cyclic coherence | (c) birth/death/merge/split | (d) scale shift | residue/non-erasure | entry |
|---|---|---|---|---|---|---|
| **Factor graphs (unified directed+undirected)** | **Y** | **Y** | N | N | N | Frey 2003 |
| Dynamic Bayesian networks | Y | ~ | N | N | N | (research map) |
| Markov random fields | ~ | Y | N | N | N | (research map) |
| **Active inference on factor graphs** | **Y** | **Y** | N (alone) | ~ (fixed depth) | N | de Vries & Friston 2017 |
| **Active inference + structure learning (BMR/expansion)** | **Y** | **Y** | **Y** | ~ | N (prunes — anti-residue) | Smith et al 2020 |
| **Renormalising Generative Models (scale-free active inference)** | **Y** | **Y** | **Y** | **Y** | N (RG discards detail) | Friston et al 2024 |
| Bayesian nonparametrics (sticky HDP-HMM / iHMM) | Y | N | **Y** (unbounded) | ~ (nested) | N | Fox et al 2011 |
| Causal discovery with latents | Y | ~ | ~ | N | N | (research map) |
| Information bottleneck / abstraction | N | N | N | Y | N | (research map) |
| Options / temporal abstraction (RL) | ~ | N | N | Y (temporal) | N | (research map) |
| Probabilistic circuits | Y (tractable) | ~ | N | N | N | (research map; tractability caveat — Vergari et al 2021, NeurIPS) |
| Neural sampling / population codes | Y (impl.) | ~ | N | N | N | (research map) |
| **REE ARC-013 residue** | — | — | — | — | **the only home of residue** | (ARC-013; open V3-EXQ-587) |

### The decisive row

The **Renormalising Generative Model** row is the counterexample to "the gap is the combination." A single, existing framework — hierarchical active inference in its scale-free RGM form, expressed on Forney factor graphs, with structure learning by expansion + Bayesian model reduction — covers **(a)+(b)+(c)+(d)** *and* the three bonus capacities the cluster also wanted:

- **action coupling** — intrinsic to active inference (de Vries & Friston 2017).
- **precision modulation** — precision is inverse variance in the generative model; native.
- **offline consolidation** — Bayesian model reduction is literally an offline "sleep"-like restructuring step in this literature.

So the named prime candidate in the falsifier ("hierarchical active inference") **does** jointly deliver the combination. Capacities (a)-(d) are not a gap.

## 3. The one capacity nothing covers — and why it does NOT flip the verdict

Every surveyed formalism scores **N** on residue/non-erasure. More than that: the two structure-learning mechanisms that buy capacity (c)/(d) — Bayesian model reduction and the RG coarse-graining operator — work by *discarding* redundant detail. They are structurally **anti-residue**. Residue is the genuinely REE-specific commitment.

But the Q-079 falsifier is explicit and was written to forbid exactly this shortcut: residue counts toward ANSWERED-POSITIVE **only if shown separable from salience + uncertainty** (HA2), and that separability is **ARC-013's open experimental question (V3-EXQ-587)** — a REE agent experiment, not something a literature drill can settle. Active inference already contains precision (uncertainty) and salience-weighting; the claim that residue is something *more* than a precision/salience deformation is precisely what is unproven. Until V3-EXQ-587 separates it, residue is **inherited, not added** — it cannot, on its own, constitute a novel mathematical object, and the DLIF re-statement must not be read as independent confirmation of ARC-013 (pilot R2).

## 4. Tractability footnote (does not change the verdict)

Exact inference over a dynamic, cyclic, latent-scale graph is computationally hard; tractability typically demands strong structural restrictions (probabilistic circuits — Vergari, Choi & Van den Broeck 2021; Wang & Kwiatkowska 2023). This is a real *implementation* constraint on any runnable DLIF, but it is an engineering matter, not evidence of mathematical novelty. It bears on the SD-062 utility / repo-build decision, not on Q-079.

## 5. Verdict — ANSWERED-NEGATIVE

The DLIF / structured-uncertainty field is **not a distinct mathematical object**. It is a **re-notation / engineering synthesis** of:

- factor-graph unification of directed + undirected models (Frey 2003) — capacities (a)+(b);
- active inference on factor graphs (de Vries & Friston 2017) — (a)+(b)+action+precision;
- structure learning by expansion + Bayesian model reduction (Smith et al 2020) and Bayesian nonparametrics (Fox et al 2011) — capacity (c);
- scale-free Renormalising Generative Models (Friston et al 2024) — capacity (d) and the full (a)–(d) combination;
- plus REE's ARC-013 residue — the only candidate-distinct ingredient, whose *separability* remains open (V3-EXQ-587).

This confirms the pilot's HA1 (field-first buys representational ergonomics, not new computational power), HA6 (combination-of-known-pieces is a weaker novelty claim than "a new object"), and R1 (treat novelty as the drill's first question — answered: no).

## 6. Recommendation to governance (Q-079 disposition)

1. **Close Q-079 as ANSWERED-NEGATIVE → synthesis note.** Record the equation DLIF ≈ factor-graph active inference + structure learning (BNP / Bayesian model reduction) + RGM scale-free hierarchy + ARC-013 residue. Suggested status: resolve the open question (e.g. `status: superseded`/closed with a synthesis pointer, or retain as `answer_state` with an explicit answered-note), at governance's discretion — Q-079 is `out_of_domain`, so promote/demote gating is suppressed regardless; this lit evidence is informational.
2. **Do NOT build the standalone `structured-uncertainty-fields` repo.** It was gated on ANSWERED-POSITIVE + SD-062 utility; the ANSWERED-NEGATIVE result removes the novelty leg. (A *runnable integration* of these existing pieces with REE's residue channel could still be an engineering artifact — but that is an SD-062 utility decision, not a math-novelty claim, and remains gated.)
3. **Leave ARC-013's V3-EXQ-587 open marker untouched.** Residue separability is the live, inherited question. If — and only if — V3-EXQ-587 later shows residue separable from salience + uncertainty, a *narrow* residue-object sub-question reopens (not the full DLIF). Do not let this drill read as evidence for or against ARC-013.
4. **Keep the field/projection/residue vocabulary** as a thinking aid and as the cross-refs already wired into ARC-084 / ARC-013 / MECH-363 (cluster P1/P2/P3) — no new claims (anti-proliferation).

---

## Sources

- Brendan J. Frey (2003), "Extending Factor Graphs so as to Unify Directed and Undirected Graphical Models," UAI 2003. arXiv:1212.2486.
- Bert de Vries & Karl J. Friston (2017), "A Factor Graph Description of Deep Temporal Active Inference," Frontiers in Computational Neuroscience 11:95. DOI 10.3389/fncom.2017.00095.
- Ryan Smith, Philipp Schwartenbeck, Thomas Parr & Karl J. Friston (2020), "An active inference approach to modeling structure learning: concept learning as an example case," Frontiers in Computational Neuroscience 14:41. DOI 10.3389/fncom.2020.00041.
- Karl Friston et al. (2024), "From pixels to planning: scale-free active inference," arXiv:2407.20292.
- Emily B. Fox, Erik B. Sudderth, Michael I. Jordan & Alan S. Willsky (2011), "A sticky HDP-HMM with application to speaker diarization," Annals of Applied Statistics 5(2A):1020-1056. DOI 10.1214/10-AOAS395. (Foundational HDP: Teh, Jordan, Beal & Blei 2006, JASA.)
- Antonio Vergari, YooJung Choi, Anji Liu, Stefano Teso & Guy Van den Broeck (2021), "A Compositional Atlas of Tractable Circuit Operations for Probabilistic Inference," NeurIPS 2021. (Tractability footnote.)
