# V3-EXQ-1008 -- z_world actor-adequacy portfolio (H-E; H-C corroborator)

Outcome: **PASS** -- label `ws250_optimal_linear_compression_supports_mapping__linear_content_ceiling_information_not_geometry` -- **H-E: eliminated; H-C: weakened**

| arm | feature dim | action-path params | mean held-out agreement | seeds clearing bar | mean cloned res/ep |
|---|---|---|---|---|---|
| rawfield_ceiling | 25 | 20485 | 0.9791 | 3/3 | 51.500 |
| ws250_full | 250 | 49285 | 0.9387 | 3/3 | 50.733 |
| ws250_randproj | 32 | 21381 | 0.7725 | 0/3 | 26.833 |
| ws250_pca | 32 | 21381 | 0.8684 | 3/3 | 43.833 |
| zworld_untrained_diag | 32 | 21381 | 0.6946 | 0/3 | 17.500 |
| zworld_untrained_fielddecode | 32 | 21381 | 0.6644 | 0/3 | 16.067 |
| zworld_off_diag | 32 | 21381 | 0.6686 | 0/3 | 16.233 |
| zworld_off_fielddecode | 32 | 21381 | 0.6656 | 0/3 | 16.333 |
| zworld_off_zca | 32 | 21381 | 0.7078 | 0/3 | 23.833 |
| zworld_off_ldawhiten | 32 | 21381 | 0.7114 | 0/3 | 24.450 |

LEG 1 (H-E): `ws250_optimal_linear_compression_supports_mapping`. Verdict arm ws250_pca; anchor ws250_full (must reach 0.80); control ws250_randproj (second draw reported).

| seed | ws250_full | ws250_pca | ws250_randproj | randproj draw b | pca - randproj |
|---|---|---|---|---|---|
| 42 | 0.9399 | 0.8771 | 0.7863 | 0.7728 | +0.0908 |
| 43 | 0.9335 | 0.8578 | 0.7865 | 0.7744 | +0.0713 |
| 44 | 0.9425 | 0.8702 | 0.7445 | 0.7430 | +0.1257 |

LEG 2 (H-C corroborator): `linear_content_ceiling_information_not_geometry`. Seed-majority lift class of zworld_off_fielddecode over zworld_off_diag: **flat** (untrained pair: flat; content witness: degrade; zca: flat; ldawhiten: flat).

| seed | off_diag | off_fielddecode | lift | class | lift on untrained | decode-then-oracle | content class |
|---|---|---|---|---|---|---|---|
| 42 | 0.6718 | 0.6755 | +0.0037 | flat | -0.0363 | 0.5931 | degrade |
| 43 | 0.6735 | 0.6541 | -0.0194 | flat | -0.0209 | 0.5910 | degrade |
| 44 | 0.6606 | 0.6672 | +0.0066 | flat | -0.0336 | 0.6066 | degrade |

Bar: agreement >= 0.80 AND elevation >= 0.20 over the strongest trivial predictor (worst seed 0.5803), on >= 2 of 3 seeds. Lift classes: lift >= 0.10, marginal >= 0.05, flat within +-0.05, degrade <= -0.05. Demonstrator anchor local_view_greedy worst seed 45.75 res/ep (cell local_view_greedy|seed42).

TWO INDEPENDENT LEGS, each a pure function of seed-majority classes under its own readiness gates (`_adjudicate_leg1`, `_adjudicate_leg2`, contract-tested by --self-test). LEG 1 (H-E): verdict on ws250_pca alone -- clears bar+elevation -> H-E eliminated; neither task-agnostic compression clears -> H-E confirmed; random-clears-but-PCA-does-not -> undetermined. The PCA-minus-random margin is reported, not a conjunct. LEG 2 (H-C corroborator): verdict on the paired lift of zworld_off_fielddecode over zworld_off_diag -- seed-majority LIFT (>= 0.10) -> corroborated (strong if the re-based arm also clears the bar; CHANNEL-LEVEL, never latent-specific, if the untrained latent lifts by the same class); FLAT or DEGRADE -> weakened ONLY when the closed-form decode-then-oracle content witness is itself not a lift (information ceiling), otherwise undetermined (reader shortfall / inconsistent); MARGINAL or inconsistent -> undetermined. Fewer than 2 seeds -> no verdict on either leg. A red gate on either leg licenses NO verdict for that leg and never for the other. OUTCOME = PASS iff BOTH legs adjudicated (C_leg1_adjudicated AND C_leg2_adjudicated); the science is in the labels and hypothesis_verdict, not in PASS/FAIL.
