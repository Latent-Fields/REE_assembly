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
handling it. The only changes are that the child is asked to exit first,
and that the post-SIGKILL drain of its pipes is BOUNDED, so `timeout=`
stays a real wall-clock ceiling even when a surviving grandchild still
holds them open. See `DEFAULT_REAP_SECONDS`.

`run_soft_timeout()` (below) is the opt-in variant for callers that want a
timeout to be a FAILED RESULT rather than an exception. See its docstring.
"""

import subprocess as _subprocess
import types

__all__ = [
    "run", "run_soft_timeout", "wrap", "DEFAULT_GRACE_SECONDS",
    "DEFAULT_REAP_SECONDS", "TIMEOUT_RETURNCODE",
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

# How long to keep draining the child's pipes AFTER the SIGKILL before
# giving up on the streams entirely.
#
# WHY THIS BOUND EXISTS. A killed child does not necessarily close the pipes
# the caller is reading: every process the child spawned INHERITED the same
# write ends, so the read side sees EOF only when the LAST descendant exits.
# Draining without a bound therefore makes the caller's `timeout=` unenforceable.
#
# Measured 2026-07-21 (macOS): `git add` on a file whose clean filter is
# `sleep 120`. git takes SIGTERM, unlinks its lockfile and exits promptly --
# but the filter process survives holding git's stderr, verified with `lsof`
# (the filter's fd 2 is the SAME pipe as git's fd 2; only fd 1 is re-plumbed
# to git). A `run(..., timeout=30)` returned after ~120s: the grandchild's
# lifetime, not the caller's timeout. The callers here are unattended loops
# (serve.py's 5-minute `_auto_pull` thread, the hourly igw tick), where a
# multi-minute stall is a real stall.
#
# NOT stdlib-identical, in either direction. On POSIX, CPython's `run()` does
# NOT re-drain after the kill -- it does `process.wait()` and lifts the partial
# output off the `TimeoutExpired` that `_communicate` already populated
# (verified against 3.13's source; the bare `communicate()` is the _mswindows
# branch only, where the reads live on child threads that must be joined). So
# the unbounded drain this replaces was a deviation THIS module introduced when
# it grew the SIGTERM escalation, not inherited behaviour. Bounding it restores
# the stdlib's wall-clock guarantee while keeping the one thing the re-drain
# buys: output the child emitted between the SIGTERM and its death.
#
# Two seconds is generous for the ordinary case, where the killed child was
# the only pipe holder and the read hits EOF immediately.
DEFAULT_REAP_SECONDS = 2.0


def run(*popenargs, input=None, capture_output=False, timeout=None, check=False,
        grace=DEFAULT_GRACE_SECONDS, reap=DEFAULT_REAP_SECONDS, **kwargs):
    """Drop-in `subprocess.run` that SIGTERMs (not SIGKILLs) on timeout.

    On timeout: send SIGTERM, wait up to `grace` seconds for the child to
    exit on its own, and only then SIGKILL. `TimeoutExpired` is raised
    either way, carrying whatever output was captured, so callers see the
    same exception they see today.

    The post-SIGKILL drain is bounded by `reap` seconds, so
    `timeout + grace + reap` is a genuine wall-clock ceiling
    even when a surviving GRANDCHILD still holds the inherited pipes. See
    `DEFAULT_REAP_SECONDS`. Giving up on the STREAMS is not giving up on the
    PROCESS: it has already been SIGKILLed by that point, and `Popen.__exit__`
    reaps it on the way out.

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
                # Ignored SIGTERM (or wedged) -- or exited while a descendant
                # kept the pipes open, which is indistinguishable from here.
                process.kill()
                try:
                    stdout, stderr = process.communicate(timeout=reap)
                except _subprocess.TimeoutExpired as reap_exc:
                    # The pipes outlived the child: a grandchild still holds
                    # the inherited write ends, so the read will not see EOF
                    # until IT exits. Give up on the STREAMS -- not on the
                    # process, which is already SIGKILLed and gets reaped by
                    # `Popen.__exit__` below -- and report whatever partial
                    # output was drained before we stopped waiting, which is
                    # exactly what the stdlib's POSIX path reports.
                    stdout, stderr = reap_exc.output, reap_exc.stderr
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
