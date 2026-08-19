# Steward -- preserved design of record

The documents in this directory are the **design of record** for the Steward
integrity skill, written 2026-08-15 and committed here 2026-08-17 by
`chip-20260816-steward-handover-design-docs-into-repo`.

| file | what it is |
|---|---|
| `SKILL.md` | The skill contract: thesis, the T0/T1/T2 tier model, the ratchet, the escalation budget, repair authority, the git lane, the escalation prompt contract. |
| `DETECTORS.md` | The 13-detector catalogue -- one entry per detector, each cited to a defect that actually occurred -- plus the seed suppressions and the build order. |
| `FIELD_NOTES_20260815_git_lane_reconcile.md` | The git lane executed by hand end-to-end across three repos. Empirical calibration for stages 2-3, and the only record of two still-unbuilt findings. |

## Why these were not already in the repo, and what that cost

They existed **only** at `/Users/dgolden/.ree_handover/20260815-steward-integrity-skill/`
on the Mac: not version-controlled, not backed up, not readable from any other
machine. When `chip-20260815-steward-stage1-detectors` was dispatched to
`ree-cloud-5` -- where `/Users/dgolden` is a symlink to the worker's own
`/home/ree` -- the path silently did not exist, and the stage-1 build had to
reconstruct the detector semantics from the adjudication commit `7478ffe8ad`, the
chip ledger's stored prompts, and `generate_closure_snapshot.py` itself.

That reconstruction worked -- D-002 reproduces the validated 4-finding output
exactly -- but it was avoidable rework and there was no reason to expect it to
keep working for the next detector. Two further chips
(`chip-20260815-steward-t0-autofix-git-lane`,
`chip-20260816-steward-d007-stale-gate-reference`) referenced `DETECTORS.md` by
name and were both dispatchable to a cloud worker.

## Why here and not `docs/architecture/`

Both were offered. `scripts/steward/docs/` wins on three counts:

1. **Drift visibility, which is the failure being fixed.** This chip exists
   partly *because* the catalogue and the implementation drifted -- two entries
   state the closure denominator incorrectly. Co-locating them means a session
   editing a detector has the catalogue in the same directory, `git log --
   scripts/steward/` shows both, and a spec correction and its code change land
   in one reviewable commit. Splitting them across the tree re-creates the exact
   gap.
2. **`docs/architecture/` is a different corpus.** Its 285 files are REE's
   scientific and system architecture -- brain maps, affect primitives, claim
   phase provenance -- and several scripts reference specific files there by
   name. Steward is *tooling*, and its design of record belongs beside
   `scripts/steward/README.md`, which is already the operational doc for the same
   subsystem.
3. **The readers are already here.** The consumers are the sessions that will
   build D-003 / D-005 / D-009 / D-103 or extend the git lane, and they start in
   `scripts/steward/`.

Cloud-worker reachability -- the actual defect -- is satisfied by either
location, so it did not decide it.

**Filenames are kept as `SKILL.md` / `DETECTORS.md` deliberately**, because
existing chip prompts cite them by those names and a prompt saying "see
DETECTORS.md" should resolve without a translation step. `SKILL.md` is a design
document, **not** an installed skill -- no `steward` skill is registered in
`.claude/skills/` or `.agents/skills/`.

## Relationship to `scripts/steward/README.md`

**`../README.md` is authoritative for what exists. These documents are
authoritative for what was intended.** Where they disagree, the README is
as-built and the difference is either a deliberate departure (each one is argued
there) or drift worth fixing. The `AS BUILT` blocks inserted into `DETECTORS.md`
mark the places where the original spec is actively *wrong* and would mislead a
reader building against it; everything else is left verbatim.

## As-built map (2026-08-17)

Stages 1-4 shipped over 2026-08-16: `971de87793` (stage 1, D-002/D-001/D-010),
`5ec8813d24` (stages 2+3, D-006/D-008 autofix + D-101/D-102 git lane),
`c131d538c1` (stage 4, D-007), `f4d43eb7e5` (wired into `governance.sh` as
Step 3m, warn-only).

| detector | catalogue says | built | note |
|---|---|---|---|
| D-001 `phase_generation_mismatch` | P1 T1 | **yes** | 27 findings; scoped, since the literal any-owner reading fires 63x |
| D-002 `orphan_v3_claim` | P0 T1 | **yes** | precision 4/4; predicate corrected -- see its `AS BUILT` block |
| D-003 `never_revisited_node` | P1 T1 | no | step 5 of the build order |
| D-004 `phantom_owner_exq` | ~~P0 T1~~ | **RETIRED, do not build** | both halves landed elsewhere (`4fa9f8199b`, REE_Working `67ce615f`); a second suppression state for one defect class is the failure that let V3-EXQ-631 recur |
| D-005 `crosslink_asymmetry` | P2 T1 | no | step 5; its seed suppression is forward-declared and inert |
| D-006 `duplicate_governance_flag` | P2 T0 | **yes** | annotates, never deletes -- departure argued in `../README.md` |
| D-007 `stale_gate_reference` | P1 T1 | **yes** | documentation-accuracy only, framing user-signed-off 2026-08-16 |
| D-008 `plan_frontmatter_date_drift` | P2 T0 | **yes** | 19 real fixes queued, deliberately not applied |
| D-009 `owed_successor` | P1 T1 | no | step 5 |
| D-010 `denominator_integrity` | P0 T0-assert | **yes** | assertion as specified was wrong -- see its `AS BUILT` block |
| D-101 `divergence_content_equivalence` | P1 T1 | **yes** | 4 per-commit classes as of `chip-20260817-steward-d101-superseded-upstream-verdict` -- see below |
| D-102 `moving_ref_guard` | P0 T0-assert | **yes** | |
| D-103 `untracked_research_artefact` | P2 T1 | no | step 5. Its two named artefacts are *still untracked on this tree* |

**Built: 8. Unbuilt: 4. Retired: 1.** The escalation/adjudication half of
`SKILL.md` -- the skill body a model loads on `escalate: true` -- is not built;
what exists is the deterministic detection half plus the T0 repair lane.

## Open items carried forward

Recorded here because these documents are their only home. **Nothing in this
preservation pass changed detector behaviour**, so all four were open as of
2026-08-17. Item 1 has since been built; see the resolution note under it.

1. ~~**`superseded_upstream`, D-101's missing fourth verdict**~~ **RESOLVED
   2026-08-19 by `chip-20260817-steward-d101-superseded-upstream-verdict`.**
   (`FIELD_NOTES` §1). As built on 2026-08-17, D-101 emitted three per-commit
   classes. The field notes recorded a real case the trichotomy mis-classified:
   a commit that is `upstream_by_patch_id` but whose file is *absent from
   origin's HEAD tree*, because origin later renamed and reframed it. Both
   naive readings were wrong, and reading it as `unique` means committing it --
   re-adding a document the project deliberately renamed away. Fixed by
   following rename history (`_gitlane.renamed_away_target()`: `git log
   --diff-filter=D --follow` to find the deleting commit, `git diff-tree -M
   --name-status` on it to confirm it was a rename rather than a genuine
   delete) before emitting a verdict, and routing the result to a new
   `superseded_upstream` class that contributes to `safe_to_adopt`, never
   `unique_work_present`. The same rename-follow also covers route A's false
   negatives (`FIELD_NOTES` §2) for a renamed path, not only a confirmed
   patch-id hit -- a commit whose content-equivalence probe leaves every
   missing path resolved as a rename is classified `superseded_upstream` too.
   Tests: `test_gitlane.py::test_patch_id_hit_whose_path_was_renamed_upstream_is_superseded`
   (the field-notes case, reproduced), plus a negative control
   (`test_missing_path_that_was_genuinely_deleted_is_not_superseded`) proving a
   plain delete does not get the same pass. `hook_activation_on_adopt` (item 2
   below) and the post-adopt `A ` skew repair gap (item 4 below) remain open --
   out of scope for this chip; item 4 in particular lives in
   `scripts/safe_adopt_ref.py` / `scripts/ree_commit.py`, not in this detector.
2. **`hook_activation_on_adopt` (P0), proposed and never catalogued**
   (`FIELD_NOTES` §8). Adopting origin materialised a file that *activated* a
   `PreToolUse` hook dormant only because its `[ -f ]` test was failing; the hook
   had no command matcher and blocked every Bash call in all 66 worktrees. The
   check is one deterministic diff -- files in the incoming range that are
   referenced by a `[ -f ]`/`[ -x ]`-gated hook in `.claude/settings.json` and do
   not exist locally -- and it converts a fleet-wide outage into a line of
   output. Note the general form is now partly covered by
   `scripts/audit_hook_gating.py` in the umbrella repo; check for overlap before
   building, per `SKILL.md`'s own do-not-duplicate rule.
3. **Emitted `tier` does not match the designed tier for D-001, D-002 and
   D-010.** All three take `finding()`'s default `tier="T2"` and never pass
   `tier=` explicitly, so their findings carry `T2` on the wire while both the
   catalogue and `../README.md` call D-001 and D-002 **T1**. The field is not
   inert -- D-007's `assert_no_status_proposal()` raises on `tier != "T1"`, and
   `finding()` refuses `autofix=True` outside `T0`. Left unchanged here: this is
   a documentation-preservation pass and correcting it is a behaviour change.
4. **Post-adopt skew repair is unspecified for `A `** (`FIELD_NOTES` §6). The
   spec stops at the adopt verdict, and all three repos needed manual repair
   afterwards. `A ` (staged add of a path absent from HEAD) cannot be repaired
   with `git checkout HEAD -- <p>` at all. The cheap discriminator that should
   run *first* -- `git show "HEAD:$p" | diff -q - "$p"` -- resolved 6 of 7
   flagged paths on ree-v3 instantly as pure index skew.

## What was deliberately NOT copied

The handover also held `detectors/d002_orphan_v3_claim.py`, a 227-line reference
implementation. It is **not** preserved here, because
`../detectors/d002_orphan_v3_claim.py` is its shipped descendant and carries the
substance forward -- the SD-031 origin, the 4/4 adjudication and its commit
`7478ffe8ad`, the named findings, the do-not-add-a-signal-gate rule and the
silent-misses asymmetry. Keeping a stale second copy of executable code beside
the real one invites exactly the drift this directory exists to prevent, and
CLAUDE.md's vendored-copy rules exist because byte-identity between copies is not
self-maintaining.

Two things in the prototype's docstring have no shipped equivalent and are
recorded here instead:

- **Why zero-owning-node claims are not flagged.** Most of the ~1000-claim
  registry has no closure node and never should; flagging that would drown the
  signal. The defect is specifically a claim that *is* owned, by nodes that are
  *all* deferred -- which reads as tracked while being excluded. (The shipped
  detector implements this; it counts them as `n_unowned` rather than arguing
  for it.)
- **The `--root PATH` escape hatch**, which made the prototype runnable against
  a throwaway worktree checked out at another ref. The shipped runner takes
  `--git-repo` for the git lane; a detector-side equivalent is what would let the
  historical replays run against an arbitrary base.

The original handover directory is left in place on the Mac and is now
redundant.
