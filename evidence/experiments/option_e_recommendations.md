# Option E shadow recommendations (lit/exp decoupled regime)

Generated: `2026-09-25T05:13:21.958792Z`

**Phase 1 shadow report.** Production governance still uses `overall_confidence` (legacy blend). This report shows what governance would surface under the decoupled regime where `overall = exp_conf` and literature is a parallel signal. **No claim status is changed by this report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for the transition plan.

**Claim-type evidence gating** is applied: `architectural_commitment` and universal `invariant` claims are gated as `substrate_coherence` (foundational design -- no isolated experiment expected); `open_question` claims are gated as `answer_state` (exempt from exp_conf until restated as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only flags fire only for standard-gating claim types. Suppressed claims are reported separately for transparency.

### Gating distribution

| gating | claims |
|---|---:|
| `standard` | 551 |
| `substrate_coherence` | 132 |
| `answer_state` | 86 |

## Quadrant distribution

|  | high exp (>= 0.62) | low exp |
|---|---|---|
| **high lit (>= 0.55)** | confirmed_established: **76** | plausible_unproven: **664** |
| **low lit**             | novel_discovery: **7**         | speculative: **22** |

Total scored claims: 769

## Discrepancy report (regimes disagree on provisional gate)

Claims that cross the `>= 0.62` line under one regime but not the other AND have standard gating. These are the priority items for Phase 2 reckoning -- queue an experiment, adjust status, or flag a new evidence class.

Total: **421** discrepant claims (standard-gating only).

| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |
|---|---|---|---:|---:|---:|---:|---:|---|
| `ARC-031` | architecture_hypothesis | candidate | 0.743 | 0.000 | 0.743 | 0 | 4 | plausible_unproven |
| `ARC-048` | architecture_hypothesis | candidate | 0.740 | 0.000 | 0.740 | 0 | 2 | plausible_unproven |
| `ARC-049` | architecture_hypothesis | candidate | 0.849 | 0.000 | 0.849 | 0 | 26 | plausible_unproven |
| `ARC-050` | architecture_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 3 | plausible_unproven |
| `ARC-051` | architecture_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `ARC-053` | arch_commitment | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `ARC-054` | arch_commitment | candidate | 0.646 | 0.000 | 0.646 | 0 | 3 | plausible_unproven |
| `ARC-055` | arch_commitment | candidate | 0.774 | 0.000 | 0.774 | 0 | 7 | plausible_unproven |
| `ARC-056` | arch_commitment | candidate | 0.723 | 0.000 | 0.723 | 0 | 3 | plausible_unproven |
| `ARC-060` | architecture_hypothesis | candidate | 0.843 | 0.000 | 0.843 | 0 | 13 | plausible_unproven |
| `ARC-073` | architecture_hypothesis | candidate | 0.659 | 0.000 | 0.659 | 0 | 5 | plausible_unproven |
| `ARC-078` | architecture_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 11 | plausible_unproven |
| `ARC-079` | architecture_hypothesis | candidate | 0.633 | 0.000 | 0.633 | 0 | 4 | plausible_unproven |
| `ARC-090` | architecture_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 2 | plausible_unproven |
| `ARC-105` | architecture_hypothesis | candidate | 0.857 | 0.000 | 0.857 | 0 | 4 | plausible_unproven |
| `CANDIDATE-autonomic-rebound-parasympathetic-recovery` | - | - | 0.822 | 0.000 | 0.822 | 0 | 4 | plausible_unproven |
| `CANDIDATE-blocked-agency-stream` | - | - | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `CANDIDATE-contextual-memory-allocation-gate` | - | - | 0.834 | 0.000 | 0.834 | 0 | 5 | plausible_unproven |
| `CDQ-007` | - | - | 0.773 | 0.000 | 0.773 | 0 | 8 | plausible_unproven |
| `CDQ-010` | - | - | 0.872 | 0.000 | 0.872 | 0 | 5 | plausible_unproven |
| `DEV-NEED-007` | - | - | 0.684 | 0.000 | 0.684 | 0 | 1 | plausible_unproven |
| `DEV-NEED-009` | - | - | 0.856 | 0.000 | 0.856 | 0 | 4 | plausible_unproven |
| `DEV-NEED-010` | - | - | 0.694 | 0.000 | 0.694 | 0 | 1 | plausible_unproven |
| `DEV-NEED-012` | - | - | 0.849 | 0.000 | 0.849 | 0 | 6 | plausible_unproven |
| `DEV-NEED-013` | - | - | 0.777 | 0.000 | 0.777 | 0 | 3 | plausible_unproven |
| `DEV-NEED-014` | - | - | 0.794 | 0.000 | 0.794 | 0 | 3 | plausible_unproven |
| `DEV-NEED-015` | - | - | 0.694 | 0.000 | 0.694 | 0 | 1 | plausible_unproven |
| `DEV-NEED-029` | - | - | 0.704 | 0.000 | 0.704 | 0 | 1 | plausible_unproven |
| `EXT-002` | external_failure_mode | candidate | 0.850 | 0.000 | 0.850 | 0 | 5 | plausible_unproven |
| `EXT-003` | external_failure_mode | candidate | 0.757 | 0.000 | 0.757 | 0 | 5 | plausible_unproven |
| `EXT-004` | external_failure_mode | candidate | 0.624 | 0.000 | 0.624 | 0 | 5 | plausible_unproven |
| `EXT-006` | external_failure_mode | candidate | 0.856 | 0.000 | 0.856 | 0 | 5 | plausible_unproven |
| `EXT-008` | external_failure_mode | candidate | 0.825 | 0.000 | 0.825 | 0 | 5 | plausible_unproven |
| `GOV-BEHADJ-1` | governance_rule | candidate | 0.818 | 0.000 | 0.818 | 0 | 9 | plausible_unproven |
| `GOV-CONTRACT-3` | governance_rule | candidate | 0.662 | 0.000 | 0.662 | 0 | 4 | plausible_unproven |
| `GOV-INTERVENE-1` | governance_rule | candidate | 0.729 | 0.000 | 0.729 | 0 | 2 | plausible_unproven |
| `IMPL-026` | reference_note | candidate | 0.814 | 0.000 | 0.814 | 0 | 7 | plausible_unproven |
| `IMPL-027` | reference_note | candidate | 0.835 | 0.000 | 0.835 | 0 | 4 | plausible_unproven |
| `INV-034` | invariant | candidate | 0.821 | 0.000 | 0.821 | 0 | 4 | plausible_unproven |
| `INV-040` | invariant | candidate | 0.672 | 0.000 | 0.672 | 0 | 4 | plausible_unproven |
| `INV-043` | invariant | candidate | 0.808 | 0.000 | 0.808 | 0 | 9 | plausible_unproven |
| `INV-046` | invariant | candidate | 0.673 | 0.000 | 0.673 | 0 | 1 | plausible_unproven |
| `INV-048` | derived_prediction | candidate | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `INV-050` | invariant | candidate | 0.918 | 0.000 | 0.918 | 0 | 8 | plausible_unproven |
| `INV-051` | invariant | candidate | 0.695 | 0.000 | 0.695 | 0 | 2 | plausible_unproven |
| `INV-055` | invariant | candidate | 0.822 | 0.000 | 0.822 | 0 | 5 | plausible_unproven |
| `INV-056` | invariant | candidate | 0.783 | 0.000 | 0.783 | 0 | 3 | plausible_unproven |
| `INV-060` | invariant | candidate | 0.744 | 0.000 | 0.744 | 0 | 2 | plausible_unproven |
| `INV-063` | invariant | candidate | 0.758 | 0.000 | 0.758 | 0 | 9 | plausible_unproven |
| `INV-064` | invariant | candidate | 0.828 | 0.000 | 0.828 | 0 | 5 | plausible_unproven |
| `INV-065` | invariant | candidate | 0.770 | 0.000 | 0.770 | 0 | 3 | plausible_unproven |
| `INV-078` | invariant | candidate | 0.722 | 0.000 | 0.722 | 0 | 1 | plausible_unproven |
| `INV-082` | invariant | candidate | 0.795 | 0.000 | 0.795 | 0 | 4 | plausible_unproven |
| `INV-086` | invariant | candidate | 0.786 | 0.000 | 0.786 | 0 | 3 | plausible_unproven |
| `INV-104` | invariant | candidate | 0.757 | 0.000 | 0.757 | 0 | 6 | plausible_unproven |
| `MECH-002` | mechanism_hypothesis | provisional | 0.852 | 0.000 | 0.852 | 0 | 5 | plausible_unproven |
| `MECH-003` | mechanism_hypothesis | provisional | 0.718 | 0.000 | 0.718 | 0 | 5 | plausible_unproven |
| `MECH-004` | mechanism_hypothesis | candidate | 0.871 | 0.000 | 0.871 | 0 | 5 | plausible_unproven |
| `MECH-005` | mechanism_hypothesis | provisional | 0.739 | 0.000 | 0.739 | 0 | 5 | plausible_unproven |
| `MECH-006` | mechanism_hypothesis | provisional | 0.704 | 0.000 | 0.704 | 0 | 2 | plausible_unproven |
| `MECH-011` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `MECH-012` | mechanism_hypothesis | candidate | 0.626 | 0.000 | 0.626 | 0 | 6 | plausible_unproven |
| `MECH-013` | mechanism_hypothesis | candidate | 0.670 | 0.000 | 0.670 | 0 | 6 | plausible_unproven |
| `MECH-014` | mechanism_hypothesis | candidate | 0.780 | 0.000 | 0.780 | 0 | 5 | plausible_unproven |
| `MECH-016` | mechanism_hypothesis | candidate | 0.756 | 0.000 | 0.756 | 0 | 5 | plausible_unproven |
| `MECH-018` | mechanism_hypothesis | candidate | 0.715 | 0.000 | 0.715 | 0 | 6 | plausible_unproven |
| `MECH-019` | mechanism_hypothesis | candidate | 0.704 | 0.000 | 0.704 | 0 | 5 | plausible_unproven |
| `MECH-021` | mechanism_hypothesis | provisional | 0.806 | 0.000 | 0.806 | 0 | 5 | plausible_unproven |
| `MECH-022` | mechanism_hypothesis | provisional | 0.836 | 0.000 | 0.836 | 0 | 5 | plausible_unproven |
| `MECH-023` | mechanism_hypothesis | provisional | 0.743 | 0.000 | 0.743 | 0 | 5 | plausible_unproven |
| `MECH-024` | mechanism_hypothesis | provisional | 0.801 | 0.000 | 0.801 | 0 | 5 | plausible_unproven |
| `MECH-026` | mechanism_hypothesis | provisional | 0.830 | 0.000 | 0.830 | 0 | 6 | plausible_unproven |
| `MECH-028` | mechanism_hypothesis | provisional | 0.814 | 0.000 | 0.814 | 0 | 5 | plausible_unproven |
| `MECH-030` | mechanism_hypothesis | provisional | 0.854 | 0.000 | 0.854 | 0 | 4 | plausible_unproven |
| `MECH-034` | mechanism_hypothesis | provisional | 0.772 | 0.000 | 0.772 | 0 | 5 | plausible_unproven |
| `MECH-035` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 6 | plausible_unproven |
| `MECH-037` | mechanism_hypothesis | candidate | 0.697 | 0.000 | 0.697 | 0 | 5 | plausible_unproven |
| `MECH-038` | mechanism_hypothesis | candidate | 0.854 | 0.000 | 0.854 | 0 | 5 | plausible_unproven |
| `MECH-039` | mechanism_hypothesis | provisional | 0.826 | 0.000 | 0.826 | 0 | 5 | plausible_unproven |
| `MECH-040` | mechanism_hypothesis | provisional | 0.694 | 0.000 | 0.694 | 0 | 1 | plausible_unproven |
| `MECH-042` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 5 | plausible_unproven |
| `MECH-043` | mechanism_hypothesis | provisional | 0.770 | 0.000 | 0.770 | 0 | 5 | plausible_unproven |
| `MECH-044` | mechanism_hypothesis | provisional | 0.823 | 0.000 | 0.823 | 0 | 6 | plausible_unproven |
| `MECH-046` | mechanism_hypothesis | provisional | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `MECH-047` | mechanism_hypothesis | provisional | 0.831 | 0.000 | 0.831 | 0 | 4 | plausible_unproven |
| `MECH-048` | mechanism_hypothesis | provisional | 0.819 | 0.000 | 0.819 | 0 | 4 | plausible_unproven |
| `MECH-049` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `MECH-050` | mechanism_hypothesis | candidate | 0.800 | 0.000 | 0.800 | 0 | 5 | plausible_unproven |
| `MECH-053` | mechanism_hypothesis | provisional | 0.873 | 0.000 | 0.873 | 0 | 6 | plausible_unproven |
| `MECH-054` | mechanism_hypothesis | provisional | 0.782 | 0.000 | 0.782 | 0 | 2 | plausible_unproven |
| `MECH-055` | mechanism_hypothesis | candidate | 0.673 | 0.000 | 0.673 | 0 | 5 | plausible_unproven |
| `MECH-057` | mechanism_hypothesis | candidate | 0.783 | 0.000 | 0.783 | 0 | 5 | plausible_unproven |
| `MECH-057b` | - | - | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `MECH-058` | mechanism_hypothesis | retired | 0.804 | 0.000 | 0.804 | 0 | 4 | plausible_unproven |
| `MECH-064` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 5 | plausible_unproven |
| `MECH-065` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 5 | plausible_unproven |
| `MECH-066` | mechanism_hypothesis | candidate | 0.867 | 0.000 | 0.867 | 0 | 5 | plausible_unproven |
| `MECH-067` | mechanism_hypothesis | provisional | 0.724 | 0.000 | 0.724 | 0 | 5 | plausible_unproven |
| `MECH-077` | mechanism_hypothesis | candidate | 0.735 | 0.000 | 0.735 | 0 | 2 | plausible_unproven |
| `MECH-079` | mechanism_hypothesis | candidate | 0.657 | 0.000 | 0.657 | 0 | 5 | plausible_unproven |
| `MECH-080` | mechanism_hypothesis | unassigned_pending_evidence | 0.681 | 0.000 | 0.681 | 0 | 5 | plausible_unproven |
| `MECH-082` | mechanism_hypothesis | candidate | 0.767 | 0.000 | 0.767 | 0 | 5 | plausible_unproven |
| `MECH-083` | mechanism_hypothesis | candidate | 0.861 | 0.000 | 0.861 | 0 | 4 | plausible_unproven |
| `MECH-085` | mechanism_hypothesis | candidate | 0.725 | 0.000 | 0.725 | 0 | 3 | plausible_unproven |
| `MECH-088` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 3 | plausible_unproven |
| `MECH-092` | mechanism_hypothesis | candidate | 0.878 | 0.000 | 0.878 | 0 | 15 | plausible_unproven |
| `MECH-096` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 2 | plausible_unproven |
| `MECH-103` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `MECH-121` | mechanism_hypothesis | candidate | 0.894 | 0.000 | 0.894 | 0 | 5 | plausible_unproven |
| `MECH-123` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 5 | plausible_unproven |
| `MECH-129` | mechanism_hypothesis | candidate | 0.821 | 0.000 | 0.821 | 0 | 8 | plausible_unproven |
| `MECH-130` | mechanism_hypothesis | candidate | 0.673 | 0.000 | 0.673 | 0 | 5 | plausible_unproven |
| `MECH-140` | mechanism_hypothesis | candidate | 0.672 | 0.000 | 0.672 | 0 | 2 | plausible_unproven |
| `MECH-141` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 4 | plausible_unproven |
| `MECH-142` | mechanism_hypothesis | candidate | 0.661 | 0.000 | 0.661 | 0 | 1 | plausible_unproven |
| `MECH-143` | mechanism_hypothesis | candidate | 0.651 | 0.000 | 0.651 | 0 | 5 | plausible_unproven |
| `MECH-147` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `MECH-148` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-149` | mechanism_hypothesis | candidate | 0.692 | 0.000 | 0.692 | 0 | 1 | plausible_unproven |
| `MECH-151` | mechanism_hypothesis | candidate | 0.805 | 0.000 | 0.805 | 0 | 4 | plausible_unproven |
| `MECH-154` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `MECH-164` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 3 | plausible_unproven |
| `MECH-165` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 3 | plausible_unproven |
| `MECH-168` | mechanism_hypothesis | candidate | 0.837 | 0.000 | 0.837 | 0 | 4 | plausible_unproven |
| `MECH-169` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 2 | plausible_unproven |
| `MECH-171` | derived_prediction | candidate | 0.842 | 0.000 | 0.842 | 0 | 4 | plausible_unproven |
| `MECH-172` | derived_prediction | candidate | 0.853 | 0.000 | 0.853 | 0 | 6 | plausible_unproven |
| `MECH-173` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 2 | plausible_unproven |
| `MECH-174` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 2 | plausible_unproven |
| `MECH-175` | mechanism_hypothesis | candidate | 0.788 | 0.000 | 0.788 | 0 | 3 | plausible_unproven |
| `MECH-176` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 3 | plausible_unproven |
| `MECH-177` | mechanism_hypothesis | candidate | 0.730 | 0.000 | 0.730 | 0 | 2 | plausible_unproven |
| `MECH-178` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 3 | plausible_unproven |
| `MECH-179` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 3 | plausible_unproven |
| `MECH-181` | mechanism_hypothesis | candidate | 0.678 | 0.000 | 0.678 | 0 | 2 | plausible_unproven |
| `MECH-182` | mechanism_hypothesis | candidate | 0.703 | 0.000 | 0.703 | 0 | 3 | plausible_unproven |
| `MECH-183` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 5 | plausible_unproven |
| `MECH-184` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 3 | plausible_unproven |
| `MECH-185` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 4 | plausible_unproven |
| `MECH-186` | mechanism_hypothesis | candidate | 0.734 | 0.000 | 0.734 | 0 | 3 | plausible_unproven |
| `MECH-191` | mechanism_hypothesis | candidate | 0.852 | 0.000 | 0.852 | 0 | 4 | plausible_unproven |
| `MECH-192` | mechanism_hypothesis | candidate | 0.781 | 0.000 | 0.781 | 0 | 3 | plausible_unproven |
| `MECH-193` | mechanism_hypothesis | candidate | 0.773 | 0.000 | 0.773 | 0 | 3 | plausible_unproven |
| `MECH-194` | mechanism_hypothesis | candidate | 0.721 | 0.000 | 0.721 | 0 | 2 | plausible_unproven |
| `MECH-195` | mechanism_hypothesis | candidate | 0.689 | 0.000 | 0.689 | 0 | 2 | plausible_unproven |
| `MECH-196` | mechanism_hypothesis | candidate | 0.699 | 0.000 | 0.699 | 0 | 2 | plausible_unproven |
| `MECH-197` | mechanism_hypothesis | candidate | 0.838 | 0.000 | 0.838 | 0 | 12 | plausible_unproven |
| `MECH-198` | mechanism_hypothesis | candidate | 0.841 | 0.000 | 0.841 | 0 | 8 | plausible_unproven |
| `MECH-200` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `MECH-201` | mechanism_hypothesis | candidate | 0.739 | 0.000 | 0.739 | 0 | 2 | plausible_unproven |
| `MECH-203` | mechanism_hypothesis | candidate | 0.863 | 0.000 | 0.863 | 0 | 8 | plausible_unproven |
| `MECH-207` | mechanism_hypothesis | candidate | 0.722 | 0.000 | 0.722 | 0 | 2 | plausible_unproven |
| `MECH-214` | mechanism | candidate | 0.682 | 0.000 | 0.682 | 0 | 2 | plausible_unproven |
| `MECH-215` | mechanism | candidate | 0.800 | 0.000 | 0.800 | 0 | 5 | plausible_unproven |
| `MECH-217` | mechanism | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `MECH-220` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 4 | plausible_unproven |
| `MECH-236` | mechanism_hypothesis | candidate | 0.812 | 0.000 | 0.812 | 0 | 4 | plausible_unproven |
| `MECH-244` | mechanism_hypothesis | candidate | 0.741 | 0.000 | 0.741 | 0 | 2 | plausible_unproven |
| `MECH-254` | mechanism_hypothesis | candidate | 0.672 | 0.000 | 0.672 | 0 | 2 | plausible_unproven |
| `MECH-256` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 9 | plausible_unproven |
| `MECH-257` | mechanism_hypothesis | candidate | 0.733 | 0.000 | 0.733 | 0 | 2 | plausible_unproven |
| `MECH-260` | mechanism_hypothesis | candidate | 0.677 | 0.000 | 0.677 | 0 | 1 | plausible_unproven |
| `MECH-263` | mechanism_hypothesis | candidate | 0.873 | 0.000 | 0.873 | 0 | 4 | plausible_unproven |
| `MECH-264` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 5 | plausible_unproven |
| `MECH-265` | mechanism_hypothesis | candidate | 0.851 | 0.000 | 0.851 | 0 | 6 | plausible_unproven |
| `MECH-266` | mechanism_hypothesis | provisional | 0.850 | 0.000 | 0.850 | 0 | 7 | plausible_unproven |
| `MECH-267` | mechanism_hypothesis | provisional | 0.855 | 0.000 | 0.855 | 0 | 5 | plausible_unproven |
| `MECH-269` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 34 | plausible_unproven |
| `MECH-269b` | - | - | 0.803 | 0.000 | 0.803 | 0 | 7 | plausible_unproven |
| `MECH-270` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 4 | plausible_unproven |
| `MECH-271` | mechanism_hypothesis | candidate | 0.868 | 0.000 | 0.868 | 0 | 4 | plausible_unproven |
| `MECH-275` | mechanism_hypothesis | candidate | 0.844 | 0.000 | 0.844 | 0 | 7 | plausible_unproven |
| `MECH-280` | mechanism_hypothesis | candidate | 0.837 | 0.000 | 0.837 | 0 | 5 | plausible_unproven |
| `MECH-281` | mechanism_hypothesis | candidate | 0.836 | 0.000 | 0.836 | 0 | 4 | plausible_unproven |
| `MECH-282` | mechanism_hypothesis | candidate | 0.816 | 0.000 | 0.816 | 0 | 3 | plausible_unproven |
| `MECH-287` | mechanism_hypothesis | candidate | 0.825 | 0.000 | 0.825 | 0 | 7 | plausible_unproven |
| `MECH-288` | mechanism_hypothesis | candidate | 0.855 | 0.000 | 0.855 | 0 | 11 | plausible_unproven |
| `MECH-289` | mechanism_hypothesis | candidate | 0.812 | 0.000 | 0.812 | 0 | 4 | plausible_unproven |
| `MECH-291` | mechanism_hypothesis | candidate | 0.638 | 0.000 | 0.638 | 0 | 1 | plausible_unproven |
| `MECH-294` | mechanism_hypothesis | candidate | 0.839 | 0.000 | 0.839 | 0 | 9 | plausible_unproven |
| `MECH-299` | mechanism_hypothesis | candidate | 0.784 | 0.000 | 0.784 | 0 | 2 | plausible_unproven |
| `MECH-302` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 7 | plausible_unproven |
| `MECH-305` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 3 | plausible_unproven |
| `MECH-307` | mechanism_hypothesis | candidate_substrate_landed | 0.870 | 0.000 | 0.870 | 0 | 6 | plausible_unproven |
| `MECH-312` | mechanism_hypothesis | candidate | 0.828 | 0.000 | 0.828 | 0 | 14 | plausible_unproven |
| `MECH-313` | mechanism_hypothesis | candidate | 0.874 | 0.000 | 0.874 | 0 | 6 | plausible_unproven |
| `MECH-314c` | - | - | 0.858 | 0.000 | 0.858 | 0 | 6 | plausible_unproven |
| `MECH-316` | mechanism_hypothesis | candidate | 0.846 | 0.000 | 0.846 | 0 | 9 | plausible_unproven |
| `MECH-317` | mechanism_hypothesis | candidate | 0.860 | 0.000 | 0.860 | 0 | 6 | plausible_unproven |
| `MECH-318` | mechanism_hypothesis | candidate | 0.789 | 0.000 | 0.789 | 0 | 6 | plausible_unproven |
| `MECH-320` | mechanism_hypothesis | candidate_substrate_landed | 0.863 | 0.000 | 0.863 | 0 | 5 | plausible_unproven |
| `MECH-332` | mechanism_hypothesis | candidate | 0.724 | 0.000 | 0.724 | 0 | 1 | plausible_unproven |
| `MECH-333` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 6 | plausible_unproven |
| `MECH-334` | mechanism_hypothesis | candidate | 0.840 | 0.000 | 0.840 | 0 | 3 | plausible_unproven |
| `MECH-337` | mechanism_hypothesis | candidate | 0.842 | 0.000 | 0.842 | 0 | 4 | plausible_unproven |
| `MECH-338` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 3 | plausible_unproven |
| `MECH-339` | mechanism_hypothesis | candidate | 0.662 | 0.000 | 0.662 | 0 | 2 | plausible_unproven |
| `MECH-340` | mechanism_hypothesis | candidate | 0.677 | 0.000 | 0.677 | 0 | 2 | plausible_unproven |
| `MECH-342` | mechanism_hypothesis | candidate | 0.807 | 0.000 | 0.807 | 0 | 4 | plausible_unproven |
| `MECH-353` | mechanism_hypothesis | candidate | 0.824 | 0.000 | 0.824 | 0 | 5 | plausible_unproven |
| `MECH-354` | mechanism_hypothesis | candidate | 0.866 | 0.000 | 0.866 | 0 | 5 | plausible_unproven |
| `MECH-355` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `MECH-356` | mechanism_hypothesis | candidate | 0.822 | 0.000 | 0.822 | 0 | 4 | plausible_unproven |
| `MECH-357` | mechanism_hypothesis | candidate | 0.754 | 0.000 | 0.754 | 0 | 3 | plausible_unproven |
| `MECH-359` | mechanism_hypothesis | candidate | 0.783 | 0.000 | 0.783 | 0 | 3 | plausible_unproven |
| `MECH-360` | mechanism_hypothesis | candidate | 0.682 | 0.000 | 0.682 | 0 | 2 | plausible_unproven |
| `MECH-361` | mechanism_hypothesis | candidate | 0.768 | 0.000 | 0.768 | 0 | 3 | plausible_unproven |
| `MECH-364` | mechanism_hypothesis | candidate | 0.642 | 0.000 | 0.642 | 0 | 2 | plausible_unproven |
| `MECH-366` | mechanism_hypothesis | candidate | 0.802 | 0.000 | 0.802 | 0 | 5 | plausible_unproven |
| `MECH-368` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 2 | plausible_unproven |
| `MECH-371` | mechanism_hypothesis | candidate | 0.681 | 0.000 | 0.681 | 0 | 1 | plausible_unproven |
| `MECH-372` | mechanism_hypothesis | candidate | 0.798 | 0.000 | 0.798 | 0 | 3 | plausible_unproven |
| `MECH-380` | mechanism_hypothesis | candidate | 0.712 | 0.000 | 0.712 | 0 | 2 | plausible_unproven |
| `MECH-381` | mechanism_hypothesis | candidate | 0.712 | 0.000 | 0.712 | 0 | 2 | plausible_unproven |
| `MECH-382` | mechanism_hypothesis | candidate | 0.682 | 0.000 | 0.682 | 0 | 1 | plausible_unproven |
| `MECH-383` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 2 | plausible_unproven |
| `MECH-385` | mechanism_hypothesis | candidate | 0.672 | 0.000 | 0.672 | 0 | 1 | plausible_unproven |
| `MECH-388` | mechanism_hypothesis | candidate | 0.672 | 0.000 | 0.672 | 0 | 1 | plausible_unproven |
| `MECH-391` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 6 | plausible_unproven |
| `MECH-394` | mechanism_hypothesis | candidate | 0.827 | 0.000 | 0.827 | 0 | 4 | plausible_unproven |
| `MECH-398` | mechanism_hypothesis | candidate | 0.818 | 0.000 | 0.818 | 0 | 3 | plausible_unproven |
| `MECH-399` | mechanism_hypothesis | candidate | 0.723 | 0.000 | 0.723 | 0 | 1 | plausible_unproven |
| `MECH-405` | mechanism_hypothesis | candidate | 0.654 | 0.000 | 0.654 | 0 | 5 | plausible_unproven |
| `MECH-408` | mechanism_hypothesis | candidate | 0.658 | 0.000 | 0.658 | 0 | 1 | plausible_unproven |
| `MECH-411` | mechanism_hypothesis | candidate | 0.691 | 0.000 | 0.691 | 0 | 1 | plausible_unproven |
| `MECH-426` | mechanism | candidate | 0.726 | 0.000 | 0.726 | 0 | 2 | plausible_unproven |
| `MECH-428` | mechanism | candidate | 0.737 | 0.000 | 0.737 | 0 | 3 | plausible_unproven |
| `MECH-429` | mechanism_hypothesis | candidate | 0.707 | 0.000 | 0.707 | 0 | 1 | plausible_unproven |
| `MECH-432` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 3 | plausible_unproven |
| `MECH-433` | mechanism_hypothesis | candidate | 0.622 | 0.000 | 0.622 | 0 | 1 | plausible_unproven |
| `MECH-434` | mechanism_hypothesis | candidate | 0.837 | 0.000 | 0.837 | 0 | 4 | plausible_unproven |
| `MECH-435` | mechanism_hypothesis | candidate | 0.672 | 0.000 | 0.672 | 0 | 1 | plausible_unproven |
| `MECH-439` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 7 | plausible_unproven |
| `MECH-441` | mechanism_hypothesis | candidate | 0.683 | 0.000 | 0.683 | 0 | 1 | plausible_unproven |
| `MECH-442` | mechanism_hypothesis | candidate | 0.750 | 0.000 | 0.750 | 0 | 5 | plausible_unproven |
| `MECH-443` | mechanism_hypothesis | candidate | 0.795 | 0.000 | 0.795 | 0 | 5 | plausible_unproven |
| `MECH-444` | mechanism_hypothesis | candidate | 0.763 | 0.000 | 0.763 | 0 | 3 | plausible_unproven |
| `MECH-446` | mechanism_hypothesis | candidate | 0.737 | 0.000 | 0.737 | 0 | 3 | plausible_unproven |
| `MECH-448` | mechanism_hypothesis | candidate | 0.831 | 0.000 | 0.831 | 0 | 5 | plausible_unproven |
| `MECH-450` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 5 | plausible_unproven |
| `MECH-451` | mechanism_hypothesis | candidate | 0.765 | 0.000 | 0.765 | 0 | 4 | plausible_unproven |
| `MECH-452` | mechanism_hypothesis | candidate | 0.832 | 0.000 | 0.832 | 0 | 4 | plausible_unproven |
| `MECH-453` | mechanism_hypothesis | candidate | 0.803 | 0.000 | 0.803 | 0 | 3 | plausible_unproven |
| `MECH-454` | mechanism_hypothesis | candidate | 0.791 | 0.000 | 0.791 | 0 | 5 | plausible_unproven |
| `MECH-459` | mechanism_hypothesis | candidate | 0.783 | 0.000 | 0.783 | 0 | 3 | plausible_unproven |
| `MECH-467` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 3 | plausible_unproven |
| `MECH-471` | mechanism_hypothesis | candidate | 0.814 | 0.000 | 0.814 | 0 | 3 | plausible_unproven |
| `MECH-472` | mechanism_hypothesis | candidate | 0.843 | 0.000 | 0.843 | 0 | 4 | plausible_unproven |
| `MECH-480` | mechanism_hypothesis | candidate | 0.677 | 0.000 | 0.677 | 0 | 1 | plausible_unproven |
| `MECH-481` | mechanism_hypothesis | candidate | 0.785 | 0.000 | 0.785 | 0 | 4 | plausible_unproven |
| `MECH-486` | mechanism_hypothesis | candidate | 0.776 | 0.000 | 0.776 | 0 | 2 | plausible_unproven |
| `MECH-487` | mechanism_hypothesis | candidate | 0.817 | 0.000 | 0.817 | 0 | 5 | plausible_unproven |
| `MECH-489` | mechanism_hypothesis | candidate | 0.819 | 0.000 | 0.819 | 0 | 5 | plausible_unproven |
| `MECH-490` | mechanism_hypothesis | candidate | 0.778 | 0.000 | 0.778 | 0 | 4 | plausible_unproven |
| `MECH-499` | mechanism_hypothesis | candidate | 0.733 | 0.000 | 0.733 | 0 | 3 | plausible_unproven |
| `MECH-500` | mechanism_hypothesis | candidate | 0.674 | 0.000 | 0.674 | 0 | 2 | plausible_unproven |
| `MECH-501` | mechanism_hypothesis | candidate | 0.625 | 0.000 | 0.625 | 0 | 5 | plausible_unproven |
| `MECH-503` | mechanism_hypothesis | candidate | 0.833 | 0.000 | 0.833 | 0 | 4 | plausible_unproven |
| `MECH-514` | mechanism_hypothesis | candidate | 0.629 | 0.000 | 0.629 | 0 | 2 | plausible_unproven |
| `MECH-520` | mechanism_hypothesis | candidate | 0.796 | 0.000 | 0.796 | 0 | 4 | plausible_unproven |
| `MECH-521` | mechanism_hypothesis | candidate | 0.802 | 0.000 | 0.802 | 0 | 4 | plausible_unproven |
| `MECH-522` | mechanism_hypothesis | candidate | 0.722 | 0.000 | 0.722 | 0 | 2 | plausible_unproven |
| `MECH-524` | mechanism_hypothesis | candidate | 0.820 | 0.000 | 0.820 | 0 | 10 | plausible_unproven |
| `MECH-525` | mechanism_hypothesis | candidate | 0.683 | 0.000 | 0.683 | 0 | 1 | plausible_unproven |
| `MECH-526` | mechanism_hypothesis | candidate | 0.693 | 0.000 | 0.693 | 0 | 1 | plausible_unproven |
| `MECH-527` | mechanism_hypothesis | candidate | 0.885 | 0.000 | 0.885 | 0 | 4 | plausible_unproven |
| `MECH-529` | mechanism_hypothesis | candidate | 0.761 | 0.000 | 0.761 | 0 | 3 | plausible_unproven |
| `MECH-533` | mechanism_hypothesis | candidate | 0.847 | 0.000 | 0.847 | 0 | 4 | plausible_unproven |
| `MECH-534` | mechanism_hypothesis | candidate | 0.732 | 0.000 | 0.732 | 0 | 3 | plausible_unproven |
| `MECH-535` | mechanism_hypothesis | candidate | 0.700 | 0.000 | 0.700 | 0 | 11 | plausible_unproven |
| `MECH-536` | mechanism_hypothesis | candidate | 0.708 | 0.000 | 0.708 | 0 | 6 | plausible_unproven |
| `MECH-537` | mechanism_hypothesis | candidate | 0.771 | 0.000 | 0.771 | 0 | 3 | plausible_unproven |
| `MECH-539` | mechanism_hypothesis | candidate | 0.646 | 0.000 | 0.646 | 0 | 1 | plausible_unproven |
| `MECH-541` | mechanism_hypothesis | candidate | 0.793 | 0.000 | 0.793 | 0 | 4 | plausible_unproven |
| `MECH-542` | mechanism_hypothesis | candidate | 0.809 | 0.000 | 0.809 | 0 | 5 | plausible_unproven |
| `MECH-544` | mechanism_hypothesis | candidate | 0.738 | 0.000 | 0.738 | 0 | 2 | plausible_unproven |
| `MECH-545` | mechanism_hypothesis | candidate | 0.790 | 0.000 | 0.790 | 0 | 12 | plausible_unproven |
| `MECH-547` | mechanism_hypothesis | candidate | 0.794 | 0.000 | 0.794 | 0 | 4 | plausible_unproven |
| `MECH-548` | mechanism_hypothesis | candidate | 0.701 | 0.000 | 0.701 | 0 | 3 | plausible_unproven |
| `MECH-553` | mechanism_hypothesis | candidate | 0.678 | 0.000 | 0.678 | 0 | 1 | plausible_unproven |
| `MECH-560` | mechanism_hypothesis | candidate | 0.623 | 0.000 | 0.623 | 0 | 1 | plausible_unproven |
| `MECH-561` | mechanism_hypothesis | candidate | 0.661 | 0.000 | 0.661 | 0 | 2 | plausible_unproven |
| `MECH-562` | mechanism_hypothesis | candidate | 0.678 | 0.000 | 0.678 | 0 | 1 | plausible_unproven |
| `MECH-569` | mechanism_hypothesis | candidate | 0.753 | 0.000 | 0.753 | 0 | 2 | plausible_unproven |
| `MECH-570` | mechanism_hypothesis | candidate | 0.648 | 0.000 | 0.648 | 0 | 1 | plausible_unproven |
| `MECH-572` | mechanism_hypothesis | candidate | 0.835 | 0.000 | 0.835 | 0 | 4 | plausible_unproven |
| `MECH-573` | mechanism_hypothesis | candidate | 0.749 | 0.000 | 0.749 | 0 | 2 | plausible_unproven |
| `MECH-900` | - | - | 0.659 | 0.000 | 0.659 | 0 | 1 | plausible_unproven |
| `MECH-CBBL-PROPOSED` | - | - | 0.865 | 0.000 | 0.865 | 0 | 7 | plausible_unproven |
| `MECH-E2-DUAL-FUNCTION` | - | - | 0.773 | 0.000 | 0.773 | 0 | 5 | plausible_unproven |
| `Q-035` | question | resolved | 0.865 | 0.000 | 0.865 | 0 | 15 | plausible_unproven |
| `Q-046` | - | - | 0.734 | 0.000 | 0.734 | 0 | 2 | plausible_unproven |
| `Q-053` | question | open | 0.837 | 0.000 | 0.837 | 0 | 7 | plausible_unproven |
| `SD-003-SUCCESSOR` | - | - | 0.829 | 0.000 | 0.829 | 0 | 4 | plausible_unproven |
| `SD-018` | substrate_decision | implemented | 0.715 | 0.000 | 0.715 | 0 | 2 | plausible_unproven |
| `SD-021` | design_decision | candidate | 0.865 | 0.000 | 0.865 | 0 | 9 | plausible_unproven |
| `SD-025` | design_decision | candidate | 0.777 | 0.000 | 0.777 | 0 | 3 | plausible_unproven |
| `SD-027` | design_decision | candidate | 0.672 | 0.000 | 0.672 | 0 | 2 | plausible_unproven |
| `SD-029` | design_decision | candidate | 0.825 | 0.000 | 0.825 | 0 | 12 | plausible_unproven |
| `SD-030` | design_decision | candidate | 0.803 | 0.000 | 0.803 | 0 | 4 | plausible_unproven |
| `SD-032` | design_decision | stable | 0.859 | 0.000 | 0.859 | 0 | 9 | plausible_unproven |
| `SD-032b` | - | - | 0.847 | 0.000 | 0.847 | 0 | 14 | plausible_unproven |
| `SD-032c` | - | - | 0.761 | 0.000 | 0.761 | 0 | 3 | plausible_unproven |
| `SD-032d` | - | - | 0.826 | 0.000 | 0.826 | 0 | 4 | plausible_unproven |
| `SD-032e` | - | - | 0.788 | 0.000 | 0.788 | 0 | 4 | plausible_unproven |
| `SD-033` | design_decision | candidate | 0.857 | 0.000 | 0.857 | 0 | 7 | plausible_unproven |
| `SD-033b` | - | - | 0.869 | 0.000 | 0.869 | 0 | 5 | plausible_unproven |
| `SD-033c` | - | - | 0.764 | 0.000 | 0.764 | 0 | 2 | plausible_unproven |
| `SD-033d` | - | - | 0.697 | 0.000 | 0.697 | 0 | 1 | plausible_unproven |
| `SD-033e` | - | - | 0.856 | 0.000 | 0.856 | 0 | 9 | plausible_unproven |
| `SD-035` | design_decision | stable | 0.844 | 0.000 | 0.844 | 0 | 6 | plausible_unproven |
| `SD-037` | design_decision | candidate | 0.893 | 0.000 | 0.893 | 0 | 7 | plausible_unproven |
| `SD-038` | design_decision | candidate | 0.708 | 0.000 | 0.708 | 0 | 1 | plausible_unproven |
| `SD-039` | design_decision | candidate | 0.859 | 0.000 | 0.859 | 0 | 7 | plausible_unproven |
| `SD-040` | design_decision | candidate | 0.719 | 0.000 | 0.719 | 0 | 1 | plausible_unproven |
| `SD-042` | design_decision | candidate | 0.759 | 0.000 | 0.759 | 0 | 2 | plausible_unproven |
| `SD-045` | design_decision | candidate | 0.890 | 0.000 | 0.890 | 0 | 4 | plausible_unproven |
| `SD-046` | design_decision | candidate | 0.793 | 0.000 | 0.793 | 0 | 6 | plausible_unproven |
| `SD-048` | design_decision | candidate | 0.847 | 0.000 | 0.847 | 0 | 6 | plausible_unproven |
| `SD-049` | design_decision | candidate | 0.770 | 0.000 | 0.770 | 0 | 11 | plausible_unproven |
| `SD-050` | design_decision | provisional | 0.639 | 0.000 | 0.639 | 0 | 4 | plausible_unproven |
| `SD-054` | design_decision | candidate | 0.844 | 0.000 | 0.844 | 0 | 7 | plausible_unproven |
| `SD-055` | design_decision | candidate | 0.745 | 0.000 | 0.745 | 0 | 2 | plausible_unproven |
| `SD-060` | design_decision | candidate | 0.727 | 0.000 | 0.727 | 0 | 2 | plausible_unproven |
| `SD-068` | design_decision | candidate | 0.785 | 0.000 | 0.785 | 0 | 4 | plausible_unproven |
| `SD-069` | design_decision | candidate | 0.791 | 0.000 | 0.791 | 0 | 3 | plausible_unproven |
| `SD-076` | design_decision | candidate | 0.627 | 0.000 | 0.627 | 0 | 8 | plausible_unproven |
| `SD-078` | design_decision | candidate_substrate_landed | 0.754 | 0.000 | 0.754 | 0 | 2 | plausible_unproven |
| `SD-080` | design_decision | candidate | 0.790 | 0.000 | 0.790 | 0 | 3 | plausible_unproven |
| `SD-081` | design_decision | candidate | 0.698 | 0.000 | 0.698 | 0 | 1 | plausible_unproven |
| `SD-082` | design_decision | candidate_substrate_landed | 0.826 | 0.000 | 0.826 | 0 | 8 | plausible_unproven |
| `SD-091` | design_decision | candidate | 0.770 | 0.000 | 0.770 | 0 | 5 | plausible_unproven |
| `SD-092` | design_decision | candidate | 0.679 | 0.000 | 0.679 | 0 | 2 | plausible_unproven |
| `SD-097` | substrate_design | candidate | 0.732 | 0.000 | 0.732 | 0 | 5 | plausible_unproven |
| `SD-099` | design_decision | candidate | 0.773 | 0.000 | 0.773 | 0 | 4 | plausible_unproven |
| `SD-101` | design_decision | candidate | 0.810 | 0.000 | 0.810 | 0 | 5 | plausible_unproven |
| `SD-106` | design_decision | implemented | 0.849 | 0.000 | 0.849 | 0 | 5 | plausible_unproven |
| `MECH-155` | mechanism_hypothesis | candidate | 0.654 | 0.105 | 0.837 | 1 | 5 | plausible_unproven |
| `INV-054` | invariant | candidate | 0.645 | 0.125 | 0.819 | 1 | 6 | plausible_unproven |
| `SD-023` | design_decision | candidate | 0.655 | 0.125 | 0.832 | 1 | 4 | plausible_unproven |
| `SD-047` | design_decision | candidate | 0.632 | 0.125 | 0.801 | 1 | 10 | plausible_unproven |
| `INV-088` | invariant | candidate | 0.644 | 0.159 | 0.806 | 1 | 6 | plausible_unproven |
| `MECH-457` | mechanism_hypothesis | candidate | 0.653 | 0.160 | 0.817 | 1 | 21 | plausible_unproven |
| `MECH-329` | mechanism_hypothesis | candidate | 0.624 | 0.182 | 0.771 | 1 | 5 | plausible_unproven |
| `MECH-475` | mechanism_hypothesis | retired | 0.646 | 0.197 | 0.796 | 1 | 5 | plausible_unproven |
| `SD-087` | design_decision | candidate | 0.658 | 0.203 | 0.810 | 1 | 4 | plausible_unproven |
| `MECH-025b` | - | - | 0.636 | 0.207 | 0.779 | 1 | 4 | plausible_unproven |
| `MECH-122` | mechanism_hypothesis | provisional | 0.700 | 0.207 | 0.864 | 1 | 4 | plausible_unproven |
| `MECH-166` | mechanism_hypothesis | candidate | 0.716 | 0.207 | 0.886 | 1 | 5 | plausible_unproven |
| `SD-009` | design_decision | candidate | 0.625 | 0.219 | 0.760 | 1 | 3 | plausible_unproven |
| `MECH-144` | mechanism_hypothesis | candidate | 0.665 | 0.266 | 0.798 | 1 | 4 | plausible_unproven |
| `MECH-029` | mechanism_hypothesis | provisional | 0.694 | 0.275 | 0.834 | 1 | 6 | plausible_unproven |
| `MECH-258` | mechanism_hypothesis | candidate | 0.702 | 0.280 | 0.843 | 1 | 9 | plausible_unproven |
| `MECH-180` | mechanism_hypothesis | candidate | 0.772 | 0.359 | 0.910 | 1 | 7 | plausible_unproven |
| `ARC-030` | architecture_hypothesis | candidate | 0.620 | 0.368 | 0.872 | 3 | 10 | plausible_unproven |
| `MECH-216` | mechanism | provisional | 0.659 | 0.390 | 0.839 | 2 | 5 | plausible_unproven |
| `MECH-095` | mechanism_hypothesis | candidate | 0.637 | 0.425 | 0.850 | 8 | 26 | plausible_unproven |
| `ARC-032` | architecture_hypothesis | candidate | 0.625 | 0.427 | 0.823 | 5 | 6 | plausible_unproven |
| `MECH-098` | mechanism_hypothesis | candidate | 0.672 | 0.438 | 0.906 | 18 | 12 | plausible_unproven |
| `SD-012` | design_decision | provisional | 0.637 | 0.442 | 0.833 | 3 | 25 | plausible_unproven |
| `MECH-102` | mechanism_hypothesis | active | 0.631 | 0.453 | 0.809 | 18 | 8 | plausible_unproven |
| `MECH-163` | mechanism_hypothesis | candidate | 0.697 | 0.462 | 0.853 | 2 | 14 | plausible_unproven |
| `MECH-017` | mechanism_hypothesis | candidate | 0.670 | 0.463 | 0.739 | 1 | 5 | plausible_unproven |
| `MECH-204` | mechanism_hypothesis | candidate | 0.643 | 0.463 | 0.824 | 5 | 8 | plausible_unproven |
| `SD-014` | design_decision | candidate | 0.661 | 0.469 | 0.854 | 3 | 13 | plausible_unproven |
| `SD-017` | design_decision | stable | 0.735 | 0.482 | 0.903 | 2 | 19 | plausible_unproven |
| `MECH-150` | mechanism_hypothesis | candidate | 0.660 | 0.492 | 0.772 | 2 | 3 | plausible_unproven |
| `SD-015` | design_decision | candidate | 0.640 | 0.500 | 0.779 | 4 | 13 | plausible_unproven |
| `MECH-153` | mechanism_hypothesis | candidate | 0.662 | 0.510 | 0.813 | 3 | 7 | plausible_unproven |
| `Q-034` | question | open | 0.642 | 0.525 | 0.758 | 3 | 6 | plausible_unproven |
| `SD-005` | design_decision | implemented | 0.697 | 0.532 | 0.862 | 23 | 4 | plausible_unproven |
| `MECH-440` | mechanism_hypothesis | candidate | 0.622 | 0.533 | 0.682 | 2 | 10 | plausible_unproven |
| `SD-003` | design_decision | superseded | 0.670 | 0.536 | 0.803 | 81 | 7 | plausible_unproven |
| `MECH-094` | mechanism_hypothesis | stable | 0.759 | 0.555 | 0.827 | 1 | 28 | plausible_unproven |
| `MECH-230` | mechanism_hypothesis | provisional | 0.739 | 0.555 | 0.800 | 1 | 11 | plausible_unproven |
| `MECH-262` | mechanism_hypothesis | candidate | 0.771 | 0.555 | 0.843 | 1 | 8 | plausible_unproven |
| `DEV-NEED-006` | - | - | 0.752 | 0.575 | 0.811 | 1 | 5 | plausible_unproven |
| `MECH-045` | mechanism_hypothesis | provisional | 0.768 | 0.575 | 0.833 | 1 | 14 | plausible_unproven |
| `MECH-056` | mechanism_hypothesis | provisional | 0.766 | 0.575 | 0.830 | 1 | 13 | plausible_unproven |
| `MECH-057a` | - | - | 0.755 | 0.575 | 0.815 | 1 | 4 | plausible_unproven |
| `MECH-059` | mechanism_hypothesis | active | 0.726 | 0.575 | 0.777 | 1 | 7 | plausible_unproven |
| `MECH-060` | mechanism_hypothesis | provisional | 0.745 | 0.575 | 0.802 | 1 | 12 | plausible_unproven |
| `MECH-061` | mechanism_hypothesis | active | 0.754 | 0.575 | 0.814 | 1 | 8 | plausible_unproven |
| `MECH-062` | mechanism_hypothesis | candidate | 0.684 | 0.575 | 0.739 | 1 | 2 | plausible_unproven |
| `MECH-072` | mechanism_hypothesis | candidate | 0.725 | 0.575 | 0.775 | 1 | 6 | plausible_unproven |
| `MECH-087` | mechanism_hypothesis | candidate | 0.635 | 0.575 | 0.696 | 1 | 1 | plausible_unproven |
| `MECH-106` | mechanism_hypothesis | candidate | 0.766 | 0.575 | 0.829 | 1 | 5 | plausible_unproven |
| `MECH-120` | mechanism_hypothesis | candidate | 0.799 | 0.575 | 0.874 | 1 | 11 | plausible_unproven |
| `MECH-124` | mechanism_hypothesis | provisional | 0.777 | 0.575 | 0.844 | 1 | 4 | plausible_unproven |
| `MECH-187` | mechanism_hypothesis | candidate | 0.760 | 0.575 | 0.822 | 1 | 7 | plausible_unproven |
| `MECH-231` | mechanism_hypothesis | provisional | 0.708 | 0.575 | 0.753 | 1 | 3 | plausible_unproven |
| `MECH-259` | mechanism_hypothesis | stable | 0.784 | 0.575 | 0.853 | 1 | 8 | plausible_unproven |
| `MECH-268` | mechanism_hypothesis | provisional | 0.754 | 0.575 | 0.813 | 1 | 8 | plausible_unproven |
| `MECH-285` | mechanism_hypothesis | candidate | 0.791 | 0.575 | 0.863 | 1 | 16 | plausible_unproven |
| `MECH-306` | mechanism_hypothesis | provisional | 0.790 | 0.575 | 0.862 | 1 | 4 | plausible_unproven |
| `MECH-314` | mechanism_hypothesis | candidate_substrate_landed | 0.790 | 0.575 | 0.862 | 1 | 10 | plausible_unproven |
| `MECH-314a` | - | - | 0.777 | 0.575 | 0.844 | 1 | 6 | plausible_unproven |
| `MECH-346` | mechanism_hypothesis | candidate | 0.734 | 0.575 | 0.787 | 1 | 3 | plausible_unproven |
| `MECH-347` | mechanism_hypothesis | candidate | 0.738 | 0.575 | 0.792 | 1 | 3 | plausible_unproven |
| `MECH-358` | mechanism_hypothesis | candidate | 0.722 | 0.575 | 0.771 | 1 | 3 | plausible_unproven |
| `MECH-436` | mechanism_hypothesis | candidate | 0.707 | 0.575 | 0.773 | 1 | 2 | plausible_unproven |
| `SD-003-prereq` | - | - | 0.723 | 0.575 | 0.772 | 1 | 3 | plausible_unproven |
| `SD-032a` | - | - | 0.807 | 0.575 | 0.884 | 1 | 25 | plausible_unproven |
| `SD-034` | design_decision | provisional | 0.751 | 0.575 | 0.810 | 1 | 9 | plausible_unproven |
| `SD-057` | design_decision | candidate | 0.680 | 0.575 | 0.733 | 1 | 2 | plausible_unproven |
| `SD-059` | design_decision | candidate | 0.767 | 0.575 | 0.831 | 1 | 4 | plausible_unproven |
| `ARC-024` | architecture_hypothesis | provisional | 0.685 | 0.593 | 0.777 | 26 | 3 | plausible_unproven |
| `SD-007` | design_decision | implemented | 0.742 | 0.594 | 0.890 | 18 | 6 | plausible_unproven |
| `SD-063` | design_decision | provisional | 0.764 | 0.603 | 0.818 | 1 | 4 | plausible_unproven |
| `MECH-071` | mechanism_hypothesis | provisional | 0.722 | 0.604 | 0.840 | 32 | 4 | plausible_unproven |
| `MECH-309` | mechanism_hypothesis | candidate | 0.753 | 0.605 | 0.852 | 2 | 14 | plausible_unproven |
| `SD-013` | design_decision | provisional | 0.719 | 0.608 | 0.829 | 4 | 4 | plausible_unproven |
| `INV-089` | invariant | provisional | 0.732 | 0.609 | 0.773 | 1 | 3 | plausible_unproven |
| `MECH-284` | mechanism_hypothesis | provisional | 0.763 | 0.614 | 0.813 | 1 | 15 | plausible_unproven |
| `ARC-026` | architecture_hypothesis | provisional | 0.703 | 0.615 | 0.762 | 2 | 5 | plausible_unproven |
| `MECH-119` | mechanism_hypothesis | stable | 0.701 | 0.615 | 0.759 | 2 | 3 | plausible_unproven |
| `MECH-261` | mechanism_hypothesis | stable | 0.757 | 0.615 | 0.852 | 2 | 20 | plausible_unproven |
| `SD-004` | design_decision | implemented | 0.751 | 0.615 | 0.887 | 6 | 16 | plausible_unproven |
| `SD-008` | design_decision | stable | 0.658 | 0.615 | 0.701 | 2 | 2 | plausible_unproven |
| `MECH-423` | mechanism_hypothesis | provisional | 0.769 | 0.618 | 0.820 | 1 | 6 | plausible_unproven |
| `SD-079` | design_decision | provisional | 0.597 | 0.640 | 0.576 | 1 | 2 | confirmed_established |

_Suppressed by gating: 112 substrate_coherence (ARC + universal invariant), 70 answer_state (open_question). These cross the gate under one regime but not the other; the discrepancy is not actionable under their evidence rules. See suppressed sections below._

## Implementation-cohort claims with zero experimental backing

Standard-gating claims with status in {stable, active, implemented, resolved} but no experimental evidence in the matrix. Under the decoupled regime they would not qualify for promotion on lit alone. This is the central question for Phase 2 -- queue an experiment per claim. (`architectural_commitment`, universal `invariant`, and `open_question` claims with this profile are surfaced separately below; they don't need experiments under their gating.)

Total: **5** standard-gating claims with no exp.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-035` | question | resolved | 0.865 | 15 |
| `SD-032` | design_decision | stable | 0.859 | 9 |
| `SD-106` | design_decision | implemented | 0.849 | 5 |
| `SD-035` | design_decision | stable | 0.844 | 6 |
| `SD-018` | substrate_decision | implemented | 0.715 | 2 |

### Implementation cohort with no exp -- suppressed (substrate_coherence)

These don't need experiments. They're foundational design choices (ARC) or universal invariants -- by definition tested by the substrate's coherent operation, not isolated probes.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `ARC-009` | architectural_commitment | active | 0.872 | 5 |
| `ARC-010` | architectural_commitment | active | 0.866 | 4 |
| `INV-010` | invariant | active | 0.833 | 3 |
| `INV-013` | invariant | active | 0.801 | 3 |
| `ARC-002` | architectural_commitment | active | 0.782 | 5 |
| `ARC-004` | architectural_commitment | active | 0.777 | 3 |
| `ARC-011` | architectural_commitment | active | 0.766 | 3 |
| `ARC-014` | architectural_commitment | active | 0.751 | 3 |
| `ARC-001` | architectural_commitment | active | 0.652 | 1 |
| `INV-014` | invariant | active | 0.652 | 1 |

### Implementation cohort with no exp -- suppressed (answer_state)

Open questions where the implementation reflects our current operating answer, not an experimental result. Restate as a MECH or SD if the answer should be tested.

| claim | type | status | lit_conf | n_lit |
|---|---|---|---:|---:|
| `Q-042` | open_question | resolved | 0.834 | 5 |
| `Q-079` | open_question | resolved | 0.823 | 5 |
| `Q-017` | open_question | active | 0.821 | 7 |
| `Q-016` | open_question | active | 0.818 | 5 |
| `Q-015` | open_question | active | 0.799 | 5 |
| `Q-005` | open_question | active | 0.768 | 4 |
| `Q-018` | open_question | active | 0.756 | 3 |
| `Q-087` | open_question | resolved | 0.737 | 4 |
| `Q-006` | open_question | active | 0.697 | 3 |

## Novel discovery quadrant

`exp_conf >= 0.62` with `lit_conf < 0.55`. Either a genuine substrate-level finding without prior art, or a missing lit pull. Either way worth surfacing -- under the legacy regime these appear weaker than they actually are.

Total: **7**.

| claim | status | exp_conf | lit_conf | n_exp | n_lit |
|---|---|---:|---:|---:|---:|
| `SD-071` | provisional | 0.761 | 0.000 | 1 | 0 |
| `SD-098` | candidate | 0.761 | 0.000 | 1 | 0 |
| `SD-074` | candidate | 0.754 | 0.000 | 1 | 0 |
| `SD-075` | candidate | 0.752 | 0.000 | 1 | 0 |
| `SD-077` | candidate | 0.752 | 0.000 | 1 | 0 |
| `SD-019b` | - | 0.716 | 0.000 | 1 | 0 |
| `ARC-027` | active | 0.713 | 0.000 | 4 | 0 |

## New flags (would replace `low_overall_confidence` at cutover)

### `low_exp_conf` (exp_conf < 0.55 with at least one experiment)

Total: **62**.

| claim | status | exp_conf | n_exp |
|---|---|---:|---:|
| `MECH-155` | candidate | 0.105 | 1 |
| `INV-054` | candidate | 0.125 | 1 |
| `MECH-118` | candidate | 0.125 | 1 |
| `MECH-188` | candidate | 0.125 | 1 |
| `SD-023` | candidate | 0.125 | 1 |
| `SD-047` | candidate | 0.125 | 1 |
| `MECH-445` | candidate | 0.148 | 1 |
| `INV-088` | candidate | 0.159 | 1 |
| `INV-090` | candidate | 0.159 | 1 |
| `MECH-457` | candidate | 0.160 | 1 |
| `MECH-070` | retiring | 0.163 | 2 |
| `MECH-111` | candidate | 0.175 | 2 |
| `MECH-116` | candidate | 0.175 | 2 |
| `MECH-295` | candidate | 0.175 | 2 |
| `MECH-329` | candidate | 0.182 | 1 |
| `MECH-466` | candidate | 0.193 | 1 |
| `MECH-475` | retired | 0.197 | 1 |
| `SD-087` | candidate | 0.203 | 1 |
| `MECH-025b` | - | 0.207 | 1 |
| `MECH-122` | provisional | 0.207 | 1 |
| `MECH-166` | candidate | 0.207 | 1 |
| `MECH-128` | candidate | 0.217 | 3 |
| `SD-009` | candidate | 0.219 | 1 |
| `MECH-463` | candidate | 0.225 | 2 |
| `MECH-152` | candidate | 0.227 | 1 |
| `MECH-144` | candidate | 0.266 | 1 |
| `MECH-029` | provisional | 0.275 | 1 |
| `MECH-321` | candidate | 0.277 | 2 |
| `MECH-097` | candidate | 0.280 | 1 |
| `MECH-137` | candidate | 0.280 | 1 |
| ... | ... | ... | ... (32 more) |


### `lit_only_above_cap` (no exp, lit_conf >= 0.5)

Total: **361**.

Claims with literature support and no experiment yet. These are candidates for the next round of experiment design.

| claim | status | lit_conf | n_lit |
|---|---|---:|---:|
| `INV-050` | candidate | 0.918 | 8 |
| `MECH-121` | candidate | 0.894 | 5 |
| `SD-037` | candidate | 0.893 | 7 |
| `SD-045` | candidate | 0.890 | 4 |
| `MECH-527` | candidate | 0.885 | 4 |
| `MECH-092` | candidate | 0.878 | 15 |
| `MECH-302` | candidate | 0.874 | 7 |
| `MECH-313` | candidate | 0.874 | 6 |
| `MECH-053` | provisional | 0.873 | 6 |
| `MECH-263` | candidate | 0.873 | 4 |
| `CDQ-010` | - | 0.872 | 5 |
| `MECH-004` | candidate | 0.871 | 5 |
| `MECH-307` | candidate_substrate_landed | 0.870 | 6 |
| `SD-033b` | - | 0.869 | 5 |
| `MECH-271` | candidate | 0.868 | 4 |
| `MECH-066` | candidate | 0.867 | 5 |
| `MECH-354` | candidate | 0.866 | 5 |
| `MECH-CBBL-PROPOSED` | - | 0.865 | 7 |
| `Q-035` | resolved | 0.865 | 15 |
| `SD-021` | candidate | 0.865 | 9 |
| `MECH-042` | candidate | 0.863 | 5 |
| `MECH-203` | candidate | 0.863 | 8 |
| `MECH-320` | candidate_substrate_landed | 0.863 | 5 |
| `MECH-083` | candidate | 0.861 | 4 |
| `MECH-317` | candidate | 0.860 | 6 |
| `SD-032` | stable | 0.859 | 9 |
| `SD-039` | candidate | 0.859 | 7 |
| `MECH-314c` | - | 0.858 | 6 |
| `ARC-105` | candidate | 0.857 | 4 |
| `SD-033` | candidate | 0.857 | 7 |
| `DEV-NEED-009` | - | 0.856 | 4 |
| `EXT-006` | candidate | 0.856 | 5 |
| `SD-033e` | - | 0.856 | 9 |
| `MECH-141` | candidate | 0.855 | 4 |
| `MECH-267` | provisional | 0.855 | 5 |
| `MECH-288` | candidate | 0.855 | 11 |
| `MECH-030` | provisional | 0.854 | 4 |
| `MECH-038` | candidate | 0.854 | 5 |
| `MECH-172` | candidate | 0.853 | 6 |
| `MECH-002` | provisional | 0.852 | 5 |
| `MECH-191` | candidate | 0.852 | 4 |
| `MECH-064` | candidate | 0.851 | 5 |
| `MECH-265` | candidate | 0.851 | 6 |
| `EXT-002` | candidate | 0.850 | 5 |
| `MECH-266` | provisional | 0.850 | 7 |
| `ARC-049` | candidate | 0.849 | 26 |
| `DEV-NEED-012` | - | 0.849 | 6 |
| `SD-106` | implemented | 0.849 | 5 |
| `MECH-046` | provisional | 0.847 | 4 |
| `MECH-264` | candidate | 0.847 | 5 |
| ... | ... | ... | ... (311 more) |

---

Source matrix: `evidence/experiments/claim_evidence.v1.json`. Generated by `scripts/generate_option_e_shadow.py`.
