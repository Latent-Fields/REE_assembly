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
      after registration WITHOUT a labelled fan-out record, or a hypothesis's
      pre_registered_utc is AFTER the run that adjudicated it (retro-padding).
      LABELLED fan-out growth (a GOV-FANOUT-1 discrimination portfolio enumerating
      new rivals as earlier axes are eliminated) is NOT a violation -- it is
      reported separately as advisory. See `labelled_fanout_growth` in the
      registry's invariants block for the (a)-(c) conditions it must satisfy.
  (c) Confirmed without a passed control -- a `confirmed` hypothesis whose
      resolution lacks control_passed == true.
  (d) Elimination-bar violation -- an `eliminated`/`split` hypothesis missing the
      full bar (met_elimination_bar + control_passed + non_degenerate == true).

Output: evidence/planning/hypothesis_space_integrity.md.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_hypothesis_space_integrity.py
    /opt/local/bin/python3 scripts/check_hypothesis_space_integrity.py --self-test
"""

from __future__ import annotations

import json
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
# Buckets that are REPORTED but never counted as flags: sanctioned labelled growth,
# the quiet unverifiable-provenance state, and cleared git witnesses.
ADVISORY_BUCKETS = {"e_labelled_growth", "f_unverifiable", "g_witnessed"}
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


def _validate_fanout_growth(q: dict, flags: dict) -> int:
    """Validate a question's LABELLED fan-out growth against the registry's
    `labelled_fanout_growth` invariant, conditions (a)-(c).

    Growth satisfying all three is ADVISORY (bucket `e_labelled_growth`), not a
    violation. Unaccounted / unlabelled / retro-padded growth stays a REAL
    bucket-(b) flag. Returns the number of legitimately-labelled added legs, so
    the time-series check can attribute a `total_initial` rise to it.
    """
    qid = q.get("qid")
    initial = int(q.get("initial_frozen_count") or 0)
    # (c) the registration-time denominator must be preserved separately.
    at_reg = q.get("initial_frozen_count_at_registration")
    events = q.get("fanout_growth_events") or []
    growth = initial - int(at_reg) if at_reg is not None else 0

    if at_reg is None:
        if events:
            flags["b_enlargement"].append(
                f"`{qid}`: fanout_growth_events recorded but "
                "initial_frozen_count_at_registration is missing -- condition (c) "
                "unmet, the original denominator is not preserved."
            )
        # No growth claimed and no registration denominator: nothing to check here.
        # (b1) below still guards initial_frozen_count == len(hypotheses).
        return 0

    if growth < 0:
        flags["b_enlargement"].append(
            f"`{qid}`: initial_frozen_count={initial} is BELOW "
            f"initial_frozen_count_at_registration={at_reg} -- the frozen set shrank."
        )
        return 0

    by_hid = {h.get("hid"): h for h in (q.get("hypotheses") or [])}
    accounted = 0
    ok_events = 0
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
        ok_events += 1
        flags["e_labelled_growth"].append(
            f"`{qid}`: +{delta} leg(s) ({', '.join(hids)}) added by labelled fan-out "
            f"from `{src}` -- conditions (a)-(c) satisfied, advisory not a violation."
        )

    if accounted < growth:
        flags["b_enlargement"].append(
            f"`{qid}`: grew {at_reg} -> {initial} (+{growth}) but only {accounted} "
            "leg(s) are covered by a valid fanout_growth_events entry -- "
            f"{growth - accounted} unaccounted, which is post-hoc enlargement."
        )
    elif accounted > growth:
        flags["b_enlargement"].append(
            f"`{qid}`: fanout_growth_events claim {accounted} added leg(s) but the "
            f"denominator only grew by {growth} ({at_reg} -> {initial}) -- "
            "the growth record and the denominator disagree."
        )
    elif growth > 0:
        # Honest-reporting reminder: a growing denominator is a non-convergence
        # signal even when it is entirely legitimate.
        flags["e_labelled_growth"].append(
            f"`{qid}`: denominator grew {at_reg} -> {initial} across {ok_events} "
            "labelled portfolio(s). Legitimate, but report the reduction ratio BOTH "
            "ways -- a campaign enumerating new rivals as it eliminates old ones has "
            "not converged."
        )
    return min(accounted, growth)


def audit(registry: dict, timeseries: list) -> dict:
    """Return {flag_bucket: [messages]} for each of the four checks, plus the
    advisory `e_labelled_growth` bucket (labelled fan-out; NOT a violation)."""
    flags = {"a_unbacked_drop": [], "b_enlargement": [],
             "c_confirmed_no_control": [], "d_bar_violation": [],
             "e_labelled_growth": [], "f_unverifiable": [], "g_witnessed": []}
    questions = registry.get("questions") or []
    # Total legs added by VALID labelled fan-out, keyed by the date the growth was
    # recorded -- lets the time-series check attribute a total_initial rise.
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
        # (b3) labelled fan-out growth of an EXISTING question (conditions a-c).
        _validate_fanout_growth(q, flags)
        for ev in q.get("fanout_growth_events") or []:
            date = (ev.get("recorded_utc") or "")[:10]
            if date:
                labelled_growth_by_date[date] = (
                    labelled_growth_by_date.get(date, 0) + int(ev.get("delta") or 0))
        # A newly-registered question also legitimately grows total_initial.
        reg_date = (q.get("registered_utc") or "")[:10]
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

            # (c) confirmed without a passed control.
            if state == "confirmed" and res.get("control_passed") is not True:
                flags["c_confirmed_no_control"].append(
                    f"`{qid}`/`{hid}`: state=confirmed but control_passed="
                    f"{res.get('control_passed')!r} -- a confirmed node needs a passed control."
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
            flags["a_unbacked_drop"].append(
                f"time series {prev.get('date')} -> {cur.get('date')}: "
                f"surviving fell by {-d_surv} but resolved_out did not rise "
                f"(delta_resolved_out={d_res}) -- drop is not backed by adjudicated eliminations."
            )
        # (b-timeseries) frozen initial set grew. Attribute the rise to labelled
        # sources landing in this window -- new-question registrations and valid
        # fan-out growth events. Only the UNATTRIBUTED remainder is a violation.
        if d_init > 0:
            lo, hi = prev.get("date") or "", cur.get("date") or ""
            attributed = sum(
                n for date, n in labelled_growth_by_date.items() if lo < date <= hi
            )
            if attributed >= d_init:
                flags["e_labelled_growth"].append(
                    f"time series {lo} -> {hi}: total_initial grew by {d_init}, fully "
                    f"attributed to labelled sources landing in this window "
                    f"(new-question registrations + fanout_growth_events, {attributed} "
                    "leg(s)) -- advisory, not a violation."
                )
            else:
                flags["b_enlargement"].append(
                    f"time series {lo} -> {hi}: total_initial grew by {d_init} but only "
                    f"{attributed} leg(s) are attributable to a labelled source -- "
                    f"{d_init - attributed} enlarged the frozen denominator unlabelled."
                )
    return flags


def render_report(flags: dict, registry: dict, timeseries: list, now: str) -> str:
    # `e_labelled_growth` is ADVISORY -- it is reported, but never counted as a flag.
    total = sum(len(v) for k, v in flags.items() if k not in ADVISORY_BUCKETS)
    n_advisory = len(flags.get("e_labelled_growth") or [])
    n_unverifiable = len(flags.get("f_unverifiable") or [])
    n_witnessed = len(flags.get("g_witnessed") or [])
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
        f"**{n_unverifiable}** unverifiable."
    )
    L.append("")
    sections = [
        ("a_unbacked_drop", "(a) Un-backed surviving-count drop",
         "A question's surviving count fell with no adjudicated `weakens`/discrimination behind the elimination."),
        ("b_enlargement", "(b) Post-hoc enlargement of a frozen set",
         "The frozen initial enumeration grew WITHOUT a valid labelled fan-out record, "
         "or a hypothesis was pre-registered after its own adjudicating run. "
         "Labelled GOV-FANOUT-1 growth is NOT counted here -- see the advisory section below."),
        ("c_confirmed_no_control", "(c) Confirmed without a passed control",
         "A `confirmed` hypothesis lacks control_passed == true."),
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
        "**Read these as a convergence signal, not an all-clear.** The denominator grows "
        "mostly by legs that are then eliminated, which makes the headline narrowing ratio "
        "look strongest exactly when a campaign is failing to converge and having to invent "
        "new candidate explanations. The dashboard reports surviving/original AND "
        "surviving/current-including-fan-out for this reason."
    )
    L.append("")
    if not adv:
        L.append("_None._")
    else:
        for msg in adv:
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
        {"date": "2026-07-01", "total_surviving": 5, "total_resolved_out": 0, "total_initial": 5},
        {"date": "2026-07-02", "total_surviving": 3, "total_resolved_out": 0, "total_initial": 5},  # (a) unbacked drop
        {"date": "2026-07-03", "total_surviving": 3, "total_resolved_out": 0, "total_initial": 7},  # (b) init grew
    ]
    # Hermetic: stub the two git lookups so the self-test never shells out (and so
    # it exercises the witness LOGIC rather than this repo's actual history).
    global _artifact_first_commit, _registry_first_witness
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
    for name, cond, msg in [
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
    if failures:
        print(f"SELF-TEST FAILED: {failures}")
        return 1
    print("SELF-TEST PASSED")
    return 0


def main() -> int:
    now = _utc_now_iso_z()
    registry = _load_json(REGISTRY)
    if not isinstance(registry, dict):
        print("hypothesis-space integrity: registry missing; nothing to audit.")
        REPORT.write_text(
            f"# Hypothesis-Space Integrity Audit\n\nGenerated: {now}\n\n"
            "_No registry found; nothing to audit._\n", encoding="utf-8")
        return 0
    timeseries = _load_timeseries(TIMESERIES)
    flags = audit(registry, timeseries)
    REPORT.write_text(render_report(flags, registry, timeseries, now), encoding="utf-8")
    total = sum(len(v) for k, v in flags.items() if k not in ADVISORY_BUCKETS)
    print(f"Hypothesis-space integrity report written: {REPORT.relative_to(REPO_ROOT)}")
    print(f"  flags: a={len(flags['a_unbacked_drop'])} b={len(flags['b_enlargement'])} "
          f"c={len(flags['c_confirmed_no_control'])} d={len(flags['d_bar_violation'])} "
          f"(total={total}, advisory/non-blocking)")
    print(f"  labelled fan-out growth (advisory, not a flag): "
          f"{len(flags['e_labelled_growth'])} note(s)")
    print(f"  pre-registration provenance: {len(flags['g_witnessed'])} git-witnessed, "
          f"{len(flags['f_unverifiable'])} unverifiable")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover - advisory, never blocks
        print(f"hypothesis-space integrity: non-fatal error ({exc.__class__.__name__}); exiting 0.",
              file=sys.stderr)
        sys.exit(0)
