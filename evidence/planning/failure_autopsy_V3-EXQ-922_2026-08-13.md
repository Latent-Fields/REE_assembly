# Failure Autopsy: V3-EXQ-922 (SD-016 production combo — MECH-150, MECH-151, MECH-152, ARC-041)

**Generated:** 2026-08-13T05:24:45Z
**Scope:** single (one run, four claim tags)
**Status:** confirmed
**Dry-run check:** clean

**Correction to task framing:** SD-016 is a `substrate_queue.json` design decision, not a `claims.yaml` claim. The four real claim tags on this manifest are MECH-150, MECH-151, MECH-152, ARC-041.

## 1. Facts

- **Run:** `v3_exq_922_sd016_mech151_152_arc041_production_combo_20260812T035119Z_v3`, queue_id V3-EXQ-922. `evidence_direction: weakens` (blanket); `evidence_direction_per_claim`: MECH-150 supports, MECH-151 supports, MECH-152 does_not_support, ARC-041 does_not_support. `interpretation.label`: `sd016_combo_dissociation_mech151_only`. Substrate stable across all 6 cells (single hash). Recording provenance clean.
- **Design:** 2 arms (A0_OFF legacy soft-selection control, A1_PRODUCTION = the GOV-FANOUT-1-recommended combo: `cue_slot_tagger=True`, `selection=gumbel`, `ctxdiv_weight=0.5`, `use_differentiable_cem=True`) × 3 seeds.

| Claim | Criterion | Type | Result |
|---|---|---|---|
| MECH-150 (gate) | C1 entropy<2.5, C1b ctxdiv>0.1, C2 negative-control entropy>2.65 | discrimination + neg-control | **PASS all, 3/3** |
| MECH-151 | `action_bias_div(A1) > action_bias_div(A0)`, paired per-seed | relative | **PASS 2/3** (seed 42 fails, 43/44 pass) |
| MECH-152 | C1 `r_w_harm>0.5`, C2 `r_w_goal<-0.3` | absolute (inherited from V3-EXQ-194a) | **FAIL 0/3 both** |
| ARC-041 | dissociation over MECH-151/MECH-152 | discrimination | `falsified_dissociation_mech151_only` — matches ARC-041's own pre-registered signature exactly |

**Interpretive lead (not yet flagged in the manifest's own note):** A0_OFF's `r_w_harm_mean`/`r_w_goal_mean` (0.356/-0.355) sit much closer to the 194a thresholds than A1_PRODUCTION's (0.001/-0.008) — A0_OFF's `r_w_goal` would even individually clear the `<-0.3` bar. Scoring is correctly restricted to A1_PRODUCTION per the acceptance-criteria design (194a replication must hold under the production combo), but this pattern points at a **selection-hardness interaction** (hard-Gumbel + ctxdiv-loss) rather than an outright absence of the MECH-152 mechanism.

**One documented scope narrowing:** `use_differentiable_cem=True` is armed but a documented no-op here — `compute_cue_action_loss` trains via direct MSE distillation against `E2.action_object()`, never calling `HippocampalModule.propose_trajectories()`. MECH-151's "supports" verdict does **not** validate SD-055's specific CEM-gradient-restoration mechanism.

## 2. Claim-layer mapping — per claim

**MECH-150** (ContextMemory, cue-indexed selective activation): `status: candidate`, `depends_on` ARC-001/SD-005 both implemented/stable. Prior evidence thin/stale (181/181b found the circuit existed but content undifferentiated; a long chain of retests blamed first training objective, then env-entropy, before GOV-FANOUT-1 907/908 fixed the actual gap). **Digestion note (2026-08-06) named this run's predecessor conditions as the "NEXT DIGESTION PASS" checklist — this run resolves them.**

**MECH-151** (cue-indexed context → action_bias, top-down gate on HippocampalModule search): `status: candidate`, `depends_on` MECH-150/SD-004/ARC-001/ARC-002 all implemented. **No prior evidence at all** — this is the first-ever experimental entry. Digestion note (2026-08-06) flagged "no blocker statement at all" and named two live threads: env-entropy (now resolved) and SD-055's dead-gradient defect (a separate, still-open gate).

**MECH-152** (cue-indexed context → terrain_weight, E3 harm/goal scoring): `status: provisional` (promoted 2026-04-03, conf=0.773). `evidence_quality_note`: EXQ-194 MIXED (harm pathway validated, goal pathway not). Held at provisional pending goal-pathway validation. This run replicates 194a's exact methodology through the real end-to-end retrieval path — a genuine, non-degenerate FAIL of both sub-criteria, materially worse than 194a's own MIXED finding, but see the A0_OFF interpretive lead above.

**ARC-041** (dual-pathway frontal cue-weighting circuit, MECH-150→MECH-151+MECH-152, completing ARC-035): `epistemic_category: substrate_conditional` (pre-existing, appropriately set — ARC-041's own `what_would_answer` conditioned confirmation on SD-016 leg A + SD-055 gates landing). `depends_on` all implemented except MECH-160 (correctly excluded from claim_ids, out of scope). ARC-041's own `what_would_answer` pre-registers **exactly** this run's signature: "only ONE of the two pathways shows content-tracking... falsifies the DUAL-pathway architecture specifically, even though it would leave the surviving single pathway's own mechanism claim intact."

**Peripherality assessment:** no claim in this run is a peripheral co-tag — all four were directly, centrally designed for. The one real nuance is MECH-151's SD-055-gradient-route scope narrowing (affects how "supports" should be worded, not whether it counts).

## 3. Biological-reference triage

| Claim | Reference | Lit status |
|---|---|---|
| MECH-150 | OFC/vmPFC pattern completion (Murray & Izquierdo 2007) | present (`targeted_review_connectome_mech_150`) |
| MECH-151 | vmPFC→striatum/premotor projections (Haber & Behrens 2014) | **thin — no dedicated targeted review** |
| MECH-152 | vmPFC lesion / Iowa Gambling Task deficit (Bechara 1994); gain-control (Kanashiro 2017) | present |
| ARC-041 | Dual OFC/vmPFC circuit architecture | present, well-grounded |

Documented fidelity gap: biological hippocampal pattern completion is auto-associative/Hopfield-like; REE's ContextMemory uses query-key attention. The Gumbel-softmax categorical selection (a formal ML import) grafted onto this biological target is a plausible interaction candidate for why MECH-152's graded correlational output (a CA3-completion-like job) may not coexist well with the WTA-like hardness MECH-150 needs from the same single mechanism.

## 4. Four-layer diagnosis (overall)

| Layer | Status | Note |
|---|---|---|
| Claim alignment | aligned | 1:1 mapping to each claim's own pre-registered granularity |
| Biological reference | clear for 3/4, thin for MECH-151 | |
| Prerequisites | present | All formal depends_on implemented; MECH-160 correctly excluded |
| Implementation completeness | complete | Readiness gates + MECH-150 gate all cleared cleanly |
| Environment adequacy | adequate | Long-standing env-entropy precondition resolved |
| Measurement adequacy | adequate | 194a-matched Pearson-r methodology; paired/majority gating |
| Integration adequacy | adequate for tested path; NOT adequate as an SD-055 gradient test | `propose_trajectories()` never invoked |
| Scale/capacity | adequate | world_dim=128 matches validated operating point |

**Failure-location (GOV-FAILLOC-1), for MECH-152/ARC-041 specifically:** REE FAILED — implementation, measurement, environment all independently established as adequate. MECH-150/MECH-151 are confirmations, not failures — the bucket doesn't apply to them.

## 5. Re-derive brake & granularity-debt checks

Zero prior confirmed `substrate_ceiling` hits for any of the four claims; zero prior autopsy targets at all for MECH-151/MECH-152 (this is the first). Neither check fires. This run establishes, rather than continues, a recurrence pattern.

## 6. Recommended epistemic_category

`standard` for all four — none is peripheral, none warrants a substrate-gate assertion for this result. (ARC-041's pre-existing `substrate_conditional` is a separate question — see §7, HELD this cycle.)

## 7. Routing — CONFIRMED (per-claim, split)

At the Step 8 gate (2026-08-13) the user was offered "Accept the split routing" (recommended: claim-synthesis for MECH-150/ARC-041, queue-experiment for MECH-151/MECH-152, substrate_queue amend) but **chose "Hold ARC-041's falsification" instead.**

- **MECH-150 → `claim-synthesis`.** Confirmed this cycle; refresh the stale `evidence_quality_note` (still describes the 2026-03/04 training-objective gap) and retire the 2026-08-06 digestion_note.
- **MECH-151 → `claim-synthesis`** (first evidence_quality_note entry) **+ `queue-experiment`** as a distinct follow-on: a driver that actually invokes `HippocampalModule.propose_trajectories()` with a live (non-detached) `action_bias`, to test SD-055's gradient-restoration mechanism specifically — not touched by this run.
- **MECH-152 → `queue-experiment`.** A targeted soft-selection + ctxdiv=0.5 ablation (isolating whether the collapse is selection-hardness-specific) rather than a re-run of the full 6-cell combo. `substrate_queue.json` SD-016 amendment: add a `failure_record` entry, `severity: informational`, no new substrate code needed (driver-only new arm).
- **ARC-041 → HELD.** The user explicitly declined to finalize the dual-pathway falsification write-up this cycle. Per its own pre-registered signature the dissociation IS met (MECH-151 survives, MECH-152 fails), but since that reading rests on MECH-152's own not-yet-fully-resolved result (the A0_OFF interpretive lead above), disposition stays open. `epistemic_category` left **unchanged** at `substrate_conditional` (not downgraded to `standard`). Re-examine once the MECH-152 soft-selection ablation resolves.

Draft `evidence_quality_note`s (per claim): see JSON companion `failure_autopsy_V3-EXQ-922_2026-08-13.json`, `per_claim_recommendation`.

## 8. Learning extracted

- MECH-150 is now cleanly confirmed after a long chain of prior FAILs sequentially misattributed to a missing training objective, then env-entropy — both now confirmed satisfied on this apparatus.
- ARC-041's own pre-registered dissociation signature was met, but the user's decision to hold rather than finalize illustrates a real judgment call: a clean per-criterion pass/fail pattern doesn't always mean the higher-level architectural verdict should be finalized in the same cycle, when one of the two legs carries its own unresolved interpretive lead.
- MECH-151's "supports" verdict is explicitly narrower than it might first appear — it does not touch SD-055's CEM-gradient-restoration mechanism.

## 9. Governance apply checklist

- [ ] Append MECH-150 evidence_quality_note; retire its digestion_note
- [ ] Append MECH-151 evidence_quality_note (first entry); leave status candidate
- [ ] Append MECH-152 evidence_quality_note; leave status provisional
- [ ] **Do NOT change ARC-041's disposition or epistemic_category this cycle** — held pending the MECH-152 ablation
- [ ] Amend `substrate_queue.json` SD-016 entry with the MECH-152 failure_record
- [ ] Queue the MECH-151 SD-055-gradient driver and the MECH-152 soft-selection ablation (both via `/queue-experiment`)
