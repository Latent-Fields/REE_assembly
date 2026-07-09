#!/usr/bin/env python3
"""Compute the two cognitive-architecture-graveyard health ratios.

Recommendation #1 of `docs/architecture/cognitive_architecture_graveyard.md`
(WS-8 of `evidence/planning/ree_ai_design_critique_plan.md`): surface two health
ratios as first-class, periodically-reported numbers so the graveyard's central
failure mode -- "the architecture becomes ever more complete while capability
stalls" -- is *visible* rather than felt. Making the ratio visible is the whole
mitigation; you cannot manage what you never measure.

The two ratios:

  1. capability-earning claims : registered claims
     Count of registered claims that have lifted a capability metric on a
     substrate above the competence floor, over total registered claims.
     STATUS: the numerator is NOT yet measurable -- no claim-level
     "has this lifted a capability metric" flag exists in claims.yaml. This
     script reports the denominator (registered claims) and the numerator as
     UNMEASURED, with a pointer to the design note that scopes the missing flag.
     See cognitive_architecture_graveyard.md "Ratio #1 -- the missing flag".

  2. governance-mass : cognitive-mass  (the cheap commit-classification proxy)
     A rough proxy of effort spent managing the theory (registry + queue + sync
     + governance-derive + review bookkeeping) versus effort that moved a
     capability metric (substrate builds). Computed from `git log` over a
     trailing window across REE_assembly + ree-v3 by classifying each commit
     subject by its prefix. Two readings are reported:
       - PRIMARY (doc's literal cheap proxy): fraction of commits that are
         machine-written coordination data (phase3 / phase3-queue /
         phase3-heartbeats / igw-ledger). ~60-77% per the source critique.
       - REFINEMENT (coarse, prefix-heuristic): governance-mass (machine
         coordination + human bookkeeping) : cognitive-mass (substrate builds),
         with per-bucket tallies dumped so a human can sanity-check the split.

This is INSTRUMENTATION, not a claim change. PROMOTES NOTHING. It never gates
anything and always exits 0.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/graveyard_health_ratios.py
    /opt/local/bin/python3 scripts/graveyard_health_ratios.py --days 30 --markdown

Importable: `from graveyard_health_ratios import compute_ratios, render_markdown`.
generate_closure_snapshot.py imports render_markdown to append a "Graveyard
health ratios" section to the closure dashboard every governance run.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]          # REE_assembly/
WORKSPACE_ROOT = REPO_ROOT.parent                        # REE_Working/
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"

# Repos swept for the commit-classification proxy. Both are the shared trunk of
# the coordination-data plane (phase3 writers) + the executable-code plane.
COMMIT_REPOS = [
    ("REE_assembly", WORKSPACE_ROOT / "REE_assembly"),
    ("ree-v3", WORKSPACE_ROOT / "ree-v3"),
]

DEFAULT_WINDOW_DAYS = 30

# --- Commit-subject classification (coarse, prefix-based, judgment-laden) -----
#
# Buckets are matched in order; the FIRST matching prefix wins. Everything is
# lowercased first. These are heuristics over free-text commit subjects, so a
# handful will always be misclassified -- the tallies are dumped verbatim so the
# split can be audited, and the ratio is explicitly labelled a proxy.

# A: machine-written coordination data -- the sync_daemon phase3 writers + the
# IGW routine's automated ledger. This is the doc's literal "cheap proxy"
# numerator. Emitted continuously by machines; cheap-to-emit but not free (every
# human/agent must read and not-corrupt it).
MACHINE_COORDINATION = (
    "phase3-heartbeats",
    "phase3-queue",
    "phase3",
    "igw-ledger",
)

# B: human-written governance / bookkeeping -- effort spent managing the theory
# rather than producing cognition (registry edits, the queue, governance cycles,
# reviews, closure/plan reconciles, autopsies, thought-intake, session-land).
# Per the doc these are governance-mass alongside bucket A.
HUMAN_GOVERNANCE = (
    "governance",
    "session",
    "review",
    "workset",
    "closure-map",
    "closure map",
    "closure",
    "thought-intake",
    "thought-digestion",
    "thought",
    "failure-autopsy",
    "autopsy",
    "claim-synthesis",
    "claim synthesis",
    "claims",
    "claim",
    "indexer",
    "index",
    "plan-doc",
    "planning",
    "plan",
    "lit-pull-am",
    "lit-pull",
    "inter-governance",
    "insights",
    "morning",
    "digest",
    "sync",
    "queue-experiment",     # queuing an experiment is queue machinery (governance-mass)
    "queue",
    "dispatch",
    "cowork",
)

# C: cognitive / substrate -- effort that (attempts to) move a capability metric:
# substrate builds, the learned-substrate code, mechanism/architecture BUILD
# commits, tests of the substrate.
COGNITIVE_SUBSTRATE = (
    "implement-substrate",
    # NB: bare "substrate" is deliberately NOT here -- it would steal
    # "substrate_queue*" (queue bookkeeping = governance-mass, bucket B).
    "rung-",
    "mech-",
    "arc-",
    "sd-",
    "inv-",
    "q-0",
    "ree_core",
    "ree-v3/ree_core",
    "coordinator",
    "runner",
    "test",
    "build",
)

# D: neutral / other -- tooling, docs, site, not clearly governance or cognition.
# Reported but held OUT of the governance:cognitive ratio denominator so neither
# side is inflated by presentation churn.
NEUTRAL = (
    "docs",
    "doc(",
    "docs(",
    "explorer",
    "serve",
    "readme",
    "claude.md",
    "site",
    "pages",
    "fishtank",
    "goblin",
    "version-layering",
    "whimsy",
    "contributor",
)


def _prefix_key(subject: str) -> str:
    """Lowercased subject, whitespace-collapsed, for prefix matching."""
    return re.sub(r"\s+", " ", subject.strip().lower())


def classify_commit(subject: str) -> str:
    """Return one of: machine_coordination | human_governance | cognitive | neutral.

    Coarse prefix heuristic over the free-text commit subject. Machine
    coordination is tested first (it is the highest-volume + most reliable
    signal), then cognitive/substrate (so an 'implement-substrate' commit is
    never stolen by a generic word), then human governance, then neutral.
    Unmatched subjects fall through to 'neutral' (uncounted in the ratio).
    """
    s = _prefix_key(subject)
    for p in MACHINE_COORDINATION:
        if s.startswith(p):
            return "machine_coordination"
    for p in COGNITIVE_SUBSTRATE:
        if s.startswith(p):
            return "cognitive"
    for p in HUMAN_GOVERNANCE:
        if s.startswith(p):
            return "human_governance"
    for p in NEUTRAL:
        if s.startswith(p):
            return "neutral"
    return "neutral"


def _git_subjects(repo_path: Path, days: int) -> list[str]:
    """Commit subjects in `repo_path` over the trailing `days`-day window."""
    if not (repo_path / ".git").exists():
        return []
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_path), "log",
             f"--since={days} days ago", "--pretty=format:%s"],
            capture_output=True, text=True, timeout=60, check=False,
        )
    except Exception:
        return []
    if out.returncode != 0:
        return []
    return [ln for ln in out.stdout.splitlines() if ln.strip()]


def count_registered_claims() -> int:
    """Total registered claims = count of top-level `- id:` entries in claims.yaml."""
    try:
        text = CLAIMS_YAML.read_text(encoding="utf-8")
    except OSError:
        return 0
    return len(re.findall(r"^- id:", text, flags=re.MULTILINE))


def compute_commit_ratio(days: int = DEFAULT_WINDOW_DAYS) -> dict:
    """Classify commits across COMMIT_REPOS and roll up the governance/cognitive split."""
    per_repo = {}
    buckets = {"machine_coordination": 0, "human_governance": 0,
               "cognitive": 0, "neutral": 0}
    total = 0
    for name, path in COMMIT_REPOS:
        subs = _git_subjects(path, days)
        rb = {"machine_coordination": 0, "human_governance": 0,
              "cognitive": 0, "neutral": 0}
        for s in subs:
            b = classify_commit(s)
            rb[b] += 1
            buckets[b] += 1
        rb["total"] = len(subs)
        per_repo[name] = rb
        total += len(subs)

    governance_mass = buckets["machine_coordination"] + buckets["human_governance"]
    cognitive_mass = buckets["cognitive"]
    # PRIMARY proxy: machine-coordination fraction of ALL commits (doc's cheap number).
    machine_frac = (buckets["machine_coordination"] / total) if total else 0.0
    # REFINEMENT: governance:cognitive ratio (neutral excluded from both sides).
    gov_cog_ratio = (governance_mass / cognitive_mass) if cognitive_mass else None
    gov_frac = (governance_mass / (governance_mass + cognitive_mass)
                if (governance_mass + cognitive_mass) else 0.0)

    return {
        "days": days,
        "total_commits": total,
        "per_repo": per_repo,
        "buckets": buckets,
        "governance_mass": governance_mass,
        "cognitive_mass": cognitive_mass,
        "machine_coordination_fraction": machine_frac,
        "governance_cognitive_ratio": gov_cog_ratio,
        "governance_fraction": gov_frac,
    }


def compute_ratios(days: int = DEFAULT_WINDOW_DAYS) -> dict:
    """Compute both graveyard health ratios. Ratio #1 numerator is UNMEASURED."""
    registered = count_registered_claims()
    commit = compute_commit_ratio(days)
    return {
        "ratio1": {
            "name": "capability-earning claims : registered claims",
            "registered_claims": registered,
            "capability_earning_claims": None,     # no flag exists yet
            "measurable": False,
            "note": ("No claim-level capability-earning flag exists in "
                     "claims.yaml yet; numerator is unmeasured. Design note: "
                     "docs/architecture/cognitive_architecture_graveyard.md "
                     "'Ratio #1 -- the missing flag'."),
        },
        "ratio2": commit,
    }


def _fmt_ratio(r) -> str:
    if r is None:
        return "n/a (no cognitive-mass commits in window)"
    return f"{r:.0f} : 1"


def render_markdown(data: dict | None = None, days: int = DEFAULT_WINDOW_DAYS) -> str:
    """Render the 'Graveyard health ratios' section for the closure dashboard.

    Returns a self-contained markdown block (no leading/trailing blank-line
    assumptions). Safe to call with data=None (it computes fresh).
    """
    if data is None:
        data = compute_ratios(days)
    r1 = data["ratio1"]
    r2 = data["ratio2"]
    b = r2["buckets"]
    d = r2["days"]

    L: list[str] = []
    L.append("## Graveyard health ratios")
    L.append("")
    L.append(
        "The two health signals from "
        "[`docs/architecture/cognitive_architecture_graveyard.md`]"
        "(architecture/cognitive_architecture_graveyard.html) "
        "(recommendation #1). The graveyard's central failure mode is an "
        "architecture that grows ever more complete while capability stalls "
        "(Soar / ACT-R); making these ratios **visible** is the whole "
        "mitigation. **PROMOTES NOTHING** -- instrumentation, not a claim change."
    )
    L.append("")

    # --- Ratio 2 (computable) ---
    L.append("### Ratio 2 -- governance-mass : cognitive-mass  (commit proxy)")
    L.append("")
    L.append(
        f"Cheap first proxy over the last **{d} days** of commits across "
        f"`REE_assembly` + `ree-v3` ({r2['total_commits']} commits). Coarse, "
        "prefix-based, and judgment-laden by construction -- read the per-bucket "
        "tallies below, not just the headline."
    )
    L.append("")
    L.append(
        f"- **Machine coordination data** (the doc's literal cheap proxy: "
        f"`phase3*` / `igw-ledger` -- sync_daemon + IGW writers): "
        f"**{r2['machine_coordination_fraction'] * 100:.0f}%** of all commits "
        f"({b['machine_coordination']} / {r2['total_commits']}). "
        "The source critique's ~60-77% estimate, live."
    )
    L.append(
        f"- **Governance-mass : cognitive-mass** (refinement -- machine "
        f"coordination + human bookkeeping vs substrate builds; neutral tooling/"
        f"docs excluded): **{_fmt_ratio(r2['governance_cognitive_ratio'])}** "
        f"(governance {r2['governance_mass']} : cognitive {r2['cognitive_mass']})."
    )
    L.append("")
    L.append("Bucket tally (both repos, window):")
    L.append("")
    L.append("| bucket | commits | what it is |")
    L.append("|--------|--------:|------------|")
    L.append(f"| machine coordination | {b['machine_coordination']} | "
             "`phase3*` result/queue/heartbeat writers + `igw-ledger` (automated) |")
    L.append(f"| human governance | {b['human_governance']} | "
             "registry, queue, governance cycles, reviews, closure/plan reconciles, autopsies, thought-intake, session-land |")
    L.append(f"| cognitive / substrate | {b['cognitive']} | "
             "`implement-substrate`, MECH/ARC/SD builds, `ree_core` code, substrate tests -- effort that (tries to) move a capability metric |")
    L.append(f"| neutral / other | {b['neutral']} | "
             "docs, explorer/serve, site, tooling (excluded from the ratio) |")
    L.append("")
    L.append(
        "> Reading: a very high ratio is the graveyard signal, not a bug to "
        "'fix' by suppressing coordination commits. It is only a problem if, "
        "cycle after cycle, governance is busy while capability is flat. The "
        "governance mass is justified *only* as a falsification engine that "
        "kills dead structure -- never as a substitute for earning capability."
    )
    L.append("")

    # --- Ratio 1 (not yet measurable) ---
    L.append("### Ratio 1 -- capability-earning claims : registered claims  (owed)")
    L.append("")
    L.append(
        f"- Registered claims (denominator): **{r1['registered_claims']}**."
    )
    L.append(
        "- Capability-earning claims (numerator): **UNMEASURED** -- no "
        "claim-level \"has this lifted a capability metric on a competent "
        "substrate\" flag exists in `claims.yaml` yet. On the conversion-ceiling "
        "lineage the honest lower bound is ~0 (the all-ON agent forages below "
        "the competence floor; see `failure_autopsy_V3-EXQ-719a`)."
    )
    L.append(
        "- Design note for the missing flag: "
        "[`cognitive_architecture_graveyard.md` -> \"Ratio #1 -- the missing "
        "flag\"](architecture/cognitive_architecture_graveyard.html). Populating "
        "it is gated on the WS-3 capability yardstick (a substrate above the "
        "competence floor to measure against)."
    )
    L.append("")
    return "\n".join(L)


def _print_human(data: dict) -> None:
    r1 = data["ratio1"]
    r2 = data["ratio2"]
    b = r2["buckets"]
    print("=== Cognitive-architecture graveyard health ratios ===")
    print(f"(commit window: last {r2['days']} days; PROMOTES NOTHING)")
    print("")
    print("Ratio 1 -- capability-earning claims : registered claims")
    print(f"  registered claims (denominator): {r1['registered_claims']}")
    print("  capability-earning claims (numerator): UNMEASURED (no flag yet)")
    print("  -> see graveyard doc 'Ratio #1 -- the missing flag'")
    print("")
    print("Ratio 2 -- governance-mass : cognitive-mass (commit proxy)")
    print(f"  total commits (REE_assembly + ree-v3): {r2['total_commits']}")
    print(f"  machine-coordination fraction (doc's cheap proxy): "
          f"{r2['machine_coordination_fraction'] * 100:.0f}%")
    print(f"  governance:cognitive ratio (refinement): "
          f"{_fmt_ratio(r2['governance_cognitive_ratio'])}")
    print("  buckets:")
    for k in ("machine_coordination", "human_governance", "cognitive", "neutral"):
        print(f"    {k:22s}: {b[k]}")
    print("  per-repo:")
    for name, rb in r2["per_repo"].items():
        print(f"    {name:14s}: total={rb['total']:5d}  "
              f"machine={rb['machine_coordination']:5d}  "
              f"human_gov={rb['human_governance']:4d}  "
              f"cognitive={rb['cognitive']:4d}  neutral={rb['neutral']:4d}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Compute graveyard health ratios (instrumentation).")
    ap.add_argument("--days", type=int, default=DEFAULT_WINDOW_DAYS,
                    help=f"trailing commit window in days (default {DEFAULT_WINDOW_DAYS})")
    ap.add_argument("--markdown", action="store_true",
                    help="print the closure-dashboard markdown section instead of the human summary")
    args = ap.parse_args(argv)

    data = compute_ratios(args.days)
    if args.markdown:
        print(render_markdown(data, args.days))
    else:
        _print_human(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
