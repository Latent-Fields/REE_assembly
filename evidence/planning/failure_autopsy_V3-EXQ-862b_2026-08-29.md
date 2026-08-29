# Failure autopsy: V3-EXQ-862b (Q-040.c dACC PE-weight-delta correlation) — 2026-08-29

**Run:** `v3_exq_862b_q040c_dacc_pe_weight_delta_correlation_20260828T223750Z_v3` · FAIL · evidence-purpose · claims [Q-040] · seeds [42,7,19] · ree-cloud-2 · supersedes V3-EXQ-862a
**Status:** confirmed (interactive gate 2026-08-29; session autopsy-batch-20260829)
**Dry-run check:** clean (no dry citations; target is a full run).

## Facts

The lineage's first non-self-routed, non-degenerate read after three instrumentation failures (475b: z_harm_a never wired; 862: dacc_weight=0; 862a: global 0.85 gate threshold never crossed by z_harm_a's 0.989–1.000 V_s band). All pre-registered gates passed for the first time: P1 3/3, **P1′ z_harm_a-specific holds 3/3** (14/2/32), P2 3/3 both arms, preflight held 3+3, non-degenerate. C4 (OFF-arm null, negative control) passed 3/3. **C3 (ON-arm discrimination, |rho| ≥ 0.3 on ≥2/3 seeds) failed 0/3** — ON rho −0.009/−0.044/−0.116; max |rho| 0.116. Driver's pre-registered branch scored FAIL→weakens; the index consequently held 862b as Q-040's sole genuine experimental entry (weakens, exp_conf 0.324). Recording: complete except an advisory missing `config` block (driver passes None).

## The decisive finding (red-team, independently re-verified)

`bundle["pe"]` reaches the bias vector through exactly one arithmetic path: `control_required = pe * dacc_effort_cost(0.1)` (dacc.py:397), times per-candidate effort (= horizon 10, agent.py:6919-6923), times `dacc_weight` 0.5 — against payoff components `payoffs = -E3.last_scores` of ~500–1800 per candidate. Upper-bound pe-driven std of ‖bias‖ = `0.5·0.1·10·sqrt(32)·std(pe)` = 2.83·std(pe). Recomputed over the manifest's own series: **variance share ≤ 1e-6 in every cell; max direct-path |rho| ≈ 0.0002–0.0010 vs the 0.3 bar.** C3 was arithmetically unreachable whether or not the coupling exists; the observed |rho| up to 0.134 is payoff↔PE covariance (E3-score dynamics), not dACC's weighting of PE.

Secondary, independently sufficient: realized manipulation dose was ~10x below design — z_harm_a holds 0.1–2.9% of eval steps vs the calibration's predicted 15–20% sub-threshold minority. Root cause of the shortfall: the calibration pooled warmup+eval ticks, while eval-phase V_s(z_harm_a) sat almost entirely inside the 0.995–0.999 dead band (refresh counters 1/133/120). ON-vs-OFF bias-magnitude series correlate at **1.0000** in all three seeds (~2e-5 relative reach). Latent confound for any successor: the ON arm's dominant *realized* manipulation was z_beta holds (190/1962, 190/1088 via the retained 0.85 global threshold), which feed E3 scores → payoffs → the DV's dominant component.

## Claim layer

Q-040 (open_question, status open; inferred `answer_state`; decomposed 2026-05-08 into a/b settled by the 490 cohort and c = this lineage). The driver's DECLARED NULL already scopes any FAIL away from a/b. With the DV shown structurally insensitive, the FAIL does not weigh c either: **the claim was never fairly tested.** Biological reference clear and pre-existing (Hayden 2011, Brown & Braver 2007, Treuting 2025; lit_conf 0.806) — no lit-pull owed.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear | test could not let the claim express itself (DV insensitive) |
| Biological reference | clear | coupling grounded at class level; untested here |
| Prerequisites | present | P1′/P2/preflight all genuinely met — first time in lineage |
| Implementation | complete | defect is in the test's DV, not the substrate |
| Environment | adequate | 490-validated regime |
| Measurement | **misleading** | C3 arithmetically unreachable (≤1e-6 variance share); dose 10x under design |
| Integration | coupled | dACC fired every eval step, every cell |
| Scale | adequate | N was never the binding problem |

**Failure-location (GOV-FAILLOC-1): MEASURES FAILED.** Fourth consecutive instrumentation failure, displaced one level deeper each letter (stream → gain → gate → DV). Not chargeable to REE or the claim.

## Disposition (user-confirmed)

- **recommended_evidence_direction: non_contributory** (overriding the pre-registered weakens — the same override the lineage applied at 862a; a pre-registered branch cannot rescue a criterion incapable of firing). Governance must write the manifest correction (weakens → non_contributory + note) and rebuild the index, else the voided direction keeps scoring (the MECH-236 failure mode).
- **recommended_epistemic_category: answer_state** (made explicit; no suppression change).
- **GFLAG-0092**: resolve as OVERTAKEN (its instruction — mark 862a superseded — was mooted by the 2026-08-28 action setting 862a non_contributory; the flag is still open and will keep surfacing until formally resolved).
- **No 862c mandated** (user-confirmed). Requirements recorded for any future letter: (a) pe-isolated readout (bundle already exposes `control_required`/effort term, dacc.py:460-461) or payoff-normalised DV, with an arithmetic-reachability check at authoring time; (b) V_s calibration on eval-phase ticks under `agent.eval()` + a minimum realized-dose precondition; (c) z_beta confound control.

**Granularity-debt trigger: does not fire** (6 lineage targets, none `weakened`; instrumentation debt per the reader's own distribution). **Re-derive brake: does not fire** (0 substrate_ceiling targets tag Q-040; R3 excludes instrumentation categories).

**Routing: governance** (apply direction/category/note; resolve GFLAG-0092; mark reviewed). Step 9b: no ledger action (no fan-out; no registered question adjudicated).

**7b:** 0 fires. **7c:** CONTESTED — contest verified by this session's own recompute and adopted (direction flip); minor findings (seed-42 rho sign flip wording; GFLAG-0092 phrasing) also adopted.

## Learning extracted

1. A discrimination criterion needs an **arithmetic reachability check on its DV at authoring time** — 20 lines over a pilot manifest would have shown 0.3 unreachable before 110 min × 6 cells. One level up from 862a's lesson (preconditions must assert engagement of the slice the DV consumes): the DV must be shown capable of expressing the effect.
2. **Calibrate on the phase you gate**: pooled warmup+eval calibration missed the eval-phase dead-band shift that collapsed the dose. Assert minimum realized dose, not holds > 0.
3. Pre-registration fidelity governs interpretation of a *fair* test, not the fairness of the test itself.
4. z_beta side-manipulation dominance is a live confound for any dose-corrected successor.
5. Recording gap: missing `config` block (advisory) — fix in any future letter.
