#!/usr/bin/env python3
"""Tests for scripts/check_skill_improvement_recurrence.py.

Time-independent (no wall-clock reads outside the opt-in dormancy pass, which is
tested only via its pure `dormancy_verdict` function -- the git-shelling wrapper
is exercised only by a skip-if-absent live check) and filesystem-isolated (every
fixture corpus is written to a tempdir and passed in by path).

CALIBRATION IS THE POINT. This audit's clustering and already-codified matching
are bag-of-words heuristics over free text (module docstring design decision 2),
and every threshold in the module (MIN_JACCARD, MIN_CODIFIED_OVERLAP,
MIN_CODIFIED_FRACTION, the "mech" stopword, the EXQ-only id prefix) was
calibrated against a REAL false-cluster or false-match found in the live
REE_assembly corpus on 2026-08-01. TestCalibrationIncidents replays those exact
pairs as fixtures so a future edit to the heuristic cannot silently regress them
without a red test -- the same "mutation check" discipline as the sibling
scripts' TestIncidentReplay classes, done here with synthetic fixtures instead of
pinned git shas because the calibration incidents are about clustering LOGIC, not
about a manifest's exact content at a commit.

Run:
    /opt/local/bin/python3 scripts/test_check_skill_improvement_recurrence.py
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_skill_improvement_recurrence as m  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]


# --- fixture builders ----------------------------------------------------------

def autopsy_file(tmp: Path, name: str, targets: list[dict], status: str = "confirmed") -> Path:
    path = tmp / f"failure_autopsy_{name}.json"
    path.write_text(json.dumps({"status": status, "targets": targets}), encoding="utf-8")
    return path


def target(claim_ids: list[str], learning_extracted: list[str], run_id: str = "run_x") -> dict:
    return {"claim_ids": claim_ids, "learning_extracted": learning_extracted, "run_id": run_id}


def review_tracker_file(tmp: Path, review_log: list[dict] | None = None,
                        discussion_notes: list[str] | None = None) -> Path:
    path = tmp / "review_tracker.json"
    path.write_text(json.dumps({
        "review_log": review_log or [],
        "discussion_notes": discussion_notes or [],
    }), encoding="utf-8")
    return path


def skill_md(tmp: Path, skill_name: str, lines: list[str]) -> Path:
    d = tmp / skill_name
    d.mkdir(parents=True, exist_ok=True)
    path = d / "SKILL.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


# --- self-flag detection --------------------------------------------------------

class TestMatchSelfFlags(unittest.TestCase):
    def test_recurring_matches(self):
        self.assertIn("recurring", m.match_self_flags("this is a recurring artifact"))

    def test_process_recurrence_matches(self):
        flags = m.match_self_flags("PROCESS recurrence: has now under-lifted twice")
        self.assertIn("process_recurrence", flags)
        self.assertIn("twice", flags)

    def test_third_instance_matches(self):
        self.assertIn("third_instance", m.match_self_flags("Recurring pattern (third instance"))

    def test_third_consecutive_matches(self):
        self.assertIn("third_consecutive",
                      m.match_self_flags("Third consecutive 614-lineage FAIL"))

    def test_no_match_on_unrelated_text(self):
        self.assertEqual(m.match_self_flags("The arm fingerprint stamped cleanly."), [])

    def test_recurs_is_word_bounded(self):
        """'recurs' must not fire on 'recursive' or similar substrings."""
        self.assertEqual(m.match_self_flags("a recursive definition of the loop"), [])
        self.assertIn("recurs", m.match_self_flags("the same gate recurs on every seed"))


class TestStrongSeverity(unittest.TestCase):
    def test_process_recurrence_is_strong(self):
        self.assertTrue(bool(set(m.match_self_flags("PROCESS recurrence: twice"))
                             & m.STRONG_SEVERITY_PATTERNS))

    def test_plain_recurring_is_not_strong(self):
        self.assertFalse(bool(set(m.match_self_flags("a recurring artifact"))
                              & m.STRONG_SEVERITY_PATTERNS))


# --- embedded ids ----------------------------------------------------------------

class TestEmbeddedReferenceIds(unittest.TestCase):
    def test_exq_prefixed_ids(self):
        ids = m.embedded_reference_ids("confirmed at V3-EXQ-684 and EXQ-569g")
        self.assertIn("v3-exq-684", ids)
        self.assertIn("exq-569g", ids)

    def test_bare_three_digit_ids(self):
        ids = m.embedded_reference_ids("under-lifted twice (569g + 684)")
        self.assertIn("569g", ids)
        self.assertIn("684", ids)

    def test_four_digit_year_never_matches_as_a_bare_id(self):
        """No word boundary exists between digit 3 and digit 4 of '2026'."""
        ids = m.embedded_reference_ids("confirmed 2026-08-01, corpus grew")
        self.assertNotIn("202", ids)
        self.assertFalse(any(len(i) == 3 and i.isdigit() and i.startswith("202") for i in ids))

    def test_claim_prefixes_are_not_matched(self):
        """MECH/ARC/SD/INV/GAP/Q are claim prefixes, not run citations (design
        decision 1(b)) -- only EXQ and bare numbers are id-shaped here."""
        ids = m.embedded_reference_ids("weakens MECH-341 and ARC-062")
        self.assertNotIn("mech-341", ids)
        self.assertNotIn("arc-062", ids)

    def test_claim_id_numeric_parts_extracts_tail(self):
        self.assertEqual(m.claim_id_numeric_parts(["MECH-341", "ARC-062", "SD-033b"]),
                         {"341", "062", "033b"})

    def test_bare_claim_number_is_excluded_via_numeric_parts(self):
        """The calibration incident: a bare '341' inside 'MECH-341' must not be
        treated as a self-citation once the target's own claim_ids are known."""
        text = "some finding about MECH-341 that cites nothing else"
        ids = m.embedded_reference_ids(text)
        self.assertIn("341", ids)  # present before subtraction
        remaining = ids - m.claim_id_numeric_parts(["MECH-341"])
        self.assertNotIn("341", remaining)

    def test_prefixed_citations_trailing_digits_not_double_counted(self):
        """A SINGLE citation like 'V3-EXQ-642' must count as ONE id, not two.

        `_BARE_ID_RE` also matches the trailing digits of a prefixed match
        ('642' inside 'V3-EXQ-642'), which without this guard silently
        satisfies cluster_qualifies()'s ">= 2 distinct ids" self-evidencing
        test off a SINGLE citation. Confirmed 2026-08-22
        (chip-20260822-govskill1-clustering-mega-cluster-diagnosis):
        failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12's
        only citation is "canonical V3-EXQ-642", and it was self-qualifying as
        if it named two separate runs.
        """
        ids = m.embedded_reference_ids("recurring pattern, canonical V3-EXQ-642")
        self.assertEqual(ids, {"v3-exq-642"})

    def test_a_second_separate_bare_mention_still_counts(self):
        """The guard only suppresses a bare match CONTAINED in a prefixed
        span -- a genuinely separate later mention of the same number is a
        second textual occurrence and is kept (this module does not attempt
        to unify bare/prefixed forms of the SAME id across a whole entry)."""
        ids = m.embedded_reference_ids(
            "The censoring problem that dominated V3-EXQ-912 is solved, at "
            "less than half 912's eval-step cost.")
        self.assertIn("v3-exq-912", ids)
        self.assertIn("912", ids)


# --- salient tokens ---------------------------------------------------------------

class TestExtractSalientTokens(unittest.TestCase):
    def test_short_words_and_stopwords_excluded(self):
        toks = m.extract_salient_tokens("The run is set and this that these those would")
        self.assertEqual(toks, set())

    def test_mech_prefix_excluded(self):
        """'mech' is a claim-id prefix, not content -- see stopword rationale."""
        toks = m.extract_salient_tokens("weakens on MECH-341 from a bad criterion")
        self.assertNotIn("mech", toks)
        self.assertIn("criterion", toks)

    def test_hyphenated_digit_suffix_normalizes(self):
        """'Seed-44' and 'Seed44' must tokenize to the same 'seed' token --
        the flagship seed-44-truncation calibration incident."""
        a = m.extract_salient_tokens("Seed44 truncation is a recurring artifact")
        b = m.extract_salient_tokens("Seed-44 truncation (early episode death)")
        self.assertIn("seed", a)
        self.assertIn("seed", b)
        self.assertIn("truncation", a & b)

    def test_self_flag_vocabulary_excluded(self):
        toks = m.extract_salient_tokens("This is a recurring signature, confirmed twice")
        self.assertNotIn("recurring", toks)
        self.assertNotIn("signature", toks)
        self.assertNotIn("twice", toks)
        self.assertNotIn("confirmed", toks)


# --- clustering --------------------------------------------------------------------

def _mk_hit(artifact: str, text: str, claim_ids: list[str] | None = None) -> dict:
    claim_ids = claim_ids or []
    return {
        "source": "autopsy", "artifact": artifact, "target_index": 0, "item_index": 0,
        "run_id": "", "claim_ids": claim_ids, "text": text,
        "flags": m.match_self_flags(text),
        "strong_severity": bool(set(m.match_self_flags(text)) & m.STRONG_SEVERITY_PATTERNS),
        "embedded_ids": sorted(m.embedded_reference_ids(text) - m.claim_id_numeric_parts(claim_ids)),
        "tokens": sorted(m.extract_salient_tokens(text)),
    }


def _mk_review_hit(artifact: str, text: str) -> dict:
    """Like `_mk_hit` but source='review_tracker' -- a governance review_log
    note, which is the roster shape (see MAX_EMBEDDED_IDS_FOR_ROSTER / the
    cluster_qualifies source scoping) rather than a focused autopsy finding."""
    return {
        "source": "review_tracker", "artifact": artifact, "target_index": 0,
        "item_index": 0, "run_id": "", "claim_ids": [], "text": text,
        "flags": m.match_self_flags(text),
        "strong_severity": bool(set(m.match_self_flags(text)) & m.STRONG_SEVERITY_PATTERNS),
        "embedded_ids": sorted(m.embedded_reference_ids(text)),
        "tokens": sorted(m.extract_salient_tokens(text)),
    }


class TestClusterHits(unittest.TestCase):
    def test_shared_embedded_id_clusters(self):
        a = _mk_hit("a", "under-lifted twice (569g + 684), same instrument")
        b = _mk_hit("b", "does not verify-lift on this env (569g/684 unverified)")
        clusters = m.cluster_hits([a, b])
        self.assertEqual(len(clusters), 1)

    def test_bare_and_prefixed_forms_of_the_same_id_still_bridge(self):
        """Matching is on NORMALIZED ids: a bare '642' in one hit and a
        prefixed 'V3-EXQ-642' in another are the same citation and must
        still cluster, even though embedded_reference_ids() no longer lets
        ONE hit double-count a single citation as two ids (that fix is about
        the COUNT, not about cross-hit matching)."""
        a = _mk_hit("a", "the 642 pattern is now recurring at the authority layer")
        b = _mk_hit("b", "actively misleading, recurring pattern, canonical V3-EXQ-642")
        clusters = m.cluster_hits([a, b])
        self.assertEqual(len(clusters), 1)

    def test_roster_sized_hit_does_not_cluster_via_a_single_shared_id(self):
        """MAX_EMBEDDED_IDS_FOR_ROSTER guard: a hit citing many run ids as
        ordinary bookkeeping (a review_log cycle summary) must not union with
        an unrelated single-topic hit merely because the roster happens to
        mention that hit's own run number in passing."""
        roster = _mk_review_hit(
            "roster", "Governance cycle: confirmed autopsies for "
            "843/845/847/850/852/853/855/858/861 applied inline, three "
            "diagnostic PASSes left pending for next cycle review.")
        unrelated = _mk_hit("a", "MECH-180's stored category was conditioned "
                                 "on a future run scoring; it has now scored "
                                 "twice (845, 861).")
        clusters = m.cluster_hits([roster, unrelated])
        self.assertEqual(len(clusters), 2)

    def test_low_token_overlap_does_not_cluster(self):
        a = _mk_hit("a", "the harm pathway trained cleanly across all seeds recurring")
        b = _mk_hit("b", "z_world integration recurring signal on the reach pair")
        clusters = m.cluster_hits([a, b])
        self.assertEqual(len(clusters), 2)

    def test_single_shared_word_does_not_cluster(self):
        """MIN_SHARED_TOKENS floor: one coincidental word is not enough."""
        a = _mk_hit("a", "the instrument artifact recurring reading is stale")
        b = _mk_hit("b", "a wholly different finding about z_goal salience recurring")
        clusters = m.cluster_hits([a, b])
        self.assertEqual(len(clusters), 2)


class TestCalibrationIncidents(unittest.TestCase):
    """Each test replays one confirmed 2026-08-01 false-cluster / false-match
    finding as a synthetic fixture -- the mutation check for the heuristic."""

    def test_shared_claim_id_alone_does_not_cluster(self):
        """V3-EXQ-614c / V3-EXQ-629: both tag MECH-341 and share NOTHING else.
        Before excluding claim-prefix tokens and claim numeric tails from the
        recurrence signal, these clustered on 'mech'/'341' alone."""
        a = _mk_hit("614c", "Third consecutive lineage FAIL, an instrument "
                            "artifact rather than evidence against MECH-341.",
                   claim_ids=["MECH-341"])
        b = _mk_hit("629", "The score_margin degeneracy is a recurring "
                           "E3-selection-landscape signal, a different facet of "
                           "the 604a/624a family.",
                   claim_ids=["MECH-341"])
        clusters = m.cluster_hits([a, b])
        self.assertEqual(len(clusters), 2, "must not merge on the shared claim id alone")

    def test_long_summary_blob_does_not_chain_unrelated_hits(self):
        """A long multi-topic governance summary must not act as a transitive
        hub linking hits that share nothing with EACH OTHER."""
        blob = _mk_hit("review_log_note",
                       "Governance cycle: 861 (MECH-180 conditional category "
                       "stale, scored twice) and 864 (recurring third instance "
                       "write-count confound floor-saturation) both applied; "
                       "859 claim-free ARC-062 route_source ablation inconclusive; "
                       "847 denominator-bug corrected; 843 non_contributory.")
        unrelated_a = _mk_hit("A", "bistability is cross-run on one host, not "
                                   "merely cross-machine, repeated identical runs")
        unrelated_b = _mk_hit("B", "borderline gate on frozen_pe recurs if "
                                   "the margin is widened next time")
        clusters = m.cluster_hits([blob, unrelated_a, unrelated_b])
        # unrelated_a and unrelated_b must not land in the same cluster as each
        # other purely via the blob's breadth.
        groups = {}
        for i, c in enumerate(clusters):
            for h in c:
                groups[h["artifact"]] = i
        self.assertNotEqual(groups.get("A"), groups.get("B"))

    def test_already_codified_requires_overlap_and_fraction(self):
        """A short, weakly-overlapping match against a long unrelated skill
        paragraph must not count as already-codified (V3-EXQ-629 vs an
        unrelated cross-field skill paragraph, overlap=3)."""
        hit = _mk_hit("629", "The score_margin degeneracy is a recurring "
                             "E3-selection-landscape signal, different facet, "
                             "family of undifferentiated modulatory salience.")
        long_unrelated = {
            "skill_file": "skills/cross-field/SKILL.md", "line": 5,
            "text": "unrelated long paragraph",
            "tokens": {"substrate", "incomplete", "stuck", "family", "biology",
                      "translation", "engineering", "wide", "seeds", "traceback",
                      "program", "biological", "routes", "known", "unknown",
                      "falsified", "monostrategy", "move", "learning", "deep",
                      "route", "skill", "substitute", "break", "keeps", "code",
                      "fail", "crashes", "somewhere", "pattern", "recognised"},
        }
        result = m.already_codified([hit], [long_unrelated])
        self.assertIsNone(result, "weak coincidental overlap must not count as codified")

    def test_roster_hub_does_not_merge_unrelated_topics_into_one_mega_cluster(self):
        """Regression for the 2026-08-22 finding
        (chip-20260822-govskill1-clustering-mega-cluster-diagnosis): an
        11-hit cluster mixing a genuine 2-hit zworld_p0_episodes recurrence
        with 9 UNRELATED hits (pulled in transitively via governance
        review_log rosters, plus one coincidental single-id citation)
        diluted the pooled cluster vocabulary enough that already_codified()
        matched the WRONG skill line -- an unrelated GENERIC governance
        paragraph that happened to be large enough to win on raw overlap,
        instead of the actual zworld_p0_episodes fix.

        This replays the real corpus shape with paraphrased fixtures: two
        genuinely-related zworld hits (sharing the id '728' in both bare and
        prefixed form), two single-topic autopsy hits that coincidentally
        both cite prior run '845' in passing (861 / 864 shape -- these DO
        still cluster with each other under the accepted-residual design;
        see MAX_EMBEDDED_IDS_FOR_ROSTER's docstring), and two governance
        review_log roster notes that each mention several of the above run
        numbers as ordinary cycle bookkeeping and must not bridge ANY of
        them together.
        """
        pending_review = _mk_hit(
            "pending_review_batch",
            "Confirms the SD-070 zworld_p0_episodes defect propagates to any "
            "_train_all_on_agent driver that omits it -- same signature as "
            "V3-EXQ-728 pre-fix.")
        zworld_875 = _mk_hit(
            "875",
            "Recurring driver-configuration defect class: the opt-in "
            "zworld_p0_episodes default-0 design in _train_all_on_agent is "
            "silent and easy to omit -- confirmed twice now (V3-EXQ-728 "
            "originally, V3-EXQ-875 independently).")
        ceiling_861 = _mk_hit(
            "861",
            "MECH-180's stored epistemic_category was explicitly conditioned "
            "on a future ecological run scoring -- it has now scored twice "
            "(845, 861), the reading is stale on its own stated terms.")
        sweep_864 = _mk_hit(
            "864",
            "Recurring pattern (third instance, after 845's write-count "
            "confound and 794's floor-saturation defect): a driver's nominal "
            "sweep parameter fails to vary because of an environment-level "
            "constraint absorbing the manipulation.")
        roster_a = _mk_review_hit(
            "review_log[1].note",
            "Governance cycle: confirmed autopsies for 861/864 applied "
            "inline; 859 claim-free route_source ablation inconclusive; 847 "
            "denominator-bug corrected; 843 non_contributory; 850 pending "
            "next cycle; 852 ceiling reconfirmed; 855 dry-run leak closed; "
            "857 evidence_direction unset; 848 superseded by a later run.")
        roster_b = _mk_review_hit(
            "review_log[2].note",
            "Continuation of the prior cycle: applied confirmed findings for "
            "875 and 882 plus 866/873/890/321/358/471/472 processed this "
            "session; three diagnostic PASSes left pending for next cycle "
            "review, per user instruction to batch remaining items together.")

        clusters = m.cluster_hits(
            [pending_review, zworld_875, ceiling_861, sweep_864, roster_a, roster_b])
        groups = {}
        for i, c in enumerate(clusters):
            for h in c:
                groups[h["artifact"]] = i

        # The genuine pair stays together...
        self.assertEqual(groups["pending_review_batch"], groups["875"],
                         "the genuine zworld_p0_episodes pair must still cluster")
        # ...but nothing else joins it, in either direction.
        for other in ("861", "864", "review_log[1].note", "review_log[2].note"):
            self.assertNotEqual(
                groups["875"], groups[other],
                f"{other} must not merge into the zworld cluster via the roster hub")
        # The rosters must not bridge 861 and 864 to EACH OTHER via bookkeeping
        # either -- confirmed separately (test_bare_and_prefixed_forms_of_the_same_id_still_bridge's
        # sibling, test_two_topically_distinct_hits_still_merge_on_one_shared_id
        # below) that 861/864 DO still merge with each other directly, on their
        # own small, non-roster shared citation of '845' -- an accepted,
        # checked-non-wrong residual (see MAX_EMBEDDED_IDS_FOR_ROSTER docstring).
        # What this test asserts is narrower: the ROSTERS specifically must not
        # be what pulls them together, and must not pull in the zworld pair.
        self.assertNotEqual(groups["861"], groups["review_log[1].note"])
        self.assertNotEqual(groups["864"], groups["review_log[1].note"])

        zworld_skill_line = {
            "skill_file": "skills/queue-experiment/SKILL.md", "line": 771,
            "text": ("This silent driver-configuration defect class: does "
                    "every call to _train_all_on_agent pass "
                    "zworld_p0_episodes? Omitting it is easy and the default "
                    "opt-in design means the world encoder is never "
                    "stepped, so z_world silently stays a frozen random "
                    "projection with no error, propagates to any driver. "
                    "Confirmed recurring across independent drivers: "
                    "V3-EXQ-875, plus V3-EXQ-728's original pre-fix "
                    "discovery, grep every _train_all_on_agent call "
                    "site and confirm zworld_p0_episodes is explicit."),
        }
        zworld_skill_line["tokens"] = m.extract_salient_tokens(zworld_skill_line["text"])
        # A large, GENERIC governance-process paragraph, unrelated to zworld,
        # shaped like the real governance/SKILL.md GOV-APPLY-1 paragraph that
        # incidentally won on raw overlap against the diluted mega-cluster.
        generic_governance_line = {
            "skill_file": "skills/governance/SKILL.md", "line": 1581,
            "text": ("Unapplied confirmed-autopsy recommendations: the other "
                    "standing scans ask what a set of verdicts means or "
                    "whether the verdict was recorded, this asks whether it "
                    "was ever applied. A confirmed target's recommendation "
                    "is not reflected in the registry. Applies dedup so "
                    "only the latest adjudication of a run counts. Reports "
                    "its own coverage across confirmed targets carrying a "
                    "machine-readable per-claim disposition, deliberately "
                    "under-claiming rather than inferring change owed from "
                    "a category compare across the governance cycle, "
                    "session, and every claim touched this review."),
        }
        generic_governance_line["tokens"] = m.extract_salient_tokens(
            generic_governance_line["text"])

        skill_lines = [zworld_skill_line, generic_governance_line]
        hits = [pending_review, zworld_875, ceiling_861, sweep_864, roster_a, roster_b]
        result = m.audit(hits, skill_lines)

        matched = {a: r["codified_in"]["skill_file"] + ":" + str(r["codified_in"]["line"])
                  for r in result["excluded_already_codified"] for a in r["artifacts"]}
        candidate_artifacts = {a for r in result["checklist_candidates"] for a in r["artifacts"]}

        self.assertNotIn("875", candidate_artifacts,
                         "the zworld pair must resolve, not surface as a fresh candidate")
        self.assertEqual(
            matched.get("875"), "skills/queue-experiment/SKILL.md:771",
            "875 must match its OWN zworld fix line, not an unrelated generic "
            "governance paragraph diluted in via the mega-cluster")

    def test_two_topically_distinct_hits_still_merge_on_one_shared_id_but_resolve_correctly(self):
        """Accepted residual, checked rather than assumed: two SMALL,
        non-roster entries sharing exactly one incidental id (V3-EXQ-861,
        about a claim's ceiling-status re-scoring, and V3-EXQ-864, about an
        unrelated driver-parameter sweep defect, both citing prior run '845'
        in passing) DO still merge under MAX_EMBEDDED_IDS_FOR_ROSTER -- a
        shared-count floor was tried and rejected because it also breaks the
        genuine V3-EXQ-643/916-cluster "canonical" cross-reference pair (see
        that constant's docstring). What matters is that the merge does not
        resolve to a WRONG-FILE already-codified match -- 861's own strong
        overlap must still dominate the small pooled cluster vocabulary."""
        a = _mk_hit("861", "MECH-180's stored category was conditioned on a "
                           "future run scoring; it has now scored twice (845, 861).")
        b = _mk_hit("864", "Recurring pattern (third instance, after 845's "
                           "write-count confound and 794's floor-saturation defect).")
        clusters = m.cluster_hits([a, b])
        self.assertEqual(len(clusters), 1)

        matching_line = {
            "skill_file": "skills/failure-autopsy/SKILL.md", "line": 307,
            "text": ("Confirmed at V3-EXQ-861 (MECH-180): the stored "
                    "substrate_ceiling category was conditioned on a specific "
                    "future run scoring, that run scored twice (845, 861), "
                    "and nobody had revisited the reading -- a conditionally "
                    "stamped category is present, so completeness checks see "
                    "nothing to flag, check for a stated re-check condition."),
        }
        matching_line["tokens"] = m.extract_salient_tokens(matching_line["text"])
        unrelated_line = {
            "skill_file": "skills/governance/SKILL.md", "line": 1581,
            "text": ("Unapplied confirmed-autopsy recommendations: whether a "
                    "recommendation was ever applied to the registry, "
                    "deliberately under-claiming coverage rather than "
                    "inferring change owed across the governance cycle."),
        }
        unrelated_line["tokens"] = m.extract_salient_tokens(unrelated_line["text"])

        result = m.already_codified(clusters[0], [matching_line, unrelated_line])
        self.assertIsNotNone(result)
        self.assertEqual(result["skill_file"], "skills/failure-autopsy/SKILL.md",
                         "the merged pair must resolve to 861's own correct "
                         "line, not an unrelated generic paragraph")


# --- cluster_qualifies -------------------------------------------------------------

class TestClusterQualifies(unittest.TestCase):
    def test_strong_severity_qualifies_alone(self):
        hit = _mk_hit("a", "Recurring pattern (third instance, after two priors)")
        ok, reason = m.cluster_qualifies([hit])
        self.assertTrue(ok)
        self.assertIn("third instance", reason.lower().replace("_", " ").replace("/", " ")
                      if "third" in reason else "strong")

    def test_embedded_ids_over_threshold_qualifies_alone(self):
        hit = _mk_hit("a", "recurring across 654h/485i/625e/460h/460i self-routes")
        ok, _ = m.cluster_qualifies([hit])
        self.assertTrue(ok)

    def test_single_weak_hit_does_not_qualify(self):
        hit = _mk_hit("a", "this is a recurring artifact with no other signal")
        ok, _ = m.cluster_qualifies([hit])
        self.assertFalse(ok)

    def test_two_independent_files_qualify(self):
        a = _mk_hit("file_a", "seed-44 truncation is a recurring artifact on reef configs")
        b = _mk_hit("file_b", "seed-44 truncation recurring per-seed instability on reef")
        ok, reason = m.cluster_qualifies([a, b])
        self.assertTrue(ok)
        self.assertIn("independent", reason)

    def test_review_tracker_roster_does_not_self_qualify_via_embedded_ids(self):
        """Design decision 1(b) is scoped to a `learning_extracted` sentence
        (an autopsy hit's own focused finding), not a review_log governance
        roster note. Confirmed 2026-08-22: a review_log note citing 15+ run
        ids as ordinary cycle bookkeeping was self-qualifying as an
        'actionable' recurrence candidate purely by virtue of being a
        roster, with no bearing on whether anything actually recurred."""
        roster = _mk_review_hit(
            "review_log[9].note",
            "Continuation of the cycle: applied confirmed findings for "
            "005/014/030/059/089/321/322/358/457/471/472/603q/866b/873/875 "
            "processed this session, three diagnostic PASSes left pending.")
        ok, _ = m.cluster_qualifies([roster])
        self.assertFalse(
            ok, "a review_tracker roster must not self-qualify on id count alone")

    def test_autopsy_hit_still_self_qualifies_via_embedded_ids(self):
        """Companion negative control: the SAME shape (many embedded ids in
        one entry) must still qualify when it genuinely IS an autopsy's own
        focused, self-evidencing citation (design decision 1(b))."""
        hit = _mk_hit("a", "recurring across 654h/485i/625e/460h/460i self-routes")
        ok, _ = m.cluster_qualifies([hit])
        self.assertTrue(ok)


# --- end-to-end audit() over a small fixture corpus ---------------------------------

class TestAuditEndToEnd(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_qualifying_uncodified_cluster_is_a_candidate(self):
        hits = [
            _mk_hit("a", "seed-44 truncation is a recurring artifact on reef configs"),
            _mk_hit("b", "seed-44 truncation recurring per-seed instability on reef"),
        ]
        result = m.audit(hits, skill_lines=[])
        self.assertEqual(len(result["checklist_candidates"]), 1)
        self.assertEqual(result["excluded_already_codified"], [])

    def test_qualifying_codified_cluster_is_excluded(self):
        hits = [
            _mk_hit("a", "seed-44 truncation is a recurring artifact on reef configs"),
            _mk_hit("b", "seed-44 truncation recurring per-seed instability on reef"),
        ]
        skill_text = ("Is seed 44 in the seed list on a reef-config env? Confirmed a "
                     "recurring per-seed instability truncation artifact on reef "
                     "configs across independent autopsies on this config family.")
        skill_line = {
            "skill_file": "skills/queue-experiment/SKILL.md", "line": 645,
            "text": skill_text,
            "tokens": m.extract_salient_tokens(skill_text),
        }
        result = m.audit(hits, skill_lines=[skill_line])
        self.assertEqual(result["checklist_candidates"], [])
        self.assertEqual(len(result["excluded_already_codified"]), 1)

    def test_audit_result_is_json_serializable_including_a_codified_match(self):
        """Regression: `already_codified`'s returned dict carried a raw `set`
        (from `load_skill_lines`' token field) straight into the audit result,
        which crashed `--json` output (and `--write-report`, which runs after
        it in `main()`) the first time a real codified match was hit end to
        end -- not caught by the other tests here because none of them run the
        result through json.dumps."""
        hits = [
            _mk_hit("a", "seed-44 truncation is a recurring artifact on reef configs"),
            _mk_hit("b", "seed-44 truncation recurring per-seed instability on reef"),
        ]
        skill_text = ("Is seed 44 in the seed list on a reef-config env? Confirmed a "
                     "recurring per-seed instability truncation artifact on reef "
                     "configs across independent autopsies on this config family.")
        skill_line = {"skill_file": "skills/queue-experiment/SKILL.md", "line": 645,
                     "text": skill_text, "tokens": m.extract_salient_tokens(skill_text)}
        result = m.audit(hits, skill_lines=[skill_line])
        self.assertEqual(len(result["excluded_already_codified"]), 1)
        json.dumps(result)  # must not raise

    def test_non_qualifying_hit_is_sub_threshold_not_excluded_or_candidate(self):
        hits = [_mk_hit("a", "this is a recurring artifact, one-off, no other signal")]
        result = m.audit(hits, skill_lines=[])
        self.assertEqual(result["checklist_candidates"], [])
        self.assertEqual(result["excluded_already_codified"], [])
        self.assertEqual(len(result["sub_threshold"]), 1)

    def test_read_only_never_writes_into_autopsy_dir(self):
        """The scan must never touch the corpus it reads."""
        autopsy_file(self.tmp, "x", [target(["MECH-1"], ["a recurring finding, twice"])])
        before = sorted(p.name for p in self.tmp.iterdir())
        hits = []
        for fp in sorted(self.tmp.glob("failure_autopsy_*.json")):
            hits.extend(m.scan_autopsy_file(fp))
        after = sorted(p.name for p in self.tmp.iterdir())
        self.assertEqual(before, after)
        self.assertEqual(len(hits), 1)


# --- scan_autopsy_file / scan_review_tracker -----------------------------------------

class TestScanAutopsyFile(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_non_confirmed_status_yields_nothing(self):
        fp = autopsy_file(self.tmp, "x",
                          [target(["MECH-1"], ["a recurring finding, confirmed twice"])],
                          status="draft")
        self.assertEqual(m.scan_autopsy_file(fp), [])

    def test_item_without_self_flag_is_not_a_hit(self):
        fp = autopsy_file(self.tmp, "x", [target(["MECH-1"], ["a plain, unrelated finding"])])
        self.assertEqual(m.scan_autopsy_file(fp), [])

    def test_flagged_item_is_a_hit_with_claim_ids_carried(self):
        fp = autopsy_file(self.tmp, "x",
                          [target(["MECH-1", "ARC-2"], ["this is a recurring artifact"])])
        hits = m.scan_autopsy_file(fp)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["claim_ids"], ["MECH-1", "ARC-2"])
        self.assertEqual(hits[0]["source"], "autopsy")

    def test_unparseable_file_yields_nothing(self):
        fp = self.tmp / "failure_autopsy_bad.json"
        fp.write_text("{not valid json", encoding="utf-8")
        self.assertEqual(m.scan_autopsy_file(fp), [])


class TestScanReviewTracker(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_context_field_mined(self):
        fp = review_tracker_file(self.tmp, review_log=[
            {"utc": "2026-01-01T00:00:00Z", "context": "a recurring trap confirmed here",
             "claim_ids_touched": ["MECH-1"]},
        ])
        hits = m.scan_review_tracker(fp)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["source"], "review_tracker")

    def test_note_field_also_mined(self):
        fp = review_tracker_file(self.tmp, review_log=[
            {"utc": "2026-01-01T00:00:00Z", "note": "confirmed twice, same signature here"},
        ])
        self.assertEqual(len(m.scan_review_tracker(fp)), 1)

    def test_discussion_notes_mined(self):
        fp = review_tracker_file(self.tmp, discussion_notes=["a recurring trap noted here"])
        hits = m.scan_review_tracker(fp)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["artifact"], "discussion_notes[0]")

    def test_unflagged_entries_yield_nothing(self):
        fp = review_tracker_file(self.tmp, review_log=[
            {"utc": "x", "context": "ordinary review with nothing unusual"},
        ], discussion_notes=["nothing to see here"])
        self.assertEqual(m.scan_review_tracker(fp), [])


# --- pointer-based incremental scan --------------------------------------------------

class TestPointerIncremental(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.autopsy_dir = self.tmp / "planning"
        self.autopsy_dir.mkdir()
        self.review_tracker = self.tmp / "review_tracker.json"
        review_tracker_file(self.tmp).rename(self.review_tracker)
        self.pointer_file = self.tmp / "pointer.json"

    def test_first_run_finds_all_hits(self):
        autopsy_file(self.autopsy_dir, "a", [target(["MECH-1"], ["a recurring finding here"])])
        pointer = m.load_pointer(self.pointer_file)
        hits, new_pointer = m.collect_hits(self.autopsy_dir, self.review_tracker, pointer)
        self.assertEqual(len(hits), 1)
        m.save_pointer(self.pointer_file, new_pointer)
        self.assertTrue(self.pointer_file.exists())

    def test_second_run_without_changes_does_not_rescan_but_keeps_hits(self):
        fp = autopsy_file(self.autopsy_dir, "a", [target(["MECH-1"], ["a recurring finding here"])])
        pointer = m.load_pointer(self.pointer_file)
        hits1, np1 = m.collect_hits(self.autopsy_dir, self.review_tracker, pointer)
        m.save_pointer(self.pointer_file, np1)

        # Corrupt the file on disk WITHOUT changing its mtime signature tracked
        # by the pointer -- simulate "nothing changed" by just re-running with
        # the same mtime; the accumulated hit must still be reported.
        pointer2 = m.load_pointer(self.pointer_file)
        hits2, np2 = m.collect_hits(self.autopsy_dir, self.review_tracker, pointer2)
        self.assertEqual(len(hits2), 1)
        self.assertEqual(hits1[0]["artifact"], hits2[0]["artifact"])

    def test_new_file_added_later_is_picked_up_and_old_hit_retained(self):
        autopsy_file(self.autopsy_dir, "a", [target(["MECH-1"], ["a recurring finding here"])])
        pointer = m.load_pointer(self.pointer_file)
        hits1, np1 = m.collect_hits(self.autopsy_dir, self.review_tracker, pointer)
        m.save_pointer(self.pointer_file, np1)
        self.assertEqual(len(hits1), 1)

        autopsy_file(self.autopsy_dir, "b", [target(["MECH-2"], ["a recurring finding elsewhere"])])
        pointer2 = m.load_pointer(self.pointer_file)
        hits2, np2 = m.collect_hits(self.autopsy_dir, self.review_tracker, pointer2)
        self.assertEqual(len(hits2), 2, "must retain the first hit AND find the new one")

    def test_save_pointer_merges_rather_than_overwrites_concurrent_state(self):
        """Simulates a second writer landing a hit between this run's read and
        write -- save_pointer must not clobber it (narrow-append per the
        umbrella CLAUDE.md read-modify-write contamination guidance)."""
        m.save_pointer(self.pointer_file, {
            "schema_version": "v1", "last_swept_at": "t0",
            "seen_autopsy_mtimes": {"other.json": 1.0},
            "seen_review_tracker_mtime": None,
            "hits_by_key": {"autopsy|other|0|0": {"artifact": "other"}},
        })
        # A second "session" writes its own hit without having seen the first's.
        m.save_pointer(self.pointer_file, {
            "schema_version": "v1", "last_swept_at": "t1",
            "seen_autopsy_mtimes": {"mine.json": 2.0},
            "seen_review_tracker_mtime": None,
            "hits_by_key": {"autopsy|mine|0|0": {"artifact": "mine"}},
        })
        final = m.load_pointer(self.pointer_file)
        self.assertIn("autopsy|other|0|0", final["hits_by_key"])
        self.assertIn("autopsy|mine|0|0", final["hits_by_key"])
        self.assertIn("other.json", final["seen_autopsy_mtimes"])
        self.assertIn("mine.json", final["seen_autopsy_mtimes"])


# --- dormancy / effectiveness-feedback (pure logic only) -----------------------------

class TestDormancyVerdict(unittest.TestCase):
    def test_too_young_returns_none(self):
        verdict = m.dormancy_verdict({"seed", "truncation"}, months_old=1.0,
                                     post_intro_hits=[], dormancy_months=3)
        self.assertIsNone(verdict)

    def test_old_with_no_post_hits_is_no_recurrence_detected(self):
        verdict = m.dormancy_verdict({"seed", "truncation"}, months_old=5.0,
                                     post_intro_hits=[], dormancy_months=3)
        self.assertEqual(verdict, "no_post_addition_recurrence_detected")

    def test_old_with_matching_post_hit_is_recurring_despite_checklist(self):
        post_hits = [{"tokens": ["seed", "truncation", "unrelated"]}]
        verdict = m.dormancy_verdict({"seed", "truncation"}, months_old=5.0,
                                     post_intro_hits=post_hits, dormancy_months=3)
        self.assertEqual(verdict, "recurring_despite_checklist")

    def test_old_with_non_matching_post_hit_is_no_recurrence_detected(self):
        post_hits = [{"tokens": ["wholly", "different", "vocabulary"]}]
        verdict = m.dormancy_verdict({"seed", "truncation"}, months_old=5.0,
                                     post_intro_hits=post_hits, dormancy_months=3)
        self.assertEqual(verdict, "no_post_addition_recurrence_detected")


# --- load_skill_lines --------------------------------------------------------------

class TestLoadSkillLines(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def _skills_dir(self) -> Path:
        # load_skill_lines derives the reported path from `skills_dir.name`
        # (production always passes a directory literally named "skills") --
        # mirror that here rather than the tmpdir's random basename.
        d = self.tmp / "skills"
        d.mkdir()
        return d

    def test_short_lines_excluded_below_overlap_floor(self):
        skills_dir = self._skills_dir()
        skill_md(skills_dir, "foo", ["# Foo", "ok"])
        lines = m.load_skill_lines([skills_dir])
        self.assertEqual(lines, [])

    def test_line_with_enough_tokens_is_kept(self):
        skills_dir = self._skills_dir()
        skill_md(skills_dir, "foo", [
            "- A distinctive bullet about seed truncation reef config instability artifact",
        ])
        lines = m.load_skill_lines([skills_dir])
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0]["skill_file"], "skills/foo/SKILL.md")


# --- ASCII output convention ---------------------------------------------------------

class TestAsciiOutput(unittest.TestCase):
    def test_source_stdout_strings_are_ascii(self):
        for name in ("check_skill_improvement_recurrence.py",
                     "test_check_skill_improvement_recurrence.py"):
            text = (REPO_ROOT / "scripts" / name).read_text(encoding="utf-8")
            for i, line in enumerate(text.splitlines(), 1):
                try:
                    line.encode("ascii")
                except UnicodeEncodeError:
                    self.fail(f"{name}:{i} non-ASCII: {line!r}")


# --- live corpus smoke test (skip if absent) ------------------------------------------

class TestLiveCorpusSmoke(unittest.TestCase):
    """Runs the real audit against the actual REE_assembly corpus and asserts it
    reproduces the known-folded seed-44 pattern as already-codified, never as a
    fresh candidate.

    ORACLE INDEPENDENCE (oracle-vacuity audit 2026-08-18). Every guard below is
    read from the FILESYSTEM or is a LITERAL. Nothing that decides whether this
    test asserts anything is computed by `audit()` / `already_codified()`, which
    are the functions under test.

    The prior shape built its oracle by filtering `audit()`'s OWN
    `excluded_already_codified` output for the seed-44 artifacts, then asserted
    that set did not intersect the candidates. Reverting `already_codified` to
    never-fire emptied `excluded_already_codified`, which emptied the oracle,
    and the intersection assertion passed against nothing. Measured: the test
    stayed GREEN under all of `already_codified -> (False, None)`,
    `cluster_qualifies -> (False, ...)`, `cluster_hits -> []`,
    `scan_autopsy_file -> []` and `scan_review_tracker -> []`. This is the
    FM11d shape (REE_assembly `48bae8be81`).

    An absent corpus is a FAILURE here, never a skip -- a silent stand-down is
    indistinguishable from the fix having been reverted.
    """

    # Independent oracle: the two autopsy artifacts whose shared pattern (seed-44
    # truncation) was folded into the queue-experiment skill on 2026-08-01. These
    # are LITERALS, checked against the filesystem, never derived from audit().
    SEED44_ARTIFACTS = frozenset({
        "failure_autopsy_EXQ-539-540_MECH307_2026-05-17",
        "failure_autopsy_V3-EXQ-538a_2026-07-10",
    })

    def _live_inputs(self):
        """Collect the corpus, failing loudly if it cannot support an assertion."""
        self.assertTrue(
            m.DEFAULT_AUTOPSY_DIR.is_dir(),
            "evidence/planning/ is absent, so this test cannot assert anything. "
            "Do not soften this to a skip -- either restore the corpus or "
            "re-point this class at a fixture corpus.")

        # Non-vacuity guard, read straight from disk: the two artifacts the
        # oracle names must still BE in the corpus.
        on_disk = {p.stem for p in m.DEFAULT_AUTOPSY_DIR.glob("failure_autopsy_*.json")}
        missing = sorted(self.SEED44_ARTIFACTS - on_disk)
        self.assertEqual(
            [], missing,
            "the seed-44 oracle artifacts %s are no longer in evidence/planning/. "
            "This test's oracle is gone; re-point it at a fixture corpus rather "
            "than deleting the assertion." % missing)

        hits = []
        for fp in sorted(m.DEFAULT_AUTOPSY_DIR.glob("failure_autopsy_*.json")):
            hits.extend(m.scan_autopsy_file(fp))
        if m.DEFAULT_REVIEW_TRACKER.exists():
            hits.extend(m.scan_review_tracker(m.DEFAULT_REVIEW_TRACKER))
        self.assertTrue(hits, "no self-flagged hits scanned from the live corpus")

        skill_lines = m.load_skill_lines(m.DEFAULT_SKILLS_DIRS)
        self.assertTrue(skill_lines, "no skill lines loaded from the live corpus")
        return hits, skill_lines

    def test_the_live_corpus_is_actually_loaded(self):
        """Standalone non-vacuity check, so the guards fail on their own line.

        Without this, a corpus that stopped supporting the assertions below
        would surface as a confusing failure inside the invariant test rather
        than as 'the corpus is gone'.
        """
        hits, skill_lines = self._live_inputs()
        # The seed-44 hits must survive scanning -- i.e. the SCANNERS still see
        # them, independently of what audit() later decides to do with them.
        scanned = {h.get("artifact") for h in hits}
        missing = sorted(self.SEED44_ARTIFACTS - scanned)
        self.assertEqual(
            [], missing,
            "the seed-44 artifacts %s are on disk but produced no self-flagged "
            "hit; scan_autopsy_file no longer sees them" % missing)

    def test_live_corpus_runs_clean_and_known_patterns_are_codified(self):
        hits, skill_lines = self._live_inputs()
        result = m.audit(hits, skill_lines)
        for key in ("checklist_candidates", "excluded_already_codified", "sub_threshold"):
            self.assertIsInstance(result[key], list)

        buckets = {k: {a for r in result[k] for a in r["artifacts"]}
                   for k in ("checklist_candidates", "excluded_already_codified",
                             "sub_threshold")}

        # POSITIVE direction, over the LITERAL oracle rather than over audit()'s
        # own output. This is what goes RED when already_codified is reverted to
        # never-fire; the old intersection test did not.
        not_excluded = sorted(self.SEED44_ARTIFACTS - buckets["excluded_already_codified"])
        self.assertEqual(
            [], not_excluded,
            "the seed-44 pattern %s must be recognised as ALREADY CODIFIED "
            "(folded into queue-experiment 2026-08-01). Buckets: candidates=%s "
            "sub_threshold=%s" % (not_excluded,
                                  sorted(self.SEED44_ARTIFACTS & buckets["checklist_candidates"]),
                                  sorted(self.SEED44_ARTIFACTS & buckets["sub_threshold"])))

        # NEGATIVE direction, retained unweakened: a known-folded pattern must
        # not ALSO surface as fresh work.
        self.assertFalse(
            self.SEED44_ARTIFACTS & buckets["checklist_candidates"],
            "a known-folded pattern must not also appear as a fresh candidate: %s"
            % sorted(self.SEED44_ARTIFACTS & buckets["checklist_candidates"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
