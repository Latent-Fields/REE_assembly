"""A `subprocess.run` whose timeout path terminates the child GRACEFULLY.

VENDORED COPY -- KEEP IN SYNC
-----------------------------
The canonical copy of this module is `ree-v3/graceful_timeout.py`, where its
contract lives (`ree-v3/tests/contracts/test_graceful_timeout_lockfile.py`).
Byte-identical copies are vendored into:

    ree-v3/graceful_timeout.py               <- canonical (+ contract test)
    REE_assembly/graceful_timeout.py            (serve.py)
    REE_Working/scripts/graceful_timeout.py     (igw_routine_tick.py)

The three copies below this banner are byte-identical, and the banner
itself is identical too, so `shasum` over all three must match.

WHY VENDORED RATHER THAN SHARED. These are three independently-cloned git
repos -- a cross-repo import (`sys.path` hop into a sibling checkout) would
work on this Mac and break on the hub, the cloud workers, and any fresh
clone, silently falling back to the stdlib `subprocess.run` and re-arming
the exact bug this module fixes. The module is ~240 lines of pure stdlib
with no project imports and no configuration, so a copy cannot drift
functionally without someone editing it. If you DO edit it, edit the
canonical copy, re-run its contract, and re-copy to the two others
(`shasum` the three; they must match below the banner).

WHY THIS EXISTS
---------------
`subprocess.run(..., timeout=N)` SIGKILLs the child when the timeout fires.
CPython's implementation is literally::

    try:
        stdout, stderr = process.communicate(input, timeout=timeout)
    except TimeoutExpired as exc:
        process.kill()          # <-- Popen.kill() == send_signal(SIGKILL)

SIGKILL is uncatchable, so the child gets no chance to run its cleanup.

For `git` that is destructive rather than merely abrupt. Git takes
`.git/index.lock` for the whole of any index-writing command (`add`,
`commit`, `status` -- it rewrites the stat cache -- `reset`, `checkout`,
`stash`, `pull`, `rebase`, `merge`) and registers a signal handler that
unlinks the lockfile on SIGINT / SIGHUP / SIGTERM / SIGQUIT / SIGPIPE.
SIGKILL bypasses that handler, so a timed-out git leaves an ORPHAN
`.git/index.lock` behind. Measured directly (2026-07-21, macOS, git 2.x,
a `git add` held open by a slow clean filter)::

    SIGTERM: lock during=True  lock AFTER=False     <- git cleaned up
    SIGKILL: lock during=True  lock AFTER=True      <- orphan

An orphaned lock is not a nuisance-level failure in this workspace. It
blocks `scripts/ree_commit.py`'s shared-index refresh, which leaves the
just-committed paths staged in the SHARED index as a staged REVERT of the
commit that just landed -- so the next session running a plain
`git commit` in that checkout lands the revert over the work. That is the
documented mode-2 hazard in CLAUDE.md.

Confirmed incidence: `REE_assembly/runner.log` carries 274 `TimeoutExpired`
tracebacks against index-taking git commands (`git status --porcelain`
timeout=10, `git pull --rebase --autostash` timeout=30, `git rebase
--abort` timeout=10), against 270 runner restarts -- i.e. the runner has
crash-looped on this, SIGKILLing a lock-holding git each time, in BOTH
`ree-v3` and `REE_assembly` (`git_pull` is called on both every loop tick).

USAGE
-----
One line per module, immediately after `import subprocess`::

    import subprocess
    import graceful_timeout
    subprocess = graceful_timeout.wrap(subprocess)

`wrap()` returns a real `ModuleType` whose `__dict__` is a copy of the
stdlib module's with `run` replaced, so `subprocess.Popen`,
`subprocess.PIPE`, `subprocess.TimeoutExpired` and friends are the SAME
objects as the stdlib's -- `isinstance` and `except` clauses elsewhere keep
working. The rebinding is module-local: the stdlib module is not mutated,
so no other importer is affected.

Behaviour is otherwise identical to `subprocess.run`, including still
raising `TimeoutExpired` -- callers that already handle a timeout keep
handling it. The only change is that the child is asked to exit first.

`run_soft_timeout()` (below) is the opt-in variant for callers that want a
timeout to be a FAILED RESULT rather than an exception. See its docstring.
"""

import subprocess as _subprocess
import types

__all__ = [
    "run", "run_soft_timeout", "wrap", "DEFAULT_GRACE_SECONDS",
    "TIMEOUT_RETURNCODE",
]

# Return code carried by the synthetic CompletedProcess `run_soft_timeout`
# hands back on a timeout. 124 is what `timeout(1)` exits with, and it is
# outside git's own exit-code range, so a caller that wants to distinguish
# "git said no" from "git never answered" can, while every caller that only
# checks `returncode != 0` needs no change at all.
TIMEOUT_RETURNCODE = 124

# How long to let the child clean up after SIGTERM before escalating to
# SIGKILL. Unlinking a lockfile is microseconds; this only has to cover a
# heavily loaded machine getting the process scheduled. Kept short so a
# child that ignores SIGTERM cannot extend the caller's timeout budget by
# much.
DEFAULT_GRACE_SECONDS = 5.0


def run(*popenargs, input=None, capture_output=False, timeout=None, check=False,
        grace=DEFAULT_GRACE_SECONDS, **kwargs):
    """Drop-in `subprocess.run` that SIGTERMs (not SIGKILLs) on timeout.

    On timeout: send SIGTERM, wait up to `grace` seconds for the child to
    exit on its own, and only then SIGKILL. `TimeoutExpired` is raised
    either way, carrying whatever output was captured, so callers see the
    same exception they see today.

    With `timeout=None` this delegates straight to `subprocess.run` -- there
    is no timeout path to fix, and delegating keeps the no-timeout case
    bit-identical to the stdlib.
    """
    if timeout is None:
        return _subprocess.run(*popenargs, input=input, check=check,
                               capture_output=capture_output, **kwargs)

    # `input` and `capture_output` are run()-level conveniences, not Popen
    # kwargs -- translate them exactly as the stdlib does before we Popen.
    if input is not None:
        if kwargs.get("stdin") is not None:
            raise ValueError("stdin and input arguments may not both be used.")
        kwargs["stdin"] = _subprocess.PIPE
    if capture_output:
        if kwargs.get("stdout") is not None or kwargs.get("stderr") is not None:
            raise ValueError("stdout and stderr arguments may not be used "
                             "with capture_output.")
        kwargs["stdout"] = _subprocess.PIPE
        kwargs["stderr"] = _subprocess.PIPE

    with _subprocess.Popen(*popenargs, **kwargs) as process:
        try:
            stdout, stderr = process.communicate(input, timeout=timeout)
        except _subprocess.TimeoutExpired:
            # THE FIX. SIGTERM lets git unlink .git/index.lock itself.
            process.terminate()
            try:
                stdout, stderr = process.communicate(timeout=grace)
            except _subprocess.TimeoutExpired:
                # Ignored SIGTERM (or wedged). Fall back to the stdlib's
                # behaviour rather than hang the caller forever.
                process.kill()
                stdout, stderr = process.communicate()
            raise _subprocess.TimeoutExpired(
                process.args, timeout, output=stdout, stderr=stderr)
        except BaseException:
            # Matches the stdlib: on anything else (incl. KeyboardInterrupt)
            # kill and re-raise. Reaped by Popen.__exit__.
            process.kill()
            raise
        retcode = process.poll()
        if check and retcode:
            raise _subprocess.CalledProcessError(
                retcode, process.args, output=stdout, stderr=stderr)
    return _subprocess.CompletedProcess(process.args, retcode, stdout, stderr)


def _text_mode(kwargs) -> bool:
    """True iff these run() kwargs put the child's streams in text mode."""
    return bool(
        kwargs.get("text")
        or kwargs.get("universal_newlines")
        or kwargs.get("encoding")
        or kwargs.get("errors")
    )


def _coerce(value, text: bool):
    """Normalise a TimeoutExpired's partial output to the caller's stream mode.

    `TimeoutExpired.output` / `.stderr` are None when nothing was captured,
    and are bytes even in text mode on some paths -- so a caller doing
    `r.stdout.splitlines()` would hit AttributeError or a bytes/str mismatch
    on the very path that is supposed to be the SAFE one.
    """
    if value is None:
        return "" if text else b""
    if text and isinstance(value, bytes):
        return value.decode("utf-8", "replace")
    if not text and isinstance(value, str):
        return value.encode("utf-8", "replace")
    return value


def run_soft_timeout(*popenargs, on_timeout=None, **kwargs):
    """`run()`, but a TIMEOUT is returned as a failed result, not raised.

    Returns a synthetic `CompletedProcess` with `returncode ==
    TIMEOUT_RETURNCODE` carrying whatever partial output was captured, plus
    a `timed out after Ns` marker appended to stderr.

    WHY. The runner's git call sites all branch on `returncode != 0` and
    already have a correct degrade-and-retry-next-tick path for a git that
    says no -- `_list_unmerged_paths` even documents "Returns None if `git
    status --porcelain` failed". But a TIMEOUT raises instead of returning,
    so those paths never ran: the exception propagated out of `git_pull`
    and out of `main()`, killing the process. `REE_assembly/runner.log`
    carries 274 `TimeoutExpired` tracebacks against 270 `[runner] Runner
    version` startup lines -- i.e. essentially every runner restart was a
    git-timeout crash, respawned by launchd (`com.ree.runner`, KeepAlive).
    A transient 10s git stall on a contended laptop should be a skipped
    tick, not a process death.

    `on_timeout(exc)` is invoked (best-effort, exceptions ignored) before
    the synthetic result is returned, so the caller can LOG every timeout.
    Nothing here swallows a timeout silently -- the whole point is that the
    rate stays visible while the process survives.

    `check=True` still RAISES the `TimeoutExpired`: a caller that asked for
    failures-as-exceptions gets one. `on_timeout` fires first either way.
    """
    try:
        return run(*popenargs, **kwargs)
    except _subprocess.TimeoutExpired as exc:
        if on_timeout is not None:
            try:
                on_timeout(exc)
            except Exception:
                pass
        if kwargs.get("check"):
            raise
        text = _text_mode(kwargs)
        stderr = _coerce(exc.stderr, text)
        marker = "timed out after %ss" % exc.timeout
        if text:
            stderr = (stderr + "\n" + marker) if stderr else marker
        else:
            sep = b"\n" if stderr else b""
            stderr = stderr + sep + marker.encode("ascii")
        return _subprocess.CompletedProcess(
            exc.cmd, TIMEOUT_RETURNCODE, _coerce(exc.output, text), stderr,
        )


def wrap(module=_subprocess):
    """Return a module-shaped view of `module` with `run` replaced by ours.

    A real `ModuleType` holding a COPY of the original `__dict__`, so every
    other attribute is the identical object the stdlib exports and the
    stdlib module itself is left unmutated.
    """
    shim = types.ModuleType(module.__name__)
    shim.__dict__.update(module.__dict__)
    shim.__dict__["run"] = run
    shim.__dict__["__wrapped_module__"] = module
    shim.__dict__["__doc__"] = (
        "%s, with run() replaced by graceful_timeout.run (SIGTERM before "
        "SIGKILL on timeout, so git can unlink .git/index.lock)."
        % (module.__doc__ or module.__name__)
    )
    return shim
