# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-05-20T06:05:00.861223Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 247 |
| `substrate_coherence` | 46 |
| `answer_state` | 43 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **72** | plausible_unproven: **260** |
| **low lit**             | novel_discovery: **1**         | speculative: **3** |

Total scored claims: 336

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **174** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 9 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.891 | 0.000 | 0.891 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.729 | 0.000 | 0.729 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.884 | 0.000 | 0.884 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.812 | 0.000 | 0.812 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.729 | 0.000 | 0.729 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.637 | 0.000 | 0.637 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.835 | 0.000 | 0.835 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.649 | 0.000 | 0.649 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.708 | 0.000 | 0.708 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.708 | 0.000 | 0.708 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.846 | 0.000 | 0.846 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.857 | 0.000 | 0.857 | 0 | 5 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.814 | 0.000 | 0.814 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.889 | 0.000 | 0.889 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.823 | 0.000 | 0.823 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.851 | 0.000 | 0.851 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.687 | 0.000 | 0.687 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.886 | 0.000 | 0.886 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.833 | 0.000 | 0.833 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.831 | 0.000 | 0.831 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.838 | 0.000 | 0.838 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.929 | 0.000 | 0.929 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.892 | 0.000 | 0.892 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.712 | 0.000 | 0.712 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.909 | 0.000 | 0.909 | 0 | 11 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.785 | 0.000 | 0.785 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.743 | 0.000 | 0.743 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.894 | 0.000 | 0.894 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.713 | 0.000 | 0.713 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.808 | 0.000 | 0.808 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.908 | 0.000 | 0.908 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.911 | 0.000 | 0.911 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.847 | 0.000 | 0.847 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.890 | 0.000 | 0.890 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.848 | 0.000 | 0.848 | 0 | 8 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.838 | 0.000 | 0.838 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 5 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.860 | 0.000 | 0.860 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.890 | 0.000 | 0.890 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.673 | 0.000 | 0.673 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.890 | 0.000 | 0.890 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 9 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 6 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 4 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 3 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 14 | plausible_unproven |
| `MECH-314a` | - | - | 0.759 | 0.000 | 0.759 | 0 | 1 | plausible_unproven |
| `MECH-314b` | - | - | 0.799 | 0.000 | 0.799 | 0 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.831 | 0.000 | 0.831 | 0 | 3 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.896 | 0.000 | 0.896 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 8 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 1 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.694 | 0.000 | 0.694 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.900 | 0.000 | 0.900 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.808 | 0.000 | 0.808 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.900 | 0.000 | 0.900 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.889 | 0.000 | 0.889 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.823 | 0.000 | 0.823 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.904 | 0.000 | 0.904 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.893 | 0.000 | 0.893 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.850 | 0.000 | 0.850 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.825 | 0.000 | 0.825 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.877 | 0.000 | 0.877 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.754 | 0.000 | 0.754 | 0 | 1 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.881 | 0.000 | 0.881 | 0 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.657 | 0.208 | 0.807 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.675 | 0.226 | 0.825 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.661 | 0.230 | 0.805 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.714 | 0.254 | 0.867 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.713 | 0.255 | 0.866 | 1 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.620 | 0.256 | 0.862 | 2 | 8 | plausible_unproven |
| `MECH-116` | mechanism_hypothesis | candidate | 0.624 | 0.256 | 0.870 | 2 | 7 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.702 | 0.260 | 0.849 | 1 | 6 | plausible_unproven |
| `SD-032c` | - | - | 0.663 | 0.260 | 0.797 | 1 | 3 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.657 | 0.280 | 0.909 | 2 | 11 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.636 | 0.282 | 0.872 | 2 | 5 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.700 | 0.291 | 0.836 | 1 | 10 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.677 | 0.293 | 0.805 | 1 | 11 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.748 | 0.302 | 0.897 | 1 | 4 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.710 | 0.316 | 0.842 | 1 | 3 | plausible_unproven |
| `MECH-314` | mechanism_hypothesis | candidate_substrate_landed | 0.744 | 0.316 | 0.887 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.736 | 0.346 | 0.866 | 1 | 4 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.630 | 0.360 | 0.900 | 3 | 9 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.666 | 0.366 | 0.866 | 2 | 3 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.741 | 0.370 | 0.865 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.744 | 0.370 | 0.869 | 1 | 6 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.673 | 0.371 | 0.875 | 2 | 3 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.746 | 0.372 | 0.871 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.759 | 0.375 | 0.887 | 1 | 7 | plausible_unproven |
| `MECH-302` | mechanism_hypothesis | candidate | 0.645 | 0.390 | 0.900 | 3 | 6 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.620 | 0.393 | 0.848 | 4 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.647 | 0.398 | 0.897 | 6 | 7 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.658 | 0.440 | 0.876 | 5 | 6 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.784 | 0.455 | 0.893 | 1 | 5 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.647 | 0.464 | 0.831 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.682 | 0.481 | 0.882 | 10 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.670 | 0.495 | 0.845 | 24 | 9 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.717 | 0.526 | 0.907 | 7 | 10 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.706 | 0.551 | 0.861 | 3 | 5 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.671 | 0.559 | 0.784 | 7 | 3 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.750 | 0.565 | 0.874 | 2 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.704 | 0.568 | 0.841 | 10 | 24 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.744 | 0.590 | 0.898 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.753 | 0.597 | 0.908 | 19 | 9 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.711 | 0.607 | 0.814 | 8 | 13 | plausible_unproven |

_Suppressed by gating: 35 substrate_coherence (ARC + universal invariant), 34 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.900 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `ARC-003` | architectural_commitment | active | 0.801 | 3 |
| `ARC-005` | architectural_commitment | active | 0.801 | 3 |
| `ARC-014` | architectural_commitment | active | 0.786 | 3 |
| `ARC-011` | architectural_commitment | active | 0.778 | 1 |
| `ARC-001` | architectural_commitment | active | 0.687 | 1 |
| `INV-014` | invariant | active | 0.687 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.862 | 11 |
| `Q-016` | open_question | active | 0.853 | 5 |
| `Q-015` | open_question | active | 0.834 | 5 |
| `Q-005` | open_question | active | 0.803 | 4 |
| `Q-020` | open_question | resolved | 0.777 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.684 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **42**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.208 | 1 |
| `MECH-150` | candidate | 0.215 | 1 |
| `MECH-165` | candidate | 0.226 | 1 |
| `SD-018` | implemented | 0.228 | 1 |
| `MECH-188` | candidate | 0.230 | 1 |
| `SD-023` | candidate | 0.254 | 1 |
| `MECH-220` | candidate | 0.255 | 1 |
| `ARC-032` | candidate | 0.256 | 2 |
| `MECH-116` | candidate | 0.256 | 2 |
| `MECH-091` | candidate | 0.260 | 1 |
| `SD-032c` | - | 0.260 | 1 |
| `MECH-120` | candidate | 0.280 | 2 |
| `MECH-186` | candidate | 0.280 | 2 |
| `MECH-155` | candidate | 0.282 | 2 |
| `SD-047` | provisional | 0.291 | 1 |
| `SD-049` | candidate | 0.293 | 1 |
| `MECH-166` | candidate | 0.302 | 1 |
| `MECH-128` | candidate | 0.315 | 3 |
| `MECH-313` | candidate_substrate_landed | 0.316 | 1 |
| `MECH-314` | candidate_substrate_landed | 0.316 | 1 |
| `MECH-047` | provisional | 0.346 | 1 |
| `INV-054` | candidate | 0.358 | 3 |
| `SD-021` | candidate | 0.360 | 3 |
| `MECH-320` | candidate_substrate_landed | 0.366 | 2 |
| `MECH-026` | provisional | 0.370 | 1 |
| `MECH-029` | provisional | 0.370 | 1 |
| `MECH-334` | candidate | 0.371 | 2 |
| `MECH-022` | provisional | 0.372 | 1 |
| `MECH-025` | candidate | 0.375 | 1 |
| `MECH-070` | retiring | 0.388 | 4 |
| ... | ... | ... | ... (12 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **134**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.929 | 5 |
| `MECH-265` | candidate | 0.911 | 6 |
| `MECH-163` | candidate | 0.909 | 11 |
| `MECH-263` | candidate | 0.908 | 4 |
| `SD-033b` | - | 0.904 | 5 |
| `MECH-271` | candidate | 0.903 | 4 |
| `MECH-279` | candidate | 0.901 | 5 |
| `MECH-CBBL-PROPOSED` | - | 0.900 | 7 |
| `Q-035` | resolved | 0.900 | 15 |
| `MECH-317` | candidate | 0.896 | 9 |
| `MECH-180` | candidate | 0.894 | 4 |
| `SD-033e` | - | 0.893 | 10 |
| `MECH-122` | provisional | 0.892 | 4 |
| `DEV-NEED-009` | - | 0.891 | 4 |
| `MECH-292` | candidate | 0.891 | 24 |
| `MECH-267` | provisional | 0.890 | 5 |
| `MECH-288` | candidate | 0.890 | 11 |
| `MECH-293` | candidate | 0.890 | 12 |
| `MECH-030` | provisional | 0.889 | 4 |
| `SD-014` | candidate | 0.889 | 13 |
| `MECH-172` | candidate | 0.888 | 6 |
| `MECH-191` | candidate | 0.887 | 4 |
| `ARC-049` | candidate | 0.886 | 27 |
| `MECH-074` | provisional | 0.886 | 9 |
| `DEV-NEED-012` | - | 0.884 | 6 |
| `MECH-203` | candidate | 0.884 | 7 |
| `MECH-092` | candidate | 0.883 | 16 |
| `MECH-046` | provisional | 0.882 | 4 |
| `MECH-316` | candidate | 0.882 | 9 |
| `SD-054` | candidate | 0.881 | 6 |
| `ARC-060` | candidate | 0.878 | 13 |
| `MECH-171` | candidate | 0.877 | 4 |
| `MECH-198` | candidate | 0.877 | 8 |
| `MECH-295` | candidate | 0.877 | 6 |
| `MECH-337` | candidate | 0.877 | 4 |
| `SD-039` | candidate | 0.877 | 6 |
| `MECH-294` | candidate | 0.875 | 9 |
| `MECH-197` | candidate | 0.874 | 12 |
| `MECH-285` | candidate | 0.874 | 16 |
| `MECH-168` | candidate | 0.872 | 4 |
| `MECH-280` | candidate | 0.872 | 5 |
| `MECH-269` | candidate | 0.871 | 34 |
| `MECH-281` | candidate | 0.871 | 4 |
| `MECH-303` | candidate | 0.871 | 4 |
| `ARC-078` | candidate | 0.870 | 9 |
| `MECH-264` | candidate | 0.867 | 3 |
| `INV-048` | candidate | 0.864 | 4 |
| `MECH-057b` | - | 0.864 | 4 |
| `SD-003-SUCCESSOR` | - | 0.864 | 4 |
| `SD-037` | candidate | 0.864 | 4 |
| ... | ... | ... | ... (84 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
