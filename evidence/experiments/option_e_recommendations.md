# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-08-08T20:44:05.675839Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 389 |
| `substrate_coherence` | 68 |
| `answer_state` | 80 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **100** | plausible_unproven: **421** |
| **low lit**             | novel_discovery: **0**         | speculative: **16** |

Total scored claims: 537

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **260** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.835 | 0.000 | 0.835 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.837 | 0.000 | 0.837 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.847 | 0.000 | 0.847 | 0 | 5 | plausible_unproven |
| `CDQ-007` | - | - | 0.786 | 0.000 | 0.786 | 0 | 8 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.707 | 0.000 | 0.707 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.862 | 0.000 | 0.862 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.707 | 0.000 | 0.707 | 0 | 1 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.834 | 0.000 | 0.834 | 0 | 4 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.821 | 0.000 | 0.821 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.627 | 0.000 | 0.627 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.686 | 0.000 | 0.686 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.620 | 0.000 | 0.620 | 0 | 4 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.842 | 0.000 | 0.842 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.824 | 0.000 | 0.824 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.708 | 0.000 | 0.708 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.835 | 0.000 | 0.835 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.624 | 0.000 | 0.624 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.841 | 0.000 | 0.841 | 0 | 5 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.783 | 0.000 | 0.783 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.735 | 0.000 | 0.735 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.808 | 0.000 | 0.808 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.717 | 0.000 | 0.717 | 0 | 2 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.842 | 0.000 | 0.842 | 0 | 7 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.832 | 0.000 | 0.832 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.828 | 0.000 | 0.828 | 0 | 9 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 3 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 3 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.907 | 0.000 | 0.907 | 0 | 5 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.834 | 0.000 | 0.834 | 0 | 8 | plausible_unproven |
| `MECH-130` | mechanism_hypothesis | candidate | 0.686 | 0.000 | 0.686 | 0 | 5 | plausible_unproven |
| `MECH-140` | mechanism_hypothesis | candidate | 0.685 | 0.000 | 0.685 | 0 | 2 | plausible_unproven |
| `MECH-141` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.705 | 0.000 | 0.705 | 0 | 1 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.690 | 0.000 | 0.690 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.866 | 0.000 | 0.866 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.721 | 0.000 | 0.721 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.743 | 0.000 | 0.743 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 3 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.691 | 0.000 | 0.691 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.716 | 0.000 | 0.716 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.702 | 0.000 | 0.702 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 4 | plausible_unproven |
| `MECH-186` | mechanism_hypothesis | candidate | 0.742 | 0.000 | 0.742 | 0 | 3 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.702 | 0.000 | 0.702 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.712 | 0.000 | 0.712 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 8 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.735 | 0.000 | 0.735 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.695 | 0.000 | 0.695 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.813 | 0.000 | 0.813 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.694 | 0.000 | 0.694 | 0 | 1 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.685 | 0.000 | 0.685 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 7 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.825 | 0.000 | 0.825 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.816 | 0.000 | 0.816 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.651 | 0.000 | 0.651 | 0 | 1 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.876 | 0.000 | 0.876 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.675 | 0.000 | 0.675 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.690 | 0.000 | 0.690 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.695 | 0.000 | 0.695 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.655 | 0.000 | 0.655 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.694 | 0.000 | 0.694 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.725 | 0.000 | 0.725 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.725 | 0.000 | 0.725 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.695 | 0.000 | 0.695 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.685 | 0.000 | 0.685 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.685 | 0.000 | 0.685 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.720 | 0.000 | 0.720 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.685 | 0.000 | 0.685 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 7 | plausible_unproven |
| `MECH-440` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 5 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.808 | 0.000 | 0.808 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 3 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 5 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 4 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 5 | plausible_unproven |
| `MECH-459` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 3 | plausible_unproven |
| `MECH-471` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 3 | plausible_unproven |
| `MECH-472` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 4 | plausible_unproven |
| `MECH-481` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 4 | plausible_unproven |
| `MECH-487` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 5 | plausible_unproven |
| `MECH-900` | - | - | 0.672 | 0.000 | 0.672 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.878 | 0.000 | 0.878 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.786 | 0.000 | 0.786 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.878 | 0.000 | 0.878 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.842 | 0.000 | 0.842 | 0 | 4 | plausible_unproven |
| `SD-025` | design_decision | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.685 | 0.000 | 0.685 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.816 | 0.000 | 0.816 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.869 | 0.000 | 0.869 | 0 | 16 | plausible_unproven |
| `SD-032d` | - | - | 0.839 | 0.000 | 0.839 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.801 | 0.000 | 0.801 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.882 | 0.000 | 0.882 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.873 | 0.000 | 0.873 | 0 | 12 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.842 | 0.000 | 0.842 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.855 | 0.000 | 0.855 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.732 | 0.000 | 0.732 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.903 | 0.000 | 0.903 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.806 | 0.000 | 0.806 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.783 | 0.000 | 0.783 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.857 | 0.000 | 0.857 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `SD-068` | design_decision | candidate | 0.798 | 0.000 | 0.798 | 0 | 4 | plausible_unproven |
| `SD-076` | design_decision | candidate | 0.640 | 0.000 | 0.640 | 0 | 8 | plausible_unproven |
| `SD-078` | design_decision | candidate_substrate_landed | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `SD-080` | design_decision | candidate | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `SD-082` | design_decision | candidate_substrate_landed | 0.839 | 0.000 | 0.839 | 0 | 8 | plausible_unproven |
| `SD-091` | design_decision | candidate | 0.783 | 0.000 | 0.783 | 0 | 5 | plausible_unproven |
| `SD-092` | design_decision | candidate | 0.692 | 0.000 | 0.692 | 0 | 2 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.664 | 0.105 | 0.850 | 1 | 5 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.651 | 0.125 | 0.827 | 1 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.620 | 0.125 | 0.785 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.633 | 0.125 | 0.802 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.664 | 0.125 | 0.844 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.665 | 0.125 | 0.845 | 1 | 4 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.642 | 0.125 | 0.814 | 1 | 10 | plausible_unproven |
| `MECH-057b` | - | - | 0.682 | 0.203 | 0.842 | 1 | 4 | plausible_unproven |
| `INV-088` | invariant | candidate | 0.680 | 0.264 | 0.819 | 1 | 6 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.701 | 0.275 | 0.843 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.704 | 0.275 | 0.847 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.702 | 0.275 | 0.844 | 1 | 4 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.707 | 0.280 | 0.849 | 1 | 5 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.660 | 0.287 | 0.784 | 1 | 5 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.738 | 0.302 | 0.883 | 1 | 6 | plausible_unproven |
| `MECH-475` | mechanism_hypothesis | retired | 0.682 | 0.302 | 0.809 | 1 | 5 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.716 | 0.309 | 0.852 | 1 | 9 | plausible_unproven |
| `SD-087` | design_decision | candidate | 0.695 | 0.309 | 0.823 | 1 | 4 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.730 | 0.312 | 0.870 | 1 | 4 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.729 | 0.312 | 0.868 | 1 | 5 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate | 0.743 | 0.312 | 0.887 | 1 | 6 | plausible_unproven |
| `MECH-428` | mechanism | candidate | 0.640 | 0.312 | 0.750 | 1 | 3 | plausible_unproven |
| `MECH-457` | mechanism_hypothesis | candidate | 0.633 | 0.337 | 0.830 | 2 | 22 | plausible_unproven |
| `MECH-314b` | - | - | 0.710 | 0.342 | 0.833 | 1 | 3 | plausible_unproven |
| `MECH-314c` | - | - | 0.739 | 0.342 | 0.871 | 1 | 6 | plausible_unproven |
| `MECH-321` | mechanism_hypothesis | candidate | 0.634 | 0.362 | 0.816 | 2 | 14 | plausible_unproven |
| `MECH-074d` | - | - | 0.635 | 0.374 | 0.809 | 2 | 4 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.667 | 0.390 | 0.852 | 2 | 5 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.640 | 0.394 | 0.885 | 7 | 10 | plausible_unproven |
| `MECH-476` | mechanism_hypothesis | retired | 0.626 | 0.409 | 0.843 | 3 | 5 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.645 | 0.415 | 0.875 | 3 | 4 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.656 | 0.428 | 0.885 | 19 | 9 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.620 | 0.447 | 0.792 | 9 | 13 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.770 | 0.464 | 0.872 | 1 | 4 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.676 | 0.465 | 0.887 | 3 | 11 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.662 | 0.486 | 0.837 | 5 | 8 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.667 | 0.497 | 0.838 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.646 | 0.504 | 0.787 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.638 | 0.505 | 0.771 | 5 | 6 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.726 | 0.517 | 0.865 | 2 | 7 | plausible_unproven |
| `MECH-025b` | - | - | 0.682 | 0.517 | 0.792 | 2 | 4 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.647 | 0.518 | 0.775 | 3 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | candidate | 0.679 | 0.539 | 0.819 | 11 | 24 | plausible_unproven |
| `INV-089` | invariant | provisional | 0.688 | 0.540 | 0.786 | 2 | 3 | plausible_unproven |
| `MECH-256` | mechanism_hypothesis | candidate | 0.692 | 0.540 | 0.844 | 6 | 9 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.704 | 0.542 | 0.866 | 3 | 14 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.696 | 0.545 | 0.846 | 5 | 25 | plausible_unproven |
| `MECH-231` | mechanism_hypothesis | provisional | 0.713 | 0.555 | 0.766 | 1 | 3 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.781 | 0.555 | 0.856 | 1 | 8 | plausible_unproven |
| `SD-048` | design_decision | candidate | 0.784 | 0.555 | 0.860 | 1 | 6 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.711 | 0.569 | 0.852 | 12 | 10 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.721 | 0.574 | 0.867 | 3 | 13 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.775 | 0.575 | 0.842 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.763 | 0.575 | 0.826 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.738 | 0.575 | 0.792 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.757 | 0.575 | 0.818 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.764 | 0.575 | 0.827 | 1 | 8 | plausible_unproven |
| `MECH-062` | mechanism_hypothesis | candidate | 0.693 | 0.575 | 0.752 | 1 | 2 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.786 | 0.575 | 0.857 | 1 | 4 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.770 | 0.575 | 0.835 | 1 | 7 | plausible_unproven |
| `MECH-259` | mechanism_hypothesis | stable | 0.670 | 0.575 | 0.717 | 1 | 2 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.732 | 0.575 | 0.785 | 1 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.790 | 0.575 | 0.862 | 1 | 20 | plausible_unproven |
| `SD-035` | design_decision | stable | 0.786 | 0.575 | 0.857 | 1 | 6 | plausible_unproven |
| `MECH-135` | mechanism_hypothesis | candidate | 0.705 | 0.582 | 0.827 | 7 | 11 | plausible_unproven |
| `MECH-071` | mechanism_hypothesis | provisional | 0.720 | 0.588 | 0.852 | 38 | 4 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.709 | 0.592 | 0.826 | 4 | 7 | plausible_unproven |
| `SD-007` | design_decision | implemented | 0.722 | 0.593 | 0.851 | 19 | 5 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.715 | 0.606 | 0.823 | 25 | 9 | plausible_unproven |
| `SD-013` | design_decision | provisional | 0.725 | 0.608 | 0.842 | 4 | 4 | plausible_unproven |
| `MECH-106` | mechanism_hypothesis | provisional | 0.750 | 0.613 | 0.842 | 2 | 5 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.709 | 0.615 | 0.772 | 2 | 3 | plausible_unproven |
| `MECH-261` | mechanism_hypothesis | stable | 0.765 | 0.615 | 0.865 | 2 | 20 | plausible_unproven |

_Suppressed by gating: 53 substrate_coherence (ARC + universal invariant), 62 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.878 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.846 | 3 |
| `ARC-014` | architectural_commitment | active | 0.764 | 3 |
| `ARC-011` | architectural_commitment | active | 0.756 | 1 |
| `ARC-001` | architectural_commitment | active | 0.665 | 1 |
| `INV-014` | invariant | active | 0.665 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.840 | 11 |
| `Q-079` | open_question | resolved | 0.835 | 5 |
| `Q-016` | open_question | active | 0.831 | 5 |
| `Q-015` | open_question | active | 0.812 | 5 |
| `Q-005` | open_question | active | 0.781 | 4 |
| `Q-087` | open_question | resolved | 0.750 | 4 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **0**.

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **80**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-155` | candidate | 0.105 | 1 |
| `MECH-063` | provisional | 0.125 | 1 |
| `MECH-091` | candidate | 0.125 | 1 |
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-142` | candidate | 0.125 | 1 |
| `MECH-150` | candidate | 0.125 | 1 |
| `MECH-165` | candidate | 0.125 | 1 |
| `MECH-188` | candidate | 0.125 | 1 |
| `MECH-220` | candidate | 0.125 | 1 |
| `SD-018` | implemented | 0.125 | 1 |
| `SD-023` | candidate | 0.125 | 1 |
| `SD-032c` | - | 0.125 | 1 |
| `SD-047` | provisional | 0.125 | 1 |
| `MECH-070` | retiring | 0.163 | 2 |
| `ARC-032` | candidate | 0.175 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `MECH-057b` | - | 0.203 | 1 |
| `MECH-128` | candidate | 0.217 | 3 |
| `MECH-295` | candidate | 0.221 | 2 |
| `INV-054` | candidate | 0.225 | 3 |
| `SD-021` | candidate | 0.225 | 3 |
| `MECH-445` | candidate | 0.253 | 1 |
| `MECH-075` | candidate | 0.263 | 4 |
| `INV-088` | candidate | 0.264 | 1 |
| `MECH-111` | candidate | 0.269 | 4 |
| `MECH-026` | provisional | 0.275 | 1 |
| `MECH-029` | provisional | 0.275 | 1 |
| `MECH-047` | provisional | 0.275 | 1 |
| `MECH-022` | provisional | 0.280 | 1 |
| `MECH-097` | candidate | 0.280 | 1 |
| ... | ... | ... | ... (50 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **194**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.907 | 5 |
| `SD-045` | candidate | 0.903 | 4 |
| `MECH-263` | candidate | 0.886 | 4 |
| `SD-033b` | - | 0.882 | 5 |
| `MECH-271` | candidate | 0.881 | 4 |
| `MECH-440` | candidate | 0.880 | 5 |
| `MECH-CBBL-PROPOSED` | - | 0.878 | 7 |
| `Q-035` | resolved | 0.878 | 15 |
| `MECH-203` | candidate | 0.876 | 8 |
| `MECH-264` | candidate | 0.876 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.876 | 5 |
| `MECH-317` | candidate | 0.874 | 9 |
| `MECH-265` | candidate | 0.873 | 8 |
| `SD-033e` | - | 0.873 | 12 |
| `DEV-NEED-009` | - | 0.869 | 4 |
| `SD-032b` | - | 0.869 | 16 |
| `MECH-141` | candidate | 0.868 | 4 |
| `MECH-030` | provisional | 0.867 | 4 |
| `MECH-172` | candidate | 0.866 | 6 |
| `MECH-191` | candidate | 0.865 | 4 |
| `ARC-049` | candidate | 0.864 | 27 |
| `DEV-NEED-012` | - | 0.862 | 6 |
| `MECH-316` | candidate | 0.859 | 9 |
| `SD-054` | candidate | 0.857 | 7 |
| `ARC-060` | candidate | 0.856 | 13 |
| `MECH-472` | candidate | 0.856 | 4 |
| `MECH-171` | candidate | 0.855 | 4 |
| `MECH-337` | candidate | 0.855 | 4 |
| `SD-039` | candidate | 0.855 | 6 |
| `ARC-078` | candidate | 0.854 | 11 |
| `MECH-198` | candidate | 0.854 | 8 |
| `MECH-334` | candidate | 0.853 | 3 |
| `MECH-197` | candidate | 0.851 | 12 |
| `MECH-168` | candidate | 0.850 | 4 |
| `MECH-280` | candidate | 0.850 | 5 |
| `MECH-434` | candidate | 0.850 | 4 |
| `MECH-269` | candidate | 0.849 | 34 |
| `MECH-281` | candidate | 0.849 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.847 | 5 |
| `ARC-051` | candidate | 0.846 | 4 |
| `INV-048` | candidate | 0.842 | 4 |
| `MECH-044` | provisional | 0.842 | 7 |
| `SD-003-SUCCESSOR` | - | 0.842 | 4 |
| `SD-037` | candidate | 0.842 | 4 |
| `INV-064` | candidate | 0.841 | 5 |
| `MECH-312` | candidate | 0.841 | 14 |
| `MECH-394` | candidate | 0.840 | 4 |
| `MECH-275` | candidate | 0.839 | 6 |
| `SD-032d` | - | 0.839 | 4 |
| `SD-082` | candidate_substrate_landed | 0.839 | 8 |
| ... | ... | ... | ... (144 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
