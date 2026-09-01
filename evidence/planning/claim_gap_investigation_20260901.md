# Do stale dependency edges point at missing claims?

**Date:** 2026-09-01
**Session:** `govrule-gaps-20260901` (follow-on to `sd003-groupAC-20260901`)
**Question, as posed:** the terminal-dependency lint surfaced 20 edges from live claims to dead
ones. Do those edges indicate *gaps* — places where a claim ought to exist and does not?
**Answer: NO for the edges. YES for the registry, but the gap is somewhere else entirely, and it
was already being reported by a standing audit nobody had read.**

---

## Part 1 — the hypothesis, and why it does not survive

The hypothesis is a good one: a live claim depending on a dead claim with no successor might be
saying *"I need something"* and pointing at the nearest thing that ever supplied it. If nothing
replaced the target, the need would still be unmet — and the edge would be a signal, not debris.

Tested against all 15 unreferenced edges. **Every dead target is accounted for.**

| target(s) | edges | disposition | gap? |
|---|---|---|---|
| `Q-008`, `Q-009`, `Q-011` | 3 | each titled **"Legacy: resolved in favor of …"** — the question was answered | no |
| `IMPL-021`, `IMPL-022`, `IMPL-024` | 4 | each titled **"Legacy … contract"** — superseded documentation contracts | no |
| `MECH-058` | 1 | has a successor: `MECH-069` | no |
| `MECH-475` | 1 | retired, rationale recorded; dependents **explicitly considered** in the note | no |
| `MECH-476` | 1 | retired, **"withdrawn into MECH-459/460"** — content rehomed | no |
| `SD-003` (unreferenced) | 5 | has successors `MECH-256`/`SD-029`; 4 of the 5 written *after* it died | no |

The IMPL/Q cluster is the clearest: those are documentation artifacts whose questions closed, and
the claims still depending on them are themselves IMPL documentation artifacts. Nothing is waiting
on them.

`MECH-475`/`MECH-476` looked most promising — substantive scientific claims, `retired`, empty
`superseded_by`, and a live claim (`SD-083`) still depending on both. But reading the retirement
notes, both were withdrawn with the destination recorded: MECH-476 *into* MECH-459/460, and
MECH-475's note states directly that "MECH-476/MECH-460 (which cite MECH-475 in depends_on) lean on
the independently-established destructiveness phenomenon, not on MECH-475's attribution." The
content has a home. **What is missing is the machine-readable pointer, not the claim.**

### A sub-hypothesis, tested and also negative

If MECH-476 records its successor in prose while leaving `superseded_by` empty, perhaps that is
systematic — a class where live content *looks* orphaned because the trail sits in a note. Checked
all 23 terminal-status claims for a successor named in prose but absent from `superseded_by`:
**exactly one instance (MECH-476).** A class of one is not a class. No detector is warranted; the
single field is worth filling by hand.

**Conclusion for Part 1: the stale edges are bookkeeping residue.** They are worth clearing for
hygiene — and the terminal-dependency lint added earlier today will keep them visible — but they
carry no information about unmet needs.

---

## Part 2 — where the gaps actually are

The instinct was right; the population was wrong. `governance.sh` **Step 3l-bis** already runs a
dangling claim-reference audit, and it reports **17 ids that are cited as claims but were never
registered**. This is a standing report, warn-only, and it has been accumulating since April.

Splitting the 17 by what the citation actually means:

- **1 is citation imprecision.** `MECH-057` is shorthand — `MECH-057a` and `MECH-057b` both exist.
  Correct the references, register nothing.
- **10 name nothing that exists**, and are one-per-id judgements: `SD-094` (16 mentions),
  `SD-085`, `MECH-315`, `MECH-310`, `MECH-311`, `Q-046`, `Q-047`, `SD-102`, `MECH-900`,
  `SD-MECH-267`. Some are probably typos; some may be real gaps. The audit's own instruction
  applies — *"Decide per id: register in claims.yaml, or correct the reference. Do not
  bulk-register."*
- **6 are governance rules that are operationally live.** This is the finding.

### The finding: a standing-scan family is half-registered

`scripts/check_skill_improvement_recurrence.py`'s own docstring enumerates the family. Measured
2026-09-01, every member has a script and every member is wired into `governance.sh`:

| rule | script | registered? |
|---|---|---|
| `GOV-CEIL-1` | `check_substrate_ceiling_audit.py` | **yes** |
| `GOV-DIAG-1` | `check_diagnostic_chain_recurrence.py` | **yes** |
| `GOV-GRAN-1` | `check_granularity_debt_recurrence.py` | no |
| `GOV-CAT-1` | `check_epistemic_category_completeness.py` | no |
| `GOV-SKILL-1` | `check_skill_improvement_recurrence.py` | no |
| `GOV-APPLY-1` | `check_unapplied_autopsy_recommendations.py` | no |
| `GOV-DRY-1` | `check_dry_run_adjudication_leak.py` | no |
| `GOV-SUBPATH-1` | `check_substrate_path_overlap.py` | no |

**Two of eight registered.** The other 34 `GOV-*` rules in the registry — including
`GOV-HELDOUT-1`, whose registration CLAUDE.md documents as the convention — show that a governance
rule is *supposed* to be a claim.

These six are not dormant proposals. They run every governance cycle, they gate real work, and they
are cited by id as authority 4–34 times each across CLAUDE.md, the skills and the planning corpus.
`GOV-APPLY-1` alone has 24 mentions spanning 2026-04-17 to 2026-09-01 and an entire section of the
`/governance` skill written around it.

**What being unregistered costs them.** An unregistered rule cannot accumulate evidence, cannot be
promoted or demoted, is invisible to any query over `claims.yaml`, cannot be cited by a
machine-readable `depends_on` edge, and never appears in the closure or assembly-state accounting.
Six live governance gates sit outside the epistemic machinery that governs everything else — while
being quoted as though they were inside it.

**Read the sequence and it looks like an oversight, not a decision.** `GOV-CEIL-1` (2026-07-09) and
`GOV-DIAG-1` were registered as they landed; the five later siblings were not, and `GOV-APPLY-1`
grew a standing scan, a skill section and two dozen citations without anyone noticing it had no
claim. Nothing in the corpus argues they should stay unregistered.

---

## What this changes

- **Do not** build a detector for stale-edge-implies-gap. Tested; the edges are residue.
- **Do not** build a prose-successor detector. Tested; one instance.
- **Do** treat the dangling claim-reference audit as the gap map. It already exists, already runs,
  and its top finding had gone unread for four months.
- **Register the six** (done in the same pass — see below). The other eleven stay per-id
  judgements, per the audit's own warning.
- **Fill `MECH-476.superseded_by`** with `MECH-459`/`MECH-460`. One field; the prose already says it.

## Registered in this pass

`GOV-APPLY-1`, `GOV-DRY-1`, `GOV-CAT-1`, `GOV-SUBPATH-1`, `GOV-GRAN-1`, `GOV-SKILL-1` — all as
`claim_type: governance_rule`, `epistemic_category: governance_rule`, `status: candidate`, matching
the `GOV-CEIL-1` template. Registration records what the rule already does; it asserts no new
policy and changes no scan's behaviour.

## Not done

The eleven other unregistered references, and the disposition of the 20 remaining stale edges
(`GFLAG-0064`, still open). Both need per-id judgement and neither is blocked on anything.
