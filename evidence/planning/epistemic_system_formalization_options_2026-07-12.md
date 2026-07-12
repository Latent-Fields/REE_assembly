# Epistemic-System Formalization — Options Memo

**Status:** ANALYSIS ONLY — un-actioned options memo. Nothing here is built. For the user to decide a direction later.
**Date:** 2026-07-12.
**Scope:** how to improve BOTH the visualization AND the underlying representation of the governance epistemic system (the claims graph + confidence scoring).
**Sibling doc:** [`experimental_recording_standard_2026-07-12.md`](experimental_recording_standard_2026-07-12.md) — the input-quality side of the same coin.

---

## 0. TL;DR

The user's intuition — that the claims graph has latent Bayesian-/Markov-network structure (confidence as posterior; `depends_on`/`emergent_from` as conditional dependence; evidence as likelihood updates; audits as message passing) — is **structurally correct about the skeleton and structurally blocked on one fact**: the `depends_on` graph is **cyclic (132 cycles over 878 claims)**. A directed Bayesian network requires acyclicity and cannot be built over this graph without SCC-collapse or edge re-orientation the data does not license. An **undirected factor graph / Markov random field tolerates the cycles natively** and matches the existing per-node potentials (status + directional evidence) — so it, not a directed Bayes net, is the faithful formal target.

**Recommended direction: Option C (probabilistic-scoring overlay) as the near-term step, architected so it grows into Option B (factor-graph / MRF) as the principled end-state, with Option D's visualization improvements riding along on both.** Reject Option A (directed Bayes net) as topologically mismatched. Full reasoning in §6.

---

## 1. What exists today (grounding — see the survey for file:line)

**The graph.** `docs/claims/claims.yaml` — 878 claims, hand-authored, single source of truth.
- Edge types: `depends_on` (860 claims — the near-universal backbone, but **unweighted, untyped, homogeneous** — a generic "references"); `emergent_from` (32 — invariant-only, a *typed subset* of `depends_on`, semantically the strongest edge: "retract substrate X and this invariant's subject becomes ill-defined" — a genuine conditional-existence relation); `supersedes` (3); closure-plan node `unblocks_claims` / `depends_on` (a *second* graph over GAP-nodes, in `evidence/planning/*_plan.md` frontmatter, joined to claims by `scope_claims`/`bears_on`).
- Typing: `invariant_type` (universal/emergent/grey_zone), `epistemic_category` (gates promotion eligibility), `status` (candidate/provisional/active/stable/…), epistemic stance (shown/believed/asked).
- **Topology: NOT a DAG.** 132 back-edges/cycles; `build_claim_dependency_process.py` already SCC-collapses for display.

**The confidence math** (all in `evidence/experiments/scripts/build_experiment_indexes.py`, computed downstream — NOT stored in claims.yaml):
- `exp_conf = 0.45·consistency + 0.25·volume + 0.20·recency + 0.10·quality` (`:1563`); `lit_conf` a parallel weighting (`:1578`); kept **deliberately decoupled** (exp is load-bearing for promotion, lit is sanity-check).
- Per-entry confidence is a **hardcoded lookup table** (supports+PASS→0.75, mismatch→0.55, non_contributory→0.0, …; `:1467-1494`) — not a likelihood.
- `conflict_ratio = 2·min(supports,weakens)/(supports+weakens)` (`:1506-1513`).
- Hard threshold gates for promote/demote (`:2242-2260`); evidence quadrant split (`:1525`).
- **Confidence is a per-claim scalar computed from that claim's own evidence only. It does NOT propagate along `depends_on` edges at all.** This is the single biggest gap vs. the user's mental model.

**Derive-only constraint** (`.claude/skills/governance/SKILL.md:270-284`). The pipeline regenerates derived files from three hand-authored sources (`claims.yaml`, `decision_log.v1.jsonl`, plan frontmatter) and **never flips a claim's status**. Promotion is a manual claims.yaml edit + a logged decision. Any formalization must be a *derived overlay* that surfaces scores; it may not auto-mutate status.

**Visualization.** Bespoke DOM/SVG, **no graph library** (no D3/cytoscape/force layout). `explorer.html renderGraph` (`:6535`) builds a hand-rolled dependency renderer with ghost nodes for out-of-filter deps; node colour = **3-bucket thresholded stance** (`build_claims_json.py:39,55-78`), not a continuous posterior. `closure.html` renders the GAP-node graph status-coloured. **No confidence distribution, no edge weights, no uncertainty bands are visualized anywhere today.**

### Real vs invented (the load-bearing distinction)

| Ingredient | Status |
|---|---|
| Graph skeleton (nodes, `depends_on`+`emergent_from`+closure edges) | **REAL** — faithful re-encoding, not invention |
| Discrete node states (status, stance) | **REAL** — categorical latent-variable-like |
| Directional evidence attached to claim_ids (`evidence_direction`) | **REAL** — the raw material for factors/likelihoods, machine-readable in `claim_evidence.v1.json` |
| `conflict_ratio` as a sufficient statistic | **REAL** — well-defined support/weaken split |
| One genuinely conditional edge type (`emergent_from`) | **REAL** — structural-zero semantics |
| Edge weights / conditional probabilities | **INVENTED** — `depends_on` is unweighted/untyped; any CPT/potential is assigned, not read |
| Belief propagation across edges | **INVENTED** — confidence is per-node, non-propagating; audits are independent threshold tests, not message passing |
| Evidence as likelihood ratio | **INVENTED** — per-entry confidence is a categorical lookup, not P(e\|H)/P(e\|¬H) |
| Posterior semantics | **INVENTED** — the score is a hand-tuned weighted-linear heuristic |

---

## 2. Option A — Explicit Bayesian belief network (directed)

**What it models.** Each claim is a binary/ordinal latent (true / provisional / false). `depends_on` (re-oriented to causal/evidential direction) becomes a directed edge with a conditional probability table P(child | parents). Experiment/lit entries are observed children with likelihoods P(evidence | claim). Confidence becomes a genuine posterior P(claim = true | all evidence), computed by exact or variational inference. Promotion thresholds become posterior-probability cutoffs.

**What it buys epistemically.** The full prize: calibrated posteriors; automatic propagation (evidence for a substrate claim raises belief in the invariants that depend on it); principled handling of "explaining away"; a single coherent number with probability semantics; the ability to ask counterfactuals ("if MECH-457 falsifies, what happens to the conversion-ceiling cluster?").

**Cost / risk / migration.**
- **Topological blocker (decisive).** The graph has 132 cycles. A BN is acyclic *by definition*. You must either SCC-collapse (losing per-claim resolution inside each strongly-connected component — and some SCCs are large, e.g. the INV-012↔…↔INV-012 loop) or hand-re-orient every back-edge (inventing causal direction the `depends_on` "references" relation does not carry). Both are large, lossy, and contestable.
- **Every CPT is invented.** 860 edges × a conditional table each, with no data to fit them — they'd be hand-set priors masquerading as measured structure. High risk of false precision.
- **Likelihoods must be manufactured** from the categorical evidence lookup.
- Migration burden: very high. New inference engine, a re-orientation pass over the whole graph, calibration data that doesn't exist.

**Coexistence with derive-only.** Possible in principle (compute posteriors, surface them, leave promotion manual) — but the re-orientation of `claims.yaml` edges is either a source-of-truth mutation (violates derive-only) or a parallel hand-maintained edge set (duplication).

**Verdict: reject.** Highest epistemic ceiling, but fights the actual topology and manufactures the most un-grounded structure. The user's "Bayesian" intuition is right in spirit; a *directed* Bayes net is the wrong instantiation of it.

---

## 3. Option B — Factor graph / pairwise MRF (undirected) with loopy belief propagation

**What it models.** An undirected graphical model. Each claim is a node with a **unary potential** derived from its own evidence (essentially today's per-claim `exp_conf`/`conflict_ratio` — reused, not invented). Each edge is a **pairwise potential** encoding "these two claims tend to co-hold" (strong for `emergent_from`, weaker/tunable for `depends_on`). The governance audits become **message passing**: loopy belief propagation over the factor graph iteratively reconciles each node's belief with its neighbours' — exactly the "audit as approximate inference" the user envisioned. Evidence entries are observed factors clamped onto their claim_ids.

**What it buys epistemically.**
- **Native cycle tolerance** — no SCC-collapse, no re-orientation. The 132 cycles are a non-issue; loopy BP is *designed* for cyclic graphs.
- **Belief propagation** — the missing piece. Evidence for a substrate claim now flows to the invariants emergent from it, and conflict in a cluster becomes visible as unreconciled messages.
- **Reuses the real ingredients**: unary potentials = existing per-node scores; observed factors = existing `evidence_direction` entries; the one genuinely conditional edge (`emergent_from`) gets the strongest pairwise potential. Only the pairwise potentials on generic `depends_on` edges are new — and they can start near-uninformative and be tuned.
- Matches the user's MRF intuition precisely and is the **lowest-invention principled formalization**.

**Cost / risk / migration.**
- Pairwise potentials still have to be specified (the one genuinely new thing). But they can be initialised weak/uniform (so B degenerates to today's per-node scoring at t=0) and strengthened only where justified — a graceful, auditable ramp.
- Loopy BP can oscillate / not converge on dense cyclic graphs; needs damping and convergence monitoring. Tractable at 878 nodes but a real engineering surface.
- Interpretability cost: a propagated belief is harder to explain to a human ("why did this claim's confidence move? — because a neighbour's did") than a self-contained per-node score. Mitigate by always showing the unary (own-evidence) belief alongside the propagated one.
- Migration: moderate. New overlay module computing the MRF from claims.yaml + `claim_evidence.v1.json`; no change to sources.

**Coexistence with derive-only.** Clean. The MRF is a **pure derived overlay**: it reads the three hand-authored sources, computes beliefs, and surfaces them. Promotion stays a logged human act on claims.yaml. It never writes back.

**Verdict: the principled end-state.** It is what "Bayesian claim graph with message-passing audits" should actually mean given the cyclic topology.

---

## 4. Option C — Lightweight probabilistic-scoring overlay (YAML stays source of truth)

**What it models.** Keep everything as-is, but replace/augment the weighted-linear heuristic with an explicitly **probabilistic per-node score** — a Beta-Binomial (or logistic) posterior over "claim is supported", where supports/weakens are pseudo-counts, `quality` weights the evidence, and `recency` down-weights old entries. Output a **calibrated posterior mean + credible interval** per claim instead of a point score. Optionally add a *single-hop* propagation diagnostic (a claim's belief is flagged if it is high while a claim it `emergent_from` is low — an "unsupported foundation" alarm) without full belief propagation.

**What it buys epistemically.**
- Turns the magic-number heuristic (0.45/0.25/0.20/0.10) into a model with **explicit priors and uncertainty** — the promotion gate becomes "posterior mean ≥ 0.62 AND credible interval excludes 0.5" rather than a bare threshold. Immediately more honest about *how much* evidence backs a score (2 entries vs 40).
- Uncertainty bands become available to the visualization (Option D consumes them).
- Keeps exp/lit decoupling (two posteriors, not one fused number) — respects the existing Option-E regime.
- The `emergent_from` single-hop alarm captures 80% of the propagation value at ~5% of the cost — it surfaces the "foundation not yet supported" case the user cares about without a full inference engine.

**Cost / risk / migration.**
- **Lowest invention of the three representational options.** It's a swap of the aggregation function inside `build_experiment_indexes.py` (`_compute_claim_confidence`, `:1537-1598`) plus a credible-interval field, not a new graphical model.
- Risk: it's still per-node (no true multi-hop propagation) — a stepping stone, not the end-state. But it is explicitly *shaped* to become B's unary potentials.
- Calibration: to claim "calibrated" honestly you need a validation set of resolved claims to check posterior-vs-outcome. That data is thin (few claims have reached terminal truth). Start with a stated prior and label it "model-based, not yet calibrated".
- Migration: low. One function, additive output fields, no source change, no viz change required (though it enables D).

**Coexistence with derive-only.** Perfect — it *is* the derive step, just with better internals. Promotion stays manual.

**Verdict: the right near-term move.** Highest value-per-unit-risk; architecturally a down-payment on B.

---

## 5. Option D — Visualization-only (no representational change)

**What it models.** Nothing new in the representation. Improve how the *existing* data is seen:
- Replace the bespoke `renderGraph` with a real interactive graph (force-directed or hierarchical), pan/zoom/focus, cluster-collapse for the SCCs (reuse `build_claim_dependency_process.py`'s SCC output).
- **Uncertainty bands / confidence as a continuous visual channel** (node size or colour ramp by `exp_conf`, opacity by evidence volume) instead of the 3-bucket stance.
- **Evidence-flow animation**: when a claim is focused, animate which experiments support/weaken it and along which edges its dependents sit — makes the (currently invisible) evidence structure legible.
- Overlay `conflict_ratio` as a visual property (split-fill nodes).
- A closure-map ↔ claims-graph linked view (the two graphs are joined by `scope_claims`/`bears_on` but never shown together).

**What it buys epistemically.** Legibility, not new inference. The current UI *discards* most of the confidence signal (3-bucket threshold) — even with zero representational change, showing the continuous scores + evidence edges would materially improve how the user reasons about the graph. High perceived value, and it's the most externally-visible improvement.

**Cost / risk / migration.**
- Lowest conceptual risk; bounded frontend work. But real effort: a proper interactive graph over 878 cyclic nodes needs a library (the survey confirms none is currently used) or a careful hand-roll with SCC-collapse for tractability.
- Risk of prettifying a heuristic: nicer bands over a magic-number score can *overstate* rigour. Best paired with C so the bands mean something (credible intervals, not decorated point estimates).

**Coexistence with derive-only.** Trivial — pure read-side.

**Verdict: do it, but ride it on C.** On its own it polishes an un-principled score; on top of C it visualizes honest uncertainty.

---

## 6. Recommendation

**Phase 1 (near-term): Option C + the C-enabled slice of Option D.** Swap the weighted-linear aggregation for an explicit Beta-Binomial/logistic per-node posterior with credible intervals; add the `emergent_from` single-hop "unsupported-foundation" alarm; surface the continuous posterior + interval in explorer.html (replacing the 3-bucket stance colour) and add `conflict_ratio` split-fill. Lowest risk, honest about evidence volume, and every piece is a down-payment on Phase 2. Coexists perfectly with derive-only (it *is* the derive step).

**Phase 2 (principled end-state): Option B (factor graph / MRF) as a derived overlay.** Promote C's per-node posteriors to unary potentials; add pairwise potentials (strong on the 32 `emergent_from` edges, weak/tunable on `depends_on`); run damped loopy BP as the "audit as message passing" the user envisioned. Cycle-tolerant, reuses the real ingredients, invents only the pairwise potentials — and only where justified. Add Option D's evidence-flow animation over the propagated beliefs.

**Reject Option A (directed Bayes net).** The 132-cycle topology makes it the wrong instantiation of the right intuition. The user wants *Bayesian claim graph with message-passing audits*; on a cyclic graph that is an **MRF with loopy BP (B)**, not a directed BN (A).

**Cross-cutting guardrails for whichever path.**
- Everything stays a **derived overlay** — promotion remains a manual claims.yaml edit + logged decision. Never auto-mutate status.
- Keep **exp_conf / lit_conf decoupled** (two posteriors) — the Option-E regime is deliberate and load-bearing.
- Always show **own-evidence belief alongside any propagated belief**, so a human can see whether a score moved because of direct evidence or a neighbour.
- Label uncalibrated model output honestly until a resolved-claim validation set exists.
- The `emergent_from` edge is the one place real conditional structure already lives — start any propagation there, where the semantics are earned.

---

## 7. What this memo does NOT do

Per the request: **nothing here is implemented.** No code, no schema change, no viz change, no claim registration. This is a considered options survey for the user to choose a direction. If a direction is chosen, the natural first artifact is a scoped plan-of-record (`epistemic_overlay_plan.md`) for Phase 1 (Option C), gated on the user picking C-then-B vs D-only vs hold.
