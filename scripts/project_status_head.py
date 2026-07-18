#!/usr/bin/env python3
"""project_status_head.py -- SHP-1 shadow status-head projector (READ-ONLY / SHADOW).

status_history_plane:SHP-1 (see evidence/planning/status_history_plane_separation_design.md).

For every closure_plan node across evidence/planning/*_plan.md this projects a
status-plane `live:` head + a history-plane `join:` block from the append-only
event log, and emits three shadow artefacts to a SCRATCH dir only:

  1. shadow `live:` + `join:` blocks per node        -> status_head.shadow.yaml (+ .md)
  2. per-plan `<plan>_history.md` sidecar            -> pointer index into event files,
                                                        newest LAST (never re-pastes history)
  3. a DIFF-VS-BLOB report                           -> diff_vs_blob.md  (input to SHP-2)

Event log =
  * failure_autopsy_*.json          (schema failure_autopsy/v1; one event per target)
  * PASS result manifests           (evidence/experiments/**.json with outcome == PASS)
  * decision_log.v1.jsonl entries   (status-moving promotions/demotions)

Join per node (contract term 5, union):
  join(node) = events where (bears_on contains a node token) UNION (claim_ids intersects scope_claims)
  Older events lack bears_on and join only via claim_ids. Node tokens are the node id
  plus the substrate sd_ids harvested from the claim-joined slice (the additive bears_on
  backfill), so token-only events (e.g. the 732/732a policy-learning autopsies, claim_ids=[])
  are pulled in via `f_dominance_conversion_ceiling`.

Projection (`live`, contract terms 2/3/6):
  * head = newest FORWARD-routing event
      forward = autopsy that (has recommended_substrate_queue_entry with a target
                OR routing in {queue-experiment, implement-substrate})
                AND is NOT a measurement/instrument autopsy
                (routing == governance AND category in {test_design_ceiling, observability})
    -- the measurement-autopsy override wins even when a substrate entry is present
       (proven on V3-EXQ-732a: has substrate entry, but routing=governance/test_design_ceiling
        -> modifier, NOT the head).
  * needs_review = the newest forward event predates a later non-forward event,
                   OR children of an umbrella disagree.
  * brake fired  = count(substrate_ceiling events in slice) >= threshold.

This script PROMOTES/DEMOTES NOTHING. It edits NO *_plan.md and writes NOTHING into
any canonical file -- only into the (git-ignorable) scratch output dir.
"""

import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("ERROR: PyYAML required (import yaml failed)\n")
    sys.exit(2)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DEFAULT_BRAKE_THRESHOLD = 2  # count(substrate_ceiling) >= threshold => brake fired
MEASUREMENT_CATEGORIES = {"test_design_ceiling", "observability"}
FORWARD_ROUTINGS = {"queue-experiment", "implement-substrate"}

# A claim id (MECH-/ARC-/SD-/Q-/INV-/GAP-...) lives in claim_ids, not the join-token
# set: harvesting one as a substrate token would over-broaden the union join.
CLAIM_ID_RE = re.compile(r"^(?:MECH|ARC|SD|Q|INV|GAP)-[0-9A-Za-z]+$")


def is_substrate_token(t):
    """A harvestable bears_on token: a substrate sd_id (e.g. f_dominance_conversion_ceiling),
    NOT a cross-plan node id (has ':') and NOT a claim id (lives in claim_ids)."""
    return bool(t) and ":" not in t and not CLAIM_ID_RE.match(t)

# Reference-token regexes used by the diff-vs-blob report. Order matters: longer,
# more specific patterns first so they win the span.
REF_PATTERNS = [
    ("run_id", re.compile(r"\bv3_exq_[a-z0-9_]+_v3\b", re.I)),
    ("autopsy", re.compile(r"\bfailure_autopsy_[A-Za-z0-9._-]+?(?=[\s,.;:)\"']|$)")),
    ("exq", re.compile(r"\bV3-EXQ-[0-9]+[a-z]*\b")),
    ("exq", re.compile(r"\bEXQ-[0-9]+[a-z]*\b")),
    ("claim", re.compile(r"\b(?:MECH|ARC|SD|Q|INV|GAP)-[0-9A-Za-z]+\b")),
    ("commit", re.compile(r"\bmaster ([0-9a-f]{7,40})\b")),
]

# ---------------------------------------------------------------------------
# Timestamp parsing (three formats live in the log)
# ---------------------------------------------------------------------------


def parse_ts(s):
    """Parse the timestamp formats seen across event sources; return datetime or None."""
    if not s or not isinstance(s, str):
        return None
    s = s.strip()
    # compact experiment stamp: 20260709T193517Z
    m = re.fullmatch(r"(\d{8})T(\d{6})Z", s)
    if m:
        try:
            return datetime.strptime(s, "%Y%m%dT%H%M%SZ")
        except ValueError:
            return None
    t = s.replace("Z", "").replace("+00:00", "")
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%Y-%m-%dT%H:%M"):
        try:
            return datetime.strptime(t, fmt)
        except ValueError:
            continue
    return None


def ts_key(dt):
    return dt if dt is not None else datetime.min


# ---------------------------------------------------------------------------
# Event model
# ---------------------------------------------------------------------------


class Event(object):
    __slots__ = (
        "eid", "kind", "ts", "claim_ids", "bears_on", "routing", "routing_detail",
        "category", "direction", "substrate_target", "has_substrate_entry",
        "brake_fired", "is_substrate_ceiling", "queue_id", "run_id", "summary",
        "source_path", "ref_tokens",
    )

    def __init__(self, **kw):
        for s in self.__slots__:
            setattr(self, s, kw.get(s))
        self.claim_ids = self.claim_ids or []
        self.bears_on = self.bears_on or []
        self.ref_tokens = self.ref_tokens or set()

    def is_measurement(self):
        return self.kind == "autopsy" and self.routing == "governance" and \
            (self.category in MEASUREMENT_CATEGORIES)

    def is_forward(self):
        if self.kind != "autopsy":
            return False
        if self.is_measurement():
            return False  # measurement-autopsy override
        if self.has_substrate_entry and self.substrate_target:
            return True
        if self.has_substrate_entry:  # entry present but no explicit target -> still forward
            return True
        return self.routing in FORWARD_ROUTINGS


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def _as_text(v):
    """Coerce a YAML scalar blob to text (some nodes carry int/None phase/owner values)."""
    if v is None:
        return ""
    return v if isinstance(v, str) else str(v)


def extract_frontmatter(text):
    """Return the YAML frontmatter block (text between the first two `---` lines)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def load_plans(planning_dir):
    """Load closure_plan nodes from every *_plan.md; return (plans, skipped)."""
    plans = []
    skipped = []
    for path in sorted(glob.glob(os.path.join(planning_dir, "*_plan.md"))):
        text = open(path, encoding="utf-8").read()
        fm = extract_frontmatter(text)
        if fm is None:
            continue
        try:
            meta = yaml.safe_load(fm)
        except yaml.YAMLError as e:
            skipped.append((os.path.basename(path), str(e).splitlines()[0]))
            continue
        cp = (meta or {}).get("closure_plan")
        if not cp or not cp.get("nodes"):
            continue
        plan_scope = cp.get("scope_claims") or []
        nodes = []
        for nd in cp["nodes"]:
            if not isinstance(nd, dict) or not nd.get("id"):
                continue
            nodes.append({
                "id": nd["id"],
                "title": nd.get("title", "") or "",
                "status": nd.get("status"),
                "severity": nd.get("severity"),
                "assembly_status": nd.get("assembly_status"),
                "scope_claims": nd.get("scope_claims") or plan_scope,
                "blobs": {
                    "phase": _as_text(nd.get("phase")),
                    "owner_exq": _as_text(nd.get("owner_exq")),
                    "awaiting": _as_text(nd.get("awaiting")),
                },
            })
        plans.append({
            "plan_id": cp.get("id") or os.path.basename(path).replace("_plan.md", ""),
            "file": os.path.relpath(path, os.path.dirname(os.path.dirname(planning_dir))),
            "scope_claims": plan_scope,
            "nodes": nodes,
        })
    return plans, skipped


def _ref_tokens_from_text(*chunks):
    toks = set()
    for c in chunks:
        if not c:
            continue
        if not isinstance(c, str):
            c = json.dumps(c)
        for _kind, pat in REF_PATTERNS:
            for m in pat.finditer(c):
                toks.add(m.group(1) if m.groups() else m.group(0))
    return toks


def load_autopsies(repo_root):
    events = []
    seen = set()
    for path in sorted(glob.glob(
            os.path.join(repo_root, "evidence", "**", "failure_autopsy_*.json"),
            recursive=True)):
        if path in seen:
            continue
        seen.add(path)
        try:
            d = json.load(open(path, encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if not isinstance(d, dict):
            continue
        stem = os.path.basename(path)[:-5]  # strip .json
        gen = d.get("generated_utc")
        targets = d.get("targets") or []
        multi = len(targets) > 1
        rel = os.path.relpath(path, repo_root)
        for t in targets:
            if not isinstance(t, dict):
                continue
            qid = t.get("queue_id")
            sqe = t.get("recommended_substrate_queue_entry") or {}
            has_entry = bool(sqe)
            target_sd = sqe.get("target_sd_id") or sqe.get("sd_id_suggested")
            cat = t.get("recommended_epistemic_category")
            brake = (t.get("re_derive_brake") or {}).get("fired", False)
            eid = stem + ("#" + qid if (multi and qid) else "")
            ref = _ref_tokens_from_text(
                stem, qid, t.get("run_id"), t.get("routing_detail"),
                json.dumps(t.get("claim_ids") or []), json.dumps(t.get("bears_on") or []),
                target_sd,
            )
            ref.add(stem)
            if qid:
                ref.add(qid)
            events.append(Event(
                eid=eid, kind="autopsy", ts=parse_ts(gen),
                claim_ids=list(t.get("claim_ids") or []),
                bears_on=list(t.get("bears_on") or []),
                routing=t.get("routing"), routing_detail=t.get("routing_detail"),
                category=cat, direction=t.get("recommended_evidence_direction"),
                substrate_target=target_sd, has_substrate_entry=has_entry,
                brake_fired=bool(brake), is_substrate_ceiling=(cat == "substrate_ceiling"),
                queue_id=qid, run_id=t.get("run_id"),
                summary=_autopsy_summary(t), source_path=rel, ref_tokens=ref,
            ))
    return events


def _autopsy_summary(t):
    d = t.get("recommended_evidence_direction") or "?"
    c = t.get("recommended_epistemic_category") or "?"
    r = t.get("routing") or "?"
    return "autopsy %s/%s routing=%s" % (d, c, r)


def load_manifests(repo_root):
    """PASS result manifests only (status-moving positive events)."""
    events = []
    exp_dir = os.path.join(repo_root, "evidence", "experiments")
    paths = glob.glob(os.path.join(exp_dir, "*.json"))
    paths += glob.glob(os.path.join(exp_dir, "**", "runs", "**", "manifest.json"), recursive=True)
    paths += glob.glob(os.path.join(exp_dir, "*", "*.json"))
    for path in sorted(set(paths)):
        try:
            if os.path.getsize(path) > 3_000_000:
                continue
            d = json.load(open(path, encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if not isinstance(d, dict):
            continue
        if d.get("outcome") != "PASS":
            continue
        run_id = d.get("run_id")
        if not run_id:
            continue
        rel = os.path.relpath(path, repo_root)
        ref = _ref_tokens_from_text(run_id, d.get("queue_id"),
                                    json.dumps(d.get("claim_ids") or []))
        if d.get("queue_id"):
            ref.add(d["queue_id"])
        ref.add(run_id)
        events.append(Event(
            eid=run_id, kind="manifest",
            ts=parse_ts(d.get("timestamp_utc") or d.get("generated_utc")),
            claim_ids=list(d.get("claim_ids") or []),
            bears_on=list(d.get("bears_on") or []),
            routing=None, routing_detail=None, category="PASS",
            direction=d.get("evidence_direction"), substrate_target=None,
            has_substrate_entry=False, brake_fired=False, is_substrate_ceiling=False,
            queue_id=d.get("queue_id"), run_id=run_id,
            summary="PASS manifest %s" % (d.get("evidence_direction") or "supports"),
            source_path=rel, ref_tokens=ref,
        ))
    return events


def load_decisions(repo_root):
    events = []
    path = os.path.join(repo_root, "evidence", "decisions", "decision_log.v1.jsonl")
    if not os.path.exists(path):
        return events
    rel = os.path.relpath(path, repo_root)
    for i, line in enumerate(open(path, encoding="utf-8")):
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except ValueError:
            continue
        cid = d.get("claim_id")
        claim_ids = [cid] if cid else (d.get("claim_ids") or [])
        ts = d.get("timestamp_utc")
        eid = "decision:%s@%s" % (cid or "?", ts or i)
        ref = _ref_tokens_from_text(json.dumps(claim_ids), d.get("rationale"))
        for c in claim_ids:
            ref.add(c)
        events.append(Event(
            eid=eid, kind="decision", ts=parse_ts(ts), claim_ids=list(claim_ids),
            bears_on=[], routing=None, routing_detail=None,
            category=d.get("recommendation"), direction=d.get("decision_status"),
            substrate_target=None, has_substrate_entry=False, brake_fired=False,
            is_substrate_ceiling=False, queue_id=None, run_id=None,
            summary="decision %s (%s)" % (d.get("recommendation") or "?",
                                          d.get("decision_status") or "?"),
            source_path="%s#L%d" % (rel, i + 1), ref_tokens=ref,
        ))
    return events


# ---------------------------------------------------------------------------
# Join + projection
# ---------------------------------------------------------------------------


def join_node(node, events):
    """Union join; return (slice, provenance) where provenance[eid] = list of reasons."""
    scope = set(node["scope_claims"])
    nid = node["id"]
    prov = defaultdict(list)

    # pass 1 -- claim-id join and node-id-as-bears_on join
    primary = []
    for ev in events:
        matched_claims = scope & set(ev.claim_ids)
        if matched_claims:
            prov[ev.eid].append("claim_ids:" + ",".join(sorted(matched_claims)))
            primary.append(ev)
        if nid in ev.bears_on:
            prov[ev.eid].append("bears_on:node_id")
            if ev not in primary:
                primary.append(ev)

    # harvest substrate tokens (additive bears_on backfill) from the primary slice
    tokens = {nid}
    for ev in primary:
        if is_substrate_token(ev.substrate_target):
            tokens.add(ev.substrate_target)
        for b in ev.bears_on:
            if is_substrate_token(b):  # substrate sd_id, not a node/claim token
                tokens.add(b)

    # pass 2 -- token join (union)
    joined = list(primary)
    joined_ids = {ev.eid for ev in primary}
    for ev in events:
        hit = tokens & set(ev.bears_on)
        if hit:
            prov[ev.eid].append("bears_on_token:" + ",".join(sorted(hit)))
            if ev.eid not in joined_ids:
                joined.append(ev)
                joined_ids.add(ev.eid)

    joined.sort(key=lambda e: (ts_key(e.ts), e.eid or ""))  # eid tiebreak = deterministic
    return joined, tokens, dict(prov)


def project_live(node, slc, threshold):
    """Project the `live` head + brake from an event slice. Returns a dict."""
    forwards = [e for e in slc if e.is_forward()]
    non_forwards = [e for e in slc if not e.is_forward()]

    head = forwards[-1] if forwards else (slc[-1] if slc else None)

    # needs_review is the design's narrow safety valve (contract term 3): a genuine head
    # AMBIGUITY -- a later non-forward status-moving event postdates the chosen forward head
    # (the 732a case), or an umbrella's children disagree (added in the umbrella pass).
    # Absence of any forward event, or an empty slice, are NOT ambiguity -- they are exposed
    # as the separate `head_forward` / `no_events` fields so needs_review stays a real signal.
    reasons = []
    needs_review = False
    if forwards:
        newest_forward = forwards[-1]
        later_non_forward = [e for e in non_forwards
                             if ts_key(e.ts) > ts_key(newest_forward.ts)]
        if later_non_forward:
            needs_review = True
            kinds = sorted({("measurement" if e.is_measurement() else e.kind)
                            for e in later_non_forward})
            reasons.append("newest_forward_predates_later_%s_event(s)" % "+".join(kinds))

    subceil = [e for e in slc if e.is_substrate_ceiling]
    brake_fired = len(subceil) >= threshold

    live = {
        "as_of": head.ts.strftime("%Y-%m-%d") if (head and head.ts) else None,
        "from": head.eid if head else None,
        "head_kind": head.kind if head else None,
        "head_forward": bool(forwards),
        "no_events": not slc,
        "verdict": _verdict(head),
        "next": _next(head),
        "brake": "fired" if brake_fired else "not_fired",
        "brake_count": len(subceil),
        "brake_threshold": threshold,
        "needs_review": needs_review,
        "needs_review_reasons": reasons,
        "slice_size": len(slc),
        "forward_events": len(forwards),
    }
    return live, head


def _verdict(ev):
    if ev is None:
        return None
    if ev.kind == "autopsy":
        return "%s/%s" % (ev.direction or "?", ev.category or "?")
    if ev.kind == "manifest":
        return "%s/PASS" % (ev.direction or "supports")
    if ev.kind == "decision":
        return "%s/%s" % (ev.category or "?", ev.direction or "?")
    return None


def _next(ev):
    if ev is None:
        return None
    if ev.kind == "autopsy":
        # routing_detail is normally a string, but a few autopsies carry a
        # structured (dict/list) routing_detail. Coerce defensively: str() is
        # identity for the string case (so closure-plane output is unchanged),
        # and keeps project_live from crashing on the richer heads the per-claim
        # join (SHP-4) surfaces that the closure-plan joins never reached.
        rd = ev.routing_detail
        nxt = (rd if isinstance(rd, str) else ("" if rd is None else str(rd))).strip()
        if nxt:
            return nxt if len(nxt) <= 400 else nxt[:397] + "..."
        return "routing=%s" % (ev.routing or "?")
    if ev.kind == "manifest":
        return "PASS result landed (%s)" % (ev.run_id or "")
    if ev.kind == "decision":
        return ev.summary
    return None


# The STABLE subset of a projected `live` dict that SHP-2 persists into the plan
# node (design sec 4a) and that the SHP-2 status-plane drift check compares
# (projected `live` == stored `live`). Volatile derivations -- brake_count,
# slice_size, forward_events -- are DELIBERATELY excluded: they change as events
# accrue without changing the projected *status reading*, so including them would
# make the drift check perpetually red. `brake` (fired/not_fired) IS included; the
# raw count is not. This is the single source of truth for "what live: looks like
# when stored", shared by the collapse tool and check_closure_drift.py.
STORED_LIVE_FIELDS = ("as_of", "from", "verdict", "next", "brake", "needs_review")


def stored_live_view(live):
    """Project a full `live` dict down to the stable, persisted-into-plan subset.

    Returns an ordered plain dict with STORED_LIVE_FIELDS, plus
    `needs_review_reasons` only when needs_review is true (so the stored block
    carries the human-glance reason without noise when there is none)."""
    if not live:
        return {}
    out = {k: live.get(k) for k in STORED_LIVE_FIELDS}
    if live.get("needs_review") and live.get("needs_review_reasons"):
        out["needs_review_reasons"] = list(live["needs_review_reasons"])
    return out


# The history-plane counterpart of STORED_LIVE_FIELDS: the subset of a node's
# projected `join` that SHP-2 persists into the plan node. `tokens` and
# `slice_event_ids` are DELIBERATELY excluded for the same reason brake_count /
# slice_size are excluded from the live view -- they grow with every event and
# would make the drift check perpetually red without changing the join's meaning.
#
# `scope_claims` is the node's EFFECTIVE INPUT scope (node-level `scope_claims:`
# when set, else the plan-level list), exactly as load_plans resolves it. It is
# the one stored field that is an INPUT echo rather than a derivation, which is
# precisely why it must be checked: editing the plan-level `scope_claims:` list
# changes the join for EVERY node in the plan, and if that edit moves no node's
# live head then a live-only drift check sees nothing and the stored joins go
# silently stale. See check_closure_drift.status_plane_drift.
STORED_JOIN_FIELDS = ("bears_on", "scope_claims")


def stored_join_view(pr):
    """Project a node's full projection dict down to the stored `join:` subset.

    Takes the whole projection (not just the join) because the two stored fields
    come from different places: `bears_on` is derived from the joined slice, while
    `scope_claims` is the node's effective input scope. This is the single source
    of truth for "what join: looks like when stored", shared by the collapse tool
    and check_closure_drift.py -- mirroring stored_live_view for the status plane."""
    if not pr:
        return {}
    return {
        "bears_on": list(pr.get("join_bears_on") or []),
        "scope_claims": list(pr.get("node_scope_claims") or []),
    }


# ---------------------------------------------------------------------------
# Diff-vs-blob (the non-destructive razor audit, contract sec 5)
# ---------------------------------------------------------------------------


def _blob_ref_tokens(text):
    out = []
    for kind, pat in REF_PATTERNS:
        for m in pat.finditer(text or ""):
            out.append((kind, m.group(1) if m.groups() else m.group(0)))
    return out


_SENT_SPLIT = re.compile(r"(?<=[.;])\s+(?=[A-Z(0-9])")


def diff_blob(node, slc, global_coverage):
    """Diff each hand-written blob against the joined slice. Return per-field findings."""
    slice_coverage = set()
    for ev in slc:
        slice_coverage |= ev.ref_tokens
    findings = {}
    for field, text in node["blobs"].items():
        if not text:
            continue
        refs = _blob_ref_tokens(text)
        covered, join_gap, at_risk = [], [], []
        for kind, tok in refs:
            if tok in slice_coverage:
                covered.append((kind, tok))
            elif tok in global_coverage:
                join_gap.append((kind, tok))          # exists as an event, just not joined
            else:
                at_risk.append((kind, tok))            # HISTORY BIT AT RISK (sec 5)
        # sentence-level residual: sentences with no covered anchor at all
        residual_sentences = []
        for sent in _SENT_SPLIT.split(text):
            s = sent.strip()
            if len(s) < 25:
                continue
            stoks = [t for _k, t in _blob_ref_tokens(s)]
            if not any(t in slice_coverage for t in stoks):
                residual_sentences.append(s if len(s) <= 240 else s[:237] + "...")
        findings[field] = {
            "covered": _dedup(covered),
            "join_gap": _dedup(join_gap),
            "at_risk": _dedup(at_risk),
            "residual_sentences": residual_sentences,
        }
    return findings


def _dedup(pairs):
    seen = []
    out = []
    for k, t in pairs:
        if t in seen:
            continue
        seen.append(t)
        out.append({"kind": k, "token": t})
    return out


# ---------------------------------------------------------------------------
# Event loading + full projection (shared by the shadow run and the drift check)
# ---------------------------------------------------------------------------


def load_events(repo_root):
    """Load the full append-only event log. Returns (events, event_counts)."""
    autopsies = load_autopsies(repo_root)
    manifests = load_manifests(repo_root)
    decisions = load_decisions(repo_root)
    events = autopsies + manifests + decisions
    counts = {"autopsy": len(autopsies), "manifest_PASS": len(manifests),
              "decision": len(decisions)}
    return events, counts


def _umbrella_children_disagree_pass(plans, projections):
    """contract term 3: flag an umbrella node needs_review when its children's
    projected verdicts disagree. Mutates projections[*]['live'] in place."""
    for plan in plans:
        umbrellas = [n for n in plan["nodes"]
                     if "umbrella" in (n["title"] + " "
                                       + n["blobs"]["owner_exq"]).lower()]
        child_nodes = list(plan["nodes"])
        for um in umbrellas:
            children = [n for n in child_nodes if n["id"] != um["id"]]
            verdicts = sorted({projections[c["id"]]["live"]["verdict"]
                               for c in children
                               if projections[c["id"]]["live"]["verdict"]})
            if len(verdicts) > 1:
                live = projections[um["id"]]["live"]
                if not live["needs_review"]:
                    live["needs_review"] = True
                live["needs_review_reasons"].append(
                    "umbrella_children_disagree:" + "|".join(verdicts))


def build_projections(plans, events, threshold, global_coverage=None):
    """Project `live`+`join` for every node across `plans`, including the umbrella
    children-disagreement review pass. When `global_coverage` is supplied, also
    attaches the diff-vs-blob finding per node (needed only for the shadow report).

    This is THE projection code path: the shadow run and check_closure_drift.py
    both call it, so a re-projection in the drift check is bit-identical to what
    the collapse tool stored (given the same event log)."""
    projections = {}
    for plan in plans:
        for node in plan["nodes"]:
            slc, tokens, prov = join_node(node, events)
            live, head = project_live(node, slc, threshold)
            join_bears_on = sorted({b for ev in slc for b in ev.bears_on})
            pr = {
                "live": live, "head": head, "slice": slc, "tokens": tokens,
                "prov": prov, "join_bears_on": join_bears_on,
                "plan_id": plan["plan_id"],
                # The node's EFFECTIVE input scope (node-level `scope_claims:` when
                # set, else the plan-level list -- load_plans already resolved it).
                # Carried here so stored_join_view() can build the whole stored join
                # from the projection alone, and so consumers stamp the node's own
                # scope rather than re-deriving (or mis-deriving) it.
                "node_scope_claims": list(node["scope_claims"]),
            }
            if global_coverage is not None:
                pr["diff"] = diff_blob(node, slc, global_coverage)
            projections[node["id"]] = pr
    _umbrella_children_disagree_pass(plans, projections)
    return projections


# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------


def write_history_sidecars(hist_dir, plans, projections, repo_root,
                           generated_note="Generated (SHADOW)"):
    """Write per-plan `<plan>_history.md` pointer-index sidecars (newest LAST).

    Shared by the SHP-1 read-only shadow run (`emit`) and the SHP-3 governance
    promoter (`promote_status_history.py`), so both produce byte-identical
    sidecars given the same projection -- ONE sidecar-generation path, mirroring
    the ONE-projection-path principle. `repo_root` computes the event-file link
    prefix relative to `hist_dir`, so the pointer links resolve whether the dir
    is the git-ignored `scratch/status_history_shadow/history/` tree or the
    committed `evidence/planning/status_history/history/` tree (different depths)."""
    os.makedirs(hist_dir, exist_ok=True)
    rel_root = os.path.relpath(repo_root, hist_dir)
    for plan in plans:
        lines = ["# History sidecar -- %s" % plan["plan_id"], "",
                 "> Pointer index into the append-only event log, **newest last**. "
                 "%s; never hand-edited, never re-pasted into the plan." % generated_note,
                 "", "Source plan: `%s`" % plan["file"], ""]
        for node in plan["nodes"]:
            pr = projections[node["id"]]
            lines.append("## `%s`" % node["id"])
            head_id = pr["live"]["from"]
            if not pr["slice"]:
                lines.append("\n_(no joined events)_\n")
                continue
            lines.append("")
            for ev in pr["slice"]:  # already chronological, newest last
                stamp = ev.ts.strftime("%Y-%m-%dT%H:%MZ") if ev.ts else "????-??-??"
                mark = " **<- live head**" if ev.eid == head_id else \
                       (" _(modifier)_" if ev.is_measurement() else "")
                link = os.path.join(rel_root, ev.source_path)
                lines.append("- `%s` [%s] `%s` -> [`%s`](%s) :: %s%s"
                             % (stamp, ev.kind, ev.eid, ev.source_path,
                                link, ev.summary, mark))
            lines.append("")
        with open(os.path.join(hist_dir, "%s_history.md" % plan["plan_id"]), "w") as f:
            f.write("\n".join(lines) + "\n")


def emit(out_dir, plans, projections, skipped, event_counts, threshold, now_iso,
         repo_root):
    os.makedirs(out_dir, exist_ok=True)
    hist_dir = os.path.join(out_dir, "history")
    os.makedirs(hist_dir, exist_ok=True)

    # ---- 1. status_head.shadow.yaml + .md (live: + join: per node) ----
    shadow = {"_meta": {
        "generated_utc": now_iso,
        "tool": "project_status_head.py (status_history_plane:SHP-1)",
        "read_only": True, "promotes": "NOTHING",
        "event_counts": event_counts, "brake_threshold": threshold,
        "skipped_plans": [{"file": f, "error": e} for f, e in skipped],
    }, "plans": []}
    md = ["# Shadow status heads -- status_history_plane:SHP-1",
          "",
          "> READ-ONLY projection. PROMOTES/DEMOTES NOTHING. Written by "
          "`scripts/project_status_head.py`; edits no `*_plan.md`.",
          "",
          "Generated %s. Events: %s. Brake threshold: %d."
          % (now_iso, ", ".join("%s=%d" % kv for kv in sorted(event_counts.items())), threshold),
          ""]
    if skipped:
        md.append("**Skipped plans (YAML parse error):** "
                  + ", ".join(f for f, _ in skipped) + "\n")

    review_ct = 0
    for plan in plans:
        pblock = {"plan_id": plan["plan_id"], "file": plan["file"], "nodes": []}
        md.append("## %s\n" % plan["plan_id"])
        md.append("`%s`\n" % plan["file"])
        for node in plan["nodes"]:
            pr = projections[node["id"]]
            live = pr["live"]
            if live["needs_review"]:
                review_ct += 1
            join_block = {
                "bears_on": pr["join_bears_on"],
                "scope_claims": node["scope_claims"],
                "tokens": sorted(pr["tokens"]),
                "slice_event_ids": [e.eid for e in pr["slice"]],
            }
            pblock["nodes"].append({
                "id": node["id"], "status": node["status"],
                "severity": node["severity"], "live": live, "join": join_block,
            })
            flags = []
            if live["needs_review"]:
                flags.append("**NEEDS_REVIEW**")
            if live["no_events"]:
                flags.append("_no-events_")
            elif not live["head_forward"]:
                flags.append("_non-forward-head_")
            md.append("### `%s`%s\n" % (node["id"], (" " + " ".join(flags)) if flags else ""))
            md.append("```yaml")
            md.append("live:")
            md.append("  as_of: %s" % live["as_of"])
            md.append("  from: %s" % live["from"])
            md.append("  head_kind: %s" % live["head_kind"])
            md.append("  head_forward: %s" % str(live["head_forward"]).lower())
            md.append("  verdict: %s" % live["verdict"])
            md.append("  brake: %s          # %d substrate_ceiling / threshold %d"
                      % (live["brake"], live["brake_count"], live["brake_threshold"]))
            md.append("  needs_review: %s%s" % (
                str(live["needs_review"]).lower(),
                ("   # " + "; ".join(live["needs_review_reasons"]))
                if live["needs_review_reasons"] else ""))
            nxt = (live["next"] or "").replace("\n", " ")
            md.append("  next: %s" % (nxt if len(nxt) <= 240 else nxt[:237] + "..."))
            md.append("join:")
            md.append("  bears_on: %s" % json.dumps(pr["join_bears_on"]))
            md.append("  scope_claims: %s" % json.dumps(node["scope_claims"]))
            md.append("  slice_size: %d  (forward=%d)"
                      % (live["slice_size"], live["forward_events"]))
            md.append("```\n")
        shadow["plans"].append(pblock)

    with open(os.path.join(out_dir, "status_head.shadow.yaml"), "w") as f:
        yaml.safe_dump(shadow, f, sort_keys=False, width=120, allow_unicode=True)
    with open(os.path.join(out_dir, "status_head.shadow.md"), "w") as f:
        f.write("\n".join(md) + "\n")

    # ---- 2. per-plan *_history.md sidecars (pointer index, newest LAST) ----
    write_history_sidecars(hist_dir, plans, projections, repo_root)

    # ---- 3. diff-vs-blob report (SHP-2 input) ----
    dl = ["# Diff-vs-blob report -- status_history_plane:SHP-1 -> SHP-2 input", "",
          "> The non-destructive migration razor (design sec 5). For each hand-written "
          "`phase:` / `owner_exq:` / `awaiting:` blob, this diffs its content against the "
          "structured events in the node's join slice.", "",
          "Legend:",
          "- **at_risk** -- a reference named in the blob that appears in **NO** event "
          "(autopsy/manifest/decision). These are the *history bits at risk*: lift them into "
          "the log BEFORE SHP-2 collapses the blob.",
          "- **join_gap** -- a reference that exists as an event elsewhere but did not join "
          "this node (fix the join, not a lost bit).",
          "- **residual_sentences** -- blob sentences with no covered event anchor at all "
          "(candidate free-standing reconciliations written straight into the plan).", "",
          "Generated %s.\n" % now_iso]
    total_at_risk = 0
    for plan in plans:
        plan_has = any(projections[n["id"]]["diff"] for n in plan["nodes"])
        if not plan_has:
            continue
        dl.append("## %s (`%s`)\n" % (plan["plan_id"], plan["file"]))
        for node in plan["nodes"]:
            diff = projections[node["id"]]["diff"]
            if not diff:
                continue
            node_at_risk = sum(len(v["at_risk"]) for v in diff.values())
            node_resid = sum(len(v["residual_sentences"]) for v in diff.values())
            if node_at_risk == 0 and node_resid == 0:
                continue
            dl.append("### `%s`  (at_risk=%d, residual_sentences=%d)\n"
                      % (node["id"], node_at_risk, node_resid))
            for field, v in diff.items():
                if not v["at_risk"] and not v["residual_sentences"] and not v["join_gap"]:
                    continue
                dl.append("- **%s:**" % field)
                if v["at_risk"]:
                    total_at_risk += len(v["at_risk"])
                    dl.append("    - at_risk: %s"
                              % ", ".join("%s(%s)" % (r["token"], r["kind"]) for r in v["at_risk"]))
                if v["join_gap"]:
                    dl.append("    - join_gap: %s"
                              % ", ".join("%s(%s)" % (r["token"], r["kind"]) for r in v["join_gap"]))
                for s in v["residual_sentences"]:
                    dl.append("    - residual: %s" % s)
            dl.append("")
    dl.insert(len(dl) and 9 or 0,
              "**Total at-risk references across all nodes: %d.**\n" % total_at_risk)
    with open(os.path.join(out_dir, "diff_vs_blob.md"), "w") as f:
        f.write("\n".join(dl) + "\n")

    return review_ct, total_at_risk


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(here)  # scripts/ -> repo root
    ap = argparse.ArgumentParser(description="SHP-1 shadow status-head projector (read-only).")
    ap.add_argument("--repo-root", default=repo_root,
                    help="REE_assembly repo root (default: parent of this script's dir)")
    ap.add_argument("--out", default=None,
                    help="Shadow output dir (default: <repo>/scratch/status_history_shadow)")
    ap.add_argument("--threshold", type=int, default=DEFAULT_BRAKE_THRESHOLD,
                    help="substrate_ceiling count at/above which the brake is fired")
    ap.add_argument("--node", default=None,
                    help="Only project nodes whose id contains this substring (debug)")
    args = ap.parse_args()

    repo_root = os.path.abspath(args.repo_root)
    out_dir = args.out or os.path.join(repo_root, "scratch", "status_history_shadow")
    planning_dir = os.path.join(repo_root, "evidence", "planning")
    now_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    plans, skipped = load_plans(planning_dir)
    events, event_counts = load_events(repo_root)
    autopsies = event_counts["autopsy"]
    manifests = event_counts["manifest_PASS"]
    decisions = event_counts["decision"]

    global_coverage = set()
    for ev in events:
        global_coverage |= ev.ref_tokens

    if args.node:
        for plan in plans:
            plan["nodes"] = [n for n in plan["nodes"] if args.node in n["id"]]
        plans = [p for p in plans if p["nodes"]]

    projections = build_projections(plans, events, args.threshold, global_coverage)

    review_ct, total_at_risk = emit(out_dir, plans, projections, skipped,
                                    event_counts, args.threshold, now_iso, repo_root)

    n_nodes = sum(len(p["nodes"]) for p in plans)
    no_events = sum(1 for pr in projections.values() if pr["live"]["no_events"])
    non_forward = sum(1 for pr in projections.values()
                      if not pr["live"]["no_events"] and not pr["live"]["head_forward"])
    print("project_status_head.py (SHP-1, READ-ONLY) -- wrote shadow output to:")
    print("  %s" % out_dir)
    print("  plans=%d nodes=%d  events: autopsy=%d manifest_PASS=%d decision=%d"
          % (len(plans), n_nodes, autopsies, manifests, decisions))
    print("  needs_review(ambiguous head)=%d   no_events=%d   non_forward_head=%d"
          % (review_ct, no_events, non_forward))
    print("  at-risk history refs (diff-vs-blob)=%d" % total_at_risk)
    if skipped:
        print("  skipped plans (YAML parse): %s" % ", ".join(f for f, _ in skipped))
    print("  PROMOTES/DEMOTES NOTHING; no *_plan.md edited.")


if __name__ == "__main__":
    main()
