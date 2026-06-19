# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-19T21:42:19.704667Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 331 |
| `substrate_coherence` | 61 |
| `answer_state` | 51 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **68** | plausible_unproven: **370** |
| **low lit**             | novel_discovery: **0**         | speculative: **5** |

Total scored claims: 443

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **248** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.849 | 0.000 | 0.849 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.850 | 0.000 | 0.850 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.860 | 0.000 | 0.860 | 0 | 5 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.883 | 0.000 | 0.883 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.721 | 0.000 | 0.721 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.876 | 0.000 | 0.876 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.804 | 0.000 | 0.804 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.821 | 0.000 | 0.821 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.721 | 0.000 | 0.721 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.628 | 0.000 | 0.628 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.848 | 0.000 | 0.848 | 0 | 4 | plausible_unproven |
| `INV-041` | invariant | candidate | 0.637 | 0.000 | 0.637 | 0 | 1 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.835 | 0.000 | 0.835 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.641 | 0.000 | 0.641 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.856 | 0.000 | 0.856 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.838 | 0.000 | 0.838 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.722 | 0.000 | 0.722 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.849 | 0.000 | 0.849 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.637 | 0.000 | 0.637 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.723 | 0.000 | 0.723 | 0 | 2 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.748 | 0.000 | 0.748 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.822 | 0.000 | 0.822 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.806 | 0.000 | 0.806 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.856 | 0.000 | 0.856 | 0 | 7 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.874 | 0.000 | 0.874 | 0 | 4 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.842 | 0.000 | 0.842 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.679 | 0.000 | 0.679 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.877 | 0.000 | 0.877 | 0 | 9 | plausible_unproven |
| `MECH-074c` | - | - | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.822 | 0.000 | 0.822 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 3 | plausible_unproven |
| `MECH-086` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 3 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.921 | 0.000 | 0.921 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.883 | 0.000 | 0.883 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 3 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.718 | 0.000 | 0.718 | 0 | 1 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.704 | 0.000 | 0.704 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.900 | 0.000 | 0.900 | 0 | 11 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.880 | 0.000 | 0.880 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.705 | 0.000 | 0.705 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.729 | 0.000 | 0.729 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.817 | 0.000 | 0.817 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.716 | 0.000 | 0.716 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 11 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.808 | 0.000 | 0.808 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.716 | 0.000 | 0.716 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.726 | 0.000 | 0.726 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 7 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.708 | 0.000 | 0.708 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.826 | 0.000 | 0.826 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.708 | 0.000 | 0.708 | 0 | 1 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.698 | 0.000 | 0.698 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.899 | 0.000 | 0.899 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 6 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.839 | 0.000 | 0.839 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.881 | 0.000 | 0.881 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.829 | 0.000 | 0.829 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.845 | 0.000 | 0.845 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.895 | 0.000 | 0.895 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.904 | 0.000 | 0.904 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 3 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 16 | plausible_unproven |
| `MECH-286` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 3 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.665 | 0.000 | 0.665 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 5 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.899 | 0.000 | 0.899 | 0 | 4 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.890 | 0.000 | 0.890 | 0 | 5 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.703 | 0.000 | 0.703 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 1 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.668 | 0.000 | 0.668 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 1 | plausible_unproven |
| `MECH-400` | mechanism_hypothesis | candidate | 0.629 | 0.000 | 0.629 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.718 | 0.000 | 0.718 | 0 | 1 | plausible_unproven |
| `MECH-423` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 6 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.733 | 0.000 | 0.733 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `MECH-436` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 2 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `MECH-900` | - | - | 0.686 | 0.000 | 0.686 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.891 | 0.000 | 0.891 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.800 | 0.000 | 0.800 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.892 | 0.000 | 0.892 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.881 | 0.000 | 0.881 | 0 | 13 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.698 | 0.000 | 0.698 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.830 | 0.000 | 0.830 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.882 | 0.000 | 0.882 | 0 | 16 | plausible_unproven |
| `SD-032d` | - | - | 0.852 | 0.000 | 0.852 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.814 | 0.000 | 0.814 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.896 | 0.000 | 0.896 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.887 | 0.000 | 0.887 | 0 | 12 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.841 | 0.000 | 0.841 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.817 | 0.000 | 0.817 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.856 | 0.000 | 0.856 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.869 | 0.000 | 0.869 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.746 | 0.000 | 0.746 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.786 | 0.000 | 0.786 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.917 | 0.000 | 0.917 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.820 | 0.000 | 0.820 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.796 | 0.000 | 0.796 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.870 | 0.000 | 0.870 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.634 | 0.140 | 0.799 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.651 | 0.158 | 0.816 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.637 | 0.162 | 0.796 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.691 | 0.186 | 0.859 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.690 | 0.187 | 0.858 | 1 | 4 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.679 | 0.192 | 0.841 | 1 | 6 | plausible_unproven |
| `SD-032c` | - | - | 0.639 | 0.192 | 0.788 | 1 | 3 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.625 | 0.212 | 0.901 | 2 | 11 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.676 | 0.223 | 0.827 | 1 | 10 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.713 | 0.278 | 0.858 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.718 | 0.302 | 0.857 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.721 | 0.302 | 0.861 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.723 | 0.304 | 0.863 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.735 | 0.307 | 0.878 | 1 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.721 | 0.314 | 0.856 | 1 | 4 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.654 | 0.332 | 0.868 | 2 | 6 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.627 | 0.372 | 0.882 | 5 | 7 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.778 | 0.423 | 0.896 | 1 | 5 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.632 | 0.427 | 0.837 | 24 | 9 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.774 | 0.442 | 0.885 | 1 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.678 | 0.453 | 0.791 | 1 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.730 | 0.453 | 0.822 | 1 | 3 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.678 | 0.458 | 0.899 | 7 | 10 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.666 | 0.500 | 0.833 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.639 | 0.502 | 0.776 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.705 | 0.522 | 0.889 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.714 | 0.529 | 0.899 | 19 | 9 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.740 | 0.552 | 0.866 | 2 | 5 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.679 | 0.555 | 0.804 | 28 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.785 | 0.575 | 0.855 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.774 | 0.575 | 0.840 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.748 | 0.575 | 0.805 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.768 | 0.575 | 0.832 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.774 | 0.575 | 0.841 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.743 | 0.575 | 0.799 | 1 | 3 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.703 | 0.576 | 0.830 | 83 | 7 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.725 | 0.584 | 0.866 | 12 | 10 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.697 | 0.587 | 0.806 | 9 | 13 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.725 | 0.597 | 0.853 | 5 | 5 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.727 | 0.601 | 0.852 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.703 | 0.605 | 0.800 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.696 | 0.606 | 0.785 | 5 | 6 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.733 | 0.606 | 0.860 | 5 | 25 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.789 | 0.610 | 0.849 | 1 | 7 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.807 | 0.617 | 0.870 | 1 | 4 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.704 | 0.619 | 0.789 | 3 | 5 | plausible_unproven |

_Suppressed by gating: 54 substrate_coherence (ARC + universal invariant), 38 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.892 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.859 | 3 |
| `ARC-003` | architectural_commitment | active | 0.792 | 3 |
| `ARC-005` | architectural_commitment | active | 0.792 | 3 |
| `ARC-014` | architectural_commitment | active | 0.778 | 3 |
| `ARC-011` | architectural_commitment | active | 0.769 | 1 |
| `ARC-001` | architectural_commitment | active | 0.679 | 1 |
| `INV-014` | invariant | active | 0.679 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.853 | 11 |
| `Q-016` | open_question | active | 0.844 | 5 |
| `Q-015` | open_question | active | 0.826 | 5 |
| `Q-005` | open_question | active | 0.795 | 4 |
| `Q-020` | open_question | resolved | 0.769 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **0**.

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **43**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.140 | 1 |
| `MECH-150` | candidate | 0.146 | 1 |
| `MECH-165` | candidate | 0.158 | 1 |
| `SD-018` | implemented | 0.160 | 1 |
| `MECH-188` | candidate | 0.162 | 1 |
| `SD-023` | candidate | 0.186 | 1 |
| `MECH-220` | candidate | 0.187 | 1 |
| `ARC-032` | candidate | 0.188 | 2 |
| `MECH-116` | candidate | 0.188 | 2 |
| `MECH-091` | candidate | 0.192 | 1 |
| `SD-032c` | - | 0.192 | 1 |
| `MECH-120` | candidate | 0.212 | 2 |
| `MECH-186` | candidate | 0.212 | 2 |
| `MECH-155` | candidate | 0.214 | 2 |
| `SD-047` | provisional | 0.223 | 1 |
| `MECH-128` | candidate | 0.247 | 3 |
| `MECH-047` | provisional | 0.278 | 1 |
| `INV-054` | candidate | 0.290 | 3 |
| `SD-021` | candidate | 0.292 | 3 |
| `MECH-026` | provisional | 0.302 | 1 |
| `MECH-029` | provisional | 0.302 | 1 |
| `MECH-022` | provisional | 0.304 | 1 |
| `MECH-025` | candidate | 0.307 | 1 |
| `MECH-057b` | - | 0.314 | 1 |
| `MECH-070` | retiring | 0.320 | 4 |
| `MECH-153` | candidate | 0.325 | 4 |
| `MECH-099` | candidate | 0.329 | 6 |
| `MECH-295` | candidate | 0.332 | 2 |
| `MECH-097` | candidate | 0.354 | 1 |
| `MECH-075` | candidate | 0.372 | 5 |
| ... | ... | ... | ... (13 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **206**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.921 | 5 |
| `SD-045` | candidate | 0.917 | 4 |
| `MECH-279` | candidate | 0.904 | 6 |
| `MECH-163` | candidate | 0.900 | 11 |
| `MECH-263` | candidate | 0.899 | 4 |
| `MECH-304` | candidate | 0.899 | 4 |
| `SD-033b` | - | 0.896 | 5 |
| `MECH-271` | candidate | 0.895 | 4 |
| `Q-035` | resolved | 0.892 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.891 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.890 | 5 |
| `MECH-166` | candidate | 0.888 | 4 |
| `MECH-317` | candidate | 0.888 | 9 |
| `MECH-265` | candidate | 0.887 | 8 |
| `SD-033e` | - | 0.887 | 12 |
| `MECH-180` | candidate | 0.886 | 4 |
| `DEV-NEED-009` | - | 0.883 | 4 |
| `MECH-122` | provisional | 0.883 | 4 |
| `MECH-292` | candidate | 0.883 | 24 |
| `MECH-293` | candidate | 0.882 | 12 |
| `SD-032b` | - | 0.882 | 16 |
| `MECH-264` | candidate | 0.881 | 6 |
| `MECH-267` | provisional | 0.881 | 5 |
| `MECH-288` | candidate | 0.881 | 11 |
| `SD-014` | candidate | 0.881 | 13 |
| `MECH-030` | provisional | 0.880 | 4 |
| `MECH-172` | candidate | 0.880 | 6 |
| `ARC-049` | candidate | 0.878 | 27 |
| `MECH-191` | candidate | 0.878 | 4 |
| `MECH-074` | provisional | 0.877 | 9 |
| `DEV-NEED-012` | - | 0.876 | 6 |
| `MECH-203` | candidate | 0.876 | 7 |
| `MECH-092` | candidate | 0.875 | 16 |
| `MECH-046` | provisional | 0.874 | 4 |
| `MECH-316` | candidate | 0.873 | 9 |
| `ARC-060` | candidate | 0.870 | 13 |
| `MECH-303` | candidate | 0.870 | 5 |
| `SD-054` | candidate | 0.870 | 7 |
| `MECH-337` | candidate | 0.869 | 4 |
| `SD-039` | candidate | 0.869 | 6 |
| `MECH-171` | candidate | 0.868 | 4 |
| `MECH-198` | candidate | 0.868 | 8 |
| `ARC-078` | candidate | 0.867 | 11 |
| `MECH-294` | candidate | 0.866 | 9 |
| `MECH-334` | candidate | 0.866 | 3 |
| `MECH-197` | candidate | 0.865 | 12 |
| `MECH-285` | candidate | 0.865 | 16 |
| `MECH-168` | candidate | 0.863 | 4 |
| `MECH-269` | candidate | 0.863 | 34 |
| `MECH-280` | candidate | 0.863 | 5 |
| ... | ... | ... | ... (156 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
