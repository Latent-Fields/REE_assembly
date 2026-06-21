# MECH-449 / ARC-107: Go/No-Go eligibility constitution

**Claim ID:** MECH-449 (subject `selection.go_nogo_eligibility_constitution`)
**Status:** IMPLEMENTED 2026-06-21 (substrate; `candidate` / `substrate_conditional` — PROMOTES NOTHING; the falsifier gates promotion)
**Owns:** the core opponency leg (component 1) of the ARC-107 basal-ganglia E3-selector constitution
**Depends on:** ARC-107, MECH-448 (the eligibility envelope this governs), MECH-260 (the existing No-Go this generalises), MECH-439, Q-078
**Grounded under:** ARC-106 (brain-like construction) — grounding synthesis §2.1 (Kravitz 2010 D1/D2 opponency; Mink 1996 focal-go + surround-no-go; Maia & Frank 2011 disorders)

## Problem

F (the primary harm/goal score) monopolises ~88–89% of E3 committed-selection
variance (V3-EXQ-571), unmoved by the full diversity stack. MECH-448 (rank-preserving
F→eligibility demotion) lets F decide *eligibility* rather than the winner — but
the demotion envelope is **order-preserving over F**, so it structurally cannot
*exclude* a candidate that is F-eligible-but-undesirable on a non-F axis
(safety / staleness / perseveration / low viability). V3-EXQ-689f demonstrated
exactly this gap: the live `_f_eligibility_envelope` admits high-F undesirable
candidates that only an active No-Go can suppress. MECH-449 is that active No-Go,
plus the opponent bounded Go.

## Solution

A **bounded Go/No-Go pressure set** over the MECH-448 eligibility envelope, housed
as methods on `E3TrajectorySelector` (the same pattern as `_f_eligibility_envelope`
/ `_gap_scaled_commit_pick` — **no parallel module**, honouring ARC-106 G2). The
gate runs inside the shortlist-then-modulate block **after** the F-built eligible
set is computed and **before** the within-eligible `_modulatory_accum` arbitration:

```
F-merit → MECH-448 envelope → eligible_idx          (pallidal eligibility by strength)
  → MECH-449 No-Go suppress  (safety/staleness/perseveration/low-viability)
  → MECH-449 Go promote      (bounded: re-admit a lawfully-eligible demoted channel)
  → eligible_idx'  → _modulatory_accum[eligible_idx'] arbitration → committed action
```

- **No-Go** (suppress): drop a candidate from the eligible set when any bounded
  axis crosses its floor. The axes act **orthogonally to F-rank** — the property
  rank-preserving demotion structurally lacks. A No-Go'd candidate is removed from
  the eligible set, so the within-eligible argmin **can never select it regardless
  of how large its modulatory pull is** (the SAFETY guarantee).
- **Go** (promote): re-admit, bounded by `gng_go_max_promote`, a candidate that F
  demoted *out* of the envelope whose go-evidence clears `gng_go_threshold` (and
  that is not itself No-Go'd) — lawful channel-specific *access*, not scalar
  F-dominance, decides.
- **Fail-open** (`gng_protect_min_eligible`): No-Go never drops the eligible set
  below this many survivors **unless** they are *safety*-No-Go'd (safety is never
  overridden by the fail-open — a clearly-harmful candidate stays suppressed even
  if it is the last one). Guards the No-Go-over-pressure → catatonia/avolition
  failure pole (grounding §2.1/§2.5) from deadlocking the gate.

### Reuse-before-duplicate (ARC-106 G2)

The **perseveration No-Go axis reuses MECH-260**: the agent routes the existing
dACC anti-recency suppression vector (`_dacc_last_bundle["suppression"]`) in as the
`perseveration` signal — generalising MECH-260 from a (drowned) score-bias into an
eligibility-access gate. No duplicate recency buffer is built. The other axes
(safety / staleness / low-viability / Go) are genuinely new functions MECH-260
lacks; the bounded pressure *set* is the broader constitution the claim names.

### Per-candidate signals

Passed into `select(go_nogo_signals=...)` — an optional dict of `[K]` tensors keyed
`safety` / `staleness` / `perseveration` / `viability` / `go`; a missing axis is
inert. The default waking loop wires only the MECH-260 perseveration reuse; the
MECH-449 falsifier supplies the full constructed-bank axes via
`REEAgent.set_injected_go_nogo_signals(...)`.

## Config (E3Config + `from_dims`, all no-op default → bit-identical OFF)

| Param | Default | Purpose |
|-------|---------|---------|
| `use_go_nogo_constitution` | False | master switch |
| `gng_safety_floor` | 0.5 | No-Go if safety-undesirability ≥ floor (fail-open-immune) |
| `gng_staleness_floor` | 0.5 | No-Go if staleness ≥ floor |
| `gng_perseveration_floor` | 0.5 | No-Go if recency-share (MECH-260) ≥ floor |
| `gng_viability_floor` | 0.1 | No-Go if viability < floor (low-viability) |
| `gng_go_threshold` | 0.5 | Go-promote a demoted candidate if go-evidence ≥ threshold |
| `gng_go_max_promote` | 2 | bounded Go promotions per tick |
| `gng_protect_min_eligible` | 1 | fail-open floor (safety never overridden) |

With the master flag off the entire gate block is skipped → `eligible_idx` passes
through unchanged → bit-identical to the current MECH-448 selector.

## Composition / preconditions

The gate runs inside the shortlist-then-modulate block, so it requires the same
precondition as MECH-448 itself: a modulatory channel must be present
(`_modulatory_accum is not None`). With no modulatory channel there is no
within-eligible arbitration to govern, and the legacy F-argmin path runs (gate
inert). This is the non-vacuity precondition the falsifier enforces (it must
supply the SD-056-trained `e2.world_forward` + ARC-065 GAP-A
`candidate_summary_source=e2_world_forward` divergent pool + a modulatory channel,
else self-route `substrate_not_ready_requeue`).

## MECH-094

Waking committed-selection path only (pure-arithmetic gate over per-candidate
signals; no replay/memory write surface). Call-site-scoped to `select_action`,
identical to the sibling `_f_eligibility_envelope` / `_gap_scaled_commit_pick`
levers (which likewise carry no `simulation_mode` argument).

## Psychiatric failure mode (ARC-106 mandate, grounding §2.1/§2.5)

No-Go over-pressure → perseveration / catatonic action-collapse (the
`gng_protect_min_eligible` fail-open guards the deadlock pole); Go over-pressure →
tics / compulsions / impulsivity; mis-routed context arbitration →
context-inappropriate action (Maia & Frank 2011).

## Validation

`tests/contracts/test_mech_449_go_nogo_constitution.py` (6/6): bit-identical OFF
even with signals passed (C1); No-Go suppresses within the eligible set (C2);
SAFETY holds under overwhelming modulatory pull (C3); bounded Go re-admits a
demoted candidate (C4); composes with the MECH-448 f_demotion envelope (C5);
fail-open never empties the eligible set (C6).

Ablation falsifier (the post-build governance-weighting experiment, queued
separately): on the GAP-A-ready foraging substrate, the built Go/No-Go
constitution must CONVERT ≥1 previously-gated downstream channel beyond what
MECH-448 achieves (over-specification if it does not). Pre-registered: a
built-but-no-conversion result is `non_contributory` / does-not-promote, **not**
an ARC-107 falsification; non-vacuity self-route `substrate_not_ready_requeue` if
the candidate pool is not divergent or Go/No-Go variables do not vary.

## See

ARC-107 design note `evidence/planning/arc_107_selector_constitution_design_2026-06-20.md`
§3.2 + §6b; grounding `evidence/literature/targeted_review_connectome_mech_439/ARC107_GROUNDING_SYNTHESIS.md`
§2.1; MECH-448 `docs/architecture/mech_448_f_eligibility_demotion.md`; MECH-260
(dACC No-Go, `ree-v3/ree_core/cingulate/dacc.py`).
