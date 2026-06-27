# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-27T06:51:58.531007Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 339 |
| `substrate_coherence` | 64 |
| `answer_state` | 59 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **75** | plausible_unproven: **382** |
| **low lit**             | novel_discovery: **0**         | speculative: **5** |

Total scored claims: 462

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **249** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.848 | 0.000 | 0.848 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.858 | 0.000 | 0.858 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.881 | 0.000 | 0.881 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.719 | 0.000 | 0.719 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.874 | 0.000 | 0.874 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.819 | 0.000 | 0.819 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.719 | 0.000 | 0.719 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.626 | 0.000 | 0.626 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `INV-041` | invariant | candidate | 0.635 | 0.000 | 0.635 | 0 | 1 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.833 | 0.000 | 0.833 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.639 | 0.000 | 0.639 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.836 | 0.000 | 0.836 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.720 | 0.000 | 0.720 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.847 | 0.000 | 0.847 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.635 | 0.000 | 0.635 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.721 | 0.000 | 0.721 | 0 | 2 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.746 | 0.000 | 0.746 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.820 | 0.000 | 0.820 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.728 | 0.000 | 0.728 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.804 | 0.000 | 0.804 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.878 | 0.000 | 0.878 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.854 | 0.000 | 0.854 | 0 | 7 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.844 | 0.000 | 0.844 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.840 | 0.000 | 0.840 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.677 | 0.000 | 0.677 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.875 | 0.000 | 0.875 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.820 | 0.000 | 0.820 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 3 | plausible_unproven |
| `MECH-086` | mechanism_hypothesis | candidate | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.792 | 0.000 | 0.792 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.919 | 0.000 | 0.919 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.881 | 0.000 | 0.881 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.716 | 0.000 | 0.716 | 0 | 1 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.702 | 0.000 | 0.702 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.898 | 0.000 | 0.898 | 0 | 11 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.878 | 0.000 | 0.878 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.812 | 0.000 | 0.812 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.703 | 0.000 | 0.703 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.727 | 0.000 | 0.727 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.714 | 0.000 | 0.714 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.787 | 0.000 | 0.787 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.714 | 0.000 | 0.714 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 7 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.706 | 0.000 | 0.706 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.706 | 0.000 | 0.706 | 0 | 1 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.696 | 0.000 | 0.696 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.897 | 0.000 | 0.897 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 6 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.837 | 0.000 | 0.837 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.879 | 0.000 | 0.879 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.827 | 0.000 | 0.827 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.843 | 0.000 | 0.843 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.893 | 0.000 | 0.893 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 3 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.838 | 0.000 | 0.838 | 0 | 15 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.663 | 0.000 | 0.663 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.897 | 0.000 | 0.897 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.888 | 0.000 | 0.888 | 0 | 5 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.686 | 0.000 | 0.686 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.701 | 0.000 | 0.701 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.706 | 0.000 | 0.706 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.666 | 0.000 | 0.666 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.706 | 0.000 | 0.706 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.706 | 0.000 | 0.706 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.696 | 0.000 | 0.696 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.696 | 0.000 | 0.696 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 1 | plausible_unproven |
| `MECH-400` | mechanism_hypothesis | candidate | 0.627 | 0.000 | 0.627 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.716 | 0.000 | 0.716 | 0 | 1 | plausible_unproven |
| `MECH-423` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 6 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.731 | 0.000 | 0.731 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.696 | 0.000 | 0.696 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 7 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `MECH-445` | mechanism_hypothesis | candidate | 0.661 | 0.000 | 0.661 | 0 | 2 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 3 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.860 | 0.000 | 0.860 | 0 | 4 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 4 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 5 | plausible_unproven |
| `MECH-900` | - | - | 0.684 | 0.000 | 0.684 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.889 | 0.000 | 0.889 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.798 | 0.000 | 0.798 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.890 | 0.000 | 0.890 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.735 | 0.000 | 0.735 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.879 | 0.000 | 0.879 | 0 | 13 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.696 | 0.000 | 0.696 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.828 | 0.000 | 0.828 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.880 | 0.000 | 0.880 | 0 | 16 | plausible_unproven |
| `SD-032d` | - | - | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.812 | 0.000 | 0.812 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.894 | 0.000 | 0.894 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.885 | 0.000 | 0.885 | 0 | 12 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.815 | 0.000 | 0.815 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.867 | 0.000 | 0.867 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.744 | 0.000 | 0.744 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.784 | 0.000 | 0.784 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.915 | 0.000 | 0.915 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.818 | 0.000 | 0.818 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.794 | 0.000 | 0.794 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.868 | 0.000 | 0.868 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.629 | 0.125 | 0.797 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.646 | 0.141 | 0.814 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.632 | 0.145 | 0.794 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.685 | 0.170 | 0.857 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.685 | 0.171 | 0.856 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.633 | 0.175 | 0.786 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.673 | 0.176 | 0.839 | 1 | 6 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.670 | 0.206 | 0.825 | 1 | 10 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.711 | 0.275 | 0.856 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.713 | 0.285 | 0.855 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.716 | 0.285 | 0.859 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.718 | 0.288 | 0.861 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.730 | 0.290 | 0.876 | 1 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.715 | 0.298 | 0.854 | 1 | 4 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.646 | 0.315 | 0.866 | 2 | 6 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.772 | 0.407 | 0.894 | 1 | 5 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.623 | 0.411 | 0.835 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.768 | 0.425 | 0.883 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.672 | 0.437 | 0.789 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.724 | 0.437 | 0.820 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.669 | 0.441 | 0.897 | 7 | 10 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.657 | 0.484 | 0.831 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.630 | 0.485 | 0.774 | 6 | 3 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.705 | 0.513 | 0.897 | 19 | 9 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.703 | 0.518 | 0.887 | 7 | 14 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.732 | 0.535 | 0.864 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.671 | 0.540 | 0.802 | 28 | 3 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.693 | 0.559 | 0.828 | 83 | 7 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.730 | 0.560 | 0.899 | 3 | 11 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.716 | 0.569 | 0.864 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.687 | 0.570 | 0.804 | 9 | 13 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.784 | 0.575 | 0.853 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.772 | 0.575 | 0.838 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.746 | 0.575 | 0.803 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.766 | 0.575 | 0.830 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.773 | 0.575 | 0.839 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.742 | 0.575 | 0.797 | 1 | 3 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.716 | 0.581 | 0.851 | 5 | 5 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.717 | 0.585 | 0.850 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.693 | 0.588 | 0.798 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.686 | 0.590 | 0.783 | 5 | 6 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.724 | 0.590 | 0.858 | 5 | 25 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.784 | 0.594 | 0.847 | 1 | 7 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.801 | 0.601 | 0.868 | 1 | 4 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.695 | 0.602 | 0.787 | 3 | 5 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.716 | 0.615 | 0.784 | 2 | 3 | plausible_unproven |

_Suppressed by gating: 55 substrate_coherence (ARC + universal invariant), 46 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.890 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.857 | 3 |
| `ARC-003` | architectural_commitment | active | 0.790 | 3 |
| `ARC-005` | architectural_commitment | active | 0.790 | 3 |
| `ARC-014` | architectural_commitment | active | 0.776 | 3 |
| `ARC-011` | architectural_commitment | active | 0.767 | 1 |
| `ARC-001` | architectural_commitment | active | 0.677 | 1 |
| `INV-014` | invariant | active | 0.677 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.851 | 11 |
| `Q-079` | open_question | resolved | 0.847 | 5 |
| `Q-016` | open_question | active | 0.842 | 5 |
| `Q-015` | open_question | active | 0.823 | 5 |
| `Q-005` | open_question | active | 0.793 | 4 |
| `Q-020` | open_question | resolved | 0.767 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **0**.

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **45**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-150` | candidate | 0.130 | 1 |
| `MECH-165` | candidate | 0.141 | 1 |
| `SD-018` | implemented | 0.144 | 1 |
| `MECH-188` | candidate | 0.145 | 1 |
| `SD-023` | candidate | 0.170 | 1 |
| `MECH-220` | candidate | 0.171 | 1 |
| `ARC-032` | candidate | 0.175 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `SD-032c` | - | 0.175 | 1 |
| `MECH-091` | candidate | 0.176 | 1 |
| `MECH-186` | candidate | 0.195 | 2 |
| `MECH-155` | candidate | 0.198 | 2 |
| `SD-047` | provisional | 0.206 | 1 |
| `MECH-128` | candidate | 0.230 | 3 |
| `INV-054` | candidate | 0.274 | 3 |
| `MECH-047` | provisional | 0.275 | 1 |
| `SD-021` | candidate | 0.275 | 3 |
| `MECH-026` | provisional | 0.285 | 1 |
| `MECH-029` | provisional | 0.285 | 1 |
| `MECH-022` | provisional | 0.288 | 1 |
| `MECH-025` | candidate | 0.290 | 1 |
| `MECH-057b` | - | 0.298 | 1 |
| `MECH-070` | retiring | 0.304 | 4 |
| `MECH-153` | candidate | 0.309 | 4 |
| `MECH-295` | candidate | 0.315 | 2 |
| `MECH-099` | candidate | 0.317 | 6 |
| `MECH-097` | candidate | 0.337 | 1 |
| `MECH-075` | candidate | 0.356 | 5 |
| `MECH-111` | candidate | 0.359 | 4 |
| ... | ... | ... | ... (15 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **207**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.919 | 5 |
| `SD-045` | candidate | 0.915 | 4 |
| `MECH-279` | candidate | 0.902 | 6 |
| `MECH-163` | candidate | 0.898 | 11 |
| `MECH-263` | candidate | 0.897 | 4 |
| `MECH-304` | candidate | 0.897 | 4 |
| `SD-033b` | - | 0.894 | 5 |
| `MECH-271` | candidate | 0.893 | 4 |
| `Q-035` | resolved | 0.890 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.889 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.888 | 5 |
| `MECH-166` | candidate | 0.886 | 4 |
| `MECH-317` | candidate | 0.886 | 9 |
| `MECH-265` | candidate | 0.885 | 8 |
| `SD-033e` | - | 0.885 | 12 |
| `MECH-180` | candidate | 0.884 | 4 |
| `DEV-NEED-009` | - | 0.881 | 4 |
| `MECH-122` | provisional | 0.881 | 4 |
| `MECH-292` | candidate | 0.881 | 24 |
| `MECH-293` | candidate | 0.880 | 12 |
| `SD-032b` | - | 0.880 | 16 |
| `MECH-264` | candidate | 0.879 | 6 |
| `MECH-267` | provisional | 0.879 | 5 |
| `MECH-288` | candidate | 0.879 | 11 |
| `SD-014` | candidate | 0.879 | 13 |
| `MECH-030` | provisional | 0.878 | 4 |
| `MECH-172` | candidate | 0.878 | 6 |
| `ARC-049` | candidate | 0.876 | 27 |
| `MECH-191` | candidate | 0.876 | 4 |
| `MECH-074` | provisional | 0.875 | 9 |
| `DEV-NEED-012` | - | 0.874 | 6 |
| `MECH-203` | candidate | 0.874 | 7 |
| `MECH-092` | candidate | 0.873 | 16 |
| `MECH-046` | provisional | 0.872 | 4 |
| `MECH-316` | candidate | 0.871 | 9 |
| `ARC-060` | candidate | 0.868 | 13 |
| `MECH-303` | candidate | 0.868 | 5 |
| `SD-054` | candidate | 0.868 | 7 |
| `MECH-337` | candidate | 0.867 | 4 |
| `SD-039` | candidate | 0.867 | 6 |
| `MECH-171` | candidate | 0.866 | 4 |
| `MECH-198` | candidate | 0.866 | 8 |
| `ARC-078` | candidate | 0.865 | 11 |
| `MECH-294` | candidate | 0.864 | 9 |
| `MECH-334` | candidate | 0.864 | 3 |
| `MECH-197` | candidate | 0.863 | 12 |
| `MECH-168` | candidate | 0.861 | 4 |
| `MECH-269` | candidate | 0.861 | 34 |
| `MECH-280` | candidate | 0.861 | 5 |
| `MECH-281` | candidate | 0.861 | 4 |
| ... | ... | ... | ... (157 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
