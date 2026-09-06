#!/usr/bin/env bash
#
# land_governance.sh -- commit + push the working-tree edits a /governance cycle
# produced, for both REE_assembly and the REE_Working umbrella.
#
# Why this exists: when /governance runs inside Cowork, the Mac folder is mounted
# in a way that blocks unlink/rename inside .git, so `git add/commit/push` cannot
# run from the sandbox and a stale .git/index.lock is sometimes left behind. The
# working-tree edits themselves DO land on disk (same folder the Mac sees), so all
# that remains is to commit + push -- which must happen on the Mac. Run this script
# there after a Cowork governance session.
#
# It is also safe to run on a normal Mac-side /governance cycle: it is idempotent
# (a no-op when nothing is staged) and never touches sync_daemon-owned telemetry.
#
# Usage (on the Mac):
#   bash REE_assembly/scripts/land_governance.sh "governance 2026-06-08: <summary>"
#   REE_WORKING=/custom/path bash .../land_governance.sh "msg"   # non-default root
#
# What it does:
#   0. Clears a stale .git/index.lock in each repo (only if no git process holds it).
#   1. REE_assembly: stages everything EXCEPT runner_heartbeats/ and runner_status/
#      (retired 2026-09-06 -- deleted from master, no writer repopulates them; excluded
#      so a stray local copy is never re-added),
#      commits, runs the dropped-file post-commit check, then pushes master
#      (auto-rebasing once if the push is rejected non-fast-forward).
#   2. REE_Working umbrella: stages only TASK_CLAIMS.json + WORKSPACE_STATE.md,
#      commits, pushes master.
#
# It deliberately does NOT touch ree-v3 (experiment_queue.json + scripts are owned
# by the queue/runner path) or claims.yaml beyond whatever governance already wrote.
#
set -uo pipefail

BASE="${REE_WORKING:-$HOME/REE_Working}"
ASM="$BASE/REE_assembly"
MSG_ASM="${1:-governance closeout (landed via land_governance.sh)}"
MSG_UMB="${2:-governance closeout: TASK_CLAIMS + WORKSPACE_STATE}"

die() { echo "ERROR: $*" >&2; exit 1; }
[ -d "$ASM/.git" ] || die "REE_assembly git repo not found at $ASM (set REE_WORKING)"
[ -d "$BASE/.git" ] || die "REE_Working umbrella git repo not found at $BASE"

echo "=== land_governance: BASE=$BASE ==="

# --- Step 0: clear stale index.lock (only when no live git process owns it) ----
clear_stale_lock() {
  local repo="$1"
  local lock="$repo/.git/index.lock"
  [ -f "$lock" ] || return 0
  if pgrep -f "[g]it .*$repo" >/dev/null 2>&1; then
    die "a git process appears active in $repo; refusing to remove $lock"
  fi
  echo "Removing stale lock: $lock"
  rm -f "$lock" || die "could not remove $lock (remove it manually and retry)"
}
clear_stale_lock "$ASM"
clear_stale_lock "$BASE"

push_with_rebase() {
  # Push the current branch to the named remote ref; if rejected non-ff, rebase
  # the operator's just-made commit onto refreshed origin once and retry.
  local ref="$1"
  if git push origin "HEAD:$ref"; then return 0; fi
  echo "push rejected -- pulling --rebase --autostash and retrying once..."
  git pull --rebase --autostash origin "$ref" || die "rebase onto origin/$ref failed; resolve manually"
  git push origin "HEAD:$ref" || die "push to origin/$ref still failing; resolve manually"
}

# --- Step 1: REE_assembly governance regen -------------------------------------
cd "$ASM" || die "cannot cd $ASM"
git symbolic-ref -q HEAD >/dev/null || die "REE_assembly is in a detached HEAD"
git checkout master >/dev/null 2>&1 || die "could not checkout master in REE_assembly"

git add -A
# Never commit the retired telemetry dirs (2026-09-06): a stray local copy must not be re-added.
git reset -q -- evidence/experiments/runner_heartbeats \
                evidence/experiments/runner_status 2>/dev/null || true

if git diff --cached --quiet; then
  echo "REE_assembly: nothing staged (already landed?)."
else
  N=$(git diff --cached --name-only | wc -l | tr -d ' ')
  echo "REE_assembly: committing $N staged file(s)."
  git commit -m "$MSG_ASM" || die "REE_assembly commit failed"
  echo "--- dropped-file post-commit check (git show --stat HEAD, tail) ---"
  git show --stat HEAD | tail -6
  push_with_rebase master
  echo "REE_assembly: pushed -> origin/master ($(git rev-parse --short HEAD))."
fi

# --- Step 2: REE_Working umbrella coordination files ---------------------------
cd "$BASE" || die "cannot cd $BASE"
git checkout master >/dev/null 2>&1 || die "could not checkout master in REE_Working"
git add TASK_CLAIMS.json WORKSPACE_STATE.md
if git diff --cached --quiet; then
  echo "REE_Working: nothing staged."
else
  git commit -m "$MSG_UMB" || die "REE_Working commit failed"
  push_with_rebase master
  echo "REE_Working: pushed -> origin/master ($(git rev-parse --short HEAD))."
fi

echo "=== land_governance: done. ==="
echo "Reminder: flip the governance claim in TASK_CLAIMS.json to status \"done\""
echo "(it was kept active to protect uncommitted evidence/ edits from the heartbeat autostash)."
