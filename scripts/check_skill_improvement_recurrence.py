#!/usr/bin/env python3
"""Skill-improvement recurrence audit (governance, GOV-SKILL-1).

The FIFTH sibling of the failure-autopsy standing scans, and the first one that
audits the SKILLS themselves rather than the claims registry:

  * GOV-CEIL-1 (check_substrate_ceiling_audit.py)     -- >=N ceiling verdicts on one claim
  * GOV-DIAG-1 (check_diagnostic_chain_recurrence.py) -- >=N claimless no-verdict autopsies
  * GOV-GRAN-1 (check_granularity_debt_recurrence.py) -- >=N structurally-different failures
  * GOV-CAT-1  (check_epistemic_category_completeness.py) -- the verdict was never recorded
  * GOV-SKILL-1 (this file)                           -- a non-outcome LESSON keeps recurring
                                                          and no skill checklist has absorbed it

WHY THIS AUDIT EXISTS. `REE_assembly/evidence/planning/skill_improvement_audit_scoping_2026-08-01.md`
scoped this: a human session close-reading 10 confirmed autopsies found that roughly half of
`learning_extracted` items are NON-OUTCOME findings -- reusable code bugs, schema-legibility
gaps, methodology/statistic caveats -- not diagnosis of the specific result under test. Two such
findings were folded into `/queue-experiment` Step 3.5 and `/governance` Step 2b the same day,
by a human watching in real time. That is a REACTIVE, single-incident process: it depends on (a)
a human happening to notice, (b) doing so in the same session, and (c) the fold-in actually
happening. This audit is the STANDING counterpart, exactly as GOV-GRAN-1/GOV-CAT-1/GOV-CEIL-1/
GOV-DIAG-1 are standing counterparts to their own reactive `/failure-autopsy` triggers.

A one-off manual sweep run the same day (scoping doc "Sweep result") used a cheap high-precision
"self-flagged repeat" grep over `learning_extracted[]` (`recurring`, `twice`, `same signature`,
`PROCESS recurrence`, "third instance", etc.) and found 13 raw hits across 13 files, of which 5
were genuine uncodified multi-instance patterns -- all 5 were folded into `/queue-experiment` and
`/failure-autopsy` the same day (commit 95fdc06). This script is the STANDING version of exactly
that mechanism: deterministic keyword/regex detection, never an LLM-judgment pipeline (that is
explicitly future work per the scoping doc, design decision 2 -- "a pure-keyword/heuristic version
... is cheaper but brittle" was accepted as the shape for THIS chip, not deferred entirely).

============================== DESIGN DECISIONS (dated 2026-08-01) ==========================

1. RECURRENCE THRESHOLD (design decision 1 in the scoping doc): SKILL_RECURRENCE_N = 2, matching
   GOV-GRAN-1's `GRAN_RECURRENCE_N`. Severity SUBSTITUTES for cross-file count in two ways, both
   observed directly in the real corpus during scoping:
     (a) STRONG_SEVERITY_PATTERNS ("PROCESS recurrence", "third instance", "third consecutive")
         -- an author who reaches for this language has already counted for us; a single such hit
         qualifies on its own.
     (b) EMBEDDED cross-references -- a `learning_extracted` sentence that itself cites >=2
         distinct short experiment-id tokens (e.g. "twice (569g + 684)", "(794, 845, 864)") is
         self-evidencing multi-instance recurrence within ONE entry; that also qualifies alone.
   Absent either signal, a cluster needs hits from >= N independent FILES (not just N items in one
   file) -- independence is what distinguishes a pattern from one verbose author.

2. DETECTION MECHANISM: regex/keyword self-flag matching over free text (see SELF_FLAG_PATTERNS),
   exactly the scoping doc's own sweep. Deliberately NOT semantic/LLM clustering -- that is a
   strict superset that would find more (the scoping doc says so explicitly) but is out of scope
   for this chip. Grouping hits that describe the SAME underlying issue into one candidate uses a
   cheap token-overlap heuristic (`cluster_hits`), not meaning -- expect false negatives (misses a
   real recurring pattern phrased two different ways) far more than false positives, which is the
   same trade the scoping doc's manual sweep made and documented as a "lower bound".

3. PROPOSE, NEVER AUTO-APPLY (design decision 3, hard requirement). This script is READ-ONLY on
   the autopsy corpus and `review_tracker.json`, and NEVER edits any `SKILL.md`. Its only writes
   are (a) its own pointer/state file (bookkeeping, see below) and (b) an optional generated
   markdown report a human reviews. Skills are shared, every-future-session, high-blast-radius
   files; the same live-edit-with-a-human-watching that worked for the scoping session's own two
   additions is not a safety net a standing unattended scan has.

4. PRUNING/CONSOLIDATION COUNTERPART (design decision 4). `audit_checklist_dormancy()` is a
   SEPARATE, best-effort, opt-in (`--check-dormancy`) pass: for a small curated set of
   MONITORED_CHECKLIST_SECTIONS (the exact sections this audit itself can add to), it reads each
   bullet, finds its first-introduction date via `git log -S`, and reports bullets older than
   DORMANCY_MONTHS with NO post-introduction hit (from this same run's own hit-detection) sharing
   its salient tokens. This reuses the detection machinery from design decision 2 rather than
   building a second one, per the "lightweight version is fine" instruction. It is informational
   ONLY (never strict-failing) -- an item with no post-addition hit may be genuinely dormant, or
   may simply never have been exercised; the script cannot tell those apart and does not pretend to.

5. EFFECTIVENESS-FEEDBACK HOOK (design decision 5). Folded into the SAME dormancy pass: when a
   monitored bullet DOES have a post-introduction hit whose salient tokens overlap it, that is
   reported as `recurring_despite_checklist` -- the pattern the item was written for is still
   showing up in autopsies authored after the item existed, which is either a sign the item is not
   being read/applied, or that it needs to be stated more forcefully. This is the honest,
   falsifiable half of "does this checklist item actually work" that the scoping doc asks for,
   built as a byproduct of the same hit-detection rather than a second subsystem.

============================== POINTER-BASED INCREMENTAL SCAN ===============================

Full-corpus glob is only ~300 files today and would be cheap to re-run every time -- but the chip
spec calls for incremental scanning explicitly, and the mechanism doubles as the accumulator that
makes cross-file threshold counting correct across separate invocations (a hit found in a 2026-06
file and a hit found in a 2026-08 file must both count toward the SAME cluster even though only
the second file was scanned on the most recent run). The state file
(`evidence/planning/skill_improvement_audit_pointer.json`, DEFAULT_POINTER_FILE) records, per
autopsy file, the mtime it was last scanned at, plus a flat list of every hit ever found (each hit
keyed by (artifact, target_index, item_index) or a content hash for review-tracker prose so
re-scanning is idempotent). A run only re-parses an autopsy file when it is new or its mtime
changed; already-scanned, unchanged files contribute their PERSISTED hits without being re-read.
Clustering and threshold-gating always run over the full accumulated hit set, never just the new
increment.

`evidence/planning/` is a CLAUDE.md "exposed file" for read-modify-write contamination (see
umbrella CLAUDE.md, Concurrency Rules). This pointer file is written ONLY by this script and only
additively (existing hit records are never rewritten, only merged-in by key), which bounds the
damage of a read-modify-write race to, at worst, a duplicate write of a hit this run already knew
about -- deduplicated on load by key, so idempotent. Still: re-read the file immediately before
writing (this script does), and commit it with `scripts/ree_commit.py`, per the umbrella rules.

REPORT OUTPUT (`--write-report [path]`, default DEFAULT_REPORT_PATH) is fully DERIVED from the
pointer state on every run -- safe to overwrite whole, unlike the pointer file itself, the same way
`pending_review.md` / `INDEX.md` are safe to regenerate in full.

Usage:
  python3 scripts/check_skill_improvement_recurrence.py                 # human report, exit 0
  python3 scripts/check_skill_improvement_recurrence.py --json
  python3 scripts/check_skill_improvement_recurrence.py --strict        # exit 1 if any candidate
  python3 scripts/check_skill_improvement_recurrence.py --write-report  # also write the markdown proposal
  python3 scripts/check_skill_improvement_recurrence.py --no-pointer    # scan fresh, do not persist state
  python3 scripts/check_skill_improvement_recurrence.py --check-dormancy  # also run the pruning/effectiveness pass
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
UMBRELLA_ROOT = REPO_ROOT.parent

DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"
DEFAULT_REVIEW_TRACKER = REPO_ROOT / "evidence" / "experiments" / "review_tracker.json"
DEFAULT_POINTER_FILE = REPO_ROOT / "evidence" / "planning" / "skill_improvement_audit_pointer.json"
DEFAULT_REPORT_PATH = REPO_ROOT / "evidence" / "planning" / "skill_improvement_audit_candidates.md"
DEFAULT_SKILLS_DIRS = [
    UMBRELLA_ROOT / ".claude" / "skills",
    UMBRELLA_ROOT / ".agents" / "skills",
]

# GOV-SKILL-1 recurrence threshold. See design decision 1 above.
SKILL_RECURRENCE_N = 2

# Minimum shared salient tokens for two hits to be considered the SAME underlying
# pattern (clustering), and for a cluster to be considered ALREADY represented in
# a skill file (already-codified exclusion). Same cheap heuristic both places.
#
# Raw intersection count alone is NOT enough: a long free-text entry (a governance
# review_log summary paragraph in particular) accumulates enough salient tokens by
# sheer length that it clears a raw-count floor against almost every other hit,
# acting as a transitive "hub" that unions together hits with nothing in common
# with EACH OTHER (confirmed empirically 2026-08-01 -- a 90-token governance
# summary note chained 10 unrelated autopsy hits into one cluster at
# MIN_SHARED_TOKENS=2 with no Jaccard floor). MIN_JACCARD normalizes by set size
# so a big blob's incidental overlap with a small, specific entry is rejected
# (small numerator / large denominator), while two similarly-sized, genuinely
# overlapping entries still clear it. Both floors apply together: raw count
# guards against two tiny sets matching on a coincidental pair of words; Jaccard
# guards against a big set dominating by size alone.
# Calibrated against the real corpus 2026-08-01: the flagship genuine pair (the
# seed-44-truncation duplicate, EXQ-539-540 / V3-EXQ-538a -- 2 shared tokens,
# Jaccard 0.143) must clear the bar; the confirmed spurious "hub" pairs (a long
# review_log governance-cycle summary against two unrelated single-topic autopsy
# hits -- Jaccard 0.030 and 0.064 despite 4-9 raw shared tokens) must not. 0.12
# sits strictly between them with margin on both sides.
MIN_SHARED_TOKENS = 2
MIN_JACCARD = 0.12
# Roster guard for the EMBEDDED-ID union path in cluster_hits() (design decision
# 1(b)): a hit whose OWN embedded_ids set is larger than this is a ROSTER --
# ordinary bookkeeping enumerating many run numbers (a governance
# `review_log[].note` cycle summary: "confirmed autopsies for 843/847/853/...")
# -- not a focused citation, and does not participate in the id-based fast-path
# union at all (with either side over the cap, that path is skipped and only
# the token/jaccard test can still cluster the pair).
#
# Confirmed 2026-08-22 (chip-20260822-govskill1-clustering-mega-cluster-diagnosis):
# under the OLD unconditional "if ei & ej: union" rule, ANY autopsy hit whose own
# run number happens to appear anywhere in such a roster unioned with it -- not
# because the two describe the same pattern, but because the run was processed
# in that governance cycle. That is precisely the transitive "hub" failure
# MIN_JACCARD was built to reject for TOKEN overlap (see MIN_CODIFIED_OVERLAP
# below), but the id path had no analogous guard, and it chained an 11-hit
# mega-cluster (a genuine 2-hit zworld_p0_episodes recurrence plus 9 unrelated
# hits pulled in via 4 review_log rosters) whose diluted pooled vocabulary then
# made already_codified() match the WRONG skill line -- an unrelated GENERIC
# governance paragraph, instead of the actual fix.
#
# Measured: every autopsy hit's own embedded_ids set in the live corpus tops
# out at 5 members; every review_log roster starts at 18+. A cap of 8 cleanly
# separates the two shapes with margin on both sides -- deliberately a SIZE cap
# on the citing entry, not a SHARED-count floor (a stricter shared-count floor
# was tried first and rejected: it also breaks the genuine
# failure_autopsy_V3-EXQ-643_2026-06-06 / ..._916-916a-917-920-fishtank-cluster
# pair, which are both small, non-roster entries that legitimately share only
# ONE explicitly-named "canonical V3-EXQ-642" cross-reference -- structurally
# identical, on the shared-id-COUNT signal alone, to the confirmed-spurious
# V3-EXQ-861/864 pair below, so a count floor cannot separate them but a
# roster-size cap does, since neither is a roster).
MAX_EMBEDDED_IDS_FOR_ROSTER = 8
# Matching is done on NORMALIZED ids (EXQ-prefix stripped), not raw strings --
# a bare "642" in one hit and a prefixed "V3-EXQ-642" in another are the SAME
# citation and must still bridge (see _normalized_id_tail). The raw,
# prefix-preserving form from embedded_reference_ids() is kept as each hit's
# stored `embedded_ids` (needed by cluster_qualifies()'s own distinct-id COUNT,
# which must NOT collapse two genuinely different ids), so normalization is
# applied only at match time here, not at extraction time.
#
# One accepted residual: V3-EXQ-861 (MECH-180 ceiling-status re-scoring) and
# V3-EXQ-864 (a driver-parameter sweep defect) share nothing but both citing
# prior run "845" in passing, for unrelated reasons, and neither is roster-sized
# -- so they still union under this design. Checked (not just assumed): the
# resulting 2-hit cluster's already_codified() match is 861's own correct line
# (failure-autopsy/SKILL.md, the V3-EXQ-861 ceiling-staleness passage), not a
# wrong-file mismatch -- 861's overlap dominates the small pooled vocabulary.
# So the merge is mildly imprecise (864's own separate, also-correct match is
# not separately surfaced) rather than actively wrong, which is the same
# "expect false negatives more than false positives" brittleness the module's
# own design decision 2 already accepts. This is DELIBERATELY not solved here:
# distinguishing an explicit "canonical" cross-reference from an incidental
# parenthetical mention needs a signal this bag-of-words heuristic does not
# have, and over-fitting the threshold to this one pair risks the SAME
# regression that rejecting the shared-count-floor alternative above avoided.
#
# CORRECTION to the design-decision comment below, which is now WRONG: the
# "861+864+review_log" cluster it names as a 2026-08-01 calibration example of a
# confirmed-genuine already-codified match was itself built on the unguarded
# roster-hub union this cap removes -- 861 and 864 are not the same underlying
# pattern, and the review_log entry joined only via roster bookkeeping, not
# shared content. MIN_CODIFIED_OVERLAP/MIN_CODIFIED_FRACTION were validated
# against a cluster that should never have existed. Left uncorrected in place
# below (rather than rewritten) because the FRACTION/OVERLAP calibration itself
# is independent of this fix and remains valid against the corpus's other
# confirmed cases; only the specific cited example was wrong.
_ID_PREFIX_RE = re.compile(r"^(?:v3-)?exq-?", re.IGNORECASE)


def _normalized_id_tail(ref_id: str) -> str:
    """Strip an EXQ-family prefix so 'v3-exq-642' and '642' compare equal.

    Used ONLY for cross-hit id MATCHING in cluster_hits() -- never applied to
    the raw `embedded_ids` stored on a hit, which stays prefix-preserving so
    cluster_qualifies()'s distinct-id count is unaffected.
    """
    return _ID_PREFIX_RE.sub("", ref_id)
# Already-codified matching is asymmetric vs clustering: a SKILL.md bullet is
# routinely a long paragraph (tens to 100+ salient tokens), so raw overlap alone
# lets a long line match almost anything at a low floor by sheer size, and a pure
# fraction-of-cluster-vocabulary floor over-penalizes a large, multi-hit cluster
# (whose pooled vocabulary is itself large) even when its raw overlap with the
# matching line is substantial. Overlap >= 5 AND overlap covering >= 12% of the
# CLUSTER's own vocabulary together reject the worst coincidental matches
# confirmed 2026-08-01 (V3-EXQ-629 / V3-EXQ-603m / V3-EXQ-828a each spuriously
# "matched" an unrelated long paragraph at overlap 3-4) while still passing
# every confirmed-genuine match, including the large 3-hit 861+864+review_log
# cluster (overlap=21 but only 14% of its 150-token pooled vocabulary, because
# the review_log entry alone is a whole governance-cycle summary) -- SEE THE
# CORRECTION ABOVE: that cluster is itself a confirmed false merge, not a
# genuine example; it is cited here only because that is what was believed true
# at calibration time. KNOWN RESIDUAL FALSE POSITIVE: V3-EXQ-708 still
# spuriously matches an unrelated pre-push-hook paragraph (overlap=6,
# fraction=0.30) on generic shared words ("cloud", "workers", "phase") -- this
# is the accepted brittleness of a bag-of-words heuristic over free text (design
# decision 2), not something this chip tries to eliminate entirely. Because the
# report always names the matched skill_file:line and quotes it, a human
# reviewing the "already codified" bucket can catch a mismatch like this one at
# a glance -- that human review is the actual safety net (design decision 3),
# not the heuristic's precision.
MIN_CODIFIED_OVERLAP = 5
MIN_CODIFIED_FRACTION = 0.12

# Dormancy pass: a monitored checklist bullet older than this with no matching
# post-introduction hit is surfaced as a prune candidate.
DORMANCY_MONTHS = 3

# --- self-flagged-repeat detection -------------------------------------------
# The exact mechanism the scoping doc's one-off sweep used, kept close to its own
# examples. High precision, low recall by design (misses patterns an author never
# explicitly called out as recurring) -- see design decision 2.
SELF_FLAG_PATTERNS: dict[str, re.Pattern] = {
    "recurring": re.compile(r"\brecurring\b", re.IGNORECASE),
    "recurs": re.compile(r"\brecurs\b", re.IGNORECASE),
    "twice": re.compile(r"\btwice\b", re.IGNORECASE),
    "same_signature": re.compile(r"same signature", re.IGNORECASE),
    "process_recurrence": re.compile(r"PROCESS recurrence", re.IGNORECASE),
    "third_instance": re.compile(r"\bthird instance\b", re.IGNORECASE),
    "third_consecutive": re.compile(r"third consecutive", re.IGNORECASE),
    "repeated": re.compile(r"\brepeated(?:ly)?\b", re.IGNORECASE),
}

# Design decision 1(a): a single hit carrying one of these already asserts >=2
# occurrences in the author's own words -- qualifies without needing a 2nd file.
STRONG_SEVERITY_PATTERNS = {"process_recurrence", "third_instance", "third_consecutive"}

# Design decision 1(b): short RUN/experiment-id-shaped tokens cited together in
# one sentence are a self-evidencing cross-reference (e.g. "twice (569g + 684)").
# Deliberately EXQ-only, not MECH/ARC/SD/INV/GAP/Q -- those are CLAIM prefixes,
# and two DIFFERENT findings routinely cite the SAME claim (it is what
# `claim_ids` is for); matching them here would treat ordinary co-tagging as
# self-evidenced recurrence. Confirmed 2026-08-01: V3-EXQ-614c and V3-EXQ-629
# both cite MECH-341 (as the claim their own finding bears on) and were
# incorrectly clustered on that basis alone before this prefix was narrowed --
# the two findings share no other vocabulary and are not the same pattern.
_PREFIXED_ID_RE = re.compile(r"\b(?:V3-)?EXQ-?\d{2,4}[a-z]?\b", re.IGNORECASE)
# Bare 3-digit shorthand (the corpus's own convention: "569g", "684", "794").
# The trailing \b means a 4-digit token (e.g. a year) can never match this as a
# substring -- there is no word-boundary between digit 3 and digit 4 of "2026".
_BARE_ID_RE = re.compile(r"\b\d{3}[a-z]?\b")


def embedded_reference_ids(text: str) -> set[str]:
    """Short RUN/experiment-id-shaped tokens cited in one sentence (EXQ-family
    and bare 3-digit shorthand only -- see _PREFIXED_ID_RE for why claim
    prefixes are excluded).

    Returns a normalized (lowercased) set. Two or more distinct ids is treated as
    the author self-evidencing recurrence within a single entry (design decision
    1(b)). This is a heuristic over free text -- it will occasionally catch a
    coincidental 3-digit number that is not an experiment id (a dose, a percent).
    That is an accepted false-positive rate for a WARN-only, human-reviewed audit;
    see module docstring design decision 2. Callers should additionally subtract
    `claim_id_numeric_parts(claim_ids)` -- see that function's docstring for why
    the bare-number regex alone cannot tell a run citation from the target's OWN
    claim tag.

    A bare-digit match that falls INSIDE a prefixed match's own span is dropped
    rather than counted as a second, distinct id. Without this, a single
    citation like "V3-EXQ-642" registers as TWO ids ("v3-exq-642" AND "642",
    since `_BARE_ID_RE` also matches the trailing digits of the prefixed form),
    silently satisfying the ">= 2 distinct ids" self-evidencing test off ONE
    citation. Confirmed 2026-08-22 (chip-20260822-govskill1-clustering-mega-cluster-diagnosis):
    `failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12`'s only
    citation is "canonical V3-EXQ-642" and it was passing `cluster_qualifies()`
    as if it cited two separate runs.
    """
    prefixed_spans = [pm.span() for pm in _PREFIXED_ID_RE.finditer(text)]
    ids = {text[s:e].lower() for s, e in prefixed_spans}
    for bm in _BARE_ID_RE.finditer(text):
        s, e = bm.span()
        if any(ps <= s and e <= pe for ps, pe in prefixed_spans):
            continue
        ids.add(bm.group(0).lower())
    return ids


_CLAIM_NUMERIC_RE = re.compile(r"\d+[a-z]?$", re.IGNORECASE)


def claim_id_numeric_parts(claim_ids: list[str]) -> set[str]:
    """The bare numeric+letter tail of each claim id (e.g. "MECH-341" -> "341").

    `_BARE_ID_RE` cannot distinguish a genuine cross-referenced RUN number
    ("569g", "684") from the plain numeric tail of the hit's OWN claim tag
    ("MECH-341" contains a boundaried "341"). Since a target's `claim_ids` is
    structural (nearly every hit cites one) and NOT evidence of the author
    self-citing multiple prior incidents, those tails must be subtracted from
    `embedded_reference_ids(text)` before it is used as a recurrence signal.
    Confirmed 2026-08-01: V3-EXQ-614c and V3-EXQ-629 both tag MECH-341 and were
    incorrectly linked on "341" alone before this subtraction was added -- the
    two findings share no other vocabulary and are not the same pattern.
    """
    out: set[str] = set()
    for cid in claim_ids:
        m = _CLAIM_NUMERIC_RE.search(cid)
        if m:
            out.add(m.group(0).lower())
    return out


def match_self_flags(text: str) -> list[str]:
    """Names of every SELF_FLAG_PATTERNS entry that matches `text`."""
    return [name for name, pat in SELF_FLAG_PATTERNS.items() if pat.search(text)]


# --- salient-token extraction (cheap clustering + already-codified check) ----

# Common English stopwords plus REE-domain words generic enough to appear in
# nearly every hit (which would cause spurious cross-pattern merges), plus the
# self-flag vocabulary itself (excluded so two hits do not "cluster" merely
# because both say "recurring").
_STOPWORDS = frozenset("""
about above across after again against all also although always among another
any anyone anything around because before being between both cannot could
during each either every everything first found further given have having
here however into itself later least likely little maybe might more most much
never night nobody normal nothing often other others rather really second
should since some something still such than that their them then there these
they third this those though through toward under until upon using while
which whose within without would across after against being cannot could
during either found further given having however itself least likely little
maybe might nobody normal nothing often other others rather really should
since something such their there these they this those though through toward
under until upon using which whose within without would recommended reading
result results evidence experiment experiments running confirmed observed
occurs occurred instance instances consecutive repeated signature recurring
recurs recurrence twice claim claims direction category
""".split()) | {
    # Claim/experiment-id PREFIXES, not content words. "MECH-063", "V3-EXQ-538a"
    # etc. tokenize their leading letters as a bare "mech"/"exq" once the
    # trailing hyphen is stripped (see extract_salient_tokens docstring), and
    # because claim tags are cited in nearly every entry, an unfiltered "mech"
    # token alone chained three otherwise-unrelated hits into one false cluster
    # (confirmed 2026-08-01: MECH-063-777a-779a-cluster / V3-EXQ-614c / V3-EXQ-629
    # shared nothing but "mech" pairwise, yet the transitive closure merged all
    # three). "exq"/"arc"/"inv"/"sd"/"gap" are the same shape but already below
    # the 4-char floor and so never reach here; "mech" is kept explicit because
    # it is the one prefix that clears it.
    "mech",
}

_TOKEN_RE = re.compile(r"[a-zA-Z][a-zA-Z_-]{3,}")


def extract_salient_tokens(text: str) -> set[str]:
    """Lowercased distinctive words (len >= 4 after stripping), minus stopwords.

    Deliberately coarse -- a bag-of-words overlap, not embeddings or stemming.
    Good enough to notice "seed-44 truncation ... reef-config" recurring across
    two files phrased almost identically; not intended to catch a pattern
    described in genuinely different vocabulary (design decision 2 accepts this).

    Trailing/leading `-`/`_` are stripped post-match so "seed-44" (hyphen
    swallowed by the token class, digits dropped) normalizes to the same token
    as "seed" or "3-seed" -- confirmed necessary: without this strip,
    "Seed-44 truncation ..." tokenizes its lead word as "seed-" while
    "Seed44 truncation ..." tokenizes as "seed", and the two never overlap
    despite being the same underlying reference (the flagship seed-44
    truncation pair from the 2026-08-01 scoping sweep, EXQ-539-540 /
    V3-EXQ-538a). The length floor is applied AFTER stripping so a token is
    only kept once it is >= 4 real letters (the un-stripped regex over-admits
    down to 4 raw chars including a trailing separator).
    """
    out: set[str] = set()
    for m in _TOKEN_RE.finditer(text):
        tok = m.group(0).lower().strip("-_")
        if len(tok) >= 4 and tok not in _STOPWORDS:
            out.add(tok)
    return out


# --- hit collection: failure_autopsy_*.json -----------------------------------

def _load_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def scan_autopsy_file(path: Path) -> list[dict]:
    """Every self-flagged-repeat `learning_extracted` item in one confirmed autopsy.

    Returns a list of raw hit dicts (source="autopsy"). Non-confirmed artifacts and
    unparseable files yield nothing (matches every sibling scan's convention).
    """
    data = _load_json(path)
    if not isinstance(data, dict):
        return []
    if str(data.get("status", "")).strip().lower() != "confirmed":
        return []
    hits: list[dict] = []
    for ti, tgt in enumerate(data.get("targets") or []):
        if not isinstance(tgt, dict):
            continue
        claim_ids = [str(c).strip() for c in (tgt.get("claim_ids") or []) if str(c).strip()]
        for li, item in enumerate(tgt.get("learning_extracted") or []):
            if not isinstance(item, str) or not item.strip():
                continue
            flags = match_self_flags(item)
            if not flags:
                continue
            own_claim_numerics = claim_id_numeric_parts(claim_ids)
            hits.append({
                "source": "autopsy",
                "artifact": path.stem,
                "target_index": ti,
                "item_index": li,
                "run_id": str(tgt.get("run_id") or tgt.get("queue_id") or ""),
                "claim_ids": claim_ids,
                "text": item,
                "flags": flags,
                "strong_severity": bool(set(flags) & STRONG_SEVERITY_PATTERNS),
                "embedded_ids": sorted(embedded_reference_ids(item) - own_claim_numerics),
                "tokens": sorted(extract_salient_tokens(item)),
            })
    return hits


# --- hit collection: review_tracker.json --------------------------------------

def _review_hit_key(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]


def scan_review_tracker(path: Path) -> list[dict]:
    """Self-flagged-repeat prose in `review_log[].context` (+ its `note` alias --
    the field was renamed mid-corpus, both are mined, see docstring) and the
    top-level `discussion_notes[]` list.
    """
    data = _load_json(path)
    if not isinstance(data, dict):
        return []
    hits: list[dict] = []

    for idx, entry in enumerate(data.get("review_log") or []):
        if not isinstance(entry, dict):
            continue
        for field in ("context", "note"):
            text = entry.get(field)
            if not isinstance(text, str) or not text.strip():
                continue
            flags = match_self_flags(text)
            if not flags:
                continue
            entry_claim_ids = [str(c) for c in (entry.get("claim_ids_touched") or [])]
            own_claim_numerics = claim_id_numeric_parts(entry_claim_ids)
            hits.append({
                "source": "review_tracker",
                "artifact": f"review_log[{idx}].{field}",
                "target_index": idx,
                "item_index": 0,
                "run_id": str(entry.get("utc") or ""),
                "claim_ids": entry_claim_ids,
                "text": text,
                "flags": flags,
                "strong_severity": bool(set(flags) & STRONG_SEVERITY_PATTERNS),
                "embedded_ids": sorted(embedded_reference_ids(text) - own_claim_numerics),
                "tokens": sorted(extract_salient_tokens(text)),
                "hash": _review_hit_key(text),
            })

    for i, text in enumerate(data.get("discussion_notes") or []):
        if not isinstance(text, str) or not text.strip():
            continue
        flags = match_self_flags(text)
        if not flags:
            continue
        hits.append({
            "source": "review_tracker",
            "artifact": f"discussion_notes[{i}]",
            "target_index": i,
            "item_index": 0,
            "run_id": "",
            "claim_ids": [],
            "text": text,
            "flags": flags,
            "strong_severity": bool(set(flags) & STRONG_SEVERITY_PATTERNS),
            "embedded_ids": sorted(embedded_reference_ids(text)),
            "tokens": sorted(extract_salient_tokens(text)),
            "hash": _review_hit_key(text),
        })
    return hits


def _hit_key(hit: dict) -> str:
    """Stable dedup key for the pointer accumulator."""
    if hit["source"] == "autopsy":
        return f"autopsy|{hit['artifact']}|{hit['target_index']}|{hit['item_index']}"
    return f"review_tracker|{hit['artifact']}|{hit.get('hash', '')}"


# --- pointer state (incremental scan bookkeeping) -----------------------------

def load_pointer(path: Path) -> dict:
    data = _load_json(path) if path.exists() else None
    if not isinstance(data, dict):
        return {"schema_version": "v1", "last_swept_at": None,
                "seen_autopsy_mtimes": {}, "seen_review_tracker_mtime": None,
                "hits_by_key": {}}
    data.setdefault("seen_autopsy_mtimes", {})
    data.setdefault("seen_review_tracker_mtime", None)
    data.setdefault("hits_by_key", {})
    return data


def save_pointer(path: Path, state: dict) -> None:
    # Re-read immediately before writing (per umbrella CLAUDE.md concurrency
    # rules for evidence/planning/) and merge additively -- never blind-overwrite
    # another run's accumulated hits. Both writers converge to the same
    # keyed-union regardless of interleaving, so this is safe under the ordinary
    # single-writer-at-a-time cadence this standing scan runs at.
    fresh = load_pointer(path)
    merged_hits = dict(fresh.get("hits_by_key") or {})
    merged_hits.update(state.get("hits_by_key") or {})
    merged_mtimes = dict(fresh.get("seen_autopsy_mtimes") or {})
    merged_mtimes.update(state.get("seen_autopsy_mtimes") or {})
    out = {
        "schema_version": "v1",
        "last_swept_at": state.get("last_swept_at"),
        "seen_autopsy_mtimes": merged_mtimes,
        "seen_review_tracker_mtime": state.get("seen_review_tracker_mtime"),
        "hits_by_key": merged_hits,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def collect_hits(autopsy_dir: Path, review_tracker: Path, pointer: dict,
                  full_rescan: bool = False) -> tuple[list[dict], dict]:
    """Incrementally scan for new hits, return the FULL accumulated hit set.

    Only autopsy files that are new or whose mtime changed since the pointer's
    last record are re-parsed; everything else contributes its persisted hits
    unchanged. review_tracker.json is a single evolving file -- re-scanned
    whenever its mtime changes (append-only growth in practice, so this stays
    cheap), with per-item content-hash keys making the merge idempotent even if
    entries are reordered.
    """
    seen_mtimes = dict(pointer.get("seen_autopsy_mtimes") or {})
    hits_by_key = dict(pointer.get("hits_by_key") or {})

    if autopsy_dir.is_dir():
        for fp in sorted(autopsy_dir.glob("failure_autopsy_*.json")):
            mtime = fp.stat().st_mtime
            prior = seen_mtimes.get(fp.name)
            if not full_rescan and prior is not None and prior == mtime:
                continue
            for hit in scan_autopsy_file(fp):
                hits_by_key[_hit_key(hit)] = hit
            seen_mtimes[fp.name] = mtime

    rt_mtime = review_tracker.stat().st_mtime if review_tracker.exists() else None
    prior_rt = pointer.get("seen_review_tracker_mtime")
    if full_rescan or rt_mtime != prior_rt:
        for hit in scan_review_tracker(review_tracker):
            hits_by_key[_hit_key(hit)] = hit

    new_pointer = {
        "schema_version": "v1",
        "last_swept_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "seen_autopsy_mtimes": seen_mtimes,
        "seen_review_tracker_mtime": rt_mtime,
        "hits_by_key": hits_by_key,
    }
    return list(hits_by_key.values()), new_pointer


# --- clustering ----------------------------------------------------------------

class _UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


def cluster_hits(hits: list[dict], min_shared_tokens: int = MIN_SHARED_TOKENS,
                 min_jaccard: float = MIN_JACCARD,
                 max_embedded_ids_for_roster: int = MAX_EMBEDDED_IDS_FOR_ROSTER) -> list[list[dict]]:
    """Group hits describing the same underlying pattern.

    Two hits join a cluster when they share >= min_shared_tokens salient tokens
    AND the Jaccard similarity of their token sets is >= min_jaccard (see
    MIN_JACCARD docstring for why raw count alone over-clusters), OR when they
    share a NORMALIZED embedded reference id (design decision 1(b) -- if two
    entries both cite "684", whether bare or as "V3-EXQ-684", they are
    plausibly about the same incident, regardless of how their prose is
    worded) AND NEITHER hit's own embedded_ids set is roster-sized (see
    MAX_EMBEDDED_IDS_FOR_ROSTER docstring for the confirmed false merges a
    roster-mediated union let through, and why a shared-count floor was tried
    and rejected in favor of this size cap). Cheap O(n^2) union-find; the
    corpus of SELF-FLAGGED hits is small (dozens, not thousands) so this is not
    a performance concern.
    """
    n = len(hits)
    uf = _UnionFind(n)
    normalized_ids = [{_normalized_id_tail(x) for x in hits[i]["embedded_ids"]}
                      for i in range(n)]
    is_roster = [len(hits[i]["embedded_ids"]) > max_embedded_ids_for_roster
                for i in range(n)]
    for i in range(n):
        ti = set(hits[i]["tokens"])
        for j in range(i + 1, n):
            tj = set(hits[j]["tokens"])
            if (not is_roster[i] and not is_roster[j]
                    and normalized_ids[i] & normalized_ids[j]):
                uf.union(i, j)
                continue
            inter = ti & tj
            if len(inter) < min_shared_tokens:
                continue
            union_size = len(ti | tj) or 1
            if (len(inter) / union_size) >= min_jaccard:
                uf.union(i, j)
    groups: dict[int, list[dict]] = {}
    for i, hit in enumerate(hits):
        groups.setdefault(uf.find(i), []).append(hit)
    return list(groups.values())


def cluster_qualifies(cluster: list[dict], n: int = SKILL_RECURRENCE_N) -> tuple[bool, str]:
    """Whether a cluster crosses the recurrence bar. Returns (qualifies, reason)."""
    if any(h["strong_severity"] for h in cluster):
        return True, "strong self-flag (PROCESS recurrence / third instance / third consecutive)"
    # Design decision 1(b) is scoped, by its own docstring, to "a `learning_extracted`
    # sentence" -- i.e. an AUTOPSY hit's own focused finding, not a review_tracker
    # `review_log[].note`. A review_log entry is a governance-cycle bookkeeping
    # summary that routinely enumerates 15-50 run ids as a matter of course (every
    # item processed that cycle), so an unscoped check here would make EVERY such
    # note self-qualify as an "actionable" candidate regardless of content.
    # Confirmed 2026-08-22 (chip-20260822-govskill1-clustering-mega-cluster-diagnosis):
    # once cluster_hits()'s roster-hub over-merging was fixed (MAX_EMBEDDED_IDS_FOR_ROSTER),
    # `review_log[89].note` immediately surfaced standalone this way -- a new false
    # positive the mega-cluster had been incidentally (and wrongly) masking.
    if any(len(h["embedded_ids"]) >= n for h in cluster if h.get("source") == "autopsy"):
        return True, f"single entry cites >= {n} distinct experiment/claim ids"
    n_files = len({h["artifact"].split("[")[0].split(".")[0] for h in cluster})
    if n_files >= n:
        return True, f"{n_files} independent artifacts"
    return False, f"only {n_files} independent artifact(s), no strong self-flag or embedded ids"


# --- already-codified check against the live skill files ----------------------

def load_skill_lines(skills_dirs: list[Path]) -> list[dict]:
    """Every non-trivial line of every SKILL.md, with its salient tokens."""
    out: list[dict] = []
    for skills_dir in skills_dirs:
        if not skills_dir.is_dir():
            continue
        for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
            try:
                text = skill_md.read_text(encoding="utf-8")
            except OSError:
                continue
            rel = f"{skills_dir.name}/{skill_md.parent.name}/SKILL.md"
            for lineno, line in enumerate(text.splitlines(), 1):
                toks = extract_salient_tokens(line)
                if len(toks) < MIN_CODIFIED_OVERLAP:
                    continue
                out.append({"skill_file": rel, "line": lineno, "text": line.strip(),
                           "tokens": toks})
    return out


def already_codified(cluster: list[dict], skill_lines: list[dict],
                     min_overlap: int = MIN_CODIFIED_OVERLAP,
                     min_fraction: float = MIN_CODIFIED_FRACTION) -> dict | None:
    """Best-matching skill line for a cluster's pooled tokens, if any clears the bar.

    Both floors must clear -- see MIN_CODIFIED_OVERLAP for why raw overlap alone
    is not enough against long skill paragraphs.
    """
    pooled: set[str] = set()
    for h in cluster:
        pooled |= set(h["tokens"])
    if not pooled:
        return None
    best = None
    best_overlap = 0
    for sl in skill_lines:
        overlap = len(pooled & sl["tokens"])
        if overlap > best_overlap:
            best_overlap = overlap
            best = sl
    if (best is not None and best_overlap >= min_overlap
            and (best_overlap / len(pooled)) >= min_fraction):
        # Exclude "tokens" (a set) -- this dict flows into --json output, and a
        # raw set is not JSON serializable. Nothing downstream reads it.
        return {k: v for k, v in best.items() if k != "tokens"} | {"overlap": best_overlap}
    return None


# --- top-level audit -------------------------------------------------------------

def audit(hits: list[dict], skill_lines: list[dict],
          n: int = SKILL_RECURRENCE_N) -> dict[str, list]:
    clusters = cluster_hits(hits)
    candidates, excluded, sub_threshold = [], [], []
    for cluster in clusters:
        qualifies, reason = cluster_qualifies(cluster, n=n)
        record = {
            "artifacts": sorted({h["artifact"] for h in cluster}),
            "n_hits": len(cluster),
            "flags": sorted({f for h in cluster for f in h["flags"]}),
            "embedded_ids": sorted({i for h in cluster for i in h["embedded_ids"]}),
            "sample_text": cluster[0]["text"],
            "qualifies_reason": reason,
        }
        if not qualifies:
            sub_threshold.append(record)
            continue
        codified = already_codified(cluster, skill_lines)
        if codified:
            excluded.append({**record, "excluded_reason": "already_codified",
                             "codified_in": codified})
        else:
            candidates.append({**record, "tier": "checklist_candidate"})
    candidates.sort(key=lambda r: (-r["n_hits"], r["artifacts"][0] if r["artifacts"] else ""))
    excluded.sort(key=lambda r: (-r["n_hits"], r["artifacts"][0] if r["artifacts"] else ""))
    sub_threshold.sort(key=lambda r: (-r["n_hits"], r["artifacts"][0] if r["artifacts"] else ""))
    return {"checklist_candidates": candidates, "excluded_already_codified": excluded,
            "sub_threshold": sub_threshold}


# --- design decisions 4 + 5: dormancy / effectiveness-feedback (opt-in) -------

# The exact sections this audit's own candidates would be folded into. Curated,
# not auto-discovered -- keeps the dormancy pass narrow and its meaning legible
# (see design decision 4: this is intentionally the lightweight version).
# Header text is matched against each skill's OWN numbering convention, not a
# generic "Step N" pattern -- confirmed 2026-08-01 that the three skills do not
# share one: queue-experiment numbers its markdown headers "### 3.5. Code review
# pass ..."; failure-autopsy numbers its own headers "### 3. Map to the claim
# layer" / "### 5. Four-layer diagnosis" (no "Step" word); governance's Step 2b
# is a BOLD in-paragraph sub-item ("**2b. Present findings ...**") inside its
# "### 2. Walk pending experiments" header, not a header of its own, so it is
# NOT reachable by this header-scoped extractor and is deliberately left off
# this list rather than silently matched incorrectly. If governance's Step 2b
# checklist growth needs monitoring, that needs a bold-marker extractor, not a
# fix to the regex here -- out of scope for this chip (design decision 4/5 asks
# for the lightweight version).
MONITORED_CHECKLIST_SECTIONS = [
    {"skill": "queue-experiment", "header_re": re.compile(r"^#+\s*3\.5\.", re.IGNORECASE)},
    {"skill": "failure-autopsy", "header_re": re.compile(r"^#+\s*3\.\s", re.IGNORECASE)},
    {"skill": "failure-autopsy", "header_re": re.compile(r"^#+\s*5\.\s", re.IGNORECASE)},
]

_BULLET_RE = re.compile(r"^\s*[-*]\s+(.*\S)\s*$")


def extract_monitored_bullets(skills_dir: Path) -> list[dict]:
    """Bullets under each MONITORED_CHECKLIST_SECTIONS header, for one skills dir."""
    out: list[dict] = []
    for section in MONITORED_CHECKLIST_SECTIONS:
        skill_md = skills_dir / section["skill"] / "SKILL.md"
        if not skill_md.exists():
            continue
        try:
            lines = skill_md.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        in_section = False
        for lineno, line in enumerate(lines, 1):
            if line.startswith("#"):
                if section["header_re"].match(line):
                    in_section = True
                    continue
                if in_section:
                    break  # next header ends the section
                continue
            if not in_section:
                continue
            m = _BULLET_RE.match(line)
            if m:
                out.append({"skill": section["skill"], "file": str(skill_md),
                           "line": lineno, "text": m.group(1)})
    return out


def first_seen_date(repo_root: Path, rel_path: str, snippet: str) -> str | None:
    """First commit (oldest) introducing `snippet` into `rel_path`, ISO date or None.

    Best-effort git pickaxe (-S). Never raises -- git absence/failure just means
    the dormancy check is skipped for that bullet (fails open to "unknown", the
    same safe-direction posture the rest of this audit uses).
    """
    probe = snippet.strip()[:60]
    if not probe:
        return None
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_root), "log", "--follow", "--format=%aI",
             "--reverse", "-S", probe, "--", rel_path],
            capture_output=True, text=True, timeout=30, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    lines = [ln for ln in out.stdout.splitlines() if ln.strip()]
    return lines[0] if lines else None


def _months_since(iso_date: str) -> float | None:
    try:
        dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    except ValueError:
        return None
    now = datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return (now - dt).days / 30.44


def dormancy_verdict(bullet_tokens: set[str], months_old: float,
                     post_intro_hits: list[dict],
                     dormancy_months: float = DORMANCY_MONTHS) -> str | None:
    """Pure logic (no git, no filesystem) -- easy to unit test directly.

    Returns None if the bullet is not old enough to judge yet, else one of
    "recurring_despite_checklist" or "no_post_addition_recurrence_detected".
    """
    if months_old < dormancy_months:
        return None
    for h in post_intro_hits:
        if len(bullet_tokens & set(h.get("tokens") or [])) >= MIN_SHARED_TOKENS:
            return "recurring_despite_checklist"
    return "no_post_addition_recurrence_detected"


def audit_checklist_dormancy(skills_dirs: list[Path], all_hits: list[dict],
                             dormancy_months: float = DORMANCY_MONTHS) -> list[dict]:
    """Best-effort wrapper wiring git dates + collected hits into dormancy_verdict."""
    results: list[dict] = []
    seen_bullets: set[tuple[str, str]] = set()
    for skills_dir in skills_dirs:
        if not skills_dir.is_dir():
            continue
        for bullet in extract_monitored_bullets(skills_dir):
            key = (bullet["skill"], bullet["text"][:80])
            if key in seen_bullets:
                continue
            seen_bullets.add(key)
            rel = str(Path(bullet["file"]).relative_to(skills_dir.parent.parent))
            date = first_seen_date(skills_dir.parent.parent, rel, bullet["text"])
            if date is None:
                continue
            months_old = _months_since(date)
            if months_old is None:
                continue
            btoks = extract_salient_tokens(bullet["text"])
            post_hits = [h for h in all_hits if h.get("date", "") > date] if any(
                "date" in h for h in all_hits) else all_hits  # date not tracked per-hit today
            verdict = dormancy_verdict(btoks, months_old, post_hits, dormancy_months)
            if verdict:
                results.append({**bullet, "first_seen": date,
                               "months_old": round(months_old, 1), "verdict": verdict})
    return results


# --- report rendering ------------------------------------------------------------

def render_report(result: dict) -> str:
    lines = ["# Skill-improvement recurrence audit (GOV-SKILL-1)", ""]
    lines.append("Generated by `REE_assembly/scripts/check_skill_improvement_recurrence.py`. "
                 "READ-ONLY over the corpus; this file is fully regenerated each run and is a "
                 "PROPOSAL for a human to review -- it edits no SKILL.md.")
    lines.append("")
    cands = result["checklist_candidates"]
    lines.append(f"## Checklist candidates ({len(cands)})")
    lines.append("")
    if not cands:
        lines.append("None -- no unflagged, uncodified recurrence cleared the bar this sweep.")
    for r in cands:
        lines.append(f"- **{', '.join(r['artifacts'])}** ({r['n_hits']} hit(s); "
                     f"{r['qualifies_reason']})")
        lines.append(f"  - sample: {r['sample_text']}")
    lines.append("")
    exc = result["excluded_already_codified"]
    lines.append(f"## Already codified ({len(exc)})")
    lines.append("")
    for r in exc:
        cf = r["codified_in"]
        lines.append(f"- **{', '.join(r['artifacts'])}** -- see `{cf['skill_file']}`:{cf['line']}")
    lines.append("")
    return "\n".join(lines) + "\n"


# --- CLI -----------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR)
    ap.add_argument("--review-tracker", type=Path, default=DEFAULT_REVIEW_TRACKER)
    ap.add_argument("--pointer-file", type=Path, default=DEFAULT_POINTER_FILE)
    ap.add_argument("--skills-dir", type=Path, action="append", default=None,
                    help="repeatable; default is both .claude/skills and .agents/skills")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any checklist_candidate is found")
    ap.add_argument("--no-pointer", action="store_true",
                    help="do not read or write pointer state (scan fresh, in-memory only)")
    ap.add_argument("--full-rescan", action="store_true",
                    help="ignore stored mtimes; re-parse every file")
    ap.add_argument("--write-report", nargs="?", const=str(DEFAULT_REPORT_PATH), default=None,
                    help="write the markdown proposal (default path if no value given)")
    ap.add_argument("--check-dormancy", action="store_true",
                    help="also run the pruning/effectiveness pass (design decisions 4+5)")
    args = ap.parse_args()

    skills_dirs = args.skills_dir or DEFAULT_SKILLS_DIRS

    if args.no_pointer:
        all_hits: list[dict] = []
        for fp in sorted(args.autopsy_dir.glob("failure_autopsy_*.json")) if args.autopsy_dir.is_dir() else []:
            all_hits.extend(scan_autopsy_file(fp))
        all_hits.extend(scan_review_tracker(args.review_tracker))
    else:
        pointer = load_pointer(args.pointer_file)
        all_hits, new_pointer = collect_hits(args.autopsy_dir, args.review_tracker, pointer,
                                             full_rescan=args.full_rescan)
        save_pointer(args.pointer_file, new_pointer)

    skill_lines = load_skill_lines(skills_dirs)
    result = audit(all_hits, skill_lines, n=SKILL_RECURRENCE_N)

    dormancy = None
    if args.check_dormancy:
        dormancy = audit_checklist_dormancy(skills_dirs, all_hits)
        result["dormancy"] = dormancy

    if args.write_report:
        Path(args.write_report).write_text(render_report(result), encoding="utf-8")

    if args.json:
        print(json.dumps({
            "skill_recurrence_n": SKILL_RECURRENCE_N,
            "n_raw_hits": len(all_hits),
            **result,
        }, indent=2))
    else:
        print("Skill-improvement recurrence audit (GOV-SKILL-1): "
              f"{len(all_hits)} self-flagged-repeat hit(s) across the corpus")
        print(f"  checklist candidates (ACTIONABLE): {len(result['checklist_candidates'])}")
        print(f"  already codified                 : {len(result['excluded_already_codified'])}")
        print(f"  sub-threshold (informational)     : {len(result['sub_threshold'])}")
        if result["checklist_candidates"]:
            print("\n  -- CANDIDATES: uncodified recurrence a human should consider folding")
            print("     into a skill checklist:")
            for r in result["checklist_candidates"]:
                print(f"    [{', '.join(r['artifacts'])}] {r['n_hits']} hit(s) -- "
                      f"{r['qualifies_reason']}")
                print(f"        {r['sample_text'][:160]}")
        if result["excluded_already_codified"]:
            print("\n  -- already codified (no action -- shown for transparency):")
            for r in result["excluded_already_codified"]:
                cf = r["codified_in"]
                print(f"    [{', '.join(r['artifacts'])}] -> {cf['skill_file']}:{cf['line']}")
        if dormancy is not None:
            print(f"\n  dormancy/effectiveness pass: {len(dormancy)} monitored bullet(s) flagged")
            for d in dormancy:
                print(f"    [{d['verdict']}] {d['skill']} (added {d['first_seen'][:10]}, "
                      f"{d['months_old']}mo ago): {d['text'][:120]}")

    if args.strict and result["checklist_candidates"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
