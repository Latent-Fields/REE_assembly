#!/usr/bin/env python3
"""Cross-check an evidence manifest's arm-degeneracy ANNOTATION against the
per-seed arm DATA in the SAME manifest.

WHY THIS EXISTS (confirmed incident, 2026-07-30, REE_assembly eabe9c453b,
session beautiful-newton-3dca0f):
Three V3-EXQ-673 MECH-171 manifests asserted IN PROSE that their three arms
DIFFERED -- and therefore deliberately omitted `non_degenerate` /
`degeneracy_reason` -- while `per_seed_comparisons` in the very same files showed
ARM_A == ARM_B == ARM_C on slot_diversity, eval_harm AND late_pred_loss for every
seed (42/49/56), with late_pred_loss == 0.0. The defect was introduced 2026-07-20,
survived ten days, and was caught only because a human happened to read the note
beside the numbers. Nothing in the repo audited for this class.

It was scoring-harmless in that instance -- build_experiment_indexes.py hits
`continue` on both the `degenerate` and the `non_contributory` branch, so neither
label weights confidence -- but that was LUCK, not design. The same mistake in the
other direction (flag omitted on a run whose evidence_direction is NOT an excluded
bucket) mints a SCORED experimental entry out of a vacuous run.

WHAT THIS CHECKS -- two directions, deliberately asymmetric in how hard they are
to trigger:

  (a) DEGENERATE-BUT-UNFLAGGED. Every arm exactly equal on every comparable
      per-seed metric, in every comparable container, yet `non_degenerate` is
      absent/true and `non_degenerate_per_claim` records no degeneracy. This is
      the confirmed incident's signature.

  (b) FLAGGED-BUT-DISCRIMINATIVE. `non_degenerate: false` is set on an
      ARM-IDENTITY justification while the arms demonstrably differ. Rarer, but it
      de-weights real evidence, so it is the more costly direction.

DESIGN DECISIONS THAT DECIDE WHETHER THIS IS USABLE -- read before editing:

  * ARM STRUCTURE IS DISCOVERED BY SHAPE, NEVER BY NAME. `arm_a`/`arm_b`/`arm_c`
    is one family's convention, not the corpus's. Surveyed 2026-07-30 over 3412
    manifests, three shapes exist and all three are supported:
        A  list of per-seed dicts carrying `arm_<id>_<metric>` keys
           (`per_seed_comparisons`; 11 files -- the incident's own shape)
        B  dict {arm_label: [per-seed row dicts]}
           (`per_seed_results` 42, `all_results` 22, `seed_results`, `per_arm`, ...)
        C  list of row dicts each carrying an arm-label field
           (`arm_results[arm_id]` 147, `arm_results[arm]` 106, `per_seed_rows`,
            `cells[condition]`, `summary_table`, `arms`, ...)
    Container names, arm ids, arm-label field names and metric names are all read
    off the data. A new family with a new spelling is picked up for free; a
    hardcoded list would have covered 11 of ~400 comparable manifests.

  * A MANIFEST WITH NO COMPARABLE ARM STRUCTURE IS A **NOTE**, NOT A FINDING.
    ~3000 of 3412 are in that bucket -- single-arm runs, diagnostics, literature
    entries, dry-run smoke packs, aggregate-only summaries. There is no second
    representation to disagree, so there is nothing to check. Flagging them would
    bury the real findings, which is the explicit lesson recorded for
    scripts/audit_vendored_copies.py's NOTE-vs-finding split.

  * TWO THRESHOLDS, WITH A DELIBERATE DEAD ZONE BETWEEN THEM. Direction (a)
    requires EXACT equality (`==`); direction (b) requires a MATERIAL difference
    (abs delta > max(1e-12, 1e-9 * max|a|,|b|)). A pair differing by 1e-17 is
    therefore neither "identical" (so (a) cannot fire) nor "demonstrably
    different" (so (b) cannot fire). That gap is the point: float noise produces
    silence in both directions rather than a coin-flip finding. The confirmed
    incident was bit-exact, so nothing real is lost by making (a) strict.

  * (a) REQUIRES AN UNAMBIGUOUS SIGNATURE. Every arm equal on EVERY comparable
    metric across EVERY shared seed, in EVERY comparable container. Partial
    equality is not degeneracy and must not fire. When a manifest carries several
    comparable containers (673 carries both `per_seed_comparisons` and
    `all_results`) they must ALL be degenerate; one discriminating container
    vetoes the finding.
    Known and accepted cost: a run whose arms are identical on every DV but carry
    a differing MANIPULATION INDICATOR (`rem_enabled`, `sd016_on`, `reef_on`) is
    NOT flagged -- v3_exq_670_inv048_pharm_sleep is the live example, and it is
    correctly annotated by hand anyway. Separating a manipulation flag from a
    measurement would be a judgement call, and a checker that makes judgement
    calls about which columns "count" is one that argues with its users.

  * (b) IS SCOPED TO ARM-IDENTITY JUSTIFICATIONS ONLY, AND THAT SCOPING IS THE
    WHOLE DIFFICULTY. `non_degenerate: false` is set for many reasons that have
    nothing to do with arm identity -- readiness below floor, precondition unmet,
    non-vacuity gate RED in every arm, zero spread on one named DV,
    substrate_not_ready, superseded. In most of those the arms genuinely DO
    differ, and a naive "flagged but arms differ" test fires on nearly all 84
    flagged manifests in the corpus. So a reason counts as an arm-identity
    assertion only when it either
        (i) LEADS with a global phrase ("All arms identical (...)"), or
       (ii) carries an explicit arm equation `X==Y(==Z)` whose tokens resolve to
            at least two arm ids DISCOVERED IN THIS MANIFEST -- self-validating,
            so prose that merely contains '==' cannot trigger it, or
      (iii) LEADS with a named-metric assertion ("<metric> byte-identical across
            all 4 sleep arms"), in which case ONLY that metric is checked.
    "Leads with" is load-bearing. v3_exq_805_arc016 is the live counter-example:
    its reason is a non-vacuity verdict that ends "...makes every arm identical --
    exactly the state that voided EXQ-396a/b". That is an explanatory clause about
    a hypothetical, not a claim about this run's data, and an unanchored
    "contains" test reports it as a finding. An assertion is what a reason LEADS
    with.

  * BOTH COPIES OF EVERY MANIFEST ARE CHECKED, and the indexer's own precedence
    rule decides which ANNOTATION is effective. build_experiment_indexes.py
    (`_merge_flat_manifest_overrides`) overlays the flat copy onto the pack ONLY
    when the flat is annotated and the pack is not; otherwise the pack stays
    authoritative. That rule is mirrored here rather than reinvented, so this
    checker adjudicates the annotation the INDEXER will actually score. Direction
    (a) additionally consults BOTH copies before firing: a degeneracy recorded in
    either place is a governance decision already taken.

  * THE DATA COPY IS CHOSEN SEPARATELY FROM THE ANNOTATION COPY, and conflating
    them silently guts the checker. The run-pack `manifest.json` is a MAPPED
    projection, not a duplicate -- build_runpack_docs maps a whitelist, and the
    bulky per-arm containers are mostly not on it. Measured 2026-07-30: preferring
    the pack as the data source finds arm structure in 11 of 2688 runs, versus 394
    when taking whichever copy actually carries it. So the richer copy wins, and
    when both carry data whose degeneracy verdicts DISAGREE, that is reported and
    neither direction fires.

  * A FLAT/PACK ANNOTATION DIFFERENCE IS ONLY A FINDING WHEN IT IS A GENUINE
    CONFLICT: the field PRESENT IN BOTH copies with different values, both copies
    annotated, and the field direction-bearing (`non_degenerate`,
    `non_degenerate_per_claim` -- not `degeneracy_reason`, whose prose never moves
    the scoring math; the same split the indexer draws with
    _FLAT_DIRECTION_FIELDS). "Present in one, absent in the other" is producer lag
    that the overlay resolves and the indexer already warns about, and it is
    systemic: 241 live runs, essentially all `pack=<absent> vs flat=...`. Reporting
    that shape yields 242 findings and buries the ~21 real ones -- measured, both
    with the naive test and with a both-annotated test that still admits it,
    because `_is_annotated` returns True off an unrelated `evidence_direction_note`.
    It is surfaced as an aggregate NOTE count instead.

  * DETECTION ONLY. This never rewrites a manifest. The remedy for (a) is a
    /failure-autopsy adjudication that decides WHY the arms collapsed, which is
    not something a lint can infer.

Exit code: 0 by default even with findings (advisory, chains safely inside
governance.sh), matching scripts/check_closure_links.py,
scripts/check_closure_drift.py and scripts/check_plan_status_table_sync.py. Pass
--exit-nonzero to gate.

ASCII-only stdout per repo convention.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_manifest_degeneracy_consistency.py
    /opt/local/bin/python3 scripts/check_manifest_degeneracy_consistency.py --run-id v3_exq_673_..._v3
    /opt/local/bin/python3 scripts/check_manifest_degeneracy_consistency.py --file evidence/experiments/x.json
    /opt/local/bin/python3 scripts/check_manifest_degeneracy_consistency.py --exit-nonzero   # gate
    /opt/local/bin/python3 scripts/check_manifest_degeneracy_consistency.py --quiet-notes    # findings only
    /opt/local/bin/python3 scripts/check_manifest_degeneracy_consistency.py --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS_DIR = REPO_ROOT / "evidence" / "experiments"

# --- shape discovery ---------------------------------------------------------

# Shape A key: `arm_a_slot_diversity` -> arm 'a', metric 'slot_diversity'.
# Non-greedy on neither side: the arm id is the FIRST token, the metric is the
# rest. `arm_a_late_pred_loss` must yield ('a', 'late_pred_loss'), not
# ('a_late_pred', 'loss').
_ARM_METRIC_KEY_RE = re.compile(r"^arm[_-]([A-Za-z0-9]+)[_-](.+)$")

# Candidate arm-LABEL field names for shape C / row-level labels. Ordered: the
# more specific spellings win, so a row carrying both `arm_id` and `arm` is keyed
# on `arm_id`. Every one of these is attested in the corpus.
LABEL_KEYS = ("arm_id", "arm_name", "arm_label", "arm", "condition", "variant")

# Candidate per-seed key names. A row lacking all of them is keyed by position,
# which is correct for the emit order the drivers use (seed-major within arm --
# see [memory] reference on manifest per-arm field ordering).
SEED_KEYS = ("seed", "seed_index", "cell_seed", "seed_id")

# Never treated as a measured metric: the label and seed columns themselves.
_NON_METRIC_KEYS = frozenset(LABEL_KEYS) | frozenset(SEED_KEYS)

# --- annotation fields -------------------------------------------------------

# Mirrors build_experiment_indexes.py::_ANNOTATION_MARKER_FIELDS. Kept as a
# literal rather than imported: that module lives under evidence/experiments/
# (not scripts/), it is heavy, and importing it would couple a lint to the
# indexer's import side effects. The values are pinned by a regression test.
_ANNOTATION_MARKER_FIELDS = (
    "evidence_direction_note",
    "degeneracy_reason",
    "superseded_by",
    "superseded_by_substrate",
)

# The degeneracy-annotation fields this checker adjudicates.
_DEGENERACY_FIELDS = ("non_degenerate", "non_degenerate_per_claim", "degeneracy_reason")

# The subset that is DIRECTION-bearing, i.e. can change how a run scores. Mirrors
# the degeneracy slice of build_experiment_indexes.py::_FLAT_DIRECTION_FIELDS --
# `degeneracy_reason` is deliberately NOT in it there or here, because a prose
# difference between the two copies never moves the scoring math.
_DEGENERACY_DIRECTION_FIELDS = ("non_degenerate", "non_degenerate_per_claim")

# --- (b) reason classification -----------------------------------------------

# (i) A GLOBAL arm-identity assertion, anchored at the START of the reason.
#     Live positive: "All arms identical (ARM_A==ARM_B==ARM_C on every metric)
#     and late_pred_loss==0.0".
_GLOBAL_IDENTITY_LEAD_RE = re.compile(
    r"^\W*(?:all|every|the)\s+arms?\s+(?:are\s+|were\s+)?(?:byte[- ])?identical", re.I)

# (ii) An explicit arm equation. Tokens are validated against the arm ids
#      actually discovered in the manifest, so prose containing '==' cannot fire
#      this on its own.
_ARM_EQUATION_RE = re.compile(r"\b([A-Za-z][A-Za-z0-9_]*)\s*==\s*([A-Za-z][A-Za-z0-9_]*)"
                              r"(?:\s*==\s*([A-Za-z][A-Za-z0-9_]*))*")
_EQ_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_]*")

# (iii) A NAMED-METRIC identity assertion, anchored at the START.
#       Live positive: "harm_discrimination byte-identical across all 4 sleep
#       arms: run_sleep_cycle never trains ...".
_NAMED_METRIC_LEAD_RE = re.compile(
    r"^\W*([A-Za-z][A-Za-z0-9_]*)\s+(?:is\s+|are\s+|was\s+|were\s+)?"
    r"(?:byte[- ])?identical\s+(?:across|in|between|on)\b[^:.]*\barms?\b", re.I)


def _norm_arm_token(token: str) -> str:
    """Normalise an arm identifier for cross-shape matching.

    The same arm surfaces under different spellings in different containers of
    the SAME manifest: 673's shape-A keys yield 'a' while its shape-B keys yield
    'ARM_A_HEALTHY', and its prose equation says 'ARM_A'. Lowercase and strip a
    leading 'arm_' so all three reduce to a common stem ('a', 'a_healthy', 'a'),
    which prefix-matching can then relate.
    """
    t = str(token).strip().lower()
    t = re.sub(r"^arm[_-]", "", t)
    return t


def _arm_token_matches(token: str, arm_ids: list[str]) -> bool:
    """True when a prose token plausibly names one of the discovered arms."""
    t = _norm_arm_token(token)
    if not t:
        return False
    for a in arm_ids:
        n = _norm_arm_token(a)
        if n == t or n.startswith(t) or t.startswith(n):
            return True
    return False


# --- value comparison --------------------------------------------------------

def _scalar(value: Any) -> Any:
    """Return the value if it is a comparable scalar measurement, else None.

    bool is admitted (gate outcomes are real per-arm readouts) but must be tested
    BEFORE int, since bool is an int subclass. Strings, lists and dicts are not
    compared: a list-valued field like `sleep_quality_metrics` or
    `per_seed_behav_contact_rate` is a nested series, and comparing it as a unit
    would let one long identical list dominate the verdict.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        if value != value:  # NaN -- never equal to itself, never comparable
            return None
        return value
    return None


def _exactly_equal(a: Any, b: Any) -> bool:
    """Bit-level equality, with bool and number kept distinct.

    `True == 1` in Python, so a bool arm value would compare equal to a numeric
    one and silently support a degeneracy verdict across a type change. Require
    the same kind.
    """
    if isinstance(a, bool) != isinstance(b, bool):
        return False
    return a == b


def _materially_different(a: Any, b: Any) -> bool:
    """True only when the two values differ by more than float noise.

    See the module docstring: the gap between this test and _exactly_equal is a
    deliberate dead zone in which NEITHER direction fires.
    """
    if isinstance(a, bool) or isinstance(b, bool):
        return bool(a) != bool(b) or isinstance(a, bool) != isinstance(b, bool)
    fa, fb = float(a), float(b)
    return abs(fa - fb) > max(1e-12, 1e-9 * max(abs(fa), abs(fb)))


# --- arm-table extraction ----------------------------------------------------

class ArmTable:
    """A comparable per-arm/per-seed metric table discovered in a manifest.

    `arms` maps arm_id -> seed_key -> {metric: scalar}. `shape` is 'A', 'B' or 'C'
    and `container` names where it came from, both purely for reporting -- the
    comparison logic is shape-agnostic once extracted.
    """

    __slots__ = ("shape", "container", "arms")

    def __init__(self, shape: str, container: str, arms: dict):
        self.shape = shape
        self.container = container
        self.arms = arms

    @property
    def arm_ids(self) -> list[str]:
        return sorted(self.arms)

    def by_metric(self) -> dict[str, dict[Any, dict[str, Any]]]:
        """metric -> seed -> {arm: value}."""
        out: dict[str, dict[Any, dict[str, Any]]] = defaultdict(lambda: defaultdict(dict))
        for arm, seeds in self.arms.items():
            for seed, mets in seeds.items():
                for metric, value in mets.items():
                    out[metric][seed][arm] = value
        return {m: {s: dict(a) for s, a in seeds.items()} for m, seeds in out.items()}


def _row_seed(row: dict, fallback: Any) -> Any:
    for key in SEED_KEYS:
        if key in row:
            value = row[key]
            if isinstance(value, (str, int, float)) and not isinstance(value, bool):
                return value
    return fallback


def _row_metrics(row: dict) -> dict[str, Any]:
    out = {}
    for key, value in row.items():
        if key in _NON_METRIC_KEYS:
            continue
        scalar = _scalar(value)
        if scalar is not None:
            out[key] = scalar
    return out


def _extract_shape_a(key: str, rows: list) -> ArmTable | None:
    """list of per-seed dicts carrying `arm_<id>_<metric>` keys."""
    arms: dict[str, dict] = defaultdict(dict)
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        seed = _row_seed(row, i)
        for k, v in row.items():
            m = _ARM_METRIC_KEY_RE.match(k)
            if not m:
                continue
            scalar = _scalar(v)
            if scalar is None:
                continue
            arms[m.group(1)].setdefault(seed, {})[m.group(2)] = scalar
    return ArmTable("A", key, dict(arms)) if len(arms) >= 2 else None


def _extract_shape_b(key: str, mapping: dict) -> ArmTable | None:
    """dict {arm_label: [per-seed row dicts]}."""
    arms: dict[str, dict] = defaultdict(dict)
    for arm, rows in mapping.items():
        if not isinstance(arm, str) or not isinstance(rows, list):
            return None
        for i, row in enumerate(rows):
            if not isinstance(row, dict):
                return None
            mets = _row_metrics(row)
            if mets:
                arms[arm][_row_seed(row, i)] = mets
    return ArmTable("B", key, dict(arms)) if len(arms) >= 2 else None


def _extract_shape_c(key: str, rows: list) -> ArmTable | None:
    """list of row dicts each carrying an arm-label field."""
    for label in LABEL_KEYS:
        labels = {r.get(label) for r in rows
                  if isinstance(r, dict) and isinstance(r.get(label), str)}
        if len(labels) < 2:
            continue
        arms: dict[str, dict] = defaultdict(dict)
        for i, row in enumerate(rows):
            if not isinstance(row, dict):
                continue
            arm = row.get(label)
            if not isinstance(arm, str):
                continue
            mets = _row_metrics(row)
            if mets:
                arms[arm][_row_seed(row, i)] = mets
        if len(arms) >= 2:
            return ArmTable("C", f"{key}[{label}]", dict(arms))
        return None
    return None


def discover_arm_tables(manifest: dict) -> list[ArmTable]:
    """Find every comparable per-arm/per-seed metric table in a manifest.

    Top-level containers only. A nested search would pull in `params`,
    `acceptance_checks` and per-episode traces, whose "arms" are not arms; every
    attested per-arm container in the corpus is top-level.
    """
    tables: list[ArmTable] = []
    if not isinstance(manifest, dict):
        return tables
    for key, value in manifest.items():
        if isinstance(value, list) and value and all(isinstance(x, dict) for x in value):
            table = _extract_shape_a(key, value)
            if table is not None:
                tables.append(table)
            if len(value) >= 2:
                table = _extract_shape_c(key, value)
                if table is not None:
                    tables.append(table)
        elif isinstance(value, dict) and len(value) >= 2:
            values = list(value.values())
            if all(isinstance(x, list) and x and all(isinstance(y, dict) for y in x)
                   for x in values):
                table = _extract_shape_b(key, value)
                if table is not None:
                    tables.append(table)
    return tables


# --- verdicts ----------------------------------------------------------------

class TableVerdict:
    __slots__ = ("table", "n_comparisons", "n_metrics", "n_seeds",
                 "all_exactly_equal", "differing_metrics")

    def __init__(self, table: ArmTable):
        self.table = table
        by_metric = table.by_metric()
        self.n_comparisons = 0
        self.all_exactly_equal = True
        differing: set[str] = set()
        seeds: set = set()
        metrics: set[str] = set()
        for metric, per_seed in by_metric.items():
            for seed, by_arm in per_seed.items():
                if len(by_arm) < 2:
                    continue  # metric not measured on >=2 arms for this seed
                self.n_comparisons += 1
                seeds.add(seed)
                metrics.add(metric)
                values = list(by_arm.values())
                head = values[0]
                if any(not _exactly_equal(head, v) for v in values[1:]):
                    self.all_exactly_equal = False
                if any(_materially_different(head, v) for v in values[1:]):
                    differing.add(metric)
        self.n_metrics = len(metrics)
        self.n_seeds = len(seeds)
        self.differing_metrics = sorted(differing)

    @property
    def usable(self) -> bool:
        return self.n_comparisons > 0


def classify_reason(reason: str, arm_ids: list[str]) -> tuple[str, str | None]:
    """Classify a degeneracy_reason as an arm-identity assertion or not.

    Returns ``(kind, metric)`` where kind is one of:
      'global'  -- asserts all arms identical across metrics (metric is None)
      'metric'  -- asserts one named metric is identical across arms
      'other'   -- not an arm-identity assertion; out of this checker's scope

    See the module docstring for why 'leads with' and the arm-id validation are
    both load-bearing.
    """
    text = str(reason or "").strip()
    if not text:
        return "other", None

    m = _NAMED_METRIC_LEAD_RE.match(text)
    if m:
        # Guard against the global phrase being read as a metric name: "All arms
        # identical..." would otherwise yield metric='All'.
        if not _GLOBAL_IDENTITY_LEAD_RE.match(text):
            return "metric", m.group(1)

    if _GLOBAL_IDENTITY_LEAD_RE.match(text):
        return "global", None

    for m in _ARM_EQUATION_RE.finditer(text):
        tokens = _EQ_TOKEN_RE.findall(m.group(0))
        if sum(1 for t in tokens if _arm_token_matches(t, arm_ids)) >= 2:
            return "global", None

    return "other", None


def _covered_by_per_claim(manifest: dict) -> bool:
    """True when `non_degenerate_per_claim` records degeneracy for any claim.

    Deliberately permissive: ANY False entry means the run's degeneracy is at
    least partly annotated, so direction (a) stays silent. Being conservative
    here costs recall on a partially-annotated manifest and buys a checker that
    does not argue with a governance decision already taken.
    """
    per_claim = manifest.get("non_degenerate_per_claim")
    if not isinstance(per_claim, dict):
        return False
    return any(v is False for v in per_claim.values())


def _is_dry_run(manifest: dict) -> bool:
    if manifest.get("dry_run") is True:
        return True
    params = manifest.get("params")
    return isinstance(params, dict) and params.get("dry_run") is True


def _is_annotated(manifest: dict) -> bool:
    """Mirrors build_experiment_indexes.py::_is_annotated."""
    if not isinstance(manifest, dict):
        return False
    return any(str(manifest.get(f, "") or "").strip() for f in _ANNOTATION_MARKER_FIELDS)


def effective_annotation(flat: dict | None, pack: dict | None) -> tuple[dict, str]:
    """Which copy's degeneracy annotation the INDEXER will actually score.

    Mirrors build_experiment_indexes.py::_merge_flat_manifest_overrides: the flat
    copy overlays the pack ONLY when the flat is annotated and the pack is not.
    Returns (annotation_source_manifest, label).
    """
    if pack is None:
        return (flat or {}), "flat"
    if flat is None:
        return pack, "pack"
    if _is_annotated(flat) and not _is_annotated(pack):
        return flat, "flat (overlaid onto pack -- flat annotated, pack not)"
    return pack, "pack"


# --- per-run check -----------------------------------------------------------

MIN_COMPARISONS = 2


def check_run(run_id: str, forms: dict[str, tuple[Path, dict]],
              min_comparisons: int = MIN_COMPARISONS) -> dict:
    """Cross-check one run's degeneracy annotation against its own arm data.

    `forms` maps 'flat'/'pack' -> (path, parsed manifest). Data verdicts are
    computed on whichever form carries arm data (they are byte-identical by
    convention; a data disagreement is itself reported).
    """
    res: dict[str, Any] = {
        "run_id": run_id,
        "findings": [],
        "notes": [],
        "forms": sorted(forms),
        "n_tables": 0,
        "n_comparisons": 0,
    }

    flat = forms.get("flat", (None, None))[1]
    pack = forms.get("pack", (None, None))[1]

    # --- flat/pack disagreement -- scoped to the indexer's GENUINE-CONFLICT case
    # The indexer distinguishes two flat/pack shapes and this checker mirrors that
    # split rather than reporting every difference:
    #   * flat annotated, pack NOT -- the DESIGNED overlay path. The flat
    #     correction wins, the indexer already prints "flat-manifest correction
    #     applied ... Re-sync to silence", and it is systemic (the run-pack mapper
    #     is a whitelist, so a pack materialised before a field was mapped simply
    #     lacks it). Measured 2026-07-30: reporting this shape yields 242 findings,
    #     almost all `pack=<absent> vs flat=true` -- a producer-lag census, not a
    #     per-run defect, and exactly the pile that buries the ~20 real ones. It is
    #     counted as an aggregate NOTE instead.
    #   * BOTH copies annotated and disagreeing on a DIRECTION field -- a genuine
    #     conflict the overlay refuses to resolve (the pack is retained), so it
    #     needs a human. That is the finding.
    if flat is not None and pack is not None:
        disagree = []
        for field in _DEGENERACY_DIRECTION_FIELDS:
            in_flat, in_pack = field in flat, field in pack
            if not in_flat and not in_pack:
                continue
            if in_flat != in_pack or flat.get(field) != pack.get(field):
                disagree.append((field,
                                 pack.get(field) if in_pack else "<absent>",
                                 flat.get(field) if in_flat else "<absent>"))
        if disagree:
            # A GENUINE conflict needs the field PRESENT IN BOTH copies with
            # different values. "Present in one, absent in the other" is producer
            # lag however annotated the two copies are overall -- the run-pack
            # mapper is a whitelist, so a pack materialised before a field was
            # mapped simply lacks it, and `_is_annotated` says True off an
            # unrelated `evidence_direction_note`. Measured 2026-07-30: requiring
            # both-annotated alone still yields 36 findings, every one of them
            # `pack=<absent> vs flat=...`.
            both_present = [d for d in disagree
                            if d[1] != "<absent>" and d[2] != "<absent>"]
            if both_present and _is_annotated(flat) and _is_annotated(pack):
                disagree = both_present
                res["findings"].append({
                    "kind": "flat_pack_disagreement",
                    "detail": (
                        "both copies carry a governance annotation but disagree on a "
                        "direction-bearing degeneracy field; the indexer retains the PACK and "
                        "asks for manual reconcile -- "
                        + "; ".join(f"{f}: pack={_short(p)} vs flat={_short(fl)}"
                                    for f, p, fl in disagree)),
                })
            else:
                res["overlay_lag"] = [f for f, _, _ in disagree]

    annotation, ann_label = effective_annotation(flat, pack)
    res["annotation_source"] = ann_label

    # --- arm data ------------------------------------------------------------
    # The DATA copy is chosen independently of the ANNOTATION copy, and that split
    # is not cosmetic. The run-pack `manifest.json` is a MAPPED projection, not a
    # copy: build_runpack_docs maps a whitelist of fields, and the bulky per-arm
    # containers are mostly not on it. Measured 2026-07-30 -- preferring the pack
    # as the data source finds arm structure in 11 of 2688 runs; taking whichever
    # copy actually carries it finds 394. So use the richer copy, and when both
    # carry data that disagree on the verdict, say so and fire nothing.
    candidates: dict[str, list] = {}
    for label, manifest in (("flat", flat), ("pack", pack)):
        if manifest is None:
            continue
        found = [v for v in (TableVerdict(t) for t in discover_arm_tables(manifest)) if v.usable]
        if found:
            candidates[label] = found
    data_label, usable = max(
        candidates.items(),
        key=lambda kv: sum(v.n_comparisons for v in kv[1]),
        default=("none", []))
    res["data_source"] = data_label
    if len(candidates) == 2:
        verdict_by_copy = {
            lab: (all(v.all_exactly_equal for v in vs),
                  sorted({m for v in vs for m in v.differing_metrics}))
            for lab, vs in candidates.items()}
        if verdict_by_copy["flat"][0] != verdict_by_copy["pack"][0]:
            res["notes"].append(
                "flat and pack carry per-arm data that DISAGREE on whether the arms are "
                "identical -- the two copies are supposed to be byte-identical; reconcile "
                "them before this run's annotation can be cross-checked")
            res["n_tables"] = len(usable)
            res["n_comparisons"] = sum(v.n_comparisons for v in usable)
            return res
    res["n_tables"] = len(usable)
    res["n_comparisons"] = sum(v.n_comparisons for v in usable)

    if not usable:
        res["notes"].append(
            "no comparable per-arm structure (single-arm run, diagnostic, "
            "literature entry, or aggregate-only pack) -- nothing to cross-check")
        return res

    shape_desc = "; ".join(
        f"{v.table.container} [{v.table.shape}] {len(v.table.arm_ids)} arms x "
        f"{v.n_seeds} seed(s) x {v.n_metrics} metric(s) = {v.n_comparisons} comparison(s)"
        for v in usable)
    res["shape"] = shape_desc

    all_exact = all(v.all_exactly_equal for v in usable)
    differing = sorted({m for v in usable for m in v.differing_metrics})
    arm_ids = sorted({a for v in usable for a in v.table.arm_ids})

    nd = annotation.get("non_degenerate")
    reason = annotation.get("degeneracy_reason")

    # --- (a) DEGENERATE-BUT-UNFLAGGED ---------------------------------------
    if all_exact and not differing:
        if _is_dry_run(annotation) or any(_is_dry_run(m) for m in (flat, pack) if m):
            res["notes"].append(
                f"arms identical across {res['n_comparisons']} comparison(s) but this is a "
                "dry_run smoke pack -- not a finding")
        elif res["n_comparisons"] < min_comparisons:
            res["notes"].append(
                f"arms identical but only {res['n_comparisons']} comparison(s) -- below the "
                f"min-comparisons floor of {min_comparisons}, too thin to call degenerate")
        elif any(m.get("non_degenerate") is False or _covered_by_per_claim(m)
                 for m in (flat, pack) if m is not None):
            # Correctly annotated -- the corrected V3-EXQ-673 trio lands here.
            # Tested across BOTH copies, not just the effective one: a degeneracy
            # recorded in either place is a governance decision already taken, and
            # this checker must not re-open it just because the overlay rule
            # happens to surface the other copy.
            pass
        else:
            res["findings"].append({
                "kind": "degenerate_unflagged",
                "detail": (
                    f"every arm ({', '.join(arm_ids)}) is EXACTLY equal on every comparable "
                    f"per-seed metric ({res['n_comparisons']} comparison(s) across "
                    f"{len(usable)} container(s)), but non_degenerate="
                    f"{_short(nd) if 'non_degenerate' in annotation else '<absent>'} and "
                    "non_degenerate_per_claim records no degeneracy"),
                "shape": shape_desc,
                "arms": arm_ids,
                "n_comparisons": res["n_comparisons"],
            })
        return res

    # --- (b) FLAGGED-BUT-DISCRIMINATIVE --------------------------------------
    if nd is False:
        kind, metric = classify_reason(reason, arm_ids)
        if kind == "global":
            if differing:
                res["findings"].append({
                    "kind": "flagged_but_discriminative",
                    "detail": (
                        "degeneracy_reason asserts the arms are identical, but "
                        f"{len(differing)} metric(s) differ materially across arms: "
                        + ", ".join(differing[:8])
                        + (f" (+{len(differing) - 8} more)" if len(differing) > 8 else "")),
                    "reason": str(reason)[:200],
                    "shape": shape_desc,
                    "arms": arm_ids,
                    "assertion": "global",
                })
        elif kind == "metric":
            if metric in differing:
                res["findings"].append({
                    "kind": "flagged_but_discriminative",
                    "detail": (
                        f"degeneracy_reason asserts '{metric}' is identical across arms, but it "
                        "differs materially across arms in this manifest's own per-seed data"),
                    "reason": str(reason)[:200],
                    "shape": shape_desc,
                    "arms": arm_ids,
                    "assertion": f"metric:{metric}",
                })
            elif not any(metric in v.table.by_metric() for v in usable):
                res["notes"].append(
                    f"degeneracy_reason names metric '{metric}' as identical across arms, but no "
                    "comparable per-arm container carries that metric -- not cross-checked")
        elif not str(reason or "").strip():
            res["notes"].append(
                "non_degenerate:false with no degeneracy_reason -- the justification cannot be "
                "cross-checked against the arm data")
        # kind == 'other': the flag rests on a non-arm-identity justification
        # (readiness floor, non-vacuity, zero spread, substrate_not_ready).
        # Out of scope by design -- silent, see the module docstring.

    return res


def _short(value: Any, width: int = 60) -> str:
    text = json.dumps(value) if not isinstance(value, str) else value
    text = re.sub(r"\s+", " ", str(text)).strip()
    return text if len(text) <= width else text[:width - 3] + "..."


# --- corpus walk -------------------------------------------------------------

def _load(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def collect_runs(base_dir: Path) -> dict[str, dict[str, tuple[Path, dict]]]:
    """Walk the corpus ONCE, grouping both forms of each manifest by run_id.

    Single pass on purpose: the tree holds ~13k files and re-globbing per check
    is the cost pattern the ree-v3 corpus-lint contracts were rewritten to avoid
    (tests/contracts/conftest.py, 2026-07-28).
    """
    runs: dict[str, dict[str, tuple[Path, dict]]] = defaultdict(dict)
    for path in sorted(base_dir.glob("*.json")):
        manifest = _load(path)
        if manifest is None:
            continue
        run_id = manifest.get("run_id") or path.stem
        if isinstance(run_id, str) and run_id:
            runs[run_id]["flat"] = (path, manifest)
    for path in sorted(base_dir.glob("*/runs/*/manifest.json")):
        manifest = _load(path)
        if manifest is None:
            continue
        run_id = manifest.get("run_id") or path.parent.name
        if isinstance(run_id, str) and run_id:
            runs[run_id]["pack"] = (path, manifest)
    return dict(runs)


KIND_LABEL = {
    "degenerate_unflagged": "DEGENERATE BUT UNFLAGGED",
    "flagged_but_discriminative": "FLAGGED BUT DISCRIMINATIVE",
    "flat_pack_disagreement": "FLAT/PACK DISAGREEMENT",
}


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Cross-check manifest degeneracy annotations against their own per-seed arm data.")
    ap.add_argument("--dir", type=str, default=None,
                    help="evidence/experiments directory to scan (default: repo's)")
    ap.add_argument("--run-id", type=str, default=None, help="check a single run_id")
    ap.add_argument("--file", type=str, default=None,
                    help="check a single manifest file (both forms are NOT resolved)")
    ap.add_argument("--min-comparisons", type=int, default=MIN_COMPARISONS,
                    help=f"floor below which an all-equal table is too thin to call "
                         f"degenerate (default {MIN_COMPARISONS})")
    ap.add_argument("--exit-nonzero", action="store_true",
                    help="exit 1 if any finding is reported (default exits 0 -- advisory)")
    ap.add_argument("--quiet-notes", action="store_true",
                    help="suppress the NOTE section (findings only)")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = ap.parse_args()

    if args.file:
        path = Path(args.file)
        if not path.is_absolute() and not path.exists():
            path = REPO_ROOT / args.file
        manifest = _load(path)
        if manifest is None:
            print(f"check_manifest_degeneracy_consistency: {path} unreadable or not a JSON object")
            return 0
        form = "pack" if path.name == "manifest.json" else "flat"
        run_id = manifest.get("run_id") or path.stem
        results = [check_run(run_id, {form: (path, manifest)}, args.min_comparisons)]
    else:
        base = Path(args.dir) if args.dir else EXPERIMENTS_DIR
        if not base.exists():
            print(f"check_manifest_degeneracy_consistency: {base} not found -- nothing to check")
            return 0
        runs = collect_runs(base)
        if args.run_id:
            runs = {k: v for k, v in runs.items() if k == args.run_id}
            if not runs:
                print(f"check_manifest_degeneracy_consistency: no manifest for run_id {args.run_id}")
                return 0
        results = [check_run(rid, forms, args.min_comparisons)
                   for rid, forms in sorted(runs.items())]

    findings = [(r, f) for r in results for f in r["findings"]]
    comparable = [r for r in results if r["n_tables"]]

    if args.json:
        print(json.dumps({
            "runs_scanned": len(results),
            "runs_with_comparable_arm_data": len(comparable),
            "findings": [dict(f, run_id=r["run_id"]) for r, f in findings],
            "notes": [{"run_id": r["run_id"], "note": n} for r in results for n in r["notes"]],
        }, indent=2, sort_keys=True))
        return 1 if (findings and args.exit_nonzero) else 0

    print("=== check_manifest_degeneracy_consistency: annotation vs the manifest's own arm data ===")
    print(f"Scanned {len(results)} run(s); {len(comparable)} carry a comparable per-arm/per-seed "
          f"structure ({sum(r['n_comparisons'] for r in comparable)} arm comparisons).")
    no_data = len(results) - len(comparable)
    if no_data:
        print(f"NOTE: {no_data} run(s) have no comparable per-arm structure (single-arm, "
              f"diagnostic, literature, aggregate-only) -- nothing to cross-check.")
    overlay_lag = [r for r in results if r.get("overlay_lag")]
    if overlay_lag:
        print(f"NOTE: {len(overlay_lag)} run(s) have a degeneracy field in the flat copy that the "
              f"run-pack copy lacks or contradicts, with only ONE copy annotated -- the indexer's "
              f"overlay resolves these and already warns on them; not counted as findings.")

    if not findings:
        print("OK: every degeneracy annotation agrees with its manifest's own per-seed arm data.")
    else:
        by_kind: dict[str, list] = {}
        for r, f in findings:
            by_kind.setdefault(f["kind"], []).append((r, f))
        for kind in ("flagged_but_discriminative", "degenerate_unflagged", "flat_pack_disagreement"):
            items = by_kind.get(kind)
            if not items:
                continue
            print("")
            print(f"--- {KIND_LABEL[kind]} ({len(items)})")
            for r, f in sorted(items, key=lambda x: x[0]["run_id"]):
                print(f"  {r['run_id']}  [{'+'.join(r['forms'])}]")
                print(f"    {f['detail']}")
                if f.get("shape"):
                    print(f"    data: {f['shape']}")
                if f.get("reason"):
                    print(f"    reason: {_short(f['reason'], 150)}")

    notes = [(r["run_id"], n) for r in results for n in r["notes"]
             if "no comparable per-arm structure" not in n]
    if notes and not args.quiet_notes:
        print("")
        print(f"NOTES ({len(notes)}) -- uncheckable or below-floor cases, not findings:")
        for rid, n in notes:
            print(f"  {rid}: {n}")

    print("")
    print(f"check_manifest_degeneracy_consistency: {len(findings)} finding(s).")
    if any(f["kind"] == "degenerate_unflagged" for _, f in findings):
        print("A DEGENERATE BUT UNFLAGGED run needs a /failure-autopsy adjudication, not a lint fix:")
        print("the arms collapsing is the finding, and WHY they collapsed decides whether the run")
        print("is degenerate, out_of_domain, or substrate_not_ready. Do NOT mass-set non_degenerate.")
    if findings and args.exit_nonzero:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
