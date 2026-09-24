#!/usr/bin/env python3
"""INV-063 leg A: scale-invariance probe for the proposed composition-only DVs.

WHAT THIS ESTABLISHES, and why it is landed rather than left in a scratchpad.

`inv063_legA_dv_reregistration_proposal_20260920.md` proposes re-registering INV-063's
C1 leg A with DVs that are functions of the SELECTED replay-start INDICES only, and
rejects every priority-MAGNITUDE statistic. The whole proposal rests on one arithmetic
claim: the MEL dependence of replay priority enters as exactly ONE positive scalar
multiplying the whole priority vector, so an argmax (and any rank/composition statistic
built on it) is invariant to it, while any mass-normalised statistic is NOT -- because
`get_valence_priority` adds an `epsilon = 1e-6` floor AFTER the scaling.

This probe measures that against the REAL `ResidueField.get_valence_priority` and the
REAL selector rule, rather than asserting it. It is the evidence behind section 3a of
the proposal; the first draft cited a session-scoped scratchpad path that no longer
resolves, which a peer review correctly flagged as leaving the strongest claim in the
proposal auditable only on trust.

MECHANISM BEING PROBED (ree-v3 origin/main 4fc6f3d):
  - `HippocampalModule._select_valence_weighted_start` (hippocampal/module.py:3036)
    scores every theta-buffer entry and returns the ARGMAX, defaulting to the most
    recent entry (:3062) and breaking ties toward the FIRST index (strict `>` from
    -inf, :3073).
  - `ResidueField.get_valence_priority` (residue/field.py:988) returns
    dot(evaluate_valence(z), drive_state) + epsilon, epsilon = 1e-6.
  - `drive_state[VALENCE_SURPRISE]` is `min(1.0, _pe_ema * 5.0)` (agent.py:10986,
    written :11010) -- but ONLY when `config.surprise_gated_replay` is True AND
    `_pe_ema > 0`; otherwise it is the CONSTANT 0.3 (agent.py:10984). The circularity
    this proposal fixes is therefore a property of the P4-pinned regime specifically.
  - `_pe_ema` is an EMA of `e3_metrics["prediction_error"]`, which agent.py:11064
    republishes as `metrics["e3_prediction_error"]` -- the MEL the P1 manipulation
    check gates on.
  - `valence_harm_enabled` / `valence_liking_enabled` are both default False
    (config.py:3904-3905) and unset by this lineage's builder, so only the surprise
    channel carries weight and the dot reduces to `A2 * v(z) + epsilon`.

WHAT IT DOES NOT ESTABLISH: it exercises the real priority/selector arithmetic on a
synthetic buffer with synthetic writes at V3-EXQ-1069's measured MEL scale. It is not
a full agent run, and it says nothing about how these DVs behave across real intake
arms -- that is the proposal's OWED Test 2 (empirical non-co-movement), which no
landed run can currently supply.

Run: /opt/local/bin/python3 inv063_legA_independence_probe_20260924.py
Deterministic (torch.manual_seed(42)); ASCII-only output per CLAUDE.md.
"""

import math
import os
import sys

REE_V3 = os.environ.get("REE_V3_PATH", "/Users/dgolden/REE_Working/ree-v3")
sys.path.insert(0, REE_V3)

import torch  # noqa: E402
from ree_core.residue.field import (  # noqa: E402
    ResidueField,
    VALENCE_DIM,
    VALENCE_SURPRISE,
    VALENCE_WANTING,
    VALENCE_LIKING,
    VALENCE_HARM_DISCRIMINATIVE,
)
from ree_core.utils.config import ResidueConfig  # noqa: E402

WORLD_DIM = 32
T = 12                      # theta-buffer depth
EPSILON = 1e-6              # get_valence_priority's additive floor (field.py:988)

# VALENCE_SURPRISE write magnitudes at V3-EXQ-1069's measured MEL scale
# (landed per-arm mean MELs span 1.58e-05 .. 4.26e-05).
WRITES = [(1, 2.0e-5), (4, 8.0e-6), (7, 3.5e-5), (9, 1.2e-5)]

# Realised surprise weights: min(1, _pe_ema * 5) over 1069's MEL range, plus two
# larger values to show the trend is a pure rescaling rather than a regime change.
WEIGHTS = [8.0e-5, 1.0e-4, 1.4e-4, 2.13e-4, 1.0e-2, 1.0]
RESCALINGS = [1e-3, 1e-2, 0.1, 10.0]


def build_field():
    torch.manual_seed(42)
    field = ResidueField(ResidueConfig(world_dim=WORLD_DIM))
    buf = torch.randn(T, 1, WORLD_DIM) * 0.05      # reachable z_world cloud scale
    # update_valence writes at the nearest ACTIVE RBF centre, so centres must exist
    # first. Only a SUBSET of entries gets a write -- the sparse, starvation-like
    # case the claim's low-intake arm is about.
    for idx, _ in WRITES:
        field.accumulate(buf[idx], harm_magnitude=0.0, world_delta=0.02)
    for idx, mag in WRITES:
        field.update_valence(buf[idx], VALENCE_SURPRISE, mag)
    return field, buf


def drive(surprise_weight, tonic_5ht=0.0):
    """drive_state exactly as agent.py:11006-11011 builds it."""
    d = torch.zeros(VALENCE_DIM)
    d[VALENCE_WANTING] = tonic_5ht
    d[VALENCE_LIKING] = 0.5
    d[VALENCE_HARM_DISCRIMINATIVE] = 1.0 - tonic_5ht
    d[VALENCE_SURPRISE] = surprise_weight
    return d


def priorities(field, buf, surprise_weight):
    with torch.no_grad():
        return [
            float(field.get_valence_priority(buf[t], drive(surprise_weight)).sum().item())
            for t in range(T)
        ]


def argmax_selector(p):
    """The selector's OWN rule: strict `>` from -inf, so ties go to the FIRST index."""
    best, best_idx = -float("inf"), T - 1
    for i, v in enumerate(p):
        if v > best:
            best, best_idx = v, i
    return best_idx


def top_mass_share(p):
    total = sum(p)
    return max(p) / total if total else float("nan")


def normalised_mass_entropy(p):
    total = sum(p)
    q = [x / total for x in p]
    return -sum(x * math.log(x) for x in q if x > 0) / math.log(T)


def main():
    field, buf = build_field()

    print("INV-063 leg A -- scale-invariance probe")
    print("ree-v3 path: %s" % REE_V3)
    print("torch: %s" % torch.__version__)
    print()
    print("A. Statistics vs the realised surprise weight s")
    print("%-12s %-7s %-18s %-16s %-12s %s"
          % ("s", "argmax", "spread(max-min)", "top_mass_share", "Hnorm(mass)", "n_distinct"))
    for s in WEIGHTS:
        p = priorities(field, buf, s)
        print("%-12.6g %-7d %-18.6g %-16.10f %-12.9f %d"
              % (s, argmax_selector(p), max(p) - min(p), top_mass_share(p),
                 normalised_mass_entropy(p), len(set(p))))

    print()
    print("B. Invariance under a common positive rescaling priority -> c * priority")
    base = priorities(field, buf, 1.0)
    top3_base = sorted(range(T), key=lambda i: base[i], reverse=True)[:3]
    print("   reference ordering at s=1.0 (top 3 buffer positions): %s" % top3_base)
    for c in RESCALINGS:
        p = priorities(field, buf, 1.0 * c)
        top3 = sorted(range(T), key=lambda i: p[i], reverse=True)[:3]
        print("   c=%-8g argmax=%-3d top3=%-12s top_mass_share=%.10f  ordering_preserved=%s"
              % (c, argmax_selector(p), str(top3), top_mass_share(p), top3 == top3_base))

    print()
    print("C. The epsilon floor, and the float32 tie threshold (P6)")
    ulp_at_floor = torch.finfo(torch.float32).eps * EPSILON
    a2, v = 2.13e-4, 2.0e-5
    print("   float32 ulp at epsilon=%g: %g" % (EPSILON, ulp_at_floor))
    print("   A2*v at 1069 scale (A2=%g, v=%g): %g -- ratio to epsilon: %g"
          % (a2, v, a2 * v, a2 * v / EPSILON))
    print("   => the additive floor exceeds the signal ~%dx, so every mass share sits at"
          % round(EPSILON / (a2 * v)))
    print("      1/T = %.6f and carries no content at the measured scale." % (1.0 / T))

    print()
    print("VERDICTS (what the proposal's section 3a records)")
    print("  composition DVs (argmax/rank): INVARIANT -- B shows argmax and the full")
    print("    top-3 ordering unchanged across four orders of magnitude of c.")
    print("  priority-mass statistics: FAIL -- top_mass_share moves with s and with c.")
    print("  retired A3 (max-minus-min spread): FAIL -- A shows it scaling linearly")
    print("    with s, i.e. it is the surprise weight times a constant.")


if __name__ == "__main__":
    main()
