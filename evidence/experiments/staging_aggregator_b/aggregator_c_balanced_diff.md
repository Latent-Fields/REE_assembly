# Aggregator c_balanced (additive_v2 lit_conf) -- staging diff

Coefficients: form=additive_v2, quality=0.65, consistency=0.1, volume=0.15, recency=0.1, single_paper_consistency=0.0, volume_log_saturation_n=10

Compares production claim_evidence.v1.json against rescored output using the multiplicative lit_conf aggregator. exp_conf and overall blending logic are unchanged.

## Summary

- claims rescored: **263** (262 with literature evidence)
- avg lit_conf delta (lit-bearing claims): **-0.056**
- avg overall_confidence delta (all claims): **-0.046**
- claims with lit_conf drop > 0.05: **155**
- claims with lit_conf drop > 0.10: **8**
- claims with lit_conf rise > 0.05: **0**

## Top 25 lit_conf drops

| claim | n_lit | lit_prod | lit_new | delta | overall_prod | overall_new | quality | mult |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Q-001` | 4 | 0.802 | 0.695 | **-0.107** | 0.665 | 0.585 | 0.620 | 1.000 |
| `MECH-291` | 1 | 0.679 | 0.572 | **-0.107** | 0.679 | 0.572 | 0.660 | 1.000 |
| `MECH-185` | 4 | 0.803 | 0.697 | **-0.106** | 0.803 | 0.697 | 0.620 | 1.000 |
| `Q-004` | 4 | 0.805 | 0.700 | **-0.105** | 0.718 | 0.639 | 0.628 | 1.000 |
| `Q-005` | 4 | 0.809 | 0.705 | **-0.104** | 0.809 | 0.705 | 0.635 | 1.000 |
| `MECH-025b` | 4 | 0.820 | 0.716 | **-0.104** | 0.820 | 0.716 | 0.640 | 1.000 |
| `Q-003` | 4 | 0.813 | 0.710 | **-0.103** | 0.611 | 0.549 | 0.642 | 1.000 |
| `MECH-093` | 4 | 0.822 | 0.721 | **-0.101** | 0.757 | 0.707 | 0.655 | 1.000 |
| `Q-002` | 4 | 0.823 | 0.723 | **-0.100** | 0.631 | 0.581 | 0.662 | 1.000 |
| `SD-032e` | 4 | 0.829 | 0.729 | **-0.100** | 0.829 | 0.729 | 0.662 | 1.000 |
| `ARC-001` | 1 | 0.693 | 0.594 | **-0.099** | 0.693 | 0.594 | 0.720 | 1.000 |
| `INV-014` | 1 | 0.693 | 0.594 | **-0.099** | 0.693 | 0.594 | 0.720 | 1.000 |
| `MECH-068` | 1 | 0.693 | 0.594 | **-0.099** | 0.693 | 0.594 | 0.720 | 1.000 |
| `MECH-135` | 4 | 0.828 | 0.729 | **-0.099** | 0.803 | 0.754 | 0.672 | 1.000 |
| `Q-033` | 4 | 0.827 | 0.728 | **-0.099** | 0.827 | 0.728 | 0.667 | 1.000 |
| `Q-027` | 3 | 0.663 | 0.564 | **-0.099** | 0.663 | 0.564 | 0.427 | 1.000 |
| `MECH-097` | 1 | 0.698 | 0.600 | **-0.098** | 0.583 | 0.534 | 0.720 | 1.000 |
| `MECH-074d` | 4 | 0.836 | 0.738 | **-0.098** | 0.836 | 0.738 | 0.675 | 1.000 |
| `Q-040` | 4 | 0.840 | 0.742 | **-0.098** | 0.840 | 0.742 | 0.680 | 1.000 |
| `Q-013` | 4 | 0.830 | 0.733 | **-0.097** | 0.830 | 0.733 | 0.677 | 1.000 |
| `Q-014` | 4 | 0.833 | 0.736 | **-0.097** | 0.833 | 0.736 | 0.682 | 1.000 |
| `MECH-900` | 1 | 0.700 | 0.604 | **-0.096** | 0.700 | 0.604 | 0.740 | 1.000 |
| `ARC-026` | 5 | 0.803 | 0.707 | **-0.096** | 0.696 | 0.648 | 0.614 | 1.000 |
| `INV-046` | 1 | 0.714 | 0.618 | **-0.096** | 0.714 | 0.618 | 0.740 | 1.000 |
| `INV-047` | 1 | 0.714 | 0.618 | **-0.096** | 0.714 | 0.618 | 0.740 | 1.000 |

## Top 10 lit_conf rises (sanity check -- expect few/none)

| claim | n_lit | lit_prod | lit_new | delta |
|---|---:|---:|---:|---:|
| `MECH-090` | 9 | 0.701 | 0.735 | +0.034 |
| `MECH-073` | 5 | 0.682 | 0.711 | +0.029 |
| `IMPL-022` | 2 | 0.642 | 0.670 | +0.028 |

## Promotion-tier impact

Claims that cross typical confidence thresholds (0.50 candidate, 0.65 provisional, 0.80 stable) based on **overall_confidence** under the new aggregator.

| claim | prod tier | new tier | overall_prod | overall_new |
|---|---|---|---:|---:|
| `MECH-291` | provisional | candidate | 0.679 | 0.572 |
| `MECH-185` | stable | provisional | 0.803 | 0.697 |
| `Q-005` | stable | provisional | 0.809 | 0.705 |
| `MECH-025b` | stable | provisional | 0.820 | 0.716 |
| `SD-032e` | stable | provisional | 0.829 | 0.729 |
| `Q-027` | provisional | candidate | 0.663 | 0.564 |
| `ARC-001` | provisional | candidate | 0.693 | 0.594 |
| `INV-014` | provisional | candidate | 0.693 | 0.594 |
| `MECH-068` | provisional | candidate | 0.693 | 0.594 |
| `Q-033` | stable | provisional | 0.827 | 0.728 |
| `MECH-074d` | stable | provisional | 0.836 | 0.738 |
| `Q-040` | stable | provisional | 0.840 | 0.742 |
| `Q-013` | stable | provisional | 0.830 | 0.733 |
| `Q-014` | stable | provisional | 0.833 | 0.736 |
| `MECH-900` | provisional | candidate | 0.700 | 0.604 |
| `INV-046` | provisional | candidate | 0.714 | 0.618 |
| `INV-047` | provisional | candidate | 0.714 | 0.618 |
| `Q-011` | stable | provisional | 0.833 | 0.739 |
| `MECH-E2-DUAL-FUNCTION` | stable | provisional | 0.814 | 0.721 |
| `MECH-270` | stable | provisional | 0.859 | 0.767 |
| `SD-037` | stable | provisional | 0.870 | 0.781 |
| `MECH-057b` | stable | provisional | 0.870 | 0.781 |
| `SD-003-SUCCESSOR` | stable | provisional | 0.870 | 0.782 |
| `SD-032d` | stable | provisional | 0.866 | 0.778 |
| `MECH-183` | stable | provisional | 0.832 | 0.745 |
| `INV-048` | stable | provisional | 0.870 | 0.783 |
| `MECH-281` | stable | provisional | 0.877 | 0.791 |
| `ARC-023` | stable | provisional | 0.835 | 0.750 |
| `Q-015` | stable | provisional | 0.840 | 0.756 |
| `MECH-168` | stable | provisional | 0.877 | 0.793 |
| `MECH-273` | stable | provisional | 0.882 | 0.798 |
| `Q-001` | provisional | candidate | 0.665 | 0.585 |
| `Q-004` | provisional | candidate | 0.718 | 0.639 |
| `MECH-123` | stable | provisional | 0.859 | 0.780 |
| `Q-016` | stable | provisional | 0.859 | 0.781 |
| `Q-031` | stable | provisional | 0.870 | 0.793 |
| `MECH-268` | stable | provisional | 0.850 | 0.777 |
| `MECH-266` | stable | provisional | 0.853 | 0.781 |
| `SD-034` | stable | provisional | 0.855 | 0.784 |
| `INV-043` | stable | provisional | 0.841 | 0.773 |
| `MECH-275` | stable | provisional | 0.866 | 0.798 |
| `MECH-269b` | stable | provisional | 0.843 | 0.777 |
| `MECH-057` | stable | provisional | 0.829 | 0.764 |
| `ARC-028` | stable | provisional | 0.856 | 0.793 |
| `ARC-022` | stable | provisional | 0.854 | 0.792 |
| `MECH-124` | stable | provisional | 0.846 | 0.785 |
| `MECH-057a` | stable | provisional | 0.809 | 0.750 |
| `MECH-178` | stable | provisional | 0.802 | 0.746 |
| `MECH-179` | stable | provisional | 0.802 | 0.746 |
| `Q-006` | provisional | candidate | 0.667 | 0.612 |
| `Q-023` | stable | provisional | 0.803 | 0.748 |
| `Q-036` | stable | provisional | 0.809 | 0.754 |
| `MECH-193` | stable | provisional | 0.814 | 0.761 |
| `ARC-003` | stable | provisional | 0.806 | 0.755 |
| `ARC-005` | stable | provisional | 0.806 | 0.755 |
| `MECH-230` | stable | provisional | 0.834 | 0.783 |
| `INV-045` | provisional | candidate | 0.655 | 0.605 |
| `MECH-192` | stable | provisional | 0.822 | 0.772 |
| `SD-035` | stable | provisional | 0.827 | 0.777 |
| `MECH-135` | stable | provisional | 0.803 | 0.754 |
| `ARC-026` | provisional | candidate | 0.696 | 0.648 |
| `MECH-175` | stable | provisional | 0.829 | 0.781 |
| `MECH-106` | stable | provisional | 0.826 | 0.780 |
| `MECH-187` | stable | provisional | 0.829 | 0.783 |
| `MECH-074a` | stable | provisional | 0.838 | 0.792 |
| `SD-039` | stable | provisional | 0.843 | 0.797 |
| `SD-013` | stable | provisional | 0.826 | 0.782 |
| `MECH-155` | provisional | candidate | 0.658 | 0.615 |
| `SD-032c` | provisional | candidate | 0.678 | 0.635 |
| `MECH-071` | stable | provisional | 0.828 | 0.787 |
| `MECH-061` | stable | provisional | 0.810 | 0.770 |
| `MECH-188` | provisional | candidate | 0.677 | 0.637 |
| `ARC-029` | provisional | candidate | 0.671 | 0.632 |
| `ARC-038` | provisional | candidate | 0.682 | 0.643 |
| `SD-007` | stable | provisional | 0.817 | 0.781 |
| `Q-021` | provisional | candidate | 0.668 | 0.634 |
| `MECH-060` | stable | provisional | 0.803 | 0.770 |
| `ARC-021` | stable | provisional | 0.823 | 0.793 |
| `MECH-120` | provisional | candidate | 0.670 | 0.641 |
| `MECH-256` | stable | provisional | 0.823 | 0.794 |
| `MECH-119` | stable | provisional | 0.825 | 0.796 |
| `MECH-056` | stable | provisional | 0.821 | 0.792 |
| `SD-029` | provisional | candidate | 0.662 | 0.639 |
| `SD-021` | provisional | candidate | 0.651 | 0.630 |
| `MECH-229` | stable | provisional | 0.801 | 0.798 |
| `IMPL-022` | candidate | provisional | 0.642 | 0.670 |

---

Source snapshot: `claim_evidence.v1.production_snapshot.json`
Staging matrix: `claim_evidence.v1.staging_c_balanced.json`
