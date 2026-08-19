#!/usr/bin/env python3
"""Drift guard: the workset generator must write its artifacts ATOMICALLY.

WHAT THIS PROTECTS. generate_inter_governance_workset.py rewrites two files
that live readers hold open concurrently:

  * evidence/planning/inter_governance_workset.v1.json (~450 KB) -- read by
    serve.py's read_workset() on GET /api/workset, which every open /workset
    page polls every 20s; also by igw_routine_tick.py (several call sites) and
    scripts/check_workset_drift.py.
  * evidence/planning/inter_governance_workset.md -- read by igw_routine_tick.py.

Until 2026-08-19 both went out through `Path.write_text()`, which is
`open(path, "w").write(text)`: it TRUNCATES at open() and then writes the
payload in several write() syscalls. Measured on the real ~450 KB payload with
4 concurrent readers: 213 of 401 reads came back unparseable. The generator is
shelled out by igw_routine_tick.regenerate_workset() on a timer and by
/inter-governance-brief, so that window is hit by ordinary operation, not by
anything exotic.

The read side was the other half and is fixed separately: read_workset() used
to swallow the JSONDecodeError and return an empty stub, so a torn read
rendered /workset with zero packages and no error at all. It now sets
`unreadable: true` and workset.html shows a banner.

Time-independent: no clock, no network, no sleep, no git. Static analysis of
the generator's source plus a real-filesystem exercise of the helper in a
tempdir.

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_atomic_write.py
"""

import ast
import importlib.util
import json
import os
import sys
import tempfile
import threading
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
GENERATOR = SCRIPTS_DIR / "generate_inter_governance_workset.py"


def _load_generator():
    spec = importlib.util.spec_from_file_location(
        "ree_igw_generator_atomic_write_test", GENERATOR
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _scan_non_atomic_writes(source_text):
    """Return [(lineno, snippet)] for every non-atomic file-write CALL.

    AST-based rather than a line regex on purpose: the source contains
    `Path.write_text()` and `open(path, "w")` inside the _atomic_write_text
    DOCSTRING, and a textual scan would false-positive on documentation. A
    call-node scan sees only real calls, and `os.fdopen(fd, "w")` -- the
    helper's own write -- is an Attribute call named `fdopen`, never matched.

    Same detector as
    evidence/experiments/scripts/test_build_experiment_indexes.py; restated
    here because that file lives under a different tree and globs its own
    module only.
    """
    tree = ast.parse(source_text)
    lines = source_text.splitlines()
    offenders = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        hit = False
        if isinstance(func, ast.Attribute) and func.attr == "write_text":
            hit = True
        elif isinstance(func, ast.Name) and func.id == "open":
            mode = None
            if len(node.args) >= 2:
                mode = node.args[1]
            else:
                for kw in node.keywords:
                    if kw.arg == "mode":
                        mode = kw.value
            if isinstance(mode, ast.Constant) and isinstance(mode.value, str) \
                    and "w" in mode.value:
                hit = True
        if hit:
            ln = node.lineno
            snippet = lines[ln - 1].strip() if 0 < ln <= len(lines) else "?"
            offenders.append((ln, snippet))
    return sorted(offenders)


class GeneratorWritesAtomicallyTest(unittest.TestCase):
    def setUp(self):
        self.src = GENERATOR.read_text(encoding="utf-8")

    def test_no_bare_write_site_in_the_generator(self):
        """No production write in the generator may be a bare
        Path.write_text()/open(..,"w") -- all must route through
        _atomic_write_text().

        One re-introduced non-atomic write re-arms the torn-read race for every
        reader of the workset, and the symptom (a /workset page with no
        packages) does not look like a write bug from the outside.
        """
        offenders = _scan_non_atomic_writes(self.src)
        self.assertEqual(
            offenders, [],
            "generate_inter_governance_workset.py writes a live-read artifact "
            "non-atomically -- route through _atomic_write_text():\n  "
            + "\n  ".join("generate_inter_governance_workset.py:%d: %s" % (ln, s)
                          for ln, s in offenders))

    def test_both_outputs_go_through_the_helper(self):
        """Positive pin: BOTH artifacts are written, and both via the helper.

        The scan above is satisfied by writing nothing at all, and the JSON is
        the file everyone thinks about -- the markdown was the one at risk of
        being left behind on a partial fix.
        """
        tree = ast.parse(self.src)
        main_fn = next((n for n in ast.walk(tree)
                        if isinstance(n, ast.FunctionDef) and n.name == "main"), None)
        self.assertIsNotNone(main_fn, "generator has no main()")
        targets = set()
        for node in ast.walk(main_fn):
            if (isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == "_atomic_write_text"
                    and node.args
                    and isinstance(node.args[0], ast.Name)):
                targets.add(node.args[0].id)
        self.assertEqual(
            targets, {"OUTPUT_JSON", "OUTPUT_MD"},
            "main() must write BOTH outputs through _atomic_write_text(); got %r"
            % (sorted(targets),))

    def test_helper_is_real_and_uses_os_replace(self):
        """The helper must actually rename, not be gutted to a plain write
        while keeping the name (which would pass the scan above vacuously)."""
        self.assertIn("def _atomic_write_text(", self.src, "helper is gone")
        tree = ast.parse(self.src)
        fn = next((n for n in ast.walk(tree)
                   if isinstance(n, ast.FunctionDef)
                   and n.name == "_atomic_write_text"), None)
        self.assertIsNotNone(fn, "cannot find _atomic_write_text def")
        body = ast.get_source_segment(self.src, fn) or ""
        self.assertIn("os.replace(", body,
                      "_atomic_write_text no longer calls os.replace()")
        self.assertIn("mkstemp(", body,
                      "_atomic_write_text no longer writes to a temp file")

    def test_the_write_scan_is_not_vacuous(self):
        """Differential proof the detector detects: a known-bad snippet is
        flagged and a known-good (helper-routed) one is not. Without this, a
        scan that silently matched nothing would pass forever."""
        bad = ('def main():\n'
               '    OUTPUT_JSON.write_text("x", encoding="utf-8")\n')
        bad2 = ('def main():\n'
                '    with open(OUTPUT_MD, "w") as fh:\n'
                '        fh.write("x")\n')
        good = ('def main():\n'
                '    _atomic_write_text(OUTPUT_JSON, "x")\n')
        self.assertTrue(_scan_non_atomic_writes(bad), "detector missed write_text")
        self.assertTrue(_scan_non_atomic_writes(bad2), 'detector missed open(.., "w")')
        self.assertEqual(_scan_non_atomic_writes(good), [],
                         "detector false-positives on the helper-routed form")


class HelperIsActuallyAtomicTest(unittest.TestCase):
    """Exercise the real helper against a real filesystem.

    The static tests above pin the SHAPE of the code; this pins its BEHAVIOUR,
    so a helper that renames from the wrong directory (os.replace() raises
    EXDEV across filesystems) or leaks temp files still fails.
    """

    @classmethod
    def setUpClass(cls):
        cls.G = _load_generator()

    def test_concurrent_readers_never_see_a_torn_file(self):
        payload_a = json.dumps({"items": [{"id": "A%d" % i, "pad": "x" * 200}
                                          for i in range(1200)]}, indent=2)
        payload_b = json.dumps({"items": [{"id": "B%d" % i, "pad": "y" * 200}
                                          for i in range(900)]}, indent=2)
        # Differing lengths on purpose: equal-length payloads can mask a tear.
        self.assertNotEqual(len(payload_a), len(payload_b))
        self.assertGreater(len(payload_b), 8192,
                           "payload must exceed the stdio buffer to be a real test")

        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "inter_governance_workset.v1.json"
            target.write_text(payload_a, encoding="utf-8")
            stop = threading.Event()
            torn = []

            def reader():
                while not stop.is_set():
                    try:
                        json.loads(target.read_text(encoding="utf-8"))
                    except FileNotFoundError:
                        pass
                    except Exception as exc:  # noqa: BLE001 -- recorded, then asserted
                        torn.append(repr(exc))

            threads = [threading.Thread(target=reader) for _ in range(4)]
            for t in threads:
                t.start()
            try:
                for i in range(40):
                    self.G._atomic_write_text(
                        target, payload_a if i % 2 else payload_b)
            finally:
                stop.set()
                for t in threads:
                    t.join()

            self.assertEqual(torn, [],
                             "atomic write still tore a concurrent read: %r"
                             % (torn[:3],))
            self.assertEqual(list(Path(td).glob("*.tmp.*")), [],
                             "left a temp file beside the real file")
            self.assertIn(target.read_text(encoding="utf-8"),
                          (payload_a, payload_b),
                          "final content is neither writer's whole document")

    def test_failed_write_leaves_no_temp_file(self):
        """os.replace() is the realistic failure point (EXDEV, EACCES, ENOSPC).
        A leaked .tmp.* reads as untracked junk in this shared checkout and is
        name-driven noise for ree_commit.py."""
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "out.json"
            real_replace = self.G.os.replace

            def boom(*a, **k):
                raise OSError("simulated rename failure")

            self.G.os.replace = boom
            try:
                with self.assertRaises(OSError):
                    self.G._atomic_write_text(target, "payload")
            finally:
                self.G.os.replace = real_replace
            self.assertEqual(list(Path(td).glob("*.tmp.*")), [],
                             "temp file leaked after a failed rename")
            self.assertFalse(target.exists(),
                             "target must not be created by a failed write")

    def test_temp_file_is_created_beside_the_target(self):
        """Same directory => same filesystem => os.replace() cannot EXDEV.
        A helper that used /tmp would pass every source scan and then fail in
        production wherever the repo is not on the tempdir's filesystem."""
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "out.json"
            seen = {}
            real_mkstemp = self.G.tempfile.mkstemp

            def spy(*a, **k):
                seen["dir"] = k.get("dir")
                return real_mkstemp(*a, **k)

            self.G.tempfile.mkstemp = spy
            try:
                self.G._atomic_write_text(target, "payload")
            finally:
                self.G.tempfile.mkstemp = real_mkstemp
            self.assertEqual(os.path.realpath(seen["dir"] or ""),
                             os.path.realpath(str(target.parent)),
                             "temp file was not created beside the target")
            self.assertEqual(target.read_text(encoding="utf-8"), "payload")


if __name__ == "__main__":
    unittest.main(verbosity=2)
