#!/usr/bin/env python3
"""Build the Scientific Progress Dashboard rollup (Dimensions Build/Prove/Narrow/Decide).

DERIVE-ONLY. Reads the FROZEN pre-registration ledger
(evidence/planning/hypothesis_space_registry.v1.json) and joins it against live
project data -- the failure_autopsy_*.json fan-out stream, evidence/experiments
manifests, claim_evidence.v1.json Beta posteriors, evidence/planning/substrate_queue.json
build states, and serve.read_closure() -- to compute:

  Dim 1 (Build)   engineering completion + build-proof gap  <- substrate_queue.json
  Dim 2 (Prove)   epistemic closure (UNCHANGED mirror)      <- serve.read_closure()
  Dim 3 (Narrow)  surviving hypotheses per question         <- registry + autopsy
  Dim 4 (Decide)  decision-readiness state per question     <- registry + autopsy
  Momentum        every adjudicated run, by what it MOVED    <- deterministic map

Outputs:
  evidence/planning/hypothesis_space.v1.json         (the dashboard payload)
  evidence/planning/hypothesis_space_timeseries.v1.jsonl  (append-only snapshots)

CONTRACT (design rules 1, 2):
  * Never a gate. Always exits 0. A red panel blocks nothing.
  * No write-back to claims.yaml, closure weights, or the evidence scorer. The
    only persistent artifacts are the two files above -- a file the closure
    pipeline never reads.
  * The registry is the frozen denominator; this script only DERIVES from it.
    It does not invent hypotheses, states, or momentum classes.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/build_hypothesis_space.py

Registered in scripts/governance.sh (Step 3c-bis-6), as a closure_plan sibling.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
EXPERIMENTS_DIR = REPO_ROOT / "evidence" / "experiments"
REGISTRY = PLANNING_DIR / "hypothesis_space_registry.v1.json"
SUBSTRATE_QUEUE = PLANNING_DIR / "substrate_queue.json"
CLAIM_EVIDENCE = EXPERIMENTS_DIR / "claim_evidence.v1.json"
OUT_JSON = PLANNING_DIR / "hypothesis_space.v1.json"
OUT_TIMESERIES = PLANNING_DIR / "hypothesis_space_timeseries.v1.jsonl"

# Decision-readiness state -> coarse evidence decile. Deterministic (the decile
# is a read of the adjudicated readiness state, never a hand-set per-card number).
READINESS_DECILE = {
    "decided": 10,
    "decidable_now": 9,
    "discriminative_ready": 7,
    "prediction_rich_action_poor": 4,
    "observation_bottleneck": 2,
}
# States that count as an alive/surviving rival explanation.
ALIVE_STATES = {"alive", "untested"}
# States that count toward the reduction numerator ("ruled out / resolved away").
RESOLVED_OUT_STATES = {"eliminated", "split"}


def _utc_now_iso_z() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


# --------------------------------------------------------------------------
# Dim 1 -- Build (engineering completion, from substrate_queue.json)
# --------------------------------------------------------------------------

def _build_state(item: dict) -> str:
    """Normalise a substrate_queue entry into the build state machine:
    proposed -> implemented -> implemented_pending_validation -> validated.
    The queue's `status`/`implementation_status` fields are prose-polluted, so
    this is a substring classifier over both, most-advanced-wins."""
    s = " ".join(
        str(item.get(k) or "") for k in ("implementation_status", "status")
    ).lower()
    if not s.strip():
        return "proposed"
    if any(t in s for t in ("validated", "ceiling_lifted", "promoted",
                            "amend_validated", "loadbearing_pass")):
        return "validated"
    if any(t in s for t in ("pending_validation", "pending_behavioural_validation",
                            "substrate_landed")) or ("implemented" in s and "pending" in s):
        return "implemented_pending_validation"
    if any(t in s for t in ("implemented", "phase_1_implemented", "phase_2_implemented",
                            "built", "landed")):
        return "implemented"
    return "proposed"


def build_dimension(subq: dict) -> dict:
    items = subq.get("queue") or []
    counts = {"proposed": 0, "implemented": 0,
              "implemented_pending_validation": 0, "validated": 0}
    for it in items:
        counts[_build_state(it)] = counts.get(_build_state(it), 0) + 1
    total = len(items)
    built = (counts["implemented"] + counts["implemented_pending_validation"]
             + counts["validated"])
    # Build-proof gap: modules whose code exists but whose claim is not yet proven
    # (built but not stamped validated in the substrate ledger).
    build_proof_gap = counts["implemented"] + counts["implemented_pending_validation"]
    fraction = (built / total) if total else 0.0
    return {
        "question": "how much of the intended V3 architecture physically exists?",
        "total_modules": total,
        "built_modules": built,
        "fraction_built": round(fraction, 4),
        "state_counts": counts,
        "build_proof_gap": build_proof_gap,
        "build_proof_gap_note": (
            f"{built} modules built, {build_proof_gap} still unvalidated "
            "(per substrate_queue.json self-declared state; validation is usually "
            "stamped via claim promotion, so this is a conservative floor)."
        ),
        "source": "evidence/planning/substrate_queue.json",
        "independent_of": "Dim 2 (a module can be built while its claim is still candidate/v3_pending)",
    }


# --------------------------------------------------------------------------
# Dim 2 -- Prove (epistemic closure; UNCHANGED read-only mirror of read_closure)
# --------------------------------------------------------------------------

def prove_dimension() -> dict:
    """Import serve.read_closure() as the SINGLE source of truth. This never
    re-weights closure -- it embeds it. If serve is unavailable, the panel
    degrades to null rather than inventing a number."""
    try:
        spec = importlib.util.spec_from_file_location("ree_serve", REPO_ROOT / "serve.py")
        serve = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(serve)
        clo = serve.read_closure()
    except Exception as exc:  # pragma: no cover - panel degrades, never crashes
        return {
            "question": "is the claim proven? (conservative, unchanged)",
            "closure_pct": None,
            "node_total": None,
            "node_done_weighted": None,
            "unavailable_reason": f"{exc.__class__.__name__}",
            "source": "serve.read_closure() (read-only mirror)",
        }
    return {
        "question": "is the claim proven? (conservative, unchanged)",
        "closure_pct": round((clo.get("overall_progress") or 0.0) * 100.0, 1),
        "node_total": clo.get("node_total"),
        "node_done_weighted": clo.get("node_done_weighted"),
        "source": "serve.read_closure() (read-only mirror; closure weights untouched)",
        "authoritative_view": "/closure",
    }


# --------------------------------------------------------------------------
# Dim 3 + Dim 4 -- Narrow + Decide (from the frozen registry)
# --------------------------------------------------------------------------

def _question_rollup(q: dict) -> dict:
    hyps = q.get("hypotheses") or []
    initial = int(q.get("initial_frozen_count") or len(hyps))
    alive = 0
    resolved_out = 0
    confirmed = 0
    for h in hyps:
        st = (h.get("resolution") or {}).get("state") or "untested"
        if st in ALIVE_STATES:
            alive += 1
        elif st in RESOLVED_OUT_STATES:
            resolved_out += 1
        elif st == "confirmed":
            confirmed += 1
    synthesis = q.get("synthesis")
    # Surviving explanations: alive rivals, plus a single synthesis survivor when
    # the originals have collapsed onto one composed reading. A bare `confirmed`
    # answer (no synthesis, e.g. the DA-density verified run) is itself the 1
    # surviving explanation.
    if synthesis and synthesis.get("surviving_label"):
        surviving = alive + 1
    elif confirmed and alive == 0:
        surviving = confirmed
    else:
        surviving = alive if alive else max(0, initial - resolved_out - confirmed)
    reduction_num = resolved_out  # "ruled out / resolved away" (design: eliminated/split)
    reduction_ratio = (reduction_num / initial) if initial else 0.0
    # Coarse entropy proxy: only meaningful when survivors are enumerable and
    # roughly equiprobable. We report bits REMOVED (log2(initial) - log2(surviving))
    # -- the strongest defensible quantitative statement (design rule).
    bits_removed = None
    if initial > 0 and surviving >= 1:
        bits_removed = round(math.log2(initial) - math.log2(surviving), 2)

    # Dim 4 -- decision readiness state (derived from the adjudicated decision block).
    dec = q.get("decision") or {}
    if dec.get("decided") or dec.get("decision_log_ref"):
        readiness = "decided"
    elif dec.get("decidable"):
        readiness = "decidable_now"
    elif dec.get("observation_bottleneck"):
        readiness = "observation_bottleneck"
    elif dec.get("live_gate"):
        readiness = "discriminative_ready"
    else:
        readiness = "prediction_rich_action_poor"

    return {
        "qid": q.get("qid"),
        "title": q.get("title"),
        "short_title": q.get("short_title"),
        "claims": q.get("claims") or [],
        "is_hero": bool(q.get("is_hero")),
        "initial_frozen_count": initial,
        "surviving": surviving,
        "alive": alive,
        "resolved_out": resolved_out,
        "confirmed": confirmed,
        "reduction_numerator": reduction_num,
        "reduction_ratio": round(reduction_ratio, 4),
        "bits_removed": bits_removed,
        "synthesis": synthesis,
        "hypotheses": [
            {
                "hid": h.get("hid"),
                "label": h.get("label"),
                "desc": h.get("desc"),
                "axis": h.get("axis"),
                "state": (h.get("resolution") or {}).get("state") or "untested",
                "evidence_runs": (h.get("resolution") or {}).get("resolving_runs")
                or h.get("adjudicating_runs") or [],
                "basis": (h.get("resolution") or {}).get("basis"),
                "children": (h.get("resolution") or {}).get("children") or [],
                "met_elimination_bar": (h.get("resolution") or {}).get("met_elimination_bar"),
            }
            for h in hyps
        ],
        "decision": {
            "readiness_state": readiness,
            "evidence_decile": READINESS_DECILE.get(readiness, 5),
            "decision_question": dec.get("decision_question") or q.get("title"),
            "distance_phrase": dec.get("distance_phrase"),
            "live_gate": dec.get("live_gate"),
            "observation_bottleneck": dec.get("observation_bottleneck"),
        },
    }


# --------------------------------------------------------------------------
# Momentum feed -- deterministic map (design section 4, Step A)
# --------------------------------------------------------------------------

def _momentum_class(direction, epistemic, met_bar, discriminates_leg,
                    non_degenerate, is_implementation) -> str:
    d = (direction or "").lower()
    e = (epistemic or "").lower()
    if is_implementation:
        return "implementation_completed"
    if d in ("supports", "supports_necessary"):
        return "confirmed"
    if d == "weakens" and met_bar:
        return "ruled_out"
    if "measurement_degeneracy" in e or "measurement_artifact" in e:
        # a resolved measurement degeneracy/artefact
        return "measurement_improved"
    if "measurement_test_design_defect" in e or "measurement_gap" in e:
        return "control_repaired"
    if non_degenerate is False or "precondition_unmet" in e or "starved" in e or "vacuous" in e:
        return "underpowered"
    if d == "non_contributory" and discriminates_leg:
        return "hypothesis_narrowed"
    if d == "inconclusive":
        return "inconclusive"
    if d == "non_contributory":
        return "inconclusive"
    return "inconclusive"


def momentum_feed(registry: dict) -> list:
    """One entry per resolving run across the registry, classified by what it
    MOVED (not the binary PASS/FAIL). Deterministic; never hand-set."""
    feed = []
    seen = set()
    for q in registry.get("questions") or []:
        for h in q.get("hypotheses") or []:
            res = h.get("resolution") or {}
            runs = res.get("resolving_runs") or []
            if not runs:
                continue
            key_run = runs[-1]  # most-advanced run for this leg
            if key_run in seen:
                continue
            seen.add(key_run)
            discriminates = bool(res.get("self_route_label")) or res.get("state") in RESOLVED_OUT_STATES
            cls = _momentum_class(
                res.get("evidence_direction"),
                res.get("epistemic_category"),
                res.get("met_elimination_bar"),
                discriminates,
                res.get("non_degenerate"),
                is_implementation=False,
            )
            feed.append({
                "run": key_run,
                "all_runs": runs,
                "momentum_class": cls,
                "qid": q.get("qid"),
                "claims": q.get("claims") or [],
                "moved": res.get("basis"),
                "resolved_utc": res.get("resolved_utc"),
                "evidence_direction": res.get("evidence_direction"),
            })
        # Synthesis under test -> an implementation_completed entry (substrate built,
        # proof pending), matching design section 4 (implementation completed).
        syn = q.get("synthesis") or {}
        under = syn.get("under_test")
        if under and under not in seen:
            seen.add(under)
            feed.append({
                "run": under,
                "all_runs": [under],
                "momentum_class": "implementation_completed",
                "qid": q.get("qid"),
                "claims": q.get("claims") or [],
                "moved": f"Composed build under test: {syn.get('surviving_label')} "
                         "(substrate landed, proof pending).",
                "resolved_utc": None,
                "evidence_direction": "pending",
            })
    # Sort newest-first; runs with no date sink to the bottom (pending).
    feed.sort(key=lambda x: (x.get("resolved_utc") or "0000", x.get("run")), reverse=True)
    return feed


# --------------------------------------------------------------------------
# Hero time series -- reconstruct the surviving curve from resolution dates
# --------------------------------------------------------------------------

def hero_series(questions_rollup: list, registry: dict, closure_pct, build_pct) -> list:
    """Reconstruct total-surviving-hypotheses over time from the frozen registry's
    resolution dates. Each hypothesis eliminated/split on its resolved_utc drops the
    running total by 1. This is a REAL, deterministic reconstruction from the frozen
    ledger -- not a fabricated curve. Closure % is shown at its current value (flat)
    because that is the honest present reading; the append-only jsonl accumulates true
    closure history going forward."""
    total_initial = sum(q["initial_frozen_count"] for q in questions_rollup)
    # collect (date, delta) resolution events
    events = []
    for q in registry.get("questions") or []:
        for h in q.get("hypotheses") or []:
            res = h.get("resolution") or {}
            if res.get("state") in RESOLVED_OUT_STATES and res.get("resolved_utc"):
                events.append(res["resolved_utc"][:10])
    events.sort()
    if not events:
        return [{"date": _utc_now_iso_z()[:10], "surviving": total_initial,
                 "closure_pct": closure_pct, "build_pct": build_pct}]
    # earliest registration point (full space) then step down at each event date
    series = []
    first_date = min(
        (q.get("registered_utc") or events[0])[:10]
        for q in (registry.get("questions") or [])
    )
    series.append({"date": first_date, "surviving": total_initial,
                   "closure_pct": closure_pct, "build_pct": build_pct})
    running = total_initial
    from collections import Counter
    per_date = Counter(events)
    for date in sorted(per_date):
        running -= per_date[date]
        series.append({"date": date, "surviving": running,
                       "closure_pct": closure_pct, "build_pct": build_pct})
    # ensure the final point reflects today's true surviving total
    today = _utc_now_iso_z()[:10]
    surviving_now = sum(q["surviving"] for q in questions_rollup)
    if series[-1]["date"] != today or series[-1]["surviving"] != surviving_now:
        series.append({"date": today, "surviving": surviving_now,
                       "closure_pct": closure_pct, "build_pct": build_pct})
    # Collapse same-date points to their end-of-day value (last event wins) so the
    # chart has one x-position per date.
    collapsed: dict[str, dict] = {}
    for pt in series:
        collapsed[pt["date"]] = pt
    return [collapsed[d] for d in sorted(collapsed)]


# --------------------------------------------------------------------------
# Time-series ledger (append-only; one snapshot per run, deduped by date)
# --------------------------------------------------------------------------

def append_timeseries(snapshot: dict) -> None:
    date = snapshot["date"]
    lines = []
    if OUT_TIMESERIES.exists():
        for ln in OUT_TIMESERIES.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln:
                continue
            try:
                rec = json.loads(ln)
            except ValueError:
                continue
            if rec.get("date") == date:
                continue  # replace same-day snapshot (idempotent re-runs)
            lines.append(json.dumps(rec, sort_keys=True))
    lines.append(json.dumps(snapshot, sort_keys=True))
    OUT_TIMESERIES.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------

def main() -> int:
    now = _utc_now_iso_z()
    registry = _load_json(REGISTRY)
    if not isinstance(registry, dict) or not registry.get("questions"):
        print("hypothesis_space: registry missing or empty; nothing to build.")
        # still emit an empty-but-valid payload so the page renders a friendly state
        payload = {
            "schema_version": "hypothesis_space/v1",
            "generated_at": now,
            "empty": True,
            "note": "No hypothesis_space_registry.v1.json found.",
        }
        OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return 0

    subq = _load_json(SUBSTRATE_QUEUE) or {}
    dim_build = build_dimension(subq)
    dim_prove = prove_dimension()

    questions = [_question_rollup(q) for q in registry["questions"]]
    total_surviving = sum(q["surviving"] for q in questions)
    total_initial = sum(q["initial_frozen_count"] for q in questions)
    total_resolved_out = sum(q["resolved_out"] for q in questions)
    ready_count = sum(1 for q in questions
                      if q["decision"]["readiness_state"] in ("decidable_now", "decided"))

    feed = momentum_feed(registry)

    closure_pct = dim_prove.get("closure_pct")
    build_pct = round(dim_build["fraction_built"] * 100.0, 1)
    series = hero_series(questions, registry, closure_pct, build_pct)

    payload = {
        "schema_version": "hypothesis_space/v1",
        "generated_at": now,
        "generator": "scripts/build_hypothesis_space.py",
        "contract": "derive-only; exits 0; never a gate; no write-back to claims.yaml/closure/scorer.",
        "registry": "evidence/planning/hypothesis_space_registry.v1.json",
        "needles": {
            "build": dim_build,
            "prove": dim_prove,
            "narrow": {
                "question": "how many rival explanations still survive?",
                "total_surviving": total_surviving,
                "total_initial": total_initial,
                "total_resolved_out": total_resolved_out,
                "open_questions": len(questions),
            },
            "decide": {
                "question": "can a design choice legitimately be made?",
                "ready": ready_count,
                "open_questions": len(questions),
            },
        },
        "hero_series": series,
        "questions": questions,
        "momentum": feed,
        "references": {
            "closure_map": "/closure",
            "design_doc": "evidence/planning/scientific_progress_dashboard_design.md",
            "integrity_audit": "evidence/planning/hypothesis_space_integrity.md",
        },
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")

    append_timeseries({
        "date": now[:10],
        "snapshot_utc": now,
        "total_surviving": total_surviving,
        "total_initial": total_initial,
        "total_resolved_out": total_resolved_out,
        "closure_pct": closure_pct,
        "build_pct": build_pct,
        "ready": ready_count,
        "open_questions": len(questions),
    })

    print(f"hypothesis_space written: {OUT_JSON.relative_to(REPO_ROOT)}")
    print(
        f"  build={build_pct}% ({dim_build['built_modules']}/{dim_build['total_modules']}, "
        f"gap={dim_build['build_proof_gap']})  "
        f"prove={closure_pct}%  "
        f"surviving={total_surviving}/{total_initial} "
        f"(resolved_out={total_resolved_out})  "
        f"ready={ready_count}/{len(questions)}  "
        f"momentum_items={len(feed)}"
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover - derive-only never blocks governance
        print(f"hypothesis_space: non-fatal error ({exc.__class__.__name__}: {exc}); exiting 0.",
              file=sys.stderr)
        sys.exit(0)
