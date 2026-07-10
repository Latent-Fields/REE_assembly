#!/usr/bin/env python3
"""apply_status_frontmatter.py -- stamp claims.yaml-derived status frontmatter on
architecture docs (SHP-5 of the status/history plane-separation design,
evidence/planning/status_history_plane_separation_design.md Sec.4c + Sec.7).

Companion to docs/apply_nav_frontmatter.py. For each architecture doc that names a
claim id -- via a `**Claim:**` / `**Claims:**` body line (the declared convention,
e.g. `**Claim:** SD-063 (design_decision, candidate, implementation_phase v3,
v3_pending)`) or, failing that, its filename stem (`sd_063_*.md` -> SD-063) -- look
the claim up in docs/claims/claims.yaml and stamp machine-checkable YAML frontmatter:

    status:        <registry status>[/v3_pending]   # DERIVED from claims.yaml
    status_asof:   <YYYY-MM-DD>                      # when this derived value was last set
    status_claim:  <CLAIM-ID>                        # provenance -- which claim it came from

The ~184 hand-typed `**Status:**` body lines rot silently because nothing recomputes
them (confirmed live drift 2026-07-10: sd_063_*.md still said "v3_pending" though
SD-063 had been promoted provisional). Once the derived value is in frontmatter, a
LOW-INFORMATION hand line (a bare status word like `candidate` / `candidate, v3_pending`
-- the ~71 priority lines) is RETIRED. A hand line carrying residual content not present
in the registry (a date, or prose like "substrate built, disabled-by-default") is KEPT
and reported, so it can be lifted by hand -- the non-destructive migration razor (design
Sec.5). This script never deletes prose.

DERIVE, DO NOT HAND-WRITE. PROMOTES / DEMOTES NOTHING -- read-only over claims.yaml;
it only rewrites doc frontmatter and removes pure-boilerplate status lines.

Re-runnable + idempotent like the nav stamper:
  * The frontmatter block is edited by line surgery -- existing (nav) lines are left
    BYTE-IDENTICAL, only the status_* lines are dropped and re-appended -- so the two
    stampers never fight over frontmatter formatting.
  * `status_asof` is PRESERVED when the derived `status` is unchanged, and only bumped
    to today when the value actually changes (or on first stamp). A re-run against an
    unchanged registry therefore produces a bit-identical file (no git churn).

Ordering note: docs/apply_nav_frontmatter.py OWNS the same frontmatter block and strips
it on every run, but it now PRESERVES the status_* keys across its re-stamp (see the
_extract_status_lines / render_frontmatter(extra_lines=...) hook there). So the two
compose in either order. In scripts/governance.sh this stamper runs immediately AFTER
the nav stamper (Step 9b), with the drift check (scripts/claims_doc_drift.py) after it.

Usage (from REE_assembly root, or anywhere):
    python docs/apply_status_frontmatter.py            # stamp
    python docs/apply_status_frontmatter.py --check     # dry-run: list would-change docs, exit 1 if any
"""

import os
import re
import sys
from datetime import datetime, timezone

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required (pip install pyyaml).", file=sys.stderr)
    sys.exit(2)

DOCS = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(DOCS)
ARCH = os.path.join(DOCS, "architecture")
CLAIMS_YAML = os.path.join(DOCS, "claims", "claims.yaml")

# Frontmatter keys this script owns. Kept in sync with the preserve-list in
# docs/apply_nav_frontmatter.py::_extract_status_lines so a nav re-stamp keeps them.
STATUS_KEYS = ("status", "status_asof", "status_claim")

CLAIM_ID_RE = re.compile(r"\b(INV|ARC|MECH|SD|Q|IMPL)-\d+[A-Z]?\b", re.IGNORECASE)
FILENAME_STEM_RE = re.compile(r"^(inv|arc|mech|sd|q|impl)_(\d+[a-z]?)_", re.IGNORECASE)
CLAIM_LINE_RE = re.compile(r"(?m)^\*\*Claims?:\*\*\s*(.+)$")
STATUS_LINE_RE = re.compile(r"(?m)^\*\*Status:\*\*[ \t]*(.*)$")

# Bare tokens that carry NO history beyond the registry -- a status line built only
# from these (in any order) is safe to retire. A DATE or any other word is treated as
# residual and keeps the line (razor Sec.5). "implemented" is a registry status value,
# so a bare "IMPLEMENTED" with no date is retire-eligible; "IMPLEMENTED 2026-05-17" is
# not (the date is history).
STATUS_TOKEN_ALLOW = {
    "candidate", "provisional", "active", "open", "stable", "legacy",
    "implemented", "resolved", "superseded", "retired", "retiring",
    "candidate_substrate_landed", "candidate_resolved",
    "v3_pending", "v3-pending",
}


# ---------------------------------------------------------------------------
# Registry + derivation
# ---------------------------------------------------------------------------

def load_registry(path=CLAIMS_YAML):
    """id -> claim dict, from the top-level claims.yaml list."""
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    claims = data if isinstance(data, list) else data.get("claims", data)
    out = {}
    for c in claims:
        if isinstance(c, dict) and c.get("id"):
            out[str(c["id"]).upper()] = c
    return out


def derive_status(claim):
    """The single derived status token for a claim: its registry `status`, with a
    `/v3_pending` suffix when the v3_pending gate is set. Pure fn of claims.yaml."""
    base = str(claim.get("status") or "unknown").strip()
    if claim.get("v3_pending") is True:
        base += "/v3_pending"
    return base


def resolve_claim_id(basename, text, registry):
    """(claim_id, method) for a doc, or (None, 'unresolved').

    Priority: an explicit **Claim:** / **Claims:** line naming a registered id, then
    the filename stem if it maps to a registered id. Only ever returns an id that
    exists in the registry -- an unregistered filename stem stays unresolved."""
    m = CLAIM_LINE_RE.search(text)
    if m:
        idm = CLAIM_ID_RE.search(m.group(1))
        if idm and idm.group(0).upper() in registry:
            return idm.group(0).upper(), "claim_line"
    fm = FILENAME_STEM_RE.match(basename)
    if fm:
        cid = "{}-{}".format(fm.group(1).upper(), fm.group(2).upper())
        if cid in registry:
            return cid, "filename_stem"
    return None, "unresolved"


# ---------------------------------------------------------------------------
# Frontmatter line surgery (leaves non-status lines byte-identical)
# ---------------------------------------------------------------------------

def split_frontmatter(text):
    """Return (fm_lines or None, body). fm_lines excludes the --- fences."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm_block = text[4:end]
    body = text[end + 5:]
    return fm_block.split("\n"), body


def existing_status_fields(fm_lines):
    """Parse the current status_* values out of frontmatter lines (for asof preservation)."""
    out = {}
    if not fm_lines:
        return out
    for line in fm_lines:
        m = re.match(r"^(status|status_asof|status_claim):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"')
    return out


def _yaml_scalar(value):
    """Quote a value only when needed (mirrors the nav stamper's conservatism)."""
    s = str(value)
    special = [":", "{", "}", "[", "]", "#", "&", "*", "!", "|", ">", "'", '"', "%", "@", "`"]
    if s == "" or any(c in s for c in special) or s != s.strip():
        return '"{}"'.format(s.replace('"', '\\"'))
    return s


def build_frontmatter(fm_lines, status, status_asof, status_claim):
    """Return new fm_lines: existing non-status lines verbatim, status_* re-appended."""
    kept = []
    if fm_lines:
        for line in fm_lines:
            if re.match(r"^(status|status_asof|status_claim):", line):
                continue
            kept.append(line)
    # drop a trailing empty line that line-splitting can leave, so we don't grow blanks
    while kept and kept[-1].strip() == "":
        kept.pop()
    kept.append("status: {}".format(_yaml_scalar(status)))
    kept.append("status_asof: {}".format(status_asof))
    kept.append("status_claim: {}".format(status_claim))
    return kept


# ---------------------------------------------------------------------------
# Status-line retirement
# ---------------------------------------------------------------------------

def status_line_is_low_info(status_body, claim_id):
    """True when the hand status line is only bare status words (no date, no prose) --
    the retire-eligible case. Anything else (a date, a claim ref beyond the doc's own
    id, prose) keeps the line."""
    # strip markdown emphasis/backticks/parens but KEEP underscores -- they are token
    # characters here (v3_pending, candidate_substrate_landed), not emphasis.
    s = re.sub(r"[`*()]", " ", status_body.strip()).rstrip(".").strip()
    toks = [t for t in re.split(r"[\s,/]+", s) if t]
    if not toks:
        return False  # an empty status line is malformed -- leave it for a human
    cid_low = (claim_id or "").lower()
    for t in toks:
        tl = t.lower()
        if tl in STATUS_TOKEN_ALLOW:
            continue
        if tl == cid_low:
            continue
        return False
    return True


def retire_status_line(body, claim_id):
    """Remove the first low-info `**Status:**` line from body. Returns (new_body, retired_bool)."""
    m = STATUS_LINE_RE.search(body)
    if not m:
        return body, False
    if not status_line_is_low_info(m.group(1), claim_id):
        return body, False
    # remove the whole line plus its trailing newline
    start = m.start()
    end = m.end()
    if end < len(body) and body[end] == "\n":
        end += 1
    return body[:start] + body[end:], True


# ---------------------------------------------------------------------------
# Per-doc processing
# ---------------------------------------------------------------------------

def process_doc(path, registry, today, dry_run=False):
    """Returns a result dict describing what happened / would happen."""
    basename = os.path.basename(path)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    cid, method = resolve_claim_id(basename, text, registry)
    has_status_line = bool(STATUS_LINE_RE.search(text))
    if cid is None:
        return {"doc": basename, "action": "unresolved", "has_status_line": has_status_line}

    derived = derive_status(registry[cid])
    fm_lines, body = split_frontmatter(text)
    prev = existing_status_fields(fm_lines)

    # asof preservation for idempotency
    if prev.get("status") == derived and prev.get("status_asof"):
        asof = prev["status_asof"]
    else:
        asof = today

    new_fm = build_frontmatter(fm_lines, derived, asof, cid)
    new_body, retired = retire_status_line(body, cid)

    new_text = "---\n" + "\n".join(new_fm) + "\n---\n"
    # preserve exactly one blank line between frontmatter and body, like the nav stamper
    new_text += "\n" + new_body.lstrip("\n")

    changed = (new_text != text)
    result = {
        "doc": basename,
        "action": "stamp",
        "claim": cid,
        "method": method,
        "derived": derived,
        "prev_status": prev.get("status"),
        "asof": asof,
        "retired_status_line": retired,
        "changed": changed,
    }
    if changed and not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_text)
    return result


def iter_arch_docs():
    for fn in sorted(os.listdir(ARCH)):
        if fn.endswith(".md"):
            yield os.path.join(ARCH, fn)


def run(dry_run=False):
    registry = load_registry()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    stamped = changed = retired = unresolved_with_status = unresolved = 0
    changed_docs, retired_docs, kept_residual = [], [], []

    for path in iter_arch_docs():
        r = process_doc(path, registry, today, dry_run=dry_run)
        if r["action"] == "unresolved":
            unresolved += 1
            if r["has_status_line"]:
                unresolved_with_status += 1
            continue
        stamped += 1
        if r["changed"]:
            changed += 1
            changed_docs.append(r["doc"])
        if r["retired_status_line"]:
            retired += 1
            retired_docs.append(r["doc"])

    verb = "would change" if dry_run else "changed"
    print("apply_status_frontmatter: {} docs resolved to a claim; {} {} on disk; "
          "{} boilerplate **Status:** line(s) retired.".format(
              stamped, changed, verb, retired))
    print("  unresolved docs: {} ({} of them still carry a hand **Status:** line "
          "-- no claim id derivable, left untouched).".format(
              unresolved, unresolved_with_status))
    if dry_run and changed:
        for d in changed_docs:
            print("   would-change  " + d)
    return 1 if (dry_run and changed) else 0


def _self_test():
    """Regression fixtures for the fiddly derive / resolve / retire logic. Run with
    `--self-test`; exits non-zero on any failure. Deterministic -- no clock, no disk."""
    failures = []

    def check(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            failures.append(name)

    # derive_status
    check("derive provisional (v3_pending false)",
          derive_status({"status": "provisional", "v3_pending": False}) == "provisional")
    check("derive candidate/v3_pending suffix",
          derive_status({"status": "candidate", "v3_pending": True}) == "candidate/v3_pending")
    check("derive missing status -> unknown",
          derive_status({}) == "unknown")

    # resolve_claim_id: Claim line beats filename; only registered ids resolve
    reg = {"SD-063": {}, "MECH-288": {}}
    check("resolve via **Claim:** line",
          resolve_claim_id("event_segmenter.md", "**Claim:** MECH-288 (x)", reg)
          == ("MECH-288", "claim_line"))
    check("resolve via filename stem",
          resolve_claim_id("sd_063_x.md", "no claim line", reg)
          == ("SD-063", "filename_stem"))
    check("unregistered stem stays unresolved",
          resolve_claim_id("mech_999_x.md", "no claim line", reg)[0] is None)

    # status_line_is_low_info: the underscore-in-v3_pending regression that shipped a bug
    check("bare 'candidate' is low-info", status_line_is_low_info("candidate", "SD-1"))
    check("'candidate, v3_pending' is low-info (underscore kept)",
          status_line_is_low_info("candidate, v3_pending", "MECH-288"))
    check("bare 'IMPLEMENTED' is low-info", status_line_is_low_info("IMPLEMENTED", "SD-1"))
    check("dated line is NOT low-info (date is history)",
          not status_line_is_low_info("IMPLEMENTED 2026-05-17", "SD-1"))
    check("prose line is NOT low-info",
          not status_line_is_low_info("candidate architectural framing (MAP)", "SD-1"))

    # asof preservation: unchanged status keeps prior asof; changed status bumps it
    fm = ["title: X", "status: provisional", "status_asof: 2026-01-01", "status_claim: SD-063"]
    prev = existing_status_fields(fm)
    check("existing_status_fields parses prior asof", prev.get("status_asof") == "2026-01-01")

    print()
    if failures:
        print("SELF-TEST FAILED: " + ", ".join(failures))
        return 1
    print("SELF-TEST PASSED")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(_self_test())
    sys.exit(run(dry_run="--check" in sys.argv[1:]))
