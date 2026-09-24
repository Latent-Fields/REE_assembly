#!/opt/local/bin/python3
"""Summarize census_<recipe>_s<seed>.json into per-module (depth-2) classes. ASCII only."""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RECIPES = sys.argv[1:] or ["native", "r1078", "r1083", "allon", "zselfp0"]


def short(site):
    return site.split(" <- ")[0].replace("experiments/", "x/")


def tensor_class(r):
    moved = (r["param_delta_max"] or 0) > 0
    in_opt = bool(r["in_optimizers"])
    nz = r["step_status"].get("nonzero", 0)
    if in_opt and nz > 0 and moved:
        return "TRAINED"
    if in_opt and nz > 0 and not moved:
        return "TRAINED?(nonzero grad, no delta)"
    if in_opt and not moved:
        return "DEAD-OPT"
    if not in_opt and moved:
        return "NONGRAD-UPDATE"
    if in_opt and moved and nz == 0:
        return "MOVED-WITHOUT-GRAD"   # e.g. weight decay on a None-grad param would NOT do this
    return "ORPHAN"


def module_rows(d, depth=2):
    g = collections.OrderedDict()
    for r in d["rows"]:
        key = ".".join(r["name"].split(".")[:depth])
        g.setdefault(key, []).append(r)
    out = []
    for key, rs in g.items():
        cls = collections.Counter(tensor_class(r) for r in rs)
        numel = sum(r["numel"] for r in rs)
        opts = sorted({short(s) for r in rs for s in r["in_optimizers"]})
        reach = sorted({short(s) for r in rs for s in r["backward_reach"]})
        read = sum(1 for r in rs if r["read_at_act"])
        if len(cls) == 1:
            mcls = next(iter(cls))
        else:
            mcls = "MIXED(" + ",".join("%s:%d" % kv for kv in sorted(cls.items())) + ")"
        out.append(dict(module=key, n_tensors=len(rs), numel=numel, cls=mcls, opts=opts,
                        reach=reach, read=read))
    return out


def main():
    for rec in RECIPES:
        p = os.path.join(HERE, "results", "census_%s_s42.json" % rec)
        if not os.path.exists(p):
            print("MISSING", p)
            continue
        d = json.load(open(p))
        print("=" * 100)
        print("recipe=%s sha=%s world_dim=%s self_dim=%s DR13=%s act_err=%s" % (
            rec, d["ree_v3_sha"], d["world_dim"], d["self_dim"], d["use_self_recurrence"],
            d["act_error"]))
        print("optimizers:")
        for o in d["optimizers"]:
            print("   %s %s n_params=%d" % (o["cls"], o["site"], o["n_params"]))
        print("backward sites:", {short(k): v for k, v in d["backward_sites"].items()})
        tot = collections.Counter()
        for m in module_rows(d):
            tot[m["cls"] if not m["cls"].startswith("MIXED") else "MIXED"] += m["numel"]
            print("  %-46s t=%-3d n=%-7d %-34s read=%d/%d opt=%s reach=%s" % (
                m["module"], m["n_tensors"], m["numel"], m["cls"][:34], m["read"], m["n_tensors"],
                ";".join(m["opts"])[:60], ";".join(m["reach"])[:60]))
        allp = sum(tot.values())
        print("  numel by class:", {k: "%d (%.1f%%)" % (v, 100.0 * v / allp) for k, v in tot.items()})


if __name__ == "__main__":
    main()
