# Steward -- closure-map integrity detectors (stage 1)

Deterministic, read-only integrity checks over `docs/claims/claims.yaml` and the
`closure_plan` frontmatter of every `evidence/planning/*_plan.md`.

```bash
# from REE_assembly/ root
/opt/local/bin/python3 scripts/steward/run_detectors.py
/opt/local/bin/python3 scripts/steward/run_detectors.py --json     # full report
/opt/local/bin/python3 scripts/steward/run_detectors.py --no-write # dry run
/opt/local/bin/python3 -m pytest scripts/steward/test_run_detectors.py -q
```

## Why this exists

On 2026-08-15 SD-031 was found to be live V3 work (`implementation_phase: v3`,
`v3_pending: true`) whose only owning closure node, `self_attribution:GAP-5`, was
`deferred` -- and `generate_closure_snapshot.py` drops deferred nodes from the V3
denominator outright. SD-031 was therefore not done, not remaining, and not
visible as a gap. It sat that way for ten weeks. The fix was to split
`self_attribution:GAP-6` out (closure 72.6% -> 71.9%: a *correction*, not a
regression -- the number falls because the correction surfaces hidden work).

Nothing about **detecting** that required judgement. A 20-line script would have
caught it the same day for zero tokens. That is the thesis: detection is
deterministic and free, and the model is for adjudication only.

## The escalation gate

`reports/steward_report.json` carries one boolean, `escalate`, and that boolean
is the entire cost-control mechanism -- it decides whether a model is loaded at
all.

A finding escalates only if it is **NEW** (absent from the previous run's
`state/steward_state.json`), **unsuppressed**, and flagged `escalate` by its
detector. So the first run after a defect appears is loud, and every run after
that is silent until something changes. An unfixed defect is real, but it is not
news, and re-escalating it every cycle would spend the budget on things a human
has already seen and chosen to leave.

Findings that disappear are reported as **RESOLVED** rather than escalated: SD-031
no longer appearing under D-002 is the ratchet working.

At most 5 findings escalate per run, ranked by `severity x confidence`. **That cap
is a budget, not a filter** -- every finding always appears in `findings`, and the
overflow count is reported as `escalation_truncated` so five never reads as "all
of them".

## Detectors

| id | what it finds | validated |
|----|---------------|-----------|
| **D-002** | Orphan V3 claim: claim reads as live V3, every owning closure node is `deferred` -> invisible to closure accounting. The SD-031 class. | yes -- precision 4/4 |
| **D-001** | Claim `implementation_phase` disagrees with the `generation` of every plan that owns it. Same denominator-invisibility harm, reached along the generation axis. | no |
| **D-010** | Guards the accounting itself: recomputes the V3 denominator independently and reports every way it differs from what a reader would assume. | n/a (structural) |

Ownership is `unblocks_claims` on a node -- deliberately **not**
`join.scope_claims`, which is a broad "bears on" association (one live node lists
2 of the former and 29 of the latter).

D-001 is **not** a duplicate of `scripts/check_claim_phase_consistency.py`: that
walks the claim->claim dependency graph, this compares a claim against the plan
that owns it.

## Baseline on REE_assembly `7f7a1bd80d` (2026-08-16)

Whole run: **0.5s**, well inside the 10s budget. `claims.yaml` is ~1000 entries;
loading it costs 5.6s under the pure-python YAML loader and 0.39s under libyaml's
`CSafeLoader`, which is why `_common.py` reaches for the C loader and why
detectors take a shared `Context` instead of re-reading.

| detector | findings |
|---|---|
| D-002 | **4** -- MECH-316, MECH-317 (P0/strong), MECH-091, MECH-314a (P1/weak) |
| D-001 | 27 |
| D-010 | 1 (silent-exclusion surface: 10 `assembling` nodes) |

D-010 independently reproduces the committed snapshot exactly: 117 v3 nodes,
denominator **94**, and a status tally matching `closure_status.md` line for line,
with zero weight drift against `serve.py`.

**These counts are expected to fall and are deliberately NOT asserted in the
tests.** The 2026-08-15 adjudication (`7478ffe8ad`) *proposed* un-deferring the
three owning nodes to `/governance` rather than applying it; when governance
acts, those D-002 findings correctly disappear. A test pinned to the live number
would fail on a correct fix and teach the next session to weaken the detector.
The tests pin the classification logic; this table is a baseline to re-measure.

## Two corrections to the stage-1 spec, both found by running it

**1. The closure denominator is not "not deferred".** The natural one-line
statement --

```
{node : node.status not in DEFERRED_STATUSES and plan.generation == v3}
```

-- is wrong. `generate_closure_snapshot.py` builds the denominator from
`STATUS_WEIGHTS.get(status)` being non-`None`, and that exclusion set is a strict
superset of `DEFERRED_STATUSES`: it also holds `assembling`, `open_by_design`,
`deferred_v5`, `parked`, `parked_indefinite`, `closed`. On this tree the true
denominator is `117 - 13 deferred - 10 assembling = 94`, matching the committed
snapshot; the `DEFERRED_STATUSES`-only reading predicts 104. D-010 implements the
real rule and reports the gap as its standing output.

**2. D-002 must key on `deferred`, not on "excluded from the denominator"**, even
though the harm is identical. The wider set includes `assembling` -- "required for
v3, actively under construction, leave it alone", the anti-forcing status that
exists so unhurried assembly is not scored as failure. Widening the predicate
added exactly three claims (ARC-108, MECH-450, SD-033b), all owned by `assembling`
nodes, none orphaned: pure false positives against work the design deliberately
protects, diluting the one detector whose precision is its whole value. The wider
surface is real and belongs to D-010, which reports it as a surface rather than as
per-claim defects.

## Do not re-introduce a signal-strength gate on D-002

An earlier revision gated escalation on `v3_pending`, demoting MECH-091 and
MECH-314a to list-only. Adjudication returned precision **4/4** and refuted it --
MECH-314a was a real stale node the gate would have withheld indefinitely.
`severity` and `signal` **rank** findings when the budget is contended; they never
withhold one. Pinned by `test_d002_escalates_weak_signal_too`.

The general rule: a precision floor is legitimate only for a detector whose
findings are **noisy** -- never for one whose **misses are silent**. D-001 is
noisy (the literal any-owner reading fires 63 times, mostly benign forward
back-pointers), so it is scoped, and the narrowing is reported as a count rather
than applied silently. D-002's misses are silent by construction, so it is not
scoped.

D-002's weak tier is ranked P1/0.8 rather than P2/0.6 for an evidential reason:
every finding it has produced was adjudicated genuine, so even its weak tier
carries more evidence than an unvalidated detector's strong tier. Ranked lower,
D-001's P1 findings displace MECH-091 and MECH-314a out of the budget on a first
run -- the same withholding-by-signal, arriving through the ranking door instead
of the gate door.

## Suppressions

`state/suppressions.yaml`. A suppression stops a finding **escalating**; it never
removes it from the report (`"suppressed": true` plus the reason stays attached).
It is a recorded disposition, not a mute button. `finding_id` may be an fnmatch
pattern, so a whole class can be covered by one line.

Seeded with the three entries from `DETECTORS.md`. Two are **forward-declared**
for detectors stage 1 does not build (`MAE-3` whole-plan back-pointer,
`V3-EXQ-732b` deliberate refusal); they match nothing today and are kept so the
disposition is not lost when the owning detector lands.

Known clustering worth a future whole-plan entry: of D-001's 27 findings, 10 come
from one `generation: clinical` plan and 3 from one `generation: deferred` plan --
systematic back-pointer patterns rather than 13 independent defects. Collapsing
them is a *disposition*, which stage 1 has no authority to make; it belongs to
governance, and the ledger is what calibrates it.

## Scope -- what stage 1 deliberately does not do

- **Read only.** No edit to `claims.yaml`, no node status change, nothing queued.
  There is no auto-fix path.
- **Not wired into `governance.sh`.** Runnable by hand first.
- **Three detectors, not thirteen.** The ledger from three is what calibrates
  escalation ranking, and that calibration is wasted if done against thirteen.

`state/steward_ledger.jsonl` gets one line per run (counts, escalated ids,
duration, per-detector totals). Its value is the time series.

`state/steward_state.json` is absent until the first run, which is what makes that
first run escalate everything. `reports/` is gitignored for stage 1; whether the
report should be committed is a stage-2 wiring decision.
