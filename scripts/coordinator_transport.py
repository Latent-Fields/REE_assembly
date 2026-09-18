"""Coordinator transport for task_claim.py / chip_ledger.py -- PHASE-2, DEFAULT OFF.

WHAT THIS IS
------------
`TASK_CLAIMS.json` and `TASK_CHIPS.json` are shared, git-tracked whole-file
registries mutated by every session on every machine. Arbitration between those
sessions is, in root CLAUDE.md's own words, "best-effort, not a lock": two
sessions can each read the file clean, each see no rival, and each write. That
is the confirmed 2026-07-28 three-session collision on
`ree-v3/runner_remote_control.py` (three claims inside 84 seconds, two
implementations live in one working tree), and the 2026-08-09 chip
double-dispatch.

This module lets those two scripts put that one decision -- "do I own this?" --
on a real database transaction instead. The coordinator's `BEGIN IMMEDIATE`
takes the write lock BEFORE its guard SELECT, so the read-then-write window
closes across every machine at once.

Design: REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md
(section 5.2 for the schema/endpoints, 5.3 for the degrade path).

THE FLAG, AND WHY IT IS NOT `COORDINATION_MODE`
-----------------------------------------------
    TASK_CLAIM_COORDINATION_MODE = git (DEFAULT) | coordinator

`git` is today's behaviour, byte for byte: `enabled()` returns False, every
function here is a hard no-op, and neither calling script changes what it does
in any way. That is the non-negotiable property of this phase -- the actual
cutover is a separate, later, human go-live decision that additionally needs
the PHASE-1 soak evidence.

It deliberately does NOT reuse ree-v3's existing `COORDINATION_MODE`, even
though this module is otherwise modelled closely on `coordinator_client.py`.
`COORDINATION_MODE=coordinator` is ALREADY SET in production on every cloud
worker's runner service, for the EXPERIMENT plane. Reusing that name would flip
claim/chip transport on across the fleet the moment this code landed -- a
silent default flip, which is exactly what the phase forbids. One shared name
for two independent cutovers is a trap, not a convenience.

Connection settings, each falling back to the experiment-plane variable so a
box already configured for the coordinator needs only the mode flag:

    TASK_CLAIM_COORDINATOR_URL      <- COORDINATOR_URL      e.g. http://10.8.0.1:8787
    TASK_CLAIM_COORDINATOR_TOKEN    <- COORDINATOR_TOKEN    per-machine bearer token
    TASK_CLAIM_COORDINATOR_TIMEOUT  <- COORDINATOR_TIMEOUT  seconds, default 5

The timeout defaults LOWER than the experiment plane's 10s on purpose. A
heartbeat POST can afford to wait; a session opening a claim is a human sitting
in front of a terminal, and the fallback below is always available, so failing
fast to git costs correctness nothing and costs latency a lot less.

WHAT "COORDINATOR-FIRST" MEANS IN THIS PHASE -- read this before changing it
---------------------------------------------------------------------------
Under `coordinator`, the calling script does BOTH: it asks the coordinator
first, and then still performs its own git write. It does NOT stop writing git.

That is not a half-measure, it is the only correct arrangement available today,
and the reason is concrete: the DB->git materializer (the analogue of
sync_daemon's `phase3_*_writer` family, which is what makes the coordinator the
sole git writer for `experiment_queue.json`) DOES NOT EXIST for these two files.
Until it does, a claim that lived only in the DB would be invisible to
`audit_stale_claims.py`, `prune_task_claims_done.py`, `serve.py`'s `/workset`
panel, `audit_orphan_chips.py`, every `chip_ledger.py list`, and every session
on every other machine. So the git write stays, and what moves to the
coordinator is the ARBITRATION AUTHORITY -- the verdict, not the storage.

This mirrors ree-v3's own Phase 2 exactly ("SYNC_MODE=coordinator (claim
cutover): git remains the queue worklist/transport; the DB becomes the claim
authority"), which is the prior art this whole migration is copied from.

Suppressing the client git write is PHASE-2b and needs the materializer first.

THE FALLBACK IS THE POINT, NOT AN AFTERTHOUGHT
-----------------------------------------------
Every call here returns `None` -- meaning "no verdict, carry on with git" -- on
ANY failure: mode off, no URL, no token, DNS failure, connection refused, TLS
error, timeout, 5xx, unparseable body, or an unexpected exception of any kind.
The caller treats `None` as "the coordinator said nothing" and runs today's git
path unchanged.

This matters for a specific documented reason (plan doc section 6.2): the Mac's
WireGuard tunnel has a real flakiness history -- 8 flapping days in the last 30
as of PHASE-0 -- and today that does not matter for claims/chips because the Mac
talks to GitHub directly. Once the coordinator is consulted, the Mac's own
session productivity depends on that tunnel, so "coordinator unreachable" must
be a well-exercised path from day one rather than a rare edge case discovered
later. `test_coordinator_transport.py` exercises it against a real socket.

A 409 is NOT a failure. It is a legitimate verdict (a rival owns the resource,
a chip is already claimed) and is returned to the caller to act on. Only
transport and server errors degrade to git.

ASCII-only in every printed string (root CLAUDE.md).
"""

import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_TIMEOUT = 5.0

# The one verdict-bearing HTTP status that is not an error. See above.
VERDICT_STATUSES = (200, 400, 404, 409)

# Machine-local client config (PHASE-2 go-live switch). Env always wins;
# this file is the PER-MACHINE fallback so one file flips every caller on a
# box (interactive Claude sessions, launchd/systemd ticks, headless workers)
# at once, and removing/renaming it is the whole rollback. Deliberately in
# $HOME, not the repo: it must never travel through git, and worktrees must
# see the same machine state as the main checkout. Recognised keys:
#   {"mode": "coordinator", "url": "http://10.8.0.1:8787",
#    "token": "...", "timeout": 5.0, "suppress_git_write": true}
# Unreadable / malformed / absent file = no config (git path), same
# fail-open posture as a missing env var.
CONFIG_FILE_ENV = "TASK_CLAIM_COORDINATOR_CONFIG"
DEFAULT_CONFIG_FILE = "~/.ree_coordinator_client.json"

_config_cache = {"path": None, "mtime": None, "data": {}}


def _config_path():
    return os.path.expanduser(
        os.environ.get(CONFIG_FILE_ENV) or DEFAULT_CONFIG_FILE)


def _config():
    """The machine-local config dict, {} when absent/unreadable. Cached by
    (path, mtime) so repeated calls in one process stay cheap while a live
    edit (the go-live flip itself) is picked up without a restart."""
    path = _config_path()
    try:
        mtime = os.stat(path).st_mtime
    except OSError:
        return {}
    if (_config_cache["path"] == path
            and _config_cache["mtime"] == mtime):
        return _config_cache["data"]
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            data = {}
    except (OSError, ValueError):
        data = {}
    _config_cache.update(path=path, mtime=mtime, data=data)
    return data


def _env(name, fallback_name, default=""):
    val = os.environ.get(name)
    if val is None or val == "":
        val = os.environ.get(fallback_name, default)
    return val


def mode() -> str:
    """git (default) | coordinator. Env first, then the machine-local config
    file. Read on every call, not cached at import: the test suite and any
    caller that wants to scope the flag to one command can then set it with
    os.environ without reloading the module."""
    raw = os.environ.get("TASK_CLAIM_COORDINATION_MODE")
    if raw is not None and raw.strip():
        return raw.strip()
    cfg = str(_config().get("mode") or "").strip()
    return cfg or "git"


def url() -> str:
    env = _env("TASK_CLAIM_COORDINATOR_URL", "COORDINATOR_URL", "")
    if env:
        return env.rstrip("/")
    return str(_config().get("url") or "").rstrip("/")


def token() -> str:
    env = _env("TASK_CLAIM_COORDINATOR_TOKEN", "COORDINATOR_TOKEN", "")
    if env:
        return env
    return str(_config().get("token") or "")


def timeout() -> float:
    raw = _env("TASK_CLAIM_COORDINATOR_TIMEOUT", "COORDINATOR_TIMEOUT", "")
    if not raw:
        raw = _config().get("timeout")
    try:
        return float(raw) if raw else DEFAULT_TIMEOUT
    except (TypeError, ValueError):
        return DEFAULT_TIMEOUT


def suppress_git_write() -> bool:
    """PHASE-2b cutover predicate: may the CLIENT skip its own git
    write+commit+push after a SUCCESSFUL coordinator write? False unless the
    transport is fully enabled AND the flag is explicitly set (env
    TASK_CLAIM_SUPPRESS_GIT_WRITE=1 wins, else the config file's
    suppress_git_write). The caller must still take the git path whenever
    the coordinator call itself failed -- this predicate only says the
    MODE is armed, never that a particular call succeeded."""
    if not enabled():
        return False
    env = os.environ.get("TASK_CLAIM_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("suppress_git_write"))


def suppress_workspace_state_git_write() -> bool:
    """PHASE-4 cutover predicate for WORKSPACE_STATE.md appends -- a SEPARATE
    flag from suppress_git_write() on purpose, so the WS path gets its own
    dual-write soak and go-live flip independent of the registry cutover.
    While OFF (the default), an armed-transport client still POSTs the entry
    (declaring client_git_write=true) AND runs today's git append -- the hub
    materializer then only WATCHES for the entry and marks it materialized,
    never splicing it. Flipping this ON makes the materializer the one
    writer. Env WORKSPACE_STATE_SUPPRESS_GIT_WRITE wins, else the config
    file's workspace_state_suppress_git_write. Same caveat as
    suppress_git_write(): this only says the mode is armed, never that a
    particular call succeeded."""
    if not enabled():
        return False
    env = os.environ.get("WORKSPACE_STATE_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("workspace_state_suppress_git_write"))


def scope_ok() -> bool:
    """SCOPE GATE (2026-08-28, found live by the cutover canary's sibling
    failure): the config file is MACHINE-GLOBAL (~/.ree_coordinator_client.json)
    while the scripts it arms can be RE-ROOTED per-process via
    REE_WORKING_ROOT -- which is exactly what the scripts/ test corpus and any
    scratch-repo tooling do. Without this gate, a subprocess-driven test that
    opens a claim in a tempdir repo posts that claim to the PRODUCTION
    coordinator DB, and the hub materializer then renders test garbage into the
    real TASK_CLAIMS.json/TASK_CHIPS.json. Measured 2026-08-28: the first
    post-cutover corpus run failed test_ree_commit_self_repo_push_branch.py
    precisely because the transport armed itself inside the test's temp repo.

    Rule: a config carrying `scope_root` arms the transport ONLY for processes
    whose REE_WORKING_ROOT is unset (an ordinary production invocation on this
    box) or resolves to that same root. A re-rooted invocation is a test or a
    scratch run -- it falls back to the git path, which inside a temp repo is
    exactly the pre-cutover behaviour the tests pin. A config WITHOUT
    scope_root keeps the old (ungated) behaviour. A test that genuinely wants
    the transport can point REE_COORDINATOR_CLIENT_CONFIG at its own config
    file (no scope_root, URL at a fake server) instead of inheriting the
    machine's."""
    scope = str(_config().get("scope_root") or "")
    if not scope:
        return True
    env_root = os.environ.get("REE_WORKING_ROOT")
    if not env_root:
        return True
    try:
        return os.path.realpath(env_root) == os.path.realpath(scope)
    except OSError:
        return False


def _git_common_dir(path):
    """Absolute git-common-dir for the repo at `path`, or None if `path` is
    not inside a git working tree / git is unavailable.

    A worktree's `.git` is a file pointing INTO the main checkout's `.git/
    worktrees/<name>/`, but `git rev-parse --git-common-dir` resolves that
    indirection for both the main checkout and every worktree cut from it,
    returning the SAME path for all of them -- exactly the identity
    in_scope() needs below to tell "a worktree of this repo" apart from "an
    unrelated repo" (e.g. a test's throwaway tmp repo, whose common-dir
    points elsewhere entirely). Best-effort; never raises."""
    try:
        r = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--git-common-dir"],
            capture_output=True, text=True, timeout=10)
    except Exception:  # noqa: BLE001 -- this is a best-effort identity check
        return None
    if r.returncode != 0:
        return None
    out = r.stdout.strip()
    if not out:
        return None
    p = out if os.path.isabs(out) else os.path.join(str(path), out)
    try:
        return os.path.realpath(p)
    except OSError:
        return None


def in_scope(operating_root) -> bool:
    """Dynamic per-caller scope check: is `operating_root` (the repo root the
    CALLING script is actually operating on, e.g. task_claim.ROOT) the root
    this machine's config was written for?

    Complements scope_ok(), which reads the REE_WORKING_ROOT env var and so
    only sees subprocess-style re-rooting. The scripts/ test corpus ALSO
    re-roots IN-PROCESS by monkeypatching the caller's module-level ROOT with
    no env change -- only the caller can see that, so callers pass their live
    ROOT here on every coordinator_enabled() check. A config with no
    scope_root keeps the old (ungated) behaviour.

    WORKTREE-AWARE (2026-09-08, chip-20260906-wsappend-worktree-scope): the
    exact-realpath check alone rejects every worktree under
    <scope_root>/.claude/worktrees/<slug>/, even though a worktree session
    calling append_workspace_state_entry.py with `--root "$WT"` intends to
    append to the SAME coordinator-owned WORKSPACE_STATE.md the main
    checkout writes -- there is exactly one logical file, not one per
    worktree. That silent rejection sent the append down the git path
    instead, landing the entry on the worktree's own side branch where the
    hub materializer never sees it and where umbrella-repo landing can be
    wedged for a long time (observed 2026-09-06: entry only ever reached
    origin after a second run with `--root /Users/dgolden/REE_Working`).
    task_claim.py / chip_ledger.py do not hit this: both pin ROOT to the
    canonical path via REE_WORKING_ROOT (or the /Users/dgolden/REE_Working
    default) rather than a caller-supplied worktree path, so their `in_scope`
    calls always compare canonical-to-canonical. append_workspace_state_entry
    is the one caller that legitimately passes an arbitrary `--root`.

    Fix: when the exact match fails, fall back to a REPO-IDENTITY check via
    `git rev-parse --git-common-dir` (see _git_common_dir) -- every worktree
    of the same repo shares one common-dir with the main checkout, while an
    UNRELATED repo (a test's tmp repo) does not, so this does not weaken the
    test-corpus isolation scope_ok()/in_scope() exist for in the first
    place."""
    scope = str(_config().get("scope_root") or "")
    if not scope or operating_root is None:
        return True
    try:
        if os.path.realpath(str(operating_root)) == os.path.realpath(scope):
            return True
    except OSError:
        return False
    common_here = _git_common_dir(operating_root)
    common_scope = _git_common_dir(scope)
    return bool(common_here) and common_here == common_scope


def enabled() -> bool:
    """True only when the mode is explicitly `coordinator` AND both a URL and a
    token are configured AND the process is operating on the repo the config
    was written for (see scope_ok()).

    Missing config is treated as OFF rather than as an error, deliberately: a
    box that has the mode set but no token would otherwise fail every claim,
    and there is a perfectly good git path sitting right there. The warning in
    `describe()` is what makes the misconfiguration visible.
    """
    return (mode() == "coordinator" and bool(url()) and bool(token())
            and scope_ok())


def describe() -> str:
    """One ASCII line for a --why style report. Never raises."""
    m = mode()
    if m != "coordinator":
        return "coordinator transport OFF (TASK_CLAIM_COORDINATION_MODE=%s)" % m
    if not url():
        return ("coordinator transport MISCONFIGURED: mode=coordinator but no "
                "TASK_CLAIM_COORDINATOR_URL/COORDINATOR_URL -- using git")
    if not token():
        return ("coordinator transport MISCONFIGURED: mode=coordinator but no "
                "TASK_CLAIM_COORDINATOR_TOKEN/COORDINATOR_TOKEN -- using git")
    if not scope_ok():
        return ("coordinator transport OFF (scope: REE_WORKING_ROOT=%s is not "
                "this config's scope_root -- re-rooted process, using git)"
                % os.environ.get("REE_WORKING_ROOT", ""))
    return "coordinator transport ON (%s, timeout %.1fs)" % (url(), timeout())


class Verdict(object):
    """A verdict the coordinator actually returned.

    `status` is the HTTP code, `verdict` the string db.py produced, `payload`
    the whole body. `ok` is True only for a 200 whose verdict is not an error --
    a caller that just wants "may I proceed" reads that.
    """

    __slots__ = ("status", "verdict", "payload")

    def __init__(self, status, payload):
        self.status = status
        self.payload = payload or {}
        self.verdict = self.payload.get("verdict") or ""

    @property
    def ok(self) -> bool:
        return self.status == 200 and self.verdict not in ("error",)

    @property
    def refused(self) -> bool:
        """A legitimate refusal the caller must honour rather than retry."""
        return self.status == 409

    def get(self, key, default=None):
        return self.payload.get(key, default)

    def __repr__(self):
        return "Verdict(status=%d, verdict=%r)" % (self.status, self.verdict)


def _warn(msg: str) -> None:
    sys.stderr.write("coordinator-transport: %s\n" % msg)


def _verdict_suffix(payload):
    """One short clause naming the server's own verdict/error for a status the
    transport treats as degrade-to-git, so the fallback line is diagnosable
    from the client alone. WHY (2026-09-07): POST /intent/replace answered
    500 on every REE_assembly ledger write for five days; the line said only
    'returned HTTP 500' and nobody could tell repo_not_configured (a deploy
    gap, DP-11 pre-activation) from a crash without reading the hub's audit
    table. Never raises; empty when the body carries neither key."""
    if not isinstance(payload, dict):
        return ""
    bits = []
    for key in ("verdict", "error"):
        val = payload.get(key)
        if isinstance(val, str) and val.strip():
            bits.append("%s=%s" % (key, val.strip()[:80]))
    return (" (" + ", ".join(bits) + ")") if bits else ""


def post(path: str, body: dict, warn: bool = True):
    """POST one intent. Returns a Verdict, or None meaning "fall back to git".

    NEVER raises. That is a contract, not an aspiration: this sits in front of
    the only mechanism a session has for declaring what it is working on, and a
    transport bug here must degrade to today's behaviour rather than stop the
    fleet claiming anything.
    """
    if not enabled():
        return None
    endpoint = url() + path
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=data, method="POST",
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + token()})
    try:
        with urllib.request.urlopen(req, timeout=timeout()) as resp:
            raw = resp.read().decode("utf-8")
            return Verdict(resp.status, json.loads(raw))
    except urllib.error.HTTPError as exc:
        try:
            payload = json.loads(exc.read().decode("utf-8"))
        except Exception:                        # noqa: BLE001 -- never raise
            payload = None
        if exc.code in VERDICT_STATUSES and payload is not None:
            return Verdict(exc.code, payload)
        if warn:
            _warn("%s returned HTTP %s%s -- falling back to the git path"
                  % (path, exc.code, _verdict_suffix(payload)))
        return None
    except Exception as exc:                     # noqa: BLE001 -- never raise
        # Deliberately broad. urllib raises URLError, socket.timeout, OSError,
        # ssl.SSLError, http.client.* and ValueError on a bad body, and the
        # exact set varies by python version and platform. Enumerating them is
        # how a fallback path acquires a hole; the fallback must be total.
        if warn:
            _warn("%s unreachable (%s: %s) -- falling back to the git path"
                  % (path, type(exc).__name__, exc))
        return None


def get(path: str, params=None, warn: bool = True):
    """GET one read-only predicate. Same contract as post()."""
    if not enabled():
        return None
    query = ""
    if params:
        pairs = []
        for key, val in params:
            pairs.append((key, val))
        query = "?" + urllib.parse.urlencode(pairs)
    req = urllib.request.Request(
        url() + path + query, method="GET",
        headers={"Authorization": "Bearer " + token()})
    try:
        with urllib.request.urlopen(req, timeout=timeout()) as resp:
            return Verdict(resp.status, json.loads(resp.read().decode("utf-8")))
    except urllib.error.HTTPError as exc:
        try:
            payload = json.loads(exc.read().decode("utf-8"))
        except Exception:                        # noqa: BLE001
            payload = None
        if exc.code in VERDICT_STATUSES and payload is not None:
            return Verdict(exc.code, payload)
        if warn:
            _warn("%s returned HTTP %s%s -- falling back to the git path"
                  % (path, exc.code, _verdict_suffix(payload)))
        return None
    except Exception as exc:                     # noqa: BLE001
        if warn:
            _warn("%s unreachable (%s: %s) -- falling back to the git path"
                  % (path, type(exc).__name__, exc))
        return None


# ---- typed wrappers, one per verb ----------------------------------------
#
# Thin on purpose. Each exists so the calling script names an operation rather
# than a URL string, and so a path typo is a NameError here instead of a silent
# 404 that degrades to git at runtime (which would look exactly like the mesh
# being down -- the one failure mode this whole module must not make ambiguous).

def open_task_claim(session_id, session_label, task, resources,
                    claimed_at=None, allow_overlap=False, spawned_by=None,
                    stale_after_hours=None, claude_session_id=None):
    body = {"session_id": session_id, "session_label": session_label,
            "task": task, "resources": list(resources or []),
            "allow_overlap": bool(allow_overlap)}
    if claimed_at:
        body["claimed_at"] = claimed_at
    if spawned_by:
        body["spawned_by"] = spawned_by
    # Omitted when unknown rather than sent as '': an older coordinator ignores
    # the unknown key either way, and the column is write-once so a missing
    # value can still be backfilled later.
    if claude_session_id:
        body["claude_session_id"] = claude_session_id
    if stale_after_hours:
        body["stale_after_hours"] = stale_after_hours
    return post("/task_claim/open", body)


def close_task_claim(session_id, closed_at, completion_note, claimed_at=None):
    body = {"session_id": session_id, "closed_at": closed_at,
            "completion_note": completion_note}
    if claimed_at:
        body["claimed_at"] = claimed_at
    return post("/task_claim/close", body)


def renew_task_claim(session_id, claimed_at=None, new_claimed_at=None):
    body = {"session_id": session_id}
    if claimed_at:
        body["claimed_at"] = claimed_at
    if new_claimed_at:
        body["new_claimed_at"] = new_claimed_at
    return post("/task_claim/renew", body)


def amend_task_claim(session_id, completion_note, claimed_at=None):
    body = {"session_id": session_id, "completion_note": completion_note}
    if claimed_at:
        body["claimed_at"] = claimed_at
    return post("/task_claim/amend", body)


def dedupe_task_claim(session_id, claimed_at=None):
    body = {"session_id": session_id}
    if claimed_at:
        body["claimed_at"] = claimed_at
    return post("/task_claim/dedupe", body)


def check_resources(resources):
    return get("/task_claim/check",
               [("resource", r) for r in (resources or [])])


def list_task_claims(status=None):
    """GET /task_claim/list, returning a Verdict (whose .get('claims') is the
    full list ordered by claimed_at) or None on any transport failure. The
    endpoint is unconditional (always 200), so getting a Verdict back here
    means the read succeeded, not that an arbitration verdict was rendered --
    unlike open/claim, this has no 409 refusal shape to distinguish."""
    params = [("status", status)] if status else []
    return get("/task_claim/list", params)


def record_chip(chip):
    return post("/chip/record", {"chip": chip})


def claim_chip(chip_ref=None, task_id=None, claimed_by=None, claimed_host=None,
               note=None, claimed_at=None, stale_after_hours=None):
    body = {"claimed_by": claimed_by}
    if chip_ref:
        body["chip_ref"] = chip_ref
    if task_id:
        body["task_id"] = task_id
    if claimed_host:
        body["claimed_host"] = claimed_host
    if note is not None:
        body["note"] = note
    if claimed_at:
        body["claimed_at"] = claimed_at
    if stale_after_hours:
        body["stale_after_hours"] = stale_after_hours
    return post("/chip/claim", body)


def unclaim_chip(chip_ref=None, task_id=None, note=None):
    body = {}
    if chip_ref:
        body["chip_ref"] = chip_ref
    if task_id:
        body["task_id"] = task_id
    if note is not None:
        body["note"] = note
    return post("/chip/unclaim", body)


def resolve_chip(status, chip_ref=None, task_id=None, note=None,
                 resolved_by_session_id=None, note_auto=False, force=False,
                 resolved_at=None):
    body = {"status": status, "force": bool(force),
            "note_auto": bool(note_auto)}
    if chip_ref:
        body["chip_ref"] = chip_ref
    if task_id:
        body["task_id"] = task_id
    if note is not None:
        body["note"] = note
    if resolved_by_session_id:
        body["resolved_by_session_id"] = resolved_by_session_id
    if resolved_at:
        body["resolved_at"] = resolved_at
    return post("/chip/resolve", body)


def record_chip_episode(chip_ref, episode):
    """POST one observation episode into a standing OPEN chip (W5a,
    2026-08-29). See the coordinator's /chip/episode contract."""
    return post("/chip/episode", {"chip_ref": chip_ref, "episode": episode})


def fetch_chip(chip_ref=None, task_id=None):
    """GET one chip's full entry_json from the coordinator, or None.

    Read-only lookup for the suppressed-record lag window: a chip recorded
    with the git write suppressed exists in the coordinator DB immediately but
    reaches this box's TASK_CHIPS.json only after the hub materializer's next
    render plus a local pull -- so a same-session `resolve`/`claim` right
    after `record` misses the local file. Callers use this as the fallback
    lookup when the local file has no such chip and the transport is enabled.
    Returns the chip dict on an exact chip_ref/task_id match, else None (not
    found, transport off, or any transport failure -- caller falls back to
    its ordinary local-miss handling)."""
    params = []
    if chip_ref:
        params.append(("chip_ref", chip_ref))
    if task_id:
        params.append(("task_id", task_id))
    if not params:
        return None
    v = get("/chip/list", params + [("limit", "2")])
    if v is None or not v.ok:
        return None
    chips = (v.payload or {}).get("chips") or []
    for c in chips:
        if chip_ref and c.get("chip_ref") == chip_ref:
            return c
        if task_id and c.get("task_id") == task_id:
            return c
    return None


def list_chips(status=None, origin=None, chip_ref=None, task_id=None, limit=None):
    """GET /chip/list, returning the raw chips list, or None on ANY transport
    failure or a non-ok verdict (mode off, unreachable, 5xx, unparseable
    body). Deliberately never [] for "no answer" -- an empty list must mean
    the coordinator's genuine answer is empty, not that nothing was heard
    back, so a caller can tell "fall back to git" (None) apart from
    "genuinely no chips" ([]). kind is not filterable server-side (the
    endpoint has no such column predicate); callers apply it client-side on
    the returned list."""
    params = []
    if status:
        params.append(("status", status))
    if origin:
        params.append(("origin", origin))
    if chip_ref:
        params.append(("chip_ref", chip_ref))
    if task_id:
        params.append(("task_id", task_id))
    if limit:
        params.append(("limit", str(limit)))
    v = get("/chip/list", params)
    if v is None or not v.ok:
        return None
    return (v.payload or {}).get("chips")


def attach_chip(chip_ref, task_id, attached_by_session_id=None,
                stale_after_hours=None):
    body = {"chip_ref": chip_ref, "task_id": task_id}
    if attached_by_session_id:
        body["attached_by_session_id"] = attached_by_session_id
    if stale_after_hours:
        body["stale_after_hours"] = stale_after_hours
    return post("/chip/attach", body)


def amend_chip_prompt(chip_ref, prompt, reason=None):
    body = {"chip_ref": chip_ref, "prompt": prompt}
    if reason:
        body["reason"] = reason
    return post("/chip/amend-prompt", body)


def amend_chip_note(chip_ref, addendum, reason=None, session_id=None):
    """APPEND to a RESOLVED chip's resolution_note. Append-only by design --
    see db.amend_chip_note for why replacing would reintroduce the very
    clobber hazard resolve's equal-status note freeze exists to prevent."""
    body = {"chip_ref": chip_ref, "addendum": addendum}
    if reason:
        body["reason"] = reason
    if session_id:
        body["session_id"] = session_id
    return post("/chip/amend-note", body)


def append_workspace_state(text, timestamp=None, session_id=None,
                           client_git_write=None):
    """PHASE-4: spool one WORKSPACE_STATE.md closing entry on the hub for the
    materializer to land. Append-only -- there is deliberately no edit or
    delete counterpart. client_git_write=True declares this client will ALSO
    append+commit the entry itself (dual-write soak; the materializer then
    only watches for it), False that the client suppressed its git write and
    the materializer owns landing it."""
    body = {"text": text}
    if timestamp:
        body["timestamp"] = timestamp
    if session_id:
        body["session_id"] = session_id
    if client_git_write is not None:
        body["client_git_write"] = bool(client_git_write)
    return post("/workspace_state/append", body)


def fetch_shadow_status():
    """GET /shadow/status -- the coordinator's fleet snapshot (per-machine
    heartbeat rows: machine, last_seen, state, current_exq, progress dict,
    lifecycle_state, ...). Returns the parsed dict, or None on ANY failure
    (transport disabled, unreachable, non-200). This is the coordinator-
    primary replacement for reading the retired git heartbeat mirror
    (REE_assembly evidence/experiments/runner_heartbeats/); consumers fall
    back to their git read when this returns None."""
    verdict = get("/shadow/status", warn=False)
    if verdict is None or not verdict.ok:
        return None
    payload = getattr(verdict, "payload", None)
    if isinstance(payload, dict):
        return payload
    # Verdict may expose fields via .get(); rebuild the dict defensively.
    try:
        machines = verdict.get("machines")
    except Exception:  # noqa: BLE001
        return None
    return {"machines": machines} if machines is not None else None


def fetch_machine_rows():
    """fetch_shadow_status() reduced to {machine_name: row}. None on any
    failure -- never an empty dict for a transport problem, so a caller can
    distinguish 'coordinator says no machines' from 'could not ask'."""
    doc = fetch_shadow_status()
    if not isinstance(doc, dict):
        return None
    rows = {}
    for r in doc.get("machines") or []:
        if isinstance(r, dict) and r.get("machine"):
            rows[r["machine"]] = r
    return rows


def dispatcher_control_via_coordinator() -> bool:
    """PHASE-4 cutover predicate for dispatcher_control.json leases -- the
    Dispatcher run-lease's own soak/go-live flag, independent of every other
    routed file (each one soaks and flips on its own schedule -- see
    suppress_workspace_state_git_write()/suppress_recommendation_log_git_write()
    for the same shape). Env DISPATCHER_CONTROL_VIA_COORDINATOR wins, else the
    config file's dispatcher_control_via_coordinator. Default OFF.

    UNLIKE the two predicates above, this ONE flag governs BOTH directions at
    once -- grant_dispatcher_lease() dual-writing (coordinator POST, git
    write UNCHANGED and never suppressed by this flag) AND
    fetch_dispatcher_leases() being consulted coordinator-PRIMARY before the
    git fallback. That is deliberate, not a simplification: the lease is
    FAIL-CLOSED (scripts/dispatcher_control.py's own doctrine -- missing or
    expired means STOP), so a box whose READ side trusted the coordinator
    while its WRITE side (or a renewing Orchestrator's box) still only wrote
    git would see a real grant as absent and stop dispatch fleet-wide. A
    single flag makes that split impossible to reach through this predicate
    alone. There is deliberately no separate suppress-git-write predicate
    for this lane yet (unlike the two above) -- the git write stays a dual
    write until a materializer-verified go-live decision adds one, mirroring
    why coordinator_open() in task_claim.py never suppresses its own git
    write in PHASE-2a.
    """
    if not enabled():
        return False
    env = os.environ.get("DISPATCHER_CONTROL_VIA_COORDINATOR")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("dispatcher_control_via_coordinator"))


def grant_dispatcher_lease(dispatcher, entry):
    """POST /dispatcher/lease -- upsert one dispatcher's lease row. `entry`
    is the full lease dict exactly as dispatcher_control.json's
    dispatchers[<name>] carries it (lossless passthrough -- see
    ree-v3/coordinator/app.py._dispatcher_lease and db.upsert_dispatcher_lease
    for the newest-requested_at-wins reconciliation). Returns a Verdict, or
    None on any transport failure (mode off, unreachable, HTTP error) --
    the caller's git write is the fallback of record either way, so this
    stays best-effort and non-fatal by construction (see post())."""
    return post("/dispatcher/lease", {"dispatcher": dispatcher, "entry": entry})


def fetch_dispatcher_leases():
    """GET /dispatcher/leases -- the coordinator's current lease rows,
    rendered exactly as dispatcher_control.json's `dispatchers` map (see
    ree-v3/coordinator/app.py's /dispatcher/leases handler). Returns the
    dispatchers dict (possibly {} -- a coordinator genuinely holding no
    leases), or None on ANY transport failure (mode off, unreachable, non-200,
    or a malformed body missing the `dispatchers` key) -- never {} for a
    transport problem, so a caller can tell 'coordinator says no leases'
    apart from 'could not ask' and fall back to the git file only for the
    latter."""
    v = get("/dispatcher/leases", warn=False)
    if v is None or not v.ok:
        return None
    payload = v.payload if isinstance(v.payload, dict) else {}
    dispatchers = payload.get("dispatchers")
    return dispatchers if isinstance(dispatchers, dict) else None


def suppress_dispatch_campaigns_git_write() -> bool:
    """Cutover predicate for scripts/dispatch_campaigns.json (2026-09-16,
    chip-20260916-campaign-ledger-coordinator) -- its own flag, same shape as
    suppress_recommendation_log_git_write() and for the same reason: each
    routed file soaks and flips independently. While OFF (the default) an
    armed-transport client still POSTs every mutation (the coordinator's
    verdict is binding either way -- record-launch's cross-box arbitration
    in particular) AND runs today's git write, byte-identical to what the DB
    now holds, so the hub registry materializer ingests that git write and
    finds it already current. Flipping ON makes a VERIFIED coordinator ack
    (scripts/dispatch_campaigns.verify_campaign_ack) the durable write and
    the materializer the one git writer. Env
    DISPATCH_CAMPAIGNS_SUPPRESS_GIT_WRITE wins, else the config file's
    dispatch_campaigns_suppress_git_write. NOTE the hub's ree-coordinator
    must be RESTARTED on a ree-v3 carrying the /campaign/* endpoints, and the
    registry writer's clone must carry render_dispatch_campaigns, before
    this is armed -- or suppressed writes sit in the DB unlanded. Until that
    restart the endpoints answer 404 and every verb degrades to git."""
    if not enabled():
        return False
    env = os.environ.get("DISPATCH_CAMPAIGNS_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("dispatch_campaigns_suppress_git_write"))


def add_campaign(entry, now=None):
    """POST /campaign/add -- the orchestrator's curated entry on EITHER
    lane (campaign-bundle, or a single science chip with its recorded
    pre-flight; the hub learned the science lane 2026-09-17, ree-v3
    coordinator/db.py), lossless passthrough (exactly the dict save_doc
    would append).
    `now` is the client's own stamp so DB and git entries agree byte for
    byte under dual write. Returns a Verdict ('ok' | 'idempotent' on 200;
    'exists' | 'member_overlap' on 409; 'bad_entry' on 400) or None."""
    body = {"entry": entry}
    if now:
        body["now"] = now
    return post("/campaign/add", body)


def record_campaign_launch(campaign_id, launch, now=None):
    """POST /campaign/record-launch -- the dispatcher's one write and the
    cross-box MUTEX (server-side BEGIN IMMEDIATE). `launch` is the full
    launch dict {box, session_uuid, worktree, at, launched_by}. Returns a
    Verdict ('ok' | 'idempotent' on 200; 'already_launched' | 'not_live' on
    409; 'not_found' on 404) or None."""
    body = {"campaign_id": campaign_id, "launch": launch}
    if now:
        body["now"] = now
    return post("/campaign/record-launch", body)


def set_campaign_status(campaign_id, status, by, note=None, at=None, now=None):
    """POST /campaign/status -- expire / withdraw / gc transitions. Returns
    a Verdict ('ok' | 'idempotent' on 200; 'closed' on 409; 'not_found' on
    404; 'bad_status' on 400) or None."""
    body = {"campaign_id": campaign_id, "status": status, "by": by}
    if note is not None:
        body["note"] = note
    if at:
        body["at"] = at
    if now:
        body["now"] = now
    return post("/campaign/status", body)


def fetch_campaigns(status=None, live=None, now=None, campaign_id=None):
    """GET /campaign/list -- the coordinator's campaigns in ledger order,
    rendered exactly as scripts/dispatch_campaigns.json's `campaigns` list.
    Returns the list (possibly [] -- a coordinator genuinely holding none),
    or None on ANY transport failure (mode off, unreachable, non-200 -- a hub
    not yet serving the route answers 404 -- or a malformed body), same
    None-vs-[] discipline as fetch_dispatcher_leases()."""
    params = []
    if status:
        params.append(("status", status))
    if live:
        params.append(("live", "1"))
    if now:
        params.append(("now", now))
    if campaign_id:
        params.append(("campaign_id", campaign_id))
    v = get("/campaign/list", params or None, warn=False)
    if v is None or not v.ok:
        return None
    payload = v.payload if isinstance(v.payload, dict) else {}
    rows = payload.get("campaigns")
    return rows if isinstance(rows, list) else None


def suppress_recommendation_log_git_write() -> bool:
    """PHASE-4 cutover predicate for RECOMMENDATION_LOG.jsonl appends -- its
    own flag, same shape as suppress_workspace_state_git_write() and for the
    same reason: each routed file soaks and flips independently. While OFF
    (the default) an armed-transport client still POSTs the record (declaring
    client_git_write=true) AND runs today's git append; the hub materializer
    only watches for it. Flipping ON makes the materializer the one writer.
    Env RECOMMENDATION_LOG_SUPPRESS_GIT_WRITE wins, else the config file's
    recommendation_log_suppress_git_write. NOTE the hub registry writer's
    DEPLOYED copy must include render_recommendation_log (ree-v3 ca1369bf98+)
    before this is armed, or suppressed records sit in the DB unlanded."""
    if not enabled():
        return False
    env = os.environ.get("RECOMMENDATION_LOG_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("recommendation_log_suppress_git_write"))


def append_recommendation_log(record, session_id=None, client_git_write=None):
    """PHASE-4: spool one RECOMMENDATION_LOG.jsonl record line on the hub for
    the materializer to land. Append-only, the jsonl-trivial sibling of
    append_workspace_state. `record` is the exact single-line JSON string the
    git path would append -- byte-fidelity is what makes the materializer's
    presence check exact."""
    body = {"record": record}
    if session_id:
        body["session_id"] = session_id
    if client_git_write is not None:
        body["client_git_write"] = bool(client_git_write)
    return post("/recommendation_log/append", body)


def suppress_igw_log_git_write() -> bool:
    """PHASE-4 cutover predicate for igw_routine_log.md appends -- its own
    flag, same shape as suppress_recommendation_log_git_write() and for the
    same reason: each routed file soaks and flips independently. While OFF
    (the default) an armed-transport client still POSTs the line (declaring
    client_git_write=true) AND runs today's git append; the dedicated
    REE_assembly writer (ree_assembly_git_writer.py -- NOT the umbrella
    registry writer, this file lives in a different repo) only watches for
    it. Flipping ON makes that writer the one landing it. Env
    IGW_LOG_SUPPRESS_GIT_WRITE wins, else the config file's
    igw_log_suppress_git_write. NOTE the hub must be running
    ree-assembly-git-writer's timer before this is armed, or suppressed
    lines sit in the DB unlanded."""
    if not enabled():
        return False
    env = os.environ.get("IGW_LOG_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("igw_log_suppress_git_write"))


def append_igw_log(line, session_id=None, client_git_write=None):
    """PHASE-4: spool one igw_routine_log.md heartbeat line on the hub for
    the dedicated REE_assembly writer to land. Append-only, the plain-text
    sibling of append_recommendation_log -- `line` is the exact text
    scripts/igw_routine_tick.py's append_log() would write, stripped of its
    own trailing newline; byte-fidelity is what makes the writer's presence
    check exact."""
    body = {"line": line}
    if session_id:
        body["session_id"] = session_id
    if client_git_write is not None:
        body["client_git_write"] = bool(client_git_write)
    return post("/igw_log/append", body)


def fetch_igw_log_pending():
    """GET /igw_log/pending -- observability read for the igw_routine_log.md
    PHASE-4 intake spool (ree-v3/coordinator/app.py's handler; each row
    carries entry_id/session_id/client_git_write/submitted_at/line_head).
    Returns the `pending` list (possibly [] -- a genuinely empty backlog), or
    None on ANY transport failure (mode off, unreachable, non-200, or a
    malformed body missing the `pending` key) -- same discipline as
    fetch_dispatcher_leases(): never [] for a transport problem, so a caller
    (igw_routine_tick.check_igw_log_backlog_staleness) can tell 'coordinator
    says no backlog' apart from 'could not ask' and skip the staleness check
    on the latter rather than falsely reporting all-clear."""
    return fetch_phase4_pending("/igw_log/pending")


def fetch_phase4_pending(path):
    """GET one PHASE-4 append-route `/<route>/pending` observability endpoint
    (/igw_log/pending, /recommendation_log/pending, /workspace_state/pending
    -- all in ree-v3/coordinator/app.py, all returning {"pending": [...]}).
    Same None-vs-[] discipline as fetch_igw_log_pending(), which delegates
    here: [] means the coordinator reported no backlog, None means we could
    not ask."""
    v = get(path, warn=False)
    if v is None or not v.ok:
        return None
    payload = v.payload if isinstance(v.payload, dict) else {}
    pending = payload.get("pending")
    return pending if isinstance(pending, list) else None


def suppress_igw_ledger_git_write() -> bool:
    """PHASE-4 cutover predicate for igw_routine_ledger.json CAS replaces --
    its own flag, same shape as suppress_igw_log_git_write() and for the
    same reason: each routed file soaks and flips independently. While OFF
    (the default) an armed-transport client still submits the intent (dual-
    write soak: it also still writes+commits via git) and flipping ON makes
    the hub materializer the only writer for this path once its writer is
    deployed. Env IGW_LEDGER_SUPPRESS_GIT_WRITE wins, else the config
    file's igw_ledger_suppress_git_write."""
    if not enabled():
        return False
    env = os.environ.get("IGW_LEDGER_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("igw_ledger_suppress_git_write"))


def suppress_igw_assignments_git_write() -> bool:
    """PHASE-4 cutover predicate for igw_assignments.json CAS replaces --
    mirrors suppress_igw_ledger_git_write() exactly, one flag per routed
    file so each soaks and flips independently. Env
    IGW_ASSIGNMENTS_SUPPRESS_GIT_WRITE, config
    igw_assignments_suppress_git_write."""
    if not enabled():
        return False
    env = os.environ.get("IGW_ASSIGNMENTS_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("igw_assignments_suppress_git_write"))


def suppress_igw_workset_git_write() -> bool:
    """PHASE-4 cutover predicate for the inter_governance_workset CAS
    replaces -- covers BOTH the .v1.json and the .md, one flag for the pair
    (igw_routine_tick.py's commit_workset_files() always regenerates and
    commits them together; splitting the flag would let one land without
    the other). Env IGW_WORKSET_SUPPRESS_GIT_WRITE, config
    igw_workset_suppress_git_write."""
    if not enabled():
        return False
    env = os.environ.get("IGW_WORKSET_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("igw_workset_suppress_git_write"))


def suppress_igw_proposals_git_write() -> bool:
    """PHASE-4 cutover predicate for experiment_proposals.v1.json CAS
    replaces. Env IGW_PROPOSALS_SUPPRESS_GIT_WRITE, config
    igw_proposals_suppress_git_write."""
    if not enabled():
        return False
    env = os.environ.get("IGW_PROPOSALS_SUPPRESS_GIT_WRITE")
    if env is not None and env != "":
        return env.strip().lower() in ("1", "true", "yes", "on")
    return bool(_config().get("igw_proposals_suppress_git_write"))


def submit_intent_replace(repo, path, base_sha, content, message,
                          session_id=None, shadow=None, allow_shrink=False):
    """PHASE-4: submit one whole-file CAS intent -- POST /intent/replace,
    the generic editorial-file verb (phase4_commit_intake_design.md section
    3.2; git_intent.py is the server-side implementation). Unlike the
    append wrappers above, this verb itself carries no suppress-decision
    field -- a CAS replace's effect is already fully described by
    base_sha/content, so suppression is decided PER FILE by the caller
    (igw_routine_tick.py's `_ree_commit()`, the single call site per
    phase4_commit_intake_design.md section 5) via the four
    suppress_igw_{ledger,assignments,workset,proposals}_git_write()
    predicates above.

    `base_sha` must be the origin commit the caller's `content` was edited
    FROM -- and, per DP-1, edited from ORIGIN's content (e.g. `git show
    <base_sha>:<path>` against the same remote this posts to), never from a
    local working-tree read, which is exactly the read-modify-write
    contamination this verb exists to close. Passing a working-tree-derived
    base defeats that guarantee silently -- the server cannot tell the
    difference.

    Returns a Verdict (verdict in {'applied', 'base_moved', 'not_routed',
    'validation_failed', 'suspicious_shrink', 'repo_not_configured',
    'origin_unreadable', 'push_failed', 'error'}), or None meaning "no
    verdict, fall back to git" (transport off/unreachable/any failure,
    same contract as every other function in this module). A 'base_moved'
    verdict is a normal, expected outcome (409), not a resource-ownership
    refusal -- it carries `current_sha`/`current_content` for the caller to
    rebase from and resubmit."""
    body = {"repo": repo, "path": path, "content": content,
           "message": message}
    if base_sha is not None:
        body["base_sha"] = base_sha
    if session_id:
        body["session_id"] = session_id
    if shadow is not None:
        body["shadow"] = bool(shadow)
    if allow_shrink:
        body["allow_shrink"] = True
    return post("/intent/replace", body)


# `archive` has NO wrapper here, and must not grow one in Phase 2 (plan doc D7).
# Its correctness gate is that the archive file has actually reached ORIGIN --
# cmd_archive fetches and verifies at origin_ref() before stripping, after the
# 2026-08-19 first-run failure. That gate is inherently a git fact with no DB
# equivalent, so archiving stays git-side.


if __name__ == "__main__":
    # `python3 coordinator_transport.py` prints the resolved configuration.
    # Deliberately the only CLI surface: this is a library, and a --claim style
    # entry point here would be a second, untested way to do what the two real
    # scripts already do.
    print(describe())
