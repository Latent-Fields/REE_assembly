# V3-EXQ-932 -- z_goal / residue_wanting -> behaviour observational coupling

**Status:** PASS  (diagnostic / observational -- claim_ids=[], weights no governance)
**Interpretation label:** `wanting_behaviour_coupling_detected`
**Substrate:** V3-EXQ-916a verbatim (residue_wanting writer fix; use_proxy_fields=True,
tonic_5ht_enabled=True, update_benefit_salience() wired). Coupling instrument ported
byte-for-byte from V3-EXQ-906c so the z_goal re-check is directly comparable to 906c's
near-null (r~0.07, n=3785), now on the fixed substrate.

**OBSERVATIONAL, NOT CAUSAL.** A lagged correlation is consistent with but does not
establish that the internal signal DRIVES behaviour (common-cause confounds abound). The
causal-necessity test is the separate ablation V3-EXQ-931 (CEM wanting_weight); this run
does not duplicate it and must not be read as causal.

**Pre-registered non-trivial-coupling floor:** |r| or |rho| >= 0.15 with
n >= 200 (906c's r~0.07 is the "no coupling" reference).

**Readiness (measurement premise):**
- residue_wanting varies: YES  (max std 0.56797)
- z_goal varies: YES  (max std 0.07800)
- all couplings powered (n >= 200): YES
- total pooled steps: 1013

## z_goal -> behaviour couplings (906c-matched re-check + improved benefit_exposure)
| coupling | Pearson r | Spearman rho | n | reading |
|----------|-----------|--------------|---|---------|
| `zgoal_t_to_approach_t1` | +0.0000 | +0.0000 | 998 | near-null |
| `zgoal_t_to_benefit_t1t3` | -0.0321 | -0.0324 | 998 | near-null |
| `zgoal_t_to_benefitexp_t1t3` | +0.1801 | +0.1553 | 998 | NON-TRIVIAL |

## residue_wanting -> behaviour couplings (NEW -- first time on live data)
| coupling | Pearson r | Spearman rho | n | reading |
|----------|-----------|--------------|---|---------|
| `wanting_t_to_approach_t1` | +0.0000 | +0.0000 | 998 | near-null |
| `wanting_t_to_benefitexp_t1t3` | +0.1506 | +0.0859 | 998 | NON-TRIVIAL |
| `wanting_t_to_moved_t1` | +0.3726 | +0.3433 | 998 | NON-TRIVIAL |
| `wanting_t_to_reefexit_t1` | +0.1333 | +0.1263 | 998 | near-null |
| `wanting_zgoal_contemporaneous` | +0.6534 | +0.4939 | 1013 | NON-TRIVIAL |

`*_benefit_t1t3` uses 906c's exact harm_signal>0 definition (for comparability);
`*_benefitexp_t1t3` uses 916a's now-live real resource-contact signal (benefit_exposure).
`wanting_zgoal_contemporaneous` cross-checks whether the two "wanting" signals (the
hippocampal-map residue channel vs the frontal goal-attractor) even track each other.

**Channel non-degeneracy (max std across seeds):**
- z_harm_s: 0.20780  (varies)
- z_harm_un: 0.15134  (varies)
- z_harm_a: 0.66521  (varies)
- drive: 0.36466  (varies)
- z_goal: 0.07800  (varies)
- vigor: 0.00000  (FLAT)
- override: 0.24222  (varies)
- z_block: 0.00000  (FLAT)
- excite: 6.57770  (varies)
- dread: 0.76207  (varies)
- safety_cue_signal: 0.42916  (varies)
- safety_terrain_read: 0.00000  (FLAT)
- residue_wanting: 0.56797  (varies)
