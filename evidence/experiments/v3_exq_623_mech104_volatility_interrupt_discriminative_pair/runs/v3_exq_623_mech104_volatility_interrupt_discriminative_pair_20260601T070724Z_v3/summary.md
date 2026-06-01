# V3-EXQ-623 -- MECH-104: Volatility Interrupt Discriminative Pair (Signal + Behaviour)

**Status:** FAIL  (5/8 criteria met)
**Claims:** MECH-104
**Predecessor:** V3-EXQ-126 PASS 6/6 (signal-magnitude only).
**Adds:** load-bearing behavioural-consequence gates C6 / C7.

## Per-seed results

- seed 42: ON n_unexp=19 delta_unexp=0.022550 n_decommit=1 mean_post_spike_unc=2.000 | ABLATED n_decommit=0 mean_post_spike_unc=0.000
- seed 123: ON n_unexp=2 delta_unexp=0.024842 n_decommit=0 mean_post_spike_unc=0.000 | ABLATED n_decommit=0 mean_post_spike_unc=0.000

## Failure notes

- C6 FAIL seed=42: ON n_decommit=1 ABLATED n_decommit=0 ratio<2.0 or ON floor<1
- C5 FAIL seed=123: n_unexpected_harm_ON=2 < 10
- C6 FAIL seed=123: ON n_decommit=0 ABLATED n_decommit=0 ratio<2.0 or ON floor<1
- C7 FAIL seed=123: ON mean_post_spike_uncommit=0.000 ABLATED=0.000 ratio<1.5 or ON floor<1.0