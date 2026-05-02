# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-05-02T08:51:45.069546Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 202 |
| `substrate_coherence` | 30 |
| `answer_state` | 34 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **68** | plausible_unproven: **194** |
| **low lit**             | novel_discovery: **1**         | speculative: **3** |

Total scored claims: 266

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **130** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 6 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.641 | 0.000 | 0.641 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.840 | 0.000 | 0.840 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.654 | 0.000 | 0.654 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.713 | 0.000 | 0.713 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.713 | 0.000 | 0.713 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.851 | 0.000 | 0.851 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.735 | 0.000 | 0.735 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.819 | 0.000 | 0.819 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.894 | 0.000 | 0.894 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.784 | 0.000 | 0.784 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.887 | 0.000 | 0.887 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.855 | 0.000 | 0.855 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.692 | 0.000 | 0.692 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.890 | 0.000 | 0.890 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.838 | 0.000 | 0.838 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.836 | 0.000 | 0.836 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.843 | 0.000 | 0.843 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 3 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.897 | 0.000 | 0.897 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.717 | 0.000 | 0.717 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 9 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.893 | 0.000 | 0.893 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.785 | 0.000 | 0.785 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.899 | 0.000 | 0.899 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.718 | 0.000 | 0.718 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.743 | 0.000 | 0.743 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.729 | 0.000 | 0.729 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 3 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 5 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.913 | 0.000 | 0.913 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.916 | 0.000 | 0.916 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.852 | 0.000 | 0.852 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.895 | 0.000 | 0.895 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.850 | 0.000 | 0.850 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 32 | plausible_unproven |
| `MECH-269b` | - | - | 0.843 | 0.000 | 0.843 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.908 | 0.000 | 0.908 | 0 | 4 | plausible_unproven |
| `MECH-272` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 14 | plausible_unproven |
| `MECH-273` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 5 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 14 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 5 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.895 | 0.000 | 0.895 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.678 | 0.000 | 0.678 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 13 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.895 | 0.000 | 0.895 | 0 | 7 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 9 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `MECH-900` | - | - | 0.699 | 0.000 | 0.699 | 0 | 1 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.813 | 0.000 | 0.813 | 0 | 5 | plausible_unproven |
| `Q-036` | question | open | 0.808 | 0.000 | 0.808 | 0 | 3 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.902 | 0.000 | 0.902 | 0 | 4 | plausible_unproven |
| `SD-032d` | - | - | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.828 | 0.000 | 0.828 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.909 | 0.000 | 0.909 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.898 | 0.000 | 0.898 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.855 | 0.000 | 0.855 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.830 | 0.000 | 0.830 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.842 | 0.000 | 0.842 | 0 | 3 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.759 | 0.000 | 0.759 | 0 | 1 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.688 | 0.265 | 0.829 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.675 | 0.270 | 0.810 | 1 | 3 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.719 | 0.294 | 0.860 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.728 | 0.294 | 0.872 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.727 | 0.295 | 0.871 | 1 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.638 | 0.296 | 0.866 | 2 | 8 | plausible_unproven |
| `MECH-116` | mechanism_hypothesis | candidate | 0.643 | 0.296 | 0.875 | 2 | 7 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.715 | 0.300 | 0.854 | 1 | 6 | plausible_unproven |
| `SD-032c` | - | - | 0.676 | 0.300 | 0.801 | 1 | 3 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.667 | 0.319 | 0.899 | 2 | 7 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.655 | 0.322 | 0.877 | 2 | 5 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.750 | 0.385 | 0.871 | 1 | 4 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.648 | 0.400 | 0.895 | 3 | 8 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.755 | 0.410 | 0.870 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.758 | 0.410 | 0.874 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.760 | 0.412 | 0.876 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.758 | 0.414 | 0.872 | 1 | 5 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.643 | 0.433 | 0.853 | 4 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.669 | 0.437 | 0.902 | 6 | 7 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.659 | 0.456 | 0.862 | 4 | 9 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.680 | 0.480 | 0.881 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.670 | 0.504 | 0.836 | 3 | 3 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.714 | 0.527 | 0.900 | 9 | 7 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.692 | 0.534 | 0.850 | 24 | 9 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | candidate | 0.697 | 0.540 | 0.802 | 2 | 5 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.736 | 0.566 | 0.906 | 7 | 9 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.763 | 0.607 | 0.919 | 18 | 7 | plausible_unproven |

_Suppressed by gating: 21 substrate_coherence (ARC + universal invariant), 28 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **0** standard-gating claims with no exp.

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `ARC-003` | architectural_commitment | active | 0.805 | 3 |
| `ARC-005` | architectural_commitment | active | 0.805 | 3 |
| `ARC-014` | architectural_commitment | active | 0.791 | 3 |
| `ARC-011` | architectural_commitment | active | 0.783 | 1 |
| `ARC-001` | architectural_commitment | active | 0.692 | 1 |
| `INV-014` | invariant | active | 0.692 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.867 | 11 |
| `Q-016` | open_question | active | 0.858 | 5 |
| `Q-015` | open_question | active | 0.839 | 5 |
| `Q-005` | open_question | active | 0.808 | 4 |
| `Q-020` | open_question | resolved | 0.782 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.724 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **36**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-150` | candidate | 0.254 | 1 |
| `MECH-165` | candidate | 0.265 | 1 |
| `SD-018` | implemented | 0.268 | 1 |
| `MECH-188` | candidate | 0.270 | 1 |
| `MECH-111` | candidate | 0.286 | 2 |
| `MECH-118` | candidate | 0.287 | 2 |
| `MECH-216` | provisional | 0.294 | 1 |
| `SD-023` | candidate | 0.294 | 1 |
| `MECH-220` | candidate | 0.295 | 1 |
| `ARC-032` | candidate | 0.296 | 2 |
| `MECH-116` | candidate | 0.296 | 2 |
| `MECH-091` | candidate | 0.300 | 1 |
| `SD-032c` | - | 0.300 | 1 |
| `MECH-120` | candidate | 0.319 | 2 |
| `MECH-186` | candidate | 0.319 | 2 |
| `MECH-155` | candidate | 0.322 | 2 |
| `MECH-128` | candidate | 0.355 | 3 |
| `MECH-047` | provisional | 0.385 | 1 |
| `INV-054` | candidate | 0.398 | 3 |
| `SD-021` | candidate | 0.400 | 3 |
| `MECH-026` | provisional | 0.410 | 1 |
| `MECH-029` | provisional | 0.410 | 1 |
| `MECH-022` | provisional | 0.412 | 1 |
| `MECH-025` | candidate | 0.414 | 1 |
| `SD-016` | implemented | 0.417 | 3 |
| `MECH-070` | retiring | 0.428 | 4 |
| `MECH-153` | candidate | 0.433 | 4 |
| `MECH-099` | candidate | 0.437 | 6 |
| `SD-029` | candidate | 0.456 | 4 |
| `MECH-097` | candidate | 0.462 | 1 |
| ... | ... | ... | ... (6 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **103**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-265` | candidate | 0.916 | 6 |
| `MECH-263` | candidate | 0.913 | 4 |
| `SD-033b` | - | 0.909 | 5 |
| `MECH-271` | candidate | 0.908 | 4 |
| `MECH-279` | candidate | 0.906 | 5 |
| `MECH-292` | candidate | 0.905 | 13 |
| `MECH-163` | candidate | 0.903 | 9 |
| `MECH-166` | candidate | 0.902 | 4 |
| `SD-014` | candidate | 0.902 | 4 |
| `MECH-180` | candidate | 0.899 | 4 |
| `SD-033e` | - | 0.898 | 10 |
| `MECH-122` | provisional | 0.897 | 4 |
| `MECH-267` | provisional | 0.895 | 5 |
| `MECH-288` | candidate | 0.895 | 11 |
| `MECH-293` | candidate | 0.895 | 7 |
| `MECH-030` | provisional | 0.894 | 4 |
| `MECH-172` | candidate | 0.893 | 6 |
| `MECH-191` | candidate | 0.892 | 4 |
| `MECH-074` | provisional | 0.890 | 9 |
| `MECH-092` | candidate | 0.888 | 16 |
| `MECH-046` | provisional | 0.887 | 4 |
| `MECH-272` | candidate | 0.883 | 14 |
| `MECH-171` | candidate | 0.882 | 4 |
| `MECH-295` | candidate | 0.882 | 6 |
| `ARC-060` | candidate | 0.881 | 6 |
| `MECH-273` | candidate | 0.881 | 4 |
| `MECH-287` | candidate | 0.880 | 5 |
| `MECH-285` | candidate | 0.879 | 16 |
| `MECH-294` | candidate | 0.879 | 9 |
| `MECH-168` | candidate | 0.877 | 4 |
| `MECH-269` | candidate | 0.877 | 32 |
| `MECH-203` | candidate | 0.876 | 5 |
| `MECH-280` | candidate | 0.876 | 5 |
| `MECH-281` | candidate | 0.876 | 4 |
| `MECH-264` | candidate | 0.872 | 3 |
| `MECH-121` | candidate | 0.871 | 3 |
| `INV-048` | candidate | 0.869 | 4 |
| `MECH-057b` | - | 0.869 | 4 |
| `SD-003-SUCCESSOR` | - | 0.869 | 4 |
| `SD-037` | candidate | 0.869 | 4 |
| `MECH-275` | candidate | 0.866 | 6 |
| `SD-032d` | - | 0.866 | 4 |
| `MECH-123` | candidate | 0.858 | 5 |
| `MECH-270` | candidate | 0.858 | 4 |
| `MECH-058` | retired | 0.855 | 9 |
| `SD-034` | provisional | 0.855 | 6 |
| `MECH-266` | provisional | 0.852 | 6 |
| `MECH-284` | candidate | 0.852 | 14 |
| `INV-050` | candidate | 0.851 | 3 |
| `MECH-268` | provisional | 0.850 | 6 |
| ... | ... | ... | ... (53 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
