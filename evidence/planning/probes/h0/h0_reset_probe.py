"""H0 probe (bt0926-h0): is the episode reset (agent.reset(), DC-B R1) a hidden regime controller?

usage: python h0_reset_probe.py <repo_root> <arm> <seed> <ticks> [c_rate] [out_jsonl]
arms:
  A         standard agent.reset() at every env boundary (the imposed regime).
  B         body-only reset: snapshot every controller-state path that agent.reset() changes,
            call agent.reset(), restore those paths. Env layout + body (+ body-bound agent
            caches, see BODY rules) still reset. The restored set is DATA-DRIVEN: the diff of a
            generic plain-state walk of the agent before/after reset(), minus BODY and MEMORY
            rules below. Every restored / not-restored path is reported.
  C         B, plus a FULL controller reset (agent.reset() with BODY paths restored, i.e. the
            inverse of B) at random steps drawn from an independent RNG at rate c_rate
            (= A's env-boundary rate for that seed), uncorrelated with env boundaries.
  Bonly:<obj>  secondary: like A, but only controller paths passing through attribute <obj>
            (any path component) are restored (single-controller persistence; the "which controllers benefit" readout).
Ecology: the modetrace A1 config (dACC ON, cap 2.0, external_task_drive OFF), untrained agent,
CausalGridWorldV2(size=10, 3 hazards, 3 resources, max_episode_steps=100), hazard injected every
30 steps (as modetrace), world_dim=self_dim=32 (deployed), all four EMA reset-init knobs ON.
Harness-side only; no ree_core edit. ASCII output.
"""
import json, sys, copy, collections, re, random, time
root = sys.argv[1]; sys.path.insert(0, root)
arm = sys.argv[2]; seed = int(sys.argv[3]); ticks = int(sys.argv[4])
c_rate = float(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5] not in ("", "-") else 0.0
out_path = sys.argv[6] if len(sys.argv) > 6 else None
import torch, numpy as np
import torch.nn as nn
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from experiments._harness import StepHarness

K_ENDO = 8            # pre-registered: an exit is endogenous only if > K_ENDO steps from any boundary
MAX_EP = 100          # pre-registered episode length cap

torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
env = CausalGridWorldV2(seed=seed, size=10, num_hazards=3, num_resources=3, max_episode_steps=MAX_EP)
flags = dict(alpha_world=0.9, use_harm_stream=True, use_affective_harm_stream=True,
             use_amygdala_analog=True, use_cea_analog=True, use_broadcast_override=True,
             use_salience_coordinator=True, use_pag_freeze_gate=True, use_closure_operator=True,
             use_lateral_pfc_analog=True, use_habenula_decommit=True,
             use_dacc=True, salience_affinity_input_cap=2.0,
             use_zworld_ema_reset_init=True, use_zself_ema_reset_init=True,
             use_shared_ema_reset_init=True, use_zharm_ema_reset_init=True)
cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
    action_dim=env.action_dim, self_dim=32, world_dim=32,
    reafference_action_dim=env.action_dim, **flags)
agent = REEAgent(cfg)
assert agent.config.latent.use_zworld_ema_reset_init and agent.config.latent.use_zharm_ema_reset_init
coord = agent.salience
assert coord is not None and agent.dacc is not None

# ---------------------------------------------------------------- generic plain-state walk
SIZE_CAP = 20000  # elements; larger containers are fingerprinted, not copied (named as skipped)

def _plain(v, depth=0):
    if v is None or isinstance(v, (bool, int, float, str, complex, np.generic)):
        return True
    if isinstance(v, torch.Tensor):
        return not isinstance(v, nn.Parameter)
    if isinstance(v, np.ndarray):
        return True
    if depth > 4:
        return False
    if isinstance(v, (list, tuple, set, frozenset, collections.deque)):
        return all(_plain(x, depth + 1) for x in v)
    if isinstance(v, dict):
        return all(_plain(k, depth + 1) and _plain(x, depth + 1) for k, x in v.items())
    return False

def _size(v):
    if isinstance(v, torch.Tensor):
        return v.numel()
    if isinstance(v, np.ndarray):
        return v.size
    if isinstance(v, (list, tuple, set, frozenset, collections.deque)):
        return sum(_size(x) for x in v) + len(v)
    if isinstance(v, dict):
        return sum(_size(x) for x in v.values()) + len(v)
    return 1

def _copy(v):
    if isinstance(v, torch.Tensor):
        return v.detach().clone()
    if isinstance(v, np.ndarray):
        return v.copy()
    if isinstance(v, list):
        return [_copy(x) for x in v]
    if isinstance(v, tuple):
        return tuple(_copy(x) for x in v)
    if isinstance(v, collections.deque):
        return collections.deque((_copy(x) for x in v), maxlen=v.maxlen)
    if isinstance(v, dict):
        return type(v)((k, _copy(x)) for k, x in v.items()) if type(v) is dict else copy.copy(v)
    if isinstance(v, (set, frozenset)):
        return copy.copy(v)
    return v  # immutable scalars / str / None

def _eq(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, torch.Tensor):
        return a.shape == b.shape and a.dtype == b.dtype and bool(torch.equal(a, b))
    if isinstance(a, np.ndarray):
        return a.shape == b.shape and bool(np.array_equal(a, b))
    if isinstance(a, (list, tuple, collections.deque)):
        return len(a) == len(b) and all(_eq(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(_eq(a[k], b[k]) for k in a)
    try:
        r = a == b
        return bool(r)
    except Exception:
        return False

def _is_ree(o):
    m = type(o).__module__ or ""
    return m.startswith("ree_core") or m.startswith("experiments")

def walk(obj, path, out, seen, depth):
    if id(obj) in seen or depth > 4:
        return
    seen.add(id(obj))
    d = getattr(obj, "__dict__", None)
    if d is None:
        return
    items = [(k, v) for k, v in d.items() if k not in ("_parameters", "_modules", "_buffers", "config")]
    if isinstance(obj, nn.Module):
        items += [("_buffers." + k, v) for k, v in obj._buffers.items() if v is not None]
        items += [(k, v) for k, v in obj._modules.items() if v is not None]
    for k, v in items:
        p = path + (k,)
        if _plain(v):
            out[p] = v
        elif _is_ree(v) and not isinstance(v, (nn.Parameter,)):
            NODES[p] = v
            walk(v, p, out, seen, depth + 1)

def getp(p):
    o = agent
    for k in p[:-1]:
        o = getattr(o, k)
    last = p[-1]
    if last.startswith("_buffers."):
        return o._buffers[last[len("_buffers."):]]
    return getattr(o, last)

def setp(p, v):
    o = agent
    for k in p[:-1]:
        o = getattr(o, k)
    last = p[-1]
    if last.startswith("_buffers."):
        o._buffers[last[len("_buffers."):]] = v
    else:
        setattr(o, last, v)

NODES = {}

def snapshot():
    NODES.clear()
    raw = {}
    walk(agent, (), raw, set(), 0)
    snap = {}
    big = []
    for p, v in raw.items():
        if _size(v) > SIZE_CAP:
            big.append(p)
            continue
        snap[p] = _copy(v)
    return snap, big, dict(NODES)

# BODY rules: state bound to the old body / old layout / previous tick -- still reset in B.
BODY_TOP = {"_current_latent", "latent_stack", "e1", "clock", "theta_buffer", "multi_content_theta_packet",
            "last_theta_packet", "_step_count", "_harm_this_episode", "_committed_candidates",
            "_last_persistence_appraisal", "_harm_replay_buffer", "_last_action",
            "_last_e3_selection_result", "_last_e3_score_bias", "_committed_step_idx",
            "_committed_anchor_keys", "_cached_e1_prior", "_e1_predicted_next_z_self",
            "_tpj_predicted_z_self", "_zworld_visitation_buffer"}
BODY_E3 = {"_committed_trajectory", "_closure_committed_trajectory", "_closure_committed_active",
           "_persistent_committed_trajectory"}
BODY_RE = re.compile(r"(_prev(_|$)|prev_z|_last_output$|_last_tick$|_trigger_z_world$|held_policy)")
# MEMORY rules: episode-end WRITES (buffers that grow at a boundary), not controller clears.
MEMORY_TOP = {"sleep_loop", "exploration_buffer", "_exploration_buffer", "_mech287_episode_rows",
              "residue_field", "policy_chunking"}
MEMORY_RE = re.compile(r"(mech287|exploration|_episode_rows|episode_records)")

CACHE_RE = re.compile(r"(^_last_output$|^_[a-z0-9]+_last_[a-z_]+$|^_salience_last_tick$)")
DIAG_RE = re.compile(r"^_episode_")

def classify(p):
    top = p[0]
    if top in BODY_TOP or (top == "e3" and p[-1] in BODY_E3) or any(BODY_RE.search(c) for c in p):
        return "body"
    if top in MEMORY_TOP or MEMORY_RE.search("/".join(p)):
        return "memory"
    # per-tick output caches: rewritten every tick from current inputs (agent-level _x_last_y,
    # any sub-object _last_output). Not controller state.
    if CACHE_RE.search(top) or any(c == "_last_output" for c in p):
        return "cache"
    # per-episode instrument bookkeeping (MECH-287 _episode_* rows/counters)
    if any(DIAG_RE.search(c) for c in p):
        return "diagnostic"
    return "controller"

# ---------------------------------------------------------------- run
rng_c = random.Random(10_000 + seed)   # independent stream for arm C's forced resets
h = StepHarness(agent, env, train_mode=True, seed=seed)
flat, obs = env.reset(); agent.reset(); h.reset()

reset_paths = collections.Counter()      # path -> times changed by reset()
restore_skipped = collections.Counter()
restored_paths = collections.Counter()
class_of = {}
big_skipped = set()
t_snap = []

def do_reset(kind, t):
    """kind: 'env' (env boundary) or 'forced' (arm C controller clear)."""
    t0 = time.time()
    before, big, nodes_before = snapshot()
    big_skipped.update(big)
    agent.reset()
    after, _, nodes_after = snapshot()
    # object-level replacement (reset() assigned a new object / None to a sub-object attribute):
    # restore the ORIGINAL object reference (reset() replaced it, so it is untouched), not its leaves.
    replaced = sorted([n for n, o in nodes_before.items() if nodes_after.get(n) is not o],
                      key=len)
    top_replaced = [n for n in replaced if not any(n[:len(r)] == r for r in replaced if r != n and len(r) < len(n))]
    def under(p):
        return any(p[:len(r)] == r and len(p) > len(r) for r in top_replaced)
    changed = [p for p in before if (p not in after) or not _eq(before[p], after[p])]
    changed = [p for p in changed if not under(p)] + top_replaced
    before = dict(before); before.update({n: nodes_before[n] for n in top_replaced})
    for p in changed:
        c = classify(p); class_of[p] = c
        if kind == "env":
            reset_paths[p] += 1
    if kind == "env":
        if arm == "A":
            restore = []
        elif arm in ("B", "C"):
            restore = [p for p in changed if class_of[p] == "controller"]
        elif arm.startswith("Bonly:"):
            want = arm.split(":", 1)[1]
            restore = [p for p in changed if class_of[p] == "controller" and want in p]
        else:
            raise SystemExit("bad arm")
    else:  # forced controller reset: undo the BODY + MEMORY part, keep the controller clear
        restore = [p for p in changed if class_of[p] != "controller"]
    for p in restore:
        try:
            setp(p, before[p] if p in top_replaced else _copy(before[p]))
            if kind == "env":
                restored_paths[p] += 1
        except AttributeError:
            restore_skipped[p] += 1   # parent object replaced by reset(); counted and reported
    t_snap.append(time.time() - t0)

inj = []
p1_pairs = []
t_start = time.time()
boundaries = []      # env steps t at whose END the env reset (next step is t+1)
forced = []
mode_seq = []        # per env step: current_mode after the step
commit_seq = []
freeze_seq = []
harm_neg = 0.0; benefit = 0.0; deaths = 0; ep_lens = []; ep_len = 0
dacc_pe = []
for t in range(ticks):
    if t % 30 == 15:
        if env._inject_external_hazard():
            inj.append(t)
    ax, ay = env.agent_x, env.agent_y
    dmin = min([abs(ax - hz[0]) + abs(ay - hz[1]) for hz in env.hazards] + [99])
    res = h.step(obs); obs = res.next_obs_dict
    zha = getattr(res.latent, "z_harm_a", None)
    if zha is not None:
        p1_pairs.append((dmin, float(zha.norm())))
    ep_len += 1
    hs = float(res.harm_signal)
    if hs < 0: harm_neg += -hs
    else: benefit += hs
    mode_seq.append(coord.current_mode)
    commit_seq.append(bool(agent.e3.get_commitment_state()["committed_now"]))
    freeze_seq.append(bool(agent.pag_freeze_gate._freeze_active))
    dacc_pe.append(float(coord._input_signals.get("dacc_pe", 0.0)))
    if res.done:
        if env.agent_health <= 0.0: deaths += 1
        ep_lens.append(ep_len); ep_len = 0
        boundaries.append(t)
        flat, obs = env.reset()
        do_reset("env", t)
        h.reset()
        mode_seq[-1] = (mode_seq[-1], coord.current_mode)   # (mode before reset, mode after reset)
        commit_seq[-1] = (commit_seq[-1], bool(agent.e3.get_commitment_state()["committed_now"]))
        freeze_seq[-1] = (freeze_seq[-1], bool(agent.pag_freeze_gate._freeze_active))
    if not res.done and arm == "C" and c_rate > 0 and rng_c.random() < c_rate:
        forced.append(t)
        do_reset("forced", t)
        mode_seq[-1] = (mode_seq[-1], coord.current_mode)
        commit_seq[-1] = (commit_seq[-1], bool(agent.e3.get_commitment_state()["committed_now"]))
        freeze_seq[-1] = (freeze_seq[-1], bool(agent.pag_freeze_gate._freeze_active))
if ep_len:
    ep_lens.append(ep_len)

def events(seq, is_regime):
    """Transitions into / out of the regime. seq entries are value or (before_reset, after_reset).
    Returns list of (t, 'enter'|'exit', via_reset_flag)."""
    ev = []; prev = None
    for t, x in enumerate(seq):
        if isinstance(x, tuple):
            a, b = x
            if prev is not None and is_regime(prev) != is_regime(a):
                ev.append((t, "enter" if is_regime(a) else "exit", False))
            if is_regime(a) != is_regime(b):
                ev.append((t, "enter" if is_regime(b) else "exit", True))
            prev = b
        else:
            if prev is not None and is_regime(prev) != is_regime(x):
                ev.append((t, "enter" if is_regime(x) else "exit", False))
            prev = x
    return ev

def occupancy(seq, is_regime):
    vals = [(x[0] if isinstance(x, tuple) else x) for x in seq]
    return sum(1 for v in vals if is_regime(v)) / max(1, len(vals))

def dist(t, pts):
    return min([abs(t - b) for b in pts] + [10 ** 9])

def score(seq, is_regime):
    ev = events(seq, is_regime)
    exits = [e for e in ev if e[1] == "exit"]
    enters = [e for e in ev if e[1] == "enter"]
    return dict(
        occupancy=round(occupancy(seq, is_regime), 4),
        n_enter=len(enters), n_exit=len(exits),
        n_exit_via_reset_call=sum(1 for e in exits if e[2]),
        n_exit_le_k_env_boundary=sum(1 for e in exits if dist(e[0], boundaries) <= K_ENDO),
        n_exit_endogenous_env=sum(1 for e in exits if dist(e[0], boundaries) > K_ENDO),
        n_exit_endogenous_any=sum(1 for e in exits if dist(e[0], boundaries + forced) > K_ENDO),
        n_exit_le_k_forced=sum(1 for e in exits if forced and dist(e[0], forced) <= K_ENDO),
        # C's forced clears: exits near a world change (env boundary or hazard injection) or not
        n_exit_at_forced_near_world_change=sum(1 for e in exits if e[2] and e[0] in forced
                                               and dist(e[0], boundaries + inj) <= K_ENDO),
        n_exit_at_forced_far_from_world_change=sum(1 for e in exits if e[2] and e[0] in forced
                                                   and dist(e[0], boundaries + inj) > K_ENDO),
        exit_ticks=[e[0] for e in exits][:200],
        n_enter_native=sum(1 for e in enters if not e[2]),
        n_enter_native_le_k_after_boundary=sum(1 for e in enters if not e[2] and
            min([e[0] - b for b in boundaries + forced if 0 < e[0] - b] + [10 ** 9]) <= K_ENDO),
        enter_ticks=[e[0] for e in enters if not e[2]][:200],
    )

def p1_stats():
    near = [n for d, n in p1_pairs if d <= 1]; far = [n for d, n in p1_pairs if d >= 2]
    if len(near) < 5 or len(far) < 5:
        return dict(n_near=len(near), n_far=len(far), dprime=None)
    mn, mf = sum(near) / len(near), sum(far) / len(far)
    vn = sum((x - mn) ** 2 for x in near) / (len(near) - 1); vf = sum((x - mf) ** 2 for x in far) / (len(far) - 1)
    sd = ((vn + vf) / 2) ** 0.5
    return dict(n_near=len(near), n_far=len(far), mean_near=round(mn, 4), mean_far=round(mf, 4),
                dprime=round((mn - mf) / sd, 3) if sd > 0 else None)

nonext = lambda m: m != "external_task"
# switches per episode: trigger events of the register counted by episode
mode_ev = events(mode_seq, nonext)
ep_idx = []
bset = sorted(boundaries)
def ep_of(t):
    return sum(1 for b in bset if b < t)
sw_by_ep = collections.Counter(ep_of(e[0]) for e in mode_ev if not e[2])
n_ep = len(ep_lens)
out = dict(
    probe="h0_reset_probe", arm=arm, seed=seed, ticks=ticks, k=K_ENDO, max_ep=MAX_EP, c_rate=c_rate,
    n_env_boundaries=len(boundaries), n_forced_resets=len(forced), n_episodes=n_ep,
    boundary_rate=round(len(boundaries) / ticks, 5),
    ep_len_mean=round(sum(ep_lens) / max(1, n_ep), 2), deaths=deaths,
    harm_per_tick=round(harm_neg / ticks, 5), benefit_per_tick=round(benefit / ticks, 5),
    n_inj=len(inj),
    mode=score(mode_seq, nonext),
    mode_switches_native_total=sum(1 for e in mode_ev if not e[2]),
    mode_switches_native_per_episode=round(sum(sw_by_ep.values()) / max(1, n_ep), 3),
    mode_counts=dict(collections.Counter((x[0] if isinstance(x, tuple) else x) for x in mode_seq)),
    commit=score(commit_seq, lambda c: bool(c)),
    freeze=dict(occupancy=round(occupancy(freeze_seq, bool), 4)),
    dacc_pe_mean=round(sum(dacc_pe) / max(1, len(dacc_pe)), 4),
    reset_changed_paths={"/".join(p): [class_of.get(p), n] for p, n in sorted(reset_paths.items())},
    restored_paths={"/".join(p): n for p, n in sorted(restored_paths.items())},
    big_skipped=sorted("/".join(p) for p in big_skipped),
    snapshot_ms_mean=round(1000 * sum(t_snap) / max(1, len(t_snap)), 1),
    restore_skipped={"/".join(p): n for p, n in sorted(restore_skipped.items())},
    freeze_scored=score(freeze_seq, bool),
    p1_zharma=p1_stats(),
    wall_s=round(time.time() - t_start, 1),
)
line = json.dumps(out)
print(line)
if out_path:
    with open(out_path, "a") as f:
        f.write(line + "\n")
