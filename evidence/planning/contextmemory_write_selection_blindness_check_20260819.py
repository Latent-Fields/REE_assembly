"""POST-HOC (not pre-registered): is the landed rule's slot sequence content-dependent?

Direct test: drive the SAME module init (same torch seed) with THREE different
content streams and compare the slot sequences. A content-dependent selector
must produce different sequences; a content-blind one produces the same.
"""
import os, subprocess, sys, types
BASE = "/Users/dgolden/REE_Working"; REE_V3 = os.path.join(BASE, "ree-v3")
sys.path.insert(0, REE_V3)
import torch
from ree_core.predictors.e1_deep import ContextMemory as Main

src = subprocess.check_output(["git","-C",REE_V3,"show","dd4b0a4:ree_core/predictors/e1_deep.py"], text=True)
mod = types.ModuleType("salv"); exec(compile(src,"<salv>","exec"), mod.__dict__)
Salv = mod.ContextMemory

L, M, S = 64, 128, 16
def stream(seed, n, clusters=1, scale=0.078, jitter=0.0078):
    g = torch.Generator().manual_seed(seed)
    bases = [torch.randn(1, L, generator=g) * scale for _ in range(clusters)]
    return [(i % clusters, bases[i % clusters] + torch.randn(1, L, generator=g) * jitter)
            for i in range(n)]

def seq(cls, seed, states, **kw):
    torch.manual_seed(seed)
    cm = cls(L, M, S, gated_content_write=True, **kw)
    out = []
    for st in states:
        b = cm.memory.data.clone(); cm.write(st)
        d = (cm.memory.data - b).abs().sum(1)
        out.append(int(d.argmax()) if float(d.max()) > 0 else None)
    return out

ARMS = [("argmin_legacy", Main, {}),
        ("landed_usage_balancing", Main, {"write_usage_balancing": True}),
        ("salvaged_refractory_k2", Salv, {"write_selection":"refractory","write_refractory_k":2}),
        ("salvaged_usage", Salv, {"write_selection":"usage"}),
        ("salvaged_gumbel", Salv, {"write_selection":"gumbel"})]

N = 600
print("%-24s %-12s %-12s %-12s %s" % ("arm","agree_A_vs_B","agree_A_vs_C","round_robin","first 20 slots (stream A)"))
for name, cls, kw in ARMS:
    ag_ab, ag_ac, rr = [], [], []
    for seed in (0,7,13,42,100):
        A = [s for _, s in stream(seed, N, 1)]                    # near-constant
        B = [s for _, s in stream(seed+9991, N, 1)]               # different content, same shape
        C = [s for _, s in stream(seed, N, 2)]                    # 2-context
        sa, sb, sc = seq(cls,seed,A,**kw), seq(cls,seed,B,**kw), seq(cls,seed,C,**kw)
        ag_ab.append(sum(1 for x,y in zip(sa,sb) if x==y)/len(sa))
        ag_ac.append(sum(1 for x,y in zip(sa,sc) if x==y)/len(sa))
        # strict round-robin = always the least-recently-written slot
        lru, hit = {}, 0
        for t, idx in enumerate(sa):
            if len(lru) == S:
                pred = min(lru, key=lambda k: lru[k])
                if pred == idx: hit += 1
            lru[idx] = t
        rr.append(hit/max(sum(1 for t,_ in enumerate(sa) if t>=S),1))
    m = lambda v: sum(v)/len(v)
    print("%-24s %-12.3f %-12.3f %-12.3f %s" % (name, m(ag_ab), m(ag_ac), m(rr),
          seq(cls,0,[s for _,s in stream(0,20,1)],**kw)))
print()
print("chance agreement with 16 slots ~ 0.0625 (and ~1.0 means content-blind)")
