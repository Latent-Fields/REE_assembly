#!/usr/bin/env python3
"""Unapplied confirmed-autopsy recommendation audit (governance Step 3h, GOV-APPLY-1).

The FIFTH sibling of the failure-autopsy standing scans. The other four ask what a
set of verdicts MEANS, or whether the verdict was RECORDED. This one asks the next
question along: was the recorded verdict ever APPLIED?

  * GOV-CEIL-1  (check_substrate_ceiling_audit.py)      -- >=N ceiling verdicts on one claim
  * GOV-DIAG-1  (check_diagnostic_chain_recurrence.py)  -- >=N claimless no-verdict autopsies
  * GOV-GRAN-1  (check_granularity_debt_recurrence.py)  -- >=N structurally-different failures
  * GOV-CAT-1   (check_epistemic_category_completeness.py) -- the verdict was never RECORDED
  * GOV-APPLY-1 (this file)                             -- the verdict was never APPLIED

WHY THIS AUDIT EXISTS -- the already-reviewed blind spot
-------------------------------------------------------
/governance discovers autopsy recommendations by walking
`evidence/experiments/pending_review.md` and, for each run_id it surfaces, looking up
a confirmed `failure_autopsy_*.json` and reading its `recommended_*` fields
(governance SKILL.md Step 2 item 5). A run already listed in
`review_tracker.json:reviewed_run_ids` is ABSENT from pending_review.md -- so that
lookup NEVER RUNS for it.

The cycle therefore assumes adjudication precedes review. That assumption is FALSE
for every RE-adjudication, and a corpus sweep re-opens completed, reviewed runs BY
CONSTRUCTION. The recommendation is landed, confirmed, and structurally invisible.

Confirmed instance (the case this audit was built from), diagnosed in
`evidence/planning/intra_run_substrate_divergence_sweep_2026-07-20.md` sec 10:
`failure_autopsy_V3-EXQ-604c_2026-07-20` is confirmed and recommends demoting
MECH-314b / MECH-314c / Q-044 (`mixed` -> `non_contributory`, substrate_ceiling, on
structural vacuity). Its run is in reviewed_run_ids and returns 0 hits in
pending_review.md. The demotion survived THREE routing attempts (two spawn_task
chips that never produced a session, one application pass that landed the
substrate_queue entry but never reached the claim layer) before being caught by
hand.

The harm is not neutral. An unapplied demotion DECAYS INTO A POSITIVE CLAIM: while
604c sat unapplied, `inter_governance_workset.md` IGW-20260720-020 went on asserting
"Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS", which is precisely the
reading the autopsy withdrew.

THE 2026-08-20 REPAIR -- this audit was blind to its own question
----------------------------------------------------------------
`_reflects()` used to return True the moment a claim's `live_status.evidence.from`
mentioned the autopsy slug, and never opened a manifest at all. But an evidence
direction is not a claims.yaml fact: the indexer reads `evidence_direction` off the
run's MANIFEST (build_experiment_indexes.py:1708) and excludes an entry from scoring
only on that basis (:3396-3398), while `live_status.evidence.verdict` is prose that
nothing in the scoring path reads. So a recommendation could be cited in claims.yaml,
unapplied where it counts, and certified APPLIED here.

Confirmed instance (`docs/plans/mech236_registry_integrity_20260819.md`): a confirmed
autopsy reclassified V3-EXQ-914a `weakens -> non_contributory`, governance ratified it
into claims.yaml in `ff2e977acf`, and both manifest copies went on scoring `weakens` --
setting exp_conf 0.308 and conflict_ratio 0.5, which produced a
`hold_candidate_resolve_conflict` that the same governance program re-affirmed THIRTEEN
HOURS after ratifying the reclassification. This audit returned 0 hits for MECH-236
throughout, and the case it was BUILT from (604c / MECH-314b/314c/Q-044) had itself
gone silent the moment someone added the citation to claims.yaml.

A citation records that the autopsy was READ, not that it was APPLIED.

WHAT IT DOES *NOT* DO. It never edits claims.yaml, never writes a manifest, and is not
a gate. It makes an invisible debt visible; a human applies it in a /governance run,
per-case ratification FIRST -- a recorded recommendation is not by itself a ratified
one, and this audit cannot tell the difference. Read-only.

BUCKETS
-------
  unapplied_disposition  A confirmed target's `per_claim_recommendation[<claim>]`
                         records a `change` other than "STANDS" (e.g.
                         "mixed -> non_contributory"), and claims.yaml does not
                         reflect it. ACTIONABLE and STRICT-FAILING. This is the
                         high-precision bucket: the artifact states, in
                         machine-readable form, that a claim-layer change is owed.

  unapplied_evidence_direction
                         A confirmed target recommends an INERT evidence
                         direction (non_contributory / inconclusive /
                         superseded) while the manifest the indexer ACTUALLY
                         SCORES still carries a scoring one. Split by whether
                         the entry is live in `claim_evidence.v1.json`:
                         ACTIONABLE when it is weighting confidence right now,
                         WARN when it is already excluded by another route
                         (dry-run, stale substrate, diagnostic probe).

                         Added 2026-08-20. This is the bucket that would have
                         caught MECH-236, and it exists because
                         `unapplied_disposition` could not: it keys on the
                         target-level `recommended_evidence_direction`, which
                         nearly every confirmed target carries, rather than on
                         `per_claim_recommendation`, which only a few dozen of
                         them do. That is an order-of-magnitude-plus coverage
                         gap; the run-time `coverage:` line prints both counts
                         as they stand today. And it opens the manifest
                         instead of trusting claims.yaml prose.

                         It is NOT the category-compare inference rejected
                         below on precision grounds. That one INFERRED "a
                         change is owed" from two fields that legitimately
                         differ.
                         This compares a recommendation the artifact states
                         outright against the field the indexer scores -- a
                         disagreement is a fact about two files, not a
                         judgement. The fix is a MANIFEST write (flat AND
                         pack, with `evidence_direction_note`), not a
                         claims.yaml edit.

  superseded_disposition A confirmed target's `per_claim_recommendation[<claim>]`
                         is CONTRADICTED by a LATER confirmed target's recommendation
                         for the SAME CLAIM on a DIFFERENT run, and claims.yaml
                         already reflects that later recommendation. WARN-only: the
                         older artifact's disposition is moot, not owed -- it is
                         reported so the stale citation gets re-read, not silenced.

                         Added 2026-08-22 (GOV-APPLY-1 cross-run supersession
                         blind spot). See "THE 2026-08-22 REPAIR" below.

  superseded_citation    A claim whose `live_status.evidence.from` cites autopsy X
                         for run R, while a NEWER confirmed adjudication of the same
                         run R exists. The claim is being weighted by a superseded
                         reading. WARN-only: supersession does not always change the
                         claim-layer disposition (R1-R3 shape (c) retains both
                         direction and category), so a hit here is "re-read", not
                         "re-apply".

NAME BUCKETS BY KEY, NEVER BY ORDINAL
------------------------------------
Refer to a bucket as `unapplied_disposition`, `unapplied_evidence_direction` or
`superseded_citation` -- in prose, in comments, in argparse help, and in printed
output. Do not write "bucket 1"/"bucket 2"/"bucket 3".

The reason is this file's own history. `unapplied_evidence_direction` was
inserted in the MIDDLE of the list on 2026-08-20, and every ordinal downstream
silently repointed. Within hours the same two words named two different things
in one file: the KNOWN LIMIT paragraph's "bucket 2" still meant
`superseded_citation` (written when it was second), while the coverage line
printed at runtime said "bucket 2" meaning the newly-inserted direction bucket
-- and a third numbering, "BUCKET 3", labelled that same bucket in the scan
code. An ordinal is a positional reference into a list that later edits reorder;
nothing type-checks it, no test can assert it, and it cannot go stale loudly. A
key name cannot repoint. /governance SKILL.md states the same convention
(`067611cae1`); this is its code half.

COVERAGE IS REPORTED, DELIBERATELY
----------------------------------
`per_claim_recommendation` is a NEW convention (introduced by the 604c artifact),
so `unapplied_disposition` can only see targets that adopt it. The audit prints
its own coverage (`N of M confirmed targets carry a machine-readable per-claim
disposition`) rather than silently implying it checked everything.

NO CORPUS COUNTS ARE INLINED IN THIS FILE'S PROSE, AND THAT IS DELIBERATE. Every
coverage figure is printed at run time by the `coverage:` block in main(); read it
there. Hardcoded counts were removed on 2026-08-20 after three disagreeing values
for one quantity accumulated in this single file (a docstring count, a code-comment
count, and what the script actually printed). A corpus measurement embedded in
prose is true only on the day it is written, and re-measuring it by hand merely
resets the clock. Where a magnitude is load-bearing to an ARGUMENT it is stated as
a magnitude ("a few dozen", "an order of magnitude"), never as a precise count. Do
not "helpfully" restore exact numbers here. Historical one-off measurements of
things this script does NOT compute (e.g. the rejected category-compare inference
below) are kept, but always carried with the date they were taken.

That under-claim is deliberate, and it is the honest design. The rejected
alternative was to INFER "change owed" by comparing each target's
`recommended_epistemic_category` against the claim's current one. Measured
2026-07-20, that yields 338 claim-level mismatches, the overwhelming majority of
which are NOT defects -- an affirming autopsy (routing `governance-affirm`,
direction unchanged) legitimately recommends a per-target category that the claim
layer never mirrors. `failure_autopsy_V3-EXQ-778a_2026-07-20` is the canonical
example: `instrument_repair_validated` against four claims that correctly carry no
category. A report of that size that is mostly wrong would be ignored, and an
ignored report is the same failure as no report. Precision first; coverage grows
as the convention spreads.

THE 2026-08-22 REPAIR -- unapplied_disposition had the MIRROR-IMAGE blind spot
------------------------------------------------------------------------------
`superseded_citation`'s own KNOWN LIMIT (below) already names the general shape:
a supersession that moves to a DIFFERENT run is invisible to anything keyed on
run_id. `unapplied_disposition`'s R2 dedup is keyed on run_id for exactly that
reason -- but a claim can be re-adjudicated across DIFFERENT runs, and nothing
deduped THAT. The result was not under-reporting but its opposite: a claim
whose disposition claims.yaml already reflects, correctly, per the LATEST
confirmed autopsy, went on being reported ACTIONABLE forever because an OLDER
confirmed autopsy's per-claim recommendation -- for a different run of the same
claim -- was compared against current claims.yaml state and, naturally, no
longer matched it.

Confirmed instance: `failure_autopsy_V3-EXQ-436e_2026-08-13` recommends
`epistemic_category unset -> standard` for ARC-045/MECH-166/SD-017 (run
`v3_exq_436e_...`). `failure_autopsy_436f-603u-precondition-blocked-cluster_
2026-08-16` -- a LATER confirmed autopsy of a DIFFERENT run
(`v3_exq_436f_...`) covering the SAME three claims -- recommends
`epistemic_category standard -> substrate_ceiling` instead. claims.yaml
carries `substrate_ceiling` for all three: the 436f disposition, correctly
applied. 436e's disposition was superseded before it was ever applied, and
this audit re-adjudicated it by hand every cycle regardless, since it never
compared a target against anything but claims.yaml's CURRENT state.

The fix generalises R2 from "per run_id" to "per claim, across every run a
confirmed target names": for each claim, the LATEST confirmed per-claim
recommendation is authoritative. An older recommendation that DISAGREES with
the latest, where claims.yaml reflects the latest, moves to
`superseded_disposition` (WARN) instead of `unapplied_disposition`
(ACTIONABLE). An older recommendation that AGREES with the latest, or whose
latest sibling is itself unapplied, is unaffected -- both still route to
`unapplied_disposition`, biased toward false positives exactly as before.

KNOWN LIMIT. `superseded_citation` keys on run_id, so it cannot see a supersession
that moves to a DIFFERENT run. Q-044 is exactly that case -- it cites the 604b
cluster autopsy while the superseding adjudication is of 604c, a different run --
and is caught only by `unapplied_disposition`. Do not read an empty
`superseded_citation` as "no stale citations". (This is the SAME shape the
2026-08-22 repair above fixes for `unapplied_disposition` itself -- but
`superseded_citation`'s own run_id-keyed blind spot is unchanged; it is not in
this fix's scope.)

USAGE
  python3 scripts/check_unapplied_autopsy_recommendations.py
  python3 scripts/check_unapplied_autopsy_recommendations.py --full     # list every direction row
  python3 scripts/check_unapplied_autopsy_recommendations.py --strict   # exit 1 on unapplied_disposition
  python3 scripts/check_unapplied_autopsy_recommendations.py --strict-direction

`--strict`'s contract is DELIBERATELY UNCHANGED by the direction bucket: it gates on
`unapplied_disposition` only, because governance.sh Step 3h and any CI caller predate
the new bucket. That bucket runs an order of magnitude hotter than
`unapplied_disposition` (compare the two counts in the report header), so folding
it into their exit code would silently convert a warn-only step into a failing
one. `--strict-direction` is the opt-in.

Tests: scripts/test_check_unapplied_autopsy_recommendations.py
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
AUTOPSY_GLOB = "evidence/planning/failure_autopsy_*.json"
CLAIMS_YAML = "docs/claims/claims.yaml"
EVIDENCE_DIR = "evidence/experiments"
CLAIM_EVIDENCE = "evidence/experiments/claim_evidence.v1.json"

STANDS = "STANDS"

# Runs listed for unapplied_evidence_direction before the report truncates;
# --full prints all.
DIRECTION_DISPLAY_LIMIT = 25

# ---------------------------------------------------------------------------
# MIRROR OF THE INDEXER'S SCORING RULES.
#
# Everything in this block is a deliberate copy of
# `evidence/experiments/scripts/build_experiment_indexes.py`, cited by line.
# It is NOT imported, for the same reason generate_pending_review.py keeps its
# own re-scan: that module is 7900 lines, executes work at import, and this
# audit must stay a cheap read-only CLI. The cost of copying is drift, so each
# constant names the line it mirrors -- if a direction is added there and not
# here, this audit silently under-reports, which is the defect it exists to
# catch. `scripts/test_check_unapplied_autopsy_recommendations.py` pins the
# vocabulary against the indexer's own source text.
# ---------------------------------------------------------------------------

# build_experiment_indexes.py:1113 -- the accepted `evidence_direction` values.
_DIRECTION_VOCAB = {
    "supports", "weakens", "mixed", "unknown", "superseded",
    "non_contributory", "inconclusive", "does_not_support",
}
# :1116 -- synonyms folded before scoring.
_DIRECTION_SYNONYMS = {"does_not_support": "weakens"}

# :3358 and :3396-3398 -- directions the indexer refuses to score. An entry
# carrying one of these never reaches `claim_to_entries`, so it cannot weight
# confidence or the conflict ratio. Everything else (supports/weakens/mixed/
# unknown) DOES score.
INERT_DIRECTIONS = {"non_contributory", "inconclusive", "superseded"}

# :1428 `_ANNOTATION_MARKER_FIELDS` -- the discriminator that tells a
# deliberately-corrected manifest copy from a stale auto-emitted one.
_ANNOTATION_MARKER_FIELDS = (
    "evidence_direction_note",
    "degeneracy_reason",
    "superseded_by",
    "superseded_by_substrate",
)

# :1346 `_FLAT_AUTHORITATIVE_FIELDS` -- restricted to the direction-carrying
# subset, which is all this audit compares.
_FLAT_DIRECTION_FIELDS = (
    "evidence_direction",
    "evidence_direction_per_claim",
    "evidence_direction_note",
)


def _load_json(path: Path):
    try:
        with open(path) as fh:
            return json.load(fh)
    except Exception:
        return None


def _claim_ids(target: dict) -> list:
    cids = target.get("claim_ids")
    if isinstance(cids, list) and cids:
        return [c for c in cids if isinstance(c, str)]
    single = target.get("claim_id")
    return [single] if isinstance(single, str) and single else []


def load_confirmed(root: Path):
    """Return (targets, latest_by_run, runs_by_slug).

    targets     : list of (generated_utc, slug, target dict)
    latest_by_run: run_id -> (generated_utc, slug)   [R2: latest adjudication wins]
    runs_by_slug: slug -> set(run_id)
    """
    targets = []
    latest = {}
    runs_by_slug = {}
    for p in sorted(glob.glob(str(root / AUTOPSY_GLOB))):
        path = Path(p)
        data = _load_json(path)
        if not isinstance(data, dict):
            continue
        if str(data.get("status")) != "confirmed":
            continue
        gen = str(data.get("generated_utc") or "")
        slug = path.stem
        for target in data.get("targets", []) or []:
            if not isinstance(target, dict):
                continue
            targets.append((gen, slug, target))
            run_id = target.get("run_id")
            if not isinstance(run_id, str) or not run_id:
                continue
            runs_by_slug.setdefault(slug, set()).add(run_id)
            # R2 -- the most recent adjudication of a run supersedes its predecessors
            if run_id not in latest or (gen, slug) > latest[run_id]:
                latest[run_id] = (gen, slug)
    return targets, latest, runs_by_slug


def load_claims(root: Path) -> dict:
    """Index claims.yaml by id. Falls back to a regex scan if PyYAML is absent."""
    path = root / CLAIMS_YAML
    try:
        import yaml  # noqa: F401
    except ImportError:
        return _load_claims_regex(path)
    import yaml
    try:
        with open(path) as fh:
            doc = yaml.safe_load(fh)
    except Exception:
        return _load_claims_regex(path)
    claims = {}

    def harvest(node):
        if isinstance(node, dict):
            cid = node.get("id")
            if isinstance(cid, str):
                claims[cid] = node
            for value in node.values():
                harvest(value)
        elif isinstance(node, list):
            for value in node:
                harvest(value)

    harvest(doc)
    return claims


def _load_claims_regex(path: Path) -> dict:
    """Degraded index: id -> {} so membership tests still work without PyYAML."""
    try:
        text = path.read_text()
    except OSError:
        return {}
    return {m.group(1): {} for m in re.finditer(r"^\s*-?\s*id:\s*(\S+)\s*$", text, re.M)}


def _normalize_direction(raw) -> str:
    """Mirror of build_experiment_indexes.py:1110 `_normalize_direction`."""
    value = (raw or "unknown")
    if not isinstance(value, str):
        return "unknown"
    value = value.strip().lower()
    if value not in _DIRECTION_VOCAB:
        return "unknown"
    return _DIRECTION_SYNONYMS.get(value, value)


def _is_annotated(manifest) -> bool:
    """Mirror of build_experiment_indexes.py:1436 `_is_annotated`.

    THE TRAP THIS ENCODES. `evidence_direction_note` is not editorial -- it is
    the marker without which the flat-over-pack overlay at :1517 never fires.
    A flat copy corrected to `non_contributory` with NO note is silently
    discarded and the stale pack value goes on scoring (confirmed 2026-06-14 on
    MECH-171 x3 / MECH-057b). So "the manifest says the right thing" is not the
    question; "the manifest the indexer RESOLVES says it" is.
    """
    if not isinstance(manifest, dict):
        return False
    for field in _ANNOTATION_MARKER_FIELDS:
        if str(manifest.get(field, "") or "").strip():
            return True
    return False


class Effective:
    """The direction the indexer would actually score for one run."""

    __slots__ = ("run_id", "direction", "raw", "source", "claim_ids", "per_claim")

    def __init__(self, run_id, direction, raw, source, claim_ids, per_claim):
        self.run_id = run_id
        self.direction = direction
        self.raw = raw
        self.source = source
        self.claim_ids = claim_ids
        self.per_claim = per_claim

    def for_claim(self, claim_id):
        """Per-claim override wins over the run-level field (indexer :3291)."""
        if claim_id and claim_id in self.per_claim:
            return self.per_claim[claim_id]
        return self.direction


class ManifestResolver:
    """Resolves a run_id to the manifest copy the indexer scores.

    Follows build_experiment_indexes.py exactly:

      * the run pack `<base>/<type>/runs/<run_id>/manifest.json` is the scoring
        source (:1346 call site);
      * its flat sibling is looked up by EXACT PATH at `<base>/<run_id>.json`
        FIRST, then `<base>/<type>/<run_id>.json` (:1553 `_resolve_flat_sibling`,
        whose docstring records that this order is load-bearing);
      * the flat copy overrides the direction fields ONLY when
        `_is_annotated(flat) and not _is_annotated(pack)` (:1517).

    Deliberately NOT "any file whose run_id field matches". That looser rule
    finds corrections the indexer itself cannot reach -- a flat file whose
    FILENAME omits the run_id's `_v3` suffix is invisible to `_resolve_flat_
    sibling`, so its correction never applies while a reader keying on the
    run_id field concludes it did. Measured 2026-08-20: 7 live (claim, run)
    rows differ on exactly this, all in the direction of under-reporting.

    Manifests are loaded LAZILY -- the pack corpus runs to thousands of files
    and this audit needs only the subset that a confirmed target names.
    """

    def __init__(self, root: Path):
        self.base = root / EVIDENCE_DIR
        self._packs = None
        self._cache = {}

    def _pack_index(self):
        if self._packs is None:
            index = {}
            if self.base.is_dir():
                for path in self.base.glob("**/runs/*/manifest.json"):
                    if path.parent.parent.name != "runs":
                        continue
                    index.setdefault(path.parent.name, path)
            self._packs = index
        return self._packs

    def _flat_for(self, run_id, pack_path):
        candidates = [self.base / ("%s.json" % run_id)]
        if pack_path is not None:
            # <base>/<type>/runs/<run_id>/manifest.json -> <base>/<type>/
            candidates.append(pack_path.parent.parent.parent / ("%s.json" % run_id))
        for candidate in candidates:
            if candidate.is_file():
                return candidate
        return None

    def resolve(self, run_id):
        """Return an Effective, or None when no manifest exists for the run."""
        if not isinstance(run_id, str) or not run_id:
            return None
        if run_id in self._cache:
            return self._cache[run_id]
        pack_path = self._pack_index().get(run_id)
        pack = _load_json(pack_path) if pack_path is not None else None
        flat_path = self._flat_for(run_id, pack_path)
        flat = _load_json(flat_path) if flat_path is not None else None

        if not isinstance(pack, dict) and not isinstance(flat, dict):
            self._cache[run_id] = None
            return None

        if not isinstance(pack, dict):
            # No pack at all: nothing for the indexer's run scan to pick up.
            merged, source = flat, "flat_only"
        elif isinstance(flat, dict) and _is_annotated(flat) and not _is_annotated(pack):
            merged = dict(pack)
            for field in _FLAT_DIRECTION_FIELDS:
                if field in flat:
                    merged[field] = flat[field]
            source = "flat_overlay"
        else:
            merged, source = pack, "pack"

        raw = merged.get("evidence_direction")
        # The pack keys claims as `claim_ids_tested`; only the flat copy uses
        # `claim_ids`. Reading the wrong one yields an empty claim list and a
        # silently empty check (indexer :3289).
        claim_ids_raw = merged.get("claim_ids_tested") or merged.get("claim_ids") or []
        if not isinstance(claim_ids_raw, list):
            claim_ids_raw = []
        claim_ids = [str(c).strip() for c in claim_ids_raw if str(c).strip()]

        per_claim = {}
        raw_per_claim = merged.get("evidence_direction_per_claim") or {}
        if isinstance(raw_per_claim, dict):
            for cid, val in raw_per_claim.items():
                normalized = _normalize_direction(val)
                if normalized != "unknown":  # placeholder entries are a no-op
                    per_claim[str(cid)] = normalized

        result = Effective(run_id, _normalize_direction(raw),
                           str(raw or "").strip(), source, claim_ids, per_claim)
        self._cache[run_id] = result
        return result

    def effective_direction(self, run_id, claim_id=None):
        resolved = self.resolve(run_id)
        if resolved is None:
            return None
        return resolved.for_claim(claim_id)


def load_live_pairs(root: Path):
    """(claim_id, run_id) pairs that are SCORING right now.

    Read from the indexer's own output `claim_evidence.v1.json`: an entry that
    is present with a null `scoring_excluded` is weighting confidence and the
    conflict ratio today. This is what separates a manifest that is merely
    wrong on disk from one that is actively producing a wrong number.

    Returns None when the artifact is absent or unreadable -- callers then
    degrade to reporting every disagreement as WARN rather than claiming a
    liveness they cannot establish.
    """
    data = _load_json(root / CLAIM_EVIDENCE)
    if not isinstance(data, dict):
        return None
    entries = data.get("entries")
    if not isinstance(entries, list):
        return None
    live = set()
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        if entry.get("source_type") != "experimental":
            continue
        if entry.get("scoring_excluded") not in (None, ""):
            continue
        claim_id = str(entry.get("claim_id") or "").strip()
        run_id = str(entry.get("run_id") or "").strip()
        if claim_id and run_id:
            live.add((claim_id, run_id))
    return live


def _target_state(change, recommended_direction):
    """The right-hand side of a disposition: "mixed -> non_contributory" -> the
    second half, else the bare recommended direction."""
    if isinstance(change, str) and "->" in change:
        return change.split("->")[-1].strip()
    if isinstance(recommended_direction, str):
        return recommended_direction.strip()
    return None


def _reflects(claim, change, recommended_direction, slug,
              claim_id=None, run_id=None, resolver=None) -> bool:
    """Is this per-claim disposition already applied WHERE IT IS SCORED?

    Deliberately BIASED TOWARD FALSE POSITIVES (reporting an applied item costs
    one glance; omitting an unapplied one is the whole defect). Anything it
    cannot verify it reports.

    THE PROSE SHORT-CIRCUIT IS GONE, AND THAT IS THE POINT.
    ------------------------------------------------------
    Until 2026-08-20 this function returned True the moment a claim's
    `live_status.evidence.from` mentioned the autopsy slug, and never opened a
    manifest at all. But an EVIDENCE DIRECTION is not a claims.yaml fact. The
    indexer reads `evidence_direction` off the run's MANIFEST
    (build_experiment_indexes.py:1708) and excludes the entry from scoring only
    on that basis (:3396-3398); `live_status.evidence.verdict` is human-legible
    prose that nothing in the scoring path reads. So a recommendation could be
    cited in claims.yaml, unapplied where it counts, and certified APPLIED here.

    Confirmed instance (MECH-236, diagnosed in
    `docs/plans/mech236_registry_integrity_20260819.md`): a confirmed autopsy
    reclassified V3-EXQ-914a `weakens -> non_contributory`, governance ratified
    it into claims.yaml prose in `ff2e977acf`, and BOTH manifest copies kept
    scoring `weakens`. That set experimental_confidence 0.308 and
    conflict_ratio 0.5, which produced a `hold_candidate_resolve_conflict` the
    same governance program re-affirmed THIRTEEN HOURS after ratifying the
    reclassification. This audit returned 0 hits for MECH-236 throughout.

    A citation records that the autopsy was READ, not that it was APPLIED.

    Routing, by what kind of state the disposition names:

      * an EVIDENCE DIRECTION -> the manifest is the authority. Verified
        through the same pack/flat + `_is_annotated` overlay rule the indexer
        uses, honouring the per-claim override. Unverifiable (no manifest, no
        run_id, no resolver) reports as unapplied.
      * anything else (epistemic_category, status) -> claims.yaml is genuinely
        the authority, and those fields are compared directly.
    """
    target_state = _target_state(change, recommended_direction)
    if not target_state:
        return False

    if target_state.strip().lower() in _DIRECTION_VOCAB:
        if resolver is None or not run_id:
            return False  # cannot verify -> do not certify
        effective = resolver.effective_direction(run_id, claim_id)
        if effective is None:
            return False  # no manifest -> cannot certify
        return effective == _normalize_direction(target_state)

    if not isinstance(claim, dict) or not claim:
        return False
    for field in ("epistemic_category", "status"):
        if str(claim.get(field) or "").strip() == target_state:
            return True
    live = claim.get("live_status")
    if isinstance(live, dict) and str(live.get("reading") or "").strip() == target_state:
        return True
    return False


def _recommended_for_claim(target, claim_id):
    """The direction a confirmed target recommends for one claim.

    Precedence, most specific first: the per-claim recommendation block, then
    `recommended_evidence_direction_per_claim`, then the target-level
    `recommended_evidence_direction`.
    """
    pcr = target.get("per_claim_recommendation")
    if isinstance(pcr, dict) and isinstance(pcr.get(claim_id), dict):
        value = pcr[claim_id].get("recommended_evidence_direction")
        if isinstance(value, str) and value.strip():
            return value.strip()
    per_claim = target.get("recommended_evidence_direction_per_claim")
    if isinstance(per_claim, dict):
        value = per_claim.get(claim_id)
        if isinstance(value, str) and value.strip():
            return value.strip()
    value = target.get("recommended_evidence_direction")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _scoped_claims(target, resolved):
    """Which claims a target's recommendation covers, on the scored manifest.

    The autopsy's own `claim_ids` bound the scope -- a run-level recommendation
    is not evidence about a claim the adjudication never considered -- but a
    claim the MANIFEST does not tag cannot score either way, so the answer is
    the intersection. A target naming no claims falls back to the manifest's
    list, which is the set the run-level `evidence_direction` actually governs.
    """
    manifest_claims = list(resolved.claim_ids)
    target_claims = _claim_ids(target)
    if not target_claims:
        return manifest_claims
    named = set(target_claims)
    scoped = [c for c in manifest_claims if c in named]
    # A per-claim recommendation is explicit about its claim even when the
    # manifest's tag list is stale; keep those.
    for extra in target_claims:
        if extra in manifest_claims and extra not in scoped:
            scoped.append(extra)
    return scoped


def scan(root: Path) -> dict:
    targets, latest, runs_by_slug = load_confirmed(root)
    claims = load_claims(root)
    resolver = ManifestResolver(root)
    live_pairs = load_live_pairs(root)

    unapplied = []
    superseded_disposition = []
    direction_rows = []
    n_with_pcr = 0
    n_with_recommended_direction = 0
    n_direction_checkable = 0
    n_over_excluded = 0

    # Pass 1 -- collect every per-claim recommendation, keyed by CLAIM rather
    # than by run. R2 (latest-per-run_id) still applies here, unchanged: it
    # only ever discards a strictly-superseded re-adjudication of the SAME
    # run, never a different run's target for the same claim.
    per_claim_entries = {}
    for gen, slug, target in targets:
        run_id = target.get("run_id")
        # R2 -- only the latest adjudication of a run is authoritative
        if isinstance(run_id, str) and run_id in latest and latest[run_id] != (gen, slug):
            continue
        pcr = target.get("per_claim_recommendation")
        if not isinstance(pcr, dict) or not pcr:
            continue
        n_with_pcr += 1
        for cid, rec in pcr.items():
            if not isinstance(rec, dict):
                continue
            change = str(rec.get("change") or "").strip()
            if not change or change.upper() == STANDS:
                continue
            if claims.get(cid) is None:
                continue  # claim id not in registry -- GOV-CAT-1's lane, not ours
            per_claim_entries.setdefault(cid, []).append({
                "gen": gen, "slug": slug, "run_id": run_id, "change": change, "rec": rec,
            })

    # Pass 2 -- for each claim, the LATEST confirmed recommendation (by
    # generated_utc, regardless of which run it targets) is authoritative.
    # An older, DISAGREEING recommendation whose claim already reflects the
    # latest one is superseded, not unapplied -- see "THE 2026-08-22 REPAIR"
    # in the module docstring. Everything else (the latest entry itself, an
    # older entry that agrees with the latest, or an older entry whose
    # latest sibling is ALSO unapplied) is unaffected and stays biased
    # toward false positives exactly as before.
    for cid, entries in per_claim_entries.items():
        entries_sorted = sorted(entries, key=lambda e: e["gen"])
        latest_entry = entries_sorted[-1]
        latest_reflects = None
        for entry in entries_sorted:
            claim = claims.get(cid)
            if _reflects(claim, entry["change"], entry["rec"].get("recommended_evidence_direction"),
                         entry["slug"], claim_id=cid, run_id=entry["run_id"], resolver=resolver):
                continue
            is_earlier = entry is not latest_entry and entry["gen"] < latest_entry["gen"]
            if is_earlier and entry["change"] != latest_entry["change"]:
                if latest_reflects is None:
                    latest_reflects = _reflects(
                        claim, latest_entry["change"],
                        latest_entry["rec"].get("recommended_evidence_direction"),
                        latest_entry["slug"], claim_id=cid, run_id=latest_entry["run_id"],
                        resolver=resolver)
                if latest_reflects:
                    superseded_disposition.append({
                        "claim_id": cid,
                        "change": entry["change"],
                        "artifact": entry["slug"],
                        "generated_utc": entry["gen"],
                        "run_id": entry["run_id"],
                        "superseded_by": latest_entry["slug"],
                        "superseded_by_change": latest_entry["change"],
                    })
                    continue
            unapplied.append({
                "claim_id": cid,
                "change": entry["change"],
                "artifact": entry["slug"],
                "generated_utc": entry["gen"],
                "run_id": entry["run_id"],
                "recommended_epistemic_category": entry["rec"].get("recommended_epistemic_category"),
            })

    # ------------------------------------------------------------------
    # BUCKET unapplied_evidence_direction (added 2026-08-20)
    #
    # Keys on the target-level `recommended_evidence_direction`, which nearly
    # every confirmed target carries, against `per_claim_recommendation`'s few
    # dozen. (No counts inlined -- main() prints both at run time; see the
    # module docstring's COVERAGE IS REPORTED section for why.) That
    # order-of-magnitude-plus coverage gap is why unapplied_disposition could
    # not see MECH-236: both of that artifact's targets were skipped before
    # any check ran.
    #
    # This is NOT the category-compare inference the module docstring rejects
    # on precision grounds. That one INFERRED "a change is owed" from two fields
    # that legitimately differ. This one reads a recommendation the artifact
    # states outright and compares it to the field the indexer scores -- a
    # disagreement here is a fact about two files, not a judgement.
    # ------------------------------------------------------------------
    for gen, slug, target in targets:
        run_id = target.get("run_id")
        if not isinstance(run_id, str) or not run_id:
            continue
        if latest.get(run_id) != (gen, slug):
            continue  # R2 -- only the latest adjudication of a run is authoritative
        if not (target.get("recommended_evidence_direction")
                or target.get("recommended_evidence_direction_per_claim")
                or target.get("per_claim_recommendation")):
            continue
        n_with_recommended_direction += 1
        resolved = resolver.resolve(run_id)
        if resolved is None:
            continue  # no manifest on disk -- nothing to compare against
        n_direction_checkable += 1
        for cid in _scoped_claims(target, resolved):
            recommended = _recommended_for_claim(target, cid)
            if not recommended:
                continue
            want = _normalize_direction(recommended)
            have = resolved.for_claim(cid)
            if have == want:
                continue
            if want not in INERT_DIRECTIONS or have in INERT_DIRECTIONS:
                # Either the recommendation does not change scoring, or the
                # entry is already inert. The reverse shape (a scoring
                # direction recommended over an inert one) UNDER-counts
                # evidence rather than manufacturing it, so it is counted and
                # reported as a total, not listed.
                if want not in INERT_DIRECTIONS and have in INERT_DIRECTIONS:
                    n_over_excluded += 1
                continue
            live = None if live_pairs is None else ((cid, run_id) in live_pairs)
            direction_rows.append({
                "claim_id": cid,
                "run_id": run_id,
                "artifact": slug,
                "generated_utc": gen,
                "effective_direction": have,
                "effective_direction_raw": resolved.raw,
                "recommended_direction": want,
                "manifest_source": resolved.source,
                "live": live,
            })

    superseded = []
    for cid, claim in sorted(claims.items()):
        live = claim.get("live_status") if isinstance(claim, dict) else None
        if not isinstance(live, dict):
            continue
        evidence = live.get("evidence")
        if not isinstance(evidence, dict):
            continue
        match = re.match(r"(failure_autopsy_[^#\s]+)", str(evidence.get("from") or ""))
        if not match:
            continue
        cited = match.group(1).strip()
        for run_id in sorted(runs_by_slug.get(cited, ())):
            newest = latest.get(run_id, ("", ""))[1]
            if newest and newest != cited:
                superseded.append({
                    "claim_id": cid, "cites": cited,
                    "superseded_by": newest, "run_id": run_id,
                })
                break

    return {
        "unapplied_disposition": unapplied,
        "unapplied_evidence_direction": direction_rows,
        "superseded_disposition": superseded_disposition,
        "superseded_citation": superseded,
        "n_confirmed_targets": len(targets),
        "n_with_per_claim_recommendation": n_with_pcr,
        "n_with_recommended_direction": n_with_recommended_direction,
        "n_direction_checkable": n_direction_checkable,
        "n_over_excluded": n_over_excluded,
        "liveness_available": live_pairs is not None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 if any unapplied_disposition is found "
                             "(that bucket only -- unapplied_evidence_direction "
                             "never affects this exit; contract unchanged)")
    parser.add_argument("--strict-direction", action="store_true",
                        help="exit 1 if any LIVE unapplied_evidence_direction is found")
    parser.add_argument("--full", action="store_true",
                        help="list every unapplied_evidence_direction row "
                             "(default: the first %d runs)" % DIRECTION_DISPLAY_LIMIT)
    parser.add_argument("--root", default=str(REPO_ROOT),
                        help="REE_assembly root (default: this script's parent)")
    args = parser.parse_args()

    root = Path(args.root)
    buckets = scan(root)
    unapplied = buckets["unapplied_disposition"]
    directions = buckets["unapplied_evidence_direction"]
    superseded_disposition = buckets["superseded_disposition"]
    superseded = buckets["superseded_citation"]
    n_targets = buckets["n_confirmed_targets"]
    n_pcr = buckets["n_with_per_claim_recommendation"]
    n_rec_dir = buckets["n_with_recommended_direction"]
    n_dir_checkable = buckets["n_direction_checkable"]
    live_rows = [d for d in directions if d["live"]]
    other_rows = [d for d in directions if not d["live"]]

    print("Unapplied confirmed-autopsy recommendation audit (GOV-APPLY-1)")
    print("  unapplied claim disposition (ACTIONABLE): %d" % len(unapplied))
    print("  unapplied evidence direction, LIVE (ACTIONABLE): %d row(s), "
          "%d run(s), %d claim(s)"
          % (len(live_rows), len({d["run_id"] for d in live_rows}),
             len({d["claim_id"] for d in live_rows})))
    print("  unapplied evidence direction, not scoring (WARN): %d" % len(other_rows))
    print("  superseded claim disposition (WARN)     : %d" % len(superseded_disposition))
    print("  superseded live_status citation (WARN)  : %d" % len(superseded))
    print("  coverage: %d of %d confirmed targets carry a machine-readable"
          % (n_pcr, n_targets))
    print("            per-claim disposition (-> unapplied_disposition);")
    print("            %d carry a target-level recommended_evidence_direction"
          % n_rec_dir)
    print("            (-> unapplied_evidence_direction), of which %d resolve"
          % n_dir_checkable)
    print("            to a manifest and are checked.")
    if not buckets["liveness_available"]:
        print("  NOTE: claim_evidence.v1.json unreadable -- every direction row is")
        print("        reported as WARN because liveness could not be established.")
    if buckets["n_over_excluded"]:
        print("  NOTE: %d row(s) are inert on disk where the autopsy recommended a"
              % buckets["n_over_excluded"])
        print("        scoring direction. That UNDER-counts evidence rather than")
        print("        manufacturing it, so it is counted here and not listed.")

    if unapplied:
        print("")
        print("ACTIONABLE -- a confirmed autopsy records a claim-layer change that")
        print("claims.yaml does not reflect. These are invisible to the /governance")
        print("walk whenever the run is already in reviewed_run_ids (the whole point")
        print("of this audit). Apply them in a /governance run; do NOT edit here.")
        for item in sorted(unapplied, key=lambda d: (d["generated_utc"], d["claim_id"])):
            print("  - %-12s %s" % (item["claim_id"], item["change"]))
            print("      from %s (%s)" % (item["artifact"], item["generated_utc"][:10]))
    else:
        print("")
        print("  -- no confirmed autopsy has an unapplied claim disposition.")

    if live_rows:
        print("")
        print("ACTIONABLE -- a confirmed autopsy recommended an INERT evidence")
        print("direction and the manifest the indexer actually scores still carries")
        print("a SCORING one, and the entry IS weighting confidence right now.")
        print("The fix is a manifest write (flat AND pack), not a claims.yaml edit:")
        print("claims.yaml holds no numbers, so prose alone changes nothing.")
        print("Write evidence_direction_note alongside -- without it the flat-over-")
        print("pack overlay never fires and a flat-only correction is discarded.")
        print("Apply in a /governance run, per-case ratification FIRST; a recorded")
        print("recommendation is not by itself a ratified one.")
        by_run = {}
        for row in live_rows:
            by_run.setdefault(row["run_id"], []).append(row)
        ordered = sorted(by_run.items(),
                         key=lambda kv: (kv[1][0]["generated_utc"], kv[0]))
        shown = ordered if args.full else ordered[:DIRECTION_DISPLAY_LIMIT]
        for run_id, rows in shown:
            head = rows[0]
            print("  - %s" % run_id)
            print("      %s -> %s   claims: %s"
                  % (head["effective_direction"], head["recommended_direction"],
                     ", ".join(sorted(r["claim_id"] for r in rows))))
            print("      from %s (%s), manifest source: %s"
                  % (head["artifact"], head["generated_utc"][:10],
                     head["manifest_source"]))
        if len(ordered) > len(shown):
            print("  ... and %d more run(s); re-run with --full to list them."
                  % (len(ordered) - len(shown)))

    if superseded_disposition:
        print("")
        print("WARN -- a confirmed autopsy's per-claim disposition is superseded by")
        print("a LATER confirmed autopsy of a DIFFERENT run for the same claim, and")
        print("claims.yaml already reflects the later recommendation. Nothing is")
        print("owed here -- re-read before citing the older artifact, do not re-apply.")
        for item in sorted(superseded_disposition,
                            key=lambda d: (d["generated_utc"], d["claim_id"])):
            print("  - %-12s %s" % (item["claim_id"], item["change"]))
            print("      from %s (%s)" % (item["artifact"], item["generated_utc"][:10]))
            print("      superseded by %s" % item["superseded_by"])

    if superseded:
        print("")
        print("WARN -- claim live_status cites an autopsy that a NEWER confirmed")
        print("adjudication of the same run supersedes. Re-read before citing; under")
        print("R1-R3 shape (c) a supersession may legitimately retain the reading.")
        for item in superseded:
            print("  - %-12s cites %s" % (item["claim_id"], item["cites"]))
            print("      superseded by %s" % item["superseded_by"])

    print("")
    print("Read-only. Promotes/demotes nothing. See intra_run_substrate_divergence_"
          "sweep_2026-07-20.md sec 10.")

    if args.strict and unapplied:
        return 1
    if args.strict_direction and live_rows:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
