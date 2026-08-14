#!/usr/bin/env bash
# precommit_literature.sh -- run scripts/validate_literature.py when staged
# changes touch REE_assembly/evidence/literature/**.
#
# Called from the PreToolUse hook in REE_Working/.claude/settings.json on any
# `git commit` bash invocation. Self-gates: if no evidence/literature/ paths are
# staged, this exits 0 with no output, so commits to ree-v3 / other repos and to
# unrelated REE_assembly paths are not penalised. Same shape as
# ree-v3/scripts/precommit_contracts.sh.
#
# WHY IT EXISTS
# -------------
# Nothing had ever read the literature_evidence/v1 schema. The `source` object
# was violated by 605 of 2189 records for six months before anyone looked,
# because no validator existed and build_experiment_indexes._scan_literature
# never touches that object. A schema nothing reads documents convention; it
# does not hold a line. This script is what reads it, on the commit path.
#
# BLOCKING BY DEFAULT SINCE 2026-08-14 -- AND THE CONDITION FOR THAT IS RECORDED
# -----------------------------------------------------------------------------
# This shipped REPORT-ONLY, deliberately: the corpus then had a 17-finding
# baseline (17 of 2189 at REE_assembly 0bfbedccfd) being worked by sibling
# cleanup chips, and a gate that fires on every commit gets disabled, which is
# strictly worse than no gate. The stated flip condition was "once the corpus
# baseline is at zero".
#
# It is now zero, and both checks agree:
#     validate_literature.py     OK (2189 records checked, 0 findings)
#     audit_literature_schema.py 2189 records, 0 failing against HEAD schema
# reached by e8dcda8644 (the last missing summary.md) on top of 590842afa0 (the
# residual 16 source-object drifts). So the default flips, per its own rule.
#
# What the flip costs is much less than it looks: the validator is scoped to the
# records the COMMIT TOUCHES (--paths), not the whole corpus, so even a future
# backlog cannot wedge an unrelated commit. What blocks is a commit that touches
# a record which is itself bad -- which is the entire point.
#
# IF THIS EVER STARTS FIRING ON ORDINARY WORK, the fix is NOT to soften it in
# place. Either the corpus has regressed (fix the records) or the schema has
# drifted from real convention (run `audit_literature_schema.py --drift` and
# decide direction from the whole-corpus enumeration, which is what that flag is
# for). Turn it off with REE_LITERATURE_GATE_BLOCK=0 only as a temporary escape
# hatch, and say in the commit why.
#
# Exit codes:
#   0 -- nothing staged under evidence/literature/, or clean, or report-only
#   2 -- findings AND blocking enabled (blocks the commit; same code as
#        validate_queue.py)
#   3 -- internal error (repo or validator missing)
#
# Usage:
#   bash REE_assembly/scripts/precommit_literature.sh [--block|--report-only]

set -u

BLOCK="${REE_LITERATURE_GATE_BLOCK:-1}"
case "${1:-}" in
    --block)       BLOCK=1 ;;
    --report-only) BLOCK=0 ;;
esac

# Resolve the REE_assembly repo root, worktree-aware. `git rev-parse` first --
# git invokes hooks with the working tree already correct for the commit in
# question, including a `git worktree add` checkout. Fall back to this script's
# own location, which is correct whenever the script is invoked by path.
REPO=""
if TOP="$(git rev-parse --show-toplevel 2>/dev/null)"; then
    if [ -d "$TOP/evidence/literature" ]; then
        REPO="$TOP"
    fi
fi
if [ -z "$REPO" ]; then
    SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
    CAND="$(dirname "$SELF_DIR")"
    if [ -d "$CAND/evidence/literature" ]; then
        REPO="$CAND"
    fi
fi
# Not an REE_assembly checkout -> nothing of ours is being committed. Exit 0:
# this hook fires on EVERY git commit in every repo.
[ -n "$REPO" ] || exit 0

VALIDATOR="$REPO/scripts/validate_literature.py"
if [ ! -f "$VALIDATOR" ]; then
    echo "precommit_literature: $VALIDATOR missing" >&2
    exit 3
fi

PY="${REE_PYTHON:-}"
if [ -z "$PY" ]; then
    for cand in /opt/local/bin/python3 python3; do
        if command -v "$cand" >/dev/null 2>&1; then PY="$cand"; break; fi
    done
fi
if [ -z "$PY" ]; then
    echo "precommit_literature: no python3 found" >&2
    exit 3
fi

# Staged literature paths. ACMR excludes deletions: a deleted record.json has no
# content to validate. A deleted summary.md is NOT excluded -- it is an R/M/A-
# adjacent change whose damage lands on a record that may not itself be staged,
# which is why validate_literature.py's --paths resolves any entry-directory path
# up to its enclosing record.json rather than taking record.json paths only.
STAGED="$(git -C "$REPO" diff --cached --name-only --diff-filter=ACMR \
            -- evidence/literature 2>/dev/null)"

# Also feed staged DELETIONS of non-record files, for the dangling-summary_path
# case above. A deleted record.json is dropped -- there is nothing left to check.
DELETED="$(git -C "$REPO" diff --cached --name-only --diff-filter=D \
            -- evidence/literature 2>/dev/null | grep -v '/record\.json$' || true)"

# Assert non-empty before doing anything with the list. Per CLAUDE.md "Shell
# Portability": a silently-empty path list handed to a tool that treats "no
# paths" as "operate on everything" turns a shell quirk into a full-corpus run.
# Here the validator treats an explicit empty --paths as a no-op, but exiting
# early is cheaper and states the intent.
ALL="$(printf '%s\n%s\n' "$STAGED" "$DELETED" | sed '/^$/d')"
[ -n "$ALL" ] || exit 0

# `while read` rather than mapfile/readarray -- bash-4 builtins are not
# guaranteed on the cloud boxes and fail SILENTLY there (CLAUDE.md).
set -- --repo "$REPO" --paths
while IFS= read -r line; do
    [ -n "$line" ] && set -- "$@" "$line"
done <<EOF
$ALL
EOF

OUT="$("$PY" "$VALIDATOR" "$@" 2>&1)"
RC=$?

if [ "$RC" -eq 3 ]; then
    echo "$OUT" >&2
    exit 3
fi

# `OK (...)` is the clean line; anything else is a finding worth surfacing.
case "$OUT" in
    *"validate_literature: OK"*) exit 0 ;;
esac

echo "$OUT"
if [ "$BLOCK" = "1" ]; then
    echo ""
    echo "precommit_literature: BLOCKING -- a record this commit touches is invalid."
    echo "  The corpus baseline was 0 findings of 2189 as of 2026-08-14, so this is"
    echo "  something this commit introduced or is carrying forward."
    echo "  Fix the record, or set REE_LITERATURE_GATE_BLOCK=0 for a temporary"
    echo "  escape hatch (and say why in the commit message)."
    exit 2
fi
echo ""
echo "precommit_literature: report-only (REE_LITERATURE_GATE_BLOCK=0), commit NOT blocked."
exit 0
