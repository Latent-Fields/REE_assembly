# Red-team design review record -- V3-EXQ-1058 (SD-071 instrument-validity evidence run)

**Status: RECORD ONLY. Nothing in this file has been written to `claims.yaml` or any registry.**
It is the verbatim Step 4.5 adversarial design-review output for V3-EXQ-1058, preserved at a
tracked path because the reviewing session ran in a scratch worktree.

- Reviewed script: `ree-v3/experiments/v3_exq_1058_sd071_consolidation_readout_instrument_validity.py`
- Reviewer model: **fable** (model diversity from the authoring session's Opus 5)
- Verdict: **CONTESTED** -- 2 findings, both verified against source by the authoring session
- Run: 2026-09-18, session `science-20260918-sd071-carveout-and-run`, chip `chip-proposal-exp-1206-paced`

## Dispositions applied by the authoring session (every finding got one, in writing)

| # | Finding | Disposition |
|---|---------|-------------|
| F1 | C3's content-scale ladder is a bit-exact sigma-reparameterisation of the injected arm, so it cannot discharge the scale-invariance caveat SD-071 credits it with | **RECORDED, NOT DESIGNED AROUND.** Independently re-verified (rung0.5[i]==rung1.0[i+1], rung0.25[i]==rung1.0[i+2] for i>=1, EXACT on 8/8 of V3-EXQ-778g's recorded seeds). C1/C3 are transcribed verbatim from SD-071's own falsifier; re-scoping either is a governance call, not a queue session's. Raised as **GFLAG-0351** (evidence_discrepancy on SD-071). Also written into the driver docstring and the manifest `interpretation.c3_ladder_is_a_sigma_reparameterisation`. |
| F2 | The sws NULL arm has no sigma-response; its slope is a grid constant times the sigma=0 discontinuity | **RECORDED** alongside F1 (same root cause) in GFLAG-0351, the docstring, and the manifest. |
| F3 | A confounded leg (CI95 entirely above the ceiling) routed to `outcome: PASS` / `evidence_direction: mixed`, contradicting the script's own docstring | **FIXED.** That case now routes `evidence_direction` to `weakens` ahead of the pass cases. `outcome` is deliberately left as the pre-registered rule computes it -- changing the pass rule would change a criterion the claim itself fixes -- so `outcome: PASS` with `direction: weakens` is diagnostic of exactly this case and is named in `interpretation.outcome_vs_direction_note`, with `non_degenerate: false`. |
| F4(a) | C2's requeue branch is unreachable in practice (1e-6 floor sits 4-5 orders below where C1 already fails) | **RECORDED**, not changed: C2 is the correct shape for a denominator guard and its `met` is recomputable. Manifest `interpretation.c2_requeue_branch_reachability_note`. |
| F4(b),(c),(e) | subgroup predicate reuse; frozen-anchor guards add no live protection; z=1.96 vs t(7) | **No defect** -- accepted as accurate and non-actionable; (e) is pre-registered consistency with 778g. |
| F4(d) | `need_seeds` is the realized n; the claim's "n>=8" was never asserted | **FIXED** -- `assert dry_run or n >= 8` added. Cannot fire as shipped (`len(SEEDS) == 8`); it guards a future edit. |
| F5 | The nrem leg's DV is the output of the MECH-121-cluster consolidation pass (Adam), so the carve-out's rationale sentence "cannot bear on MECH-121 even incidentally" is stronger than the source supports | **CARVE-OUT TEXT NARROWED at both sites**, CONDITIONS UNCHANGED: REE_assembly `390ebeec64`, ree-v3 `057bb32b45`. The carve-out's conditions are about TAGGING, and this run tags exactly `["SD-071"]`, tags neither MECH-120 nor MECH-121, and cannot move MECH-121's status. Logged on GFLAG-0351. |
| Family 1 | Does the manipulation reach the DV -- no finding | Accepted. |

---

## Reviewer output, verbatim below this line

# Red-team findings -- V3-EXQ-1058 (SD-071 instrument-validity evidence run)

Reviewer scope: causal chain only (manipulation -> DV -> criterion -> verdict). Facts, not adjudication.
Sources: script `S` = ree-v3/experiments/v3_exq_1058_sd071_consolidation_readout_instrument_validity.py;
harness `H` = ree-v3/experiments/_lib/consolidation_lesion_harness.py;
consolidator `CC` = ree-v3/ree_core/sleep/cross_module_consolidation.py;
778g manifest = REE_assembly/evidence/experiments/v3_exq_sd068_sws_content_scored_readout_diagnostic_20260718T130139Z_v3.json.

---

## F1. C3 (sws content-scale ladder) is a bit-exact sigma-RESCALING of the injected arm. It is produced BY the scale invariance it is pre-registered to discharge. [family 2 + 3; CONFIRMED from recorded data]

Mechanism (all in the harness):
- `H:352-357`: `clean = base * content_scale`; `rms_ref = _rms(base)` (UNSCALED); `damaged = clean + sigma*rms_ref*eps` with `eps` drawn from the same generator state in every cell (fresh agent + `_gen(seed*1009+1)` per cell, `H:1091-1094`). So at rung `cs`: `store(cs, s) = cs*base + s*rms*eps = cs * (base + (s/cs)*rms*eps) = cs * store(1.0, s/cs)`, with the SAME `eps`.
- `H:356-358` `_shy(rows) = mean + (rows-mean)*decay` is homogeneous of degree 1 (no bias) -> commutes with the scalar `cs`.
- `H:411-413` cosine normalises each row -> exactly invariant to the positive scalar `cs`.
- Therefore `errs_cs(s) == errs_1.0(s/cs)` EXACTLY. The ladder rung at content_scale 0.5 is the injected curve sampled at 2x the sigma grid; rung 0.25 at 4x.

Evidence: 778g `arm_results[*].ladder_error_series`, ALL 8 seeds, bit-identical shift (seed 42 shown):
```
rung 1.0 : [0, 0.03477, 0.12187, 0.33046, 0.62135]
rung 0.5 : [0, 0.12187, 0.33046, 0.62135, 0.85094]   <- rung 1.0 shifted one grid step
rung 0.25: [0, 0.33046, 0.62135, 0.85094, 0.98382]   <- shifted two grid steps
```
(`e5[1]==e1[2]`, `e5[2]==e1[3]`, `e5[3]==e1[4]`, `e25[1]==e1[3]`, `e25[2]==e1[4]` -- equality is `==` on the floats, 8/8 seeds.)

What C3 therefore measures: whether the least-squares slope of ONE curve (the injected damage curve) differs when that curve is sampled at grid, 2*grid, 4*grid -- i.e. whether the injected response is GRADED rather than a step. It carries ZERO information about "content AMOUNT" that the injected arm does not already carry, because content amount and 1/sigma are the same coordinate under this readout.

Consequences for attribution:
- `S:174-176` ("C3's ladder is the independent test that the response tracks content AMOUNT, which a pure scale-invariance artifact cannot produce") is false: the ladder IS the scale-invariance artifact, rendered as three re-samplings of one curve.
- The claim's falsifier text ("...collapses below the 0.01 floor, which would reopen the scale-invariance caveat that C3 was pre-registered to discharge") cannot be discharged by this run under ANY outcome. A C3 PASS says "the injected curve is not a step over 4x of grid stretch"; a C3 FAIL says it is. Neither says anything about the caveat.
- C3 CAN still fail (a step-shaped injected curve gives identical rung slopes = 0.3*height), so this is not BLOCKING; it is a criterion that discriminates something other than what the claim and the script say it discriminates.
- The `cached=` reuse (`S:744-751`) is faithful: `sws_only_integrity_at_sigma` reproduces the main sweep's sws cell (dry run: ladder[1.0] == injected_slope_sws == 0.3536746693055377). The units smuggle is elsewhere: the ZERO rung is scored in raw-margin units (`S:561`, `errs = -m`) while positive rungs are in own-`m_clean` units (`S:563`); zero-rung slope 0.03198 vs the same step in injected units 0.03760 (778g s42) -> the recorded-not-gated signal ratio is inflated by 1/m_clean ~ 1.18x. Not gated, so verdict-neutral; record only.

Cheap confirmer: on the completed run, `assert ladder_error_series["0.5"][i] == ladder_error_series["1.0"][i+1]` for i in 1..3 and `["0.25"][i] == ["1.0"][i+2]` for i in 1..2 (full grid). Or re-run the 12-line python check above against the 778g manifest (it passes on 8/8 seeds).

---

## F2. The sws NULL arm has no sigma-response at all. Its "slope" is a grid constant times the sigma=0 zero-store discontinuity. [family 2; CONFIRMED]

- Null store at sigma>0 is `s*rms*eps`; cosine is invariant to `s`, so the null margin is the SAME number at every sigma>0. At sigma=0 the store is exactly zero; `H:411-412` clamps the norm and returns cosine 0 -> margin 0. The null series is therefore exactly `{0, c, c, c, c}`: `null_series_n_distinct_sws == 2` on 8/8 seeds of 778g and 1/1 of the dry run.
- LS slope of a unit step at sigma=0 over `[0,0.25,0.5,1,2]` is 0.3 (over the dry grid `[0,0.5,2]` it is 0.3846). Verified: 778g s42 `0.3*|m_noise|/m_clean = 0.3*0.10660/0.85049 = 0.0376024` == recorded `null_slope_sws 0.0376024`; ratio `0.11585` == recorded.
- So `null_slope_ratio_sws == 0.3*|m_noise| / (m_clean * inj_slope)` identically. `m_noise` (random-store margin, ~-0.11..-0.17) and `m_clean` (~0.85) are store-geometry constants per seed; the ONLY sigma-dependent quantity in the sws C1 ratio is the INJECTED slope. C1 on sws reduces to `inj_slope > 1.2*|m_noise|/m_clean` (~0.15 at s42 constants; recorded inj 0.32-0.36, so ~2.2x headroom).
- The harness set `NULL_MIN_NULL_SERIES_DISTINCT = 2` (`H:1443`, comment `H:1430-1442`) precisely so this two-valued series is NOT flagged degenerate, calling it "a genuine graded response". It is not graded; it is one step.
- Grid dependence: drop sigma=0 from SIGMAS and the sws null slope is exactly 0 -> degenerate. Change the grid spacing and the ratio changes with no substrate change (0.3 vs 0.385 factor). The dry-run 0.2140 is on the 0.385-factor grid at warm 8 and is NOT comparable to the 778g 0.1495 -- do not read it as margin erosion.
- nrem has the same structure in part: the null cell at sigma=0 has loss exactly 0 -> `CC:175-177` skips every step (`n_updates == 0`, dry run) -> null error 0 at sigma=0 by construction. Dry run: null slope 0.01517 with the step vs 0.00342 with sigma=0 set to the sigma=0.25 value -> ~78% of the nrem null slope is the discontinuity. nrem does retain a graded remainder (`n_distinct_nrem` 5 on 778g), so nrem's null is real but small.

Attribution consequence: a C1 FAIL on the sws leg (ceiling inside or above the CI) can arise ONLY from the injected slope falling (a LESS damage-sensitive instrument), never from the null arm "responding to noise" (it cannot). The self-route (`S:980-984`) would label that `consolidation_readout_leg_confounded` / `ceiling_inside_ci95_verdict_unresolved_sws` and `evidence_direction: weakens` -- attributing to noise-confounding a change that is arithmetically a sensitivity loss. Same reading applies (weaker) to nrem. The direction of the artifact is conservative for PASSING (the step inflates the ratio), so a PASS is not manufactured by it.

Cheap confirmer: on the completed run, for every seed check `null_series_n_distinct_sws == 2` and `null_slope_sws == 0.3 * (-integrity_null["0.25"]["sws"]["sws_completion_margin"]) / integrity_injected["0.0"]["sws"]["sws_completion_margin_clean"]` to ~1e-12.

---

## F3. A CONFOUNDED leg routes to outcome=PASS, evidence_direction=mixed -- contradicting the script's own docstring. [family 3; CONFIRMED by trace]

- If a leg's CI95 sits entirely ABOVE 0.25: `ceiling_inside_ci95` is False (`H:1503`) -> `c1_per_leg[leg] = True` (`S:882-885`) -> with C2 and C3 passing, `overall_pass = True` (`S:899`) -> `outcome = "PASS"` (`S:1250`). Direction: `S:998-1000` fails (`ci95_high_below_ceiling` False) -> `S:1002-1005` -> `"mixed"`. Label `consolidation_readout_leg_confounded` (`S:980-981`), `non_degenerate: false` (`S:955-961`).
- `S:190-192` says this case is "SD-071 weakened"; `S:993-995` says "A confounded leg WEAKENS". The code emits `mixed` and `PASS`.
- At n=8 with all seeds C2-eligible, `mixed` is reachable ONLY through this path (ceiling outside the CI with `ci95_high >= 0.25` implies `ci95_low > 0.25`). So `mixed` on this run MEANS "a leg is fully confounded" -- the refuting reading -- while the manifest outcome says PASS.
- Governance weight: `build_experiment_indexes.py:3779` excludes `non_degenerate is False` from scoring, so the run contributes nothing either way. The defect is the human-readable verdict (`outcome: PASS`, `direction: mixed`) on the outcome that the claim's own 0.0..1.0 scale calls "fully confounded".
- Related: a saturated-constant null (ratio exactly 0.0, `null_series_degenerate`) yields CI ⊂ [0,0] -> `ci95_high_below_ceiling` True -> `direction: supports`, `outcome: PASS`, `non_degenerate: false`. Also scoring-excluded, but the text says "supports".

Cheap confirmer: paper trace with `leg_stats["sws"] = {ci95_low: 0.30, ci95_high: 0.35, ceiling_inside_ci95: False}`; or one dry-run assertion that `label == "consolidation_readout_leg_confounded"` implies `outcome == "FAIL"` (it does not today).

---

## F4. Readiness / self-certification checks. [family 4]

(a) C2 floor 1e-6 vs `NULL_MIN_INJECTED_SLOPE = 1e-9` (`H:1425`): ordering is consistent (harness UNAVAILABLE at <=1e-9 -> `_finite` False -> C2 False; 1e-9..1e-6 -> harness ratio computed, C2 False -> requeue). Not self-certifying. BUT C2 is unreachable as a gate in practice: sws C1 already fails at inj_slope < ~0.15 (F2) and nrem C1 at inj_slope < ~0.06 (null slope ~0.015 / 0.25), both 4-5 orders of magnitude ABOVE 1e-6. So `substrate_not_ready_requeue` / `direction: unknown` (`S:978-979, 996-997`) can never fire before `weakens` does. Every reduced-sensitivity outcome is routed as a claim refutation, never as an un-exercised instrument. (This is readiness_anchor.py's own "mirror failure": rule 3, floor orders of magnitude below the criterion's gate.)

(b) `subgroup_ratio_stats(eligible=C2 predicate)` (`S:841-850`): harmless for the verdict. `readiness_ok` requires ALL seeds C2 (`S:888-890`), so any excluded seed already forces FAIL/unknown; the subgroup only changes the reported CI. Exclusion is emitted (`subgroup_n`, `excluded_seeds`). No self-certification.

(c) Anchor guards (`S:652-680`) replay a FROZEN 778g reference through predicates whose floors are 1e-6 (vs reference 0.0967/0.3232), 0.01 (vs 0.1108), 3.0 (vs 6.83). They certify only that the predicates are not unmeetable; they pass identically whether the live run is healthy or dead, by construction. Reference values verified against the 778g manifest (`null_control.injected_slope_nrem` s42 = 0.09671970039873905, matches `S:481`). Adds no live protection; not a verdict defect.

(d) `need_seeds = n` (`S:1265`) is the REALIZED n. The claim's "n>=8" is never asserted. Low severity: SEEDS is a fixed literal and a per-seed exception aborts the run (no partial completion path), so realized == intended unless the file is edited. Cheap fix: `assert dry_run or n >= 8`.

(e) CI95 uses z=1.96 (`H:1497`) at n=8 (t(7)=2.365 would be ~17% wider). Pre-registered as "the same helper 778g used", so consistent; C1 margin under either: ceiling enters the CI when the sws mean exceeds 0.2349 (z) / 0.2318 (t) at sd 0.0218; 778g mean 0.1495 -> ~3.9 sd of headroom.

---

## F5. Bearing on MECH-121 despite not tagging it. [asked explicitly]

The nrem leg's DV IS the output of the MECH-121/273 operator, and its C1 pass is a property of that operator's update rule, not of the readout formula:
- `H:625-633` runs `CrossModuleConsolidator.consolidate(...)`; `CC:162` builds `torch.optim.Adam`; `CC:175-177` skips on exactly-zero loss.
- Arithmetic: under a LINEAR consolidator (plain SGD on MSE) both arms move the same fraction alpha toward their targets, so `gap_after_inj = (1-a)^2|offset|^2 + a^2|n|^2` and `null drift = a^2|n|^2`; the two series differ by a sigma-INDEPENDENT constant, their slopes are identical, and `null_slope_ratio_nrem == 1.0` (fully confounded) by construction. The recorded 0.145 exists ONLY because Adam's per-parameter normalisation makes the step magnitude nearly independent of target scale (plus the zero-loss skip in F2).
- So a nrem PASS is a measurement that "the MECH-121 offline pass, as configured (Adam), moves parameters toward structured content more than toward equal-magnitude noise"; a nrem FAIL would be "the MECH-121 pass consolidates noise as readily as content". Both are statements about the MECH-121 substrate operator. `H:126-129` ("such a run cannot bear on MECH-121 even incidentally") is stronger than the truth for the nrem leg. `claims.yaml:76997-77000` lists MECH-120 and MECH-121 in SD-071's `depends_on`.
- The sws leg does NOT bear on MECH-120 in the same way: `_shy` is linear and cosine is scale-invariant, so SHY's `decay` cancels out of the margin ratio; the sws DV is a property of the cosine readout on the store, not of SHY.
- Condition (ii) keeps MECH-121 out of the indexer's evidence graph. It does not stop a human reader, or an autopsy of a nrem FAIL, from correctly citing the result as a MECH-121 substrate fact. This is not a defect of the script; it is a fact about the measurement the carve-out's wording does not acknowledge.

---

## Family 1 (manipulation reaches the DV) -- no finding

Both arms rebuild the agent and generator per cell (`H:1048-1063`, `H:1091-1094`); `content_scale` enters the sws store at `H:353` and the nrem target at `H:607`; noise scale is referenced to the unscaled content in both (`H:351`, `H:604-605`), so the perturbation is arm-identical. No cache collapses the arms; `cached=` reuse is exact (F1). Path is open on both legs. The only degenerate cells are the null arm's sigma=0 cells (F2), which are degenerate by the manipulation itself, not by a cache.

---

## VERDICT

CONTESTED:
1. `H:352-357` + `H:411-413` (and `S:174-176`, `S:114-120`): the C3 content-scale ladder is a bit-exact sigma-rescaling of the injected arm (`errs_cs(s) == errs_1.0(s/cs)`, 8/8 seeds of 778g, float-equal), so under NO outcome can this run discharge -- or reopen -- the "scale-invariance caveat" the claim says C3 adjudicates; C3 measures only whether the injected damage curve is graded rather than a step. Confirmer: the shift-equality on `ladder_error_series` in the 778g manifest (given above; passes 8/8), or the same assertion on the completed run.
2. `S:998-1005`: a leg whose CI95 lies entirely above the 0.25 ceiling (the claim's own "fully confounded") yields `outcome: PASS`, `evidence_direction: mixed`, contradicting `S:190-192`/`S:993-995` ("weakens"); at n=8 `mixed` is reachable only via this path. Confirmer: paper trace with ci95 = [0.30, 0.35] on either leg.

Supporting (verdict-shaping, not independently contestable): F2 -- the sws null "slope" is `0.3*|m_noise|/m_clean` with no sigma-dependence (n_distinct==2, 8/8), so any sws C1 failure is a sensitivity loss mislabelled as confounding; F4(a) -- the requeue branch is unreachable in practice. F5 -- the nrem leg is a measurement of the MECH-121 operator's update rule (Adam), which the carve-out text says cannot happen.
