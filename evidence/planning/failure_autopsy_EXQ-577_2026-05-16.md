# Failure Autopsy — V3-EXQ-577 (gap2_microhabitat_validation)

- **Generated (UTC):** 2026-05-16T22:27:18Z
- **Scope:** single
- **Status:** confirmed (interactive gate answered)
- **Run:** `v3_exq_577_gap2_microhabitat_validation_20260516T210801Z_v3`
- **Queue:** V3-EXQ-577 · **Purpose:** diagnostic · **claim_ids:** [] (no claim weighed)
- **Outcome:** FAIL (all 3 seeds) · `evidence_direction: non_contributory`

## 1. Facts (no interpretation)

Acceptance checks:

| Check | Result | Meaning |
|---|---|---|
| C1 arm0 bit-identical OFF | **PASS** (all seeds) | switch discipline correct; legacy RNG preserved |
| C2 arm1 zone_map_coverage | **FAIL** (all seeds) | strict per-episode structural invariant on `_zone_map` interior |
| C3 arm1 zone-C zero hazard + B>A density | **PASS** (all seeds) | zone weighting reads map correctly (aggregated over resets) |
| C4 arm1 zone-C ambient fires + decays | **PASS** (all seeds) | zone-C detection + `decay^n` correct |

Direct reproduction (seeds 0/1/2, 100 episodes each, current substrate):

| Sub-condition | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| `has_-1` (interior unassigned) | 0 | 0 | 0 |
| `missing_012` (a base zone absent) | **2** | **2** | **3** |
| `extra_codes` (code >=4) | 0 | 0 | 0 |
| `no_3` (zone D absent) | 0 | 0 | 0 |

First failing episodes collapse to `[0,1,3]` / `[0,2,3]` / `[1,2,3]` — **exactly one base
Voronoi zone (0/1/2) fully consumed by the automatic boundary→D (zone 3) promotion** when
the 3 Voronoi seeds land close together. Occurs in ~2-3% of stochastic episodes. `c2_ok` is
a sticky all-100-episodes conjunction, so a single collapse episode marks the whole seed FAIL.

`_build_microhabitat_zones` (causal_grid_world.py:2336) behaves exactly as its docstring
states: nearest-seed Voronoi base assignment, then any cell 4-adjacent to a different base
zone is promoted to zone 3 (ecotone/transition band). A small region entirely within the
boundary band is fully promoted — correct, documented behaviour.

## 2. Claim layer

N/A. `claim_ids: []`. This is an env substrate-readiness diagnostic. Nothing in
claims.yaml is weighed; no demotion/promotion is in scope. `infant_substrate_plan.md`
states **no per-episode "all 3 base zones present" requirement** for GAP-2.

Inconsistency surfaced: `infant_substrate_plan.md` status table (line 373) marks
`GAP-2 ... done | V3-EXQ-577 | 2026-05-16` while the owner validation experiment FAILed.
Governance should reconcile the owner-EXQ to V3-EXQ-577a once it passes.

## 3. Biological-reference triage

GAP-2 = ecological microhabitat heterogeneity: Voronoi niches + an ecotone transition
band (zone D). The mechanism is a **faithful, deliberately stochastic translation**, not
a formal-definition import. A small niche fully absorbed into the ecotone in a minority of
episodes is correct ecology. C2's per-episode determinism demand fights the intended
stochasticity. No `/lit-pull` is warranted (no formal import, no biology divergence).

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | N/A | diagnostic, no claim tagged |
| Biological reference | clear | stochastic Voronoi + ecotone; faithful translation |
| Prerequisites | present | GAP-1 done; GAP-2 mechanism complete |
| Implementation | complete | behaves exactly as `_build_microhabitat_zones` docstring states |
| Environment | adequate | CausalGridWorldV2 contains the intended pressure |
| **Measurement** | **misleading** | C2 `missing_012` per-episode over-constraint incompatible with stochastic seeding |
| Integration | N/A | — |
| Scale | N/A | — |

**Recommended epistemic_category:** measurement / test-design defect (diagnostic
instrumentation) — **not** `substrate_ceiling`, **not** claim pressure. Remains
`non_contributory` to any claim, but is contributory *substrate-readiness* information:
it positively validates GAP-2 (C1/C3/C4) and exposes a false-negative gate.

## 5. Learning extracted

1. GAP-2 microhabitat substrate is functionally validated (C1 switch discipline, C3 zone
   weighting, C4 ambient decay all PASS).
2. Readiness criteria for stochastic env substrate must not demand per-episode determinism;
   assert well-formedness per episode and aggregate properties across episodes.
3. GAP-5 `zone_coverage` (active parallel session) consumes `_zone_map` and must tolerate
   episodes where a base zone is absent — the per-zone key may legitimately have 0 cells.
4. GAP-2 "done" status and EXQ-ISEF / DEV-NEED-001/003/007 / ARC-065 unblocking must not
   be gated on this nominal FAIL.

## 6. Routing (user-confirmed: "Both — enrich + relax")

Dual pathway:

- **/implement-substrate (GAP-2 redraw guard).** Add a degenerate-seeding guard to
  `_build_microhabitat_zones`: after boundary promotion, if fewer than `n_microhabitats`
  base zones survive, redraw seeds (capped retries, deterministic via `self._rng`); on
  exhausted retries keep the best draw and surface a diagnostic. Rationale: the infant
  niche-discrimination curriculum (DEV-NEED-001/003/007, EXQ-ISEF-003) benefits from all
  niches present each episode — defense in depth.
- **/queue-experiment V3-EXQ-577a** (alphabetic suffix — same scientific question, GAP-2
  substrate readiness; implementation/measurement fix per naming convention). Corrected
  C2: per-episode assert well-formedness (no `-1` in interior, codes ⊆ {0,1,2,3}, zone 3
  present, ≥2 base zones); assert all of {0,1,2} present **aggregated over episodes**; and
  **report base-zone-collapse frequency as a diagnostic statistic** (expect near-zero once
  the GAP-2 redraw guard lands; non-zero quantifies residual stochastic collapse).

GAP-5 flag (user-confirmed "Yes"): recorded here and in WORKSPACE_STATE — the GAP-5
`zone_coverage` consumer must not assume all of {0,1,2,3} are present every episode.

## 7. Draft note for governance (do not apply here)

> V3-EXQ-577 (gap2_microhabitat_validation, diagnostic, claim_ids:[]) FAIL is a
> false-negative from an over-strict per-episode C2 invariant: ~2-3% of stochastic
> Voronoi episodes fully absorb one base niche into the ecotone (zone D) by design.
> GAP-2 substrate functionally validated by C1/C3/C4. Superseded by V3-EXQ-577a
> (corrected C2 + collapse-frequency stat) after the GAP-2 redraw guard lands. Not
> claim-weighing; `non_contributory` retained. Reconcile infant_substrate_plan.md
> GAP-2 owner-EXQ to V3-EXQ-577a on its PASS.
