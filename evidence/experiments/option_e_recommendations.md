# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-07T14:27:55.429148Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 257 |
| `substrate_coherence` | 49 |
| `answer_state` | 44 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **64** | plausible_unproven: **278** |
| **low lit**             | novel_discovery: **3**         | speculative: **5** |

Total scored claims: 350

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **184** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 2 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 11 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.852 | 0.000 | 0.852 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.854 | 0.000 | 0.854 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.864 | 0.000 | 0.864 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.724 | 0.000 | 0.724 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.879 | 0.000 | 0.879 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.824 | 0.000 | 0.824 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.724 | 0.000 | 0.724 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.632 | 0.000 | 0.632 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.830 | 0.000 | 0.830 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.644 | 0.000 | 0.644 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.703 | 0.000 | 0.703 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.703 | 0.000 | 0.703 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.841 | 0.000 | 0.841 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.725 | 0.000 | 0.725 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.852 | 0.000 | 0.852 | 0 | 5 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.809 | 0.000 | 0.809 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.884 | 0.000 | 0.884 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.856 | 0.000 | 0.856 | 0 | 4 | plausible_unproven |
| `MECH-045` | mechanism_hypothesis | provisional | 0.864 | 0.000 | 0.864 | 0 | 10 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.846 | 0.000 | 0.846 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.682 | 0.000 | 0.682 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.881 | 0.000 | 0.881 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.828 | 0.000 | 0.828 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.826 | 0.000 | 0.826 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.924 | 0.000 | 0.924 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.887 | 0.000 | 0.887 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.904 | 0.000 | 0.904 | 0 | 11 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.733 | 0.000 | 0.733 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.729 | 0.000 | 0.729 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.842 | 0.000 | 0.842 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.885 | 0.000 | 0.885 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.833 | 0.000 | 0.833 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.898 | 0.000 | 0.898 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.896 | 0.000 | 0.896 | 0 | 5 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.843 | 0.000 | 0.843 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.668 | 0.000 | 0.668 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.893 | 0.000 | 0.893 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.808 | 0.000 | 0.808 | 0 | 3 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 1 | plausible_unproven |
| `MECH-900` | - | - | 0.689 | 0.000 | 0.689 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.895 | 0.000 | 0.895 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.803 | 0.000 | 0.803 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.895 | 0.000 | 0.895 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.741 | 0.000 | 0.741 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.884 | 0.000 | 0.884 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.856 | 0.000 | 0.856 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.818 | 0.000 | 0.818 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.899 | 0.000 | 0.899 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.888 | 0.000 | 0.888 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.845 | 0.000 | 0.845 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.820 | 0.000 | 0.820 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.872 | 0.000 | 0.872 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.749 | 0.000 | 0.749 | 0 | 1 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.800 | 0.000 | 0.800 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.876 | 0.000 | 0.876 | 0 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.643 | 0.167 | 0.802 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.660 | 0.185 | 0.819 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.647 | 0.189 | 0.800 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.699 | 0.214 | 0.861 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.700 | 0.214 | 0.862 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.649 | 0.219 | 0.792 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.688 | 0.220 | 0.844 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.638 | 0.239 | 0.904 | 2 | 11 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.686 | 0.250 | 0.831 | 1 | 10 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.722 | 0.279 | 0.870 | 1 | 3 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.722 | 0.305 | 0.861 | 1 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.736 | 0.325 | 0.873 | 1 | 13 | plausible_unproven |
| `MECH-314` | mechanism_hypothesis | candidate_substrate_landed | 0.743 | 0.325 | 0.882 | 1 | 6 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.727 | 0.329 | 0.860 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.730 | 0.329 | 0.864 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.732 | 0.332 | 0.866 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.745 | 0.334 | 0.882 | 1 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.624 | 0.357 | 0.892 | 6 | 7 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.667 | 0.359 | 0.872 | 2 | 6 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.636 | 0.400 | 0.871 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.625 | 0.424 | 0.826 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.659 | 0.440 | 0.877 | 10 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.647 | 0.454 | 0.840 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.783 | 0.469 | 0.888 | 1 | 5 | plausible_unproven |
| `MECH-314a` | - | - | 0.764 | 0.480 | 0.859 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.689 | 0.480 | 0.794 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.739 | 0.480 | 0.826 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.693 | 0.485 | 0.902 | 7 | 10 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.703 | 0.503 | 0.837 | 2 | 3 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.683 | 0.510 | 0.856 | 3 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.682 | 0.528 | 0.836 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.654 | 0.529 | 0.779 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.721 | 0.549 | 0.892 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.730 | 0.557 | 0.903 | 19 | 9 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.754 | 0.575 | 0.873 | 2 | 8 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.753 | 0.579 | 0.869 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.695 | 0.582 | 0.807 | 28 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.791 | 0.587 | 0.859 | 1 | 15 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.754 | 0.587 | 0.809 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.773 | 0.587 | 0.835 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.780 | 0.587 | 0.844 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.748 | 0.587 | 0.802 | 1 | 3 | plausible_unproven |
| `MECH-057a` | - | - | 0.779 | 0.589 | 0.843 | 1 | 5 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.718 | 0.603 | 0.833 | 83 | 7 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.740 | 0.612 | 0.869 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.712 | 0.614 | 0.809 | 9 | 13 | plausible_unproven |

_Suppressed by gating: 38 substrate_coherence (ARC + universal invariant), 33 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.895 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.863 | 3 |
| `ARC-003` | architectural_commitment | active | 0.796 | 3 |
| `ARC-005` | architectural_commitment | active | 0.796 | 3 |
| `ARC-014` | architectural_commitment | active | 0.781 | 3 |
| `ARC-011` | architectural_commitment | active | 0.773 | 1 |
| `ARC-001` | architectural_commitment | active | 0.682 | 1 |
| `INV-014` | invariant | active | 0.682 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.857 | 11 |
| `Q-016` | open_question | active | 0.848 | 5 |
| `Q-015` | open_question | active | 0.829 | 5 |
| `Q-005` | open_question | active | 0.798 | 4 |
| `Q-020` | open_question | resolved | 0.772 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **3**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-306` | provisional | 0.764 | 0.000 | 1 | 0 |
| `MECH-319` | candidate_substrate_landed | 0.764 | 0.000 | 1 | 0 |
| `onboarding` | - | 0.643 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **47**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.167 | 1 |
| `MECH-150` | candidate | 0.174 | 1 |
| `MECH-165` | candidate | 0.185 | 1 |
| `SD-018` | implemented | 0.187 | 1 |
| `MECH-188` | candidate | 0.189 | 1 |
| `MECH-220` | candidate | 0.214 | 1 |
| `SD-023` | candidate | 0.214 | 1 |
| `ARC-032` | candidate | 0.215 | 2 |
| `MECH-116` | candidate | 0.215 | 2 |
| `SD-032c` | - | 0.219 | 1 |
| `MECH-091` | candidate | 0.220 | 1 |
| `MECH-120` | candidate | 0.239 | 2 |
| `MECH-186` | candidate | 0.239 | 2 |
| `MECH-155` | candidate | 0.241 | 2 |
| `SD-047` | provisional | 0.250 | 1 |
| `MECH-128` | candidate | 0.274 | 3 |
| `MECH-334` | candidate | 0.279 | 1 |
| `MECH-047` | provisional | 0.305 | 1 |
| `INV-054` | candidate | 0.317 | 3 |
| `SD-021` | candidate | 0.319 | 3 |
| `ARC-060` | candidate | 0.325 | 1 |
| `MECH-314` | candidate_substrate_landed | 0.325 | 1 |
| `MECH-026` | provisional | 0.329 | 1 |
| `MECH-029` | provisional | 0.329 | 1 |
| `MECH-022` | provisional | 0.332 | 1 |
| `MECH-025` | candidate | 0.334 | 1 |
| `MECH-070` | retiring | 0.348 | 4 |
| `MECH-153` | candidate | 0.353 | 4 |
| `MECH-099` | candidate | 0.357 | 6 |
| `MECH-295` | candidate | 0.359 | 2 |
| ... | ... | ... | ... (17 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **138**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.924 | 5 |
| `MECH-265` | candidate | 0.906 | 6 |
| `MECH-163` | candidate | 0.904 | 11 |
| `MECH-263` | candidate | 0.903 | 4 |
| `MECH-304` | candidate | 0.902 | 4 |
| `SD-033b` | - | 0.899 | 5 |
| `MECH-271` | candidate | 0.898 | 4 |
| `MECH-279` | candidate | 0.896 | 5 |
| `MECH-CBBL-PROPOSED` | - | 0.895 | 7 |
| `Q-035` | resolved | 0.895 | 15 |
| `MECH-320` | candidate_substrate_landed | 0.893 | 5 |
| `MECH-166` | candidate | 0.892 | 4 |
| `MECH-317` | candidate | 0.891 | 9 |
| `MECH-180` | candidate | 0.889 | 4 |
| `SD-033e` | - | 0.888 | 10 |
| `MECH-122` | provisional | 0.887 | 4 |
| `DEV-NEED-009` | - | 0.886 | 4 |
| `MECH-292` | candidate | 0.886 | 24 |
| `MECH-267` | provisional | 0.885 | 5 |
| `MECH-288` | candidate | 0.885 | 11 |
| `MECH-293` | candidate | 0.885 | 12 |
| `MECH-030` | provisional | 0.884 | 4 |
| `SD-014` | candidate | 0.884 | 13 |
| `MECH-172` | candidate | 0.883 | 6 |
| `MECH-191` | candidate | 0.882 | 4 |
| `ARC-049` | candidate | 0.881 | 27 |
| `MECH-074` | provisional | 0.881 | 9 |
| `DEV-NEED-012` | - | 0.879 | 6 |
| `MECH-203` | candidate | 0.879 | 7 |
| `MECH-092` | candidate | 0.878 | 16 |
| `MECH-046` | provisional | 0.877 | 4 |
| `MECH-316` | candidate | 0.876 | 9 |
| `SD-054` | candidate | 0.876 | 6 |
| `MECH-303` | candidate | 0.874 | 5 |
| `MECH-171` | candidate | 0.872 | 4 |
| `MECH-337` | candidate | 0.872 | 4 |
| `SD-039` | candidate | 0.872 | 6 |
| `ARC-078` | candidate | 0.871 | 11 |
| `MECH-198` | candidate | 0.871 | 8 |
| `MECH-285` | candidate | 0.869 | 16 |
| `MECH-294` | candidate | 0.869 | 9 |
| `MECH-197` | candidate | 0.868 | 12 |
| `MECH-168` | candidate | 0.867 | 4 |
| `MECH-280` | candidate | 0.867 | 5 |
| `MECH-269` | candidate | 0.866 | 34 |
| `MECH-281` | candidate | 0.866 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.864 | 5 |
| `MECH-045` | provisional | 0.864 | 10 |
| `MECH-264` | candidate | 0.862 | 3 |
| `INV-048` | candidate | 0.859 | 4 |
| ... | ... | ... | ... (88 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
