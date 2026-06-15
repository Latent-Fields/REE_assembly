# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-15T16:18:45.204591Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 323 |
| `substrate_coherence` | 60 |
| `answer_state` | 46 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **65** | plausible_unproven: **356** |
| **low lit**             | novel_discovery: **4**         | speculative: **4** |

Total scored claims: 429

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **240** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.808 | 0.000 | 0.808 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.860 | 0.000 | 0.860 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.851 | 0.000 | 0.851 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.861 | 0.000 | 0.861 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.884 | 0.000 | 0.884 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.722 | 0.000 | 0.722 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.877 | 0.000 | 0.877 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.805 | 0.000 | 0.805 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.822 | 0.000 | 0.822 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.722 | 0.000 | 0.722 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.629 | 0.000 | 0.629 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.849 | 0.000 | 0.849 | 0 | 4 | plausible_unproven |
| `INV-041` | invariant | candidate | 0.638 | 0.000 | 0.638 | 0 | 1 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.836 | 0.000 | 0.836 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.642 | 0.000 | 0.642 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.701 | 0.000 | 0.701 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.701 | 0.000 | 0.701 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.839 | 0.000 | 0.839 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.723 | 0.000 | 0.723 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.850 | 0.000 | 0.850 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.638 | 0.000 | 0.638 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.725 | 0.000 | 0.725 | 0 | 2 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.798 | 0.000 | 0.798 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.750 | 0.000 | 0.750 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.823 | 0.000 | 0.823 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.807 | 0.000 | 0.807 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.843 | 0.000 | 0.843 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.680 | 0.000 | 0.680 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.878 | 0.000 | 0.878 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.824 | 0.000 | 0.824 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 3 | plausible_unproven |
| `MECH-086` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.922 | 0.000 | 0.922 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.884 | 0.000 | 0.884 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.835 | 0.000 | 0.835 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.782 | 0.000 | 0.782 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.720 | 0.000 | 0.720 | 0 | 1 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.705 | 0.000 | 0.705 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 11 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 3 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.881 | 0.000 | 0.881 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.706 | 0.000 | 0.706 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.731 | 0.000 | 0.731 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.819 | 0.000 | 0.819 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 11 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.727 | 0.000 | 0.727 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 7 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.710 | 0.000 | 0.710 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.828 | 0.000 | 0.828 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.709 | 0.000 | 0.709 | 0 | 1 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.700 | 0.000 | 0.700 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.900 | 0.000 | 0.900 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.840 | 0.000 | 0.840 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.883 | 0.000 | 0.883 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.830 | 0.000 | 0.830 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.896 | 0.000 | 0.896 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 3 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 16 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 3 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.666 | 0.000 | 0.666 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.900 | 0.000 | 0.900 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.837 | 0.000 | 0.837 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.891 | 0.000 | 0.891 | 0 | 5 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.752 | 0.000 | 0.752 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.704 | 0.000 | 0.704 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 1 | plausible_unproven |
| `MECH-358` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.710 | 0.000 | 0.710 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.670 | 0.000 | 0.670 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.709 | 0.000 | 0.709 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 1 | plausible_unproven |
| `MECH-423` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 6 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.735 | 0.000 | 0.735 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `MECH-900` | - | - | 0.687 | 0.000 | 0.687 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.892 | 0.000 | 0.892 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.801 | 0.000 | 0.801 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.893 | 0.000 | 0.893 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.882 | 0.000 | 0.882 | 0 | 13 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.700 | 0.000 | 0.700 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.831 | 0.000 | 0.831 | 0 | 4 | plausible_unproven |
| `SD-032d` | - | - | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.816 | 0.000 | 0.816 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.897 | 0.000 | 0.897 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.888 | 0.000 | 0.888 | 0 | 12 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.842 | 0.000 | 0.842 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.818 | 0.000 | 0.818 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.870 | 0.000 | 0.870 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.747 | 0.000 | 0.747 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.787 | 0.000 | 0.787 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.918 | 0.000 | 0.918 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.821 | 0.000 | 0.821 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.798 | 0.000 | 0.798 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.871 | 0.000 | 0.871 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `SD-059` | design_decision | candidate | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.637 | 0.149 | 0.800 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.654 | 0.167 | 0.817 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.640 | 0.171 | 0.797 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.693 | 0.196 | 0.859 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.694 | 0.196 | 0.860 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.642 | 0.201 | 0.789 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.682 | 0.202 | 0.842 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.630 | 0.221 | 0.902 | 2 | 11 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.680 | 0.232 | 0.829 | 1 | 10 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.716 | 0.287 | 0.859 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.721 | 0.311 | 0.858 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.724 | 0.311 | 0.862 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.727 | 0.314 | 0.864 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.738 | 0.316 | 0.879 | 1 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.724 | 0.324 | 0.857 | 1 | 4 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.658 | 0.341 | 0.870 | 2 | 6 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.632 | 0.382 | 0.883 | 5 | 7 | plausible_unproven |
| `SD-032b` | - | - | 0.653 | 0.422 | 0.884 | 10 | 16 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.734 | 0.432 | 0.835 | 1 | 3 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.637 | 0.436 | 0.838 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.777 | 0.451 | 0.886 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.682 | 0.463 | 0.792 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.733 | 0.463 | 0.823 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.683 | 0.467 | 0.900 | 7 | 10 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.672 | 0.510 | 0.834 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.644 | 0.511 | 0.777 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.711 | 0.531 | 0.890 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.720 | 0.539 | 0.900 | 19 | 9 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.745 | 0.561 | 0.867 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.684 | 0.564 | 0.805 | 28 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.786 | 0.575 | 0.857 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.774 | 0.575 | 0.841 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.749 | 0.575 | 0.807 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.768 | 0.575 | 0.833 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.775 | 0.575 | 0.842 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.744 | 0.575 | 0.800 | 1 | 3 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.708 | 0.585 | 0.831 | 83 | 7 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.731 | 0.594 | 0.867 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.701 | 0.596 | 0.807 | 9 | 13 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.731 | 0.607 | 0.854 | 5 | 5 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.732 | 0.611 | 0.853 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.708 | 0.614 | 0.802 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.701 | 0.615 | 0.786 | 5 | 6 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.739 | 0.616 | 0.861 | 5 | 25 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.792 | 0.619 | 0.850 | 1 | 7 | plausible_unproven |

_Suppressed by gating: 52 substrate_coherence (ARC + universal invariant), 33 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.893 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.860 | 3 |
| `ARC-003` | architectural_commitment | active | 0.793 | 3 |
| `ARC-005` | architectural_commitment | active | 0.793 | 3 |
| `ARC-014` | architectural_commitment | active | 0.779 | 3 |
| `ARC-011` | architectural_commitment | active | 0.770 | 1 |
| `ARC-001` | architectural_commitment | active | 0.680 | 1 |
| `INV-014` | invariant | active | 0.680 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.855 | 11 |
| `Q-016` | open_question | active | 0.846 | 5 |
| `Q-015` | open_question | active | 0.827 | 5 |
| `Q-005` | open_question | active | 0.796 | 4 |
| `Q-020` | open_question | resolved | 0.770 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **4**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-346` | candidate | 0.758 | 0.000 | 1 | 0 |
| `MECH-347` | candidate | 0.758 | 0.000 | 1 | 0 |
| `SD-057` | candidate | 0.758 | 0.000 | 1 | 0 |
| `onboarding` | - | 0.625 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **44**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.149 | 1 |
| `MECH-150` | candidate | 0.156 | 1 |
| `MECH-165` | candidate | 0.167 | 1 |
| `SD-018` | implemented | 0.170 | 1 |
| `MECH-188` | candidate | 0.171 | 1 |
| `MECH-220` | candidate | 0.196 | 1 |
| `SD-023` | candidate | 0.196 | 1 |
| `ARC-032` | candidate | 0.197 | 2 |
| `MECH-116` | candidate | 0.197 | 2 |
| `SD-032c` | - | 0.201 | 1 |
| `MECH-091` | candidate | 0.202 | 1 |
| `MECH-120` | candidate | 0.221 | 2 |
| `MECH-186` | candidate | 0.221 | 2 |
| `MECH-155` | candidate | 0.223 | 2 |
| `SD-047` | provisional | 0.232 | 1 |
| `MECH-128` | candidate | 0.256 | 3 |
| `MECH-047` | provisional | 0.287 | 1 |
| `INV-054` | candidate | 0.299 | 3 |
| `SD-021` | candidate | 0.301 | 3 |
| `MECH-026` | provisional | 0.311 | 1 |
| `MECH-029` | provisional | 0.311 | 1 |
| `MECH-022` | provisional | 0.314 | 1 |
| `MECH-025` | candidate | 0.316 | 1 |
| `MECH-057b` | - | 0.324 | 1 |
| `MECH-070` | retiring | 0.330 | 4 |
| `MECH-153` | candidate | 0.335 | 4 |
| `MECH-099` | candidate | 0.339 | 6 |
| `MECH-295` | candidate | 0.341 | 2 |
| `MECH-097` | candidate | 0.363 | 1 |
| `MECH-075` | candidate | 0.382 | 5 |
| ... | ... | ... | ... (14 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **199**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.922 | 5 |
| `SD-045` | candidate | 0.918 | 4 |
| `MECH-279` | candidate | 0.905 | 6 |
| `MECH-163` | candidate | 0.901 | 11 |
| `MECH-263` | candidate | 0.900 | 4 |
| `MECH-304` | candidate | 0.900 | 4 |
| `SD-033b` | - | 0.897 | 5 |
| `MECH-271` | candidate | 0.896 | 4 |
| `Q-035` | resolved | 0.893 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.892 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.891 | 5 |
| `MECH-166` | candidate | 0.889 | 4 |
| `MECH-317` | candidate | 0.889 | 9 |
| `MECH-265` | candidate | 0.888 | 8 |
| `SD-033e` | - | 0.888 | 12 |
| `MECH-180` | candidate | 0.887 | 4 |
| `DEV-NEED-009` | - | 0.884 | 4 |
| `MECH-122` | provisional | 0.884 | 4 |
| `MECH-292` | candidate | 0.884 | 24 |
| `MECH-267` | provisional | 0.883 | 5 |
| `MECH-293` | candidate | 0.883 | 12 |
| `MECH-030` | provisional | 0.882 | 4 |
| `MECH-264` | candidate | 0.882 | 6 |
| `MECH-288` | candidate | 0.882 | 11 |
| `SD-014` | candidate | 0.882 | 13 |
| `MECH-172` | candidate | 0.881 | 6 |
| `ARC-049` | candidate | 0.879 | 27 |
| `MECH-191` | candidate | 0.879 | 4 |
| `MECH-074` | provisional | 0.878 | 9 |
| `DEV-NEED-012` | - | 0.877 | 6 |
| `MECH-203` | candidate | 0.877 | 7 |
| `MECH-092` | candidate | 0.876 | 16 |
| `MECH-046` | provisional | 0.875 | 4 |
| `MECH-316` | candidate | 0.874 | 9 |
| `ARC-060` | candidate | 0.871 | 13 |
| `MECH-303` | candidate | 0.871 | 5 |
| `SD-054` | candidate | 0.871 | 7 |
| `MECH-337` | candidate | 0.870 | 4 |
| `SD-039` | candidate | 0.870 | 6 |
| `ARC-078` | candidate | 0.869 | 11 |
| `MECH-171` | candidate | 0.869 | 4 |
| `MECH-198` | candidate | 0.869 | 8 |
| `MECH-334` | candidate | 0.868 | 3 |
| `MECH-294` | candidate | 0.867 | 9 |
| `MECH-197` | candidate | 0.866 | 12 |
| `MECH-285` | candidate | 0.866 | 16 |
| `MECH-168` | candidate | 0.864 | 4 |
| `MECH-269` | candidate | 0.864 | 34 |
| `MECH-280` | candidate | 0.864 | 5 |
| `MECH-281` | candidate | 0.864 | 4 |
| ... | ... | ... | ... (149 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
