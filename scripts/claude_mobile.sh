#!/usr/bin/env bash
# claude_mobile.sh -- ensure a persistent Claude Code session on the Mac that an
# iPhone SSH client can attach to over WireGuard.
#
# It keeps a detached tmux session named "ree" alive in the REE_Working tree.
# Because tmux outlives your SSH connection, you can lock the phone / lose signal
# and re-attach to the SAME Claude Code session later.
#
# Typical use from the iPhone (after SSH is set up -- see docs/mobile_access.md):
#   ssh mac            # mac -> 10.8.0.11, user dgolden (host alias in your SSH app)
#   bash /Users/dgolden/REE_Working/REE_assembly/scripts/claude_mobile.sh
#   # ... you are now attached to tmux session "ree"; run `claude` inside it.
#
# Run with no TTY (e.g. over `ssh mac bash .../claude_mobile.sh` non-interactively)
# and it just ensures the session exists and reports -- it won't try to attach.
set -euo pipefail

SESSION="ree"
WORKDIR="/Users/dgolden/REE_Working"

if ! command -v tmux >/dev/null 2>&1; then
    echo "ERROR: tmux is not installed. Install it with:  brew install tmux" >&2
    exit 1
fi

# Create the session detached if it does not already exist. -A on new-session
# would attach-or-create, but we want create-if-absent without attaching here so
# the non-interactive path stays clean.
if tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "[claude_mobile] tmux session '$SESSION' already running."
else
    tmux new-session -d -s "$SESSION" -c "$WORKDIR"
    echo "[claude_mobile] created detached tmux session '$SESSION' in $WORKDIR."
    echo "[claude_mobile] tip: inside the session, run 'claude' to start Claude Code."
fi

# Attach only when we have an interactive terminal and are not already inside tmux.
if [ -t 1 ] && [ -z "${TMUX:-}" ]; then
    echo "[claude_mobile] attaching... (detach with Ctrl-b then d)"
    exec tmux attach-session -t "$SESSION"
else
    echo "[claude_mobile] not attaching (no TTY or already inside tmux)."
    echo "[claude_mobile] attach manually with:  tmux attach -t $SESSION"
fi
