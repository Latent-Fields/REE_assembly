# V3-EXQ-1007 -- MECH-536 eval-time action-persistence discriminator

Outcome: **PASS** (latch_abolishes_cycle_competence_flat_representational_deficit) -- MECH-536: supports, MECH-535: supports

| arm | mean res/ep | per-seed res/ep | per-seed cycle incidence | per-seed fixed-point incidence | per-seed survival |
|---|---|---|---|---|---|
| greedy_argmax | 0.2667 | 0.00/0.25/0.55 | 0.80/0.00/0.00 | 0.20/1.00/1.00 | 50.75/200.00/200.00 |
| persist_k2 | 0.2833 | 0.10/0.25/0.50 | 0.00/0.00/0.00 | 0.25/1.00/1.00 | 62.80/200.00/200.00 |
| persist_k4 | 0.3000 | 0.15/0.25/0.50 | 0.00/0.00/0.00 | 0.30/1.00/1.00 | 103.55/200.00/200.00 |
| switch_cost | 0.3333 | 0.25/0.25/0.50 | 0.15/0.00/0.00 | 0.55/1.00/1.00 | 127.75/200.00/200.00 |
| stochastic_sample | 1.8833 | 2.05/1.70/1.90 | 0.05/0.00/0.05 | 0.00/0.00/0.00 | 66.25/72.10/63.65 |
| random_walk (anchor) | 0.9333 | 1.05/0.90/0.85 | 0.00/0.10/0.15 | 0.00/0.00/0.00 | 48.10/42.60/47.30 |
| local_view_greedy (anchor) | 48.0500 | 45.75/49.70/48.70 | 0.00/0.00/0.00 | 0.00/0.00/0.00 | 154.15/170.50/166.90 |
| local_view_greedy_persist_k2 (anchor) | 5.6333 | 5.75/3.45/7.70 | 0.00/0.00/0.00 | 0.00/0.00/0.00 | 38.90/30.00/46.60 |
| greedy_argmax@contamination_off | 0.2500 | 0.00/0.25/0.50 | 0.75/0.00/0.00 | 0.15/1.00/1.00 | 200.00/200.00/200.00 |
| persist_k2@contamination_off | 0.2833 | 0.10/0.25/0.50 | 0.00/0.00/0.00 | 0.20/1.00/1.00 | 200.00/200.00/200.00 |

Cycle-present seeds (greedy cycle_incidence >= 0.25): [42] of [42, 43, 44].
C1 PASS; C2 PASS (effect floor 0.50; k2 lifts [0.1, 0.0, -0.05], k4 lifts [0.15, 0.0, -0.05]);
exceeds random-walk envelope: False. C3 (latch harmless on lvg) FAIL;
C2 survival-matched (contamination off) PASS.
switch_cost delta per seed: [0.05, 0.079, 0.1888]. Caveats: ["latch_costs_good_representation: local_view_greedy_persist_k2 retained < 50% of local_view_greedy on some seed -- MECH-536's 'protective, not necessary' framing needs a caveat", 'cycle_replaced_by_longer_orbit: a verdict arm shows a bounded orbit of period > 2 on a cycle-present seed -- the two-cycle was lengthened, not dissolved'].

Verdict = C1 AND C2 on the verdict arms persist_k2 AND persist_k4, under a green gate. PASS iff both. C1 false -> non_contributory (the manipulation did not reach the DV). C1 true, C2 false -> weakens (gating deficit; ARC-107 root C) iff a verdict arm's competence beats random_walk on a strict majority of seeds or clears 1.0 on any seed; otherwise mixed (a measured rise that stays inside the undirected envelope). switch_cost and stochastic_sample carry their own C1/C2 flags and are reported, never adjudicated; C3 and C2_survival_matched are reported.

One trained reader per seed (978's field_loss_off cell, imported recipe); every arm is the SAME
reader under a different EXECUTION rule on a deep copy of the post-training snapshot and a fresh
env at the same seed. A fishtank episode-log companion (first seed, every arm, per-episode `arm`
badge) is written alongside; it is an observational pass, not the scored data.
