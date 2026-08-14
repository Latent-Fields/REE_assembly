#!/usr/bin/env python3
"""Regression tests for precommit_literature.sh -- the literature COMMIT GATE.

The shim had no test coverage at all until 2026-08-14, the day its default
flipped from report-only to BLOCKING. That flip is what makes coverage
load-bearing rather than nice-to-have: until then a bug in the shim could only
fail to warn, and from now on it can refuse a commit.

Every test builds a REAL git repository in a tempdir, with a real schema, real
entry directories, real staged changes, and runs the real shell script against
the real validate_literature.py. Nothing is monkeypatched -- the shim's entire
job is to read git's staged state and decide, so a mocked git would test the
mock. Two prior incidents in this repo argue for exactly that: the commit-guard
hooks are `[ -f ]`-gated and therefore FAIL OPEN AND SILENT when a path misses
(CLAUDE.md, worktree rule 4), which is invisible to any test that does not
execute the real script by its real path.

Roughly half of these are NEGATIVE CONTROLS -- commits the gate must NOT block.
Those are the assertions that stop a later session widening the predicate until
the gate has to be turned off, the same reasoning `test_ref_move_guard.py`
records for the ref-move guard.

Time-independent: no wall-clock reads, no dates derived from `now`.

Run: /opt/local/bin/python3 scripts/test_precommit_literature.py
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
SCHEMA_REL = "evidence/literature/schemas/v1/literature_evidence.schema.json"
SHIM = SCRIPTS_DIR / "precommit_literature.sh"

# Exit codes the shim documents. Named so a change to one fails loudly here.
CLEAN = 0
BLOCKED = 2
INTERNAL_ERROR = 3


def valid_record(entry_id, literature_type):
    return {
        "schema_version": "literature_evidence/v1",
        "literature_type": literature_type,
        "entry_id": entry_id,
        "timestamp_utc": "2026-05-16T10:00:00Z",
        "claim_ids_tested": ["MECH-001"],
        "source": {
            "title": "A Paper",
            "authors": ["Author, A."],
            "year": 2024,
            "doi": "10.1000/abc",
        },
        "evidence_class": "review",
        "evidence_direction": "supports",
        "confidence": 0.7,
        "confidence_rationale": "single well-powered study",
        "summary_path": "summary.md",
    }


class ShimTestCase(unittest.TestCase):
    """A real git repo shaped like REE_assembly, with the real schema + validator."""

    make_literature_dir = True

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ree_precommit_lit_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Test")

        if self.make_literature_dir:
            schema_dst = self.tmp / SCHEMA_REL
            schema_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO_ROOT / SCHEMA_REL, schema_dst)
            (self.tmp / "scripts").mkdir(exist_ok=True)
            shutil.copyfile(REPO_ROOT / "scripts" / "validate_literature.py",
                            self.tmp / "scripts" / "validate_literature.py")

        # An initial commit, so `git diff --cached` has a HEAD to diff against.
        (self.tmp / "README.md").write_text("seed\n")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "seed")

    # -- helpers ----------------------------------------------------------
    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.tmp), *args],
                              capture_output=True, text=True, check=True)

    def write_entry(self, literature_type, entry_id, record=None, summary=True):
        entry_dir = self.tmp / "evidence" / "literature" / literature_type / "entries" / entry_id
        entry_dir.mkdir(parents=True, exist_ok=True)
        if record is None:
            record = valid_record(entry_id, literature_type)
        (entry_dir / "record.json").write_text(json.dumps(record, indent=2))
        if summary:
            (entry_dir / "summary.md").write_text("# summary\n")
        return entry_dir

    def run_shim(self, *args, env=None):
        """Execute the REAL shim, from the repo, exactly as a hook would."""
        environ = dict(os.environ)
        environ["REE_PYTHON"] = sys.executable
        # The shim resolves the repo via `git rev-parse --show-toplevel`, so it
        # must run with cwd inside the tempdir repo, not this checkout.
        environ.pop("REE_LITERATURE_GATE_BLOCK", None)
        if env:
            environ.update(env)
        return subprocess.run(["bash", str(self.tmp / "scripts" / "precommit_literature.sh"), *args],
                              cwd=str(self.tmp), capture_output=True, text=True, env=environ)

    def install_shim(self):
        shutil.copyfile(SHIM, self.tmp / "scripts" / "precommit_literature.sh")


class NothingStagedTest(ShimTestCase):
    """SELF-GATING. This hook fires on EVERY git commit in EVERY repo, so the
    overwhelmingly common case is 'nothing of ours is being committed'."""

    def setUp(self):
        super().setUp()
        self.install_shim()

    def test_no_staged_changes_at_all_is_silent_and_clean(self):
        r = self.run_shim()
        self.assertEqual(r.returncode, CLEAN)
        self.assertEqual(r.stdout.strip(), "", "must be silent when nothing is staged")

    def test_staged_change_outside_evidence_literature_is_ignored(self):
        (self.tmp / "unrelated.py").write_text("x = 1\n")
        self.git("add", "unrelated.py")
        r = self.run_shim()
        self.assertEqual(r.returncode, CLEAN)
        self.assertEqual(r.stdout.strip(), "")

    def test_a_bad_record_that_is_NOT_STAGED_does_not_block(self):
        """PATH SCOPING -- the property the blocking default depends on.

        A pre-existing bad record elsewhere in the corpus must never wedge an
        unrelated commit. This is precisely what makes flipping the default to
        blocking cheap, so it is asserted rather than assumed.
        """
        bad = valid_record("2026-05-16_bad", "targeted_review_x")
        bad["source"]["undeclared_key"] = "boom"
        self.write_entry("targeted_review_x", "2026-05-16_bad", record=bad)
        (self.tmp / "unrelated.py").write_text("x = 1\n")
        self.git("add", "unrelated.py")  # note: the bad record is NOT staged
        r = self.run_shim()
        self.assertEqual(r.returncode, CLEAN, r.stdout + r.stderr)


class CleanStagedRecordTest(ShimTestCase):
    """NEGATIVE CONTROL: ordinary, correct literature work must sail through."""

    def setUp(self):
        super().setUp()
        self.install_shim()

    def test_valid_staged_record_passes(self):
        self.write_entry("targeted_review_x", "2026-05-16_a")
        self.git("add", "-A")
        r = self.run_shim()
        self.assertEqual(r.returncode, CLEAN, r.stdout + r.stderr)

    def test_valid_record_alongside_an_unrelated_staged_file_passes(self):
        self.write_entry("targeted_review_x", "2026-05-16_a")
        (self.tmp / "unrelated.py").write_text("x = 1\n")
        self.git("add", "-A")
        r = self.run_shim()
        self.assertEqual(r.returncode, CLEAN, r.stdout + r.stderr)


class BlockingTest(ShimTestCase):
    """The flip. Default is BLOCKING as of 2026-08-14."""

    def setUp(self):
        super().setUp()
        self.install_shim()

    def _stage_bad_record(self):
        bad = valid_record("2026-05-16_bad", "targeted_review_x")
        bad["source"]["undeclared_key"] = "boom"
        self.write_entry("targeted_review_x", "2026-05-16_bad", record=bad)
        self.git("add", "-A")

    def test_bad_staged_record_blocks_BY_DEFAULT(self):
        """THE flip assertion. If this ever reverts to 0, the gate is off."""
        self._stage_bad_record()
        r = self.run_shim()
        self.assertEqual(r.returncode, BLOCKED,
                         "the default must BLOCK a bad staged record:\n" + r.stdout + r.stderr)
        self.assertIn("BLOCKING", r.stdout)

    def test_the_finding_itself_is_printed_not_just_the_verdict(self):
        """A gate that blocks without naming the record is a gate people disable."""
        self._stage_bad_record()
        r = self.run_shim()
        self.assertIn("2026-05-16_bad", r.stdout)

    def test_env_escape_hatch_downgrades_to_report_only(self):
        self._stage_bad_record()
        r = self.run_shim(env={"REE_LITERATURE_GATE_BLOCK": "0"})
        self.assertEqual(r.returncode, CLEAN, r.stdout + r.stderr)
        self.assertIn("report-only", r.stdout)

    def test_report_only_flag_downgrades_too(self):
        self._stage_bad_record()
        r = self.run_shim("--report-only")
        self.assertEqual(r.returncode, CLEAN, r.stdout + r.stderr)

    def test_explicit_block_flag_still_blocks(self):
        """--block was the pre-flip opt-IN; it must keep working, not become a no-op."""
        self._stage_bad_record()
        r = self.run_shim("--block")
        self.assertEqual(r.returncode, BLOCKED, r.stdout + r.stderr)

    def test_env_block_1_still_blocks(self):
        self._stage_bad_record()
        r = self.run_shim(env={"REE_LITERATURE_GATE_BLOCK": "1"})
        self.assertEqual(r.returncode, BLOCKED, r.stdout + r.stderr)

    def test_a_staged_summary_deletion_is_checked(self):
        """The dangling-summary_path case: the damage lands on a record that is
        not itself staged, which is why the shim feeds staged DELETIONS too."""
        entry = self.write_entry("targeted_review_x", "2026-05-16_a")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "add entry")
        (entry / "summary.md").unlink()
        self.git("add", "-A")
        r = self.run_shim()
        self.assertEqual(r.returncode, BLOCKED,
                         "deleting a summary.md a record still points at must block:\n"
                         + r.stdout + r.stderr)


class NotOurRepoTest(ShimTestCase):
    """FAIL-OPEN control. The hook runs on every commit in ree-v3, the umbrella
    repo, everywhere. A repo with no evidence/literature/ is not ours."""

    make_literature_dir = False

    def test_repo_without_evidence_literature_exits_clean_and_silent(self):
        (self.tmp / "scripts").mkdir(exist_ok=True)
        self.install_shim()
        (self.tmp / "unrelated.py").write_text("x = 1\n")
        self.git("add", "-A")
        r = self.run_shim()
        self.assertEqual(r.returncode, CLEAN, r.stdout + r.stderr)
        self.assertEqual(r.stdout.strip(), "")


class MissingValidatorTest(ShimTestCase):
    """An absent validator must be LOUD (exit 3), not a silent pass.

    This is the `[ -f ]`-gated fail-open-and-silent failure mode CLAUDE.md
    records for the worktree commit guards: the gate that quietly stops existing
    is worse than the gate that errors.
    """

    def test_missing_validator_is_an_internal_error_not_a_silent_pass(self):
        self.install_shim()
        (self.tmp / "scripts" / "validate_literature.py").unlink()
        self.write_entry("targeted_review_x", "2026-05-16_a")
        self.git("add", "-A")
        r = self.run_shim()
        self.assertEqual(r.returncode, INTERNAL_ERROR, r.stdout + r.stderr)
        self.assertIn("missing", r.stderr)


class ShimAgreesWithTheValidatorTest(ShimTestCase):
    """The shim's clean-detection is a STRING MATCH on the validator's OK line.

    That coupling is invisible from either side: rewording validate_literature's
    success line turns every gate run into a silent block. Pin it.
    """

    def test_the_ok_line_the_shim_greps_for_is_the_line_the_validator_prints(self):
        self.install_shim()
        self.write_entry("targeted_review_x", "2026-05-16_a")
        out = subprocess.run(
            [sys.executable, str(self.tmp / "scripts" / "validate_literature.py"),
             "--repo", str(self.tmp)],
            capture_output=True, text=True).stdout
        self.assertIn("validate_literature: OK", out,
                      "precommit_literature.sh greps for this exact prefix; if the "
                      "validator's success line changed, update BOTH.")
        self.assertIn("validate_literature: OK", SHIM.read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
