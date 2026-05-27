# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-05-27T06:36:33.000899Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 247 |
| `substrate_coherence` | 47 |
| `answer_state` | 43 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **63** | plausible_unproven: **269** |
| **low lit**             | novel_discovery: **1**         | speculative: **4** |

Total scored claims: 337

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **178** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 9 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.890 | 0.000 | 0.890 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.727 | 0.000 | 0.727 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.827 | 0.000 | 0.827 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.727 | 0.000 | 0.727 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.635 | 0.000 | 0.635 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.833 | 0.000 | 0.833 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.648 | 0.000 | 0.648 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.706 | 0.000 | 0.706 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.706 | 0.000 | 0.706 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.844 | 0.000 | 0.844 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.729 | 0.000 | 0.729 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.855 | 0.000 | 0.855 | 0 | 5 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.812 | 0.000 | 0.812 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.887 | 0.000 | 0.887 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.849 | 0.000 | 0.849 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.685 | 0.000 | 0.685 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.884 | 0.000 | 0.884 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.831 | 0.000 | 0.831 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.927 | 0.000 | 0.927 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.890 | 0.000 | 0.890 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.710 | 0.000 | 0.710 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.907 | 0.000 | 0.907 | 0 | 11 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.783 | 0.000 | 0.783 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.711 | 0.000 | 0.711 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.722 | 0.000 | 0.722 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.722 | 0.000 | 0.722 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.909 | 0.000 | 0.909 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.845 | 0.000 | 0.845 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.888 | 0.000 | 0.888 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.847 | 0.000 | 0.847 | 0 | 8 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.836 | 0.000 | 0.836 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.899 | 0.000 | 0.899 | 0 | 5 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.672 | 0.000 | 0.672 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 9 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 6 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 3 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 14 | plausible_unproven |
| `MECH-314a` | - | - | 0.757 | 0.000 | 0.757 | 0 | 1 | plausible_unproven |
| `MECH-314b` | - | - | 0.797 | 0.000 | 0.797 | 0 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.894 | 0.000 | 0.894 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 8 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 1 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.692 | 0.000 | 0.692 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.898 | 0.000 | 0.898 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.806 | 0.000 | 0.806 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.898 | 0.000 | 0.898 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.887 | 0.000 | 0.887 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.821 | 0.000 | 0.821 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.902 | 0.000 | 0.902 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.891 | 0.000 | 0.891 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.848 | 0.000 | 0.848 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.823 | 0.000 | 0.823 | 0 | 2 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.875 | 0.000 | 0.875 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.752 | 0.000 | 0.752 | 0 | 1 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.879 | 0.000 | 0.879 | 0 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.653 | 0.193 | 0.806 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.670 | 0.210 | 0.823 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.656 | 0.214 | 0.803 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.708 | 0.239 | 0.865 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.708 | 0.240 | 0.864 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.657 | 0.244 | 0.795 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.697 | 0.245 | 0.847 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.650 | 0.264 | 0.907 | 2 | 11 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.629 | 0.266 | 0.871 | 2 | 5 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.694 | 0.275 | 0.834 | 1 | 10 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.743 | 0.286 | 0.895 | 1 | 4 | plausible_unproven |
| `MECH-314` | mechanism_hypothesis | candidate_substrate_landed | 0.739 | 0.301 | 0.885 | 1 | 6 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.724 | 0.312 | 0.862 | 1 | 4 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.731 | 0.330 | 0.864 | 1 | 4 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.621 | 0.344 | 0.898 | 3 | 9 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.659 | 0.351 | 0.864 | 2 | 3 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.736 | 0.354 | 0.863 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.739 | 0.354 | 0.867 | 1 | 6 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.666 | 0.355 | 0.873 | 2 | 3 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.741 | 0.357 | 0.869 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.754 | 0.359 | 0.885 | 1 | 7 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.629 | 0.368 | 0.803 | 2 | 11 | plausible_unproven |
| `MECH-302` | mechanism_hypothesis | candidate | 0.636 | 0.375 | 0.898 | 3 | 6 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.638 | 0.382 | 0.895 | 6 | 7 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.649 | 0.425 | 0.874 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.639 | 0.449 | 0.829 | 3 | 3 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.650 | 0.460 | 0.840 | 4 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.672 | 0.465 | 0.880 | 10 | 14 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.769 | 0.467 | 0.870 | 1 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.769 | 0.467 | 0.870 | 1 | 4 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.661 | 0.479 | 0.843 | 24 | 9 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.708 | 0.510 | 0.906 | 7 | 10 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.744 | 0.523 | 0.891 | 2 | 5 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.698 | 0.536 | 0.859 | 3 | 5 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.662 | 0.543 | 0.782 | 7 | 3 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.743 | 0.549 | 0.872 | 2 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.696 | 0.553 | 0.839 | 10 | 24 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.735 | 0.574 | 0.896 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.744 | 0.582 | 0.906 | 19 | 9 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.709 | 0.607 | 0.810 | 28 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.799 | 0.612 | 0.862 | 1 | 15 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.762 | 0.612 | 0.812 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.781 | 0.612 | 0.838 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.788 | 0.612 | 0.847 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.757 | 0.613 | 0.805 | 1 | 3 | plausible_unproven |
| `MECH-057a` | - | - | 0.788 | 0.614 | 0.846 | 1 | 5 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.715 | 0.618 | 0.812 | 9 | 13 | plausible_unproven |

_Suppressed by gating: 37 substrate_coherence (ARC + universal invariant), 33 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.898 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `ARC-003` | architectural_commitment | active | 0.799 | 3 |
| `ARC-005` | architectural_commitment | active | 0.799 | 3 |
| `ARC-014` | architectural_commitment | active | 0.784 | 3 |
| `ARC-011` | architectural_commitment | active | 0.776 | 1 |
| `ARC-001` | architectural_commitment | active | 0.685 | 1 |
| `INV-014` | invariant | active | 0.685 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.860 | 11 |
| `Q-016` | open_question | active | 0.851 | 5 |
| `Q-015` | open_question | active | 0.832 | 5 |
| `Q-005` | open_question | active | 0.801 | 4 |
| `Q-020` | open_question | resolved | 0.775 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.668 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **48**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.193 | 1 |
| `MECH-150` | candidate | 0.199 | 1 |
| `MECH-165` | candidate | 0.210 | 1 |
| `SD-018` | implemented | 0.213 | 1 |
| `MECH-188` | candidate | 0.214 | 1 |
| `SD-023` | candidate | 0.239 | 1 |
| `ARC-032` | candidate | 0.240 | 2 |
| `MECH-116` | candidate | 0.240 | 2 |
| `MECH-220` | candidate | 0.240 | 1 |
| `SD-032c` | - | 0.244 | 1 |
| `MECH-091` | candidate | 0.245 | 1 |
| `MECH-120` | candidate | 0.264 | 2 |
| `MECH-186` | candidate | 0.264 | 2 |
| `MECH-155` | candidate | 0.266 | 2 |
| `SD-047` | provisional | 0.275 | 1 |
| `MECH-166` | candidate | 0.286 | 1 |
| `MECH-128` | candidate | 0.299 | 3 |
| `MECH-314` | candidate_substrate_landed | 0.301 | 1 |
| `SD-037` | candidate | 0.312 | 1 |
| `MECH-047` | provisional | 0.330 | 1 |
| `INV-054` | candidate | 0.343 | 3 |
| `SD-021` | candidate | 0.344 | 3 |
| `MECH-320` | candidate_substrate_landed | 0.351 | 2 |
| `MECH-026` | provisional | 0.354 | 1 |
| `MECH-029` | provisional | 0.354 | 1 |
| `MECH-334` | candidate | 0.355 | 2 |
| `MECH-022` | provisional | 0.357 | 1 |
| `MECH-025` | candidate | 0.359 | 1 |
| `SD-049` | candidate | 0.368 | 2 |
| `MECH-070` | retiring | 0.373 | 4 |
| ... | ... | ... | ... (18 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **131**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.927 | 5 |
| `MECH-265` | candidate | 0.909 | 6 |
| `MECH-163` | candidate | 0.907 | 11 |
| `MECH-263` | candidate | 0.906 | 4 |
| `SD-033b` | - | 0.902 | 5 |
| `MECH-271` | candidate | 0.901 | 4 |
| `MECH-279` | candidate | 0.899 | 5 |
| `MECH-CBBL-PROPOSED` | - | 0.898 | 7 |
| `Q-035` | resolved | 0.898 | 15 |
| `MECH-317` | candidate | 0.894 | 9 |
| `MECH-180` | candidate | 0.892 | 4 |
| `SD-033e` | - | 0.891 | 10 |
| `DEV-NEED-009` | - | 0.890 | 4 |
| `MECH-122` | provisional | 0.890 | 4 |
| `MECH-292` | candidate | 0.889 | 24 |
| `MECH-267` | provisional | 0.888 | 5 |
| `MECH-288` | candidate | 0.888 | 11 |
| `MECH-293` | candidate | 0.888 | 12 |
| `MECH-030` | provisional | 0.887 | 4 |
| `SD-014` | candidate | 0.887 | 13 |
| `MECH-172` | candidate | 0.886 | 6 |
| `ARC-049` | candidate | 0.885 | 27 |
| `MECH-191` | candidate | 0.885 | 4 |
| `MECH-074` | provisional | 0.884 | 9 |
| `DEV-NEED-012` | - | 0.882 | 6 |
| `MECH-092` | candidate | 0.882 | 16 |
| `MECH-203` | candidate | 0.882 | 7 |
| `MECH-046` | provisional | 0.880 | 4 |
| `MECH-316` | candidate | 0.880 | 9 |
| `SD-054` | candidate | 0.879 | 6 |
| `ARC-060` | candidate | 0.876 | 13 |
| `MECH-171` | candidate | 0.875 | 4 |
| `MECH-198` | candidate | 0.875 | 8 |
| `MECH-295` | candidate | 0.875 | 6 |
| `MECH-337` | candidate | 0.875 | 4 |
| `SD-039` | candidate | 0.875 | 6 |
| `MECH-294` | candidate | 0.873 | 9 |
| `MECH-197` | candidate | 0.872 | 12 |
| `MECH-285` | candidate | 0.872 | 16 |
| `MECH-168` | candidate | 0.870 | 4 |
| `MECH-269` | candidate | 0.869 | 34 |
| `MECH-303` | candidate | 0.869 | 4 |
| `ARC-078` | candidate | 0.868 | 9 |
| `MECH-264` | candidate | 0.865 | 3 |
| `INV-048` | candidate | 0.862 | 4 |
| `MECH-057b` | - | 0.862 | 4 |
| `SD-003-SUCCESSOR` | - | 0.862 | 4 |
| `MECH-312` | candidate | 0.861 | 14 |
| `MECH-275` | candidate | 0.859 | 6 |
| `SD-032d` | - | 0.859 | 4 |
| ... | ... | ... | ... (81 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
