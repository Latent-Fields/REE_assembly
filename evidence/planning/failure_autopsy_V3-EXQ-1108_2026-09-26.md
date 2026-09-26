# Failure autopsy: V3-EXQ-1108 (N2 replay policy under a training encoder, full dose, pinned)

- **Status: CONFIRMED** (interactive Step 8 gate, 2026-09-26T11:00:42Z). Session `fa-exq1108-20260926`.
- **Run:** `v3_exq_1108_n2_replay_encoder_full_dose_pinned_20260926T100252Z_v3`, ree-cloud-2, 28,322 s. `ree_core` pinned to `9b322d5` (verified), `claim_ids: []`, `experiment_purpose: diagnostic`, manifest outcome FAIL, `n2_verdict: NEITHER`.
- **Pre-registration:** `n2_replay_encoder_probe_20260925.md` secs 1-2 (`025fc6a5cfe`) + amendment A1 sec 4 (`fc5c0795221`: post 1200, seeds 811-815, fleet, red-team F1-F3 dispositions).
- **Bears on:** `coupled_loop_repair_campaign_plan:N2`, `:W6a`, `:P8`.

## 1. Facts

**Dry-run gate.** `check_dry_run_citations.py V3-EXQ-1108 --family v3_exq_1108`: 0 dry, 1 real. The dry-run-unreachable-criterion lint does not flag the driver. `validate_recording.py`: complete (always-core present, `substrate_hash` scoped to the pinned tree).

**Design (as registered).** There are three arms on one sha: `frozen` (W6a OFF, W3 re-encode; the control), `reencode` (W6a ON, W3 re-encodes raw obs through the current path) and `stored` (W6a ON, W3 replays the z sensed at record time). Each arm has a label-permuted `shuf` twin. Legs: (a) disc4_h1 >= 0.47 **and** k == 10; (b) retention >= 0.5; (c) twin fails (a); (d) guard PASS; (e) late-growth max < 1.2 and t30/t0 median < 5. Keep the bar = (a) 4/5, (b) 4/5, (c) twin <= 1/5, (d) 5/5, (e) 4/5. Rule: CANNOT_DETERMINE if the control misses (a) on 2 or more seeds, then HOLDS-*, else NEITHER.

**Result.** All 30 cells and 5 B0s completed; non-degenerate.

| arm | post disc4 median | paired disc4 minus frozen (mean, sd) | (a) registered | (a) disc4-only | (b) | twin (a) | (d) | (e) | twin shares (e) fail |
|---|---|---|---|---|---|---|---|---|---|
| frozen | 0.510 | - | 4/5 (815 misses, 0.440) | 4/5 | 5/5 | 0/5 | 5/5 | 5/5 | - |
| reencode | 0.517 | -0.005 (0.050) | **3/5** (812 k=9 at disc4 0.563; 815 0.447) | 4/5 | 5/5 | 0/5 | 5/5 | **1/5** | 4/4 |
| stored | ~0.28 | **-0.231** (0.052) | 0/5 (k 0 on 5/5) | 0/5 | 0/5 | 0/5 | 5/5 | 0/5 | 5/5 |

Per-seed paired (reencode - frozen): -0.083, +0.053, -0.013, +0.013, +0.007. (stored - frozen): -0.297, -0.213, -0.263, -0.223, -0.160. In the W6a arms the test-set norm rises x10.5-12.0; PR rises from ~1.5 to 7.85-9.81 in reencode and to 6.63-11.17 in stored. Retained stored-z relative staleness is 0.95-0.97 and on-policy staleness 0.30-0.64. The (e) numbers: frozen late-growth max <= 1.021; reencode 1.10-1.46, t30 1.29-8.84; stored 1.74-2.39, t30 median 4.8 to ~3.5e5.

**Verdict as computed: NEITHER**, correctly computed. Rule 1 does not fire (control 4/5).

**Precondition flag.** `pre_phase_identical_across_arms` is `met: false` (max 1/300). The mismatches are in 4 stored-arm cells only (812/815 real, 811/814 shuf); frozen and reencode have identical pre values on every seed. Mechanism: in its pre phase the stored arm replays the live-sensed z while the others replay a 26-tick re-encode. The two differ by EMA-window truncation even with a frozen encoder (frozen `stale_on_policy` reaches 6.6e-5). So the "byte-identical" premise was false by construction for the stored arm. It does not affect the verdict.

## 2. Claim layer

None. This is a campaign design probe that gates the W6 preset buffer policy (plan P8). Category `standard`, direction `non_contributory`, no `per_claim_recommendation`.

## 3. Biological reference

Hippocampal replay regenerates episodes through the *current* cortical code; it is not a playback of stored activations. A replay buffer of detached latents that goes stale as the encoder learns has no biological analogue. Raw-obs re-encode is the closer translation, and the stored-arm collapse is what the reference predicts.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free |
| Biological reference | partial | replay is regenerative; stale-latent replay has no analogue |
| Prerequisites | present | W3 + W6a on branch `9b322d5`; pin verified |
| Implementation | complete | the stored arm is a deliberate configuration, not a defect |
| Environment | adequate | W3 member-gate protocol, CausalGridWorldV2 size 12 |
| Measurement | under-instrumented (reencode question); adequate (stored) | see below |
| Integration | partially coupled | re-encode tracks the moved encoder on disc4; the W6a-space rollout fails the literal (e) bound |
| Scale | adequate | full W3 dose; 1200 W6a updates |

Measurement, in detail:
1. As registered, (a) carries the `k == 10` conjunct. `w3_k_excluding_reset_ticks_20260926.md` showed on 6/6 seeds that this conjunct is carried by near-reset ticks, and it was **provisionally** dropped from the W3 gate at 09:33Z. That decision is unratified, and the branch record re-scores no past result.
2. The (a) count threshold is 4/5, and the control's base rate is ~0.60 (W3 sweep 9/15, same recipe). An arm identical to the control therefore keeps the bar with P = 0.337, and rule 1 was about 66% likely to fire a priori. The sweep landed after A1 was pre-registered, so this was not knowable at design time.
3. Leg (e) is a max over 40 starts drawn with near-reset ticks included, on a pin that predates the reset-init build. That is the same EMA zero-init artefact the 09:33Z decision (1) found carried 84% of the ASP literal growth-bound failure.

**Failure location (GOV-FAILLOC-1).** For the reencode arm, MIXED (MECHANISM + MEASURES), not chargeable to REE. For the stored arm, a genuine negative for the stored-z policy (measures established).

## 5. Reading, as confirmed at the gate

- **Stored-z replay is ruled out** while the encoder trains through the read path (D1, 5/5, large margin, S1/S2 agree).
- **Re-encode, as registered, fails (a) 3/5 and (e) 1/5**, with `keeps_bar_excluding_e_secondary` false. So the pre-stated F1 reading ("fails ONLY (e), twin shares it = rollout-stability finding") **does not fire as registered.**
- **Conditional on ratification of the disc4-only (a):** re-encode's 812 miss is k-only (disc4 0.563) and its 815 miss is shared with the control. That leaves (e) as the only failed leg, with the twin sharing 4/4, which is exactly the F1 reading about the W6a-trained encoder. On disc4, re-encode is at parity with the control (paired mean -0.005).
- **(e) attribution, narrowed (red-team F2):** in the reencode arm, whose only difference from frozen is W6a ON, the (e) miss is attributable to the encoder space. In the stored arm, (e) magnitude tracks the replay policy. It is not yet separated whether reencode's (e) miss is genuine instability or the reset-transient growth artefact.

## 6. Routing (confirmed: hand to the campaign orchestrator)

Owner: `orchestrate-20260924-breakthrough-c2`, via the plan's N2 / W6 rows. /governance chips after ratification; this session spawns nothing.

1. The W6 preset buffer policy is **raw-obs re-encode**. Stored-z is ruled out.
2. `HarmEvalMember`, `CodecMember` and `E1Member` store detached z. Each needs a raw-obs re-encode build (as W3 has) or a phased schedule that freezes the encoder while it trains. `complicated (buildable)`.
3. Re-read leg (e) relative to env truth with the reset-init knobs ON (09:33Z decisions (1) and (4)) before crediting it as a W6a rollout defect. `complex (probe-gated) / puzzle (known rules)`.
4. For any N2 re-run, gate arms on the paired per-seed disc4 difference against the control, not on a 4/5 count at a ~0.6 base rate.
5. Revisit the leg-(a) reading when the provisional disc4-only contract is ratified or reverted.

No `substrate_queue.json` entry is needed; this is campaign branch work. The re-derive brake does not apply (no claim ids).

## 7. Mechanical checks and red-team

- **7b** `autopsy_pre_routing_checks.py`: 0 fires. C1/C2/C3 are inapplicable on a claim-free target and C5 had no .md, so the quiet report reflects structural blindness, not clearance.
- **7c** red-team on **fable** (cross-model; this session runs on Opus): **CONTESTED**, arithmetic reproduced exactly. F1 (F1 rule invoked where its precondition fails), F2 ((e) attribution overbroad) and F3 (routing bypassed the orchestrator; (e) confound not tied to the existing decision) were all verified against source and applied above. Hygiene fixes applied: 4 mismatched pre cells, not 1; per-arm PR ranges.

## 8. Draft evidence_quality_note

> V3-EXQ-1108 (N2, claim-free, D1): pre-registered verdict NEITHER stands as computed. Stored-z replay loses the L2R bar under a training encoder on 5/5 seeds (post disc4 -0.231 vs the frozen control, paired sd 0.052; k 0; (b) and (e) fail; retained z 0.95-0.97 stale). Re-encode matches the control on disc4 (paired mean -0.005, sd 0.050), retention 5/5, twins 0/5, but as registered fails (a) 3/5 and (e) 1/5, so the pre-stated F1 reading does not fire. Conditional on ratification of the provisional 09:33Z disc4-only (a), (e) is its only failed leg (twin shares 4/4), which is the F1 rollout-stability reading about the W6a-trained encoder. Leg (e) is not yet separated from the reset-transient growth artefact (the pin predates reset-init).

## 9. Hypothesis-space ledger

Step 9b skipped. There is no fan-out, and no registered ledger question covers N2; its pre-registration lives in the N2 record. This is a claim-free campaign probe (precedent: V3-EXQ-1099 / 1104 autopsies, 2026-09-26).
