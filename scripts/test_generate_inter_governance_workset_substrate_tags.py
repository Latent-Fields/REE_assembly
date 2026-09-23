#!/usr/bin/env python3
"""Regression tests for GFLAG-0254 -- the GOV-CONFIRM-1 'is this claim built?'
detector counted a claim id found ONLY in comment prose as built substrate.

THE DEFECT. `_claims_implemented_in_substrate` regex-scanned the RAW text of
every ree-v3/ree_core .py, so a comment recording ABSENCE made its claim
'built'. The motivating instance (GFLAG-0219 -> GFLAG-0254): until ree-v3
7642cd1 the only MECH-057b string in ree_core was config.py's

    # EXQ-048/049 confirmed: beta gate never elevated, MECH-057b/090 could not be tested.)

and the confirmer lane offered MECH-057b as 'built substrate (tagged in ree_core)'.

WHY NOT 'IGNORE COMMENTS AND DOCSTRINGS'. Measured on the live tree
2026-09-23: docstrings and comment headers ARE the REE tagging convention.
Stripping both took the tagged set from 316 ids to 35 (every code-string hit),
i.e. it would have turned ~280 true 'built' verdicts false. The fix keeps
string constants (docstrings included) and comment TAG HEADERS
(`# MECH-463: ...`), and splits prose-only mentions into a separate
cannot-determine set that the confirmer lane renders `blocked`, not `ready`
and not dropped. On the live tree that moved 11 of 304 claims.yaml ids
from built to mention-only (MECH-191, MECH-329, MECH-022, MECH-173, MECH-447,
INV-086 are absence/incidental notes; MECH-074, MECH-023, INV-023, MECH-230,
MECH-233 are real substrate named mid-sentence -- hence blocked, not dropped).

The blind-spot check: `CommentOnlyMentionTest` FAILS against the pre-fix
generator (REE_assembly a343c7e2a70) and passes after; `RealTagsStillCountTest`
passes on both.

Hermetic apart from `LiveTreeCanaryTest`, which is skipped when ree_core is
absent (cloud boxes without a ree-v3 checkout).

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_substrate_tags.py
"""

import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_generator():
    path = Path(os.environ.get("IGW_GENERATOR_UNDER_TEST")
                or SCRIPTS_DIR / "generate_inter_governance_workset.py")
    spec = importlib.util.spec_from_file_location(
        "ree_igw_generator_substrate_tags_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


G = _load_generator()


# Verbatim from ree-v3 ree_core/utils/config.py (pre-7642cd1 the only MECH-057b hit).
ABSENCE_COMMENT_SRC = '''\
class E3Config:
    commitment_threshold: float = 0.40
    # (Prior value 0.003 was 25,000x below actual running_variance -> never committed.
    # EXQ-048/049 confirmed: beta gate never elevated, MECH-057b/090 could not be tested.)
    #
'''

# Mid-prose mentions from the live tree that record gaps / other experiments.
PROSE_MENTIONS_SRC = '''\
def select():
    # consuming Linear collapses it -- the MECH-191 phasic-externalisation gap),
    # that self-routed substrate_not_ready_requeue and left MECH-329 / MECH-189
    return 0
'''

DOCSTRING_TAG_SRC = '''\
def completion_confidence(self):
    """MECH-057b: sequence-completion verification confidence for one
    candidate trajectory."""
    return 0.0
'''

COMMENT_HEADER_SRC = '''\
x = 1  # SD-057 phase-2 L7 (MECH-348): dACC object-discriminative goal readout
# MECH-463: per-candidate [K] channel-bias tensors retained UNREDUCED
# SD-016: frontal cue-indexed integration (MECH-150/151/152, ARC-041).
y = 2
'''

CODE_STRING_SRC = '''\
OWNING_CLAIM = "MECH-900"
REGISTRY = {"channel": "ARC-900"}
'''


class _TreeFixture(unittest.TestCase):
    """Point REE_V3_CORE at a tempdir tree built from fixture sources."""

    FILES: dict = {}

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.core = Path(self._tmp.name) / "ree_core"
        self.core.mkdir()
        for name, src in self.FILES.items():
            p = self.core / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(src, encoding="utf-8")
        self._orig_core = G.REE_V3_CORE
        G.REE_V3_CORE = self.core

    def tearDown(self):
        G.REE_V3_CORE = self._orig_core
        self._tmp.cleanup()

    def built(self):
        return G._claims_implemented_in_substrate()


class CommentOnlyMentionTest(_TreeFixture):
    """THE DEFECT. Must FAIL on the pre-fix generator."""

    FILES = {"utils/config.py": ABSENCE_COMMENT_SRC,
             "agent.py": PROSE_MENTIONS_SRC}

    def test_absence_comment_does_not_make_mech_057b_built(self):
        self.assertNotIn("MECH-057b", self.built())

    def test_mid_prose_gap_mentions_are_not_built(self):
        built = self.built()
        for cid in ("MECH-191", "MECH-329", "MECH-189"):
            self.assertNotIn(cid, built)


class RealTagsStillCountTest(_TreeFixture):
    """The non-vacuity half: real tags must keep counting (passes on old code
    too -- it guards the fix from over-correcting into an empty set)."""

    FILES = {"hippocampal/module.py": DOCSTRING_TAG_SRC,
             "predictors/e3_selector.py": COMMENT_HEADER_SRC,
             "registry.py": CODE_STRING_SRC}

    def test_docstring_tag_counts(self):
        self.assertIn("MECH-057b", self.built())

    def test_comment_tag_headers_count(self):
        built = self.built()
        for cid in ("MECH-348", "SD-057", "MECH-463", "SD-016", "ARC-041"):
            self.assertIn(cid, built)

    def test_code_string_constants_count(self):
        built = self.built()
        self.assertIn("MECH-900", built)
        self.assertIn("ARC-900", built)


class RealTagsAreNotMentionOnlyTest(RealTagsStillCountTest.__base__):
    FILES = RealTagsStillCountTest.FILES

    def test_nothing_here_is_mention_only(self):
        self.assertEqual(set(), G._claims_mentioned_only_in_substrate())


class MentionOnlyCategoryTest(_TreeFixture):
    """Prose-only mentions are a cannot-determine category, not silently lost."""

    FILES = {"utils/config.py": ABSENCE_COMMENT_SRC,
             "agent.py": PROSE_MENTIONS_SRC,
             "hippocampal/module.py": DOCSTRING_TAG_SRC}

    def test_prose_only_ids_are_reported_mention_only(self):
        mo = G._claims_mentioned_only_in_substrate()
        self.assertTrue({"MECH-191", "MECH-329", "MECH-189"} <= mo, mo)

    def test_a_tag_in_any_file_wins_over_a_mention_in_another(self):
        self.assertIn("MECH-057b", self.built())
        self.assertNotIn("MECH-057b", G._claims_mentioned_only_in_substrate())

    def test_exq_led_header_counts_only_ids_before_the_colon(self):
        t, m = G._substrate_tags_in_source("# EXQ-048/049 confirmed: MECH-057b untested\n")
        self.assertEqual(set(), t)
        self.assertEqual({"MECH-057b"}, m)

    def test_unparseable_file_is_mention_only_never_tagged(self):
        t, m = G._substrate_tags_in_source('"""MECH-777: tag"""\ndef broken(:\n')
        self.assertEqual(set(), t)
        self.assertEqual({"MECH-777"}, m)

    def test_rescan_after_a_file_changes(self):
        """The scan cache is keyed on mtimes (serve.py imports this module and
        is long-lived) -- a newly tagged claim must show up without a restart."""
        self.assertNotIn("MECH-191", self.built())
        p = self.core / "agent.py"
        p.write_text('"""MECH-191: channel externalisation."""\n', encoding="utf-8")
        st = p.stat()
        os.utime(p, ns=(st.st_atime_ns, st.st_mtime_ns + 10_000_000_000))
        self.assertIn("MECH-191", self.built())

    def test_absent_tree_is_inert(self):
        G.REE_V3_CORE = self.core / "missing"
        self.assertEqual(set(), self.built())
        self.assertEqual(set(), G._claims_mentioned_only_in_substrate())


class ConfirmerLaneTest(unittest.TestCase):
    """A mention-only claim reaches the lane as `substrate_unverified` (the call
    site renders it `blocked`), never `ready` and never dropped."""

    META = {cid: {"status": "candidate", "title": cid, "location": "x.md"}
            for cid in ("MECH-801", "MECH-802", "MECH-803")}

    def setUp(self):
        self._orig_lit = G._claim_lit_conf
        self._orig_built = G._claims_implemented_in_substrate
        G._claim_lit_conf = lambda: {"MECH-801": 0.8, "MECH-802": 0.9, "MECH-803": 0.85}
        G._claims_implemented_in_substrate = lambda: {"MECH-801"}

    def tearDown(self):
        G._claim_lit_conf = self._orig_lit
        G._claims_implemented_in_substrate = self._orig_built

    def _by_cid(self, mention_only):
        out = G._evidence_confirmer_candidates(
            self.META, set(), {}, set(), None, mention_only)
        return [c["claim_id"] for c in out], {c["claim_id"]: c for c in out}

    def test_mention_only_candidate_is_flagged_not_dropped(self):
        order, by = self._by_cid({"MECH-802"})
        self.assertIn("MECH-802", by)
        self.assertIn("GFLAG-0254", by["MECH-802"]["substrate_unverified"])
        self.assertNotIn("substrate_unverified", by["MECH-801"])
        self.assertNotIn("MECH-803", by, "neither tagged nor mentioned -> dropped")

    def test_unverified_sorts_after_tagged_despite_higher_lit_conf(self):
        order, _ = self._by_cid({"MECH-802"})
        self.assertEqual(["MECH-801", "MECH-802"], order)

    def test_tagged_wins_if_a_claim_is_in_both_sets(self):
        _, by = self._by_cid({"MECH-801"})
        self.assertNotIn("substrate_unverified", by["MECH-801"])

    def test_default_is_the_tagged_only_gate(self):
        order, _ = self._by_cid(None)
        self.assertEqual(["MECH-801"], order)


REE_V3_LIVE_CORE = SCRIPTS_DIR.parent.parent / "ree-v3" / "ree_core"


@unittest.skipUnless(REE_V3_LIVE_CORE.exists(), "no ree-v3 checkout on this box")
class LiveTreeCanaryTest(unittest.TestCase):
    """Pinned findings on the real tree, so a scan that silently breaks (a parse
    regression making every file mention-only, an empty rglob) cannot read as
    'nothing is built'."""

    def setUp(self):
        self._orig_core = G.REE_V3_CORE
        G.REE_V3_CORE = REE_V3_LIVE_CORE

    def tearDown(self):
        G.REE_V3_CORE = self._orig_core

    def test_tagged_set_is_not_collapsed(self):
        # 316 raw ids / ~305 tagged on 2026-09-23; the over-broad fix gave 35.
        self.assertGreater(len(G._claims_implemented_in_substrate()), 200)

    def test_mech_057b_is_built_now_via_its_real_tags(self):
        # ree-v3 7642cd1 landed the promotion gate with docstring tags.
        self.assertIn("MECH-057b", G._claims_implemented_in_substrate())

    def test_mention_only_set_stays_small(self):
        self.assertLess(len(G._claims_mentioned_only_in_substrate()), 60)


if __name__ == "__main__":
    unittest.main(verbosity=2)
