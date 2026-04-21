# Amygdala Analogue — Literature Synthesis (2026-04-21)

Cross-cutting synthesis for the amygdala analogue implementation in ree-v3. Individual literature entries live in the per-claim directories:

- **MECH-046** (CeA mode prior, fast salience classification) — `targeted_review_connectome_mech_046/`
- **MECH-074** (BLA/CeA read/write head on valenced hippocampal map) — `targeted_review_connectome_mech_074/`

This file exists at `targeted_review_amygdala_analog/` to centralise the quantitative config defaults that inform the BLAAnalog and CeAAnalog modules being implemented under the plan at `.claude/plans/amygdala-there-is-no-concurrent-corbato.md`.

## Entries consulted

| Target | Paper | Entry | Claim | Confidence |
|---|---|---|---|---|
| BLA encoding (supplementary) | Roozendaal & McGaugh 2011, Behav Neurosci | `2026-04-21_mech_074_memory_modulation_roozendaal2011` | MECH-074 | 0.82 |
| CeA fast route (latency) | Méndez-Bértolo et al 2016, Nat Neurosci | `2026-04-21_mech_046_fast_pathway_mendezbertolo2016` | MECH-046, MECH-074 | 0.88 |
| CeA fast route (bounds) | Pessoa & Adolphs 2010, Nat Rev Neurosci | `2026-04-21_mech_046_many_roads_pessoaadolphs2010` | MECH-046, MECH-074 | 0.72 |
| BLA retrieval bias | LaBar & Cabeza 2006, Nat Rev Neurosci | `2026-04-21_mech_074_retrieval_bias_labar2006` | MECH-074 | 0.72 |
| BLA remap (reconsolidation) | Nader, Schafe & LeDoux 2000, Nature | `2026-04-21_mech_074_reconsolidation_nader2000` | MECH-074 | 0.80 |
| BLA remap (place cells) | Moita et al 2004, J Neurosci | `2026-04-21_mech_074_place_cell_remap_moita2004` | MECH-074 | 0.78 |
| BLA encoding (canonical; pre-existing) | McGaugh 2004, Annu Rev Neurosci | `2026-04-02_mech_074_amygdala_consolidation_mcgaugh2004` | MECH-074, MECH-073 | 0.82 |
| BLA retrieval (canonical; pre-existing) | Dolcos, LaBar & Cabeza 2004, fMRI | `2026-04-02_mech_074_amygdala_mtl_fmri_dolcos2004` | MECH-074 | — |

## Quantitative defaults by sub-behavior

Assumptions: 1 simulation step ≈ 100 ms biological time. `||z_harm_a||` is normalised to roughly [0, 1].

### BLAAnalog — encoding gain (MECH-074a)

From Roozendaal & McGaugh 2011 (supplemented by McGaugh 2004):

- `encoding_gain_max`: **2.5x** (peak multiplier on HippocampalModule write strength)
- `encoding_gain_floor`: **1.0** (no suppression below threshold)
- `arousal_threshold_on`: **||z_harm_a|| ≥ 0.4** (below: flat baseline 1.0)
- `arousal_peak`: **||z_harm_a|| ≈ 0.7** (inverted-U — gain falls off above peak)
- `post_event_window_steps`: **~18 000** (~30 min biological)
- `window_half_life_steps`: **~3 600** (~6 min biological)
- **Shape**: inverted-U over arousal magnitude, decaying exponentially in time after event onset.

### BLAAnalog — retrieval bias (MECH-074b)

From LaBar & Cabeza 2006 (supplemented by Dolcos et al 2004):

- **Design decision — CRITICAL**: retrieval_bias must be a **content-selective per-trace weight vector**, NOT a scalar gain. Scalar is a named failure signature — it cannot reproduce the central/peripheral dissociation that is the hallmark of amygdala-lesion studies.
- `retrieval_bias_alpha`: **0.3 – 1.0** (per-trace weight `w_i = 1 + alpha * arousal_tag_i`)
- **Magnitude**: central/gist items retrieved ~1.3x – 2.0x relative to neutral baseline.
- **Zero-sum compensation**: untagged traces suppressed by ~10 – 30% (optional; simpler implementation may omit).
- **Persistence**: non-transient. Arousal tag must be written **at encoding** and consulted at every retrieval; BLA contribution *grows* with trace age (amygdala-MTL connectivity increases from 20 min to 1 week).
- **Implementation implication**: HippocampalModule needs a per-trace `arousal_tag` field that BLAAnalog writes at encoding time; BLA retrieval_bias at readout consults this tag. This is a second data-flow beyond the encoding_gain multiplier.

### CeAAnalog — fast salience classification → mode prior (MECH-046)

From Méndez-Bértolo et al 2016, bounded by Pessoa & Adolphs 2010:

- **Fast-route latency**: emit `mode_prior` within **1 – 2 sim steps** of `z_harm_a_coarse` crossing threshold (maps to ~75 ms biological).
- **Cortical comparison**: AIC/dACC analogues take ~5 – 10 sim steps (~400 ms) for comparable discrimination. **Fast:slow ratio ≈ 5:1**.
- **Input projection**: gate on `||LowFreq(z_harm_a)||_1 > theta_cea_fast`, NOT the full `z_harm_a` vector. Coarse / magnitude-only projection — trades specificity for speed.
- `theta_cea_fast`: tune so fast gate fires on ~70 – 80% of true harm events and ~25 – 30% of arousing-but-neutral events (deliberately high false-positive rate; corrected by cortical override).
- **Selectivity constraint**: CeA must fire on harm-affective valence, not generic arousal. Calibration test: CeA should NOT fire on arousing non-threat stimuli.
- **Gating placement**: `mode_prior` and `fast_prime` added **pre-softmax** in SalienceCoordinator as additive log-odds bias on the harm channel. NOT post-softmax multiplicative.
- **Bias magnitude ceiling**: `|fast_prime_max| ≤` max cortical AIC/dACC log-odds adjustment. Must be overridable.

### CeAAnalog — fast subcortical priming (MECH-074c)

From Pessoa & Adolphs 2010 (many-roads framing):

- **Override window**: cortical signals must be able to flip CeA `fast_prime` within **5 – 10 sim steps** (~300 – 400 ms). After this window, if cortical confirmation is absent, `fast_prime` decays toward baseline.
- `fast_prime_decay_tau_steps`: **3 – 5** (~150 – 250 ms biological half-life if unconfirmed).
- **No direct motor gating**: CeAAnalog writes only to SalienceCoordinator. Motor-level effects are mediated by downstream consumers of the mode vector. The inline urgency interrupt at `agent.py:869-886` is a **separate** path and stays unchanged in this pass (per plan).
- **Coordination principle**: CeA biases a coordinator that also takes cortical input. Never unilateral.

### BLAAnalog — remap signal on PE spike (MECH-074d)

From Nader, Schafe & LeDoux 2000 + Moita et al 2004:

- **PE threshold**: emit `remap_signal` when `||z_harm_a - E2_harm_a_pred||` exceeds **~1 standard deviation of the running harm-PE distribution** AND a predictor-attribution head flags at least one candidate latent code. Both conditions required.
- **Attribution gating — CRITICAL**: the **contextual-vs-auditory dissociation** in Moita 2004 (Z = -1.36 vs -0.34, p = 0.02) rules out a broadcast architecture. BLAAnalog MUST consult a predictor-identification step before emitting remap_signal — only codes with non-zero attribution to the harm-PE are targeted.
- **Shape**: step-function at the per-code level (binary per code), NOT graded. Population looks graded only because the gate fires on only ~30 – 40% of predictor-candidate codes.
- **Remap amplitude**: perturb roughly **one-third** of selected latent codes (Moita: training-box correlation dropped 0.57 → 0.39, ~30-35% overwrite). Not wholesale replacement.
- **Decision time constant**: fires fast (within minutes of PE biological = O(10³) sim steps at 100 ms/step).
- **Plasticity gate window**: 4 – 6 hours biological (~1.4e5 – 2.2e5 sim steps) — spans multiple REE episodes, not a single step. This is relevant if/when we add learnable components; for the initial non-trainable pass, the remap_signal just fires and HippocampalModule consumes it.

## Mapping to config dataclasses (preview)

These values feed `BLAConfig` and `CeAConfig` in `ree_core/utils/config.py`:

```python
@dataclass
class BLAConfig:
    enabled: bool = False                          # master switch
    encoding_gain_max: float = 2.5                 # Roozendaal 2011
    encoding_gain_arousal_threshold: float = 0.4
    encoding_gain_arousal_peak: float = 0.7
    encoding_gain_window_steps: int = 18000
    encoding_gain_half_life_steps: int = 3600
    retrieval_bias_alpha: float = 0.6              # midpoint of 0.3-1.0
    retrieval_bias_compensation: float = 0.0       # start at 0; enable 0.1-0.3 later
    retrieval_tag_at_encoding: bool = True         # required per LaBar 2006
    remap_pe_sigma_threshold: float = 1.0          # units of running PE stdev
    remap_code_fraction: float = 0.33              # Moita 2004
    remap_requires_attribution: bool = True        # Moita 2004

@dataclass
class CeAConfig:
    enabled: bool = False                          # master switch
    fast_route_threshold: float = 0.5              # theta_cea_fast on LowFreq(z_harm_a)
    fast_route_input_is_lowfreq: bool = True       # Méndez-Bértolo 2016
    mode_prior_log_odds_max: float = 0.8           # bounded below AIC/dACC ceiling
    fast_prime_decay_tau_steps: int = 4            # 3-5 range
    fast_prime_override_window_steps: int = 8      # 5-10 range; after, decays
    pre_softmax_additive: bool = True              # NOT post-softmax multiplicative
```

## Open risks / follow-ups

1. **BLA retrieval_bias requires encoding-time tag writes into HippocampalModule.** This is a broader wiring change than a simple read-path multiplier. If HippocampalModule does not currently carry a per-trace arousal_tag, we need to add one. Check at implement-substrate time.
2. **Remap attribution head**: `BLAAnalog.remap_signal` requires a predictor-identification step. For the initial pass we can approximate by picking codes whose contribution to the harm-PE exceeds a threshold; a learnable attribution head is deferred.
3. **Cortical override calibration**: CeA `fast_prime` magnitude ceiling must stay ≤ AIC/dACC log-odds ceiling. Need to check `SalienceCoordinatorConfig` for the current AIC ceiling and set `mode_prior_log_odds_max` accordingly.
4. **Q-036 escapability placeholder**: CeAAnalog carries an `escapability_hint` parameter as a no-op placeholder so MECH-219 can wire in later without refactor (per plan).
5. **SD-032b dACC FAIL** (`v3_exq_445`): affective PE path is currently underperforming. EXQ-A/B acceptance criteria must be calibrated against this — don't expect the mode-prior ablation to produce clean signals if upstream PE is broken.

## Citations

Full record.json + summary.md per entry at the paths listed in the table above.
