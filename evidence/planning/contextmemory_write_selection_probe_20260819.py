#!/usr/bin/env python3
"""Independent probe: ContextMemory write-address degeneracy, landed vs salvaged.

chip-20260819-contextmemory-writesel-verify-measurement

WHAT THIS ANSWERS
-----------------
Is the LANDED usage-penalty write-selection (ree-v3 76cbf844,
E1Config.contextmemory_write_usage_balancing) worse on write-address
degeneracy / content-conditioning than the SALVAGED four-mode implementation
(ree-v3 stash dd4b0a4 == tag stash-archive/20260819-dd4b0a4)?

The salvaged branch's own notes
(REE_assembly/docs/architecture/contextmemory_write_address_selection.md,
untracked as of 2026-08-19) assert that a `usage` rule reaches occupancy by
going CONTENT-BLIND. That table's rows are `argmin` / `refractory` / `usage` /
`gumbel` -- all four from the salvaged branch, whose base f7a6e9c PREDATES
76cbf844. It therefore never measured the landed rule at all. The two `usage`
rules are DIFFERENT algorithms:

  landed    (76cbf844): argmin( mean_scores + w * usage_ema * sqrt(memory_dim) )
  salvaged  (dd4b0a4):  argmax( -z(mean_scores) - w * z(usage_ema) )

This probe scores BOTH, plus the legacy default and the salvaged refractory /
gumbel arms, under ONE instrumentation, at matched seeds and matched streams.

INSTRUMENTATION -- deliberately implementation-independent
----------------------------------------------------------
The written slot is recovered by DIFFING `memory` across the write (exactly one
row is blended), never by re-deriving the selection expression. The salvaged
doc's own "Instrumentation change" section warns that V3-EXQ-436f's tracker
re-derived `scores.mean(0).argmin()` and so silently reports the wrong slot the
moment the rule changes. Diffing cannot be wrong in that way, and -- the reason
it is used here rather than the salvaged `last_write_index` property -- it is
the SAME instrument on both implementations, where `last_write_index` exists
only on one of them and would make the arms non-comparable.

STREAMS / OPERATING POINT
-------------------------
Reproduced verbatim from the salvaged contract's `_stream` helper so the
comparison lands on the same operating point it claims (state rms 0.078,
jitter 0.0078, latent 64, memory_dim 128, num_slots 16, gated_content_write).
clusters=1 is the near-constant stream that triggers the lock; clusters=2 is
the varied stream on which context-conditioning is measurable.

PRE-REGISTERED METRICS (defined before any run; see the doc for the record)
---------------------------------------------------------------------------
Degenerate stream (clusters=1):
  D1 n_distinct        distinct write addresses used (primary degeneracy DV)
  D2 entropy_bits      Shannon entropy of the write-count distribution, bits
                       (max = log2(16) = 4.0; a locked bank = 0.0)
  D3 self_repeat       fraction of writes landing on the same slot as the
                       immediately preceding write (collision/overwrite rate)
  D4 herfindahl        sum p_i^2 over write shares (1.0 = fully locked)
2-context stream (clusters=2):
  C1 jaccard           |S0 & S1| / |S0 | S1| over per-context slot sets.
                       LOWER = more context-conditioned.
  C2 occ_cos           mean pairwise cosine similarity among occupied slot
                       vectors. LOWER = more differentiated. This is the DV
                       SD-017 / ARC-045 / MECH-166 turn on.

PRE-REGISTERED DECISION RULES
-----------------------------
R4 (validity gate, negative control). `argmin_legacy` must reproduce the
   documented lock: exactly 3/5 seeds with >= 2 slots on the degenerate stream.
   If not, the operating point has drifted and every other row is void.
R0 (base-identity control). `argmin_legacy` (main) and `salvaged_argmin` must
   produce an identical slot sequence AND identical final memory. If not, the
   two module copies are not the same base and the comparison is void.
R1 (does the landed fix work?). `landed_usage_balancing` must reach >= 2
   occupied slots on >= 4/5 seeds. FAIL => the landed fix does not fix the
   registered defect => reconciliation justified regardless of R2.
R2 (is the landed fix content-blind?). mean C1(landed) - mean C1(refractory)
   > 0.25 => landed is materially more content-blind => reconciliation
   justified. The 0.25 margin is NOT chosen here: it is the salvaged
   contract's own pre-existing materiality margin in
   test_refractory_preserves_content_conditioning.
R3 (secondary, descriptive, no threshold). C2 across arms, reported with
   Cohen's d over the 5 seeds.

Disposition mapping: R1 pass AND R2 not triggered => the landed implementation
is adequate, keep it. R1 fail OR R2 triggered => reconciliation justified.

Run:  /opt/local/bin/python3 contextmemory_write_selection_probe_20260819.py
Deps: ree-v3 checkout at REE_WORKING/ree-v3 with the salvaged commit object
      dd4b0a4 reachable (tag stash-archive/20260819-dd4b0a4; LOCAL-ONLY on
      DLAPTOP -- a stash archive tag is not pushed).
"""

import json
import math
import os
import subprocess
import sys
import types

BASE = os.environ.get("REE_WORKING_ROOT", "/Users/dgolden/REE_Working")
REE_V3 = os.path.join(BASE, "ree-v3")
SALVAGED_REF = os.environ.get("REE_CM_SALVAGED_REF", "dd4b0a4")

sys.path.insert(0, REE_V3)

import torch  # noqa: E402

from ree_core.predictors.e1_deep import ContextMemory as MainContextMemory  # noqa: E402

LATENT_DIM, MEMORY_DIM, NUM_SLOTS = 64, 128, 16
SEEDS = (0, 7, 13, 42, 100)
LOCKING_SEEDS = (0, 100)


def load_salvaged_context_memory():
    """Exec the salvaged e1_deep.py from the git object, without touching disk.

    No temp file and no sys.path mutation: CLAUDE.md's `sys.path[0]` shadowing
    hazard cannot arise, and nothing is left behind to be committed by accident.
    """
    src = subprocess.check_output(
        ["git", "-C", REE_V3, "show", "%s:ree_core/predictors/e1_deep.py" % SALVAGED_REF],
        text=True,
    )
    mod = types.ModuleType("e1_deep_salvaged_probe")
    mod.__dict__["__file__"] = "<%s:ree_core/predictors/e1_deep.py>" % SALVAGED_REF
    exec(compile(src, mod.__dict__["__file__"], "exec"), mod.__dict__)
    return mod.ContextMemory


def stream(seed, n, jitter=0.0078, clusters=1):
    """Verbatim from the salvaged contract's _stream()."""
    gen = torch.Generator().manual_seed(seed)
    bases = [torch.randn(1, LATENT_DIM, generator=gen) * 0.078 for _ in range(clusters)]
    return [
        (i % clusters,
         bases[i % clusters] + torch.randn(1, LATENT_DIM, generator=gen) * jitter)
        for i in range(n)
    ]


def run_arm(cm_cls, seed, n, clusters, **kwargs):
    """Drive one ContextMemory over one stream; recover slots by memory-diff."""
    torch.manual_seed(seed)
    cm = cm_cls(LATENT_DIM, MEMORY_DIM, NUM_SLOTS, gated_content_write=True, **kwargs)
    seq = []
    per_cluster = {}
    for cid, state in stream(seed, n, clusters=clusters):
        before = cm.memory.data.clone()
        cm.write(state)
        delta = (cm.memory.data - before).abs().sum(dim=1)
        idx = int(delta.argmax()) if float(delta.max()) > 0.0 else None
        seq.append(idx)
        if idx is not None:
            per_cluster.setdefault(cid, set()).add(idx)
    return cm, seq, per_cluster


def entropy_bits(seq):
    counts = {}
    for i in seq:
        if i is not None:
            counts[i] = counts.get(i, 0) + 1
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def herfindahl(seq):
    counts = {}
    for i in seq:
        if i is not None:
            counts[i] = counts.get(i, 0) + 1
    total = sum(counts.values())
    if total == 0:
        return 1.0
    return sum((c / total) ** 2 for c in counts.values())


def self_repeat(seq):
    pairs = [(a, b) for a, b in zip(seq, seq[1:]) if a is not None and b is not None]
    if not pairs:
        return float("nan")
    return sum(1 for a, b in pairs if a == b) / len(pairs)


def occupied_cosine(cm, occupied):
    """Mean pairwise cosine similarity among occupied slot vectors."""
    idx = sorted(occupied)
    if len(idx) < 2:
        return float("nan")
    m = cm.memory.data[idx]
    m = m / m.norm(dim=1, keepdim=True).clamp_min(1e-12)
    sim = m @ m.t()
    n = len(idx)
    off = (sim.sum() - sim.diag().sum()) / (n * (n - 1))
    return float(off)


def cohens_d(a, b):
    a = [x for x in a if not math.isnan(x)]
    b = [x for x in b if not math.isnan(x)]
    if len(a) < 2 or len(b) < 2:
        return float("nan")
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    va = sum((x - ma) ** 2 for x in a) / (len(a) - 1)
    vb = sum((x - mb) ** 2 for x in b) / (len(b) - 1)
    sp = math.sqrt(((len(a) - 1) * va + (len(b) - 1) * vb) / (len(a) + len(b) - 2))
    return (ma - mb) / sp if sp > 0 else float("nan")


def main():
    Salvaged = load_salvaged_context_memory()

    arms = [
        ("argmin_legacy", MainContextMemory, {}),
        ("landed_usage_balancing", MainContextMemory, {"write_usage_balancing": True}),
        ("salvaged_argmin", Salvaged, {"write_selection": "argmin"}),
        ("salvaged_refractory_k2", Salvaged,
         {"write_selection": "refractory", "write_refractory_k": 2}),
        ("salvaged_usage", Salvaged, {"write_selection": "usage"}),
        ("salvaged_gumbel", Salvaged, {"write_selection": "gumbel"}),
    ]

    results = {}
    for n_writes in (1500, 3000):
        for name, cls, kw in arms:
            for seed in SEEDS:
                cm1, seq1, _ = run_arm(cls, seed, n_writes, 1, **kw)
                occ1 = {i for i in seq1 if i is not None}
                cm2, seq2, per2 = run_arm(cls, seed, n_writes, 2, **kw)
                occ2 = {i for i in seq2 if i is not None}
                s0, s1 = per2.get(0, set()), per2.get(1, set())
                results[(n_writes, name, seed)] = {
                    "n_distinct": len(occ1),
                    "entropy_bits": entropy_bits(seq1),
                    "self_repeat": self_repeat(seq1),
                    "herfindahl": herfindahl(seq1),
                    "occ_cos_degenerate": occupied_cosine(cm1, occ1),
                    "n_distinct_2ctx": len(occ2),
                    "jaccard": len(s0 & s1) / max(len(s0 | s1), 1),
                    "occ_cos": occupied_cosine(cm2, occ2),
                    "final_mem_hash": hash(tuple(
                        round(float(v), 9) for v in cm1.memory.data.flatten()[:64])),
                    "slot_seq_head": seq1[:40],
                }

    # ---- R0 base-identity control -------------------------------------------
    r0_ok = True
    for n_writes in (1500, 3000):
        for seed in SEEDS:
            a = results[(n_writes, "argmin_legacy", seed)]
            b = results[(n_writes, "salvaged_argmin", seed)]
            if a["slot_seq_head"] != b["slot_seq_head"] or \
               a["final_mem_hash"] != b["final_mem_hash"] or \
               a["n_distinct"] != b["n_distinct"]:
                r0_ok = False

    out = {
        "generated_utc": subprocess.check_output(
            ["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip(),
        "ree_v3_head": subprocess.check_output(
            ["git", "-C", REE_V3, "rev-parse", "HEAD"], text=True).strip(),
        "salvaged_ref": subprocess.check_output(
            ["git", "-C", REE_V3, "rev-parse", SALVAGED_REF], text=True).strip(),
        "torch": torch.__version__,
        "platform": "%s-%s" % (sys.platform, os.uname().machine),
        "seeds": list(SEEDS),
        "r0_base_identity_ok": r0_ok,
        "rows": [],
    }

    for n_writes in (1500, 3000):
        for name, _, _ in arms:
            per = [results[(n_writes, name, s)] for s in SEEDS]
            occ_pass = sum(1 for r in per if r["n_distinct"] >= 2)
            def mean(key):
                vals = [r[key] for r in per if not (isinstance(r[key], float) and math.isnan(r[key]))]
                return sum(vals) / len(vals) if vals else float("nan")
            out["rows"].append({
                "n_writes": n_writes,
                "arm": name,
                "seeds_ge2_slots": "%d/%d" % (occ_pass, len(SEEDS)),
                "n_distinct_per_seed": [r["n_distinct"] for r in per],
                "mean_n_distinct": mean("n_distinct"),
                "mean_entropy_bits": mean("entropy_bits"),
                "mean_self_repeat": mean("self_repeat"),
                "mean_herfindahl": mean("herfindahl"),
                "mean_occ_cos_degenerate": mean("occ_cos_degenerate"),
                "mean_n_distinct_2ctx": mean("n_distinct_2ctx"),
                "mean_jaccard": mean("jaccard"),
                "jaccard_per_seed": [round(r["jaccard"], 4) for r in per],
                "mean_occ_cos": mean("occ_cos"),
                "occ_cos_per_seed": [round(r["occ_cos"], 4) if not math.isnan(r["occ_cos"])
                                     else None for r in per],
            })

    # ---- pre-registered rules ------------------------------------------------
    def row(n, arm):
        return next(r for r in out["rows"] if r["n_writes"] == n and r["arm"] == arm)

    verdicts = {}
    for n_writes in (1500, 3000):
        leg = row(n_writes, "argmin_legacy")
        lan = row(n_writes, "landed_usage_balancing")
        ref = row(n_writes, "salvaged_refractory_k2")
        n_lock_pass = int(leg["seeds_ge2_slots"].split("/")[0])
        n_landed_pass = int(lan["seeds_ge2_slots"].split("/")[0])
        j_delta = lan["mean_jaccard"] - ref["mean_jaccard"]
        verdicts[n_writes] = {
            "R4_legacy_reproduces_lock_3of5": n_lock_pass == 3,
            "R4_legacy_seeds_ge2": leg["seeds_ge2_slots"],
            "R1_landed_ge2_on_ge4of5": n_landed_pass >= 4,
            "R1_landed_seeds_ge2": lan["seeds_ge2_slots"],
            "R2_jaccard_delta_landed_minus_refractory": round(j_delta, 4),
            "R2_triggered_content_blind": j_delta > 0.25,
            "R3_occ_cos_landed": lan["mean_occ_cos"],
            "R3_occ_cos_refractory": ref["mean_occ_cos"],
            "R3_occ_cos_legacy": leg["mean_occ_cos"],
            "R3_cohens_d_landed_vs_refractory": cohens_d(
                [results[(n_writes, "landed_usage_balancing", s)]["occ_cos"] for s in SEEDS],
                [results[(n_writes, "salvaged_refractory_k2", s)]["occ_cos"] for s in SEEDS]),
        }
    out["verdicts"] = verdicts

    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
