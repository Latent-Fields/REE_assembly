# Evidence Backlog Literature Channel Probe (2026-08-25)

**Status: FINDING -- diagnostic probe only, no code/data changed.**

## Question

`evidence/planning/evidence_backlog.v1.json` (regenerated 2026-08-25T18:02:28Z,
commit `e65df1d395`, 417 items) carries `evidence_needed: ["experimental"]` on
416/417 items, with the sole exception (`EVB-PINNED-Q019`) holding an empty
`evidence_needed` list. The 2026-08-24T06:05:46Z scheduled `ree-lit-pull-am`
run correspondingly reported `NO PULL: selector returned NONE_AVAILABLE,
correctly`. Question: is the literature channel genuinely **drained** (every
literature need met, `NONE_AVAILABLE` is correct), or **not being emitted**
(the generator can no longer produce `evidence_needed: literature` at all, so
the selector is structurally starved regardless of real need)?

## Verdict: DRAINED, not broken

The generator can still emit `literature` -- the code path is live,
unconditional, and was itself corrected by a documented 2026-05-05 bugfix.
Every real claim in the current registry already meets every literature
sufficiency threshold the generator checks, so no item currently trips a
literature-need condition. `NONE_AVAILABLE` on 2026-08-24 was the correct
answer given the data, not a symptom of a starved generator.

## 1. Generator identity

`/Users/dgolden/REE_Working/REE_assembly/evidence/experiments/scripts/build_experiment_indexes.py`,
function building `backlog_items` inside `_write_planning_outputs` (the
per-claim loop starts ~line 5777, `evidence_needed` construction ~5928-6320).
Invoked as part of `REE_assembly/scripts/governance.sh`'s "derive-only
pipeline" stage (hence the generic `governance regen: derive-only pipeline
output` commit message that lands `evidence_backlog.v1.json` alongside
~40 other derived artifacts each cycle). Not referenced anywhere under
`REE_assembly/scripts/*.py` -- it lives under
`evidence/experiments/scripts/`, which is why a scoped grep of
`REE_assembly/scripts/` alone (as suggested in the brief) does not find it;
`evidence/planning/scripts/run_governance_cycle.py` also *reads* the backlog
(line 634) but does not write it.

## 2. Is `literature` still emittable?

Yes -- six live call sites add `"literature"` to the per-claim `evidence_needed`
set, none behind a feature flag (`grep` for a
`literature_channel`/`LITERATURE_ENABLED`-shaped flag in the file: no match):

| Line | Condition | Reason token |
|---|---|---|
| 5931 | `claim_meta is None and claim_type == "open_question"` (claim has zero evidence entries at all) | `no_evidence_for_open_question` |
| 5991-5993 | `lit_count == 0` | `missing_literature_evidence` |
| 5999-6001 | `conflict_ratio >= conflict_alert_threshold and lit_count == 0` | `directional_conflict_alert` |
| 6005-6007 | `current_status == "provisional" and lit_count < provisional_min_lit (2)` | `insufficient_literature_grounding` |
| 6015-6017 | `claim_id in conflicts_by_claim and lit_count == 0` | `active_conflict` |
| 6046-6048 / 6057-6059 | `external_precedence_pressure` / `consider_new_structure` structural triggers, each `and lit_count == 0` | `external_precedence_pressure` / `consider_new_structure` |

The only place `"literature"` is ever *removed* after being added is the
`mandatory_decision_checkpoint` guard (line 6210-6212), which discards both
`experimental` and `literature` together -- a deliberate "halt until a human
decision is recorded" gate, not a literature-specific suppression. There is
no unconditional discard of `literature` anywhere in the file.

## 3. Why none of the six conditions currently fire

Checked the live data the 2026-08-25T18:02:28Z regen actually ran against
(`claim_evidence.v1.json` as of the same window, and `claims.yaml`):

- **553 claims in `claim_evidence.v1.json`; 552 have `source_counts.literature >= 1`.**
  The single exception is the pseudo-claim id `"onboarding"` (a contributor
  smoke-test bucket label, not a registered claim), which never reaches the
  `evidence_needed` logic at all -- it fails the canonical-claim filter
  (`_CANONICAL_CLAIM_RE` / `claim_registry` membership check, ~line 5778) before
  the loop body runs. So `lit_count == 0` is true for zero real claims.
- **74 claims are `status: provisional`; only one (`MECH-040`) has
  `lit_count < provisional_min_lit (2)`** -- and at build time (18:02:28Z
  snapshot) `MECH-040` actually held `lit_count == 2` (visible in its own
  backlog entry's `signals.source_counts.literature`), exactly at the
  threshold, not below it, so `insufficient_literature_grounding` correctly
  did not fire. (A subsequent, unrelated live `lit-pull:` commit landed
  ~5h later at 23:11:27Z and the recomputed matrix now shows `MECH-040`
  at `lit_count == 1` -- a live data change that postdates this backlog
  snapshot, not a defect in this generator; a future regen will pick it up
  and correctly re-flag `MECH-040` if it stays below 2.)
- **No item in the actual 417-item backlog carries any of the six
  literature-triggering reason tokens.** Full reason tally across all 417
  items: `low_exp_conf` (346), `insufficient_experimental_replication` (208),
  `lit_only_above_cap` (198), `missing_experimental_evidence` (198),
  `synthetic_signals_only` (198), `active_conflict` (119),
  `directional_conflict_alert` (99), `mandatory_decision_checkpoint` (22),
  `proxy_stage_noise_expected` (1). Zero occurrences of
  `missing_literature_evidence`, `insufficient_literature_grounding`,
  `no_evidence_for_open_question`, `consider_new_structure`, or
  `external_precedence_pressure`.

This is consistent with sustained `/lit-pull` throughput: the repo's recent
commit history on this file's regen chain includes a steady stream of
`lit-pull: <claim(s)> ...` commits (e.g. `aa29e04c8f` Q-095,
`baa449053c` quarantine repair + MECH-054 gap fill, `1986e3e2c3` MECH-499/500,
`6314951852` SD-101/MECH-503), i.e. literature coverage has kept pace with
(and currently exceeds) every threshold the backlog generator checks.

## 4. Was this ever different? (git history)

`git log --oneline -S'missing_literature_evidence' -- build_experiment_indexes.py`
surfaces one substantive change: commit `11e15d4482` ("governance: backlog
mirrors matrix lit-exemption policy", 2026-05-05). Before that fix, the
backlog generator ran literature entries through the same epoch-applicability
filter (`is_applicable()`, `planning_criteria.evidence_applicability`) as
experimental entries, which silently dropped valid pre-2026-02-27 literature
citations from the backlog's view -- causing `missing_literature_evidence` to
fire spuriously on claims (`MECH-057`, `MECH-062`, `Q-019`) that already had
plenty of literature. The fix made literature entries bypass the epoch filter
(mirroring `_write_claim_evidence_matrix`'s existing policy), and the
commit's own verification note records `missing_literature_evidence` reasons
dropping from 3 to 1 backlog-wide (the remaining 1 being the `EVB-0131`
onboarding phantom, later filtered out entirely by the canonical-claim regex
added afterward). This was a **deliberate, documented correctness fix**, not
a retirement -- it made literature counting *more* accurate, and the
generator has counted literature correctly (and the registry has stayed
saturated) ever since.

No other commit in that `-S` history touches this logic; the literature-need
codepaths are otherwise unchanged since 2026-05-05.

## 5. Q-019's empty `evidence_needed` -- same defect or unrelated?

**Unrelated.** `EVB-PINNED-Q019` is a `"pinned": true` backlog entry, and
pinned entries are excluded from the entire auto-generation loop described
above (`_pinned_claim_ids` skip, ~line 5784: `if claim_id in
_pinned_claim_ids: continue`). Its `evidence_needed: []` is not computed by
any of the six branches in section 2 -- it is a **manually curated value**,
and its own `status_reason` field documents exactly when and why it was set:
a 2026-08-09 correction (`chip-20260809-evidence-backlog-false-lit-gaps`)
that changed it from `["literature"]` to `[]` because "literature base is
saturated ... no new searches warranted," specifically to stop it recurring
as a false positive in `/morning-digest` Literature Pull Candidate scans.
This is a separate, already-resolved incident on a pinned item, not a symptom
shared with the 416 auto-generated `experimental`-only items.

## Conclusion / re-trigger condition

The literature channel is fully live in the generator. It reads as empty
right now because literature coverage across the claims registry is
genuinely saturated relative to every threshold the generator checks
(`lit_count == 0`, and `provisional_min_lit = 2` for provisional claims),
which is itself the product of sustained `/lit-pull` activity, not a
regression. `NONE_AVAILABLE` from the 2026-08-24 lit-pull selector run was
the correct answer.

It will re-trigger literature emission automatically, next regen, as soon as
any of: (a) a claim's `source_counts.literature` drops to 0 (e.g. a
quarantine/dedup pass removing an entry, as may already be happening to
`MECH-040` per section 3); (b) a new claim or `open_question` is registered
with zero evidence; (c) a provisional claim's literature count regresses
below 2; or (d) a conflict/escalation/external-precedence structural trigger
newly engages on a claim that currently has `lit_count == 0`. No code change
is recommended -- this is a data-state finding, not a generator defect.

## Scope note

Diagnostic probe only, per CLAUDE.md work-graph vocabulary
(`complex (probe-gated)` -> converted to fact). The generator, backlog file,
and lit-pull selector were not modified. If MECH-040's apparent regression
(section 3, lit_count 2 -> 1 same day) turns out to be a real coverage loss
rather than a legitimate dedup, that is a separate, narrower question for
`/governance` or a future `/lit-pull` run to pick up on its own -- not
something this probe should act on.
