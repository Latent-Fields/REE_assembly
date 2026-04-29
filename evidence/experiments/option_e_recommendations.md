# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-04-29T15:39:39.301914Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **64** | plausible_unproven: **198** |
| **low lit**             | novel_discovery: **1**         | speculative: **3** |

Total scored claims: 266

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **183** discrepant claims.

| claim | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---:|---:|---:|---:|---:|---|
| `ARC-001` | active | 0.693 | 0.000 | 0.693 | 0 | 1 | plausible_unproven |
| `ARC-003` | active | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `ARC-005` | active | 0.806 | 0.000 | 0.806 | 0 | 3 | plausible_unproven |
| `ARC-011` | active | 0.783 | 0.000 | 0.783 | 0 | 1 | plausible_unproven |
| `ARC-014` | active | 0.792 | 0.000 | 0.792 | 0 | 3 | plausible_unproven |
| `ARC-022` | provisional | 0.854 | 0.000 | 0.854 | 0 | 7 | plausible_unproven |
| `ARC-023` | candidate | 0.835 | 0.000 | 0.835 | 0 | 5 | plausible_unproven |
| `ARC-028` | candidate | 0.856 | 0.000 | 0.856 | 0 | 7 | plausible_unproven |
| `ARC-035` | candidate | 0.898 | 0.000 | 0.898 | 0 | 13 | plausible_unproven |
| `ARC-039` | candidate | 0.880 | 0.000 | 0.880 | 0 | 5 | plausible_unproven |
| `ARC-045` | candidate | 0.847 | 0.000 | 0.847 | 0 | 3 | plausible_unproven |
| `ARC-048` | candidate | 0.781 | 0.000 | 0.781 | 0 | 2 | plausible_unproven |
| `ARC-051` | candidate | 0.816 | 0.000 | 0.816 | 0 | 2 | plausible_unproven |
| `ARC-058` | candidate | 0.739 | 0.000 | 0.739 | 0 | 4 | plausible_unproven |
| `ARC-060` | candidate | 0.881 | 0.000 | 0.881 | 0 | 6 | plausible_unproven |
| `IMPL-022` | legacy | 0.642 | 0.000 | 0.642 | 0 | 2 | plausible_unproven |
| `INV-014` | active | 0.693 | 0.000 | 0.693 | 0 | 1 | plausible_unproven |
| `INV-034` | candidate | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `INV-043` | candidate | 0.840 | 0.000 | 0.840 | 0 | 7 | plausible_unproven |
| `INV-045` | candidate | 0.655 | 0.000 | 0.655 | 0 | 6 | plausible_unproven |
| `INV-046` | candidate | 0.714 | 0.000 | 0.714 | 0 | 1 | plausible_unproven |
| `INV-047` | candidate | 0.714 | 0.000 | 0.714 | 0 | 1 | plausible_unproven |
| `INV-048` | candidate | 0.870 | 0.000 | 0.870 | 0 | 4 | plausible_unproven |
| `INV-049` | candidate | 0.895 | 0.000 | 0.895 | 0 | 5 | plausible_unproven |
| `INV-050` | candidate | 0.852 | 0.000 | 0.852 | 0 | 3 | plausible_unproven |
| `INV-051` | candidate | 0.736 | 0.000 | 0.736 | 0 | 2 | plausible_unproven |
| `INV-057` | candidate | 0.897 | 0.000 | 0.897 | 0 | 5 | plausible_unproven |
| `MECH-025b` | - | 0.820 | 0.000 | 0.820 | 0 | 4 | plausible_unproven |
| `MECH-030` | provisional | 0.894 | 0.000 | 0.894 | 0 | 4 | plausible_unproven |
| `MECH-040` | provisional | 0.785 | 0.000 | 0.785 | 0 | 2 | plausible_unproven |
| `MECH-046` | provisional | 0.888 | 0.000 | 0.888 | 0 | 4 | plausible_unproven |
| `MECH-053` | provisional | 0.760 | 0.000 | 0.760 | 0 | 2 | plausible_unproven |
| `MECH-054` | provisional | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-057` | candidate | 0.829 | 0.000 | 0.829 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | 0.870 | 0.000 | 0.870 | 0 | 4 | plausible_unproven |
| `MECH-058` | retired | 0.856 | 0.000 | 0.856 | 0 | 9 | plausible_unproven |
| `MECH-062` | stable | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-063` | provisional | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-068` | candidate | 0.693 | 0.000 | 0.693 | 0 | 1 | plausible_unproven |
| `MECH-074` | provisional | 0.891 | 0.000 | 0.891 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | 0.838 | 0.000 | 0.838 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | 0.781 | 0.000 | 0.781 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | 0.836 | 0.000 | 0.836 | 0 | 4 | plausible_unproven |
| `MECH-076` | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-077` | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-092` | candidate | 0.889 | 0.000 | 0.889 | 0 | 16 | plausible_unproven |
| `MECH-094` | stable | 0.866 | 0.000 | 0.866 | 0 | 13 | plausible_unproven |
| `MECH-096` | candidate | 0.808 | 0.000 | 0.808 | 0 | 2 | plausible_unproven |
| `MECH-103` | candidate | 0.844 | 0.000 | 0.844 | 0 | 3 | plausible_unproven |
| `MECH-121` | candidate | 0.872 | 0.000 | 0.872 | 0 | 3 | plausible_unproven |
| `MECH-122` | provisional | 0.897 | 0.000 | 0.897 | 0 | 4 | plausible_unproven |
| `MECH-123` | candidate | 0.858 | 0.000 | 0.858 | 0 | 5 | plausible_unproven |
| `MECH-152` | provisional | 0.718 | 0.000 | 0.718 | 0 | 2 | plausible_unproven |
| `MECH-154` | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-163` | candidate | 0.904 | 0.000 | 0.904 | 0 | 9 | plausible_unproven |
| `MECH-166` | candidate | 0.902 | 0.000 | 0.902 | 0 | 4 | plausible_unproven |
| `MECH-168` | candidate | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-169` | candidate | 0.791 | 0.000 | 0.791 | 0 | 2 | plausible_unproven |
| `MECH-171` | candidate | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-172` | candidate | 0.894 | 0.000 | 0.894 | 0 | 6 | plausible_unproven |
| `MECH-173` | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-174` | candidate | 0.748 | 0.000 | 0.748 | 0 | 2 | plausible_unproven |
| `MECH-175` | candidate | 0.829 | 0.000 | 0.829 | 0 | 3 | plausible_unproven |
| `MECH-176` | candidate | 0.786 | 0.000 | 0.786 | 0 | 2 | plausible_unproven |
| `MECH-177` | candidate | 0.771 | 0.000 | 0.771 | 0 | 2 | plausible_unproven |
| `MECH-178` | candidate | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `MECH-179` | candidate | 0.802 | 0.000 | 0.802 | 0 | 3 | plausible_unproven |
| `MECH-180` | candidate | 0.900 | 0.000 | 0.900 | 0 | 4 | plausible_unproven |
| `MECH-181` | candidate | 0.719 | 0.000 | 0.719 | 0 | 2 | plausible_unproven |
| `MECH-182` | candidate | 0.743 | 0.000 | 0.743 | 0 | 3 | plausible_unproven |
| `MECH-183` | candidate | 0.831 | 0.000 | 0.831 | 0 | 5 | plausible_unproven |
| `MECH-184` | candidate | 0.730 | 0.000 | 0.730 | 0 | 3 | plausible_unproven |
| `MECH-185` | candidate | 0.803 | 0.000 | 0.803 | 0 | 4 | plausible_unproven |
| `MECH-191` | candidate | 0.892 | 0.000 | 0.892 | 0 | 4 | plausible_unproven |
| `MECH-192` | candidate | 0.822 | 0.000 | 0.822 | 0 | 3 | plausible_unproven |
| `MECH-193` | candidate | 0.814 | 0.000 | 0.814 | 0 | 3 | plausible_unproven |
| `MECH-203` | candidate | 0.877 | 0.000 | 0.877 | 0 | 5 | plausible_unproven |
| `MECH-244` | candidate | 0.781 | 0.000 | 0.781 | 0 | 2 | plausible_unproven |
| `MECH-245` | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-257` | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-263` | candidate | 0.913 | 0.000 | 0.913 | 0 | 4 | plausible_unproven |
| `MECH-264` | candidate | 0.873 | 0.000 | 0.873 | 0 | 3 | plausible_unproven |
| `MECH-265` | candidate | 0.917 | 0.000 | 0.917 | 0 | 6 | plausible_unproven |
| `MECH-266` | provisional | 0.853 | 0.000 | 0.853 | 0 | 6 | plausible_unproven |
| `MECH-267` | provisional | 0.896 | 0.000 | 0.896 | 0 | 5 | plausible_unproven |
| `MECH-268` | provisional | 0.850 | 0.000 | 0.850 | 0 | 6 | plausible_unproven |
| `MECH-269` | candidate | 0.877 | 0.000 | 0.877 | 0 | 32 | plausible_unproven |
| `MECH-269b` | - | 0.843 | 0.000 | 0.843 | 0 | 7 | plausible_unproven |
| `MECH-270` | candidate | 0.859 | 0.000 | 0.859 | 0 | 4 | plausible_unproven |
| `MECH-271` | candidate | 0.909 | 0.000 | 0.909 | 0 | 4 | plausible_unproven |
| `MECH-272` | candidate | 0.884 | 0.000 | 0.884 | 0 | 14 | plausible_unproven |
| `MECH-273` | candidate | 0.882 | 0.000 | 0.882 | 0 | 4 | plausible_unproven |
| `MECH-275` | candidate | 0.866 | 0.000 | 0.866 | 0 | 6 | plausible_unproven |
| `MECH-279` | candidate | 0.907 | 0.000 | 0.907 | 0 | 5 | plausible_unproven |
| `MECH-280` | candidate | 0.877 | 0.000 | 0.877 | 0 | 5 | plausible_unproven |
| `MECH-281` | candidate | 0.877 | 0.000 | 0.877 | 0 | 4 | plausible_unproven |
| `MECH-284` | candidate | 0.852 | 0.000 | 0.852 | 0 | 14 | plausible_unproven |
| `MECH-285` | candidate | 0.879 | 0.000 | 0.879 | 0 | 16 | plausible_unproven |
| `MECH-287` | candidate | 0.881 | 0.000 | 0.881 | 0 | 5 | plausible_unproven |
| `MECH-288` | candidate | 0.895 | 0.000 | 0.895 | 0 | 11 | plausible_unproven |
| `MECH-291` | candidate | 0.679 | 0.000 | 0.679 | 0 | 1 | plausible_unproven |
| `MECH-292` | candidate | 0.905 | 0.000 | 0.905 | 0 | 13 | plausible_unproven |
| `MECH-293` | candidate | 0.896 | 0.000 | 0.896 | 0 | 7 | plausible_unproven |
| `MECH-294` | candidate | 0.880 | 0.000 | 0.880 | 0 | 9 | plausible_unproven |
| `MECH-295` | candidate | 0.882 | 0.000 | 0.882 | 0 | 6 | plausible_unproven |
| `MECH-900` | - | 0.700 | 0.000 | 0.700 | 0 | 1 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | 0.814 | 0.000 | 0.814 | 0 | 5 | plausible_unproven |
| `Q-005` | active | 0.809 | 0.000 | 0.809 | 0 | 4 | plausible_unproven |
| `Q-011` | legacy | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `Q-013` | legacy | 0.830 | 0.000 | 0.830 | 0 | 4 | plausible_unproven |
| `Q-014` | legacy | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `Q-015` | active | 0.840 | 0.000 | 0.840 | 0 | 5 | plausible_unproven |
| `Q-016` | active | 0.858 | 0.000 | 0.858 | 0 | 5 | plausible_unproven |
| `Q-017` | active | 0.867 | 0.000 | 0.867 | 0 | 11 | plausible_unproven |
| `Q-019` | open | 0.886 | 0.000 | 0.886 | 0 | 16 | plausible_unproven |
| `Q-020` | resolved | 0.783 | 0.000 | 0.783 | 0 | 6 | plausible_unproven |
| `Q-023` | open | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `Q-024` | open | 0.792 | 0.000 | 0.792 | 0 | 3 | plausible_unproven |
| `Q-025` | open | 0.632 | 0.000 | 0.632 | 0 | 2 | plausible_unproven |
| `Q-027` | open | 0.663 | 0.000 | 0.663 | 0 | 3 | plausible_unproven |
| `Q-028` | open | 0.625 | 0.000 | 0.625 | 0 | 2 | plausible_unproven |
| `Q-029` | open | 0.875 | 0.000 | 0.875 | 0 | 5 | plausible_unproven |
| `Q-030` | open | 0.874 | 0.000 | 0.874 | 0 | 5 | plausible_unproven |
| `Q-031` | open | 0.870 | 0.000 | 0.870 | 0 | 5 | plausible_unproven |
| `Q-032` | open | 0.839 | 0.000 | 0.839 | 0 | 5 | plausible_unproven |
| `Q-033` | open | 0.827 | 0.000 | 0.827 | 0 | 4 | plausible_unproven |
| `Q-036` | open | 0.809 | 0.000 | 0.809 | 0 | 3 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | 0.869 | 0.000 | 0.869 | 0 | 4 | plausible_unproven |
| `SD-009` | provisional | 0.752 | 0.000 | 0.752 | 0 | 2 | plausible_unproven |
| `SD-014` | candidate | 0.903 | 0.000 | 0.903 | 0 | 4 | plausible_unproven |
| `SD-017` | stable | 0.902 | 0.000 | 0.902 | 0 | 6 | plausible_unproven |
| `SD-032d` | - | 0.866 | 0.000 | 0.866 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | 0.910 | 0.000 | 0.910 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | 0.898 | 0.000 | 0.898 | 0 | 10 | plausible_unproven |
| `SD-034` | provisional | 0.855 | 0.000 | 0.855 | 0 | 6 | plausible_unproven |
| `SD-035` | stable | 0.827 | 0.000 | 0.827 | 0 | 3 | plausible_unproven |
| `SD-036` | candidate | 0.831 | 0.000 | 0.831 | 0 | 2 | plausible_unproven |
| `SD-037` | candidate | 0.870 | 0.000 | 0.870 | 0 | 4 | plausible_unproven |
| `SD-039` | candidate | 0.842 | 0.000 | 0.842 | 0 | 3 | plausible_unproven |
| `SD-040` | candidate | 0.760 | 0.000 | 0.760 | 0 | 1 | plausible_unproven |
| `Q-001` | active | 0.664 | 0.255 | 0.801 | 1 | 4 | plausible_unproven |
| `Q-007` | active | 0.633 | 0.266 | 0.756 | 1 | 3 | plausible_unproven |
| `MECH-165` | candidate | 0.690 | 0.271 | 0.830 | 1 | 3 | plausible_unproven |
| `MECH-188` | candidate | 0.677 | 0.276 | 0.810 | 1 | 3 | plausible_unproven |
| `SD-023` | candidate | 0.730 | 0.300 | 0.873 | 1 | 4 | plausible_unproven |
| `MECH-220` | candidate | 0.729 | 0.301 | 0.872 | 1 | 4 | plausible_unproven |
| `INV-010` | active | 0.730 | 0.302 | 0.873 | 1 | 3 | plausible_unproven |
| `MECH-091` | candidate | 0.718 | 0.306 | 0.855 | 1 | 6 | plausible_unproven |
| `SD-032c` | - | 0.678 | 0.306 | 0.802 | 1 | 3 | plausible_unproven |
| `Q-040` | open | 0.711 | 0.324 | 0.840 | 1 | 4 | plausible_unproven |
| `MECH-120` | candidate | 0.670 | 0.326 | 0.899 | 2 | 7 | plausible_unproven |
| `MECH-155` | candidate | 0.658 | 0.328 | 0.878 | 2 | 5 | plausible_unproven |
| `ARC-038` | candidate | 0.682 | 0.351 | 0.902 | 2 | 5 | plausible_unproven |
| `INV-029` | active | 0.694 | 0.387 | 0.796 | 1 | 3 | plausible_unproven |
| `MECH-047` | provisional | 0.752 | 0.391 | 0.872 | 1 | 4 | plausible_unproven |
| `ARC-032` | candidate | 0.636 | 0.404 | 0.867 | 4 | 8 | plausible_unproven |
| `MECH-116` | candidate | 0.640 | 0.404 | 0.876 | 4 | 7 | plausible_unproven |
| `SD-021` | candidate | 0.651 | 0.406 | 0.896 | 3 | 8 | plausible_unproven |
| `MECH-026` | provisional | 0.757 | 0.416 | 0.871 | 1 | 6 | plausible_unproven |
| `MECH-029` | provisional | 0.760 | 0.416 | 0.875 | 1 | 6 | plausible_unproven |
| `MECH-022` | provisional | 0.762 | 0.418 | 0.877 | 1 | 5 | plausible_unproven |
| `MECH-025` | candidate | 0.760 | 0.420 | 0.873 | 1 | 5 | plausible_unproven |
| `Q-012` | candidate | 0.748 | 0.424 | 0.856 | 1 | 5 | plausible_unproven |
| `Q-002` | active | 0.630 | 0.438 | 0.823 | 4 | 4 | plausible_unproven |
| `MECH-153` | candidate | 0.646 | 0.439 | 0.854 | 4 | 7 | plausible_unproven |
| `MECH-099` | candidate | 0.673 | 0.443 | 0.903 | 6 | 7 | plausible_unproven |
| `Q-004` | active | 0.718 | 0.455 | 0.805 | 1 | 4 | plausible_unproven |
| `Q-006` | active | 0.667 | 0.455 | 0.738 | 1 | 3 | plausible_unproven |
| `ARC-017` | provisional | 0.638 | 0.460 | 0.816 | 2 | 2 | plausible_unproven |
| `SD-029` | candidate | 0.662 | 0.462 | 0.862 | 4 | 9 | plausible_unproven |
| `Q-021` | open | 0.668 | 0.469 | 0.800 | 2 | 3 | plausible_unproven |
| `MECH-075` | candidate | 0.684 | 0.486 | 0.882 | 5 | 6 | plausible_unproven |
| `ARC-036` | candidate | 0.747 | 0.505 | 0.908 | 2 | 4 | plausible_unproven |
| `ARC-029` | provisional | 0.670 | 0.518 | 0.823 | 3 | 6 | plausible_unproven |
| `MECH-095` | active | 0.717 | 0.533 | 0.901 | 9 | 7 | plausible_unproven |
| `MECH-102` | active | 0.696 | 0.540 | 0.851 | 24 | 9 | plausible_unproven |
| `MECH-118` | candidate | 0.683 | 0.553 | 0.813 | 4 | 3 | plausible_unproven |
| `MECH-216` | provisional | 0.743 | 0.565 | 0.861 | 2 | 4 | plausible_unproven |
| `MECH-113` | candidate | 0.703 | 0.569 | 0.837 | 4 | 3 | plausible_unproven |
| `ARC-030` | candidate | 0.739 | 0.572 | 0.907 | 7 | 9 | plausible_unproven |
| `ARC-026` | candidate | 0.696 | 0.588 | 0.803 | 3 | 5 | plausible_unproven |
| `SD-004` | implemented | 0.757 | 0.612 | 0.903 | 8 | 14 | plausible_unproven |

## Implementation-cohort claims with zero experimental backing

These claims have status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2.

Total: **15** implementation-cohort claims with no exp.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `SD-017` | stable | 0.902 | 6 |
| `Q-017` | active | 0.867 | 11 |
| `MECH-094` | stable | 0.866 | 13 |
| `Q-016` | active | 0.858 | 5 |
| `Q-015` | active | 0.840 | 5 |
| `SD-035` | stable | 0.827 | 3 |
| `Q-005` | active | 0.809 | 4 |
| `ARC-003` | active | 0.806 | 3 |
| `ARC-005` | active | 0.806 | 3 |
| `ARC-014` | active | 0.792 | 3 |
| `ARC-011` | active | 0.783 | 1 |
| `Q-020` | resolved | 0.783 | 6 |
| `MECH-062` | stable | 0.780 | 2 |
| `ARC-001` | active | 0.693 | 1 |
| `INV-014` | active | 0.693 | 1 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.730 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **50**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `Q-001` | active | 0.255 | 1 |
| `Q-007` | active | 0.266 | 1 |
| `MECH-165` | candidate | 0.271 | 1 |
| `SD-018` | implemented | 0.274 | 1 |
| `MECH-188` | candidate | 0.276 | 1 |
| `ARC-041` | candidate | 0.298 | 2 |
| `MECH-150` | candidate | 0.298 | 2 |
| `SD-023` | candidate | 0.300 | 1 |
| `MECH-220` | candidate | 0.301 | 1 |
| `INV-010` | active | 0.302 | 1 |
| `MECH-091` | candidate | 0.306 | 1 |
| `Q-003` | active | 0.306 | 2 |
| `SD-032c` | - | 0.306 | 1 |
| `Q-040` | open | 0.324 | 1 |
| `MECH-186` | candidate | 0.325 | 2 |
| `MECH-120` | candidate | 0.326 | 2 |
| `MECH-155` | candidate | 0.328 | 2 |
| `MECH-111` | candidate | 0.347 | 3 |
| `ARC-038` | candidate | 0.351 | 2 |
| `MECH-128` | candidate | 0.361 | 3 |
| `INV-029` | active | 0.387 | 1 |
| `MECH-047` | provisional | 0.391 | 1 |
| `ARC-042` | candidate | 0.394 | 3 |
| `ARC-032` | candidate | 0.404 | 4 |
| `INV-054` | candidate | 0.404 | 3 |
| `MECH-116` | candidate | 0.404 | 4 |
| `SD-021` | candidate | 0.406 | 3 |
| `MECH-026` | provisional | 0.416 | 1 |
| `MECH-029` | provisional | 0.416 | 1 |
| `MECH-022` | provisional | 0.418 | 1 |
| ... | ... | ... | ... (20 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **142**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-265` | candidate | 0.917 | 6 |
| `MECH-263` | candidate | 0.913 | 4 |
| `SD-033b` | - | 0.910 | 5 |
| `MECH-271` | candidate | 0.909 | 4 |
| `MECH-279` | candidate | 0.907 | 5 |
| `MECH-292` | candidate | 0.905 | 13 |
| `MECH-163` | candidate | 0.904 | 9 |
| `SD-014` | candidate | 0.903 | 4 |
| `MECH-166` | candidate | 0.902 | 4 |
| `SD-017` | stable | 0.902 | 6 |
| `MECH-180` | candidate | 0.900 | 4 |
| `ARC-035` | candidate | 0.898 | 13 |
| `SD-033e` | - | 0.898 | 10 |
| `INV-057` | candidate | 0.897 | 5 |
| `MECH-122` | provisional | 0.897 | 4 |
| `MECH-267` | provisional | 0.896 | 5 |
| `MECH-293` | candidate | 0.896 | 7 |
| `INV-049` | candidate | 0.895 | 5 |
| `MECH-288` | candidate | 0.895 | 11 |
| `MECH-030` | provisional | 0.894 | 4 |
| `MECH-172` | candidate | 0.894 | 6 |
| `MECH-191` | candidate | 0.892 | 4 |
| `MECH-074` | provisional | 0.891 | 9 |
| `MECH-092` | candidate | 0.889 | 16 |
| `MECH-046` | provisional | 0.888 | 4 |
| `Q-019` | open | 0.886 | 16 |
| `MECH-272` | candidate | 0.884 | 14 |
| `MECH-171` | candidate | 0.882 | 4 |
| `MECH-273` | candidate | 0.882 | 4 |
| `MECH-295` | candidate | 0.882 | 6 |
| `ARC-060` | candidate | 0.881 | 6 |
| `MECH-287` | candidate | 0.881 | 5 |
| `ARC-039` | candidate | 0.880 | 5 |
| `MECH-294` | candidate | 0.880 | 9 |
| `MECH-285` | candidate | 0.879 | 16 |
| `MECH-168` | candidate | 0.877 | 4 |
| `MECH-203` | candidate | 0.877 | 5 |
| `MECH-269` | candidate | 0.877 | 32 |
| `MECH-280` | candidate | 0.877 | 5 |
| `MECH-281` | candidate | 0.877 | 4 |
| `Q-029` | open | 0.875 | 5 |
| `Q-030` | open | 0.874 | 5 |
| `MECH-264` | candidate | 0.873 | 3 |
| `MECH-121` | candidate | 0.872 | 3 |
| `INV-048` | candidate | 0.870 | 4 |
| `MECH-057b` | - | 0.870 | 4 |
| `Q-031` | open | 0.870 | 5 |
| `SD-037` | candidate | 0.870 | 4 |
| `SD-003-SUCCESSOR` | - | 0.869 | 4 |
| `Q-017` | active | 0.867 | 11 |
| ... | ... | ... | ... (92 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
