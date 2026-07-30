# RESOLVED 2026-07-30: `ARM_2_ALL_ON` "nonreproducibility" was a SUBSTRATE RETUNE, not nondeterminism

Session `great-hopper-1d7b24`, chip `chip-20260730-arm2-allon-nonreproducibility`.
Predecessor finding: [`README_ree-cloud-4_2026-07-30.md`](README_ree-cloud-4_2026-07-30.md)
("The reproducibility finding"), session `awesome-mestorf-fa7072`, REE_assembly `05ebef9e40`.

**Verdict: the nondeterminism hypothesis is FALSIFIED. `V3-EXQ-614` and `V3-EXQ-614a` are not
a replicate pair at all — they ran against two different values of a substrate parameter that
changed in the 24 h between them. The FAIL -> PASS flip is the intended, designed effect of
that change. No reproducibility probe is needed, and none was queued.**

---

## The cause

`ree-v3` commit **`a45ca7f`** — *"MECH-341 retune: entropy_lambda 0.05 -> 0.5, bias_scale
0.1 -> 1.0"* — committed **2026-05-29T23:41:55Z**, i.e. **between the two runs**. It changed
two `REEConfig` defaults *and* the matching `E3ScoreDiversityConfig` dataclass defaults:

```
e3_diversity_entropy_lambda:     0.05 -> 0.5   (10x)
e3_diversity_entropy_bias_scale: 0.1  -> 1.0
```

### Timeline (all UTC; manifest timestamps are WRITE time, i.e. end of run)

| when | event |
|---|---|
| 2026-05-29T19:13:18Z | **614 manifest written** on ree-cloud-4 — 4 h 28 m *before* the retune |
| 2026-05-29T23:41:55Z | **`a45ca7f` retune committed**: λ 0.05 -> 0.5 |
| 2026-05-30T06:45:23Z | **614a driver authored + queued** (`ree-v3 c90ee9f`) — 7 h *after* the retune |
| 2026-05-30T19:32:45Z | **614a manifest written** on ree-cloud-3 |

The 614a driver **did not exist** until 7 h after the retune, so there is no runtime long
enough to place its execution pre-retune. 614 finished 4½ h before it. **614 ran at λ=0.05;
614a ran at λ=0.5.** This is not an inference from run duration — it is fixed by the file's
own creation commit.

### Why `config_summary` could not see it — the reason this looked like nondeterminism

The predecessor session verified `config_summary` **field-for-field identical** and was
right to; that check simply cannot detect this change:

- `mech341_entropy_bias_scale` **is** pinned by the driver (`MECH341_ENTROPY_BIAS_SCALE = 2.0`,
  passed explicitly to `REEConfig.from_dims`) and **is** recorded in `config_summary`. It
  therefore overrode the retune's `bias_scale` half and is genuinely identical in both runs.
- `e3_diversity_entropy_lambda` is **neither passed by the driver nor recorded in
  `config_summary`**. It silently took the `REEConfig` default — which is the half that changed.

`config_summary` (identical in both manifests) is 8 keys:
`alpha_world, drive_weight, mech341_entropy_bias_scale, mech341_sub_flavours,
reef_bipartite_layout, reef_enabled, vs_stack, z_goal_enabled`. λ is absent.

The re-queue commit `c90ee9f` frames 614a purely as a *"post `41c3411` manifest-pipeline
fix"* re-run, and the 614a docstring asserts *"the science is identical; only the pipeline bug
was the difference between predecessor and successor."* **That assertion was false at the time
it was written** — the substrate had been retuned 7 h earlier — and nothing in the
`/diagnose-errors` re-queue path checks for it.

---

## Why the divergence is confined to `ARM_2_ALL_ON` — the part that made it look intrinsic

The predecessor session's structural diff was exactly right: 43 leaf differences, **all** in
`arms[2]`; `ARM_0_B_only` and `ARM_1_ablate_B` bit-identical *across two machines*. That
pattern is fully explained by two guard clauses in
`ree-v3/ree_core/predictors/e3_score_diversity.py`, with **no nondeterminism required**:

| arm | axes | is MECH-341 live? | can λ matter? |
|---|---|---|---|
| `ARM_0_B_only` | A off, **B on**, C off, D off | **NO** — inert via guards | no -> bit-identical |
| `ARM_1_ablate_B` | A on, **B off**, C on, D on | **NO** — module not built | no -> bit-identical |
| `ARM_2_ALL_ON` | A on, **B on**, C on, D on | **YES** | **yes -> diverges** |

`ARM_0` has B (MECH-341) ON, so it *looks* like λ should bite there too. It does not, because
`ARM_0` has A (SP-CEM) **OFF**, so its candidate pool collapses to a single first-action
class, and both MECH-341 sub-flavours then short-circuit on that:

- `apply_entropy_bonus` (`e3_score_diversity.py:207-209`) — `if len(unique_classes) <= 1:
  return scores.new_zeros(K)`. **Returns zeros before λ is ever read** (λ is used at :217).
- `stratified_select` (`:270-273`) — `if len(unique_classes) <
  min_classes_for_stratification (2): return None`, so the caller falls through to legacy
  argmin.

That collapse is **measured, not assumed** — and it is identical in both manifests:

| arm | `mean_n_unique_selected_classes` | `mean_selected_class_entropy_nats` |
|---|---|---|
| `ARM_0_B_only` | **1.0** (614) / **1.0** (614a) | **0.0** / **0.0** |
| `ARM_1_ablate_B` | 2.667 / 2.667 | 0.525839 / 0.525839 |
| `ARM_2_ALL_ON` | 3.333 / 3.333 | **0.579882 / 0.683762** |

`ARM_0` sits at exactly one class in both runs. `ARM_1` is bit-identical. So **`ARM_2_ALL_ON`
is the only arm in this experiment in which MECH-341 is live at all** — hence the only arm a
λ change can touch. `A_sp_cem` is what makes it live: SP-CEM's
`support_preserving_min_first_action_classes=2` is what supplies the >= 2 classes the guards
require.

### The magnitudes agree with the retune's own prediction

`a45ca7f`'s message predicted the pre-retune regime quantitatively: *"for 90% dominant class,
bonus = lambda * freq = 0.045, far below observed score gaps 0.27-1.96."* 614's C2 delta is
**0.054043** — the ineffective-bonus regime, as predicted. At λ=0.5 the bonus is ~0.45,
comparable to the score gaps, so it bites: 614a's delta is **0.157923**.

C2 is `ALL_ON entropy − ablate_B entropy`, and `ablate_B` is bit-identical, so the entire
delta change is `ARM_2`'s entropy rise `0.579882 -> 0.683762`. `n_seeds_rung1_pass` 2 -> 3
moves in the same direction — a larger diversity bonus clears Rung 1 on one more seed.

**The causal chain is closed with no unexplained residual.** Every arm's behaviour is
accounted for by the guard clauses plus one 10x parameter change. Positing additional
nondeterminism is unnecessary; and `ARM_0`/`ARM_1` reproducing **bit-identically across two
different machines** is itself strong evidence these paths are deterministic and
cross-machine reproducible.

### Correction to the predecessor write-up

`README_ree-cloud-4_2026-07-30.md` reasoned: *"if the two boxes computed differently, all
three arms should drift"* -> therefore the divergence is *"intrinsic to that arm"*, naming
"a nondeterminism reachable only in the full-stack combination" as the natural hypothesis.
The premise and the arm-localisation were both correct; the inference to *nondeterminism*
skipped the alternative that a **substrate parameter changed between the runs**. That session
explicitly flagged the hypothesis as uninvestigated and chipped it, which is why it is
resolved here at documentary cost rather than by burning compute.

---

## Consequences for MECH-341 / ARC-065 — for `/governance`

**1. The reproducibility objection to the landed 614a PASS is withdrawn.** The
`PASS_C2_C3_only_mech341_load_bearing_in_stack_only` disposition does **not** rest on an arm
that a bit-identical re-run failed to reproduce. It rests on λ=0.5, which is the substrate's
value at HEAD today (`e3_diversity_entropy_lambda: float = 0.5`, `config.py:1799`). **No
change to the disposition is required on reproducibility grounds.**

**2. A different and live question replaces it: MECH-341's C2 pass is λ-dependent, and λ was
retuned *because* C2 was failing.** The honest statement of the evidential situation:

- `V3-EXQ-611c` PASSed with C2=False, root-caused as *"entropy_lambda=0.05 too small"*.
- `a45ca7f` raised λ 10x, citing a **mechanistic** rationale (bonus 0.045 vs observed score
  gaps 0.27-1.96), not the C2 threshold value.
- `V3-EXQ-614a` then PASSed C2 at 0.157923 against a pre-registered threshold of **0.1**.

So C2 clears its threshold by ~1.6x on the tuned parameter, and the recovered 614 now
supplies the previously-missing counterfactual: **at λ=0.05 the same falsifier returns C2
delta 0.054 — a FAIL.** That makes MECH-341's "load-bearing in stack only" verdict
explicitly **λ-conditional**, which is a stronger and more precise claim than "reproducible",
but also a narrower one than the disposition text currently implies.

This is a governance call, not this session's: whether `load_bearing_in_stack_only` should
carry an explicit λ-conditionality note, and whether a λ-sensitivity sweep is wanted to
establish how knife-edge the 0.1 threshold crossing is. **Per the CLAUDE.md rule that a
session must not chip follow-on depending on its own not-yet-governance-reviewed finding,
no experiment has been queued for this and no chip spawned.** It is reported here and in the
closing note for `/governance` to ratify or revise first.

**3. ARC-065 is affected only in the same way** — it is co-tagged on both runs and takes the
same λ-conditionality qualifier. No independent issue found.

**4. The recovered 614 is not a "delivery-failure FAIL" — it is a valid result for a
superseded configuration.** See the admission decision below; this changes the *reason* for
its treatment, though not the treatment itself.

---

## The generalizable defect — the actual infrastructure finding

**Manifests do not record the substrate version, so no two runs in this corpus can be
verified as a true replicate pair.** Measured 2026-07-30: **5 of 747** flat manifests under
`evidence/experiments/` carry any substrate-commit field
(`v3_exq_792`, `792a`, `819`, `819a`, `830`). The other 742 do not.

This episode is the cost of that gap, and it cost real work twice over: a substrate retune
7 h before a run was invisible in the manifest, so a bit-identical-driver re-run was recorded
and reasoned about as a scientific replicate for two months, then investigated as suspected
substrate nondeterminism. Both were avoidable by one recorded SHA.

Two distinct sub-defects, both worth fixing:

- **(a) No substrate commit in the manifest.** A `ree_core` SHA (plus dirty-flag) would have
  reduced this whole investigation to one `git diff`.
- **(b) `config_summary` is a hand-curated allowlist, so any `REEConfig` default the driver
  does not explicitly pass is unrecorded and un-auditable.** Here the driver pinned
  `bias_scale` (recorded, unchanged) but not `entropy_lambda` (unrecorded, changed 10x) —
  the worst case, because the *recorded* half of the same retune was identical, which
  actively corroborated the false "identical configuration" conclusion.

Fixing (b) generally means emitting the resolved config for the flags the experiment's own
axes touch, not just the ones the author remembered. Chipped separately — this is an
infrastructure defect nothing audits, and it does not depend on the scientific finding above.

---

## ADMISSION DECISION TAKEN: 614 ADMITTED as `evidence_direction: "superseded"`

Chip step 4. The manifest was parked at
`evidence/planning/recovered_stranded_manifests/v3_exq_614_..._20260529T191318Z_v3.json`,
deliberately outside `evidence/experiments/` so the indexer could not score it.

**Decision: ADMIT, with `evidence_direction: "superseded"`.** Method follows the
`DECISION TAKEN 2026-07-30` precedent in [`README.md`](README.md) — flat **plus**
`runs/<run_id>/manifest.json`, because a flat-only manifest is inert to the indexer.

### Why `superseded`, and why NOT the two alternatives

- **NOT as-emitted `weakens`.** It would mint scored `weakens` entries for MECH-341 and
  ARC-065 out of a configuration the substrate no longer has.
- **NOT `superseded_by_substrate` (+ `weakens`), despite that field being semantically
  perfect here.** `build_experiment_indexes.py:110-117` defines
  `superseded_by_substrate` for precisely this case — *"mechanistically stale because a
  substrate it depends on changed AFTER the run was recorded"* — and it does correctly set
  `scoring_excluded="stale_substrate"`, protecting confidence. **But it leaves
  `evidence_direction` as `weakens`, and the gap register does not honour
  `scoring_excluded`:** `direction_counts` is accumulated over **all** entries keyed on
  `evidence_direction` with no exclusion check (`:2349-2353`), and
  `ARCHITECTURE_GAP_REGISTER.md`'s `conflict_ratio` reads it (`:3603`). That is the known
  `scoring_excluded`-does-not-protect-the-gap-register leak, and it is exactly how admitting
  ARC-110 as `weakens` moved its `conflict_ratio` 1.0 -> 0.8 in the precedent.
- **`superseded` is inert on both paths.** It sets `scoring_excluded="superseded"`
  (`:2604-2605`), excluding it from confidence; **and** `_direction_conflict_ratio`
  (`:2066-2073`) reads **only** the `supports` and `weakens` keys, so a `superseded`
  direction contributes to neither numerator nor denominator and `conflict_ratio` cannot
  move. This is why the CLAUDE.md supersession policy is right, and it is right for a
  sharper reason than "the indexer treats it as inactive".

`superseded_by_substrate: "MECH-341@2026-05-29"` is **additionally** recorded on the admitted
manifest as machine-readable provenance for *why* it is superseded — it is inert alongside
`evidence_direction: "superseded"` (which already excludes the run) but makes the retune
attributable without reading this document.

### What the as-emitted record costs, and where it is preserved

`evidence_direction: "superseded"` overwrites the as-emitted `weakens`, so the admitted copy
is no longer the record that the falsifier returned FAIL on first execution — which is the
provenance value the chip identified. That record is preserved in two places:
`result.acceptance_criteria` (`C2_b_necessity_delta: false`,
`C2_entropy_delta_value: 0.054043`) and `result.outcome: FAIL` are **untouched** on the
admitted manifest, and the parked copy in this directory stays **byte-identical to the
worker's file** as the provenance original, exactly as the 707c/673 precedent did.

`outcome: FAIL` means the run will appear in `pending_review.md` under **FAIL (action
required)** — correct and intended, same as the precedent. **`review_tracker.json` was
deliberately NOT touched**: marking runs reviewed is `/governance` Step 5's call.

### Measured effect on the corpus

See the "Measured" section appended below after the index rebuild.
