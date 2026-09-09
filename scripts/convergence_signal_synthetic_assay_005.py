#!/usr/bin/env python3
"""Synthetic Convergence Assay 005: imperfect provenance, learned leverage,
and domain-specific evaluator competence.

Standalone measurement assay. It does not modify the REE creature, claims,
or experiment queue.
"""
from __future__ import annotations
import argparse, itertools, json, math
from pathlib import Path
import numpy as np

TOPOLOGIES = {
    "independent_5": [[0],[1],[2],[3],[4]],
    "copies_5": [[0,1,2,3,4]],
    "two_clusters_3_2": [[0,1,2],[3,4]],
    "mixed_3_plus_2": [[0,1,2],[3],[4]],
}
TOPO_NAMES = tuple(TOPOLOGIES)
TOPO_P = np.array([0.30,0.20,0.20,0.30])
P_SOURCE = 0.78
READOUT = np.array([
    [0.98,0.80,0.80],
    [0.80,0.98,0.80],
    [0.80,0.80,0.98],
    [0.92,0.86,0.86],
    [0.86,0.92,0.86],
], dtype=float)
Q_VALUES=np.array([0.50,0.65,0.80,0.95])
Q_P=np.array([0.15,0.25,0.30,0.30])
L_VALUES=np.array([1,2,4,8])
PROFILES={
    "clean": {"missing":0.0,"wrong":0.0,"n_hist":64,
              "pair":{"same":1.0,"diff":0.0,"missing":0.370}},
    "moderate":{"missing":0.25,"wrong":0.10,"n_hist":32,
                "pair":{"same":0.911,"diff":0.104,"missing":0.370}},
    "harsh":{"missing":0.50,"wrong":0.20,"n_hist":8,
             "pair":{"same":0.812,"diff":0.184,"missing":0.370}},
}
METHODS=("M0_conflated","M1_global_factorised","M2_domain_factorised",
         "M3_hard_provenance","M4_soft_provenance",
         "A_trueprov_learnedL","A_softprov_trueL","M5_exact_oracle")
PAIRS=tuple(itertools.combinations(range(5),2))
VOTE_PATTERNS=tuple(itertools.product((-1,1),repeat=5))

def clip_p(p):
    return min(max(float(p),1e-12),1-1e-12)
def logit(p):
    p=clip_p(p); return math.log(p/(1-p))
def sigmoid(x):
    if x >= 0: return 1/(1+math.exp(-min(x,50)))
    e=math.exp(max(x,-50)); return e/(1+e)
def hbin(p):
    p=clip_p(p); return -(p*math.log(p)+(1-p)*math.log(1-p))
def eig(prior,q):
    prior=float(prior); q=float(q)
    px=prior*q+(1-prior)*(1-q)
    pp=prior*q/px
    pm=prior*(1-q)/(1-px)
    return hbin(prior)-(px*hbin(pp)+(1-px)*hbin(pm))

def calibrate_competence(seed=5005,n_per_domain=20_000):
    """Separate labelled corpus; only marginal domain competence is estimated."""
    rng=np.random.default_rng(seed)
    p=np.zeros((5,3),dtype=float)
    for d in range(3):
        src_correct=rng.random((n_per_domain,5)) < P_SOURCE
        src=np.where(src_correct,1,-1)
        rd_correct=rng.random((n_per_domain,5)) < READOUT[:,d][None,:]
        votes=np.where(rd_correct,src,-src)
        p[:,d]=(votes==1).mean(axis=0)
    return p,p.mean(axis=1)

def generate_votes(rng,y,domain,clusters):
    v=np.empty(5,dtype=np.int8)
    for cl in clusters:
        z=y if rng.random()<P_SOURCE else -y
        for i in cl:
            v[i]=z if rng.random()<READOUT[i,domain] else -z
    return v

def true_labels(clusters):
    t=np.empty(5,dtype=np.int8)
    for k,cl in enumerate(clusters):
        for i in cl: t[i]=k
    return t

def corrupt_labels(rng,t,missing,wrong):
    obs=t.copy()
    for i in range(5):
        if rng.random()<missing:
            obs[i]=-1
        elif rng.random()<wrong:
            choices=[x for x in range(5) if x!=int(t[i])]
            obs[i]=int(rng.choice(choices))
    return obs

def cluster_like(v,cl,y,domain):
    total=0.0
    for z,pz in ((y,P_SOURCE),(-y,1-P_SOURCE)):
        pr=pz
        for i in cl:
            pr *= READOUT[i,domain] if v[i]==z else (1-READOUT[i,domain])
        total += pr
    return total

def exact_posterior(v,domain,clusters):
    lp=lm=1.0
    for cl in clusters:
        lp *= cluster_like(v,cl,1,domain)
        lm *= cluster_like(v,cl,-1,domain)
    return lp/(lp+lm)

def hard_posterior(v,lod_i,obs):
    used=set(); total=0.0
    for i in range(5):
        if i in used: continue
        if obs[i] == -1:
            g=[i]
        else:
            g=[j for j in range(5) if j not in used and obs[j]==obs[i]]
        used.update(g)
        total += sum(v[j]*lod_i[j] for j in g)/len(g)
    return sigmoid(total)

def soft_posterior(v,lod_i,obs,pair):
    dep=[0.0]*5
    for i,j in PAIRS:
        if obs[i]==-1 or obs[j]==-1:
            s=pair["missing"]
        elif obs[i]==obs[j]:
            s=pair["same"]
        else:
            s=pair["diff"]
        dep[i]+=s; dep[j]+=s
    total=0.0
    for i in range(5):
        total += (1/(1+dep[i]))*v[i]*lod_i[i]
    return sigmoid(total)

def trueprov_posterior(v,lod_i,t):
    dep=[0]*5
    for i,j in PAIRS:
        if t[i]==t[j]:
            dep[i]+=1; dep[j]+=1
    return sigmoid(sum((1/(1+dep[i]))*v[i]*lod_i[i] for i in range(5)))

def learned_leverage(rng,L,n):
    h=rng.binomial(n,L/8)
    return 8*(h+1)/(n+2)

def hard_cluster_count(obs):
    return len(set(int(x) for x in obs if x!=-1)) + int(np.sum(obs==-1))

def build_caches(p_dom,p_global):
    lod_global=np.array([logit(x) for x in p_global])
    lod_dom=np.array([[logit(p_dom[i,d]) for i in range(5)] for d in range(3)])
    base_global={}; base_domain={}; exact={}; trueprov={}
    for vt in VOTE_PATTERNS:
        v=np.array(vt,dtype=np.int8)
        base_global[vt]=sigmoid(float(np.dot(v,lod_global)))
        for d in range(3):
            base_domain[(d,vt)]=sigmoid(float(np.dot(v,lod_dom[d])))
            for topo in TOPO_NAMES:
                exact[(topo,d,vt)]=exact_posterior(v,d,TOPOLOGIES[topo])
                t=true_labels(TOPOLOGIES[topo])
                trueprov[(topo,d,vt)]=trueprov_posterior(v,lod_dom[d],t)
    return lod_global,lod_dom,base_global,base_domain,exact,trueprov

def run_profile(profile,seed,episodes,candidates,p_dom,p_global,caches):
    cfg=PROFILES[profile]
    _,lod_dom,base_global,base_domain,exact_cache,trueprov_cache=caches
    rng=np.random.default_rng(seed)
    regret={m:0.0 for m in METHODS}; hits={m:0 for m in METHODS}; util={m:0.0 for m in METHODS}
    oracle_total=0.0; oracle_viol=0; l_abs=0.0; n_cand=0
    for _ in range(episodes):
        rows=[]
        for _ in range(candidates):
            topo=str(rng.choice(TOPO_NAMES,p=TOPO_P))
            clusters=TOPOLOGIES[topo]
            d=int(rng.integers(0,3)); y=1 if rng.random()<0.5 else -1
            v=generate_votes(rng,y,d,clusters); vt=tuple(int(x) for x in v)
            t=true_labels(clusters)
            obs=corrupt_labels(rng,t,cfg["missing"],cfg["wrong"])
            q=float(rng.choice(Q_VALUES,p=Q_P)); L=int(rng.choice(L_VALUES))
            Lh=learned_leverage(rng,L,cfg["n_hist"])
            l_abs += abs(Lh-L); n_cand += 1
            p_g=base_global[vt]
            p_d=base_domain[(d,vt)]
            p_h=hard_posterior(v,lod_dom[d],obs)
            p_s=soft_posterior(v,lod_dom[d],obs,cfg["pair"])
            p_t=trueprov_cache[(topo,d,vt)]
            p_e=exact_cache[(topo,d,vt)]
            scores={
                "M0_conflated": hard_cluster_count(obs)*eig(p_g,q),
                "M1_global_factorised": Lh*eig(p_g,q),
                "M2_domain_factorised": Lh*eig(p_d,q),
                "M3_hard_provenance": Lh*eig(p_h,q),
                "M4_soft_provenance": Lh*eig(p_s,q),
                "A_trueprov_learnedL": Lh*eig(p_t,q),
                "A_softprov_trueL": L*eig(p_s,q),
                "M5_exact_oracle": L*eig(p_e,q),
            }
            rows.append(scores)
        truev=np.array([r["M5_exact_oracle"] for r in rows])
        best=float(truev.max()); oracle_total += best
        for m in METHODS:
            sc=np.array([r[m] for r in rows])
            idx=int(np.argmax(sc)); chosen=float(truev[idx])
            if chosen > best + 1e-12: oracle_viol += 1
            regret[m] += best-chosen; util[m] += chosen
            hits[m] += abs(chosen-best)<1e-12
    out={}
    for m in METHODS:
        out[m]={"mean_regret":regret[m]/episodes,
                "optimal_hit_rate":hits[m]/episodes,
                "oracle_utility_fraction":util[m]/oracle_total}
    return {"methods":out,"L_hat_mae":l_abs/n_cand,"oracle_ordering_violations":oracle_viol}

def run(seed=29,episodes=10_000,candidates=6):
    p_dom,p_global=calibrate_competence()
    caches=build_caches(p_dom,p_global)
    profiles={}
    for k,name in enumerate(("clean","moderate","harsh")):
        profiles[name]=run_profile(name,seed+1000*k,episodes,candidates,p_dom,p_global,caches)
    c1=(profiles["moderate"]["methods"]["M4_soft_provenance"]["mean_regret"] <=
        .45*profiles["moderate"]["methods"]["M2_domain_factorised"]["mean_regret"] and
        profiles["moderate"]["methods"]["M4_soft_provenance"]["oracle_utility_fraction"] >= .95)
    c2=(profiles["harsh"]["methods"]["M4_soft_provenance"]["mean_regret"] <=
        .65*profiles["harsh"]["methods"]["M2_domain_factorised"]["mean_regret"] and
        profiles["harsh"]["methods"]["M4_soft_provenance"]["oracle_utility_fraction"] >= .92)
    c3=(profiles["moderate"]["methods"]["M4_soft_provenance"]["mean_regret"] <=
        .95*profiles["moderate"]["methods"]["M3_hard_provenance"]["mean_regret"] and
        profiles["harsh"]["methods"]["M4_soft_provenance"]["mean_regret"] <=
        .80*profiles["harsh"]["methods"]["M3_hard_provenance"]["mean_regret"])
    c4=(profiles["moderate"]["L_hat_mae"] <= .45 and profiles["harsh"]["L_hat_mae"] <= .90 and
        profiles["moderate"]["methods"]["A_trueprov_learnedL"]["oracle_utility_fraction"] >= .975 and
        profiles["harsh"]["methods"]["A_trueprov_learnedL"]["oracle_utility_fraction"] >= .955)
    r_domain=np.mean([profiles[p]["methods"]["M2_domain_factorised"]["mean_regret"] for p in profiles])
    r_global=np.mean([profiles[p]["methods"]["M1_global_factorised"]["mean_regret"] for p in profiles])
    c5=r_domain <= .95*r_global
    c6=(all(profiles[p]["methods"]["M5_exact_oracle"]["mean_regret"] < 1e-12 for p in profiles)
        and sum(profiles[p]["oracle_ordering_violations"] for p in profiles)==0)
    criteria={
        "C1_moderate_useful":bool(c1),
        "C2_harsh_graceful":bool(c2),
        "C3_soft_beats_hard":bool(c3),
        "C4_learned_leverage_adequate":bool(c4),
        "C5_domain_competence_earns_representation":bool(c5),
        "C5_mean_domain_regret":float(r_domain),
        "C5_mean_global_regret":float(r_global),
        "C6_oracle_ceiling":bool(c6),
    }
    criteria["measurement_pass_C1_to_C6"]=bool(c1 and c2 and c3 and c4 and c5 and c6)
    return {
        "assay":"convergence_signal_synthetic_assay_005",
        "status":"synthetic_reference_run_only",
        "seed":seed,"episodes_per_profile":episodes,"candidates_per_episode":candidates,
        "calibration_examples_per_domain":20_000,
        "estimated_domain_accuracy":p_dom.tolist(),
        "estimated_global_accuracy":p_global.tolist(),
        "profiles":profiles,"criteria":criteria,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",type=int,default=29)
    ap.add_argument("--episodes",type=int,default=10_000)
    ap.add_argument("--candidates",type=int,default=6)
    ap.add_argument("--out-json",type=Path,default=None)
    args=ap.parse_args()
    payload=run(args.seed,args.episodes,args.candidates)
    text=json.dumps(payload,indent=2,sort_keys=True)
    print(text)
    if args.out_json:
        args.out_json.parent.mkdir(parents=True,exist_ok=True)
        args.out_json.write_text(text+"\n",encoding="utf-8")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
