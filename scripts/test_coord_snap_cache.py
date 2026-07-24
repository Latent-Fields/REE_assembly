#!/usr/bin/env python3
"""Unit tests for coordinator snapshot cache fallback in serve.py."""

import importlib.util
import sys
import time
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SERVE_PATH = REPO_ROOT / "serve.py"

# serve.py does `import graceful_timeout` at module scope; that module lives in
# REPO_ROOT, not scripts/. Running this file as `python3 scripts/test_coord_snap_cache.py`
# puts scripts/ (not REPO_ROOT) at sys.path[0], so serve.py's import fails unless
# REPO_ROOT is on sys.path before it is loaded via spec_from_file_location below.
sys.path.insert(0, str(REPO_ROOT))


def _load_serve():
    spec = importlib.util.spec_from_file_location("ree_serve", SERVE_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class CoordSnapCacheTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.serve = _load_serve()

    def setUp(self):
        with self.serve._COORD_SNAP_LOCK:
            self.serve._COORD_SNAP_CACHE.clear()
            self.serve._COORD_SNAP_CACHE.update({
                "t": 0.0,
                "ok": False,
                "data": {},
                "last_good": {"ree-cloud-2": {"state": "running"}},
                "last_good_t": time.monotonic(),
            })

    def test_failure_returns_last_good(self):
        cfg = {"COORDINATOR_URL": "http://10.0.0.1:8787",
               "COORDINATOR_LOCAL_TOKEN": "tok"}
        with mock.patch("urllib.request.urlopen", side_effect=OSError("down")):
            out = self.serve._fetch_coordinator_machine_snapshots(cfg)
        self.assertEqual(out, {"ree-cloud-2": {"state": "running"}})

    def test_success_updates_cache(self):
        cfg = {"COORDINATOR_URL": "http://10.0.0.1:8787",
               "COORDINATOR_LOCAL_TOKEN": "tok"}
        payload = b'{"machines": [{"machine": "ree-cloud-3", "state": "idle"}]}'

        class _Resp:
            def read(self):
                return payload

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        with mock.patch("urllib.request.urlopen", return_value=_Resp()):
            out = self.serve._fetch_coordinator_machine_snapshots(cfg)
        self.assertIn("ree-cloud-3", out)
        self.assertEqual(out["ree-cloud-3"]["state"], "idle")


if __name__ == "__main__":
    unittest.main()
