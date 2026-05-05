# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-05-05T22:10:17.242772Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 208 |
| `substrate_coherence` | 30 |
| `answer_state` | 38 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **70** | plausible_unproven: **202** |
| **low lit**             | novel_discovery: **1**         | speculative: **3** |

Total scored claims: 276

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **135** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.815 | 0.000 | 0.815 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 6 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.641 | 0.000 | 0.641 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.839 | 0.000 | 0.839 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.653 | 0.000 | 0.653 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.712 | 0.000 | 0.712 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.712 | 0.000 | 0.712 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.850 | 0.000 | 0.850 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.818 | 0.000 | 0.818 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.893 | 0.000 | 0.893 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.783 | 0.000 | 0.783 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.766 | 0.000 | 0.766 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.854 | 0.000 | 0.854 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.889 | 0.000 | 0.889 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.837 | 0.000 | 0.837 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.835 | 0.000 | 0.835 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 3 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.896 | 0.000 | 0.896 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.716 | 0.000 | 0.716 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.902 | 0.000 | 0.902 | 0 | 9 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.777 | 0.000 | 0.777 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.747 | 0.000 | 0.747 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.784 | 0.000 | 0.784 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.898 | 0.000 | 0.898 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.717 | 0.000 | 0.717 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.742 | 0.000 | 0.742 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.830 | 0.000 | 0.830 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.728 | 0.000 | 0.728 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.802 | 0.000 | 0.802 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.891 | 0.000 | 0.891 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.812 | 0.000 | 0.812 | 0 | 3 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 5 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.775 | 0.000 | 0.775 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.912 | 0.000 | 0.912 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.915 | 0.000 | 0.915 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.851 | 0.000 | 0.851 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.894 | 0.000 | 0.894 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.849 | 0.000 | 0.849 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 32 | plausible_unproven |
| `MECH-269b` | - | - | 0.842 | 0.000 | 0.842 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.907 | 0.000 | 0.907 | 0 | 4 | plausible_unproven |
| `MECH-272` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 14 | plausible_unproven |
| `MECH-273` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.865 | 0.000 | 0.865 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 5 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.876 | 0.000 | 0.876 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 14 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 5 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.894 | 0.000 | 0.894 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.677 | 0.000 | 0.677 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.904 | 0.000 | 0.904 | 0 | 13 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.894 | 0.000 | 0.894 | 0 | 7 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 9 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.881 | 0.000 | 0.881 | 0 | 6 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 4 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.853 | 0.000 | 0.853 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.904 | 0.000 | 0.904 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.812 | 0.000 | 0.812 | 0 | 5 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.901 | 0.000 | 0.901 | 0 | 4 | plausible_unproven |
| `SD-032d` | - | - | 0.865 | 0.000 | 0.865 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.827 | 0.000 | 0.827 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.908 | 0.000 | 0.908 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.897 | 0.000 | 0.897 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.854 | 0.000 | 0.854 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.829 | 0.000 | 0.829 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.841 | 0.000 | 0.841 | 0 | 3 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.758 | 0.000 | 0.758 | 0 | 1 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.685 | 0.258 | 0.828 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.672 | 0.262 | 0.809 | 1 | 3 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.730 | 0.286 | 0.878 | 1 | 5 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.725 | 0.286 | 0.871 | 1 | 4 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.724 | 0.287 | 0.870 | 1 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.634 | 0.288 | 0.865 | 2 | 8 | plausible_unproven |
| `MECH-116` | mechanism_hypothesis | candidate | 0.640 | 0.288 | 0.874 | 2 | 7 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.713 | 0.292 | 0.853 | 1 | 6 | plausible_unproven |
| `SD-032c` | - | - | 0.673 | 0.292 | 0.800 | 1 | 3 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.664 | 0.312 | 0.898 | 2 | 7 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.651 | 0.314 | 0.876 | 2 | 5 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.711 | 0.323 | 0.840 | 1 | 10 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.688 | 0.325 | 0.809 | 1 | 11 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.747 | 0.377 | 0.870 | 1 | 4 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.643 | 0.392 | 0.894 | 3 | 8 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.752 | 0.402 | 0.869 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.755 | 0.402 | 0.873 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.757 | 0.404 | 0.875 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.755 | 0.407 | 0.871 | 1 | 5 | plausible_unproven |
| `MECH-302` | mechanism_hypothesis | candidate | 0.662 | 0.422 | 0.903 | 3 | 6 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.638 | 0.425 | 0.852 | 4 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.665 | 0.429 | 0.901 | 6 | 7 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.676 | 0.472 | 0.880 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.665 | 0.496 | 0.835 | 3 | 3 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.655 | 0.523 | 0.788 | 5 | 3 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.693 | 0.524 | 0.861 | 5 | 9 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.688 | 0.527 | 0.849 | 24 | 9 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.735 | 0.558 | 0.911 | 7 | 10 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.755 | 0.599 | 0.911 | 18 | 9 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.723 | 0.600 | 0.845 | 10 | 24 | plausible_unproven |

_Suppressed by gating: 21 substrate_coherence (ARC + universal invariant), 32 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **0** standard-gating claims with no exp.

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `ARC-003` | architectural_commitment | active | 0.804 | 3 |
| `ARC-005` | architectural_commitment | active | 0.804 | 3 |
| `ARC-014` | architectural_commitment | active | 0.790 | 3 |
| `ARC-011` | architectural_commitment | active | 0.782 | 1 |
| `ARC-001` | architectural_commitment | active | 0.691 | 1 |
| `INV-014` | invariant | active | 0.691 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.866 | 11 |
| `Q-016` | open_question | active | 0.857 | 5 |
| `Q-015` | open_question | active | 0.838 | 5 |
| `Q-005` | open_question | active | 0.807 | 4 |
| `Q-020` | open_question | resolved | 0.781 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.716 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **37**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-150` | candidate | 0.246 | 1 |
| `MECH-165` | candidate | 0.258 | 1 |
| `SD-018` | implemented | 0.260 | 1 |
| `MECH-188` | candidate | 0.262 | 1 |
| `MECH-111` | candidate | 0.279 | 2 |
| `MECH-118` | candidate | 0.279 | 2 |
| `MECH-216` | provisional | 0.286 | 1 |
| `SD-023` | candidate | 0.286 | 1 |
| `MECH-220` | candidate | 0.287 | 1 |
| `ARC-032` | candidate | 0.288 | 2 |
| `MECH-116` | candidate | 0.288 | 2 |
| `MECH-091` | candidate | 0.292 | 1 |
| `SD-032c` | - | 0.292 | 1 |
| `MECH-186` | candidate | 0.311 | 2 |
| `MECH-120` | candidate | 0.312 | 2 |
| `MECH-155` | candidate | 0.314 | 2 |
| `SD-047` | provisional | 0.323 | 1 |
| `SD-049` | candidate | 0.325 | 1 |
| `MECH-128` | candidate | 0.347 | 3 |
| `MECH-047` | provisional | 0.377 | 1 |
| `INV-054` | candidate | 0.390 | 3 |
| `SD-021` | candidate | 0.392 | 3 |
| `MECH-026` | provisional | 0.402 | 1 |
| `MECH-029` | provisional | 0.402 | 1 |
| `MECH-022` | provisional | 0.404 | 1 |
| `MECH-025` | candidate | 0.407 | 1 |
| `MECH-070` | retiring | 0.420 | 4 |
| `MECH-302` | candidate | 0.422 | 3 |
| `MECH-153` | candidate | 0.425 | 4 |
| `MECH-099` | candidate | 0.429 | 6 |
| ... | ... | ... | ... (7 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **105**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-265` | candidate | 0.915 | 6 |
| `MECH-263` | candidate | 0.912 | 4 |
| `SD-033b` | - | 0.908 | 5 |
| `MECH-271` | candidate | 0.907 | 4 |
| `MECH-279` | candidate | 0.905 | 5 |
| `MECH-292` | candidate | 0.904 | 13 |
| `MECH-CBBL-PROPOSED` | - | 0.904 | 7 |
| `MECH-163` | candidate | 0.902 | 9 |
| `MECH-166` | candidate | 0.901 | 4 |
| `SD-014` | candidate | 0.901 | 4 |
| `MECH-180` | candidate | 0.898 | 4 |
| `SD-033e` | - | 0.897 | 10 |
| `MECH-122` | provisional | 0.896 | 4 |
| `MECH-267` | provisional | 0.894 | 5 |
| `MECH-288` | candidate | 0.894 | 11 |
| `MECH-293` | candidate | 0.894 | 7 |
| `MECH-030` | provisional | 0.893 | 4 |
| `MECH-172` | candidate | 0.892 | 6 |
| `MECH-191` | candidate | 0.891 | 4 |
| `MECH-074` | provisional | 0.889 | 9 |
| `MECH-092` | candidate | 0.887 | 16 |
| `MECH-046` | provisional | 0.886 | 4 |
| `MECH-272` | candidate | 0.882 | 14 |
| `MECH-171` | candidate | 0.881 | 4 |
| `MECH-295` | candidate | 0.881 | 6 |
| `ARC-060` | candidate | 0.880 | 6 |
| `MECH-273` | candidate | 0.880 | 4 |
| `MECH-287` | candidate | 0.879 | 5 |
| `MECH-285` | candidate | 0.878 | 16 |
| `MECH-294` | candidate | 0.878 | 9 |
| `MECH-168` | candidate | 0.876 | 4 |
| `MECH-269` | candidate | 0.876 | 32 |
| `MECH-280` | candidate | 0.876 | 5 |
| `MECH-203` | candidate | 0.875 | 5 |
| `MECH-281` | candidate | 0.875 | 4 |
| `MECH-303` | candidate | 0.874 | 4 |
| `MECH-264` | candidate | 0.871 | 3 |
| `MECH-121` | candidate | 0.870 | 3 |
| `INV-048` | candidate | 0.868 | 4 |
| `MECH-057b` | - | 0.868 | 4 |
| `SD-003-SUCCESSOR` | - | 0.868 | 4 |
| `SD-037` | candidate | 0.868 | 4 |
| `MECH-275` | candidate | 0.865 | 6 |
| `SD-032d` | - | 0.865 | 4 |
| `MECH-123` | candidate | 0.857 | 5 |
| `MECH-270` | candidate | 0.857 | 4 |
| `MECH-058` | retired | 0.854 | 9 |
| `SD-034` | provisional | 0.854 | 6 |
| `MECH-304` | candidate | 0.853 | 3 |
| `MECH-266` | provisional | 0.851 | 6 |
| ... | ... | ... | ... (55 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
