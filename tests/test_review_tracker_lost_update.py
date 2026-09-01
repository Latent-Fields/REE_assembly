#!/usr/bin/env python3
"""Regression tests for the review_tracker.json lost update
(derived_evidence_index:P2, plan section 3).

review_tracker.json is documented in CLAUDE.md as the SOLE source of truth for
whether an experiment has been discussed. serve.py runs on a
ThreadingHTTPServer, and `POST /api/review/discuss` used to do
load -> mutate -> save with nothing serialising it, so two concurrent review
actions each read the same snapshot and the later save silently erased the
earlier append.

REAL THREADS, REAL FILES. The race is a property of concurrent execution against
a real filesystem; a mocked "two calls in sequence" test would pass against the
BROKEN code and prove nothing. `test_unserialised_read_modify_write_loses_updates`
is the negative control that reproduces the old shape and asserts it really does
lose data on this machine -- without it, a green suite could mean "fixed" or
could mean "the race never fired here".

Time-independent: no sleeps are used to order anything; a Barrier forces the
overlap deterministically.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def _load_serve():
    spec = importlib.util.spec_from_file_location("_serve_under_test", REPO / "serve.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_serve_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


serve = _load_serve()

N_WRITERS = 24


class ReviewTrackerConcurrencyTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "review_tracker.json"
        self.path.write_text(json.dumps({
            "schema_version": "review_tracker/v1",
            "reviewed_run_ids": [],
            "discussed_experiment_dirs": [],
        }))
        self._orig_file = serve.REVIEW_TRACKER_FILE
        self._orig_lockfile = serve._REVIEW_TRACKER_LOCKFILE
        serve.REVIEW_TRACKER_FILE = self.path
        serve._REVIEW_TRACKER_LOCKFILE = self.path.with_name(self.path.name + ".lock")

    def tearDown(self):
        serve.REVIEW_TRACKER_FILE = self._orig_file
        serve._REVIEW_TRACKER_LOCKFILE = self._orig_lockfile
        self._tmp.cleanup()

    def _dirs(self):
        return json.loads(self.path.read_text())["discussed_experiment_dirs"]

    def _run_concurrently(self, fn):
        barrier = threading.Barrier(N_WRITERS)
        errors = []

        def worker(i):
            try:
                barrier.wait()
                fn(f"dir_{i:03d}")
            except Exception as exc:  # pragma: no cover - surfaced by the assert
                errors.append(exc)

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(N_WRITERS)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(errors, [], f"worker raised: {errors[:3]}")

    # -- negative control: the bug, reproduced -----------------------------

    def test_unserialised_read_modify_write_loses_updates(self):
        """The OLD shape must actually break here, or the fix proves nothing.

        Measured 2026-09-01 on darwin-arm64 at N_WRITERS=24: the old path both
        LOSES appends (later save overwrites earlier ones) and hands concurrent
        readers a TRUNCATED file -- 16 of 24 workers raised JSONDecodeError from
        `load_review_tracker()` itself, because a bare `write_text` truncates to
        zero before refilling. Both failures are counted here; either one alone
        is sufficient evidence the race is live on this machine.
        """
        read_failures = []

        def old_toggle(dir_name):
            try:
                data = serve.load_review_tracker()      # read
            except Exception as exc:                    # truncated mid-write
                read_failures.append(exc)
                return
            data.setdefault("discussed_experiment_dirs", []).append(dir_name)
            self.path.write_text(json.dumps(data, indent=2) + "\n")  # non-atomic save

        self._run_concurrently(old_toggle)
        try:
            landed = len(self._dirs())
        except Exception:
            # The final file is not even parseable -- concurrent non-atomic writes
            # of differing lengths can leave trailing bytes from a longer payload
            # behind a shorter one ("Extra data"). That is the strongest possible
            # form of the breakage, so it counts as evidence, not as a test error.
            landed = -1
        self.assertTrue(
            landed < N_WRITERS or read_failures,
            "the unserialised path neither lost an update nor tore a read on this "
            "machine -- the positive tests below would then be vacuous; re-check "
            "N_WRITERS before trusting a green run",
        )

    # -- the fix -----------------------------------------------------------

    def test_update_review_tracker_loses_nothing_under_concurrency(self):
        def add(dir_name):
            serve.update_review_tracker(
                lambda d: d.setdefault("discussed_experiment_dirs", []).append(dir_name)
            )

        self._run_concurrently(add)
        dirs = self._dirs()
        self.assertEqual(len(dirs), N_WRITERS)
        self.assertEqual(set(dirs), {f"dir_{i:03d}" for i in range(N_WRITERS)})

    def test_concurrent_add_and_remove_converge(self):
        """Mixed toggles: every add that is not later removed must survive."""
        serve.update_review_tracker(
            lambda d: d.__setitem__("discussed_experiment_dirs",
                                    [f"pre_{i:03d}" for i in range(N_WRITERS)])
        )

        def toggle(dir_name):
            i = int(dir_name.split("_")[1])
            if i % 2:
                serve.update_review_tracker(
                    lambda d: d["discussed_experiment_dirs"].remove(f"pre_{i:03d}")
                )
            else:
                serve.update_review_tracker(
                    lambda d: d["discussed_experiment_dirs"].append(f"new_{i:03d}")
                )

        self._run_concurrently(toggle)
        dirs = set(self._dirs())
        expected = ({f"pre_{i:03d}" for i in range(0, N_WRITERS, 2)}
                    | {f"new_{i:03d}" for i in range(0, N_WRITERS, 2)})
        self.assertEqual(dirs, expected)

    # -- atomicity ----------------------------------------------------------

    def test_save_is_atomic_and_leaves_no_temp_file(self):
        serve.save_review_tracker({"schema_version": "review_tracker/v1",
                                   "reviewed_run_ids": ["r_v3"],
                                   "discussed_experiment_dirs": []})
        self.assertEqual(
            json.loads(self.path.read_text())["reviewed_run_ids"], ["r_v3"])
        self.assertEqual(
            [p.name for p in self.path.parent.glob("*.tmp-*")], [])

    def test_a_reader_never_observes_a_truncated_file(self):
        """A concurrent reader must always parse cleanly.

        The old bare write_text truncates to zero then refills, so a reader
        landing in that window gets invalid JSON. os.replace removes the window.
        """
        serve.update_review_tracker(
            lambda d: d.__setitem__("discussed_experiment_dirs",
                                    [f"d_{i}" for i in range(2000)])
        )
        stop = threading.Event()
        bad = []

        def reader():
            while not stop.is_set():
                try:
                    json.loads(self.path.read_text())
                except Exception as exc:
                    bad.append(exc)
                    return

        r = threading.Thread(target=reader)
        r.start()
        try:
            for i in range(200):
                serve.update_review_tracker(
                    lambda d: d.__setitem__("n", i)
                )
        finally:
            stop.set()
            r.join()
        self.assertEqual(bad, [], f"reader saw a partial file: {bad[:1]}")

    def test_mutator_sees_current_contents_not_a_stale_snapshot(self):
        """Re-reading INSIDE the lock is the half that fixes the lost update."""
        serve.update_review_tracker(
            lambda d: d["discussed_experiment_dirs"].append("first"))
        seen = {}
        serve.update_review_tracker(
            lambda d: seen.setdefault("dirs", list(d["discussed_experiment_dirs"])))
        self.assertEqual(seen["dirs"], ["first"])

    def test_flock_failure_degrades_to_the_in_process_lock(self):
        """Best-effort by design: a filesystem without flock must still write."""
        import fcntl
        orig = fcntl.flock
        fcntl.flock = lambda *a, **k: (_ for _ in ()).throw(OSError("no flock here"))
        try:
            serve.update_review_tracker(
                lambda d: d["discussed_experiment_dirs"].append("degraded"))
        finally:
            fcntl.flock = orig
        self.assertIn("degraded", self._dirs())


if __name__ == "__main__":
    unittest.main(verbosity=2)
