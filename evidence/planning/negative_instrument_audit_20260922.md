# Negative-instrument audit: can "nothing found" be told apart from "the search broke"?

**Date:** 2026-09-22
**Session:** `audit-negative-instruments-20260922`
**Posture:** READ-ONLY audit. No tool was edited. One file written (this one).
**Verdict:** **The thesis HOLDS.** It is a class, not a cluster -- but the corpus is
**bimodal**, and the defect is concentrated in the **highest-level** instruments. One
guard was found **dead in production for 16 days**. See section 5.

---

## 1. The thesis under test

> A tool whose job is to establish a NEGATIVE is dangerous when its "nothing found"
> output is indistinguishable from its "the search was broken" output. A negative
> established with such an instrument is not established at all.

Negatives are load-bearing here. They authorise *starting* work ("no prior run covers
this"), *closing* work ("no orphans remain"), and *skipping* work ("intake is caught up").

The structural restatement that makes the class tractable:

> **Every negative instrument asserts a universally quantified claim over a set it
> discovered itself. It is only as good as its evidence that the set is the right set.
> The defect is that the instrument derives its denominator from the same search that
> produced its numerator -- so one failure destroys both, undetectably.**

Two faces, same class, **different remedies**:

- **The tool face.** A scan reports a count. Remedy: report a denominator measured
  *before* filtering.
- **The test face.** A suite asserts a property over a corpus. A green verdict carries no
  number at all, because `for x in []: assert P(x)` is *vacuously* true. Remedy is
  different in kind -- an **existential** added to the universal: assert the corpus is
  non-empty before asserting anything about it.

Recorded separately for that reason, not merged to lengthen the list.

### Two independent axes -- do not conflate them

A late counter-example forced a distinction this audit needs and did not start with.
**"Does the instrument run?" and "does the instrument distinguish a negative from a
non-answer?" are independent properties.** A tool can fail one while passing the other:

- **AVAILABILITY.** Does it execute at all, against the real corpus, today?
- **EPISTEMICS.** When it does run, does it have a structural **cannot-determine**
  category, or does it collapse "I checked and it is fine" into the same output as
  "I could not check this"?

`thought_intake_audit.py` is the proof that these are orthogonal: it was **catastrophically
unavailable** (18 days of `TypeError`) while having **the best epistemics in the corpus**
(section 3.1). Conversely, several tools below run flawlessly every day and have no
cannot-determine class at all. An audit that scores only one axis mis-ranks both.

Findings below are marked on whichever axis they fail; where a tool fails both, that is
stated.

---

## 2. Findings -- highest severity first

Method: four sweeps (one by hand, three parallel read-only subagents) over
`scripts/`, `REE_assembly/scripts/`, `ree-v3/`, and the governance pipeline. Broken-search
cases were **constructed and run** wherever the tool does not write; rows reasoned from
source are marked. `file:line` is the state at audit time.

### 2.1 A guard that has been dead in production for 16 days

| | |
|---|---|
| **Instrument** | `ree-v3/validate_queue.py` -- burned-queue-ID scan |
| **Negative relied on** | "this `V3-EXQ-*` id has not already run" |
| **Distinguishable?** | **NO -- and currently returning a permanent false negative** |
| **Evidence** | `_find_status_dir()` (`:610-621`) looks for the **directory** `REE_assembly/evidence/experiments/runner_status/`. That directory was deleted by REE_assembly `6320b7f3fad` ("R7: retire the frozen telemetry dirs", 2026-09-06). **Independently re-measured this session: `_find_status_dir() -> None`, `_scan_completed_queue_ids() -> 0 ids`.** `completed_scan` (`:1241`) is therefore always empty and the check at `:1525` **can never fire**. The fail-soft `return {}` at `:631` makes "no id collides" and "I scanned nothing" the same output. |
| **Why no test caught it** | **Every** test that touches the scan monkeypatches it to `lambda: {}` (`test_validate_queue_seed_enforcement.py:231,269`; `test_validate_queue_prereg_share_feasibility.py:234`). The suite is green on a guard whose real input no longer exists. **This is the test face and the tool face of the class stacked on the same guard.** |
| **Aggravating** | The surviving flat `runner_status.json` still carries 840 `completed` entries and a `_frozen` block asserting the per-machine split "IS still live" -- now false. `queue-validate.yml` (fresh clone, no REE_assembly sibling) never had this check at all. |
| **Authorises** | Re-queuing an already-completed id with `Queue OK`, then either the runner **silently skipping** it (the canonical EXQ-126 failure the guard was built for) or a **duplicate multi-hour fleet run**. `force_rerun` is now meaningless -- nothing it escapes from is running. |

This is the single most consequential finding of the audit, and it is not hypothetical.

### 2.2 The pipeline-level instance -- every clean verdict laundered

| | |
|---|---|
| **Instrument** | `REE_assembly/scripts/governance.sh` |
| **Distinguishable?** | **NO** |
| **Evidence** | `set -euo pipefail` at `:24`, then **24 audits invoked as `"$PYTHON" scripts/check_*.py \|\| true`**, then an unconditional closing `echo "Done."`. No exit code captured for any of them; no "N audits ran, N clean, N failed" roll-up. (Read, not run -- it writes.) |
| **Authorises** | An audit that dies on an ImportError after a module rename, a missing `jsonschema`, or a moved input produces no findings, and the cycle reports the same `Done.` as a fully clean run. **This converts every individual audit's clean verdict -- including the well-built ones in section 3 -- into an unverifiable negative.** |
| **The repo already knows the fix** | The steward step at `:672-679` captures `STEWARD_RC` and emits `ERROR: run_detectors.py exited N -- escalation state UNKNOWN`. **That pattern is applied at exactly 1 of 25 steps.** |

### 2.3 The governance worklist

| | |
|---|---|
| **Instrument** | `REE_assembly/scripts/generate_pending_review.py` |
| **Distinguishable?** | **NO** (for the *shrink* case; the *total-miss* case is well defended) |
| **Evidence** | Simulated against an empty index, the artifact body is **byte-identical** to a genuinely caught-up corpus: `Pending: **0** item(s) -- 0 PASS, 0 FAIL, 0 runner-only, 0 unclaimed, 0 ERROR` + `All experiments reviewed. Nothing pending.` Nowhere does it say how many index entries, reviewed run_ids, or on-disk manifests were considered. Total miss *is* caught (`:595` exits 1 when `claim_evidence.v1.json` is absent; `:100` warns on a missing tracker). |
| **Authorises** | The undetected case is an index regenerated in a **wedged or behind checkout** -- a documented recurring hazard. The file exists, parses, and is simply smaller, and every stderr warning stays silent. CLAUDE.md step 6 and `/governance` both treat this file as the worklist. So: closing a governance cycle with unreviewed FAILs, skipping `/failure-autopsy` on structurally invisible runs, and **promoting claims on confidence computed from a smaller evidence set than the operator believes**. |
| **Fix** | One line of arithmetic the script already has in hand -- print `entries_considered` / `reviewed` / `manifests_on_disk` alongside `Pending: 0`. |

### 2.4 The rest, ranked

| # | Instrument | Distinguishable? | Evidence | A false negative authorises |
|---|---|---|---|---|
| 4 | `scripts/check_autopsy_coverage.py` | **NO** | Three outputs **byte-identical in structure**, all exit 0: a typo'd `--scan-dir`, a wrong `--repo`, and a genuinely uncovered target all print `AVAILABLE: YES`. `build_coverage_index():139` `if rc != 0: return index` (empty); a wrong-but-valid scan dir makes `git ls-files` exit 0 with empty stdout. No corpus denominator in table **or** `--json` | A **duplicated multi-hour `/failure-autopsy`** plus duplicate TASK_CLAIMS on already-confirmed work. **Aggravated: this tool was written because the previous check produced this exact false negative on 2026-08-16, and it reproduces it through a different door** |
| 5 | `ree-v3/validate_experiments.py` | **NO** | 7 of 8 sampled lints return `None` (= clean) for a nonexistent path; only `check_script` fails closed. Measured: `--strict --quiet --checks manifest_writer --paths <bogus>` -> **exit 0**, `checked 1 scripts: 0 OK, 0 exempt, 0 non-conforming`. `_candidate_paths` (`:9174-9177`) resolves CWD-relative with **no existence check**. Adjacent: `--paths` with an **empty shell expansion** silently becomes a full 1504-driver run **with all four hard gates downgraded to advisory** (`bool(args.paths)`, `:9209-9226`) | Landing a driver with a missing arm fingerprint, a hand-rolled manifest write, or a use-before-def -- the V3-EXQ-591g repeat the file's own comment prices at **5h46m of lost cloud compute** |
| 6 | `ree-v3/scripts/precommit_contracts.sh` | **NO** | `STAGED=$(git ... 2>/dev/null \|\| true)` (`:325`) swallows the error. Every block is `[ -n "$STAGED_*" ]`-gated; Block 2 (the ~3560-test suite) exits at `:530-531`. **Every other degradation in this script prints "FALLING BACK"; an empty `STAGED` prints nothing.** Structural, not measured | A contract-breaking `ree_core/` change landing on `main` with **no contract run**, which the fleet then pulls and executes |
| 7 | `scripts/ref_move_guard.py::commits_discarded` | **NO by design** -- LIVE but LATENT | `if rc != 0: return []` (`:148-149`); docstring says "**fails OPEN**". Measured: honest -> `[(sha, author, subject)]`; unresolvable range -> `[]`. **Identical.** Consumed by the hook (clause 3, `:215-217`) **and** `safe_adopt_ref.py:345` **and** `ref_convergence.py:978`. Selftest `:313-321` **enforces** the sharing. **No test covers the `rc != 0` branch** | **An irreversible ref move discarding local commits** (A-72: no status-code signature; a live writer's next tick can erase the reflog trace). See the correction below |
| 8 | `generate_inter_governance_workset.py` + `check_workset_drift.py` | **NO**, and **correlated** | `_load_substrate_queue` (`:1832-1838`) and `_queue_from_worktree` (`:677-684`) both `return []` on missing **or unparseable**. Measured: real 235 entries, bogus path 0, **silently**. `check_workset_drift.py` exists as the "defense-in-depth sibling" so "a generator bug cannot hide itself" -- but it calls the **same loaders**, then prints `ready_items_flagged=0` / `None -- every ready item re-validates clean` | A retest surfaced `ready` whose substrate blocker is live -> a **queued multi-hour fleet experiment against a substrate that is not implemented**. `substrate_queue.json` is on CLAUDE.md's "Exposed files" list, so mid-write is realistic. **Both layers fail in the same direction at the same moment** |
| 9 | `audit_flat_only_orphaned_manifests.py` | **NO** | Two **verbatim-identical** outputs, exit 0 both: real root and `/nonexistent` root both print `no flat-only orphaned manifests found -- clean` | "No evidence is invisible to the indexer" while orphaned manifests carrying scoring-relevant `claim_ids` sit unscored |
| 10 | `REE_assembly/scripts/validate_literature.py --paths` | **PARTIAL** -- LIVE | Type-dir: `OK (0 records in scope)`, exit 0. Correct: `OK (12 records checked, 0 findings)`, exit 0. Denominator **is** printed; verdict word and exit code identical (`:521-522`). **`precommit_literature.sh:208` matches only `*"validate_literature: OK"*`**, so a zero-scope resolution passes the gate as clean | A whole literature pull validated as OK having checked nothing |
| 11 | Harness `grep` wrapper (ugrep `-I`) | **NO** -- LIVE | Fresh repro this session: file with one NUL byte; wrapper `grep -c findme_token` -> no output, exit 1. `/usr/bin/grep -c` -> `1`, exit 0 | Concluding a feature does not exist and **building it again** -- the confirmed 2026-08-12 outcome |
| 12 | `verify_governance_cycle.py` | **NO** | `:190`, `:465`, `:592-600` each `return` **silently** on a missing/unparseable input. Terminal summary prints block/warn/info counts, **never how many checks ran**. Read, not run | "Governance state is internally consistent" when 3+ checks never executed. Inherits 2.3 via `pending_review.md` |
| 13 | `scripts/audit_stashes.py` | **PARTIAL** | Clean human-mode run prints **literally nothing** (1 char). A bad path **is** loud (`SKIP (not a git repo)`), and `--json` names every repo. But `parse_entries():497` `if rc != 0 or not out.strip(): return []` -- a failed `git stash list` in a **valid** repo reads as "no stashes" | Closing a session with work stranded in an autostash entry. CLAUDE.md: "**a loss check, not hygiene**"; a failed pop reaches the owner as **no error** |
| 14 | 2 zero-pinned corpus lints lacking the floor | **YES (vacuous)** | `test_spearman_guard_shape_lint.py:352-360` and `test_ceiling_route_anchor_floor.py:214-220` -- bare `assert X == []` with **no** `_MIN_CORPUS_FILES_FOR_A_MEANINGFUL_PIN`. Both written in a different idiom, which is why the guard sweep missed them | A hand-rolled defective Spearman helper, or a ceiling-route driver missing the anchor floor, reappearing unseen. **Fix is one `assert` each** |
| 15 | `test_thought_intake_audit.py::MainEndToEndTests` | **NO** -- **FIXED** | `thoughts_root.mkdir()` (`:433`) **never populated**; Stage-1 corpus empty; **31 tests green throughout** | 18 days of believing a ground-truth check existed. **The vacuity was PARTIAL, which is why it survived** -- Stage 2 genuinely passed |
| 16 | `reanalysis_query.py` | **NO** -> **FIXED mid-audit** | Pre-fix: `rows` reassigned post-filter (`:180`), printed as `scanned %d` (`:224`). Post-fix (`76b116678bc`, on origin): `scanned 1061 manifests ..., 0 matched` | Queueing a full experiment instead of a recorded reanalysis (GOV-REUSE-1) |
| 17 | `thought_intake_audit.py` | **AVAILABILITY: failed** (crashed) -> FIXED. **EPISTEMICS: best in corpus** | `TypeError`, unrunnable ~18 days. Fixed `e84bfcf535c`, on origin. But its classifier has a structural cannot-determine class -- see 3.1 | Believing intake is caught up while the ground-truth check does not run. **The counter-example that forced the two-axis split**: this tool fails the availability axis and passes the epistemic axis better than anything else audited |
| 18 | `ree_commit.py::summarize_json_delta` | **NO**, self-aware | Returns `[]` on five broken conditions (`:1917-1931`) and on genuine no-change | Missing a read-modify-write sweep. **Low** -- doctrine says "a signal to read, not a gate". `MAX_SUMMARY_BYTES` = 20 MB; `TASK_CHIPS.json` is already 13.9 MB (70%) -- a **size-correlated blind spot arriving silently** |

Also noted, lower severity: `audit_dangling_citations.py` prints denominators and SKIP
reasons but its **final line still says `clean`** when zero checks ran;
`audit_orphan_chips.py:247` prints `no findings across %d bucket(s)` where the number is a
constant 8 regardless of chips scanned; `audit_shared_checkout_conflicts.py:246`
`if rc != 0: return []` audits zero worktrees with no total-count line;
`audit_stale_claims.py:932` silently drops a claim with a malformed `claimed_at`.

### Correction to finding 7 -- stated so it is not overread

`safe_adopt_ref.py` asserts `cur_branch == branch` (`:290`), **dies** on fetch failure
(`:322-324`) and **dies** if the target is unresolvable (`:328-330`). Both ends of the
range resolve in practice on the wrapper path; the likely broken-search routes **are
closed**. So the finding is sharper than "the wrapper is open":

> **The wrapper's safety comes from ad-hoc pre-checks, not from its predicate.**

**And the real defect is not fail-open -- it is a POSTURE MISMATCH under composition.**
`commits_discarded` is *correctly* fail-open for the git hook (CLAUDE.md: "blocks
narrowly, on purpose -- a guard that fires on ordinary work gets disabled") and
*incorrectly* fail-open for `safe_adopt_ref.py`, whose job is to **refuse**. One function
cannot serve both postures with one return convention. The anti-drift argument that locked
them together is sound about the *predicate* and silently wrong about the *posture*. Fix:
return `None` for "could not compute" and `[]` for "nothing discarded"; the hook maps both
to allow, the wrapper maps `None` to refuse. No drift, no new mechanism.

### A finding I got WRONG, and the correction

I initially recorded that `ree-v3`'s CI holds an **unguarded** duplicate of the six
`PYTEST_ROOTS` (`contract-tests.yml:291`), drifting freely from
`remote_pytest.sh --selftest`. **That is false.**
`tests/contracts/test_ci_workflow_test_roots.py` parses the workflow's `PYTEST_ROOTS` and
asserts `roots` is non-empty (`:74`) **and** that every collectable test file is covered by
them **and** that the enumeration itself is non-vacuous (`:115`:
`assert files, "enumeration found no test files at all -- the sweep is broken"`). The
duplicate **is** guarded, by an in-suite twin of the positive control. Recorded because an
audit that does not publish its own false positives is itself a weak instrument.

---

## 3. What the corpus does RIGHT -- and the remedy hierarchy

This is not a corpus that lacks the discipline. It applies it unevenly. Three remedies
were found in use here, and they are **not equivalent** -- they form a hierarchy, strongest
first.

### 3.1 BEST: an explicit cannot-determine CATEGORY (structural)

**`thought_intake_audit.py` is the reference implementation, and it is a genuine
counter-example to a lazy reading of this audit: a tool can be catastrophically
*unavailable* while having the best *epistemics* in the corpus.**

Its Stage-2 classifier emits five outcomes, and keeps **two "cannot determine
mechanically" classes structurally separate** from the failure classes:

```
orphan_classes    = {fully_orphaned, partially_registered, not_registered_no_ids}
needs_read_classes = {no_ids_named, partially_unlabeled}      # <- never folded in
```

That separation is maintained at four independent call sites (`:314-315`, `:347-348`,
`:462-463`, and the report writer at `:385-408`), and surfaces as a distinct
`stage2_needs_read` count reported **alongside** `stage2_orphaned`, never inside it.

The reasoning is written into the source (`:270-283`) and is the best statement of this
audit's thesis found anywhere in the repo:

> a flat section-wide scan cannot tell "every candidate in this list has a registered ID"
> apart from "one candidate incidentally cites an unrelated registered ID while its
> siblings carry no ID at all".

Confirmed 2026-08-07/09 on `thought_intake_2026-04-16_language_lateralisation.md`: three
prose-only candidates, none with an ID of its own, but the **third**'s aside ("overlaps
ARC-009") made the whole section read as `all_registered`. The fix was to split into
per-candidate items and check each independently rather than trusting the flat verdict.

**Why a category beats a printed number:** a category is part of the data model, so it
survives refactoring, propagates into `--json` consumers, and cannot be silently dropped by
someone tidying output. A print statement is a courtesy that the next edit can remove
without any test noticing.

**A qualification this same file supplies, which corrects advice I would otherwise have
given.** I was ready to recommend "declared manifests beat discovered sets" without
reservation. This tool shows the limit: its claim-ID regex originally used a **hardcoded**
prefix list (`ARC|MECH|INV|Q|SD`), and when `GOV-` prefixes were registered, a
fully-registered file misclassified (`:76-90`). **A declared set goes stale independently
of the thing it describes.** The fix was to derive the prefix set from the same
`claims.yaml` the caller already loaded -- *declared from a source that cannot go stale
separately*. Note also the failure direction: the misclassification landed in
`no_ids_named` (cannot-determine), **not** in `all_registered`. A correct cannot-determine
class absorbs its own bugs safely.

**One real usability defect, worth recording because it was observed live.** The name
`stage2_needs_read` reads as a *human-work backlog* rather than as *the tool declining to
certify 52 files mechanically*. It was misread that way twice by a consumer of this audit,
within one day. That is a **different and much milder defect** than the one under audit --
the epistemics are correct, only the label invites the wrong inference -- but a category
that is right and named misleadingly still transmits a false negative to the human. Suggest
`stage2_undetermined` or `stage2_not_mechanically_checkable`.

### 3.2 STRONG: the known-baseline CANARY

**Strictly better than a denominator, for a reason worth stating.** `check_duplicate_queue_id_execution.py` and
`check_run_id_letter_hygiene.py` each pin a list of findings that **must keep
reproducing**. Verified: repointing `EVIDENCE_DIR` at `/nonexistent` produced
`Baseline entrie(s) no longer reproducing -- update KNOWN_DUPLICATE_QUEUE_IDS in this
script: V3-EXQ-542a, ... (22 ids)` and **exit 1**. A denominator detects a *totally*
broken search; **a canary detects a PARTIALLY broken one** -- the far more common and far
harder case.

### 3.3 ADEQUATE: a pre-filter denominator, printed

The weakest of the three, and the one this audit started out recommending. It works, it is
cheap, and it is the right fix where the instrument has no natural cannot-determine state
(`generate_pending_review.py`, `reanalysis_query.py`'s landed fix). But it is a print
statement, not a contract.

### 3.4 Other correct implementations, with the property that makes each work

- `remote_pytest.sh --selftest` (`:834-897`) -- four-part guard: forward check (declared
  paths exist), converse enumeration (every collectable file reachable), **explicit
  vacuity line** (`:890-893`: "found no test files at all ... it would pass vacuously"),
  and **the denominator printed on success** (`:895`). Its design note (`:799-822`) states
  the generalisable rule: enumerate the tree, do not pin the names known on the day of the
  fix.
- `session_startup_checklist.py::run_json` (`:55-66`) -- **two-channel** `(data, err)`;
  every caller checks `if err:` (`:124, :296, :325, :379`). A sub-tool crash is reported as
  an error, never folded into "nothing found".
- `audit_unqueued_experiment_scripts.py` -- the reference implementation in its family:
  pre-filter `checked: 1521 script(s)`, an explicit `TOOL FAILURE` for a missing dir, a
  separate "degraded input, **not** a tool failure" section, and **over**-reporting on a
  broken corpus (the safe direction).
- `check_worker_work_landed.py` -- the only tool carrying an explicit `degraded_routes`
  channel and printing `** DEGRADED -- this verdict is NOT exhaustive **` rather than
  letting a timeout masquerade as a clean negative.
- `audit_vendored_copies.py` -- checks against `VENDOR_SETS`, a **declared** manifest.
  `build_experiment_indexes.py` -- skew-guard **refuses to write** and exits non-zero.
  `check_unapplied_autopsy_recommendations.py` -- `coverage: N of M`, plus an explicit
  `NOTE: ... unreadable` line. `test_dv_headroom_statistic_mismatch.py:364-410` -- the best
  denominator *inflation* hygiene in the tree (committed-only filter **plus** a regression
  test that drops an untracked specimen into `experiments/` and asserts the pin holds).
- The corpus-lint family states its own policy correctly at
  `test_hardcoded_dry_run_lint.py:438-446`: **only zero-pinned gates need a non-vacuity
  floor, because a nonzero pin fails loudly on an empty walk.** Eight tests carry
  `_MIN_CORPUS_FILES_FOR_A_MEANINGFUL_PIN`, with a global `n_glob_files > 500` backstop at
  `test_corpus_scan_sharing.py:356`. Only the two in finding 14 were missed.
- **The class has been met and fixed corpus-wide before.** `chip_ledger.archived_field()`
  exists because a raw `chip.get(field)` reads an archived chip as "never had one" --
  silently, and precisely for the oldest chips. Adopted at 5+ sites with explicit "never
  `.get()`" comments.

Measured coverage of the non-vacuity idiom: `ree-v3/tests/` 101/397 files (25%);
`scripts/test_*.py` 58/260 (22%); `REE_assembly/scripts/` 30. **I expected the discipline
to be concentrated in the science-facing tests and absent from the coordination plane.
That hypothesis is FALSE** -- the rates are comparable.

---

## 4. Where the class stops -- the boundary

1. **Positives-only instruments are out of scope.** A tool whose callers never conclude
   "therefore nothing exists" is not in the class.
2. **Advisory negatives the doctrine already discounts sit at very low severity**
   (finding 18).
3. **Fail-open by design is NOT a defect where fail-open is correct.** A blocking git hook
   that wedges the fleet is worse than one that occasionally misses. The defect appears
   only under **composition** with a fail-closed caller (finding 7). Likewise
   `validate_queue._is_tracked` fails open deliberately and says so, and
   `check_experiment_queue_floor.py` **names its fail-open in the output**
   (`treating as NOT starved (fail-open)`) -- which is the correct way to ship one.
4. **Silent-when-clean is a deliberate noise-budget choice** (A-25 reasons it out for the
   worktree-skills banner). This yields the sharpest operational rule the audit produced:

   > **Silent-when-clean is RIGHT for a hygiene check and WRONG for a loss check.**

   CLAUDE.md itself classifies `audit_stashes.py` as "a loss check, not hygiene", which
   settles finding 13 on the project's own terms.
5. **A correct category that is NAMED misleadingly is a different and much milder
   defect.** `stage2_needs_read` (section 3.1) has the right epistemics and the wrong
   label -- it transmits a false inference to the human without the instrument being
   wrong. Worth fixing, but it is a usability defect, not an instance of this class. Do
   not let the class absorb it; that is how a sharp finding becomes a vague one.
6. **An UNAVAILABLE tool is not automatically an instance either.** A tool that crashes
   loudly has *no* output to confuse -- the defect is that nobody was running it, which is
   a monitoring gap. It becomes an instance of this class only when the absence of its
   output is read as a clean verdict by something downstream (which is exactly what
   happened at CLAUDE.md step 6a, and why finding 17 counts).

---

## 5. Verdict on the thesis

**The thesis HOLDS, and more strongly than the four motivating instances suggested.**
Eighteen instruments, most confirmed by constructed broken-search cases rather than source
reading, spanning tools, test fixtures, a shell pipeline, a pre-commit gate, and the shell
harness itself. **One guard is dead in production right now and has been for 16 days.**

**But the corpus is BIMODAL, and that is the decision-relevant shape.** It contains some of
the best negative-instrument engineering I would expect to see anywhere -- the
known-baseline canary, the `--selftest` reachability sweep, two-channel returns, an
explicit `degraded_routes` channel -- alongside top-level instruments with no denominator
at all. **The failure is not missing knowledge. It is inconsistent application, and it is
concentrated at the TOP of the call graph**: `governance.sh` (the pipeline driver),
`generate_pending_review.py` (the worklist), `validate_queue.py`'s primary guard. The
well-built audits underneath them have their clean verdicts laundered into an unverifiable
`Done.`

**On the selection effect, directly.** The concern that "instances found by people looking
for them is weaker evidence than it feels" is correct and worth answering rather than
arguing around:

- The *original* four were found by **four independent routes** (a GOV-REUSE-1 reuse
  check, a crash, a literature pull, a surprising grep) -- not one sweep. Independent
  discovery is much stronger evidence of a real class than a directed search.
- The sweep findings were produced by **four searchers working from the same thesis**,
  which is exactly the correlated-evidence problem. I have weighted them accordingly: the
  ranking below is by *consequence*, and the two headline findings (2.1, 2.2) were each
  **independently re-measured by hand** before publication.
- The strongest evidence that this is a real class and not pattern-matching is
  **finding 4**: a tool written *specifically because* its predecessor produced this exact
  false negative, which reproduces it through a different door. That is recurrence under
  deliberate remediation.

**On the two axes.** Scoring availability and epistemics separately changes the picture
in a way worth stating plainly: the corpus is *worse* on epistemics than a count of
outright-broken tools suggests, and *better* on the tools that have thought about it at
all. Most instruments here are perfectly available and have no cannot-determine state
whatsoever -- they run daily and cannot say "I don't know". That is the actual shape of
the problem, and it is invisible to any check that only asks whether a tool runs.

**Recommendation -- and this changed twice during the audit.** Do not build a general
detector: it would itself be a negative instrument scanning a tree, subject to the very
defect it hunts, and at ~25% existing non-vacuity coverage it would fire constantly on
correct code, which is the documented way a guard gets disabled.

**Instead, apply the strongest remedy each instrument can carry** (section 3):

1. **An explicit cannot-determine category** where the instrument has a natural "I could
   not check this" state -- structural, survives refactoring, propagates to `--json`.
   Precedent: `thought_intake_audit.py`.
2. **A known-baseline canary** where a stable set of findings must keep reproducing --
   catches *partial* breakage, which nothing else here does. Precedent:
   `check_duplicate_queue_id_execution.py`.
3. **A printed pre-filter denominator** as the floor, where neither of the above fits.

All three already exist in this codebase. This is porting working local practice across a
boundary, not inventing a mechanism.

---

## 6. Ranked shortlist -- what to fix first, by severity

1. **`validate_queue.py`'s dead burned-queue-ID scan (2.1) -- LIVE, MEASURED, FIX TODAY.**
   Not a latent risk: the guard returns a false negative on every invocation right now, and
   the tests cannot see it because they all mock the scan. Repoint `_find_status_dir()` at
   the surviving flat `runner_status.json`, **and** make an unresolvable status source a
   loud failure rather than `return {}`, **and** drop one test that exercises the real
   resolver unmocked.
2. **`governance.sh`'s 24 unchecked `|| true` (2.2).** Highest leverage per line changed:
   it is what makes every *other* audit's clean verdict trustworthy. The correct pattern is
   already in the file at `:672-679` -- apply it to the other 24 steps and print an
   audits-ran/clean/failed tally before `Done.`
3. **`generate_pending_review.py`'s bare zero (2.3).** This is the promotion gate. One line
   of arithmetic it already has in hand.
4. **`check_autopsy_coverage.py` (finding 4).** Recurrence under deliberate remediation.
   The right fix here is **remedy 1, not remedy 3**: `AVAILABLE` should be a three-valued
   field (`YES` / `NO` / `UNDETERMINED -- corpus empty or scan dir unresolvable`), not a
   boolean with a count printed beside it. `audit_unqueued_experiment_scripts.py`'s
   `TOOL FAILURE` for a missing dir is the availability half; the cannot-determine class is
   the epistemic half, and a valid-but-wrong `--scan-dir` needs the latter.
5. **`validate_experiments.py`'s unreadable-path green (finding 5)** -- particularly the
   empty-`--paths`-expansion case that silently downgrades four hard gates while looking
   like a strict run. Note this interacts with the documented shell-portability hazard:
   a silently-empty path list is exactly the failure CLAUDE.md warns about.
6. **The two unguarded zero-pins (finding 14)** -- one `assert` each; the policy is already
   written down in the same directory.

**Below the line:** finding 7 is a sentinel return (small, high consequence, low
likelihood). Finding 10's gate-matching bug (`precommit_literature.sh:208`) is a one-line
pattern change. Finding 13 is settled by the project's own hygiene-vs-loss classification.
Finding 18 needs a tracked threshold, not a fix. Findings 15-17 landed on origin during
this audit.

---

## 7. Provenance and what was NOT done

- **No tool was edited by this session.** Findings 15-17 were repaired by **sibling
  sessions**, verified on `origin/master` (`76b116678bc`, `e84bfcf535c`).
- `governance.sh`, `verify_governance_cycle.py`, `check_workset_drift.py`,
  `check_closure_drift.py`, and the other writing scripts were **read, not run**, and their
  rows are marked.
- The `ree-v3` pytest suite was **not** run (it must not run on the Mac). One accidental
  full-corpus `validate_experiments.py` invocation was killed at ~120s.
- **One incidental write to report:** `check_citation_staleness.py` turned out to write
  `evidence/planning/citation_staleness.md` and was run. The diff is two lines (`Generated:`
  timestamp, `Citations checked: 326 -> 337`); **no finding changed** (`stale=0 missing=2
  ambiguous=0` before and after). It was left uncommitted and un-reverted, since reverting
  is itself a write and `evidence/planning/` already carried several concurrent sessions'
  dirty files. Flagged rather than raced, per CLAUDE.md's narrow-edits scoping rule.
- Scratch under `/Users/dgolden/REE_Working/.scratch/`, never `/tmp`.
