# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-11T05:50:52.037709Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 268 |
| `substrate_coherence` | 49 |
| `answer_state` | 44 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **70** | plausible_unproven: **279** |
| **low lit**             | novel_discovery: **6**         | speculative: **6** |

Total scored claims: 361

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **185** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 11 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.853 | 0.000 | 0.853 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.863 | 0.000 | 0.863 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.885 | 0.000 | 0.885 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.723 | 0.000 | 0.723 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.878 | 0.000 | 0.878 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.723 | 0.000 | 0.723 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.631 | 0.000 | 0.631 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `INV-041` | invariant | candidate | 0.640 | 0.000 | 0.640 | 0 | 1 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.829 | 0.000 | 0.829 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.643 | 0.000 | 0.643 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.702 | 0.000 | 0.702 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.702 | 0.000 | 0.702 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.840 | 0.000 | 0.840 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.851 | 0.000 | 0.851 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.640 | 0.000 | 0.640 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.808 | 0.000 | 0.808 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.883 | 0.000 | 0.883 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.876 | 0.000 | 0.876 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.817 | 0.000 | 0.817 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.845 | 0.000 | 0.845 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.880 | 0.000 | 0.880 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.825 | 0.000 | 0.825 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.923 | 0.000 | 0.923 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.706 | 0.000 | 0.706 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 11 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.817 | 0.000 | 0.817 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.718 | 0.000 | 0.718 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.792 | 0.000 | 0.792 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 11 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.718 | 0.000 | 0.718 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.728 | 0.000 | 0.728 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.841 | 0.000 | 0.841 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.884 | 0.000 | 0.884 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.832 | 0.000 | 0.832 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.897 | 0.000 | 0.897 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.845 | 0.000 | 0.845 | 0 | 3 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 16 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 3 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.667 | 0.000 | 0.667 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.890 | 0.000 | 0.890 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.838 | 0.000 | 0.838 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.892 | 0.000 | 0.892 | 0 | 5 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 1 | plausible_unproven |
| `MECH-900` | - | - | 0.688 | 0.000 | 0.688 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.894 | 0.000 | 0.894 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.802 | 0.000 | 0.802 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.894 | 0.000 | 0.894 | 0 | 15 | plausible_unproven |
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
| `SD-039` | design_decision | candidate | 0.871 | 0.000 | 0.871 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.748 | 0.000 | 0.748 | 0 | 1 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.799 | 0.000 | 0.799 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.873 | 0.000 | 0.873 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.640 | 0.159 | 0.801 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.658 | 0.177 | 0.819 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.645 | 0.181 | 0.799 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.697 | 0.206 | 0.860 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.697 | 0.206 | 0.861 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.646 | 0.211 | 0.791 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.685 | 0.212 | 0.843 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.634 | 0.231 | 0.903 | 2 | 11 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.683 | 0.242 | 0.830 | 1 | 10 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.720 | 0.271 | 0.869 | 1 | 3 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.719 | 0.297 | 0.860 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.725 | 0.321 | 0.859 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.728 | 0.321 | 0.863 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.729 | 0.323 | 0.865 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.742 | 0.326 | 0.881 | 1 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.620 | 0.349 | 0.891 | 6 | 7 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.663 | 0.351 | 0.871 | 2 | 6 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.631 | 0.392 | 0.870 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.620 | 0.416 | 0.825 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.654 | 0.432 | 0.876 | 10 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.642 | 0.446 | 0.839 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.780 | 0.461 | 0.887 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.686 | 0.472 | 0.793 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.737 | 0.472 | 0.825 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.689 | 0.477 | 0.901 | 7 | 10 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.700 | 0.495 | 0.836 | 2 | 3 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.678 | 0.502 | 0.855 | 3 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.677 | 0.520 | 0.835 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.650 | 0.521 | 0.778 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.716 | 0.541 | 0.891 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.725 | 0.549 | 0.902 | 19 | 9 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.749 | 0.571 | 0.868 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.690 | 0.574 | 0.806 | 28 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.788 | 0.579 | 0.858 | 1 | 15 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.751 | 0.579 | 0.808 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.770 | 0.579 | 0.834 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.777 | 0.579 | 0.843 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.746 | 0.579 | 0.801 | 1 | 3 | plausible_unproven |
| `MECH-057a` | - | - | 0.777 | 0.581 | 0.842 | 1 | 5 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.713 | 0.595 | 0.832 | 83 | 7 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.736 | 0.604 | 0.868 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.707 | 0.606 | 0.808 | 9 | 13 | plausible_unproven |

_Suppressed by gating: 38 substrate_coherence (ARC + universal invariant), 32 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.894 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.862 | 3 |
| `ARC-003` | architectural_commitment | active | 0.795 | 3 |
| `ARC-005` | architectural_commitment | active | 0.795 | 3 |
| `ARC-014` | architectural_commitment | active | 0.780 | 3 |
| `ARC-011` | architectural_commitment | active | 0.772 | 1 |
| `ARC-001` | architectural_commitment | active | 0.681 | 1 |
| `INV-014` | invariant | active | 0.681 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.856 | 11 |
| `Q-016` | open_question | active | 0.847 | 5 |
| `Q-015` | open_question | active | 0.828 | 5 |
| `Q-005` | open_question | active | 0.797 | 4 |
| `Q-020` | open_question | resolved | 0.771 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **6**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-346` | candidate | 0.768 | 0.000 | 1 | 0 |
| `MECH-347` | candidate | 0.768 | 0.000 | 1 | 0 |
| `SD-057` | candidate | 0.768 | 0.000 | 1 | 0 |
| `MECH-306` | provisional | 0.756 | 0.000 | 1 | 0 |
| `MECH-319` | candidate_substrate_landed | 0.756 | 0.000 | 1 | 0 |
| `onboarding` | - | 0.635 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **47**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.159 | 1 |
| `MECH-150` | candidate | 0.166 | 1 |
| `MECH-165` | candidate | 0.177 | 1 |
| `SD-018` | implemented | 0.179 | 1 |
| `MECH-188` | candidate | 0.181 | 1 |
| `MECH-220` | candidate | 0.206 | 1 |
| `SD-023` | candidate | 0.206 | 1 |
| `ARC-032` | candidate | 0.207 | 2 |
| `MECH-116` | candidate | 0.207 | 2 |
| `SD-032c` | - | 0.211 | 1 |
| `MECH-091` | candidate | 0.212 | 1 |
| `MECH-120` | candidate | 0.231 | 2 |
| `MECH-186` | candidate | 0.231 | 2 |
| `MECH-155` | candidate | 0.233 | 2 |
| `SD-047` | provisional | 0.242 | 1 |
| `MECH-128` | candidate | 0.266 | 3 |
| `MECH-334` | candidate | 0.271 | 1 |
| `MECH-047` | provisional | 0.297 | 1 |
| `INV-054` | candidate | 0.309 | 3 |
| `SD-021` | candidate | 0.311 | 3 |
| `MECH-026` | provisional | 0.321 | 1 |
| `MECH-029` | provisional | 0.321 | 1 |
| `MECH-022` | provisional | 0.323 | 1 |
| `MECH-358` | candidate | 0.324 | 1 |
| `SD-059` | candidate | 0.324 | 1 |
| `MECH-025` | candidate | 0.326 | 1 |
| `MECH-070` | retiring | 0.339 | 4 |
| `MECH-153` | candidate | 0.344 | 4 |
| `MECH-099` | candidate | 0.349 | 6 |
| `MECH-295` | candidate | 0.351 | 2 |
| ... | ... | ... | ... (17 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **143**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.923 | 5 |
| `MECH-279` | candidate | 0.906 | 6 |
| `MECH-265` | candidate | 0.905 | 6 |
| `MECH-163` | candidate | 0.903 | 11 |
| `MECH-263` | candidate | 0.902 | 4 |
| `MECH-304` | candidate | 0.901 | 4 |
| `SD-033b` | - | 0.898 | 5 |
| `MECH-271` | candidate | 0.897 | 4 |
| `MECH-CBBL-PROPOSED` | - | 0.894 | 7 |
| `Q-035` | resolved | 0.894 | 15 |
| `MECH-320` | candidate_substrate_landed | 0.892 | 5 |
| `MECH-166` | candidate | 0.891 | 4 |
| `MECH-317` | candidate | 0.890 | 9 |
| `MECH-180` | candidate | 0.888 | 4 |
| `SD-033e` | - | 0.887 | 10 |
| `MECH-122` | provisional | 0.886 | 4 |
| `DEV-NEED-009` | - | 0.885 | 4 |
| `MECH-292` | candidate | 0.885 | 24 |
| `MECH-267` | provisional | 0.884 | 5 |
| `MECH-288` | candidate | 0.884 | 11 |
| `MECH-293` | candidate | 0.884 | 12 |
| `MECH-030` | provisional | 0.883 | 4 |
| `SD-014` | candidate | 0.883 | 13 |
| `MECH-172` | candidate | 0.882 | 6 |
| `MECH-191` | candidate | 0.881 | 4 |
| `ARC-049` | candidate | 0.880 | 27 |
| `MECH-074` | provisional | 0.880 | 9 |
| `DEV-NEED-012` | - | 0.878 | 6 |
| `MECH-203` | candidate | 0.878 | 7 |
| `MECH-092` | candidate | 0.877 | 16 |
| `MECH-046` | provisional | 0.876 | 4 |
| `MECH-316` | candidate | 0.875 | 9 |
| `MECH-303` | candidate | 0.873 | 5 |
| `SD-054` | candidate | 0.873 | 7 |
| `ARC-060` | candidate | 0.872 | 13 |
| `MECH-171` | candidate | 0.871 | 4 |
| `MECH-337` | candidate | 0.871 | 4 |
| `SD-039` | candidate | 0.871 | 6 |
| `ARC-078` | candidate | 0.870 | 11 |
| `MECH-198` | candidate | 0.870 | 8 |
| `MECH-197` | candidate | 0.868 | 12 |
| `MECH-285` | candidate | 0.868 | 16 |
| `MECH-294` | candidate | 0.868 | 9 |
| `MECH-168` | candidate | 0.866 | 4 |
| `MECH-280` | candidate | 0.866 | 5 |
| `MECH-269` | candidate | 0.865 | 34 |
| `MECH-281` | candidate | 0.865 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.863 | 5 |
| `MECH-264` | candidate | 0.861 | 3 |
| `INV-048` | candidate | 0.858 | 4 |
| ... | ... | ... | ... (93 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
