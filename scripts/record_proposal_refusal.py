#!/usr/bin/env python3
"""Write a /queue-experiment substrate-readiness REFUSAL back to the proposal.

WHY THIS EXISTS
---------------
`/queue-experiment` Step 2.5 can establish, against the live substrate, that a
proposal is not buildable. That finding is expensive -- it is usually a runtime
probe -- and until now it had nowhere sanctioned to go. A session scoped out of
`evidence/planning/experiment_proposals.v1.json` by its launch constraints could
only raise a governance flag by hand, so the proposal stayed `status: proposed`
with no `blocked_by`, and `audit_blocked_proposal_unblockers.py` -- which reads
only proposals that are in a blocked status AND carry `blocked_by` -- was
STRUCTURALLY BLIND to it.

That is not hypothetical. GFLAG-0425 (2026-09-19, REE_assembly b501e436b16)
records exactly this for SD-106 / MECH-567: the M1_FALSIFY route is not
buildable (`oracle_action` has zero references in `ree_core/`), the flag says so
verbatim, and EXP-0255 is still `proposed` today with no `blocked_by` at all.
The detector could not see the one shape it exists to find.

WHAT THIS GUARANTEES
--------------------
1. **The refusal lands in the two fields the audit reads.** A blocked status and
   a NON-EMPTY `blocked_by`. `--blocked-by` is mandatory and an empty list is
   refused: an unattributed block is the second half of the same blind spot --
   measured 2026-09-23, 146 proposals sit in a blocked status with an empty
   `blocked_by`, against 77 the audit reports at all.
2. **Provenance travels with it.** `refused_by_session`, `refused_utc`,
   `refusal_route` and an optional `governance_flag`, so a later reader can tell
   a probe-backed refusal from a drive-by status change.
3. **It is a NARROW STRUCTURAL EDIT.** One proposal object is located by id and
   mutated in place; every other item is written back byte-identical, and the
   script verifies that before writing. It never regenerates the file.
4. **It respects the claim plane.** `scripts/task_claim.py check` runs first and
   the write is refused if another session owns the registry -- which is exactly
   what should happen while a `/governance` cycle holds it.

Usage:
  python3 scripts/record_proposal_refusal.py --proposal EXP-0255 \\
      --blocked-by MECH-567 --route implement_substrate \\
      --session igw-240-proposal-for-mech-567 \\
      --note "oracle_action has zero references in ree_core/ ..." \\
      --governance-flag GFLAG-0425
  ... --dry-run     print the diff and write nothing
  ... --no-commit   write the file, leave the commit to the caller
  ... --no-push     commit without pushing (an unpushed refusal is invisible
                    to the audit everyone else runs, so push is the default)
Exit codes: 0 written, 2 bad input, 3 another session owns the registry,
4 proposal not found.
"""
from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PY = "/opt/local/bin/python3"
ROOT = Path(__file__).resolve().parent.parent          # REE_assembly
UMBRELLA = ROOT.parent                                 # REE_Working
PROPOSALS_REL = "evidence/planning/experiment_proposals.v1.json"

# The statuses audit_blocked_proposal_unblockers.BLOCKED_STATUSES recognises.
# Writing anything outside this set puts the refusal back out of the audit's
# sight, which is the whole defect, so the choice is constrained here.
BLOCKED_STATUSES = (
    "blocked_substrate",
    "proposed_blocked_substrate",
    "deferred_substrate_not_ready",
    "blocked_on_gate",
    "gated",
)

# Where the refusal says the work goes next. Free prose would not group.
ROUTES = (
    "implement_substrate",   # a build is owed; /implement-substrate picks it up
    "governance",            # a disposition is owed; /governance picks it up
    "claim_synthesis",       # the claim needs reframing before any run
    "upstream_experiment",   # sequencing-gated on another run landing first
)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def claim_conflict(resources) -> str:
    """'' if nobody else owns these paths, else the arbitration verdict."""
    helper = UMBRELLA / "scripts" / "task_claim.py"
    if not helper.exists():
        return ""
    try:
        r = subprocess.run([PY, str(helper), "check", "--resources", *resources],
                           capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as exc:
        # Fail OPEN but LOUD: a broken claim helper must not wedge a refusal
        # write, but the caller has to be told the check did not happen. This
        # is a "could not compute", never a silent clean bill of health.
        return "CHECK-DID-NOT-RUN: %s" % exc
    return "" if r.returncode == 0 else (r.stdout or r.returncode).__str__()


def apply_refusal(doc: dict, proposal_id: str, blocked_by, note, route,
                  session, status, governance_flag=None, when=None) -> dict:
    """Mutate ONE item in place and return it. Raises KeyError if absent."""
    for item in doc.get("items", []):
        if isinstance(item, dict) and item.get("proposal_id") == proposal_id:
            item["status"] = status
            item["blocked_by"] = list(blocked_by)
            item["blocked_note"] = note
            item["refusal_route"] = route
            item["refused_by_session"] = session
            item["refused_utc"] = when or _now()
            if governance_flag:
                item["governance_flag"] = governance_flag
            return item
    raise KeyError(proposal_id)


def _other_items_unchanged(before: dict, after: dict, proposal_id: str) -> list:
    """Ids of any item OTHER than the target that moved. Must always be []."""
    b = {i.get("proposal_id"): i for i in before.get("items", [])
         if isinstance(i, dict)}
    a = {i.get("proposal_id"): i for i in after.get("items", [])
         if isinstance(i, dict)}
    moved = [pid for pid in set(b) | set(a)
             if pid != proposal_id and b.get(pid) != a.get(pid)]
    return sorted(str(p) for p in moved)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proposal", required=True)
    ap.add_argument("--blocked-by", action="append", default=[],
                    help="id of substrate this proposal waits on (repeatable; "
                         "at least one is MANDATORY)")
    ap.add_argument("--note", required=True, help="what the probe established")
    ap.add_argument("--route", required=True, choices=ROUTES)
    ap.add_argument("--session", required=True, help="refusing session slug")
    ap.add_argument("--status", default="blocked_substrate",
                    choices=BLOCKED_STATUSES)
    ap.add_argument("--governance-flag", default=None)
    ap.add_argument("--root", default=None, help="REE_assembly root (tests)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-commit", action="store_true")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--allow-self-block", action="store_true",
                    help="permit naming the proposal's own claim_id as its "
                         "blocker (see the refusal message for why not to)")
    ap.add_argument("--skip-claim-check", action="store_true",
                    help="tests only; never pass this against the live registry")
    args = ap.parse_args()

    blocked_by = [b.strip() for b in args.blocked_by if b and b.strip()]
    if not blocked_by:
        print("ERROR: --blocked-by is mandatory and must name at least one id.\n"
              "  A refusal with no named blocker is invisible to "
              "audit_blocked_proposal_unblockers.py, which is the exact blind\n"
              "  spot this script exists to close. Name the substrate, the "
              "claim, or the sd_id the proposal is waiting on.", file=sys.stderr)
        return 2
    if not args.note.strip():
        print("ERROR: --note must say what the probe established.",
              file=sys.stderr)
        return 2

    root = Path(args.root) if args.root else ROOT
    path = root / PROPOSALS_REL

    if not args.skip_claim_check and not args.dry_run:
        verdict = claim_conflict([PROPOSALS_REL])
        if verdict:
            print("REFUSING: another session owns %s\n\n%s"
                  % (PROPOSALS_REL, verdict), file=sys.stderr)
            print("Hand the refusal to that session, or wait for it to close.",
                  file=sys.stderr)
            return 3

    raw = path.read_text(encoding="utf-8")       # re-read immediately before write
    doc = json.loads(raw)
    before = copy.deepcopy(doc)
    try:
        item = apply_refusal(doc, args.proposal, blocked_by, args.note,
                             args.route, args.session, args.status,
                             args.governance_flag)
    except KeyError:
        print("ERROR: no proposal %s in %s" % (args.proposal, path),
              file=sys.stderr)
        return 4

    self_claim = str(item.get("claim_id") or "").strip()
    if self_claim and self_claim in blocked_by and not args.allow_self_block:
        print("ERROR: --blocked-by %s is this proposal's OWN claim_id.\n"
              "  audit_blocked_proposal_unblockers.py reads that as a "
              "self-block and can say nothing further about it: the id may be\n"
              "  a claims.yaml queue gate, a substrate_queue sd_id, or a "
              "coincidence, and no mechanical rule separates them. Name the\n"
              "  SUBSTRATE the proposal is waiting on -- the missing producer, "
              "the sd_id, the upstream claim -- not the claim under test.\n"
              "  --allow-self-block overrides if the claim genuinely is its "
              "own blocker." % self_claim, file=sys.stderr)
        return 2

    moved = _other_items_unchanged(before, doc, args.proposal)
    if moved:
        print("REFUSING: %d other proposal(s) would change: %s"
              % (len(moved), ", ".join(moved[:10])), file=sys.stderr)
        return 2

    print("%s -> status=%s blocked_by=%s route=%s"
          % (args.proposal, item["status"], ",".join(blocked_by), args.route))
    if args.dry_run:
        print("(dry run -- nothing written)")
        return 0

    path.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")
    print("wrote %s" % path)
    if args.no_commit:
        return 0

    cmd = [PY, str(UMBRELLA / "scripts" / "ree_commit.py"),
           "--repo", "REE_assembly", "-m",
           "proposal refusal: %s blocked on %s (%s, session %s)"
           % (args.proposal, ", ".join(blocked_by), args.route, args.session)]
    if not args.no_push:
        cmd.append("--push")
    cmd += ["--", PROPOSALS_REL]
    return subprocess.run(cmd, cwd=str(UMBRELLA)).returncode


if __name__ == "__main__":
    sys.exit(main())
