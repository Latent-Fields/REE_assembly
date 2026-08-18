# Orphaned untracked evidence triage -- 2026-08-13/14 items

- **Status:** investigation COMPLETE and landed; **execution BLOCKED on machine** (`DLAPTOP` only)
- **Written:** 2026-08-18T05:49Z, session `metaworker-chip-20260817-orphaned-untracked-evidence-triage`
- **Chip:** `chip-20260817-orphaned-untracked-evidence-triage` (left OPEN -- see "What is left")
- **Ran on:** `ree-cloud-5` (headless metaworker dispatch). Base for all origin-side facts:
  `REE_assembly` `origin/master` `fefd2c5de2` (fetched 2026-08-18T05:47Z).

---

## Why this document exists rather than a commit landing the files

The three files named in the chip **do not exist on `ree-cloud-5`.** They are uncommitted
working-tree files in the **Mac's** (`DLAPTOP`) shared `REE_assembly` checkout, and they were
found there by the `ree-evening-sync` session of 2026-08-17T17:47Z, which ran on that box
(`WORKSPACE_STATE.md`, that entry: "this box IS the owner, `DLAPTOP`"). An uncommitted file has
no git object, so there is no route by which a cloud worker can read it.

Verified, not assumed:

```
$ ls REE_assembly/evidence/literature/targeted_review_connectome_sd_005/entries/2026-08-13_*/
ls: No such file or directory
$ ls REE_assembly/evidence/literature/targeted_review_ethological_play_signals/record.json
ls: No such file or directory
$ ls REE_assembly/evidence/planning/q093_dimensionality_dynamics_discussion_2026-08-13.md
ls: No such file or directory
$ git status --porcelain -- <all three>      # no output: not untracked here either, simply absent
```

(`/Users/dgolden` on this box is a compat symlink to `/home/ree`, so the Mac-shaped paths in the
chip prompt resolve to this same absent checkout. That is worth knowing before someone re-reads
the prompt and concludes the paths were merely mistyped.)

The land/remove decision needs the **bytes** -- schema validity, whether `summary.md` is complete,
whether the q093 doc is a draft or finished. Everything that could be established *without* the
bytes is below, so the `DLAPTOP` session that picks this up starts from the byte-level check only.

---

## The chip's premise is inverted, and this is the substantive finding

The chip brief reasoned: *"if (1) and (2) are complete literature entries, their evidence is not
reaching the indexer, so every claim they test is under-counted."*

**For item (1) the opposite is true.** Its evidence is already fully counted in the committed,
pushed derived artifacts on `origin/master`, while its source of record exists on exactly one
laptop, untracked.

Three committed artifacts on `origin/master` cite it:

| artifact | how it appears |
|---|---|
| `evidence/literature/INDEX.md` (line 170) | markdown links to `.../record.json` and `.../summary.md` -- **both resolve to nothing in the repo** |
| `evidence/experiments/claim_evidence.v1.json` | a full evidence row under **both** `SD-005` and `ARC-010`; `latest_run_id` for both |
| `evidence/experiments/conflicts.md` (line 108) | named as `SD-005`'s `latest_run_id` (row: 11 / 13 / 0.917 / 30) |

Provenance: all three were written by **`3d8de8f990`** -- *"governance regen: derive-only pipeline
output (cycle 2026-08-16)"*, author `nooarche`, 2026-08-16 12:28:32 +0100, 59 files. The indexer
globs the **working tree** (`build_experiment_indexes.py:1779`,
`literature_root.glob("**/entries/**/record.json")`), so on the Mac it reads the untracked file
and bakes it into artifacts that are then committed. The source never is.

Note this happened **after** the 2026-08-16T06:22Z `/lit-pull` session had deliberately excluded
the same file and verified byte-identity both ways ("no foreign content is baked into the
committed derived artifacts"). That statement was true of *that* session's commit and was
overtaken by the governance regen six hours later. Two sessions, opposite dispositions, neither
wrong about its own commit.

### Full sweep: this is the only case

Cross-referencing every `record.json` / `summary.md` path cited in the committed `INDEX.md`
against `git ls-tree -r origin/master -- evidence/literature/`:

```
cited paths: 888    tracked lit files: 4532
DANGLING (cited in committed INDEX.md, absent from origin/master): 2
    .../2026-08-13_sd005_arc010_dynamic_population_coding_chatzimichail2026/record.json
    .../2026-08-13_sd005_arc010_dynamic_population_coding_chatzimichail2026/summary.md
```

Both belong to this one entry. **1 dangling entry out of 888 cited** -- isolated, not systemic.

### Why it matters concretely

`SD-005` (`literature_confidence` 0.873) and `ARC-010` (0.619) each carry a live evidence row at
confidence **0.74**, `evidence_direction: mixed`, with a 90-word `confidence_rationale` and three
`failure_signatures`. If the Mac's working tree ever loses that file -- a `git clean`, a worktree
reap, a disk event -- the source behind two claims' confidence has **no recovery path**, while
the derived artifacts go on asserting it. The defect is also **self-perpetuating**: every future
regen *on the Mac* re-reads the file from disk and re-emits the citation, so it will not age out.

Partial reconstruction survives in `claim_evidence.v1.json` (confidence, rationale, evidence_class,
evidence_direction, failure_signatures, timestamp `2026-08-13T22:45:00Z`). What is **not**
recoverable from it: the whole `source` object (title, authors, year, venue, doi/url), the
`claim_ids_tested` shape, and all 8657 bytes of `summary.md`.

---

## Per-item adjudication

Each is adjudicated separately, as the chip required. "Verified" = established from `origin/master`
on this box. "Needs bytes" = requires the file, i.e. `DLAPTOP`.

### (1) `targeted_review_connectome_sd_005/entries/2026-08-13_sd005_arc010_dynamic_population_coding_chatzimichail2026/`
`record.json` (4931 b) + `summary.md` (8657 b), mtime 2026-08-13 23:37/23:40.

**Recommendation: COMPLETE, then LAND. Do not land as-is; do not delete.**

- *Verified:* it has a known **schema failure** -- `data_code_url` inside the `source` object,
  which is `additionalProperties: false`. Two independent prior sessions found this
  (`WORKSPACE_STATE.md` 2026-08-16T06:22Z and 2026-08-17T06:06Z) and both excluded the file for it.
- *Verified:* `data_code_url` appears in **zero** tracked records corpus-wide
  (`git grep -l data_code_url origin/master -- evidence/literature/` -> empty), so it is a
  one-off spelling, not an unratified convention. The 2026-08-14 schema-widening work
  (`f9a5ea65c0`) deliberately declined to admit the open-science link cluster
  (`code_repository`/`code_url`/`zenodo`/...) precisely because it was n=1-2 across three
  spellings; `data_code_url` is a fourth. **Do not widen the schema for this one record.**
- *Verified:* sibling shape in the same review --
  top-level `claim_ids_tested, confidence, confidence_components, confidence_rationale, entry_id,
  evidence_class, evidence_direction, literature_type, mapping, schema_version, source,
  summary_path, tags, timestamp_utc`; `source` = `authors, doi, title, url, venue, year`.
- *Verified:* it is genuinely absent from `origin/master` -- the `sd_005` review dir on origin
  contains only 4 entries, all from March 2026, and the review has no root `summary.md`.
- *Needs bytes:* confirm `data_code_url` is the **only** violation; confirm `summary.md` is
  complete prose and not a stub; confirm `summary_path` is present (28 corpus records are missing
  that key per the 2026-08-14 audit, so it is a live defect class).
- **Fix:** move the Zenodo link out of `source` (the rationale already records "a Zenodo code/data
  deposit", so the information is not lost by relocating it to `summary.md` or a top-level field),
  re-validate against a sibling, land `record.json` + `summary.md` together. The derived-artifact
  citations then resolve with **no regen needed** -- they already point at these exact paths.

### (2) `targeted_review_ethological_play_signals/record.json`
No adjacent `summary.md`; mtime 2026-08-14 15:04.

**Recommendation: it is MISPLACED, not half-written. Relocate under `entries/<slug>/` or delete.
Do not land it where it sits.**

- *Verified:* the convention question the chip asked is **settled, and it is not record-only.**
  All 8 committed entries in this review are `entries/<slug>/{record.json, summary.md}` --
  **8 of 8 have a `summary.md`**. There is no root-level `record.json` on origin; the review dir
  holds exactly `entries/` and `summary.md`.
- *Verified:* the indexer glob is `**/entries/**/record.json`
  (`build_experiment_indexes.py:1779`). A file at the review **root** has no `entries/` segment,
  so **it is never ingested** -- it contributes nothing to any claim today and never has.
  This independently reconfirms the finding already recorded at `WORKSPACE_STATE.md`
  2026-08-14T02:48Z ("sits OUTSIDE any `entries/` dir, so the indexer's glob never ingests it"),
  which is the same file, found four days ago and left unowned.
- *Needs bytes:* read it and decide which it is -- (a) a real entry saved to the wrong path, which
  wants an `entries/<slug>/` dir **and** a `summary.md` written before landing; or (b) a scratch
  or aborted write, which is a plain delete. Its own `entry_id` / `source` fields answer this
  immediately.
- **Note it is contentless for governance either way** -- unlike item (1), nothing downstream
  currently depends on it, so this one is genuinely low-stakes.

### (3) `evidence/planning/q093_dimensionality_dynamics_discussion_2026-08-13.md`
mtime 2026-08-13 23:43.

**Recommendation: LAND if it is finished prose; otherwise report per remedy (b). Do not delete.**

- *Verified:* nothing named `q093` exists anywhere on `origin/master`
  (`git ls-tree -r --name-only origin/master | grep -i q093` -> empty).
- *Verified:* `Q-093` is a real registered claim -- intook 2026-08-12T02:55Z, landed
  `REE_assembly` `50f8cb6263`, described as "REE control-machinery scaling vs. represented-world
  richness, `substrate_conditional` on a matched-competence baseline that doesn't exist yet".
  So the doc has a live subject; it is not orphaned scaffolding.
- *Verified:* it is a **planning discussion doc, not indexed evidence** -- `evidence/planning/*.md`
  is not read by `build_experiment_indexes.py`. So unlike item (1) there is no
  derived-artifact coupling and no under- or over-counting either way.
- *Needs bytes:* is it finished? Its mtime (23:43) is 3 minutes after item (1)'s `summary.md`
  (23:40), which suggests one `/lit-pull`-adjacent session wrote both back to back and then
  simply never committed anything -- consistent with item (1) failing schema validation and the
  session stopping there. That is a hypothesis from timestamps, **not** established; no
  `WORKSPACE_STATE.md` entry from 2026-08-13/14 explains the omission (searched; the only
  mentions of these files are the three later sessions that found them lying there).

---

## What is left, and who can do it

**Everything remaining requires the files, therefore requires `DLAPTOP`.** Concretely, for a
session on that box:

1. Read all three. For item (1) confirm `data_code_url` is the only schema violation, fix it, and
   land `record.json` + `summary.md`.
2. For item (2) decide relocate-vs-delete from its own contents.
3. For item (3) land it if finished; if half-written, **stop on that item and report it**
   (CLAUDE.md read-modify-write remedy (b)) rather than landing or deleting.
4. Commit with `ree_commit.py --repo REE_assembly`, naming paths explicitly. **No regen is needed
   for item (1)** -- the committed derived artifacts already cite exactly those paths, so landing
   the source *repairs* them in place. Re-running the indexer would be a ~1100-file regen for a
   citation that is already correct, which "Narrow Edits Only" forbids.

The chip `chip-20260817-orphaned-untracked-evidence-triage` is therefore left **OPEN** and
unclaimed. It must be re-dispatched on `DLAPTOP`; a cloud metaworker cannot complete it, and
re-dispatching it to `ree-cloud-5` will reproduce this exact outcome.

---

## Follow-on recorded separately

`chip-20260818-lit-index-dangling-citation-audit` -- a standing check that every source path cited
in the committed derived artifacts is actually tracked. Nothing audits this today, which is why the
gap sat open for 5 days and was found only by a session looking at something else. The sweep is
~15 lines and its yield **today is exactly 1 finding** (stated so the value is not oversold), but
that one finding is a claim-weighting evidence row with no source of record.
