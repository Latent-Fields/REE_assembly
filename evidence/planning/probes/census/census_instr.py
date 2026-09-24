"""Gradient-reach census instrumentation (bt0925-census, 2026-09-25).

Non-perturbing global instrumentation, installed BEFORE a driver recipe runs:
  * torch.optim.Optimizer.__init__ wrapped -> every optimizer constructed anywhere (driver,
    _lib trainer, or a ree_core self-owned optimizer) is recorded with its construction
    call-site and the ids of its parameters.
  * a global optimizer step pre-hook -> at every .step(), per param: grad None / zero / nonzero.
  * torch.Tensor.backward wrapped -> grads snapshotted before, diffed after; params whose grad
    changed are attributed to that backward call-site (the loss). Does not alter grads.
  * ParamReadMode (TorchFunctionMode) + forward hooks -> which parameters/modules are READ
    while the agent acts (sense -> e1 tick -> generate_trajectories -> select_action).
All printed text is ASCII.
"""
import collections
import os
import traceback

import torch
from torch.overrides import TorchFunctionMode
import torch.optim.optimizer as _optmod
from torch.utils._pytree import tree_flatten

HERE = os.path.dirname(os.path.abspath(__file__))
_TORCH_DIR = os.path.dirname(torch.__file__)

STATE = {
    "optimizers": {},        # id(opt) -> {"site": str, "param_ids": [..]}
    "step_status": collections.defaultdict(lambda: collections.Counter()),  # pid -> Counter
    "step_opts": collections.defaultdict(set),   # pid -> set(opt sites) seen at step
    "backward_reach": collections.defaultdict(set),  # pid -> set(backward sites)
    "backward_sites": collections.Counter(),
    "autograd_grad_calls": collections.Counter(),
}


def _site(skip_self=True):
    """First stack frame outside torch and outside this instrumentation file."""
    for fr in reversed(traceback.extract_stack()[:-1]):
        fn = fr.filename
        if fn.startswith(_TORCH_DIR) or fn.endswith("census_instr.py"):
            continue
        # shorten to repo-relative
        for key in ("/ree-v3-wt/", "/census/"):
            if key in fn:
                fn = fn.split(key, 1)[1]
                break
        return "%s:%d" % (fn, fr.lineno)
    return "?"


def _site_chain(depth=3):
    out = []
    for fr in reversed(traceback.extract_stack()[:-1]):
        fn = fr.filename
        if fn.startswith(_TORCH_DIR) or fn.endswith("census_instr.py"):
            continue
        for key in ("/ree-v3-wt/", "/census/"):
            if key in fn:
                fn = fn.split(key, 1)[1]
                break
        out.append("%s:%d" % (fn, fr.lineno))
        if len(out) >= depth:
            break
    return " <- ".join(out)


_orig_opt_init = torch.optim.Optimizer.__init__
_orig_backward = torch.Tensor.backward
_installed = {"on": False, "hook": None}


def _opt_init(self, params, *a, **k):
    _orig_opt_init(self, params, *a, **k)
    pids = [id(p) for g in self.param_groups for p in g["params"]]
    STATE["optimizers"][id(self)] = {"site": _site_chain(2), "param_ids": pids,
                                     "cls": type(self).__name__}


def _step_pre_hook(opt, args, kwargs):
    rec = STATE["optimizers"].get(id(opt))
    site = rec["site"] if rec else "unregistered"
    for g in opt.param_groups:
        for p in g["params"]:
            if p.grad is None:
                s = "none"
            elif float(p.grad.detach().abs().sum()) == 0.0:
                s = "zero"
            else:
                s = "nonzero"
            STATE["step_status"][id(p)][s] += 1
            STATE["step_opts"][id(p)].add(site)


TRACKED = {"params": []}   # list of Parameters whose grads are diffed on backward


def _backward(self, *a, **k):
    params = TRACKED["params"]
    before = [(p, None if p.grad is None else p.grad.detach().clone()) for p in params]
    out = _orig_backward(self, *a, **k)
    site = _site_chain(2)
    STATE["backward_sites"][site] += 1
    for p, g0 in before:
        g1 = p.grad
        if g1 is None:
            continue
        d = g1.detach() if g0 is None else (g1.detach() - g0)
        if float(d.abs().sum()) > 0.0:
            STATE["backward_reach"][id(p)].add(site)
    return out


def install():
    if _installed["on"]:
        return
    torch.optim.Optimizer.__init__ = _opt_init
    _installed["hook"] = _optmod.register_optimizer_step_pre_hook(_step_pre_hook)
    torch.Tensor.backward = _backward
    _installed["on"] = True


def track(agent, extra_params=()):
    TRACKED["params"] = list(agent.parameters()) + list(extra_params)


class ParamReadMode(TorchFunctionMode):
    """Records ids of any Parameter passed to any torch function / tensor method."""

    def __init__(self, pids):
        super().__init__()
        self.pids = pids
        self.hit = set()

    def __torch_function__(self, func, types, args=(), kwargs=None):
        kwargs = kwargs or {}
        flat, _ = tree_flatten((args, kwargs))
        for x in flat:
            if isinstance(x, torch.Tensor) and id(x) in self.pids:
                self.hit.add(id(x))
        return func(*args, **(kwargs or {}))


def module_forward_hooks(agent):
    called = collections.Counter()
    handles = []
    for name, m in agent.named_modules():
        if name == "":
            continue

        def mk(n):
            def h(mod, inp, out):
                called[n] += 1
            return h
        handles.append(m.register_forward_hook(mk(name)))
    return called, handles


def snapshot(agent):
    return {n: p.detach().clone() for n, p in agent.named_parameters()}


def classify(agent, snap0, read_pids=None, read_modules=None):
    """Per-parameter-tensor rows."""
    rows = []
    opt_by_pid = collections.defaultdict(list)
    for rec in STATE["optimizers"].values():
        for pid in rec["param_ids"]:
            opt_by_pid[pid].append(rec["site"])
    for n, p in agent.named_parameters():
        pid = id(p)
        delta = float((p.detach() - snap0[n]).abs().max()) if n in snap0 else None
        ss = STATE["step_status"].get(pid, collections.Counter())
        rows.append({
            "name": n,
            "numel": int(p.numel()),
            "requires_grad": bool(p.requires_grad),
            "in_optimizers": sorted(set(opt_by_pid.get(pid, []))),
            "step_status": dict(ss),
            "backward_reach": sorted(STATE["backward_reach"].get(pid, set())),
            "param_delta_max": delta,
            "read_at_act": (None if read_pids is None else (pid in read_pids)),
        })
    return rows


def reset_state():
    STATE["optimizers"].clear()
    STATE["step_status"].clear()
    STATE["step_opts"].clear()
    STATE["backward_reach"].clear()
    STATE["backward_sites"].clear()
