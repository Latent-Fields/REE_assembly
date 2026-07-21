# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-07-21T04:17:40.154779Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 353 |
| `substrate_coherence` | 67 |
| `answer_state` | 69 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **75** | plausible_unproven: **409** |
| **low lit**             | novel_discovery: **0**         | speculative: **5** |

Total scored claims: 489

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **256** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.742 | 0.000 | 0.742 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.840 | 0.000 | 0.840 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.842 | 0.000 | 0.842 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.852 | 0.000 | 0.852 | 0 | 5 | plausible_unproven |
| `CDQ-007` | - | - | 0.791 | 0.000 | 0.791 | 0 | 8 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.874 | 0.000 | 0.874 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.712 | 0.000 | 0.712 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.867 | 0.000 | 0.867 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.795 | 0.000 | 0.795 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.812 | 0.000 | 0.812 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.712 | 0.000 | 0.712 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.620 | 0.000 | 0.620 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.840 | 0.000 | 0.840 | 0 | 4 | plausible_unproven |
| `INV-041` | invariant | candidate | 0.629 | 0.000 | 0.629 | 0 | 1 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.826 | 0.000 | 0.826 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.632 | 0.000 | 0.632 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.625 | 0.000 | 0.625 | 0 | 4 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.713 | 0.000 | 0.713 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.840 | 0.000 | 0.840 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.629 | 0.000 | 0.629 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.846 | 0.000 | 0.846 | 0 | 5 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.740 | 0.000 | 0.740 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.813 | 0.000 | 0.813 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.722 | 0.000 | 0.722 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.797 | 0.000 | 0.797 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.847 | 0.000 | 0.847 | 0 | 7 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.837 | 0.000 | 0.837 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.834 | 0.000 | 0.834 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.670 | 0.000 | 0.670 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.869 | 0.000 | 0.869 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.814 | 0.000 | 0.814 | 0 | 4 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.743 | 0.000 | 0.743 | 0 | 3 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.912 | 0.000 | 0.912 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-140` | mechanism_hypothesis | candidate | 0.690 | 0.000 | 0.690 | 0 | 2 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.695 | 0.000 | 0.695 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 11 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.860 | 0.000 | 0.860 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.871 | 0.000 | 0.871 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.726 | 0.000 | 0.726 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.696 | 0.000 | 0.696 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.721 | 0.000 | 0.721 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.860 | 0.000 | 0.860 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 8 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.700 | 0.000 | 0.700 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.818 | 0.000 | 0.818 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `MECH-232` | mechanism_hypothesis | provisional | 0.784 | 0.000 | 0.784 | 0 | 2 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.690 | 0.000 | 0.690 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 6 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.830 | 0.000 | 0.830 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.873 | 0.000 | 0.873 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.821 | 0.000 | 0.821 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 3 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 3 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.656 | 0.000 | 0.656 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 9 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.881 | 0.000 | 0.881 | 0 | 5 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.742 | 0.000 | 0.742 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.860 | 0.000 | 0.860 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.680 | 0.000 | 0.680 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.695 | 0.000 | 0.695 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.700 | 0.000 | 0.700 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.660 | 0.000 | 0.660 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.699 | 0.000 | 0.699 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.690 | 0.000 | 0.690 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.690 | 0.000 | 0.690 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.845 | 0.000 | 0.845 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 1 | plausible_unproven |
| `MECH-400` | mechanism_hypothesis | candidate | 0.621 | 0.000 | 0.621 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.709 | 0.000 | 0.709 | 0 | 1 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.725 | 0.000 | 0.725 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.690 | 0.000 | 0.690 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 7 | plausible_unproven |
| `MECH-440` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 3 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 3 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 5 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.783 | 0.000 | 0.783 | 0 | 4 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 5 | plausible_unproven |
| `MECH-459` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.677 | 0.000 | 0.677 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.883 | 0.000 | 0.883 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.791 | 0.000 | 0.791 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.883 | 0.000 | 0.883 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.729 | 0.000 | 0.729 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.872 | 0.000 | 0.872 | 0 | 13 | plausible_unproven |
| `SD-025` | design_decision | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.690 | 0.000 | 0.690 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.821 | 0.000 | 0.821 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.874 | 0.000 | 0.874 | 0 | 16 | plausible_unproven |
| `SD-032d` | - | - | 0.844 | 0.000 | 0.844 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.806 | 0.000 | 0.806 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.887 | 0.000 | 0.887 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.878 | 0.000 | 0.878 | 0 | 12 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.808 | 0.000 | 0.808 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.860 | 0.000 | 0.860 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.737 | 0.000 | 0.737 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.909 | 0.000 | 0.909 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.811 | 0.000 | 0.811 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.788 | 0.000 | 0.788 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.862 | 0.000 | 0.862 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `SD-068` | design_decision | candidate | 0.803 | 0.000 | 0.803 | 0 | 4 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.655 | 0.125 | 0.832 | 1 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.625 | 0.125 | 0.791 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.637 | 0.125 | 0.808 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.622 | 0.125 | 0.788 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.668 | 0.125 | 0.849 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.669 | 0.125 | 0.850 | 1 | 4 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.652 | 0.153 | 0.819 | 1 | 10 | plausible_unproven |
| `MECH-057b` | - | - | 0.697 | 0.245 | 0.847 | 1 | 4 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.621 | 0.262 | 0.860 | 2 | 6 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.705 | 0.275 | 0.848 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.708 | 0.275 | 0.852 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.705 | 0.275 | 0.849 | 1 | 4 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.710 | 0.280 | 0.854 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.722 | 0.280 | 0.870 | 1 | 7 | plausible_unproven |
| `INV-088` | invariant | candidate | 0.693 | 0.306 | 0.822 | 1 | 4 | plausible_unproven |
| `MECH-457` | mechanism_hypothesis | candidate | 0.703 | 0.307 | 0.835 | 1 | 22 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate | 0.754 | 0.354 | 0.887 | 1 | 5 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.760 | 0.372 | 0.889 | 1 | 6 | plausible_unproven |
| `MECH-314b` | - | - | 0.649 | 0.384 | 0.782 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.753 | 0.384 | 0.876 | 1 | 6 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.643 | 0.396 | 0.890 | 7 | 10 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.675 | 0.460 | 0.891 | 19 | 9 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.707 | 0.482 | 0.857 | 2 | 5 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.663 | 0.506 | 0.821 | 83 | 7 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.700 | 0.507 | 0.892 | 3 | 11 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.657 | 0.517 | 0.797 | 9 | 13 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.700 | 0.518 | 0.881 | 7 | 14 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.685 | 0.528 | 0.843 | 5 | 7 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.688 | 0.532 | 0.843 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.664 | 0.535 | 0.792 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.656 | 0.536 | 0.776 | 5 | 6 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.668 | 0.540 | 0.795 | 28 | 3 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.698 | 0.545 | 0.851 | 5 | 25 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.664 | 0.549 | 0.780 | 3 | 5 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.713 | 0.569 | 0.857 | 12 | 10 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.779 | 0.575 | 0.847 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.767 | 0.575 | 0.831 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.742 | 0.575 | 0.797 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.761 | 0.575 | 0.823 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.768 | 0.575 | 0.832 | 1 | 8 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.790 | 0.575 | 0.862 | 1 | 4 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.774 | 0.575 | 0.840 | 1 | 7 | plausible_unproven |
| `MECH-256` | mechanism_hypothesis | candidate | 0.712 | 0.575 | 0.850 | 6 | 9 | plausible_unproven |
| `MECH-259` | mechanism_hypothesis | stable | 0.673 | 0.575 | 0.722 | 1 | 2 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.736 | 0.575 | 0.790 | 1 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.795 | 0.575 | 0.868 | 1 | 20 | plausible_unproven |
| `INV-089` | invariant | provisional | 0.708 | 0.581 | 0.792 | 2 | 3 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | candidate | 0.703 | 0.581 | 0.824 | 11 | 24 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.792 | 0.586 | 0.861 | 1 | 8 | plausible_unproven |
| `MECH-071` | mechanism_hypothesis | provisional | 0.723 | 0.588 | 0.858 | 38 | 4 | plausible_unproven |
| `MECH-062` | mechanism_hypothesis | candidate | 0.702 | 0.592 | 0.757 | 1 | 2 | plausible_unproven |
| `SD-035` | design_decision | stable | 0.794 | 0.592 | 0.862 | 1 | 6 | plausible_unproven |
| `SD-007` | design_decision | implemented | 0.724 | 0.593 | 0.856 | 19 | 5 | plausible_unproven |
| `SD-048` | design_decision | candidate | 0.799 | 0.602 | 0.865 | 1 | 6 | plausible_unproven |
| `SD-013` | design_decision | provisional | 0.728 | 0.608 | 0.847 | 4 | 4 | plausible_unproven |
| `MECH-106` | mechanism_hypothesis | provisional | 0.753 | 0.613 | 0.847 | 2 | 5 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.712 | 0.615 | 0.777 | 2 | 3 | plausible_unproven |
| `MECH-090` | mechanism_hypothesis | active | 0.658 | 0.617 | 0.700 | 18 | 19 | plausible_unproven |

_Suppressed by gating: 57 substrate_coherence (ARC + universal invariant), 54 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.883 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.851 | 3 |
| `ARC-003` | architectural_commitment | active | 0.784 | 3 |
| `ARC-005` | architectural_commitment | active | 0.784 | 3 |
| `ARC-014` | architectural_commitment | active | 0.769 | 3 |
| `ARC-011` | architectural_commitment | active | 0.761 | 1 |
| `ARC-001` | architectural_commitment | active | 0.670 | 1 |
| `INV-014` | invariant | active | 0.670 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.845 | 11 |
| `Q-079` | open_question | resolved | 0.841 | 5 |
| `Q-016` | open_question | active | 0.836 | 5 |
| `Q-015` | open_question | active | 0.817 | 5 |
| `Q-005` | open_question | active | 0.786 | 4 |
| `Q-020` | open_question | resolved | 0.760 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **0**.

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **57**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-091` | candidate | 0.125 | 1 |
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-150` | candidate | 0.125 | 1 |
| `MECH-165` | candidate | 0.125 | 1 |
| `MECH-188` | candidate | 0.125 | 1 |
| `MECH-220` | candidate | 0.125 | 1 |
| `SD-018` | implemented | 0.125 | 1 |
| `SD-023` | candidate | 0.125 | 1 |
| `SD-032c` | - | 0.125 | 1 |
| `MECH-155` | candidate | 0.153 | 2 |
| `SD-047` | provisional | 0.153 | 1 |
| `ARC-032` | candidate | 0.175 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `MECH-186` | candidate | 0.175 | 2 |
| `MECH-128` | candidate | 0.217 | 3 |
| `INV-054` | candidate | 0.225 | 3 |
| `SD-021` | candidate | 0.225 | 3 |
| `MECH-057b` | - | 0.245 | 1 |
| `MECH-070` | retiring | 0.259 | 4 |
| `MECH-295` | candidate | 0.262 | 2 |
| `MECH-153` | candidate | 0.264 | 4 |
| `MECH-026` | provisional | 0.275 | 1 |
| `MECH-029` | provisional | 0.275 | 1 |
| `MECH-047` | provisional | 0.275 | 1 |
| `MECH-022` | provisional | 0.280 | 1 |
| `MECH-025` | candidate | 0.280 | 1 |
| `MECH-097` | candidate | 0.284 | 1 |
| `MECH-445` | candidate | 0.294 | 1 |
| `INV-088` | candidate | 0.306 | 1 |
| `MECH-111` | candidate | 0.306 | 4 |
| ... | ... | ... | ... (27 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **203**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.912 | 5 |
| `SD-045` | candidate | 0.909 | 4 |
| `MECH-163` | candidate | 0.892 | 11 |
| `MECH-263` | candidate | 0.891 | 4 |
| `SD-033b` | - | 0.887 | 5 |
| `MECH-271` | candidate | 0.886 | 4 |
| `MECH-CBBL-PROPOSED` | - | 0.883 | 7 |
| `Q-035` | resolved | 0.883 | 15 |
| `MECH-203` | candidate | 0.881 | 8 |
| `MECH-320` | candidate_substrate_landed | 0.881 | 5 |
| `MECH-166` | candidate | 0.880 | 4 |
| `MECH-317` | candidate | 0.879 | 9 |
| `MECH-265` | candidate | 0.878 | 8 |
| `SD-033e` | - | 0.878 | 12 |
| `MECH-180` | candidate | 0.877 | 4 |
| `MECH-122` | provisional | 0.875 | 4 |
| `DEV-NEED-009` | - | 0.874 | 4 |
| `MECH-292` | candidate | 0.874 | 24 |
| `SD-032b` | - | 0.874 | 16 |
| `MECH-267` | provisional | 0.873 | 5 |
| `MECH-293` | candidate | 0.873 | 12 |
| `MECH-030` | provisional | 0.872 | 4 |
| `MECH-264` | candidate | 0.872 | 6 |
| `SD-014` | candidate | 0.872 | 13 |
| `MECH-172` | candidate | 0.871 | 6 |
| `MECH-191` | candidate | 0.870 | 4 |
| `ARC-049` | candidate | 0.869 | 27 |
| `MECH-074` | provisional | 0.869 | 9 |
| `DEV-NEED-012` | - | 0.867 | 6 |
| `MECH-316` | candidate | 0.865 | 9 |
| `SD-054` | candidate | 0.862 | 7 |
| `ARC-060` | candidate | 0.861 | 13 |
| `MECH-171` | candidate | 0.860 | 4 |
| `MECH-198` | candidate | 0.860 | 8 |
| `MECH-337` | candidate | 0.860 | 4 |
| `SD-039` | candidate | 0.860 | 6 |
| `ARC-078` | candidate | 0.859 | 11 |
| `MECH-294` | candidate | 0.858 | 9 |
| `MECH-334` | candidate | 0.858 | 3 |
| `MECH-197` | candidate | 0.857 | 12 |
| `MECH-168` | candidate | 0.855 | 4 |
| `MECH-280` | candidate | 0.855 | 5 |
| `MECH-434` | candidate | 0.855 | 4 |
| `MECH-269` | candidate | 0.854 | 34 |
| `MECH-281` | candidate | 0.854 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.852 | 5 |
| `ARC-051` | candidate | 0.851 | 4 |
| `INV-048` | candidate | 0.847 | 4 |
| `MECH-044` | provisional | 0.847 | 7 |
| `SD-003-SUCCESSOR` | - | 0.847 | 4 |
| ... | ... | ... | ... (153 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
