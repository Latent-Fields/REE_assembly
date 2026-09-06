#!/usr/bin/env python3
"""Regression tests for thought_sweep.py's back-link recognition.

Measured 2026-09-04: the sweep reported ``processed_missing_links=53`` because
``_extract_processed_links()`` recognised only the legacy ``Processed in:``
bullet block, while ~60 processed raw thoughts carry the newer header form
(``Status: processed`` + ``Intake: <path>``), a bold ``**Intake:**`` variant,
YAML frontmatter (``intake:`` / ``related_claims:``), or a ``Superseded by:``
header standing in for an intake. Every one of those was a false "missing
link". The fix recognises all four forms and records which one matched as
``link_form`` (``legacy | intake_header | frontmatter | superseded | none``).

The negative controls matter most: a processed file with NONE of the forms
must still report as missing (``link_form == "none"``), ``Intake class:`` /
``Thought Intake:`` prose must not be read as a back-link, and the report
files that live beside the thoughts (``INTAKE_AUDIT_REPORT.md``,
``SWEEP_REPORT.md``) must not be swept as thoughts at all.

Hermetic: every test builds a tmp thoughts tree. This file lives in
REE_assembly, so the umbrella ``run_scripts_tests.sh`` corpus never sees it.

Run: /opt/local/bin/python3 -m pytest docs/thoughts/scripts/test_thought_sweep.py -q
  or /opt/local/bin/python3 docs/thoughts/scripts/test_thought_sweep.py
"""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
SWEEP_PATH = SCRIPTS_DIR / "thought_sweep.py"


def _load_sweep():
    spec = importlib.util.spec_from_file_location("thought_sweep_under_test", SWEEP_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    # Register before exec: the script's dataclass (under ``from __future__
    # import annotations``) resolves its field types via sys.modules.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


sweep = _load_sweep()


LEGACY = """# Old thought

Status: processed

body text

Processed in:
- docs/claims/claims.yaml#MECH-001
- docs/architecture/foo.md
"""

INTAKE_HEADER = """# New thought

Status: processed
Intake: evidence/planning/thought_intake_2026-08-12_example.md
Claims registered: MECH-499, MECH-500

body text
"""

INTAKE_BOLD = """# Milestone

**Date:** 2026-08-04
Status: processed
**Intake:** evidence/planning/thought_intake_2026-08-04_milestone.md
**Registered:** none this pass
"""

FRONTMATTER = """---
title: Motifs
date: 2026-08-23
status: processed
related_claims:
  - SD-091
  - MECH-481
intake: evidence/planning/thought_intake_2026-08-23_motifs.md
claims_registered:
  - SD-101
---

# Motifs

## Intake status
"""

FRONTMATTER_RELATED_ONLY = """---
status: processed
related_claims:
  - SD-091
---

# Body only
"""

FRONTMATTER_STATUS_THEN_HEADER = """---
title: Umpire
status: processed
---

Status: processed
Intake: evidence/planning/thought_intake_2026-08-31_umpire.md
Claims registered: GOV-UMPIRE-1
"""

SUPERSEDED = """REE as a single understandable cognifold

Date: 2026-08-10
Status: processed
Superseded by: docs/thoughts/2026-08-10_canonical.md (canonical
  draft of the same idea)
"""

GENUINE_GAP = """# Gap

Status: processed

Note: Speculative conjecture. No structured intake created.

Intake class: MILESTONE / NOT A NORMAL THOUGHT INTAKE
Thought Intake: Versioned Organisms
"""

UNPROCESSED = """# Fresh

**Status:** thought + experiment seed
"""


def _links(text: str):
    return sweep._extract_processed_links(text.splitlines())


class LinkFormRecognition(unittest.TestCase):
    def test_legacy_block_still_works(self):
        links, form = _links(LEGACY)
        self.assertEqual(form, "legacy")
        self.assertEqual(links, ["docs/claims/claims.yaml#MECH-001", "docs/architecture/foo.md"])

    def test_intake_header(self):
        links, form = _links(INTAKE_HEADER)
        self.assertEqual(form, "intake_header")
        self.assertEqual(links, ["evidence/planning/thought_intake_2026-08-12_example.md"])

    def test_bold_intake_header(self):
        links, form = _links(INTAKE_BOLD)
        self.assertEqual(form, "intake_header")
        self.assertEqual(links, ["evidence/planning/thought_intake_2026-08-04_milestone.md"])

    def test_frontmatter_intake_and_claims(self):
        links, form = _links(FRONTMATTER)
        self.assertEqual(form, "frontmatter")
        self.assertIn("evidence/planning/thought_intake_2026-08-23_motifs.md", links)
        self.assertIn("SD-091", links)
        self.assertIn("SD-101", links)

    def test_frontmatter_related_claims_alone_counts(self):
        links, form = _links(FRONTMATTER_RELATED_ONLY)
        self.assertEqual(form, "frontmatter")
        self.assertEqual(links, ["SD-091"])

    def test_frontmatter_without_links_falls_through_to_header(self):
        links, form = _links(FRONTMATTER_STATUS_THEN_HEADER)
        self.assertEqual(form, "intake_header")
        self.assertEqual(links, ["evidence/planning/thought_intake_2026-08-31_umpire.md"])

    def test_superseded_by(self):
        links, form = _links(SUPERSEDED)
        self.assertEqual(form, "superseded")
        self.assertEqual(links, ["docs/thoughts/2026-08-10_canonical.md"])

    def test_legacy_wins_when_both_present(self):
        links, form = _links(INTAKE_HEADER + "\n" + LEGACY.split("body text", 1)[1])
        self.assertEqual(form, "legacy")
        self.assertEqual(len(links), 2)

    def test_genuine_gap_is_none(self):
        # Negative control: "Intake class:" and "Thought Intake:" are prose, not links.
        links, form = _links(GENUINE_GAP)
        self.assertEqual(form, "none")
        self.assertEqual(links, [])

    def test_status_detection_unchanged(self):
        self.assertEqual(sweep._extract_status(INTAKE_HEADER.splitlines()), "processed")
        self.assertEqual(sweep._extract_status(FRONTMATTER.splitlines()), "processed")
        self.assertEqual(sweep._extract_status(UNPROCESSED.splitlines()), "unprocessed")


class EndToEndSweep(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        files = {
            "2026-01-01_legacy.md": LEGACY,
            "2026-08-12_header.md": INTAKE_HEADER,
            "2026-08-04_bold.md": INTAKE_BOLD,
            "2026-08-23_frontmatter.md": FRONTMATTER,
            "2026-08-31_umpire.md": FRONTMATTER_STATUS_THEN_HEADER,
            "2028-08-10_superseded.md": SUPERSEDED,
            "2026-04-07_gap.md": GENUINE_GAP,
            "2026-09-06_fresh.md": UNPROCESSED,
            "README.md": "# readme\n",
            "SWEEP_REPORT.md": "# Thought Sweep Report\n",
            "INTAKE_AUDIT_REPORT.md": "# Intake audit\n",
        }
        for name, text in files.items():
            (self.root / name).write_text(text, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_reports_are_not_thoughts_and_gaps_are_named(self):
        out_json = self.root / "out.json"
        out_md = self.root / "out.md"
        proc = subprocess.run(
            [sys.executable, str(SWEEP_PATH), "--root", str(self.root),
             "--output-json", str(out_json), "--output-md", str(out_md)],
            capture_output=True, text=True, check=True,
        )
        payload = json.loads(out_json.read_text(encoding="utf-8"))
        names = {r["file"] for r in payload["records"]}
        self.assertNotIn("INTAKE_AUDIT_REPORT.md", names)
        self.assertNotIn("SWEEP_REPORT.md", names)
        self.assertNotIn("README.md", names)
        summary = payload["summary"]
        self.assertEqual(summary["total"], 8)
        self.assertEqual(summary["unprocessed"], 1)
        self.assertEqual(summary["processed_missing_links"], 1)
        self.assertEqual(summary["link_forms"]["legacy"], 1)
        self.assertEqual(summary["link_forms"]["intake_header"], 3)
        self.assertEqual(summary["link_forms"]["frontmatter"], 1)
        self.assertEqual(summary["link_forms"]["superseded"], 1)
        self.assertEqual(summary["link_forms"]["none"], 1)
        by_name = {r["file"]: r for r in payload["records"]}
        self.assertEqual(by_name["2026-04-07_gap.md"]["link_form"], "none")
        self.assertEqual(by_name["2026-08-12_header.md"]["link_form"], "intake_header")
        report = out_md.read_text(encoding="utf-8")
        self.assertIn("- `2026-04-07_gap.md`", report)
        self.assertIn("`2026-09-06_fresh.md` (status=`unprocessed`)", report)
        self.assertIn("processed_missing_links=1", proc.stdout)
        self.assertTrue(proc.stdout.isascii())


if __name__ == "__main__":
    unittest.main()
