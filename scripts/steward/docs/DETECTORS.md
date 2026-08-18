# Steward detector catalogue

> **PRESERVED DESIGN DOCUMENT.** Verbatim from
> `/Users/dgolden/.ree_handover/20260815-steward-integrity-skill/DETECTORS.md`
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
> **Read the `AS BUILT` blocks.** Two entries below (D-002, D-010) state the
> closure denominator incorrectly, and running the detectors is what found it.
> The blocks are inserted in place rather than rewriting the original text,
> because the original wording is the spec that the corrections are corrections
> *to*. A full as-built map -- which of the 13 are built, which are unbuilt,
> which is retired -- is in `docs/README.md`.

Every detector below is derived from a defect that **actually occurred** in
this repo, with the incident cited. No speculative checks — a detector with no
incident behind it has no measured precision and will burn escalation budget.

Contract for all detectors:

- pure file reads; no network, no model, no writes outside `state/`
- exit `0` clean, `1` findings, `2` detector error (never conflate 1 and 2)
- emit JSONL to stdout, one finding per line
- `finding_id = sha1(detector_id + stable_key)` — **stable across runs**, so
  suppressions hold and recurrence is measurable
- runtime budget < 2s each

```json
{"detector_id":"D-002","finding_id":"...","severity":"P0","tier":"T1",
 "title":"...","artefacts":[{"path":"...","line":35293,"reading":"..."}],
 "evidence":"<=40 lines","autofix":false,"confidence":0.9}
```

---

## Map integrity

### D-001 · `phase_generation_mismatch` · P1 · T1
A claim's `implementation_phase` disagrees with the `generation` of the plan
that owns its closure node (plan-level `generation`, defaulting to `v3`).

*Incident:* SD-031 — `implementation_phase: v3` owned by a node in a plan whose
only home for it was flagged V4. **Detects the SD-031 class directly.**

#### Cycle-1 adjudication — 2026-08-18 · **verdict `refine`** · **DEMOTED TO LIST-ONLY**

All 27 findings on base `b3b95d7938` adjudicated per claim:
**3 confirmed, 24 false positive → precision 3/27 = 0.11**, below the 0.6 floor.
Under the most generous defensible reading (also counting SD-036 and MECH-286,
which have live V3 experiments, as real denominator holes) it is 5/27 = 0.19 —
still well below. Demoted to list-only via `LIST_ONLY_ESCALATE` in
`detectors/d001_phase_generation_mismatch.py`: every finding is still
**reported**, none consumes escalation budget.

The floor is appropriate here for the reason SKILL.md gives, and the brief for
this adjudication independently reached it: **D-001's misses are not silent.**
An unowned v3 claim still appears in the registry. That is the opposite of
D-002, whose orphans are invisible by construction — which is why D-002 escalates
unconditionally and this one does not.

**Correction to a premise worth recording**, because it changes how the finding
set reads: D-001 does **not** fire on claims with no closure node. The detector
opens with `if not owners: continue`. Every one of the 27 *is* owned — just never
by a `generation: v3` plan. The population is therefore far sharper than
"unowned v3 claims", and the dominant failure mode is not absence of a plan but
**deliberate cross-generation ownership**.

| verdict | n | class |
|---|---|---|
| confirmed | 3 | ARC-053, ARC-054 (`deferred_by_commitment:DEF-1`), MECH-270 (`DEF-2`) |
| false positive | 13 | clinical lane, cross-generation **by construction** |
| false positive | 2 | owning node's own text explicitly refutes it (MECH-163, MECH-308) |
| false positive | 9 | forward-roadmap back-pointer (incl. the pre-suppressed MECH-099) |

**The 3 confirmed are a half-finished reassignment**, and two independent signals
agree. The co-listed siblings were moved and these were not — ARC-055 and
MECH-225/226/228 now read `implementation_phase: v4`, while ARC-053/054/270 still
read `v3`. And both node notes name the drift outright: DEF-1 says *"NOTE
phase-tag drift: ARC-053/ARC-054 currently read implementation_phase: v3 …
reconcile in the held-reassignment batch"*, DEF-2 *"MECH-270 currently reads
implementation_phase: v3 (drift, same note as DEF-1)"*. That batch never ran.
The fix is a claims.yaml edit → **proposed to /governance**, not applied:
`evidence/planning/d001_adjudication_staged_20260818.md`. Neither is suppressed.

**Why the predicate was not tightened instead.** A sharper structural rule was
*measured*, not assumed: fire only when a sibling claim co-listed in the same
owning node has already been reassigned off v3 ("partial reconcile"). That cuts
**27 → 9**, keeps all 3 confirmed, and drops all 13 clinical plus MECH-163 and
MECH-308 — but precision only reaches **3/9 = 0.33**, still under the floor,
because inside a v4 plan most co-listed claims are v4 anyway. Tightening past
that means fitting the predicate to the same 3 cases it would be validated on,
which `GOV-HELDOUT-1` exists to forbid. The disposition therefore lives in
`state/suppressions.yaml` — per-claim, reasoned, reversible — and the detector
keeps honest recall.

**No plan frontmatter was edited and no closure number moved**, so no A/B
regeneration of `generate_closure_snapshot.py` was required. Every false
positive resolved to "the existing arrangement is correct", and the confirmed
three are claims.yaml work outside this adjudication's authority.

*Resume condition:* restore escalation once governance dispositions the three,
**and** one full cycle has run with the suppressions live, **if** the
unsuppressed residue then measures ≥ 0.6. One constant to flip.

### D-002 · `orphan_v3_claim` · P0 · T1
A claim with `implementation_phase: v3` / `v3_pending: true` whose **only**
owning closure node has a status in `DEFERRED_STATUSES` — therefore excluded
from the V3 progress denominator and invisible to closure accounting.

*Incident:* SD-031, hidden ten weeks. This is the highest-value detector in the
set: the failure mode is silence, so nothing else surfaces it. Reference
implementation in `detectors/d002_orphan_v3_claim.py`.

> **AS BUILT (2026-08-16) -- the wording above is wrong in one load-bearing
> way, and the correction is the whole reason D-010 exists.** "a status in
> `DEFERRED_STATUSES` -- therefore excluded from the V3 progress denominator"
> conflates two different sets. `generate_closure_snapshot.py` excludes a node
> when `STATUS_WEIGHTS[status] is None`, which is a **strict superset** of
> `DEFERRED_STATUSES`, also holding `assembling`, `open_by_design`, `parked`,
> `parked_indefinite`, `closed` and `deferred_v5`. On the 2026-08-16 tree the
> real denominator is `117 v3 nodes - 13 deferred - 10 assembling = 94`,
> matching the committed snapshot; the `DEFERRED_STATUSES`-only reading above
> predicts **104**.
>
> **D-002 as built therefore keys on `deferred` specifically, NOT on "excluded
> from the denominator"** -- even though the accounting harm is identical.
> Widening the predicate to the full exclusion set added exactly three claims
> (ARC-108, MECH-450, SD-033b), all owned by `assembling` nodes and none
> orphaned: pure false positives against `assembling`, the anti-forcing status
> that exists so unhurried assembly is not scored as failure. Diluting the one
> detector whose precision is its entire value is the worst possible trade. The
> wider surface is real and belongs to **D-010**, which reports it as a surface
> rather than as per-claim defects.
>
> Concretely: `_common.DEFERRED_STATUSES` is `{"deferred", "deferred_v4"}`. The
> prototype's set additionally held `deferred_v5` and a space-spelled
> `"deferred v4"`; `deferred_v5` moved out to D-010's exclusion table.

**Pilot result (2026-08-15, local pre-reconcile tree, 0.31s):** recovered
SD-031 — the known true positive — and surfaced **four further instances of the
same class that nobody had found**:

| Claim | Owning deferred node | Signal |
|---|---|---|
| SD-031 | `self_attribution:GAP-5` | strong (known true positive ✓) |
| MECH-316 | `arc_062_rule_apprehension:GAP-I-absorption` | strong |
| MECH-317 | `arc_062_rule_apprehension:GAP-I-absorption` | strong |
| MECH-091 | `commitment_closure:GAP-7` | weak |
| MECH-314a | `behavioral_diversity_isolation:GAP-G` | weak |

**Ratchet cycle 1 — `refine`, applied then REVERTED.** The original trigger
(`implementation_phase == v3 OR v3_pending`) was narrowed to escalate only on
`v3_pending: true`, demoting `MECH-091` (no `v3_pending` key) and `MECH-314a`
(`v3_pending: False`, `provisional`) to list-only. Claimed precision 0.6 → 1.0.

**Ratchet cycle 2 — that refinement was wrong; gate removed.** Adjudication
(`chip-20260815-orphan-v3-claims-adjudicate`, landed `REE_assembly 7478ffe8ad`)
returned **precision 4/4 via three distinct mechanisms** — including both
findings cycle 1 had demoted:

| Claim | Verdict | Mechanism |
|---|---|---|
| MECH-316 / MECH-317 | node **wrong**, un-defer | 4 of 5 artefacts say live V3 |
| MECH-314a | node **stale**, un-defer | provisional, `v3_pending` lifted after a PASS, 8 manifests; falsifier ran 17d *after* the node's `last_updated` |
| MECH-091 | **undetermined** | needs the generation of SD-006 phase 2 settled first (zero `substrate_queue` entries) |

Closure delta, measured A/B: **71.9% / 94 nodes → 70.0% / 97**. Status changes
and a conditional `claims.yaml` correction were *proposed* to `/governance`,
not applied — so the detector still reports all four until governance acts.

Two corrections worth carrying forward:

1. **`signal` is ranking metadata, never a gate.** `escalate` is unconditional
   for this detector. When the runner's budget is contended, `severity` and
   `signal` decide ordering; they must not withhold a finding. Cycle 1's gate
   would have withheld MECH-314a — a real stale node — indefinitely.
2. **Gate on cost asymmetry, not on precision.** This detector's failure mode
   is *silence*: an orphaned claim is invisible by construction, which is how
   SD-031 survived ten weeks inside an actively-worked plan. A miss costs
   months of a distorted closure figure; a false positive cost one session ~20
   minutes. Precision floors (SKILL.md) are the right instrument for detectors
   whose findings are *noisy*, not for detectors whose misses are *silent*.

Also refuted: the prediction that `GAP-I-absorption` would resolve the inverse
way (correct the claims, not the node). It did not — the node was wrong. The
catalogue entry had flagged this as an open question rather than asserting it,
which is what let the adjudication go where the artefacts pointed.

### D-003 · `never_revisited_node` · P1 · T1
A non-`done` node carrying no `governance_*` key and no `last_updated` movement
since the plan's `registered` date.

*Incident:* GAP-5 was the only node in `self_attribution` never revisited since
2026-05-08 — which is precisely why the rescope never reached it. This detector
finds the *structural condition* that lets stale tags hide, before they cause
harm. Expect low precision initially (deferred nodes are legitimately quiet);
run list-only until tuned.

### D-004 · `phantom_owner_exq` · ~~P0 · T1~~ · **RETIRED 2026-08-16, do not build**

Originally specified for the V3-EXQ-631 / 483f / 445i / 816e / 732b incident,
where 631 *recurred* after a partial 2026-07-21 fix that repointed only the
MECH-342 rows while `commitment_closure:GAP-4` still named it.

**Both halves have since landed elsewhere, and Steward must not duplicate them:**

- the one-time prose fix — `chip-20260815-phantom-ownerexq-plan-prose`, done,
  `REE_assembly 4fa9f8199b`. Note it found **three** dispositions, not the two
  this entry originally specified: phantom-duplicate (631 → 629/629b),
  pre-allocated placeholder (483f), and deliberately-refused (445i, 816e, 732b).
- the recurrence fix — `chip-20260815-morningdigest-7c-declared-notowed`, done,
  `REE_Working 67ce615f`. Step 7c of the morning digest now exempts positively
  *declared* retired ids, adjacency-scoped (a file-level rule would have
  false-skipped the correct 631 finding, whose declaration sat on the MECH-342
  rows while GAP-4 still read DEFERRED), forward-only, with a held-out check.

**Why building it anyway would be actively harmful, not merely wasteful.** Two
systems detecting one defect class hold *separate suppression state*. A finding
declared not-owed in Step 7c but unsuppressed in Steward — or the reverse —
reproduces precisely the failure that let 631 recur: a partial fix reading as
complete because the other half of the system never heard about it. Divergent
suppression is worse than no suppression, because it is silent.

**General rule this yields (see SKILL.md):** before building a detector, check
whether an existing check already owns the defect class. Steward's job is to
cover what nothing covers, and to make suppression durable where coverage
exists — not to re-detect in parallel.

*If D-004 is ever revived*, the surviving design note worth keeping is the
false-positive trap: 631 and 483f both produce `git log -S` hits, and every one
is a reference inside another entry's title or note field, never a queue entry.
Presence-in-text is not provenance.

### D-005 · `crosslink_asymmetry` · P2 · T1
`A.cross_plan_link` names B, but neither B nor B's plan points back.

*Incident:* GAP-5 ↔ `self_model_v4:SELF-2` — both successors pointed at the
self-attribution plan and nothing pointed forward, so the V3 → V4 → V5 hand-off
never rendered as map edges. **Seed suppression required — see below.**

### D-006 · `duplicate_governance_flag` · P2 · **T0 (auto-fix)**
Entries in `governance_flags.v1.json` identical on `(claim_ids, flag_type,
date)`.

*Incident:* MECH-449 / ARC-107 raised twice locally (4 occurrences vs origin's
2) from a repeated commit. Mechanical dedup, no judgement.

### D-007 · `stale_gate_reference` · P1 · T1
A node's `blocking_external` or `resume_condition` names a gate `plan:NODE`
whose status is now `done`.

*Incident:* this happened **twice** in `self_attribution`. The 2026-06-09
re-adjudication found the MECH-269 gate had been satisfiable *the day after it
was written* and stayed stale ~3 weeks; the 2026-07-29 reconcile found two of
three named gates had since cleared. High value, because a stale gate makes
blocked work look correctly blocked.

**FRAMING — user-signed-off 2026-08-16. This is a constraint, not a default.**

D-007 is a *documentation-accuracy* detector, never an *unblock-detection*
one. It reports **"the gate text is stale"** and is forbidden from concluding
**"the node should be open."**

*Cleared gate ≠ unblocked node.* Every recorded instance in this repo ended
with the node correctly staying `blocked` on a **re-pointed** gate:

| Date | Gate that cleared | Why the node stayed blocked |
|---|---|---|
| 2026-06-09 | MECH-269 satisfied 2026-05-17 (SP-CEM main-path default, V3-EXQ-583) — *one day after the gate was written* | 543l/598b/614e: candidate pool collapses at z_world **upstream** of SP-CEM, so stratified sampling has nothing to stratify |
| 2026-06-23 | `behavioral_diversity_isolation:GAP-A` → `done` (569i PASS) | V3-EXQ-625e autopsy: conversion is ENV-CONDITIONAL, does not propagate to a threat-engaged candidate pool |
| 2026-07-29 | `sleep_substrate:GAP-1` and `goal_pipeline:GAP-1` both `done` | node stayed blocked on a re-pointed third gate |

A detector emitting "node should open" would have been wrong all three times,
and the cost is not noise: the plan states that re-queuing on a falsely-cleared
gate re-derives a known `non_contributory` result and burns a runner session.
The plan names "GAP-A done → unblock GAP-2" explicitly as *the trap the axis_b
autopsy caught*.

**Two severity tiers** (the signed-off refinement — ranking only, both still
report stale text and neither asserts a status change):

- **P2** — *some* named gates cleared, others outstanding.
- **P1** — *all* named gates cleared. Higher signal: the node's stated
  rationale is now entirely vacuous, so the re-adjudication is overdue. Still
  not a conclusion that it should open.

**Implementation consequences that follow from the framing:**

- Permanently **T1**. Never auto-fix — re-pointing a gate is the judgement.
- Suppression keys on `(node, gate-set)`. A node adjudicated "still blocked,
  gate re-pointed" must not re-fire every run, but **must** re-fire when the
  gate set changes.
- **A precision floor DOES apply here**, unlike D-002. D-007's misses are not
  silent — stale plans already surface in the morning digest's staleness
  table. This is the SKILL.md asymmetry rule discriminating between two
  detectors rather than applying one policy to both.

*Value, given the constraint:* it only fixes prose, which can read as low
value. The 2026-07-29 reconcile is the counter-evidence — stale gate text made
three nodes read as *"blocked on three unmet gates, nobody assigned"*, and they
sat 60 days on that reading. The value is forcing a re-adjudication without
pre-empting its answer.

### D-008 · `plan_frontmatter_date_drift` · P2 · **T0 (auto-fix)**
Plan-level `last_updated` older than `max(node.last_updated)`.

*Incident:* `self_attribution` frontmatter read 2026-06-04 while its rows were
reconciled 2026-07-29 — inflating the "72d stale" figure in the morning digest
and sending attention to a plan that had in fact been touched. Cheap fix,
directly improves digest signal quality.

### D-009 · `owed_successor` · P1 · T1
The digest's four-check provenance walk over every EXQ referenced by an
open/blocked node, automated.

*Incident:* run by hand on 2026-08-15 over 205 ids. Four looked owed and all
four resolved to superseding runs. Pure mechanical work, currently costing a
human pass per digest.

### D-010 · `denominator_integrity` · P0 · T0-assert
Assert the closure denominator equals exactly
`{nodes | status ∉ DEFERRED_STATUSES ∧ plan.generation == 'v3'}`, recomputed
independently of `generate_closure_snapshot.py`.

*Rationale:* D-002 exists because the denominator silently dropped a claim.
This guards the accounting itself rather than its inputs. Fails loud.

> **AS BUILT (2026-08-16) -- the assertion as written above is the bug it was
> meant to catch.** The real rule is `STATUS_WEIGHTS[status] is not None`, not
> `status not in DEFERRED_STATUSES`; the two differ by `assembling`,
> `open_by_design`, `parked`, `parked_indefinite`, `closed`, `deferred_v5`, and
> on the 2026-08-16 tree that is the difference between the correct **94** and a
> predicted 104. D-010 implements the real rule, reproduces the committed
> snapshot exactly (117 v3 nodes, denominator 94, status tally matching
> `closure_status.md` line for line, zero weight drift against `serve.py`), and
> reports the silent-exclusion surface -- 10 `assembling` nodes on that tree --
> as its standing output rather than as a defect. Emitted `tier` is `T2`, not
> `T0-assert`. See D-002 above and `README.md` -> "Two corrections to the
> stage-1 spec".

#### Cycle-1 adjudication — 2026-08-18 · **verdict `refine`** · both standing findings

Both of D-010's standing findings adjudicated on base `e0c9901eac`
(`origin/master`). **1 confirmed, 1 false positive. No suppression was added**, and
that is the substantive finding rather than an omission — see below.

| finding | verdict | disposition |
|---|---|---|
| `silent_exclusion_surface` (10 `assembling` nodes) | **false positive** | check now *measures* the label it was asserting |
| `snapshot_denominator_mismatch` (94 vs 95) | **confirmed — regen lag** | check now discriminates lag from rule divergence |

**Check 2 was asserting a property it never measured.** Its detail read "the
exclusion is unlabelled", and for `assembling` that has not been true since the
snapshot grew its Assembly-frontier block. `closure_status.md` states it two lines
under the percentage — *"Assembly frontier (required, under construction — a
SEPARATE axis, not counted in the % above and not a stalled backlog): **10**
nodes"* — and again as a dedicated section listing all ten. The finding was
correct that the *general* surface is where the next SD-031 comes from; it was
wrong that this instance is on it.

**Why a suppression was rejected, and this is the load-bearing part.** The brief
required that any suppression be keyed so it re-fires should a NON-`assembling`
status ever start leaving the denominator. **`subject` was a constant**
(`silent_exclusion_surface`), and the suppression key is `<detector>:<subject>`
— so *no* suppression narrow enough to be honest was writable. Any entry that
silenced today's finding would equally silence `parked`, `parked_indefinite`,
`closed`, `deferred_v5` and `open_by_design`, every one of which really would be
excluded with nothing said about it. That is the blanket the brief forbade, and
it is a blanket over the exact defect class this detector exists for.

So the **identity was refined instead**, following D-007's `(node, gate-set)`
precedent: the subject now carries the status set
(`silent_exclusion_surface@statuses=parked`), and `EXCLUSION_LABELS` maps an
excluded status to the marker text the snapshot uses. A status counts as labelled
only when that marker is present in the **Overall** block *and* the count it
states matches. Absent marker, renamed marker, stale count, label further down
the file, or an unreadable snapshot all read as **unlabelled** — the failure
direction is loud. Labelled exclusions do not vanish from the report along with
the finding; they are carried in the detector summary as `labelled_exclusions`.

`EXCLUSION_LABELS` deliberately maps `assembling` **and** `open_by_design` to one
marker, because `generate_closure_snapshot.ASSEMBLING_STATUSES` reports them as a
single number; the count is checked against their sum. Splitting them would have
fired spuriously the first time an `open_by_design` node appeared.

**Check 5 was confirmed, and it is regen lag — proved, not assumed.** It does not
reproduce on the `ree-cloud-5` shared checkout at all (`[behind 187]`, where
94 == 94); on `origin/master` the committed snapshot says **94 / 71.9%** and the
recomputation says **95**. A clean `generate_closure_snapshot.py` run moved the
snapshot to **95 / 72.3%**, which settles it.

**The snapshot discriminates itself, exactly, with no dates and no git.** It
commits its own per-status tally, and that tally separates two failures with
opposite urgency that the old single finding_id conflated:

- tally **differs** from the recomputation → different *inputs* → **regen lag**.
  `lag=explained`, P2, `escalate: false`. Self-heals at `governance.sh` Step
  3c-bis. The specific statuses that moved are named
  (`blocked 11→12; deferred 13→12; done 62→63; open 8→7`).
- tally **identical** but denominator differs → same inputs, different *answer* →
  the denominator **rule** has diverged from the producer. `lag=unexplained`, P1,
  `escalate: true`. Regenerating will not fix it. This is the accounting
  breaking, and under the old flat P2 it was buried behind the common case.
- no parseable tally line → `lag=unknown`, P1, `escalate: true`. Undecidable is
  treated as the loud branch on purpose.

A date-based discriminator (snapshot `Generated:` vs newest plan `last_updated`)
was considered and dropped: `D-008` exists precisely because those date bumps are
often skipped, so it would have called real lag "unexplained" routinely. The
tally is exact.

**Nothing outside `scripts/steward/` was touched.** The stale snapshot was *not*
regenerated and committed here — `evidence/planning/` is governance's, and the
pipeline rebuilds it at Step 3c-bis. No plan frontmatter, no `claims.yaml`, no
closure number moved.

*Tests:* `test_d010_denominator_integrity.py`, 18, time-independent, synthetic
trees. Nine are **negative controls** asserting the checks still fire — label
absent, label renamed, stale count, label outside the Overall block, absent
snapshot, a new unlabelled status arriving beside a labelled one, identical
tally, unparseable tally — because both halves of this refinement make the
detector emit *less*, and a bug in either would silence the guard on the closure
accounting without any symptom.

*Resume condition:* re-measure at cycle 2. Check 2 firing for a status other than
`assembling`/`open_by_design` is the ratchet working, not a regression. A
`lag=unexplained` is a P1 that regeneration will not clear.

---

## Git lane

### D-101 · `divergence_content_equivalence` · P1 · T1
On ahead/behind divergence, classify each ahead commit:
`upstream_by_patch_id` (via `git cherry`) / `upstream_by_content` (probe key
identifiers in the origin blobs) / `unique`. Emit
`safe_to_adopt` | `needs_rebase` | `unique_work_present`.

*Incident:* "272 commits behind, cannot fast-forward" blocked the digest and
read as dangerous. Manual analysis showed 28 already upstream by patch-id, the
substantive remainder present on origin by content, and the rest regenerable
automation churn — plus a *duplicate* flag entry that adopting origin would
clean up. That analysis took ~15 tool calls and should be one script.

### D-102 · `moving_ref_guard` · P0 · T0-assert
Record `origin/*` SHAs and timestamps at detection time; re-read before any
action; abort if moved.

*Incident:* `origin/master` advanced three times mid-session (05:05, 05:08,
05:38 UTC). An equivalence check run before the 05:38 fetch reported "identical"
for a file that had been substantially rewritten. **A verified-then-stale check
is more dangerous than no check**, because it is trusted.

### D-103 · `untracked_research_artefact` · P2 · T1
Untracked files under `evidence/` matching research-record shapes (literature
entry dirs, `*_discussion_*.md`, `*_audit_*.md`) — real records at risk of loss
in any tree operation.

*Incident:* a `targeted_review_connectome_sd_005` entry and a Q-093 discussion
doc sitting untracked during a pending reconciliation.

---

## Seed suppressions

Pre-loaded so the first run does not escalate three known non-defects.

> **AS BUILT (2026-08-16) -- two of these three are FORWARD-DECLARED and match
> nothing.** They were seeded inert because no stage-1 detector emits a node- or
> experiment-subject finding, and they are kept so the *disposition* is not lost
> when an owning detector lands. Live copies with their current status are in
> `state/suppressions.yaml`; that file is authoritative.
>
> | seed | owner | live? |
> |---|---|---|
> | `D-001:MECH-099` | D-001, **built** | **LIVE** -- suppresses a real finding every run |
> | `*:multi_agent_ecology_v5:MAE-3` (D-005 whole-plan back-pointer) | D-005, **not built** | **FORWARD-DECLARED, inert.** D-007 now emits node subjects, so the "waiting for a node-level detector" condition is met -- but a D-007 subject carries a `@cleared=...;named=...` suffix and this pattern has no trailing wildcard, so it still matches nothing. Left deliberately unwidened: the recorded disposition is about a back-POINTER, and a stale *gate* on MAE-3 is a different question that should escalate on its own merits. |
> | `*:V3-EXQ-732b` (deliberate refusal) | D-004, **RETIRED** | **FORWARD-DECLARED, inert with no owner pending.** Its intended owner was retired rather than built, so this is no longer "waiting" -- it is orphaned. Kept because the underlying disposition (732b was refused on purpose, not omitted) stays true. |
>
> Keeping this table honest is not optional housekeeping: a stale
> "becomes live when X lands" left standing after X has landed **is** stale gate
> text, i.e. the exact defect class D-007 detects. The Steward's own config is
> in scope for its own rules.

```yaml
- finding_id: D-005:multi_agent_ecology_v5:MAE-3->self_attribution
  reason: >
    MAE-3's cross_plan_link is a whole-PLAN back-pointer, documented by
    check_closure_links.py as a sanctioned intentional pattern, not a dangling
    node id. Adjudicated 2026-08-15 and explicitly marked "do not fix" after
    the forward edges were added on the self_attribution side.
  permanent: true

- finding_id: D-004:ree_ai_design_critique:WS-1:V3-EXQ-732b
  reason: >
    732b was a DELIBERATELY REFUSED experiment (competence-floor observability
    confound). The prose reference is correct history, not a phantom id.
  permanent: true

- finding_id: D-001:MECH-099
  reason: >
    implementation_phase v3 while sitting in the v5 MAE-3 node. Noted and left
    unadjudicated 2026-08-15: it is a multi_agent_ecology_v5 question, and that
    plan's generation:v5 already holds it out of the V3 percentage, so nothing
    is mis-counted today.
  resume_condition: >
    Re-escalate if MAE-3 gains an owner_exq, or if MECH-099 is pulled into a
    V3 plan node.
```

---

## Build order

Sequenced by value-per-hour, not by id.

> **AS BUILT (2026-08-16): stages 1-4 all shipped, in this order, and the volume
> prediction for step 4 did not hold.** D-007 was sequenced last as "the highest
> escalation volume" detector and produced **3** findings against D-001's 27 and
> D-008's 19, running in under 10ms -- the `plan:NODE`-only resolution and the
> citation veto keep it narrow. If a later revision loosens either, expect the
> prediction to start being right, and re-measure precision before it does.
> Step 5 (**D-003, D-005, D-009, D-103**) is **not built**.

1. **D-002, D-001, D-010** — the SD-031 class plus the guard on the accounting.
   These three justify the whole skill on their own.
2. **D-006, D-008** — T0 auto-fixes, immediate digest-quality improvement for
   almost no work.
3. **D-101, D-102** — the git lane; would have saved most of one session.
4. **D-007 only** — highest judgement content, so highest escalation volume.
   Land it once the ledger has enough records to tune escalation ranking, and
   only with the signed-off framing constraint written into the build brief.
   **D-004 is retired — see its entry. Do not build it.**
5. **D-003, D-005, D-009, D-103** — long tail; run list-only until precision is
   measured.

Do not build all of them before running any of them. The ledger from stage 1 is
what tells you whether the escalation budget and ranking are set correctly, and
that calibration should happen on three detectors rather than thirteen.
