# Fan-out sweep — the whole-bank `slot_cosine_sim` / `sws_slot_diversity` confound

**Status:** `confirmed` (2026-08-20, interactive `/failure-autopsy` Step 8 gate, session `failure-autopsy-slotcosine-confirm`) — drafted headless 2026-08-14, confirmed after independent re-verification. **See the Confirmation section at the foot of this file: recommendations 3 and 7 were already discharged before confirmation and must not be re-applied; recommendation 1's `epistemic_category` was corrected to a valid enum value.**
**Generated:** 2026-08-14T01:41:47Z
**Session:** `metaworker-chip-20260813-slotcosinesim-fanout-sweep`
**Machine-readable companion:** `failure_autopsy_slot_cosine_sim_fanout_sweep_2026-08-13.json`

**Discharges:** the fan-out recommendation left open by `failure_autopsy_V3-EXQ-436d-methodology-check_2026-08-07` (confirmed, `REE_assembly` `01d985a422`) — *"A grep-level sweep for other criteria pre-registered on a whole-bank cosine is warranted."* That note has been quoted in the `ARC-045` and `MECH-166` `evidence_quality_note`s since 2026-08-07 (*"`sws_slot_diversity` (same whole-bank formula) inherits the identical confound across v3_exq_242/243/245/245a/245b/246"*) and was never actioned.

**Scope:** all 32 `ree-v3/experiments/*.py` drivers referencing `sws_slot_diversity` or `slot_cosine_sim`, less the 6 436-family drivers (already adjudicated; `436e` closed 2026-08-13).

---

## Verdict

**One claim is materially affected and was not previously known to be: `INV-044`.** Confidence: **high**.

`INV-044` was **promoted to `provisional`** on 2026-04-19 on the strength of `V3-EXQ-429`, whose outcome gate is `PASS iff (C1 AND C2)` — and **both C1 and C2 are the raw whole-bank statistic**. Both of `INV-044`'s two experimental evidence entries are `V3-EXQ-429` runs, both `supports`, `pass_runs=2 fail_runs=0`. Its promotion note quotes the confounded numbers verbatim as the justification. **100% of `INV-044`'s experimental evidence base is the confounded instrument.**

Three further claims carry the confound in a weaker or already-discounted form (`SD-017`, `INV-010`, `MECH-120`), and one adjacent infrastructure defect was found that is independent of the DV but is what keeps `MECH-120`'s reclassification from taking effect.

**This session applied nothing.** Every disposition below is a proposal for `/governance`, per the precedent this fan-out note itself came from.

---

## The single sentence version

The confound has a **second direction** nobody had characterised: `sws_slot_diversity` is exactly `1 − slot_cosine_sim`, so where `436d`'s C1 **failed for the wrong reason**, every criterion registered as an *absolute lower bound on diversity* **passes for the wrong reason** — an untouched 16-slot bank reads **0.9993 ± 0.0086**, which clears every such threshold in the corpus (0.10, 0.05, 0.02, 0.01) with **P = 1.0000**.

---

## The substrate is unchanged

`run_sws_schema_pass` (`ree-v3/ree_core/agent.py:11328-11343`, re-read 2026-08-13) still computes

```python
sim_mat = torch.mm(normed, normed.t())
mask    = torch.eye(num_slots, ...)      # diagonal only -- NO occupancy mask
diversity = float((1.0 - sim_mat[~mask]).mean())
```

over all 16 slots of `ContextMemory.memory`. This is `436d` F7b confirmed still live: the emitted `sws_slot_diversity` is `1 − slot_cosine_sim` on the same bank with the same mask, and every driver that calls a sleep pass receives it.

**Measured first-hand, not derived** — 400 fresh `ContextMemory(latent_dim=64)` inits on the real substrate:

| statistic | value |
|---|---|
| untouched-bank `sws_slot_diversity` | **0.999284** (sd 0.008610, range 0.968–1.022) |
| `P(diversity > 0.10)` | **1.0000** |
| `P(diversity > 0.05)` | **1.0000** |
| `P(diversity > 0.02)` | **1.0000** |
| `P(diversity > 0.01)` | **1.0000** |

So a **lower** diversity reading means a **more homogeneous** bank. A criterion of the form `diversity > ε` cannot fail from failure-to-differentiate; it can only fail once writes have already collapsed the bank. It is a homogenisation detector being read as a differentiation detector.

---

## Triage of all 26 non-436 drivers

**Load-bearing on the raw whole-bank statistic (11):** `242`, `245`, `245a`, `245b`, `265`, `265a`, `429`, `430`, `500`, `500a`, `673`.
**Records it as a diagnostic only, not load-bearing (11):** `243`, `246`, `385`, `385a`, `418`, `418a`, `418l`, `691`, `901` (marked *"SECONDARY / non-load-bearing / informational"* in its own header), `909` (`claim_ids=[]`), `922` (docstring mention only).
**Already independently fixed (4):** `845`, `861`, `861a`, `861b` — see below.

### The MECH-180 lineage found this first, and fixed it

`845`'s C1b gated on `mean sws_slot_diversity monotone non-decreasing`. `failure_autopsy_V3-EXQ-845_2026-08-01` (user-confirmed routing *"Mixed + redesign the DV"*) identified the **same whole-bank confound six days before the `436d` check**, by a different route — write-count entanglement rather than occupancy — and `861`/`861a`/`861b` now route on `mean_sws_new_slot_diversity` (occupied-this-cycle slots only), retaining the old statistic renamed `mean_sws_slot_diversity_wholebank_legacy` and explicitly **non-gating**.

Two independent lineages converging on the same defect, three months apart, with no shared author, is itself the strongest evidence that the statistic — not any one experiment — is the problem. **The corrected readout already exists in-tree** (`861`, computed by before/after `ContextMemory.memory` snapshot around each pass, no `ree_core` change required) and is the natural template for any repair below.

---

## Findings

### F1 — `INV-044`: an active promotion resting entirely on the confounded instrument *(the finding)*

`v3_exq_429_inv044_bayesian_prior_before_posterior.py:316` — `outcome = "PASS" if (c1_pass and c2_pass)`. Both gating criteria are the raw whole-bank statistic:

| criterion | as registered | measured | problem |
|---|---|---|---|
| **C1** (gating) | `ORDERED mean_sws_slot_diversity > 0.05` in ≥2/3 seeds | ORDERED 0.288 | Threshold is **~20× below the untouched-bank value**. An empty bank passes with P = 1.0000. The measured 0.288 corresponds to whole-bank cosine ≈ **0.71** — substantial homogenisation, read by C1 as success. |
| **C2** (gating) | `ORDERED mean_sws_slot_diversity > WAKING_ONLY final_slot_diversity` in ≥2/3 | 0.288 vs 0.177 | Compares ORDERED's **mid-training per-cycle mean** against WAKING's **end-of-training final** value. Per `436d` F5 the statistic's baseline is Adam drift on `context_memory.memory` and is **non-monotone in training time** — so this compares two different points on a drifting nuisance trajectory. |
| **C4** (not gating, but quoted in the promotion note) | `REM_ONLY < ORDERED` in ALL seeds | REM_ONLY **0.0** in 3/3 | `0.0` is **not a measurement**. It is the initialised default in `run_sws_schema_pass`'s metrics dict (`agent.py:11197`), returned unchanged when `sws_enabled` is `False`. REM_ONLY runs no SWS pass. C4 is guaranteed to pass whenever ORDERED > 0. |

`INV-044`'s `evidence_quality_note` in `claims.yaml`, verbatim:

> *"EXQ-429 PASS (2026-04-18, supports): … **ORDERED mean_sws_slot_diversity=0.290 vs REM_ONLY=0.0 and WAKING_ONLY=0.177**; 3/3 seeds pass all 4 acceptance checks. **Promoted to provisional on governance 2026-04-19.**"*

The leading contrast in the promotion rationale — `0.290 vs 0.0` — is a real readout against a placeholder.

Index state (`claim_evidence.v1.json`, generated 2026-08-13T19:53Z): `genuine_exp_count=2`, `pass_runs=2`, `fail_runs=0`, both entries `V3-EXQ-429` (`20260418T075824Z`, `20260419T075804Z`), `experimental_confidence=0.625`, `overall_confidence=0.768`, `evidence_quadrant=confirmed_established`, status `provisional`.

**There is no unaffected experimental evidence for `INV-044` to fall back on.**

### F2 — `INV-010`: the recorded rationale is inverted *(no direction change; note is wrong)*

`430`'s C3 is `SLEEP mean_sws_slot_diversity > 0.02 in ALL seeds` — passed 3/3 at 0.342 / 0.290 / 0.083. `INV-010`'s `evidence_quality_note` records:

> *"**SWS slots differentiated (C3 3/3)** but did not translate to behavioral harm reduction — symptom of missing MECH-261 mode-conditioned offline-write gating substrate."*

Against an untouched-bank value of 0.9993, those three numbers mean whole-bank cosine ≈ **0.66 / 0.71 / 0.92** — the bank became *substantially more homogeneous*, in one seed nearly totally so. **"Slots differentiated" is backwards.** (`NO_SLEEP` reads `0.0` — the same `agent.py:11197` placeholder as F1.)

`430` is already `non_contributory` so nothing is weighting, and `INV-010` has `genuine_exp_count=0`. But the note's causal story is what currently scopes `INV-010`'s retest eligibility onto MECH-261 substrate maturity, and that story is built on an unsupported premise: the "differentiation happened, behaviour didn't follow" dissociation was never observed.

### F3 — `SD-017`: both supporting runs carry the confound, neither decisively

`SD-017` is `stable`, `pass_runs=2 fail_runs=3`, `exp_conf=0.684`, `overall=0.777`. Both `supports` entries touch the statistic:

- **`265a`** — C2 `mean_sws_slot_diversity > 0.10`, measured 0.257. Same vacuity class as F1's C1 (P = 1.0000 on an empty bank). Not the sole criterion.
- **`500a`** — C3 is `mean_replay_quality >= 8.0` where `replay_quality = rem_n_rollouts + 0.25*sws_n_writes + 0.1*sws_slot_diversity`. Measured 8.09995, with `rem_n_rollouts=6.0, sws_n_writes=8.0` → the non-diversity part is **exactly 8.0**. Under `>=` C3 passes with or without the diversity term, so **the confound is not decisive** — but 100% of the visible margin above threshold is the confounded term, and had the criterion been strict (`>`) it would have been the sole reason for the pass.
  Separately worth governance's eye: `500a` reports `sws_slot_diversity ≈ 0.9995` with `slot_diversity_before_test == slot_diversity_after_test` to full float precision across every cycle and seed — i.e. **the value sits at the untouched-bank null despite 8 writes/cycle**, because 8 EMA-blended writes (`0.9*old + 0.1*new`) barely perturb a near-orthogonal init. The term contributes a near-constant `+0.0999` to `replay_quality` regardless of consolidation quality: it adds a constant, not information.

**Proposal: no direction change for `SD-017`.** Flagged so the two supporting runs are not later cited as independent corroboration of slot differentiation — neither measures it.

### F4 — `MECH-120`: two `weakens` entries governance already voted to discount

`MECH-120` is `candidate`, `pass=1 fail=2`, `exp_conf=0.454`. The two `weakens` entries are both `V3-EXQ-245` runs, whose criteria are `PASS = S1 AND S2` with **both** on `slot_cosine_sim` (100% of the gate).

`claims.yaml` states these were already dealt with: *"EXQ-245 FAIL x2 (2026-04-05, 2026-04-07): **both reclassified to non_contributory** — proxy substrate without full offline-phase architecture."* The flat manifests agree (`non_contributory`, with the 2026-04-08 note).

**The reclassification never reached the indexer.** See F5. `245a`/`245b` (also load-bearing on the statistic) *were* correctly reclassified and are excluded from the genuine count.

The underlying data is degenerate independently of occupancy: in 2/3 seeds **both** arms are pinned at `slot_cosine_sim ≈ 0.9999998` vs `0.999997` — differences at the 1e-6 level, the legacy `write_gate`-as-payload collapse `436d` repaired — and in the third seed the control arm sits at `0.000449`, the untouched-bank null. S2/P1 is **unsatisfiable in 3/3 seeds**, by two different mechanisms.

### F5 — Adjacent infrastructure defect: 26 governance corrections stranded in subdirectory manifests *(not a DV finding — routed separately)*

`build_experiment_indexes.py:1454` resolves the flat sibling as:

```python
flat_manifest = _load_json(base_dir / f"{run_id}.json")     # TOP LEVEL ONLY
```

`_merge_flat_manifest_overrides` (line 1297) is the mechanism by which a governance correction written to the flat manifest overrides a stale run-pack — it fires when *"the flat copy is ANNOTATED and the pack copy is NOT"*, which is exactly `245`'s shape. But when a run's flat manifest lives in an **experiment-type subdirectory** (`v3_exq_245_mech120_shy_normalisation/<run_id>.json`) rather than at `evidence/experiments/<run_id>.json`, the lookup misses, `_load_json` returns `{}`, and the overlay is a **documented no-op** (*"A missing sibling => {} => no-op"*). No warning fires, because the warning is gated on `_flat_applied`.

Confirmed by two cases resolving in **opposite** directions, both matching the pack: `242` (pack `non_contributory` / flat `weakens` → index `non_contributory`) and `245` (pack `weakens` / flat `non_contributory` → index `weakens`).

**Corpus scan** (2817 run packs): 1948 have no top-level flat sibling; of those, **26** have a subdirectory flat manifest that is annotated, a pack that is not, and disagreeing direction fields. Full list in the JSON companion. Beyond the `245` pair they include `v3_exq_244`, `v3_exq_246`, `321a`, `325a`, `325d`, `326a`, `328b`, `395`, `452`(×2), `452a`, `453`(×2), `511`, `514`, `514j`, `526`, `535a`, `537`, `537b`, `537c`, `540f`, `591`, `881` — touching `SD-021`, `SD-032c`, `SD-015`, `MECH-229`, `MECH-230`, `SD-012`, `MECH-220`, `MECH-257`, `SD-013`, `ARC-033`, `MECH-261`, `SD-032a`, `SD-032e`, `SD-049`, `Q-034`, `SD-029`, `MECH-256`, `MECH-307`, `ARC-046` among others.

This is **out of scope for this sweep and must not be fixed here** — it needs its own owner, and several of the 26 are supersession records rather than direction flips. Flagged because it is the reason F4 is still live, and because its blast radius is an order of magnitude wider than this sweep's.

### F6 — `242`: direction already correct, recorded rationale inverted

`242`'s C1 is the exact shape of `436d`'s C1 (`slot_cosine_sim(SWS_ONLY) < slot_cosine_sim(WAKING_ONLY)` in ≥3/5), and it is a **necessary conjunct** (`PASS = C1 AND (C2 OR C4)`) whose value alone determines all three per-claim directions in the driver. The run-pack manifest already reads `non_contributory` for `SD-017`/`ARC-045`/`MECH-166`, and the index agrees — **so nothing is weighting and no direction change is proposed.**

But its note reads *"**Slot differentiation works (4/5 seeds)** but behavioral benefit doesn't follow. Representationally encouraging…"*, and the data says the opposite:

| seed | WAKING_ONLY | SWS_ONLY | reading |
|---|---|---|---|
| 42 | 0.000966 | 0.000448 | both inside the untouched-bank null |
| 7 | 0.002224 | **1.000000** | total collapse |
| 13 | −0.012985 | **1.000000** | total collapse |
| 100 | −0.005960 | **1.000000** | total collapse |
| 200 | −0.002195 | **1.000000** | total collapse |

All five WAKING_ONLY values sit within ±1.6 sd of the untouched-bank cosine null (`436d` F2: mean 0.000145, sd 0.008121) — **the waking arm wrote nothing**, `436d` F1 reproduced three months earlier. The "4/5" in the note is the four seeds reading `1.000000`, which is *total homogenisation* (the legacy `write_gate`-as-payload collapse), not differentiation. C1 is **unsatisfiable in 5/5 seeds**: the comparison arm is at the metric's zero point and writing content can only raise the statistic (`436d` F3). Effective denominator **0**, not 5 — worse than `436d`'s ≤3.

"Representationally encouraging" is the phrase most likely to be cited forward, and it is unsupported.

### F7 — `MECH-171` / `673`: load-bearing, already fully discounted

`673`'s `_compute_slot_diversity` (driver:170) is the identical raw whole-bank formula, and C1/C2 gate on it (`PASS = (C1 AND C3 AND C5) OR (C2 AND C4)` — C1 and C2 sit one in each disjunct). All **7** runs are `non_contributory` (`out_of_domain`, `failure_autopsy_batch9_2026-06-12`) and `MECH-171` has `genuine_exp_count=0`. Latent only — recorded so a future re-scope of `MECH-171` into domain does not silently re-activate a confounded gate.

---

## What this sweep did NOT establish

- **Whether any of the underlying hypotheses are true.** This invalidates instruments, not claims. In particular `INV-044` may well be correct — it has 6 literature entries at `lit_conf 0.863`; what it does not have is uncompromised *experimental* support.
- **What a corrected DV would have reported** for any run here. As with `436d`, no per-slot occupancy or write-index trace is persisted in these manifests, so the occupied-only statistic is not recoverable by post-hoc reanalysis. `861`'s before/after-snapshot method requires a re-run.
- **Whether `500`/`500a`'s `replay_quality` composite is sound in other respects.** Only the `0.1*sws_slot_diversity` term was examined.
- **The other 25 stranded corrections in F5.** Each needs individual adjudication; several are supersessions, not direction flips. Only the `245` pair was traced end-to-end.
- **Any `ree-v2`/`ree-v1` driver.** Scope was `ree-v3/experiments/*.py`.

---

## Recommendations to `/governance` (proposed — not applied)

1. **`INV-044` — the decision this sweep exists for.** Both `V3-EXQ-429` runs (`20260418T075824Z`, `20260419T075804Z`) `supports → non_contributory`, `epistemic_category: measurement_test_design_defect`. This removes 2/2 of its experimental evidence, so **`provisional` is no longer supported by experiment** and the status should be re-derived (`candidate`, or `provisional` explicitly on literature alone with that stated). Amend the `evidence_quality_note` to record that the promotion rationale's leading figure (`REM_ONLY=0.0`) was a metrics-dict placeholder. **This is a demotion-shaped change and should go to the user explicitly**, not be applied as routine cleanup.
2. **`INV-010`** — no direction change. Correct the `evidence_quality_note`: strike *"SWS slots differentiated (C3 3/3)"*, which is backwards, and re-scope the retest gate, since the MECH-261 attribution rests on a dissociation that was never observed.
3. **`MECH-120`** — no *new* decision needed; **execute the one already taken.** Propagate the 2026-04-08 `non_contributory` reclassification of both `V3-EXQ-245` runs into their run-pack manifests. Expected effect: `fail_runs` 2 → 0, `genuine_exp_count` 3 → 1, `exp_conf` rises from 0.454.
4. **`SD-017`** — no direction change. Add a note that neither supporting run (`265a`, `500a`) measures slot differentiation, so they must not be cited as corroboration of it.
5. **`242`** — no direction change. Correct the run-pack note; "Slot differentiation works (4/5 seeds)" is the four collapsed seeds.
6. **Substrate repair, the durable fix.** `run_sws_schema_pass` should emit an occupancy-masked statistic alongside (not instead of) the legacy one, following `861`'s already-proven pattern — similarity and occupancy `k` reported **separately**, never their product. Until then, **no new criterion should be pre-registered on `sws_slot_diversity`**, and the absolute-threshold form (`diversity > ε`) should be prohibited outright: it is satisfied by an empty bank at P = 1.0000.
7. **Route F5 to its own owner.** 26 stranded governance corrections is a coordination-plane defect with far wider blast radius than this sweep; it needs a dedicated pass, not a side-fix here.

### Fan-out worth governance's attention

`909` (`v3_exq_909_sleep_dv_fishtank_multifiring.py:478`) uses `sws_slot_diversity > 0.01` as half of its pre-registered *"is the sleep DV non-null"* discrimination rule. An untouched bank clears that threshold with P = 1.0000, so the probe can report `sleep_dv_nonnull_detected` for a bank nothing was written to. `claim_ids=[]` and it weights no claim, so this is **not** a claim-layer finding — but `909` exists to decide whether the sleep DV is live for `sleep_substrate_plan.md` GAP-2, and that decision is being made with a detector that cannot return "null".

---

## Reproduction

- Substrate re-read: `ree-v3/ree_core/agent.py:11328-11343` (`run_sws_schema_pass` diversity block), `:11197` (metrics-dict default), `ree_core/predictors/e1_deep.py:36-60` (`ContextMemory`).
- Untouched-bank null: 400 fresh `ContextMemory(latent_dim=64)` inits on the real substrate, whole-bank `mean(1 − off_diag_cosine)`.
- Driver criteria: `grep -l "sws_slot_diversity\|slot_cosine_sim" ree-v3/experiments/*.py` (32 hits, 26 after excluding the 436 family), each read at its `outcome =` / `PASS criteria` site.
- Directions: `runs/<run_id>/manifest.json` (**authoritative** — the flat sibling is stale for several of these; see F5), cross-checked against `evidence/experiments/claim_evidence.v1.json` generated 2026-08-13T19:53:12Z.
- F5 scan: 2817 run packs, comparing subdirectory flat siblings against packs on `_FLAT_AUTHORITATIVE_FIELDS` under the `_is_annotated` gate.

---

## Claims

`task_claim.py open --resources REE_assembly/docs/claims/claims.yaml` returned **exit 3** naming this session as OWNER (earliest `claimed_at`); three stale `igw-auto-*` claims (>6h) also name the file and were reported as notes. No `claims.yaml` edit was made regardless — dispositions are governance's call.

Artifact paths were claimed under a second entry (`…-artifact`) once the dated filenames were known, per CLAUDE.md's rule that a resource discovered mid-task is claimed before it is written.


---

# Confirmation — 2026-08-20

Confirmed at the interactive `/failure-autopsy` Step 8 gate by session
`failure-autopsy-slotcosine-confirm`, six days after the headless draft. The draft was
**re-verified from source rather than accepted**, and three things had moved underneath it.

## Independent re-verification

| Draft claim | Check performed | Result |
|---|---|---|
| Substrate unchanged, diagonal-only mask | read `ree_core/agent.py` at `ree-v3` HEAD | **Confirmed.** `mask = torch.eye(...)`, no occupancy mask. Region last modified **2026-04-09** (`19b7c2d`) — four months untouched. The two uncommitted edits live in the tree (lines 238, 8422; CEM modulatory-authority build) do not touch `run_sws_schema_pass`. |
| `sws_slot_diversity ≡ 1 − slot_cosine_sim` | read the computation | **Confirmed literally** — `diversity = float((1.0 - off_diag).mean().item())`. |
| `REM_ONLY = 0.0` is a placeholder | read metrics dict + guard | **Confirmed structurally** — `"sws_slot_diversity": 0.0` initialised, then `if not self.config.sws_enabled: return metrics`. A REM_ONLY arm emits `0.0` having measured nothing. |
| Untouched bank ≈ 0.9993; every threshold P = 1.0000 | **probe re-run independently**, 200 fresh `ContextMemory(latent_dim=64)` inits, seeds 10000–10199, on the live substrate | **Reproduced.** mean **1.000386**, sd **0.008664**, range 0.969782–1.019436. `P(>0.10) = P(>0.05) = P(>0.02) = P(>0.01) = 1.0000`. Independent seeds, same distribution as the draft's n=400 (0.999284 ± 0.008610). |
| `INV-044` still rests 2/2 on the confounded gate | `claim_evidence.v1.json` (2026-08-18T21:27:48Z) + `claims.yaml` | **Confirmed and still live.** `genuine_exp_count=2, pass_runs=2, fail_runs=0`, both entries `V3-EXQ-429`, `exp_conf 0.625`, quadrant `confirmed_established`, `lit_conf 0.861`, overall `0.767`. `claims.yaml` still reads `status: provisional`, `live_status.evidence.from` the 2026-04-19 run, `needs_review: false`. **Nothing has been applied.** |
| Dry-run gate (Step 2a, mandatory) | every cited family | **Passes — 0 dry runs cited.** A dry smoke *does* exist in the 429 family (`20260415T143340Z`) and is correctly absent from both this artifact's citations and the index. Recorded rather than omitted so a later reader need not re-derive the concern. |

**The finding stands.** An untouched 16-slot bank reads ~1.0, so a criterion of the form
`diversity > ε` is satisfied with certainty by a bank nothing was written to.

## What had moved since 2026-08-13

**Recommendation 3 (`MECH-120`) — ALREADY DISCHARGED. Do not re-apply.**
The F5 indexer fix landed 2026-08-14 (`chip-20260814-indexer-flat-sibling-subdir-lookup`,
`done`; `REE_assembly` `d3e6872db8` code+tests, `e030b03b4c` regen). `_resolve_flat_sibling`
now falls back to the experiment-type subdirectory after the top-level lookup. The live index
confirms `MECH-120` at `genuine_exp_count=1, pass_runs=1, fail_runs=0, exp_conf 0.643,
confirmed_established` — matching this sweep's **pre-registered prediction** (`fail 2→0`,
`genuine 3→1`) exactly. A rare case of an autopsy's numeric prediction being checked against
its own repair.

**Recommendation 7 (route F5) — ALREADY DISCHARGED.** Same chip. The 26 stranded corrections
resolved as 19 direction flips, 5 supersessions, 1 per-claim map, 1 `non_degenerate` backfill,
with confidence deltas recorded for 14 claims.

**Recommendation 4 (`SD-017`) — STRENGTHENED, not superseded.** `V3-EXQ-436f`, the corrected
occupied-only-DV armed retest, **ran** on 2026-08-14 and returned **FAIL / `non_contributory`**,
self-routing `insufficient_occupancy_for_c1`: arming the full SD-016 production combination
moved write-path slot occupancy by *exactly zero seeds*. Already autopsied and
governance-processed 2026-08-16 (`failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16`).
So `SD-017` has still never had slot differentiation measured — now for a **second, upstream**
reason. Recommendation 4 stands and is reinforced.

**Recommendation 6 — partially overtaken by practice; substrate still unrepaired.** The corpus
grew **32 → 35** drivers referencing the statistic. All three additions use the *corrected*
pattern: `436f` computes `slot_cosine_sim_occupied_only` and records the raw whole-bank value
as non-gating `slot_cosine_sim_raw_whole_bank`; `861c`/`861d` gate on
`mean_sws_new_slot_diversity` with the legacy statistic retained as
`mean_sws_slot_diversity_wholebank_legacy`, **recorded and not scored**. So no new criterion has
been pre-registered on the raw whole-bank statistic in the six days since. **But** the
prohibition is written nowhere binding, and `run_sws_schema_pass` still emits *only* the
confounded statistic to every driver that calls a sleep pass.

## Corrections made at confirmation

1. **`recommended_epistemic_category` for `INV-044`: `measurement_test_design_defect` → `standard`.**
   The draft's value is **outside the eight-value enum** (`validate_claims.VALID_EPISTEMIC_CATEGORIES`).
   Governance writes this field into `claims.yaml` **verbatim**, where `--strict` raises an ERROR —
   *after* the value is already in the registry. `standard` is the behaviour-preserving mapping: it
   asserts no epistemic suppression, which is the correct verdict (the claim is **untested**, not
   substrate-gated), and it leaves GOV-GRAN-1 surfacing and v3-testability unchanged. The
   failure-mode wording is preserved in `recommended_epistemic_category_note`.
2. **`targets[]` and `per_claim_recommendation` added.** The draft was sweep-shaped with no
   `targets[]`, which makes a confirmed disposition **invisible to GOV-APPLY-1** — it reads
   `targets[].per_claim_recommendation` and nothing else. That is the precise route by which an
   unapplied demotion decays into a standing positive claim.
   **`targets[]` deliberately contains only the two `V3-EXQ-429` runs** — the sole runs whose
   direction this sweep adjudicates. Recommendations 2, 4 and 5 are *note* corrections with no
   direction change, and `242`/`430`/`265a`/`500a` already carry their own adjudications; adding
   them as targets would make this artifact the **latest** adjudication of those run_ids under the
   re-derive brake's R2 latest-wins rule and silently supersede readings this sweep never re-derived.
3. **`failure_location` added** per GOV-FAILLOC-1.

## Failure-location summary (GOV-FAILLOC-1)

**MEASURES FAILED — solo.** Implementation reads *complete* (`run_sws_schema_pass` does exactly
what it declares); environment is not implicated; the dependent variable is the defect.
`mechanism: not_established`, `measures: established`, `environment: not_established`,
`ree: false`. This sweep invalidates **instruments, not hypotheses** — no REE-level or
mechanism-level failure read is licensed by it, and `INV-044` in particular may well be correct.

## Dispositions confirmed by the user

**Recommendation 1 — `INV-044`.** Both `V3-EXQ-429` runs `supports → non_contributory`,
`epistemic_category: standard`. **Status: retain `provisional`, re-scoped explicitly to the 6
literature entries (`lit_conf 0.861`)**, with the `evidence_quality_note` recording that its
experimental support was withdrawn as instrument-invalid. Rationale: the claim was *never tested*,
as opposed to tested and found wanting — demoting to `candidate` would read in the registry as
evidence **against** `INV-044` when no experimental evidence exists in either direction.

**Recommendation 6 — both halves.** Route a `validate_experiments.py` lint flagging any driver
that gates on the raw whole-bank `sws_slot_diversity` with an absolute threshold, **and** the
substrate repair emitting the occupancy-masked statistic alongside the legacy one, following
`861`'s proven pattern (similarity and occupancy `k` reported **separately**, never their
product). Rationale: the corpus is demonstrably drifty here (32 → 35 in six days), and a written
rule with no detector is exactly what let this defect run for four months across two independent
lineages.

Both answers matched the recommended option and are recorded in `RECOMMENDATION_LOG.jsonl`.

## Status after confirmation

- **Live for `/governance`:** recommendations **1, 2, 4, 5, 6** (+ the `909` fan-out note).
- **Discharged, do not re-apply:** recommendations **3, 7**.
- **No hypothesis-ledger write.** Step 9b does not apply: `fanout_recommendation.is_discrimination`
  is `false` (the `909` note is an observation about a detector, not a rival-hypothesis portfolio)
  and the draft carries no `hypothesis_space_ledger_pending` block. Nothing was appended to
  `hypothesis_space_registry.v1.json`.
- **No follow-on chip spawned.** Per `/failure-autopsy` Step 8 (2026-07-30 rule), an autopsy does
  not `spawn_task` work its own routing names — `/governance` ratifies at its Step 2b first. The
  recommendation-6 lint and substrate repair are recorded here for governance to chip once ratified.
