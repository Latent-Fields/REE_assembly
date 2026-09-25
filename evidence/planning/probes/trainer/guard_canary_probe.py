#!/opt/local/bin/python3
"""Canary probe for the prototype gradient-reach guard (bt0925-trainer).

usage: /opt/local/bin/python3 guard_canary_probe.py <case> [seed]
Runs against a ree-v3 worktree at ./ree-v3-wt (origin/main 863d23d65a), reusing the census
recipes verbatim (REE_assembly/evidence/planning/probes/census/census_probe.py):
  A_all     V3-EXQ-1078 P0: Adam(agent.parameters()) on E1+E2 losses, 2 eps x 40 steps.
            Expect FAIL, with hippocampal.action_object_decoder among the dead (canary 1).
  A_e1      same agent/env, but a CORRECTLY SCOPED group: Adam(e1) on compute_prediction_loss
            only. Expect PASS with the frozen-by-design allowlist (negative control / no false
            alarm); also report the naive none-at-any-step form (expected false alarm) and the
            same group with NO allowlist (expected FAIL on write_gate only).
  A_stale   A_e1 with a WRONG allowlist entry (e1.transition_rnn). Expect FAIL (stale allowlist).
  allon     all-ON recipe (x1002 + x734._train_all_on_agent incl. SD-070 P0a), p0=1 p1=1 x 40.
            A guard is attached to EVERY optimizer the recipe constructs. Expect the e2
            optimizer to FAIL with e2.self_transition / self_action_encoder dead (canary 2).
  zselfp0   1078 DR-13 config + run_zself_p0 (17-tensor optimizer). Expect PASS (positive
            control: a correctly scoped phased trainer passes).
  vacuous   empty group and a too-short window. Expect CANNOT_DETERMINE for both.
ASCII-only output. torch.set_num_threads(2). world_dim = self_dim = 32 (deployed).
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(HERE, "ree-v3-wt")
sys.path.insert(0, WT)
sys.path.insert(0, os.path.join(WT, "experiments"))
sys.path.insert(0, HERE)
os.chdir(WT)

import numpy as np  # noqa: E402
import torch  # noqa: E402
torch.set_num_threads(2)

import grad_reach_guard_proto as G  # noqa: E402

CASE = sys.argv[1]
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 42
OUT = os.path.join(HERE, "results")
os.makedirs(OUT, exist_ok=True)

# Frozen-by-design allowlist (design record section 1b). Prefixes over agent.named_parameters().
FROZEN_BY_DESIGN = {
    "residue_field.rbf_field": "non-gradient harm accumulation rule",
    "e1.context_memory.write_gate": "write runs under torch.no_grad (e1_deep.py:381-384)",
    "e1.context_memory.write_content": "write runs under torch.no_grad (e1_deep.py:381-384)",
    "lateral_pfc.delta_proj": "frozen-random by design (lateral_pfc_analog.py:233-236)",
    "lateral_pfc.world_proj": "frozen-random by design (lateral_pfc_analog.py:233-236)",
    "ofc.state_bias_head": "output zeroed when train_state_bias_head=False (ofc_analog.py:201-215)",
}


def seed_all(s):
    torch.manual_seed(s)
    random.seed(s)
    np.random.seed(s)


def build_1078():
    import importlib
    from ree_core.agent import REEAgent
    from ree_core.utils.config import REEConfig
    x = importlib.import_module("experiments.v3_exq_1078_inv069_zself_coherence_unsettled")
    env = x._make_env(SEED)
    env.reset()
    cfg = REEConfig.from_dims(**dict(x.CFG_KW, body_obs_dim=env.body_obs_dim,
                                      world_obs_dim=env.world_obs_dim, action_dim=env.action_dim))
    return x, env, REEAgent(cfg)


def run_1078_loop(x, env, agent, opt, loss_fn, guard):
    from experiments._harness import StepHarness
    harness = StepHarness(agent, env, train_mode=True, seed=SEED)
    agent.train()
    for _ep in range(2):
        _, obs = env.reset()
        agent.reset()
        harness.reset()
        for _t in range(40):
            r = harness.step(obs)
            obs = r.next_obs_dict
            loss = loss_fn()
            if loss.requires_grad:
                opt.zero_grad()
                loss.backward()
                for g in (guard if isinstance(guard, list) else [guard]):
                    g.observe()
                opt.step()
            if r.done:
                break


def report(v, extra=None):
    d = dict(v)
    d["dead_by_module"] = {k: {"tensors": a[0], "params": a[1]}
                           for k, a in G.summarize_dead(v["dead"]).items()}
    d["dead"] = [n for n, *_ in v["dead"]]
    if extra:
        d.update(extra)
    print("[%s] status=%s steps=%d n_params=%d checked=%d allowlisted=%d dead_tensors=%d "
          "not_moved=%d stale_allow=%d leak=%d" % (
              v["group"], v["status"], v["steps"], v["n_params"], v["n_checked"],
              v["n_allowlisted"], len(v["dead"]), len(v["reached_not_moved"]),
              len(v["stale_allowlist"]), len(v["leak_outside_group"])))
    for k, a in d["dead_by_module"].items():
        print("    dead: %-48s tensors=%d params=%d" % (k, a["tensors"], a["params"]))
    for n, why in v["stale_allowlist"]:
        print("    STALE ALLOWLIST: %s (%s)" % (n, why))
    if extra:
        for k, val in extra.items():
            print("    %s: %s" % (k, val if not isinstance(val, list) else "%d items" % len(val)))
    return d


def main():
    seed_all(SEED)
    results = {"case": CASE, "seed": SEED,
               "ree_v3_sha": os.popen("git -C %s rev-parse --short=10 HEAD" % WT).read().strip()}
    out = []
    if CASE == "A_all":
        x, env, agent = build_1078()
        opt = torch.optim.Adam(agent.parameters(), lr=x.LR)
        g = G.GradReachGuard("A_all:Adam(agent.parameters())", list(agent.named_parameters()),
                             allowlist=FROZEN_BY_DESIGN, min_steps=8)
        run_1078_loop(x, env, agent, opt,
                      lambda: agent.compute_prediction_loss() + agent.compute_e2_loss(), g)
        v = g.verdict()
        canary = any(n.startswith("hippocampal.action_object_decoder") for n, *_ in v["dead"])
        out.append(report(v, {"canary_decoder_caught": canary,
                              "naive_optimizer_moved": G.naive_optimizer_moved(g),
                              "naive_none_any_step": G.naive_none_any_step(g)[0]}))
    elif CASE in ("A_e1", "A_stale"):
        x, env, agent = build_1078()
        e1_named = [("e1." + n, p) for n, p in agent.e1.named_parameters()]
        opt = torch.optim.Adam(agent.e1.parameters(), lr=x.LR)
        allow = dict(FROZEN_BY_DESIGN)
        if CASE == "A_stale":
            allow["e1.transition_rnn"] = "WRONG entry planted by the canary"
        g = G.GradReachGuard("%s:Adam(e1)" % CASE, e1_named, allowlist=allow, min_steps=8,
                             watch_outside=list(agent.named_parameters()))
        g_noallow = G.GradReachGuard("%s:Adam(e1) NO allowlist" % CASE, e1_named, allowlist={},
                                     min_steps=8)
        run_1078_loop(x, env, agent, opt, lambda: agent.compute_prediction_loss(), [g, g_noallow])
        naive_status, naive_bad = G.naive_none_any_step(g)
        out.append(report(g.verdict(), {"naive_none_any_step": naive_status,
                                        "naive_none_any_step_flagged": naive_bad}))
        out.append(report(g_noallow.verdict()))
    elif CASE == "allon":
        import importlib
        guards = []
        name_of = {}
        name_of_items = []
        orig_init = torch.optim.Optimizer.__init__

        def init(self, params, *a, **k):
            orig_init(self, params, *a, **k)
            named = []
            for grp in self.param_groups:
                for i, p in enumerate(grp["params"]):
                    named.append((name_of.get(id(p), "local.%d" % len(named)), p))
            import traceback
            site = "?"
            for fr in reversed(traceback.extract_stack()[:-1]):
                if "/torch/" in fr.filename or fr.filename.endswith("guard_canary_probe.py"):
                    continue
                site = "%s:%d" % (fr.filename.split("/ree-v3-wt/")[-1], fr.lineno)
                break
            g = G.GradReachGuard(site, named, allowlist=FROZEN_BY_DESIGN, min_steps=1,
                                 watch_outside=[(n, p) for n, p in name_of_items])
            guards.append(g)
            self.register_step_pre_hook(lambda opt, args, kwargs, _g=g: _g.observe())

        torch.optim.Optimizer.__init__ = init
        x1002 = importlib.import_module(
            "experiments.v3_exq_1002_zworld_actor_adequacy_oracle_adapter")
        x734 = importlib.import_module(
            "experiments.v3_exq_734_env_difficulty_competence_recovery_sweep")
        env_kwargs = x734._env_kwargs_for_rung(x1002.RUNG)
        env = x734._make_env(SEED, env_kwargs)
        agent = x1002._make_agent(env)
        name_of_items[:] = list(agent.named_parameters())
        name_of.update({id(p): n for n, p in name_of_items})
        x734._train_all_on_agent(
            agent, env, seed=SEED, p0_episodes=1, p1_episodes=1, steps_per_episode=40,
            rung_id="guardcanary", total_denominator=2, zworld_p0_episodes=2,
            zworld_p0_env=x734._make_env(SEED, env_kwargs), zworld_p0_dry_run=True,
            zworld_p0_resource_field_weight=0.0)
        torch.optim.Optimizer.__init__ = orig_init
        for g in guards:
            v = g.verdict()
            extra = {"naive_optimizer_moved": G.naive_optimizer_moved(g)}
            if "allon_training.py:572" in g.name:
                extra["canary_e2_self_caught"] = any(
                    n.startswith("e2.self_transition") or n.startswith("e2.self_action_encoder")
                    for n, *_ in v["dead"])
            out.append(report(v, extra))
    elif CASE == "zselfp0":
        x, env, agent = build_1078()
        from experiments._lib.zself_p0_warmup import run_zself_p0
        from experiments._lib.capability_eval import RandomPolicy
        guards = []
        name_of = {id(p): n for n, p in agent.named_parameters()}
        orig_init = torch.optim.Optimizer.__init__

        def init(self, params, *a, **k):
            orig_init(self, params, *a, **k)
            named = [(name_of.get(id(p), "local_head.%d" % i), p)
                     for grp in self.param_groups for i, p in enumerate(grp["params"])]
            g = G.GradReachGuard("zself_p0.py:724 optimizer", named, allowlist=FROZEN_BY_DESIGN,
                                 min_steps=4, watch_outside=list(agent.named_parameters()))
            guards.append(g)
            self.register_step_pre_hook(lambda opt, args, kwargs, _g=g: _g.observe())

        torch.optim.Optimizer.__init__ = init
        run_zself_p0(agent, x._make_env(SEED), SEED, 2, 40, policy=RandomPolicy(SEED),
                     label="guardcanary", dry_run=True)
        torch.optim.Optimizer.__init__ = orig_init
        for g in guards:
            v = g.verdict()
            out.append(report(v, {"leak_modules": sorted({".".join(n.split(".")[:2])
                                                          for n in v["leak_outside_group"]})}))
    elif CASE == "vacuous":
        g_empty = G.GradReachGuard("empty group", [], min_steps=1)
        g_empty.observe()
        out.append(report(g_empty.verdict()))
        lin = torch.nn.Linear(3, 1)
        g_short = G.GradReachGuard("window too short", list(lin.named_parameters()), min_steps=8)
        opt = torch.optim.Adam(lin.parameters(), lr=1e-2)
        for _ in range(3):
            opt.zero_grad()
            lin(torch.randn(4, 3)).sum().backward()
            g_short.observe()
            opt.step()
        out.append(report(g_short.verdict()))
        g_full = G.GradReachGuard("window full (positive)", list(lin.named_parameters()),
                                  min_steps=8)
        for _ in range(8):
            opt.zero_grad()
            lin(torch.randn(4, 3)).sum().backward()
            g_full.observe()
            opt.step()
        out.append(report(g_full.verdict()))
    else:
        raise SystemExit("unknown case %s" % CASE)
    results["groups"] = out
    path = os.path.join(OUT, "guard_%s_s%d.json" % (CASE, SEED))
    with open(path, "w") as f:
        json.dump(results, f, indent=1, default=str)
    print("-> %s" % path)


if __name__ == "__main__":
    main()
