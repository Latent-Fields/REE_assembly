# Failure Autopsy: Round-5 batch2+3 mixed findings, 28 targets

**Generated:** 2026-08-08T19:37:15Z
**Scope:** cluster (round-5 grandfathered-backlog sweep, batches 2+3 non-legacy findings)
**Status:** confirmed (Step 8: MECH-266/SD-032a escalated to `/implement-substrate`; INV-045/INV-049 corrected to `non_contributory`)

## Q-007's predecessor trajectory (3 targets) — extends round 4's existing brake, doesn't reopen it

`20260315T150155_valence_regime_correlation_v2` (V2), `v3_exq_051` (V3), `v3_exq_051c` (canonical original — round 4 diagnosed only its later duplicate) all show "no rv→z_beta pathway," extending backward the 4-attempt trajectory (V2→051→051c→200) round 4 already stamped `substrate_ceiling` at EXQ-200. Attached as supporting predecessor evidence, not a new stamping.

## ARC-038's remaining lineage (3 targets) — folds into round 4's 267 disposition

`191` gets its own read: 1/3 criteria, but both failing criteria hit the eval-budget ceiling exactly at 200/200 — the schema-primed agent never converged within budget rather than genuinely failing. `355`/`355a` share the identical bit-identical-conditions signature round 4's 267 target already explained via the MECH-261 write-gating-propagation fix (landed 2026-04-22) — folded in, no new diagnosis.

## MECH-057a (139/203) — first-ever stamping for this claim

Two design iterations (manual `running_variance` proxy, then a BreathOscillator variant) both produce bit-identical GATE_ON/GATE_ABLATED harm rates. Both explicitly gesture at the same missing substrate (ARC-023 + SD-006). First `substrate_ceiling`-adjacent stamping for MECH-057a — routed `/implement-substrate` rather than a third proxy letter.

## MECH-266/SD-032a (464d/467d) — 6th consecutive non-engagement, escalated

Step 8 confirmed (recommended option): route to `/implement-substrate` for the mode-governance-engagement substrate itself, refuse another behavioural letter. The `use_external_task_drive=True` fix still fails its own non-vacuity gate on both parallel lineages (464, 467) — 4 prior stampings plus this round's 2 makes 6 consecutive reads of the same un-engaged mechanism.

## MECH-070 (132/212) — clean two-test falsification

Two independently-designed tests converge on a real negative: `132` shows E2 learns a real forward model (r²=0.996) yet produces zero downstream harm-eval effect (bit-identical arms); `212`, a redesigned horizon-sweep, shows the claimed longer-horizon advantage actually *reverses* (E2's fit degrades ~163× faster than E1's as horizon grows). Two methodologically distinct tests agreeing is strong grounds for `standard`/`does_not_support`, not a substrate gap. No prior stampings for MECH-070 anywhere — brake not applicable.

## MECH-153/ARC-042 (187a/211) — converged under-powered-supervision finding

Two independent attempts (different warmup lengths/lambda configs) both show near-zero context differentiation from supervised terrain_loss, and where `211` does achieve marginal differentiation, it produces *zero* downstream behavioral effect (bit-identical `e3_harm_eval_diff` across all seeds). Not yet `substrate_ceiling`-labeled; flagged for governance to watch for a third attempt repeating the pattern.

## INV-045 (243) and INV-049 (385) — measurement-defect corrections (Step 8 confirmed)

Both show a bit-identical-across-manipulated-conditions signature (243: `harm_discrimination` identical across every sleep-phase-order variant; 385: `eval_harm_rate` identical between WITH/WITHOUT offline consolidation in every seed, plus a suspiciously-exact `late_pred_loss=0.0` in both arms) — the tests as instrumented could not have discriminated the claim either way. Corrected from `weakens`/`does_not_support` to `non_contributory` per Step 8's recommended option. 385 additionally surfaces a directionality concern: its criterion may expect *more* diversity from offline consolidation when the biologically sensible prediction is *less* (consolidation/pruning).

## Formalization-only backfill (remaining targets)

SD-017/ARC-045/MECH-166 pair (242/436, already `non_contributory`, 436's successor already queued), MECH-118/119/Q-022 (084d canonical — a genuine dissociation result, C2/C4 support MECH-119, C1/C3 weaken MECH-118), MECH-097 (137, clean negative matching its own pre-registered `retire_ree_claim` decision), MECH-022 (190, environment misconfigured — zero hazard contacts), MECH-153 (239, possibly substrate-confounded by context_memory infra immaturity), MECH-216 (332, weak-but-real sub-threshold signal), SD-029/MECH-256 (433, aligns with an already-12-hit-fired brake), SD-033a (598b, already governance-closed), MECH-439 (689c — a formal target *stub* pointing to a prose-only diagnosis buried in a differently-named artifact's reconciliation block, closing a structural grep-visibility gap), MECH-094 (140, mechanism absent, correctly self-overridden), Q-012 (193, substantively positive, load-bearing for `retain_ree`).

## Biological-reference triage

All claims touched have present literature grounding.

## Re-derive brake state

**Fired and reaffirmed** (no new escalation beyond what's already routed): Q-007 (4 attempts, routed `/implement-substrate`), SD-029/MECH-256 (12 hits). **Fired and freshly escalated this round**: MECH-266/SD-032a (6 consecutive, routed `/implement-substrate` per Step 8). **First stamping this round**: MECH-057a (139/203).

## Recommended routing summary

Most targets: `governance-note-only`. Two escalations to `/implement-substrate`: MECH-057a (create — ARC-023 + SD-006 substrate) and MECH-266/SD-032a (create — mode-governance-engagement substrate).

## Learning extracted

1. Round-5's disciplined coverage-verification pass repeatedly found that a run's "canonical original" is not always the version a prior round diagnosed — round 4's Q-007/EXQ-051c target was actually the later duplicate, leaving the true canonical original undiagnosed until this round traced the `supersedes`/`superseded_by` chain.
2. Two independently-designed tests agreeing on a negative (MECH-070's 132/212) is qualitatively stronger evidence than either alone — worth treating as a distinct evidentiary tier from a single clean FAIL.
3. A criterion's directionality assumption (INV-049's "more diversity is better") can itself be biologically backwards — worth checking the biology's predicted direction before treating a bit-identical/zero-effect result as either evidence or noise.
