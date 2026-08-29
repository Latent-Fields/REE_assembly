#!/usr/bin/env python3
"""Contract tests for the Steward daily T0 auto-fix sweep.

Run from REE_assembly/ root:
    /opt/local/bin/python3 -m pytest scripts/steward/test_steward_sweep.py -q

WHAT IS BEING PINNED
=====================================================================
This is the project's only SCHEDULED, UNATTENDED WRITER to evidence/planning/ --
a shared, multi-writer tree. What makes that acceptable is not the sweep's
intent but its four gates, and every one of them is asserted here:

  * it commits through scripts/ree_commit.py and never plain git (proved by the
    intent record ree_commit writes, which is the same artefact the pre-push
    hook checks -- not by reading the source for the string "ree_commit");
  * it commits ONLY the paths a T0 fixer reports having written, plus its own
    ledger -- an unrelated dirty file in the tree must survive untouched;
  * it authors AND commits as the bot identity, so it can never assert an
    off-duty attestation on the operator's behalf;
  * it aborts on a moving ref, on a detached HEAD, and on invalid plan
    frontmatter, and an abort leaves the tree byte-identical.

Roughly half of these are negative controls, and that is the point: every gate
is a refusal, so a bug in one is SILENT -- the sweep just commits something it
should not have, once a day, unattended. The tests that assert "nothing
happened" are the ones that matter most.

Real git repos in a tmpdir. Time-independent: no sleeps, no wall-clock
dependence, no network.
"""

from __future__ import annotations

import json
import os
import plistlib
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

_STEWARD = Path(__file__).resolve().parent
if str(_STEWARD) not in sys.path:
    sys.path.insert(0, str(_STEWARD))

import steward_sweep as sw  # noqa: E402
from detectors import _gitlane as G  # noqa: E402

_REPO_ROOT = _STEWARD.parents[1]                  # REE_assembly/


def _find_ree_commit() -> Path:
    """Locate the umbrella's scripts/ree_commit.py.

    The ordinary derivation (REE_assembly/../scripts/ree_commit.py) is what the
    sweep itself uses and is correct in the deployed layout. It is WRONG in a
    detached `git worktree` of REE_assembly, which is where this suite is
    routinely run from on a divergent checkout -- there the worktree's parent is
    a scratch directory, not REE_Working. Falling through to `skip` in that case
    would leave a 21-test suite silently proving nothing, so the worktree's
    common git dir is used to find the main checkout, and the umbrella from
    there.
    """
    env = os.environ.get("REE_COMMIT")
    if env and Path(env).exists():
        return Path(env).resolve()
    direct = _REPO_ROOT.parent / "scripts" / "ree_commit.py"
    if direct.exists():
        return direct
    proc = subprocess.run(
        ["git", "-C", str(_REPO_ROOT), "rev-parse", "--path-format=absolute",
         "--git-common-dir"], capture_output=True, text=True)
    if proc.returncode == 0:
        common = Path(proc.stdout.strip())          # <main checkout>/.git
        candidate = common.parent.parent / "scripts" / "ree_commit.py"
        if candidate.exists():
            return candidate.resolve()
    return direct                                   # non-existent -> skip


_REE_COMMIT = _find_ree_commit()

BOT_NAME = "REE Automation (Mac)"
BOT_EMAIL = "nooarche@users.noreply.github.com"

pytestmark = pytest.mark.skipif(
    not _REE_COMMIT.exists(),
    reason="ree_commit.py not present; the sweep's commit gate cannot be exercised")


# ---------------------------------------------------------------------------
# fixture helpers
# ---------------------------------------------------------------------------

def git(repo: Path, *args: str) -> str:
    p = subprocess.run(["git", "-C", str(repo), *args],
                       capture_output=True, text=True)
    assert p.returncode == 0, "git %s failed: %s" % (" ".join(args), p.stderr)
    return p.stdout


def plan_text(plan_date: str, node_date: str) -> str:
    """A plan whose frontmatter date TRAILS its newest node date -> D-008 fires."""
    fm = {"closure_plan": {
        "id": "alpha", "title": "Alpha", "generation": "v3",
        "last_updated": plan_date,
        "nodes": [{"id": "alpha:1", "title": "One", "status": "done",
                   "last_updated": node_date}]}}
    return "---\n" + yaml.safe_dump(fm, sort_keys=False) + "\n---\n\n# Alpha\n"


def make_repo(root: Path, drifted: bool = True, with_checker: bool = False,
              broken_plan: bool = False) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    (root / "docs" / "claims").mkdir(parents=True, exist_ok=True)
    (root / "evidence" / "planning").mkdir(parents=True, exist_ok=True)
    (root / "scripts").mkdir(parents=True, exist_ok=True)
    (root / "docs" / "claims" / "claims.yaml").write_text("[]\n", encoding="utf-8")
    (root / "evidence" / "planning" / "alpha_plan.md").write_text(
        plan_text("2026-06-01" if drifted else "2026-07-01", "2026-07-01"),
        encoding="utf-8")
    if broken_plan:
        # An UNQUOTED prose scalar containing ': ' -- the 2026-06-19 incident
        # shape check_plan_frontmatter.py exists for.
        (root / "evidence" / "planning" / "broken_plan.md").write_text(
            "---\nclosure_plan:\n  id: broken\n  owner_exq: the fix worked: OFC bias\n"
            "  nodes:\n    - id: broken:1\n      status: open\n---\n\n# Broken\n",
            encoding="utf-8")
    if with_checker:
        # The REAL checker, not a stub -- the gate under test is its --strict exit.
        (root / "scripts" / "check_plan_frontmatter.py").write_text(
            (_REPO_ROOT / "scripts" / "check_plan_frontmatter.py")
            .read_text(encoding="utf-8"), encoding="utf-8")

    git(root, "init", "-q", "-b", "master")
    git(root, "config", "user.name", "Fixture")
    git(root, "config", "user.email", "fixture@example.invalid")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "base")
    return root


def sweep(repo: Path, monkeypatch, push: bool = False, dry_run: bool = False) -> int:
    monkeypatch.setenv("REE_COMMIT", str(_REE_COMMIT))
    return sw.sweep(repo, push=push, dry_run=dry_run)


def head(repo: Path) -> str:
    return git(repo, "rev-parse", "HEAD").strip()


def ledger_records(repo: Path) -> list[dict]:
    p = repo / sw.LEDGER_REL
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def sweep_records(repo: Path) -> list[dict]:
    return [r for r in ledger_records(repo) if r.get("source") == "steward_sweep"]


def plan_bytes(repo: Path) -> bytes:
    return (repo / "evidence" / "planning" / "alpha_plan.md").read_bytes()


# ---------------------------------------------------------------------------
# the commit gate -- ree_commit.py, never plain git
# ---------------------------------------------------------------------------

def test_sweep_commits_through_ree_commit_not_plain_git(tmp_path, monkeypatch):
    """THE ITEM-2b CONTRACT.

    Proved by the artefact rather than by reading the source: ree_commit.py
    writes <gitdir>/ree_commit_intent/<sha>.json for the commit it builds, and
    that record is exactly what the pre-push hook looks for when it warns
    "touches managed path(s) ... but was not built by ree_commit.py
    (race-prone idiom)" -- the warning the 2026-08-16 D-008 fix drew.
    """
    repo = make_repo(tmp_path / "r")
    before = head(repo)
    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    after = head(repo)
    assert after != before, "the sweep did not commit"
    intent = repo / ".git" / "ree_commit_intent" / ("%s.json" % after)
    assert intent.exists(), \
        "no ree_commit intent record -- this commit was built the race-prone way"
    declared = json.loads(intent.read_text(encoding="utf-8"))
    assert "evidence/planning/alpha_plan.md" in json.dumps(declared)


def test_commit_invokes_ree_commit_with_bot_and_declared_paths(tmp_path, monkeypatch):
    """Pin the argv itself: --bot present, paths after a bare --, push honoured."""
    seen = {}

    def fake_run(cmd, **kw):
        seen["cmd"] = list(cmd)
        return subprocess.CompletedProcess(cmd, 0, "ok", "")

    monkeypatch.setattr(sw.subprocess, "run", fake_run)
    monkeypatch.setenv("REE_COMMIT", str(_REE_COMMIT))
    ok, _ = sw.commit(tmp_path, ["a.md", "b.md"], "msg", push=True)
    assert ok
    cmd = seen["cmd"]
    assert cmd[1].endswith("ree_commit.py"), "the sweep must not shell out to git"
    assert "--bot" in cmd
    assert "--push" in cmd
    assert cmd[cmd.index("--") + 1:] == ["a.md", "b.md"]


def test_commit_without_push_does_not_pass_push(tmp_path, monkeypatch):
    seen = {}

    def fake_run(cmd, **kw):
        seen["cmd"] = list(cmd)
        return subprocess.CompletedProcess(cmd, 0, "ok", "")

    monkeypatch.setattr(sw.subprocess, "run", fake_run)
    monkeypatch.setenv("REE_COMMIT", str(_REE_COMMIT))
    sw.commit(tmp_path, ["a.md"], "msg", push=False)
    assert "--push" not in seen["cmd"]


def test_sweep_commits_as_the_bot_identity(tmp_path, monkeypatch):
    """Author AND committer.

    An unattended job must never commit under the operator's personal identity:
    clinical_hours_guard.py treats a personal-identity commit as an assertion
    that the work was done off clinical duty, and a scheduled job cannot make
    that assertion. It is also what lets the push-side bot exemption apply.
    """
    repo = make_repo(tmp_path / "r")
    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    an, ae, cn, ce = git(repo, "log", "-1", "--format=%an%n%ae%n%cn%n%ce").splitlines()
    assert (an, ae) == (BOT_NAME, BOT_EMAIL)
    assert (cn, ce) == (BOT_NAME, BOT_EMAIL)


# ---------------------------------------------------------------------------
# scope -- T0 paths and the ledger, nothing else
# ---------------------------------------------------------------------------

def test_sweep_commits_only_t0_paths_and_its_own_ledger(tmp_path, monkeypatch):
    """NEGATIVE CONTROL: an unrelated dirty file must survive the sweep.

    This is the failure that would be invisible: a scheduled writer that swept
    another session's in-flight edit into its own commit, daily, under a message
    saying "T0 repairs". CLAUDE.md's whole read-modify-write section is about
    this shape.
    """
    repo = make_repo(tmp_path / "r")
    bystander = repo / "docs" / "claims" / "claims.yaml"
    bystander.write_text("- id: SOMEONE-ELSE-WIP\n", encoding="utf-8")

    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    committed = set(git(repo, "show", "--name-only", "--format=", "HEAD").split())
    assert committed <= {"evidence/planning/alpha_plan.md", sw.LEDGER_REL}, \
        "the sweep committed a path no T0 fixer wrote: %s" % committed
    assert "docs/claims/claims.yaml" not in committed
    assert bystander.read_text(encoding="utf-8") == "- id: SOMEONE-ELSE-WIP\n"
    assert git(repo, "status", "--porcelain", "docs/claims/claims.yaml").strip()


def test_sweep_refuses_a_target_another_session_has_open(tmp_path, monkeypatch):
    """apply_fixes' dirty-path guard, exercised end to end.

    Refusing is free; the fix is still there next run. Writing is not free.
    """
    repo = make_repo(tmp_path / "r")
    p = repo / "evidence" / "planning" / "alpha_plan.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n<!-- in-flight edit -->\n",
                 encoding="utf-8")
    dirty_before = p.read_bytes()
    before = head(repo)

    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    assert head(repo) == before, "committed despite the target being dirty"
    assert p.read_bytes() == dirty_before, "overwrote an in-flight edit"
    assert sweep_records(repo)[-1]["applied"] == 0


# ---------------------------------------------------------------------------
# the gates -- every one of these must leave the tree untouched
# ---------------------------------------------------------------------------

def test_sweep_aborts_when_a_pinned_ref_moves(tmp_path, monkeypatch):
    """The D-102 gate. Nothing may be written -- the preview precedes the guard."""
    repo = make_repo(tmp_path / "r")
    before, bytes_before = head(repo), plan_bytes(repo)

    def moved(_repo, _expected):
        raise G.RefMoved([("master", "a" * 40, "b" * 40)])

    monkeypatch.setattr(sw, "guard", moved)
    assert sweep(repo, monkeypatch) == sw.EXIT_ABORTED
    assert head(repo) == before
    assert plan_bytes(repo) == bytes_before, \
        "wrote before the ref guard ran -- preview must precede apply"
    assert sweep_records(repo)[-1]["aborted"] == "ref_moved"


def test_sweep_refuses_on_a_detached_head(tmp_path, monkeypatch):
    """No branch to pin means the mandatory gate cannot run -> refuse, not proceed."""
    repo = make_repo(tmp_path / "r")
    git(repo, "checkout", "-q", "--detach")
    before, bytes_before = head(repo), plan_bytes(repo)
    assert sweep(repo, monkeypatch) == sw.EXIT_ABORTED
    assert head(repo) == before and plan_bytes(repo) == bytes_before
    assert sweep_records(repo)[-1]["aborted"] == "no_ref_to_pin"


def test_sweep_refuses_outside_a_git_repo(tmp_path, monkeypatch):
    root = tmp_path / "notrepo"
    (root / "evidence" / "planning").mkdir(parents=True)
    assert sweep(root, monkeypatch) == sw.EXIT_ABORTED
    assert sweep_records(root)[-1]["aborted"] == "not_a_git_repo"


def test_sweep_aborts_on_invalid_frontmatter_and_reverts(tmp_path, monkeypatch):
    """The strict-parse gate, with the REAL checker and a real broken plan.

    The revert is the delicate part: it must restore exactly the paths the sweep
    wrote and nothing else. Safe only because apply_fixes refuses a dirty target,
    so every applied path was provably clean beforehand.
    """
    repo = make_repo(tmp_path / "r", with_checker=True, broken_plan=True)
    before, bytes_before = head(repo), plan_bytes(repo)

    assert sweep(repo, monkeypatch) == sw.EXIT_ABORTED
    assert head(repo) == before, "committed on top of unparseable plan frontmatter"
    assert plan_bytes(repo) == bytes_before, "applied edit was not reverted"
    rec = sweep_records(repo)[-1]
    assert rec["aborted"] == "frontmatter_invalid"
    assert rec["reverted"] == ["evidence/planning/alpha_plan.md"]


def test_valid_frontmatter_passes_the_gate(tmp_path, monkeypatch):
    """NEGATIVE CONTROL: the checker must not block an ordinary sweep."""
    repo = make_repo(tmp_path / "r", with_checker=True)
    base = head(repo)
    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    assert head(repo) != base, "the gate blocked a valid sweep"
    assert git(repo, "rev-parse", "HEAD^").strip() == base
    assert sweep_records(repo)[-1]["applied"] == 1


def test_absent_checker_is_reported_not_silently_passed(tmp_path):
    ok, detail = sw.validate_frontmatter(tmp_path)
    assert ok and "validation skipped" in detail


# ---------------------------------------------------------------------------
# the ledger -- one autofix record per run, always
# ---------------------------------------------------------------------------

def test_every_run_appends_exactly_one_sweep_record(tmp_path, monkeypatch):
    repo = make_repo(tmp_path / "r")
    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    assert len(sweep_records(repo)) == 1
    # second run: nothing left to fix, but the run is still recorded
    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    recs = sweep_records(repo)
    assert len(recs) == 2
    assert all(r["action"] == "autofix" for r in recs)
    assert recs[1]["applied"] == 0


def test_the_sweep_record_carries_its_base_so_the_commit_is_findable(tmp_path, monkeypatch):
    """The record lands IN the commit, so it cannot carry the resulting sha.

    It carries `base` instead, and the commit is that base's child.
    """
    repo = make_repo(tmp_path / "r")
    base = head(repo)
    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    rec = sweep_records(repo)[-1]
    assert rec["base"] == base
    assert rec["committed"] is True
    assert git(repo, "rev-parse", "HEAD^").strip() == base


def test_nothing_to_fix_does_not_commit(tmp_path, monkeypatch):
    repo = make_repo(tmp_path / "r", drifted=False)
    before = head(repo)
    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    assert head(repo) == before
    assert sweep_records(repo)[-1]["committed"] is False


def test_dry_run_writes_nothing_at_all(tmp_path, monkeypatch):
    """No plan edit, no commit, and no ledger line -- a preview must not ratchet."""
    repo = make_repo(tmp_path / "r")
    before, bytes_before = head(repo), plan_bytes(repo)
    assert sweep(repo, monkeypatch, dry_run=True) == sw.EXIT_OK
    assert head(repo) == before
    assert plan_bytes(repo) == bytes_before
    assert sweep_records(repo) == []
    assert git(repo, "status", "--porcelain").strip() == ""


# ---------------------------------------------------------------------------
# the ledger never stays dirty, even when the commit fails (2026-08-29
# fleet-wedge hardening, chip-20260829-steward-sweep-dirty-exit-hardening)
# ---------------------------------------------------------------------------

_BOGUS_REE_COMMIT = "/nonexistent/path/does_not_exist_ree_commit.py"


def _fake_pending_record() -> dict:
    """A record shaped like one `stash_pending` would actually write."""
    return {"action": "autofix", "source": "steward_sweep",
            "ts": "2026-01-01T00:00:00Z", "repo": "irrelevant",
            "dry_run": False, "applied": 1, "committed": False,
            "error": "simulated earlier commit failure"}


def test_commit_failure_with_nothing_landed_reverts_ledger_and_stashes_pending(
        tmp_path, monkeypatch):
    """THE CORE CONTRACT: a commit failure that lands nothing locally must
    leave the ledger byte-identical to before this run touched it, with the
    record it would have carried moved to the pending file instead.
    """
    repo = make_repo(tmp_path / "r")
    monkeypatch.setenv("REE_COMMIT", _BOGUS_REE_COMMIT)

    assert sw.sweep(repo, push=False, dry_run=False) == sw.EXIT_ERROR
    assert git(repo, "status", "--porcelain", sw.LEDGER_REL).strip() == "", \
        "the ledger append must not be left as a dirty diff"
    assert not (repo / sw.LEDGER_REL).exists(), \
        "the ledger never existed before this run -- it must not exist after either"

    pending = sw.pending_records(repo)
    assert len(pending) == 1
    assert pending[0]["committed"] is False
    assert pending[0]["applied"] == 1
    assert "ree_commit.py not found" in pending[0]["error"]


def test_commit_failure_that_lands_locally_leaves_the_ledger_alone(tmp_path, monkeypatch):
    """Simulates a rejected-but-unretryable PUSH: ree_commit.py's update-ref
    still lands a real local commit before the push fails, so `commit()`
    reports failure even though HEAD advanced. The ledger append is already
    safely inside that commit -- it must not be touched, and nothing goes
    to the pending file (there is nothing left to recover).
    """
    repo = make_repo(tmp_path / "r")

    def fake_commit(repo_root, paths, message, push):
        git(repo_root, "add", "--", *paths)
        git(repo_root, "-c", "user.name=Fixture", "-c",
            "user.email=fixture@example.invalid", "commit", "-q", "-m", message)
        return False, "push rejected (simulated)"

    monkeypatch.setattr(sw, "commit", fake_commit)
    before = head(repo)

    assert sw.sweep(repo, push=True, dry_run=False) == sw.EXIT_ERROR
    assert head(repo) != before, "the simulated local commit should have landed"
    assert git(repo, "status", "--porcelain", sw.LEDGER_REL).strip() == "", \
        "content already committed locally is not a dirty diff"
    assert sw.pending_records(repo) == [], \
        "nothing should be pending -- the append already landed in git history"


def test_flush_pending_lands_a_stranded_record_and_clears_the_file(tmp_path, monkeypatch):
    repo = make_repo(tmp_path / "r")
    monkeypatch.setenv("REE_COMMIT", str(_REE_COMMIT))
    rec = _fake_pending_record()
    sw.stash_pending(repo, rec)
    before = head(repo)

    sw.flush_pending(repo, push=False)

    assert sw.pending_records(repo) == []
    assert head(repo) != before, "the stranded record should now be committed"
    assert git(repo, "status", "--porcelain", sw.LEDGER_REL).strip() == ""
    assert any(r.get("error") == rec["error"] for r in ledger_records(repo))


def test_flush_pending_leaves_no_dirty_diff_when_it_fails_again(tmp_path, monkeypatch):
    """NEGATIVE CONTROL: a flush that still cannot land must not itself create
    a new dirty diff, and the stashed record must survive untouched for the
    next retry -- never lost, never duplicated.
    """
    repo = make_repo(tmp_path / "r")
    monkeypatch.setenv("REE_COMMIT", _BOGUS_REE_COMMIT)
    rec = _fake_pending_record()
    sw.stash_pending(repo, rec)
    before = head(repo)

    sw.flush_pending(repo, push=False)

    assert head(repo) == before, "nothing should have committed"
    assert git(repo, "status", "--porcelain", sw.LEDGER_REL).strip() == "", \
        "a failed flush must not leave the ledger dirty either"
    assert sw.pending_records(repo) == [rec]


def test_flush_pending_is_a_noop_with_nothing_pending(tmp_path, monkeypatch):
    repo = make_repo(tmp_path / "r")
    monkeypatch.setenv("REE_COMMIT", str(_REE_COMMIT))
    before = head(repo)

    sw.flush_pending(repo, push=False)

    assert head(repo) == before
    assert git(repo, "status", "--porcelain").strip() == ""


def test_sweep_flushes_pending_before_its_own_gates(tmp_path, monkeypatch):
    """Integration: an ordinary sweep run lands a PRIOR run's stranded record,
    on top of doing its own work, with nothing left pending afterward.
    """
    repo = make_repo(tmp_path / "r")
    monkeypatch.setenv("REE_COMMIT", str(_REE_COMMIT))
    rec = _fake_pending_record()
    sw.stash_pending(repo, rec)

    assert sweep(repo, monkeypatch) == sw.EXIT_OK
    assert sw.pending_records(repo) == []
    assert any(r.get("error") == rec["error"] for r in ledger_records(repo))


def test_dry_run_does_not_flush_pending(tmp_path, monkeypatch):
    """A preview run must not mutate the pending file or commit anything,
    exactly like it must not touch anything else (test_dry_run_writes_nothing_at_all).
    """
    repo = make_repo(tmp_path / "r")
    monkeypatch.setenv("REE_COMMIT", str(_REE_COMMIT))
    rec = _fake_pending_record()
    sw.stash_pending(repo, rec)
    before = head(repo)

    assert sweep(repo, monkeypatch, dry_run=True) == sw.EXIT_OK
    assert head(repo) == before
    assert sw.pending_records(repo) == [rec]
    assert git(repo, "status", "--porcelain", sw.LEDGER_REL).strip() == ""


def test_pending_records_skips_corrupt_lines(tmp_path):
    """A mangled pending file must not wedge every future flush attempt."""
    repo = tmp_path / "r"
    path = repo / sw.PENDING_LEDGER_REL
    path.parent.mkdir(parents=True)
    path.write_text('not json\n{"a": 1}\n\n', encoding="utf-8")
    assert sw.pending_records(repo) == [{"a": 1}]


# ---------------------------------------------------------------------------
# wiring -- the plist, the installer, and governance staying read-only
# ---------------------------------------------------------------------------

def test_plist_parses_and_is_a_daily_agent():
    d = plistlib.loads((_STEWARD / "com.ree.steward.plist").read_bytes())
    assert d["Label"] == "com.ree.steward"
    assert d["StartInterval"] == 86400, "the decision was DAILY"
    assert d["ProgramArguments"][-1].endswith("scripts/steward/steward_sweep.py")
    assert d["ProgramArguments"][0].endswith("python3")


def test_plist_comment_has_no_double_hyphen():
    """An XML comment may not contain '--'; one makes the whole plist unparseable.

    Easy to reintroduce, because the natural thing to write about this job is
    the name of the flag it passes.
    """
    text = (_STEWARD / "com.ree.steward.plist").read_text(encoding="utf-8")
    comment = text[text.index("<!--") + 4:text.index("-->")]
    assert "--" not in comment


def test_installer_installs_this_plist_and_this_sweep():
    sh = (_STEWARD / "install_steward_sweep.sh").read_text(encoding="utf-8")
    assert "com.ree.steward.plist" in sh
    assert "steward_sweep.py" in sh
    assert "launchctl bootout" in sh and "launchctl bootstrap" in sh, \
        "launchd caches the loaded plist; an edit is a silent no-op without both"
    assert "--dry-run" in sh, "prove the sweep runs before scheduling it"


def test_governance_does_not_call_the_sweep():
    """NEGATIVE CONTROL, and the decision this whole change rests on.

    governance.sh stays READ-ONLY. If a later session 'simplifies' by calling the
    sweep from the pipeline, it reintroduces both problems the separate job was
    chosen to avoid: a governance regen that writes, and a fix at Step 3m that
    leaves Step 3c-bis's freshly-regenerated closure snapshot stale.
    """
    gov = (_REPO_ROOT / "scripts" / "governance.sh").read_text(encoding="utf-8")
    assert "steward_sweep" not in gov
    assert "com.ree.steward" not in gov
    # The other half of the decision -- that Step 3m itself passes no --fix --
    # is owned by test_governance_wiring.test_no_fix_flag, which tokenises it
    # correctly. governance.sh's comment block DISCUSSES --fix at length, so a
    # naive substring check here would fail on the prose that explains the rule.


def test_sweep_never_invokes_git_commit_and_never_checks_out_broadly(
        tmp_path, monkeypatch):
    """BEHAVIOURAL, not a source grep.

    Records every subprocess the sweep module itself launches during a real
    end-to-end run and asserts two things about them: no `git commit` (ITEM 2b
    -- the commit must go through ree_commit.py) and no unscoped `git checkout`
    (a broad restore would discard other sessions' uncommitted work, the hazard
    CLAUDE.md's narrow-restore rule exists for).

    An earlier version of this test grepped the module source and failed on its
    own docstring, which warns against exactly the string it was grepping for.
    """
    repo = make_repo(tmp_path / "r")
    real_run = subprocess.run
    seen: list[list[str]] = []

    def recording_run(cmd, **kw):
        seen.append([str(c) for c in cmd])
        return real_run(cmd, **kw)

    monkeypatch.setattr(sw.subprocess, "run", recording_run)
    assert sweep(repo, monkeypatch) == sw.EXIT_OK

    gits = [c for c in seen if Path(c[0]).name == "git"]
    assert not [c for c in gits if "commit" in c], \
        "the sweep shelled out to git commit: %s" % gits
    for c in gits:
        if "checkout" in c:
            assert "--" in c and c[c.index("--") + 1:], \
                "unscoped git checkout: %s" % c
            assert "." not in c[c.index("--") + 1:], \
                "broad `git checkout -- .`: %s" % c
    assert any(Path(c[1]).name == "ree_commit.py"
               for c in seen if len(c) > 1), "ree_commit.py was never invoked"


def test_revert_is_path_scoped(tmp_path, monkeypatch):
    """NEGATIVE CONTROL on the one destructive-shaped call the sweep can make."""
    seen = {}

    def fake_run(cmd, **kw):
        seen["cmd"] = [str(c) for c in cmd]
        return subprocess.CompletedProcess(cmd, 0, "", "")

    monkeypatch.setattr(sw.subprocess, "run", fake_run)
    sw.revert(tmp_path, ["a.md", "b.md"])
    cmd = seen["cmd"]
    assert cmd[-4:] == ["HEAD", "--", "a.md", "b.md"]


def test_revert_with_no_paths_runs_nothing(tmp_path, monkeypatch):
    """An empty path list must NOT degrade into a whole-tree operation.

    CLAUDE.md's shell-portability rule names this exact shape: a silently-empty
    path list handed to something that falls back to "operate on everything".
    """
    called = []
    monkeypatch.setattr(sw.subprocess, "run",
                        lambda cmd, **kw: called.append(cmd))
    sw.revert(tmp_path, [])
    assert called == []
