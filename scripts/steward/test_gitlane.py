#!/usr/bin/env python3
"""Contract tests for the Steward git lane (D-101 divergence, D-102 ref guard).

Run from REE_assembly/ root:
    /opt/local/bin/python3 -m pytest scripts/steward/test_gitlane.py -q

Unlike test_run_detectors.py / test_autofix.py these DO use git -- real
repositories built in a tmpdir, with a real bare remote and real pushes. That
follows the precedent of scripts/test_ref_move_guard.py and
scripts/test_safe_adopt_ref.py: a guard against git behaviour that is tested
against a mock of git is a guard against the mock. No network, no sleeps, no
wall-clock dependence.

WHY SO MANY NEGATIVE CONTROLS. Roughly half of these pin what the lane must NOT
do: not classify TASK_CLAIMS/TASK_CHIPS as churn, not mutate anything, not
publish a verdict computed across a ref move, not call a mutating subcommand.
Those are the assertions that stop a later session widening a predicate until
the lane starts discarding real work -- which is the failure this whole lane
exists to prevent, and which has a measured 15-stranded-commit incident behind
it.

ON THE 2026-08-15 ACCEPTANCE CASE. The incident range (REE_assembly at
[ahead 66, behind 274]) lived in the MAC checkout's reflog and is not reachable
from a Linux worker -- this box's reflog begins 2026-08-16. So the acceptance
test is built the reproducible way instead: test_incident_shape_is_reproduced
constructs a divergence carrying all the shapes the manual analysis found
(patch-id equivalents, substantive-content-equivalent commits that patch-id
MISSES, and regenerable churn) and asserts both the per-commit classification
and the safe_to_adopt verdict the hand analysis reached. The live-tree
measurement is recorded in README.md as a baseline.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

_STEWARD = Path(__file__).resolve().parent
if str(_STEWARD) not in sys.path:
    sys.path.insert(0, str(_STEWARD))

from detectors import _gitlane as G  # noqa: E402
from detectors import d101_divergence_content_equivalence as D101  # noqa: E402
from detectors import d102_moving_ref_guard as D102  # noqa: E402
from detectors._common import Context  # noqa: E402


# ---------------------------------------------------------------------------
# git fixture helpers
# ---------------------------------------------------------------------------

def sh(repo: Path, *args: str) -> str:
    proc = subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), proc.stderr))
    return proc.stdout


def commit(repo: Path, path: str, content: str, msg: str) -> str:
    f = repo / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")
    sh(repo, "add", "-A")
    sh(repo, "-c", "user.email=t@t", "-c", "user.name=Tester",
       "commit", "-qm", msg)
    return sh(repo, "rev-parse", "HEAD").strip()


def make_pair(tmp_path: Path) -> tuple[Path, Path]:
    """A local repo on `master` tracking a real bare `origin`."""
    bare = tmp_path / "origin.git"
    subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
    local = tmp_path / "local"
    subprocess.run(["git", "init", "-q", "-b", "master", str(local)], check=True)
    commit(local, "seed.txt", "seed\n", "seed")
    sh(local, "remote", "add", "origin", str(bare))
    sh(local, "push", "-q", "-u", "origin", "master")
    return local, bare


def clone_of(bare: Path, dest: Path) -> Path:
    subprocess.run(["git", "clone", "-q", str(bare), str(dest)], check=True)
    return dest


def ctx_for(repos: list[Path]) -> Context:
    return Context(repo_root=repos[0], claims=[], claims_by_id={}, nodes=[],
                   plans=[], owners={}, parse_errors=[],
                   git_repos=[Path(r) for r in repos])


# ===========================================================================
# The non-negotiable: the lane cannot act
# ===========================================================================

@pytest.mark.parametrize("sub", [
    "update-ref", "reset", "commit", "push", "rebase", "checkout", "add",
    "merge", "cherry-pick", "fetch", "pull", "clean", "branch", "stash",
])
def test_mutating_subcommands_are_refused(tmp_path, sub):
    """A whitelist, not a blacklist -- and `fetch` is refused on purpose.

    Fetching MOVES remote-tracking refs, which would make the guard the cause
    of the movement it exists to detect.
    """
    local, _ = make_pair(tmp_path)
    with pytest.raises(G.GitLaneViolation):
        G.git(local, sub, "--help")


def test_read_only_subcommands_are_permitted(tmp_path):
    local, _ = make_pair(tmp_path)
    assert G.git(local, "rev-parse", "HEAD").strip()
    assert G.git(local, "status", "--porcelain") == ""


def test_classify_never_mutates_the_repo(tmp_path):
    local, bare = make_pair(tmp_path)
    commit(local, "a.txt", "a\n", "local work")
    before_head = sh(local, "rev-parse", "HEAD").strip()
    before_status = sh(local, "status", "--porcelain")
    before_reflog = sh(local, "reflog", "show", "master")

    D101.classify_repo(local)

    assert sh(local, "rev-parse", "HEAD").strip() == before_head
    assert sh(local, "status", "--porcelain") == before_status
    assert sh(local, "reflog", "show", "master") == before_reflog


# ===========================================================================
# D-101 classification
# ===========================================================================

def test_no_divergence_is_safe_to_adopt(tmp_path):
    local, _ = make_pair(tmp_path)
    res = D101.classify_repo(local)
    assert res["ahead"] == 0 and res["behind"] == 0
    assert res["verdict"] == "safe_to_adopt"


def test_behind_only_is_safe_to_adopt(tmp_path):
    local, bare = make_pair(tmp_path)
    other = clone_of(bare, tmp_path / "other")
    commit(other, "up.txt", "up\n", "upstream work")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["ahead"] == 0 and res["behind"] == 1
    assert res["verdict"] == "safe_to_adopt"


def test_patch_id_equivalent_commit_is_not_unique(tmp_path):
    """The same change landed upstream as a cherry-pick -- route A."""
    local, bare = make_pair(tmp_path)
    sha = commit(local, "f.txt", "hello\n", "add f")

    other = clone_of(bare, tmp_path / "other")
    sh(other, "fetch", "-q", str(local), "master")
    sh(other, "cherry-pick", sha)
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    klasses = [c["klass"] for c in res["commits"]]
    assert "upstream_by_patch_id" in klasses
    assert res["verdict"] == "safe_to_adopt"


def test_content_equivalent_commit_that_patch_id_misses(tmp_path):
    """Route A's endemic false negative, caught by route B.

    The same lines land upstream at a DIFFERENT offset, so the diff context --
    and therefore the patch-id -- differs. This is the append-at-a-different-
    position shape CLAUDE.md names as native to the hot JSON registries.
    """
    local, bare = make_pair(tmp_path)
    commit(local, "reg.txt", "seed\nMINE-1\n", "append mine")

    other = clone_of(bare, tmp_path / "other")
    commit(other, "reg.txt", "seed\nTHEIRS-1\nTHEIRS-2\nMINE-1\n", "their appends")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["tally"].get("upstream_by_patch_id", 0) == 0, "patch-id must miss it"
    assert res["tally"].get("upstream_by_content") == 1
    assert res["verdict"] == "safe_to_adopt"


def test_genuinely_unique_work_is_flagged(tmp_path):
    local, bare = make_pair(tmp_path)
    commit(local, "mine.txt", "content origin has never seen\n", "unique work")
    other = clone_of(bare, tmp_path / "other")
    commit(other, "theirs.txt", "unrelated\n", "upstream")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["tally"].get("unique") == 1
    # touches no path origin changed -> replayable
    assert res["verdict"] == "needs_rebase"
    assert res["contested_paths"] == []


def test_unique_work_touching_an_upstream_modified_path_is_contested(tmp_path):
    local, bare = make_pair(tmp_path)
    commit(local, "shared.txt", "seed\nMINE\n", "my edit")
    other = clone_of(bare, tmp_path / "other")
    commit(other, "shared.txt", "seed\nTHEIRS\n", "their edit")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["verdict"] == "unique_work_present"
    assert "shared.txt" in res["contested_paths"]


def test_regenerable_churn_does_not_block_adoption(tmp_path):
    local, bare = make_pair(tmp_path)
    commit(local, "evidence/planning/igw_assignments.json", '{"a":1}\n',
           "igw-assignments: route")
    other = clone_of(bare, tmp_path / "other")
    commit(other, "unrelated.txt", "x\n", "upstream")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["tally"].get("regenerable_churn") == 1
    assert res["verdict"] == "safe_to_adopt"


@pytest.mark.parametrize("path", list(D101.NEVER_CHURN))
def test_task_claims_and_chips_are_never_churn(path):
    """THE category error, encoded.

    A decision chip asserted exactly this of 26 commits, 15 of which were
    genuinely stranded. The shape of a file explains why a patch-id proof
    FAILS; it says nothing about whether the content reached origin.
    """
    assert D101._is_churn_path(path) is False


def test_task_claims_commit_is_classified_unique_not_churn(tmp_path):
    local, bare = make_pair(tmp_path)
    commit(local, "TASK_CLAIMS.json", '{"claims":[{"id":"mine"}]}\n',
           "claim: open")
    other = clone_of(bare, tmp_path / "other")
    commit(other, "unrelated.txt", "x\n", "upstream")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["tally"].get("unique") == 1
    assert res["tally"].get("regenerable_churn", 0) == 0
    assert res["verdict"] != "safe_to_adopt"


def test_content_check_normalises_both_sides(tmp_path):
    """Indented content that IS upstream must not read as unique.

    Found live on 2026-08-16: added_lines() strips each line, so the upstream
    side must strip too. Comparing stripped against unstripped classified a
    commit whose blob was BYTE-IDENTICAL to origin's as unique work.
    """
    local, bare = make_pair(tmp_path)
    body = "def f():\n    return 1\n        deeply = True\n"
    commit(local, "mod.py", body, "add mod")
    other = clone_of(bare, tmp_path / "other")
    commit(other, "mod.py", body, "same content, different commit")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["tally"].get("unique", 0) == 0
    assert res["verdict"] == "safe_to_adopt"


def test_incident_shape_is_reproduced(tmp_path):
    """The 2026-08-15 acceptance case, as a reproducible fixture.

    All three shapes the hand analysis found, in one divergence: commits
    already upstream by patch-id, a substantive commit upstream only by
    CONTENT (which patch-id misses), and regenerable automation churn.
    Hand verdict: safe to adopt. So is this one.
    """
    local, bare = make_pair(tmp_path)
    other = clone_of(bare, tmp_path / "other")

    # (a) three commits that will land upstream verbatim (patch-id route)
    picks = [commit(local, "doc%d.md" % i, "body %d\n" % i, "note %d" % i)
             for i in range(3)]
    # (b) a substantive append that lands upstream at a different offset
    commit(local, "registry.txt", "seed\nSOC-HUM-1\n", "register SOC-HUM-1")
    # (c) machine churn the producer rewrites on its next tick
    commit(local, "evidence/experiments/runner_heartbeats/box.json",
           '{"tick":1}\n', "phase3-heartbeats: tick")

    sh(other, "fetch", "-q", str(local), "master")
    for sha in picks:
        sh(other, "cherry-pick", sha)
    commit(other, "registry.txt", "seed\nUPSTREAM-A\nSOC-HUM-1\n",
           "upstream registry churn")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    res = D101.classify_repo(local)
    assert res["ahead"] == 5
    assert res["tally"].get("upstream_by_patch_id") == 3
    assert res["tally"].get("upstream_by_content") == 1
    assert res["tally"].get("regenerable_churn") == 1
    assert res["tally"].get("unique", 0) == 0
    assert res["verdict"] == "safe_to_adopt"


def test_detached_head_is_skipped_not_crashed(tmp_path):
    local, _ = make_pair(tmp_path)
    sh(local, "checkout", "-q", "--detach", "HEAD")
    assert "skipped" in D101.classify_repo(local)


def test_repo_with_no_upstream_is_skipped(tmp_path):
    solo = tmp_path / "solo"
    subprocess.run(["git", "init", "-q", "-b", "master", str(solo)], check=True)
    commit(solo, "a.txt", "a\n", "only")
    assert "skipped" in D101.classify_repo(solo)


# ===========================================================================
# D-102 -- the moving-ref guard
# ===========================================================================

def test_pin_records_concrete_shas(tmp_path):
    local, _ = make_pair(tmp_path)
    pin = G.RefPin.capture(local, ["master", "origin/master"])
    assert pin.sha("master") == sh(local, "rev-parse", "master").strip()
    assert pin.captured_at.endswith("Z")


def test_pin_refuses_to_resolve_an_unpinned_ref(tmp_path):
    """The API cannot NAME a moving ref -- that is the structural fix."""
    local, _ = make_pair(tmp_path)
    pin = G.RefPin.capture(local, ["master"])
    with pytest.raises(KeyError):
        pin.sha("origin/master")


def test_assert_unmoved_passes_on_a_quiet_repo(tmp_path):
    local, _ = make_pair(tmp_path)
    pin = G.RefPin.capture(local, ["master", "origin/master"])
    pin.assert_unmoved()


def test_assert_unmoved_aborts_when_the_ref_moved(tmp_path):
    """The 2026-08-15 shape: verified, then stale, then trusted."""
    local, _ = make_pair(tmp_path)
    pin = G.RefPin.capture(local, ["master"])
    commit(local, "later.txt", "later\n", "moves master")

    with pytest.raises(G.RefMoved) as exc:
        pin.assert_unmoved()
    assert exc.value.moves[0][0] == "master"


def test_guard_aborts_on_a_deliberately_stale_pin(tmp_path):
    """The acceptance case: hand the guard a pin that is known to be stale."""
    local, _ = make_pair(tmp_path)
    stale = {"master": "0" * 40}
    with pytest.raises(G.RefMoved):
        D102.guard(local, stale)


def test_guard_passes_on_a_current_pin(tmp_path):
    local, _ = make_pair(tmp_path)
    D102.guard(local, {"master": sh(local, "rev-parse", "master").strip()})


def test_blob_sha_reads_through_the_pin_not_the_moving_ref(tmp_path):
    """A pinned read must keep returning the PINNED content after a move."""
    local, _ = make_pair(tmp_path)
    commit(local, "f.txt", "v1\n", "v1")
    pin = G.RefPin.capture(local, ["master"])
    pinned = pin.blob_sha("master", "f.txt")
    assert pin.blob_lines("master", "f.txt") == ["v1"]

    commit(local, "f.txt", "v2\n", "v2")
    assert pin.blob_sha("master", "f.txt") == pinned, "pin followed the ref"
    assert pin.blob_lines("master", "f.txt") == ["v1"]


def test_d102_reports_movement_since_the_previous_run(tmp_path):
    local, _ = make_pair(tmp_path)
    ctx = ctx_for([local])
    findings, _ = D102.run(ctx)
    assert findings == [], "first run has no prior pin to compare"
    assert str(local.resolve()) in ctx.ref_pins_out

    prior = dict(ctx.ref_pins_out)
    commit(local, "next.txt", "n\n", "moves master")

    ctx2 = ctx_for([local])
    ctx2.prior_ref_pins = prior
    findings, _ = D102.run(ctx2)
    assert len(findings) == 1
    assert findings[0]["subject"].endswith(":since-last-run")
    assert findings[0]["escalate"] is False, "perishability is not a defect"
    assert findings[0]["evidence"]["moved"][0]["ref"] == "master"


def test_d102_escalates_when_a_published_verdict_went_stale(tmp_path):
    """The tail window: a ref moved after D-101 computed its verdict."""
    local, _ = make_pair(tmp_path)
    ctx = ctx_for([local])
    ctx.ref_pins[str(local.resolve())] = {
        "captured_at": "2026-08-16T00:00:00Z",
        "shas": {"master": "0" * 40},
    }
    findings, _ = D102.run(ctx)
    stale = [f for f in findings if f["subject"].endswith(":in-run")]
    assert len(stale) == 1
    assert stale[0]["severity"] == "P0"
    assert stale[0]["escalate"] is True


def test_d101_withholds_its_verdict_when_the_pin_moves(monkeypatch, tmp_path):
    """A verdict computed across a ref move is discarded, never downgraded."""
    local, _ = make_pair(tmp_path)
    commit(local, "a.txt", "a\n", "work")

    real = G.RefPin.assert_unmoved

    def boom(self):
        raise G.RefMoved([("origin/master", "a" * 40, "b" * 40)])

    monkeypatch.setattr(G.RefPin, "assert_unmoved", boom)
    findings, _ = D101.run(ctx_for([local]))
    monkeypatch.setattr(G.RefPin, "assert_unmoved", real)

    assert len(findings) == 1
    assert findings[0]["subject"].endswith(":ref-moved")
    assert "withheld" in findings[0]["title"]
    # no verdict of any kind may be published
    assert "verdict" not in findings[0]["evidence"]


def test_git_lane_findings_are_never_autofixable(tmp_path):
    """T2 by construction: the lane classifies, a human acts."""
    local, bare = make_pair(tmp_path)
    commit(local, "mine.txt", "unique\n", "work")
    other = clone_of(bare, tmp_path / "other")
    commit(other, "up.txt", "u\n", "upstream")
    sh(other, "push", "-q", "origin", "master")
    sh(local, "fetch", "-q", "origin")

    findings, _ = D101.run(ctx_for([local]))
    assert findings
    for f in findings:
        assert f["tier"] == "T2" and f["autofix"] is False
