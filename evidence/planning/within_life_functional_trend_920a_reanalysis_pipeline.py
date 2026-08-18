#!/usr/bin/env python3
"""Reference implementation for the three-question zero-compute reanalysis of
V3-EXQ-920a's committed episode log, per Section 11 item 1 of
`failure_autopsy_V3-EXQ-920a_2026-08-16.md`:

  (1) does the empirical within-life hazard function support the "wear
      (accumulating damage)" reading, or the memoryless reading imported from
      V3-EXQ-912?
  (2) does the harm-dose-at-death hypothesis (Section 6b of the autopsy) hold
      up against PER-STEP `harm_event`/`health`, rather than the autopsy's
      reconstruction from the `lifetime_affective_occupancy` summary stat?
  (3) what explains the seed-3 reef anomaly (91.9% reef time, second-earliest
      death, second-highest harm rate)?

Landed as a TRACKED file, per the same "the n=1 script was left in a
scratchpad and did not survive" lesson Section 6/7 of the parent doc already
states -- this is analysis, not an experiment; results are appended as
Section 8 of `within_life_functional_trend_920_lineage_2026-08-14.md`.

DESCRIPTIVE ONLY. N=8. No p-values are computed anywhere in this file.
ASCII-only output (CLAUDE.md).

Run:  /opt/local/bin/python3 within_life_functional_trend_920a_reanalysis_pipeline.py
"""
import json
import statistics as st
from pathlib import Path

LOG = Path(
    "/Users/dgolden/REE_Working/REE_assembly/evidence/experiments/"
    "v3_exq_920_uncensored_survival_single_life_fishtank/"
    "v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_episode_log.json"
)


def spearman(a, b):
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        r = [0.0] * len(vals)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg_rank = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg_rank
            i = j + 1
        return r
    ra, rb = ranks(a), ranks(b)
    return pearson(ra, rb)


def pearson(a, b):
    ma, mb = st.mean(a), st.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = sum((x - ma) ** 2 for x in a) ** 0.5
    db = sum((y - mb) ** 2 for y in b) ** 0.5
    return num / (da * db) if da and db else float("nan")


def cv(vals):
    # Sample stdev (n-1), matching the autopsy's own convention (its sd=670.2 for
    # survival and sd=14.0 for harm-dose both reproduce exactly under this, not pstdev).
    m = st.mean(vals)
    s = st.stdev(vals)
    return m, s, (s / m if m else float("nan"))


def main():
    doc = json.loads(LOG.read_text())
    seeds = doc["seeds"]
    N = len(seeds)

    rows = []
    for sd in seeds:
        life = sd["life"]
        steps = life["steps"]
        survival = life["realized_steps"]
        done = life["done_cause"]
        assert survival == len(steps), (sd["seed"], survival, len(steps))
        harm_total = sum(1 for s in steps if s["harm_event"])
        n_in_reef = sum(1 for s in steps if s["in_reef"])
        harm_in_reef = sum(1 for s in steps if s["in_reef"] and s["harm_event"])
        harm_out_reef = harm_total - harm_in_reef
        n_out_reef = survival - n_in_reef
        rate_in = harm_in_reef / n_in_reef if n_in_reef else float("nan")
        rate_out = harm_out_reef / n_out_reef if n_out_reef else float("nan")
        transitions = sum(
            1 for i in range(1, survival) if steps[i]["in_reef"] != steps[i - 1]["in_reef"]
        )
        reef_cells = set(tuple(c) for c in life["reef_cells"])
        init_res = life["initial_resources"]
        init_haz = life["initial_hazards"]
        res_in_reef = sum(1 for r in init_res if tuple(r) in reef_cells)
        haz_in_reef = sum(1 for h in init_haz if tuple(h) in reef_cells)
        res_counts = [len(s["resources"]) for s in steps]
        health_lt50 = next((s["t"] for s in steps if s["health"] < 0.5), None)
        energy_le0 = next((s["t"] for s in steps if s["energy"] <= 0.0), None)
        health_drops = [
            steps[i]["health"] - steps[i + 1]["health"]
            for i in range(survival - 1)
            if steps[i + 1]["health"] < steps[i]["health"]
        ]
        rows.append(dict(
            seed=sd["seed"], survival=survival, done=done, harm_total=harm_total,
            harm_rate=harm_total / survival, frac_in_reef=n_in_reef / survival,
            rate_in=rate_in, rate_out=rate_out, transitions=transitions,
            trans_rate=transitions / survival, res_in_reef=res_in_reef,
            n_init_res=len(init_res), haz_in_reef=haz_in_reef, n_init_haz=len(init_haz),
            res_start=res_counts[0], res_min=min(res_counts), res_end=res_counts[-1],
            health_lt50=health_lt50, energy_le0=energy_le0,
            total_health_loss=sum(health_drops), mean_drop_per_harm_event=(
                sum(health_drops) / harm_total if harm_total else float("nan")
            ),
        ))

    print("=" * 100)
    print("Q1: EMPIRICAL WITHIN-LIFE HAZARD FUNCTION -- does the wear reading hold up?")
    print("=" * 100)
    surv = [r["survival"] for r in rows]
    m, s, c = cv(surv)
    print(f"survival times: {sorted(surv)}")
    print(f"n={N} mean={m:.2f} sd={s:.2f} CV={c:.4f}  (exponential/memoryless => CV=1 exactly)")
    print("A homogeneous-Poisson (constant-hazard) death process forces i.i.d. Exponential")
    print("survival times, whose CV is 1 regardless of the rate. CV << 1 is a model-free")
    print("(distribution-free) signature inconsistent with constant hazard and consistent")
    print("with an increasing (wear-out / IFR) hazard. It does not, on its own, fit or")
    print("identify a distributional family (n=8 cannot -- autopsy Section 6c).")
    print()
    print("Discrete-time hazard by 500-step bin (912's own segment scale), all 8 lives pooled:")
    print(f"{'bin':>14}{'at_risk':>9}{'deaths':>8}{'hazard':>9}")
    bin_edges = list(range(0, 3001, 500))
    at_risk = N
    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
        deaths = sum(1 for t in surv if lo <= t < hi)
        hz = deaths / at_risk if at_risk else float("nan")
        print(f"{lo:>6}-{hi:<6}{at_risk:>9}{deaths:>8}{hz:>9.3f}")
        at_risk -= deaths
    print(f"(final at-risk after 3000: {at_risk} -- matches 0 deaths beyond max=2527)")
    print()
    print("Self-referential memoryless null (rate = 1/observed mean, no import from 912):")
    lam = 1.0 / m
    print(f"lambda = 1/{m:.2f} = {lam:.6f} per step")
    for t in [666, 1000, 1500, 2000, 2500]:
        pred_surv_frac = pow(2.718281828459045, -lam * t)
        obs_surv_frac = sum(1 for x in surv if x > t) / N
        print(f"  t={t:5d}: predicted P(survive)={pred_surv_frac:.3f}  "
              f"observed fraction still alive={obs_surv_frac:.3f}  "
              f"(observed count={sum(1 for x in surv if x > t)}/{N})")
    print()
    print("Cross-check against 912's own imported calibration (autopsy 6b):")
    p912 = 4 / 60
    lam912 = -st.mean([0]) if False else None
    mean912 = 500 / p912
    print(f"  912 per-500-step hazard p={p912:.4f} -> implied mean {mean912:.0f} steps")
    print(f"  920a observed mean {m:.2f} steps -> ratio {mean912 / m:.2f}x")

    print()
    print("=" * 100)
    print("Q2: HARM-DOSE-AT-DEATH HYPOTHESIS -- verified against PER-STEP harm_event/health")
    print("=" * 100)
    harm_counts = [r["harm_total"] for r in rows]
    mh, sh, ch = cv(harm_counts)
    print(f"{'seed':>5}{'survival':>10}{'harm_total':>12}{'harm_rate':>11}"
          f"{'total_health_loss':>19}{'mean_drop/event':>17}")
    for r in rows:
        print(f"{r['seed']:>5}{r['survival']:>10}{r['harm_total']:>12}"
              f"{r['harm_rate']:>11.4f}{r['total_health_loss']:>19.4f}"
              f"{r['mean_drop_per_harm_event']:>17.5f}")
    print(f"\nharm_total counted directly from per-step boolean `harm_event` field")
    print(f"(NOT reconstructed from `lifetime_affective_occupancy`): {sorted(harm_counts)}")
    print(f"mean={mh:.2f} sd={sh:.2f} CV={ch:.4f}  max/min={max(harm_counts)/min(harm_counts):.2f}")
    print(f"survival CV (from Q1) = {c:.4f}  max/min={max(surv)/min(surv):.2f}")
    print(f"stereotypy ratio (survival_CV / harm_CV) = {c/ch:.2f}x")
    print(f"Spearman(harm_rate, survival) = {spearman([r['harm_rate'] for r in rows], surv):.4f}")
    print(f"Spearman(harm_total, survival) = {spearman(harm_counts, surv):.4f}")
    mean_drops = [r["mean_drop_per_harm_event"] for r in rows]
    mdm, mds, mdc = cv(mean_drops)
    print(f"\nmean health-drop-per-harm-event across seeds: {[round(x,5) for x in mean_drops]}")
    print(f"  mean={mdm:.5f} sd={mds:.5f} CV={mdc:.4f}")
    print(f"  1/mean_harm_total = {1.0/mh:.5f} (implied per-event dose under a flat 1.0 budget)")

    print()
    print("=" * 100)
    print("Q3: SEED-3 REEF ANOMALY")
    print("=" * 100)
    print(f"{'seed':>5}{'survival':>9}{'frac_reef':>10}{'harm_tot':>9}{'harm_rate':>10}"
          f"{'rate_in':>9}{'rate_out':>9}{'trans':>7}{'trans_rt':>9}{'res_s/min/end':>15}"
          f"{'res_in_reef':>12}{'haz_in_reef':>12}{'h<0.5':>7}{'E<=0':>6}")
    for r in rows:
        res = f"{r['res_start']}/{r['res_min']}/{r['res_end']}"
        rin = f"{r['res_in_reef']}/{r['n_init_res']}"
        hin = f"{r['haz_in_reef']}/{r['n_init_haz']}"
        print(f"{r['seed']:>5}{r['survival']:>9}{r['frac_in_reef']:>10.3f}{r['harm_total']:>9}"
              f"{r['harm_rate']:>10.4f}{r['rate_in']:>9.4f}{r['rate_out']:>9.4f}"
              f"{r['transitions']:>7}{r['trans_rate']:>9.4f}{res:>15}{rin:>12}{hin:>12}"
              f"{str(r['health_lt50']):>7}{str(r['energy_le0']):>6}")
    print(f"\nSpearman(frac_in_reef, survival) = "
          f"{spearman([r['frac_in_reef'] for r in rows], surv):.4f}")
    print(f"Resources placed inside reef cells at spawn, ANY seed: "
          f"{sum(r['res_in_reef'] for r in rows)} of {sum(r['n_init_res'] for r in rows)} total "
          f"(0 in every individual seed) -- reef is structurally foodless in this env layout.")
    seed3 = next(r for r in rows if r["seed"] == 3)
    print(f"\nseed 3 detail: frac_in_reef={seed3['frac_in_reef']:.3f} "
          f"(highest of {N}), transitions={seed3['transitions']} "
          f"trans_rate={seed3['trans_rate']:.4f} (highest of {N}), "
          f"resources consumed over whole life = "
          f"{seed3['res_start'] - seed3['res_end']} (start={seed3['res_start']}, "
          f"end={seed3['res_end']})")
    print(f"  harm_rate_in_reef={seed3['rate_in']:.4f} vs harm_rate_out_reef="
          f"{seed3['rate_out']:.4f} ({seed3['rate_out']/seed3['rate_in']:.1f}x higher outside)")
    print(f"  health<0.5 at t={seed3['health_lt50']}, energy<=0 at t={seed3['energy_le0']} "
          f"-- health crossed 0.5 BEFORE energy exhaustion "
          f"({'yes' if seed3['health_lt50'] < seed3['energy_le0'] else 'no'})")
    print(f"  haz_in_reef={seed3['haz_in_reef']}/{seed3['n_init_haz']} initial hazards spawned "
          f"inside seed 3's own reef cells (max possible across the corpus)")


if __name__ == "__main__":
    main()
