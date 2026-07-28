# Audit — failure autopsies that reasoned over `--dry-run` smoke manifests

- **Generated (UTC):** 2026-07-28T17:22:44Z
- **Session:** `dazzling-solomon-8a0090`
- **Trigger:** session `sweet-williams-f30676` fixed the dry-run *scoring* leak (REE_assembly `cb7298c1c4` converter+indexer gate, `5189800eea` rebuild dropping 34 claim-entries across 22 run_ids). This audit is the separate question: did any **human/agent adjudication** also reason over those smokes?
- **Scope:** all 542 `evidence/planning/failure_autopsy_*` files, grepped against the 23 dry-run run_ids. 9 hits / 4 files, reducing to two cases.
- **Verdict:** **Case 1 — diagnosis does NOT survive.** Case 2 — conclusion survives; one population statistic is inflated ~1.9x.
- **This document applies nothing.** Manifest `evidence_direction`, `substrate_queue.json` and `claims.yaml` writes are governance's; the recomputed values are stated below for governance to apply.

---

## Case 1 — V3-EXQ-543i (ARC-062 / MECH-309 / INV-074 / MECH-334): **diagnosis does not survive**

### 1.1 The smoke is structurally incapable of producing the reading taken from it

`v3_exq_543i_..._20260518T063711Z_v3` is `dry_run: true`, 691 s against the real run's 12386 s. The driver
(`ree-v3/experiments/v3_exq_543i_arc062_differential_heads_falsifier.py:1494-1497`) reduces
P0 40->3, **P1 60->4**, P2 8->2, steps/episode 200->30 — ~80x less compute (270 vs 21600 env steps per seed-arm).

The decisive detail is not the budget but the detector gate at line 1286:

```python
if (probe["applicable"] and (ep + 1) >= MID_TRAINING_EP        # MID_TRAINING_EP = 30
        and probe["mean_tv_distance"] < INERT_GATING_THRESHOLD # 0.05
        and not inert_gating_detected):
    inert_gating_detected = True
```

Dry-run P1 is **4 episodes**, so `(ep+1) >= 30` is **never true**. `p1_inert_gating_detected` is
**structurally unsettable** in any dry run — hardcoded `False` by the guard, whatever the policy did.
Verified: 0/36 cells detected, exactly one probe per cell (at `p1_ep = 4`).

**And the sign is inverted.** The smoke's gated arms recorded `mean_tv_distance` of
0.00053 / 0.00113 / 0.00063 / 0.00037 / 0.00087 / 0.00072 — **~100x BELOW** the 0.05 inert threshold.
The smoke's policy was *more* collapsed than the real run's. Had the `>= 30` gate not blocked it,
every gated arm would have flagged INERT.

So `diff_off_reproduced_collapse = false` and `diff_on_escape = true` in the smoke are **vacuous** —
a disabled detector, not a measurement of escape.

### 1.2 There is no bistability. The real runs are unanimous.

| run | dry | elapsed | branch | `diff_off_reproduced_collapse` | `diff_on_escape` | gated arms inert |
|---|---|---|---|---|---|---|
| 543i `20260518T063711Z` | **YES** | 691 s | (c) | false *(vacuous)* | true *(vacuous)* | 0/3 *(detector disabled)* |
| 543i `20260518T191052Z` | no | 12386 s | (e) | true | false | **3/3 all 8 arms** |
| 543i `20260521T035802Z` | no | 21781 s | (e) | true | false | **3/3 all 8 arms** |
| 543j `20260519T080741Z` (ree-cloud-4) | no | 22298 s | (e) | true | false | **3/3 all 8 arms** |

**Three full-budget runs, at least two machines, all branch-e, zero variance.** The sole dissenting
data point in the entire cluster is the smoke.

### 1.3 The correct diagnosis already existed and was overwritten six hours later

Two autopsies were written on 2026-05-19:

| file | generated | reading of the smoke |
|---|---|---|
| `failure_autopsy_V3-EXQ-543i_2026-05-19.json` | **01:13:33Z** | **CORRECT** — "Truncated-training artifact (~690 s vs full ~12386 s). No arm trained into the head-collapse attractor, so `diff_off_reproduced_collapse=false` is **vacuous**, not a sanity-baseline failure." Discharges the `arc_062_rule_apprehension` GAP-B resume_condition step. |
| `failure_autopsy_543i_2026-05-19.{md,json}` | **07:06:52Z** | **REGRESSED** — treats the pair as "**two byte-identical runs**" that "landed opposite basins", and builds a cross-run basin-nondeterminism narrative on it. |

The later autopsy is the one governance applied. The 01:13Z autopsy's conclusions were discarded, and
with them a live claim disposition:

- 01:13Z recommended `ARC-062: weakens`, `MECH-309: supports (narrow)`, `MECH-333: weakens`, with
  `provisional_gate: "V3-EXQ-543j cross-machine confirmation ... branch-e CONFIRMS -> ARC-062 weak-reading demotion + ARC-063/V4 escalation may proceed"`.
- 543j **landed branch-e** — the gate was satisfied.
- But governance, applying the 07:06Z autopsy, wrote all four claims `non_contributory` and recorded
  on the 543j manifest: *"basin selection RNG/init + cross-run + cross-machine nondeterministic"* —
  asserting nondeterminism over a run set with **zero** variance, because the only dissenting point was a smoke.

ARC-062 is still `candidate` / `pending_retest_after_substrate: true`. The demotion the 01:13Z autopsy
gated on 543j was blocked by a phantom.

### 1.4 What propagated

**`evidence/experiments/` manifest notes** — `20260518T191052Z` carries the 07:06Z autopsy's §8 draft
near-verbatim ("Two byte-identical runs landed opposite basins..."); `20260521T035802Z` and the 543j
manifest carry the derived "basin nondeterminism" line.

**`evidence/planning/substrate_queue.json`** — `/queue[68]/failure_record[3]` is an entry whose `run_id`
**is the smoke**, asserting *"Cross-run basin split: byte-identical 063711Z (all-escape) vs 191052Z
(all-collapse) demonstrates RNG/init + cross-run nondeterminism."* Both `failure_record[3]` and `[4]`
now carry a `target` demanding `n_inert_gating_seeds == 0 ... reproducibly across K>=3 repeated
same-machine runs ... basin selection deterministic w.r.t. init RNG` — **a bar raised to clear an
instability that does not exist**, which any future ARC-062 fix must now clear.

`failure_record[2]` (the 543h entry) separately reads the same smoke the other way — *"V3-EXQ-543i
validation: diff_on_escape=true (all 4 diff-ON gated arms 0 inert / 3 seeds -- **fix WORKS**)"*. The same
vacuous field was cited once as proof the fix worked and once as proof of nondeterminism.

### 1.5 Recommended writes — **for governance, not applied here**

1. **Dispositions are unchanged.** All four claims stay `non_contributory` on 543i, and
   `epistemic_category: substrate_ceiling` stands — but on the *correct* grounds: diff-ON arms collapse
   3/3 identically to diff-OFF across three full-budget runs and two machines, so `use_differential_heads`
   produced no differentiation and ARC-062's falsifier could not discriminate. **No claim's confidence
   changes.** What changes is the stated reason and everything downstream of it.
2. **Retract the bistability finding.** It was 543i's headline contribution over 543h ("upgrades the
   543h evidence from cross-machine to cross-run on a single host") and it is not supported. Learning #2
   of the 07:06Z autopsy is false; learning #1 should read *deterministically collapses*, not
   *remains basin-nondeterministic* — a **stronger** result against the fix, not a weaker one.
3. **Correct `substrate_queue.json` `/queue[68]`** — `failure_record[3]` cites a dry run as evidence and
   should be struck or relabelled vacuous; drop `K>=3 repeated same-machine runs` and
   `basin selection deterministic w.r.t. init RNG` from the `target` of `[3]` and `[4]` unless
   independently motivated. The `mean_tv >= 0.05` and cross-machine conditions stand on their own.
4. **Re-open the 01:13Z gate.** 543j confirmed branch-e cross-machine; `20260521T035802Z` confirmed it
   cross-run same-machine. Whether that now licenses the ARC-062 weak-reading demotion and ARC-063/V4
   escalation is a governance decision, but it should be decided on the merits rather than left blocked
   by the phantom. Note the countervailing reading: because diff-ON also collapsed, the rule-apprehender
   never functioned, so MECH-309's "collapse is the equilibrium *without* an apprehender" is arguably
   still untested — `non_contributory` may well remain right for MECH-309 on its own merits.
5. **INV-074 / MECH-334 are unaffected.** Untested-not-weakened stands under either reading.

---

## Case 2 — `failure_autopsy_sd081-spearman-degenerate-dv_2026-07-27`: **conclusion survives; one statistic inflated**

Committed clean at `54e10bee85`, no active claim — not live work.

The five smokes are **population members**, not worked examples, in a 17-run corpus analysis of degenerate
`rho_drive_vs_reef`. (The population actually contains **six** dry runs — the 543i smoke from Case 1 is in
the member list too.)

**The cited statistic is inflated.** The autopsy reports degeneracy on *"the 64/378 arms with
`mean_reef_fraction == 0.0`"*:

| subset | arms | zero-reef | rate |
|---|---|---|---|
| all 17 runs (as cited) | 354 | 64 | 18.1% |
| **6 dry smokes** | 108 (30%) | **42 (66%)** | **38.9%** |
| **11 real runs** | 246 | **22** | **8.9%** |

The smokes contribute **two-thirds of the zero-reef arms from under a third of the arms**, more than
doubling the apparent degeneracy rate. The mechanism is mundane: at 30 steps/episode an agent barely
moves, so `mean_reef_fraction == 0.0` is the *signature of truncation*, not of the measurement defect
under study. Three of the six are the same driver smoked three times in four minutes (36 near-duplicate
arms), which distorts a rate more than a count — as anticipated.

Note the denominator does not reproduce: 354 arms on disk vs 378 cited.

**The conclusion holds, and robustly.** Two independent reasons:

1. The load-bearing claim is **structural, not statistical** — *"this rho is REPORTED ONLY; the
   load-bearing PASS/FAIL gates read `mean_reef_fraction` and `d4_delta_abs`, not the rho."* That is a
   property of the code and is unaffected by which runs are in the population. 22 real-run zero-reef arms
   remain, so the phenomenon is real on real runs.
2. **The evidence for the tie-break-artifact diagnosis is 100% real-run.** The recurring deterministic
   values the autopsy cites as proof — `0.74072` and `0.0088` — trace to **0 dry / 4 real** and
   **0 dry / 10 real** respectively.

**Recommended write:** annotation only — correct the prevalence figure to **22/246 (8.9%) on full-budget
runs**, noting the dry-run exclusion. `evidence_direction: unchanged` and the "do NOT re-adjudicate"
disposition stand. No claim impact.

---

## Secondary finding — the governance annotation sweep

All five 543f/g/h smokes carry a **byte-identical** `evidence_direction: superseded` +
`epistemic_category: substrate_ceiling` + note, applied by `a6fda79367`
(*"governance 2026-05-18: apply confirmed V3-EXQ-543h autopsy to ARC-062/MECH-309 cluster ...
543f x4 / 543g / 543h x2"*).

**It is not a script.** The commit touches no `.py`/`.sh`; it was an agent-driven `/governance` pass that
swept by queue-id/experiment-type family with no `dry_run` filter. So there is nothing to patch — the
verdict came from `failure_autopsy_V3-EXQ-543h_2026-05-18`, which correctly read only non-dry runs, and
was then stamped onto dry siblings by family match. That is how smokes acquired governance-grade metadata
indistinguishable from adjudicated evidence — the precondition for Case 1.

**The remaining gap is procedural, not mechanical.** As of `cb7298c1c4` the *scoring* path is gated at
the converter and the indexer, and `generate_pending_review.py` excludes dry run_ids from every pending
bucket. Nothing prevents an **adjudicating session** from reading a dry manifest as evidence — which is
exactly what happened here, twice, six hours apart, in opposite directions. Worth a `/failure-autopsy`
and `/governance` step that checks `dry_run` on every manifest it cites and refuses to write
`evidence_direction` / `epistemic_category` onto a dry one.

---

## Standing lesson

The defect was caught per-instance and patched per-instance at least four times without the pipeline
being fixed — V3-EXQ-429 (2026-04-15), V3-EXQ-615 (2026-05-31), and the 543i 01:13Z autopsy (2026-05-19),
whose correct finding was then overwritten by a second autopsy on the same day. A correct local diagnosis
does not survive on its own; only a gate does.
