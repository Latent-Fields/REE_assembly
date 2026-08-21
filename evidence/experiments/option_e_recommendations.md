# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-08-21T02:07:11.088199Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 397 |
| `substrate_coherence` | 69 |
| `answer_state` | 82 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **90** | plausible_unproven: **450** |
| **low lit**             | novel_discovery: **0**         | speculative: **8** |

Total scored claims: 548

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **278** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 26 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.832 | 0.000 | 0.832 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.833 | 0.000 | 0.833 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.843 | 0.000 | 0.843 | 0 | 5 | plausible_unproven |
| `CDQ-007` | - | - | 0.783 | 0.000 | 0.783 | 0 | 8 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.858 | 0.000 | 0.858 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.787 | 0.000 | 0.787 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.804 | 0.000 | 0.804 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `GOV-BEHADJ-1` | governance_rule | candidate | 0.828 | 0.000 | 0.828 | 0 | 9 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.831 | 0.000 | 0.831 | 0 | 4 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.818 | 0.000 | 0.818 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.624 | 0.000 | 0.624 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.682 | 0.000 | 0.682 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.839 | 0.000 | 0.839 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.927 | 0.000 | 0.927 | 0 | 8 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.705 | 0.000 | 0.705 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.832 | 0.000 | 0.832 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.620 | 0.000 | 0.620 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.838 | 0.000 | 0.838 | 0 | 5 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.779 | 0.000 | 0.779 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.731 | 0.000 | 0.731 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.805 | 0.000 | 0.805 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.714 | 0.000 | 0.714 | 0 | 2 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.863 | 0.000 | 0.863 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.833 | 0.000 | 0.833 | 0 | 6 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.792 | 0.000 | 0.792 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.792 | 0.000 | 0.792 | 0 | 5 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.814 | 0.000 | 0.814 | 0 | 4 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 3 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 6 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.904 | 0.000 | 0.904 | 0 | 5 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 8 | plausible_unproven |
| `MECH-130` | mechanism_hypothesis | candidate | 0.683 | 0.000 | 0.683 | 0 | 5 | plausible_unproven |
| `MECH-140` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 2 | plausible_unproven |
| `MECH-141` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.701 | 0.000 | 0.701 | 0 | 1 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 3 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.851 | 0.000 | 0.851 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.863 | 0.000 | 0.863 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 3 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.712 | 0.000 | 0.712 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.699 | 0.000 | 0.699 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 4 | plausible_unproven |
| `MECH-186` | mechanism_hypothesis | candidate | 0.743 | 0.000 | 0.743 | 0 | 3 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.782 | 0.000 | 0.782 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.731 | 0.000 | 0.731 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.699 | 0.000 | 0.699 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 8 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.731 | 0.000 | 0.731 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.691 | 0.000 | 0.691 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.809 | 0.000 | 0.809 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 4 | plausible_unproven |
| `MECH-236` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 4 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.743 | 0.000 | 0.743 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 5 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.860 | 0.000 | 0.860 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.822 | 0.000 | 0.822 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.812 | 0.000 | 0.812 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.835 | 0.000 | 0.835 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 3 | plausible_unproven |
| `MECH-289` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 4 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.648 | 0.000 | 0.648 | 0 | 1 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.880 | 0.000 | 0.880 | 0 | 6 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.838 | 0.000 | 0.838 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 6 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 6 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.873 | 0.000 | 0.873 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.671 | 0.000 | 0.671 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.686 | 0.000 | 0.686 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.817 | 0.000 | 0.817 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.691 | 0.000 | 0.691 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.651 | 0.000 | 0.651 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.808 | 0.000 | 0.808 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.721 | 0.000 | 0.721 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.721 | 0.000 | 0.721 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.701 | 0.000 | 0.701 | 0 | 1 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.716 | 0.000 | 0.716 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `MECH-440` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 5 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.760 | 0.000 | 0.760 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 3 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 4 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 5 | plausible_unproven |
| `MECH-459` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `MECH-471` | mechanism_hypothesis | candidate | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `MECH-472` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `MECH-481` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 4 | plausible_unproven |
| `MECH-487` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 5 | plausible_unproven |
| `MECH-489` | mechanism_hypothesis | candidate | 0.829 | 0.000 | 0.829 | 0 | 5 | plausible_unproven |
| `MECH-490` | mechanism_hypothesis | candidate | 0.787 | 0.000 | 0.787 | 0 | 4 | plausible_unproven |
| `MECH-900` | - | - | 0.669 | 0.000 | 0.669 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.874 | 0.000 | 0.874 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.783 | 0.000 | 0.783 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.875 | 0.000 | 0.875 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.838 | 0.000 | 0.838 | 0 | 4 | plausible_unproven |
| `SD-025` | design_decision | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.681 | 0.000 | 0.681 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.813 | 0.000 | 0.813 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.856 | 0.000 | 0.856 | 0 | 14 | plausible_unproven |
| `SD-032c` | - | - | 0.771 | 0.000 | 0.771 | 0 | 3 | plausible_unproven |
| `SD-032d` | - | - | 0.835 | 0.000 | 0.835 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.797 | 0.000 | 0.797 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.879 | 0.000 | 0.879 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.865 | 0.000 | 0.865 | 0 | 9 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.902 | 0.000 | 0.902 | 0 | 7 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.852 | 0.000 | 0.852 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.729 | 0.000 | 0.729 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.900 | 0.000 | 0.900 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.803 | 0.000 | 0.803 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.779 | 0.000 | 0.779 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.853 | 0.000 | 0.853 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.736 | 0.000 | 0.736 | 0 | 2 | plausible_unproven |
| `SD-068` | design_decision | candidate | 0.794 | 0.000 | 0.794 | 0 | 4 | plausible_unproven |
| `SD-076` | design_decision | candidate | 0.637 | 0.000 | 0.637 | 0 | 8 | plausible_unproven |
| `SD-078` | design_decision | candidate_substrate_landed | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `SD-080` | design_decision | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `SD-082` | design_decision | candidate_substrate_landed | 0.836 | 0.000 | 0.836 | 0 | 8 | plausible_unproven |
| `SD-091` | design_decision | candidate | 0.780 | 0.000 | 0.780 | 0 | 5 | plausible_unproven |
| `SD-092` | design_decision | candidate | 0.689 | 0.000 | 0.689 | 0 | 2 | plausible_unproven |
| `SD-099` | design_decision | candidate | 0.782 | 0.000 | 0.782 | 0 | 4 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.661 | 0.105 | 0.847 | 1 | 5 | plausible_unproven |
| `INV-054` | invariant | candidate | 0.653 | 0.125 | 0.829 | 1 | 6 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.687 | 0.125 | 0.874 | 1 | 9 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.663 | 0.125 | 0.842 | 1 | 4 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.639 | 0.125 | 0.810 | 1 | 10 | plausible_unproven |
| `MECH-057b` | - | - | 0.673 | 0.176 | 0.839 | 1 | 4 | plausible_unproven |
| `INV-088` | invariant | candidate | 0.671 | 0.237 | 0.816 | 1 | 6 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.650 | 0.260 | 0.780 | 1 | 5 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.699 | 0.275 | 0.840 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.702 | 0.275 | 0.844 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.699 | 0.275 | 0.841 | 1 | 4 | plausible_unproven |
| `MECH-475` | mechanism_hypothesis | retired | 0.673 | 0.275 | 0.806 | 1 | 5 | plausible_unproven |
| `MECH-144` | mechanism_hypothesis | candidate | 0.676 | 0.280 | 0.808 | 1 | 4 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.707 | 0.281 | 0.849 | 1 | 9 | plausible_unproven |
| `SD-087` | design_decision | candidate | 0.685 | 0.282 | 0.820 | 1 | 4 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.719 | 0.284 | 0.864 | 1 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.677 | 0.285 | 0.807 | 1 | 3 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate | 0.734 | 0.285 | 0.884 | 1 | 6 | plausible_unproven |
| `MECH-428` | mechanism | candidate | 0.632 | 0.285 | 0.747 | 1 | 3 | plausible_unproven |
| `MECH-467` | mechanism_hypothesis | candidate | 0.660 | 0.285 | 0.785 | 1 | 3 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.678 | 0.297 | 0.805 | 1 | 7 | plausible_unproven |
| `SD-009` | design_decision | candidate | 0.652 | 0.297 | 0.770 | 1 | 3 | plausible_unproven |
| `MECH-357` | mechanism_hypothesis | candidate | 0.647 | 0.298 | 0.764 | 1 | 3 | plausible_unproven |
| `MECH-457` | mechanism_hypothesis | candidate | 0.620 | 0.310 | 0.826 | 2 | 21 | plausible_unproven |
| `MECH-314b` | - | - | 0.701 | 0.315 | 0.830 | 1 | 3 | plausible_unproven |
| `MECH-314c` | - | - | 0.730 | 0.315 | 0.868 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.642 | 0.336 | 0.846 | 2 | 5 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.630 | 0.388 | 0.871 | 3 | 4 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.665 | 0.390 | 0.849 | 2 | 5 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.638 | 0.394 | 0.882 | 7 | 10 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.631 | 0.419 | 0.843 | 4 | 25 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.655 | 0.428 | 0.882 | 19 | 9 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.799 | 0.437 | 0.920 | 1 | 7 | plausible_unproven |
| `MECH-074d` | - | - | 0.626 | 0.446 | 0.805 | 4 | 4 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.622 | 0.454 | 0.789 | 7 | 13 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.648 | 0.463 | 0.833 | 5 | 8 | plausible_unproven |
| `MECH-321` | mechanism_hypothesis | candidate | 0.642 | 0.470 | 0.813 | 4 | 14 | plausible_unproven |
| `MECH-025b` | - | - | 0.669 | 0.490 | 0.789 | 2 | 4 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.688 | 0.504 | 0.872 | 26 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.669 | 0.505 | 0.833 | 5 | 6 | plausible_unproven |
| `INV-089` | invariant | provisional | 0.675 | 0.512 | 0.783 | 2 | 3 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | candidate | 0.664 | 0.512 | 0.816 | 11 | 24 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.689 | 0.515 | 0.863 | 3 | 14 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.645 | 0.518 | 0.772 | 3 | 5 | plausible_unproven |
| `Q-034` | question | open | 0.647 | 0.525 | 0.768 | 3 | 6 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.706 | 0.547 | 0.864 | 3 | 13 | plausible_unproven |
| `MECH-231` | mechanism_hypothesis | provisional | 0.711 | 0.555 | 0.763 | 1 | 3 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.779 | 0.555 | 0.853 | 1 | 8 | plausible_unproven |
| `SD-048` | design_decision | candidate | 0.739 | 0.563 | 0.857 | 2 | 6 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.704 | 0.569 | 0.838 | 12 | 9 | plausible_unproven |
| `MECH-150` | mechanism_hypothesis | candidate | 0.697 | 0.570 | 0.782 | 2 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.774 | 0.575 | 0.840 | 1 | 13 | plausible_unproven |
| `MECH-057a` | - | - | 0.762 | 0.575 | 0.825 | 1 | 4 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.734 | 0.575 | 0.787 | 1 | 7 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.753 | 0.575 | 0.812 | 1 | 12 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.762 | 0.575 | 0.824 | 1 | 8 | plausible_unproven |
| `MECH-062` | mechanism_hypothesis | candidate | 0.691 | 0.575 | 0.749 | 1 | 2 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.784 | 0.575 | 0.853 | 1 | 4 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.768 | 0.575 | 0.832 | 1 | 7 | plausible_unproven |
| `MECH-259` | mechanism_hypothesis | stable | 0.668 | 0.575 | 0.714 | 1 | 2 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.730 | 0.575 | 0.782 | 1 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.788 | 0.575 | 0.859 | 1 | 20 | plausible_unproven |
| `SD-035` | design_decision | stable | 0.784 | 0.575 | 0.854 | 1 | 6 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.699 | 0.579 | 0.818 | 25 | 8 | plausible_unproven |
| `MECH-135` | mechanism_hypothesis | candidate | 0.703 | 0.582 | 0.823 | 7 | 11 | plausible_unproven |
| `MECH-256` | mechanism_hypothesis | candidate | 0.712 | 0.583 | 0.841 | 5 | 9 | plausible_unproven |
| `MECH-071` | mechanism_hypothesis | provisional | 0.719 | 0.588 | 0.849 | 38 | 4 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.705 | 0.588 | 0.823 | 3 | 7 | plausible_unproven |
| `SD-007` | design_decision | implemented | 0.721 | 0.593 | 0.848 | 19 | 5 | plausible_unproven |
| `MECH-230` | mechanism_hypothesis | provisional | 0.757 | 0.598 | 0.810 | 1 | 11 | plausible_unproven |
| `MECH-306` | mechanism_hypothesis | provisional | 0.804 | 0.599 | 0.872 | 1 | 4 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.768 | 0.602 | 0.823 | 1 | 8 | plausible_unproven |
| `SD-013` | design_decision | provisional | 0.723 | 0.608 | 0.838 | 4 | 4 | plausible_unproven |
| `MECH-314` | mechanism_hypothesis | candidate_substrate_landed | 0.806 | 0.610 | 0.871 | 1 | 10 | plausible_unproven |
| `MECH-314a` | - | - | 0.792 | 0.610 | 0.853 | 1 | 6 | plausible_unproven |
| `MECH-346` | mechanism_hypothesis | candidate | 0.750 | 0.611 | 0.797 | 1 | 3 | plausible_unproven |
| `MECH-347` | mechanism_hypothesis | candidate | 0.754 | 0.611 | 0.802 | 1 | 3 | plausible_unproven |
| `SD-057` | design_decision | candidate | 0.698 | 0.611 | 0.742 | 1 | 2 | plausible_unproven |
| `MECH-309` | mechanism_hypothesis | candidate | 0.761 | 0.612 | 0.861 | 2 | 14 | plausible_unproven |
| `MECH-106` | mechanism_hypothesis | provisional | 0.748 | 0.613 | 0.838 | 2 | 5 | plausible_unproven |
| `MECH-045` | mechanism_hypothesis | provisional | 0.786 | 0.614 | 0.843 | 1 | 14 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.707 | 0.615 | 0.769 | 2 | 3 | plausible_unproven |
| `MECH-261` | mechanism_hypothesis | stable | 0.763 | 0.615 | 0.862 | 2 | 20 | plausible_unproven |

_Suppressed by gating: 56 substrate_coherence (ARC + universal invariant), 65 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.875 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.842 | 3 |
| `ARC-014` | architectural_commitment | active | 0.761 | 3 |
| `ARC-011` | architectural_commitment | active | 0.752 | 1 |
| `ARC-001` | architectural_commitment | active | 0.662 | 1 |
| `INV-014` | invariant | active | 0.662 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-079` | open_question | resolved | 0.832 | 5 |
| `Q-017` | open_question | active | 0.830 | 7 |
| `Q-016` | open_question | active | 0.827 | 5 |
| `Q-015` | open_question | active | 0.808 | 5 |
| `Q-005` | open_question | active | 0.778 | 4 |
| `Q-087` | open_question | resolved | 0.746 | 4 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **0**.

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **75**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-155` | candidate | 0.105 | 1 |
| `INV-054` | candidate | 0.125 | 1 |
| `MECH-063` | provisional | 0.125 | 1 |
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-142` | candidate | 0.125 | 1 |
| `MECH-188` | candidate | 0.125 | 1 |
| `SD-018` | implemented | 0.125 | 1 |
| `SD-021` | candidate | 0.125 | 1 |
| `SD-023` | candidate | 0.125 | 1 |
| `SD-047` | provisional | 0.125 | 1 |
| `MECH-070` | retiring | 0.163 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `MECH-057b` | - | 0.176 | 1 |
| `MECH-295` | candidate | 0.194 | 2 |
| `MECH-111` | candidate | 0.217 | 3 |
| `MECH-128` | candidate | 0.217 | 3 |
| `MECH-445` | candidate | 0.226 | 1 |
| `INV-088` | candidate | 0.237 | 1 |
| `MECH-329` | candidate | 0.260 | 1 |
| `MECH-466` | candidate | 0.271 | 1 |
| `MECH-026` | provisional | 0.275 | 1 |
| `MECH-029` | provisional | 0.275 | 1 |
| `MECH-047` | provisional | 0.275 | 1 |
| `MECH-475` | retired | 0.275 | 1 |
| `MECH-097` | candidate | 0.280 | 1 |
| `MECH-137` | candidate | 0.280 | 1 |
| `MECH-138` | candidate | 0.280 | 1 |
| `MECH-139` | candidate | 0.280 | 1 |
| `MECH-143` | candidate | 0.280 | 1 |
| `MECH-144` | candidate | 0.280 | 1 |
| ... | ... | ... | ... (45 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **203**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `INV-050` | candidate | 0.927 | 8 |
| `MECH-121` | candidate | 0.904 | 5 |
| `SD-037` | candidate | 0.902 | 7 |
| `SD-045` | candidate | 0.900 | 4 |
| `MECH-053` | provisional | 0.882 | 6 |
| `MECH-263` | candidate | 0.882 | 4 |
| `MECH-307` | candidate_substrate_landed | 0.880 | 6 |
| `SD-033b` | - | 0.879 | 5 |
| `MECH-271` | candidate | 0.878 | 4 |
| `MECH-440` | candidate | 0.877 | 5 |
| `Q-035` | resolved | 0.875 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.874 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.873 | 5 |
| `MECH-203` | candidate | 0.872 | 8 |
| `MECH-317` | candidate | 0.870 | 6 |
| `DEV-NEED-009` | - | 0.866 | 4 |
| `SD-033e` | - | 0.865 | 9 |
| `MECH-141` | candidate | 0.864 | 4 |
| `MECH-030` | provisional | 0.863 | 4 |
| `MECH-172` | candidate | 0.863 | 6 |
| `MECH-191` | candidate | 0.861 | 4 |
| `MECH-265` | candidate | 0.860 | 6 |
| `ARC-049` | candidate | 0.859 | 26 |
| `DEV-NEED-012` | - | 0.858 | 6 |
| `MECH-264` | candidate | 0.856 | 5 |
| `MECH-316` | candidate | 0.856 | 9 |
| `SD-032b` | - | 0.856 | 14 |
| `ARC-060` | candidate | 0.853 | 13 |
| `MECH-472` | candidate | 0.853 | 4 |
| `SD-054` | candidate | 0.853 | 7 |
| `MECH-337` | candidate | 0.852 | 4 |
| `SD-039` | candidate | 0.852 | 6 |
| `MECH-171` | candidate | 0.851 | 4 |
| `MECH-198` | candidate | 0.851 | 8 |
| `ARC-078` | candidate | 0.850 | 11 |
| `MECH-334` | candidate | 0.849 | 3 |
| `MECH-197` | candidate | 0.848 | 12 |
| `MECH-168` | candidate | 0.846 | 4 |
| `MECH-269` | candidate | 0.846 | 34 |
| `MECH-280` | candidate | 0.846 | 5 |
| `MECH-281` | candidate | 0.846 | 4 |
| `MECH-434` | candidate | 0.846 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.843 | 5 |
| `ARC-051` | candidate | 0.842 | 4 |
| `MECH-220` | candidate | 0.841 | 4 |
| `INV-048` | candidate | 0.839 | 4 |
| `INV-064` | candidate | 0.838 | 5 |
| `MECH-312` | candidate | 0.838 | 14 |
| `SD-003-SUCCESSOR` | - | 0.838 | 4 |
| `MECH-394` | candidate | 0.836 | 4 |
| ... | ... | ... | ... (153 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
