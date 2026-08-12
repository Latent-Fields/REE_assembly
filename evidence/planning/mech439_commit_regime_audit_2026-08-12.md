# MECH-439 commit-regime audit of the 9 confirmed `substrate_ceiling` hits

**Date:** 2026-08-12
**Session:** jovial-shannon-35d300 (chip `chip-20260812-mech439-commit-regime-audit`)
**Requested by:** `failure_autopsy_V3-EXQ-925_2026-08-12` (confirmed; REE_assembly `9258c98a3f`), option (b) of its
governance recommendation: *"commission an audit of the 9 confirmed `substrate_ceiling` hits'
`committed_fraction`/temperature configuration before attaching anything."*
**Status:** DERIVE-ONLY. This document is an input to a future `/governance` Step 2b decision. It does not
edit `claims.yaml`, does not attach the V3-EXQ-925 evidence_quality_note, and does not adjudicate MECH-439.

---

## 1. Feasibility correction (read this first)

**The audit as posed in option (b) is not runnable.** `committed_fraction` is a diagnostic that V3-EXQ-925's
causal-replay harness introduced on 2026-08-12; it does not exist in any experiment run before that date.
Grepping all 9 manifests for the literal string `committed_fraction` returns **zero hits in every one**
(verified directly, not inherited from the earlier feasibility probe). There is no `committed_fraction` value
to read for any of the 9 hits, at any temperature, because nothing in the driver scripts or the E3 selector
computed or recorded it at the time these runs executed.

**What this document does instead**, since the literal audit cannot run:

1. Confirms exactly what commit-regime-adjacent information the 9 driver scripts and manifests DO carry.
2. Establishes that one candidate proxy present in every manifest (`committed_class_entropy_nats` and its
   relatives) is **not** a substitute for `committed_fraction` — it measures something structurally different
   (see §3) — a refinement beyond what the originating feasibility probe (session
   `mech357-pressure-scoping-11e9c9`) had established.
3. Classifies each of the 9 runs on the one thing that *is* directly recoverable from source: whether the
   driver script set `use_gap_scaled_commit_temperature` (the one commit-regime-relevant knob that existed at
   the time), and what selection path each run tested.
4. States plainly what this narrower audit can and cannot license governance to conclude.

---

## 2. Background: what the commit gate actually is

From `ree-v3/ree_core/predictors/e3_selector.py`, the primary commit gate (module docstring line 15 and the
live logic near line 3198/3211) is:

```
committed = running_variance < commit_threshold   # or harm_score_variance < effective_threshold, branch-dependent
```

`commit_threshold` resolves from `config.commitment_threshold` (default `0.40`, `ree_core/utils/config.py:682`)
via `variance_commit_threshold()`. This is the gate V3-EXQ-925 measured as `committed_fraction=0.000` at
default configuration (2493 fresh selections, 2 seeds, `use_gap_scaled_commit_temperature=False`,
temperature=1.0) — i.e. the selector spent effectively all measured ticks in the **uncommitted** branch,
sampling from `softmax(-scores/T)`, rather than the committed argmin/gap-scaled-argmin branch.

`use_gap_scaled_commit_temperature` (default `False`, `ree_core/utils/config.py:1325`) does **not** control
whether `committed` becomes `True`. It only takes effect `elif committed:` (`e3_selector.py` ~line 3419 and
~3500) — it softens the **within-commit** pick (hard argmin → gap-scaled multinomial) once the gate has
already fired. Setting it to `True` therefore tells you a run *could* have shown softened committed-selection
behaviour *if and when* the gate fired; it does not by itself tell you the gate ever fired, nor how often.
This distinction matters for how §4's classification should be read.

---

## 3. Why `committed_class_entropy_nats` is not a `committed_fraction` proxy

Every one of the 9 manifests carries commitment-adjacent-sounding fields: `committed_class_entropy_nats`,
`n_unique_committed_classes`, `committed_class_counts`, and (in 3 of the 9) `loop_frac_committed_neq_motor`.
Grepping each driver script for how `committed_class` is computed shows the same pattern in all 9:

```python
committed_class = int(action[0].argmax().item())
```

(689a `e3_exq_689a...py:807`; 700 `:794`; 711 `:893`; 713 `:938`; identical pattern in 700a/700b/700c/700d/709.)

This is **the argmax of the agent's output action vector for that tick** — a label for "which action class the
agent ultimately took" — computed independently of, and blind to, the E3 selector's internal `committed`
boolean or `running_variance`/`commit_threshold` state. I additionally grepped all 9 drivers for any read of
the selector's actual internal gate (`.get("committed")`, `committed_now`, `committed_fraction`, or a bare
`committed =` assignment outside the `committed_class` pattern) and found **zero hits** in any of the 9.

So `committed_class_entropy_nats` measures **diversity of the final selected action class**, which is
producible whether the selector spent that run in the committed branch, the uncommitted (softmax-sampling)
branch, or some mixture of both — the driver-level metric cannot distinguish these. A non-zero entropy here
(and all 9 runs show non-zero entropy, `n_unique_committed_classes` ranging 2-5) tells you the final actions
were not degenerate; it does **not** tell you whether that diversity came from committed argmin/gap-scaled
selection or from uncommitted softmax sampling — both can produce diverse outputs. **This field is a false
friend for the commit-regime question and should not be cited as evidence either way.**

---

## 4. Per-run table

Static config = what the driver script sets. E3 selection path = the mechanism variant each run's own
title/purpose was actually testing (from `use_*` flags in the driver). Manifest content = what commitment-
adjacent field IS present and what it can (not) tell you.

| # | Run | `use_gap_scaled_commit_temperature` | Other commit-threshold override | E3 selection path under test | Manifest commit-adjacent field(s) | Classification |
|---|---|---|---|---|---|---|
| 1 | 689a `mech439_conflict_grade_gapblind_falsifier` | **Varies by arm**: `bool(arm["factor_b"])`. Confirmed-hit arm is `ARM_A1B1_both_on` → **`True`**, T=2.5, `gap_scaled_commit_entropy_alpha=1.5`. Sibling arms `ARM_A0B0`/`ARM_A1B0` → `False`. | none | Modulatory shortlist-then-modulate (`use_modulatory_shortlist_then_modulate=True`, `use_modulatory_selection_authority=True`) — Factor A (shortlist width) × Factor B (commit-T) 2×2 | `selected_entropy_mean` per arm (two_by_two_dissociation): A0B0=0.371, A1B0=0.440, A0B1=0.850, **A1B1=0.387** (confirmed hit) | **explicitly-engages-commitment-lever** (confirmed-hit arm sets the knob), but see caveat below — the knob only fires *if* the gate is already committed; A1B1's entropy (0.387) sits at baseline, not elevated, so even the engaged-lever arm shows no distinguishable commit-branch signature in this proxy |
| 2 | 700 `arc108_sec7_learned_gating_2x2` | absent (library default `False`) | none | ARC-108 §7 F-eligibility demotion + Go/No-Go constitution (`use_f_eligibility_demotion`, `use_go_nogo_constitution`) × learned channel gating/settling 2×2 | `committed_class_entropy_nats` 0.68–1.36 across arms; `n_unique_committed_classes` 2–5 | indeterminate |
| 3 | 700a `arc108_sec7_c3_signed_vs_unsigned_rpe` | absent (default `False`) | none | Same ARC-108 base + signed-vs-unsigned RPE C3 variant | entropy 0.69–1.30; n_unique 3–5 | indeterminate |
| 4 | 700b `arc108_sec7_learned_gating_settling_c3` | absent (default `False`) | none | Same base + settling C3 (signed/unsigned) | entropy 0.56–1.40; n_unique 3–5 | indeterminate |
| 5 | 700c `arc108_sec7_learned_gating_settling_samelayer_null` | absent (default `False`) | none | Same base + same-layer null control | entropy 0.48–1.33; n_unique 3–5 | indeterminate |
| 6 | 700d `..._samelayer_null_retune` | absent (default `False`) | none | Same as 700c, retuned | entropy 0.48–1.37; n_unique 3–5 | indeterminate |
| 7 | 709 `learned_cross_loop_arbitration_validation` | absent (default `False`) | none | Learned cross-loop arbitration (`use_learned_cross_loop_arbitration` A/B) + loop segregation | entropy 0.55–1.20; n_unique 3–5; `loop_frac_committed_neq_motor` 0.19–0.65 present but same false-friend caveat (per-loop label, not the gate) | indeterminate |
| 8 | 711 `ascending_spiral_gain_validation` | absent (default `False`) | none | Ascending spiral gain (target-parity controller), OFF/ON | entropy 0.55–1.20; n_unique 3–5; `loop_frac_committed_neq_motor` 0.19–0.89 | indeterminate |
| 9 | 713 `bounded_parity_controller_validation` | absent (default `False`) | none | Bounded parity controller, OFF/ON (successor to 711) | entropy 0.53–1.20; n_unique 3–5; `loop_frac_committed_neq_motor` 0.14–0.65 | indeterminate |

All 9 manifests: `outcome=FAIL`. Evidence directions: 689a/700b/700d/709/711/713 = `non_contributory`;
700/700a/700c = `superseded`. None carry `committed_fraction`. None read the selector's internal `committed`
gate directly.

**8 of 9 (all except 689a) ran with `use_gap_scaled_commit_temperature` absent from the driver, i.e. at the
library default `False`** — the same default configuration under which V3-EXQ-925 later measured
`committed_fraction=0.000`. This is the strongest fact this audit can state, and it is circumstantial, not
dispositive (see §5). **1 of 9 (689a)** has its confirmed-hit arm explicitly set the knob `True`, but as noted
in the table, this only governs the within-commit pick, not whether the gate fired, and the arm's own
diversity proxy shows no signature distinguishing it from the knob-off baseline.

---

## 5. What this CAN and CANNOT establish

**CAN establish:**
- The literal audit requested by option (b) (`committed_fraction`/temperature configuration per hit) is not
  runnable — the instrumentation post-dates all 9 runs.
- 8 of the 9 runs used the identical default value (`False`) of the one commitment-regime-relevant knob that
  did exist at the time, matching the default under which V3-EXQ-925 later found `committed_fraction=0.000`.
- The 9th (689a) explicitly engaged that knob for its confirmed-hit arm, but the engaged arm's own diversity
  metric shows no distinguishable effect versus the knob-off baseline.
- No driver script, and no manifest, records the selector's actual internal `committed` boolean or fraction
  for any of the 9 runs — the "commit"-named fields present are a different, structurally unrelated metric
  (argmax-of-output-action diversity, not gate state).

**CANNOT establish:**
- Whether the E3 commit gate (`running_variance < commit_threshold`) ever fired `True` during any of the 9
  runs, or what fraction of ticks it was `True` for. **"Ran at the default value of a knob that later, in a
  different experiment, correlated with an uncommitted-dominant regime" does not establish "ran uncommitted."**
  `running_variance` depends on the prediction-error dynamics of each run's own environment configuration,
  candidate pool, and score composition — all of which differ across these 9 runs and from V3-EXQ-925's
  causal-replay setup. The primary gate is independent of `use_gap_scaled_commit_temperature`; a run could
  commit frequently with the knob off, or rarely with it on.
- Whether MECH-439's "committed-selection variance monopoly" framing was actually being tested under a
  committed-selection regime in any of the 9 runs, or under the uncommitted-sampling regime V3-EXQ-925
  documented as the corpus-standard default behaviour. This audit narrows the population of runs that share
  V3-EXQ-925's default configuration; it does not measure their actual commit fraction.
- Any ranking or confidence-weighting among the 9 hits based on commit regime — none of them can be
  distinguished from each other on this axis beyond the single binary (689a's confirmed arm vs the other 8) in
  §4.

**Recommendation for `/governance` to weigh (not applied here):** the honest state after this audit is that
all 9 hits remain **indeterminate** on whether they ran committed or uncommitted — 8 by complete absence of
any recoverable signal, and the 9th (689a) because its one distinguishing config choice governs the wrong part
of the pipeline to answer the question. A regime-matched re-test of a MECH-439 falsifier (the "V3-EXQ-925's
successor letter" option (c) in the autopsy) is the only route that would produce a real answer; a
retrospective audit of the existing 9 manifests cannot.
