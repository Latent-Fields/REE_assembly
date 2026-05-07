# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-05-07T22:30:21.691380Z`

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

Total: **136** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-048` | architecture_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 2 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 6 | plausible_unproven |
| `IMPL-022` | implementation_note | legacy | 0.640 | 0.000 | 0.640 | 0 | 2 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.838 | 0.000 | 0.838 | 0 | 7 | plausible_unproven |
| `INV-045` | invariant | candidate | 0.653 | 0.000 | 0.653 | 0 | 6 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.711 | 0.000 | 0.711 | 0 | 1 | plausible_unproven |
| `INV-047` | derived_prediction | candidate | 0.711 | 0.000 | 0.711 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.850 | 0.000 | 0.850 | 0 | 3 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `MECH-025b` | - | - | 0.818 | 0.000 | 0.818 | 0 | 4 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.892 | 0.000 | 0.892 | 0 | 4 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.783 | 0.000 | 0.783 | 0 | 2 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.886 | 0.000 | 0.886 | 0 | 4 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.758 | 0.000 | 0.758 | 0 | 2 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.765 | 0.000 | 0.765 | 0 | 2 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 7 | plausible_unproven |
| `MECH-057b` | - | - | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.854 | 0.000 | 0.854 | 0 | 9 | plausible_unproven |
| `MECH-063` | mechanism_hypothesis | provisional | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-068` | mechanism_hypothesis | candidate | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `MECH-074` | mechanism_hypothesis | provisional | 0.889 | 0.000 | 0.889 | 0 | 9 | plausible_unproven |
| `MECH-074a` | - | - | 0.836 | 0.000 | 0.836 | 0 | 3 | plausible_unproven |
| `MECH-074c` | - | - | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-074d` | - | - | 0.834 | 0.000 | 0.834 | 0 | 4 | plausible_unproven |
| `MECH-076` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 2 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.887 | 0.000 | 0.887 | 0 | 16 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.806 | 0.000 | 0.806 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.870 | 0.000 | 0.870 | 0 | 3 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.895 | 0.000 | 0.895 | 0 | 4 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 5 | plausible_unproven |
| `MECH-152` | mechanism_hypothesis | provisional | 0.715 | 0.000 | 0.715 | 0 | 2 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 2 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.901 | 0.000 | 0.901 | 0 | 9 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.900 | 0.000 | 0.900 | 0 | 4 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 2 | plausible_unproven |
| `MECH-171` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-172` | mechanism_hypothesis | candidate | 0.892 | 0.000 | 0.892 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.746 | 0.000 | 0.746 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.826 | 0.000 | 0.826 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.784 | 0.000 | 0.784 | 0 | 2 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.769 | 0.000 | 0.769 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 3 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.897 | 0.000 | 0.897 | 0 | 4 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.716 | 0.000 | 0.716 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.829 | 0.000 | 0.829 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.728 | 0.000 | 0.728 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.801 | 0.000 | 0.801 | 0 | 4 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.890 | 0.000 | 0.890 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.811 | 0.000 | 0.811 | 0 | 3 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 5 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.779 | 0.000 | 0.779 | 0 | 2 | plausible_unproven |
| `MECH-245` | mechanism_hypothesis | candidate | 0.774 | 0.000 | 0.774 | 0 | 2 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.772 | 0.000 | 0.772 | 0 | 2 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.911 | 0.000 | 0.911 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 3 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.915 | 0.000 | 0.915 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.851 | 0.000 | 0.851 | 0 | 6 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.893 | 0.000 | 0.893 | 0 | 5 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.848 | 0.000 | 0.848 | 0 | 6 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 32 | plausible_unproven |
| `MECH-269b` | - | - | 0.841 | 0.000 | 0.841 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.856 | 0.000 | 0.856 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.906 | 0.000 | 0.906 | 0 | 4 | plausible_unproven |
| `MECH-272` | mechanism_hypothesis | candidate | 0.882 | 0.000 | 0.882 | 0 | 14 | plausible_unproven |
| `MECH-273` | mechanism_hypothesis | candidate | 0.880 | 0.000 | 0.880 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.864 | 0.000 | 0.864 | 0 | 6 | plausible_unproven |
| `MECH-279` | mechanism_hypothesis | candidate | 0.905 | 0.000 | 0.905 | 0 | 5 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.875 | 0.000 | 0.875 | 0 | 4 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | candidate | 0.850 | 0.000 | 0.850 | 0 | 14 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.877 | 0.000 | 0.877 | 0 | 16 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.879 | 0.000 | 0.879 | 0 | 5 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.893 | 0.000 | 0.893 | 0 | 11 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.677 | 0.000 | 0.677 | 0 | 1 | plausible_unproven |
| `MECH-292` | mechanism_hypothesis | candidate | 0.903 | 0.000 | 0.903 | 0 | 13 | plausible_unproven |
| `MECH-293` | mechanism_hypothesis | candidate | 0.894 | 0.000 | 0.894 | 0 | 7 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 9 | plausible_unproven |
| `MECH-303` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 4 | plausible_unproven |
| `MECH-304` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 3 | plausible_unproven |
| `MECH-900` | - | - | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.903 | 0.000 | 0.903 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.812 | 0.000 | 0.812 | 0 | 5 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `SD-009` | design_decision | provisional | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.901 | 0.000 | 0.901 | 0 | 4 | plausible_unproven |
| `SD-032d` | - | - | 0.864 | 0.000 | 0.864 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.826 | 0.000 | 0.826 | 0 | 4 | plausible_unproven |
| `SD-033b` | - | - | 0.907 | 0.000 | 0.907 | 0 | 5 | plausible_unproven |
| `SD-033e` | - | - | 0.896 | 0.000 | 0.896 | 0 | 10 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.853 | 0.000 | 0.853 | 0 | 6 | plausible_unproven |
| `SD-036` | design_decision | candidate | 0.828 | 0.000 | 0.828 | 0 | 2 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.867 | 0.000 | 0.867 | 0 | 4 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.840 | 0.000 | 0.840 | 0 | 3 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.757 | 0.000 | 0.757 | 0 | 1 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.684 | 0.253 | 0.828 | 1 | 3 | plausible_unproven |
| `MECH-188` | mechanism_hypothesis | candidate | 0.670 | 0.257 | 0.808 | 1 | 3 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.729 | 0.282 | 0.878 | 1 | 5 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.724 | 0.282 | 0.871 | 1 | 4 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.632 | 0.283 | 0.865 | 2 | 8 | plausible_unproven |
| `MECH-116` | mechanism_hypothesis | candidate | 0.637 | 0.283 | 0.873 | 2 | 7 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.723 | 0.283 | 0.870 | 1 | 4 | plausible_unproven |
| `SD-032c` | - | - | 0.672 | 0.287 | 0.800 | 1 | 3 | plausible_unproven |
| `MECH-091` | mechanism_hypothesis | candidate | 0.711 | 0.288 | 0.852 | 1 | 6 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.661 | 0.307 | 0.897 | 2 | 7 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.649 | 0.309 | 0.876 | 2 | 5 | plausible_unproven |
| `SD-047` | design_decision | provisional | 0.709 | 0.318 | 0.839 | 1 | 10 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.686 | 0.320 | 0.808 | 1 | 11 | plausible_unproven |
| `MECH-295` | mechanism_hypothesis | candidate | 0.741 | 0.325 | 0.880 | 1 | 6 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.746 | 0.373 | 0.870 | 1 | 4 | plausible_unproven |
| `INV-054` | invariant | candidate | 0.622 | 0.386 | 0.858 | 3 | 6 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.640 | 0.387 | 0.894 | 3 | 8 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.751 | 0.397 | 0.869 | 1 | 6 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.754 | 0.397 | 0.873 | 1 | 6 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.755 | 0.400 | 0.874 | 1 | 5 | plausible_unproven |
| `MECH-025` | mechanism_hypothesis | candidate | 0.753 | 0.402 | 0.870 | 1 | 5 | plausible_unproven |
| `MECH-302` | mechanism_hypothesis | candidate | 0.660 | 0.418 | 0.903 | 3 | 6 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.636 | 0.421 | 0.852 | 4 | 7 | plausible_unproven |
| `MECH-099` | mechanism_hypothesis | candidate | 0.662 | 0.425 | 0.900 | 6 | 7 | plausible_unproven |
| `MECH-075` | mechanism_hypothesis | candidate | 0.674 | 0.468 | 0.880 | 5 | 6 | plausible_unproven |
| `MECH-113` | mechanism_hypothesis | candidate | 0.663 | 0.492 | 0.834 | 3 | 3 | plausible_unproven |
| `SD-032b` | - | - | 0.692 | 0.499 | 0.885 | 8 | 14 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.685 | 0.522 | 0.848 | 24 | 9 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.748 | 0.586 | 0.911 | 8 | 10 | plausible_unproven |
| `SD-016` | design_decision | implemented | 0.687 | 0.586 | 0.788 | 7 | 3 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | active | 0.720 | 0.596 | 0.844 | 10 | 24 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.759 | 0.617 | 0.901 | 7 | 14 | plausible_unproven |

_Suppressed by gating: 21 substrate_coherence (ARC + universal invariant), 31 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

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
| `ARC-011` | architectural_commitment | active | 0.781 | 1 |
| `ARC-001` | architectural_commitment | active | 0.691 | 1 |
| `INV-014` | invariant | active | 0.691 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-017` | open_question | active | 0.865 | 11 |
| `Q-016` | open_question | active | 0.856 | 5 |
| `Q-015` | open_question | active | 0.837 | 5 |
| `Q-005` | open_question | active | 0.807 | 4 |
| `Q-020` | open_question | resolved | 0.780 | 6 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **1**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `onboarding` | - | 0.711 | 0.000 | 1 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **37**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-150` | candidate | 0.242 | 1 |
| `MECH-165` | candidate | 0.253 | 1 |
| `MECH-188` | candidate | 0.257 | 1 |
| `MECH-111` | candidate | 0.274 | 2 |
| `MECH-118` | candidate | 0.274 | 2 |
| `MECH-216` | provisional | 0.282 | 1 |
| `SD-023` | candidate | 0.282 | 1 |
| `ARC-032` | candidate | 0.283 | 2 |
| `MECH-116` | candidate | 0.283 | 2 |
| `MECH-220` | candidate | 0.283 | 1 |
| `SD-032c` | - | 0.287 | 1 |
| `MECH-091` | candidate | 0.288 | 1 |
| `MECH-120` | candidate | 0.307 | 2 |
| `MECH-186` | candidate | 0.307 | 2 |
| `MECH-155` | candidate | 0.309 | 2 |
| `SD-047` | provisional | 0.318 | 1 |
| `SD-049` | candidate | 0.320 | 1 |
| `MECH-295` | candidate | 0.325 | 1 |
| `MECH-128` | candidate | 0.342 | 3 |
| `MECH-047` | provisional | 0.373 | 1 |
| `SD-018` | implemented | 0.375 | 2 |
| `INV-054` | candidate | 0.386 | 3 |
| `SD-021` | candidate | 0.387 | 3 |
| `MECH-026` | provisional | 0.397 | 1 |
| `MECH-029` | provisional | 0.397 | 1 |
| `MECH-022` | provisional | 0.400 | 1 |
| `MECH-025` | candidate | 0.402 | 1 |
| `MECH-070` | retiring | 0.416 | 4 |
| `MECH-302` | candidate | 0.418 | 3 |
| `MECH-153` | candidate | 0.421 | 4 |
| ... | ... | ... | ... (7 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **104**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `MECH-265` | candidate | 0.915 | 6 |
| `MECH-263` | candidate | 0.911 | 4 |
| `SD-033b` | - | 0.907 | 5 |
| `MECH-271` | candidate | 0.906 | 4 |
| `MECH-279` | candidate | 0.905 | 5 |
| `MECH-292` | candidate | 0.903 | 13 |
| `MECH-CBBL-PROPOSED` | - | 0.903 | 7 |
| `MECH-163` | candidate | 0.901 | 9 |
| `SD-014` | candidate | 0.901 | 4 |
| `MECH-166` | candidate | 0.900 | 4 |
| `MECH-180` | candidate | 0.897 | 4 |
| `SD-033e` | - | 0.896 | 10 |
| `MECH-122` | provisional | 0.895 | 4 |
| `MECH-293` | candidate | 0.894 | 7 |
| `MECH-267` | provisional | 0.893 | 5 |
| `MECH-288` | candidate | 0.893 | 11 |
| `MECH-030` | provisional | 0.892 | 4 |
| `MECH-172` | candidate | 0.892 | 6 |
| `MECH-191` | candidate | 0.890 | 4 |
| `MECH-074` | provisional | 0.889 | 9 |
| `MECH-092` | candidate | 0.887 | 16 |
| `MECH-046` | provisional | 0.886 | 4 |
| `MECH-272` | candidate | 0.882 | 14 |
| `MECH-171` | candidate | 0.880 | 4 |
| `MECH-273` | candidate | 0.880 | 4 |
| `ARC-060` | candidate | 0.879 | 6 |
| `MECH-287` | candidate | 0.879 | 5 |
| `MECH-294` | candidate | 0.878 | 9 |
| `MECH-285` | candidate | 0.877 | 16 |
| `MECH-168` | candidate | 0.875 | 4 |
| `MECH-269` | candidate | 0.875 | 32 |
| `MECH-280` | candidate | 0.875 | 5 |
| `MECH-281` | candidate | 0.875 | 4 |
| `MECH-203` | candidate | 0.874 | 5 |
| `MECH-303` | candidate | 0.874 | 4 |
| `MECH-264` | candidate | 0.871 | 3 |
| `MECH-121` | candidate | 0.870 | 3 |
| `INV-048` | candidate | 0.867 | 4 |
| `MECH-057b` | - | 0.867 | 4 |
| `SD-003-SUCCESSOR` | - | 0.867 | 4 |
| `SD-037` | candidate | 0.867 | 4 |
| `MECH-275` | candidate | 0.864 | 6 |
| `SD-032d` | - | 0.864 | 4 |
| `MECH-123` | candidate | 0.856 | 5 |
| `MECH-270` | candidate | 0.856 | 4 |
| `MECH-058` | retired | 0.854 | 9 |
| `SD-034` | provisional | 0.853 | 6 |
| `MECH-304` | candidate | 0.852 | 3 |
| `MECH-266` | provisional | 0.851 | 6 |
| `INV-050` | candidate | 0.850 | 3 |
| ... | ... | ... | ... (54 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
