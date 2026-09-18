# `harm_obs_a` rank-2 scoping spike -- SD-011 / SD-019 / SD-020 / SD-022 / SD-086 / MECH-258

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, substrate_queue.json, experiment_queue.json, or any other registry.**

- Session: `metaworker-science-20260918-sd011-harm-obs-a-rank2-spike` (headless, ree-cloud-5)
- Chip: `chip-20260918-sd011-harm-obs-a-rank2-spike`; campaign `science-20260918-sd011-harm-obs-a-rank2-spike`
- Written 2026-09-18T19:51:24Z against `ree-v3` origin/main `e1ff0927` and `REE_assembly` origin/master `74bd9c16d1`
- Kind: **scoping spike, design doc only**. No `ree_core` edit, no env edit, no experiment queued, no completed run re-adjudicated.
- User decision this executes (2026-09-18T19:19:21Z, Orchestrator decision lane `orchestrate-20260918-1840-cloud4`, real `AskUserQuestion`): *"Build the trainer fix now; scope the env fix first"*, and for SD-086 itself *"D now, then C once the encoder trains"*.
- Upstream finding: `evidence/planning/sd086_zharma_readout_precondition_staged_20260918.md` sections 4a/4b/7/8, and GFLAG-0348.

---

## 0. STOP-CHECK (run at start, 2026-09-18T19:45Z)

- `evidence/planning/` contained no existing `harm_obs_a` / `rank2` scoping doc. Clear.
- `ree-v3` origin/main had no commit touching `ree_core/environment/causal_grid_world.py` after 2026-09-18T19:00Z. Clear.
- `task_claim.py check` on this file's path: no overlap. Claim opened 2026-09-18T19:45:40Z.
- Producer site re-verified live, not taken from the brief (see section 2).

---

## 1. One-paragraph answer

`harm_obs_a`'s rank-2 structure is **not a bug, not a placeholder, and not a deliberate minimal
design**. It is a **regression introduced on 2026-03-28 by a targeted fix for an unrelated defect**
(`ree-v3` `2fbf5d62`, fixing the EXQ-102 autocorrelation-~0 finding), which replaced a genuinely
50-dimensional spatial EMA with two scalars broadcast over 25 dims each, kept the 50-d interface,
and was validated by a criterion (EXQ-106 lag-10 autocorrelation) that is **blind to rank by
construction**. The architecture doc's written spec (`harm_obs_a = EMA(harm_obs_s, tau=10-30)`,
`docs/architecture/sd_011_dual_nociceptive_streams.md`) was never updated and the code has diverged
from it ever since. The registry already carries the ratified remedy -- **SD-022**, registered
2026-04-09, whose own `functional_restatement` diagnoses exactly this defect -- but it is
**default-OFF** (`limb_damage_enabled=False`), and it is 7-d with signal rank 4, not an arbitrary
enrichment. The live exposure is therefore narrower than the finding first suggests (section 4)
and the decision owed is a **containment-and-default question**, not an emergency (section 6).

---

## 2. Measured facts, re-verified this session

### 2a. The producer site (confirmed live at `e1ff0927`)

`ree_core/environment/causal_grid_world.py:3033-3038`:

```python
alpha_a = self.harm_obs_a_ema_alpha
ax2, ay2 = int(self.agent_x), int(self.agent_y)
hazard_at_agent   = float(np.clip(self.hazard_field[ax2, ay2], 0.0, 1.0))
resource_at_agent = float(np.clip(self.resource_field[ax2, ay2], 0.0, 1.0))
self.harm_obs_a_ema[:25] = (1.0 - alpha_a) * self.harm_obs_a_ema[:25] + alpha_a * hazard_at_agent
self.harm_obs_a_ema[25:] = (1.0 - alpha_a) * self.harm_obs_a_ema[25:] + alpha_a * resource_at_agent
```

Two scalars, each broadcast uniformly over 25 dims. GFLAG-0348's measurement (singular values
`[22.597, 6.698, 0, 0, ...]`, exactly 2 distinct column patterns, `col0==col24`, `col25==col49`)
is the arithmetic consequence and is taken as given here; this spike did not re-run it.

### 2b. NEW: the two later writers do not add rank

Two further code paths touch `harm_obs_a_ema` and **neither raises the rank**:

- **Q-080.a effort injection** (`:3080-3081`) adds `alpha_a * eff_harm`, a scalar, to `[:25]`.
  A uniform block plus a scalar stays uniform. Rank still 2.
- **SD-MECH303 safety-proximity EMA** (`:3042-3050`) reads the *same* `hazard_at_agent` scalar but
  writes a **separate** accumulator (`_safety_proximity_ema`), so it neither enriches nor is
  enriched by `harm_obs_a`.

So the rank-2 bound holds for every configuration of the legacy path, not only the raw-warmup one
SD-086 measured.

### 2c. NEW, and it materially narrows the finding: there are TWO `harm_obs_a` paths, not one

`causal_grid_world.py:4145-4163` branches on `limb_damage_enabled`:

| Path | Gate | Shape | Signal rank | Content |
|---|---|---|---|---|
| **Legacy** | `limb_damage_enabled=False` (**default**) | 50 | **2** | `hazard_at_agent` EMA, `resource_at_agent` EMA |
| **SD-022 body** | `limb_damage_enabled=True` | **7** | **4** | `limb_damage[4]`, then `max`, `mean`, `residual_pain` -- all deterministic functions of the same 4 |

The SD-022 path is *not* rank 7: `max`, `mean` and `residual_pain` (`sum * residual_pain_scale`)
are functions of `limb_damage[4]`, so the free dimension count is 4. That is **twice** the legacy
path and, unlike it, is **causally independent of current world proximity** -- which is precisely
what SD-022 was registered to provide. `config.py:8858-8864` auto-sets
`latent.harm_obs_a_dim = 7` when the flag is on, so the encoder side already follows.

### 2d. SD-048 noise does not repair the rank

`_apply_interoceptive_noise` (`:5006-5128`) can add full-rank i.i.d. Gaussian autonomic noise to
the readout. That raises the *numerical* rank and lowers nothing: it is noise, not signal, so the
**mutual information** about the world stays capped at the 2 (or 4) underlying scalars. It does,
however, matter for RNG comparability -- see section 5c.

### 2e. Provenance: when and why it was written this way

| Commit | Date | What it did |
|---|---|---|
| `db45993a` | 2026-03-24 | **Original construction.** `harm_obs_a_ema` = EMA of the *50-dim proximity vector* (`hazard_field_view[25] + resource_field_view[25]`) at tau ~ 20. Genuinely high-rank; matches the architecture doc. |
| `2fbf5d62` | 2026-03-28 | **The regression.** "replace spatial 5x5 window EMA with agent-centered scalar accumulator. EXQ-102 root cause: window content changes each step as agent moves (autocorr~0). Fix: EMA hazard/resource at agent cell into all 25 dims per channel." |
| `8acc9477` | 2026-03-28 | EXQ-106a episode-reset bug fix (same lineage). |
| `65eb8cf6` | 2026-04-08 | SD-011 second source (`harm_history`) added *alongside*, not replacing. |
| `a75d4cc8` / `b257e7ad` | 2026-07-09 / 2026-08-14 | Q-080 effort injection, MECH-303 proximity EMA (section 2b). |

The in-code comment at `:3026-3032` states the tradeoff explicitly and honestly -- "Interface stays
50-dim" -- so nothing was hidden. What was never done is the follow-through: **the fix traded rank
for autocorrelation, and no criterion anywhere in the evidence base ever checked the side of the
trade that was given up.**

---

## 3. (a) What the specs and the biology say `harm_obs_a` SHOULD carry

### 3a. Biology first (as the chip asked)

The claims cite four independent lines, and they do **not** all point the same way on
dimensionality:

- **Melzack & Casey 1968; Rainville et al. 1997 (*Science*); Craig 2002/2003/2009.** The
  affective-motivational (C-fiber / medial paleospinothalamic -> ACC/insula) pathway is
  *diffuse and poorly localized* -- classically "second pain". **This cuts AGAINST the original
  spec**: an affective stream that carried a 25-cell spatial hazard map would be *too*
  discriminative for the pathway it models. On this reading, low dimensionality is correct and
  the 2026-03-28 change moved *toward* the biology, not away from it.
- **Woolf & Salter 2000 (C-fiber temporal summation / wind-up), cited on SD-019.** Requires
  **accumulation with a slow, separately-parameterised recovery** -- i.e. at minimum a second
  timescale distinguishable from the encoding timescale. The current construction has **one**
  `alpha_a` for both channels and no separate recovery rate: wind-up and decay are the same
  constant.
- **Craig 2003 (lamina I / VMpo / insula as the interoceptive *body-state* route), cited on
  SD-019 and SD-022.** Requires the affective stream to carry **body state, not world
  proximity**. The legacy path carries *only* world proximity at the agent's cell. This is the
  gap SD-022 exists to close.
- **Chen 2023 / Hoskin 2023 / Horing 2022 (AIC encodes unsigned intensity PE, not magnitude),
  cited on SD-020 and MECH-258.** Requires **surprise to be separable from magnitude**. Two
  co-evolving single-tau EMAs of the same two scalars cannot carry both.

**Synthesis.** The biology demands *low-dimensional but multi-functional*: diffuse (no spatial
map) yet carrying at least three separable quantities -- accumulated load with its own recovery,
body state independent of world proximity, and surprise distinct from magnitude. Rank 2 at a
single time constant satisfies the first requirement and **none of the other three**. So "diffuse
is right" is a real defence of the *direction* of the 2026-03-28 change and **not** a defence of
its *magnitude*.

### 3b. The formal specs

- **`docs/architecture/sd_011_dual_nociceptive_streams.md`** states the spec as
  `harm_obs_a = EMA(harm_obs_s, tau=10-30_steps)`. `harm_obs_s` is the 51-d sensory vector. **The
  shipped code does not implement this and has not since 2026-03-28.** The doc still carries
  `status: stable`, `status_asof: 2026-07-10`.
- **SD-011 `what_would_answer` (iii)** already requires every run scored against SD-011 to
  **state its sourcing mode**, citing V3-EXQ-917's measured AUC divergence between the two paths.
  The registry therefore already knows the two paths are not interchangeable; what it does not
  record is *why* -- the rank gap in section 2c.
- **SD-019** requires "nonredundant temporal integration with persistence and slower recovery" and
  is explicitly violated by "a delayed, smoothed, or monotone-transformed copy of `z_harm_s`".
  On the legacy path `harm_obs_a` **is** a smoothed transform of a scalar read out of the same
  hazard field `harm_obs_s` reads. EXQ-241b's `r2_s_to_a = 0.996` is that fact, measured.
- **SD-022 `functional_restatement`** is the sharpest statement already in the registry:
  *"harm_obs_a is currently an EMA of hazard/resource proximity fields -- structurally identical to
  harm_obs with a slower time constant ... The EMA-based harm_obs_a is superseded by the
  damage-state source when limb_damage_enabled=True."*
  **Correction owed to that sentence:** post-2026-03-28 the legacy path is not "structurally
  identical to harm_obs with a slower time constant" -- it is strictly *poorer* than that, being
  two scalars rather than a smoothed 50-d field. SD-022's diagnosis describes the **pre-2026-03-28**
  construction. This is a `stale_note`-class correction for /governance, not a status change.

### 3c. Verdict

**Regression, with a ratified-but-default-off remedy.** Specifically:

1. Not a **bug** in the sense of an unintended coding error -- the commit message states the design.
2. Not a **placeholder** -- nothing marks it provisional, and four SD-011-supporting runs were
   scored on it.
3. Not a **deliberate minimal design** -- no claim, doc or note asserts that rank 2 is sufficient;
   the architecture doc asserts something different, and SD-022 asserts it is insufficient.
4. It **is** a regression: a fix for defect A (autocorrelation) that silently created defect B
   (rank collapse), where defect B is invisible to every criterion in the evidence base.

In work-graph debt vocabulary the *finding* was `complex (probe-gated)`; **this spike was the
probe**, and it resolves to `puzzle (known rules)` -- the rules are known (what the affective
stream must carry, section 3a), and what is missing is one decision about which construction to
build and how to contain it (section 6).

---

## 4. (b) Which completed experiments' conclusions depend on >2 d.o.f.

**Listed for /governance. Not re-adjudicated here; no `evidence_direction` is proposed.**

Method: pulled every `exp:simulation` entry for SD-011/SD-019/SD-020/SD-022/SD-086/MECH-258 from
`evidence/experiments/claim_evidence.v1.json` (71 entries), then read each *live* (non-superseded,
non-`non_contributory`) supporting run's driver for `limb_damage_enabled`.

### 4a. Sourcing-mode split of the live supporting runs

| Run id | Claim(s) | Direction | Path |
|---|---|---|---|
| `v3_exq_106_harm_obs_a_temporal_persistence_20260428T171409Z_v3` | SD-011 | supports/PASS | **legacy (rank 2)** |
| `v3_exq_178b_sd011_dual_stream_dissociation_20260330T193525Z_v3` | SD-011 | supports/PASS | **legacy (rank 2)** |
| `v3_exq_198_sd011_dual_stream_stability_20260401T232341Z_v3` | SD-011 | supports/PASS | **legacy (rank 2)** |
| `v3_exq_472_sd011_platform_stability_pilot_20260421T183651Z_v3` | SD-011 | supports/PASS | **legacy (rank 2)**, `harm_history_len=10` |
| `v3_exq_463_mech268_dacc_conflict_saturation_v3_20260421T180917Z_v3` (+`...T202354Z`) | MECH-258 | supports/PASS | **neither** -- synthetic `z_harm_a = [1,0,0,0]` unit-contract fixture, never reads env `harm_obs_a` |
| `v3_exq_319_sd022_harm_stream_dissociation_20260410T093948Z_v3` | SD-011, SD-022 | supports/PASS | SD-022 body (rank 4) |
| `v3_exq_323a_sd019_harm_nonredundancy_20260416T172811Z_v3` | SD-011, SD-019, SD-022 | supports/PASS | SD-022 body (rank 4) |
| `v3_exq_324b_sd020_harm_surprise_pe_*` (3 runs, 2026-04-18/19) | SD-020 | supports/PASS | SD-022 body (rank 4) |
| `v3_exq_917_mech303_harm_threshold_calibration_battery_20260811T205119Z_v3` | SD-011 | supports/PASS | SD-022 body (rank 4) |

### 4b. Of the legacy-path runs, which conclusions actually REQUIRE rank > 2?

Read against each run's own pre-registered criteria:

- **EXQ-178b** -- C1 `harm_fwd_r2 >= 0.20` (on `z_harm_s`, not `z_harm_a`), C2 `stream_corr <= 0.85`
  (correlation of two **norms**), C3 `autocorr_gap >= 0.10` (lag-10 autocorr of **norms**), C4
  `z_harm_s_hazard_corr >= 0.25` (on `z_harm_s`). **Every `z_harm_a`-touching criterion is a scalar
  statistic of the norm. None requires rank > 2.**
- **EXQ-198** -- C1-C4 replicate 178b; C5 composite `dissociation_score`; C6 seed stability. Same
  finding: all norm-based.
- **EXQ-106** -- criterion is lag-10 autocorrelation of `harm_obs_a`. **Rank-blind by construction,
  and the rank-2 change is what produces the pass.** This run *validates the commit that created
  the finding*.
- **EXQ-472** -- platform-stability / checkpoint-round-trip pilot; norm-based.
- **EXQ-463** -- does not read env `harm_obs_a` at all (fixture). **Unexposed.**

**So: NO completed run's pre-registered criterion is arithmetically invalidated by the rank-2
finding.** That is a genuine, and deliberately unglamorous, result of this spike.

### 4c. What IS exposed, stated precisely

The exposure is **construct validity, not arithmetic**. Two specific items for /governance:

- **C2 `stream_corr <= 0.85` and C3 `autocorr_gap >= 0.10` (EXQ-178b, EXQ-198) pass for a reason
  that is not the reason SD-011 asserts.** On the legacy path both streams read the same hazard
  field; the affective norm decorrelates from the sensory norm because of **temporal smoothing at
  a single tau**, not because of nonredundant content. SD-019 was registered 2026-04-08 to sharpen
  exactly this ("invalid if it is recoverable as a simple lagged or monotone mapping"), and
  EXQ-241b then measured `r2_s_to_a = 0.996` on this same substrate. The rank-2 measurement is a
  **structural explanation** for a redundancy the registry had already measured empirically -- it
  strengthens the existing record rather than overturning it.
- **SD-011's live supporting base splits cleanly by path.** Its four validated results are
  EXQ-178b and EXQ-198 (legacy, rank 2) and EXQ-323a plus the D3-reversal resolution (SD-022 body,
  rank 4). A governance reading of SD-011's evidence that does not carry that split forward is
  under-scoped; SD-011's own `what_would_answer` (iii) already demands the sourcing mode be stated,
  so this is enforcement of an existing rule, not a new one.

Everything downstream of `z_harm_a`'s **degenerate range** -- MECH-258's forward-R2, SD-086/SD-087,
Q-086 -- is **already** covered by GFLAG-0210/0212/0348 and is deliberately not restated as new
exposure here.

---

## 5. (c) Candidate richer constructions

All three keep the trajectory-following property EXQ-102/EXQ-106 established as mandatory (the
readout must follow the agent, not the window), and all three keep the affective stream
**non-spatial** in line with section 3a's biology.

### 5a. C1 -- Multi-timescale scalar bank (RECOMMENDED)

Replace the single `alpha_a` with `K` EMAs of the same two scalars at different time constants
(e.g. tau = 2, 5, 20, 60, 200), emitting `2K` dims.

- **Rank:** 2K (10 at K=5). Directly supplies the **wind-up vs recovery** separation Woolf & Salter
  2000 requires and SD-019 asks for, and gives SD-020/MECH-258 a substrate on which "surprise"
  (fast-tau minus slow-tau) is **representable in the observation** rather than reconstructed
  downstream.
- **Cost:** ~15 lines in `causal_grid_world.py` (a `(K,2)` array, one vectorised EMA update, one
  flatten at readout), plus the `config.py` wiring precedent already set by SD-022 at `:8858-8864`
  (set `latent.harm_obs_a_dim = 2K`). No new module. ~1 session including contract tests.
- **Biology:** strongest fit. Diffuse (no spatial map) *and* multi-timescale, which is the actual
  C-fiber phenomenology.
- **Risk:** changes `harm_obs_a`'s **shape** -> see 5c, this is the RNG-hazardous class.

### 5b. C2 -- Allocentric per-cell exposure map

Maintain a persistent per-cell hazard/resource *exposure* accumulator over the whole grid
(incremented only at the agent's current cell, decayed globally), and read the agent-centred 5x5
window out of **that** instead of out of the instantaneous field.

- **Rank:** up to 50. This is what the architecture doc's spec (`EMA(harm_obs_s)`) *meant* to be,
  and unlike the pre-2026-03-28 construction it **does not have the EXQ-102 defect**: because
  accumulation is allocentric and the readout is egocentric, window content persists across agent
  motion instead of being destroyed by it.
- **Cost:** two `size x size` float arrays (trivial at grid scale), O(1) update, O(25) readout;
  ~25 lines. Also ~1 session.
- **Biology:** **weakest fit of the three.** It gives the affective stream a spatial map, which is
  the A-delta / S1 property, not the C-fiber / ACC one (section 3a). Recorded because it is the
  construction the written spec implies and the one a reader of that doc would expect -- **and it
  should probably be rejected on the biology**, which is itself worth writing down.
- **Risk:** keeps 50 dims, so it is the only candidate that is **RNG-shape-neutral** (5c).

### 5c. C3 -- Flip the SD-022 body path on by default

No new code: set `limb_damage_enabled=True` as the default.

- **Rank:** 4, in 7 dims. Doubles the legacy path and is the only option that delivers the
  **body-state independence** Craig 2003 and SD-022 require.
- **Cost:** zero implementation. But SD-022 is only `provisional`, the flag also enables
  movement-failure stochastics (`:2915`, `self._rng.random() < damage * failure_prob_scale`), and
  it changes agent dynamics, not only the observation. It is a **behavioural** default change
  wearing an observation change's clothes.
- **Assessment:** should **not** be a silent default flip. It is a legitimate *third arm* in any
  comparison and a legitimate governance question in its own right, but as a default it changes
  more than the thing under discussion.

### 5d. Effect on fixed-seed RNG streams -- the part that must not be got wrong

`causal_grid_world.py` uses **one** generator, `self._rng = np.random.default_rng(seed)`
(`:1604`), at **54 call sites** including hazard placement (`:4239`, `:4283-4284`), movement
failure (`:2915`), scheduled limb damage (`:3156`), external hazards (`:3201`), transients
(`:3338`) and SD-048 autonomic noise (`:5096`). Two distinct ways a construction change
desynchronises it:

1. **Shape-driven (silent, and the one that catches people).** SD-048's autonomic noise draws
   `self._rng.standard_normal(size=out.shape)` on `harm_obs_a`. Changing `harm_obs_a` from 50 dims
   to 2K dims changes the number of variates consumed **per tick**, so the shared generator
   advances differently and **every other stochastic element of the env diverges at the same
   seed** -- hazard layout included. This fires only when `interoceptive_noise_enabled` **and**
   `autonomic_noise_enabled` are on, which makes it intermittent and therefore worse.
   **C1 and C3 are exposed to this; C2 is not** (50 dims in, 50 dims out).
2. **Behaviour-driven (unavoidable, applies to all three).** A richer `harm_obs_a` changes
   `z_harm_a`, which changes selection, which changes the action sequence, which changes *when*
   the movement-failure and scheduled-injection draws happen. **No flag design can preserve
   fixed-seed comparability in the ON arm.** Say so rather than designing around it.

### 5e. Containment: what a default-off flag does and does not buy

The repo's established convention -- SD-047 (`multi_source_dynamics_enabled`: "RNG draws guarded
inside the master if so seed sequences for existing experiments are bit-identical when disabled")
and SD-048 (`interoceptive_noise_enabled`: "no RNG draws, no state advance, zeroed counters") -- is
the right pattern and should be followed exactly:

- **What it buys:** the OFF path stays **bit-identical**, so every pre-change run, every minted
  baseline arm and every fixed-seed comparison *that does not cross the flag* remains valid and
  reusable. This is the whole containment, and it is sufficient for the existing evidence base.
- **What it does NOT buy:** any comparison **spanning** the flag. Concretely, an arm minted before
  the change cannot be reused in an ON arm; per `evidence/planning/arm_reuse_fingerprint_plan.md`
  and `evidence/experiments/arm_fingerprint_index.json` (`arm_fp/v1`), the flag must be part of the
  arm fingerprint so reuse is **refused** rather than silently granted. **Any experiment testing
  the new construction must mint its own baseline in-line** (CLAUDE.md "Experiment Scripts": the
  first run of a lineage IS the mint).
- **Named requirement for whoever builds this:** the flag must gate the construction **and** the
  emitted shape together, so that in the OFF arm `harm_obs_a.shape == (50,)` and the SD-048 draw
  count is unchanged. A build that changes the shape unconditionally and only gates the *content*
  breaks bit-identity through route 1 above while appearing to be default-off.

---

## 6. (d) Recommended `substrate_queue` candidate entry -- **NOT APPLIED**

Proposed only. `/governance` ratifies (Step 2b/4/6a) before anything is written.

```json
{
  "sd_id": "harm-obs-a-rank2-enrichment",
  "title": "harm_obs_a is structurally rank 2 on the default path: two scalars broadcast over 25 dims each, capping every z_harm_a readout at 2 d.o.f.",
  "node_class": "puzzle (known rules)",
  "status": "candidate_pending_governance",
  "status_phase": "decision_owed",
  "severity": "degrading",
  "ready": false,
  "priority": 2,
  "design_doc": "evidence/planning/harm_obs_a_rank2_scoping_staged_20260918.md",
  "substrate_paths": [
    "ree_core/environment/causal_grid_world.py::step",
    "ree_core/environment/causal_grid_world.py::_get_observation_dict",
    "ree_core/utils/config.py"
  ],
  "depends_on_unresolved": [],
  "unblocks_claims": ["SD-011", "SD-019", "SD-020", "SD-086", "MECH-258"],
  "failure_record": [],
  "implementation_hint": "Add a default-off env flag harm_obs_a_construction ('scalar_broadcast' default | 'multiscale_bank'). Multiscale bank = K EMAs of hazard_at_agent and resource_at_agent at K time constants, emitting 2K dims; wire latent.harm_obs_a_dim = 2K in config.py following the SD-022 precedent at config.py:8858-8864. OFF path must be BIT-IDENTICAL including the emitted shape (50,), because SD-048 autonomic noise draws standard_normal(size=harm_obs_a.shape) off the SHARED env RNG -- a shape change desynchronises hazard placement and every other stochastic element at the same seed. Comparisons spanning the flag are NOT fixed-seed comparable; the flag must enter the arm fingerprint so pre-change baselines are refused for reuse, and any validating experiment mints its own baseline in-line.",
  "metric_trajectory": {
    "primary_metric": "numerical_rank(harm_obs_a) over a >=500-tick rollout",
    "primary_metric_description": "Free dimension count of the affective observation. Bounds the information any z_harm_a readout -- norm or trained head -- can carry about the world.",
    "direction": "higher_is_better",
    "target": "rank >= 4 with at least two distinguishable time constants (SD-019 wind-up-vs-recovery)",
    "current_blocker": "Default path emits two scalars at ONE time constant (causal_grid_world.py:3037-3038, since ree-v3 2fbf5d62, 2026-03-28)",
    "observations": [
      "2026-04-08 EXQ-241b: r2_s_to_a = 0.996 on the legacy path -- the redundancy, measured empirically",
      "2026-08-11 V3-EXQ-917: safe/unsafe AUC ~0.500 under SD-022 damage sourcing vs up to 0.969 under legacy proximity sourcing -- the two paths are not interchangeable readouts",
      "2026-09-18 SD-086 probe (GFLAG-0348): singular values [22.597, 6.698, 0, 0]; numerical rank EXACTLY 2; z_harm_a 97.1% variance in PC1",
      "2026-09-18 this spike: SD-022 body path is 7-dim with signal rank 4 (max/mean/residual_pain are functions of limb_damage[4]); Q-080 effort injection and the MECH-303 proximity EMA add no rank"
    ],
    "prediction": "A K=5 multiscale bank yields rank 10 with lag-10 autocorrelation preserved at the slow taus, so EXQ-106's temporal-persistence criterion continues to pass while SD-019's nonredundancy criterion becomes non-trivially testable on the DEFAULT path for the first time."
  },
  "validation_experiment": null,
  "added_session": "metaworker-science-20260918-sd011-harm-obs-a-rank2-spike",
  "added_utc": "2026-09-18T19:51:24Z",
  "origin": "Scoping spike off GFLAG-0348 / SD-086 refusal, under the 2026-09-18T19:19:21Z user decision 'Build the trainer fix now; scope the env fix first'. PROPOSED ONLY -- not applied; /governance ratifies."
}
```

### The decision the user must make

**One question, three options.** It is a `STOP` under the consent rule -- it changes what gets
measured on the default path for SD-011/SD-019/SD-020 -- so it is raised here and **not** decided
by this session.

> **Given that (i) no completed run's pre-registered criterion is invalidated (section 4b), (ii) the
> registry's own ratified remedy SD-022 already exists at rank 4 but is default-off, and (iii) any
> enrichment breaks fixed-seed comparability in its ON arm and, if it changes shape, risks breaking
> the OFF arm too (section 5d route 1) -- which do we do?**

- **Option 1 -- Build C1 (multiscale bank), default-off.** ~1 session. Gives the default path a
  substrate on which SD-019's nonredundancy and SD-020's surprise-vs-magnitude are testable for the
  first time. Cost: the shape-change RNG hazard must be handled exactly as 5e specifies, and every
  ON-arm experiment mints its own baseline. **This session's recommendation**, because it is the
  only option that addresses the biology's *unmet* requirements (3a) rather than the one it already
  meets.
- **Option 2 -- Do not build; scope-note instead.** Add the rank-2 fact to SD-011/SD-019's
  `what_would_answer` as a mandatory sourcing declaration (extending the existing clause (iii)),
  correct SD-022's stale `functional_restatement` sentence (3b), and route all future SD-011-family
  work to the SD-022 body path. **Zero substrate risk, zero comparability break.** Weaker: rank 4
  is still below what SD-020/MECH-258 need, and it leaves the default path degraded.
- **Option 3 -- Build C2 (allocentric exposure map).** Matches the written architecture spec and is
  RNG-shape-neutral. **This session recommends against it** on the biology (3a): it re-introduces a
  spatial map into the pathway whose defining property is that it has none. If chosen, the
  architecture doc is right and section 3a is the thing to argue with.

**Recommendation: Option 1, with Option 2's scope-note and SD-022 correction done regardless of
which is chosen** -- those are cheap, are owed independently, and do not touch the substrate.

---

## 7. Governance registration -- no new flag raised, deliberately

The chip said to register the finding "if no flag already covers it (the SD-086 session raised one
-- check first, do not duplicate)". Checked: **GFLAG-0348** (open, `evidence_discrepancy`, claims
`SD-086` + `SD-011`, raised 2026-09-18T18:52:46Z by `metaworker-science-20260918-sd086-zharma-readout`)
carries the rank-2 measurement and names the SD-011 second-order finding explicitly. **No new flag
was raised.**

Two amendments for /governance to make **on GFLAG-0348 when it adjudicates** -- as widenings of
that flag, not as a second near-duplicate flag (STEWARD D-006 exists precisely to catch that shape):

1. **Widen `claim_ids`** from `[SD-086, SD-011]` to include **SD-019, SD-020, SD-022, MECH-258** --
   sections 3a/3b establish that each carries an unmet requirement traceable to this construction.
2. **Record the sourcing-mode split** (section 4a) and the `stale_note`-class correction to SD-022's
   `functional_restatement` (section 3b). If governance prefers, the SD-022 sentence is cleanly
   separable as its own `stale_note` flag; it is recorded here rather than raised so that this
   session does not pre-empt that call.

---

## 8. Scope discipline -- what this spike did NOT do

- **Did not edit `ree_core` or the environment.** No code change of any kind.
- **Did not queue an experiment** and did not author a driver.
- **Did not re-adjudicate any completed run.** Section 4 lists run ids and their sourcing mode;
  no `evidence_direction` change is proposed anywhere in this document.
- **Did not re-run GFLAG-0348's measurements.** Section 2a takes them as given and cites them;
  the new measurements in 2b/2c/2e are code and git reads, not rollouts.
- **Did not write to `claims.yaml`, `substrate_queue.json`, `experiment_queue.json`,
  `governance_flags.v1.json`, or the curation ledger.**

## 9. Reproduction

All read-only, all from `REE_Working` on ree-cloud-5 at the heads named in the header:

```bash
BASE=/Users/dgolden/REE_Working
# 2a/2b/2c -- producer site, the two later writers, the two-path branch
sed -n '3026,3085p'  $BASE/ree-v3/ree_core/environment/causal_grid_world.py
sed -n '4136,4165p'  $BASE/ree-v3/ree_core/environment/causal_grid_world.py
sed -n '8855,8870p'  $BASE/ree-v3/ree_core/utils/config.py
# 2d/5d -- SD-048 noise, and the single shared generator
sed -n '5006,5128p'  $BASE/ree-v3/ree_core/environment/causal_grid_world.py
grep -n 'self\._rng' $BASE/ree-v3/ree_core/environment/causal_grid_world.py | wc -l   # 54
# 2e -- provenance
git -C $BASE/ree-v3 log --format='%h %ad %s' --date=short -S 'harm_obs_a_ema' -- ree_core/environment/causal_grid_world.py
git -C $BASE/ree-v3 show 2fbf5d62 --stat
git -C $BASE/ree-v3 show db45993a -- ree_core/environment/causal_grid_world.py
# 4a -- evidence entries, then sourcing mode per driver
python3 -c "import json;d=json.load(open('$BASE/REE_assembly/evidence/experiments/claim_evidence.v1.json'));print([ (e['claim_id'],e.get('run_id'),e.get('evidence_direction')) for e in d['entries'] if e.get('claim_id') in {'SD-011','SD-019','SD-020','SD-022','SD-086','MECH-258'} and str(e.get('evidence_class','')).startswith('exp')])"
grep -c 'limb_damage_enabled=True' $BASE/ree-v3/experiments/v3_exq_178b_sd011_dual_stream_dissociation.py   # 0
grep -c 'limb_damage_enabled=True' $BASE/ree-v3/experiments/v3_exq_323a_sd019_harm_nonredundancy.py         # 6
```
