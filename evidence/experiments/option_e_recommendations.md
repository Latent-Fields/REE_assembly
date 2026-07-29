# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-07-28T17:43:29.417478Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 364 |
| `substrate_coherence` | 68 |
| `answer_state` | 73 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **87** | plausible_unproven: **410** |
| **low lit**             | novel_discovery: **0**         | speculative: **8** |

Total scored claims: 505

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **255** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.838 | 0.000 | 0.838 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.840 | 0.000 | 0.840 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.850 | 0.000 | 0.850 | 0 | 5 | plausible_unproven |
| `CDQ-007` | - | - | 0.789 | 0.000 | 0.789 | 0 | 8 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.865 | 0.000 | 0.865 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.837 | 0.000 | 0.837 | 0 | 4 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.824 | 0.000 | 0.824 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.630 | 0.000 | 0.630 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.689 | 0.000 | 0.689 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.623 | 0.000 | 0.623 | 0 | 4 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.845 | 0.000 | 0.845 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.827 | 0.000 | 0.827 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.711 | 0.000 | 0.711 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.838 | 0.000 | 0.838 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.627 | 0.000 | 0.627 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.844 | 0.000 | 0.844 | 0 | 5 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.738 | 0.000 | 0.738 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.811 | 0.000 | 0.811 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.720 | 0.000 | 0.720 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.795 | 0.000 | 0.795 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.870 | 0.000 | 0.870 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.845 | 0.000 | 0.845 | 0 | 7 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.835 | 0.000 | 0.835 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.735 | 0.000 | 0.735 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.743 | 0.000 | 0.743 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.832 | 0.000 | 0.832 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.668 | 0.000 | 0.668 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.867 | 0.000 | 0.867 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.812 | 0.000 | 0.812 | 0 | 4 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 3 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.784 | 0.000 | 0.784 | 0 | 3 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.784 | 0.000 | 0.784 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.819 | 0.000 | 0.819 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.910 | 0.000 | 0.910 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.787 | 0.000 | 0.787 | 0 | 3 | plausible_unproven |
| `MECH-140` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 2 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 1 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.693 | 0.000 | 0.693 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.792 | 0.000 | 0.792 | 0 | 3 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.869 | 0.000 | 0.869 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.694 | 0.000 | 0.694 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.705 | 0.000 | 0.705 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.705 | 0.000 | 0.705 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.715 | 0.000 | 0.715 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 8 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.698 | 0.000 | 0.698 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.816 | 0.000 | 0.816 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.697 | 0.000 | 0.697 | 0 | 1 | plausible_unproven |
| `MECH-232` | mechanism_hypothesis | provisional | 0.782 | 0.000 | 0.782 | 0 | 2 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 6 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.828 | 0.000 | 0.828 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.871 | 0.000 | 0.871 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.819 | 0.000 | 0.819 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 3 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 3 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.654 | 0.000 | 0.654 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 9 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.879 | 0.000 | 0.879 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.678 | 0.000 | 0.678 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.693 | 0.000 | 0.693 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.823 | 0.000 | 0.823 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.698 | 0.000 | 0.698 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.784 | 0.000 | 0.784 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.658 | 0.000 | 0.658 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.728 | 0.000 | 0.728 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.728 | 0.000 | 0.728 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.843 | 0.000 | 0.843 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 1 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.723 | 0.000 | 0.723 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.812 | 0.000 | 0.812 | 0 | 7 | plausible_unproven |
| `MECH-440` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 5 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 3 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 5 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 4 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 5 | plausible_unproven |
| `MECH-459` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.675 | 0.000 | 0.675 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.881 | 0.000 | 0.881 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.789 | 0.000 | 0.789 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.881 | 0.000 | 0.881 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.845 | 0.000 | 0.845 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.727 | 0.000 | 0.727 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.870 | 0.000 | 0.870 | 0 | 13 | plausible_unproven |
| `SD-024` | design_decision | candidate | 0.705 | 0.000 | 0.705 | 0 | 5 | plausible_unproven |
| `SD-025` | design_decision | candidate | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.688 | 0.000 | 0.688 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.819 | 0.000 | 0.819 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.872 | 0.000 | 0.872 | 0 | 16 | plausible_unproven |
| `SD-032d` | - | - | 0.842 | 0.000 | 0.842 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.804 | 0.000 | 0.804 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.885 | 0.000 | 0.885 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.876 | 0.000 | 0.876 | 0 | 12 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.806 | 0.000 | 0.806 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.845 | 0.000 | 0.845 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.858 | 0.000 | 0.858 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.735 | 0.000 | 0.735 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.906 | 0.000 | 0.906 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.809 | 0.000 | 0.809 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.786 | 0.000 | 0.786 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.860 | 0.000 | 0.860 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.743 | 0.000 | 0.743 | 0 | 2 | plausible_unproven |
| `SD-068` | design_decision | candidate | 0.801 | 0.000 | 0.801 | 0 | 4 | plausible_unproven |
| `SD-076` | design_decision | candidate | 0.725 | 0.000 | 0.725 | 0 | 4 | plausible_unproven |
| `SD-078` | design_decision | candidate_substrate_landed | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.666 | 0.105 | 0.853 | 1 | 5 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.654 | 0.125 | 0.830 | 1 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.622 | 0.125 | 0.788 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.635 | 0.125 | 0.805 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.621 | 0.125 | 0.786 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.666 | 0.125 | 0.847 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.667 | 0.125 | 0.848 | 1 | 4 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.646 | 0.135 | 0.817 | 1 | 10 | plausible_unproven |
| `MECH-057b` | - | - | 0.691 | 0.228 | 0.845 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.703 | 0.275 | 0.846 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.706 | 0.275 | 0.850 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.704 | 0.275 | 0.847 | 1 | 4 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.709 | 0.280 | 0.852 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.721 | 0.280 | 0.868 | 1 | 7 | plausible_unproven |
| `INV-088` | invariant | candidate | 0.687 | 0.289 | 0.820 | 1 | 4 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.668 | 0.312 | 0.787 | 1 | 5 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.746 | 0.327 | 0.886 | 1 | 6 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate | 0.752 | 0.337 | 0.890 | 1 | 6 | plausible_unproven |
| `MECH-457` | mechanism_hypothesis | candidate | 0.645 | 0.362 | 0.833 | 2 | 22 | plausible_unproven |
| `MECH-314b` | - | - | 0.642 | 0.367 | 0.780 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.747 | 0.367 | 0.874 | 1 | 6 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.642 | 0.396 | 0.888 | 7 | 10 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.677 | 0.410 | 0.855 | 2 | 5 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.666 | 0.443 | 0.889 | 19 | 9 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.634 | 0.472 | 0.795 | 9 | 13 | plausible_unproven |
| `SD-080` | design_decision | candidate | 0.724 | 0.475 | 0.807 | 1 | 3 | plausible_unproven |
| `MECH-324` | mechanism_hypothesis | candidate | 0.772 | 0.478 | 0.870 | 1 | 4 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.690 | 0.490 | 0.890 | 3 | 11 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.676 | 0.511 | 0.841 | 5 | 7 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.678 | 0.515 | 0.841 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.654 | 0.519 | 0.790 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.647 | 0.520 | 0.774 | 5 | 6 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.655 | 0.532 | 0.778 | 3 | 5 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.697 | 0.545 | 0.849 | 5 | 25 | plausible_unproven |
| `MECH-256` | mechanism_hypothesis | candidate | 0.703 | 0.558 | 0.847 | 6 | 9 | plausible_unproven |
| `INV-089` | invariant | provisional | 0.700 | 0.564 | 0.790 | 2 | 3 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | candidate | 0.693 | 0.564 | 0.822 | 11 | 24 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.718 | 0.567 | 0.869 | 3 | 14 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.712 | 0.569 | 0.855 | 12 | 10 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.778 | 0.575 | 0.845 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.766 | 0.575 | 0.829 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.740 | 0.575 | 0.795 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.760 | 0.575 | 0.821 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.766 | 0.575 | 0.830 | 1 | 8 | plausible_unproven |
| `MECH-062` | mechanism_hypothesis | candidate | 0.695 | 0.575 | 0.755 | 1 | 2 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.789 | 0.575 | 0.860 | 1 | 4 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.772 | 0.575 | 0.838 | 1 | 7 | plausible_unproven |
| `MECH-231` | mechanism_hypothesis | provisional | 0.720 | 0.575 | 0.769 | 1 | 3 | plausible_unproven |
| `MECH-259` | mechanism_hypothesis | stable | 0.672 | 0.575 | 0.720 | 1 | 2 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.788 | 0.575 | 0.859 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.735 | 0.575 | 0.788 | 1 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.792 | 0.575 | 0.865 | 1 | 20 | plausible_unproven |
| `SD-035` | design_decision | stable | 0.789 | 0.575 | 0.860 | 1 | 6 | plausible_unproven |
| `SD-048` | design_decision | candidate | 0.793 | 0.585 | 0.863 | 1 | 6 | plausible_unproven |
| `MECH-071` | mechanism_hypothesis | provisional | 0.722 | 0.588 | 0.856 | 38 | 4 | plausible_unproven |
| `SD-007` | design_decision | implemented | 0.723 | 0.593 | 0.854 | 19 | 5 | plausible_unproven |
| `SD-013` | design_decision | provisional | 0.727 | 0.608 | 0.845 | 4 | 4 | plausible_unproven |
| `MECH-106` | mechanism_hypothesis | provisional | 0.752 | 0.613 | 0.845 | 2 | 5 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.711 | 0.615 | 0.775 | 2 | 3 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.723 | 0.617 | 0.829 | 4 | 7 | plausible_unproven |

_Suppressed by gating: 55 substrate_coherence (ARC + universal invariant), 57 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.881 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.849 | 3 |
| `ARC-014` | architectural_commitment | active | 0.767 | 3 |
| `ARC-011` | architectural_commitment | active | 0.759 | 1 |
| `ARC-001` | architectural_commitment | active | 0.668 | 1 |
| `INV-014` | invariant | active | 0.668 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.843 | 11 |
| `Q-079` | open_question | resolved | 0.839 | 5 |
| `Q-016` | open_question | active | 0.834 | 5 |
| `Q-015` | open_question | active | 0.815 | 5 |
| `Q-005` | open_question | active | 0.784 | 4 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **0**.

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **57**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-155` | candidate | 0.105 | 1 |
| `MECH-091` | candidate | 0.125 | 1 |
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-150` | candidate | 0.125 | 1 |
| `MECH-165` | candidate | 0.125 | 1 |
| `MECH-188` | candidate | 0.125 | 1 |
| `MECH-220` | candidate | 0.125 | 1 |
| `SD-018` | implemented | 0.125 | 1 |
| `SD-023` | candidate | 0.125 | 1 |
| `SD-032c` | - | 0.125 | 1 |
| `SD-047` | provisional | 0.135 | 1 |
| `MECH-070` | retiring | 0.163 | 2 |
| `ARC-032` | candidate | 0.175 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `MECH-186` | candidate | 0.175 | 2 |
| `MECH-128` | candidate | 0.217 | 3 |
| `INV-054` | candidate | 0.225 | 3 |
| `SD-021` | candidate | 0.225 | 3 |
| `MECH-057b` | - | 0.228 | 1 |
| `MECH-295` | candidate | 0.246 | 2 |
| `MECH-075` | candidate | 0.263 | 4 |
| `MECH-026` | provisional | 0.275 | 1 |
| `MECH-029` | provisional | 0.275 | 1 |
| `MECH-047` | provisional | 0.275 | 1 |
| `MECH-445` | candidate | 0.278 | 1 |
| `MECH-022` | provisional | 0.280 | 1 |
| `MECH-025` | candidate | 0.280 | 1 |
| `MECH-097` | candidate | 0.280 | 1 |
| `MECH-156` | candidate | 0.280 | 1 |
| `INV-088` | candidate | 0.289 | 1 |
| ... | ... | ... | ... (27 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **203**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.910 | 5 |
| `SD-045` | candidate | 0.906 | 4 |
| `MECH-263` | candidate | 0.889 | 4 |
| `SD-033b` | - | 0.885 | 5 |
| `MECH-271` | candidate | 0.884 | 4 |
| `MECH-440` | candidate | 0.883 | 5 |
| `MECH-CBBL-PROPOSED` | - | 0.881 | 7 |
| `Q-035` | resolved | 0.881 | 15 |
| `MECH-203` | candidate | 0.879 | 8 |
| `MECH-320` | candidate_substrate_landed | 0.879 | 5 |
| `MECH-166` | candidate | 0.878 | 4 |
| `MECH-317` | candidate | 0.877 | 9 |
| `MECH-265` | candidate | 0.876 | 8 |
| `SD-033e` | - | 0.876 | 12 |
| `MECH-180` | candidate | 0.875 | 4 |
| `MECH-122` | provisional | 0.873 | 4 |
| `DEV-NEED-009` | - | 0.872 | 4 |
| `MECH-292` | candidate | 0.872 | 24 |
| `SD-032b` | - | 0.872 | 16 |
| `MECH-267` | provisional | 0.871 | 5 |
| `MECH-293` | candidate | 0.871 | 12 |
| `MECH-030` | provisional | 0.870 | 4 |
| `MECH-264` | candidate | 0.870 | 6 |
| `SD-014` | candidate | 0.870 | 13 |
| `MECH-172` | candidate | 0.869 | 6 |
| `MECH-191` | candidate | 0.868 | 4 |
| `ARC-049` | candidate | 0.867 | 27 |
| `MECH-074` | provisional | 0.867 | 9 |
| `DEV-NEED-012` | - | 0.865 | 6 |
| `MECH-316` | candidate | 0.862 | 9 |
| `SD-054` | candidate | 0.860 | 7 |
| `ARC-060` | candidate | 0.859 | 13 |
| `MECH-171` | candidate | 0.858 | 4 |
| `MECH-337` | candidate | 0.858 | 4 |
| `SD-039` | candidate | 0.858 | 6 |
| `ARC-078` | candidate | 0.857 | 11 |
| `MECH-198` | candidate | 0.857 | 8 |
| `MECH-334` | candidate | 0.856 | 3 |
| `MECH-294` | candidate | 0.855 | 9 |
| `MECH-197` | candidate | 0.854 | 12 |
| `MECH-168` | candidate | 0.853 | 4 |
| `MECH-280` | candidate | 0.853 | 5 |
| `MECH-434` | candidate | 0.853 | 4 |
| `MECH-269` | candidate | 0.852 | 34 |
| `MECH-281` | candidate | 0.852 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.850 | 5 |
| `ARC-051` | candidate | 0.849 | 4 |
| `INV-048` | candidate | 0.845 | 4 |
| `MECH-044` | provisional | 0.845 | 7 |
| `SD-003-SUCCESSOR` | - | 0.845 | 4 |
| ... | ... | ... | ... (153 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
