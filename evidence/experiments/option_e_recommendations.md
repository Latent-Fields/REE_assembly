# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-23T04:22:27.632736Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 335 |
| `substrate_coherence` | 63 |
| `answer_state` | 56 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **72** | plausible_unproven: **377** |
| **low lit**             | novel_discovery: **0**         | speculative: **5** |

Total scored claims: 454

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **249** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.848 | 0.000 | 0.848 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.849 | 0.000 | 0.849 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.859 | 0.000 | 0.859 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.720 | 0.000 | 0.720 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.875 | 0.000 | 0.875 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.820 | 0.000 | 0.820 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.720 | 0.000 | 0.720 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.627 | 0.000 | 0.627 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `INV-041` | invariant | candidate | 0.636 | 0.000 | 0.636 | 0 | 1 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.834 | 0.000 | 0.834 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.640 | 0.000 | 0.640 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.699 | 0.000 | 0.699 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.699 | 0.000 | 0.699 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.837 | 0.000 | 0.837 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.721 | 0.000 | 0.721 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.848 | 0.000 | 0.848 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.636 | 0.000 | 0.636 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.722 | 0.000 | 0.722 | 0 | 2 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.795 | 0.000 | 0.795 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.747 | 0.000 | 0.747 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.821 | 0.000 | 0.821 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.805 | 0.000 | 0.805 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.855 | 0.000 | 0.855 | 0 | 7 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.845 | 0.000 | 0.845 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.841 | 0.000 | 0.841 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.678 | 0.000 | 0.678 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.876 | 0.000 | 0.876 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.821 | 0.000 | 0.821 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 3 | plausible_unproven |
| `MECH-086` | mechanism_hypothesis | candidate | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.920 | 0.000 | 0.920 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 1 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.703 | 0.000 | 0.703 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.899 | 0.000 | 0.899 | 0 | 11 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.879 | 0.000 | 0.879 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.733 | 0.000 | 0.733 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.787 | 0.000 | 0.787 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.787 | 0.000 | 0.787 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.704 | 0.000 | 0.704 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.728 | 0.000 | 0.728 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.715 | 0.000 | 0.715 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 11 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.715 | 0.000 | 0.715 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.725 | 0.000 | 0.725 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 7 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.825 | 0.000 | 0.825 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.707 | 0.000 | 0.707 | 0 | 1 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.898 | 0.000 | 0.898 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 6 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.838 | 0.000 | 0.838 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.881 | 0.000 | 0.881 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.828 | 0.000 | 0.828 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.894 | 0.000 | 0.894 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 3 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 16 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 3 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.664 | 0.000 | 0.664 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.898 | 0.000 | 0.898 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.835 | 0.000 | 0.835 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.889 | 0.000 | 0.889 | 0 | 5 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.687 | 0.000 | 0.687 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.702 | 0.000 | 0.702 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.667 | 0.000 | 0.667 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.843 | 0.000 | 0.843 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 1 | plausible_unproven |
| `MECH-400` | mechanism_hypothesis | candidate | 0.628 | 0.000 | 0.628 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 1 | plausible_unproven |
| `MECH-423` | mechanism_hypothesis | candidate | 0.845 | 0.000 | 0.845 | 0 | 6 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 7 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-445` | mechanism_hypothesis | candidate | 0.662 | 0.000 | 0.662 | 0 | 2 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.685 | 0.000 | 0.685 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.890 | 0.000 | 0.890 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.799 | 0.000 | 0.799 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.891 | 0.000 | 0.891 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.880 | 0.000 | 0.880 | 0 | 13 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.697 | 0.000 | 0.697 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.881 | 0.000 | 0.881 | 0 | 16 | plausible_unproven |
| `SD-032d` | - | - | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.814 | 0.000 | 0.814 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.895 | 0.000 | 0.895 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.886 | 0.000 | 0.886 | 0 | 12 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.836 | 0.000 | 0.836 | 0 | 9 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.816 | 0.000 | 0.816 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.868 | 0.000 | 0.868 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.745 | 0.000 | 0.745 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.785 | 0.000 | 0.785 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.916 | 0.000 | 0.916 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.819 | 0.000 | 0.819 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.796 | 0.000 | 0.796 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.869 | 0.000 | 0.869 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.632 | 0.133 | 0.798 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.649 | 0.150 | 0.815 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.635 | 0.154 | 0.795 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.688 | 0.179 | 0.858 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.688 | 0.180 | 0.857 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.636 | 0.184 | 0.787 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.676 | 0.185 | 0.840 | 1 | 6 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.674 | 0.215 | 0.827 | 1 | 10 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.711 | 0.275 | 0.857 | 1 | 4 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.719 | 0.294 | 0.860 | 1 | 6 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.716 | 0.295 | 0.856 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.721 | 0.297 | 0.862 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.733 | 0.299 | 0.877 | 1 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.718 | 0.307 | 0.855 | 1 | 4 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.651 | 0.325 | 0.868 | 2 | 6 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.623 | 0.365 | 0.881 | 5 | 7 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.775 | 0.416 | 0.895 | 1 | 5 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.627 | 0.419 | 0.836 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.772 | 0.434 | 0.884 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.675 | 0.446 | 0.790 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.727 | 0.446 | 0.821 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.674 | 0.451 | 0.898 | 7 | 10 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.662 | 0.493 | 0.832 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.635 | 0.494 | 0.775 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.703 | 0.518 | 0.888 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.710 | 0.522 | 0.898 | 19 | 9 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.737 | 0.544 | 0.865 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.676 | 0.548 | 0.803 | 28 | 3 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.699 | 0.568 | 0.829 | 83 | 7 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.735 | 0.569 | 0.900 | 3 | 11 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.784 | 0.575 | 0.854 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.773 | 0.575 | 0.839 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.747 | 0.575 | 0.804 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.767 | 0.575 | 0.831 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.774 | 0.575 | 0.840 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.742 | 0.575 | 0.798 | 1 | 3 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.721 | 0.577 | 0.865 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.692 | 0.579 | 0.805 | 9 | 13 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.721 | 0.590 | 0.852 | 5 | 5 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.723 | 0.594 | 0.851 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.699 | 0.598 | 0.800 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.692 | 0.599 | 0.784 | 5 | 6 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.729 | 0.599 | 0.859 | 5 | 25 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.787 | 0.603 | 0.848 | 1 | 7 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.804 | 0.610 | 0.869 | 1 | 4 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.700 | 0.611 | 0.788 | 3 | 5 | plausible_unproven |

_Suppressed by gating: 54 substrate_coherence (ARC + universal invariant), 43 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.891 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.858 | 3 |
| `ARC-003` | architectural_commitment | active | 0.791 | 3 |
| `ARC-005` | architectural_commitment | active | 0.791 | 3 |
| `ARC-014` | architectural_commitment | active | 0.777 | 3 |
| `ARC-011` | architectural_commitment | active | 0.768 | 1 |
| `ARC-001` | architectural_commitment | active | 0.678 | 1 |
| `INV-014` | invariant | active | 0.678 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.853 | 11 |
| `Q-079` | open_question | resolved | 0.848 | 5 |
| `Q-016` | open_question | active | 0.844 | 5 |
| `Q-015` | open_question | active | 0.825 | 5 |
| `Q-005` | open_question | active | 0.794 | 4 |
| `Q-020` | open_question | resolved | 0.768 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **0**.

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **45**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.133 | 1 |
| `MECH-150` | candidate | 0.139 | 1 |
| `MECH-165` | candidate | 0.150 | 1 |
| `SD-018` | implemented | 0.153 | 1 |
| `MECH-188` | candidate | 0.154 | 1 |
| `SD-023` | candidate | 0.179 | 1 |
| `ARC-032` | candidate | 0.180 | 2 |
| `MECH-116` | candidate | 0.180 | 2 |
| `MECH-220` | candidate | 0.180 | 1 |
| `SD-032c` | - | 0.184 | 1 |
| `MECH-091` | candidate | 0.185 | 1 |
| `MECH-186` | candidate | 0.204 | 2 |
| `MECH-155` | candidate | 0.207 | 2 |
| `SD-047` | provisional | 0.215 | 1 |
| `MECH-128` | candidate | 0.239 | 3 |
| `MECH-047` | provisional | 0.275 | 1 |
| `INV-054` | candidate | 0.283 | 3 |
| `SD-021` | candidate | 0.284 | 3 |
| `MECH-029` | provisional | 0.294 | 1 |
| `MECH-026` | provisional | 0.295 | 1 |
| `MECH-022` | provisional | 0.297 | 1 |
| `MECH-025` | candidate | 0.299 | 1 |
| `MECH-057b` | - | 0.307 | 1 |
| `MECH-070` | retiring | 0.313 | 4 |
| `MECH-153` | candidate | 0.318 | 4 |
| `MECH-099` | candidate | 0.322 | 6 |
| `MECH-295` | candidate | 0.325 | 2 |
| `MECH-097` | candidate | 0.346 | 1 |
| `MECH-075` | candidate | 0.365 | 5 |
| `MECH-111` | candidate | 0.368 | 4 |
| ... | ... | ... | ... (15 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **207**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.920 | 5 |
| `SD-045` | candidate | 0.916 | 4 |
| `MECH-279` | candidate | 0.903 | 6 |
| `MECH-163` | candidate | 0.899 | 11 |
| `MECH-263` | candidate | 0.898 | 4 |
| `MECH-304` | candidate | 0.898 | 4 |
| `SD-033b` | - | 0.895 | 5 |
| `MECH-271` | candidate | 0.894 | 4 |
| `Q-035` | resolved | 0.891 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.890 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.889 | 5 |
| `MECH-166` | candidate | 0.887 | 4 |
| `MECH-317` | candidate | 0.887 | 9 |
| `MECH-265` | candidate | 0.886 | 8 |
| `SD-033e` | - | 0.886 | 12 |
| `MECH-180` | candidate | 0.885 | 4 |
| `DEV-NEED-009` | - | 0.882 | 4 |
| `MECH-122` | provisional | 0.882 | 4 |
| `MECH-292` | candidate | 0.882 | 24 |
| `MECH-267` | provisional | 0.881 | 5 |
| `MECH-293` | candidate | 0.881 | 12 |
| `SD-032b` | - | 0.881 | 16 |
| `MECH-030` | provisional | 0.880 | 4 |
| `MECH-264` | candidate | 0.880 | 6 |
| `MECH-288` | candidate | 0.880 | 11 |
| `SD-014` | candidate | 0.880 | 13 |
| `MECH-172` | candidate | 0.879 | 6 |
| `ARC-049` | candidate | 0.877 | 27 |
| `MECH-191` | candidate | 0.877 | 4 |
| `MECH-074` | provisional | 0.876 | 9 |
| `DEV-NEED-012` | - | 0.875 | 6 |
| `MECH-203` | candidate | 0.875 | 7 |
| `MECH-092` | candidate | 0.874 | 16 |
| `MECH-046` | provisional | 0.873 | 4 |
| `MECH-316` | candidate | 0.872 | 9 |
| `ARC-060` | candidate | 0.869 | 13 |
| `MECH-303` | candidate | 0.869 | 5 |
| `SD-054` | candidate | 0.869 | 7 |
| `MECH-337` | candidate | 0.868 | 4 |
| `SD-039` | candidate | 0.868 | 6 |
| `ARC-078` | candidate | 0.867 | 11 |
| `MECH-171` | candidate | 0.867 | 4 |
| `MECH-198` | candidate | 0.867 | 8 |
| `MECH-294` | candidate | 0.865 | 9 |
| `MECH-334` | candidate | 0.865 | 3 |
| `MECH-197` | candidate | 0.864 | 12 |
| `MECH-285` | candidate | 0.864 | 16 |
| `MECH-168` | candidate | 0.862 | 4 |
| `MECH-269` | candidate | 0.862 | 34 |
| `MECH-280` | candidate | 0.862 | 5 |
| ... | ... | ... | ... (157 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
