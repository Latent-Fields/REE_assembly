---
closure_plan:
  id: epistemic_overlay
  generation: meta
  title: "Epistemic Overlay (derive-only probabilistic confidence overlay)"
  registered: 2026-07-12
  last_updated: 2026-07-12
  owner: machinery
  summary: >
    Turns the magic-number confidence heuristic into an explicit probabilistic
    per-node score with uncertainty, as a pure derived overlay on
    claim_evidence.v1.json. generation: meta -> excluded from the V3 closure %
    (epistemic-machinery work, not V3 substrate) and not scanned by
    check_closure_drift (no owner_exq). PROMOTES/DEMOTES NOTHING.
  scope_claims: []
  sibling_plans: []
  nodes:
    - id: PHASE-1
      title: "Phase 1 (Option C + C-slice of D): Beta-Binomial per-node posterior (exp/lit decoupled) + promotion-gate honesty surface + emergent_from single-hop alarm + continuous-posterior visualization"
      status: done
      severity: load-bearing
      last_updated: 2026-07-12
      note: >
        LANDED (REE_assembly master 7edabd57b6). Per-node posterior mean +
        credible interval additive to claim_evidence.v1.json (the unary potential
        a Phase-2 MRF consumes unchanged); promotion-gate honesty surface shown as
        data only (actual gate logic untouched); one-hop unsupported-foundation
        alarm over emergent_from (NOT belief propagation); continuous posterior +
        credible-interval band as the explorer confidence channel. Derive-only.
    - id: PHASE-2
      title: "Phase 2 (Option B): pairwise MRF + damped loopy belief propagation, additive output schema, evidence-flow animation"
      status: in_progress
      severity: high
      last_updated: 2026-07-12
      note: >
        Design + implementation ACTIVE (opened 2026-07-12). Pairwise MRF over the
        earned conditional structure + damped loopy BP beyond the single hop;
        output additive (Phase-1 fields untouched); Option-D evidence-flow viz
        layer. Still derive-only: no status mutation, no auto-promotion, no
        depends_on Bayes-net re-orientation. PROMOTES/DEMOTES NOTHING.
---
# Epistemic Overlay — Plan-of-Record (Phase 1 Option C; Phase 2 Option B)

**Status:** Phase 1 (Option C + C-slice of D) LANDED (REE_assembly master 7edabd57b6). Phase 2 (Option B — pairwise MRF + damped loopy BP) design + implementation ACTIVE (this session, 2026-07-12). Derive-only overlay. Promotes/demotes nothing.
**Date opened:** 2026-07-12.
**Parent memo:** [`epistemic_system_formalization_options_2026-07-12.md`](epistemic_system_formalization_options_2026-07-12.md) — the user picked **Phase 1 = Option C + the C-enabled slice of Option D** (memo §6).
**Sibling doc:** [`experimental_recording_standard_2026-07-12.md`](experimental_recording_standard_2026-07-12.md) — input-quality side; a parallel session (`great-antonelli-05f6c3`) is widening the indexer's consumed-field set concurrently. User approved parallel edits to `build_experiment_indexes.py` on 2026-07-12.

---

## 0. What this delivers (and what it deliberately does NOT)

Phase 1 turns the magic-number confidence heuristic into an **explicit probabilistic per-node score with uncertainty**, adds the **one hop of conditional structure the data already earns** (`emergent_from`), and **shows honest uncertainty** in the explorer — all as a pure derived overlay.

**In scope:**
1. Beta-Binomial per-node **posterior** (mean + credible interval), exp and lit **decoupled** (two posteriors), additive to `claim_evidence.v1.json`. The per-node posterior **is the unary potential** a Phase-2 MRF consumes unchanged.
2. Promotion-gate **honesty surface** — show how the gate *could* read "posterior mean >= 0.62 AND credible interval excludes 0.5". Surfaced as data only; the actual gate logic is untouched; the pipeline stays derive-only.
3. `emergent_from` **single-hop alarm** — flag a claim whose belief is high while a claim it `emergent_from` is low ("unsupported foundation"). One hop only; NOT belief propagation.
4. **Visualization** — continuous posterior + credible-interval band as a visual channel (replacing the 3-bucket stance colour as the *confidence* channel), `conflict_ratio` split-fill, and the own-evidence (unary) belief shown alongside the derived alarm.

**Explicitly OUT of scope (Phase 2 / not now):**
- No Option-B factor graph / MRF, no pairwise potentials, no loopy belief propagation beyond the single hop.
- No re-orientation of `depends_on` into a directed Bayes net (rejected: 132-cycle topology, memo §2).
- No status mutation, no auto-promotion, no clearing of `v3_pending`. **PROMOTES/DEMOTES NOTHING.**
- No change to `exp_conf` / `lit_conf` — they stay for continuity and side-by-side comparison.
- No calibration claim — there is no resolved-claim validation set yet; output is labelled "model-based, not yet calibrated".

---

## 1. Grounding (verified against the live data, 2026-07-12)

| Fact | Value | Source |
|---|---|---|
| Claims with `emergent_from` | **34** | `docs/claims/claims.yaml` |
| Total `emergent_from` edges | **62** | (memo said 32 — undercount; use 62) |
| Claims with evidence entries | **479** | `evidence/experiments/claim_evidence.v1.json` |
| Per-node scoring function | `_compute_claim_confidence` | `build_experiment_indexes.py:1537-1598` |
| Per-entry confidence lookup | `_experimental_entry_confidence` | `:1467-1494` |
| conflict_ratio | `_direction_conflict_ratio` | `:1506-1513` |
| Claim summary assembled | `_summarize_claim_entries` (has the FULL entry list) | `:1601-1688` |
| Promotion gates | `candidate_to_provisional` etc. | `:2242-2260`, gate logic `:2843-2906` |
| Explorer already fetches `claim_evidence.v1.json` and merges per-claim fields | merge block | `explorer.html:8687-8709` |
| Viz stance colour = 3-bucket threshold | `resolve_epistemic_stance` | `build_claims_json.py:39,55-71` |
| Derive-only constraint | never flip status | `.claude/skills/governance/SKILL.md:270-284` |

**Key architectural fact:** `_summarize_claim_entries` receives the full ordered entry list for a claim, so the posterior can be computed over *all* entries (not just the `recent_entries[-5:]` slice). The explorer already merges `claim_evidence.v1.json` per-claim — so new posterior fields ride the existing merge with near-zero plumbing.

---

## 2. The per-node posterior (unary potential) — the model

**Object:** for each claim, two independent Beta posteriors over P(claim is supported): one from experimental entries, one from literature entries. Kept decoupled (Option-E regime — memo guardrail).

**Pseudo-counts from directional evidence.** Each entry contributes a weighted vote:
- `supports` -> alpha (+w)
- `weakens`  -> beta  (+w)
- `mixed`    -> split: +w/2 to alpha, +w/2 to beta
- `unknown` / `non_contributory` / `inconclusive` -> **excluded** (w=0) — matches the existing scoring exclusions (`:1471-1473`).

**Per-entry weight** `w = quality * recency`:
- `quality` = the entry's own `confidence` (already computed: `_experimental_entry_confidence` for exp, `lit.confidence` for lit) in [0,1].
- `recency` = `max(recency_floor, 1 - age_days/horizon)`, horizon **90d exp / 365d lit** (reuse existing horizons at `:1560,:1575`), `recency_floor = 0.25` so old evidence is down-weighted, never fully discarded.

**Prior.** Uniform `Beta(1,1)` — deliberately weak. With little evidence the posterior mean is pulled toward 0.5, which is the whole point: 2 entries must not look like 40. Prior stated explicitly in output metadata.

**Posterior.** `Beta(alpha_0 + sum_support_w, beta_0 + sum_weaken_w)`.
- **mean** = alpha / (alpha + beta).
- **credible interval** = 95% equal-tailed (quantiles 0.025 / 0.975) via the regularized incomplete Beta inverse.

**No new dependency.** `build_experiment_indexes.py` must run in the governance pipeline without scipy. The Beta quantile is computed with a self-contained regularized-incomplete-beta (`_betai`, continued-fraction, Numerical-Recipes-style) inverted by bisection. ASCII-only prints.

**Additive output** into each `claims[cid]` block of `claim_evidence.v1.json`:
```
"exp_posterior": {"mean","ci_low","ci_high","alpha","beta","n_support_w","n_weaken_w","n_entries"},
"lit_posterior": {"mean","ci_low","ci_high","alpha","beta","n_support_w","n_weaken_w","n_entries"}
```
plus a matrix-level `"posterior_model"` block: `{"family":"beta-binomial","prior":"Beta(1,1)","ci_mass":0.95,"recency_horizon_days":{"exp":90,"lit":365},"recency_floor":0.25,"calibration":"model-based, not yet calibrated"}`.

`exp_conf`, `lit_conf`, `overall_confidence` are **untouched**.

---

## 3. Promotion-gate honesty surface (data only)

The current candidate->provisional gate is `exp_conf >= 0.62 AND >=2 entries AND conflict_ratio <= 0.35 AND >=1 supporting` (`:2848-2853`). Phase 1 **surfaces an alternative reading without applying it**:

> posterior_gate = (exp_posterior.mean >= 0.62) AND (exp_posterior.ci_low > 0.5)

Emitted per claim in the overlay as:
```
"posterior_gate": {"mean","ci_low","ci_high","ci_excludes_half":bool,
                   "would_promote_candidate_to_provisional":bool,
                   "agrees_with_current_heuristic":bool}
```
This is **informational**. `recommendation` in `promotion_demotion_recommendations.md` is NOT changed; no status flips. It lets a human see, per claim, whether the honest-uncertainty gate would agree with the point-threshold gate — the "how much evidence backs this" signal the heuristic hides.

---

## 4. The `emergent_from` single-hop alarm (the one earned edge)

`emergent_from` carries structural-zero semantics: "retract substrate X and this invariant's subject becomes ill-defined". So a claim believed while its foundation is not is a genuine epistemic smell.

**Rule (single hop, no propagation):** for each claim C with parents P = `emergent_from`:
- child belief `b_C` = C's exp_posterior.mean (own-evidence unary; fall back to lit if no exp).
- for each parent p: parent belief `b_p` = p's exp_posterior.mean.
- **`unsupported_foundation` fires** when `b_C >= HIGH` (0.62) AND some parent has evidence with `b_p <= LOW` (0.45) — the foundation is *contradicted/weak*, not merely untested. Record `{weakest_parent, parent_mean, gap}`.
- **`untested_foundation` (softer, separate flag)** when `b_C >= HIGH` AND some parent has **zero** evidence entries — the foundation is unshown, not disproven. Distinguished on purpose: absence of evidence != evidence of absence.

Both are advisory diagnostics. Neither changes any status or recommendation.

**Phase-2 seed:** this join (child posterior x parent posterior over `emergent_from`) is exactly the first pairwise potential a Phase-2 MRF strengthens. The alarm module is where loopy BP later grows; the unary potentials it reads (§2) do not change.

---

## 5. Module layout (grows into Phase 2 without a rewrite)

| Layer | File | Role | Phase 2 growth |
|---|---|---|---|
| **Unary potentials** | `build_experiment_indexes.py` (§2 helper + additive fields in `_summarize_claim_entries`) | per-node Beta posteriors into `claim_evidence.v1.json` | unchanged — MRF reads these as unary potentials |
| **Graph overlay** | **NEW** `scripts/build_epistemic_overlay.py` | reads `claim_evidence.v1.json` + `claims.yaml`; emits `docs/assets/data/epistemic_overlay.json` with per-claim {posterior mirror, conflict_ratio, posterior_gate} + `emergent_from` alarms + metadata | pairwise potentials + damped loopy BP grow HERE; single-hop alarm becomes the first message |
| **Visualization** | `explorer.html` (`renderGraph:6535`, claim table) | continuous posterior + CI band, conflict_ratio split-fill, alarm badges, own-evidence belief alongside derived signal | evidence-flow animation over propagated beliefs (Phase 2 / Option D) |

**Derive-only compliance:** every writer reads only hand-authored sources (`claims.yaml`) + already-derived files (`claim_evidence.v1.json`) and writes only derived outputs (`claim_evidence.v1.json`, `docs/assets/data/epistemic_overlay.json`) + the viz. No hand-authored source is mutated. `build_epistemic_overlay.py` is added to the governance pipeline after `build_experiment_indexes.py` and `build_claims_json.py`.

---

## 6. Visualization plan (C-enabled slice of D)

- **Confidence channel:** node fill/border encodes `exp_posterior.mean` on a continuous ramp (was: 3-bucket stance). A **credible-interval band** (mean +/- via ci_low/ci_high) is drawn as a secondary channel (e.g. a thin uncertainty bar / lightened halo) so a wide interval reads as "little evidence" at a glance. Stance (shown/believed/asked) is retained as a separate glyph/legend, not conflated with confidence.
- **conflict_ratio split-fill:** nodes with directional conflict render a split fill proportional to `conflict_ratio` (support vs weaken), making unreconciled evidence visible.
- **Own-evidence alongside derived:** wherever an `emergent_from` alarm badge appears, the node also shows its own-evidence (unary) belief, so a human sees whether the flag reflects direct evidence or the foundation join. (Guardrail: never show a derived signal without the unary one beside it.)
- **Honesty label:** a visible "model-based, not yet calibrated" note wherever posteriors are surfaced.
- Bump `EXPLORER_VERSION` stamp (line 2). Restart `serve.py` on :8000 (or a spare port) to verify before landing.

---

## 7. Build order / checklist

1. [ ] Plan-of-record (this doc). **Land first.**
2. [ ] `build_experiment_indexes.py`: `_beta_binomial_posterior` helper + self-contained `_betai`/quantile; additive `exp_posterior`/`lit_posterior` fields in `_summarize_claim_entries`; matrix-level `posterior_model` metadata. Keep textual footprint minimal (parallel session editing same file).
3. [ ] Regenerate `claim_evidence.v1.json` (run the indexer in the same mode governance uses); verify new fields present, `exp_conf`/`lit_conf` unchanged.
4. [ ] `scripts/build_epistemic_overlay.py`: emit `docs/assets/data/epistemic_overlay.json` (posterior mirror + conflict_ratio + posterior_gate + emergent_from alarms + metadata). Smoke-run; verify alarms fire only where earned.
5. [ ] `explorer.html`: continuous posterior + CI band + conflict split-fill + alarm badges + honesty label; merge overlay fetch; bump EXPLORER_VERSION.
6. [ ] Verify on a spare-port `serve.py`; screenshot proof.
7. [ ] Land `REE_assembly` on `master` (Session Land Protocol). Reconcile any collision with `great-antonelli-05f6c3` on the shared file.

---

## 8. Guardrails (restated — non-negotiable)

- **Derive-only.** No status flip, no `v3_pending` clear, no auto-promotion. Overlay reads sources, writes derived only.
- **exp/lit decoupled.** Two posteriors, never a fused number.
- **Own-evidence always shown beside any derived/alarm signal.**
- **Honestly uncalibrated.** Labelled "model-based, not yet calibrated" until a resolved-claim validation set exists.
- **ASCII-only** in any `.py` stdout; timestamps from `date -u`.
- **Phase-2-ready.** The per-node posterior is B's unary potential; the alarm module is where loopy BP grows. No throwaway scaffolding.

---
---

# Phase 2 Plan-of-Record — Option B (pairwise MRF + damped loopy BP)

**Status:** ACTIVE — grows `build_epistemic_overlay.py` in place (NOT a rewrite). Derive-only. Promotes/demotes nothing.
**Date opened:** 2026-07-12.
**Parent memo:** `epistemic_system_formalization_options_2026-07-12.md` §3 (Option B), §6 (recommendation). Phase 1 landed the unary potentials; Phase 2 adds the pairwise potentials + belief propagation the memo names as the principled end-state for a **cyclic** claims graph (an MRF with loopy BP — NOT a directed Bayes net, which the 132-cycle topology rejects, memo §2/§6).

## P2.0 What Phase 2 adds (and still does NOT do)

Phase 1 gave every node an honest per-node posterior but confidence still **does not propagate** — the single biggest gap vs the user's mental model (memo §1). Phase 2 makes the claims graph a genuine **undirected pairwise Markov random field** and runs **damped loopy belief propagation** so evidence for a substrate claim flows to the invariants emergent from it, and a weak foundation transitively drags down everything built on it.

**In scope (Phase 2):**
1. **Pairwise potentials** on the graph edges — the ONLY invented objects. Strong + directional on the 62 `emergent_from` edges; weak/near-uniform/tunable on generic `depends_on`. At the weak defaults the MRF degenerates to Phase-1 per-node scoring (t=0 recovery).
2. **Damped loopy sum-product BP** over the full 880-node graph (132 cycles tolerated natively — no SCC-collapse, no edge re-orientation). Convergence + oscillation monitoring, per channel.
3. **Propagated beliefs** emitted alongside the unary (own-evidence) belief, exp/lit kept decoupled (two BP runs, two propagated numbers, never fused).
4. **Evidence-flow animation** (Option D viz layer) over the propagated beliefs in `explorer.html`.

**Still explicitly OUT (unchanged from Phase 1):**
- No directed Bayes net, no edge re-orientation, no SCC-collapse (Option A — rejected on topology).
- No status mutation, no auto-promotion, no `v3_pending` clear. **PROMOTES/DEMOTES NOTHING.**
- No fusing of exp and lit into one belief.
- No calibration claim — still labelled "model-based, not yet calibrated".
- The propagated belief NEVER feeds the promotion gate; the honesty surface (§3) stays keyed to the unary posterior.

## P2.1 The MRF model

**Nodes.** All N=880 claims (every `id` in `claims.yaml`), not just the 479 with evidence. A claim with no evidence is a **connector node** with a uniform unary that still passes messages between its neighbours — this is how propagation reaches through the graph. Each node is a binary latent `X_i in {0=unsupported, 1=supported}`; the belief we report is `b_i = P(X_i = 1)`.

**Unary potentials — REUSED, not recomputed (guardrail).** For each node, `phi_i = (1 - m_i, m_i)` where `m_i` is the **existing** Beta posterior mean from `claim_evidence.v1.json`. Two **decoupled** channels, each run separately:
- **exp channel:** `m_i = exp_posterior.mean` if `exp_posterior.n_entries > 0`, else `0.5` (uniform — no own experimental evidence).
- **lit channel:** `m_i = lit_posterior.mean` if `lit_posterior.n_entries > 0`, else `0.5`.

exp is load-bearing (it is what gates promotion); lit is the sanity channel. They are **never** combined into one number — Phase 2 runs BP twice and emits two propagated beliefs, honouring the Option-E decoupling regime.

**Pairwise potentials — the ONLY invented objects (initialise weak; strengthen only where justified).**

- **Generic `depends_on` edge** (an edge NOT also `emergent_from`): a symmetric associative (Potts/Ising) coupling
  ```
  psi_dep(x_i, x_j) = exp(+w_dep) if x_i == x_j        (agree)
                      exp(-w_dep) if x_i != x_j        (disagree)
  ```
  with `w_dep` **small** (default **0.15** — near-uniform). **At `w_dep = 0` the potential is the all-ones matrix, the MRF factorises into the product of unaries, and `b_i == unary_i` exactly** — i.e. it degenerates to today's per-node scoring. `w_dep` is a documented, tunable knob. `depends_on` carries no measured strength (memo §1: "unweighted, untyped, homogeneous"), so it MUST stay near-uniform until something licenses more.

- **`emergent_from` edge** (child C `emergent_from` parent P): a **directional** potential encoding the structural-zero semantics — "retract substrate P and C's subject becomes ill-defined" — by penalising the single incoherent corner `(C = supported, P = unsupported)`:
  ```
  psi_ef(x_C, x_P) =            x_P=0        x_P=1
                     x_C=0 [    1.0          1.0    ]   child unsupported: consistent with either parent
                     x_C=1 [  exp(-w_ef)     1.0    ]   child supported: parent-unsupported penalised
  ```
  with `w_ef` **strong** (default **1.6**). This is exactly the Phase-1 single-hop "unsupported foundation" alarm promoted to a pairwise factor: it becomes the FIRST BP message and now propagates **multi-hop** (a weak foundation drags down the whole cluster emergent from it, transitively). The potential is intentionally **non-symmetric** — a supported child pulls a parent up only weakly, but an unsupported parent pulls a supported child down hard (parents can hold without their emergents; emergents cannot hold without their parents). Undirected message passing is well-defined on a non-symmetric potential: the two directed messages simply use the two argument orders.

**Degree normalization (regularization — added at implementation, honestly disclosed).** Raw loopy BP on this graph saturates: a hub with ~78 `depends_on` neighbours floods to belief ~1.0 even at `w_dep = 0.15`, because weak associative pushes compound multiplicatively with degree — the classic loopy-BP overconfidence pathology. Since `depends_on` is precisely the "unweighted, untyped, homogeneous" catch-all (memo §1), letting hub-degree dominate is exactly wrong. So each edge's coupling is **degree-normalised** (a symmetric normalised-adjacency `D^{-1/2} A D^{-1/2}`-style scaling), by **type-specific** degree:
- `depends_on`: `w_eff = w_dep / sqrt(dep_deg_a * dep_deg_b)` — bounds each node's dependency-coupling budget so hubs do not saturate.
- `emergent_from`: `w_eff = w_ef / sqrt(ef_deg_a * ef_deg_b)` — `ef_deg` is usually 1-3, so a child with few foundations keeps a strong pull while a hub-foundation with many emergents does not saturate.

This preserves the `w=0 -> per-node scoring` degeneracy (verified: at `w_dep=w_ef=0` the max `|propagated - unary|` is ~1e-15, converging in 1 iteration) and turns propagation into a **gentle refinement** (with the tuned defaults: exp-channel median delta ~0.004, p90 ~0.04, max ~0.25; biggest movers are foundational substrate claims where dependency structure genuinely carries signal) rather than a saturation. The normalization is recorded in the output `mrf.pairwise[*].degree_norm`.

Only the pairwise potentials (and their degree normalization) are new. Everything else (unary potentials, evidence entries) is reused unchanged. This is the memo's "lowest-invention principled formalization" (§3).

## P2.2 Damped loopy belief propagation

**Sum-product BP.** For each directed edge `i -> j`:
```
m_{i->j}(x_j)  proportional to  sum_{x_i} phi_i(x_i) * psi_ij(x_i, x_j) * prod_{k in N(i)\j} m_{k->i}(x_i)
```
Beliefs:
```
b_i(x_i)  proportional to  phi_i(x_i) * prod_{k in N(i)} m_{k->i}(x_i)
```
All messages are 2-vectors normalised to sum 1; the reported propagated belief is `b_i(1)`.

**Damping (oscillation control).** Update in message space with damping factor `lambda = 0.5`:
```
m^{t+1} = (1 - lambda) * m_computed + lambda * m^t
```
Damping is the standard mitigation for loopy-BP oscillation on cyclic graphs (memo §3 names this as the real engineering surface).

**Convergence + oscillation monitoring.** Iterate to `max_iters = 200` or until `max over all directed edges |m^{t+1} - m^t|_inf < tol = 1e-6`. Track the per-iteration max-delta; if it never crosses `tol` AND is non-monotone / rising over the last window, set `oscillating = true`. Emit `{iterations, converged, final_max_delta, oscillating}` **per channel**. A non-converged channel still emits its propagated belief but flags it `converged=false` so downstream never silently trusts it.

**Cycle safety.** The 132 cycles are handled natively — loopy BP is *designed* for cyclic graphs; no SCC-collapse, no re-orientation (that was Option A). Because the default couplings are weak (`w_dep = 0.15`, and `emergent_from` is only 62 of ~3200 edges) the influence graph is near-tree-like and converges in a handful of iterations at 880 nodes; convergence is verified and reported rather than assumed.

## P2.3 Output schema (additive; Phase-1 fields untouched)

Per **evidence-bearing** claim entry in `overlay["claims"][cid]` (own-evidence must exist so the guardrail "own-evidence shown beside propagated" holds):
```
"exp_propagated": {"mean", "delta_vs_unary", "n_neighbors"}   # ONLY if exp_posterior.n_entries > 0
"lit_propagated": {"mean", "delta_vs_unary", "n_neighbors"}   # ONLY if lit_posterior.n_entries > 0
```
A node with only lit evidence gets `lit_propagated` beside its lit unary and NO `exp_propagated` (decoupled). A connector node with no evidence gets neither attached (nothing to show a propagated belief *beside*) — it still participates in message passing.

Top-level `overlay["mrf"]` block:
```
{"model": "pairwise-mrf-loopy-bp",
 "pairwise": {"emergent_from": {"coupling": w_ef, "form": "directional; penalizes child-supported-while-parent-unsupported"},
              "depends_on":   {"coupling": w_dep, "form": "symmetric-associative (near-uniform); w=0 -> per-node scoring"},
              "note": "only pairwise potentials are invented; unary = existing Beta posteriors, reused unchanged"},
 "bp": {"damping": lambda, "max_iters", "tol", "states": ["unsupported","supported"]},
 "convergence": {"exp": {...}, "lit": {...}},
 "graph": {"nodes", "depends_on_edges", "emergent_from_edges"},
 "movers": [{"id","channel","unary","propagated","delta"} ...],   # largest |delta|, for the animation + inspection
 "calibration": "model-based, not yet calibrated"}
```
`counts` gains `beliefs_moved_exp` / `beliefs_moved_lit` (nodes with `|delta| > 0.01`).

## P2.4 Evidence-flow animation (Option D viz layer)

In `explorer.html renderGraph`, when a node is focused (anchor mode):
- Animate belief flow along the focused node's **in-edges** from evidence-bearing neighbours — an SMIL dot travels each edge toward the focused node, coloured by the neighbour's own-belief direction (green if unary > 0.5, red if < 0.5). `emergent_from` in-edges animate thicker/stronger (they carry the strong potential).
- The focused node's posterior bar gains a **second tick = propagated mean**, with the unary tick retained beside it so the delta is visible at a glance (guardrail: own-evidence always shown beside propagated).
- `overlaySummaryHtml` gains a "Propagated (exp): X (unary Y, delta)" line, only where a propagated belief exists.
- Honesty label ("model-based, not yet calibrated") retained wherever propagated beliefs surface.

## P2.5 Build order / checklist (Phase 2)

1. [x] Plan-of-record extension (this section). **Land first.**
2. [ ] `scripts/build_epistemic_overlay.py`: add `_build_graph`, pairwise-potential builders, `_loopy_bp` (damped, per-channel, convergence/oscillation report); attach `exp_propagated`/`lit_propagated` to evidence-bearing entries; emit top-level `mrf` block + `movers`. Keep ALL Phase-1 code (posterior mirror, conflict split, posterior_gate, single-hop alarm) intact.
3. [ ] Smoke-run: verify both channels converge, `w=0` sanity (propagated == unary), alarms unchanged, Phase-1 fields byte-stable except the additive blocks.
4. [ ] `explorer.html`: propagated tick on the posterior bar + summary line + table hint; evidence-flow animation on focus; honesty label; bump `EXPLORER_VERSION`.
5. [ ] Verify on a spare-port `serve.py`; screenshot proof.
6. [ ] Land `REE_assembly` on `master` (Session Land Protocol).

## P2.6 Guardrails (Phase 2 — restated)

- **Derive-only.** Reads `claims.yaml` + `claim_evidence.v1.json`; writes only `docs/assets/data/epistemic_overlay.json` + the viz. No source mutated. PROMOTES/DEMOTES NOTHING; the promotion-gate honesty surface stays keyed to the **unary** posterior, never the propagated one.
- **exp/lit decoupled.** Two BP runs, two propagated numbers, never fused.
- **Own-evidence always shown beside any propagated belief.** Propagated beliefs are attached ONLY to nodes that have own evidence in that channel.
- **Cycle-native.** MRF + loopy BP over the 132-cycle graph; no re-orientation into a DAG.
- **Honestly uncalibrated + convergence-flagged.** Labelled "model-based, not yet calibrated"; a non-converged channel is flagged, never silently trusted.
- **Weak by default.** Pairwise potentials initialise near-uniform (`w_dep=0.15`); the MRF recovers Phase-1 per-node scoring at `w=0`. Strengthen only where the semantics are earned (`emergent_from`).
- **ASCII-only** `.py` stdout.
