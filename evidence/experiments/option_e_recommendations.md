# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-05-15T21:22:03.810486Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 218 |
| `substrate_coherence` | 39 |
| `answer_state` | 43 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **70** | plausible_unproven: **225** |
| **low lit**             | novel_discovery: **1**         | speculative: **4** |

Total scored claims: 300

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **146** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.812 | 0.000 | 0.812 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 6 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.638 | 0.000 | 0.638 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.836 | 0.000 | 0.836 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.651 | 0.000 | 0.651 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.709 | 0.000 | 0.709 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.709 | 0.000 | 0.709 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.847 | 0.000 | 0.847 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.815 | 0.000 | 0.815 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.890 | 0.000 | 0.890 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.883 | 0.000 | 0.883 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.755 | 0.000 | 0.755 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.852 | 0.000 | 0.852 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.688 | 0.000 | 0.688 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.887 | 0.000 | 0.887 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.834 | 0.000 | 0.834 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.832 | 0.000 | 0.832 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 3 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.893 | 0.000 | 0.893 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.713 | 0.000 | 0.713 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.910 | 0.000 | 0.910 | 0 | 11 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.787 | 0.000 | 0.787 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.782 | 0.000 | 0.782 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.797 | 0.000 | 0.797 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.895 | 0.000 | 0.895 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.714 | 0.000 | 0.714 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.726 | 0.000 | 0.726 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 3 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.909 | 0.000 | 0.909 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.912 | 0.000 | 0.912 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.848 | 0.000 | 0.848 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.891 | 0.000 | 0.891 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.846 | 0.000 | 0.846 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.839 | 0.000 | 0.839 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.904 | 0.000 | 0.904 | 0 | 4 | plausible_unproven |
| `MECH-273` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 5 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.675 | 0.000 | 0.675 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 13 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 7 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 9 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 6 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.872 | 0.000 | 0.872 | 0 | 4 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 3 | plausible_unproven |
| `MECH-309` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 14 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 14 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.793 | 0.000 | 0.793 | 0 | 2 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.897 | 0.000 | 0.897 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.845 | 0.000 | 0.845 | 0 | 8 | plausible_unproven |
| `MECH-900` | - | - | 0.696 | 0.000 | 0.696 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.901 | 0.000 | 0.901 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.810 | 0.000 | 0.810 | 0 | 5 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.890 | 0.000 | 0.890 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.862 | 0.000 | 0.862 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.824 | 0.000 | 0.824 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.905 | 0.000 | 0.905 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.894 | 0.000 | 0.894 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.851 | 0.000 | 0.851 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.826 | 0.000 | 0.826 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.838 | 0.000 | 0.838 | 0 | 3 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.755 | 0.000 | 0.755 | 0 | 1 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.661 | 0.218 | 0.809 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.678 | 0.235 | 0.826 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.665 | 0.240 | 0.806 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.717 | 0.264 | 0.868 | 1 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.624 | 0.265 | 0.863 | 2 | 8 | plausible_unproven |
| `MECH-116` | mechanism_hypothesis | candidate | 0.629 | 0.265 | 0.871 | 2 | 7 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.717 | 0.265 | 0.868 | 1 | 4 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.705 | 0.270 | 0.850 | 1 | 6 | plausible_unproven |
| `SD-032c` | - | - | 0.666 | 0.270 | 0.798 | 1 | 3 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.653 | 0.289 | 0.895 | 2 | 7 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.641 | 0.292 | 0.874 | 2 | 5 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.703 | 0.301 | 0.837 | 1 | 10 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.680 | 0.302 | 0.806 | 1 | 11 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.751 | 0.312 | 0.898 | 1 | 4 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.740 | 0.355 | 0.868 | 1 | 4 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.631 | 0.370 | 0.892 | 3 | 8 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.744 | 0.380 | 0.866 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.748 | 0.380 | 0.871 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.750 | 0.382 | 0.872 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.762 | 0.384 | 0.888 | 1 | 7 | plausible_unproven |
| `MECH-302` | mechanism_hypothesis | candidate | 0.651 | 0.400 | 0.901 | 3 | 6 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.626 | 0.403 | 0.850 | 4 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.652 | 0.407 | 0.898 | 6 | 7 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.664 | 0.450 | 0.878 | 5 | 6 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.787 | 0.465 | 0.894 | 1 | 5 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.653 | 0.474 | 0.832 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.687 | 0.491 | 0.883 | 10 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.675 | 0.504 | 0.846 | 24 | 9 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.723 | 0.536 | 0.909 | 7 | 10 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.712 | 0.561 | 0.862 | 3 | 5 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.677 | 0.569 | 0.785 | 7 | 3 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.756 | 0.575 | 0.876 | 2 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.710 | 0.578 | 0.842 | 10 | 24 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.749 | 0.600 | 0.899 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.758 | 0.607 | 0.909 | 19 | 9 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.716 | 0.617 | 0.816 | 8 | 13 | plausible_unproven |

_Suppressed by gating: 28 substrate_coherence (ARC + universal invariant), 36 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **0** standard-gating claims with no exp.

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `ARC-003` | architectural_commitment | active | 0.802 | 3 |
| `ARC-005` | architectural_commitment | active | 0.802 | 3 |
| `ARC-014` | architectural_commitment | active | 0.787 | 3 |
| `ARC-011` | architectural_commitment | active | 0.779 | 1 |
| `ARC-001` | architectural_commitment | active | 0.688 | 1 |
| `INV-014` | invariant | active | 0.688 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.863 | 11 |
| `Q-016` | open_question | active | 0.854 | 5 |
| `Q-015` | open_question | active | 0.835 | 5 |
| `Q-005` | open_question | active | 0.805 | 4 |
| `Q-020` | open_question | resolved | 0.778 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.694 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **39**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.218 | 1 |
| `MECH-150` | candidate | 0.224 | 1 |
| `MECH-165` | candidate | 0.235 | 1 |
| `SD-018` | implemented | 0.238 | 1 |
| `MECH-188` | candidate | 0.240 | 1 |
| `SD-023` | candidate | 0.264 | 1 |
| `ARC-032` | candidate | 0.265 | 2 |
| `MECH-116` | candidate | 0.265 | 2 |
| `MECH-220` | candidate | 0.265 | 1 |
| `MECH-091` | candidate | 0.270 | 1 |
| `SD-032c` | - | 0.270 | 1 |
| `MECH-120` | candidate | 0.289 | 2 |
| `MECH-186` | candidate | 0.289 | 2 |
| `MECH-155` | candidate | 0.292 | 2 |
| `SD-047` | provisional | 0.301 | 1 |
| `SD-049` | candidate | 0.302 | 1 |
| `MECH-166` | candidate | 0.312 | 1 |
| `MECH-320` | candidate_substrate_landed | 0.316 | 1 |
| `MECH-128` | candidate | 0.324 | 3 |
| `MECH-047` | provisional | 0.355 | 1 |
| `INV-054` | candidate | 0.368 | 3 |
| `SD-021` | candidate | 0.370 | 3 |
| `MECH-026` | provisional | 0.380 | 1 |
| `MECH-029` | provisional | 0.380 | 1 |
| `MECH-022` | provisional | 0.382 | 1 |
| `MECH-025` | candidate | 0.384 | 1 |
| `MECH-070` | retiring | 0.398 | 4 |
| `MECH-302` | candidate | 0.400 | 3 |
| `MECH-153` | candidate | 0.403 | 4 |
| `MECH-099` | candidate | 0.407 | 6 |
| ... | ... | ... | ... (9 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **110**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-265` | candidate | 0.912 | 6 |
| `MECH-163` | candidate | 0.910 | 11 |
| `MECH-263` | candidate | 0.909 | 4 |
| `SD-033b` | - | 0.905 | 5 |
| `MECH-271` | candidate | 0.904 | 4 |
| `MECH-279` | candidate | 0.903 | 5 |
| `MECH-292` | candidate | 0.901 | 13 |
| `MECH-CBBL-PROPOSED` | - | 0.901 | 7 |
| `MECH-317` | candidate | 0.897 | 9 |
| `MECH-180` | candidate | 0.895 | 4 |
| `SD-033e` | - | 0.894 | 10 |
| `MECH-122` | provisional | 0.893 | 4 |
| `MECH-293` | candidate | 0.892 | 7 |
| `MECH-267` | provisional | 0.891 | 5 |
| `MECH-288` | candidate | 0.891 | 11 |
| `MECH-030` | provisional | 0.890 | 4 |
| `SD-014` | candidate | 0.890 | 13 |
| `MECH-172` | candidate | 0.889 | 6 |
| `MECH-191` | candidate | 0.888 | 4 |
| `MECH-309` | candidate | 0.888 | 14 |
| `MECH-074` | provisional | 0.887 | 9 |
| `MECH-092` | candidate | 0.885 | 16 |
| `MECH-203` | candidate | 0.885 | 7 |
| `MECH-046` | provisional | 0.883 | 4 |
| `MECH-316` | candidate | 0.883 | 9 |
| `SD-054` | candidate | 0.882 | 6 |
| `MECH-171` | candidate | 0.878 | 4 |
| `MECH-273` | candidate | 0.878 | 4 |
| `MECH-295` | candidate | 0.878 | 6 |
| `ARC-060` | candidate | 0.877 | 6 |
| `MECH-294` | candidate | 0.876 | 9 |
| `MECH-285` | candidate | 0.875 | 16 |
| `MECH-168` | candidate | 0.873 | 4 |
| `MECH-280` | candidate | 0.873 | 5 |
| `MECH-281` | candidate | 0.873 | 4 |
| `MECH-269` | candidate | 0.872 | 34 |
| `MECH-303` | candidate | 0.872 | 4 |
| `MECH-264` | candidate | 0.868 | 3 |
| `MECH-121` | candidate | 0.867 | 3 |
| `INV-048` | candidate | 0.865 | 4 |
| `MECH-057b` | - | 0.865 | 4 |
| `SD-003-SUCCESSOR` | - | 0.865 | 4 |
| `SD-037` | candidate | 0.865 | 4 |
| `MECH-312` | candidate | 0.864 | 14 |
| `MECH-275` | candidate | 0.862 | 6 |
| `SD-032d` | - | 0.862 | 4 |
| `MECH-287` | candidate | 0.861 | 7 |
| `MECH-123` | candidate | 0.854 | 5 |
| `MECH-270` | candidate | 0.854 | 4 |
| `MECH-058` | retired | 0.852 | 9 |
| ... | ... | ... | ... (60 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
