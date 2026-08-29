# Diagnostic-PASS adjudication: V3-EXQ-957 (MECH-219 controllability-dissociation substrate readiness) — 2026-08-29

**Run:** `v3_exq_957_mech219_controllability_dissociation_substrate_readiness_20260829T113551Z_v3` · PASS · diagnostic · claim_ids [] · seeds [11,23,37,41,59] · ree-cloud-2 · self-route `mech219_controllability_dissociation_confirmed` · non_degenerate true · elapsed 3.06 s
**Status:** confirmed (interactive gate 2026-08-29; session autopsy-batch-20260829)
**Dry-run check:** clean (full run; 5 seeds × 2 conditions × 180 live sense() ticks).

## Facts

The substrate-readiness probe the MECH-219 design memo Section 7 prescribes (claim_ids=[] first; behavioural evidence run later — V3-EXQ-518/SD-019a precedent), delivered ~2.5 months after the build left it owed. Pure-arithmetic regulator (`HarmSufferingAccumulator`, no nn.Module) probed on an untrained agent under matched nociception (fixed position 1 cell from a single hazard, stay-action; ESCAPABLE esc=1.0 throughout vs INESCAPABLE esc=0.0→1.0 at relief). **The 3.06 s runtime is proportionate** (no training; ~1,855 no_grad sense ticks), not evidence of skipped computation.

All four load-bearing criteria pass conjunctively per-seed with pre-registered thresholds (never fitted to this run), at large margins: C1 controllability gaps 0.523–0.694 vs 0.10 (escapable suffering exactly 0.0 by construction, its non-vacuity carried by C3's un_floor: escapable z_harm_un 0.54–0.70 ≥ 0.10); C2 retention@5 = 0.95099005 (matches (1−0.01)^5 to ~1e-10 in all seeds), half-life 69.0 = the exact discrete-EMA prediction ceil(ln 0.5/ln 0.99); C4 SD-021 parity — attenuation genuinely fired 5/5 (z_harm ≈ halved) with the escapability scalar bit-identical 0.0→0.0. `degenerate_metrics` empty; the deliberately-constant escapable series is correctly excluded from the scan. Recording complete; substrate clean (ed7bd75).

## Adjudication

**GENUINE PASS, scoped to the ACCUMULATION side.** The escapable-arm zero is analytic (g_t = 1−esc), but the probe's information is that the construction is wired into the live sense() path — the external escapability lever demonstrably reaches the accumulator, and the enumerable mis-wirings (escapability not plumbed; drive using u_t alone; SD-021 leaking into the gate) would each have failed a criterion. C2 verifies the-code-is-the-documented-code (real but deliberately weak — seed-independent arithmetic).

**Scope limit (red-team finding, adopted):** in this configuration the accumulator's **output is a dead-end register** — the driver reads s_t from `get_state()`, never from the latent, and every `harm_suffering_redirect_*` consumer flag is OFF; the agent.py vector-build line could be deleted and all four criteria would still pass. "Substrate readiness confirmed" = accumulation-side readiness only; the output/consumer path is unverified by this run.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | n/a | claim-free by triple documented intent (memo §7, driver "double-safe", queue note); the MECH-219/MECH-305 scope split independently forbids reading a controllability-only demo as MECH-219 evidence |
| Biological reference | clear | controllability gating of suffering (Salomons 2004; Loffler 2018); faithful coarse translation |
| Prerequisites | present | SD-019a/b built; SD-058 avoided via external mode |
| Implementation | complete | for the probed (accumulation-side) scope |
| Environment | adequate | matched-nociception wiring probe |
| Measurement | adequate | pre-registered thresholds, conjunctive per-seed, degeneracy scan + C4 fired-control |
| Integration | **partially coupled** | untrained encoder; external mode only; output/consumer path unverified (dead-end register) |
| Scale | adequate | for purpose |

**Failure-location: n/a** — no failure; PASS adjudicated genuine at its stated scope.

## Disposition (user-confirmed)

- Self-route label accurate at its (carefully self-delimited) scope; direction non_contributory; category `standard`. MECH-219 stays candidate with zero scoring experimental entries — correct, by design.
- **Routing: queue-experiment** — the behavioural MECH-219/SD-019b evidence run: claim_ids=['MECH-219'], trained substrate, C3(b) anti-correlation with MECH-353 z_block_assert, full z_harm_s attenuation-magnitude C4, escapability from avoidance_efficacy once SD-058 clears (external mode fallback). Per the red-team pass it MUST additionally (1) **enable the `harm_suffering_redirect_*` consumer flags** (MECH-219's own what_would_answer requires it; 957 leaves that path unverified) and (2) test the memo-§7 **C2 contrast half** (z_harm_un releases FAST after offset while s_t releases slowly — the input/accumulator temporal dissociation, not just the accumulator's own decay constant). Inherited caveat: on an untrained/lightly-trained encoder, relocation-based relief operationalisations are confounded (driver's rejected-design record: z_harm_un rose 0.55→1.45 after relocation). No existing queue entry or chip covers the follow-on (checked). Not spawned by this session (2026-07-30 rule).
- Substrate queue: no action (SD-019a/b entries stand as-is; governance's standard sweep).

**Re-derive brake / granularity trigger: do not fire** (0 prior targets tag MECH-219). Step 9b: no ledger action (no fan-out; no registered controllability qid exists — the follow-on evidence run can open one if governance wishes).

**7b:** 0 fires (claim-keyed checks inapplicable). **7c:** CONFIRMED on adjudication; routing note CONTESTED and adopted (dead-end-register scope limit + two follow-on requirements + "matched theory" wording tempered to the exact discrete prediction).

## Learning extracted

1. The readiness-first, claim_ids=[] discipline worked as designed — an adjudicable wiring verdict with zero contamination of MECH-219's evidence record.
2. An analytically-forced zero can carry real information when the criterion set includes input non-vacuity (C3) and live-path plumbing checks — but a wiring probe verifies only the paths it reads: state what is a dead-end register in the probed configuration, or "readiness" over-claims.
3. The rejected-design record (relocation relief confounded on untrained encoders) is a caveat every successor inherits.
