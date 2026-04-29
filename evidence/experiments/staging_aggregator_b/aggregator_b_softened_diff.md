# Aggregator b_softened (multiplicative lit_conf) -- staging diff

Coefficients: floor=0.85, consistency=0.1, volume=0.03, recency=0.02 (multiplier range: [0.85, 1.00])

Compares production claim_evidence.v1.json against rescored output using the multiplicative lit_conf aggregator. exp_conf and overall blending logic are unchanged.

## Summary

- claims rescored: **263** (262 with literature evidence)
- avg lit_conf delta (lit-bearing claims): **-0.093**
- avg overall_confidence delta (all claims): **-0.074**
- claims with lit_conf drop > 0.05: **209**
- claims with lit_conf drop > 0.10: **136**
- claims with lit_conf rise > 0.05: **2**

## Top 25 lit_conf drops

| claim | n_lit | lit_prod | lit_new | delta | overall_prod | overall_new | quality | mult |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Q-027` | 3 | 0.663 | 0.423 | **-0.240** | 0.663 | 0.423 | 0.427 | 0.992 |
| `Q-034` | 6 | 0.799 | 0.608 | **-0.191** | 0.740 | 0.644 | 0.608 | 0.999 |
| `ARC-026` | 5 | 0.803 | 0.613 | **-0.190** | 0.696 | 0.601 | 0.614 | 0.999 |
| `Q-026` | 2 | 0.617 | 0.428 | **-0.189** | 0.617 | 0.428 | 0.435 | 0.985 |
| `MECH-185` | 4 | 0.803 | 0.619 | **-0.184** | 0.803 | 0.619 | 0.620 | 0.999 |
| `Q-001` | 4 | 0.802 | 0.619 | **-0.183** | 0.665 | 0.528 | 0.620 | 0.998 |
| `INV-053` | 5 | 0.811 | 0.628 | **-0.183** | 0.883 | 0.791 | 0.628 | 0.999 |
| `Q-028` | 2 | 0.625 | 0.443 | **-0.182** | 0.625 | 0.443 | 0.450 | 0.985 |
| `MECH-025b` | 4 | 0.820 | 0.640 | **-0.180** | 0.820 | 0.640 | 0.640 | 1.000 |
| `MECH-E2-DUAL-FUNCTION` | 5 | 0.814 | 0.634 | **-0.180** | 0.814 | 0.634 | 0.634 | 0.999 |
| `Q-004` | 4 | 0.805 | 0.626 | **-0.179** | 0.718 | 0.584 | 0.628 | 0.998 |
| `MECH-072` | 6 | 0.815 | 0.638 | **-0.177** | 0.857 | 0.769 | 0.638 | 0.999 |
| `Q-005` | 4 | 0.809 | 0.634 | **-0.175** | 0.809 | 0.634 | 0.635 | 0.998 |
| `Q-025` | 2 | 0.632 | 0.458 | **-0.174** | 0.632 | 0.458 | 0.465 | 0.985 |
| `Q-003` | 4 | 0.813 | 0.641 | **-0.172** | 0.611 | 0.507 | 0.642 | 0.998 |
| `MECH-059` | 11 | 0.820 | 0.652 | **-0.168** | 0.783 | 0.657 | 0.653 | 0.999 |
| `MECH-093` | 4 | 0.822 | 0.654 | **-0.168** | 0.757 | 0.674 | 0.655 | 0.999 |
| `SD-032e` | 4 | 0.829 | 0.662 | **-0.167** | 0.829 | 0.662 | 0.662 | 0.999 |
| `ARC-029` | 6 | 0.823 | 0.659 | **-0.164** | 0.671 | 0.589 | 0.660 | 0.999 |
| `Q-002` | 4 | 0.823 | 0.661 | **-0.162** | 0.631 | 0.550 | 0.662 | 0.998 |
| `MECH-184` | 3 | 0.730 | 0.568 | **-0.162** | 0.730 | 0.568 | 0.573 | 0.991 |
| `MECH-074d` | 4 | 0.836 | 0.675 | **-0.161** | 0.836 | 0.675 | 0.675 | 1.000 |
| `INV-043` | 7 | 0.841 | 0.681 | **-0.160** | 0.841 | 0.681 | 0.681 | 1.000 |
| `Q-033` | 4 | 0.827 | 0.667 | **-0.160** | 0.827 | 0.667 | 0.667 | 0.999 |
| `Q-040` | 4 | 0.840 | 0.680 | **-0.160** | 0.840 | 0.680 | 0.680 | 1.000 |

## Top 10 lit_conf rises (sanity check -- expect few/none)

| claim | n_lit | lit_prod | lit_new | delta |
|---|---:|---:|---:|---:|
| `MECH-156` | 1 | 0.783 | 0.859 | +0.076 |
| `ARC-011` | 1 | 0.783 | 0.859 | +0.076 |
| `SD-040` | 1 | 0.760 | 0.802 | +0.042 |
| `IMPL-022` | 2 | 0.642 | 0.675 | +0.033 |
| `ARC-017` | 2 | 0.816 | 0.840 | +0.024 |
| `SD-036` | 2 | 0.831 | 0.852 | +0.021 |
| `MECH-900` | 1 | 0.700 | 0.720 | +0.020 |
| `MECH-096` | 2 | 0.808 | 0.825 | +0.017 |
| `MECH-073` | 5 | 0.682 | 0.699 | +0.017 |
| `MECH-040` | 2 | 0.785 | 0.795 | +0.010 |

## Promotion-tier impact

Claims that cross typical confidence thresholds (0.50 candidate, 0.65 provisional, 0.80 stable) based on **overall_confidence** under the new aggregator.

| claim | prod tier | new tier | overall_prod | overall_new |
|---|---|---|---:|---:|
| `Q-027` | provisional | below_candidate | 0.663 | 0.423 |
| `Q-026` | candidate | below_candidate | 0.617 | 0.428 |
| `MECH-185` | stable | candidate | 0.803 | 0.619 |
| `Q-028` | candidate | below_candidate | 0.625 | 0.443 |
| `MECH-025b` | stable | candidate | 0.820 | 0.640 |
| `MECH-E2-DUAL-FUNCTION` | stable | candidate | 0.814 | 0.634 |
| `Q-005` | stable | candidate | 0.809 | 0.634 |
| `Q-025` | candidate | below_candidate | 0.632 | 0.458 |
| `SD-032e` | stable | provisional | 0.829 | 0.662 |
| `MECH-184` | provisional | candidate | 0.730 | 0.568 |
| `MECH-074d` | stable | provisional | 0.836 | 0.675 |
| `INV-043` | stable | provisional | 0.841 | 0.681 |
| `Q-033` | stable | provisional | 0.827 | 0.667 |
| `Q-040` | stable | provisional | 0.840 | 0.680 |
| `INV-045` | provisional | below_candidate | 0.655 | 0.496 |
| `MECH-183` | stable | provisional | 0.832 | 0.675 |
| `MECH-269b` | stable | provisional | 0.843 | 0.688 |
| `Q-013` | stable | provisional | 0.830 | 0.676 |
| `ARC-023` | stable | provisional | 0.835 | 0.681 |
| `Q-014` | stable | provisional | 0.833 | 0.681 |
| `MECH-182` | provisional | candidate | 0.744 | 0.595 |
| `MECH-268` | stable | provisional | 0.850 | 0.702 |
| `MECH-266` | stable | provisional | 0.853 | 0.707 |
| `Q-015` | stable | provisional | 0.840 | 0.695 |
| `MECH-284` | stable | provisional | 0.852 | 0.708 |
| `SD-034` | stable | provisional | 0.855 | 0.712 |
| `ARC-028` | stable | provisional | 0.856 | 0.714 |
| `MECH-270` | stable | provisional | 0.859 | 0.720 |
| `Q-001` | provisional | candidate | 0.665 | 0.528 |
| `Q-004` | provisional | candidate | 0.718 | 0.584 |
| `ARC-022` | stable | provisional | 0.854 | 0.720 |
| `MECH-057` | stable | provisional | 0.829 | 0.696 |
| `MECH-275` | stable | provisional | 0.866 | 0.733 |
| `Q-011` | stable | provisional | 0.833 | 0.702 |
| `MECH-094` | stable | provisional | 0.866 | 0.736 |
| `MECH-123` | stable | provisional | 0.859 | 0.729 |
| `SD-037` | stable | provisional | 0.870 | 0.740 |
| `MECH-057b` | stable | provisional | 0.870 | 0.740 |
| `Q-031` | stable | provisional | 0.870 | 0.740 |
| `SD-032d` | stable | provisional | 0.866 | 0.737 |
| `Q-016` | stable | provisional | 0.859 | 0.733 |
| `SD-003-SUCCESSOR` | stable | provisional | 0.870 | 0.745 |
| `MECH-269` | stable | provisional | 0.877 | 0.755 |
| `MECH-281` | stable | provisional | 0.877 | 0.755 |
| `MECH-280` | stable | provisional | 0.877 | 0.756 |
| `MECH-285` | stable | provisional | 0.879 | 0.759 |
| `MECH-294` | stable | provisional | 0.880 | 0.761 |
| `INV-048` | stable | provisional | 0.870 | 0.752 |
| `Q-017` | stable | provisional | 0.868 | 0.751 |
| `MECH-273` | stable | provisional | 0.882 | 0.765 |
| `ARC-060` | stable | provisional | 0.882 | 0.765 |
| `MECH-295` | stable | provisional | 0.883 | 0.767 |
| `MECH-272` | stable | provisional | 0.884 | 0.769 |
| `MECH-287` | stable | provisional | 0.881 | 0.766 |
| `ARC-039` | stable | provisional | 0.880 | 0.766 |
| `MECH-203` | stable | provisional | 0.877 | 0.763 |
| `Q-019` | stable | provisional | 0.886 | 0.773 |
| `Q-006` | provisional | candidate | 0.667 | 0.555 |
| `MECH-168` | stable | provisional | 0.877 | 0.767 |
| `MECH-092` | stable | provisional | 0.889 | 0.780 |
| `MECH-046` | stable | provisional | 0.888 | 0.780 |
| `MECH-058` | stable | provisional | 0.856 | 0.749 |
| `MECH-060` | stable | provisional | 0.803 | 0.697 |
| `MECH-172` | stable | provisional | 0.894 | 0.788 |
| `MECH-091` | provisional | candidate | 0.718 | 0.613 |
| `MECH-074` | stable | provisional | 0.891 | 0.786 |
| `MECH-171` | stable | provisional | 0.882 | 0.777 |
| `MECH-267` | stable | provisional | 0.896 | 0.792 |
| `MECH-187` | stable | provisional | 0.829 | 0.726 |
| `MECH-293` | stable | provisional | 0.896 | 0.793 |
| `ARC-035` | stable | provisional | 0.899 | 0.798 |
| `SD-033e` | stable | provisional | 0.899 | 0.798 |
| `MECH-288` | stable | provisional | 0.895 | 0.794 |
| `MECH-230` | stable | provisional | 0.834 | 0.734 |
| `MECH-122` | stable | provisional | 0.897 | 0.797 |
| `MECH-057a` | stable | provisional | 0.809 | 0.710 |
| `MECH-061` | stable | provisional | 0.810 | 0.711 |
| `INV-049` | stable | provisional | 0.895 | 0.796 |
| `Q-034` | provisional | candidate | 0.740 | 0.644 |
| `MECH-191` | stable | provisional | 0.892 | 0.796 |
| `ARC-026` | provisional | candidate | 0.696 | 0.601 |
| `MECH-178` | stable | provisional | 0.802 | 0.710 |
| `MECH-179` | stable | provisional | 0.802 | 0.710 |
| `INV-053` | stable | provisional | 0.883 | 0.791 |
| `Q-036` | stable | provisional | 0.809 | 0.718 |
| `SD-023` | provisional | candidate | 0.730 | 0.639 |
| `MECH-220` | provisional | candidate | 0.730 | 0.641 |
| `MECH-072` | stable | provisional | 0.857 | 0.769 |
| `MECH-056` | stable | provisional | 0.821 | 0.733 |
| `Q-023` | stable | provisional | 0.803 | 0.717 |
| `ARC-029` | provisional | candidate | 0.671 | 0.589 |
| `SD-032a` | stable | provisional | 0.857 | 0.777 |
| `MECH-193` | stable | provisional | 0.814 | 0.734 |
| `MECH-181` | provisional | candidate | 0.719 | 0.639 |
| `MECH-152` | provisional | candidate | 0.718 | 0.639 |
| `MECH-135` | stable | provisional | 0.803 | 0.725 |
| `MECH-124` | stable | provisional | 0.846 | 0.769 |
| `SD-032c` | provisional | candidate | 0.678 | 0.602 |
| `SD-035` | stable | provisional | 0.827 | 0.751 |
| `MECH-102` | provisional | candidate | 0.696 | 0.622 |
| `MECH-205` | stable | provisional | 0.832 | 0.758 |
| `MECH-106` | stable | provisional | 0.826 | 0.754 |
| `MECH-192` | stable | provisional | 0.822 | 0.750 |
| `INV-029` | provisional | candidate | 0.695 | 0.624 |
| `MECH-155` | provisional | candidate | 0.658 | 0.589 |
| `SD-029` | provisional | candidate | 0.662 | 0.595 |
| `ARC-003` | stable | provisional | 0.806 | 0.739 |
| `ARC-005` | stable | provisional | 0.806 | 0.739 |
| `MECH-175` | stable | provisional | 0.829 | 0.763 |
| `MECH-074a` | stable | provisional | 0.838 | 0.774 |
| `MECH-188` | provisional | candidate | 0.677 | 0.614 |
| `INV-052` | stable | provisional | 0.847 | 0.784 |
| `MECH-256` | stable | provisional | 0.823 | 0.761 |
| `SD-013` | stable | provisional | 0.826 | 0.764 |
| `ARC-021` | stable | provisional | 0.823 | 0.761 |
| `SD-039` | stable | provisional | 0.843 | 0.781 |
| `INV-044` | stable | provisional | 0.856 | 0.799 |
| `MECH-075` | provisional | candidate | 0.684 | 0.629 |
| `ARC-033` | stable | provisional | 0.809 | 0.755 |
| `Q-021` | provisional | candidate | 0.668 | 0.614 |
| `MECH-120` | provisional | candidate | 0.670 | 0.616 |
| `SD-007` | stable | provisional | 0.817 | 0.765 |
| `MECH-071` | stable | provisional | 0.828 | 0.776 |
| `ARC-038` | provisional | candidate | 0.682 | 0.631 |
| `SD-021` | provisional | candidate | 0.651 | 0.602 |
| `MECH-112` | stable | provisional | 0.843 | 0.796 |
| `MECH-165` | provisional | candidate | 0.690 | 0.643 |
| `MECH-119` | stable | provisional | 0.825 | 0.779 |
| `MECH-099` | provisional | candidate | 0.674 | 0.631 |
| `MECH-118` | provisional | candidate | 0.683 | 0.646 |
| `MECH-291` | provisional | candidate | 0.679 | 0.645 |
| `ARC-041` | candidate | below_candidate | 0.517 | 0.487 |
| `MECH-150` | candidate | below_candidate | 0.521 | 0.493 |
| `ARC-017` | candidate | provisional | 0.638 | 0.650 |
| `IMPL-022` | candidate | provisional | 0.642 | 0.675 |
| `SD-040` | provisional | stable | 0.760 | 0.802 |
| `ARC-011` | provisional | stable | 0.783 | 0.859 |

---

Source snapshot: `claim_evidence.v1.production_snapshot.json`
Staging matrix: `claim_evidence.v1.staging_b_softened.json`
