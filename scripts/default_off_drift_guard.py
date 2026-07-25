#!/usr/bin/env python3
"""Standing guard for default-off drift between the claims registry and REEConfig.

WHAT THIS ASKS
--------------
"Is the flag ever ON at all, and does the claim's status admit that it isn't?"

A claim whose registered `status` implies settled architecture, but whose implementing
mechanism sits behind a config knob defaulting to False/0/0.0 that nothing in the
corpus ever turns on, is DRIFT: the registry reading and the substrate reading have
diverged, and the registry reading is what gets cited in governance and in any V3
closure account.

This regenerates the enablement counts of
`REE_assembly/evidence/planning/default_off_drift_audit_2026-07-21.md` (session
`reverent-lamport-d18a32`) so that a one-off report becomes a repeatable check.

ORTHOGONAL TO `ree-v3/tests/test_flag_inertness.py`
---------------------------------------------------
That harness asks the OTHER direction -- "the flag is ON, does the mechanism actually
do anything?" (inertness, F-C1..F-P6). Do NOT merge the two. This script
cross-references it (the `inertness` column) but never defers to it: a flag can be
live-when-on and still never be turned on, and vice versa. The worst cell in the
matrix is a claim that fires in BOTH (ARC-004 in the source audit).

METHOD (as validated 2026-07-21)
--------------------------------
1. Parse the dataclass field region of `ree-v3/ree_core/utils/config.py` and extract
   bool/numeric fields defaulting to False/0/0.0, plus the claim ids appearing in each
   field's preceding comment block. The `from_dims()` block mirrors the same names and
   is excluded to avoid double-counting -- this parse is AST-based, so `from_dims` is a
   FunctionDef body and is structurally excluded rather than excluded by line number.
2. Join knob -> claim against `REE_assembly/docs/claims/claims.yaml`, keeping claims at
   status stable / active / provisional / implemented.
3. For each knob, count files under `ree-v3/experiments/` and `ree-v3/tests/` that set
   it `= True`. THIS ENABLEMENT COUNT IS THE LOAD-BEARING DISCRIMINATOR. Near-zero
   enablement plus a settled status is drift; high enablement (use_harm_stream at 382)
   is a benign config-default-off-but-experiment-default-on artifact.

ATTRIBUTION IS A CANDIDATE, NOT GROUND TRUTH
--------------------------------------------
Claim->knob attribution comes from claim ids in config.py field comments and can be
WRONG. MECH-104 is the worked false positive: `use_phasic_burst` carries MECH-104 in
its comment, but MECH-104's evidence run `v3_exq_365` manipulates `_ema_alpha` on the
default-ON running-variance path instead -- the knob is context in a comment, not the
implementer. That is why every row prints the claim's `live_status.evidence.from` run:
a human must check that the cited run actually exercised the knob before acting on a
finding.

The `attr` column grades that pairing. `decl` means the id heads a comment line
(`# SD-007: ReafferencePredictor -- ...`), the shape a field-declaring comment takes;
`mention` means the id appears mid-prose, which is where the false positives live --
MECH-104 / `use_phasic_burst` grades `mention`, as does `use_soft_competitive_settling`
naming MECH-094 only in a parenthetical about replay ticks.

`attr` IS ADVISORY AND DOES NOT GATE. It is deliberately not wired into the exit code:
suppressing a `mention` pairing would silently drop real drift (`pacc_offline_decay`
names SD-032e mid-prose and is Tier 1 #2 of the source audit; `override_pfc_eta_gain`
names SD-035 mid-prose and is Tier 2 #6). Grade the pairing, do not filter on it.

EXIT STATUS
-----------
0  no un-allowlisted drift
1  at least one claim at `stable` or `implemented` maps to a knob with ZERO
   experiment enablements
2  usage / input error
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuration                                                                #
# --------------------------------------------------------------------------- #

# Claim statuses that assert the mechanism is real (in-scope for the join).
IN_SCOPE_STATUS = ("stable", "active", "provisional", "implemented")

# Statuses that assert SETTLED architecture -- these gate the exit code.
GATING_STATUS = ("stable", "implemented")

CLAIM_ID_RE = re.compile(r"\b(?:SD|MECH|ARC|INV|Q|GAP)-\d+[a-z]?\b")

# A comment line that OPENS with one or more claim ids -- "# SD-007: ..." or
# "# MECH-112 / MECH-117: ..." -- is a field-declaring comment. Ids matched by this
# prefix grade `decl`; ids found only mid-prose grade `mention`. Advisory only.
# No `^` anchor: these are used with .match(line, pos), which already anchors at pos,
# whereas `^` would only ever match at pos 0 and silently truncate the id list to one.
_ID_ONLY_RE = re.compile(r"(?:SD|MECH|ARC|INV|Q|GAP)-\d+[a-z]?")
_ID_SEP_RE = re.compile(r"[\s/,+&]+")

# One pass over the corpus captures every `name = True` / `"name": True` /
# `name=True` site; the report's per-knob grep recipe generalised.
ENABLE_RE = re.compile(r"""([A-Za-z_][A-Za-z0-9_]*)["']?[ \t]*[:=][ \t]*True\b""")

# --------------------------------------------------------------------------- #
# Allowlist -- verified benign 2026-07-21. Do not extend without a written        #
# reason; each entry is a claim the guard would otherwise flag forever.        #
# --------------------------------------------------------------------------- #

ALLOWLIST_CLAIMS = {
    "ARC-007": "live_status verdict records hold_pending_v3_substrate; V3-Pending Gate",
    "ARC-018": "live_status verdict records hold_pending_v3_substrate; V3-Pending Gate",
    "Q-007": "live_status verdict records hold_pending_v3_substrate; V3-Pending Gate",
    "MECH-059": "live_status verdict records hold_candidate_resolve_conflict",
    "MECH-267": "live_status verdict records hold_candidate_resolve_conflict",
}

ALLOWLIST_KNOBS = {
    "use_differentiable_cem": (
        "deliberately held; >=4 experiment manifests record "
        '"NOT FLIPPED (default False; SD-055 safety note)"'
    ),
}

SOURCE_REPORT = "REE_assembly/evidence/planning/default_off_drift_audit_2026-07-21.md"


# --------------------------------------------------------------------------- #
# Data model                                                                   #
# --------------------------------------------------------------------------- #


@dataclass
class Knob:
    name: str
    lineno: int
    owner: str            # dataclass that declares it
    default: str          # rendered default ("False" / "0" / "0.0")
    claim_ids: dict = field(default_factory=dict)   # claim id -> "decl" | "mention"
    exp_files: int = 0
    test_files: int = 0


@dataclass
class Row:
    claim_id: str
    status: str
    knob: Knob
    evidence_from: str
    evidence_verdict: str
    inertness: str
    attr: str             # "decl" | "mention" -- advisory, never gates

    @property
    def gating(self) -> bool:
        """A finding the guard fails on."""
        return (
            self.status in GATING_STATUS
            and self.knob.exp_files == 0
            and self.claim_id not in ALLOWLIST_CLAIMS
            and self.knob.name not in ALLOWLIST_KNOBS
        )


# --------------------------------------------------------------------------- #
# Step 1 -- parse config.py                                                    #
# --------------------------------------------------------------------------- #


def _is_dataclass(node: ast.ClassDef) -> bool:
    for dec in node.decorator_list:
        target = dec.func if isinstance(dec, ast.Call) else dec
        name = getattr(target, "attr", None) or getattr(target, "id", None)
        if name == "dataclass":
            return True
    return False


def _default_off(node: ast.AnnAssign):
    """Return the rendered default if this field defaults to False/0/0.0, else None."""
    val = node.value
    if not isinstance(val, ast.Constant):
        return None
    v = val.value
    if v is False:
        return "False"
    # bool is a subclass of int -- True is already excluded above.
    if isinstance(v, int) and not isinstance(v, bool) and v == 0:
        return "0"
    if isinstance(v, float) and v == 0.0:
        return "0.0"
    return None


def _preceding_comment(lines, lineno: int):
    """Contiguous block of `#` lines immediately above a field declaration."""
    out = []
    i = lineno - 2  # lineno is 1-based; step to the line above
    while i >= 0:
        stripped = lines[i].strip()
        if stripped.startswith("#"):
            out.append(stripped.lstrip("#").strip())
            i -= 1
            continue
        break
    out.reverse()
    return out


def _leading_ids(line: str):
    """Claim ids in the id-list prefix of a comment line, e.g. `MECH-112 / MECH-117:`."""
    ids, pos = [], 0
    while True:
        m = _ID_ONLY_RE.match(line, pos)
        if not m:
            break
        ids.append(m.group(0))
        pos = m.end()
        sep = _ID_SEP_RE.match(line, pos)
        if not sep:
            break
        pos = sep.end()
    return ids


def extract_claim_ids(comment_lines):
    """Map claim id -> attribution grade (`decl` beats `mention`). Advisory only."""
    graded = {}
    for line in comment_lines:
        decl = set(_leading_ids(line))
        for cid in CLAIM_ID_RE.findall(line):
            grade = "decl" if cid in decl else "mention"
            if graded.get(cid) != "decl":
                graded[cid] = grade
    return graded


def parse_knobs(config_py: Path):
    src = config_py.read_text(encoding="utf-8")
    lines = src.splitlines()
    tree = ast.parse(src)

    knobs = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef) or not _is_dataclass(node):
            continue
        for stmt in node.body:
            if not isinstance(stmt, ast.AnnAssign) or not isinstance(stmt.target, ast.Name):
                continue
            rendered = _default_off(stmt)
            if rendered is None:
                continue
            name = stmt.target.id
            if name in knobs:
                # Same field name declared in two dataclasses. Enablement counting is
                # by NAME, so keep the first declaration and do not double-count.
                continue
            comment = _preceding_comment(lines, stmt.lineno)
            # Also fold in a same-line trailing comment.
            trailing = lines[stmt.lineno - 1]
            if "#" in trailing:
                comment.append(trailing.split("#", 1)[1].strip())
            ids = extract_claim_ids(comment)
            knobs[name] = Knob(
                name=name,
                lineno=stmt.lineno,
                owner=node.name,
                default=rendered,
                claim_ids=ids,
            )
    return knobs


# --------------------------------------------------------------------------- #
# Step 2 -- claims registry                                                    #
# --------------------------------------------------------------------------- #


def load_claims(claims_yaml: Path):
    try:
        import yaml
    except ImportError:
        sys.stderr.write(
            "ERROR: PyYAML not available. Run with /opt/local/bin/python3.\n"
        )
        raise SystemExit(2)
    data = yaml.safe_load(claims_yaml.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        sys.stderr.write("ERROR: claims.yaml did not parse as a list.\n")
        raise SystemExit(2)
    return {c["id"]: c for c in data if isinstance(c, dict) and c.get("id")}


def evidence_of(claim):
    ls = claim.get("live_status") or {}
    ev = ls.get("evidence") or {}
    if not isinstance(ev, dict):
        return ("(unparseable live_status.evidence)", "")
    return (ev.get("from") or "(no live_status.evidence)", ev.get("verdict") or "")


# --------------------------------------------------------------------------- #
# Step 3 -- enablement counts                                                  #
# --------------------------------------------------------------------------- #


def count_enablements(roots, knob_names):
    """Files under each root that set any knob `= True`. One pass over the corpus."""
    counts = {root_label: {} for root_label, _ in roots}
    for label, root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.py")):
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            seen = set()
            for m in ENABLE_RE.finditer(text):
                name = m.group(1)
                if name in knob_names:
                    seen.add(name)
            for name in seen:
                counts[label][name] = counts[label].get(name, 0) + 1
    return counts


# --------------------------------------------------------------------------- #
# Cross-reference: test_flag_inertness.py (the OTHER direction)                #
# --------------------------------------------------------------------------- #


def inertness_index(test_path: Path):
    """Return (known_inert_names, all_names_mentioned) from the inertness harness."""
    known_inert, mentioned = set(), set()
    if not test_path.exists():
        return known_inert, mentioned
    src = test_path.read_text(encoding="utf-8")
    for m in re.finditer(r"""["']([a-z_][a-z0-9_]*)["']""", src):
        mentioned.add(m.group(1))
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return known_inert, mentioned
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        if "KNOWN_INERT" not in names or not isinstance(node.value, ast.Dict):
            continue
        for key in node.value.keys:
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                known_inert.add(key.value)
    return known_inert, mentioned


# --------------------------------------------------------------------------- #
# Report                                                                       #
# --------------------------------------------------------------------------- #


STATUS_RANK = {"stable": 0, "implemented": 1, "active": 2, "provisional": 3}


def build_rows(knobs, claims, known_inert, mentioned):
    rows = []
    for knob in knobs.values():
        for cid, attr in knob.claim_ids.items():
            claim = claims.get(cid)
            if claim is None:
                continue
            status = claim.get("status")
            if status not in IN_SCOPE_STATUS:
                continue
            ev_from, ev_verdict = evidence_of(claim)
            if knob.name in known_inert:
                inert = "KNOWN-INERT"
            elif knob.name in mentioned:
                inert = "listed"
            else:
                inert = "-"
            rows.append(
                Row(
                    claim_id=cid,
                    status=status,
                    knob=knob,
                    evidence_from=ev_from,
                    evidence_verdict=ev_verdict,
                    inertness=inert,
                    attr=attr,
                )
            )
    rows.sort(
        key=lambda r: (
            STATUS_RANK.get(r.status, 9),
            r.knob.exp_files,
            r.knob.test_files,
            r.claim_id,
            r.knob.name,
        )
    )
    return rows


def render(rows, knobs, claims, args, out):
    n_default_off = len(knobs)
    n_with_claim = sum(1 for k in knobs.values() if k.claim_ids)
    gating = [r for r in rows if r.gating]
    suppressed = [
        r
        for r in rows
        if r.status in GATING_STATUS
        and r.knob.exp_files == 0
        and not r.gating
    ]

    w = out.write
    w("# Default-off drift audit (regenerated)\n\n")
    w("Generated by `REE_assembly/scripts/default_off_drift_guard.py`.\n")
    w("Method and its known false-positive mode: `%s`.\n\n" % SOURCE_REPORT)
    w(
        "Scope: %d default-off (False/0/0.0) dataclass fields in `%s`, %d carrying a "
        "claim id in their comment block; joined to claims at status %s.\n\n"
        % (
            n_default_off,
            args.config.relative_to(args.base) if _under(args.config, args.base) else args.config,
            n_with_claim,
            "/".join(IN_SCOPE_STATUS),
        )
    )
    w(
        "`exp`/`test` = number of files under `ree-v3/experiments/` and `ree-v3/tests/` "
        "that set the knob `= True`. This count is the load-bearing discriminator: "
        "near-zero enablement plus a settled status is drift; high enablement is a "
        "benign config-default-off-but-experiment-default-on artifact.\n\n"
    )
    w(
        "ATTRIBUTION IS A CANDIDATE. Claim->knob pairing comes from config.py comments "
        "and can be wrong (MECH-104 / `use_phasic_burst` is the worked false positive). "
        "Check the evidence run named in each row before acting on it.\n\n"
    )
    w(
        "`inertness` cross-references `ree-v3/tests/test_flag_inertness.py`, which asks "
        "the ORTHOGONAL question (flag ON -- does it do anything?). The two are not "
        "merged. A row that is both zero-enablement here and KNOWN-INERT there is the "
        "worst cell in the matrix.\n\n"
    )

    w("## Table\n\n")
    w("| Claim | Status | attr | Knob | Default | config.py:line | exp | test | inertness | Evidence run |\n")
    w("|---|---|---|---|---|---|---|---|---|---|\n")
    for r in rows:
        mark = " **<-- FAIL**" if r.gating else (" (allowlisted)" if r.status in GATING_STATUS and r.knob.exp_files == 0 else "")
        ev = r.evidence_from
        if r.evidence_verdict:
            ev = "%s (`%s`)" % (ev, r.evidence_verdict)
        w(
            "| %s | `%s` | %s | `%s` | `%s` | %d | %s | %d | %s | %s%s |\n"
            % (
                r.claim_id,
                r.status,
                r.attr,
                r.knob.name,
                r.knob.default,
                r.knob.lineno,
                ("**%d**" % r.knob.exp_files) if r.knob.exp_files == 0 else str(r.knob.exp_files),
                r.knob.test_files,
                r.inertness,
                ev,
                mark,
            )
        )
    w("\n")

    if suppressed:
        w("## Allowlisted (verified benign 2026-07-21 -- not flagged)\n\n")
        for r in suppressed:
            reason = ALLOWLIST_CLAIMS.get(r.claim_id) or ALLOWLIST_KNOBS.get(r.knob.name, "")
            w("- **%s** / `%s` -- %s\n" % (r.claim_id, r.knob.name, reason))
        w("\n")

    w("## Verdict\n\n")
    if gating:
        w(
            "**FAIL** -- %d claim/knob pair(s) at status `stable`/`implemented` have "
            "ZERO experiment enablements:\n\n" % len(gating)
        )
        for r in gating:
            w(
                "- **%s** (`%s`) -> `%s` (config.py:%d), attribution `%s`, evidence `%s`\n"
                % (
                    r.claim_id,
                    r.status,
                    r.knob.name,
                    r.knob.lineno,
                    r.attr,
                    r.evidence_from,
                )
            )
        n_mention = sum(1 for r in gating if r.attr == "mention")
        if n_mention:
            w(
                "\n%d of those are `mention`-grade pairings -- the claim id appears "
                "mid-prose in the field comment rather than heading it. Verify against "
                "the evidence run before treating them as drift; that is the MECH-104 "
                "failure mode.\n" % n_mention
            )
        w(
            "\nThe fix is NOT a status demotion on the strength of this guard alone. "
            "Per the source report: annotate the claim with a `default_off` block "
            "recording the knob, its `file:line`, and whether the evidence run enabled "
            "it. Demotion is a governance decision on separate evidence.\n"
        )
    else:
        w("**PASS** -- no un-allowlisted zero-enablement knob under a settled claim.\n")
    return gating


def _under(path: Path, base: Path) -> bool:
    try:
        path.relative_to(base)
        return True
    except ValueError:
        return False


# --------------------------------------------------------------------------- #
# Entry point                                                                  #
# --------------------------------------------------------------------------- #


def main(argv=None):
    default_base = Path(
        os.environ.get("REE_WORKING", Path(__file__).resolve().parents[2])
    )
    p = argparse.ArgumentParser(
        description="Regenerate the default-off drift audit and fail on new drift."
    )
    p.add_argument("--base", type=Path, default=default_base, help="REE_Working root")
    p.add_argument("--config", type=Path, default=None, help="path to config.py")
    p.add_argument("--claims", type=Path, default=None, help="path to claims.yaml")
    p.add_argument("--out", type=Path, default=None, help="write the report here")
    p.add_argument("--json", type=Path, default=None, help="also write machine-readable JSON")
    p.add_argument(
        "--no-fail",
        action="store_true",
        help="always exit 0 (report-only; for regenerating the table)",
    )
    args = p.parse_args(argv)

    args.base = args.base.resolve()
    args.config = (args.config or args.base / "ree-v3/ree_core/utils/config.py").resolve()
    args.claims = (args.claims or args.base / "REE_assembly/docs/claims/claims.yaml").resolve()

    for path, what in ((args.config, "config.py"), (args.claims, "claims.yaml")):
        if not path.exists():
            sys.stderr.write("ERROR: %s not found at %s\n" % (what, path))
            return 2

    knobs = parse_knobs(args.config)
    claims = load_claims(args.claims)

    roots = [
        ("exp", args.base / "ree-v3/experiments"),
        ("test", args.base / "ree-v3/tests"),
    ]
    counts = count_enablements(roots, set(knobs))
    for name, knob in knobs.items():
        knob.exp_files = counts["exp"].get(name, 0)
        knob.test_files = counts["test"].get(name, 0)

    known_inert, mentioned = inertness_index(args.base / "ree-v3/tests/test_flag_inertness.py")
    rows = build_rows(knobs, claims, known_inert, mentioned)

    import io

    buf = io.StringIO()
    gating = render(rows, knobs, claims, args, buf)
    text = buf.getvalue()
    sys.stdout.write(text)
    if args.out:
        args.out.write_text(text, encoding="utf-8")

    if args.json:
        payload = {
            "n_default_off_fields": len(knobs),
            "n_fields_with_claim_id": sum(1 for k in knobs.values() if k.claim_ids),
            "rows": [
                {
                    "claim_id": r.claim_id,
                    "status": r.status,
                    "attribution": r.attr,
                    "knob": r.knob.name,
                    "default": r.knob.default,
                    "config_line": r.knob.lineno,
                    "owner_dataclass": r.knob.owner,
                    "exp_files": r.knob.exp_files,
                    "test_files": r.knob.test_files,
                    "inertness": r.inertness,
                    "evidence_from": r.evidence_from,
                    "evidence_verdict": r.evidence_verdict,
                    "gating": r.gating,
                }
                for r in rows
            ],
            "failing": [
                {"claim_id": r.claim_id, "knob": r.knob.name} for r in gating
            ],
        }
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if gating and not args.no_fail:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
