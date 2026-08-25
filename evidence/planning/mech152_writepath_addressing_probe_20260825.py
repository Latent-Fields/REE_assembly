#!/usr/bin/env python3
"""MECH-152 write-path ADDRESSING probe -- LEGACY vs BIAS vs REFRACTORY.

WHY THIS EXISTS
---------------
substrate_queue entry `contextmemory-write-path-addressing-degeneracy` sits at
`implemented_pending_validation`. Governance cycle gov-20260821-0203 ratified
`failure_autopsy_V3-EXQ-943_2026-08-21` and deliberately did NOT flip it,
recording that it must not go to `implemented_validated` "without a human call
on whether occupancy-without-addressing (BIAS) or the k+1 eligibility floor
(REFRACTORY) closes the corrupting 1-slot-bank defect".

V3-EXQ-943 PASSed both arms on OCCUPANCY (BIAS 16/16/16/16/16, REFRACTORY
6/3/3/3/9, LEGACY 8/1/1/1/9 against a floor of 2) and its own autopsy states
plainly that occupancy CANNOT discriminate the two. This probe measures the
quantity that can: whether the resulting bank is CONTENT-ORGANISED, and what
MECH-152 terrain_weight modulation depth is attainable on it.

WHY MECH-152 IS THE RIGHT LENS FOR THAT CALL
--------------------------------------------
From `mech152_measurement_redesign_gated_20260818.md` section 2a, re-verified
against e1_deep.py:684 in this session:

    terrain_weight = sigmoid(cue_terrain_proj(cue_context))
    cue_context    = output_proj(bmm(selection_weights, value_proj(memory)))

There is NO direct z_world path. z_world enters ONLY through the selection
weights. Selection weights are a softmax (non-negative, sum to 1), and
value_proj / output_proj / cue_terrain_proj are linear with sigmoid monotone,
so cue_context is a CONVEX COMBINATION of per-slot vectors and the attainable
w_harm range is EXACTLY [min_i, max_i] over the per-slot images -- a tight
bound, not an upper bound. Consequence: if slot content is not organised BY
CONTEXT, terrain_weight cannot vary with context, whatever the read path does.

That makes MECH-152 the claim for which "occupancy without addressing" is
decisive rather than academic -- which is precisely the pending human call.

WHAT SECTION 2c OF THE REDESIGN DOC DID *NOT* TEST
--------------------------------------------------
2c showed cue_terrain_proj can amplify a tiny 2-slot difference to a 0.6056
swing under best-case training. Stated honestly there, and repeated here: that
training regressed PER-SLOT targets DIRECTLY, bypassing z_world, the tagger and
the selection entirely. It establishes attainability across SLOTS. It does NOT
establish attainability across CONTEXTS, which additionally requires the
SELECTION to route different contexts to different slots. That gap is exactly
what this probe closes, and it is the gap the pending governance call sits in.

METHOD
------
Two-context low-variance query stream (the regime the substrate_queue entry
names), context switching every 5 writes to match the 436-family harness that
V3-EXQ-943 used. 3000 writes, 5 seeds (42, 7, 13, 100, 200 -- 943's seeds), all
three write modes driven with an IDENTICAL stream per seed.

Per mode, per seed:
  n_distinct            distinct slots ever addressed (943's DV, for continuity)
  nmi_context_slot      normalised mutual information between context label and
                        slot addressed. 0 = addressing is blind to content;
                        1 = addressing is fully determined by content.
  js_divergence         Jensen-Shannon divergence between the two contexts'
                        slot distributions (bits, 0..1)
  exclusive_slots       slots addressed by exactly one of the two contexts
  bound_untrained       section 2a tight bound on w_harm range, cue_terrain_proj
                        at init
  depth_bestcase        BEST-CASE between-context depth through the REAL read
                        path after training cue_terrain_proj only
  band_met              depth_bestcase clears MECH-152's own asserted band
                        (E[w_harm|hazard] > 0.8 AND E[w_harm|resource] < 0.5)

This is a PROBE, not an experiment: no manifest, no queue entry, no claim
write, and it is not evidence for or against MECH-152 itself. It is evidence
about whether MECH-152 is MEASURABLE under each candidate write mode.

`depth_bestcase` is an UPPER BOUND on what the real phased training loop could
extract, for the same reason section 2c's 0.6056 was -- it trains
cue_terrain_proj directly on the read output with the tagger disabled. A mode
that cannot reach the band HERE cannot reach it in a real run either, which is
the direction that matters for a gating decision.
"""

import json
import math
import sys
from pathlib import Path

REE_V3 = Path("/Users/dgolden/REE_Working/ree-v3")
sys.path.insert(0, str(REE_V3))

import torch  # noqa: E402
import torch.nn.functional as F  # noqa: E402

from ree_core.predictors.e1_deep import ContextMemory  # noqa: E402

SEEDS = [42, 7, 13, 100, 200, 1, 2, 3, 4, 5]
N_WRITES = 3000
SWITCH_EVERY = 5
LATENT_DIM = 64
MEMORY_DIM = 128
NUM_SLOTS = 16
JITTER = 0.02
TRAIN_STEPS = 4000

MODES = {
    "LEGACY":     dict(write_usage_balancing=False, write_selection="argmin"),
    "BIAS":       dict(write_usage_balancing=True,  write_selection="argmin"),
    "REFRACTORY": dict(write_usage_balancing=False, write_selection="refractory",
                       write_refractory_k=2),
}

# MECH-152's own asserted band (claims.yaml notes, EXQ-194 criteria):
#   hazard-gradient context   -> w_harm > 0.8
#   resource-proximate context-> w_harm < 0.5
BAND_HI = 0.8
# Train PAST the band, not to it: MSE on a sigmoid asymptotes toward its target
# from below, so training to 0.8 exactly clips band_met at the threshold and
# reports a false negative (observed on the first run: REFRACTORY seed 13 hit
# 0.79996 / 0.20004 and scored band_met False). 0.95 / 0.05 leaves headroom so
# the band test measures ATTAINABILITY rather than convergence margin.
TRAIN_HI = 0.95
BAND_LO = 0.5



def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy) if dx > 0 and dy > 0 else float("nan")


def build_stream(seed):
    """Two low-variance context clusters, switching every SWITCH_EVERY writes."""
    g = torch.Generator().manual_seed(seed)
    base_hazard = torch.randn(LATENT_DIM, generator=g)
    base_resource = torch.randn(LATENT_DIM, generator=g)
    states, labels = [], []
    for i in range(N_WRITES):
        ctx = (i // SWITCH_EVERY) % 2
        base = base_hazard if ctx == 0 else base_resource
        states.append(base + JITTER * torch.randn(LATENT_DIM, generator=g))
        labels.append(ctx)
    return torch.stack(states), torch.tensor(labels)


def nmi(labels, slots, num_slots):
    """Normalised mutual information I(C;S) / sqrt(H(C) H(S)), in bits."""
    n = len(labels)
    joint = torch.zeros(2, num_slots)
    for c, s in zip(labels.tolist(), slots):
        joint[c, s] += 1.0
    joint /= n
    p_c = joint.sum(1)
    p_s = joint.sum(0)

    def ent(p):
        p = p[p > 0]
        return float(-(p * torch.log2(p)).sum())

    h_c, h_s = ent(p_c), ent(p_s)
    mi = 0.0
    for c in range(2):
        for s in range(num_slots):
            if joint[c, s] > 0:
                mi += float(joint[c, s]) * math.log2(
                    float(joint[c, s]) / (float(p_c[c]) * float(p_s[s]))
                )
    if h_c <= 0 or h_s <= 0:
        return 0.0
    return mi / math.sqrt(h_c * h_s)


def js_divergence(labels, slots, num_slots):
    """Jensen-Shannon divergence (bits) between the two contexts' slot dists."""
    counts = torch.zeros(2, num_slots)
    for c, s in zip(labels.tolist(), slots):
        counts[c, s] += 1.0
    p = counts[0] / max(float(counts[0].sum()), 1.0)
    q = counts[1] / max(float(counts[1].sum()), 1.0)
    m = 0.5 * (p + q)

    def kl(a, b):
        mask = a > 0
        return float((a[mask] * torch.log2(a[mask] / b[mask])).sum())

    return 0.5 * kl(p, m) + 0.5 * kl(q, m)


def exclusive_slots(labels, slots, num_slots):
    counts = torch.zeros(2, num_slots)
    for c, s in zip(labels.tolist(), slots):
        counts[c, s] += 1.0
    return int(((counts[0] > 0) ^ (counts[1] > 0)).sum())


def read_cue_context(cm, queries):
    """The REAL read path of extract_cue_context()'s legacy (non-tagger) branch,
    with world_query_proj replaced by query_proj since the probe drives
    ContextMemory directly rather than a full E1DeepPredictor. Structurally
    identical: a learned linear map into memory_dim, then q.k softmax over
    key_proj(memory), then value_proj / output_proj. The convexity argument in
    section 2a -- the whole basis of the tight bound -- depends only on the
    softmax being a softmax, so this substitution cannot change the finding.
    """
    memory = cm.memory
    q = cm.query_proj(queries).unsqueeze(1)
    k = cm.key_proj(memory).unsqueeze(0).expand(queries.shape[0], -1, -1)
    v = cm.value_proj(memory).unsqueeze(0).expand(queries.shape[0], -1, -1)
    scores = torch.bmm(q, k.transpose(1, 2)) / (cm.memory_dim ** 0.5)
    weights = F.softmax(scores, dim=-1)
    return cm.output_proj(torch.bmm(weights, v).squeeze(1)), weights.squeeze(1)


def run_cell(mode_name, mode_kwargs, seed):
    torch.manual_seed(seed)
    cm = ContextMemory(latent_dim=LATENT_DIM, memory_dim=MEMORY_DIM,
                       num_slots=NUM_SLOTS, **mode_kwargs)
    states, labels = build_stream(seed)

    # --- drive the real write path, recording the address of every write ---
    addressed = []
    orig_record = cm._record_write

    def spy(idx):
        addressed.append(int(idx))
        orig_record(idx)

    cm._record_write = spy
    for i in range(N_WRITES):
        cm.write(states[i:i + 1])
    cm._record_write = orig_record

    n_distinct = len(set(addressed))

    # --- section 2a tight bound on attainable w_harm, cue_terrain_proj at init ---
    torch.manual_seed(seed + 1)
    cue_terrain_proj = torch.nn.Linear(LATENT_DIM, 2)
    with torch.no_grad():
        per_slot = cm.output_proj(cm.value_proj(cm.memory))
        w_slots = torch.sigmoid(cue_terrain_proj(per_slot))[:, 0]
        bound_untrained = float(w_slots.max() - w_slots.min())

    # --- best-case BETWEEN-CONTEXT depth through the real read path ---
    # Only cue_terrain_proj trains; the bank is frozen (the write mode's product)
    # and the tagger is bypassed. This is the section 2c method lifted from
    # per-slot targets to per-CONTEXT targets -- the step 2c did not take.
    g = torch.Generator().manual_seed(seed + 2)
    # TRAIN / HELD-OUT SPLIT (added after the first tagger run).
    # The tagger arm below is an MLP (~2.6k params) trained 4000 steps; fitting
    # it on the SAME vectors it is scored on would let it memorise the 512 eval
    # states and report a depth that reflects capacity, not the bank. The first
    # run did exactly that and returned the training target (0.9000) in 30/30
    # cells -- a saturated, non-discriminating result. Both arms are now fit on
    # `*_tr` and scored on the DISJOINT `*_te`, drawn from the same two clusters.
    # (The legacy arm is a single Linear(64,2), 130 params, and did NOT saturate,
    # so it was never at real risk -- but it is split too, for symmetry.)
    _haz_all = states[labels == 0]
    _res_all = states[labels == 1]
    hazard_tr, hazard_te = _haz_all[:256], _haz_all[256:512]
    resource_tr, resource_te = _res_all[:256], _res_all[256:512]
    eval_hazard, eval_resource = hazard_tr, resource_tr
    with torch.no_grad():
        ctx_hazard, w_hazard = read_cue_context(cm, eval_hazard)
        ctx_resource, w_resource = read_cue_context(cm, eval_resource)

    opt = torch.optim.Adam(cue_terrain_proj.parameters(), lr=0.01)
    tgt_hi = torch.full((ctx_hazard.shape[0],), TRAIN_HI)
    tgt_lo = torch.full((ctx_resource.shape[0],), 1.0 - TRAIN_HI)
    for _ in range(TRAIN_STEPS):
        opt.zero_grad()
        wh = torch.sigmoid(cue_terrain_proj(ctx_hazard))[:, 0]
        wr = torch.sigmoid(cue_terrain_proj(ctx_resource))[:, 0]
        loss = F.mse_loss(wh, tgt_hi) + F.mse_loss(wr, tgt_lo)
        loss.backward()
        opt.step()

    with torch.no_grad():
        ctx_hazard_te, _ = read_cue_context(cm, hazard_te)
        ctx_resource_te, _ = read_cue_context(cm, resource_te)
        wh = float(torch.sigmoid(cue_terrain_proj(ctx_hazard_te))[:, 0].mean())
        wr = float(torch.sigmoid(cue_terrain_proj(ctx_resource_te))[:, 0].mean())


    # --- SAME best-case depth, but through the SD-016 cue_slot_tagger read path ---
    # The redesign's production config runs cue_slot_tagger=True, which REPLACES
    # the q.k attention above with a learned MLP z_world -> slot logits
    # (e1_deep.py:513-517, Linear(world_dim,32) -> ReLU -> Linear(32,num_slots)),
    # trained by the terrain_loss gradient. That gives the SELECTION a learned
    # route from context, which the frozen q.k path does not have.
    #
    # This arm therefore tests the load-bearing objection to the legacy-path
    # result: if the tagger can route the two contexts to different slots by
    # itself, MECH-152's measurability stops depending on how the WRITE path
    # distributed content, and the write-path gate is much weaker than assumed.
    # Trained jointly with cue_terrain_proj, best-case, on the same frozen bank.
    torch.manual_seed(seed + 3)
    tagger = torch.nn.Sequential(
        torch.nn.Linear(LATENT_DIM, 32),
        torch.nn.ReLU(),
        torch.nn.Linear(32, NUM_SLOTS),
    )
    ct_proj_t = torch.nn.Linear(LATENT_DIM, 2)
    opt_t = torch.optim.Adam(
        list(tagger.parameters()) + list(ct_proj_t.parameters()), lr=0.01)
    with torch.no_grad():
        v_slots = cm.value_proj(cm.memory)          # [num_slots, memory_dim]
    for _ in range(TRAIN_STEPS):
        opt_t.zero_grad()
        wts_h = F.softmax(tagger(eval_hazard), dim=-1)
        wts_r = F.softmax(tagger(eval_resource), dim=-1)
        ch = cm.output_proj(wts_h @ v_slots)
        cr = cm.output_proj(wts_r @ v_slots)
        wh_t = torch.sigmoid(ct_proj_t(ch))[:, 0]
        wr_t = torch.sigmoid(ct_proj_t(cr))[:, 0]
        loss_t = (F.mse_loss(wh_t, tgt_hi) + F.mse_loss(wr_t, tgt_lo))
        loss_t.backward()
        opt_t.step()
    with torch.no_grad():
        wts_h = F.softmax(tagger(hazard_te), dim=-1)
        wts_r = F.softmax(tagger(resource_te), dim=-1)
        ch = cm.output_proj(wts_h @ v_slots)
        cr = cm.output_proj(wts_r @ v_slots)
        wh_tag = float(torch.sigmoid(ct_proj_t(ch))[:, 0].mean())
        wr_tag = float(torch.sigmoid(ct_proj_t(cr))[:, 0].mean())
        tagger_sel_l1 = float((wts_h.mean(0) - wts_r.mean(0)).abs().sum())


    # --- ATTRIBUTION CONTROL: the same tagger arm on a RANDOM bank ---
    # The tagger arm above clears MECH-152's band on every write mode, including
    # LEGACY cells with a 1-slot bank. That raises the question the redesign has
    # to answer before it can interpret ANY positive result: is the depth coming
    # from the cue-indexed MEMORY, or purely from the tagger's own capacity to
    # split two input clusters?
    #
    # This control answers it directly. Same tagger, same head, same training,
    # same held-out scoring -- but the slot bank is REPLACED with random values
    # carrying no written content at all. If depth survives, the DV is not
    # measuring a cue-indexed retrieval pathway and a positive MECH-152 result
    # would be uninterpretable regardless of the write path.
    torch.manual_seed(seed + 4)
    rand_bank = torch.randn_like(cm.memory) * float(cm.memory.std())
    tagger_c = torch.nn.Sequential(
        torch.nn.Linear(LATENT_DIM, 32),
        torch.nn.ReLU(),
        torch.nn.Linear(32, NUM_SLOTS),
    )
    ct_proj_c = torch.nn.Linear(LATENT_DIM, 2)
    opt_c = torch.optim.Adam(
        list(tagger_c.parameters()) + list(ct_proj_c.parameters()), lr=0.01)
    with torch.no_grad():
        v_rand = cm.value_proj(rand_bank)
    for _ in range(TRAIN_STEPS):
        opt_c.zero_grad()
        ch = cm.output_proj(F.softmax(tagger_c(hazard_tr), dim=-1) @ v_rand)
        cr = cm.output_proj(F.softmax(tagger_c(resource_tr), dim=-1) @ v_rand)
        loss_c = (F.mse_loss(torch.sigmoid(ct_proj_c(ch))[:, 0], tgt_hi)
                  + F.mse_loss(torch.sigmoid(ct_proj_c(cr))[:, 0], tgt_lo))
        loss_c.backward()
        opt_c.step()
    with torch.no_grad():
        ch = cm.output_proj(F.softmax(tagger_c(hazard_te), dim=-1) @ v_rand)
        cr = cm.output_proj(F.softmax(tagger_c(resource_te), dim=-1) @ v_rand)
        wh_rand = float(torch.sigmoid(ct_proj_c(ch))[:, 0].mean())
        wr_rand = float(torch.sigmoid(ct_proj_c(cr))[:, 0].mean())

    # how distinguishable are the two contexts' READ distributions at all?
    with torch.no_grad():
        sel_l1 = float((w_hazard.mean(0) - w_resource.mean(0)).abs().sum())
        ctx_sep = float((ctx_hazard.mean(0) - ctx_resource.mean(0)).norm())

    return {
        "mode": mode_name,
        "seed": seed,
        "n_distinct": n_distinct,
        "nmi_context_slot": round(nmi(labels, addressed, NUM_SLOTS), 4),
        "js_divergence_bits": round(js_divergence(labels, addressed, NUM_SLOTS), 4),
        "exclusive_slots": exclusive_slots(labels, addressed, NUM_SLOTS),
        "bound_untrained": round(bound_untrained, 6),
        "read_selection_l1_gap": round(sel_l1, 6),
        "cue_context_separation": round(ctx_sep, 6),
        "w_harm_hazard": round(wh, 4),
        "w_harm_resource": round(wr, 4),
        "depth_bestcase": round(wh - wr, 4),
        "band_met": bool(wh > BAND_HI and wr < BAND_LO),
        "w_harm_hazard_tagger": round(wh_tag, 4),
        "w_harm_resource_tagger": round(wr_tag, 4),
        "depth_bestcase_tagger": round(wh_tag - wr_tag, 4),
        "tagger_selection_l1_gap": round(tagger_sel_l1, 6),
        "band_met_tagger": bool(wh_tag > BAND_HI and wr_tag < BAND_LO),
        "depth_randombank": round(wh_rand - wr_rand, 4),
        "band_met_randombank": bool(wh_rand > BAND_HI and wr_rand < BAND_LO),
    }


def main():
    rows = []
    for mode_name, kwargs in MODES.items():
        for seed in SEEDS:
            row = run_cell(mode_name, kwargs, seed)
            rows.append(row)
            print("{:11s} seed {:3d}  slots {:2d}  NMI {:.4f}  JS {:.4f}  "
                  "excl {:2d}  bound {:.4f}  depth {:+.4f}  band {}".format(
                      row["mode"], row["seed"], row["n_distinct"],
                      row["nmi_context_slot"], row["js_divergence_bits"],
                      row["exclusive_slots"], row["bound_untrained"],
                      row["depth_bestcase"], row["band_met"])
                  + "  | TAGGER {:+.4f} {}  | RANDBANK {:+.4f} {}".format(
                      row["depth_bestcase_tagger"], row["band_met_tagger"],
                      row["depth_randombank"], row["band_met_randombank"]))

    print("\n=== per-mode summary (median over {} seeds) ===".format(len(SEEDS)))
    summary = {}
    for mode_name in MODES:
        sub = [r for r in rows if r["mode"] == mode_name]

        def med(key):
            vals = sorted(r[key] for r in sub)
            return vals[len(vals) // 2]

        summary[mode_name] = {
            "n_distinct_median": med("n_distinct"),
            "n_distinct_all": [r["n_distinct"] for r in sub],
            "nmi_median": round(med("nmi_context_slot"), 4),
            "nmi_all": [r["nmi_context_slot"] for r in sub],
            "js_median": round(med("js_divergence_bits"), 4),
            "exclusive_slots_all": [r["exclusive_slots"] for r in sub],
            "depth_bestcase_median": round(med("depth_bestcase"), 4),
            "depth_bestcase_all": [r["depth_bestcase"] for r in sub],
            "band_met_n_seeds": sum(1 for r in sub if r["band_met"]),
            "depth_tagger_median": round(med("depth_bestcase_tagger"), 4),
            "depth_tagger_all": [r["depth_bestcase_tagger"] for r in sub],
            "band_met_tagger_n_seeds": sum(1 for r in sub if r["band_met_tagger"]),
            "depth_randombank_median": round(med("depth_randombank"), 4),
            "depth_randombank_all": [r["depth_randombank"] for r in sub],
            "band_met_randombank_n_seeds": sum(1 for r in sub if r["band_met_randombank"]),
        }
        s = summary[mode_name]
        print("{:11s} legacy-read depth {:+.4f} band {}/{}   |   "
              "tagger-read depth {:+.4f} band {}/{}".format(
                  mode_name, s["depth_bestcase_median"], s["band_met_n_seeds"],
                  len(SEEDS), s["depth_tagger_median"],
                  s["band_met_tagger_n_seeds"], len(SEEDS))
              + "   |   RANDOM-BANK control depth {:+.4f} band {}/{}".format(
                  s["depth_randombank_median"],
                  s["band_met_randombank_n_seeds"], len(SEEDS)))


    # --- does ANY write-path DV predict MECH-152 measurability? ---
    # This is the question the pending governance call actually turns on.
    # V3-EXQ-943 adjudicated on occupancy; MECH-152's DV is between-context
    # modulation depth. If occupancy does not predict depth, an occupancy PASS
    # cannot license a MECH-152 run, whichever mode wins.
    print("\n=== does any write-path DV predict MECH-152 depth? (all cells) ===")
    depth = [r["depth_bestcase"] for r in rows]
    predictors = {
        "n_distinct (943's DV)": [r["n_distinct"] for r in rows],
        "nmi_context_slot":      [r["nmi_context_slot"] for r in rows],
        "js_divergence_bits":    [r["js_divergence_bits"] for r in rows],
        "exclusive_slots":       [r["exclusive_slots"] for r in rows],
        "bound_untrained":       [r["bound_untrained"] for r in rows],
        "cue_context_separation": [r["cue_context_separation"] for r in rows],
    }
    tagger_depth = [r["depth_bestcase_tagger"] for r in rows]
    corrs = {}
    for name, xs in predictors.items():
        r = pearson(xs, depth)
        corrs[name] = round(r, 4)
        print("  r(depth, {:24s}) = {:+.4f}".format(name, r))
    r_tag = pearson([r["n_distinct"] for r in rows], tagger_depth)
    corrs["n_distinct__vs__tagger_depth"] = round(r_tag, 4)
    r_lt = pearson(depth, tagger_depth)
    corrs["legacy_depth__vs__tagger_depth"] = round(r_lt, 4)
    print("  r(TAGGER depth, n_distinct)          = {:+.4f}".format(r_tag))
    print("  r(TAGGER depth, legacy depth)        = {:+.4f}".format(r_lt))

    out = Path(__file__).with_suffix(".results.json")
    caveats = {
        "nmi_context_slot": "DESCRIPTIVE ONLY -- NOT a valid addressing measure. "
                            "I(slot;context) against chance is the trap V3-EXQ-946's "
                            "driver header identifies: a period-16 clock or a "
                            "period-(k+1) cycle can produce non-zero MI purely by "
                            "aligning with the context block schedule, with zero "
                            "context-sensitivity in the addressing rule. Use "
                            "V3-EXQ-946's blockwise-permutation order-only null "
                            "instead, which supersedes this column.",
        "js_divergence_bits": "DESCRIPTIVE ONLY -- same defect as nmi_context_slot.",
        "depth_bestcase / depth_bestcase_tagger / depth_randombank":
            "UPPER BOUNDS, not predictions. Trained best-case (4000 Adam steps, "
            "frozen bank, no competing objectives) and scored on held-out samples. "
            "Establishes what the DV CAN reach, not what a real phased training "
            "loop does reach.",
        "r(depth, n_distinct) = -0.53":
            "CONFOUNDED -- do not quote. Low-occupancy cells cluster on seeds "
            "42/13/4, which also have the largest bound_untrained. Use the "
            "within-stratum statement instead: among cells at 16/16 occupancy, "
            "depth ranges 0.0000 to 0.7310.",
    }
    out.write_text(json.dumps({"rows": rows, "summary": summary,
                               "column_caveats": caveats,
                               "correlations_with_depth": corrs,
                               "config": {"n_writes": N_WRITES,
                                          "switch_every": SWITCH_EVERY,
                                          "jitter": JITTER,
                                          "num_slots": NUM_SLOTS,
                                          "train_steps": TRAIN_STEPS,
                                          "seeds": SEEDS}}, indent=2))
    print("\nwrote {}".format(out))


if __name__ == "__main__":
    main()
