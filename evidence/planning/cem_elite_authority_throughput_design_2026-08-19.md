# CEM elite-stage selection authority + behavioural throughput

**Design note for the 2026-08-16 amend to substrate_queue `sd_id: modulatory-bias-selection-authority`.**

- Source spec: `failure_autopsy_931-932-wanting-authority-cluster_2026-08-16.json`,
  target `v3_exq_931_...`, `recommended_substrate_queue_entry.implementation_hint_addendum`
  (confirmed, human-gated 2026-08-16T18:41:10Z by `/governance` cycle `cranky-driscoll-126a36`).
- Chip: `chip-20260819-modulatory-authority-cem-throughput-build`.
- Session: `metaworker-chip-20260819-modulatory-authority-cem-throughput-build` (headless).

This is the FOURTH convergent instance of one bottleneck -- *scoring-layer signals do not
reach the committed argmax* -- after MECH-314 curiosity bias, MECH-320 vigor penalty and
MECH-341 within-class temperature. It is amended into the existing entry, not given a
parallel one, per the autopsy's explicit instruction.

---

## 0. What V3-EXQ-931 measured

Two INDEPENDENT failures at the hippocampal CEM elite-selection stage:

| # | failure | measurement |
|---|---|---|
| (a) | **AUTHORITY** -- the wanting term cannot move the CEM argmin | `wanting_authority_ratio ~= 0.0037` (cross-candidate spread of the wanting term / spread of the terrain term). `selection_flip_rate = 0.0` in 5/5 seeds at the documented operating weight `wanting_weight=0.5`. First flips at w~50; 5/5 seeds at w~500; 0.80 at w=5000. |
| (b) | **THROUGHPUT** -- a flipped CEM argmin does not change behaviour | at `w=5000`, 80.3% of genuine refits flip the elite argmin (43/104, 96/98) while `mean_resource_proximity` is BIT-IDENTICAL to ablation (0.6229773644254133). |

The positive control `P3_instrument_can_detect_authority` fired at 5/5 seeds, so this is a
well-powered NEGATIVE, not a null of unknown power. Fixing (a) alone buys flipped picks and
**no** behavioural change -- which is why the autopsy ranks (b) as the more important half.

Mechanism of (b): `REEAgent.select_action` re-scores the candidate pool with
`self.e3.last_scores`, independently of `HippocampalModule._score_trajectory`'s elite pick.
The CEM elite stage shapes the PROPOSAL DISTRIBUTION; E3 alone decides the COMMITTED action.

---

## 1. Part (a) -- authority at the CEM elite stage

### The structural obstacle

`_score_trajectory` scores ONE trajectory at a time and returns a scalar. Cross-candidate
spread -- the quantity an authority rescale needs -- does not exist inside it. So the
rescale cannot live where the sub-threshold term lives; it has to live at the site that
holds the whole candidate set.

### The fix

1. `_score_trajectory` gains `return_components: bool = False`. When True it returns
   `(score, {"terrain": ..., "modulatory": ...})` where `modulatory` is the **signed
   additive** contribution such that `score == terrain + modulatory`. That sign convention
   is chosen to mirror E3's `scores = scores_raw + scale_factor * modulatory_total`
   exactly, so the two layers read as one mechanism rather than two dialects. All three
   subtracted terms (wanting, curiosity, mode_value) are folded in with their existing
   signs. Default `False` reproduces the current return type and value -- bit-identical.

2. At the CEM elite-selection site (`propose_trajectories`, the `scores_tensor` /
   `argsort` block), when `use_cem_modulatory_authority` is on, per-candidate `terrain`
   and `modulatory` vectors are assembled and the score recomposed as

   ```
   scale  = gain * terrain_spread / modulatory_spread          (spread = range | std)
   scores = terrain + scale * modulatory                       (applied iff spread > floor)
   ```

   before `argsort`. This is E3's algebra verbatim, one layer upstream.

### Config (all no-op defaults, `HippocampalConfig`)

| field | default | meaning |
|---|---|---|
| `use_cem_modulatory_authority` | `False` | master switch |
| `cem_modulatory_authority_gain` | `0.5` | target spread as a fraction of the terrain spread; keep `<1.0` so the term stays subdominant to a decisive terrain gap |
| `cem_modulatory_authority_normalize_basis` | `"range"` | `"range"` (outlier-sensitive, near-tie flips) or `"std"` (robust, competes with the TYPICAL spread) -- same two bases the 2026-06-15 conversion amend added at E3 |
| `cem_modulatory_authority_min_spread_floor` | `1e-6` | below this the rescale is skipped (a flat term cannot be given authority: "scaling zero is still zero", V3-EXQ-648) |

---

## 2. Part (b) -- throughput. **Chosen route, and why**

The autopsy offers two acceptable routes and does not force the choice:

- **(i) propagate the CEM elite pick into E3's committed selection**, or
- **(ii) document the CEM elite stage as ADVISORY-ONLY** so no future experiment reads a
  behavioural DV off it.

**Chosen: a bounded form of (i), plus (ii) as the default posture.** Stated plainly:

**Rejected -- (i) in its literal form (let the CEM pick override E3).** `_score_trajectory`'s
own contract is `ARC-007 STRICT: primary scoring is terrain-only... No independent harm
prediction here -- E3 introduces all value weighting.` E3 is where harm and ethical cost
enter the committed decision. Letting a terrain-plus-wanting argmin bypass E3 would give a
scoring-layer knob authority over the committed action *without* harm weighting -- an
architectural violation with a real safety edge, not merely a style objection.

**Adopted -- route the CEM elite stage's modulatory contribution INTO E3 as a channel,
where it passes through E3's existing, already-validated, bounded authority rescale.**
The 2026-06-10 route-range amendment built exactly this injection point for exactly this
purpose: `channel_route_bias` is documented as *"folded into the modulatory accumulator the
authority rescales, so the channel's cross-candidate range reaches the committed argmax."*
So:

- `propose_trajectories` caches `last_candidate_modulatory_bias` -- a `[K]` tensor of the
  modulatory contribution over the **final returned pool**, index-aligned to the candidate
  list `E3.select` receives. Computed only when the lever is engaged (it costs one residue
  evaluation per candidate), so the default path is zero-cost and bit-identical.
- `agent.py`'s route-source dispatch gains `"cem_elite"`, reading that cache and feeding it
  through the existing parameter-free `project_channel_range` -> `channel_route_bias`.

What this buys: the signal reaches the committed argmin (real behavioural throughput),
E3 remains the sole committed selector (ARC-007 STRICT intact), harm weighting is still
applied downstream of the routed bias, and the authority stays bounded by
`modulatory_authority_gain` -- the safety property the 2026-06-15 amend established. It
also inherits, for free, the inert-route backstop warning added 2026-08-03 (a silently
`None` route source is the V3-EXQ-863 failure shape) and the `modulatory_channel_route_range`
readiness diagnostic.

**And (ii) is the DEFAULT posture, not an alternative to (i).** With every new flag off --
which is the shipped configuration -- the CEM elite stage remains advisory-only and is now
*documented as such at the code site*, so the structural null that cost V3-EXQ-914/914a two
runs is legible before an experiment is designed rather than after it fails. Route (i) is
what an experiment opts INTO when it needs behavioural throughput. Doing only (ii) would
have left the substrate unfixed and the 18 gated claims still blocked.

---

## 3. Part (c) -- the standing readiness assertion

Generalises the 2026-06-10 amendment ("assert cross-candidate range EXISTS") by one step:

> A scoring-layer lever must report the ratio of its own cross-candidate spread to the
> dominant term's, and that ratio must be **COMPETITIVE** -- not merely nonzero -- before
> any behavioural falsifier is queued.

V3-EXQ-931's `wanting_authority_ratio ~= 0.0037` predicts its null directly. A
nonzero-range gate passes at 0.0037; a competitiveness gate does not.

Implemented as a shared helper, `authority_spread_ratio()`, used at BOTH layers so the
statistic has one definition:

- **CEM layer**: `cem_modulatory_authority_ratio` + `cem_modulatory_authority_competitive`
  in the propose diagnostics.
- **E3 layer**: the existing `score_bias_to_raw_range_ratio` gains its companion verdict
  `modulatory_authority_ratio_competitive`.

Floor: `authority_competitive_ratio_floor = 0.1` -- i.e. the lever's spread must be at
least 10% of the dominant term's. Reported, never enforced in the substrate: it is a
READINESS statistic for experiment design, and a substrate that refused to run below the
floor would break every existing default-off configuration. The gate belongs at
`/queue-experiment` time, which is what the amended `substrate_queue` entry records.

---

## 4. Backward compatibility

Every new field defaults to no-op. With defaults:
`return_components=False` -> `_score_trajectory` returns the identical scalar;
`use_cem_modulatory_authority=False` -> `argsort` sees the identical `scores_tensor`;
`modulatory_channel_route_source="none"` -> `channel_route_bias=None`;
`last_candidate_modulatory_bias=None` -> nothing to route.
No existing experiment's behaviour or output changes.

## 5. MECH-094

Not applicable in the write direction. `_score_trajectory` and `_curiosity_bonus` are
read-only over hypothesis-space CEM candidates and write no memory (`_curiosity_bonus`
states this explicitly). No simulation or replay content is produced by this change, so
there is nothing here to carry `hypothesis_tag=True`.

## 6. Phased training

Not applicable. No encoder head is added and nothing here trains; all terms are existing
read-only field evaluations recomposed arithmetically.

## 7. ML/AI engineering notes (Layer 7)

The engineering problem is **scale mismatch between additively-composed score terms**, the
same problem multi-task loss balancing solves (GradNorm, uncertainty weighting). The
adopted technique -- normalise a subordinate term's spread to a fixed fraction of the
dominant term's -- is the standard fix and is already the shipped E3 mechanism; this change
reuses it rather than importing anything new.

Two hazards defended against, both of which have already bitten this lineage:

1. **Catastrophic cancellation in float32.** V3-EXQ-643's dead gate was caused by
   reconstructing the modulatory total as `(scores - scores_raw)` when primary scores had
   exploded to ~1e32, losing a real ~0.17 range below the ULP. Defence: the components are
   tracked EXPLICITLY through `return_components` and never reconstructed by subtraction --
   the same fix that repaired E3 on 2026-06-06.
2. **Amplifying a flat signal.** "Scaling zero is still zero" (V3-EXQ-648). Defence: the
   `min_spread_floor` guard, and the part-(c) competitiveness verdict which reports the
   ratio rather than silently rescaling a near-uniform offset into apparent authority.

No architecture is imported by analogy; the composition is specified by the SD entry and the
autopsy, and the biological grounding (mesolimbic incentive salience as a SELECTION
mechanism -- Berridge wanting/liking) is untouched by a rescaling of magnitudes.

## 8. Scope note -- what this build deliberately does NOT do

No behavioural falsifier is queued. Per part (c) that is gated on this build landing AND on
the spread ratio becoming competitive. A readiness/validation diagnostic for the build
itself is the correct next step; a behavioural falsifier queued now would reproduce
V3-EXQ-931's structural null.
