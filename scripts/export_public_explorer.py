#!/usr/bin/env python3
"""
Export the public, read-only REE Explorer ("Lab Window") data files.

Reads canonical sources (claims.yaml, claim_evidence.v1.json, reviewed
experiment manifests, review_tracker.json, pending_review.md) and emits a
curated, trajectory-safe subset to docs/public_explorer/data/*.json for the
static GitHub Pages front-end.

SAFETY MODEL (defence in depth):
  1. SCOPE FILTER   -- only settled / V3-relevant claims (see config `scope`);
                       future-stage (v4/v5/...) and substrate_conditional
                       claims are withheld. Experiments are exported only when
                       reviewed AND linked to a public claim.
  2. ALLOWLIST      -- every output record is assembled field-by-field from an
                       explicit whitelist. Unlisted source fields are NEVER
                       copied, so they cannot leak.
  3. PATTERN SCRUB  -- every string that survives the allowlist is scanned for
                       sensitive patterns (IPs, hostnames, paths, secrets). A
                       match DROPS the whole field and is logged for human
                       review in public_explorer_redaction_report.md.

Nothing in this script mutates any source file. It only reads canonical data
and writes under docs/public_explorer/data/ plus the root redaction report.

Usage:
  python3 scripts/export_public_explorer.py          # build the export
  python3 scripts/export_public_explorer.py --check   # build + run leak/scope
                                                       # validation (non-zero
                                                       # exit on any failure)

The redaction report is written to the repo ROOT (not under docs/) so it is
never published by GitHub Pages -- it is the maintainer's review artifact.
"""
import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
CLAIM_EVIDENCE = REPO_ROOT / "evidence" / "experiments" / "claim_evidence.v1.json"
EXPERIMENTS_DIR = REPO_ROOT / "evidence" / "experiments"
REVIEW_TRACKER = EXPERIMENTS_DIR / "review_tracker.json"
PENDING_REVIEW = EXPERIMENTS_DIR / "pending_review.md"
CONFIG = Path(__file__).resolve().parent / "public_explorer_config.yaml"

OUT_DIR = REPO_ROOT / "docs" / "public_explorer" / "data"
REDACTION_REPORT = REPO_ROOT / "public_explorer_redaction_report.md"

# Manifest files in evidence/experiments/ that are NOT experiment runs.
NON_MANIFEST_TOKENS = (
    "index", "tracker", "claim_evidence", "snapshot", "proposals",
    "recommend", "decision_", "criteria", "option_e", "staging",
)

# ---------------------------------------------------------------------------
# Sensitive-pattern scrub. Conservative: any hit drops the entire field.
# ---------------------------------------------------------------------------
SENSITIVE_PATTERNS = [
    ("ipv4", re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")),
    ("private_10_net", re.compile(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")),
    ("hub_port", re.compile(r":8787\b")),
    ("cloud_host", re.compile(r"\bree-(?:cloud|worker)-\d+\b", re.I)),
    ("named_host", re.compile(r"\b(?:DLAPTOP|Daniel-PC|EWIN-PC|ree-cloud-1)\b", re.I)),
    ("dot_local", re.compile(r"\b[\w-]+\.local\b", re.I)),
    ("abs_path", re.compile(r"(?:/Users/|/home/|/etc/|/var/|~/)[\w./-]+")),
    ("ssh", re.compile(r"\bssh\s+\w+@", re.I)),
    ("secret", re.compile(r"(?i)\b(?:secret|api[_-]?key|password|access[_-]?token|bearer)\b\s*[:=]")),
    ("sk_token", re.compile(r"\bsk-[A-Za-z0-9]{16,}\b")),
    ("systemd", re.compile(r"\.service\b|systemctl|/etc/systemd")),
]


class Redactions:
    """Accumulates everything withheld, for the human-review report."""

    def __init__(self):
        self.claim_exclusions = Counter()       # reason -> count
        self.experiment_exclusions = Counter()  # reason -> count
        self.dropped_fields = Counter()         # (record_type.field) -> count
        # High-signal: an ALLOWLISTED field tripped the scrub. These warrant a
        # human look because they were meant to be public.
        self.pattern_hits = []                  # list of dict


def scrub(text, redactions, record_type, field, record_id):
    """Return the string if clean, else None (dropped). Logs pattern hits."""
    if text is None:
        return None
    s = str(text)
    for name, pat in SENSITIVE_PATTERNS:
        m = pat.search(s)
        if m:
            redactions.dropped_fields[f"{record_type}.{field}"] += 1
            redactions.pattern_hits.append({
                "record_type": record_type,
                "record_id": record_id,
                "field": field,
                "pattern": name,
                "matched": m.group(0)[:60],
            })
            return None
    return s


def truncate(s, n=400):
    if s is None:
        return None
    s = s.strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


# ---------------------------------------------------------------------------
# Friendly labels
# ---------------------------------------------------------------------------
CLAIM_TYPE_LABELS = {
    "invariant": "Invariant",
    "architectural_commitment": "Architectural commitment",
    "architecture": "Architectural commitment",
    "mechanism_hypothesis": "Mechanism hypothesis",
    "mechanism": "Mechanism hypothesis",
    "substrate_design": "Substrate design",
    "design_decision": "Substrate design",
    "open_question": "Open question",
    "question": "Open question",
    "implementation": "Implementation",
    "implementation_note": "Implementation note",
    "research_anchor": "Research anchor",
    "literature_synthesis": "Literature synthesis",
}
STATUS_LABELS = {
    "active": "Active",
    "provisional": "Provisional",
    "stable": "Stable",
    "implemented": "Implemented",
    "resolved": "Resolved",
    "candidate_resolved": "Resolved",
    "superseded": "Superseded",
}


def claim_type_label(t):
    return CLAIM_TYPE_LABELS.get(str(t or "").strip(), str(t or "").replace("_", " ").title() or "Claim")


def status_label(s):
    return STATUS_LABELS.get(str(s or "").strip(), str(s or "").replace("_", " ").title())


# ---------------------------------------------------------------------------
# Config + taxonomy
# ---------------------------------------------------------------------------
def load_config():
    with open(CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_function_resolver(cfg):
    groups = cfg.get("cognitive_functions", [])

    def resolve(subject):
        prefix = str(subject or "").split(".")[0].strip().lower()
        for g in groups:
            if prefix in [p.lower() for p in g.get("prefixes", [])]:
                return g["name"]
        return "Other"

    return resolve


# ---------------------------------------------------------------------------
# Evidence overlay
# ---------------------------------------------------------------------------
def load_evidence_index():
    if not CLAIM_EVIDENCE.exists():
        return {}
    try:
        data = json.loads(CLAIM_EVIDENCE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return data.get("claims", {}) if isinstance(data, dict) else {}


def evidence_state(claim, ev):
    """Compute a public evidence label for a claim.
    Returns (state, overlay_dict_or_None)."""
    if str(claim.get("status", "")).strip() == "superseded":
        return "superseded", None
    if not ev:
        return "unresolved", None
    dc = ev.get("direction_counts", {}) or {}
    supports = int(dc.get("supports", 0) or 0)
    weakens = int(dc.get("weakens", 0) or 0)
    mixed = int(dc.get("mixed", 0) or 0)
    total = int(ev.get("entries_total", 0) or 0)
    overlay = {
        "quadrant": ev.get("evidence_quadrant"),
        "supports": supports,
        "weakens": weakens,
        "mixed": mixed,
        "pass_runs": int(ev.get("pass_runs", 0) or 0),
        "fail_runs": int(ev.get("fail_runs", 0) or 0),
        "entries_total": total,
    }
    if total == 0 and supports == 0 and weakens == 0 and mixed == 0:
        return "unresolved", overlay
    if supports > 0 and weakens == 0 and mixed == 0:
        return "supported", overlay
    if weakens > 0 and supports == 0 and mixed == 0:
        return "weakened", overlay
    if supports > 0 or weakens > 0 or mixed > 0:
        return "mixed", overlay
    return "unresolved", overlay


# ---------------------------------------------------------------------------
# Claims export
# ---------------------------------------------------------------------------
def claim_is_public(claim, cfg):
    """Return (is_public, exclusion_reason_or_None)."""
    scope = cfg["scope"]
    if claim.get("deprecated") is True:
        return False, "deprecated"
    status = str(claim.get("status", "")).strip()
    if status not in scope["include_statuses"]:
        return False, f"status:{status or 'none'}"
    phase = str(claim.get("implementation_phase", "")).strip()
    if phase in scope["exclude_implementation_phases"]:
        return False, f"impl_phase:{phase}"
    cat = str(claim.get("epistemic_category", "")).strip()
    if cat in scope["exclude_epistemic_categories"]:
        return False, f"epistemic_category:{cat}"
    return True, None


def export_claims(claims, cfg, ev_index, resolve_fn, redactions):
    # First pass: which claim ids are public (for depends_on filtering).
    public_ids = set()
    for c in claims:
        cid = c.get("id")
        if not cid:
            continue
        ok, reason = claim_is_public(c, cfg)
        if ok:
            public_ids.add(cid)
        else:
            redactions.claim_exclusions[reason] += 1

    out = []
    for c in claims:
        cid = c.get("id")
        if cid not in public_ids:
            continue
        title = scrub(c.get("title", ""), redactions, "claim", "title", cid) or ""
        subject = scrub(c.get("subject", ""), redactions, "claim", "subject", cid) or ""
        state, overlay = evidence_state(c, ev_index.get(cid))
        rec = {
            "id": cid,
            "title": title,
            "claim_type": claim_type_label(c.get("claim_type")),
            "subject": subject,
            "cognitive_function": resolve_fn(c.get("subject")),
            "status": status_label(c.get("status")),
            "epistemic_stance": str(c.get("epistemic_stance", "") or "") or None,
            "evidence_state": state,
            "depends_on": [d for d in (c.get("depends_on") or []) if d in public_ids],
        }
        if str(c.get("claim_type", "")).strip() == "invariant" and c.get("invariant_type"):
            rec["invariant_type"] = c.get("invariant_type")
        if str(c.get("epistemic_category", "")).strip() == "substrate_ceiling":
            rec["limitation"] = "substrate"
        if overlay:
            rec["evidence"] = overlay
        # Drop empty-valued keys for compactness.
        rec = {k: v for k, v in rec.items() if v not in (None, "", [])}
        out.append(rec)
    out.sort(key=lambda r: r["id"])
    return out, public_ids


# ---------------------------------------------------------------------------
# Experiments export
# ---------------------------------------------------------------------------
def iter_manifest_files():
    for f in sorted(EXPERIMENTS_DIR.glob("*.json")):
        if any(tok in f.name for tok in NON_MANIFEST_TOKENS):
            continue
        yield f


def load_reviewed_ids():
    if not REVIEW_TRACKER.exists():
        return set(), set()
    try:
        d = json.loads(REVIEW_TRACKER.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return set(), set()
    return set(d.get("reviewed_run_ids", []) or []), set(d.get("discussed_experiment_dirs", []) or [])


def parse_pending_count():
    """Return the single integer pending count (no breakdown, no IDs)."""
    if not PENDING_REVIEW.exists():
        return None
    try:
        text = PENDING_REVIEW.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.search(r"Pending:\s*\*\*(\d+)\*\*", text)
    if not m:
        m = re.search(r"Pending:\s*(\d+)", text)
    return int(m.group(1)) if m else None


def public_outcome(d):
    direction = str(d.get("evidence_direction", "")).strip()
    if direction == "superseded" or d.get("scoring_excluded") == "superseded":
        return "superseded"
    outcome = str(d.get("outcome", "")).strip().upper()
    if outcome == "PASS":
        return "pass"
    if outcome == "FAIL":
        return "fail"
    return "error"  # ERROR / UNKNOWN / anything else


def derive_exp_id(d):
    src = str(d.get("queue_id") or d.get("experiment_type") or d.get("run_id") or "")
    m = re.search(r"exq[_-]?(\w+?)(?:_|$)", src, re.I)
    if m:
        return "EXQ-" + m.group(1).upper()
    return src.split("_")[0].upper() if src else "EXPERIMENT"


def humanize_title(et):
    et = re.sub(r"^v3_exq_\w+?_", "", str(et or ""))
    et = re.sub(r"_\d{8}T\d{6}Z.*$", "", et)
    return et.replace("_", " ").strip().capitalize() or "Experiment"


def parse_date(d):
    raw = str(d.get("timestamp_utc") or d.get("generated_utc") or "")
    m = re.search(r"(\d{4})-?(\d{2})-?(\d{2})", raw)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None


def export_experiments(public_ids, reviewed_ids, discussed_dirs, redactions):
    out = []
    seen_runs = set()
    for f in iter_manifest_files():
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if not isinstance(d, dict) or "outcome" not in d:
            continue
        run_id = d.get("run_id") or f.stem
        if run_id in seen_runs:
            continue
        # Reviewed gate: run_id reviewed, OR its EXQ dir was discussed.
        exq_id = derive_exp_id(d)
        dir_token = exq_id.replace("EXQ-", "V3-EXQ-")
        if run_id not in reviewed_ids and dir_token not in discussed_dirs:
            redactions.experiment_exclusions["unreviewed"] += 1
            continue
        claim_ids = d.get("claim_ids_tested") or d.get("claim_ids") or []
        public_claim_ids = [c for c in claim_ids if c in public_ids]
        if not public_claim_ids:
            redactions.experiment_exclusions["no_public_claim"] += 1
            continue
        seen_runs.add(run_id)

        caveats = []
        if d.get("non_degenerate") is False:
            caveats.append("Excluded from scoring: test criterion was vacuous (degenerate).")
        if d.get("scoring_excluded"):
            caveats.append(f"Excluded from scoring: {d.get('scoring_excluded')}.")
        note = scrub(d.get("evidence_direction_note"), redactions,
                     "experiment", "summary", run_id)

        rec = {
            "id": exq_id,
            "title": humanize_title(d.get("experiment_type")),
            "status": public_outcome(d),
            "evidence_direction": str(d.get("evidence_direction", "") or "") or None,
            "claim_ids": public_claim_ids,
            "date": parse_date(d),
            "reviewed": True,
        }
        if note:
            rec["summary"] = truncate(note)
        if caveats:
            rec["caveats"] = caveats
        if d.get("supersedes"):
            rec["supersedes"] = scrub(d.get("supersedes"), redactions,
                                      "experiment", "supersedes", run_id)
        if d.get("superseded_by"):
            rec["superseded_by"] = scrub(d.get("superseded_by"), redactions,
                                         "experiment", "superseded_by", run_id)
        rec = {k: v for k, v in rec.items() if v not in (None, "", [])}
        out.append(rec)
    out.sort(key=lambda r: (r.get("date") or "", r["id"]), reverse=True)
    return out


# ---------------------------------------------------------------------------
# Mechanisms (view over public claims)
# ---------------------------------------------------------------------------
MECHANISM_TYPES = {"Invariant", "Architectural commitment", "Mechanism hypothesis", "Substrate design"}


def export_mechanisms(claims_public):
    groups = {}
    for c in claims_public:
        if c["claim_type"] not in MECHANISM_TYPES:
            continue
        fn = c.get("cognitive_function", "Other")
        groups.setdefault(fn, []).append({
            "id": c["id"],
            "title": c["title"],
            "claim_type": c["claim_type"],
            "state": c["evidence_state"],
        })
    out = []
    for fn in sorted(groups):
        members = sorted(groups[fn], key=lambda m: m["id"])
        out.append({"function": fn, "count": len(members), "claims": members})
    out.sort(key=lambda g: g["count"], reverse=True)
    return out


# ---------------------------------------------------------------------------
# Redaction report
# ---------------------------------------------------------------------------
def write_redaction_report(redactions, counts, generated):
    lines = [
        "# Public Explorer -- Redaction & Safety Report",
        "",
        "> Local review artifact. NOT published (lives at repo root, not under `docs/`).",
        "> Review this -- especially the **Manual review required** section -- before",
        "> committing `docs/public_explorer/` and pushing to `master`.",
        "",
        f"Generated: `{generated}`",
        "",
        "## What was published",
        "",
        f"- Public claims: **{counts['claims']}**",
        f"- Public (reviewed) experiments: **{counts['experiments']}**",
        f"- Mechanism-map function groups: **{counts['mechanisms']}**",
        f"- Pending experiments (count only, no detail published): "
        f"**{counts['pending'] if counts['pending'] is not None else 'unknown'}**",
        "",
        "## Claims withheld (by reason)",
        "",
    ]
    if redactions.claim_exclusions:
        for reason, n in redactions.claim_exclusions.most_common():
            lines.append(f"- `{reason}`: {n}")
    else:
        lines.append("- (none)")
    lines += ["", "## Experiments withheld (by reason)", ""]
    if redactions.experiment_exclusions:
        for reason, n in redactions.experiment_exclusions.most_common():
            lines.append(f"- `{reason}`: {n}")
    else:
        lines.append("- (none)")
    lines += [
        "",
        "## Fields always dropped by policy (allowlist)",
        "",
        "Output records are built from an explicit allowlist; every other source",
        "field is dropped unconditionally. Notably withheld: claim `notes`,",
        "`evidence_quality_note`, `implementation_note`, `source`,",
        "`what_would_answer`, internal `location`; experiment `per_seed_results`,",
        "per-arm metrics, `config`, `elapsed_seconds`, machine/path fields.",
        "",
        "## Fields dropped by sensitive-pattern scrub",
        "",
    ]
    if redactions.dropped_fields:
        for key, n in redactions.dropped_fields.most_common():
            lines.append(f"- `{key}`: {n}")
    else:
        lines.append("- (none)")

    lines += ["", "## Manual review required", ""]
    if redactions.pattern_hits:
        lines.append(
            "The following ALLOWLISTED fields tripped the sensitive-pattern scrub "
            "and were dropped. They were intended to be public, so confirm the "
            "match is a true positive (and consider fixing the source):")
        lines.append("")
        lines.append("| record | id | field | pattern | matched |")
        lines.append("|---|---|---|---|---|")
        for h in redactions.pattern_hits[:200]:
            matched = h["matched"].replace("|", "\\|")
            lines.append(
                f"| {h['record_type']} | `{h['record_id']}` | {h['field']} "
                f"| {h['pattern']} | `{matched}` |")
        if len(redactions.pattern_hits) > 200:
            lines.append(f"| ... | ... | ... | ... | (+{len(redactions.pattern_hits) - 200} more) |")
    else:
        lines.append("None -- no allowlisted field tripped the scrub. :white_check_mark:")
    lines.append("")
    REDACTION_REPORT.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Validation (used by --check and by the standalone test module)
# ---------------------------------------------------------------------------
def validate_outputs():
    """Re-read the written output files and assert safety/scope invariants.
    Returns a list of failure strings (empty == pass)."""
    failures = []

    def load(name):
        p = OUT_DIR / name
        if not p.exists():
            failures.append(f"missing output: {name}")
            return None
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            failures.append(f"invalid JSON in {name}: {e}")
            return None

    index = load("index.json")
    claims = load("claims_public.json")
    experiments = load("experiments_public.json")
    mechanisms = load("mechanisms_public.json")
    load("help_wanted.json")

    def scan(obj, path):
        if isinstance(obj, str):
            for name, pat in SENSITIVE_PATTERNS:
                if pat.search(obj):
                    failures.append(f"sensitive pattern '{name}' at {path}: {obj[:80]!r}")
        elif isinstance(obj, dict):
            for k, v in obj.items():
                scan(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                scan(v, f"{path}[{i}]")

    for nm, obj in [("index", index), ("claims", claims),
                    ("experiments", experiments), ("mechanisms", mechanisms)]:
        if obj is not None:
            scan(obj, nm)

    # Allowlist enforcement.
    CLAIM_KEYS = {"id", "title", "claim_type", "subject", "cognitive_function",
                  "status", "epistemic_stance", "evidence_state", "depends_on",
                  "invariant_type", "limitation", "evidence"}
    EXP_KEYS = {"id", "title", "status", "evidence_direction", "claim_ids",
                "date", "reviewed", "summary", "caveats", "supersedes",
                "superseded_by"}
    public_ids = set()
    if isinstance(claims, list):
        for c in claims:
            public_ids.add(c.get("id"))
            extra = set(c) - CLAIM_KEYS
            if extra:
                failures.append(f"claim {c.get('id')} has non-allowlisted keys: {extra}")
        for c in claims:
            for d in c.get("depends_on", []):
                if d not in public_ids:
                    failures.append(f"claim {c.get('id')} depends_on non-public {d}")
    if isinstance(experiments, list):
        for e in experiments:
            extra = set(e) - EXP_KEYS
            if extra:
                failures.append(f"experiment {e.get('id')} has non-allowlisted keys: {extra}")
            if e.get("reviewed") is not True:
                failures.append(f"experiment {e.get('id')} is not marked reviewed")
            for cid in e.get("claim_ids", []):
                if public_ids and cid not in public_ids:
                    failures.append(f"experiment {e.get('id')} links non-public claim {cid}")

    # Pending must be count-only.
    if isinstance(index, dict):
        prc = index.get("pending_review_count")
        if prc is not None and not isinstance(prc, int):
            failures.append("pending_review_count is not a bare integer")
        for forbidden in ("pending_items", "pending_runs", "pending_breakdown"):
            if forbidden in index:
                failures.append(f"index leaks pending detail: {forbidden}")

    return failures


# ---------------------------------------------------------------------------
# Build (no side effects)
# ---------------------------------------------------------------------------
class ExportSourceError(Exception):
    """A canonical source is missing or malformed; the export cannot be built."""


def build_export():
    """Compute the complete public export and WRITE NOTHING.

    Split out of main() so a caller can obtain the scrub `pattern_hits` without
    touching the tracked output directory or the root redaction report.

    That property is load-bearing for scripts/check_public_export_redactions.py,
    which runs on every scheduled refresh: a gate that had to perform the real
    export in order to decide whether the real export is safe would be writing
    the very files it is gating -- and in a shared multi-session checkout that
    is the read-modify-write contamination shape that got the test module
    redirected to a tempdir in 7a6120e3e1. Returning the data instead means the
    gate is a pure read, safe to run anywhere, in any checkout, at any time.

    Returns a dict with keys: index, claims_public, experiments_public,
    mechanisms_public, help_wanted, orientation, redactions, counts, generated.
    Raises ExportSourceError if a canonical source is missing or malformed.
    """
    for required in (CLAIMS_YAML, CONFIG):
        if not required.exists():
            raise ExportSourceError(f"required source missing: {required}")

    cfg = load_config()
    resolve_fn = build_function_resolver(cfg)
    redactions = Redactions()

    claims = yaml.safe_load(CLAIMS_YAML.read_text(encoding="utf-8"))
    if not isinstance(claims, list):
        raise ExportSourceError("claims.yaml top level must be a list")

    ev_index = load_evidence_index()
    reviewed_ids, discussed_dirs = load_reviewed_ids()

    claims_public, public_ids = export_claims(claims, cfg, ev_index, resolve_fn, redactions)
    experiments_public = export_experiments(public_ids, reviewed_ids, discussed_dirs, redactions)
    mechanisms_public = export_mechanisms(claims_public)
    pending_count = parse_pending_count()

    generated = datetime.utcnow().isoformat() + "Z"
    index = {
        "schema_version": cfg["schema_version"],
        "generated_utc": generated,
        "counts": {
            "claims_public": len(claims_public),
            "experiments_public": len(experiments_public),
            "mechanisms": len(mechanisms_public),
        },
        "pending_review_count": pending_count,
        "evidence_overlay_available": bool(ev_index),
        "scope_note": ("Public, read-only view. Settled / V3-relevant claims only; "
                       "future-stage and substrate-conditional claims are withheld. "
                       "Experiments shown only when reviewed; pending work is a count only."),
    }

    return {
        "index": index,
        "claims_public": claims_public,
        "experiments_public": experiments_public,
        "mechanisms_public": mechanisms_public,
        "help_wanted": cfg.get("help_wanted", {}),
        "orientation": cfg.get("orientation", {}),
        "redactions": redactions,
        "counts": {
            "claims": len(claims_public),
            "experiments": len(experiments_public),
            "mechanisms": len(mechanisms_public),
            "pending": pending_count,
        },
        "generated": generated,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Export public REE Explorer data.")
    ap.add_argument("--check", action="store_true",
                    help="After export, run leak/scope validation; non-zero exit on failure.")
    args = ap.parse_args()

    try:
        built = build_export()
    except ExportSourceError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    redactions = built["redactions"]
    counts = built["counts"]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    def dump(name, obj):
        (OUT_DIR / name).write_text(
            json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    dump("index.json", built["index"])
    dump("claims_public.json", built["claims_public"])
    dump("experiments_public.json", built["experiments_public"])
    dump("mechanisms_public.json", built["mechanisms_public"])
    dump("help_wanted.json", built["help_wanted"])
    dump("orientation.json", built["orientation"])

    write_redaction_report(redactions, counts, built["generated"])

    claims_public = built["claims_public"]
    experiments_public = built["experiments_public"]
    mechanisms_public = built["mechanisms_public"]
    pending_count = counts["pending"]

    print(f"Public export written to {OUT_DIR}")
    print(f"  claims_public      : {len(claims_public)} "
          f"(withheld {sum(redactions.claim_exclusions.values())})")
    print(f"  experiments_public : {len(experiments_public)} "
          f"(withheld {sum(redactions.experiment_exclusions.values())})")
    print(f"  mechanisms groups  : {len(mechanisms_public)}")
    print(f"  pending (count)    : {pending_count}")
    print(f"  scrub pattern-hits : {len(redactions.pattern_hits)} "
          f"(see {REDACTION_REPORT.name})")

    if args.check:
        failures = validate_outputs()
        if failures:
            print("\nVALIDATION FAILED:", file=sys.stderr)
            for fmsg in failures:
                print(f"  - {fmsg}", file=sys.stderr)
            return 2
        print("\nValidation passed: no leaks, scope and allowlist clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
