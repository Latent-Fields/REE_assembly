# Aggregator b_strict (multiplicative lit_conf) -- staging diff

Coefficients: floor=0.7, consistency=0.15, volume=0.1, recency=0.05 (multiplier range: [0.70, 1.00])

Compares production claim_evidence.v1.json against rescored output using the multiplicative lit_conf aggregator. exp_conf and overall blending logic are unchanged.

## Summary

- claims rescored: **263** (262 with literature evidence)
- avg lit_conf delta (lit-bearing claims): **-0.104**
- avg overall_confidence delta (all claims): **-0.083**
- claims with lit_conf drop > 0.05: **227**
- claims with lit_conf drop > 0.10: **149**
- claims with lit_conf rise > 0.05: **0**

## Top 25 lit_conf drops

| claim | n_lit | lit_prod | lit_new | delta | overall_prod | overall_new | quality | mult |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Q-027` | 3 | 0.663 | 0.416 | **-0.247** | 0.663 | 0.416 | 0.427 | 0.975 |
| `Q-026` | 2 | 0.617 | 0.413 | **-0.204** | 0.617 | 0.413 | 0.435 | 0.950 |
| `Q-028` | 2 | 0.625 | 0.427 | **-0.198** | 0.625 | 0.427 | 0.450 | 0.950 |
| `Q-034` | 6 | 0.799 | 0.607 | **-0.192** | 0.740 | 0.644 | 0.608 | 0.997 |
| `ARC-026` | 5 | 0.803 | 0.613 | **-0.190** | 0.696 | 0.601 | 0.614 | 0.998 |
| `Q-025` | 2 | 0.632 | 0.442 | **-0.190** | 0.632 | 0.442 | 0.465 | 0.950 |
| `Q-001` | 4 | 0.802 | 0.617 | **-0.185** | 0.665 | 0.527 | 0.620 | 0.996 |
| `MECH-185` | 4 | 0.803 | 0.618 | **-0.185** | 0.803 | 0.618 | 0.620 | 0.997 |
| `INV-053` | 5 | 0.811 | 0.627 | **-0.184** | 0.883 | 0.791 | 0.628 | 0.999 |
| `MECH-E2-DUAL-FUNCTION` | 5 | 0.814 | 0.633 | **-0.181** | 0.814 | 0.633 | 0.634 | 0.999 |
| `Q-004` | 4 | 0.805 | 0.625 | **-0.180** | 0.718 | 0.583 | 0.628 | 0.996 |
| `MECH-025b` | 4 | 0.820 | 0.640 | **-0.180** | 0.820 | 0.640 | 0.640 | 1.000 |
| `MECH-072` | 6 | 0.815 | 0.637 | **-0.178** | 0.857 | 0.768 | 0.638 | 0.998 |
| `Q-005` | 4 | 0.809 | 0.632 | **-0.177** | 0.809 | 0.632 | 0.635 | 0.996 |
| `Q-003` | 4 | 0.813 | 0.640 | **-0.173** | 0.611 | 0.507 | 0.642 | 0.996 |
| `MECH-184` | 3 | 0.730 | 0.557 | **-0.173** | 0.730 | 0.557 | 0.573 | 0.972 |
| `INV-045` | 6 | 0.655 | 0.482 | **-0.173** | 0.655 | 0.482 | 0.523 | 0.922 |
| `MECH-059` | 11 | 0.820 | 0.651 | **-0.169** | 0.783 | 0.657 | 0.653 | 0.997 |
| `MECH-093` | 4 | 0.822 | 0.653 | **-0.169** | 0.757 | 0.673 | 0.655 | 0.997 |
| `SD-032e` | 4 | 0.829 | 0.662 | **-0.167** | 0.829 | 0.662 | 0.662 | 0.999 |
| `ARC-029` | 6 | 0.823 | 0.658 | **-0.165** | 0.671 | 0.589 | 0.660 | 0.997 |
| `Q-002` | 4 | 0.823 | 0.660 | **-0.163** | 0.631 | 0.549 | 0.662 | 0.996 |
| `Q-006` | 3 | 0.738 | 0.576 | **-0.162** | 0.667 | 0.546 | 0.593 | 0.971 |
| `Q-033` | 4 | 0.827 | 0.665 | **-0.162** | 0.827 | 0.665 | 0.667 | 0.997 |
| `MECH-182` | 3 | 0.744 | 0.583 | **-0.161** | 0.744 | 0.583 | 0.600 | 0.972 |

## Top 10 lit_conf rises (sanity check -- expect few/none)

| claim | n_lit | lit_prod | lit_new | delta |
|---|---:|---:|---:|---:|
| `MECH-156` | 1 | 0.783 | 0.811 | +0.028 |
| `ARC-011` | 1 | 0.783 | 0.811 | +0.028 |

## Promotion-tier impact

Claims that cross typical confidence thresholds (0.50 candidate, 0.65 provisional, 0.80 stable) based on **overall_confidence** under the new aggregator.

| claim | prod tier | new tier | overall_prod | overall_new |
|---|---|---|---:|---:|
| `Q-027` | provisional | below_candidate | 0.663 | 0.416 |
| `Q-026` | candidate | below_candidate | 0.617 | 0.413 |
| `Q-028` | candidate | below_candidate | 0.625 | 0.427 |
| `Q-025` | candidate | below_candidate | 0.632 | 0.442 |
| `MECH-185` | stable | candidate | 0.803 | 0.618 |
| `MECH-E2-DUAL-FUNCTION` | stable | candidate | 0.814 | 0.633 |
| `MECH-025b` | stable | candidate | 0.820 | 0.640 |
| `Q-005` | stable | candidate | 0.809 | 0.632 |
| `INV-045` | provisional | below_candidate | 0.655 | 0.482 |
| `MECH-184` | provisional | candidate | 0.730 | 0.557 |
| `SD-032e` | stable | provisional | 0.829 | 0.662 |
| `Q-033` | stable | provisional | 0.827 | 0.665 |
| `MECH-182` | provisional | candidate | 0.744 | 0.583 |
| `MECH-074d` | stable | provisional | 0.836 | 0.675 |
| `INV-043` | stable | provisional | 0.841 | 0.681 |
| `Q-040` | stable | provisional | 0.840 | 0.680 |
| `MECH-183` | stable | provisional | 0.832 | 0.674 |
| `MECH-269b` | stable | provisional | 0.843 | 0.688 |
| `Q-013` | stable | provisional | 0.830 | 0.675 |
| `ARC-023` | stable | provisional | 0.835 | 0.680 |
| `Q-014` | stable | provisional | 0.833 | 0.680 |
| `MECH-268` | stable | provisional | 0.850 | 0.702 |
| `Q-015` | stable | provisional | 0.840 | 0.693 |
| `MECH-266` | stable | provisional | 0.853 | 0.707 |
| `MECH-284` | stable | provisional | 0.852 | 0.708 |
| `SD-034` | stable | provisional | 0.855 | 0.712 |
| `ARC-028` | stable | provisional | 0.856 | 0.714 |
| `MECH-270` | stable | provisional | 0.859 | 0.720 |
| `Q-001` | provisional | candidate | 0.665 | 0.527 |
| `MECH-057` | stable | provisional | 0.829 | 0.692 |
| `Q-004` | provisional | candidate | 0.718 | 0.583 |
| `Q-011` | stable | provisional | 0.833 | 0.698 |
| `ARC-022` | stable | provisional | 0.854 | 0.719 |
| `MECH-275` | stable | provisional | 0.866 | 0.733 |
| `MECH-094` | stable | provisional | 0.866 | 0.735 |
| `MECH-123` | stable | provisional | 0.859 | 0.728 |
| `SD-037` | stable | provisional | 0.870 | 0.740 |
| `MECH-057b` | stable | provisional | 0.870 | 0.740 |
| `Q-031` | stable | provisional | 0.870 | 0.740 |
| `SD-032d` | stable | provisional | 0.866 | 0.737 |
| `Q-016` | stable | provisional | 0.859 | 0.731 |
| `SD-003-SUCCESSOR` | stable | provisional | 0.870 | 0.744 |
| `MECH-269` | stable | provisional | 0.877 | 0.755 |
| `MECH-281` | stable | provisional | 0.877 | 0.755 |
| `Q-006` | provisional | candidate | 0.667 | 0.546 |
| `MECH-280` | stable | provisional | 0.877 | 0.756 |
| `INV-048` | stable | provisional | 0.870 | 0.750 |
| `MECH-285` | stable | provisional | 0.879 | 0.759 |
| `Q-017` | stable | provisional | 0.868 | 0.749 |
| `MECH-294` | stable | provisional | 0.880 | 0.761 |
| `MECH-273` | stable | provisional | 0.882 | 0.765 |
| `ARC-060` | stable | provisional | 0.882 | 0.765 |
| `MECH-295` | stable | provisional | 0.883 | 0.766 |
| `MECH-272` | stable | provisional | 0.884 | 0.768 |
| `MECH-287` | stable | provisional | 0.881 | 0.765 |
| `ARC-039` | stable | provisional | 0.880 | 0.765 |
| `MECH-203` | stable | provisional | 0.877 | 0.762 |
| `Q-019` | stable | provisional | 0.886 | 0.773 |
| `MECH-168` | stable | provisional | 0.877 | 0.765 |
| `MECH-058` | stable | provisional | 0.856 | 0.745 |
| `MECH-046` | stable | provisional | 0.888 | 0.779 |
| `MECH-092` | stable | provisional | 0.889 | 0.780 |
| `MECH-060` | stable | provisional | 0.803 | 0.696 |
| `MECH-171` | stable | provisional | 0.882 | 0.775 |
| `MECH-178` | stable | provisional | 0.802 | 0.696 |
| `MECH-179` | stable | provisional | 0.802 | 0.696 |
| `MECH-091` | provisional | candidate | 0.718 | 0.612 |
| `MECH-172` | stable | provisional | 0.894 | 0.788 |
| `Q-036` | stable | provisional | 0.809 | 0.704 |
| `MECH-074` | stable | provisional | 0.891 | 0.786 |
| `MECH-181` | provisional | candidate | 0.719 | 0.615 |
| `MECH-267` | stable | provisional | 0.896 | 0.792 |
| `MECH-187` | stable | provisional | 0.829 | 0.726 |
| `MECH-152` | provisional | candidate | 0.718 | 0.615 |
| `MECH-293` | stable | provisional | 0.896 | 0.793 |
| `Q-023` | stable | provisional | 0.803 | 0.702 |
| `MECH-230` | stable | provisional | 0.834 | 0.733 |
| `ARC-035` | stable | provisional | 0.899 | 0.798 |
| `SD-033e` | stable | provisional | 0.899 | 0.798 |
| `MECH-288` | stable | provisional | 0.895 | 0.794 |
| `MECH-061` | stable | provisional | 0.810 | 0.710 |
| `MECH-057a` | stable | provisional | 0.809 | 0.709 |
| `MECH-122` | stable | provisional | 0.897 | 0.797 |
| `INV-049` | stable | provisional | 0.895 | 0.795 |
| `MECH-191` | stable | provisional | 0.892 | 0.795 |
| `Q-034` | provisional | candidate | 0.740 | 0.644 |
| `ARC-026` | provisional | candidate | 0.696 | 0.601 |
| `MECH-193` | stable | provisional | 0.814 | 0.719 |
| `INV-053` | stable | provisional | 0.883 | 0.791 |
| `SD-023` | provisional | candidate | 0.730 | 0.639 |
| `MECH-056` | stable | provisional | 0.821 | 0.731 |
| `MECH-220` | provisional | candidate | 0.730 | 0.640 |
| `SD-035` | stable | provisional | 0.827 | 0.737 |
| `MECH-072` | stable | provisional | 0.857 | 0.768 |
| `MECH-192` | stable | provisional | 0.822 | 0.735 |
| `INV-051` | provisional | candidate | 0.736 | 0.649 |
| `SD-032c` | provisional | candidate | 0.678 | 0.593 |
| `ARC-003` | stable | provisional | 0.806 | 0.722 |
| `ARC-005` | stable | provisional | 0.806 | 0.722 |
| `ARC-029` | provisional | candidate | 0.671 | 0.589 |
| `INV-029` | provisional | candidate | 0.695 | 0.614 |
| `MECH-175` | stable | provisional | 0.829 | 0.748 |
| `SD-032a` | stable | provisional | 0.857 | 0.777 |
| `MECH-135` | stable | provisional | 0.803 | 0.725 |
| `MECH-124` | stable | provisional | 0.846 | 0.768 |
| `MECH-074a` | stable | provisional | 0.838 | 0.760 |
| `SD-039` | stable | provisional | 0.843 | 0.767 |
| `MECH-205` | stable | provisional | 0.832 | 0.757 |
| `MECH-102` | provisional | candidate | 0.696 | 0.622 |
| `MECH-188` | provisional | candidate | 0.677 | 0.604 |
| `MECH-106` | stable | provisional | 0.826 | 0.754 |
| `MECH-155` | provisional | candidate | 0.658 | 0.589 |
| `MECH-291` | provisional | candidate | 0.679 | 0.610 |
| `SD-029` | provisional | candidate | 0.662 | 0.594 |
| `INV-052` | stable | provisional | 0.847 | 0.784 |
| `ARC-045` | stable | provisional | 0.847 | 0.784 |
| `Q-021` | provisional | candidate | 0.668 | 0.606 |
| `MECH-256` | stable | provisional | 0.823 | 0.761 |
| `SD-013` | stable | provisional | 0.826 | 0.764 |
| `ARC-021` | stable | provisional | 0.823 | 0.761 |
| `ARC-033` | stable | provisional | 0.809 | 0.750 |
| `MECH-103` | stable | provisional | 0.844 | 0.785 |
| `INV-044` | stable | provisional | 0.856 | 0.798 |
| `MECH-165` | provisional | candidate | 0.690 | 0.632 |
| `INV-050` | stable | provisional | 0.852 | 0.794 |
| `MECH-075` | provisional | candidate | 0.684 | 0.628 |
| `MECH-120` | provisional | candidate | 0.670 | 0.616 |
| `SD-007` | stable | provisional | 0.817 | 0.764 |
| `MECH-071` | stable | provisional | 0.828 | 0.775 |
| `MECH-119` | stable | provisional | 0.825 | 0.772 |
| `ARC-038` | provisional | candidate | 0.682 | 0.630 |
| `SD-021` | provisional | candidate | 0.651 | 0.602 |
| `MECH-112` | stable | provisional | 0.843 | 0.796 |
| `MECH-118` | provisional | candidate | 0.683 | 0.638 |
| `MECH-099` | provisional | candidate | 0.674 | 0.630 |
| `ARC-041` | candidate | below_candidate | 0.517 | 0.474 |
| `MECH-150` | candidate | below_candidate | 0.521 | 0.481 |
| `SD-010` | stable | provisional | 0.837 | 0.799 |
| `MECH-111` | candidate | below_candidate | 0.516 | 0.492 |
| `ARC-051` | stable | provisional | 0.817 | 0.793 |
| `SD-006` | stable | provisional | 0.815 | 0.798 |
| `MECH-096` | stable | provisional | 0.808 | 0.793 |
| `MECH-229` | stable | provisional | 0.801 | 0.791 |
| `ARC-011` | provisional | stable | 0.783 | 0.811 |

---

Source snapshot: `claim_evidence.v1.production_snapshot.json`
Staging matrix: `claim_evidence.v1.staging_b_strict.json`
