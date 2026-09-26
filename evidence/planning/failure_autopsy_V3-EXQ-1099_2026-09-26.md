# Failure autopsy -- V3-EXQ-1099 (v3_exq_1099_contamination_truncation_extension_probe_20260925T182543Z_v3)

- Generated: `2026-09-26T10:19:36Z` | Status: **confirmed** (2026-09-26T10:43:53Z, user at /failure-autopsy Step 8 interactive gate (session failure-autopsy-20260926-batch7))
- Batch: failure-autopsy-20260926-batch7 (V3-EXQ-1105a/1067/1106/1107/1099/1104/1090)
- Claims: (claim-free) | audited: INV-054, MECH-106, MECH-427
- bears_on: GFLAG-0304, sd094_contamination_footgun_exposure
- Recommendation ledger: rec-20260926-614b94c8
- Dry-run gate: scripts/check_dry_run_citations.py run over all 7 2026-09-25 diagnostic run_ids of this batch: 0 dry, 7 clean.

## 1. Self-route and failed criterion

Self-route `historical_verdicts_not_reproduced_adjudicate_drift_first`; failed criterion: **absolute**.

Does the self-route hold? partially -- the run-level label understates a between-arm finding: on today's substrate, seed-paired, 231a STOCK is FAIL/weakens and gated OPTOUT is PASS/supports, so the gate alone flips today's verdict (the sensitivity branches are only reached when ready is True, so the label never says so). But drift is ALSO live in both arms: OPTOUT does not reproduce April's magnitudes (positive-history latency 0.0 vs 2-3; negative 187-201 vs 22; ratio ~194 vs 7-11) -- 'reproduction' is a 2-field (outcome, direction) test. April's own per-seed values (da_pos 0.82-0.88, probe commits at steps 2-22 on 4/5 seeds) do not look materially truncated, so this is a sensitivity of the DESIGN on today's (STAY-heavy, modal share 0.45/0.77) substrate, not proof that the April evidence was contamination-driven.

## 2. Facts (re-measured from the flat manifest and driver)

- **INV-054**: 278 and 435 truncated (stock death frac 1.0) but verdicts robust and reproducing -> phase-2 scope cleared, no re-run owed
- **MECH-427**: 883 insensitive_by_construction (DV structurally 0 in the exposed arm) -> not answerable by this instrument; converges with the pre-existing R4 disposition (_z_goal_parent has no consumer)
- **MECH-106**: 231a's DESIGN is contamination-sensitive on today's substrate (paired flip). The gate is inert on 231a's DV-carrying PROBE/HARD envs (num_hazards 2/5), where 950/950 episodes died in BOTH arms; an env-only simulation (red-team) shows contamination roughly halves survival there anyway.
- **231a_already_inadmissible**: Independently of contamination, 231a was already inadmissible for MECH-106: C2 is an arithmetic consequence of C1 (GFLAG-0163), the claim's behavioural prediction was sign-inverted (GFLAG-0164), and the valence bias lives in the driver, not ree_core. The driver compared today's stock arm against the raw April PASS without those corrections.
- **positive_control**: stock walker dies 20/20, gated 0/20 -- the gate works
- **provenance**: top-level seeds [0] is a placeholder (targets ran 3-5 seeds each), as in 1080; substrate_stable_across_run false from a mid-run checkout update on ree-worker-3 (per-cell hashes agree)

## 3. Four-layer diagnosis

| Layer | Reading |
|---|---|
| claim_alignment | n/a -- claim-free contamination audit. |
| biological_reference | n/a -- environment-hygiene instrument. |
| prerequisites | present -- gate validated by positive control. |
| implementation | complete -- the gate zeroes contamination_spread in hazard-free envs as specified. |
| environment | partial -- the gate only acts on hazard-free envs; 231a's probe/hard envs (hazarded) carry contamination deaths in both arms, outside the gate's reach. |
| measurement | partially misleading -- readiness requires every answerable claim to be 'covered', so a single target already known to be inadmissible (231a) fails the run and suppresses its own sensitivity finding at run level; baseline derivation ignored standing governance corrections to 231a. 278's criterion is pinned by construction under this manipulation (stock latency 1/1/3 at the floor; PASS needs >50; the gate can only speed recovery) yet the manifest labels it could_discriminate -- the P2-5 mislabel shape; only 435 carries the INV-054 reading. |
| integration | isolated. |
| scale | adequate per target. |

**Failure location (GOV-FAILLOC-1):** mechanism established, measures partial, environment partial, REE failed: False. Net: MEASURES + ENVIRONMENT (routing structure, stale 231a baseline, 2-field reproduction test, gate out of reach on hazarded probe envs), not chargeable to REE.

## 4. Biological reference

n/a -- divergence: n/a; lit: n/a.

## 5. Recommendations

- evidence_direction: `non_contributory`; epistemic_category: `standard` (note: claim-free audit)
- **INV-054** (audited): annotate (red-team wording): V3-EXQ-1099 (2026-09-25): phase-2 recovery windows of 278/435 were 100% contamination-truncated at stock settings (window loss 68%) and 0% gated; both verdicts stayed FAIL/does_not_support and recovery got FASTER when gated (278 latency 1.67 -> 1.0, 435 onset 2.0 -> 1.0), so the footgun cannot have produced the negative verdict. 278's criterion is non-discriminating under this manipulation (already at floor); 435 carries the reading. Phase 1 (where depression is established; 150/150 episodes died in both arms) is outside the gate's reach and unmeasured. No contamination re-run owed for phase 2; not a clearance.
- **MECH-106** (audited): annotate: 231a's design is contamination-sensitive on today's substrate (seed-paired stock FAIL/weakens vs gated PASS/supports), and its probe/hard envs carry contamination deaths the gate cannot reach. This does not add admissible evidence either way: MECH-106 already has none (GFLAG-0163 degenerate C2; GFLAG-0164 sign inversion; valence bias in the driver). Under the corrected sign, today's OPTOUT PASS is the wrong direction. OVERRIDES the manifest's per_claim_disposition verdict_sensitive_rerun_owed: no 231a re-run is owed. Any re-measurement is a redesign (substrate-resident valence bias, corrected sign, non-degenerate criteria) with contamination_spread = 0.0 on EVERY env, not only the gate on hazard-free ones.
- **MECH-427** (audited): annotate: 883 is insensitive_by_construction to contamination; the pre-existing R4 disposition stands.
- Substrate queue: ```{
 "action": "none"
}```
- Re-derive brake: {'fired': False, 'threshold': 2, 'note': 'claim-free'}

## 6. Routing

**governance** -- Governance-note-only: three annotations (texts above), no re-runs; resolve the 231a coupling-detector chip as done on the empirical answer.


## 7. Hypothesis-space ledger (Step 9b)

No registered question names this run or its claims and no fan-out was emitted: nothing to register.

## 8. Learning extracted

- A seed-paired between-arm verdict flip isolates the manipulation on today's substrate; it does not by itself say the historical run was affected -- check the historical per-seed values.
- A 2-field (outcome, direction) reproduction test hides large magnitude drift.
- A 'could_discriminate' label derived from 'determinable and not insensitive' mislabels a criterion pinned at its floor (278).
- The hazard_free_contamination_gate does not reach hazarded envs; contamination deaths there persist in both arms.
- chip-20260925-exq1099-231a-coupling-detector is discharged EMPIRICALLY: the run demonstrated coupling for 231a (da_pos 0.985 -> 1e-5, verdict flipped), answering P2-6. Recommend governance resolve it done (not withdrawn), citing this run, since GFLAG-0496's resolution names it.

## 9. Checks

- Step 7b pre-routing checks: no fires
- Step 7c red-team (Step 7c red-team run on fable (cross-model; drafter opus)): {'model': 'fable', 'verdict': 'CONTESTED (narrow)', 'applied': 'all four findings applied: drift-in-both-arms, gate out of reach on hazarded envs, INV-054 not a clearance (red-team wording adopted), chip discharged empirically not by inadmissibility; manifest per_claim_disposition override stated', 'file': 'redteam_C.md'}

Granularity-debt recurrence trigger: does NOT fire (no target in any of this run's claim clusters reads `weakened` with structurally different signatures attributable to this run; this run's own claim_alignment is n/a / could-not-express).
