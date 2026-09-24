#!/opt/local/bin/python3
"""Module x recipe class matrix (markdown) from census_<recipe>_s42.json. ASCII only."""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from summarize import module_rows
R = [("native", "N"), ("r1078", "A"), ("r1083", "B"), ("allon", "C"), ("zselfp0", "Z")]
CODE = {"TRAINED": "T", "DEAD-OPT": "D", "ORPHAN": "O", "NONGRAD-UPDATE": "G", "MOVED-WITHOUT-GRAD": "G"}
mat = collections.OrderedDict(); numel = {}; read = collections.defaultdict(set)
for rec, tag in R:
    d = json.load(open("results/census_%s_s42.json" % rec))
    for m in module_rows(d):
        c = m["cls"]
        if c.startswith("MIXED"):
            parts = dict(p.split(":") for p in c[6:-1].split(","))
            c = "M(" + "/".join("%s%s" % (CODE.get(k, "?"), v) for k, v in sorted(parts.items())) + ")"
        else:
            c = CODE.get(c, c)
        mat.setdefault(m["module"], {})[tag] = c
        numel[m["module"]] = max(numel.get(m["module"], 0), m["numel"])
        if m["read"]:
            read[m["module"]].add(tag)
print("| module | params | N | A 1078 | B 1083 | C all-ON | Z zself-P0 | read at act (recipes) |")
print("|---|---:|---|---|---|---|---|---|")
for mod, row in mat.items():
    print("| `%s` | %d | %s | %s |" % (mod, numel[mod], " | ".join(row.get(t, "-") for _, t in R),
                                    ",".join(t for _, t in R if t in read[mod]) or "none"))
