# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-05-12T18:15:44.409043Z`

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
| **high lit (>= 0.55)** | confirmed_established: **69** | plausible_unproven: **226** |
| **low lit**             | novel_discovery: **1**         | speculative: **4** |

Total scored claims: 300

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **146** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 6 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.639 | 0.000 | 0.639 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.763 | 0.000 | 0.763 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.837 | 0.000 | 0.837 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.651 | 0.000 | 0.651 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.710 | 0.000 | 0.710 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.848 | 0.000 | 0.848 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.816 | 0.000 | 0.816 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.891 | 0.000 | 0.891 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.781 | 0.000 | 0.781 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.884 | 0.000 | 0.884 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.756 | 0.000 | 0.756 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.853 | 0.000 | 0.853 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.888 | 0.000 | 0.888 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.835 | 0.000 | 0.835 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 3 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.894 | 0.000 | 0.894 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.714 | 0.000 | 0.714 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.911 | 0.000 | 0.911 | 0 | 11 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.787 | 0.000 | 0.787 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.890 | 0.000 | 0.890 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.782 | 0.000 | 0.782 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.896 | 0.000 | 0.896 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.715 | 0.000 | 0.715 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.726 | 0.000 | 0.726 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.810 | 0.000 | 0.810 | 0 | 3 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.910 | 0.000 | 0.910 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.869 | 0.000 | 0.869 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.913 | 0.000 | 0.913 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.849 | 0.000 | 0.849 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.892 | 0.000 | 0.892 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.847 | 0.000 | 0.847 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.840 | 0.000 | 0.840 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 4 | plausible_unproven |
| `MECH-272` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 14 | plausible_unproven |
| `MECH-273` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 5 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.862 | 0.000 | 0.862 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.676 | 0.000 | 0.676 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 13 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 7 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 9 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 6 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 3 | plausible_unproven |
| `MECH-309` | mechanism_hypothesis | candidate | 0.889 | 0.000 | 0.889 | 0 | 14 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 14 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.794 | 0.000 | 0.794 | 0 | 2 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.884 | 0.000 | 0.884 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.898 | 0.000 | 0.898 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 8 | plausible_unproven |
| `MECH-900` | - | - | 0.696 | 0.000 | 0.696 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.902 | 0.000 | 0.902 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.810 | 0.000 | 0.810 | 0 | 5 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.891 | 0.000 | 0.891 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.863 | 0.000 | 0.863 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.825 | 0.000 | 0.825 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.906 | 0.000 | 0.906 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.895 | 0.000 | 0.895 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.852 | 0.000 | 0.852 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.827 | 0.000 | 0.827 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.839 | 0.000 | 0.839 | 0 | 3 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.756 | 0.000 | 0.756 | 0 | 1 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.883 | 0.000 | 0.883 | 0 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.664 | 0.225 | 0.810 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.681 | 0.242 | 0.827 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.667 | 0.246 | 0.807 | 1 | 3 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.720 | 0.271 | 0.869 | 1 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.627 | 0.272 | 0.864 | 2 | 8 | plausible_unproven |
| `MECH-116` | mechanism_hypothesis | candidate | 0.632 | 0.272 | 0.872 | 2 | 7 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.719 | 0.272 | 0.868 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.668 | 0.276 | 0.799 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.708 | 0.277 | 0.851 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.656 | 0.296 | 0.896 | 2 | 7 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.645 | 0.299 | 0.875 | 2 | 5 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.705 | 0.308 | 0.838 | 1 | 10 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.683 | 0.309 | 0.807 | 1 | 11 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.754 | 0.319 | 0.899 | 1 | 4 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.742 | 0.362 | 0.868 | 1 | 4 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.634 | 0.376 | 0.892 | 3 | 8 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.747 | 0.387 | 0.867 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.750 | 0.387 | 0.871 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.752 | 0.389 | 0.873 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.750 | 0.391 | 0.869 | 1 | 5 | plausible_unproven |
| `MECH-302` | mechanism_hypothesis | candidate | 0.654 | 0.407 | 0.902 | 3 | 6 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.630 | 0.410 | 0.851 | 4 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.656 | 0.414 | 0.899 | 6 | 7 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.667 | 0.457 | 0.878 | 5 | 6 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.789 | 0.471 | 0.895 | 1 | 5 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.657 | 0.481 | 0.833 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.691 | 0.497 | 0.884 | 10 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.679 | 0.511 | 0.847 | 24 | 9 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.726 | 0.543 | 0.909 | 7 | 10 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.715 | 0.568 | 0.863 | 3 | 5 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.681 | 0.576 | 0.786 | 7 | 3 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.758 | 0.581 | 0.876 | 2 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.714 | 0.585 | 0.843 | 10 | 24 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.753 | 0.607 | 0.900 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.762 | 0.614 | 0.910 | 19 | 9 | plausible_unproven |

_Suppressed by gating: 30 substrate_coherence (ARC + universal invariant), 36 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **0** standard-gating claims with no exp.

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `ARC-003` | architectural_commitment | active | 0.803 | 3 |
| `ARC-005` | architectural_commitment | active | 0.803 | 3 |
| `ARC-014` | architectural_commitment | active | 0.788 | 3 |
| `ARC-011` | architectural_commitment | active | 0.780 | 1 |
| `ARC-001` | architectural_commitment | active | 0.689 | 1 |
| `INV-014` | invariant | active | 0.689 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.864 | 11 |
| `Q-016` | open_question | active | 0.855 | 5 |
| `Q-015` | open_question | active | 0.836 | 5 |
| `Q-005` | open_question | active | 0.805 | 4 |
| `Q-020` | open_question | resolved | 0.779 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.701 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **39**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.225 | 1 |
| `MECH-150` | candidate | 0.231 | 1 |
| `MECH-165` | candidate | 0.242 | 1 |
| `SD-018` | implemented | 0.245 | 1 |
| `MECH-188` | candidate | 0.246 | 1 |
| `SD-023` | candidate | 0.271 | 1 |
| `ARC-032` | candidate | 0.272 | 2 |
| `MECH-116` | candidate | 0.272 | 2 |
| `MECH-220` | candidate | 0.272 | 1 |
| `SD-032c` | - | 0.276 | 1 |
| `MECH-091` | candidate | 0.277 | 1 |
| `MECH-120` | candidate | 0.296 | 2 |
| `MECH-186` | candidate | 0.296 | 2 |
| `MECH-155` | candidate | 0.299 | 2 |
| `SD-047` | provisional | 0.308 | 1 |
| `SD-049` | candidate | 0.309 | 1 |
| `MECH-166` | candidate | 0.319 | 1 |
| `MECH-320` | candidate_substrate_landed | 0.323 | 1 |
| `MECH-128` | candidate | 0.331 | 3 |
| `MECH-047` | provisional | 0.362 | 1 |
| `INV-054` | candidate | 0.375 | 3 |
| `SD-021` | candidate | 0.376 | 3 |
| `MECH-026` | provisional | 0.387 | 1 |
| `MECH-029` | provisional | 0.387 | 1 |
| `MECH-022` | provisional | 0.389 | 1 |
| `MECH-025` | candidate | 0.391 | 1 |
| `MECH-070` | retiring | 0.405 | 4 |
| `MECH-302` | candidate | 0.407 | 3 |
| `MECH-153` | candidate | 0.410 | 4 |
| `MECH-099` | candidate | 0.414 | 6 |
| ... | ... | ... | ... (9 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **111**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-265` | candidate | 0.913 | 6 |
| `MECH-163` | candidate | 0.911 | 11 |
| `MECH-263` | candidate | 0.910 | 4 |
| `SD-033b` | - | 0.906 | 5 |
| `MECH-271` | candidate | 0.905 | 4 |
| `MECH-279` | candidate | 0.903 | 5 |
| `MECH-292` | candidate | 0.902 | 13 |
| `MECH-CBBL-PROPOSED` | - | 0.902 | 7 |
| `MECH-317` | candidate | 0.898 | 9 |
| `MECH-180` | candidate | 0.896 | 4 |
| `SD-033e` | - | 0.895 | 10 |
| `MECH-122` | provisional | 0.894 | 4 |
| `MECH-267` | provisional | 0.892 | 5 |
| `MECH-288` | candidate | 0.892 | 11 |
| `MECH-293` | candidate | 0.892 | 7 |
| `MECH-030` | provisional | 0.891 | 4 |
| `SD-014` | candidate | 0.891 | 13 |
| `MECH-172` | candidate | 0.890 | 6 |
| `MECH-191` | candidate | 0.889 | 4 |
| `MECH-309` | candidate | 0.889 | 14 |
| `MECH-074` | provisional | 0.888 | 9 |
| `MECH-092` | candidate | 0.886 | 16 |
| `MECH-203` | candidate | 0.886 | 7 |
| `MECH-046` | provisional | 0.884 | 4 |
| `MECH-316` | candidate | 0.884 | 9 |
| `SD-054` | candidate | 0.883 | 6 |
| `MECH-272` | candidate | 0.880 | 14 |
| `MECH-171` | candidate | 0.879 | 4 |
| `MECH-295` | candidate | 0.879 | 6 |
| `ARC-060` | candidate | 0.878 | 6 |
| `MECH-273` | candidate | 0.878 | 4 |
| `MECH-294` | candidate | 0.877 | 9 |
| `MECH-285` | candidate | 0.876 | 16 |
| `MECH-168` | candidate | 0.874 | 4 |
| `MECH-280` | candidate | 0.874 | 5 |
| `MECH-269` | candidate | 0.873 | 34 |
| `MECH-281` | candidate | 0.873 | 4 |
| `MECH-303` | candidate | 0.873 | 4 |
| `MECH-264` | candidate | 0.869 | 3 |
| `MECH-121` | candidate | 0.868 | 3 |
| `INV-048` | candidate | 0.866 | 4 |
| `MECH-057b` | - | 0.866 | 4 |
| `SD-003-SUCCESSOR` | - | 0.866 | 4 |
| `SD-037` | candidate | 0.866 | 4 |
| `MECH-312` | candidate | 0.865 | 14 |
| `MECH-275` | candidate | 0.863 | 6 |
| `SD-032d` | - | 0.863 | 4 |
| `MECH-287` | candidate | 0.862 | 7 |
| `MECH-123` | candidate | 0.855 | 5 |
| `MECH-270` | candidate | 0.855 | 4 |
| ... | ... | ... | ... (61 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
