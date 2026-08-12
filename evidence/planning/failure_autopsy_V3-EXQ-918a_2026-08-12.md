# Failure Autopsy: V3-EXQ-918a (SD-RESIDUE-VALENCE-BOUND validation)

**Generated:** 2026-08-12T04:56:07Z
**Scope:** single
**Status:** confirmed
**Target:** `v3_exq_918a_sd_residue_valence_bound_validation_20260812T044049Z_v3` (PASS, diagnostic, `claim_ids: []`, `queue_id: V3-EXQ-918a`)

## Why this session ran

Pulled from `pending_review.md`'s mandatory "Diagnostic -- autopsy required (no confirmed
adjudication)" section, the blanket rule from the 2026-08-07 correction: **every**
`experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a confirmed `/failure-autopsy`
before governance acts on it, regardless of whether the indexer's own `adjudication` flag
caught anything. This was the only entry left in that section after a fresh regen
(`sync_v3_results.py` -> `build_experiment_indexes.py` -> `generate_pending_review.py`,
2026-08-12T04:52Z).

Scoping note: of the 10 FAILs also listed in `pending_review.md` at the time of this session,
three already had confirmed autopsies (`V3-EXQ-894c`, `V3-EXQ-910a`, the `V3-EXQ-912-913`
fishtank cluster) -- `review_tracker.json`/`pending_review.md` simply hadn't caught up, which is
governance's regen to run, not this skill's. `V3-EXQ-916/916a/917/920` had also just been
autopsied by a prior session in this same worktree (`failure_autopsy_V3-EXQ-916-916a-917-920-
fishtank-cluster_2026-08-12.md`). Of the remaining un-autopsied candidates
(`V3-EXQ-914`-cluster/MECH-236, `V3-EXQ-603t`/MECH-357, `V3-EXQ-919`/MECH-321,
`V3-EXQ-228d`/ARC-032, `V3-EXQ-922`/SD-016 combo, `V3-EXQ-918a`), `V3-EXQ-603t` was deliberately
excluded from the scoping menu -- the concurrently-active `mech357-pressure-scoping-11e9c9`
session already owns that exact claim (MECH-357 causal localisation). The user selected
`V3-EXQ-918a` at the scoping `AskUserQuestion` (recommended option; logged to
`RECOMMENDATION_LOG.jsonl`).

## 2a. Dry-run gate

`check_dry_run_citations.py` run over all 10 candidate run_ids from the scoping menu, including
this target: **0 dry cited, 0 dry in named families, 0 ambiguous, 10 clean, 0 unknown.** Real
run (`N_SEEDS=3`, not `--dry-run`'s single seed).

## Facts reconstruction

**Manifest.** `outcome: PASS`, `evidence_direction: supports`, `non_degenerate: true`,
`degeneracy_reason: null`. Recording provenance complete: `recording_schema: "rec/v1"`,
`substrate_hash` present, `machine: "ree-cloud-2"`, `machine_class:
"linux-x86_64-py3.10-torch2.12.0+cpu"`, `elapsed_seconds: 0.319`, full `config`, explicit
`seeds: [0, 1, 2]`. `substrate_commit` recorded (`c4baf80c`, `dirty: False`,
`substrate_stable_across_run: true`).

**Script** (`ree-v3/experiments/v3_exq_918a_sd_residue_valence_bound_validation.py`).
Unit-level test against `ResidueField`/`RBFLayer` directly (no `CausalGridWorldV2`/`REEAgent`
needed -- the fix is a single central write path, matching the V3-EXQ-520 Part-1 precedent for a
ResidueField-internal readiness diagnostic). Design: 2 bounding arms (`OFF` = pre-fix default,
`ON` = `valence_bounding_enabled=True, valence_decay_rate=0.02, valence_clamp_abs=5.0`) x 3
channels (`positive_surprise`, `negative_surprise` via `update_valence`;
`wanting_sensitized` via `update_wanting_sensitized`, a distinct call path sharing the same
underlying primitive) x 3 seeds = 18 cells, 200 repeated writes per cell landing on the SAME
z_world point (reproducing an agent revisiting the same RBF center under sustained exposure --
the exact scenario the motivating autopsies exercised).

**Pre-registered criteria (all load-bearing, plain AND):**
- C1 `off_arm_reproduces_unbounded_growth`: OFF final |value| clears `0.8 * 200 * 1.0 = 160`.
- C2 `on_arm_stays_bounded`: ON final |value| <= `5.0 + 1e-3`.
- C3 `off_arm_bit_identical_to_pre_fix`: OFF final value == `200 * value` exactly (float tol),
  applies only to the two direct-channel cells (positive/negative_surprise) -- `wanting_sensitized`
  is gain-saturating, not a flat per-write constant, so the driver correctly exempts it
  (`exact_match_to_naive_sum: None` on those rows) rather than mis-scoring a nonlinear channel
  against a linear-sum check.
- C4 `mech094_hypothesis_gate_unaffected`: with `hypothesis_tag=True` throughout, the tracked
  value never leaves its 0.0 init, under BOTH bounding conditions.

**Readiness** (non-vacuity guard, self-routes `substrate_not_ready_requeue` on failure, never a
false structural verdict): `active_center_exists` -- before testing, one `accumulate()` call
must seed a real active RBF center; without one `update_valence` no-ops silently and every
result would falsely read as bounded.

**Queue entry.** `V3-EXQ-918a` supersedes `V3-EXQ-918` (ERROR, crash-before-manifest --
root-caused by `/diagnose-errors` the same session as a queue-before-fix race: `ree-cloud-3`
pulled `main` inside the 26-minute window between the script's push and the substrate fix's
push, not a script bug). Byte-identical script, re-run once the substrate fix was safely on
`main`.

**Observed vs expected.** Exactly as predicted: OFF-arm final values are 200.0 (positive),
-200.0 (negative), bit-identical to the pre-fix naive sum; the third (wanting_sensitized)
channel saturates nonlinearly at 395.5, correctly exempted from the exact-match check. ON-arm
final values clamp to exactly ±5.0 (or +5.0 for wanting) on every cell. No criterion failed --
all four load-bearing criteria pass, and the readiness precondition is met on 100% of the 18
cells (verified directly against the raw `arm_results`, not just the manifest's own summary
flags).

## Claim-layer mapping

N/A. `claim_ids: []` -- confirmed against `docs/architecture/sd_residue_valence_bound.md`'s own
"Related Claims" section: no `claims.yaml` claim gates on this SD (`unblocks_claims: []`). The
fix "bears on" MECH-307 (the split-surprise mechanism whose excite/dread writes are the
most-affected components) and SD-014/ARC-036 (the valence-vector mechanism this accumulator
belongs to) by corroboration/repair -- restoring trustworthiness to readouts several diagnostic
showcases explicitly flagged as contaminated -- not by any claim status change.

## Biological-reference triage

Closest mechanism: bounded/habituating accumulation of affective signal at a fixed-capacity
memory substrate (the RBF center pool, 32 centers by default) -- a leaky-integrator decay plus
hard clamp is the standard computational analog of homeostatic/allostatic bounding, preventing a
small, reused set of memory nodes from accumulating unbounded valence under sustained
revisitation. This is not a formal-definition import standing in for a biological mechanism
(SD-003's failure mode) -- it is plumbing restoring an *assumed* invariant (valence magnitude
stays in a bounded, interpretable range) that the pre-fix code silently violated. No new
scientific claim is under test here, so the "is biology divergence load-bearing" question does
not apply; the biological framing is offered only as the design rationale already stated in the
SD doc, which this autopsy confirms is sound and does not need independent lit-pull support
(no `claims.yaml` claim rides on it).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | `claim_ids=[]`, no claim gates on this SD |
| Biological reference | clear | bounded-accumulator/habituation pattern; restores an assumed invariant, not a novel mechanism under test |
| Developmental / dependency prerequisites | present | `depends_on: none` |
| Implementation completeness | complete | single shared helper (`ResidueField._valence_bound_params()`) resolves both parameters from config for both callers (`update_valence`, `update_wanting_sensitized`); off-by-default (`valence_bounding_enabled=False`) preserves all historical evidence bit-identical (confirmed here by C3 and independently by the SD doc's own backward-compat note re: a full `--dry-run` of `v3_exq_887` at default config) |
| Environment adequacy | adequate | unit-level test at the exact primitive is the correct scope for a single central write-path fix -- no CausalGridWorld/REEAgent machinery needed, matches the V3-EXQ-520 Part-1 precedent |
| Measurement adequacy | adequate | readiness precondition rules out the silent-no-op false-bounded failure mode; C1-C4 jointly cover bug reproduction, fix efficacy, backward-compat exactness, and non-interference with the MECH-094 gate |
| Integration adequacy | coupled, stable | one control point for all 13 `agent.py` call sites plus the sensitized-wanting path; `valence_vecs` is a `register_buffer` not an `nn.Parameter` (writes under `torch.no_grad()`), so MECH-094 phased-training gating is structurally unaffected, not merely empirically unaffected |
| Scale / capacity | n/a | plumbing fix, not a representational-capacity question |

**Failure-location triage (GOV-FAILLOC-1):** not applicable. There is no FAIL and no
organism-level "REE failed" read to classify here -- this is a clean confirming validation of an
already-landed fix.

## Learning extracted

- The fix (landed `ree-v3 00449c7d0e`, this session per the SD doc) is genuinely validated, not
  merely self-reported: independent unit-level reproduction of both the original bug (unbounded
  OFF-arm growth, exactly matching the pre-fix `+=` semantics) and the fix (bounded ON-arm,
  clamped to exactly the configured `valence_clamp_abs`).
- The readiness precondition is not decorative -- it is the exact guard that prevents a silent
  `update_valence` no-op (e.g. if `accumulate()`'s center-activation path were itself broken)
  from producing a false "bounded" reading. It held at 100% here, so no instrument-gap
  contaminates the verdict.
- `wanting_sensitized`'s correct exemption from the C3 exact-match check (its own
  `exact_match_to_naive_sum: None`) demonstrates the driver author already understood the
  channel is gain-saturating rather than a flat per-write accumulator -- appropriately scoping a
  linear-sum check to only the two channels it actually applies to, rather than a blanket
  application that would have manufactured a spurious near-miss on the third.
- The previously-descoped "residue_wanting orphaned writer" bug (same failure-autopsy cluster
  that motivated this SD, but a structurally separate defect -- `update_benefit_salience()`/
  `update_schema_wanting()` never called from the 906-family driver step loop) is confirmed
  fully handled by a separate, already-landed thread: `V3-EXQ-916a` (ree-v3 `26260a519634`)
  wired the writer calls in, and two follow-on chips
  (`chip-20260811-sd-residue-valence-bound-wanting-resolved`,
  `chip-20260812-zgoal-wanting-coupling-reinstrument`) closed the loop on marking
  `substrate_queue.json`'s `failure_record` entries resolved and re-instrumenting the coupling
  measurement on the repaired substrate. Nothing further to route from this autopsy on that
  thread.

## Recommended routing

**None.** The SD (`SD-RESIDUE-VALENCE-BOUND`) is already `status: implemented` per its own doc,
and this run is the validation that confirms the implementation is correct and non-vacuous. No
claim status to write, no substrate gap to register, no re-run needed. The only action this
autopsy enables is clearing the `pending_review.md` "Diagnostic -- autopsy required" flag for
this run_id at the next `/governance` walk (governance's regen to run, not written here).

Draft `recommended_evidence_quality_note` (scoped to the SD, since no claim carries it):
"V3-EXQ-918a (confirmed `/failure-autopsy` 2026-08-12) independently validates
SD-RESIDUE-VALENCE-BOUND: unit-level reproduction of both the original unbounded-accumulator bug
(OFF arm, bit-identical to pre-fix `+=`) and the fix (ON arm, clamped to exactly
`valence_clamp_abs`), across 3 channels x 3 seeds, with a met readiness precondition ruling out a
silent-no-op false-bounded reading. Self-route label `sd_residue_valence_bound_validated` is
accurate and non-vacuous."

## User confirmation

Presented via `AskUserQuestion` (Step 8 gate): four-layer diagnosis, recommended
`epistemic_category: standard`, `evidence_direction: supports` (of the SD only), and "no further
routing needed" (SD already implemented; the orphaned-writer half already fully handled by a
separate landed thread). User confirmed as diagnosed (recommended option; logged to
`RECOMMENDATION_LOG.jsonl`).
