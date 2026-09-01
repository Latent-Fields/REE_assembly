#!/usr/bin/env python3
"""Unit tests for scripts/fleet_status_client.py -- the FAILURE contract.

The module's whole job is "never raise, return None on ANY failure" so the
five telemetry consumers migrated to coordinator-primary reads (2026-09-01)
always fall back to the frozen git heartbeat/status files instead of
crashing a governance generator. These tests pin that contract:

  * missing config file (bogus REE_COORDINATOR_CLIENT_CONFIG path) -> None
  * unparseable config / non-dict config / missing url or token -> None
  * unreachable coordinator url -> None (no exception escapes)
  * non-dict response payload -> None
  * good payload -> machine_rows keyed by machine, junk rows skipped
  * process-lifetime cache: failure is memoised; refresh=True bypasses

No test touches the network beyond a connect to 127.0.0.1:9 (closed port,
fails fast) and none reads the real ~/.ree_coordinator_client.json.
"""

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent / "fleet_status_client.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("ree_fleet_status", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FleetStatusClientFailurePaths(unittest.TestCase):
    def setUp(self):
        self._saved_env = os.environ.get("REE_COORDINATOR_CLIENT_CONFIG")
        self.mod = _load_module()  # fresh module (and fresh cache) per test

    def tearDown(self):
        if self._saved_env is None:
            os.environ.pop("REE_COORDINATOR_CLIENT_CONFIG", None)
        else:
            os.environ["REE_COORDINATOR_CLIENT_CONFIG"] = self._saved_env

    def _point_config_at(self, path):
        os.environ["REE_COORDINATOR_CLIENT_CONFIG"] = str(path)

    def test_missing_config_file_returns_none(self):
        self._point_config_at("/nonexistent/definitely/not/a/config.json")
        self.assertIsNone(self.mod.load_client_config())
        self.assertIsNone(self.mod.fetch_shadow_status(refresh=True))
        self.assertIsNone(self.mod.machine_rows(refresh=True))

    def test_unparseable_config_returns_none(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as fh:
            fh.write("{not json")
            path = fh.name
        try:
            self._point_config_at(path)
            self.assertIsNone(self.mod.load_client_config())
            self.assertIsNone(self.mod.fetch_shadow_status(refresh=True))
        finally:
            os.unlink(path)

    def test_non_dict_config_returns_none(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as fh:
            json.dump(["not", "a", "dict"], fh)
            path = fh.name
        try:
            self._point_config_at(path)
            self.assertIsNone(self.mod.load_client_config())
        finally:
            os.unlink(path)

    def test_config_missing_url_or_token_returns_none(self):
        for cfg in ({"token": "t"}, {"url": "http://127.0.0.1:9"}, {}):
            with tempfile.NamedTemporaryFile("w", suffix=".json",
                                             delete=False) as fh:
                json.dump(cfg, fh)
                path = fh.name
            try:
                self._point_config_at(path)
                self.assertIsNone(
                    self.mod.fetch_shadow_status(refresh=True), cfg)
            finally:
                os.unlink(path)

    def test_unreachable_url_returns_none_without_raising(self):
        # Port 9 (discard) is closed on loopback -> connection refused fast.
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as fh:
            json.dump({"url": "http://127.0.0.1:9", "token": "t"}, fh)
            path = fh.name
        try:
            self._point_config_at(path)
            self.assertIsNone(self.mod.fetch_shadow_status(
                timeout=0.5, refresh=True))
            self.assertIsNone(self.mod.machine_rows(
                timeout=0.5, refresh=True))
        finally:
            os.unlink(path)

    def test_non_dict_payload_returns_none(self):
        self.mod._fetch = lambda timeout: None  # simulates parse-level failure
        self.assertIsNone(self.mod.fetch_shadow_status(refresh=True))

    def test_machine_rows_parses_good_payload_and_skips_junk(self):
        payload = {"machines": [
            {"machine": "ree-cloud-2", "state": "running",
             "current_exq": "V3-EXQ-999", "last_seen": "2026-09-01T00:00:00Z"},
            {"machine": "", "state": "idle"},        # unnamed -> skipped
            {"state": "idle"},                       # no machine key -> skipped
            "junk-not-a-dict",                       # wrong type -> skipped
        ]}
        self.mod._fetch = lambda timeout: payload
        rows = self.mod.machine_rows(refresh=True)
        self.assertEqual(set(rows), {"ree-cloud-2"})
        self.assertEqual(rows["ree-cloud-2"]["current_exq"], "V3-EXQ-999")

    def test_payload_without_machines_yields_empty_dict_not_none(self):
        self.mod._fetch = lambda timeout: {"something_else": 1}
        self.assertEqual(self.mod.machine_rows(refresh=True), {})

    def test_failure_is_cached_and_refresh_bypasses(self):
        calls = []

        def fake_fetch(timeout):
            calls.append(timeout)
            return None

        self.mod._fetch = fake_fetch
        self.assertIsNone(self.mod.fetch_shadow_status(refresh=True))
        self.assertIsNone(self.mod.fetch_shadow_status())  # cached, no refetch
        self.assertEqual(len(calls), 1)
        self.mod.fetch_shadow_status(refresh=True)
        self.assertEqual(len(calls), 2)


if __name__ == "__main__":
    unittest.main()
