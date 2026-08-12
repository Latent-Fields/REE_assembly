# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-08-12T18:24:52.684054Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 395 |
| `substrate_coherence` | 68 |
| `answer_state` | 80 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **100** | plausible_unproven: **433** |
| **low lit**             | novel_discovery: **1**         | speculative: **9** |

Total scored claims: 543

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **264** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.792 | 0.000 | 0.792 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.845 | 0.000 | 0.845 | 0 | 4 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 11 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 2 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.834 | 0.000 | 0.834 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.835 | 0.000 | 0.835 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.846 | 0.000 | 0.846 | 0 | 5 | plausible_unproven |
| `CDQ-007` | - | - | 0.785 | 0.000 | 0.785 | 0 | 8 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.706 | 0.000 | 0.706 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.861 | 0.000 | 0.861 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.706 | 0.000 | 0.706 | 0 | 1 | plausible_unproven |
| `GOV-BEHADJ-1` | governance_rule | candidate | 0.830 | 0.000 | 0.830 | 0 | 9 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.820 | 0.000 | 0.820 | 0 | 9 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.626 | 0.000 | 0.626 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.685 | 0.000 | 0.685 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.841 | 0.000 | 0.841 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.823 | 0.000 | 0.823 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.707 | 0.000 | 0.707 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.834 | 0.000 | 0.834 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.623 | 0.000 | 0.623 | 0 | 1 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.840 | 0.000 | 0.840 | 0 | 5 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.782 | 0.000 | 0.782 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.734 | 0.000 | 0.734 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.807 | 0.000 | 0.807 | 0 | 4 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.716 | 0.000 | 0.716 | 0 | 2 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.841 | 0.000 | 0.841 | 0 | 7 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.831 | 0.000 | 0.831 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.731 | 0.000 | 0.731 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 7 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.827 | 0.000 | 0.827 | 0 | 9 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 3 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 3 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 5 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 8 | plausible_unproven |
| `MECH-130` | mechanism_hypothesis | candidate | 0.685 | 0.000 | 0.685 | 0 | 5 | plausible_unproven |
| `MECH-140` | mechanism_hypothesis | candidate | 0.684 | 0.000 | 0.684 | 0 | 2 | plausible_unproven |
| `MECH-141` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.819 | 0.000 | 0.819 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.853 | 0.000 | 0.853 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.865 | 0.000 | 0.865 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.720 | 0.000 | 0.720 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.742 | 0.000 | 0.742 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 3 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.690 | 0.000 | 0.690 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.715 | 0.000 | 0.715 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.701 | 0.000 | 0.701 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 4 | plausible_unproven |
| `MECH-186` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 3 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.785 | 0.000 | 0.785 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.733 | 0.000 | 0.733 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.701 | 0.000 | 0.701 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.711 | 0.000 | 0.711 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 8 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.694 | 0.000 | 0.694 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.812 | 0.000 | 0.812 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.693 | 0.000 | 0.693 | 0 | 1 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.684 | 0.000 | 0.684 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 7 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 8 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.824 | 0.000 | 0.824 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.815 | 0.000 | 0.815 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.837 | 0.000 | 0.837 | 0 | 6 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.848 | 0.000 | 0.848 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 3 | plausible_unproven |
| `MECH-289` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 4 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.650 | 0.000 | 0.650 | 0 | 1 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 14 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.858 | 0.000 | 0.858 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.875 | 0.000 | 0.875 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.736 | 0.000 | 0.736 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.755 | 0.000 | 0.755 | 0 | 3 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.674 | 0.000 | 0.674 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.819 | 0.000 | 0.819 | 0 | 4 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 3 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.694 | 0.000 | 0.694 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.654 | 0.000 | 0.654 | 0 | 2 | plausible_unproven |
| `MECH-365` | mechanism_hypothesis | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.693 | 0.000 | 0.693 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.694 | 0.000 | 0.694 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.684 | 0.000 | 0.684 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.684 | 0.000 | 0.684 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.735 | 0.000 | 0.735 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.703 | 0.000 | 0.703 | 0 | 1 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.719 | 0.000 | 0.719 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.684 | 0.000 | 0.684 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.808 | 0.000 | 0.808 | 0 | 7 | plausible_unproven |
| `MECH-440` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 5 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 3 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 5 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 4 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 5 | plausible_unproven |
| `MECH-459` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 3 | plausible_unproven |
| `MECH-471` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 3 | plausible_unproven |
| `MECH-472` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-481` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 4 | plausible_unproven |
| `MECH-487` | mechanism_hypothesis | candidate | 0.829 | 0.000 | 0.829 | 0 | 5 | plausible_unproven |
| `MECH-490` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 4 | plausible_unproven |
| `MECH-900` | - | - | 0.671 | 0.000 | 0.671 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.877 | 0.000 | 0.877 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.785 | 0.000 | 0.785 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.877 | 0.000 | 0.877 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.841 | 0.000 | 0.841 | 0 | 4 | plausible_unproven |
| `SD-025` | design_decision | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.684 | 0.000 | 0.684 | 0 | 2 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.815 | 0.000 | 0.815 | 0 | 4 | plausible_unproven |
| `SD-032b` | - | - | 0.868 | 0.000 | 0.868 | 0 | 16 | plausible_unproven |
| `SD-032d` | - | - | 0.838 | 0.000 | 0.838 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.800 | 0.000 | 0.800 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.881 | 0.000 | 0.881 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.872 | 0.000 | 0.872 | 0 | 12 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.841 | 0.000 | 0.841 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.854 | 0.000 | 0.854 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.731 | 0.000 | 0.731 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.902 | 0.000 | 0.902 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.805 | 0.000 | 0.805 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.782 | 0.000 | 0.782 | 0 | 11 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.855 | 0.000 | 0.855 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `SD-068` | design_decision | candidate | 0.797 | 0.000 | 0.797 | 0 | 4 | plausible_unproven |
| `SD-076` | design_decision | candidate | 0.639 | 0.000 | 0.639 | 0 | 8 | plausible_unproven |
| `SD-078` | design_decision | candidate_substrate_landed | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `SD-080` | design_decision | candidate | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `SD-082` | design_decision | candidate_substrate_landed | 0.838 | 0.000 | 0.838 | 0 | 8 | plausible_unproven |
| `SD-091` | design_decision | candidate | 0.782 | 0.000 | 0.782 | 0 | 5 | plausible_unproven |
| `SD-092` | design_decision | candidate | 0.691 | 0.000 | 0.691 | 0 | 2 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.663 | 0.105 | 0.849 | 1 | 5 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.651 | 0.125 | 0.826 | 1 | 6 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.632 | 0.125 | 0.801 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.663 | 0.125 | 0.843 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.664 | 0.125 | 0.844 | 1 | 4 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.641 | 0.125 | 0.813 | 1 | 10 | plausible_unproven |
| `MECH-057b` | - | - | 0.679 | 0.195 | 0.841 | 1 | 4 | plausible_unproven |
| `INV-088` | invariant | candidate | 0.677 | 0.256 | 0.818 | 1 | 6 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.700 | 0.275 | 0.842 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.703 | 0.275 | 0.846 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.701 | 0.275 | 0.843 | 1 | 4 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.657 | 0.279 | 0.783 | 1 | 5 | plausible_unproven |
| `MECH-144` | mechanism_hypothesis | candidate | 0.677 | 0.280 | 0.810 | 1 | 4 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.735 | 0.294 | 0.882 | 1 | 6 | plausible_unproven |
| `MECH-475` | mechanism_hypothesis | retired | 0.680 | 0.294 | 0.808 | 1 | 5 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.713 | 0.300 | 0.851 | 1 | 9 | plausible_unproven |
| `SD-087` | design_decision | candidate | 0.691 | 0.300 | 0.822 | 1 | 4 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.728 | 0.303 | 0.869 | 1 | 4 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.726 | 0.303 | 0.867 | 1 | 5 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate | 0.740 | 0.303 | 0.886 | 1 | 6 | plausible_unproven |
| `MECH-428` | mechanism | candidate | 0.638 | 0.304 | 0.749 | 1 | 3 | plausible_unproven |
| `SD-009` | design_decision | candidate | 0.658 | 0.315 | 0.772 | 1 | 3 | plausible_unproven |
| `MECH-357` | mechanism_hypothesis | candidate | 0.654 | 0.317 | 0.766 | 1 | 3 | plausible_unproven |
| `MECH-236` | mechanism_hypothesis | candidate | 0.699 | 0.322 | 0.824 | 1 | 4 | plausible_unproven |
| `MECH-457` | mechanism_hypothesis | candidate | 0.628 | 0.328 | 0.828 | 2 | 22 | plausible_unproven |
| `MECH-314b` | - | - | 0.707 | 0.333 | 0.832 | 1 | 3 | plausible_unproven |
| `MECH-314c` | - | - | 0.736 | 0.333 | 0.870 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.650 | 0.354 | 0.848 | 2 | 5 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.667 | 0.390 | 0.851 | 2 | 5 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.639 | 0.394 | 0.884 | 7 | 10 | plausible_unproven |
| `MECH-476` | mechanism_hypothesis | retired | 0.621 | 0.400 | 0.842 | 3 | 5 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.639 | 0.406 | 0.873 | 3 | 4 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.656 | 0.428 | 0.884 | 19 | 9 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.671 | 0.456 | 0.886 | 3 | 11 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.767 | 0.456 | 0.871 | 1 | 4 | plausible_unproven |
| `MECH-074d` | - | - | 0.636 | 0.465 | 0.807 | 4 | 4 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.657 | 0.478 | 0.836 | 5 | 8 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.667 | 0.497 | 0.837 | 5 | 12 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.645 | 0.504 | 0.786 | 26 | 3 | plausible_unproven |
| `Q-034` | question | open | 0.638 | 0.505 | 0.770 | 5 | 6 | plausible_unproven |
| `MECH-025b` | - | - | 0.678 | 0.509 | 0.791 | 2 | 4 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.646 | 0.518 | 0.774 | 3 | 5 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.680 | 0.523 | 0.838 | 5 | 8 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | candidate | 0.674 | 0.530 | 0.818 | 11 | 24 | plausible_unproven |
| `INV-089` | invariant | provisional | 0.683 | 0.531 | 0.785 | 2 | 3 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.699 | 0.533 | 0.865 | 3 | 14 | plausible_unproven |
| `MECH-256` | mechanism_hypothesis | candidate | 0.692 | 0.540 | 0.843 | 6 | 9 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.695 | 0.545 | 0.845 | 5 | 25 | plausible_unproven |
| `MECH-231` | mechanism_hypothesis | provisional | 0.713 | 0.555 | 0.765 | 1 | 3 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.780 | 0.555 | 0.855 | 1 | 8 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.715 | 0.565 | 0.866 | 3 | 13 | plausible_unproven |
| `MECH-089` | mechanism_hypothesis | active | 0.710 | 0.569 | 0.851 | 12 | 10 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.774 | 0.575 | 0.841 | 1 | 15 | plausible_unproven |
| `MECH-057a` | - | - | 0.762 | 0.575 | 0.825 | 1 | 5 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.737 | 0.575 | 0.791 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.756 | 0.575 | 0.817 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.763 | 0.575 | 0.826 | 1 | 8 | plausible_unproven |
| `MECH-062` | mechanism_hypothesis | candidate | 0.692 | 0.575 | 0.751 | 1 | 2 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.786 | 0.575 | 0.856 | 1 | 4 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.769 | 0.575 | 0.834 | 1 | 7 | plausible_unproven |
| `MECH-259` | mechanism_hypothesis | stable | 0.669 | 0.575 | 0.716 | 1 | 2 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.732 | 0.575 | 0.784 | 1 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.790 | 0.575 | 0.861 | 1 | 20 | plausible_unproven |
| `SD-035` | design_decision | stable | 0.786 | 0.575 | 0.856 | 1 | 6 | plausible_unproven |
| `MECH-135` | mechanism_hypothesis | candidate | 0.704 | 0.582 | 0.826 | 7 | 11 | plausible_unproven |
| `SD-048` | design_decision | candidate | 0.748 | 0.582 | 0.859 | 2 | 6 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.704 | 0.584 | 0.825 | 4 | 7 | plausible_unproven |
| `MECH-071` | mechanism_hypothesis | provisional | 0.720 | 0.588 | 0.851 | 38 | 4 | plausible_unproven |
| `MECH-150` | mechanism_hypothesis | candidate | 0.651 | 0.589 | 0.714 | 2 | 2 | plausible_unproven |
| `SD-007` | design_decision | implemented | 0.721 | 0.593 | 0.850 | 19 | 5 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.709 | 0.597 | 0.822 | 25 | 9 | plausible_unproven |
| `SD-013` | design_decision | provisional | 0.724 | 0.608 | 0.841 | 4 | 4 | plausible_unproven |
| `MECH-106` | mechanism_hypothesis | provisional | 0.750 | 0.613 | 0.841 | 2 | 5 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.709 | 0.615 | 0.771 | 2 | 3 | plausible_unproven |
| `MECH-261` | mechanism_hypothesis | stable | 0.764 | 0.615 | 0.864 | 2 | 20 | plausible_unproven |
| `MECH-306` | mechanism_hypothesis | provisional | 0.810 | 0.617 | 0.874 | 1 | 4 | plausible_unproven |

_Suppressed by gating: 53 substrate_coherence (ARC + universal invariant), 62 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.877 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.844 | 3 |
| `ARC-014` | architectural_commitment | active | 0.763 | 3 |
| `ARC-011` | architectural_commitment | active | 0.754 | 1 |
| `ARC-001` | architectural_commitment | active | 0.664 | 1 |
| `INV-014` | invariant | active | 0.664 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.842 | 11 |
| `Q-079` | open_question | resolved | 0.834 | 5 |
| `Q-016` | open_question | active | 0.830 | 5 |
| `Q-015` | open_question | active | 0.811 | 5 |
| `Q-005` | open_question | active | 0.780 | 4 |
| `Q-087` | open_question | resolved | 0.749 | 4 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-151` | candidate | 0.754 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **81**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-155` | candidate | 0.105 | 1 |
| `MECH-063` | provisional | 0.125 | 1 |
| `MECH-091` | candidate | 0.125 | 1 |
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-142` | candidate | 0.125 | 1 |
| `MECH-165` | candidate | 0.125 | 1 |
| `MECH-188` | candidate | 0.125 | 1 |
| `MECH-220` | candidate | 0.125 | 1 |
| `SD-018` | implemented | 0.125 | 1 |
| `SD-023` | candidate | 0.125 | 1 |
| `SD-032c` | - | 0.125 | 1 |
| `SD-047` | provisional | 0.125 | 1 |
| `MECH-070` | retiring | 0.163 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `MECH-057b` | - | 0.195 | 1 |
| `MECH-295` | candidate | 0.212 | 2 |
| `MECH-128` | candidate | 0.217 | 3 |
| `INV-054` | candidate | 0.225 | 3 |
| `SD-021` | candidate | 0.225 | 3 |
| `MECH-445` | candidate | 0.244 | 1 |
| `INV-088` | candidate | 0.256 | 1 |
| `MECH-111` | candidate | 0.269 | 4 |
| `MECH-026` | provisional | 0.275 | 1 |
| `MECH-029` | provisional | 0.275 | 1 |
| `MECH-047` | provisional | 0.275 | 1 |
| `MECH-329` | candidate | 0.279 | 1 |
| `MECH-097` | candidate | 0.280 | 1 |
| `MECH-137` | candidate | 0.280 | 1 |
| `MECH-138` | candidate | 0.280 | 1 |
| `MECH-139` | candidate | 0.280 | 1 |
| ... | ... | ... | ... (51 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **196**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.906 | 5 |
| `SD-045` | candidate | 0.902 | 4 |
| `MECH-263` | candidate | 0.884 | 4 |
| `SD-033b` | - | 0.881 | 5 |
| `MECH-271` | candidate | 0.880 | 4 |
| `MECH-440` | candidate | 0.879 | 5 |
| `MECH-CBBL-PROPOSED` | - | 0.877 | 7 |
| `Q-035` | resolved | 0.877 | 15 |
| `MECH-203` | candidate | 0.875 | 8 |
| `MECH-264` | candidate | 0.875 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.875 | 5 |
| `MECH-317` | candidate | 0.873 | 9 |
| `MECH-265` | candidate | 0.872 | 8 |
| `SD-033e` | - | 0.872 | 12 |
| `DEV-NEED-009` | - | 0.868 | 4 |
| `SD-032b` | - | 0.868 | 16 |
| `MECH-030` | provisional | 0.866 | 4 |
| `MECH-141` | candidate | 0.866 | 4 |
| `MECH-172` | candidate | 0.865 | 6 |
| `MECH-191` | candidate | 0.864 | 4 |
| `ARC-049` | candidate | 0.863 | 27 |
| `DEV-NEED-012` | - | 0.861 | 6 |
| `MECH-316` | candidate | 0.858 | 9 |
| `ARC-060` | candidate | 0.855 | 13 |
| `MECH-472` | candidate | 0.855 | 4 |
| `SD-054` | candidate | 0.855 | 7 |
| `MECH-337` | candidate | 0.854 | 4 |
| `SD-039` | candidate | 0.854 | 6 |
| `ARC-078` | candidate | 0.853 | 11 |
| `MECH-171` | candidate | 0.853 | 4 |
| `MECH-198` | candidate | 0.853 | 8 |
| `MECH-334` | candidate | 0.852 | 3 |
| `MECH-197` | candidate | 0.850 | 12 |
| `MECH-434` | candidate | 0.849 | 4 |
| `MECH-168` | candidate | 0.848 | 4 |
| `MECH-269` | candidate | 0.848 | 34 |
| `MECH-280` | candidate | 0.848 | 5 |
| `MECH-281` | candidate | 0.848 | 4 |
| `CANDIDATE-contextual-memory-allocation-gate` | - | 0.846 | 5 |
| `ARC-051` | candidate | 0.845 | 4 |
| `INV-048` | candidate | 0.841 | 4 |
| `MECH-044` | provisional | 0.841 | 7 |
| `SD-003-SUCCESSOR` | - | 0.841 | 4 |
| `SD-037` | candidate | 0.841 | 4 |
| `INV-064` | candidate | 0.840 | 5 |
| `MECH-312` | candidate | 0.840 | 14 |
| `MECH-394` | candidate | 0.839 | 4 |
| `SD-032d` | - | 0.838 | 4 |
| `SD-082` | candidate_substrate_landed | 0.838 | 8 |
| `MECH-275` | candidate | 0.837 | 6 |
| ... | ... | ... | ... (146 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
