# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-13T08:59:46.102013Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 283 |
| `substrate_coherence` | 54 |
| `answer_state` | 45 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **67** | plausible_unproven: **308** |
| **low lit**             | novel_discovery: **4**         | speculative: **3** |

Total scored claims: 382

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **203** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 11 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.852 | 0.000 | 0.852 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.862 | 0.000 | 0.862 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.885 | 0.000 | 0.885 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.722 | 0.000 | 0.722 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.877 | 0.000 | 0.877 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.822 | 0.000 | 0.822 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.722 | 0.000 | 0.722 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.630 | 0.000 | 0.630 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `INV-041` | invariant | candidate | 0.639 | 0.000 | 0.639 | 0 | 1 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.836 | 0.000 | 0.836 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.643 | 0.000 | 0.643 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.701 | 0.000 | 0.701 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.701 | 0.000 | 0.701 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.840 | 0.000 | 0.840 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.850 | 0.000 | 0.850 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.639 | 0.000 | 0.639 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.798 | 0.000 | 0.798 | 0 | 3 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.824 | 0.000 | 0.824 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.876 | 0.000 | 0.876 | 0 | 4 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.817 | 0.000 | 0.817 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.844 | 0.000 | 0.844 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.879 | 0.000 | 0.879 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.824 | 0.000 | 0.824 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 3 | plausible_unproven |
| `MECH-086` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.923 | 0.000 | 0.923 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.885 | 0.000 | 0.885 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.705 | 0.000 | 0.705 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 11 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 3 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.890 | 0.000 | 0.890 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.706 | 0.000 | 0.706 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.731 | 0.000 | 0.731 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.819 | 0.000 | 0.819 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.718 | 0.000 | 0.718 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.727 | 0.000 | 0.727 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 7 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.883 | 0.000 | 0.883 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.831 | 0.000 | 0.831 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.896 | 0.000 | 0.896 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 3 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 16 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 3 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.667 | 0.000 | 0.667 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.900 | 0.000 | 0.900 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.837 | 0.000 | 0.837 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.892 | 0.000 | 0.892 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 1 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 1 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 3 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.720 | 0.000 | 0.720 | 0 | 1 | plausible_unproven |
| `MECH-423` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 6 | plausible_unproven |
| `MECH-900` | - | - | 0.688 | 0.000 | 0.688 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.893 | 0.000 | 0.893 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.802 | 0.000 | 0.802 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.894 | 0.000 | 0.894 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.882 | 0.000 | 0.882 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.816 | 0.000 | 0.816 | 0 | 4 | plausible_unproven |
| `SD-033e` | - | - | 0.886 | 0.000 | 0.886 | 0 | 10 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.818 | 0.000 | 0.818 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.871 | 0.000 | 0.871 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.747 | 0.000 | 0.747 | 0 | 1 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.798 | 0.000 | 0.798 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.872 | 0.000 | 0.872 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.639 | 0.155 | 0.801 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.656 | 0.172 | 0.818 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.643 | 0.176 | 0.798 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.696 | 0.201 | 0.861 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.696 | 0.202 | 0.860 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.644 | 0.206 | 0.790 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.683 | 0.207 | 0.842 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.632 | 0.226 | 0.903 | 2 | 11 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.681 | 0.237 | 0.829 | 1 | 10 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.718 | 0.292 | 0.860 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.723 | 0.316 | 0.859 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.726 | 0.316 | 0.863 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.728 | 0.319 | 0.864 | 1 | 5 | plausible_unproven |
| `MECH-358` | mechanism_hypothesis | candidate | 0.680 | 0.319 | 0.800 | 1 | 3 | plausible_unproven |
| `SD-059` | design_decision | candidate | 0.725 | 0.319 | 0.860 | 1 | 4 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.740 | 0.321 | 0.880 | 1 | 7 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.756 | 0.322 | 0.901 | 1 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.753 | 0.322 | 0.897 | 1 | 5 | plausible_unproven |
| `MECH-057b` | - | - | 0.724 | 0.324 | 0.857 | 1 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.707 | 0.325 | 0.834 | 1 | 11 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.681 | 0.325 | 0.799 | 1 | 5 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.660 | 0.325 | 0.772 | 1 | 3 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.660 | 0.346 | 0.870 | 2 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.654 | 0.373 | 0.841 | 2 | 6 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.671 | 0.375 | 0.868 | 2 | 3 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.628 | 0.387 | 0.870 | 5 | 6 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.622 | 0.408 | 0.836 | 3 | 3 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.646 | 0.422 | 0.870 | 3 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.651 | 0.427 | 0.875 | 10 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.639 | 0.441 | 0.838 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.778 | 0.456 | 0.886 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.684 | 0.468 | 0.792 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.735 | 0.468 | 0.824 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.686 | 0.472 | 0.901 | 7 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.658 | 0.474 | 0.843 | 4 | 6 | plausible_unproven |
| `MECH-025b` | - | - | 0.725 | 0.477 | 0.807 | 1 | 4 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.676 | 0.498 | 0.855 | 3 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.674 | 0.515 | 0.834 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.647 | 0.516 | 0.778 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.714 | 0.536 | 0.891 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.723 | 0.544 | 0.901 | 19 | 9 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.747 | 0.566 | 0.868 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.688 | 0.569 | 0.806 | 28 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.725 | 0.573 | 0.878 | 3 | 20 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.786 | 0.575 | 0.857 | 1 | 15 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.749 | 0.575 | 0.807 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.769 | 0.575 | 0.834 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.776 | 0.575 | 0.843 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.744 | 0.575 | 0.801 | 1 | 3 | plausible_unproven |
| `MECH-057a` | - | - | 0.775 | 0.576 | 0.842 | 1 | 5 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.711 | 0.590 | 0.832 | 83 | 7 | plausible_unproven |
| `MECH-314a` | - | - | 0.754 | 0.597 | 0.858 | 2 | 5 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.733 | 0.599 | 0.868 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.705 | 0.601 | 0.808 | 9 | 13 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.735 | 0.616 | 0.854 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.711 | 0.619 | 0.802 | 26 | 3 | plausible_unproven |

_Suppressed by gating: 45 substrate_coherence (ARC + universal invariant), 34 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

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
| `INV-010` | invariant | active | 0.861 | 3 |
| `ARC-003` | architectural_commitment | active | 0.794 | 3 |
| `ARC-005` | architectural_commitment | active | 0.794 | 3 |
| `ARC-014` | architectural_commitment | active | 0.780 | 3 |
| `ARC-011` | architectural_commitment | active | 0.771 | 1 |
| `ARC-001` | architectural_commitment | active | 0.681 | 1 |
| `INV-014` | invariant | active | 0.681 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.855 | 11 |
| `Q-016` | open_question | active | 0.846 | 5 |
| `Q-015` | open_question | active | 0.827 | 5 |
| `Q-005` | open_question | active | 0.797 | 4 |
| `Q-020` | open_question | resolved | 0.770 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **4**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-346` | candidate | 0.764 | 0.000 | 1 | 0 |
| `MECH-347` | candidate | 0.764 | 0.000 | 1 | 0 |
| `SD-057` | candidate | 0.764 | 0.000 | 1 | 0 |
| `onboarding` | - | 0.630 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **57**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.155 | 1 |
| `MECH-150` | candidate | 0.161 | 1 |
| `MECH-165` | candidate | 0.172 | 1 |
| `SD-018` | implemented | 0.175 | 1 |
| `MECH-188` | candidate | 0.176 | 1 |
| `SD-023` | candidate | 0.201 | 1 |
| `ARC-032` | candidate | 0.202 | 2 |
| `MECH-116` | candidate | 0.202 | 2 |
| `MECH-220` | candidate | 0.202 | 1 |
| `SD-032c` | - | 0.206 | 1 |
| `MECH-091` | candidate | 0.207 | 1 |
| `MECH-120` | candidate | 0.226 | 2 |
| `MECH-186` | candidate | 0.226 | 2 |
| `MECH-155` | candidate | 0.228 | 2 |
| `SD-047` | provisional | 0.237 | 1 |
| `MECH-128` | candidate | 0.261 | 3 |
| `MECH-047` | provisional | 0.292 | 1 |
| `INV-054` | candidate | 0.305 | 3 |
| `SD-021` | candidate | 0.306 | 3 |
| `MECH-026` | provisional | 0.316 | 1 |
| `MECH-029` | provisional | 0.316 | 1 |
| `MECH-022` | provisional | 0.319 | 1 |
| `MECH-358` | candidate | 0.319 | 1 |
| `SD-059` | candidate | 0.319 | 1 |
| `MECH-025` | candidate | 0.321 | 1 |
| `MECH-263` | candidate | 0.322 | 1 |
| `SD-033b` | - | 0.322 | 1 |
| `MECH-057b` | - | 0.324 | 1 |
| `MECH-189` | candidate | 0.325 | 1 |
| `MECH-329` | candidate | 0.325 | 1 |
| ... | ... | ... | ... (27 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **147**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.923 | 5 |
| `MECH-279` | candidate | 0.906 | 6 |
| `MECH-265` | candidate | 0.905 | 6 |
| `MECH-163` | candidate | 0.902 | 11 |
| `MECH-304` | candidate | 0.900 | 4 |
| `MECH-271` | candidate | 0.896 | 4 |
| `Q-035` | resolved | 0.894 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.893 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.892 | 5 |
| `MECH-166` | candidate | 0.890 | 4 |
| `MECH-317` | candidate | 0.889 | 9 |
| `MECH-180` | candidate | 0.888 | 4 |
| `SD-033e` | - | 0.886 | 10 |
| `DEV-NEED-009` | - | 0.885 | 4 |
| `MECH-122` | provisional | 0.885 | 4 |
| `MECH-292` | candidate | 0.885 | 24 |
| `MECH-267` | provisional | 0.883 | 5 |
| `MECH-288` | candidate | 0.883 | 11 |
| `MECH-293` | candidate | 0.883 | 12 |
| `MECH-030` | provisional | 0.882 | 4 |
| `MECH-172` | candidate | 0.882 | 6 |
| `SD-014` | candidate | 0.882 | 13 |
| `ARC-049` | candidate | 0.880 | 27 |
| `MECH-191` | candidate | 0.880 | 4 |
| `MECH-074` | provisional | 0.879 | 9 |
| `MECH-203` | candidate | 0.878 | 7 |
| `DEV-NEED-012` | - | 0.877 | 6 |
| `MECH-092` | candidate | 0.877 | 16 |
| `MECH-046` | provisional | 0.876 | 4 |
| `MECH-316` | candidate | 0.875 | 9 |
| `MECH-303` | candidate | 0.872 | 5 |
| `SD-054` | candidate | 0.872 | 7 |
| `ARC-060` | candidate | 0.871 | 13 |
| `MECH-337` | candidate | 0.871 | 4 |
| `SD-039` | candidate | 0.871 | 6 |
| `MECH-198` | candidate | 0.870 | 8 |
| `ARC-078` | candidate | 0.869 | 11 |
| `MECH-294` | candidate | 0.868 | 9 |
| `MECH-197` | candidate | 0.867 | 12 |
| `MECH-285` | candidate | 0.867 | 16 |
| `MECH-168` | candidate | 0.865 | 4 |
| `MECH-269` | candidate | 0.865 | 34 |
| `MECH-280` | candidate | 0.865 | 5 |
| `MECH-281` | candidate | 0.865 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.862 | 5 |
| `ARC-051` | candidate | 0.861 | 4 |
| `MECH-264` | candidate | 0.861 | 3 |
| `INV-048` | candidate | 0.858 | 4 |
| `SD-003-SUCCESSOR` | - | 0.857 | 4 |
| `SD-037` | candidate | 0.857 | 4 |
| ... | ... | ... | ... (97 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
