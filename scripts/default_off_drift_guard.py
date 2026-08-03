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
   The parse FOLLOWS `field(default_factory=XConfig)` references to wherever `XConfig`
   is actually declared, which is not always config.py -- see NESTED SUB-CONFIGS below.
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

NESTED SUB-CONFIGS ARE NOT ALL DECLARED IN config.py
----------------------------------------------------
`REEConfig` composes 10 nested sub-config dataclasses via
`goal: GoalConfig = field(default_factory=GoalConfig)`. Two of those classes are declared
in OTHER modules (`GoalConfig` in `ree_core/goal.py`, `SerotoninConfig` in
`ree_core/neuromodulation/serotonin.py`); config.py only imports them. Until 2026-08-03
this parse read config.py's text and nothing else, so every field those two classes
declare was invisible to the guard -- not "unresolved", never considered a knob at all.
`use_hierarchical_goal_credit` (on `GoalConfig`) was the worked case: it did not appear
in `parse_knobs()`'s returned set, which silently defeated the default-off filters in
`check_substrate_staleness_candidates.py` that consume this function as ground truth
(see `evidence/planning/substrate_stability_and_drift_detection_plan.md` section 7.4).

The fix is IMPORT RESOLUTION, not a second hardcoded file list: each
`field(default_factory=XConfig)` (and each `x: XConfig = XConfig()`) is followed to
whichever module actually declares `XConfig`, by reading the declaring module's own
`import` statements and locating the target file on disk, recursively. An 11th nested
config added in a third location tomorrow is picked up with no change here. The files
are AST-PARSED, never imported -- `ree_core/goal.py` imports torch, and this script is
stdlib-only by design.

Two deliberate asymmetries in that walk:
  * The ENTRY module (config.py) contributes EVERY dataclass in it, as before. A
    FOLLOWED module contributes only the specific class that was referenced (plus what
    that class itself references), never every dataclass that happens to live in the
    same file -- `ree_core/goal.py` also declares unrelated classes, and hoovering them
    up would silently widen the knob set beyond what REEConfig actually composes.
  * Name collisions keep the FIRST declaration, and config.py is walked first, so no
    existing knob's `owner`/`lineno`/attribution can be changed by a followed module.

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

# Enablement is judged by AST, not by a `= True` grep, and this matters for
# correctness of the load-bearing discriminator. All in-scope knobs default to a FALSY
# value (False / 0 / 0.0), so an ENABLEMENT is any assignment of a TRUTHY / non-zero
# value -- regardless of bool vs numeric. A `= True`-only scan (the source report's own
# recipe) is blind to two whole classes and manufactures false drift:
#
#   * NUMERIC knobs set by value -- `goal_weight` (MECH-117) defaults 0.0 and is set
#     non-zero in hundreds of corpus files; `harm_history_len` (SD-011) likewise. A
#     `= True` scan calls both zero-enablement drift.
#   * VARIABLE / module-constant RHS -- `override_pfc_eta_gain": ARM3_OVERRIDE_PFC_ETA_GAIN`
#     where `ARM3_OVERRIDE_PFC_ETA_GAIN = 1.0` (SD-035), or `use_offline_wanting_spread=
#     use_spread`. A literal scan misses these; resolving module-level constants recovers
#     them, and an unresolved RHS (`reafference_action_dim=env.action_dim`) is counted as
#     an UNRESOLVED enablement that suppresses a false FAIL rather than being read as off.
#
# The three outcomes per assignment site: ON (truthy/non-zero literal, or a Name that
# resolves through module constants to truthy/non-zero), OFF (falsy/zero -- an explicit
# `=0.0` or `=False`, or an OFF-arm constant, is NOT an enablement), and UNRESOLVED (a
# Name/attribute/expression we cannot evaluate -- almost never zero in practice).

_UNRESOLVED = object()


def _literal_value(node):
    """Python value of a literal AST node (incl. `-1`), else _UNRESOLVED."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        inner = _literal_value(node.operand)
        if isinstance(inner, (int, float)) and not isinstance(inner, bool):
            return -inner if isinstance(node.op, ast.USub) else inner
    return _UNRESOLVED


def _module_constants(tree):
    """Top-level `NAME = <literal>` bindings, for resolving a knob's variable RHS."""
    env = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets, val = node.targets, node.value
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets, val = [node.target], node.value
        else:
            continue
        lit = _literal_value(val)
        if lit is _UNRESOLVED:
            continue
        for t in targets:
            if isinstance(t, ast.Name):
                env[t.id] = lit
    return env


def _classify_rhs(node, env):
    """'on' | 'off' | 'unresolved' for an assignment's right-hand side.

    'on' = a truthy / non-zero value (an enablement, since every in-scope knob defaults
    falsy). 'off' = an explicit falsy/zero value (NOT an enablement). 'unresolved' = a
    value we cannot evaluate.
    """
    lit = _literal_value(node)
    if lit is _UNRESOLVED:
        if isinstance(node, ast.Name) and node.id in env:
            lit = env[node.id]
        else:
            return "unresolved"
    if isinstance(lit, bool):
        return "on" if lit else "off"
    if isinstance(lit, (int, float)):
        return "on" if lit != 0 else "off"
    if lit is None:
        return "off"
    return "unresolved"

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
    source: str = ""      # file the OWNER dataclass is declared in (not always config.py)
    claim_ids: dict = field(default_factory=dict)   # claim id -> "decl" | "mention"
    exp_files: int = 0       # experiment files with a confirmed ON site
    test_files: int = 0      # test files with a confirmed ON site
    exp_unresolved: int = 0  # experiment files whose only sites are UNRESOLVED
    test_unresolved: int = 0


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
        """A finding the guard fails on: a settled claim whose knob has ZERO confirmed
        experiment enablements AND no unresolved experiment sites that might be one.

        The `exp_unresolved == 0` clause is what stops a false FAIL on a knob that IS
        enabled but via an RHS the scanner cannot evaluate (`knob=env.action_dim`).
        """
        return (
            self.status in GATING_STATUS
            and self.knob.exp_files == 0
            and self.knob.exp_unresolved == 0
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


def _collect_class_knobs(node: ast.ClassDef, lines, source: Path, knobs) -> None:
    """Add every default-off field of one dataclass to `knobs` (first declaration wins)."""
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
        knobs[name] = Knob(
            name=name,
            lineno=stmt.lineno,
            owner=node.name,
            default=rendered,
            source=str(source),
            claim_ids=extract_claim_ids(comment),
        )


# --- following `field(default_factory=XConfig)` to wherever XConfig is declared ------ #


def _dotted(node):
    """['a', 'b', 'C'] for `a.b.C`, ['C'] for `C`, None for anything else (lambda, call)."""
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if not isinstance(node, ast.Name):
        return None
    parts.append(node.id)
    parts.reverse()
    return parts


def _import_bindings(tree):
    """Local name -> (module, level, imported_name) for the import forms this resolver reads.

    `from ree_core.goal import GoalConfig`       -> GoalConfig -> ("ree_core.goal", 0, "GoalConfig")
    `from ree_core.goal import GoalConfig as G`  -> G          -> ("ree_core.goal", 0, "GoalConfig")
    `from . import goal`                         -> goal       -> ("",             1, "goal")
    `import ree_core.goal as g`                  -> g          -> ("ree_core.goal", 0, None)
    `import ree_core.goal`                       -> ree_core   -> ("ree_core",      0, None)

    `imported_name` is None for a whole-module binding. It is not None for a `from`-import,
    where the bound name may be EITHER a class in that module or a submodule of it -- the
    resolver tries both rather than guessing from the name.
    """
    bindings = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for alias in node.names:
                if alias.name == "*":
                    continue
                bindings.setdefault(alias.asname or alias.name, (module, node.level, alias.name))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    bindings.setdefault(alias.asname, (alias.name, 0, None))
                else:
                    head = alias.name.split(".")[0]
                    bindings.setdefault(head, (head, 0, None))
    return bindings


def _resolve_module_file(module: str, level: int, origin: Path):
    """Locate the .py file for a module named in `origin`'s imports, or None.

    Absolute imports are searched against every ancestor directory of `origin`,
    nearest first -- that finds `ree-v3/ree_core/goal.py` for `ree_core.goal` imported
    from `ree-v3/ree_core/utils/config.py` without being told where the package root is.
    Relative imports (`level > 0`) are resolved against `origin`'s own package instead.
    """
    parts = [p for p in module.split(".") if p]
    if not parts:
        return None
    if level:
        base = origin.parent
        for _ in range(level - 1):
            base = base.parent
        bases = [base]
    else:
        bases = list(origin.parents)
    for base in bases:
        mod = base.joinpath(*parts[:-1]) / (parts[-1] + ".py")
        if mod.is_file():
            return mod.resolve()
        pkg = base.joinpath(*parts) / "__init__.py"
        if pkg.is_file():
            return pkg.resolve()
    return None


def _resolve_class_ref(parts, bindings, origin: Path):
    """(file, class_name) for a config class referenced as `parts`, or None if unresolvable.

    Unresolvable is the safe answer and is common and benign: `field(default_factory=dict)`
    and `field(default_factory=lambda: ...)` name no importable class at all.
    """
    cls, prefix = parts[-1], parts[:-1]
    if not prefix:
        binding = bindings.get(cls)
        if binding is None:
            return None
        module, level, imported = binding
        if imported is None:      # a module binding used as a bare name -- not a class
            return None
        path = _resolve_module_file(module, level, origin)
        return (path, imported) if path else None
    binding = bindings.get(prefix[0])
    if binding is None:
        return None
    module, level, imported = binding
    mod_parts = [p for p in module.split(".") if p]
    if imported is not None:      # `from . import goal` used as `goal.GoalConfig`
        mod_parts.append(imported)
    mod_parts.extend(prefix[1:])
    path = _resolve_module_file(".".join(mod_parts), level, origin)
    return (path, cls) if path else None


def _nested_config_refs(class_node: ast.ClassDef):
    """Dotted names of the sub-config classes a dataclass composes.

    Both spellings this codebase uses: `x: XConfig = field(default_factory=XConfig)` and
    the plain `x: XConfig = XConfig()`. A `default_factory=lambda: ...` / `=dict` yields
    nothing resolvable and is dropped downstream.
    """
    refs = []
    for stmt in class_node.body:
        if not isinstance(stmt, ast.AnnAssign) or not isinstance(stmt.value, ast.Call):
            continue
        call = stmt.value
        func = _dotted(call.func)
        if func and func[-1] == "field":
            for kw in call.keywords:
                if kw.arg == "default_factory":
                    parts = _dotted(kw.value)
                    if parts:
                        refs.append(parts)
        elif func:
            refs.append(func)
    return refs


def parse_knobs(config_py: Path, max_modules: int = 64):
    """Default-off knobs of config.py AND of every nested sub-config class it composes.

    Returns {field name: Knob}. See NESTED SUB-CONFIGS in the module docstring for why
    this follows imports rather than reading one file: two of REEConfig's 10 nested
    config classes are declared elsewhere, and their fields were invisible to this guard
    entirely until 2026-08-03.

    Best-effort by construction -- an unreadable, unparseable or unlocatable module is
    skipped, never raised. `max_modules` caps how many distinct files a pathological
    import graph can make this parse (the real one reaches 3).
    """
    config_py = Path(config_py).resolve()
    knobs: dict = {}
    cache: dict = {}
    seen = set()
    # (file, class name) work items; class name None means "every dataclass in this
    # file" and is used ONLY for the entry module.
    queue = [(config_py, None)]

    while queue:
        path, want = queue.pop(0)
        if (path, want) in seen:
            continue
        seen.add((path, want))

        parsed = cache.get(path)
        if parsed is None:
            if len(cache) >= max_modules:
                continue
            try:
                src = path.read_text(encoding="utf-8")
                tree = ast.parse(src)
            except (OSError, SyntaxError, ValueError):
                cache[path] = parsed = ([], None, {}, {})
            else:
                parsed = (
                    src.splitlines(),
                    tree,
                    _import_bindings(tree),
                    {
                        n.name: n
                        for n in ast.walk(tree)
                        if isinstance(n, ast.ClassDef) and _is_dataclass(n)
                    },
                )
                cache[path] = parsed
        lines, _tree, bindings, classes = parsed

        if want is None:
            targets = list(classes.values())
        else:
            targets = [classes[want]] if want in classes else []

        for node in targets:
            _collect_class_knobs(node, lines, path, knobs)
            for parts in _nested_config_refs(node):
                if len(parts) == 1 and parts[0] in classes:
                    # Declared in this same file. Already covered when want is None
                    # (every dataclass was queued); otherwise queue it explicitly.
                    if want is not None:
                        queue.append((path, parts[0]))
                    continue
                target = _resolve_class_ref(parts, bindings, path)
                if target is not None:
                    queue.append(target)
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


def _file_knob_sites(tree, knob_names, env):
    """Map knob name -> set of verdicts ({'on','off','unresolved'}) seen in one file.

    Enabling assignments appear as keyword args (`REEConfig(knob=...)`,
    `from_dims(knob=...)`), string-keyed dict entries (`{"knob": ...}`), and plain
    Name/Attribute assignments (`knob = ...`, `cfg.knob = ...`).
    """
    sites = {}

    def note(name, node):
        if name in knob_names:
            sites.setdefault(name, set()).add(_classify_rhs(node, env))

    for node in ast.walk(tree):
        if isinstance(node, ast.keyword) and node.arg:
            note(node.arg, node.value)
        elif isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and isinstance(k.value, str):
                    note(k.value, v)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                nm = t.id if isinstance(t, ast.Name) else getattr(t, "attr", None)
                if nm:
                    note(nm, node.value)
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            nm = getattr(node.target, "id", None) or getattr(node.target, "attr", None)
            if nm:
                note(nm, node.value)
    return sites


def count_enablements(roots, knob_names):
    """Per root, count files that ENABLE each knob. One AST pass over the corpus.

    Returns {label: {knob: {"on": n_files, "unresolved": n_files}}}. A file is counted
    ON if it has any confirmed truthy/non-zero site; else UNRESOLVED if its only sites
    are unevaluable; a file whose sites are all OFF (explicit `=False` / `=0.0`, incl.
    OFF-arm constants) is not counted for that knob at all.
    """
    counts = {label: {} for label, _ in roots}
    for label, root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.py")):
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
                tree = ast.parse(text)
            except (OSError, SyntaxError):
                continue
            env = _module_constants(tree)
            for name, verdicts in _file_knob_sites(tree, knob_names, env).items():
                bucket = counts[label].setdefault(name, {"on": 0, "unresolved": 0})
                if "on" in verdicts:
                    bucket["on"] += 1
                elif "unresolved" in verdicts:
                    bucket["unresolved"] += 1
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

# Rendered declaration sites are relative to this, so the common case stays short
# (`utils/config.py:4342`) while a knob declared elsewhere is visibly elsewhere
# (`goal.py:335`). A bare line number would misattribute the latter to config.py.
_SITE_TRIM = "ree-v3/ree_core/"


def knob_site(knob, base=None) -> str:
    """`utils/config.py:335`-style declaration site for a knob."""
    if not knob.source:
        return str(knob.lineno)
    path = Path(knob.source)
    rel = str(path)
    if base is not None and _under(path, base):
        rel = path.relative_to(base).as_posix()
        if rel.startswith(_SITE_TRIM):
            rel = rel[len(_SITE_TRIM):]
    else:
        rel = path.name
    return "%s:%d" % (rel, knob.lineno)


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
    # "suppressed" = would gate on the zero-confirmed-enablement rule, but is held off
    # ONLY by the allowlist (not by unresolved sites -- those aren't a benign hold).
    suppressed = [
        r
        for r in rows
        if r.status in GATING_STATUS
        and r.knob.exp_files == 0
        and r.knob.exp_unresolved == 0
        and not r.gating
    ]

    w = out.write
    w("# Default-off drift audit (regenerated)\n\n")
    w("Generated by `REE_assembly/scripts/default_off_drift_guard.py`.\n")
    w("Method and its known false-positive mode: `%s`.\n\n" % SOURCE_REPORT)
    w(
        "Scope: %d default-off (False/0/0.0) dataclass fields in `%s` **and in the nested "
        "sub-config classes it composes** (two of which -- `GoalConfig`, `SerotoninConfig` "
        "-- are declared in other modules and are followed by import resolution), %d "
        "carrying a claim id in their comment block; joined to claims at status %s.\n\n"
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
    w(
        "`exp`/`test` show confirmed-ON files; a `+N?` suffix is files whose only site "
        "is an UNRESOLVED RHS (a variable the scanner could not evaluate) -- possible "
        "enablements that suppress a FAIL. `declared at` is relative to "
        "`ree-v3/ree_core/`, since not every knob is declared in config.py.\n\n"
    )
    w("| Claim | Status | attr | Knob | Default | declared at | exp | test | inertness | Evidence run |\n")
    w("|---|---|---|---|---|---|---|---|---|---|\n")

    def cell(on, unresolved):
        s = ("**%d**" % on) if on == 0 else str(on)
        if unresolved:
            s += " (+%d?)" % unresolved
        return s

    for r in rows:
        if r.gating:
            mark = " **<-- FAIL**"
        elif (
            r.status in GATING_STATUS
            and r.knob.exp_files == 0
            and r.knob.exp_unresolved == 0
            and (r.claim_id in ALLOWLIST_CLAIMS or r.knob.name in ALLOWLIST_KNOBS)
        ):
            mark = " (allowlisted)"
        else:
            mark = ""
        ev = r.evidence_from
        if r.evidence_verdict:
            ev = "%s (`%s`)" % (ev, r.evidence_verdict)
        w(
            "| %s | `%s` | %s | `%s` | `%s` | %s | %s | %s | %s | %s%s |\n"
            % (
                r.claim_id,
                r.status,
                r.attr,
                r.knob.name,
                r.knob.default,
                knob_site(r.knob, args.base),
                cell(r.knob.exp_files, r.knob.exp_unresolved),
                cell(r.knob.test_files, r.knob.test_unresolved),
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
                "- **%s** (`%s`) -> `%s` (%s), attribution `%s`, evidence `%s`\n"
                % (
                    r.claim_id,
                    r.status,
                    r.knob.name,
                    knob_site(r.knob, args.base),
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
        exp = counts["exp"].get(name, {"on": 0, "unresolved": 0})
        test = counts["test"].get(name, {"on": 0, "unresolved": 0})
        knob.exp_files = exp["on"]
        knob.test_files = test["on"]
        knob.exp_unresolved = exp["unresolved"]
        knob.test_unresolved = test["unresolved"]

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
                    # `config_line` is the line in `source_file`, which is NOT always
                    # config.py -- the key name predates nested-config resolution.
                    "config_line": r.knob.lineno,
                    "source_file": knob_site(r.knob, args.base).rsplit(":", 1)[0],
                    "owner_dataclass": r.knob.owner,
                    "exp_files": r.knob.exp_files,
                    "test_files": r.knob.test_files,
                    "exp_unresolved": r.knob.exp_unresolved,
                    "test_unresolved": r.knob.test_unresolved,
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
