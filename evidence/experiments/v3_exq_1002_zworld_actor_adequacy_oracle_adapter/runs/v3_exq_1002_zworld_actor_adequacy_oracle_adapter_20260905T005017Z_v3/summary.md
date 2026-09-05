# V3-EXQ-1002 -- z_world actor-adequacy locus (H-B vs H-C)

Outcome: **FAIL** (zworld_geometry_blocks_oracle_mapping_h_c_geometry_mismatch) -- hypothesis verdict: **H-C-geometry-mismatch**

| arm | action-path params | mean held-out agreement | seeds clearing bar | mean cloned res/ep |
|---|---|---|---|---|
| rawfield_ceiling | 20485 | 0.9791 | 3/3 | 51.5000 |
| zworld_untrained | 21381 | 0.6880 | 0/3 | 15.8167 |
| zworld_off | 21381 | 0.6636 | 0/3 | 16.8833 |

Strongest TRIVIAL predictor -- max(state-blind majority class, repeat-previous-executed-action)
-- worst seed: 0.5803. Bar: agreement >= 0.80 AND elevation >= 0.20 over that trivial baseline AND
>= 0.10 over the paired `zworld_untrained` negative control, on >= 2 of 3 seeds. **Effective per-seed pass
threshold** (what those three ANDed conjuncts actually require) -- worst seed: 0.8000; see
`interpretation.effective_pass_threshold_per_seed`. Verdict arm beat the untrained control on
0 of 3 seeds. Demonstrator anchor local_view_greedy worst seed = 45.75 res/ep against the 1.0
floor (cell local_view_greedy|seed42).

The VERDICT is C_zworld_adapter_reproduces_oracle alone, on the pre-registered arm zworld_off. C_positive_control_learns_from_raw_field is a gate on INTERPRETABILITY, not a conjunct: its failure routes the run to substrate_not_ready_requeue rather than turning a pass into a fail. C_untrained_control_below_bar is reported only, and is what separates an attributable H-C from 'nothing at 32 dimensions works'. The FIVE outcome cells are a function of three seed-majority booleans -- off_clears, beats_untrained, untrained_clears -- under three readiness gates -- gate_green, verdict_arm_green and comparator_green -- all computed by `_adjudicate()` and contract-tested by `--self-test`. H-C REQUIRES `not beats_untrained`: a verdict arm that beat its own untrained control by the margin is never labelled 'the geometry blocks the mapping'. A RED COMPARATOR ARM licenses no hypothesis verdict in either direction and routes to substrate_not_ready_requeue: the separation is differential, so a collapsed untrained control can neither hand the verdict arm a free margin (a spurious H-B) nor supply a vacuous `not beats_untrained` (a spurious H-C).

The adapter IS `x734.PPOPolicyNet`, the exact class V3-EXQ-978 used as its reader, so the
capacity match to the consumer's policy head holds by construction (governance amendment 5,
2026-09-03). The manipulation relative to 978 is the OBJECTIVE -- cross-entropy on the oracle's
action instead of PPO -- which removes the credit-assignment confound that both prior
frozen-latent readings (948, 978 OFF) were confounded with.

The `zworld_untrained` arm is the NEGATIVE CONTROL: identical agent construction, warmup skipped. It exists
because the pre-amend criteria were clearable without reading the state -- "repeat the previous
executed action" scores 0.57 held-out on this oracle, and an untrained z_world scores
0.681-0.695 UNDER THIS RUN'S OWN ADAPTER (the stale 0.59 figure was a LINEAR readout; red-team
pass 2 Finding 1). Neither the positive control nor the state-blind majority baseline can see
either shortcut, which is why AGREEMENT_BAR is calibrated against the untrained-MLP figure.

The `zworld_on` arm (978's ON-arm warmup) was DROPPED: 978's confirmed autopsy measured the
SD-018 ON leg moving the latent two to three orders below the within-arm seed spread and
sign-inconsistently across seeds, so three more 350-episode warmups would re-measure a foregone
conclusion. What that costs is stated in the docstring's ARMS section.
