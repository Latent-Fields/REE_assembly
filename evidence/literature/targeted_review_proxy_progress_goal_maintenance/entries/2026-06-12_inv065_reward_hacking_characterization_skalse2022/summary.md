# Skalse, Howe, Krasheninnikov & Krueger (2022) -- when a proxy provably diverges

**Claim strand:** B (negative half) -- formal characterization of reward hacking / proxy-true divergence.
**Wires to:** INV-065 (proxy_goal_necessity) and the prospective `proxy_tethering_guard`.

## What it adds beyond Ng et al.

Ng et al. give the positive condition (potential-based shaping is safe). Skalse et al. give the negative characterization: they define a proxy as **unhackable** relative to a true reward exactly when "increasing the expected proxy return can never decrease the expected true return," and then ask when such proxies exist. The central impossibility result: "for the set of all stochastic policies, two reward functions can only be unhackable if one of them is constant." Because expected return is linear in the policy's state-action occupancy, demanding that a non-trivial proxy *never* diverge from the true reward, over all policies, is almost unsatisfiable.

## Why the result is reassuring, not just alarming, for REE

The impossibility is a *worst-case over all stochastic policies*. The paper shows that non-trivial unhackable pairs **do** exist once the policy set is restricted -- deterministic policies, or finite/structured subsets. This is exactly the regime a biological or biologically-motivated agent occupies: REE agents do not roam the full stochastic-policy simplex; they are constrained by homeostatic drives, harm-avoidance, and bounded planning to a structured manifold. So the lesson for the prospective `proxy_tethering_guard` is precise and constructive: the way to keep a maintenance proxy aligned is not only to shape the reward (Ng et al.) but to *restrict the policy space* over which the proxy is trusted. The guard becomes tractable rather than impossible.

## Caveat

The framework assumes a single fixed true reward and reasons over occupancy measures of a fixed policy set. REE has multiple homeostatic drives and a non-stationary objective, so the unhackability comparison would have to be re-specified per drive before it certifies anything in-substrate. Hence `confidence` 0.62 and direction `mixed` -- it both warns against naive proxy reliance and supplies the structural escape hatch that makes REE's setting one where aligned proxies can exist. Chosen over Pan et al. (2022) and Amodei et al. (2016), which remain available as the empirical / problem-survey companions.
