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


class EvidenceDomainTests(unittest.TestCase):
    """GOV-JURIS-1 stamp (added 2026-09-16): surfaced verbatim, never derived, never a gate."""

    def setUp(self):
        import tempfile, json as _json
        self.mod = _load_module()
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "current_front_evidence_domain.json"
        self.orig = self.mod.EVIDENCE_DOMAIN
        self.mod.EVIDENCE_DOMAIN = str(self.path)
        self._json = _json

    def tearDown(self):
        self.mod.EVIDENCE_DOMAIN = self.orig
        self.tmp.cleanup()

    def _write(self, obj):
        self.path.write_text(self._json.dumps(obj), encoding="utf-8")

    def _stamp(self, anchor="V3-EXQ-500"):
        return {"front_anchor": anchor, "domain_reached": "D1", "as_of_utc": "2026-09-16",
                "domains_not_tested": ["D2 untested", "D4 one world family"],
                "stochastic_replication": "3 seeds", "world_family_replication": "1 family"}

    def _derive_with(self, insights_text, closure_text=CLOSURE_FIXTURE):
        orig_read = self.mod._read
        try:
            self.mod._read = lambda path: (
                insights_text if path == self.mod.INSIGHTS
                else closure_text if path == self.mod.CLOSURE
                else orig_read(path))
            return self.mod.derive()
        finally:
            self.mod._read = orig_read

    def test_missing_stamp_renders_not_stated_and_does_not_trip_needs_review(self):
        f, needs_review = self._derive_with(OLD_FORMAT_INSIGHTS)
        self.assertFalse(needs_review)
        self.assertEqual(f["evidence_domain"]["status"], "missing")
        text = self.mod.render(f, needs_review, "2026-09-16T00:00:00Z")
        self.assertIn("Evidence domain reached:** NOT STATED", text)
        self.assertIn("GOV-JURIS-1", text)

    def test_stated_stamp_matching_lead_renders_verbatim(self):
        self._write(self._stamp("V3-EXQ-500"))
        f, _ = self._derive_with(OLD_FORMAT_INSIGHTS)
        self.assertEqual(f["lead_exq"], "V3-EXQ-500")
        self.assertEqual(f["evidence_domain"]["status"], "stated")
        text = self.mod.render(f, False, "2026-09-16T00:00:00Z")
        self.assertIn("Evidence domain reached:** D1", text)
        self.assertIn("Domains not tested:** D2 untested; D4 one world family", text)
        self.assertIn("stochastic 3 seeds / world-family 1 family", text)
        self.assertNotIn("STALE", text)

    def test_stamp_against_old_lead_is_marked_stale_not_dropped(self):
        self._write(self._stamp("V3-EXQ-499"))
        f, _ = self._derive_with(OLD_FORMAT_INSIGHTS)
        self.assertEqual(f["evidence_domain"]["status"], "stale")
        text = self.mod.render(f, False, "2026-09-16T00:00:00Z")
        self.assertIn("Evidence domain reached:** D1", text)
        self.assertIn("**STALE**", text)
        self.assertIn("V3-EXQ-500", text)

    def test_malformed_stamp_renders_not_stated_with_reason(self):
        self.path.write_text("{not json", encoding="utf-8")
        f, _ = self._derive_with(OLD_FORMAT_INSIGHTS)
        self.assertEqual(f["evidence_domain"]["status"], "malformed")
        text = self.mod.render(f, False, "2026-09-16T00:00:00Z")
        self.assertIn("NOT STATED (malformed stamp", text)
        self._write({"front_anchor": "V3-EXQ-500"})  # missing required keys
        f, _ = self._derive_with(OLD_FORMAT_INSIGHTS)
        self.assertEqual(f["evidence_domain"]["status"], "malformed")

    def test_no_derivable_lead_shows_stamp_as_stated_not_stale(self):
        """Staleness needs a lead to compare against; with none derivable the stamp
        is shown as written rather than falsely flagged."""
        self._write(self._stamp("V3-EXQ-500"))
        f, needs_review = self._derive_with(NO_ANCHOR_INSIGHTS)
        self.assertTrue(needs_review)
        self.assertEqual(f["evidence_domain"]["status"], "stated")


if __name__ == "__main__":
    unittest.main()
