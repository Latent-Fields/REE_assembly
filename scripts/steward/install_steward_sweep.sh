#!/bin/bash
# Install/refresh the Steward daily T0 auto-fix sweep launchd agent.
#
# MAC / DEV MACHINE ONLY. Do NOT install on the hub or the cloud workers -- they
# run the phase3 writers against continuously-moving checkouts, and a scheduled
# writer competing with those is exactly the contention the concurrency rules in
# CLAUDE.md exist to avoid. Same exclusion as the git commit guards.
#
# Idempotent: safe to re-run after editing the plist or the sweep. Re-running is
# in fact REQUIRED after editing the plist -- launchd caches the loaded copy, so
# an edit to the repo file changes nothing until bootout+bootstrap. (Same class
# of silent no-op as the .claude/settings.json drift that left 66 worktrees
# committing with their guards skipped.)
#
# RunAtLoad is true, so installing runs one sweep immediately. That is deliberate
# -- it is how you find out the install works -- and it is safe: the sweep is
# idempotent, refuses on a moving ref, refuses to write over another session's
# in-flight edit, and commits as the bot identity.

set -eu

BASE=/Users/dgolden/REE_Working
REPO_PLIST="$BASE/REE_assembly/scripts/steward/com.ree.steward.plist"
SWEEP="$BASE/REE_assembly/scripts/steward/steward_sweep.py"
LABEL=com.ree.steward
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

[ -f "$REPO_PLIST" ] || { echo "missing $REPO_PLIST" >&2; exit 1; }
[ -f "$SWEEP" ]      || { echo "missing $SWEEP" >&2; exit 1; }

# The sweep commits through ree_commit.py; without it every run would abort at
# the commit gate. Fail here rather than daily in a log nobody reads.
[ -f "$BASE/scripts/ree_commit.py" ] \
  || { echo "missing $BASE/scripts/ree_commit.py -- the sweep cannot commit" >&2; exit 1; }

# Prove the sweep runs before scheduling it. --dry-run applies nothing and
# commits nothing; it exercises the ref pin, the preview and the gates.
echo "--- dry run ---"
/opt/local/bin/python3 "$SWEEP" --dry-run || {
  echo "sweep --dry-run failed; NOT installing" >&2; exit 1; }

mkdir -p "$HOME/Library/LaunchAgents"
cp "$REPO_PLIST" "$DEST"

# bootout first so an edited plist actually takes effect; ignore "not loaded".
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$DEST"

echo "installed $LABEL"
launchctl print "gui/$(id -u)/$LABEL" 2>/dev/null \
  | grep -E "^\s+(state|pid|runs) " || true
echo "log:    $HOME/Library/Logs/ree_steward_sweep.launchd.log"
echo "ledger: $BASE/REE_assembly/scripts/steward/state/steward_ledger.jsonl  (source=steward_sweep)"
echo "stop:   launchctl bootout gui/\$(id -u)/$LABEL"
