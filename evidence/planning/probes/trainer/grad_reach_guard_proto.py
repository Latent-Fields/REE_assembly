"""Prototype gradient-reach guard (bt0925-trainer, chip-20260925-native-waking-trainer-design).

PROBE-ONLY prototype of the guard specified in
REE_assembly/evidence/planning/native_waking_trainer_design_20260925.md section 3.
Not a ree_core module; nothing here is imported by ree-v3.

What it asserts, per trainer GROUP (a named list of (param_name, Parameter)):
  G1 REACH:     every non-allowlisted parameter receives a NONZERO, finite gradient on at
                least one optimizer step within the window. grad None and grad exactly 0 are
                both "not reached". (Not "None at any step": the native zero-loss sentinel
                `next(m.parameters()).sum() * 0.0` legitimately yields None/0 while replay
                buffers fill -- measured in the census raw JSON, recipe A.)
  G2 MOVED:     every reached parameter actually changed value over the window (catches a
                parameter that gets gradient but is not in the stepping optimizer, or lr 0).
  G3 ALLOWLIST: every allowlisted parameter did NOT receive gradient. A frozen-by-design entry
                that starts receiving gradient is a stale allowlist entry and FAILS -- the
                allowlist cannot silently hide a module that has become trainable (or one
                that was never frozen).
  G4 NON-VACUOUS: the group is non-empty, the window has >= min_steps optimizer steps, and at
                least one parameter was checked. Otherwise the verdict is CANNOT_DETERMINE,
                never PASS (CLAUDE.md "Negative instruments": an empty denominator must not
                read as a clean result).
  G5 LEAK (report only): parameters OUTSIDE every group that nevertheless received gradient
                from the group's losses (the census's `**` case: gradient reaches a module
                that no optimizer holds, and is discarded). Reported, not failed -- whether
                that is a defect depends on the design (ZSelfP0 excludes the world path on
                purpose).
Verdicts: PASS / FAIL / CANNOT_DETERMINE. All printed text is ASCII.
"""
import collections

import torch


class GradReachGuard:
    def __init__(self, name, named_params, allowlist=None, min_steps=8, watch_outside=None):
        self.name = name
        self.named = [(n, p) for n, p in named_params if p.requires_grad]
        self.allow = dict(allowlist or {})          # param-name prefix -> reason
        self.min_steps = int(min_steps)
        self.steps = 0
        self.nonzero = collections.Counter()
        self.none = collections.Counter()
        self.zero = collections.Counter()
        self.snap = {n: p.detach().clone() for n, p in self.named}
        ids = {id(p) for _, p in self.named}
        self.outside = [(n, p) for n, p in (watch_outside or []) if id(p) not in ids]
        self.leak = collections.Counter()

    def _allowed(self, n):
        for pre, why in self.allow.items():
            if n == pre or n.startswith(pre + ".") or n.startswith(pre):
                return why
        return None

    def observe(self):
        """Call immediately BEFORE optimizer.step() (e.g. from a step pre-hook)."""
        self.steps += 1
        for n, p in self.named:
            g = p.grad
            if g is None:
                self.none[n] += 1
            elif not bool(torch.isfinite(g).all()) or float(g.detach().abs().sum()) == 0.0:
                self.zero[n] += 1
            else:
                self.nonzero[n] += 1
        for n, p in self.outside:
            g = p.grad
            if g is not None and float(g.detach().abs().sum()) > 0.0:
                self.leak[n] += 1

    def verdict(self):
        dead, not_moved, stale_allow, allowed_ok = [], [], [], []
        checked = 0
        for n, p in self.named:
            why = self._allowed(n)
            reached = self.nonzero[n] > 0
            if why is not None:
                if reached:
                    stale_allow.append((n, why))
                else:
                    allowed_ok.append((n, why))
                continue
            checked += 1
            if not reached:
                dead.append((n, int(p.numel()), self.none[n], self.zero[n]))
            elif float((p.detach() - self.snap[n]).abs().max()) == 0.0:
                not_moved.append(n)
        if not self.named or checked == 0 or self.steps < self.min_steps:
            status = "CANNOT_DETERMINE"
        elif dead or not_moved or stale_allow:
            status = "FAIL"
        else:
            status = "PASS"
        return {
            "group": self.name, "status": status, "steps": self.steps,
            "min_steps": self.min_steps, "n_params": len(self.named), "n_checked": checked,
            "n_allowlisted": len(allowed_ok),
            "dead": dead, "reached_not_moved": not_moved, "stale_allowlist": stale_allow,
            "leak_outside_group": sorted(self.leak),
        }


def naive_none_any_step(guard):
    """The naive form the design rejects: FAIL if any param had grad None at any step."""
    bad = [n for n, _ in guard.named if guard.none[n] > 0 or guard.zero[n] > 0]
    return ("FAIL" if bad else "PASS"), bad


def naive_optimizer_moved(guard):
    """The status-quo style check: the optimizer 'trained' if ANY of its params moved
    (what an aggregate loss curve / weight-norm delta tells you)."""
    moved = any(float((p.detach() - guard.snap[n]).abs().max()) > 0.0 for n, p in guard.named)
    return "PASS" if moved else "FAIL"


def summarize_dead(dead, depth=2):
    agg = collections.OrderedDict()
    for n, numel, _nn, _nz in dead:
        k = ".".join(n.split(".")[:depth])
        a = agg.setdefault(k, [0, 0])
        a[0] += 1
        a[1] += numel
    return agg
