# Benefit-field bandwidth build -- red-team findings (2026-09-25)

**Status: RECORD OF A COMPLETED ADVERSARIAL REVIEW. The build it reviews is LANDED
(ree-v3 `5e18e9797e` on `origin/main`). Nothing here has been applied to
`claims.yaml`. The one item that would change a USER-SPECIFIED validation criterion
(F-2/F-3's density floor) is recorded as an UNRATIFIED RECOMMENDATION and was
deliberately NOT applied.**

Session: `metaworker-science-20260925-orchc-benefit-bw-build` (campaign
`science-20260925-orchc-benefit-bw-build`, chip
`chip-20260924-benefit-field-bandwidth-build`), run on `ree-cloud-5`.
Substrate entry: `substrate_queue.json` -> `benefit-field-kernel-resolution`.

## What was reviewed

`ResidueConfig.benefit_field_bandwidth` -- an opt-in dedicated kernel bandwidth for
the BENEFIT terrain RBF, default `None` = inherit `kernel_bandwidth` = bit-identical.
Third instance of the SD-067 saturation class, after the MECH-303 safety terrain and
the harm field. Landed `b0f7457b`; corrections `5e18e9797e`.

## Verdict

**RED-TEAM VERDICT: BLOCKING** -- one blocking finding, four major, four minor.

The blocking finding is **scientific, not mechanical**. The engineering held: the
bit-identity claim survived a 10-config A/B against the pre-build sha `863d23d65a`
(byte-hashes of every read, the full `state_dict`, and every `integrate()` metric --
the only diff was the new attribute's presence in `vars()` and the dataclass field
count), and no fifth benefit consumer exists at an unreached bandwidth.

**Both findings that contradicted the build's own claims (F-1, F-4) were
independently re-verified by the authoring session before being acted on.** Both
reproduced exactly. That re-verification is the reason they were treated as real
rather than as subagent noise.

## F-1 [BLOCKING] Arming the knob INVERTS SD-024's DV at the config-default jitter

`add_residue_cluster` jitters each DA-allocated center by `randn * da_jitter_radius`.
`ResidueConfig.da_jitter_radius` defaults to **0.1**, and the live SD-024 run used
**0.3**. Both are far wider than any bandwidth that resolves a 0.07 manifold, so the
allocated cluster lands *outside* the narrowed kernel and density at the reward site
goes to **zero** -- while SD-024's DV is precisely that cluster allocation *raises*
density.

So narrowing the bandwidth fixes the **spatial** defect and destroys the
**allocation** axis, which is the DV itself. Independently measured (single-center
vs 3-center cluster density at the reward site):

| `benefit_field_bandwidth` | `da_jitter_radius` | single | cluster | ratio | verdict |
|---|---|---|---|---|---|
| OFF (1.0) | 0.3 (live) | 1.000 | 2.375 | 2.3753 | DV rises, correct |
| OFF (1.0) | 0.1 (default) | 1.000 | 2.923 | 2.9232 | DV rises, correct |
| OFF (1.0) | 0.01 | 1.000 | 2.999 | 2.9992 | DV rises, correct |
| 0.02 | 0.3 (live) | 1.000 | 0.000 | **0.0000** | **INVERTED** |
| 0.02 | 0.1 (default) | 1.000 | 0.000 | **0.0000** | **INVERTED** |
| 0.02 | 0.01 | 1.000 | 1.569 | 1.5687 | DV rises, correct |

Empirically `da_jitter_radius <= ~bandwidth/2`.

The original contract fixture set `da_jitter_radius = 0.01` with no comment, which is
what concealed this: every DA cell ran inside the curable regime, and
`test_c2_knob_reaches_the_da_cluster_allocator_base` asserted only per-center
bandwidth *values*, never that the density discriminator still pointed the right way.

**Applied:** the coupling is documented as constraint (a) on
`ResidueConfig.benefit_field_bandwidth` and in `field.py`'s carve-out (2); the
fixture override is commented as a deliberate coupling choice; and two contract
cells pin it -- `test_f1_da_cluster_dv_inverts_at_the_default_jitter_radius` (reading
the default from `ResidueConfig` rather than restating it, so a default change cannot
leave a stale literal) and `test_f1_co_scaling_the_jitter_restores_the_dv`. The
second cell is load-bearing: without it the first would read as a reason not to ship
rather than as a constraint.

**Owed by EXP-1391: pre-register the PAIR (bandwidth, jitter radius), never the
bandwidth alone.** This is now in the entry's `ready_blocked_by`.

## F-4 [MAJOR] "One constructor site is the complete wiring" was too strong

On the SD-024 per-center path (`use_da_modulated_rbf_density=True`),
`center_bandwidths` is a registered **buffer** and `_two_bw_sq` *prefers* it over
`self.bandwidth`. The constructor only **seeds** it. A `load_state_dict` from a
checkpoint written before this knob therefore restores the old scale silently:

```
checkpoint center_bandwidths unique: [1.0]
armed BEFORE load: self.bandwidth=0.02  center_bandwidths=[0.02]
load_state_dict -> <All keys matched successfully>
armed AFTER  load: self.bandwidth=0.02  center_bandwidths=[1.0]
effective_benefit_bandwidth still reports: 0.02
AFTER RESTORE: contact=23.99737 heldout=23.96777 ratio=0.99877  (the original defect)
CONTROL (same config, no restore):                  ratio=0.05270
```

`effective_benefit_bandwidth` reports armed while every read runs at 1.0 -- the
"structurally present but functionally inert" failure the harm knob's own comment
names. **Latent, not a current regression:** no live call site restores the benefit
RBF's `state_dict` today (the nearest, `v3_exq_768_..._spike.py::_share_terrain`, is
scoped to `neural_field`). Bounded to the DA path -- on the default scalar path the
buffer is not registered at all.

**Applied:** claim narrowed in `field.py` and in the entry's
`implementation_note_update`; pinned by
`test_f4_state_dict_restore_can_silently_defeat_the_knob` plus
`test_f4_the_scalar_path_has_no_such_buffer` (which bounds it, so the hazard does not
read broader than it is).

## F-2 / F-3 [MAJOR] The registered criterion has a degenerate-pass region and no floor

The criterion as registered -- *"benefit density at a held-out real state in a
different grid cell < 0.5x the density at the contact state"* -- is a **pure ratio**,
and is therefore satisfied by an arbitrarily narrow kernel where everything reads ~0,
the contact state included. Measured: **PASS at bw 0.001 with contact density
0.00000.** Separately, F-3: the build documented only the *ceiling* ("do not copy the
harm knob's 0.15, it exceeds the whole 0.07 manifold") and said nothing about the
*floor* the harm knob measured an inversion below (seed 0 inverted at bw 0.065,
ratio 0.748631, when the kernel got narrower than the within-class spread).

**NOT APPLIED -- and this is the deliberate line.** The criterion's wording came from
the user, via the chip. Adding a floor to it changes a user-specified pass/fail gate,
which is not this session's call. What was done instead:

- The hazard and the recommended fix are documented as constraint (b) (stay above the
  measured within-cell spread) and constraint (c) (a bare ratio is not enough; pair
  it with a contact-density floor scaled to the active center count) on
  `ResidueConfig.benefit_field_bandwidth`.
- Two contract cells pin both: `test_f3_below_the_within_cell_spread_the_read_collapses`
  (parametrised over two spreads) and
  `test_f2_the_ratio_criterion_alone_admits_a_degenerate_pass`, which exists so nobody
  later removes the contract's `assert d_contact > 1.0` floor as redundant with the ratio.
- The entry keeps `ready: false`, so nothing can run against the un-floored criterion.

**Recommended to EXP-1391's pre-registration (unratified):** carry a floor of roughly
`d_contact >= 0.5 * n_active_benefit_centers` alongside the ratio. No decision chip
was raised for this because the criterion's only consumer is EXP-1391's
pre-registration, which is *itself* a user-gated `/queue-experiment` step that will
see this record -- and because `ready: false` already blocks the path. Raising a chip
to ask permission to tighten a gate that cannot fire yet would put a non-question in
the consent lane.

## F-5 [MAJOR] Two "measured" fixture constants were not measured

The test file's geometry block was headed "facts about the substrate, not tuning
choices", but the source measurement gives only max pairwise 0.07, 180 states, 7 grid
cells, `||z|| ~0.33`, 23 centers, jitter 0.3. `GRID_CELL_SEP = 0.05` and
`WITHIN_CELL_SPREAD = 0.004` are **not in it** -- and the entry's own
`ready_blocked_by` makes the within-cell spread something EXP-1391's P0 still owes.

This mattered because the two together *bracket* an answer:
`WITHIN_CELL_SPREAD < bw < GRID_CELL_SEP` gives `0.004 < bw < 0.05`, i.e. ~0.02 --
exactly the fixture value. A future session dutifully refusing to copy
`_RESOLVABILITY_DEMO_BW` could re-derive it in one line from two numbers presented as
measured substrate facts.

**Applied:** the block is split into MEASURED and "ASSUMED FOR THIS FIXTURE -- NOT
MEASURED", with the bracketing arithmetic spelled out and flagged as an artifact of
the assumed numbers rather than a result.

## F-6 [MAJOR] The `from_dims` kwarg is inert without six unwired siblings

`benefit_terrain_enabled`, `use_da_modulated_rbf_density`, `da_allocation_scale`,
`da_jitter_radius`, `da_bandwidth_narrowing` and `da_benefit_num_centers` are at
**zero of three** wiring sites, so `from_dims(benefit_field_bandwidth=0.02, ...)`
alone arms a bandwidth on a terrain that never turns on -- and F-1's coupling fix
cannot be applied through `from_dims` either. The build's own C4 test has to hand-set
`benefit_terrain_enabled` after the call to make its assertion reachable.

**Applied as documentation only** (a note on the `from_dims` signature entry naming
all six). Wiring six more knobs is beyond this chip's scope and would be a change to
the DA mechanism's public surface, not to this knob.

## Minor findings

- **F-7** `benefit_field_bandwidth = 0.0` is accepted with no validation and makes
  the Gaussian denominator 0, so density *at* a center is `NaN`. `0.0` is the OFF
  idiom for every sibling in the same config block (`da_allocation_scale`,
  `curiosity_weight`), so it is a plausible mistake. **Recorded, not fixed:** shared
  with `harm_field_bandwidth` and `safety_terrain_bandwidth`, and validating all
  three changes harm-field behaviour, which this chip does not authorise.
- **F-8** All three bandwidth knobs default to `None`, so none appears in
  `manifest_core.enabled_default_off_flags` (which reports only `False`/`0`/`0.0`
  defaults). A run at 0.02 and one at the inherited 1.0 are indistinguishable in that
  manifest block. `arm_fingerprint` hashes the whole config so reuse safety is
  unaffected. **EXP-1391 must record the chosen bandwidth in its own `config_slice`**,
  since the criterion is stated "at the chosen bandwidth".
- **F-9** The entry's `familiarity_bandwidth` claim ("already a dedicated knob,
  nothing to wire") is literally true -- it is a dedicated dataclass field and never
  shared `kernel_bandwidth` -- but it is at zero of three `from_dims` sites, i.e.
  weaker than this build's own wiring standard. Contested, not refuted; the family's
  drivers use the direct `HippocampalConfig` constructor. Separately:
  `_curiosity_bonus` computes `density * (1 - familiarity)`, and at the 0.20 default
  on a 0.07 manifold the familiarity factor is *itself* a spatial constant, so
  **arming the benefit knob alone does not make EXP-1392's cross-candidate curiosity
  range non-degenerate.**
- **F-10** `test_c1_default_path_bitidentical_to_config_without_the_attribute` is
  headed "the strong bit-identity proof" but both arms run the NEW code: it proves the
  `getattr` fallback equals the `None`-valued field, not identity with the pre-build
  implementation. It is one of the 5 cells that pass on `863d23d65a`. The real A/B is
  out-of-tree and was run (see Verdict).

## Related, and out of this knob's scope

The `VALENCE_LIKING` channel -- written from `benefit_exposure` by
`agent.py::update_liking` -- is stored on and read from `self.rbf_field`, i.e. at
`effective_harm_bandwidth`, not the benefit field's scale. So the "liking" read stays
spatially saturated on a 0.07 manifold unless `harm_field_bandwidth` is armed too.
Anyone reading "the benefit map now resolves" should not assume the liking channel
moved with it.

## Confirmed sound

Bit-identity across 10 config shapes including the DA cluster path, int
`kernel_bandwidth` preservation, and the full `state_dict`; no fifth benefit consumer
(`RBFLayer(` has exactly three construction sites in `ree_core/`; `integrate()` is
harm-only; `field.py` line ~541 is the one reader of the config field in the repo);
`_PreKnobConfigView` genuinely hides the attribute and asserts that it does;
`test_c3_shared_bandwidth_is_spatially_constant...` is a real discriminator with a
working zero-centers canary; the swallowed-kwarg guard is real; the declared
17-of-22 blind-spot measurement reproduced exactly; the fence against recommending an
operating value is strong on all four copyable surfaces; and the entry's checkable
registry claims hold (258 entries total, no other owner of this gap,
`implemented_pending_validation` + `ready: false` well-precedented).
