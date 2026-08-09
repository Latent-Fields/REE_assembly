# Failure Autopsy — V3-EXQ-244b (MECH-165 replay diversity validation, diagnostic-purpose PASS)

**Generated:** 2026-08-09T05:43:28Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-09 — low controversy; direction confirmed as filed with an added scope-limitation flag)

## 0. Trigger

Diagnostic-purpose PASS (`experiment_purpose: "diagnostic"`) — per skill trigger #2, requires the full four-layer autopsy regardless of outcome or adjudication flag ("a diagnostic that cleared its own preconditions still needs the four-layer diagnosis before its reading can be trusted, since 'cleared its own preconditions' is exactly what a vacuous or confounded pass would also show").

## 1. Facts

### The predecessor (V3-EXQ-244a) and why 244b exists
244a's `evidence_quality_note` already self-labeled it degenerate: "only 1/5 seeds shows a genuine BALANCED_REPLAY advantage; 3/5 seeds win by ~1e-13 (floating-point noise). Critically, FORWARD_REPLAY == NO_REPLAY byte-for-byte in all seeds." No dedicated `failure_autopsy_*` artifact exists for 244a (diagnosed informally, superseded directly) — a process gap this skill's trigger #2 exists to close; not backfilled here.

Root cause (confirmed via manifest comparison): 244a's driver called `agent.reset()` as a final-flush after Phase 1, wiping `theta_buffer` before its hand-rolled SWS loop read it — silently skipping replay in every condition. Confirmed directly: 244a's `NO_REPLAY` and `FORWARD_REPLAY` `condition_stats` are identical to 17 significant figures; `sws_metrics.reverse_replayed: 0` on every row.

### The 244b corrected driver
Drops the final-flush reset; routes replay through the production path (`agent.clock.advance()` -> `agent._do_replay(...)` on real `e3_quiescent` ticks, exactly as `agent.act()` calls it internally); asserts non-degeneracy in-run via 4 preconditions; doubles consolidation volume.

Pre-registered PASS criterion (verbatim, matching claims.yaml's own `what_would_answer`): `mean(retention_BALANCED) > mean(retention_FORWARD)` AND `BALANCED > FORWARD` in >=3/5 seeds — **a comparison against FORWARD_REPLAY only, not against NO_REPLAY.**

### The result, read precisely
```
NO_REPLAY:       mean 0.683978, std 0.127555
FORWARD_REPLAY:  mean 0.677222, std 0.127903
BALANCED_REPLAY: mean 0.685483, std 0.127502
```
BALANCED - FORWARD = +0.00826 (satisfies the criterion). BALANCED - NO_REPLAY = +0.00151 (essentially zero, ~4x smaller). FORWARD - NO_REPLAY = -0.00676 (forward-only replay is *worse* than no replay).

Per-seed BALANCED vs FORWARD: 4/5 seeds favor BALANCED, margins mostly 0.002-0.012 except seed 42 (+0.038); the one dissenting seed (1024, -0.017) reverses by a magnitude comparable to three of the four "wins." Pooled std (~0.128) is ~15x the mean gap (0.0083) — Cohen's-d-equivalent ~0.065, a very small effect.

All 4 non-degeneracy preconditions genuinely met (reverse replay fires 9-23x, FORWARD diverges from NO_REPLAY by up to 0.046 — 10 orders of magnitude above 244a's 1e-13, exploration buffer populated, production path exercised). These establish the harness now genuinely exercises the mechanism; they say nothing about effect-size adequacy.

Dry-run check: not a smoke (elapsed_seconds 9105s consistent with a full run).

## 2. Claim-layer mapping

MECH-165 (`candidate`, `substrate_conditional`, `depends_on: [MECH-120, MECH-121, MECH-092, ARC-007]`). Pre-registered CONFIRMING (verbatim): "balanced replay produces significantly higher post-consolidation entropy retention than forward-only replay, in a design where (a) reverse replay confirmed fired, (b) exploration buffer populated by genuine alternative-strategy material, (c) effect reproduces across >=3/5 seeds with an effect size that exceeds floating-point noise (EXQ-244a's own 1/5-real/3/5-at-1e-13 is the explicit negative example to exceed)."

244b clears CONFIRMING on the letter — direction positive, reproduces 4/5 seeds, clears the "exceeds floating-point noise" bar by many orders of magnitude. But "exceeds floating-point noise" was written specifically to rule out a repeat of 244a's exact bug, not to certify statistical significance, and the claim's own CONFIRMING text says "significantly higher," a stronger claim than what was measured.

## 3. Biological-reference triage

Strong, specific literature: Foster & Wilson 2006 (Nature, reverse replay at reward, dopamine-coupled — existence proof for past-path replay as a real process); Shin, Tang & Jadhav 2019 (Neuron) — the most direct grounding, reverse replay dominates early learning and encodes retrospective evaluation including error paths, forward replay dominates late learning; its own translation note states "a system with only forward replay from the dominant strategy would consolidate that strategy preferentially, reproducing the monostrategy problem" — essentially MECH-165 in the primary literature's own terms. Huelin Gorriz 2023 (Nat Commun): direct empirical demonstration of the failure mode MECH-165 guards against (sleep replay is biased toward heavily-encoded traces without a bounding mechanism). Not a formal import.

**Divergence worth naming**: Shin 2019 shows reverse and forward replay are not symmetric alternatives at a single point in learning — reverse dominates early, forward dominates late, tracking the exploration->consolidation transition. 244b's `BALANCED_REPLAY` uses a single fixed 50/30/20 forward/reverse/random split for the entire consolidation window (a fixed mixture, not a scheduled one). A legitimate first-pass simplification, but a genuinely faithful implementation would plausibly show a larger effect than measured here, since biology front-loads reverse replay when non-dominant paths are still viable rather than diluting it uniformly.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact, weakly strengthened | tested for the first time under conditions where the claim could express itself |
| Biological reference | clear | Shin 2019, Foster & Wilson 2006, Huelin Gorriz 2023 |
| Dependency prerequisites | present, not independently re-verified this run | MECH-120/MECH-092 used as scaffolding |
| Implementation completeness | complete (was: stub that never fired in 244a) | 244a's achievement — production call path now demonstrably fires end-to-end |
| Environment adequacy | too sparse to differentiate at this effect size | between-seed SD (~0.128) is an order of magnitude larger than the manipulation's mean effect (0.0083) |
| Measurement adequacy | under-powered; one unaddressed confound | possible RNG-stream perturbation: `diverse_replay`'s mode selection and content sampling appear to draw from the single shared global torch RNG stream; BALANCED consumes a different, variable number of extra draws than FORWARD/NO_REPLAY before Phase 2's action sampling — not confirmed to be inert to Phase-2 sampling |
| Integration adequacy | coupled and functioning | production call path demonstrably exercised end-to-end |
| Scale/capacity | adequate for a diagnostic, insufficient for a confirmatory claim | 5 seeds, no formal significance test computed anywhere in the driver |

## 5. Vacuous-pass-adjacent analysis

Two claims must be kept separate: (A) "the harness now exercises the mechanism" — established, genuinely non-degenerate, not a repeat of 244a's artifact. (B) "balanced replay produces a behaviorally meaningful benefit over forward-only replay" (the claim's actual "significantly higher" language) — weakly supported at best: binomial P(>=4/5 wins | no true effect) ~ 0.19, not significant at conventional thresholds; BALANCED does not clearly outperform NO_REPLAY (+0.0015 mean, wins only 2/5 seeds — FORWARD_REPLAY is itself worse than NO_REPLAY on average). The demonstrated effect is specifically "balanced replay recovers most of the deficit forward-only replay introduces relative to doing nothing," not a general "replay improves retention" finding. **Verdict: not vacuous in the 244a sense (real, non-degenerate harness), but statistically weak and narrowly scoped.** The manifest's interpretation label overstates it.

## 6. Learning extracted

1. 244a's driver bug (final-flush reset before the hand-rolled SWS loop) confirmed fixed by direct data comparison.
2. The 4 non-degeneracy preconditions certify the harness exercises the mechanism, not that the resulting effect is large or statistically robust — separate bars the manifest's single interpretation label conflates.
3. The claim's pre-registered CONFIRMING criterion is BALANCED-vs-FORWARD only; the practically meaningful comparison (does any replay help vs none) is not established here.
4. Possible uncontrolled RNG-stream confound between replay-selection sampling and policy-action sampling, not ruled out.
5. V3-EXQ-244a reached a self-labeled degenerate PASS and was superseded without ever passing through `/failure-autopsy` — a clean illustration of trigger #2's purpose.

## 7. Routing (confirmed)

`recommended_evidence_direction: supports` (confirmed as filed). `recommended_epistemic_category: standard`, with `narrow_supports_flag: true` to make the scope limitation visible to governance and future citers without demoting the category. Routing: `/queue-experiment`, optional strengthening (more seeds, formal significance test, RNG-stream isolation between replay-selection and policy-action sampling) — **not required** to validate the current PASS. `recommended_substrate_queue_entry.action: none` — no substrate gap, this is a statistical-power/measurement-design question.

**Process note for governance**, out of this autopsy's own scope: 244a should be retroactively logged as a should-have-been-autopsied diagnostic PASS/FAIL, illustrating why trigger #2 exists.

**Step 9b**: no existing hypothesis-space qid names MECH-165; no `fanout_recommendation` emitted. Registration deferred.

## 8. Evidence quality note (for governance to apply)

> Non-degenerate PASS -- corrects 244a's silent no-op bug (theta_buffer wiped before consolidation; FORWARD byte-identical to NO_REPLAY). All 4 harness-integrity preconditions genuinely met: reverse replay fires (9-23/seed), FORWARD now measurably diverges from NO_REPLAY (up to 0.046, vs 244a's 1e-13), production call path exercised. However, the confirmed effect is small and only weakly seed-robust: BALANCED beats FORWARD by a mean of +0.0083 against a between-seed SD of 0.128 (Cohen's-d ~0.065), in 4/5 seeds with 3 of those 4 margins under 0.012 and the dissenting seed reversing by a comparable magnitude (binomial P(>=4/5 wins | H0 no effect) ~0.19, not significant at conventional thresholds; no formal significance test is computed in the driver). BALANCED does not clearly outperform NO_REPLAY (+0.0015 mean, wins only 2/5 seeds) -- the demonstrated effect is specifically "balanced replay recovers most of the deficit forward-only replay introduces relative to doing nothing," matching the claim's own BALANCED-vs-FORWARD operationalization, not a general "replay improves retention" finding. Treat as real, directionally-correct, biologically-grounded support at modest statistical strength -- not yet the "significantly higher" result the claim's CONFIRMING text describes. A confirmatory follow-up with more seeds, a formal significance test, and RNG-stream isolation between replay-selection sampling and policy-action sampling would strengthen this considerably.
