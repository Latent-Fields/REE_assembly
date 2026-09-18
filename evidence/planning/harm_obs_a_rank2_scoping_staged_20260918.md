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
- **Correction, added post-red-team:** the STOP-CHECK as run searched `evidence/planning/` for a
  *document* but did not search `substrate_queue.json` for an *entry*. It should have. The entry
  `sd_zharm_a_warmup_optimizer_group` (updated 2026-09-18) already carries the rank-2 fact in its
  `severity_note_2026_09_18` and an `affected_completed_runs_candidates_2026_09_18` list -- prior
  work on this chip's question (b). It is incorporated in section 4e. That entry is the **trainer**
  lever (the affective encoder has no optimizer group); the entry proposed in section 6 is the
  **env-construction** lever. They are siblings, not duplicates -- see 6a.
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
**default-OFF** (`limb_damage_enabled=False`), and it is 7-d with 4 free dimensions, not an
arbitrary enrichment. **No completed run's pre-registered criterion is arithmetically invalidated**
(section 4b) -- but SD-011's *own* registered precondition, applied for the first time, classifies
two of its four validated results as **vacuous tests of SD-011** for an adjacent reason the rank-2
measurement explains (section 4d). The decision owed is therefore a **containment-and-default
question plus three corrections**, not an emergency (section 6).

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
- **SD-MECH303 safety-proximity EMA** (`:3049-3053`) reads the *same* `hazard_at_agent` scalar but
  writes a **separate** accumulator (`_safety_proximity_ema`), so it neither enriches nor is
  enriched by `harm_obs_a`.

So the rank-2 bound holds for every configuration of the legacy path, not only the raw-warmup one
SD-086 measured.

### 2c. NEW, and it materially narrows the finding: there are TWO `harm_obs_a` paths, not one

`causal_grid_world.py:4144-4163` branches on `limb_damage_enabled`:

| Path | Gate | Shape | Signal rank | Content |
|---|---|---|---|---|
| **Legacy** | `limb_damage_enabled=False` (**default**) | 50 | **2** | `hazard_at_agent` EMA, `resource_at_agent` EMA |
| **SD-022 body** | `limb_damage_enabled=True` | **7** | **4 free / 5 numerical** | `limb_damage[4]`, then `max`, `mean`, `residual_pain` -- all deterministic functions of the same 4 |

The SD-022 path is *not* rank 7: `max`, `mean` and `residual_pain` (`sum * residual_pain_scale`)
are all deterministic functions of `limb_damage[4]`, so the **free dimension count is 4**.

**The two rank numbers must not be conflated, and the first draft of this doc did conflate them.**
`mean` and `residual_pain` are *linear* in `limb_damage`, but `max()` is **not** in their linear
span, so the **numerical** rank of the 7-d body vector is **5**, not 4 (measured on 2000 uniform
draws: singular values `[67.24, 13.31, 13.13, 12.70, 6.01, 0, 0]`). The legacy path's "rank 2" is a
*numerical* rank. So the like-for-like comparison is **2 vs 5**, and the
information-theoretic one is **2 vs 4**. Either way the SD-022 path is **at least twice** the
legacy path and, unlike it, is **causally independent of current world proximity** -- which is
precisely what SD-022 was registered to provide. `config.py:8862-8864` auto-sets
`latent.harm_obs_a_dim = 7` when the flag is on, so the encoder side already follows.

This distinction is load-bearing for section 6: a naive acceptance target of "numerical rank >= 4"
would be **already satisfied by simply flipping `limb_damage_enabled` on**, and would therefore
fail to discriminate the construction this spike is actually proposing.

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
  cited on SD-020** -- and the same substance, on **Seymour 2019 (*Neuron*), pain-as-precision**,
  which is MECH-258's own grounding (the first draft mis-attributed the 2022/2023 AIC citations to
  MECH-258; they are SD-020's). Requires **surprise to be separable from magnitude**. Two
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

**Stated scope limit (post-red-team).** That six-claim filter is **narrower than the question**, and
a conclusion of the form "no completed run is invalidated" cannot be established from it alone.
Section 4d widens the population; section 4e incorporates a pre-existing candidate list this spike's
STOP-CHECK missed. Even after both, the sweep is not exhaustive, and the conclusion in 4b should be
read as *"nothing found, over a population that is now stated"*, not as a proof of absence.

### 4a. Sourcing-mode split of the live supporting runs

`scoring_excluded` is copied verbatim from `claim_evidence.v1.json`: it is what determines whether
an entry actually weights governance confidence, and three of these six legacy-path entries are
already excluded.

| Run id | Claim(s) | Direction | `scoring_excluded` | Path |
|---|---|---|---|---|
| `v3_exq_106_harm_obs_a_temporal_persistence_20260428T171409Z_v3` | SD-011 | supports/PASS | -- | **legacy (rank 2)** |
| `v3_exq_178b_sd011_dual_stream_dissociation_20260330T193525Z_v3` | SD-011, ARC-033 | supports/PASS | -- | **legacy (rank 2)** |
| `v3_exq_198_sd011_dual_stream_stability_20260401T232341Z_v3` | SD-011 | supports/PASS | **`superseded`** | **legacy (rank 2)** |
| `v3_exq_472_sd011_platform_stability_pilot_20260421T183651Z_v3` | SD-011 | supports/PASS | **`diagnostic_probe`** | **legacy (rank 2)**, `harm_history_len=10` |
| `v3_exq_463_mech268_dacc_conflict_saturation_v3_20260421T180917Z_v3` (+`...T202354Z`) | MECH-258, MECH-268, SD-032b, SD-034 | supports/PASS | **`diagnostic_probe`** | **neither** -- synthetic `z_harm_a = [1,0,0,0]` unit-contract fixture (driver `:219`), never constructs an env |
| `v3_exq_319_sd022_harm_stream_dissociation_20260410T093948Z_v3` | SD-011, SD-022 | supports/PASS | -- | SD-022 body |
| `v3_exq_323a_sd019_harm_nonredundancy_20260416T172811Z_v3` | SD-011, SD-019, SD-022 | supports/PASS | -- | SD-022 body |
| `v3_exq_324b_sd020_harm_surprise_pe_*` (3 runs, 2026-04-18/19) | SD-020 | supports/PASS | -- | SD-022 body |
| `v3_exq_917_mech303_harm_threshold_calibration_battery_20260811T205119Z_v3` | SD-011 | supports/PASS | **`diagnostic_probe`** | **BOTH** -- it crosses `num_hazards` with `SOURCING_MODE` (`damage_sourced` x `proximity_ema_sourced`) by design; driver docstring `:30`. It is the one run that *measured* the two paths against each other. |

**Net: only two unexcluded, live, legacy-path supporting entries exist -- EXQ-178b and EXQ-106.**
EXQ-198 is `superseded` and EXQ-472/463/917 are `diagnostic_probe`, so they do not weight
confidence today regardless of what this spike concludes about them.

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

### 4d. The sharper exposure the first draft missed: SD-011's OWN clause (i) calls two of its four validated results VACUOUS

SD-011's `what_would_answer` opens with a non-degeneracy precondition whose clause (i) reads, verbatim:

> *"SECOND SOURCE LIVE. LatentStackConfig.harm_history_len defaults to 0. At 0, AffectiveHarmEncoder
> receives only harm_obs_a and z_harm_a is a monotone transform of the sensory stream -- the D3
> reversal documented in the 2026-04-06 governance meta. A run with harm_history_len=0 is **VACUOUS**
> as an SD-011 test regardless of what its stream_corr reads, and must be reported as such rather than
> as a weakens."*

Measured against the drivers: **EXQ-178b (`:158`), EXQ-198 (`:196`) and EXQ-323a (`:326`) all
construct `AffectiveHarmEncoder(harm_obs_a_dim=..., z_harm_a_dim=...)` with no `harm_history_len`
argument**, so they take the default `0` (`ree_core/latent/stack.py:208-209`). Only EXQ-472 sets
`harm_history_len=10` -- and EXQ-472 is `scoring_excluded: diagnostic_probe`.

Two consequences, both for /governance and neither adjudicated here:

1. **Section 4c understates the exposure.** It is not only that C2/C3 pass "for a reason that is not
   the reason SD-011 asserts": on the legacy path at `harm_history_len=0`, SD-011's own registered
   rule classifies those runs as **vacuous tests of SD-011**. The rank-2 measurement explains *why*
   the rule was right -- with only `harm_obs_a` as input and `harm_obs_a` carrying two scalars,
   `z_harm_a` cannot be anything but a transform of the sensory stream.
2. **SD-011's `what_would_answer` contains a factual error about its own evidence base.** It states
   that its four validated results (EXQ-178b, EXQ-198, EXQ-323a, the D3-reversal resolution) "were
   ALL obtained in one specific regime ... harm_history_len=10". Three of the four named drivers use
   the default `0`. This is a `stale_note`-class correction, owed regardless of any decision in
   section 6.

This is the single most consequential finding of the spike and it is **not** a new rule -- it is the
registry's existing rule, applied to its own evidence for the first time.

### 4e. Population checked beyond the six claims, and the prior candidate list

Widened after the red-team, by scanning for drivers that read env `harm_obs_a` or measure a
`z_harm_a` quantity outside the six-claim filter:

| Run / driver | Claim | DV shape | Exposed? |
|---|---|---|---|
| `v3_exq_854_sd036_gaba_tone_dose_response_*` | SD-036 | `harm_a_sustain_ratio` = mean/peak of **`\|\|z_harm_a\|\|`** (driver `:34`, `:304`); reads `od.get("harm_obs_a")` at `:200` | **No** -- norm statistic, rank-blind |
| `v3_exq_501_sd035_amygdala_analog_*` | SD-035 | `z_harm_a_dim` config only | No |
| `v3_exq_760`, `v3_exq_939a` | MECH-303 | `\|\|z_harm_a\|\|` threshold gate | **No** -- norm |
| `v3_exq_262_mech220_harm_hub`, `v3_exq_260_sd020_harm_surprise_pe`, `v3_exq_445_sd032b_dacc_analog` | SD-011 / SD-020 / MECH-258 | norm / scalar | No |

Prior work, from `substrate_queue.json` entry **`sd_zharm_a_warmup_optimizer_group`**
(`affected_completed_runs_candidates_2026_09_18`), which this spike's STOP-CHECK should have found
and did not. It classifies candidates into `vector_or_channel_readers`
(`v3_exq_906_full_stack_observational_fishtank.py` -- `z_harm_a` recorded per tick as a CORE_CHANNEL),
`norm_readers_low_impact` (`v3_exq_1018`, `v3_exq_1015`) and `config_dim_only_not_affected`
(`v3_exq_724`, `v3_exq_728`, `v3_exq_728b`, `exq885_mech426_velocity_baseline`). That list was
derived for the **trainer** defect; it applies unchanged to the **construction** defect, because
both bound the same quantity. **`v3_exq_906` is the one VECTOR reader identified anywhere in either
sweep** and is the run /governance should look at first.

**Conclusion, restated at the strength the evidence supports:** across the population in 4a, 4e and
the prior candidate list, **no completed run's pre-registered criterion is arithmetically
invalidated by the rank-2 finding** -- every `z_harm_a`-touching DV found is a norm or scalar
statistic. The live exposure is the construct-validity issue in 4c and the vacuity issue in 4d.

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
- **Risk:** changes `harm_obs_a`'s **shape**, which is the RNG-hazardous class (5d route 1) --
  **but the repo already contains the pattern that neutralises it** (5d, "the dedicated-generator
  precedent"). With that pattern applied, C1's only differentiating risk against C2 disappears.

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
- **Risk:** keeps 50 dims, so it is **RNG-shape-neutral without needing any mitigation** (5d). The
  first draft of this doc treated that as C2's decisive technical advantage over C1; the
  dedicated-generator precedent in 5d means it is an advantage of convenience, not of kind.

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

`causal_grid_world.py` uses **one** generator for env dynamics, `self._rng =
np.random.default_rng(seed)` (`:1604`), at **43 call sites** (`grep 'self\._rng\.'`, comment lines excluded) including hazard placement (`:4239`,
`:4283-4284`), movement failure (`:2915`), scheduled limb damage (`:3156`), external hazards
(`:3201`), transients (`:3338`) and SD-048 autonomic noise (`:5097`). `reset()` does **not** reseed
it, so a desynchronisation persists for the life of the env, not just the episode. Two distinct ways
a construction change desynchronises it:

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

**The dedicated-generator precedent (added post-red-team, and it changes the C1-vs-C2 balance).**
Route 1 is **avoidable**, and the repo already solved this exact problem once. `causal_grid_world.py:1438`
creates a second generator for trajectory telemetry, with the comment at `:1433-1434`:

> *"`_traj_pair_rng` is separate from `self._rng` to preserve bit-identity of env dynamics when
> telemetry is ON vs OFF."*

Routing SD-048's `standard_normal(size=harm_obs_a.shape)` draw to a dedicated
`_interoceptive_noise_rng` seeded the same way would make the autonomic-noise draw count
**irrelevant to env dynamics**, and C1's shape change would then be RNG-neutral like C2's. That is a
small, well-precedented change -- but it is **itself** a bit-identity break for any existing run
with `interoceptive_noise_enabled=True`, so it must be part of the same default-off flag, not a
separate "harmless tidy-up". Note that `interoceptive_noise_enabled` defaults to `False`
(`autonomic_noise_enabled` defaults `True` but is gated by the master), so the affected population
is small and enumerable -- which is what makes this tractable rather than a second regression.

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

### 6a. Relationship to the existing `sd_zharm_a_warmup_optimizer_group` entry -- sibling, not duplicate

`substrate_queue.json` already carries `sd_zharm_a_warmup_optimizer_group`
(`status_phase: validation_pending`, `severity: degrading`, updated 2026-09-18): the affective
encoder has **no optimizer group** in the `_train_all_on_agent` warmup, so `z_harm_a` is a frozen
random projection. That is the **trainer** lever and is the "build the trainer fix now" half of the
2026-09-18 user decision. The entry proposed below is the **env-construction** lever -- the "scope
the env fix first" half. They are genuinely different levers on the same bottleneck and neither
substitutes for the other: that entry's own `severity_note_2026_09_18` says it outright --
*"harm_obs_a has exact rank 2 (sec 4a), so no amount of encoder training adds d.o.f. the input does
not carry."* Training an encoder on a rank-2 input cannot manufacture rank; enriching the input
without a trainable encoder leaves a frozen random projection of a richer signal. **Both are
needed, and the sequencing the user already chose (trainer now, env scoped) is the right one.**
`sd_id: harm-obs-a-rank2-enrichment` is collision-free against all 185 existing entries.

```json
{
  "sd_id": "harm-obs-a-rank2-enrichment",
  "title": "harm_obs_a is structurally rank 2 on the default path: two scalars broadcast over 25 dims each, capping every z_harm_a readout at 2 d.o.f.",
  "node_class": "puzzle (known rules)",
  "status": "PROPOSED_BY_SCOPING_SPIKE_2026_09_18__decision_owed__not_ratified__see_design_doc_section_6_for_the_three_options",
  "status_phase": "build_owed",
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
  "implementation_hint": "Add a default-off env flag harm_obs_a_construction ('scalar_broadcast' default | 'multiscale_bank'). Multiscale bank = K EMAs of hazard_at_agent and resource_at_agent at K time constants, emitting 2K dims; wire latent.harm_obs_a_dim = 2K in config.py following the SD-022 precedent at config.py:8862-8864. OFF path must be BIT-IDENTICAL including the emitted shape (50,), because SD-048 autonomic noise draws standard_normal(size=harm_obs_a.shape) off the SHARED env RNG (causal_grid_world.py:5097) and reset() does not reseed it -- a shape change desynchronises hazard placement and every other stochastic element at the same seed, permanently. In the ON arm, route that draw to a dedicated generator following the _traj_pair_rng precedent (causal_grid_world.py:1433-1441), inside the SAME flag, so the shape change stops being an env-dynamics perturbation. Comparisons spanning the flag are NOT fixed-seed comparable under any design; the flag must enter the arm fingerprint so pre-change baselines are refused for reuse, and any validating experiment mints its own baseline in-line. SIBLING ENTRY: sd_zharm_a_warmup_optimizer_group is the TRAINER lever on the same bottleneck -- neither substitutes for the other.",
  "metric_trajectory": {
    "primary_metric": "numerical_rank(harm_obs_a) ON THE DEFAULT PATH (limb_damage_enabled=False), over a >=500-tick rollout",
    "primary_metric_description": "Numerical rank of the affective observation as emitted by the DEFAULT configuration. Bounds the information any z_harm_a readout -- norm or trained head -- can carry about the world. Scoped to the default path on purpose: the SD-022 body path already reaches numerical rank 5 / 4 free dimensions, so an unscoped rank target would be satisfied by flipping an existing flag and would not discriminate this entry at all.",
    "direction": "higher_is_better",
    "target": "numerical_rank >= 4 ON THE DEFAULT PATH, AND at least two distinguishable time constants (SD-019 wind-up-vs-recovery), AND EXQ-106's lag-10 autocorrelation criterion (>0.30) still met at the slow tau",
    "current_blocker": "Default path emits two scalars at ONE time constant (causal_grid_world.py:3037-3038, since ree-v3 2fbf5d62, 2026-03-28)",
    "observations": [
      "2026-04-08 EXQ-241b: r2_s_to_a = 0.996 on the legacy path -- the redundancy, measured empirically",
      "2026-08-11 V3-EXQ-917: safe/unsafe AUC ~0.500 under SD-022 damage sourcing vs up to 0.969 under legacy proximity sourcing -- the two paths are not interchangeable readouts",
      "2026-09-18 SD-086 probe (GFLAG-0348): singular values [22.597, 6.698, 0, 0]; numerical rank EXACTLY 2; z_harm_a 97.1% variance in PC1",
      "2026-09-18 this spike: SD-022 body path is 7-dim with 4 FREE dimensions but numerical rank 5 (mean/residual_pain are linear in limb_damage[4]; max() is not in their span); Q-080 effort injection and the MECH-303 proximity EMA add no rank; EXQ-178b/198/323a all run at harm_history_len=0, which SD-011 what_would_answer (i) classifies as VACUOUS"
    ],
    "prediction": "A K=5 multiscale bank yields rank 10 with lag-10 autocorrelation preserved at the slow taus, so EXQ-106's temporal-persistence criterion continues to pass while SD-019's nonredundancy criterion becomes non-trivially testable on the DEFAULT path for the first time."
  },
  "validation_experiment": null,
  "added_session": "metaworker-science-20260918-sd011-harm-obs-a-rank2-spike",
  "added_utc": "2026-09-18T19:51:24Z",
  "origin": "Scoping spike off GFLAG-0348 / SD-086 refusal, under the 2026-09-18T19:19:21Z user decision 'Build the trainer fix now; scope the env fix first'. Design doc red-teamed in-session (verdict NON-BLOCKING-FINDINGS; five material corrections applied, recorded in section 10). PROPOSED ONLY -- not applied; /governance ratifies."
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

- **Option 1 -- Build C1 (multiscale bank), default-off.** ~1 session, plus the dedicated-generator
  change of 5d inside the same flag. Gives the **default** path a substrate on which SD-019's
  nonredundancy and SD-020's surprise-vs-magnitude are testable for the first time. Cost: the
  shape-change RNG hazard must be handled exactly as 5d/5e specify, and every ON-arm experiment
  mints its own baseline. **This session's recommendation**, because it is the only option that
  addresses the biology's *unmet* requirements (3a) rather than the one it already meets.
- **Option 2 -- Do not build; scope-note instead.** Route all future SD-011-family work to the
  SD-022 body path and take the three corrections in 6b. **Zero substrate risk, zero comparability
  break, and it is the honest option if the answer is "we are not going to run this family again
  soon".** Weaker: 4 free dimensions is still below what SD-020/MECH-258 need, and it leaves the
  default path degraded and the architecture doc still wrong.
- **Option 3 -- Build C2 (allocentric exposure map).** Matches the written architecture spec and is
  RNG-shape-neutral *without* the 5d mitigation. **This session recommends against it** on the
  biology (3a): it re-introduces a spatial map into the pathway whose defining property is that it
  has none. Stated plainly so the recommendation can be attacked at its weakest joint: **the
  strongest case for Option 3 is that it is the only option whose correctness argument does not
  depend on this doc's reading of the biology.** If the biology reading in 3a is wrong, Option 3 is
  right and Option 1 is a detour.

### 6b. Owed regardless of which option is chosen

These are corrections, not builds. None touches the substrate and none is blocked on the decision:

1. **SD-011 `what_would_answer`** -- correct the false statement that its four validated results
   were all at `harm_history_len=10` (4d finding 2), and make the sourcing-mode + `harm_history_len`
   declaration that clause (i)/(iii) already require actually enforced on the four runs.
2. **SD-022 `functional_restatement`** -- correct the sentence describing the legacy path as
   "structurally identical to harm_obs with a slower time constant"; that describes the
   **pre-2026-03-28** construction (3b).
3. **`docs/architecture/sd_011_dual_nociceptive_streams.md:73`** -- `harm_obs_a = EMA(harm_obs_s,
   tau=10-30_steps)` has not described the code since 2026-03-28. Either the doc or the code is
   wrong, and section 6's decision determines which; until then the doc should carry a note.

**Recommendation: Option 1, with 6b done regardless of which option is chosen.**

---

## 7. Governance registration

The chip said to register the finding "if no flag already covers it (the SD-086 session raised one
-- check first, do not duplicate)". Checked: **GFLAG-0348** (open, `evidence_discrepancy`, claims
`SD-086` + `SD-011`, raised 2026-09-18T18:52:46Z by `metaworker-science-20260918-sd086-zharma-readout`)
carries the rank-2 measurement and names the SD-011 second-order finding explicitly. **No new flag
was raised.**

**GFLAG-0350 raised (`stale_note`, claims SD-011 / SD-019 / SD-022, 2026-09-18).** The section 4d
finding is genuinely NEW and is a different *type* of finding on different claims, so it is not a
duplicate of GFLAG-0348: it records that SD-011's `what_would_answer` misstates the
`harm_history_len` regime of its own four validated results, that applying its own clause (i) makes
two of them vacuous, and that SD-022's `functional_restatement` describes the pre-2026-03-28
construction. It explicitly proposes no `evidence_direction` for any run.

Two amendments for /governance to make **on GFLAG-0348 when it adjudicates** -- as widenings of
that flag, not as a second near-duplicate flag (STEWARD D-006 exists precisely to catch that shape):

1. **Widen `claim_ids`** from `[SD-086, SD-011]` to include **SD-019, SD-020, SD-022, MECH-258** --
   sections 3a/3b establish that each carries an unmet requirement traceable to this construction.
2. **Record the sourcing-mode split** (section 4a) and the two `stale_note`-class corrections:
   SD-022's `functional_restatement` (3b) and **SD-011's `what_would_answer` misstatement about its
   own `harm_history_len` regime (4d finding 2)**. Either is cleanly separable as its own
   `stale_note` flag; both are recorded here rather than raised so that this session does not
   pre-empt that call. The SD-011 one is the more consequential: it is a claim asserting something
   false about the provenance of its own supporting evidence.
3. **Note the vacuity finding (4d).** Applying SD-011's clause (i) to EXQ-178b/198/323a is a
   disposition for /governance, not for this spike; it is stated as a measured fact about the
   drivers (`:158`, `:196`, `:326` all default `harm_history_len=0`) with no `evidence_direction`
   proposed.

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

## 9. Red-team record

Reviewed in-session by a foreground adversarial red-team pass over the committed first draft
(`REE_assembly b61eacdad7`), tasked to verify every load-bearing claim against the live repo.

**Verdict: NON-BLOCKING-FINDINGS.** The headline verdict (section 1/3c, "it is a regression
introduced by `2fbf5d62`") was independently re-verified from `git show db45993a` / `git show
2fbf5d62` and **held**, as did the producer-site quote, the exhaustive writer sweep, the two-path
split, the architecture-spec divergence, the sourcing-mode table, the EXQ-463 fixture finding, the
norm-based-criteria finding, the RNG mechanism, GFLAG-0348's contents, and scope compliance
(1 file, doc only).

Five material findings were raised and **all five are incorporated above**, each re-verified by this
session before acceptance rather than taken on the reviewer's word:

| # | Finding | Where fixed |
|---|---|---|
| 1 | The proposed acceptance target `rank >= 4` is already met by flipping `limb_damage_enabled` -- and the body path's *numerical* rank is 5, not 4 | 2c, 6 (target now scoped to the DEFAULT path) |
| 2 | SD-011's `what_would_answer` clause (i) was omitted; applied, it calls EXQ-178b/198/323a **vacuous**, and the claim misstates its own `harm_history_len` regime | **new 4d** |
| 3 | Section 4's six-claim method under-scoped a universally-stated conclusion | 4 method note, **new 4e** |
| 4 | STOP-CHECK missed `substrate_queue` entry `sd_zharm_a_warmup_optimizer_group` and its pre-existing affected-runs candidate list | 0, 4e, **new 6a** |
| 5 | `status_phase: "decision_owed"` was an invented enum value | 6 (now `build_owed`) |

Minor corrections also applied: the `_traj_pair_rng` dedicated-generator precedent (which materially
weakens C2's advantage over C1 -- 5a/5b/5d), `scoring_excluded` flags and the EXQ-917 both-paths
relabel (4a), the MECH-258 citation attribution (3a), the RNG call-site count (53, not 54), and
line-number drift at `:3049-3053`, `:4144`, `:5097`. The call-site figure was corrected twice: the
first draft's 54 counted every `self._rng` mention (assignment and a docstring line included) and
the red-team's 53 subtracted only the assignment; the accurate count of `self._rng.` call-site lines
excluding comments is **43**.

**Not accepted:** nothing. The red-team raised no finding this session judged wrong.

---

## 10. Reproduction

All read-only, all from `REE_Working` on ree-cloud-5 at the heads named in the header:

```bash
BASE=/Users/dgolden/REE_Working
# 2a/2b/2c -- producer site, the two later writers, the two-path branch
sed -n '3026,3085p'  $BASE/ree-v3/ree_core/environment/causal_grid_world.py
sed -n '4136,4165p'  $BASE/ree-v3/ree_core/environment/causal_grid_world.py
sed -n '8855,8870p'  $BASE/ree-v3/ree_core/utils/config.py
# 2c -- the 4-free-vs-5-numerical rank of the SD-022 body vector
python3 -c "import numpy as np; r=np.random.default_rng(0); d=r.random((2000,4)); M=np.column_stack([d,d.max(1),d.mean(1),np.clip(d.sum(1)*0.25,0,1)]); print(np.round(np.linalg.svd(M,compute_uv=False),4), np.linalg.matrix_rank(M))"
# 2d/5d -- SD-048 noise, and the single shared generator
sed -n '5006,5128p'  $BASE/ree-v3/ree_core/environment/causal_grid_world.py
grep 'self\._rng\.' $BASE/ree-v3/ree_core/environment/causal_grid_world.py | grep -vc '^\s*#'  # 43
sed -n '1430,1442p' $BASE/ree-v3/ree_core/environment/causal_grid_world.py   # _traj_pair_rng precedent
# 2e -- provenance
git -C $BASE/ree-v3 log --format='%h %ad %s' --date=short -S 'harm_obs_a_ema' -- ree_core/environment/causal_grid_world.py
git -C $BASE/ree-v3 show 2fbf5d62 --stat
git -C $BASE/ree-v3 show db45993a -- ree_core/environment/causal_grid_world.py
# 4a -- evidence entries, then sourcing mode per driver
python3 -c "import json;d=json.load(open('$BASE/REE_assembly/evidence/experiments/claim_evidence.v1.json'));print([ (e['claim_id'],e.get('run_id'),e.get('evidence_direction')) for e in d['entries'] if e.get('claim_id') in {'SD-011','SD-019','SD-020','SD-022','SD-086','MECH-258'} and str(e.get('evidence_class','')).startswith('exp')])"
grep -c 'limb_damage_enabled=True' $BASE/ree-v3/experiments/v3_exq_178b_sd011_dual_stream_dissociation.py   # 0
grep -c 'limb_damage_enabled=True' $BASE/ree-v3/experiments/v3_exq_323a_sd019_harm_nonredundancy.py         # 5
# 4d -- harm_history_len defaults to 0 in all three
grep -n 'AffectiveHarmEncoder(' -A2 $BASE/ree-v3/experiments/v3_exq_178b_sd011_dual_stream_dissociation.py
grep -n 'AffectiveHarmEncoder(' -A2 $BASE/ree-v3/experiments/v3_exq_198_sd011_dual_stream_stability.py
grep -n 'AffectiveHarmEncoder(' -A2 $BASE/ree-v3/experiments/v3_exq_323a_sd019_harm_nonredundancy.py
sed -n '206,212p' $BASE/ree-v3/ree_core/latent/stack.py
# 4e -- the prior candidate list this STOP-CHECK missed
python3 -c "import json;d=json.load(open('$BASE/REE_assembly/evidence/planning/substrate_queue.json'));print([i for i in d['queue'] if i['sd_id']=='sd_zharm_a_warmup_optimizer_group'][0]['affected_completed_runs_candidates_2026_09_18'])"
```
