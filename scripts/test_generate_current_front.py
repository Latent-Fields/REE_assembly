#!/usr/bin/env python3
"""Unit tests for generate_current_front.py's anchor extraction.

Regression cover for the 2026-07-29..07-31 anchor-drift defect: `/insights`
changed insights_report.md's format to a "clean state, nothing survives the
four gates" narrative (## Recommendations -> **Gate check result: ...**),
dropping the old '### The live front' headline and '## The live campaign'
table entirely. The generator's headline/live-path extraction had no fallback
for that shape, so docs/CURRENT_FRONT.md -- the doc every session is told to
read FIRST -- emitted its own failure banner ("could not derive front
headline") on every regen from 2026-07-29T22:46:51Z onward, because
regeneration reproduces the same drift forever; nothing but a code fix could
close it. Fixed by deriving the headline from the Recommendations section's
own "Gate check result" bold sentence, and the live path from the EXQ ids
named in the already-derived `gate` text, when no separate campaign section
exists.
"""

import importlib.util
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent / "generate_current_front.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("ree_gen_current_front", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CLOSURE_FIXTURE = """Generated: 2026-07-26T00:00:00Z

Weighted progress: **76.2%**
Remaining (unweighted node count): **25**
"""

# Shape confirmed live in insights_report.md as of 2026-07-26: no '### The
# live front' heading and no '## The live campaign' table -- the Recommendations
# section states outright that nothing survives the four gates.
NEW_FORMAT_INSIGHTS = """# Project Insights -- 2026-07-26

Generated: 2026-07-26T13:20:01Z

## Recommendations

**Gate check result: no recommendation survives all four gates.** Specifically:

1. The two most obvious candidate actions from Step 3 -- re-running V3-EXQ-817/819 with corrected objectives/gates -- are **already queued and claimed** (`V3-EXQ-817a`, `V3-EXQ-819a`, both `status: claimed` in the live queue as of this run)
2. No substrate node is ready and unbuilt.
"""

# Shape the generator was originally written against.
OLD_FORMAT_INSIGHTS = """# Project Insights -- 2026-06-01

Generated: 2026-06-01T00:00:00Z

### The live front is MECH-090 vs the F-dominance conversion ceiling

## The live campaign

| Rank | EXQ | Claim |
|---|---|---|
| **V3-EXQ-500** | **1 (lead)** | MECH-090 |
| V3-EXQ-501 | 2 | MECH-091 |

## Recommendations

1. **Queue the MECH-090 discriminator** -- direct F-weight sweep.
"""

NO_ANCHOR_INSIGHTS = """# Project Insights -- 2026-01-01

Generated: 2026-01-01T00:00:00Z

## Some Other Section

Nothing recognizable here at all.
"""


class DeriveTests(unittest.TestCase):
    def setUp(self):
        self.mod = _load_module()

    def _derive_with(self, insights_text, closure_text=CLOSURE_FIXTURE):
        orig_read = self.mod._read
        try:
            self.mod._read = lambda path: (
                insights_text if path == self.mod.INSIGHTS
                else closure_text if path == self.mod.CLOSURE
                else orig_read(path)
            )
            return self.mod.derive()
        finally:
            self.mod._read = orig_read

    def test_new_format_derives_headline_from_gate_check_result(self):
        f, needs_review = self._derive_with(NEW_FORMAT_INSIGHTS)
        self.assertFalse(needs_review, "new-format Recommendations must not trip needs_review")
        self.assertIn("Gate check result", f["headline"])
        self.assertNotIn("could not derive", f["headline"])

    def test_new_format_derives_live_path_from_gate_text(self):
        f, needs_review = self._derive_with(NEW_FORMAT_INSIGHTS)
        self.assertFalse(needs_review)
        self.assertTrue(f["live_path_is_fallback"])
        self.assertIn("V3-EXQ-817a", f["live_path_exqs"])
        self.assertIn("V3-EXQ-819a", f["live_path_exqs"])

    def test_new_format_gate_still_derives(self):
        f, _ = self._derive_with(NEW_FORMAT_INSIGHTS)
        self.assertIn("already queued and claimed", f["gate"])

    def test_old_format_still_derives_headline_and_campaign(self):
        """Backward compatibility: if /insights ever reverts to the original
        campaign-table shape, the original (non-fallback) path must still fire."""
        f, needs_review = self._derive_with(OLD_FORMAT_INSIGHTS)
        self.assertFalse(needs_review)
        self.assertEqual(f["headline"], "The live front is MECH-090 vs the F-dominance conversion ceiling")
        self.assertFalse(f["live_path_is_fallback"])
        self.assertEqual(f["lead_exq"], "V3-EXQ-500")
        self.assertEqual(f["live_path_exqs"][0], "V3-EXQ-500")

    def test_genuinely_missing_anchors_still_flags_needs_review(self):
        """The robustness contract must still hold: a source with NEITHER the
        old campaign shape NOR the new Gate-check-result shape is real drift,
        and must still degrade to the explicit '(could not derive...)' marker
        rather than fabricating content."""
        f, needs_review = self._derive_with(NO_ANCHOR_INSIGHTS)
        self.assertTrue(needs_review)
        self.assertIn("could not derive", f["headline"])
        self.assertEqual(f["live_path_exqs"], [])

    def test_render_marks_fallback_live_path_distinctly(self):
        f, needs_review = self._derive_with(NEW_FORMAT_INSIGHTS)
        text = self.mod.render(f, needs_review, "2026-07-31T00:00:00Z")
        self.assertIn("no separate live-campaign section this snapshot", text)
        self.assertNotIn("needs_review", text)

    def test_render_old_format_does_not_mark_fallback(self):
        f, needs_review = self._derive_with(OLD_FORMAT_INSIGHTS)
        text = self.mod.render(f, needs_review, "2026-07-31T00:00:00Z")
        self.assertNotIn("no separate live-campaign section", text)


if __name__ == "__main__":
    unittest.main()
