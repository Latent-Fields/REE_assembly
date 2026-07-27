# Failure Autopsy — Degenerate constant-vector Spearman DV (SD-081 finding)

**Generated:** 2026-07-27T05:56:41Z
**Scope:** cluster (2 disposition classes, 18 runs)
**Status:** confirmed
**Trigger:** Building SD-081 (MECH-477 dual-system arbitration, ree-v3 `4472811`) confirmed by
measurement that V3-EXQ-786a's recruitment DV was degenerate; a sweep of `ree-v3/experiments/`
for the same guard shape surfaced the runs adjudicated here.

---

## Root cause (shared by both targets)

A rank-correlation dependent variable is computed over an input vector that is **constant by
construction**, past a guard that tests the variance of the **ranks** rather than of the input:

```python
ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
if np.std(ra) == 0.0 or np.std(rb) == 0.0:   # never True
    return None
```

Double-`argsort` of a constant vector returns a permutation of `0..K-1`, whose std is large
(9.23 at K=32), **not** 0. So a constant input sails past the guard and the Spearman is computed
against an arbitrary stable-sort tie-break ordering — i.e. noise with deterministic structure.

**Correct guard is on the INPUT vector**, not its ranks:

```python
if np.std(a) == 0.0 or len(set(a)) < 2 or np.std(b) == 0.0 or len(set(b)) < 2:
    return None
```

Average-ranking ties (all-equal ranks → genuine 0 rank-variance) fixes it structurally as a
side effect, which is why the 16 tie-averaged Spearman helpers in the corpus are already safe.

**Sweep result (34 helpers, none in `experiments/_lib/`):** 18 carry the defective shape
(13 × `_spearman_rho` in the 543 family, `_spearman` in 786/786a, `_spearman_r` in 207/208/210,
and the guard-less inline d² in 071d); 16 average-rank ties and are safe. There is **no shared
`_lib` helper** — the defect propagated by script cloning, so there is nothing to fix centrally.
Full sweep in the session scratchpad `spearman_audit.md`.

---

## Target 1 — V3-EXQ-786 (MECH-163): load-bearing recruitment DV is degenerate

**Run:** `v3_exq_786_mech163_dual_system_recruitment_20260719T163935Z_v3`
**Manifest state:** `outcome: FAIL`; `evidence_direction: non_contributory`; self-route
`substrate_not_ready_requeue` (precondition `familiarity_separation` measured 0.0494 < 0.05, unmet);
load-bearing criterion `C1_recruitment_higher_on_novel` failed; `non_degenerate: True`.
Recording core present (`substrate_hash`, `config`, `seeds`, `machine_class`, `elapsed_seconds`).

### Facts

`_depth_scores` scores every candidate trajectory twice: at full horizon (`full`) and at
`world_seq[:, :1, :]` (`first`). Index 0 of the z_world sequence is the **current state, shared by
every candidate**, so `first` is a constant vector across candidates by construction. The DV is
`recruitment = 1 - rho(full, first)`. With `first` constant, `rho ≈ 0` and the DV reads ≈ 1.0
("full recruitment") regardless of substrate behaviour.

- Per-seed `recruitment_rate` 0.996–1.042, `recruitment_sd` 0.155–0.204.
- Simulated one-side-constant null at K=32: mean +0.005, sd 0.178. The manifest values are
  **indistinguishable from that null** — the DV carries no signal about the claim.
- The manifest's own `candidate_score_range_non_degenerate` precondition (measured 27.49, "met")
  checks the range of **`full`**, not `first`. It structurally cannot detect the constant `first`
  vector, which is why the run self-reported `non_degenerate: True`. The non-degeneracy check is on
  the wrong vector — this is the mechanism by which the defect evaded the run's own guardrails.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (not tested) | The recruitment DV never measured recruitment; the run tested *nothing* about MECH-163. Not weakened, not strengthened. |
| Biological reference | not the failing axis | MECH-163 (dual-system habit/planned recruitment) has a clear cortico-striatal existence proof; the failure is instrumental, not a biology-translation gap. |
| Prerequisites | present | Substrate ran; `substrate_hash` recorded. |
| Implementation completeness | **complete-but-mismeasured** | The measurement, not the substrate, is broken: depth-1 `first` vector constant + rank-variance guard that cannot fire. |
| Environment adequacy | adequate | — |
| Measurement adequacy | **misleading (degenerate)** | Dominant layer. DV = noise indistinguishable from null. |
| Integration adequacy | n/a | — |
| Scale / capacity | n/a | — |

**Dominant diagnosis / recommended epistemic category:** `measurement_test_design_defect`.

### Disposition

- **Confirm `evidence_direction: non_contributory`.** The run already carried it (for the shallower
  familiarity-separation reason); this autopsy establishes the **deeper, independent** reason —
  the recruitment instrument is degenerate regardless of whether the familiarity precondition had
  passed. MECH-163 is **not** weakened.
- **Recommended epistemic category:** `measurement_test_design_defect` (per-claim map records this
  for MECH-163). Under the re-derive brake convention R3 (only `substrate_ceiling` counts), this
  does **NOT** count toward the MECH-163 ceiling tally — an instrument defect is not evidence of a
  substrate ceiling.
- **Routing: superseded-in-lineage; no new queue work.** A repaired successor **V3-EXQ-786b**
  already exists (ree-v3 `2f43287`): it sets `HABIT_DEPTH=2` so the habit/`first` vector spans ≥2
  world-states (not the shared current state), and adds an explicit input-range readiness gate on
  **both** score vectors (`full_range_measured` and `habit_range_measured >= CANDIDATE_SCORE_RANGE_FLOOR`)
  as a second line of defence. The degenerate path is closed by construction + the input gate.
  *Residual hygiene note:* 786b's `_spearman` still carries the unfireable `np.std(ra) == 0.0`
  rank-variance guard — harmless now that the inputs are genuinely non-constant and gated, but it
  should adopt the input-vector guard (see follow-on below).
- **786a re-adjudication is flagged separately and is not duplicated here.**

---

## Target 2 — V3-EXQ-543 family (17 runs, ARC-062): degenerate side-diagnostic, verdicts stand

**Runs (all `*_v3.json` in `REE_assembly/evidence/experiments/`):** 543, 543b, 543c, 543d,
543f×3, 543g×2, 543h×2, 543i×3, 543j, 543k, 543l.

### Facts

`_spearman_rho(flat_drives, flat_in_reef)` where `flat_in_reef` is a per-step 0/1 reef-occupancy
indicator. When an arm **never enters the reef**, `flat_in_reef` is all-zero → constant. **64 of
378 arms** across these runs report `mean_reef_fraction == 0.0` yet still emit a
`rho_drive_vs_reef` reaching **|0.74|**. The magnitude is large (not ~0.02 noise) because
`flat_drives` is temporally autocorrelated, so `argsort` on the all-equal `flat_in_reef` returns a
structured — not random — permutation. Tell-tale: identical values recur across independent
experiments (`0.74072` in 543g/h/i/j; `0.0088` in 543h/i/j/k/l) — deterministic tie-break
artifacts, not measurements.

### The defect is confined and NOT gate-bearing

`rho_drive_vs_reef` is a **reported per-arm diagnostic**. The 543 load-bearing PASS/FAIL gates read
`mean_reef_fraction` and `d4_delta_abs` (`abs(a2.mean_reef_fraction - a0.mean_reef_fraction)`),
**not** the rho (verified in `v3_exq_543k_...py:1677,1710` and the arm-summary block). The 17 runs'
`outcome` and `evidence_direction` do not depend on the degenerate metric.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | ARC-062 verdicts turn on the reef-fraction gates, which are sound. |
| Measurement adequacy | **misleading (confined)** | `rho_drive_vs_reef` is noise on zero-reef arms; all other metrics sound. |
| All other layers | adequate | — |

**Dominant diagnosis / recommended epistemic category:** `measurement_gap` (confined, non-load-bearing).

### Disposition

- **Annotate only — verdicts STAND.** Do **not** re-adjudicate any of the 17 runs'
  `outcome`/`evidence_direction`. The load-bearing gates never read the rho.
- The learning: `rho_drive_vs_reef` on a zero-reef arm (`mean_reef_fraction == 0.0`) is a
  deterministic tie-break artifact and **must not be read as drive–reef coupling** in any narrative
  or synthesis. A reader who cites "drive couples to reef occupancy at ρ=0.74" on such an arm is
  citing noise.
- No brake impact for ARC-062 (measurement category, not `substrate_ceiling`).

---

## Re-derive brake

**Does not fire** for either MECH-163 or ARC-062. Both dispositions are measurement-instrument
categories (`measurement_test_design_defect` / `measurement_gap`), and under convention R3 only
`substrate_ceiling` readings count toward the ceiling tally. Counting a broken instrument as a
ceiling hit would invert the brake's purpose.

---

## Latent (not triggered) — recorded for completeness

- **V3-EXQ-071d** carries the worst *shape* (no guard at all; both-sides-constant → the d² formula
  returns exactly 1.0, which would pass its `rank_corr > 0.90` gate). Its three landed runs report
  `rank_corr = 1.0` at every hazard level, but this is **genuine**: `seq_sig_approach = -0.00012594317`
  vs `batch_sig_approach = -0.00012594280` — near-identical-but-distinct values, real perfect rank
  agreement. Not a false PASS. The false-PASS *path* remains open for a future run whose inputs go
  truly constant.
- **V3-EXQ-207 / 208 / 210** carry the defective `_spearman_r` shape, but their inputs (RSA over
  upper-triangle similarity vectors, n = 40–272; drift-vs-step-index) would need total
  representational collapse to go constant; reported values (rsa 0.03–0.25, order corrs 0.38–0.80)
  show no sign of it. Defect present, degenerate input did not occur.

---

## Learning extracted

1. A degeneracy guard must test the **input** vector, not a post-`argsort` rank vector — rank
   variance of a constant input is maximal, not zero. This is a general instrument-design rule.
2. A run's own non-degeneracy precondition can check the **wrong vector** (786 checked `full`'s
   range while the DV's second argument `first` was the constant one). Non-degeneracy checks must
   cover **every** input the DV consumes.
3. Copy-paste of statistical helpers propagates a latent defect silently. The 18 defective copies
   share no `_lib` home — a canonical guarded helper would have prevented all of them.
4. A degenerate metric can be **confined to a non-load-bearing diagnostic** (543) or can **be the
   load-bearing DV** (786). Adjudication must trace whether the degenerate quantity feeds a gate
   before deciding between "annotate" and "non_contributory".

## Follow-on (chipped — guard-shape hardening)

Add a canonical `experiments/_lib/stats.py` Spearman/rank-correlation helper that guards on the
**input** vector (`np.std(a) == 0.0 or len(set(a)) < 2`), pinned by a contract that feeds in a
constant vector and asserts `None` is returned; migrate the 18 defective call sites (and update
786b's residual unfireable guard). This fixes no past run — it stops the 19th copy-paste. Routed
to `/implement-substrate` via a chip; net-new hygiene work, not part of this adjudication.

## Routing summary

| Target | evidence_direction | epistemic_category | routing |
|---|---|---|---|
| V3-EXQ-786 (MECH-163) | non_contributory (confirm) | measurement_test_design_defect | superseded by 786b (built); no new queue work |
| V3-EXQ-543 ×17 (ARC-062) | unchanged — verdicts stand | measurement_gap (confined) | annotate-only; no re-adjudication |
| guard-shape (18 helpers) | — | — | chip → /implement-substrate (canonical _lib helper + contract) |

`/governance` applies the annotations; this skill produced the diagnosis only.
