#!/usr/bin/env python3
"""Tests for scripts/token_split_measure.py -- focused on the WI-I prompt-cache section.

The OLS split predates these tests and is validated by its own per-turn R^2
diagnostic against real transcripts. What is tested here is the part that is new
and arithmetically checkable against a hand-computed fixture: the prompt-cache
counters, and the fact that the pre-WI-I report lines still print.

The fixture is a synthetic 3-turn transcript whose usage blocks are chosen so
every derived cache figure has a closed form (see EXPECTED below).

Run: /opt/local/bin/python3 -m pytest scripts/test_token_split_measure.py -q
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, "token_split_measure.py")

_spec = importlib.util.spec_from_file_location("token_split_measure", TARGET)
tsm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tsm)


# --- fixture -----------------------------------------------------------------
# Conversation chars are laid out so cumulative-chars-before-turn is exactly
# 4000 / 8000 / 12000, and the usage totals are exactly 10000 + chars/4. So the
# OLS fit must recover baseline=10000 and chars_per_token=4.0 with R^2 == 1.
#
# Usage blocks (billed input = input + cache_read + cache_creation):
#   turn 1  input  1,000 + creation 10,000 + read      0  = 11,000  (cold start)
#   turn 2  input    100 + creation      0 + read 11,900  = 12,000  (warm hit)
#   turn 3  input 13,000 + creation      0 + read      0  = 13,000  (MISS)
USAGE = [
    {"input_tokens": 1000, "cache_creation_input_tokens": 10000,
     "cache_read_input_tokens": 0, "output_tokens": 50},
    {"input_tokens": 100, "cache_creation_input_tokens": 0,
     "cache_read_input_tokens": 11900, "output_tokens": 50},
    {"input_tokens": 13000, "cache_creation_input_tokens": 0,
     "cache_read_input_tokens": 0, "output_tokens": 50},
]
EXPECTED = {
    "billed": 36000,
    "read": 11900,
    "creation": 10000,
    "fresh": 14100,
    "read_share": 11900 / 36000.0,
    "creation_share": 10000 / 36000.0,
    "turn_shares": [0.0, 11900 / 12000.0, 0.0],
    "misses": 1,              # turn 3 only -- turn 1 is never a miss
    "considered": 2,          # turns 2 and 3
    "median_turn_share": 0.0,
}


def write_fixture(path, ts="2026-09-10T12:00:00.000Z", prefix=()):
    """3 assistant turns, each preceded by a user message sized to hit 4000/8000/12000.

    `prefix` records are written first (e.g. baseline-restating attachments)."""
    recs = list(prefix)
    # Each assistant record contributes 2 chars ("ok"), so user blocks are
    # 4000, 3998, 3998 to land the cumulative counter on exact multiples.
    for i, (pad, u) in enumerate(zip([4000, 3998, 3998], USAGE)):
        recs.append({"type": "user", "timestamp": ts,
                     "message": {"role": "user", "content": "u" * pad}})
        recs.append({"type": "assistant", "timestamp": ts, "entrypoint": "cli",
                     "message": {"role": "assistant", "usage": u,
                                 "content": [{"type": "text", "text": "ok"}]}})
    with open(path, "w") as fh:
        for r in recs:
            fh.write(json.dumps(r) + "\n")
    return path


def analyzed():
    d = tempfile.mkdtemp()
    return tsm.analyze(write_fixture(os.path.join(d, "s.jsonl")))


# --- the fixture itself is only useful if the pre-existing fit still works ----
def test_fit_recovers_the_planted_baseline():
    r = analyzed()
    assert r is not None, "fixture must produce a usable fit"
    assert r["n_turns"] == 3
    assert abs(r["baseline_tokens"] - 10000) < 1e-6
    assert abs(r["chars_per_token"] - 4.0) < 1e-9
    assert r["r2"] is None or r["r2"] > 0.999999
    assert r["billed_total_measured"] == EXPECTED["billed"]


# --- baseline double-count (plan section 7.1) ----------------------------------
# Since 2026-09-02 the baseline B is also written into the transcript as attachments.
# A 150,000-char `instructions` record counted as conversation shifts the intercept by
# -150000/4 = -37,500 -> negative baseline -> session rejected. Excluded, the planted
# fit must come back exactly.
BASELINE_PREFIX = [
    {"type": "attachment", "timestamp": "2026-09-10T12:00:00.000Z",
     "attachment": {"type": "instructions", "content": "c" * 150000}},
    {"type": "attachment", "timestamp": "2026-09-10T12:00:00.000Z",
     "attachment": {"type": "prompt_snapshot", "content": "p" * 90000}},
]


def test_baseline_attachments_do_not_double_count_b():
    d = tempfile.mkdtemp()
    r = tsm.analyze(write_fixture(os.path.join(d, "s.jsonl"), prefix=BASELINE_PREFIX))
    assert r is not None and r["fitted"], "baseline attachments must not reject the fit"
    assert abs(r["baseline_tokens"] - 10000) < 1e-6
    assert abs(r["chars_per_token"] - 4.0) < 1e-9
    assert r["billed_cat"]["attachment"] == 0


def test_categorize_excludes_every_baseline_type_but_keeps_real_injections():
    for t in tsm.BASELINE_ATTACHMENT_TYPES:
        assert tsm.categorize({"type": "attachment", "attachment": {"type": t, "x": "y"}}) == []
    nm = {"type": "attachment", "attachment": {"type": "nested_memory", "content": "z" * 50}}
    got = tsm.categorize(nm)
    assert len(got) == 1 and got[0][0] == "attachment" and got[0][1] > 50


# --- WI-I: prompt-cache counters ---------------------------------------------
def test_cache_token_totals():
    r = analyzed()
    assert r["cache_read_tokens"] == EXPECTED["read"]
    assert r["cache_creation_tokens"] == EXPECTED["creation"]
    assert r["fresh_input_tokens"] == EXPECTED["fresh"]
    # The three must partition the same denominator the split above uses.
    assert (r["cache_read_tokens"] + r["cache_creation_tokens"]
            + r["fresh_input_tokens"]) == r["billed_total_measured"]


def test_cache_shares():
    r = analyzed()
    assert abs(r["cache_read_share"] - EXPECTED["read_share"]) < 1e-12
    assert abs(r["cache_creation_share"] - EXPECTED["creation_share"]) < 1e-12


def test_per_turn_shares_in_order():
    r = analyzed()
    got = r["turn_cache_read_share"]
    assert len(got) == 3
    for a, b in zip(got, EXPECTED["turn_shares"]):
        assert abs(a - b) < 1e-12
    assert abs(r["med_turn_cache_read_share"] - EXPECTED["median_turn_share"]) < 1e-12


def test_first_turn_is_never_counted_as_a_miss():
    """Turn 1 has nothing to hit -- counting it would report a 100% miss floor."""
    r = analyzed()
    assert r["cache_misses"] == EXPECTED["misses"]
    assert r["cache_miss_turns_considered"] == EXPECTED["considered"]
    # Guard the semantics explicitly: turn 1 read 0 tokens and is still not a miss.
    assert r["turn_cache_read_share"][0] == 0.0
    assert r["cache_misses"] < len([s for s in r["turn_cache_read_share"] if s == 0.0])


def test_all_hits_reports_zero_misses():
    d = tempfile.mkdtemp()
    p = os.path.join(d, "s.jsonl")
    saved = [dict(u) for u in USAGE]
    try:
        USAGE[2].update({"input_tokens": 100, "cache_read_input_tokens": 12900})
        write_fixture(p)
        r = tsm.analyze(p)
        assert r["cache_misses"] == 0
        assert r["cache_miss_turns_considered"] == 2
    finally:
        for u, s in zip(USAGE, saved):
            u.clear()
            u.update(s)


# --- end-to-end --report ------------------------------------------------------
def write_unfittable_substrate_reader(path, ts="2026-09-10T12:00:00.000Z"):
    """2 assistant turns (< 3, so the fit rejects it) that read a docs/substrate/ file."""
    recs = []
    for i in range(2):
        recs.append({"type": "user", "timestamp": ts,
                     "message": {"role": "user", "content": "u" * 100}})
        recs.append({"type": "assistant", "timestamp": ts, "entrypoint": "cli",
                     "message": {"role": "assistant",
                                 "usage": {"input_tokens": 5000, "output_tokens": 5},
                                 "content": [{"type": "tool_use", "name": "Read", "input": {
                                     "file_path": "/x/ree-v3/docs/substrate/SD-001.md"}}]}})
    with open(path, "w") as fh:
        for r in recs:
            fh.write(json.dumps(r) + "\n")
    return path


def _report(extra=(), unfittable=False):
    """Run the real script against a fake HOME holding one fixture transcript."""
    home = tempfile.mkdtemp()
    proj = os.path.join(home, ".claude", "projects", "-Users-dgolden-REE-Working")
    os.makedirs(proj)
    write_fixture(os.path.join(proj, "sess.jsonl"))
    if unfittable:
        write_unfittable_substrate_reader(os.path.join(proj, "unfit.jsonl"))
    env = dict(os.environ, HOME=home)
    env.pop("USERPROFILE", None)
    p = subprocess.run([sys.executable, TARGET, "--report", "--min-bytes", "0"]
                       + list(extra),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env,
                       timeout=120)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def test_report_prints_the_cache_section_with_the_right_numbers():
    rc, out, err = _report()
    assert rc == 0, err
    assert "--- PROMPT CACHE (realized) ---" in out
    assert "cache READ      33.06%" in out
    assert "cache CREATION  27.78%" in out
    assert "uncached input  39.17%" in out
    assert "MISSES (cache_read == 0 on a non-first turn): 1 of 2 turns  (50.00%)" in out
    assert "sessions with >=1 miss: 1/1" in out


def test_report_keeps_every_pre_wi_i_line():
    """WI-I is ADD-only: the 2026-09-14T08:00Z re-measure ran the pre-WI-I script
    and its output must stay diffable against this one."""
    rc, out, _ = _report()
    assert rc == 0
    for line in ["TOKEN-SPLIT MEASUREMENT",
                 "FIT QUALITY -- per-turn, NOT summed (see docstring):",
                 "--- share of billed INPUT tokens ---",
                 "--- nested_memory injections (the WI-1 target) ---",
                 "--- NEGATIVE CONTROL: read-back of split-out per-feature files ---",
                 "FIXED PROMPT (sys+CLAUDE.md+skills+tool defs)"]:
        assert line in out, "pre-WI-I line missing: %r" % line
    # ...and the cache block must not have displaced the split block's ordering.
    assert out.index("--- share of billed INPUT tokens ---") \
        < out.index("--- PROMPT CACHE (realized) ---") \
        < out.index("--- nested_memory injections (the WI-1 target) ---")


def test_since_filter_applies_to_the_cache_section():
    rc, out, _ = _report(["--since", "2026-12-01"])
    assert rc == 1                                  # no sessions matched
    assert "No sessions matched" in out
    assert "PROMPT CACHE" not in out
    rc, out, _ = _report(["--since", "2026-09-01"])
    assert rc == 0
    assert "--- PROMPT CACHE (realized) ---" in out


def test_unfitted_session_still_returns_its_fit_free_observations():
    d = tempfile.mkdtemp()
    r = tsm.analyze(write_unfittable_substrate_reader(os.path.join(d, "u.jsonl")))
    assert r is not None and r["fitted"] is False
    assert r["substrate_reads"] == 2
    assert r["read_via_tool"] == []   # no CLAUDE.md Read in this fixture


# --- Read-channel CLAUDE.md loads (chip-20260914-token-split-read-channel-count) ---
def _read_tool_use(tool_use_id, file_path):
    return {"type": "tool_use", "id": tool_use_id, "name": "Read",
            "input": {"file_path": file_path}}


def _read_tool_result(tool_use_id, is_error=False):
    return {"type": "tool_result", "tool_use_id": tool_use_id, "is_error": is_error}


def write_claude_read_fixture(path, ts="2026-09-10T12:00:00.000Z",
                              file_path="/Users/dgolden/REE_Working/ree-v3/CLAUDE.md",
                              is_error=False, is_sidechain=False, no_result=False):
    """< 3 turns on purpose (unfitted) -- isolates the Read-channel fields from the OLS fit."""
    tuid = "toolu_fixture001"
    recs = [
        {"type": "user", "timestamp": ts, "isSidechain": is_sidechain,
         "message": {"role": "user", "content": "read the CLAUDE.md please"}},
        {"type": "assistant", "timestamp": ts, "entrypoint": "cli", "isSidechain": is_sidechain,
         "message": {"role": "assistant", "usage": {"input_tokens": 100, "output_tokens": 5},
                     "content": [_read_tool_use(tuid, file_path)]}},
    ]
    if not no_result:
        recs.append({"type": "user", "timestamp": ts, "isSidechain": is_sidechain,
                     "message": {"role": "user", "content": [_read_tool_result(tuid, is_error)]}})
    with open(path, "w") as fh:
        for r in recs:
            fh.write(json.dumps(r) + "\n")
    return path


def test_successful_claude_md_read_is_counted():
    d = tempfile.mkdtemp()
    r = tsm.analyze(write_claude_read_fixture(os.path.join(d, "r.jsonl")))
    assert r is not None and r["fitted"] is False   # 2 turns, below the fit floor
    assert r["read_via_tool"] == ["ree-v3/CLAUDE.md"]


def test_errored_read_is_not_counted():
    d = tempfile.mkdtemp()
    r = tsm.analyze(write_claude_read_fixture(os.path.join(d, "r.jsonl"), is_error=True))
    assert r["read_via_tool"] == []


def test_sidechain_read_is_not_counted():
    """A subagent's own Read is not this session's main-thread context loading."""
    d = tempfile.mkdtemp()
    r = tsm.analyze(write_claude_read_fixture(os.path.join(d, "r.jsonl"), is_sidechain=True))
    assert r["read_via_tool"] == []


def test_read_with_no_paired_result_is_not_counted():
    """Guards against a false positive if the tool_use is issued but never resolves
    (e.g. a truncated transcript) -- only a PAIRED, successful result counts."""
    d = tempfile.mkdtemp()
    r = tsm.analyze(write_claude_read_fixture(os.path.join(d, "r.jsonl"), no_result=True))
    assert r["read_via_tool"] == []


def test_non_claude_md_read_is_not_counted():
    d = tempfile.mkdtemp()
    r = tsm.analyze(write_claude_read_fixture(
        os.path.join(d, "r.jsonl"), file_path="/Users/dgolden/REE_Working/ree-v3/ree_core/agent.py"))
    assert r["read_via_tool"] == []


def _report_with_read_and_nested(min_bytes=0):
    """A fitted 3-turn session that ALSO Reads REE_assembly/CLAUDE.md (no nested_memory
    for it), plus the standard nested-memory-injecting fixture, so both channels and
    their union are exercised in one --report run."""
    home = tempfile.mkdtemp()
    proj = os.path.join(home, ".claude", "projects", "-Users-dgolden-REE-Working")
    os.makedirs(proj)
    ts = "2026-09-10T12:00:00.000Z"
    tuid = "toolu_readfixture"
    recs = []
    for i, (pad, u) in enumerate(zip([4000, 3998, 3998], USAGE)):
        content = [{"type": "text", "text": "ok"}]
        if i == 0:
            content = [_read_tool_use(tuid, "/Users/dgolden/REE_Working/REE_assembly/CLAUDE.md")]
        recs.append({"type": "user", "timestamp": ts, "message": {"role": "user", "content": "u" * pad}})
        recs.append({"type": "assistant", "timestamp": ts, "entrypoint": "cli",
                     "message": {"role": "assistant", "usage": u, "content": content}})
        if i == 0:
            recs.append({"type": "user", "timestamp": ts,
                        "message": {"role": "user", "content": [_read_tool_result(tuid)]}})
    with open(os.path.join(proj, "readsess.jsonl"), "w") as fh:
        for r in recs:
            fh.write(json.dumps(r) + "\n")
    nested_attach = {"type": "attachment", "timestamp": ts,
                     "attachment": {"type": "nested_memory",
                                    "path": "/Users/dgolden/REE_Working/ree-v3/CLAUDE.md",
                                    "content": "z" * 5000}}
    write_fixture(os.path.join(proj, "nestedsess.jsonl"), prefix=[nested_attach])
    env = dict(os.environ, HOME=home)
    env.pop("USERPROFILE", None)
    p = subprocess.run([sys.executable, TARGET, "--report", "--min-bytes", str(min_bytes)],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, timeout=120)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def test_report_prints_read_channel_section_with_nested_and_read_and_union():
    rc, out, err = _report_with_read_and_nested()
    assert rc == 0, err
    assert "--- Read-channel CLAUDE.md loads (chip-20260914-token-split-read-channel-count) ---" in out
    # REE_assembly/CLAUDE.md: Read only (no nested_memory attachment in this fixture).
    assert "REE_assembly/CLAUDE.md" in out
    # ree-v3/CLAUDE.md: nested_memory only (no Read in this fixture).
    assert "ree-v3/CLAUDE.md" in out
    # Relative-path resolution depends on a real ~/REE_Working prefix match, which this
    # test's fake HOME cannot provide -- match on the trailing repo-relative substring
    # rather than a line prefix (production, with a real HOME, prints the clean path).
    assembly_line = [l for l in out.splitlines()
                     if "REE_assembly/CLAUDE.md" in l and "nested_memory=" in l][0]
    assert "nested_memory=  0" in assembly_line and "read=  1" in assembly_line and "union=  1" in assembly_line
    ree_v3_line = [l for l in out.splitlines()
                   if "ree-v3/CLAUDE.md" in l and "nested_memory=" in l][0]
    assert "nested_memory=  1" in ree_v3_line and "read=  0" in ree_v3_line and "union=  1" in ree_v3_line
    # section stays before the negative control, matching the doc-required ordering.
    assert out.index("--- Read-channel CLAUDE.md loads") < out.index("--- NEGATIVE CONTROL")


def test_negative_control_covers_unfitted_sessions():
    """Scoped to fitted sessions it printed a vacuous 0/18 (plan section 7.3)."""
    rc, out, _ = _report(unfittable=True)
    assert rc == 0
    assert "sessions 1 (of 2 candidates)" in out          # the split still uses fitted only
    assert "sessions referencing docs/substrate/: 1/2" in out


def test_report_output_is_ascii():
    """CLAUDE.md: anything reaching stdout from a .py file must be ASCII."""
    rc, out, _ = _report()
    assert rc == 0
    out.encode("ascii")


if __name__ == "__main__":
    sys.exit(subprocess.call([sys.executable, "-m", "pytest", __file__, "-q"]))
