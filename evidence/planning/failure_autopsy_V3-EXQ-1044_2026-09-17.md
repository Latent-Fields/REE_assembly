# Failure autopsy -- V3-EXQ-1044 (hippocampal campaign assay A, Gate A1)

**STATUS: `confirmed`** -- interactive Step 8 gate held 2026-09-17.

| | |
|---|---|
| run_id | `v3_exq_1044_hippocampal_assay_a_access_mechanism_20260916T141717Z_v3` |
| queue_id | V3-EXQ-1044 |
| claims | **none** -- `claim_ids: []` by design (claim-free diagnostic) |
| bears_on | `hippocampal_campaign_assay_a:gate_a1_conditional_access`, ARC-139, MECH-537/538/540/547/548, INV-105 |
| outcome | FAIL -- 4/8 criteria; both load-bearing criteria missed their floor |
| manifest self-route | `conditional_access_earns_nothing_at_any_bandwidth` |
| **adjudicated label** | **`gate_a1_undetermined_instrument_noise_exceeds_effect_floor`** |
| machine | DLAPTOP-4.local, `darwin-arm64-py3.13-torch2.12.0`, 3906 s, seeds [42, 43, 45] |

---

## 1. The headline: UNDETERMINED, not negative

Both load-bearing criteria missed the +0.05 floor -- C1b mean **-0.0736** at M*, C1a mean **-0.0141** at M_A4. The first draft read that as a clean negative. **It is not**, because the instrument cannot resolve a 0.05 effect:

- **A4's hypothesis class strictly CONTAINS A1's.** Identical architecture and parameter count (`in_dim` 33), and `_cond_mask` gives A1 an **all-zero** conditioning vector -- zero A4's conditioning columns and A4 *is* A1, under the same optimiser, lr, passes and clipping. So `A4 - A1 >= 0` is required at the optimum. **Measured: 16 of 30 matched cells violate it**, 7 by at least 0.05, worst **-0.1947**.
- **Median within-cell restart spread = 0.0573** over 210 fitted cells (mean 0.1109, p90 0.3012, max 0.4727) -- **larger than the 0.05 effect the criterion exists to detect**.
- **27 of 135 adjacent-width steps run downward**, although width M nests M-1.
- The paired SE of the C1b mean is 0.0533 -- **equal to the floor**.

The driver's own header anticipated this ("a one-shot unconditional fit is non-monotone in M at 60 passes"); `N_RESTARTS = 3` with block-2 argmax was the mitigation, and the residuals show it did not work.

**Correcting the draft's English.** `n_seeds_positive` counts seeds **clearing 0.05**, not seeds above zero (driver:1281). Correct statement: *0 of 3 seeds cleared the floor at either width; at M_A4 the per-seed delta is **positive on 2 of 3 seeds** (+0.014, +0.020), the mean carried negative by seed 45 alone (-0.076).* The two widths are also not independent -- `M*` [3,3,2] and `M_A4` [4,3,2] coincide on seeds 43 and 45, so C1a and C1b share two thirds of their cells byte-identically.

## 2. The zero-compute re-analysis (run at the gate, user-authorised)

The driver pre-registered it; it was run on the banked `restarts_block3_agreement` arrays, replacing block-2-argmax with the within-cell **median**, pre-registered widths held fixed:

| | C1b mean | C1a mean | seeds > 0 | nested-order violations |
|---|---|---|---|---|
| argmax (as run) | -0.0736 | -0.0141 | 1 / 2 | 16/30 (53%), worst -0.1947 |
| **median** | **-0.2240** | **-0.1697** | 0 / 0 | 16/30 (53%), worst **-0.2718** |

**Two findings, pointing different ways, both reported.**

1. **The direction is robust to aggregation -- and robust the *opposite* way from a rescue.** Under the median the deficit *grows* and every seed turns negative, with C1b's across-seed sd collapsing to 0.0034. The two per-seed positives at M_A4 do not survive. That closes the near-miss reading.
2. **The instrument gate still fails, identically.** The violation rate is 53% under **both** aggregations and the worst violation gets worse. The pre-stated threshold was ~10%.

**Net: still UNDETERMINED, on a sharper basis.** A persistent, aggregation-robust *deficit* for an arm whose hypothesis class contains its comparator's cannot be a fact about conditioning -- at the optimum it is impossible. It is a fact about the **fit**: the extra conditioning columns make this optimiser reliably converge worse. The run measures an **optimisation pathology**, not the value of receiver-state conditioning.

## 3. What the redesign did and did not fix

The predecessor design was structurally incapable of answering: an MSE fit to a query-invariant target forced A4 onto A1. Verified in code that the redesign genuinely closed this -- the loss is CrossEntropy on the query-specific oracle action with gradient flowing only into the bridge (`_fit_end_to_end`, 976-1017). So the negative is **not** the old confound recurring. It is a new, different limit.

## 4. Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | n/a -- claim-free |
| Biological reference | partial; and "receiver state" is operationalised as the externally-assigned query cue, a **fidelity** divergence the tranche names, not merely a scope one |
| Prerequisites | present; but "99 of 99" is 5 precondition **families** replicated across arms and seeds, two close to un-failable |
| Implementation | complete **as redesigned** -- but the fitted-arm residuals invalidate the sign |
| Environment | adequate for the narrow question (hazard-free rung, narrow by design) |
| Measurement | **under-instrumented on the LOAD-BEARING pair too**, not only the refinements |
| Integration | C7 fails, but on a denominator that limits what it can carry |
| Scale | insufficient |

**Failure location (GOV-FAILLOC-1):** mechanism `not_established`, measures `not_established`, environment `partial`, REE **false**. **Net: MIXED.** Stated explicitly because this claim-free run carries organism-level numbers that invite a "REE failed" write-up. It cannot be: at the actual evaluation widths the **native arm scores 11.59 against A4's 2.70** -- REE's own closed-loop competence is intact; what degrades is the **bridged apparatus under test**.

## 5. Scope guard (binding)

The manifest's own **FORBIDDEN** clause travels with every restatement: *this licenses no claim that the interface is unconditional in general.* Retained -- but **re-sourced**. The draft attributed it to a spec "null table C1a/C1b FAIL row"; **no such row exists** (the strings C1a/C1b do not occur in the spec; sec 2.8's table is keyed on result patterns). The observed pattern matches none of its rows cleanly. The clause is kept on its own merits.

## 6. Routing

**`queue-experiment`**, **NEW EXQ number** -- not because Gate A1 is answered (it is not), but because a successor needs a materially **different instrument**.

**OWED FIRST (`complicated (buildable)`, gates the rest):** the nested-order violation rate must become a hard pre-registered readiness gate, and the fit must be shown to close it *before* C1a/C1b are read at all. The cheapest candidate repair: **warm-start the conditioned arm from the unconditional arm's fitted solution**, which makes the nesting constructive so A4 cannot end up worse than A1 by construction.

Then: variance control on the **load-bearing pair** (not only C3); keep the bandwidth ladder and block-2 selection rule; fix C7's denominator and add an applicability precondition; flag C6 as structurally-expected (it is a conjunction that passes whenever its first conjunct never fires -- which happened on all 3 seeds); power C3 or demote it; record rollout aliveness as first-class (37-67% of episodes are dead by step 20).

**REFUSED:** a Gate A1 re-pose **with this instrument**. *(Corrected -- the draft refused any re-pose on the ground that the deltas were wrong-signed and power would not move them. That ground is withdrawn.)*

**Substrate queue: `none`.** **Secondary routing: none.**

## 7. Gates

- **Re-derive brake: formally 0** -- a claim-free target accumulates on no claim. Recorded because that is exactly the GOV-DIAG-1 blind spot: this chain is invisible unless the `bears_on` token is carried forward **verbatim**. This target **establishes** the campaign's token (no prior artifact in the corpus carries one for it).
- **Granularity-debt trigger:** cannot fire (no tagged claim).
- **Step 7b: 0 fires, but FOUR checks `inapplicable`** (C1/C2/C3 are claim-keyed and blind on a `claim_ids: []` target). **Not a clean bill -- the checks could not look.** Step 7c was briefed to carry the whole load, and it did: the decisive finding came from 7c.
- **Step 7c: `CONTESTED`**, run on the **session model (Opus 5) -- a SAME-MODEL pass** (fable unavailable, monthly spend limit). Decisive findings in sections A and C, all accepted and applied.

## 8. Claim recommendations -- NOTE-ONLY

`claim_ids` is empty by design, so **no direction and no flag** are written on any claim, and `epistemic_category` is left alone (MECH-547/548/ARC-139 are `substrate_conditional`, `implementation_phase: v4` -- a v3 synthetic instrument cannot adjudicate them). The stronger ground, from Step 7c: the instrument cannot resolve the effect, so **there is no adjudication to record on any claim even if the run had tagged one**.

- **MECH-547** -- note-only; record that Gate A1 is UNDETERMINED *at this instrument*, not negative. **Do not record a weakening.**
- **MECH-548** -- **downgraded** to a non-attributed observation about the bridged interface. Letting C7 carry a MECH-548 note over-records: C7 is a non-load-bearing refinement measured on an arm with no established advantage, and its statistic and bar use different denominators.
- The manifest's `evidence_direction: "weakens"` stamp is **flagged as unsupported** by the instrument's own residuals. Recommended: leave the manifest field as recorded (rewriting history is worse) and record the flag in the note. Registry effect is zero either way.

## 9. Frozen ledger -- deliberate abstention

**No ledger write.** No registry question covers this campaign, and this autopsy declines to open one: the campaign already carries its own pre-registered gate structure and null table in `hippocampal_campaign_assay_specifications_20260910.md`, which is a frozen pre-registration in all but file format. A parallel registry question would create a **second, competing denominator**. Surfaced at the gate as a deliberate abstention; Step 7c independently agreed this is sound rather than an evasion.

## 10. Owed to `/governance`

1. Apply the two **note-only** updates (MECH-547, MECH-548) -- no direction, no flag, no category change.
2. Mark the run reviewed.
3. Preserve the `bears_on` token **verbatim** in every successor of this campaign.
4. Chip the successor design. This session spawned no chip off its own unreviewed routing.
