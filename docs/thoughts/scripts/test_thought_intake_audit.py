#!/usr/bin/env python3
"""Regression tests for thought_intake_audit.py's claim-ID recognition.

Confirmed live 2026-08-09: `CLAIM_ID_RE` was hardcoded to
`(?:ARC|MECH|INV|Q|SD)-...` and `_load_claim_ids()`'s own extraction regex
only handled the 2-segment `PREFIX-NUMBER` shape (e.g. MECH-063) -- so a
registered `GOV-FAILLOC-1` claim (claims.yaml's governance_rule IDs are
3-segment, `PREFIX-WORD-NUMBER`) was invisible to BOTH the loader and the
extractor. A Stage 2 thought-intake file naming that ID in its "Candidate
claims" section misclassified as "no_ids_named" (needs a human read) instead
of "all_registered", even though the claim was correctly registered.

Fix: `_load_claim_ids()` now accepts the 3-segment shape too, and the
extraction regex is built at runtime from the PREFIXES actually present in
claims.yaml (`_build_claim_id_re`), rather than a hardcoded alternation --
so a newly-introduced claim_type prefix is recognized the moment its first
claim is registered, with no code change required.

The tests that matter most are the negative controls: a claim-shaped ID that
is NOT in claims.yaml must still classify as missing/orphaned (the fix must
not turn the extractor into a rubber stamp that treats every plausible-shaped
token as registered), and a non-claim hyphenated token using an unregistered
prefix (e.g. an EXQ experiment-queue ID) must not be extracted at all.

Hermetic: every test builds a tmp claims.yaml + tmp thoughts/planning trees
and points main() / the helpers at them directly, so nothing depends on the
real evidence tree.

Run: /opt/local/bin/python3 docs/thoughts/scripts/test_thought_intake_audit.py
"""

import importlib.util
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


M = _load_module("ree_thought_intake_audit", "thought_intake_audit.py")


def _claims_yaml(tmp: Path, ids: list[str]) -> Path:
    path = tmp / "claims.yaml"
    lines = []
    for cid in ids:
        lines.append(f"- id: {cid}")
        lines.append("  title: 'stub'")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


class LoadClaimIdsTests(unittest.TestCase):
    """`_load_claim_ids()` must recognize both real ID shapes."""

    def test_two_segment_ids_still_load(self):
        with tempfile.TemporaryDirectory() as tmp:
            claims = _claims_yaml(Path(tmp), ["MECH-063", "ARC-007", "Q-007", "SD-017", "INV-001"])
            ids = M._load_claim_ids(claims)
            self.assertEqual(
                ids, {"MECH-063", "ARC-007", "Q-007", "SD-017", "INV-001"}
            )

    def test_three_segment_gov_ids_load(self):
        """GOV-WORD-NUMBER (e.g. GOV-FAILLOC-1) is the shape that was invisible."""
        with tempfile.TemporaryDirectory() as tmp:
            claims = _claims_yaml(
                Path(tmp), ["GOV-FAILLOC-1", "GOV-HELDOUT-1", "GOV-V3FREEZE-1"]
            )
            ids = M._load_claim_ids(claims)
            self.assertEqual(
                ids, {"GOV-FAILLOC-1", "GOV-HELDOUT-1", "GOV-V3FREEZE-1"}
            )

    def test_single_and_double_digit_ids_load(self):
        """SENT-0 .. SENT-17 -- not zero-padded to 3 digits like most prefixes."""
        with tempfile.TemporaryDirectory() as tmp:
            claims = _claims_yaml(Path(tmp), ["SENT-0", "SENT-9", "SENT-17"])
            ids = M._load_claim_ids(claims)
            self.assertEqual(ids, {"SENT-0", "SENT-9", "SENT-17"})


class BuildClaimIdReTests(unittest.TestCase):
    """The extraction regex must be derived from claim_ids, not hardcoded."""

    def test_recognizes_a_prefix_not_in_the_old_hardcoded_list(self):
        claim_ids = {"GOV-FAILLOC-1", "IMPL-001", "EXT-001", "RA-001", "SENT-0"}
        pat = M._build_claim_id_re(claim_ids)
        text = "See GOV-FAILLOC-1, IMPL-001, EXT-001, RA-001 and SENT-0 for detail."
        found = set(pat.findall(text))
        self.assertEqual(found, claim_ids)

    def test_does_not_extract_an_unregistered_prefix(self):
        """An EXQ experiment-queue ID must never be mistaken for a claim ID."""
        claim_ids = {"MECH-063"}
        pat = M._build_claim_id_re(claim_ids)
        text = "Superseded by V3-EXQ-603d after MECH-063 landed."
        found = set(pat.findall(text))
        self.assertEqual(found, {"MECH-063"})
        self.assertNotIn("EXQ-603d", found)

    def test_empty_claim_ids_matches_nothing(self):
        pat = M._build_claim_id_re(set())
        self.assertEqual(pat.findall("GOV-FAILLOC-1 MECH-063"), [])

    def test_longest_prefix_does_not_get_shadowed(self):
        """Sorted longest-first: a short prefix must not swallow a longer one's match."""
        claim_ids = {"SD-017", "SDX-001"}
        pat = M._build_claim_id_re(claim_ids)
        found = set(pat.findall("SD-017 and SDX-001 are both cited."))
        self.assertEqual(found, {"SD-017", "SDX-001"})


class ClassifyStage2Tests(unittest.TestCase):
    """The end-to-end classification the chip's worked example depends on."""

    def _classify(self, text, claim_ids):
        pat = M._build_claim_id_re(claim_ids)
        return M._classify_stage2(text, claim_ids, pat)

    def test_registered_gov_id_classifies_all_registered(self):
        """Regression case: this is exactly what misclassified before the fix."""
        claim_ids = {"GOV-FAILLOC-1", "GOV-DIAG-1", "GOV-HELDOUT-1"}
        text = (
            "## Candidate claims\n\n"
            "### GOV-FAILLOC-1 (registered in `claims.yaml`, this session)\n\n"
            "- depends on GOV-DIAG-1 and GOV-HELDOUT-1\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "all_registered")
        self.assertEqual(
            ids_named, ["GOV-DIAG-1", "GOV-FAILLOC-1", "GOV-HELDOUT-1"]
        )
        self.assertEqual(missing, [])

    def test_unregistered_gov_id_classifies_fully_orphaned(self):
        """Negative control: a GOV-shaped ID absent from claims.yaml must still
        be flagged missing -- the fix must not rubber-stamp every GOV-shaped
        token as registered just because the prefix is now recognized."""
        claim_ids = {"GOV-DIAG-1"}  # GOV-NEWTHING-1 deliberately absent
        text = "## Candidate claims\n\n### GOV-NEWTHING-1\n\nproposed here.\n"
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "fully_orphaned")
        self.assertEqual(ids_named, ["GOV-NEWTHING-1"])
        self.assertEqual(missing, ["GOV-NEWTHING-1"])

    def test_no_candidate_section_unaffected(self):
        classification, ids_named, missing = self._classify(
            "Just prose, no candidate header.", {"GOV-DIAG-1"}
        )
        self.assertEqual(classification, "no_candidate_section")
        self.assertEqual(ids_named, [])
        self.assertEqual(missing, [])


class MainEndToEndTests(unittest.TestCase):
    """Full main() over tmp trees -- the worked example from the chip."""

    def test_gov_claim_stage2_file_reports_all_registered(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            thoughts_root = root / "thoughts"
            planning_root = root / "planning"
            thoughts_root.mkdir()
            planning_root.mkdir()
            claims_yaml = _claims_yaml(
                root, ["GOV-FAILLOC-1", "GOV-DIAG-1", "GOV-HELDOUT-1"]
            )
            (planning_root / "thought_intake_2026-08-09_example.md").write_text(
                "## Candidate claims\n\n"
                "### GOV-FAILLOC-1 (registered in `claims.yaml`, this session)\n\n"
                "- depends on GOV-DIAG-1 and GOV-HELDOUT-1\n",
                encoding="utf-8",
            )
            out_json = root / "out.json"
            out_md = root / "out.md"

            argv = [
                "thought_intake_audit.py",
                "--thoughts-root", str(thoughts_root),
                "--planning-root", str(planning_root),
                "--claims-yaml", str(claims_yaml),
                "--output-json", str(out_json),
                "--output-md", str(out_md),
                "--check-clean",
            ]
            old_argv = sys.argv
            sys.argv = argv
            try:
                # --check-clean only raises when something is orphaned/broken;
                # nothing is here, so main() must return normally (exit 0).
                M.main()
            finally:
                sys.argv = old_argv

            report = out_md.read_text(encoding="utf-8")
            self.assertIn("all named candidate IDs registered | 1", report)
            self.assertIn(
                "candidate section present, no IDs named (needs a human read) | 0",
                report,
            )
            self.assertNotIn("thought_intake_2026-08-09_example.md", report.split(
                "### Needs a human read")[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
