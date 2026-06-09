# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-09T17:47:50.255699Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 261 |
| `substrate_coherence` | 49 |
| `answer_state` | 44 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **68** | plausible_unproven: **276** |
| **low lit**             | novel_discovery: **6**         | speculative: **4** |

Total scored claims: 354

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **182** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 11 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.853 | 0.000 | 0.853 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.863 | 0.000 | 0.863 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.723 | 0.000 | 0.723 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.878 | 0.000 | 0.878 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.723 | 0.000 | 0.723 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.631 | 0.000 | 0.631 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.829 | 0.000 | 0.829 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.644 | 0.000 | 0.644 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.702 | 0.000 | 0.702 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.702 | 0.000 | 0.702 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.841 | 0.000 | 0.841 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.725 | 0.000 | 0.725 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.851 | 0.000 | 0.851 | 0 | 5 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.808 | 0.000 | 0.808 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.883 | 0.000 | 0.883 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-045` | mechanism_hypothesis | provisional | 0.864 | 0.000 | 0.864 | 0 | 10 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.845 | 0.000 | 0.845 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.682 | 0.000 | 0.682 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.880 | 0.000 | 0.880 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.827 | 0.000 | 0.827 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.825 | 0.000 | 0.825 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.924 | 0.000 | 0.924 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.706 | 0.000 | 0.706 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 11 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.817 | 0.000 | 0.817 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.792 | 0.000 | 0.792 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.718 | 0.000 | 0.718 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.728 | 0.000 | 0.728 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.842 | 0.000 | 0.842 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.884 | 0.000 | 0.884 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.832 | 0.000 | 0.832 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.897 | 0.000 | 0.897 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.907 | 0.000 | 0.907 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.668 | 0.000 | 0.668 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.890 | 0.000 | 0.890 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.838 | 0.000 | 0.838 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.893 | 0.000 | 0.893 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 1 | plausible_unproven |
| `MECH-900` | - | - | 0.689 | 0.000 | 0.689 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.894 | 0.000 | 0.894 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.803 | 0.000 | 0.803 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.895 | 0.000 | 0.895 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.883 | 0.000 | 0.883 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.817 | 0.000 | 0.817 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.898 | 0.000 | 0.898 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.887 | 0.000 | 0.887 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.844 | 0.000 | 0.844 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.819 | 0.000 | 0.819 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.872 | 0.000 | 0.872 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.748 | 0.000 | 0.748 | 0 | 1 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.799 | 0.000 | 0.799 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.873 | 0.000 | 0.873 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.642 | 0.163 | 0.802 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.659 | 0.180 | 0.819 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.645 | 0.184 | 0.799 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.699 | 0.209 | 0.862 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.698 | 0.210 | 0.861 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.647 | 0.214 | 0.791 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.686 | 0.215 | 0.843 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.636 | 0.234 | 0.904 | 2 | 11 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.684 | 0.245 | 0.830 | 1 | 10 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.720 | 0.274 | 0.869 | 1 | 3 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.721 | 0.300 | 0.861 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.726 | 0.324 | 0.860 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.729 | 0.324 | 0.864 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.730 | 0.327 | 0.865 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.743 | 0.329 | 0.881 | 1 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.622 | 0.352 | 0.891 | 6 | 7 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.664 | 0.354 | 0.871 | 2 | 6 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.633 | 0.395 | 0.871 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.622 | 0.419 | 0.825 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.655 | 0.435 | 0.876 | 10 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.644 | 0.449 | 0.839 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.781 | 0.464 | 0.887 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.687 | 0.476 | 0.793 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.738 | 0.476 | 0.825 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.691 | 0.480 | 0.902 | 7 | 10 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.701 | 0.498 | 0.837 | 2 | 3 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.680 | 0.506 | 0.855 | 3 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.679 | 0.523 | 0.835 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.652 | 0.524 | 0.779 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.718 | 0.544 | 0.892 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.727 | 0.552 | 0.902 | 19 | 9 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.751 | 0.574 | 0.869 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.692 | 0.577 | 0.807 | 28 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.789 | 0.582 | 0.858 | 1 | 15 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.752 | 0.582 | 0.808 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.772 | 0.582 | 0.835 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.778 | 0.582 | 0.844 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.747 | 0.583 | 0.802 | 1 | 3 | plausible_unproven |
| `MECH-057a` | - | - | 0.778 | 0.584 | 0.843 | 1 | 5 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.715 | 0.598 | 0.833 | 83 | 7 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.738 | 0.607 | 0.869 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.709 | 0.609 | 0.809 | 9 | 13 | plausible_unproven |

_Suppressed by gating: 38 substrate_coherence (ARC + universal invariant), 32 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

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
| `INV-010` | invariant | active | 0.862 | 3 |
| `ARC-003` | architectural_commitment | active | 0.795 | 3 |
| `ARC-005` | architectural_commitment | active | 0.795 | 3 |
| `ARC-014` | architectural_commitment | active | 0.781 | 3 |
| `ARC-011` | architectural_commitment | active | 0.772 | 1 |
| `ARC-001` | architectural_commitment | active | 0.682 | 1 |
| `INV-014` | invariant | active | 0.682 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.856 | 11 |
| `Q-016` | open_question | active | 0.847 | 5 |
| `Q-015` | open_question | active | 0.828 | 5 |
| `Q-005` | open_question | active | 0.798 | 4 |
| `Q-020` | open_question | resolved | 0.771 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **6**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-346` | candidate | 0.772 | 0.000 | 1 | 0 |
| `MECH-347` | candidate | 0.772 | 0.000 | 1 | 0 |
| `SD-057` | candidate | 0.772 | 0.000 | 1 | 0 |
| `MECH-319` | candidate_substrate_landed | 0.760 | 0.000 | 1 | 0 |
| `MECH-306` | provisional | 0.759 | 0.000 | 1 | 0 |
| `onboarding` | - | 0.639 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **44**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.163 | 1 |
| `MECH-150` | candidate | 0.169 | 1 |
| `MECH-165` | candidate | 0.180 | 1 |
| `SD-018` | implemented | 0.183 | 1 |
| `MECH-188` | candidate | 0.184 | 1 |
| `SD-023` | candidate | 0.209 | 1 |
| `ARC-032` | candidate | 0.210 | 2 |
| `MECH-116` | candidate | 0.210 | 2 |
| `MECH-220` | candidate | 0.210 | 1 |
| `SD-032c` | - | 0.214 | 1 |
| `MECH-091` | candidate | 0.215 | 1 |
| `MECH-120` | candidate | 0.234 | 2 |
| `MECH-186` | candidate | 0.234 | 2 |
| `MECH-155` | candidate | 0.236 | 2 |
| `SD-047` | provisional | 0.245 | 1 |
| `MECH-128` | candidate | 0.269 | 3 |
| `MECH-334` | candidate | 0.274 | 1 |
| `MECH-047` | provisional | 0.300 | 1 |
| `INV-054` | candidate | 0.313 | 3 |
| `SD-021` | candidate | 0.314 | 3 |
| `MECH-026` | provisional | 0.324 | 1 |
| `MECH-029` | provisional | 0.324 | 1 |
| `MECH-022` | provisional | 0.327 | 1 |
| `MECH-025` | candidate | 0.329 | 1 |
| `MECH-070` | retiring | 0.343 | 4 |
| `MECH-153` | candidate | 0.348 | 4 |
| `MECH-099` | candidate | 0.352 | 6 |
| `MECH-295` | candidate | 0.354 | 2 |
| `MECH-097` | candidate | 0.376 | 1 |
| `MECH-075` | candidate | 0.395 | 5 |
| ... | ... | ... | ... (14 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **140**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.924 | 5 |
| `MECH-279` | candidate | 0.907 | 6 |
| `MECH-265` | candidate | 0.906 | 6 |
| `MECH-163` | candidate | 0.903 | 11 |
| `MECH-263` | candidate | 0.902 | 4 |
| `MECH-304` | candidate | 0.901 | 4 |
| `SD-033b` | - | 0.898 | 5 |
| `MECH-271` | candidate | 0.897 | 4 |
| `Q-035` | resolved | 0.895 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.894 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.893 | 5 |
| `MECH-166` | candidate | 0.891 | 4 |
| `MECH-317` | candidate | 0.890 | 9 |
| `MECH-180` | candidate | 0.889 | 4 |
| `SD-033e` | - | 0.887 | 10 |
| `DEV-NEED-009` | - | 0.886 | 4 |
| `MECH-122` | provisional | 0.886 | 4 |
| `MECH-292` | candidate | 0.886 | 24 |
| `MECH-267` | provisional | 0.884 | 5 |
| `MECH-288` | candidate | 0.884 | 11 |
| `MECH-293` | candidate | 0.884 | 12 |
| `MECH-030` | provisional | 0.883 | 4 |
| `MECH-172` | candidate | 0.883 | 6 |
| `SD-014` | candidate | 0.883 | 13 |
| `ARC-049` | candidate | 0.881 | 27 |
| `MECH-191` | candidate | 0.881 | 4 |
| `MECH-074` | provisional | 0.880 | 9 |
| `MECH-203` | candidate | 0.879 | 7 |
| `DEV-NEED-012` | - | 0.878 | 6 |
| `MECH-092` | candidate | 0.878 | 16 |
| `MECH-046` | provisional | 0.877 | 4 |
| `MECH-316` | candidate | 0.876 | 9 |
| `MECH-303` | candidate | 0.873 | 5 |
| `SD-054` | candidate | 0.873 | 7 |
| `ARC-060` | candidate | 0.872 | 13 |
| `MECH-337` | candidate | 0.872 | 4 |
| `SD-039` | candidate | 0.872 | 6 |
| `MECH-171` | candidate | 0.871 | 4 |
| `MECH-198` | candidate | 0.871 | 8 |
| `ARC-078` | candidate | 0.870 | 11 |
| `MECH-294` | candidate | 0.869 | 9 |
| `MECH-197` | candidate | 0.868 | 12 |
| `MECH-285` | candidate | 0.868 | 16 |
| `MECH-168` | candidate | 0.866 | 4 |
| `MECH-269` | candidate | 0.866 | 34 |
| `MECH-280` | candidate | 0.866 | 5 |
| `MECH-281` | candidate | 0.866 | 4 |
| `MECH-045` | provisional | 0.864 | 10 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.863 | 5 |
| `MECH-264` | candidate | 0.862 | 3 |
| ... | ... | ... | ... (90 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
