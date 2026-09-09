#!/usr/bin/env python3
"""Synthetic Convergence Assay 006: state-dependent evidence and downstream-overlap graphs."""
from __future__ import annotations
import argparse, itertools, json, math
from pathlib import Path
import numpy as np

P_SOURCE=0.78
P_READOUT=0.90
P_MARG=P_SOURCE*P_READOUT+(1-P_SOURCE)*(1-P_READOUT)
Q_VALUES=np.array([0.50,0.65,0.80,0.95]); Q_P=np.array([0.15,0.25,0.30,0.30])
CTX_CLUSTERS={0:[[0,1,2],[3],[4]],1:[[0],[1],[2,3,4]],2:[[0,3],[1,4],[2]]}
CONSUMER_GROUPS={0:[[0,1,2],[3],[4,5],[6],[7]],1:[[0],[1,2],[3,4,5],[6,7]],2:[[0,7],[1],[2,3],[4],[5,6]]}
METHODS=("M0_static_count","M0b_static_overlap","M1_dynamicE_count","M2_staticE_dynamicL","M3_dynamic_both","M4_exact_oracle")
PAIRS=tuple(itertools.combinations(range(5),2))

def clip_p(p): return min(max(float(p),1e-12),1-1e-12)
def logit(p): p=clip_p(p); return math.log(p/(1-p))
def sigmoid(x):
    if x>=0: return 1/(1+math.exp(-min(x,50)))
    e=math.exp(max(x,-50)); return e/(1+e)
def hbin(p): p=clip_p(p); return -(p*math.log(p)+(1-p)*math.log(1-p))
def eig(p,q):
    px=p*q+(1-p)*(1-q); pp=p*q/px; pm=p*(1-q)/(1-px)
    return hbin(p)-(px*hbin(pp)+(1-px)*hbin(pm))

def dep_matrix(n,groups):
    s=np.zeros((n,n),dtype=float)
    for g in groups:
        for i,j in itertools.combinations(g,2): s[i,j]=s[j,i]=1.0
    return s
E_DYNAMIC={c:dep_matrix(5,g) for c,g in CTX_CLUSTERS.items()}
E_STATIC=sum(E_DYNAMIC.values())/3.0
C_DYNAMIC={c:dep_matrix(8,g) for c,g in CONSUMER_GROUPS.items()}
C_STATIC=sum(C_DYNAMIC.values())/3.0

def generate_votes(rng,y,clusters):
    v=np.empty(5,dtype=np.int8)
    for cl in clusters:
        z=y if rng.random()<P_SOURCE else -y
        for i in cl: v[i]=z if rng.random()<P_READOUT else -z
    return v

def cluster_like(v,cl,y):
    total=0.0
    for z,pz in ((y,P_SOURCE),(-y,1-P_SOURCE)):
        pr=pz
        for i in cl: pr*=P_READOUT if v[i]==z else (1-P_READOUT)
        total+=pr
    return total

def exact_posterior(v,clusters):
    lp=lm=1.0
    for cl in clusters:
        lp*=cluster_like(v,cl,1); lm*=cluster_like(v,cl,-1)
    return lp/(lp+lm)

def approx_posterior(v,S):
    w=1/(1+S.sum(axis=1)); lod=logit(P_MARG)
    return sigmoid(float(np.sum(w*v*lod)))

def effective_leverage(ids,S):
    ids=list(ids); sub=S[np.ix_(ids,ids)]; w=1/(1+sub.sum(axis=1)); return float(w.sum())

def run(seed=37,episodes=10_000,candidates=6):
    rng=np.random.default_rng(seed)
    regret={m:0.0 for m in METHODS}; hits={m:0 for m in METHODS}; util={m:0.0 for m in METHODS}
    oracle_total=0.0; oracle_viol=0
    for _ in range(episodes):
        rows=[]
        for _ in range(candidates):
            c=int(rng.integers(0,3)); y=1 if rng.random()<0.5 else -1
            clusters=CTX_CLUSTERS[c]; v=generate_votes(rng,y,clusters)
            q=float(rng.choice(Q_VALUES,p=Q_P)); k=int(rng.integers(1,7)); ids=tuple(sorted(rng.choice(8,size=k,replace=False)))
            ps=approx_posterior(v,E_STATIC); pd=approx_posterior(v,E_DYNAMIC[c]); pe=exact_posterior(v,clusters)
            lc=float(len(ids)); ls=effective_leverage(ids,C_STATIC); ld=effective_leverage(ids,C_DYNAMIC[c])
            rows.append({
                "M0_static_count":lc*eig(ps,q),
                "M0b_static_overlap":ls*eig(ps,q),
                "M1_dynamicE_count":lc*eig(pd,q),
                "M2_staticE_dynamicL":ld*eig(ps,q),
                "M3_dynamic_both":ld*eig(pd,q),
                "M4_exact_oracle":ld*eig(pe,q),
            })
        truev=np.array([r["M4_exact_oracle"] for r in rows]); best=float(truev.max()); oracle_total+=best
        for m in METHODS:
            idx=int(np.argmax([r[m] for r in rows])); chosen=float(truev[idx])
            if chosen>best+1e-12: oracle_viol+=1
            regret[m]+=best-chosen; util[m]+=chosen; hits[m]+=abs(chosen-best)<1e-12
    out={m:{"mean_regret":regret[m]/episodes,"optimal_hit_rate":hits[m]/episodes,"oracle_utility_fraction":util[m]/oracle_total} for m in METHODS}
    c1=out["M3_dynamic_both"]["mean_regret"]<=.020 and out["M3_dynamic_both"]["oracle_utility_fraction"]>=.98
    c2=out["M3_dynamic_both"]["mean_regret"]<=.60*out["M2_staticE_dynamicL"]["mean_regret"]
    c3=out["M3_dynamic_both"]["mean_regret"]<=.60*out["M1_dynamicE_count"]["mean_regret"]
    c4=out["M3_dynamic_both"]["optimal_hit_rate"]>=max(out["M1_dynamicE_count"]["optimal_hit_rate"],out["M2_staticE_dynamicL"]["optimal_hit_rate"])+.04
    c5=out["M0b_static_overlap"]["oracle_utility_fraction"]<=.97 and out["M3_dynamic_both"]["oracle_utility_fraction"]-out["M0b_static_overlap"]["oracle_utility_fraction"]>=.02
    c6=out["M4_exact_oracle"]["mean_regret"]<1e-12 and oracle_viol==0
    criteria={"C1_dynamic_graph_useful":bool(c1),"C2_dynamic_evidence_matters":bool(c2),"C3_dynamic_overlap_matters":bool(c3),"C4_both_axes_hit_gain":bool(c4),"C5_static_average_insufficient":bool(c5),"C6_oracle_ceiling":bool(c6)}
    criteria["measurement_pass_C1_to_C6"]=all(criteria.values())
    return {"assay":"convergence_signal_synthetic_assay_006","status":"synthetic_reference_run_only","seed":seed,"episodes":episodes,"candidates_per_episode":candidates,"methods":out,"criteria":criteria,"oracle_ordering_violations":oracle_viol}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--seed",type=int,default=37); ap.add_argument("--episodes",type=int,default=10_000); ap.add_argument("--candidates",type=int,default=6); ap.add_argument("--out-json",type=Path,default=None); args=ap.parse_args()
    payload=run(args.seed,args.episodes,args.candidates); text=json.dumps(payload,indent=2,sort_keys=True); print(text)
    if args.out_json: args.out_json.parent.mkdir(parents=True,exist_ok=True); args.out_json.write_text(text+"\n",encoding="utf-8")
    return 0
if __name__=="__main__": raise SystemExit(main())
