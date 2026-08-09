#!/usr/bin/env python3
"""Behavioural contract for build_experiment_indexes._atomic_write_text().

THE GAP THIS FILLS, stated narrowly. 1266b2e67c routed all ~18 regen write
sites through `_atomic_write_text()` and guarded that routing well: an AST scan
for any bare `.write_text(` / `open(.., "w")` that returns
(`test_regen_writes_shared_artifacts_atomically`), a differential proving that
scan is not vacuous (`test_the_write_scan_is_not_vacuous`), and a check that the
helper has not been gutted while keeping its name
(`test_atomic_write_helper_is_real_and_uses_os_replace`). All three are
STRUCTURAL -- they read the source. Nothing anywhere RUNS the helper.

That leaves a class of regression the source scan passes by construction,
because the strings it looks for are still present:

  * `mkstemp()` losing its `dir=` argument. The scan asserts `mkstemp(` and
    `os.replace(` appear, and both still would -- but the temp file would land
    in /tmp, and os.replace() across filesystems raises OSError(EXDEV). /tmp is
    a separate mount on the cloud workers, so this fails THERE and not on the
    Mac, which is the same "works on the Mac, breaks on the fleet" shape the
    helper's own docstring cites as the reason it is not a cross-repo import.
  * the cleanup branch breaking, leaving `.tmp.*` litter beside a tracked
    artifact -- untracked junk in every other session's `git status` on this
    shared checkout, and ree_commit.py's path list is name-driven.
  * the failure being swallowed rather than re-raised, which would turn a
    failed regen into a silently skipped artifact -- indistinguishable from a
    successful one at exit 0.
  * a reordering that writes and renames in the wrong sequence.

So this module asserts the PROPERTY instead of the spelling: real concurrent
processes writing the real helper's output to one real file, with the naive
`Path.write_text()` as a negative control on identical payloads. Without the
control, the atomic tests could be passing because the burst never actually
races -- which would make the whole module vacuous, the failure mode its
siblings were careful to rule out for the scan.

The control is a DETERMINISTIC two-descriptor interleave rather than a timing
race, so this suite has no wall-clock dependence and cannot flake.

Runs both as `python3 evidence/experiments/scripts/test_atomic_write_behaviour.py`
and under the bare-root `pytest` that CI runs. Stdlib only. ASCII-only.
"""
import json
import multiprocessing
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import build_experiment_indexes as b  # noqa: E402

atomic_write_text = b._atomic_write_text


def payload(writer, size):
    """Valid JSON whose LENGTH varies with `writer` -- the key ingredient.

    Equal-length writers would overwrite each other cleanly and hide the bug.
    The real artifacts differ in length between regens for the same reason:
    the run corpus grows.
    """
    return json.dumps(
        {"items": [{"i": i, "w": "writer%d" % writer} for i in range(size)]},
        indent=2) + "\n"


def _writer_proc(path, writer, size, rounds):
    for _ in range(rounds):
        atomic_write_text(Path(path), payload(writer, size))


def _reader_proc(path, rounds, out):
    """Read `rounds` times; report how many reads did not parse."""
    torn = 0
    for _ in range(rounds):
        try:
            json.loads(Path(path).read_text(encoding="utf-8"))
        except Exception:
            torn += 1
    out.put(torn)


class AtomicWriteBehaviourTest(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="reeatomic-"))
        self.addCleanup(shutil.rmtree, self.dir, True)
        self.path = self.dir / "artifact.v1.json"

    def test_replaces_a_longer_file_completely(self):
        """No tail of the previous, longer content may survive."""
        atomic_write_text(self.path, payload(1, 400))
        atomic_write_text(self.path, payload(2, 5))
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8")),
                         json.loads(payload(2, 5)))

    def test_no_temp_file_survives_a_successful_write(self):
        atomic_write_text(self.path, payload(1, 50))
        self.assertEqual([p.name for p in self.dir.iterdir()],
                         ["artifact.v1.json"])

    def test_temp_file_is_created_beside_the_target(self):
        """Same directory => same filesystem => os.replace() cannot EXDEV.

        The regression this catches is `mkstemp()` losing its `dir=`: the
        source scan still sees `mkstemp(` and `os.replace(`, but the rename
        would cross a filesystem boundary and raise on any box where /tmp is a
        separate mount -- the cloud workers -- and not on the Mac.
        """
        seen = []
        real_mkstemp = b.tempfile.mkstemp

        def spy(*a, **kw):
            seen.append(kw.get("dir"))
            return real_mkstemp(*a, **kw)

        b.tempfile.mkstemp = spy
        try:
            atomic_write_text(self.path, payload(1, 20))
        finally:
            b.tempfile.mkstemp = real_mkstemp
        self.assertEqual(seen, [str(self.dir)])

    def test_a_failed_rename_raises_and_leaves_no_temp_file(self):
        """os.replace() is the realistic failure point (EXDEV, EACCES, ENOSPC).

        The raise matters as much as the cleanup: swallowing it would turn a
        failed regen into a silently skipped artifact at exit 0.
        """
        real_replace = b.os.replace

        def boom(*_a, **_kw):
            raise OSError(18, "Invalid cross-device link")

        b.os.replace = boom
        try:
            with self.assertRaises(OSError):
                atomic_write_text(self.path, payload(1, 50))
        finally:
            b.os.replace = real_replace
        self.assertEqual(list(self.dir.iterdir()), [])


class ConcurrentProcessTest(unittest.TestCase):
    """Real processes, real file, no mocking. The point of the whole module."""

    WRITERS = 5
    ROUNDS = 12

    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="reeatomicproc-"))
        self.addCleanup(shutil.rmtree, self.dir, True)
        self.path = self.dir / "artifact.v1.json"
        atomic_write_text(self.path, payload(0, 200))

    def _burst(self):
        ctx = multiprocessing.get_context("spawn")
        out = ctx.Queue()
        procs = [ctx.Process(target=_writer_proc,
                             args=(str(self.path), w, 40 + w * 90, self.ROUNDS))
                 for w in range(1, self.WRITERS + 1)]
        procs.append(ctx.Process(target=_reader_proc,
                                 args=(str(self.path), self.ROUNDS * 12, out)))
        for p in procs:
            p.start()
        for p in procs:
            p.join(180)
        return out.get(timeout=15)

    def test_no_concurrent_reader_ever_sees_a_torn_file(self):
        self.assertEqual(
            self._burst(), 0,
            "a concurrent reader parsed a torn artifact -- "
            "_atomic_write_text() is not atomic")

    def test_the_final_file_is_exactly_one_writers_document(self):
        self._burst()
        data = json.loads(self.path.read_text(encoding="utf-8"))
        names = {c["w"] for c in data["items"]}
        self.assertEqual(len(names), 1,
                         "final file spliced %d writers together: %s"
                         % (len(names), sorted(names)))

    def test_no_temp_files_survive_the_burst(self):
        self._burst()
        strays = sorted(p.name for p in self.dir.iterdir()
                        if p.name != "artifact.v1.json")
        self.assertEqual(strays, [], "leftover temp files: %s" % strays)


class NaiveWriteIsTheHazardTest(unittest.TestCase):
    """Negative control: the SAME payloads through Path.write_text() tear.

    Deterministic two-descriptor interleave, not a race -- exactly what two
    concurrent Path.write_text() calls do, since each opens (truncating) and
    writes at its own offset.
    """

    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="reenaive-"))
        self.addCleanup(shutil.rmtree, self.dir, True)
        self.path = self.dir / "artifact.v1.json"

    def test_two_interleaved_write_text_calls_produce_the_incident_signature(self):
        long_doc, short_doc = payload(2, 400), payload(1, 100)
        fh_long = open(self.path, "w", encoding="utf-8")
        fh_short = open(self.path, "w", encoding="utf-8")
        fh_long.write(long_doc)
        fh_long.close()
        # The shorter writer finishing last overwrites only the PREFIX, leaving
        # the longer one's tail behind.
        fh_short.write(short_doc)
        fh_short.close()
        with self.assertRaises(json.JSONDecodeError) as ctx:
            json.loads(self.path.read_text(encoding="utf-8"))
        self.assertIn("Extra data", str(ctx.exception),
                      "expected a valid prefix followed by a stray tail")

    def test_the_same_content_through_the_helper_is_clean(self):
        """Positive control on the identical payloads."""
        atomic_write_text(self.path, payload(2, 400))
        atomic_write_text(self.path, payload(1, 100))
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8")),
                         json.loads(payload(1, 100)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
