# V3-EXQ-932a -- z_goal / residue_wanting -> behaviour coupling (RE-INSTRUMENTED)

**Status:** PASS  (diagnostic / observational -- claim_ids=[], weights no governance)
**Interpretation label:** `wanting_behaviour_coupling_detected`
**Green arms:** ['g1_emergent', 'g4_seeded']   **Red arms:** (none)
**z_goal dose separation:** +0.8436 (floor +0.0500)

Lettered re-instrument of V3-EXQ-932 per `failure_autopsy_931-932-wanting-authority-cluster_2026-08-16` Section 8. 932's MEASUREMENT-VALIDITY PASS stands; its reported coupling narrative is what this repairs.

**A non-settled coupling reports `null`, never 0.0.** Statuses: `settled` | `underpowered_n` | `unsettable_x_degenerate` (affect channel flat) | `unsettable_dv_degenerate` (behaviour DV cannot move).

## Arm `g1_emergent`  (z_goal_seeding_gain = 1.0)

- z_goal active_frac (mean over seeds): 0.1564
- chan_min_std residue_wanting: 0.22903   z_goal: 0.00000
- chan_max_std (932-comparable, REPORTED ONLY) residue_wanting: 0.39043   z_goal: 0.10263
- gating couplings settled: 3 / 5

| coupling | status | r | rho | within-seed r | seeds def. | n | DV base rate | partial r |
|---|---|---|---|---|---|---|---|---|
| `zgoal_t_to_approach_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 738 | 0.000 | null |
| `zgoal_t_to_approachraw_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 738 | 0.005 | null |
| `zgoal_t_to_benefit_t1t3` | unsettable_dv_degenerate | null | null | null | 0/3 | 738 | 0.008 | null |
| `zgoal_t_to_benefitexp_t1t3` | settled | -0.1170 | -0.1544 | +0.3418 | 1/3 | 738 | 0.266 | -0.0839 |
| `wanting_t_to_approach_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 738 | 0.000 | null |
| `wanting_t_to_approachraw_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 738 | 0.005 | null |
| `wanting_t_to_benefitexp_t1t3` | settled | -0.1319 | -0.2186 | +0.5415 | 2/3 | 738 | 0.266 | -0.1038 |
| `wanting_t_to_moved_t1` | settled | +0.0806 | +0.0114 | +0.1091 | 2/3 | 738 | 0.114 | +0.0695 |
| `wanting_t_to_reefexit_t1` | unsettable_dv_degenerate | null | null | null | 0/3 | 738 | 0.003 | null |
| `wanting_zgoal_contemporaneous` *(reported-only)* | settled | +0.2902 | +0.2645 | -0.2037 | 1/3 | 753 | n/a | null |

## Arm `g4_seeded`  (z_goal_seeding_gain = 4.0)

- z_goal active_frac (mean over seeds): 1.0000
- chan_min_std residue_wanting: 0.30370   z_goal: 0.12702
- chan_max_std (932-comparable, REPORTED ONLY) residue_wanting: 0.56704   z_goal: 0.82190
- gating couplings settled: 3 / 5

| coupling | status | r | rho | within-seed r | seeds def. | n | DV base rate | partial r |
|---|---|---|---|---|---|---|---|---|
| `zgoal_t_to_approach_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 751 | 0.000 | null |
| `zgoal_t_to_approachraw_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 751 | 0.004 | null |
| `zgoal_t_to_benefit_t1t3` | unsettable_dv_degenerate | null | null | null | 0/3 | 751 | 0.009 | null |
| `zgoal_t_to_benefitexp_t1t3` | settled | +0.2625 | +0.2073 | +0.1714 | 2/3 | 751 | 0.063 | +0.2193 |
| `wanting_t_to_approach_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 751 | 0.000 | null |
| `wanting_t_to_approachraw_t1` *(reported-only)* | unsettable_dv_degenerate | null | null | null | 0/3 | 751 | 0.004 | null |
| `wanting_t_to_benefitexp_t1t3` | settled | +0.3620 | +0.2873 | +0.5172 | 2/3 | 751 | 0.063 | +0.3341 |
| `wanting_t_to_moved_t1` | settled | +0.2985 | +0.1908 | +0.3045 | 3/3 | 751 | 0.101 | +0.2728 |
| `wanting_t_to_reefexit_t1` | unsettable_dv_degenerate | null | null | null | 0/3 | 751 | 0.000 | null |
| `wanting_zgoal_contemporaneous` *(reported-only)* | settled | +0.1991 | -0.4059 | +0.2348 | 3/3 | 766 | n/a | null |

`*_to_approach_t1` (mode-based) and `*_to_approachraw_t1` are REPORTED-ONLY and can never gate this run -- see `interpretation.approach_dv_disposition`.
