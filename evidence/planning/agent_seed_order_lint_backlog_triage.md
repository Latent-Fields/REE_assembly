# Agent-seed-order lint backlog: materiality triage of all 18 flagged scripts

**Status: all 18 triaged, all 18 immaterial to their reported finding.** This closes the
open follow-on from `q081_landmark_removal_arm_design.md` section 8 / addendum
(2026-08-01): "the other 10 ... were NOT individually re-adjudicated by this audit."

**Update, same day: the two precision gaps this triage found were FIXED, not left as
documented-only.** The "Known lint limitations" section below was originally written
before the fix landed; it is kept for the reasoning trail (why each fires the way it
did, and why fixing was judged safe), but the lint itself now no longer fires on 7 of
the 18 (418j, 418k, 785, 785a, 787, 804, 805) -- see "Precision fix landed" at the
bottom. The corpus pin moved from 18 to 11 (`ree-v3`
`tests/contracts/test_agent_construction_seed_order_lint.py`). Nothing in the
per-script materiality table below changes: all 18 verdicts (IMMATERIAL /
NEVER-RAN) stand exactly as adjudicated: only whether the LINT itself fires on the
now-cleared 7 has changed, not whether the bug was ever real in them, nor whether it
mattered.

## What this is

`ree-v3` `validate_experiments.agent_construction_before_seed_lint` (`--checks
agent_seed_order`, `ree-v3` `ccb96243eb`) is a WARN-only static lint that fires when a
module-level function constructs `REEAgent(...)` with no torch-RNG seed call earlier in
its own flow. `torch.nn.Module` weight init draws from torch's own global RNG, so an
unseeded construction gets weights that depend on process-level RNG history, not on
`seed`. It found 18 driver scripts with this shape, corpus-wide, pinned as a backlog
(not a target -- landed runs are not retro-edited) in
`tests/contracts/test_agent_construction_seed_order_lint.py`.

A lint fire is a **necessary-but-not-sufficient** signal: it proves an unseeded
construction call exists in that function's text, not that it affected the reported
result. This document is the materiality call for each of the 18, individually, against
its actual landed manifest and comparison design.

## Method: four ways a fire turns out immaterial

Triage found exactly four recurring reasons a flagged file's finding is unaffected,
none of them "got lucky":

- **(i) Shared-object / shared-template design.** The compared conditions run off the
  *same* agent (not even a copy -- MECH-135's FROZEN vs E1_COE scoring, SD-051's
  OFF-vs-ON authority toggle) or off `copy.deepcopy()` of one per-seed template
  (Q-081, INV-091). Whatever the uncontrolled weights are, every compared condition
  shares them identically, so a between-condition difference cannot be explained by
  weight-init variance.
- **(ii) Effect margin swamps plausible init variance.** Arms ARE independently
  constructed (no sharing), but the measured effect is many multiples of the
  pass/fail threshold, and/or the same degenerate value reproduces across multiple
  independently-seeded draws (ARC-065: entropy pinned at exactly 0.0 across 3
  independent OFF-arm constructions, vs. ~1.1 nats ON -- a 7x margin over the 0.15
  threshold; three independent draws landing bit-identical argues the collapse is
  architecture-driven, not init-driven).
- **(iii) The flagged construction is scaffolding that never executes in the scored
  run.** A `--dry-run` smoke-test branch inside `main()` builds an agent without
  seeding (the lint sees this, since it doesn't distinguish an early-return branch
  from the rest of the function), but the actual experiment loop calls a *different*,
  correctly-seeded function (SD-016: `_run_one_arm_seed` seeds before calling
  `_make_agent`; only the unrelated `--dry-run` branch in `main()` doesn't).
- **(iv) The flagged construction is a discarded probe; the real build is two hops
  away, inside a correctly-resetting `arm_cell`.** A recurring author idiom across
  several scripts: `probe_slice = _build(seed)[4]` before `with arm_cell(seed, ...)`,
  used only to harvest a static config-slice dict for the fingerprint -- the returned
  `agent`/`env` objects are thrown away. The REAL, scored agent is built by a helper
  called *from inside* the `arm_cell` block (`_collect_cell` -> `_build(seed)`), so it
  runs after `arm_cell.__enter__`'s `reset_all_rng(seed)`. The lint's one-hop name
  resolution (by design, see its docstring) sees only the shallow, discarded call and
  cannot trace the two-hop chain to the real one -- so it fires on the immaterial
  half of a script that get its real half right.

(iii) and (iv) are lint PRECISION gaps, not backlog-materiality arguments in the
Q-081/(i) sense -- see "Known lint limitations found during this triage" below for why
they are not being fixed in the lint right now.

## The 18, individually

| # | Script | Claim | evidence_direction | Design reason | Verdict |
|---|---|---|---|---|---|
| 1 | `v3_exq_824_q081_shared_organisation_landmark_removal.py` | Q-081 | non_contributory | (i) `copy.deepcopy` of shared P0 template | IMMATERIAL |
| 2 | `v3_exq_824a_q081_shared_organisation_landmark_removal.py` | Q-081 | non_contributory | (i) | IMMATERIAL |
| 3 | `v3_exq_838_q081_cross_stream_recording.py` | Q-081 | non_contributory | (i) | IMMATERIAL |
| 4 | `v3_exq_827_inv091_cross_stream_similarity_band.py` | INV-091 | non_contributory | (i) same shared-P0-template+arm_cell shape as Q-081 | IMMATERIAL |
| 5 | `v3_exq_827a_inv091_cross_stream_similarity_band_phase_sync.py` | INV-091 | non_contributory | (i) | IMMATERIAL |
| 6 | `v3_exq_828_inv091_cross_stream_similarity_band_remaining_ablations.py` | INV-091 | **weakens** | (i) | IMMATERIAL |
| 7 | `v3_exq_828a_inv091_cross_stream_similarity_band_null_validated.py` | INV-091 | **weakens** | (i) | IMMATERIAL |
| 8 | `v3_exq_615_arc065_rung1_matched_entropy.py` | ARC-065 | **supports** | (ii) 7x margin + bit-identical 0.0 floor across 3 independent draws | IMMATERIAL |
| 9 | `v3_exq_108_mech135_discriminative_pair.py` | MECH-135 | **supports** | (i) FROZEN/E1_COE scored off the literal same agent object | IMMATERIAL* |
| 10 | `v3_exq_418j_sd016_context_memory_reef.py` | SD-016 | -- (never landed a manifest) | n/a | NEVER-RAN -- crashed on an unrelated `torch.cat` dim-mismatch bug before any scored result; not in the current queue |
| 11 | `v3_exq_418k_sd016_context_memory_reef.py` | SD-016 | does_not_support | (iii) bug confined to `main()`'s `--dry-run` branch; real path `_run_one_arm_seed` seeds correctly | IMMATERIAL |
| 12 | `v3_exq_635_modulatory_bias_selection_authority_readiness.py` | (readiness diagnostic) | non_contributory | (i) OFF/ON authority toggled in place on one shared agent | IMMATERIAL |
| 13 | `v3_exq_688_mech044_hippocampal_relational_binding.py` | MECH-044 | superseded | doubly immaterial: already superseded/vacuous (G1/G2 self-route) AND the flagged construction is a P0-only readiness probe that never fed the (separately, correctly-seeded) arm comparison | IMMATERIAL |
| 14 | `v3_exq_785_mech463_arousal_variance_amplifier_decomp.py` | MECH-463 | superseded (by 785a) | (iv) | IMMATERIAL |
| 15 | `v3_exq_785a_mech463_arousal_exogenous_urgency_decomp.py` | MECH-463 | does_not_support | (iv); also single-agent-vs-i.i.d.-covariate design, not a between-agent comparison at all | IMMATERIAL |
| 16 | `v3_exq_787_mech463_hazard_geometry_exogenous_proximity.py` | MECH-463 | does_not_support | (iv); load-bearing stat is a per-seed OLS-slope t-test across 24 seeds, which already averages over between-seed noise | IMMATERIAL |
| 17 | `v3_exq_804_arc003_e3_selection_authority.py` | ARC-003 | **weakens** (C1 borderline FAIL) | (iv); `reset_all_rng(seed)` runs immediately before each arm's REAL `_build(seed)`, so arms are seed-MATCHED (byte-identical init) despite independent construction | IMMATERIAL |
| 18 | `v3_exq_805_arc016_eval_derived_commit_threshold.py` | ARC-016 | non_contributory (gate RED, non_degenerate=False) | (iv); additionally all three arms failed the SAME environmental precondition uniformly -- not a per-arm weight effect | IMMATERIAL |

\* 108 also carries a **pre-existing, unrelated** `evidence_direction_note` (a multi-sense
training-loop confound, flagged 2026-05-08, recommending re-run via StepHarness to
confirm direction) -- not resolved by this triage, not caused by the RNG bug, noted so a
future reader does not conflate the two open questions on this one script.

## Escalation outcome

**None.** Every one of the 18 was immaterial to its own reported finding. The two
`supports` carriers (615, 108) and the four live non-`non_contributory` carriers
(828, 828a `weakens`; 418k, 785a, 787 `does_not_support`; 804 `weakens`) were the
priority items and all cleared under (i)/(ii)/(iv) reasoning above -- see the per-row
justification; none required a downgrade or a re-run recommendation on RNG grounds.

## Known lint limitations found during this triage (historical -- FIXED same day, see below)

Reasons (iii) and (iv) were genuine precision gaps in
`agent_construction_before_seed_lint`'s Tier-1, one-hop-only design (stated as a
deliberate scope boundary in the lint's own docstring: "does NOT attempt... general
[reproducibility]... interprocedural reproducibility... is out of scope by design"):

1. **No branch-awareness.** The lint walked a function's whole direct statement flow
   without distinguishing an early-return `if args.dry_run: ...; return` block from
   the function's main path, so an unseeded smoke-test-only construction fired
   identically to a real one (case iii, SD-016).
2. **One-hop-only name resolution.** A "probe, discard, real-build-two-hops-away"
   idiom (case iv) -- confirmed as a recurring cross-script author pattern in 5 of
   the 18 (785, 785a, 787, 804, 805 -- NOT 688, see below) -- was invisible past the
   first hop, so the lint flagged the harmless discarded probe and never saw that the
   real, scored construction was correctly ordered.

Originally judged ACCEPTABLE-to-leave within the lint's stated WARN-only scope and
recorded here rather than fixed. **Superseded the same day** -- see "Precision fix
landed" below for why that judgment changed once the user asked for it explicitly:
trusting a future fire without re-deriving this triage each time is worth more than
the (real, but here judged small) engineering cost.

## Precision fix landed (2026-08-01, same session)

Both gaps above are fixed in `ree-v3` `validate_experiments.py` (commit lands with
this doc's update), not merely documented:

1. **Guard-clause isolation.** `_DirectFlowWalker.visit_If` now isolates any `if`
   whose body unconditionally exits (`return`/`raise`/`continue`/`break` as its
   last statement) into its own independently-checked scope, rather than merging
   its calls into the surrounding flow. A guard-clause branch with NO seed
   evidence of its own stays silent (Tier-1's existing "no local evidence" rule);
   a guard-clause branch that itself has a genuine bug still fires (verified by a
   dedicated negative-control test).
2. **Discarded-probe subscript detection.** A ctor call whose result is
   immediately subscripted (`_build(seed)[N]`) no longer counts as a
   construction event when the extracted index is POSITIVELY CONFIRMED (by
   tracing the callee's own `return <tuple>` statement for where its
   `REEAgent(...)`-holding variable appears) to be something other than the
   agent. Deliberately conservative: when the index or the callee's return
   shape can't be resolved, the call still counts (verified by two dedicated
   negative-control tests) -- a missed fire is judged worse than an occasional
   benign one, for a lint whose whole purpose is evidence-integrity assurance.

**Result: the corpus fire count dropped from 18 to 11.** Cleared: 418j, 418k (fix 1),
785, 785a, 787, 804, 805 (fix 2). **688 was NOT cleared, and correctly so** -- its
flagged construction (`test_agent = _build_agent(...)`) is a genuine unseeded build
directly assigned to a name and used for a P0 readiness check, not a discarded,
subscripted probe; it does not match either fixed pattern, and a dedicated negative-
control test (`test_real_688_construction_bug_still_fires`) pins that it must keep
firing. (The original draft of item 2 above listed 688 among the discard-pattern
carriers -- that was inaccurate; corrected here once the fix's own real-corpus
testing surfaced the discrepancy.)

None of the 18 per-script MATERIALITY verdicts above change: fixing the lint's
precision only changes whether the lint itself fires, not whether any of the 18
scripts' bugs were real or whether they mattered to a reported finding -- both were
already settled by the individual triage rows before this fix existed. Full test
coverage: `tests/contracts/test_agent_construction_seed_order_lint.py` (32 tests --
14 new: guard-clause isolation x3, discard-subscript detection x3, real-corpus
witnesses for the 7 cleared files x1 batch + 688's negative control, plus the
existing suite unchanged).

## Follow-on, unowned

- MECH-135 (108)'s pre-existing multi-sense training confound (`evidence_direction_note`,
  2026-05-08) still recommends a StepHarness re-run to confirm direction -- unrelated to
  RNG seeding, not touched here.
