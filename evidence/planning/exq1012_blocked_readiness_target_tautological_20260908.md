# V3-EXQ-1012 NOT QUEUED -- the E3 commensurability operator's own readiness target is tautologically satisfied by the operator, and the control gate is refuted by its predecessor's data

**Generated:** 2026-09-08T19:32:00Z
**Session:** `w5-freshfill-20260908` (campaign W5 fresh-design queue-fill)
**Chip:** `chip-20260907-e3-commensurability-validation`
**Driver authored, smoke-green, NOT QUEUED:** `ree-v3/experiments/v3_exq_1012_e3_commensurability_regime_validation.py`
**Substrate under validation:** `f_dominance_conversion_ceiling` rung 3 / `SD-E3-CHANNEL-COMMENSURABILITY`, IMPLEMENTED ree-v3 `c47b885` (2026-09-07)
**Target-setting artifact:** `failure_autopsy_V3-EXQ-571c_2026-09-02` (CONFIRMED; ratified by /governance 2026-09-02, REE_assembly `0ade914d46`)
**Red-team (Step 4.5, model `fable`):** **BLOCKING** -- findings file `scratchpad/redteam_1012.md`
**Claim involved:** MECH-439. **Its direction does not change on this record.**

---

## 0. The one-paragraph statement

The owed regime-level validation of the E3 channel-commensurability operator was authored in
full against the chip's brief -- the ablation pair on the same seeds and 936-regime env, the
knob set on `cfg.e3` (never through `from_dims`) with a runtime assert that it reached the live
selector, the spec-mandated `last_channel_scale_estimates` exposure recorded on every cell with
`engaged` gated, and the OFF arm as a load-bearing positive control. It is **not queued**,
because the Step 4.5 review returned **BLOCKING** on two findings that were then verified
directly against source and against the predecessor's landed manifest. The deeper of the two is
not a defect in this driver at all: **the readiness target the confirmed autopsy pre-registered
is an arithmetic identity of the operator it is meant to validate.** No experiment built on that
target can fail, so none can validate anything.

---

## 1. Finding 1 (BLOCKING) -- the readiness target is tautologically satisfied by the operator

**The target, verbatim from the confirmed autopsy and restated in the operator's own spec:**

> ">= 2 E3 score channels simultaneously above a 1e-3 RELATIVE cross-candidate share in the
> 936 regime"

**What the operator does** (`sd_e3_channel_commensurability.md`): each declared channel's
per-candidate term is divided by an EMA of **that channel's own cross-candidate standard
deviation**, estimated from prior ticks.

**What the DV is:** the within-tick **cross-candidate variance partition** over those same
per-channel terms, read from `E3TrajectorySelector._last_traj_components`.

**Which terms the partition reads -- verified at source.** `ree_core/predictors/e3_selector.py`,
in the `_last_traj_components` block, says so itself:

```python
if self.e3_score_decomp_enabled:
    self._last_traj_components = {
        "f": float(f.detach().mean().item()),
        # EFFECTIVE (post-commensurability) terms -- what actually
        # entered the score, which is what channel authority is a
        # partition OF. Bit-identical to the raw terms when the
        # operator is off, since then no scaling was applied.
        "f_weighted": float(_t_f.detach().mean().item()),
        "harm_weighted": float(_t_m.detach().mean().item()),
        "residue_weighted": float(_t_phi.detach().mean().item()),
        ...
```

**The identity.** Writing `s_c` for the EMA of channel `c`'s cross-candidate SD:

```
Var_xcand( term_c / s_c )  =  Var_xcand(term_c) / s_c^2  ~=  1     for every channel whose
                                                                  raw SD exceeds the floor
```

because `s_c` is an EMA of exactly `sqrt(Var_xcand(term_c))`. Every live channel's normalised
cross-candidate variance therefore lands near 1, and the shares -- which are that variance
divided by their sum -- land near **1/k**. The 1e-3 share floor is a **1000x** tolerance, so
every channel whose raw cross-candidate SD clears the 1e-12 absolute floor clears the relative
floor too, by construction.

**The operator's own build-time measurement is the identity's fingerprint**, and it is recorded
in the spec:

| | n_live (>= 1e-3) | top share |
|---|---|---|
| operator OFF | 1 | 0.999518 |
| operator ON | **2** | **0.500000** |

`0.500000` is exactly `1/2`. With two non-structurally-zero channels, equal shares *are*
0.500000. That number is not evidence the operator rebalanced authority in this environment; it
is what dividing each channel by its own spread produces in any environment whatever.

**The authoring smoke of this driver reproduces it.** The fed ON arm returned three live
channels with shares `f 0.215 / harm 0.130 / residue 0.654` -- moving toward, though not yet at,
1/3 each, with the residual spread explained by the EMA lagging a non-stationary raw variance
over only 34 updates. At the full 200-fresh-selection scale the EMA is far better converged and
the shares should be *closer* to 1/k, not further -- i.e. the run gets **more** tautological with
more data, not less.

**So the pre-registered criterion cannot fail.** A criterion that cannot fail cannot validate,
and this one would have returned `commensurability_lifts_readiness_condition_both_regimes` --
PASS, target met, "the blocked MECH-439 / ARC-062 experiments are now posable" -- from an
arithmetic identity.

**This is a finding about the TARGET, not only about this driver.** The target was
pre-registered by a confirmed, governance-ratified autopsy and is restated as the acceptance
condition in the operator's own implementation record. Any experiment that adopts it inherits the
tautology. That is why this record routes to governance rather than being repaired here.

## 2. Finding 2 (BLOCKING, independent) -- the control gate is refuted by V3-EXQ-571c's own landed data

The design's step 1 makes the OFF arm a load-bearing positive control: it must **reproduce the
monopoly**, operationalised as `n_live_channels <= 1` on every seed. That is refuted by the
predecessor's own manifest
(`evidence/experiments/v3_exq_571c_e3_variance_monopoly_presence_936_regime_20260902T152856Z_v3.json`),
whose starved arm -- byte-identical to this driver's `C3_starved_operator_off`, on the same
seeds -- measured:

```
B2_936_env_starved_warmup  seed 42  n_live 1   top harm_weighted 0.99885
B2_936_env_starved_warmup  seed 43  n_live 2   top harm_weighted 0.98064
B2_936_env_starved_warmup  seed 45  n_live 1   top harm_weighted 0.99957
B2_936_env_starved_warmup  seed 46  n_live 3   top harm_weighted 0.73787
```

Across all 16 of 571c's cells, `n_live == 1` holds in only **7**. The OFF path is pinned
bit-identical when the operator is off (the operator's own backward-compatibility contract), so
these values reproduce -- and the run would have routed
`control_monopoly_absent_regime_drifted_substrate_not_ready_requeue`, **discarding all four arms
and reporting that the 936 regime had drifted, while in fact reproducing 571c exactly.**

The error is mine and is a misreading of the autopsy: `n_live_channels == 1` was 571c's
**worst-cell readiness gate** verdict, not a per-cell fact. The monopoly is better
operationalised on the **share** (`xcand_top_share >= 0.85`, which does hold broadly: 0.9989 /
0.9806 / 0.9996 / 0.7379 on the cells above) than on the live-channel count. Fixing this alone
is straightforward -- but it does not touch Finding 1, which is why the run stops regardless.

## 3. Two further findings, recorded (not the reason for the stop)

- **The `engaged` gate is close to a formality at full scale.** `engaged` is
  `_chan_scale_n >= 20` and monotone, and P0 alone contributes ~12,000 env ticks before P1, so
  it is trivially true in a real run. It earned its place anyway: in the authoring dry-run the
  starved ON arm had `n_updates 18 < 20`, was therefore inert, and came out **byte-identical to
  its own control** -- which without the gate would have read as "the operator does not work in
  the starved regime". Worth keeping in any successor; just not load-bearing at scale.
- **The inherited `n_live_channels >= 2` readiness precondition, scoped to the ON arms, is the
  same quantity the verdict routes on.** A genuine "operator does not lift" result would be
  recorded twice with contradictory meanings -- as a content verdict in `interpretation.label`
  and as an *unscored, explicitly not-a-refutation* red arm in `per_arm_gate`. A successor should
  drop the precondition from the driver, since the verdict already reads it.

## 4. What a NON-tautological validation would measure

The operator's claim is about **which channel decides the committed action**. That is a property
of the SELECTION, and it must be read off something the operator does not itself define. Three
candidates, in rising order of directness:

1. **Commit-flip under shadow scoring.** On the same tick and the same candidate set, score once
   with the operator OFF and once ON, and report the fraction of ticks whose argmin CHANGES.
   Zero flips would mean the operator is rank-irrelevant however tidy its shares look -- which
   the current DV cannot detect at all.
2. **Per-channel argmin agreement with the committed candidate.** For each channel, does its own
   argmin coincide with the committed candidate, OFF vs ON? This measures authority in the sense
   the claim means -- "which channel's preference the commit follows" -- rather than variance
   bookkeeping.
3. **Behavioural readouts already recorded and currently unrouted** (`selected_class_counts`,
   `committed_entropy`, harm counts), matched OFF vs ON on the same seeds.

(1) is the natural falsifier and is cheap: it needs one extra scoring pass per tick and no new
training. Note it is also the honest test of the operator's stated virtue -- the spec argues at
length that a pooled denominator would be **argmin-invariant** and that only per-channel
standardisation "reaches the target". That argument is about argmins, so the validation should be
about argmins too.

## 5. Governance follow-on

Recommend the substrate entry's rung-3 readiness target be **re-posed onto a
selection-level DV** before any validation is queued against it, and that
`sd_e3_channel_commensurability.md`'s "Readiness target" section and the 571c autopsy's target
line be amended together, since the same sentence appears in both. Until then the rung is
**IMPLEMENTED but UNVALIDATABLE as specified**, which is a materially different state from
"validation owed" and should be visible as such on the entry.

**No claim direction changes on this record.** MECH-439 is untouched: nothing here says the
operator does or does not work, only that the pre-registered target cannot tell.

---

**Bottom line:** the driver is complete and its instrument is sound, and it would have returned a
confident PASS from an arithmetic identity. One afternoon of source-reading and one line of
algebra replaced a fleet run whose result would have been unfalsifiable by construction -- and
surfaced that the same defect sits in a confirmed autopsy's target and in the substrate record
that adopted it.
