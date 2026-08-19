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

---

# EXECUTION COMPLETE -- 2026-08-19T12:39:04Z (DLAPTOP)

Session `metaworker-chip-20260817-orphaned-untracked-evidence-triage` on `DLAPTOP`, the box
that holds the files. The investigation above was correct on every point it could establish
without the bytes; the byte-level checks it deferred are resolved below. **One finding above is
now superseded by events -- see item (1).**

Landing commit: `REE_assembly` **`8c693d770f`** (pushed to `origin/master`).

## (1) Chatzimichail 2026 entry -- COMPLETED AND LANDED

`data_code_url` was confirmed to be the **only** schema violation, by running
`scripts/validate_literature.py` against the record rather than reasoning from the schema
(1 finding before, `OK (1 records checked, 0 findings)` after). `summary.md` is complete
80-line prose, not a stub, and `summary_path` is present and resolves.

The fix needed no relocation work: **`summary.md` line 14 already carries
`- Data/code: \`https://doi.org/10.5281/zenodo.18983284\``** under `## Source`, which is
exactly where the schema's own description directs such content. Deleting the key from
`record.json` therefore loses nothing. Both files landed together.

### Superseded: the citations were no longer dangling -- they were GONE

The investigation above found this entry cited by three committed derived artifacts whose
source did not exist in the repo, and concluded its evidence was "already fully counted". As of
`origin/master` today that is **no longer true in either direction**: `chatzimichail` appears
in **no** derived artifact at all. It was removed by **`baa449053c`** ("lit-pull: quarantine
repair GFLAG-0027/0028/0029, MECH-054 gap fill GFLAG-0031", **REE Cloud Worker**,
2026-08-18 21:29Z), which rebuilt `INDEX.md` and the derived artifacts from a **cloud**
checkout -- a box where the untracked Mac file does not exist, so the indexer's working-tree
glob simply did not see it. That commit's message enumerates its four deliberate actions; this
entry is not among them, so the removal was an unintended side-effect, not a quarantine.

**The real defect is therefore worse than "dangling citation", and this is the durable
finding: the evidence row's presence was oscillating with whichever machine last ran the
regen.** A Mac regen (`3d8de8f990`) read the untracked file off disk and emitted the row; a
cloud regen (`baa449053c`) could not see it and dropped it. Between those two commits, SD-005
and ARC-010 each silently lost a literature evidence row at confidence 0.74
(`evidence_direction: mixed`, 3 failure signatures) with no failure, no warning, and no
reviewable diff attributable to a decision. Landing the source ends the oscillation.

**No regen was run here**, per CLAUDE.md "Narrow Edits Only" -- reinstating one evidence row
does not justify a ~1100-file rebuild. The next governance cycle's regen restores it from the
now-tracked source, and will do so identically on any box.

## (2) `targeted_review_ethological_play_signals/record.json` -- DELETED

The recommendation above ("misplaced entry; relocate under `entries/<slug>/` or delete") was
formed without the bytes and its premise does not survive them: **this is not an entry record
at all.** It has no `source`, no `confidence`, no `entry_id`. It is a **review-level
manifest** -- `review_id`, `review_description`, `search_terms_used`, `entries_count`,
`entries[]`, `overall_verdict`, `key_findings_for_arc049`, `missing_evidence` -- describing
the whole 8-entry May 2026 review. So relocating it under `entries/<slug>/` was never an
option; there is no entry for it to be.

Deleted rather than landed, on four independent grounds:

1. **It is a strictly information-poorer duplicate of committed prose.** The adjacent
   `summary.md` (tracked, clean, 7117 b) carries the same content in richer form, verified
   section by section: `review_description` -> `## Overview` + goal; `overall_verdict` +
   all 6 `key_findings_for_arc049` -> `## Summary Verdict`'s 6 numbered points;
   `entries[]` (8 bare ids) -> `## Entries` (the same 8 **plus** source and confidence per
   entry); all 4 `missing_evidence` bullets -> `## Missing Evidence` **verbatim**; all 14
   `search_terms_used` -> `## Search Terms Used`. Nothing in the JSON is absent from the
   prose.
2. **It matches no convention.** Zero of **449** review directories on `origin/master` have a
   root-level `record.json`, and `review_id` appears in **zero** tracked records corpus-wide.
3. **It has zero consumers and always has.** `build_experiment_indexes._scan_literature`
   globs `**/entries/**/record.json`; a file at the review root has no `entries/` segment.
   Confirmed by running that glob: not reachable. It has never contributed to any claim.
4. **It could not be landed as-is.** Despite declaring `"schema_version":
   "literature_evidence/v1"` it fails that schema in both directions -- **7 missing required
   keys** (`entry_id`, `source`, `evidence_class`, `evidence_direction`, `confidence`,
   `confidence_rationale`, `summary_path`) and **8 undeclared keys** against a top-level
   `additionalProperties: false`.

Its full content is preserved verbatim in the appendix below, so this deletion is reversible
from git history despite the file itself having had no git object.

## (3) `q093_dimensionality_dynamics_discussion_2026-08-13.md` -- LANDED

**Finished, not half-written**, so remedy (b) was not triggered. It runs 80 lines through a
complete arc (`## Why This Was Not Filed As Strong Evidence` -> `## Does It Help REE?` ->
`## What It Adds` / `## What It Challenges` / `## What It Does Not Prove` -> `## REE
Discussion Verdict`) and closes on a deliberate terminal disposition -- "No claim status
change. No new claim registered. This is a discussion note attached to the `Q-093` research
thread." It carries `nav_exclude: true` front matter and full citation provenance.

Its subject is not redundant: Wang & Fan 2025 (*Patterns* 6(8):101231) is cited **nowhere** on
`origin/master`, checked by both DOI (`10.1016/j.patter.2025.101231`) and PMID
(`40843340`), and the 2026-08-18 five-entry Q-093 targeted review (`f8e1bece65`) does not
cover it. The thought doc it references, `docs/thoughts/2026-08-10_REE_efficiency.md`, is
tracked. As the investigation above established, `evidence/planning/*.md` is not read by the
indexer, so this affects no derived artifact.

## The timestamp hypothesis above is now supported

The investigation offered, explicitly as a hypothesis from mtimes, that one session wrote
item (1) and item (3) back to back (23:37 / 23:40 / 23:43) and then committed nothing,
consistent with item (1) failing schema validation and the session stopping there. The bytes
fit that: item (1) is complete but schema-invalid in exactly one place, and item (3) is
complete and was never blocked by anything. It remains a reconstruction -- no
`WORKSPACE_STATE.md` entry from 2026-08-13/14 explains the omission -- but nothing found on
this box contradicts it.

## Appendix: verbatim content of the deleted item (2)

Preserved for reversibility. `targeted_review_ethological_play_signals/record.json`,
5223 bytes, mtime 2026-08-14 15:04, never tracked.

```json
{
  "schema_version": "literature_evidence/v1",
  "literature_type": "targeted_review_ethological_play_signals",
  "review_id": "targeted_review_ethological_play_signals",
  "timestamp_utc": "2026-05-16T12:28:47Z",
  "review_description": "Targeted literature pull on ethological play signals and the three-level signal architecture (open/background/repair) described by Bekoff 1995 in canids. Goal: verify generalization beyond canids, understand functional specificity of each level, find evidence on what determines explicit repair signal deployment, and identify developmental timelines.",
  "claim_ids_tested": ["ARC-049", "Q-035", "INV-059", "DEV-NEED-009", "DEV-NEED-014"],
  "search_terms_used": [
    "play signals primates metacommunication ethology",
    "play face open mouth primates chimpanzee function",
    "Bekoff play signals canid dog metacommunication",
    "animal play behavior social signals development evolution",
    "dolphin cetacean play behavior social signals",
    "van Hooff play face open mouth display chimpanzee gorilla primate play signal ethology",
    "Palagi primate play signals laughter play face repair signals metacommunication",
    "play bow function dogs wolves puppies function initiation reinitiation",
    "gelada Theropithecus play face facial expression modulation social play",
    "hyena play signals visual communication social play",
    "raven juvenile play emotional contagion behavioral synchronization",
    "Waller gorilla facilitating play through communication teeth exposure play face 2010",
    "bottlenose dolphin open mouth play face smile signal rapid mimicry 2024 Palagi",
    "Palagi gelada face never lies facial mimicry modulate play 2022"
  ],
  "entries_count": 8,
  "entries": [
    "2026-05-16_arc049_bekoff1995_play_signals_canids_punctuation",
    "2026-05-16_arc049_q035_byosiere2017_play_bow_function_dogs_wolves",
    "2026-05-16_arc049_waller2012_gorilla_play_face_teeth_exposure",
    "2026-05-16_arc049_palagi2011_gelada_play_face_ontogeny",
    "2026-05-16_arc049_davilaross_palagi2022_laughter_play_faces_mimicry",
    "2026-05-16_arc049_nolfo_palagi2022_hyena_play_signals_visual",
    "2026-05-16_arc049_palagi2024_dolphin_open_mouth_play_mimicry",
    "2026-05-16_arc049_wenig2021_raven_play_emotional_contagion"
  ],
  "overall_verdict": "The three-level play signal architecture generalizes robustly beyond canids. Background signals (level-2) are documented in primates, gorillas, hyenas, and now dolphins via open-mouth displays and rapid facial mimicry (RFM). RFM is a conserved mammalian mechanism that sustains the play frame and predicts episode duration. Explicit repair/metacommunicative signals (level-3) are documented in hyenas (ROM, dissociated from background head-bobbing) and canids, and fire specifically at elevated ambiguity moments (asymmetric play, pre-offensive actions). Developmental timelines show that background signal sensitivity emerges through play experience (immature-to-adult transition documented in geladas). Corvid (raven) data extends the mood-maintenance principle to non-mammalian species but without a clear signal architecture.",
  "key_findings_for_arc049": [
    "Background signal (level-2) mechanism is conserved across mammals from canids to primates to hyenas to dolphins -- supported by phylogenetic homology of open-mouth expressions (Davila-Ross & Palagi 2022) and convergent evidence in cetaceans (Palagi 2024)",
    "Explicit repair signal (level-3) fires specifically at high-ambiguity moments: before offensive actions (Bekoff 1995 canids, Nolfo 2022 hyenas), after pauses in play (Byosiere 2017 dogs), and during asymmetric play (Nolfo 2022 hyenas) -- all variants of the same threshold-trigger mechanism",
    "Background signal is functionally necessary (not just convenient): RFM predicts episode duration (Davila-Ross 2022); episodes with adequate background signaling are longer and more balanced",
    "Background signal carries graded intensity information, not just binary on/off: gorilla PF vs full-PF dissociation (Waller 2012), gelada PF vs FPF developmental shift (Palagi 2011)",
    "Developmental trajectory confirmed: immature animals use simpler background signal variant (PF); adult signal sensitivity and variant use is acquired through play experience and neural maturation (Palagi 2011 geladas)",
    "Cross-taxon generalization at 95 MY distance: dolphins independently evolved OM play display with identical properties to terrestrial mammal play faces, and RFM rate matches terrestrial carnivores (Palagi 2024)"
  ],
  "missing_evidence": [
    "Direct evidence for level-3 explicit repair signals in primates (versus the background play face): no study yet isolates a primate-specific repair signal analogous to the canid play bow or hyena ROM",
    "Wild population data on RFM timing and play duration relationship (most RFM studies are captive)",
    "Longitudinal developmental data on play signal competence (cross-sectional data available for geladas; longitudinal trajectory not yet tracked)",
    "Corvid-specific play signal inventory: ravens show emotional contagion but no discrete play signal architecture has been documented in corvids"
  ]
}
```
