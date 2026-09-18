"""Coordinator routing adapter for REE_assembly writers -- PHASE-4.

WHY THIS FILE EXISTS
--------------------
`phase4_routing_compliance_20260918.md` (DP-12's measurement) found that
phase-4 routing compliance "tracks writer topology, not flag state". Its
structural finding, in one line: **`grep -rl coordinator_transport
REE_assembly/scripts/` returned ZERO files** while the umbrella returned 72.
The coordinator client simply did not exist in this repo, so every routed path
a REE_assembly tool writes was *structurally* un-routable -- no matter what the
machine's client flags said. Worst case measured:
`evidence/planning/experiment_proposals.v1.json` at **4.4% routed**, flag armed,
58 of 68 commits since the route went live from writers with no call site at
all, across three boxes.

This module removes that structural blocker. It does NOT by itself convert any
writer: a writer still has to call it.

WHY A VENDORED COPY AND NOT A CROSS-REPO IMPORT
-----------------------------------------------
`coordinator_transport.py` is vendored BYTE-IDENTICAL from the canonical copy at
`REE_Working/scripts/coordinator_transport.py` and registered in
`scripts/audit_vendored_copies.py` `VENDOR_SETS` (set name
`coordinator_transport`). A cross-repo `sys.path` import into
`REE_Working/scripts/` was rejected for the same reason root CLAUDE.md (Session
Startup step 7a) rejected it for `graceful_timeout.py`: it works on the Mac and
fails on a box laid out differently, and it fails SILENTLY. Here the silent
fallback would be the git path -- i.e. precisely the 4.4%-routed defect this
module exists to end, except now invisible because the flag would still read
armed. A defect that hides itself is worse than one that is merely present.

The usual objection to vendoring -- "it duplicates state" -- does not apply, and
that is the load-bearing fact. `coordinator_transport` keeps NO repo-relative
state: its config and bearer token live in `~/.ree_coordinator_client.json`, in
`$HOME`, deliberately outside any repo (see that module's CONFIG_FILE comment).
Two copies therefore read ONE config, ONE token, ONE set of flags. What is
duplicated is CODE, and code drift is exactly what `audit_vendored_copies.py`
detects -- with a direction rule (canonical wins; a change that lives in a copy
goes into the canonical FIRST, then re-vendors).

Residual, stated rather than papered over: the audit is detection-only and runs
at session start / session land, so a window exists in which this copy can lag
the canonical. That window is bounded by the audit cadence, and a lagging copy
degrades toward MORE gating, never less -- a verb this copy has not yet vendored
is simply unavailable, which falls back to the git path DP-2 blesses.

DP-10 IS SATISFIED BY CONSTRUCTION, NOT BY CONVENTION
------------------------------------------------------
DP-10 requires every client branch to sit behind
`enabled() and in_scope(<operating root>)`, with fixtures unroutable BY
CONSTRUCTION. The 2026-08-28 incident is the reason: a plain test run on a
suppression-armed box leaked 21 fixture chips into the production DB, because
fixtures redirect the FILE, not the transport.

A second copy of the client in a second repo doubles that surface, so the gate
here is not optional and must not be inlined by callers. Two facts make it hold:

1. `transport.enabled()` already covers mode/url/token plus `scope_ok()` (the
   REE_WORKING_ROOT env-var form of re-rooting).
2. `in_scope()` additionally needs the OPERATING ROOT -- and for a REE_assembly
   script the honest answer to "which REE_Working tree am I part of?" is the
   umbrella directory that CONTAINS this checkout, which is exactly
   `UMBRELLA_ROOT` below: `<this file>/../..`.

   That is not a bypass of the gate, it is the faithful input to it. It also
   preserves the isolation property unchanged and needs NO widening of the
   canonical `in_scope()`: a fixture clone of this repo at, say,
   `/var/folders/xyz/REE_assembly/scripts/` computes `UMBRELLA_ROOT =
   /var/folders/xyz`, which does not equal the config's `scope_root`
   (`/Users/dgolden/REE_Working`) and shares no git-common-dir with it, so the
   transport stays OFF for it. Only a REE_assembly checkout sitting in the real
   umbrella tree arms.

   Widening `in_scope()` itself to accept any path CONTAINED in `scope_root` was
   considered and NOT done: containment is strictly broader than the identity
   check the gate is built on, and widening the arming condition is the one
   change DP-10 exists to prevent.

ASCII-only in every printed string (root CLAUDE.md).
"""

import os
import sys
from pathlib import Path

# Intra-repo import, the same idiom ~20 other REE_assembly/scripts/ modules use.
# Never a cross-repo path -- see the module docstring.
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

try:
    import coordinator_transport as transport  # noqa: E402
except Exception as exc:  # noqa: BLE001 -- see IMPORT_ERROR below
    transport = None
    IMPORT_ERROR = "%s: %s" % (type(exc).__name__, exc)
else:
    IMPORT_ERROR = None

# The repo root this script operates on: <umbrella>/REE_assembly/scripts/x.py
# -> parents[1] is <umbrella>. Computed from __file__, never from cwd (sessions
# run from worktrees) and never from a hardcoded path (that is what makes the
# fixture case above resolve correctly).
REPO_ROOT = _HERE.parent
UMBRELLA_ROOT = _HERE.parents[1]

# Routed paths a REE_assembly writer can touch, repo-relative, mapped to the
# per-file suppress predicate on the transport. Source of truth for the rows
# themselves: phase4_commit_intake_design.md section 5. One entry per FILE even
# where one flag covers a pair (the workset .v1.json/.md), because callers name
# files, not flags.
ROUTED_PATHS = {
    "evidence/planning/experiment_proposals.v1.json":
        "suppress_igw_proposals_git_write",
    "evidence/planning/inter_governance_workset.v1.json":
        "suppress_igw_workset_git_write",
    "evidence/planning/inter_governance_workset.md":
        "suppress_igw_workset_git_write",
    "evidence/planning/igw_routine_ledger.json":
        "suppress_igw_ledger_git_write",
    "evidence/planning/igw_assignments.json":
        "suppress_igw_assignments_git_write",
    "evidence/planning/igw_routine_log.md":
        "suppress_igw_log_git_write",
}


def available() -> bool:
    """True when the vendored transport imported at all. False is LOUD, not
    silent: callers get `describe()` text naming the import error, and the
    git path is taken. See the docstring on why a silent fallback is the
    failure mode this module was built to avoid."""
    return transport is not None


def routing_armed() -> bool:
    """The DP-10 gate, and the ONLY place it should be spelled out.

    `enabled()` covers mode/url/token/scope_ok(); `in_scope(UMBRELLA_ROOT)`
    covers in-process re-rooting and fixture clones outside the real tree.
    Callers MUST NOT re-implement either half."""
    if transport is None:
        return False
    return bool(transport.enabled() and transport.in_scope(UMBRELLA_ROOT))


def suppress_git_write(path) -> bool:
    """Is the git write for this routed repo-relative path suppressed on this
    box? False for an unknown path, an unarmed transport, or an unset flag --
    i.e. the caller keeps writing git, which is the DP-2 degrade route."""
    if not routing_armed():
        return False
    name = ROUTED_PATHS.get(str(path))
    if name is None:
        return False
    predicate = getattr(transport, name, None)
    if predicate is None:
        # A path this copy knows but this (older) vendored transport does not.
        # Degrade toward MORE gating: no suppression, keep the git write.
        return False
    try:
        return bool(predicate())
    except Exception:  # noqa: BLE001 -- same fail-open-to-git contract
        return False


def submit_replace(path, base_sha, content, message, session_id=None,
                   shadow=None, allow_shrink=False):
    """Submit one whole-file CAS intent for a routed REE_assembly path.

    Returns None -- meaning "no verdict, carry on with git" -- whenever the
    transport is unavailable, unarmed, or the path is not routed, matching
    coordinator_transport's contract exactly. `base_sha` must be the ORIGIN
    commit `content` was edited from (DP-1), never a working-tree read."""
    if not routing_armed():
        return None
    if str(path) not in ROUTED_PATHS:
        return None
    return transport.submit_intent_replace(
        "REE_assembly", str(path), base_sha, content, message,
        session_id=session_id, shadow=shadow, allow_shrink=allow_shrink)


def describe() -> str:
    """One ASCII line for a --why style report. Never raises."""
    if transport is None:
        return ("assembly coordinator UNAVAILABLE: vendored "
                "coordinator_transport did not import (%s) -- using git"
                % IMPORT_ERROR)
    base = transport.describe()
    if not transport.enabled():
        return "assembly coordinator OFF -- %s" % base
    if not transport.in_scope(UMBRELLA_ROOT):
        return ("assembly coordinator OFF (scope: operating root %s is not "
                "this config's scope_root -- fixture or re-rooted checkout, "
                "using git)" % UMBRELLA_ROOT)
    return "assembly coordinator ON (root %s) -- %s" % (UMBRELLA_ROOT, base)


if __name__ == "__main__":
    # Deliberately the only CLI surface: this is a library. Mirrors
    # coordinator_transport's own `python3 coordinator_transport.py`.
    print(describe())
    if available() and routing_armed():
        for p in sorted(ROUTED_PATHS):
            print("  %-52s suppress_git_write=%s" % (p, suppress_git_write(p)))
    sys.exit(0)
