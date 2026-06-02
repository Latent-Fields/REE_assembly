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

**Still open (not applied):** confirm `483c` superseded by `483e`; optional backfill of the B.3
"asserts-but-missing" autopsy manifests (scoring-neutral); SD-012 fan-out + KEEP rows untouched.
