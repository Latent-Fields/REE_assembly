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


class IncidentalIdMaskingTests(unittest.TestCase):
    """Regression tests for the per-candidate-item split (chip
    chip-20260809-intake-audit-incidental-id-masking).

    Confirmed live 2026-08-07/09 on
    thought_intake_2026-04-16_language_lateralisation.md: a "Candidate
    claims" section can list SEVERAL distinct candidates as top-level bullet
    or numbered items, some carrying no ID at all and some incidentally
    citing an unrelated, already-registered ID in passing prose (e.g.
    "overlaps ARC-009; fold in rather than duplicate"). The old flat,
    whole-section regex scan found that one registered ID anywhere in the
    section and called the whole file all_registered, silently masking the
    unregistered siblings. `_split_candidate_items` fixes this by checking
    each top-level candidate item independently.
    """

    def _classify(self, text, claim_ids):
        pat = M._build_claim_id_re(claim_ids)
        return M._classify_stage2(text, claim_ids, pat)

    def test_mixed_registered_and_prose_only_candidates_not_all_registered(self):
        """The exact language_lateralisation.md shape: three bullet
        candidates, none with its own ID, one of them incidentally citing an
        already-registered ARC-009 in an aside. Must NOT be all_registered."""
        claim_ids = {"ARC-009"}
        text = (
            "## 3. Candidate claims\n\n"
            "- **Candidate ARC** (language.routing_vs_affect_separation) -- dorsal "
            "high-fidelity structured routing is architecturally distinct from the "
            "affective-coupling system. *[integrates existing pieces]*\n"
            "- **Candidate MECH** (affect.bilateral_right_biased_coupling) -- affective "
            "coupling runs on bilateral temporal-limbic circuits. *[lit-pull first]*\n"
            "- **Candidate HYP** (language.emerges_from_social_latent_compression) -- "
            "language emerges where socially-derived latents are compressed. "
            "*[overlaps ARC-009; fold in rather than duplicate]*\n\n"
            "## 4. Affected existing claims / docs\n\n"
            "- ARC-010, language architecture docs.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertNotEqual(classification, "all_registered")
        self.assertEqual(classification, "partially_unlabeled")
        self.assertEqual(ids_named, ["ARC-009"])
        self.assertEqual(missing, [])

    def test_every_item_carrying_its_own_id_stays_all_registered(self):
        """Negative control: a section with MULTIPLE top-level bullet items
        where every single one names its own registered ID must still
        classify all_registered -- the fix must not turn per-item splitting
        into a source of new false positives."""
        claim_ids = {"ARC-034", "MECH-127", "Q-023"}
        text = (
            "## Candidate claims\n\n"
            "- **ARC-034** -- ethics testing requires nth-order trajectory integration.\n"
            "- **MECH-127** -- counterfactual other-cost-aversion as motivational surrogate.\n"
            "- **Q-023** -- formal convergence characterization for ethical attractors.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "all_registered")
        self.assertEqual(ids_named, ["ARC-034", "MECH-127", "Q-023"])
        self.assertEqual(missing, [])

    def test_every_item_carrying_its_own_id_via_subheaders_stays_all_registered(self):
        """Negative control for the OTHER structuring convention (deeper
        sub-headers, not bullets) -- same requirement as above."""
        claim_ids = {"ARC-034", "MECH-127"}
        text = (
            "## Candidate Claims\n\n"
            "### MECH-127: Counterfactual other-cost-aversion\n\n"
            "Description here.\n\n"
            "### ARC-034: Ethics testing scope\n\n"
            "Description here, related: INV-001 (unregistered cross-ref, ignored since "
            "this item already carries its own id).\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "all_registered")
        self.assertEqual(ids_named, ["ARC-034", "MECH-127"])
        self.assertEqual(missing, [])

    def test_section_with_zero_id_tokens_at_all_stays_no_ids_named(self):
        """Negative control: a section with NO claim-shaped ID anywhere
        (the pre-existing no_ids_named path) must be unaffected by the
        per-item split -- there is nothing to split against in the first
        place since ids_named is empty before the split is even attempted."""
        claim_ids = {"ARC-009"}
        text = (
            "## Candidate claims\n\n"
            "- **Candidate ARC** (some.dotted.label) -- a prose-only candidate.\n"
            "- **Candidate MECH** (another.dotted.label) -- another prose-only candidate.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "no_ids_named")
        self.assertEqual(ids_named, [])
        self.assertEqual(missing, [])

    def test_partially_registered_unaffected_by_item_split(self):
        """When some named IDs are already missing, the file is already
        correctly flagged (partially_registered) -- the item-split override
        only applies on the all_registered branch, so this must be
        unchanged regardless of per-item structure.

        claim_ids deliberately includes a registered MECH-001 (distinct from
        the MECH-999 the section names) so the MECH prefix is recognized by
        the extraction regex at all -- otherwise MECH-999 would never be
        extracted in the first place and this test would exercise nothing.
        """
        claim_ids = {"ARC-009", "MECH-001"}
        text = (
            "## Candidate claims\n\n"
            "- **ARC-009** -- already registered.\n"
            "- **MECH-999** -- not registered anywhere.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "partially_registered")
        self.assertEqual(ids_named, ["ARC-009", "MECH-999"])
        self.assertEqual(missing, ["MECH-999"])

    def test_cross_ref_only_items_still_flagged_even_when_every_item_cites_one(self):
        """The harder case, confirmed 2026-08-09 on
        thought_intake_2026-06-23_language_as_cooperation_interface.md: EVERY
        item cites at least one already-registered id as a "Cross-ref:", so a
        naive "does this item contain any id token" check finds one in every
        item and never flags the section -- even though none of the three
        candidates has actually been minted its own new id. The self-id
        check must look only at each item's leading label, not its whole
        body, to catch this."""
        claim_ids = {"ARC-009", "MECH-192"}
        text = (
            "## Candidate claims\n\n"
            "1. **Message selection minimises the receiver's residual uncertainty.** "
            "*Candidate, architectural.* Some falsifier text. *Cross-ref:* ARC-009, MECH-192.\n"
            "2. **Worldly reference is inherited through the world model.** "
            "*Candidate, architectural.* Some falsifier text. *Cross-ref:* ARC-009.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "partially_unlabeled")
        self.assertEqual(ids_named, ["ARC-009", "MECH-192"])
        self.assertEqual(missing, [])

    def test_own_id_inside_label_span_still_recognized(self):
        """Negative control for the label-scoping refinement: an item whose
        OWN id is genuinely inside its leading bold/backtick label (not just
        cited later) must still count as labeled, even alongside a sibling
        item that only cites cross-refs."""
        claim_ids = {"MECH-364", "ARC-009"}
        text = (
            "## Candidate claims\n\n"
            "- **MECH-364** (REGISTERED) -- discharges accumulated load.\n"
            "- **A prose-only candidate with no id of its own.** *Cross-ref:* ARC-009.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "partially_unlabeled")
        self.assertEqual(ids_named, ["ARC-009", "MECH-364"])

    def test_dotted_namespace_label_with_amend_target_still_flagged(self):
        """The agent_memory_consolidation_faults.md shape: the item's own
        label is a backtick dotted-namespace string with no id, and the
        registered id appears only in a parenthetical "likely amend X" aside
        immediately after the label -- must still be flagged as un-ID'd."""
        claim_ids = {"ARC-020", "MECH-094"}
        text = (
            "## Candidate claims\n\n"
            "1. **`memory.consolidation.raw_episode_preservation`** (candidate invariant "
            "or amend ARC-020/MECH-094): a consolidated abstraction must retain a pointer "
            "to its source episodes.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "partially_unlabeled")
        self.assertEqual(ids_named, ["ARC-020", "MECH-094"])

    def test_no_item_structure_falls_back_to_flat_section_unchanged(self):
        """A candidate section with no bullets, no numbered items, and no
        deeper sub-headers (a single prose paragraph naming one registered
        ID) has nothing for `_split_candidate_items` to split -- it must
        fall back to the pre-fix flat-section verdict, not spuriously flag
        partially_unlabeled just because "no items" trivially contains an
        unlabeled reading."""
        claim_ids = {"ARC-009"}
        text = (
            "## Candidate claims\n\n"
            "A single prose paragraph discussing ARC-009 with no list "
            "structure and no sub-headers at all.\n"
        )
        classification, ids_named, missing = self._classify(text, claim_ids)
        self.assertEqual(classification, "all_registered")
        self.assertEqual(ids_named, ["ARC-009"])
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
                "candidate section present, no IDs named or a sibling candidate "
                "is un-ID'd (needs a human read) | 0",
                report,
            )
            self.assertNotIn("thought_intake_2026-08-09_example.md", report.split(
                "### Needs a human read")[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
