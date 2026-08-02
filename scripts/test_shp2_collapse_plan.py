#!/usr/bin/env python3
"""Regression test for shp2_collapse_plan.py's duplicate live:/join: bug.

Confirmed 2026-08-02 on commitment_closure:GAP-4-battery: this node carried
BOTH a legacy `owner_exq:` blob (so `has_blob=True`, the "not yet collapsed"
branch) AND an already-present, STALE `live:`/`join:` block -- a half-migrated
leftover from an earlier partial collapse attempt. The collapse code's
`has_blob` check only ever looked for the three blob fields (`_BLOB_RE`), not
for whether a live:/join: span already existed too, so the stale span survived
untouched in `kept` and the fresh block got inserted right after severity,
producing a SECOND `live:`/`join:` pair. `yaml.safe_load` silently resolves a
duplicate key to whichever occurs LAST, so the "stored" value the drift check
(check_closure_drift.py, gate 4 of shp2_collapse_and_verify.py) read back was
the orphaned STALE block, not the fresh one collapse had just written --
gate 4 kept reporting drift immediately after a fresh collapse, with no way to
converge by re-running it.

Live reproduction + fix verification (2026-08-02, session insights-34f9b4):
running `shp2_collapse_and_verify.py --plan commitment_closure_plan.md` before
this fix produced exactly this duplicate (two `live:` blocks, gate4 FAIL
"status-plane drift 1/99"); after this fix, one `live:` block per node and
gate4 "status-plane drift 0/99", all 5 gates green.

Run: /opt/local/bin/python3 scripts/test_shp2_collapse_plan.py
"""

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# The exact shape confirmed on commitment_closure:GAP-4-battery: a node with a
# STALE live:/join: block (right after severity) AND a legacy owner_exq blob
# further down (making has_blob=True).
_MIXED_NODE_LINES = [
    '    - id: "commitment_closure:GAP-4-battery"',
    '      title: "some title"',
    '      status: in_progress',
    '      severity: medium',
    '      live:',
    '        as_of: "2026-07-10"',
    '        from: "failure_autopsy_V3-EXQ-732_2026-07-10"',
    '        verdict: "non_contributory/precondition_unmet"',
    '        next: "routing=queue-experiment"',
    '        brake: "fired"',
    '        needs_review: true',
    '        needs_review_reasons: ["newest_forward_predates_later_manifest+measurement_event(s)"]',
    '      join:',
    '        bears_on: ["f_dominance_conversion_ceiling"]',
    '        scope_claims: ["SD-034"]',
    '      unblocks_claims: [SD-034]',
    '      last_updated: 2026-07-24',
    '      owner_exq: "V3-EXQ-629c queued 2026-07-21"',
    '      resume_condition: "some free text"',
]

# The ordinary (not yet collapsed, no stale live:/join: leftover) shape --
# every other node in the corpus before it is ever touched by collapse.
_ORDINARY_UNCOLLAPSED_NODE_LINES = [
    '    - id: "some_plan:NODE"',
    '      title: "some title"',
    '      status: in_progress',
    '      severity: medium',
    '      last_updated: 2026-07-24',
    '      owner_exq: "V3-EXQ-100 queued"',
]


class KeptLinesForCollapseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module("ree_shp2_collapse_plan", "shp2_collapse_plan.py")

    def test_strips_both_the_blob_and_the_stale_live_join_span(self):
        kept = self.mod._kept_lines_for_collapse(_MIXED_NODE_LINES)
        joined = "\n".join(kept)
        self.assertNotIn("owner_exq:", joined)
        self.assertNotIn("live:", joined)
        self.assertNotIn("join:", joined)
        self.assertNotIn("failure_autopsy_V3-EXQ-732", joined)  # the stale content specifically

    def test_kept_lines_preserve_non_blob_non_live_fields(self):
        kept = self.mod._kept_lines_for_collapse(_MIXED_NODE_LINES)
        joined = "\n".join(kept)
        self.assertIn('id: "commitment_closure:GAP-4-battery"', joined)
        self.assertIn("title:", joined)
        self.assertIn("unblocks_claims:", joined)
        self.assertIn("resume_condition:", joined)

    def test_no_regression_on_ordinary_uncollapsed_node(self):
        """A node with no pre-existing live:/join: block (the normal shape for
        a not-yet-collapsed node) must be unaffected -- only the blob is
        stripped, nothing else changes."""
        kept = self.mod._kept_lines_for_collapse(_ORDINARY_UNCOLLAPSED_NODE_LINES)
        joined = "\n".join(kept)
        self.assertNotIn("owner_exq:", joined)
        self.assertIn('id: "some_plan:NODE"', joined)
        self.assertIn("last_updated:", joined)

    def test_inserting_fresh_block_after_the_fix_yields_exactly_one_live_key(self):
        """End-to-end within the pure helper: simulate the caller's insert-after-
        severity step on the MIXED node and confirm exactly one `live:` (and one
        `join:`) line survives -- the actual defect was a SECOND live:/join:
        pair appearing after insertion."""
        kept = self.mod._kept_lines_for_collapse(_MIXED_NODE_LINES)
        anchor = next(i for i, nl in enumerate(kept) if nl.strip().startswith("severity:"))
        fresh_block = [
            "      live:",
            '        as_of: "2026-08-02"',
            '        from: "failure_autopsy_V3-EXQ-871_2026-08-02"',
            '        verdict: "non_contributory/measurement_test_design_defect"',
            '        next: "routing=queue-experiment"',
            '        brake: "fired"',
            "        needs_review: false",
            "      join:",
            '        bears_on: ["f_dominance_conversion_ceiling"]',
            '        scope_claims: ["SD-034"]',
        ]
        new_node = kept[:anchor + 1] + fresh_block + kept[anchor + 1:]
        n_live = sum(1 for nl in new_node if nl == "      live:")
        n_join = sum(1 for nl in new_node if nl == "      join:")
        self.assertEqual(n_live, 1)
        self.assertEqual(n_join, 1)
        # And the surviving live: block is the FRESH one, not the stale one.
        joined = "\n".join(new_node)
        self.assertIn("failure_autopsy_V3-EXQ-871_2026-08-02", joined)
        self.assertNotIn("failure_autopsy_V3-EXQ-732_2026-07-10", joined)


if __name__ == "__main__":
    unittest.main()
