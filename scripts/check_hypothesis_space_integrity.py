#!/usr/bin/env python3
"""Anti-Goodhart audit for the Scientific Progress Dashboard's hypothesis space.

Sibling of check_closure_drift.py / check_granularity_debt_recurrence.py. The
hypothesis-space dashboard can be gamed three ways -- this catches all three and
prints them as advisory flags. It NEVER blocks: exits 0 regardless of findings
(design rule 5: "Flags are advisory, printed, non-blocking").

Checks (design rule 5):
  (a) Un-backed surviving-count drop -- a question whose surviving count fell
      (across the append-only time series, or within the registry) with no
      adjudicated `weakens`/discrimination behind the eliminations that caused it.
  (b) Post-hoc enlargement of a frozen initial set -- initial_frozen_count grew
      after registration WITHOUT a labelled fan-out or discovery-growth record,
      or a hypothesis's pre_registered_utc is AFTER the run that adjudicated it
      (retro-padding). LABELLED fan-out growth (a GOV-FANOUT-1 discrimination
      portfolio enumerating new rivals as earlier axes are eliminated) and
      LABELLED discovery growth (a genuinely serendipitous explanation found
      DURING the same analysis that resolves it, never anticipated beforehand)
      are NOT violations -- both are reported separately as advisory. See
      `labelled_fanout_growth` and `discovery_growth` in the registry's
      invariants block for the conditions each must satisfy.
  (c) Confirmed/superseded without a passed control -- a `confirmed` or
      `superseded` hypothesis whose resolution lacks control_passed == true.
      `superseded` (ratified moot/no-longer-load-bearing) needs the same
      adjudicated-control bar as `confirmed`, but is deliberately EXEMPT from
      check (d) below -- see SUPERSEDED_STATES.
  (d) Elimination-bar violation -- an `eliminated`/`split` hypothesis missing the
      full bar (met_elimination_bar + control_passed + non_degenerate == true).
      `superseded` is NOT in this bucket's state set: asserting
      met_elimination_bar true for a superseded leg would be the over-counting
      Goodhart move GOV-FROZEN-1 exists to prevent.

Also emits ADVISORY overlays that are reported but never counted as flags -- including
the GOV-FROZEN-1 fan-out/discovery RECURRENCE overlays (N >= FANOUT_RECURRENCE_N growth
events on one question), and, since 2026-08-14, an ACKNOWLEDGED bucket for a recurrence
whose question has been re-posed and closed (`growth_restriction` + zero `alive` legs).
Acknowledgement withdraws the ROUTING, never the record: see `_recurrence_acknowledged`.

Output: evidence/planning/hypothesis_space_integrity.md.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_hypothesis_space_integrity.py
    /opt/local/bin/python3 scripts/check_hypothesis_space_integrity.py --self-test
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
REGISTRY = PLANNING_DIR / "hypothesis_space_registry.v1.json"
TIMESERIES = PLANNING_DIR / "hypothesis_space_timeseries.v1.jsonl"
REPORT = PLANNING_DIR / "hypothesis_space_integrity.md"

RESOLVED_OUT_STATES = {"eliminated", "split"}
# A RATIFIED MOOT/SUPERSEDED resolution -- no longer load-bearing for its question
# whatever its own truth value (see the registry's `resolution.basis`). Deliberately
# its OWN set, disjoint from RESOLVED_OUT_STATES: that set gates check (d)'s
# elimination-bar requirement below, and a superseded leg is EXEMPT from that bar by
# design -- asserting met_elimination_bar true for one would be the over-counting
# Goodhart direction GOV-FROZEN-1 exists to prevent. build_hypothesis_space.py's
# SUPERSEDED_STATES mirrors this name; the two files intentionally do NOT share one
# constant across the module boundary (each script is hermetic -- see the
# `--self-test` docstring).
SUPERSEDED_STATES = {"superseded"}
# States needing an adjudicated, passed control (check (c)) but EXEMPT from the
# elimination bar (check (d)): `confirmed` (supports) and `superseded` (ratified
# moot). Kept distinct from RESOLVED_OUT_STATES for the same reason as above.
CONTROL_REQUIRED_STATES = {"confirmed"} | SUPERSEDED_STATES
# Buckets that are REPORTED but never counted as flags: sanctioned labelled growth,
# the quiet unverifiable-provenance state, cleared git witnesses, and the
# fan-out RECURRENCE overlay (an ACTIONABLE routing signal, still never a gate).
ADVISORY_BUCKETS = {"e_labelled_growth", "f_unverifiable", "g_witnessed",
                    "h_fanout_recurrence", "i_confirmed_backed",
                    "j_confirmed_unverifiable", "k_discovery_growth",
                    "l_discovery_recurrence", "m_recurrence_acknowledged",
                    "n_ledger_pending"}

# Distinct labelled fan-out portfolios on ONE question before the recurrence
# overlay fires. Matches GOV-CEIL-1's CEILING_EXHAUSTION_N and GOV-DIAG-1's
# DIAG_RECURRENCE_N -- same three-strikes epistemics, tunable module constant.
#
# Why this exists (GOV-FROZEN-1 escalation clause). Conditions (a)-(c) make an
# individual growth event legitimate, but legitimacy is per-event and therefore
# says nothing about RECURRENCE: a question can fan out indefinitely, clearing
# every check every time, while its denominator outruns its eliminations. That is
# precisely the alarm-fatigue vector GOV-FROZEN-1 warns about turned on the rule
# itself -- a recurring advisory with a plausible narrative ("legitimate labelled
# fan-out") is accepted by default. The sibling rules escalate on a COUNT for the
# same reason; this closes the asymmetry.
#
# NOT redundant with GOV-DIAG-1, which counts pure-diagnostic NO-VERDICT autopsies.
# Fan-out recurrence is the opposite signature: every run REACHED a verdict and
# eliminated a leg, so the chain is invisible to the no-verdict counter by
# construction. A campaign can hold perfect GOV-DIAG-1 hygiene and still never
# converge. (Confirmed empirically 2026-07-18: GOV-DIAG-1 fires on
# ree_ai_design_critique_plan:WS-1 + f_dominance_conversion_ceiling, and NOT on
# the `competence_floor` question that has fanned out twice.)
FANOUT_RECURRENCE_N = 3

# ACKNOWLEDGEMENT of a worked recurrence -- NOT suppression of it.
#
# The overlay counts portfolios, and that count never decreases (GOV-FROZEN-1 has
# no shrinkage operation, correctly). So once a question crosses N it re-fires
# every cycle FOREVER, including long after the recurrence has been re-posed,
# formally closed to further growth, and had every leg resolved. Nothing in the
# ACTIONABLE line distinguishes that from a live campaign about to open another
# portfolio -- so a reader routes work for it, again, every cycle.
#
# Confirmed cost, and this is the whole reason the bucket exists: `competence_floor`
# was re-posed and closed 2026-08-08 (`growth_restriction` written to the qid; its
# last alive leg resolved `eliminated` the same day on V3-EXQ-821b), and on
# 2026-08-12 a `/governance` session read the still-firing ACTIONABLE line and routed
# `chip-20260812-govfrozen1-repose-competence-floor` -- a duplicate re-pose of an
# already-closed campaign, FOUR DAYS after closure and after its own routed follow-on
# had itself been executed. That is precisely the alarm-fatigue Goodhart vector
# GOV-FROZEN-1 warns about, turned on the rule itself.
#
# BOTH HALVES ARE REQUIRED, and the restriction is the load-bearing one:
#
#   (i) a non-empty top-level `growth_restriction` -- the SAME field `/failure-autopsy`
#       Step 9b reads before attaching a leg to an already-registered question. It is a
#       positive, deliberate, human-authored statement that this qid is closed; and
#  (ii) zero `alive` legs -- nothing outstanding that a re-pose could still redirect.
#
# (ii) ALONE WOULD BE WRONG, and this is not hypothetical -- `competence_floor`'s own
# history falsifies it twice. It sat at 0 alive with the overlay firing on 2026-07-26
# (`ed0027587`, 3 portfolios) and again on 2026-08-02 (`ccc067123`, 5 portfolios), and
# on BOTH occasions the campaign was mid-flight, not closed: portfolio 4 opened twelve
# hours after the first (`cff9a4fe0`) and a leg went back alive five days after the
# second (`7d4e8ba0b`). A 0-alive-only predicate would have de-routed the overlay at
# exactly the two moments it was about to be proved right. A campaign between
# portfolios legitimately has no live legs; only the restriction says it is closed.
#
# And acknowledgement is NEVER silence. The line keeps being emitted, in its own
# report section, quoting the restriction verbatim, with its count carried into the
# ACTIONABLE section headers and the stdout summary -- so a closed recurrence stays
# visible and auditable. A rule that can erase its own alarm is worse than a noisy one;
# what is removed here is the ROUTING, not the record.
#
# Scope, stated honestly (CLAUDE.md held-out check, GOV-HELDOUT-1): across the
# registry's entire 77-commit history exactly ONE question has ever reached N>=3
# portfolios and exactly ONE has ever carried a `growth_restriction` -- the same one.
# So there do NOT exist 3 held-out cases where the old and new behaviour differ; there
# is 1, and it is the motivating incident. This ships scoped to that incident rather
# than as a general rule. What the check DID buy is the two negative controls above,
# which is why (i) is required rather than inferred.
def _recurrence_acknowledged(restriction: str, alive: int) -> bool:
    """True when a recurrence is WORKED (closed + nothing outstanding), not live."""
    return bool(restriction) and alive == 0


def _quote_block(text: str, indent: str = "  ") -> str:
    """Render `text` as a markdown blockquote nested under a list item."""
    return "\n".join(f"{indent}> {ln}" if ln else f"{indent}>"
                     for ln in text.splitlines())


# An adjudicated basis for an elimination: a weakens, OR a confirmed-cluster
# non_contributory discrimination that met the bar (design's own Dim-3 worked
# example treats a sub-floor discrimination against passing reference bands as an
# elimination -- see the registry's elimination_bar invariant).
ADJUDICATED_DIRECTIONS = {"weakens", "non_contributory"}


def _utc_now_iso_z() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


# --------------------------------------------------------------------------
# Git-witnessed pre-registration
#
# `pre_registered_utc` is SELF-REPORTED and written into the registry after the
# fact, so invariant 2 (pre <= resolved) is trivially satisfiable by choosing a
# convenient earlier timestamp -- no audit reading only the registry can detect
# back-dating. The witness closes that: we ask git when the claim to have
# pre-registered actually became durable, and compare THAT against the run it
# adjudicates. The honest case self-clears (its autopsy artifact was committed
# before the run resolved); the back-dated case cannot manufacture a commit.
#
# Design note (alarm fatigue is itself a Goodhart vector): a flag that recurs
# every cycle with a plausible narrative attached gets accepted by default.
# So legitimate provenance must self-clear WITHOUT human adjudication, and the
# degenerate cases (no git history yet, wholesale file rewrite, git absent) are
# reported as a quiet `unverifiable` state -- never as a violation.
# --------------------------------------------------------------------------

_GIT_CACHE: dict = {}


def _git(args: list) -> str:
    """Run a read-only git command in the repo. Returns '' on any failure --
    git being unavailable must degrade to `unverifiable`, never to a flag."""
    key = tuple(args)
    if key in _GIT_CACHE:
        return _GIT_CACHE[key]
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT)] + args,
            capture_output=True, text=True, timeout=20,
        )
        val = out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        val = ""
    _GIT_CACHE[key] = val
    return val


def _artifact_first_commit(rel_path: str) -> str:
    """Earliest commit date (ISO-8601 Z, date part) that ADDED `rel_path`.
    '' if the file has no git history (uncommitted / unknown / git absent)."""
    if not rel_path:
        return ""
    for prefix in ("evidence/planning/", ""):
        p = rel_path if rel_path.startswith(prefix) else prefix + rel_path
        out = _git(["log", "--diff-filter=A", "--format=%cI", "--", p])
        if out:
            return out.splitlines()[-1].strip()[:10]
    return ""


def _registry_first_witness(hid: str) -> str:
    """Earliest commit date that introduced `hid` into the registry file.
    This is the fallback witness when a leg carries no pre_registration_source."""
    if not hid:
        return ""
    out = _git(["log", "-S", hid, "--format=%cI", "--",
                "evidence/planning/hypothesis_space_registry.v1.json"])
    if not out:
        return ""
    return out.splitlines()[-1].strip()[:10]


def witness_pre_registration(h: dict) -> tuple:
    """Return (state, witness_date, detail) for one hypothesis.

    state is one of:
      'witnessed'    -- durable evidence of pre-registration predates the
                        adjudicating run's resolution. Self-cleared, no flag.
      'unwitnessed'  -- git history EXISTS and contradicts the claim: the
                        earliest durable record post-dates the resolution and
                        no pre_registration_source clears it. This is the
                        detectable back-dating case -> a real flag.
      'unverifiable' -- no git history to check (uncommitted leg, wholesale
                        rewrite, git unavailable). Quiet; counted, not flagged.
      'n/a'          -- the leg is unresolved, so there is nothing to back-date.
    """
    res = h.get("resolution") or {}
    resolved = (res.get("resolved_utc") or "")[:10]
    if not resolved:
        # Invariant 3's strict form: a leg whose adjudicating run has NOT
        # resolved cannot be retro-padded -- there is no evidence to have seen.
        return ("n/a", "", "adjudicating run not resolved")

    src = h.get("pre_registration_source")
    if src:
        art = _artifact_first_commit(src)
        if art and art <= resolved:
            return ("witnessed", art,
                    f"`{src}` committed {art} <= resolution {resolved}")
        if art:
            return ("unwitnessed", art,
                    f"`{src}` was committed {art}, AFTER resolution {resolved}")
        # Named source has no git history -- fall through to the registry witness.

    reg = _registry_first_witness(h.get("hid"))
    if not reg:
        return ("unverifiable", "", "no git history for this leg")
    if reg <= resolved:
        return ("witnessed", reg, f"entered the registry {reg} <= resolution {resolved}")
    return ("unwitnessed", reg,
            f"first durable record {reg} POST-DATES resolution {resolved}"
            + ("" if src else " and the leg names no `pre_registration_source`"))


def _load_timeseries(path: Path) -> list:
    out = []
    if not path.exists():
        return out
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            out.append(json.loads(ln))
        except ValueError:
            continue
    out.sort(key=lambda r: r.get("date") or "")
    return out


def _validate_fanout_events(qid: str, events: list, by_hid: dict, flags: dict) -> tuple:
    """Validate a question's LABELLED fan-out growth events against the
    registry's `labelled_fanout_growth` invariant, conditions (a)-(c).

    Growth satisfying all three is ADVISORY (bucket `e_labelled_growth`), not a
    violation. Unaccounted / unlabelled / retro-padded growth stays a REAL
    bucket-(b) flag. Returns (accounted, valid_sources).
    """
    accounted = 0
    # Keyed on the ARTIFACT, not on recorded_utc: a single backfill pass can record
    # several historically-distinct portfolios with one timestamp (and conversely a
    # re-record of one portfolio must not inflate the count). The autopsy that
    # opened the portfolio is the thing there is one of per fan-out decision.
    valid_sources = set()
    for ev in events:
        src = ev.get("fanout_source")
        hids = ev.get("added_hids") or []
        delta = int(ev.get("delta") or len(hids))
        label = f"`{qid}` fan-out {src or '<no source>'}"
        # (b) the growth must NAME the autopsy that opened the portfolio.
        if not src:
            flags["b_enlargement"].append(
                f"{label}: fanout_growth_event has no `fanout_source` -- condition (b) "
                "unmet, the growth is unlabelled."
            )
            continue
        if not hids:
            flags["b_enlargement"].append(
                f"{label}: fanout_growth_event lists no `added_hids` -- condition (b) "
                "unmet, the growth is untraceable to specific legs."
            )
            continue
        if delta != len(hids):
            flags["b_enlargement"].append(
                f"{label}: delta={delta} but {len(hids)} added_hids listed -- "
                "the growth record does not match the legs it claims to add."
            )
            continue
        # (a) STRICT (Step 9b invariant 3): growth is legitimate only for legs whose
        # adjudicating run has NOT resolved. A leg added after its own evidence is in
        # may still clear -- but only on WITNESSED provenance (a pre_registration_source
        # artifact, or a registry entry, durably committed before the run resolved).
        # The self-reported pre_registered_utc alone is NOT sufficient: it is
        # back-datable, which is what made this rule non-enforceable before.
        bad = []
        for hid in hids:
            h = by_hid.get(hid)
            if h is None:
                bad.append(f"{hid} (not in hypotheses[])")
                continue
            pre = (h.get("pre_registered_utc") or "")[:10]
            resolved = ((h.get("resolution") or {}).get("resolved_utc") or "")[:10]
            if not pre:
                bad.append(f"{hid} (no pre_registered_utc)")
                continue
            if resolved and pre > resolved:
                bad.append(f"{hid} (pre {pre} AFTER resolution {resolved})")
                continue
            state, wdate, detail = witness_pre_registration(h)
            if state == "unwitnessed":
                bad.append(
                    f"{hid} (adjudicating run already RESOLVED when the leg was added; "
                    f"{detail} -- self-reported pre_registered_utc {pre} is unwitnessed)"
                )
            elif state == "unverifiable":
                flags["f_unverifiable"].append(
                    f"`{qid}`/`{hid}`: pre-registration could not be checked against git "
                    f"({detail}). Not a violation -- but it is also not evidence. Commit "
                    "the leg (and name a `pre_registration_source`) so it self-clears."
                )
            elif state == "witnessed":
                flags["g_witnessed"].append(f"`{qid}`/`{hid}`: {detail}")
        if bad:
            flags["b_enlargement"].append(
                f"{label}: condition (a) unmet for {', '.join(bad)} -- a leg added "
                "by fan-out must pre-date the run that adjudicates it."
            )
            continue
        accounted += delta
        valid_sources.add(src)
        flags["e_labelled_growth"].append(
            f"`{qid}`: +{delta} leg(s) ({', '.join(hids)}) added by labelled fan-out "
            f"from `{src}` -- conditions (a)-(c) satisfied, advisory not a violation."
        )
    return accounted, valid_sources


def _validate_discovery_events(qid: str, events: list, by_hid: dict, flags: dict) -> tuple:
    """Validate a question's LABELLED discovery-growth events against the
    registry's `discovery_growth` invariant, conditions (i)-(iii).

    Unlike fan-out growth, a discovery leg's adjudicating run has ALREADY
    resolved by construction -- the same analysis that discovered the
    hypothesis is what resolves it, so "pre-dates the run" is structurally
    impossible to satisfy honestly. The validity test is instead "born already
    resolved, same-day, with a rationale" (condition i/ii). A leg left `alive`
    needed Mode A pre-registration BEFORE its adjudicating run instead --
    that is not what this path is for, and back-dating pre_registered_utc to
    fake it is exactly the (b) violation this ledger polices either way.

    Growth satisfying all three is ADVISORY (bucket `k_discovery_growth`), not
    a violation. Returns (accounted, valid_sources).
    """
    accounted = 0
    valid_sources = set()
    for ev in events:
        src = ev.get("discovery_source")
        hids = ev.get("added_hids") or []
        delta = int(ev.get("delta") or len(hids))
        rationale = ev.get("rationale")
        label = f"`{qid}` discovery {src or '<no source>'}"
        # (ii) the growth must NAME the discovering-and-resolving autopsy.
        if not src:
            flags["b_enlargement"].append(
                f"{label}: discovery_growth_event has no `discovery_source` -- condition "
                "(ii) unmet, the growth is unlabelled."
            )
            continue
        if not hids:
            flags["b_enlargement"].append(
                f"{label}: discovery_growth_event lists no `added_hids` -- condition (ii) "
                "unmet, the growth is untraceable to specific legs."
            )
            continue
        if delta != len(hids):
            flags["b_enlargement"].append(
                f"{label}: delta={delta} but {len(hids)} added_hids listed -- "
                "the growth record does not match the legs it claims to add."
            )
            continue
        if not rationale:
            flags["b_enlargement"].append(
                f"{label}: discovery_growth_event has no `rationale` -- condition (ii) "
                "unmet, the theory/mechanism grounding for the discovery is not recorded."
            )
            continue
        # (i) born resolved, same-day: the structural signature that distinguishes
        # genuine serendipity (discovered by the very run that resolves it) from a
        # rival that was actually anticipated and should have used Mode A instead.
        bad = []
        for hid in hids:
            h = by_hid.get(hid)
            if h is None:
                bad.append(f"{hid} (not in hypotheses[])")
                continue
            resolution = h.get("resolution") or {}
            resolved = (resolution.get("resolved_utc") or "")[:10]
            state = resolution.get("state")
            pre = (h.get("pre_registered_utc") or "")[:10]
            if not resolved or state in (None, "alive", "untested"):
                bad.append(
                    f"{hid} (not born resolved -- state={state!r}; a hypothesis left "
                    "alive needed Mode A pre-registration BEFORE its adjudicating run "
                    "instead, not discovery growth)"
                )
                continue
            if not pre:
                bad.append(f"{hid} (no pre_registered_utc)")
                continue
            if pre != resolved:
                bad.append(
                    f"{hid} (pre_registered_utc {pre} != resolved_utc {resolved} -- a "
                    "discovery leg must be born on the same day it is resolved)"
                )
                continue
        if bad:
            flags["b_enlargement"].append(
                f"{label}: condition (i) unmet for {', '.join(bad)} -- a leg added by "
                "discovery growth must be born already resolved, same-day."
            )
            continue
        accounted += delta
        valid_sources.add(src)
        flags["k_discovery_growth"].append(
            f"`{qid}`: +{delta} leg(s) ({', '.join(hids)}) added by labelled discovery "
            f"from `{src}` -- conditions (i)-(iii) satisfied, advisory not a violation. "
            f"Rationale: {rationale}"
        )
    return accounted, valid_sources


def _validate_question_growth(q: dict, flags: dict) -> int:
    """Validate a question's denominator growth against BOTH sanctioned paths --
    labelled fan-out (`labelled_fanout_growth` invariant) and labelled discovery
    (`discovery_growth` invariant) -- and reconcile the combined accounted total
    against the actual denominator move. Returns the reconciled accounted count.
    """
    qid = q.get("qid")
    initial = int(q.get("initial_frozen_count") or 0)
    # (iii)/(c) the registration-time denominator must be preserved separately.
    at_reg = q.get("initial_frozen_count_at_registration")
    fanout_events = q.get("fanout_growth_events") or []
    discovery_events = q.get("discovery_growth_events") or []
    growth = initial - int(at_reg) if at_reg is not None else 0

    if at_reg is None:
        if fanout_events or discovery_events:
            flags["b_enlargement"].append(
                f"`{qid}`: growth events recorded but "
                "initial_frozen_count_at_registration is missing -- the original "
                "denominator is not preserved."
            )
        # No growth claimed and no registration denominator: nothing to check here.
        # (b1) elsewhere still guards initial_frozen_count == len(hypotheses).
        return 0

    if growth < 0:
        flags["b_enlargement"].append(
            f"`{qid}`: initial_frozen_count={initial} is BELOW "
            f"initial_frozen_count_at_registration={at_reg} -- the frozen set shrank."
        )
        return 0

    by_hid = {h.get("hid"): h for h in (q.get("hypotheses") or [])}
    fanout_accounted, fanout_sources = _validate_fanout_events(qid, fanout_events, by_hid, flags)
    discovery_accounted, discovery_sources = _validate_discovery_events(
        qid, discovery_events, by_hid, flags)
    accounted = fanout_accounted + discovery_accounted

    if accounted < growth:
        flags["b_enlargement"].append(
            f"`{qid}`: grew {at_reg} -> {initial} (+{growth}) but only {accounted} "
            "leg(s) are covered by a valid fanout_growth_events/discovery_growth_events "
            f"entry -- {growth - accounted} unaccounted, which is post-hoc enlargement."
        )
    elif accounted > growth:
        flags["b_enlargement"].append(
            f"`{qid}`: growth events claim {accounted} added leg(s) but the "
            f"denominator only grew by {growth} ({at_reg} -> {initial}) -- "
            "the growth record and the denominator disagree."
        )
    elif growth > 0:
        # Honest-reporting reminder: a growing denominator is a non-convergence
        # signal even when it is entirely legitimate.
        n_events = len(fanout_sources) + len(discovery_sources)
        flags["e_labelled_growth"].append(
            f"`{qid}`: denominator grew {at_reg} -> {initial} across {n_events} "
            "labelled event(s) (fan-out + discovery). Legitimate; report the reduction "
            "ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, "
            "survivors on fresh territory) or CIRCLING (re-entry into already-eliminated "
            "territory) is decided by the axis-family discriminator -- read "
            "`convergence.convergence_class` for this question in hypothesis_space.v1.json "
            "rather than assuming either."
        )

    # RECURRENCE overlays (GOV-FROZEN-1 escalation). Every event counted here was
    # individually legitimate -- that is the point. The signal is the COUNT.
    #
    # `growth_restriction` is read here ONLY to BUCKET the report line (ACTIONABLE vs
    # ACKNOWLEDGED). This script stays derive-only: it never writes the field, never
    # writes the ledger, and adds no second registry producer -- the frozen ledger's
    # single producer is still `/failure-autopsy` Step 9b. See `_recurrence_acknowledged`.
    hs = q.get("hypotheses") or []
    alive = sum(1 for h in hs
                if (h.get("resolution") or {}).get("state") == "alive")
    restriction = (q.get("growth_restriction") or "").strip()
    acknowledged = _recurrence_acknowledged(restriction, alive)
    # A restriction that does NOT acknowledge is still worth saying out loud: it tells
    # the reader the qid is closed AND that the second half of the predicate is what
    # kept the line actionable, rather than leaving the mismatch to be re-derived.
    restriction_note = (
        f" NOTE: this qid carries a `growth_restriction`, but {alive} leg(s) are still "
        "alive, so the recurrence is NOT acknowledged -- both halves are required "
        "(a campaign between portfolios legitimately has no live legs)."
        if restriction and not acknowledged else ""
    )

    if len(fanout_sources) >= FANOUT_RECURRENCE_N:
        head = (
            f"`{qid}`: {len(fanout_sources)} distinct labelled fan-out portfolios "
            f"(>= N={FANOUT_RECURRENCE_N}); denominator {at_reg} -> {initial}, "
            f"{alive} leg(s) still alive."
        )
        sources = "Sources: " + ", ".join(f"`{s}`" for s in sorted(fanout_sources))
        if acknowledged:
            flags["m_recurrence_acknowledged"].append(
                f"{head} **ACKNOWLEDGED (fan-out).** The qid carries a "
                "`growth_restriction` closing it to further growth AND no leg is still "
                "alive, so this recurrence has been WORKED -- it needs no re-pose "
                "routing this cycle. Reported, never suppressed: the count does not "
                "decrease and the overlay does not clear itself. Re-read the "
                "restriction before treating any new portfolio on this qid as "
                f"sanctioned. {sources}\n\n"
                "  Restriction, verbatim:\n\n" + _quote_block(restriction)
            )
        else:
            flags["h_fanout_recurrence"].append(
                f"{head} Each portfolio cleared conditions (a)-(c) "
                "individually -- the RECURRENCE is the signal. Reading: the question may "
                "be MIS-POSED rather than under-enumerated. Re-pose the operationalization "
                "before opening portfolio "
                f"{len(fanout_sources) + 1}; enumerating another round of rivals on an "
                "unchanged framing is the denominator-side twin of re-running a braked "
                f"experiment harder.{restriction_note} " + sources
            )
    if len(discovery_sources) >= FANOUT_RECURRENCE_N:
        # Same acknowledgement, because `growth_restriction` governs the discovery path
        # too: /failure-autopsy Step 9b applies it to "Mode C in every case (discovery
        # growth is by construction growth of an existing question)". Leaving this
        # overlay unacknowledged would say a closed qid is closed to fan-out but still
        # routes on discovery -- an asymmetry the field itself does not have. No live
        # case exercises it (no question has ever exceeded 1 discovery source), so it is
        # pinned by the self-test rather than by production.
        head = (
            f"`{qid}`: {len(discovery_sources)} distinct labelled discovery-growth "
            f"events (>= N={FANOUT_RECURRENCE_N}); denominator {at_reg} -> {initial}."
        )
        sources = "Sources: " + ", ".join(f"`{s}`" for s in sorted(discovery_sources))
        if acknowledged:
            flags["m_recurrence_acknowledged"].append(
                f"{head} {alive} leg(s) still alive. **ACKNOWLEDGED (discovery).** The "
                "qid carries a `growth_restriction` closing it to further growth AND no "
                "leg is still alive, so this recurrence has been WORKED -- it needs no "
                "routing this cycle. Reported, never suppressed. "
                f"{sources}\n\n  Restriction, verbatim:\n\n" + _quote_block(restriction)
            )
        else:
            flags["l_discovery_recurrence"].append(
                f"{head} "
                "Each event cleared conditions (i)-(iii) individually -- the RECURRENCE is "
                "the signal. Reading: 'discovery' may be substituting for pre-registration "
                "discipline rather than genuine one-off serendipity -- check whether a rival "
                "hypothesis was actually anticipated before its adjudicating run and should "
                f"have gone through Mode A pre-registration instead.{restriction_note} "
                + sources
            )
    return min(accounted, growth)


_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

# A date with no time carries no intra-day ordering, so it is pinned to the END of
# its day. That is the only choice that keeps a same-day event in exactly ONE
# window: it sorts after any snapshot taken earlier that day (so it attributes to
# the window it actually landed in) and before the next day's snapshot (so it
# cannot also be claimed by the preceding window).
_END_OF_DAY = "T23:59:59Z"


def _instant(value: str) -> str:
    """Normalise a registry/timeseries timestamp to a comparable ISO instant.

    Accepts a full `...THH:MM:SSZ` timestamp (used verbatim), a bare `YYYY-MM-DD`,
    or any string carrying a date (e.g. a source artifact FILENAME, which is the
    fallback when an event predates the `recorded_utc` field). Returns '' if no
    date can be read at all.
    """
    if not value:
        return ""
    m = _DATE_RE.search(value)
    if not m:
        return ""
    date = m.group(1)
    # Only trust a time component that actually came with this date.
    rest = value[m.end():]
    if rest.startswith("T") and len(rest) >= 9:
        return value[m.start():m.end() + 9].rstrip("Z") + "Z"
    return date + _END_OF_DAY


def _event_instant(ev: dict) -> str:
    """When a fan-out or discovery growth event happened.

    Honours an explicit `recorded_utc` / `event_utc` on the event; falls back to
    the date embedded in the source artifact's filename only when neither is
    present. The explicit field matters because a portfolio designed the same day
    as the previous snapshot but recorded AFTER it is otherwise structurally
    unattributable -- the false positive this fallback ordering causes.
    """
    for key in ("recorded_utc", "event_utc"):
        got = _instant(ev.get(key) or "")
        if got:
            return got
    return _instant(ev.get("fanout_source") or ev.get("discovery_source") or "")


def _snapshot_instant(row: dict) -> str:
    """Window bound for a time-series row: the real `snapshot_utc` when present."""
    return _instant(row.get("snapshot_utc") or "") or _instant(row.get("date") or "")


def audit(registry: dict, timeseries: list) -> dict:
    """Return {flag_bucket: [messages]} for each of the four checks, plus the
    advisory `e_labelled_growth` bucket (labelled fan-out; NOT a violation)."""
    flags = {"a_unbacked_drop": [], "b_enlargement": [],
             "c_confirmed_no_control": [], "d_bar_violation": [],
             "e_labelled_growth": [], "f_unverifiable": [], "g_witnessed": [],
             "h_fanout_recurrence": [], "i_confirmed_backed": [],
             "j_confirmed_unverifiable": [], "k_discovery_growth": [],
             "l_discovery_recurrence": [], "m_recurrence_acknowledged": []}
    questions = registry.get("questions") or []
    # Total legs added by VALID labelled fan-out, keyed by the INSTANT the growth
    # was recorded -- lets the time-series check attribute a total_initial rise.
    # Keyed on a full timestamp rather than a date so that an event landing later
    # on the same day as the previous snapshot still attributes to its own window.
    labelled_growth_by_date: dict = {}

    for q in questions:
        qid = q.get("qid")
        initial = int(q.get("initial_frozen_count") or 0)
        n_hyps = len(q.get("hypotheses") or [])
        # (b1) denominator consistency: initial_frozen_count must equal the number
        # of pre-registered hypotheses (no phantom denominator padding).
        if initial != n_hyps:
            flags["b_enlargement"].append(
                f"`{qid}`: initial_frozen_count={initial} but {n_hyps} hypotheses "
                "registered -- denominator does not match the enumerated set."
            )
        # (b3) labelled fan-out / discovery growth of an EXISTING question.
        _validate_question_growth(q, flags)
        for ev in (q.get("fanout_growth_events") or []) + (q.get("discovery_growth_events") or []):
            date = _event_instant(ev)
            if date:
                labelled_growth_by_date[date] = (
                    labelled_growth_by_date.get(date, 0) + int(ev.get("delta") or 0))
        # A newly-registered question also legitimately grows total_initial.
        reg_date = _instant(q.get("registered_utc") or "")
        at_reg = q.get("initial_frozen_count_at_registration")
        if reg_date:
            labelled_growth_by_date[reg_date] = (
                labelled_growth_by_date.get(reg_date, 0)
                + int(at_reg if at_reg is not None else initial))
        for h in q.get("hypotheses") or []:
            hid = h.get("hid")
            res = h.get("resolution") or {}
            state = res.get("state") or "untested"
            pre = (h.get("pre_registered_utc") or "")[:10]
            resolved = (res.get("resolved_utc") or "")[:10]
            direction = (res.get("evidence_direction") or "").lower()

            # (b2) retro-padding: a hypothesis pre-registered AFTER the run that
            # adjudicated it (evidence was already in when it was "pre"-registered).
            if pre and resolved and pre > resolved:
                flags["b_enlargement"].append(
                    f"`{qid}`/`{hid}`: pre_registered_utc {pre} is AFTER its "
                    f"resolution {resolved} -- retro-padded pre-registration."
                )

            # (c) confirmed/superseded without a passed control.
            if state in CONTROL_REQUIRED_STATES and res.get("control_passed") is not True:
                flags["c_confirmed_no_control"].append(
                    f"`{qid}`/`{hid}`: state={state} but control_passed="
                    f"{res.get('control_passed')!r} -- a {state} node needs a passed control."
                )

            # (d) elimination-bar violation.
            if state in RESOLVED_OUT_STATES:
                missing = []
                if res.get("met_elimination_bar") is not True:
                    missing.append("met_elimination_bar")
                if res.get("control_passed") is not True:
                    missing.append("control_passed")
                if res.get("non_degenerate") is not True:
                    missing.append("non_degenerate")
                if missing:
                    flags["d_bar_violation"].append(
                        f"`{qid}`/`{hid}`: state={state} but missing "
                        f"{', '.join(missing)} -- elimination requires the full bar."
                    )
                # (a-registry) un-backed elimination: no adjudicated direction.
                if direction not in ADJUDICATED_DIRECTIONS and direction != "supports":
                    flags["a_unbacked_drop"].append(
                        f"`{qid}`/`{hid}`: eliminated with evidence_direction="
                        f"{direction!r} (no adjudicated weakens/discrimination behind the drop)."
                    )

    # (a-timeseries) a total_surviving drop across snapshots must be matched by a
    # rise in total_resolved_out (adjudicated eliminations). A bare drop with no
    # corresponding resolution is the classic Goodhart move.
    for prev, cur in zip(timeseries, timeseries[1:]):
        d_surv = (cur.get("total_surviving") or 0) - (prev.get("total_surviving") or 0)
        d_res = (cur.get("total_resolved_out") or 0) - (prev.get("total_resolved_out") or 0)
        d_init = (cur.get("total_initial") or 0) - (prev.get("total_initial") or 0)
        if d_surv < 0 and d_res <= 0 and d_init <= 0:
            # A `confirmed` resolution (supports + control_passed) also
            # legitimately removes a hypothesis from "surviving": per
            # build_hypothesis_space._question_rollup, surviving == alive
            # whenever alive > 0, so an alive -> confirmed transition on a
            # question with other alive legs remaining drops the total with NO
            # elimination behind it -- resolved_out only ever counts
            # eliminated/split. Before total_confirmed existed in the ledger
            # this read as an unbacked drop -- confirmed false positive
            # 2026-08-02 on H-zworld-trained-instrument (V3-EXQ-819a landed the
            # confirmation into the registry on 2026-07-30, inside the
            # 07-29->07-30 window; check_hypothesis_space_integrity.md kept
            # reporting it as unbacked because nothing credited the
            # confirmation). total_confirmed is only populated going forward
            # (build_hypothesis_space.py), so an existing snapshot missing it
            # on either side cannot be checked either way -- treated as
            # unverifiable (quiet), never as a violation, matching the
            # git-witness provenance design elsewhere in this file (insufficient
            # data reads as "cannot tell", not as "therefore a violation").
            #
            # A `superseded` resolution (SUPERSEDED_STATES) is the SAME shape of
            # legitimate non-eliminating drop, added 2026-08-19 alongside the
            # registry vocabulary itself -- an alive -> superseded transition also
            # drops `surviving` with no elimination behind it. total_superseded
            # gets the identical missing-field-is-unverifiable treatment (it is
            # absent from every snapshot recorded before this date), and a
            # snapshot pair is credited on the COMBINED confirmed+superseded
            # delta, since either kind of resolution explains the same drop.
            conf_prev, conf_cur = prev.get("total_confirmed"), cur.get("total_confirmed")
            sup_prev, sup_cur = prev.get("total_superseded"), cur.get("total_superseded")
            if conf_prev is None or conf_cur is None or sup_prev is None or sup_cur is None:
                flags["j_confirmed_unverifiable"].append(
                    f"time series {prev.get('date')} -> {cur.get('date')}: surviving fell by "
                    f"{-d_surv} with no rise in resolved_out, but total_confirmed and/or "
                    "total_superseded is absent from one or both snapshots (predates the "
                    "field) so a confirmation/supersession-explained drop cannot be ruled "
                    "out -- unverifiable, not a violation."
                )
            else:
                d_credited = (conf_cur - conf_prev) + (sup_cur - sup_prev)
                if d_credited > 0:
                    flags["i_confirmed_backed"].append(
                        f"time series {prev.get('date')} -> {cur.get('date')}: surviving fell "
                        f"by {-d_surv}, backed by {d_credited} newly-confirmed/superseded "
                        "hypothesis(es) (an adjudicated resolution, not an elimination) -- "
                        "advisory, not a violation."
                    )
                else:
                    flags["a_unbacked_drop"].append(
                        f"time series {prev.get('date')} -> {cur.get('date')}: "
                        f"surviving fell by {-d_surv} but resolved_out did not rise "
                        f"(delta_resolved_out={d_res}) -- drop is not backed by adjudicated eliminations."
                    )
        # (b-timeseries) frozen initial set grew. Attribute the rise to labelled
        # sources landing in this window -- new-question registrations and valid
        # fan-out growth events. Only the UNATTRIBUTED remainder is a violation.
        if d_init > 0:
            # Compare on the snapshots' real `snapshot_utc` instants, not their
            # coarse `date`. With day granularity a growth event whose source is
            # dated the SAME DAY as the previous snapshot but which lands AFTER it
            # is structurally unattributable -- `lo < date` excludes it and the legs
            # fall through into the real-violation branch below. Confirmed as a
            # false positive on the 2026-07-18 -> 2026-07-19 window (the
            # competence_floor retention portfolio, recorded 18T18:37Z, 22 minutes
            # after the 18T18:15Z snapshot). The bound stays STRICT on the low side
            # and inclusive on the high side, so each event is still attributable to
            # exactly one window -- genuinely unlabelled growth has no instant to
            # match and remains a bucket-(b) violation.
            lo, hi = _snapshot_instant(prev), _snapshot_instant(cur)
            lo_label, hi_label = prev.get("date") or lo, cur.get("date") or hi
            attributed = sum(
                n for date, n in labelled_growth_by_date.items() if lo < date <= hi
            )
            if attributed >= d_init:
                flags["e_labelled_growth"].append(
                    f"time series {lo_label} -> {hi_label}: total_initial grew by {d_init}, fully "
                    f"attributed to labelled sources landing in this window "
                    f"(new-question registrations + fanout_growth_events, {attributed} "
                    "leg(s)) -- advisory, not a violation."
                )
            else:
                flags["b_enlargement"].append(
                    f"time series {lo_label} -> {hi_label}: total_initial grew by {d_init} but only "
                    f"{attributed} leg(s) are attributable to a labelled source -- "
                    f"{d_init - attributed} enlarged the frozen denominator unlabelled."
                )
    return flags


# ---------------------------------------------------------------------------
# Ledger-pending scan (advisory bucket `n_ledger_pending`)
#
# WHY THIS EXISTS. `/failure-autopsy` in STAGING MODE must not write this
# registry -- it is a live dashboard input -- so Step 9b instead DRAFTS its
# intended Mode A/B/C edits into a `hypothesis_space_ledger_pending` field on
# the autopsy artifact, for "the confirming interactive session or the next
# /governance walk" to apply. Until 2026-09-03 nothing applied those blocks and,
# worse, nothing CHECKED that they had been applied: a grep for the field name
# across REE_assembly/scripts/ and REE_Working/scripts/ returned zero hits while
# 34 confirmed artifacts carried one, the oldest from 2026-07-19. The concrete
# failure that surfaced the gap: failure_autopsy_V3-EXQ-976_2026-09-02 drafted
# three pre-registered legs for `sd_e1_residual_crush_locus` and they were still
# absent a day later, so V3-EXQ-980 adjudicated a leg (`H-readout-regime`) that
# did not exist in the ledger. A drafted edit with no applier and no auditor is
# indistinguishable from an applied one -- which is the same silent-no-op-reads-
# as-success failure this script's own fail-open handler exists to prevent.
#
# WHAT IT DETECTS, per CONFIRMED artifact carrying a block: a `qid` the block
# names that is absent from the registry; a `hid` it names that is absent from
# every question; and a `hid` whose registry state has not reached the resolved
# state the block intends. That last clause is the one that catches a drafted
# Mode B resolve nobody ever applied -- the 861f-mech180-cluster-a case, deferred
# by TASK_CLAIMS arbitration on 2026-08-25 and then simply forgotten.
#
# WHAT IT DELIBERATELY DOES NOT DETECT, and why:
#   (1) A registry state MORE resolved than the block intended is never flagged.
#       That is ordinary supersession by a later, better-informed autopsy
#       (816c-822 drafted `alive`; the 2026-07-28 sweep later confirmed the same
#       leg on further evidence). Flagging it would train readers to skip the
#       section, which costs more than the miss.
#   (2) No comparison of `basis` prose, `resolving_runs`, decision blocks, or
#       axis-family rows. These blocks are free-form -- 34 artifacts share no two
#       identical schemas -- so a deeper equality check would be guesswork
#       reported as fact.
#   (3) Sub-trees a block marks as explicitly NOT recommended
#       (`if_the_confirming_session_disagrees`, `optional_new_question_sketch`,
#       `optional_cosmetic_corroboration`) are pruned before the walk. Reading a
#       declined alternative as an owed edit is the obvious false-positive
#       source, and these are its named carriers.
# So a QUIET result means "nothing this scan can see is missing", NOT "every
# block was applied". It is a floor on the hole, not a proof of its absence.
#
# NOT a duplicate of `check_unapplied_autopsy_recommendations.py` (GOV-APPLY-1),
# which asks the same "was the verdict ever APPLIED?" question one plane over:
# that audit walks a confirmed autopsy's `recommended_*` fields against the CLAIMS
# layer (claims.yaml / substrate_queue.json); this one walks its Step 9b draft
# against the LEDGER. An artifact can be clean under one and dirty under the
# other -- 861f-mech180-cluster-a landed its claim-side routing while its ledger
# block sat unapplied for nine days.
#
# ADVISORY, like every bucket here: exits 0, gates nothing. A block a human has
# deliberately decided NOT to apply (superseded by a later adjudication) keeps
# appearing until that decision is recorded ON the block -- set `applied: true`,
# `registry_written: true`, an `applied_utc`, or `superseded_by: "<artifact>"`,
# and the scan goes quiet for it. Recording the disposition is the fix; deleting
# the field is not.
# ---------------------------------------------------------------------------
LEDGER_PENDING_FIELD = "hypothesis_space_ledger_pending"
AUTOPSY_GLOB = "failure_autopsy_*.json"
# Only a CONFIRMED artifact's block is OWED. A staging artifact still at
# `awaiting_human_confirmation` has not passed its own Step 8 gate, so its draft
# is correctly pending rather than missing -- flagging it would report the
# skill working as designed as a defect.
LEDGER_PENDING_OWED_STATUS = "confirmed"
_PENDING_HYPOTHETICAL_KEYS = {"if_the_confirming_session_disagrees",
                              "optional_new_question_sketch",
                              "optional_cosmetic_corroboration"}
_PENDING_QID_KEYS = ("qid", "question_qid", "question", "candidate_qid")
_PENDING_HID_KEYS = ("hid", "hypothesis")
_PENDING_STATE_KEYS = ("state", "proposed_state")
_PENDING_RES_KEYS = ("resolution", "resolution_patch")
# Any TRUTHY one of these means the block records its own disposition. Truthiness
# matters: several blocks carry `"applied_utc": null`, which asserts the opposite.
_PENDING_SETTLED_KEYS = ("applied", "registry_written", "applied_utc", "superseded_by")
# untested < alive < resolved. Everything resolved ranks equally: the check asks
# "has the registry got at least this far", never "is it in exactly this state".
_PENDING_STATE_RANK = {"untested": 0, "alive": 1}


def _pending_state_rank(state: str) -> int:
    return _PENDING_STATE_RANK.get(state or "untested", 2)


def _prune_hypothetical(node):
    """Drop sub-trees a block marks as explicitly NOT recommended."""
    if isinstance(node, dict):
        return {k: _prune_hypothetical(v) for k, v in node.items()
                if k not in _PENDING_HYPOTHETICAL_KEYS}
    if isinstance(node, list):
        return [_prune_hypothetical(v) for v in node]
    return node


def _collect_pending_intents(block, known_hids: set) -> tuple:
    """Return (qids_named, {hid: intended_state_or_None}) for one pending block."""
    qids, intents = set(), {}

    def record(hid, state):
        # A later mention carrying a state beats an earlier bare one.
        if hid not in intents or (intents[hid] is None and state is not None):
            intents[hid] = state

    def state_of(node):
        for k in _PENDING_STATE_KEYS:
            if isinstance(node.get(k), str):
                return node[k]
        for k in _PENDING_RES_KEYS:
            sub = node.get(k)
            if isinstance(sub, dict) and isinstance(sub.get("state"), str):
                return sub["state"]
        return None

    def walk(node):
        if isinstance(node, dict):
            for k in _PENDING_QID_KEYS:
                v = node.get(k)
                if isinstance(v, str) and v:
                    qids.add(v)
            for k in _PENDING_HID_KEYS:
                v = node.get(k)
                if isinstance(v, str) and v:
                    record(v, state_of(node))
            # `intended: {"<hid>": {...,"resolution":{...}}}` -- the hid is the
            # KEY, not a value, so the value-keyed clauses above never see it.
            # Gated on `known_hids` so an arbitrary key can never be read as one.
            for k, v in node.items():
                if k in known_hids and isinstance(v, dict):
                    record(k, state_of(v))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(block)
    return qids, intents


def scan_ledger_pending(registry: dict, planning_dir=None) -> list:
    """Confirmed autopsy blocks whose drafted ledger edit is not in the registry.

    Kept OUT of `audit()` on purpose: `audit()` is a pure function of
    (registry, timeseries) and its self-test cases lean on that, while this
    reads the planning directory. `main()` merges the result into `flags`.
    """
    planning_dir = Path(planning_dir) if planning_dir is not None else PLANNING_DIR
    questions = registry.get("questions") or []
    known_qids = {q.get("qid") for q in questions}
    state_by_hid = {}
    for q in questions:
        for h in (q.get("hypotheses") or []):
            state_by_hid[h.get("hid")] = (h.get("resolution") or {}).get("state") or "untested"
    known_hids = set(state_by_hid)

    msgs = []
    for path in sorted(Path(planning_dir).glob(AUTOPSY_GLOB)):
        art = _load_json(path)
        if not isinstance(art, dict):
            continue
        block = art.get(LEDGER_PENDING_FIELD)
        if not isinstance(block, dict) or not block:
            continue
        if (art.get("status") or "") != LEDGER_PENDING_OWED_STATUS:
            continue
        if any(block.get(k) for k in _PENDING_SETTLED_KEYS):
            continue
        qids, intents = _collect_pending_intents(
            _prune_hypothetical(block), known_hids)
        gaps = []
        for qid in sorted(q for q in qids if q not in known_qids):
            gaps.append(f"question `{qid}` absent from the registry")
        for hid, want in sorted(intents.items()):
            if hid not in known_hids:
                gaps.append(f"hypothesis `{hid}` absent from the registry")
            elif want and _pending_state_rank(want) > _pending_state_rank(state_by_hid[hid]):
                gaps.append(f"`{hid}` drafted as `{want}`, registry has "
                            f"`{state_by_hid[hid]}`")
        if gaps:
            msgs.append(f"`{path.name}`: " + "; ".join(gaps))
    return msgs


def render_report(flags: dict, registry: dict, timeseries: list, now: str) -> str:
    # `e_labelled_growth` is ADVISORY -- it is reported, but never counted as a flag.
    total = sum(len(v) for k, v in flags.items() if k not in ADVISORY_BUCKETS)
    n_advisory = len(flags.get("e_labelled_growth") or [])
    n_unverifiable = len(flags.get("f_unverifiable") or [])
    n_witnessed = len(flags.get("g_witnessed") or [])
    n_recurrence = len(flags.get("h_fanout_recurrence") or [])
    n_discovery = len(flags.get("k_discovery_growth") or [])
    n_discovery_recurrence = len(flags.get("l_discovery_recurrence") or [])
    n_acknowledged = len(flags.get("m_recurrence_acknowledged") or [])
    L = []
    L.append("# Hypothesis-Space Integrity Audit (anti-Goodhart)")
    L.append("")
    L.append(f"Generated: {now}")
    L.append("")
    L.append(
        "GENERATED FILE -- do not edit by hand. Advisory, non-blocking sibling of "
        "`check_closure_drift.py`. It audits `hypothesis_space_registry.v1.json` + "
        "`hypothesis_space_timeseries.v1.jsonl` for the four ways the Narrow/Decide "
        "dashboard could be gamed (design rule 5). Flags are review hints, never a gate. "
        "LABELLED GOV-FANOUT-1 growth of an existing question is reported separately as "
        "advisory (see the final section) rather than counted as a bucket-(b) violation."
    )
    L.append("")
    n_q = len(registry.get("questions") or [])
    L.append(
        f"Audited **{n_q}** open question(s) across **{len(timeseries)}** time-series "
        f"snapshot(s). **{total}** flag(s) raised, **{n_advisory}** advisory note(s), "
        f"**{n_witnessed}** git-witnessed pre-registration(s), "
        f"**{n_unverifiable}** unverifiable, "
        f"**{n_recurrence}** fan-out recurrence overlay(s), "
        f"**{n_discovery}** discovery-growth note(s), "
        f"**{n_discovery_recurrence}** discovery-recurrence overlay(s), "
        f"**{n_acknowledged}** acknowledged (worked) recurrence(s)."
    )
    L.append("")
    sections = [
        ("a_unbacked_drop", "(a) Un-backed surviving-count drop",
         "A question's surviving count fell with no adjudicated `weakens`/discrimination behind the elimination."),
        ("b_enlargement", "(b) Post-hoc enlargement of a frozen set",
         "The frozen initial enumeration grew WITHOUT a valid labelled fan-out record, "
         "or a hypothesis was pre-registered after its own adjudicating run. "
         "Labelled GOV-FANOUT-1 growth is NOT counted here -- see the advisory section below."),
        ("c_confirmed_no_control", "(c) Confirmed/superseded without a passed control",
         "A `confirmed` or `superseded` hypothesis lacks control_passed == true."),
        ("d_bar_violation", "(d) Elimination-bar violation",
         "An `eliminated`/`split` hypothesis is missing part of the bar (met_elimination_bar + control_passed + non_degenerate)."),
    ]
    for key, title, desc in sections:
        items = flags.get(key) or []
        L.append(f"## {title} ({len(items)})")
        L.append("")
        L.append(f"_{desc}_")
        L.append("")
        if not items:
            L.append("_None._")
        else:
            for msg in items:
                L.append(f"- {msg}")
        L.append("")

    adv = flags.get("e_labelled_growth") or []
    L.append(f"## Advisory -- labelled fan-out growth ({len(adv)}, NOT violations)")
    L.append("")
    L.append(
        "_An existing question's hypothesis set grew because a GOV-FANOUT-1 discrimination "
        "portfolio enumerated new rival explanations as earlier axes were eliminated. This "
        "is permitted when the growth satisfies (a) each new leg pre-dates its adjudicating "
        "run, (b) it is recorded in `fanout_growth_events[]` naming the autopsy that opened "
        "the portfolio, and (c) `initial_frozen_count_at_registration` is preserved. These "
        "are LABELLED, not flagged._"
    )
    L.append("")
    L.append(
        "**Read these alongside the convergence class, not as an all-clear.** The "
        "denominator grows mostly by legs that are then eliminated, which inflates the "
        "headline narrowing ratio -- so the dashboard reports surviving/original AND "
        "surviving/current-including-fan-out. But growth alone does NOT mean a campaign is "
        "failing: the axis-family discriminator (`convergence.convergence_class` in "
        "`hypothesis_space.v1.json`) separates **refining** (an axis family was closed out "
        "and the survivors sit on fresh territory -- count grows while the KIND of answer "
        "narrows) from **circling** (new legs re-enter already-eliminated families, the "
        "leg-level analogue of the re-derive brake) and **scattering** (nothing ever closed). "
        "Cite the class when you report growth."
    )
    L.append("")
    if not adv:
        L.append("_None._")
    else:
        for msg in adv:
            L.append(f"- {msg}")
    L.append("")

    conf_backed = flags.get("i_confirmed_backed") or []
    conf_unv = flags.get("j_confirmed_unverifiable") or []
    L.append(
        f"## Advisory -- surviving-count drop backed by confirmation/supersession "
        f"({len(conf_backed)} backed, {len(conf_unv)} unverifiable, NOT violations)"
    )
    L.append("")
    L.append(
        "_A `confirmed` resolution (supports + control_passed) or a `superseded` resolution "
        "(ratified moot, added 2026-08-19) also legitimately removes a hypothesis from "
        "`surviving`, exactly like an elimination does -- `surviving` counts alive legs, so an "
        "alive -> confirmed/superseded transition drops the total with no elimination behind "
        "it. `total_confirmed` (build_hypothesis_space.py, added 2026-08-02) and "
        "`total_superseded` (added 2026-08-19) let this check credit either instead of reading "
        "the drop as unbacked. A snapshot pair predating either field is UNVERIFIABLE, not a "
        "violation -- same quiet-on-insufficient-data design as the git-witness provenance "
        "check below._"
    )
    L.append("")
    if conf_backed:
        L.append("**Backed (drop fully explained by a confirmation/supersession):**")
        L.append("")
        for msg in conf_backed:
            L.append(f"- {msg}")
        L.append("")
    if conf_unv:
        L.append(
            "**Unverifiable (quiet -- total_confirmed and/or total_superseded absent from "
            "one or both snapshots):**"
        )
        L.append("")
        for msg in conf_unv:
            L.append(f"- {msg}")
        L.append("")
    if not conf_backed and not conf_unv:
        L.append("_No surviving-count drop needed a confirmation check this cycle._")
        L.append("")

    rec = flags.get("h_fanout_recurrence") or []
    L.append(f"## Fan-out recurrence (ACTIONABLE, {len(rec)}) -- N >= {FANOUT_RECURRENCE_N} portfolios on one question")
    L.append("")
    L.append(
        "_GOV-FROZEN-1 escalation clause. Conditions (a)-(c) license an INDIVIDUAL growth "
        "event, so they say nothing about recurrence: a question can fan out indefinitely, "
        "clearing every check every time, while its denominator outruns its eliminations. "
        "Every portfolio counted below was individually legitimate -- **the recurrence is "
        "the signal**, and the reading is that the question may be MIS-POSED rather than "
        "under-enumerated._"
    )
    L.append("")
    L.append(
        "_Complementary to GOV-DIAG-1, not redundant with it: that rule counts "
        "pure-diagnostic NO-VERDICT chains, whereas fan-out recurrence is the opposite "
        "signature -- every run reached a verdict and eliminated a leg. A campaign can "
        "hold perfect GOV-DIAG-1 hygiene and still never converge._"
    )
    L.append("")
    L.append(
        "**Response is routing, not demotion.** These are questions, not claims; nothing "
        "is promoted or demoted. Re-pose the operationalization before opening another "
        "portfolio -- enumerating a further round of rivals on an unchanged framing is the "
        "denominator-side twin of re-running a braked experiment harder. Warn-only: this "
        "never gates a cycle."
    )
    L.append("")
    L.append(
        f"**A count of 0 here is NOT the same as 'no recurrence'.** {n_acknowledged} "
        "recurrence(s) are ACKNOWLEDGED this cycle and listed in the next section rather "
        "than here -- read both before concluding the ledger is quiet."
    )
    L.append("")
    if not rec:
        L.append("_None._")
    else:
        for msg in rec:
            L.append(f"- {msg}")
    L.append("")

    ack = flags.get("m_recurrence_acknowledged") or []
    L.append(
        f"## Recurrence acknowledged ({len(ack)}, advisory) -- worked, not live"
    )
    L.append("")
    L.append(
        "_A recurrence overlay whose question has since been RE-POSED and formally closed. "
        "The portfolio count never decreases (GOV-FROZEN-1 has no shrinkage operation, "
        "correctly), so a question that crossed N goes on firing forever -- including long "
        "after every leg was resolved and the qid was closed to further growth. Listing "
        "those alongside live ones is a duplicate-work generator that fires once per "
        "governance cycle per closed campaign, which is the alarm-fatigue Goodhart vector "
        "GOV-FROZEN-1 warns about turned on the rule itself. Confirmed: `competence_floor` "
        "closed 2026-08-08 and a governance cycle routed a re-pose chip for it on "
        "2026-08-12, four days later._"
    )
    L.append("")
    L.append(
        "**Acknowledgement is not suppression.** The line is still emitted, the "
        "restriction is quoted verbatim, and the count appears in the summary above and in "
        "both ACTIONABLE section headers. Nothing here clears itself silently -- what is "
        "withdrawn is the routing, not the record. **Two conditions, both required:** the "
        "question carries a non-empty top-level `growth_restriction` (the same field "
        "`/failure-autopsy` Step 9b reads before attaching a leg), AND it has zero `alive` "
        "legs. Zero-alive alone is deliberately NOT sufficient: a campaign between "
        "portfolios legitimately has no live legs, and `competence_floor` sat at 0 alive "
        "twice while still live -- twelve hours before it opened portfolio 4 (2026-07-26) "
        "and five days before a leg went back alive (2026-08-02)."
    )
    L.append("")
    L.append(
        "**Re-read the restriction before treating any new growth on these questions as "
        "sanctioned.** A restriction names its own exception conditions; an acknowledged "
        "recurrence that starts growing again is a real finding, not a resolved one."
    )
    L.append("")
    if not ack:
        L.append("_None._")
    else:
        for msg in ack:
            L.append(f"- {msg}")
    L.append("")

    disc = flags.get("k_discovery_growth") or []
    L.append(f"## Advisory -- labelled discovery growth ({len(disc)}, NOT violations)")
    L.append("")
    L.append(
        "_An existing question's hypothesis set grew because a genuinely serendipitous "
        "explanation was found DURING the same analysis that resolves it -- discovered "
        "while explaining away already-pre-registered rivals, never anticipated "
        "beforehand. This is DIFFERENT from labelled fan-out growth above: by "
        "construction no artifact can pre-date a discovery made by the very run that "
        "reveals it, so this path does not require (and cannot honestly satisfy) the "
        "pre-dates-the-run witness fan-out growth needs. It is permitted instead when "
        "(i) the hypothesis is born already resolved in the same edit (never left "
        "`alive`), (ii) it is recorded in `discovery_growth_events[]` naming the "
        "discovering-and-resolving autopsy plus a `rationale` grounding why this is "
        "principled abduction and not motivated post-hoc reasoning, and (iii) "
        "`initial_frozen_count_at_registration` is preserved. These are LABELLED, not "
        "flagged._"
    )
    L.append("")
    L.append(
        "**A hypothesis left `alive` never qualifies here.** If a leg is not resolved "
        "in the same edit, it needed Mode A pre-registration BEFORE its adjudicating "
        "run instead -- back-dating `pre_registered_utc` to make an actually-anticipated "
        "rival look like a discovery is exactly the (b) violation this ledger polices, "
        "whichever door it is walked through."
    )
    L.append("")
    if not disc:
        L.append("_None._")
    else:
        for msg in disc:
            L.append(f"- {msg}")
    L.append("")

    disc_rec = flags.get("l_discovery_recurrence") or []
    L.append(
        f"## Discovery-growth recurrence (ACTIONABLE, {len(disc_rec)}) -- "
        f"N >= {FANOUT_RECURRENCE_N} discovery events on one question"
    )
    L.append("")
    L.append(
        "_Mirrors the fan-out recurrence overlay above, for the discovery-growth path. "
        "Every event counted below was individually legitimate -- **the recurrence is "
        "the signal**: a question racking up repeated 'discoveries' may be using this "
        "path as a substitute for pre-registration discipline (an actually-anticipated "
        "rival hypothesis being called a discovery each time to dodge Mode A) rather "
        "than genuine one-off serendipity. Response is routing -- check whether the "
        "next candidate explanation was really unforeseeable before treating it as "
        "another discovery. Warn-only: this never gates a cycle._"
    )
    L.append("")
    L.append(
        "**Same acknowledgement rule as the fan-out overlay above** -- a closed question "
        "with no alive legs is listed under 'Recurrence acknowledged', not here, because "
        "`growth_restriction` governs the discovery path too (Step 9b applies it to Mode C "
        "in every case). A count of 0 here is not by itself evidence of no recurrence."
    )
    L.append("")
    if not disc_rec:
        L.append("_None._")
    else:
        for msg in disc_rec:
            L.append(f"- {msg}")
    L.append("")

    wit = flags.get("g_witnessed") or []
    unv = flags.get("f_unverifiable") or []
    L.append(f"## Pre-registration provenance ({len(wit)} witnessed, {len(unv)} unverifiable)")
    L.append("")
    L.append(
        "_`pre_registered_utc` is SELF-REPORTED and written into the registry after the "
        "fact, so the pre <= resolved invariant is trivially satisfiable by back-dating -- "
        "no audit reading only the registry can detect that. A fan-out leg whose "
        "adjudicating run had ALREADY RESOLVED when it was added therefore clears only on "
        "**git-witnessed** provenance: its `pre_registration_source` artifact (or its own "
        "registry entry) must have been durably committed before the run resolved. The "
        "honest case self-clears with no human adjudication; a back-dated one cannot "
        "manufacture a commit._"
    )
    L.append("")
    if wit:
        L.append("**Witnessed (cleared on evidence):**")
        L.append("")
        for msg in wit:
            L.append(f"- {msg}")
        L.append("")
    if unv:
        L.append(
            "**Unverifiable (quiet -- not a violation, but not evidence either).** No git "
            "history was available to check these (uncommitted leg, wholesale file rewrite, "
            "or git unavailable). Commit the leg and name a `pre_registration_source` so it "
            "self-clears next cycle:"
        )
        L.append("")
        for msg in unv:
            L.append(f"- {msg}")
        L.append("")
    if not wit and not unv:
        L.append("_No fan-out leg required a provenance check this cycle._")
        L.append("")
    pend = flags.get("n_ledger_pending") or []
    L.append(f"## Advisory -- drafted ledger edits not reflected in the registry "
             f"({len(pend)}, NOT violations)")
    L.append("")
    if pend:
        L.append(
            "`/failure-autopsy` in staging mode drafts its intended Step 9b edits into a "
            "`hypothesis_space_ledger_pending` block on the autopsy artifact instead of "
            "writing this registry, for the confirming session or the next `/governance` "
            "walk to apply. Each CONFIRMED artifact below names a question, a hypothesis, "
            "or an intended resolved state that the registry does not currently carry."
        )
        L.append("")
        for msg in pend:
            L.append(f"- {msg}")
        L.append("")
        L.append(
            "A gap here is not automatically an owed edit -- a later, better-informed "
            "autopsy may have superseded the draft, which is a legitimate outcome. Apply "
            "it, or record the disposition on the block (`applied` / `registry_written` / "
            "`applied_utc` / `superseded_by`) so it stops being reported. Note the scan "
            "compares question, hypothesis and resolved-state presence only -- never "
            "`basis` prose or `resolving_runs` -- so a quiet result is a floor on the "
            "gap, not a proof there is none."
        )
        L.append("")
    else:
        L.append("_No confirmed autopsy carries an unreflected `hypothesis_space_ledger_pending` block._")
        L.append("")
    L.append("---")
    L.append("")
    L.append(
        "This audit promotes/demotes nothing. Response to any flag is a human decision "
        "at governance (the same handling as `check_closure_drift.py`). Advisory "
        "labelled-growth notes need no action -- but a question accumulating them is one "
        "whose campaign has not converged."
    )
    L.append("")
    return "\n".join(L) + "\n"


def _self_test() -> int:
    """Synthetic registry exercising each flag exactly once."""
    # Hoisted: Python requires a global declaration before the name's first use in
    # the function body, and `audit` is called partway through.
    global _artifact_first_commit, _registry_first_witness, REPORT, audit
    reg = {"questions": [
        {"qid": "ok_q", "initial_frozen_count": 2, "hypotheses": [
            {"hid": "h1", "pre_registered_utc": "2026-07-01",
             "resolution": {"state": "eliminated", "resolved_utc": "2026-07-05",
                            "evidence_direction": "weakens", "met_elimination_bar": True,
                            "control_passed": True, "non_degenerate": True}},
            {"hid": "h2", "pre_registered_utc": "2026-07-01",
             "resolution": {"state": "confirmed", "resolved_utc": "2026-07-06",
                            "evidence_direction": "supports", "control_passed": True,
                            "non_degenerate": True}},
        ]},
        # LABELLED fan-out growth: must land in the advisory bucket, NOT bucket (b).
        {"qid": "fanout_ok_q", "initial_frozen_count": 3,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-07-01T00:00:00Z",
         "fanout_growth_events": [
             {"recorded_utc": "2026-07-03T00:00:00Z",
              "fanout_source": "failure_autopsy_synthetic_2026-07-03.json",
              "added_hids": ["f_new"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": "f1", "pre_registered_utc": "2026-07-01",
              "resolution": {"state": "eliminated", "resolved_utc": "2026-07-02",
                             "evidence_direction": "weakens", "met_elimination_bar": True,
                             "control_passed": True, "non_degenerate": True}},
             {"hid": "f2", "pre_registered_utc": "2026-07-01",
              "resolution": {"state": "alive"}},
             {"hid": "f_new", "pre_registered_utc": "2026-07-03",
              "resolution": {"state": "alive"}},
         ]},
        # WITNESSED late append: the leg was added AFTER its run resolved, but its
        # pre_registration_source artifact was committed BEFORE -> self-clears.
        {"qid": "fanout_witnessed_q", "initial_frozen_count": 2,
         "initial_frozen_count_at_registration": 1,
         "registered_utc": "2026-07-01T00:00:00Z",
         "fanout_growth_events": [
             {"recorded_utc": "2026-07-09T00:00:00Z",
              "fanout_source": "failure_autopsy_witnessed_2026-07-03.json",
              "added_hids": ["w_new"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": "w1", "pre_registered_utc": "2026-07-01", "resolution": {"state": "alive"}},
             {"hid": "w_new", "pre_registered_utc": "2026-07-03",
              "pre_registration_source": "failure_autopsy_witnessed_2026-07-03.json",
              "resolution": {"state": "eliminated", "resolved_utc": "2026-07-05",
                             "evidence_direction": "weakens", "met_elimination_bar": True,
                             "control_passed": True, "non_degenerate": True}},
         ]},
        # BACK-DATED: claims pre_registered_utc 2026-07-03 but nothing durable exists
        # until 2026-07-09, after the run resolved -> real (b) flag. This is the case
        # the self-reported timestamp alone could never catch.
        {"qid": "fanout_backdated_q", "initial_frozen_count": 2,
         "initial_frozen_count_at_registration": 1,
         "registered_utc": "2026-07-01T00:00:00Z",
         "fanout_growth_events": [
             {"recorded_utc": "2026-07-09T00:00:00Z",
              "fanout_source": "failure_autopsy_backdated_2026-07-09.json",
              "added_hids": ["bd_new"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": "bd1", "pre_registered_utc": "2026-07-01", "resolution": {"state": "alive"}},
             {"hid": "bd_new", "pre_registered_utc": "2026-07-03",
              "resolution": {"state": "eliminated", "resolved_utc": "2026-07-05",
                             "evidence_direction": "weakens", "met_elimination_bar": True,
                             "control_passed": True, "non_degenerate": True}},
         ]},
        # UNVERIFIABLE: resolved leg with no git history at all -> quiet, NOT a flag.
        {"qid": "fanout_unverifiable_q", "initial_frozen_count": 2,
         "initial_frozen_count_at_registration": 1,
         "registered_utc": "2026-07-01T00:00:00Z",
         "fanout_growth_events": [
             {"recorded_utc": "2026-07-09T00:00:00Z",
              "fanout_source": "failure_autopsy_nohistory_2026-07-09.json",
              "added_hids": ["uv_new"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": "uv1", "pre_registered_utc": "2026-07-01", "resolution": {"state": "alive"}},
             {"hid": "uv_new", "pre_registered_utc": "2026-07-03",
              "resolution": {"state": "eliminated", "resolved_utc": "2026-07-05",
                             "evidence_direction": "weakens", "met_elimination_bar": True,
                             "control_passed": True, "non_degenerate": True}},
         ]},
        # RECURRENCE: three individually-VALID portfolios on one question. Every event
        # clears (a)-(c), so nothing may land in (b) -- but the count must fire the
        # h_fanout_recurrence overlay. Two of the three share a recorded_utc (a single
        # backfill pass) to pin that the counter keys on fanout_source, not timestamps.
        {"qid": "fanout_recurring_q", "initial_frozen_count": 5,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-07-01T00:00:00Z",
         "fanout_growth_events": [
             {"recorded_utc": "2026-07-04T00:00:00Z",
              "fanout_source": "failure_autopsy_rec_a_2026-07-04.json",
              "added_hids": ["r_a"], "delta": 1},
             {"recorded_utc": "2026-07-04T00:00:00Z",
              "fanout_source": "failure_autopsy_rec_b_2026-07-05.json",
              "added_hids": ["r_b"], "delta": 1},
             {"recorded_utc": "2026-07-06T00:00:00Z",
              "fanout_source": "failure_autopsy_rec_c_2026-07-06.json",
              "added_hids": ["r_c"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": "r1", "pre_registered_utc": "2026-07-01", "resolution": {"state": "alive"}},
             {"hid": "r2", "pre_registered_utc": "2026-07-01", "resolution": {"state": "alive"}},
             {"hid": "r_a", "pre_registered_utc": "2026-07-04", "resolution": {"state": "alive"}},
             {"hid": "r_b", "pre_registered_utc": "2026-07-05", "resolution": {"state": "alive"}},
             {"hid": "r_c", "pre_registered_utc": "2026-07-06", "resolution": {"state": "alive"}},
         ]},
        # ACKNOWLEDGED recurrence: 3 valid portfolios, the qid closed by a
        # `growth_restriction`, and every leg resolved -> the recurrence is WORKED.
        # Must move to m_recurrence_acknowledged and OUT of the ACTIONABLE bucket,
        # still never a (b) violation. This is the `competence_floor` shape as of
        # 2026-08-08 (`342a33e6a`), which the ACTIONABLE overlay re-routed on
        # 2026-08-12, four days after closure.
        {"qid": "fanout_closed_q", "initial_frozen_count": 5,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-08-10T00:00:00Z",
         "growth_restriction": "CLOSED TO FURTHER FAN-OUT (synthetic). Exception: a "
                               "mechanism targeting an axis family the decision block "
                               "still lists as undecided.",
         "fanout_growth_events": [
             {"recorded_utc": "2026-08-11T00:00:00Z",
              "fanout_source": "failure_autopsy_cl_a_2026-08-11.json",
              "added_hids": ["cl_a"], "delta": 1},
             {"recorded_utc": "2026-08-12T00:00:00Z",
              "fanout_source": "failure_autopsy_cl_b_2026-08-12.json",
              "added_hids": ["cl_b"], "delta": 1},
             {"recorded_utc": "2026-08-13T00:00:00Z",
              "fanout_source": "failure_autopsy_cl_c_2026-08-13.json",
              "added_hids": ["cl_c"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": hid, "pre_registered_utc": pre,
              "resolution": {"state": "eliminated", "resolved_utc": res,
                             "evidence_direction": "weakens", "met_elimination_bar": True,
                             "control_passed": True, "non_degenerate": True}}
             for hid, pre, res in [("cl1", "2026-08-10", "2026-08-14"),
                                   ("cl2", "2026-08-10", "2026-08-14"),
                                   ("cl_a", "2026-08-11", "2026-08-14"),
                                   ("cl_b", "2026-08-12", "2026-08-14"),
                                   ("cl_c", "2026-08-13", "2026-08-14")]
         ]},
        # NEGATIVE CONTROL 1 -- restriction present but a leg is STILL ALIVE. The
        # restriction half alone must NOT acknowledge: there is outstanding work a
        # re-pose could still redirect. Stays ACTIONABLE, with the mismatch named.
        # (`competence_floor` 2026-08-08T09:55Z `1c4a52062`: restriction written, one
        # leg still alive for ~8 hours before V3-EXQ-821b resolved it.)
        {"qid": "fanout_restricted_alive_q", "initial_frozen_count": 5,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-08-10T00:00:00Z",
         "growth_restriction": "CLOSED TO FURTHER FAN-OUT (synthetic, still working "
                               "its last leg).",
         "fanout_growth_events": [
             {"recorded_utc": "2026-08-11T00:00:00Z",
              "fanout_source": "failure_autopsy_ra_a_2026-08-11.json",
              "added_hids": ["ra_a"], "delta": 1},
             {"recorded_utc": "2026-08-12T00:00:00Z",
              "fanout_source": "failure_autopsy_ra_b_2026-08-12.json",
              "added_hids": ["ra_b"], "delta": 1},
             {"recorded_utc": "2026-08-13T00:00:00Z",
              "fanout_source": "failure_autopsy_ra_c_2026-08-13.json",
              "added_hids": ["ra_c"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": "ra1", "pre_registered_utc": "2026-08-10",
              "resolution": {"state": "alive"}},
             {"hid": "ra2", "pre_registered_utc": "2026-08-10",
              "resolution": {"state": "alive"}},
         ] + [
             {"hid": hid, "pre_registered_utc": pre, "resolution": {"state": "alive"}}
             for hid, pre in [("ra_a", "2026-08-11"), ("ra_b", "2026-08-12"),
                              ("ra_c", "2026-08-13")]
         ]},
        # NEGATIVE CONTROL 2 -- THE LOAD-BEARING ONE. 0 alive legs, NO restriction:
        # a campaign BETWEEN portfolios, which legitimately has no live legs. Must
        # stay ACTIONABLE. `competence_floor` was in exactly this state twice while
        # still live -- 2026-07-26T00:15Z (`ed0027587`, 3 portfolios), twelve hours
        # before portfolio 4 opened, and 2026-08-02T18:06Z (`ccc067123`, 5
        # portfolios), five days before a leg went back alive. A 0-alive-only
        # predicate would have de-routed the overlay at both of those moments.
        {"qid": "fanout_between_portfolios_q", "initial_frozen_count": 5,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-08-10T00:00:00Z",
         "fanout_growth_events": [
             {"recorded_utc": "2026-08-11T00:00:00Z",
              "fanout_source": "failure_autopsy_bp_a_2026-08-11.json",
              "added_hids": ["bp_a"], "delta": 1},
             {"recorded_utc": "2026-08-12T00:00:00Z",
              "fanout_source": "failure_autopsy_bp_b_2026-08-12.json",
              "added_hids": ["bp_b"], "delta": 1},
             {"recorded_utc": "2026-08-13T00:00:00Z",
              "fanout_source": "failure_autopsy_bp_c_2026-08-13.json",
              "added_hids": ["bp_c"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": hid, "pre_registered_utc": pre,
              "resolution": {"state": "eliminated", "resolved_utc": res,
                             "evidence_direction": "weakens", "met_elimination_bar": True,
                             "control_passed": True, "non_degenerate": True}}
             for hid, pre, res in [("bp1", "2026-08-10", "2026-08-14"),
                                   ("bp2", "2026-08-10", "2026-08-14"),
                                   ("bp_a", "2026-08-11", "2026-08-14"),
                                   ("bp_b", "2026-08-12", "2026-08-14"),
                                   ("bp_c", "2026-08-13", "2026-08-14")]
         ]},
        # LABELLED discovery growth: born resolved same-day, with a rationale --
        # must land in k_discovery_growth, NOT bucket (b).
        {"qid": "discovery_ok_q", "initial_frozen_count": 2,
         "initial_frozen_count_at_registration": 1,
         "registered_utc": "2026-08-01T00:00:00Z",
         "discovery_growth_events": [
             {"recorded_utc": "2026-08-02T00:00:00Z",
              "discovery_source": "failure_autopsy_disc_ok_2026-08-02.json",
              "added_hids": ["d_new"], "delta": 1,
              "rationale": "eliminates both pre-registered rivals; the remaining "
                           "pattern matches an independent, established mechanism."},
         ],
         "hypotheses": [
             {"hid": "d1", "pre_registered_utc": "2026-08-01", "resolution": {"state": "alive"}},
             {"hid": "d_new", "pre_registered_utc": "2026-08-02",
              "discovery_source": "failure_autopsy_disc_ok_2026-08-02.json",
              "resolution": {"state": "confirmed", "resolved_utc": "2026-08-02",
                             "evidence_direction": "supports", "control_passed": True,
                             "non_degenerate": True}},
         ]},
        # INVALID discovery growth: the "discovered" leg is left alive -- did not
        # qualify (needed Mode A instead) -> real (b) flag, not advisory.
        {"qid": "discovery_alive_q", "initial_frozen_count": 2,
         "initial_frozen_count_at_registration": 1,
         "registered_utc": "2026-08-01T00:00:00Z",
         "discovery_growth_events": [
             {"recorded_utc": "2026-08-02T00:00:00Z",
              "discovery_source": "failure_autopsy_disc_alive_2026-08-02.json",
              "added_hids": ["da_new"], "delta": 1,
              "rationale": "claims a discovery but the leg is still alive."},
         ],
         "hypotheses": [
             {"hid": "da1", "pre_registered_utc": "2026-08-01", "resolution": {"state": "alive"}},
             {"hid": "da_new", "pre_registered_utc": "2026-08-02", "resolution": {"state": "alive"}},
         ]},
        # INVALID discovery growth: no rationale -> real (b) flag.
        {"qid": "discovery_norationale_q", "initial_frozen_count": 2,
         "initial_frozen_count_at_registration": 1,
         "registered_utc": "2026-08-01T00:00:00Z",
         "discovery_growth_events": [
             {"recorded_utc": "2026-08-02T00:00:00Z",
              "discovery_source": "failure_autopsy_disc_norat_2026-08-02.json",
              "added_hids": ["dn_new"], "delta": 1},
         ],
         "hypotheses": [
             {"hid": "dn1", "pre_registered_utc": "2026-08-01", "resolution": {"state": "alive"}},
             {"hid": "dn_new", "pre_registered_utc": "2026-08-02",
              "resolution": {"state": "confirmed", "resolved_utc": "2026-08-02",
                             "evidence_direction": "supports", "control_passed": True,
                             "non_degenerate": True}},
         ]},
        # RECURRENCE: three individually-VALID discovery events on one question ->
        # l_discovery_recurrence overlay must fire, still NOT a (b) violation.
        {"qid": "discovery_recurring_q", "initial_frozen_count": 5,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-08-01T00:00:00Z",
         "discovery_growth_events": [
             {"recorded_utc": "2026-08-02T00:00:00Z",
              "discovery_source": "failure_autopsy_disc_rec_a_2026-08-02.json",
              "added_hids": ["dr_a"], "delta": 1, "rationale": "discovery A."},
             {"recorded_utc": "2026-08-03T00:00:00Z",
              "discovery_source": "failure_autopsy_disc_rec_b_2026-08-03.json",
              "added_hids": ["dr_b"], "delta": 1, "rationale": "discovery B."},
             {"recorded_utc": "2026-08-04T00:00:00Z",
              "discovery_source": "failure_autopsy_disc_rec_c_2026-08-04.json",
              "added_hids": ["dr_c"], "delta": 1, "rationale": "discovery C."},
         ],
         "hypotheses": [
             {"hid": "dr1", "pre_registered_utc": "2026-08-01", "resolution": {"state": "alive"}},
             {"hid": "dr2", "pre_registered_utc": "2026-08-01", "resolution": {"state": "alive"}},
             {"hid": "dr_a", "pre_registered_utc": "2026-08-02",
              "resolution": {"state": "confirmed", "resolved_utc": "2026-08-02",
                             "evidence_direction": "supports", "control_passed": True,
                             "non_degenerate": True}},
             {"hid": "dr_b", "pre_registered_utc": "2026-08-03",
              "resolution": {"state": "confirmed", "resolved_utc": "2026-08-03",
                             "evidence_direction": "supports", "control_passed": True,
                             "non_degenerate": True}},
             {"hid": "dr_c", "pre_registered_utc": "2026-08-04",
              "resolution": {"state": "confirmed", "resolved_utc": "2026-08-04",
                             "evidence_direction": "supports", "control_passed": True,
                             "non_degenerate": True}},
         ]},
        # ACKNOWLEDGED recurrence, DISCOVERY path. `growth_restriction` governs Mode C
        # too (/failure-autopsy Step 9b: "Mode C in every case"), so a closed qid must
        # not go on routing on the discovery overlay either. No production case exercises
        # this -- no question has ever exceeded ONE discovery source -- so this fixture is
        # the only thing holding the two overlays symmetric.
        {"qid": "discovery_closed_q", "initial_frozen_count": 5,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-08-10T00:00:00Z",
         "growth_restriction": "CLOSED TO FURTHER GROWTH (synthetic, discovery path).",
         "discovery_growth_events": [
             {"recorded_utc": "2026-08-11T00:00:00Z",
              "discovery_source": "failure_autopsy_dcl_a_2026-08-11.json",
              "added_hids": ["dcl_a"], "delta": 1, "rationale": "discovery A."},
             {"recorded_utc": "2026-08-12T00:00:00Z",
              "discovery_source": "failure_autopsy_dcl_b_2026-08-12.json",
              "added_hids": ["dcl_b"], "delta": 1, "rationale": "discovery B."},
             {"recorded_utc": "2026-08-13T00:00:00Z",
              "discovery_source": "failure_autopsy_dcl_c_2026-08-13.json",
              "added_hids": ["dcl_c"], "delta": 1, "rationale": "discovery C."},
         ],
         "hypotheses": [
             {"hid": hid, "pre_registered_utc": d,
              "resolution": {"state": "confirmed", "resolved_utc": d,
                             "evidence_direction": "supports", "control_passed": True,
                             "non_degenerate": True}}
             for hid, d in [("dcl1", "2026-08-10"), ("dcl2", "2026-08-10"),
                            ("dcl_a", "2026-08-11"), ("dcl_b", "2026-08-12"),
                            ("dcl_c", "2026-08-13")]
         ]},
        # UNLABELLED growth: no fanout_growth_events covering it -> real (b) flag.
        {"qid": "fanout_bad_q", "initial_frozen_count": 3,
         "initial_frozen_count_at_registration": 2,
         "registered_utc": "2026-07-01T00:00:00Z",
         "fanout_growth_events": [],
         "hypotheses": [
             {"hid": "u1", "pre_registered_utc": "2026-07-01", "resolution": {"state": "alive"}},
             {"hid": "u2", "pre_registered_utc": "2026-07-01", "resolution": {"state": "alive"}},
             {"hid": "u3", "pre_registered_utc": "2026-07-09", "resolution": {"state": "alive"}},
         ]},
        {"qid": "bad_q", "initial_frozen_count": 3, "hypotheses": [  # (b) count mismatch: 3 vs 2
            {"hid": "b_retro", "pre_registered_utc": "2026-07-10",   # (b) retro-pad
             "resolution": {"state": "eliminated", "resolved_utc": "2026-07-05",
                            "evidence_direction": "supports",         # (a) unbacked
                            "met_elimination_bar": False,             # (d) bar violation
                            "control_passed": False, "non_degenerate": True}},
            {"hid": "c_nocontrol",
             "resolution": {"state": "confirmed", "control_passed": None}},  # (c)
        ]},
    ]}
    ts = [
        # total_confirmed AND total_superseded present + FLAT across every row:
        # proves the 07-01->07-02 drop is genuinely unbacked (neither a
        # confirmation nor a supersession explains it), not merely unverifiable
        # for lack of either field.
        {"date": "2026-07-01", "total_surviving": 5, "total_resolved_out": 0,
         "total_initial": 5, "total_confirmed": 0, "total_superseded": 0},
        {"date": "2026-07-02", "total_surviving": 3, "total_resolved_out": 0,
         "total_initial": 5, "total_confirmed": 0, "total_superseded": 0},  # (a) unbacked drop
        {"date": "2026-07-03", "total_surviving": 3, "total_resolved_out": 0,
         "total_initial": 7, "total_confirmed": 0, "total_superseded": 0},  # (b) init grew
    ]
    # Hermetic: stub the two git lookups so the self-test never shells out (and so
    # it exercises the witness LOGIC rather than this repo's actual history).
    _real_art, _real_reg = _artifact_first_commit, _registry_first_witness
    _artifact_first_commit = lambda p: {
        "failure_autopsy_witnessed_2026-07-03.json": "2026-07-03",   # before resolution
        "failure_autopsy_backdated_2026-07-09.json": "2026-07-09",   # after resolution
    }.get(p, "")                                                      # nohistory -> ''
    _registry_first_witness = lambda hid: {
        "bd_new": "2026-07-09",   # nothing durable until after the run resolved
    }.get(hid, "")                # uv_new -> '' -> unverifiable
    try:
        flags = audit(reg, ts)
    finally:
        _artifact_first_commit, _registry_first_witness = _real_art, _real_reg
    checks = {
        "a_unbacked_drop": flags["a_unbacked_drop"],
        "b_enlargement": flags["b_enlargement"],
        "c_confirmed_no_control": flags["c_confirmed_no_control"],
        "d_bar_violation": flags["d_bar_violation"],
        "e_labelled_growth": flags["e_labelled_growth"],
        "f_unverifiable": flags["f_unverifiable"],
        "g_witnessed": flags["g_witnessed"],
        "h_fanout_recurrence": flags["h_fanout_recurrence"],
        "k_discovery_growth": flags["k_discovery_growth"],
        "l_discovery_recurrence": flags["l_discovery_recurrence"],
        "m_recurrence_acknowledged": flags["m_recurrence_acknowledged"],
    }
    failures = [k for k, v in checks.items() if not v]
    for k, v in checks.items():
        print(f"  {'ok  ' if v else 'FAIL'} {k}: {len(v)} item(s)")
    # Discrimination checks: labelled growth must NOT land in (b); unlabelled MUST.
    joined_b = " ".join(flags["b_enlargement"])
    joined_e = " ".join(flags["e_labelled_growth"])
    if "fanout_ok_q" in joined_b:
        print("  FAIL discrimination: labelled fan-out growth was flagged as a (b) violation")
        failures.append("labelled_growth_misflagged")
    else:
        print("  ok   discrimination: labelled fan-out growth not flagged as (b)")
    if "fanout_bad_q" not in joined_b:
        print("  FAIL discrimination: UNLABELLED growth was not flagged as a (b) violation")
        failures.append("unlabelled_growth_missed")
    else:
        print("  ok   discrimination: unlabelled growth flagged as (b)")
    if "fanout_ok_q" not in joined_e:
        print("  FAIL discrimination: labelled fan-out growth missing from the advisory bucket")
        failures.append("labelled_growth_not_advised")
    else:
        print("  ok   discrimination: labelled fan-out growth reported as advisory")

    # Provenance discriminations -- the point of the git witness.
    joined_f = " ".join(flags["f_unverifiable"])
    joined_g = " ".join(flags["g_witnessed"])
    # Recurrence discriminations (GOV-FROZEN-1 escalation clause).
    joined_h = " ".join(flags["h_fanout_recurrence"])
    for name, cond, msg in [
        ("recurrence_fires", "fanout_recurring_q" in joined_h,
         f"N>={FANOUT_RECURRENCE_N} valid portfolios fired the recurrence overlay"),
        ("recurrence_not_a_violation", "fanout_recurring_q" not in joined_b,
         "recurring question NOT flagged as (b) -- every portfolio was legitimate"),
        ("recurrence_keys_on_source", "3 distinct labelled fan-out portfolios" in joined_h,
         "counter keyed on fanout_source, not recorded_utc (2 events shared a timestamp)"),
        ("recurrence_below_n_quiet", "fanout_ok_q" not in joined_h,
         f"a question below N={FANOUT_RECURRENCE_N} stays quiet (no mass-surfacing)"),
        ("backdated_caught", "fanout_backdated_q" in joined_b,
         "back-dated late append flagged as (b)"),
        ("witnessed_cleared", "fanout_witnessed_q" not in joined_b and "w_new" in joined_g,
         "witnessed late append self-cleared (not flagged, listed as witnessed)"),
        ("unverifiable_quiet", "fanout_unverifiable_q" not in joined_b and "uv_new" in joined_f,
         "no-git-history leg reported unverifiable, NOT flagged"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)

    # Recurrence ACKNOWLEDGEMENT discriminations. The predicate has two halves and the
    # two negative controls below are the reason it does -- each is a real historical
    # `competence_floor` state in which the campaign was demonstrably still live.
    joined_m = " ".join(flags["m_recurrence_acknowledged"])
    ack_msg = next((m for m in flags["m_recurrence_acknowledged"]
                    if "fanout_closed_q" in m), "")
    live_msg = next((m for m in flags["h_fanout_recurrence"]
                     if "fanout_restricted_alive_q" in m), "")
    for name, cond, msg in [
        ("ack_fires", "fanout_closed_q" in joined_m,
         "a closed qid (growth_restriction + 0 alive) is ACKNOWLEDGED"),
        ("ack_leaves_actionable", "fanout_closed_q" not in joined_h,
         "an acknowledged recurrence no longer routes work from the ACTIONABLE bucket"),
        ("ack_not_a_violation", "fanout_closed_q" not in joined_b,
         "acknowledgement does not turn a legitimate recurrence into a (b) violation"),
        ("ack_quotes_restriction_verbatim",
         "Exception: a mechanism targeting an axis family" in ack_msg,
         "the acknowledged line quotes the restriction VERBATIM -- exception "
         "conditions are not paraphrased away"),
        ("ack_still_names_the_count",
         "3 distinct labelled fan-out portfolios" in ack_msg,
         "acknowledgement is not suppression: the portfolio count is still reported"),
        # NEGATIVE CONTROL 1: the restriction half alone is not sufficient.
        ("ack_needs_zero_alive",
         "fanout_restricted_alive_q" in joined_h
         and "fanout_restricted_alive_q" not in joined_m,
         "a RESTRICTED qid with a live leg stays ACTIONABLE -- restriction alone "
         "does not acknowledge"),
        ("ack_names_the_mismatch", "NOT acknowledged" in live_msg,
         "the restricted-but-alive case says so in the line, rather than leaving "
         "the reader to re-derive why it is still actionable"),
        # NEGATIVE CONTROL 2: the load-bearing one. 0 alive without a restriction is
        # a campaign BETWEEN portfolios -- `competence_floor` sat here twice (2026-07-26
        # `ed0027587`, 2026-08-02 `ccc067123`) and re-grew both times.
        ("ack_needs_restriction",
         "fanout_between_portfolios_q" in joined_h
         and "fanout_between_portfolios_q" not in joined_m,
         "0 alive legs WITHOUT a growth_restriction stays ACTIONABLE -- a campaign "
         "between portfolios has no live legs and is not closed"),
        ("ack_discovery_path",
         "discovery_closed_q" in joined_m
         and "discovery_closed_q" not in " ".join(flags["l_discovery_recurrence"])
         and "discovery_closed_q" not in joined_b,
         "the discovery overlay acknowledges on the same predicate -- "
         "growth_restriction governs Mode C too"),
        ("ack_below_n_quiet", "fanout_ok_q" not in joined_m,
         f"a question below N={FANOUT_RECURRENCE_N} is never acknowledged (nothing "
         "fired to acknowledge)"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)

    # Acknowledgement must never be SILENT. The whole risk of this bucket is that it
    # becomes an alarm that erases itself, so pin the three places the count has to
    # remain visible in the rendered report a governance session actually reads.
    rendered = render_report(flags, reg, ts, "2026-08-14T00:00:00Z")
    n_ack = len(flags["m_recurrence_acknowledged"])
    for name, cond, msg in [
        ("render_ack_section", f"## Recurrence acknowledged ({n_ack}, advisory)" in rendered,
         "the rendered report carries its own acknowledged section"),
        ("render_ack_lists_qid", "fanout_closed_q" in rendered.split(
            "## Recurrence acknowledged")[-1],
         "the acknowledged question is listed in that section, not merely counted"),
        ("render_actionable_header_warns",
         f"{n_ack} recurrence(s) are ACKNOWLEDGED" in rendered,
         "the ACTIONABLE section states the acknowledged count, so a count of 0 "
         "there can never read as 'no recurrence'"),
        ("render_summary_counts_ack",
         f"**{n_ack}** acknowledged (worked) recurrence(s)" in rendered,
         "the report's summary line counts acknowledged recurrences"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)

    # Discovery-growth discriminations (the serendipity path, distinct from fan-out).
    joined_k = " ".join(flags["k_discovery_growth"])
    joined_l = " ".join(flags["l_discovery_recurrence"])
    for name, cond, msg in [
        ("discovery_ok_advised", "discovery_ok_q" in joined_k and "discovery_ok_q" not in joined_b,
         "valid discovery growth (born resolved same-day, with a rationale) reported "
         "as advisory, not flagged as (b)"),
        ("discovery_alive_caught", "discovery_alive_q" in joined_b,
         "a leg left alive after a claimed 'discovery' is flagged as (b) -- it needed "
         "Mode A pre-registration instead"),
        ("discovery_norationale_caught", "discovery_norationale_q" in joined_b,
         "a discovery event with no rationale is flagged as (b)"),
        ("discovery_recurrence_fires", "discovery_recurring_q" in joined_l,
         f"N>={FANOUT_RECURRENCE_N} valid discovery events fired the recurrence overlay"),
        ("discovery_recurrence_not_a_violation", "discovery_recurring_q" not in joined_b,
         "recurring discovery question NOT flagged as (b) -- every event was legitimate"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)
    # Same-day attribution (regression, confirmed false positive 2026-07-19a). An
    # event recorded LATER ON THE SAME DAY as the previous snapshot must attribute
    # to the window it landed in. Under date granularity `lo < date` excluded it and
    # its legs fell through into bucket (b) with a "0 leg(s) attributable" message,
    # which is the alarm-fatigue vector GOV-FROZEN-1 warns about turned on itself.
    # The paired window pins the other side: adding an event must NOT make genuinely
    # unlabelled growth attributable.
    def _same_day_case(delta: int, d_init: int,
                       rec: str = "2026-07-18T18:37:29Z") -> list:
        reg2 = {"questions": [{
            "qid": "sameday_q", "initial_frozen_count": 1 + delta,
            "initial_frozen_count_at_registration": 1,
            "registered_utc": "2026-07-01T00:00:00Z",
            "fanout_growth_events": [
                {"recorded_utc": rec,                      # default: 22 min AFTER
                 "fanout_source": "sameday_portfolio_2026-07-18.md",
                 "added_hids": [f"sd_{i}" for i in range(delta)], "delta": delta},
            ],
            "hypotheses": [{"hid": "sd1", "pre_registered_utc": "2026-07-01",
                            "resolution": {"state": "alive"}}]
                          + [{"hid": f"sd_{i}", "pre_registered_utc": "2026-07-18",
                              "resolution": {"state": "alive"}} for i in range(delta)],
        }]}
        ts2 = [
            {"date": "2026-07-18", "snapshot_utc": "2026-07-18T18:15:48Z",
             "total_surviving": 1, "total_resolved_out": 0, "total_initial": 1},
            {"date": "2026-07-19", "snapshot_utc": "2026-07-19T11:37:06Z",
             "total_surviving": 1 + d_init, "total_resolved_out": 0,
             "total_initial": 1 + d_init},
        ]
        return [m for m in audit(reg2, ts2)["b_enlargement"] if "time series" in m]

    for name, cond, msg in [
        ("sameday_attributes", not _same_day_case(4, 4),
         "growth recorded after the same-day prior snapshot attributes to its window"),
        ("sameday_no_overcorrection", _same_day_case(4, 6),
         "growth beyond what the labelled events cover is STILL flagged as (b)"),
        # Pins the BOUNDS half: an event recorded BEFORE the prior snapshot was
        # already counted in that snapshot's total_initial, so it cannot explain a
        # later rise. Day-granularity bounds cannot tell the two apart -- which is
        # why the window compares `snapshot_utc`, not `date`.
        ("sameday_before_snapshot_not_attributed",
         _same_day_case(4, 4, rec="2026-07-18T04:49:14Z"),
         "growth recorded BEFORE the same-day prior snapshot does not attribute"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)

    # Confirmed-backed / confirmed-unverifiable surviving-drop discriminations
    # (2026-08-02 fix, generalised 2026-08-19 to also credit `total_superseded`).
    # A minimal one-question registry+timeseries pair is enough here -- the drop
    # is purely a total_surviving/total_resolved_out/total_confirmed/
    # total_superseded arithmetic comparison, unlike the fan-out checks above
    # which need real hypotheses/events to drive. Each `*_prev`/`*_cur` param
    # controls whether that snapshot row carries the field (and what it's set
    # to); `None` means the key is omitted entirely, simulating a pre-fix ledger
    # row. `superseded_prev`/`superseded_cur` default to 0 on both rows so the
    # pre-existing confirmed-only call sites below are unaffected -- they
    # simulate a POST-fix ledger where total_superseded exists and is simply
    # uninvolved, not a pre-fix ledger missing the field (that path is exercised
    # explicitly by the superseded-missing cases further down).
    def _credited_drop_case(confirmed_prev, confirmed_cur,
                            superseded_prev=0, superseded_cur=0) -> list:
        reg3 = {"questions": [{"qid": "confdrop_q", "initial_frozen_count": 2,
                               "hypotheses": [
                                   {"hid": "cd1", "pre_registered_utc": "2026-07-01",
                                    "resolution": {"state": "alive"}},
                               ]}]}
        row1 = {"date": "2026-07-29", "total_surviving": 5, "total_resolved_out": 2,
                "total_initial": 7}
        row2 = {"date": "2026-07-30", "total_surviving": 4, "total_resolved_out": 2,
                "total_initial": 7}
        if confirmed_prev is not None:
            row1["total_confirmed"] = confirmed_prev
        if confirmed_cur is not None:
            row2["total_confirmed"] = confirmed_cur
        if superseded_prev is not None:
            row1["total_superseded"] = superseded_prev
        if superseded_cur is not None:
            row2["total_superseded"] = superseded_cur
        return audit(reg3, [row1, row2])

    flags_backed = _credited_drop_case(3, 4)          # total_confirmed rose by 1 == the drop
    flags_missing_cur = _credited_drop_case(3, None)   # field absent on the LATER row
    flags_missing_prev = _credited_drop_case(None, 4)  # field absent on the EARLIER row
    flags_flat = _credited_drop_case(3, 3)             # field present but flat -> genuinely unbacked

    for name, cond, msg in [
        ("confirmed_backed_not_unbacked",
         not flags_backed["a_unbacked_drop"] and len(flags_backed["i_confirmed_backed"]) == 1,
         "a drop matched by a total_confirmed rise lands in i_confirmed_backed, not a_unbacked_drop"),
        ("confirmed_missing_cur_is_unverifiable",
         not flags_missing_cur["a_unbacked_drop"] and len(flags_missing_cur["j_confirmed_unverifiable"]) == 1,
         "total_confirmed absent from the LATER snapshot reads as unverifiable, not a violation"),
        ("confirmed_missing_prev_is_unverifiable",
         not flags_missing_prev["a_unbacked_drop"] and len(flags_missing_prev["j_confirmed_unverifiable"]) == 1,
         "total_confirmed absent from the EARLIER snapshot reads as unverifiable, not a violation"),
        ("confirmed_flat_stays_unbacked",
         len(flags_flat["a_unbacked_drop"]) == 1 and not flags_flat["i_confirmed_backed"]
         and not flags_flat["j_confirmed_unverifiable"],
         "total_confirmed present on both sides but FLAT -- drop stays a real (a) violation"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)

    # Superseded-backed / superseded-unverifiable surviving-drop discriminations
    # (2026-08-19, `superseded` state added to the registry vocabulary). Exact
    # mirror of the confirmed-credit block above, but driving total_superseded
    # instead -- proves a `superseded` resolution credits an otherwise-unbacked
    # drop the same way a `confirmed` one does, and that a MIXED delta (one
    # field flat, the other moving) still credits on the sum.
    flags_sup_backed = _credited_drop_case(0, 0, 3, 4)          # total_superseded rose by 1
    flags_sup_missing_cur = _credited_drop_case(0, 0, 3, None)   # field absent on the LATER row
    flags_sup_missing_prev = _credited_drop_case(0, 0, None, 4)  # field absent on the EARLIER row
    flags_sup_flat = _credited_drop_case(0, 0, 3, 3)             # field present but flat
    flags_mixed_backed = _credited_drop_case(3, 3, 0, 1)         # confirmed flat, superseded rose

    for name, cond, msg in [
        ("superseded_backed_not_unbacked",
         not flags_sup_backed["a_unbacked_drop"] and len(flags_sup_backed["i_confirmed_backed"]) == 1,
         "a drop matched by a total_superseded rise lands in i_confirmed_backed, not a_unbacked_drop"),
        ("superseded_missing_cur_is_unverifiable",
         not flags_sup_missing_cur["a_unbacked_drop"]
         and len(flags_sup_missing_cur["j_confirmed_unverifiable"]) == 1,
         "total_superseded absent from the LATER snapshot reads as unverifiable, not a violation"),
        ("superseded_missing_prev_is_unverifiable",
         not flags_sup_missing_prev["a_unbacked_drop"]
         and len(flags_sup_missing_prev["j_confirmed_unverifiable"]) == 1,
         "total_superseded absent from the EARLIER snapshot reads as unverifiable, not a violation"),
        ("superseded_flat_stays_unbacked",
         len(flags_sup_flat["a_unbacked_drop"]) == 1 and not flags_sup_flat["i_confirmed_backed"]
         and not flags_sup_flat["j_confirmed_unverifiable"],
         "total_superseded present on both sides but FLAT -- drop stays a real (a) violation"),
        ("mixed_credit_sums_both_fields",
         not flags_mixed_backed["a_unbacked_drop"] and len(flags_mixed_backed["i_confirmed_backed"]) == 1,
         "confirmed flat + superseded rose by 1 still credits the drop -- the two fields sum"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)

    # (c)/(d) state-set discriminations for `superseded` (2026-08-19). A single
    # synthetic question carries both: a superseded leg MISSING a passed control
    # (must land in c_confirmed_no_control, same bucket confirmed uses) and a
    # superseded leg WITH a passed control but met_elimination_bar explicitly
    # False (must clear check (c) AND, the negative control this task exists to
    # pin, must NOT land in d_bar_violation -- superseded is deliberately exempt
    # from the elimination bar).
    reg_sup = {"questions": [{"qid": "superseded_checks_q", "initial_frozen_count": 2,
                              "hypotheses": [
                                  {"hid": "sup_nocontrol", "pre_registered_utc": "2026-08-01",
                                   "resolution": {"state": "superseded",
                                                  "resolved_utc": "2026-08-02",
                                                  "control_passed": None}},
                                  {"hid": "sup_ok", "pre_registered_utc": "2026-08-01",
                                   "resolution": {"state": "superseded",
                                                  "resolved_utc": "2026-08-02",
                                                  "control_passed": True,
                                                  "non_degenerate": True,
                                                  "met_elimination_bar": False}},
                              ]}]}
    flags_sup_checks = audit(reg_sup, [])
    joined_sup_c = " ".join(flags_sup_checks["c_confirmed_no_control"])
    joined_sup_d = " ".join(flags_sup_checks["d_bar_violation"])
    for name, cond, msg in [
        ("superseded_no_control_caught", "sup_nocontrol" in joined_sup_c,
         "a `superseded` leg without control_passed is flagged as (c), same as confirmed"),
        ("superseded_with_control_clears_c", "sup_ok" not in joined_sup_c,
         "a `superseded` leg WITH a passed control clears check (c)"),
        ("superseded_exempt_from_bar", "sup_ok" not in joined_sup_d,
         "a `superseded` leg is EXEMPT from the elimination bar (d) even with "
         "met_elimination_bar explicitly False -- negative control for the "
         "anti-over-counting design (GOV-FROZEN-1)"),
        ("superseded_nocontrol_also_exempt_from_bar", "sup_nocontrol" not in joined_sup_d,
         "a `superseded` leg missing a control still never enters check (d) -- "
         "(c) and (d) are independent gates on disjoint state sets"),
    ]:
        if cond:
            print(f"  ok   discrimination: {msg}")
        else:
            print(f"  FAIL discrimination: {msg}")
            failures.append(name)

    # Fail-open check: a crashed audit must INVALIDATE the report, not leave a stale
    # clean one behind. Governance reads the file, so "silently kept the old report"
    # is indistinguishable from "audited and found nothing" -- the failure mode this
    # whole script exists to catch. Verified by actually breaking audit().
    import tempfile
    _real_report, _real_audit = REPORT, audit
    try:
        with tempfile.TemporaryDirectory() as td:
            REPORT = Path(td) / "report.md"
            REPORT.write_text("# stale\n\nAudited 6 questions. **0** flag(s) raised.\n",
                              encoding="utf-8")

            def _boom(*a, **k):
                raise RuntimeError("synthetic audit failure")

            audit = _boom
            # Exactly the __main__ shape: main() propagates, the handler invalidates.
            try:
                main()
            except Exception as exc:
                _write_incomplete_report(exc)
            body = REPORT.read_text(encoding="utf-8")
            stale_survived = "0** flag(s) raised" in body and "DID NOT" not in body
    finally:
        REPORT, audit = _real_report, _real_audit
    if stale_survived:
        print("  FAIL fail-open: a crashed audit left the stale '0 flags' report in place")
        failures.append("stale_report_survives_crash")
    else:
        print("  ok   fail-open: a crashed audit does not leave a stale clean report")

    if failures:
        print(f"SELF-TEST FAILED: {failures}")
        return 1
    print("SELF-TEST PASSED")
    return 0


def _rel(p: Path) -> str:
    """Repo-relative display path, falling back to the absolute one.

    `Path.relative_to` RAISES when the path is outside REPO_ROOT. That never
    happens in production, but it did crash the unparseable-registry branch under
    test -- and a crash inside an error path is the worst place for one, since it
    is what runs when things are already wrong.
    """
    try:
        return str(p.relative_to(REPO_ROOT))
    except ValueError:
        return str(p)


def _write_incomplete_report(exc: Exception) -> None:
    """Overwrite the report so a CRASHED audit cannot be read as a CLEAN one.

    Exercised by --self-test; called from the __main__ handler. Never raises --
    the contract is that this script gates nothing, so even a failed
    invalidation must not turn into a non-zero exit.
    """
    try:
        REPORT.write_text(
            "# Hypothesis-Space Integrity Audit (anti-Goodhart)\n\n"
            f"Generated: {_utc_now_iso_z()}\n\n"
            "## AUDIT DID NOT COMPLETE\n\n"
            f"The audit raised `{exc.__class__.__name__}: {exc}` and exited without "
            "producing findings, so **no integrity check was performed this run**.\n\n"
            "**This is not an all-clear, and any flag count quoted from an earlier "
            "report is stale.** The previous report was overwritten deliberately: it "
            "said what the last *successful* run found, and leaving it in place would "
            "let a crashed audit read as a clean one.\n\n"
            "Re-run `scripts/check_hypothesis_space_integrity.py` once the cause is "
            "fixed; `--self-test` checks the audit logic itself.\n\n"
            "_Advisory and non-blocking as always -- this exits 0 and gates nothing._\n",
            encoding="utf-8")
    except Exception:
        # Even the invalidation failed (read-only FS, etc.). Still never gate.
        pass


def main() -> int:
    now = _utc_now_iso_z()
    registry = _load_json(REGISTRY)
    if not isinstance(registry, dict):
        # An UNPARSEABLE registry is not the same as an absent one. _load_json
        # swallows both, but the first is the case you most want an alarm for --
        # a corrupted or half-written ledger. Reporting it as "nothing to audit"
        # would make ledger corruption read as all-clear.
        if REGISTRY.exists():
            print("hypothesis-space integrity: REGISTRY UNPARSEABLE -- see report.",
                  file=sys.stderr)
            REPORT.write_text(
                "# Hypothesis-Space Integrity Audit (anti-Goodhart)\n\n"
                f"Generated: {now}\n\n"
                "## AUDIT DID NOT RUN -- REGISTRY UNPARSEABLE\n\n"
                f"`{_rel(REGISTRY)}` exists but could not be parsed as "
                "JSON, so **no integrity check was performed**. This is NOT an all-clear: "
                "a malformed ledger is exactly the state the frozen-set invariants exist "
                "to catch, and it is also what a half-written or conflict-mangled edit "
                "looks like.\n\n"
                "Fix the JSON, then re-run `scripts/check_hypothesis_space_integrity.py`. "
                "Treat any flag count quoted from an earlier report as stale.\n\n"
                "_Advisory and non-blocking as always -- this exits 0 and gates nothing._\n",
                encoding="utf-8")
            return 0
        print("hypothesis-space integrity: registry missing; nothing to audit.")
        REPORT.write_text(
            f"# Hypothesis-Space Integrity Audit\n\nGenerated: {now}\n\n"
            "_No registry found; nothing to audit._\n", encoding="utf-8")
        return 0
    timeseries = _load_timeseries(TIMESERIES)
    flags = audit(registry, timeseries)
    flags["n_ledger_pending"] = scan_ledger_pending(registry)
    REPORT.write_text(render_report(flags, registry, timeseries, now), encoding="utf-8")
    total = sum(len(v) for k, v in flags.items() if k not in ADVISORY_BUCKETS)
    print(f"Hypothesis-space integrity report written: {_rel(REPORT)}")
    print(f"  flags: a={len(flags['a_unbacked_drop'])} b={len(flags['b_enlargement'])} "
          f"c={len(flags['c_confirmed_no_control'])} d={len(flags['d_bar_violation'])} "
          f"(total={total}, advisory/non-blocking)")
    print(f"  labelled fan-out growth (advisory, not a flag): "
          f"{len(flags['e_labelled_growth'])} note(s)")
    print(f"  pre-registration provenance: {len(flags['g_witnessed'])} git-witnessed, "
          f"{len(flags['f_unverifiable'])} unverifiable")
    print(f"  surviving-drop confirmation check (advisory, not a flag): "
          f"{len(flags['i_confirmed_backed'])} backed, "
          f"{len(flags['j_confirmed_unverifiable'])} unverifiable")
    n_rec = len(flags["h_fanout_recurrence"])
    print(f"  fan-out recurrence (N>={FANOUT_RECURRENCE_N} portfolios, ACTIONABLE): "
          f"{n_rec}")
    if n_rec:
        print("  -- RECURRENCE: the question may be MIS-POSED rather than")
        print("     under-enumerated. Re-pose the operationalization before")
        print("     opening another portfolio (routing only; promotes/demotes nothing):")
        for msg in flags["h_fanout_recurrence"]:
            qid = msg.split("`")[1] if "`" in msg else msg[:40]
            print(f"    [recurrence] {qid}")
    print(f"  labelled discovery growth (advisory, not a flag): "
          f"{len(flags['k_discovery_growth'])} note(s)")
    n_pend = len(flags.get("n_ledger_pending") or [])
    print(f"  drafted ledger edits not reflected (advisory, not a flag): {n_pend}")
    if n_pend:
        print("  -- staged Step 9b blocks whose question/hypothesis/state is not in")
        print("     the registry. Apply, or record the disposition on the block:")
        for msg in flags["n_ledger_pending"]:
            print(f"    [ledger-pending] {msg.split('`')[1] if '`' in msg else msg[:60]}")
    n_disc_rec = len(flags["l_discovery_recurrence"])
    print(f"  discovery-growth recurrence (N>={FANOUT_RECURRENCE_N} events, ACTIONABLE): "
          f"{n_disc_rec}")
    if n_disc_rec:
        print("  -- RECURRENCE: 'discovery' may be substituting for pre-registration")
        print("     discipline. Check whether the next candidate was really")
        print("     unforeseeable (routing only; promotes/demotes nothing):")
        for msg in flags["l_discovery_recurrence"]:
            qid = msg.split("`")[1] if "`" in msg else msg[:40]
            print(f"    [discovery-recurrence] {qid}")
    n_ack = len(flags["m_recurrence_acknowledged"])
    print(f"  recurrence ACKNOWLEDGED (closed qid + 0 alive legs, advisory): {n_ack}")
    if n_ack:
        # Printed even though it routes nothing: a reader who sees "ACTIONABLE: 0"
        # and stops there must still learn the ledger is not quiet.
        print("  -- WORKED, not live: re-posed and closed to further growth. No")
        print("     routing this cycle; re-read the restriction before sanctioning")
        print("     any new growth on these questions:")
        for msg in flags["m_recurrence_acknowledged"]:
            qid = msg.split("`")[1] if "`" in msg else msg[:40]
            print(f"    [acknowledged] {qid}")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover - advisory, never blocks
        # SELF-INVALIDATE THE REPORT. The contract is "never gates" (exit 0), but a
        # crash used to leave the PREVIOUS report on disk -- typically one saying
        # "0 flag(s) raised" -- while only stderr carried the failure. Governance
        # Step 5c reads the FILE, not the exit code or stderr, and stderr scrolls
        # past inside governance.sh. So a crashed audit read as a clean audit: a
        # silent no-op presenting as success, which is the exact failure mode this
        # script exists to catch elsewhere. Overwrite the report so a stale clean
        # one can never be mistaken for a current one.
        print(f"hypothesis-space integrity: non-fatal error ({exc.__class__.__name__}); exiting 0.",
              file=sys.stderr)
        _write_incomplete_report(exc)
        sys.exit(0)
