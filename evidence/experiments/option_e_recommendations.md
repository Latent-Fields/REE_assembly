# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-08-28T07:09:00.318245Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 408 |
| `substrate_coherence` | 73 |
| `answer_state` | 84 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **85** | plausible_unproven: **470** |
| **low lit**             | novel_discovery: **1**         | speculative: **9** |

Total scored claims: 565

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **288** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 26 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.830 | 0.000 | 0.830 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.831 | 0.000 | 0.831 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.841 | 0.000 | 0.841 | 0 | 5 | plausible_unproven |
| `CDQ-007` | - | - | 0.781 | 0.000 | 0.781 | 0 | 8 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.702 | 0.000 | 0.702 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.857 | 0.000 | 0.857 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.785 | 0.000 | 0.785 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.702 | 0.000 | 0.702 | 0 | 1 | plausible_unproven |
| `GOV-BEHADJ-1` | governance_rule | candidate | 0.826 | 0.000 | 0.826 | 0 | 9 | plausible_unproven |
| `GOV-INTERVENE-1` | governance_rule | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.816 | 0.000 | 0.816 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.622 | 0.000 | 0.622 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.837 | 0.000 | 0.837 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.925 | 0.000 | 0.925 | 0 | 8 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.703 | 0.000 | 0.703 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.830 | 0.000 | 0.830 | 0 | 5 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.836 | 0.000 | 0.836 | 0 | 5 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.777 | 0.000 | 0.777 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.729 | 0.000 | 0.729 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.803 | 0.000 | 0.803 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.712 | 0.000 | 0.712 | 0 | 2 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.702 | 0.000 | 0.702 | 0 | 1 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.831 | 0.000 | 0.831 | 0 | 6 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.827 | 0.000 | 0.827 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.880 | 0.000 | 0.880 | 0 | 6 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.790 | 0.000 | 0.790 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 5 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.812 | 0.000 | 0.812 | 0 | 4 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.742 | 0.000 | 0.742 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 3 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 3 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 5 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 8 | plausible_unproven |
| `MECH-130` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 5 | plausible_unproven |
| `MECH-140` | mechanism_hypothesis | candidate | 0.679 | 0.000 | 0.679 | 0 | 2 | plausible_unproven |
| `MECH-141` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.699 | 0.000 | 0.699 | 0 | 1 | plausible_unproven |
| `MECH-151` | mechanism_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 4 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.784 | 0.000 | 0.784 | 0 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.849 | 0.000 | 0.849 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.861 | 0.000 | 0.861 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.715 | 0.000 | 0.715 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 3 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.686 | 0.000 | 0.686 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.710 | 0.000 | 0.710 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 4 | plausible_unproven |
| `MECH-186` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 3 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.729 | 0.000 | 0.729 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 8 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.729 | 0.000 | 0.729 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.689 | 0.000 | 0.689 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.807 | 0.000 | 0.807 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.689 | 0.000 | 0.689 | 0 | 1 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 4 | plausible_unproven |
| `MECH-236` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 4 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.679 | 0.000 | 0.679 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 5 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.820 | 0.000 | 0.820 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.810 | 0.000 | 0.810 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `MECH-289` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 4 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.646 | 0.000 | 0.646 | 0 | 1 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.878 | 0.000 | 0.878 | 0 | 6 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 14 | plausible_unproven |
| `MECH-314c` | - | - | 0.866 | 0.000 | 0.866 | 0 | 6 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 6 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 6 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.871 | 0.000 | 0.871 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.669 | 0.000 | 0.669 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.684 | 0.000 | 0.684 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.649 | 0.000 | 0.649 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.679 | 0.000 | 0.679 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.679 | 0.000 | 0.679 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.730 | 0.000 | 0.730 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.699 | 0.000 | 0.699 | 0 | 1 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.714 | 0.000 | 0.714 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.679 | 0.000 | 0.679 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 7 | plausible_unproven |
| `MECH-440` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 5 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.745 | 0.000 | 0.745 | 0 | 3 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 5 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 4 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 5 | plausible_unproven |
| `MECH-459` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-471` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 3 | plausible_unproven |
| `MECH-472` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `MECH-481` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 4 | plausible_unproven |
| `MECH-487` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `MECH-489` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 5 | plausible_unproven |
| `MECH-490` | mechanism_hypothesis | candidate | 0.785 | 0.000 | 0.785 | 0 | 4 | plausible_unproven |
| `MECH-499` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 3 | plausible_unproven |
| `MECH-500` | mechanism_hypothesis | candidate | 0.682 | 0.000 | 0.682 | 0 | 2 | plausible_unproven |
| `MECH-503` | mechanism_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 4 | plausible_unproven |
| `MECH-513` | mechanism_hypothesis | candidate | 0.624 | 0.000 | 0.624 | 0 | 1 | plausible_unproven |
| `MECH-514` | mechanism_hypothesis | candidate | 0.637 | 0.000 | 0.637 | 0 | 2 | plausible_unproven |
| `MECH-520` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 4 | plausible_unproven |
| `MECH-521` | mechanism_hypothesis | candidate | 0.810 | 0.000 | 0.810 | 0 | 4 | plausible_unproven |
| `MECH-522` | mechanism_hypothesis | candidate | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `MECH-900` | - | - | 0.667 | 0.000 | 0.667 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.872 | 0.000 | 0.872 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.781 | 0.000 | 0.781 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.873 | 0.000 | 0.873 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.742 | 0.000 | 0.742 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.836 | 0.000 | 0.836 | 0 | 4 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.872 | 0.000 | 0.872 | 0 | 9 | plausible_unproven |
| `SD-025` | design_decision | candidate | 0.784 | 0.000 | 0.784 | 0 | 3 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.679 | 0.000 | 0.679 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.811 | 0.000 | 0.811 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.854 | 0.000 | 0.854 | 0 | 14 | plausible_unproven |
| `SD-032c` | - | - | 0.769 | 0.000 | 0.769 | 0 | 3 | plausible_unproven |
| `SD-032d` | - | - | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.795 | 0.000 | 0.795 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.877 | 0.000 | 0.877 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.863 | 0.000 | 0.863 | 0 | 9 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.900 | 0.000 | 0.900 | 0 | 7 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.850 | 0.000 | 0.850 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.727 | 0.000 | 0.727 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.898 | 0.000 | 0.898 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.801 | 0.000 | 0.801 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.777 | 0.000 | 0.777 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.851 | 0.000 | 0.851 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `SD-068` | design_decision | candidate | 0.793 | 0.000 | 0.793 | 0 | 4 | plausible_unproven |
| `SD-076` | design_decision | candidate | 0.635 | 0.000 | 0.635 | 0 | 8 | plausible_unproven |
| `SD-078` | design_decision | candidate_substrate_landed | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `SD-080` | design_decision | candidate | 0.798 | 0.000 | 0.798 | 0 | 3 | plausible_unproven |
| `SD-082` | design_decision | candidate_substrate_landed | 0.834 | 0.000 | 0.834 | 0 | 8 | plausible_unproven |
| `SD-091` | design_decision | candidate | 0.778 | 0.000 | 0.778 | 0 | 5 | plausible_unproven |
| `SD-092` | design_decision | candidate | 0.687 | 0.000 | 0.687 | 0 | 2 | plausible_unproven |
| `SD-099` | design_decision | candidate | 0.780 | 0.000 | 0.780 | 0 | 4 | plausible_unproven |
| `SD-101` | design_decision | candidate | 0.817 | 0.000 | 0.817 | 0 | 5 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.660 | 0.105 | 0.845 | 1 | 5 | plausible_unproven |
| `INV-054` | invariant | candidate | 0.651 | 0.125 | 0.827 | 1 | 6 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.661 | 0.125 | 0.840 | 1 | 4 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.637 | 0.125 | 0.808 | 1 | 10 | plausible_unproven |
| `MECH-057b` | - | - | 0.668 | 0.160 | 0.837 | 1 | 4 | plausible_unproven |
| `INV-088` | invariant | candidate | 0.666 | 0.221 | 0.814 | 1 | 6 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.645 | 0.244 | 0.778 | 1 | 5 | plausible_unproven |
| `MECH-475` | mechanism_hypothesis | retired | 0.668 | 0.259 | 0.804 | 1 | 5 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.702 | 0.265 | 0.847 | 1 | 9 | plausible_unproven |
| `SD-087` | design_decision | candidate | 0.680 | 0.266 | 0.818 | 1 | 4 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.714 | 0.268 | 0.862 | 1 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.671 | 0.269 | 0.805 | 1 | 3 | plausible_unproven |
| `MECH-428` | mechanism | candidate | 0.626 | 0.269 | 0.745 | 1 | 3 | plausible_unproven |
| `MECH-467` | mechanism_hypothesis | candidate | 0.655 | 0.269 | 0.783 | 1 | 3 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.697 | 0.275 | 0.838 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.700 | 0.275 | 0.842 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.698 | 0.275 | 0.839 | 1 | 4 | plausible_unproven |
| `MECH-144` | mechanism_hypothesis | candidate | 0.675 | 0.280 | 0.806 | 1 | 4 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate | 0.732 | 0.280 | 0.882 | 1 | 6 | plausible_unproven |
| `SD-009` | design_decision | candidate | 0.646 | 0.281 | 0.768 | 1 | 3 | plausible_unproven |
| `MECH-357` | mechanism_hypothesis | candidate | 0.642 | 0.282 | 0.762 | 1 | 3 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.634 | 0.320 | 0.844 | 2 | 5 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.621 | 0.372 | 0.869 | 3 | 4 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.664 | 0.390 | 0.847 | 2 | 5 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.637 | 0.394 | 0.880 | 7 | 10 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.630 | 0.419 | 0.841 | 4 | 25 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.794 | 0.421 | 0.918 | 1 | 7 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.654 | 0.428 | 0.880 | 19 | 9 | plausible_unproven |
| `MECH-321` | mechanism_hypothesis | candidate | 0.633 | 0.454 | 0.811 | 4 | 14 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.621 | 0.454 | 0.787 | 7 | 13 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.647 | 0.463 | 0.831 | 5 | 8 | plausible_unproven |
| `MECH-025b` | - | - | 0.662 | 0.474 | 0.787 | 2 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.660 | 0.489 | 0.831 | 5 | 6 | plausible_unproven |
| `INV-089` | invariant | provisional | 0.667 | 0.496 | 0.781 | 2 | 3 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | candidate | 0.655 | 0.496 | 0.814 | 11 | 24 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.680 | 0.499 | 0.861 | 3 | 14 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.687 | 0.504 | 0.870 | 26 | 4 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.644 | 0.518 | 0.770 | 3 | 5 | plausible_unproven |
| `Q-034` | question | open | 0.646 | 0.525 | 0.766 | 3 | 6 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.697 | 0.531 | 0.862 | 3 | 13 | plausible_unproven |
| `SD-048` | design_decision | candidate | 0.732 | 0.547 | 0.855 | 2 | 6 | plausible_unproven |
| `MECH-150` | mechanism_hypothesis | candidate | 0.690 | 0.554 | 0.780 | 2 | 3 | plausible_unproven |
| `MECH-231` | mechanism_hypothesis | provisional | 0.710 | 0.555 | 0.761 | 1 | 3 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.777 | 0.555 | 0.851 | 1 | 8 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.689 | 0.563 | 0.816 | 25 | 8 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.703 | 0.569 | 0.836 | 12 | 9 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.697 | 0.572 | 0.821 | 3 | 7 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.772 | 0.575 | 0.838 | 1 | 13 | plausible_unproven |
| `MECH-057a` | - | - | 0.761 | 0.575 | 0.823 | 1 | 4 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.732 | 0.575 | 0.785 | 1 | 7 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.751 | 0.575 | 0.810 | 1 | 12 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.760 | 0.575 | 0.822 | 1 | 8 | plausible_unproven |
| `MECH-062` | mechanism_hypothesis | candidate | 0.690 | 0.575 | 0.747 | 1 | 2 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.782 | 0.575 | 0.851 | 1 | 4 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.766 | 0.575 | 0.830 | 1 | 7 | plausible_unproven |
| `MECH-259` | mechanism_hypothesis | stable | 0.666 | 0.575 | 0.712 | 1 | 2 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.729 | 0.575 | 0.780 | 1 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.786 | 0.575 | 0.857 | 1 | 20 | plausible_unproven |
| `SD-035` | design_decision | stable | 0.783 | 0.575 | 0.852 | 1 | 6 | plausible_unproven |
| `MECH-135` | mechanism_hypothesis | candidate | 0.701 | 0.582 | 0.821 | 7 | 11 | plausible_unproven |
| `MECH-230` | mechanism_hypothesis | provisional | 0.752 | 0.582 | 0.808 | 1 | 11 | plausible_unproven |
| `MECH-256` | mechanism_hypothesis | candidate | 0.711 | 0.583 | 0.839 | 5 | 9 | plausible_unproven |
| `MECH-306` | mechanism_hypothesis | provisional | 0.798 | 0.583 | 0.870 | 1 | 4 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.762 | 0.586 | 0.821 | 1 | 8 | plausible_unproven |
| `MECH-071` | mechanism_hypothesis | provisional | 0.717 | 0.588 | 0.847 | 38 | 4 | plausible_unproven |
| `SD-007` | design_decision | implemented | 0.720 | 0.593 | 0.846 | 19 | 5 | plausible_unproven |
| `MECH-314` | mechanism_hypothesis | candidate_substrate_landed | 0.800 | 0.594 | 0.869 | 1 | 10 | plausible_unproven |
| `MECH-314a` | - | - | 0.787 | 0.594 | 0.851 | 1 | 6 | plausible_unproven |
| `MECH-346` | mechanism_hypothesis | candidate | 0.745 | 0.595 | 0.795 | 1 | 3 | plausible_unproven |
| `MECH-347` | mechanism_hypothesis | candidate | 0.749 | 0.595 | 0.800 | 1 | 3 | plausible_unproven |
| `SD-057` | design_decision | candidate | 0.692 | 0.595 | 0.740 | 1 | 2 | plausible_unproven |
| `MECH-045` | mechanism_hypothesis | provisional | 0.780 | 0.598 | 0.841 | 1 | 14 | plausible_unproven |
| `MECH-087` | mechanism_hypothesis | candidate | 0.654 | 0.605 | 0.704 | 1 | 1 | plausible_unproven |
| `MECH-309` | mechanism_hypothesis | candidate | 0.757 | 0.605 | 0.859 | 2 | 14 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.709 | 0.607 | 0.811 | 84 | 7 | plausible_unproven |
| `SD-013` | design_decision | provisional | 0.722 | 0.608 | 0.836 | 4 | 4 | plausible_unproven |
| `MECH-106` | mechanism_hypothesis | provisional | 0.747 | 0.613 | 0.836 | 2 | 5 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.706 | 0.615 | 0.767 | 2 | 3 | plausible_unproven |
| `MECH-261` | mechanism_hypothesis | stable | 0.762 | 0.615 | 0.860 | 2 | 20 | plausible_unproven |
| `MECH-358` | mechanism_hypothesis | candidate | 0.738 | 0.615 | 0.779 | 1 | 3 | plausible_unproven |
| `SD-059` | design_decision | candidate | 0.783 | 0.615 | 0.839 | 1 | 4 | plausible_unproven |

_Suppressed by gating: 61 substrate_coherence (ARC + universal invariant), 67 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.873 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.840 | 3 |
| `INV-013` | invariant | active | 0.808 | 3 |
| `ARC-014` | architectural_commitment | active | 0.759 | 3 |
| `ARC-011` | architectural_commitment | active | 0.750 | 1 |
| `ARC-001` | architectural_commitment | active | 0.660 | 1 |
| `INV-014` | invariant | active | 0.660 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-079` | open_question | resolved | 0.830 | 5 |
| `Q-017` | open_question | active | 0.828 | 7 |
| `Q-016` | open_question | active | 0.825 | 5 |
| `Q-015` | open_question | active | 0.806 | 5 |
| `Q-005` | open_question | active | 0.776 | 4 |
| `Q-087` | open_question | resolved | 0.744 | 4 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-492` | candidate | 0.771 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **72**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-155` | candidate | 0.105 | 1 |
| `INV-054` | candidate | 0.125 | 1 |
| `MECH-063` | provisional | 0.125 | 1 |
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-142` | candidate | 0.125 | 1 |
| `MECH-188` | candidate | 0.125 | 1 |
| `SD-018` | implemented | 0.125 | 1 |
| `SD-023` | candidate | 0.125 | 1 |
| `SD-047` | provisional | 0.125 | 1 |
| `MECH-057b` | - | 0.160 | 1 |
| `MECH-070` | retiring | 0.163 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `MECH-295` | candidate | 0.178 | 2 |
| `MECH-445` | candidate | 0.210 | 1 |
| `MECH-111` | candidate | 0.217 | 3 |
| `MECH-128` | candidate | 0.217 | 3 |
| `INV-088` | candidate | 0.221 | 1 |
| `MECH-329` | candidate | 0.244 | 1 |
| `MECH-466` | candidate | 0.255 | 1 |
| `MECH-475` | retired | 0.259 | 1 |
| `MECH-294` | candidate | 0.265 | 1 |
| `SD-087` | candidate | 0.266 | 1 |
| `MECH-267` | provisional | 0.268 | 1 |
| `MECH-480` | candidate | 0.268 | 1 |
| `MECH-122` | provisional | 0.269 | 1 |
| `MECH-428` | candidate | 0.269 | 1 |
| `MECH-467` | candidate | 0.269 | 1 |
| `MECH-026` | provisional | 0.275 | 1 |
| `MECH-029` | provisional | 0.275 | 1 |
| `MECH-047` | provisional | 0.275 | 1 |
| ... | ... | ... | ... (42 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **216**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `INV-050` | candidate | 0.925 | 8 |
| `MECH-121` | candidate | 0.902 | 5 |
| `SD-037` | candidate | 0.900 | 7 |
| `SD-045` | candidate | 0.898 | 4 |
| `MECH-053` | provisional | 0.880 | 6 |
| `MECH-263` | candidate | 0.880 | 4 |
| `MECH-307` | candidate_substrate_landed | 0.878 | 6 |
| `SD-033b` | - | 0.877 | 5 |
| `MECH-271` | candidate | 0.876 | 4 |
| `MECH-440` | candidate | 0.875 | 5 |
| `Q-035` | resolved | 0.873 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.872 | 7 |
| `SD-021` | candidate | 0.872 | 9 |
| `MECH-320` | candidate_substrate_landed | 0.871 | 5 |
| `MECH-203` | candidate | 0.870 | 8 |
| `MECH-317` | candidate | 0.868 | 6 |
| `MECH-314c` | - | 0.866 | 6 |
| `DEV-NEED-009` | - | 0.864 | 4 |
| `SD-033e` | - | 0.863 | 9 |
| `MECH-141` | candidate | 0.862 | 4 |
| `MECH-030` | provisional | 0.861 | 4 |
| `MECH-172` | candidate | 0.861 | 6 |
| `MECH-191` | candidate | 0.859 | 4 |
| `MECH-265` | candidate | 0.858 | 6 |
| `ARC-049` | candidate | 0.857 | 26 |
| `DEV-NEED-012` | - | 0.857 | 6 |
| `MECH-264` | candidate | 0.854 | 5 |
| `MECH-316` | candidate | 0.854 | 9 |
| `SD-032b` | - | 0.854 | 14 |
| `ARC-060` | candidate | 0.851 | 13 |
| `MECH-472` | candidate | 0.851 | 4 |
| `SD-054` | candidate | 0.851 | 7 |
| `MECH-337` | candidate | 0.850 | 4 |
| `SD-039` | candidate | 0.850 | 6 |
| `MECH-171` | candidate | 0.849 | 4 |
| `MECH-198` | candidate | 0.849 | 8 |
| `ARC-078` | candidate | 0.848 | 11 |
| `MECH-334` | candidate | 0.847 | 3 |
| `MECH-197` | candidate | 0.846 | 12 |
| `MECH-168` | candidate | 0.844 | 4 |
| `MECH-269` | candidate | 0.844 | 34 |
| `MECH-280` | candidate | 0.844 | 5 |
| `MECH-281` | candidate | 0.844 | 4 |
| `MECH-434` | candidate | 0.844 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.841 | 5 |
| `MECH-503` | candidate | 0.841 | 4 |
| `ARC-051` | candidate | 0.840 | 4 |
| `MECH-220` | candidate | 0.839 | 4 |
| `INV-048` | candidate | 0.837 | 4 |
| `INV-064` | candidate | 0.836 | 5 |
| ... | ... | ... | ... (166 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
