#!/usr/bin/env python3
"""apply_live_status.py -- stamp a DERIVED `live_status` block + a record-once
`last_reviewed` field on every claim in docs/claims/claims.yaml (SHP-4 of the
status/history plane-separation design,
evidence/planning/status_history_plane_separation_design.md Sec.4b + Sec.7).

This is the claims-registry port of the plane-separation razor (design Sec.2 + 5):

  * STATUS PLANE (regenerable) -- `live_status`. A pure projection over the claim's
    OWN current-state fields (`status` + `v3_pending` + `epistemic_category`). It is
    RECOMPUTABLE, so it is *derived*, blown away and re-stamped each run, never
    hand-maintained. `status:` stays the human-set epistemic category; `live_status`
    carries the *derived current reading* -- the base status with the phase/evidence
    gates that qualify a claim's true live standing layered on (a `candidate` that is
    still V3-pending is not the same live thing as a plain `candidate`; a `provisional`
    claim whose epistemic_category is `substrate_ceiling` is parked, not promotable).

    On top of the self-field reading, an EVENT-STREAM PROVENANCE sub-block
    (`live_status.evidence`: `from` / `as_of` / `verdict`) is projected from the
    append-only event log (autopsies + PASS manifests + decision_log) via
    project_status_head -- the ONE projection path SHP-1/2/3 use, joining each claim by
    scope_claims=[claim_id] (design Sec.4b: "carries the derived current reading + as_of
    + from"). It records the newest event bearing on the claim and its date, so
    "recently-moved truth" is sortable and the reading has a provenance anchor the
    self-field composite alone cannot give. It is nested one level under `live_status`
    so `evidence.as_of` (the event date) never collides with the reading-plane
    `live_status.as_of` (the reading-change date). Event-less claims omit it entirely.

  * HISTORY PLANE (record-once) -- `last_reviewed`. A fact-at-a-timestamp that can only
    be recorded when it happened, never recomputed -> APPEND-ONLY. Seeded once from the
    claim's existing authoritative review event (`adjudicated_at_utc`) where present;
    otherwise left ABSENT (= not yet reviewed under this plane). NEVER overwritten by a
    re-run and NEVER derived. Set going forward with `--mark-reviewed <ID>[,<ID>...]`.

DERIVE, DO NOT HAND-WRITE.  PROMOTES / DEMOTES NOTHING -- this script only ever writes
the derived `live_status` block and the record-once `last_reviewed` field. It NEVER
edits `status`, `confidence`, `v3_pending`, `epistemic_category`, or any other
governance-owned field, and it never changes a claim's confidence or status enum.

Idempotent, like docs/apply_status_frontmatter.py (SHP-5):
  * The claim block is edited by LINE SURGERY -- every other line is left BYTE-IDENTICAL,
    only the `live_status:` block and `last_reviewed:` line are dropped and re-inserted
    (right after the claim's `status:` line). A full yaml.safe_load / yaml.dump round-trip
    is deliberately AVOIDED -- it would reflow the whole 49k-line registry and destroy the
    header + inline governance-note comments. claims.yaml is high-contention; a clean diff
    matters.
  * `live_status.as_of` is PRESERVED when the derived `reading` is unchanged, and only
    bumped to today when the reading actually moves (or on first stamp). A re-run against
    an unchanged registry therefore produces a bit-identical file (no git churn).
  * `last_reviewed` is preserved verbatim on every re-run.

No inline `# comments` are ever written on any field (the claims.yaml line-based readers
mis-resolve enum fields carrying an inline comment -- see CLAUDE.md).

Usage (from REE_assembly root, or anywhere):
    python scripts/apply_live_status.py                 # stamp
    python scripts/apply_live_status.py --check          # dry-run: report would-change, exit 1 if any
    python scripts/apply_live_status.py --mark-reviewed MECH-306,SD-063   # record-once last_reviewed=today
    python scripts/apply_live_status.py --self-test      # deterministic regression fixtures
"""

from __future__ import annotations

import os
import re
import sys
from datetime import date, datetime, timezone

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML required (pip install pyyaml).", file=sys.stderr)
    sys.exit(2)

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS)
CLAIMS_YAML = os.path.join(REPO_ROOT, "docs", "claims", "claims.yaml")

# SHP-4 augmentation (design Sec.4b: "carries the derived current reading + as_of + from").
# The self-field `reading` above is the regenerable STATUS PLANE; on top of it we attach an
# event-stream PROVENANCE sub-block (`live_status.evidence`: from / as_of / verdict) projected
# from the append-only event log (autopsies + PASS manifests + decision_log) via
# project_status_head -- the ONE projection path SHP-1/2/3 already use, joining each claim by
# scope_claims=[claim_id]. This answers "what event last moved this claim, and when" that the
# self-field reading alone cannot. Optional import: if the projector is unavailable the stamper
# still writes the self-field block (evidence sub-block simply omitted).
if SCRIPTS not in sys.path:
    sys.path.insert(0, SCRIPTS)
try:
    import project_status_head as _psh
except Exception:  # pragma: no cover
    _psh = None

# A top-level claim starts here (column-0 list item). Nested `- id:` items (e.g. under
# child_claims / competing_claims, indented) are intentionally NOT block boundaries.
ID_LINE_RE = re.compile(r"^- id:\s*(.+)$")
# The claim's own status field, at exactly 2-space indent. A deeper `status:` (inside a
# nested sub-map) or the `live_status:` key never matches this.
STATUS_LINE_RE = re.compile(r"^  status:\s")
LIVE_STATUS_KEY_RE = re.compile(r"^  live_status:\s*$")
LAST_REVIEWED_KEY_RE = re.compile(r"^  last_reviewed:\s")
# Any stray legacy flat form we might have written before (defensive idempotency).
LEGACY_FLAT_RE = re.compile(r"^  (live_status|live_status_asof):\s")

# Statuses that count as PROMOTED for the internal-consistency (needs_review) check.
PROMOTED_STATUSES = {"provisional", "active", "stable", "implemented"}


# ---------------------------------------------------------------------------
# Derivation (the pure status-plane projection -- single-sourced here)
# ---------------------------------------------------------------------------

def _clean_status(claim):
    """The claim's base status word, first token only (yaml.safe_load already strips any
    inline `# comment`; the split guard is belt-and-braces)."""
    raw = str(claim.get("status") or "").strip()
    if not raw:
        return ""
    return raw.split()[0]


def derive_reading(claim):
    """The single derived live reading string for a claim: the base status with the
    phase/evidence gates that qualify its true live standing layered on. Pure fn of the
    claim record (`status` + `v3_pending` + `epistemic_category`).

      candidate                                (plain)
      candidate/v3_pending                     (V3-pending gate still set)
      provisional/substrate_ceiling            (epistemic_category parks it)
      candidate/v3_pending/substrate_conditional

    The suffixes stack (v3_pending is orthogonal to the epistemic_category park); the two
    epistemic_category parks are mutually exclusive (one category)."""
    status = _clean_status(claim) or "unknown"
    reading = status
    if claim.get("v3_pending") is True:
        reading += "/v3_pending"
    epi = str(claim.get("epistemic_category") or "").strip().lower()
    if epi == "substrate_ceiling":
        reading += "/substrate_ceiling"
    elif epi == "substrate_conditional":
        reading += "/substrate_conditional"
    return reading


def derive_needs_review(claim):
    """(needs_review, reasons). NARROW by design (design Sec.3 term 3: keep the flag a
    signal): fires only on an INTERNAL contradiction among the claim's own current-state
    fields, where the derived reading is a best-effort and a human should glance.

      * a PROMOTED status that still carries the V3-pending gate (the gate should have
        been cleared on promotion);
      * a PROMOTED status whose epistemic_category is `substrate_ceiling` (GOV-CEIL-1
        floors ceiling claims to `candidate`, so a promoted ceiling claim is inconsistent);
      * no `status` field at all.
    """
    reasons = []
    raw_status = str(claim.get("status") or "").strip()
    status = _clean_status(claim)
    v3p = claim.get("v3_pending") is True
    epi = str(claim.get("epistemic_category") or "").strip().lower()
    if not raw_status:
        reasons.append("no status field")
    if status in PROMOTED_STATUSES and v3p:
        reasons.append(f"promoted status '{status}' still carries v3_pending gate")
    if status in PROMOTED_STATUSES and epi == "substrate_ceiling":
        reasons.append(
            f"promoted status '{status}' but epistemic_category substrate_ceiling "
            "(GOV-CEIL-1 floors ceilings to candidate)")
    return bool(reasons), reasons


def _to_date_str(value):
    """Coerce an authoritative timestamp (ISO string or yaml date/datetime) to a
    YYYY-MM-DD string; None if not coercible."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    s = str(value).strip()
    if len(s) >= 10:
        try:
            datetime.strptime(s[:10], "%Y-%m-%d")
            return s[:10]
        except ValueError:
            return None
    return None


def seed_last_reviewed(claim):
    """Record-once seed for `last_reviewed` from the claim's existing authoritative review
    event (`adjudicated_at_utc`). An adjudication IS a governance review of the claim, and
    the timestamp is already record-once in the registry, so lifting its date into the
    canonical `last_reviewed` field is non-destructive (design Sec.5). None when the claim
    has no such event -- the field then stays ABSENT (= not yet reviewed under this plane).
    """
    return _to_date_str(claim.get("adjudicated_at_utc"))


# ---------------------------------------------------------------------------
# Registry load (read-only, for the derivation inputs)
# ---------------------------------------------------------------------------

def load_registry(path=CLAIMS_YAML):
    """id -> claim dict, from the top-level claims.yaml list."""
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    claims = data if isinstance(data, list) else data.get("claims", data)
    out = {}
    for c in claims:
        if isinstance(c, dict) and c.get("id"):
            out[str(c["id"]).strip()] = c
    return out


# ---------------------------------------------------------------------------
# Event-stream provenance (SHP-4 augmentation -- reuse the ONE projection path)
# ---------------------------------------------------------------------------

def build_provenance(claim_ids, repo_root=REPO_ROOT, threshold=None):
    """Return {claim_id: {"from","as_of","verdict"}} projected from the append-only
    event log via project_status_head, joining each claim by scope_claims=[claim_id].

    Only claims with >= 1 joined event (a projected head exists) get an entry; event-less
    claims (most INV-/ARC- foundational claims) are omitted, so no `evidence:` sub-block is
    stamped for them (minimal churn -- the block appears exactly where there is real
    provenance). `{}` when the projector is unavailable (evidence sub-block then omitted
    everywhere; the self-field reading is unaffected). The projection is a pure fn of the
    event log, so a re-run against an unchanged log yields identical provenance; the block
    updates only when a newer event lands (which is the point -- it tracks the live front)."""
    if _psh is None:
        return {}
    thr = _psh.DEFAULT_BRAKE_THRESHOLD if threshold is None else threshold
    events, _counts = _psh.load_events(repo_root)
    prov = {}
    for cid in claim_ids:
        node = {"id": cid, "scope_claims": [cid]}
        slc, _tokens, _p = _psh.join_node(node, events)
        if not slc:
            continue
        live, head = _psh.project_live(node, slc, thr)
        if head is None:
            continue
        sv = _psh.stored_live_view(live)
        entry = {"from": sv.get("from"), "as_of": sv.get("as_of"),
                 "verdict": sv.get("verdict")}
        if entry["from"]:
            prov[cid] = entry
    return prov


# ---------------------------------------------------------------------------
# Line surgery
# ---------------------------------------------------------------------------

def _strip_scalar(v):
    """First token / inline-comment-stripped / unquoted scalar (for reading the id off a
    `- id:` line and old values off previously-stamped lines)."""
    v = v.split("#", 1)[0].strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        v = v[1:-1]
    return v.strip()


def _leading_spaces(line):
    return len(line) - len(line.lstrip(" "))


def split_claim_blocks(lines):
    """Partition file lines into (preamble, [(id, block_lines), ...]).

    A block runs from a column-0 `- id:` line up to (not including) the next one. The
    preamble is everything before the first `- id:` (the header comment). Blank lines and
    folded-scalar (`notes: >`) content simply belong to whichever block they fall in --
    we never interpret them, only locate the `status:` line to insert after."""
    preamble = []
    blocks = []
    cur_id = None
    cur = []
    seen_first = False
    for line in lines:
        m = ID_LINE_RE.match(line)
        if m:
            if seen_first:
                blocks.append((cur_id, cur))
            else:
                seen_first = True
            cur_id = _strip_scalar(m.group(1))
            cur = [line]
        elif not seen_first:
            preamble.append(line)
        else:
            cur.append(line)
    if seen_first:
        blocks.append((cur_id, cur))
    return preamble, blocks


def extract_existing(block_lines):
    """Read the currently-stamped (as_of, reading, last_reviewed) from a block so a re-run
    can preserve as_of (when the reading is unchanged) and last_reviewed (always)."""
    as_of = None
    reading = None
    last_reviewed = None
    i = 0
    n = len(block_lines)
    while i < n:
        line = block_lines[i]
        if LIVE_STATUS_KEY_RE.match(line):
            # consume nested children (indent > 2), but only read the DIRECT children
            # (indent == 4). A deeper `as_of:` inside the nested `evidence:` sub-block
            # (indent 6) must NOT be mistaken for the top-level live_status.as_of --
            # else re-runs would clobber the reading-change as_of with the event date.
            j = i + 1
            while j < n and block_lines[j].strip() and _leading_spaces(block_lines[j]) > 2:
                if _leading_spaces(block_lines[j]) == 4:
                    child = block_lines[j].strip()
                    cm = re.match(r"^(as_of|reading|needs_review):\s*(.*)$", child)
                    if cm:
                        if cm.group(1) == "as_of":
                            as_of = _strip_scalar(cm.group(2))
                        elif cm.group(1) == "reading":
                            reading = _strip_scalar(cm.group(2))
                j += 1
            i = j
            continue
        if LAST_REVIEWED_KEY_RE.match(line):
            last_reviewed = _strip_scalar(line.split(":", 1)[1])
        i += 1
    return as_of, reading, last_reviewed


def strip_stamp_lines(block_lines):
    """Return block_lines with any existing live_status block + last_reviewed + legacy
    flat stamp removed, leaving every other line byte-identical."""
    out = []
    i = 0
    n = len(block_lines)
    while i < n:
        line = block_lines[i]
        if LIVE_STATUS_KEY_RE.match(line):
            i += 1
            while i < n and block_lines[i].strip() and _leading_spaces(block_lines[i]) > 2:
                i += 1
            continue
        if LAST_REVIEWED_KEY_RE.match(line) or LEGACY_FLAT_RE.match(line):
            i += 1
            continue
        out.append(line)
        i += 1
    return out


def _yaml_scalar(value):
    """Quote a value only when needed (mirrors the nav/status stamper conservatism)."""
    s = str(value)
    special = [":", "{", "}", "[", "]", "#", "&", "*", "!", "|", ">", "'", '"', "%", "@", "`", ","]
    if s == "" or any(c in s for c in special) or s != s.strip():
        return '"{}"'.format(s.replace('"', '\\"'))
    return s


def build_stamp_lines(reading, as_of, needs_review, last_reviewed, provenance=None):
    out = [
        "  live_status:",
        f"    reading: {_yaml_scalar(reading)}",
        f"    as_of: {as_of}",
        f"    needs_review: {'true' if needs_review else 'false'}",
    ]
    # Event-stream provenance sub-block (SHP-4 augmentation). Nested one level under
    # live_status so live_status.evidence.as_of (the newest bearing event's date) never
    # collides with the reading-plane live_status.as_of (the reading-change date). Emitted
    # only when the claim has a projected head (event-less claims omit it entirely).
    if provenance and provenance.get("from"):
        out.append("    evidence:")
        out.append(f"      from: {_yaml_scalar(provenance['from'])}")
        if provenance.get("as_of"):
            out.append(f"      as_of: {provenance['as_of']}")
        if provenance.get("verdict"):
            out.append(f"      verdict: {_yaml_scalar(provenance['verdict'])}")
    if last_reviewed:
        out.append(f"  last_reviewed: {last_reviewed}")
    return out


def _insert_index(stripped):
    """Index at which to insert the stamp lines: right after the claim's own `status:`
    line, else after the `- id:` line (index 0)."""
    for idx, line in enumerate(stripped):
        if STATUS_LINE_RE.match(line):
            return idx + 1
    return 1  # after the `- id:` line


def process_block(claim_id, block_lines, registry, today, provenance_map=None):
    """Return (new_block_lines, changed_bool, result_dict). Non-registry ids are left
    untouched."""
    claim = registry.get(claim_id)
    if claim is None:
        return block_lines, False, {"id": claim_id, "action": "unregistered"}

    old_as_of, old_reading, old_last_reviewed = extract_existing(block_lines)
    reading = derive_reading(claim)
    needs_review, _reasons = derive_needs_review(claim)

    # as_of preservation for idempotency.
    if old_as_of and old_reading == reading:
        as_of = old_as_of
    else:
        as_of = today

    # last_reviewed: record-once. Preserve any existing value; else seed once.
    last_reviewed = old_last_reviewed if old_last_reviewed else seed_last_reviewed(claim)

    provenance = (provenance_map or {}).get(claim_id)

    stripped = strip_stamp_lines(block_lines)
    stamp = build_stamp_lines(reading, as_of, needs_review, last_reviewed, provenance)
    idx = _insert_index(stripped)
    new_block = stripped[:idx] + stamp + stripped[idx:]

    changed = new_block != block_lines
    return new_block, changed, {
        "id": claim_id, "action": "stamp", "reading": reading,
        "prev_reading": old_reading, "as_of": as_of, "needs_review": needs_review,
        "last_reviewed": last_reviewed,
        "has_evidence": bool(provenance and provenance.get("from")),
        "changed": changed,
    }


def _read_lines(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    # splitlines(keepends=False) + explicit '\n' join preserves a trailing newline iff
    # the file had one; capture that.
    trailing_nl = text.endswith("\n")
    return text.split("\n"), trailing_nl


def _write_lines(path, lines, trailing_nl):
    text = "\n".join(lines)
    if trailing_nl and not text.endswith("\n"):
        text += "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def run(dry_run=False, mark_reviewed=None, path=CLAIMS_YAML):
    registry = load_registry(path)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines, trailing_nl = _read_lines(path)
    # splitlines via '\n' on a trailing-newline file yields a final '' element; drop it so
    # we don't grow a blank line, and rely on trailing_nl to restore the newline.
    if trailing_nl and lines and lines[-1] == "":
        lines = lines[:-1]

    preamble, blocks = split_claim_blocks(lines)

    # Event-stream provenance projected ONCE over the whole registry (reuses
    # project_status_head's ONE projection path). {} if the projector is unavailable.
    # claims.yaml lives at <repo>/docs/claims/claims.yaml -> repo root is 3 levels up.
    _repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(path))))
    provenance_map = build_provenance(registry.keys(), repo_root=_repo_root)

    mark_set = set()
    if mark_reviewed:
        for tok in mark_reviewed.replace(",", " ").split():
            mark_set.add(tok.strip())

    new_lines = list(preamble)
    stamped = changed = needs_review_ct = seeded = evidence_ct = 0
    unregistered = []
    changed_ids = []
    for claim_id, block in blocks:
        # --mark-reviewed: stamp last_reviewed=today (record-once; refuse to overwrite).
        if claim_id in mark_set and registry.get(claim_id) is not None:
            _a, _r, existing_lr = extract_existing(block)
            if existing_lr:
                print(f"  --mark-reviewed: {claim_id} already has last_reviewed={existing_lr}; "
                      "left unchanged (record-once).")
            else:
                # inject a synthetic value the derivation path will preserve
                registry[claim_id] = dict(registry[claim_id])
                registry[claim_id]["adjudicated_at_utc"] = today  # seed path picks it up

        new_block, ch, res = process_block(claim_id, block, registry, today, provenance_map)
        if res["action"] == "unregistered":
            unregistered.append(claim_id)
        else:
            stamped += 1
            if res["needs_review"]:
                needs_review_ct += 1
            if res["last_reviewed"]:
                seeded += 1
            if res.get("has_evidence"):
                evidence_ct += 1
            if ch:
                changed += 1
                changed_ids.append(claim_id)
        new_lines.extend(new_block)

    if not dry_run and changed:
        _write_lines(path, new_lines, trailing_nl)

    verb = "would change" if dry_run else "changed"
    print(f"apply_live_status: {stamped} claims stamped; {changed} {verb} on disk; "
          f"{needs_review_ct} needs_review; {seeded} carry last_reviewed; "
          f"{evidence_ct} carry event provenance.")
    if unregistered:
        print(f"  {len(unregistered)} `- id:` block(s) not in the yaml registry, left "
              f"untouched: {', '.join(unregistered[:8])}"
              + (" ..." if len(unregistered) > 8 else ""))
    if dry_run and changed_ids:
        for cid in changed_ids[:40]:
            print("   would-change  " + cid)
        if len(changed_ids) > 40:
            print(f"   ... (+{len(changed_ids) - 40} more)")
    return 1 if (dry_run and changed) else 0


# ---------------------------------------------------------------------------
# Self-test (deterministic -- no clock, no disk)
# ---------------------------------------------------------------------------

def _self_test():
    failures = []

    def check(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            failures.append(name)

    # --- derive_reading ------------------------------------------------------
    check("plain candidate", derive_reading({"status": "candidate"}) == "candidate")
    check("v3_pending suffix",
          derive_reading({"status": "candidate", "v3_pending": True}) == "candidate/v3_pending")
    check("ceiling suffix",
          derive_reading({"status": "provisional", "epistemic_category": "substrate_ceiling"})
          == "provisional/substrate_ceiling")
    check("conditional suffix",
          derive_reading({"status": "candidate", "epistemic_category": "substrate_conditional"})
          == "candidate/substrate_conditional")
    check("stacked v3_pending + conditional",
          derive_reading({"status": "candidate", "v3_pending": True,
                          "epistemic_category": "substrate_conditional"})
          == "candidate/v3_pending/substrate_conditional")
    check("status with inline-comment leak -> first token",
          derive_reading({"status": "provisional # gov note"}) == "provisional")
    check("missing status -> unknown", derive_reading({}) == "unknown")

    # --- derive_needs_review -------------------------------------------------
    nr, _ = derive_needs_review({"status": "candidate", "v3_pending": True})
    check("candidate + v3_pending is NOT a contradiction", nr is False)
    nr, _ = derive_needs_review({"status": "provisional", "v3_pending": True})
    check("promoted + v3_pending IS a contradiction", nr is True)
    nr, _ = derive_needs_review(
        {"status": "active", "epistemic_category": "substrate_ceiling"})
    check("promoted + substrate_ceiling IS a contradiction", nr is True)
    nr, _ = derive_needs_review({"status": ""})
    check("missing status flags needs_review", nr is True)
    nr, _ = derive_needs_review({"status": "provisional"})
    check("clean provisional does NOT flag", nr is False)

    # --- last_reviewed seed --------------------------------------------------
    check("seed from adjudicated_at_utc string",
          seed_last_reviewed({"adjudicated_at_utc": "2026-02-25T16:56:17.901452Z"}) == "2026-02-25")
    check("seed None when no adjudication", seed_last_reviewed({}) is None)
    check("seed from a yaml date object",
          seed_last_reviewed({"adjudicated_at_utc": date(2026, 3, 1)}) == "2026-03-01")

    # --- line surgery round-trip + idempotency -------------------------------
    sample = [
        "- id: MECH-999",
        '  title: "x"',
        "  claim_type: mechanism_hypothesis",
        "  status: candidate",
        "  v3_pending: true",
        "  epistemic_category: substrate_conditional",
        "  notes: >",
        "    multi",
        "",
        "    line note with a blank inside the folded scalar",
        "  adjudicated_at_utc: 2026-02-25T16:56:17.901452Z",
    ]
    reg = {"MECH-999": {"id": "MECH-999", "status": "candidate", "v3_pending": True,
                        "epistemic_category": "substrate_conditional",
                        "adjudicated_at_utc": "2026-02-25T16:56:17.901452Z"}}
    b1, ch1, _r1 = process_block("MECH-999", sample, reg, "2026-07-11")
    check("first stamp changes the block", ch1 is True)
    check("live_status inserted after status",
          b1[b1.index("  status: candidate") + 1] == "  live_status:")
    check("reading correct in stamp",
          "    reading: candidate/v3_pending/substrate_conditional" in b1)
    check("as_of stamped", "    as_of: 2026-07-11" in b1)
    check("last_reviewed seeded from adjudication", "  last_reviewed: 2026-02-25" in b1)
    check("folded-scalar blank line preserved byte-identical", "" in b1 and b1.count("") == 1)
    # idempotent re-run: same registry + a LATER 'today' must keep as_of (reading unchanged)
    b2, ch2, _r2 = process_block("MECH-999", b1, reg, "2026-09-99")
    check("re-run is a no-op (bit-identical, as_of preserved)", ch2 is False and b2 == b1)
    # reading moves -> as_of bumps
    reg2 = {"MECH-999": {"id": "MECH-999", "status": "provisional",
                         "epistemic_category": "substrate_conditional",
                         "adjudicated_at_utc": "2026-02-25T16:56:17.901452Z"}}
    b3, ch3, _r3 = process_block("MECH-999", b1, reg2, "2026-08-01")
    check("reading move re-stamps + bumps as_of",
          ch3 and "    reading: provisional/substrate_conditional" in b3
          and "    as_of: 2026-08-01" in b3)
    check("last_reviewed preserved across re-stamp (record-once)",
          "  last_reviewed: 2026-02-25" in b3)
    # only one live_status block after re-stamp (no duplication)
    check("no duplicate live_status block", b3.count("  live_status:") == 1)

    # block with no status line -> insert after id line
    nostatus = ["- id: Q-999", '  title: "y"', "  claim_type: open_question"]
    regq = {"Q-999": {"id": "Q-999"}}
    bq, chq, _rq = process_block("Q-999", nostatus, regq, "2026-07-11")
    check("no-status block -> live_status after id line, reading unknown",
          bq[1] == "  live_status:" and "    reading: unknown" in bq
          and "    needs_review: true" in bq)

    # --- SHP-4 augmentation: event-stream provenance sub-block ----------------
    prov = {"from": "failure_autopsy_V3-EXQ-733_2026-07-10", "as_of": "2026-07-10",
            "verdict": "non_contributory/substrate_ceiling"}
    pmap = {"MECH-999": prov}
    be, che, _re = process_block("MECH-999", sample, reg, "2026-07-11", pmap)
    check("evidence sub-block nested under live_status", "    evidence:" in be)
    check("evidence.from stamped (event id)",
          "      from: failure_autopsy_V3-EXQ-733_2026-07-10" in be)
    check("evidence.as_of is the EVENT date (nested, indent 6)", "      as_of: 2026-07-10" in be)
    check("evidence.verdict stamped (unquoted; '/' needs no quoting)",
          "      verdict: non_contributory/substrate_ceiling" in be)
    check("reading-plane as_of still the reading date (not clobbered by event date)",
          "    as_of: 2026-07-11" in be)
    check("evidence sits between needs_review and last_reviewed",
          be.index("    evidence:") > be.index("    needs_review: false")
          and be.index("    evidence:") < be.index("  last_reviewed: 2026-02-25"))
    # idempotent re-run WITH provenance + a later 'today': nested event as_of must NOT be
    # read as the top-level as_of, so the block stays bit-identical (the extract_existing fix).
    be2, che2, _re2 = process_block("MECH-999", be, reg, "2026-12-31", pmap)
    check("re-run with nested evidence is bit-identical (no as_of clobber)",
          che2 is False and be2 == be)
    check("no duplicate evidence block after re-stamp", be.count("    evidence:") == 1)
    # dropping provenance removes the evidence block cleanly on re-stamp
    be3, che3, _re3 = process_block("MECH-999", be, reg, "2026-07-11", {})
    check("no-provenance re-stamp strips the evidence block",
          che3 is True and "    evidence:" not in be3 and be3.count("  live_status:") == 1)
    # provenance with no 'from' emits no block
    bn, _chn, _rn = process_block("MECH-999", sample, reg, "2026-07-11",
                                  {"MECH-999": {"from": None}})
    check("provenance lacking 'from' -> no evidence block", "    evidence:" not in bn)

    print()
    if failures:
        print("SELF-TEST FAILED: " + ", ".join(failures))
        return 1
    print("SELF-TEST PASSED")
    return 0


def main(argv):
    if "--self-test" in argv:
        return _self_test()
    mark = None
    if "--mark-reviewed" in argv:
        i = argv.index("--mark-reviewed")
        if i + 1 < len(argv):
            mark = argv[i + 1]
        else:
            print("ERROR: --mark-reviewed needs a comma/space list of claim ids.", file=sys.stderr)
            return 2
    return run(dry_run="--check" in argv, mark_reviewed=mark)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
