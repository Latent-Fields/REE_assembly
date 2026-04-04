#!/usr/bin/env bash
# REE Experiment Runner -- container entrypoint
#
# Environment variables (set via docker-compose or -e flags):
#   REE_GITHUB_USER    GitHub username whose repos to clone  (default: dgolden)
#   AUTO_START_RUNNER  Set to "true" to start V3 runner automatically without
#                      needing to click Start in the Explorer UI.  (default: false)
#
# SSH key:
#   Mount your SSH key at container startup:
#     -v ~/.ssh:/root/.ssh:ro
#   The key must have read/write access to the REE repos on GitHub.

set -euo pipefail

GITHUB_USER="${REE_GITHUB_USER:-dgolden}"
AUTO_START="${AUTO_START_RUNNER:-false}"
WORKSPACE="/workspace"
# Stable name used for machine attribution in contribution tracking.
# Set REE_MACHINE_NAME in docker-compose.yml to a short identifier for this machine
# (e.g. "alice-rtx4090"). Defaults to "docker-contributor" if not set.
MACHINE_NAME="${REE_MACHINE_NAME:-docker-contributor}"

echo "[ree-entrypoint] Starting REE container (github user: ${GITHUB_USER}, machine: ${MACHINE_NAME})"

# ── SSH setup ─────────────────────────────────────────────────────────────────
if [ -d /root/.ssh ]; then
    # The bind mount is read-only (and Windows perms are too open for SSH).
    # Copy to a writable location and set correct permissions there.
    mkdir -p /tmp/ssh-rw
    cp /root/.ssh/* /tmp/ssh-rw/ 2>/dev/null || true
    chmod 700 /tmp/ssh-rw
    find /tmp/ssh-rw -maxdepth 1 -type f -exec chmod 600 {} \;

    # Trust GitHub host key
    ssh-keyscan -H github.com >> /tmp/ssh-rw/known_hosts 2>/dev/null || true

    # Write an SSH config so git picks up keys from the writable copy
    cat > /tmp/ssh-config << 'SSHEOF'
Host github.com
    IdentityFile /tmp/ssh-rw/id_ed25519
    IdentityFile /tmp/ssh-rw/id_rsa
    UserKnownHostsFile /tmp/ssh-rw/known_hosts
    StrictHostKeyChecking no
SSHEOF
    export GIT_SSH_COMMAND="ssh -F /tmp/ssh-config"
    echo "[ree-entrypoint] SSH configured"
else
    echo "[ree-entrypoint] WARNING: no SSH key mounted -- git push will fail"
    echo "[ree-entrypoint] Mount your key with: -v ~/.ssh:/root/.ssh:ro"
fi

# Configure git identity (required for commits by auto-sync)
git config --global user.email "ree-runner@container" || true
git config --global user.name  "REE Runner"           || true

# ── Clone / update repos ──────────────────────────────────────────────────────
REPOS=(
    "REE_assembly"
    "ree-v3"
    "ree-v2"
    "ree-v1-minimal"
    "REE_convergence"
)

mkdir -p "${WORKSPACE}"
cd "${WORKSPACE}"

for repo in "${REPOS[@]}"; do
    url="git@github.com:${GITHUB_USER}/${repo}.git"
    if [ -d "${WORKSPACE}/${repo}/.git" ]; then
        echo "[ree-entrypoint] Pulling ${repo} ..."
        git -C "${WORKSPACE}/${repo}" pull --ff-only 2>&1 | tail -1
    else
        echo "[ree-entrypoint] Cloning ${repo} ..."
        git clone "${url}" "${WORKSPACE}/${repo}" 2>&1 | tail -2
    fi
done

echo "[ree-entrypoint] Repos ready"

# ── Auto-start runner (optional) ─────────────────────────────────────────────
SERVE_DIR="${WORKSPACE}/REE_assembly"
RUNNER_SCRIPT="${WORKSPACE}/ree-v3/experiment_runner.py"

if [ "${AUTO_START}" = "true" ]; then
    echo "[ree-entrypoint] AUTO_START_RUNNER=true -- launching V3 runner ..."
    # Start runner in background; serve.py will detect the PID file
    nohup python3 "${RUNNER_SCRIPT}" \
        --status-file "${SERVE_DIR}/evidence/experiments/runner_status/${MACHINE_NAME}.json" \
        --machine "${MACHINE_NAME}" \
        --auto-sync \
        --loop \
        > "${SERVE_DIR}/runner.log" 2>&1 &
    echo $! > "${WORKSPACE}/ree-v3/runner.pid"
    echo "[ree-entrypoint] Runner PID: $!"
fi

# ── Start serve.py ────────────────────────────────────────────────────────────
echo "[ree-entrypoint] Starting serve.py on port 8000 ..."
cd "${SERVE_DIR}"
exec python3 serve.py --port 8000
