---
name: steward
description: >
  Long-running integrity steward for the REE closure maps, claim registry and
  git state. Detects cross-artefact inconsistencies deterministically, repairs
  the mechanical ones without an LLM, escalates only genuinely ambiguous
  findings, and converts every adjudication into a durable detector so the same
  defect class never needs a model again. Invoke ONLY when
  `steward_report.json` sets `escalate: true`, or when explicitly asked to
  audit, adjudicate a finding, or add a detector.
---

> **PRESERVED DESIGN DOCUMENT.** Verbatim from
> `/Users/dgolden/.ree_handover/20260815-steward-integrity-skill/SKILL.md`
> (2026-08-15), committed into the repo on 2026-08-17 by
> `chip-20260816-steward-handover-design-docs-into-repo`. It had existed only on
> the Mac, outside version control, unreadable from any other machine -- which
> forced `chip-20260815-steward-stage1-detectors` to reconstruct detector
> semantics from other evidence when it was dispatched to `ree-cloud-5`.
> **The prose below is the ORIGINAL design of record and is not edited except
> where a block is explicitly marked `AS BUILT`.** For what actually shipped,
> `scripts/steward/README.md` is authoritative; see `docs/README.md` here for
> the as-built map.
>
> **This is a DESIGN document, not an installed skill.** No `steward` skill is
> registered in `.claude/skills/` or `.agents/skills/`; the frontmatter above is
> preserved because the `name` + `description` pair *is* the invocation contract
> being specified. What exists today is the deterministic detection half
> (`scripts/steward/run_detectors.py` + 8 detectors, wired into `governance.sh`
> as Step 3m). The escalation/adjudication half described below -- the skill body
> a model loads on `escalate: true` -- is **not built**.

# Steward

## What this exists to fix

On 2026-08-15 a live V3 claim (SD-031) was found sitting inside a `deferred`
V4 closure node. It had been rescoped v4 → v3 on 2026-06-06; the node that
owned it was never updated. For ten weeks the claim was invisible to closure
accounting — not done, not remaining, not a gap — and the V3 percentage was
overstated as a result.

Nothing about that defect required judgement to *detect*. Five artefacts said
v3, one said v4. A twenty-line script comparing `implementation_phase` against
the generation of the owning plan node would have caught it the same day, for
zero tokens.

That is the thesis of this skill: **most integrity defects in this repo are
deterministic to detect and only occasionally require judgement to resolve.**
The model is the scarce resource. Spend it on adjudication, never on detection.

## Operating model

Three tiers, and the cost profile is the whole point.

| Tier | Detection | Resolution | LLM cost |
|---|---|---|---|
| **T0** | deterministic | mechanical auto-fix | none |
| **T1** | deterministic | needs judgement | one adjudication, bounded |
| **T2** | model-discovered | needs judgement | scheduled, rare, budgeted |

The common path is T0/T1. T2 is a discovery sweep that runs on a slow cadence
(monthly, or after a large structural change) and exists mainly to *manufacture
new T0/T1 detectors*.

## The ratchet — how this gets cheaper over time

Every T1/T2 adjudication **must** terminate in one of three durable artefacts.
An adjudication that produces only a fix is incomplete and the skill should
refuse to close it:

- **`promote`** — write a new deterministic detector so this defect class is
  free to find from now on. Required whenever a T2 finding is confirmed.
- **`suppress`** — record a suppression keyed by `finding_id`, with a reason
  and (where applicable) a `resume_condition`. A declined finding must never
  re-escalate.
- **`refine`** — tighten an existing detector that produced a false positive.

Every adjudication also appends one record to `steward_ledger.jsonl`:

```json
{"ts":"...","finding_id":"...","detector_id":"D-002","verdict":"confirmed",
 "action":"promote","artefact":"detectors/d011_gate_cleared.py",
 "tokens":4120,"human_adjudicated":true}
```

That ledger is the training data. A weekly rollup computes per-detector
precision (`confirmed / (confirmed + false_positive)`) and:

- precision **< 0.6** → detector auto-demoted to *list-only* (reported, never
  escalated) until refined. This matches the existing `GOV-GRAN-1` P1
  list-only idiom rather than inventing a new one.
- precision **> 0.9** and fix is mechanical → candidate for promotion T1 → T0.

**Precision floors apply only to detectors whose findings are noisy — never to
detectors whose misses are silent.** Before gating a detector on precision,
ask what a miss costs. If the defect announces itself eventually (a failing
test, a red pipeline, a number that visibly moves), a floor is right. If the
defect is invisible by construction — as an orphaned V3 claim is: not done,
not remaining, not a gap — a miss costs months of a wrong number and nothing
surfaces it. Those detectors escalate unconditionally, and `severity` merely
ranks them under budget contention.

This rule is written from a live mistake. D-002's cycle-1 refinement gated on
signal strength and would have withheld a real finding indefinitely; cycle 2
measured 4/4 precision and removed the gate. The generalisation is not "D-002
is accurate" — n was 4 — it is that the cost asymmetry, not the precision
estimate, was the load-bearing consideration all along.

**Before building any detector, check whether an existing check already owns
the defect class.** Two systems detecting one defect hold *separate suppression
state*, and a finding suppressed in one but live in the other reproduces the
exact failure most of these detectors exist to prevent: a partial fix that
reads as complete. Divergent suppression is worse than no suppression, because
it is silent.

D-004 was retired under this rule on 2026-08-16 — the morning digest's Step 7c
had already absorbed both the defect and its recurrence-suppression rule.
Steward's job is to cover what nothing covers, and to make suppression durable
where coverage exists. It is not to re-detect in parallel.

**The success metric is escalations per run trending down while confirmed
fixes per run holds flat or rises.** If escalation volume is flat, the ratchet
is not engaging and the detector set is wrong.

## Invocation economics

The skill body must not load on a clean repo. The gate is a file, not a model:

1. `scripts/steward/run_detectors.py` runs from `governance.sh` and cron. Pure
   file reads, no network, no model. Target wall-clock < 10s for the full set.
2. It writes `steward_report.json` with `escalate: true|false`.
3. **Only `escalate: true` justifies loading this skill.** A human or agent
   that opens Steward on a clean report has already wasted the budget it exists
   to protect.

When escalation does happen, the payload is bounded:

- **max 5 findings per run**, ranked by `severity x confidence`
- **max 40 lines of evidence excerpt per finding** — never whole files; the
  detector extracts the specific conflicting lines with paths and line numbers
- recurring-but-unadjudicated findings collapse to **one line** plus a pointer
  to the prior ledger record
- suppressed findings are **absent entirely**, not summarised

Anything over budget is deferred to the next run rather than truncated
silently. Silent truncation reads as "covered everything" when it did not.

## Repair authority

Bounded deliberately, because this operates on a governed research record.

**May do without asking**
- T0 mechanical fixes in plan frontmatter and generated indices (date drift,
  duplicate flag entries, dangling-link repair where the target is unambiguous)
- Write new detectors, suppressions, ledger records
- Regenerate derived artefacts it is the declared owner of

**Must propose, never apply**
- Any `claims.yaml` edit — the claim registry is governance-owned
- Any node **status** change (`blocked` → `open` etc.), any `owner_exq`
  assignment, anything that queues an experiment
- Any generation reassignment (v3 → v4/v5). The 2026-08-15 precedent sets the
  bar: MECH-095 was reassigned only after a *valid, non-degenerate* ceiling hit
  empirically confirmed the substrate was the blocker. Reassignment off invalid
  or degenerate runs is forbidden.
- Anything touching git refs (see the git lane below)

**Never**
- `reset --hard`, bare `update-ref`, force-push, history rewrite on a shared
  checkout

## Git lane

This repo is a shared checkout that other machines push to. Two rules earned
the hard way on 2026-08-15:

- **Re-read the remote ref immediately before any write.** `origin/master`
  moved three times in a single session; an equivalence check performed against
  a ref that has since advanced is worse than no check, because it reads as
  verified. `D-102` enforces this by recording the ref at detection time and
  aborting if it moved before action.
- **Classify divergence by content, not by count.** "66 ahead / 274 behind"
  sounds catastrophic and was not: 28 commits were already upstream by
  patch-id, and every substantive remainder was present on origin by content.
  `D-101` produces that classification automatically and emits a verdict of
  `safe_to_adopt` / `needs_rebase` / `unique_work_present`.

## Escalation prompt contract

When the skill is loaded, it receives the bounded report and must, per finding,
produce exactly:

1. **Verdict** — `confirmed` / `false_positive` / `wontfix`
2. **Evidence** — which artefacts were consulted and what each said. Follow the
   2026-08-15 SD-031 precedent: enumerate every artefact and its reading, and
   state the count (*"six consulted, five say v3, one says v4"*). A verdict
   that cites fewer than two independent artefacts is not a verdict.
3. **Mechanism** — *why* the defect arose. "GAP-5 was the only node never
   revisited since registration, so the rescope never propagated" is what makes
   a defect preventable rather than merely fixed. This sentence is what becomes
   the next detector.
4. **Ratchet artefact** — `promote` / `suppress` / `refine`, with the file
   written.
5. **Blast radius** — if the fix moves a published number (closure %, counts),
   measure it by A/B regeneration on the same base. Never estimate. Never
   difference against a committed dashboard that may be stale.

## Files

```
scripts/steward/
  run_detectors.py          # runner; writes steward_report.json
  detectors/
    d001_phase_generation_mismatch.py
    d002_orphan_v3_claim.py            # reference implementation
    ...
  state/
    steward_state.json      # seen findings, first-seen timestamps
    suppressions.yaml       # finding_id -> reason, resume_condition
    steward_ledger.jsonl    # append-only adjudication record
  reports/
    steward_report.json     # the escalation gate
```

See `DETECTORS.md` for the catalogue and the seed suppressions.
