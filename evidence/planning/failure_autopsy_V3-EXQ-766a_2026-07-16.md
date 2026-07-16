# Diagnostic adjudication — V3-EXQ-766a (MECH-232 cloud gate)

- **Generated (UTC):** 2026-07-16T15:31:38Z
- **Scope:** single
- **Status:** confirmed
- **Target run:** `v3_exq_766_mech232_da_modulated_representational_expansion_20260716T152044Z_v3`
- **Queue:** V3-EXQ-766a · **Machine:** ree-cloud-2 · **machine_class:** `linux-x86_64-py3.10` (cloud)
- **Claim:** MECH-232 (hippocampus.da_representational_expansion) · **Purpose:** diagnostic
- **Outcome:** PASS / supports · **Indexer adjudication:** `verified`

## Why this adjudication was owed

This is not a FAIL. It is a **decision-routing diagnostic PASS** whose self-route
(`da_representational_expansion_produces_approach_without_valence_gradient`) gates the
MECH-232 `candidate -> provisional` promotion. Per governance Step 1.5a a gate-clearing
diagnostic PASS must be adjudicated (self-route is a hypothesis, not a verdict), and per
SD-024's design (`docs/architecture/sd_024_da_modulated_rbf_density.md`) the gate is
**cloud-authoritative** — the inline Mac validation was deliberately not treated as the
gate. V3-EXQ-766 PASSed on the Mac (DLAPTOP-4.local) but Mac machine_class cannot serve the
cloud gate; V3-EXQ-766a re-ran the identical, unchanged diagnostic script on ree-cloud-2 to
produce the cloud-class evidence.

## Facts (from the committed flat manifest + coordinator DB)

- **Cloud provenance:** coordinator DB `results` row `V3-EXQ-766a -> PASS, machine ree-cloud-2`;
  committed flat manifest `machine_class: linux-x86_64-py3.10`, `substrate_hash f92a600c…`,
  `seeds [0..7]`, `per_seed` + `arm_results` present, `non_degenerate: true`.
- **Readiness preconditions met** — asserted on the SAME statistic the load-bearing criteria
  route on: `density_read_discriminates` 2.11 ≥ 0.5; `density_walker_functional` 0.917 ≥ 0.8.
- **Non-degeneracy (all three True):** densities positive & vary across seeds; approach varies
  across seeds; DA-ON allocates more centers than DA-OFF (mechanism genuinely active).
- **All four load-bearing criteria pass:**
  - L1a density-expansion ratio **2.40** ≥ 1.5
  - L2a density-approach **0.958** ≥ 0.60
  - L2b above-chance margin **0.958** ≥ 0.20
  - **L2c approach-without-gradient (CRUX):** with every benefit weight zeroed (value field
    removed), the weight-independent density-follower still approaches (0.958) while the
    value-follower falls to chance (0.0).
- Reproduces the Mac 766 run (same discrimination / walker values).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** | test let the claim express itself; the CRUX (L2c weight-zeroing) is a genuine discriminator against a valence-tag account, not a proxy — and it held |
| Biological reference | **clear** | VTA-hippocampal DA representational expansion (Retailleau & Morris 2018; Lisman & Grace 2005; Wittmann 2005). Faithful translation, NOT a formal-definition import — the weight-independent density read IS the mechanism |
| Prerequisites | **present** | SD-024 IMPLEMENTED (2026-07-16); depends_on ARC-007 / SD-004 / MECH-229 satisfied |
| Implementation | **complete** | SD-024 full (residue/field.py RBFLayer+ResidueField, hippocampal/module.py); 1475 pytest + 13 SD-024 contracts pass |
| Environment | **adequate** | non-parametric RBF benefit terrain; representational test needs no env pressure |
| Measurement | **adequate** | readiness asserts the routed statistic (range/discrimination), non-degeneracy checks confirm; no magnitude-vs-range mismatch |
| Integration | n/a | isolated representational test by design |
| Scale | **adequate** | 8 seeds, non_degenerate |

- **recommended_epistemic_category:** `verified` (clean diagnostic PASS)
- **Re-derive brake:** not fired (0 prior substrate_ceiling / non_contributory autopsies on MECH-232)

## Learning extracted

- MECH-232's falsifiable prediction holds on cloud class: DA-modulated RBF **representational
  expansion** — not an explicit positive-valence gradient — is sufficient to produce approach
  behaviour, demonstrated by the weight-zeroing CRUX.
- The cloud PASS reproduces the Mac inline validation, confirming the diagnostic is machine-class
  robust (Regime-A determinism on `linux-x86_64-py3.10`).

## Secondary observation (NOT a blocker; follow-up chip)

The committed `runs/<run_id>/manifest.json` **pack** is thin — empty `metrics.values`, no
top-level `machine_class` / `substrate_hash` — so the index reads `machine_class: null` for
this run even though the committed **flat** manifest carries the full always-core. The phase3
pack-writer producing a thin pack is a pre-existing recording-provenance property, worth an
infra follow-up so the index-scored artifact carries machine_class/substrate_hash directly.
It does not make this gate unauditable (the flat manifest + coordinator DB both record the
cloud provenance).

**RESOLVED 2026-07-16** (REE_assembly `59e9f69f1f`, ree-v3 `7197e9e`). Root cause: the
phase3 run-pack producer `sync_v3_results.build_runpack_docs` never mapped the flat
manifest's always-core provenance (`machine`/`machine_class`/`substrate_hash`) into the
pack, and set `metrics.values` from a top-level `metrics` key that 766-style manifests
don't have (their readouts live under `aggregates`). Systemic: all 2519 packs read
`machine_class: null`. Fix: (1) producer now carries the provenance (conditional-add ->
legacy flats byte-identical) and folds `aggregates` into `metrics.values` when no
top-level `metrics`; (2) `build_experiment_indexes` unconditionally backfills provenance
from the flat sibling onto the pack (independent of the annotation gate; never changes
scoring), so all historical thin packs heal at index time without a rewrite; (3) the two
V3-EXQ-766 packs (+ the V3-EXQ-633 golden fixture) were regenerated on disk; (4)
`validate_recording.check_pack_provenance` flags any pack that drops provenance the flat
carries. This run's cloud pack now carries `machine_class: linux-x86_64-py3.10`,
`substrate_hash f92a600c…`, and 11 metrics.values.

## Routing

**`governance`** — promote **MECH-232 candidate -> provisional**, citing the cloud PASS.
Diagnostic evidence is excluded from confidence scoring; the promotion is the gate-clearing
action, not a confidence increment. Mark V3-EXQ-766 and V3-EXQ-766a reviewed at the governance walk.

### Draft `evidence_quality_note` for MECH-232 (governance to write)

> 2026-07-16: candidate -> provisional. SD-024 diagnostic V3-EXQ-766a (cloud, ree-cloud-2,
> linux-x86_64-py3.10) PASS/supports, adjudication=verified. DA-modulated RBF representational
> expansion produces approach from representational density ALONE: with all benefit weights
> zeroed (value field removed), the weight-independent density-follower still approaches reward
> (0.958) while the value-follower falls to chance (0.0) — the CRUX discriminator against a
> valence-tag account. All 4 load-bearing criteria pass (L1a 2.40>=1.5, L2a 0.958>=0.60,
> L2b 0.958>=0.20, L2c approach-without-gradient); readiness met (density discrim 2.11, walker
> 0.917); non_degenerate. Cloud PASS satisfies SD-024's cloud-authoritative gate; the Mac 766
> run reproduces but is not gate-authoritative. Diagnostic (excluded from confidence scoring).
