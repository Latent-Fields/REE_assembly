# Architecture-epoch stale-evidence review (2026-06-02)

Implements `outstanding_tasks_triage_2026-06-02.md` item 5. Two parts:
**(a) indexer enhancement** (LANDED — safe, scoring-neutral) and
**(b) scoped review** (THIS MEMO — surfaced for user approval; **no tags applied**).

The epoch gate (`planning_criteria.v1.yaml`: `epoch_start_utc=2026-02-27`,
`stale_if_timestamp_before_epoch_start`) is **time-only**: it drops pre-hybrid-guardrails
synthetic runs and nothing else. Nothing flags evidence as stale when a substrate it
*mechanistically depends on* changed AFTER the evidence was recorded (but after the epoch
start). This memo audits the 2026-05-09 .. 2026-06-02 substrate-landing wave for that
second kind of staleness.

---

## Part (a) — Indexer enhancement (LANDED)

`build_experiment_indexes.py` now honors two manually-set manifest fields:

- `pending_retest_after_substrate: true` (bool / truthy string)
- `superseded_by_substrate: "<SD-id>@<YYYY-MM-DD>"` (reference string)

Either flag tags the entry `scoring_excluded: "stale_substrate"` (parallel to the existing
`stale_epoch` / `invalid_run` / `superseded` / `*_probe` / `non_contributory` exclusions).
The entry stays in the full `claim_evidence.v1.json` `entries[]` audit log (with the
`superseded_by_substrate` ref echoed) but no longer weights confidence, conflict ratios,
the promotion/demotion gate, or conflict detection. **Absent fields ⇒ bit-identical.**

Contract coverage: `scripts/test_substrate_staleness_gate.py` (9 tests, all green).

**Verified scoring-neutral on landing.** A same-moment old-code-vs-new-code diff of
`claim_evidence.v1.json` showed **7 entry relabels and 0 claim-level confidence/conflict
changes**:

| run | claims | before → after |
|-----|--------|----------------|
| `v3_exq_603d_…scaffolded_sd054_20260601T095345Z_v3` | MECH-260, MECH-313, Q-045 | `non_contributory` → `stale_substrate` |
| `v3_exq_610b_inv074_crystallization_necessity_20260601T122002Z_v3` | INV-074, MECH-333, MECH-334, MECH-341 | `non_contributory` → `stale_substrate` |

These two runs already carried `pending_retest_after_substrate: true` in their **nested**
`runs/.../manifest.json` (placed by prior diagnose/autopsy sessions) and were already
excluded as `non_contributory`, so the relabel is cosmetic — confidence is unchanged.

### CRITICAL operational note: nested manifest, not flat file

The indexer reads experiment manifests from `evidence/experiments/<exp>/runs/<run_id>/manifest.json`,
**not** the flat `evidence/experiments/<run_id>.json` mirror. Several flat files carry
`pending_retest_after_substrate: true` while their nested manifest does **not** (e.g. the
`v3_exq_543f/543g/543h_arc062_*` falsifiers). Those flags are therefore **NOT honored** —
the flat-file flag is informational only.

**To make a flag take effect, write it to the nested `runs/.../manifest.json`.** Any
re-tagging the user approves below must target the nested manifest.

---

## Part (b) — Scoped review (FOR APPROVAL — nothing applied)

### Headline conclusions

1. **The SD-012 fan-out (38 dependents) is a false-positive cluster — do NOT re-validate
   any of it.** The 2026-05-17 SD-012 amendment is `drive_ema_alpha` with **default 1.0 =
   bit-identical** to the prior instantaneous form (ree-v3/CLAUDE.md ~line 514-516,
   contracts C1/C2). No mechanism changed at the default. Revisit only if a future MECH-306
   decision promotes `alpha < 1.0` as default.
2. **Genuine stale-evidence concern concentrates on MECH-090 and the SD-037/MECH-281
   cascade.** The 2026-05-28/29 MECH-090 commit-entry-predicate (R-c readiness conjunction)
   landing changes what MECH-090 itself and its committed-mode downstream (ARC-029) measure;
   the 2026-05-30 SD-037/MECH-281 consumer-cascade amend superseded the inert `483c`
   broadcast run.
3. **The `pending_retest_after_substrate` flag is currently autopsy-side only.** Of ~43
   autopsy blocks asserting it, only ~6 nested manifests actually carry the field. Honoring
   the others requires writing the field into their nested manifests (plus a filename
   reconciliation for ~10 EXQ-level references that don't resolve to a single manifest).

### (B.1) Substrate landings in window (primary source: ree-v3/CLAUDE.md)

Mechanism-changing landings are **bold**; the rest are additive/no-op/robustness fixes.

| Substrate | Landed | Nature | Mechanism-changing? |
|-----------|--------|--------|---------------------|
| ARC-062 gated-policy (GAP-A) | 2026-05-09 | policy heads + context discriminator | yes (own claim) |
| MECH-313 stochastic noise floor | 2026-05-10 | LC-NE tonic analog | additive |
| MECH-314 curiosity bonus (+a/b/c) | 2026-05-10 | exploration bonus | additive |
| MECH-319 sim-mode write gate | 2026-05-10 | categorical replay tag | additive |
| MECH-320 tonic vigor bias | 2026-05-10 | DA-vigor score bias | additive |
| SD-054 bipartite layout | 2026-05-11 | env spawn partition | env knob |
| **MECH-307 anticipatory affect** | 2026-05-11 (+recalib 05-12) | split affect channels | **yes (own claim)** |
| SD-055 differentiable CEM | 2026-05-15 | softmax-weighted selection approx | selection path |
| INF-ENV-001 harm-gradient | 2026-05-16 | env feature | env knob |
| **ARC-065 SP-CEM main-path** | 2026-05-17 | SP-CEM is now the default live action path | **yes — broad** |
| SD-012 sustained-drive EMA | 2026-05-17 | `drive_ema_alpha` default 1.0 | **NO (no-op default)** |
| **INV-074 / MECH-333 / MECH-334** | 2026-05-17 | plasticity-injection crystallization + EWC write-protect | **yes (own claims)** |
| ARC-062 differential-heads fix | 2026-05-18 | robustness fix | no (robustness) |
| MECH-339 composite cue / outshining | 2026-05-19 | retrieval cue | additive |
| ARC-062 GAP-B mode-separation floor | 2026-05-20 | floor constraint | own claim |
| MECH-282 LPB interoceptive routing | 2026-05-21 | routing | own claim |
| MECH-286 override-gated sleep onset | 2026-05-21 | sleep gate | own claim |
| MECH-340 persistence/efficacy gate | 2026-05-21 | gate | own claim |
| **MECH-341 E3 score diversity** | 2026-05-27 (+retune 05-28, +amend 06-01) | stratified select on the action path | **yes (own claim)** |
| **MECH-090 commit-entry predicate** | 2026-05-28 / 2026-05-29 | R-c readiness conjunction; nav_competence axis | **yes — own claim + downstream** |
| **SD-056 E2 action-conditional divergence** | 2026-05-29 (+multi-step 05-31) | contrastive next-state | **yes (own claim)** |
| **SD-037 / MECH-281 consumer-cascade** | 2026-05-30 | motor-coupling axis amend | **yes** |
| SD-022 ext / MECH-302 | 2026-05-30 | scheduled-injection env extension | env knob |
| SD-049 Phase 3 | 2026-05-31 | SD-032 per-axis consumer read | own claim |
| scaffolded_sd054_onboarding (+amend 06-02) | 2026-05-31 / 06-02 | onboarding scaffold + update_z_goal | own scaffold |

(Cross-checked against `substrate_queue.json` `implemented_utc` flips: SD-049-PHASE-3 05-31,
MECH-307 05-11, ARC-062 05-09, SD-055 05-15, INF-ENV-001 05-16 — all consistent.)

### (B.2) Per-entry recommendations (candidate-stale SCORING entries)

The raw cross-reference returned ~95 pre-landing scoring entries; after removing the SD-012
no-op fan-out and orthogonal-axis listings, the actionable set is small. **Recommendation
codes:** REVALIDATE (queue an EXQ), MARK (`pending_retest_after_substrate` on the nested
manifest — stop weighting, no fresh experiment yet), KEEP (weak/no real dependence).

| claim | run_id | entry ts | substrate (landed) | rec | conf | rationale |
|-------|--------|----------|--------------------|-----|------|-----------|
| MECH-090 (self) | `v3_exq_049a_mech090_bistable_concordance_*` + `321a` + `321b` (×3) | 2026-04-16..19 | MECH-090 (05-28) | **MARK** | med | Tested the *old* beta-gate/bistable commit gate; the R-c readiness-conjunction landing changes the commit-entry predicate MECH-090 measures. Stop weighting until 592d/e/f-class re-validation lands. |
| ARC-029 | `v3_exq_063_*` + `v3_exq_125_committed_mode_*` (×2) | 2026-03-22 / 03-29 | MECH-090 (05-28) | **MARK** | med | Committed-mode harm outcomes are directly downstream of the commit-entry gate; the new conjunction changes *when* commitment is entered. Stale; no fresh EXQ required yet. |
| MECH-281 / MECH-280 / SD-037 | `v3_exq_483c_sd037_broadcast_gap4_tier1_20260521T064444Z_v3` | 2026-05-21 | SD-037/MECH-281 (05-30) | **REVALIDATE → confirm superseded** | high | 483c's inert downstream coupling is what *routed* the 05-30 cascade amend (483c→483d→483e autopsy chain). Almost certainly already superseded by 483e — **action: confirm 483e supersession is recorded, then 483c needs no separate flag.** |
| MECH-307 (self) | `v3_exq_539_mech307_commit_gating_check_20260508T185404Z_v3` | 2026-05-08 | MECH-307 (05-11/12) | **MARK** | med | Ran before the split-channel landing + default recalibration; the 540g re-run is the live evidence. Should stop weighting. |
| SD-049 (self) | `v3_exq_514b_*` (05-05) + `v3_exq_514j_*` (05-23) | 2026-05-05/23 | SD-049 (05-31) | **MARK** | med | Self-evidence before the Phase-3 per-axis consumer-cascade read changed what SD-049 exposes downstream. |
| MECH-104, MECH-091, MECH-106, SD-021 (under MECH-090.depends_on) | ~14 runs | 2026-03..04 | MECH-090 (05-28) | **KEEP** | high | Listed only because each ∈ `MECH-090.depends_on`; their mechanisms (volatility/surprise gating, phase-reset, BG hysteresis, descending pain) are orthogonal to the commit-entry decisiveness axis. No real dependence. |
| ARC-065 (self) | `v3_exq_567_*_sp_cem_2026-05-15` (×2) | 2026-05-15 | ARC-065 (05-17) | **KEEP** | high | These runs *are* the evidence basis for the SP-CEM main-path landing — they already ran SP-CEM. Not stale. |
| SD-012 fan-out (INV-052/053, Q-034, MECH-186/187/188/230, SD-015, ARC-036/042, SD-032c, SD-049, …≈30) | various | 2026-04..05 | SD-012 (05-17) | **KEEP** | high | No-op-default EMA amendment (see headline #1). |
| SD-022 / SD-047 / SD-048 | `v3_exq_319`, `v3_exq_323a`, `v3_exq_510`, `v3_exq_512a` | 2026-04-10..05-04 | SD-022 (05-30) | **KEEP** | high | The 05-30 SD-022 landing is an additive scheduled-injection env knob; does not alter harm-stream dissociation or the comparator-gap axis. |
| MECH-229 | `v3_exq_326a_wanting_gradient_nav_fix` (×2) | 2026-04-13 | SD-049 (05-31) | **KEEP** | med | SD-049 Phase 3 is a SD-032 consumer read; MECH-229 wanting-gradient nav is not re-measured by it. |

**Net:** REVALIDATE/confirm-supersession ×1 (483c), MARK ×~5 clusters (MECH-090 bistable trio,
ARC-029 pair, MECH-307 539, SD-049 514b/514j, MECH-090-self), KEEP for the large remainder.

### (B.3) Cross-check — existing `pending_retest_after_substrate` autopsy tags vs nested manifest

~43 `failure_autopsy_*` blocks assert the flag. Most reference a FAIL/non_contributory run
(already `scoring_excluded`), a separate population from B.2. Only the nested manifests below
already carry the field (the indexer now honors these):

`v3_exq_543i_…20260518T191052Z_v3`, `v3_exq_543h_…crystallization_falsifier_20260518T000930Z_v3`,
`v3_exq_483e_sd037_consumer_cascade_4arm_20260530T195925Z_v3`,
`v3_exq_569e_sd056_mechanism_probe_…20260531T004944Z_v3`,
`v3_exq_603d_…scaffolded_sd054_20260601T095345Z_v3`,
`v3_exq_614b_mech341_p3_…sd056_amended_20260531T182040Z_v3`
(+ `v3_exq_610b_…20260601T122002Z_v3`).

**Autopsy asserts the flag but the nested manifest does NOT carry it** (would need the field
written for the gate to honor — FAIL/non_contributory, so mostly already excluded; writing the
flag would relabel `non_contributory → stale_substrate`, scoring-neutral but more accurate):
`v3_exq_572`, `v3_exq_573`, `v3_exq_577`, `v3_exq_603c`, `v3_exq_517b`, `v3_exq_543i_20260521T035802Z`,
`v3_exq_543l_…20260526T023059Z`, `v3_exq_592f_…20260601T194325Z`, `v3_exq_598_…20260521T070715Z`,
`v3_exq_603a/603b/603c/604/605`, `v3_exq_606_…20260521T090253Z`, `v3_exq_610a_…20260529T224419Z`,
`v3_exq_616_…20260531T141508Z`, `v3_exq_622_…20260531T223804Z`, `v3_exq_625b_…20260601T181233Z`.

**Manifest not found at the asserted run_id** (autopsy uses an EXQ-level reference, not the
manifest filename — needs filename reconciliation before tagging): EXQ-566-582 / 575 / 588 / 591
GAP runs and the V3-EXQ-455a cluster (455, 447, 448, 445h, 325d).

---

## Recommended next actions (pending user approval)

1. **Apply MARK (nested-manifest `pending_retest_after_substrate: true`)** to the B.2 MARK set
   (MECH-090 bistable trio + ARC-029 pair + MECH-307 539 + SD-049 514b/514j). Scoring-neutral
   for any that already read non_contributory; genuinely de-weights the rest.
2. **Confirm 483c is already superseded by 483e** (B.2 REVALIDATE row); if so, no new EXQ.
3. **Optionally backfill the nested-manifest flag** for the B.3 "asserts but missing" autopsy
   set so the audit trail is machine-consistent (scoring-neutral — they're already excluded).
4. **Do NOT touch** the SD-012 fan-out or the KEEP rows.

Durable follow-ups landed alongside this memo: `substrate_dependencies.json` (date-stamped
substrate→dependent-claim registry) and an evidence-staleness audit step added to the
substrate-landing routine in `/governance` and `/implement-substrate`.

---

## RESOLUTION (2026-06-02, applied)

The MECH-090 release-path audit landed in parallel (`mech090_release_path_audit_2026-06-02.md`,
verdict **B3b**: all four existing release pathways verdict NO; admission-only is the
architectural commitment; the 592f `pending_retest_after_substrate` reach-claim flag stays
TRUE). Two consequences refined the application below:

1. **MECH-090 bistable runs → KEEP (review reversed).** The audit established the bistable
   *latch* (hold-rate / concordance — what `049a`/`321a`/`321b` measure) is INTACT; only
   *admission* gained a readiness pre-condition. Those runs measure the unchanged latch, so they
   are NOT stale. The B.2 "MARK the MECH-090 bistable trio" recommendation is withdrawn.

2. **Run-level gate is insufficient for multi-claim manifests.** `v3_exq_539` (MECH-307) also
   tags MECH-216/205/093 (supports) + SD-014; `v3_exq_514b/j` (SD-049) also tag SD-015 (weakens)
   + MECH-229/230. A run-level `stale_substrate` flag would have wrongly de-weighted those
   co-tagged, non-stale claims. The indexer was therefore extended with a **per-claim** form —
   `pending_retest_after_substrate_per_claim: [claim_id]` and
   `superseded_by_substrate_per_claim: {claim_id: "<id>@<date>"}` — mirroring
   `evidence_direction_per_claim`. Contract coverage added (12 tests total).

**MARKs applied** (per-claim, on the nested `runs/<id>/manifest.json`; verified surgical via a
same-moment old-vs-new-indexer diff = exactly these 4 entries, zero collateral):

| run (nested manifest) | claim MARKed | ref | exp_conf effect |
|------------------------|--------------|-----|-----------------|
| `v3_exq_063_arc029_committed_mode_harm_outcomes` | ARC-029 | `MECH-090@2026-05-28` | 0.454 → 0.179 |
| `v3_exq_539_mech307_commit_gating_check` | MECH-307 | `MECH-307@2026-05-11` | 0.53 → 0.48 |
| `v3_exq_514b_sd049_phase_2_behavioural_validation` | SD-049 | `SD-049@2026-05-31` | (combined) |
| `v3_exq_514j_sd049_phase2_reef_mech307_spcem` | SD-049 | `SD-049@2026-05-31` | 0.375 → 0.0 |

Co-tagged claims confirmed UNAFFECTED: MECH-216/205/093, SD-014, SD-015, MECH-229/230.

**Governance consequence to watch:** ARC-029 (now 0.179) and SD-049 (now 0.0 experimental) are
left with thin/no experimental evidence after de-weighting — both are now genuine **REVALIDATE**
candidates (queue a post-landing EXQ) rather than merely de-weighted. The de-weight is durable in
the manifests; live scoring refreshes on the next `/governance` index rebuild.

**Still open (not applied):** ~~confirm `483c` superseded by `483e`; optional backfill of the B.3
"asserts-but-missing" autopsy manifests (scoring-neutral)~~ — **BOTH CLOSED 2026-06-02, see the
CLOSURE section at the end of this memo.** SD-012 fan-out + KEEP rows untouched.

---

## REVALIDATION STATUS (2026-06-02) — read before re-queuing anything for ARC-029 / SD-049

The two REVALIDATE candidates above were dispositioned the same day. **Do not re-queue either —
both are already in flight:**

### ARC-029 → V3-EXQ-063a QUEUED (ree-v3 main, commit 1e7fdc9)

`experiments/v3_exq_063a_arc029_committed_mode_harm_outcomes_rc_gate.py` (supersedes V3-EXQ-063).
Re-runs the identical 063 2×2 gate×environment committed-mode harm-outcomes design with
`config.heartbeat.use_commit_readiness_gate=True` so commit ENTRY is governed by the MECH-090 R-c
commit-entry predicate that landed 2026-05-28 (the staleness cause). Within-tick decisiveness axis
only (floor 0.05; wiring verified: margin<0.05 blocks / ≥0.05 admits / gate-OFF admits
unconditionally). Across-tick nav_competence axis intentionally OFF — it needs a per-tick harness
`notify_outcome` push this eval design does not emit, so it would sit fail-open and add no signal.

**Result-interpretation routing (for /governance + /failure-autopsy when 063a completes):**
- **PASS** (C1–C5) → ARC-029 supports; replaces the de-weighted 063 evidence on the current substrate.
- **C3 FAIL** (`n_committed_active_stable ≤ n_uncommitted`) is the load-bearing branch and is **NOT
  noise**: it means the R-c readiness gate now *suppresses commitment* in this environment — a
  substantively different ARC-029 verdict than the original 063 PASS (the gate that was supposed to
  help committed-mode no longer fires). Route to **/failure-autopsy**, not /diagnose-errors: the
  question is whether the commit-entry predicate's `commit_readiness_floor=0.05` is mis-calibrated
  for this env's score-margin distribution, or whether committed-mode is genuinely no longer entered
  under R-c gating. Do not silently re-tune the floor — that is a substrate decision.
- **C1/C2 FAIL with C3 PASS** → committed-mode is entered under the R-c gate but no longer produces
  the harm advantage / volatility narrowing → ARC-029 weakens on the current substrate (governance
  demotion candidate).

### SD-049 → ALREADY COVERED by queued V3-EXQ-514l — DO NOT queue a separate 514m

`V3-EXQ-514l` (already in `ree-v3/experiment_queue.json`, status=claimed; supersedes 514k) IS the
SD-049 Phase-3 revalidation: it runs `use_sd049_per_axis_consumer_cascade=True` (the exact Phase-3
substrate that landed 2026-05-31 and de-weighted 514b/514j), tags SD-049, and tests the wanting≠liking
dissociation (C6) + goal_resource_r lift (C4/C5) — SD-049's load-bearing acceptance criteria. When it
runs it re-establishes SD-049 evidence on the current substrate automatically. Its title foregrounds
MECH-229, but its `claim_ids` include SD-049 and its acceptance grid IS the SD-049 behavioural test.
Queueing a separate SD-049 EXQ would duplicate it and contaminate both runs' evidence records.

### MECH-307 (v3_exq_539) — no separate revalidation queued

The 539 MARK de-weighted MECH-307's pre-split-channel commit-gating run; the live MECH-307 evidence is
already the post-recalibration 540g lineage (ree-v3/CLAUDE.md "MECH-307 Default-Value Recalibration").
No new EXQ needed — the de-weight simply stops the stale 539 entry from weighting; 540g carries MECH-307.

---

## CLOSURE (2026-06-02) — the two "Still open" bookkeeping items

Both scoring-neutral / audit-hygiene items above are now closed. Manifest edits landed on the nested
`runs/<id>/manifest.json` (the indexer-read copy); the index relabels apply on the next `/governance`
rebuild (the regenerated index was NOT committed here — it carried unrelated concurrent manifest drift,
same handling as the B.2 MARK session).

### (1) 483c supersession — was NOT recorded; now recorded (this is a real de-weight, not scoring-neutral)

The B.2 row assumed "almost certainly already superseded by 483e — confirm, then 483c needs no flag."
On inspection the supersession was **not** recorded anywhere: `v3_exq_483c`'s nested manifest read
`evidence_direction: mixed` (per-claim SD-037=weakens, MECH-280/281=unknown) and **was still weighting**;
neither the `483e` nested manifest nor `483c`'s carried a supersession reference. The chain is genuine:
`483d`'s docstring states *"Supersedes V3-EXQ-483c. Root cause of 483c failure: C2 measured agent.dacc
which was [the wrong attribute]"* and `483e` (`...consumer_cascade_4arm_20260530T195925Z_v3`) supersedes
`483d`. So `483c`'s scoring contribution came from a **defective harness** and was spurious.

**Action taken:** set `evidence_direction: "superseded"` + `evidence_direction_note` (+ informational
`superseded_by`) on `483c`'s nested manifest; cleared `evidence_direction_per_claim` (canonical for a
superseded run, mirrors the indexer's auto-supersede path). Run-level `superseded` excludes all three
tagged claims (`scoring_excluded: superseded`).

**Governance consequence (parallels the ARC-029 / SD-049 MARK outcome).** `483c` was the **only** genuine
experimental entry for SD-037, MECH-280, and MECH-281, and the superseding runs `483d`/`483e` are
themselves `non_contributory`. So de-weighting `483c` drops the **experimental** confidence of all three
to **0.0** (HEAD→post-edit, verified via same-code old-vs-new manifest diff; zero collateral on any other
claim):

| claim | exp_conf before → after | genuine_exp_count | note |
|-------|-------------------------|-------------------|------|
| SD-037 | 0.297 → 0.0 | 1 → 0 | overall_confidence (decoupled) rose 0.719→0.86 as a spurious *weakens* left scoring; lit unaffected |
| MECH-280 | 0.452 → 0.0 | 1 → 0 | sole entry was 483c (mixed) |
| MECH-281 | 0.452 → 0.0 | 1 → 0 | sole entry was 483c (mixed) |

These three are now genuine **REVALIDATE** candidates on the SD-037/MECH-281 consumer-cascade axis (no
contributory experimental evidence post-supersession). Note SD-037 itself remains `implemented` with
*other* active streams (483b readiness PASS, 620b axis-a PASS, 625c axis-b queued) — the zero is specific
to the broadcast/consumer-cascade evidence that 483c/d/e were probing. Do not double-queue against the
existing axis-b work; route a consumer-cascade revalidation only if governance wants the MECH-280/281
broadcast axis re-established.

### (2) B.3 backfill — applied, verified scoring-neutral (17 nested manifests)

Wrote `pending_retest_after_substrate` to the nested manifests of the B.3 "asserts-but-missing" set,
using the **per-claim** form (`pending_retest_after_substrate_per_claim: [...]`) on multi-claim manifests
and targeting **only the claims that currently read `non_contributory`** so no co-tagged scoring claim is
de-weighted (per the RESOLUTION note on `v3_exq_539` co-tagging). Verified scoring-neutral by a
same-moment indexer diff: **0 claims with any confidence/conflict delta**; the only change is the
`scoring_excluded` label — `non_contributory` 303→270 and `diagnostic_probe` 365→364 (the 592f MECH-090
entry) all moved into `stale_substrate` 11→45 (+34).

| run (nested manifest) | form | claim(s) flagged |
|------------------------|------|------------------|
| `v3_exq_572_intervention_a_dual_attractor` (×4 runs) | run-level | ARC-065 |
| `v3_exq_573_arc065_bias_scale_sweep` | per-claim | ARC-065, MECH-313, MECH-314, MECH-320 |
| `v3_exq_603a_q045_mech313_mech260_four_arm_ablation` | per-claim | Q-045, MECH-313, MECH-260 |
| `v3_exq_603c_q045_mech313_mech260_phased_training` | per-claim | Q-045, MECH-313, MECH-260 |
| `v3_exq_604_q044_mech314_subflavour_three_arm_ablation` | per-claim | Q-044, MECH-314, MECH-314a/b/c |
| `v3_exq_605_q043_noise_floor_curiosity_weight_sweep` | per-claim | Q-043, ARC-065, MECH-313, MECH-314 |
| `v3_exq_606_arc064_gap_i_mech318_multi_rule_empirical_gate` | run-level | MECH-318 |
| `v3_exq_517b_mech302_relief_completion_discriminative_pair` | run-level | MECH-302 |
| `v3_exq_543i_arc062_differential_heads_falsifier` (035802Z) | per-claim | ARC-062, MECH-309, INV-074, MECH-334 |
| `v3_exq_543l_arc062_mode_separation_gap_b_falsifier` (023059Z) | per-claim | INV-074, MECH-334 *(only)* |
| `v3_exq_592f_mech090_commitment_state_transition_probe` | run-level | MECH-090 (diagnostic_probe→stale_substrate) |
| `v3_exq_598_gap1_sd033a_bias_head_trainable_ablation` | run-level | SD-033a |
| `v3_exq_616_q054_mech341_entropy_bias_scale_sweep` | per-claim | MECH-341 *(only)* |
| `v3_exq_625b_sd037_axis_b_phase1b_..._sustained_threat` | run-level | (claim_ids=[]; documentary — produces no index entries) |

**Deliberately NOT flagged (would not have been scoring-neutral, or no nested manifest):**

- **`v3_exq_577`** — flat-only; no `runs/<id>/manifest.json` exists, and the indexer reads **only** nested
  manifests, so it is not indexed at all (nothing to relabel; a flat-file flag is inert).
- **`v3_exq_603b`** (×2 runs) — currently reads `mixed` (all of Q-045/MECH-313/MECH-260 score). Flagging
  would *de-weight* live scoring entries — that is a substantive call (like the B.2 MARK process), not the
  scoring-neutral backfill, so it was left for a governance decision.
- **`v3_exq_610a`** — run-level `evidence_direction: superseded` already; `superseded` is a stronger
  exclusion that takes precedence over the stale-substrate gate, so a flag would be inert.
- **`v3_exq_622`** — `claim_ids: []` and already `superseded`; inert.
- On `543l` and `616` the scoring claims (`543l`: ARC-062 *weakens* / MECH-309 *supports*; `616`: Q-054
  *mixed*) were left untouched — only their `non_contributory` co-tags were flagged.
