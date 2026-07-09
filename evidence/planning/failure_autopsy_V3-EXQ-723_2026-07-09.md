# Failure Autopsy — V3-EXQ-723 J-lens dispositional readout (flagged `vacuous_pass`)

- **Generated:** 2026-07-09T17:34:20Z
- **Target run:** `v3_exq_723_jlens_dispositional_readout_diagnostic_20260709T151028Z_v3`
- **Queue id:** V3-EXQ-723 · **purpose:** diagnostic · **claim_ids:** [] (SD-064 global-workspace + MECH-191 signal-legibility referenced for CONTEXT only)
- **Outcome:** PASS · **self-route label:** `compact_action_coupled_subspace_present` · **indexer adjudication:** `vacuous_pass`
- **Scope:** single · **Status:** confirmed (user-adjudicated)
- **Design ref:** `evidence/planning/global_workspace_jlens_plan.md` §2 (Experiment A)

---

## 1. Verdict in one line

The `vacuous_pass` flag is a **false positive at the mechanism it detected** (a `diffuse_branch: False`
schema collision), **but its conclusion is correct**: the self-route must NOT drive a governance action.
The real reason is that the two discrimination gates (compactness, retention) are **non-discriminative by
construction** — they are trivially satisfied by any weak nonzero linear signal, so the run does **not**
provide evidence for a *compact* action-coupled workspace. Committed action is *weakly* linearly decodable
above null; the compact-vs-diffuse question is **UNRESOLVED**. Diagnosis layer: **measurement adequacy**.

---

## 2. Facts (no interpretation)

**Self-route criterion (script line 57, PRIMARY_H=3):** `action predictable above null` AND
`jspace_activity_fraction < 0.10` AND `predictive_retention >= 0.80`, on a majority of 3 seeds.
The plan's richer positive-mode DVs (broadcast-alignment reportability proxy; reactive-bypass H1-vs-H5
contrast) were **reported, not gated** (script lines 49–51).

**Readiness preconditions (all met, recomputed):** P2 ticks 4211≥3000; train-pairs 2107≥1000;
distinct committed classes 3≥2; seeds above-null 3≥2; estimable seeds 3≥2.

**Aggregate DVs:**

| DV | Value | Gate | Passes? | Note |
|---|---|---|---|---|
| `primary_bal_acc_full_mean` | 0.504 | > null p95 | yes | vs `primary_null_p95_mean` 0.363 — weak margin |
| `primary_jspace_activity_fraction_mean` | **0.000284** | < 0.10 | yes ×350 | non-discriminative (see §5) |
| `primary_predictive_retention_mean` | **1.006** | ≥ 0.80 | yes | ~all predictivity retained; non-discriminative |
| `primary_jspace_dim_mean` | 2.0 | — | — | 1–3 dims of 112 |

**Per-seed:**

| seed | n_classes | committed_class_counts | bal_acc_full | null_p95 | jspace_frac | retention | jspace_dim |
|---|---|---|---|---|---|---|---|
| 42 | 5 | {0:877,1:1291,2:1872,3:1879,4:88} | 0.349 | 0.214 | 0.00046 | 1.005 | 3 |
| 43 | 3 | **{1:2699,2:3398,3:1}** | 0.699 | 0.513 | 0.000027 | 1.015 | 1 |
| 44 | 3 | {0:1447,2:952,4:1812} | 0.465 | 0.363 | 0.00037 | 1.000 | 2 |

Seed 43's committed-class distribution is near-degenerate (one class has a single instance) — effectively a
binary problem; its `jspace_dim=1`.

**Which criterion "failed":** none FAILed; this is a *flagged PASS*. The load-bearing issue is that the two
**discrimination** criteria (compactness, retention) are degenerate-passable — the substrate-ceiling *tell*
in the diagnostic-design register rather than the run register.

---

## 3. Why the flag fired — schema collision (tooling false positive)

`_compute_adjudication` legacy check (`build_experiment_indexes.py:289`):
`if PASS and any(v is False for v in criteria_non_degenerate.values()) -> vacuous_pass`.

The script writes `criteria_non_degenerate = {readiness_estimable:True,
action_predictable_above_null_majority:True, jspace_compact_majority:True,
predictive_retention_majority:True, diffuse_branch:False}` (script line 1222).

`diffuse_branch` is a **branch-selector** (`diffuse = signal_gate and not (compact_gate and retention_gate)`),
not a non-degeneracy assertion. `False` here is the *good* outcome ("did NOT take the diffuse branch" =
"took the compact/present branch"). Every other key follows the "True = non-degenerate/good" convention; this
one inverts it, so `any(v is False)` fires. **Verified:** deleting the `diffuse_branch` key re-adjudicates the
run to `verified`. This is the same class of bug as the V3-EXQ-648a/649 directionality false-flag: a
schema-convention mismatch producing a spurious adjudication, not a real degeneracy. Handed off as a separate
task (see §8).

---

## 4. Claim-layer map

`claim_ids=[]`; SD-064 and MECH-191 are context-only. So no claim can be weakened by this run. SD-064
(global-workspace access channel, candidate / v3_pending) is *tested for real only if* the discrimination
gates are discriminative — which they are not. The diagnostic therefore **cannot let SD-064 express itself**,
so it neither raises nor lowers the SD-064 prior. The plan's decision this gates — "build the SD-027 retrofit
for Experiment B only on a *clean positive* A" — is **not** satisfied.

---

## 5. Biological-reference triage

- **Closest reference:** Baars' Global Workspace (access-consciousness); the *method* is a formal
  interpretability import (Anthropic 2026 Jacobian lens). SD-064 makes the access-functional claim only.
- **Import type:** the DV is a **ported measurement**, not a biology translation. The failure is therefore
  **not** a biology divergence (no `/lit-pull` owed — the design note already exists).
- **Core measurement flaw:** the port's compactness operationalization does not survive REE's geometry. The
  J-space is the top singular directions of the ridge weight matrix W. `jspace_activity_fraction` = variance
  of z projected onto those directions / total z variance. In a 112-dim latent whose variance is spread across
  all dims, the action-predictive subspace occupies a tiny fraction **whether or not** a genuine compact
  workspace exists — so `< 0.10` is essentially always true. Likewise `retention` (`bal_acc_jspace /
  bal_acc_full`) is ~1.0 *by construction* because the J-space *is* W's predictive directions. **Both
  discrimination gates are non-discriminative.** The only informative signal is weak above-null decodability.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | claim_ids=[]; SD-064 cannot express itself through non-discriminative gates |
| Biological reference | clear | Baars GWT / Anthropic J-space; ported *measurement*, not biology divergence |
| Prerequisites | present | post-hoc readout on existing all-ON substrate; all readiness floors met |
| Implementation completeness | partial | readout ran, but compactness/retention criteria carry the *symbol* of the "<10%" test without its discriminative force; broadcast/reactive contrasts computed but not gated |
| Environment adequacy | partial | seed 43 committed-class distribution near-degenerate (2 effective classes); CausalGridWorldV2 may under-exercise committed-action diversity |
| **Measurement adequacy** | **under-instrumented / misleading (DOMINANT)** | compactness (<0.10) and retention (≥0.80) trivially satisfiable by any weak nonzero linear signal |
| Integration adequacy | n/a | single-module readout |
| Scale / capacity | adequate for estimability | signal itself weak (bal_acc barely above null) |

**Recommended epistemic_category:** *not* `substrate_ceiling`. This is a **diagnostic measurement /
test-design gap** — the discrimination criteria do not test what the label asserts. Re-derive brake: first
autopsy tagging SD-064 → **does not fire**.

---

## 7. Learning extracted

1. **Activity-fraction is not a compactness test in a high-dim recurrent latent.** A ridge-map row space is a
   tiny fraction of a 112-dim latent for any weak signal; `<0.10` is non-discriminative. A real compactness
   test must compare against a **matched-rank random-subspace baseline** (does the action-predictive subspace
   predict *better than* a random same-dimension projection, and/or occupy *less* activity than a random
   same-dim subspace would).
2. **Retention ~1.0 is near-automatic** when the J-space is defined as W's own predictive directions; it needs
   a non-trivial comparator or must be dropped.
3. **The plan's positive-mode was richer than the gated self-route.** Broadcast-alignment (reportability) and
   reactive-bypass (H1 vs H5) were "reported, not gated" — the label overclaims relative to the plan's own
   definition of a positive J-space. A redesign should **gate** these.
4. **Branch-selector flags must not live in `criteria_non_degenerate{}`** (see §3) — a governance-tooling
   convention lesson.

## 7b. Repair pathway (user-confirmed)

**Adjudication:** inconclusive / `non_contributory` — weak above-null decodability, compact-vs-diffuse
**UNRESOLVED**. The self-route label must NOT raise the SD-064 prior and must NOT greenlight the SD-027
Experiment-B retrofit build.

**Routing:** `/queue-experiment` — redesign Experiment A as a **new lettered iteration (V3-EXQ-723a)**, same
scientific question, implementation fix to the criteria:
- discriminative compactness: J-space must beat a **matched-rank random-subspace** baseline;
- **gate** the broadcast-alignment and reactive-bypass (H1-vs-H5) contrasts into the verdict (plan §2 DVs);
- prefer a committed-action-balanced eval so no seed degenerates to ~2 classes (cf. seed 43).

This is an implementation fix to the *same* question (alphabetic suffix), not a new hypothesis, and not a
same-ceiling re-derive (the brake is inapplicable — first autopsy, and the redesign changes the *measurement*,
not merely re-runs it).

**Draft `evidence_quality_note` for governance to write on the manifest (do NOT write from this skill):**

> V3-EXQ-723 (J-lens dispositional readout, diagnostic, claim_ids=[]): adjudicated INCONCLUSIVE by
> failure_autopsy_V3-EXQ-723_2026-07-09. The `vacuous_pass` indexer flag is a schema-collision false positive
> (`diffuse_branch:False` inside criteria_non_degenerate). The self-route `compact_action_coupled_subspace_present`
> is NOT trustworthy on its own terms: the discrimination gates (jspace_activity_fraction<0.10; retention>=0.80)
> are non-discriminative — trivially satisfied by any weak nonzero linear ridge map in a 112-dim latent.
> Established: committed action is WEAKLY linearly decodable above null (bal_acc 0.35-0.50 vs null_p95 0.21-0.51).
> NOT established: a *compact* action-coupled workspace. Does NOT raise the SD-064 prior; does NOT justify the
> SD-027 Experiment-B retrofit build. Superseded by V3-EXQ-723a (redesigned discriminative compactness +
> gated broadcast/reactive contrasts) when it runs.

---

## 8. Tooling handoff (spawned as a separate task)

The `diffuse_branch:False` schema collision (§3) false-flags this and every future *compact-branch* J-lens run
as `vacuous_pass`. Fix is out of scope for this claims-governance autopsy and is spawned as its own task:
either **script-side** (move branch-selectors out of `criteria_non_degenerate{}`, or invert to
`compact_branch:True`) or **indexer-side** (the legacy check should key on a non-degeneracy naming convention
and ignore branch-selector keys). Script edits must go through `/queue-experiment`.

---

## 9. Routing summary for /governance

- **evidence_direction:** `non_contributory` (keep; annotate with the note in §7b).
- **Does NOT** raise SD-064 prior. **Does NOT** greenlight SD-027 Experiment-B build.
- **Route:** `/queue-experiment` → V3-EXQ-723a redesign (discriminative compactness + gated broadcast/reactive).
- **No** substrate_queue entry (measurement fix, not a substrate build). **No** lit-pull (design note exists).
- Separate tooling task spawned for the `diffuse_branch` adjudication false-positive.
