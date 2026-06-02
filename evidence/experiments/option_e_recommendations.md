# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-06-02T05:21:23.066638Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 248 |
| `substrate_coherence` | 47 |
| `answer_state` | 44 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **63** | plausible_unproven: **269** |
| **low lit**             | novel_discovery: **2**         | speculative: **5** |

Total scored claims: 339

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **178** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 27 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.812 | 0.000 | 0.812 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 13 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 9 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.888 | 0.000 | 0.888 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.725 | 0.000 | 0.725 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.880 | 0.000 | 0.880 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.809 | 0.000 | 0.809 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.825 | 0.000 | 0.825 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.725 | 0.000 | 0.725 | 0 | 1 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.633 | 0.000 | 0.633 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.757 | 0.000 | 0.757 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.831 | 0.000 | 0.831 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.646 | 0.000 | 0.646 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.843 | 0.000 | 0.843 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.727 | 0.000 | 0.727 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.853 | 0.000 | 0.853 | 0 | 5 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.810 | 0.000 | 0.810 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.885 | 0.000 | 0.885 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.879 | 0.000 | 0.879 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.751 | 0.000 | 0.751 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.860 | 0.000 | 0.860 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.847 | 0.000 | 0.847 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.684 | 0.000 | 0.684 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.882 | 0.000 | 0.882 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.827 | 0.000 | 0.827 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.799 | 0.000 | 0.799 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.835 | 0.000 | 0.835 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.926 | 0.000 | 0.926 | 0 | 5 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.888 | 0.000 | 0.888 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.708 | 0.000 | 0.708 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 11 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.893 | 0.000 | 0.893 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.782 | 0.000 | 0.782 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.819 | 0.000 | 0.819 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.762 | 0.000 | 0.762 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.709 | 0.000 | 0.709 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.721 | 0.000 | 0.721 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 4 | plausible_unproven |
| `MECH-189` | mechanism_hypothesis | candidate | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.883 | 0.000 | 0.883 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.813 | 0.000 | 0.813 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.804 | 0.000 | 0.804 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.720 | 0.000 | 0.720 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.770 | 0.000 | 0.770 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 7 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.904 | 0.000 | 0.904 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.908 | 0.000 | 0.908 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.844 | 0.000 | 0.844 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.886 | 0.000 | 0.886 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.845 | 0.000 | 0.845 | 0 | 8 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.834 | 0.000 | 0.834 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.900 | 0.000 | 0.900 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.898 | 0.000 | 0.898 | 0 | 5 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 15 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.886 | 0.000 | 0.886 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.670 | 0.000 | 0.670 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.888 | 0.000 | 0.888 | 0 | 24 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 12 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.845 | 0.000 | 0.845 | 0 | 3 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.859 | 0.000 | 0.859 | 0 | 14 | plausible_unproven |
| `MECH-314` | mechanism_hypothesis | candidate_substrate_landed | 0.884 | 0.000 | 0.884 | 0 | 6 | plausible_unproven |
| `MECH-314a` | - | - | 0.861 | 0.000 | 0.861 | 0 | 5 | plausible_unproven |
| `MECH-314b` | - | - | 0.795 | 0.000 | 0.795 | 0 | 2 | plausible_unproven |
| `MECH-314c` | - | - | 0.827 | 0.000 | 0.827 | 0 | 3 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 9 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 8 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.895 | 0.000 | 0.895 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 1 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.896 | 0.000 | 0.896 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.805 | 0.000 | 0.805 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.897 | 0.000 | 0.897 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.860 | 0.000 | 0.860 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.742 | 0.000 | 0.742 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.886 | 0.000 | 0.886 | 0 | 13 | plausible_unproven |
| `SD-032d` | - | - | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.819 | 0.000 | 0.819 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.900 | 0.000 | 0.900 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.889 | 0.000 | 0.889 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.846 | 0.000 | 0.846 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.821 | 0.000 | 0.821 | 0 | 2 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.874 | 0.000 | 0.874 | 0 | 6 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.750 | 0.000 | 0.750 | 0 | 1 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.878 | 0.000 | 0.878 | 0 | 6 | plausible_unproven |
| `MECH-118` | mechanism_hypothesis | candidate | 0.648 | 0.179 | 0.804 | 1 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.665 | 0.197 | 0.821 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.651 | 0.201 | 0.801 | 1 | 3 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.704 | 0.226 | 0.863 | 1 | 4 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.705 | 0.226 | 0.864 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.652 | 0.231 | 0.793 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.693 | 0.232 | 0.846 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.644 | 0.251 | 0.906 | 2 | 11 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.623 | 0.253 | 0.869 | 2 | 5 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.690 | 0.262 | 0.832 | 1 | 10 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.726 | 0.291 | 0.871 | 1 | 3 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.720 | 0.298 | 0.860 | 1 | 4 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.727 | 0.317 | 0.863 | 1 | 4 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.732 | 0.341 | 0.862 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.735 | 0.341 | 0.866 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.737 | 0.344 | 0.868 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.749 | 0.346 | 0.883 | 1 | 7 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.622 | 0.354 | 0.801 | 2 | 11 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.631 | 0.369 | 0.894 | 6 | 7 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.672 | 0.371 | 0.873 | 2 | 6 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.642 | 0.412 | 0.873 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.631 | 0.436 | 0.827 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.665 | 0.452 | 0.878 | 10 | 14 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.764 | 0.453 | 0.868 | 1 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.764 | 0.453 | 0.868 | 1 | 4 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.653 | 0.466 | 0.841 | 24 | 9 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.701 | 0.497 | 0.904 | 7 | 10 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.738 | 0.509 | 0.890 | 2 | 5 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate_substrate_landed | 0.709 | 0.515 | 0.839 | 2 | 3 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.690 | 0.522 | 0.858 | 3 | 5 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.737 | 0.536 | 0.871 | 2 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.689 | 0.540 | 0.837 | 10 | 24 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.661 | 0.541 | 0.781 | 6 | 3 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.728 | 0.561 | 0.894 | 7 | 14 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.737 | 0.569 | 0.904 | 19 | 9 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.760 | 0.587 | 0.875 | 2 | 8 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.701 | 0.594 | 0.809 | 28 | 3 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.795 | 0.599 | 0.860 | 1 | 15 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.757 | 0.599 | 0.810 | 1 | 11 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.778 | 0.599 | 0.837 | 1 | 18 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.784 | 0.599 | 0.846 | 1 | 8 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.753 | 0.599 | 0.804 | 1 | 3 | plausible_unproven |
| `MECH-057a` | - | - | 0.784 | 0.601 | 0.845 | 1 | 5 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.708 | 0.604 | 0.811 | 9 | 13 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.725 | 0.615 | 0.835 | 83 | 7 | plausible_unproven |

_Suppressed by gating: 36 substrate_coherence (ARC + universal invariant), 33 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **1** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.897 | 15 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `INV-010` | invariant | active | 0.864 | 3 |
| `ARC-003` | architectural_commitment | active | 0.797 | 3 |
| `ARC-005` | architectural_commitment | active | 0.797 | 3 |
| `ARC-014` | architectural_commitment | active | 0.783 | 3 |
| `ARC-011` | architectural_commitment | active | 0.774 | 1 |
| `ARC-001` | architectural_commitment | active | 0.684 | 1 |
| `INV-014` | invariant | active | 0.684 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.858 | 11 |
| `Q-016` | open_question | active | 0.849 | 5 |
| `Q-015` | open_question | active | 0.830 | 5 |
| `Q-005` | open_question | active | 0.800 | 4 |
| `Q-020` | open_question | resolved | 0.774 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **2**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `MECH-341` | candidate | 0.821 | 0.000 | 2 | 0 |
| `onboarding` | - | 0.655 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **46**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-118` | candidate | 0.179 | 1 |
| `MECH-150` | candidate | 0.186 | 1 |
| `MECH-165` | candidate | 0.197 | 1 |
| `SD-018` | implemented | 0.199 | 1 |
| `MECH-188` | candidate | 0.201 | 1 |
| `MECH-220` | candidate | 0.226 | 1 |
| `SD-023` | candidate | 0.226 | 1 |
| `ARC-032` | candidate | 0.227 | 2 |
| `MECH-116` | candidate | 0.227 | 2 |
| `SD-032c` | - | 0.231 | 1 |
| `MECH-091` | candidate | 0.232 | 1 |
| `MECH-120` | candidate | 0.251 | 2 |
| `MECH-186` | candidate | 0.251 | 2 |
| `MECH-155` | candidate | 0.253 | 2 |
| `SD-047` | provisional | 0.262 | 1 |
| `MECH-128` | candidate | 0.286 | 3 |
| `MECH-334` | candidate | 0.291 | 1 |
| `SD-037` | candidate | 0.298 | 1 |
| `MECH-047` | provisional | 0.317 | 1 |
| `INV-054` | candidate | 0.329 | 3 |
| `SD-021` | candidate | 0.331 | 3 |
| `MECH-026` | provisional | 0.341 | 1 |
| `MECH-029` | provisional | 0.341 | 1 |
| `MECH-022` | provisional | 0.344 | 1 |
| `MECH-025` | candidate | 0.346 | 1 |
| `SD-049` | candidate | 0.354 | 2 |
| `MECH-070` | retiring | 0.359 | 4 |
| `MECH-153` | candidate | 0.364 | 4 |
| `MECH-099` | candidate | 0.369 | 6 |
| `MECH-295` | candidate | 0.371 | 2 |
| ... | ... | ... | ... (16 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **133**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-121` | candidate | 0.926 | 5 |
| `MECH-265` | candidate | 0.908 | 6 |
| `MECH-163` | candidate | 0.905 | 11 |
| `MECH-263` | candidate | 0.904 | 4 |
| `MECH-271` | candidate | 0.900 | 4 |
| `SD-033b` | - | 0.900 | 5 |
| `MECH-279` | candidate | 0.898 | 5 |
| `Q-035` | resolved | 0.897 | 15 |
| `MECH-CBBL-PROPOSED` | - | 0.896 | 7 |
| `MECH-320` | candidate_substrate_landed | 0.895 | 5 |
| `MECH-166` | candidate | 0.893 | 4 |
| `MECH-317` | candidate | 0.892 | 9 |
| `MECH-180` | candidate | 0.891 | 4 |
| `SD-033e` | - | 0.889 | 10 |
| `DEV-NEED-009` | - | 0.888 | 4 |
| `MECH-122` | provisional | 0.888 | 4 |
| `MECH-292` | candidate | 0.888 | 24 |
| `MECH-293` | candidate | 0.887 | 12 |
| `MECH-267` | provisional | 0.886 | 5 |
| `MECH-288` | candidate | 0.886 | 11 |
| `SD-014` | candidate | 0.886 | 13 |
| `MECH-030` | provisional | 0.885 | 4 |
| `MECH-172` | candidate | 0.885 | 6 |
| `MECH-314` | candidate_substrate_landed | 0.884 | 6 |
| `ARC-049` | candidate | 0.883 | 27 |
| `MECH-191` | candidate | 0.883 | 4 |
| `MECH-074` | provisional | 0.882 | 9 |
| `MECH-203` | candidate | 0.881 | 7 |
| `DEV-NEED-012` | - | 0.880 | 6 |
| `MECH-092` | candidate | 0.880 | 16 |
| `MECH-046` | provisional | 0.879 | 4 |
| `MECH-316` | candidate | 0.878 | 9 |
| `SD-054` | candidate | 0.878 | 6 |
| `ARC-060` | candidate | 0.875 | 13 |
| `MECH-337` | candidate | 0.874 | 4 |
| `SD-039` | candidate | 0.874 | 6 |
| `MECH-171` | candidate | 0.873 | 4 |
| `MECH-198` | candidate | 0.873 | 8 |
| `MECH-294` | candidate | 0.871 | 9 |
| `MECH-197` | candidate | 0.870 | 12 |
| `MECH-285` | candidate | 0.870 | 16 |
| `MECH-168` | candidate | 0.868 | 4 |
| `MECH-269` | candidate | 0.868 | 34 |
| `ARC-078` | candidate | 0.867 | 9 |
| `MECH-303` | candidate | 0.867 | 4 |
| `MECH-264` | candidate | 0.864 | 3 |
| `INV-048` | candidate | 0.861 | 4 |
| `MECH-314a` | - | 0.861 | 5 |
| `MECH-057b` | - | 0.860 | 4 |
| `SD-003-SUCCESSOR` | - | 0.860 | 4 |
| ... | ... | ... | ... (83 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
