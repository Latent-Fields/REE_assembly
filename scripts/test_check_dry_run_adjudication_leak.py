#!/usr/bin/env python3
"""Regression tests for check_dry_run_adjudication_leak.py (GOV-DRY-1).

WHAT THIS PINS
---------------
`scan_citations()` harvested dry run_ids from EVERY string in a confirmed
`failure_autopsy_*.json`, with no distinction between a field that CITES a
dry smoke as evidence and a field that RECORDS that a dry smoke was checked
and correctly excluded. `check_dry_run_citations.py`'s own Step 2a gate
writes exactly that record onto a confirmed artifact -- `excluded_dry_run_ids`
plus a `dry_run_check_note` explaining the exclusion -- so the audit was
flagging its own sibling gate doing its job.

Confirmed false positive, 2026-08-22 (governance cycle bold-chaum-7e245c):
`failure_autopsy_slot_cosine_sim_fanout_sweep_2026-08-13.json` was reported
ACTIONABLE for "citing" DRY `v3_exq_429_inv044_..._20260415T143340Z_v3`, whose
ONLY occurrence in the file is inside `excluded_dry_run_ids` (with
`dry_run_checked: true`) -- not a citation at all.

`test_real_incident_fixture_*` below reproduces that artifact's relevant
shape as a static fixture (not a read of the live repo file, so this test
does not drift when that file is edited or reviewed by a later governance
cycle).

THE NEGATIVE CONTROLS ARE THE LOAD-BEARING HALF: the fix must not swallow a
genuine citation. A dry run_id named in a `target`, `failure_record`, or
ordinary prose/reasoning field must still fire -- the whole point of GOV-DRY-1
is that those citations are dangerous. Roughly half of the tests below assert
exactly that, plus that `substrate_queue.json` scanning (deliberately left
untouched by this fix) still harvests an `excluded_dry_run_ids`-shaped field
literally, since that scan has no equivalent exclusion-record convention.

Run: /opt/local/bin/python3 scripts/test_check_dry_run_adjudication_leak.py
"""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


M = _load_module("ree_check_dry_run_adjudication_leak",
                 "check_dry_run_adjudication_leak.py")

DRY_ID = "v3_exq_429_inv044_bayesian_prior_before_posterior_20260415T143340Z_v3"
DRY = {DRY_ID}
OTHER_DRY_ID = "v3_exq_900_fixture_other_dry_smoke_20260601T010101Z_v3"


class Fixture:
    """A tmp evidence/planning tree of failure_autopsy_*.json files."""

    def __init__(self, root: Path):
        self.planning = root / "evidence" / "planning"
        self.planning.mkdir(parents=True)
        self.queue_path = self.planning / "substrate_queue.json"

    def autopsy(self, slug, data):
        (self.planning / ("failure_autopsy_%s.json" % slug)).write_text(
            json.dumps(data, indent=1))

    def queue(self, data):
        self.queue_path.write_text(json.dumps(data, indent=1))


class CheckDryRunAdjudicationLeakTests(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.fx = Fixture(self.root)

    def scan(self, dry=DRY):
        return M.scan_citations(self.fx.planning, self.fx.queue_path, dry)

    # ---- the fix: exclusion-record fields must not read as citations ------

    def test_real_incident_fixture_exclusion_only_mention_not_flagged(self):
        """Reproduces the confirmed 2026-08-22 false positive verbatim."""
        self.fx.autopsy("slot_cosine_sim_fanout_sweep_2026-08-13", {
            "status": "confirmed",
            "dry_run_checked": True,
            "excluded_dry_run_ids": [DRY_ID],
            "dry_run_check_note": (
                "Step 2a gate run at confirmation over every cited family: "
                "0 dry runs cited. A dry smoke DOES exist in the 429 family "
                "(20260415T143340Z, dry_run true) and is correctly absent "
                "from both this artifact's citations and from "
                "claim_evidence.v1.json."
            ),
        })
        result = self.scan()
        self.assertEqual(result["actionable"], [])
        cited_ids = {r["run_id"] for r in result["actionable"] + result["adjudicated"]}
        self.assertNotIn(DRY_ID, cited_ids)

    def test_dry_run_check_note_alone_not_flagged(self):
        """The exclusion note alone (no excluded_dry_run_ids array) must also
        not read as a citation -- the prose mentions the id by design."""
        self.fx.autopsy("note_only_2026-08-22", {
            "status": "confirmed",
            "dry_run_check_note": "checked family; %s is a dry sibling, correctly excluded" % DRY_ID,
        })
        result = self.scan()
        self.assertEqual(result["actionable"], [])

    def test_excluded_dry_run_ids_alone_not_flagged(self):
        """The array alone (no accompanying note) must also not read as a
        citation."""
        self.fx.autopsy("array_only_2026-08-22", {
            "status": "confirmed",
            "excluded_dry_run_ids": [DRY_ID],
        })
        result = self.scan()
        self.assertEqual(result["actionable"], [])

    def test_two_dry_ids_both_only_in_exclusion_fields_neither_flagged(self):
        two = {DRY_ID, OTHER_DRY_ID}
        self.fx.autopsy("multi_2026-08-22", {
            "status": "confirmed",
            "excluded_dry_run_ids": sorted(two),
            "dry_run_check_note": "both checked and excluded",
        })
        result = self.scan(dry=two)
        self.assertEqual(result["actionable"], [])

    # ---- negative controls: genuine citations must still fire -------------

    def test_target_field_citation_still_flagged(self):
        """NEGATIVE CONTROL: a dry id named in a structured `target`-shaped
        field is a real citation and must still be actionable."""
        self.fx.autopsy("target_hit_2026-08-22", {
            "status": "confirmed",
            "findings": [{"id": "F1", "target": "gate cites %s directly" % DRY_ID}],
        })
        result = self.scan()
        self.assertEqual(len(result["actionable"]), 1)
        self.assertEqual(result["actionable"][0]["run_id"], DRY_ID)

    def test_failure_record_field_citation_still_flagged(self):
        """NEGATIVE CONTROL: the exact field shape of the original 543i
        incident (a `failure_record` prose note) must still fire."""
        self.fx.autopsy("failure_record_hit_2026-08-22", {
            "status": "confirmed",
            "failure_record": ["basin-nondeterminism narrative built on %s" % DRY_ID],
        })
        result = self.scan()
        self.assertEqual(len(result["actionable"]), 1)
        self.assertEqual(result["actionable"][0]["run_id"], DRY_ID)

    def test_ordinary_reasoning_prose_citation_still_flagged(self):
        """NEGATIVE CONTROL: any other free-text field (not one of the two
        exclusion-record field names) is unaffected by skip_keys."""
        self.fx.autopsy("reasoning_hit_2026-08-22", {
            "status": "confirmed",
            "reasoning": "we compared against %s to establish the trend" % DRY_ID,
        })
        result = self.scan()
        self.assertEqual(len(result["actionable"]), 1)
        self.assertEqual(result["actionable"][0]["run_id"], DRY_ID)

    def test_citation_in_both_exclusion_and_target_field_still_flagged(self):
        """NEGATIVE CONTROL: a run_id that is BOTH properly recorded as
        excluded AND separately, genuinely cited elsewhere must still fire --
        the skip only removes the exclusion-record field's own contribution,
        it must not blanket-silence the id for the whole document."""
        self.fx.autopsy("both_2026-08-22", {
            "status": "confirmed",
            "excluded_dry_run_ids": [DRY_ID],
            "dry_run_check_note": "checked and excluded",
            "findings": [{"id": "F1", "target": "but also reasons over %s here" % DRY_ID}],
        })
        result = self.scan()
        self.assertEqual(len(result["actionable"]), 1)
        self.assertEqual(result["actionable"][0]["run_id"], DRY_ID)

    def test_substrate_queue_excluded_dry_run_ids_shaped_field_still_flagged(self):
        """NEGATIVE CONTROL: substrate_queue.json scanning was deliberately
        left untouched -- it has no exclusion-record convention, so even a
        field literally named `excluded_dry_run_ids` there must still be
        harvested as a citation."""
        self.fx.queue({"excluded_dry_run_ids": [DRY_ID]})
        result = self.scan()
        self.assertEqual(len(result["actionable"]), 1)
        self.assertEqual(result["actionable"][0]["run_id"], DRY_ID)
        self.assertEqual(result["actionable"][0]["kind"], "substrate_queue")

    def test_unconfirmed_status_still_ignored(self):
        """REGRESSION (pre-existing behavior, unaffected by this fix): a
        non-confirmed autopsy is never scanned at all."""
        self.fx.autopsy("draft_2026-08-22", {
            "status": "draft",
            "findings": [{"id": "F1", "target": "cites %s" % DRY_ID}],
        })
        result = self.scan()
        self.assertEqual(result["actionable"], [])
        self.assertEqual(result["adjudicated"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
