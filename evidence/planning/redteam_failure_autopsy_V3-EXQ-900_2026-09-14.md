# Red-team verification: failure_autopsy_V3-EXQ-900 draft (GFLAG-0246)

**Generated:** 2026-09-14T12:22:35Z
**Method:** manifest and driver read first; every load-bearing number recomputed from
`per_seed_rows` before the draft was opened; then draft .md/.json, Krishnan 2022 and
Duvelle 2019 `summary.md`, `REEAgent.update_z_goal` (agent.py:11571-11670),
`RBFLayer.add_residue_cluster` / `compute_local_density` (field.py:182-292),
`ResidueField.accumulate_benefit` (field.py:694-743), GFLAG-0246 text, SD-024
`what_would_answer`, driver git history.

## VERDICT: CONTESTED

The draft's headline answer to GFLAG-0246's literal ask -- "the flat
`mean_benefit_magnitude` split does NOT falsify SD-024" -- is CORRECT and I confirm it
(Section 2). But two of the things the autopsy ASSERTS on the way to that answer are wrong
against the artifact's own cells and the cited sources, and both would change the text the
autopsy recommends landing in `claims.yaml` (`recommended_evidence_quality_note`), one
four-layer grade, `narrow_supports_flag`, and the content of the residual test it endorses.
Neither is hygiene. Each has a one-command confirmer (Section 4).

- **Defect A (gate that cannot discriminate by construction, graded "adequate").** C2 is not
  a test of "functional": it is computed on `density_delta`, which is identically 1.0 for
  every single-center event and is `n x mean-kernel-at-jitter` for a cluster -- an arithmetic
  consequence of `compute_local_density`'s kernel sum, and exactly the statistic the P0
  readiness sweep (R2) already certifies. The pre-registered form of C2, `rho(cluster_size,
  density)`, measures **0.177 on this manifest, below the 0.30 bar**; the driver's own comment
  records that it was swapped to the delta after a pre-queue probe found 0.18 on a 57-event
  live sample. The draft praises the swap as "a genuinely careful design choice" and rests
  its central "functional is already operationalised and passing" argument on C2. GFLAG-0246's
  original reading ("nothing in the rule tests the functional half") is substantially right.
- **Defect B (inference on an unstated premise / literature over-read).** The draft calls the
  flat split "a confirmed prediction from the existing evidence record" (Krishnan, Duvelle).
  The Krishnan summary says nothing about magnitude-independence (it supports the SD-012
  `benefit x drive` scaling). The Duvelle summary predicts value-INSENSITIVITY *of biology*
  and explicitly says that if REE's density scales with `benefit_magnitude` "that is a
  divergence from the biology" -- and the substrate formula (`n = 1 + int(ben * drive *
  40)`) commits to exactly that scaling. The run has no `benefit_magnitude` variance (CV
  1.6%) so it confirms nothing either way; the draft itself says the split "carries no
  information ... by construction" three paragraphs earlier. A zero-information statistic
  cannot be a confirmed prediction. The `recommended_evidence_quality_note` would write this
  inversion into the claim record.

## 1. Load-bearing numbers recomputed from `per_seed_rows`

| Quantity | My recompute | Draft / manifest | Match |
|---|---|---|---|
| pooled n benefit events | 57 (16 / 13 / 28 by seed 11/23/37) | 57 | yes |
| cluster_size distribution | {1:51, 2:2, 3:1, 4:1, 5:1, 8:1}; n>=2 = 6; mean 1.3158; max 8 | same | yes |
| C1 Spearman(dopamine_signal, cluster_size) | 0.53272 | 0.53272 | yes |
| **C2 Spearman(cluster_size, `density`)** | **0.17748** | not reported | **manifest's C2 is NOT this** |
| C2 Spearman(cluster_size, `density_delta`) | 0.51660 | 0.51660 (labelled "cluster_size_vs_density") | matches the delta only |
| mean benefit_magnitude, cs>=2 / cs==1 | 0.557726 / 0.558248 | 0.5577 / 0.5582 | yes |
| benefit_magnitude range, all 57 | [0.5300, 0.5736]; CV 1.61% (pop) / 1.62% (sample) | [0.530, 0.5736], "CV ~1.5%" | yes (1.5 vs 1.6, immaterial) |
| dopamine_signal range, all 57 | [0.00530, 0.18149], 34.2x | [0.0053, 0.1815], 34x | yes |
| dopamine_signal / benefit_magnitude (= drive_level) | 7 discrete values {0.01,0.04,0.05,0.09,0.15,0.22,0.32}; the 6 expansion events sit at {0.05,0.09,0.09,0.15,0.22,0.32}, all 51 singles at 0.01-0.04 | "drive_level supplies essentially all of the 34x range" | yes -- confirmed, not a confound |
| Spearman(cluster_size, benefit_magnitude) | -0.010 pooled; -0.134 (s11), n/a (s23, all cs=1), +0.026 (s37) | flat | yes; no seed tells a different story |
| `density_delta` for the 51 single-center events | min 0.9999995, max 1.0000019 -- **51/51 within 2e-6 of 1.0** | not examined | see Defect A |
| `density_delta` per allocated center, expansion events | 0.503, 0.503, 0.479, 0.450, 0.528, 0.547 (i.e. ~0.49 = exp(-16 x 0.3^2 / 2)) | not examined | see Defect A |
| expansion events whose delta <= single-center 1.0 | 1 of 6 (cs=2, delta 0.958); a second at 1.094 | not examined | see Defect A |
| per-seed C1 / C2(delta) | s11: 0.575 / 0.699; s23: degenerate (0 expansions); s37: 0.609 / 0.491 | pooled only | consistent with pooling; seed 23 contributes nothing to C1/C2 |
| leave-one-out on the 6 expansion events | C1 -> 0.495 (any drop); C2(delta) -> 0.444 (drop any cs>=3) or 0.713/0.449 (drop a cs=2) | not examined | both stay above 0.30; PASS is LOO-robust on its own DV |
| C4 | 1403 harm calls = 1403 add_residue, 0 add_cluster (519+225+659) | same | yes |
| driver commit date vs run start | f871d95b 2026-08-08 10:20:41 UTC; run started 10:22:49 UTC | -- | single commit; DV swap predates the run by 2 min |
| `what_would_answer` commit date | ada5d97af0 2026-09-06 20:27 +0100 | "2026-09-06, predates flag (2026-09-09)" | yes |

The draft's arithmetic is sound everywhere it did arithmetic. The defects are in what it did
not recompute (C2 on the pre-registered column; the single-center delta) and in what it
inferred.

## 2. What the draft gets RIGHT (confirmed, in both directions)

- `benefit_magnitude` is the env reward at contact (`causal_grid_world.py:2219,2257`:
  `resource_benefit * amp [+ proximity_benefit]`), passed as `intensity`; `dopamine_signal
  = benefit_exposure * drive_level` (agent.py:11665-11669). `cluster_size = 1 + int(da *
  40)` (field.py:227). Since benefit varies 1.6% and drive 32x, a magnitude-keyed split is
  uninformative. **Confirmed.** GFLAG-0246's "one functional discriminator the run records"
  is not a functional discriminator. The flat split does not falsify SD-024.
- Minor prose slip only: "essentially fixed at RESOURCE_BENEFIT=0.5 plus float noise" --
  values are 0.53-0.574, i.e. 6-15% above 0.5 from the env's amp/proximity terms, not float
  noise. Immaterial to the argument.
- Sample-size caveat (R3 cleared by 1; 6-of-57 tail; seed 23 contributes zero expansions) is
  fairly stated. My LOO check shows the PASS does not hinge on any single event *on its own
  DV*, which is slightly stronger than the draft claims for itself.
- The dopamine-range attribution to `drive_level` is not a confound: the ratio column takes
  only 7 discrete values, and `REEAgent.compute_drive_level(body)` is the only multiplicand.

## 3. Defects, with citations

### Defect A -- C2 admits (in fact, is) a construction-only reading; the pre-registered C2 fails

**Pre-registration.** Driver docstring lines 97-100 and 155-157:
`C2 FUNCTIONAL (load-bearing): Spearman rho(cluster_size, density) over the SAME live
events >= RHO_LIVE_MIN` and `C2 rho(cluster_size, density) >= RHO_LIVE_MIN (0.30)`. The
manifest criterion is named `C2_cluster_size_vs_density` and the interpretation_note says
"cluster size correlates with the weight-independent density reader".

**What is computed.** `evaluate()` line 722: `dens = np.array([ev["density_delta"] ...])`.
Lines 717-721 and the recorder comment at lines 462-471 say why: "the live rollout (57
pooled events, spatially recurring contacts) gave only 0.18 on the raw post-event level. The
delta isolates THIS event's own contribution". On THIS manifest, Spearman(cluster_size,
`density`) = **0.1775** -- the same 0.18, on the same n=57, under deterministic
`torch.manual_seed(seed)` + env seed. The DV was redefined after the pre-registered form was
observed failing at the evaluation config. The manifest does not record that C2 uses the delta
column; a reader recomputing "cluster_size vs density" from the artifact gets a C2 FAIL.

**Why the delta is arithmetic, not function.** `compute_local_density` (field.py:284-292) is
`sum_i active_i * exp(-||z - c_i||^2 / (2 bw^2))`. `add_residue` (field.py:165-180) places
the new center AT `location`, so the post-minus-pre density at `location` is exactly
`exp(0) = 1.0` -- confirmed 51/51 in `per_seed_rows` (max deviation 2e-6). `add_residue_cluster`
(field.py:241-253) places `n` centers at `location + N(0, 0.3^2)` in 16 dims, so each
contributes `exp(-||j||^2/2)` with `E||j||^2 = 1.44`, i.e. ~0.49 -- confirmed: per-center
delta 0.45-0.55 for all 6 expansion events. So `density_delta ~= 0.49 n` for n>=2 and `= 1.0`
for n=1, regardless of anything the agent, environment, or field history does. C2 on the delta
can only fail if the kernel sum is broken -- which R2 (the P0 sweep, rho=1.0) already
certifies on the same code path. C2 is R2 re-run with live jitter. It carries no information
about propagation "in the live-populated field" beyond what R2 carries, and the pre-registered
statistic that WOULD have carried that information (raw `density`, i.e. does expansion raise
the reader's signal at the reward location in the field the agent actually accumulates)
measures 0.18 and fails.

**A cell the draft's absolute misses.** Draft.md line 153-154: C2 "tested, passed,
non-degenerate". Draft.md line 124 grades Measurement "adequate" and the delta swap "a genuinely
careful design choice". But at the jitter/bandwidth used, a cluster of n=2 contributes LESS
density at the reward location than a single center (0.958 < 1.000; seed 37 event 14) -- i.e.
for the smallest expansion the "functional" reader reads a *reduction*. One third of the
expansion events (2 of 6) are at n=2. The driver documented the same geometry for bandwidth
narrowing (lines 222-237, rho -0.49) and correctly excluded narrowing from the gate; it did not
notice that jitter alone does it at n=2.

**What this changes in the autopsy.**
- Draft.md line 151-157 / json `learning_extracted[0]`: "GFLAG-0246's 'functional' concern
  conflates two senses ... rather than an actual gap in the run's own combination rule" ->
  the flag's reading is substantially right: C2 as computed is representational arithmetic.
  The gap in the combination rule is real.
- json `four_layer_diagnosis.measurement: "adequate"` -> should be something like "adequate
  for C1/C4; C2 non-discriminating by construction on the delta column, and the pre-registered
  raw-density form measures 0.18 (< 0.30)".
- json `narrow_supports_flag: false` -> `true`. The PASS supports the representational
  sub-clause (C1) and the MECH-233 asymmetry (C4). The label's "functional" half is
  over-claimed. This is the exact "PASS label asserts more than its criteria test" shape
  GFLAG-0246 named.
- `recommended_evidence_quality_note`: "does not weaken this PASS" and "the driver's own
  docstring operationalises SD-024's 'functional' clause as C2 (density-reader propagation,
  rho=0.5166, PASS)" must be qualified as above, and must record which column C2 uses.
- This also belongs under the corpus-wide recording-standard flag raised the same cycle
  (governance_flags.v1.json:3507, "None of those three were visible in the manifest") --
  V3-EXQ-900 is a fourth instance: the manifest names C2 as "vs_density" while it is computed
  on `density_delta`, and the pre-registered form is not recorded.

### Defect B -- the literature does not "predict" the flat split; Duvelle predicts the opposite of the substrate's formula

Draft.md lines 97, 99, 102-109; json `biological_reference.divergence`,
`learning_extracted[2]`, and the `recommended_evidence_quality_note` ("independently predicted
by the claim's own literature record ... a confirmed prediction, not an anomaly").

- Krishnan summary.md line 17: the ramp is expectation-dependent and this "supports the SD-012
  scaling decision ... `dopamine_signal = benefit_magnitude * drive_level`". Nothing in the
  summary predicts magnitude-insensitivity. The draft's "directly predicts a flat magnitude-
  keyed split" (line 97) is not in the source.
- Duvelle summary.md line 19: "`dopamine_signal = benefit_magnitude * drive_level` implies
  density should scale with how good the reward is. These animals ... their place cells did not
  care. **If REE's ablation shows density scaling cleanly with `benefit_magnitude`, that is a
  divergence from the biology, not a convergence with it.**" Duvelle is logged `weakens/0.70`
  and line 15 calls it "the principal counter-evidence". Its prediction is about biology; the
  substrate formula commits to the opposite; V3-EXQ-900 cannot adjudicate because
  `benefit_magnitude` never varied. The draft's own Section 5 says the split "carries no
  information for or against the claim, by construction" -- which is correct, and which is
  incompatible with calling the same split a confirmed prediction eleven lines earlier.
- Consequence for the recommendation: the draft (and `what_would_answer`, which it
  propagates) names `drive_level` as "the untested lever" and does not include
  `benefit_magnitude` in the residual dose-response sweep. Duvelle sets up the one
  discriminating test the literature record actually contains -- does allocation scale with
  reward VALUE at fixed drive -- and the substrate's formula gives a definite, falsifiable
  answer (yes, linearly). A sweep over `resource_benefit` (or `transient_benefit_multiplier`)
  at pinned `drive_level` is cheap in this exact driver and is the test that would move
  Duvelle's `weakens` one way or the other. The draft's "biological reference: clear" grade
  should be "present but bidirectionally untested on the magnitude axis".

### Not defects (checked and cleared)

- Sample size / R3-by-one: fairly stated; LOO-robust on the run's own DV.
- Confound in the dopamine range: none; drive_level is the sole multiplicand and takes 7
  discrete values.
- Per-seed heterogeneity masking a pooled story: none on C1 or on cluster_size~benefit; seed
  23 is simply uninformative (0 expansions), which the draft's "6 of 57" caveat already
  covers.
- "Six-event arm can carry it": on C1, yes at the 0.30 bar (LOO min 0.495). On the
  "functional" question it carries nothing, per Defect A -- but that is Defect A, not a sample
  problem.
- V3-EXQ-795 scoping-out: correct per Scope Discipline.
- Not-chipping the residual sweep from the autopsy: correct per CLAUDE.md.

## 4. Cheap confirmers (each resolves its defect in one command / one read)

**Defect A (both halves):**
```
python3 - <<'EOF'
import json
m=json.load(open('/Users/dgolden/REE_Working/REE_assembly/evidence/experiments/v3_exq_900_sd024_da_cluster_allocation_representational_functional_20260808T103846Z_v3.json'))
ev=[e for r in m['per_seed_rows'] for e in r['benefit_events']]
from scipy.stats import spearmanr   # or the driver's _spearman
print(spearmanr([e['cluster_size'] for e in ev],[e['density'] for e in ev]).correlation)        # -> 0.1775 (< 0.30)
print(spearmanr([e['cluster_size'] for e in ev],[e['density_delta'] for e in ev]).correlation)  # -> 0.5166 (manifest C2)
print(all(abs(e['density_delta']-1.0)<1e-5 for e in ev if e['cluster_size']==1))              # -> True, 51/51
EOF
```
plus `sed -n '97,100p;155,157p;462,471p;717,722p'` on the driver, which shows the
pre-registered "density" and the post-probe switch to "density_delta" in the author's own words.

**Defect B:** `sed -n '17p'` on
`.../targeted_review_sd_024/entries/2026-07-21_sd_024_vta_ca1_reward_proximity_krishnan2022/summary.md`
and `sed -n '19p'` on
`.../2026-07-21_sd_024_no_goal_overrepresentation_duvelle2019/summary.md`. Neither line
predicts a flat magnitude split; the second predicts the substrate's formula diverges from
biology.

## 5. Routing grade

Draft routing: `governance-note-only`, SD-024 stays `candidate`, no re-queue / substrate /
lit-pull, GFLAG-0246 -> resolved.

- **SD-024 stays candidate: agree.** Nothing here promotes or demotes it. C1 and C4 are real
  and C1 is LOO-robust.
- **No substrate build: agree.** `add_residue_cluster` behaves as specified; the n=2
  density-reduction is a parameter-geometry fact (jitter 0.3 in 16-d vs bandwidth 1.0), not a
  code defect. It should be recorded, not built against.
- **No lit-pull: agree**, provided the note stops misreading the lit that exists. The five
  entries are sufficient; the problem is the draft's reading of two of them.
- **Governance-note-only: agree on channel, disagree on content.** The note as drafted would
  land three wrong statements in `claims.yaml` (C2 = functional and adequate; flat split =
  confirmed lit prediction; `narrow_supports_flag` false). The corrected note should say: (i)
  flat `benefit_magnitude` split is uninformative (input near-constant) -- does not falsify;
  (ii) C2 is computed on `density_delta`, which is an arithmetic function of `n` and
  `jitter_radius` (single-center delta identically 1.0; per-center ~0.49); the pre-registered
  `rho(cluster_size, density)` measures 0.18 on this manifest; so the PASS is a
  **narrow-supports** for the representational (C1) and asymmetry (C4) sub-clauses and the
  "functional" label is over-claimed -- GFLAG-0246's core reading holds; (iii) the residual
  sweep should vary `benefit_magnitude` at pinned `drive_level` as well as the reverse,
  because that is the axis on which Duvelle (weakens) and the substrate formula make opposite
  predictions; (iv) at n=2 the cluster reads lower density at the contact point than a single
  center (0.958 vs 1.000), a geometry the future sweep should either fix (jitter/bandwidth
  ratio) or declare intended.
- **GFLAG-0246 -> resolved: agree**, but the resolution_note should say the flag was
  substantially RIGHT about the combination rule and WRONG only about which recorded number
  was the functional discriminator (the flat split is not one; the raw `density` column is,
  and it fails).
- **Re-queue: not from the autopsy** (CLAUDE.md rule on autopsy-own-finding follow-on stands),
  but governance should chip the residual sweep with the amended factor list, and should NOT
  wait on it to correct the C2 characterisation, which is a fact about this manifest.
- **One additional routing the draft omits:** attach V3-EXQ-900 as a fourth instance to the
  recording-standard flag at governance_flags.v1.json:3507 (criterion name/column mismatch
  invisible from the manifest). That is a one-line addition to an existing open flag, not a
  new flag.

## 6. Honest bounds on this red-team

- I did not re-run the driver; the "same sample as the probe" inference rests on identical
  n (57), identical rho (0.18 vs 0.1775), deterministic seeding, and a single driver commit two
  minutes before run start. Machine class differs (probe likely darwin, run linux; multinomial
  can diverge), so it is possible the probe sample differed and coincidentally matched. Either
  way the DV was redefined after the pre-registered form was observed to fail at this config,
  which is the point.
- The n=2 density-reduction is one event (plus a second at 1.094); I am flagging the geometry,
  not claiming a measured effect size.
- I have NOT found anything that flips the top-line "does not falsify" answer, and I am not
  claiming SD-024 is weakened by this run. The contest is about what the autopsy asserts C2
  proves, what it says the literature predicts, and the text it proposes to land.
