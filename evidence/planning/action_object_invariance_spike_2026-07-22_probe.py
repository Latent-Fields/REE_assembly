"""SCOPING SPIKE (probe, not an experiment): is E2's action-object embedding's
near action-invariance a DEFECT or an intended consequence-space property?

Reading (a) NOT A DEFECT: O is consequence space. Actions with the SAME
consequence should embed alike; actions with DIFFERENT consequences should
embed differently. Predicts consequence-STRUCTURED variance.

Reading (b) IS A DEFECT: coordinates barely move under the thing being
optimised. Predicts near-zero action variance regardless of consequence.

Measurements, per arm (untrained / warmed):
  M0  gradient reachability of action_object_head
  M1  variance decomposition of ao over (state, action)
  M2  action-class recoverability by a LINEAR probe on state-centred ao
  M3  DECISIVE: does D_ao track D_consequence? Mantel-style Spearman, plus the
      sharp same-consequence-vs-different-consequence contrast
  M4  same measurements on world_forward output (SD-056 collapse site) as a
      calibration reference

ASCII-only output.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import numpy as np
import torch

REPO = Path("/Users/dgolden/REE_Working/ree-v3")
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "experiments"))

from ree_core.agent import REEAgent  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402

SEED = 42
WORLD_DIM = SELF_DIM = 32
N_STATES = 120
WARMUP_EPISODES = 40
STEPS_PER_EPISODE = 200


def make_env(seed=SEED):
    return CausalGridWorldV2(size=6, seed=seed)


def make_agent(env):
    cfg = REEConfig.from_dims(
        body_obs_dim=env.body_obs_dim,
        world_obs_dim=env.world_obs_dim,
        action_dim=env.action_dim,
        alpha_world=0.9,
        world_dim=WORLD_DIM,
        self_dim=SELF_DIM,
    )
    return REEAgent(cfg)


# ---------------------------------------------------------------- collection

def collect_states(agent, env, n_states):
    """Roll out; capture (z_world, env snapshot) at each visited state."""
    from _harness import StepHarness

    harness = StepHarness(agent, env, train_mode=False)
    out = []
    _, obs_dict = env.reset()
    agent.reset()
    harness.reset()
    steps = 0
    # Force periodic resets so the state sample is not one short trajectory --
    # otherwise between-state variance is an artefact of sampling one corner.
    reset_every = max(5, n_states // 12)
    while len(out) < n_states and steps < n_states * 6:
        snapshot = copy.deepcopy(env)
        res = harness.step(obs_dict)
        z_world = res.latent.z_world.detach().clone()
        out.append((z_world, snapshot))
        obs_dict = res.next_obs_dict
        steps += 1
        if getattr(res, "done", False) or steps % reset_every == 0:
            _, obs_dict = env.reset()
            agent.reset()
            harness.reset()
    return out[:n_states]


def consequence_vector(snapshot, a, action_dim):
    """Ground-truth consequence of taking action a from this exact env state.

    Uses a deepcopy of the env so each action is evaluated from the SAME state.
    Returns (dense consequence vector, discrete consequence key).
    """
    env2 = copy.deepcopy(snapshot)
    pos0 = (float(env2.agent_x), float(env2.agent_y))
    onehot = torch.zeros(action_dim)
    onehot[a] = 1.0
    flat, harm, done, info, obs_dict = env2.step(onehot)
    pos1 = (float(env2.agent_x), float(env2.agent_y))
    dpos = (pos1[0] - pos0[0], pos1[1] - pos0[1])

    dense = np.concatenate([
        np.asarray(dpos, dtype=np.float64),
        np.asarray([float(harm)], dtype=np.float64),
        np.asarray(flat, dtype=np.float64).ravel(),
    ])
    # Discrete key: two actions share it iff they produce the same displacement
    # and the same transition type -- i.e. genuinely the same consequence.
    # Deliberately coarse: two actions share a key iff they move the agent the
    # same way AND produce the same transition type. Float harm is excluded so
    # sampling noise does not split otherwise-identical consequences.
    key = (dpos, str(info.get("transition_type", "")))
    return dense, key


def gather(agent, env, n_states):
    action_dim = env.action_dim
    states = collect_states(agent, env, n_states)
    AO, WF, CONS, KEYS, ZW = [], [], [], [], []
    with torch.no_grad():
        for z_world, snap in states:
            ZW.append(z_world[0].numpy())
            ao_s, wf_s, cons_s, key_s = [], [], [], []
            for a in range(action_dim):
                onehot = torch.zeros(1, action_dim)
                onehot[0, a] = 1.0
                ao_s.append(agent.e2.action_object(z_world, onehot)[0].numpy())
                wf_s.append(agent.e2.world_forward(z_world, onehot)[0].numpy())
                dense, key = consequence_vector(snap, a, action_dim)
                cons_s.append(dense)
                key_s.append(key)
            AO.append(np.stack(ao_s))
            WF.append(np.stack(wf_s))
            CONS.append(np.stack(cons_s))
            KEYS.append(key_s)
    return np.stack(AO), np.stack(WF), np.stack(CONS), KEYS, np.stack(ZW)


# ---------------------------------------------------------------- measures

def m1_variance_decomposition(X):
    """X: [S, A, D]. Between-state vs within-state(action) variance."""
    per_state_mean = X.mean(axis=1, keepdims=True)          # [S,1,D]
    between = per_state_mean[:, 0, :].var(axis=0).sum()      # over states
    within = (X - per_state_mean).var(axis=(0, 1)).sum()     # action-driven
    grand_mean = X.mean(axis=(0, 1))
    dev = X - per_state_mean
    # AMPLITUDE: action-driven displacement relative to the constant offset the
    # embedding rides on. This is what decides whether a downstream argmax can
    # see the action at all.
    return {
        "between_state_var": float(between),
        "within_state_action_var": float(within),
        "action_var_fraction": float(within / (within + between + 1e-30)),
        "mean_per_dim_action_std": float(dev.std(axis=(0, 1)).mean()),
        "grand_mean_norm": float(np.linalg.norm(grand_mean)),
        "mean_action_deviation_norm": float(np.linalg.norm(dev, axis=-1).mean()),
        "action_signal_to_offset_ratio": float(
            np.linalg.norm(dev, axis=-1).mean() / (np.linalg.norm(grand_mean) + 1e-30)
        ),
    }


def m2_linear_probe(X, seed=0):
    """Can a LINEAR probe recover the action class from state-centred ao?

    State-centring removes the state component, isolating the action signal.
    Multinomial logistic regression via plain gradient descent (no sklearn).
    """
    S, A, D = X.shape
    Xc = (X - X.mean(axis=1, keepdims=True)).reshape(S * A, D)
    y = np.tile(np.arange(A), S)
    # standardise so a tiny-amplitude but present signal is not a scaling artefact
    sd = Xc.std(axis=0)
    Xc = Xc / np.where(sd > 1e-12, sd, 1.0)
    rng = np.random.default_rng(seed)
    idx = rng.permutation(S)
    n_tr = int(S * 0.7)
    tr = np.concatenate([np.arange(i * A, (i + 1) * A) for i in idx[:n_tr]])
    te = np.concatenate([np.arange(i * A, (i + 1) * A) for i in idx[n_tr:]])

    Xt = torch.tensor(Xc[tr], dtype=torch.float32)
    yt = torch.tensor(y[tr], dtype=torch.long)
    Xe = torch.tensor(Xc[te], dtype=torch.float32)
    ye = torch.tensor(y[te], dtype=torch.long)
    W = torch.zeros(D, A, requires_grad=True)
    b = torch.zeros(A, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=0.05)
    for _ in range(600):
        opt.zero_grad()
        loss = torch.nn.functional.cross_entropy(Xt @ W + b, yt)
        loss.backward()
        opt.step()
    with torch.no_grad():
        acc = float(((Xe @ W + b).argmax(dim=1) == ye).float().mean())
    return {"linear_probe_test_acc": acc, "chance": 1.0 / A}


def _spearman(u, v):
    def rank(x):
        order = np.argsort(x)
        r = np.empty_like(order, dtype=np.float64)
        r[order] = np.arange(len(x))
        return r
    ru, rv = rank(u), rank(v)
    ru -= ru.mean(); rv -= rv.mean()
    den = np.sqrt((ru ** 2).sum() * (rv ** 2).sum())
    return float((ru * rv).sum() / den) if den > 0 else 0.0


def m3_consequence_structure(X, CONS, KEYS):
    """DECISIVE. Does embedding distance track consequence distance?"""
    S, A, _ = X.shape
    d_emb, d_con, same_flag = [], [], []
    for s in range(S):
        # normalise the consequence vector scale per state so distances are
        # comparable across states
        for i in range(A):
            for j in range(i + 1, A):
                d_emb.append(np.linalg.norm(X[s, i] - X[s, j]))
                d_con.append(np.linalg.norm(CONS[s, i] - CONS[s, j]))
                same_flag.append(KEYS[s][i] == KEYS[s][j])
    d_emb = np.asarray(d_emb); d_con = np.asarray(d_con)
    same = np.asarray(same_flag, dtype=bool)
    diff = ~same

    out = {
        "n_pairs": int(len(d_emb)),
        "n_same_consequence_pairs": int(same.sum()),
        "n_diff_consequence_pairs": int(diff.sum()),
        "spearman_d_emb_vs_d_consequence": _spearman(d_emb, d_con),
    }
    if same.sum() > 0 and diff.sum() > 0:
        ms, md = float(d_emb[same].mean()), float(d_emb[diff].mean())
        pooled = float(d_emb.std() + 1e-30)
        out.update({
            "mean_d_emb_same_consequence": ms,
            "mean_d_emb_diff_consequence": md,
            "separation_ratio_diff_over_same": float(md / (ms + 1e-30)),
            "cohens_d_diff_minus_same": float((md - ms) / pooled),
        })
    return out


def m5_state_dependence(X):
    """Is the embedding a function of the ACTION ALONE?

    CONTROL for M3. If ao ~= g(action) with negligible state dependence, the
    within-state pairwise-distance matrix is the SAME for every state, so it
    CANNOT be consequence-structured -- consequences vary by state while the
    embedding does not. Any M3 signal is then an artefact of how the
    same/different labels redistribute over a FIXED distance matrix.

    R2 = fraction of ao variance explained by a per-action-class mean lookup.
    """
    S, A, D = X.shape
    per_action_mean = X.mean(axis=0)                       # [A, D] -- g(action)
    resid = X - per_action_mean[None, :, :]
    ss_res = float((resid ** 2).sum())
    ss_tot = float(((X - X.mean(axis=(0, 1))) ** 2).sum())
    r2_action_only = 1.0 - ss_res / (ss_tot + 1e-30)

    # Stability of the pairwise-distance matrix across states.
    dmats = []
    for s in range(S):
        dmats.append([np.linalg.norm(X[s, i] - X[s, j])
                      for i in range(A) for j in range(i + 1, A)])
    dmats = np.asarray(dmats)                              # [S, A*(A-1)/2]
    cv = dmats.std(axis=0) / (dmats.mean(axis=0) + 1e-30)
    return {
        "r2_explained_by_action_alone": float(r2_action_only),
        "pairdist_across_state_cv_mean": float(cv.mean()),
        "pairdist_across_state_cv_max": float(cv.max()),
    }


def m6_within_pair_consequence_corr(X, CONS):
    """M3 with action-pair identity partialled out.

    For each FIXED action pair (i,j), correlate d_emb vs d_consequence ACROSS
    states. This removes the fixed-distance-matrix artefact entirely: it asks
    whether, for the same two actions, the embedding moves them apart more when
    their consequences differ more.
    """
    S, A, _ = X.shape
    per_pair = {}
    for i in range(A):
        for j in range(i + 1, A):
            de = np.array([np.linalg.norm(X[s, i] - X[s, j]) for s in range(S)])
            dc = np.array([np.linalg.norm(CONS[s, i] - CONS[s, j]) for s in range(S)])
            per_pair["%d-%d" % (i, j)] = {
                "spearman": _spearman(de, dc),
                "d_emb_cv": float(de.std() / (de.mean() + 1e-30)),
            }
    vals = [v["spearman"] for v in per_pair.values()]
    return {
        "per_pair": per_pair,
        "mean_within_pair_spearman": float(np.mean(vals)),
        "max_abs_within_pair_spearman": float(np.max(np.abs(vals))),
        "mean_d_emb_cv_within_pair": float(
            np.mean([v["d_emb_cv"] for v in per_pair.values()])),
    }


def m0_gradient_reachability(agent, env):
    """Does ANY standard training path put gradient into action_object_head?"""
    from _harness import StepHarness
    from experiments._lib.goal_pipeline_tier1 import warmup_train  # noqa

    head = agent.e2.action_object_head
    before = [p.detach().clone() for p in head.parameters()]
    return before


# ---------------------------------------------------------------- driver

def run_arm(label, warm_episodes):
    torch.manual_seed(SEED)
    np.random.seed(SEED)
    env = make_env()
    agent = make_agent(env)

    head_before = [p.detach().clone() for p in agent.e2.action_object_head.parameters()]

    if warm_episodes > 0:
        from _lib.goal_pipeline_tier1 import warmup_train
        warmup_train(agent, env, num_episodes=warm_episodes,
                     steps_per_episode=STEPS_PER_EPISODE,
                     label="ao-spike %s" % label)

    head_after = [p.detach().clone() for p in agent.e2.action_object_head.parameters()]
    head_delta = float(sum(((b - a) ** 2).sum() for b, a in zip(head_before, head_after)) ** 0.5)

    agent.eval()
    AO, WF, CONS, KEYS, ZW = gather(agent, env, N_STATES)

    np.savez(Path(__file__).with_name("raw_%s.npz" % label),
             AO=AO, WF=WF, CONS=CONS, ZW=ZW)

    return {
        "arm": label,
        "warmup_episodes": warm_episodes,
        "n_states": int(AO.shape[0]),
        "action_dim": int(AO.shape[1]),
        "action_object_dim": int(AO.shape[2]),
        "M0_action_object_head_param_delta_l2": head_delta,
        "zworld_control": {
            "zworld_total_var_across_states": float(ZW.var(axis=0).sum()),
            "zworld_mean_per_dim_std": float(ZW.std(axis=0).mean()),
            "zworld_mean_norm": float(np.linalg.norm(ZW, axis=1).mean()),
        },
        "ao": {
            "M1": m1_variance_decomposition(AO),
            "M2": m2_linear_probe(AO),
            "M3": m3_consequence_structure(AO, CONS, KEYS),
            "M5": m5_state_dependence(AO),
            "M6": m6_within_pair_consequence_corr(AO, CONS),
        },
        "world_forward_reference": {
            "M1": m1_variance_decomposition(WF),
            "M2": m2_linear_probe(WF),
            "M3": m3_consequence_structure(WF, CONS, KEYS),
            "M5": m5_state_dependence(WF),
            "M6": m6_within_pair_consequence_corr(WF, CONS),
        },
    }


def main():
    results = []
    for label, eps in [("untrained", 0), ("warmed_40ep", WARMUP_EPISODES)]:
        print("=== arm %s ===" % label, flush=True)
        results.append(run_arm(label, eps))
    out = Path(__file__).with_name("ao_invariance_spike_results.json")
    out.write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
