"""serve.py auto-pull: the pre-pull FOSSIL reconcile wiring (2026-09-20).

WHY THIS FILE EXISTS
--------------------
`igw_routine_tick.py` lands `evidence/planning/igw_routine_log.md` with
`ree_commit.py --to-remote-tip`, which pushes the edit WITHOUT moving the local
ref or index. The path is left ` M` with bytes identical to origin's, and git
refuses a fast-forward over a modified path without comparing content -- so
this Mac's explorer was blocked by its own pushed commit for 70-280 minutes at
a time (evidence/planning/autopull_index_fossil_selfheal_staged_20260920.md).

`_pull_repo`'s dirty branch now shells out to the umbrella repo's
`scripts/ff_fossil_reconcile.py`. serve.py must never IMPORT that module (it
lives in another repo), and a box without the umbrella must behave exactly as
before. So what is pinned here is mostly what must NOT change:

  * helper absent / timed out / crashed / garbage output / NOT_APPLICABLE
        -> the printed line is BYTE-IDENTICAL to the pre-wiring line,
           `stuck_since` keeps counting, the repo is untouched;
  * UNPROVEN -> same skip, same `stuck_since`, plus the helper's path names;
  * a helper that CLAIMS RECONCILED while git still says "behind"
        -> not believed (two independent signals are required);
  * local commits ahead -> the helper is not even invoked.

The positive case runs the REAL helper when the umbrella checkout is present
(it is on every dev box; REE_assembly's own CI has no umbrella, so it skips
there) against a real repo + real filesystem remote.
"""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
REAL_HELPER = ROOT.parent / "scripts" / "ff_fossil_reconcile.py"

GIT_ENV = dict(
    os.environ,
    GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid",
    GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.invalid",
    GIT_CONFIG_NOSYSTEM="1",
)


def load_serve():
    """Import REE_assembly/serve.py under its own name (see sibling tests)."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("serve", ROOT / "serve.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def serve():
    return load_serve()


def git(cwd, *args):
    r = subprocess.run(["git", "-C", str(cwd)] + list(args), env=GIT_ENV,
                       capture_output=True, text=True)
    assert r.returncode == 0, "git %s failed: %s" % (" ".join(args), r.stderr)
    return r.stdout.strip()


@pytest.fixture
def world(tmp_path):
    """A bare remote, the checkout under test (`box`), and a second clone
    (`other`) that lands commits on the remote the way another machine would.
    `log.md` and `data.json` both exist at the shared base."""
    remote = tmp_path / "remote.git"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "master", str(remote)],
                   env=GIT_ENV, check=True)
    other = tmp_path / "other"
    subprocess.run(["git", "clone", "-q", str(remote), str(other)],
                   env=GIT_ENV, check=True, capture_output=True)
    git(other, "checkout", "-q", "-b", "master")
    (other / "log.md").write_text("l1\n")
    (other / "data.json").write_text("{}\n")
    git(other, "add", "log.md", "data.json")
    git(other, "commit", "-q", "-m", "base")
    git(other, "push", "-q", "origin", "master")
    box = tmp_path / "box"
    subprocess.run(["git", "clone", "-q", str(remote), str(box)],
                   env=GIT_ENV, check=True, capture_output=True)
    return {"remote": remote, "other": other, "box": box, "tmp": tmp_path}


def land_upstream(world, path, content, msg="upstream"):
    other = world["other"]
    (other / path).write_text(content)
    git(other, "add", path)
    git(other, "commit", "-q", "-m", msg)
    git(other, "push", "-q", "origin", "master")
    return git(other, "rev-parse", "HEAD")


def snapshot(box):
    """Everything a wrong reconcile could disturb."""
    return {
        "head": git(box, "rev-parse", "HEAD"),
        "index": git(box, "ls-files", "-s"),
        "status": git(box, "status", "--porcelain"),
        "bytes": {p.name: p.read_bytes() for p in sorted(box.iterdir())
                  if p.is_file()},
    }


def stub_helper(tmp, body):
    """A stand-in helper. `body` is python run with the real argv."""
    p = tmp / "stub_helper.py"
    p.write_text("import json, sys, time\n" + textwrap.dedent(body))
    return p


def today_line(name, behind, blocker):
    """The line _pull_repo printed for this shape BEFORE the wiring."""
    return ("[serve] git pull %s: behind %s, NOT diverged -- uncommitted "
            "paths block ff; skipping. blocked by: %s" % (name, behind, blocker))


# --------------------------------------------------------------------------- #
# Negative controls: nothing changes unless the helper PROVES a fossil.        #
# --------------------------------------------------------------------------- #

def test_missing_helper_prints_todays_line_byte_identical(serve, world, monkeypatch, capsys):
    box = world["box"]
    land_upstream(world, "log.md", "l1\nl2\n")
    (box / "log.md").write_text("l1\nl2\n")            # a genuine fossil...
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(world["tmp"] / "absent.py"))
    before = snapshot(box)
    stuck = {}
    serve._pull_repo(box, stuck)
    out = capsys.readouterr().out.strip()
    assert out == today_line("box", 1, "log.md")       # ...but no umbrella here
    assert "box" in stuck
    after = snapshot(box)
    assert after == before


@pytest.mark.parametrize("body", [
    "time.sleep(30)\n",                                           # timeout
    "sys.exit(7)\n",                                              # crash, no output
    "print('not json at all')\n",                                 # garbage
    "print(json.dumps(['a', 'list']))\n",                         # wrong JSON shape
    "print(json.dumps({'verdict': 'NOT_APPLICABLE', 'fossils': [], 'unproven': []}))\nsys.exit(4)\n",
    "print(json.dumps({'verdict': 'FF_REFUSED', 'fossils': ['log.md'], 'unproven': []}))\nsys.exit(5)\n",
    "print(json.dumps({'verdict': 'NO_OVERLAP', 'fossils': [], 'unproven': []}))\nsys.exit(4)\n",
], ids=["timeout", "crash", "garbage", "wrong-shape", "not-applicable",
        "ff-refused", "no-overlap"])
def test_every_non_proof_outcome_is_todays_line_unchanged(serve, world, monkeypatch, capsys, body):
    box = world["box"]
    land_upstream(world, "log.md", "l1\nl2\n")
    (box / "log.md").write_text("l1\nl2\n")
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(stub_helper(world["tmp"], body)))
    monkeypatch.setattr(serve, "_FF_FOSSIL_TIMEOUT_S", 2)
    before = snapshot(box)
    stuck = {}
    serve._pull_repo(box, stuck)
    assert capsys.readouterr().out.strip() == today_line("box", 1, "log.md")
    assert "box" in stuck
    assert snapshot(box) == before


def test_claimed_reconciled_is_not_believed_while_git_says_behind(serve, world, monkeypatch, capsys):
    """A helper verdict alone never clears stuck_since -- git must agree."""
    box = world["box"]
    land_upstream(world, "log.md", "l1\nl2\n")
    (box / "log.md").write_text("l1\nl2\n")
    liar = stub_helper(world["tmp"],
                       "print(json.dumps({'verdict': 'RECONCILED', 'fossils': ['log.md'], 'unproven': []}))\n")
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(liar))
    before = snapshot(box)
    stuck = {}
    serve._pull_repo(box, stuck)
    assert capsys.readouterr().out.strip() == today_line("box", 1, "log.md")
    assert "box" in stuck
    assert snapshot(box) == before


def test_unproven_still_skips_and_names_the_genuinely_dirty_path(serve, world, monkeypatch, capsys):
    box = world["box"]
    land_upstream(world, "log.md", "l1\nl2\n")
    (box / "log.md").write_text("l1\nLIVE EDIT\n")
    stub = stub_helper(world["tmp"], """\
        print(json.dumps({'verdict': 'UNPROVEN', 'fossils': [],
              'unproven': [{'path': 'log.md', 'status': ' M', 'why': 'differs'}]}))
        sys.exit(3)
        """)
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(stub))
    before = snapshot(box)
    stuck = {}
    serve._pull_repo(box, stuck)
    out = capsys.readouterr().out.strip()
    assert out.startswith(today_line("box", 1, "log.md"))
    assert "NOT a fossil (genuinely dirty): log.md" in out
    assert "box" in stuck
    assert snapshot(box) == before


def test_helper_is_not_invoked_when_local_commits_are_ahead(serve, world, monkeypatch, capsys):
    box = world["box"]
    land_upstream(world, "log.md", "l1\nl2\n")
    (box / "data.json").write_text('{"local": 1}\n')
    git(box, "add", "data.json")
    git(box, "commit", "-q", "-m", "local commit")
    (box / "log.md").write_text("l1\nl2\n")
    marker = world["tmp"] / "helper_was_called"
    stub = stub_helper(world["tmp"], "open(%r, 'w').close()\n" % str(marker))
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(stub))
    before = snapshot(box)
    stuck = {}
    serve._pull_repo(box, stuck)
    out = capsys.readouterr().out
    assert "diverged + local changes" in out
    assert not marker.exists()
    assert "box" in stuck
    assert snapshot(box) == before


def test_ordinary_pull_is_unaffected_and_clears_stuck_since(serve, world, monkeypatch, capsys):
    box = world["box"]
    tip = land_upstream(world, "data.json", '{"v": 2}\n')
    (box / "log.md").write_text("l1\nunrelated live edit\n")   # dirty, no overlap
    marker = world["tmp"] / "helper_was_called"
    stub = stub_helper(world["tmp"], "open(%r, 'w').close()\n" % str(marker))
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(stub))
    stuck = {"box": 0.0}
    serve._pull_repo(box, stuck)
    assert git(box, "rev-parse", "HEAD") == tip
    assert stuck == {}
    assert not marker.exists()
    assert (box / "log.md").read_text() == "l1\nunrelated live edit\n"


# --------------------------------------------------------------------------- #
# The real helper, end to end (skips where the umbrella is not checked out).   #
# --------------------------------------------------------------------------- #

needs_umbrella = pytest.mark.skipif(
    not REAL_HELPER.is_file(),
    reason="umbrella scripts/ff_fossil_reconcile.py not present on this box")


@needs_umbrella
def test_real_fossil_is_reconciled_and_clears_stuck_since(serve, world, monkeypatch, capsys):
    box = world["box"]
    tip = land_upstream(world, "log.md", "l1\nl2\n")
    (box / "log.md").write_text("l1\nl2\n")
    (box / "data.json").write_text('{"workset": "regen"}\n')   # dirty, NOT incoming
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(REAL_HELPER))
    log_before = (box / "log.md").stat().st_mtime_ns
    stuck = {"box": 0.0}
    serve._pull_repo(box, stuck)
    out = capsys.readouterr().out
    assert "over index fossil(s) [log.md]" in out
    assert git(box, "rev-parse", "HEAD") == tip
    assert stuck == {}
    # no fossil byte was written, and unrelated dirt is exactly where it was
    assert (box / "log.md").stat().st_mtime_ns == log_before
    assert git(box, "status", "--porcelain") == "M data.json"
    assert (box / "data.json").read_text() == '{"workset": "regen"}\n'


@needs_umbrella
def test_real_genuinely_dirty_overlap_is_left_alone(serve, world, monkeypatch, capsys):
    box = world["box"]
    land_upstream(world, "log.md", "l1\nl2\n")
    (box / "log.md").write_text("l1\nMY UNCOMMITTED LINE\n")
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(REAL_HELPER))
    before = snapshot(box)
    stuck = {}
    serve._pull_repo(box, stuck)
    out = capsys.readouterr().out.strip()
    assert out.startswith(today_line("box", 1, "log.md"))
    assert "NOT a fossil (genuinely dirty): log.md" in out
    assert "box" in stuck
    assert snapshot(box) == before


@needs_umbrella
def test_real_fossil_plus_genuine_dirt_reconciles_nothing(serve, world, monkeypatch, capsys):
    """Partial proof is not proof: a provable fossil is left alone too."""
    box = world["box"]
    other = world["other"]
    (other / "log.md").write_text("l1\nl2\n")
    (other / "data.json").write_text('{"v": 2}\n')
    git(other, "add", "log.md", "data.json")
    git(other, "commit", "-q", "-m", "both")
    git(other, "push", "-q", "origin", "master")
    (box / "log.md").write_text("l1\nl2\n")                    # fossil
    (box / "data.json").write_text('{"mine": true}\n')          # genuinely dirty
    monkeypatch.setenv(serve._FF_FOSSIL_HELPER_ENV, str(REAL_HELPER))
    before = snapshot(box)
    stuck = {}
    serve._pull_repo(box, stuck)
    out = capsys.readouterr().out
    assert "NOT a fossil (genuinely dirty): data.json" in out
    assert "provable fossil(s) left alone" in out and "log.md" in out
    assert "box" in stuck
    assert snapshot(box) == before


def test_serve_does_not_import_the_umbrella_helper(serve):
    """Shell-out only. A cross-repo import works on this Mac and breaks on
    every box that has REE_assembly without the umbrella."""
    src = (ROOT / "serve.py").read_text(encoding="utf-8")
    assert "import ff_fossil_reconcile" not in src
    assert "ff_fossil_reconcile" not in sys.modules
