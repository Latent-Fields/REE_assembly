# Epistemic Overlay — Phase 1 Plan-of-Record (Option C + C-slice of D)

**Status:** ACTIVE — Phase 1 implementation. Derive-only overlay. Promotes/demotes nothing.
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
