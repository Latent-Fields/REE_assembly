# Option E (decouple lit_conf / exp_conf) -- staging diff

**overall_confidence = exp_conf only.** Literature is reported as a parallel signal and via `evidence_quadrant`. Quadrants:

- `high_exp` threshold: exp_conf >= 0.62
- `high_lit` threshold: lit_conf >= 0.55
- `low_exp_flag` (replaces low_overall_confidence): exp_conf < 0.55
- `lit_only_above_cap` flag: no experimental evidence but lit_conf >= 0.5

## Quadrant distribution

|  | **high exp** | **low exp** |
|---|---|---|
| **high lit** | confirmed established: **64** | plausible unproven: **195** |
| **low lit** | novel discovery: **1** | speculative: **3** |

Total scored claims: 263

## Overall delta summary

- avg overall_confidence delta: **-0.506**
- claims with overall drop > 0.05: **229**
- claims with overall drop > 0.10: **210**
- claims with overall rise > 0.05: **6** (claims where stripping lit revealed strong exp underneath)

## New flag summary

- `low_exp_flag`: **49** claims have experiments but exp_conf < 0.55
- `lit_only_above_cap`: **140** claims have no exp but lit_conf >= 0.5 (need an exp pull)

## Top 25 claims by overall_confidence drop

| claim | n_exp | n_lit | exp_conf | lit_conf | overall_prod | overall_new | delta | quadrant |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `MECH-265` | 0 | 6 | 0.000 | 0.917 | 0.917 | 0.000 | **-0.917** | plausible_unproven |
| `MECH-263` | 0 | 4 | 0.000 | 0.913 | 0.913 | 0.000 | **-0.913** | plausible_unproven |
| `SD-033b` | 0 | 5 | 0.000 | 0.910 | 0.910 | 0.000 | **-0.910** | plausible_unproven |
| `MECH-271` | 0 | 4 | 0.000 | 0.909 | 0.909 | 0.000 | **-0.909** | plausible_unproven |
| `MECH-279` | 0 | 5 | 0.000 | 0.907 | 0.907 | 0.000 | **-0.907** | plausible_unproven |
| `MECH-292` | 0 | 13 | 0.000 | 0.905 | 0.905 | 0.000 | **-0.905** | plausible_unproven |
| `MECH-163` | 0 | 9 | 0.000 | 0.904 | 0.904 | 0.000 | **-0.904** | plausible_unproven |
| `SD-014` | 0 | 4 | 0.000 | 0.903 | 0.903 | 0.000 | **-0.903** | plausible_unproven |
| `MECH-166` | 0 | 4 | 0.000 | 0.902 | 0.902 | 0.000 | **-0.902** | plausible_unproven |
| `SD-017` | 0 | 6 | 0.000 | 0.902 | 0.902 | 0.000 | **-0.902** | plausible_unproven |
| `MECH-180` | 0 | 4 | 0.000 | 0.900 | 0.900 | 0.000 | **-0.900** | plausible_unproven |
| `ARC-035` | 0 | 13 | 0.000 | 0.899 | 0.899 | 0.000 | **-0.899** | plausible_unproven |
| `SD-033e` | 0 | 10 | 0.000 | 0.899 | 0.899 | 0.000 | **-0.899** | plausible_unproven |
| `MECH-122` | 0 | 4 | 0.000 | 0.897 | 0.897 | 0.000 | **-0.897** | plausible_unproven |
| `INV-057` | 0 | 5 | 0.000 | 0.897 | 0.897 | 0.000 | **-0.897** | plausible_unproven |
| `MECH-267` | 0 | 5 | 0.000 | 0.896 | 0.896 | 0.000 | **-0.896** | plausible_unproven |
| `MECH-293` | 0 | 7 | 0.000 | 0.896 | 0.896 | 0.000 | **-0.896** | plausible_unproven |
| `MECH-030` | 0 | 4 | 0.000 | 0.895 | 0.895 | 0.000 | **-0.895** | plausible_unproven |
| `INV-049` | 0 | 5 | 0.000 | 0.895 | 0.895 | 0.000 | **-0.895** | plausible_unproven |
| `MECH-288` | 0 | 11 | 0.000 | 0.895 | 0.895 | 0.000 | **-0.895** | plausible_unproven |
| `MECH-172` | 0 | 6 | 0.000 | 0.894 | 0.894 | 0.000 | **-0.894** | plausible_unproven |
| `MECH-191` | 0 | 4 | 0.000 | 0.892 | 0.892 | 0.000 | **-0.892** | plausible_unproven |
| `MECH-074` | 0 | 9 | 0.000 | 0.891 | 0.891 | 0.000 | **-0.891** | plausible_unproven |
| `MECH-092` | 0 | 16 | 0.000 | 0.889 | 0.889 | 0.000 | **-0.889** | plausible_unproven |
| `MECH-046` | 0 | 4 | 0.000 | 0.888 | 0.888 | 0.000 | **-0.888** | plausible_unproven |

## Top 25 claims by overall_confidence RISE (these were being held back by missing/weak lit)

| claim | n_exp | n_lit | exp_conf | lit_conf | overall_prod | overall_new | delta | quadrant |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `MECH-073` | 3 | 5 | 0.851 | 0.682 | 0.767 | 0.851 | **+0.084** | confirmed_established |
| `SD-008` | 5 | 2 | 0.933 | 0.742 | 0.857 | 0.933 | **+0.076** | confirmed_established |
| `INV-053` | 7 | 5 | 0.955 | 0.811 | 0.883 | 0.955 | **+0.072** | confirmed_established |
| `MECH-260` | 6 | 1 | 0.943 | 0.717 | 0.886 | 0.943 | **+0.057** | confirmed_established |
| `MECH-117` | 6 | 2 | 0.914 | 0.774 | 0.858 | 0.914 | **+0.056** | confirmed_established |
| `MECH-090` | 20 | 9 | 0.805 | 0.701 | 0.753 | 0.805 | **+0.052** | confirmed_established |
| `MECH-072` | 5 | 6 | 0.899 | 0.815 | 0.857 | 0.899 | **+0.042** | confirmed_established |
| `MECH-100` | 4 | 3 | 0.817 | 0.750 | 0.783 | 0.817 | **+0.034** | confirmed_established |
| `MECH-069` | 8 | 2 | 0.871 | 0.791 | 0.839 | 0.871 | **+0.032** | confirmed_established |
| `MECH-258` | 6 | 9 | 0.943 | 0.884 | 0.913 | 0.943 | **+0.030** | confirmed_established |
| `MECH-119` | 4 | 3 | 0.849 | 0.800 | 0.825 | 0.849 | **+0.024** | confirmed_established |
| `SD-006` | 4 | 2 | 0.835 | 0.784 | 0.815 | 0.835 | **+0.020** | confirmed_established |
| `ARC-027` | 4 | 3 | 0.889 | 0.856 | 0.872 | 0.889 | **+0.017** | confirmed_established |
| `SD-020` | 5 | 5 | 0.943 | 0.911 | 0.927 | 0.943 | **+0.016** | confirmed_established |
| `ARC-025` | 2 | 2 | 0.733 | 0.712 | 0.722 | 0.733 | **+0.011** | confirmed_established |
| `ARC-033` | 14 | 20 | 0.820 | 0.799 | 0.809 | 0.820 | **+0.011** | confirmed_established |
| `SD-022` | 2 | 2 | 0.797 | 0.774 | 0.786 | 0.797 | **+0.011** | confirmed_established |
| `MECH-033` | 11 | 18 | 0.869 | 0.851 | 0.860 | 0.869 | **+0.009** | confirmed_established |
| `MECH-259` | 1 | 2 | 0.757 | 0.745 | 0.749 | 0.757 | **+0.008** | confirmed_established |
| `SD-010` | 19 | 3 | 0.843 | 0.830 | 0.837 | 0.843 | **+0.006** | confirmed_established |
| `SD-011` | 7 | 23 | 0.878 | 0.871 | 0.874 | 0.878 | **+0.004** | confirmed_established |
| `MECH-231` | 2 | 3 | 0.801 | 0.794 | 0.797 | 0.801 | **+0.004** | confirmed_established |

## Novel discovery quadrant -- worth surfacing in governance

These have exp_conf >= 0.62 but lit_conf < 0.55. Either a genuine novel finding without prior art, or a missing lit pull.

Total in quadrant: **1**

| claim | exp_conf | lit_conf |
|---|---:|---:|
| `onboarding` | 0.731 | 0.000 |

---

Source snapshot: `claim_evidence.v1.production_snapshot.json`
Staging matrix: `claim_evidence.v1.staging_e_decoupled.json`
