---
title: Governance Verification Gate
parent: Governance
nav_order: 1
---

# Governance Verification Gate

## Why this gate exists

REE_assembly governance cycles involve multiple moving parts: experiment manifests on
multiple machines, coordinator-held runner heartbeats and status (the git-committed
heartbeat/status/command directories were retired 2026-09-06; the checks below read
coordinator `/shadow/status` and fall back to the now-empty git files only when it is
unreachable), a central runner status file that may lag behind, pending_review.md
generated from indexed manifests, and
roadmap snapshots that summarise the current state.

These pieces can disagree. Documented failure modes:

- **Stale pending_review.md**: new manifests land after the review file is generated,
  leaving experiments invisible to governance.
- **Roadmap/pending_review mismatch**: the roadmap snapshot and pending_review.md
  report different pending counts, typically because one was written after and the
  other before a governance walk.
- **Stale central runner_status.json**: after the Phase-2 coordinator cutover the
  per-machine status files carried live writes while the central file lagged; both are
  now a retired git mirror (2026-09-06) and this check is skipped whenever the
  coordinator answers. Downstream
  indexers that depend on the central file see stale counts.
- **EXQ drained without manifest**: an experiment drains from the queue and its
  outcome disappears from central indices, leaving its claim evidence status unknown.
- **Failed experiment without autopsy**: a FAIL result in pending_review.md is closed
  without a structured /failure-autopsy, making the failure evidence uninterpretable.
- **Heartbeat scope bleed**: the runner heartbeat git pull --rebase --autostash
  cycle can silently stash uncommitted governance edits, causing them to be lost or
  applied out of order.

This gate provides a deterministic, read-only check that surfaces these failure modes
before a governance cycle is closed.

---

## Scripts

### `scripts/verify_governance_cycle.py`

Runs all checks, writes a JSON report, and prints a terminal summary.

```bash
# From REE_assembly root:
python scripts/verify_governance_cycle.py

# Custom stale threshold:
python scripts/verify_governance_cycle.py --stale-hours 6

# Custom output path:
python scripts/verify_governance_cycle.py --output /tmp/verify.json

# Help:
python scripts/verify_governance_cycle.py --help
```

Exit codes:
- `0` -- pass (no block findings)
- `1` -- fail (one or more block findings)
- `2` -- usage error

### `scripts/generate_governance_handoff.py`

Reads the verification report and current state, writes a structured handoff.

```bash
# From REE_assembly root:
python scripts/generate_governance_handoff.py
```

Outputs:
- `evidence/handoffs/active_governance_handoff.json`
- `evidence/handoffs/active_governance_handoff.md`

Run after `verify_governance_cycle.py` so the handoff reflects the latest verification
status.

---

## Checks and severity

### Block vs Warn

A **block** finding means the governance cycle MUST NOT be marked complete until the
finding is resolved. Block findings exit with code 1.

A **warn** finding is a signal worth investigating but does not block cycle closure. It
may indicate genuine ambiguity (e.g. Phase-2 coordinator cutover means central status
intentionally lags) or a soft inconsistency.

An **info** finding is purely informational.

### Check A: `PENDING_REVIEW_STALE_AGAINST_MANIFESTS` (block)

Compares the Generated timestamp in pending_review.md against the newest manifest.json
mtime in evidence/experiments/. If a newer manifest exists, pending_review.md does not
reflect the latest experiment results.

**Resolution**: Run `python scripts/generate_pending_review.py`, then re-run the verifier.

### Check B: `ROADMAP_PENDING_REVIEW_MISMATCH` (block)

Extracts the pending_review count from the most recent Status Snapshot in docs/roadmap.md
and compares it to the Pending count in pending_review.md. A mismatch means the roadmap
and review list describe different states.

**Resolution**: Re-generate pending_review.md, update the roadmap snapshot to match, or
add an explicit note that the snapshot is intentionally stale (and why).

### Check C: `CENTRAL_RUNNER_STATUS_STALE` / `CENTRAL_RUNNER_STATUS_ABSENT` (warn)

Checks whether evidence/experiments/runner_status.json is present and recent. The
default stale threshold is 12 hours. This is a warn (not block) because, after the
Phase-2 coordinator cutover the coordinator (`GET /shadow/status`) is authoritative and
this whole check is skipped when it answers; the per-machine git status files are a
retired (2026-09-06) fallback, not a current source.

**Resolution**: Investigate whether the coordinator->central-index merge has wedged. If
Phase-2 is intentionally active, document that in the roadmap snapshot and the finding
is acceptable.

### Check D: `HEARTBEAT_STATUS_DIVERGENCE` (warn)

Compares each machine's live coordinator row (or, when the coordinator is unreachable,
its git heartbeat file -- a retired 2026-09-06 fallback) against its per-machine
runner_status.json (idle, current). If the heartbeat says running but the status says
idle, the runner may have stopped mid-experiment. Heartbeats older than 4 hours are
skipped (machine may be offline).

**Resolution**: Check the runner process on the affected machine. If stopped, determine
whether the experiment needs to be re-queued.

### Check E: `EXQ_DRAINED_WITHOUT_MANIFEST_OR_DISPOSITION` (block)

Searches the most recent Status Snapshot for explicit mentions of an EXQ being drained
or force_rerequed without a manifest. If a matching manifest is not found in
evidence/experiments/, the experiment's outcome is opaque.

**Resolution**: Check per-machine runner_status files and the coordinator panel.
- If the manifest is on a remote machine: wait for sync.
- If the run was pruned or never ran: add an explicit disposition note to the roadmap.
- If a re-run is needed: re-queue with a new letter suffix.

### Check F: `FAILED_EXPERIMENT_WITHOUT_DIAGNOSIS_LINK` (warn)

For each run ID in the FAIL section of pending_review.md, searches for a corresponding
failure_autopsy file in evidence/planning/. If none is found, the failure is
undiagnosed.

This is a warn (not block) in the first version. If a governance cycle is explicitly
being closed and the failure has no autopsy, it should become block.

**Resolution**: Run /failure-autopsy for the experiment, or add a non_contributory
rationale with an explicit reason to its manifest.

### Check G: `HEARTBEAT_SCOPE_BLEED` (warn)

If the working tree is dirty, checks whether any dirty file appears in both a telemetry
path (runner_heartbeats/, runner_status/) and a protected governance path
(docs/claims/claims.yaml, evidence/planning/). This catches cases where the runner
heartbeat rebase cycle has touched governance state.

**Resolution**: Run `git diff -- <path>` to inspect the change. Revert any
telemetry-driven change to protected files and re-apply the governance edit manually.

---

## Governance cycle integration

The gate is designed to run at two points in the governance workflow:

1. **Before walking pending experiments**: ensures pending_review.md is current.
2. **Before closing a cycle**: ensures no block findings remain.

### Wiring into `governance.sh`

To wire the gate into the end of the governance pipeline:

```bash
# Add to governance.sh after the final step:
echo "--- Step N: Governance verification gate ---"
if ! "$PYTHON" scripts/verify_governance_cycle.py; then
  echo "ERROR: Governance verification gate FAILED. Resolve block findings before closing." >&2
  exit 1
fi
```

### Running manually (recommended for now)

Until the gate is wired into `governance.sh`, run it manually:

```bash
cd /path/to/REE_assembly
python scripts/verify_governance_cycle.py
python scripts/generate_governance_handoff.py
```

Review `evidence/verification/governance_verification_latest.json` and
`evidence/handoffs/active_governance_handoff.md`.

---

## Overriding a block finding

The correct way to override a block finding is to resolve the underlying inconsistency
with an explicit documented disposition, not to weaken the check.

Examples:

- **PENDING_REVIEW_STALE_AGAINST_MANIFESTS**: Re-run generate_pending_review.py. If a
  manifest is deliberately excluded (e.g. a telemetry-only file), document why in the
  manifest or pending_review generation script.
- **ROADMAP_PENDING_REVIEW_MISMATCH**: Add a sentence to the roadmap snapshot explaining
  that the count difference reflects a governance cycle that is currently in progress.
- **EXQ_DRAINED_WITHOUT_MANIFEST_OR_DISPOSITION**: Add a line to the roadmap snapshot:
  "V3-EXQ-XXX: pruned from queue without run (reason: ...)" or "awaiting sync from
  machine Y". This explicit disposition allows the check to pass on the next run
  after the roadmap snapshot is updated.

Do not silence a block by editing the verifier unless the check is demonstrably
producing false positives (e.g. mtime comparison is unreliable in a specific environment).
If you must silence, document the reason with a comment and open a work item to revisit.

---

## Relation to failure autopsy and inter-governance handoff

- **Failure autopsy** (`/failure-autopsy` skill, `evidence/planning/failure_autopsy_*.{md,json}`):
  the structured post-mortem for a specific FAIL or ERROR experiment. The verification
  gate checks that one exists for each pending FAIL; it does not replace the autopsy.

- **Inter-governance workset** (`evidence/planning/inter_governance_workset.v1.json`,
  generated by `scripts/generate_inter_governance_workset.py`): the cross-cycle tracking
  of in-flight experiments and plan items. The handoff generator reads its summary for
  the workset section.

- **Active governance handoff** (`evidence/handoffs/active_governance_handoff.{json,md}`):
  the machine-readable state packet generated by this system. It summarises verification
  status, pending items, in-flight experiments, and a single concrete next action.
  Intended to be read at the start of each governance session as a resumption primitive.

---

## Report schema

```json
{
  "generated_at_utc": "ISO-8601 string",
  "repo_root": "/absolute/path/to/REE_assembly",
  "git_head": "40-char SHA or null",
  "status": "pass | fail",
  "findings": [
    {
      "severity": "block | warn | info",
      "code": "CHECK_CODE_STRING",
      "message": "Human-readable description",
      "evidence_paths": ["list of relevant file paths"],
      "suggested_next_action": "Concrete action to resolve"
    }
  ],
  "summary": {
    "block_count": 0,
    "warn_count": 0,
    "info_count": 0
  }
}
```
